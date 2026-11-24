import { icon } from "../icons.js";
import { api, esc, rich, toast, toneOf, labLinkToHash, registerCleanup } from "../main.js";
import { subjectArt } from "../art.js";
import { mountStudyTools } from "../tools_drawer.js";
import { exerciseDiagram } from "../diagrams.js";
import { checkAnswer } from "./review.js";

/**
 * Exercises & Real Mock Exams:
 *   - Topic practice: hints, step-by-step solutions, error tagging, FSRS card conversion, tools drawer.
 *   - Real Mock Exams: free navigation across problems (1..N), flag for review, deferred grading
 *     until final submission (or timeout), full post-exam review with step-by-step solutions and
 *     per-problem procedure self-evaluation (100% / 50% / 0%) persisted to SQLite.
 *   - Retry Queue (#/ejercicios/reintentos): focused run over failed / solution-assisted problems.
 */

const PROBLEM_LEVELS = { 1: "Básico", 2: "Intermedio", 3: "Tipo examen" };
const PROJECT_LEVELS = { 1: "Corto", 2: "Intermedio", 3: "Desafío" };
const EXAM_SIZE = 8;
const EXAM_MAX_PER_TOPIC = 2;

const ERROR_TAG_LIST = [
  ["planteo", "Planteo"],
  ["calculo", "Álgebra"],
  ["formula", "Fórmula"],
  ["unidades", "Unidades"],
  ["lectura", "Consigna"],
];

const EXAM_PRESETS = {
  matematicas: [
    { id: "p1", label: "Parcial 1 (U0–U3)", units: ["U0", "U1", "U2", "U3"], count: 8, minutes: 60 },
    { id: "p2", label: "Parcial 2 (U4–U7)", units: ["U4", "U5", "U6", "U7"], count: 8, minutes: 60 },
    { id: "global", label: "Global (U0–U7)", units: null, count: 10, minutes: 90 },
  ],
  fisica: [
    { id: "p1", label: "Parcial 1 (U1–U3)", units: ["U1", "U2", "U3"], count: 8, minutes: 60 },
    { id: "p2", label: "Parcial 2 (U4–U5)", units: ["U4", "U5"], count: 8, minutes: 60 },
    { id: "global", label: "Global (U1–U5)", units: null, count: 10, minutes: 90 },
  ],
  "comprension-problemas": [
    { id: "global", label: "Global (U1–U2)", units: null, count: 8, minutes: 60 },
  ],
};

const stripNumber = (title) => String(title || "").replace(/^\d+\.\s*/, "");
const levelLabel = (ex) => (ex.kind === "project" ? PROJECT_LEVELS : PROBLEM_LEVELS)[ex.level] || "";
const noun = (kind, n) => (kind === "project" ? (n === 1 ? "proyecto" : "proyectos") : n === 1 ? "ejercicio" : "ejercicios");
const doneWord = (kind, n) => (kind === "project" ? (n === 1 ? "hecho" : "hechos") : n === 1 ? "resuelto" : "resueltos");

function fmtClock(totalSec) {
  const sec = Math.max(0, Math.floor(totalSec));
  const h = Math.floor(sec / 3600);
  const m = Math.floor((sec % 3600) / 60);
  const s = sec % 60;
  if (h > 0) return `${h}:${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
  return `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
}

function shuffled(arr) {
  const out = arr.slice();
  for (let i = out.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [out[i], out[j]] = [out[j], out[i]];
  }
  return out;
}

const paragraphs = (text) =>
  String(text || "")
    .split(/\n\s*\n/)
    .map((p) => `<p class="rich m-0">${rich(p.trim())}</p>`)
    .join("");

export function renderExamTrendSvg(examsList) {
  const pts = (examsList || []).slice(-10);
  if (pts.length < 2) return "";
  const W = 320;
  const H = 104;
  const padL = 28;
  const padR = 12;
  const padT = 12;
  const padB = 20;
  const plotW = W - padL - padR;
  const plotH = H - padT - padB;
  const xAt = (i) => padL + (pts.length === 1 ? plotW / 2 : (i / (pts.length - 1)) * plotW);
  const yAt = (v) => padT + plotH - (Math.max(0, Math.min(100, v)) / 100) * plotH;
  const y60 = yAt(60);
  const coords = pts.map((p, i) => [xAt(i), yAt(p.effective_score_pct ?? p.score_pct), p]);
  const linePath = coords.map(([x, y], i) => `${i === 0 ? "M" : "L"}${x.toFixed(1)} ${y.toFixed(1)}`).join(" ");
  return `
    <svg class="exam-trend-svg" viewBox="0 0 ${W} ${H}" role="img" aria-label="Evolución de puntajes de simulacros">
      <line x1="${padL}" y1="${y60.toFixed(1)}" x2="${W - padR}" y2="${y60.toFixed(1)}" stroke="var(--ok)" stroke-width="1.2" stroke-dasharray="4 3" opacity="0.7"/>
      <text x="${padL - 4}" y="${(y60 + 3).toFixed(1)}" text-anchor="end" fill="var(--ok)" font-size="9">60%</text>
      <text x="${padL - 4}" y="${padT + 4}" text-anchor="end" fill="var(--text-muted)" font-size="9">100</text>
      <text x="${padL - 4}" y="${H - padB + 3}" text-anchor="end" fill="var(--text-muted)" font-size="9">0</text>
      <path d="${linePath}" fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
      ${coords
        .map(([x, y, p]) => {
          const val = p.effective_score_pct ?? p.score_pct;
          const col = val >= 60 ? "var(--ok)" : "var(--danger)";
          return `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="4" fill="${col}" stroke="var(--bg)" stroke-width="1.5"><title>${esc(p.date || (p.created_at || "").slice(0, 10))}: ${val}%</title></circle>`;
        })
        .join("")}
    </svg>`;
}

/* ---------- Index: one tile per discipline ---------- */

export async function renderExercisesIndex(container) {
  const [{ domains }, retryData] = await Promise.all([
    api.get("/api/exercises"),
    api.get("/api/exercises/retries").catch(() => ({ total: 0, due_count: 0 })),
  ]);

  container.innerHTML = `
    <div class="page-header">
      <div>
        <h1>Ejercicios</h1>
        <p class="muted">Problemas para resolver en papel y proyectos para hacer con las manos, ordenados por tema. El repaso es para no olvidar; esto es para aprender a resolver.</p>
      </div>
      ${
        retryData.total > 0
          ? `<a href="#/ejercicios/reintentos" class="btn btn-primary">${icon("refresh", 16)} Reintentar fallados (${retryData.total})</a>`
          : ""
      }
    </div>
    ${
      domains.length
        ? `<div class="grid-2">
            ${domains
              .map((d) => {
                const tone = toneOf(d.lab_type);
                const pct = d.total ? Math.round((d.solved / d.total) * 100) : 0;
                return `
                <a href="#/ejercicios/${esc(d.slug)}" class="tile" data-tone="${tone}">
                  <div class="tile-art">${subjectArt(d.slug || tone)}</div>
                  <div class="stack-sm">
                    <h2 class="tile-title">${esc(d.name)}</h2>
                    <p class="m-0 muted">${
                      d.kind === "project"
                        ? "Mini proyectos y rutinas para practicar lo de cada tema."
                        : `Problemas de varios pasos con resolución completa, en ${d.topics_with_exercises} temas.`
                    }</p>
                  </div>
                  <div class="stack-sm">
                    <div class="progress-track"><div class="progress-fill" style="width:${pct}%;"></div></div>
                    <div class="tile-foot">
                      <span class="small">${d.solved} de ${d.total} ${doneWord(d.kind, d.total)}</span>
                      ${icon("arrowRight", 20)}
                    </div>
                  </div>
                </a>`;
              })
              .join("")}
          </div>`
        : `<p class="empty">Todavía no hay ejercicios cargados.</p>`
    }
  `;
}

