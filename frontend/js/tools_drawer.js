import { icon } from "./icons.js";
import { esc } from "./main.js";

/**
 * Reusable in-exercise study tools drawer:
 *   1. Scientific calculator (DEG/RAD, history, safe expression evaluator — no raw eval).
 *   2. Quick unit converter tailored to UNCuyo Physics U1–U5.
 *   3. Touch/mouse drawing scratchpad + text notes persisted per exercise in sessionStorage.
 */

const UNIT_GROUPS = {
  length: {
    label: "Longitud",
    units: {
      m: { name: "m", factor: 1 },
      km: { name: "km", factor: 1000 },
      cm: { name: "cm", factor: 0.01 },
      mm: { name: "mm", factor: 0.001 },
      pulg: { name: "pulg (in)", factor: 0.0254 },
      pie: { name: "pie (ft)", factor: 0.3048 },
    },
    defFrom: "km",
    defTo: "m",
  },
  speed: {
    label: "Velocidad",
    units: {
      ms: { name: "m/s", factor: 1 },
      kmh: { name: "km/h", factor: 1 / 3.6 },
      cms: { name: "cm/s", factor: 0.01 },
      mph: { name: "mi/h", factor: 0.44704 },
    },
    defFrom: "kmh",
    defTo: "ms",
  },
  mass: {
    label: "Masa",
    units: {
      kg: { name: "kg", factor: 1 },
      g: { name: "g", factor: 0.001 },
      mg: { name: "mg", factor: 1e-6 },
      t: { name: "t (ton)", factor: 1000 },
      utm: { name: "u.t.m.", factor: 9.8 },
      lb: { name: "lb", factor: 0.45359237 },
    },
    defFrom: "g",
    defTo: "kg",
  },
  force: {
    label: "Fuerza",
    units: {
      N: { name: "N", factor: 1 },
      kN: { name: "kN", factor: 1000 },
      kgf: { name: "kgf (g=9,8)", factor: 9.8 },
      dyn: { name: "dina", factor: 1e-5 },
      lbf: { name: "lbf", factor: 4.44822 },
    },
    defFrom: "kgf",
    defTo: "N",
  },
  energy: {
    label: "Energía",
    units: {
      J: { name: "J", factor: 1 },
      kJ: { name: "kJ", factor: 1000 },
      cal: { name: "cal", factor: 4.184 },
      kcal: { name: "kcal", factor: 4184 },
      kgm: { name: "kgf·m", factor: 9.8 },
      kWh: { name: "kW·h", factor: 3.6e6 },
    },
    defFrom: "kWh",
    defTo: "J",
  },
  angle: {
    label: "Ángulo",
    units: {
      deg: { name: "grados (°)", factor: Math.PI / 180 },
      rad: { name: "radianes", factor: 1 },
      rev: { name: "vueltas", factor: 2 * Math.PI },
    },
    defFrom: "deg",
    defTo: "rad",
  },
};

