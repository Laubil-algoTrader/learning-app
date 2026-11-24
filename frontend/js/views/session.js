import { icon, resolveDomainIcon } from "../icons.js";
import { api, esc, rich, registerCleanup, toast } from "../main.js";
import { renderActiveRecallCard, checkAnswer } from "./review.js";
import { mountStudyTools } from "../tools_drawer.js";
import { exerciseDiagram } from "../diagrams.js";

const STORE_KEY = "aprendelab_session";
const MAX_AGE_MS = 3 * 60 * 60 * 1000;
const INGRESO_SLUGS = ["matematicas", "fisica", "comprension-problemas"];

/* Plain-language names for the phases */
const PHASES = {
  warmup: { name: "Entrada en calor", tip: "Repasos que ya te tocaban. Respondé de memoria antes de mirar." },
  deliberate: { name: "Lo que más te cuesta", tip: "Andá despacio: primero sin errores, después rápido." },
  interleave: { name: "Mezcla de temas", tip: "Cambiar de tema te obliga a elegir la estrategia, no solo a ejecutarla." },
  consolidation: { name: "Cierre", tip: "Afirmá lo más difícil de hoy con repeticiones limpias." },
  practice_problem: { name: "Problema en papel", tip: "Resolvé en hoja aparte antes de corregir. Si necesitás calculadora o borrador, abrilos arriba." },
};

function loadSaved() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORE_KEY) || "null");
    if (!saved || !saved.session?.blocks?.length) return null;
    if (Date.now() - saved.savedAt > MAX_AGE_MS || saved.currentIdx >= saved.session.blocks.length) return null;
    return saved;
  } catch {
    return null;
  }
}

function clearSaved() {
  try {
    localStorage.removeItem(STORE_KEY);
  } catch {
    // ignore
  }
}

function shuffled(arr) {
  const out = arr.slice();
  for (let i = out.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [out[i], out[j]] = [out[j], out[i]];
  }
  return out;
}

function playGentleChime() {
  try {
    const AC = window.AudioContext || window.webkitAudioContext;
    const ctx = new AC();
    const now = ctx.currentTime;
    [523.25, 659.25].forEach((freq, i) => {
      const osc = ctx.createOscillator();
      const g = ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(freq, now + i * 0.14);
      g.gain.setValueAtTime(0.001, now + i * 0.14);
      g.gain.linearRampToValueAtTime(0.14, now + i * 0.14 + 0.02);
      g.gain.exponentialRampToValueAtTime(0.001, now + i * 0.14 + 0.55);
      osc.connect(g).connect(ctx.destination);
      osc.start(now + i * 0.14);
      osc.stop(now + i * 0.14 + 0.6);
    });
    setTimeout(() => ctx.close().catch(() => {}), 900);
  } catch {
    // non-fatal if audio is blocked
  }
}

async function fetchPracticeExerciseBlocks(domainSlugs, maxCount = 3) {
  const responses = await Promise.all(
    domainSlugs.map((slug) => api.get(`/api/exercises/${encodeURIComponent(slug)}`).catch(() => null))
  );
  const candidates = [];
  for (const res of responses) {
    if (!res?.topics) continue;
    for (const topic of res.topics) {
      for (const ex of topic.exercises || []) {
        if (ex.kind !== "problem") continue;
        candidates.push({
          domain: res.domain,
          topic: { slug: topic.slug, title: topic.title, node_id: topic.node_id },
          exercise: ex,
        });
      }
    }
  }
  if (!candidates.length) return [];
  const pool = shuffled(candidates).sort(
    (a, b) => Number(a.exercise.status?.solved) - Number(b.exercise.status?.solved) || Number(!a.exercise.source) - Number(!b.exercise.source)
  );
  const picked = [];
  const usedDomains = new Set();
  // First pass: at most one per domain for interleaving
  for (const c of pool) {
    if (picked.length >= maxCount) break;
    if (usedDomains.has(c.domain.slug)) continue;
    usedDomains.add(c.domain.slug);
    picked.push(c);
  }
  // Second pass: fill up to maxCount
  for (const c of pool) {
    if (picked.length >= maxCount) break;
    if (picked.some((p) => p.exercise.id === c.exercise.id)) continue;
    picked.push(c);
  }
  return picked.map((c) => ({
    kind: "exercise",
    phase: "practice_problem",
    suggested_minutes: c.exercise.minutes || 5,
    domain: c.domain,
    topic: c.topic,
    exercise: c.exercise,
  }));
}