/* ---------- One discipline: topics grouped by section ---------- */

export async function renderExerciseDomain(container, slug) {
  const { domain, topics, totals } = await api.get(`/api/exercises/${encodeURIComponent(slug)}`);
  const kind = topics.every((t) => t.exercises.every((e) => e.kind === "project")) ? "project" : "problem";
  const problems = topics.flatMap((t) => t.exercises).filter((e) => e.kind === "problem");
  const pct = totals.total ? Math.round((totals.solved / totals.total) * 100) : 0;

  const sections = [];
  for (const t of topics) {
    const name = t.section || "";
    let section = sections.find((s) => s.name === name);
    if (!section) sections.push((section = { name, topics: [] }));
    section.topics.push(t);
  }

  const topicRow = (t) => {
    const total = t.exercises.length;
    const levels = [...new Set(t.exercises.map((e) => e.level))].sort();
    const allDone = t.solved === total;
    return `
      <div class="list-row">
        <a class="grow stack-sm ex-row-link" href="#/ejercicios/${esc(domain.slug)}/${esc(t.slug)}">
          <span class="list-title">${esc(stripNumber(t.title))}</span>
          <span class="small muted">${total} ${noun(kind, total)}${
            t.exercises.some((e) => e.source) ? ` (${t.exercises.filter((e) => e.source).length} de las guías oficiales)` : ""
          } · ${
            levels.length > 1 ? `niveles ${levels[0]} a ${levels[levels.length - 1]}` : `nivel ${levels[0]}`
          }</span>
        </a>
        ${t.struggling ? `<a class="pill pill-amber" href="#/learn/${t.node_id}">Repasá la lección</a>` : ""}
        <span class="pill ${allDone ? "pill-green" : ""} tabular">${allDone ? "✓ " : ""}${t.solved} de ${total}</span>
      </div>`;
  };

  container.innerHTML = `
    <div class="page-header">
      <div>
        <div class="breadcrumb"><a href="#/ejercicios">Ejercicios</a> <span>/</span> <span>${esc(domain.name)}</span></div>
        <h1>${esc(domain.name)}</h1>
        <p class="muted">${totals.solved} de ${totals.total} ${doneWord(kind, totals.total)}. Hay ${noun(kind, 2)} en ${totals.topics_with_exercises} de los ${totals.topics_total} temas.</p>
      </div>
      ${
        problems.length >= 4
          ? `<a href="#/ejercicios/${esc(domain.slug)}/simulacro" class="btn btn-primary">${icon("target", 16)} Configurar simulacro</a>`
          : ""
      }
    </div>
    <div class="progress-track" style="margin-bottom:32px;"><div class="progress-fill" style="width:${pct}%;"></div></div>
    <div class="stack-lg">
      ${sections
        .map(
          (s) => `
        <section class="stack">
          ${s.name ? `<h2 class="title-md m-0">${esc(s.name)}</h2>` : ""}
          <div class="card"><div class="list">${s.topics.map(topicRow).join("")}</div></div>
        </section>`
        )
        .join("")}
    </div>
  `;
}

/* ---------- Runner: topic practice, retry queue, or real deferred-grading mock exam ---------- */

function newWorkState(ex) {
  return {
    values: (ex.parts || []).map(() => ""),
    picked: (ex.parts || []).map(() => null),
    order: (ex.parts || []).map((p) => (p.check.type === "choice" ? shuffled(p.check.options.map((_, i) => i)) : [])),
    verdicts: null,
    hintsShown: 0,
    solutionShown: false,
    sawSolution: false,
    ticks: (ex.done_when || []).map(() => false),
    locked: false,
    flagged: false,
    procRating: null, // 1.0 | 0.5 | 0.0 (post-exam procedure self-evaluation)
    errorTag: ex.status?.error_tag || "",
    cardCreated: false,
  };
}

function isExerciseAnswered(ex, w) {
  return (ex.parts || []).every((p, i) => (p.check.type === "choice" ? w.picked[i] !== null : w.values[i].trim() !== ""));
}

