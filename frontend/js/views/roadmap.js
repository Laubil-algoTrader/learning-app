import { icon } from "../icons.js";
import { api, esc, labLinkToHash, refreshSidebarDomains, toast, toneOf, LAB_ROUTES } from "../main.js";

const STATUS_META = {
  mastered: { label: "Dominado", cls: "pill-green" },
  in_progress: { label: "En práctica", cls: "pill-amber" },
  available: { label: "Disponible", cls: "pill-tone" },
  locked: { label: "Bloqueado", cls: "" },
};

const TYPE_LABEL = {
  recall: "Pregunta",
  drill: "Ejercicio",
  debug: "Encontrar el error",
  worked_example: "Problema",
  project_step: "Proyecto",
};

const ALL_STAGES = "__all__";
const stripNum = (t) => String(t || "").replace(/^\d+\.\s*/, "");
const normSearch = (s) =>
  String(s || "")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .trim();

function formatEstTime(mins) {
  if (!mins || mins <= 0) return "";
  if (mins < 60) return `~${mins} min`;
  const h = Math.floor(mins / 60);
  const m = mins % 60;
  return m >= 10 ? `~${h} h ${m} min` : `~${h} h`;
}

function stageStorageKey(slug) {
  return `aprendelab_roadmap_stage:${slug}`;
}

function readSavedStage(slug) {
  try {
    return sessionStorage.getItem(stageStorageKey(slug)) || "";
  } catch {
    return "";
  }
}

function saveStage(slug, key) {
  try {
    sessionStorage.setItem(stageStorageKey(slug), key);
  } catch {
    /* ignore private mode errors */
  }
}

function renderCardsDrawer(node) {
  const count = node.items.length;
  return `
    <details class="lesson-cards-drawer">
      <summary class="lesson-drawer-toggle">
        <span>${count} ${count === 1 ? "tarjeta" : "tarjetas"} de práctica</span>
        ${icon("arrowDown", 13, "drawer-chev")}
      </summary>
      <div class="lesson-drawer-body">
        ${
          count
            ? `<div class="list">
                ${node.items
                  .map((it) => {
                    const deepLab = labLinkToHash(it.payload?.lab_link);
                    return `
                    <div class="list-row" style="padding:10px 0;">
                      <div class="grow">
                        <div class="small">${esc(it.title)}</div>
                        <div class="xs muted">${esc(TYPE_LABEL[it.item_type] || "Tarjeta")} · ${esc(it.due_label)}${it.mastered ? " · dominada" : ""}${it.lapses >= 3 ? ` · te cuesta (${it.lapses} olvidos)` : ""}</div>
                      </div>
                      ${deepLab ? `<a href="${deepLab}" class="btn btn-text btn-sm">Laboratorio</a>` : ""}
                    </div>`;
                  })
                  .join("")}
              </div>`
            : `<p class="xs muted m-0">Todavía no hay tarjetas en esta lección.</p>`
        }
        <details class="mt-sm">
          <summary class="xs link" style="cursor:pointer;width:fit-content;">Agregar una tarjeta propia</summary>
          <form class="quick-item-form stack-sm mt-sm" data-node-id="${node.id}">
            <input type="text" name="title" placeholder="Título corto (ej.: mi error típico al despejar)" aria-label="Título" required />
            <textarea name="prompt" placeholder="Pregunta o situación a practicar" aria-label="Pregunta" required></textarea>
            <textarea name="answer" placeholder="Respuesta o solución" aria-label="Respuesta" required></textarea>
            <div><button class="btn btn-secondary btn-sm" type="submit">${icon("plus", 14)} Guardar tarjeta</button></div>
          </form>
        </details>
      </div>
    </details>`;
}

function renderPrimaryAction(node, { emphasis = false } = {}) {
  const dueHere = node.due_count || 0;
  if (!node.lesson_completed && node.has_lesson !== false) {
    return `<a href="#/learn/${node.id}" class="btn ${emphasis ? "btn-primary" : "btn-secondary"} btn-sm">${icon("bookOpen", 14)} ${emphasis ? "Empezar" : "Aprender"}${emphasis ? ` ${icon("arrowRight", 14)}` : ""}</a>`;
  }
  if (node.items.length) {
    return `<a href="#/review?node=${node.id}" class="btn ${dueHere || emphasis ? "btn-primary" : "btn-secondary"} btn-sm">${dueHere ? `Repasar (${dueHere})` : "Practicar"}${emphasis ? ` ${icon("arrowRight", 14)}` : ""}</a>`;
  }
  return "";
}

