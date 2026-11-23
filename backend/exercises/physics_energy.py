"""Ejercicios de Física: magnitudes y unidades, trabajo y energía, momento lineal, torque y fluidos.

Problemas de varios pasos (tipo guía de trabajos prácticos / parcial de ingreso) para los temas
`f-magnitudes-vectores`, `f-trabajo-energia`, `f-momento-choques`, `f-torque-rotacion` y `f-fluidos`.
Cuatro por tema: uno de nivel 1, dos de nivel 2 y uno de nivel 3.
"""

EXERCISES = [
    # ============================================================
    # f-magnitudes-vectores — unidades, notación científica, análisis dimensional
    # ============================================================
    {
        "id": "f-magnitudes-vectores-1",
        "node": "f-magnitudes-vectores",
        "kind": "problem",
        "level": 1,
        "title": "El colectivo y el tiempo de reacción",
        "statement": (
            "Un colectivo de larga distancia viaja por la Ruta 2 a una velocidad constante de **90 km/h**. "
            "El chofer ve un obstáculo y tarda **0.8 s** en reaccionar; durante ese tiempo el colectivo sigue "
            "a la misma velocidad. Por la colectora, un ciclista avanza **150 m** en **20 s** a ritmo parejo."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la velocidad del colectivo en m/s? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 25, "tolerance": 0, "unit": "m/s"},
                "answer": "25 m/s",
            },
            {
                "prompt": "b) ¿Cuántos metros recorre el colectivo durante el tiempo de reacción del chofer? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "m"},
                "answer": "20 m",
            },
            {
                "prompt": "c) ¿Cuál es la velocidad del ciclista en km/h? Respondé solo con el número en km/h.",
                "check": {"type": "numeric", "value": 27, "tolerance": 0, "unit": "km/h"},
                "answer": "27 km/h",
            },
        ],
        "hints": [
            "Antes de multiplicar velocidad por tiempo, las dos magnitudes tienen que estar en unidades compatibles (m/s con s).",
            "`1 km = 1000 m` y `1 h = 3600 s`: pasar de km/h a m/s es dividir por 3.6; de m/s a km/h, multiplicar por 3.6.",
        ],
        "solution": [
            "Factor de conversión: `1 km/h = 1000 m / 3600 s = (1/3.6) m/s`. Por eso de km/h a m/s se divide por 3.6 y de m/s a km/h se multiplica por 3.6.",
            "a) `90 km/h = 90 × 1000 m / 3600 s = 90 ÷ 3.6 = 25 m/s`.",
            "b) A velocidad constante, `d = v · t`, con todo en SI: `d = 25 m/s × 0.8 s = 20 m`. (Error típico: hacer `90 × 0.8 = 72`, mezclando km/h con segundos.)",
            "c) Primero la velocidad del ciclista en SI: `v = 150 m / 20 s = 7.5 m/s`.",
            "Después se pasa a km/h: `7.5 × 3.6 = 27 km/h`.",
            "Respuestas: 25 m/s, 20 m y 27 km/h. Verificación: 27 km/h es menos de un tercio de 90 km/h, razonable para una bici frente a un colectivo.",
        ],
    },
    {
        "id": "f-magnitudes-vectores-2",
        "node": "f-magnitudes-vectores",
        "kind": "problem",
        "level": 2,
        "title": "Llenar el tanque de la terraza",
        "statement": (
            "Un tanque de agua de base rectangular mide por dentro **150 cm × 80 cm**. Está vacío y se lo llena "
            "con una manguera que entrega un caudal constante de **0.2 L/s**, hasta que el agua alcanza "
            "**50 cm** de altura. Datos: `1 L = 1 dm³ = 1000 cm³` y `1 m³ = 1000 L`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto mide el área de la base del tanque en m²? Respondé solo con el número en m².",
                "check": {"type": "numeric", "value": 1.2, "tolerance": 0, "unit": "m²"},
                "answer": "1.2 m²",
            },
            {
                "prompt": "b) ¿Qué volumen de agua hay en el tanque al final, en litros? Respondé solo con el número en L.",
                "check": {"type": "numeric", "value": 600, "tolerance": 0, "unit": "L"},
                "answer": "600 L",
            },
            {
                "prompt": "c) ¿Cuántos minutos tarda la manguera en cargar esa cantidad de agua? Respondé solo con el número en min.",
                "check": {"type": "numeric", "value": 50, "tolerance": 0, "unit": "min"},
                "answer": "50 min",
            },
        ],
        "hints": [
            "Conviene pasar las tres medidas a metros antes de multiplicar. Ojo: `1 m² = 100 cm × 100 cm = 10 000 cm²`, no 100 cm².",
            "Volumen = área de la base × altura. Después convertí m³ a litros con `1 m³ = 1000 L`.",
            "Tiempo = volumen ÷ caudal. Te va a dar en segundos: falta dividir por 60.",
        ],
        "solution": [
            "Se pasan las longitudes a metros: `150 cm = 1.5 m`, `80 cm = 0.8 m`, `50 cm = 0.5 m`.",
            "a) Área de la base: `A = 1.5 m × 0.8 m = 1.2 m²`. Por el otro camino: `150 × 80 = 12 000 cm²`, y como `1 m² = 10 000 cm²`, `12 000 ÷ 10 000 = 1.2 m²`. (Error típico: dividir por 100 y obtener 120 m².)",
            "b) Volumen: `V = A · h = 1.2 m² × 0.5 m = 0.6 m³`.",
            "Como `1 m³ = 1000 L`, `V = 0.6 × 1000 = 600 L`.",
            "c) Tiempo de llenado: `t = V / caudal = 600 L ÷ 0.2 L/s = 3000 s`.",
            "En minutos: `3000 s ÷ 60 = 50 min`.",
            "Respuestas: 1.2 m², 600 L y 50 min. Verificación: 0.2 L/s son 12 L por minuto, y `12 × 50 = 600 L`.",
        ],
    },
    {
        "id": "f-magnitudes-vectores-3",
        "node": "f-magnitudes-vectores",
        "kind": "problem",
        "level": 2,
        "title": "Nafta: de g/cm³ a notación científica",
        "statement": (
            "La nafta tiene una densidad de **0.75 g/cm³**. El tanque de un auto carga **40 L**. "
            "Además, se estima que en la Argentina se consumen unos **9 × 10⁹ L** de nafta por año (valor redondeado). "
            "Datos: `1 L = 1000 cm³` y `1 m³ = 1000 L`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la densidad de la nafta en kg/m³? Respondé solo con el número en kg/m³.",
                "check": {"type": "numeric", "value": 750, "tolerance": 0, "unit": "kg/m³"},
                "answer": "750 kg/m³",
            },
            {
                "prompt": "b) ¿Qué masa de nafta entra en el tanque del auto? Respondé solo con el número en kg.",
                "check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": "kg"},
                "answer": "30 kg",
            },
            {
                "prompt": "c) ¿Cuál es la masa de la nafta que se consume en un año, en kg y en notación científica?",
                "check": {
                    "type": "choice",
                    "options": [
                        "6.75 × 10⁹ kg",
                        "6.75 × 10¹² kg",
                        "1.2 × 10¹⁰ kg",
                        "6.75 × 10⁶ kg",
                    ],
                    "correct": 0,
                },
                "answer": "6.75 × 10⁹ kg",
            },
        ],
        "hints": [
            "Para convertir g/cm³ a kg/m³ convertí por separado el numerador (g → kg) y el denominador (cm³ → m³): `1 m³ = 100³ cm³ = 10⁶ cm³`.",
            "Masa = densidad × volumen, con el volumen en m³ si la densidad está en kg/m³ (`40 L = 0.04 m³`).",
            "En el inciso c) pasá los litros a m³ restando 3 al exponente (`10⁹ L = 10⁶ m³`) y recién después multiplicá por la densidad.",
        ],
        "solution": [
            "a) `1 g = 10⁻³ kg` y `1 cm³ = 10⁻⁶ m³`, entonces `1 g/cm³ = 10⁻³ kg / 10⁻⁶ m³ = 1000 kg/m³`.",
            "Por lo tanto `0.75 g/cm³ = 0.75 × 1000 = 750 kg/m³`.",
            "b) Volumen del tanque en SI: `40 L = 40 ÷ 1000 = 0.04 m³`. Masa: `m = ρ · V = 750 kg/m³ × 0.04 m³ = 30 kg`. (Otra forma: `40 L = 40 000 cm³`, y `0.75 × 40 000 = 30 000 g = 30 kg`.)",
            "c) Volumen anual en m³: `9 × 10⁹ L ÷ 10³ = 9 × 10⁶ m³`.",
            "Masa anual: `m = 750 × 9 × 10⁶ = 6750 × 10⁶ kg = 6.75 × 10³ × 10⁶ kg = 6.75 × 10⁹ kg`.",
            "Respuestas: 750 kg/m³, 30 kg y 6.75 × 10⁹ kg (casi 7 millones de toneladas: orden de magnitud 10¹⁰ kg). Los distractores salen de errores típicos: no pasar los litros a m³ (10¹²), dividir por la densidad en vez de multiplicar (1.2 × 10¹⁰) o tomar la densidad como 0.75 g por litro (10⁶).",
        ],
    },
    {
        "id": "f-magnitudes-vectores-4",
        "node": "f-magnitudes-vectores",
        "kind": "problem",
        "level": 3,
        "title": "Resistencia del aire: análisis dimensional",
        "statement": (
            "La fuerza de resistencia del aire sobre un auto se modela con `F = ½ · C · ρ · A · v²`, donde `C` es un "
            "coeficiente **adimensional** (sin unidades), `ρ` es la densidad del aire, `A` es el área frontal del auto "
            "y `v` su velocidad. Para un auto dado se agrupan las constantes en `k = ½ · C · ρ · A`, de modo que "
            "`F = k · v²`. Datos del auto y del aire: `C = 0.3`, `ρ = 1.2 × 10⁻³ g/cm³` y `A = 25 000 cm²`."
        ),
        "parts": [
            {
                "prompt": "a) ¿En qué unidad del SI se mide la constante `k`?",
                "check": {
                    "type": "choice",
                    "options": ["kg/m", "kg/s", "kg·m/s²", "kg·m"],
                    "correct": 0,
                },
                "answer": "kg/m",
            },
            {
                "prompt": "b) ¿Cuánto vale `k` para este auto, en unidades del SI? Respondé solo con el número en kg/m.",
                "check": {"type": "numeric", "value": 0.45, "tolerance": 0, "unit": "kg/m"},
                "answer": "0.45 kg/m",
            },
            {
                "prompt": "c) ¿Qué fuerza de resistencia actúa sobre el auto cuando viaja a 144 km/h? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 720, "tolerance": 0, "unit": "N"},
                "answer": "720 N",
            },
        ],
        "hints": [
            "Despejá `k = F / v²` y reemplazá cada magnitud por sus unidades básicas: `N = kg·m/s²` y `v²` en `m²/s²`.",
            "Pasá todos los datos al SI antes de multiplicar: `1 g/cm³ = 1000 kg/m³` y `1 m² = 10 000 cm²`.",
            "Para el inciso c) la velocidad tiene que estar en m/s (dividí por 3.6) y va elevada al cuadrado.",
        ],
        "solution": [
            "a) De `F = k · v²` sale `k = F / v²`. En unidades: `[k] = (kg·m/s²) ÷ (m²/s²) = kg·m/s² × s²/m² = kg/m`.",
            "Control con la definición `k = ½ · C · ρ · A`: `C` y `½` no tienen unidades, así que `[k] = (kg/m³) · m² = kg/m`. Coincide.",
            "b) Densidad del aire en SI: `1.2 × 10⁻³ g/cm³ × 1000 = 1.2 kg/m³`.",
            "Área frontal en SI: `25 000 cm² ÷ 10 000 = 2.5 m²`.",
            "Entonces `k = ½ × 0.3 × 1.2 × 2.5 = 0.45 kg/m`.",
            "c) Velocidad en SI: `144 km/h ÷ 3.6 = 40 m/s`. Fuerza: `F = k · v² = 0.45 × 40² = 0.45 × 1600 = 720 N`.",
            "Respuestas: kg/m, 0.45 kg/m y 720 N. Error típico: reemplazar `v = 144` sin convertir, que daría más de 9000 N (unas 13 veces de más, porque el factor 3.6 queda elevado al cuadrado).",
        ],
    },
    # ============================================================
    # f-trabajo-energia
    # ============================================================
    {
        "id": "f-trabajo-energia-1",
        "node": "f-trabajo-energia",
        "kind": "problem",
        "level": 1,
        "title": "La valija con rueditas",
        "statement": (
            "En la terminal de Retiro arrastrás una valija por el piso horizontal tirando de la manija con una fuerza "
            "constante de **50 N** que forma **37°** con la horizontal (sen 37° = 0.6 y cos 37° = 0.8). "
            "La valija recorre **20 m** en línea recta, a **velocidad constante**, en **16 s**. "
            "Hay rozamiento entre la valija y el piso."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué trabajo hace tu fuerza sobre la valija en ese recorrido? Respondé solo con el número en J.",
                "check": {"type": "numeric", "value": 800, "tolerance": 0, "unit": "J"},
                "answer": "800 J",
            },
            {
                "prompt": "b) ¿Qué trabajo hace la fuerza de rozamiento en ese mismo recorrido (con su signo)? Respondé solo con el número en J.",
                "check": {"type": "numeric", "value": -800, "tolerance": 0, "unit": "J"},
                "answer": "−800 J",
            },
            {
                "prompt": "c) ¿Qué potencia media desarrolla tu fuerza? Respondé solo con el número en W.",
                "check": {"type": "numeric", "value": 50, "tolerance": 0, "unit": "W"},
                "answer": "50 W",
            },
        ],
        "hints": [
            "Solo trabaja la componente de la fuerza que está en la dirección del desplazamiento: `W = F · d · cos θ`.",
            "Si la velocidad es constante, la energía cinética no cambia, así que el trabajo neto de todas las fuerzas es cero. El peso y la normal son perpendiculares al desplazamiento.",
        ],
        "solution": [
            "a) Trabajo de una fuerza constante: `W = F · d · cos θ = 50 N × 20 m × 0.8 = 800 J`. (Error típico: usar sen 37°, que es la componente vertical y no trabaja.)",
            "b) Teorema trabajo-energía: `W_neto = ΔEk`. Como la velocidad es constante, `ΔEk = 0` y entonces `W_neto = 0`.",
            "El peso y la normal son perpendiculares al desplazamiento (`cos 90° = 0`), así que no hacen trabajo. Quedan tu fuerza y el rozamiento: `800 J + W_roz = 0`.",
            "Por lo tanto `W_roz = −800 J`: es negativo porque el rozamiento se opone al movimiento (le saca energía a la valija y la convierte en calor).",
            "c) Potencia media: `P = W / t = 800 J ÷ 16 s = 50 W`.",
            "Respuestas: 800 J, −800 J y 50 W. Verificación: la fuerza de rozamiento vale `800 J ÷ 20 m = 40 N`, igual a la componente horizontal de tu fuerza (`50 × 0.8 = 40 N`), como corresponde a velocidad constante.",
        ],
    },
    {
        "id": "f-trabajo-energia-2",
        "node": "f-trabajo-energia",
        "kind": "problem",
        "level": 2,
        "title": "Frenada de emergencia",
        "statement": (
            "Un auto de **1200 kg** viaja a **72 km/h** por una calle horizontal. El conductor clava los frenos y el auto "
            "patina hasta detenerse. Durante la frenada, la fuerza de rozamiento con el asfalto es constante y vale "
            "**6000 N**; despreciá la resistencia del aire."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánta energía cinética tiene el auto antes de frenar? Respondé solo con el número en J.",
                "check": {"type": "numeric", "value": 240000, "tolerance": 0, "unit": "J"},
                "answer": "240 000 J",
            },
            {
                "prompt": "b) ¿Qué distancia recorre patinando hasta detenerse? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 40, "tolerance": 0, "unit": "m"},
                "answer": "40 m",
            },
            {
                "prompt": "c) Si el auto hubiera ido a 108 km/h, con la misma fuerza de rozamiento, ¿qué distancia habría necesitado para detenerse? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 90, "tolerance": 0, "unit": "m"},
                "answer": "90 m",
            },
        ],
        "hints": [
            "Pasá la velocidad a m/s antes de calcular `Ek = ½ · m · v²`.",
            "El rozamiento es la única fuerza que trabaja, y lo hace en contra del movimiento: `−F_roz · d = Ek_final − Ek_inicial`, con `Ek_final = 0`.",
            "Para el inciso c) repetí la cuenta con la nueva velocidad: la distancia no crece en proporción a `v` sino a `v²`.",
        ],
        "solution": [
            "Velocidad en SI: `72 km/h ÷ 3.6 = 20 m/s`.",
            "a) `Ek = ½ · m · v² = ½ × 1200 × 20² = 600 × 400 = 240 000 J`.",
            "b) Teorema trabajo-energía: `W_neto = ΔEk`. El peso y la normal no trabajan (son perpendiculares al desplazamiento); el rozamiento hace `W = −F_roz · d`.",
            "Entonces `−6000 · d = 0 − 240 000`, de donde `d = 240 000 ÷ 6000 = 40 m`.",
            "c) Nueva velocidad: `108 km/h ÷ 3.6 = 30 m/s`. `Ek = ½ × 1200 × 30² = 600 × 900 = 540 000 J`.",
            "Distancia: `d = 540 000 ÷ 6000 = 90 m`.",
            "Respuestas: 240 000 J, 40 m y 90 m. La velocidad aumentó 1.5 veces pero la distancia de frenado aumentó `1.5² = 2.25` veces (`40 × 2.25 = 90`): el error típico es suponer que crece en la misma proporción y responder 60 m.",
        ],
    },
    {
        "id": "f-trabajo-energia-3",
        "node": "f-trabajo-energia",
        "kind": "problem",
        "level": 2,
        "title": "La montaña rusa",
        "statement": (
            "En un parque de diversiones, un carrito de montaña rusa de **500 kg** (con sus pasajeros) parte "
            "**del reposo** desde el punto A, a **20 m** de altura sobre el suelo. Baja hasta el punto B, a nivel del "
            "suelo, y vuelve a subir hasta el punto C, que está a **7.2 m** de altura. El carrito no tiene motor. "
            "Usá **g = 10 m/s²**."
        ),
        "parts": [
            {
                "prompt": "a) Suponiendo que no hay rozamiento, ¿con qué velocidad pasa por B? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "m/s"},
                "answer": "20 m/s",
            },
            {
                "prompt": "b) También sin rozamiento, ¿con qué velocidad pasa por C? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 16, "tolerance": 0, "unit": "m/s"},
                "answer": "16 m/s",
            },
            {
                "prompt": "c) En una prueba real se mide que el carrito pasa por B a 18 m/s. ¿Cuánta energía mecánica se disipó por rozamiento entre A y B? Respondé solo con el número en J.",
                "check": {"type": "numeric", "value": 19000, "tolerance": 0, "unit": "J"},
                "answer": "19 000 J",
            },
        ],
        "hints": [
            "Sin rozamiento, la energía mecánica `Ek + Ep` vale lo mismo en A, en B y en C. En A es toda potencial porque parte del reposo.",
            "Para C importa solo el desnivel entre A y C, no el camino que hizo el carrito en el medio.",
            "Con rozamiento, la energía disipada es la diferencia entre la energía mecánica que tenía en A y la que tiene en B.",
        ],
        "solution": [
            "Energía mecánica en A (tomando `Ep = 0` en el suelo y con `v = 0`): `E_A = m · g · h = 500 × 10 × 20 = 100 000 J`.",
            "a) En B toda esa energía es cinética: `½ · m · v_B² = m · g · h_A`, o sea `v_B² = 2 · g · h_A = 2 × 10 × 20 = 400`, y `v_B = 20 m/s`.",
            "b) Entre A y C: `m · g · h_A = ½ · m · v_C² + m · g · h_C`, de donde `v_C² = 2 · g · (h_A − h_C) = 2 × 10 × (20 − 7.2) = 2 × 10 × 12.8 = 256`.",
            "Entonces `v_C = √256 = 16 m/s`. La masa se canceló en los dos incisos: sin rozamiento, la velocidad no depende de cuánto pese el carrito.",
            "c) Energía mecánica real en B: `Ek = ½ × 500 × 18² = 250 × 324 = 81 000 J` (la potencial es cero).",
            "Energía disipada: `E_A − E_B = 100 000 − 81 000 = 19 000 J`, que pasaron a calor en ruedas, rieles y aire.",
            "Respuestas: 20 m/s, 16 m/s y 19 000 J. Error típico en c): restar velocidades (`20 − 18 = 2 m/s`) y calcular `½ · m · 2²`; las energías se restan, las velocidades no.",
        ],
    },
    {
        "id": "f-trabajo-energia-4",
        "node": "f-trabajo-energia",
        "kind": "problem",
        "level": 3,
        "title": "Rampa, tramo rugoso y resorte",
        "statement": (
            "Un bloque de **2 kg** se suelta **desde el reposo** en lo alto de una rampa **sin rozamiento**, a "
            "**3.2 m** de altura respecto de una pista horizontal. Al pie de la rampa, la pista horizontal tiene un "
            "tramo **rugoso de 2.8 m** de largo, con coeficiente de rozamiento dinámico `μ = 0.25`. Después de ese "
            "tramo la pista vuelve a ser lisa y termina en un resorte horizontal ideal de constante "
            "**k = 2500 N/m**, fijo a una pared. Usá **g = 10 m/s²** y despreciá la resistencia del aire."
        ),
        "parts": [
            {
                "prompt": "a) ¿Con qué velocidad llega el bloque al pie de la rampa, justo antes de entrar al tramo rugoso? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": "m/s"},
                "answer": "8 m/s",
            },
            {
                "prompt": "b) ¿Cuál es la compresión máxima del resorte? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 0.2, "tolerance": 0, "unit": "m"},
                "answer": "0.2 m",
            },
            {
                "prompt": "c) El resorte devuelve el bloque, que cruza otra vez el tramo rugoso y sube por la rampa. ¿Hasta qué altura máxima llega? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 1.8, "tolerance": 0, "unit": "m"},
                "answer": "1.8 m",
            },
        ],
        "hints": [
            "Hacé un balance de energía entre estados: arriba de la rampa (solo `Ep`), al pie (solo `Ek`), resorte comprimido al máximo (solo `Ee`, porque ahí el bloque está quieto un instante).",
            "En el tramo rugoso horizontal la normal vale `m · g`, así que el rozamiento es `μ · m · g` y disipa `μ · m · g · d` cada vez que el bloque lo cruza.",
            "A la vuelta el bloque cruza el tramo rugoso por segunda vez: descontá esa pérdida de nuevo antes de igualar a `m · g · h`.",
        ],
        "solution": [
            "Energía inicial (toda potencial, con `Ep = 0` en la pista): `E₀ = m · g · h = 2 × 10 × 3.2 = 64 J`.",
            "a) La rampa no tiene rozamiento, así que al pie `½ · m · v² = 64 J`: `v² = 2 × 64 ÷ 2 = 64` y `v = 8 m/s`.",
            "Rozamiento en el tramo rugoso: la normal es `N = m · g = 20 N`, entonces `F_roz = μ · N = 0.25 × 20 = 5 N`. En cada cruce disipa `5 N × 2.8 m = 14 J`.",
            "b) Energía con la que llega al resorte: `64 − 14 = 50 J`. En la compresión máxima el bloque está detenido y toda esa energía es elástica: `½ · k · x² = 50`.",
            "`x² = 2 × 50 ÷ 2500 = 0.04`, de donde `x = 0.2 m` (20 cm).",
            "c) El resorte ideal le devuelve los 50 J. Al cruzar el tramo rugoso de vuelta pierde otros 14 J: llega al pie de la rampa con `50 − 14 = 36 J`.",
            "Sube hasta que toda esa energía es potencial: `m · g · h' = 36`, o sea `h' = 36 ÷ (2 × 10) = 1.8 m`.",
            "Respuestas: 8 m/s, 0.2 m y 1.8 m. Verificación: `64 J − 2 × 14 J = 36 J`. Error típico: descontar el rozamiento una sola vez y responder 2.5 m.",
        ],
    },
    # ============================================================
    # f-momento-choques
    # ============================================================
    {
        "id": "f-momento-choques-1",
        "node": "f-momento-choques",
        "kind": "problem",
        "level": 1,
        "title": "Pelota contra el frontón",
        "statement": (
            "Una pelota de tenis de **0.06 kg** (60 g) llega horizontalmente a un frontón a **25 m/s** y rebota en la "
            "misma dirección pero en sentido contrario, a **15 m/s**. El contacto con la pared dura **0.005 s**. "
            "Tomá como positivo el sentido en que la pelota viaja hacia la pared y despreciá el peso durante el contacto."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la variación del momento lineal de la pelota, `Δp`, con su signo? Respondé solo con el número en kg·m/s.",
                "check": {"type": "numeric", "value": -2.4, "tolerance": 0, "unit": "kg·m/s"},
                "answer": "−2.4 kg·m/s",
            },
            {
                "prompt": "b) ¿Cuál es el módulo de la fuerza media que la pared le hace a la pelota? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 480, "tolerance": 0, "unit": "N"},
                "answer": "480 N",
            },
            {
                "prompt": "c) Si en lugar de rebotar la pelota quedara detenida contra la pared (misma velocidad de llegada y mismo tiempo de contacto), ¿cuál sería el módulo de la fuerza media? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 300, "tolerance": 0, "unit": "N"},
                "answer": "300 N",
            },
        ],
        "hints": [
            "El momento lineal es un vector: con el sentido positivo elegido, la velocidad de llegada es `+25 m/s` y la de salida es `−15 m/s`.",
            "`Δp = p_final − p_inicial` y la fuerza media sale del impulso: `F · Δt = Δp`.",
        ],
        "solution": [
            "Con positivo hacia la pared: `v_inicial = +25 m/s` y `v_final = −15 m/s` (vuelve).",
            "Momentos: `p_inicial = 0.06 × 25 = 1.5 kg·m/s` y `p_final = 0.06 × (−15) = −0.9 kg·m/s`.",
            "a) `Δp = p_final − p_inicial = −0.9 − 1.5 = −2.4 kg·m/s`. El signo negativo indica que el cambio apunta en sentido contrario a la pared (la pared empuja la pelota hacia afuera).",
            "b) Impulso: `F · Δt = Δp`, entonces `|F| = 2.4 ÷ 0.005 = 480 N` (unas 800 veces el peso de la pelota, que es 0.6 N: por eso se puede despreciar).",
            "c) Si queda detenida, `Δp = 0 − 1.5 = −1.5 kg·m/s` y `|F| = 1.5 ÷ 0.005 = 300 N`.",
            "Respuestas: −2.4 kg·m/s, 480 N y 300 N. Rebotar exige más fuerza que frenar, porque hay que anular el momento y además darle momento en sentido contrario. Error típico: restar los módulos (`25 − 15 = 10 m/s`) y obtener `Δp = 0.6 kg·m/s`.",
        ],
    },
    {
        "id": "f-momento-choques-2",
        "node": "f-momento-choques",
        "kind": "problem",
        "level": 2,
        "title": "Choque frontal en la ruta",
        "statement": (
            "En una ruta recta, una camioneta de **2000 kg** que va hacia el este a **20 m/s** choca de frente con un "
            "auto de **1000 kg** que venía hacia el oeste a **10 m/s**. Después del choque quedan enganchados. "
            "Despreciá las fuerzas externas durante el choque y tomá el este como sentido positivo."
        ),
        "parts": [
            {
                "prompt": "a) ¿Con qué velocidad (con su signo) se mueve el conjunto justo después del choque? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "m/s"},
                "answer": "10 m/s (hacia el este)",
            },
            {
                "prompt": "b) ¿Cuánta energía cinética se pierde en el choque? Respondé solo con el número en J.",
                "check": {"type": "numeric", "value": 300000, "tolerance": 0, "unit": "J"},
                "answer": "300 000 J",
            },
            {
                "prompt": "c) ¿Cuál es el módulo del cambio de momento lineal que sufre el auto? Respondé solo con el número en kg·m/s.",
                "check": {"type": "numeric", "value": 20000, "tolerance": 0, "unit": "kg·m/s"},
                "answer": "20 000 kg·m/s",
            },
        ],
        "hints": [
            "El momento total se conserva, pero es un vector: la velocidad del auto antes del choque es `−10 m/s`.",
            "Como quedan enganchados, después del choque hay una sola velocidad para la masa total. La energía perdida es `Ek_antes − Ek_después` (ahí sí se suman las energías de los dos, siempre positivas).",
            "Para el inciso c) compará la velocidad del auto antes y después, cada una con su signo.",
        ],
        "solution": [
            "Momento total antes: `p = 2000 × 20 + 1000 × (−10) = 40 000 − 10 000 = 30 000 kg·m/s`.",
            "a) Choque perfectamente inelástico: `p = (m₁ + m₂) · v`, entonces `v = 30 000 ÷ 3000 = 10 m/s`. Positivo: el conjunto sigue hacia el este.",
            "b) Energía cinética antes: `½ × 2000 × 20² + ½ × 1000 × 10² = 400 000 + 50 000 = 450 000 J` (la energía no tiene signo: las dos suman).",
            "Energía cinética después: `½ × 3000 × 10² = 150 000 J`.",
            "Energía perdida: `450 000 − 150 000 = 300 000 J` (dos tercios del total), que se fueron en deformar la chapa, ruido y calor.",
            "c) El auto pasa de `−10 m/s` a `+10 m/s`: `Δp = 1000 × (10 − (−10)) = 20 000 kg·m/s`.",
            "Respuestas: 10 m/s hacia el este, 300 000 J y 20 000 kg·m/s. Verificación: la camioneta cambia `2000 × (10 − 20) = −20 000 kg·m/s`, igual y opuesto. Pero el auto cambió su velocidad en 20 m/s y la camioneta solo en 10 m/s: por eso el vehículo liviano lleva la peor parte.",
        ],
    },
    {
        "id": "f-momento-choques-3",
        "node": "f-momento-choques",
        "kind": "problem",
        "level": 2,
        "title": "Dos carritos y un resorte comprimido",
        "statement": (
            "Dos carritos de laboratorio, A de **1 kg** y B de **3 kg**, están en reposo sobre un riel horizontal "
            "**sin rozamiento**, atados por un hilo y con un resorte liviano comprimido entre ellos. El resorte guarda "
            "**24 J** de energía elástica. Se quema el hilo: el resorte se expande, empuja a los carritos en sentidos "
            "opuestos y les entrega toda su energía."
        ),
        "parts": [
            {
                "prompt": "a) ¿Con qué rapidez sale el carrito A? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": "m/s"},
                "answer": "6 m/s",
            },
            {
                "prompt": "b) ¿Con qué rapidez sale el carrito B? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "m/s"},
                "answer": "2 m/s",
            },
            {
                "prompt": "c) ¿Qué fracción de la energía del resorte se lleva el carrito A? Respondé solo con el número (fracción o decimal).",
                "check": {"type": "numeric", "value": 0.75, "tolerance": 0, "unit": ""},
                "answer": "3/4 (0.75)",
            },
        ],
        "hints": [
            "Hay dos incógnitas (las dos rapideces), así que hacen falta dos ecuaciones: conservación del momento lineal y conservación de la energía.",
            "El momento total antes es cero, así que después los dos momentos tienen igual módulo: `m_A · v_A = m_B · v_B`. De ahí sale `v_A` en función de `v_B`.",
            "Reemplazá esa relación en `½ · m_A · v_A² + ½ · m_B · v_B² = 24 J`.",
        ],
        "solution": [
            "Sobre el sistema no actúan fuerzas externas horizontales, así que el momento total se conserva y vale cero (estaban quietos): `m_A · v_A = m_B · v_B` en módulo.",
            "`1 · v_A = 3 · v_B`, es decir `v_A = 3 · v_B`: el carrito liviano sale tres veces más rápido.",
            "Conservación de la energía (sin rozamiento, toda la energía elástica pasa a cinética): `½ × 1 × v_A² + ½ × 3 × v_B² = 24`.",
            "Reemplazando `v_A = 3 · v_B`: `½ × 9 · v_B² + 1.5 · v_B² = 6 · v_B² = 24`, de donde `v_B² = 4` y `v_B = 2 m/s`.",
            "Entonces `v_A = 3 × 2 = 6 m/s`.",
            "c) `Ek_A = ½ × 1 × 6² = 18 J` y `Ek_B = ½ × 3 × 2² = 6 J` (suman 24 J). Fracción de A: `18 ÷ 24 = 3/4`.",
            "Respuestas: 6 m/s, 2 m/s y 3/4. El momento se reparte en partes iguales (6 kg·m/s cada uno, en sentidos opuestos), pero la energía no: el más liviano se lleva la mayor parte. Error típico: repartir la energía mitad y mitad.",
        ],
    },
    {
        "id": "f-momento-choques-4",
        "node": "f-momento-choques",
        "kind": "problem",
        "level": 3,
        "title": "Un choque elástico y después uno plástico",
        "statement": (
            "Sobre un riel horizontal **sin rozamiento**, un carrito A de **2 kg** que se mueve a **6 m/s** hacia la "
            "derecha choca de frente, en forma **perfectamente elástica**, con un carrito B de **4 kg** que está en "
            "reposo. Más adelante, B choca con un carrito C de **12 kg**, también en reposo, y queda pegado a él "
            "(choque perfectamente inelástico). Todo ocurre sobre la misma recta; tomá positivo hacia la derecha."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué velocidad (con su signo) tiene A después del primer choque? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": -2, "tolerance": 0, "unit": "m/s"},
                "answer": "−2 m/s (rebota hacia la izquierda)",
            },
            {
                "prompt": "b) ¿Qué velocidad tiene B después del primer choque? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "m/s"},
                "answer": "4 m/s",
            },
            {
                "prompt": "c) ¿Cuánta energía cinética se pierde en el segundo choque (el de B con C)? Respondé solo con el número en J.",
                "check": {"type": "numeric", "value": 24, "tolerance": 0, "unit": "J"},
                "answer": "24 J",
            },
        ],
        "hints": [
            "En el choque elástico se conservan el momento lineal y la energía cinética: son dos ecuaciones para las dos velocidades finales.",
            "Atajo válido para choques elásticos en una dimensión: la velocidad relativa se invierte, `v_A − v_B = −(v_A' − v_B')`. Con B en reposo: `v_B' − v_A' = 6`.",
            "En el segundo choque solo se conserva el momento; B y C salen juntos. Compará la energía cinética antes y después de ese choque.",
        ],
        "solution": [
            "Primer choque, conservación del momento: `2 × 6 + 4 × 0 = 2 · v_A' + 4 · v_B'`, o sea `2 · v_A' + 4 · v_B' = 12`.",
            "Por ser elástico se conserva también la energía cinética, lo que en una dimensión equivale a que la velocidad relativa se invierte: `v_B' − v_A' = 6 − 0 = 6`, es decir `v_B' = v_A' + 6`.",
            "Reemplazando: `2 · v_A' + 4 · (v_A' + 6) = 12` → `6 · v_A' = −12` → `v_A' = −2 m/s`. A rebota hacia la izquierda porque chocó contra un carrito más pesado.",
            "b) `v_B' = −2 + 6 = 4 m/s`. Verificación con la energía: antes `½ × 2 × 6² = 36 J`; después `½ × 2 × 2² + ½ × 4 × 4² = 4 + 32 = 36 J`. Se conserva.",
            "Segundo choque (inelástico), conservación del momento: `4 × 4 + 12 × 0 = (4 + 12) · v`, de donde `v = 16 ÷ 16 = 1 m/s`.",
            "Energía cinética antes del segundo choque: `½ × 4 × 4² = 32 J`. Después: `½ × 16 × 1² = 8 J`.",
            "c) Energía perdida: `32 − 8 = 24 J` (tres cuartas partes de la que traía B).",
            "Respuestas: −2 m/s, 4 m/s y 24 J. Error típico en el primer choque: usar solo el momento y suponer que A queda quieto; eso solo pasa cuando las dos masas son iguales.",
        ],
    },
    # ============================================================
    # f-torque-rotacion
    # ============================================================
    {
        "id": "f-torque-rotacion-1",
        "node": "f-torque-rotacion",
        "kind": "problem",
        "level": 1,
        "title": "Parado sobre el pedal",
        "statement": (
            "Un ciclista de **60 kg** se para sobre un pedal de su bicicleta y apoya en él todo su peso (una fuerza "
            "vertical hacia abajo). La biela, que es la palanca que une el pedal con el eje, mide **18 cm**. "
            "Usá **g = 10 m/s²** y calculá los torques respecto del eje de los pedales."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué torque produce el peso del ciclista cuando la biela está horizontal? Respondé solo con el número en N·m.",
                "check": {"type": "numeric", "value": 108, "tolerance": 0, "unit": "N·m"},
                "answer": "108 N·m",
            },
            {
                "prompt": "b) ¿Y cuando la biela forma 30° con la vertical (sen 30° = 0.5)? Respondé solo con el número en N·m.",
                "check": {"type": "numeric", "value": 54, "tolerance": 0, "unit": "N·m"},
                "answer": "54 N·m",
            },
            {
                "prompt": "c) ¿En qué posición de la biela el peso del ciclista no produce ningún torque sobre el eje?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Con la biela vertical (pedal en el punto más alto o más bajo)",
                        "Con la biela horizontal",
                        "Con la biela a 45° de la vertical",
                        "En ninguna: el peso siempre produce torque",
                    ],
                    "correct": 0,
                },
                "answer": "Con la biela vertical (pedal en el punto más alto o más bajo)",
            },
        ],
        "hints": [
            "`τ = r · F · sen θ`, donde `θ` es el ángulo entre la biela (que va del eje al pedal) y la fuerza. Pasá la longitud de la biela a metros.",
            "La fuerza es vertical. Si la biela está horizontal, el ángulo entre ambas es 90°; si la biela forma 30° con la vertical, el ángulo entre ambas es 30°.",
        ],
        "solution": [
            "Fuerza aplicada: el peso, `F = m · g = 60 × 10 = 600 N`, vertical hacia abajo. Brazo: `r = 18 cm = 0.18 m`.",
            "a) Biela horizontal y fuerza vertical: `θ = 90°`, `sen 90° = 1`. `τ = r · F = 0.18 × 600 = 108 N·m`. Es el torque máximo posible.",
            "b) Si la biela forma 30° con la vertical, ese es justamente el ángulo entre la biela y la fuerza (que es vertical): `τ = 0.18 × 600 × sen 30° = 108 × 0.5 = 54 N·m`.",
            "c) El torque se anula cuando `sen θ = 0`, es decir cuando la fuerza es paralela a la biela (`θ = 0°` o `180°`): con la biela vertical, el peso apunta hacia el eje o en sentido opuesto y no hace girar nada.",
            "Respuestas: 108 N·m, 54 N·m y biela vertical. Por eso al pedalear se empuja fuerte cuando la biela pasa por la horizontal, y en los puntos alto y bajo (los puntos muertos) el empuje vertical no sirve. Error típico: reemplazar `r = 18` sin pasar a metros.",
        ],
    },
    {
        "id": "f-torque-rotacion-2",
        "node": "f-torque-rotacion",
        "kind": "problem",
        "level": 2,
        "title": "Torque neto sobre una barra",
        "statement": (
            "Una barra liviana (masa despreciable) de **1.2 m** de largo está apoyada sobre una mesa horizontal y puede "
            "girar sin rozamiento alrededor de un eje vertical que pasa por su extremo O. Vista desde arriba, sobre la "
            "barra actúan tres fuerzas horizontales: **F₁ = 50 N**, aplicada en el extremo libre y perpendicular a la "
            "barra, que tiende a hacerla girar en sentido antihorario; **F₂ = 80 N**, aplicada en el punto medio de la "
            "barra y formando **30°** con ella (sen 30° = 0.5), que tiende a hacerla girar en sentido horario; y "
            "**F₃ = 100 N**, aplicada en el extremo libre y dirigida a lo largo de la barra, hacia el eje. "
            "Tomá como positivo el sentido antihorario."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale el torque de F₂ respecto de O, con su signo? Respondé solo con el número en N·m.",
                "check": {"type": "numeric", "value": -24, "tolerance": 0, "unit": "N·m"},
                "answer": "−24 N·m",
            },
            {
                "prompt": "b) ¿Cuánto vale el torque neto respecto de O, con su signo? Respondé solo con el número en N·m.",
                "check": {"type": "numeric", "value": 36, "tolerance": 0, "unit": "N·m"},
                "answer": "36 N·m (antihorario)",
            },
            {
                "prompt": "c) ¿Qué módulo debe tener una cuarta fuerza, perpendicular a la barra y aplicada a 0.9 m de O, para que la barra quede en equilibrio de rotación? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 40, "tolerance": 0, "unit": "N"},
                "answer": "40 N",
            },
        ],
        "hints": [
            "Calculá el torque de cada fuerza por separado con `τ = r · F · sen θ`, usando la distancia de O al punto de aplicación, y ponele signo según el sentido de giro.",
            "Una fuerza cuya recta de acción pasa por el eje no produce torque, por grande que sea.",
            "Equilibrio de rotación: la cuarta fuerza tiene que producir un torque igual y opuesto al torque neto de las otras tres.",
        ],
        "solution": [
            "Torque de F₁: `r = 1.2 m`, perpendicular (`sen 90° = 1`), antihorario: `τ₁ = +1.2 × 50 = +60 N·m`.",
            "a) Torque de F₂: está en el punto medio, `r = 0.6 m`, con `θ = 30°`, horario: `τ₂ = −0.6 × 80 × 0.5 = −24 N·m`.",
            "Torque de F₃: su recta de acción pasa por O (`θ = 180°`, `sen θ = 0`), así que `τ₃ = 0`, aunque sea la fuerza más grande.",
            "b) Torque neto: `Στ = 60 − 24 + 0 = +36 N·m`. La barra tiende a girar en sentido antihorario.",
            "c) Para el equilibrio hace falta `Στ = 0`: la cuarta fuerza debe dar `−36 N·m` (sentido horario). Como es perpendicular y está a 0.9 m: `0.9 · F₄ = 36`, entonces `F₄ = 36 ÷ 0.9 = 40 N`.",
            "Respuestas: −24 N·m, +36 N·m y 40 N (empujando en sentido horario). Errores típicos: usar `r = 1.2 m` para F₂ (está en el punto medio) o contar a F₃ como si hiciera torque.",
        ],
    },
    {
        "id": "f-torque-rotacion-3",
        "node": "f-torque-rotacion",
        "kind": "problem",
        "level": 2,
        "title": "Subibaja con el pivote corrido",
        "statement": (
            "En una plaza armaron un subibaja con un tablón **homogéneo** de **4 m** de largo y **20 kg**, apoyado sobre "
            "un pivote ubicado a **1.5 m** del extremo izquierdo (no está centrado). Sofía, de **30 kg**, se sienta justo "
            "en el extremo izquierdo. Tomás, de **20 kg**, se sienta del lado derecho. Usá **g = 10 m/s²**."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el módulo del torque que hace el peso del tablón respecto del pivote? Respondé solo con el número en N·m.",
                "check": {"type": "numeric", "value": 100, "tolerance": 0, "unit": "N·m"},
                "answer": "100 N·m",
            },
            {
                "prompt": "b) ¿A qué distancia del pivote debe sentarse Tomás para que el tablón quede en equilibrio horizontal? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 1.75, "tolerance": 0, "unit": "m"},
                "answer": "1.75 m",
            },
            {
                "prompt": "c) En esa situación de equilibrio, ¿qué fuerza hace el pivote sobre el tablón? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 700, "tolerance": 0, "unit": "N"},
                "answer": "700 N",
            },
        ],
        "hints": [
            "El peso de un tablón homogéneo se considera aplicado en su centro (a 2 m de cada extremo). Fijate de qué lado del pivote queda ese punto y a qué distancia.",
            "Planteá `Στ = 0` respecto del pivote: de un lado gira Sofía; del otro, el tablón y Tomás. La fuerza del pivote no hace torque respecto de sí mismo.",
            "Para el inciso c) usá el equilibrio de fuerzas verticales: el pivote sostiene todos los pesos.",
        ],
        "solution": [
            "Pesos: Sofía `30 × 10 = 300 N`, Tomás `20 × 10 = 200 N`, tablón `20 × 10 = 200 N`.",
            "a) El centro del tablón está a 2 m del extremo izquierdo y el pivote a 1.5 m: el peso del tablón actúa `2 − 1.5 = 0.5 m` a la derecha del pivote. `τ_tablón = 200 × 0.5 = 100 N·m` (tiende a bajar el lado derecho).",
            "Torque de Sofía (a 1.5 m, a la izquierda del pivote): `300 × 1.5 = 450 N·m` (tiende a bajar el lado izquierdo).",
            "b) Equilibrio de rotación respecto del pivote: `450 = 100 + 200 · d`, de donde `200 · d = 350` y `d = 1.75 m`.",
            "Es posible: del lado derecho hay `4 − 1.5 = 2.5 m` de tablón, y Tomás queda a 1.75 m del pivote.",
            "c) Equilibrio de fuerzas verticales: el pivote empuja hacia arriba con `N = 300 + 200 + 200 = 700 N`.",
            "Respuestas: 100 N·m, 1.75 m y 700 N. Error típico: olvidar el peso del tablón y plantear `300 × 1.5 = 200 · d`, que da 2.25 m; el tablón solo no se cancela porque el pivote no está en su centro.",
        ],
    },
    {
        "id": "f-torque-rotacion-4",
        "node": "f-torque-rotacion",
        "kind": "problem",
        "level": 3,
        "title": "La barrera con contrapeso",
        "statement": (
            "La barrera de un paso a nivel es una barra **homogénea** de **6 m** de largo y **30 kg** que gira alrededor "
            "de un eje horizontal ubicado a **1 m** de uno de sus extremos. Justo en ese extremo corto lleva fijo un "
            "contrapeso, que puede considerarse puntual. Usá **g = 10 m/s²**, despreciá el rozamiento en el eje y "
            "tomá sen 37° = 0.6 y cos 37° = 0.8."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué masa debe tener el contrapeso para que la barrera quede en equilibrio en posición horizontal, sin ninguna otra fuerza? Respondé solo con el número en kg.",
                "check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": "kg"},
                "answer": "60 kg",
            },
            {
                "prompt": "b) Se instala un contrapeso de 50 kg. ¿Qué fuerza vertical hacia arriba hay que hacer en la punta del lado largo para sostener la barrera horizontal? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "N"},
                "answer": "20 N",
            },
            {
                "prompt": "c) Con el contrapeso de 50 kg y sin esa fuerza, ¿cuál es el módulo del torque neto de los pesos respecto del eje cuando la barrera está levantada 53° sobre la horizontal? Respondé solo con el número en N·m.",
                "check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": "N·m"},
                "answer": "60 N·m",
            },
        ],
        "hints": [
            "El peso de la barra entera se aplica en su centro, a 3 m de cada extremo. No hace falta partir la barra en dos tramos: alcanza con ubicar ese centro respecto del eje.",
            "Con la barrera horizontal los pesos son perpendiculares a ella. Planteá `Στ = 0` respecto del eje; la punta del lado largo está a 5 m del eje.",
            "Con la barrera levantada 53°, cada peso (vertical) forma 37° con la barra: todos los torques quedan multiplicados por sen 37°.",
        ],
        "solution": [
            "Peso de la barra: `30 × 10 = 300 N`, aplicado en su centro, a 3 m del extremo corto. Como el eje está a 1 m de ese extremo, el centro queda a `3 − 1 = 2 m` del eje, del lado largo.",
            "Torque del peso de la barra con la barrera horizontal: `300 × 2 = 600 N·m` (tiende a bajar el lado largo).",
            "a) El contrapeso está a 1 m del eje, del otro lado. Equilibrio: `M · g × 1 = 600`, entonces `M · 10 = 600` y `M = 60 kg`.",
            "b) Con 50 kg, el contrapeso hace `500 × 1 = 500 N·m`, menos que los 600 N·m de la barra: el lado largo tiende a bajar con un torque neto de `600 − 500 = 100 N·m`.",
            "La fuerza hacia arriba en la punta larga, a `6 − 1 = 5 m` del eje, debe compensarlo: `5 · F = 100`, entonces `F = 20 N`.",
            "c) Levantada 53°, la barra forma `90° − 53° = 37°` con la vertical, que es la dirección de los pesos. Cada torque es `r · F · sen 37°`: barra `2 × 300 × 0.6 = 360 N·m`; contrapeso `1 × 500 × 0.6 = 300 N·m`, en sentido opuesto.",
            "Torque neto: `360 − 300 = 60 N·m`, que tiende a bajar el lado largo (a cerrar la barrera).",
            "Respuestas: 60 kg, 20 N y 60 N·m. Verificación: el torque neto horizontal (100 N·m) multiplicado por sen 37° = 0.6 da 60 N·m. Error típico en a): ubicar el peso de la barra en el centro del tramo largo (a 2.5 m del eje) sin descontar el tramo corto.",
        ],
    },
    # ============================================================
    # f-fluidos
    # ============================================================
    {
        "id": "f-fluidos-1",
        "node": "f-fluidos",
        "kind": "problem",
        "level": 1,
        "title": "La presión en la canilla de planta baja",
        "statement": (
            "En un edificio, el tanque de agua está en la terraza y abierto a la atmósfera. Una canilla cerrada de la "
            "planta baja está **25 m** por debajo del nivel del agua del tanque; el agua de la cañería está en reposo. "
            "Datos: densidad del agua **1000 kg/m³**, **g = 10 m/s²** y presión atmosférica **P₀ = 100 kPa**."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la presión debida solo a la columna de agua (presión hidrostática o manométrica) a la altura de la canilla? Respondé solo con el número en kPa.",
                "check": {"type": "numeric", "value": 250, "tolerance": 0, "unit": "kPa"},
                "answer": "250 kPa",
            },
            {
                "prompt": "b) ¿Cuánto vale la presión absoluta del agua en la canilla? Respondé solo con el número en kPa.",
                "check": {"type": "numeric", "value": 350, "tolerance": 0, "unit": "kPa"},
                "answer": "350 kPa",
            },
            {
                "prompt": "c) El cierre de la canilla tapa una abertura de 2 cm² y del lado de afuera hay aire a presión atmosférica. ¿Qué fuerza neta soporta el cierre? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 50, "tolerance": 0, "unit": "N"},
                "answer": "50 N",
            },
        ],
        "hints": [
            "La columna de agua aporta `ρ · g · h`. El resultado sale en pascales: `1 kPa = 1000 Pa`.",
            "Presión absoluta = presión atmosférica + presión de la columna de agua (`P = P₀ + ρ · g · h`).",
            "La atmósfera empuja el cierre de los dos lados, así que la fuerza neta sale de la diferencia de presiones. Pasá el área a m²: `1 cm² = 10⁻⁴ m²`.",
        ],
        "solution": [
            "a) Presión de la columna de agua: `ρ · g · h = 1000 × 10 × 25 = 250 000 Pa = 250 kPa`.",
            "b) Presión absoluta: `P = P₀ + ρ · g · h = 100 kPa + 250 kPa = 350 kPa` (3.5 veces la atmosférica).",
            "c) Del lado del agua la presión es 350 kPa y del lado de afuera 100 kPa: la diferencia es `350 − 100 = 250 kPa = 250 000 Pa`, justamente la presión manométrica.",
            "Área en SI: `2 cm² = 2 × 10⁻⁴ m²`.",
            "Fuerza neta: `F = ΔP · A = 250 000 × 2 × 10⁻⁴ = 50 N` (como sostener unos 5 kg).",
            "Respuestas: 250 kPa, 350 kPa y 50 N. Errores típicos: usar la presión absoluta en c) (daría 70 N, pero la atmósfera también empuja desde afuera) o no convertir los cm² a m².",
        ],
    },
    {
        "id": "f-fluidos-2",
        "node": "f-fluidos",
        "kind": "problem",
        "level": 2,
        "title": "El elevador hidráulico del taller",
        "statement": (
            "En un taller mecánico, un elevador hidráulico tiene un pistón chico de **4 cm de diámetro** y un pistón "
            "grande de **40 cm de diámetro**, los dos circulares y a la misma altura. Sobre el pistón grande hay un auto "
            "de **1500 kg**. El aceite es incompresible; despreciá el peso de los pistones y el rozamiento. "
            "Usá **g = 10 m/s²**."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué fuerza hay que hacer sobre el pistón chico para sostener el auto? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 150, "tolerance": 0, "unit": "N"},
                "answer": "150 N",
            },
            {
                "prompt": "b) Si, sumando varios bombeos, el pistón chico baja en total 50 cm, ¿cuánto sube el auto? Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 0.5, "tolerance": 0, "unit": "cm"},
                "answer": "0.5 cm",
            },
            {
                "prompt": "c) ¿Qué trabajo se hace sobre el pistón chico al bajarlo esos 50 cm con la fuerza del inciso a)? Respondé solo con el número en J.",
                "check": {"type": "numeric", "value": 75, "tolerance": 0, "unit": "J"},
                "answer": "75 J",
            },
        ],
        "hints": [
            "Pascal: `F₁ / A₁ = F₂ / A₂`. Las áreas son círculos: dependen del **cuadrado** del diámetro, así que no hace falta usar π, alcanza con la relación entre áreas.",
            "El aceite es incompresible: el volumen que sale del cilindro chico es el que entra al grande, `A₁ · d₁ = A₂ · d₂`.",
            "Trabajo = fuerza × desplazamiento, con el desplazamiento en metros.",
        ],
        "solution": [
            "Relación de áreas: `A₂ / A₁ = (D₂ / D₁)² = (40 / 4)² = 10² = 100`. (Error típico: usar la relación de diámetros, 10.)",
            "Peso del auto: `F₂ = m · g = 1500 × 10 = 15 000 N`.",
            "a) Pascal: `F₁ / A₁ = F₂ / A₂`, entonces `F₁ = F₂ · A₁ / A₂ = 15 000 ÷ 100 = 150 N` (como levantar 15 kg).",
            "b) Conservación del volumen de aceite: `A₁ · d₁ = A₂ · d₂`, entonces `d₂ = d₁ · A₁ / A₂ = 50 cm ÷ 100 = 0.5 cm`.",
            "c) Trabajo sobre el pistón chico: `W = F₁ · d₁ = 150 N × 0.5 m = 75 J`.",
            "Respuestas: 150 N, 0.5 cm y 75 J. Verificación: el trabajo que recibe el auto es `15 000 N × 0.005 m = 75 J`, el mismo. La prensa multiplica la fuerza por 100 pero divide el recorrido por 100: no regala energía.",
        ],
    },
    {
        "id": "f-fluidos-3",
        "node": "f-fluidos",
        "kind": "problem",
        "level": 2,
        "title": "La pieza colgada del dinamómetro",
        "statement": (
            "Una pieza maciza de plástico se cuelga de un dinamómetro. En el aire, el dinamómetro marca **6 N**; con la "
            "pieza totalmente sumergida en agua, sin tocar el fondo, marca **1 N**. Después se descuelga la pieza y se la "
            "suelta en un recipiente con un líquido de densidad **1500 kg/m³**, donde flota en equilibrio. "
            "Datos: densidad del agua **1000 kg/m³** y **g = 10 m/s²**; despreciá el empuje del aire."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el volumen de la pieza? Respondé solo con el número en cm³.",
                "check": {"type": "numeric", "value": 500, "tolerance": 0, "unit": "cm³"},
                "answer": "500 cm³",
            },
            {
                "prompt": "b) ¿Cuál es la densidad del plástico? Respondé solo con el número en kg/m³.",
                "check": {"type": "numeric", "value": 1200, "tolerance": 0, "unit": "kg/m³"},
                "answer": "1200 kg/m³",
            },
            {
                "prompt": "c) Cuando flota en el líquido de 1500 kg/m³, ¿qué porcentaje de su volumen queda sumergido? Respondé solo con el número en %.",
                "check": {"type": "numeric", "value": 80, "tolerance": 0, "unit": "%"},
                "answer": "80 %",
            },
        ],
        "hints": [
            "La diferencia entre lo que marca el dinamómetro en el aire y en el agua es el empuje: `E = P − P_aparente`.",
            "Como está totalmente sumergida, `E = ρ_agua · V · g` con `V` el volumen completo de la pieza. Recordá que `1 m³ = 10⁶ cm³`.",
            "Al flotar, el empuje iguala al peso: `ρ_líq · V_sum · g = ρ_obj · V · g`. La fracción sumergida es `ρ_obj / ρ_líq`.",
        ],
        "solution": [
            "Empuje en el agua: `E = P − P_aparente = 6 N − 1 N = 5 N`.",
            "a) Arquímedes con la pieza totalmente sumergida: `E = ρ_agua · V · g`, entonces `V = 5 ÷ (1000 × 10) = 5 × 10⁻⁴ m³`.",
            "En cm³: `5 × 10⁻⁴ m³ × 10⁶ cm³/m³ = 500 cm³`.",
            "b) Masa de la pieza: `m = P / g = 6 ÷ 10 = 0.6 kg`. Densidad: `ρ = m / V = 0.6 ÷ (5 × 10⁻⁴) = 1200 kg/m³`. Es mayor que la del agua: por eso en agua se hunde y el dinamómetro todavía marca algo.",
            "c) En el líquido de 1500 kg/m³ flota porque `1200 < 1500`. En equilibrio `E = P`: `ρ_líq · V_sum · g = ρ_obj · V · g`, de donde `V_sum / V = 1200 ÷ 1500 = 0.8`.",
            "Queda sumergido el 80 % del volumen (400 cm³) y asoma el 20 %.",
            "Respuestas: 500 cm³, 1200 kg/m³ y 80 %. Verificación: el empuje al flotar es `1500 × 4 × 10⁻⁴ × 10 = 6 N`, igual al peso. Error típico: tomar el empuje como 1 N (la lectura sumergida) en vez de la diferencia.",
        ],
    },
    {
        "id": "f-fluidos-4",
        "node": "f-fluidos",
        "kind": "problem",
        "level": 3,
        "title": "La cañería que sube y se angosta",
        "statement": (
            "Por la cañería de una casa circula agua, que se puede considerar un fluido ideal (incompresible y sin "
            "viscosidad) en régimen estacionario. En la planta baja el caño tiene una sección de **30 cm²**, el agua "
            "circula a **2 m/s** y la presión es de **150 kPa**. El caño sube **2 m** hasta el primer piso, donde su "
            "sección se reduce a **10 cm²**. Datos: densidad del agua **1000 kg/m³** y **g = 10 m/s²**."
        ),
        "parts": [
            {
                "prompt": "a) ¿Con qué velocidad circula el agua en el tramo del primer piso? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": "m/s"},
                "answer": "6 m/s",
            },
            {
                "prompt": "b) ¿Cuál es la presión del agua en el tramo del primer piso? Respondé solo con el número en kPa.",
                "check": {"type": "numeric", "value": 114, "tolerance": 0, "unit": "kPa"},
                "answer": "114 kPa",
            },
            {
                "prompt": "c) ¿Cuánto tarda esa cañería en llenar un tanque de 900 L? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 150, "tolerance": 0, "unit": "s"},
                "answer": "150 s",
            },
        ],
        "hints": [
            "Continuidad: el caudal `Q = A · v` es el mismo en los dos tramos. Como aparece el cociente de áreas, podés dejarlas en cm².",
            "Bernoulli entre planta baja (1) y primer piso (2): `P₁ + ½ · ρ · v₁² + ρ · g · h₁ = P₂ + ½ · ρ · v₂² + ρ · g · h₂`. Trabajá en pascales y pasá a kPa al final.",
            "Para el caudal sí hace falta el área en m² (`1 cm² = 10⁻⁴ m²`); después `1 m³ = 1000 L`.",
        ],
        "solution": [
            "a) Continuidad: `A₁ · v₁ = A₂ · v₂`, entonces `v₂ = v₁ · A₁ / A₂ = 2 × 30 ÷ 10 = 6 m/s`.",
            "b) Bernoulli, tomando `h₁ = 0` y `h₂ = 2 m`: `P₂ = P₁ + ½ · ρ · (v₁² − v₂²) − ρ · g · h₂`.",
            "Término de velocidad: `½ × 1000 × (2² − 6²) = 500 × (4 − 36) = −16 000 Pa`. Término de altura: `1000 × 10 × 2 = 20 000 Pa`.",
            "`P₂ = 150 000 − 16 000 − 20 000 = 114 000 Pa = 114 kPa`. La presión baja por dos motivos: el agua va más rápido y está más alta.",
            "c) Caudal: `Q = A₁ · v₁ = 30 × 10⁻⁴ m² × 2 m/s = 6 × 10⁻³ m³/s = 6 L/s`.",
            "Tiempo de llenado: `t = V / Q = 900 L ÷ 6 L/s = 150 s` (2 minutos y medio).",
            "Respuestas: 6 m/s, 114 kPa y 150 s. Verificación del caudal en el tramo angosto: `10 × 10⁻⁴ × 6 = 6 × 10⁻³ m³/s`, el mismo. Error típico en b): olvidar el término `ρ · g · h` (daría 134 kPa) o sumar en lugar de restar el cambio de energía cinética.",
        ],
    },
]
