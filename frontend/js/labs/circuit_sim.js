/**
 * Small transient circuit simulator (modified nodal analysis).
 *
 * Built for guided labs with fixed circuits, not as a general SPICE:
 * resistors, capacitors, inductors, voltage sources (DC, PWM, sine),
 * current sources, diodes (with optional reverse breakdown) and
 * time-controlled switches. Pure module with no DOM access.
 *
 * Circuit format:
 *   {
 *     nodes: ["vin", "out"],          // "0" / "gnd" is ground and is implicit
 *     elements: [
 *       { type: "V", name: "V1", a: "vin", b: "0", dc: 5 },
 *       { type: "V", name: "V2", a: "x", b: "0", wave: { kind: "pwm", high: 5, low: 0, freq: 1000, duty: 0.5 } },
 *       { type: "R", name: "R1", a: "vin", b: "out", value: 1000 },
 *       { type: "C", name: "C1", a: "out", b: "0", value: 1e-6, ic: 0 },
 *       { type: "L", name: "L1", a: "x", b: "y", value: 0.1, ic: 0 },
 *       { type: "D", name: "D1", a: "anode", b: "cathode", is: 1e-12, n: 1.8, bv: 60 },
 *       { type: "S", name: "S1", a: "x", b: "0", ron: 0.05, roff: 1e9, on: (t) => t > 1e-3 },
 *       { type: "I", name: "I1", a: "x", b: "0", dc: 0.001 },   // current flows a -> b inside the source
 *     ],
 *   }
 *
 * Currents are reported as flowing from `a` to `b` through the element.
 */

const GROUND = new Set(["0", "gnd", "GND"]);
const VT = 0.025852; // thermal voltage at ~300 K
const INIT_G = 1e6; // S, pins capacitors at t = 0
const INIT_R = 1e9; // Ω, pins inductor currents at t = 0

/* ------------------------------------------------------------------ */
/* Sources                                                              */
/* ------------------------------------------------------------------ */

export function sourceValue(el, t) {
  const w = el.wave;
  if (!w) return el.dc ?? 0;
  if (w.kind === "pwm" || w.kind === "pulse") {
    const period = 1 / w.freq;
    const delay = w.delay ?? 0;
    if (t < delay) return w.low ?? 0;
    const phase = ((t - delay) % period) / period;
    return phase < (w.duty ?? 0.5) ? w.high : (w.low ?? 0);
  }
  if (w.kind === "step") {
    return t >= (w.at ?? 0) ? w.high : (w.low ?? 0);
  }
  if (w.kind === "sine") {
    return (w.offset ?? 0) + w.amp * Math.sin(2 * Math.PI * w.freq * t + (w.phase ?? 0));
  }
  return el.dc ?? 0;
}

/* ------------------------------------------------------------------ */
/* Dense linear solver (Gaussian elimination, partial pivoting)          */
/* ------------------------------------------------------------------ */

function solveLinear(A, z) {
  const n = z.length;
  const M = A.map((row, i) => {
    const r = row.slice();
    r.push(z[i]);
    return r;
  });
  for (let col = 0; col < n; col++) {
    let piv = col;
    let best = Math.abs(M[col][col]);
    for (let r = col + 1; r < n; r++) {
      const v = Math.abs(M[r][col]);
      if (v > best) { best = v; piv = r; }
    }
    if (best < 1e-18) throw new Error("Circuito singular: revisá que todos los nodos tengan un camino a masa.");
    if (piv !== col) { const tmp = M[col]; M[col] = M[piv]; M[piv] = tmp; }
    const p = M[col][col];
    for (let r = col + 1; r < n; r++) {
      const f = M[r][col] / p;
      if (f === 0) continue;
      const Mr = M[r];
      const Mc = M[col];
      for (let c = col; c <= n; c++) Mr[c] -= f * Mc[c];
    }
  }
  const x = new Array(n).fill(0);
  for (let r = n - 1; r >= 0; r--) {
    let s = M[r][n];
    for (let c = r + 1; c < n; c++) s -= M[r][c] * x[c];
    x[r] = s / M[r][r];
  }
  return x;
}

/* ------------------------------------------------------------------ */
/* Diode model                                                         */
/* ------------------------------------------------------------------ */

function diodeParams(el) {
  return { is: el.is ?? 1e-12, nvt: (el.n ?? 1.8) * VT, bv: el.bv ?? null, gmin: 1e-12 };
}