async function runExercises(container, { domain, heading, crumbs, exercises, startIndex = 0, exam = false, examOptions = {}, backHash, lessonLink }) {
  let index = Math.min(Math.max(startIndex, 0), exercises.length - 1);
  const work = exercises.map(newWorkState);
  const examResults = exercises.map(() => false);
  let finished = false;
  let savedExamId = null;
  let timedOut = false;
  let toolsOpen = false;
  const toolsNodes = new Map();

  // Timer state for mock exams
  const timeLimitSec = exam ? Number(examOptions.timeLimitSec || 0) : 0;
  const startedAt = Date.now();
  let remainingSec = timeLimitSec;
  let elapsedSec = 0;
  let timerId = null;

  const stopTimer = () => {
    if (timerId) {
      clearInterval(timerId);
      timerId = null;
    }
  };
  registerCleanup(stopTimer);

  const getToolsEl = (exId) => {
    if (!toolsNodes.has(exId)) {
      const el = document.createElement("div");
      mountStudyTools(el, { storageKey: exId });
      toolsNodes.set(exId, el);
    }
    return toolsNodes.get(exId);
  };

  const record = async (ex, body) => {
    try {
      const res = await api.post(`/api/exercises/${encodeURIComponent(ex.id)}/attempts`, body);
      ex.status = res.status;
    } catch (err) {
      toast(`No se pudo guardar el intento: ${err.message}`, "err");
    }
  };

  /** Final exam submission: grade ALL exercises at once, record attempts, save exam & open review. */
  const submitFullExam = async () => {
    if (finished) return;
    stopTimer();
    finished = true;
    elapsedSec = Math.max(1, Math.round((Date.now() - startedAt) / 1000));

    // Grade every exercise at submission time
    const attemptPromises = exercises.map((ex, idx) => {
      const w = work[idx];
      const verdicts = (ex.parts || []).map(
        (p, i) => checkAnswer(p.check, p.check.type === "choice" ? w.picked[i] : w.values[i]) === true
      );
      w.verdicts = verdicts;
      w.locked = true;
      w.solutionShown = true;
      const ok = verdicts.length > 0 && verdicts.every(Boolean);
      examResults[idx] = ok;
      // Default procedure score matches auto-check until learner adjusts it
      w.procRating = ok ? 1.0 : 0.0;
      return record(ex, {
        correct: ok,
        parts_ok: verdicts.filter(Boolean).length,
        saw_solution: false,
      });
    });
    await Promise.all(attemptPromises);

    const right = examResults.filter(Boolean).length;
    const scorePct = Math.round((100 * right) / exercises.length);
    try {
      const res = await api.post("/api/exams", {
        domain_slug: domain.slug,
        mode: examOptions.mode || (examOptions.ingreso ? "ingreso" : "practice"),
        title: heading,
        units: examOptions.unitCodes || [],
        score_pct: scorePct,
        procedure_score_pct: scorePct,
        correct_count: right,
        total_count: exercises.length,
        duration_sec: elapsedSec,
        time_limit_sec: timeLimitSec,
        details: exercises.map((ex, i) => ({
          exercise_id: ex.id,
          topic_slug: ex.topic.slug,
          unit_code: ex.unitCode || "",
          correct: Boolean(examResults[i]),
          procedure_rating: work[i].procRating,
        })),
      });
      savedExamId = res.exam?.id || null;
    } catch (err) {
      toast(`Simulacro corregido, pero no se pudo guardar en el historial: ${err.message}`, "err");
    }
    paint();
  };

  if (exam) {
    timerId = setInterval(() => {
      if (finished) {
        stopTimer();
        return;
      }
      elapsedSec = Math.round((Date.now() - startedAt) / 1000);
      const pill = container.querySelector("#exam-timer-pill");
      const valEl = container.querySelector("#exam-timer-val");
      if (timeLimitSec > 0) {
        remainingSec = Math.max(0, timeLimitSec - elapsedSec);
        if (valEl) valEl.textContent = fmtClock(remainingSec);
        if (pill) {
          pill.classList.toggle("is-warn", remainingSec <= Math.min(600, timeLimitSec * 0.25) && remainingSec > 120);
          pill.classList.toggle("is-urgent", remainingSec <= 120);
        }
        if (remainingSec <= 0) {
          timedOut = true;
          toast("Se cumplió el tiempo: entregamos tu simulacro.", "info");
          submitFullExam();
        }
      } else if (valEl) {
        valEl.textContent = fmtClock(elapsedSec);
      }
    }, 1000);
  }

  const gradePractice = async () => {
    const ex = exercises[index];
    const w = work[index];
    if (!isExerciseAnswered(ex, w)) {
      toast(ex.parts.length > 1 ? "Respondé todos los incisos antes de corregir." : "Escribí tu respuesta antes de corregir.", "info");
      return;
    }
    const verdicts = ex.parts.map((p, i) => checkAnswer(p.check, p.check.type === "choice" ? w.picked[i] : w.values[i]) === true);
    w.verdicts = verdicts;
    const ok = verdicts.every(Boolean);
    if (ok) w.locked = true;
    await record(ex, { correct: ok, parts_ok: verdicts.filter(Boolean).length, saw_solution: w.sawSolution });
    paint();
    container.querySelector(ok ? "#ex-next" : "#ex-form input, #ex-form .option-btn")?.focus({ preventScroll: true });
  };

  const markProjectDone = async () => {
    const ex = exercises[index];
    const w = work[index];
    w.locked = true;
    await record(ex, { correct: true, parts_ok: ex.done_when.length, saw_solution: false });
    toast("Proyecto registrado como hecho.", "ok");
    paint();
  };

  const partHtml = (ex, w, p, i) => {
    const verdict = !exam && w.verdicts ? w.verdicts[i] : null;
    const badge =
      verdict === null
        ? ""
        : verdict
        ? `<span class="pill pill-green">Correcto</span>`
        : `<span class="pill pill-red">No coincide</span>`;
    const reveal = !exam && w.solutionShown ? `<p class="small m-0"><strong>Respuesta:</strong> <span class="rich">${rich(p.answer)}</span></p>` : "";
    const body =
      p.check.type === "choice"
        ? `<div class="stack-sm" role="group" aria-label="Opciones">
            ${w.order[i]
              .map((optIdx, pos) => {
                const picked = w.picked[i] === optIdx;
                const cls = picked ? (verdict === null ? "picked" : verdict ? "right" : "wrong") : "";
                return `
                <button type="button" class="option-btn ex-opt ${cls}" data-part="${i}" data-opt="${optIdx}" aria-pressed="${picked}" ${w.locked ? "disabled" : ""}>
                  <span class="opt-key">${String.fromCharCode(65 + pos)}</span>
                  <span class="rich">${rich(p.check.options[optIdx])}</span>
                </button>`;
              })
              .join("")}
          </div>`
        : `<label class="field">
            <span>Tu respuesta${p.check.unit ? ` (en ${esc(p.check.unit)})` : ""}</span>
            <input type="text" class="ex-input" data-part="${i}" value="${esc(w.values[i])}" autocomplete="off" autocapitalize="off" spellcheck="false" inputmode="${p.check.type === "numeric" ? "decimal" : "text"}" ${w.locked ? "disabled" : ""} />
          </label>`;
    return `
      <div class="ex-part stack-sm">
        <div class="row-between row-top">
          <p class="rich m-0 ex-prompt">${rich(p.prompt)}</p>
          ${badge}
        </div>
        ${body}
        ${reveal}
      </div>`;
  };

  const problemHtml = (ex, w) => {
    const solved = !exam && w.verdicts && w.verdicts.every(Boolean);
    const graded = !exam && Boolean(w.verdicts);
    const isLast = index === exercises.length - 1;
    const isFirst = index === 0;
    const diagram = exerciseDiagram(ex);
    const showDiagnosticBar = !exam && ((graded && !solved) || (w.solutionShown && !solved));

    if (exam) {
      const answeredCount = exercises.filter((e, i) => isExerciseAnswered(e, work[i])).length;
      return `
        <form id="ex-form" class="stack-lg" novalidate>
          <div class="stack">${paragraphs(ex.statement)}</div>
          ${diagram}
          <div class="stack-lg">${ex.parts.map((p, i) => partHtml(ex, w, p, i)).join("")}</div>

          <div class="row-between" style="padding-top:8px;border-top:1px solid var(--border);">
            <div class="row gap-sm">
              ${!isFirst ? `<button type="button" class="btn btn-secondary" id="ex-prev">${icon("arrowLeft", 15)} Anterior</button>` : ""}
              <button type="button" class="btn ${w.flagged ? "btn-primary" : "btn-secondary"} btn-sm" id="ex-flag">
                ${w.flagged ? "⚑ Marcado para revisar" : "⚐ Marcar para revisar"}
              </button>
            </div>
            <div class="row gap-sm">
              ${
                !isLast
                  ? `<button type="button" class="btn btn-primary" id="ex-next">Siguiente ${icon("arrowRight", 16)}</button>`
                  : `<button type="button" class="btn btn-primary" id="ex-submit-final">${icon("check", 16)} Entregar simulacro (${answeredCount}/${exercises.length})</button>`
              }
            </div>
          </div>
          <p class="xs muted m-0">Podés moverte libremente entre los ${exercises.length} problemas usando los botones de arriba. Todo se corrige junto al entregar.</p>
        </form>`;
    }

    const nextLabel = isLast ? "Volver a los temas" : "Siguiente ejercicio";
    return `
      <form id="ex-form" class="stack-lg" novalidate>
        <div class="stack">${paragraphs(ex.statement)}</div>
        ${diagram}
        <div class="stack-lg">${ex.parts.map((p, i) => partHtml(ex, w, p, i)).join("")}</div>

        ${
          w.hintsShown
            ? `<div class="callout callout-info stack-sm" role="status">
                ${ex.hints.slice(0, w.hintsShown).map((h, i) => `<p class="m-0 small"><strong>Pista ${i + 1}.</strong> <span class="rich">${rich(h)}</span></p>`).join("")}
              </div>`
            : ""
        }

        ${
          graded
            ? `<p class="callout ${solved ? "callout-ok" : "callout-warn"} m-0" role="status">
                ${
                  solved
                    ? "<strong>Resuelto.</strong> Compará tu procedimiento con la resolución: a veces hay un camino más corto."
                    : `<strong>Todavía no.</strong> ${w.verdicts.filter(Boolean).length} de ${ex.parts.length} ${ex.parts.length === 1 ? "inciso" : "incisos"} bien. Quedó agendado para reintentar automáticamente; revisá las cuentas o mirá la resolución.`
                }
              </p>`
            : ""
        }

        ${
          showDiagnosticBar
            ? `<div class="err-tag-bar">
                <div class="row gap-sm" style="align-items:center;">
                  <span class="xs muted">¿Dónde estuvo el error?</span>
                  ${ERROR_TAG_LIST.map(
                    ([k, lbl]) =>
                      `<button type="button" class="pill ex-err-tag ${w.errorTag === k ? "pill-accent" : ""}" data-tag="${k}">${esc(lbl)}</button>`
                  ).join("")}
                </div>
                <button type="button" class="btn btn-secondary btn-sm" id="ex-to-card" ${w.cardCreated ? "disabled" : ""}>
                  ${w.cardCreated ? `${icon("check", 13)} En tu repaso FSRS` : `${icon("plus", 13)} Pasar a tarjeta FSRS`}
                </button>
              </div>`
            : ""
        }

        <div class="row-between">
          <div class="row">
            ${w.locked ? "" : `<button type="submit" class="btn btn-primary">Corregir</button>`}
            ${w.locked ? `<button type="button" class="btn btn-primary" id="ex-next">${nextLabel} ${icon("arrowRight", 16)}</button>` : ""}
            ${
              !w.locked && w.hintsShown < ex.hints.length
                ? `<button type="button" class="btn btn-secondary" id="ex-hint">${w.hintsShown ? "Otra pista" : "Pedir una pista"} (${w.hintsShown + 1} de ${ex.hints.length})</button>`
                : ""
            }
            ${!w.solutionShown ? `<button type="button" class="btn btn-ghost" id="ex-solution">Ver la resolución</button>` : ""}
            ${!w.locked && !isLast ? `<button type="button" class="btn btn-ghost" id="ex-skip">Saltear</button>` : ""}
          </div>
          <button type="button" class="btn btn-text btn-sm muted" id="ex-report-btn" title="Reportar un error en este ejercicio">${icon("alert", 13)} Reportar</button>
        </div>

        ${
          w.solutionShown
            ? `<div class="card-flat stack">
                <h3 class="m-0">Resolución paso a paso</h3>
                <ol class="ex-steps">${ex.solution.map((s) => `<li class="rich">${rich(s)}</li>`).join("")}</ol>
              </div>`
            : ""
        }
      </form>`;
  };

  const projectHtml = (ex, w) => {
    const done = w.locked || ex.status.solved;
    const allTicked = w.ticks.every(Boolean);
    const lab = labLinkToHash(ex.lab_link);
    const isLast = index === exercises.length - 1;
    return `
      <div class="stack-lg">
        <div class="stack">${paragraphs(ex.statement)}</div>
        <div class="grid-2 ex-project-grid">
          <div class="card-flat stack-sm">
            <h3 class="m-0">Qué necesitás</h3>
            <ul class="ex-list">${ex.materials.map((m) => `<li class="rich">${rich(m)}</li>`).join("")}</ul>
          </div>
          <div class="card-flat stack-sm">
            <h3 class="m-0">Consejos</h3>
            <ul class="ex-list">${ex.hints.map((h) => `<li class="rich">${rich(h)}</li>`).join("")}</ul>
          </div>
        </div>
        <div class="stack-sm">
          <h3 class="m-0">Pasos</h3>
          <ol class="ex-steps">${ex.steps.map((s) => `<li class="rich">${rich(s)}</li>`).join("")}</ol>
        </div>
        <fieldset class="card-flat stack-sm ex-checklist">
          <legend class="ex-legend">Está hecho cuando…</legend>
          ${ex.done_when
            .map(
              (c, i) => `
            <label class="ex-check">
              <input type="checkbox" class="ex-tick" data-tick="${i}" ${w.ticks[i] ? "checked" : ""} ${w.locked ? "disabled" : ""} />
              <span class="rich">${rich(c)}</span>
            </label>`
            )
            .join("")}
        </fieldset>
        ${w.locked ? `<p class="callout callout-ok m-0" role="status"><strong>Hecho.</strong> Quedó registrado.</p>` : ""}
        <div class="row">
          ${w.locked ? "" : `<button type="button" class="btn btn-primary" id="ex-done" ${allTicked ? "" : "disabled"}>${done ? "Registrar de nuevo" : "Marcar como hecho"}</button>`}
          ${w.locked ? `<button type="button" class="btn btn-primary" id="ex-next">${isLast ? "Volver a los temas" : "Siguiente"} ${icon("arrowRight", 16)}</button>` : ""}
          ${lab ? `<a class="btn btn-secondary" href="${lab}">${icon("flask", 16)} Abrir el laboratorio</a>` : ""}
          ${!w.locked && !isLast ? `<button type="button" class="btn btn-ghost" id="ex-skip">Saltear</button>` : ""}
        </div>
        ${!w.locked && !allTicked ? `<p class="small muted m-0">Tildá cada criterio cuando lo hayas comprobado.</p>` : ""}
      </div>`;
  };

  const computeProcedureScore = () => {
    const sum = work.reduce((acc, w) => acc + (w.procRating ?? 0), 0);
    return Math.round((100 * sum) / exercises.length);
  };

  const persistProcedureEval = async () => {
    if (!savedExamId) return;
    const procScore = computeProcedureScore();
    try {
      await api.put(`/api/exams/${savedExamId}`, {
        procedure_score_pct: procScore,
        details: exercises.map((ex, i) => ({
          exercise_id: ex.id,
          topic_slug: ex.topic.slug,
          unit_code: ex.unitCode || "",
          correct: Boolean(examResults[i]),
          procedure_rating: work[i].procRating,
        })),
      });
    } catch {
      // non-fatal
    }
  };

  const summaryHtml = () => {
    const right = examResults.filter(Boolean).length;
    const total = exercises.length;
    const autoScore = Math.round((100 * right) / total);
    const procScore = computeProcedureScore();
    const passed = procScore >= 60;

    // Unit-level score breakdown
    const unitMap = new Map();
    exercises.forEach((ex, i) => {
      const code = ex.unitCode || stripNumber(ex.topic.title);
      const label = ex.unitTitle ? `${ex.unitCode} · ${ex.unitTitle}` : stripNumber(ex.topic.title);
      if (!unitMap.has(code)) unitMap.set(code, { code, label, ok: 0, total: 0 });
      const u = unitMap.get(code);
      u.total += 1;
      if (examResults[i]) u.ok += 1;
    });
    const unitRows = [...unitMap.values()];

    return `
      <section class="band dots page-header" data-tone="${toneOf(domain.lab_type)}">
        <div class="stack-sm">
          <div class="breadcrumb">${crumbs}</div>
          <div class="row gap-sm">
            <span class="pill ${passed ? "pill-green" : "pill-red"}">${passed ? "APROBADO (≥ 60 %)" : "A REFORZAR (< 60 %)"}</span>
            <span class="xs muted tabular">${icon("clock", 13)} ${fmtClock(elapsedSec)}${timeLimitSec ? ` / ${fmtClock(timeLimitSec)}` : ""}</span>
            ${timedOut ? `<span class="pill pill-amber">Tiempo cumplido</span>` : ""}
          </div>
          <h1 class="m-0">Resultado: ${autoScore} / 100 · Procedimiento: ${procScore} / 100</h1>
          <p class="muted m-0">Revisá cada resolución abajo y autoevaluá tu desarrollo en papel (como corrige la cátedra). El puntaje con procedimiento se guarda automáticamente en tu historial.</p>
        </div>
      </section>

      <div class="stack-lg">
        ${
          unitRows.length > 1
            ? `<section class="card stack">
                <h2 class="title-sm m-0">Desglose por unidad / tema</h2>
                <div class="stack-sm">
                  ${unitRows
                    .map((u) => {
                      const pct = Math.round((100 * u.ok) / u.total);
                      const color = pct >= 60 ? "var(--ok)" : "var(--danger)";
                      return `
                      <div class="energy-bar-row" style="grid-template-columns:minmax(140px,220px) 1fr 78px;">
                        <span class="small truncate" title="${esc(u.label)}">${esc(u.label)}</span>
                        <div class="energy-track"><div class="energy-fill" style="width:${pct}%;background:${color};"></div></div>
                        <span class="xs tabular" style="text-align:right;">${u.ok}/${u.total} (${pct}%)</span>
                      </div>`;
                    })
                    .join("")}
                </div>
              </section>`
            : ""
        }

        <section class="stack">
          <div class="row-between">
            <h2 class="title-md m-0">Revisión completa y autoevaluación del procedimiento</h2>
            <a href="#/errores?domain=${esc(domain.slug)}" class="btn btn-text btn-sm">Ir al banco de errores ${icon("arrowRight", 14)}</a>
          </div>
          ${exercises
            .map((ex, i) => {
              const w = work[i];
              const ok = Boolean(examResults[i]);
              return `
              <article class="card stack exam-review-card">
                <div class="row-between row-top">
                  <div class="stack-sm" style="gap:3px;">
                    <span class="xs muted">Ejercicio ${i + 1}${ex.unitCode ? ` · ${esc(ex.unitCode)}` : ""} · ${esc(stripNumber(ex.topic.title))}</span>
                    <h3 class="title-sm m-0">${esc(ex.title)}</h3>
                  </div>
                  <span class="pill ${ok ? "pill-green" : "pill-red"}">${ok ? "Respuesta correcta" : "Respuesta incorrecta"}</span>
                </div>

                <div class="stack-sm small">
                  ${(ex.parts || [])
                    .map((p, pi) => {
                      const given =
                        p.check.type === "choice"
                          ? w.picked[pi] !== null
                            ? p.check.options[w.picked[pi]]
                            : "(sin responder)"
                          : w.values[pi].trim() || "(sin responder)";
                      return `
                      <div class="card-flat stack-sm" style="gap:4px;">
                        <div class="rich"><strong>${rich(p.prompt)}</strong></div>
                        <div>Tu respuesta: <span class="rich">${rich(given)}</span> · Esperada: <strong class="rich">${rich(p.answer)}</strong></div>
                      </div>`;
                    })
                    .join("")}
                </div>

                <details ${ok ? "" : "open"}>
                  <summary class="link small" style="cursor:pointer;">Ver resolución paso a paso</summary>
                  <ol class="ex-steps mt-sm">${(ex.solution || []).map((s) => `<li class="rich">${rich(s)}</li>`).join("")}</ol>
                </details>

                <div class="exam-proc-bar">
                  <span class="xs muted"><strong>Tu procedimiento en papel:</strong></span>
                  <div class="segmented" role="group" aria-label="Autoevaluación de procedimiento">
                    <button type="button" class="seg-btn proc-eval-btn ${w.procRating === 1 ? "active" : ""}" data-idx="${i}" data-val="1">Bien planteado (100%)</button>
                    <button type="button" class="seg-btn proc-eval-btn ${w.procRating === 0.5 ? "active" : ""}" data-idx="${i}" data-val="0.5">Error de cuenta (50%)</button>
                    <button type="button" class="seg-btn proc-eval-btn ${w.procRating === 0 ? "active" : ""}" data-idx="${i}" data-val="0">Mal / sin hacer (0%)</button>
                  </div>
                </div>

                ${
                  !ok
                    ? `<div class="row-between" style="padding-top:6px;border-top:1px solid var(--border);">
                        <div class="row gap-sm">
                          <span class="xs muted">Error:</span>
                          ${ERROR_TAG_LIST.map(
                            ([k, lbl]) =>
                              `<button type="button" class="pill sum-err-tag ${w.errorTag === k ? "pill-accent" : ""}" data-idx="${i}" data-tag="${k}">${esc(lbl)}</button>`
                          ).join("")}
                        </div>
                        <div class="row gap-sm">
                          <button type="button" class="btn btn-secondary btn-sm sum-to-card" data-ex="${esc(ex.id)}" ${w.cardCreated ? "disabled" : ""}>${w.cardCreated ? "En repaso ✓" : `${icon("plus", 13)} A tarjeta FSRS`}</button>
                          <a class="btn btn-secondary btn-sm" href="#/learn/${ex.topic.node_id}">Lección</a>
                        </div>
                      </div>`
                    : ""
                }
              </article>`;
            })
            .join("")}
        </section>

        <div class="row">
          <button type="button" class="btn btn-primary" id="ex-again">Configurar otro simulacro</button>
          <a class="btn btn-secondary" href="${backHash}">Volver</a>
        </div>
      </div>`;
  };

  function paint() {
    if (finished) {
      container.innerHTML = summaryHtml();
      container.querySelector("#ex-again")?.addEventListener("click", () => renderExerciseExam(container, domain.slug, { ingreso: examOptions.ingreso }));
      container.querySelectorAll(".proc-eval-btn").forEach((btn) =>
        btn.addEventListener("click", async () => {
          const i = Number(btn.dataset.idx);
          work[i].procRating = Number(btn.dataset.val);
          await persistProcedureEval();
          paint();
        })
      );
      container.querySelectorAll(".sum-err-tag").forEach((btn) =>
        btn.addEventListener("click", async () => {
          const i = Number(btn.dataset.idx);
          const tag = work[i].errorTag === btn.dataset.tag ? "" : btn.dataset.tag;
          try {
            await api.post(`/api/exercises/${encodeURIComponent(exercises[i].id)}/error-tag`, { error_tag: tag });
            work[i].errorTag = tag;
            toast(tag ? "Error etiquetado" : "Etiqueta quitada", "ok");
            paint();
          } catch (err) {
            toast(err.message, "err");
          }
        })
      );
      container.querySelectorAll(".sum-to-card").forEach((btn) =>
        btn.addEventListener("click", async () => {
          try {
            const res = await api.post(`/api/exercises/${encodeURIComponent(btn.dataset.ex)}/to-card`, {});
            const targetIdx = exercises.findIndex((x) => x.id === btn.dataset.ex);
            if (targetIdx >= 0) work[targetIdx].cardCreated = true;
            toast(res.already_exists ? "Ya estaba en tu repaso FSRS." : "Tarjeta creada para tu repaso FSRS.", "ok");
            paint();
          } catch (err) {
            toast(err.message, "err");
          }
        })
      );
      return;
    }

    const ex = exercises[index];
    const w = work[index];
    const clockDisplay = timeLimitSec > 0 ? fmtClock(remainingSec) : fmtClock(elapsedSec);
    const warnCls =
      timeLimitSec > 0
        ? remainingSec <= 120
          ? "is-urgent"
          : remainingSec <= Math.min(600, timeLimitSec * 0.25)
          ? "is-warn"
          : ""
        : "";
    const answeredCount = exam ? exercises.filter((e, i) => isExerciseAnswered(e, work[i])).length : 0;

    container.innerHTML = `
      <div class="page-header">
        <div>
          <div class="breadcrumb">${crumbs}</div>
          <h1>${esc(heading)}</h1>
        </div>
        <div class="row gap-sm">
          ${
            exam
              ? `<span id="exam-timer-pill" class="pill exam-timer ${warnCls}" title="${timeLimitSec ? "Tiempo restante" : "Tiempo transcurrido"}">${icon("clock", 14)} <span id="exam-timer-val" class="mono">${clockDisplay}</span></span>
                 <button type="button" class="btn btn-primary btn-sm" id="exam-finish-now">Entregar (${answeredCount}/${exercises.length})</button>`
              : ""
          }
          ${
            ex.kind === "problem"
              ? `<button type="button" class="btn ${toolsOpen ? "btn-primary" : "btn-secondary"} btn-sm" id="ex-tools-toggle" aria-expanded="${toolsOpen}">
                  ${icon("sliders", 15)} Herramientas
                </button>`
              : ""
          }
          ${lessonLink ? `<a href="${lessonLink}" class="btn btn-secondary btn-sm">${icon("book", 15)} Ver la lección</a>` : ""}
        </div>
      </div>

      <div class="row ex-pager" role="tablist" aria-label="Ejercicios">
        ${exercises
          .map((e, i) => {
            if (exam) {
              const ans = isExerciseAnswered(e, work[i]);
              const flg = work[i].flagged;
              const state = flg ? "pill-amber" : ans ? "pill-green" : "";
              const mark = flg ? `${i + 1}⚑` : ans ? `${i + 1}●` : i + 1;
              return `<button type="button" role="tab" class="pill ex-jump ${i === index ? "pill-accent ex-current" : state}" data-jump="${i}" aria-selected="${i === index}" aria-label="Ejercicio ${i + 1}">${mark}</button>`;
            }
            const state = e.status.solved ? "pill-green" : e.status.attempts ? "pill-amber" : "";
            const mark = e.status.solved ? "✓" : i + 1;
            return `<button type="button" role="tab" class="pill ex-jump ${i === index ? "pill-accent ex-current" : state}" data-jump="${i}" aria-selected="${i === index}" aria-label="Ejercicio ${i + 1}">${mark}</button>`;
          })
          .join("")}
      </div>

      <div id="ex-tools-slot" class="mb-md" ${toolsOpen && ex.kind === "problem" ? "" : "hidden"}></div>

      <article class="card stack-lg ex-card">
        <div class="stack-sm">
          <span class="eyebrow m-0">${
            exam
              ? `Ejercicio ${index + 1} de ${exercises.length}${ex.unitCode ? ` · ${esc(ex.unitCode)}` : ""} · ${esc(stripNumber(ex.topic.title))}`
              : `${ex.kind === "project" ? "Proyecto" : "Ejercicio"} ${index + 1} de ${exercises.length} · ${levelLabel(ex)}${ex.minutes ? ` · ${ex.minutes} min` : ""}`
          }</span>
          <h2 class="title-md m-0">${esc(ex.title)}</h2>
          ${ex.source ? `<span class="pill pill-accent ex-source">${icon("book", 12)} ${esc(ex.source)}</span>` : ""}
        </div>
        ${ex.kind === "project" ? projectHtml(ex, w) : problemHtml(ex, w)}
      </article>
    `;

    if (toolsOpen && ex.kind === "problem") {
      const slot = container.querySelector("#ex-tools-slot");
      if (slot) slot.appendChild(getToolsEl(ex.id));
    }

    bind(ex, w);
  }

  const goNext = () => {
    if (index < exercises.length - 1) {
      index += 1;
      paint();
      window.scrollTo({ top: 0, behavior: "instant" });
    } else if (!exam) {
      location.hash = backHash;
    }
  };

  const confirmAndSubmitExam = () => {
    const answered = exercises.filter((e, i) => isExerciseAnswered(e, work[i])).length;
    const flagged = work.filter((w) => w.flagged).length;
    const warnParts = [];
    if (answered < exercises.length) warnParts.push(`Respondiste ${answered} de ${exercises.length}`);
    if (flagged > 0) warnParts.push(`tenés ${flagged} marcado${flagged === 1 ? "" : "s"} para revisar`);
    if (warnParts.length && !window.confirm(`${warnParts.join(" y ")}. ¿Entregar el simulacro ahora?`)) {
      return;
    }
    submitFullExam();
  };

  function bind(ex, w) {
    container.querySelector("#ex-tools-toggle")?.addEventListener("click", () => {
      toolsOpen = !toolsOpen;
      paint();
    });
    container.querySelector("#exam-finish-now")?.addEventListener("click", confirmAndSubmitExam);
    container.querySelector("#ex-submit-final")?.addEventListener("click", confirmAndSubmitExam);
    container.querySelectorAll(".ex-jump").forEach((b) =>
      b.addEventListener("click", () => {
        index = Number(b.dataset.jump);
        paint();
      })
    );
    container.querySelector("#ex-prev")?.addEventListener("click", () => {
      if (index > 0) {
        index -= 1;
        paint();
        window.scrollTo({ top: 0, behavior: "instant" });
      }
    });
    container.querySelector("#ex-flag")?.addEventListener("click", () => {
      w.flagged = !w.flagged;
      paint();
    });
    container.querySelector("#ex-next")?.addEventListener("click", goNext);
    container.querySelector("#ex-skip")?.addEventListener("click", goNext);

    if (ex.kind === "project") {
      container.querySelectorAll(".ex-tick").forEach((t) =>
        t.addEventListener("change", () => {
          w.ticks[Number(t.dataset.tick)] = t.checked;
          paint();
        })
      );
      container.querySelector("#ex-done")?.addEventListener("click", markProjectDone);
      return;
    }

    container.querySelectorAll(".ex-input").forEach((inp) =>
      inp.addEventListener("input", () => {
        w.values[Number(inp.dataset.part)] = inp.value;
      })
    );
    container.querySelectorAll(".ex-opt").forEach((b) =>
      b.addEventListener("click", () => {
        const part = Number(b.dataset.part);
        w.picked[part] = Number(b.dataset.opt);
        if (w.verdicts) w.verdicts = null;
        paint();
        container.querySelector(`.ex-opt[data-part="${part}"][data-opt="${w.picked[part]}"]`)?.focus({ preventScroll: true });
      })
    );
    container.querySelector("#ex-form")?.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!exam && !w.locked) gradePractice();
    });
    container.querySelector("#ex-hint")?.addEventListener("click", () => {
      w.hintsShown += 1;
      paint();
    });
    container.querySelector("#ex-solution")?.addEventListener("click", () => {
      w.solutionShown = true;
      if (!(w.verdicts && w.verdicts.every(Boolean))) w.sawSolution = true;
      paint();
      container.querySelector(".ex-steps")?.scrollIntoView({ behavior: "smooth", block: "nearest" });
    });
    container.querySelector("#ex-report-btn")?.addEventListener("click", async () => {
      const msg = window.prompt(`¿Qué error o detalle encontraste en «${ex.title}»?`);
      if (!msg || !msg.trim()) return;
      try {
        await api.post("/api/reports", { kind: "exercise", target_id: ex.id, title: ex.title, message: msg.trim() });
        toast("Reporte guardado (visible en Ajustes)", "ok");
      } catch (err) {
        toast(err.message, "err");
      }
    });
    container.querySelectorAll(".ex-err-tag").forEach((btn) =>
      btn.addEventListener("click", async () => {
        const tag = w.errorTag === btn.dataset.tag ? "" : btn.dataset.tag;
        try {
          if (!ex.status?.attempts) {
            await record(ex, { correct: false, parts_ok: 0, saw_solution: true, error_tag: tag });
          } else {
            await api.post(`/api/exercises/${encodeURIComponent(ex.id)}/error-tag`, { error_tag: tag });
          }
          w.errorTag = tag;
          toast(tag ? "Error etiquetado para tu banco de errores" : "Etiqueta quitada", "ok");
          paint();
        } catch (err) {
          toast(err.message, "err");
        }
      })
    );
    container.querySelector("#ex-to-card")?.addEventListener("click", async () => {
      try {
        const res = await api.post(`/api/exercises/${encodeURIComponent(ex.id)}/to-card`, {});
        w.cardCreated = true;
        toast(res.already_exists ? "Ese ejercicio ya tiene tarjeta en tu repaso." : "Tarjeta agregada a tu repaso FSRS.", "ok");
        paint();
      } catch (err) {
        toast(err.message, "err");
      }
    });
  }

  paint();
}

