/**
 * Guided circuit labs: predict → simulate → measure with virtual instruments.
 *
 * Each practice comes from the electronics-for-robotics syllabus
 * (temarios/electronica-robotica-hardware.md). The learner writes a
 * prediction first; the simulation then plays the role of the bench and the
 * app compares both numbers. Progress is stored in settings.ui_state.circuit_lab
 * so the PC and the phone show the same checkmarks.
 */
import { icon } from "../icons.js";
import { api, esc, toast } from "../main.js";
import { simulate, operatingPoint, stats, crossingTime, fmtSI, parseSI } from "./circuit_sim.js";

/* ------------------------------------------------------------------ */
/* Constants                                                           */
/* ------------------------------------------------------------------ */

const E_RES = [100, 220, 330, 470, 680, 1000, 2200, 3300, 4700, 6800, 10000, 22000, 33000, 47000, 100000];
const E_CAP = [1e-6, 2.2e-6, 4.7e-6, 10e-6, 22e-6, 47e-6, 100e-6, 220e-6, 470e-6];

// Scope traces use a fixed dark screen (like a real scope) in both themes;
// `ink` is the same hue darkened enough to read on the page background.
export const CH = [
  { scope: "#5fd4c8", ink: "#1d8a80" },
  { scope: "#f4c04e", ink: "#b7790c" },
];

/* ------------------------------------------------------------------ */
/* Schematic drawing helpers (SVG, axis-aligned parts)                  */
/* ------------------------------------------------------------------ */

const SYMBOL = {
  R: `<polyline points="-20,0 -16,-7 -8,7 0,-7 8,7 16,-7 20,0"/>`,
  C: `<path d="M-20,0H-4M4,0H20M-4,-11V11M4,-11V11"/>`,
  L: `<path d="M-20,0 a5,5 0 0 1 10,0 a5,5 0 0 1 10,0 a5,5 0 0 1 10,0 a5,5 0 0 1 10,0"/>`,
  D: `<path d="M-20,0H-8M8,0H20M8,-8V8"/><polygon points="-8,-8 -8,8 8,0" class="csim-fill"/>`,
  BAT: `<path d="M-20,0H-3M3,0H20M-3,-13V13M3,-7V7"/>`,
  VSRC: `<path d="M-20,0H-14M14,0H20"/><circle r="14"/>`,
  SW_OPEN: `<path d="M-20,0H-12M12,0H20M-12,0L10,-12"/><circle cx="-12" r="2.2" class="csim-solid"/><circle cx="12" r="2.2" class="csim-solid"/>`,
  SW_CLOSED: `<path d="M-20,0H-12M12,0H20M-12,0L12,-2"/><circle cx="-12" r="2.2" class="csim-solid"/><circle cx="12" r="2.2" class="csim-solid"/>`,
};

/**
 * Draw a two-terminal part between (x1,y1) and (x2,y2). For D the first point
 * is the anode; for BAT the first point is the + terminal.
 */
export function part(kind, x1, y1, x2, y2, { name = "", value = "", side = "auto", off = false } = {}) {
  const cx = (x1 + x2) / 2;
  const cy = (y1 + y2) / 2;
  const len = Math.hypot(x2 - x1, y2 - y1);
  const ux = (x2 - x1) / len;
  const uy = (y2 - y1) / len;
  const ang = (Math.atan2(y2 - y1, x2 - x1) * 180) / Math.PI;
  const half = 20;
  const vertical = Math.abs(uy) > Math.abs(ux);
  let label = "";
  if (name || value) {
    if (vertical) {
      const left = side === "left";
      const tx = cx + (left ? -20 : 20);
      label = `<text x="${tx}" y="${cy - 3}" text-anchor="${left ? "end" : "start"}">${esc(name)}</text>
        <text x="${tx}" y="${cy + 12}" text-anchor="${left ? "end" : "start"}" class="csim-val">${esc(value)}</text>`;
    } else {
      const below = side === "below";
      label = `<text x="${cx}" y="${below ? cy + 26 : cy - 22}" text-anchor="middle">${esc(name)}${value ? ` <tspan class="csim-val">${esc(value)}</tspan>` : ""}</text>`;
    }
  }
  let extra = "";
  if (kind === "VSRC_PWM") {
    extra = `<path d="M${cx - 8},${cy + 4}H${cx - 4}V${cy - 4}H${cx}V${cy + 4}H${cx + 4}V${cy - 4}H${cx + 8}"/>`;
  }
  const sym = SYMBOL[kind === "VSRC_PWM" ? "VSRC" : kind];
  return `<g class="${off ? "csim-off" : ""}">
    <path d="M${x1},${y1}L${cx - ux * half},${cy - uy * half}M${cx + ux * half},${cy + uy * half}L${x2},${y2}"/>
    <g transform="translate(${cx} ${cy}) rotate(${ang})">${sym}</g>
    ${extra}
    ${label}
  </g>`;
}

export const wire = (...pts) => `<polyline points="${pts.map((p) => p.join(",")).join(" ")}"/>`;
export const dot = (x, y) => `<circle cx="${x}" cy="${y}" r="3" class="csim-solid"/>`;
export const gnd = (x, y) =>
  `<path d="M${x},${y}v8M${x - 10},${y + 8}h20M${x - 6},${y + 12}h12M${x - 2},${y + 16}h4"/>`;
export const nodeLabel = (x, y, text, anchor = "middle") =>
  `<text x="${x}" y="${y}" text-anchor="${anchor}" class="csim-node">${esc(text)}</text>`;

function probe(x, y, ch, text, dx = 26, dy = -22) {
  const c = CH[ch].ink;
  return `<g class="csim-probe" style="color:${c}">
    <path d="M${x},${y}L${x + dx},${y + dy}" stroke-dasharray="3 3"/>
    <circle cx="${x + dx}" cy="${y + dy}" r="5" class="csim-solid"/>
    <text x="${x + dx + 9}" y="${y + dy + 4}" class="csim-probe-text">${esc(text)}</text>
  </g>`;
}

const svgWrap = (w, h, inner, label) =>
  `<svg viewBox="0 0 ${w} ${h}" class="csim-schem" role="img" aria-label="${esc(label)}">${inner}</svg>`;

/* ------------------------------------------------------------------ */
/* Small helpers                                                       */
/* ------------------------------------------------------------------ */

/** Smallest 1-2-5 step that is >= x. */
export function niceStep(x) {
  if (!(x > 0)) return 1;
  const p = Math.pow(10, Math.floor(Math.log10(x)));
  for (const m of [1, 2, 5, 10]) if (m * p >= x * 0.9999) return m * p;
  return 10 * p;
}

