import { icon } from "../icons.js";
import { api, esc, toast } from "../main.js";
import { renderCircuitLab } from "./circuit_lab.js";
import { renderArduinoLab } from "./arduino_lab.js";

const LED_PRESETS = [
  { name: "Rojo", vf: 2.0, color: "#c94444" },
  { name: "Amarillo", vf: 2.1, color: "#cfa332" },
  { name: "Verde", vf: 2.2, color: "#2d8f66" },
  { name: "Azul", vf: 3.0, color: "#3b76b8" },
  { name: "Blanco", vf: 3.2, color: "#eef2f1" },
];

const E12_VALUES = [
  10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82,
  100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820,
  1000, 1200, 1500, 1800, 2200, 2700, 3300, 4700, 10000,
];

const BAND_COLORS = [
  { name: "Negro", hex: "#1b1b19" },
  { name: "Marrón", hex: "#85441b" },
  { name: "Rojo", hex: "#c83333" },
  { name: "Naranja", hex: "#e07224" },
  { name: "Amarillo", hex: "#d9b326" },
  { name: "Verde", hex: "#248249" },
  { name: "Azul", hex: "#2d60b5" },
  { name: "Violeta", hex: "#6f44a8" },
  { name: "Gris", hex: "#6e6c69" },
  { name: "Blanco", hex: "#f5f4ee" },
];

function formatOhms(ohms) {
  if (ohms >= 1_000_000) return `${(ohms / 1_000_000).toFixed(ohms % 1_000_000 === 0 ? 0 : 1)} MΩ`;
  if (ohms >= 1000) return `${(ohms / 1000).toFixed(ohms % 1000 === 0 ? 0 : 1)} kΩ`;
  return `${ohms} Ω`;
}

function resistorBands(ohms) {
  let val = Math.max(10, Math.round(ohms));
  let mult = 0;
  while (val >= 100) {
    val = Math.round(val / 10);
    mult += 1;
  }
  const d1 = Math.floor(val / 10);
  const d2 = val % 10;
  return [BAND_COLORS[d1], BAND_COLORS[d2], BAND_COLORS[Math.min(mult, 6)]];
}

