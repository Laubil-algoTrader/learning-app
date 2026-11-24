import { DOMAIN_ICON_CHOICES, icon, resolveDomainIcon } from "../icons.js";
import { api, esc, refreshSidebarDomains, toast } from "../main.js";

const STARTER_PACKS = {
  ingles: {
    name: "Inglés Práctico",
    icon: "globe",
    color: "#3d664e",
    domain_type: "conceptual",
    description: "Inmersión comprensible, active recall en contexto y producción oral/escrita con FSRS-5.",
    nodes: [
      {
        title: "1. Phrasal Verbs de alta frecuencia",
        summary: "Dominar verbos compuestos esenciales en conversación y documentación técnica.",
        items: [
          { title: "figure out", prompt: "¿Qué significa 'figure out' y cómo lo usarías en una frase sobre tecnología?", answer: "Descubrir, deducir o resolver cómo funciona algo. Ej: 'I finally figured out why the ESP32 kept rebooting.'" },
          { title: "look up vs look into", prompt: "¿Cuál es la diferencia entre 'look up' y 'look into'?", answer: "'Look up' = buscar un dato concreto (diccionario, datasheet). 'Look into' = investigar un problema a fondo." },
        ],
      },
      {
        title: "2. Conectores y fluidez oral",
        summary: "Unir ideas con naturalidad sin traducir palabra por palabra.",
        items: [
          { title: "Even though vs Despite", prompt: "¿Cómo cambia la estructura de la frase al usar 'even though' frente a 'despite'?", answer: "'Even though' va seguido de sujeto + verbo ('Even though it was late...'). 'Despite' va seguido de sustantivo o verbo-ing ('Despite being late...')." },
        ],
      },
    ],
  },
  python: {
    name: "Programación (Python)",
    icon: "code",
    color: "#235e63",
    domain_type: "project",
    description: "Práctica basada en pequeños proyectos, lectura activa de código, debugging y estructuras de datos.",
    nodes: [
      {
        title: "1. Variables, tipos y control de flujo",
        summary: "Listas, diccionarios, condicionales y bucles limpios.",
        items: [
          { title: "Lista vs Diccionario (complejidad)", prompt: "¿Cuándo conviene usar un dict/set en lugar de una list para buscar elementos?", answer: "Cuando necesitás búsquedas rápidas por clave o pertenencia: dict y set buscan en O(1) promedio frente a O(n) en listas." },
        ],
      },
      {
        title: "2. Funciones y debugging sistemático",
        summary: "Dividir problemas en funciones puras y leer tracebacks sin pánico.",
        items: [
          { title: "Mutabilidad en argumentos por defecto", prompt: "¿Por qué es un bug clásico escribir def agregar(x, lista=[]) en Python?", answer: "Porque el valor por defecto [] se evalúa una sola vez al definir la función y se comparte entre llamadas. Se usa lista=None y dentro if lista is None: lista = []." },
        ],
      },
    ],
  },
  dibujo: {
    name: "Dibujo y Observación",
    icon: "pen",
    color: "#9c5a2c",
    domain_type: "motor",
    description: "Control de trazo, construcción en formas 3D (cajas, cilindros, esferas), perspectiva y luz/sombra.",
    nodes: [
      {
        title: "1. Control de línea desde el hombro",
        summary: "Trazos seguros de una sola pasada evitando 'líneas peludas'.",
        items: [
          { title: "Drill: Líneas fantasma (Ghosting)", prompt: "¿En qué consiste la técnica de 'ghosting' antes de trazar una línea recta?", answer: "Marcar punto A y B, practicar el movimiento 3 veces en el aire desde el hombro sin apoyar el lápiz y bajar en una sola pasada decidida." },
        ],
      },
      {
        title: "2. Formas básicas y perspectiva",
        summary: "Construir objetos complejos a partir de cajas y cilindros en el espacio.",
        items: [
          { title: "Línea del horizonte y punto de fuga", prompt: "¿Qué representa exactamente la línea del horizonte en un dibujo de perspectiva?", answer: "La altura exacta de los ojos del observador. Todo lo que está por encima se ve desde abajo y todo lo que está por debajo se ve desde arriba." },
        ],
      },
    ],
  },
};

function checkToText(check) {
  if (!check) return "";
  if (check.type === "numeric") return String(check.value);
  if (check.type === "text") return (check.accept || []).join(" | ");
  if (check.type === "choice") {
    const opts = check.options || [];
    return [opts[check.correct], ...opts.filter((_, i) => i !== check.correct)].join(" | ");
  }
  return "";
}

