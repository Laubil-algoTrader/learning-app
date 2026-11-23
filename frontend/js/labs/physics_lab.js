import { icon } from "../icons.js";
import { api, esc, registerCleanup, toast } from "../main.js";

const GRAVITIES = [
  { name: "Tierra", g: 9.81 },
  { name: "Luna", g: 1.62 },
  { name: "Marte", g: 3.72 },
];

const SURFACES = [
  { name: "Hielo (μ = 0.05)", mu: 0.05 },
  { name: "Madera (μ = 0.30)", mu: 0.30 },
  { name: "Goma (μ = 0.70)", mu: 0.70 },
];

const FLUID_OBJECTS = [
  { name: "Corcho", rho: 240, color: "#c8a97e" },
  { name: "Madera", rho: 600, color: "#b67e4f" },
  { name: "Hielo", rho: 900, color: "#c7dfdb" },
  { name: "Aluminio", rho: 2700, color: "#a9b7de" },
  { name: "Acero", rho: 7800, color: "#8d8a82" },
];

const FLUID_LIQUIDS = [
  { name: "Aceite", rho: 800, color: "rgba(220, 189, 120, 0.42)" },
  { name: "Agua dulce", rho: 1000, color: "rgba(86, 152, 168, 0.45)" },
  { name: "Agua de mar", rho: 1025, color: "rgba(41, 106, 108, 0.55)" },
  { name: "Mercurio", rho: 13600, color: "rgba(180, 184, 192, 0.65)" },
];

const OPTIC_MEDIA = [
  { name: "Aire", n: 1.0, tint: "rgba(255, 255, 255, 0.03)" },
  { name: "Agua", n: 1.33, tint: "rgba(86, 152, 168, 0.28)" },
  { name: "Vidrio (Fibra)", n: 1.5, tint: "rgba(143, 193, 187, 0.34)" },
  { name: "Diamante", n: 2.42, tint: "rgba(169, 183, 222, 0.36)" },
];

function drawArrow(ctx, x1, y1, x2, y2, color, label = "") {
  const dx = x2 - x1;
  const dy = y2 - y1;
  const len = Math.hypot(dx, dy);
  if (len < 4) return;
  const angle = Math.atan2(dy, dx);
  ctx.save();
  ctx.strokeStyle = color;
  ctx.fillStyle = color;
  ctx.lineWidth = 2.4;
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.lineTo(x2, y2);
  ctx.stroke();

  const head = 8;
  ctx.beginPath();
  ctx.moveTo(x2, y2);
  ctx.lineTo(x2 - head * Math.cos(angle - 0.45), y2 - head * Math.sin(angle - 0.45));
  ctx.lineTo(x2 - head * Math.cos(angle + 0.45), y2 - head * Math.sin(angle + 0.45));
  ctx.closePath();
  ctx.fill();

  if (label) {
    ctx.font = "11px monospace";
    ctx.fillText(label, x2 + 6, y2 + 4);
  }
  ctx.restore();
}

