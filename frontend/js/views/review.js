import { icon, resolveDomainIcon } from "../icons.js";
import { api, esc, rich, labLinkToHash, refreshSidebarDomains, registerCleanup, toast, toneOf } from "../main.js";

/* ---------- Answer checking (cards that grade themselves) ---------- */

export function normalizeAnswer(str) {
  return String(str ?? "")
    .toLowerCase()
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .replace(/[^a-z0-9]/g, "");
}

/** Minus variants become "-", and currency/percent/degree signs are dropped ("-$650" is -650). */
const cleanNumeric = (str) => String(str ?? "").replace(/[−–]/g, "-").replace(/[$%°]/g, "");

function parseNumber(str) {
  const m = cleanNumeric(str)
    .replace(/\s/g, "")
    .replace(",", ".")
    .match(/-?(?:\d+(?:\.\d+)?|\.\d+)(?:\/-?\d+(?:\.\d+)?)?/);
  if (!m) return null;
  if (m[0].includes("/")) {
    const [a, b] = m[0].split("/").map(Number);
    return b ? a / b : null;
  }
  return Number(m[0]);
}

const SUPERSCRIPTS = { "⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁻": "-" };

/**
 * Scientific notation as written in class: "1,23.10³", "1,23 × 10^-3", "2·10⁵", "1.5e4".
 * A power of ten needs "^" or a superscript, so "2.103" is never read as 2 × 10³.
 */
function parseScientific(str) {
  const s = cleanNumeric(str).replace(/\s/g, "").replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]/g, (c) => `§${SUPERSCRIPTS[c]}`);
  let m = s.match(/^(-?\d+(?:[.,]\d+)?)(?:[.·×xX*]|\\cdot)10(?:\^\(?(-?\d+)\)?|((?:§-?)?(?:§\d)+))/);
  if (m) {
    const exp = m[2] !== undefined ? m[2] : m[3].replace(/§/g, "");
    return Number(m[1].replace(",", ".")) * 10 ** Number(exp);
  }
  m = s.match(/^(-?\d+(?:[.,]\d+)?)[eE](-?\d+)(?![\d.,])/);
  return m ? Number(m[1].replace(",", ".")) * 10 ** Number(m[2]) : null;
}

/** "84.000" or "84,000" can be eighty-four thousand written with separators, not a decimal. */
function parseGroupedThousands(str) {
  const s = cleanNumeric(str).replace(/\s/g, "").replace(/^[^\d-]+/, "");
  const m =
    s.match(/^(-?\d{1,3}(?:\.\d{3})+)(?:,(\d+))?(?!\d)/) || s.match(/^(-?\d{1,3}(?:,\d{3})+)(?:\.(\d+))?(?!\d)/);
  if (!m) return null;
  return Number(m[1].replace(/[.,]/g, "") + (m[2] ? `.${m[2]}` : ""));
}

/** "4 1/2" or "4 y 1/2" is a mixed number; read without its space it would be 41/2. */
function parseMixedNumber(str) {
  const m = cleanNumeric(str).trim().match(/^(-?)\s*(\d+)\s+(?:y\s+)?(\d+)\s*\/\s*(\d+)/i);
  if (!m || !Number(m[4])) return null;
  const value = Number(m[2]) + Number(m[3]) / Number(m[4]);
  return m[1] ? -value : value;
}

