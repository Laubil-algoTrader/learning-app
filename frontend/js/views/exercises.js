import { icon } from "../icons.js";
import { api, esc, rich, toast, toneOf, labLinkToHash } from "../main.js";
import { ART } from "./library.js";
import { checkAnswer } from "./review.js";

/**
 * Exercises: multi-step problems (maths, physics) and hands-on projects (electronics,
 * guitar), grouped by roadmap topic. Unlike review cards they are not scheduled: the
 * learner picks a topic, works on paper and the app records each graded attempt.
 */

const PROBLEM_LEVELS = { 1: "Básico", 2: "Intermedio", 3: "Tipo examen" };
const PROJECT_LEVELS = { 1: "Corto", 2: "Intermedio", 3: "Desafío" };
const EXAM_SIZE = 8;
const EXAM_MAX_PER_TOPIC = 2;

const stripNumber = (title) => String(title || "").replace(/^\d+\.\s*/, "");
const levelLabel = (ex) => (ex.kind === "project" ? PROJECT_LEVELS : PROBLEM_LEVELS)[ex.level] || "";
const noun = (kind, n) => (kind === "project" ? (n === 1 ? "proyecto" : "proyectos") : n === 1 ? "ejercicio" : "ejercicios");
const doneWord = (kind, n) => (kind === "project" ? (n === 1 ? "hecho" : "hechos") : n === 1 ? "resuelto" : "resueltos");

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

/* ---------- Index: one tile per discipline ---------- */

