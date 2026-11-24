/**
 * Editorial SVG artwork (320×120 banners) and matching emblem logos (24×24)
 * for each subject, with 4 curated selectable options per discipline.
 *
 * Every graphic uses `currentColor` and layered opacities so it adapts cleanly
 * to each discipline's flat tone block in both light and dark themes.
 */

const STORAGE_KEY = "aprendelab_subject_art_v1";

export const SUBJECT_ORDER = ["math", "physics", "clyrp", "electronics", "guitar"];

export const ART_GALLERY = {
  math: {
    key: "math",
    label: "Matemáticas",
    tone: "math",
    options: [
      {
        id: "v1",
        name: "Plano y parábola",
        desc: "Ejes cartesianos, área bajo la curva y punto tangente.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <g stroke-width="1" opacity="0.18">
              <path d="M44 12V108M96 12V108M148 12V108M200 12V108M252 12V108M304 12V108M18 28H306M18 52H306M18 76H306"/>
            </g>
            <path d="M46 100 Q 152 -10, 258 100 Z" fill="currentColor" stroke="none" opacity="0.11"/>
            <g stroke-width="1.6" opacity="0.65">
              <path d="M18 100 H304 M296 95 l8 5 l-8 5"/>
              <path d="M96 112 V12 M91 20 l5 -8 l5 8"/>
            </g>
            <path d="M46 100 Q 152 -10, 258 100" stroke-width="2.6"/>
            <path d="M124 22 L274 88" stroke-width="1.8" stroke-dasharray="6 5" opacity="0.72"/>
            <path d="M200 56 V100 M96 56 H200" stroke-width="1.2" stroke-dasharray="3 4" opacity="0.48"/>
            <circle cx="152" cy="45" r="4" fill="currentColor" stroke="none" opacity="0.55"/>
            <circle cx="200" cy="56" r="14" stroke-width="1.4" opacity="0.38"/>
            <circle cx="200" cy="56" r="6.5" fill="currentColor" stroke="none"/>
          </svg>`,
        logo: `<path d="M4 19h16M7 4v16" opacity="0.45"/><path d="M5 18Q12.5 2 20 18"/><circle cx="12.5" cy="10" r="1.8" fill="currentColor" stroke="none"/>`,
      },
      {
        id: "v2",
        name: "Geometría y compás",
        desc: "Círculo unitario, triángulo trigonométrico y escuadra.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <path d="M112 62 L134 62 A22 22 0 0 0 129 48 Z" fill="currentColor" stroke="none" opacity="0.22"/>
            <circle cx="112" cy="62" r="44" stroke-width="2.2"/>
            <path d="M56 62 H168 M112 10 V112" stroke-width="1.3" opacity="0.4"/>
            <path d="M112 62 L147 35 V62 Z" fill="currentColor" fill-opacity="0.12" stroke-width="2.2"/>
            <path d="M139 62 V54 H147" stroke-width="1.4" opacity="0.75"/>
            <circle cx="147" cy="35" r="5" fill="currentColor" stroke="none"/>
            <path d="M192 98 H292 V22 Z" fill="currentColor" fill-opacity="0.1" stroke-width="2.2"/>
            <path d="M226 84 H278 V44 Z" stroke-width="1.5" opacity="0.55"/>
            <g stroke-width="1.3" opacity="0.5">
              <path d="M210 98 v-5 M226 98 v-7 M242 98 v-5 M258 98 v-7 M274 98 v-5"/>
            </g>
            <path d="M174 22 A76 76 0 0 1 224 108" stroke-width="1.5" stroke-dasharray="5 5" opacity="0.55"/>
          </svg>`,
        logo: `<circle cx="12" cy="5.5" r="2"/><path d="M10.7 7.3 5.5 20M13.3 7.3 18.5 20M6.5 14.5a7.5 7.5 0 0 0 11 0"/>`,
      },
      {
        id: "v3",
        name: "Espiral áurea y poliedro",
        desc: "Proporción de Fibonacci y geometría espacial isométrica.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <rect x="34" y="18" width="136" height="84" rx="3" fill="currentColor" fill-opacity="0.07" stroke-width="1.8" opacity="0.75"/>
            <path d="M118 18 V102 M118 70 H170 M138 70 V102 M118 82 H138" stroke-width="1.2" opacity="0.45"/>
            <path d="M34 102 A84 84 0 0 1 118 18 A52 52 0 0 1 170 70 A32 32 0 0 1 138 102 A20 20 0 0 1 118 82 A12 12 0 0 1 130 70" stroke-width="2.6"/>
            <circle cx="130" cy="70" r="3.5" fill="currentColor" stroke="none"/>
            <g transform="translate(244 60)">
              <polygon points="0,-42 38,-14 24,34 -24,34 -38,-14" fill="currentColor" fill-opacity="0.09" stroke-width="2"/>
              <polygon points="0,-42 18,-4 -18,-4" fill="currentColor" fill-opacity="0.16" stroke-width="1.6"/>
              <path d="M-38,-14 L-18,-4 L-24,34 M38,-14 L18,-4 L24,34 M-18,-4 L0,18 L18,-4 M0,18 L-24,34 M0,18 L24,34" stroke-width="1.6" opacity="0.8"/>
              <path d="M0,-42 V18" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.45"/>
            </g>
          </svg>`,
        logo: `<rect x="3" y="5" width="18" height="14" rx="1.5" opacity="0.45"/><path d="M13 5v14M13 13h8" opacity="0.4"/><path d="M3 19A14 14 0 0 1 13 5a8 8 0 0 1 8 8 6 6 0 0 1-6 6 3 3 0 0 1-3-3"/>`,
      },
      {
        id: "v4",
        name: "Funciones y simetría",
        desc: "Exponencial, logaritmo inverso, onda seno y sumatoria.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="64" cy="60" r="34" fill="currentColor" fill-opacity="0.11" stroke-width="1.6" opacity="0.8"/>
            <path d="M78 42 H50 L66 60 L50 78 H78" stroke-width="2.8"/>
            <path d="M126 102 L206 22" stroke-width="1.3" stroke-dasharray="4 4" opacity="0.5"/>
            <path d="M122 92 C148 90, 166 74, 178 20" stroke-width="2.4"/>
            <path d="M138 106 C152 68, 172 48, 212 40" stroke-width="2.4" opacity="0.72"/>
            <circle cx="159" cy="69" r="4.5" fill="currentColor" stroke="none"/>
            <path d="M214 60 H304" stroke-width="1.2" opacity="0.35"/>
            <path d="M218 60 Q232 22, 246 60 T274 60 T302 60" stroke-width="2.4"/>
            <circle cx="232" cy="41" r="3.5" fill="currentColor" stroke="none" opacity="0.7"/>
            <circle cx="260" cy="79" r="3.5" fill="currentColor" stroke="none" opacity="0.7"/>
          </svg>`,
        logo: `<path d="M18 5H6.5L13 12l-6.5 7H18"/><path d="M18 5v2.5M18 16.5V19"/>`,
      },
    ],
  },

  physics: {
    key: "physics",
    label: "Física",
    tone: "physics",
    options: [
      {
        id: "v1",
        name: "Tiro parabólico y vectores",
        desc: "Trayectoria balística con descomposición de velocidad.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <line x1="16" y1="102" x2="304" y2="102" stroke-width="1.8"/>
            <g stroke-width="1.2" opacity="0.32">
              <path d="M28 102 l-6 8 M52 102 l-6 8 M76 102 l-6 8 M100 102 l-6 8 M124 102 l-6 8 M148 102 l-6 8 M172 102 l-6 8 M196 102 l-6 8 M220 102 l-6 8 M244 102 l-6 8 M268 102 l-6 8 M292 102 l-6 8"/>
            </g>
            <path d="M30 102 Q 154 -22, 278 102" stroke-width="2.2" stroke-dasharray="6 5" opacity="0.75"/>
            <path d="M154 40 V102" stroke-width="1.2" stroke-dasharray="3 4" opacity="0.45"/>
            <circle cx="68" cy="72" r="4.5" fill="currentColor" stroke="none" opacity="0.28"/>
            <circle cx="154" cy="40" r="5" fill="currentColor" stroke="none" opacity="0.42"/>
            <circle cx="236" cy="70" r="4.5" fill="currentColor" stroke="none" opacity="0.28"/>
            <path d="M114 46 H172 V16 H114" stroke-width="1.2" stroke-dasharray="3 4" opacity="0.45"/>
            <path d="M114 46 H172 M164 40 l8 6 l-8 6" stroke-width="2" opacity="0.75"/>
            <path d="M114 46 V16 M108 24 l6 -8 l6 8" stroke-width="2" opacity="0.75"/>
            <path d="M114 46 L172 16 M161 15 l11 1 l-5 10" stroke-width="2.8"/>
            <circle cx="114" cy="46" r="9.5" fill="currentColor" stroke="none"/>
            <circle cx="278" cy="102" r="4" fill="currentColor" stroke="none"/>
          </svg>`,
        logo: `<path d="M3 19h18" opacity="0.4"/><path d="M4 19Q11.5 2 20 16" stroke-dasharray="2.5 2.5"/><path d="M10 10l7-5m-4-.5 4 .5-.8 3.8"/><circle cx="10" cy="10" r="2.2" fill="currentColor" stroke="none"/>`,
      },
      {
        id: "v2",
        name: "Estática y plano inclinado",
        desc: "Bloque en rampa, diagrama de fuerzas y polea colgante.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <path d="M36 102 H214 V28 Z" fill="currentColor" fill-opacity="0.1" stroke-width="2"/>
            <path d="M74 102 A38 38 0 0 0 71 87" stroke-width="1.6" opacity="0.65"/>
            <g transform="translate(132 61) rotate(-22.6)">
              <rect x="-20" y="-15" width="40" height="30" rx="4" fill="currentColor" fill-opacity="0.18" stroke-width="2.2"/>
              <path d="M0 0 V-38 M-5 -31 l5 -7 l5 7" stroke-width="2.2"/>
              <path d="M20 0 H76" stroke-width="2"/>
            </g>
            <path d="M132 61 V99 M126 91 l6 8 l6 -8" stroke-width="2.4"/>
            <circle cx="220" cy="24" r="11" fill="currentColor" fill-opacity="0.14" stroke-width="2.2"/>
            <circle cx="220" cy="24" r="3" fill="currentColor" stroke="none"/>
            <line x1="231" y1="24" x2="231" y2="62" stroke-width="2"/>
            <rect x="218" y="62" width="26" height="24" rx="4" fill="currentColor" fill-opacity="0.22" stroke-width="2"/>
            <path d="M231 86 V108 M226 102 l5 6 l5 -6" stroke-width="2" opacity="0.8"/>
            <line x1="20" y1="102" x2="296" y2="102" stroke-width="1.5" opacity="0.5"/>
          </svg>`,
        logo: `<path d="M4 19h16V8L4 19Z" opacity="0.45"/><rect x="8.5" y="7.5" width="6" height="4.5" rx="1" transform="rotate(-33 11.5 9.8)"/><path d="M14 8l5-3.2m-3-.5 3 .5-.7 2.8"/>`,
      },
      {
        id: "v3",
        name: "Átomo y ondas EM",
        desc: "Órbitas concéntricas y propagación electromagnética.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="110" cy="60" r="16" fill="currentColor" stroke="none" opacity="0.16"/>
            <circle cx="110" cy="60" r="7" fill="currentColor" stroke="none"/>
            <g stroke-width="1.9">
              <ellipse cx="110" cy="60" rx="58" ry="20"/>
              <ellipse cx="110" cy="60" rx="58" ry="20" transform="rotate(60 110 60)"/>
              <ellipse cx="110" cy="60" rx="58" ry="20" transform="rotate(-60 110 60)"/>
            </g>
            <circle cx="168" cy="60" r="4.5" fill="currentColor" stroke="none"/>
            <circle cx="81" cy="21" r="4.5" fill="currentColor" stroke="none"/>
            <circle cx="86" cy="98" r="4.5" fill="currentColor" stroke="none"/>
            <path d="M188 60 H302 M295 55 l7 5 l-7 5" stroke-width="1.5" opacity="0.5"/>
            <path d="M192 60 Q206 20, 220 60 T248 60 T276 60 T296 60" stroke-width="2.4"/>
            <path d="M192 60 Q206 86, 220 60 T248 60 T276 60 T296 60" stroke-width="1.5" stroke-dasharray="4 4" opacity="0.55"/>
          </svg>`,
        logo: `<circle cx="12" cy="12" r="2.2" fill="currentColor" stroke="none"/><ellipse cx="12" cy="12" rx="9" ry="3.8" transform="rotate(30 12 12)"/><ellipse cx="12" cy="12" rx="9" ry="3.8" transform="rotate(-30 12 12)"/><ellipse cx="12" cy="12" rx="9" ry="3.8" transform="rotate(90 12 12)"/>`,
      },
      {
        id: "v4",
        name: "Péndulo y oscilación",
        desc: "Movimiento armónico simple y onda amortiguada.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <line x1="34" y1="16" x2="134" y2="16" stroke-width="2.4"/>
            <circle cx="84" cy="16" r="3.5" fill="currentColor" stroke="none"/>
            <path d="M40 78 A76 76 0 0 0 128 78" stroke-width="1.6" stroke-dasharray="5 5" opacity="0.55"/>
            <line x1="84" y1="16" x2="54" y2="84" stroke-width="1.4" opacity="0.28"/>
            <circle cx="54" cy="84" r="9" fill="currentColor" stroke="none" opacity="0.22"/>
            <line x1="84" y1="16" x2="84" y2="92" stroke-width="1.4" opacity="0.4"/>
            <circle cx="84" cy="92" r="9" fill="currentColor" stroke="none" opacity="0.34"/>
            <line x1="84" y1="16" x2="116" y2="83" stroke-width="2.2"/>
            <circle cx="116" cy="83" r="10.5" fill="currentColor" stroke="none"/>
            <line x1="158" y1="60" x2="304" y2="60" stroke-width="1.3" opacity="0.38"/>
            <path d="M162 20 Q232 34, 302 52 M162 100 Q232 86, 302 68" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.4"/>
            <path d="M162 60 C172 14, 184 14, 194 60 C204 98, 216 98, 226 60 C236 28, 248 28, 258 60 C268 84, 280 84, 290 60 C295 48, 300 48, 304 60" stroke-width="2.5"/>
          </svg>`,
        logo: `<path d="M5 4h14M12 4l5 12"/><circle cx="17" cy="16.5" r="2.5" fill="currentColor" stroke="none"/><path d="M6.5 16.5a8.5 8.5 0 0 0 8 2.5" stroke-dasharray="2.2 2.2"/>`,
      },
    ],
  },

  clyrp: {
    key: "clyrp",
    label: "Comprensión lectora y resolución de problemas",
    tone: "generic",
    options: [
      {
        id: "v1",
        name: "Lectura y mapa conceptual",
        desc: "Texto subrayado conectado a nodos de síntesis e ideas.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <path d="M26 26 H86 a12 12 0 0 1 12 12 V100 a10 10 0 0 0 -10 -10 H26 Z" fill="currentColor" fill-opacity="0.09" stroke-width="2.2"/>
            <path d="M170 26 H110 a12 12 0 0 0 -12 12 V100 a10 10 0 0 1 10 -10 H170 Z" fill="currentColor" fill-opacity="0.06" stroke-width="2.2"/>
            <rect x="38" y="42" width="44" height="7" rx="3.5" fill="currentColor" stroke="none" opacity="0.28"/>
            <path d="M38 58 H82 M38 70 H76 M114 44 H156 M114 58 H148" stroke-width="1.8" opacity="0.6"/>
            <rect x="114" y="68" width="40" height="7" rx="3.5" fill="currentColor" stroke="none" opacity="0.28"/>
            <path d="M170 58 C192 58, 196 58, 212 58 M236 52 C252 44, 256 32, 272 30 M236 58 H274 M236 64 C252 72, 256 86, 272 88" stroke-width="2" opacity="0.78"/>
            <circle cx="224" cy="58" r="12" fill="currentColor" fill-opacity="0.22" stroke-width="2.2"/>
            <circle cx="282" cy="30" r="8" fill="currentColor" stroke="none"/>
            <circle cx="284" cy="58" r="8" fill="currentColor" fill-opacity="0.16" stroke-width="2"/>
            <circle cx="282" cy="88" r="8" fill="currentColor" fill-opacity="0.16" stroke-width="2"/>
          </svg>`,
        logo: `<path d="M3 6.5A2 2 0 0 1 5 4.5h4.5A2.5 2.5 0 0 1 12 7v12a2 2 0 0 0-2-1.5H5a2 2 0 0 1-2-2V6.5Z"/><path d="M21 6.5A2 2 0 0 0 19 4.5h-4.5A2.5 2.5 0 0 0 12 7v12a2 2 0 0 1 2-1.5h5a2 2 0 0 0 2-2V6.5Z"/><circle cx="12" cy="3.2" r="1.4" fill="currentColor" stroke="none"/>`,
      },
      {
        id: "v2",
        name: "Lógica y diagramas de Venn",
        desc: "Conjuntos, intersecciones e implicación hipótesis → tesis.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <g fill="currentColor" fill-opacity="0.11" stroke-width="2">
              <circle cx="88" cy="50" r="32"/>
              <circle cx="128" cy="50" r="32"/>
              <circle cx="108" cy="78" r="32"/>
            </g>
            <circle cx="108" cy="58" r="5.5" fill="currentColor" stroke="none"/>
            <rect x="184" y="42" width="38" height="34" rx="8" fill="currentColor" fill-opacity="0.14" stroke-width="2"/>
            <path d="M198 52 V66 M208 52 V66 M198 59 H208" stroke-width="2"/>
            <path d="M222 55 H248 M222 63 H248 M242 50 l9 9 l-9 9" stroke-width="2"/>
            <rect x="256" y="42" width="38" height="34" rx="8" fill="currentColor" fill-opacity="0.22" stroke-width="2.2"/>
            <path d="M268 53 H282 M275 53 V66" stroke-width="2.2"/>
            <path d="M150 58 H178" stroke-width="1.4" stroke-dasharray="4 4" opacity="0.5"/>
          </svg>`,
        logo: `<circle cx="9.2" cy="9.5" r="5.2" fill="currentColor" fill-opacity="0.12"/><circle cx="14.8" cy="9.5" r="5.2" fill="currentColor" fill-opacity="0.12"/><circle cx="12" cy="14.5" r="5.2" fill="currentColor" fill-opacity="0.12"/>`,
      },
      {
        id: "v3",
        name: "Estrategia de Pólya",
        desc: "Ruta paso a paso, lupa de análisis y objetivo resuelto.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <g stroke-width="1" opacity="0.18">
              <path d="M40 20V100M80 20V100M120 20V100M160 20V100M200 20V100M240 20V100M280 20V100M28 32H292M28 60H292M28 88H292"/>
            </g>
            <path d="M46 88 H110 V54 H196 V34 H266" stroke-width="2.8"/>
            <circle cx="46" cy="88" r="6" fill="currentColor" stroke="none"/>
            <circle cx="110" cy="54" r="6" fill="currentColor" fill-opacity="0.25" stroke-width="2"/>
            <circle cx="196" cy="34" r="6" fill="currentColor" fill-opacity="0.25" stroke-width="2"/>
            <circle cx="154" cy="54" r="24" fill="currentColor" fill-opacity="0.1" stroke-width="2.4"/>
            <line x1="171" y1="71" x2="192" y2="92" stroke-width="3.6"/>
            <circle cx="268" cy="34" r="14" stroke-width="1.8" opacity="0.55"/>
            <circle cx="268" cy="34" r="7" fill="currentColor" stroke="none"/>
          </svg>`,
        logo: `<circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 4.8 4.8"/><path d="M7.5 11.5 9.8 13.5 13.8 8.5"/>`,
      },
      {
        id: "v4",
        name: "Datos, tablas y gráficos",
        desc: "Cuadro de doble entrada, barras, tendencia y torta.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <rect x="24" y="24" width="96" height="74" rx="7" stroke-width="2"/>
            <rect x="24" y="24" width="96" height="20" rx="7" fill="currentColor" stroke="none" opacity="0.2"/>
            <path d="M24 44 H120 M24 62 H120 M24 80 H120 M62 24 V98 M92 24 V98" stroke-width="1.3" opacity="0.55"/>
            <rect x="64" y="64" width="26" height="14" fill="currentColor" stroke="none" opacity="0.24"/>
            <rect x="142" y="66" width="14" height="32" rx="3" fill="currentColor" fill-opacity="0.18" stroke-width="1.8"/>
            <rect x="164" y="48" width="14" height="50" rx="3" fill="currentColor" fill-opacity="0.26" stroke-width="1.8"/>
            <rect x="186" y="56" width="14" height="42" rx="3" fill="currentColor" fill-opacity="0.18" stroke-width="1.8"/>
            <rect x="208" y="34" width="14" height="64" rx="3" fill="currentColor" fill-opacity="0.34" stroke-width="1.8"/>
            <path d="M149 54 L171 36 L193 44 L215 22" stroke-width="2.2"/>
            <circle cx="215" cy="22" r="4" fill="currentColor" stroke="none"/>
            <circle cx="268" cy="64" r="28" stroke-width="2"/>
            <path d="M268 64 L268 36 A28 28 0 0 1 296 64 Z" fill="currentColor" fill-opacity="0.3" stroke-width="2"/>
            <circle cx="268" cy="64" r="10" fill="currentColor" fill-opacity="0.08" stroke-width="1.4"/>
          </svg>`,
        logo: `<path d="M4 19h16"/><rect x="5.5" y="12" width="3" height="7" rx="0.8"/><rect x="10.5" y="8" width="3" height="11" rx="0.8"/><rect x="15.5" y="5" width="3" height="14" rx="0.8" fill="currentColor" fill-opacity="0.25"/>`,
      },
    ],
  },

  electronics: {
    key: "electronics",
    label: "Electrónica (Arduino / ESP32)",
    tone: "electronics",
    options: [
      {
        id: "v1",
        name: "Microcontrolador PCB",
        desc: "Chip MCU central, pistas a 45°, resistor y LED.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <rect x="124" y="22" width="72" height="76" rx="8" fill="currentColor" fill-opacity="0.1" stroke-width="2.4"/>
            <rect x="142" y="40" width="36" height="40" rx="4" fill="currentColor" fill-opacity="0.24" stroke-width="1.6"/>
            <circle cx="136" cy="34" r="3" fill="currentColor" stroke="none"/>
            <path d="M142 22 V10 M160 22 V10 M178 22 V10 M142 98 V110 M160 98 V110 M178 98 V110" stroke-width="2"/>
            <path d="M124 40 H94 L78 24 H28 M124 60 H88 M124 80 H92 L76 96 H64" stroke-width="2"/>
            <path d="M64 96 l-5 -9 l-7 18 l-7 -18 l-7 18 l-5 -9 H22" stroke-width="2"/>
            <path d="M196 36 H228 L244 20 H292 M196 60 H294 M196 84 H228 L244 100 H292" stroke-width="2"/>
            <circle cx="28" cy="24" r="5" fill="currentColor" fill-opacity="0.2" stroke-width="2"/>
            <circle cx="22" cy="96" r="5" fill="currentColor" fill-opacity="0.2" stroke-width="2"/>
            <circle cx="292" cy="20" r="5" fill="currentColor" stroke="none"/>
            <circle cx="294" cy="60" r="5" fill="currentColor" fill-opacity="0.2" stroke-width="2"/>
            <circle cx="292" cy="100" r="5" fill="currentColor" stroke="none"/>
            <polygon points="248,60 264,51 264,69" fill="currentColor" fill-opacity="0.25" stroke-width="1.8"/>
            <line x1="248" y1="50" x2="248" y2="70" stroke-width="2"/>
          </svg>`,
        logo: `<rect x="6" y="6" width="12" height="12" rx="2"/><rect x="9.5" y="9.5" width="5" height="5" rx="0.6" fill="currentColor" fill-opacity="0.3"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>`,
      },
      {
        id: "v2",
        name: "Osciloscopio y PWM",
        desc: "Retícula de medición con señal digital cuadrada y analógica.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <rect x="20" y="12" width="280" height="96" rx="10" fill="currentColor" fill-opacity="0.06" stroke-width="2"/>
            <g stroke-width="1" opacity="0.2">
              <path d="M60 12V108M100 12V108M140 12V108M180 12V108M220 12V108M260 12V108M20 36H300M20 60H300M20 84H300"/>
            </g>
            <path d="M32 54 H58 V28 H94 V54 H130 V28 H166 V54 H202 V28 H238 V54 H288" stroke-width="2.4"/>
            <path d="M32 82 Q52 56, 72 82 T112 82 T152 82 T192 82 T232 82 T272 82 T288 76" stroke-width="2.2" opacity="0.72"/>
            <line x1="166" y1="16" x2="166" y2="104" stroke-width="1.3" stroke-dasharray="4 4" opacity="0.55"/>
            <circle cx="166" cy="28" r="4.5" fill="currentColor" stroke="none"/>
            <circle cx="166" cy="92" r="4" fill="currentColor" stroke="none" opacity="0.7"/>
          </svg>`,
        logo: `<rect x="3" y="4.5" width="18" height="15" rx="2.5" opacity="0.45"/><path d="M5.5 14h2.8V9h3.4v5h3.2V9h3.6"/>`,
      },
      {
        id: "v3",
        name: "Esquemático eléctrico",
        desc: "Fuente DC, resistencia, capacitor y puesta a tierra.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <path d="M56 44 V24 H114 M174 24 H262 V48 M262 72 V96 H56 V76" stroke-width="2.2"/>
            <circle cx="56" cy="60" r="16" fill="currentColor" fill-opacity="0.12" stroke-width="2.2"/>
            <path d="M51 54 H61 M56 49 V59 M51 67 H61" stroke-width="1.8"/>
            <path d="M114 24 l5 -10 l10 20 l10 -20 l10 20 l10 -20 l10 20 l5 -10" stroke-width="2.4"/>
            <path d="M244 54 H280 M244 66 H280" stroke-width="2.6"/>
            <path d="M196 24 V96" stroke-width="1.6" stroke-dasharray="4 4" opacity="0.45"/>
            <circle cx="196" cy="24" r="4.5" fill="currentColor" stroke="none"/>
            <circle cx="196" cy="96" r="4.5" fill="currentColor" stroke="none"/>
            <path d="M158 96 V106 M144 106 H172 M149 111 H167 M154 116 H162" stroke-width="2"/>
          </svg>`,
        logo: `<path d="M2 12h3.5l1.6-4 3 8 3-8 3 8 1.6-4H22"/><circle cx="3" cy="12" r="1.4" fill="currentColor" stroke="none"/><circle cx="21" cy="12" r="1.4" fill="currentColor" stroke="none"/>`,
      },
      {
        id: "v4",
        name: "Placa ESP32 y antena Wi-Fi",
        desc: "DevBoard con puerto USB, pines GPIO y antena PCB RF.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <rect x="44" y="24" width="182" height="72" rx="9" fill="currentColor" fill-opacity="0.08" stroke-width="2.2"/>
            <rect x="30" y="44" width="18" height="32" rx="3" fill="currentColor" fill-opacity="0.22" stroke-width="2"/>
            <rect x="108" y="38" width="60" height="44" rx="4" fill="currentColor" fill-opacity="0.18" stroke-width="2"/>
            <g fill="currentColor" stroke="none" opacity="0.72">
              <circle cx="64" cy="33" r="3"/><circle cx="78" cy="33" r="3"/><circle cx="92" cy="33" r="3"/><circle cx="106" cy="33" r="3"/>
              <circle cx="120" cy="33" r="3"/><circle cx="134" cy="33" r="3"/><circle cx="148" cy="33" r="3"/><circle cx="162" cy="33" r="3"/>
              <circle cx="64" cy="87" r="3"/><circle cx="78" cy="87" r="3"/><circle cx="92" cy="87" r="3"/><circle cx="106" cy="87" r="3"/>
              <circle cx="120" cy="87" r="3"/><circle cx="134" cy="87" r="3"/><circle cx="148" cy="87" r="3"/><circle cx="162" cy="87" r="3"/>
            </g>
            <path d="M180 76 V42 H190 V68 H200 V42 H210 V76" stroke-width="2.2"/>
            <path d="M242 46 A20 20 0 0 1 242 74" stroke-width="2.2"/>
            <path d="M256 35 A34 34 0 0 1 256 85" stroke-width="2" opacity="0.7"/>
            <path d="M270 24 A48 48 0 0 1 270 96" stroke-width="1.8" opacity="0.45"/>
          </svg>`,
        logo: `<path d="M4.5 10.5a10.5 10.5 0 0 1 15 0M7.8 14a6 6 0 0 1 8.4 0"/><circle cx="12" cy="18" r="1.8" fill="currentColor" stroke="none"/>`,
      },
    ],
  },

  guitar: {
    key: "guitar",
    label: "Guitarra",
    tone: "guitar",
    options: [
      {
        id: "v1",
        name: "Diapasón y onda acústica",
        desc: "Trastes, marcadores, acorde pisado y cuerda vibrante.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round">
            <rect x="20" y="18" width="280" height="84" rx="6" fill="currentColor" fill-opacity="0.06" stroke="none"/>
            <line x1="24" y1="18" x2="24" y2="102" stroke-width="4.5"/>
            <g stroke-width="2" opacity="0.45">
              <line x1="88" y1="18" x2="88" y2="102"/><line x1="152" y1="18" x2="152" y2="102"/>
              <line x1="216" y1="18" x2="216" y2="102"/><line x1="280" y1="18" x2="280" y2="102"/>
            </g>
            <circle cx="120" cy="60" r="4.5" fill="currentColor" stroke="none" opacity="0.22"/>
            <circle cx="248" cy="60" r="4.5" fill="currentColor" stroke="none" opacity="0.22"/>
            <g opacity="0.58">
              <line x1="14" y1="26" x2="306" y2="26" stroke-width="1"/>
              <line x1="14" y1="40" x2="306" y2="40" stroke-width="1.15"/>
              <line x1="14" y1="54" x2="306" y2="54" stroke-width="1.3"/>
              <line x1="14" y1="68" x2="306" y2="68" stroke-width="1.45"/>
              <line x1="14" y1="82" x2="306" y2="82" stroke-width="1.6"/>
              <line x1="14" y1="96" x2="306" y2="96" stroke-width="1.8"/>
            </g>
            <path d="M14 54 Q52 24, 90 54 T166 54 T242 54 T306 54" stroke-width="2.6"/>
            <circle cx="56" cy="40" r="13" stroke-width="1.4" opacity="0.35"/>
            <circle cx="56" cy="40" r="8" fill="currentColor" stroke="none"/>
            <circle cx="120" cy="68" r="8" fill="currentColor" stroke="none"/>
            <circle cx="184" cy="82" r="8" fill="currentColor" stroke="none"/>
          </svg>`,
        logo: `<path d="M5 5h14" stroke-width="2.2"/><path d="M5 5v14M12 5v14M19 5v14M5 10h14M5 15h14" opacity="0.5"/><circle cx="8.5" cy="12.5" r="1.8" fill="currentColor" stroke="none"/><circle cx="15.5" cy="7.5" r="1.8" fill="currentColor" stroke="none"/><circle cx="15.5" cy="17.5" r="1.8" fill="currentColor" stroke="none"/>`,
      },
      {
        id: "v2",
        name: "Boca acústica y roseta",
        desc: "Detalle de caja acústica, roseta concéntrica y puente.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round">
            <circle cx="124" cy="60" r="48" stroke-width="1.4" stroke-dasharray="4 4" opacity="0.5"/>
            <circle cx="124" cy="60" r="42" stroke-width="2.2"/>
            <circle cx="124" cy="60" r="34" fill="currentColor" fill-opacity="0.16" stroke-width="1.6"/>
            <rect x="234" y="24" width="22" height="72" rx="4" fill="currentColor" fill-opacity="0.18" stroke-width="2.2"/>
            <line x1="241" y1="30" x2="241" y2="90" stroke-width="1.8" opacity="0.75"/>
            <g stroke-width="1.5" opacity="0.72">
              <line x1="16" y1="35" x2="248" y2="35"/><line x1="16" y1="45" x2="248" y2="45"/>
              <line x1="16" y1="55" x2="248" y2="55"/><line x1="16" y1="65" x2="248" y2="65"/>
              <line x1="16" y1="75" x2="248" y2="75"/><line x1="16" y1="85" x2="248" y2="85"/>
            </g>
            <g fill="currentColor" stroke="none">
              <circle cx="249" cy="35" r="2.8"/><circle cx="249" cy="45" r="2.8"/><circle cx="249" cy="55" r="2.8"/>
              <circle cx="249" cy="65" r="2.8"/><circle cx="249" cy="75" r="2.8"/><circle cx="249" cy="85" r="2.8"/>
            </g>
            <path d="M274 36 A36 36 0 0 1 274 84" stroke-width="1.8" opacity="0.45"/>
            <path d="M286 24 A50 50 0 0 1 286 96" stroke-width="1.4" opacity="0.28"/>
          </svg>`,
        logo: `<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="5" fill="currentColor" fill-opacity="0.18"/><path d="M3 9h18M3 12h18M3 15h18" opacity="0.7"/>`,
      },
      {
        id: "v3",
        name: "Clavijero y pentagrama",
        desc: "Silueta de clavijero clásico y flujo musical de corcheas.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <path d="M32 32 L116 40 V80 L32 88 Z" fill="currentColor" fill-opacity="0.12" stroke-width="2.2"/>
            <path d="M116 44 H144 M116 76 H144" stroke-width="2"/>
            <g stroke-width="2">
              <path d="M50 33 V20 M74 36 V22 M98 38 V24 M50 87 V100 M74 84 V98 M98 82 V96"/>
            </g>
            <g fill="currentColor" stroke="none">
              <circle cx="50" cy="18" r="4.2"/><circle cx="74" cy="20" r="4.2"/><circle cx="98" cy="22" r="4.2"/>
              <circle cx="50" cy="102" r="4.2"/><circle cx="74" cy="100" r="4.2"/><circle cx="98" cy="98" r="4.2"/>
            </g>
            <g stroke-width="1.2" opacity="0.45">
              <path d="M154 34 Q226 24, 300 34 M154 46 Q226 36, 300 46 M154 58 Q226 48, 300 58 M154 70 Q226 60, 300 70 M154 82 Q226 72, 300 82"/>
            </g>
            <path d="M204 72 V34 L252 26 V64" stroke-width="2.4"/>
            <path d="M204 42 L252 34" stroke-width="2"/>
            <ellipse cx="196" cy="73" rx="8.5" ry="6" transform="rotate(-18 196 73)" fill="currentColor" stroke="none"/>
            <ellipse cx="244" cy="65" rx="8.5" ry="6" transform="rotate(-18 244 65)" fill="currentColor" stroke="none"/>
            <path d="M282 78 V44" stroke-width="2.4"/>
            <ellipse cx="275" cy="79" rx="7.5" ry="5.5" transform="rotate(-18 275 79)" fill="currentColor" stroke="none"/>
          </svg>`,
        logo: `<path d="M9 17.5V6l10-2v11.5"/><circle cx="6.5" cy="17.5" r="2.5" fill="currentColor" fill-opacity="0.25"/><circle cx="16.5" cy="15.5" r="2.5" fill="currentColor" fill-opacity="0.25"/>`,
      },
      {
        id: "v4",
        name: "Púa y resonancia",
        desc: "Púa geométrica central con anillos de vibración y compás.",
        art: `
          <svg viewBox="0 0 320 120" aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
            <path d="M160 20 C196 20, 204 50, 160 100 C116 50, 124 20, 160 20 Z" fill="currentColor" fill-opacity="0.18" stroke-width="2.6"/>
            <path d="M144 46 Q160 36, 176 46" stroke-width="2" opacity="0.65"/>
            <path d="M104 34 A62 62 0 0 0 104 86 M216 34 A62 62 0 0 1 216 86" stroke-width="2.2" opacity="0.72"/>
            <path d="M78 22 A86 86 0 0 0 78 98 M242 22 A86 86 0 0 1 242 98" stroke-width="1.8" opacity="0.45"/>
            <path d="M52 14 A110 110 0 0 0 52 106 M268 14 A110 110 0 0 1 268 106" stroke-width="1.4" opacity="0.24"/>
            <circle cx="38" cy="60" r="5" fill="currentColor" stroke="none" opacity="0.5"/>
            <circle cx="282" cy="60" r="5" fill="currentColor" stroke="none" opacity="0.5"/>
          </svg>`,
        logo: `<path d="M12 3.5c5 0 6.5 4.2 0 17-6.5-12.8-5-17 0-17Z" fill="currentColor" fill-opacity="0.2"/><path d="M9.5 8.5a4 4 0 0 1 5 0"/>`,
      },
    ],
  },
};

