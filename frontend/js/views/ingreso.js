import { icon } from "../icons.js";
import { subjectArt, subjectLogo } from "../art.js";
import { api, esc, toast, toneOf, LAB_ROUTES } from "../main.js";

/**
 * The UNCuyo 2027 entrance course workspace:
 *   1. Overall readiness band (progress across the 3 exam modules + pass mark).
 *   2. Interactive 3-module switcher (Matemática, Física, Comprensión Lectora).
 *   3. Focused subject workspace with sticky unit sidebar, search, status filters,
 *      active-topic spotlight and clear 3-step mastery chips (Lección → Repaso → Ejercicios).
 */

const ALL_UNITS = "__all__";
const SUBJECT_KEY_STORAGE = "aprendelab_ingreso_subject";
const unitStorageKey = (subjectKey) => `aprendelab_ingreso_unit:${subjectKey}`;

const stripNumber = (title) => String(title || "").replace(/^\d+\.\s*/, "");
const normSearch = (s) =>
  String(s || "")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .trim();

const SHORT_SUBJECT_NAME = {
  matematica: "Matemática",
  fisica: "Física",
  clyrp: "Comprensión y Problemas",
};

function readStore(key) {
  try {
    return sessionStorage.getItem(key) || "";
  } catch {
    return "";
  }
}

function writeStore(key, val) {
  try {
    sessionStorage.setItem(key, val);
  } catch {
    // ignore private-mode storage errors
  }
}

function formatEstTime(mins) {
  if (!mins || mins <= 0) return "";
  if (mins < 60) return `~${mins} min`;
  const h = Math.floor(mins / 60);
  const m = mins % 60;
  return m >= 10 ? `~${h} h ${m} min` : `~${h} h`;
}

function topicNextStep(t) {
  if (t.due_count > 0) return "review";
  if (!t.lesson_completed) return "lesson";
  if (t.cards > 0 && t.practiced_pct < 60) return "review";
  if (t.exercises_total > 0 && t.exercises_solved < t.exercises_total) return "exercises";
  return "done";
}

function renderSubjectAction(s) {
  const act = s.next_action || {};
  const t = act.topic || s.next_topic;
  if (act.kind === "review" && s.due_count > 0) {
    return `<a class="btn btn-primary" href="#/review?domain=${esc(s.domain)}">Repasar hoy (${s.due_count}) ${icon("arrowRight", 16)}</a>`;
  }
  if (act.kind === "practice" && t) {
    return `<a class="btn btn-primary" href="#/review?node=${t.node_id}">Practicar tarjetas: ${esc(stripNumber(t.title))} ${icon("arrowRight", 16)}</a>`;
  }
  if (act.kind === "lesson" && t) {
    const verb = s.lessons_done > 0 ? "Seguir" : "Empezar";
    return `<a class="btn btn-primary" href="#/learn/${t.node_id}">${verb}: ${esc(stripNumber(t.title))} ${icon("arrowRight", 16)}</a>`;
  }
  if (act.kind === "exercises" && t) {
    return `<a class="btn btn-primary" href="#/ejercicios/${esc(s.domain)}/${esc(t.slug)}">Ejercicios: ${esc(stripNumber(t.title))} ${icon("arrowRight", 16)}</a>`;
  }
  return `<a class="btn btn-primary" href="#/ejercicios/${esc(s.domain)}/simulacro?ingreso=1">${icon("target", 16)} Rendir simulacro ${icon("arrowRight", 16)}</a>`;
}

function renderTopicSteps(t, domain) {
  const step = topicNextStep(t);

  const lessonDone = t.lesson_completed;
  const lessonCls = lessonDone ? "is-done" : step === "lesson" ? "is-next" : "";
  const lessonChip = `
    <a class="ing-step ${lessonCls}" href="#/learn/${t.node_id}" title="${lessonDone ? "Lección completada · clic para releer" : "Abrir lección"}">
      <span class="ing-step-ico">${lessonDone ? icon("check", 12) : "1"}</span>
      <span>${lessonDone ? "Lección" : "Lección"}</span>
    </a>`;

  let reviewChip = "";
  if (t.cards > 0) {
    const reviewDone = t.practiced_pct >= 60 && t.due_count === 0;
    const reviewDue = t.due_count > 0;
    const reviewLocked = !t.lesson_completed && t.practiced_pct === 0 && !reviewDue;
    const reviewCls = reviewDue
      ? "is-warn"
      : reviewDone
      ? "is-done"
      : step === "review"
      ? "is-next"
      : reviewLocked
      ? "is-muted"
      : "";
    const reviewText = reviewDue
      ? `Repaso · ${t.due_count} hoy`
      : t.practiced_pct > 0
      ? `Repaso · ${t.practiced_pct} %`
      : `Repaso (${t.cards})`;
    const reviewTitle = reviewLocked
      ? "Completá primero la lección para habilitar sus tarjetas de repaso"
      : `${t.cards} tarjetas · ${t.practiced_pct} % practicadas`;
    reviewChip = `
      <a class="ing-step ${reviewCls}" href="#/review?node=${t.node_id}" title="${esc(reviewTitle)}">
        <span class="ing-step-ico">${reviewDone ? icon("check", 12) : "2"}</span>
        <span>${reviewText}</span>
      </a>`;
  }

  let exChip = "";
  if (t.exercises_total > 0) {
    const exDone = t.exercises_solved >= t.exercises_total;
    const exCls = exDone ? "is-done" : step === "exercises" ? "is-next" : "";
    const officialHint = t.exercises_official ? ` (${t.exercises_official} de las guías oficiales)` : "";
    exChip = `
      <a class="ing-step ${exCls}" href="#/ejercicios/${esc(domain)}/${esc(t.slug)}" title="${t.exercises_solved} de ${t.exercises_total} ejercicios resueltos${esc(officialHint)}">
        <span class="ing-step-ico">${exDone ? icon("check", 12) : "3"}</span>
        <span>Ejercicios ${t.exercises_solved}/${t.exercises_total}</span>
        ${t.exercises_official ? `<span class="ing-official-dot" aria-label="${t.exercises_official} oficiales">${icon("book", 11)}</span>` : ""}
      </a>`;
  }

  return `<div class="ing-steps">${lessonChip}${reviewChip}${exChip}</div>`;
}

