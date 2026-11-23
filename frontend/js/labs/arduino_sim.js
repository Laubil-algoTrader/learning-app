/**
 * "Mini Arduino": runs a practical subset of Arduino C++ in the browser.
 *
 * The sketch is translated to JavaScript generator functions so that delay()
 * and the passage of CPU time can pause the program while the circuit
 * simulator advances. No compiler and no network are needed.
 *
 * Supported: setup()/loop(), user functions with parameters and return values,
 * int/long/float/bool/byte/String variables, arrays, #define, if/for/while/
 * do/switch, pinMode, digitalWrite/Read, analogRead/Write, delay,
 * delayMicroseconds, millis, micros, map, constrain, min, max, abs, random,
 * Serial.begin/print/println.
 *
 * Known differences with a real board: there is no integer division (7/2 is
 * 3.5) unless the value is cast with (int), and no libraries (Wire, Servo, WiFi).
 */

const TYPES =
  "(?:long\\s+long|long|int|short|float|double|bool|boolean|byte|char|String|word|uint8_t|uint16_t|uint32_t|uint64_t|int8_t|int16_t|int32_t|int64_t|size_t)";

export const SUPPORTED = [
  "pinMode", "digitalWrite", "digitalRead", "analogRead", "analogWrite", "delay", "delayMicroseconds",
  "millis", "micros", "map", "constrain", "min", "max", "abs", "random", "randomSeed", "pow", "sqrt", "sq",
  "Serial.begin", "Serial.print", "Serial.println",
];

export class SketchError extends Error {
  constructor(message, line = null) {
    super(message);
    this.line = line;
  }
}

/* ------------------------------------------------------------------ */
/* Lexical helpers                                                     */
/* ------------------------------------------------------------------ */

/** Remove comments (keeping line breaks) and swap string/char literals for placeholders. */
function protect(src) {
  let out = "";
  const strs = [];
  let i = 0;
  while (i < src.length) {
    const c = src[i];
    const d = src[i + 1];
    if (c === "/" && d === "/") {
      while (i < src.length && src[i] !== "\n") i++;
      continue;
    }
    if (c === "/" && d === "*") {
      const j = src.indexOf("*/", i + 2);
      const stop = j < 0 ? src.length : j + 2;
      out += src.slice(i, stop).replace(/[^\n]/g, " ");
      i = stop;
      continue;
    }
    if (c === '"' || c === "'") {
      let j = i + 1;
      while (j < src.length && src[j] !== c && src[j] !== "\n") {
        if (src[j] === "\\") j++;
        j++;
      }
      if (src[j] !== c) {
        throw new SketchError("Falta cerrar las comillas.", lineAt(src, i));
      }
      strs.push(src.slice(i, j + 1));
      out += `__STR${strs.length - 1}__`;
      i = j + 1;
      continue;
    }
    out += c;
    i++;
  }
  return { code: out, strs };
}

function lineAt(text, pos) {
  let n = 1;
  for (let k = 0; k < pos && k < text.length; k++) if (text[k] === "\n") n++;
  return n;
}

/** Index of the bracket matching the one at `open` (which must be ( [ or {). */
function matchForward(text, open) {
  const pairs = { "(": ")", "[": "]", "{": "}" };
  const o = text[open];
  const cl = pairs[o];
  let depth = 0;
  for (let k = open; k < text.length; k++) {
    if (text[k] === o) depth++;
    else if (text[k] === cl) {
      depth--;
      if (depth === 0) return k;
    }
  }
  return -1;
}

/** Index of the "{" matching the "}" at `close`. */
function matchBackward(text, close) {
  let depth = 0;
  for (let k = close; k >= 0; k--) {
    if (text[k] === "}") depth++;
    else if (text[k] === "{") {
      depth--;
      if (depth === 0) return k;
    }
  }
  return -1;
}

/** Report the first unbalanced bracket with its line, like a compiler would. */
function checkBalance(code) {
  const stack = [];
  const close = { ")": "(", "]": "[", "}": "{" };
  const names = { "(": "paréntesis", "[": "corchete", "{": "llave" };
  const art = { "(": "un", "[": "un", "{": "una" };
  for (let k = 0; k < code.length; k++) {
    const c = code[k];
    if (c === "(" || c === "[" || c === "{") stack.push([c, k]);
    else if (c in close) {
      const top = stack.pop();
      if (!top || top[0] !== close[c]) {
        throw new SketchError(`Sobra un «${c}» o falta abrir ${art[close[c]]} ${names[close[c]]}.`, lineAt(code, k));
      }
    }
  }
  if (stack.length) {
    const [c, k] = stack[stack.length - 1];
    throw new SketchError(`Falta cerrar ${art[c]} ${names[c]} «${c}» ${c === "{" ? "abierta" : "abierto"} en esta línea.`, lineAt(code, k));
  }
}

