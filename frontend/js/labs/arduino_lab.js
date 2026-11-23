/**
 * Virtual Arduino Nano wired to a small bench of real (simulated) circuits:
 *   D13 → resistor → LED → GND
 *   D2  → push button → GND   (optional external 10 kΩ pull-up)
 *   A0  ← wiper of a 10 kΩ potentiometer between 5 V and GND
 *   D9  → 10 kΩ → 10 µF → GND (RC filter for analogWrite)
 *
 * The sketch runs in arduino_sim.js; the circuit runs in circuit_sim.js.
 * Unlike a purely digital simulator, pin currents, LED brightness, floating
 * inputs, button bounce and PWM filtering all come out of the circuit model.
 */
import { icon } from "../icons.js";
import { esc } from "../main.js";
import { createStepper, fmtSI } from "./circuit_sim.js";
import { translateSketch, createProgram, SketchError, SUPPORTED } from "./arduino_sim.js";
import { CH, part, wire, dot, gnd, nodeLabel, niceStep, drawScope, ensureStyles } from "./circuit_lab.js";

/* ------------------------------------------------------------------ */
/* Examples                                                            */
/* ------------------------------------------------------------------ */

export const EXAMPLES = [
  {
    id: "blink",
    title: "Blink: parpadear el LED",
    scope: ["d13", "iled"],
    tdiv: 0.1,
    code: `// Parpadeo: el "Hola mundo" del hardware.
// Probá cambiar la resistencia del LED en el banco y mirá la corriente en CH2.
const int LED = 13;

void setup() {
  pinMode(LED, OUTPUT);
}

void loop() {
  digitalWrite(LED, HIGH);
  delay(500);
  digitalWrite(LED, LOW);
  delay(500);
}
`,
  },
  {
    id: "pullup",
    title: "Pulsador con INPUT_PULLUP",
    scope: ["d2", "d13"],
    tdiv: 0.1,
    code: `// Con INPUT_PULLUP el pin queda en HIGH cuando el pulsador está suelto
// y baja a LOW al apretarlo (el pulsador une el pin con GND).
const int BOTON = 2;
const int LED = 13;

void setup() {
  pinMode(BOTON, INPUT_PULLUP);
  pinMode(LED, OUTPUT);
}

void loop() {
  int estado = digitalRead(BOTON);
  if (estado == LOW) {
    digitalWrite(LED, HIGH);
  } else {
    digitalWrite(LED, LOW);
  }
  delay(10);
}
`,
  },
  {
    id: "flotante",
    title: "Entrada flotante (sin pull-up)",
    scope: ["d2", "d13"],
    tdiv: 0.1,
    code: `// Con INPUT y sin resistencia de pull-up, el pin queda "al aire":
// mirá el monitor serie con el pulsador suelto. Después activá el
// pull-up externo de 10 kΩ en el banco, o cambiá a INPUT_PULLUP.
const int BOTON = 2;

void setup() {
  pinMode(BOTON, INPUT);
  Serial.begin(9600);
}

void loop() {
  Serial.println(digitalRead(BOTON));
  delay(200);
}
`,
  },
  {
    id: "rebote",
    title: "Contar pulsaciones (rebote)",
    scope: ["d2", "d13"],
    tdiv: 0.0005,
    trigger: true,
    code: `// Cuenta cada vez que el pin pasa de HIGH a LOW.
// Apretá el pulsador UNA vez: el contador salta varios números
// por el rebote mecánico. El osciloscopio está en «disparo único»:
// captura el momento en que D2 baja y se pausa solo.
const int BOTON = 2;
int ultimo = HIGH;
int cuenta = 0;

void setup() {
  pinMode(BOTON, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int ahora = digitalRead(BOTON);
  if (ultimo == HIGH && ahora == LOW) {
    cuenta++;
    Serial.print("Pulsaciones: ");
    Serial.println(cuenta);
  }
  ultimo = ahora;
}
`,
  },
  {
    id: "pote",
    title: "Potenciómetro + monitor serie",
    scope: ["a0", "d13"],
    tdiv: 0.1,
    code: `// Leé el potenciómetro (A0) y mostrá la lectura y la tensión.
// Mové el control del potenciómetro en el banco.
void setup() {
  Serial.begin(9600);
}

void loop() {
  int lectura = analogRead(A0);          // 0 .. 1023
  float volts = lectura * 5.0 / 1023.0;  // 0 .. 5 V
  Serial.print("A0 = ");
  Serial.print(lectura);
  Serial.print("  ->  ");
  Serial.print(volts);
  Serial.println(" V");
  delay(250);
}
`,
  },
  {
    id: "fade",
    title: "PWM: subir y bajar en D9",
    scope: ["d9", "filt"],
    tdiv: 0.002,
    code: `// analogWrite no da una tensión analógica: da PWM (pulsos a 490 Hz).
// El filtro RC del banco (10 kΩ + 10 µF) lo convierte en tensión continua.
// Mirá CH1 (el PWM) y CH2 (la salida del filtro). Probá 100 ms/div.
const int SALIDA = 9;

void setup() {
  pinMode(SALIDA, OUTPUT);
}

void loop() {
  for (int brillo = 0; brillo <= 255; brillo += 5) {
    analogWrite(SALIDA, brillo);
    delay(30);
  }
  for (int brillo = 255; brillo >= 0; brillo -= 5) {
    analogWrite(SALIDA, brillo);
    delay(30);
  }
}
`,
  },
  {
    id: "serial-blink",
    title: "Iteración 01: Blink con monitor serie",
    scope: ["d13", "iled"],
    tdiv: 0.1,
    code: `// Iteración 01: Blink con diagnóstico por el monitor serie.
// En el Arduino Nano el LED del banco está en D13 (en un ESP32 sería GPIO 2).
// Después probá el Morse SOS: tres cortos, tres largos, tres cortos.
// Experimento: borrá la línea de pinMode y volvé a ejecutar. El LED apenas
// brilla, porque digitalWrite sobre una entrada solo activa el pull-up interno.
const int LED_PIN = 13;

void setup() {
  Serial.begin(115200);       // misma velocidad que el monitor serie
  pinMode(LED_PIN, OUTPUT);   // sin esto el pin queda como entrada
}

void loop() {
  digitalWrite(LED_PIN, HIGH);
  Serial.println("LED ON");
  delay(500);
  digitalWrite(LED_PIN, LOW);
  Serial.println("LED OFF");
  delay(500);
}
`,
  },
  {
    id: "dimmer",
    title: "Iteración 02: pulsador + potenciómetro → PWM",
    scope: ["d9", "filt"],
    tdiv: 0.1,
    code: `// Iteración 02: pulsador + potenciómetro → brillo por PWM.
// En el Nano: pulsador en D2, potenciómetro en A0 (0..1023) y PWM en D9.
// Mantené apretado el pulsador y mové el potenciómetro: la salida del
// filtro RC (CH2) sigue al brillo que pediste.
const int BTN_PIN = 2;
const int POT_PIN = A0;
const int PWM_PIN = 9;

void setup() {
  Serial.begin(115200);
  pinMode(BTN_PIN, INPUT_PULLUP);  // suelto = HIGH, apretado = LOW
  pinMode(PWM_PIN, OUTPUT);
}

void loop() {
  bool activo = (digitalRead(BTN_PIN) == LOW);
  int crudo = analogRead(POT_PIN);           // 0..1023 en el Nano (0..4095 en ESP32)
  int brillo = map(crudo, 0, 1023, 0, 255);  // escalar a PWM de 8 bits
  analogWrite(PWM_PIN, activo ? brillo : 0);
  delay(20);
}
`,
  },
  {
    id: "millis",
    title: "millis(): parpadear sin delay()",
    scope: ["d13", "d2"],
    tdiv: 0.1,
    code: `// Parpadeo con millis(): el loop nunca se frena, así que
// el pulsador responde al instante mientras el LED parpadea.
const int LED = 13;
const int BOTON = 2;
unsigned long ultimoCambio = 0;
int estadoLed = LOW;
int intervalo = 500;

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(BOTON, INPUT_PULLUP);
}

void loop() {
  // con el pulsador apretado parpadea más rápido
  if (digitalRead(BOTON) == LOW) {
    intervalo = 100;
  } else {
    intervalo = 500;
  }
  unsigned long ahora = millis();
  if (ahora - ultimoCambio >= intervalo) {
    ultimoCambio = ahora;
    estadoLed = !estadoLed;
    digitalWrite(LED, estadoLed);
  }
}
`,
  },
];

