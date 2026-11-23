import { icon } from "../icons.js";
import { api, esc, toast } from "../main.js";

function randInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
function gcd(a, b) {
  let x = Math.abs(a), y = Math.abs(b);
  while (y) [x, y] = [y, x % y];
  return x || 1;
}

/**
 * Reads what the learner typed as a number: "7", "-0,5", "+12", "x = 7", "57°", "3/4",
 * the mixed number "1 1/12" or "1.575" written with a thousands separator.
 * `simplified` is false only for a fraction that can still be reduced.
 */
function parseAnswer(raw) {
  const s = String(raw ?? "")
    .trim()
    .toLowerCase()
    .replace(/[−–]/g, "-")
    .replace(/^[a-zθ]\s*=\s*/, "")
    .replace(/[°%$]/g, "")
    .replace(/^\+/, "")
    .trim();
  const mixed = s.match(/^(-?)\s*(\d+)\s+(\d+)\s*\/\s*(\d+)$/);
  if (mixed && Number(mixed[4])) {
    const [whole, n, d] = [Number(mixed[2]), Number(mixed[3]), Number(mixed[4])];
    const value = whole + n / d;
    return { values: [mixed[1] ? -value : value], simplified: n < d && gcd(n, d) === 1 };
  }
  const t = s.replace(/\s/g, "");
  const frac = t.match(/^(-?\d+)\/(\d+)$/);
  if (frac && Number(frac[2])) {
    return { values: [Number(frac[1]) / Number(frac[2])], simplified: gcd(Number(frac[1]), Number(frac[2])) === 1 };
  }
  const dec = t.replace(",", ".");
  if (!/^-?(\d+(\.\d+)?|\.\d+)$/.test(dec)) return null;
  const values = [Number(dec)];
  if (/^-?\d{1,3}([.,]\d{3})+$/.test(t)) values.push(Number(t.replace(/[.,]/g, "")));
  return { values, simplified: true };
}

/**
 * Grades by value, so "1.50", "1,5" and "3/2" all match "1.5". When the expected answer
 * is a fraction, an equivalent fraction that is not fully reduced is reported apart.
 */
function gradeAnswer(given, expected) {
  const want = parseAnswer(expected);
  const got = parseAnswer(given);
  if (!want || !got) {
    return { ok: String(given ?? "").trim().replaceAll(" ", "") === String(expected), unsimplified: false };
  }
  const same = got.values.some((v) => Math.abs(v - want.values[0]) < 1e-9);
  const mustReduce = String(expected).includes("/");
  return { ok: same && (!mustReduce || got.simplified), unsimplified: same && mustReduce && !got.simplified };
}

function renderFractionVisualSVG() {
  const w = 360;
  const drawBar = (y, total, filled, fillHex, label) => {
    const bw = 260;
    const step = bw / total;
    let out = `<text x="0" y="${y + 16}" fill="currentColor" font-size="11" font-family="monospace">${label}</text>`;
    for (let i = 0; i < total; i++) {
      out += `<rect x="${76 + i * step}" y="${y}" width="${step - 2}" height="22" rx="3" fill="${i < filled ? fillHex : "rgba(128,128,128,0.16)"}" stroke="currentColor" stroke-opacity="0.2" />`;
    }
    return out;
  };
  return `
    <svg viewBox="0 0 ${w} 102" width="100%" style="max-width:390px;" role="img" aria-label="Visualización de 2/3 más 1/4 igual 11/12">
      ${drawBar(6, 12, 8, "#235e63", "2/3 = 8/12")}
      ${drawBar(38, 12, 3, "#7fa29d", "1/4 = 3/12")}
      ${drawBar(70, 12, 11, "#1e1e1c", "Total 11/12")}
    </svg>`;
}

