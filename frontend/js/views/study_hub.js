import { icon } from "../icons.js";
import { subjectLogo } from "../art.js";
import { api, esc, rich, toast, toneOf } from "../main.js";

/**
 * Study Hub views:
 *   1. renderCheatsheet (#/formulario) — Printable formula & key-rules sheet grouped by unit.
 *   2. renderErrorBank  (#/errores)    — Weak exercises, error-tag distribution & high-lapse cards.
 *   3. renderNotebook   (#/cuaderno)   — Editable personal Feynman notes & exam bookmarks.
 */

const stripNum = (t) => String(t || "").replace(/^\d+\.\s*/, "");
const normSearch = (s) =>
  String(s || "")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .trim();

const INGRESO_DOMAINS = [
  { slug: "matematicas", name: "Matemática", lab: "math" },
  { slug: "fisica", name: "Física", lab: "physics" },
  { slug: "comprension-problemas", name: "Comprensión y Problemas", lab: "generic" },
];

/* ============================================================================
   1. FORMULA & SUMMARY SHEET (#/formulario)
   ============================================================================ */

export async function renderCheatsheet(container, domainSlug = "matematicas", { ingresoOnly = true } = {}) {
  const activeSlug = domainSlug || "matematicas";
  const data = await api.get(`/api/cheatsheet/${encodeURIComponent(activeSlug)}?ingreso=${ingresoOnly ? "1" : "0"}`);
  const { domain, groups } = data;
  const tone = toneOf(domain.lab_type);

  const state = {
    query: "",
    unitCode: "__all__",
    showPoints: false,
  };

  container.innerHTML = `
    <section class="band dots page-header no-print" data-tone="${tone}">
      <div>
        <div class="breadcrumb"><a href="#/ingreso">Ingreso</a> <span>/</span> <span>Formulario y resúmenes</span></div>
        <h1>Formulario de <em>${esc(domain.name)}</em></h1>
        <p>Reglas clave y errores típicos de cada tema del programa en un solo lugar. Ideal para repasar antes de un parcial.</p>
        <div class="row mt-md">
          <button type="button" class="btn btn-primary" id="cs-print">${icon("download", 16)} Imprimir / Guardar PDF</button>
          <a href="#/ingreso?materia=${activeSlug === "matematicas" ? "matematica" : activeSlug === "fisica" ? "fisica" : "clyrp"}" class="btn btn-secondary">Volver a Ingreso</a>
        </div>
      </div>
      <div class="stat">
        <span class="num num-xl tabular">${data.topics_total}</span>
        <span class="stat-label">temas resumidos · ${groups.length} unidades</span>
      </div>
    </section>

    <div class="print-only-header">
      <h1>Formulario · ${esc(domain.name)} (${data.ingreso_only ? "Ingreso UNCuyo 2027" : "Ruta completa"})</h1>
    </div>

    <div class="row-between mb-md no-print">
      <div class="tabs m-0" style="margin-bottom:0;">
        ${INGRESO_DOMAINS.map(
          (d) =>
            `<a href="#/formulario/${esc(d.slug)}" class="tab-btn ${d.slug === activeSlug ? "active" : ""}">${subjectLogo(d.slug, 16)} ${esc(d.name)}</a>`
        ).join("")}
      </div>
      <label class="row gap-sm small" style="cursor:pointer;">
        <input type="checkbox" id="cs-points-toggle" style="width:18px;height:18px;min-height:0;" />
        <span>Mostrar apuntes detallados</span>
      </label>
    </div>

    <div class="roadmap-toolbar mb-lg no-print">
      <label class="roadmap-search">
        ${icon("search", 16, "roadmap-search-ico")}
        <input type="search" id="cs-search" placeholder="Buscar fórmula, propiedad o tema…" autocomplete="off" />
      </label>
      <div class="segmented" id="cs-units" role="group" aria-label="Filtrar unidad">
        <button type="button" class="seg-btn active" data-u="__all__">Todas</button>
        ${groups.map((g) => `<button type="button" class="seg-btn" data-u="${esc(g.code)}">${esc(g.code)}</button>`).join("")}
      </div>
    </div>

    <div id="cs-body" class="stack-lg" data-tone="${tone}"></div>
  `;

  const body = container.querySelector("#cs-body");

  function paint() {
    const q = normSearch(state.query);
    const filteredGroups = groups
      .filter((g) => state.unitCode === "__all__" || g.code === state.unitCode)
      .map((g) => ({
        ...g,
        topics: g.topics.filter(
          (t) => !q || normSearch(`${t.title} ${t.key_rule} ${t.pitfall} ${t.summary}`).includes(q)
        ),
      }))
      .filter((g) => g.topics.length > 0);

    if (!filteredGroups.length) {
      body.innerHTML = `<div class="empty">No hay fórmulas que coincidan con «${esc(state.query)}».</div>`;
      return;
    }

    body.innerHTML = filteredGroups
      .map(
        (g) => `
      <section class="stack cs-group">
        <div class="row-between">
          <div class="row gap-sm">
            <span class="pill pill-tone tabular">${esc(g.code)}</span>
            <h2 class="title-md m-0">${esc(g.short_title)}</h2>
          </div>
          <span class="xs muted tabular">${g.topics.length} temas</span>
        </div>
        <div class="grid-2 cs-grid">
          ${g.topics
            .map(
              (t) => `
            <article class="card stack-sm cs-card">
              <div class="row-between row-top">
                <a href="#/learn/${t.node_id}" class="list-title link">${esc(stripNum(t.title))}</a>
                ${t.lesson_completed ? `<span class="pill pill-green no-print">${icon("check", 11)} Visto</span>` : ""}
              </div>
              ${
                t.key_rule
                  ? `<div class="card-tone cs-rule"><span class="eyebrow m-0" style="margin-bottom:4px;">Fórmula / Regla clave</span><div class="rich small">${rich(t.key_rule)}</div></div>`
                  : `<p class="small muted m-0">${esc(t.summary)}</p>`
              }
              ${
                t.pitfall
                  ? `<div class="callout callout-warn xs m-0"><strong>Ojo:</strong> <span class="rich">${rich(t.pitfall)}</span></div>`
                  : ""
              }
              ${
                state.showPoints && t.points?.length
                  ? `<ul class="ex-list xs muted">${t.points.map((p) => `<li class="rich">${rich(p)}</li>`).join("")}</ul>`
                  : ""
              }
            </article>`
            )
            .join("")}
        </div>
      </section>`
      )
      .join("");
  }

  container.querySelector("#cs-print")?.addEventListener("click", () => window.print());
  container.querySelector("#cs-search")?.addEventListener("input", (e) => {
    state.query = e.target.value;
    paint();
  });
  container.querySelector("#cs-points-toggle")?.addEventListener("change", (e) => {
    state.showPoints = e.target.checked;
    paint();
  });
  container.querySelectorAll("#cs-units [data-u]").forEach((b) =>
    b.addEventListener("click", () => {
      state.unitCode = b.dataset.u;
      container.querySelectorAll("#cs-units [data-u]").forEach((x) => x.classList.toggle("active", x === b));
      paint();
    })
  );

  paint();
}

