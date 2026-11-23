import { icon, resolveDomainIcon } from "../icons.js";
import { api, esc, toneOf, LAB_ROUTES } from "../main.js";

/**
 * Line-art per discipline, drawn in currentColor so it inherits the tile's tone.
 * This is the app's visual identity (together with the halftone .dots motif).
 */
export const ART = {
  guitar: `
    <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round">
      <g stroke-width="1.2" opacity="0.55">
        <line x1="8" y1="24" x2="312" y2="24"/><line x1="8" y1="40" x2="312" y2="40"/>
        <line x1="8" y1="56" x2="312" y2="56"/><line x1="8" y1="72" x2="312" y2="72"/>
        <line x1="8" y1="88" x2="312" y2="88"/><line x1="8" y1="104" x2="312" y2="104"/>
      </g>
      <g stroke-width="2.4" opacity="0.5">
        <line x1="70" y1="20" x2="70" y2="108"/><line x1="140" y1="20" x2="140" y2="108"/>
        <line x1="210" y1="20" x2="210" y2="108"/><line x1="280" y1="20" x2="280" y2="108"/>
      </g>
      <path d="M8 56 Q 40 28, 72 56 T 136 56 T 200 56 T 264 56 T 312 56" stroke-width="2.6"/>
      <g fill="currentColor" stroke="none">
        <circle cx="105" cy="40" r="9"/><circle cx="175" cy="72" r="9"/><circle cx="245" cy="88" r="9"/>
      </g>
    </svg>`,
  electronics: `
    <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
      <path d="M10 40 H86 L104 22 H130 M10 82 H70 L88 100 H130 M190 30 H236 L254 14 H310 M190 60 H310 M190 90 H232 L250 106 H310" stroke-width="2"/>
      <rect x="130" y="10" width="60" height="100" rx="8" stroke-width="2.4"/>
      <rect x="146" y="38" width="28" height="28" rx="4" fill="currentColor" stroke="none" opacity="0.3"/>
      <g fill="currentColor" stroke="none">
        <circle cx="10" cy="40" r="5"/><circle cx="10" cy="82" r="5"/>
        <circle cx="310" cy="14" r="5"/><circle cx="310" cy="60" r="5"/><circle cx="310" cy="106" r="5"/>
      </g>
      <path d="M40 82 l6 -10 l8 20 l8 -20 l8 20 l6 -10" stroke-width="2"/>
    </svg>`,
  math: `
    <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round">
      <g stroke-width="1" opacity="0.4">
        <path d="M40 10V110M100 10V110M160 10V110M220 10V110M280 10V110M10 30H310M10 60H310M10 90H310"/>
      </g>
      <line x1="10" y1="90" x2="310" y2="90" stroke-width="1.8"/>
      <line x1="100" y1="6" x2="100" y2="114" stroke-width="1.8"/>
      <line x1="20" y1="104" x2="300" y2="16" stroke-width="2.8"/>
      <path d="M30 20 Q 160 150, 290 24" stroke-width="2.2" stroke-dasharray="6 5"/>
      <circle cx="207" cy="45" r="8" fill="currentColor" stroke="none"/>
      <circle cx="207" cy="45" r="16" stroke-width="1.6" opacity="0.5"/>
    </svg>`,
  physics: `
    <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round">
      <line x1="10" y1="104" x2="310" y2="104" stroke-width="1.8"/>
      <path d="M24 104 Q 150 -44, 276 104" stroke-width="2.4" stroke-dasharray="7 5"/>
      <circle cx="112" cy="44" r="10" fill="currentColor" stroke="none"/>
      <path d="M112 44 H170 M160 36 l10 8 l-10 8" stroke-width="2.4"/>
      <path d="M112 44 V12 M104 22 l8 -10 l8 10" stroke-width="2.4"/>
      <g stroke-width="1.6" opacity="0.7">
        <ellipse cx="262" cy="42" rx="30" ry="11" transform="rotate(-28 262 42)"/>
        <ellipse cx="262" cy="42" rx="30" ry="11" transform="rotate(28 262 42)"/>
      </g>
      <circle cx="262" cy="42" r="4.5" fill="currentColor" stroke="none"/>
    </svg>`,
  generic: `
    <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
      <path d="M60 30 H150 a12 12 0 0 1 12 12 V104 a10 10 0 0 0 -10 -10 H60 Z" stroke-width="2.4"/>
      <path d="M264 30 H174 a12 12 0 0 0 -12 12 V104 a10 10 0 0 1 10 -10 H264 Z" stroke-width="2.4"/>
      <path d="M82 50H140M82 66H132M186 50H244M194 66H244" stroke-width="1.8" opacity="0.6"/>
    </svg>`,
};

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
      <a href="#/creator" class="btn btn-secondary">${icon("plus", 16)} Nueva materia</a>
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
            <div class="tile-art">${ART[tone] || ART.generic}</div>
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
          <div class="tile-art">${ART[lab.key]}</div>
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