export function checkAnswer(check, given) {
  if (!check) return null;
  if (check.type === "choice") return given === check.correct;
  if (check.type === "numeric") {
    const target = Number(check.value);
    const tol = Number(check.tolerance || 0);
    const margin = tol > 0 ? Math.max(Math.abs(target) * tol, 1e-9) : 1e-9;
    // Every plausible reading of what was typed is tried: "1.250" is right for 1.25 and for 1250.
    return [parseNumber(given), parseGroupedThousands(given), parseMixedNumber(given), parseScientific(given)].some(
      (x) => x !== null && Math.abs(x - target) <= margin
    );
  }
  if (check.type === "text") {
    // Fractions keep their slash ("1/2" must not match a stray "12") and may come with a
    // unit ("3/8 de taza"); everything else ignores punctuation so "E-A-D-G-B-E" matches "e a d g b e".
    const norm = (v, keepSlash) =>
      keepSlash ? cleanNumeric(v).toLowerCase().replace(/[^a-z0-9/-]/g, "") : normalizeAnswer(v);
    // A mixed number ("1 1/8", "1 y 1/8") is read as its improper fraction ("9/8"), so it
    // neither collapses into "11/8" nor lets the "1/8" inside it pass for the whole answer.
    const mixed = cleanNumeric(given).trim().match(/^(-?)(\d+)\s+(?:y\s+)?(\d+)\s*\/\s*(\d+)(?![\d/])/i);
    const typed = mixed ? `${mixed[1]}${Number(mixed[2]) * Number(mixed[4]) + Number(mixed[3])}/${mixed[4]}` : given;
    const fraction = cleanNumeric(typed).replace(/\s*\/\s*/g, "/").match(/(?:^|[^\d/])(-?\d+\/\d+)(?![\d/])/);
    return (check.accept || []).some((a) => {
      const keep = String(a).includes("/");
      const g = norm(typed, keep);
      if (keep && fraction && /^-?\d+\/\d+$/.test(String(a).trim()) && fraction[1] === String(a).trim()) return true;
      return g.length > 0 && g === norm(a, keep);
    });
  }
  if (check.type === "order") {
    return (given || []).every((line, i) => line === check.lines[i]);
  }
  return null;
}

function shuffled(arr) {
  const out = arr.slice();
  for (let i = out.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [out[i], out[j]] = [out[j], out[i]];
  }
  return out;
}

const CONFIDENCE = [
  { key: "baja", label: "Poco seguro" },
  { key: "media", label: "Algo seguro" },
  { key: "alta", label: "Muy seguro" },
];

const RATINGS = [
  { n: 1, label: "Otra vez", hint: "No me salió" },
  { n: 2, label: "Difícil", hint: "Me costó" },
  { n: 3, label: "Bien", hint: "Me salió" },
  { n: 4, label: "Fácil", hint: "Sin pensar" },
];

function isToday(iso) {
  if (!iso) return false;
  return new Date(iso).toDateString() === new Date().toDateString();
}

/**
 * One practice card. Flow:
 *   1. the learner answers (auto-checked input, or from memory for open cards);
 *   2. says how sure they are — that click is also what reveals/checks the answer,
 *      so the confidence judgement is always recorded and costs no extra step;
 *   3. sees the result and rates how it went (the app suggests a rating when it
 *      has evidence: an auto-checked answer or a lab result from today).
 */