/** Current and conductance of a diode at voltage vd (anode - cathode). */
function diodeEval(p, vd) {
  const lim = 40; // cap exponent to avoid overflow; Newton limiting keeps us near the knee
  const xf = Math.min(vd / p.nvt, lim);
  const ef = Math.exp(xf);
  let id = p.is * (ef - 1);
  let gd = (p.is / p.nvt) * ef;
  if (vd / p.nvt > lim) {
    // linear continuation beyond the cap
    id += gd * (vd - lim * p.nvt);
  }
  if (p.bv != null) {
    const xr = Math.min((-vd - p.bv) / p.nvt, lim);
    const er = Math.exp(xr);
    let ir = p.is * er;
    const gr = (p.is / p.nvt) * er;
    if ((-vd - p.bv) / p.nvt > lim) ir += gr * (-vd - p.bv - lim * p.nvt);
    id -= ir;
    gd += gr;
  }
  return { id: id + p.gmin * vd, gd: gd + p.gmin };
}

/** SPICE-style junction voltage limiting to keep Newton stable. */
function limitJunction(vnew, vold, p) {
  const vcrit = p.nvt * Math.log(p.nvt / (Math.SQRT2 * p.is));
  if (vnew > vcrit && Math.abs(vnew - vold) > 2 * p.nvt) {
    if (vold > 0) {
      const arg = 1 + (vnew - vold) / p.nvt;
      vnew = arg > 0 ? vold + p.nvt * Math.log(arg) : vcrit;
    } else {
      vnew = p.nvt * Math.log(vnew / p.nvt);
    }
  }
  if (p.bv != null) {
    // mirror limiting for the breakdown branch
    const vr = -vnew - p.bv;
    const vrOld = -vold - p.bv;
    if (vr > vcrit && Math.abs(vr - vrOld) > 2 * p.nvt) {
      let lim;
      if (vrOld > 0) {
        const arg = 1 + (vr - vrOld) / p.nvt;
        lim = arg > 0 ? vrOld + p.nvt * Math.log(arg) : vcrit;
      } else {
        lim = p.nvt * Math.log(vr / p.nvt);
      }
      vnew = -(lim + p.bv);
    }
  }
  return vnew;
}

/* ------------------------------------------------------------------ */
/* Simulator                                                           */
/* ------------------------------------------------------------------ */

/**
 * Incremental transient solver: build once, then call step() as many times as
 * needed. Element values (R value, I/V dc, S on) may be changed between steps;
 * call kick() after an abrupt change so the next steps use backward Euler.
 * @param {object} circuit
 * @param {object} opts { dt, maxIter? }
 */