function within(pred, meas, tol) {
  return Math.abs(pred - meas) <= Math.max(tol.abs ?? 0, (tol.rel ?? 0) * Math.abs(meas));
}

const pct = (pred, meas) => {
  const v = meas === 0 ? 0 : ((pred - meas) / Math.abs(meas)) * 100;
  return Math.abs(v) < 0.05 ? 0 : v; // avoid "-0.0 %"
};

/* ------------------------------------------------------------------ */
/* Practices                                                           */
/* ------------------------------------------------------------------ */

const PRACTICES = [
  /* ---------------- Módulo 1 · Divisor con carga ---------------- */
  {
    id: "m1-divisor",
    module: "Módulo 1 · Práctica 1",
    title: "Divisor de tensión con carga",
    goal: "Ver por qué un divisor deja de dar la tensión calculada cuando le conectás algo.",
    steps: [
      "Calculá V(OUT) sin carga: V<sub>in</sub> · R2 / (R1 + R2).",
      "Conectá la carga RL y volvé a predecir. Pista: RL queda en paralelo con R2.",
      "Probá una RL mucho más grande que R2 y una parecida. ¿Cuándo el divisor «aguanta»?",
    ],
    defaults: { r1: 10000, r2: 10000, load: true, rl: 10000 },
    controls: [
      { key: "r1", label: "R1", kind: "select", options: E_RES, unit: "Ω" },
      { key: "r2", label: "R2", kind: "select", options: E_RES, unit: "Ω" },
      { key: "load", label: "Carga RL conectada", kind: "toggle" },
      { key: "rl", label: "RL (la carga)", kind: "select", options: E_RES, unit: "Ω", showIf: (p) => p.load },
    ],
    build(p) {
      const elements = [
        { type: "V", name: "V1", a: "vin", b: "0", dc: 12 },
        { type: "R", name: "R1", a: "vin", b: "out", value: p.r1 },
        { type: "R", name: "R2", a: "out", b: "0", value: p.r2 },
      ];
      if (p.load) elements.push({ type: "R", name: "RL", a: "out", b: "0", value: p.rl });
      return { nodes: ["vin", "out"], elements };
    },
    run(p) {
      const op = operatingPoint(this.build(p));
      return { op, measured: op.v.out };
    },
    instrument: "meter",
    meterReadings: (p, r) => [
      { id: "vout", label: "V(OUT)", text: fmtSI(r.op.v.out, "V", 4), mode: "V ⎓" },
      { id: "irl", label: "I por RL", text: p.load ? fmtSI(r.op.i.RL, "A", 3) : "— (sin carga)", mode: "A ⎓" },
      { id: "ir1", label: "I por R1", text: fmtSI(r.op.i.R1, "A", 3), mode: "A ⎓" },
    ],
    task: {
      kind: "number",
      unit: "V",
      prompt: "¿Cuánto vas a medir entre OUT y masa?",
      tol: { rel: 0.02, abs: 0.02 },
    },
    explain(p, r) {
      const vth = (12 * p.r2) / (p.r1 + p.r2);
      const rth = (p.r1 * p.r2) / (p.r1 + p.r2);
      const vout = r.op.v.out;
      if (!p.load) {
        return `Sin carga es el divisor «de libro»: 12 V · ${fmtSI(p.r2, "Ω")} / (${fmtSI(p.r1, "Ω")} + ${fmtSI(p.r2, "Ω")}) = <strong>${fmtSI(vth, "V", 4)}</strong>.
          Ahora conectá RL y fijate cuánto cambia.`;
      }
      const drop = ((vth - vout) / vth) * 100;
      return `Visto desde OUT, el divisor es una fuente de <strong>Thévenin</strong>: V<sub>th</sub> = ${fmtSI(vth, "V", 4)} con una resistencia interna R<sub>th</sub> = R1 ∥ R2 = ${fmtSI(rth, "Ω", 3)}.
        Al colgarle RL = ${fmtSI(p.rl, "Ω")} se forma otro divisor: V<sub>th</sub> · RL / (R<sub>th</sub> + RL) = <strong>${fmtSI(vout, "V", 4)}</strong>,
        un ${drop.toFixed(1)} % menos que sin carga. ${
          p.rl >= 10 * rth
            ? "Como RL es más de 10 veces R<sub>th</sub>, el divisor casi no se entera."
            : "RL es comparable a R<sub>th</sub>, así que el divisor «se cae». Por eso un divisor no sirve para alimentar cosas: para eso está el buffer (módulo 7) o un regulador (módulo 10)."
        }`;
    },
    schematic(p) {
      const inner = `
        ${part("BAT", 50, 60, 50, 200, { name: "Vin", value: "12 V", side: "left" })}
        ${wire([50, 60], [100, 60])}
        ${part("R", 100, 60, 200, 60, { name: "R1", value: fmtSI(p.r1, "Ω") })}
        ${wire([200, 60], [330, 60])}
        ${dot(240, 60)}
        ${nodeLabel(240, 48, "OUT")}
        ${part("R", 240, 60, 240, 200, { name: "R2", value: fmtSI(p.r2, "Ω") })}
        ${part("R", 330, 60, 330, 200, { name: "RL", value: p.load ? fmtSI(p.rl, "Ω") : "desconectada", off: !p.load })}
        ${wire([50, 200], [330, 200])}
        ${dot(240, 200)}
        ${gnd(190, 200)}
        ${probe(240, 60, 0, "V", 30, -28)}`;
      return svgWrap(420, 240, inner, "Divisor de tensión R1-R2 con carga RL");
    },
  },

  /* ---------------- Módulo 2 · Carga RC ---------------- */
  {
    id: "m2-rc",
    module: "Módulo 2 · Práctica 1",
    title: "Carga de un capacitor (constante de tiempo)",
    goal: "Medir τ con el osciloscopio y comprobar que vale R·C.",
    steps: [
      "Predecí τ = R · C (cuidado con los prefijos: k = 10³, µ = 10⁻⁶).",
      "Simulá y usá el cursor del osciloscopio: τ es el tiempo desde que cierra S1 (marca T, t = 0) hasta que V(C) llega al 63 % de la fuente (3,16 V).",
      "Cambiá R o C y fijate cómo se estira o se encoge la curva.",
    ],
    defaults: { r: 10000, c: 100e-6 },
    controls: [
      { key: "r", label: "R", kind: "select", options: E_RES, unit: "Ω" },
      { key: "c", label: "C", kind: "select", options: E_CAP, unit: "F" },
    ],
    build(p, closeAt = 0) {
      return {
        nodes: ["vs", "sw", "out"],
        elements: [
          { type: "V", name: "V1", a: "vs", b: "0", dc: 5 },
          { type: "S", name: "S1", a: "vs", b: "sw", ron: 0.01, roff: 1e12, on: (t) => t >= closeAt * (1 - 1e-9) }, // tolerate float error in the time grid
          { type: "R", name: "R", a: "sw", b: "out", value: p.r },
          { type: "C", name: "C", a: "out", b: "0", value: p.c, ic: 0 },
        ],
      };
    },
    run(p) {
      const tau = p.r * p.c;
      const tdiv = niceStep((6 * tau) / 10);
      const tStop = 10 * tdiv;
      const closeAt = tdiv; // S1 closes one division in, like a scope triggered on the step
      const sim = simulate(this.build(p, closeAt), { tStop, dt: tStop / 20000, record: 1200 });
      const measured = crossingTime(sim.t, sim.v.out, 5 * (1 - Math.exp(-1)), 1) - closeAt;
      return {
        sim,
        measured,
        scope: {
          tdiv,
          trigger: closeAt,
          channels: [
            { label: "CH1 · V(C)", data: sim.v.out, unit: "V" },
            { label: "CH2 · después de S1", data: sim.v.sw, unit: "V" },
          ],
          markers: [{ ch: 0, level: 5 * (1 - Math.exp(-1)), text: "63 %" }],
        },
      };
    },
    instrument: "scope",
    task: {
      kind: "number",
      unit: "s",
      prompt: "¿Cuánto vale τ? (podés escribir 1 s, 470 ms, 0,22…)",
      tol: { rel: 0.05 },
    },
    explain(p, r) {
      const tau = p.r * p.c;
      return `τ = R · C = ${fmtSI(p.r, "Ω")} · ${fmtSI(p.c, "F")} = <strong>${fmtSI(tau, "s")}</strong>. En la simulación, V(C) cruzó 3,16 V a los <strong>${fmtSI(r.measured, "s")}</strong>.
        A 1τ el capacitor está al 63 %, a 3τ al 95 % y a 5τ al 99 %: por eso se dice que «tarda 5τ en cargarse».
        Esta misma cuenta te dice cuánto tarda el antirrebote de un pulsador o cuánto filtra un RC.`;
    },
    schematic(p) {
      const inner = `
        ${part("BAT", 50, 60, 50, 200, { name: "V1", value: "5 V", side: "left" })}
        ${wire([50, 60], [80, 60])}
        ${part("SW_OPEN", 80, 60, 150, 60, { name: "S1", value: "cierra en t=0" })}
        ${wire([150, 60], [170, 60])}
        ${dot(165, 60)}
        ${part("R", 170, 60, 270, 60, { name: "R", value: fmtSI(p.r, "Ω") })}
        ${wire([270, 60], [300, 60])}
        ${dot(300, 60)}
        ${part("C", 300, 60, 300, 200, { name: "C", value: fmtSI(p.c, "F") })}
        ${wire([50, 200], [300, 200])}
        ${gnd(175, 200)}
        ${probe(300, 60, 0, "CH1", 30, -28)}
        ${probe(165, 60, 1, "CH2", -10, -36)}`;
      return svgWrap(400, 240, inner, "Circuito RC: batería, llave, resistencia y capacitor");
    },
  },

  /* ---------------- Módulo 2 · Pico inductivo ---------------- */
  {
    id: "m2-pico",
    module: "Módulo 2 · Práctica 3",
    title: "El pico inductivo (y el diodo de rueda libre)",
    goal: "Ver qué pasa cuando cortás de golpe la corriente de una bobina, como la de un relé o un motor.",
    steps: [
      "Sin diodo: predecí hasta dónde sube la tensión del colector cuando Q1 se apaga.",
      "Simulá y mirá CH1. El transistor de este modelo empieza a conducir «por avalancha» cerca de 60 V.",
      "Activá el diodo de rueda libre, predecí de nuevo y compará las dos capturas.",
    ],
    defaults: { diode: false },
    controls: [{ key: "diode", label: "Diodo de rueda libre D1", kind: "toggle" }],
    build(p) {
      const elements = [
        { type: "V", name: "V1", a: "vcc", b: "0", dc: 5 },
        { type: "R", name: "Rbob", a: "vcc", b: "m", value: 70 },
        { type: "L", name: "Lbob", a: "m", b: "col", value: 0.05, ic: 0 },
        { type: "S", name: "Q1", a: "col", b: "0", ron: 0.2, roff: 1e9, on: (t) => t >= 1e-3 && t < 5e-3 },
        // collector-emitter avalanche of the transistor, modeled as a 60 V breakdown
        { type: "D", name: "Qbv", a: "0", b: "col", is: 1e-14, n: 1, bv: 60 },
      ];
      if (p.diode) elements.push({ type: "D", name: "D1", a: "col", b: "vcc", is: 1e-9, n: 1.8 });
      return { nodes: ["vcc", "m", "col"], elements };
    },
    run(p) {
      const tStop = 10e-3;
      const sim = simulate(this.build(p), { tStop, dt: 0.5e-6, record: 4000 });
      const peak = stats(sim.v.col).max;
      return {
        sim,
        peak,
        measured: peak > 20 ? 2 : peak > 5.3 ? 1 : 0,
        scope: {
          tdiv: 1e-3,
          channels: [
            { label: "CH1 · V(colector)", data: sim.v.col, unit: "V" },
            { label: "CH2 · I(bobina)", data: sim.i.Lbob, unit: "A" },
          ],
        },
      };
    },
    instrument: "scope",
    task: {
      kind: "choice",
      prompt: "Cuando Q1 se apaga (t = 5 ms), ¿hasta dónde sube la tensión del colector?",
      options: [
        "Hasta 5 V, como la fuente",
        "Un poco más de 5 V (≈ 5,7 V)",
        "Decenas de voltios: lo que aguante el transistor",
      ],
    },
    explain(p, r) {
      const i = 5 / 70.2;
      const e = 0.5 * 0.05 * i * i;
      const base = `Con Q1 encendido circula I ≈ 5 V / 70 Ω = ${fmtSI(i, "A")} y la bobina guarda E = ½·L·I² = ${fmtSI(e, "J")}.
        Una bobina no deja que su corriente cambie de golpe (V = L·di/dt): si le cortás el camino, sube la tensión hasta encontrar uno.`;
      if (!p.diode) {
        return `${base} Sin diodo, el colector subió a <strong>${fmtSI(r.peak, "V")}</strong>: la energía se descargó «rompiendo» el transistor por avalancha.
          En la vida real eso degrada o mata al transistor, y el pico se acopla como ruido a todo el circuito. Activá D1 y compará.`;
      }
      return `${base} Con D1, la corriente encuentra un camino de vuelta a +5 V y el colector queda en <strong>${fmtSI(r.peak, "V")}</strong> (5 V + la caída del diodo).
        Mirá CH2: la corriente ya no se corta de golpe, baja despacio por la bobina y el diodo. Por eso todo relé, solenoide y motor lleva su diodo de rueda libre.`;
    },
    schematic(p) {
      const inner = `
        ${part("BAT", 50, 40, 50, 260, { name: "V1", value: "5 V", side: "left" })}
        ${wire([50, 40], [250, 40])}
        ${dot(250, 40)}
        ${nodeLabel(150, 30, "+5 V")}
        ${part("L", 250, 40, 250, 170, { name: "Bobina del relé", value: "70 Ω · 50 mH", side: "left" })}
        ${wire([250, 40], [420, 40])}
        ${part("D", 420, 170, 420, 40, { name: "D1", value: p.diode ? "1N4007" : "sin diodo", off: !p.diode })}
        ${wire([250, 170], [420, 170])}
        ${dot(250, 170)}
        ${part("SW_OPEN", 250, 170, 250, 260, { name: "Q1 (transistor)", value: "encendido 1–5 ms", side: "left" })}
        ${wire([50, 260], [250, 260])}
        ${gnd(150, 260)}
        ${probe(250, 170, 0, "CH1", 40, 26)}
        ${probe(250, 105, 1, "CH2 (corriente)", 30, -20)}`;
      return svgWrap(520, 290, inner, "Bobina de relé conmutada por un transistor, con diodo de rueda libre opcional");
    },
  },

  /* ---------------- Módulo 3 · PWM + filtro RC ---------------- */
  {
    id: "m3-pwm",
    module: "Módulo 3 · Práctica 1",
    title: "PWM + filtro RC = tensión «analógica»",
    goal: "Convertir el PWM del Arduino en una tensión continua y ver el compromiso entre rizado y velocidad.",
    steps: [
      "Predecí el valor medio de la salida en régimen: el filtro deja pasar el promedio del PWM.",
      "Simulá y mirá CH2 en «Régimen»: el valor medio y el rizado (Vpp).",
      "Pasá a «Arranque» y subí C: menos rizado, pero tarda más en llegar. Ese es el compromiso.",
    ],
    defaults: { duty: 0.5, freq: 490, r: 10000, c: 1e-6, view: "steady" },
    controls: [
      { key: "duty", label: "Ciclo de trabajo", kind: "range", min: 0.05, max: 0.95, step: 0.05, fmt: (v) => `${Math.round(v * 100)} %` },
      { key: "freq", label: "Frecuencia PWM", kind: "select", options: [490, 980], unit: "Hz" },
      { key: "r", label: "R", kind: "select", options: [1000, 4700, 10000], unit: "Ω" },
      { key: "c", label: "C", kind: "select", options: [0.1e-6, 1e-6, 4.7e-6, 10e-6], unit: "F" },
      { key: "view", label: "Vista del osciloscopio", kind: "segmented", options: [["steady", "Régimen"], ["startup", "Arranque"]], live: true },
    ],
    build(p) {
      return {
        nodes: ["pwm", "out"],
        elements: [
          { type: "V", name: "V1", a: "pwm", b: "0", wave: { kind: "pwm", high: 5, low: 0, freq: p.freq, duty: p.duty } },
          { type: "R", name: "R", a: "pwm", b: "out", value: p.r },
          { type: "C", name: "C", a: "out", b: "0", value: p.c, ic: 0 },
        ],
      };
    },
    run(p) {
      const T = 1 / p.freq;
      const tau = p.r * p.c;
      const periods = Math.max(8, Math.ceil((7 * tau) / T));
      const tStop = periods * T;
      const dt = T / 200;
      const circuit = this.build(p);
      const steady = simulate(circuit, { tStop, dt, recordFrom: tStop - 4 * T, record: 1600 });
      const st = stats(steady.v.out);
      const out = { measured: st.mean, ripple: st.pp, tau, T };
      out.views = {
        steady: {
          sim: steady,
          tdiv: niceStep((4 * T) / 10),
          t0: steady.t[0],
          channels: [
            { label: "CH1 · PWM", data: steady.v.pwm, unit: "V" },
            { label: "CH2 · V(C)", data: steady.v.out, unit: "V" },
          ],
        },
      };
      if (p.view === "startup") {
        const tdivStart = niceStep(Math.max(6 * tau, 4 * T) / 10);
        const full = simulate(circuit, { tStop: 10 * tdivStart, dt, record: 2000 });
        out.views.startup = {
          sim: full,
          tdiv: tdivStart,
          channels: [
            { label: "CH1 · PWM", data: full.v.pwm, unit: "V" },
            { label: "CH2 · V(C)", data: full.v.out, unit: "V" },
          ],
        };
      }
      return out;
    },
    scopeFor(p, r) {
      const v = r.views[p.view] || r.views.steady;
      return { tdiv: v.tdiv, t0: v.t0 ?? 0, channels: v.channels, sim: v.sim };
    },
    instrument: "scope",
    task: {
      kind: "number",
      unit: "V",
      prompt: "¿Cuál es el valor medio de V(C) en régimen?",
      tol: { rel: 0.03, abs: 0.05 },
    },
    explain(p, r) {
      const approx = (5 * p.duty * (1 - p.duty)) / (p.freq * p.r * p.c);
      return `El filtro deja pasar el promedio: D · 5 V = ${Math.round(p.duty * 100)} % · 5 V = <strong>${fmtSI(5 * p.duty, "V", 3)}</strong> (medido: ${fmtSI(r.measured, "V", 3)}).
        El rizado medido es <strong>${fmtSI(r.ripple, "V")} pico a pico</strong>${
          r.tau > 3 * r.T ? ` (la aproximación 5·D·(1−D)/(f·R·C) da ${fmtSI(approx, "V")})` : ""
        }.
        Con τ = R·C = ${fmtSI(r.tau, "s")}: más grande → menos rizado pero respuesta más lenta (mirá la vista «Arranque»). Subir la frecuencia del PWM baja el rizado sin hacer más lento el filtro.`;
    },
    schematic(p) {
      const inner = `
        ${part("VSRC_PWM", 50, 60, 50, 200, { name: "PWM", value: `${p.freq} Hz · ${Math.round(p.duty * 100)} %`, side: "left" })}
        ${wire([50, 60], [110, 60])}
        ${dot(90, 60)}
        ${part("R", 110, 60, 220, 60, { name: "R", value: fmtSI(p.r, "Ω") })}
        ${wire([220, 60], [260, 60])}
        ${dot(260, 60)}
        ${part("C", 260, 60, 260, 200, { name: "C", value: fmtSI(p.c, "F") })}
        ${wire([50, 200], [260, 200])}
        ${gnd(155, 200)}
        ${probe(90, 60, 0, "CH1", -10, -34)}
        ${probe(260, 60, 1, "CH2", 30, -28)}`;
      return svgWrap(380, 240, inner, "Filtro RC pasa bajos alimentado con PWM");
    },
  },
];