/** Safe math expression evaluator supporting +, -, *, /, ^, (), pi, e and trig/log functions. */
export function evaluateMath(expr, degMode = true) {
  let s = String(expr || "")
    .trim()
    .replaceAll(",", ".")
    .replaceAll("−", "-")
    .replaceAll("×", "*")
    .replaceAll("·", "*")
    .replaceAll("÷", "/")
    .replaceAll("π", "pi");
  if (!s) return null;
  // Insert implicit multiplication (e.g. 2pi -> 2*pi, 3sin(30) -> 3*sin(30), 2(3) -> 2*(3)) while keeping 1e-5 intact
  s = s
    .replace(/(\d)(?!e[+-]?\d)(?=[a-zA-Z(])/gi, "$1*")
    .replace(/\)(?=[0-9a-zA-Z(])/g, ")*");
  // Allow only safe math identifiers, scientific notation and operators
  const stripped = s
    .replace(/(\d)e[+-]?\d+/gi, "$1")
    .replace(/\b(sin|sen|cos|tan|tg|asin|acos|atan|sqrt|cbrt|abs|ln|log|exp|pi|e)\b/gi, "");
  if (/[^0-9.+\-*/^()\s]/.test(stripped)) {
    throw new Error("Expresión no válida");
  }
  const toRad = degMode ? Math.PI / 180 : 1;
  const fromRad = degMode ? 180 / Math.PI : 1;
  const scope = {
    sin: (x) => Math.sin(x * toRad),
    sen: (x) => Math.sin(x * toRad),
    cos: (x) => Math.cos(x * toRad),
    tan: (x) => Math.tan(x * toRad),
    tg: (x) => Math.tan(x * toRad),
    asin: (x) => Math.asin(x) * fromRad,
    acos: (x) => Math.acos(x) * fromRad,
    atan: (x) => Math.atan(x) * fromRad,
    sqrt: Math.sqrt,
    cbrt: Math.cbrt,
    abs: Math.abs,
    ln: Math.log,
    log: Math.log10,
    exp: Math.exp,
    pi: Math.PI,
    e: Math.E,
  };
  // Replace ^ with ** and map math identifiers (skipping scientific notation like 1e-5)
  let js = s.replace(/\^/g, "**");
  js = js.replace(/(?<!\d)\b(sin|sen|cos|tan|tg|asin|acos|atan|sqrt|cbrt|abs|ln|log|exp|pi|e)\b/gi, (m) => `scope.${m.toLowerCase()}`);
  // eslint-disable-next-line no-new-func
  const fn = new Function("scope", `"use strict"; return (${js});`);
  const val = fn(scope);
  if (typeof val !== "number" || !Number.isFinite(val)) throw new Error("Resultado indefinido");
  return val;
}

function fmtNum(n) {
  if (n === 0) return "0";
  const a = Math.abs(n);
  if (a >= 1e7 || a < 1e-4) return n.toExponential(4).replace(".", ",");
  return Number(n.toPrecision(8)).toString().replace(".", ",");
}

export function mountStudyTools(host, { storageKey = "default" } = {}) {
  if (!host) return;
  const noteKey = `aprendelab_scratch:${storageKey}`;
  const state = {
    tab: "calc",
    deg: true,
    expr: "",
    result: "",
    history: [],
    unitGroup: "speed",
    unitVal: "90",
    unitFrom: UNIT_GROUPS.speed.defFrom,
    unitTo: UNIT_GROUPS.speed.defTo,
    eraser: false,
    scratchText: (() => {
      try {
        return sessionStorage.getItem(noteKey) || "";
      } catch {
        return "";
      }
    })(),
  };

  function paint() {
    const ug = UNIT_GROUPS[state.unitGroup];
    const numVal = Number(String(state.unitVal).replace(",", "."));
    let converted = "—";
    if (Number.isFinite(numVal) && state.unitVal.trim() !== "") {
      const base = numVal * ug.units[state.unitFrom].factor;
      converted = `${fmtNum(base / ug.units[state.unitTo].factor)} ${ug.units[state.unitTo].name}`;
    }

    host.innerHTML = `
      <div class="tools-panel stack">
        <div class="row-between">
          <div class="segmented" role="tablist" aria-label="Herramientas de cálculo">
            <button type="button" class="seg-btn ${state.tab === "calc" ? "active" : ""}" data-tool-tab="calc">Calculadora</button>
            <button type="button" class="seg-btn ${state.tab === "units" ? "active" : ""}" data-tool-tab="units">Unidades</button>
            <button type="button" class="seg-btn ${state.tab === "pad" ? "active" : ""}" data-tool-tab="pad">Borrador</button>
          </div>
          ${
            state.tab === "calc"
              ? `<button type="button" class="btn btn-secondary btn-sm" id="tool-deg">${state.deg ? "DEG (°)" : "RAD"}</button>`
              : ""
          }
        </div>

        ${
          state.tab === "calc"
            ? `<div class="stack-sm">
                <form id="tool-calc-form" class="row nowrap gap-sm">
                  <input type="text" id="tool-calc-in" class="mono" value="${esc(state.expr)}" placeholder="Ej.: sqrt(3^2 + 4^2) · sin(30) · log(100)" autocomplete="off" />
                  <button type="submit" class="btn btn-primary btn-sm">=</button>
                </form>
                <div class="tool-calc-keys">
                  ${["sin(", "cos(", "tan(", "sqrt(", "log(", "ln(", "^", "pi", "(", ")", "9.8", "C"]
                    .map((k) => `<button type="button" class="btn btn-secondary btn-sm tool-key" data-key="${esc(k)}">${esc(k)}</button>`)
                    .join("")}
                </div>
                ${
                  state.result
                    ? `<div class="callout callout-info row-between">
                        <span class="mono"><strong>${esc(state.result)}</strong></span>
                        <span class="xs muted">${state.deg ? "en grados" : "en radianes"}</span>
                      </div>`
                    : ""
                }
                ${
                  state.history.length
                    ? `<div class="tool-hist">
                        ${state.history
                          .slice(0, 4)
                          .map(
                            (h) =>
                              `<button type="button" class="tool-hist-row" data-reuse="${esc(h.expr)}"><span class="mono xs muted">${esc(h.expr)}</span><span class="mono xs"><strong>= ${esc(h.res)}</strong></span></button>`
                          )
                          .join("")}
                      </div>`
                    : ""
                }
              </div>`
            : state.tab === "units"
            ? `<div class="stack-sm">
                <div class="row gap-sm">
                  ${Object.entries(UNIT_GROUPS)
                    .map(
                      ([k, g]) =>
                        `<button type="button" class="pill tool-ug ${state.unitGroup === k ? "pill-accent" : ""}" data-ug="${k}">${esc(g.label)}</button>`
                    )
                    .join("")}
                </div>
                <div class="tool-unit-grid">
                  <input type="text" id="tool-u-val" inputmode="decimal" value="${esc(state.unitVal)}" aria-label="Valor a convertir" />
                  <select id="tool-u-from" aria-label="Unidad origen">
                    ${Object.entries(ug.units)
                      .map(([k, u]) => `<option value="${k}" ${state.unitFrom === k ? "selected" : ""}>${esc(u.name)}</option>`)
                      .join("")}
                  </select>
                  <button type="button" class="icon-btn" id="tool-u-swap" title="Invertir unidades" aria-label="Invertir">${icon("shuffle", 15)}</button>
                  <select id="tool-u-to" aria-label="Unidad destino">
                    ${Object.entries(ug.units)
                      .map(([k, u]) => `<option value="${k}" ${state.unitTo === k ? "selected" : ""}>${esc(u.name)}</option>`)
                      .join("")}
                  </select>
                </div>
                <div class="callout callout-info mono"><strong>${esc(converted)}</strong></div>
              </div>`
            : `<div class="stack-sm">
                <div class="row-between">
                  <span class="xs muted">Dibujá un DCL, triángulo o cuentas rápidas.</span>
                  <div class="row gap-sm">
                    <button type="button" class="btn btn-sm ${!state.eraser ? "btn-primary" : "btn-secondary"}" id="pad-pen">Lápiz</button>
                    <button type="button" class="btn btn-sm ${state.eraser ? "btn-primary" : "btn-secondary"}" id="pad-erase">Goma</button>
                    <button type="button" class="btn btn-secondary btn-sm" id="pad-clear">Limpiar</button>
                  </div>
                </div>
                <canvas id="tool-pad-canvas" class="tool-pad-canvas" width="640" height="220"></canvas>
                <textarea id="tool-scratch-text" rows="2" placeholder="Anotá pasos intermedios, datos o despejes…">${esc(state.scratchText)}</textarea>
              </div>`
        }
      </div>
    `;

    host.querySelectorAll("[data-tool-tab]").forEach((b) =>
      b.addEventListener("click", () => {
        state.tab = b.dataset.toolTab;
        paint();
      })
    );

    if (state.tab === "calc") {
      const inp = host.querySelector("#tool-calc-in");
      host.querySelector("#tool-deg")?.addEventListener("click", () => {
        state.deg = !state.deg;
        paint();
      });
      host.querySelectorAll(".tool-key").forEach((kBtn) =>
        kBtn.addEventListener("click", () => {
          const k = kBtn.dataset.key;
          if (k === "C") {
            state.expr = "";
            state.result = "";
          } else {
            state.expr += k;
          }
          paint();
          host.querySelector("#tool-calc-in")?.focus();
        })
      );
      host.querySelectorAll("[data-reuse]").forEach((b) =>
        b.addEventListener("click", () => {
          state.expr = b.dataset.reuse;
          paint();
        })
      );
      inp?.addEventListener("input", () => {
        state.expr = inp.value;
      });
      host.querySelector("#tool-calc-form")?.addEventListener("submit", (e) => {
        e.preventDefault();
        try {
          const v = evaluateMath(state.expr, state.deg);
          if (v === null) return;
          state.result = fmtNum(v);
          state.history.unshift({ expr: state.expr, res: state.result });
          state.history = state.history.slice(0, 6);
        } catch (err) {
          state.result = err.message;
        }
        paint();
      });
    } else if (state.tab === "units") {
      host.querySelectorAll("[data-ug]").forEach((b) =>
        b.addEventListener("click", () => {
          state.unitGroup = b.dataset.ug;
          state.unitFrom = UNIT_GROUPS[state.unitGroup].defFrom;
          state.unitTo = UNIT_GROUPS[state.unitGroup].defTo;
          paint();
        })
      );
      host.querySelector("#tool-u-val")?.addEventListener("input", (e) => {
        state.unitVal = e.target.value;
        const n = Number(String(state.unitVal).replace(",", "."));
        const out = host.querySelector(".callout-info strong");
        if (out) {
          if (Number.isFinite(n) && state.unitVal.trim() !== "") {
            const base = n * ug.units[state.unitFrom].factor;
            out.textContent = `${fmtNum(base / ug.units[state.unitTo].factor)} ${ug.units[state.unitTo].name}`;
          } else {
            out.textContent = "—";
          }
        }
      });
      host.querySelector("#tool-u-from")?.addEventListener("change", (e) => {
        state.unitFrom = e.target.value;
        paint();
      });
      host.querySelector("#tool-u-to")?.addEventListener("change", (e) => {
        state.unitTo = e.target.value;
        paint();
      });
      host.querySelector("#tool-u-swap")?.addEventListener("click", () => {
        [state.unitFrom, state.unitTo] = [state.unitTo, state.unitFrom];
        paint();
      });
    } else if (state.tab === "pad") {
      const canvas = host.querySelector("#tool-pad-canvas");
      const ctx = canvas.getContext("2d");
      let drawing = false;
      const pos = (ev) => {
        const rect = canvas.getBoundingClientRect();
        return {
          x: ((ev.clientX - rect.left) / rect.width) * canvas.width,
          y: ((ev.clientY - rect.top) / rect.height) * canvas.height,
        };
      };
      canvas.addEventListener("pointerdown", (ev) => {
        canvas.setPointerCapture(ev.pointerId);
        drawing = true;
        const p = pos(ev);
        ctx.beginPath();
        ctx.moveTo(p.x, p.y);
      });
      canvas.addEventListener("pointermove", (ev) => {
        if (!drawing) return;
        const p = pos(ev);
        ctx.lineCap = "round";
        ctx.lineJoin = "round";
        if (state.eraser) {
          ctx.globalCompositeOperation = "destination-out";
          ctx.lineWidth = 18;
        } else {
          ctx.globalCompositeOperation = "source-over";
          ctx.strokeStyle = getComputedStyle(document.documentElement).getPropertyValue("--text").trim() || "#2b2b29";
          ctx.lineWidth = 2.4;
        }
        ctx.lineTo(p.x, p.y);
        ctx.stroke();
      });
      const endDraw = () => {
        drawing = false;
      };
      canvas.addEventListener("pointerup", endDraw);
      canvas.addEventListener("pointercancel", endDraw);
      host.querySelector("#pad-pen")?.addEventListener("click", () => {
        state.eraser = false;
        paint();
      });
      host.querySelector("#pad-erase")?.addEventListener("click", () => {
        state.eraser = true;
        paint();
      });
      host.querySelector("#pad-clear")?.addEventListener("click", () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      });
      host.querySelector("#tool-scratch-text")?.addEventListener("input", (e) => {
        state.scratchText = e.target.value;
        try {
          sessionStorage.setItem(noteKey, state.scratchText);
        } catch {
          // ignore
        }
      });
    }
  }

  paint();
}
