import { icon } from "../icons.js";
import { api, esc, registerCleanup, toast } from "../main.js";

const CHORDS = {
  Em: { name: "Mi menor (Em)", frets: [0, 2, 2, 0, 0, 0], fingers: ["", "2", "3", "", "", ""], tip: "Rasgueá las 6 cuerdas. Mantené dedos 2 y 3 cerca de la varilla del traste 2." },
  Am: { name: "La menor (Am)", frets: [-1, 0, 2, 2, 1, 0], fingers: ["", "", "2", "3", "1", ""], tip: "No rasguees la 6ª cuerda. Arqueá el dedo 1 para no apagar la 1ª cuerda." },
  E: { name: "Mi mayor (E)", frets: [0, 2, 2, 1, 0, 0], fingers: ["", "2", "3", "1", "", ""], tip: "Igual que Em, agregando el dedo 1 en 3ª cuerda traste 1." },
  A: { name: "La mayor (A)", frets: [-1, 0, 2, 2, 2, 0], fingers: ["", "", "2", "1", "3", ""], tip: "Digitación moderna (2-1-3): el dedo 1 queda en 3ª cuerda como ancla para D y E." },
  D: { name: "Re mayor (D)", frets: [-1, -1, 0, 2, 3, 2], fingers: ["", "", "", "1", "3", "2"], tip: "Rasgueá desde la 4ª cuerda. Cuidá que el dedo 3 no roce la 1ª cuerda." },
  G: { name: "Sol mayor (G)", frets: [3, 2, 0, 0, 0, 3], fingers: ["2", "1", "", "", "", "3"], tip: "También podés usar 3-2-4 para cambiar más rápido hacia C." },
  C: { name: "Do mayor (C)", frets: [-1, 3, 2, 0, 1, 0], fingers: ["", "3", "2", "", "1", ""], tip: "Desde la 5ª cuerda. Bajá levemente el pulgar detrás del mástil para liberar la 1ª cuerda." },
  Dm: { name: "Re menor (Dm)", frets: [-1, -1, 0, 2, 3, 1], fingers: ["", "", "", "2", "3", "1"], tip: "Rasgueá desde la 4ª cuerda." },
  Fmaj7: { name: "Fa mayor 7 (Fmaj7)", frets: [-1, -1, 3, 2, 1, 0], fingers: ["", "", "3", "2", "1", ""], tip: "Gran puente antes de la cejilla de Fa. Rasgueá desde la 4ª cuerda." },
};

const STRINGS = [
  { num: 6, note: "E2 — Mi grave", openSemi: 4, freq: 82.41 },
  { num: 5, note: "A2 — La", openSemi: 9, freq: 110.0 },
  { num: 4, note: "D3 — Re", openSemi: 2, freq: 146.83 },
  { num: 3, note: "G3 — Sol", openSemi: 7, freq: 196.0 },
  { num: 2, note: "B3 — Si", openSemi: 11, freq: 246.94 },
  { num: 1, note: "E4 — Mi agudo", openSemi: 4, freq: 329.63 },
];

const NOTE_NAMES = [
  { en: "C", es: "Do", nat: true },
  { en: "C#", es: "Do#", nat: false },
  { en: "D", es: "Re", nat: true },
  { en: "D#", es: "Re#", nat: false },
  { en: "E", es: "Mi", nat: true },
  { en: "F", es: "Fa", nat: true },
  { en: "F#", es: "Fa#", nat: false },
  { en: "G", es: "Sol", nat: true },
  { en: "G#", es: "Sol#", nat: false },
  { en: "A", es: "La", nat: true },
  { en: "A#", es: "La#", nat: false },
  { en: "B", es: "Si", nat: true },
];

const PROGRESSIONS = {
  none: { label: "Solo pulso", chords: [], pattern: "↓   ↓   ↓   ↓" },
  pop: { label: "I–V–vi–IV (G - D - Em - C)", chords: ["G", "D", "Em", "C"], pattern: "↓   ↓ ↑   ↑ ↓ ↑" },
  starter: { label: "Inicio (Em - Am - D - G)", chords: ["Em", "Am", "D", "G"], pattern: "↓   ↓   ↓ ↑ ↓ ↑" },
  triad: { label: "Tríada (D - A - E - A)", chords: ["D", "A", "E", "A"], pattern: "↓   ↓ ↑   ↓ ↑" },
};

const MOTOR_VARIATIONS = [
  "Acentuá claramente los tiempos 2 y 4 manteniendo el resto suave (control dinámico).",
  "Tocá 2 compases mirando un punto fijo lejos del mástil para activar tu propiocepción.",
  "Alterná un compás rasgueando muy suave (piano) y el siguiente firme (mezzo-forte).",
  "Hacé un arpegio lento cuerda por cuerda en el tiempo 1 para detectar trasteos ocultos.",
  "Bajá 10 BPM y exagerá la relajación de hombros y muñeca entre cada cambio.",
  "Cambiá de acorde en silencio durante el último 'y' del compás sin frenar la mano derecha.",
];

const FRET_OVERLAYS = {
  am_box1: {
    label: "Pentatónica Am (Caja 1 · Traste 5)",
    rootSemi: 9,
    positions: { 0: [5, 8], 1: [5, 8], 2: [5, 7], 3: [5, 7], 4: [5, 7], 5: [5, 8] },
  },
  em_open: {
    label: "Pentatónica Em (Posición abierta)",
    rootSemi: 4,
    positions: { 0: [0, 3], 1: [0, 3], 2: [0, 2], 3: [0, 2], 4: [0, 2], 5: [0, 3] },
  },
  naturals: {
    label: "Notas naturales (sin sostenidos)",
    rootSemi: -1,
    positions: null,
  },
};

function renderSparklineSVG(values, unit) {
  if (!values || values.length < 2) return "";
  const ordered = [...values].reverse();
  const w = 260;
  const h = 54;
  const pad = 8;
  const min = Math.min(...ordered);
  const max = Math.max(...ordered);
  const span = Math.max(1, max - min);
  const pts = ordered.map((v, i) => {
    const x = pad + (i / (ordered.length - 1)) * (w - pad * 2);
    const y = h - pad - ((v - min) / span) * (h - pad * 2);
    return [x, y, v];
  });
  const path = pts.map(([x, y], i) => `${i === 0 ? "M" : "L"}${x.toFixed(1)},${y.toFixed(1)}`).join(" ");
  return `
    <svg viewBox="0 0 ${w} ${h}" width="100%" height="${h}" aria-label="Tendencia de ${esc(unit)}">
      <path d="${path}" fill="none" stroke="var(--accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
      ${pts.map(([x, y, v]) => `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="3.2" fill="var(--bg-inverse)"><title>${v} ${esc(unit)}</title></circle>`).join("")}
    </svg>`;
}