const MATH_TOPICS = {
  place_value: {
    name: "Valor posicional, sumas y restas",
    strategyHint: "Para restar sobre ceros (como 5000 − 1375), restale 1 a los dos números (4999 − 1374) o subí contando desde el menor.",
    worked: {
      problem: "5000 − 1375",
      steps: [
        { expr: "4999 − 1374", why: "Restar 1 a ambos números mantiene exactamente la misma distancia y elimina todos los 'pedir prestado'." },
        { expr: "3625", why: "Restamos columna por columna sin enredos: 9−4=5, 9−7=2, 9−3=6, 4−1=3." },
      ],
    },
    faded: {
      problem: "3000 − 1425",
      given: "Truco del −1 en ambos lados: 2999 − 1424",
      blankPrompt: "¿Cuánto da 9 − 4 en las unidades?",
      blankAnswer: "5",
      finalPrompt: "Resultado final de 2999 − 1424:",
      finalAnswer: "1575",
    },
    generate(level = 1) {
      if (level === 1) {
        const a = randInt(2, 9) * 100 - randInt(1, 3) * 10;
        const b = randInt(12, 65) * 10;
        const ans = a + b;
        return {
          topic: "place_value",
          promptHtml: `<span class="math-expr">${a} + ${b}</span>`,
          answer: String(ans),
          diagnose(val) {
            if (Math.abs(Number(val) - ans) === 100) return "Cuidado al llevar 1 centena cuando la suma de decenas pasa de 100.";
            return "";
          },
          explain: `${a} + ${b} = ${ans}.`,
        };
      }
      const top = level === 2 ? randInt(2, 6) * 1000 : randInt(4, 9) * 1000;
      const sub = randInt(325, top - 450);
      const ans = top - sub;
      return {
        topic: "place_value",
        promptHtml: `<span class="math-expr">${top} − ${sub}</span>`,
        answer: String(ans),
        diagnose(val) {
          if (Math.abs(Number(val) - ans) === 100 || Math.abs(Number(val) - ans) === 1000) {
            return `Error clásico al pedir prestado sobre ceros: probá el truco ${top - 1} − ${sub - 1}.`;
          }
          return "";
        },
        explain: `Con el truco del −1: ${top - 1} − ${sub - 1} = ${ans} (verificación: ${ans} + ${sub} = ${top}).`,
      };
    },
  },
  mult_div: {
    name: "Multiplicación y división",
    strategyHint: "Descomponé en decenas y unidades (modelo de área: 24 × 15 = 24×10 + 24×5) o dividí sacando bloques fáciles (×10, ×20).",
    worked: {
      problem: "24 × 15 (modelo de área)",
      steps: [
        { expr: "24 × 10 = 240", why: "Primero multiplicamos por las decenas (10): agregar un cero es instantáneo." },
        { expr: "24 × 5 = 120", why: "Multiplicar por 5 es exactamente la mitad de multiplicar por 10." },
        { expr: "240 + 120 = 360", why: "Sumamos los dos bloques del área total." },
      ],
    },
    faded: {
      problem: "18 × 15",
      given: "Separamos 15 en 10 + 5 → 18 × 10 = 180",
      blankPrompt: "¿Cuánto es 18 × 5 (la mitad de 180)?",
      blankAnswer: "90",
      finalPrompt: "Total (180 + ese valor):",
      finalAnswer: "270",
    },
    generate(level = 1) {
      if (level === 1) {
        const a = randInt(6, 9);
        const b = randInt(6, 9);
        const ans = a * b;
        return {
          topic: "mult_div",
          promptHtml: `<span class="math-expr">${a} × ${b}</span>`,
          answer: String(ans),
          diagnose(val) {
            if (Math.abs(Number(val) - ans) === a || Math.abs(Number(val) - ans) === b) {
              return `Estuviste a un grupo de distancia: probá descomponer ${a} × ${b} = ${a} × 5 + ${a} × ${b - 5}.`;
            }
            return "";
          },
          explain: `${a} × ${b} = ${a} × 5 + ${a} × ${b - 5} = ${a * 5} + ${a * (b - 5)} = ${ans}.`,
        };
      }
      if (level === 2) {
        const a = randInt(12, 28);
        const b = [12, 15, 25, 14, 16][randInt(0, 4)];
        const ans = a * b;
        return {
          topic: "mult_div",
          promptHtml: `<span class="math-expr">${a} × ${b}</span>`,
          answer: String(ans),
          diagnose(val) {
            const tens = Math.floor(b / 10);
            const ones = b % 10;
            if (val === String(a * ones + a * tens)) {
              return `Faltó el cero de las decenas: el ${tens} de ${b} vale ${tens * 10}, no ${tens}.`;
            }
            return "";
          },
          explain: `${a} × ${Math.floor(b / 10) * 10} + ${a} × ${b % 10} = ${a * Math.floor(b / 10) * 10} + ${a * (b % 10)} = ${ans}.`,
        };
      }
      const divisor = randInt(12, 24);
      const q = randInt(11, 22);
      const dividend = divisor * q;
      return {
        topic: "mult_div",
        promptHtml: `<span class="math-expr">${dividend} ÷ ${divisor}</span>`,
        answer: String(q),
        diagnose() {
          return `Probá por cocientes parciales: ${divisor} × 10 = ${divisor * 10}, y restá eso de ${dividend}.`;
        },
        explain: `${divisor} × ${q} = ${dividend}, así que ${dividend} ÷ ${divisor} = ${q}.`,
      };
    },
  },
  fractions: {
    name: "Fracciones",
    strategyHint: "Convertí ambas fracciones a un denominador común antes de sumar numeradores, y simplificá si comparten divisor.",
    worked: {
      problem: "2/3 + 1/4",
      visual: true,
      steps: [
        { expr: "8/12 + 3/12", why: "Buscamos denominador común (mcm de 3 y 4 = 12) multiplicando numerador y denominador para preservar el valor." },
        { expr: "(8 + 3) / 12 = 11/12", why: "Con el mismo denominador, simplemente sumamos los numeradores." },
      ],
    },
    faded: {
      problem: "1/2 + 1/3",
      given: "Denominador común = 6 → 1/2 = 3/6 y 1/3 = 2/6",
      blankPrompt: "¿Qué numerador queda al sumar 3 + 2?",
      blankAnswer: "5",
      finalPrompt: "Fracción final (ej. 5/6):",
      finalAnswer: "5/6",
    },
    generate(level = 1) {
      const pairs = level === 1 ? [[2, 3], [3, 4], [2, 5]] : level === 2 ? [[3, 5], [4, 5], [3, 8]] : [[4, 6], [5, 6], [4, 9], [6, 8]];
      const [d1, d2] = pairs[randInt(0, pairs.length - 1)];
      const n1 = randInt(1, d1 - 1);
      const n2 = randInt(1, d2 - 1);
      const num = n1 * d2 + n2 * d1;
      const den = d1 * d2;
      const g = gcd(num, den);
      const sNum = num / g;
      const sDen = den / g;
      const naiveTrap = `${n1 + n2}/${d1 + d2}`;
      const unsimplified = `${num}/${den}`;
      return {
        topic: "fractions",
        promptHtml: `<span class="math-expr"><span class="math-frac"><span>${n1}</span><span>${d1}</span></span> + <span class="math-frac"><span>${n2}</span><span>${d2}</span></span></span> <span class="xs muted">(simplificada, ej. 5/6)</span>`,
        answer: sDen === 1 ? String(sNum) : `${sNum}/${sDen}`,
        diagnose(val) {
          if (val === naiveTrap) return "Trampa frecuente: nunca se suman los denominadores entre sí. Primero pasá ambas fracciones al mismo denominador común.";
          if (val === unsimplified && g > 1) return `El valor es equivalente pero faltó simplificar dividiendo arriba y abajo por ${g}.`;
          return "";
        },
        explain: `Denominador común ${den}: ${n1 * d2}/${den} + ${n2 * d1}/${den} = ${num}/${den} → ${sDen === 1 ? sNum : sNum + "/" + sDen}.`,
      };
    },
  },
  decimals: {
    name: "Decimales",
    strategyHint: "Para sumar/restar alineá la coma y rellená con ceros (5 = 5.00). Para multiplicar contá el total de cifras decimales.",
    worked: {
      problem: "10 − 3.65",
      steps: [
        { expr: "10.00 − 3.65", why: "Todo entero tiene coma y ceros al final: alinear la coma evita mezclar décimos con centésimos." },
        { expr: "6.35", why: "De 3.65 a 4.00 faltan 0.35, y de 4.00 a 10.00 faltan 6 → 6.35." },
      ],
    },
    faded: {
      problem: "0.3 × 0.4",
      given: "Ignoramos las comas primero: 3 × 4 = 12",
      blankPrompt: "¿Cuántas cifras decimales suman entre 0.3 (1) y 0.4 (1)?",
      blankAnswer: "2",
      finalPrompt: "Resultado con la coma puesta (ej. 0.12):",
      finalAnswer: "0.12",
    },
    generate(level = 1) {
      if (level === 1) {
        const a = randInt(12, 48) / 10;
        const b = randInt(15, 85) / 100;
        const ans = Number((a + b).toFixed(2));
        return {
          topic: "decimals",
          promptHtml: `<span class="math-expr">${a.toFixed(1)} + ${b.toFixed(2)}</span>`,
          answer: String(ans),
          diagnose() {
            return `Alineá la coma escribiendo ${a.toFixed(1)} como ${a.toFixed(2)} antes de sumar.`;
          },
          explain: `${a.toFixed(2)} + ${b.toFixed(2)} = ${ans}.`,
        };
      }
      if (level === 2) {
        const a = randInt(2, 9);
        const b = randInt(2, 9);
        const ans = Number(((a * b) / 100).toFixed(2));
        return {
          topic: "decimals",
          promptHtml: `<span class="math-expr">0.${a} × 0.${b}</span>`,
          answer: String(ans),
          diagnose(val) {
            if (val === String(Number(((a * b) / 10).toFixed(1)))) {
              return "Corriste solo 1 lugar decimal: entre los dos factores hay 1 + 1 = 2 decimales.";
            }
            return "";
          },
          explain: `${a} × ${b} = ${a * b}, con 2 cifras decimales → ${ans}.`,
        };
      }
      const d = [2, 4, 5, 8][randInt(0, 3)];
      const q = randInt(3, 14);
      const num = Number(((d * q) / 10).toFixed(1));
      const div = Number((d / 10).toFixed(1));
      return {
        topic: "decimals",
        promptHtml: `<span class="math-expr">${num} ÷ ${div}</span>`,
        answer: String(q),
        diagnose(val) {
          if (val === String(q / 10)) return "Te olvidaste de correr la coma también en el dividendo: multiplicá ambos por 10.";
          return "";
        },
        explain: `Multiplicando ambos por 10 queda ${Math.round(num * 10)} ÷ ${d} = ${q}.`,
      };
    },
  },
  powers: {
    name: "Exponentes y potencias de 10",
    strategyHint: "Multiplicar por 10ⁿ corre la coma n lugares a la derecha; al multiplicar potencias de igual base se suman los exponentes.",
    worked: {
      problem: "3.45 × 10³",
      steps: [
        { expr: "10³ = 10 × 10 × 10 = 1000", why: "El exponente 3 indica multiplicar por 10 tres veces (3 ceros)." },
        { expr: "3.45 × 1000 = 3450", why: "Corremos la coma 3 lugares hacia la derecha y completamos el espacio vacío con un cero." },
      ],
    },
    faded: {
      problem: "Simplificar 2³ · 2² y calcular su valor",
      given: "Misma base multiplicándose → sumamos exponentes: 3 + 2",
      blankPrompt: "¿Qué exponente queda en 2^(?)?",
      blankAnswer: "5",
      finalPrompt: "Valor numérico de 2⁵:",
      finalAnswer: "32",
    },
    generate(level = 1) {
      if (level === 1) {
        const base = randInt(12, 89) / 10;
        const exp = randInt(2, 3);
        const ans = Math.round(base * 10 ** exp);
        return {
          topic: "powers",
          promptHtml: `<span class="math-expr">${base.toFixed(1)} × 10<sup>${exp}</sup></span>`,
          answer: String(ans),
          diagnose(val) {
            if (val === String(ans / 10) || val === String(ans * 10)) {
              return `Revisá cuántos lugares corriste la coma: 10^${exp} mueve exactamente ${exp} lugares a la derecha.`;
            }
            return "";
          },
          explain: `Multiplicar ${base.toFixed(1)} por ${10 ** exp} corre la coma ${exp} lugares → ${ans}.`,
        };
      }
      const a = level === 3 ? randInt(4, 8) : randInt(2, 5);
      const b = level === 3 ? randInt(-3, -1) : randInt(1, 4);
      const exp = a + b;
      const multTrap = a * b;
      return {
        topic: "powers",
        promptHtml: `<span class="math-expr">Si 2<sup>${a}</sup> · 2<sup>${b}</sup> = 2<sup>k</sup>, ¿cuánto vale k?</span>`,
        answer: String(exp),
        diagnose(val) {
          if (val === String(multTrap)) return "Cuidado: los exponentes se SUMAN al multiplicar potencias de igual base (no se multiplican entre sí).";
          return "";
        },
        explain: `Al multiplicar potencias de igual base se suman los exponentes: ${a} + (${b}) = ${exp}.`,
      };
    },
  },
  integers: {
    name: "Negativos y orden de operaciones",
    strategyHint: "Resolvé primero el interior del paréntesis, luego la multiplicación respetando regla de signos, y al final la suma/resta.",
    worked: {
      problem: "12 − 3 · (2 − 6)",
      steps: [
        { expr: "12 − 3 · (−4)", why: "Resolvemos primero lo que está dentro del paréntesis: 2 − 6 = −4." },
        { expr: "12 + 12", why: "La multiplicación tiene prioridad sobre la resta: (−3) · (−4) = +12 (menos por menos es más)." },
        { expr: "24", why: "Finalmente sumamos los términos restantes." },
      ],
    },
    faded: {
      problem: "10 − 2 · (3 − 8)",
      given: "Paso 1 (paréntesis): 10 − 2 · (−5)",
      blankPrompt: "¿Cuánto da −2 · (−5)?",
      blankAnswer: "10",
      finalPrompt: "Resultado final (10 + ese valor):",
      finalAnswer: "20",
    },
    generate(level = 1) {
      const a = level === 1 ? randInt(6, 15) : level === 2 ? randInt(-8, 18) : randInt(-16, 14);
      const b = level === 3 ? randInt(3, 7) : randInt(2, 5);
      const c = randInt(1, 5);
      const d = randInt(c + 2, c + (level === 3 ? 9 : 6));
      const ans = a - b * (c - d);
      const pemdasTrap = (a - b) * (c - d);
      const signTrap = a + b * (c - d);
      return {
        topic: "integers",
        promptHtml: `<span class="math-expr">${a} − ${b} · (${c} − ${d})</span>`,
        answer: String(ans),
        diagnose(val) {
          if (val === String(pemdasTrap)) return "Error típico de PEMDAS: hiciste la resta antes de multiplicar. Siempre multiplicá primero.";
          if (val === String(signTrap)) return "Error de signo: recordá que menos por menos da positivo (−" + b + " · (" + (c - d) + ") = +" + (-b * (c - d)) + ").";
          return "";
        },
        explain: `Paréntesis: ${c} − ${d} = ${c - d}. Luego −${b} · (${c - d}) = ${-b * (c - d)}. Total: ${a} + ${-b * (c - d)} = ${ans}.`,
      };
    },
  },
  percentages: {
    group: "Preálgebra",
    name: "Porcentajes y proporciones",
    strategyHint: "Descomponé el porcentaje en bloques sencillos como 10% (dividir por 10) y 5% (la mitad del 10%).",
    worked: {
      problem: "Calcular el 15% de 240",
      steps: [
        { expr: "10% de 240 = 24", why: "El 10% siempre equivale a dividir por 10 (correr la coma un lugar)." },
        { expr: "5% de 240 = 12", why: "El 5% es exactamente la mitad del 10%." },
        { expr: "15% = 24 + 12 = 36", why: "Descomponer porcentajes evita errores y desarrolla agilidad mental." },
      ],
    },
    faded: {
      problem: "Calcular el 25% de 160",
      given: "25% equivale a 1/4 (la cuarta parte)",
      blankPrompt: "¿Cuánto es la mitad (50%) de 160?",
      blankAnswer: "80",
      finalPrompt: "Y la mitad de eso (25% de 160):",
      finalAnswer: "40",
    },
    generate(level = 1) {
      const pcts = level === 1 ? [10, 20, 25, 50] : level === 2 ? [15, 30, 35, 40] : [12, 18, 24, 35, 65];
      const p = pcts[randInt(0, pcts.length - 1)];
      const base = level === 3 ? randInt(3, 12) * 50 : randInt(2, 14) * 20;
      const ans = (base * p) / 100;
      return {
        topic: "percentages",
        promptHtml: `<span class="math-expr">¿Cuánto es el ${p}% de ${base}?</span>`,
        answer: String(ans),
        diagnose(val) {
          if (val === String(ans * 10) || val === String(ans / 10)) return "Error de coma decimal: revisá cuántas posiciones movés al dividir por 100.";
          return "";
        },
        explain: `${p}% de ${base} = ${base} × ${(p / 100).toFixed(2)} = ${ans}.`,
      };
    },
  },
  linear_eq: {
    group: "Preálgebra",
    name: "Ecuaciones lineales",
    strategyHint: "Aplicá operaciones inversas a ambos lados de la balanza: primero deshacé la suma/resta y al final la multiplicación.",
    worked: {
      problem: "3x − 7 = 14",
      steps: [
        { expr: "3x = 21", why: "Sumamos 7 a ambos lados para cancelar el −7 y mantener la balanza equilibrada." },
        { expr: "x = 7", why: "Dividimos ambos lados por 3 para despejar x. Verificación: 3(7) − 7 = 14." },
      ],
    },
    faded: {
      problem: "4x + 5 = 29",
      given: "Restamos 5 en ambos lados → 4x = 24",
      blankPrompt: "¿Por qué número debemos dividir ambos lados?",
      blankAnswer: "4",
      finalPrompt: "Valor de x:",
      finalAnswer: "6",
    },
    generate(level = 1) {
      const m = level === 3 ? randInt(-6, -2) : randInt(2, 6);
      const x = level === 1 ? randInt(1, 8) : randInt(-6, 9);
      const b = randInt(1, 12);
      const rhs = m * x + b;
      return {
        topic: "linear_eq",
        promptHtml: `<span class="math-expr">Resolvé para x: &nbsp; ${m}x + ${b} = ${rhs}</span>`,
        answer: String(x),
        diagnose(val) {
          if (val === String(rhs - b)) return `Faltó el último paso: llegaste a ${m}x = ${rhs - b}, ahora dividí ambos lados por ${m}.`;
          if (val === String((rhs + b) / m)) return `Error de signo al despejar: como +${b} suma, tenés que RESTAR ${b} en ambos lados.`;
          return "";
        },
        explain: `Restamos ${b}: ${m}x = ${rhs - b}. Dividimos por ${m}: x = ${x}.`,
      };
    },
  },
  linear_fn: {
    group: "Preálgebra",
    name: "Funciones lineales (y = mx + b)",
    strategyHint: "Sustituí el valor indicado dentro de f(x) respetando primero la multiplicación m·x y luego sumando o restando b.",
    worked: {
      problem: "En y = 2x − 3, hallar y cuando x = 4",
      steps: [
        { expr: "y = 2(4) − 3", why: "Sustituimos la entrada x = 4 en la regla de la función." },
        { expr: "y = 8 − 3 = 5", why: "La pendiente m=2 indica que sube 2 por cada paso en x; b=−3 es el inicio en x=0." },
      ],
    },
    faded: {
      problem: "Una recta tiene pendiente m = 3 y pasa por (0, 2)",
      given: "Su ecuación es y = 3x + 2",
      blankPrompt: "¿Cuánto vale y cuando x = 0?",
      blankAnswer: "2",
      finalPrompt: "¿Cuánto vale y cuando x = 4?",
      finalAnswer: "14",
    },
    generate(level = 1) {
      const m = level === 1 ? randInt(1, 4) : randInt(-4, 5) || -2;
      const b = randInt(-5, 8);
      const x = level === 3 ? randInt(-5, -1) : randInt(1, 6);
      const y = m * x + b;
      const bStr = b >= 0 ? `+ ${b}` : `− ${Math.abs(b)}`;
      return {
        topic: "linear_fn",
        promptHtml: `<span class="math-expr">Dada f(x) = ${m}x ${bStr}, calculá f(${x})</span>`,
        answer: String(y),
        diagnose(val) {
          if (val === String(m * x)) return "Te olvidaste de sumar/restar la ordenada al origen (b).";
          return "";
        },
        explain: `f(${x}) = ${m}(${x}) ${bStr} = ${m * x} ${bStr} = ${y}.`,
      };
    },
  },
  systems: {
    group: "Preálgebra",
    name: "Sistemas 2×2",
    strategyHint: "Observá los signos de y en ambas ecuaciones: al sumarlas término a término, +y y −y se cancelan de inmediato.",
    worked: {
      problem: "x + y = 10  y  x − y = 4",
      steps: [
        { expr: "2x = 14", why: "Sumamos ambas ecuaciones término a término: (+y) + (−y) = 0." },
        { expr: "x = 7,  y = 3", why: "Despejamos x = 7 y sustituimos en x + y = 10 para hallar y = 3." },
      ],
    },
    faded: {
      problem: "x + y = 12  y  x − y = 2",
      given: "Sumando ambas ecuaciones: 2x = 14",
      blankPrompt: "¿Cuánto vale x?",
      blankAnswer: "7",
      finalPrompt: "Sustituyendo en x + y = 12, ¿cuánto vale y?",
      finalAnswer: "5",
    },
    generate(level = 1) {
      const x = level === 3 ? randInt(-6, 12) : randInt(3, 10);
      const y = randInt(1, 7);
      return {
        topic: "systems",
        promptHtml: `<span class="math-expr">Sistema: x + y = ${x + y} &nbsp;y&nbsp; x − y = ${x - y}. &nbsp;¿Cuánto vale x?</span>`,
        answer: String(x),
        diagnose(val) {
          if (val === String(2 * x)) return "Casi: sumaste bien las ecuaciones obteniendo 2x = " + (2 * x) + ", solo faltó dividir por 2.";
          if (val === String(y)) return "Hallaste el valor de y en vez de x. Revisá cuál incógnita pedía la consigna.";
          return "";
        },
        explain: `Sumando las ecuaciones: 2x = ${2 * x} → x = ${x} (y además y = ${y}).`,
      };
    },
  },
  exponentials: {
    group: "Álgebra 1",
    name: "Crecimiento y decaimiento exponencial",
    strategyHint: "En y = a · bˣ, a es el valor inicial y b el factor multiplicativo en cada paso (por ej. ×2 duplica, ×0.5 divide por 2).",
    worked: {
      problem: "P(t) = 50 · 2^t para t = 4",
      steps: [
        { expr: "2⁴ = 2 · 2 · 2 · 2 = 16", why: "Primero resolvemos el exponente antes de multiplicar por el valor inicial." },
        { expr: "50 · 16 = 800", why: "Multiplicamos el valor inicial (50) por el factor acumulado (16)." },
      ],
    },
    faded: {
      problem: "C(n) = 160 · (0.5)^n para n = 3",
      given: "Cada período divide a la mitad: (0.5)³ = 1/8",
      blankPrompt: "¿Cuánto queda tras 2 períodos (160 ÷ 4)?",
      blankAnswer: "40",
      finalPrompt: "Y tras el 3er período (dividir por 2 otra vez):",
      finalAnswer: "20",
    },
    generate(level = 1) {
      if (level === 1) {
        const a = [10, 20, 25, 50][randInt(0, 3)];
        const t = randInt(2, 4);
        const ans = a * 2 ** t;
        return {
          topic: "exponentials",
          promptHtml: `<span class="math-expr">Si P(t) = ${a} · 2<sup>t</sup>, calculá P(${t})</span>`,
          answer: String(ans),
          diagnose(val) {
            if (val === String(a * 2 * t)) return `Cuidado: 2^${t} es multiplicar 2 por sí mismo ${t} veces (${2 ** t}), no 2 × ${t}.`;
            return "";
          },
          explain: `2^${t} = ${2 ** t}, y ${a} × ${2 ** t} = ${ans}.`,
        };
      }
      if (level === 2) {
        const a = [80, 160, 240, 320][randInt(0, 3)];
        const t = randInt(2, 3);
        const ans = a / 2 ** t;
        return {
          topic: "exponentials",
          promptHtml: `<span class="math-expr">Vida media: C(n) = ${a} · (0.5)<sup>n</sup>. ¿Cuánto vale C(${t})?</span>`,
          answer: String(ans),
          diagnose() {
            return `Dividí ${a} por 2 exactamente ${t} veces seguidas.`;
          },
          explain: `${a} ÷ ${2 ** t} = ${ans}.`,
        };
      }
      const a = [100, 200, 500, 1000][randInt(0, 3)];
      const ans = Math.round(a * 1.21);
      return {
        topic: "exponentials",
        promptHtml: `<span class="math-expr">Interés compuesto (+10%/año): $${a} · (1.10)<sup>2</sup></span>`,
        answer: String(ans),
        diagnose(val) {
          if (val === String(Math.round(a * 1.2))) return "Eso es interés simple (+20%): en compuesto, 1.10² = 1.21 (+21%).";
          return "";
        },
        explain: `1.10² = 1.21 → ${a} × 1.21 = ${ans}.`,
      };
    },
  },
  factoring: {
    group: "Álgebra 1",
    name: "Binomios y factorización cuadrática",
    strategyHint: "Para factorizar x² + bx + c = 0 buscá dos números p y q que sumen b y multipliquen c; luego las raíces son −p y −q.",
    worked: {
      problem: "Resolver x² − 5x + 6 = 0 factorizando",
      steps: [
        { expr: "(x − 2)(x − 3) = 0", why: "Buscamos dos números que multipliquen +6 y sumen −5: son −2 y −3." },
        { expr: "x = 2  o  x = 3", why: "Por la propiedad del producto cero, igualamos cada paréntesis a 0." },
      ],
    },
    faded: {
      problem: "Expandir (x + 4)²",
      given: "(x + 4)(x + 4) = x² + 4x + 4x + 16",
      blankPrompt: "¿Qué coeficiente queda delante de x (4 + 4)?",
      blankAnswer: "8",
      finalPrompt: "¿Y el término independiente (4 × 4)?",
      finalAnswer: "16",
    },
    generate(level = 1) {
      const r1 = randInt(1, level === 1 ? 5 : 7);
      const r2 = randInt(r1 + 1, level === 1 ? 6 : 9);
      const b = -(r1 + r2);
      const c = r1 * r2;
      return {
        topic: "factoring",
        promptHtml: `<span class="math-expr">Resolvé x² − ${r1 + r2}x + ${c} = 0. ¿Cuál es la solución MAYOR?</span>`,
        answer: String(r2),
        diagnose(val) {
          if (val === String(r1)) return `Bien factorizado: las dos raíces son ${r1} y ${r2}, pero pedía la MAYOR (${r2}).`;
          if (val === String(-r2)) return "Cuidado con el signo al despejar: de (x − " + r2 + ") = 0 sale x = +" + r2 + ".";
          return "";
        },
        explain: `(x − ${r1})(x − ${r2}) = 0 → soluciones x = ${r1} y x = ${r2} (la mayor es ${r2}).`,
      };
    },
  },
  quadratics: {
    group: "Álgebra 1",
    name: "Parábolas, vértice y discriminante",
    strategyHint: "El vértice de y = ax² + bx + c está siempre en x = −b / (2a), y el discriminante es Δ = b² − 4ac.",
    worked: {
      problem: "Hallar el vértice de h(t) = −5t² + 20t + 2",
      steps: [
        { expr: "t = −20 / (2 · (−5)) = 2", why: "Aplicamos x = −b / (2a) con a = −5 y b = 20." },
        { expr: "h(2) = −5(4) + 20(2) + 2 = 22", why: "Evaluamos en t = 2 para hallar la altura máxima de la parábola." },
      ],
    },
    faded: {
      problem: "Discriminante de x² − 6x + 5 = 0",
      given: "a = 1, b = −6, c = 5 → Δ = b² − 4ac = (−6)² − 4(1)(5)",
      blankPrompt: "¿Cuánto vale (−6)²?",
      blankAnswer: "36",
      finalPrompt: "Resultado final de Δ = 36 − 20:",
      finalAnswer: "16",
    },
    generate(level = 1) {
      if (level <= 2) {
        const a = level === 1 ? 1 : [1, 2, -1, -2][randInt(0, 3)];
        const h = randInt(-5, 6) || 3;
        const b = -2 * a * h;
        const c = randInt(-6, 8) || 2;
        const bStr = b > 0 ? `+ ${b}x` : `− ${Math.abs(b)}x`;
        const cStr = c > 0 ? `+ ${c}` : `− ${Math.abs(c)}`;
        const aStr = a === 1 ? "" : a === -1 ? "−" : String(a);
        return {
          topic: "quadratics",
          promptHtml: `<span class="math-expr">¿En qué x está el vértice de y = ${aStr}x² ${bStr} ${cStr}?</span>`,
          answer: String(h),
          diagnose(val) {
            if (val === String(-h)) return "Error de signo en la fórmula del vértice: recordá el menos adelante en x = −b / (2a).";
            if (val === String(2 * h)) return "Te olvidaste de dividir por 2a.";
            return "";
          },
          explain: `x = −(${b}) / (2 · ${a}) = ${-b} / ${2 * a} = ${h}.`,
        };
      }
      const a = 1;
      const b = randInt(-6, 6) || -4;
      const c = randInt(-4, 6) || 3;
      const delta = b * b - 4 * a * c;
      const bStr = b > 0 ? `+ ${b}x` : `− ${Math.abs(b)}x`;
      const cStr = c > 0 ? `+ ${c}` : `− ${Math.abs(c)}`;
      return {
        topic: "quadratics",
        promptHtml: `<span class="math-expr">Calculá el discriminante Δ = b² − 4ac de x² ${bStr} ${cStr} = 0</span>`,
        answer: String(delta),
        diagnose() {
          return `Reemplazá a = 1, b = ${b}, c = ${c} en b² − 4ac (recordá que b² siempre es ≥ 0).`;
        },
        explain: `Δ = (${b})² − 4(1)(${c}) = ${b * b} − (${4 * c}) = ${delta}.`,
      };
    },
  },
  geometry_angles: {
    group: "Geometría",
    name: "Ángulos, triángulos y semejanza",
    strategyHint: "Los ángulos de un triángulo suman 180°, una línea recta suma 180°, y al escalar por k el área se multiplica por k².",
    worked: {
      problem: "Hallar el 3er ángulo de un triángulo con 48° y 75°",
      steps: [
        { expr: "48° + 75° = 123°", why: "Sumamos los dos ángulos interiores conocidos." },
        { expr: "180° − 123° = 57°", why: "Los tres ángulos de cualquier triángulo siempre suman 180°." },
      ],
    },
    faded: {
      problem: "Suma de ángulos internos de un hexágono (6 lados)",
      given: "Fórmula de polígonos: (n − 2) · 180° con n = 6",
      blankPrompt: "¿En cuántos triángulos se divide (6 − 2)?",
      blankAnswer: "4",
      finalPrompt: "Suma total (4 × 180°):",
      finalAnswer: "720",
    },
    generate(level = 1) {
      if (level === 1) {
        const a = randInt(25, 85);
        const b = randInt(25, 130 - a);
        const c = 180 - a - b;
        return {
          topic: "geometry_angles",
          promptHtml: `<span class="math-expr">Un triángulo tiene ángulos ${a}° y ${b}°. ¿Cuánto mide el tercer ángulo (en °)?</span>`,
          answer: String(c),
          diagnose(val) {
            if (val === String(a + b)) return "Sumaste los dos ángulos conocidos; ahora restá ese resultado a 180°.";
            return "";
          },
          explain: `180° − (${a}° + ${b}°) = 180° − ${a + b}° = ${c}°.`,
        };
      }
      if (level === 2) {
        const n = randInt(4, 8);
        const ans = (n - 2) * 180;
        return {
          topic: "geometry_angles",
          promptHtml: `<span class="math-expr">¿Cuánto suman los ángulos internos de un polígono de ${n} lados (en °)?</span>`,
          answer: String(ans),
          diagnose(val) {
            if (val === String(n * 180)) return "Cuidado: se multiplica (n − 2) por 180°, no n por 180°.";
            return "";
          },
          explain: `(${n} − 2) × 180° = ${n - 2} × 180° = ${ans}°.`,
        };
      }
      const k = randInt(2, 5);
      const baseArea = randInt(3, 12) * 5;
      const ans = baseArea * k * k;
      return {
        topic: "geometry_angles",
        promptHtml: `<span class="math-expr">Una figura de ${baseArea} cm² se amplía con factor k = ${k}. ¿Nueva área (cm²)?</span>`,
        answer: String(ans),
        diagnose(val) {
          if (val === String(baseArea * k)) return `El área escala con k² = ${k * k}, no con k = ${k}.`;
          return "";
        },
        explain: `Área nueva = ${baseArea} × ${k}² = ${baseArea} × ${k * k} = ${ans} cm².`,
      };
    },
  },
  pythagoras_trig: {
    group: "Geometría",
    name: "Pitágoras y trigonometría básica",
    strategyHint: "Identificá primero la hipotenusa (lado más largo frente a 90°): para hallarla sumás cuadrados; para un cateto restás.",
    worked: {
      problem: "Escalera de 13 m apoyada a 5 m de la pared: hallar altura",
      steps: [
        { expr: "h² = 13² − 5² = 169 − 25 = 144", why: "13 m es la hipotenusa, así que despejamos el cateto restando." },
        { expr: "h = √144 = 12 m", why: "Sacamos la raíz cuadrada para obtener la altura exacta." },
      ],
    },
    faded: {
      problem: "Catetos 6 cm y 8 cm: hallar hipotenusa c",
      given: "c² = 6² + 8² = 36 + 64",
      blankPrompt: "¿Cuánto vale 36 + 64?",
      blankAnswer: "100",
      finalPrompt: "Hipotenusa c = √100:",
      finalAnswer: "10",
    },
    generate(level = 1) {
      const triples = [
        [3, 4, 5],
        [5, 12, 13],
        [6, 8, 10],
        [8, 15, 17],
        [9, 12, 15],
      ];
      const [a, b, c] = triples[randInt(0, triples.length - 1)];
      if (level === 1) {
        return {
          topic: "pythagoras_trig",
          promptHtml: `<span class="math-expr">Catetos a = ${a} y b = ${b}. ¿Cuánto mide la hipotenusa c?</span>`,
          answer: String(c),
          diagnose(val) {
            if (val === String(c * c)) return "Te faltó el último paso: sacar la raíz cuadrada de " + (c * c) + ".";
            if (val === String(a + b)) return "No se suman los catetos directo: usá √(a² + b²).";
            return "";
          },
          explain: `c = √(${a}² + ${b}²) = √(${a * a} + ${b * b}) = √${c * c} = ${c}.`,
        };
      }
      if (level === 2) {
        return {
          topic: "pythagoras_trig",
          promptHtml: `<span class="math-expr">Hipotenusa c = ${c} y cateto a = ${a}. ¿Cuánto mide el otro cateto b?</span>`,
          answer: String(b),
          diagnose(val) {
            if (val === String(b * b)) return "Sacá la raíz cuadrada de " + (b * b) + ".";
            return "Como buscás un cateto, RESTÁ cuadrados: √(c² − a²).";
          },
          explain: `b = √(${c}² − ${a}²) = √(${c * c} − ${a * a}) = √${b * b} = ${b}.`,
        };
      }
      const hyp = randInt(2, 10) * 4;
      const ans = hyp / 2;
      return {
        topic: "pythagoras_trig",
        promptHtml: `<span class="math-expr">Rampa de ${hyp} m inclinada 30° (sen 30° = 0.5). ¿Qué altura alcanza (m)?</span>`,
        answer: String(ans),
        diagnose(val) {
          if (val === String(hyp * 2)) return "La altura (cateto opuesto) siempre es menor que la hipotenusa: multiplicá por 0.5.";
          return "";
        },
        explain: `h = ${hyp} × sen(30°) = ${hyp} × 0.5 = ${ans} m.`,
      };
    },
  },
  geometry_coords: {
    group: "Geometría",
    name: "Geometría analítica y circunferencia",
    strategyHint: "Distancia = √(Δx² + Δy²), punto medio = promedio de coordenadas, y en (x − h)² + (y − k)² = r² el radio es √(r²).",
    worked: {
      problem: "Distancia entre A(1, 2) y B(4, 6)",
      steps: [
        { expr: "Δx = 4 − 1 = 3,  Δy = 6 − 2 = 4", why: "Restamos coordenadas para formar los dos catetos." },
        { expr: "d = √(3² + 4²) = √25 = 5", why: "Aplicamos Pitágoras para hallar la distancia directa." },
      ],
    },
    faded: {
      problem: "Radio de (x − 2)² + (y + 5)² = 36",
      given: "El número de la derecha corresponde a r² = 36",
      blankPrompt: "¿Qué centro h tiene (x − 2)²?",
      blankAnswer: "2",
      finalPrompt: "Valor del radio r = √36:",
      finalAnswer: "6",
    },
    generate(level = 1) {
      if (level === 1) {
        const [dx, dy, d] = [
          [3, 4, 5],
          [6, 8, 10],
          [5, 12, 13],
        ][randInt(0, 2)];
        const x1 = randInt(-3, 5);
        const y1 = randInt(-3, 5);
        return {
          topic: "geometry_coords",
          promptHtml: `<span class="math-expr">Distancia entre (${x1}, ${y1}) y (${x1 + dx}, ${y1 + dy})</span>`,
          answer: String(d),
          diagnose(val) {
            if (val === String(dx + dy)) return "Sumaste Δx + Δy en vez de usar Pitágoras √(Δx² + Δy²).";
            return "";
          },
          explain: `Δx = ${dx}, Δy = ${dy} → d = √(${dx * dx} + ${dy * dy}) = ${d}.`,
        };
      }
      if (level === 2) {
        const xm = randInt(-4, 6);
        const ym = randInt(-4, 6);
        const dx = randInt(1, 5);
        const dy = randInt(1, 5);
        return {
          topic: "geometry_coords",
          promptHtml: `<span class="math-expr">Punto medio entre (${xm - dx}, ${ym - dy}) y (${xm + dx}, ${ym + dy}). ¿Coordenada x?</span>`,
          answer: String(xm),
          diagnose(val) {
            if (val === String(2 * xm)) return "Te faltó dividir la suma por 2.";
            return "";
          },
          explain: `x_M = ((${xm - dx}) + (${xm + dx})) / 2 = ${xm}.`,
        };
      }
      const h = randInt(-5, 5) || 2;
      const k = randInt(-5, 5) || -3;
      const r = randInt(2, 9);
      const hStr = h > 0 ? `− ${h}` : `+ ${Math.abs(h)}`;
      const kStr = k > 0 ? `− ${k}` : `+ ${Math.abs(k)}`;
      return {
        topic: "geometry_coords",
        promptHtml: `<span class="math-expr">Radio de la circunferencia (x ${hStr})² + (y ${kStr})² = ${r * r}</span>`,
        answer: String(r),
        diagnose(val) {
          if (val === String(r * r)) return `Ojo: ${r * r} es r², tenés que sacar la raíz cuadrada.`;
          return "";
        },
        explain: `El lado derecho es r² = ${r * r} → r = √${r * r} = ${r}.`,
      };
    },
  },
  geometry_3d: {
    group: "Geometría",
    name: "Círculos, arcos y volúmenes 3D",
    strategyHint: "Ángulo inscrito = central / 2; cono o pirámide = 1/3 del cilindro/prisma; en 3D el volumen escala con k³.",
    worked: {
      problem: "Cono de igual base y altura que un cilindro de 900 mL",
      steps: [
        { expr: "V_cono = (1/3) · V_cilindro", why: "Todo cono o pirámide ocupa un tercio del prisma/cilindro que lo contiene." },
        { expr: "900 ÷ 3 = 300 mL", why: "Dividimos el volumen del cilindro por 3." },
      ],
    },
    faded: {
      problem: "Escalar una caja 3D por factor k = 2 (volumen original 15 L)",
      given: "En 3 dimensiones el volumen se multiplica por k³ = 2³",
      blankPrompt: "¿Cuánto vale 2³?",
      blankAnswer: "8",
      finalPrompt: "Nuevo volumen (15 × 8) en litros:",
      finalAnswer: "120",
    },
    generate(level = 1) {
      if (level === 1) {
        const central = randInt(4, 15) * 10;
        const insc = central / 2;
        return {
          topic: "geometry_3d",
          promptHtml: `<span class="math-expr">Si un ángulo central mide ${central}°, ¿cuánto mide el ángulo inscrito del mismo arco (en °)?</span>`,
          answer: String(insc),
          diagnose(val) {
            if (val === String(central * 2)) return "Al revés: el ángulo inscrito mide la MITAD del ángulo central.";
            return "";
          },
          explain: `Ángulo inscrito = ${central}° ÷ 2 = ${insc}°.`,
        };
      }
      if (level === 2) {
        const cone = randInt(3, 15) * 50;
        const cyl = cone * 3;
        return {
          topic: "geometry_3d",
          promptHtml: `<span class="math-expr">Un cilindro carga ${cyl} mL. ¿Cuántos mL carga un cono de igual radio y altura?</span>`,
          answer: String(cone),
          diagnose(val) {
            if (val === String(cyl / 2)) return "La relación cono/cilindro es 1/3, no 1/2.";
            return "";
          },
          explain: `V_cono = ${cyl} ÷ 3 = ${cone} mL.`,
        };
      }
      const k = randInt(2, 4);
      const v0 = randInt(2, 10) * 5;
      const ans = v0 * k * k * k;
      return {
        topic: "geometry_3d",
        promptHtml: `<span class="math-expr">Un sólido de ${v0} cm³ se amplía con factor k = ${k} en 3D. ¿Nuevo volumen (cm³)?</span>`,
        answer: String(ans),
        diagnose(val) {
          if (val === String(v0 * k)) return `El volumen escala con k³ = ${k ** 3}, no con k.`;
          if (val === String(v0 * k * k)) return `k² = ${k * k} es para áreas; en 3D el volumen escala con k³ = ${k ** 3}.`;
          return "";
        },
        explain: `V_nuevo = ${v0} × ${k}³ = ${v0} × ${k ** 3} = ${ans} cm³.`,
      };
    },
  },
  complex_nums: {
    group: "Álgebra 2",
    name: "Números complejos (a + bi)",
    strategyHint: "Recordá siempre i² = −1, el ciclo de 4 para iⁿ, y que (a + bi)(a − bi) = a² + b².",
    worked: {
      problem: "Parte real de (2 + 3i)(4 − i)",
      steps: [
        { expr: "8 − 2i + 12i − 3i²", why: "Aplicamos propiedad distributiva igual que con binomios." },
        { expr: "8 + 3 + 10i = 11 + 10i", why: "Reemplazamos i² = −1, así −3i² pasa a +3 y se suma a 8." },
      ],
    },
    faded: {
      problem: "Producto con conjugado (3 + 4i)(3 − 4i)",
      given: "Diferencia de cuadrados: 3² − (4i)² = 9 − 16i²",
      blankPrompt: "¿En qué se convierte −16i² al usar i² = −1?",
      blankAnswer: "16",
      finalPrompt: "Resultado final (9 + 16):",
      finalAnswer: "25",
    },
    generate(level = 1) {
      if (level === 1) {
        const a = randInt(-6, 8);
        const b = randInt(-6, 8);
        const c = randInt(-6, 8);
        const d = randInt(-6, 8);
        const bStr = b >= 0 ? `+ ${b}i` : `− ${Math.abs(b)}i`;
        const dStr = d >= 0 ? `+ ${d}i` : `− ${Math.abs(d)}i`;
        const ans = b + d;
        return {
          topic: "complex_nums",
          promptHtml: `<span class="math-expr">En (${a} ${bStr}) + (${c} ${dStr}), ¿cuánto vale la parte IMAGINARIA (coef. de i)?</span>`,
          answer: String(ans),
          diagnose(val) {
            if (val === String(a + c)) return "Esa es la parte real; la consigna pedía la parte imaginaria (coeficiente de i).";
            return "";
          },
          explain: `Sumamos partes imaginarias: ${b} + (${d}) = ${ans}.`,
        };
      }
      if (level === 2) {
        const a = randInt(1, 5);
        const b = randInt(1, 5);
        const c = randInt(1, 5);
        const d = randInt(1, 5);
        const real = a * c - b * d;
        return {
          topic: "complex_nums",
          promptHtml: `<span class="math-expr">En (${a} + ${b}i)(${c} + ${d}i), ¿cuál es la parte REAL?</span>`,
          answer: String(real),
          diagnose(val) {
            if (val === String(a * c + b * d)) return "Ojo con i² = −1: el producto (+bi)(+di) = +bdi² = −bd, se RESTA a ac.";
            return "";
          },
          explain: `Parte real = (${a})(${c}) − (${b})(${d}) = ${a * c} − ${b * d} = ${real}.`,
        };
      }
      const [a, b, mod] = [
        [3, 4, 5],
        [5, 12, 13],
        [6, 8, 10],
      ][randInt(0, 2)];
      return {
        topic: "complex_nums",
        promptHtml: `<span class="math-expr">Calculá el módulo |${a} + ${b}i| = √(a² + b²)</span>`,
        answer: String(mod),
        diagnose(val) {
          if (val === String(mod * mod)) return `Sacá la raíz cuadrada de ${mod * mod}.`;
          return "";
        },
        explain: `|${a} + ${b}i| = √(${a}² + ${b}²) = √${mod * mod} = ${mod}.`,
      };
    },
  },
  polynomials: {
    group: "Álgebra 2",
    name: "Polinomios, Teorema del Resto y asíntotas",
    strategyHint: "El resto de P(x) ÷ (x − c) es P(c); la asíntota vertical anula el denominador; el grado de un producto es la suma de exponentes.",
    worked: {
      problem: "Resto de dividir P(x) = x³ − 2x + 5 por (x − 2)",
      steps: [
        { expr: "c = 2 (anula x − 2)", why: "Identificamos el valor c con signo invertido al del divisor." },
        { expr: "P(2) = 8 − 4 + 5 = 9", why: "Por el Teorema del Resto, evaluar P(2) da el resto exacto." },
      ],
    },
    faded: {
      problem: "Resto de P(x) = x² + 5x + 10 dividido por (x + 3)",
      given: "Como x + 3 = x − (−3), evaluamos en c = −3",
      blankPrompt: "¿Cuánto vale (−3)²?",
      blankAnswer: "9",
      finalPrompt: "Resultado de P(−3) = 9 − 15 + 10:",
      finalAnswer: "4",
    },
    generate(level = 1) {
      if (level === 1) {
        const c = randInt(1, 3);
        const a = randInt(1, 3);
        const b = randInt(-4, 5);
        const d = randInt(-5, 8);
        const rem = a * c * c + b * c + d;
        const bStr = b >= 0 ? `+ ${b}x` : `− ${Math.abs(b)}x`;
        const dStr = d >= 0 ? `+ ${d}` : `− ${Math.abs(d)}`;
        return {
          topic: "polynomials",
          promptHtml: `<span class="math-expr">Resto de dividir (${a}x² ${bStr} ${dStr}) por (x − ${c})</span>`,
          answer: String(rem),
          diagnose() {
            return `Aplicá el Teorema del Resto: evaluá el polinomio en x = ${c}.`;
          },
          explain: `P(${c}) = ${a}(${c}²) + ${b}(${c}) + (${d}) = ${rem}.`,
        };
      }
      if (level === 2) {
        const v = randInt(-6, 8) || 3;
        const k = randInt(2, 9);
        const vStr = v > 0 ? `− ${v}` : `+ ${Math.abs(v)}`;
        return {
          topic: "polynomials",
          promptHtml: `<span class="math-expr">¿En qué x tiene asíntota vertical f(x) = ${k} / (x ${vStr})?</span>`,
          answer: String(v),
          diagnose(val) {
            if (val === String(-v)) return "Revisá el signo: buscá el valor de x que hace cero al denominador.";
            return "";
          },
          explain: `El denominador x ${vStr} = 0 se anula en x = ${v}.`,
        };
      }
      const m1 = randInt(1, 4);
      const m2 = randInt(2, 4);
      const deg = m1 + m2;
      return {
        topic: "polynomials",
        promptHtml: `<span class="math-expr">¿Cuál es el grado total de P(x) = −3(x − 1)<sup>${m1}</sup>(x + 4)<sup>${m2}</sup>?</span>`,
        answer: String(deg),
        diagnose(val) {
          if (val === String(m1 * m2)) return "Al multiplicar potencias de x se SUMAN los exponentes, no se multiplican.";
          return "";
        },
        explain: `Grado total = ${m1} + ${m2} = ${deg}.`,
      };
    },
  },
  logarithms: {
    group: "Álgebra 2",
    name: "Logaritmos y ecuaciones radicales",
    strategyHint: "log_b(y) = x equivale a bˣ = y; en ecuaciones radicales aislá la raíz, elevá al cuadrado y verificá.",
    worked: {
      problem: "Evaluar log₂(32)",
      steps: [
        { expr: "2^x = 32", why: "Reescribimos el logaritmo como pregunta de exponente." },
        { expr: "2⁵ = 32 → x = 5", why: "Multiplicando 2 cinco veces llegamos a 32." },
      ],
    },
    faded: {
      problem: "Resolver √(x + 5) = 4",
      given: "Elevamos ambos lados al cuadrado para quitar la raíz",
      blankPrompt: "¿Cuánto vale 4²?",
      blankAnswer: "16",
      finalPrompt: "Despejando x + 5 = 16, ¿cuánto vale x?",
      finalAnswer: "11",
    },
    generate(level = 1) {
      if (level === 1) {
        const pairs = [
          [2, 3, 8],
          [2, 4, 16],
          [2, 5, 32],
          [2, 6, 64],
          [3, 3, 27],
          [3, 4, 81],
          [5, 3, 125],
          [10, 3, 1000],
          [10, 4, 10000],
        ];
        const [b, exp, val] = pairs[randInt(0, pairs.length - 1)];
        return {
          topic: "logarithms",
          promptHtml: `<span class="math-expr">Evaluá log<sub>${b}</sub>(${val})</span>`,
          answer: String(exp),
          diagnose(v) {
            if (v === String(val / b)) return `Cuidado: el logaritmo no divide por ${b}, busca el exponente tal que ${b}^x = ${val}.`;
            return "";
          },
          explain: `${b}^${exp} = ${val} → log_${b}(${val}) = ${exp}.`,
        };
      }
      if (level === 2) {
        const e1 = randInt(1, 3);
        const e2 = randInt(2, 4);
        return {
          topic: "logarithms",
          promptHtml: `<span class="math-expr">Usando propiedades: log<sub>2</sub>(${2 ** e1}) + log<sub>2</sub>(${2 ** e2})</span>`,
          answer: String(e1 + e2),
          diagnose(v) {
            if (v === String(e1 * e2)) return "Sumar logaritmos suma los exponentes (no los multiplica).";
            return "";
          },
          explain: `log₂(${2 ** e1}) + log₂(${2 ** e2}) = ${e1} + ${e2} = ${e1 + e2}.`,
        };
      }
      const k = randInt(3, 8);
      const a = randInt(2, 12);
      const x = k * k - a;
      return {
        topic: "logarithms",
        promptHtml: `<span class="math-expr">Resolvé la ecuación radical: √(x + ${a}) = ${k}</span>`,
        answer: String(x),
        diagnose(v) {
          if (v === String(k - a)) return `Te olvidaste de elevar ${k} al cuadrado (${k * k}).`;
          return "";
        },
        explain: `x + ${a} = ${k}² = ${k * k} → x = ${k * k} − ${a} = ${x}.`,
      };
    },
  },
  trig_waves: {
    group: "Álgebra 2",
    name: "Ondas sinusoidales y composición",
    strategyHint: "En y = A·sen(Bx) + D, el máximo es D + |A| y el mínimo D − |A|; en f(g(x)) evaluá siempre de adentro hacia afuera.",
    worked: {
      problem: "Máximo y mínimo de h(t) = 1.5·sen(t) + 2.5",
      steps: [
        { expr: "Línea media D = 2.5, amplitud |A| = 1.5", why: "Identificamos el centro de oscilación y cuánto sube/baja." },
        { expr: "Máx = 4,  Mín = 1", why: "Sumamos y restamos la amplitud a la línea media." },
      ],
    },
    faded: {
      problem: "Calcular f(g(3)) con g(x) = 2x + 1 y f(x) = x²",
      given: "Evaluamos primero la función interna g(3) = 2(3) + 1",
      blankPrompt: "¿Cuánto vale g(3)?",
      blankAnswer: "7",
      finalPrompt: "Ahora aplicá f(7) = 7²:",
      finalAnswer: "49",
    },
    generate(level = 1) {
      if (level <= 2) {
        const amp = randInt(2, 9);
        const mid = randInt(3, 15);
        const askMax = level === 1;
        const ans = askMax ? mid + amp : mid - amp;
        return {
          topic: "trig_waves",
          promptHtml: `<span class="math-expr">Dada y = ${amp}·sen(2x) + ${mid}, ¿cuál es su valor ${askMax ? "MÁXIMO" : "MÍNIMO"}?</span>`,
          answer: String(ans),
          diagnose(val) {
            if (val === String(amp)) return `${amp} es la amplitud; sumala o restala a la línea media (${mid}).`;
            return "";
          },
          explain: `${askMax ? "Máximo = D + A" : "Mínimo = D − A"} = ${mid} ${askMax ? "+" : "−"} ${amp} = ${ans}.`,
        };
      }
      const x = randInt(1, 5);
      const m = randInt(2, 4);
      const b = randInt(1, 4);
      const gx = m * x + b;
      const ans = gx * gx;
      return {
        topic: "trig_waves",
        promptHtml: `<span class="math-expr">Con g(x) = ${m}x + ${b} y f(x) = x², calculá f(g(${x}))</span>`,
        answer: String(ans),
        diagnose(val) {
          if (val === String(m * x * x + b)) return "Hiciste g(f(x)) al revés: evaluá primero adentro g(" + x + ") = " + gx + ".";
          return "";
        },
        explain: `g(${x}) = ${m}(${x}) + ${b} = ${gx} → f(${gx}) = ${gx}² = ${ans}.`,
      };
    },
  },
  oblique_triangles: {
    group: "Trigonometría",
    name: "Ley de senos, Ley de cosenos y área",
    strategyHint: "Área = ½ab·sen(C); Ley de cosenos c² = a² + b² − 2ab·cos(C); Ley de senos a/sen(A) = b/sen(B).",
    worked: {
      problem: "Lados a = 5 y b = 8 con ángulo C = 60° (cos 60° = 0.5): hallar lado c",
      steps: [
        { expr: "c² = 5² + 8² − 2(5)(8)(0.5) = 25 + 64 − 40 = 49", why: "Aplicamos la Ley de cosenos en un caso LAL." },
        { expr: "c = √49 = 7", why: "Sacamos la raíz cuadrada para hallar el lado opuesto a 60°." },
      ],
    },
    faded: {
      problem: "Área de triángulo con lados 10 m y 12 m formando 30° (sen 30° = 0.5)",
      given: "Área = (1/2) · 10 · 12 · sen(30°)",
      blankPrompt: "¿Cuánto vale (1/2) · 10 · 12?",
      blankAnswer: "60",
      finalPrompt: "Multiplicando por sen(30°) = 0.5, ¿área final (m²)?",
      finalAnswer: "30",
    },
    generate(level = 1) {
      if (level === 1) {
        const a = randInt(2, 9) * 2;
        const b = randInt(2, 9) * 2;
        const ans = (a * b) / 4;
        return {
          topic: "oblique_triangles",
          promptHtml: `<span class="math-expr">Triángulo con lados ${a} m y ${b} m formando 30° (sen 30° = 0.5). ¿Área (m²)?</span>`,
          answer: String(ans),
          diagnose(val) {
            if (val === String((a * b) / 2)) return "Te faltó multiplicar por sen(30°) = 0.5.";
            return "";
          },
          explain: `Área = (1/2) × ${a} × ${b} × 0.5 = ${ans} m².`,
        };
      }
      if (level === 2) {
        const cases = [
          [3, 8, 60, "0.5", 7],
          [5, 8, 60, "0.5", 7],
          [7, 15, 60, "0.5", 13],
          [3, 5, 120, "−0.5", 7],
          [7, 8, 120, "−0.5", 13],
        ];
        const [a, b, ang, cosStr, c] = cases[randInt(0, cases.length - 1)];
        return {
          topic: "oblique_triangles",
          promptHtml: `<span class="math-expr">Ley de cosenos: a = ${a}, b = ${b}, C = ${ang}° (cos = ${cosStr}). ¿Lado c?</span>`,
          answer: String(c),
          diagnose(val) {
            if (val === String(c * c)) return `Te faltó sacar la raíz cuadrada de ${c * c}.`;
            return `Aplicá c² = ${a}² + ${b}² − 2(${a})(${b})(${cosStr}) y sacá raíz.`;
          },
          explain: `c² = ${a * a} + ${b * b} ${ang === 60 ? "−" : "+"} ${a * b} = ${c * c} → c = ${c}.`,
        };
      }
      const k = randInt(2, 6) * 5;
      const sinB = [0.6, 0.8][randInt(0, 1)];
      const b = Math.round((k / 0.5) * sinB);
      return {
        topic: "oblique_triangles",
        promptHtml: `<span class="math-expr">Ley de senos: a = ${k}, sen(A) = 0.5, sen(B) = ${sinB}. ¿Cuánto vale el lado b?</span>`,
        answer: String(b),
        diagnose() {
          return `Planteá b = (${k} / 0.5) × ${sinB} = ${k * 2} × ${sinB}.`;
        },
        explain: `a / sen(A) = ${k} / 0.5 = ${k * 2} → b = ${k * 2} × ${sinB} = ${b}.`,
      };
    },
  },
  trig_identities: {
    group: "Trigonometría",
    name: "Recíprocas, referencia e identidades",
    strategyHint: "Ángulo de referencia = distancia aguda al eje X; csc = 1/sen, sec = 1/cos, cot = 1/tan; sen(2θ) = 2·sen(θ)·cos(θ).",
    worked: {
      problem: "Ángulo de referencia de 225° y valor de sen(2θ) si sen θ = 0.6, cos θ = 0.8",
      steps: [
        { expr: "225° − 180° = 45°", why: "En el 3.er cuadrante medimos cuánto se pasa del eje horizontal (180°)." },
        { expr: "sen(2θ) = 2(0.6)(0.8) = 0.96", why: "Aplicamos la identidad del ángulo doble." },
      ],
    },
    faded: {
      problem: "Calcular cos(2θ) = cos²(θ) − sen²(θ) con sen(θ) = 0.6 y cos(θ) = 0.8",
      given: "cos²(θ) = 0.64 y sen²(θ) = 0.36",
      blankPrompt: "¿Cuánto vale 0.8²?",
      blankAnswer: "0.64",
      finalPrompt: "Resultado de cos(2θ) = 0.64 − 0.36:",
      finalAnswer: "0.28",
    },
    generate(level = 1) {
      if (level === 1) {
        const list = [
          [120, 60],
          [135, 45],
          [150, 30],
          [210, 30],
          [225, 45],
          [240, 60],
          [300, 60],
          [315, 45],
          [330, 30],
        ];
        const [ang, ref] = list[randInt(0, list.length - 1)];
        return {
          topic: "trig_identities",
          promptHtml: `<span class="math-expr">¿Cuál es el ángulo de referencia de ${ang}° (en °)?</span>`,
          answer: String(ref),
          diagnose() {
            return "Medí la distancia aguda contra el eje horizontal X (180° o 360°), nunca contra 90° o 270°.";
          },
          explain: `La distancia aguda de ${ang}° al eje X es ${ref}°.`,
        };
      }
      if (level === 2) {
        const items = [
          ["sen(θ) = 0.25", "csc(θ)", "4"],
          ["cos(θ) = 0.5", "sec(θ)", "2"],
          ["cos(θ) = 0.2", "sec(θ)", "5"],
          ["tan(θ) = 0.5", "cot(θ)", "2"],
          ["sen(θ) = 0.1", "csc(θ)", "10"],
        ];
        const [given, ask, ans] = items[randInt(0, items.length - 1)];
        return {
          topic: "trig_identities",
          promptHtml: `<span class="math-expr">Si ${given}, ¿cuánto vale ${ask}?</span>`,
          answer: ans,
          diagnose() {
            return `Calculá el recíproco (1 dividido el valor dado).`;
          },
          explain: `${ask} es el recíproco de ${given.split(" ")[0]} → ${ans}.`,
        };
      }
      const variants = [
        {
          html: "Si sen(θ) = 0.6 y cos(θ) = 0.8, calculá sen(2θ) = 2·sen(θ)·cos(θ)",
          ans: "0.96",
          exp: "2 × 0.6 × 0.8 = 0.96.",
        },
        {
          html: "Si sen(θ) = 0.6 y cos(θ) = 0.8, calculá cos(2θ) = cos²(θ) − sen²(θ)",
          ans: "0.28",
          exp: "0.64 − 0.36 = 0.28.",
        },
        {
          html: "En Q1, calculá cos(arcsen(0.6)) usando triángulo 3-4-5",
          ans: "0.8",
          exp: "Si Op = 3 y Hip = 5, Ady = 4 → cos = 4/5 = 0.8.",
        },
      ];
      const v = variants[randInt(0, variants.length - 1)];
      return {
        topic: "trig_identities",
        promptHtml: `<span class="math-expr">${v.html}</span>`,
        answer: v.ans,
        diagnose() {
          return "Revisá la fórmula: sen(2θ) = 2·sen·cos, cos(2θ) = cos² − sen².";
        },
        explain: v.exp,
      };
    },
  },
  vectors_matrices: {
    group: "Precálculo",
    name: "Vectores, producto punto y determinantes",
    strategyHint: "Producto punto: u_x·v_x + u_y·v_y (= 0 si son perpendiculares); determinante 2×2: ad − bc.",
    worked: {
      problem: "Determinante de A = [[4, 2], [1, 3]]",
      steps: [
        { expr: "Diagonal principal: 4 × 3 = 12", why: "Multiplicamos los elementos a y d." },
        { expr: "12 − (2 × 1) = 10", why: "Restamos el producto de la otra diagonal (b · c)." },
      ],
    },
    faded: {
      problem: "Producto punto de ⟨2, 5⟩ y ⟨3, −1⟩",
      given: "Multiplicamos por componentes: (2)(3) + (5)(−1)",
      blankPrompt: "¿Cuánto vale (5)(−1)?",
      blankAnswer: "-5",
      finalPrompt: "Suma final (6 + (−5)):",
      finalAnswer: "1",
    },
    generate(level = 1) {
      if (level === 1) {
        const ux = randInt(-5, 6);
        const uy = randInt(-5, 6);
        const vx = randInt(-5, 6);
        const vy = randInt(-5, 6);
        const ans = ux * vx + uy * vy;
        return {
          topic: "vectors_matrices",
          promptHtml: `<span class="math-expr">Producto punto: ⟨${ux}, ${uy}⟩ · ⟨${vx}, ${vy}⟩</span>`,
          answer: String(ans),
          diagnose() {
            return `Multiplicá (${ux})(${vx}) + (${uy})(${vy}) respetando signos.`;
          },
          explain: `(${ux})(${vx}) + (${uy})(${vy}) = ${ux * vx} + (${uy * vy}) = ${ans}.`,
        };
      }
      if (level === 2) {
        const a = randInt(-5, 7);
        const b = randInt(-5, 7);
        const c = randInt(-5, 7);
        const d = randInt(-5, 7);
        const det = a * d - b * c;
        return {
          topic: "vectors_matrices",
          promptHtml: `<span class="math-expr">Determinante de [[${a}, ${b}], [${c}, ${d}]] (ad − bc)</span>`,
          answer: String(det),
          diagnose(val) {
            if (val === String(a * d + b * c)) return "Cuidado: el determinante RESTA ad − bc, no suma.";
            if (val === String(b * c - a * d)) return "Restaste al revés: siempre es ad − bc.";
            return "";
          },
          explain: `det = (${a})(${d}) − (${b})(${c}) = ${a * d} − (${b * c}) = ${det}.`,
        };
      }
      const [a, b, c, d] = [randInt(1, 5), randInt(1, 4), randInt(1, 5), randInt(1, 4)];
      const ans = a * c + b * d;
      return {
        topic: "vectors_matrices",
        promptHtml: `<span class="math-expr">Entrada (1,1) del producto [[${a}, ${b}], [0, 1]] · [[${c}, 2], [${d}, 1]]</span>`,
        answer: String(ans),
        diagnose(val) {
          if (val === String(a * c)) return "Multiplicaste solo el primer par: hacé Fila 1 · Col 1 = a·c + b·d.";
          return "";
        },
        explain: `Fila 1 [${a}, ${b}] · Col 1 [${c}, ${d}] = ${a * c} + ${b * d} = ${ans}.`,
      };
    },
  },
  combinatorics_series: {
    group: "Precálculo",
    name: "Combinatoria (nPr, nCr) y series",
    strategyHint: "Orden importa → nPr; orden NO importa → nCr = nPr / r!; Gauss: n(1+n)/2; infinita (|r|<1): a₁ / (1 − r).",
    worked: {
      problem: "Suma infinita de 12 + 4 + 4/3 + ... (r = 1/3)",
      steps: [
        { expr: "1 − r = 1 − 1/3 = 2/3", why: "Como |r| = 1/3 < 1, la serie converge." },
        { expr: "S_∞ = 12 / (2/3) = 18", why: "Dividir por 2/3 equivale a multiplicar por 3/2." },
      ],
    },
    faded: {
      problem: "Elegir 2 personas de un grupo de 6 sin importar el orden (6C2)",
      given: "6P2 = 6 × 5 = 30 ordenamientos posibles",
      blankPrompt: "¿Por cuánto dividimos (2!) para eliminar repeticiones de orden?",
      blankAnswer: "2",
      finalPrompt: "Cantidad final de parejas (6C2):",
      finalAnswer: "15",
    },
    generate(level = 1) {
      if (level === 1) {
        const n = randInt(4, 8);
        const askComb = randInt(0, 1) === 1;
        const ans = askComb ? (n * (n - 1)) / 2 : n * (n - 1);
        return {
          topic: "combinatorics_series",
          promptHtml: askComb
            ? `<span class="math-expr">Combinaciones ${n}C2 (elegir 2 de ${n}, SIN orden)</span>`
            : `<span class="math-expr">Permutaciones ${n}P2 (1.° y 2.° puesto entre ${n}, CON orden)</span>`,
          answer: String(ans),
          diagnose(val) {
            if (askComb && val === String(n * (n - 1))) return "Como el orden NO importa, dividí por 2! = 2.";
            return "";
          },
          explain: askComb ? `${n}C2 = (${n} × ${n - 1}) / 2 = ${ans}.` : `${n}P2 = ${n} × ${n - 1} = ${ans}.`,
        };
      }
      if (level === 2) {
        const n = randInt(6, 20);
        const ans = (n * (n + 1)) / 2;
        return {
          topic: "combinatorics_series",
          promptHtml: `<span class="math-expr">Suma aritmética de Gauss: 1 + 2 + 3 + ... + ${n}</span>`,
          answer: String(ans),
          diagnose(val) {
            if (val === String(n * (n + 1))) return "Te faltó dividir por 2 en n(n + 1) / 2.";
            return "";
          },
          explain: `S = ${n} × (${n} + 1) / 2 = ${ans}.`,
        };
      }
      const cases = [
        [6, "0.5", 12],
        [10, "0.5", 20],
        [15, "0.5", 30],
        [9, "0.25", 12],
        [12, "0.25", 16],
        [8, "0.2", 10],
      ];
      const [a1, rStr, ans] = cases[randInt(0, cases.length - 1)];
      return {
        topic: "combinatorics_series",
        promptHtml: `<span class="math-expr">Serie geométrica infinita con a₁ = ${a1} y r = ${rStr}. ¿Suma S_∞?</span>`,
        answer: String(ans),
        diagnose() {
          return `Aplicá S_∞ = ${a1} / (1 − ${rStr}).`;
        },
        explain: `S_∞ = ${a1} / (1 − ${rStr}) = ${ans}.`,
      };
    },
  },
  limits_intro: {
    group: "Precálculo",
    name: "Límites algebraicos y forma 0/0",
    strategyHint: "Probá sustitución directa; si da 0/0, factorizá el numerador, cancelá (x − a) y volvé a sustituir.",
    worked: {
      problem: "lim(x → 4) (x² − 16) / (x − 4)",
      steps: [
        { expr: "(x − 4)(x + 4) / (x − 4) = x + 4", why: "Factorizamos la diferencia de cuadrados para cancelar el factor 0/0." },
        { expr: "4 + 4 = 8", why: "Evaluamos x + 4 en x = 4." },
      ],
    },
    faded: {
      problem: "lim(x → 2) (x² − 5x + 6) / (x − 2)",
      given: "Factorizamos arriba: (x − 2)(x − 3) / (x − 2)",
      blankPrompt: "¿Qué factor queda después de cancelar (x − 2)? (escribí el número que resta a x)",
      blankAnswer: "3",
      finalPrompt: "Evaluando x − 3 en x = 2, ¿cuánto da el límite?",
      finalAnswer: "-1",
    },
    generate(level = 1) {
      if (level === 1) {
        const c = randInt(-3, 5);
        const a = randInt(1, 3);
        const b = randInt(-4, 5);
        const ans = a * c * c + b;
        const bStr = b >= 0 ? `+ ${b}` : `− ${Math.abs(b)}`;
        return {
          topic: "limits_intro",
          promptHtml: `<span class="math-expr">lim(x → ${c}) de (${a}x² ${bStr})</span>`,
          answer: String(ans),
          diagnose() {
            return `Es un polinomio continuo: sustituí directo x = ${c}.`;
          },
          explain: `${a}·(${c})² ${bStr} = ${ans}.`,
        };
      }
      if (level === 2) {
        const a = randInt(2, 9);
        const ans = 2 * a;
        return {
          topic: "limits_intro",
          promptHtml: `<span class="math-expr">lim(x → ${a}) de (x² − ${a * a}) / (x − ${a})</span>`,
          answer: String(ans),
          diagnose(val) {
            if (val === "0") return "0/0 no significa límite 0: factorizá (x − " + a + ")(x + " + a + ") y cancelá.";
            return "";
          },
          explain: `Factorizando queda x + ${a} → ${a} + ${a} = ${ans}.`,
        };
      }
      const r1 = randInt(1, 5);
      const r2 = randInt(r1 + 1, 8);
      const ans = r1 - r2;
      return {
        topic: "limits_intro",
        promptHtml: `<span class="math-expr">lim(x → ${r1}) de (x² − ${r1 + r2}x + ${r1 * r2}) / (x − ${r1})</span>`,
        answer: String(ans),
        diagnose() {
          return `Factorizá el numerador como (x − ${r1})(x − ${r2}), cancelá (x − ${r1}) y evaluá en x = ${r1}.`;
        },
        explain: `Queda (x − ${r2}) evaluado en x = ${r1} → ${r1} − ${r2} = ${ans}.`,
      };
    },
  },
  derivatives: {
    group: "Cálculo 1",
    name: "Derivadas, cadena y puntos críticos",
    strategyHint: "Potencia: (xⁿ)' = n·xⁿ⁻¹; Cadena: [f(g(x))]' = f'(g(x))·g'(x); puntos críticos donde f'(x) = 0.",
    worked: {
      problem: "Pendiente f'(2) de f(x) = 4x³ − 5x + 7",
      steps: [
        { expr: "f'(x) = 12x² − 5", why: "Aplicamos regla de la potencia término a término (la constante 7 da 0)." },
        { expr: "f'(2) = 12(4) − 5 = 43", why: "Evaluamos la derivada en x = 2." },
      ],
    },
    faded: {
      problem: "Derivar f(x) = (2x + 1)³ en x = 1 (Regla de la cadena)",
      given: "Derivada afuera: 3(2x + 1)²; derivada adentro: 2",
      blankPrompt: "¿Cuánto vale 3(2·1 + 1)²?",
      blankAnswer: "27",
      finalPrompt: "Multiplicando por la derivada interna (× 2):",
      finalAnswer: "54",
    },
    generate(level = 1) {
      if (level === 1) {
        const a = randInt(1, 4);
        const b = randInt(-5, 6) || 2;
        const x = randInt(1, 4);
        const ans = 3 * a * x * x + b;
        const bStr = b > 0 ? `+ ${b}x` : `− ${Math.abs(b)}x`;
        return {
          topic: "derivatives",
          promptHtml: `<span class="math-expr">Dada f(x) = ${a}x³ ${bStr} + 5, calculá f'(${x})</span>`,
          answer: String(ans),
          diagnose() {
            return `Derivá primero: f'(x) = ${3 * a}x² ${b > 0 ? `+ ${b}` : `− ${Math.abs(b)}`}, luego evaluá en x = ${x}.`;
          },
          explain: `f'(x) = ${3 * a}x² + (${b}) → f'(${x}) = ${3 * a * x * x} + (${b}) = ${ans}.`,
        };
      }
      if (level === 2) {
        const m = randInt(2, 4);
        const b = randInt(1, 5);
        const x = randInt(1, 3);
        const inner = m * x + b;
        const ans = 2 * m * inner;
        return {
          topic: "derivatives",
          promptHtml: `<span class="math-expr">Cadena: dada f(x) = (${m}x + ${b})², calculá f'(${x})</span>`,
          answer: String(ans),
          diagnose(val) {
            if (val === String(2 * inner)) return `Te olvidaste de multiplicar por la derivada interna (× ${m})!`;
            return "";
          },
          explain: `f'(x) = 2(${m}x + ${b}) · ${m} → en x = ${x}: 2(${inner})(${m}) = ${ans}.`,
        };
      }
      const a = randInt(1, 4);
      const c = randInt(-5, 6) || 3;
      const b = -2 * a * c;
      const bStr = b > 0 ? `+ ${b}x` : `− ${Math.abs(b)}x`;
      return {
        topic: "derivatives",
        promptHtml: `<span class="math-expr">¿En qué x tiene punto crítico (f'(x) = 0) la función f(x) = ${a}x² ${bStr} + 9?</span>`,
        answer: String(c),
        diagnose(val) {
          if (val === String(-c)) return "Revisá el signo al despejar f'(x) = 0.";
          return "";
        },
        explain: `f'(x) = ${2 * a}x ${b > 0 ? `+ ${b}` : `− ${Math.abs(b)}`} = 0 → x = ${c}.`,
      };
    },
  },
  integrals: {
    group: "Cálculo 1",
    name: "Integrales definidas, promedios y volúmenes",
    strategyHint: "TFC: ∫_a^b f(x)dx = F(b) − F(a); antiderivada de k·xⁿ es k·xⁿ⁺¹/(n+1); valor promedio = integral ÷ (b − a).",
    worked: {
      problem: "Evaluar ∫(de 1 a 3) 3x² dx",
      steps: [
        { expr: "Antiderivada F(x) = x³", why: "Porque al derivar x³ recuperamos exactamente 3x²." },
        { expr: "F(3) − F(1) = 27 − 1 = 26", why: "Aplicamos el Teorema Fundamental del Cálculo." },
      ],
    },
    faded: {
      problem: "Valor promedio de f(x) = 3x² en el intervalo [0, 2]",
      given: "Primero integramos: ∫(de 0 a 2) 3x² dx = [x³] de 0 a 2",
      blankPrompt: "¿Cuánto vale la integral definida (2³ − 0³)?",
      blankAnswer: "8",
      finalPrompt: "Dividiendo por el ancho del intervalo (2 − 0 = 2):",
      finalAnswer: "4",
    },
    generate(level = 1) {
      if (level === 1) {
        const b = randInt(2, 5);
        const a = randInt(0, b - 1);
        const ans = b ** 3 - a ** 3;
        return {
          topic: "integrals",
          promptHtml: `<span class="math-expr">Evaluá ∫<sub>${a}</sub><sup>${b}</sup> 3x² dx</span>`,
          answer: String(ans),
          diagnose(val) {
            if (val === String(b ** 3)) return `Te faltó restar el límite inferior F(${a}) = ${a ** 3}.`;
            return "";
          },
          explain: `[x³] de ${a} a ${b} = ${b ** 3} − ${a ** 3} = ${ans}.`,
        };
      }
      if (level === 2) {
        const b = randInt(2, 6);
        const ans = b * b;
        return {
          topic: "integrals",
          promptHtml: `<span class="math-expr">Valor promedio de f(x) = 3x² en [0, ${b}] (integral ÷ ${b})</span>`,
          answer: String(ans),
          diagnose(val) {
            if (val === String(b ** 3)) return `Eso es la integral total; dividila por el ancho (${b}) para obtener el promedio.`;
            return "";
          },
          explain: `Integral = ${b}³ = ${b ** 3}; promedio = ${b ** 3} ÷ ${b} = ${ans}.`,
        };
      }
      const b = randInt(2, 6) * 2;
      const ans = (b * b) / 2;
      return {
        topic: "integrals",
        promptHtml: `<span class="math-expr">Volumen de revolución de y = √x en [0, ${b}]: V = k·π con k = ∫<sub>0</sub><sup>${b}</sup> x dx. ¿Valor de k?</span>`,
        answer: String(ans),
        diagnose(val) {
          if (val === String(b * b)) return "Te faltó dividir por 2 al antiderivar x → x²/2.";
          return "";
        },
        explain: `k = [x²/2] de 0 a ${b} = ${b * b} / 2 = ${ans} (V = ${ans}π).`,
      };
    },
  },
  integrals_adv: {
    group: "Cálculo 2",
    name: "Integrales impropias, Euler y logístico",
    strategyHint: "∫_1^∞ (c/x²)dx = c; Euler: y_nuevo = y + Δx·pendiente; en logístico dP/dt = kP(1 − P/K), el máximo crecimiento está en K/2.",
    worked: {
      problem: "Evaluar ∫(de 1 a ∞) 6 / x² dx",
      steps: [
        { expr: "Antiderivada de 6x⁻² es −6 / x", why: "Regla de la potencia con n = −2: n + 1 = −1." },
        { expr: "lim(b→∞) (−6/b − (−6/1)) = 0 + 6 = 6", why: "Cuando b → ∞, −6/b desaparece hacia 0." },
      ],
    },
    faded: {
      problem: "Un paso de Euler para dy/dx = x + y desde (1, 3) con Δx = 0.5",
      given: "Calculamos primero la pendiente inicial en (1, 3): 1 + 3",
      blankPrompt: "¿Cuánto vale la pendiente inicial?",
      blankAnswer: "4",
      finalPrompt: "Nuevo valor y₁ = 3 + 0.5 × 4:",
      finalAnswer: "5",
    },
    generate(level = 1) {
      if (level === 1) {
        const c = randInt(2, 12);
        return {
          topic: "integrals_adv",
          promptHtml: `<span class="math-expr">Integral impropia: ∫<sub>1</sub><sup>∞</sup> (${c} / x²) dx</span>`,
          answer: String(c),
          diagnose() {
            return `Antiderivada: −${c}/x. Evaluá lim(b→∞) [−${c}/b − (−${c}/1)] = ${c}.`;
          },
          explain: `[−${c}/x] de 1 a ∞ = 0 − (−${c}) = ${c}.`,
        };
      }
      if (level === 2) {
        const x0 = randInt(0, 3);
        const y0 = randInt(1, 5);
        const slope = x0 + y0;
        const y1 = y0 + 0.5 * slope;
        return {
          topic: "integrals_adv",
          promptHtml: `<span class="math-expr">Euler (Δx = 0.5): dy/dx = x + y desde (${x0}, ${y0}). ¿Valor y₁ en x = ${(x0 + 0.5).toFixed(1)}?</span>`,
          answer: String(y1),
          diagnose(val) {
            if (val === String(y0 + slope)) return "Te faltó multiplicar la pendiente por el paso Δx = 0.5.";
            return "";
          },
          explain: `Pendiente = ${x0} + ${y0} = ${slope} → y₁ = ${y0} + 0.5(${slope}) = ${y1}.`,
        };
      }
      const kHalf = randInt(2, 12) * 50;
      const K = kHalf * 2;
      return {
        topic: "integrals_adv",
        promptHtml: `<span class="math-expr">Logístico dP/dt = 0.3P(1 − P / ${K}). ¿En qué población P crece MÁS RÁPIDO?</span>`,
        answer: String(kHalf),
        diagnose(val) {
          if (val === String(K)) return `${K} es la capacidad de carga donde deja de crecer; el máximo crecimiento está en K/2.`;
          return "";
        },
        explain: `El crecimiento máximo siempre ocurre en K / 2 = ${K} / 2 = ${kHalf}.`,
      };
    },
  },
  parametric_series: {
    group: "Cálculo 2",
    name: "Paramétricas, polares y Taylor",
    strategyHint: "Rapidez 2D = √(x'² + y'²); pendiente dy/dx = y'/x'; coeficiente de Taylor c_n = f^(n)(a) / n!.",
    worked: {
      problem: "Coeficiente de x³ en Maclaurin si f'''(0) = 12",
      steps: [
        { expr: "3! = 3 × 2 × 1 = 6", why: "Cada término de Taylor divide la n-ésima derivada por n!." },
        { expr: "c₃ = 12 / 6 = 2", why: "El término es 2x³." },
      ],
    },
    faded: {
      problem: "Rapidez en t = 1 de r(t) = ⟨3t², 4t²⟩",
      given: "Derivamos cada componente: v(t) = ⟨6t, 8t⟩ → v(1) = ⟨6, 8⟩",
      blankPrompt: "¿Cuánto vale 6² + 8²?",
      blankAnswer: "100",
      finalPrompt: "Rapidez instantánea |v(1)| = √100:",
      finalAnswer: "10",
    },
    generate(level = 1) {
      if (level === 1) {
        const triples = [
          [3, 4, 5],
          [6, 8, 10],
          [5, 12, 13],
          [8, 15, 17],
        ];
        const [vx, vy, spd] = triples[randInt(0, triples.length - 1)];
        return {
          topic: "parametric_series",
          promptHtml: `<span class="math-expr">Curva paramétrica con velocidad v(2) = ⟨${vx}, ${vy}⟩. ¿Rapidez instantánea |v(2)|?</span>`,
          answer: String(spd),
          diagnose(val) {
            if (val === String(spd * spd)) return `Te faltó sacar la raíz cuadrada de ${spd * spd}.`;
            return "";
          },
          explain: `|v| = √(${vx}² + ${vy}²) = √${spd * spd} = ${spd}.`,
        };
      }
      if (level === 2) {
        const dx = randInt(2, 6);
        const m = randInt(-4, 5) || 3;
        const dy = dx * m;
        return {
          topic: "parametric_series",
          promptHtml: `<span class="math-expr">Paramétrica: en t = 1 vale dx/dt = ${dx} y dy/dt = ${dy}. ¿Pendiente dy/dx?</span>`,
          answer: String(m),
          diagnose() {
            return `Dividí dy/dt (${dy}) por dx/dt (${dx}).`;
          },
          explain: `dy/dx = (dy/dt) / (dx/dt) = ${dy} / ${dx} = ${m}.`,
        };
      }
      const c = randInt(2, 8);
      const n = randInt(2, 3);
      const fact = n === 2 ? 2 : 6;
      const deriv = c * fact;
      return {
        topic: "parametric_series",
        promptHtml: `<span class="math-expr">Maclaurin: si f<sup>(${n})</sup>(0) = ${deriv}, ¿cuál es el coeficiente de x<sup>${n}</sup> (f<sup>(${n})</sup>(0) / ${n}!)?</span>`,
        answer: String(c),
        diagnose(val) {
          if (val === String(deriv)) return `Te faltó dividir por ${n}! = ${fact}.`;
          return "";
        },
        explain: `c_${n} = ${deriv} / ${n}! = ${deriv} / ${fact} = ${c}.`,
      };
    },
  },
  multivar_diff: {
    group: "Cálculo multivariable",
    name: "Parciales, gradiente, divergencia y rotacional",
    strategyHint: "∂f/∂x congela y; D_u f = ∇f · u; div(F) = ∂P/∂x + ∂Q/∂y; rot₂D(F) = ∂Q/∂x − ∂P/∂y.",
    worked: {
      problem: "Derivada parcial ∂f/∂x de f(x, y) = x³y² + 5y en (2, 1)",
      steps: [
        { expr: "∂f/∂x = 3x²y² + 0", why: "Tratamos y como constante (así 5y tiene derivada 0 respecto de x)." },
        { expr: "3(2²)(1²) = 12", why: "Evaluamos en el punto (2, 1)." },
      ],
    },
    faded: {
      problem: "Rotacional 2D de F(x, y) = ⟨2y, 5x⟩",
      given: "Fórmula: rot(F) = ∂Q/∂x − ∂P/∂y con P = 2y y Q = 5x",
      blankPrompt: "¿Cuánto vale ∂Q/∂x = ∂(5x)/∂x?",
      blankAnswer: "5",
      finalPrompt: "Restando ∂P/∂y = 2, ¿rotacional final (5 − 2)?",
      finalAnswer: "3",
    },
    generate(level = 1) {
      if (level === 1) {
        const a = randInt(1, 4);
        const b = randInt(2, 6);
        const x = randInt(1, 4);
        const y = randInt(1, 3);
        const ans = 2 * a * x * y;
        return {
          topic: "multivar_diff",
          promptHtml: `<span class="math-expr">Dada f(x, y) = ${a}x²y + ${b}y², calculá ∂f/∂x en (${x}, ${y})</span>`,
          answer: String(ans),
          diagnose() {
            return `Congelá y como constante: ∂f/∂x = ${2 * a}xy (el término ${b}y² da 0 respecto de x).`;
          },
          explain: `∂f/∂x = ${2 * a}xy → en (${x}, ${y}): ${2 * a}(${x})(${y}) = ${ans}.`,
        };
      }
      if (level === 2) {
        const gx = randInt(1, 6) * 5;
        const gy = randInt(1, 6) * 5;
        const ans = Math.round(gx * 0.6 + gy * 0.8);
        return {
          topic: "multivar_diff",
          promptHtml: `<span class="math-expr">Con ∇f = ⟨${gx}, ${gy}⟩ y dirección unitaria u = ⟨0.6, 0.8⟩, calculá D<sub>u</sub>f = ∇f · u</span>`,
          answer: String(ans),
          diagnose() {
            return `Hacé el producto punto: ${gx}(0.6) + ${gy}(0.8).`;
          },
          explain: `D_u f = ${gx}(0.6) + ${gy}(0.8) = ${Math.round(gx * 0.6)} + ${Math.round(gy * 0.8)} = ${ans}.`,
        };
      }
      const p = randInt(-4, 6) || 2;
      const q = randInt(-4, 6) || 5;
      const askDiv = randInt(0, 1) === 1;
      const ans = askDiv ? p + q : q - p;
      return {
        topic: "multivar_diff",
        promptHtml: askDiv
          ? `<span class="math-expr">Calculá la divergencia div(F) de F(x, y) = ⟨${p}x, ${q}y⟩</span>`
          : `<span class="math-expr">Calculá el rotacional 2D (∂Q/∂x − ∂P/∂y) de F(x, y) = ⟨${p}y, ${q}x⟩</span>`,
        answer: String(ans),
        diagnose() {
          return askDiv ? `div(F) = ∂P/∂x + ∂Q/∂y = ${p} + (${q}).` : `rot(F) = ∂Q/∂x − ∂P/∂y = ${q} − (${p}).`;
        },
        explain: askDiv ? `div(F) = ${p} + (${q}) = ${ans}.` : `rot(F) = ${q} − (${p}) = ${ans}.`,
      };
    },
  },
  multivar_int: {
    group: "Cálculo multivariable",
    name: "Integrales dobles, trabajo conservativo y Green/Gauss",
    strategyHint: "Conservativo: ∫ ∇f·dr = f(B) − f(A); Green: ∮ F·dr = ∬ rot dA; Gauss: ∬ F·dS = ∭ div dV.",
    worked: {
      problem: "Flujo de F = ⟨2x, 3y, 4z⟩ saliendo de un cubo de lado 2 (Gauss)",
      steps: [
        { expr: "div(F) = 2 + 3 + 4 = 9", why: "Sumamos las tres derivadas parciales ∂P/∂x + ∂Q/∂y + ∂R/∂z." },
        { expr: "9 × 2³ = 9 × 8 = 72", why: "Multiplicamos la divergencia constante por el volumen del cubo." },
      ],
    },
    faded: {
      problem: "Trabajo de F = ∇(x² + y²) desde (1, 2) hasta (3, 4)",
      given: "Por el TFC de líneas, basta evaluar f(3, 4) − f(1, 2)",
      blankPrompt: "¿Cuánto vale f(3, 4) = 3² + 4²?",
      blankAnswer: "25",
      finalPrompt: "Restando f(1, 2) = 5, ¿trabajo total?",
      finalAnswer: "20",
    },
    generate(level = 1) {
      if (level === 1) {
        const a = randInt(2, 5);
        const b = randInt(2, 5);
        const ans = a * a * b;
        return {
          topic: "multivar_int",
          promptHtml: `<span class="math-expr">Integral doble: ∫<sub>0</sub><sup>${a}</sup> ∫<sub>0</sub><sup>${b}</sup> 2x dy dx</span>`,
          answer: String(ans),
          diagnose() {
            return `Adentro da ${2 * b}x; afuera ∫_0^${a} ${2 * b}x dx = ${b}·${a}².`;
          },
          explain: `Adentro: [2xy]_0^${b} = ${2 * b}x → afuera: [${b}x²]_0^${a} = ${ans}.`,
        };
      }
      if (level === 2) {
        const x1 = randInt(1, 3);
        const y1 = randInt(1, 3);
        const x2 = randInt(x1 + 1, 6);
        const y2 = randInt(y1 + 1, 6);
        const ans = x2 * x2 + y2 * y2 - (x1 * x1 + y1 * y1);
        return {
          topic: "multivar_int",
          promptHtml: `<span class="math-expr">Campo conservativo F = ∇(x² + y²). Trabajo ∫ F·dr de (${x1}, ${y1}) a (${x2}, ${y2}):</span>`,
          answer: String(ans),
          diagnose() {
            return `Evaluá f(${x2}, ${y2}) − f(${x1}, ${y1}) = (${x2 * x2 + y2 * y2}) − (${x1 * x1 + y1 * y1}).`;
          },
          explain: `(${x2}² + ${y2}²) − (${x1}² + ${y1}²) = ${x2 * x2 + y2 * y2} − ${x1 * x1 + y1 * y1} = ${ans}.`,
        };
      }
      const a = randInt(1, 4);
      const b = randInt(1, 4);
      const c = randInt(1, 4);
      const vol = randInt(3, 10);
      const div = a + b + c;
      const ans = div * vol;
      return {
        topic: "multivar_int",
        promptHtml: `<span class="math-expr">Gauss: F = ⟨${a}x, ${b}y, ${c}z⟩ saliendo de una región cerrada de volumen ${vol}. ¿Flujo neto?</span>`,
        answer: String(ans),
        diagnose() {
          return `Calculá div(F) = ${a} + ${b} + ${c} = ${div} y multiplicá por el volumen (${vol}).`;
        },
        explain: `div(F) = ${div} → Flujo = ${div} × ${vol} = ${ans}.`,
      };
    },
  },
  diff_eqs: {
    group: "Ecuaciones diferenciales",
    name: "EDOs de 1.er y 2.° orden (exactas y características)",
    strategyHint: "Exacta: ∂M/∂y = ∂N/∂x; 2.° orden homogénea: ar² + br + c = 0; particular constante: c·A = rhs.",
    worked: {
      problem: "Raíces características de y'' − 5y' + 6y = 0",
      steps: [
        { expr: "r² − 5r + 6 = 0 → (r − 2)(r − 3) = 0", why: "Reemplazamos y'' por r², y' por r e y por 1." },
        { expr: "r = 2, r = 3 → y = c₁e^(2t) + c₂e^(3t)", why: "Dos raíces reales distintas generan dos exponenciales." },
      ],
    },
    faded: {
      problem: "Hallar k para que (k·x·y + 1) dx + (2x² + 3y) dy = 0 sea exacta",
      given: "Test de exactitud: ∂M/∂y = ∂N/∂x → kx = ∂(2x² + 3y)/∂x",
      blankPrompt: "¿Cuánto vale el coeficiente de x en ∂(2x² + 3y)/∂x?",
      blankAnswer: "4",
      finalPrompt: "Igualando kx = 4x, ¿cuánto vale k?",
      finalAnswer: "4",
    },
    generate(level = 1) {
      if (level === 1) {
        const r1 = randInt(1, 4);
        const r2 = randInt(r1 + 1, 7);
        const b = r1 + r2;
        const c = r1 * r2;
        return {
          topic: "diff_eqs",
          promptHtml: `<span class="math-expr">EDO y'' − ${b}y' + ${c}y = 0. ¿Cuál es la MAYOR raíz característica r?</span>`,
          answer: String(r2),
          diagnose(val) {
            if (val === String(r1)) return `Bien factorizado (${r1} y ${r2}), pero la consigna pedía la MAYOR raíz (${r2}).`;
            return `Factorizá r² − ${b}r + ${c} = 0.`;
          },
          explain: `(r − ${r1})(r − ${r2}) = 0 → raíces ${r1} y ${r2} (mayor = ${r2}).`,
        };
      }
      if (level === 2) {
        const a = randInt(2, 6);
        const k = 2 * a;
        return {
          topic: "diff_eqs",
          promptHtml: `<span class="math-expr">¿Qué valor de k hace EXACTA a (k·x·y) dx + (${a}x² + 5y) dy = 0?</span>`,
          answer: String(k),
          diagnose() {
            return `Igualá ∂M/∂y = kx con ∂N/∂x = ${2 * a}x.`;
          },
          explain: `∂M/∂y = kx y ∂N/∂x = ${2 * a}x → k = ${k}.`,
        };
      }
      const c = randInt(2, 7);
      const A = randInt(2, 9);
      const rhs = c * A;
      return {
        topic: "diff_eqs",
        promptHtml: `<span class="math-expr">Solución particular constante y<sub>p</sub> = A para y'' + 4y' + ${c}y = ${rhs}. ¿Valor de A?</span>`,
        answer: String(A),
        diagnose() {
          return `Como A es constante, y'_p = y''_p = 0 → queda ${c}A = ${rhs}.`;
        },
        explain: `0 + 0 + ${c}A = ${rhs} → A = ${rhs} / ${c} = ${A}.`,
      };
    },
  },
  laplace_lab: {
    group: "Ecuaciones diferenciales",
    name: "Transformada de Laplace, traslaciones e impulso",
    strategyHint: "L{tⁿ} = n!/s^(n+1); L{sen(ωt)} = ω/(s² + ω²); L{e^(at)f(t)} = F(s − a); ∫ f(t)δ(t − c)dt = f(c).",
    worked: {
      problem: "Calcular ∫(de 0 a ∞) (t² + 3)·δ(t − 4) dt",
      steps: [
        { expr: "La delta δ(t − 4) evalúa f(t) en t = 4", why: "Por propiedad de muestreo, solo importa el punto t = 4." },
        { expr: "f(4) = 4² + 3 = 19", why: "Sustituimos directamente sin integrar." },
      ],
    },
    faded: {
      problem: "Evaluar el denominador (s − 3)² + 16 de L{e^(3t)·sen(4t)} en s = 6",
      given: "Por 1.er teorema de traslación, sustituimos s → (s − 3) en s² + 4²",
      blankPrompt: "¿Cuánto vale (6 − 3)²?",
      blankAnswer: "9",
      finalPrompt: "Suma final (9 + 16):",
      finalAnswer: "25",
    },
    generate(level = 1) {
      if (level === 1) {
        const w = randInt(2, 9);
        return {
          topic: "laplace_lab",
          promptHtml: `<span class="math-expr">En L{sen(${w}t)} = ${w} / (s² + k), ¿cuánto vale k (ω²)?</span>`,
          answer: String(w * w),
          diagnose(val) {
            if (val === String(w)) return `En el denominador va ω² = ${w}², no ω.`;
            return "";
          },
          explain: `L{sen(${w}t)} = ${w} / (s² + ${w}²) = ${w} / (s² + ${w * w}).`,
        };
      }
      if (level === 2) {
        const c = randInt(2, 6);
        const k = randInt(1, 8);
        const ans = c * c + k;
        return {
          topic: "laplace_lab",
          promptHtml: `<span class="math-expr">Muestreo de Dirac: ∫<sub>0</sub><sup>∞</sup> (t² + ${k}) · δ(t − ${c}) dt</span>`,
          answer: String(ans),
          diagnose() {
            return `La delta en t = ${c} evalúa directamente t² + ${k} en t = ${c}.`;
          },
          explain: `f(${c}) = ${c}² + ${k} = ${c * c} + ${k} = ${ans}.`,
        };
      }
      const a = randInt(1, 4);
      const w = randInt(2, 5);
      const s = a + randInt(2, 5);
      const denom = (s - a) ** 2 + w * w;
      return {
        topic: "laplace_lab",
        promptHtml: `<span class="math-expr">Traslación L{e<sup>${a}t</sup>·sen(${w}t)} = ${w} / ((s − ${a})² + ${w * w}). ¿Denominador en s = ${s}?</span>`,
        answer: String(denom),
        diagnose() {
          return `Evaluá (${s} − ${a})² + ${w * w}.`;
        },
        explain: `(${s} − ${a})² + ${w * w} = ${(s - a) ** 2} + ${w * w} = ${denom}.`,
      };
    },
  },
  linear_algebra: {
    group: "Álgebra lineal",
    name: "Rango-Nulidad, proyecciones y Gram-Schmidt",
    strategyHint: "rango + nulidad = columnas; proj_u(v) = ((v·u)/(u·u))·u; mínimos cuadrados: AᵀA x̂ = Aᵀb.",
    worked: {
      problem: "Proyección ortogonal de v = ⟨4, 6⟩ sobre u = ⟨1, 1⟩",
      steps: [
        { expr: "v · u = 10,  u · u = 2", why: "Calculamos los dos productos punto necesarios." },
        { expr: "(10 / 2) · ⟨1, 1⟩ = ⟨5, 5⟩", why: "Multiplicamos el escalar 5 por el vector dirección u." },
      ],
    },
    faded: {
      problem: "Matriz de 4 × 7 con rango = 3: hallar nulidad (dim Nul(A))",
      given: "Teorema del Rango-Nulidad: rango + nulidad = número de columnas",
      blankPrompt: "¿Cuántas columnas tiene una matriz de 4 × 7?",
      blankAnswer: "7",
      finalPrompt: "Nulidad = 7 − 3:",
      finalAnswer: "4",
    },
    generate(level = 1) {
      if (level === 1) {
        const cols = randInt(5, 10);
        const rows = randInt(3, 6);
        const rank = randInt(2, Math.min(rows, cols - 1));
        const nullity = cols - rank;
        return {
          topic: "linear_algebra",
          promptHtml: `<span class="math-expr">Una matriz de ${rows} × ${cols} tiene rango = ${rank}. ¿Cuál es su nulidad (dim Nul)?</span>`,
          answer: String(nullity),
          diagnose(val) {
            if (val === String(rows - rank)) return `Cuidado: rango + nulidad iguala al número de COLUMNAS (${cols}), no de filas (${rows}).`;
            return "";
          },
          explain: `rango + nulidad = columnas → ${rank} + nulidad = ${cols} → nulidad = ${nullity}.`,
        };
      }
      if (level === 2) {
        const k = randInt(2, 7);
        const diff = randInt(1, 3);
        const vx = k - diff;
        const vy = k + diff;
        return {
          topic: "linear_algebra",
          promptHtml: `<span class="math-expr">Proyección de v = ⟨${vx}, ${vy}⟩ sobre u = ⟨1, 1⟩. ¿Primera coordenada x de proj<sub>u</sub>(v)?</span>`,
          answer: String(k),
          diagnose(val) {
            if (val === String(vx + vy)) return "Te faltó dividir por u · u = 1² + 1² = 2.";
            return "";
          },
          explain: `((v·u)/(u·u)) = (${vx} + ${vy}) / 2 = ${k} → proj = ⟨${k}, ${k}⟩.`,
        };
      }
      const x1 = randInt(2, 5);
      const scale = randInt(2, 5);
      const y1 = randInt(2, 6);
      const k = scale * y1;
      return {
        topic: "linear_algebra",
        promptHtml: `<span class="math-expr">¿Qué valor de k hace linealmente DEPENDIENTES a ⟨${x1}, ${y1}⟩ y ⟨${x1 * scale}, k⟩?</span>`,
        answer: String(k),
        diagnose() {
          return `Buscá el múltiplo: la primera componente se multiplicó por ${scale}, así que k = ${y1} × ${scale}.`;
        },
        explain: `⟨${x1 * scale}, ${k}⟩ = ${scale} · ⟨${x1}, ${y1}⟩ → det = 0 con k = ${k}.`,
      };
    },
  },
  eigen_lab: {
    group: "Álgebra lineal",
    name: "Valores propios (λ), traza y diagonalización",
    strategyHint: "Av = λv; en 2×2: λ₁ + λ₂ = traza y λ₁·λ₂ = det; en diagonales/triangulares los λ están en la diagonal.",
    worked: {
      problem: "Segundo eigenvalor de A = [[4, 1], [2, 3]] sabiendo que λ₁ = 5",
      steps: [
        { expr: "traza(A) = 4 + 3 = 7", why: "La suma de todos los eigenvalores siempre iguala a la traza." },
        { expr: "λ₂ = 7 − 5 = 2", why: "Verificación con det(A) = 12 − 2 = 10 = 5 × 2." },
      ],
    },
    faded: {
      problem: "Hallar el eigenvalor λ de A = [[4, 1], [2, 3]] para el eigenvector v = ⟨1, 1⟩",
      given: "Calculamos Av = ⟨4(1) + 1(1), 2(1) + 3(1)⟩",
      blankPrompt: "¿Cuánto vale la primera componente de Av?",
      blankAnswer: "5",
      finalPrompt: "Como Av = 5 · ⟨1, 1⟩, ¿cuánto vale λ?",
      finalAnswer: "5",
    },
    generate(level = 1) {
      if (level === 1) {
        const l1 = randInt(-3, 7);
        const l2 = randInt(l1 + 1, 10);
        const off = randInt(-5, 8) || 3;
        return {
          topic: "eigen_lab",
          promptHtml: `<span class="math-expr">Matriz triangular [[${l1}, ${off}], [0, ${l2}]]. ¿Cuál es su MAYOR eigenvalor λ?</span>`,
          answer: String(l2),
          diagnose() {
            return `En matrices triangulares los eigenvalores son directamente la diagonal: ${l1} y ${l2}.`;
          },
          explain: `Diagonal = {${l1}, ${l2}} → mayor eigenvalor = ${l2}.`,
        };
      }
      if (level === 2) {
        const l1 = randInt(1, 6);
        const l2 = randInt(1, 7);
        const tr = l1 + l2;
        return {
          topic: "eigen_lab",
          promptHtml: `<span class="math-expr">Una matriz 2×2 tiene traza = ${tr} y un eigenvalor λ₁ = ${l1}. ¿Cuánto vale λ₂?</span>`,
          answer: String(l2),
          diagnose() {
            return `Recordá: λ₁ + λ₂ = traza (${tr}).`;
          },
          explain: `λ₂ = traza − λ₁ = ${tr} − ${l1} = ${l2}.`,
        };
      }
      const d = randInt(2, 4);
      const p = randInt(3, 4);
      const ans = d ** p;
      return {
        topic: "eigen_lab",
        promptHtml: `<span class="math-expr">Si D = [[1, 0], [0, ${d}]], ¿cuánto vale la entrada inferior derecha de D<sup>${p}</sup>?</span>`,
        answer: String(ans),
        diagnose(val) {
          if (val === String(d * p)) return `Elevá ${d} a la potencia ${p} (${d}^${p}), no multipliques ${d} × ${p}.`;
          return "";
        },
        explain: `D^${p} = [[1^${p}, 0], [0, ${d}^${p}]] → ${d}^${p} = ${ans}.`,
      };
    },
  },
};

