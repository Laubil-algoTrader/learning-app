import { icon } from "../icons.js";
import { api, esc, rich, labLinkToHash, registerCleanup, toast, toneOf } from "../main.js";
import { renderChordSVG } from "../labs/guitar_lab.js";

const STEPS = [
  { key: "hook", name: "La idea" },
  { key: "concept", name: "Cómo funciona" },
  { key: "example", name: "Ejemplo" },
  { key: "check", name: "Comprobación" },
  { key: "takeaway", name: "Cierre" },
];
const CHECK_STEP = 3;

function shuffled(arr) {
  const out = arr.slice();
  for (let i = out.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [out[i], out[j]] = [out[j], out[i]];
  }
  return out;
}

/* Chord diagrams shown inside the lessons that teach them */
const LESSON_CHORDS = {
  "g-acordes-em-am": ["Em", "Am"],
  "g-acordes-d-a-e": ["D", "A", "E"],
  "g-acordes-g-c": ["G", "C"],
};

export async function renderLearn(container, nodeId) {
  const data = await api.get(`/api/nodes/${encodeURIComponent(nodeId)}/lesson`);
  const { node, domain, lesson, prev_node, next_node } = data;
  const tone = toneOf(domain.lab_type);
  const deepLab = labLinkToHash(lesson.example?.lab_link);
  const chords = LESSON_CHORDS[node.slug] || [];
  const title = node.title.replace(/^\d+\.\s*/, "");

  // Options are shuffled once per visit: in the authored content the right answer is
  // almost always written first, and its position must not give it away.
  const checks = [lesson.check, ...(lesson.checks || [])]
    .filter((c) => c && c.options?.length)
    .map((c) => ({ ...c, options: shuffled(c.options), picked: null, solved: false, missed: false }));

  // A hook is either {question, intuition} or a single opening statement.
  const hook = typeof lesson.hook === "string" ? { question: "", intuition: lesson.hook } : lesson.hook || {};

  let stepIdx = 0;
  let checkIdx = 0;
  let takeawayText = "";
  let completedNow = Boolean(node.lesson_completed);
  let createdCards = 0;

  const checksPassed = () => completedNow || checks.every((c) => c.solved);
  const canGoTo = (idx) => idx <= CHECK_STEP || checksPassed();

  const goTo = (idx) => {
    const area = container.querySelector("#lesson-feynman");
    if (area) takeawayText = area.value;
    if (!canGoTo(idx)) {
      toast("Respondé bien las preguntas para cerrar la lección.", "info");
      return;
    }
    stepIdx = Math.max(0, Math.min(STEPS.length - 1, idx));
    paint();
    container.querySelector(".focus-column")?.scrollIntoView({ block: "start", behavior: "instant" });
  };

  const onKeyDown = (e) => {
    const tag = (document.activeElement?.tagName || "").toLowerCase();
    if (tag === "textarea" || tag === "input" || tag === "select") return;
    const cmd = document.getElementById("cmd-modal");
    if (cmd && !cmd.hidden) return;
    if (e.key === "ArrowRight" && stepIdx < STEPS.length - 1) {
      e.preventDefault();
      goTo(stepIdx + 1);
    } else if (e.key === "ArrowLeft" && stepIdx > 0) {
      e.preventDefault();
      goTo(stepIdx - 1);
    }
  };
  window.addEventListener("keydown", onKeyDown);
  registerCleanup(() => window.removeEventListener("keydown", onKeyDown));

  const stepHtml = () => {
    const step = STEPS[stepIdx];

    if (step.key === "hook") {
      return `
        <div class="stack-lg">
          ${
            hook.question
              ? `<h2>${esc(hook.question)}</h2>
                 <p class="lead rich" style="max-width:none;color:var(--text);">${rich(hook.intuition)}</p>`
              : `<h2 class="rich">${rich(hook.intuition)}</h2>`
          }
        </div>`;
    }

    if (step.key === "concept") {
      const realWorld = lesson.concept.real_world || [];
      return `
        <div class="stack-lg">
          <h2>Cómo funciona</h2>
          <ol class="lesson-list">
            ${(lesson.concept.points || [])
              .map((pt, i) => `<li><span class="lesson-step-idx">${i + 1}</span><span class="rich">${rich(pt)}</span></li>`)
              .join("")}
          </ol>
          ${
            realWorld.length
              ? `<div class="stack-sm">
                  <span class="eyebrow m-0">En la vida real</span>
                  <div class="grid-3" style="gap:12px;">
                    ${realWorld
                      .map(
                        (rw) => `
                        <div class="card-flat stack-sm" style="gap:6px;">
                          <strong class="small">${esc(rw.title)}</strong>
                          <p class="small muted m-0 rich">${rich(rw.detail)}</p>
                        </div>`
                      )
                      .join("")}
                  </div>
                </div>`
              : ""
          }
          ${
            chords.length
              ? `<div class="row" style="gap:12px;">
                  ${chords.map((c) => `<figure class="chord-figure m-0">${renderChordSVG(c)}</figure>`).join("")}
                </div>`
              : ""
          }
          <div class="card-tone stack-sm" style="padding:20px 24px;">
            <span class="eyebrow m-0">Para acordarte</span>
            <p class="title-sm m-0 rich">${rich(lesson.concept.key_rule)}</p>
          </div>
          <p class="callout callout-warn m-0"><strong>Error típico:</strong> <span class="rich">${rich(lesson.concept.pitfall)}</span></p>
        </div>`;
    }

    if (step.key === "example") {
      return `
        <div class="stack-lg">
          <h2>${esc(lesson.example.title)}</h2>
          <ol class="lesson-list">
            ${(lesson.example.steps || [])
              .map((st, i) => `<li><span class="lesson-step-idx">${i + 1}</span><span class="rich">${rich(st)}</span></li>`)
              .join("")}
          </ol>
          ${
            deepLab
              ? `<div class="card-tone row-between" style="padding:20px 24px;">
                  <span><strong>Probalo vos:</strong> hacé el ejemplo en el laboratorio y volvé para la comprobación.</span>
                  <a href="${deepLab}" class="btn btn-primary btn-wrap" data-lab-link>${icon("flask", 16)} ${esc(lesson.example.lab_cta || "Abrir laboratorio")}</a>
                </div>`
              : ""
          }
        </div>`;
    }

    if (step.key === "check") {
      const c = checks[checkIdx];
      if (!c) return `<p class="muted">Esta lección no tiene preguntas.</p>`;
      const chosen = c.picked !== null ? c.options[c.picked] : null;
      return `
        <div class="stack-lg">
          <div class="row-between">
            <span class="eyebrow m-0">Pregunta ${checkIdx + 1} de ${checks.length}</span>
            <div class="row gap-sm" aria-hidden="true">
              ${checks.map((x, i) => `<span class="pill ${x.solved ? "pill-green" : i === checkIdx ? "pill-accent" : ""}">${x.solved ? "✓" : i + 1}</span>`).join("")}
            </div>
          </div>
          <h2 class="title-md">${esc(c.question)}</h2>
          <div class="stack-sm">
            ${c.options
              .map((opt, idx) => {
                const isPicked = c.picked === idx;
                const cls = isPicked ? (opt.ok ? "right" : "wrong") : "";
                return `
                <button type="button" class="option-btn check-opt ${cls}" data-idx="${idx}" ${c.solved ? "disabled" : ""}>
                  <span class="opt-key">${String.fromCharCode(65 + idx)}</span>
                  <span class="rich">${rich(opt.text)}</span>
                </button>`;
              })
              .join("")}
          </div>
          ${
            chosen
              ? `<p class="callout ${chosen.ok ? "callout-ok" : "callout-warn"} m-0" role="status">
                  <strong>${chosen.ok ? "Correcto." : "Todavía no."}</strong> ${esc(chosen.feedback)}${chosen.ok ? "" : " Probá con otra."}
                 </p>`
              : ""
          }
        </div>`;
    }

    // takeaway
    return `
      <div class="stack-lg">
        <h2>Decilo con tus palabras</h2>
        <p class="lead" style="max-width:none;">${esc(lesson.takeaway_prompt || "Resumí en una o dos frases la idea más importante de esta lección.")}</p>
        <label class="field">
          <span>Tu resumen <span class="muted" style="font-weight:400;">(opcional, queda en tu cuaderno)</span></span>
          <textarea id="lesson-feynman" placeholder="Si se lo explicaras a un amigo en 20 segundos, ¿qué le dirías?">${esc(takeawayText)}</textarea>
        </label>
        ${
          !completedNow
            ? `<div><button id="complete-lesson-btn" class="btn btn-primary btn-lg" type="button">${icon("check", 18)} Terminar la lección</button></div>`
            : `<div class="card-tone stack">
                <div>
                  <h3 class="m-0">Lección terminada</h3>
                  <p class="m-0 muted">${
                    createdCards
                      ? `Sumé ${createdCards} ${createdCards === 1 ? "tarjeta" : "tarjetas"} con lo que te costó en la comprobación. `
                      : ""
                  }Ahora practicala: ahí es donde se fija.</p>
                </div>
                <div class="row">
                  <a href="#/review?node=${node.id}" class="btn btn-primary">${icon("brain", 16)} Practicar este tema</a>
                  ${
                    data.exercise_count
                      ? `<a href="#/ejercicios/${encodeURIComponent(domain.slug)}/${encodeURIComponent(node.slug)}" class="btn btn-secondary">${icon("target", 16)} Ejercicios del tema (${data.exercise_count})</a>`
                      : ""
                  }
                  ${next_node ? `<a href="#/learn/${next_node.id}" class="btn btn-secondary">Siguiente lección ${icon("arrowRight", 16)}</a>` : ""}
                </div>
              </div>`
        }
      </div>`;
  };

  function paint() {
    const onCheck = stepIdx === CHECK_STEP;
    const current = checks[checkIdx];
    let nextLabel = "Continuar";
    let nextDisabled = false;
    if (onCheck && !completedNow) {
      if (!current?.solved) nextDisabled = true;
      else if (checkIdx < checks.length - 1) nextLabel = "Siguiente pregunta";
    }

    container.innerHTML = `
      <div class="focus-column" data-tone="${tone}">
        <div class="page-header" style="padding-bottom:24px;">
          <div>
            <div class="breadcrumb">
              <a href="#/roadmap/${esc(domain.slug)}">${esc(domain.name)}</a> <span>/</span>
              <span>Lección ${node.position} de ${node.total_nodes}</span>
              ${completedNow ? `<span class="pill pill-green">${icon("check", 12)} Completada</span>` : ""}
            </div>
            <h1 class="title-md" style="font-size:clamp(2rem,4.2vw,3.25rem);">${esc(title)}</h1>
          </div>
        </div>

        <div class="lesson-stepper" role="tablist" aria-label="Pasos de la lección">
          ${STEPS.map((s, idx) => {
            const cls = idx === stepIdx ? "active" : idx < stepIdx || completedNow ? "done" : "";
            return `
            <button type="button" role="tab" aria-selected="${idx === stepIdx}" class="step-pill ${cls}" data-step="${idx}" ${canGoTo(idx) ? "" : "disabled"}>
              <span class="step-name">${s.name}</span>
            </button>`;
          }).join("")}
        </div>

        <div class="card" style="padding:clamp(24px,4vw,44px);">${stepHtml()}</div>

        <div class="row-between mt-lg">
          <div>
            ${
              stepIdx > 0
                ? `<button id="prev-step" class="btn btn-secondary" type="button">${icon("arrowLeft", 16)} Anterior</button>`
                : prev_node
                ? `<a href="#/learn/${prev_node.id}" class="btn btn-secondary">${icon("arrowLeft", 16)} Lección anterior</a>`
                : ""
            }
          </div>
          ${
            stepIdx < STEPS.length - 1
              ? `<button id="next-step" class="btn btn-primary" type="button" ${nextDisabled ? "disabled" : ""}>${nextLabel} ${icon("arrowRight", 16)}</button>`
              : ""
          }
        </div>
      </div>
    `;

    container.querySelectorAll("[data-lab-link]").forEach((a) =>
      a.addEventListener("click", () => {
        try {
          sessionStorage.setItem("aprendelab_return", location.hash);
        } catch {
          // ignore
        }
      })
    );
    container.querySelectorAll(".step-pill").forEach((b) => b.addEventListener("click", () => goTo(Number(b.dataset.step))));
    container.querySelector("#prev-step")?.addEventListener("click", () => {
      if (onCheck && checkIdx > 0) {
        checkIdx -= 1;
        paint();
      } else {
        goTo(stepIdx - 1);
      }
    });
    container.querySelector("#next-step")?.addEventListener("click", () => {
      if (onCheck && checkIdx < checks.length - 1 && (current?.solved || completedNow)) {
        checkIdx += 1;
        paint();
      } else {
        goTo(stepIdx + 1);
      }
    });
    container.querySelectorAll(".check-opt").forEach((b) =>
      b.addEventListener("click", () => {
        const c = checks[checkIdx];
        c.picked = Number(b.dataset.idx);
        if (c.options[c.picked]?.ok) c.solved = true;
        else c.missed = true;
        paint();
        container.querySelector(c.solved ? "#next-step" : ".check-opt:not(.wrong)")?.focus({ preventScroll: true });
      })
    );
    container.querySelector("#complete-lesson-btn")?.addEventListener("click", async () => {
      const area = container.querySelector("#lesson-feynman");
      takeawayText = area ? area.value : takeawayText;
      const missed = checks
        .filter((c) => c.missed)
        .map((c) => {
          const correct = c.options.findIndex((o) => o.ok);
          return {
            question: c.question,
            options: c.options.map((o) => o.text),
            correct,
            feedback: c.options[correct]?.feedback || "",
          };
        });
      try {
        const res = await api.post(`/api/nodes/${node.id}/lesson/complete`, {
          feynman_note: takeawayText,
          missed_checks: missed,
        });
        completedNow = true;
        createdCards = res.created_cards || 0;
        paint();
      } catch (err) {
        toast(err.message, "err");
      }
    });
  }

  paint();
}