export function artKeyFor(slugOrType = "") {
  const s = String(slugOrType || "").toLowerCase();
  if (s.includes("mat") || s === "math") return "math";
  if (s.includes("fis") || s === "physics") return "physics";
  if (s.includes("elec") || s === "electronics") return "electronics";
  if (s.includes("guit") || s === "guitar") return "guitar";
  if (s.includes("comp") || s.includes("clyrp") || s === "generic") return "clyrp";
  return "clyrp";
}

function loadPrefs() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}

export function getSelectedVariant(key) {
  const k = artKeyFor(key);
  const entry = ART_GALLERY[k] || ART_GALLERY.clyrp;
  const saved = loadPrefs()[k];
  return entry.options.some((o) => o.id === saved) ? saved : entry.options[0].id;
}

export function setSelectedVariant(key, variantId) {
  const k = artKeyFor(key);
  const entry = ART_GALLERY[k];
  if (!entry || !entry.options.some((o) => o.id === variantId)) return;
  const prefs = loadPrefs();
  prefs[k] = variantId;
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(prefs));
  } catch {
    // ignore private-mode storage errors
  }
}

export function getVariantOption(key) {
  const k = artKeyFor(key);
  const entry = ART_GALLERY[k] || ART_GALLERY.clyrp;
  const id = getSelectedVariant(k);
  return entry.options.find((o) => o.id === id) || entry.options[0];
}

export function subjectArt(slugOrType) {
  return getVariantOption(slugOrType).art;
}

export function subjectLogo(slugOrType, size = 20, cls = "") {
  const body = getVariantOption(slugOrType).logo;
  return `<svg class="ico ${cls}" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${body}</svg>`;
}

/** Backwards-compatible map reading the currently selected artwork for each tone. */
export const ART = new Proxy(
  {},
  {
    get(_, prop) {
      return subjectArt(String(prop));
    },
  }
);
