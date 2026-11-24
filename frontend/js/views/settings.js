import { icon } from "../icons.js";
import { ART_GALLERY, SUBJECT_ORDER, getSelectedVariant, setSelectedVariant } from "../art.js";
import { api, applyTheme, esc, toast } from "../main.js";

function renderArtGallery() {
  return SUBJECT_ORDER.map((key) => {
    const subject = ART_GALLERY[key];
    const activeId = getSelectedVariant(key);
    return `
      <div class="card stack art-subject-block" data-tone="${esc(subject.tone)}">
        <div class="row-between">
          <div>
            <h3 class="title-sm m-0">${esc(subject.label)}</h3>
            <p class="xs muted m-0">Elegí la ilustración de tarjeta y el logo que más te gusten.</p>
          </div>
          <span class="pill pill-tone">4 opciones</span>
        </div>
        <div class="art-opt-grid" role="radiogroup" aria-label="Estilo visual de ${esc(subject.label)}">
          ${subject.options
            .map((opt, idx) => {
              const selected = opt.id === activeId;
              return `
              <button
                type="button"
                role="radio"
                aria-checked="${selected ? "true" : "false"}"
                class="art-opt-card ${selected ? "active" : ""}"
                data-art-subject="${esc(key)}"
                data-art-variant="${esc(opt.id)}"
              >
                <div class="art-opt-preview">
                  <div class="art-opt-banner">${opt.art}</div>
                  <span class="art-opt-logo" title="Logo en Ingreso y Hoy">
                    <svg class="ico" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${opt.logo}</svg>
                  </span>
                </div>
                <div class="art-opt-foot">
                  <div class="row-between gap-sm">
                    <strong class="art-opt-name">${idx + 1}. ${esc(opt.name)}</strong>
                    ${selected ? `<span class="art-opt-check" aria-label="Seleccionada">${icon("check", 13)}</span>` : ""}
                  </div>
                  <span class="xs muted art-opt-desc">${esc(opt.desc)}</span>
                </div>
              </button>`;
            })
            .join("")}
        </div>
      </div>`;
  }).join("");
}

function buildDailyReminderIcs(hour = 19, minute = 0) {
  const pad = (n) => String(n).padStart(2, "0");
  const now = new Date();
  const stamp = `${now.getUTCFullYear()}${pad(now.getUTCMonth() + 1)}${pad(now.getUTCDate())}T${pad(now.getUTCHours())}${pad(now.getUTCMinutes())}00Z`;
  const start = `${now.getFullYear()}${pad(now.getMonth() + 1)}${pad(now.getDate())}T${pad(hour)}${pad(minute)}00`;
  const endHour = (hour + 1) % 24;
  const end = `${now.getFullYear()}${pad(now.getMonth() + 1)}${pad(now.getDate())}T${pad(endHour)}${pad(minute)}00`;
  return [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//AprendeLab//Estudio Diario//ES",
    "BEGIN:VEVENT",
    `UID:aprendelab-daily-${Date.now()}@localhost`,
    `DTSTAMP:${stamp}`,
    `DTSTART:${start}`,
    `DTEND:${end}`,
    "RRULE:FREQ=DAILY",
    "SUMMARY:Sesión diaria de Ingreso · AprendeLab",
    "DESCRIPTION:Repaso FSRS + lección o ejercicios del día en http://localhost:8000/#/ingreso",
    "BEGIN:VALARM",
    "TRIGGER:-PT10M",
    "ACTION:DISPLAY",
    "DESCRIPTION:Hora de estudiar en AprendeLab",
    "END:VALARM",
    "END:VEVENT",
    "END:VCALENDAR",
  ].join("\r\n");
}