/* ------------------------------------------------------------------ */
/* Bench: the circuit around the Nano                                  */
/* ------------------------------------------------------------------ */

const VCC = 5;
const R_OUT = 25; // ATmega328P output driver resistance (≈ 25 Ω at 5 V)
const R_PULLUP = 35000; // internal pull-up, 20–50 kΩ in the datasheet
const OFF = 1e12;
const PIN_MAX_A = 0.04; // absolute maximum per pin
const PWM_PINS = { 3: 490, 5: 980, 6: 980, 9: 490, 10: 490, 11: 490 };
const DT = 50e-6;

const LED_RS = [
  { label: "220 Ω", value: 220 },
  { label: "330 Ω", value: 330 },
  { label: "1 kΩ", value: 1000 },
  { label: "10 kΩ", value: 10000 },
  { label: "Sin resistencia", value: 0.5 },
];

/** Hash in [0,1) so bounce is random but repeatable within one press. */
const hash01 = (n) => {
  const x = Math.sin(n * 12.9898 + 78.233) * 43758.5453;
  return x - Math.floor(x);
};

export class Bench {
  constructor(opts) {
    this.opts = opts; // { ledR, extPullup, bounce, pot }
    this.button = { pressed: false, tChange: -1, seed: 1 };
    const bench = this;
    this.drivers = {};
    const els = [{ type: "V", name: "VCC", a: "vcc", b: "0", dc: VCC }];
    const nodes = ["vcc"];
    // Each connected pin is a Norton driver: I source + R to GND, plus a pull-up R to VCC.
    for (const [pin, node] of [[13, "p13"], [2, "p2"], [9, "p9"], [14, "a0"]]) {
      nodes.push(node);
      const drv = {
        node,
        mode: "INPUT",
        level: 0,
        duty: null,
        lastRead: 0,
        I: { type: "I", name: `I${pin}`, a: "0", b: node, dc: 0 },
        R: { type: "R", name: `R${pin}`, a: node, b: "0", value: OFF },
        PU: { type: "R", name: `PU${pin}`, a: "vcc", b: node, value: OFF },
      };
      els.push(drv.I, drv.R, drv.PU);
      this.drivers[pin] = drv;
    }
    nodes.push("led", "filt");
    this.rLed = { type: "R", name: "Rled", a: "p13", b: "led", value: opts.ledR };
    this.dLed = { type: "D", name: "LED", a: "led", b: "0", is: 1e-19, n: 2 }; // red LED, ≈ 2 V at 10 mA
    this.sBtn = {
      type: "S", name: "BTN", a: "p2", b: "0", ron: 0.5, roff: OFF,
      on: (t) => bench.buttonClosed(t),
    };
    this.rExt = { type: "R", name: "Rext", a: "vcc", b: "p2", value: opts.extPullup ? 10000 : OFF };
    this.rTop = { type: "R", name: "Rtop", a: "vcc", b: "a0", value: 1 };
    this.rBot = { type: "R", name: "Rbot", a: "a0", b: "0", value: 1 };
    this.rF = { type: "R", name: "Rf", a: "p9", b: "filt", value: 10000 };
    this.cF = { type: "C", name: "Cf", a: "filt", b: "0", value: 10e-6, ic: 0 };
    els.push(this.rLed, this.dLed, this.sBtn, this.rExt, this.rTop, this.rBot, this.rF, this.cF);
    this.setPot(opts.pot);
    this.stepper = createStepper({ nodes, elements: els }, { dt: DT });
    this.other = {}; // pins with nothing connected
  }

  buttonClosed(t) {
    const b = this.button;
    if (this.opts.bounce && b.tChange >= 0) {
      const since = t - b.tChange;
      if (since >= 0 && since < 2e-3) {
        // contacts chatter for ~2 ms; chatter gets rarer towards the end
        const bucket = Math.floor(since / 0.25e-3);
        const settle = since / 2e-3;
        if (hash01(bucket + b.seed * 97) < 0.4 - 0.35 * settle) return !b.pressed;
      }
    }
    return b.pressed;
  }

  press(down) {
    if (this.button.pressed === down) return;
    this.button.pressed = down;
    this.button.tChange = this.stepper.t;
    this.button.seed += 1;
  }

  setLedR(v) { this.rLed.value = v; this.stepper?.refresh(); }
  setExtPullup(on) { this.opts.extPullup = on; this.rExt.value = on ? 10000 : OFF; this.stepper?.refresh(); }
  setPot(k) {
    this.opts.pot = k;
    this.rTop.value = (1 - k) * 10000 + 1;
    this.rBot.value = k * 10000 + 1;
    this.stepper?.refresh();
  }