function renderSpotlight(node, { isToPractice, showStageBadge }) {
  const dueHere = node.due_count || 0;
  const badgeLabel = dueHere > 0 ? `Repaso pendiente (${dueHere})` : isToPractice ? "Practicar ahora" : "Siguiente paso";
  const badgeCls = dueHere > 0 || isToPractice ? "pill-amber" : "pill-tone";
  const numStr = String(node._displayNum).padStart(2, "0");

  return `
    <article class="lesson-spotlight" id="node-${esc(node.slug)}">
      <div class="lesson-spotlight-top">
        <div class="row gap-sm">
          <span class="pill ${badgeCls}">${badgeLabel}</span>
          ${showStageBadge && node._secName ? `<span class="pill">${esc(node._secName)}</span>` : ""}
          ${node.metadata?.est_minutes && !node.lesson_completed ? `<span class="xs muted">${icon("clock", 13)} ~${node.metadata.est_minutes} min</span>` : ""}
          <span class="xs muted">${node.items.length} ${node.items.length === 1 ? "tarjeta" : "tarjetas"}</span>
        </div>
      </div>
      <div class="lesson-spotlight-grid">
        <span class="lesson-spotlight-num tabular" aria-hidden="true">${numStr}</span>
        <div class="grow stack-sm">
          <h3 class="title-sm m-0">${esc(stripNum(node.title))}</h3>
          <p class="secondary m-0">${esc(node.summary)}</p>
          ${
            node.lesson_completed && node.mastery_pct > 0
              ? `<div class="lesson-inline-progress">
                  <div class="progress-track grow"><div class="progress-fill" style="width:${node.mastery_pct}%;"></div></div>
                  <span class="xs muted tabular">${node.mastery_pct}% afianzado</span>
                </div>`
              : ""
          }
        </div>
        <div class="lesson-spotlight-actions">
          ${renderPrimaryAction(node, { emphasis: true })}
          ${node.lesson_completed ? `<a href="#/learn/${node.id}" class="btn btn-text btn-sm">Releer lección</a>` : ""}
        </div>
      </div>
      <div class="lesson-spotlight-foot">
        ${renderCardsDrawer(node)}
      </div>
    </article>`;
}

function renderUnlockedRow(node, { showStageBadge }) {
  const st = STATUS_META[node.status] || STATUS_META.available;
  const numStr = String(node._displayNum).padStart(2, "0");
  const marker =
    node.status === "mastered"
      ? `<span class="lesson-marker is-mastered" aria-label="Dominado">${icon("check", 15)}</span>`
      : `<span class="lesson-marker is-${esc(node.status)} tabular" aria-hidden="true">${numStr}</span>`;

  return `
    <article class="lesson-row is-${esc(node.status)}" id="node-${esc(node.slug)}">
      ${marker}
      <div class="lesson-row-main">
        <div class="lesson-row-head">
          <div class="grow">
            <div class="row gap-sm" style="margin-bottom:4px;">
              <h3 class="lesson-row-title m-0">${esc(stripNum(node.title))}</h3>
              <span class="pill ${st.cls}">${st.label}</span>
              ${showStageBadge && node._secName ? `<span class="pill">${esc(node._secName)}</span>` : ""}
            </div>
            <p class="muted small m-0">${esc(node.summary)}</p>
          </div>
          <div class="lesson-row-actions">
            ${renderPrimaryAction(node, { emphasis: node.due_count > 0 })}
            ${node.lesson_completed ? `<a href="#/learn/${node.id}" class="btn btn-text btn-sm">Releer</a>` : ""}
          </div>
        </div>
        <div class="lesson-row-meta">
          ${node.metadata?.est_minutes && !node.lesson_completed ? `<span class="xs muted">~${node.metadata.est_minutes} min</span>` : ""}
          ${
            node.lesson_completed && node.mastery_pct > 0
              ? `<div class="lesson-inline-progress" style="max-width:240px;">
                  <div class="progress-track grow"><div class="progress-fill" style="width:${node.mastery_pct}%;"></div></div>
                  <span class="xs muted tabular">${node.mastery_pct}%</span>
                </div>`
              : ""
          }
        </div>
        ${renderCardsDrawer(node)}
      </div>
    </article>`;
}