/* ------------------------------------------------------------------ */
/* Instruments                                                         */
/* ------------------------------------------------------------------ */

function meterHTML(readings, selectedId) {
  const sel = readings.find((r) => r.id === selectedId) || readings[0];
  return `
    <div class="csim-meter">
      <div class="csim-lcd" aria-live="polite">
        <span class="csim-lcd-mode">${esc(sel.mode)}</span>
        <span class="csim-lcd-value">${esc(sel.text)}</span>
        <span class="csim-lcd-label">${esc(sel.label)}</span>
      </div>
      <div class="segmented csim-meter-sel" role="group" aria-label="Qué medir">
        ${readings
          .map(
            (r) => `<button type="button" class="seg-btn ${r.id === sel.id ? "active" : ""}" data-meter="${r.id}">${esc(r.label)}</button>`
          )
          .join("")}
      </div>
    </div>`;
}

/**
 * Draw a scope screen. Each channel gets its own V/div (like a real scope);
 * all channels share the ground line.
 */
export function drawScope(canvas, scope, cursorX = null) {
  const dpr = window.devicePixelRatio || 1;
  const w = canvas.clientWidth;
  const h = canvas.clientHeight;
  if (!w || !h) return null;
  canvas.width = Math.round(w * dpr);
  canvas.height = Math.round(h * dpr);
  const ctx = canvas.getContext("2d");
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

  const DX = 10;
  const DY = 8;
  ctx.fillStyle = "#141917";
  ctx.fillRect(0, 0, w, h);

  const t = scope.sim.t;
  const t0 = scope.t0 ?? t[0] ?? 0;
  const tSpan = scope.tdiv * DX;

  // vertical layout: ground at 1 div from the bottom unless a trace goes negative
  // (small undershoots such as a diode's -0.6 V do not justify losing half the screen)
  const anyNeg = scope.channels.some((c) => {
    const s = stats(c.data);
    return s.min < -0.15 * Math.max(1e-12, s.max);
  });
  const groundDiv = anyNeg ? DY / 2 : 1;
  // Channels with the same unit share V/div so their heights compare directly
  // (a 2.5 V trace must look half as tall as a 5 V one).
  const room = anyNeg ? DY / 2 - 0.3 : DY - groundDiv - 0.4;
  const maxByUnit = {};
  for (const c of scope.channels) {
    const s = stats(c.data);
    const m = Math.max(Math.abs(s.max), Math.abs(s.min), 1e-12);
    maxByUnit[c.unit] = Math.max(maxByUnit[c.unit] ?? 0, m);
  }
  const scales = scope.fixedScales || scope.channels.map((c) => niceStep(maxByUnit[c.unit] / room));

  // grid
  ctx.strokeStyle = "rgba(255,255,255,0.10)";
  ctx.lineWidth = 1;
  for (let i = 0; i <= DX; i++) {
    const x = Math.round((i / DX) * w) + 0.5;
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
  }
  for (let j = 0; j <= DY; j++) {
    const y = Math.round((j / DY) * h) + 0.5;
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
  }
  const yOf = (v, scale) => h - ((groundDiv + v / scale) / DY) * h;
  const xOf = (tt) => ((tt - t0) / tSpan) * w;

  // ground marker
  ctx.strokeStyle = "rgba(255,255,255,0.28)";
  ctx.setLineDash([4, 4]);
  ctx.beginPath(); ctx.moveTo(0, yOf(0, 1)); ctx.lineTo(w, yOf(0, 1)); ctx.stroke();
  ctx.setLineDash([]);

  // reference markers (e.g. the 63 % level)
  for (const m of scope.markers || []) {
    const y = yOf(m.level, scales[m.ch]);
    ctx.strokeStyle = "rgba(255,255,255,0.35)";
    ctx.setLineDash([2, 5]);
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = "rgba(255,255,255,0.6)";
    ctx.font = "11px ui-monospace, monospace";
    ctx.fillText(m.text, 6, y - 4);
  }

  // trigger marker: a small "T" at the top, where t = 0 is for the cursor
  if (scope.trigger != null) {
    const xt = xOf(scope.trigger);
    ctx.fillStyle = "rgba(255,255,255,0.75)";
    ctx.beginPath(); ctx.moveTo(xt - 5, 0); ctx.lineTo(xt + 5, 0); ctx.lineTo(xt, 7); ctx.closePath(); ctx.fill();
    ctx.font = "11px ui-monospace, monospace";
    ctx.fillText("T", xt + 7, 11);
  }

  // traces
  scope.channels.forEach((c, k) => {
    ctx.strokeStyle = CH[k].scope;
    ctx.lineWidth = 1.8;
    ctx.beginPath();
    let started = false;
    for (let i = 0; i < t.length; i++) {
      const x = xOf(t[i]);
      if (x < -2 || x > w + 2) continue;
      const y = yOf(c.data[i], scales[k]);
      if (!started) { ctx.moveTo(x, y); started = true; } else ctx.lineTo(x, y);
    }
    ctx.stroke();
  });

  // cursor
  let readout = null;
  if (cursorX != null) {
    const tc = t0 + (cursorX / w) * tSpan;
    let best = 0;
    let bestD = Infinity;
    for (let i = 0; i < t.length; i++) {
      const d = Math.abs(t[i] - tc);
      if (d < bestD) { bestD = d; best = i; }
    }
    const x = xOf(t[best]);
    ctx.strokeStyle = "rgba(255,255,255,0.75)";
    ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
    scope.channels.forEach((c, k) => {
      ctx.fillStyle = CH[k].scope;
      ctx.beginPath(); ctx.arc(x, yOf(c.data[best], scales[k]), 3.5, 0, Math.PI * 2); ctx.fill();
    });
    readout = { t: t[best] - (scope.trigger ?? (scope.t0 ? t0 : 0)), values: scope.channels.map((c) => ({ label: c.label, v: c.data[best], unit: c.unit })) };
  }
  return { scales, readout };
}