  normPin(pin) {
    pin = Number(pin);
    if (!Number.isInteger(pin) || pin < 0 || pin > 21) throw new Error(`El pin ${pin} no existe en el Arduino Nano (D0–D13, A0–A7).`);
    return pin;
  }

  applyDriver(d) {
    const out = d.mode === "OUTPUT" || d.mode === "PWM";
    d.R.value = out ? R_OUT : OFF;
    d.PU.value = d.mode === "INPUT_PULLUP" ? R_PULLUP : OFF;
    d.I.dc = out && d.level ? VCC / R_OUT : 0;
    this.stepper.refresh(); // pins switch in nanoseconds: settle the node now
  }

  pinMode(pin, mode) {
    pin = this.normPin(pin);
    const d = this.drivers[pin];
    if (!d) { this.other[pin] = { mode, level: 0 }; return; }
    d.mode = mode;
    d.duty = null;
    if (mode !== "OUTPUT") d.level = 0;
    this.applyDriver(d);
  }

  digitalWrite(pin, v) {
    pin = this.normPin(pin);
    const d = this.drivers[pin];
    if (!d) {
      const o = (this.other[pin] ||= { mode: "INPUT", level: 0 });
      o.level = v;
      return;
    }
    if (d.mode === "PWM") d.mode = "OUTPUT";
    d.duty = null;
    if (d.mode === "INPUT" || d.mode === "INPUT_PULLUP") {
      // Arduino quirk: digitalWrite on an input turns the pull-up on/off
      d.mode = v ? "INPUT_PULLUP" : "INPUT";
      this.applyDriver(d);
      return;
    }
    d.level = v;
    this.applyDriver(d);
  }

  analogWrite(pin, v) {
    pin = this.normPin(pin);
    const d = this.drivers[pin];
    if (!PWM_PINS[pin]) {
      // non-PWM pin: Arduino falls back to digitalWrite
      this.pinMode(pin, "OUTPUT");
      this.digitalWrite(pin, v >= 128 ? 1 : 0);
      return;
    }
    if (!d) { this.other[pin] = { mode: "OUTPUT", level: v >= 128 ? 1 : 0 }; return; }
    if (v === 0 || v === 255) {
      d.mode = "OUTPUT";
      d.duty = null;
      d.level = v === 255 ? 1 : 0;
    } else {
      d.mode = "PWM";
      d.duty = v / 255;
      d.freq = PWM_PINS[pin];
    }
    this.applyDriver(d);
  }

  /** Is the D2 node left with nothing defining its voltage? */
  floating(pin, d) {
    if (d.mode !== "INPUT") return false;
    if (pin === 2) return !this.opts.extPullup && !this.buttonClosed(this.stepper.t);
    if (pin === 9 || pin === 13) return false; // LED / RC pull the pin towards GND
    return false;
  }

  digitalRead(pin) {
    pin = this.normPin(pin);
    const d = this.drivers[pin];
    if (!d) {
      const o = this.other[pin];
      if (o && (o.mode === "OUTPUT")) return o.level ? 1 : 0;
      if (o && o.mode === "INPUT_PULLUP") return 1;
      return Math.random() < 0.5 ? 1 : 0; // nothing connected: floating
    }
    if (this.floating(pin, d)) {
      d.lastRead = Math.random() < 0.5 ? 1 : 0;
      return d.lastRead;
    }
    const v = this.stepper.v(d.node);
    if (v > 3.0) d.lastRead = 1;
    else if (v < 1.5) d.lastRead = 0; // in between: Schmitt-trigger input keeps the last value
    return d.lastRead;
  }

  analogRead(pin) {
    pin = Number(pin);
    if (pin >= 0 && pin <= 7) pin += 14; // analogRead(0) == analogRead(A0)
    pin = this.normPin(pin);
    if (pin < 14) throw new Error(`analogRead(${pin}): usá un pin analógico (A0–A7).`);
    const d = this.drivers[pin];
    if (!d) return Math.round(300 + Math.random() * 400); // floating analog input wanders
    const v = this.stepper.v(d.node);
    const raw = Math.round((v / VCC) * 1023 + (Math.random() - 0.5) * 2);
    return Math.max(0, Math.min(1023, raw));
  }

  /** Advance the circuit up to time `until`, updating PWM pins every step. */
  advanceTo(until, onSample) {
    const st = this.stepper;
    while (st.t + DT / 2 <= until) {
      const tNext = st.t + DT;
      for (const d of Object.values(this.drivers)) {
        if (d.mode !== "PWM") continue;
        const phase = (tNext * d.freq) % 1;
        const lvl = phase < d.duty ? 1 : 0;
        if (lvl !== d.level) { d.level = lvl; d.I.dc = lvl ? VCC / R_OUT : 0; st.kick(); }
      }
      st.step();
      onSample?.(st.t);
    }
  }

  ledCurrent() { return this.stepper.i(this.dLed); }

  /** Current out of a pin (positive = sourcing). */
  pinCurrent(pin) {
    const d = this.drivers[pin];
    if (!d || (d.mode !== "OUTPUT" && d.mode !== "PWM")) return 0;
    return ((d.level ? VCC : 0) - this.stepper.v(d.node)) / R_OUT;
  }
}

/* ------------------------------------------------------------------ */
/* Scope ring buffer                                                   */
/* ------------------------------------------------------------------ */

const SIGNALS = {
  d13: { label: "D13", unit: "V", read: (b) => b.stepper.v("p13") },
  iled: { label: "I(LED)", unit: "A", read: (b) => b.ledCurrent() },
  d2: { label: "D2", unit: "V", read: (b) => b.stepper.v("p2") },
  a0: { label: "A0", unit: "V", read: (b) => b.stepper.v("a0") },
  d9: { label: "D9 (PWM)", unit: "V", read: (b) => b.stepper.v("p9") },
  filt: { label: "Salida del filtro", unit: "V", read: (b) => b.stepper.v("filt") },
};
const SIG_KEYS = Object.keys(SIGNALS);
const RING = 120000; // 6 s at 50 µs

