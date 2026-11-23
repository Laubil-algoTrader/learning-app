/**
 * Minimal 1.5px stroke monochrome SVG icon set (zero emojis).
 * Automatically maps legacy emoji icons stored in SQLite to clean vector glyphs.
 */

const ICON_PATHS = {
  home: `<path d="M3 10.5 12 3l9 7.5"/><path d="M5.5 9.5V20h13V9.5"/>`,
  layers: `<path d="m12 3 9 4.5-9 4.5-9-4.5L12 3Z"/><path d="m3 12 9 4.5 9-4.5"/><path d="m3 16.5 9 4.5 9-4.5"/>`,
  brain: `<path d="M9.5 4a3 3 0 0 0-3 3c-1.7.4-3 1.9-3 3.7a3.8 3.8 0 0 0 1.3 2.9 3.2 3.2 0 0 0 2.7 4.9h2V4Z"/><path d="M14.5 4a3 3 0 0 1 3 3c1.7.4 3 1.9 3 3.7a3.8 3.8 0 0 1-1.3 2.9 3.2 3.2 0 0 1-2.7 4.9h-2V4Z"/>`,
  guitar: `<path d="m19 5-4.5 4.5"/><path d="m17 3 4 4"/><path d="M14.5 9.5c-1.4-1.4-3.7-1.2-4.8.4-.7 1-.6 2.3-1.4 3.1-1.3 1.3-3.5 1.4-4.5 3.1-1 1.7-.4 4 1.3 5 1.7 1 4 .4 5-1.3 1-1.6 1.1-3.2 2.4-4.5.8-.8 2.1-.7 3.1-1.4 1.6-1.1 1.8-3.4.4-4.8Z"/><circle cx="9.2" cy="15.2" r="1.1"/>`,
  music: `<path d="M9 18V6l11-2v12"/><circle cx="6.5" cy="18" r="2.5"/><circle cx="17.5" cy="16" r="2.5"/>`,
  electronics: `<rect x="6" y="6" width="12" height="12" rx="2"/><rect x="9.5" y="9.5" width="5" height="5" rx="0.5"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>`,
  math: `<path d="M4 19 20 5"/><path d="M4 7h6M7 4v6"/><path d="M14 17h6"/><path d="M14 20h6"/>`,
  physics: `<circle cx="12" cy="12" r="2.2" fill="currentColor"/><ellipse cx="12" cy="12" rx="9.5" ry="4" transform="rotate(30 12 12)"/><ellipse cx="12" cy="12" rx="9.5" ry="4" transform="rotate(-30 12 12)"/><ellipse cx="12" cy="12" rx="9.5" ry="4" transform="rotate(90 12 12)"/>`,
  bookOpen: `<path d="M2 5.5A2.5 2.5 0 0 1 4.5 3H10a3 3 0 0 1 2 1 3 3 0 0 1 2-1h5.5A2.5 2.5 0 0 1 22 5.5V19a1.5 1.5 0 0 1-1.5 1.5H14a2 2 0 0 0-2 1.5 2 2 0 0 0-2-1.5H3.5A1.5 1.5 0 0 1 2 19V5.5Z"/><path d="M12 4v17.5"/>`,
  compass: `<circle cx="12" cy="12" r="9"/><polygon points="15.5 8.5 13.5 13.5 8.5 15.5 10.5 10.5 15.5 8.5"/>`,
  book: `<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v17H6.5A2.5 2.5 0 0 0 4 22V5.5Z"/><path d="M8 7h8M8 11h6"/>`,
  code: `<path d="m8 8-4 4 4 4"/><path d="m16 8 4 4-4 4"/><path d="m14 5-4 14"/>`,
  globe: `<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>`,
  pen: `<path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/>`,
  zap: `<path d="M13 2 4 14h7l-1 8 9-12h-7l1-8Z"/>`,
  play: `<polygon points="7 5 19 12 7 19 7 5"/>`,
  pause: `<rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/>`,
  stop: `<rect x="6" y="6" width="12" height="12" rx="1.5"/>`,
  check: `<path d="m5 12.5 4.5 4.5L19 7.5"/>`,
  x: `<path d="M6 6l12 12M18 6 6 18"/>`,
  arrowRight: `<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>`,
  arrowUpRight: `<path d="M7 17 17 7"/><path d="M8 7h9v9"/>`,
  plus: `<path d="M12 5v14M5 12h14"/>`,
  sliders: `<path d="M4 7h16M4 17h16"/><circle cx="9" cy="7" r="2.2" fill="var(--bg)"/><circle cx="15" cy="17" r="2.2" fill="var(--bg)"/>`,
  activity: `<path d="M3 12h4l2.5-7 5 14 2.5-7h4"/>`,
  sun: `<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>`,
  moon: `<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/>`,
  download: `<path d="M12 3v12"/><path d="m7 11 5 5 5-5"/><path d="M4 19h16"/>`,
  upload: `<path d="M12 16V4"/><path d="m7 9 5-5 5 5"/><path d="M4 19h16"/>`,
  lock: `<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>`,
  unlock: `<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V7a4 4 0 0 1 7.4-2"/>`,
  volume: `<path d="M5 9v6h4l5 4V5l-5 4H5Z"/><path d="M17.5 8.5a5 5 0 0 1 0 7"/>`,
  shuffle: `<path d="M16 4h4v4"/><path d="m4 20 16-16"/><path d="M16 20h4v-4"/><path d="m14 14 6 6"/><path d="m4 4 6 6"/>`,
  refresh: `<path d="M20 11a8 8 0 1 0 2 5.3"/><path d="M20 4v7h-7"/>`,
  target: `<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>`,
  clock: `<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>`,
  bug: `<rect x="8" y="8" width="8" height="10" rx="4"/><path d="M9.5 8V6a2.5 2.5 0 0 1 5 0v2M4 11h4M16 11h4M4 15h4M16 15h4M5.5 7 8 9M18.5 7 16 9"/>`,
  eye: `<path d="M2 12s3.8-6.5 10-6.5S22 12 22 12s-3.8 6.5-10 6.5S2 12 2 12Z"/><circle cx="12" cy="12" r="2.8"/>`,
  trash: `<path d="M4 7h16"/><path d="M9 7V4h6v3"/><path d="M6 7l1 13h10l1-13"/>`,
  alert: `<path d="M12 3 2.5 19.5h19L12 3Z"/><path d="M12 9.5v4.5"/><circle cx="12" cy="16.8" r="0.7" fill="currentColor"/>`,
  flask: `<path d="M9 3h6M10 3v5.5L4.8 18.2A2 2 0 0 0 6.5 21h11a2 2 0 0 0 1.7-2.8L14 8.5V3"/><path d="M7.5 15h9"/>`,
  map: `<path d="M3 6.5 9 4l6 2.5L21 4v13.5L15 20l-6-2.5L3 20V6.5Z"/><path d="M9 4v13.5M15 6.5V20"/>`,
  search: `<circle cx="11" cy="11" r="7"/><path d="m20 20-3.8-3.8"/>`,
  grid: `<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>`,
  more: `<circle cx="5" cy="12" r="1.4" fill="currentColor"/><circle cx="12" cy="12" r="1.4" fill="currentColor"/><circle cx="19" cy="12" r="1.4" fill="currentColor"/>`,
  settings: `<path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12M20 18h0"/><circle cx="16" cy="6" r="2"/><circle cx="10" cy="12" r="2"/><circle cx="18" cy="18" r="2"/>`,
  arrowUp: `<path d="M12 19V5"/><path d="m6 11 6-6 6 6"/>`,
  arrowDown: `<path d="M12 5v14"/><path d="m6 13 6 6 6-6"/>`,
  arrowLeft: `<path d="M19 12H5"/><path d="m11 6-6 6 6 6"/>`,
  mic: `<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5.5 11a6.5 6.5 0 0 0 13 0"/><path d="M12 17.5V21"/>`,
  flame: `<path d="M12 3c1 3.5 5 5.5 5 10a5 5 0 0 1-10 0c0-1.8.7-3 1.7-4 .3 1.5 1.3 2.3 2.3 2.3C11.5 8.5 10.5 6 12 3Z"/>`,
  help: `<circle cx="12" cy="12" r="9"/><path d="M9.5 9.2a2.6 2.6 0 0 1 5 .8c0 1.8-2.5 2.2-2.5 3.8"/><circle cx="12" cy="17" r="0.6" fill="currentColor"/>`,
};