/* ============================================================================
   2. ERROR BANK (#/errores)
   ============================================================================ */

export async function renderErrorBank(container, { domain = null } = {}) {
  const activeDomain = domain || "";
  const url = `/api/errors?ingreso=1${activeDomain ? `&domain=${encodeURIComponent(activeDomain)}` : ""}`;
  const data = await api.get(url);
  const { weak_exercises, weak_cards, tag_counts, totals, error_tags } = data;
  const maxTag = Math.max(1, ...tag_counts.map((t) => t.count));

  container.innerHTML = `
    <section class="band dots page-header" data-tone="brand">
      <div>
        <div class="breadcrumb"><a href="#/ingreso">Ingreso</a> <span>/</span> <span>Banco de errores</span></div>
        <h1>Tus <em>puntos débiles</em></h1>
        <p>Todos los ejercicios que fallaste o resolviste mirando la solución se agendan automáticamente para reintento, junto a las tarjetas con más olvidos.</p>
        ${
          weak_exercises.length
            ? `<div class="row mt-md">
                <a href="#/ejercicios/reintentos${activeDomain ? `?domain=${esc(activeDomain)}` : ""}" class="btn btn-primary">${icon("refresh", 16)} Reintentar en tanda (${weak_exercises.length})</a>
              </div>`
            : ""
        }
      </div>
      <div class="ing-hero-kpis">
        <div class="stat">
          <span class="num num-xl tabular">${totals.unsolved_exercises}</span>
          <span class="stat-label">sin resolver</span>
        </div>
        <div class="stat">
          <span class="num num-xl tabular">${totals.solution_assisted}</span>
          <span class="stat-label">con ayuda</span>
        </div>
        <div class="stat">
          <span class="num num-xl tabular">${totals.weak_cards}</span>
          <span class="stat-label">tarjetas difíciles</span>
        </div>
      </div>
    </section>

    <div class="tabs">
      <a href="#/errores" class="tab-btn ${!activeDomain ? "active" : ""}">Todas las materias</a>
      ${INGRESO_DOMAINS.map(
        (d) => `<a href="#/errores?domain=${esc(d.slug)}" class="tab-btn ${activeDomain === d.slug ? "active" : ""}">${subjectLogo(d.slug, 16)} ${esc(d.name)}</a>`
      ).join("")}
    </div>

    ${
      tag_counts.some((t) => t.count > 0)
        ? `<section class="card stack mb-lg">
            <h3 class="m-0">¿Por qué te estás equivocando?</h3>
            <div class="stack-sm">
              ${tag_counts
                .map(
                  (t) => `
                <div class="energy-bar-row" style="grid-template-columns:160px 1fr 42px;">
                  <span class="small">${esc(t.label)}</span>
                  <div class="energy-track"><div class="energy-fill" style="width:${Math.round((t.count / maxTag) * 100)}%;background:var(--warn);"></div></div>
                  <span class="small tabular" style="text-align:right;">${t.count}</span>
                </div>`
                )
                .join("")}
            </div>
          </section>`
        : ""
    }

    <div class="grid-asymmetric">
      <section class="stack">
        <div class="row-between">
          <h2 class="title-md m-0">Ejercicios a reintentar sin ayuda</h2>
          <span class="xs muted tabular">${weak_exercises.length}</span>
        </div>
        ${
          weak_exercises.length
            ? `<div class="card"><div class="list">
                ${weak_exercises
                  .map(
                    (e) => `
                  <div class="list-row err-row">
                    <div class="grow stack-sm" style="gap:4px;">
                      <div class="row gap-sm">
                        <a href="#/ejercicios/${esc(e.domain_slug)}/${esc(e.node_slug)}?e=${esc(e.exercise_id)}" class="list-title link">${esc(e.title)}</a>
                        <span class="pill ${e.solved ? "pill-amber" : "pill-red"}">${e.solved ? "Resuelto con solución" : `${e.fails} ${e.fails === 1 ? "fallo" : "fallos"}`}</span>
                        ${e.retry_due ? `<span class="pill pill-accent">Reintentar hoy</span>` : e.next_retry_at ? `<span class="xs muted">Próximo: ${esc(e.next_retry_at.slice(0, 10))}</span>` : ""}
                        ${e.error_tag_label ? `<span class="pill">${esc(e.error_tag_label)}</span>` : ""}
                      </div>
                      <span class="xs muted">${esc(e.domain_name)} · ${esc(stripNum(e.node_title))}${e.source ? ` · ${esc(e.source)}` : ""}</span>
                      <div class="row gap-sm mt-sm">
                        <a href="#/ejercicios/${esc(e.domain_slug)}/${esc(e.node_slug)}?e=${esc(e.exercise_id)}" class="btn btn-primary btn-sm">Reintentar</a>
                        <button type="button" class="btn btn-secondary btn-sm err-to-card" data-ex="${esc(e.exercise_id)}">${icon("plus", 13)} Pasar a tarjeta FSRS</button>
                        <select class="err-tag-sel" data-ex="${esc(e.exercise_id)}" aria-label="Tipo de error">
                          <option value="">Etiquetar error…</option>
                          ${Object.entries(error_tags)
                            .map(([k, lbl]) => `<option value="${k}" ${e.error_tag === k ? "selected" : ""}>${esc(lbl)}</option>`)
                            .join("")}
                        </select>
                      </div>
                    </div>
                  </div>`
                  )
                  .join("")}
              </div></div>`
            : `<div class="card callout-ok stack-sm">
                <h3 class="m-0">Sin ejercicios pendientes en el banco de errores</h3>
                <p class="small m-0">A medida que resuelvas ejercicios o simulacros, acá van a aparecer automáticamente los que falles o los que resuelvas mirando la solución.</p>
                <div><a href="#/ingreso" class="btn btn-secondary btn-sm">Ir a Ingreso</a></div>
              </div>`
        }
      </section>

      <aside class="stack">
        <div class="row-between">
          <h2 class="title-md m-0">Tarjetas con olvidos</h2>
          <span class="xs muted tabular">${weak_cards.length}</span>
        </div>
        ${
          weak_cards.length
            ? `<div class="card"><div class="list">
                ${weak_cards
                  .slice(0, 15)
                  .map(
                    (c) => `
                  <div class="list-row" style="padding:12px 0;">
                    <div class="grow">
                      <div class="small"><strong>${esc(c.title)}</strong></div>
                      <div class="xs muted">${esc(c.domain_name)} · ${esc(stripNum(c.node_title))} · ${c.lapses} ${c.lapses === 1 ? "olvido" : "olvidos"}</div>
                    </div>
                    <a href="#/review?node=${c.node_id}" class="btn btn-secondary btn-sm">Repasar</a>
                  </div>`
                  )
                  .join("")}
              </div></div>`
            : `<div class="empty">Todavía no tenés tarjetas con olvidos registrados.</div>`
        }
      </aside>
    </div>
  `;

  container.querySelectorAll(".err-to-card").forEach((btn) =>
    btn.addEventListener("click", async () => {
      try {
        const res = await api.post(`/api/exercises/${encodeURIComponent(btn.dataset.ex)}/to-card`, {});
        toast(res.already_exists ? "Ese ejercicio ya tiene tarjeta en tu repaso." : "Tarjeta agregada a tu repaso FSRS.", "ok");
        btn.disabled = true;
        btn.textContent = "En tu repaso ✓";
      } catch (err) {
        toast(err.message, "err");
      }
    })
  );

  container.querySelectorAll(".err-tag-sel").forEach((sel) =>
    sel.addEventListener("change", async () => {
      try {
        await api.post(`/api/exercises/${encodeURIComponent(sel.dataset.ex)}/error-tag`, { error_tag: sel.value });
        toast("Tipo de error guardado", "ok");
      } catch (err) {
        toast(err.message, "err");
      }
    })
  );
}

