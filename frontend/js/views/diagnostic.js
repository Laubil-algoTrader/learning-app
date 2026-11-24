import { icon } from "../icons.js";
import { api, esc, rich, toast, toneOf } from "../main.js";

/**
 * Diagnostic level check (#/diagnostico/<domain>):
 * Samples 2–3 distinct non-lesson questions (from exercises & cards) per official unit,
 * grades unit-by-unit readiness without auto-unlocking from a lucky guess, and lets
 * the learner explicitly opt in to unlocking strong units.
 */

function shuffledIndices(len) {
  const arr = Array.from({ length: len }, (_, i) => i);
  for (let i = arr.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

export async function renderDiagnostic(container, domainSlug) {
  const data = await api.get(`/api/diagnostic/${encodeURIComponent(domainSlug)}`);
  const { subject_key, subject_name, domain, questions, per_unit_target = 2 } = data;
  const tone = toneOf(domain.lab_type);

  if (!questions.length) {
    container.innerHTML = `<div class="empty">No hay preguntas suficientes para el diagnóstico de esta materia.</div>`;
    return;
  }

  const state = {
    idx: 0,
    started: false,
    finished: false,
    report: null,
    unlockedDone: false,
    orders: questions.map((q) => shuffledIndices(q.options.length)),
    answers: questions.map(() => null), // { picked, correct, skipped }
  };

  const buildResults = () =>
    questions.map((q, i) => ({
      unit_code: q.unit_code,
      node_slug: q.node_slug,
      correct: Boolean(state.answers[i]?.correct),
      skipped: Boolean(state.answers[i]?.skipped),
    }));

  async function finish() {
    // Score first with unlock_strong: false so unlocking is always explicit opt-in
    state.report = await api.post(`/api/diagnostic/${encodeURIComponent(domainSlug)}/apply`, {
      results: buildResults(),
      unlock_strong: false,
      save_metric: true,
    });
    state.finished = true;
    paint();
  }

  async function unlockStrongUnits() {
    try {
      const res = await api.post(`/api/diagnostic/${encodeURIComponent(domainSlug)}/apply`, {
        results: buildResults(),
        unlock_strong: true,
        save_metric: false,
      });
      state.report = res;
      state.unlockedDone = true;
      toast(
        res.unlocked_topics
          ? `Se desbloquearon ${res.unlocked_topics} temas de las unidades sólidas.`
          : "Esas unidades ya estaban desbloqueadas.",
        "ok"
      );
      paint();
    } catch (err) {
      toast(err.message, "err");
    }
  }

  function paint() {
    if (!state.started) {
      const unitCount = new Set(questions.map((q) => q.unit_code)).size;
      container.innerHTML = `
        <div class="focus-column" data-tone="${tone}">
          <div class="breadcrumb"><a href="#/ingreso?materia=${esc(subject_key)}">Ingreso</a> <span>/</span> <span>Diagnóstico de ${esc(subject_name)}</span></div>
          <section class="card-tone stack-lg">
            <div class="stack-sm">
              <span class="eyebrow m-0">Evaluación de nivel · ${per_unit_target} preguntas por unidad</span>
              <h1 class="title-md m-0" style="font-size:clamp(1.9rem,3.5vw,2.6rem);">Diagnóstico de ${esc(subject_name)}</h1>
              <p class="m-0">Son <strong>${questions.length} preguntas</strong> repartidas en las <strong>${unitCount} unidades</strong> del programa (distintas a las comprobaciones de las lecciones). Una unidad solo se marca como «Sólida» con ≥ 75 % en varias preguntas. Si no sabés una, usá «No lo sé» en vez de adivinar.</p>
            </div>
            <div class="row">
              <button type="button" class="btn btn-primary btn-lg" id="diag-start">Empezar diagnóstico ${icon("arrowRight", 18)}</button>
              <a href="#/ingreso?materia=${esc(subject_key)}" class="btn btn-secondary btn-lg">Volver</a>
            </div>
          </section>
        </div>`;
      container.querySelector("#diag-start")?.addEventListener("click", () => {
        state.started = true;
        paint();
      });
      return;
    }

    if (state.finished && state.report) {
      const rep = state.report;
      const lvlMeta = {
        strong: { label: "Sólido", cls: "pill-green" },
        medium: { label: "Repasar", cls: "pill-amber" },
        weak: { label: "Empezar acá", cls: "pill-red" },
      };
      container.innerHTML = `
        <div class="focus-column stack-lg" data-tone="${tone}">
          <div class="breadcrumb"><a href="#/ingreso?materia=${esc(subject_key)}">Ingreso</a> <span>/</span> <span>Resultado del diagnóstico</span></div>
          <section class="card-tone stack">
            <span class="eyebrow m-0">Diagnóstico completado</span>
            <div class="row-between">
              <h1 class="title-md m-0">${esc(subject_name)} · ${rep.score_pct} %</h1>
              <span class="pill ${rep.score_pct >= 60 ? "pill-green" : "pill-amber"}">${rep.correct} de ${rep.total} correctas</span>
            </div>
            <p class="m-0 small">${
              state.unlockedDone
                ? `Desbloqueamos ${rep.unlocked_topics} temas de tus unidades sólidas para que vayas directo a lo que te falta.`
                : rep.strong_units_count > 0
                ? `Saliste sólido en ${rep.strong_units_count} ${rep.strong_units_count === 1 ? "unidad" : "unidades"}. Podés desbloquearlas para saltear prerrequisitos o seguir en orden desde la unidad recomendada.`
                : "Usá el mapa por unidad para priorizar las unidades en rojo y ámbar."
            }</p>
            <div class="row">
              ${
                rep.recommended_unit
                  ? `<a href="#/ingreso?materia=${esc(subject_key)}&unidad=${esc(rep.recommended_unit)}" class="btn btn-primary">Empezar por ${esc(rep.recommended_unit)} ${icon("arrowRight", 16)}</a>`
                  : ""
              }
              ${
                rep.strong_units_count > 0 && !state.unlockedDone
                  ? `<button type="button" class="btn btn-secondary" id="diag-unlock-btn">${icon("unlock", 15)} Desbloquear ${rep.strong_units_count} ${rep.strong_units_count === 1 ? "unidad sólida" : "unidades sólidas"}</button>`
                  : ""
              }
              <a href="#/ingreso?materia=${esc(subject_key)}" class="btn btn-secondary">Ver programa completo</a>
            </div>
          </section>

          <section class="card stack">
            <h2 class="title-sm m-0">Mapa de nivel por unidad</h2>
            <div class="list">
              ${rep.units
                .map((u) => {
                  const m = lvlMeta[u.level] || lvlMeta.weak;
                  return `
                  <div class="list-row">
                    <span class="pill pill-tone tabular">${esc(u.code)}</span>
                    <div class="grow">
                      <div class="list-title">${esc(u.short_title)}</div>
                      <div class="xs muted tabular">${u.correct}/${u.total} correctas (${u.pct} %)</div>
                    </div>
                    <span class="pill ${m.cls}">${m.label}</span>
                    <a href="#/ingreso?materia=${esc(subject_key)}&unidad=${esc(u.code)}" class="btn btn-secondary btn-sm">Ir</a>
                  </div>`;
                })
                .join("")}
            </div>
          </section>
        </div>`;
      container.querySelector("#diag-unlock-btn")?.addEventListener("click", unlockStrongUnits);
      return;
    }

    const q = questions[state.idx];
    const order = state.orders[state.idx];
    const pct = Math.round(((state.idx + 1) / questions.length) * 100);

    container.innerHTML = `
      <div class="focus-column stack" data-tone="${tone}">
        <div class="row-between">
          <span class="eyebrow m-0">Pregunta ${state.idx + 1} de ${questions.length} · ${esc(q.unit_code)} · ${esc(q.unit_title)}</span>
          <span class="xs muted tabular">${pct} %</span>
        </div>
        <div class="progress-track"><div class="progress-fill" style="width:${pct}%;"></div></div>

        <article class="card stack-lg">
          <div class="title-md m-0 rich" style="font-size:1.15rem;line-height:1.5;">${rich(q.question)}</div>
          <div class="stack-sm">
            ${order
              .map(
                (optIdx, pos) => `
              <button type="button" class="option-btn diag-opt" data-opt="${optIdx}">
                <span class="opt-key">${String.fromCharCode(65 + pos)}</span>
                <span class="rich">${rich(q.options[optIdx])}</span>
              </button>`
              )
              .join("")}
          </div>
          <div class="row-between">
            <button type="button" class="btn btn-text btn-sm" id="diag-skip">No lo sé todavía (saltar)</button>
            <a href="#/ingreso?materia=${esc(subject_key)}" class="btn btn-text btn-sm muted">Cancelar</a>
          </div>
        </article>
      </div>`;

    const advance = async (entry) => {
      state.answers[state.idx] = entry;
      if (state.idx < questions.length - 1) {
        state.idx += 1;
        paint();
      } else {
        await finish();
      }
    };

    container.querySelectorAll(".diag-opt").forEach((b) =>
      b.addEventListener("click", () => {
        const picked = Number(b.dataset.opt);
        advance({ picked, correct: picked === q.correct, skipped: false });
      })
    );
    container.querySelector("#diag-skip")?.addEventListener("click", () => {
      advance({ picked: null, correct: false, skipped: true });
    });
  }

  paint();
}