function renderLockedRow(node, { showStageBadge }) {
  const numStr = String(node._displayNum).padStart(2, "0");
  const unmet = node.unmet_prerequisites || [];
  return `
    <details class="lesson-locked-row" id="node-${esc(node.slug)}">
      <summary class="lesson-locked-summary">
        <span class="lesson-marker is-locked tabular" aria-hidden="true">${numStr}</span>
        <div class="lesson-locked-copy grow">
          <div class="row gap-sm">
            <span class="lesson-locked-title">${esc(stripNum(node.title))}</span>
            ${showStageBadge && node._secName ? `<span class="pill">${esc(node._secName)}</span>` : ""}
          </div>
          <span class="xs muted truncate">${esc(node.summary)}</span>
        </div>
        <div class="lesson-locked-meta">
          ${node.metadata?.est_minutes ? `<span class="xs muted tabular">~${node.metadata.est_minutes} min</span>` : ""}
          <span class="lesson-lock-tag" title="Bloqueada hasta completar requisitos">${icon("lock", 13)}</span>
          ${icon("arrowDown", 14, "locked-chev")}
        </div>
      </summary>
      <div class="lesson-locked-body">
        <p class="small secondary m-0">${esc(node.summary)}</p>
        ${
          unmet.length
            ? `<div class="callout small">
                <strong>Antes:</strong> ${unmet
                  .map((p) => `${esc(stripNum(p.title))} <span class="muted">(${p.lesson_completed ? "practicá sus tarjetas" : "completá la lección"})</span>`)
                  .join(", ")}.
              </div>`
            : ""
        }
        <div class="row">
          <button class="btn btn-secondary btn-sm unlock-btn" data-node-id="${node.id}" type="button">${icon("unlock", 14)} Ya lo sé, desbloquear</button>
          ${node.has_lesson !== false ? `<a href="#/learn/${node.id}" class="btn btn-text btn-sm">${icon("bookOpen", 14)} Ir a la lección igual</a>` : ""}
        </div>
        ${renderCardsDrawer(node)}
      </div>
    </details>`;
}

function renderGroupedNodes(list, { focusNode, toPractice, allowSpotlight, showStageBadge }) {
  const blocks = [];
  let panelBuffer = [];

  const flushPanel = () => {
    if (!panelBuffer.length) return;
    blocks.push(`<div class="curriculum-panel">${panelBuffer.join("")}</div>`);
    panelBuffer = [];
  };

  for (const node of list) {
    const isSpotlight = allowSpotlight && focusNode && node.id === focusNode.id && node.status !== "locked";
    if (isSpotlight) {
      flushPanel();
      blocks.push(
        renderSpotlight(node, {
          isToPractice: Boolean(toPractice && toPractice.id === node.id),
          showStageBadge,
        })
      );
    } else if (node.status === "locked") {
      panelBuffer.push(renderLockedRow(node, { showStageBadge }));
    } else {
      panelBuffer.push(renderUnlockedRow(node, { showStageBadge }));
    }
  }
  flushPanel();
  return blocks.join("");
}