class Ring {
  constructor() {
    this.t = new Float64Array(RING);
    this.data = Object.fromEntries(SIG_KEYS.map((k) => [k, new Float32Array(RING)]));
    this.n = 0;
  }
  push(t, bench) {
    const k = this.n % RING;
    this.t[k] = t;
    for (const key of SIG_KEYS) this.data[key][k] = SIGNALS[key].read(bench);
    this.n++;
  }
  /** Samples with t in [from, to], reduced to min/max pairs so PWM shows as a band. */
  window(from, to, keys, maxPts = 1600) {
    const count = Math.min(this.n, RING);
    const start = this.n - count;
    // binary search the first index >= from
    let lo = start;
    let hi = this.n;
    while (lo < hi) {
      const mid = (lo + hi) >> 1;
      if (this.t[mid % RING] < from) lo = mid + 1; else hi = mid;
    }
    const idx = [];
    for (let i = lo; i < this.n && this.t[i % RING] <= to; i++) idx.push(i % RING);
    const out = { t: [], ch: keys.map(() => []) };
    if (!idx.length) return out;
    const buckets = Math.max(1, Math.ceil(idx.length / (maxPts / 2)));
    if (buckets === 1) {
      for (const i of idx) { out.t.push(this.t[i]); keys.forEach((k, c) => out.ch[c].push(this.data[k][i])); }
      return out;
    }
    for (let b = 0; b < idx.length; b += buckets) {
      const seg = idx.slice(b, b + buckets);
      const tA = this.t[seg[0]];
      const tB = this.t[seg[seg.length - 1]];
      const mins = keys.map((k) => Math.min(...seg.map((i) => this.data[k][i])));
      const maxs = keys.map((k) => Math.max(...seg.map((i) => this.data[k][i])));
      out.t.push(tA, tB);
      keys.forEach((k, c) => { out.ch[c].push(mins[c], maxs[c]); });
    }
    return out;
  }
}

/* ------------------------------------------------------------------ */
/* Bench drawing                                                       */
/* ------------------------------------------------------------------ */

function benchSVG(opts) {
  const rLabel = LED_RS.find((r) => r.value === opts.ledR)?.label || fmtSI(opts.ledR, "Ω");
  const pinRow = (y, name) => `
    <path d="M150,${y}H170"/>
    <text x="142" y="${y + 4}" text-anchor="end" class="ard-pin">${name}</text>`;
  return `
  <svg viewBox="0 0 600 440" class="csim-schem ard-bench" role="img" aria-label="Arduino Nano conectado a un LED, un pulsador, un potenciómetro y un filtro RC">
    <rect x="30" y="20" width="120" height="400" rx="10" class="ard-board"/>
    <text x="90" y="220" text-anchor="middle" class="ard-board-text" transform="rotate(-90 90 220)">ARDUINO NANO</text>
    ${pinRow(50, "D13")}${pinRow(165, "D2")}${pinRow(290, "A0")}${pinRow(385, "D9")}

    <!-- D13: resistor + LED -->
    ${wire([170, 50], [200, 50])}
    ${part("R", 200, 50, 300, 50, { name: "R", value: rLabel })}
    ${wire([300, 50], [330, 50])}
    ${part("D", 330, 50, 400, 50, { name: "LED", value: "rojo" })}
    <circle id="ard-led-glow" cx="365" cy="50" r="16" style="fill:#ff3b30;stroke:none" opacity="0"/>
    ${wire([400, 50], [470, 50], [470, 68])}
    ${gnd(470, 68)}
    <text id="ard-v-d13" x="176" y="80" class="csim-val">0 V</text>
    <text id="ard-i-led" x="330" y="86" class="ard-live">I = 0 A</text>

    <!-- D2: button to GND, optional external pull-up -->
    ${wire([170, 165], [370, 165])}
    ${dot(230, 165)}
    ${part("R", 230, 165, 230, 105, { name: "Pull-up", value: opts.extPullup ? "10 kΩ" : "sin conectar", off: !opts.extPullup })}
    ${wire([230, 105], [230, 98])}
    <text x="230" y="92" text-anchor="middle" class="csim-node">+5 V</text>
    <g id="ard-btn" class="ard-btn" tabindex="0" role="button" aria-label="Pulsador: mantené apretado">
      <rect x="366" y="130" width="98" height="62" rx="8" class="ard-btn-hit"/>
      <path d="M370,165H390M440,165H460"/>
      <circle cx="390" cy="165" r="2.4" class="csim-solid"/><circle cx="440" cy="165" r="2.4" class="csim-solid"/>
      <path id="ard-btn-lever" d="M390,151H440M415,151V141"/>
      <text x="415" y="210" text-anchor="middle" class="csim-val">pulsador: mantené apretado</text>
    </g>
    ${wire([460, 165], [500, 165], [500, 183])}
    ${gnd(500, 183)}
    <text id="ard-v-d2" x="176" y="195" class="csim-val">0 V</text>

    <!-- A0: potentiometer -->
    ${wire([170, 290], [335, 290])}
    <path d="M335,290l-10,-5v10z" class="csim-solid"/>
    ${part("R", 350, 245, 350, 335, { name: "Pote 10 kΩ", value: "" })}
    <text x="350" y="238" text-anchor="middle" class="csim-node">+5 V</text>
    ${gnd(350, 335)}
    <text id="ard-v-a0" x="176" y="320" class="csim-val">0 V</text>

    <!-- D9: RC filter -->
    ${wire([170, 385], [200, 385])}
    ${part("R", 200, 385, 300, 385, { name: "10 kΩ", value: "" })}
    ${wire([300, 385], [470, 385])}
    ${dot(340, 385)}
    ${nodeLabel(340, 373, "filtro")}
    ${part("C", 470, 385, 470, 425, { name: "10 µF", value: "" })}
    <text id="ard-v-d9" x="176" y="412" class="csim-val">0 V</text>
    <text id="ard-v-filt" x="340" y="412" class="ard-live">0 V</text>
  </svg>`;
}

