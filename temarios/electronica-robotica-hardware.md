# Temario: Electrónica para Robótica (enfoque hardware)

**Desde cero hasta diseñar tu propia placa controladora de robot.**

- **Filosofía**: el circuito lo hacés vos, el código puede hacerlo la IA. Cada tema se trabaja en tres pasos: **calcular a mano → simular (LTspice) → armar y medir**.
- **Ritmo de referencia**: 6–10 h por semana, con una duración total de **~12–14 meses**. Si tenés más tiempo, se comprime.
- **Hardware principal**: Arduino Nano (módulos 0–7) y STM32 (Nucleo-F446RE o Black Pill F411 + ST-Link) desde el módulo 8.
- **Regla de oro**: ningún proyecto se da por terminado sin una **medición que lo respalde** (captura de osciloscopio, tabla de valores, foto).

---

## Mapa general

| # | Módulo | Duración | Placa |
|---|---|---|---|
| 0 | Laboratorio, seguridad e instrumentos | 1–2 sem | — |
| 1 | Circuitos de corriente continua | 3–4 sem | — |
| 2 | Capacitores, inductores y transitorios | 3 sem | Nano (como generador) |
| 3 | Corriente alterna, frecuencia y filtros | 3 sem | Nano |
| 4 | Diodos | 2 sem | — |
| 5 | Transistores como llave (BJT y MOSFET) | 3–4 sem | Nano |
| 6 | Motores DC y puente H | 4 sem | Nano |
| 7 | Amplificadores operacionales y sensado | 4 sem | Nano |
| 8 | Microcontrolador desde el hardware (STM32) | 3 sem | STM32 |
| 9 | Sensores y acondicionamiento de señal | 4 sem | STM32 |
| 10 | Potencia: baterías, reguladores y protección | 4 sem | STM32 |
| 11 | Motores avanzados: encoders, PID, steppers, servos | 5 sem | STM32 |
| 12 | Ruido, masas y robustez (EMC práctica) | 3 sem | STM32 |
| 13 | Soldadura y construcción | transversal | — |
| 14 | Diseño de PCB con KiCad | 6 sem | — |
| 15 | Proyecto final: robot con placa propia | 6–8 sem | Tu PCB |

---

## Módulo 0 — Laboratorio, seguridad e instrumentos

**Objetivo**: saber medir antes de saber diseñar.

### Temas
- **Seguridad**
  - Tensiones peligrosas: no se toca la red de 220 V en todo el curso.
  - Baterías LiPo: incendios, bolsa ignífuga, nunca cargarlas sin vigilancia.
  - Quemaduras con el soldador, ventilación por el humo del flux y protección ocular al cortar patas.
- **Multímetro**
  - Medir tensión en paralelo y corriente en serie, con los cables en la entrada correcta (mA/10A).
  - Resistencia y continuidad (siempre sin alimentación) y prueba de diodos.
  - El error clásico: medir corriente con los cables en paralelo y quemar el fusible.
- **Fuente de laboratorio**
  - Modo CV/CC y límite de corriente.
  - Por qué siempre se arranca con el límite bajo.
- **Osciloscopio**
  - Base de tiempo, V/div y trigger (flanco, nivel, modo normal/auto).
  - Punta x1 o x10 y compensación de punta.
  - El cable de masa: corto, y nunca conectado a un punto que no sea masa (con osciloscopio de mesa, la masa está unida a tierra).
  - Mediciones automáticas: frecuencia, Vpp, ciclo de trabajo, tiempo de subida.
- **Analizador lógico**: canales, muestreo, PulseView/sigrok.
- **Protoboard**: cómo están conectadas las filas, los rieles de alimentación y sus límites (capacitancia parásita, malos contactos, poca corriente).
- **Código de colores de resistencias**, valores E12/E24, tolerancia.
- **Lectura de datasheets (introducción)**: valores máximos absolutos frente a condiciones de operación, y dónde está el pinout.

### Prácticas
1. Medir resistencias del kit con el multímetro y comparar contra el código de colores y la tolerancia.
2. Ajustar la fuente a 5 V / 100 mA y medir la tensión con el multímetro.
3. Compensar la punta x10 con la señal de calibración del osciloscopio.
4. Medir la señal PWM de `analogWrite()` del Nano: frecuencia, ciclo de trabajo y Vpp.

### Entregable
Cuaderno de laboratorio (físico o digital) con la primera captura de osciloscopio anotada.

---

## Módulo 1 — Circuitos de corriente continua

**Objetivo**: dominar las cuentas que vas a usar todos los días.

### Temas
- Carga, corriente, tensión, potencia y energía (unidades y prefijos: µ, m, k, M).
- **Ley de Ohm** y potencia (P = V·I = I²R = V²/R), con potencia nominal de resistencias (¼ W, ½ W).
- Resistencias en serie y en paralelo.
- **Divisor de tensión** y su gran limitación: la carga lo modifica.
- Divisor de corriente.
- **Leyes de Kirchhoff** (KVL y KCL), análisis de mallas y nodos con circuitos de 2–3 mallas.
- **Thévenin y Norton**: por qué una fuente "real" tiene resistencia interna (la batería que cae de tensión con carga).
- Superposición, a nivel conceptual.
- Potenciómetros como divisor y como reóstato.
- LEDs: tensión directa, cálculo de la resistencia limitadora y LED en el pin de un micro (corriente máxima del pin).
- Pull-up y pull-down: qué es una entrada flotante y por qué un pulsador necesita uno.
- Resistencia de cables y pistas: caída de tensión en cables largos o finos.