export async function renderExerciseTopic(container, domainSlug, topicSlug, { exerciseId = null } = {}) {
  const { domain, topics } = await api.get(`/api/exercises/${encodeURIComponent(domainSlug)}`);
  const topic = topics.find((t) => t.slug === topicSlug);
  if (!topic) throw new Error("Este tema todavía no tiene ejercicios.");
  const exercises = topic.exercises.map((e) => ({ ...e, topic }));
  const wanted = exercises.findIndex((e) => e.id === exerciseId);
  const firstUnsolved = exercises.findIndex((e) => !e.status.solved);
  await runExercises(container, {
    domain,
    heading: stripNumber(topic.title),
    crumbs: `<a href="#/ejercicios">Ejercicios</a> <span>/</span> <a href="#/ejercicios/${esc(domain.slug)}">${esc(domain.name)}</a> <span>/</span> <span>${esc(stripNumber(topic.title))}</span>`,
    exercises,
    startIndex: wanted >= 0 ? wanted : Math.max(firstUnsolved, 0),
    backHash: `#/ejercicios/${domain.slug}`,
    lessonLink: `#/learn/${topic.node_id}`,
  });
}

/** Focused retry session over automatically scheduled failed / solution-assisted exercises. */
export async function renderExerciseRetries(container, { domain = null } = {}) {
  const qs = domain ? `?domain=${encodeURIComponent(domain)}` : "";
  const data = await api.get(`/api/exercises/retries${qs}`);
  if (!data.exercises?.length) {
    container.innerHTML = `
      <div class="focus-column">
        <div class="card callout-ok stack">
          <h2 class="m-0">No tenés ejercicios pendientes de reintento</h2>
          <p class="m-0">Cada ejercicio que falles o resuelvas mirando la solución vuelve automáticamente acá hasta que te salga solo.</p>
          <div class="row">
            <a href="#/ingreso" class="btn btn-primary">Volver a Ingreso</a>
            <a href="#/errores" class="btn btn-secondary">Ver banco de errores</a>
          </div>
        </div>
      </div>`;
    return;
  }
  const firstDom = data.exercises[0].topic;
  await runExercises(container, {
    domain: { slug: domain || firstDom.domain_slug, name: domain ? firstDom.domain_name : "Reintentos", lab_type: firstDom.lab_type },
    heading: `Reintentos automáticos (${data.exercises.length})`,
    crumbs: `<a href="#/errores">Banco de errores</a> <span>/</span> <span>Reintentos</span>`,
    exercises: data.exercises,
    startIndex: 0,
    backHash: domain ? `#/errores?domain=${encodeURIComponent(domain)}` : "#/errores",
  });
}

