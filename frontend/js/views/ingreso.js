import { icon } from "../icons.js";
import { api, esc, toneOf } from "../main.js";

/**
 * The UNCuyo 2027 entrance course: each subject with its official units, and for every
 * topic the lesson, the review practice and the exercises. It answers "what is left before
 * the exam?" without the rest of the app's (much wider) curriculum in the way.
 */

const stripNumber = (title) => String(title || "").replace(/^\d+\.\s*/, "");

function topicRow(t, domain) {
  const lesson = t.lesson_completed
    ? `<span class="pill pill-green">${icon("check", 12)} Lección</span>`
    : `<a class="pill" href="#/learn/${t.node_id}">Lección pendiente</a>`;
  const practice = t.cards
    ? `<a class="pill ${t.practiced_pct >= 60 ? "pill-green" : ""}" href="#/review?node=${t.node_id}" title="Tarjetas de repaso practicadas">Repaso ${t.practiced_pct} %${t.due_count ? ` · ${t.due_count} hoy` : ""}</a>`
    : "";
  const exercises = t.exercises_total
    ? `<a class="pill ${t.exercises_solved === t.exercises_total ? "pill-green" : ""}" href="#/ejercicios/${esc(domain)}/${esc(t.slug)}" title="${t.exercises_official ? `${t.exercises_official} de las guías oficiales` : ""}">Ejercicios ${t.exercises_solved}/${t.exercises_total}${t.exercises_official ? ` ${icon("book", 12)}` : ""}</a>`
    : "";
  return `
    <div class="list-row ing-topic">
      <a class="grow list-title ing-topic-title" href="#/learn/${t.node_id}">${esc(stripNumber(t.title))}</a>
      <div class="row ing-pills">${lesson}${practice}${exercises}</div>
    </div>`;
}

function subjectBlock(s) {
  const tone = toneOf(s.lab_type);
  const firstOpen = s.units.findIndex((u) => u.lessons_done < u.topics.length);
  return `
    <section class="stack ing-subject" data-tone="${tone}">
      <div class="card-tone stack">
        <div class="row-between row-top">
          <div class="stack-sm">
            <h2 class="title-md m-0">${esc(s.name)}</h2>
            <p class="m-0 small muted">${esc(s.exam)}</p>
          </div>
          <strong class="ing-pct tabular">${s.progress_pct} %</strong>
        </div>
        <div class="progress-track"><div class="progress-fill" style="width:${s.progress_pct}%;"></div></div>
        <div class="row small">
          <span>${s.lessons_done} de ${s.topics_total} lecciones</span>
          <span class="muted">·</span>
          <span>${s.exercises_solved} de ${s.exercises_total} ejercicios${s.exercises_official ? ` (${s.exercises_official} de las guías oficiales)` : ""}</span>
        </div>
        <div class="row">
          ${s.next_topic ? `<a class="btn btn-primary" href="#/learn/${s.next_topic.node_id}">Seguir: ${esc(stripNumber(s.next_topic.title))} ${icon("arrowRight", 16)}</a>` : ""}
          ${s.exercises_total >= 4 ? `<a class="btn btn-secondary" href="#/ejercicios/${esc(s.domain)}/simulacro?ingreso=1">${icon("target", 16)} Simulacro del programa</a>` : ""}
        </div>
      </div>
      ${s.units
        .map(
          (u, i) => `
        <details class="card ing-unit" ${i === Math.max(firstOpen, 0) ? "open" : ""}>
          <summary class="row-between ing-unit-head">
            <span class="list-title">${esc(u.title)}</span>
            <span class="small muted tabular">${u.lessons_done}/${u.topics.length} lecciones · ${u.progress_pct} %</span>
          </summary>
          <div class="list">${u.topics.map((t) => topicRow(t, s.domain)).join("")}</div>
        </details>`
        )
        .join("")}
      ${
        s.outside_count
          ? `<p class="small muted m-0">La ruta de ${esc(s.name)} tiene además ${s.outside_count} temas que no entran en el ingreso: sirven de base o para después. <a href="#/roadmap/${esc(s.domain)}">Ver la ruta completa</a></p>`
          : ""
      }
    </section>`;
}

export async function renderIngreso(container) {
  const data = await api.get("/api/ingreso");
  container.innerHTML = `
    <div class="page-header">
      <div>
        <h1>${esc(data.title)}</h1>
        <p class="muted">${esc(data.summary)} Acá está solo lo que entra, ordenado como el programa oficial.</p>
      </div>
    </div>
    <div class="stack-lg">${data.subjects.map(subjectBlock).join("")}</div>
  `;
}