function ensureArduinoStyles() {
  ensureStyles();
  if (document.getElementById("ard-styles")) return;
  const st = document.createElement("style");
  st.id = "ard-styles";
  st.textContent = `
    .ard-layout { display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1.1fr); gap:16px; align-items:start; }
    @media (max-width:1100px) { .ard-layout { grid-template-columns:1fr; } }
    .ard-editor { width:100%; min-height:420px; resize:vertical; font:13px/1.5 var(--font-mono); tab-size:2; background:var(--bg-field); color:var(--text); border:1px solid var(--border-strong); border-radius:var(--radius-sm); padding:10px 12px; white-space:pre; overflow:auto; }
    .ard-toolbar { display:flex; gap:8px; flex-wrap:wrap; align-items:center; }
    .ard-status { font:12px var(--font-mono); color:var(--text-secondary); }
    .ard-error { white-space:pre-wrap; }
    .ard-bench { max-height:none; }
    .ard-board { fill:#1f5f8b; stroke:#173f5c; }
    .ard-board-text { fill:#e9f3fb !important; font:600 14px var(--font-mono) !important; letter-spacing:.12em; }
    .ard-pin { font-weight:600; }
    .ard-live { fill:var(--accent) !important; font-weight:600; }
    .ard-btn { cursor:pointer; outline:none; }
    .ard-btn-hit { fill:transparent; stroke:var(--border-strong); stroke-dasharray:3 3; }
    .ard-btn:hover .ard-btn-hit, .ard-btn:focus-visible .ard-btn-hit { stroke:var(--accent); }
    .ard-btn.pressed .ard-btn-hit { fill:var(--accent-soft); stroke:var(--accent); }
    .ard-bench-controls { display:grid; grid-template-columns:repeat(auto-fit,minmax(170px,1fr)); gap:10px 14px; align-items:end; }
    .ard-serial { background:#141917; color:#d8f3e2; font:12.5px/1.45 var(--font-mono); border-radius:var(--radius-sm); padding:10px 12px; height:180px; overflow:auto; white-space:pre-wrap; margin:0; border:6px solid #3a3a37; }
    .ard-warn { color:var(--danger); font-weight:600; }
    .ard-scope-ctl { display:flex; gap:10px; flex-wrap:wrap; align-items:end; }
    .ard-scope-ctl .field { min-width:130px; }
  `;
  document.head.appendChild(st);
}

/* ------------------------------------------------------------------ */
/* Main render                                                         */
/* ------------------------------------------------------------------ */

const CODE_KEY = "aprendelab_arduino_code";
const memory = { exampleId: "blink", code: null, ch: ["d13", "iled"], tdiv: 0.1, bench: { ledR: 220, extPullup: false, bounce: true, pot: 0.5 }, speed: 1 };