/**
 * Fundamental frequency of a time-domain buffer by autocorrelation with
 * parabolic interpolation. Returns null when the signal is too quiet.
 */
export function detectPitch(input, sampleRate) {
  let size = input.length;
  let rms = 0;
  for (let i = 0; i < size; i++) rms += input[i] * input[i];
  if (Math.sqrt(rms / size) < 0.012) return null;

  let r1 = 0;
  let r2 = size - 1;
  const thres = 0.2;
  for (let i = 0; i < size / 2; i++) {
    if (Math.abs(input[i]) < thres) { r1 = i; break; }
  }
  for (let i = 1; i < size / 2; i++) {
    if (Math.abs(input[size - i]) < thres) { r2 = size - i; break; }
  }
  const buf = input.slice(r1, r2);
  size = buf.length;
  if (size < 512) return null;

  const maxLag = Math.min(size - 1, Math.floor(sampleRate / 55));
  const c = new Float32Array(maxLag + 2);
  for (let lag = 0; lag <= maxLag + 1 && lag < size; lag++) {
    let sum = 0;
    for (let j = 0; j < size - lag; j++) sum += buf[j] * buf[j + lag];
    c[lag] = sum;
  }
  let d = 0;
  while (d < maxLag && c[d] > c[d + 1]) d++;
  let maxval = -1;
  let maxpos = -1;
  for (let i = d; i <= maxLag; i++) {
    if (c[i] > maxval) { maxval = c[i]; maxpos = i; }
  }
  if (maxpos <= 0 || maxval < c[0] * 0.3) return null;
  let t0 = maxpos;
  const x1 = c[t0 - 1];
  const x2 = c[t0];
  const x3 = c[t0 + 1];
  const a = (x1 + x3 - 2 * x2) / 2;
  const b = (x3 - x1) / 2;
  if (a) t0 -= b / (2 * a);
  return sampleRate / t0;
}

export function renderChordSVG(code) {
  const c = CHORDS[code];
  if (!c) return "";
  const w = 156;
  const h = 178;
  const left = 24;
  const top = 34;
  const strGap = 21;
  const fretGap = 27;

  let svg = `<svg viewBox="0 0 ${w} ${h}" width="${w}" height="${h}" role="img" aria-label="Diagrama de ${esc(c.name)}">`;
  svg += `<text x="${w / 2}" y="16" text-anchor="middle" fill="currentColor" font-weight="600" font-size="14">${esc(code)}</text>`;
  svg += `<line x1="${left}" y1="${top}" x2="${left + strGap * 5}" y2="${top}" stroke="currentColor" stroke-width="3.5" />`;
  for (let f = 1; f <= 4; f++) {
    const y = top + f * fretGap;
    svg += `<line x1="${left}" y1="${y}" x2="${left + strGap * 5}" y2="${y}" stroke="currentColor" stroke-opacity="0.28" stroke-width="1.3" />`;
  }
  for (let s = 0; s < 6; s++) {
    const x = left + s * strGap;
    svg += `<line x1="${x}" y1="${top}" x2="${x}" y2="${top + fretGap * 4}" stroke="currentColor" stroke-opacity="0.45" stroke-width="${1.7 - s * 0.13}" />`;
    const fret = c.frets[s];
    if (fret === -1) {
      svg += `<text x="${x}" y="${top - 8}" text-anchor="middle" fill="var(--danger)" font-size="11" font-weight="700">x</text>`;
    } else if (fret === 0) {
      svg += `<circle cx="${x}" cy="${top - 10}" r="4" fill="none" stroke="var(--accent)" stroke-width="1.6" />`;
    } else {
      const cy = top + (fret - 0.5) * fretGap;
      svg += `<circle cx="${x}" cy="${cy}" r="8.5" fill="var(--accent)" />`;
      if (c.fingers[s]) {
        svg += `<text x="${x}" y="${cy + 3.5}" text-anchor="middle" fill="var(--bg)" font-size="10" font-weight="600">${esc(c.fingers[s])}</text>`;
      }
    }
  }
  svg += `</svg>`;
  return svg;
}

function renderFretboardSVG(overlayKey, lastHit, quizMode) {
  const orderedStrings = [...STRINGS].reverse();
  const frets = 12;
  const w = 780;
  const h = 214;
  const left = 48;
  const top = 28;
  const fretW = 58;
  const strGap = 28;
  const overlay = FRET_OVERLAYS[overlayKey];

  let svg = `<svg viewBox="0 0 ${w} ${h}" width="100%" style="min-width:640px;" role="img" aria-label="Diapasón interactivo de guitarra">`;
  svg += `<rect x="${left}" y="${top - 10}" width="${frets * fretW}" height="${strGap * 5 + 20}" rx="8" fill="#1e1e1c" />`;
  svg += `<line x1="${left}" y1="${top - 10}" x2="${left}" y2="${top + strGap * 5 + 10}" stroke="#f7f5ef" stroke-width="4.5" />`;

  for (let f = 1; f <= frets; f++) {
    const x = left + f * fretW;
    svg += `<line x1="${x}" y1="${top - 10}" x2="${x}" y2="${top + strGap * 5 + 10}" stroke="rgba(247,245,239,0.22)" stroke-width="1.5" />`;
    svg += `<text x="${x - fretW / 2}" y="${top + strGap * 5 + 32}" text-anchor="middle" fill="currentColor" opacity="0.65" font-size="11" font-family="monospace">${f}</text>`;
    if ([3, 5, 7, 9].includes(f)) {
      svg += `<circle cx="${x - fretW / 2}" cy="${top + strGap * 2.5}" r="4.5" fill="rgba(247,245,239,0.16)" />`;
    } else if (f === 12) {
      svg += `<circle cx="${x - fretW / 2}" cy="${top + strGap * 1.5}" r="4.2" fill="rgba(247,245,239,0.22)" />`;
      svg += `<circle cx="${x - fretW / 2}" cy="${top + strGap * 3.5}" r="4.2" fill="rgba(247,245,239,0.22)" />`;
    }
  }

  orderedStrings.forEach((st, sIdx) => {
    const y = top + sIdx * strGap;
    svg += `<line x1="${left - 12}" y1="${y}" x2="${left + frets * fretW}" y2="${y}" stroke="rgba(247,245,239,0.55)" stroke-width="${1.0 + sIdx * 0.28}" />`;
    svg += `<text x="14" y="${y + 4}" fill="currentColor" opacity="0.7" font-size="11" font-family="monospace">${st.num}ª</text>`;

    for (let f = 0; f <= frets; f++) {
      const cx = f === 0 ? left - 18 : left + (f - 0.5) * fretW;
      const semi = (st.openSemi + f) % 12;
      const note = NOTE_NAMES[semi];
      const inOverlay = !quizMode && (overlay.positions ? (overlay.positions[sIdx] || []).includes(f) : note.nat);
      const isRoot = !quizMode && semi === overlay.rootSemi && inOverlay;
      const isActive = lastHit && lastHit.stringNum === st.num && lastHit.fret === f;

      const fill = isActive
        ? "#a2e55f"
        : isRoot
        ? "#235e63"
        : inOverlay
        ? "#c7dfdb"
        : "transparent";
      const textFill = isActive ? "#141413" : isRoot ? "#f7f5ef" : "#1e1e1c";

      svg += `<g class="fret-hit" data-str="${st.num}" data-fret="${f}">`;
      svg += `<circle cx="${cx}" cy="${y}" r="11" fill="${fill}" stroke="${inOverlay || isActive ? "rgba(247,245,239,0.25)" : "transparent"}" stroke-width="1" />`;
      if (inOverlay || isActive) {
        svg += `<text x="${cx}" y="${y + 3.8}" text-anchor="middle" fill="${textFill}" font-size="9.5" font-weight="700" font-family="monospace">${note.en}</text>`;
      }
      svg += `</g>`;
    }
  });

  svg += `</svg>`;
  return svg;
}