/**
 * JavaScript would silently accept a missing semicolon; the Arduino compiler
 * does not, and it is the most common beginner error. Two heuristics:
 *  1. a statement right before a closing brace: `{ x = 3 }`
 *  2. a line that ends a statement without ";" while the next line starts a new one.
 */
function checkSemicolons(code) {
  const missing = (pos) => {
    throw new SketchError("Falta un punto y coma (;) al final de esta línea.", lineAt(code, pos));
  };
  // 1. statement directly before a closing brace of a code block
  const braceIsInit = [];
  let segStart = 0;
  for (let k = 0; k < code.length; k++) {
    const c = code[k];
    if (c === "{") {
      let b = k - 1;
      while (b >= 0 && /\s/.test(code[b])) b--;
      braceIsInit.push(code[b] === "=" || code[b] === "," || code[b] === "(" || code[b] === "{");
      segStart = k + 1;
    } else if (c === "}") {
      const init = braceIsInit.pop();
      const seg = code.slice(segStart, k).trim();
      if (!init && seg && !/[:;]$/.test(seg) && !/^(case\b|default\b)/.test(seg)) missing(segStart + code.slice(segStart, k).search(/\S/) + seg.length - 1);
      segStart = k + 1;
    } else if (c === ";") {
      segStart = k + 1;
    }
  }
  // 2. line endings
  const lines = code.split("\n");
  let offset = 0;
  const starts = [];
  for (const ln of lines) { starts.push(offset); offset += ln.length + 1; }
  const control = /^(if|else|for|while|do|switch|case|default)\b/;
  for (let i = 0; i < lines.length; i++) {
    const cur = lines[i].trim();
    if (!cur || cur.startsWith("#")) continue;
    if (!/([A-Za-z0-9_\])\]]|\+\+|--)$/.test(cur)) continue;
    if (control.test(cur) || /^\}\s*else\b/.test(cur)) continue;
    let j = i + 1;
    while (j < lines.length && !lines[j].trim()) j++;
    if (j >= lines.length) continue;
    const next = lines[j].trim();
    if (/^[{)\].?:+\-*/%&|^=<>!,]/.test(next)) continue; // block or continuation
    if (/^(void|int|long|unsigned|float|double|bool|boolean|byte|char|String|const|static)\b[^;=]*\)$/.test(cur)) continue; // function header, brace below
    missing(starts[i] + lines[i].length - 1);
  }
}

/* ------------------------------------------------------------------ */
/* Translation                                                         */
/* ------------------------------------------------------------------ */

function cleanParams(params) {
  return params
    .split(",")
    .map((x) => x.trim())
    .filter((x) => x && x !== "void")
    .map((x) => {
      const m = x.replace(/\[[^\]]*\]/g, "").replace(/[&*]/g, " ").match(/([A-Za-z_]\w*)\s*(=.*)?$/);
      return m ? m[1] + (m[2] ? " " + m[2] : "") : "_";
    })
    .join(", ");
}

/** Wrap every call to a user function as (yield* name(...)) so it can pause. */
function wrapUserCalls(code, names) {
  if (!names.length) return code;
  const re = new RegExp(`\\b(${names.join("|")})\\s*\\(`, "g");
  const hits = [];
  let m;
  while ((m = re.exec(code))) hits.push({ at: m.index, open: m.index + m[0].length - 1 });
  for (let h = hits.length - 1; h >= 0; h--) {
    const { at, open } = hits[h];
    if (/function\*\s*$/.test(code.slice(Math.max(0, at - 12), at))) continue; // the definition itself
    if (/\.\s*$/.test(code.slice(Math.max(0, at - 2), at))) continue; // obj.method(
    const close = matchForward(code, open);
    if (close < 0) continue;
    code = code.slice(0, at) + "(yield* " + code.slice(at, close + 1) + ")" + code.slice(close + 1);
  }
  return code;
}

