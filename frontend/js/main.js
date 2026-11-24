import { icon, resolveDomainIcon } from "./icons.js";
import { formatInlineCode } from "./math_render.js";
import { renderDashboard } from "./views/dashboard.js";
import { renderLearnIndex, renderLabsIndex } from "./views/library.js";
import { renderSettings } from "./views/settings.js";
import { renderRoadmap } from "./views/roadmap.js";
import { renderLearn } from "./views/learn.js";
import { renderReview } from "./views/review.js";
import { renderSession } from "./views/session.js";
import { renderCreator } from "./views/creator.js";
import { renderExercisesIndex, renderExerciseDomain, renderExerciseTopic, renderExerciseExam, renderExerciseRetries } from "./views/exercises.js";
import { renderIngreso } from "./views/ingreso.js";
import { renderCheatsheet, renderErrorBank, renderNotebook } from "./views/study_hub.js";
import { renderDiagnostic } from "./views/diagnostic.js";
import { renderGuitarLab } from "./labs/guitar_lab.js";
import { renderElectronicsLab } from "./labs/electronics_lab.js";
import { renderMathLab } from "./labs/math_lab.js";
import { renderPhysicsLab } from "./labs/physics_lab.js";

export const api = {
  async request(path, options = {}) {
    const res = await fetch(path, {
      headers: { "Content-Type": "application/json", ...(options.headers || {}) },
      ...options,
    });
    const data = await res.json().catch(() => ({}));
    if (res.status === 401 && data.pin_required) {
      showPinGate();
      throw new Error("Ingresá el PIN para continuar.");
    }
    if (!res.ok) {
      throw new Error(data.error || `Error HTTP ${res.status}`);
    }
    return data;
  },
  get(path) {
    return this.request(path, { method: "GET" });
  },
  post(path, body) {
    return this.request(path, { method: "POST", body: JSON.stringify(body || {}) });
  },
  put(path, body) {
    return this.request(path, { method: "PUT", body: JSON.stringify(body || {}) });
  },
  del(path) {
    return this.request(path, { method: "DELETE" });
  },
};

