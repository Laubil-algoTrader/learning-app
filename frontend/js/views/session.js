import { icon, resolveDomainIcon } from "../icons.js";
import { api, esc, registerCleanup, toast } from "../main.js";
import { renderActiveRecallCard } from "./review.js";

const STORE_KEY = "aprendelab_session";
const MAX_AGE_MS = 3 * 60 * 60 * 1000;

/* Plain-language names for the four phases the server builds */
const PHASES = {
  warmup: { name: "Entrada en calor", tip: "Repasos que ya te tocaban. Respondé de memoria antes de mirar." },
  deliberate: { name: "Lo que más te cuesta", tip: "Andá despacio: primero sin errores, después rápido." },
  interleave: { name: "Mezcla de temas", tip: "Cambiar de tema te obliga a elegir la estrategia, no solo a ejecutarla." },
  consolidation: { name: "Cierre", tip: "Afirmá lo más difícil de hoy con repeticiones limpias." },
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

export async function renderSession(container, { minutes = null, domains = null } = {}) {
  const [domainsRes, settingsRes] = await Promise.all([api.get("/api/domains"), api.get("/api/settings")]);
  const allDomains = domainsRes.domains;
  let selectedMinutes = minutes || settingsRes.settings.default_session_minutes || 25;
  let selectedDomains = domains ? new Set(domains) : new Set(allDomains.map((d) => d.slug));
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
      // storage full / private mode: the session simply won't survive a reload
    }
  };

  const fmtTime = (s) => `${String(Math.floor(s / 60)).padStart(2, "0")}:${String(s % 60).padStart(2, "0")}`;

  const startSession = async () => {
    const chosen = Array.from(selectedDomains);
    if (!chosen.length) {
      toast("Elegí al menos una materia.", "err");
      return;
    }
    session = await api.post("/api/sessions/generate", { duration_minutes: selectedMinutes, domains: chosen });
    currentIdx = 0;
    completedLog = [];
    sessionStartedAt = Date.now();
    persist();
    renderRunner();
  };

  const renderSetup = () => {
    stopTimer();
    const saved = loadSaved();
    container.innerHTML = `
      <div class="focus-column">
        <div class="page-header">
          <div>
            <h1>Sesión guiada</h1>
            <p class="muted">La app arma el orden por vos: primero lo que tocaba repasar, después lo que más te cuesta, una mezcla de temas y un cierre.</p>
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
            <h3 class="m-0">¿Qué materias mezclamos?</h3>
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
    container.querySelectorAll(".dom-toggle").forEach((b) =>
      b.addEventListener("click", () => {
        const s = b.dataset.slug;
        if (selectedDomains.has(s)) selectedDomains.delete(s);
        else selectedDomains.add(s);
        renderSetup();
      })
    );
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
          <p class="lead">Las sesiones usan temas que ya aprendiste. Completá una lección y volvé: sus tarjetas se suman solas.</p>
          <div class="row">
            <a href="#/aprender" class="btn btn-primary">Ir a aprender ${icon("arrowRight", 16)}</a>
            <a href="#/labs" class="btn btn-secondary">Laboratorios</a>
          </div>
        </div>
      </div>`;
  };

  const renderSummary = () => {
    clearSaved();
    const totalMins = Math.max(1, Math.round((Date.now() - sessionStartedAt) / 60000));
    const rated = completedLog.filter((x) => x.rating);
    const recalled = rated.filter((x) => x.rating >= 2).length;
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
          <div class="row" style="gap:40px;">
            <div class="stat"><span class="num num-xl">${rated.length}</span><span class="stat-label">tarjetas calificadas</span></div>
            <div class="stat"><span class="num num-xl">${rated.length ? Math.round((recalled / rated.length) * 100) : 0}%</span><span class="stat-label">las recordaste</span></div>
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
            <a href="#/" class="btn btn-primary">Volver a Hoy</a>
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
    const phase = PHASES[block.phase] || { name: block.phase_label, tip: block.phase_tip };
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
      completedLog.push({ skipped: true, item: block.item });
      advance();
    });

    renderActiveRecallCard(container.querySelector("#session-card-host"), block.item, {
      phaseLabel: null,
      phaseTip: phase.tip,
      isOverlearning: Boolean(block.is_overlearning),
      noSchedule: Boolean(block.no_schedule),
      isRetry: Boolean(block.is_retry),
      onRated: (res) => {
        completedLog.push({ rating: res.rating, item: block.item });
        if (res.rating === 1 && !block.is_retry) {
          // A miss comes back once, a couple of blocks later (but before the closing block)
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
