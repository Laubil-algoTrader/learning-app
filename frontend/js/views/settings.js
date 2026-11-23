import { icon } from "../icons.js";
import { api, applyTheme, toast } from "../main.js";

export async function renderSettings(container) {
  const { settings } = await api.get("/api/settings");
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

  container.innerHTML = `
    <div class="focus-column">
      <div class="page-header">
        <div>
          <h1>Ajustes</h1>
          <p class="muted">Tu ritmo de estudio y la apariencia de la app.</p>
        </div>
      </div>

      <div class="stack">
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

        <section class="card row-between">
          <div>
            <h3>Tus datos</h3>
            <p class="muted small m-0">Todo se guarda en esta computadora. Podés exportar un respaldo desde el editor.</p>
          </div>
          <a href="#/creator" class="btn btn-secondary">${icon("download", 16)} Ir al editor</a>
        </section>
      </div>
    </div>
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
}