function scopeHTML(scope) {
  // numerical dust (pV, nA) reads as noise to a learner: show it as 0
  const s = scope.channels.map((c) => {
    const st = stats(c.data);
    const span = Math.max(Math.abs(st.max), Math.abs(st.min));
    const clean = (v) => (Math.abs(v) < 1e-5 * span ? 0 : v);
    return { max: clean(st.max), min: clean(st.min), mean: clean(st.mean), pp: clean(st.pp) };
  });
  return `
    <div class="csim-scope">
      <canvas class="csim-screen" aria-label="Pantalla del osciloscopio"></canvas>
      <div class="csim-scope-bar mono xs">
        <span>${fmtSI(scope.tdiv, "s")}/div</span>
        ${scope.channels.map((c, k) => `<span style="color:${CH[k].ink}" class="csim-chdiv" data-ch="${k}">${esc(c.label)}</span>`).join("")}
      </div>
      <div class="csim-cursor mono xs" aria-live="polite">Pasá el mouse o el dedo por la pantalla para mover el cursor.</div>
      <div class="csim-measures">
        ${scope.channels
          .map(
            (c, k) => `<div class="card-flat csim-measure" style="border-left:3px solid ${CH[k].ink}">
              <div class="xs mono muted">${esc(c.label)}</div>
              <div class="mono small">máx ${fmtSI(s[k].max, c.unit)} · mín ${fmtSI(s[k].min, c.unit)}</div>
              <div class="mono small">media ${fmtSI(s[k].mean, c.unit)} · Vpp ${fmtSI(s[k].pp, c.unit)}</div>
            </div>`
          )
          .join("")}
      </div>
    </div>`;
}

