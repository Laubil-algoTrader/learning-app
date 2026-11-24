/**
 * Verified setup-specific schematic SVG diagrams for Physics & Math exercises and lessons.
 *
 * Exercises are matched STRICTLY by explicit verified exercise ID (never blindly by node slug)
 * so a horizontal-floor problem never shows a ramp, and a pulley-less coupled-blocks problem
 * never shows a pulley. Lessons receive clean conceptual figures via `lessonDiagram(nodeSlug)`.
 */

const SCHEMATICS = {
  horizontalBlock: {
    caption: "Esquema orientativo · Bloque sobre superficie horizontal (N, P = m·g, F y rozamiento fᵣ)",
    svg: `
      <svg viewBox="0 0 360 145" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <line x1="36" y1="104" x2="324" y2="104" stroke-width="2"/>
        <path d="M52 104 l-8 10 M82 104 l-8 10 M112 104 l-8 10 M142 104 l-8 10 M172 104 l-8 10 M202 104 l-8 10 M232 104 l-8 10 M262 104 l-8 10 M292 104 l-8 10" stroke-width="1.2" opacity="0.45"/>
        <rect x="142" y="58" width="76" height="46" rx="5" fill="currentColor" fill-opacity="0.13" stroke-width="2"/>
        <text x="174" y="85" fill="currentColor" stroke="none" font-size="13" font-weight="600">m</text>
        <path d="M180 58 V20 M175 27 l5 -7 l5 7" stroke-width="2"/>
        <text x="190" y="30" fill="currentColor" stroke="none" font-size="12" font-weight="600">N</text>
        <path d="M180 104 V136 M175 129 l5 7 l5 -7" stroke-width="2.2"/>
        <text x="190" y="136" fill="currentColor" stroke="none" font-size="12" font-weight="600">P = m·g</text>
        <path d="M218 81 H292 M285 76 l7 5 l-7 5" stroke-width="2.2"/>
        <text x="262" y="72" fill="currentColor" stroke="none" font-size="12" font-weight="600">F</text>
        <path d="M142 96 H80 M87 91 l-7 5 l7 5" stroke-width="1.8" stroke-dasharray="4 3" opacity="0.8"/>
        <text x="86" y="86" fill="currentColor" stroke="none" font-size="11" opacity="0.85">fᵣ</text>
      </svg>`,
  },
  incline: {
    caption: "Esquema orientativo · Plano inclinado y descomposición de fuerzas",
    svg: `
      <svg viewBox="0 0 360 150" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M40 128 H310 M60 128 H280 V40 Z" stroke-width="1.8"/>
        <path d="M60 128 H280 V40 Z" fill="currentColor" fill-opacity="0.06" stroke="none"/>
        <path d="M104 128 A44 44 0 0 0 100 112" stroke-width="1.4" opacity="0.7"/>
        <text x="110" y="122" fill="currentColor" stroke="none" font-size="12" font-family="var(--font-serif)">α</text>
        <g transform="translate(174 82) rotate(-21.8)">
          <rect x="-24" y="-17" width="48" height="34" rx="4" fill="currentColor" fill-opacity="0.14" stroke-width="2"/>
          <path d="M0 -17 V-54 M-5 -47 l5 -7 l5 7" stroke-width="2"/>
          <text x="8" y="-44" fill="currentColor" stroke="none" font-size="12" font-weight="600">N</text>
          <path d="M24 0 H70 M63 -5 l7 5 l-7 5" stroke-width="2"/>
          <text x="58" y="-10" fill="currentColor" stroke="none" font-size="12" font-weight="600">F / T</text>
          <path d="M-24 0 H-64 M-57 -5 l-7 5 l7 5" stroke-width="1.6" stroke-dasharray="4 3" opacity="0.75"/>
          <text x="-66" y="-9" fill="currentColor" stroke="none" font-size="11" opacity="0.8">fᵣ</text>
        </g>
        <path d="M174 82 V136 M169 129 l5 7 l5 -7" stroke-width="2.2"/>
        <text x="183" y="138" fill="currentColor" stroke="none" font-size="12" font-weight="600">P = m·g</text>
      </svg>`,
  },
  twoBlocksHorizontal: {
    caption: "Esquema orientativo · Bloques vinculados en superficie horizontal (misma aceleración a)",
    svg: `
      <svg viewBox="0 0 360 136" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <line x1="30" y1="100" x2="330" y2="100" stroke-width="2"/>
        <rect x="64" y="60" width="58" height="40" rx="5" fill="currentColor" fill-opacity="0.14" stroke-width="2"/>
        <text x="84" y="84" fill="currentColor" stroke="none" font-size="13" font-weight="600">m₁</text>
        <line x1="122" y1="80" x2="188" y2="80" stroke-width="2"/>
        <text x="150" y="72" fill="currentColor" stroke="none" font-size="12">T</text>
        <rect x="188" y="60" width="58" height="40" rx="5" fill="currentColor" fill-opacity="0.14" stroke-width="2"/>
        <text x="208" y="84" fill="currentColor" stroke="none" font-size="13" font-weight="600">m₂</text>
        <path d="M246 80 H314 M307 75 l7 5 l-7 5" stroke-width="2.2"/>
        <text x="284" y="71" fill="currentColor" stroke="none" font-size="12" font-weight="600">F</text>
        <path d="M140 34 H220 M213 29 l7 5 l-7 5" stroke-width="1.5" stroke-dasharray="4 3" opacity="0.75"/>
        <text x="176" y="27" fill="currentColor" stroke="none" font-size="11" opacity="0.85">a</text>
      </svg>`,
  },
  verticalBlocks: {
    caption: "Esquema orientativo · Cuerpos vinculados en vertical (tracción hacia arriba / peso)",
    svg: `
      <svg viewBox="0 0 360 150" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M180 42 V12 M175 19 l5 -7 l5 7" stroke-width="2.2"/>
        <text x="190" y="24" fill="currentColor" stroke="none" font-size="12" font-weight="600">F / T</text>
        <rect x="154" y="42" width="52" height="30" rx="4" fill="currentColor" fill-opacity="0.15" stroke-width="2"/>
        <text x="171" y="61" fill="currentColor" stroke="none" font-size="12" font-weight="600">m₁</text>
        <line x1="180" y1="72" x2="180" y2="98" stroke-width="2"/>
        <text x="188" y="89" fill="currentColor" stroke="none" font-size="11">T</text>
        <rect x="154" y="98" width="52" height="30" rx="4" fill="currentColor" fill-opacity="0.15" stroke-width="2"/>
        <text x="171" y="117" fill="currentColor" stroke="none" font-size="12" font-weight="600">m₂</text>
        <path d="M180 128 V146 M176 141 l4 5 l4 -5" stroke-width="1.8" opacity="0.8"/>
        <text x="189" y="144" fill="currentColor" stroke="none" font-size="11">P</text>
      </svg>`,
  },
  tablePulley: {
    caption: "Esquema orientativo · Bloque sobre mesa horizontal unido por polea a masa colgante",
    svg: `
      <svg viewBox="0 0 360 150" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <rect x="44" y="64" width="186" height="68" rx="4" fill="currentColor" fill-opacity="0.06" stroke-width="1.8"/>
        <rect x="88" y="34" width="52" height="30" rx="4" fill="currentColor" fill-opacity="0.16" stroke-width="2"/>
        <text x="108" y="54" fill="currentColor" stroke="none" font-size="13" font-weight="600">m₁</text>
        <circle cx="242" cy="52" r="14" fill="currentColor" fill-opacity="0.12" stroke-width="2"/>
        <circle cx="242" cy="52" r="3" fill="currentColor" stroke="none"/>
        <path d="M140 48 H242 M256 52 V92" stroke-width="2"/>
        <rect x="238" y="92" width="36" height="34" rx="4" fill="currentColor" fill-opacity="0.16" stroke-width="2"/>
        <text x="249" y="113" fill="currentColor" stroke="none" font-size="13" font-weight="600">m₂</text>
        <path d="M178 48 H204 M198 44 l6 4 l-6 4" stroke-width="1.6"/>
        <text x="184" y="40" fill="currentColor" stroke="none" font-size="12">T</text>
        <path d="M256 76 V64 M252 70 l4 -6 l4 6" stroke-width="1.6"/>
        <text x="266" y="75" fill="currentColor" stroke="none" font-size="12">T</text>
      </svg>`,
  },
  atwood: {
    caption: "Esquema orientativo · Máquina de Atwood (polea fija en el techo, dos masas colgantes)",
    svg: `
      <svg viewBox="0 0 360 150" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <line x1="120" y1="16" x2="240" y2="16" stroke-width="2"/>
        <line x1="180" y1="16" x2="180" y2="42" stroke-width="2"/>
        <circle cx="180" cy="48" r="16" fill="currentColor" fill-opacity="0.12" stroke-width="2"/>
        <circle cx="180" cy="48" r="3" fill="currentColor" stroke="none"/>
        <line x1="164" y1="48" x2="164" y2="96" stroke-width="2"/>
        <line x1="196" y1="48" x2="196" y2="82" stroke-width="2"/>
        <rect x="144" y="96" width="40" height="34" rx="4" fill="currentColor" fill-opacity="0.16" stroke-width="2"/>
        <text x="156" y="117" fill="currentColor" stroke="none" font-size="12" font-weight="600">m₁</text>
        <rect x="176" y="82" width="40" height="30" rx="4" fill="currentColor" fill-opacity="0.16" stroke-width="2"/>
        <text x="188" y="101" fill="currentColor" stroke="none" font-size="12" font-weight="600">m₂</text>
        <text x="148" y="78" fill="currentColor" stroke="none" font-size="11">T</text>
        <text x="204" y="72" fill="currentColor" stroke="none" font-size="11">T</text>
      </svg>`,
  },
  inclinePulley: {
    caption: "Esquema orientativo · Plano inclinado con polea en la cima y contrapeso",
    svg: `
      <svg viewBox="0 0 360 150" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M40 128 H310 M60 128 H250 V48 Z" stroke-width="1.8"/>
        <path d="M60 128 H250 V48 Z" fill="currentColor" fill-opacity="0.06" stroke="none"/>
        <circle cx="258" cy="44" r="12" fill="currentColor" fill-opacity="0.12" stroke-width="2"/>
        <circle cx="258" cy="44" r="2.5" fill="currentColor" stroke="none"/>
        <g transform="translate(158 84) rotate(-22.8)">
          <rect x="-22" y="-14" width="44" height="28" rx="4" fill="currentColor" fill-opacity="0.16" stroke-width="2"/>
          <text x="-8" y="4" fill="currentColor" stroke="none" font-size="11" font-weight="600">m₁</text>
        </g>
        <line x1="178" y1="74" x2="250" y2="42" stroke-width="2"/>
        <line x1="270" y1="44" x2="270" y2="86" stroke-width="2"/>
        <rect x="254" y="86" width="32" height="30" rx="4" fill="currentColor" fill-opacity="0.16" stroke-width="2"/>
        <text x="262" y="105" fill="currentColor" stroke="none" font-size="11" font-weight="600">m₂</text>
      </svg>`,
  },
  hangingRopes: {
    caption: "Esquema orientativo · Cuerpo en equilibrio suspendido de un nudo (∑Fₓ = 0, ∑Fᵧ = 0)",
    svg: `
      <svg viewBox="0 0 360 145" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <line x1="60" y1="20" x2="300" y2="20" stroke-width="2"/>
        <line x1="104" y1="20" x2="180" y2="74" stroke-width="2"/>
        <line x1="256" y1="20" x2="180" y2="74" stroke-width="2"/>
        <circle cx="180" cy="74" r="4" fill="currentColor" stroke="none"/>
        <line x1="180" y1="74" x2="180" y2="96" stroke-width="2"/>
        <rect x="160" y="96" width="40" height="32" rx="4" fill="currentColor" fill-opacity="0.16" stroke-width="2"/>
        <text x="174" y="116" fill="currentColor" stroke="none" font-size="12" font-weight="600">P</text>
        <text x="116" y="60" fill="currentColor" stroke="none" font-size="12" font-weight="600">T₁</text>
        <text x="228" y="60" fill="currentColor" stroke="none" font-size="12" font-weight="600">T₂</text>
        <line x1="130" y1="74" x2="230" y2="74" stroke-width="1.2" stroke-dasharray="4 3" opacity="0.5"/>
      </svg>`,
  },
  beam: {
    caption: "Esquema orientativo · Barra rígida horizontal y reacciones de vínculo (∑F = 0, ∑M = 0)",
    svg: `
      <svg viewBox="0 0 360 140" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <rect x="64" y="64" width="232" height="12" rx="3" fill="currentColor" fill-opacity="0.14" stroke-width="2"/>
        <polygon points="78,76 64,104 92,104" fill="currentColor" fill-opacity="0.12" stroke-width="1.8"/>
        <line x1="56" y1="104" x2="100" y2="104" stroke-width="1.8"/>
        <polygon points="280,76 268,98 292,98" fill="currentColor" fill-opacity="0.08" stroke-width="1.8"/>
        <circle cx="274" cy="103" r="4" stroke-width="1.5"/>
        <circle cx="286" cy="103" r="4" stroke-width="1.5"/>
        <line x1="260" y1="108" x2="300" y2="108" stroke-width="1.8"/>
        <path d="M168 22 V62 M163 55 l5 7 l5 -7" stroke-width="2.2"/>
        <text x="178" y="38" fill="currentColor" stroke="none" font-size="12" font-weight="600">F / P</text>
        <path d="M78 124 V108 M73 114 l5 -6 l5 6" stroke-width="1.8" opacity="0.8"/>
        <text x="86" y="124" fill="currentColor" stroke="none" font-size="11">R<tspan dy="2" font-size="8.5">A</tspan></text>
        <path d="M280 124 V111 M275 117 l5 -6 l5 6" stroke-width="1.8" opacity="0.8"/>
        <text x="290" y="124" fill="currentColor" stroke="none" font-size="11">R<tspan dy="2" font-size="8.5">B</tspan></text>
      </svg>`,
  },
  vertical: {
    caption: "Esquema orientativo · Caída libre / tiro vertical (g hacia abajo)",
    svg: `
      <svg viewBox="0 0 360 145" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <line x1="36" y1="126" x2="324" y2="126" stroke-width="1.8"/>
        <rect x="64" y="62" width="54" height="64" fill="currentColor" fill-opacity="0.1" stroke-width="1.8"/>
        <path d="M130 62 C130 16, 210 16, 210 126" stroke-width="2" stroke-dasharray="5 5"/>
        <circle cx="170" cy="27" r="6" fill="currentColor" stroke="none"/>
        <text x="182" y="29" fill="currentColor" stroke="none" font-size="11">v = 0 (hₘₐₓ)</text>
        <path d="M130 62 V38 M125 45 l5 -7 l5 7" stroke-width="2"/>
        <text x="139" y="52" fill="currentColor" stroke="none" font-size="11">v₀</text>
        <path d="M276 34 V74 M271 67 l5 7 l5 -7" stroke-width="2.2"/>
        <text x="286" y="58" fill="currentColor" stroke="none" font-size="12" font-weight="600">g</text>
      </svg>`,
  },
  vectors: {
    caption: "Esquema orientativo · Descomposición vectorial (vₓ = v·cos θ, vᵧ = v·sen θ)",
    svg: `
      <svg viewBox="0 0 360 145" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M56 116 H308 M301 112 l7 4 l-7 4" stroke-width="1.5" opacity="0.6"/>
        <path d="M110 132 V18 M106 25 l4 -7 l4 7" stroke-width="1.5" opacity="0.6"/>
        <path d="M110 116 L246 42 M235 41 l11 1 l-5 10" stroke-width="2.6"/>
        <path d="M246 42 V116 M110 42 H246" stroke-width="1.3" stroke-dasharray="4 4" opacity="0.55"/>
        <path d="M110 116 H244 M237 112 l7 4 l-7 4" stroke-width="1.8" opacity="0.8"/>
        <path d="M110 116 V44 M106 51 l4 -7 l4 7" stroke-width="1.8" opacity="0.8"/>
        <path d="M152 116 A42 42 0 0 0 147 96" stroke-width="1.5"/>
        <text x="157" y="108" fill="currentColor" stroke="none" font-size="12" font-family="var(--font-serif)">θ</text>
        <text x="176" y="68" fill="currentColor" stroke="none" font-size="13" font-weight="600">R</text>
        <text x="180" y="132" fill="currentColor" stroke="none" font-size="11">Rₓ</text>
        <text x="86" y="78" fill="currentColor" stroke="none" font-size="11">Rᵧ</text>
      </svg>`,
  },
  rightTriangle: {
    caption: "Esquema orientativo · Triángulo rectángulo (sen, cos y tg)",
    svg: `
      <svg viewBox="0 0 360 140" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M68 114 H284 V30 Z" fill="currentColor" fill-opacity="0.08" stroke-width="2.2"/>
        <path d="M270 114 V100 H284" stroke-width="1.5"/>
        <path d="M112 114 A44 44 0 0 0 108 98" stroke-width="1.6"/>
        <text x="118" y="108" fill="currentColor" stroke="none" font-size="12" font-family="var(--font-serif)">α</text>
        <text x="166" y="130" fill="currentColor" stroke="none" font-size="11">cateto adyacente</text>
        <text x="292" y="76" fill="currentColor" stroke="none" font-size="11">h</text>
        <text x="148" y="64" fill="currentColor" stroke="none" font-size="11">hipotenusa</text>
      </svg>`,
  },
  doubleAngle: {
    caption: "Esquema orientativo · Dos visuales con dos ángulos (sistema de dos triángulos rectángulos)",
    svg: `
      <svg viewBox="0 0 360 142" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <line x1="36" y1="118" x2="320" y2="118" stroke-width="1.8"/>
        <line x1="278" y1="118" x2="278" y2="24" stroke-width="2.4"/>
        <path d="M266 118 V106 H278" stroke-width="1.4"/>
        <line x1="68" y1="118" x2="278" y2="24" stroke-width="1.8"/>
        <line x1="168" y1="118" x2="278" y2="24" stroke-width="1.8" stroke-dasharray="5 3"/>
        <text x="108" y="112" fill="currentColor" stroke="none" font-size="12" font-family="var(--font-serif)">α</text>
        <text x="196" y="112" fill="currentColor" stroke="none" font-size="12" font-family="var(--font-serif)">β</text>
        <text x="288" y="74" fill="currentColor" stroke="none" font-size="12" font-weight="600">h</text>
        <text x="112" y="133" fill="currentColor" stroke="none" font-size="11">d</text>
        <text x="218" y="133" fill="currentColor" stroke="none" font-size="11">x</text>
      </svg>`,
  },
  circle: {
    caption: "Esquema orientativo · Circunferencia (x − h)² + (y − k)² = r²",
    svg: `
      <svg viewBox="0 0 360 140" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M54 110 H306 M124 128 V14" stroke-width="1.3" opacity="0.45"/>
        <circle cx="196" cy="64" r="42" fill="currentColor" fill-opacity="0.08" stroke-width="2.2"/>
        <circle cx="196" cy="64" r="4" fill="currentColor" stroke="none"/>
        <line x1="196" y1="64" x2="232" y2="42" stroke-width="2"/>
        <path d="M196 64 V110 M124 64 H196" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.55"/>
        <text x="214" y="47" fill="currentColor" stroke="none" font-size="12" font-weight="600">r</text>
        <text x="164" y="58" fill="currentColor" stroke="none" font-size="11">C(h; k)</text>
      </svg>`,
  },
  venn3: {
    caption: "Esquema orientativo · Diagrama de Venn de tres conjuntos (A, B, C en U)",
    svg: `
      <svg viewBox="0 0 360 148" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <rect x="64" y="12" width="232" height="124" rx="8" stroke-width="1.5" opacity="0.5"/>
        <text x="74" y="28" fill="currentColor" stroke="none" font-size="12" font-weight="600">U</text>
        <circle cx="154" cy="62" r="34" fill="currentColor" fill-opacity="0.08" stroke-width="2"/>
        <circle cx="206" cy="62" r="34" fill="currentColor" fill-opacity="0.08" stroke-width="2"/>
        <circle cx="180" cy="96" r="34" fill="currentColor" fill-opacity="0.08" stroke-width="2"/>
        <text x="132" y="56" fill="currentColor" stroke="none" font-size="12" font-weight="600">A</text>
        <text x="222" y="56" fill="currentColor" stroke="none" font-size="12" font-weight="600">B</text>
        <text x="176" y="118" fill="currentColor" stroke="none" font-size="12" font-weight="600">C</text>
      </svg>`,
  },
};