function renderSpotlight(t, domain, idx) {
  const step = topicNextStep(t);
  const badgeMap = {
    review: t.due_count > 0 ? { cls: "pill-amber", text: `Repaso pendiente (${t.due_count})` } : { cls: "pill-amber", text: "Practicar tarjetas" },
    lesson: { cls: "pill-tone", text: "Próxima lección de la unidad" },
    exercises: { cls: "pill-tone", text: "Ejercicios pendientes" },
    done: { cls: "pill-green", text: "Tema completo" },
  };
  const badge = badgeMap[step] || badgeMap.lesson;
  const numStr = String(idx + 1).padStart(2, "0");

  let primaryBtn = `<a class="btn btn-primary btn-sm" href="#/learn/${t.node_id}">${icon("bookOpen", 14)} Empezar lección ${icon("arrowRight", 14)}</a>`;
  if (step === "review") {
    primaryBtn = `<a class="btn btn-primary btn-sm" href="#/review?node=${t.node_id}">${icon("brain", 14)} ${t.due_count ? `Repasar (${t.due_count})` : "Practicar tarjetas"} ${icon("arrowRight", 14)}</a>`;
  } else if (step === "exercises") {
    primaryBtn = `<a class="btn btn-primary btn-sm" href="#/ejercicios/${esc(domain)}/${esc(t.slug)}">${icon("target", 14)} Resolver ejercicios ${icon("arrowRight", 14)}</a>`;
  }

  return `
    <article class="lesson-spotlight ing-spotlight">
      <div class="row-between">
        <div class="row gap-sm">
          <span class="pill ${badge.cls}">${badge.text}</span>
          ${t.est_minutes && !t.lesson_completed ? `<span class="xs muted">${icon("clock", 13)} ~${t.est_minutes} min</span>` : ""}
          ${t.exercises_official ? `<span class="xs muted">${icon("book", 12)} ${t.exercises_official} de guía oficial</span>` : ""}
          ${t.struggling ? `<span class="pill pill-amber">Conviene releer</span>` : ""}
        </div>
        <div class="row gap-sm">
          <span class="xs muted tabular">${t.progress_pct} % del tema</span>
          <button type="button" class="ing-star-btn ${t.bookmarked ? "is-on" : ""}" data-bookmark-node="${t.node_id}" aria-pressed="${Boolean(t.bookmarked)}" title="${t.bookmarked ? "Quitar marca para el parcial" : "Marcar para repasar antes del parcial"}">${t.bookmarked ? "★" : "☆"}</button>
        </div>
      </div>
      <div class="lesson-spotlight-grid">
        <span class="lesson-spotlight-num tabular" aria-hidden="true">${numStr}</span>
        <div class="grow stack-sm">
          <h3 class="title-sm m-0">${esc(stripNumber(t.title))}</h3>
          ${t.summary ? `<p class="secondary small m-0">${esc(t.summary)}</p>` : ""}
          ${renderTopicSteps(t, domain)}
        </div>
        <div class="lesson-spotlight-actions">
          ${primaryBtn}
        </div>
      </div>
    </article>`;
}

function renderTopicRow(t, domain, displayIdx, { showUnitBadge = false, unitCode = "" } = {}) {
  const numStr = String(displayIdx + 1).padStart(2, "0");
  const isComplete = t.completed || t.status === "mastered";
  const isWarn = t.due_count > 0 || t.struggling;
  const markerCls = isComplete
    ? "is-mastered"
    : isWarn
    ? "is-in_progress"
    : t.lesson_completed || t.exercises_solved > 0
    ? "is-available"
    : "is-locked";
  const markerContent = isComplete ? icon("check", 14) : numStr;

  return `
    <article class="ing-topic-row ${isComplete ? "is-complete" : ""}">
      <span class="lesson-marker ${markerCls} tabular" aria-hidden="true">${markerContent}</span>
      <div class="ing-topic-body">
        <div class="ing-topic-head">
          <div class="ing-topic-copy">
            <div class="row gap-sm" style="align-items:baseline;">
              <a class="ing-topic-link" href="#/learn/${t.node_id}">${esc(stripNumber(t.title))}</a>
              ${showUnitBadge && unitCode ? `<span class="pill xs">${esc(unitCode)}</span>` : ""}
              ${t.struggling ? `<span class="pill pill-amber">Reforzar</span>` : ""}
            </div>
            ${t.summary ? `<p class="xs muted m-0 ing-topic-summary">${esc(t.summary)}</p>` : ""}
          </div>
          <div class="ing-topic-right">
            ${t.est_minutes && !t.lesson_completed ? `<span class="xs muted tabular">~${t.est_minutes} min</span>` : ""}
            <span class="ing-topic-pct tabular ${t.progress_pct >= 60 ? "is-ok" : ""}">${t.progress_pct} %</span>
            <button type="button" class="ing-star-btn ${t.bookmarked ? "is-on" : ""}" data-bookmark-node="${t.node_id}" aria-pressed="${Boolean(t.bookmarked)}" title="${t.bookmarked ? "Quitar marca para el parcial" : "Marcar para repasar antes del parcial"}">${t.bookmarked ? "★" : "☆"}</button>
          </div>
        </div>
        <div class="ing-topic-foot">
          ${renderTopicSteps(t, domain)}
          <div class="ing-topic-bar" aria-hidden="true"><span style="width:${t.progress_pct}%;"></span></div>
        </div>
      </div>
    </article>`;
}