class GuitarAudio {
  constructor() {
    this.ctx = null;
  }
  ensure() {
    if (!this.ctx) {
      const AC = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AC();
    }
    if (this.ctx.state === "suspended") this.ctx.resume();
    return this.ctx;
  }
  click(time, accent = false) {
    const ctx = this.ensure();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = "triangle";
    osc.frequency.setValueAtTime(accent ? 1280 : 840, time);
    gain.gain.setValueAtTime(accent ? 0.35 : 0.2, time);
    gain.gain.exponentialRampToValueAtTime(0.001, time + 0.045);
    osc.connect(gain).connect(ctx.destination);
    osc.start(time);
    osc.stop(time + 0.05);
  }
  pluck(freq, delaySec = 0, duration = 1.6, volume = 0.24) {
    const ctx = this.ensure();
    const start = ctx.currentTime + delaySec;
    const master = ctx.createGain();
    master.gain.setValueAtTime(0.001, start);
    master.gain.linearRampToValueAtTime(volume, start + 0.012);
    master.gain.exponentialRampToValueAtTime(0.001, start + duration);
    master.connect(ctx.destination);

    const partials = [
      { mult: 1, amp: 1.0, type: "triangle" },
      { mult: 2, amp: 0.42, type: "sine" },
      { mult: 3, amp: 0.16, type: "sine" },
    ];
    partials.forEach((p) => {
      const osc = ctx.createOscillator();
      const g = ctx.createGain();
      osc.type = p.type;
      osc.frequency.setValueAtTime(freq * p.mult, start);
      g.gain.setValueAtTime(p.amp, start);
      osc.connect(g).connect(master);
      osc.start(start);
      osc.stop(start + duration + 0.02);
    });
  }
  strumChord(code) {
    const c = CHORDS[code];
    if (!c) return;
    let offset = 0;
    c.frets.forEach((fret, idx) => {
      if (fret < 0) return;
      const baseFreq = STRINGS[idx].freq;
      const freq = baseFreq * Math.pow(2, fret / 12);
      this.pluck(freq, offset, 1.75, 0.14);
      offset += 0.028;
    });
  }
  close() {
    if (this.ctx) {
      this.ctx.close().catch(() => {});
      this.ctx = null;
    }
  }
}