### Prácticas
1. Divisor de tensión 12 V → 5 V: medir en vacío y con distintas cargas, y explicar la diferencia con Thévenin.
2. Medir la resistencia interna de una pila o batería: tensión en vacío contra tensión con carga conocida.
3. Resolver tres circuitos con Kirchhoff a mano, simularlos en LTspice y medirlos en protoboard. Tabla comparativa.
4. Leer el ADC del Nano con un potenciómetro y explicar por qué la lectura "baila" con una entrada flotante.

### Entregable
Tabla calculado / simulado / medido de los tres circuitos, con el error explicado.

---

## Módulo 2 — Capacitores, inductores y transitorios

**Objetivo**: entender el comportamiento en el tiempo. Un motor es una bobina y el desacople es un capacitor.

### Temas
- **Capacitor**: Q = C·V, energía almacenada y comportamiento (se opone a cambios de tensión).
  - Tipos: cerámico (X7R contra Y5V y su pérdida de capacidad con la tensión aplicada, *DC bias*), electrolítico (polaridad, ESR, vida útil) y tantalio (cuidado con los picos).
  - Tensión nominal y margen de seguridad.
- **Carga y descarga RC**: constante de tiempo τ = RC; al 63 % en 1τ y prácticamente completa en 5τ.
- **Inductor**: V = L·di/dt; se opone a cambios de corriente y almacena energía en el campo magnético.
  - **El pico inductivo**: qué pasa cuando cortás la corriente de una bobina de golpe.
- **Circuito RL**: τ = L/R y crecimiento de la corriente.
- **Capacitores de desacople**: por qué van 100 nF pegados a cada chip, más un capacitor de bulk.
- Antirrebote de pulsadores con RC.
- Introducción a ESR y ESL (los componentes reales no son ideales).

### Prácticas
1. Cargar un capacitor de 100 µF con 10 kΩ: ver la curva en el osciloscopio, medir τ y compararlo con el cálculo.
2. Rebote de un pulsador: capturarlo en el osciloscopio (modo single), agregar un RC y volver a capturar.
3. **Pico inductivo**: bobina de un relé conmutada con un transistor, **sin diodo**. Medir el pico con punta x10 (se ven decenas de voltios). Después agregar el diodo y comparar.
4. Simular RC y RL en LTspice con análisis transitorio.

### Entregable
Las dos capturas del pico inductivo (con y sin diodo) anotadas. Vas a volver a ellas en el módulo 6.

---

## Módulo 3 — Corriente alterna, frecuencia y filtros

**Objetivo**: pensar en frecuencia, porque el PWM, el ruido y los filtros se entienden así.

### Temas
- Señales periódicas: amplitud, frecuencia, período, valor medio, valor eficaz (RMS) y ciclo de trabajo.
- **El PWM como señal**: su valor medio y por qué un motor "ve" el promedio.
- Senoidales e introducción a la idea de Fourier: una cuadrada es una suma de armónicos (solo intuición, sin matemática pesada).
- **Impedancia**: X_C = 1/(2πfC) y X_L = 2πfL, con intuición de cómo cambian con la frecuencia.
- **Filtro RC pasa bajos y pasa altos**: frecuencia de corte fc = 1/(2πRC).
- **Diagrama de Bode** a nivel intuitivo: −3 dB, −20 dB/década y fase.
- Filtro RC sobre PWM para obtener una tensión analógica (un DAC "pobre"): rizado contra tiempo de respuesta.
- Filtros LC y resonancia (introducción, útil para fuentes conmutadas).
- Decibeles.

### Prácticas
1. PWM del Nano + filtro RC: medir la tensión media y el rizado con dos valores de C distintos.
2. Barrido de frecuencia de un filtro RC (con generador de funciones o PWM a varias frecuencias): medir la ganancia y graficar un Bode experimental.
3. Simular el mismo filtro en LTspice (análisis AC) y superponer los resultados.
4. Con la función FFT del osciloscopio (si la tiene), ver los armónicos de una cuadrada.

### Entregable
Bode medido contra Bode simulado en un mismo gráfico.

---

## Módulo 4 — Diodos

**Objetivo**: entender el primer componente no lineal y sus usos en robótica.

### Temas
- Unión PN, polarización directa e inversa y curva I-V.
- Parámetros del datasheet: Vf, If máxima, Vr máxima, tiempo de recuperación inversa.
- Tipos:
  - **Rectificador** (1N4007), lento.
  - **Schottky** (1N5819, SS34): Vf baja y rápido, ideal para rueda libre y protección.
  - **Señal** (1N4148).
  - **Zener**: referencia y recorte.
  - **TVS**: protección contra picos.
  - **LED**: Vf según color.
- **Diodo de rueda libre** en cargas inductivas.
- **Protección contra polaridad inversa**: diodo serie (simple, pero con pérdida) frente a MOSFET P (lo vemos en el módulo 10).
- Rectificación de media onda y onda completa con capacitor de filtro (conceptual, sin red de 220 V; con un transformador de baja tensión si tenés uno).
- Diodos de clamping para proteger entradas del micro.
- OR de alimentaciones con diodos (USB o batería).

### Prácticas
1. Curva I-V de un diodo de silicio, un Schottky y un LED: barrer la tensión con fuente y resistencia, medir y graficar.
2. Zener como referencia: medir la regulación al variar la entrada y la carga, y ver sus límites.
3. Protección de polaridad con diodo serie: medir la tensión perdida y la potencia disipada a distintas corrientes.

### Entregable
Gráfico con las tres curvas I-V superpuestas.