export function esc(str) {
  return String(str ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

/**
 * Tiny safe formatter for authored content: escapes HTML, allows **bold**,
 * typographic math/code `spans` and line breaks without pulling a Markdown lib.
 */
const richInline = (line) =>
  String(line ?? "")
    .split(/(`[^`]+`)/g)
    .map((part) => {
      if (part.length >= 2 && part.startsWith("`") && part.endsWith("`")) {
        return formatInlineCode(part.slice(1, -1));
      }
      return esc(part).replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
    })
    .join("");

const TABLE_ROW = /^\s*\|.*\|\s*$/;
const TABLE_RULE = /^\s*\|?(\s*:?-{3,}:?\s*\|)+\s*:?-{0,}:?\s*$/;
const tableCells = (row) => row.trim().replace(/^\|/, "").replace(/\|$/, "").split("|").map((c) => richInline(c.trim()));

/** A block of "| a | b |" lines becomes a table; a "|---|---|" second line marks a header row. */
function richTable(rows) {
  const hasHeader = rows.length > 1 && TABLE_RULE.test(rows[1]);
  const body = hasHeader ? rows.slice(2) : rows;
  const head = hasHeader ? `<thead><tr>${tableCells(rows[0]).map((c) => `<th>${c}</th>`).join("")}</tr></thead>` : "";
  return `<div class="rich-table-wrap"><table class="rich-table">${head}<tbody>${body
    .map((r) => `<tr>${tableCells(r).map((c) => `<td>${c}</td>`).join("")}</tr>`)
    .join("")}</tbody></table></div>`;
}

/** Minimal markup for authored content: **bold**, `code`, line breaks and pipe tables. */
export function rich(str) {
  const lines = String(str ?? "").split("\n");
  const out = [];
  let text = [];
  const flush = () => {
    if (text.length) out.push(text.map(richInline).join("<br>"));
    text = [];
  };
  for (let i = 0; i < lines.length; i += 1) {
    if (TABLE_ROW.test(lines[i])) {
      const rows = [];
      while (i < lines.length && (TABLE_ROW.test(lines[i]) || TABLE_RULE.test(lines[i]))) rows.push(lines[i++]);
      i -= 1;
      if (rows.length >= 2) {
        flush();
        out.push(richTable(rows));
        continue;
      }
      text.push(...rows);
      continue;
    }
    text.push(lines[i]);
  }
  flush();
  return out.join("");
}

export const TONES = ["guitar", "electronics", "math", "physics"];
export function toneOf(labType) {
  return TONES.includes(labType) ? labType : "generic";
}
export const LAB_ROUTES = {
  guitar: "#/lab/guitar",
  electronics: "#/lab/electronics",
  math: "#/lab/math",
  physics: "#/lab/physics",
};

function showPinGate() {
  const view = document.getElementById("app-view");
  if (!view || view.querySelector("#pin-form")) return;
  runCleanups();
  view.innerHTML = `
    <div class="pin-screen">
      <form id="pin-form" class="card stack" style="max-width:420px;width:100%;">
        <div class="eyebrow">Acceso desde la red</div>
        <h2>Ingresá el PIN</h2>
        <p class="muted">Lo muestra la consola de la computadora donde corre AprendeLab.</p>
        <input type="text" name="pin" inputmode="numeric" autocomplete="one-time-code" class="input-xl" placeholder="000000" required />
        <button class="btn btn-primary" type="submit">Entrar</button>
      </form>
    </div>`;
  view.querySelector("#pin-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const pin = new FormData(e.currentTarget).get("pin");
    const res = await fetch("/api/auth", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ pin }),
    });
    if (res.ok) location.reload();
    else toast("PIN incorrecto", "err");
  });
}

export function toast(message, type = "info") {
  const host = document.getElementById("toast-container");
  if (!host) return;
  const el = document.createElement("div");
  el.className = `toast ${type}`;
  el.innerHTML = `${type === "ok" ? icon("check", 14) : type === "err" ? icon("alert", 14) : icon("activity", 14)}<span>${esc(message)}</span>`;
  host.appendChild(el);
  setTimeout(() => {
    el.style.opacity = "0";
    el.style.transition = "opacity 0.25s";
    setTimeout(() => el.remove(), 260);
  }, 3200);
}

export function labLinkToHash(labLink) {
  if (!labLink) return null;
  const [lab, sub, item] = String(labLink).split(":");
  if (lab === "guitar") return `#/lab/guitar${sub ? "?tab=" + encodeURIComponent(sub) : ""}`;
  if (lab === "electronics") {
    // a third part picks what opens inside the tab: "electronics:arduino:blink", "electronics:sim:m2-rc"
    const extra = item ? `&${sub === "sim" ? "practice" : "ex"}=${encodeURIComponent(item)}` : "";
    return `#/lab/electronics${sub ? "?tab=" + encodeURIComponent(sub) + extra : ""}`;
  }
  if (lab === "math") return `#/lab/math${sub ? "?topic=" + encodeURIComponent(sub) : ""}`;
  if (lab === "physics") return `#/lab/physics${sub ? "?tab=" + encodeURIComponent(sub) : ""}`;
  return null;
}

const cleanups = [];

export function registerCleanup(fn) {
  if (typeof fn === "function") cleanups.push(fn);
}

function runCleanups() {
  while (cleanups.length) {
    const fn = cleanups.pop();
    try {
      fn();
    } catch {
      // ignore
    }
  }
}

export async function refreshSidebarDomains() {
  const pills = document.querySelectorAll("[data-due-pill]");
  if (!pills.length) return;
  try {
    const { domains } = await api.get("/api/domains");
    const totalDue = domains.reduce((acc, d) => acc + (d.due_count || 0), 0);
    pills.forEach((pill) => {
      pill.textContent = String(totalDue);
      pill.hidden = totalDue <= 0;
    });
  } catch {
    // non-fatal
  }
}

function renderMobileNav() {
  const nav = document.getElementById("mobile-nav");
  if (!nav) return;
  nav.innerHTML = `
    <a href="#/" data-nav="hoy">${icon("home", 20)}<span>Hoy</span></a>
    <a href="#/ingreso" data-nav="ingreso">${icon("target", 20)}<span>Ingreso</span></a>
    <a href="#/aprender" data-nav="aprender">${icon("bookOpen", 20)}<span>Aprender</span></a>
    <a href="#/review" data-nav="review">${icon("brain", 20)}<span>Repaso</span><span class="nav-count" data-due-pill hidden>0</span></a>
    <a href="#/ejercicios" data-nav="ejercicios">${icon("target", 20)}<span>Ejercicios</span></a>
    <a href="#/labs" data-nav="labs">${icon("flask", 20)}<span>Labs</span></a>
    <button type="button" id="mobile-more" aria-haspopup="true">${icon("more", 20)}<span>Más</span></button>
  `;
  nav.querySelector("#mobile-more").addEventListener("click", (e) => {
    e.stopPropagation();
    toggleMenu();
  });
}

/* ---------- Secondary menu ---------- */
function currentTheme() {
  return document.documentElement.getAttribute("data-theme") === "dark" ? "dark" : "light";
}

export function applyTheme(choice) {
  // choice: "light" | "dark" | "system"
  try {
    localStorage.setItem("aprendelab_theme", choice);
  } catch {
    // private mode: theme just won't persist on this device
  }
  const dark = choice === "dark" || (choice === "system" && window.matchMedia("(prefers-color-scheme: dark)").matches);
  document.documentElement.setAttribute("data-theme", dark ? "dark" : "light");
  api.put("/api/settings", { theme: choice }).catch(() => {});
}

function renderMenu() {
  const pop = document.getElementById("menu-pop");
  if (!pop) return;
  const dark = currentTheme() === "dark";
  pop.innerHTML = `
    <a class="menu-item" role="menuitem" href="#/session">${icon("zap", 18)}<span>Sesión guiada</span></a>
    <a class="menu-item" role="menuitem" href="#/formulario">${icon("book", 18)}<span>Formulario imprimible</span></a>
    <a class="menu-item" role="menuitem" href="#/errores">${icon("alert", 18)}<span>Banco de errores</span></a>
    <a class="menu-item" role="menuitem" href="#/cuaderno">${icon("pen", 18)}<span>Cuaderno de estudio</span></a>
    <a class="menu-item" role="menuitem" href="#/creator">${icon("layers", 18)}<span>Editor de materias</span></a>
    <a class="menu-item" role="menuitem" href="#/ajustes">${icon("settings", 18)}<span>Ajustes</span></a>
    <button class="menu-item" role="menuitem" type="button" id="menu-theme">${icon(dark ? "sun" : "moon", 18)}<span>${dark ? "Tema claro" : "Tema oscuro"}</span></button>
    <button class="menu-item" role="menuitem" type="button" id="menu-search">${icon("search", 18)}<span>Buscar</span><span class="menu-hint">Ctrl K</span></button>
  `;
  pop.querySelector("#menu-theme").addEventListener("click", () => {
    applyTheme(dark ? "light" : "dark");
    closeMenu();
  });
  pop.querySelector("#menu-search").addEventListener("click", () => {
    closeMenu();
    openCommandPalette();
  });
  pop.querySelectorAll("a").forEach((a) => a.addEventListener("click", closeMenu));
}

function closeMenu() {
  const pop = document.getElementById("menu-pop");
  if (pop) pop.hidden = true;
  document.getElementById("menu-trigger")?.setAttribute("aria-expanded", "false");
}

function toggleMenu() {
  const pop = document.getElementById("menu-pop");
  if (!pop) return;
  if (pop.hidden) {
    renderMenu();
    pop.hidden = false;
    document.getElementById("menu-trigger")?.setAttribute("aria-expanded", "true");
  } else {
    closeMenu();
  }
}

function parseRoute() {
  const raw = (location.hash || "#/").slice(1);
  const [pathPart, queryPart] = raw.split("?");
  const path = pathPart || "/";
  const params = new URLSearchParams(queryPart || "");
  return { path, params };
}

function highlightActiveNav() {
  const { path } = parseRoute();
  let key = "hoy";
  if (path.startsWith("/review")) key = "review";
  else if (
    path.startsWith("/ingreso") ||
    path.startsWith("/formulario") ||
    path.startsWith("/errores") ||
    path.startsWith("/cuaderno") ||
    path.startsWith("/diagnostico")
  )
    key = "ingreso";
  else if (path.startsWith("/ejercicios")) key = "ejercicios";
  else if (path.startsWith("/lab")) key = "labs";
  else if (path.startsWith("/aprender") || path.startsWith("/roadmap/") || path.startsWith("/learn/")) key = "aprender";
  else if (path !== "/" && path !== "") key = "";

  document.querySelectorAll("[data-nav]").forEach((el) => {
    const on = el.getAttribute("data-nav") === key;
    el.classList.toggle("active", on);
    if (on) el.setAttribute("aria-current", "page");
    else el.removeAttribute("aria-current");
  });
}

let lastRoutePath = null;

/** When a card/lesson sent the learner to a lab, offer a one-tap way back. */
function paintReturnBar(path) {
  document.getElementById("return-bar")?.remove();
  let back = null;
  try {
    back = sessionStorage.getItem("aprendelab_return");
    if (back && !path.startsWith("/lab")) {
      sessionStorage.removeItem("aprendelab_return");
      back = null;
    }
  } catch {
    back = null;
  }
  if (!back) return;
  const label = back.startsWith("#/learn") ? "Volver a la lección" : back.startsWith("#/session") ? "Volver a la sesión" : "Volver al repaso";
  const bar = document.createElement("div");
  bar.id = "return-bar";
  bar.className = "toast";
  bar.style.cssText = "position:fixed;left:50%;transform:translateX(-50%);bottom:calc(92px + env(safe-area-inset-bottom));z-index:45;";
  bar.innerHTML = `<span>Cuando termines de practicar:</span><a href="${esc(back)}" class="btn btn-inverse btn-sm">${esc(label)}</a>`;
  document.body.appendChild(bar);
}

async function renderRoute() {
  runCleanups();
  const container = document.getElementById("app-view");
  const { path, params } = parseRoute();
  highlightActiveNav();
  closeMenu();
  // Entrance motion only when the page actually changes (not on same-view query updates)
  const isNewPage = path !== lastRoutePath;
  lastRoutePath = path;
  container.classList.remove("route-enter");
  container.innerHTML = `<div class="loading-box">Cargando…</div>`;

  try {
    if (path === "/" || path === "") {
      await renderDashboard(container);
    } else if (path.startsWith("/aprender")) {
      await renderLearnIndex(container);
    } else if (path.startsWith("/ingreso")) {
      await renderIngreso(container, {
        subject: params.get("materia") || null,
        unit: params.get("unidad") || null,
      });
    } else if (path.startsWith("/formulario")) {
      const domainSlug = decodeURIComponent(path.split("/")[2] || "") || "matematicas";
      await renderCheatsheet(container, domainSlug, { ingresoOnly: params.get("all") !== "1" });
    } else if (path.startsWith("/errores")) {
      await renderErrorBank(container, { domain: params.get("domain") || null });
    } else if (path.startsWith("/cuaderno")) {
      await renderNotebook(container, {
        domain: params.get("domain") || null,
        bookmarked: params.get("bookmarked") === "1",
      });
    } else if (path.startsWith("/diagnostico")) {
      const domainSlug = decodeURIComponent(path.split("/")[2] || "") || "matematicas";
      await renderDiagnostic(container, domainSlug);
    } else if (path.startsWith("/ejercicios")) {
      const [, , domainSlug, topicSlug] = path.split("/").map((seg) => decodeURIComponent(seg || ""));
      if (!domainSlug) await renderExercisesIndex(container);
      else if (domainSlug === "reintentos") await renderExerciseRetries(container, { domain: params.get("domain") || null });
      else if (!topicSlug) await renderExerciseDomain(container, domainSlug);
      else if (topicSlug === "simulacro") await renderExerciseExam(container, domainSlug, { ingreso: params.get("ingreso") === "1" });
      else await renderExerciseTopic(container, domainSlug, topicSlug, { exerciseId: params.get("e") || null });
    } else if (path.startsWith("/labs")) {
      await renderLabsIndex(container);
    } else if (path.startsWith("/ajustes")) {
      await renderSettings(container);
    } else if (path.startsWith("/roadmap/")) {
      const slug = decodeURIComponent(path.split("/")[2] || "");
      await renderRoadmap(container, slug);
    } else if (path.startsWith("/learn/")) {
      const nodeId = Number(path.split("/")[2] || 0);
      await renderLearn(container, nodeId);
    } else if (path.startsWith("/review")) {
      await renderReview(container, {
        domain: params.get("domain") || null,
        node: params.get("node") ? Number(params.get("node")) : null,
        mode: params.get("mode") || null,
      });
    } else if (path.startsWith("/session")) {
      await renderSession(container, {
        minutes: Number(params.get("minutes")) || null,
        domains: params.get("domains") ? params.get("domains").split(",") : null,
      });
    } else if (path.startsWith("/lab/guitar")) {
      await renderGuitarLab(container, { tab: params.get("tab") || "metronome" });
    } else if (path.startsWith("/lab/electronics")) {
      await renderElectronicsLab(container, { tab: params.get("tab") || "ohm", practice: params.get("practice"), example: params.get("ex") });
    } else if (path.startsWith("/lab/math")) {
      await renderMathLab(container, { topic: params.get("topic") || "integers" });
    } else if (path.startsWith("/lab/physics")) {
      await renderPhysicsLab(container, { tab: params.get("tab") || "kinematics" });
    } else if (path.startsWith("/creator")) {
      await renderCreator(container);
    } else {
      await renderDashboard(container);
    }
    paintReturnBar(path);
    if (isNewPage) {
      window.scrollTo({ top: 0, behavior: "instant" });
      container.classList.add("route-enter");
      setTimeout(() => container.classList.remove("route-enter"), 700);
    }
  } catch (err) {
    container.innerHTML = `
      <div class="card callout-warn stack">
        <h2>No se pudo cargar esta página</h2>
        <p>${esc(err.message)}</p>
        <div><a href="#/" class="btn btn-primary">Volver a Hoy</a></div>
      </div>`;
  }
}

/* ---------- Command Palette (Ctrl+K / Cmd+K) ---------- */
let cmdEntries = [];
let cmdOpen = false;
let cmdSelected = 0;

async function buildCommandEntries() {
  const base = [
    { label: "Ingreso a Ingeniería (UNCuyo 2027)", meta: "Programa oficial", ico: "target", hash: "#/ingreso" },
    { label: "Formulario de Matemática (imprimible)", meta: "Resumen", ico: "math", hash: "#/formulario/matematicas" },
    { label: "Formulario de Física (imprimible)", meta: "Resumen", ico: "physics", hash: "#/formulario/fisica" },
    { label: "Formulario de Comprensión Lectora", meta: "Resumen", ico: "book", hash: "#/formulario/comprension-problemas" },
    { label: "Banco de errores y puntos débiles", meta: "Práctica", ico: "alert", hash: "#/errores" },
    { label: "Cuaderno de estudio y temas marcados", meta: "Apuntes", ico: "pen", hash: "#/cuaderno" },
    { label: "Diagnóstico de nivel: Matemática", meta: "Evaluación", ico: "math", hash: "#/diagnostico/matematicas" },
    { label: "Diagnóstico de nivel: Física", meta: "Evaluación", ico: "physics", hash: "#/diagnostico/fisica" },
    { label: "Diagnóstico de nivel: Comprensión Lectora", meta: "Evaluación", ico: "book", hash: "#/diagnostico/comprension-problemas" },
    { label: "Repasar lo de hoy", meta: "Repaso", ico: "brain", hash: "#/review" },
    { label: "Empezar una sesión guiada", meta: "Sesión", ico: "zap", hash: "#/session" },
    { label: "Guitarra: metrónomo y escalera de tempo", meta: "Laboratorio", ico: "guitar", hash: "#/lab/guitar?tab=metronome" },
    { label: "Guitarra: afinador con micrófono", meta: "Laboratorio", ico: "mic", hash: "#/lab/guitar?tab=tuner" },
    { label: "Guitarra: diapasón y escala pentatónica", meta: "Laboratorio", ico: "grid", hash: "#/lab/guitar?tab=fretboard" },
    { label: "Guitarra: cambios de acordes en 1 minuto", meta: "Laboratorio", ico: "target", hash: "#/lab/guitar?tab=chords" },
    { label: "Electrónica: ley de Ohm y divisor de tensión", meta: "Laboratorio", ico: "electronics", hash: "#/lab/electronics?tab=ohm" },
    { label: "Electrónica: simulador de circuitos (osciloscopio y multímetro)", meta: "Laboratorio", ico: "activity", hash: "#/lab/electronics?tab=sim" },
    { label: "Electrónica: Arduino virtual (código + circuito)", meta: "Laboratorio", ico: "code", hash: "#/lab/electronics?tab=arduino" },
    { label: "Electrónica: pines del ESP32 y Arduino", meta: "Laboratorio", ico: "electronics", hash: "#/lab/electronics?tab=pinout" },
    { label: "Electrónica: encontrar el error", meta: "Laboratorio", ico: "bug", hash: "#/lab/electronics?tab=debug" },
    { label: "Matemáticas: ejemplos resueltos y práctica", meta: "Laboratorio", ico: "math", hash: "#/lab/math" },
    { label: "Física: simuladores", meta: "Laboratorio", ico: "physics", hash: "#/lab/physics" },
    { label: "Editor de materias", meta: "Crear y respaldar", ico: "layers", hash: "#/creator" },
    { label: "Ajustes", meta: "Tema, ritmo diario", ico: "settings", hash: "#/ajustes" },
  ];
  try {
    const idx = await api.get("/api/search-index");
    for (const d of idx.domains || []) {
      base.push({
        label: d.name,
        meta: "Materia",
        ico: resolveDomainIcon(d.icon, d.lab_type),
        hash: `#/roadmap/${d.slug}`,
      });
    }
    for (const n of idx.nodes || []) {
      base.push({
        label: n.title,
        meta: `Lección · ${n.domain_name}`,
        ico: resolveDomainIcon(n.domain_icon, n.lab_type),
        hash: `#/learn/${n.id}`,
      });
    }
  } catch {
    // fallback to base entries
  }
  cmdEntries = base;
}

function closeCommandPalette() {
  cmdOpen = false;
  const modal = document.getElementById("cmd-modal");
  if (modal) modal.hidden = true;
}

async function openCommandPalette() {
  await buildCommandEntries();
  cmdOpen = true;
  cmdSelected = 0;
  const modal = document.getElementById("cmd-modal");
  if (!modal) return;
  modal.hidden = false;

  let remoteResults = [];
  let searchTimer = null;
  let searchSeq = 0;

  const renderList = (query = "") => {
    const q = query.trim().toLowerCase();
    const localFiltered = q
      ? cmdEntries.filter(
          (e) => e.label.toLowerCase().includes(q) || e.meta.toLowerCase().includes(q)
        )
      : cmdEntries.slice(0, 14);
    const seen = new Set(localFiltered.map((x) => `${x.hash}|${x.label}`));
    const merged = q.length >= 2
      ? [
          ...localFiltered.slice(0, 6),
          ...remoteResults.filter((r) => !seen.has(`${r.hash}|${r.label}`)),
        ].slice(0, 18)
      : localFiltered;

    cmdSelected = Math.min(cmdSelected, Math.max(0, merged.length - 1));
    const listEl = modal.querySelector(".cmd-list");
    if (!merged.length) {
      listEl.innerHTML = `<div class="muted center" style="padding:24px;">Sin resultados para «${esc(query)}»</div>`;
      return merged;
    }
    listEl.innerHTML = merged
      .map(
        (item, i) => `
      <button type="button" class="cmd-item ${i === cmdSelected ? "selected" : ""}" data-idx="${i}">
        <span class="row" style="gap:10px;min-width:0;text-align:left;">
          ${icon(resolveDomainIcon(item.ico, item.ico), 15)}
          <span style="min-width:0;">
            <span style="display:block;">${esc(item.label)}</span>
            ${item.snippet ? `<span class="xs muted truncate" style="display:block;max-width:440px;">${esc(item.snippet)}</span>` : ""}
          </span>
        </span>
        <span class="xs muted" style="flex-shrink:0;">${esc(item.meta)}</span>
      </button>`
      )
      .join("");
    listEl.querySelectorAll(".cmd-item").forEach((btn) => {
      btn.addEventListener("click", () => {
        const picked = merged[Number(btn.dataset.idx)];
        closeCommandPalette();
        if (picked) location.hash = picked.hash;
      });
    });
    return merged;
  };

  modal.innerHTML = `
    <div class="cmd-dialog" role="dialog" aria-modal="true" aria-label="Paleta de comandos">
      <div class="cmd-input-row">
        ${icon("search", 16)}
        <input type="text" class="cmd-input" placeholder="Buscar fórmulas, ejercicios, tarjetas, apuntes o acciones…" aria-label="Buscar" autocomplete="off" />
        <kbd class="kbd">ESC</kbd>
      </div>
      <div class="cmd-list"></div>
      <div class="cmd-footer">
        <span>↑ ↓ para moverte · Enter para abrir</span>
        <span>Busca en lecciones, ejercicios, tarjetas y cuaderno</span>
      </div>
    </div>
  `;

  let currentFiltered = renderList("");
  const input = modal.querySelector(".cmd-input");
  input.focus();

  modal.addEventListener("click", (e) => {
    if (e.target === modal) closeCommandPalette();
  });

  input.addEventListener("input", () => {
    cmdSelected = 0;
    const q = input.value.trim();
    if (q.length < 2) {
      remoteResults = [];
      currentFiltered = renderList(q);
      return;
    }
    currentFiltered = renderList(q);
    clearTimeout(searchTimer);
    const seq = ++searchSeq;
    searchTimer = setTimeout(async () => {
      try {
        const res = await api.get(`/api/search?q=${encodeURIComponent(q)}&limit=18`);
        if (seq !== searchSeq || !cmdOpen) return;
        remoteResults = res.results || [];
        currentFiltered = renderList(input.value);
      } catch {
        // non-fatal
      }
    }, 150);
  });

  input.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      closeCommandPalette();
    } else if (e.key === "ArrowDown") {
      e.preventDefault();
      if (currentFiltered.length) {
        cmdSelected = (cmdSelected + 1) % currentFiltered.length;
        renderList(input.value);
      }
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      if (currentFiltered.length) {
        cmdSelected = (cmdSelected - 1 + currentFiltered.length) % currentFiltered.length;
        renderList(input.value);
      }
    } else if (e.key === "Enter" && currentFiltered[cmdSelected]) {
      e.preventDefault();
      const picked = currentFiltered[cmdSelected];
      closeCommandPalette();
      location.hash = picked.hash;
    }
  });
}