export async function renderSettings(container) {
  const [{ settings }, suspendedRes, reportsRes, autoBackupsRes] = await Promise.all([
    api.get("/api/settings"),
    api.get("/api/items/suspended").catch(() => ({ items: [] })),
    api.get("/api/reports").catch(() => ({ reports: [] })),
    api.get("/api/backup/auto").catch(() => ({ backups: [] })),
  ]);
  const suspendedItems = suspendedRes.items || [];
  const reports = reportsRes.reports || [];
  const autoBackups = autoBackupsRes.backups || [];
  let themeChoice = "system";
  try {
    themeChoice = localStorage.getItem("aprendelab_theme") || "system";
  } catch {
    // ignore
  }

  const seg = (name, options, current) => `
    <div class="segmented" role="group" data-setting="${name}">
      ${options
        .map(
          ([value, label]) =>
            `<button type="button" class="seg-btn ${String(current) === String(value) ? "active" : ""}" data-value="${value}">${label}</button>`
        )
        .join("")}
    </div>`;

  const examDates = settings.exam_dates || {};
  const ingresoFocus = Boolean(settings.ingreso_focus_mode);

  container.innerHTML = `
    <div class="focus-column">
      <div class="page-header">
        <div>
          <h1>Ajustes</h1>
          <p class="muted">Tu ritmo de estudio, fechas de examen, respaldos y apariencia de la app.</p>
        </div>
      </div>

      <div class="stack">
        <section class="card stack">
          <div>
            <h3>Meta diaria de estudio</h3>
            <p class="muted small m-0">Define cuántas lecciones y ejercicios querés completar por día. Se refleja en el panel de Ingreso.</p>
          </div>
          <div class="grid-2" style="gap:16px;">
            <div class="stack-sm">
              <span class="small"><strong>Lecciones por día</strong></span>
              ${seg("daily_lesson_goal", [[1, "1"], [2, "2"], [3, "3"], [4, "4"]], settings.daily_lesson_goal || 2)}
            </div>
            <div class="stack-sm">
              <span class="small"><strong>Ejercicios por día</strong></span>
              ${seg("daily_exercise_goal", [[3, "3"], [5, "5"], [8, "8"], [12, "12"]], settings.daily_exercise_goal || 5)}
            </div>
          </div>
          <div class="row-between" style="padding-top:8px;border-top:1px solid var(--border);">
            <div>
              <strong class="small">Modo «Solo Ingreso» en Hoy</strong>
              <p class="xs muted m-0">Filtra el inicio y la sesión guiada a Matemática, Física y Comprensión Lectora.</p>
            </div>
            <button type="button" id="toggle-ingreso-focus" class="btn btn-sm ${ingresoFocus ? "btn-primary" : "btn-secondary"}" aria-pressed="${ingresoFocus}">
              ${ingresoFocus ? "Activado" : "Desactivado"}
            </button>
          </div>
        </section>

        <section class="card stack">
          <div>
            <h3>Fechas de examen (Ingreso UNCuyo)</h3>
            <p class="muted small m-0">Con estas fechas calculamos los días restantes y el ritmo diario sugerido, reservando 2 semanas previas para simulacros.</p>
          </div>
          <form id="exam-dates-form" class="stack">
            <div class="grid-3" style="gap:12px;">
              <label class="field">
                <span>Matemática</span>
                <input type="date" name="matematica" value="${esc(examDates.matematica || "")}" />
              </label>
              <label class="field">
                <span>Física</span>
                <input type="date" name="fisica" value="${esc(examDates.fisica || "")}" />
              </label>
              <label class="field">
                <span>Comprensión Lectora</span>
                <input type="date" name="clyrp" value="${esc(examDates.clyrp || "")}" />
              </label>
            </div>
            <div class="row">
              <button type="submit" class="btn btn-primary btn-sm">${icon("check", 14)} Guardar fechas</button>
              <button type="button" id="clear-exam-dates" class="btn btn-secondary btn-sm">Limpiar</button>
            </div>
          </form>
        </section>

        <section class="card stack">
          <div>
            <h3>Tarjetas nuevas por día</h3>
            <p class="muted small m-0">Cuántas tarjetas que nunca viste entran a tu repaso cada día. Menos es más sostenible: cada tarjeta nueva genera repasos futuros.</p>
          </div>
          ${seg("new_per_day", [[4, "4"], [8, "8"], [12, "12"], [20, "20"]], settings.new_per_day)}
        </section>

        <section class="card stack">
          <div>
            <h3>Cuánto querés recordar</h3>
            <p class="muted small m-0">
              La app agenda cada repaso para cuando la probabilidad de acordarte baja a este valor.
              Más alto = repasos más seguidos. <strong id="ret-val">${Math.round(settings.desired_retention * 100)}%</strong>
            </p>
          </div>
          <input id="ret-slider" type="range" min="0.80" max="0.96" step="0.01" value="${settings.desired_retention}" aria-label="Retención objetivo" />
          <div class="row-between xs muted"><span>80% · menos repasos</span><span>96% · más repasos</span></div>
        </section>

        <section class="card stack">
          <div>
            <h3>Duración de la sesión guiada</h3>
            <p class="muted small m-0">Valor por defecto al empezar una sesión.</p>
          </div>
          ${seg("default_session_minutes", [[15, "15 min"], [25, "25 min"], [45, "45 min"]], settings.default_session_minutes)}
        </section>

        <section class="card stack">
          <h3>Apariencia</h3>
          ${seg("theme", [["system", "Según el sistema"], ["light", "Claro"], ["dark", "Oscuro"]], themeChoice)}
        </section>

        <section class="card stack">
          <div>
            <h3>Respaldo completo y restauración</h3>
            <p class="muted small m-0">El JSON incluye lecciones, FSRS, historial de repasos, métricas, intentos, simulacros y cuaderno. También podés descargar y restaurar el archivo <code>.db</code> completo desde acá. Además, la app crea copias automáticas diarias en <code>data/backups/</code>.</p>
          </div>
          <div class="row">
            <button type="button" id="backup-json-btn" class="btn btn-primary btn-sm">${icon("download", 15)} Descargar JSON</button>
            <a href="/api/backup/db" download class="btn btn-secondary btn-sm">${icon("download", 15)} Descargar SQLite (.db)</a>
            <label class="btn btn-secondary btn-sm" style="cursor:pointer;">
              ${icon("upload", 15)} Restaurar JSON
              <input type="file" id="restore-json-input" accept="application/json,.json" hidden />
            </label>
            <label class="btn btn-secondary btn-sm" style="cursor:pointer;">
              ${icon("upload", 15)} Restaurar SQLite (.db)
              <input type="file" id="restore-db-input" accept=".db,.sqlite,.sqlite3,application/x-sqlite3" hidden />
            </label>
            <a href="#/creator" class="btn btn-text btn-sm">Editor</a>
          </div>
          ${
            autoBackups.length
              ? `<p class="xs muted m-0">Última copia automática: <strong>${esc(autoBackups[0].name)}</strong> (${autoBackups[0].size_kb} KB · ${autoBackups.length} ${autoBackups.length === 1 ? "respaldo guardado" : "respaldos guardados"} en <code>data/backups/</code>).</p>`
              : ""
          }
        </section>

        <section class="card stack">
          <div>
            <h3>Recordatorio diario en tu calendario</h3>
            <p class="muted small m-0">Descargá un evento diario <code>.ics</code> para importarlo en Google Calendar, Apple Calendar o el celular y no cortar la racha.</p>
          </div>
          <div class="row">
            <label class="row gap-sm small">
              <span>Horario:</span>
              <input type="time" id="ics-time" value="19:00" style="width:auto;" />
            </label>
            <button type="button" id="download-ics-btn" class="btn btn-secondary btn-sm">${icon("clock", 14)} Descargar recordatorio (.ics)</button>
          </div>
        </section>

        ${
          suspendedItems.length
            ? `<section class="card stack">
                <div class="row-between">
                  <h3 class="m-0">Tarjetas suspendidas (${suspendedItems.length})</h3>
                </div>
                <div class="list">
                  ${suspendedItems
                    .map(
                      (it) => `
                    <div class="list-row" style="padding:10px 0;">
                      <div class="grow">
                        <div class="small"><strong>${esc(it.title)}</strong></div>
                        <div class="xs muted">${esc(it.domain_name)} · ${esc(it.node_title)}</div>
                      </div>
                      <button type="button" class="btn btn-secondary btn-sm unsuspend-btn" data-id="${it.id}">Reactivar</button>
                    </div>`
                    )
                    .join("")}
                </div>
              </section>`
            : ""
        }

        ${
          reports.length
            ? `<section class="card stack">
                <div class="row-between">
                  <h3 class="m-0">Errores de contenido reportados (${reports.length})</h3>
                </div>
                <div class="list">
                  ${reports
                    .map(
                      (r) => `
                    <div class="list-row" style="padding:10px 0;">
                      <div class="grow">
                        <div class="small"><strong>${esc(r.title || r.target_id)}</strong> <span class="pill xs">${esc(r.kind)}</span></div>
                        <div class="xs muted">${esc(r.message)} · ${esc((r.created_at || "").slice(0, 10))}</div>
                      </div>
                      <button type="button" class="btn btn-ghost btn-sm del-report-btn" data-id="${r.id}">${icon("trash", 13)}</button>
                    </div>`
                    )
                    .join("")}
                </div>
              </section>`
            : ""
        }
      </div>
    </div>

    <section class="section section-tight art-gallery-section" id="estilos-materias">
      <div class="section-head">
        <div>
          <h2>Imágenes y logos de materias</h2>
          <p class="section-sub">Elegí entre 4 diseños para cada materia. Se aplican al instante en Ingreso, Aprender, Ejercicios, Laboratorios y Hoy.</p>
        </div>
      </div>
      <div id="art-gallery-host" class="stack-lg">${renderArtGallery()}</div>
    </section>
  `;

  container.querySelectorAll("[data-setting]").forEach((group) => {
    group.addEventListener("click", async (e) => {
      const btn = e.target.closest(".seg-btn");
      if (!btn) return;
      group.querySelectorAll(".seg-btn").forEach((b) => b.classList.toggle("active", b === btn));
      const key = group.dataset.setting;
      const value = btn.dataset.value;
      if (key === "theme") {
        applyTheme(value);
        return;
      }
      try {
        await api.put("/api/settings", { [key]: Number(value) });
        toast("Guardado", "ok");
      } catch (err) {
        toast(err.message, "err");
      }
    });
  });

  const slider = container.querySelector("#ret-slider");
  const label = container.querySelector("#ret-val");
  slider.addEventListener("input", () => {
    label.textContent = `${Math.round(Number(slider.value) * 100)}%`;
  });
  slider.addEventListener("change", async () => {
    try {
      await api.put("/api/settings", { desired_retention: Number(slider.value) });
      toast("Guardado", "ok");
    } catch (err) {
      toast(err.message, "err");
    }
  });

  const galleryHost = container.querySelector("#art-gallery-host");
  galleryHost.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-art-subject]");
    if (!btn) return;
    const subjectKey = btn.dataset.artSubject;
    const variantId = btn.dataset.artVariant;
    setSelectedVariant(subjectKey, variantId);
    galleryHost.innerHTML = renderArtGallery();
    const subjectName = ART_GALLERY[subjectKey]?.label || "la materia";
    toast(`Estilo de ${subjectName} actualizado`, "ok");
  });

  // Modo "Solo Ingreso" toggle
  const focusBtn = container.querySelector("#toggle-ingreso-focus");
  focusBtn?.addEventListener("click", async () => {
    const next = focusBtn.getAttribute("aria-pressed") !== "true";
    try {
      await api.put("/api/settings", { ingreso_focus_mode: next });
      focusBtn.setAttribute("aria-pressed", String(next));
      focusBtn.textContent = next ? "Activado" : "Desactivado";
      focusBtn.classList.toggle("btn-primary", next);
      focusBtn.classList.toggle("btn-secondary", !next);
      toast(next ? "Modo Solo Ingreso activado" : "Modo Solo Ingreso desactivado", "ok");
    } catch (err) {
      toast(err.message, "err");
    }
  });

  // Exam dates form
  const datesForm = container.querySelector("#exam-dates-form");
  datesForm?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const fd = new FormData(datesForm);
    const dates = {
      matematica: String(fd.get("matematica") || "").trim(),
      fisica: String(fd.get("fisica") || "").trim(),
      clyrp: String(fd.get("clyrp") || "").trim(),
    };
    try {
      await api.put("/api/settings", { exam_dates: dates });
      toast("Fechas de examen guardadas", "ok");
    } catch (err) {
      toast(err.message, "err");
    }
  });
  container.querySelector("#clear-exam-dates")?.addEventListener("click", async () => {
    if (!datesForm) return;
    datesForm.querySelectorAll('input[type="date"]').forEach((inp) => {
      inp.value = "";
    });
    try {
      await api.put("/api/settings", { exam_dates: {} });
      toast("Fechas limpiadas", "ok");
    } catch (err) {
      toast(err.message, "err");
    }
  });

  // Complete backup download (JSON v2)
  container.querySelector("#backup-json-btn")?.addEventListener("click", async () => {
    try {
      const bundle = await api.get("/api/export");
      const blob = new Blob([JSON.stringify(bundle, null, 2)], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `aprendelab-backup-${new Date().toISOString().slice(0, 10)}.json`;
      a.click();
      URL.revokeObjectURL(url);
      toast("Respaldo completo descargado", "ok");
    } catch (err) {
      toast(err.message, "err");
    }
  });

  // Restore complete backup from JSON
  container.querySelector("#restore-json-input")?.addEventListener("change", async (e) => {
    const file = e.target.files?.[0];
    if (!file) return;
    try {
      const text = await file.text();
      const bundle = JSON.parse(text);
      if (!window.confirm("¿Restaurar el respaldo seleccionado? Se combinará con tu progreso actual y actualizará notas, intentos y simulacros.")) {
        e.target.value = "";
        return;
      }
      const { restored } = await api.post("/api/backup/restore", bundle);
      toast(
        `Restaurado: ${restored.restored_nodes || 0} lecciones, ${restored.restored_reviews || 0} repasos, ${restored.restored_metrics || 0} métricas, ${restored.restored_attempts || 0} intentos, ${restored.restored_exams || 0} simulacros y ${restored.restored_notes || 0} notas.`,
        "ok"
      );
      renderSettings(container);
    } catch (err) {
      toast(`No se pudo restaurar: ${err.message}`, "err");
      e.target.value = "";
    }
  });

  // Restore raw SQLite .db file directly
  container.querySelector("#restore-db-input")?.addEventListener("change", async (e) => {
    const file = e.target.files?.[0];
    if (!file) return;
    if (!window.confirm("¿Reemplazar tu base actual por este archivo .db? Antes de reemplazar se guardará una copia de seguridad automática en data/backups/.")) {
      e.target.value = "";
      return;
    }
    try {
      const buf = await file.arrayBuffer();
      const res = await fetch("/api/backup/restore-db", {
        method: "POST",
        headers: { "Content-Type": "application/x-sqlite3" },
        body: buf,
      });
      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.error || `Error HTTP ${res.status}`);
      toast(`Base SQLite restaurada (${data.restored?.reviews || 0} repasos, ${data.restored?.nodes || 0} temas).`, "ok");
      renderSettings(container);
    } catch (err) {
      toast(`No se pudo restaurar el .db: ${err.message}`, "err");
      e.target.value = "";
    }
  });

  // Download daily reminder .ics
  container.querySelector("#download-ics-btn")?.addEventListener("click", () => {
    const val = container.querySelector("#ics-time")?.value || "19:00";
    const [hh, mm] = val.split(":").map((x) => Number(x) || 0);
    const ics = buildDailyReminderIcs(hh, mm);
    const blob = new Blob([ics], { type: "text/calendar;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "aprendelab-estudio-diario.ics";
    a.click();
    URL.revokeObjectURL(url);
    toast("Recordatorio .ics descargado", "ok");
  });

  // Unsuspend cards & dismiss content reports
  container.querySelectorAll(".unsuspend-btn").forEach((btn) =>
    btn.addEventListener("click", async () => {
      try {
        await api.put(`/api/items/${btn.dataset.id}`, { suspended: false });
        toast("Tarjeta reactivada", "ok");
        renderSettings(container);
      } catch (err) {
        toast(err.message, "err");
      }
    })
  );
  container.querySelectorAll(".del-report-btn").forEach((btn) =>
    btn.addEventListener("click", async () => {
      try {
        await api.del(`/api/reports/${btn.dataset.id}`);
        toast("Reporte cerrado", "ok");
        renderSettings(container);
      } catch (err) {
        toast(err.message, "err");
      }
    })
  );
}