export async function renderGuitarLab(container, { tab = "metronome" } = {}) {
  let activeTab = ["metronome", "chords", "fretboard", "tuner", "ear"].includes(tab) ? tab : "metronome";
  const audio = new GuitarAudio();

  let bpm = 65;
  let beatsPerBar = 4;
  let metroRunning = false;
  let metroTimer = null;
  let nextNoteTime = 0;
  let currentBeat = 0;
  let currentBar = 0;
  let progKey = "pop";
  let cleanReps = 0;
  let variationIdx = 0;
  let tapTimes = [];

  let chordA = "Em";
  let chordB = "Am";
  let trainerSec = 60;
  let trainerRunning = false;
  let trainerTimer = null;
  let chordCount = 0;

  let fretOverlay = "am_box1";
  let fretQuizMode = false;
  let fretTarget = null;
  let fretQuizScore = { ok: 0, total: 0 };
  let fretQuizMsg = null;
  let lastHit = null;

  let tunerLoop = null;
  let activeString = null;

  // --- Microphone tuner (real pitch detection, no libraries) ---
  let micStream = null;
  let micCtx = null;
  let micTimer = null;
  let micError = "";

  const stopMic = () => {
    if (micTimer) clearInterval(micTimer);
    micTimer = null;
    micStream?.getTracks().forEach((t) => t.stop());
    micStream = null;
    micCtx?.close().catch(() => {});
    micCtx = null;
  };

  const startMic = async () => {
    micError = "";
    if (!navigator.mediaDevices?.getUserMedia) {
      micError = "El micrófono solo funciona en localhost o con HTTPS (mirá el README para activarlo en el celular).";
      return;
    }
    try {
      micStream = await navigator.mediaDevices.getUserMedia({
        audio: { echoCancellation: false, noiseSuppression: false, autoGainControl: false },
      });
    } catch {
      micError = "No pude acceder al micrófono. Revisá el permiso del navegador.";
      return;
    }
    const AC = window.AudioContext || window.webkitAudioContext;
    micCtx = new AC();
    const analyser = micCtx.createAnalyser();
    analyser.fftSize = 4096;
    micCtx.createMediaStreamSource(micStream).connect(analyser);
    const buf = new Float32Array(analyser.fftSize);
    let smooth = null;
    micTimer = setInterval(() => {
      const noteEl = document.getElementById("tuner-note");
      if (!noteEl) {
        stopMic(); // the learner left the tuner tab
        return;
      }
      analyser.getFloatTimeDomainData(buf);
      const freq = detectPitch(buf, micCtx.sampleRate);
      const needle = document.getElementById("tuner-needle");
      const hint = document.getElementById("tuner-hint");
      if (!freq || freq < 60 || freq > 420) {
        hint.textContent = "Tocá una cuerda al aire y dejala sonar…";
        return;
      }
      smooth = smooth && Math.abs(freq - smooth) < 6 ? smooth * 0.6 + freq * 0.4 : freq;
      let best = STRINGS[0];
      let bestCents = Infinity;
      for (const s of STRINGS) {
        const cents = 1200 * Math.log2(smooth / s.freq);
        if (Math.abs(cents) < Math.abs(bestCents)) {
          best = s;
          bestCents = cents;
        }
      }
      const inTune = Math.abs(bestCents) <= 5;
      noteEl.textContent = best.note.split(" ")[0];
      document.getElementById("tuner-string").textContent = `${best.num}ª cuerda · ${smooth.toFixed(1)} Hz`;
      needle.style.left = `${50 + Math.max(-50, Math.min(50, bestCents))}%`;
      needle.classList.toggle("in-tune", inTune);
      hint.textContent = inTune
        ? "Afinada"
        : Math.abs(bestCents) > 250
        ? "Muy lejos: revisá que sea la cuerda correcta"
        : bestCents < 0
        ? `Está baja (${Math.round(bestCents)} cents): tensá la clavija`
        : `Está alta (+${Math.round(bestCents)} cents): aflojá la clavija`;
    }, 90);
  };

  let earMode = "chords";
  let earCurrent = null;
  let earScore = { ok: 0, total: 0 };
  let earFeedback = null;

  const newFretChallenge = () => {
    const natNotes = NOTE_NAMES.filter((n) => n.nat);
    const note = natNotes[Math.floor(Math.random() * natNotes.length)];
    const stringNum = Math.floor(Math.random() * 6) + 1;
    fretTarget = { note, stringNum };
    fretQuizMsg = null;
    lastHit = null;
  };

  const stopAll = () => {
    metroRunning = false;
    if (metroTimer) clearInterval(metroTimer);
    metroTimer = null;
    trainerRunning = false;
    if (trainerTimer) clearInterval(trainerTimer);
    trainerTimer = null;
    if (tunerLoop) clearInterval(tunerLoop);
    tunerLoop = null;
    activeString = null;
    stopMic();
  };

  const onLabKey = (e) => {
    const tag = (document.activeElement?.tagName || "").toLowerCase();
    if (tag === "input" || tag === "textarea" || tag === "select") return;
    if (document.getElementById("cmd-modal") && !document.getElementById("cmd-modal").hidden) return;
    if (e.key === " ") {
      if (activeTab === "metronome") {
        e.preventDefault();
        container.querySelector("#metro-toggle")?.click();
      } else if (activeTab === "chords") {
        e.preventDefault();
        container.querySelector("#add-change")?.click();
      }
    }
  };
  window.addEventListener("keydown", onLabKey);

  registerCleanup(() => {
    window.removeEventListener("keydown", onLabKey);
    stopAll();
    audio.close();
  });

  let metricsCache = [];
  const loadMetrics = async () => {
    try {
      const res = await api.get("/api/metrics?domain=guitarra&limit=20");
      metricsCache = res.metrics || [];
    } catch {
      metricsCache = [];
    }
  };
  await loadMetrics();

  const startMetronome = () => {
    const ctx = audio.ensure();
    metroRunning = true;
    currentBeat = 0;
    currentBar = 0;
    nextNoteTime = ctx.currentTime + 0.05;
    const lookaheadMs = 25;
    const scheduleAheadSec = 0.1;

    metroTimer = setInterval(() => {
      if (!metroRunning) return;
      while (nextNoteTime < ctx.currentTime + scheduleAheadSec) {
        const beatToDraw = currentBeat;
        const barToDraw = currentBar;
        const isAccent = beatToDraw === 0;
        audio.click(nextNoteTime, isAccent);
        const delayMs = Math.max(0, (nextNoteTime - ctx.currentTime) * 1000);
        setTimeout(() => {
          container.querySelectorAll(".beat-dot").forEach((d, idx) => {
            d.classList.toggle("active", idx === beatToDraw);
          });
          const prog = PROGRESSIONS[progKey];
          if (prog && prog.chords.length) {
            const cIdx = barToDraw % prog.chords.length;
            const nIdx = (cIdx + 1) % prog.chords.length;
            container.querySelectorAll(".prog-chord").forEach((el, i) => {
              el.classList.toggle("pill-accent", i === cIdx);
              el.style.fontWeight = i === cIdx ? "700" : "400";
            });
            const hintEl = container.querySelector("#prog-next-hint");
            if (hintEl) {
              hintEl.textContent =
                beatToDraw === beatsPerBar - 1
                  ? `Prepará cambio → ${prog.chords[nIdx]}`
                  : `Acorde actual: ${prog.chords[cIdx]} · Siguiente: ${prog.chords[nIdx]}`;
            }
          }
        }, delayMs);
        nextNoteTime += 60.0 / bpm;
        currentBeat = (currentBeat + 1) % beatsPerBar;
        if (currentBeat === 0) currentBar += 1;
      }
    }, lookaheadMs);
  };

  const stopMetronome = () => {
    metroRunning = false;
    if (metroTimer) clearInterval(metroTimer);
    metroTimer = null;
    container.querySelectorAll(".beat-dot").forEach((d) => d.classList.remove("active"));
  };

  const newEarQuestion = () => {
    earFeedback = null;
    const roots = [196, 220, 246.94, 261.63, 293.66, 329.63];
    const root = roots[Math.floor(Math.random() * roots.length)];
    if (earMode === "chords") {
      const isMajor = Math.random() < 0.5;
      const third = isMajor ? 4 : 3;
      earCurrent = {
        answer: isMajor ? "Mayor" : "Menor",
        options: ["Mayor", "Menor"],
        play: () => {
          audio.pluck(root, 0, 1.5);
          audio.pluck(root * Math.pow(2, third / 12), 0.08, 1.5);
          audio.pluck(root * Math.pow(2, 7 / 12), 0.16, 1.5);
        },
      };
    } else {
      const intervals = [
        { name: "3ª Mayor", semis: 4 },
        { name: "5ª Justa", semis: 7 },
        { name: "8ª Justa (Octava)", semis: 12 },
      ];
      const pick = intervals[Math.floor(Math.random() * intervals.length)];
      earCurrent = {
        answer: pick.name,
        options: intervals.map((i) => i.name),
        play: () => {
          audio.pluck(root, 0, 1.0);
          audio.pluck(root * Math.pow(2, pick.semis / 12), 0.55, 1.2);
        },
      };
    }
    earCurrent.play();
  };

  const paint = () => {
    const bpmHistory = metricsCache.filter((m) => m.metric_type === "bpm_clean").slice(0, 8);
    const chordHistory = metricsCache.filter((m) => m.metric_type === "chord_changes_min").slice(0, 8);

    container.innerHTML = `
      <div class="page-header band dots" data-tone="guitar">
        <div>
          <div class="breadcrumb"><a href="#/labs">Laboratorios</a> <span>/</span> <span>Guitarra</span></div>
          <h1>Guitarra</h1>
          <p>Metrónomo, afinador con micrófono, cambios de acordes, diapasón y oído.</p>
        </div>
        <a href="#/roadmap/guitarra" class="btn btn-secondary btn-sm">${icon("map", 14)} Lecciones de guitarra</a>
      </div>

      <div class="tabs">
        <button class="tab-btn ${activeTab === "metronome" ? "active" : ""}" data-tab="metronome" type="button">${icon("clock", 14)} Metrónomo</button>
        <button class="tab-btn ${activeTab === "chords" ? "active" : ""}" data-tab="chords" type="button">${icon("target", 14)} Cambios de acordes</button>
        <button class="tab-btn ${activeTab === "fretboard" ? "active" : ""}" data-tab="fretboard" type="button">${icon("grid", 14)} Diapasón</button>
        <button class="tab-btn ${activeTab === "tuner" ? "active" : ""}" data-tab="tuner" type="button">${icon("mic", 14)} Afinador</button>
        <button class="tab-btn ${activeTab === "ear" ? "active" : ""}" data-tab="ear" type="button">${icon("volume", 14)} Oído</button>
      </div>

      <div id="guitar-tab-body"></div>
    `;

    container.querySelectorAll(".tab-btn").forEach((b) => {
      b.addEventListener("click", () => {
        stopAll();
        activeTab = b.dataset.tab;
        paint();
      });
    });

    const body = container.querySelector("#guitar-tab-body");

    if (activeTab === "metronome") {
      const prog = PROGRESSIONS[progKey];
      body.innerHTML = `
        <div class="grid-2" style="align-items:start;">
          <div class="card stack" style="text-align:center;">
            <div class="row-between">
              <span class="pill pill-accent">Web Audio · Lookahead</span>
              <div class="segmented">
                ${[4, 3, 6]
                  .map(
                    (b) =>
                      `<button type="button" class="seg-btn ${beatsPerBar === b ? "active" : ""} sig-btn" data-b="${b}">${b}/${b === 6 ? 8 : 4}</button>`
                  )
                  .join("")}
              </div>
            </div>

            <div style="padding:10px 0 4px;">
              <div style="font-family:var(--font-serif);font-size:3.8rem;font-weight:400;line-height:1;" id="bpm-display">${bpm}</div>
              <div class="xs mono muted">BPM · <kbd class="kbd">Espacio</kbd> iniciar/pausar</div>
            </div>

            <div class="beat-dots">
              ${Array.from({ length: beatsPerBar })
                .map((_, i) => `<div class="beat-dot ${i === 0 ? "accent" : ""}"></div>`)
                .join("")}
            </div>

            <input id="bpm-slider" type="range" min="35" max="200" value="${bpm}" />
            <div class="row" style="justify-content:center;">
              <button id="bpm-minus" class="btn btn-secondary btn-sm" type="button">-5 BPM</button>
              <button id="metro-toggle" class="btn ${metroRunning ? "btn-danger" : "btn-primary"} btn-lg" type="button">
                ${metroRunning ? icon("stop", 15) + " Detener" : icon("play", 15) + " Iniciar"}
              </button>
              <button id="bpm-plus" class="btn btn-secondary btn-sm" type="button">+5 BPM</button>
              <button id="tap-tempo" class="btn btn-ghost btn-sm" type="button">Tap Tempo</button>
            </div>

            <div class="divider"></div>
            <div class="stack" style="text-align:left;gap:10px;">
              <label class="field">
                <span>Progresión guiada por compás (avisa el cambio en el pulso 4)</span>
                <select id="prog-select">
                  ${Object.entries(PROGRESSIONS)
                    .map(([k, v]) => `<option value="${k}" ${k === progKey ? "selected" : ""}>${esc(v.label)}</option>`)
                    .join("")}
                </select>
              </label>
              <div class="card-flat stack" style="gap:8px;">
                <div class="row-between">
                  <span class="xs mono muted">PATRÓN DE RASGUEO</span>
                  <span class="mono small" style="font-weight:600;letter-spacing:0.08em;">${esc(prog.pattern)}</span>
                </div>
                ${
                  prog.chords.length
                    ? `<div class="row" style="justify-content:center;gap:8px;">
                        ${prog.chords.map((c, i) => `<button type="button" class="pill prog-chord ${i === 0 ? "pill-accent" : ""}" data-c="${c}" style="cursor:pointer;font-size:0.86rem;padding:5px 13px;">${esc(c)}</button>`).join("")}
                       </div>
                       <div id="prog-next-hint" class="xs mono muted" style="text-align:center;">Tocá cualquier acorde arriba para escucharlo · Iniciá el metrónomo para ciclar</div>`
                    : `<div class="xs muted">Elegí una progresión para practicar cambios a tempo real.</div>`
                }
              </div>
            </div>
          </div>

          <div class="card stack">
            <div class="eyebrow" style="margin:0;">Práctica deliberada · Overlearning</div>
            <h2 style="font-size:1.35rem;margin-bottom:4px;">Escalera de BPM</h2>
            <p class="small muted">
              Regla motora: <strong>no subas la velocidad si cometiste un error</strong>.
              Marcá 3 repeticiones limpias seguidas para guardar tu marca y subir +5 BPM automáticamente.
            </p>
            <label class="field">
              <span>Ejercicio o pasaje actual</span>
              <input id="drill-label" type="text" value="Progresión G-D-Em-C / Patrón 4/4" />
            </label>
            <div class="row-between card-flat">
              <div>
                <strong class="small">Repeticiones limpias: ${cleanReps}/3</strong>
                <div class="xs muted">Si trasteaste o frenaste, bajá 5 BPM.</div>
              </div>
              <div class="rep-dots">
                ${[1, 2, 3]
                  .map((n) => `<button type="button" class="rep-dot ${n <= cleanReps ? "done" : ""}" data-n="${n}">${n}</button>`)
                  .join("")}
              </div>
            </div>
            <div class="row">
              <button id="clean-rep-btn" class="btn btn-accent" type="button">${icon("check", 15)} Repetición limpia (+1)</button>
              <button id="mistake-btn" class="btn btn-danger btn-sm" type="button">${icon("refresh", 13)} Hubo error (-5 BPM)</button>
            </div>

            <div class="card-flat callout-info stack" style="gap:6px;">
              <div class="row-between">
                <span class="xs mono muted">VARIACIÓN MOTORA (JOHNS HOPKINS)</span>
                <button id="next-var" type="button" class="btn btn-ghost btn-sm" style="padding:3px 9px;">${icon("shuffle", 12)} Otra</button>
              </div>
              <p class="small" style="margin:0;">${esc(MOTOR_VARIATIONS[variationIdx])}</p>
            </div>

            ${
              bpmHistory.length
                ? `<div class="divider"></div>
                   <div class="row-between xs mono muted"><span>EVOLUCIÓN DE BPM LIMPIO</span><span>${bpmHistory.length} marcas</span></div>
                   ${renderSparklineSVG(bpmHistory.map((m) => m.value), "BPM")}
                   <div class="stack" style="gap:6px;">
                     ${bpmHistory
                       .slice(0, 5)
                       .map(
                         (m) =>
                           `<div class="row-between small"><span>${esc(m.label || "Práctica")}</span><span class="pill pill-green">${m.value} BPM</span></div>`
                       )
                       .join("")}
                   </div>`
                : ""
            }
          </div>
        </div>
      `;

      const updateBpm = (val) => {
        bpm = Math.max(35, Math.min(200, Math.round(val)));
        body.querySelector("#bpm-display").textContent = bpm;
        body.querySelector("#bpm-slider").value = bpm;
      };
      body.querySelector("#bpm-slider").addEventListener("input", (e) => updateBpm(Number(e.target.value)));
      body.querySelector("#bpm-minus").addEventListener("click", () => updateBpm(bpm - 5));
      body.querySelector("#bpm-plus").addEventListener("click", () => updateBpm(bpm + 5));
      body.querySelector("#prog-select").addEventListener("change", (e) => { progKey = e.target.value; paint(); });
      body.querySelectorAll(".prog-chord").forEach((btn) => {
        btn.addEventListener("click", () => audio.strumChord(btn.dataset.c));
      });
      body.querySelector("#next-var").addEventListener("click", () => {
        variationIdx = (variationIdx + 1) % MOTOR_VARIATIONS.length;
        paint();
      });
      body.querySelectorAll(".sig-btn").forEach((b) => {
        b.addEventListener("click", () => {
          const wasRunning = metroRunning;
          stopMetronome();
          beatsPerBar = Number(b.dataset.b);
          paint();
          if (wasRunning) startMetronome();
        });
      });
      body.querySelector("#metro-toggle").addEventListener("click", () => {
        if (metroRunning) stopMetronome();
        else startMetronome();
        paint();
      });
      body.querySelector("#tap-tempo").addEventListener("click", () => {
        const now = performance.now();
        tapTimes = tapTimes.filter((t) => now - t < 2500);
        tapTimes.push(now);
        if (tapTimes.length >= 2) {
          const diffs = [];
          for (let i = 1; i < tapTimes.length; i++) diffs.push(tapTimes[i] - tapTimes[i - 1]);
          const avgMs = diffs.reduce((a, b) => a + b, 0) / diffs.length;
          updateBpm(60000 / avgMs);
        }
      });

      const handleCleanRep = async () => {
        cleanReps += 1;
        if (cleanReps >= 3) {
          const label = body.querySelector("#drill-label")?.value || "Escalera BPM";
          await api.post("/api/metrics", {
            domain_slug: "guitarra",
            metric_type: "bpm_clean",
            label,
            value: bpm,
            unit: "BPM",
          });
          toast(`3 limpias a ${bpm} BPM — subiendo a ${Math.min(200, bpm + 5)} BPM`, "ok");
          bpm = Math.min(200, bpm + 5);
          cleanReps = 0;
          await loadMetrics();
        }
        paint();
      };

      body.querySelector("#clean-rep-btn").addEventListener("click", handleCleanRep);
      body.querySelectorAll(".rep-dot").forEach((b) => b.addEventListener("click", handleCleanRep));
      body.querySelector("#mistake-btn").addEventListener("click", () => {
        cleanReps = 0;
        bpm = Math.max(35, bpm - 5);
        toast(`Ajustado a ${bpm} BPM para consolidar sin errores`, "info");
        paint();
      });
    } else if (activeTab === "chords") {
      const chordKeys = Object.keys(CHORDS);
      body.innerHTML = `
        <div class="grid-2" style="align-items:start;">
          <div class="card stack">
            <div class="row-between">
              <h2 style="font-size:1.3rem;margin:0;">Cambios de Acordes (60s)</h2>
              <span class="pill pill-accent mono" id="chord-timer" style="font-size:0.9rem;">${icon("clock", 13)} ${trainerSec}s</span>
            </div>
            <div class="grid-2" style="gap:10px;">
              <label class="field">
                <span>Acorde A</span>
                <select id="sel-chord-a">
                  ${chordKeys.map((k) => `<option value="${k}" ${k === chordA ? "selected" : ""}>${esc(CHORDS[k].name)}</option>`).join("")}
                </select>
              </label>
              <label class="field">
                <span>Acorde B</span>
                <select id="sel-chord-b">
                  ${chordKeys.map((k) => `<option value="${k}" ${k === chordB ? "selected" : ""}>${esc(CHORDS[k].name)}</option>`).join("")}
                </select>
              </label>
            </div>
            <div class="row" style="justify-content:space-around;padding:10px 0;">
              <div class="stack" style="align-items:center;gap:8px;">
                ${renderChordSVG(chordA)}
                <button type="button" class="btn btn-secondary btn-sm strum-btn" data-c="${chordA}">${icon("volume", 13)} Escuchar ${esc(chordA)}</button>
                <div class="xs muted" style="max-width:170px;text-align:center;">${esc(CHORDS[chordA].tip)}</div>
              </div>
              <div class="mono muted" style="font-size:1.4rem;">↔</div>
              <div class="stack" style="align-items:center;gap:8px;">
                ${renderChordSVG(chordB)}
                <button type="button" class="btn btn-secondary btn-sm strum-btn" data-c="${chordB}">${icon("volume", 13)} Escuchar ${esc(chordB)}</button>
                <div class="xs muted" style="max-width:170px;text-align:center;">${esc(CHORDS[chordB].tip)}</div>
              </div>
            </div>
          </div>

          <div class="card stack" style="text-align:center;">
            <div class="eyebrow" style="margin:0 auto;">Micro-Drill cronometrado · <kbd class="kbd">Espacio</kbd> para contar</div>
            <h2 style="font-size:1.3rem;margin:0;">Cambios limpios por minuto</h2>
            <p class="small muted">Escuchá el sonido de referencia antes de empezar y contá solo los cambios que suenen limpios.</p>
            <div style="font-family:var(--font-serif);font-size:4rem;line-height:1;color:var(--accent);" id="chord-count">${chordCount}</div>
            <div class="row" style="justify-content:center;">
              <button id="start-1m" class="btn ${trainerRunning ? "btn-danger" : "btn-primary"}" type="button">
                ${trainerRunning ? icon("stop", 14) + " Reiniciar 60s" : icon("play", 14) + " Iniciar 60s"}
              </button>
              <button id="add-change" class="btn btn-accent btn-lg" type="button">${icon("plus", 15)} 1 cambio limpio</button>
              <button id="save-changes" class="btn btn-secondary" type="button">Guardar marca</button>
            </div>

            ${
              chordHistory.length
                ? `<div class="divider"></div>
                   <div class="xs mono muted" style="text-align:left;">EVOLUCIÓN DE MARCAS</div>
                   ${renderSparklineSVG(chordHistory.map((m) => m.value), "cambios/min")}
                   <div class="stack" style="gap:6px;text-align:left;">
                     ${chordHistory
                       .slice(0, 5)
                       .map(
                         (m) =>
                           `<div class="row-between small"><span>${esc(m.label)}</span><span class="pill pill-green">${m.value} / min</span></div>`
                       )
                       .join("")}
                   </div>`
                : ""
            }
          </div>
        </div>
      `;

      body.querySelectorAll(".strum-btn").forEach((b) => {
        b.addEventListener("click", () => audio.strumChord(b.dataset.c));
      });
      body.querySelector("#sel-chord-a").addEventListener("change", (e) => { chordA = e.target.value; paint(); });
      body.querySelector("#sel-chord-b").addEventListener("change", (e) => { chordB = e.target.value; paint(); });
      body.querySelector("#add-change").addEventListener("click", () => {
        chordCount += 1;
        body.querySelector("#chord-count").textContent = chordCount;
      });
      body.querySelector("#start-1m").addEventListener("click", () => {
        if (trainerRunning) {
          clearInterval(trainerTimer);
          trainerRunning = false;
          trainerSec = 60;
          chordCount = 0;
          paint();
          return;
        }
        trainerRunning = true;
        trainerSec = 60;
        chordCount = 0;
        paint();
        trainerTimer = setInterval(() => {
          trainerSec -= 1;
          const tEl = body.querySelector("#chord-timer");
          if (tEl) tEl.innerHTML = `${icon("clock", 13)} ${trainerSec}s`;
          if (trainerSec <= 0) {
            clearInterval(trainerTimer);
            trainerRunning = false;
            audio.click(audio.ensure().currentTime, true);
            toast(`Tiempo cumplido: ${chordCount} cambios (${chordA} ↔ ${chordB}). Guardá tu marca.`, "ok");
          }
        }, 1000);
      });
      body.querySelector("#save-changes").addEventListener("click", async () => {
        if (chordCount <= 0) {
          toast("Registrá al menos 1 cambio antes de guardar", "err");
          return;
        }
        await api.post("/api/metrics", {
          domain_slug: "guitarra",
          metric_type: "chord_changes_min",
          label: `${chordA} ↔ ${chordB}`,
          value: chordCount,
          unit: "cambios/min",
        });
        toast(`Marca guardada: ${chordCount} cambios/min (${chordA} ↔ ${chordB})`, "ok");
        await loadMetrics();
        paint();
      });
    } else if (activeTab === "fretboard") {
      if (fretQuizMode && !fretTarget) newFretChallenge();
      body.innerHTML = `
        <div class="card stack">
          <div class="row-between">
            <div>
              <div class="eyebrow" style="margin-bottom:4px;">Mapeo visual + Web Audio real</div>
              <h2 style="font-size:1.35rem;margin:0;">Diapasón interactivo (6 cuerdas × 12 trastes)</h2>
            </div>
            <div class="row">
              <div class="segmented">
                <button type="button" class="seg-btn ${!fretQuizMode ? "active" : ""} f-mode" data-m="explore">Explorar escalas</button>
                <button type="button" class="seg-btn ${fretQuizMode ? "active" : ""} f-mode" data-m="quiz">Modo Desafío</button>
              </div>
              ${
                !fretQuizMode
                  ? `<div class="segmented">
                      ${Object.entries(FRET_OVERLAYS)
                        .map(
                          ([k, v]) =>
                            `<button type="button" class="seg-btn ${fretOverlay === k ? "active" : ""} fret-ov" data-ov="${k}">${esc(v.label.split("(")[0].trim())}</button>`
                        )
                        .join("")}
                     </div>`
                  : `<span class="pill pill-green">Aciertos: ${fretQuizScore.ok}/${fretQuizScore.total}</span>`
              }
            </div>
          </div>

          ${
            fretQuizMode
              ? `<div class="card-flat callout-info row-between">
                  <div>
                    <div class="xs mono muted">DESAFÍO ACTIVO DE MEMORIA DEL MÁSTIL</div>
                    <strong style="font-size:1.05rem;">Encontrá un ${esc(fretTarget.note.es)} (${esc(fretTarget.note.en)}) en la ${fretTarget.stringNum}ª cuerda</strong>
                  </div>
                  <button id="next-fret-q" type="button" class="btn btn-secondary btn-sm">Otra nota →</button>
                 </div>
                 ${fretQuizMsg ? `<div class="callout ${fretQuizMsg.ok ? "callout-ok" : "callout-warn"} small">${fretQuizMsg.ok ? icon("check", 14) : icon("x", 14)} ${esc(fretQuizMsg.text)}</div>` : ""}`
              : `<div class="row-between card-flat">
                  <span class="small">
                    ${
                      lastHit
                        ? `<strong>${lastHit.stringNum}ª cuerda · Traste ${lastHit.fret}:</strong> ${esc(lastHit.noteEs)} (${esc(lastHit.noteEn)}) · <span class="mono">${lastHit.freq.toFixed(1)} Hz</span>`
                        : `<span>Patrón activo: <strong>${esc(FRET_OVERLAYS[fretOverlay].label)}</strong>. Hacé click en cualquier traste para escuchar su nota.</span>`
                    }
                  </span>
                  <div class="row xs mono muted">
                    <span class="pill pill-accent">Tónica</span>
                    <span class="pill">Nota del patrón</span>
                  </div>
                </div>`
          }

          <div class="fretboard-wrap">
            ${renderFretboardSVG(fretOverlay, lastHit, fretQuizMode)}
          </div>
        </div>
      `;

      body.querySelectorAll(".f-mode").forEach((b) => {
        b.addEventListener("click", () => {
          fretQuizMode = b.dataset.m === "quiz";
          if (fretQuizMode) newFretChallenge();
          paint();
        });
      });
      body.querySelector("#next-fret-q")?.addEventListener("click", () => { newFretChallenge(); paint(); });
      body.querySelectorAll(".fret-ov").forEach((b) => {
        b.addEventListener("click", () => { fretOverlay = b.dataset.ov; paint(); });
      });
      body.querySelectorAll(".fret-hit").forEach((g) => {
        g.addEventListener("click", () => {
          const stringNum = Number(g.dataset.str);
          const fret = Number(g.dataset.fret);
          const st = STRINGS.find((x) => x.num === stringNum);
          const freq = st.freq * Math.pow(2, fret / 12);
          const note = NOTE_NAMES[(st.openSemi + fret) % 12];
          audio.pluck(freq, 0, 1.4);
          lastHit = { stringNum, fret, freq, noteEn: note.en, noteEs: note.es };
          if (fretQuizMode && fretTarget) {
            fretQuizScore.total += 1;
            if (stringNum === fretTarget.stringNum && note.en === fretTarget.note.en) {
              fretQuizScore.ok += 1;
              fretQuizMsg = { ok: true, text: `Exacto: ${note.es} (${note.en}) en ${stringNum}ª cuerda traste ${fret}.` };
              setTimeout(() => { newFretChallenge(); paint(); }, 1000);
            } else {
              fretQuizMsg = { ok: false, text: `Tocaste ${note.es} (${note.en}) en la ${stringNum}ª cuerda traste ${fret}. Buscá ${fretTarget.note.es} en la ${fretTarget.stringNum}ª cuerda.` };
            }
          }
          paint();
        });
      });
    } else if (activeTab === "tuner") {
      body.innerHTML = `
        <div class="card stack mb-md" style="max-width:780px;">
          <div class="row-between">
            <div>
              <h2 class="title-sm m-0">Afinador con micrófono</h2>
              <p class="small muted m-0 mt-sm">Tocá una cuerda al aire: te digo cuál es y si está alta o baja.</p>
            </div>
            <button id="mic-toggle" class="btn ${micStream ? "btn-danger" : "btn-primary"}" type="button">${icon(micStream ? "stop" : "mic", 16)} ${micStream ? "Dejar de escuchar" : "Escuchar"}</button>
          </div>
          ${micError ? `<p class="callout callout-warn m-0">${esc(micError)}</p>` : ""}
          ${
            micStream
              ? `<div class="tuner-face" aria-live="polite">
                  <div class="tuner-note" id="tuner-note">–</div>
                  <div class="small muted" id="tuner-string">Esperando sonido</div>
                  <div class="tuner-scale"><div class="tuner-needle" id="tuner-needle"></div></div>
                  <div class="row-between xs muted" style="width:100%;max-width:420px;"><span>baja</span><span>alta</span></div>
                  <strong id="tuner-hint">Tocá una cuerda al aire y dejala sonar…</strong>
                </div>`
              : ""
          }
        </div>
        <div class="card stack" style="max-width:780px;">
          <div class="row-between">
            <div>
              <h2 class="title-sm m-0">Tonos de referencia</h2>
              <p class="small muted m-0 mt-sm">Elegí una cuerda para escuchar cómo debe sonar, en repetición, mientras ajustás la clavija de oído.</p>
            </div>
            <button id="stop-tuner" class="btn btn-danger btn-sm" type="button">${icon("stop", 13)} Silenciar</button>
          </div>
          <div class="grid-3">
            ${STRINGS.map(
              (s) => `
              <button type="button" class="card-flat stack string-btn" data-num="${s.num}" style="cursor:pointer;text-align:left;border-color:${activeString === s.num ? "var(--accent)" : ""};background:${activeString === s.num ? "var(--bg-wash)" : ""};">
                <div class="row-between">
                  <span class="pill ${activeString === s.num ? "pill-accent" : ""}">${s.num}ª cuerda</span>
                  <span class="xs mono muted">${s.freq} Hz</span>
                </div>
                <strong>${esc(s.note)}</strong>
                <span class="xs muted">${activeString === s.num ? "Sonando en loop..." : "Click para reproducir"}</span>
              </button>`
            ).join("")}
          </div>
        </div>
      `;

      body.querySelectorAll(".string-btn").forEach((btn) => {
        btn.addEventListener("click", () => {
          const num = Number(btn.dataset.num);
          const s = STRINGS.find((x) => x.num === num);
          if (tunerLoop) clearInterval(tunerLoop);
          activeString = num;
          audio.pluck(s.freq, 0, 2.0);
          tunerLoop = setInterval(() => audio.pluck(s.freq, 0, 2.0), 2200);
          paint();
        });
      });
      body.querySelector("#mic-toggle").addEventListener("click", async () => {
        if (micStream) stopMic();
        else await startMic();
        paint();
      });
      body.querySelector("#stop-tuner").addEventListener("click", () => {
        if (tunerLoop) clearInterval(tunerLoop);
        tunerLoop = null;
        activeString = null;
        paint();
      });
    } else if (activeTab === "ear") {
      body.innerHTML = `
        <div class="card stack" style="max-width:720px;">
          <div class="row-between">
            <div>
              <div class="eyebrow" style="margin-bottom:4px;">Percepción auditiva</div>
              <h2 style="font-size:1.35rem;margin:0;">Entrenamiento de oído inicial</h2>
            </div>
            <span class="pill pill-green">Aciertos: ${earScore.ok}/${earScore.total}</span>
          </div>
          <div class="segmented" style="width:fit-content;">
            <button type="button" class="seg-btn ${earMode === "chords" ? "active" : ""} ear-mode" data-m="chords">Mayor vs Menor</button>
            <button type="button" class="seg-btn ${earMode === "intervals" ? "active" : ""} ear-mode" data-m="intervals">Intervalos (3ª, 5ª, 8ª)</button>
          </div>
          <div class="card-flat stack" style="text-align:center;padding:28px 20px;">
            <div class="row" style="justify-content:center;">
              <button id="ear-new" class="btn btn-primary btn-lg" type="button">${icon("volume", 16)} ${earCurrent ? "Nueva prueba" : "Escuchar primera prueba"}</button>
              ${earCurrent ? `<button id="ear-replay" class="btn btn-secondary" type="button">${icon("refresh", 14)} Repetir</button>` : ""}
            </div>
            ${
              earCurrent
                ? `<div class="row" style="justify-content:center;margin-top:10px;">
                    ${earCurrent.options
                      .map((opt) => `<button type="button" class="btn btn-secondary ear-ans" data-opt="${esc(opt)}">${esc(opt)}</button>`)
                      .join("")}
                   </div>`
                : `<p class="xs muted">Recomendación: cantá mentalmente o en voz baja las notas antes de elegir respuesta.</p>`
            }
            ${
              earFeedback
                ? `<div class="callout ${earFeedback.ok ? "callout-ok" : "callout-warn"} small">${earFeedback.ok ? icon("check", 14) : icon("x", 14)} ${esc(earFeedback.text)}</div>`
                : ""
            }
          </div>
        </div>
      `;

      body.querySelectorAll(".ear-mode").forEach((b) => {
        b.addEventListener("click", () => {
          earMode = b.dataset.m;
          earCurrent = null;
          earFeedback = null;
          paint();
        });
      });
      body.querySelector("#ear-new")?.addEventListener("click", () => { newEarQuestion(); paint(); });
      body.querySelector("#ear-replay")?.addEventListener("click", () => earCurrent?.play());
      body.querySelectorAll(".ear-ans").forEach((b) => {
        b.addEventListener("click", () => {
          const picked = b.dataset.opt;
          earScore.total += 1;
          if (picked === earCurrent.answer) {
            earScore.ok += 1;
            earFeedback = { ok: true, text: `Correcto: era ${earCurrent.answer}.` };
          } else {
            earFeedback = { ok: false, text: `Era ${earCurrent.answer} (elegiste ${picked}). Repetí el sonido para fijar el color armónico.` };
          }
          paint();
        });
      });
    }
  };

  paint();
}