export async function renderRoadmap(container, slug, opts = {}) {
  const data = await api.get(`/api/domains/${encodeURIComponent(slug)}/roadmap`);
  const { domain, nodes, remediation_hints } = data;
  const tips = domain.config?.method_tips || [];
  const tone = toneOf(domain.lab_type);
  const labEntry = LAB_ROUTES[domain.lab_type] || null;

  const lessonsDone = nodes.filter((n) => n.lesson_completed).length;
  const mastered = nodes.filter((n) => n.status === "mastered").length;
  const dueTotal = nodes.reduce((a, n) => a + (n.due_count || 0), 0);
  const overallPct = nodes.length ? Math.round((lessonsDone / nodes.length) * 100) : 0;

  const nextNode =
    nodes.find((n) => ["available", "in_progress"].includes(n.status) && !n.lesson_completed) ||
    nodes.find((n) => n.status === "in_progress") ||
    null;

  // A learned lesson whose cards were never practised blocks the next one: surface it first
  const toPractice = nodes.find((n) => n.lesson_completed && n.items.length && n.practiced_pct < 60) || null;
  const focusNode = toPractice || nextNode || null;

  // Group multi-stage courses (explicit metadata.section, or fallback to level groups for custom subjects)
  const hasExplicitSections = nodes.some((n) => Boolean(n.metadata?.section));
  const distinctLevels = new Set(nodes.map((n) => n.level).filter((lvl) => lvl != null));
  const fallbackByLevel = !hasExplicitSections && distinctLevels.size >= 2;

  const sections = [];
  for (const n of nodes) {
    const secName = hasExplicitSections
      ? n.metadata?.section || ""
      : fallbackByLevel
      ? `Nivel ${n.level}`
      : "";
    if (!secName) continue;
    let entry = sections.find((s) => s.name === secName);
    if (!entry) {
      entry = {
        key: `sec-${sections.length + 1}`,
        index: sections.length,
        name: secName,
        nodes: [],
        total: 0,
        done: 0,
        mastered: 0,
        due: 0,
        estMinutes: 0,
      };
      sections.push(entry);
    }
    entry.nodes.push(n);
    entry.total += 1;
    if (n.lesson_completed) entry.done += 1;
    if (n.status === "mastered") entry.mastered += 1;
    entry.due += n.due_count || 0;
    entry.estMinutes += Number(n.metadata?.est_minutes) || 0;
  }

  const hasSections = sections.length >= 2;
  if (hasSections) {
    for (const s of sections) {
      s.nodes.forEach((n, idx) => {
        n._secKey = s.key;
        n._secName = s.name;
        n._displayNum = idx + 1;
      });
    }
  } else {
    nodes.forEach((n, idx) => {
      n._secKey = "";
      n._secName = "";
      n._displayNum = idx + 1;
    });
  }

  const currentSection = hasSections
    ? sections.find((s) => focusNode && s.nodes.some((n) => n.id === focusNode.id)) ||
      sections.find((s) => s.done < s.total) ||
      sections[0]
    : null;

  const validStageKeys = new Set([ALL_STAGES, ...sections.map((s) => s.key)]);
  const requestedStage = opts.stage || readSavedStage(slug);
  const initialStage = hasSections
    ? validStageKeys.has(requestedStage)
      ? requestedStage
      : currentSection.key
    : ALL_STAGES;

  const state = {
    stage: initialStage,
    query: opts.query || "",
    filter: opts.filter || "all",
  };

  const showToolbar = nodes.length > 0;

  container.innerHTML = `
    <section class="band dots page-header" data-tone="${tone}">
      <div>
        <div class="breadcrumb"><a href="#/aprender">Aprender</a> <span>/</span> <span>${esc(domain.name)}</span></div>
        <h1>${esc(domain.name)}</h1>
        <p>${esc(domain.description)}</p>
        <div class="row mt-lg">
          ${
            dueTotal > 0
              ? `<a href="#/review?domain=${esc(domain.slug)}" class="btn btn-primary">Repasar (${dueTotal}) ${icon("arrowRight", 16)}</a>`
              : toPractice
              ? `<a href="#/review?node=${toPractice.id}" class="btn btn-primary">Practicar: ${esc(stripNum(toPractice.title))} ${icon("arrowRight", 16)}</a>`
              : nextNode && !nextNode.lesson_completed
              ? `<a href="#/learn/${nextNode.id}" class="btn btn-primary">${lessonsDone ? "Seguir" : "Empezar"}: ${esc(stripNum(nextNode.title))} ${icon("arrowRight", 16)}</a>`
              : ""
          }
          ${labEntry ? `<a href="${labEntry}" class="btn btn-secondary">${icon("flask", 16)} Laboratorio</a>` : ""}
        </div>
      </div>
      <div class="roadmap-hero-stats">
        <div class="row" style="gap:32px;">
          <div class="stat"><span class="num num-xl">${lessonsDone}<span style="font-size:0.5em;opacity:0.7;"> / ${nodes.length}</span></span><span class="stat-label">lecciones</span></div>
          <div class="stat"><span class="num num-xl">${mastered}</span><span class="stat-label">${mastered === 1 ? "tema dominado" : "temas dominados"}</span></div>
        </div>
        ${
          nodes.length
            ? `<div class="roadmap-hero-bar">
                <div class="progress-track"><div class="progress-fill" style="width:${overallPct}%;"></div></div>
                <span class="xs muted tabular">${overallPct}% completado${hasSections ? ` · ${sections.length} etapas` : ""}</span>
              </div>`
            : ""
        }
      </div>
    </section>

    ${
      remediation_hints.length
        ? `<div class="card callout-warn stack-sm mb-lg">
            <h3 class="m-0">${icon("alert", 16)} Conviene reforzar la base</h3>
            ${remediation_hints.map((h) => `<p class="m-0">${esc(h.reason)}</p>`).join("")}
          </div>`
        : ""
    }

    <div class="roadmap-shell ${hasSections ? "has-sidebar" : ""}" data-tone="${tone}">
      ${
        hasSections
          ? `<aside class="roadmap-sidebar" aria-label="Etapas del curso">
              <div class="stage-sidebar-head">
                <span class="eyebrow m-0">Etapas del curso</span>
                <span class="xs muted tabular">${sections.length}</span>
              </div>
              <nav class="stage-nav">
                ${sections
                  .map((s) => {
                    const pct = s.total ? Math.round((s.done / s.total) * 100) : 0;
                    const isComplete = s.total > 0 && s.done >= s.total;
                    const isCurrent = currentSection && s.key === currentSection.key;
                    return `
                    <button type="button" class="stage-btn ${state.stage === s.key ? "active" : ""} ${isComplete ? "is-complete" : ""}" data-stage="${s.key}">
                      <span class="stage-idx tabular" aria-hidden="true">${isComplete ? icon("check", 13) : String(s.index + 1).padStart(2, "0")}</span>
                      <span class="stage-info">
                        <span class="stage-name">${esc(s.name)}</span>
                        ${
                          pct > 0 && !isComplete
                            ? `<span class="stage-micro-bar"><span style="width:${pct}%;"></span></span>`
                            : isCurrent
                            ? `<span class="stage-current-tag">Tu paso actual</span>`
                            : ""
                        }
                      </span>
                      <span class="stage-count tabular">${s.done}/${s.total}</span>
                    </button>`;
                  })
                  .join("")}
              </nav>
              <div class="stage-sidebar-foot">
                <button type="button" class="stage-all-btn ${state.stage === ALL_STAGES ? "active" : ""}" data-stage="${ALL_STAGES}">
                  ${icon("layers", 15)}
                  <span>Todas las etapas</span>
                  <span class="stage-count tabular">${nodes.length}</span>
                </button>
              </div>
            </aside>`
          : ""
      }

      <div class="roadmap-main">
        ${
          hasSections
            ? `<div class="stage-mobile-bar" aria-label="Cambiar de etapa">
                <button type="button" class="icon-btn stage-prev-mobile" aria-label="Etapa anterior">${icon("arrowLeft", 16)}</button>
                <select class="stage-select" id="stage-mobile-select" aria-label="Elegir etapa">
                  ${sections
                    .map(
                      (s) =>
                        `<option value="${s.key}" ${state.stage === s.key ? "selected" : ""}>${String(s.index + 1).padStart(2, "0")} · ${esc(s.name)} (${s.done}/${s.total})</option>`
                    )
                    .join("")}
                  <option value="${ALL_STAGES}" ${state.stage === ALL_STAGES ? "selected" : ""}>Todas las etapas (${nodes.length})</option>
                </select>
                <button type="button" class="icon-btn stage-next-mobile" aria-label="Siguiente etapa">${icon("arrowRight", 16)}</button>
              </div>`
            : ""
        }

        ${
          showToolbar
            ? `<div class="roadmap-toolbar">
                <div class="roadmap-search">
                  ${icon("search", 16, "roadmap-search-ico")}
                  <input type="search" id="roadmap-search-input" value="${esc(state.query)}" placeholder="Buscar tema en ${esc(domain.name)}..." aria-label="Buscar tema" autocomplete="off" />
                  <button type="button" class="roadmap-search-clear" id="roadmap-search-clear" aria-label="Limpiar búsqueda" ${state.query ? "" : "hidden"}>${icon("x", 14)}</button>
                </div>
                <div class="segmented" role="group" aria-label="Filtrar lecciones">
                  <button type="button" class="seg-btn ${state.filter === "all" ? "active" : ""}" data-filter="all">Todas</button>
                  <button type="button" class="seg-btn ${state.filter === "available" ? "active" : ""}" data-filter="available">Disponibles</button>
                  <button type="button" class="seg-btn ${state.filter === "done" ? "active" : ""}" data-filter="done">Completadas</button>
                </div>
              </div>`
            : ""
        }

        <div id="roadmap-stage-view" class="stack"></div>
      </div>
    </div>

    ${
      tips.length
        ? `<section class="section">
            <div class="section-head"><h2>Cómo practicar ${esc(domain.name.toLowerCase())}</h2></div>
            <div class="grid-3">
              ${tips.map((t, i) => `<div class="stack-sm"><span class="num num-lg" style="color:var(--tone, var(--accent));">${i + 1}</span><p class="m-0">${esc(t)}</p></div>`).join("")}
            </div>
          </section>`
        : ""
    }
  `;

  const stageView = container.querySelector("#roadmap-stage-view");
  const shellEl = container.querySelector(".roadmap-shell");
  const searchInput = container.querySelector("#roadmap-search-input");
  const searchClear = container.querySelector("#roadmap-search-clear");
  const mobileSelect = container.querySelector("#stage-mobile-select");
  const prevMobileBtn = container.querySelector(".stage-prev-mobile");
  const nextMobileBtn = container.querySelector(".stage-next-mobile");

  function syncNavUI() {
    if (!hasSections) return;
    container.querySelectorAll(".stage-btn, .stage-all-btn").forEach((btn) => {
      btn.classList.toggle("active", !normSearch(state.query) && btn.dataset.stage === state.stage);
    });
    if (mobileSelect && mobileSelect.value !== state.stage) {
      mobileSelect.value = state.stage;
    }
    const idx = sections.findIndex((s) => s.key === state.stage);
    if (prevMobileBtn) prevMobileBtn.disabled = idx <= 0;
    if (nextMobileBtn) nextMobileBtn.disabled = idx < 0 || idx >= sections.length - 1;
  }

  function applyFilter(list) {
    if (state.filter === "available") {
      return list.filter((n) => n.status === "available" || n.status === "in_progress");
    }
    if (state.filter === "done") {
      return list.filter((n) => n.lesson_completed || n.status === "mastered");
    }
    return list;
  }

  function selectStage(stageKey, { scroll = false } = {}) {
    state.stage = stageKey;
    saveStage(slug, stageKey);
    if (state.query) {
      state.query = "";
      if (searchInput) searchInput.value = "";
      if (searchClear) searchClear.hidden = true;
    }
    renderStageContent();
    if (scroll && shellEl) {
      const top = shellEl.getBoundingClientRect().top + window.scrollY - 88;
      window.scrollTo({ top: Math.max(0, top), behavior: "smooth" });
    }
  }

  function renderStageContent() {
    syncNavUI();

    if (!nodes.length) {
      stageView.innerHTML = `<div class="empty">Esta materia todavía no tiene lecciones. Agregalas desde el <a class="link" href="#/creator">editor</a>.</div>`;
      return;
    }

    const q = normSearch(state.query);
    let html = "";

    if (q) {
      // Cross-stage search across the entire curriculum
      const matched = applyFilter(
        nodes.filter((n) => {
          const hay = `${stripNum(n.title)} ${n.summary} ${n._secName}`;
          if (normSearch(hay).includes(q)) return true;
          return n.items.some((it) => normSearch(it.title).includes(q));
        })
      );

      html += `
        <div class="stage-header-inline">
          <span class="small muted">${matched.length} ${matched.length === 1 ? "resultado" : "resultados"} para «${esc(state.query.trim())}»${hasSections ? " en todas las etapas" : ""}</span>
          <button type="button" class="btn btn-text btn-sm clear-filters-btn">Limpiar búsqueda</button>
        </div>`;

      if (!matched.length) {
        html += `<div class="empty">No encontramos temas que coincidan con «${esc(state.query.trim())}». Probá con otra palabra o limpiá los filtros.</div>`;
      } else {
        html += renderGroupedNodes(matched, {
          focusNode,
          toPractice,
          allowSpotlight: false,
          showStageBadge: hasSections,
        });
      }
    } else if (hasSections && state.stage === ALL_STAGES) {
      const totalFiltered = applyFilter(nodes);
      html += `
        <div class="stage-header">
          <div class="stage-header-top">
            <span class="eyebrow m-0"><span class="eyebrow-dot" style="background:var(--tone);"></span>Programa completo</span>
            <span class="xs muted tabular">${sections.length} etapas · ${nodes.length} lecciones</span>
          </div>
          <div class="row-between">
            <h2 class="title-md m-0">Todas las etapas</h2>
            <span class="small muted tabular">${lessonsDone} de ${nodes.length} completadas</span>
          </div>
        </div>`;

      if (!totalFiltered.length) {
        html += `<div class="empty">No hay lecciones en este filtro todavía. <button type="button" class="btn btn-text btn-sm clear-filters-btn">Ver todas</button></div>`;
      } else {
        for (const sec of sections) {
          const secFiltered = applyFilter(sec.nodes);
          if (!secFiltered.length) continue;
          html += `
            <section class="stack-sm">
              <div class="row-between stage-all-heading">
                <div class="row gap-sm">
                  <span class="xs muted tabular">${String(sec.index + 1).padStart(2, "0")}</span>
                  <h3 class="title-sm m-0">${esc(sec.name)}</h3>
                </div>
                <div class="row gap-sm">
                  <span class="xs muted tabular">${sec.done}/${sec.total}</span>
                  <button type="button" class="btn btn-text btn-sm stage-jump-btn" data-stage="${sec.key}">Enfocar ${icon("arrowRight", 13)}</button>
                </div>
              </div>
              ${renderGroupedNodes(secFiltered, {
                focusNode,
                toPractice,
                allowSpotlight: state.filter === "all",
                showStageBadge: false,
              })}
            </section>`;
        }
      }
    } else if (hasSections) {
      const sec = sections.find((s) => s.key === state.stage) || sections[0];
      const secPct = sec.total ? Math.round((sec.done / sec.total) * 100) : 0;
      const filtered = applyFilter(sec.nodes);
      const prevSec = sec.index > 0 ? sections[sec.index - 1] : null;
      const nextSec = sec.index < sections.length - 1 ? sections[sec.index + 1] : null;

      html += `
        <div class="stage-header">
          <div class="stage-header-top">
            <span class="eyebrow m-0"><span class="eyebrow-dot" style="background:var(--tone);"></span>Etapa ${sec.index + 1} de ${sections.length}</span>
            ${sec.estMinutes ? `<span class="xs muted">${icon("clock", 13)} ${formatEstTime(sec.estMinutes)} estimados</span>` : ""}
          </div>
          <div class="row-between">
            <h2 class="title-md m-0">${esc(sec.name)}</h2>
            <div class="row gap-sm">
              ${sec.due > 0 ? `<span class="pill pill-amber">${sec.due} para repasar</span>` : ""}
              <span class="small muted tabular">${sec.done} de ${sec.total} completadas</span>
            </div>
          </div>
          <div class="progress-track stage-progress"><div class="progress-fill" style="width:${secPct}%;"></div></div>
        </div>`;

      if (!filtered.length) {
        html += `
          <div class="empty row-between">
            <span>No hay lecciones en esta etapa con el filtro actual.</span>
            <button type="button" class="btn btn-text btn-sm clear-filters-btn">Mostrar todas</button>
          </div>`;
      } else {
        html += renderGroupedNodes(filtered, {
          focusNode,
          toPractice,
          allowSpotlight: state.filter === "all",
          showStageBadge: false,
        });
      }

      if (prevSec || nextSec) {
        html += `
          <nav class="stage-footer" aria-label="Navegar entre etapas">
            ${
              prevSec
                ? `<button type="button" class="stage-footer-btn stage-jump-btn" data-stage="${prevSec.key}">
                    <span class="xs muted">${icon("arrowLeft", 13)} Etapa anterior</span>
                    <strong>${esc(prevSec.name)}</strong>
                  </button>`
                : `<span></span>`
            }
            ${
              nextSec
                ? `<button type="button" class="stage-footer-btn is-next stage-jump-btn" data-stage="${nextSec.key}">
                    <span class="xs muted">Siguiente etapa ${icon("arrowRight", 13)}</span>
                    <strong>${esc(nextSec.name)}</strong>
                  </button>`
                : `<span></span>`
            }
          </nav>`;
      }
    } else {
      // Single-stage roadmap (Física, Guitarra, Electrónica, custom)
      const filtered = applyFilter(nodes);
      if (!filtered.length) {
        html += `
          <div class="empty row-between">
            <span>No hay lecciones en este filtro todavía.</span>
            <button type="button" class="btn btn-text btn-sm clear-filters-btn">Mostrar todas</button>
          </div>`;
      } else {
        html += renderGroupedNodes(filtered, {
          focusNode,
          toPractice,
          allowSpotlight: state.filter === "all",
          showStageBadge: false,
        });
      }
    }

    stageView.innerHTML = html;
    bindStageInteractions();
  }

  function bindStageInteractions() {
    stageView.querySelectorAll(".unlock-btn").forEach((btn) => {
      btn.addEventListener("click", async () => {
        await api.post(`/api/nodes/${btn.dataset.nodeId}/unlock`);
        toast("Lección desbloqueada.", "ok");
        renderRoadmap(container, slug, { ...state });
      });
    });

    stageView.querySelectorAll(".quick-item-form").forEach((form) => {
      form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const fd = new FormData(form);
        try {
          await api.post("/api/items", {
            node_id: Number(form.dataset.nodeId),
            item_type: "recall",
            title: fd.get("title"),
            prompt: fd.get("prompt"),
            answer: fd.get("answer"),
          });
          toast("Tarjeta guardada.", "ok");
          await refreshSidebarDomains();
          renderRoadmap(container, slug, { ...state });
        } catch (err) {
          toast(err.message, "err");
        }
      });
    });

    stageView.querySelectorAll(".stage-jump-btn").forEach((btn) => {
      btn.addEventListener("click", () => selectStage(btn.dataset.stage, { scroll: true }));
    });

    stageView.querySelectorAll(".clear-filters-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        state.query = "";
        state.filter = "all";
        if (searchInput) searchInput.value = "";
        if (searchClear) searchClear.hidden = true;
        container.querySelectorAll(".seg-btn[data-filter]").forEach((b) => {
          b.classList.toggle("active", b.dataset.filter === "all");
        });
        renderStageContent();
      });
    });
  }

  // Bind persistent shell controls
  container.querySelectorAll(".stage-btn, .stage-all-btn").forEach((btn) => {
    btn.addEventListener("click", () => selectStage(btn.dataset.stage, { scroll: false }));
  });

  mobileSelect?.addEventListener("change", () => {
    selectStage(mobileSelect.value, { scroll: false });
  });

  prevMobileBtn?.addEventListener("click", () => {
    const idx = sections.findIndex((s) => s.key === state.stage);
    if (idx > 0) selectStage(sections[idx - 1].key, { scroll: false });
  });

  nextMobileBtn?.addEventListener("click", () => {
    const idx = sections.findIndex((s) => s.key === state.stage);
    if (idx >= 0 && idx < sections.length - 1) selectStage(sections[idx + 1].key, { scroll: false });
  });

  searchInput?.addEventListener("input", () => {
    state.query = searchInput.value;
    if (searchClear) searchClear.hidden = !state.query;
    renderStageContent();
  });

  searchClear?.addEventListener("click", () => {
    state.query = "";
    if (searchInput) {
      searchInput.value = "";
      searchInput.focus();
    }
    searchClear.hidden = true;
    renderStageContent();
  });

  container.querySelectorAll(".seg-btn[data-filter]").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.filter = btn.dataset.filter;
      container.querySelectorAll(".seg-btn[data-filter]").forEach((b) => {
        b.classList.toggle("active", b === btn);
      });
      renderStageContent();
    });
  });

  renderStageContent();
}