function renderResistorSVG(ohms, ledHex = null, safe = true, explicitBands = null) {
  const [b1, b2, b3] = explicitBands || resistorBands(ohms);
  return `
    <svg viewBox="0 0 ${ledHex ? 320 : 280} 92" width="100%" style="max-width:340px;" role="img" aria-label="Resistencia de ${formatOhms(ohms)}">
      <line x1="12" y1="45" x2="72" y2="45" stroke="#8b8882" stroke-width="4" stroke-linecap="round" />
      <line x1="210" y1="45" x2="${ledHex ? 255 : 268}" y2="45" stroke="#8b8882" stroke-width="4" stroke-linecap="round" />
      <rect x="70" y="23" width="142" height="44" rx="14" fill="#d8c3a5" stroke="#9d8563" stroke-width="1.8" />
      <rect x="92" y="23" width="14" height="44" fill="${b1.hex}" />
      <rect x="118" y="23" width="14" height="44" fill="${b2.hex}" />
      <rect x="144" y="23" width="14" height="44" fill="${b3.hex}" />
      <rect x="182" y="23" width="12" height="44" fill="#c7a54b" />
      ${ledHex ? `<circle cx="282" cy="45" r="17" fill="${ledHex}" opacity="${safe ? "0.95" : "0.3"}" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" />` : ""}
      <text x="141" y="84" text-anchor="middle" fill="currentColor" font-size="10.5" opacity="0.72" font-family="monospace">
        ${esc(b1.name)} · ${esc(b2.name)} · ${esc(b3.name)} · Dorado (±5%)
      </text>
    </svg>`;
}

const BOARDS = {
  esp32: {
    name: "ESP32 DevKit v1 (3.3V)",
    chipLabel: "ESP32\nWROOM-32\nWi-Fi + BLE\nLógica 3.3V",
    left: [
      { pin: "3V3", tag: "PWR", cls: "pwr", info: "Salida regulada de 3.3V para sensores de bajo consumo." },
      { pin: "GND", tag: "GND", cls: "gnd", info: "Tierra común (0V). Todos los módulos deben compartir GND." },
      { pin: "GPIO 34", tag: "IN-ONLY", cls: "warn", info: "ADC1_CH6. SOLO ENTRADA (sin pull-up interno ni digitalWrite). Ideal para sensores analógicos incluso con Wi-Fi." },
      { pin: "GPIO 35", tag: "IN-ONLY", cls: "warn", info: "ADC1_CH7. SOLO ENTRADA. Seguro para analogRead() con Wi-Fi activo." },
      { pin: "GPIO 32", tag: "ADC1/PWM", cls: "", info: "Pin multipropósito muy confiable: entrada analógica ADC1, PWM, Touch y GPIO." },
      { pin: "GPIO 33", tag: "ADC1/PWM", cls: "", info: "Multipropósito excelente (ADC1 + GPIO + PWM)." },
      { pin: "GPIO 25", tag: "DAC/PWM", cls: "", info: "GPIO + salida analógica real (DAC1). Nota: es ADC2 (no usar analogRead con Wi-Fi)." },
      { pin: "GPIO 26", tag: "DAC/PWM", cls: "", info: "GPIO + DAC2. Evitar analogRead si Wi-Fi está encendido." },
    ],
    right: [
      { pin: "VIN (5V)", tag: "PWR", cls: "pwr", info: "Entrada 5V desde USB o fuente externa regulada. NO aplicar 5V a pines GPIO." },
      { pin: "GPIO 23", tag: "SPI MOSI", cls: "", info: "GPIO seguro y línea MOSI del bus SPI." },
      { pin: "GPIO 22", tag: "I2C SCL", cls: "", info: "Reloj I2C por defecto (SCL) para OLED y sensores BME280/MPU6050." },
      { pin: "GPIO 21", tag: "I2C SDA", cls: "", info: "Datos I2C por defecto (SDA). Par inseparable de GPIO 22." },
      { pin: "GPIO 19", tag: "SPI MISO", cls: "", info: "GPIO limpio, sin restricciones de arranque." },
      { pin: "GPIO 18", tag: "SPI SCK", cls: "", info: "GPIO limpio y reloj SPI." },
      { pin: "GPIO 4", tag: "ADC2/PWM", cls: "warn", info: "Excelente GPIO digital/PWM, pero su ADC2 falla si activás Wi-Fi." },
      { pin: "GPIO 2", tag: "LED/BOOT", cls: "warn", info: "Conectado al LED integrado azul en la mayoría de DevKits. Pin de strapping (no forzar HIGH al flashear)." },
    ],
  },
  uno: {
    name: "Arduino Uno (5V)",
    chipLabel: "ATmega328P\n16 MHz\nLógica 5V\nADC 10-bit",
    left: [
      { pin: "5V", tag: "PWR", cls: "pwr", info: "Salida regulada de 5V para alimentar protoboard y sensores." },
      { pin: "3.3V", tag: "PWR", cls: "pwr", info: "Salida 3.3V (máx ~50 mA). Cuidado: los pines digitales siguen siendo 5V." },
      { pin: "GND", tag: "GND", cls: "gnd", info: "Tierra común (0V)." },
      { pin: "A0", tag: "ADC 10b", cls: "", info: "Entrada analógica (0..1023 → 0..5V). También funciona como digital." },
      { pin: "A1", tag: "ADC 10b", cls: "", info: "Entrada analógica para potenciómetros o sensores analógicos." },
      { pin: "A4", tag: "I2C SDA", cls: "", info: "Entrada analógica y bus I2C SDA por defecto en Arduino Uno." },
      { pin: "A5", tag: "I2C SCL", cls: "", info: "Entrada analógica y bus I2C SCL por defecto." },
    ],
    right: [
      { pin: "D13", tag: "LED/SCK", cls: "", info: "Conectado al LED integrado 'L'. Ideal para tu primer Blink." },
      { pin: "D11", tag: "PWM ~", cls: "", info: "Digital + salida PWM (analogWrite 0..255)." },
      { pin: "D10", tag: "PWM ~", cls: "", info: "Digital + PWM + SPI SS." },
      { pin: "D9", tag: "PWM ~", cls: "", info: "Digital + PWM. Ideal para servos y dimmers LED." },
      { pin: "D4", tag: "GPIO", cls: "", info: "Pin digital limpio para pulsadores (INPUT_PULLUP) o relés." },
      { pin: "D2", tag: "INT0", cls: "", info: "Soporta interrupciones externas hardware (attachInterrupt)." },
      { pin: "D0 / D1", tag: "RX/TX", cls: "warn", info: "Usados por USB/Serial Monitor. Evitá conectar cosas aquí o fallará la carga del código." },
    ],
  },
};

const PARSONS_CHALLENGES = {
  millis: {
    label: "Reto 01 · millis()",
    title: "Parson's Problem: Parpadeo sin delay() usando millis()",
    goal: "Ordená las líneas para que el LED cambie de estado cada 500 ms sin congelar el resto del loop().",
    correct: [
      "unsigned long ahora = millis();",
      "if (ahora - ultimoCambio >= 500) {",
      "  ultimoCambio = ahora;",
      "  estadoLed = !estadoLed;",
      "  digitalWrite(LED_PIN, estadoLed);",
      "}",
    ],
    initial: [2, 0, 4, 1, 5, 3],
    hint: "Primero leés millis(), luego comparás con if, actualizás ultimoCambio y al final conmutás el LED.",
  },
  pullup: {
    label: "Reto 02 · INPUT_PULLUP",
    title: "Parson's Problem: Botón confiable con INPUT_PULLUP",
    goal: "Ordená la inicialización y lectura de un botón conectado a GND para encender el LED solo al presionarlo.",
    correct: [
      "pinMode(BTN_PIN, INPUT_PULLUP);",
      "pinMode(LED_PIN, OUTPUT);",
      "int estado = digitalRead(BTN_PIN);",
      "if (estado == LOW) {",
      "  digitalWrite(LED_PIN, HIGH);",
      "}",
    ],
    initial: [2, 4, 0, 3, 1, 5],
    hint: "Primero configurás los dos pinMode (entrada pull-up y salida), luego leés digitalRead y verificás si es LOW.",
  },
};

const DEBUG_QUIZZES = [
  {
    id: "floating-pin",
    title: "Diagnóstico 01 · Botón fantasma",
    scenario: "Conectaste un botón entre GPIO 4 y 3.3V con pinMode(4, INPUT). Sin tocarlo, el Monitor Serial alterna entre 0 y 1.",
    options: [
      { text: "Falta delay(1000) dentro del loop()", ok: false, why: "delay() no estabiliza un pin eléctricamente abierto." },
      { text: "El pin está flotante: conectá a GND y usá pinMode(4, INPUT_PULLUP)", ok: true, why: "Exacto: la resistencia pull-up interna fija el pin en HIGH hasta que presionás a GND (LOW)." },
      { text: "El ESP32 necesita 5V en GPIO 4 para leer HIGH", ok: false, why: "Peligro: 5V puede dañar un GPIO del ESP32 (su lógica es 3.3V)." },
    ],
  },
  {
    id: "adc2-wifi",
    title: "Diagnóstico 02 · Sensor analógico y Wi-Fi (ESP32)",
    scenario: "Tu potenciómetro en GPIO 4 funcionaba perfecto, pero al agregar WiFi.begin() dejó de devolver lecturas válidas.",
    options: [
      { text: "GPIO 4 pertenece a ADC2 (conflicto con Wi-Fi); mudalo a ADC1 (ej. GPIO 32 o 34)", ok: true, why: "Exacto: es uno de los errores más frecuentes en ESP32. ADC1 (GPIO 32–39) opera sin conflictos con Wi-Fi." },
      { text: "analogRead() no existe en ESP32", ok: false, why: "Sí existe y entrega 12 bits (0–4095)." },
      { text: "Hay que cambiar Serial.begin(115200) a 9600", ok: false, why: "El baud rate solo afecta el texto en el Monitor Serial." },
    ],
  },
  {
    id: "baud-mismatch",
    title: "Diagnóstico 03 · Caracteres ilegibles en Monitor Serial",
    scenario: "Tu sketch llama a Serial.begin(115200) pero al abrir el Monitor Serial solo aparecen símbolos raros (x⸮).",
    options: [
      { text: "La placa se quemó por sobrecorriente", ok: false, why: "Si imprime caracteres, la placa y el USB funcionan bien." },
      { text: "El Monitor Serial está configurado a otra velocidad (ej. 9600 baud) en vez de 115200", ok: true, why: "Exacto: ambos extremos (código y Monitor Serial) deben coincidir exactamente en baud rate." },
      { text: "Falta conectar una resistencia de 10kΩ al cable USB", ok: false, why: "El cable USB ya maneja la comunicación diferencial internamente." },
    ],
  },
];

const TROUBLESHOOT_STEPS = [
  { step: "1. Alimentación y cable USB", check: "¿Enciende el LED de encendido (PWR) de la placa? Probá otro cable USB (muchos son solo carga, sin datos)." },
  { step: "2. Tierra común (GND) y polaridad", check: "¿Todos los sensores y fuentes comparten el mismo GND? En LEDs, la pata larga es ánodo (+) y el lado plano es cátodo (-)." },
  { step: "3. Voltaje lógico y pines especiales", check: "En ESP32: ¿estás usando 3.3V (nunca 5V en GPIO), evitando GPIO 34–39 como salida y usando ADC1 con Wi-Fi?" },
  { step: "4. Rayos X con Serial.println()", check: "Agregá Serial.begin(115200) y logueá el valor crudo del sensor/botón antes de cualquier if() para separar fallo hardware vs. software." },
  { step: "5. Aislamiento en un simulador", check: "Reproducí solo el componente que falla en el Arduino virtual (o en un proyecto limpio de Wokwi si es algo propio del ESP32): si en el simulador funciona, el fallo está en el cableado o en un componente físico." },
];

const SPIRAL_PROJECT = [
  {
    id: "v1",
    phase: "Iteración 01 · Fundamentos (GPIO)",
    title: "Blink SOS + Diagnóstico por Serial Monitor",
    wokwi: "https://wokwi.com/projects/new/esp32",
    arduino: "serial-blink",
    tasks: [
      "Simular LED + resistencia 220Ω en el Arduino virtual (D13) o en Wokwi (GPIO 2 del ESP32)",
      "Imprimir cada estado en Serial.println() a 115200 baud",
      "Pasar el circuito a protoboard física verificando polaridad del LED (pata larga = ánodo +)",
    ],
    code: `const int LED_PIN = 2; // GPIO 2 en ESP32 (Pin 13 en Arduino Uno)

void setup() {
  Serial.begin(115200);       // Misma velocidad que el Monitor Serial
  pinMode(LED_PIN, OUTPUT);   // Sin esto el pin queda en entrada
}

void loop() {
  digitalWrite(LED_PIN, HIGH);
  Serial.println("LED ON");
  delay(500);
  digitalWrite(LED_PIN, LOW);
  Serial.println("LED OFF");
  delay(500);
}`,
  },
  {
    id: "v2",
    phase: "Iteración 02 · Interacción (INPUT_PULLUP + PWM)",
    title: "Botón confiable + Dimmer con Potenciómetro",
    wokwi: "https://wokwi.com/projects/new/esp32",
    arduino: "dimmer",
    tasks: [
      "Leer pulsador con INPUT_PULLUP (sin lecturas fantasma)",
      "Leer potenciómetro en ADC1 (GPIO 34 en ESP32 / A0 en Uno)",
      "Mapear lectura a brillo PWM usando código no bloqueante (millis())",
    ],
    code: `const int BTN_PIN = 4;   // Pulsador entre GPIO 4 y GND
const int POT_PIN = 34;  // ADC1 seguro incluso con Wi-Fi
const int LED_PIN = 2;

void setup() {
  Serial.begin(115200);
  pinMode(BTN_PIN, INPUT_PULLUP); // Suelto=HIGH, Presionado=LOW
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  bool activo = (digitalRead(BTN_PIN) == LOW);
  int crudo = analogRead(POT_PIN);             // 0..4095 en ESP32
  int brillo = map(crudo, 0, 4095, 0, 255);    // Escalar a PWM 8-bit
  analogWrite(LED_PIN, activo ? brillo : 0);
}`,
  },
  {
    id: "v3",
    phase: "Iteración 03 · Bus I2C (Estación Meteorológica v1)",
    title: "Sensor DHT22 / BME280 + Pantalla OLED SSD1306",
    wokwi: "https://wokwi.com/projects/new/esp32",
    tasks: [
      "Correr un I2C Scanner y confirmar dirección del OLED (usualmente 0x3C)",
      "Unir todas las tierras (GND) en común y alimentar a 3.3V",
      "Mostrar temperatura y humedad actualizadas cada 2s sin delay()",
    ],
    code: `#include <Wire.h>
// I2C Scanner mínimo: corre esto primero si tu OLED o sensor no responde
void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22); // SDA=21, SCL=22 en ESP32 (A4, A5 en Uno)
  Serial.println("Escaneando bus I2C...");
  for (byte addr = 1; addr < 127; addr++) {
    Wire.beginTransmission(addr);
    if (Wire.endTransmission() == 0) {
      Serial.print("Dispositivo detectado en 0x");
      Serial.println(addr, HEX);
    }
  }
}
void loop() {}`,
  },
  {
    id: "v4",
    phase: "Iteración 04 · ESP32 IoT (Estación v2)",
    title: "Servidor Web Local Wi-Fi + Alerta Automática",
    wokwi: "https://wokwi.com/projects/new/esp32",
    tasks: [
      "Conectar a Wi-Fi ('Wokwi-GUEST' en simulador o tu red local en hardware real)",
      "Servir página HTML liviana con la temperatura en vivo desde la IP del ESP32",
      "Reto abierto: encender alerta visual o sonora cuando supere tu umbral",
    ],
    code: `#include <WiFi.h>
