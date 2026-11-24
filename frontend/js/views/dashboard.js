import { icon } from "../icons.js";
import { subjectArt, subjectLogo } from "../art.js";
import { api, esc, refreshSidebarDomains, toneOf } from "../main.js";
import { renderExamTrendSvg } from "./exercises.js";

function fmtStudyDuration(sec) {
  const s = Math.max(0, Math.round(sec || 0));
  if (s < 60) return `${s} s`;
  const mins = Math.round(s / 60);
  if (mins < 60) return `${mins} min`;
  const h = Math.floor(mins / 60);
  const rem = mins % 60;
  return rem ? `${h} h ${rem} m` : `${h} h`;
}

function heatLevel(count) {
  if (count <= 0) return 0;
  if (count <= 2) return 1;
  if (count <= 5) return 2;
  if (count <= 10) return 3;
  return 4;
}

const stripNum = (title) => String(title || "").replace(/^\d+\.\s*/, "");

function todayLabel() {
  const txt = new Intl.DateTimeFormat("es", { weekday: "long", day: "numeric", month: "long" }).format(new Date());
  return txt.charAt(0).toUpperCase() + txt.slice(1);
}

/** First visit: explain the loop and let the learner pick where to start. */
function renderWelcome(container, { domains, next_steps }) {
  container.innerHTML = `
    <section class="band dots page-header" data-tone="brand" style="align-items:flex-start;">
      <div>
        <div class="eyebrow"><span class="eyebrow-dot"></span>Bienvenido a AprendeLab</div>
        <h1 class="hero-title">Aprendé de verdad,<br><em>no de memoria</em>.</h1>
        <p class="hero-lead">Lecciones cortas, práctica con las manos y repasos justo antes de que te olvides.</p>
        <a href="#start" class="btn btn-primary btn-lg" id="welcome-start">Elegir una materia ${icon("arrowDown", 18)}</a>
      </div>
    </section>

    <section class="section" style="padding-top:28px;">
      <div class="grid-3">
        <div class="stack-sm">
          <span class="num num-lg" style="color:var(--accent);">1</span>
          <h3 class="m-0">Aprendé una lección</h3>
          <p class="muted m-0">Diez a veinte minutos: la idea, un ejemplo y tres preguntas para comprobar que la entendiste.</p>
        </div>
        <div class="stack-sm">
          <span class="num num-lg" style="color:var(--accent);">2</span>
          <h3 class="m-0">Practicá en el laboratorio</h3>
          <p class="muted m-0">Metrónomo, simuladores y ejercicios que se corrigen solos.</p>
        </div>
        <div class="stack-sm">
          <span class="num num-lg" style="color:var(--accent);">3</span>
          <h3 class="m-0">Repasá cuando toca</h3>
          <p class="muted m-0">La app te trae cada tema justo antes de que lo olvides. Unos minutos por día alcanzan.</p>
        </div>
      </div>
    </section>

    <section class="section" id="start">
      <div class="section-head">
        <h2>¿Por dónde querés empezar?</h2>
        <p class="section-sub">Podés llevar varias materias a la vez. Elegí una para ver su ruta de aprendizaje.</p>
      </div>
      <div class="grid-2">
        ${domains
          .map((d) => {
            const tone = toneOf(d.lab_type);
            const next = next_steps[d.slug];
            const href = `#/roadmap/${esc(d.slug)}`;
            return `
            <a href="${href}" class="tile" data-tone="${tone}">
              <div class="tile-art">${subjectArt(d.slug || tone)}</div>
              <div class="stack-sm">
                <h3 class="tile-title">${esc(d.name)}</h3>
                <p class="m-0 muted">${next ? `Empieza con: ${esc(stripNum(next.node_title))}` : esc(d.description)}</p>
              </div>
              <div class="tile-foot">
                <span class="small">${d.node_count} lecciones · Ver ruta</span>
                ${icon("arrowRight", 20)}
              </div>
            </a>`;
          })
          .join("")}
      </div>
    </section>
  `;
  container.querySelector("#welcome-start")?.addEventListener("click", (e) => {
    e.preventDefault();
    container.querySelector("#start")?.scrollIntoView({ behavior: "smooth", block: "start" });
  });
}

export async function renderDashboard(container) {
  const [data, settingsRes, analytics] = await Promise.all([
    api.get("/api/dashboard"),
    api.get("/api/settings").catch(() => ({ settings: {} })),
    api.get("/api/analytics").catch(() => null),
  ]);
  const {
    domains,
    summary,
    heatmap,
    forecast_14d = [],
    recent_metrics = [],
    feynman_journal = [],
    calibration = {},
    next_steps = {},
    remediation_alerts = [],
  } = data;
  const ingresoFocus = Boolean(settingsRes?.settings?.ingreso_focus_mode);
  const INGRESO_SLUGS = new Set(["matematicas", "fisica", "comprension-problemas"]);
  const visibleDomains = ingresoFocus ? domains.filter((d) => INGRESO_SLUGS.has(d.slug)) : domains;
  await refreshSidebarDomains();

  if (summary.is_first_run) {
    renderWelcome(container, data);
    return;
  }

  const toReview = summary.total_due + summary.new_today;
  const estMinutes = Math.max(1, Math.round((toReview * 40) / 60));
  // The most useful next lesson: prefer a discipline the learner already started (and Ingreso if focus mode is on)
  const lessonCandidates = (visibleDomains.length ? visibleDomains : domains)
    .map((d) => ({ d, next: next_steps[d.slug] }))
    .filter((x) => x.next && !x.next.lesson_completed)
    .sort((a, b) => b.d.lessons_completed - a.d.lessons_completed);
  const nextLesson = lessonCandidates[0] || null;

  let headline;
  let detail;
  let primary;
  let secondary = "";
  if (toReview > 0) {
    headline = toReview === 1 ? "Tenés <em>1 repaso</em> para hoy." : `Tenés <em>${toReview} repasos</em> para hoy.`;
    const parts = [];
    if (summary.total_due) parts.push(`${summary.total_due} que ya viste`);
    if (summary.new_today) parts.push(`${summary.new_today} ${summary.new_today === 1 ? "nueva" : "nuevas"}`);
    detail = `${parts.join(" y ")} · ${estMinutes === 1 ? "un minuto" : `unos ${estMinutes} minutos`}.`;
    primary = `<a href="#/review" class="btn btn-primary btn-lg">Empezar el repaso ${icon("arrowRight", 18)}</a>`;
    if (nextLesson) {
      secondary = `<a href="#/learn/${nextLesson.next.node_id}" class="btn btn-secondary btn-lg">Aprender algo nuevo</a>`;
    }
  } else if (nextLesson) {
    headline = "Estás al día. <em>Aprendé algo nuevo</em>.";
    detail = `Tu próxima lección: ${esc(stripNum(nextLesson.next.node_title))} (${esc(nextLesson.d.name)}).`;
    primary = `<a href="#/learn/${nextLesson.next.node_id}" class="btn btn-primary btn-lg">Empezar la lección ${icon("arrowRight", 18)}</a>`;
    secondary = `<a href="#/labs" class="btn btn-secondary btn-lg">Practicar en un laboratorio</a>`;
  } else {
    headline = "Estás al día. <em>Buen trabajo</em>.";
    detail = "No hay repasos pendientes ni lecciones nuevas. Podés practicar en un laboratorio o hacer práctica extra.";
    primary = `<a href="#/labs" class="btn btn-primary btn-lg">Ir a los laboratorios ${icon("arrowRight", 18)}</a>`;
    secondary = `<a href="#/review?mode=practice_all" class="btn btn-secondary btn-lg">Práctica extra</a>`;
  }

  const maxForecast = Math.max(1, ...forecast_14d.map((f) => f.count));
  const upcoming = forecast_14d.slice(1).reduce((a, f) => a + f.count, 0);
  const activeDays = heatmap.filter((c) => c.count > 0).length;
  const todayIso = heatmap.length ? heatmap[heatmap.length - 1].date : "";

  container.innerHTML = `
    <section class="page-header" style="align-items:flex-end;">
      <div>
        <div class="eyebrow">${todayLabel()}</div>
        <h1 class="hero-title">${headline}</h1>
        <p class="hero-lead">${detail}</p>
        <div class="row">${primary}${secondary}</div>
      </div>
      <div class="row" style="gap:32px;">
        <div class="stat">
          <span class="num num-xl">${summary.today_reviews}</span>
          <span class="stat-label">repasos hoy</span>
        </div>
        <div class="stat">
          <span class="num num-xl">${summary.streak_days}</span>
          <span class="stat-label">${summary.streak_days === 1 ? "día seguido" : "días seguidos"}</span>
        </div>
        <div class="stat">
          <span class="num num-xl">${summary.lessons_completed}<span class="muted" style="font-size:0.5em;"> / ${summary.total_lessons}</span></span>
          <span class="stat-label">lecciones</span>
        </div>
        ${
          analytics?.study_time
            ? `<div class="stat">
                <span class="num num-xl">${esc(fmtStudyDuration(analytics.study_time.week_sec))}</span>
                <span class="stat-label">esta semana (${esc(fmtStudyDuration(analytics.study_time.today_sec))} hoy)</span>
              </div>`
            : ""
        }
      </div>
    </section>

    ${
      analytics?.error_totals?.weak_exercises > 0
        ? `<section class="card callout-info row-between mb-lg">
            <div>
              <strong>${
                analytics.error_totals.due_retries > 0
                  ? `${analytics.error_totals.due_retries} ${analytics.error_totals.due_retries === 1 ? "ejercicio vencido" : "ejercicios vencidos"} para reintentar hoy`
                  : `${analytics.error_totals.weak_exercises} ${analytics.error_totals.weak_exercises === 1 ? "ejercicio" : "ejercicios"} en tu cola de reintentos`
              }</strong>
              <p class="xs muted m-0">Todo lo que fallaste o miraste con solución vuelve solo hasta que te salga sin ayuda.</p>
            </div>
            <a href="#/ejercicios/reintentos" class="btn btn-primary btn-sm">${icon("refresh", 14)} Reintentar ahora</a>
          </section>`
        : ""
    }

    ${
      remediation_alerts.length
        ? `<section class="card callout-warn stack mb-lg">
            <h3 class="m-0">${icon("alert", 16)} Conviene reforzar la base</h3>
            ${remediation_alerts
              .map(
                (a) => `
              <div class="row-between">
                <span><strong>${esc(a.domain_name)}:</strong> ${esc(a.reason)}</span>
                <a href="#/roadmap/${esc(a.domain_slug)}" class="btn btn-secondary btn-sm">Ver la ruta</a>
              </div>`
              )
              .join("")}
          </section>`
        : ""
    }

    <section class="section section-tight" style="padding-top:8px;">
      <div class="section-head">
        <h2>${ingresoFocus ? "Materias del Ingreso" : "Tus materias"}</h2>
        <div class="row gap-sm">
          <button type="button" id="dash-ingreso-focus" class="btn btn-sm ${ingresoFocus ? "btn-primary" : "btn-secondary"}" aria-pressed="${ingresoFocus}">
            ${icon("target", 14)} ${ingresoFocus ? "Solo Ingreso: ON" : "Modo Solo Ingreso"}
          </button>
          <a href="#/ingreso" class="btn-text btn">Ir a Ingreso</a>
          ${ingresoFocus ? "" : `<a href="#/aprender" class="btn-text btn">Ver todas</a>`}
        </div>
      </div>
      ${
        ingresoFocus
          ? `<div class="ing-hub-bar mb-md">
              <a class="ing-hub-pill" href="#/formulario/matematicas">${icon("book", 14)}<span>Formulario</span></a>
              <a class="ing-hub-pill" href="#/errores">${icon("alert", 14)}<span>Banco de errores</span></a>
              <a class="ing-hub-pill" href="#/cuaderno">${icon("pen", 14)}<span>Cuaderno</span></a>
              <a class="ing-hub-pill" href="#/session?domains=matematicas,fisica,comprension-problemas">${icon("zap", 14)}<span>Sesión Ingreso</span></a>
            </div>`
          : ""
      }
      <div class="card">
        <div class="list">
          ${visibleDomains
            .map((d) => {
              const tone = toneOf(d.lab_type);
              const next = next_steps[d.slug];
              const allLessons = d.node_count > 0 && d.lessons_completed >= d.node_count;
              const roadmapHref = `#/roadmap/${esc(d.slug)}`;
              let action;
              let sub;
              if (d.due_count > 0) {
                sub = `${d.due_count} ${d.due_count === 1 ? "repaso pendiente" : "repasos pendientes"}`;
                action = `<a href="#/review?domain=${esc(d.slug)}" class="btn btn-secondary btn-sm">Repasar (${d.due_count})</a>`;
              } else if (d.new_count > 0 && summary.new_today > 0) {
                sub = `${d.new_count} ${d.new_count === 1 ? "tarjeta nueva" : "tarjetas nuevas"} para practicar`;
                action = `<a href="${roadmapHref}" class="btn btn-secondary btn-sm">Ver ruta ${icon("arrowRight", 14)}</a>`;
              } else if (next && !next.lesson_completed) {
                sub = `Próxima lección: ${esc(stripNum(next.node_title))}`;
                action = `<a href="${roadmapHref}" class="btn btn-secondary btn-sm">Ver ruta ${icon("arrowRight", 14)}</a>`;
              } else if (allLessons) {
                sub = "Lecciones completas · al día";
                action = `<a href="${roadmapHref}" class="btn btn-secondary btn-sm">Ver ruta ${icon("arrowRight", 14)}</a>`;
              } else {
                sub = next ? `En práctica: ${esc(stripNum(next.node_title))}` : "Sin lecciones todavía";
                action = `<a href="${roadmapHref}" class="btn btn-secondary btn-sm">Ver ruta ${icon("arrowRight", 14)}</a>`;
              }
              const pct = d.node_count ? Math.round((d.lessons_completed / d.node_count) * 100) : 0;
              return `
              <div class="list-row subject-row" data-tone="${tone}">
                <a href="${roadmapHref}" class="subject-row-link">
                  <span class="domain-icon-box">${subjectLogo(d.slug || d.lab_type, 22)}</span>
                  <div class="grow">
                    <div class="list-title">${esc(d.name)}</div>
                    <div class="muted small truncate">${sub}</div>
                  </div>
                  <div class="subject-row-progress" title="${d.lessons_completed} de ${d.node_count} lecciones">
                    <div class="xs muted tabular" style="margin-bottom:6px;">${d.lessons_completed} de ${d.node_count} lecciones</div>
                    <div class="progress-track"><div class="progress-fill" style="width:${pct}%;"></div></div>
                  </div>
                </a>
                ${action}
              </div>`;
            })
            .join("")}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="section-head">
        <h2>Tu progreso</h2>
        <p class="section-sub">${summary.total_reviews} repasos en total${
          summary.overall_memory_health_pct !== null ? ` · recordás cerca del ${summary.overall_memory_health_pct}% de lo que estudiaste` : ""
        }.</p>
      </div>

      <div class="grid-2">
        <div class="card stack">
          <div>
            <h3>Próximos 14 días</h3>
            <p class="muted small m-0">${
              upcoming > 0
                ? `${upcoming} ${upcoming === 1 ? "repaso agendado" : "repasos agendados"} después de hoy.`
                : "Todavía no hay repasos agendados: aparecen cuando calificás tus primeras tarjetas."
            }</p>
          </div>
          ${
            upcoming > 0 || forecast_14d[0]?.count
              ? `<div class="forecast-bars" role="img" aria-label="Repasos agendados por día en los próximos 14 días">
                  ${forecast_14d
                    .map((f, i) => {
                      const h = f.count > 0 ? Math.max(10, Math.round((f.count / maxForecast) * 72)) : 3;
                      return `
                      <div class="forecast-col ${i === 0 ? "today" : ""}" title="${esc(f.date)}: ${f.count}">
                        <div class="forecast-bar" style="height:${h}px;"></div>
                        <span class="forecast-lbl">${i === 0 ? "Hoy" : i % 3 === 0 ? `+${i}` : ""}</span>
                      </div>`;
                    })
                    .join("")}
                </div>`
              : ""
          }
        </div>

        <div class="card stack">
          <div>
            <h3>Constancia</h3>
            <p class="muted small m-0">${
              activeDays > 0
                ? `Estudiaste ${activeDays} ${activeDays === 1 ? "día" : "días"} de los últimos 56.`
                : "Cada día que estudies se va a marcar acá."
            }</p>
          </div>
          <div class="heatmap-grid" role="img" aria-label="Días con actividad en las últimas 8 semanas">
            ${heatmap
              .map(
                (c) =>
                  `<span class="heat-cell ${c.date === todayIso ? "today" : ""}" data-level="${heatLevel(c.count)}" title="${esc(c.date)}: ${c.count}"></span>`
              )
              .join("")}
          </div>
        </div>

        <div class="card stack">
          <div>
            <h3>¿Sabés lo que creés que sabés?</h3>
            <p class="muted small m-0">Antes de cada respuesta decís qué tan seguro estás. Acá se compara con lo que pasó.</p>
          </div>
          ${
            calibration.total_checked
              ? `<div class="row" style="gap:36px;">
                  <div class="stat">
                    <span class="num num-lg">${calibration.calibrated_pct}%</span>
                    <span class="stat-label">de aciertos en tu predicción</span>
                  </div>
                  <div class="stat">
                    <span class="num num-lg" style="color:${calibration.overconfident_lapses ? "var(--danger)" : "inherit"};">${calibration.overconfident_lapses}</span>
                    <span class="stat-label">veces muy seguro y falló</span>
                  </div>
                </div>`
              : `<div class="empty">Aparece después de tus primeros repasos.</div>`
          }
        </div>

        <div class="card stack">
          <h3 class="m-0">Últimos logros en laboratorios</h3>
          ${
            recent_metrics.length
              ? `<div class="list">
                  ${recent_metrics
                    .slice(0, 4)
                    .map(
                      (m) => `
                    <div class="list-row" style="padding:12px 0;">
                      <div class="grow">
                        <div class="truncate">${esc(m.label || m.metric_type)}</div>
                        <div class="xs muted">${esc(m.domain_name)} · ${esc(m.created_at.slice(0, 10))}</div>
                      </div>
                      <span class="num num-md">${m.value}</span><span class="xs muted">${esc(m.unit)}</span>
                    </div>`
                    )
                    .join("")}
                </div>`
              : `<div class="empty">Tus marcas del metrónomo, los cambios de acordes y los ejercicios resueltos se guardan acá.</div>`
          }
        </div>

        ${
          analytics
            ? `<div class="card stack">
                <div class="row-between">
                  <div>
                    <h3 class="m-0">Dominio real de ejercicios</h3>
                    <p class="muted small m-0">Resueltos sin ayuda vs. mirando la solución o en intento.</p>
                  </div>
                  ${
                    analytics.error_totals?.weak_exercises
                      ? `<a href="#/errores" class="btn btn-secondary btn-sm">Errores (${analytics.error_totals.weak_exercises})</a>`
                      : ""
                  }
                </div>
                <div class="stack-sm">
                  ${(analytics.subjects || [])
                    .map((s) => {
                      const tot = Math.max(1, s.total || 0);
                      const pUnaided = Math.round((100 * s.unaided) / tot);
                      const pAssisted = Math.round((100 * s.assisted) / tot);
                      const pTried = Math.round((100 * s.unsolved_tried) / tot);
                      return `
                      <div class="stack-sm" style="gap:4px;">
                        <div class="row-between xs">
                          <strong>${esc(s.name)}</strong>
                          <span class="muted tabular">${s.unaided} sin ayuda · ${s.assisted} con sol. · ${s.unsolved_tried} en intento / ${s.total}</span>
                        </div>
                        <div class="analytics-stack-bar" title="Sin ayuda: ${s.unaided} · Con solución: ${s.assisted} · Fallados: ${s.unsolved_tried}">
                          <span class="asb-ok" style="width:${pUnaided}%;"></span>
                          <span class="asb-warn" style="width:${pAssisted}%;"></span>
                          <span class="asb-err" style="width:${pTried}%;"></span>
                        </div>
                      </div>`;
                    })
                    .join("")}
                </div>
                <div class="row xs muted" style="gap:14px;">
                  <span><i class="asb-dot asb-ok"></i> Sin ayuda</span>
                  <span><i class="asb-dot asb-warn"></i> Con solución</span>
                  <span><i class="asb-dot asb-err"></i> A reintentar</span>
                </div>
              </div>

              <div class="card stack">
                <div class="row-between">
                  <div>
                    <h3 class="m-0">Evolución de simulacros</h3>
                    <p class="muted small m-0">${
                      analytics.exams?.stats?.count
                        ? `${analytics.exams.stats.passed} de ${analytics.exams.stats.count} aprobados · mejor nota ${analytics.exams.stats.best_score}%`
                        : "Medite con entrega final, cronómetro y autoevaluación."
                    }</p>
                  </div>
                  <a href="#/ejercicios/matematicas/simulacro?ingreso=1" class="btn btn-secondary btn-sm">Nuevo</a>
                </div>
                ${renderExamTrendSvg(analytics.exam_trend || [])}
                ${
                  analytics.exams?.exams?.length
                    ? `<div class="list">
                        ${analytics.exams.exams
                          .slice(0, 4)
                          .map(
                            (e) => `
                          <div class="list-row" style="padding:10px 0;">
                            <div class="grow">
                              <div class="small truncate"><strong>${esc(e.title)}</strong></div>
                              <div class="xs muted tabular">${esc((e.created_at || "").slice(0, 10))} · ${e.correct_count}/${e.total_count}</div>
                            </div>
                            <span class="pill ${e.passed ? "pill-green" : "pill-red"} tabular">${e.effective_score_pct ?? e.score_pct}%</span>
                          </div>`
                          )
                          .join("")}
                      </div>`
                    : `<div class="empty stack-sm">
                        <p class="m-0">Todavía no rendiste simulacros.</p>
                        <div class="row" style="justify-content:center;">
                          <a href="#/ejercicios/matematicas/simulacro?ingreso=1" class="btn btn-secondary btn-sm">Matemática</a>
                          <a href="#/ejercicios/fisica/simulacro?ingreso=1" class="btn btn-secondary btn-sm">Física</a>
                        </div>
                      </div>`
                }
              </div>

              <div class="card stack">
                <div>
                  <h3 class="m-0">Acierto por tema</h3>
                  <p class="muted small m-0">Porcentaje real combinando repasos y ejercicios. Los temas más flojos aparecen primero.</p>
                </div>
                ${
                  (analytics.topic_accuracy || []).length
                    ? `<div class="stack-sm">
                        ${analytics.topic_accuracy
                          .slice(0, 6)
                          .map((t) => {
                            const col = t.accuracy_pct >= 75 ? "var(--ok)" : t.accuracy_pct >= 50 ? "var(--warn)" : "var(--danger)";
                            return `
                            <div class="energy-bar-row" style="grid-template-columns:minmax(130px,185px) 1fr 56px;">
                              <a href="#/learn/${t.node_id}" class="xs link truncate" title="${esc(t.domain_name)} · ${esc(stripNum(t.node_title))}">${esc(stripNum(t.node_title))}</a>
                              <div class="energy-track"><div class="energy-fill" style="width:${t.accuracy_pct}%;background:${col};"></div></div>
                              <span class="xs tabular" style="text-align:right;">${t.accuracy_pct}% (${t.total})</span>
                            </div>`;
                          })
                          .join("")}
                      </div>`
                    : `<div class="empty">Aparece apenas completes tus primeros repasos o ejercicios.</div>`
                }
              </div>

              <div class="card stack">
                <div>
                  <h3 class="m-0">Tiempo de estudio registrado</h3>
                  <p class="muted small m-0">Suma el tiempo real en repasos y simulacros.</p>
                </div>
                <div class="row" style="gap:28px;">
                  <div class="stat">
                    <span class="num num-lg">${esc(fmtStudyDuration(analytics.study_time?.today_sec || 0))}</span>
                    <span class="stat-label">hoy</span>
                  </div>
                  <div class="stat">
                    <span class="num num-lg">${esc(fmtStudyDuration(analytics.study_time?.week_sec || 0))}</span>
                    <span class="stat-label">últimos 7 días</span>
                  </div>
                  <div class="stat">
                    <span class="num num-lg">${esc(fmtStudyDuration(analytics.study_time?.total_sec || 0))}</span>
                    <span class="stat-label">acumulado</span>
                  </div>
                </div>
              </div>`
            : ""
        }
      </div>
    </section>

    <section class="section">
      <div class="section-head">
        <div>
          <h2>Tu cuaderno</h2>
          <p class="section-sub">Lo que explicaste con tus palabras al cerrar una lección o responder una tarjeta.</p>
        </div>
        <a href="#/cuaderno" class="btn-text btn">Abrir cuaderno completo ${icon("arrowRight", 14)}</a>
      </div>
      ${
        feynman_journal.length
          ? `<div class="grid-2">
              ${feynman_journal
                .slice(0, 4)
                .map(
                  (f) => `
                <figure class="card stack m-0">
                  <blockquote class="title-sm m-0" style="white-space:pre-line;">«${esc(f.feynman_note)}»</blockquote>
                  <figcaption class="small muted">${esc(f.domain_name)} · ${esc(stripNum(f.item_title))} · ${esc(f.created_at.slice(0, 10))}</figcaption>
                </figure>`
                )
                .join("")}
            </div>`
          : `<div class="empty">Todavía no escribiste ninguna explicación. Al final de cada lección vas a poder resumirla en una frase.</div>`
      }
    </section>
  `;

  container.querySelector("#dash-ingreso-focus")?.addEventListener("click", async () => {
    try {
      await api.put("/api/settings", { ingreso_focus_mode: !ingresoFocus });
      await renderDashboard(container);
    } catch {
      // ignore
    }
  });
}