function textToCheck(type, raw) {
  const parts = raw.split("|").map((x) => x.trim()).filter(Boolean);
  if (!type) return null;
  if (type === "numeric") {
    const value = Number(raw.trim().replace(",", "."));
    if (!raw.trim() || Number.isNaN(value)) throw new Error("Para corrección numérica, escribí solo el número esperado.");
    return { type, value, tolerance: Number.isInteger(value) ? 0 : 0.02 };
  }
  if (type === "text") {
    if (!parts.length) throw new Error("Escribí al menos una respuesta aceptada.");
    return { type, accept: parts };
  }
  if (type === "choice") {
    if (parts.length < 2) throw new Error("Opción múltiple necesita la correcta y al menos una incorrecta, separadas por |.");
    return { type, options: parts, correct: 0 };
  }
  return null;
}

export async function renderCreator(container) {
  const { domains } = await api.get("/api/domains");
  let selectedSlug = domains[0]?.slug || "";
  let roadmap = selectedSlug ? await api.get(`/api/domains/${encodeURIComponent(selectedSlug)}/roadmap`) : null;
  let domExData = selectedSlug ? await api.get(`/api/exercises/${encodeURIComponent(selectedSlug)}`).catch(() => ({ topics: [] })) : { topics: [] };
  let editingItem = null;
  let editingNode = null;
  let editingNodeLesson = null;

  const reloadDomain = async () => {
    if (!selectedSlug) return;
    [roadmap, domExData] = await Promise.all([
      api.get(`/api/domains/${encodeURIComponent(selectedSlug)}/roadmap`),
      api.get(`/api/exercises/${encodeURIComponent(selectedSlug)}`).catch(() => ({ topics: [] })),
    ]);
  };

  const installStarterPack = async (packKey) => {
    const pack = STARTER_PACKS[packKey];
    if (!pack) return;
    try {
      const createdDom = await api.post("/api/domains", {
        name: pack.name,
        icon: pack.icon,
        color: pack.color,
        domain_type: pack.domain_type,
        description: pack.description,
        create_starter_node: false,
      });
      let prevSlug = null;
      for (let i = 0; i < pack.nodes.length; i++) {
        const n = pack.nodes[i];
        const createdNode = await api.post("/api/nodes", {
          domain_id: createdDom.domain.id,
          title: n.title,
          level: i + 1,
          summary: n.summary,
          prerequisites: prevSlug ? [prevSlug] : [],
        });
        prevSlug = createdNode.node.slug;
        for (const it of n.items) {
          await api.post("/api/items", {
            node_id: createdNode.node.id,
            item_type: "recall",
            title: it.title,
            prompt: it.prompt,
            answer: it.answer,
          });
        }
      }
      toast(`Plantilla «${pack.name}» instalada`, "ok");
      await refreshSidebarDomains();
      renderCreator(container);
    } catch (err) {
      toast(err.message, "err");
    }
  };

  const paint = () => {
    const nodes = roadmap?.nodes || [];
    const allNodeItems = nodes.flatMap((n) => (n.items || []).map((it) => ({ ...it, node_title: n.title })));
    const customExercises = (domExData?.topics || []).flatMap((t) =>
      (t.exercises || []).filter((e) => e.custom).map((e) => ({ ...e, topic_title: t.title }))
    );

    const les = editingNodeLesson || {};
    const lesHook = typeof les.hook === "string" ? les.hook : les.hook?.intuition || "";
    const lesPoints = (les.concept?.points || []).join("\n");
    const lesRule = les.concept?.key_rule || "";
    const lesPitfall = les.concept?.pitfall || "";
    const lesExTitle = les.example?.title || "";
    const lesExSteps = (les.example?.steps || []).join("\n");

    container.innerHTML = `
      <div class="page-header">
        <div>
          <h1>Editor de materias</h1>
          <p class="muted">Creá o editá materias, temas, lecciones completas, ejercicios propios y tarjetas FSRS.</p>
        </div>
        <div class="row">
          <button id="export-btn" class="btn btn-secondary btn-sm" type="button">${icon("download", 14)} Exportar respaldo</button>
          <label class="btn btn-secondary btn-sm" style="cursor:pointer;">
            ${icon("upload", 14)} Restaurar JSON
            <input id="import-file" type="file" accept=".json,application/json" style="display:none;" />
          </label>
        </div>
      </div>

      <!-- ONE-CLICK PEDAGOGICAL STARTER PACKS -->
      <div class="card card-wash stack" style="margin-bottom:20px;">
        <div class="row-between">
          <div><h3 style="margin:0;">Empezar con una plantilla</h3></div>
          <span class="xs mono muted">Incluyen ruta con prerrequisitos e ítems FSRS</span>
        </div>
        <div class="grid-3">
          ${Object.entries(STARTER_PACKS)
            .map(
              ([k, p]) => `
            <div class="card-flat row-between" style="background:var(--bg-card);">
              <div class="row" style="gap:10px;">
                <div class="domain-icon-box" style="width:34px;height:34px;">${icon(p.icon, 16)}</div>
                <div>
                  <div class="small" style="font-weight:600;">${esc(p.name)}</div>
                  <div class="xs muted">${p.nodes.length} nodos base</div>
                </div>
              </div>
              <button type="button" class="btn btn-secondary btn-sm pack-btn" data-pack="${k}">${icon("plus", 13)} Instalar</button>
            </div>`
            )
            .join("")}
        </div>
      </div>

      <div class="card stack mb-lg">
        <label class="field">
          <span>Materia en edición</span>
          <select id="studio-domain-select">
            ${domains
              .map(
                (d) =>
                  `<option value="${esc(d.slug)}" ${d.slug === selectedSlug ? "selected" : ""}>${esc(d.name)} (${d.node_count} temas · ${d.item_count} tarjetas)</option>`
              )
              .join("")}
          </select>
        </label>
      </div>

      <div class="grid-2" style="align-items:start;">
        <!-- LEFT: Node & Lesson Editor + Custom Exercise Creator -->
        <div class="stack">
          <form id="node-editor-form" class="card stack">
            <div class="row-between">
              <h2 class="title-sm m-0">${editingNode ? "Editar tema y lección" : "Agregar tema / lección"}</h2>
              ${editingNode ? `<button id="cancel-node-edit" type="button" class="btn btn-ghost btn-sm">Cancelar</button>` : ""}
            </div>
            <label class="field">
              <span>Título del tema</span>
              <input type="text" name="title" value="${esc(editingNode?.title || "")}" placeholder="Ej: 9. Ecuaciones trigonométricas" required />
            </label>
            <div class="grid-2" style="gap:10px;">
              <label class="field">
                <span>Nivel</span>
                <input type="number" name="level" value="${editingNode?.level || 1}" min="1" max="20" />
              </label>
              <label class="field">
                <span>Prerrequisito</span>
                <select name="prereq">
                  <option value="">Ninguno</option>
                  ${nodes
                    .filter((n) => !editingNode || n.id !== editingNode.id)
                    .map(
                      (n) =>
                        `<option value="${esc(n.slug)}" ${(editingNode?.prerequisites || []).includes(n.slug) ? "selected" : ""}>${esc(n.title)}</option>`
                    )
                    .join("")}
                </select>
              </label>
            </div>
            <label class="field">
              <span>Resumen</span>
              <input type="text" name="summary" value="${esc(editingNode?.summary || "")}" placeholder="Qué habilidad concreta enseña este tema" />
            </label>
            <details ${editingNode ? "open" : ""}>
              <summary class="link small" style="cursor:pointer;">Contenido de la lección (idea, puntos, fórmula clave, ejemplo)</summary>
              <div class="stack-sm mt-sm">
                <label class="field">
                  <span>Idea / intuición inicial</span>
                  <textarea name="lesson_hook" rows="2" placeholder="¿Por qué sirve este tema?">${esc(lesHook)}</textarea>
                </label>
                <label class="field">
                  <span>Puntos clave (uno por línea)</span>
                  <textarea name="lesson_points" rows="3" placeholder="Paso o propiedad 1&#10;Paso o propiedad 2">${esc(lesPoints)}</textarea>
                </label>
                <label class="field">
                  <span>Regla o fórmula clave (aparece en el Formulario)</span>
                  <input type="text" name="lesson_rule" value="${esc(lesRule)}" placeholder="Ej: \`v = v_0 + a·t\`" />
                </label>
                <label class="field">
                  <span>Error típico</span>
                  <input type="text" name="lesson_pitfall" value="${esc(lesPitfall)}" placeholder="Qué trampa evitar en el examen" />
                </label>
                <label class="field">
                  <span>Título del ejemplo</span>
                  <input type="text" name="lesson_ex_title" value="${esc(lesExTitle)}" placeholder="Ej: Calcular el tiempo de frenado" />
                </label>
                <label class="field">
                  <span>Pasos del ejemplo (uno por línea)</span>
                  <textarea name="lesson_ex_steps" rows="2" placeholder="Paso 1...&#10;Paso 2...">${esc(lesExSteps)}</textarea>
                </label>
              </div>
            </details>
            <button class="btn btn-primary btn-sm" type="submit">${editingNode ? "Guardar tema y lección" : `${icon("plus", 14)} Crear tema`}</button>
          </form>

          <form id="custom-ex-form" class="card stack">
            <h2 class="title-sm m-0">Crear ejercicio propio</h2>
            <p class="xs muted m-0">Se suma al tema elegido, entra en los simulacros y aparece en el banco de errores si lo fallás.</p>
            <div class="grid-2" style="gap:10px;">
              <label class="field">
                <span>Tema</span>
                <select name="node_id" required>
                  ${nodes.map((n) => `<option value="${n.id}">${esc(n.title)}</option>`).join("")}
                </select>
              </label>
              <label class="field">
                <span>Nivel</span>
                <select name="level">
                  <option value="1">1 · Básico</option>
                  <option value="2">2 · Intermedio</option>
                  <option value="3">3 · Tipo examen</option>
                </select>
              </label>
            </div>
            <label class="field">
              <span>Título del ejercicio</span>
              <input type="text" name="title" placeholder="Ej: Parcial 2025 · Bloque con rozamiento" required />
            </label>
            <label class="field">
              <span>Enunciado</span>
              <textarea name="statement" rows="3" placeholder="Escribí los datos y el problema completo…" required></textarea>
            </label>
            <label class="field">
              <span>Pregunta / inciso</span>
              <input type="text" name="part_prompt" placeholder="Ej: Calculá la aceleración en m/s²." required />
            </label>
            <div class="grid-2" style="gap:10px;">
              <label class="field">
                <span>Tipo de corrección</span>
                <select name="check_type">
                  <option value="numeric">Numérica</option>
                  <option value="text">Texto corto</option>
                  <option value="choice">Opción múltiple</option>
                </select>
              </label>
              <label class="field">
                <span>Respuesta esperada</span>
                <input type="text" name="check_value" placeholder="2.5 · o: correcta | distractor1 | distractor2" required />
              </label>
            </div>
            <div class="grid-2" style="gap:10px;">
              <label class="field">
                <span>Unidad (opcional)</span>
                <input type="text" name="unit" placeholder="m/s², N, cm…" />
              </label>
              <label class="field">
                <span>Pista (opcional)</span>
                <input type="text" name="hint" placeholder="Planteá primero ∑F = m·a" />
              </label>
            </div>
            <label class="field">
              <span>Resolución paso a paso (una línea por paso)</span>
              <textarea name="solution" rows="2" placeholder="1) Descomponemos el peso...&#10;2) Despejamos a = ..."></textarea>
            </label>
            <button class="btn btn-primary btn-sm" type="submit">${icon("plus", 14)} Guardar ejercicio</button>
          </form>
        </div>

        <!-- RIGHT: Flashcard Editor + Create New Domain -->
        <div class="stack">
          <form id="new-item-form" class="card stack">
            <div class="row-between">
              <h2 class="title-sm m-0">${editingItem ? "Editar tarjeta FSRS" : "Agregar una tarjeta FSRS"}</h2>
              ${editingItem ? `<button id="cancel-edit" type="button" class="btn btn-ghost btn-sm">Cancelar edición</button>` : ""}
            </div>
            ${
              !editingItem
                ? `<div class="grid-2" style="gap:10px;">
                    <label class="field">
                      <span>Tema destino</span>
                      <select name="node_id" required>
                        ${nodes.map((n) => `<option value="${n.id}">${esc(n.title)}</option>`).join("")}
                      </select>
                    </label>
                    <label class="field">
                      <span>Tipo de ítem</span>
                      <select name="item_type">
                        <option value="recall">Pregunta</option>
                        <option value="drill">Ejercicio práctico</option>
                        <option value="worked_example">Problema</option>
                        <option value="debug">Encontrar el error</option>
                        <option value="project_step">Paso de proyecto</option>
                      </select>
                    </label>
                  </div>`
                : ""
            }
            <label class="field">
              <span>Título corto</span>
              <input type="text" name="title" value="${esc(editingItem?.title || "")}" placeholder="Ej: Regla de oro para..." required />
            </label>
            <label class="field">
              <span>Pregunta o consigna</span>
              <textarea name="prompt" placeholder="¿Qué tenés que recordar, ejecutar o resolver?" required>${esc(editingItem?.prompt || "")}</textarea>
            </label>
            <label class="field">
              <span>Respuesta (o explicación, si se corrige sola)</span>
              <textarea name="answer" placeholder="Respuesta clara o criterio objetivo de éxito." required>${esc(editingItem?.answer || "")}</textarea>
            </label>
            <label class="field">
              <span>Pista opcional</span>
              <input type="text" name="hint" value="${esc(editingItem?.hints?.[0] || "")}" placeholder="Ayuda mínima sin revelar la respuesta" />
            </label>
            <div class="grid-2" style="gap:12px;">
              <label class="field">
                <span>Corrección</span>
                <select name="check_type">
                  ${[
                    ["", "Me califico yo"],
                    ["numeric", "Automática: número"],
                    ["text", "Automática: texto corto"],
                    ["choice", "Automática: opción múltiple"],
                  ]
                    .map(([v, l]) => `<option value="${v}" ${(editingItem?.payload?.check?.type || "") === v ? "selected" : ""}>${l}</option>`)
                    .join("")}
                </select>
              </label>
              <label class="field">
                <span>Respuesta esperada</span>
                <input type="text" name="check_value" value="${esc(checkToText(editingItem?.payload?.check))}" placeholder="220 · o: correcta | otra | otra" />
              </label>
            </div>
            <button class="btn btn-primary btn-sm" type="submit">${editingItem ? "Guardar cambios" : "Guardar tarjeta"}</button>
          </form>

          <form id="new-domain-form" class="card stack">
            <h2 class="title-sm m-0">Crear una materia nueva</h2>
            <label class="field">
              <span>Nombre de la disciplina</span>
              <input type="text" name="name" placeholder="Ej: Química, Álgebra lineal, Piano…" required />
            </label>
            <div class="grid-2" style="gap:12px;">
              <label class="field">
                <span>Ícono vectorial</span>
                <select name="icon">
                  ${DOMAIN_ICON_CHOICES.map((c) => `<option value="${c.key}">${esc(c.label)}</option>`).join("")}
                </select>
              </label>
              <label class="field">
                <span>Tipo de aprendizaje</span>
                <select name="domain_type">
                  <option value="mixed">Mixto (teoría + práctica)</option>
                  <option value="motor">Habilidad motora</option>
                  <option value="project">Proyectos / técnico</option>
                  <option value="conceptual">Conceptual / problemas</option>
                </select>
              </label>
            </div>
            <label class="field">
              <span>Descripción breve</span>
              <textarea name="description" rows="2" placeholder="¿Qué querés dominar y con qué enfoque práctico?"></textarea>
            </label>
            <button class="btn btn-secondary btn-sm" type="submit">${icon("plus", 15)} Crear materia</button>
          </form>
        </div>
      </div>

      <!-- TOPICS LIST (EDIT / DELETE NODES & LESSONS) -->
      <div class="card stack" style="margin-top:20px;">
        <h3 class="m-0">Temas y lecciones de ${esc(roadmap?.domain?.name || "")} (${nodes.length})</h3>
        <div class="stack" style="gap:7px;max-height:320px;overflow-y:auto;">
          ${nodes
            .map(
              (n) => `
            <div class="card-flat row-between">
              <div style="min-width:0;">
                <div class="small" style="font-weight:600;">${esc(n.title)}</div>
                <div class="xs muted truncate">${esc(n.summary || "Sin resumen")} · Nivel ${n.level} · ${(n.items || []).length} tarjetas</div>
              </div>
              <div class="row">
                <a href="#/learn/${n.id}" class="btn btn-ghost btn-sm">Ver</a>
                <button type="button" class="btn btn-secondary btn-sm edit-node-btn" data-id="${n.id}">Editar</button>
                <button type="button" class="btn btn-danger btn-sm del-node-btn" data-id="${n.id}" data-title="${esc(n.title)}">${icon("trash", 13)}</button>
              </div>
            </div>`
            )
            .join("")}
        </div>
      </div>

      ${
        customExercises.length
          ? `<div class="card stack" style="margin-top:20px;">
              <h3 class="m-0">Tus ejercicios propios en ${esc(roadmap?.domain?.name || "")} (${customExercises.length})</h3>
              <div class="stack" style="gap:7px;">
                ${customExercises
                  .map(
                    (ex) => `
                  <div class="card-flat row-between">
                    <div style="min-width:0;">
                      <div class="small" style="font-weight:600;">${esc(ex.title)}</div>
                      <div class="xs muted">${esc(ex.topic_title)} · Nivel ${ex.level}</div>
                    </div>
                    <div class="row">
                      <a href="#/ejercicios/${esc(selectedSlug)}/${esc(ex.node)}?e=${esc(ex.id)}" class="btn btn-ghost btn-sm">Abrir</a>
                      <button type="button" class="btn btn-danger btn-sm del-custom-ex-btn" data-id="${esc(ex.id)}">${icon("trash", 13)}</button>
                    </div>
                  </div>`
                  )
                  .join("")}
              </div>
            </div>`
          : ""
      }

      <!-- CARDS LIST -->
      <div class="card stack" style="margin-top:20px;">
        <h3 class="m-0">Tarjetas FSRS de ${esc(roadmap?.domain?.name || "")} (${allNodeItems.length})</h3>
        <div class="stack" style="gap:7px;max-height:320px;overflow-y:auto;">
          ${allNodeItems
            .map(
              (it) => `
            <div class="card-flat row-between">
              <div style="min-width:0;">
                <div class="small" style="font-weight:600;">${esc(it.title)} ${it.suspended ? `<span class="pill pill-amber xs">Suspendida</span>` : ""}</div>
                <div class="xs mono muted">${esc(it.node_title)} · ${esc(it.item_type)} · S: ${it.stability}d</div>
              </div>
              <div class="row">
                ${
                  it.suspended
                    ? `<button type="button" class="btn btn-secondary btn-sm unsuspend-item-btn" data-id="${it.id}">Reactivar</button>`
                    : ""
                }
                <button type="button" class="btn btn-ghost btn-sm edit-item-btn" data-id="${it.id}">Editar</button>
                <button type="button" class="btn btn-danger btn-sm del-item-btn" data-id="${it.id}">${icon("trash", 13)}</button>
              </div>
            </div>`
            )
            .join("")}
        </div>
      </div>

      <!-- DOMAINS LIST -->
      <div class="card" style="margin-top:20px;">
        <h3 style="margin-bottom:12px;">Tus materias (${domains.length})</h3>
        <div class="stack" style="gap:8px;">
          ${domains
            .map((d) => {
              const ico = resolveDomainIcon(d.icon, d.lab_type);
              return `
              <div class="card-flat row-between">
                <div class="row">
                  <div class="domain-icon-box" style="width:32px;height:32px;">${icon(ico, 16)}</div>
                  <div>
                    <strong>${esc(d.name)}</strong>
                    <div class="xs mono muted">${d.node_count} nodos · ${d.item_count} ítems</div>
                  </div>
                </div>
                <div class="row">
                  <a href="#/roadmap/${esc(d.slug)}" class="btn btn-ghost btn-sm">Ver ruta</a>
                  ${
                    d.lab_type === "generic"
                      ? `<button class="btn btn-danger btn-sm del-domain" data-id="${d.id}" data-name="${esc(d.name)}" type="button">${icon("trash", 13)} Eliminar</button>`
                      : `<span class="pill">Base</span>`
                  }
                </div>
              </div>`;
            })
            .join("")}
        </div>
      </div>
    `;

    container.querySelectorAll(".pack-btn").forEach((btn) => {
      btn.addEventListener("click", () => installStarterPack(btn.dataset.pack));
    });

    container.querySelector("#studio-domain-select")?.addEventListener("change", async (e) => {
      selectedSlug = e.target.value;
      editingItem = null;
      editingNode = null;
      editingNodeLesson = null;
      await reloadDomain();
      paint();
    });

    container.querySelector("#cancel-edit")?.addEventListener("click", () => {
      editingItem = null;
      paint();
    });
    container.querySelector("#cancel-node-edit")?.addEventListener("click", () => {
      editingNode = null;
      editingNodeLesson = null;
      paint();
    });

    container.querySelectorAll(".edit-node-btn").forEach((btn) => {
      btn.addEventListener("click", async () => {
        const nid = Number(btn.dataset.id);
        editingNode = nodes.find((x) => x.id === nid) || null;
        try {
          const lesData = await api.get(`/api/nodes/${nid}/lesson`);
          editingNodeLesson = lesData.lesson || null;
        } catch {
          editingNodeLesson = null;
        }
        paint();
        container.querySelector("#node-editor-form")?.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });

    container.querySelectorAll(".del-node-btn").forEach((btn) => {
      btn.addEventListener("click", async () => {
        if (!window.confirm(`¿Eliminar el tema «${btn.dataset.title}» junto con sus tarjetas y ejercicios propios?`)) return;
        try {
          await api.del(`/api/nodes/${btn.dataset.id}`);
          if (editingNode?.id === Number(btn.dataset.id)) {
            editingNode = null;
            editingNodeLesson = null;
          }
          toast("Tema eliminado", "ok");
          await reloadDomain();
          await refreshSidebarDomains();
          paint();
        } catch (err) {
          toast(err.message, "err");
        }
      });
    });

    container.querySelectorAll(".del-custom-ex-btn").forEach((btn) => {
      btn.addEventListener("click", async () => {
        if (!window.confirm("¿Eliminar este ejercicio propio?")) return;
        try {
          await api.del(`/api/exercises/custom/${encodeURIComponent(btn.dataset.id)}`);
          toast("Ejercicio eliminado", "ok");
          await reloadDomain();
          paint();
        } catch (err) {
          toast(err.message, "err");
        }
      });
    });

    container.querySelectorAll(".unsuspend-item-btn").forEach((btn) => {
      btn.addEventListener("click", async () => {
        await api.put(`/api/items/${btn.dataset.id}`, { suspended: false });
        toast("Tarjeta reactivada", "ok");
        await reloadDomain();
        await refreshSidebarDomains();
        paint();
      });
    });

    container.querySelectorAll(".edit-item-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        editingItem = allNodeItems.find((x) => x.id === Number(btn.dataset.id)) || null;
        paint();
        container.querySelector("#new-item-form")?.scrollIntoView({ behavior: "smooth", block: "center" });
      });
    });

    container.querySelectorAll(".del-item-btn").forEach((btn) => {
      btn.addEventListener("click", async () => {
        if (!confirm("¿Eliminar este ítem de estudio?")) return;
        await api.del(`/api/items/${btn.dataset.id}`);
        toast("Tarjeta eliminada", "ok");
        await reloadDomain();
        await refreshSidebarDomains();
        paint();
      });
    });

    container.querySelector("#new-domain-form")?.addEventListener("submit", async (e) => {
      e.preventDefault();
      const fd = new FormData(e.target);
      try {
        const res = await api.post("/api/domains", {
          name: fd.get("name"),
          icon: fd.get("icon"),
          color: "#235e63",
          domain_type: fd.get("domain_type"),
          description: fd.get("description"),
        });
        toast(`Materia «${res.domain.name}» creada`, "ok");
        await refreshSidebarDomains();
        renderCreator(container);
      } catch (err) {
        toast(err.message, "err");
      }
    });

    container.querySelector("#node-editor-form")?.addEventListener("submit", async (e) => {
      e.preventDefault();
      if (!roadmap?.domain?.id) return;
      const fd = new FormData(e.target);
      const prereq = String(fd.get("prereq") || "").trim();
      const hookTxt = String(fd.get("lesson_hook") || "").trim();
      const pointsArr = String(fd.get("lesson_points") || "")
        .split("\n")
        .map((x) => x.trim())
        .filter(Boolean);
      const keyRule = String(fd.get("lesson_rule") || "").trim();
      const pitfall = String(fd.get("lesson_pitfall") || "").trim();
      const exTitle = String(fd.get("lesson_ex_title") || "").trim();
      const exSteps = String(fd.get("lesson_ex_steps") || "")
        .split("\n")
        .map((x) => x.trim())
        .filter(Boolean);

      const hasLessonFields = Boolean(hookTxt || pointsArr.length || keyRule || pitfall || exTitle || exSteps.length);
      const lessonPayload = hasLessonFields
        ? {
            ...(editingNodeLesson || {}),
            hook: {
              question: (editingNodeLesson?.hook && typeof editingNodeLesson.hook === "object" ? editingNodeLesson.hook.question : "") || `¿Qué resuelve «${fd.get("title")}»?`,
              intuition: hookTxt || String(fd.get("summary") || ""),
            },
            concept: {
              ...(editingNodeLesson?.concept || {}),
              points: pointsArr.length ? pointsArr : editingNodeLesson?.concept?.points || [String(fd.get("summary") || fd.get("title"))],
              key_rule: keyRule || editingNodeLesson?.concept?.key_rule || String(fd.get("title")),
              pitfall: pitfall || editingNodeLesson?.concept?.pitfall || "Verificá signos, unidades y dominio antes de cerrar la cuenta.",
            },
            example: {
              ...(editingNodeLesson?.example || {}),
              title: exTitle || editingNodeLesson?.example?.title || "Ejemplo resuelto",
              steps: exSteps.length ? exSteps : editingNodeLesson?.example?.steps || ["Aplicá la regla paso a paso y comprobá el resultado."],
            },
          }
        : undefined;

      try {
        if (editingNode) {
          await api.put(`/api/nodes/${editingNode.id}`, {
            title: fd.get("title"),
            level: Number(fd.get("level") || 1),
            summary: fd.get("summary"),
            prerequisites: prereq ? [prereq] : [],
            ...(lessonPayload ? { lesson: lessonPayload } : {}),
          });
          toast("Tema y lección actualizados", "ok");
          editingNode = null;
          editingNodeLesson = null;
        } else {
          const created = await api.post("/api/nodes", {
            domain_id: roadmap.domain.id,
            title: fd.get("title"),
            level: Number(fd.get("level") || 1),
            summary: fd.get("summary"),
            prerequisites: prereq ? [prereq] : [],
          });
          if (lessonPayload && created.node?.id) {
            await api.put(`/api/nodes/${created.node.id}`, { lesson: lessonPayload });
          }
          toast("Tema y lección creados", "ok");
        }
        await reloadDomain();
        paint();
      } catch (err) {
        toast(err.message, "err");
      }
    });

    container.querySelector("#custom-ex-form")?.addEventListener("submit", async (e) => {
      e.preventDefault();
      const fd = new FormData(e.target);
      const checkType = String(fd.get("check_type") || "numeric");
      const checkRaw = String(fd.get("check_value") || "");
      const unit = String(fd.get("unit") || "").trim();
      let check;
      try {
        check = textToCheck(checkType, checkRaw);
        if (unit && check) check.unit = unit;
      } catch (err) {
        toast(err.message, "err");
        return;
      }
      const answerDisplay =
        check.type === "choice"
          ? check.options[0]
          : check.type === "numeric"
          ? `${check.value}${unit ? " " + unit : ""}`
          : check.accept[0];
      const hint = String(fd.get("hint") || "").trim();
      const solSteps = String(fd.get("solution") || "")
        .split("\n")
        .map((x) => x.trim())
        .filter(Boolean);
      try {
        await api.post("/api/exercises/custom", {
          node_id: Number(fd.get("node_id")),
          title: fd.get("title"),
          level: Number(fd.get("level") || 1),
          statement: fd.get("statement"),
          parts: [
            {
              prompt: String(fd.get("part_prompt") || "").trim(),
              answer: answerDisplay,
              check,
            },
          ],
          hints: hint ? [hint] : [],
          solution: solSteps.length ? solSteps : [`Respuesta: ${answerDisplay}`],
        });
        toast("Ejercicio propio guardado", "ok");
        await reloadDomain();
        paint();
      } catch (err) {
        toast(err.message, "err");
      }
    });

    container.querySelector("#new-item-form")?.addEventListener("submit", async (e) => {
      e.preventDefault();
      const fd = new FormData(e.target);
      const hint = String(fd.get("hint") || "").trim();
      let check;
      try {
        check = textToCheck(String(fd.get("check_type") || ""), String(fd.get("check_value") || ""));
      } catch (err) {
        toast(err.message, "err");
        return;
      }
      try {
        if (editingItem) {
          await api.put(`/api/items/${editingItem.id}`, {
            title: fd.get("title"),
            prompt: fd.get("prompt"),
            answer: fd.get("answer"),
            hints: hint ? [hint] : [],
            payload: { check },
          });
          toast("Tarjeta actualizada", "ok");
          editingItem = null;
        } else {
          await api.post("/api/items", {
            node_id: Number(fd.get("node_id")),
            item_type: fd.get("item_type"),
            title: fd.get("title"),
            prompt: fd.get("prompt"),
            answer: fd.get("answer"),
            hints: hint ? [hint] : [],
            payload: check ? { check } : {},
          });
          toast("Tarjeta guardada", "ok");
        }
        await reloadDomain();
        await refreshSidebarDomains();
        paint();
      } catch (err) {
        toast(err.message, "err");
      }
    });

    container.querySelectorAll(".del-domain").forEach((btn) => {
      btn.addEventListener("click", async () => {
        if (!confirm(`¿Eliminar la disciplina "${btn.dataset.name}" y todos sus ítems?`)) return;
        await api.del(`/api/domains/${btn.dataset.id}`);
        toast("Materia eliminada", "ok");
        await refreshSidebarDomains();
        renderCreator(container);
      });
    });

    container.querySelector("#export-btn")?.addEventListener("click", async () => {
      const bundle = await api.get("/api/export");
      const blob = new Blob([JSON.stringify(bundle, null, 2)], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `aprendelab-backup-${new Date().toISOString().slice(0, 10)}.json`;
      a.click();
      URL.revokeObjectURL(url);
      toast("Respaldo descargado", "ok");
    });

    container.querySelector("#import-file")?.addEventListener("change", async (e) => {
      const file = e.target.files?.[0];
      if (!file) return;
      try {
        const text = await file.text();
        const json = JSON.parse(text);
        const { restored } = await api.post("/api/backup/restore", json);
        toast(
          `Restaurado: ${restored.restored_nodes || 0} temas, ${restored.restored_reviews || 0} repasos, ${restored.restored_attempts || 0} intentos, ${restored.restored_exams || 0} simulacros.`,
          "ok"
        );
        await refreshSidebarDomains();
        renderCreator(container);
      } catch (err) {
        toast(`Error al restaurar: ${err.message}`, "err");
      }
    });
  };

  paint();
}