---

## Módulo 5 — Transistores como llave (BJT y MOSFET)

**Objetivo**: controlar cargas de potencia desde un pin del micro.

### Temas
- **BJT (NPN y PNP)**
  - Base, colector y emisor; ganancia hFE.
  - Regiones de corte, activa y saturación.
  - **Cálculo de la resistencia de base** para saturar con margen (hFE forzado ≈ 10).
  - Vce(sat) y disipación.
  - Darlington (TIP120) y por qué no conviene (calienta).
- **MOSFET (canal N y canal P)**
  - Gate, drain y source; el gate es un capacitor.
  - **Vgs(th) no es la tensión a la que conduce bien.** Hay que mirar Rds(on) **al Vgs que tenés** (3.3 V o 5 V).
  - MOSFETs "de nivel lógico" (IRLZ44N, AO3400) frente a los que no lo son (IRF540N).
  - Resistencia de gate (limita corriente y oscilaciones) y pull-down de gate (evita encendidos al arrancar).
  - Disipación: P = I²·Rds(on) en estado estable y pérdidas de conmutación.
  - Diodo de cuerpo.
- **Lado bajo (low-side) frente a lado alto (high-side)**: por qué el lado alto con canal N necesita un gate driver.
- Llave de lado alto con MOSFET P + un NPN para manejarlo.
- **Térmica**: resistencia térmica (°C/W), Tj máxima, cuándo hace falta disipador y cómo calcularlo.
- Leer el datasheet completo de un MOSFET: SOA, curvas Rds(on) contra Vgs y Qg.
- Relés: cuándo convienen y cuándo no (y el diodo de rueda libre).
- Optoacopladores (introducción).

### Prácticas
1. NPN (2N2222/BC337) maneja un LED de potencia o una tira LED: calcular Rb, medir Vce(sat) y comparar con la teoría.
2. **IRLZ44N contra IRF540N** manejados con 5 V del Nano y la misma carga: medir Vds y temperatura. La lección aparece sola.
3. Medir la temperatura del MOSFET (con el dedo con cuidado o un termómetro IR) a distintas corrientes y compararla con el cálculo térmico.
4. Conmutación con osciloscopio: ver el flanco en el gate y en el drain y cómo cambia con distintas resistencias de gate (100 Ω, 1 kΩ, 10 kΩ).
5. Llave de lado alto con MOSFET P controlada desde el Nano.

### Entregable
Tabla comparativa de los dos MOSFET y una nota sobre cómo elegir un MOSFET para un micro de 3.3 V.

---

## Módulo 6 — Motores DC y puente H

**Objetivo**: mover un robot, entendiendo cada componente.

### Temas
- **El motor DC como carga eléctrica**
  - Modelo: resistencia + inductancia + fuerza contraelectromotriz (back-EMF).
  - **Corriente de arranque (stall)**: por qué es varias veces la nominal.
  - Velocidad proporcional a la tensión y torque proporcional a la corriente.
  - Medir los parámetros de tu motor: R de bobinado, corriente en vacío y de stall, y constante Kv.
  - El motor como generador (freno, back-EMF).
- Reductoras: torque contra velocidad.
- **Control de velocidad con PWM de un solo lado**: frecuencia de PWM (ruido audible frente a pérdidas) y el diodo de rueda libre otra vez.
- **Puente H**
  - Topología con 4 llaves y las combinaciones válidas.
  - **Shoot-through**: qué es, por qué destruye el puente y el dead-time.
  - Modos: avance, retroceso, freno (cortocircuito del motor) y rueda libre (coast).
  - Decaimiento rápido frente a lento (fast/slow decay).
- **Puente H integrado**: L298N (y por qué es malo: bipolar, cae 2–4 V), TB6612FNG y DRV8871 (MOSFET, eficientes).
  - Leer el datasheet del TB6612: corriente continua y pico, protección térmica, lógica de control.
- Capacitor de bulk en la alimentación del motor y cerámico en bornes del motor (supresión de ruido).

### Prácticas
1. **Caracterizar tu motor**: medir R, corriente en vacío y de stall (¡breve!) y velocidad contra tensión. Ficha técnica propia.
2. **Corriente de arranque en el osciloscopio**: resistencia shunt de 0.1–0.5 Ω en serie y capturar el pico al arrancar.
3. **Puente H discreto** con 2 MOSFET P + 2 N (o 4 N con driver si te animás), controlado por el Nano. **Usar la fuente con límite de corriente.**
4. Provocar shoot-through *a propósito* con límite de corriente bajo y ver el pico de corriente en el shunt.
5. Reemplazar el puente discreto por un TB6612 y comparar eficiencia, temperatura y caída de tensión.
6. 🤖 **Proyecto integrador A: robot móvil básico** con Nano + TB6612 + 2 motores con reductora + batería. Control por botones o serie.

### Entregable
Ficha técnica de tu motor y el robot móvil funcionando, con una captura de la corriente de arranque.

---

## Módulo 7 — Amplificadores operacionales y sensado

**Objetivo**: convertir señales del mundo real en algo que el micro pueda leer bien.

### Temas
- El op-amp ideal: las dos "reglas de oro" con realimentación negativa.
- Configuraciones:
  - **Seguidor (buffer)**: por qué arregla el problema del divisor del módulo 1.
  - **No inversor** e **inversor**: ganancia.
  - **Sumador**.
  - **Diferencial** e introducción al amplificador de instrumentación.
  - **Comparador** (sin realimentación) y **comparador con histéresis** (Schmitt trigger).
  - Integrador y derivador, de forma conceptual.