function renderTopicOptions(selectedKey) {
  const groups = { Aritmética: [], Preálgebra: [], "Álgebra 1": [], Geometría: [], "Álgebra 2": [], Trigonometría: [], Precálculo: [], "Cálculo 1": [], "Cálculo 2": [], "Cálculo multivariable": [], "Ecuaciones diferenciales": [], "Álgebra lineal": [] };
  for (const [k, v] of Object.entries(MATH_TOPICS)) {
    const g = v.group || "Aritmética";
    (groups[g] ||= []).push([k, v]);
  }
  return Object.entries(groups)
    .map(
      ([g, entries]) =>
        `<optgroup label="${esc(g)}">${entries
          .map(([k, v]) => `<option value="${k}" ${k === selectedKey ? "selected" : ""}>${esc(v.name)}</option>`)
          .join("")}</optgroup>`
    )
    .join("");
}

export async function renderMathLab(container, { topic = "place_value" } = {}) {
  let activeTab = "faded";
  let selectedTopic = MATH_TOPICS[topic] ? topic : "place_value";
  let interleaved = true;
  let difficulty = 1;
  let currentProblem = null;
  let showHint = false;
  let probFeedback = null;
  let stats = { ok: 0, total: 0, streak: 0 };
  const topicStats = {};

  let slopeM = 1.5;
  let interceptB = 1;
  let showSecondLine = true;
  let slopeM2 = -1.0;
  let interceptB2 = 3.5;

  const nextProblem = () => {
    probFeedback = null;
    showHint = false;
    const keys = Object.keys(MATH_TOPICS);
    const chosenKey = interleaved ? keys[randInt(0, keys.length - 1)] : selectedTopic;
    currentProblem = MATH_TOPICS[chosenKey].generate(difficulty);
  };
  nextProblem();

  const drawGraph = (canvas) => {
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const w = canvas.width;
    const h = canvas.height;
    const cx = w / 2;
    const cy = h / 2;
    const scale = 26;

    ctx.clearRect(0, 0, w, h);
    ctx.fillStyle = "#1e1e1c";
    ctx.fillRect(0, 0, w, h);

    ctx.strokeStyle = "rgba(247,245,239,0.09)";
    ctx.lineWidth = 1;
    for (let x = cx % scale; x < w; x += scale) {
      ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
    }
    for (let y = cy % scale; y < h; y += scale) {
      ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
    }

    ctx.strokeStyle = "rgba(247,245,239,0.45)";
    ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(0, cy); ctx.lineTo(w, cy); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(cx, 0); ctx.lineTo(cx, h); ctx.stroke();

    const toPx = (x, y) => [cx + x * scale, cy - y * scale];

    const [x1, y1] = toPx(-10, slopeM * -10 + interceptB);
    const [x2, y2] = toPx(10, slopeM * 10 + interceptB);
    ctx.strokeStyle = "#c7dfdb";
    ctx.lineWidth = 2.8;
    ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();

    const [p0x, p0y] = toPx(0, interceptB);
    const [p1x, p1y] = toPx(1, interceptB);
    const [p2x, p2y] = toPx(1, slopeM + interceptB);
    ctx.strokeStyle = "rgba(162,229,95,0.75)";
    ctx.setLineDash([4, 3]);
    ctx.lineWidth = 1.8;
    ctx.beginPath(); ctx.moveTo(p0x, p0y); ctx.lineTo(p1x, p1y); ctx.lineTo(p2x, p2y); ctx.stroke();
    ctx.setLineDash([]);

    ctx.fillStyle = "#f7f5ef";
    ctx.beginPath(); ctx.arc(p0x, p0y, 4.5, 0, Math.PI * 2); ctx.fill();

    if (showSecondLine) {
      const [bx1, by1] = toPx(-10, slopeM2 * -10 + interceptB2);
      const [bx2, by2] = toPx(10, slopeM2 * 10 + interceptB2);
      ctx.strokeStyle = "#c8bcae";
      ctx.lineWidth = 2.4;
      ctx.beginPath(); ctx.moveTo(bx1, by1); ctx.lineTo(bx2, by2); ctx.stroke();

      if (Math.abs(slopeM - slopeM2) > 0.001) {
        const ix = (interceptB2 - interceptB) / (slopeM - slopeM2);
        const iy = slopeM * ix + interceptB;
        const [ipx, ipy] = toPx(ix, iy);
        ctx.fillStyle = "#a2e55f";
        ctx.beginPath(); ctx.arc(ipx, ipy, 6, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = "#f7f5ef";
        ctx.font = "11px monospace";
        ctx.fillText(`(${ix.toFixed(1)}, ${iy.toFixed(1)})`, ipx + 9, ipy - 8);
      }
    }
  };

  const setupScratchpad = (canvas) => {
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "#1e1e1c";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    let drawing = false;
    let strokeColor = "#f7f5ef";

    const getPos = (e) => {
      const rect = canvas.getBoundingClientRect();
      const scaleX = canvas.width / rect.width;
      const scaleY = canvas.height / rect.height;
      return [(e.clientX - rect.left) * scaleX, (e.clientY - rect.top) * scaleY];
    };

    canvas.addEventListener("pointerdown", (e) => {
      drawing = true;
      canvas.setPointerCapture(e.pointerId);
      const [x, y] = getPos(e);
      ctx.beginPath();
      ctx.moveTo(x, y);
    });
    canvas.addEventListener("pointermove", (e) => {
      if (!drawing) return;
      const [x, y] = getPos(e);
      ctx.strokeStyle = strokeColor;
      ctx.lineWidth = 2.4;
      ctx.lineCap = "round";
      ctx.lineTo(x, y);
      ctx.stroke();
    });
    const end = () => { drawing = false; };
    canvas.addEventListener("pointerup", end);
    canvas.addEventListener("pointercancel", end);

    container.querySelector("#clear-pad")?.addEventListener("click", () => {
      ctx.fillStyle = "#1e1e1c";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
    });
    container.querySelectorAll(".pad-color").forEach((b) => {
      b.addEventListener("click", () => { strokeColor = b.dataset.c; });
    });
  };

  const paint = () => {
    const topicObj = MATH_TOPICS[selectedTopic];
    container.innerHTML = `
      <div class="page-header band dots" data-tone="math">
        <div>
          <div class="breadcrumb"><a href="#/labs">Laboratorios</a> <span>/</span> <span>Matemáticas</span></div>
          <h1>Matemáticas</h1>
          <p>Ejemplos resueltos paso a paso, práctica mezclada que detecta tus errores típicos, graficador y pizarra.</p>
        </div>
        <a href="#/roadmap/matematicas" class="btn btn-secondary btn-sm">${icon("map", 14)} Lecciones de matemáticas</a>
      </div>

      <div class="tabs">
        <button class="tab-btn ${activeTab === "faded" ? "active" : ""}" data-tab="faded" type="button">${icon("layers", 14)} Ejemplos guiados</button>
        <button class="tab-btn ${activeTab === "practice" ? "active" : ""}" data-tab="practice" type="button">${icon("shuffle", 14)} Práctica mezclada</button>
        <button class="tab-btn ${activeTab === "visual" ? "active" : ""}" data-tab="visual" type="button">${icon("activity", 14)} Graficador y pizarra</button>
      </div>

      <div id="math-tab-body"></div>
    `;

    container.querySelectorAll(".tab-btn").forEach((b) => {
      b.addEventListener("click", () => { activeTab = b.dataset.tab; paint(); });
    });

    const body = container.querySelector("#math-tab-body");

    if (activeTab === "faded") {
      body.innerHTML = `
        <div class="stack">
          <div class="row">
            <label class="field" style="max-width:380px;width:100%;">
              <span>Tema a estudiar por andamiaje progresivo</span>
              <select id="math-topic-sel">
                ${renderTopicOptions(selectedTopic)}
              </select>
            </label>
          </div>

          <div class="grid-2" style="align-items:start;">
            <div class="card stack">
              <span class="pill pill-accent" style="width:fit-content;">Paso 01 · Ejemplo Resuelto (Auto-explicación)</span>
              <h2 style="font-size:1.4rem;">${esc(topicObj.worked.problem)}</h2>
              ${topicObj.worked.visual ? `<div class="card-flat">${renderFractionVisualSVG()}</div>` : ""}
              <p class="xs muted">Antes de desplegar cada justificación, intentá verbalizar qué regla permite avanzar al paso siguiente.</p>
              <div class="stack" style="gap:10px;">
                ${topicObj.worked.steps
                  .map(
                    (st, i) => `
                  <div class="card-flat stack" style="gap:6px;">
                    <div class="math-expr"><strong>${i + 1}.</strong> ${esc(st.expr)}</div>
                    <details class="xs">
                      <summary style="cursor:pointer;color:var(--accent);font-weight:500;">¿Por qué este paso?</summary>
                      <p class="small secondary" style="margin:6px 0 0;">${esc(st.why)}</p>
                    </details>
                  </div>`
                  )
                  .join("")}
              </div>
            </div>

            <form id="faded-form" class="card stack">
              <span class="pill pill-amber" style="width:fit-content;">Paso 02 · Ejemplo Desvanecido</span>
              <h2 style="font-size:1.4rem;">${esc(topicObj.faded.problem)}</h2>
              <div class="callout small">${esc(topicObj.faded.given)}</div>
              <label class="field">
                <span>${esc(topicObj.faded.blankPrompt)}</span>
                <input type="text" name="step1" autocomplete="off" required />
              </label>
              <label class="field">
                <span>${esc(topicObj.faded.finalPrompt)}</span>
                <input type="text" name="step2" autocomplete="off" required />
              </label>
              <div class="row">
                <button class="btn btn-primary" type="submit">Verificar pasos</button>
                <button id="go-independent" class="btn btn-secondary btn-sm" type="button">Paso 03: Práctica independiente ${icon("arrowRight", 13)}</button>
              </div>
              <div id="faded-feedback"></div>
            </form>
          </div>
        </div>
      `;

      body.querySelector("#math-topic-sel").addEventListener("change", (e) => { selectedTopic = e.target.value; paint(); });
      body.querySelector("#go-independent").addEventListener("click", () => {
        interleaved = false;
        activeTab = "practice";
        nextProblem();
        paint();
      });
      body.querySelector("#faded-form").addEventListener("submit", (e) => {
        e.preventDefault();
        const fd = new FormData(e.target);
        const ok1 = gradeAnswer(fd.get("step1"), topicObj.faded.blankAnswer).ok;
        const ok2 = gradeAnswer(fd.get("step2"), topicObj.faded.finalAnswer).ok;
        const fb = body.querySelector("#faded-feedback");
        if (ok1 && ok2) {
          fb.innerHTML = `<div class="callout callout-ok small">${icon("check", 14)} Excelente. Ya podés pasar al Paso 03 (práctica sin andamiaje).</div>`;
          toast("Ejemplo desvanecido completado", "ok");
        } else {
          fb.innerHTML = `<div class="callout callout-warn small">Revisá tus pasos: ${ok1 ? "Paso 1 correcto" : "Paso 1 esperado: " + esc(topicObj.faded.blankAnswer)} · ${ok2 ? "Paso 2 correcto" : "Paso 2 esperado: " + esc(topicObj.faded.finalAnswer)}</div>`;
        }
      });
    } else if (activeTab === "practice") {
      const acc = stats.total ? Math.round((stats.ok / stats.total) * 100) : 0;
      const curTopicObj = MATH_TOPICS[currentProblem.topic];
      const practicedTopics = Object.entries(topicStats);
      const weakest = practicedTopics
        .map(([k, s]) => ({ k, pct: Math.round((s.ok / s.total) * 100), ...s }))
        .sort((a, b) => a.pct - b.pct)[0];

      body.innerHTML = `
        <div class="stack" style="max-width:820px;">
          <div class="card stack">
            <div class="row-between">
              <div class="row">
                <button id="toggle-interleave" class="btn btn-sm ${interleaved ? "btn-primary" : "btn-secondary"}" type="button">
                  ${icon("shuffle", 14)} Intercalado: ${interleaved ? "ON (tema oculto)" : "OFF"}
                </button>
                <div class="segmented" aria-label="Nivel de dificultad">
                  ${[
                    { lvl: 1, lbl: "Base" },
                    { lvl: 2, lbl: "Sólido" },
                    { lvl: 3, lbl: "Desafío" },
                  ]
                    .map(
                      (d) =>
                        `<button type="button" class="seg-btn ${difficulty === d.lvl ? "active" : ""} diff-btn" data-d="${d.lvl}">${d.lbl}</button>`
                    )
                    .join("")}
                </div>
                ${
                  !interleaved
                    ? `<select id="prac-topic-sel" style="width:auto;">
                        ${renderTopicOptions(selectedTopic)}
                       </select>`
                    : ""
                }
              </div>
              <div class="row">
                <span class="pill pill-green">Precisión: ${acc}% (${stats.ok}/${stats.total})</span>
                <span class="pill">Racha: ${stats.streak}</span>
              </div>
            </div>

            <div class="card-flat stack" style="padding:28px 22px;text-align:center;">
              <div class="xs mono muted">
                ${interleaved && !probFeedback ? "TEMA OCULTO — IDENTIFICÁ PRIMERO QUÉ ESTRATEGIA CORRESPONDE" : "TEMA: " + esc(curTopicObj.name).toUpperCase()}
              </div>
              <div style="margin:14px 0;">${currentProblem.promptHtml}</div>
              <form id="prac-form" class="row" style="justify-content:center;max-width:460px;margin:0 auto;width:100%;">
                <input id="prac-input" type="text" placeholder="Tu respuesta (ej. 12 o 5/6)" autocomplete="off" style="flex:1;" required />
                <button class="btn btn-primary" type="submit">Comprobar</button>
                ${!probFeedback ? `<button id="hint-btn" class="btn btn-ghost btn-sm" type="button">${icon("help", 14)} Pista</button>` : ""}
              </form>
              ${
                showHint && !probFeedback
                  ? `<div class="callout callout-info small" style="text-align:left;"><strong>Pista estratégica:</strong> ${esc(curTopicObj.strategyHint)}</div>`
                  : ""
              }
              ${
                probFeedback
                  ? `<div class="callout ${probFeedback.ok ? "callout-ok" : "callout-warn"} small" style="text-align:left;">
                      <div>${probFeedback.ok ? icon("check", 14) : icon("x", 14)} ${esc(probFeedback.text)}</div>
                      ${probFeedback.diag ? `<div style="margin-top:6px;"><strong>Diagnóstico de error:</strong> ${esc(probFeedback.diag)}</div>` : ""}
                     </div>
                     <button id="next-prob-btn" class="btn btn-secondary" type="button" style="width:fit-content;margin:0 auto;">Siguiente problema ${icon("arrowRight", 14)}</button>`
                  : ""
              }
            </div>
          </div>

          ${
            practicedTopics.length
              ? `<div class="card stack">
                  <div class="row-between">
                    <div>
                      <div class="eyebrow" style="margin-bottom:2px;">Mastery Learning en vivo</div>
                      <h3 style="margin:0;">Precisión por tema en esta sesión</h3>
                    </div>
                    ${
                      weakest && weakest.pct < 85
                        ? `<button id="drill-weakest" type="button" class="btn btn-secondary btn-sm" data-topic="${weakest.k}">Reforzar ${esc(MATH_TOPICS[weakest.k].name)} →</button>`
                        : ""
                    }
                  </div>
                  <div class="row" style="gap:8px;">
                    ${practicedTopics
                      .map(([k, s]) => {
                        const p = Math.round((s.ok / s.total) * 100);
                        return `<span class="pill ${p >= 80 ? "pill-green" : p >= 50 ? "pill-amber" : "pill-red"}">${esc(MATH_TOPICS[k].name)}: ${p}% (${s.ok}/${s.total})</span>`;
                      })
                      .join("")}
                  </div>
                </div>`
              : ""
          }
        </div>
      `;

      body.querySelector("#toggle-interleave").addEventListener("click", () => { interleaved = !interleaved; nextProblem(); paint(); });
      body.querySelectorAll(".diff-btn").forEach((b) => {
        b.addEventListener("click", () => { difficulty = Number(b.dataset.d); nextProblem(); paint(); });
      });
      body.querySelector("#prac-topic-sel")?.addEventListener("change", (e) => { selectedTopic = e.target.value; nextProblem(); paint(); });
      body.querySelector("#hint-btn")?.addEventListener("click", () => { showHint = true; paint(); });
      body.querySelector("#next-prob-btn")?.addEventListener("click", () => { nextProblem(); paint(); });
      body.querySelector("#drill-weakest")?.addEventListener("click", (e) => {
        selectedTopic = e.currentTarget.dataset.topic;
        interleaved = false;
        nextProblem();
        paint();
      });
      body.querySelector("#prac-form").addEventListener("submit", async (e) => {
        e.preventDefault();
        if (probFeedback) { nextProblem(); paint(); return; }
        const typed = body.querySelector("#prac-input").value;
        const val = typed.trim().replaceAll(" ", "").replace(",", ".");
        const grade = gradeAnswer(typed, currentProblem.answer);
        stats.total += 1;
        const ts = (topicStats[currentProblem.topic] ||= { ok: 0, total: 0 });
        ts.total += 1;
        if (grade.ok) {
          stats.ok += 1;
          stats.streak += 1;
          ts.ok += 1;
          probFeedback = { ok: true, text: `Correcto. ${currentProblem.explain}`, diag: "" };
          if (stats.total % 5 === 0) {
            await api.post("/api/metrics", {
              domain_slug: "matematicas",
              metric_type: "math_accuracy",
              label: interleaved ? `Intercalado (N${difficulty})` : MATH_TOPICS[selectedTopic].name,
              value: Math.round((stats.ok / stats.total) * 100),
              unit: "%",
            });
          }
        } else {
          stats.streak = 0;
          const diag =
            (typeof currentProblem.diagnose === "function" ? currentProblem.diagnose(val) : "") ||
            (grade.unsimplified ? "El valor es equivalente, pero faltó simplificar la fracción al máximo." : "");
          probFeedback = { ok: false, text: `Respuesta esperada: ${currentProblem.answer}. ${currentProblem.explain}`, diag };
        }
        paint();
      });
    } else if (activeTab === "visual") {
      const hasIntersection = showSecondLine && Math.abs(slopeM - slopeM2) > 0.001;
      const sameLine = !hasIntersection && Math.abs(interceptB - interceptB2) <= 0.001;
      const ix = hasIntersection ? (interceptB2 - interceptB) / (slopeM - slopeM2) : null;
      const iy = hasIntersection ? slopeM * ix + interceptB : null;

      body.innerHTML = `
        <div class="grid-2" style="align-items:start;">
          <div class="card stack">
            <div class="row-between">
              <div>
                <div class="eyebrow" style="margin-bottom:2px;">Funciones lineales & Sistemas 2×2</div>
                <h2 style="font-size:1.3rem;margin:0;">Graficador cartesiano dual</h2>
              </div>
              <button id="toggle-l2" type="button" class="btn btn-sm ${showSecondLine ? "btn-primary" : "btn-secondary"}">
                ${showSecondLine ? "2 rectas (Intersección)" : "Solo 1 recta"}
              </button>
            </div>
            <div class="row-between small mono">
              <span style="color:var(--accent);">L1: y = ${slopeM.toFixed(1)}x ${interceptB >= 0 ? "+ " + interceptB.toFixed(1) : "− " + Math.abs(interceptB).toFixed(1)}</span>
              ${
                showSecondLine
                  ? `<span class="muted">L2: y = ${slopeM2.toFixed(1)}x ${interceptB2 >= 0 ? "+ " + interceptB2.toFixed(1) : "− " + Math.abs(interceptB2).toFixed(1)}</span>`
                  : ""
              }
            </div>
            <canvas id="graph-canvas" class="lab-canvas" width="440" height="300"></canvas>
            ${
              showSecondLine
                ? `<div class="card-flat xs mono">
                    ${hasIntersection ? `Punto de intersección (solución 2×2): <strong>(${ix.toFixed(2)}, ${iy.toFixed(2)})</strong>` : sameLine ? "Rectas coincidentes: el sistema 2×2 tiene infinitas soluciones." : "Rectas paralelas: el sistema 2×2 no tiene punto de cruce."}
                   </div>`
                : ""
            }
            <div class="grid-2" style="gap:10px;">
              <label class="field">
                <span class="row-between"><span>L1 Pendiente (m₁)</span><strong class="mono">${slopeM.toFixed(1)}</strong></span>
                <input id="m-slider" type="range" min="-4" max="4" step="0.5" value="${slopeM}" />
              </label>
              <label class="field">
                <span class="row-between"><span>L1 Ordenada (b₁)</span><strong class="mono">${interceptB.toFixed(1)}</strong></span>
                <input id="b-slider" type="range" min="-5" max="5" step="0.5" value="${interceptB}" />
              </label>
              ${
                showSecondLine
                  ? `<label class="field">
                      <span class="row-between"><span>L2 Pendiente (m₂)</span><strong class="mono">${slopeM2.toFixed(1)}</strong></span>
                      <input id="m2-slider" type="range" min="-4" max="4" step="0.5" value="${slopeM2}" />
                    </label>
                    <label class="field">
                      <span class="row-between"><span>L2 Ordenada (b₂)</span><strong class="mono">${interceptB2.toFixed(1)}</strong></span>
                      <input id="b2-slider" type="range" min="-5" max="5" step="0.5" value="${interceptB2}" />
                    </label>`
                  : ""
              }
            </div>
          </div>

          <div class="card stack">
            <div class="row-between">
              <div>
                <div class="eyebrow" style="margin-bottom:2px;">Hoja en blanco</div>
                <h2 style="font-size:1.3rem;margin:0;">Pizarra de borrador</h2>
              </div>
              <div class="row">
                <button type="button" class="btn btn-ghost btn-sm pad-color" data-c="#f7f5ef" title="Tiza blanca"><span style="width:10px;height:10px;border-radius:50%;background:#f7f5ef;border:1px solid #999;display:inline-block;"></span></button>
                <button type="button" class="btn btn-ghost btn-sm pad-color" data-c="#c7dfdb" title="Salvia"><span style="width:10px;height:10px;border-radius:50%;background:#c7dfdb;display:inline-block;"></span></button>
                <button type="button" class="btn btn-ghost btn-sm pad-color" data-c="#a2e55f" title="Señal"><span style="width:10px;height:10px;border-radius:50%;background:#a2e55f;display:inline-block;"></span></button>
                <button id="clear-pad" type="button" class="btn btn-danger btn-sm">Borrar</button>
              </div>
            </div>
            <p class="xs muted">Resolvé despejes, fracciones o esquemas a mano alzada con mouse o pantalla táctil.</p>
            <canvas id="pad-canvas" class="lab-canvas" width="460" height="360"></canvas>
          </div>
        </div>
      `;

      drawGraph(body.querySelector("#graph-canvas"));
      body.querySelector("#toggle-l2").addEventListener("click", () => { showSecondLine = !showSecondLine; paint(); });
      body.querySelector("#m-slider").addEventListener("input", (e) => { slopeM = Number(e.target.value); paint(); });
      body.querySelector("#b-slider").addEventListener("input", (e) => { interceptB = Number(e.target.value); paint(); });
      body.querySelector("#m2-slider")?.addEventListener("input", (e) => { slopeM2 = Number(e.target.value); paint(); });
      body.querySelector("#b2-slider")?.addEventListener("input", (e) => { interceptB2 = Number(e.target.value); paint(); });
      setupScratchpad(body.querySelector("#pad-canvas"));
    }
  };

  paint();
}