/** Interactive mock exam configurator + persisted exam history & trend chart. */
export async function renderExerciseExam(container, domainSlug, { ingreso = false } = {}) {
  const [exData, ingresoData, historyData] = await Promise.all([
    api.get(`/api/exercises/${encodeURIComponent(domainSlug)}`),
    api.get("/api/ingreso").catch(() => ({ subjects: [] })),
    api.get(`/api/exams?domain=${encodeURIComponent(domainSlug)}&limit=12`).catch(() => ({ exams: [], stats: { count: 0 } })),
  ]);

  const { domain, topics: allTopics } = exData;
  const subject = (ingresoData.subjects || []).find((s) => s.domain === domainSlug) || null;
  const topicsBySlug = new Map(allTopics.map((t) => [t.slug, t]));

  const unitItems = subject
    ? subject.units
        .map((u) => {
          const uTopics = u.topics.map((t) => topicsBySlug.get(t.slug)).filter(Boolean);
          const problems = uTopics.flatMap((t) =>
            t.exercises
              .filter((e) => e.kind === "problem")
              .map((e) => ({ ...e, topic: t, unitCode: u.code, unitTitle: u.short_title }))
          );
          return { code: u.code, short_title: u.short_title, problems };
        })
        .filter((u) => u.problems.length > 0)
    : [];

  const allProblems = unitItems.length
    ? unitItems.flatMap((u) => u.problems)
    : allTopics.flatMap((t) => t.exercises.filter((e) => e.kind === "problem").map((e) => ({ ...e, topic: t })));

  if (!allProblems.length) {
    throw new Error("No hay problemas para armar un simulacro en esta materia.");
  }

  const presets = EXAM_PRESETS[domainSlug] || [];
  const state = {
    presetId: presets.length ? presets[presets.length - 1].id : "custom",
    selectedUnits: new Set(unitItems.map((u) => u.code)),
    count: ingreso ? Math.min(10, allProblems.length) : Math.min(EXAM_SIZE, allProblems.length),
    minutes: ingreso ? 90 : 60,
    prioritizeOfficial: true,
  };

  function currentPool() {
    if (!unitItems.length) return allProblems;
    return unitItems.filter((u) => state.selectedUnits.has(u.code)).flatMap((u) => u.problems);
  }

  function launchExam() {
    const rawPool = currentPool();
    if (!rawPool.length) {
      toast("Seleccioná al menos una unidad con problemas.", "err");
      return;
    }
    const pool = shuffled(rawPool);
    if (state.prioritizeOfficial) {
      pool.sort((a, b) => Number(a.status.solved) - Number(b.status.solved) || Number(!a.source) - Number(!b.source));
    }
    const target = Math.min(state.count, pool.length);
    const chosen = [];
    const chosenIds = new Set();
    const perTopic = new Map();
    for (const cap of [EXAM_MAX_PER_TOPIC, 4, 99]) {
      for (const ex of pool) {
        if (chosen.length >= target) break;
        if (chosenIds.has(ex.id)) continue;
        const used = perTopic.get(ex.topic.slug) || 0;
        if (used >= cap) continue;
        perTopic.set(ex.topic.slug, used + 1);
        chosen.push(ex);
        chosenIds.add(ex.id);
      }
      if (chosen.length >= target) break;
    }

    const activePreset = presets.find((p) => p.id === state.presetId);
    const examHeading = activePreset ? `Simulacro · ${activePreset.label}` : `Simulacro · ${domain.name}`;
    const crumbs = ingreso
      ? `<a href="#/ingreso">Ingreso</a> <span>/</span> <span>${esc(domain.name)}</span> <span>/</span> <span>Simulacro</span>`
      : `<a href="#/ejercicios">Ejercicios</a> <span>/</span> <a href="#/ejercicios/${esc(domain.slug)}">${esc(domain.name)}</a> <span>/</span> <span>Simulacro</span>`;

    runExercises(container, {
      domain,
      heading: examHeading,
      crumbs,
      exercises: shuffled(chosen),
      exam: true,
      examOptions: {
        ingreso,
        mode: activePreset ? activePreset.id : ingreso ? "ingreso" : "custom",
        unitCodes: [...state.selectedUnits],
        timeLimitSec: state.minutes * 60,
      },
      backHash: ingreso ? "#/ingreso" : `#/ejercicios/${domain.slug}`,
    });
  }

  function paintConfig() {
    const pool = currentPool();
    const actualCount = Math.min(state.count, pool.length);
    const crumbs = ingreso
      ? `<a href="#/ingreso">Ingreso</a> <span>/</span> <span>${esc(domain.name)}</span> <span>/</span> <span>Simulacro</span>`
      : `<a href="#/ejercicios">Ejercicios</a> <span>/</span> <a href="#/ejercicios/${esc(domain.slug)}">${esc(domain.name)}</a> <span>/</span> <span>Simulacro</span>`;
    const exams = historyData.exams || [];
    const stats = historyData.stats || {};
    const trendSvg = renderExamTrendSvg([...exams].reverse());

    container.innerHTML = `
      <section class="band dots page-header" data-tone="${toneOf(domain.lab_type)}">
        <div>
          <div class="breadcrumb">${crumbs}</div>
          <h1>Simulacro de <em>${esc(domain.name)}</em></h1>
          <p class="m-0">Navegación libre entre problemas, entrega única al final y revisión completa con autoevaluación del procedimiento (aprobás con 60 %).</p>
        </div>
        ${
          stats.count
            ? `<div class="ing-hero-kpis">
                <div class="stat"><span class="num num-xl tabular">${stats.best_score}%</span><span class="stat-label">mejor nota</span></div>
                <div class="stat"><span class="num num-xl tabular">${stats.passed}/${stats.count}</span><span class="stat-label">aprobados</span></div>
              </div>`
            : ""
        }
      </section>

      <div class="grid-asymmetric">
        <section class="card stack-lg">
          ${
            presets.length
              ? `<div class="stack-sm">
                  <span class="eyebrow m-0">Elegí el formato</span>
                  <div class="row exam-presets">
                    ${presets
                      .map(
                        (p) =>
                          `<button type="button" class="btn btn-sm ${state.presetId === p.id ? "btn-primary" : "btn-secondary"} ex-preset-btn" data-preset="${esc(p.id)}">${esc(p.label)}</button>`
                      )
                      .join("")}
                  </div>
                </div>`
              : ""
          }

          ${
            unitItems.length
              ? `<div class="stack-sm">
                  <div class="row-between">
                    <span class="eyebrow m-0">Unidades incluidas</span>
                    <button type="button" class="btn btn-text btn-sm" id="ex-units-all">Seleccionar todas</button>
                  </div>
                  <div class="exam-unit-grid">
                    ${unitItems
                      .map((u) => {
                        const checked = state.selectedUnits.has(u.code);
                        return `
                        <label class="exam-unit-opt ${checked ? "is-on" : ""}">
                          <input type="checkbox" class="ex-unit-cb" value="${esc(u.code)}" ${checked ? "checked" : ""} />
                          <span class="grow"><strong>${esc(u.code)}</strong> · ${esc(u.short_title)}</span>
                          <span class="xs muted tabular">${u.problems.length}</span>
                        </label>`;
                      })
                      .join("")}
                  </div>
                </div>`
              : ""
          }

          <div class="grid-2" style="gap:16px;">
            <div class="stack-sm">
              <span class="small"><strong>Cantidad de problemas</strong></span>
              <div class="segmented" role="group">
                ${[6, 8, 10, 12]
                  .map(
                    (n) =>
                      `<button type="button" class="seg-btn ${state.count === n ? "active" : ""} ex-cnt-btn" data-cnt="${n}">${n}</button>`
                  )
                  .join("")}
              </div>
            </div>
            <div class="stack-sm">
              <span class="small"><strong>Tiempo límite</strong></span>
              <div class="segmented" role="group">
                ${[
                  [0, "Libre"],
                  [30, "30m"],
                  [60, "60m"],
                  [90, "90m"],
                  [120, "2h"],
                ]
                  .map(
                    ([m, lbl]) =>
                      `<button type="button" class="seg-btn ${state.minutes === m ? "active" : ""} ex-min-btn" data-min="${m}">${lbl}</button>`
                  )
                  .join("")}
              </div>
            </div>
          </div>

          <label class="row gap-sm small" style="cursor:pointer;">
            <input type="checkbox" id="ex-prio-cb" ${state.prioritizeOfficial ? "checked" : ""} style="width:18px;height:18px;min-height:0;" />
            <span>Priorizar ejercicios sin resolver y problemas de guías oficiales</span>
          </label>

          <div class="row-between">
            <span class="small muted tabular">${pool.length} problemas disponibles en esta selección</span>
            <button type="button" class="btn btn-primary btn-lg" id="ex-start-exam" ${actualCount ? "" : "disabled"}>
              ${icon("target", 18)} Empezar simulacro (${actualCount})
            </button>
          </div>
        </section>

        <aside class="card stack">
          <h2 class="title-sm m-0">Historial y evolución</h2>
          ${trendSvg}
          ${
            exams.length
              ? `<div class="list">
                  ${exams
                    .map(
                      (e) => `
                    <div class="list-row" style="padding:12px 0;">
                      <div class="grow">
                        <div class="small"><strong>${esc(e.title)}</strong></div>
                        <div class="xs muted tabular">${esc((e.created_at || "").slice(0, 10))} · ${e.correct_count}/${e.total_count} · ${fmtClock(e.duration_sec)}${
                          e.procedure_score_pct !== null && e.procedure_score_pct !== e.score_pct ? ` · proc ${e.procedure_score_pct}%` : ""
                        }</div>
                      </div>
                      <span class="pill ${e.passed ? "pill-green" : "pill-red"} tabular">${e.effective_score_pct ?? e.score_pct}%</span>
                    </div>`
                    )
                    .join("")}
                </div>`
              : `<div class="empty">Todavía no rendiste simulacros de esta materia. Tu evolución y notas van a aparecer acá.</div>`
          }
        </aside>
      </div>
    `;

    container.querySelectorAll(".ex-preset-btn").forEach((b) =>
      b.addEventListener("click", () => {
        const p = presets.find((x) => x.id === b.dataset.preset);
        if (!p) return;
        state.presetId = p.id;
        state.selectedUnits = new Set(p.units ? p.units.filter((c) => unitItems.some((u) => u.code === c)) : unitItems.map((u) => u.code));
        state.count = p.count;
        state.minutes = p.minutes;
        paintConfig();
      })
    );
    container.querySelector("#ex-units-all")?.addEventListener("click", () => {
      state.presetId = "custom";
      state.selectedUnits = new Set(unitItems.map((u) => u.code));
      paintConfig();
    });
    container.querySelectorAll(".ex-unit-cb").forEach((cb) =>
      cb.addEventListener("change", () => {
        state.presetId = "custom";
        if (cb.checked) state.selectedUnits.add(cb.value);
        else state.selectedUnits.delete(cb.value);
        paintConfig();
      })
    );
    container.querySelectorAll(".ex-cnt-btn").forEach((b) =>
      b.addEventListener("click", () => {
        state.count = Number(b.dataset.cnt);
        paintConfig();
      })
    );
    container.querySelectorAll(".ex-min-btn").forEach((b) =>
      b.addEventListener("click", () => {
        state.minutes = Number(b.dataset.min);
        paintConfig();
      })
    );
    container.querySelector("#ex-prio-cb")?.addEventListener("change", (e) => {
      state.prioritizeOfficial = e.target.checked;
    });
    container.querySelector("#ex-start-exam")?.addEventListener("click", launchExam);
  }

  paintConfig();
}
