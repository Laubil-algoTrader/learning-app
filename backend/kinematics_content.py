"""Cinemática para el ingreso a ingeniería (5 temas que desarrollan `f-cinematica`).

  - Operar con vectores: componentes, suma, resta y resultante
  - MRU: ecuación horaria y problemas de encuentro
  - MRUV: ecuaciones horarias y gráficas x-t, v-t y a-t
  - Caída libre y tiro vertical
  - Tiro oblicuo: alcance, altura máxima y tiempo de vuelo

Convenciones: en los problemas con gravedad se usa g = 10 m/s² y se desprecia el
rozamiento del aire (dicho en cada consigna). Los senos y cosenos que no son exactos
se dan como dato (sen 37° = 0.6, cos 37° = 0.8, etc.).
"""

from __future__ import annotations

_SECTION = "Cinemática y base"
_LAB = "physics:kinematics"

KINEMATICS_NODES: list[dict] = [
    # ==================== VECTORES ====================
    {
        "slug": "f-vectores-operaciones",
        "title": "Operar con vectores: componentes, suma y resultante",
        "summary": "Descomponer un vector con seno y coseno, recuperar módulo y dirección, y sumar o restar vectores componente a componente.",
        "prerequisites": ["f-magnitudes-vectores"],
        "insert_after": "f-magnitudes-vectores",
        "metadata": {"section": _SECTION, "lab_tab": "kinematics", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Velocidad de ascenso de un avión con sen 37°",
                "prompt": "Un avión despega de Aeroparque a 80 m/s con la trayectoria inclinada 37° respecto de la pista (sen 37° = 0.6 y cos 37° = 0.8). ¿Cuánto vale la componente vertical de su velocidad? Respondé solo con el número en m/s.",
                "answer": "48 m/s: la componente vertical es el cateto opuesto al ángulo, así que vy = v · sen 37° = 80 · 0.6 = 48 m/s. (La horizontal sería vx = 80 · 0.8 = 64 m/s.)",
                "hints": [
                    "La componente vertical es el cateto opuesto al ángulo medido desde la horizontal.",
                    "Cateto opuesto → seno: vy = v · sen θ.",
                ],
                "payload": {"check": {"type": "numeric", "value": 48, "tolerance": 0, "unit": "m/s"}},
            },
            {
                "item_type": "worked_example",
                "title": "Módulo de un vector con una componente negativa",
                "prompt": "La velocidad de una lancha en el Delta tiene componentes vx = −8 m/s y vy = 15 m/s. ¿Cuánto vale el módulo de la velocidad? Respondé solo con el número en m/s.",
                "answer": "17 m/s: |v| = √(vx² + vy²) = √((−8)² + 15²) = √(64 + 225) = √289 = 17 m/s. El signo de una componente indica el sentido; al elevarla al cuadrado siempre suma.",
                "hints": [
                    "El módulo sale por Pitágoras con las dos componentes.",
                    "Cuidado con el signo: (−8)² es positivo.",
                ],
                "payload": {"check": {"type": "numeric", "value": 17, "tolerance": 0, "unit": "m/s"}},
            },
            {
                "item_type": "worked_example",
                "title": "Dirección de un vector con la arcotangente",
                "prompt": "Un desplazamiento tiene componentes Δx = 3 km (hacia el este) y Δy = 4 km (hacia el norte). ¿Qué ángulo forma con la dirección este? Datos: tg 37° = 0.75 y tg 53° = 1.33. Respondé solo con el número en grados.",
                "answer": "53°: tg θ = Δy / Δx = 4 / 3 ≈ 1.33, así que θ ≈ 53° medido desde el este hacia el norte. Si invertís el cociente (3 / 4 = 0.75) obtenés 37°, que es el ángulo respecto del norte.",
                "hints": [
                    "La tangente del ángulo con el eje x es la componente y dividida por la componente x.",
                    "Calculá 4 / 3 y buscá a qué dato de tangente corresponde.",
                ],
                "payload": {"check": {"type": "numeric", "value": 53, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Módulo de la suma de dos fuerzas por componentes",
                "prompt": "Dos fuerzas actúan sobre una caja: F₁ = (2; 7) N y F₂ = (4; 1) N. ¿Cuánto vale el módulo de la fuerza resultante? Respondé solo con el número en N.",
                "answer": "10 N: se suma componente a componente, R = (2 + 4; 7 + 1) = (6; 8) N, y después |R| = √(6² + 8²) = √100 = 10 N. Sumar los módulos por separado (√53 + √17 ≈ 11.4 N) da de más porque las fuerzas no son paralelas.",
                "hints": [
                    "Primero sumá las x entre sí y las y entre sí.",
                    "Recién con las componentes de la resultante aplicá Pitágoras.",
                ],
                "payload": {"check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "N"}},
            },
            {
                "item_type": "worked_example",
                "title": "Cambio de velocidad en un rebote (resta de vectores)",
                "prompt": "Una bola de pool llega a la banda con velocidad v₁ = (3; 4) m/s y rebota con v₂ = (3; −4) m/s. ¿Cuánto vale el módulo del cambio de velocidad Δv = v₂ − v₁? Respondé solo con el número en m/s.",
                "answer": "8 m/s: Δv = (3 − 3; −4 − 4) = (0; −8) m/s, de módulo 8 m/s. Aunque la rapidez es 5 m/s antes y después, la velocidad cambió porque cambió su dirección: restar los módulos (5 − 5 = 0) es incorrecto.",
                "hints": [
                    "Restá componente a componente: las x entre sí y las y entre sí.",
                    "Ojo con los signos en y: −4 − 4.",
                ],
                "payload": {"check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": "m/s"}},
            },
            {
                "item_type": "recall",
                "title": "Rango posible de la resultante de dos fuerzas",
                "prompt": "Dos fuerzas de 30 N y 40 N actúan sobre el mismo cuerpo, pero no sabés qué ángulo forman entre sí. ¿Qué podés afirmar sobre el módulo de la resultante?",
                "answer": "Está entre 10 N y 70 N. Si apuntan en la misma dirección y sentido se suman (70 N); si son colineales de sentido contrario se restan (10 N); si son perpendiculares da √(30² + 40²) = 50 N. Cualquier otro ángulo da un valor intermedio, y nunca puede dar 0 porque los módulos son distintos.",
                "hints": [
                    "Pensá los dos casos extremos: las dos fuerzas apuntando igual y apuntando en sentidos opuestos.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Vale siempre 70 N",
                            "Vale siempre 50 N",
                            "Está entre 10 N y 70 N, según el ángulo",
                            "Está entre 0 N y 70 N, según el ángulo",
                        ],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Cuadrante correcto al usar la arcotangente",
                "prompt": "Un vector tiene componentes Ax = −5 y Ay = 5. La calculadora da arctg(5 / (−5)) = −45°. ¿Qué ángulo forma el vector con el eje x positivo, medido en sentido antihorario?",
                "answer": "135°. Con Ax negativa y Ay positiva el vector está en el segundo cuadrante. La arcotangente no distingue un vector de su opuesto: −45° corresponde a (5; −5), en el cuarto cuadrante, así que hay que sumarle 180°: −45° + 180° = 135°.",
                "hints": [
                    "Dibujá el vector: ¿en qué cuadrante cae con x negativa e y positiva?",
                    "Cuando Ax es negativa, al resultado de la calculadora hay que sumarle 180°.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["−45°", "45°", "135°", "225°"],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Vector opuesto: componentes y módulo",
                "prompt": "Si A = (6; −2), ¿cuáles son las componentes del vector opuesto −A y cómo es su módulo comparado con el de A?",
                "answer": "−A = (−6; 2), con el mismo módulo que A. El opuesto cambia el signo de TODAS las componentes: misma dirección, sentido contrario. El módulo no cambia (√40 en los dos casos) y nunca es negativo.",
                "hints": ["El opuesto es el vector que sumado a A da (0; 0)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "(−6; 2), con el mismo módulo que A",
                            "(−6; −2), con el mismo módulo que A",
                            "(−6; 2), con módulo negativo",
                            "(6; 2), con el mismo módulo que A",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== MRU ====================
    {
        "slug": "f-mru-encuentro",
        "title": "MRU: ecuación horaria y problemas de encuentro",
        "summary": "Escribir x(t) = x₀ + v·t con un sistema de referencia y sus signos, leer la gráfica x-t y resolver encuentros y persecuciones.",
        "prerequisites": ["f-cinematica"],
        "insert_after": "f-cinematica",
        "metadata": {"section": _SECTION, "lab_tab": "kinematics", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "MRU con velocidad negativa: posición en la ruta",
                "prompt": "Un micro viaja de Mar del Plata a Buenos Aires por la Ruta 2 a 90 km/h constantes, en el sentido en que los mojones kilométricos disminuyen. Si pasa por el km 300, ¿por qué kilómetro pasa 2 h después? Respondé solo con el número en km.",
                "answer": "120 km: como avanza hacia kilómetros decrecientes, en ese sistema de referencia su velocidad es negativa: x = x₀ + v · t = 300 + (−90) · 2 = 300 − 180 = 120 km.",
                "hints": [
                    "Usá x = x₀ + v · t con x₀ = 300 km.",
                    "Si la posición disminuye con el tiempo, la velocidad lleva signo negativo.",
                ],
                "payload": {"check": {"type": "numeric", "value": 120, "tolerance": 0, "unit": "km"}},
            },
            {
                "item_type": "worked_example",
                "title": "Velocidad media cuando hay un tramo de vuelta",
                "prompt": "Trotás por la costanera 300 m hacia el norte en 60 s y enseguida volvés 100 m hacia el sur en 40 s. ¿Cuánto vale el módulo de tu velocidad media en todo el trayecto? Respondé solo con el número en m/s.",
                "answer": "2 m/s: la velocidad media usa el desplazamiento, no la distancia recorrida. Δx = 300 − 100 = 200 m hacia el norte en Δt = 60 + 40 = 100 s, así que v_media = 200 / 100 = 2 m/s. La rapidez media, en cambio, usa la distancia: 400 / 100 = 4 m/s.",
                "hints": [
                    "La velocidad media es desplazamiento (posición final menos inicial) dividido por el tiempo total.",
                    "¿A cuántos metros del punto de partida terminaste?",
                ],
                "payload": {"check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "m/s"}},
            },
            {
                "item_type": "worked_example",
                "title": "Velocidad como pendiente de una gráfica x-t",
                "prompt": "En una gráfica posición-tiempo, la recta de un ciclista pasa por los puntos (t = 2 s; x = 30 m) y (t = 6 s; x = 10 m). ¿Cuál es su velocidad? Respondé solo con el número en m/s, con su signo.",
                "answer": "−5 m/s: la velocidad es la pendiente de la recta, v = Δx / Δt = (10 − 30) / (6 − 2) = −20 / 4 = −5 m/s. El signo negativo indica que se mueve en el sentido negativo del eje.",
                "hints": [
                    "Pendiente = (x final − x inicial) / (t final − t inicial).",
                    "La posición disminuye: el resultado tiene que ser negativo.",
                ],
                "payload": {"check": {"type": "numeric", "value": -5, "tolerance": 0, "unit": "m/s"}},
            },
            {
                "item_type": "worked_example",
                "title": "Tiempo de encuentro de dos trenes en sentidos opuestos",
                "prompt": "Dos trenes salen al mismo tiempo de dos estaciones separadas 360 km y viajan uno hacia el otro por vías paralelas, a 70 km/h y 50 km/h constantes. ¿Cuánto tardan en cruzarse? Respondé solo con el número en h.",
                "answer": "3 h: con origen en la primera estación, x₁ = 70 · t y x₂ = 360 − 50 · t. Se cruzan cuando x₁ = x₂: 70 · t = 360 − 50 · t → 120 · t = 360 → t = 3 h. (Al ir en sentidos opuestos, la separación se achica a razón de 70 + 50 = 120 km/h.)",
                "hints": [
                    "Poné el origen en una estación: un tren tiene x₀ = 0 y velocidad positiva; el otro, x₀ = 360 km y velocidad negativa.",
                    "Igualá las dos posiciones y despejá t.",
                ],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": "h"}},
            },
            {
                "item_type": "worked_example",
                "title": "Persecución con velocidades en km/h",
                "prompt": "Un patrullero va a 108 km/h por la autopista y persigue a una moto que va a 90 km/h y le lleva 200 m de ventaja. Si ambos mantienen su velocidad, ¿cuánto tarda el patrullero en alcanzarla? Respondé solo con el número en s.",
                "answer": "40 s: primero pasá a m/s: 108 ÷ 3.6 = 30 m/s y 90 ÷ 3.6 = 25 m/s. Con origen en el patrullero: x_P = 30 · t y x_M = 200 + 25 · t. Igualando: 30 · t = 200 + 25 · t → 5 · t = 200 → t = 40 s.",
                "hints": [
                    "La ventaja está en metros: pasá las dos velocidades a m/s dividiendo por 3.6.",
                    "Los dos van en el mismo sentido: la moto arranca con x₀ = 200 m. Igualá las posiciones.",
                ],
                "payload": {"check": {"type": "numeric", "value": 40, "tolerance": 0, "unit": "s"}},
            },
            {
                "item_type": "recall",
                "title": "Ecuación horaria del móvil que viene de frente",
                "prompt": "El auto A sale de x = 0 hacia la derecha a 15 m/s. En el mismo instante, el auto B sale de x = 400 m y viaja hacia A a 25 m/s. Tomando el eje x positivo hacia la derecha, ¿cuál es la ecuación horaria de B (x en m, t en s)?",
                "answer": "x = 400 − 25·t. B arranca en x₀ = 400 m y se mueve hacia la izquierda, en contra del sentido positivo, así que su velocidad es −25 m/s. Los dos autos se describen con el mismo origen y el mismo eje.",
                "hints": [
                    "¿Dónde está B en t = 0? Ese es su x₀.",
                    "B se mueve en contra del sentido positivo del eje.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["x = 400 + 25·t", "x = 400 − 25·t", "x = −25·t", "x = 25·t − 400"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Cruce de dos rectas en una gráfica x-t",
                "prompt": "En una misma gráfica posición-tiempo, las rectas de dos autos se cortan en el punto (t = 10 s; x = 150 m). ¿Qué podés asegurar sobre ese instante?",
                "answer": "Que los dos autos están en la misma posición (x = 150 m) en el mismo instante: se encuentran. No tienen la misma velocidad (rectas que se cortan tienen pendientes distintas), y solo habrían recorrido la misma distancia si hubieran salido del mismo lugar.",
                "hints": ["Cada punto de la gráfica x-t dice dónde está el móvil en cada instante."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Los dos autos tienen la misma velocidad",
                            "Los dos autos están en la misma posición: se encuentran",
                            "Los dos autos recorrieron la misma distancia desde t = 0",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Recta horizontal en una gráfica x-t",
                "prompt": "En una gráfica posición-tiempo, un tramo es una recta horizontal a la altura x = 40 m. ¿Qué hace el móvil en ese tramo?",
                "answer": "Está detenido en x = 40 m: la posición no cambia con el tiempo, así que la pendiente (la velocidad) es cero. Una recta horizontal significa velocidad constante distinta de cero recién en una gráfica v-t.",
                "hints": ["La pendiente de la gráfica x-t es la velocidad: ¿cuánto vale la pendiente de una recta horizontal?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Se mueve a 40 m/s constantes",
                            "Está detenido en x = 40 m",
                            "Avanza con aceleración constante",
                        ],
                        "correct": 1,
                    },
                },
            },
        ],
    },
    # ==================== MRUV ====================
    {
        "slug": "f-mruv-graficas",
        "title": "MRUV: ecuaciones horarias y gráficas x-t, v-t y a-t",
        "summary": "Las tres ecuaciones del movimiento con aceleración constante, el signo de la aceleración al frenar y la lectura de pendiente y área en la gráfica v-t.",
        "prerequisites": ["f-mru-encuentro"],
        "insert_after": "f-mru-encuentro",
        "metadata": {"section": _SECTION, "lab_tab": "kinematics", "est_minutes": 25},
        "items": [
            {
                "item_type": "worked_example",
                "title": "MRUV: distancia recorrida con velocidad inicial",
                "prompt": "Un auto va a 10 m/s por una avenida y acelera a 2 m/s² constantes durante 5 s. ¿Qué distancia recorre en esos 5 s? Respondé solo con el número en m.",
                "answer": "75 m: Δx = v₀ · t + ½ · a · t² = 10 · 5 + ½ · 2 · 5² = 50 + 25 = 75 m.",
                "hints": [
                    "Usá Δx = v₀ · t + ½ · a · t².",
                    "Son dos términos: lo que recorrería sin acelerar más el extra por la aceleración (no te olvides del ½).",
                ],
                "payload": {"check": {"type": "numeric", "value": 75, "tolerance": 0, "unit": "m"}},
            },
            {
                "item_type": "worked_example",
                "title": "Distancia de frenado con la ecuación sin tiempo",
                "prompt": "Un auto va a 30 m/s (108 km/h) por la ruta y frena con aceleración constante de −5 m/s² hasta detenerse. ¿Qué distancia recorre durante la frenada? Respondé solo con el número en m.",
                "answer": "90 m: con v² = v₀² + 2 · a · Δx y v = 0 queda 0 = 30² + 2 · (−5) · Δx → Δx = 900 / 10 = 90 m.",
                "hints": [
                    "No te dan el tiempo: usá v² = v₀² + 2 · a · Δx.",
                    "Al detenerse, v = 0. Despejá Δx.",
                ],
                "payload": {"check": {"type": "numeric", "value": 90, "tolerance": 0, "unit": "m"}},
            },
            {
                "item_type": "worked_example",
                "title": "Velocidad al final de la pista sin conocer el tiempo",
                "prompt": "Un avión parte del reposo en la cabecera de la pista y acelera a 4 m/s² constantes a lo largo de 800 m. ¿Qué velocidad tiene al final de ese tramo? Respondé solo con el número en m/s.",
                "answer": "80 m/s: v² = v₀² + 2 · a · Δx = 0 + 2 · 4 · 800 = 6400 → v = √6400 = 80 m/s (288 km/h).",
                "hints": [
                    "Con v₀ = 0 queda v² = 2 · a · Δx.",
                    "No te olvides de sacar la raíz cuadrada al final.",
                ],
                "payload": {"check": {"type": "numeric", "value": 80, "tolerance": 0, "unit": "m/s"}},
            },
            {
                "item_type": "worked_example",
                "title": "Desplazamiento como área de un trapecio en la gráfica v-t",
                "prompt": "En una gráfica velocidad-tiempo, la recta de una moto sube de 4 m/s en t = 0 a 16 m/s en t = 5 s. ¿Cuánto se desplazó en esos 5 s? Respondé solo con el número en m.",
                "answer": "50 m: el desplazamiento es el área bajo la recta, un trapecio: (4 + 16) / 2 · 5 = 50 m. También sale como rectángulo (4 · 5 = 20 m) más triángulo (½ · 5 · 12 = 30 m).",
                "hints": [
                    "El desplazamiento es el área entre la recta y el eje del tiempo.",
                    "No arranca de cero: la figura es un trapecio (o un rectángulo más un triángulo).",
                ],
                "payload": {"check": {"type": "numeric", "value": 50, "tolerance": 0, "unit": "m"}},
            },
            {
                "item_type": "worked_example",
                "title": "Aceleración como pendiente de la gráfica v-t",
                "prompt": "En una gráfica velocidad-tiempo, la recta de un colectivo pasa por los puntos (t = 2 s; v = 18 m/s) y (t = 6 s; v = 8 m/s). ¿Cuál es su aceleración? Respondé solo con el número en m/s², con su signo.",
                "answer": "−2.5 m/s²: la aceleración es la pendiente de la recta, a = Δv / Δt = (8 − 18) / (6 − 2) = −10 / 4 = −2.5 m/s². Es negativa porque la velocidad (positiva) está disminuyendo: el colectivo frena.",
                "hints": [
                    "Pendiente = (v final − v inicial) / (t final − t inicial).",
                    "La velocidad baja: el resultado tiene que ser negativo.",
                ],
                "payload": {"check": {"type": "numeric", "value": -2.5, "tolerance": 0, "unit": "m/s²"}},
            },
            {
                "item_type": "recall",
                "title": "Signos de v y a al frenar moviéndose en sentido negativo",
                "prompt": "Un auto se mueve en el sentido negativo del eje x y está frenando. ¿Qué signos tienen su velocidad y su aceleración?",
                "answer": "v < 0 y a > 0. Frenar significa que la aceleración tiene sentido opuesto a la velocidad, no que sea negativa. Como la velocidad es negativa, la aceleración es positiva. Con v < 0 y a < 0 el auto iría cada vez más rápido hacia el lado negativo.",
                "hints": ["Al frenar, la aceleración apunta en contra de la velocidad."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["v < 0 y a < 0", "v < 0 y a > 0", "v > 0 y a < 0"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Forma de las gráficas x-t, v-t y a-t en un MRUV",
                "prompt": "¿Qué forma tienen las gráficas x-t, v-t y a-t de un movimiento rectilíneo con aceleración constante distinta de cero (MRUV)?",
                "answer": "x-t es una parábola (por el término ½ · a · t²), v-t es una recta inclinada (v = v₀ + a · t, de pendiente a) y a-t es una recta horizontal (a constante). Recta inclinada en x-t y recta horizontal en v-t corresponden a un MRU.",
                "hints": ["Mirá las ecuaciones: ¿cuál tiene t², cuál tiene t y cuál no depende de t?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "x-t: recta inclinada · v-t: recta horizontal · a-t: nula",
                            "x-t: parábola · v-t: recta inclinada · a-t: recta horizontal",
                            "x-t: parábola · v-t: parábola · a-t: recta inclinada",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Distancia de frenado al duplicar la velocidad",
                "prompt": "Con los mismos frenos (la misma desaceleración constante), un auto pasa de circular a 60 km/h a circular a 120 km/h. ¿Cómo cambia su distancia de frenado?",
                "answer": "Se cuadruplica. De v² = v₀² + 2 · a · Δx con v = 0 sale d = v₀² / (2 · |a|): la distancia depende del CUADRADO de la velocidad inicial, así que el doble de velocidad exige 2² = 4 veces más distancia.",
                "hints": ["Despejá la distancia de v² = v₀² + 2 · a · Δx con v = 0 y fijate cómo aparece v₀."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Se duplica",
                            "Se cuadruplica",
                            "No cambia: depende solo de los frenos",
                        ],
                        "correct": 1,
                    },
                },
            },
        ],
    },
    # ==================== CAÍDA LIBRE Y TIRO VERTICAL ====================
    {
        "slug": "f-caida-libre-tiro-vertical",
        "title": "Caída libre y tiro vertical",
        "summary": "MRUV vertical con aceleración g: caída desde el reposo, tiempo de subida, altura máxima, simetría del tiro vertical y elección del eje.",
        "prerequisites": ["f-mruv-graficas"],
        "insert_after": "f-mruv-graficas",
        "metadata": {"section": _SECTION, "lab_tab": "kinematics", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Velocidad de llegada al suelo en caída libre",
                "prompt": "Una maceta se cae desde un balcón a 45 m de altura (parte del reposo). Despreciá el rozamiento del aire y usá g = 10 m/s². ¿Con qué rapidez llega a la vereda? Respondé solo con el número en m/s.",
                "answer": "30 m/s: sin usar el tiempo, v² = v₀² + 2 · g · h = 0 + 2 · 10 · 45 = 900 → v = √900 = 30 m/s (108 km/h).",
                "hints": [
                    "No te dan el tiempo: usá v² = v₀² + 2 · g · h con v₀ = 0.",
                    "No te olvides de la raíz cuadrada al final.",
                ],
                "payload": {"check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": "m/s"}},
            },
            {
                "item_type": "worked_example",
                "title": "Tiempo de caída desde una altura conocida",
                "prompt": "Un dron que está quieto en el aire a 125 m de altura suelta un paquete. Despreciá el rozamiento del aire y usá g = 10 m/s². ¿Cuánto tarda el paquete en llegar al suelo? Respondé solo con el número en s.",
                "answer": "5 s: como parte del reposo, h = ½ · g · t² → t = √(2 · h / g) = √(2 · 125 / 10) = √25 = 5 s.",
                "hints": [
                    "Parte del reposo: h = ½ · g · t².",
                    "Despejá t²: primero multiplicá la altura por 2, dividí por g y recién después sacá la raíz.",
                ],
                "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "s"}},
            },
            {
                "item_type": "worked_example",
                "title": "Tiempo de subida en un tiro vertical",
                "prompt": "Lanzás una pelota verticalmente hacia arriba a 25 m/s. Despreciá el rozamiento del aire y usá g = 10 m/s². ¿Cuánto tarda en llegar al punto más alto? Respondé solo con el número en s.",
                "answer": "2.5 s: en el punto más alto v = 0, así que 0 = v₀ − g · t → t = v₀ / g = 25 / 10 = 2.5 s. (El vuelo completo hasta volver a la mano dura el doble: 5 s.)",
                "hints": [
                    "¿Cuánto vale la velocidad justo en el punto más alto?",
                    "Usá v = v₀ − g · t con v = 0.",
                ],
                "payload": {
                    "lab_link": _LAB,
                    "check": {"type": "numeric", "value": 2.5, "tolerance": 0, "unit": "s"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Altura máxima de un tiro vertical",
                "prompt": "Una bengala se dispara verticalmente hacia arriba a 40 m/s. Despreciá el rozamiento del aire y usá g = 10 m/s². ¿Qué altura máxima alcanza sobre el punto de disparo? Respondé solo con el número en m.",
                "answer": "80 m: en la cima v = 0, así que 0 = v₀² − 2 · g · h → h = v₀² / (2 · g) = 1600 / 20 = 80 m.",
                "hints": [
                    "En el punto más alto v = 0: usá v² = v₀² − 2 · g · h.",
                    "Cuidado con el 2 del denominador: h = v₀² / (2 · g).",
                ],
                "payload": {
                    "lab_link": _LAB,
                    "check": {"type": "numeric", "value": 80, "tolerance": 0, "unit": "m"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Altura en un instante lanzando desde una terraza",
                "prompt": "Desde una terraza a 25 m del suelo lanzás una pelota verticalmente hacia arriba a 20 m/s. Despreciá el rozamiento del aire y usá g = 10 m/s². ¿A qué altura respecto del suelo está la pelota 3 s después del lanzamiento? Respondé solo con el número en m.",
                "answer": "40 m: con el eje hacia arriba y el origen en el suelo, y = y₀ + v₀ · t − ½ · g · t² = 25 + 20 · 3 − ½ · 10 · 3² = 25 + 60 − 45 = 40 m. (Ya pasó por la cima, a los 2 s y a 45 m del suelo, y está bajando.)",
                "hints": [
                    "Eje positivo hacia arriba con origen en el suelo: y₀ = 25 m y la aceleración es −g.",
                    "y = y₀ + v₀ · t − ½ · g · t².",
                ],
                "payload": {"check": {"type": "numeric", "value": 40, "tolerance": 0, "unit": "m"}},
            },
            {
                "item_type": "recall",
                "title": "Velocidad al volver al punto de lanzamiento",
                "prompt": "Lanzás una pelota verticalmente hacia arriba a 15 m/s y la atajás a la misma altura a la que la soltaste. Despreciando el rozamiento del aire (g = 10 m/s²), ¿con qué velocidad llega a tu mano?",
                "answer": "15 m/s hacia abajo. Sin aire el movimiento es simétrico: la gravedad le quita 10 m/s por segundo al subir y le devuelve lo mismo al bajar, así que vuelve a la altura de partida con la misma rapidez y sentido contrario. Con v² = v₀² − 2 · g · Δy y Δy = 0 queda v² = v₀².",
                "hints": ["Al volver a la misma altura el desplazamiento total es cero: mirá v² = v₀² − 2 · g · Δy."],
                "payload": {
                    "lab_link": _LAB,
                    "check": {
                        "type": "choice",
                        "options": [
                            "0 m/s",
                            "15 m/s hacia abajo",
                            "Más de 15 m/s, porque vino acelerando en toda la bajada",
                            "Menos de 15 m/s, porque perdió velocidad al subir",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Aceleración en la subida, la cima y la bajada",
                "prompt": "Tomás el eje y positivo hacia arriba y lanzás una piedra verticalmente hacia arriba (sin rozamiento del aire, g = 10 m/s²). ¿Cuánto vale su aceleración mientras sube, en el punto más alto y mientras baja?",
                "answer": "−10 m/s² en los tres casos. La gravedad apunta hacia abajo todo el tiempo y, una vez elegido el eje, su signo no cambia. Lo que cambia de signo es la velocidad: positiva al subir, cero en la cima y negativa al bajar.",
                "hints": ["La aceleración mide cómo cambia la velocidad: ¿en algún momento deja de cambiar 10 m/s por segundo hacia abajo?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "−10 m/s² al subir, 0 en el punto más alto y +10 m/s² al bajar",
                            "+10 m/s² al subir y −10 m/s² al bajar",
                            "−10 m/s² en los tres casos",
                        ],
                        "correct": 2,
                    },
                },
            },
        ],
    },
    # ==================== TIRO OBLICUO ====================
    {
        "slug": "f-tiro-oblicuo",
        "title": "Tiro oblicuo: alcance, altura máxima y tiempo de vuelo",
        "summary": "Un MRU horizontal y un tiro vertical simultáneos: componentes de la velocidad inicial, tiempo de vuelo, altura máxima, alcance y tiro horizontal.",
        "prerequisites": ["f-caida-libre-tiro-vertical", "f-vectores-operaciones"],
        "insert_after": "f-caida-libre-tiro-vertical",
        "metadata": {"section": _SECTION, "lab_tab": "kinematics", "est_minutes": 25},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Tiempo de vuelo de un tiro oblicuo",
                "prompt": "Pateás una pelota desde el pasto a 25 m/s con un ángulo de 37° sobre la horizontal (sen 37° = 0.6 y cos 37° = 0.8). Despreciá el rozamiento del aire y usá g = 10 m/s². ¿Cuánto tiempo está en el aire hasta volver al pasto? Respondé solo con el número en s.",
                "answer": "3 s: la componente vertical es v₀y = 25 · 0.6 = 15 m/s. Tarda v₀y / g = 1.5 s en subir y lo mismo en bajar: t_vuelo = 2 · v₀y / g = 2 · 15 / 10 = 3 s.",
                "hints": [
                    "El tiempo en el aire lo decide solo la componente vertical: v₀y = v₀ · sen θ.",
                    "Calculá el tiempo de subida (v₀y / g) y recordá que la bajada dura lo mismo.",
                ],
                "payload": {
                    "lab_link": _LAB,
                    "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": "s"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Altura máxima de un tiro oblicuo",
                "prompt": "Una bengala de señales se dispara desde el suelo a 40 m/s con un ángulo de 30° sobre la horizontal (sen 30° = 0.5). Despreciá el rozamiento del aire y usá g = 10 m/s². ¿Qué altura máxima alcanza? Respondé solo con el número en m.",
                "answer": "20 m: solo la componente vertical decide la altura: v₀y = 40 · 0.5 = 20 m/s, y h_max = v₀y² / (2 · g) = 400 / 20 = 20 m. Usar los 40 m/s completos daría 80 m, que es la altura de un tiro vertical.",
                "hints": [
                    "Primero calculá la componente vertical de la velocidad inicial.",
                    "h_max = v₀y² / (2 · g): va la componente vertical, no la velocidad completa.",
                ],
                "payload": {
                    "lab_link": _LAB,
                    "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "m"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Alcance horizontal de un tiro oblicuo",
                "prompt": "Un golfista le pega a la pelota a 50 m/s con un ángulo de 37° sobre el césped horizontal (sen 37° = 0.6 y cos 37° = 0.8). Despreciá el rozamiento del aire y usá g = 10 m/s². ¿A qué distancia horizontal vuelve a tocar el césped? Respondé solo con el número en m.",
                "answer": "240 m: v₀x = 50 · 0.8 = 40 m/s y v₀y = 50 · 0.6 = 30 m/s. Tiempo de vuelo: 2 · v₀y / g = 2 · 30 / 10 = 6 s. Alcance: x = v₀x · t = 40 · 6 = 240 m.",
                "hints": [
                    "Descomponé la velocidad: la componente vertical da el tiempo de vuelo; la horizontal, el avance.",
                    "Alcance = v₀x · t_vuelo, con t_vuelo = 2 · v₀y / g.",
                ],
                "payload": {
                    "lab_link": _LAB,
                    "check": {"type": "numeric", "value": 240, "tolerance": 0, "unit": "m"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Tiro horizontal desde una terraza: dónde cae",
                "prompt": "Desde el borde de una terraza a 20 m de altura se patea una pelota en dirección horizontal a 15 m/s. Despreciá el rozamiento del aire y usá g = 10 m/s². ¿A qué distancia horizontal de la base del edificio toca el suelo? Respondé solo con el número en m.",
                "answer": "30 m: como sale horizontal, v₀y = 0 y en vertical es una caída libre: t = √(2 · h / g) = √(2 · 20 / 10) = 2 s. En ese tiempo avanza x = v₀ · t = 15 · 2 = 30 m.",
                "hints": [
                    "La velocidad inicial no tiene componente vertical: el tiempo de caída sale de h = ½ · g · t².",
                    "Con ese tiempo, el avance horizontal es un MRU: x = v₀ · t.",
                ],
                "payload": {"check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": "m"}},
            },
            {
                "item_type": "worked_example",
                "title": "Rapidez en el punto más alto de un tiro oblicuo",
                "prompt": "Lanzás una pelota a 20 m/s con un ángulo de 60° sobre la horizontal (cos 60° = 0.5). Despreciá el rozamiento del aire y usá g = 10 m/s². ¿Cuál es su rapidez en el punto más alto de la trayectoria? Respondé solo con el número en m/s.",
                "answer": "10 m/s: en el punto más alto solo se anula la componente vertical; la horizontal no cambia en todo el vuelo: v = v₀x = 20 · cos 60° = 20 · 0.5 = 10 m/s.",
                "hints": [
                    "En la cima se anula la componente vertical, pero la pelota sigue avanzando.",
                    "La componente horizontal v₀x = v₀ · cos θ se mantiene durante todo el vuelo.",
                ],
                "payload": {
                    "lab_link": _LAB,
                    "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "m/s"},
                },
            },
            {
                "item_type": "recall",
                "title": "Qué componente de la velocidad cambia durante el vuelo",
                "prompt": "Durante el vuelo de un tiro oblicuo sin rozamiento del aire (g = 10 m/s²), ¿qué pasa con las componentes de la velocidad?",
                "answer": "vx se mantiene constante y vy cambia 10 m/s en cada segundo. La única aceleración es la de la gravedad, que es vertical: en horizontal el movimiento es un MRU y en vertical es un MRUV (vy disminuye al subir, se anula en la cima y crece hacia abajo al bajar).",
                "hints": ["¿En qué dirección apunta la única aceleración que hay durante el vuelo?"],
                "payload": {
                    "lab_link": _LAB,
                    "check": {
                        "type": "choice",
                        "options": [
                            "vx se mantiene constante y vy cambia 10 m/s en cada segundo",
                            "vx y vy disminuyen al subir y aumentan al bajar",
                            "vx disminuye por la gravedad y vy se mantiene constante",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Tiros a 37° y 53° con la misma rapidez",
                "prompt": "Dos pelotas se lanzan desde el suelo con la misma rapidez, una a 37° y otra a 53° sobre la horizontal (terreno horizontal, sin rozamiento del aire, g = 10 m/s²). ¿Qué ocurre?",
                "answer": "Tienen el mismo alcance, pero la de 53° sube más alto y está más tiempo en el aire. 37° y 53° son complementarios (suman 90°): la de 53° tiene más velocidad vertical (más tiempo de vuelo y más altura) y menos horizontal, y el producto v₀x · t_vuelo termina siendo el mismo.",
                "hints": [
                    "37° + 53° = 90°: son ángulos complementarios.",
                    "La altura y el tiempo de vuelo dependen de la componente vertical, v₀ · sen θ.",
                ],
                "payload": {
                    "lab_link": _LAB,
                    "check": {
                        "type": "choice",
                        "options": [
                            "La de 53° llega más lejos, porque sale más empinada",
                            "Tienen el mismo alcance, la misma altura máxima y el mismo tiempo de vuelo",
                            "La de 37° llega más lejos, porque tiene más velocidad horizontal",
                            "Tienen el mismo alcance, pero la de 53° sube más alto y está más tiempo en el aire",
                        ],
                        "correct": 3,
                    },
                },
            },
        ],
    },
]


KINEMATICS_LESSONS: dict[str, dict] = {
    "f-vectores-operaciones": {
        "hook": {
            "question": "Dos personas empujan un auto que se quedó: una hace 300 N y la otra 400 N. ¿La fuerza total sobre el auto es de 700 N?",
            "intuition": "Solo si empujan en la misma dirección y sentido. Si empujan en direcciones perpendiculares, la resultante es de `500 N`; si empujan una contra la otra, apenas `100 N`. Los vectores no se suman como números comunes: se suman **componente a componente**.",
        },
        "concept": {
            "points": [
                "**Descomponer**: un vector de módulo `A` que forma un ángulo `θ` con el eje x positivo tiene componentes `Ax = A · cos θ` y `Ay = A · sen θ`. El signo de cada componente indica su sentido (negativa = hacia la izquierda o hacia abajo).",
                "**Recomponer**: desde las componentes, el módulo sale por Pitágoras, `A = √(Ax² + Ay²)`, y la dirección con `tg θ = Ay / Ax`. La arcotangente no distingue un vector de su opuesto: mirá los signos de las componentes para ubicar el cuadrante.",
                "**Sumar y restar**: se opera eje por eje. `R = A + B` significa `Rx = Ax + Bx` y `Ry = Ay + By`. Restar es sumar el **opuesto**: `−A` tiene todas las componentes cambiadas de signo, el mismo módulo y sentido contrario.",
                "**Casos rápidos**: colineales del mismo sentido → se suman los módulos; colineales de sentido contrario → se restan; perpendiculares → Pitágoras. En cualquier otro caso, componentes.",
                "**Por qué no se suman los módulos**: el módulo de la resultante de dos vectores de módulos `A` y `B` siempre queda entre `|A − B|` y `A + B`; solo llega a `A + B` cuando los dos apuntan en la misma dirección y sentido.",
            ],
            "real_world": [
                {
                    "title": "Cruzar el río en lancha",
                    "detail": "Apuntás la proa derecho a la otra orilla a `4 m/s` y la corriente te arrastra de costado a `3 m/s`: avanzás en diagonal a `5 m/s`, no a 7.",
                },
                {
                    "title": "Una cinchada",
                    "detail": "Un equipo tira con `900 N` y el otro con `850 N` en sentido contrario: la resultante sobre la soga es de solo `50 N` hacia el equipo que tira más.",
                },
                {
                    "title": "Un avión con viento",
                    "detail": "Los pilotos suman el vector velocidad del avión respecto del aire con el vector viento para conocer su velocidad real respecto del suelo y corregir el rumbo.",
                },
            ],
            "key_rule": "`Ax = A·cos θ`, `Ay = A·sen θ` · `A = √(Ax² + Ay²)`, `tg θ = Ay/Ax` · Suma y resta: componente a componente.",
            "pitfall": "Sumar o restar los módulos de vectores que no son paralelos (`10 + 9 = 19` para dos tramos en distinta dirección, `5 − 5 = 0` para un rebote). Los módulos solo se suman directamente cuando los vectores tienen la misma dirección y sentido.",
        },
        "example": {
            "title": "Sumá dos tramos de una travesía en kayak",
            "steps": [
                "Remás `10 km` en una dirección a `37°` al norte del este (`sen 37° = 0.6`, `cos 37° = 0.8`) y después `9 km` derecho al norte. ¿A qué distancia quedaste del punto de partida?",
                "Descomponé el primer tramo: `Ax = 10 · 0.8 = 8 km` (este) y `Ay = 10 · 0.6 = 6 km` (norte). El segundo ya está sobre un eje: `B = (0; 9) km`.",
                "Sumá eje por eje: `R = (8 + 0; 6 + 9) = (8; 15) km`.",
                "Módulo: `R = √(8² + 15²) = √289 = 17 km`, menos que los `19 km` que remaste, porque los tramos no eran paralelos.",
                "Dirección: `tg θ = 15 / 8 ≈ 1.88` → `θ ≈ 62°` al norte del este (las dos componentes son positivas: primer cuadrante).",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Un vector tiene componentes `Ax = −3` y `Ay = −3`. La calculadora da `arctg((−3) / (−3)) = 45°`. ¿Qué ángulo forma con el eje x positivo, medido en sentido antihorario?",
            "options": [
                {"text": "45°", "ok": False, "feedback": "Ese es el ángulo del vector opuesto, `(3; 3)`. La arcotangente solo ve el cociente `Ay / Ax = 1` y no distingue entre los dos: con ambas componentes negativas hay que sumar 180°."},
                {"text": "225°", "ok": True, "feedback": "Exacto: las dos componentes son negativas, así que el vector está en el tercer cuadrante: `45° + 180° = 225°`."},
                {"text": "135°", "ok": False, "feedback": "135° está en el segundo cuadrante, donde `Ax` es negativa pero `Ay` es positiva. Acá las dos son negativas: tercer cuadrante."},
            ],
        },
        "checks": [
            {
                "question": "Dos fuerzas de 50 N y 120 N actúan sobre el mismo cuerpo. ¿Cuál de estos valores NO puede ser el módulo de la resultante?",
                "options": [
                    {"text": "130 N", "ok": False, "feedback": "Sí puede: es la resultante cuando son perpendiculares, `√(50² + 120²) = 130 N`."},
                    {"text": "70 N", "ok": False, "feedback": "Sí puede: es el mínimo, cuando son colineales de sentido contrario, `120 − 50 = 70 N`."},
                    {"text": "180 N", "ok": True, "feedback": "Exacto: el máximo posible es `50 + 120 = 170 N`, cuando apuntan en la misma dirección y sentido. Ningún ángulo da más que eso."},
                ],
            },
            {
                "question": "Si `A = (5; −3)` y `B = (2; 4)`, ¿cuáles son las componentes de `A − B`?",
                "options": [
                    {"text": "(3; −7)", "ok": True, "feedback": "Exacto: `(5 − 2; −3 − 4) = (3; −7)`."},
                    {"text": "(3; 1)", "ok": False, "feedback": "Restaste bien en x, pero en y sumaste: `−3 + 4 = 1`. Hay que restar también ahí: `−3 − 4 = −7`."},
                    {"text": "(7; 1)", "ok": False, "feedback": "Eso es `A + B = (5 + 2; −3 + 4)`. Para restar, a cada componente de A se le resta la de B."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué dos fuerzas de 30 N y 40 N pueden dar una resultante de 70 N, de 50 N o de 10 N, y cómo sumarías dos vectores que no son ni paralelos ni perpendiculares.",
    },
    "f-mru-encuentro": {
        "hook": {
            "question": "Un auto sale de Buenos Aires hacia Rosario a 110 km/h y, en el mismo instante, otro sale de Rosario hacia Buenos Aires a 90 km/h. Las ciudades están a 300 km. ¿Se cruzan en la mitad del camino?",
            "intuition": "No: se cruzan a `165 km` de Buenos Aires, después de `1.5 h`. Los dos viajan el mismo tiempo, así que el más rápido recorre más. Encontrarse significa estar en la **misma posición en el mismo instante**, y eso se resuelve escribiendo la ecuación horaria de cada uno.",
        },
        "concept": {
            "points": [
                "**Sistema de referencia**: antes de escribir nada, elegí un origen (`x = 0`) y un sentido positivo. La ecuación horaria del MRU es `x(t) = x₀ + v · t`, con `v > 0` si el móvil avanza en el sentido positivo y `v < 0` si va en contra.",
                "**Velocidad media vs. rapidez media**: la velocidad media usa el desplazamiento, `v_m = Δx / Δt`; la rapidez media usa la distancia recorrida. Sus valores coinciden solo si el móvil no cambia de sentido.",
                "**Gráfica x-t**: en un MRU es una recta y su **pendiente es la velocidad**. Recta horizontal = detenido; pendiente negativa = se mueve en sentido negativo; más empinada = más rápido.",
                "**Encuentro**: usá un único origen y un único reloj para los dos móviles, escribí `x_A(t)` y `x_B(t)`, igualalas (`x_A = x_B`), despejá `t` y reemplazá para hallar la posición.",
                "**Unidades coherentes**: no mezcles `km/h` con metros y segundos. `km/h ÷ 3.6 = m/s` y `m/s × 3.6 = km/h`.",
            ],
            "real_world": [
                {
                    "title": "\"Llega en 6 minutos\"",
                    "detail": "Las apps de colectivos y el GPS estiman la llegada con una ecuación horaria: la distancia que falta dividida por la velocidad media del tramo.",
                },
                {
                    "title": "Trenes en vía única",
                    "detail": "En los ramales de una sola vía, el cruce de dos trenes que vienen de frente se programa en una estación con desvío: hay que saber dónde y cuándo se encontrarían.",
                },
                {
                    "title": "Radares de tramo",
                    "detail": "Registran la hora a la que pasás por dos pórticos y calculan tu velocidad media `Δx / Δt`: de nada sirve frenar justo delante de la cámara.",
                },
            ],
            "key_rule": "`x(t) = x₀ + v · t` (con signos según el eje elegido) · Pendiente de `x-t` = velocidad · Encuentro: `x_A(t) = x_B(t)`.",
            "pitfall": "Usar un origen distinto para cada móvil o ponerle velocidad positiva al que viene de frente. Con un solo eje, el que se mueve en sentido negativo lleva `v < 0` y el que sale adelantado lleva su propio `x₀`.",
        },
        "example": {
            "title": "Una moto alcanza a un colectivo",
            "steps": [
                "Un colectivo va a `36 km/h` y una moto que va a `54 km/h` está `60 m` detrás. ¿Cuándo y dónde lo alcanza? Primero las unidades: `36 ÷ 3.6 = 10 m/s` y `54 ÷ 3.6 = 15 m/s`.",
                "Sistema de referencia: origen donde está la moto en `t = 0`, positivo hacia adelante. Entonces `x_moto = 15 · t` y `x_cole = 60 + 10 · t`.",
                "Encuentro: `15 · t = 60 + 10 · t` → `5 · t = 60` → `t = 12 s`.",
                "Posición: `x_moto = 15 · 12 = 180 m`. Verificación con el otro móvil: `x_cole = 60 + 10 · 12 = 180 m`. Coinciden: ese es el punto de encuentro.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "La ecuación horaria de un auto es `x(t) = 200 − 25 · t` (x en m, t en s). ¿Qué describe?",
            "options": [
                {"text": "En t = 0 está en x = 200 m y se mueve en sentido positivo a 25 m/s", "ok": False, "feedback": "Ignoraste el signo: el coeficiente de `t` es `−25`, así que la posición disminuye con el tiempo."},
                {"text": "En t = 0 está en x = 200 m y se mueve en sentido negativo a 25 m/s", "ok": True, "feedback": "Exacto: `x₀ = 200 m` y el coeficiente de `t` es la velocidad, `−25 m/s`."},
                {"text": "Parte del origen y frena a 25 m/s²", "ok": False, "feedback": "No hay término con `t²`, así que no hay aceleración: 25 es una velocidad en m/s. Y en `t = 0` la posición es 200 m, no el origen."},
            ],
        },
        "checks": [
            {
                "question": "Nadás un largo de ida y otro de vuelta en una pileta de 50 m y tardás 100 s en total. ¿Cuánto vale tu velocidad media en todo el recorrido?",
                "options": [
                    {"text": "1 m/s", "ok": False, "feedback": "Esa es la rapidez media: distancia recorrida (100 m) dividida por el tiempo (100 s). La velocidad media usa el desplazamiento, que acá es cero."},
                    {"text": "0.5 m/s", "ok": False, "feedback": "Dividiste un solo largo (50 m) por el tiempo total. El desplazamiento total no es 50 m: es 0, porque terminaste donde empezaste."},
                    {"text": "0 m/s", "ok": True, "feedback": "Exacto: volviste al punto de partida, así que `Δx = 0`. Tu rapidez media, en cambio, fue `100 m / 100 s = 1 m/s`."},
                ],
            },
            {
                "question": "El móvil A sale de `x = 0` hacia la derecha a `20 m/s`; en el mismo instante, B sale de `x = 500 m` hacia A a `30 m/s`. ¿En qué posición se encuentran?",
                "options": [
                    {"text": "x = 200 m", "ok": True, "feedback": "Exacto: `20 · t = 500 − 30 · t` → `t = 10 s` → `x = 20 · 10 = 200 m`."},
                    {"text": "x = 250 m", "ok": False, "feedback": "Ese es el punto medio: solo se cruzarían ahí si fueran a la misma velocidad. B es más rápido, así que el encuentro queda más cerca de la salida de A."},
                    {"text": "x = 300 m", "ok": False, "feedback": "300 m es la distancia que recorrió B en los 10 s. La posición del encuentro, medida desde el origen, es `500 − 300 = 200 m`."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá los pasos para resolver un problema de encuentro y por qué los dos móviles tienen que compartir el mismo origen y el mismo reloj.",
    },
    "f-mruv-graficas": {
        "hook": {
            "question": "Un auto que va a 20 m/s frena parejo y se detiene en 40 m. Cuando lleva recorridos 20 m (la mitad de la frenada), ¿ya bajó a 10 m/s?",
            "intuition": "No: todavía va a unos `14 m/s`. La velocidad baja a la mitad en la mitad del **tiempo**, no en la mitad de la distancia: al principio el auto va más rápido y recorre más metros en cada segundo. Por eso en un MRUV hay que elegir bien la ecuación: con tiempo o sin tiempo.",
        },
        "concept": {
            "points": [
                "**MRUV** = aceleración constante: la velocidad cambia lo mismo en cada segundo. `v = v₀ + a · t`.",
                "**Posición**: `x = x₀ + v₀ · t + ½ · a · t²`. El término `½ · a · t²` es lo que se agrega (o se quita) respecto de un MRU.",
                "**Sin tiempo**: `v² = v₀² + 2 · a · Δx`. Es la ecuación ideal cuando no te dan ni te piden el tiempo, como en la distancia de frenado: `d = v₀² / (2 · |a|)`.",
                "**Signos**: un móvil frena cuando `a` tiene signo **opuesto** al de `v`, y aumenta su rapidez cuando tienen el mismo signo. Si se mueve en sentido negativo, frenar corresponde a una aceleración positiva.",
                "**Gráficas**: `v-t` es una recta cuya **pendiente es la aceleración** y cuya **área (con signo) es el desplazamiento**; `x-t` es una parábola; `a-t` es una recta horizontal.",
            ],
            "real_world": [
                {
                    "title": "Distancia de frenado",
                    "detail": "Como `d = v₀² / (2 · |a|)`, la distancia para frenar crece con el cuadrado de la velocidad. Por eso unos pocos km/h de más cambian tanto el resultado frente a un imprevisto.",
                },
                {
                    "title": "El largo de una pista",
                    "detail": "Un avión que necesita `70 m/s` para despegar y acelera a `2.5 m/s²` requiere al menos `70² / (2 · 2.5) = 980 m` de pista.",
                },
                {
                    "title": "El subte entre dos estaciones",
                    "detail": "Acelera, mantiene la velocidad y frena: su gráfica `v-t` es un trapecio, y el área de ese trapecio es la distancia entre las estaciones.",
                },
            ],
            "key_rule": "`v = v₀ + a·t` · `x = x₀ + v₀·t + ½·a·t²` · `v² = v₀² + 2·a·Δx` · En `v-t`: pendiente = aceleración, área = desplazamiento.",
            "pitfall": "Usar `x = v · t` con la velocidad final (o la inicial) en un movimiento acelerado: esa fórmula solo vale con velocidad constante. En un MRUV usá la ecuación horaria completa o el área bajo la gráfica `v-t`.",
        },
        "example": {
            "title": "Frenada de emergencia a 90 km/h",
            "steps": [
                "Vas a `90 km/h` y frenás con una aceleración constante de módulo `5 m/s²`. Unidades y signos: `v₀ = 90 ÷ 3.6 = 25 m/s`; tomando positivo el sentido de avance, `a = −5 m/s²`.",
                "Tiempo hasta detenerte: `0 = 25 − 5 · t` → `t = 5 s`.",
                "Distancia sin usar el tiempo: `0 = 25² + 2 · (−5) · Δx` → `Δx = 625 / 10 = 62.5 m`.",
                "Verificación con la gráfica `v-t`: es un triángulo de base `5 s` y altura `25 m/s`, de área `½ · 5 · 25 = 62.5 m`. Los dos caminos coinciden.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "En una gráfica `v-t`, la recta de un tren baja de `12 m/s` en `t = 0` a `0` en `t = 4 s`. ¿Cuáles son su aceleración y la distancia que recorre en ese tramo?",
            "options": [
                {"text": "a = −3 m/s² y 48 m", "ok": False, "feedback": "La pendiente está bien, pero 48 m es base × altura (`4 · 12`): al área del triángulo le falta el ½. Recorrería 48 m si hubiera seguido a 12 m/s durante los 4 s."},
                {"text": "a = −3 m/s² y 24 m", "ok": True, "feedback": "Exacto: pendiente `(0 − 12) / 4 = −3 m/s²` y área del triángulo `½ · 4 · 12 = 24 m`."},
                {"text": "a = +3 m/s² y 24 m", "ok": False, "feedback": "La distancia está bien, pero la recta baja: la pendiente es negativa, `(0 − 12) / 4 = −3 m/s²`."},
            ],
        },
        "checks": [
            {
                "question": "Un auto parte del reposo y acelera a `2 m/s²` durante `6 s`. ¿Qué distancia recorre?",
                "options": [
                    {"text": "72 m", "ok": False, "feedback": "Multiplicaste la velocidad final (`2 · 6 = 12 m/s`) por el tiempo, como si hubiera ido siempre a 12 m/s. Arrancó de 0, así que recorre la mitad."},
                    {"text": "12 m", "ok": False, "feedback": "12 es la velocidad final en m/s (`v = a · t`), no la distancia."},
                    {"text": "36 m", "ok": True, "feedback": "Exacto: `Δx = ½ · a · t² = ½ · 2 · 6² = 36 m`."},
                ],
            },
            {
                "question": "Una moto se mueve en el sentido negativo del eje (`v = −20 m/s`) y su aceleración es `a = +4 m/s²`. ¿Qué le pasa?",
                "options": [
                    {"text": "Frena: su rapidez disminuye", "ok": True, "feedback": "Exacto: `a` y `v` tienen signos opuestos. Un segundo después va a `−20 + 4 = −16 m/s`: más lento."},
                    {"text": "Va cada vez más rápido, porque la aceleración es positiva", "ok": False, "feedback": "El signo de `a` solo no alcanza: hay que compararlo con el de `v`. Acá son opuestos, así que la rapidez baja (de 20 a 16 m/s en un segundo)."},
                    {"text": "Cambia de sentido en ese mismo instante", "ok": False, "feedback": "Para invertir el sentido primero tiene que llegar a `v = 0`, y eso recién ocurre a los `20 / 4 = 5 s`."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué información da la pendiente y qué información da el área en una gráfica v-t, y por qué frenar no siempre significa aceleración negativa.",
    },
    "f-caida-libre-tiro-vertical": {
        "hook": {
            "question": "Tirás una pelota verticalmente hacia arriba a 20 m/s. Cuando vuelve a tu mano, ¿llega más rápido, más lento o igual que como salió?",
            "intuition": "Si se desprecia el rozamiento del aire, llega con la misma rapidez, `20 m/s`, pero hacia abajo. La gravedad le quita `10 m/s` en cada segundo de subida y le devuelve exactamente lo mismo en la bajada: 2 s para subir y 2 s para bajar.",
        },
        "concept": {
            "points": [
                "**Caída libre y tiro vertical son MRUV** con una aceleración conocida: `g`, vertical y hacia abajo, igual para cualquier masa si se desprecia el aire. En estos problemas usamos `g = 10 m/s²` (el valor medido es ≈ `9.8 m/s²`).",
                "**Elegí el eje y respetalo**: con `y` positivo hacia arriba, `a = −g`: `v = v₀ − g · t` e `y = y₀ + v₀ · t − ½ · g · t²`. Una velocidad negativa significa que el cuerpo está bajando.",
                "**Caída desde el reposo** (conviene el eje hacia abajo): `v = g · t`, `h = ½ · g · t²` y, sin tiempo, `v = √(2 · g · h)`.",
                "**Tiro hacia arriba**: en el punto más alto `v = 0`, de donde `t_subida = v₀ / g` y `h_max = v₀² / (2 · g)`.",
                "**Simetría** (sin aire): al volver a la altura de partida tiene la misma rapidez con sentido contrario, y bajar tarda lo mismo que subir. La aceleración vale `g` hacia abajo en todo el vuelo, también en el punto más alto.",
            ],
            "real_world": [
                {
                    "title": "El salto de un jugador de vóley",
                    "detail": "Para elevarse `0.8 m` hay que despegar a `4 m/s` (`h = v₀² / (2 · g)`), y todo el salto dura apenas `0.8 s` entre subir y bajar.",
                },
                {
                    "title": "Clavados desde la plataforma de 10 m",
                    "detail": "El clavadista entra al agua a `√(2 · 10 · 10) ≈ 14 m/s`, unos 50 km/h, después de caer durante 1.4 s.",
                },
                {
                    "title": "Fuegos artificiales",
                    "detail": "Despreciando el aire, una bomba que sale del mortero a `50 m/s` sube `50² / 20 = 125 m` en 5 s: la mecha se calcula para que estalle cerca de la cima.",
                },
            ],
            "key_rule": "Eje hacia arriba: `v = v₀ − g·t`, `y = y₀ + v₀·t − ½·g·t²` · `t_subida = v₀/g` · `h_max = v₀²/(2·g)` · Desde el reposo: `h = ½·g·t²`, `v = √(2·g·h)`.",
            "pitfall": "Cambiarle el signo a `g` a mitad del problema (\"negativa cuando sube, positiva cuando baja\"). Una vez elegido el eje, la aceleración tiene el mismo signo durante todo el vuelo; lo que cambia de signo es la velocidad.",
        },
        "example": {
            "title": "Seguí paso a paso la pelota lanzada a 20 m/s",
            "steps": [
                "Lanzás hacia arriba a `v₀ = 20 m/s` (sin aire, `g = 10 m/s²`). Eje `y` positivo hacia arriba y origen en tu mano: `v = 20 − 10 · t` e `y = 20 · t − 5 · t²`.",
                "Punto más alto: `v = 0` → `t = 20 / 10 = 2 s`. Altura: `y = 20 · 2 − 5 · 2² = 20 m` (coincide con `v₀² / (2 · g) = 400 / 20`).",
                "Vuelta a la mano: `y = 0` → `20 · t − 5 · t² = 0` → `t = 4 s`, el doble del tiempo de subida. Velocidad: `v = 20 − 10 · 4 = −20 m/s`: la misma rapidez, hacia abajo.",
                "En el simulador de proyectiles, poné el ángulo en `85°` (lo más vertical que permite) y `v₀ = 20 m/s`: mirá cómo la flecha `Vy` se achica al subir, se anula arriba y crece hacia abajo en la bajada.",
            ],
            "lab_link": _LAB,
            "lab_cta": "Ver subida y bajada",
        },
        "check": {
            "question": "Lanzás una piedra hacia arriba a `30 m/s` (sin aire, `g = 10 m/s²`, eje positivo hacia arriba). ¿Cuál es su velocidad a los `4 s`?",
            "options": [
                {"text": "+10 m/s: todavía sube", "ok": False, "feedback": "El módulo está bien, pero el signo no: llegó a la cima a los `30 / 10 = 3 s`, así que a los 4 s ya está bajando."},
                {"text": "70 m/s", "ok": False, "feedback": "Sumaste `g · t` en vez de restarlo: con el eje hacia arriba la aceleración es `−10 m/s²`, y `v = 30 − 10 · 4`."},
                {"text": "−10 m/s: ya está bajando", "ok": True, "feedback": "Exacto: `v = 30 − 10 · 4 = −10 m/s`. Pasó por la cima a los 3 s y lleva 1 s cayendo."},
            ],
        },
        "checks": [
            {
                "question": "Una pelota lanzada verticalmente hacia arriba tarda `3 s` en llegar al punto más alto (sin aire, `g = 10 m/s²`). ¿Con qué velocidad se lanzó y cuánto tarda en total en volver a la mano?",
                "options": [
                    {"text": "30 m/s y 3 s", "ok": False, "feedback": "La velocidad está bien, pero 3 s es solo la subida: falta la bajada, que dura lo mismo."},
                    {"text": "30 m/s y 6 s", "ok": True, "feedback": "Exacto: `v₀ = g · t_subida = 10 · 3 = 30 m/s`, y por simetría el vuelo completo dura `2 · 3 = 6 s`."},
                    {"text": "60 m/s y 6 s", "ok": False, "feedback": "El tiempo total está bien, pero en `v₀ = g · t` va el tiempo de subida (3 s), no el total: `10 · 3 = 30 m/s`."},
                ],
            },
            {
                "question": "Soltás una piedra desde un puente (sin aire, `g = 10 m/s²`). En el primer segundo cae `5 m`. ¿Cuánto cayó en total a los `3 s`?",
                "options": [
                    {"text": "45 m", "ok": True, "feedback": "Exacto: `h = ½ · g · t² = ½ · 10 · 3² = 45 m`. Al triplicar el tiempo, la distancia se multiplica por 9."},
                    {"text": "15 m", "ok": False, "feedback": "Supusiste que cae 5 m en cada segundo, pero la caída es acelerada: la distancia crece con `t²`, no con `t`."},
                    {"text": "30 m", "ok": False, "feedback": "30 es la velocidad a los 3 s en m/s (`v = g · t`), no la distancia. Para la distancia va `h = ½ · g · t²`."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué pasa con la velocidad y con la aceleración de una pelota lanzada hacia arriba durante la subida, en el punto más alto y en la bajada.",
    },
    "f-tiro-oblicuo": {
        "hook": {
            "question": "Pateás una pelota en diagonal. Mientras está en el aire, ¿qué la sigue empujando hacia adelante?",
            "intuition": "Nada, y no hace falta. Si se desprecia el rozamiento del aire, en horizontal no hay aceleración: la pelota conserva la velocidad horizontal con la que salió. La gravedad solo actúa en vertical. Un tiro oblicuo es un MRU horizontal y un tiro vertical ocurriendo **al mismo tiempo**.",
        },
        "concept": {
            "points": [
                "**Descomponé la velocidad inicial**: `v₀x = v₀ · cos θ` y `v₀y = v₀ · sen θ`, con `θ` medido desde la horizontal.",
                "**Dos movimientos independientes**: en horizontal es un MRU, `x = v₀x · t`; en vertical es un tiro vertical, `vy = v₀y − g · t` e `y = y₀ + v₀y · t − ½ · g · t²`. Lo único que comparten es el **tiempo**.",
                "**Si sale y cae al mismo nivel**: `t_vuelo = 2 · v₀y / g`, `h_max = v₀y² / (2 · g)` y `alcance = v₀x · t_vuelo`. Con la misma rapidez, dos ángulos complementarios (como 37° y 53°) dan el mismo alcance, y el máximo se logra a 45°.",
                "**Punto más alto**: se anula solo `vy`. La pelota sigue moviéndose con `v = v₀x`, y la aceleración sigue siendo `g` hacia abajo.",
                "**Tiro horizontal desde una altura `h`**: `v₀y = 0`, así que el tiempo de caída es el de una caída libre, `t = √(2 · h / g)`, y el avance es `x = v₀ · t`.",
            ],
            "real_world": [
                {
                    "title": "Saque de arco",
                    "detail": "Sin contar el aire, el mayor alcance se logra cerca de 45°; un saque más empinado gana altura y tiempo de vuelo, pero pierde distancia.",
                },
                {
                    "title": "Avión hidrante",
                    "detail": "El agua que suelta conserva la velocidad horizontal del avión mientras cae: por eso el piloto la larga antes de estar sobre el fuego.",
                },
                {
                    "title": "Salto en largo",
                    "detail": "El atleta es un proyectil: la carrera le da la velocidad horizontal y el pique le agrega la vertical, que decide cuánto tiempo estará en el aire.",
                },
            ],
            "key_rule": "`v₀x = v₀·cos θ`, `v₀y = v₀·sen θ` · Horizontal: `x = v₀x·t` · Vertical: `vy = v₀y − g·t`, `y = y₀ + v₀y·t − ½·g·t²` · El tiempo une los dos ejes.",
            "pitfall": "Meter la velocidad `v₀` completa en las fórmulas verticales (tiempo de vuelo, altura máxima). En vertical solo cuenta `v₀y = v₀ · sen θ`; en horizontal, solo `v₀x = v₀ · cos θ`.",
        },
        "example": {
            "title": "Un tiro libre a 20 m/s y 53°",
            "steps": [
                "Pateás desde el pasto a `v₀ = 20 m/s` con `53°` (`sen 53° = 0.8`, `cos 53° = 0.6`), sin aire y con `g = 10 m/s²`. Componentes: `v₀x = 20 · 0.6 = 12 m/s` y `v₀y = 20 · 0.8 = 16 m/s`.",
                "Vertical: sube hasta que `vy = 0` → `t_subida = 16 / 10 = 1.6 s`. Altura máxima: `h = 16² / (2 · 10) = 12.8 m`.",
                "Tiempo de vuelo (vuelve al mismo nivel): `2 · 1.6 = 3.2 s`.",
                "Horizontal: `alcance = v₀x · t_vuelo = 12 · 3.2 = 38.4 m`. En el punto más alto la pelota no está quieta: va a `12 m/s`.",
                "Reproducilo en el simulador (`20 m/s`, `53°`): como usa `g = 9.81 m/s²`, los valores salen apenas distintos (alcance ≈ `39 m`).",
            ],
            "lab_link": _LAB,
            "lab_cta": "Lanzar a 53° en el simulador",
        },
        "check": {
            "question": "Pateás una pelota a `20 m/s` con `30°` sobre la horizontal (`sen 30° = 0.5`; sin aire, `g = 10 m/s²`). ¿Cuánto dura el vuelo hasta que vuelve al pasto?",
            "options": [
                {"text": "1 s", "ok": False, "feedback": "Ese es solo el tiempo de subida (`v₀y / g = 10 / 10`). Falta la bajada, que dura lo mismo."},
                {"text": "2 s", "ok": True, "feedback": "Exacto: `v₀y = 20 · 0.5 = 10 m/s` y `t_vuelo = 2 · 10 / 10 = 2 s`."},
                {"text": "4 s", "ok": False, "feedback": "Usaste la velocidad completa (`2 · 20 / 10`). En vertical solo cuenta `v₀y = 20 · 0.5 = 10 m/s`."},
            ],
        },
        "checks": [
            {
                "question": "Desde un acantilado de `45 m` de altura se lanza una piedra en dirección horizontal a `10 m/s` (sin aire, `g = 10 m/s²`). ¿A qué distancia horizontal de la base cae?",
                "options": [
                    {"text": "30 m", "ok": True, "feedback": "Exacto: `t = √(2 · 45 / 10) = 3 s` y `x = 10 · 3 = 30 m`."},
                    {"text": "45 m", "ok": False, "feedback": "Usaste `t = h / g = 4.5 s`. En la caída vale `h = ½ · g · t²`, así que `t = √(2 · 45 / 10) = 3 s`."},
                    {"text": "90 m", "ok": False, "feedback": "Calculaste `2 · h / g = 9` y lo usaste como tiempo: ese valor es `t²`. Falta la raíz cuadrada: `t = √9 = 3 s`."},
                ],
            },
            {
                "question": "Un avión hidrante vuela horizontal a `60 m/s` y suelta su carga de agua desde `80 m` de altura (sin aire, `g = 10 m/s²`). Si el avión mantiene su velocidad, ¿dónde está cuando el agua toca el suelo?",
                "options": [
                    {"text": "240 m más adelante que el agua", "ok": False, "feedback": "Eso supone que el agua cae en vertical desde donde se soltó, perdiendo su velocidad horizontal. Sin aire la conserva: avanza los mismos `60 · 4 = 240 m` que el avión."},
                    {"text": "Más atrás que el agua", "ok": False, "feedback": "Para eso el agua tendría que ganar velocidad horizontal, y en horizontal no hay aceleración: sigue a 60 m/s, igual que el avión."},
                    {"text": "Justo encima del punto donde cae el agua", "ok": True, "feedback": "Exacto: el agua conserva los 60 m/s horizontales del avión, así que los dos avanzan `60 · 4 = 240 m` durante los 4 s de caída."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué un tiro oblicuo se puede estudiar como dos movimientos separados y qué magnitud los conecta.",
    },
}