export function renderActiveRecallCard(host, item, options = {}) {
  const {
    phaseLabel = null,
    phaseTip = null,
    isOverlearning = false,
    noSchedule = false,
    isRetry = false,
    onRated = () => {},
  } = options;

  const startedAt = Date.now();
  const check = item.payload?.check || null;
  const labMetric = item.payload?.lab_metric || null;
  const deepLab = labLinkToHash(item.payload?.lab_link);
  const ico = resolveDomainIcon(item.domain_icon, item.domain_slug);
  const tone = toneOf({ guitarra: "guitar", electronica: "electronics", matematicas: "math", fisica: "physics" }[item.domain_slug]);
  const isLeech = (item.lapses || 0) >= 3;
  const requiredReps = isOverlearning ? 3 : Number(item.payload?.overlearning_reps || 0);

  let revealed = false;
  let confidence = "";
  let submitting = false;
  let attemptText = "";
  let inputVal = "";
  let picked = null;
  let cleanReps = 0;
  let verdict = null; // true | false | null (self-graded)
  let labResult = null;
  let firstPaint = true;

  const optionOrder = check?.type === "choice" ? shuffled(check.options.map((_, i) => i)) : [];
  let orderLines = [];
  if (check?.type === "order") {
    orderLines = shuffled(check.lines);
    if (orderLines.every((l, i) => l === check.lines[i]) && orderLines.length > 1) orderLines.reverse();
  }

  if (labMetric?.type) {
    api
      .get(`/api/metrics?type=${encodeURIComponent(labMetric.type)}&limit=1`)
      .then(({ metrics }) => {
        if (metrics[0] && isToday(metrics[0].created_at)) {
          labResult = metrics[0];
          render();
        }
      })
      .catch(() => {});
  }

  const suggestedRating = () => {
    if (verdict === false) return 1;
    if (verdict === true) {
      if (confidence === "baja") return 2;
      const fast = Date.now() - startedAt < 12000;
      return confidence === "alta" && fast && item.reps > 0 ? 4 : 3;
    }
    if (labResult && labMetric) {
      if (labResult.value >= labMetric.easy) return 4;
      if (labResult.value >= labMetric.good) return 3;
      return 2;
    }
    return null;
  };

  const finish = (res) => {
    detachKeys();
    onRated(res);
  };

  const submitRating = async (rating) => {
    if (submitting) return;
    submitting = true;
    const durationSec = Math.max(1, Math.round((Date.now() - startedAt) / 1000));
    try {
      const res = await api.post(`/api/reviews/${item.id}`, {
        rating,
        confidence_before: confidence,
        duration_sec: durationSec,
        feynman_note: attemptText,
      });
      await refreshSidebarDomains();
      if (confidence === "alta" && rating === 1) {
        toast("Estabas muy seguro y no salió: vale la pena mirarlo con calma. Vuelve en un rato.", "info");
      } else if (rating === 1) {
        toast("Vuelve a aparecer en esta sesión.", "info");
      } else {
        toast(`Lo vas a ver de nuevo en ${res.schedule.interval_label}.`, "ok");
      }
      finish({ ...res, rating, confidence, item: { ...item, ...res.item } });
    } catch (err) {
      submitting = false;
      toast(err.message, "err");
    }
  };

  const finishWithoutSchedule = async () => {
    if (submitting) return;
    submitting = true;
    if (cleanReps > 0) {
      api
        .post("/api/metrics", {
          domain_id: item.domain_id,
          node_id: item.node_id,
          metric_type: "clean_reps",
          label: item.title,
          value: cleanReps,
          unit: cleanReps === 1 ? "repetición limpia" : "repeticiones limpias",
        })
        .catch(() => {});
    }
    finish({ rating: null, confidence, item, noSchedule: true, cleanReps });
  };

  const reveal = (conf) => {
    if (revealed) return;
    if (check?.type === "choice" && picked === null) {
      toast("Elegí una opción primero.", "info");
      return;
    }
    if ((check?.type === "numeric" || check?.type === "text") && !inputVal.trim()) {
      toast("Escribí tu respuesta primero.", "info");
      host.querySelector("#answer-input")?.focus();
      return;
    }
    confidence = conf;
    attemptText = host.querySelector("#feynman-input")?.value ?? attemptText;
    if (check) {
      const given = check.type === "choice" ? picked : check.type === "order" ? orderLines : inputVal;
      verdict = checkAnswer(check, given);
    }
    revealed = true;
    render();
    // Focus the suggested action when there is one; never pre-focus a rating the app
    // has no evidence for (Enter would then grade the card by accident).
    const target = host.querySelector(".rating-btn.suggested, #finish-block");
    if (target) target.focus({ preventScroll: true });
    else document.activeElement?.blur?.();
  };

  const allowedRatings = () => {
    if (verdict === false) return [1];
    if (verdict === true) return [2, 3, 4];
    return [1, 2, 3, 4];
  };

  const onKeyDown = (e) => {
    const tag = (document.activeElement?.tagName || "").toLowerCase();
    const typing = tag === "textarea" || tag === "input" || tag === "select";
    const cmd = document.getElementById("cmd-modal");
    if ((cmd && !cmd.hidden) || e.ctrlKey || e.metaKey || e.altKey) return;
    if (!revealed) {
      if (typing) {
        if (e.key === "Enter" && tag === "input") {
          e.preventDefault();
          document.activeElement.blur();
          host.querySelector(".conf-btn")?.focus();
        }
        return;
      }
      if (["1", "2", "3"].includes(e.key)) {
        e.preventDefault();
        reveal(CONFIDENCE[Number(e.key) - 1].key);
      } else if (check?.type === "choice" && /^[a-d]$/i.test(e.key)) {
        const pos = e.key.toLowerCase().charCodeAt(0) - 97;
        if (pos < optionOrder.length) {
          picked = optionOrder[pos];
          render();
        }
      }
      return;
    }
    if (typing) return;
    if (noSchedule) {
      if (e.key === "Enter") {
        e.preventDefault();
        finishWithoutSchedule();
      }
      return;
    }
    const allowed = allowedRatings();
    if (["1", "2", "3", "4"].includes(e.key) && allowed.includes(Number(e.key))) {
      e.preventDefault();
      submitRating(Number(e.key));
    } else if (e.key === "Enter" && tag !== "button" && tag !== "a") {
      const s = suggestedRating();
      if (s) {
        e.preventDefault();
        submitRating(s);
      }
    }
  };
  const detachKeys = () => window.removeEventListener("keydown", onKeyDown);
  window.addEventListener("keydown", onKeyDown);
  registerCleanup(detachKeys);

  const answerInputHtml = () => {
    if (!check) {
      return `
        <label class="field">
          <span>Tu respuesta <span class="muted" style="font-weight:400;">(opcional: escribirla ayuda a no engañarte)</span></span>
          <textarea id="feynman-input" placeholder="Intentá responder de memoria antes de ver la respuesta…">${esc(attemptText)}</textarea>
        </label>`;
    }
    if (check.type === "choice") {
      return `
        <div class="stack-sm" role="radiogroup" aria-label="Opciones">
          ${optionOrder
            .map(
              (optIdx, pos) => `
            <button type="button" role="radio" aria-checked="${picked === optIdx}" class="option-btn ${picked === optIdx ? "picked" : ""}" data-opt="${optIdx}">
              <span class="opt-key">${String.fromCharCode(65 + pos)}</span>
              <span>${rich(check.options[optIdx])}</span>
            </button>`
            )
            .join("")}
        </div>`;
    }
    if (check.type === "numeric" || check.type === "text") {
      return `
        <label class="field">
          <span>Tu respuesta${check.unit && /[a-zA-ZΩ°%$]/.test(check.unit) ? ` (en ${esc(check.unit)})` : ""}</span>
          <input id="answer-input" type="text" class="input-xl" autocomplete="off" autocapitalize="off" spellcheck="false"
            ${check.type === "numeric" ? 'inputmode="decimal"' : ""} value="${esc(inputVal)}" placeholder="${check.type === "numeric" ? "0" : "Escribí acá"}" />
        </label>`;
    }
    if (check.type === "order") {
      return `
        <div class="stack-sm">
          <span class="small muted">Ordená los pasos con las flechas.</span>
          ${orderLines
            .map(
              (line, i) => `
            <div class="order-line">
              <span class="grow">${esc(line)}</span>
              <button type="button" class="mini-btn order-up" data-i="${i}" ${i === 0 ? "disabled" : ""} aria-label="Subir">${icon("arrowUp", 16)}</button>
              <button type="button" class="mini-btn order-down" data-i="${i}" ${i === orderLines.length - 1 ? "disabled" : ""} aria-label="Bajar">${icon("arrowDown", 16)}</button>
            </div>`
            )
            .join("")}
        </div>`;
    }
    return "";
  };

  const resultHtml = () => {
    let yourAnswer = "";
    if (check?.type === "choice") {
      yourAnswer = `
        <div class="stack-sm">
          ${optionOrder
            .map((optIdx, pos) => {
              const cls = optIdx === check.correct ? "right" : optIdx === picked ? "wrong" : "";
              return `
              <button type="button" class="option-btn ${cls}" disabled>
                <span class="opt-key">${String.fromCharCode(65 + pos)}</span>
                <span>${rich(check.options[optIdx])}</span>
              </button>`;
            })
            .join("")}
        </div>`;
    } else if (check?.type === "order") {
      yourAnswer = `
        <div class="stack-sm">
          ${check.lines.map((line) => `<div class="order-line ${verdict ? "right" : ""}"><span class="grow">${esc(line)}</span></div>`).join("")}
        </div>`;
    } else if (check) {
      yourAnswer = `<p class="m-0">Respondiste: <strong>${esc(inputVal)}</strong>${
        verdict === false && check.type === "numeric" ? ` · Correcto: <strong>${esc(String(check.value))}${check.unit ? " " + esc(check.unit) : ""}</strong>` : ""
      }</p>`;
    } else if (attemptText.trim()) {
      yourAnswer = `
        <div class="card-flat stack-sm">
          <span class="xs muted">Lo que escribiste</span>
          <p class="m-0" style="white-space:pre-line;">${esc(attemptText)}</p>
        </div>`;
    }

    const verdictHtml =
      verdict === true
        ? `<div class="verdict ok">${icon("check", 20)} Correcto</div>`
        : verdict === false
        ? `<div class="verdict bad">${icon("x", 20)} ${check?.type === "order" ? "El orden correcto es este" : "No era esa"}</div>`
        : "";

    return `
      ${verdictHtml}
      ${yourAnswer}
      <div class="callout ${verdict === false ? "callout-warn" : "callout-ok"} stack-sm">
        <span class="xs muted">${check ? "Por qué" : "Respuesta"}</span>
        <div class="rich" style="font-size:1.0625rem;">${rich(item.answer)}</div>
      </div>
      ${
        item.last_feynman_note && !check
          ? `<p class="small muted m-0">La vez anterior escribiste: «${esc(item.last_feynman_note)}»</p>`
          : ""
      }`;
  };

  const ratingHtml = () => {
    if (noSchedule) {
      return `
        ${
          requiredReps > 0
            ? `<div class="row-between">
                <div>
                  <strong>Repeticiones limpias: ${cleanReps} de ${requiredReps}</strong>
                  <div class="small muted">Marcá cada vez que te salga sin errores.</div>
                </div>
                <div class="rep-dots">
                  ${Array.from({ length: requiredReps })
                    .map((_, idx) => `<button type="button" class="rep-dot ${idx < cleanReps ? "done" : ""}" data-rep="${idx + 1}" aria-label="Repetición ${idx + 1}">${idx + 1}</button>`)
                    .join("")}
                </div>
              </div>`
            : ""
        }
        <div class="row-between">
          <span class="small muted">Ya calificaste esta tarjeta hoy: este bloque es solo para afirmarla.</span>
          <button id="finish-block" class="btn btn-primary" type="button">Terminar bloque ${icon("arrowRight", 16)}</button>
        </div>`;
    }
    if (verdict === false) {
      return `
        <div class="row-between">
          <span class="small muted">Vuelve a aparecer en esta sesión hasta que salga.</span>
          <button class="btn btn-primary rating-btn-plain" data-rating="1" type="button" id="finish-block">Seguir <kbd class="kbd">Enter</kbd></button>
        </div>`;
    }
    const allowed = allowedRatings();
    const suggested = suggestedRating();
    const previews = item.interval_previews || {};
    return `
      <div class="stack-sm">
        <div class="row-between">
          <strong>¿Cómo te fue?</strong>
          ${
            labResult && labMetric
              ? `<span class="small muted">Hoy en el laboratorio: <strong>${labResult.value} ${esc(labMetric.unit || labResult.unit || "")}</strong> (objetivo ${labMetric.good})</span>`
              : ""
          }
        </div>
        <div class="rating-grid ${allowed.length === 3 ? "cols-3" : ""}">
          ${RATINGS.filter((r) => allowed.includes(r.n))
            .map(
              (r) => `
            <button class="rating-btn rating-${r.n} ${suggested === r.n ? "suggested" : ""}" data-rating="${r.n}" type="button">
              <strong>${r.label} <kbd class="kbd">${r.n}</kbd></strong>
              <span>${r.n === 1 ? "vuelve en esta sesión" : `vuelve en ${esc(previews[r.n] || previews[String(r.n)] || "unos días")}`}</span>
            </button>`
            )
            .join("")}
        </div>
      </div>`;
  };

  function render() {
    const hadFocusInput = document.activeElement?.id === "answer-input";
    host.innerHTML = `
      <article class="card stack-lg" data-tone="${tone}">
        <div class="stack">
          <div class="row-between">
            <div class="row gap-sm">
              <span class="pill pill-tone">${icon(ico, 14)} ${esc(item.domain_name || "Estudio")}</span>
              <span class="small muted">${esc(String(item.node_title || "").replace(/^\d+\.\s*/, ""))}</span>
              ${isRetry ? `<span class="pill pill-amber">Segundo intento</span>` : ""}
              ${isLeech ? `<span class="pill pill-red">Te cuesta: ${item.lapses} olvidos</span>` : ""}
            </div>
            ${
              deepLab
                ? `<a href="${deepLab}" class="btn btn-secondary btn-sm" data-lab-link>${icon("flask", 14)} ${labMetric ? "Hacerlo en el laboratorio" : "Abrir laboratorio"}</a>`
                : ""
            }
          </div>

          ${phaseTip ? `<p class="small muted m-0">${esc(phaseLabel ? phaseLabel + ": " : "")}${esc(phaseTip)}</p>` : ""}

          <h2 class="question-title">${esc(item.payload?.from_lesson ? "De la lección: te había costado" : item.title)}</h2>
          <p class="question-body rich">${rich(item.prompt)}</p>

          ${
            isLeech && !revealed
              ? `<p class="callout callout-warn m-0">Esta tarjeta se te resiste. Probá explicarla con palabras más simples o practicar el paso aislado en el laboratorio.</p>`
              : ""
          }

          ${
            item.hints?.length && !revealed
              ? `<details class="small">
                  <summary style="cursor:pointer;" class="link">Ver ${item.hints.length === 1 ? "una pista" : "pistas"}</summary>
                  <ul style="margin:8px 0 0 20px;padding:0;">${item.hints.map((h) => `<li>${esc(h)}</li>`).join("")}</ul>
                </details>`
              : ""
          }
        </div>

        ${
          !revealed
            ? `
            ${answerInputHtml()}
            <div class="stack-sm">
              <strong>${check ? "¿Qué tan seguro estás?" : "¿Qué tan seguro estás de saberla?"} <span class="muted" style="font-weight:400;">Tu elección ${check ? "comprueba" : "muestra"} la respuesta.</span></strong>
              <div class="rating-grid cols-3">
                ${CONFIDENCE.map(
                  (c, i) => `
                  <button type="button" class="rating-btn conf-btn" data-conf="${c.key}">
                    <strong>${c.label} <kbd class="kbd">${i + 1}</kbd></strong>
                  </button>`
                ).join("")}
              </div>
            </div>`
            : `${resultHtml()}${ratingHtml()}`
        }
      </article>
    `;

    host.querySelectorAll("[data-lab-link]").forEach((a) =>
      a.addEventListener("click", () => {
        try {
          sessionStorage.setItem("aprendelab_return", location.hash || "#/review");
        } catch {
          // ignore
        }
      })
    );
    host.querySelectorAll(".option-btn[data-opt]").forEach((b) =>
      b.addEventListener("click", () => {
        picked = Number(b.dataset.opt);
        render();
      })
    );
    const input = host.querySelector("#answer-input");
    if (input) {
      input.addEventListener("input", () => {
        inputVal = input.value;
      });
      if ((firstPaint && window.matchMedia("(hover: hover)").matches) || hadFocusInput) input.focus({ preventScroll: true });
    }
    host.querySelectorAll(".order-up, .order-down").forEach((b) =>
      b.addEventListener("click", () => {
        const i = Number(b.dataset.i);
        const j = b.classList.contains("order-up") ? i - 1 : i + 1;
        [orderLines[i], orderLines[j]] = [orderLines[j], orderLines[i]];
        render();
      })
    );
    host.querySelectorAll(".conf-btn").forEach((b) => b.addEventListener("click", () => reveal(b.dataset.conf)));
    host.querySelectorAll(".rep-dot").forEach((b) =>
      b.addEventListener("click", () => {
        const idx = Number(b.dataset.rep);
        cleanReps = idx === cleanReps ? idx - 1 : idx;
        render();
      })
    );
    host.querySelectorAll("[data-rating]").forEach((b) => b.addEventListener("click", () => submitRating(Number(b.dataset.rating))));
    if (noSchedule) host.querySelector("#finish-block")?.addEventListener("click", finishWithoutSchedule);
    firstPaint = false;
  }

  render();
  return detachKeys;
}