export function createStepper(circuit, opts) {
  const { dt } = opts;
  const maxIter = opts.maxIter ?? 80;

  const nodeIndex = new Map();
  for (const n of circuit.nodes) if (!GROUND.has(n)) nodeIndex.set(n, nodeIndex.size);
  const idx = (n) => (GROUND.has(n) ? -1 : nodeIndex.get(n));
  for (const el of circuit.elements) {
    for (const k of ["a", "b"]) {
      if (!GROUND.has(el[k]) && !nodeIndex.has(el[k])) {
        throw new Error(`El elemento ${el.name} usa un nodo no declarado: ${el[k]}`);
      }
    }
  }

  // Voltage sources and inductors get an extra branch-current unknown.
  const branchOf = new Map();
  let nUnknowns = nodeIndex.size;
  for (const el of circuit.elements) {
    if (el.type === "V" || el.type === "L") branchOf.set(el, nUnknowns++);
  }

  // State
  const state = new Map(); // per element: capacitor voltage / inductor current
  for (const el of circuit.elements) {
    if (el.type === "C") state.set(el, { v: el.ic ?? 0, v2: el.ic ?? 0, i: 0 });
    if (el.type === "L") state.set(el, { i: el.ic ?? 0, i2: el.ic ?? 0, v: 0 });
  }

  const nodeV = (x, n) => { const k = idx(n); return k < 0 ? 0 : x[k]; };
  const switchOn = (el, t) => (typeof el.on === "function" ? el.on(t) : !!el.on);

  const stamp = (A, z, el, t, x, method) => {
    const ia = idx(el.a);
    const ib = idx(el.b);
    const g2 = (g) => {
      if (ia >= 0) A[ia][ia] += g;
      if (ib >= 0) A[ib][ib] += g;
      if (ia >= 0 && ib >= 0) { A[ia][ib] -= g; A[ib][ia] -= g; }
    };
    const iInj = (cur) => {
      // current `cur` flows from a to b through the element => leaves node a, enters node b
      if (ia >= 0) z[ia] -= cur;
      if (ib >= 0) z[ib] += cur;
    };
    switch (el.type) {
      case "R":
        g2(1 / el.value);
        break;
      case "S":
        g2(1 / (switchOn(el, t) ? (el.ron ?? 0.05) : (el.roff ?? 1e9)));
        break;
      case "C": {
        const s = state.get(el);
        if (method === "dc") { g2(1e-12); break; }
        // Companion model i = geq*v - ieq.
        //   BE:   i = C/dt * (v - v1)
        //   BDF2: i = C/dt * (1.5 v - 2 v1 + 0.5 v2)   (2nd order and L-stable: no ringing on stiff circuits)
        // "init" pins the capacitor at its initial voltage with a stiff conductance.
        let geq;
        let ieq;
        if (method === "init") { geq = INIT_G; ieq = geq * s.v; }
        else if (method === "be") { geq = el.value / dt; ieq = geq * s.v; }
        else { geq = (1.5 * el.value) / dt; ieq = (el.value / dt) * (2 * s.v - 0.5 * s.v2); }
        g2(geq);
        iInj(-ieq);
        break;
      }
      case "L": {
        const s = state.get(el);
        const k = branchOf.get(el);
        // KCL: branch current leaves a, enters b
        if (ia >= 0) { A[ia][k] += 1; A[k][ia] += 1; }
        if (ib >= 0) { A[ib][k] -= 1; A[k][ib] -= 1; }
        if (method === "dc") {
          A[k][k] -= 1e-9; // tiny series resistance: short circuit at DC
          break;
        }
        // v = req*i - veq  (BE: L/dt*(i - i1); BDF2: L/dt*(1.5 i - 2 i1 + 0.5 i2))
        // "init" pins the inductor at its initial current with a stiff series resistance.
        let req;
        let veq;
        if (method === "init") { req = INIT_R; veq = req * s.i; }
        else if (method === "be") { req = el.value / dt; veq = req * s.i; }
        else { req = (1.5 * el.value) / dt; veq = (el.value / dt) * (2 * s.i - 0.5 * s.i2); }
        A[k][k] -= req;
        z[k] -= veq;
        break;
      }
      case "V": {
        const k = branchOf.get(el);
        if (ia >= 0) { A[ia][k] += 1; A[k][ia] += 1; }
        if (ib >= 0) { A[ib][k] -= 1; A[k][ib] -= 1; }
        z[k] += sourceValue(el, t);
        break;
      }
      case "I":
        iInj(sourceValue(el, t));
        break;
      case "D": {
        const p = diodeParams(el);
        const vd = nodeV(x, el.a) - nodeV(x, el.b);
        const { id, gd } = diodeEval(p, vd);
        g2(gd);
        iInj(id - gd * vd);
        break;
      }
      default:
        throw new Error(`Tipo de elemento desconocido: ${el.type}`);
    }
  };

  const hasNonlinear = circuit.elements.some((e) => e.type === "D");

  const solveAt = (t, method, guess) => {
    let x = guess ? guess.slice() : new Array(nUnknowns).fill(0);
    for (let iter = 0; iter < (hasNonlinear ? maxIter : 1); iter++) {
      const A = Array.from({ length: nUnknowns }, () => new Array(nUnknowns).fill(0));
      const z = new Array(nUnknowns).fill(0);
      // tiny conductance to ground keeps floating nodes solvable
      for (let k = 0; k < nodeIndex.size; k++) A[k][k] += 1e-12;
      for (const el of circuit.elements) stamp(A, z, el, t, x, method);
      const xn = solveLinear(A, z);
      if (!hasNonlinear) return xn;
      // junction limiting
      let converged = true;
      for (const el of circuit.elements) {
        if (el.type !== "D") continue;
        const p = diodeParams(el);
        const vOld = nodeV(x, el.a) - nodeV(x, el.b);
        const vNew = nodeV(xn, el.a) - nodeV(xn, el.b);
        const vLim = limitJunction(vNew, vOld, p);
        if (Math.abs(vNew - vOld) > 1e-6 + 1e-4 * Math.abs(vNew)) converged = false;
        if (vLim !== vNew) {
          converged = false;
          // nudge the anode side so the next linearization point is the limited voltage
          const ka = idx(el.a);
          const kb = idx(el.b);
          if (ka >= 0) xn[ka] = (kb >= 0 ? xn[kb] : 0) + vLim;
          else if (kb >= 0) xn[kb] = -vLim;
        }
      }
      x = xn;
      if (converged && iter > 0) return x;
    }
    return x; // best effort
  };

  const elementCurrent = (el, x, t) => {
    const va = nodeV(x, el.a);
    const vb = nodeV(x, el.b);
    switch (el.type) {
      case "R": return (va - vb) / el.value;
      case "S": return (va - vb) / (switchOn(el, t) ? (el.ron ?? 0.05) : (el.roff ?? 1e9));
      case "V":
      case "L": return x[branchOf.get(el)];
      case "I": return sourceValue(el, t);
      case "D": return diodeEval(diodeParams(el), va - vb).id;
      case "C": return state.get(el).i;
      default: return 0;
    }
  };

  const updateState = (x, method) => {
    for (const el of circuit.elements) {
      if (el.type === "C") {
        const s = state.get(el);
        const v = nodeV(x, el.a) - nodeV(x, el.b);
        const i = method === "be"
          ? (el.value / dt) * (v - s.v)
          : (el.value / dt) * (1.5 * v - 2 * s.v + 0.5 * s.v2);
        s.v2 = s.v;
        s.v = v;
        s.i = i;
      } else if (el.type === "L") {
        const s = state.get(el);
        s.i2 = s.i;
        s.i = x[branchOf.get(el)];
        s.v = nodeV(x, el.a) - nodeV(x, el.b);
      }
    }
  };

  // Initial point: capacitors and inductors are pinned at their initial
  // conditions, which also gives the starting currents/voltages for reporting.
  let x = solveAt(0, "init", null);
  for (const el of circuit.elements) {
    if (el.type === "C") {
      const s = state.get(el);
      s.i = INIT_G * (nodeV(x, el.a) - nodeV(x, el.b) - s.v);
      s.v2 = s.v;
    }
    if (el.type === "L") {
      const s = state.get(el);
      s.i2 = s.i;
      s.v = nodeV(x, el.a) - nodeV(x, el.b);
    }
  }

  // BDF2 needs two points of clean history: after any discontinuity (a switch
  // or a stepped source changing) use backward Euler for two steps, like SPICE.
  let beSteps = 2;
  const edgy = circuit.elements.filter((e) => e.type === "S" || (e.type === "V" && e.wave && e.wave.kind !== "sine"));
  const switchState = (tt) => edgy.map((e) => (e.type === "S" ? switchOn(e, tt) : sourceValue(e, tt))).join("|");
  let lastSig = switchState(0);
  let n = 0;
  let t = 0;

  return {
    get t() { return t; },
    dt,
    step() {
      n += 1;
      t = n * dt;
      const sig = switchState(t);
      if (sig !== lastSig) { beSteps = 2; lastSig = sig; }
      const method = beSteps > 0 ? "be" : "bdf2";
      if (beSteps > 0) beSteps--;
      x = solveAt(t, method, x);
      updateState(x, method);
    },
    /** Signal an abrupt change made from outside (element values edited). */
    kick() { beSteps = 2; },
    /**
     * Re-solve the present instant after editing element values, without
     * advancing time: capacitors keep their voltage, inductors their current,
     * and resistive nodes settle immediately (like a real pull-up does).
     */
    refresh() {
      x = solveAt(t, "init", x);
      beSteps = 2;
    },
    v(node) { return nodeV(x, node); },
    i(el) { return elementCurrent(el, x, t); },
    nodes: [...nodeIndex.keys()],
  };
}