export async function renderPhysicsLab(container, { tab = "kinematics" } = {}) {
  let activeTab = ["kinematics", "forces", "waves", "energy", "fluids", "optics"].includes(tab) ? tab : "kinematics";
  let rafId = null;

  // Audio for Waves tab
  let audioCtx = null;
  let waveOsc = null;
  let waveGain = null;
  let waveSoundOn = false;

  const stopAnimAndAudio = () => {
    if (rafId) {
      cancelAnimationFrame(rafId);
      rafId = null;
    }
    if (waveOsc) {
      try { waveOsc.stop(); } catch { /* ignore */ }
      waveOsc = null;
    }
    if (audioCtx) {
      audioCtx.close().catch(() => {});
      audioCtx = null;
    }
    waveSoundOn = false;
  };
  registerCleanup(stopAnimAndAudio);

  // Tab 1: Projectile state
  let angleDeg = 45;
  let speed0 = 22;
  let gravIdx = 0;
  let projRunning = false;
  let projT = 0;
  let projTrail = [];

  // Tab 2: Forces & Newton DCL state
  let massKg = 5;
  let pushN = 25;
  let surfIdx = 1;
  let blockX = 120;
  let blockV = 0;

  // Tab 3: Waves & Harmonics state
  let baseFreq = 110;
  let harmonicN = 1;
  let waveAmp = 36;
  let wavePhase = 0;

  // Tab 4: Energy Ramp state
  let rampMass = 2;
  let rampHeight = 4.0;
  let rampFriction = false;
  let rampPos = -1.0; // normalized -1..+1 along parabola y = x^2
  let rampVel = 0;
  let thermalJ = 0;

  // Tab 5: Fluids & Archimedes state
  let fluidObjIdx = 2; // Hielo (900 kg/m³)
  let fluidLiqIdx = 1; // Agua dulce (1000 kg/m³)
  let fluidVolL = 10; // Liters (dm³ -> 0.001 m³)
  let diveDepthM = 10;

  // Tab 6: Optics & Snell's Law state
  let opticMed1 = 2; // Vidrio (1.50)
  let opticMed2 = 0; // Aire (1.00) -> immediately shows critical angle & fiber optics!
  let incAngleDeg = 35;

  const toggleWaveTone = () => {
    if (waveSoundOn) {
      if (waveOsc) { try { waveOsc.stop(); } catch { /* ignore */ } waveOsc = null; }
      waveSoundOn = false;
      return;
    }
    const AC = window.AudioContext || window.webkitAudioContext;
    if (!audioCtx) audioCtx = new AC();
    if (audioCtx.state === "suspended") audioCtx.resume();
    waveOsc = audioCtx.createOscillator();
    waveGain = audioCtx.createGain();
    waveOsc.type = "triangle";
    waveOsc.frequency.setValueAtTime(baseFreq * harmonicN, audioCtx.currentTime);
    waveGain.gain.setValueAtTime(Math.min(0.22, (waveAmp / 60) * 0.2), audioCtx.currentTime);
    waveOsc.connect(waveGain).connect(audioCtx.destination);
    waveOsc.start();
    waveSoundOn = true;
  };

  const paint = () => {
    if (rafId) { cancelAnimationFrame(rafId); rafId = null; }
    if (activeTab !== "waves" && waveSoundOn) toggleWaveTone();

    container.innerHTML = `
      <div class="page-header band dots" data-tone="physics">
        <div>
          <div class="breadcrumb"><a href="#/labs">Laboratorios</a> <span>/</span> <span>Física</span></div>
          <h1>Física</h1>
          <p>Simuladores para ver lo que no se ve: trayectorias, fuerzas, ondas, energía, fluidos y óptica.</p>
        </div>
        <a href="#/roadmap/fisica" class="btn btn-secondary btn-sm">${icon("map", 14)} Lecciones de física</a>
      </div>

      <div class="tabs">
        <button class="tab-btn ${activeTab === "kinematics" ? "active" : ""}" data-tab="kinematics" type="button">${icon("arrowUpRight", 14)} Proyectiles</button>
        <button class="tab-btn ${activeTab === "forces" ? "active" : ""}" data-tab="forces" type="button">${icon("target", 14)} Fuerzas</button>
        <button class="tab-btn ${activeTab === "waves" ? "active" : ""}" data-tab="waves" type="button">${icon("volume", 14)} Ondas</button>
        <button class="tab-btn ${activeTab === "energy" ? "active" : ""}" data-tab="energy" type="button">${icon("activity", 14)} Energía</button>
        <button class="tab-btn ${activeTab === "fluids" ? "active" : ""}" data-tab="fluids" type="button">${icon("layers", 14)} Fluidos</button>
        <button class="tab-btn ${activeTab === "optics" ? "active" : ""}" data-tab="optics" type="button">${icon("eye", 14)} Óptica</button>
      </div>

      <div id="phys-tab-body"></div>
    `;

    container.querySelectorAll(".tab-btn").forEach((b) => {
      b.addEventListener("click", () => { activeTab = b.dataset.tab; paint(); });
    });

    const body = container.querySelector("#phys-tab-body");

    /* ---------------- TAB 1: KINEMATICS & PROJECTILES ---------------- */
    if (activeTab === "kinematics") {
      const grav = GRAVITIES[gravIdx];
      const rad = (angleDeg * Math.PI) / 180;
      const vx0 = speed0 * Math.cos(rad);
      const vy0 = speed0 * Math.sin(rad);
      const tFlight = (2 * vy0) / grav.g;
      const hMax = (vy0 * vy0) / (2 * grav.g);
      const range = vx0 * tFlight;

      body.innerHTML = `
        <div class="grid-asymmetric">
          <div class="card stack">
            <div class="row-between">
              <div>
                <div class="eyebrow" style="margin-bottom:2px;">Cinemática 2D · Sin rozamiento del aire</div>
                <h2 style="font-size:1.3rem;margin:0;">Simulador de Tiro Parabólico</h2>
              </div>
              <div class="row">
                <button id="proj-fire" class="btn btn-primary btn-sm" type="button">${icon("play", 13)} Lanzar</button>
                <button id="proj-clear" class="btn btn-ghost btn-sm" type="button">Limpiar</button>
              </div>
            </div>
            <canvas id="proj-canvas" class="lab-canvas" width="600" height="310"></canvas>
            <div class="grid-4">
              <div class="card-flat">
                <div class="xs mono muted">ALCANCE (R)</div>
                <strong class="mono">${range.toFixed(1)} m</strong>
              </div>
              <div class="card-flat">
                <div class="xs mono muted">ALTURA MÁX</div>
                <strong class="mono">${hMax.toFixed(1)} m</strong>
              </div>
              <div class="card-flat">
                <div class="xs mono muted">TIEMPO VUELO</div>
                <strong class="mono">${tFlight.toFixed(2)} s</strong>
              </div>
              <div class="card-flat">
                <div class="xs mono muted">Vx / Vy₀</div>
                <strong class="mono">${vx0.toFixed(1)} / ${vy0.toFixed(1)}</strong>
              </div>
            </div>
          </div>

          <div class="card stack">
            <div class="eyebrow" style="margin:0;">Controles del experimento</div>
            <div class="segmented" style="width:fit-content;">
              ${GRAVITIES.map(
                (gr, i) => `<button type="button" class="seg-btn ${i === gravIdx ? "active" : ""} grav-btn" data-i="${i}">${gr.name} (${gr.g})</button>`
              ).join("")}
            </div>
            <label class="field">
              <span class="row-between"><span>Ángulo de disparo (θ)</span><strong class="mono">${angleDeg}°</strong></span>
              <input id="ang-slider" type="range" min="15" max="85" step="1" value="${angleDeg}" />
            </label>
            <label class="field">
              <span class="row-between"><span>Velocidad inicial (v₀)</span><strong class="mono">${speed0} m/s</strong></span>
              <input id="spd-slider" type="range" min="10" max="32" step="1" value="${speed0}" />
            </label>
            <div class="callout callout-info small">
              <strong>Reto de indagación guiada:</strong> Lanzá a <strong>30°</strong> y luego a <strong>60°</strong> con la misma velocidad sin limpiar.
              Comprobá por qué caen en el mismo alcance y observá que el vector verde <strong>Vx</strong> jamás cambia de tamaño.
            </div>
          </div>
        </div>
      `;

      const canvas = body.querySelector("#proj-canvas");
      const ctx = canvas.getContext("2d");

      const drawProjectile = (curT) => {
        const w = canvas.width;
        const h = canvas.height;
        const groundY = h - 34;
        const originX = 36;
        // Dynamic scale so trajectory always fits cleanly
        const scale = Math.min((w - 72) / Math.max(range, 35), (groundY - 36) / Math.max(hMax, 18));

        ctx.fillStyle = "#1e1e1c";
        ctx.fillRect(0, 0, w, h);

        // Ground line
        ctx.strokeStyle = "rgba(247,245,239,0.35)";
        ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.moveTo(0, groundY); ctx.lineTo(w, groundY); ctx.stroke();

        // Theoretical dashed curve
        ctx.strokeStyle = "rgba(199,223,219,0.28)";
        ctx.setLineDash([4, 4]);
        ctx.lineWidth = 1.6;
        ctx.beginPath();
        for (let i = 0; i <= 60; i++) {
          const t = (i / 60) * tFlight;
          const px = originX + vx0 * t * scale;
          const py = groundY - (vy0 * t - 0.5 * grav.g * t * t) * scale;
          if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
        ctx.setLineDash([]);

        // Previous trails
        projTrail.forEach((tr) => {
          ctx.strokeStyle = "rgba(162,229,95,0.45)";
          ctx.lineWidth = 1.8;
          ctx.beginPath();
          tr.forEach(([x, y], i) => {
            const px = originX + x * scale;
            const py = groundY - y * scale;
            if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
          });
          ctx.stroke();
        });

        // Current projectile + velocity vectors
        const tClamped = Math.min(curT, tFlight);
        const cx = vx0 * tClamped;
        const cy = Math.max(0, vy0 * tClamped - 0.5 * grav.g * tClamped * tClamped);
        const vyNow = vy0 - grav.g * tClamped;
        const px = originX + cx * scale;
        const py = groundY - cy * scale;

        drawArrow(ctx, px, py, px + vx0 * 2.2, py, "#a2e55f", "Vx");
        drawArrow(ctx, px, py, px, py - vyNow * 2.2, "#d99ab3", "Vy");

        ctx.fillStyle = "#f7f5ef";
        ctx.beginPath(); ctx.arc(px, py, 6, 0, Math.PI * 2); ctx.fill();
      };

      drawProjectile(0);

      let lastTs = 0;
      const tick = (ts) => {
        if (!projRunning) return;
        const dt = lastTs ? Math.min(0.05, (ts - lastTs) / 1000) : 0.016;
        lastTs = ts;
        projT += dt;
        const curX = vx0 * Math.min(projT, tFlight);
        const curY = Math.max(0, vy0 * Math.min(projT, tFlight) - 0.5 * grav.g * Math.min(projT, tFlight) ** 2);
        if (projTrail.length) projTrail[projTrail.length - 1].push([curX, curY]);
        drawProjectile(projT);
        if (projT >= tFlight) {
          projRunning = false;
          return;
        }
        rafId = requestAnimationFrame(tick);
      };

      body.querySelector("#proj-fire").addEventListener("click", () => {
        projT = 0;
        lastTs = 0;
        projTrail.push([[0, 0]]);
        if (projTrail.length > 4) projTrail.shift();
        projRunning = true;
        rafId = requestAnimationFrame(tick);
      });
      body.querySelector("#proj-clear").addEventListener("click", () => {
        projRunning = false;
        projTrail = [];
        projT = 0;
        drawProjectile(0);
      });
      body.querySelectorAll(".grav-btn").forEach((b) => {
        b.addEventListener("click", () => { gravIdx = Number(b.dataset.i); projRunning = false; projTrail = []; paint(); });
      });
      body.querySelector("#ang-slider").addEventListener("input", (e) => { angleDeg = Number(e.target.value); projRunning = false; paint(); });
      body.querySelector("#spd-slider").addEventListener("input", (e) => { speed0 = Number(e.target.value); projRunning = false; paint(); });

    /* ---------------- TAB 2: NEWTON FORCES & FREE BODY DIAGRAM ---------------- */
    } else if (activeTab === "forces") {
      const surf = SURFACES[surfIdx];
      const g = 9.81;
      const weight = massKg * g;
      const maxFriction = surf.mu * weight;
      const friction = Math.abs(blockV) > 0.05
        ? -Math.sign(blockV) * maxFriction
        : Math.abs(pushN) <= maxFriction
        ? -pushN
        : -Math.sign(pushN) * maxFriction;
      const fNet = pushN + friction;
      const acc = fNet / massKg;

      body.innerHTML = `
        <div class="grid-asymmetric">
          <div class="card stack">
            <div class="row-between">
              <div>
                <div class="eyebrow" style="margin-bottom:2px;">2ª Ley de Newton · Diagrama de Cuerpo Libre</div>
                <h2 style="font-size:1.3rem;margin:0;">F<sub>neta</sub> = m · a en tiempo real</h2>
              </div>
              <button id="forces-reset" class="btn btn-secondary btn-sm" type="button">${icon("refresh", 13)} Detener / Centrar</button>
            </div>
            <canvas id="forces-canvas" class="lab-canvas" width="600" height="270"></canvas>
            <div class="grid-4">
              <div class="card-flat"><div class="xs mono muted">EMPUJE</div><strong class="mono">${pushN} N</strong></div>
              <div class="card-flat"><div class="xs mono muted">FRICCIÓN MÁX</div><strong class="mono">${maxFriction.toFixed(1)} N</strong></div>
              <div class="card-flat"><div class="xs mono muted">FUERZA NETA</div><strong class="mono" style="color:var(--accent);" id="fnet-val">${fNet.toFixed(1)} N</strong></div>
              <div class="card-flat"><div class="xs mono muted">ACELERACIÓN</div><strong class="mono" id="acc-val">${acc.toFixed(2)} m/s²</strong></div>
            </div>
          </div>

          <div class="card stack">
            <div class="eyebrow" style="margin:0;">Superficie y fuerzas</div>
            <div class="segmented" style="width:fit-content;">
              ${SURFACES.map(
                (s, i) => `<button type="button" class="seg-btn ${i === surfIdx ? "active" : ""} surf-btn" data-i="${i}">${s.name.split(" ")[0]}</button>`
              ).join("")}
            </div>
            <label class="field">
              <span class="row-between"><span>Fuerza aplicada (F)</span><strong class="mono">${pushN} N</strong></span>
              <input id="push-slider" type="range" min="-60" max="60" step="1" value="${pushN}" />
            </label>
            <label class="field">
              <span class="row-between"><span>Masa del bloque (m)</span><strong class="mono">${massKg} kg</strong></span>
              <input id="mass-slider" type="range" min="1" max="15" step="1" value="${massKg}" />
            </label>
            <div class="callout callout-info small">
              <strong>Experimento clave:</strong> Poné superficie <strong>Hielo</strong>, empujá hasta tomar velocidad y luego bajá la fuerza a <strong>0 N</strong>.
              Notá cómo el bloque casi no se frena (1ª Ley: Inercia).
            </div>
          </div>
        </div>
      `;

      const canvas = body.querySelector("#forces-canvas");
      const ctx = canvas.getContext("2d");
      let lastTs = 0;

      const tickForces = (ts) => {
        const dt = lastTs ? Math.min(0.04, (ts - lastTs) / 1000) : 0.016;
        lastTs = ts;
        const w = canvas.width;
        const h = canvas.height;
        const floorY = h - 54;
        const curWeight = massKg * 9.81;
        const curMaxFr = SURFACES[surfIdx].mu * curWeight;

        let curFr = 0;
        if (Math.abs(blockV) > 0.06) {
          curFr = -Math.sign(blockV) * curMaxFr;
        } else if (Math.abs(pushN) <= curMaxFr) {
          curFr = -pushN;
          blockV = 0;
        } else {
          curFr = -Math.sign(pushN) * curMaxFr;
        }
        const curNet = pushN + curFr;
        const curAcc = curNet / massKg;
        blockV += curAcc * dt;
        // Stop cleanly if friction reversed small velocity
        if (Math.abs(pushN) <= curMaxFr && Math.abs(blockV) < 0.08) blockV = 0;
        blockX += blockV * 28 * dt;
        if (blockX > w - 50) blockX = 50;
        if (blockX < 50) blockX = w - 50;

        ctx.fillStyle = "#1e1e1c";
        ctx.fillRect(0, 0, w, h);

        // Floor
        ctx.fillStyle = "#2b2b29";
        ctx.fillRect(0, floorY, w, h - floorY);
        ctx.strokeStyle = "rgba(247,245,239,0.35)";
        ctx.beginPath(); ctx.moveTo(0, floorY); ctx.lineTo(w, floorY); ctx.stroke();

        // Block
        const bw = 54 + massKg * 2.2;
        const bh = 46 + massKg * 1.4;
        const bx = blockX - bw / 2;
        const by = floorY - bh;
        ctx.fillStyle = "#c7dfdb";
        ctx.strokeStyle = "#235e63";
        ctx.lineWidth = 2;
        ctx.fillRect(bx, by, bw, bh);
        ctx.strokeRect(bx, by, bw, bh);
        ctx.fillStyle = "#1e1e1c";
        ctx.font = "bold 12px monospace";
        ctx.textAlign = "center";
        ctx.fillText(`${massKg} kg`, blockX, by + bh / 2 + 4);
        ctx.textAlign = "left";

        // Free-Body Diagram Vector Arrows from center
        const cx = blockX;
        const cy = by + bh / 2;
        drawArrow(ctx, cx, cy, cx, cy - Math.min(72, curWeight * 0.55), "#9fb0db", "N");
        drawArrow(ctx, cx, cy, cx, cy + Math.min(48, curWeight * 0.45), "#c8bcae", "mg");
        if (Math.abs(pushN) > 0.5) drawArrow(ctx, cx, cy, cx + pushN * 1.6, cy, "#a2e55f", `F (${pushN}N)`);
        if (Math.abs(curFr) > 0.5) drawArrow(ctx, cx, cy + 12, cx + curFr * 1.6, cy + 12, "#e48787", `fr`);

        ctx.fillStyle = "#f7f5ef";
        ctx.font = "12px monospace";
        ctx.fillText(`v = ${blockV.toFixed(2)} m/s`, 16, 24);

        const fnEl = body.querySelector("#fnet-val");
        const acEl = body.querySelector("#acc-val");
        if (fnEl) fnEl.textContent = `${curNet.toFixed(1)} N`;
        if (acEl) acEl.textContent = `${curAcc.toFixed(2)} m/s²`;

        rafId = requestAnimationFrame(tickForces);
      };
      rafId = requestAnimationFrame(tickForces);

      body.querySelector("#forces-reset").addEventListener("click", () => { blockX = 300; blockV = 0; pushN = 0; paint(); });
      body.querySelectorAll(".surf-btn").forEach((b) => { b.addEventListener("click", () => { surfIdx = Number(b.dataset.i); paint(); }); });
      body.querySelector("#push-slider").addEventListener("input", (e) => { pushN = Number(e.target.value); paint(); });
      body.querySelector("#mass-slider").addEventListener("input", (e) => { massKg = Number(e.target.value); paint(); });

    /* ---------------- TAB 3: WAVES, HARMONICS & ACOUSTICS ---------------- */
    } else if (activeTab === "waves") {
      const freqNow = baseFreq * harmonicN;
      const periodMs = 1000 / freqNow;
      const lambdaAir = 343 / freqNow; // speed of sound in air ~343 m/s

      body.innerHTML = `
        <div class="grid-asymmetric">
          <div class="card stack">
            <div class="row-between">
              <div>
                <div class="eyebrow" style="margin-bottom:2px;">Acústica · Puente directo con Guitarra</div>
                <h2 style="font-size:1.3rem;margin:0;">Onda Estacionaria y Armónicos (n = ${harmonicN})</h2>
              </div>
              <button id="wave-sound-btn" class="btn ${waveSoundOn ? "btn-danger" : "btn-primary"} btn-sm" type="button">
                ${icon("volume", 14)} ${waveSoundOn ? "Silenciar tono" : "Escuchar " + freqNow + " Hz"}
              </button>
            </div>
            <canvas id="wave-canvas" class="lab-canvas" width="600" height="260"></canvas>
            <div class="grid-3">
              <div class="card-flat"><div class="xs mono muted">FRECUENCIA (f)</div><strong class="mono">${freqNow} Hz</strong></div>
              <div class="card-flat"><div class="xs mono muted">PERÍODO (T = 1/f)</div><strong class="mono">${periodMs.toFixed(2)} ms</strong></div>
              <div class="card-flat"><div class="xs mono muted">λ EN AIRE (v/f)</div><strong class="mono">${lambdaAir.toFixed(2)} m</strong></div>
            </div>
          </div>

          <div class="card stack">
            <div class="eyebrow" style="margin:0;">Parámetros de la cuerda</div>
            <label class="field">
              <span class="row-between"><span>Frecuencia fundamental (f₁)</span><strong class="mono">${baseFreq} Hz</strong></span>
              <input id="wfreq-slider" type="range" min="82" max="330" step="1" value="${baseFreq}" />
            </label>
            <div>
              <div class="xs mono muted" style="margin-bottom:6px;">ARMÓNICO DE LA CUERDA (n)</div>
              <div class="segmented">
                ${[1, 2, 3, 4]
                  .map((n) => `<button type="button" class="seg-btn ${harmonicN === n ? "active" : ""} harm-btn" data-n="${n}">n = ${n} (${n}f₁)</button>`)
                  .join("")}
              </div>
            </div>
            <label class="field">
              <span class="row-between"><span>Amplitud (Volumen)</span><strong class="mono">${waveAmp} px</strong></span>
              <input id="wamp-slider" type="range" min="10" max="64" step="2" value="${waveAmp}" />
            </label>
            <div class="callout callout-info small">
              <strong>Puente con Guitarra:</strong> Activá el audio en <strong>110 Hz (5ª cuerda La2)</strong> y cambiá a <strong>n = 2 (220 Hz)</strong>:
              aparece un nodo exacto en el medio (traste 12) y escuchás una octava exacta arriba.
            </div>
          </div>
        </div>
      `;

      const canvas = body.querySelector("#wave-canvas");
      const ctx = canvas.getContext("2d");

      const tickWave = () => {
        const w = canvas.width;
        const h = canvas.height;
        const midY = h / 2;
        const left = 36;
        const span = w - 72;
        wavePhase += 0.08 + (freqNow / 2400);

        ctx.fillStyle = "#1e1e1c";
        ctx.fillRect(0, 0, w, h);

        // Center rest string
        ctx.strokeStyle = "rgba(247,245,239,0.2)";
        ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(left, midY); ctx.lineTo(left + span, midY); ctx.stroke();
        ctx.setLineDash([]);

        // Standing wave envelope
        const env = Math.sin(wavePhase);
        ctx.strokeStyle = "#c7dfdb";
        ctx.lineWidth = 3;
        ctx.beginPath();
        for (let i = 0; i <= 140; i++) {
          const u = i / 140;
          const x = left + u * span;
          const y = midY - waveAmp * Math.sin(harmonicN * Math.PI * u) * env;
          if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();

        // Draw Nodes (fixed points)
        for (let k = 0; k <= harmonicN; k++) {
          const nx = left + (k / harmonicN) * span;
          ctx.fillStyle = "#a2e55f";
          ctx.beginPath(); ctx.arc(nx, midY, 5, 0, Math.PI * 2); ctx.fill();
        }
        ctx.fillStyle = "rgba(247,245,239,0.72)";
        ctx.font = "11px monospace";
        ctx.fillText(`Nodos (puntos quietos): ${harmonicN + 1} · Antinodos: ${harmonicN}`, 18, 22);

        rafId = requestAnimationFrame(tickWave);
      };
      rafId = requestAnimationFrame(tickWave);

      body.querySelector("#wave-sound-btn").addEventListener("click", () => { toggleWaveTone(); paint(); });
      body.querySelector("#wfreq-slider").addEventListener("input", (e) => {
        baseFreq = Number(e.target.value);
        if (waveOsc && audioCtx) waveOsc.frequency.setValueAtTime(baseFreq * harmonicN, audioCtx.currentTime);
        paint();
      });
      body.querySelectorAll(".harm-btn").forEach((b) => {
        b.addEventListener("click", () => {
          harmonicN = Number(b.dataset.n);
          if (waveOsc && audioCtx) waveOsc.frequency.setValueAtTime(baseFreq * harmonicN, audioCtx.currentTime);
          paint();
        });
      });
      body.querySelector("#wamp-slider").addEventListener("input", (e) => {
        waveAmp = Number(e.target.value);
        if (waveGain && audioCtx) waveGain.gain.setValueAtTime(Math.min(0.22, (waveAmp / 60) * 0.2), audioCtx.currentTime);
        paint();
      });

    /* ---------------- TAB 4: CONSERVATION OF ENERGY RAMP ---------------- */
    } else if (activeTab === "energy") {
      const g = 9.81;
      const totalE = rampMass * g * rampHeight;

      body.innerHTML = `
        <div class="grid-asymmetric">
          <div class="card stack">
            <div class="row-between">
              <div>
                <div class="eyebrow" style="margin-bottom:2px;">Conservación · Ep = mgh · Ek = ½mv²</div>
                <h2 style="font-size:1.3rem;margin:0;">Simulador de Energía en Rampa</h2>
              </div>
              <button id="ramp-reset" class="btn btn-primary btn-sm" type="button">${icon("refresh", 13)} Soltar desde arriba</button>
            </div>
            <canvas id="ramp-canvas" class="lab-canvas" width="600" height="250"></canvas>

            <div class="stack" style="gap:8px;">
              <div class="energy-bar-row">
                <span class="mono xs">Potencial (Ep)</span>
                <div class="energy-track"><div id="bar-ep" class="energy-fill" style="background:#9fb0db;width:100%;"></div></div>
                <span class="mono xs" id="val-ep">${totalE.toFixed(1)} J</span>
              </div>
              <div class="energy-bar-row">
                <span class="mono xs">Cinética (Ek)</span>
                <div class="energy-track"><div id="bar-ek" class="energy-fill" style="background:#a2e55f;width:0%;"></div></div>
                <span class="mono xs" id="val-ek">0.0 J</span>
              </div>
              <div class="energy-bar-row">
                <span class="mono xs">Térmica (Calor)</span>
                <div class="energy-track"><div id="bar-th" class="energy-fill" style="background:#dfa072;width:0%;"></div></div>
                <span class="mono xs" id="val-th">0.0 J</span>
              </div>
              <div class="energy-bar-row">
                <span class="mono xs"><strong>Total (E)</strong></span>
                <div class="energy-track"><div class="energy-fill" style="background:var(--accent);width:100%;"></div></div>
                <span class="mono xs"><strong>${totalE.toFixed(1)} J</strong></span>
              </div>
            </div>
          </div>

          <div class="card stack">
            <div class="eyebrow" style="margin:0;">Parámetros del sistema</div>
            <div class="segmented" style="width:fit-content;">
              <button type="button" class="seg-btn ${!rampFriction ? "active" : ""} rfr-btn" data-f="0">Sin fricción (Ideal)</button>
              <button type="button" class="seg-btn ${rampFriction ? "active" : ""} rfr-btn" data-f="1">Con fricción</button>
            </div>
            <label class="field">
              <span class="row-between"><span>Masa (m)</span><strong class="mono">${rampMass} kg</strong></span>
              <input id="rmass-slider" type="range" min="1" max="10" step="1" value="${rampMass}" />
            </label>
            <label class="field">
              <span class="row-between"><span>Altura inicial (h)</span><strong class="mono">${rampHeight.toFixed(1)} m</strong></span>
              <input id="rheight-slider" type="range" min="1" max="6" step="0.5" value="${rampHeight}" />
            </label>
            <div class="callout callout-info small">
              <strong>Observación clave:</strong> Aunque actives la fricción y la esfera se frene al fondo,
              la barra <strong>Total</strong> jamás cambia: toda la energía mecánica perdida pasó a ser <strong>Térmica</strong>.
            </div>
          </div>
        </div>
      `;

      const canvas = body.querySelector("#ramp-canvas");
      const ctx = canvas.getContext("2d");
      let lastTs = 0;

      const tickRamp = (ts) => {
        const dt = lastTs ? Math.min(0.035, (ts - lastTs) / 1000) : 0.016;
        lastTs = ts;
        const w = canvas.width;
        const h = canvas.height;
        const total = rampMass * 9.81 * rampHeight;

        // Simple harmonic / parabolic track dynamics
        const omega2 = 3.2;
        const damping = rampFriction ? 0.42 : 0.0;
        const acc = -omega2 * rampPos - damping * rampVel;
        rampVel += acc * dt;
        rampPos += rampVel * dt;
        if (rampPos > 1) { rampPos = 1; rampVel = -Math.abs(rampVel); }
        if (rampPos < -1) { rampPos = -1; rampVel = Math.abs(rampVel); }

        const normH = Math.min(1, rampPos * rampPos);
        const ep = total * normH;
        const mechFrac = rampFriction ? Math.min(1, normH + (rampVel * rampVel) / omega2) : 1.0;
        const ek = Math.max(0, total * mechFrac - ep);
        thermalJ = Math.max(0, total - ep - ek);

        // Draw track
        ctx.fillStyle = "#1e1e1c";
        ctx.fillRect(0, 0, w, h);

        const padX = 56;
        const bottomY = h - 32;
        const topY = 36 + (6 - rampHeight) * 18;
        const trackH = bottomY - topY;
        const toCanvas = (u) => [padX + ((u + 1) / 2) * (w - padX * 2), bottomY - u * u * trackH];

        ctx.strokeStyle = "#c7dfdb";
        ctx.lineWidth = 3.5;
        ctx.beginPath();
        for (let i = 0; i <= 80; i++) {
          const u = -1 + (i / 80) * 2;
          const [px, py] = toCanvas(u);
          if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();

        const [bx, by] = toCanvas(rampPos);
        ctx.fillStyle = "#a2e55f";
        ctx.beginPath(); ctx.arc(bx, by - 10, 10, 0, Math.PI * 2); ctx.fill();

        // Update energy bars
        const bEp = body.querySelector("#bar-ep");
        const bEk = body.querySelector("#bar-ek");
        const bTh = body.querySelector("#bar-th");
        if (bEp) bEp.style.width = `${(ep / total) * 100}%`;
        if (bEk) bEk.style.width = `${(ek / total) * 100}%`;
        if (bTh) bTh.style.width = `${(thermalJ / total) * 100}%`;
        const vEp = body.querySelector("#val-ep");
        const vEk = body.querySelector("#val-ek");
        const vTh = body.querySelector("#val-th");
        if (vEp) vEp.textContent = `${ep.toFixed(1)} J`;
        if (vEk) vEk.textContent = `${ek.toFixed(1)} J`;
        if (vTh) vTh.textContent = `${thermalJ.toFixed(1)} J`;

        rafId = requestAnimationFrame(tickRamp);
      };
      rafId = requestAnimationFrame(tickRamp);

      const resetRamp = () => { rampPos = -1.0; rampVel = 0; thermalJ = 0; };
      body.querySelector("#ramp-reset").addEventListener("click", () => { resetRamp(); paint(); });
      body.querySelectorAll(".rfr-btn").forEach((b) => {
        b.addEventListener("click", () => { rampFriction = b.dataset.f === "1"; resetRamp(); paint(); });
      });
      body.querySelector("#rmass-slider").addEventListener("input", (e) => { rampMass = Number(e.target.value); resetRamp(); paint(); });
      body.querySelector("#rheight-slider").addEventListener("input", (e) => { rampHeight = Number(e.target.value); resetRamp(); paint(); });

    /* ---------------- TAB 5: FLUIDS, ARCHIMEDES & HYDROSTATIC PRESSURE ---------------- */
    } else if (activeTab === "fluids") {
      const obj = FLUID_OBJECTS[fluidObjIdx];
      const liq = FLUID_LIQUIDS[fluidLiqIdx];
      const g = 9.81;
      const volM3 = fluidVolL / 1000;
      const massObj = obj.rho * volM3;
      const weightN = massObj * g;
      const floats = obj.rho <= liq.rho;
      const subFrac = floats ? obj.rho / liq.rho : 1.0;
      const buoyancyN = liq.rho * (volM3 * subFrac) * g;
      const pAtm = 1 + (liq.rho * g * diveDepthM) / 101325;
      const pKpa = 101.325 + (liq.rho * g * diveDepthM) / 1000;

      body.innerHTML = `
        <div class="grid-asymmetric">
          <div class="card stack">
            <div class="row-between">
              <div>
                <div class="eyebrow" style="margin-bottom:2px;">Arquímedes y Presión Hidrostática</div>
                <h2 style="font-size:1.3rem;margin:0;">${esc(obj.name)} en ${esc(liq.name)} — ${floats ? "Flota" : "Se hunde"}</h2>
              </div>
              <span class="pill ${floats ? "pill-green" : "pill-amber"}">
                ${floats ? `${Math.round(subFrac * 100)}% sumergido` : "100% sumergido (fondo)"}
              </span>
            </div>
            <canvas id="fluids-canvas" class="lab-canvas" width="600" height="280"></canvas>
            <div class="grid-4">
              <div class="card-flat">
                <div class="xs mono muted">PESO (mg)</div>
                <strong class="mono">${weightN.toFixed(1)} N</strong>
              </div>
              <div class="card-flat">
                <div class="xs mono muted">EMPUJE (E)</div>
                <strong class="mono">${buoyancyN.toFixed(1)} N</strong>
              </div>
              <div class="card-flat">
                <div class="xs mono muted">PRESIÓN A ${diveDepthM} m</div>
                <strong class="mono">${pAtm.toFixed(2)} atm</strong>
              </div>
              <div class="card-flat">
                <div class="xs mono muted">EN KILOPASCALES</div>
                <strong class="mono">${pKpa.toFixed(0)} kPa</strong>
              </div>
            </div>
          </div>

          <div class="card stack">
            <div class="eyebrow" style="margin:0;">Material y líquido</div>
            <label class="field">
              <span>Objeto (densidad ρ)</span>
              <select id="fluid-obj-sel">
                ${FLUID_OBJECTS.map((o, i) => `<option value="${i}" ${i === fluidObjIdx ? "selected" : ""}>${esc(o.name)} (${o.rho} kg/m³)</option>`).join("")}
              </select>
            </label>
            <label class="field">
              <span>Líquido del tanque</span>
              <select id="fluid-liq-sel">
                ${FLUID_LIQUIDS.map((l, i) => `<option value="${i}" ${i === fluidLiqIdx ? "selected" : ""}>${esc(l.name)} (${l.rho} kg/m³)</option>`).join("")}
              </select>
            </label>
            <label class="field">
              <span class="row-between"><span>Volumen del bloque</span><strong class="mono">${fluidVolL} L (${massObj.toFixed(1)} kg)</strong></span>
              <input id="fluid-vol-slider" type="range" min="2" max="25" step="1" value="${fluidVolL}" />
            </label>
            <label class="field">
              <span class="row-between"><span>Profundidad del buzo (h)</span><strong class="mono">${diveDepthM} m</strong></span>
              <input id="fluid-depth-slider" type="range" min="0" max="30" step="1" value="${diveDepthM}" />
            </label>
            <div class="callout callout-info small">
              <strong>Probá esto:</strong> poné <strong>Hielo</strong> en <strong>Agua dulce</strong> (90% bajo el agua, como un iceberg) y después poné <strong>Acero</strong> en <strong>Mercurio</strong> para ver por qué el metal flota en un líquido más denso.
            </div>
          </div>
        </div>
      `;

      const canvas = body.querySelector("#fluids-canvas");
      const ctx = canvas.getContext("2d");
      const w = canvas.width;
      const h = canvas.height;
      const surfaceY = 82;
      const floorY = h - 22;

      ctx.fillStyle = "#1e1e1c";
      ctx.fillRect(0, 0, w, h);

      // Liquid body
      ctx.fillStyle = liq.color;
      ctx.fillRect(24, surfaceY, w - 48, floorY - surfaceY);
      ctx.strokeStyle = "rgba(247,245,239,0.45)";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(24, surfaceY);
      ctx.lineTo(w - 24, surfaceY);
      ctx.stroke();

      // Tank walls
      ctx.strokeStyle = "rgba(247,245,239,0.28)";
      ctx.beginPath();
      ctx.moveTo(24, 34);
      ctx.lineTo(24, floorY);
      ctx.lineTo(w - 24, floorY);
      ctx.lineTo(w - 24, 34);
      ctx.stroke();

      // Depth gauge on right side
      const depthPx = surfaceY + (diveDepthM / 30) * (floorY - surfaceY - 12);
      ctx.strokeStyle = "rgba(247,245,239,0.5)";
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(w - 150, depthPx);
      ctx.lineTo(w - 30, depthPx);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f7f5ef";
      ctx.font = "11px monospace";
      ctx.fillText(`h = ${diveDepthM} m → ${pAtm.toFixed(2)} atm`, w - 188, depthPx - 6);

      // Floating or sunken block
      const side = Math.round(52 + fluidVolL * 1.6);
      const bx = 170 - side / 2;
      const by = floats ? surfaceY - side * (1 - subFrac) : floorY - side;
      ctx.fillStyle = obj.color;
      ctx.strokeStyle = "#f7f5ef";
      ctx.lineWidth = 1.8;
      ctx.fillRect(bx, by, side, side);
      ctx.strokeRect(bx, by, side, side);

      ctx.fillStyle = "#161615";
      ctx.font = "bold 11px monospace";
      ctx.textAlign = "center";
      ctx.fillText(`${obj.rho} kg/m³`, bx + side / 2, by + side / 2 + 4);
      ctx.textAlign = "left";

      // Force arrows (Weight down, Buoyancy up)
      const cx = bx + side / 2;
      const cy = by + side / 2;
      const maxForce = Math.max(weightN, buoyancyN, 1);
      const wLen = Math.max(22, (weightN / maxForce) * 68);
      const bLen = Math.max(22, (buoyancyN / maxForce) * 68);
      drawArrow(ctx, cx - 10, cy, cx - 10, cy + wLen, "#ea9089", `mg (${weightN.toFixed(0)}N)`);
      drawArrow(ctx, cx + 10, cy, cx + 10, cy - bLen, "#a2e55f", `E (${buoyancyN.toFixed(0)}N)`);

      ctx.fillStyle = "rgba(247,245,239,0.75)";
      ctx.font = "11px monospace";
      ctx.fillText(`Aire (1.00 atm)`, 36, 26);
      ctx.fillText(`${liq.name} (${liq.rho} kg/m³)`, 36, floorY - 8);

      body.querySelector("#fluid-obj-sel").addEventListener("change", (e) => { fluidObjIdx = Number(e.target.value); paint(); });
      body.querySelector("#fluid-liq-sel").addEventListener("change", (e) => { fluidLiqIdx = Number(e.target.value); paint(); });
      body.querySelector("#fluid-vol-slider").addEventListener("input", (e) => { fluidVolL = Number(e.target.value); paint(); });
      body.querySelector("#fluid-depth-slider").addEventListener("input", (e) => { diveDepthM = Number(e.target.value); paint(); });

    /* ---------------- TAB 6: OPTICS, SNELL'S LAW & TOTAL INTERNAL REFLECTION ---------------- */
    } else if (activeTab === "optics") {
      const m1 = OPTIC_MEDIA[opticMed1];
      const m2 = OPTIC_MEDIA[opticMed2];
      const th1 = (incAngleDeg * Math.PI) / 180;
      const sin2 = (m1.n / m2.n) * Math.sin(th1);
      const isTIR = sin2 > 1.0;
      const th2Deg = isTIR ? null : (Math.asin(sin2) * 180) / Math.PI;
      const critDeg = m1.n > m2.n ? (Math.asin(m2.n / m1.n) * 180) / Math.PI : null;
      const v1 = 300000 / m1.n;
      const v2 = 300000 / m2.n;

      body.innerHTML = `
        <div class="grid-asymmetric">
          <div class="card stack">
            <div class="row-between">
              <div>
                <div class="eyebrow" style="margin-bottom:2px;">Ley de Snell · n₁·sen(θ₁) = n₂·sen(θ₂)</div>
                <h2 style="font-size:1.3rem;margin:0;">${isTIR ? "Reflexión Interna Total (Fibra óptica)" : "Refracción y Reflexión de la Luz"}</h2>
              </div>
              <span class="pill ${isTIR ? "pill-green" : "pill-accent"}">
                ${isTIR ? "100% reflejado" : `θ₂ = ${th2Deg.toFixed(1)}°`}
              </span>
            </div>
            <canvas id="optics-canvas" class="lab-canvas" width="600" height="290"></canvas>
            <div class="grid-4">
              <div class="card-flat">
                <div class="xs mono muted">ÁNGULO ENTRADA</div>
                <strong class="mono">${incAngleDeg}°</strong>
              </div>
              <div class="card-flat">
                <div class="xs mono muted">ÁNGULO SALIDA</div>
                <strong class="mono">${isTIR ? "No sale (TIR)" : `${th2Deg.toFixed(1)}°`}</strong>
              </div>
              <div class="card-flat">
                <div class="xs mono muted">ÁNGULO CRÍTICO</div>
                <strong class="mono">${critDeg ? `${critDeg.toFixed(1)}°` : "No existe"}</strong>
              </div>
              <div class="card-flat">
                <div class="xs mono muted">VELOCIDAD v₁ / v₂</div>
                <strong class="mono">${Math.round(v1 / 1000)}k / ${Math.round(v2 / 1000)}k</strong>
              </div>
            </div>
          </div>

          <div class="card stack">
            <div class="eyebrow" style="margin:0;">Medios y rayo láser</div>
            <label class="field">
              <span>Medio 1 (de donde viene el láser)</span>
              <select id="opt-m1">
                ${OPTIC_MEDIA.map((m, i) => `<option value="${i}" ${i === opticMed1 ? "selected" : ""}>${esc(m.name)} (n = ${m.n.toFixed(2)})</option>`).join("")}
              </select>
            </label>
            <label class="field">
              <span>Medio 2 (hacia donde intenta pasar)</span>
              <select id="opt-m2">
                ${OPTIC_MEDIA.map((m, i) => `<option value="${i}" ${i === opticMed2 ? "selected" : ""}>${esc(m.name)} (n = ${m.n.toFixed(2)})</option>`).join("")}
              </select>
            </label>
            <label class="field">
              <span class="row-between"><span>Ángulo de incidencia (θ₁)</span><strong class="mono">${incAngleDeg}°</strong></span>
              <input id="opt-angle-slider" type="range" min="0" max="85" step="1" value="${incAngleDeg}" />
            </label>
            <div class="callout callout-info small">
              <strong>Experimento de fibra óptica:</strong> con <strong>Vidrio → Aire</strong>, arrastrá el ángulo por encima de <strong>41.8°</strong>. El rayo deja de escapar y rebota al 100% adentro: así viaja internet por fibra óptica.
            </div>
          </div>
        </div>
      `;

      const canvas = body.querySelector("#optics-canvas");
      const ctx = canvas.getContext("2d");
      const w = canvas.width;
      const h = canvas.height;
      const cx = w / 2;
      const midY = h / 2;

      ctx.fillStyle = "#1e1e1c";
      ctx.fillRect(0, 0, w, h);

      // Top medium (m1) and bottom medium (m2)
      ctx.fillStyle = m1.tint;
      ctx.fillRect(0, 0, w, midY);
      ctx.fillStyle = m2.tint;
      ctx.fillRect(0, midY, w, h - midY);

      // Interface & normal line
      ctx.strokeStyle = "rgba(247,245,239,0.5)";
      ctx.lineWidth = 1.6;
      ctx.beginPath();
      ctx.moveTo(0, midY);
      ctx.lineTo(w, midY);
      ctx.stroke();

      ctx.strokeStyle = "rgba(247,245,239,0.28)";
      ctx.setLineDash([5, 5]);
      ctx.beginPath();
      ctx.moveTo(cx, 16);
      ctx.lineTo(cx, h - 16);
      ctx.stroke();
      ctx.setLineDash([]);

      const rayLen = 132;
      // Incident ray (top-left -> center)
      const ix = cx - rayLen * Math.sin(th1);
      const iy = midY - rayLen * Math.cos(th1);
      drawArrow(ctx, ix, iy, cx, midY, "#a2e55f", "");

      // Reflected ray (center -> top-right)
      const rx = cx + rayLen * Math.sin(th1);
      const ry = midY - rayLen * Math.cos(th1);
      drawArrow(ctx, cx, midY, rx, ry, isTIR ? "#a2e55f" : "rgba(162,229,95,0.45)", isTIR ? "100% TIR" : "reflejado");

      // Refracted ray (center -> bottom-right) if not TIR
      if (!isTIR) {
        const th2 = (th2Deg * Math.PI) / 180;
        const tx = cx + rayLen * Math.sin(th2);
        const ty = midY + rayLen * Math.cos(th2);
        drawArrow(ctx, cx, midY, tx, ty, "#d99ab3", `θ₂=${th2Deg.toFixed(1)}°`);
      }

      ctx.fillStyle = "#f7f5ef";
      ctx.font = "11px monospace";
      ctx.fillText(`Medio 1: ${m1.name} (n = ${m1.n.toFixed(2)})`, 16, 24);
      ctx.fillText(`Medio 2: ${m2.name} (n = ${m2.n.toFixed(2)})`, 16, h - 16);
      ctx.fillStyle = "rgba(247,245,239,0.65)";
      ctx.fillText("Normal", cx + 6, 26);

      body.querySelector("#opt-m1").addEventListener("change", (e) => { opticMed1 = Number(e.target.value); paint(); });
      body.querySelector("#opt-m2").addEventListener("change", (e) => { opticMed2 = Number(e.target.value); paint(); });
      body.querySelector("#opt-angle-slider").addEventListener("input", (e) => { incAngleDeg = Number(e.target.value); paint(); });
    }
  };

  paint();
}