export async function renderExercisesIndex(container) {
  const { domains } = await api.get("/api/exercises");

  container.innerHTML = `
    <div class="page-header">
      <div>
        <h1>Ejercicios</h1>
        <p class="muted">Problemas para resolver en papel y proyectos para hacer con las manos, ordenados por tema. El repaso es para no olvidar; esto es para aprender a resolver.</p>
      </div>
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
                  <div class="tile-art">${ART[tone] || ART.generic}</div>
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
          ? `<a href="#/ejercicios/${esc(domain.slug)}/simulacro" class="btn btn-primary">${icon("target", 16)} Simulacro de ${Math.min(EXAM_SIZE, problems.length)}</a>`
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

/* ---------- Runner: a topic's exercises, or a mixed mock exam ---------- */

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
  };
}

async function runExercises(container, { domain, heading, crumbs, exercises, startIndex = 0, exam = false, examOptions = {}, backHash, lessonLink }) {
  let index = Math.min(Math.max(startIndex, 0), exercises.length - 1);
  const work = exercises.map(newWorkState);
  const examResults = exercises.map(() => null);
  let finished = false;

  const record = async (ex, body) => {
    try {
      const res = await api.post(`/api/exercises/${encodeURIComponent(ex.id)}/attempts`, body);
      ex.status = res.status;
    } catch (err) {
      toast(`No se pudo guardar el intento: ${err.message}`, "err");
    }
  };

  const grade = async () => {
    const ex = exercises[index];
    const w = work[index];
    const verdicts = ex.parts.map((p, i) => checkAnswer(p.check, p.check.type === "choice" ? w.picked[i] : w.values[i]) === true);
    const answered = ex.parts.every((p, i) => (p.check.type === "choice" ? w.picked[i] !== null : w.values[i].trim() !== ""));
    if (!answered) {
      toast(ex.parts.length > 1 ? "Respondé todos los incisos antes de corregir." : "Escribí tu respuesta antes de corregir.", "info");
      return;
    }
    w.verdicts = verdicts;
    const ok = verdicts.every(Boolean);
    if (exam) {
      w.locked = true;
      w.solutionShown = true;
      examResults[index] = ok;
    } else if (ok) {
      w.locked = true;
    }
    await record(ex, { correct: ok, parts_ok: verdicts.filter(Boolean).length, saw_solution: w.sawSolution });
    paint();
    container.querySelector(ok || exam ? "#ex-next" : "#ex-form input, #ex-form .option-btn")?.focus({ preventScroll: true });
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
    const verdict = w.verdicts ? w.verdicts[i] : null;
    const badge =
      verdict === null
        ? ""
        : verdict
        ? `<span class="pill pill-green">Correcto</span>`
        : `<span class="pill pill-red">No coincide</span>`;
    const reveal = w.solutionShown ? `<p class="small m-0"><strong>Respuesta:</strong> <span class="rich">${rich(p.answer)}</span></p>` : "";
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
    const solved = w.verdicts && w.verdicts.every(Boolean);
    const graded = Boolean(w.verdicts);
    const isLast = index === exercises.length - 1;
    const nextLabel = isLast ? (exam ? "Ver el resultado" : "Volver a los temas") : "Siguiente ejercicio";
    return `
      <form id="ex-form" class="stack-lg" novalidate>
        <div class="stack">${paragraphs(ex.statement)}</div>
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
                    : exam
                    ? "<strong>No salió.</strong> Mirá la resolución y marcá en qué paso te desviaste."
                    : `<strong>Todavía no.</strong> ${w.verdicts.filter(Boolean).length} de ${ex.parts.length} ${ex.parts.length === 1 ? "inciso" : "incisos"} bien. Revisá las cuentas y volvé a corregir, o mirá la resolución.`
                }
              </p>`
            : ""
        }

        <div class="row">
          ${w.locked ? "" : `<button type="submit" class="btn btn-primary">Corregir</button>`}
          ${w.locked ? `<button type="button" class="btn btn-primary" id="ex-next">${nextLabel} ${icon("arrowRight", 16)}</button>` : ""}
          ${
            !exam && !w.locked && w.hintsShown < ex.hints.length
              ? `<button type="button" class="btn btn-secondary" id="ex-hint">${w.hintsShown ? "Otra pista" : "Pedir una pista"} (${w.hintsShown + 1} de ${ex.hints.length})</button>`
              : ""
          }
          ${!w.solutionShown && !exam ? `<button type="button" class="btn btn-ghost" id="ex-solution">Ver la resolución</button>` : ""}
          ${!exam && !w.locked && !isLast ? `<button type="button" class="btn btn-ghost" id="ex-skip">Saltear</button>` : ""}
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

  const summaryHtml = () => {
    const right = examResults.filter(Boolean).length;
    const failedTopics = new Map();
    exercises.forEach((ex, i) => {
      if (!examResults[i]) failedTopics.set(ex.topic.slug, ex.topic);
    });
    return `
      <div class="page-header">
        <div>
          <div class="breadcrumb">${crumbs}</div>
          <h1>${right} de ${exercises.length}</h1>
          <p class="muted">${
            right === exercises.length
              ? "Simulacro perfecto. Probá otro: los ejercicios cambian."
              : right >= Math.ceil(exercises.length * 0.6)
              ? "Buen simulacro. Los que no salieron te marcan qué temas reforzar."
              : "Todavía falta práctica en varios temas. Empezá por los de abajo."
          }</p>
        </div>
      </div>
      <div class="stack-lg">
        ${
          failedTopics.size
            ? `<section class="stack">
                <h2 class="title-md m-0">Para reforzar</h2>
                <div class="card"><div class="list">
                  ${[...failedTopics.values()]
                    .map(
                      (t) => `
                    <div class="list-row">
                      <span class="grow list-title">${esc(stripNumber(t.title))}</span>
                      <a class="btn btn-secondary btn-sm" href="#/learn/${t.node_id}">Lección</a>
                      <a class="btn btn-secondary btn-sm" href="#/ejercicios/${esc(domain.slug)}/${esc(t.slug)}">Ejercicios</a>
                    </div>`
                    )
                    .join("")}
                </div></div>
              </section>`
            : ""
        }
        <div class="row">
          <button type="button" class="btn btn-primary" id="ex-again">Otro simulacro</button>
          <a class="btn btn-secondary" href="${backHash}">Volver a los temas</a>
        </div>
      </div>`;
  };

  function paint() {
    if (finished) {
      container.innerHTML = summaryHtml();
      container.querySelector("#ex-again")?.addEventListener("click", () => renderExerciseExam(container, domain.slug, examOptions));
      window.scrollTo({ top: 0, behavior: "instant" });
      return;
    }
    const ex = exercises[index];
    const w = work[index];
    container.innerHTML = `
      <div class="page-header">
        <div>
          <div class="breadcrumb">${crumbs}</div>
          <h1>${esc(heading)}</h1>
        </div>
        ${lessonLink ? `<a href="${lessonLink}" class="btn btn-secondary">${icon("book", 16)} Ver la lección</a>` : ""}
      </div>

      <div class="row ex-pager" role="tablist" aria-label="Ejercicios">
        ${exercises
          .map((e, i) => {
            const state = exam ? (examResults[i] === null ? "" : examResults[i] ? "pill-green" : "pill-red") : e.status.solved ? "pill-green" : e.status.attempts ? "pill-amber" : "";
            const mark = exam ? (examResults[i] === true ? "✓" : examResults[i] === false ? "✗" : i + 1) : e.status.solved ? "✓" : i + 1;
            return `<button type="button" role="tab" class="pill ex-jump ${i === index ? "pill-accent ex-current" : state}" data-jump="${i}" aria-selected="${i === index}" ${exam ? "disabled" : ""} aria-label="Ejercicio ${i + 1}">${mark}</button>`;
          })
          .join("")}
      </div>

      <article class="card stack-lg ex-card">
        <div class="stack-sm">
          <span class="eyebrow m-0">${exam ? `Ejercicio ${index + 1} de ${exercises.length} · ${esc(stripNumber(ex.topic.title))}` : `${ex.kind === "project" ? "Proyecto" : "Ejercicio"} ${index + 1} de ${exercises.length} · ${levelLabel(ex)}${ex.minutes ? ` · ${ex.minutes} min` : ""}`}</span>
          <h2 class="title-md m-0">${esc(ex.title)}</h2>
          ${ex.source ? `<span class="pill pill-accent ex-source">${icon("book", 12)} ${esc(ex.source)}</span>` : ""}
        </div>
        ${ex.kind === "project" ? projectHtml(ex, w) : problemHtml(ex, w)}
      </article>
    `;
    bind(ex, w);
  }

  const goNext = () => {
    if (index < exercises.length - 1) {
      index += 1;
      paint();
      window.scrollTo({ top: 0, behavior: "instant" });
    } else if (exam) {
      finished = true;
      paint();
    } else {
      location.hash = backHash;
    }
  };

  function bind(ex, w) {
    container.querySelectorAll(".ex-jump").forEach((b) =>
      b.addEventListener("click", () => {
        index = Number(b.dataset.jump);
        paint();
      })
    );
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
      if (!w.locked) grade();
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

/** A mixed mock exam: unsolved problems first, at most two per topic, graded once each. */
/**
 * With `ingreso`, only topics of the UNCuyo entrance syllabus enter the exam, there are more
 * problems, and those taken from the official guides come first.
 */
export async function renderExerciseExam(container, domainSlug, { ingreso = false } = {}) {
  const { domain, topics: allTopics } = await api.get(`/api/exercises/${encodeURIComponent(domainSlug)}`);
  let topics = allTopics;
  if (ingreso) {
    const { subjects } = await api.get("/api/ingreso");
    const subject = subjects.find((s) => s.domain === domainSlug);
    const program = new Set((subject?.units || []).flatMap((u) => u.topics.map((t) => t.slug)));
    topics = allTopics.filter((t) => program.has(t.slug));
  }
  const size = ingreso ? EXAM_SIZE + 2 : EXAM_SIZE;
  const pool = shuffled(topics.flatMap((t) => t.exercises.filter((e) => e.kind === "problem").map((e) => ({ ...e, topic: t }))));
  pool.sort((a, b) => Number(a.status.solved) - Number(b.status.solved) || (ingreso ? Number(!a.source) - Number(!b.source) : 0));
  const perTopic = new Map();
  const chosen = [];
  for (const ex of pool) {
    const used = perTopic.get(ex.topic.slug) || 0;
    if (used >= EXAM_MAX_PER_TOPIC) continue;
    perTopic.set(ex.topic.slug, used + 1);
    chosen.push(ex);
    if (chosen.length === size) break;
  }
  if (!chosen.length) throw new Error("No hay problemas para armar un simulacro en esta materia.");
  await runExercises(container, {
    domain,
    heading: ingreso ? "Simulacro del programa del ingreso" : "Simulacro",
    crumbs: ingreso
      ? `<a href="#/ingreso">Ingreso</a> <span>/</span> <span>${esc(domain.name)}</span> <span>/</span> <span>Simulacro</span>`
      : `<a href="#/ejercicios">Ejercicios</a> <span>/</span> <a href="#/ejercicios/${esc(domain.slug)}">${esc(domain.name)}</a> <span>/</span> <span>Simulacro</span>`,
    exercises: shuffled(chosen),
    exam: true,
    examOptions: { ingreso },
    backHash: ingreso ? "#/ingreso" : `#/ejercicios/${domain.slug}`,
  });
}