/**
 * Explicit, audited per-exercise diagram assignments.
 * Every ID listed below was checked against its actual problem statement.
 */
const EXERCISE_DIAGRAM_MAP = {
  // Horizontal surface with friction (NO ramp)
  "f-dcl-rozamiento-plano-1": "horizontalBlock",
  "f-dcl-rozamiento-plano-2": "horizontalBlock",
  "f-dcl-rozamiento-plano-tp5b-1b": "horizontalBlock",
  "f-dcl-rozamiento-plano-tp5b-1f": "horizontalBlock",
  "f-dcl-rozamiento-plano-tp5b-2e": "horizontalBlock",

  // True inclined planes
  "f-dcl-rozamiento-plano-3": "incline",
  "f-dcl-rozamiento-plano-4": "incline",
  "f-dcl-rozamiento-plano-u5-4": "incline",
  "f-dcl-rozamiento-plano-u5-9": "incline",
  "f-dcl-rozamiento-plano-u5-10": "incline",
  "f-estatica-concurrentes-tp41b-2": "incline",
  "f-estatica-concurrentes-tp41b-5c": "incline",

  // Coupled bodies on horizontal surface (NO pulley)
  "f-cuerpos-vinculados-1": "twoBlocksHorizontal",
  "f-cuerpos-vinculados-u5-1": "twoBlocksHorizontal",
  "f-cuerpos-vinculados-u5-2": "twoBlocksHorizontal",
  "f-cuerpos-vinculados-u5-7": "twoBlocksHorizontal",
  "f-cuerpos-vinculados-tp5b-2d": "twoBlocksHorizontal",

  // Coupled bodies hanging vertically (NO pulley)
  "f-cuerpos-vinculados-u5-3": "verticalBlocks",
  "f-cuerpos-vinculados-tp5b-2f": "verticalBlocks",

  // Table + edge pulley + hanging mass
  "f-cuerpos-vinculados-2": "tablePulley",
  "f-cuerpos-vinculados-u5-8": "tablePulley",
  "f-cuerpos-vinculados-tp5b-2h": "tablePulley",

  // Ceiling pulley (Atwood machine)
  "f-cuerpos-vinculados-3": "atwood",

  // Inclined plane + pulley + counterweight
  "f-cuerpos-vinculados-4": "inclinePulley",

  // Hanging weight from knot & angled cords
  "f-estatica-concurrentes-u4-4a": "hangingRopes",
  "f-estatica-concurrentes-u4-4b": "hangingRopes",
  "f-estatica-concurrentes-tp41b-4b": "hangingRopes",
  "f-estatica-concurrentes-tp41b-4c": "hangingRopes",
  "f-estatica-concurrentes-tp41b-7": "hangingRopes",
  "f-estatica-concurrentes-vallone-10": "hangingRopes",

  // Rigid horizontal beams & reactions
  "f-momento-cupla-vinculos-u4-7": "beam",
  "f-momento-cupla-vinculos-vallone-12": "beam",
  "f-momento-cupla-vinculos-vallone-13": "beam",
  "f-momento-cupla-vinculos-apuntes-cupla": "beam",

  // Free fall & vertical throw
  "f-caida-libre-tiro-vertical-1": "vertical",
  "f-caida-libre-tiro-vertical-2": "vertical",
  "f-caida-libre-tiro-vertical-3": "vertical",
  "f-caida-libre-tiro-vertical-4": "vertical",
  "f-caida-libre-tiro-vertical-u3-17": "vertical",
  "f-caida-libre-tiro-vertical-u3-18": "vertical",
  "f-caida-libre-tiro-vertical-u3-20": "vertical",
  "f-caida-libre-tiro-vertical-tp3b2-2a": "vertical",
  "f-caida-libre-tiro-vertical-tp3b2-2g": "vertical",

  // Vector decomposition
  "f-vectores-operaciones-1": "vectors",
  "f-vectores-operaciones-u2-4": "vectors",
  "f-vectores-operaciones-u2-5-1": "vectors",
  "f-vectores-operaciones-u2-6a": "vectors",
  "f-vectores-operaciones-u2-6b": "vectors",
  "f-vectores-operaciones-u2-6c": "vectors",
  "f-vectores-operaciones-u2-7": "vectors",
  "f-vectores-operaciones-tp2b-10": "vectors",

  // Right triangle (single angle)
  "g-trigonometria-1": "rightTriangle",
  "g-trigonometria-2": "rightTriangle",
  "g-trigonometria-tp2-58": "rightTriangle",
  "g-trigonometria-tp2-62": "rightTriangle",

  // Two-angle sightline problems
  "g-trigonometria-3": "doubleAngle",
  "g-trigonometria-tp2-61": "doubleAngle",
  "g-trigonometria-tp2-63": "doubleAngle",
  "g-trigonometria-tp2-64": "doubleAngle",
  "g-trigonometria-tp2-65": "doubleAngle",
  "g-trigonometria-tp2-66": "doubleAngle",
  "g-trigonometria-tp3-48": "doubleAngle",
  "g-trigonometria-tp3-49": "doubleAngle",

  // Circle equation
  "g-ecuacion-circulo-1": "circle",
  "g-ecuacion-circulo-2": "circle",
  "g-ecuacion-circulo-3": "circle",
  "g-ecuacion-circulo-tp4-28": "circle",

  // 3-set Venn diagram (tp0-5 has 4 custom sets P,Q,S,R so intentionally excluded)
  "al-teoria-conjuntos-tp0-6": "venn3",
  "al-teoria-conjuntos-tp0-7": "venn3",
};

const LESSON_DIAGRAM_MAP = {
  "f-dcl-rozamiento-plano": "incline",
  "f-cuerpos-vinculados": "tablePulley",
  "f-estatica-concurrentes": "hangingRopes",
  "f-momento-cupla-vinculos": "beam",
  "f-caida-libre-tiro-vertical": "vertical",
  "f-vectores-operaciones": "vectors",
  "g-trigonometria": "rightTriangle",
  "g-ecuacion-circulo": "circle",
  "al-teoria-conjuntos": "venn3",
};

function renderFigure(key, labelOverride = "") {
  const s = SCHEMATICS[key];
  if (!s) return "";
  return `
    <figure class="ex-diagram m-0">
      ${s.svg}
      <figcaption class="xs muted">${labelOverride || s.caption}</figcaption>
    </figure>`;
}

export function exerciseDiagram(ex) {
  if (!ex || ex.kind !== "problem") return "";
  const key = EXERCISE_DIAGRAM_MAP[ex.id];
  return key ? renderFigure(key) : "";
}

export function lessonDiagram(nodeSlug) {
  const key = LESSON_DIAGRAM_MAP[String(nodeSlug || "")];
  return key ? renderFigure(key) : "";
}