async function initTheme() {
  let saved = null;
  try {
    saved = localStorage.getItem("aprendelab_theme");
  } catch {
    // ignore
  }
  if (!saved) {
    // First visit on this device: adopt the choice stored on the server, if the learner made one
    try {
      const { settings } = await api.get("/api/settings");
      if (settings?.theme === "dark") applyTheme("dark");
    } catch {
      // keep system preference
    }
  }
  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", (e) => {
    let choice = "system";
    try {
      choice = localStorage.getItem("aprendelab_theme") || "system";
    } catch {
      // ignore
    }
    if (choice === "system") document.documentElement.setAttribute("data-theme", e.matches ? "dark" : "light");
  });
}

if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("/sw.js").catch(() => {});
}

window.addEventListener("keydown", (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
    e.preventDefault();
    if (cmdOpen) closeCommandPalette();
    else openCommandPalette();
  } else if (e.key === "Escape") {
    if (cmdOpen) closeCommandPalette();
    closeMenu();
  }
});
document.addEventListener("click", (e) => {
  const pop = document.getElementById("menu-pop");
  if (pop && !pop.hidden && !pop.contains(e.target) && !e.target.closest("#menu-trigger")) closeMenu();
});

window.addEventListener("hashchange", renderRoute);
window.addEventListener("DOMContentLoaded", async () => {
  const cmdTrigger = document.getElementById("cmd-trigger");
  if (cmdTrigger) {
    cmdTrigger.innerHTML = icon("search", 18);
    cmdTrigger.addEventListener("click", openCommandPalette);
  }
  const menuTrigger = document.getElementById("menu-trigger");
  if (menuTrigger) {
    menuTrigger.innerHTML = icon("more", 18);
    menuTrigger.addEventListener("click", (e) => {
      e.stopPropagation();
      toggleMenu();
    });
  }
  renderMobileNav();
  await initTheme();
  await refreshSidebarDomains();
  await renderRoute();
});