/** Give every loop body a CPU tick so busy loops still let time pass. */
function instrumentLoops(code) {
  // do { ... } while (...);
  code = code.replace(/\bdo\s*\{/g, "do { yield* __tick();");
  const re = /\b(while|for)\s*\(/g;
  const hits = [];
  let m;
  while ((m = re.exec(code))) hits.push({ at: m.index, open: m.index + m[0].length - 1 });
  for (let h = hits.length - 1; h >= 0; h--) {
    const { at, open } = hits[h];
    const close = matchForward(code, open);
    if (close < 0) continue;
    let k = close + 1;
    while (k < code.length && /\s/.test(code[k])) k++;
    if (code[k] === "{") {
      code = code.slice(0, k + 1) + " yield* __tick();" + code.slice(k + 1);
    } else if (code[k] === ";") {
      // either `while (x);` (busy wait) or the tail of a do { } while (x);
      let b = at - 1;
      while (b >= 0 && /\s/.test(code[b])) b--;
      if (code[b] === "}") {
        const ob = matchBackward(code, b);
        if (ob >= 0 && /\bdo\s*$/.test(code.slice(Math.max(0, ob - 8), ob))) continue;
      }
      code = code.slice(0, k) + "{ yield* __tick(); }" + code.slice(k + 1);
    } else {
      // single statement body: wrap it up to the next ; at depth 0
      let depth = 0;
      let e = k;
      for (; e < code.length; e++) {
        const c = code[e];
        if (c === "(" || c === "[" || c === "{") depth++;
        else if (c === ")" || c === "]" || c === "}") depth--;
        else if (c === ";" && depth === 0) break;
      }
      code = code.slice(0, k) + "{ yield* __tick(); " + code.slice(k, e + 1) + " }" + code.slice(e + 1);
    }
  }
  return code;
}

/**
 * Translate an Arduino sketch into a factory: factory(runtime) -> { setup, loop }.
 * Throws SketchError with a line number for the errors we can detect up front.
 */
export function translateSketch(src) {
  let { code, strs } = protect(src.replace(/\r\n?/g, "\n"));
  checkBalance(code);
  checkSemicolons(code.replace(/^[ \t]*#[^\n]*$/gm, ""));

  // preprocessor
  code = code.replace(/^[ \t]*#\s*include[^\n]*$/gm, "");
  code = code.replace(/^[ \t]*#\s*define[ \t]+([A-Za-z_]\w*)[ \t]+([^\n]+)$/gm, "const $1 = $2;");
  code = code.replace(/^[ \t]*#[^\n]*$/gm, "");

  // forward declarations: void foo(int a);
  code = code.replace(
    new RegExp(`(^|[;{}\\n])[ \\t]*(?:static\\s+|inline\\s+)*(?:unsigned\\s+|signed\\s+)?(?:void|${TYPES})\\s+[A-Za-z_]\\w*\\s*\\([^)]*\\)\\s*;`, "g"),
    "$1"
  );

  // function definitions -> generator functions
  const userFns = [];
  code = code.replace(
    new RegExp(`(^|[;{}\\n])([ \\t]*)(?:static\\s+|inline\\s+)*(?:unsigned\\s+|signed\\s+)?(?:void|${TYPES})\\s+([A-Za-z_]\\w*)\\s*\\(([^)]*)\\)\\s*\\{`, "g"),
    (all, pre, ws, name, params) => {
      userFns.push(name);
      return `${pre}${ws}function* ${name}(${cleanParams(params)}) {`;
    }
  );
  if (!userFns.includes("setup") || !userFns.includes("loop")) {
    throw new SketchError("Todo programa de Arduino necesita las funciones void setup() { … } y void loop() { … }.");
  }

  // casts
  code = code.replace(/\(\s*(?:float|double)\s*\)\s*/g, "");
  code = code.replace(
    new RegExp(`\\(\\s*(?:unsigned\\s+)?${TYPES}\\s*\\)\\s*(\\((?:[^()]|\\([^()]*\\))*\\)|[A-Za-z_][\\w.]*(?:\\[[^\\]]*\\])?(?:\\([^()]*\\))?|\\d+(?:\\.\\d+)?)`, "g"),
    "Math.trunc($1)"
  );

  // declarations
  code = code.replace(/\bString\s+([A-Za-z_]\w*)\s*;/g, 'let $1 = "";');
  code = code.replace(
    new RegExp(`\\b(const\\s+)?(?:static\\s+|volatile\\s+)*(const\\s+)?(?:unsigned\\s+|signed\\s+)?${TYPES}\\b\\s*(?=[A-Za-z_*&])`, "g"),
    (all, c1, c2) => (c1 || c2 ? "const " : "let ")
  );
  code = code.replace(/\b(let|const)\s+\*?\s*/g, "$1 ");
  // arrays
  code = code.replace(/\b(let|const)\s+([A-Za-z_]\w*)\s*\[\s*[^\]]*\]\s*=\s*\{([^}]*)\}/g, "$1 $2 = [$3]");
  code = code.replace(/\b(let|const)\s+([A-Za-z_]\w*)\s*\[\s*([^\]]+)\]\s*;/g, "$1 $2 = new Array($3).fill(0);");
  // uninitialized scalars start at 0, like Arduino globals
  code = code.replace(/\blet\s+([A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)\s*;/g, (all, list) =>
    "let " + list.split(",").map((v) => `${v.trim()} = 0`).join(", ") + ";"
  );

  // builtins that take time
  code = code.replace(/\bdelayMicroseconds\s*\(/g, "yield* __delayUs(");
  code = code.replace(/\bdelay\s*\(/g, "yield* __delay(");
  code = code.replace(/\bSerial\s*\./g, "__Serial.");

  code = wrapUserCalls(code, userFns.filter((n) => n !== "setup" && n !== "loop").concat(["loop", "setup"]).filter((v, i, a) => a.indexOf(v) === i));
  code = instrumentLoops(code);

  // restore string literals
  code = code.replace(/__STR(\d+)__/g, (all, k) => strs[Number(k)]);

  const RUNTIME = [
    "pinMode", "digitalWrite", "digitalRead", "analogRead", "analogWrite", "millis", "micros",
    "__delay", "__delayUs", "__tick", "__Serial", "map", "constrain", "min", "max", "abs", "random",
    "randomSeed", "pow", "sqrt", "sq", "HIGH", "LOW", "INPUT", "OUTPUT", "INPUT_PULLUP", "LED_BUILTIN",
    "A0", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "PI", "DEC", "HEX", "BIN", "tone", "noTone",
  ];
  const body = `"use strict";
const { ${RUNTIME.join(", ")} } = __rt;
${code}
return { setup, loop };`;
  let factory;
  try {
    // eslint-disable-next-line no-new-func
    factory = new Function("__rt", body);
  } catch (err) {
    throw new SketchError(`Error de sintaxis: ${err.message}. Revisá punto y coma, llaves y nombres de variables.`);
  }
  return { factory, translated: body, userFns };
}

/* ------------------------------------------------------------------ */
/* Runtime                                                             */
/* ------------------------------------------------------------------ */

// CPU time charged per operation (seconds), roughly a 16 MHz ATmega328P.
const COST = { loop: 10e-6, tick: 4e-6, digital: 5e-6, analogRead: 112e-6, other: 2e-6 };
const CPU_QUANTUM = 100e-6;

/**
 * Create the program runner.
 * @param {object} io  { pinMode(pin, mode), digitalWrite(pin, v), digitalRead(pin) -> 0|1,
 *                       analogRead(pin) -> 0..1023, analogWrite(pin, 0..255), now() -> seconds,
 *                       serial(text), warn(text) }
 * @returns {{ next(): { wait: number } | { done: true } }} each next() runs until the program
 *          asks for time to pass and returns how many seconds.
 */
export function createProgram(factory, io) {
  let cpu = 0; // CPU time used since the last yield
  const now = () => io.now() + cpu;
  const charge = (s) => { cpu += s; };

  function* __tick() {
    cpu += COST.tick;
    if (cpu >= CPU_QUANTUM) { const d = cpu; cpu = 0; yield d; }
  }
  function* __delay(ms) {
    const d = cpu + Math.max(0, Number(ms) || 0) / 1000;
    cpu = 0;
    yield d;
  }
  function* __delayUs(us) {
    const d = cpu + Math.max(0, Number(us) || 0) / 1e6;
    cpu = 0;
    yield d;
  }

  const fmt = (v, base) => {
    if (typeof v === "number") {
      if (base === 16) return Math.trunc(v).toString(16).toUpperCase();
      if (base === 2) return Math.trunc(v).toString(2);
      if (typeof base === "number" && base >= 0 && base <= 8 && base !== 2) return v.toFixed(base);
      return Number.isInteger(v) ? String(v) : v.toFixed(2);
    }
    if (typeof v === "boolean") return v ? "1" : "0";
    return String(v);
  };

  let serialStarted = false;
  let warnedSerial = false;
  const serialOut = (text) => {
    if (!serialStarted && !warnedSerial) {
      warnedSerial = true;
      io.warn("Usaste Serial.print sin Serial.begin(9600) en setup(): en una placa real no aparecería nada.");
    }
    io.serial(text);
  };

  const rt = {
    HIGH: 1, LOW: 0, INPUT: "INPUT", OUTPUT: "OUTPUT", INPUT_PULLUP: "INPUT_PULLUP", LED_BUILTIN: 13,
    A0: 14, A1: 15, A2: 16, A3: 17, A4: 18, A5: 19, A6: 20, A7: 21, PI: Math.PI, DEC: 10, HEX: 16, BIN: 2,
    pinMode(pin, mode) {
      charge(COST.other);
      if (!["INPUT", "OUTPUT", "INPUT_PULLUP"].includes(mode)) throw new Error(`pinMode(${pin}, ...) necesita INPUT, OUTPUT o INPUT_PULLUP.`);
      io.pinMode(pin, mode);
    },
    digitalWrite(pin, value) { charge(COST.digital); io.digitalWrite(pin, value ? 1 : 0); },
    digitalRead(pin) { charge(COST.digital); return io.digitalRead(pin); },
    analogRead(pin) { charge(COST.analogRead); return io.analogRead(pin); },
    analogWrite(pin, value) { charge(COST.digital); io.analogWrite(pin, Math.max(0, Math.min(255, Math.trunc(Number(value) || 0)))); },
    millis() { return Math.floor(now() * 1000); },
    micros() { return Math.floor(now() * 1e6 / 4) * 4; },
    map(x, inMin, inMax, outMin, outMax) {
      return Math.trunc(((x - inMin) * (outMax - outMin)) / (inMax - inMin) + outMin);
    },
    constrain(x, a, b) { return Math.min(b, Math.max(a, x)); },
    min: Math.min, max: Math.max, abs: Math.abs, pow: Math.pow, sqrt: Math.sqrt, sq: (x) => x * x,
    random(a, b) {
      if (b === undefined) { b = a; a = 0; }
      return Math.floor(a + Math.random() * (b - a));
    },
    randomSeed() {},
    tone() { io.warn("tone() no está simulado todavía."); },
    noTone() {},
    __tick, __delay, __delayUs,
    __Serial: {
      begin() { serialStarted = true; },
      print(v, base) { serialOut(fmt(v, base)); },
      println(v = "", base) { serialOut(fmt(v, base) + "\n"); },
      available() { return 0; },
      read() { return -1; },
    },
  };

  let program;
  try {
    program = factory(rt);
  } catch (err) {
    throw new SketchError(explainRuntime(err));
  }

  function* main() {
    yield* program.setup();
    for (;;) {
      cpu += COST.loop;
      if (cpu >= CPU_QUANTUM) { const d = cpu; cpu = 0; yield d; }
      yield* program.loop();
    }
  }
  const gen = main();
  return {
    next() {
      let r;
      try {
        r = gen.next();
      } catch (err) {
        throw new SketchError(explainRuntime(err));
      }
      if (r.done) return { done: true };
      return { wait: r.value };
    },
  };
}

export function explainRuntime(err) {
  const msg = String(err && err.message ? err.message : err);
  // errors raised inside the simulator itself are reported as they are
  if (/\bthis\./.test(msg)) return `Error interno del simulador: ${msg}`;
  let m = msg.match(/^(\w+) is not defined/);
  if (m) {
    return `«${m[1]}» no existe: ¿la declaraste (por ejemplo int ${m[1]} = 0;) o es una función que el Arduino virtual todavía no tiene? Funciones disponibles: ${SUPPORTED.join(", ")}.`;
  }
  m = msg.match(/Assignment to constant variable/);
  if (m) return "Intentaste cambiar una constante (const). Si el valor tiene que cambiar, declaralo sin const.";
  m = msg.match(/(\S+) is not a function/);
  if (m) return `${m[1]} no es una función disponible en el Arduino virtual. Disponibles: ${SUPPORTED.join(", ")}.`;
  return msg;
}