function wireScope(root, scope) {
  const canvas = root.querySelector(".csim-screen");
  if (!canvas) return;
  const bar = root.querySelector(".csim-scope-bar");
  const cursorBox = root.querySelector(".csim-cursor");
  let cursorX = null;
  const paint = () => {
    const res = drawScope(canvas, scope, cursorX);
    if (!res) return;
    bar.querySelectorAll(".csim-chdiv").forEach((el) => {
      const k = Number(el.dataset.ch);
      el.textContent = `${scope.channels[k].label}: ${fmtSI(res.scales[k], scope.channels[k].unit)}/div`;
    });
    if (res.readout) {
      cursorBox.innerHTML = `Cursor: t = <strong>${fmtSI(res.readout.t, "s", 4)}</strong>${res.readout.values
        .map((v, k) => ` · <span style="color:${CH[k].ink}">${esc(v.label.split("·")[0].trim())} = <strong>${fmtSI(v.v, v.unit, 4)}</strong></span>`)
        .join("")}`;
    }
  };
  const move = (e) => {
    const rect = canvas.getBoundingClientRect();
    cursorX = Math.min(rect.width, Math.max(0, e.clientX - rect.left));
    paint();
  };
  canvas.addEventListener("pointermove", move);
  canvas.addEventListener("pointerdown", move);
  paint();
  if (typeof ResizeObserver !== "undefined") {
    const ro = new ResizeObserver(() => {
      if (!canvas.isConnected) { ro.disconnect(); return; }
      paint();
    });
    ro.observe(canvas);
  }
}