function renderModuleCards(data, activeKey) {
  const passMark = data.pass_mark || 60;
  return `
    <div class="ing-modules" role="tablist" aria-label="Módulos del curso de ingreso">
      ${data.subjects
        .map((s) => {
          const tone = toneOf(s.lab_type);
          const active = s.key === activeKey;
          const shortName = SHORT_SUBJECT_NAME[s.key] || s.name;
          const ready = s.progress_pct >= passMark;
          let statusTag = `${s.units.length} unidades`;
          let statusCls = "muted";
          if (s.due_count > 0) {
            statusTag = `${s.due_count} ${s.due_count === 1 ? "repaso hoy" : "repasos hoy"}`;
            statusCls = "is-warn";
          } else if (ready) {
            statusTag = "En nivel de examen";
            statusCls = "is-ok";
          } else if (s.lessons_done > 0 || s.exercises_solved > 0) {
            statusTag = "En curso";
            statusCls = "is-active-tag";
          }

          return `
          <button
            type="button"
            role="tab"
            aria-selected="${active ? "true" : "false"}"
            class="ing-mod-card ${active ? "active" : ""}"
            data-subject="${esc(s.key)}"
            data-tone="${tone}"
          >
            <div class="ing-mod-top">
              <span class="domain-icon-box ing-mod-ico">${subjectLogo(s.key, 22)}</span>
              <div class="ing-mod-titles">
                <span class="ing-mod-name">${esc(shortName)}</span>
                <span class="xs ing-mod-status ${statusCls}">${esc(statusTag)}</span>
              </div>
              <span class="num ing-mod-pct tabular">${s.progress_pct}<span class="ing-mod-pct-sym">%</span></span>
            </div>
            <div class="ing-track-wrap" title="Meta de aprobación: ${passMark} %">
              <div class="progress-track"><div class="progress-fill" style="width:${s.progress_pct}%;"></div></div>
              <span class="ing-pass-tick" style="left:${passMark}%;" aria-hidden="true"></span>
            </div>
            <div class="ing-mod-meta xs muted tabular">
              <span>${s.lessons_done}/${s.topics_total} lecciones</span>
              <span>·</span>
              <span>${s.exercises_solved}/${s.exercises_total} ejercicios</span>
              ${s.exam_stats?.count ? `<span>·</span><span>Simulacro ${s.exam_stats.best_score}%</span>` : ""}
              ${s.pace?.days_left !== null && s.pace?.days_left >= 0 ? `<span>·</span><span>${s.pace.days_left}d</span>` : ""}
            </div>
          </button>`;
        })
        .join("")}
    </div>`;
}