/* ============================================================================
   3. STUDY NOTEBOOK & BOOKMARKS (#/cuaderno)
   ============================================================================ */

export async function renderNotebook(container, { domain = null, bookmarked = false } = {}) {
  const activeDomain = domain || "";
  const url = `/api/notes?${activeDomain ? `domain=${encodeURIComponent(activeDomain)}&` : ""}${bookmarked ? "bookmarked=1" : ""}`;
  const [data, searchIdx] = await Promise.all([api.get(url), api.get("/api/search-index")]);
  const { notes, totals } = data;

  const state = { query: "", adding: false };

  container.innerHTML = `
    <section class="band dots page-header" data-tone="brand">
      <div>
        <div class="breadcrumb"><a href="#/ingreso">Ingreso</a> <span>/</span> <span>Cuaderno de estudio</span></div>
        <h1>Tu <em>cuaderno</em></h1>
        <p>Tus resúmenes Feynman de cada lección, apuntes propios y temas marcados para repasar antes del examen.</p>
        <div class="row mt-md">
          <button type="button" class="btn btn-primary" id="nb-add-btn">${icon("plus", 16)} Nueva nota</button>
          <a href="#/formulario" class="btn btn-secondary">${icon("book", 16)} Ver formulario</a>
        </div>
      </div>
      <div class="ing-hero-kpis">
        <div class="stat"><span class="num num-xl tabular">${totals.total}</span><span class="stat-label">apuntes</span></div>
        <div class="stat"><span class="num num-xl tabular">${totals.bookmarked}</span><span class="stat-label">marcados ★</span></div>
      </div>
    </section>

    <div class="roadmap-toolbar mb-lg">
      <div class="tabs m-0" style="margin-bottom:0;">
        <a href="#/cuaderno" class="tab-btn ${!activeDomain && !bookmarked ? "active" : ""}">Todos</a>
        <a href="#/cuaderno?bookmarked=1" class="tab-btn ${bookmarked ? "active" : ""}">★ Para el parcial</a>
        ${INGRESO_DOMAINS.map(
          (d) => `<a href="#/cuaderno?domain=${esc(d.slug)}" class="tab-btn ${activeDomain === d.slug && !bookmarked ? "active" : ""}">${esc(d.name)}</a>`
        ).join("")}
      </div>
      <label class="roadmap-search">
        ${icon("search", 16, "roadmap-search-ico")}
        <input type="search" id="nb-search" placeholder="Buscar en tus apuntes…" autocomplete="off" />
      </label>
    </div>

    <div id="nb-new-host" class="mb-lg" hidden></div>
    <div id="nb-list" class="stack"></div>
  `;

  const listEl = container.querySelector("#nb-list");
  const newHost = container.querySelector("#nb-new-host");

  function renderNewForm() {
    newHost.hidden = !state.adding;
    if (!state.adding) return;
    const ingNodes = (searchIdx.nodes || []).filter((n) =>
      ["matematicas", "fisica", "comprension-problemas"].includes(n.domain_slug)
    );
    newHost.innerHTML = `
      <form class="card stack" id="nb-create-form">
        <h3 class="m-0">Agregar nota a un tema</h3>
        <label class="field">
          <span>Tema</span>
          <select name="node_id" required>
            ${ingNodes
              .map((n) => `<option value="${n.id}">${esc(n.domain_name)} · ${esc(stripNum(n.title))}</option>`)
              .join("")}
          </select>
        </label>
        <label class="field">
          <span>Tu apunte</span>
          <textarea name="content" placeholder="Fórmula clave, truco para no olvidarte o resumen en tus palabras…" required></textarea>
        </label>
        <label class="row gap-sm small" style="cursor:pointer;">
          <input type="checkbox" name="bookmarked" checked style="width:18px;height:18px;min-height:0;" />
          <span>Marcar ★ para repasar antes del parcial</span>
        </label>
        <div class="row">
          <button type="submit" class="btn btn-primary btn-sm">Guardar nota</button>
          <button type="button" class="btn btn-secondary btn-sm" id="nb-cancel-new">Cancelar</button>
        </div>
      </form>`;
    newHost.querySelector("#nb-cancel-new")?.addEventListener("click", () => {
      state.adding = false;
      renderNewForm();
    });
    newHost.querySelector("#nb-create-form")?.addEventListener("submit", async (e) => {
      e.preventDefault();
      const fd = new FormData(e.currentTarget);
      await api.put(`/api/notes/${fd.get("node_id")}`, {
        content: fd.get("content"),
        bookmarked: fd.get("bookmarked") === "on",
      });
      toast("Nota guardada", "ok");
      renderNotebook(container, { domain, bookmarked });
    });
  }

  function paintList() {
    const q = normSearch(state.query);
    const items = notes.filter((n) => !q || normSearch(`${n.node_title} ${n.content} ${n.domain_name}`).includes(q));
    if (!items.length) {
      listEl.innerHTML = `
        <div class="empty stack-sm">
          <p class="m-0">${q ? `Sin resultados para «${esc(state.query)}».` : "Todavía no tenés notas guardadas. Cada resumen que escribas al cerrar una lección aparece acá automáticamente, o podés crear una nota ahora."}</p>
        </div>`;
      return;
    }
    listEl.innerHTML = items
      .map(
        (n) => `
      <article class="card stack-sm nb-card" data-tone="${toneOf(n.lab_type)}" data-node="${n.node_id}">
        <div class="row-between row-top">
          <div class="stack-sm" style="gap:2px;">
            <div class="row gap-sm">
              <span class="pill pill-tone">${esc(n.domain_name)}</span>
              <a href="#/learn/${n.node_id}" class="list-title link">${esc(stripNum(n.node_title))}</a>
            </div>
            <span class="xs muted">${esc(n.node_summary)}</span>
          </div>
          <div class="row gap-sm">
            <button type="button" class="btn btn-sm ${n.bookmarked ? "btn-primary" : "btn-secondary"} nb-star" data-node="${n.node_id}" data-star="${n.bookmarked ? "1" : "0"}" title="Marcar para repasar antes del parcial">
              ${n.bookmarked ? "★ Marcado" : "☆ Marcar"}
            </button>
          </div>
        </div>
        <textarea class="nb-editor" data-node="${n.node_id}" rows="3" placeholder="Escribí tus apuntes de este tema…">${esc(n.content)}</textarea>
        <div class="row-between">
          <div class="row gap-sm">
            <button type="button" class="btn btn-secondary btn-sm nb-save" data-node="${n.node_id}">${icon("check", 13)} Guardar cambios</button>
            <a href="#/ejercicios/${esc(n.domain_slug)}/${esc(n.node_slug)}" class="btn btn-text btn-sm">Ir a ejercicios</a>
          </div>
          <span class="xs muted">Actualizado ${esc((n.updated_at || "").slice(0, 10))}</span>
        </div>
      </article>`
      )
      .join("");

    listEl.querySelectorAll(".nb-save").forEach((btn) =>
      btn.addEventListener("click", async () => {
        const nid = btn.dataset.node;
        const ta = listEl.querySelector(`.nb-editor[data-node="${nid}"]`);
        await api.put(`/api/notes/${nid}`, { content: ta.value });
        toast("Apunte guardado", "ok");
      })
    );
    listEl.querySelectorAll(".nb-star").forEach((btn) =>
      btn.addEventListener("click", async () => {
        const nid = btn.dataset.node;
        const next = btn.dataset.star !== "1";
        await api.put(`/api/notes/${nid}`, { bookmarked: next });
        toast(next ? "Marcado para antes del parcial" : "Marca quitada", "ok");
        renderNotebook(container, { domain, bookmarked });
      })
    );
  }

  container.querySelector("#nb-add-btn")?.addEventListener("click", () => {
    state.adding = !state.adding;
    renderNewForm();
  });
  container.querySelector("#nb-search")?.addEventListener("input", (e) => {
    state.query = e.target.value;
    paintList();
  });

  paintList();
}