/* ------------------------------------------------------------------ */
/* Styles (scoped with the csim- prefix)                                */
/* ------------------------------------------------------------------ */

export function ensureStyles() {
  if (document.getElementById("csim-styles")) return;
  const st = document.createElement("style");
  st.id = "csim-styles";
  st.textContent = `
    .csim-list { display:grid; grid-template-columns:repeat(auto-fill,minmax(220px,1fr)); gap:10px; }
    .csim-pick { text-align:left; cursor:pointer; display:flex; flex-direction:column; gap:4px; border:1px solid var(--border); background:var(--bg-card); border-radius:var(--radius); padding:12px 14px; color:var(--text); font:inherit; }
    .csim-pick:hover { border-color:var(--border-strong); }
    .csim-pick.active { border-color:var(--accent); box-shadow:inset 0 0 0 1px var(--accent); }
    .csim-pick-title { font-weight:600; line-height:1.3; }
    .csim-pick-top { display:flex; justify-content:space-between; align-items:center; gap:8px; }
    .csim-done { color:var(--ok); display:inline-flex; align-items:center; gap:4px; }
    .csim-schem { width:100%; height:auto; max-height:300px; color:var(--text); fill:none; stroke:currentColor; stroke-width:1.8; stroke-linecap:round; stroke-linejoin:round; }
    .csim-schem text { fill:currentColor; stroke:none; font:12px var(--font-mono); }
    .csim-schem .csim-val { fill:var(--text-muted); font-size:11px; }
    .csim-schem .csim-node { font-weight:600; font-size:11px; }
    .csim-schem .csim-solid { fill:currentColor; }
    .csim-schem .csim-fill { fill:currentColor; fill-opacity:.15; }
    .csim-schem .csim-off { opacity:.3; }
    .csim-schem .csim-off path, .csim-schem .csim-off polyline { stroke-dasharray:4 4; }
    .csim-schem .csim-probe { stroke:currentColor; }
    .csim-schem .csim-probe-text { fill:currentColor; font-weight:600; }
    .csim-steps { margin:0; padding-left:1.2em; display:grid; gap:4px; }
    .csim-controls { display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:10px 14px; }
    .csim-toggle { display:flex; align-items:center; gap:8px; cursor:pointer; padding-top:20px; }
    .csim-toggle input { width:18px; height:18px; accent-color:var(--accent); }
    .csim-predict { display:flex; gap:8px; align-items:center; flex-wrap:wrap; }
    .csim-predict input[type=text] { flex:1; min-width:120px; }
    .csim-choice { display:grid; gap:6px; }
    .csim-choice label { display:flex; gap:8px; align-items:flex-start; padding:8px 10px; border:1px solid var(--border); border-radius:var(--radius-sm); cursor:pointer; }
    .csim-choice label:has(input:checked) { border-color:var(--accent); background:var(--accent-soft); }
    .csim-choice input { margin-top:3px; accent-color:var(--accent); }
    .csim-meter { display:grid; gap:10px; }
    .csim-lcd { background:#1b221e; color:#c9f2d6; border-radius:var(--radius); padding:14px 16px; display:grid; grid-template-columns:auto 1fr; grid-template-areas:"mode value" "label label"; align-items:baseline; gap:2px 12px; border:6px solid #3a3a37; }
    .csim-lcd-mode { grid-area:mode; font:600 13px var(--font-mono); opacity:.75; }
    .csim-lcd-value { grid-area:value; text-align:right; font:500 clamp(1.6rem,6vw,2.3rem) var(--font-mono); letter-spacing:.02em; }
    .csim-lcd-label { grid-area:label; font:12px var(--font-mono); opacity:.7; }
    .csim-meter-sel { flex-wrap:wrap; }
    .csim-scope { display:grid; gap:8px; }
    .csim-screen { width:100%; aspect-ratio:10/8; max-height:380px; display:block; border-radius:var(--radius-sm); border:6px solid #3a3a37; touch-action:none; cursor:crosshair; background:#141917; }
    .csim-scope-bar { display:flex; flex-wrap:wrap; gap:4px 14px; }
    .csim-cursor { min-height:1.4em; color:var(--text-secondary); }
    .csim-measures { display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:8px; }
    .csim-measure { padding:8px 10px; }
    .csim-compare { display:grid; grid-template-columns:repeat(3,1fr); gap:8px; }
    .csim-compare .card-flat { padding:8px 10px; }
    @media (max-width:560px) { .csim-compare { grid-template-columns:1fr; } }
  `;
  document.head.appendChild(st);
}