const EMOJI_OR_KEY_MAP = {
  "🎸": "guitar",
  "⚡": "electronics",
  "📐": "math",
  "📘": "book",
  "🗣️": "globe",
  "✏️": "pen",
  "💻": "code",
  "🎵": "music",
  guitar: "guitar",
  guitarra: "guitar",
  electronics: "electronics",
  electronica: "electronics",
  cpu: "electronics",
  math: "math",
  matematicas: "math",
  physics: "physics",
  fisica: "physics",
  book: "book",
  code: "code",
  globe: "globe",
  pen: "pen",
  music: "music",
  layers: "layers",
  compass: "compass",
  flask: "flask",
};

export function resolveDomainIcon(raw, labType = "") {
  if (raw && EMOJI_OR_KEY_MAP[raw]) return EMOJI_OR_KEY_MAP[raw];
  if (labType === "guitar") return "guitar";
  if (labType === "electronics") return "electronics";
  if (labType === "math") return "math";
  if (labType === "physics") return "physics";
  return "book";
}

export function icon(name, size = 16, cls = "") {
  const key = ICON_PATHS[name] ? name : EMOJI_OR_KEY_MAP[name] || "book";
  const body = ICON_PATHS[key] || ICON_PATHS.book;
  return `<svg class="ico ${cls}" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${body}</svg>`;
}

export const DOMAIN_ICON_CHOICES = [
  { key: "book", label: "Libro / General" },
  { key: "guitar", label: "Instrumento / Música" },
  { key: "electronics", label: "Electrónica / Hardware" },
  { key: "math", label: "Matemáticas / Ciencias" },
  { key: "physics", label: "Física / Fenómenos" },
  { key: "code", label: "Programación / Código" },
  { key: "globe", label: "Idiomas / Cultura" },
  { key: "pen", label: "Diseño / Dibujo / Escritura" },
  { key: "compass", label: "Estrategia / Exploración" },
  { key: "layers", label: "Arquitectura / Sistemas" },
];