- Op-amps reales:
  - **Rail-to-rail** (entrada y salida): por qué el LM358 no llega a 0 V ni a Vcc.
  - Alimentación simple frente a partida y la tierra virtual.
  - Offset, producto ganancia-ancho de banda y slew rate.
  - Elegir el op-amp: LM358, MCP6002, TLV9062.
- Comparadores dedicados (LM393, salida colector abierto).
- **Sensado de corriente**:
  - Shunt de lado bajo + amplificador no inversor.
  - Shunt de lado alto + amplificador dedicado (INA180/INA181/INA240), con el problema del modo común.
  - Elegir el valor del shunt: caída de tensión contra resolución y potencia.
- **ADC**: resolución, rango, referencia y cuantización.
  - Resistencia de fuente que pide el ADC (capacitor de muestreo).
  - Filtro antialiasing RC antes del ADC.

### Prácticas
1. Seguidor de tensión: repetir el divisor con carga del módulo 1, ahora con buffer.
2. Amplificador no inversor con ganancia 10: medir la ganancia real y la saturación con LM358 frente a un rail-to-rail.
3. **Medidor de corriente del motor**: shunt de 0.1 Ω + amplificador, al ADC del Nano. Calibrar contra el multímetro.
4. Comparador con histéresis para un sensor IR: ver en el osciloscopio la salida con y sin histéresis cuando la señal es ruidosa.
5. 🤖 **Proyecto integrador B: seguidor de línea "a mano"** con fototransistores + LEDs IR discretos, comparadores con umbral por potenciómetro y el puente H del módulo 6. Sin módulos comprados.

### Entregable
Seguidor de línea funcionando y gráfico de corriente del motor contra carga mecánica (frenándolo con la mano).

---

## Módulo 8 — El microcontrolador desde el hardware (STM32)

**Objetivo**: entender el micro como **componente electrónico**, no como plataforma de programación.

### Temas
- Pasar a 3.3 V: niveles lógicos (VIH, VIL, VOH, VOL), **pines tolerantes a 5 V (FT)** del STM32 y cuáles no lo son.
- **Adaptación de niveles**: divisor resistivo (unidireccional), MOSFET BSS138 (bidireccional, I²C) e integrados (TXS0108, 74LVC245).
- Estructura de un pin GPIO: push-pull, open-drain, pull-ups internos y diodos de protección.
  - Corriente máxima por pin y por puerto.
- Lo mínimo para que el micro arranque (lo que tu PCB necesitará en el módulo 14):
  - Alimentación + desacople por cada pin VDD.
  - VDDA con filtro (ferrita + capacitores).
  - Pin NRST con capacitor.
  - BOOT0 con pull-down.
  - Cristal HSE: capacitores de carga y su cálculo.
  - Conector SWD (SWDIO, SWCLK, GND, 3V3, NRST).
- **Leer el datasheet y el reference manual del STM32F4**: pinout, funciones alternativas, tabla de características eléctricas.
- **STM32CubeMX**: asignar pines y ver conflictos. Es la herramienta de *hardware* del micro.
- **Periféricos desde lo eléctrico**:
  - **Timers**: PWM, frecuencia contra resolución; timers avanzados (TIM1/TIM8): PWM complementario, dead-time y entrada de *break* para apagado de emergencia.
  - **Modo encoder** por hardware.
  - **ADC**: tiempo de muestreo e impedancia de fuente.
  - UART, I²C y SPI a nivel de señal: open-drain y pull-ups en I²C, velocidad de flancos.
- Depuración con SWD (ST-Link): el código lo escribe la IA, pero vos tenés que saber leer un registro, ver un pin y medir.

### Prácticas
1. Configurar en CubeMX un proyecto con PWM, encoder, ADC e I²C y documentar la asignación de pines (es el pinout de tu futura PCB).
2. Generar PWM complementario con dead-time en TIM1 y **medir el dead-time en el osciloscopio** con dos canales.
3. Medir los flancos de I²C con distintos pull-ups (1k, 4k7, 10k) y explicar el tiempo de subida (RC con la capacitancia del bus).
4. Adaptador de niveles con BSS138 entre el Nano (5 V) y el STM32 (3.3 V).

### Entregable
Hoja de "asignación de pines" del robot final, con justificación por periférico.

---

## Módulo 9 — Sensores y acondicionamiento de señal

**Objetivo**: que el robot perciba el mundo con datos confiables.

### Temas
- **Clasificación**: analógicos contra digitales; resistivos, de corriente y de frecuencia.
- **Sensores de proximidad y distancia**
  - IR reflectivos discretos (del módulo 7).
  - Ultrasónico HC-SR04: pulso de eco y adaptación a 3.3 V.
  - ToF VL53L0X/VL53L1X (I²C).
  - IR analógico Sharp GP2Y0A21: no lineal y ruidoso (necesita capacitor de desacople grande).
- **IMU**: acelerómetro + giroscopio (MPU6050, BNO085, ICM-42688).
  - Desacople y ubicación mecánica (vibración de motores).
  - Interrupciones y frecuencia de muestreo.
- **Encoders**:
  - Ópticos y magnéticos (de efecto Hall en motores tipo JGA25/N20).
  - Señales en cuadratura: A, B y su desfase.
  - Pull-ups, filtrado RC y Schmitt trigger (74HC14) para limpiar flancos.