/* ------------------------------------------------------------------ */
/* Main render                                                         */
/* ------------------------------------------------------------------ */

/**
 * Render the guided simulator into `body`. `startId` picks the practice.
 * Returns nothing; keeps its own state between re-renders of the parent tab
 * through the module-level `memory` object.
 */
const memory = { active: null, perPractice: {}, progress: null, meterSel: {} };

export async function renderCircuitLab(body, { startId = null } = {}) {
  ensureStyles();
  if (startId && PRACTICES.some((p) => p.id === startId)) memory.active = startId;
  if (!memory.active) memory.active = PRACTICES[0].id;

  if (memory.progress == null) {
    memory.progress = {};
    try {
      const { settings } = await api.get("/api/settings");
      memory.progress = { ...(settings.ui_state?.circuit_lab || {}) };
    } catch {
      // offline: progress still works for this visit
    }
  }

  const stateOf = (pr) => {
    if (!memory.perPractice[pr.id]) {
      memory.perPractice[pr.id] = { params: { ...pr.defaults }, prediction: "", choice: null, result: null, graded: null };
    }
    return memory.perPractice[pr.id];
  };

  const saveProgress = async (pr, ok) => {
    const prev = memory.progress[pr.id] || { tries: 0, ok: false };
    memory.progress[pr.id] = {
      tries: (prev.tries || 0) + 1,
      ok: prev.ok || ok,
      last: new Date().toISOString(),
    };
    try {
      await api.put("/api/settings", { ui_state: { circuit_lab: memory.progress } });
    } catch {
      // keep it in memory; next successful save will carry it
    }
  };

  const paint = () => {
    if (!body.isConnected) return;
    const pr = PRACTICES.find((p) => p.id === memory.active);
    const st = stateOf(pr);
    const p = st.params;
    const doneCount = PRACTICES.filter((x) => memory.progress[x.id]?.ok).length;

    const controlsHTML = pr.controls
      .filter((c) => !c.showIf || c.showIf(p))
      .map((c) => {
        if (c.kind === "select") {
          return `<label class="field"><span>${esc(c.label)}</span>
            <select data-key="${c.key}">
              ${c.options.map((v, i) => `<option value="${i}" ${v === p[c.key] ? "selected" : ""}>${esc(fmtSI(v, c.unit))}</option>`).join("")}
            </select></label>`;
        }
        if (c.kind === "toggle") {
          return `<label class="csim-toggle"><input type="checkbox" data-key="${c.key}" ${p[c.key] ? "checked" : ""}/> <span>${esc(c.label)}</span></label>`;
        }
        if (c.kind === "range") {
          return `<label class="field"><span class="row-between"><span>${esc(c.label)}</span><strong class="mono">${esc(c.fmt(p[c.key]))}</strong></span>
            <input type="range" data-key="${c.key}" min="${c.min}" max="${c.max}" step="${c.step}" value="${p[c.key]}"/></label>`;
        }
        if (c.kind === "segmented") {
          return `<div class="field"><span>${esc(c.label)}</span>
            <div class="segmented" style="width:fit-content;">
              ${c.options.map(([v, lbl]) => `<button type="button" class="seg-btn ${p[c.key] === v ? "active" : ""}" data-seg="${c.key}" data-val="${v}">${esc(lbl)}</button>`).join("")}
            </div></div>`;
        }
        return "";
      })
      .join("");

    const task = pr.task;
    const predictHTML =
      task.kind === "number"
        ? `<div class="csim-predict">
            <input type="text" id="csim-pred" inputmode="decimal" autocomplete="off" placeholder="Tu predicción (${esc(task.unit)})" value="${esc(st.prediction)}" aria-label="Tu predicción en ${esc(task.unit)}"/>
            <span class="mono muted">${esc(task.unit)}</span>
          </div>`
        : `<div class="csim-choice" role="radiogroup" aria-label="Tu predicción">
            ${task.options
              .map((o, i) => `<label><input type="radio" name="csim-choice" value="${i}" ${st.choice === i ? "checked" : ""}/> <span>${esc(o)}</span></label>`)
              .join("")}
          </div>`;

    let resultHTML = "";
    if (st.result) {
      const r = st.result;
      let verdict = "";
      if (st.graded) {
        const g = st.graded;
        const cls = g.ok ? "callout-ok" : "callout-warn";
        const head = g.ok ? `${icon("check", 14)} ¡Bien predicho!` : `${icon("alert", 14)} No coincide: revisá la explicación y probá de nuevo.`;
        const cmp =
          task.kind === "number"
            ? `<div class="csim-compare">
                <div class="card-flat"><div class="xs mono muted">TU PREDICCIÓN</div><strong class="mono">${fmtSI(g.pred, task.unit, 4)}</strong></div>
                <div class="card-flat"><div class="xs mono muted">MEDIDO</div><strong class="mono">${fmtSI(r.measured, task.unit, 4)}</strong></div>
                <div class="card-flat"><div class="xs mono muted">DIFERENCIA</div><strong class="mono">${pct(g.pred, r.measured).toFixed(1)} %</strong></div>
              </div>`
            : `<div class="small">Elegiste: <strong>${esc(task.options[g.pred])}</strong>. Lo que pasó: <strong>${esc(task.options[r.measured])}</strong>.</div>`;
        verdict = `<div class="callout ${cls} small stack-sm"><strong>${head}</strong>${cmp}</div>`;
      } else {
        verdict = `<div class="callout callout-info small">${icon("eye", 14)} Modo exploración: sin predicción no cuenta como práctica. Escribí tu predicción y volvé a simular.</div>`;
      }

      let inst = "";
      if (pr.instrument === "meter") {
        inst = meterHTML(pr.meterReadings(p, r), memory.meterSel[pr.id]);
      } else {
        const scope = pr.scopeFor ? pr.scopeFor(p, r) : { ...r.scope, sim: r.sim };
        inst = scopeHTML(scope);
      }
      resultHTML = `
        <div class="stack-sm">
          <div class="eyebrow" style="margin:0;">${pr.instrument === "meter" ? "Multímetro" : "Osciloscopio"}</div>
          ${inst}
        </div>
        ${verdict}
        <div class="callout callout-info small"><strong>Por qué:</strong> ${pr.explain(p, r)}</div>`;
    }

    body.innerHTML = `
      <div class="stack">
        <div class="card stack-sm">
          <div class="row-between" style="flex-wrap:wrap;gap:8px;">
            <div>
              <div class="eyebrow" style="margin:0;">Simulador guiado · predecir → simular → medir</div>
              <p class="xs muted" style="margin:4px 0 0;">Prácticas del temario de electrónica para robótica. Primero escribís qué esperás; después la simulación hace de banco de pruebas.</p>
            </div>
            <span class="pill ${doneCount === PRACTICES.length ? "pill-green" : ""}">${doneCount}/${PRACTICES.length} logradas</span>
          </div>
          <div class="csim-list">
            ${PRACTICES.map((x) => {
              const pg = memory.progress[x.id];
              return `<button type="button" class="csim-pick ${x.id === pr.id ? "active" : ""}" data-pick="${x.id}">
                <span class="csim-pick-top"><span class="xs mono muted">${esc(x.module)}</span>${
                  pg?.ok ? `<span class="csim-done xs">${icon("check", 13)} lograda</span>` : pg ? `<span class="xs muted">${pg.tries} intento${pg.tries === 1 ? "" : "s"}</span>` : ""
                }</span>
                <span class="csim-pick-title">${esc(x.title)}</span>
              </button>`;
            }).join("")}
          </div>
        </div>

        <div class="grid-2" style="align-items:start;">
          <div class="card stack">
            <div>
              <div class="eyebrow" style="margin:0;">${esc(pr.module)}</div>
              <h2 style="font-size:1.3rem;margin:4px 0;">${esc(pr.title)}</h2>
              <p class="small muted" style="margin:0;">${esc(pr.goal)}</p>
            </div>
            ${pr.schematic(p)}
            <div class="csim-controls">${controlsHTML}</div>
            <ol class="csim-steps small">${pr.steps.map((s) => `<li>${s}</li>`).join("")}</ol>
          </div>

          <div class="card stack">
            <div class="stack-sm">
              <div class="eyebrow" style="margin:0;">1 · Tu predicción</div>
              <div class="small">${esc(task.prompt)}</div>
              ${predictHTML}
            </div>
            <div class="row" style="gap:8px;flex-wrap:wrap;">
              <button type="button" class="btn btn-primary" id="csim-run">${icon("play", 14)} Simular y medir</button>
              ${st.result ? `<button type="button" class="btn btn-ghost btn-sm" id="csim-reset">${icon("refresh", 14)} Valores iniciales</button>` : ""}
            </div>
            ${resultHTML}
          </div>
        </div>
      </div>`;

    // practice picker
    body.querySelectorAll("[data-pick]").forEach((b) =>
      b.addEventListener("click", () => {
        memory.active = b.dataset.pick;
        paint();
      })
    );

    // parameter controls: changing the circuit invalidates the last measurement
    const invalidate = () => { st.result = null; st.graded = null; };
    body.querySelectorAll("select[data-key]").forEach((el) =>
      el.addEventListener("change", () => {
        const c = pr.controls.find((x) => x.key === el.dataset.key);
        p[c.key] = c.options[Number(el.value)];
        invalidate();
        paint();
      })
    );
    body.querySelectorAll("input[type=checkbox][data-key]").forEach((el) =>
      el.addEventListener("change", () => {
        p[el.dataset.key] = el.checked;
        invalidate();
        paint();
      })
    );
    body.querySelectorAll("input[type=range][data-key]").forEach((el) => {
      el.addEventListener("input", () => {
        const c = pr.controls.find((x) => x.key === el.dataset.key);
        p[c.key] = Number(el.value);
        el.closest(".field").querySelector("strong").textContent = c.fmt(p[c.key]);
      });
      el.addEventListener("change", () => { invalidate(); paint(); });
    });
    body.querySelectorAll("[data-seg]").forEach((el) =>
      el.addEventListener("click", () => {
        const c = pr.controls.find((x) => x.key === el.dataset.seg);
        p[c.key] = el.dataset.val;
        // view switches keep the grade, they only need the extra simulation
        if (c.live && st.result) {
          try {
            const r = pr.run(p);
            st.result = r;
          } catch (err) {
            toast(err.message, "err");
          }
        } else {
          invalidate();
        }
        paint();
      })
    );

    // prediction inputs
    const predInput = body.querySelector("#csim-pred");
    if (predInput) {
      predInput.addEventListener("input", () => { st.prediction = predInput.value; });
      predInput.addEventListener("keydown", (e) => { if (e.key === "Enter") body.querySelector("#csim-run").click(); });
    }
    body.querySelectorAll("input[name=csim-choice]").forEach((el) =>
      el.addEventListener("change", () => { st.choice = Number(el.value); })
    );

    // meter selector
    body.querySelectorAll("[data-meter]").forEach((b) =>
      b.addEventListener("click", () => {
        memory.meterSel[pr.id] = b.dataset.meter;
        paint();
      })
    );

    body.querySelector("#csim-reset")?.addEventListener("click", () => {
      memory.perPractice[pr.id] = null;
      paint();
    });

    body.querySelector("#csim-run").addEventListener("click", async () => {
      // parse the prediction before simulating: predicting first is the point
      let pred = null;
      if (task.kind === "number" && st.prediction.trim()) {
        pred = parseSI(st.prediction.replace(new RegExp(`${task.unit}$`), "").trim());
        if (!Number.isFinite(pred)) {
          toast(`No entendí «${st.prediction}». Probá con un número, por ejemplo 4.5 o 470m.`, "err");
          return;
        }
      } else if (task.kind === "choice" && st.choice != null) {
        pred = st.choice;
      }
      const btn = body.querySelector("#csim-run");
      btn.disabled = true;
      btn.innerHTML = `${icon("activity", 14)} Simulando…`;
      // let the button repaint before the (synchronous) simulation runs
      await new Promise((res) => setTimeout(res, 20));
      let r;
      try {
        r = pr.run(p);
      } catch (err) {
        toast(`La simulación falló: ${err.message}`, "err");
        btn.disabled = false;
        paint();
        return;
      }
      st.result = r;
      if (pred == null || r.measured == null) {
        st.graded = null;
      } else {
        const ok = task.kind === "number" ? within(pred, r.measured, task.tol) : pred === r.measured;
        st.graded = { ok, pred };
        const firstOk = ok && !memory.progress[pr.id]?.ok;
        await saveProgress(pr, ok);
        if (firstOk) toast("Práctica lograda", "ok");
      }
      paint();
    });

    if (st.result && pr.instrument === "scope") {
      const scope = pr.scopeFor ? pr.scopeFor(p, st.result) : { ...st.result.scope, sim: st.result.sim };
      wireScope(body, scope);
    }
  };

  paint();
}

export const CIRCUIT_PRACTICES = PRACTICES.map(({ id, module, title }) => ({ id, module, title }));