export async function renderIngreso(container, opts = {}) {
  const data = await api.get("/api/ingreso");
  const subjects = data.subjects || [];
  if (!subjects.length) {
    container.innerHTML = `<div class="empty">No se encontraron materias del programa de ingreso.</div>`;
    return;
  }

  const passMark = data.pass_mark || 60;
  const validSubjects = new Set(subjects.map((s) => s.key));
  const savedSubject = readStore(SUBJECT_KEY_STORAGE);
  const autoSubject =
    subjects.find((s) => s.due_count > 0)?.key ||
    subjects.find((s) => s.lessons_done > 0 || s.exercises_solved > 0)?.key ||
    subjects[0].key;
  const initialSubject =
    (opts.subject && validSubjects.has(opts.subject) && opts.subject) ||
    (validSubjects.has(savedSubject) && savedSubject) ||
    autoSubject;

  const state = {
    subjectKey: initialSubject,
    unitKey: "",
    filter: "all",
    query: "",
  };

  function resolveInitialUnit(subject, requestedUnit = "") {
    const unitCodes = new Set(subject.units.map((u) => u.code));
    if (requestedUnit === ALL_UNITS || requestedUnit === "todas") return ALL_UNITS;
    if (requestedUnit && unitCodes.has(requestedUnit.toUpperCase())) return requestedUnit.toUpperCase();
    const saved = readStore(unitStorageKey(subject.key));
    if (saved === ALL_UNITS || unitCodes.has(saved)) return saved;
    const activeTopicId = subject.next_action?.topic?.node_id || subject.next_topic?.node_id;
    const activeUnit =
      subject.units.find((u) => activeTopicId && u.topics.some((t) => t.node_id === activeTopicId)) ||
      subject.units.find((u) => u.lessons_done < u.topics.length) ||
      subject.units[0];
    return activeUnit ? activeUnit.code : ALL_UNITS;
  }

  state.unitKey = resolveInitialUnit(
    subjects.find((s) => s.key === state.subjectKey),
    opts.unit || ""
  );

  // Build static top hero once, plus dynamic module switcher & workspace containers
  const dueGlobal = data.due_count || 0;
  const firstDueSubject = subjects.find((s) => s.due_count > 0);
  container.innerHTML = `
    <section class="band dots page-header ing-hero" data-tone="brand">
      <div class="ing-hero-copy">
        <div class="eyebrow"><span class="eyebrow-dot"></span>Curso de Ingreso · ${subjects.length} módulos · Aprobación ${passMark} %</div>
        <h1>Ingreso a <em>Ingeniería</em></h1>
        <p>UNCuyo 2027 · Solo los temas y guías que entran en el examen, ordenados unidad por unidad. Cada tema avanza por partes iguales entre lección, repaso y ejercicios.</p>
        ${
          dueGlobal > 0 && firstDueSubject
            ? `<div class="row mt-md">
                <a class="btn btn-primary" href="#/review?domain=${esc(firstDueSubject.domain)}">${icon("brain", 16)} ${dueGlobal} ${dueGlobal === 1 ? "repaso pendiente hoy" : "repasos pendientes hoy"} ${icon("arrowRight", 16)}</a>
              </div>`
            : ""
        }
      </div>
      <div class="ing-hero-stats">
        <div class="ing-hero-kpis">
          <div class="stat">
            <span class="num num-xl tabular">${data.overall_pct}<span style="font-size:0.48em;opacity:0.75;">%</span></span>
            <span class="stat-label">avance global</span>
          </div>
          <div class="stat">
            <span class="num num-xl tabular">${data.lessons_done}<span style="font-size:0.48em;opacity:0.65;"> / ${data.topics_total}</span></span>
            <span class="stat-label">lecciones</span>
          </div>
          <div class="stat">
            <span class="num num-xl tabular">${data.exercises_solved}<span style="font-size:0.48em;opacity:0.65;"> / ${data.exercises_total}</span></span>
            <span class="stat-label">ejercicios (${data.exercises_official} oficiales)</span>
          </div>
        </div>
        <div class="ing-hero-meter">
          <div class="ing-track-wrap" title="Meta de aprobación: ${passMark} % en cada módulo">
            <div class="progress-track"><div class="progress-fill" style="width:${data.overall_pct}%;"></div></div>
            <span class="ing-pass-tick" style="left:${passMark}%;" aria-hidden="true"></span>
          </div>
          <div class="row-between xs muted tabular">
            <span>${data.subjects_ready} de ${subjects.length} módulos en ≥ ${passMark} %</span>
            <span>Meta: ${passMark} %</span>
          </div>
        </div>
      </div>
    </section>

    <section id="ing-modules-host" class="mb-lg"></section>
    <section id="ing-plan-host" class="mb-lg"></section>
    <div id="ing-workspace-host"></div>
  `;

  const modulesHost = container.querySelector("#ing-modules-host");
  const planHost = container.querySelector("#ing-plan-host");
  const workspaceHost = container.querySelector("#ing-workspace-host");
  let editingDates = false;

  function renderPlanBar(s) {
    const today = data.today || { lessons: 0, exercises: 0, reviews: 0, lesson_goal: 2, exercise_goal: 5 };
    const pace = s.pace || {};
    const dates = data.exam_dates || {};
    const lesOk = today.lessons >= (today.lesson_goal || 2);
    const exOk = today.exercises >= (today.exercise_goal || 5);

    let paceHtml = `<span class="xs muted">Definí tu fecha de examen para calcular el ritmo diario sugerido.</span>`;
    if (pace.pace_status === "past") {
      paceHtml = `<span class="pill">Fecha pasada (${esc(pace.exam_date)})</span>`;
    } else if (pace.days_left !== null && pace.days_left !== undefined) {
      const statusCls = pace.pace_status === "tight" ? "pill-amber" : "pill-green";
      const paceCopy =
        pace.pace_status === "ready"
          ? "¡Programa al día! Enfocate en simulacros y repaso."
          : `Sugerido: ~${pace.recommended_lessons_per_day} lec/día · ~${pace.recommended_exercises_per_day} ej/día`;
      paceHtml = `
        <span class="pill ${statusCls} tabular">${pace.days_left === 0 ? "¡Hoy es el examen!" : `Faltan ${pace.days_left} días`}</span>
        <span class="xs muted">${paceCopy}</span>`;
    }

    planHost.innerHTML = `
      <div class="card ing-plan-bar stack-sm">
        <div class="row-between">
          <div class="row gap-sm" style="align-items:center;">
            <span class="eyebrow m-0">Meta de hoy</span>
            <span class="pill ${lesOk ? "pill-green" : ""} tabular">${lesOk ? "✓ " : ""}${today.lessons}/${today.lesson_goal} lecciones</span>
            <span class="pill ${exOk ? "pill-green" : ""} tabular">${exOk ? "✓ " : ""}${today.exercises}/${today.exercise_goal} ejercicios</span>
            <span class="pill tabular">${today.reviews} repasos</span>
          </div>
          <div class="row gap-sm" style="align-items:center;">
            ${paceHtml}
            <button type="button" class="btn btn-secondary btn-sm" id="ing-dates-toggle">
              ${icon("clock", 14)} ${editingDates ? "Cerrar fechas" : "Fechas de examen"}
            </button>
          </div>
        </div>
        ${
          editingDates
            ? `<form id="ing-dates-form" class="ing-dates-form">
                <label class="field">
                  <span>Matemática</span>
                  <input type="date" name="matematica" value="${esc(dates.matematica || "")}" />
                </label>
                <label class="field">
                  <span>Física</span>
                  <input type="date" name="fisica" value="${esc(dates.fisica || "")}" />
                </label>
                <label class="field">
                  <span>Comprensión Lectora</span>
                  <input type="date" name="clyrp" value="${esc(dates.clyrp || "")}" />
                </label>
                <div class="row" style="align-items:flex-end;">
                  <button type="submit" class="btn btn-primary btn-sm">Guardar fechas</button>
                </div>
              </form>`
            : ""
        }
      </div>`;

    planHost.querySelector("#ing-dates-toggle")?.addEventListener("click", () => {
      editingDates = !editingDates;
      renderPlanBar(s);
    });
    planHost.querySelector("#ing-dates-form")?.addEventListener("submit", async (e) => {
      e.preventDefault();
      const fd = new FormData(e.currentTarget);
      const nextDates = {
        matematica: String(fd.get("matematica") || "").trim(),
        fisica: String(fd.get("fisica") || "").trim(),
        clyrp: String(fd.get("clyrp") || "").trim(),
      };
      try {
        await api.put("/api/settings", { exam_dates: nextDates });
        toast("Plan actualizado con tus fechas de examen", "ok");
        await renderIngreso(container, { subject: state.subjectKey, unit: state.unitKey });
      } catch (err) {
        toast(err.message, "err");
      }
    });
  }

  function renderAll() {
    const s = subjects.find((x) => x.key === state.subjectKey) || subjects[0];
    const tone = toneOf(s.lab_type);
    const labHref = LAB_ROUTES[s.lab_type] || null;
    const totalPending = s.units.flatMap((u) => u.topics).filter((t) => !t.completed).length;
    const totalComplete = s.topics_total - totalPending;
    const totalDueTopics = s.units.flatMap((u) => u.topics).filter((t) => t.due_count > 0).length;

    modulesHost.innerHTML = renderModuleCards(data, s.key);
    renderPlanBar(s);
    modulesHost.querySelectorAll("[data-subject]").forEach((btn) => {
      btn.addEventListener("click", () => {
        const nextKey = btn.dataset.subject;
        if (nextKey === state.subjectKey) return;
        state.subjectKey = nextKey;
        state.filter = "all";
        state.query = "";
        const nextSub = subjects.find((x) => x.key === nextKey);
        state.unitKey = resolveInitialUnit(nextSub);
        writeStore(SUBJECT_KEY_STORAGE, nextKey);
        renderAll();
      });
    });

    const currentFrontierUnit =
      s.units.find((u) => s.next_action?.topic && u.topics.some((t) => t.node_id === s.next_action.topic.node_id)) ||
      s.units.find((u) => u.lessons_done < u.topics.length) ||
      s.units[0];

    workspaceHost.innerHTML = `
      <div class="ing-workspace stack-lg" data-tone="${tone}">
        <section class="card-tone ing-subject-banner">
          <div class="ing-subject-art" aria-hidden="true">${subjectArt(s.key)}</div>
          <div class="ing-subject-banner-top">
            <div class="stack-sm grow">
              <div class="row gap-sm">
                <h2 class="title-md m-0">${esc(s.name)}</h2>
                ${s.due_count > 0 ? `<span class="pill pill-amber">${s.due_count} ${s.due_count === 1 ? "repaso hoy" : "repasos hoy"}</span>` : ""}
              </div>
              <p class="m-0 small muted">${esc(s.exam)}</p>
            </div>
            <div class="ing-subject-metrics tabular">
              <div class="ing-metric">
                <strong>${s.lessons_done}/${s.topics_total}</strong>
                <span>lecciones</span>
              </div>
              <div class="ing-metric">
                <strong>${s.exercises_solved}/${s.exercises_total}</strong>
                <span>ejercicios</span>
              </div>
              <div class="ing-metric">
                <strong>${s.exercises_official}</strong>
                <span>de guías oficiales</span>
              </div>
            </div>
          </div>
          <div class="row-between ing-subject-actions">
            <div class="row">
              ${renderSubjectAction(s)}
              ${
                s.exercises_total >= 4
                  ? `<a class="btn btn-secondary" href="#/ejercicios/${esc(s.domain)}/simulacro?ingreso=1">${icon("target", 16)} Simulacro del programa</a>`
                  : ""
              }
              ${
                s.due_count > 0 && s.next_action?.kind !== "review"
                  ? `<a class="btn btn-secondary" href="#/review?domain=${esc(s.domain)}">${icon("brain", 16)} Repasar (${s.due_count})</a>`
                  : ""
              }
            </div>
            <div class="row gap-sm">
              ${labHref ? `<a class="btn btn-text btn-sm" href="${labHref}">${icon("flask", 14)} Laboratorio</a>` : ""}
              ${
                s.outside_count
                  ? `<a class="btn btn-text btn-sm" href="#/roadmap/${esc(s.domain)}">${icon("map", 14)} Ruta completa (+${s.outside_count} temas)</a>`
                  : `<a class="btn btn-text btn-sm" href="#/roadmap/${esc(s.domain)}">${icon("map", 14)} Ver ruta</a>`
              }
            </div>
          </div>
        </section>

        <nav class="ing-hub-bar" aria-label="Herramientas de estudio de ${esc(s.name)}">
          <a class="ing-hub-pill" href="#/formulario/${esc(s.domain)}">${icon("book", 15)}<span>Formulario imprimible</span></a>
          <a class="ing-hub-pill" href="#/errores?domain=${esc(s.domain)}">${icon("alert", 15)}<span>Banco de errores</span></a>
          <a class="ing-hub-pill" href="#/cuaderno?domain=${esc(s.domain)}">${icon("pen", 15)}<span>Cuaderno${s.bookmarked_count ? ` (${s.bookmarked_count} ★)` : ""}</span></a>
          <a class="ing-hub-pill" href="#/diagnostico/${esc(s.domain)}">${icon("compass", 15)}<span>Diagnóstico de nivel</span></a>
          <a class="ing-hub-pill" href="#/session?domains=matematicas,fisica,comprension-problemas">${icon("zap", 15)}<span>Sesión guiada Ingreso</span></a>
        </nav>

        <div class="roadmap-shell has-sidebar ing-shell">
          <aside class="roadmap-sidebar ing-sidebar" aria-label="Unidades de ${esc(s.name)}">
            <div class="stage-sidebar-head">
              <span class="eyebrow m-0">Unidades del programa</span>
              <span class="xs muted tabular">${s.units.length}</span>
            </div>
            <nav class="stage-nav" id="ing-unit-nav">
              ${s.units
                .map((u) => {
                  const isActive = state.unitKey === u.code;
                  const isComplete = u.topics.length > 0 && u.topics.every((t) => t.completed);
                  const isFrontier = currentFrontierUnit && u.code === currentFrontierUnit.code;
                  return `
                  <button
                    type="button"
                    class="stage-btn ${isActive ? "active" : ""} ${isComplete ? "is-complete" : ""}"
                    data-unit="${esc(u.code)}"
                    aria-current="${isActive ? "true" : "false"}"
                  >
                    <span class="stage-idx tabular" aria-hidden="true">${isComplete ? icon("check", 13) : esc(u.code)}</span>
                    <span class="stage-info">
                      <span class="stage-name">${esc(u.short_title)}</span>
                      ${
                        u.progress_pct > 0 && !isComplete
                          ? `<span class="stage-micro-bar"><span style="width:${u.progress_pct}%;"></span></span>`
                          : isFrontier
                          ? `<span class="stage-current-tag">Tu unidad actual</span>`
                          : ""
                      }
                    </span>
                    <span class="ing-unit-side-meta tabular">
                      ${u.due_count > 0 ? `<span class="ing-due-dot" title="${u.due_count} repasos pendientes"></span>` : ""}
                      <span class="stage-count">${u.lessons_done}/${u.topics.length}</span>
                    </span>
                  </button>`;
                })
                .join("")}
            </nav>
            <div class="stage-sidebar-foot">
              <button
                type="button"
                class="stage-all-btn ${state.unitKey === ALL_UNITS ? "active" : ""}"
                data-unit="${ALL_UNITS}"
              >
                ${icon("layers", 15)}
                <span>Todas las unidades</span>
                <span class="stage-count tabular">${s.topics_total}</span>
              </button>
            </div>
          </aside>

          <div class="roadmap-main">
            <div class="stage-mobile-bar">
              <select class="stage-select" id="ing-unit-select" aria-label="Elegir unidad">
                ${s.units
                  .map(
                    (u) =>
                      `<option value="${esc(u.code)}" ${state.unitKey === u.code ? "selected" : ""}>${esc(u.code)} · ${esc(u.short_title)} (${u.lessons_done}/${u.topics.length})</option>`
                  )
                  .join("")}
                <option value="${ALL_UNITS}" ${state.unitKey === ALL_UNITS ? "selected" : ""}>Todas las unidades (${s.topics_total} temas)</option>
              </select>
            </div>

            <div class="roadmap-toolbar">
              <label class="roadmap-search" aria-label="Buscar tema en ${esc(s.name)}">
                ${icon("search", 16, "roadmap-search-ico")}
                <input type="search" id="ing-search" placeholder="Buscar tema en ${esc(SHORT_SUBJECT_NAME[s.key] || s.name)}…" value="${esc(state.query)}" autocomplete="off" />
                <button type="button" class="roadmap-search-clear" id="ing-search-clear" aria-label="Borrar búsqueda" ${state.query ? "" : "hidden"}>${icon("x", 14)}</button>
              </label>
              <div class="segmented" role="group" aria-label="Filtrar temas">
                <button type="button" class="seg-btn ${state.filter === "all" ? "active" : ""}" data-filter="all">Todos</button>
                <button type="button" class="seg-btn ${state.filter === "pending" ? "active" : ""}" data-filter="pending">Pendientes (${totalPending})</button>
                ${
                  totalDueTopics > 0
                    ? `<button type="button" class="seg-btn ${state.filter === "due" ? "active" : ""}" data-filter="due">Con repaso (${totalDueTopics})</button>`
                    : ""
                }
                ${
                  s.bookmarked_count > 0
                    ? `<button type="button" class="seg-btn ${state.filter === "bookmarked" ? "active" : ""}" data-filter="bookmarked">Marcados ★ (${s.bookmarked_count})</button>`
                    : ""
                }
                <button type="button" class="seg-btn ${state.filter === "done" ? "active" : ""}" data-filter="done">Completos (${totalComplete})</button>
              </div>
            </div>

            <div id="ing-unit-body" class="stack"></div>
          </div>
        </div>
      </div>
    `;

    const unitBody = workspaceHost.querySelector("#ing-unit-body");
    const searchInput = workspaceHost.querySelector("#ing-search");
    const searchClear = workspaceHost.querySelector("#ing-search-clear");
    const unitSelect = workspaceHost.querySelector("#ing-unit-select");

    function matchesFilter(t) {
      if (state.filter === "pending") return !t.completed;
      if (state.filter === "due") return t.due_count > 0;
      if (state.filter === "bookmarked") return Boolean(t.bookmarked);
      if (state.filter === "done") return t.completed;
      return true;
    }

    function matchesQuery(t, unit, q) {
      if (!q) return true;
      return normSearch(`${t.title} ${t.summary} ${unit.title}`).includes(q);
    }

    function updateUnitBody() {
      const q = normSearch(state.query);
      const isFiltering = Boolean(q) || state.filter !== "all";

      // Update sidebar + select active styling
      workspaceHost.querySelectorAll("[data-unit]").forEach((btn) => {
        const on = btn.dataset.unit === state.unitKey;
        btn.classList.toggle("active", on);
        if (btn.classList.contains("stage-btn")) btn.setAttribute("aria-current", on ? "true" : "false");
      });
      if (unitSelect) unitSelect.value = state.unitKey;
      workspaceHost.querySelectorAll("[data-filter]").forEach((btn) => {
        btn.classList.toggle("active", btn.dataset.filter === state.filter);
      });
      if (searchClear) searchClear.hidden = !state.query;

      // Searching scans the whole subject so learners never get stuck inside one unit
      if (q || state.unitKey === ALL_UNITS) {
        const blocks = [];
        let matchedCount = 0;
        for (const u of s.units) {
          const matching = u.topics.filter((t) => matchesFilter(t) && matchesQuery(t, u, q));
          if (!matching.length) continue;
          matchedCount += matching.length;
          blocks.push(`
            <section class="stack-sm">
              <div class="stage-header-inline stage-all-heading">
                <div class="row gap-sm">
                  <span class="pill pill-tone tabular">${esc(u.code)}</span>
                  <h3 class="title-sm m-0">${esc(u.short_title)}</h3>
                </div>
                <span class="xs muted tabular">${u.lessons_done}/${u.topics.length} lecciones · ${u.exercises_solved}/${u.exercises_total} ej. · ${u.progress_pct} %</span>
              </div>
              <div class="curriculum-panel">
                ${matching.map((t, i) => renderTopicRow(t, s.domain, i)).join("")}
              </div>
            </section>`);
        }

        if (!blocks.length) {
          unitBody.innerHTML = `
            <div class="empty stack-sm">
              <p class="m-0">No hay temas que coincidan con ${q ? `«${esc(state.query)}»` : "este filtro"} en ${esc(s.name)}.</p>
              <div><button type="button" class="btn btn-secondary btn-sm" id="ing-reset-filters">Limpiar filtros</button></div>
            </div>`;
          unitBody.querySelector("#ing-reset-filters")?.addEventListener("click", () => {
            state.query = "";
            state.filter = "all";
            if (searchInput) searchInput.value = "";
            updateUnitBody();
          });
          return;
        }

        const headerCopy = q
          ? `<div class="xs muted">${matchedCount} ${matchedCount === 1 ? "tema encontrado" : "temas encontrados"} en ${esc(s.name)}</div>`
          : `<div class="ing-legend xs muted">Cada tema se domina en 3 pasos: <strong>1. Lección</strong> → <strong>2. Repaso</strong> → <strong>3. Ejercicios</strong> (${icon("book", 12)} incluye guías oficiales).</div>`;
        unitBody.innerHTML = `${headerCopy}${blocks.join("")}`;
        return;
      }

      // Focused single-unit view
      const uIdx = s.units.findIndex((u) => u.code === state.unitKey);
      const unit = s.units[uIdx] || s.units[0];
      if (!unit) return;
      const visible = unit.topics.filter(matchesFilter);
      const estLabel = formatEstTime(unit.est_minutes);

      // Spotlight the first pending/due topic in this unit when unfiltered
      const spotIdx = !isFiltering
        ? unit.topics.findIndex((t) => t.due_count > 0) !== -1
          ? unit.topics.findIndex((t) => t.due_count > 0)
          : unit.topics.findIndex((t) => !t.completed)
        : -1;
      const spotTopic = spotIdx >= 0 ? unit.topics[spotIdx] : null;
      const restTopics = spotTopic ? visible.filter((t) => t.node_id !== spotTopic.node_id) : visible;

      const prevUnit = uIdx > 0 ? s.units[uIdx - 1] : null;
      const nextUnit = uIdx < s.units.length - 1 ? s.units[uIdx + 1] : null;

      unitBody.innerHTML = `
        <header class="stage-header">
          <div class="stage-header-top">
            <div>
              <div class="eyebrow m-0" style="margin-bottom:4px;">${esc(unit.title.split("·")[0]?.trim() || unit.code)}</div>
              <h3 class="title-md m-0">${esc(unit.short_title)}</h3>
            </div>
            <span class="num num-md tabular" style="color:var(--tone, var(--accent));">${unit.progress_pct} %</span>
          </div>
          <div class="row xs muted tabular" style="gap:8px 14px;">
            <span>${unit.lessons_done}/${unit.topics.length} lecciones</span>
            <span>·</span>
            <span>${unit.exercises_solved}/${unit.exercises_total} ejercicios${unit.exercises_official ? ` (${unit.exercises_official} oficiales)` : ""}</span>
            ${estLabel ? `<span>·</span><span>${estLabel} de lectura</span>` : ""}
            ${unit.due_count > 0 ? `<span>·</span><span style="color:var(--warn);font-weight:500;">${unit.due_count} repasos hoy</span>` : ""}
          </div>
          <div class="progress-track stage-progress"><div class="progress-fill" style="width:${unit.progress_pct}%;"></div></div>
        </header>

        <div class="ing-legend xs muted">
          <span>Pasos por tema: <strong>1. Lección</strong> → <strong>2. Repaso</strong> → <strong>3. Ejercicios</strong></span>
          <span>·</span>
          <span>${icon("book", 12)} incluye guías oficiales</span>
        </div>

        ${spotTopic ? renderSpotlight(spotTopic, s.domain, spotIdx) : ""}

        ${
          restTopics.length
            ? `<div class="curriculum-panel">
                ${restTopics
                  .map((t) => renderTopicRow(t, s.domain, unit.topics.indexOf(t)))
                  .join("")}
              </div>`
            : !spotTopic
            ? `<div class="empty stack-sm">
                <p class="m-0">No hay temas en esta unidad que coincidan con el filtro seleccionado.</p>
                <div><button type="button" class="btn btn-secondary btn-sm" id="ing-reset-unit-filter">Ver todos los de la unidad</button></div>
              </div>`
            : ""
        }

        ${
          prevUnit || nextUnit
            ? `<nav class="stage-footer" aria-label="Navegar entre unidades">
                ${
                  prevUnit
                    ? `<button type="button" class="stage-footer-btn" data-jump-unit="${esc(prevUnit.code)}">
                        <span class="xs muted">${icon("arrowLeft", 13)} Unidad anterior</span>
                        <strong>${esc(prevUnit.code)} · ${esc(prevUnit.short_title)}</strong>
                      </button>`
                    : `<div></div>`
                }
                ${
                  nextUnit
                    ? `<button type="button" class="stage-footer-btn is-next" data-jump-unit="${esc(nextUnit.code)}">
                        <span class="xs muted">Siguiente unidad ${icon("arrowRight", 13)}</span>
                        <strong>${esc(nextUnit.code)} · ${esc(nextUnit.short_title)}</strong>
                      </button>`
                    : `<div></div>`
                }
              </nav>`
            : ""
        }
      `;

      unitBody.querySelector("#ing-reset-unit-filter")?.addEventListener("click", () => {
        state.filter = "all";
        updateUnitBody();
      });
      unitBody.querySelectorAll("[data-jump-unit]").forEach((btn) => {
        btn.addEventListener("click", () => {
          state.unitKey = btn.dataset.jumpUnit;
          writeStore(unitStorageKey(s.key), state.unitKey);
          updateUnitBody();
          workspaceHost.querySelector(".ing-shell")?.scrollIntoView({ behavior: "smooth", block: "start" });
        });
      });
    }

    // Bind unit & filter controls
    workspaceHost.querySelectorAll("[data-unit]").forEach((btn) => {
      btn.addEventListener("click", () => {
        state.unitKey = btn.dataset.unit;
        state.query = "";
        if (searchInput) searchInput.value = "";
        writeStore(unitStorageKey(s.key), state.unitKey);
        updateUnitBody();
      });
    });

    unitSelect?.addEventListener("change", () => {
      state.unitKey = unitSelect.value;
      state.query = "";
      if (searchInput) searchInput.value = "";
      writeStore(unitStorageKey(s.key), state.unitKey);
      updateUnitBody();
    });

    workspaceHost.querySelectorAll("[data-filter]").forEach((btn) => {
      btn.addEventListener("click", () => {
        state.filter = btn.dataset.filter;
        updateUnitBody();
      });
    });

    searchInput?.addEventListener("input", () => {
      state.query = searchInput.value;
      updateUnitBody();
    });

    searchClear?.addEventListener("click", () => {
      state.query = "";
      if (searchInput) {
        searchInput.value = "";
        searchInput.focus();
      }
      updateUnitBody();
    });

    unitBody?.addEventListener("click", async (e) => {
      const btn = e.target.closest("[data-bookmark-node]");
      if (!btn) return;
      const nid = Number(btn.dataset.bookmarkNode);
      const topic = s.units.flatMap((u) => u.topics).find((t) => t.node_id === nid);
      if (!topic) return;
      const next = !topic.bookmarked;
      try {
        await api.put(`/api/notes/${nid}`, { bookmarked: next });
        topic.bookmarked = next;
        s.bookmarked_count = s.units.flatMap((u) => u.topics).filter((t) => t.bookmarked).length;
        toast(next ? "Tema marcado ★ para antes del parcial" : "Marca quitada", "ok");
        renderAll();
      } catch (err) {
        toast(err.message, "err");
      }
    });

    updateUnitBody();
  }

  renderAll();
}