/** Where a failed card goes back into the queue: a few cards later, so it is recalled, not parroted. */
export function requeuePosition(currentIdx, length) {
  return Math.min(length, currentIdx + 4);
}

export async function renderReview(container, { domain = null, node = null, mode = null } = {}) {
  const domainsRes = await api.get("/api/domains");
  const qs = new URLSearchParams({ limit: "40" });
  if (domain) qs.set("domain", domain);
  if (node) qs.set("node", String(node));
  if (mode === "practice_all") qs.set("mode", "practice_all");
  const { items: fetched, meta } = await api.get(`/api/reviews/due?${qs.toString()}`);

  const queue = fetched.map((it) => ({ item: it, retry: 0 }));
  let idx = 0;
  let done = 0;
  let failedOnce = 0;
  let activeDetach = null;
  const focusedNodeTitle = node && fetched[0]?.node_title ? fetched[0].node_title.replace(/^\d+\.\s*/, "") : null;
  const title = focusedNodeTitle || (mode === "practice_all" ? "Práctica extra" : "Repaso");

  const emptyState = () => {
    if (queue.length) {
      return {
        h: "Listo por hoy",
        p: `Repasaste ${done} ${done === 1 ? "tarjeta" : "tarjetas"}${failedOnce ? ` y ${failedOnce} ${failedOnce === 1 ? "necesitó" : "necesitaron"} un segundo intento` : ""}. Descansar también es parte de aprender.`,
      };
    }
    if (mode === "practice_all") {
      return { h: "Todavía no hay tarjetas para práctica extra", p: "La práctica extra usa tarjetas que ya repasaste alguna vez." };
    }
    if (meta.new_available > 0 && meta.new_remaining_today === 0) {
      return {
        h: "Estás al día",
        p: `Ya viste las ${meta.new_per_day} tarjetas nuevas de hoy y no hay repasos pendientes. Mañana hay más (podés cambiar el ritmo en Ajustes).`,
      };
    }
    if (meta.locked_new > 0 && meta.due_total === 0) {
      return {
        h: "No hay nada para repasar todavía",
        p: "El repaso solo incluye temas que ya aprendiste. Completá una lección y sus tarjetas van a aparecer acá.",
        learn: true,
      };
    }
    return { h: "Estás al día", p: "No hay repasos pendientes." };
  };

  const paint = () => {
    if (activeDetach) {
      activeDetach();
      activeDetach = null;
    }
    const finished = !queue.length || idx >= queue.length;
    const remaining = queue.length - idx;

    container.innerHTML = `
      <div class="focus-column">
        <div class="page-header" style="padding-bottom:20px;">
          <div>
            <h1 class="title-md" style="font-size:clamp(2rem,4vw,3rem);">${esc(title)}</h1>
          </div>
          <div class="row">
            ${node || mode ? `<a href="#/review" class="btn btn-secondary btn-sm">Repaso de hoy</a>` : ""}
            ${
              !node
                ? `<select id="domain-filter" aria-label="Filtrar por materia" style="width:auto;min-width:200px;">
                    <option value="">Todas las materias</option>
                    ${domainsRes.domains
                      .map((d) => `<option value="${esc(d.slug)}" ${domain === d.slug ? "selected" : ""}>${esc(d.name)}</option>`)
                      .join("")}
                  </select>`
                : ""
            }
          </div>
        </div>
        ${
          !finished
            ? `<div class="row-between small muted" style="margin-bottom:10px;">
                <span>${remaining === 1 ? "Queda 1 tarjeta" : `Quedan ${remaining} tarjetas`}</span>
                <span>${done} ${done === 1 ? "hecha" : "hechas"}</span>
              </div>
              <div class="progress-track mb-lg"><div class="progress-fill" style="width:${Math.round((idx / queue.length) * 100)}%;"></div></div>`
            : ""
        }
        <div id="review-stage"></div>
      </div>
    `;

    container.querySelector("#domain-filter")?.addEventListener("change", (e) => {
      const val = e.target.value;
      const params = new URLSearchParams();
      if (val) params.set("domain", val);
      if (mode) params.set("mode", mode);
      location.hash = params.toString() ? `#/review?${params.toString()}` : "#/review";
    });

    const stage = container.querySelector("#review-stage");
    if (finished) {
      const st = emptyState();
      stage.innerHTML = `
        <div class="card-wash stack" style="padding:48px 32px;">
          <h2>${st.h}</h2>
          <p class="lead">${st.p}</p>
          <div class="row">
            ${
              st.learn
                ? `<a href="#/aprender" class="btn btn-primary">Ir a aprender ${icon("arrowRight", 16)}</a>`
                : `<a href="#/" class="btn btn-primary">Volver a Hoy</a>`
            }
            ${mode !== "practice_all" && !st.learn ? `<a href="#/review?mode=practice_all${domain ? "&domain=" + encodeURIComponent(domain) : ""}" class="btn btn-secondary">Práctica extra</a>` : ""}
            <a href="#/labs" class="btn btn-secondary">Laboratorios</a>
          </div>
        </div>`;
      return;
    }

    const entry = queue[idx];
    activeDetach = renderActiveRecallCard(stage, entry.item, {
      isRetry: entry.retry > 0,
      onRated: (res) => {
        if (res.rating === 1 && entry.retry < 3) {
          // Failed cards come back later in this same session until they stick
          if (entry.retry === 0) failedOnce += 1;
          queue.splice(requeuePosition(idx, queue.length), 0, { item: res.item, retry: entry.retry + 1 });
        } else {
          done += 1;
        }
        idx += 1;
        paint();
      },
    });
  };

  paint();
}