- **Finales de carrera y bumpers**: rebote, pull-up y protección de la entrada (resistencia serie + clamping) cuando el cable es largo.
- **Sensores de temperatura**: NTC + divisor (no lineal; Steinhart-Hart o tabla) y digitales (DS18B20, TMP117).
- **Sensado de tensión de batería**: divisor de alta impedancia + capacitor al ADC.
- **Acondicionamiento general**: offset, ganancia, filtro y protección. "Cadena de señal" de punta a punta.
- **Cables y buses**: largo máximo de I²C, uso de cables trenzados y apantallados, y cuándo pasar a señales diferenciales (CAN, RS-485, en introducción).

### Prácticas
1. Encoder de motor: ver A y B en el osciloscopio, con y sin el motor encendido (ruido), y después agregar filtro + Schmitt trigger.
2. IMU por I²C: capturar los datos con el analizador lógico; medir el ruido del acelerómetro quieto, sobre la mesa y sobre el chasis con motores andando.
3. Sharp GP2Y0A21: medir el pico de consumo en el osciloscopio y ver el efecto de un capacitor de 100 µF en la alimentación.
4. Divisor de batería con filtro: calcular la impedancia de fuente y comparar la lectura del ADC con y sin capacitor.

### Entregable
"Placa de sensores" en placa perforada con IMU, sensor ToF, entradas de encoder acondicionadas y divisor de batería.

---

## Módulo 10 — Potencia: baterías, reguladores y protección

**Objetivo**: que el robot tenga energía estable y no se queme ni se incendie.

### Temas
- **Baterías**
  - Químicas: NiMH, Li-ion (18650) y LiPo (paquetes RC).
  - Tensión nominal, de carga completa y de corte (3.0–4.2 V por celda).
  - Capacidad (mAh), tasa C, resistencia interna y curvas de descarga.
  - Configuraciones S y P (2S, 3S) y balanceo.
  - **BMS**: protección contra sobrecarga, sobredescarga y cortocircuito.
  - **Seguridad LiPo**: carga balanceada, almacenamiento a 3.8 V por celda, celdas hinchadas y bolsa ignífuga.
- **Reguladores lineales**
  - LDO (AMS1117, AP2112, MCP1700): dropout, disipación P = (Vin − Vout)·I y estabilidad (ESR del capacitor de salida).
  - Cuándo convienen: bajo ruido, poca diferencia de tensión y poca corriente.
- **Fuentes conmutadas**
  - Buck: funcionamiento (llave, diodo o síncrono, inductor, capacitor), ciclo de trabajo, rizado y eficiencia.
  - Boost y buck-boost.
  - Selección del inductor (corriente de saturación) y de capacitores.
  - **Layout crítico**: el lazo de corriente caliente (aquí se conecta con el módulo 14).
  - Módulos (MP1584, LM2596, frente a los buenos: TPS5430, módulos de Pololu) y sus límites reales.
- **Arquitectura de potencia de un robot**
  - Batería → fusible → llave → protección de polaridad → bus de motores, y → buck → 5 V → LDO → 3.3 V lógica.
  - Capacitores de bulk y separación de dominios.
  - **Brown-out**: por qué el micro se reinicia cuando arranca el motor y cómo evitarlo.
- **Protecciones**
  - Fusibles (rápidos, lentos, PTC reseteables).
  - **Polaridad inversa con MOSFET P** (sin la caída de un diodo).
  - TVS en la entrada.
  - Soft-start y corriente de arranque de capacitores (inrush).
  - Ideal diode e eFuse (introducción).
- **Conectores y cables de potencia**: XT30/XT60, JST-XH (balanceo), calibre AWG contra corriente y caída de tensión en cables.

### Prácticas
1. Curva de descarga de una celda 18650 o LiPo con carga resistiva, midiendo cada X minutos (o automatizado con el ADC).
2. LDO contra buck con la misma carga: medir eficiencia (Pin/Pout) y temperatura.
3. Rizado de un buck en el osciloscopio: técnica de medición correcta con resorte de masa corto, y la diferencia con el cable largo.
4. **Provocar un brown-out**: micro y motor en la misma alimentación sin bulk, ver la caída en el osciloscopio y el reinicio. Corregir con bulk, separación y diodo, y documentar.
5. Protección de polaridad con MOSFET P: medir la caída comparada con el diodo del módulo 4.
6. 🔧 **Proyecto: placa de distribución de energía** en placa perforada con entrada XT60, fusible, polaridad con MOSFET P, TVS, buck a 5 V, LDO a 3.3 V, medición de tensión y corriente de batería y LED de estado.

### Entregable
Placa de distribución funcionando, con mediciones de eficiencia y rizado.

---

## Módulo 11 — Motores avanzados: encoders, PID, steppers y servos

**Objetivo**: control preciso de movimiento.

### Temas
- **Control en lazo cerrado**
  - Lazo abierto frente a cerrado.
  - **PID** de forma intuitiva: P (presente), I (pasado) y D (futuro).
  - Ajuste empírico (Ziegler-Nichols o a mano) y saturación con *anti-windup*.
  - Lazos de velocidad y de posición, en cascada.
  - Frecuencia de lazo y por qué importa.
  - Visualizar la respuesta: escalón, sobrepico y tiempo de establecimiento.
- **Medio puente con gate driver**
  - Gate drivers (IR2104, DRV8301 como referencia).
  - **Bootstrap**: cómo se alimenta el MOSFET de lado alto canal N.
  - Dead-time por hardware (del módulo 8).
  - Sensado de corriente por fase.