const char* SSID = "Wokwi-GUEST"; // Cambiá por tu Wi-Fi en hardware real
const char* PASS = "";

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(SSID, PASS);
  unsigned long inicio = millis();
  while (WiFi.status() != WL_CONNECTED && millis() - inicio < 15000) {
    delay(300); Serial.print(".");
  }
  Serial.print("\\nIP asignada: ");
  Serial.println(WiFi.localIP());
}
void loop() {}`,
  },
];

export async function renderElectronicsLab(container, { tab = "ohm", practice = null, example = null } = {}) {
  let activeTab = ["ohm", "sim", "arduino", "pinout", "debug", "projects"].includes(tab) ? tab : "ohm";

  let vSource = 5.0;
  let ledIdx = 0;
  let targetMa = 15;

  let divVin = 5.0;
  let divR1 = 1000;
  let divR2 = 2000;

  // Reverse resistor decoder state (defaults to 220 ohm: Red, Red, Brown)
  let decB1 = 2;
  let decB2 = 2;
  let decMult = 1;

  let boardKey = "esp32";
  let selectedPin = BOARDS.esp32.left[2];

  let parsonsKey = "millis";
  const parsonsOrders = {
    millis: PARSONS_CHALLENGES.millis.initial.map((i) => PARSONS_CHALLENGES.millis.correct[i]),
    pullup: PARSONS_CHALLENGES.pullup.initial.map((i) => PARSONS_CHALLENGES.pullup.correct[i]),
  };
  let parsonsResult = null;
  const debugAnswers = {};
  const troubleChecks = {};

  // Project checklist lives on the server so the PC and the phone show the same progress.
  let savedChecks = {};
  try {
    const { settings } = await api.get("/api/settings");
    savedChecks = { ...(settings.ui_state?.pbl_checks || {}) };
    const legacy = JSON.parse(localStorage.getItem("aprendelab_pbl_checks") || "null");
    if (legacy && !Object.keys(savedChecks).length) {
      savedChecks = legacy;
      await api.put("/api/settings", { ui_state: { pbl_checks: savedChecks } });
    }
    if (legacy) localStorage.removeItem("aprendelab_pbl_checks");
  } catch {
    // offline or storage blocked: checklist still works for this visit
  }

  const paint = () => {
    container.innerHTML = `
      <div class="page-header band dots" data-tone="electronics">
        <div>
          <div class="breadcrumb"><a href="#/labs">Laboratorios</a> <span>/</span> <span>Electrónica</span></div>
          <h1>Electrónica</h1>
          <p>Calculá resistencias, mirá qué hace cada pin, encontrá errores y armá proyectos paso a paso.</p>
        </div>
        <a href="#/roadmap/electronica" class="btn btn-secondary btn-sm">${icon("map", 14)} Lecciones de electrónica</a>
      </div>

      <div class="tabs">
        <button class="tab-btn ${activeTab === "ohm" ? "active" : ""}" data-tab="ohm" type="button">${icon("zap", 14)} Ley de Ohm</button>
        <button class="tab-btn ${activeTab === "sim" ? "active" : ""}" data-tab="sim" type="button">${icon("activity", 14)} Simulador</button>
        <button class="tab-btn ${activeTab === "arduino" ? "active" : ""}" data-tab="arduino" type="button">${icon("code", 14)} Arduino virtual</button>
        <button class="tab-btn ${activeTab === "pinout" ? "active" : ""}" data-tab="pinout" type="button">${icon("electronics", 14)} Pines</button>
        <button class="tab-btn ${activeTab === "debug" ? "active" : ""}" data-tab="debug" type="button">${icon("bug", 14)} Encontrar el error</button>
        <button class="tab-btn ${activeTab === "projects" ? "active" : ""}" data-tab="projects" type="button">${icon("layers", 14)} Proyectos</button>
      </div>

      <div id="elec-tab-body"></div>
    `;

    container.querySelectorAll(".tab-btn").forEach((b) => {
      b.addEventListener("click", () => { activeTab = b.dataset.tab; paint(); });
    });

    const body = container.querySelector("#elec-tab-body");

    if (activeTab === "arduino") {
      renderArduinoLab(body, { exampleId: example });
      example = null; // only honor the deep link on first paint
      return;
    }

    if (activeTab === "sim") {
      renderCircuitLab(body, { startId: practice });
      practice = null; // only honor the deep link on first paint
      return;
    }

    if (activeTab === "ohm") {
      const led = LED_PRESETS[ledIdx];
      const vDrop = vSource - led.vf;
      const canLight = vDrop > 0.05;
      const exactR = canLight ? vDrop / (targetMa / 1000) : 0;
      const commercialR = canLight
        ? E12_VALUES.find((v) => v >= exactR) || E12_VALUES[E12_VALUES.length - 1]
        : 220;
      const realMa = canLight ? (vDrop / commercialR) * 1000 : 0;
      const powerMw = canLight ? vDrop * realMa : 0;
      const safe = canLight && realMa <= 22;

      const vOut = (divVin * divR2) / (divR1 + divR2);
      const esp32Safe = vOut <= 3.35;
      const decodedOhms = (decB1 * 10 + decB2) * Math.pow(10, decMult);

      body.innerHTML = `
        <div class="stack">
          <div class="grid-2" style="align-items:start;">
            <div class="card stack">
              <div class="eyebrow" style="margin:0;">01 / Circuito LED limitador</div>
              <h2 style="font-size:1.3rem;margin-bottom:4px;">Calculadora visual de Ley de Ohm</h2>
              <div class="segmented" style="width:fit-content;">
                <button type="button" class="seg-btn ${vSource === 3.3 ? "active" : ""} v-preset" data-v="3.3">3.3V · ESP32</button>
                <button type="button" class="seg-btn ${vSource === 5.0 ? "active" : ""} v-preset" data-v="5">5V · Arduino</button>
                <button type="button" class="seg-btn ${vSource === 9.0 ? "active" : ""} v-preset" data-v="9">9V · Batería</button>
              </div>
              <label class="field">
                <span class="row-between"><span>Voltaje de fuente</span><strong class="mono">${vSource.toFixed(1)} V</strong></span>
                <input id="v-slider" type="range" min="1.8" max="12" step="0.1" value="${vSource}" />
              </label>
              <label class="field">
                <span>Color del LED (voltaje directo V<sub>f</sub>)</span>
                <select id="led-select">
                  ${LED_PRESETS.map((l, idx) => `<option value="${idx}" ${idx === ledIdx ? "selected" : ""}>LED ${l.name} (Vf ≈ ${l.vf}V)</option>`).join("")}
                </select>
              </label>
              <label class="field">
                <span class="row-between"><span>Corriente objetivo</span><strong class="mono">${targetMa} mA</strong></span>
                <input id="ma-slider" type="range" min="3" max="25" step="1" value="${targetMa}" />
              </label>
            </div>

            <div class="card stack" style="text-align:center;">
              <div class="eyebrow" style="margin:0 auto;">Resultado y bandas de color</div>
              <div style="padding:8px 0;">${renderResistorSVG(commercialR, led.color, safe)}</div>
              ${
                !canLight
                  ? `<div class="callout callout-warn small">${icon("alert", 14)} El voltaje de fuente (${vSource.toFixed(1)}V) no alcanza a superar la caída del LED (${led.vf}V).</div>`
                  : `
                  <div class="grid-3" style="text-align:left;">
                    <div class="card-flat">
                      <div class="xs mono muted">R COMERCIAL (E12)</div>
                      <strong style="font-family:var(--font-serif);font-size:1.45rem;color:var(--accent);">${formatOhms(commercialR)}</strong>
                      <div class="xs mono muted">Exacta: ${Math.round(exactR)} Ω</div>
                    </div>
                    <div class="card-flat">
                      <div class="xs mono muted">CORRIENTE REAL</div>
                      <strong style="font-family:var(--font-serif);font-size:1.45rem;color:${safe ? "var(--ok)" : "var(--danger)"};">${realMa.toFixed(1)} mA</strong>
                      <div class="xs mono muted">Segura &le; 20 mA</div>
                    </div>
                    <div class="card-flat">
                      <div class="xs mono muted">POTENCIA EN R</div>
                      <strong style="font-family:var(--font-serif);font-size:1.45rem;">${Math.round(powerMw)} mW</strong>
                      <div class="xs mono muted">${powerMw < 180 ? "1/4 W alcanza" : "Usar 1/2 W"}</div>
                    </div>
                  </div>
                  <div class="callout callout-info small" style="text-align:left;">
                    <strong>Fórmula:</strong> R = (${vSource.toFixed(1)}V − ${led.vf}V) / ${(targetMa / 1000).toFixed(3)}A = <strong>${Math.round(exactR)} Ω</strong> → comercial: <strong>${formatOhms(commercialR)}</strong>.
                  </div>`
              }
            </div>
          </div>

          <div class="grid-2" style="align-items:start;">
            <div class="card stack">
              <div class="eyebrow" style="margin:0;">02 / Lector inverso (kit físico)</div>
              <h2 style="font-size:1.3rem;margin:0;">Bandas de color → Valor en Ohmios</h2>
              <p class="xs muted">Elegí los colores que ves en tu resistencia real para leer su valor al instante.</p>
              <div class="grid-3" style="gap:10px;">
                <label class="field">
                  <span>Banda 1</span>
                  <select id="dec-b1">
                    ${BAND_COLORS.slice(1).map((c, idx) => `<option value="${idx + 1}" ${idx + 1 === decB1 ? "selected" : ""}>${idx + 1} · ${c.name}</option>`).join("")}
                  </select>
                </label>
                <label class="field">
                  <span>Banda 2</span>
                  <select id="dec-b2">
                    ${BAND_COLORS.map((c, idx) => `<option value="${idx}" ${idx === decB2 ? "selected" : ""}>${idx} · ${c.name}</option>`).join("")}
                  </select>
                </label>
                <label class="field">
                  <span>Multiplicador</span>
                  <select id="dec-mult">
                    ${BAND_COLORS.slice(0, 6).map((c, idx) => `<option value="${idx}" ${idx === decMult ? "selected" : ""}>×10^${idx} · ${c.name}</option>`).join("")}
                  </select>
                </label>
              </div>
              <div class="row-between card-flat" style="align-items:center;">
                <div style="flex:1;max-width:240px;">${renderResistorSVG(decodedOhms, null, true, [BAND_COLORS[decB1], BAND_COLORS[decB2], BAND_COLORS[decMult]])}</div>
                <div style="text-align:right;">
                  <div class="xs mono muted">VALOR DECODIFICADO</div>
                  <div style="font-family:var(--font-serif);font-size:1.9rem;color:var(--accent);">${formatOhms(decodedOhms)}</div>
                  <div class="xs mono muted">±5% tolerancia</div>
                </div>
              </div>
            </div>

            <div class="card stack">
              <div class="row-between">
                <div>
                  <div class="eyebrow" style="margin-bottom:4px;">03 / Protección GPIO ESP32</div>
                  <h2 style="font-size:1.3rem;margin:0;">Divisor Resistivo (5V → 3.3V)</h2>
                </div>
                <span class="pill ${esp32Safe ? "pill-green" : "pill-red"}">
                  ${esp32Safe ? "Seguro (≤ 3.3V)" : "Peligro (> 3.3V)"}
                </span>
              </div>
              <label class="field">
                <span class="row-between"><span>V<sub>in</sub> (señal sensor)</span><strong class="mono">${divVin.toFixed(1)} V</strong></span>
                <input id="div-vin" type="range" min="3.3" max="12" step="0.1" value="${divVin}" />
              </label>
              <div class="grid-2" style="gap:10px;">
                <label class="field">
                  <span class="row-between"><span>R1 (superior)</span><strong class="mono">${(divR1 / 1000).toFixed(1)} kΩ</strong></span>
                  <input id="div-r1" type="range" min="500" max="10000" step="500" value="${divR1}" />
                </label>
                <label class="field">
                  <span class="row-between"><span>R2 (a GND)</span><strong class="mono">${(divR2 / 1000).toFixed(1)} kΩ</strong></span>
                  <input id="div-r2" type="range" min="500" max="10000" step="500" value="${divR2}" />
                </label>
              </div>
              <div class="card-flat row-between">
                <span class="small">Salida V<sub>out</sub>: <strong class="mono" style="font-size:1.1rem;color:${esp32Safe ? "var(--ok)" : "var(--danger)"};">${vOut.toFixed(2)} V</strong></span>
                <button id="div-preset-5v" type="button" class="btn btn-secondary btn-sm">Par 1kΩ / 2kΩ</button>
              </div>
            </div>
          </div>
        </div>
      `;

      body.querySelectorAll(".v-preset").forEach((b) => { b.addEventListener("click", () => { vSource = Number(b.dataset.v); paint(); }); });
      body.querySelector("#v-slider").addEventListener("input", (e) => { vSource = Number(e.target.value); paint(); });
      body.querySelector("#led-select").addEventListener("change", (e) => { ledIdx = Number(e.target.value); paint(); });
      body.querySelector("#ma-slider").addEventListener("input", (e) => { targetMa = Number(e.target.value); paint(); });
      body.querySelector("#dec-b1").addEventListener("change", (e) => { decB1 = Number(e.target.value); paint(); });
      body.querySelector("#dec-b2").addEventListener("change", (e) => { decB2 = Number(e.target.value); paint(); });
      body.querySelector("#dec-mult").addEventListener("change", (e) => { decMult = Number(e.target.value); paint(); });
      body.querySelector("#div-vin").addEventListener("input", (e) => { divVin = Number(e.target.value); paint(); });
      body.querySelector("#div-r1").addEventListener("input", (e) => { divR1 = Number(e.target.value); paint(); });
      body.querySelector("#div-r2").addEventListener("input", (e) => { divR2 = Number(e.target.value); paint(); });
      body.querySelector("#div-preset-5v").addEventListener("click", () => { divVin = 5.0; divR1 = 1000; divR2 = 2000; paint(); });
    } else if (activeTab === "pinout") {
      const board = BOARDS[boardKey];
      body.innerHTML = `
        <div class="stack">
          <div class="segmented" style="width:fit-content;">
            <button type="button" class="seg-btn ${boardKey === "esp32" ? "active" : ""} b-switch" data-b="esp32">ESP32 DevKit v1 (3.3V)</button>
            <button type="button" class="seg-btn ${boardKey === "uno" ? "active" : ""} b-switch" data-b="uno">Arduino Uno (5V)</button>
          </div>
          <div class="grid-2" style="align-items:start;">
            <div class="pinout-board">
              <div class="pin-col">
                ${board.left
                  .map(
                    (p, i) => `
                  <button type="button" class="pin-btn ${selectedPin.pin === p.pin ? "selected" : ""}" data-side="left" data-idx="${i}">
                    <span>${esc(p.pin)}</span>
                    <span class="pin-tag ${esc(p.cls)}">${esc(p.tag)}</span>
                  </button>`
                  )
                  .join("")}
              </div>
              <div class="board-chip">${esc(board.chipLabel).replaceAll("\n", "<br/>")}</div>
              <div class="pin-col">
                ${board.right
                  .map(
                    (p, i) => `
                  <button type="button" class="pin-btn ${selectedPin.pin === p.pin ? "selected" : ""}" data-side="right" data-idx="${i}">
                    <span class="pin-tag ${esc(p.cls)}">${esc(p.tag)}</span>
                    <span>${esc(p.pin)}</span>
                  </button>`
                  )
                  .join("")}
              </div>
            </div>

            <div class="card stack">
              <div class="row-between">
                <h2 class="mono" style="font-size:1.3rem;margin:0;">${esc(selectedPin.pin)}</h2>
                <span class="pill ${selectedPin.cls === "warn" ? "pill-amber" : selectedPin.cls === "pwr" ? "pill-red" : "pill-accent"}">${esc(selectedPin.tag)}</span>
              </div>
              <p class="secondary">${esc(selectedPin.info)}</p>
              <div class="divider"></div>
              <div class="callout callout-warn small">
                ${icon("alert", 14)} <strong>Seguridad al cablear:</strong> Desconectá el USB antes de modificar cables de alimentación, verificá 3.3V vs 5V y revisá que no haya cortocircuito entre VCC y GND.
              </div>
            </div>
          </div>
        </div>
      `;

      body.querySelectorAll(".b-switch").forEach((b) => {
        b.addEventListener("click", () => { boardKey = b.dataset.b; selectedPin = BOARDS[boardKey].left[0]; paint(); });
      });
      body.querySelectorAll(".pin-btn").forEach((b) => {
        b.addEventListener("click", () => { selectedPin = board[b.dataset.side][Number(b.dataset.idx)]; paint(); });
      });
    } else if (activeTab === "debug") {
      const challenge = PARSONS_CHALLENGES[parsonsKey];
      const order = parsonsOrders[parsonsKey];
      body.innerHTML = `
        <div class="stack">
          <div class="card stack">
            <div class="row-between">
              <div>
                <div class="eyebrow" style="margin-bottom:4px;">Andamiaje Nivel 2 · Reconstrucción de firmware</div>
                <h2 style="font-size:1.3rem;margin-bottom:4px;">${esc(challenge.title)}</h2>
                <p class="small muted" style="margin:0;">${esc(challenge.goal)}</p>
              </div>
              <div class="row">
                <div class="segmented">
                  ${Object.entries(PARSONS_CHALLENGES)
                    .map(
                      ([k, v]) =>
                        `<button type="button" class="seg-btn ${parsonsKey === k ? "active" : ""} p-switch" data-k="${k}">${esc(v.label)}</button>`
                    )
                    .join("")}
                </div>
                <button id="check-parsons" class="btn btn-primary btn-sm" type="button">${icon("check", 14)} Verificar orden</button>
              </div>
            </div>
            <div class="stack" style="gap:7px;">
              ${order
                .map(
                  (line, i) => `
                <div class="code-line-btn">
                  <span><span class="muted">${i + 1}.</span> ${esc(line)}</span>
                  <span class="row" style="gap:4px;">
                    <button type="button" class="btn btn-ghost btn-sm move-up" data-i="${i}" ${i === 0 ? "disabled" : ""}>Subir</button>
                    <button type="button" class="btn btn-ghost btn-sm move-down" data-i="${i}" ${i === order.length - 1 ? "disabled" : ""}>Bajar</button>
                  </span>
                </div>`
                )
                .join("")}
            </div>
            ${
              parsonsResult
                ? `<div class="callout ${parsonsResult.ok ? "callout-ok" : "callout-warn"} small">${parsonsResult.ok ? icon("check", 14) : icon("x", 14)} ${esc(parsonsResult.text)}</div>`
                : ""
            }
          </div>

          <div class="grid-3">
            ${DEBUG_QUIZZES.map((q) => {
              const picked = debugAnswers[q.id];
              return `
              <div class="card stack">
                <h3>${esc(q.title)}</h3>
                <p class="small secondary">${esc(q.scenario)}</p>
                <div class="stack" style="gap:8px;margin-top:auto;">
                  ${q.options
                    .map(
                      (opt, idx) => `
                    <button type="button" class="btn btn-secondary dbg-opt" data-q="${esc(q.id)}" data-idx="${idx}" style="justify-content:flex-start;text-align:left;white-space:normal;border-radius:12px;">
                      ${esc(opt.text)}
                    </button>`
                    )
                    .join("")}
                </div>
                ${
                  picked !== undefined
                    ? `<div class="callout ${q.options[picked].ok ? "callout-ok" : "callout-warn"} small">
                        ${q.options[picked].ok ? icon("check", 14) : icon("x", 14)} ${esc(q.options[picked].why)}
                       </div>`
                    : ""
                }
              </div>`;
            }).join("")}
          </div>

          <div class="card card-wash stack">
            <div>
              <div class="eyebrow" style="margin-bottom:4px;">Protocolo de Ingeniería · Troubleshooting</div>
              <h2 style="font-size:1.3rem;margin:0;">"Mi circuito no anda" — Diagnóstico en 5 pasos</h2>
            </div>
            <div class="stack" style="gap:8px;">
              ${TROUBLESHOOT_STEPS.map(
                (t, i) => `
                <label class="card-flat row" style="background:var(--bg-card);cursor:pointer;align-items:flex-start;">
                  <input type="checkbox" class="tr-chk" data-i="${i}" ${troubleChecks[i] ? "checked" : ""} style="width:auto;margin-top:3px;" />
                  <div>
                    <strong class="small" style="${troubleChecks[i] ? "text-decoration:line-through;opacity:0.65;" : ""}">${esc(t.step)}</strong>
                    <div class="xs muted">${esc(t.check)}</div>
                  </div>
                </label>`
              ).join("")}
            </div>
          </div>
        </div>
      `;

      body.querySelectorAll(".tr-chk").forEach((c) => {
        c.addEventListener("change", () => { troubleChecks[c.dataset.i] = c.checked; paint(); });
      });
      body.querySelectorAll(".p-switch").forEach((b) => {
        b.addEventListener("click", () => { parsonsKey = b.dataset.k; parsonsResult = null; paint(); });
      });
      body.querySelectorAll(".move-up").forEach((b) => {
        b.addEventListener("click", () => {
          const i = Number(b.dataset.i);
          if (i > 0) { [order[i - 1], order[i]] = [order[i], order[i - 1]]; paint(); }
        });
      });
      body.querySelectorAll(".move-down").forEach((b) => {
        b.addEventListener("click", () => {
          const i = Number(b.dataset.i);
          if (i < order.length - 1) { [order[i + 1], order[i]] = [order[i], order[i + 1]]; paint(); }
        });
      });
      body.querySelector("#check-parsons").addEventListener("click", async () => {
        const isCorrect = order.every((line, idx) => line === challenge.correct[idx]);
        if (isCorrect) {
          parsonsResult = { ok: true, text: "Orden correcto: lógica embebida sólida y limpia." };
          await api.post("/api/metrics", {
            domain_slug: "electronica",
            metric_type: "debug_solved",
            label: challenge.label,
            value: 1,
            unit: "ok",
          });
          toast(`${challenge.label} resuelto`, "ok");
        } else {
          parsonsResult = { ok: false, text: challenge.hint };
        }
        paint();
      });
      body.querySelectorAll(".dbg-opt").forEach((b) => {
        b.addEventListener("click", async () => {
          const qId = b.dataset.q;
          const idx = Number(b.dataset.idx);
          debugAnswers[qId] = idx;
          const q = DEBUG_QUIZZES.find((x) => x.id === qId);
          if (q.options[idx].ok) {
            await api.post("/api/metrics", {
              domain_slug: "electronica",
              metric_type: "debug_solved",
              label: q.title,
              value: 1,
              unit: "ok",
            });
          }
          paint();
        });
      });
    } else if (activeTab === "projects") {
      body.innerHTML = `
        <div class="card card-wash small" style="margin-bottom:18px;">
          <strong>Currículo en Espiral (PBL Híbrido):</strong> Cada iteración incluye código base comentado para probar sin riesgo antes de armarlo en tu protoboard física. Las iteraciones 01 y 02 corren en el <strong>Arduino virtual</strong> de este laboratorio (con el circuito simulado de verdad); las de I²C y Wi-Fi necesitan un ESP32, así que van en <strong>Wokwi</strong>.
        </div>
        <div class="stack">
          ${SPIRAL_PROJECT.map((step) => {
            const doneCount = step.tasks.filter((_, i) => savedChecks[`${step.id}-${i}`]).length;
            const pct = Math.round((doneCount / step.tasks.length) * 100);
            return `
            <article class="card stack">
              <div class="row-between">
                <div>
                  <span class="pill pill-accent">${esc(step.phase)}</span>
                  <h2 style="font-size:1.3rem;margin-top:8px;">${esc(step.title)}</h2>
                </div>
                <div class="row">
                  <span class="pill ${pct === 100 ? "pill-green" : ""}">${doneCount}/${step.tasks.length}</span>
                  ${step.arduino
                    ? `<a href="#/lab/electronics?tab=arduino&ex=${esc(step.arduino)}" class="btn btn-primary btn-sm">${icon("code", 13)} Probar en el Arduino virtual</a>
                       <a href="${esc(step.wokwi)}" target="_blank" rel="noopener" class="btn btn-ghost btn-sm">Wokwi (ESP32) ${icon("arrowUpRight", 13)}</a>`
                    : `<a href="${esc(step.wokwi)}" target="_blank" rel="noopener" class="btn btn-primary btn-sm">Abrir Wokwi ${icon("arrowUpRight", 13)}</a>`}
                </div>
              </div>
              <div class="stack" style="gap:7px;">
                ${step.tasks
                  .map((t, i) => {
                    const key = `${step.id}-${i}`;
                    const checked = Boolean(savedChecks[key]);
                    return `
                    <label class="card-flat row" style="cursor:pointer;">
                      <input type="checkbox" class="pbl-check" data-key="${key}" data-title="${esc(step.title)}" ${checked ? "checked" : ""} style="width:auto;" />
                      <span class="small" style="${checked ? "text-decoration:line-through;opacity:0.65;" : ""}">${esc(t)}</span>
                    </label>`;
                  })
                  .join("")}
              </div>
              <details class="card-flat" style="padding:12px 14px;">
                <summary class="xs mono" style="cursor:pointer;font-weight:600;color:var(--accent);">Ver firmware base comentado (Arduino / ESP32)</summary>
                <div class="stack" style="margin-top:10px;gap:8px;">
                  <pre class="mono xs" style="margin:0;padding:12px;border-radius:10px;background:#1e1e1c;color:#f7f5ef;overflow-x:auto;line-height:1.5;">${esc(step.code)}</pre>
                  <div>
                    <button type="button" class="btn btn-secondary btn-sm copy-code" data-id="${step.id}">Copiar código</button>
                  </div>
                </div>
              </details>
            </article>`;
          }).join("")}
        </div>
      `;

      body.querySelectorAll(".copy-code").forEach((btn) => {
        btn.addEventListener("click", async () => {
          const step = SPIRAL_PROJECT.find((s) => s.id === btn.dataset.id);
          if (!step) return;
          try {
            await navigator.clipboard.writeText(step.code);
            toast("Código copiado al portapapeles", "ok");
          } catch {
            toast("Seleccioná y copiá el bloque manualmente", "info");
          }
        });
      });

      body.querySelectorAll(".pbl-check").forEach((chk) => {
        chk.addEventListener("change", async () => {
          savedChecks[chk.dataset.key] = chk.checked;
          api.put("/api/settings", { ui_state: { pbl_checks: savedChecks } }).catch(() => {});
          if (chk.checked) {
            await api.post("/api/metrics", {
              domain_slug: "electronica",
              metric_type: "project_step_done",
              label: chk.dataset.title,
              value: 1,
              unit: "hito",
            });
            toast("Hito de proyecto registrado", "ok");
          }
          paint();
        });
      });
    }
  };

  paint();
}