function renderExerciseBlock(host, block, { onDone }) {
  const { exercise: ex, domain, topic } = block;
  const values = (ex.parts || []).map(() => "");
  const picked = (ex.parts || []).map(() => null);
  const orders = (ex.parts || []).map((p) => (p.check.type === "choice" ? shuffled(p.check.options.map((_, i) => i)) : []));
  let verdicts = null;
  let hintsShown = 0;
  let solutionShown = false;
  let sawSolution = false;
  let locked = false;
  let toolsOpen = false;
  const toolsEl = document.createElement("div");
  mountStudyTools(toolsEl, { storageKey: `sess:${ex.id}` });

  const paint = () => {
    const solved = verdicts && verdicts.every(Boolean);
    const diagram = exerciseDiagram(ex);
    host.innerHTML = `
      <article class="card stack-lg">
        <div class="row-between row-top">
          <div class="stack-sm" style="gap:4px;">
            <span class="eyebrow m-0">${esc(domain.name)} · ${esc(String(topic.title || "").replace(/^\d+\.\s*/, ""))}</span>
            <h2 class="title-md m-0">${esc(ex.title)}</h2>
          </div>
          <button type="button" class="btn ${toolsOpen ? "btn-primary" : "btn-secondary"} btn-sm" id="sess-tools-btn">
            ${icon("sliders", 14)} Herramientas
          </button>
        </div>

        <div id="sess-tools-slot" ${toolsOpen ? "" : "hidden"}></div>

        <form id="sess-ex-form" class="stack-lg" novalidate>
          <div class="stack">
            ${String(ex.statement || "")
              .split(/\n\s*\n/)
              .map((p) => `<p class="rich m-0">${rich(p.trim())}</p>`)
              .join("")}
          </div>
          ${diagram}
          <div class="stack">
            ${ex.parts
              .map((p, i) => {
                const v = verdicts ? verdicts[i] : null;
                const badge = v === null ? "" : v ? `<span class="pill pill-green">Correcto</span>` : `<span class="pill pill-red">No coincide</span>`;
                const ctrl =
                  p.check.type === "choice"
                    ? `<div class="stack-sm">
                        ${orders[i]
                          .map((optIdx, pos) => {
                            const isSel = picked[i] === optIdx;
                            const cls = isSel ? (v === null ? "picked" : v ? "right" : "wrong") : "";
                            return `<button type="button" class="option-btn sess-opt ${cls}" data-part="${i}" data-opt="${optIdx}" ${locked ? "disabled" : ""}>
                              <span class="opt-key">${String.fromCharCode(65 + pos)}</span>
                              <span class="rich">${rich(p.check.options[optIdx])}</span>
                            </button>`;
                          })
                          .join("")}
                      </div>`
                    : `<label class="field">
                        <span>Tu respuesta${p.check.unit ? ` (en ${esc(p.check.unit)})` : ""}</span>
                        <input type="text" class="sess-inp" data-part="${i}" value="${esc(values[i])}" autocomplete="off" inputmode="${p.check.type === "numeric" ? "decimal" : "text"}" ${locked ? "disabled" : ""} />
                      </label>`;
                return `<div class="ex-part stack-sm">
                  <div class="row-between row-top"><p class="rich m-0">${rich(p.prompt)}</p>${badge}</div>
                  ${ctrl}
                  ${solutionShown ? `<p class="small m-0"><strong>Respuesta:</strong> <span class="rich">${rich(p.answer)}</span></p>` : ""}
                </div>`;
              })
              .join("")}
          </div>

          ${
            hintsShown
              ? `<div class="callout callout-info stack-sm">${ex.hints
                  .slice(0, hintsShown)
                  .map((h, i) => `<p class="m-0 small"><strong>Pista ${i + 1}.</strong> <span class="rich">${rich(h)}</span></p>`)
                  .join("")}</div>`
              : ""
          }

          ${
            verdicts
              ? `<p class="callout ${solved ? "callout-ok" : "callout-warn"} m-0">${
                  solved ? "<strong>¡Bien resuelto!</strong> Seguí con el próximo bloque." : "<strong>Todavía no coincide.</strong> Podés reintentar, mirar la resolución o pasar al siguiente bloque."
                }</p>`
              : ""
          }

          <div class="row">
            ${locked ? "" : `<button type="submit" class="btn btn-primary">Corregir</button>`}
            ${locked || verdicts ? `<button type="button" class="btn ${locked ? "btn-primary" : "btn-secondary"}" id="sess-ex-next">Siguiente bloque ${icon("arrowRight", 15)}</button>` : ""}
            ${!locked && hintsShown < (ex.hints || []).length ? `<button type="button" class="btn btn-secondary" id="sess-ex-hint">Pista (${hintsShown + 1}/${ex.hints.length})</button>` : ""}
            ${!solutionShown ? `<button type="button" class="btn btn-ghost" id="sess-ex-sol">Ver resolución</button>` : ""}
          </div>

          ${
            solutionShown
              ? `<div class="card-flat stack">
                  <h3 class="m-0">Resolución</h3>
                  <ol class="ex-steps">${(ex.solution || []).map((s) => `<li class="rich">${rich(s)}</li>`).join("")}</ol>
                </div>`
              : ""
          }
        </form>
      </article>
    `;

    if (toolsOpen) {
      host.querySelector("#sess-tools-slot")?.appendChild(toolsEl);
    }

    host.querySelector("#sess-tools-btn")?.addEventListener("click", () => {
      toolsOpen = !toolsOpen;
      paint();
    });
    host.querySelectorAll(".sess-inp").forEach((inp) =>
      inp.addEventListener("input", () => {
        values[Number(inp.dataset.part)] = inp.value;
      })
    );
    host.querySelectorAll(".sess-opt").forEach((b) =>
      b.addEventListener("click", () => {
        picked[Number(b.dataset.part)] = Number(b.dataset.opt);
        verdicts = null;
        paint();
      })
    );
    host.querySelector("#sess-ex-hint")?.addEventListener("click", () => {
      hintsShown += 1;
      paint();
    });
    host.querySelector("#sess-ex-sol")?.addEventListener("click", () => {
      solutionShown = true;
      if (!(verdicts && verdicts.every(Boolean))) sawSolution = true;
      paint();
    });
    host.querySelector("#sess-ex-form")?.addEventListener("submit", async (e) => {
      e.preventDefault();
      const answered = ex.parts.every((p, i) => (p.check.type === "choice" ? picked[i] !== null : values[i].trim() !== ""));
      if (!answered) {
        toast("Completá tu respuesta antes de corregir.", "info");
        return;
      }
      verdicts = ex.parts.map((p, i) => checkAnswer(p.check, p.check.type === "choice" ? picked[i] : values[i]) === true);
      const ok = verdicts.every(Boolean);
      if (ok) locked = true;
      await api
        .post(`/api/exercises/${encodeURIComponent(ex.id)}/attempts`, {
          correct: ok,
          parts_ok: verdicts.filter(Boolean).length,
          saw_solution: sawSolution,
        })
        .catch(() => {});
      paint();
    });
    host.querySelector("#sess-ex-next")?.addEventListener("click", () => {
      onDone({ ok: Boolean(verdicts && verdicts.every(Boolean)) });
    });
  };

  paint();
}