- **Motores paso a paso**
  - Bipolar y unipolar, pasos y micropasos.
  - Control por corriente (chopper) y **ajuste de Vref** del driver.
  - Drivers A4988, DRV8825 y TMC2209 (silencioso, StallGuard).
  - Resonancia y pérdida de pasos.
  - Temperatura de motor y driver.
- **Servos de hobby**: señal de 50 Hz y 1–2 ms, **consumo pico** (reinicios típicos) y alimentación separada.
- **BLDC** (introducción): 3 fases, conmutación con sensores Hall, ESC. Base para seguir más adelante con FOC.

### Prácticas
1. **Servo casero**: motor DC + encoder + PID de posición en el STM32 con encoder por timer. Respuesta al escalón capturada (osciloscopio o graficada por UART).
2. Ajustar el PID en tres configuraciones (subamortiguado, crítico y sobreamortiguado) y documentar cada una.
3. Medio puente discreto con IR2104 + 2 MOSFET N: medir la tensión de bootstrap, el dead-time y los flancos.
4. Stepper NEMA17 con TMC2209: ajustar Vref, medir la corriente por fase con el shunt y encontrar la velocidad máxima antes de perder pasos.
5. Servo MG996R: medir el pico de corriente en el osciloscopio y ver qué le pasa a la alimentación compartida.
6. 🤖 **Proyecto integrador C** (elegí uno):
   - **Robot diferencial con odometría**: dos motores con encoder + IMU, y que vaya a coordenadas (x, y).
   - **Brazo de 3 ejes con steppers** + finales de carrera y *homing*.

### Entregable
Gráficos de la respuesta PID y el proyecto C funcionando.

---

## Módulo 12 — Ruido, masas y robustez (EMC práctica)

**Objetivo**: que el robot funcione siempre, no solo en la mesa.

### Temas
- **De dónde viene el ruido en un robot**: conmutación PWM, escobillas de los motores, picos inductivos, fuentes conmutadas y descargas electrostáticas.
- **Corriente de retorno**: toda corriente vuelve por algún lado y elige el camino de menor impedancia (a alta frecuencia, por debajo de la ida).
- **Lazos de corriente**: área del lazo = antena; minimizarla.
- **Masas**: estrella, plano, separación de masa de potencia y de señal, y dónde se unen.
- **Ground bounce** y cómo la corriente del motor corre la referencia del ADC.
- Desacople: valores, ubicación y vías.
- Ferritas: cuándo ayudan y cuándo no.
- **Supresión en motores DC**: capacitores cerámicos de borne a borne y de borne a carcasa.
- Cables: trenzado de pares (motor e ida/vuelta), apantallado y alejar señales de potencia.
- **ESD**: protección de conectores (TVS, resistencias en serie).
- **Watchdog y brown-out** del micro: la última línea de defensa.
- Cómo **medir ruido** bien: punta x10, resorte de masa y modo de adquisición (promedio frente a pico).

### Prácticas
1. Medir el ruido en la línea de 3.3 V y en una entrada del ADC con los motores andando. Ir aplicando una mejora a la vez y medir:
   - Capacitores en el motor.
   - Trenzado de cables.
   - Separación de masas.
   - Filtro en el ADC.
2. Cable de I²C de 50 cm junto a los cables del motor: contar errores de comunicación. Arreglarlo (pull-ups más fuertes, trenzado, menor velocidad) y documentar.
3. Pasar el cable de masa del osciloscopio de largo a corto (resorte) y ver cuánto "ruido" era del propio instrumento.

### Entregable
Informe "antes y después" con capturas de cada mejora aplicada al robot del módulo 11.

---

## Módulo 13 — Soldadura y construcción (transversal)

**Objetivo**: construir cosas que no se desarmen. Se practica en paralelo desde el módulo 1.

### Progresión
1. **Through-hole (THT)**
   - Temperatura (330–360 °C), punta limpia y estañada, y flux.
   - La junta correcta: cono brillante (y cómo se ve una junta fría).
   - Kits para practicar (por ejemplo, un kit de soldadura con LEDs o una radio sencilla).
2. **Placa perforada**: planificar el layout en papel, puentes, pistas con alambre o estaño, y separar potencia de señal.
3. **Desoldar**: malla, bomba y aire caliente.
4. **SMD**
   - 1206 → 0805 → 0603, con pinzas y flux.
   - SOIC y SOT-23.
   - TSSOP con técnica de arrastre (*drag soldering*) y malla para los puentes.
   - QFN y LQFP del STM32: pasta + aire caliente o placa calefactora (hotplate).
   - Inspección con lupa o microscopio USB.
5. **Cables y conectores**: crimpado de JST y Dupont (crimpadora de verdad), termocontraíble, organización y alivio de tensión.
6. **Mecánica básica**: separadores (standoffs), fijación de placas, antivibración e impresión 3D de soportes (opcional).

### Entregable
Una placa de práctica SMD con componentes del 1206 al 0603 + un TSSOP soldados y revisados con lupa.

---

## Módulo 14 — Diseño de PCB con KiCad

**Objetivo**: pasar de la placa perforada a una PCB profesional.

### Temas
- **Flujo completo**: esquemático → asignación de footprints → layout → DRC → Gerbers → pedido a fábrica.
- **Esquemático**
  - Símbolos, etiquetas, hojas jerárquicas, ERC.
  - Buenas prácticas de legibilidad (la señal de izquierda a derecha, alimentación arriba).