/**
 * Run a transient simulation.
 * @param {object} circuit
 * @param {object} opts { tStop, dt, record?: max points kept, recordFrom?: seconds, maxIter? }
 * @returns {{ t: number[], v: Record<string, number[]>, i: Record<string, number[]> }}
 */
export function simulate(circuit, opts) {
  const { tStop, dt } = opts;
  const maxPoints = opts.record ?? 2000;
  const recordFrom = opts.recordFrom ?? 0; // keep only samples with t >= recordFrom
  const st = createStepper(circuit, { dt, maxIter: opts.maxIter });

  const steps = Math.max(1, Math.ceil(tStop / dt));
  const firstRecorded = Math.min(steps, Math.max(0, Math.ceil(recordFrom / dt - 1e-9)));
  const stride = Math.max(1, Math.ceil((steps - firstRecorded) / maxPoints));
  const out = { t: [], v: {}, i: {} };
  for (const nd of st.nodes) out.v[nd] = [];
  for (const el of circuit.elements) out.i[el.name] = [];

  const record = () => {
    out.t.push(st.t);
    for (const nd of st.nodes) out.v[nd].push(st.v(nd));
    for (const el of circuit.elements) out.i[el.name].push(st.i(el));
  };

  if (firstRecorded === 0) record();
  for (let s = 1; s <= steps; s++) {
    st.step();
    if (s >= firstRecorded && ((s - firstRecorded) % stride === 0 || s === steps)) record();
  }
  return out;
}

