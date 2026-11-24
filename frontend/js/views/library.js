import { icon, resolveDomainIcon } from "../icons.js";
import { ART, subjectArt } from "../art.js";
import { api, esc, toneOf, LAB_ROUTES } from "../main.js";

export { ART };

export const LABS = [
  {
    key: "guitar",
    title: "Guitarra",
    what: "Metrónomo, afinador con micrófono, acordes y diapasón.",
    tools: ["Metrónomo", "Afinador", "Acordes", "Diapasón", "Oído"],
  },
  {
    key: "electronics",
    title: "Electrónica",
    what: "Ley de Ohm, pines del ESP32, encontrar errores y proyectos.",
    tools: ["Ley de Ohm", "Pines", "Depuración", "Proyectos"],
  },
  {
    key: "math",
    title: "Matemáticas",
    what: "Ejemplos resueltos, práctica mezclada y graficador.",
    tools: ["Ejemplos", "Práctica", "Graficador"],
  },
  {
    key: "physics",
    title: "Física",
    what: "Simuladores de proyectiles, fuerzas, ondas, energía, fluidos y óptica.",
    tools: ["Proyectiles", "Fuerzas", "Ondas", "Energía", "Fluidos", "Óptica"],
  },
];

export async function renderLearnIndex(container) {
  const dash = await api.get("/api/dashboard");
  const { domains, next_steps = {} } = dash;

  container.innerHTML = `
    <div class="page-header">
      <div>
        <h1>Aprender</h1>
        <p class="muted">Cada materia es una ruta de lecciones cortas. Completás una, la practicás, y se desbloquea la siguiente.</p>
      </div>
      <div class="row">
        <a href="#/ajustes" class="btn btn-secondary">${icon("sliders", 16)} Estilos e imágenes</a>
        <a href="#/creator" class="btn btn-secondary">${icon("plus", 16)} Nueva materia</a>
      </div>
    </div>

    <div class="grid-2">
      ${domains
        .map((d) => {
          const tone = toneOf(d.lab_type);
          const next = next_steps[d.slug];
          const allDone = d.node_count > 0 && d.lessons_completed >= d.node_count;
          const lessonsPct = d.node_count ? Math.round((d.lessons_completed / d.node_count) * 100) : 0;
          return `
          <a href="#/roadmap/${esc(d.slug)}" class="tile" data-tone="${tone}">
            <div class="tile-art">${subjectArt(d.slug || tone)}</div>
            <div class="stack-sm">
              <h2 class="tile-title">${esc(d.name)}</h2>
              <p class="m-0 muted">${
                allDone
                  ? "Todas las lecciones completadas. Ahora, a consolidar con repasos."
                  : next
                  ? `${next.lesson_completed ? "Seguí practicando" : "Próxima lección"}: ${esc(next.node_title.replace(/^\d+\.\s*/, ""))}`
                  : esc(d.description)
              }</p>
            </div>
            <div class="stack-sm">
              <div class="progress-track"><div class="progress-fill" style="width:${lessonsPct}%;"></div></div>
              <div class="tile-foot">
                <span class="small">${d.lessons_completed} de ${d.node_count} lecciones${d.due_count ? ` · ${d.due_count} para repasar` : ""}</span>
                ${icon("arrowRight", 20)}
              </div>
            </div>
          </a>`;
        })
        .join("")}
    </div>
  `;
}

export async function renderLabsIndex(container) {
  container.innerHTML = `
    <div class="page-header">
      <div>
        <h1>Laboratorios</h1>
        <p class="muted">Herramientas para practicar con las manos: tocar, medir, simular y equivocarte sin costo.</p>
      </div>
    </div>

    <div class="grid-2">
      ${LABS.map(
        (lab) => `
        <a href="${LAB_ROUTES[lab.key]}" class="tile dots" data-tone="${lab.key}">
          <div class="tile-art">${subjectArt(lab.key)}</div>
          <div class="stack-sm">
            <h2 class="tile-title">${lab.title}</h2>
            <p class="m-0 muted">${lab.what}</p>
          </div>
          <div class="tile-foot">
            <span class="small">${lab.tools.join(" · ")}</span>
            ${icon("arrowRight", 20)}
          </div>
        </a>`
      ).join("")}
    </div>
  `;
}

export { resolveDomainIcon };