- **Componentes**: crear símbolos y footprints propios y verificar dimensiones con el datasheet (el error más caro).
- **Elegir componentes para fabricar**: disponibilidad (LCSC, Mouser, DigiKey) y el catálogo "basic" de JLCPCB para montaje.
- **Stack-up**: 2 capas frente a 4 capas (con 4 capas el plano de masa es mucho más fácil).
- **Layout**
  - Ubicación primero (el 80 % del trabajo), ruteo después.
  - **Plano de masa continuo**: no cortarlo con pistas.
  - Ancho de pista contra corriente (calculadora IPC-2152) y vías térmicas y de corriente.
  - **Lazo de potencia del buck y del puente H**: minimizarlo.
  - Desacople pegado a cada pin de alimentación.
  - Separar la zona de potencia de la de señal.
  - Cristal: cerca del micro, con un anillo de masa.
  - Pads para puntas de prueba (test points).
  - Serigrafía útil: polaridad, nombres de conectores, versión y fecha.
- **Disipación de calor en PCB**: cobre como disipador y vías térmicas bajo los MOSFET.
- **Reglas de fabricante** (JLCPCB): pista y separación mínima, vías y máscara.
- **Revisión antes del pedido**: checklist, impresión 1:1 en papel para probar componentes, vista 3D.
- **Bring-up de la placa nueva**
  - Inspección visual y continuidad entre alimentación y masa **antes** de alimentar.
  - Primer encendido con la fuente con límite de corriente bajo.
  - Medir las tensiones en orden, programar y probar bloque por bloque.
  - Retrabajos: cortes de pista y puentes.