export function renderArduinoLab(body, { exampleId = null } = {}) {
  ensureArduinoStyles();
  if (memory.code == null) {
    try { memory.code = localStorage.getItem(CODE_KEY); } catch { /* storage blocked */ }
    if (!memory.code) memory.code = EXAMPLES[0].code;
  }
  // Deep link from a lesson or project: open with that example loaded.
  // The learner's own sketch is kept aside so it can be recovered.
  let previousCode = null;
  const linked = exampleId ? EXAMPLES.find((e) => e.id === exampleId) : null;
  if (linked) {
    const isExample = EXAMPLES.some((e) => e.code === memory.code);
    if (!isExample && memory.code.trim()) {
      previousCode = memory.code;
      try { localStorage.setItem(`${CODE_KEY}_prev`, previousCode); } catch { /* ignore */ }
    }
    memory.exampleId = linked.id;
    memory.code = linked.code;
    memory.ch = [...linked.scope];
    memory.tdiv = linked.tdiv;
    try { localStorage.setItem(CODE_KEY, memory.code); } catch { /* ignore */ }
  }

  let bench = null;
  let program = null;
  let ring = null;
  let now = 0; // program clock (s)
  let resumeAt = 0;
  let running = false;
  let paused = false;
  let lastWall = 0;
  let raf = 0;
  let serialText = "";
  let cursorX = null;
  let realRatio = 1;
  let lastOverload = 0;
  // single-shot trigger on a falling edge of CH1 (like a real scope's SINGLE button)
  const trig = { on: false, scan: 0, tf: null, view: null };
  const armTrigger = () => { trig.tf = null; trig.view = null; trig.scan = ring ? ring.n : 0; };

  body.innerHTML = `
    <div class="stack">
      <div class="card stack-sm">
        <div class="eyebrow" style="margin:0;">Arduino virtual · el código y el circuito en el mismo simulador</div>
        <p class="xs muted" style="margin:0;">Un Arduino Nano conectado a un LED (D13), un pulsador (D2), un potenciómetro (A0) y un filtro RC (D9).
          A diferencia de Wokwi, el circuito es analógico: la resistencia cambia la corriente del LED, una entrada sin pull-up «flota», el pulsador rebota y el PWM se filtra de verdad.</p>
      </div>

      <div class="ard-layout">
        <div class="card stack">
          <div class="ard-toolbar">
            <label class="field" style="flex:1;min-width:200px;margin:0;"><span>Ejemplo</span>
              <select id="ard-example">
                ${EXAMPLES.map((e) => `<option value="${e.id}" ${e.id === memory.exampleId ? "selected" : ""}>${esc(e.title)}</option>`).join("")}
              </select>
            </label>
            <button type="button" class="btn btn-secondary btn-sm" id="ard-load" style="align-self:end;">${icon("download", 14)} Cargar ejemplo</button>
          </div>
          <textarea id="ard-code" class="ard-editor" spellcheck="false" autocomplete="off" aria-label="Código del sketch">${esc(memory.code)}</textarea>
          <div class="ard-toolbar">
            <button type="button" class="btn btn-primary" id="ard-run">${icon("play", 14)} Cargar y ejecutar</button>
            <button type="button" class="btn btn-secondary" id="ard-pause" disabled>${icon("pause", 14)} Pausar</button>
            <button type="button" class="btn btn-ghost" id="ard-stop" disabled>${icon("stop", 14)} Detener</button>
            <label class="field" style="margin:0;min-width:120px;"><span>Velocidad</span>
              <select id="ard-speed">
                <option value="1" ${memory.speed === 1 ? "selected" : ""}>Tiempo real</option>
                <option value="0.1" ${memory.speed === 0.1 ? "selected" : ""}>Cámara lenta ×0,1</option>
                <option value="0.01" ${memory.speed === 0.01 ? "selected" : ""}>Cámara lenta ×0,01</option>
              </select>
            </label>
          </div>
          <div class="ard-status" id="ard-status">Detenido. Elegí un ejemplo o escribí tu sketch y apretá «Cargar y ejecutar».</div>
          <div id="ard-msg"></div>
          <details class="small">
            <summary>Qué acepta el Arduino virtual</summary>
            <p class="xs muted">Funciones: ${esc(SUPPORTED.join(", "))}. Variables int, long, float, bool, byte, String y arreglos; if, for, while, do, switch y funciones propias.
              Diferencias con una placa real: no hay librerías (Wire, Servo, WiFi) y la división no redondea a entero salvo que uses (int).</p>
          </details>
        </div>

        <div class="stack">
          <div class="card stack-sm">
            <div class="eyebrow" style="margin:0;">Banco de pruebas</div>
            <div id="ard-bench"></div>
            <div class="ard-bench-controls">
              <label class="field" style="margin:0;"><span>Resistencia del LED</span>
                <select id="ard-ledr">${LED_RS.map((r) => `<option value="${r.value}" ${r.value === memory.bench.ledR ? "selected" : ""}>${esc(r.label)}</option>`).join("")}</select>
              </label>
              <label class="csim-toggle" style="padding-top:0;"><input type="checkbox" id="ard-extpu" ${memory.bench.extPullup ? "checked" : ""}/> <span>Pull-up externo 10 kΩ en D2</span></label>
              <label class="csim-toggle" style="padding-top:0;"><input type="checkbox" id="ard-bounce" ${memory.bench.bounce ? "checked" : ""}/> <span>Rebote del pulsador</span></label>
              <label class="field" style="margin:0;"><span class="row-between"><span>Potenciómetro</span><strong class="mono" id="ard-pot-lbl">${Math.round(memory.bench.pot * 100)} %</strong></span>
                <input type="range" id="ard-pot" min="0" max="1" step="0.01" value="${memory.bench.pot}"/>
              </label>
            </div>
            <div id="ard-overload" class="small"></div>
          </div>

          <div class="card stack-sm">
            <div class="row-between"><div class="eyebrow" style="margin:0;">Osciloscopio</div><span class="xs muted">Pausá para medir con el cursor.</span></div>
            <div class="ard-scope-ctl">
              ${[0, 1].map((c) => `<label class="field" style="margin:0;"><span style="color:${CH[c].ink}">CH${c + 1}</span>
                <select data-ch="${c}">${SIG_KEYS.map((k) => `<option value="${k}" ${memory.ch[c] === k ? "selected" : ""}>${esc(SIGNALS[k].label)}</option>`).join("")}</select></label>`).join("")}
              <label class="field" style="margin:0;"><span>Base de tiempo</span>
                <select id="ard-tdiv">${[0.0005, 0.001, 0.002, 0.005, 0.02, 0.1, 0.5].map((v) => `<option value="${v}" ${v === memory.tdiv ? "selected" : ""}>${fmtSI(v, "s")}/div</option>`).join("")}</select>
              </label>
              <label class="csim-toggle" style="padding-top:0;margin-bottom:8px;" title="Espera a que CH1 baje de 2,5 V, captura ese instante y pausa"><input type="checkbox" id="ard-trig"/> <span>Disparo único (CH1 baja)</span></label>
            </div>
            <canvas class="csim-screen" id="ard-screen" aria-label="Pantalla del osciloscopio"></canvas>
            <div class="csim-scope-bar mono xs" id="ard-scope-bar"></div>
            <div class="csim-cursor mono xs" id="ard-cursor"></div>
          </div>

          <div class="card stack-sm">
            <div class="row-between"><div class="eyebrow" style="margin:0;">Monitor serie</div>
              <button type="button" class="btn btn-ghost btn-sm" id="ard-clear">${icon("trash", 14)} Limpiar</button></div>
            <pre class="ard-serial" id="ard-serial" aria-live="polite"></pre>
          </div>
        </div>
      </div>
    </div>`;

  const $ = (sel) => body.querySelector(sel);
  const codeEl = $("#ard-code");
  const statusEl = $("#ard-status");
  const msgEl = $("#ard-msg");
  const serialEl = $("#ard-serial");
  const canvas = $("#ard-screen");

  const paintBench = () => { $("#ard-bench").innerHTML = benchSVG(memory.bench); wireButton(); };

  const showMsg = (html, kind = "warn") => {
    msgEl.innerHTML = html ? `<div class="callout callout-${kind} small ard-error">${html}</div>` : "";
  };

  const saveCode = () => {
    memory.code = codeEl.value;
    try { localStorage.setItem(CODE_KEY, memory.code); } catch { /* ignore */ }
  };

  /* ---------- editor ---------- */
  codeEl.addEventListener("input", saveCode);
  codeEl.addEventListener("keydown", (e) => {
    if (e.key === "Tab") {
      e.preventDefault();
      const { selectionStart: a, selectionEnd: b } = codeEl;
      codeEl.setRangeText("  ", a, b, "end");
      saveCode();
    } else if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
      e.preventDefault();
      start();
    }
  });
  $("#ard-load").addEventListener("click", () => {
    const ex = EXAMPLES.find((x) => x.id === $("#ard-example").value);
    if (!ex) return;
    memory.exampleId = ex.id;
    codeEl.value = ex.code;
    saveCode();
    memory.ch = [...ex.scope];
    memory.tdiv = ex.tdiv;
    body.querySelectorAll("select[data-ch]").forEach((s) => { s.value = memory.ch[Number(s.dataset.ch)]; });
    $("#ard-tdiv").value = String(ex.tdiv);
    start();
    setTrigger(!!ex.trigger);
  });

  /* ---------- bench controls ---------- */
  $("#ard-ledr").addEventListener("change", (e) => {
    memory.bench.ledR = Number(e.target.value);
    bench?.setLedR(memory.bench.ledR);
    paintBench();
  });
  $("#ard-extpu").addEventListener("change", (e) => {
    memory.bench.extPullup = e.target.checked;
    bench?.setExtPullup(e.target.checked);
    paintBench();
  });
  $("#ard-bounce").addEventListener("change", (e) => {
    memory.bench.bounce = e.target.checked;
    if (bench) bench.opts.bounce = e.target.checked;
  });
  $("#ard-pot").addEventListener("input", (e) => {
    memory.bench.pot = Number(e.target.value);
    $("#ard-pot-lbl").textContent = `${Math.round(memory.bench.pot * 100)} %`;
    bench?.setPot(memory.bench.pot);
  });
  $("#ard-speed").addEventListener("change", (e) => { memory.speed = Number(e.target.value); });

  function wireButton() {
    const btn = $("#ard-btn");
    if (!btn) return;
    const set = (down) => {
      btn.classList.toggle("pressed", down);
      btn.querySelector("#ard-btn-lever").setAttribute("d", down ? "M390,163H440M415,163V153" : "M390,151H440M415,151V141");
      bench?.press(down);
    };
    btn.addEventListener("pointerdown", (e) => { e.preventDefault(); btn.setPointerCapture?.(e.pointerId); set(true); });
    btn.addEventListener("pointerup", () => set(false));
    btn.addEventListener("pointercancel", () => set(false));
    btn.addEventListener("keydown", (e) => { if ((e.key === " " || e.key === "Enter") && !e.repeat) { e.preventDefault(); set(true); } });
    btn.addEventListener("keyup", (e) => { if (e.key === " " || e.key === "Enter") set(false); });
  }

  /* ---------- scope controls ---------- */
  body.querySelectorAll("select[data-ch]").forEach((s) =>
    s.addEventListener("change", () => { memory.ch[Number(s.dataset.ch)] = s.value; drawNow(); })
  );
  $("#ard-tdiv").addEventListener("change", (e) => { memory.tdiv = Number(e.target.value); drawNow(); });
  const setTrigger = (on) => {
    trig.on = on;
    $("#ard-trig").checked = on;
    armTrigger();
    if (running && !paused) statusEl.textContent = on ? "Esperando el disparo…" : statusEl.textContent;
  };
  $("#ard-trig").addEventListener("change", (e) => {
    setTrigger(e.target.checked);
    if (e.target.checked && running && paused) $("#ard-pause").click(); // re-arm and continue
  });
  const moveCursor = (e) => {
    const r = canvas.getBoundingClientRect();
    cursorX = Math.min(r.width, Math.max(0, e.clientX - r.left));
    if (!running || paused) drawNow();
  };
  canvas.addEventListener("pointermove", moveCursor);
  canvas.addEventListener("pointerdown", moveCursor);
  canvas.addEventListener("pointerleave", () => { cursorX = null; if (!running || paused) drawNow(); });

  /* ---------- serial ---------- */
  const appendSerial = (text) => {
    serialText += text;
    if (serialText.length > 20000) serialText = serialText.slice(-15000);
  };
  $("#ard-clear").addEventListener("click", () => { serialText = ""; serialEl.textContent = ""; });

  /* ---------- run control ---------- */
  function setButtons() {
    $("#ard-pause").disabled = !running;
    $("#ard-stop").disabled = !running;
    $("#ard-pause").innerHTML = paused ? `${icon("play", 14)} Seguir` : `${icon("pause", 14)} Pausar`;
  }

  function stop(reason = "Detenido.") {
    running = false;
    paused = false;
    cancelAnimationFrame(raf);
    statusEl.textContent = reason;
    setButtons();
  }

  function fail(err) {
    const line = err instanceof SketchError && err.line ? `Línea ${err.line}: ` : "";
    showMsg(`${icon("alert", 14)} <strong>${err instanceof SketchError && !running ? "No se pudo cargar el sketch" : "El programa se detuvo"}.</strong>\n${esc(line + err.message)}`, "warn");
    stop("Detenido por un error.");
  }

  function start() {
    cancelAnimationFrame(raf);
    running = false;
    saveCode();
    showMsg("");
    let factory;
    try {
      ({ factory } = translateSketch(codeEl.value));
    } catch (err) {
      fail(err);
      return;
    }
    bench = new Bench({ ...memory.bench });
    ring = new Ring();
    now = 0;
    resumeAt = 0;
    serialText = "";
    serialEl.textContent = "";
    const warned = new Set();
    try {
      program = createProgram(factory, {
        now: () => now,
        pinMode: (p, m) => bench.pinMode(p, m),
        digitalWrite: (p, v) => bench.digitalWrite(p, v),
        digitalRead: (p) => bench.digitalRead(p),
        analogRead: (p) => bench.analogRead(p),
        analogWrite: (p, v) => bench.analogWrite(p, v),
        serial: appendSerial,
        warn: (t) => {
          if (warned.has(t)) return;
          warned.add(t);
          showMsg(`${icon("alert", 14)} ${esc(t)}`, "info");
        },
      });
    } catch (err) {
      fail(err);
      return;
    }
    ring.push(0, bench);
    armTrigger();
    running = true;
    paused = false;
    lastWall = performance.now();
    setButtons();
    raf = requestAnimationFrame(frame);
  }

  $("#ard-run").addEventListener("click", start);
  $("#ard-pause").addEventListener("click", () => {
    if (!running) return;
    paused = !paused;
    lastWall = performance.now();
    setButtons();
    if (!paused && trig.on) armTrigger(); // «Seguir» arms the next single shot
    if (!paused) raf = requestAnimationFrame(frame);
    else { statusEl.textContent = `En pausa · t = ${fmtSI(now, "s", 4)}`; drawNow(); }
  });
  $("#ard-stop").addEventListener("click", () => stop());

  /* ---------- simulation loop ---------- */
  function frame(wall) {
    if (!running || paused) return;
    if (!body.isConnected) { stop(); return; }
    const frameStart = performance.now();
    const wantedReal = Math.min(0.05, (wall - lastWall) / 1000);
    lastWall = wall;
    const target = now + wantedReal * memory.speed;
    const before = now;
    try {
      while (now < target) {
        if (resumeAt <= now + 1e-12) {
          const r = program.next();
          if (r.done) { stop("El programa terminó."); break; }
          resumeAt = now + r.wait;
          continue;
        }
        const until = Math.min(resumeAt, target);
        bench.advanceTo(until, (t) => ring.push(t, bench));
        now = until;
        if (performance.now() - frameStart > 28) break; // keep the page responsive
      }
    } catch (err) {
      fail(err);
      return;
    }
    if (wantedReal > 0) realRatio = 0.9 * realRatio + 0.1 * Math.min(1, (now - before) / (wantedReal * memory.speed));
    if (trig.on && running) {
      const data = ring.data[memory.ch[0]];
      if (trig.tf == null) {
        for (let k = Math.max(trig.scan, 1, ring.n - RING + 1); k < ring.n; k++) {
          if (data[(k - 1) % RING] > 2.5 && data[k % RING] <= 2.5) { trig.tf = ring.t[k % RING]; break; }
        }
        trig.scan = ring.n;
      }
      if (trig.tf != null && bench.stepper.t >= trig.tf + 8 * memory.tdiv) {
        trig.view = trig.tf - 2 * memory.tdiv;
        paused = true;
        setButtons();
      }
    }
    drawNow();
    if (running && !paused) raf = requestAnimationFrame(frame);
  }

  function drawNow() {
    if (!bench) { drawEmpty(); return; }
    // bench live values
    const set = (id, text) => { const el = body.querySelector(id); if (el) el.textContent = text; };
    const st = bench.stepper;
    const vtxt = (v) => (Math.abs(v) < 1e-3 ? "0 V" : fmtSI(v, "V", 3));
    set("#ard-v-d13", vtxt(st.v("p13")));
    set("#ard-v-d2", bench.floating(2, bench.drivers[2]) ? "flotante (sin pull-up)" : vtxt(st.v("p2")));
    set("#ard-v-a0", vtxt(st.v("a0")));
    set("#ard-v-d9", vtxt(st.v("p9")));
    set("#ard-v-filt", vtxt(st.v("filt")));
    const iLed = Math.max(0, bench.ledCurrent());
    set("#ard-i-led", `I = ${iLed < 1e-6 ? "0 A" : fmtSI(iLed, "A", 3)}`);
    const glow = body.querySelector("#ard-led-glow");
    if (glow) glow.setAttribute("opacity", String(Math.min(0.9, Math.sqrt(iLed / 0.02) * 0.9)));
    const iPin = Math.abs(bench.pinCurrent(13));
    const ovl = body.querySelector("#ard-overload");
    if (iPin > PIN_MAX_A) lastOverload = iPin;
    if (ovl) {
      ovl.innerHTML = lastOverload > PIN_MAX_A
        ? `<span class="ard-warn">${icon("alert", 14)} El pin D13 llegó a entregar ${fmtSI(lastOverload, "A", 3)}: supera el máximo absoluto de 40 mA del ATmega328P. En una placa real el pin (o el LED) se daña.</span>`
        : `<span class="xs muted">Corriente del pin D13: ${iPin < 1e-6 ? "0 A" : fmtSI(iPin, "A", 3)} (máximo 40 mA).</span>`;
    }
    if (lastOverload && iPin < PIN_MAX_A && memory.bench.ledR > 1) lastOverload = 0;

    // serial
    if (serialEl.textContent.length !== serialText.length) {
      const atBottom = serialEl.scrollTop + serialEl.clientHeight >= serialEl.scrollHeight - 8;
      serialEl.textContent = serialText;
      if (atBottom) serialEl.scrollTop = serialEl.scrollHeight;
    }

    if (running) {
      const speedTxt = memory.speed === 1 ? "" : ` · cámara lenta ×${String(memory.speed).replace(".", ",")}`;
      const lag = realRatio < 0.95 && !paused ? ` · el simulador va al ${Math.round(realRatio * 100)} % del tiempo real` : "";
      const trigTxt = trig.on ? (trig.view != null ? " · disparo capturado: «Seguir» espera el próximo" : " · esperando el disparo (CH1 baja de 2,5 V)") : "";
      statusEl.textContent = paused ? `En pausa · t = ${fmtSI(now, "s", 4)}${trig.view != null && paused ? trigTxt : ""}` : `Corriendo · t = ${now.toFixed(2)} s${speedTxt}${lag}${trigTxt}`;
    }

    // scope
    const span = memory.tdiv * 10;
    const captured = paused && trig.view != null;
    const t1 = captured ? trig.view + span : bench.stepper.t;
    const t0 = captured ? trig.view : Math.max(0, t1 - span);
    const keys = memory.ch;
    const win = ring.window(t0, t1, keys);
    const scales = keys.map((k, c) => {
      if (SIGNALS[k].unit === "V") return 1;
      const m = Math.max(1e-3, ...win.ch[c].map(Math.abs));
      return niceStep(m / 6.4);
    });
    const scope = {
      sim: { t: win.t },
      t0: captured || t1 > span ? t0 : 0,
      trigger: captured ? trig.tf : undefined,
      tdiv: memory.tdiv,
      fixedScales: scales,
      channels: keys.map((k, c) => ({ label: `CH${c + 1} · ${SIGNALS[k].label}`, data: win.ch[c], unit: SIGNALS[k].unit })),
    };
    if (!win.t.length) { drawEmpty(); return; }
    const res = drawScope(canvas, scope, paused || !running ? cursorX : null);
    $("#ard-scope-bar").innerHTML = `<span>${fmtSI(memory.tdiv, "s")}/div</span>${keys
      .map((k, c) => `<span style="color:${CH[c].ink}">CH${c + 1} · ${esc(SIGNALS[k].label)}: ${fmtSI(scales[c], SIGNALS[k].unit)}/div</span>`)
      .join("")}`;
    const cur = $("#ard-cursor");
    if (res?.readout) {
      const tAbs = captured ? res.readout.t : res.readout.t + (t1 > span ? t0 : 0);
      cur.innerHTML = `Cursor: ${captured ? "t desde el disparo" : "t"} = <strong>${fmtSI(tAbs, "s", 5)}</strong>${res.readout.values
        .map((v, c) => ` · <span style="color:${CH[c].ink}">CH${c + 1} = <strong>${fmtSI(v.v, v.unit, 4)}</strong></span>`)
        .join("")}`;
    } else {
      cur.textContent = running && !paused ? "Pausá para mover el cursor sobre la pantalla." : "Pasá el mouse por la pantalla para medir.";
    }
  }

  function drawEmpty() {
    const dpr = window.devicePixelRatio || 1;
    const w = canvas.clientWidth;
    const h = canvas.clientHeight;
    if (!w || !h) return;
    canvas.width = Math.round(w * dpr);
    canvas.height = Math.round(h * dpr);
    const ctx = canvas.getContext("2d");
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.fillStyle = "#141917";
    ctx.fillRect(0, 0, w, h);
    ctx.fillStyle = "rgba(255,255,255,0.5)";
    ctx.font = "12px ui-monospace, monospace";
    ctx.fillText("Sin señal: ejecutá un sketch.", 14, 22);
  }

  paintBench();
  drawEmpty();
  if (linked) {
    statusEl.textContent = `Cargué el ejemplo «${linked.title}». Apretá «Cargar y ejecutar» (o Ctrl+Enter).`;
    if (linked.trigger) $("#ard-trig").checked = trig.on = true;
  }
  if (previousCode) {
    showMsg(`${icon("alert", 14)} Tu sketch anterior quedó guardado. <button type="button" class="btn btn-ghost btn-sm" id="ard-restore">Recuperarlo</button>`, "info");
    $("#ard-restore").addEventListener("click", () => {
      codeEl.value = previousCode;
      saveCode();
      showMsg("");
    });
  }
  if (typeof ResizeObserver !== "undefined") {
    const ro = new ResizeObserver(() => {
      if (!canvas.isConnected) { ro.disconnect(); stop(); return; }
      if (!running || paused) drawNow();
    });
    ro.observe(canvas);
  }
}