/** DC operating point: capacitors open, inductors short. */
export function operatingPoint(circuit) {
  const res = simulate(
    {
      ...circuit,
      elements: circuit.elements.map((e) =>
        e.type === "C" ? { ...e, type: "R", value: 1e12 } : e.type === "L" ? { ...e, type: "R", value: 1e-6 } : e
      ),
    },
    { tStop: 1e-9, dt: 1e-9, record: 2 }
  );
  const v = {};
  const i = {};
  for (const n of Object.keys(res.v)) v[n] = res.v[n][res.v[n].length - 1];
  for (const n of Object.keys(res.i)) i[n] = res.i[n][res.i[n].length - 1];
  return { v, i };
}

/* ------------------------------------------------------------------ */
/* Measurement helpers (what an oscilloscope would compute)             */
/* ------------------------------------------------------------------ */

export function stats(arr, from = 0, to = arr.length) {
  let min = Infinity;
  let max = -Infinity;
  let sum = 0;
  for (let k = from; k < to; k++) {
    const v = arr[k];
    if (v < min) min = v;
    if (v > max) max = v;
    sum += v;
  }
  const n = Math.max(1, to - from);
  return { min, max, mean: sum / n, pp: max - min };
}

/** First time the trace crosses `level` going in `dir` (+1 rising, -1 falling), linear interpolation. */
export function crossingTime(t, y, level, dir = 1, fromTime = 0) {
  for (let k = 1; k < t.length; k++) {
    if (t[k] < fromTime) continue;
    const a = y[k - 1] - level;
    const b = y[k] - level;
    if ((dir > 0 && a < 0 && b >= 0) || (dir < 0 && a > 0 && b <= 0)) {
      const f = a / (a - b);
      return t[k - 1] + f * (t[k] - t[k - 1]);
    }
  }
  return null;
}

/** Engineering notation with SI prefix: fmtSI(0.0047, "F") -> "4.7 mF". */
export function fmtSI(value, unit = "", digits = 3) {
  if (value == null || !Number.isFinite(value)) return "—";
  if (value === 0) return `0 ${unit}`.trim();
  const prefixes = [
    [1e9, "G"], [1e6, "M"], [1e3, "k"], [1, ""], [1e-3, "m"], [1e-6, "µ"], [1e-9, "n"], [1e-12, "p"],
  ];
  const abs = Math.abs(value);
  for (const [scale, p] of prefixes) {
    if (abs >= scale * 0.9995) {
      const n = value / scale;
      return `${Number(n.toPrecision(digits))} ${p}${unit}`;
    }
  }
  return `${Number((value / 1e-12).toPrecision(digits))} p${unit}`;
}

/** Parse "4.7k", "100u", "10 ms", "2,2" etc. Returns NaN when it cannot. */
export function parseSI(text) {
  if (text == null) return NaN;
  const s = String(text).trim().replace(",", ".").replace(/\s+/g, "");
  // number, optional SI prefix (case matters: m = milli, M = mega), optional unit
  const m = s.match(/^([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)([GMkKmunpµμ]?)(Ω|ohms?|Hz|hz|[VvAasFfHh])?$/);
  if (!m) return NaN;
  const map = { G: 1e9, M: 1e6, k: 1e3, K: 1e3, "": 1, m: 1e-3, u: 1e-6, "µ": 1e-6, "μ": 1e-6, n: 1e-9, p: 1e-12 };
  return parseFloat(m[1]) * map[m[2]];
}