### Prácticas (en orden)
1. **PCB 1: una placa simple** con uno de tus circuitos ya probados (por ejemplo, el driver de motor con MOSFET + diodo + bornera). 2 capas, todo THT o SMD 1206.
2. **PCB 2: la placa de distribución de energía** del módulo 10, con un buck en SMD y atención al lazo de potencia.
3. **Revisión de un diseño ajeno**: tomar un diseño open source (por ejemplo, de Phil's Lab), estudiar sus decisiones de layout y anotar lo que aprendiste.

### Entregable
Dos PCB fabricadas, armadas y funcionando, con el registro de bring-up de cada una.

---

## Módulo 15 — Proyecto final: robot con placa controladora propia

**Objetivo**: integrar todo en un robot que funcione con **tu** hardware.

### Especificación de la placa (sugerida)
- **Micro**: STM32F4 (F411 o F446, en LQFP) con SWD, cristal y circuito de reset/boot.
- **Potencia**:
  - Entrada 2S–3S LiPo (7–12.6 V) con XT30/XT60.
  - Fusible, protección de polaridad con MOSFET P y TVS.
  - Buck a 5 V y LDO a 3.3 V.
- **Motores**: 2 drivers (DRV8871 o TB6612) **o** puentes discretos con gate driver si querés el desafío.
- **Sensado de corriente** por motor (INA181 o similar).
- **Encoders**: 2 entradas con filtro + Schmitt trigger, conectadas a timers en modo encoder.
- **Conectores** para IMU (I²C), ToF (I²C), servos (PWM, con alimentación separada) y UART libre (para un módulo Bluetooth, una Raspberry Pi o el debug).
- **Medición** de tensión de batería y apagado por batería baja.
- **LEDs** de alimentación y de estado, botón de usuario y test points.

### Fases
1. **Requerimientos**: qué tiene que hacer el robot (seguidor de línea rápido, robot de sumo, mapeo, brazo).
2. **Presupuesto de potencia**: corriente de cada bloque, picos y autonomía.
3. **Esquemático**, con revisión propia y "de pares" (pasárselo a un foro o comunidad).
4. **Prototipo de los bloques riesgosos** en protoboard o en las placas de módulos anteriores.
5. **Layout** + checklist del módulo 14.
6. **Fabricación**: 5 placas (te van a hacer falta).
7. **Bring-up** bloque por bloque, con registro de errores. Habrá errores, y forman parte del aprendizaje.
8. **Integración mecánica** y firmware (con ayuda de la IA).
9. **Validación**: autonomía real, temperatura de los drivers, ruido en sensores con motores andando, prueba de 30 minutos sin reinicios.
10. **Revisión 2 de la placa** con las correcciones (opcional, pero es donde más se aprende).

### Entregable final
- Robot funcionando.
- Repositorio con esquemático, PCB, BOM, notas de bring-up y las mediciones de validación.
- Un **post-mortem**: qué salió mal, qué cambiarías y qué aprendiste. Es tu portfolio de hardware.

---

## Lista de compras por etapa

### Etapa 1: módulos 0–4 (arranque)
- Multímetro decente (UNI-T UT61E+, UT139C o similar).
- Fuente de laboratorio regulable con límite de corriente (0–30 V, 0–5 A).
- Osciloscopio de 2 canales (Rigol DHO800, Siglent SDS1104X-E, Owon). **La compra más importante.**
- Analizador lógico 8 canales (clon de Saleae).
- 2 protoboards grandes + cables Dupont + cable rígido.
- Arduino Nano (x2: uno de repuesto).
- Kit de resistencias E12 ¼ W, kit de capacitores cerámicos y electrolíticos.
- Diodos: 1N4007, 1N4148, 1N5819, zeners surtidos.
- LEDs surtidos, potenciómetros, pulsadores.
- Un relé de 5 V (para el pico inductivo).
- Soldador con control de temperatura (Pinecil o TS101), estaño 0.8 mm con flux, flux en pasta, malla desoldante, pinzas, alicate de corte.

### Etapa 2: módulos 5–7
- MOSFET: IRLZ44N (x4), IRF540N (x2, para comparar), IRF9540 o IRF4905 (canal P, x2), AO3400/AO3401 (SMD, para más adelante).
- BJT: 2N2222 o BC337, 2N3906 o BC327.
- TB6612FNG (módulo), DRV8871 (módulo).
- 2 motores DC con reductora (amarillos de robot o N20/JGA25 **con encoder**: mejor que ya traigan encoder).
- Resistencias shunt de 0.1 Ω y 0.5 Ω, de 1–3 W.
- Op-amps: LM358, MCP6002 o TLV9062; comparador LM393; INA181.
- LEDs IR + fototransistores.
- Chasis de robot de 2 ruedas + rueda loca.
- Portapilas o batería 2S con su BMS y cargador.

### Etapa 3: módulos 8–12
- STM32: Nucleo-F446RE (o Black Pill F411 + ST-Link V2).
- BSS138 (adaptadores de nivel), 74HC14 (Schmitt trigger).
- IMU (MPU6050 para empezar; BNO085 o ICM-42688 si querés calidad), VL53L0X, HC-SR04.
- Baterías LiPo 2S/3S + **cargador balanceador** (ISDT o SkyRC) + **bolsa ignífuga**.
- Conectores XT30/XT60, JST-XH, crimpadora.
- Reguladores: AMS1117-3.3, módulos buck (MP1584), fusibles y portafusibles, TVS (SMBJ).
- IR2104 + MOSFET N para el medio puente.
- Stepper NEMA17 + TMC2209, servo MG996R y SG90.
- Placas perforadas (de buena calidad, con agujeros metalizados).

### Etapa 4: módulos 13–15
- Estación de aire caliente o placa calefactora (hotplate).
- Pasta de soldar, flux de mejor calidad.
- Lupa o microscopio USB.
- Pedidos de PCB (JLCPCB/PCBWay) y componentes de LCSC.

---

## Recursos

### Libros
| Libro | Para qué |
|---|---|
| *Practical Electronics for Inventors* (Scherz y Monk) | Base de los módulos 1–7, muy práctico |
| *The Art of Electronics* (Horowitz y Hill) | Referencia de cabecera; profundidad en transistores, op-amps y potencia |
| *Make: Electronics* (Platt) | Opcional, si te gusta aprender haciendo desde cero |
| *Learning the Art of Electronics* (Hayes y Horowitz) | Manual de laboratorio del anterior; ideal para el método "medir" |
| *High Speed Digital Design* (Johnson y Graham) | Avanzado, para el módulo 12 |
| *Electromagnetic Compatibility Engineering* (Ott) | Referencia de EMC, consulta puntual |

### YouTube
- **EEVblog**: medición, criterio, fallas de diseño.
- **w2aew** (Alan Wolke): el mejor material sobre osciloscopios y técnicas de medición.
- **Phil's Lab**: diseño de PCB serio con STM32 y KiCad.
- **Robert Feranec**: layout y diseño de alta velocidad.
- **GreatScott!**: proyectos de potencia y drivers explicados.
- **James Bruton**: robótica real e integración.
- **Ben Eater**: electrónica digital desde cero.
- **ElectroBOOM**: seguridad y lo que pasa cuando hacés las cosas mal (entretenido y educativo).

### Documentación gratuita (oro puro)
- Notas de aplicación de **Texas Instruments**: control de motores, gate drivers, layout de fuentes conmutadas, op-amps ("Op Amps for Everyone").
- Notas de aplicación de **ST**: hardware de STM32 (AN2867 sobre osciladores, AN4488 de hardware para STM32F4), control de motores.
- Notas de **Analog Devices**: tutoriales MT (op-amps, ADC).
- **Infineon / International Rectifier**: AN-978 (gate drivers y bootstrap).

### Software
- **LTspice**: simulación (gratis).
- **KiCad**: diseño de PCB (gratis).
- **STM32CubeMX / CubeIDE**: configuración y depuración del STM32.
- **PulseView** (sigrok): analizador lógico.
- **Falstad Circuit Simulator** (web): intuición rápida, ideal para los módulos 1–3.

---

## Método de estudio sugerido

1. **Cuaderno de laboratorio** desde el día 1: fecha, objetivo, circuito, cálculo, medición y conclusión. Es lo que convierte el "jugar" en "aprender".
2. **Ciclo por tema**: leer/ver (30 %) → calcular y simular (20 %) → armar y medir (50 %).
3. **Romper cosas a propósito**, controladamente: pico inductivo, shoot-through, brown-out, entrada flotante. Con límite de corriente y medición.
4. **Leer un datasheet por semana**, completo, de algo que estés usando.
5. **La IA para lo derivable**: firmware, cuentas repetitivas, "explicame por qué...". El criterio de diseño y la medición, vos.
6. **Repaso espaciado**: los conceptos clave (fórmulas, valores típicos, reglas de diseño) en tarjetas.
7. **Comunidades**: r/AskElectronics, r/PrintedCircuitBoard (revisan tu PCB gratis antes de fabricar) y el foro de EEVblog.

---

## Hitos de control (¿voy bien?)

| Al terminar | Deberías poder... |
|---|---|
| Módulo 3 | Predecir la curva de un RC, medirla y explicar las diferencias |
| Módulo 6 | Elegir un MOSFET y un driver para un motor dado, sabiendo por qué |
| Módulo 7 | Diseñar la cadena de medición de corriente de un motor |
| Módulo 10 | Diseñar la alimentación completa de un robot con protecciones |
| Módulo 12 | Diagnosticar por qué un robot se reinicia o lee mal un sensor |
| Módulo 15 | Diseñar, fabricar y poner en marcha una placa controladora propia |