export async function renderSession(container, { minutes = null, domains = null } = {}) {
  const [domainsRes, settingsRes] = await Promise.all([api.get("/api/domains"), api.get("/api/settings")]);
  const allDomains = domainsRes.domains;
  const availableIngreso = allDomains.filter((d) => INGRESO_SLUGS.includes(d.slug)).map((d) => d.slug);
  const ingresoFocusDefault = Boolean(settingsRes.settings?.ingreso_focus_mode);

  let selectedMinutes = minutes || settingsRes.settings.default_session_minutes || 25;
  let selectedDomains = domains
    ? new Set(domains)
    : new Set(ingresoFocusDefault && availableIngreso.length ? availableIngreso : allDomains.map((d) => d.slug));
  let includeExercises = true;
  let session = null;
  let currentIdx = 0;
  let timerId = null;
  let soundEnabled = true;
  let sessionStartedAt = 0;
  let completedLog = [];

  const stopTimer = () => {
    if (timerId) {
      clearInterval(timerId);
      timerId = null;
    }
  };
  registerCleanup(stopTimer);

  const persist = () => {
    try {
      localStorage.setItem(
        STORE_KEY,
        JSON.stringify({ session, currentIdx, completedLog, sessionStartedAt, savedAt: Date.now() })
      );
    } catch {
      // storage full / private mode
    }
  };

  const fmtTime = (s) => `${String(Math.floor(s / 60)).padStart(2, "0")}:${String(s % 60).padStart(2, "0")}`;

  const startSession = async () => {
    const chosen = Array.from(selectedDomains);
    if (!chosen.length) {
      toast("Elegí al menos una materia.", "err");
      return;
    }
    const baseSession = await api.post("/api/sessions/generate", { duration_minutes: selectedMinutes, domains: chosen });
    const blocks = [...(baseSession.blocks || [])];
    if (includeExercises) {
      const exTarget = blocks.length ? (selectedMinutes >= 45 ? 3 : 2) : Math.min(4, Math.max(2, Math.round(selectedMinutes / 8)));
      const exBlocks = await fetchPracticeExerciseBlocks(chosen, exTarget);
      if (exBlocks.length) {
        if (!blocks.length) {
          blocks.push(...exBlocks);
        } else {
          // Interleave exercises into the middle / second half of the session
          const step = Math.max(2, Math.floor(blocks.length / (exBlocks.length + 1)));
          exBlocks.forEach((eb, idx) => {
            const pos = Math.min(blocks.length, (idx + 1) * step + idx);
            blocks.splice(pos, 0, eb);
          });
        }
      }
    }
    session = { ...baseSession, blocks };
    currentIdx = 0;
    completedLog = [];
    sessionStartedAt = Date.now();
    persist();
    renderRunner();
  };

  const renderSetup = () => {
    stopTimer();
    const saved = loadSaved();
    const isIngresoPreset =
      availableIngreso.length > 0 &&
      selectedDomains.size === availableIngreso.length &&
      availableIngreso.every((s) => selectedDomains.has(s));

    container.innerHTML = `
      <div class="focus-column">
        <div class="page-header">
          <div>
            <h1>Sesión guiada</h1>
            <p class="muted">La app arma el orden por vos: repasos pendientes, mezcla de temas y problemas en papel intercalados.</p>
          </div>
        </div>

        ${
          saved
            ? `<div class="card-wash row-between mb-lg">
                <div>
                  <h3 class="m-0">Tenés una sesión sin terminar</h3>
                  <p class="muted small m-0">Ibas por el bloque ${saved.currentIdx + 1} de ${saved.session.blocks.length}.</p>
                </div>
                <div class="row">
                  <button id="resume-session" class="btn btn-primary" type="button">Continuar</button>
                  <button id="discard-session" class="btn btn-secondary" type="button">Descartar</button>
                </div>
              </div>`
            : ""
        }

        <div class="card stack-lg">
          <div class="stack-sm">
            <h3 class="m-0">¿Cuánto tiempo tenés?</h3>
            <div class="segmented" role="group" aria-label="Duración">
              ${[15, 25, 45]
                .map((m) => `<button type="button" class="seg-btn ${selectedMinutes === m ? "active" : ""} dur-btn" data-m="${m}">${m} min</button>`)
                .join("")}
            </div>
          </div>

          <div class="stack-sm">
            <div class="row-between">
              <h3 class="m-0">¿Qué materias mezclamos?</h3>
              <div class="row gap-sm">
                ${
                  availableIngreso.length
                    ? `<button type="button" class="btn btn-sm ${isIngresoPreset ? "btn-primary" : "btn-secondary"}" id="preset-ingreso">Solo Ingreso</button>`
                    : ""
                }
                <button type="button" class="btn btn-text btn-sm" id="preset-all">Todas</button>
              </div>
            </div>
            <p class="small muted m-0">Mezclar dos o tres rinde más que hacer una sola de corrido.</p>
            <div class="row">
              ${allDomains
                .map((d) => {
                  const on = selectedDomains.has(d.slug);
                  return `
                  <button type="button" class="btn btn-sm ${on ? "btn-primary" : "btn-secondary"} dom-toggle" data-slug="${esc(d.slug)}" aria-pressed="${on}">
                    ${icon(resolveDomainIcon(d.icon, d.lab_type), 14)} ${esc(d.name)}
                  </button>`;
                })
                .join("")}
            </div>
          </div>

          <label class="row gap-sm small" style="cursor:pointer;">
            <input type="checkbox" id="include-ex-cb" ${includeExercises ? "checked" : ""} style="width:18px;height:18px;min-height:0;" />
            <span>Incluir problemas de práctica en papel (funciona incluso desde el día 1)</span>
          </label>

          <div><button id="launch-session" class="btn btn-primary btn-lg" type="button">Empezar ${icon("arrowRight", 18)}</button></div>
        </div>
      </div>
    `;

    container.querySelectorAll(".dur-btn").forEach((b) =>
      b.addEventListener("click", () => {
        selectedMinutes = Number(b.dataset.m);
        renderSetup();
      })
    );
    container.querySelector("#preset-ingreso")?.addEventListener("click", () => {
      selectedDomains = new Set(availableIngreso);
      renderSetup();
    });
    container.querySelector("#preset-all")?.addEventListener("click", () => {
      selectedDomains = new Set(allDomains.map((d) => d.slug));
      renderSetup();
    });
    container.querySelectorAll(".dom-toggle").forEach((b) =>
      b.addEventListener("click", () => {
        const s = b.dataset.slug;
        if (selectedDomains.has(s)) selectedDomains.delete(s);
        else selectedDomains.add(s);
        renderSetup();
      })
    );
    container.querySelector("#include-ex-cb")?.addEventListener("change", (e) => {
      includeExercises = e.target.checked;
    });
    container.querySelector("#launch-session")?.addEventListener("click", startSession);
    container.querySelector("#resume-session")?.addEventListener("click", () => {
      ({ session, currentIdx, completedLog, sessionStartedAt } = saved);
      renderRunner();
    });
    container.querySelector("#discard-session")?.addEventListener("click", () => {
      clearSaved();
      renderSetup();
    });
  };

  const renderNothingToDo = () => {
    clearSaved();
    container.innerHTML = `
      <div class="focus-column">
        <div class="card-wash stack" style="padding:48px 32px;">
          <h2>Todavía no hay con qué armar una sesión</h2>
          <p class="lead">Las sesiones usan temas que ya aprendiste o ejercicios de práctica. Completá una lección o activá los problemas en papel y volvé.</p>
          <div class="row">
            <a href="#/ingreso" class="btn btn-primary">Ir a Ingreso ${icon("arrowRight", 16)}</a>
            <a href="#/aprender" class="btn btn-secondary">Ver materias</a>
          </div>
        </div>
      </div>`;
  };

  const renderSummary = () => {
    clearSaved();
    const totalMins = Math.max(1, Math.round((Date.now() - sessionStartedAt) / 60000));
    const rated = completedLog.filter((x) => x.rating);
    const recalled = rated.filter((x) => x.rating >= 2).length;
    const exDone = completedLog.filter((x) => x.kind === "exercise");
    const exRight = exDone.filter((x) => x.ok).length;
    const skipped = completedLog.filter((x) => x.skipped).length;
    const hard = rated.filter((x) => x.rating <= 2);
    const uniqueHard = [...new Map(hard.map((b) => [b.item.id, b])).values()];

    container.innerHTML = `
      <div class="focus-column">
        <div class="card-wash stack-lg" style="padding:44px 32px;">
          <div>
            <h2>Sesión terminada</h2>
            <p class="lead m-0">Lo que practicaste hoy se afirma mientras descansás. No hace falta repetirlo ahora.</p>
          </div>
          <div class="row" style="gap:36px;">
            ${rated.length ? `<div class="stat"><span class="num num-xl">${rated.length}</span><span class="stat-label">tarjetas (${Math.round((recalled / rated.length) * 100)}% bien)</span></div>` : ""}
            ${exDone.length ? `<div class="stat"><span class="num num-xl">${exRight}/${exDone.length}</span><span class="stat-label">problemas resueltos</span></div>` : ""}
            <div class="stat"><span class="num num-xl">${totalMins}</span><span class="stat-label">${totalMins === 1 ? "minuto" : "minutos"}</span></div>
          </div>
          ${skipped ? `<p class="small muted m-0">Salteaste ${skipped} ${skipped === 1 ? "bloque" : "bloques"}: siguen en tu repaso.</p>` : ""}
          ${
            uniqueHard.length
              ? `<div class="stack-sm">
                  <h3 class="m-0">Para reforzar en estos días</h3>
                  <div class="list">
                    ${uniqueHard
                      .map(
                        (b) => `
                      <div class="list-row" style="padding:12px 0;">
                        <span class="grow"><strong>${esc(b.item.domain_name)}:</strong> ${esc(b.item.title)}</span>
                        <a href="#/review?node=${b.item.node_id}" class="btn btn-secondary btn-sm">Practicar el tema</a>
                      </div>`
                      )
                      .join("")}
                  </div>
                </div>`
              : ""
          }
          <div class="row">
            <a href="#/ingreso" class="btn btn-primary">Volver a Ingreso</a>
            <a href="#/" class="btn btn-secondary">Ir a Hoy</a>
            <button id="new-sess-btn" class="btn btn-secondary" type="button">Otra sesión</button>
          </div>
        </div>
      </div>`;
    container.querySelector("#new-sess-btn")?.addEventListener("click", renderSetup);
  };

  const renderRunner = () => {
    stopTimer();
    if (!session || !session.blocks.length) {
      renderNothingToDo();
      return;
    }
    if (currentIdx >= session.blocks.length) {
      renderSummary();
      return;
    }

    const block = session.blocks[currentIdx];
    const phase = PHASES[block.phase] || { name: block.phase_label || "Bloque", tip: block.phase_tip || "" };
    let timerSec = (block.suggested_minutes || 3) * 60;
    let chimePlayed = false;
    let paused = false;

    const advance = () => {
      currentIdx += 1;
      persist();
      renderRunner();
    };

    container.innerHTML = `
      <div class="focus-column">
        <div class="page-header" style="padding-bottom:16px;">
          <div>
            <div class="eyebrow">Bloque ${currentIdx + 1} de ${session.blocks.length}</div>
            <h1 class="title-md" style="font-size:clamp(2rem,4vw,3rem);">${esc(phase.name)}</h1>
          </div>
          <div class="row">
            <span class="pill" title="Tiempo sugerido para este bloque">${icon("clock", 14)} <span id="timer-val" class="mono">${fmtTime(timerSec)}</span></span>
            <button id="pause-timer" class="icon-btn" type="button" aria-label="Pausar o reanudar el reloj">${icon("pause", 16)}</button>
            <button id="sound-toggle" class="icon-btn" type="button" aria-label="Activar o silenciar la campana" aria-pressed="${soundEnabled}" style="opacity:${soundEnabled ? 1 : 0.45};">${icon("volume", 16)}</button>
            <button id="skip-block" class="btn btn-secondary btn-sm" type="button">Saltear</button>
          </div>
        </div>

        <div class="session-map" role="img" aria-label="Bloque ${currentIdx + 1} de ${session.blocks.length}">
          ${session.blocks.map((_, i) => `<span class="${i < currentIdx ? "done" : i === currentIdx ? "now" : ""}"></span>`).join("")}
        </div>

        <div id="session-card-host"></div>
      </div>
    `;

    const timerVal = container.querySelector("#timer-val");
    timerId = setInterval(() => {
      if (paused) return;
      if (timerSec > 0) {
        timerSec -= 1;
        timerVal.textContent = fmtTime(timerSec);
      } else if (!chimePlayed) {
        chimePlayed = true;
        timerVal.textContent = "Tiempo";
        if (soundEnabled) playGentleChime();
      }
    }, 1000);

    container.querySelector("#sound-toggle")?.addEventListener("click", (e) => {
      soundEnabled = !soundEnabled;
      e.currentTarget.style.opacity = soundEnabled ? "1" : "0.45";
      e.currentTarget.setAttribute("aria-pressed", String(soundEnabled));
    });
    container.querySelector("#pause-timer")?.addEventListener("click", (e) => {
      paused = !paused;
      e.currentTarget.innerHTML = paused ? icon("play", 16) : icon("pause", 16);
    });
    container.querySelector("#skip-block")?.addEventListener("click", () => {
      completedLog.push({ skipped: true, kind: block.kind || "card", item: block.item });
      advance();
    });

    const host = container.querySelector("#session-card-host");
    if (block.kind === "exercise") {
      renderExerciseBlock(host, block, {
        onDone: ({ ok }) => {
          completedLog.push({ kind: "exercise", ok, exercise: block.exercise });
          advance();
        },
      });
      return;
    }

    renderActiveRecallCard(host, block.item, {
      phaseLabel: null,
      phaseTip: phase.tip,
      isOverlearning: Boolean(block.is_overlearning),
      noSchedule: Boolean(block.no_schedule),
      isRetry: Boolean(block.is_retry),
      onRated: (res) => {
        completedLog.push({ rating: res.rating, item: block.item });
        if (res.rating === 1 && !block.is_retry) {
          const last = session.blocks.length - 1;
          const closing = session.blocks[last]?.phase === "consolidation" ? last : session.blocks.length;
          const at = Math.max(currentIdx + 1, Math.min(closing, currentIdx + 3));
          session.blocks.splice(at, 0, { ...block, item: res.item, is_retry: true, suggested_minutes: 2 });
        }
        advance();
      },
    });
  };

  if (minutes || domains) {
    await startSession();
  } else {
    renderSetup();
  }
}
