"""Ejercicios de Física: cinemática (vectores, MRU, MRUV, caída libre y tiro vertical,
tiro oblicuo) y movimiento circular uniforme.

Cuatro problemas por tema: uno de nivel 1, dos de nivel 2 y uno de nivel 3.

Convenciones (las mismas de las lecciones): en los problemas con gravedad se usa
g = 10 m/s² y se desprecia el rozamiento del aire (dicho en cada enunciado); los senos,
cosenos y tangentes que no son exactos se dan como dato; cuando aparece π en un
resultado numérico se indica "usá π ≈ 3.14" y el redondeo.
"""

from __future__ import annotations

EXERCISES: list[dict] = [
    # ==================== VECTORES ====================
    {
        "id": "f-vectores-operaciones-1",
        "node": "f-vectores-operaciones",
        "kind": "problem",
        "level": 1,
        "title": "Tirar de un trineo entre dos",
        "statement": (
            "En el cerro Otto (Bariloche) arrastrás un trineo sobre la nieve horizontal tirando de una soga con una "
            "fuerza de 100 N. La soga forma un ángulo de 37° por encima de la horizontal (sen 37° = 0.6 y "
            "cos 37° = 0.8). Una amiga ayuda empujando el trineo desde atrás con una fuerza horizontal de 64 N, en el "
            "mismo sentido en que avanza. Tomá el eje x horizontal, en el sentido de avance, y el eje y vertical "
            "hacia arriba."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la componente horizontal de tu fuerza? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 80, "tolerance": 0, "unit": "N"},
                "answer": "80 N",
            },
            {
                "prompt": "b) ¿Cuánto vale la componente vertical de tu fuerza? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": "N"},
                "answer": "60 N",
            },
            {
                "prompt": "c) ¿Cuánto vale el módulo de la resultante de esas dos fuerzas (la tuya y la de tu amiga)? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 156, "tolerance": 0, "unit": "N"},
                "answer": "156 N",
            },
        ],
        "hints": [
            "Dibujá tu fuerza como la hipotenusa de un triángulo rectángulo: el cateto pegado al ángulo de 37° es la componente horizontal y el opuesto es la vertical.",
            "Para la resultante no sumes los módulos: sumá las componentes x entre sí y las componentes y entre sí. La fuerza de tu amiga solo tiene componente x.",
            "Con las dos componentes de la resultante, el módulo sale por Pitágoras.",
        ],
        "solution": [
            "El ángulo de 37° está medido desde la horizontal, así que la componente horizontal es el cateto adyacente (va con el coseno) y la vertical es el cateto opuesto (va con el seno).",
            "Componente horizontal: `Fx = F · cos 37° = 100 · 0.8 = 80 N`.",
            "Componente vertical: `Fy = F · sen 37° = 100 · 0.6 = 60 N`, hacia arriba. Verificación: `√(80² + 60²) = √10000 = 100 N`, el módulo original.",
            "La fuerza de tu amiga es horizontal y en el sentido de avance: `(64; 0) N`. Sumá componente a componente: `R = (80 + 64; 60 + 0) = (144; 60) N`.",
            "Módulo de la resultante: `|R| = √(144² + 60²) = √(20736 + 3600) = √24336 = 156 N`.",
            "Respuestas: 80 N, 60 N y 156 N. El error típico es sumar los módulos (`100 + 64 = 164 N`): eso solo vale cuando las dos fuerzas tienen la misma dirección y sentido, y acá la soga está inclinada.",
        ],
    },
    {
        "id": "f-vectores-operaciones-2",
        "node": "f-vectores-operaciones",
        "kind": "problem",
        "level": 2,
        "title": "Doblar la esquina: el cambio de velocidad",
        "statement": (
            "Un auto circula hacia el este a 20 m/s, toma una curva y sale de ella circulando hacia el norte a "
            "15 m/s. La maniobra dura 5 s. Tomá el eje x hacia el este y el eje y hacia el norte. El cambio de "
            "velocidad es el vector `Δv = v₂ − v₁` y la aceleración media es `a_m = Δv / Δt`, un vector con la misma "
            "dirección y sentido que `Δv`. Datos: tg 37° = 0.75 y tg 53° ≈ 1.33."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale el módulo del cambio de velocidad `Δv`? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 25, "tolerance": 0, "unit": "m/s"},
                "answer": "25 m/s",
            },
            {
                "prompt": "b) ¿Qué ángulo forma `Δv` con el eje x positivo (el este), medido en sentido antihorario? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 143, "tolerance": 0.005, "unit": "°"},
                "answer": "143°",
            },
            {
                "prompt": "c) ¿Cuánto vale el módulo de la aceleración media durante la maniobra? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "m/s²"},
                "answer": "5 m/s²",
            },
        ],
        "hints": [
            "Escribí cada velocidad como un par de componentes: la que apunta al este solo tiene x; la que apunta al norte solo tiene y.",
            "Restar vectores es restar componente a componente (final menos inicial). Con el resultado, Pitágoras para el módulo.",
            "Para el ángulo, mirá los signos de las dos componentes de `Δv` antes de usar la tangente: te dicen en qué cuadrante está.",
        ],
        "solution": [
            "Velocidades por componentes: `v₁ = (20; 0) m/s` (hacia el este) y `v₂ = (0; 15) m/s` (hacia el norte).",
            "Resta componente a componente: `Δv = v₂ − v₁ = (0 − 20; 15 − 0) = (−20; 15) m/s`.",
            "Módulo: `|Δv| = √((−20)² + 15²) = √(400 + 225) = √625 = 25 m/s`.",
            "Dirección: `Δvx < 0` y `Δvy > 0`, así que `Δv` está en el segundo cuadrante (apunta hacia el noroeste). El ángulo `α` que forma con el eje x negativo cumple `tg α = 15 / 20 = 0.75` → `α = 37°`.",
            "Medido desde el eje x positivo en sentido antihorario: `180° − 37° = 143°`.",
            "Aceleración media: `|a_m| = |Δv| / Δt = 25 / 5 = 5 m/s²`, con la dirección de `Δv`.",
            "Respuestas: 25 m/s, 143° y 5 m/s². El error típico es restar los módulos (`15 − 20 = −5 m/s`) y concluir que la aceleración media vale 1 m/s²: la velocidad cambió sobre todo de dirección, y eso solo se ve restando vectores.",
        ],
    },
    {
        "id": "f-vectores-operaciones-3",
        "node": "f-vectores-operaciones",
        "kind": "problem",
        "level": 2,
        "title": "Tres tramos de vuelo y el regreso",
        "statement": (
            "Una avioneta fumigadora despega de un aeródromo de La Pampa y vuela tres tramos rectos: primero 10 km "
            "en una dirección a 37° al norte del este (sen 37° = 0.6 y cos 37° = 0.8), después 20 km hacia el oeste "
            "y por último 22 km hacia el sur. Tomá el eje x hacia el este y el eje y hacia el norte. "
            "Datos: tg 37° = 0.75 y tg 53° ≈ 1.33."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la componente y (norte-sur) del desplazamiento total? Respondé solo con el número en km, con su signo.",
                "check": {"type": "numeric", "value": -16, "tolerance": 0, "unit": "km"},
                "answer": "−16 km",
            },
            {
                "prompt": "b) ¿A qué distancia del aeródromo queda la avioneta al terminar el tercer tramo? Respondé solo con el número en km.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "km"},
                "answer": "20 km",
            },
            {
                "prompt": "c) ¿En qué dirección tiene que volar para volver en línea recta al aeródromo?",
                "check": {
                    "type": "choice",
                    "options": [
                        "53° al norte del este",
                        "53° al sur del oeste",
                        "37° al norte del este",
                        "53° al norte del oeste",
                    ],
                    "correct": 0,
                },
                "answer": "53° al norte del este",
            },
        ],
        "hints": [
            "Escribí cada tramo como un par (x; y). Solo el primero hay que descomponerlo con seno y coseno; el oeste es x negativa y el sur es y negativa.",
            "Sumá las tres componentes x y las tres componentes y: ese vector es el desplazamiento total, y su módulo es la distancia al aeródromo.",
            "El regreso es el vector opuesto al desplazamiento total: cambiale el signo a las dos componentes antes de calcular el ángulo.",
        ],
        "solution": [
            "Primer tramo: `A = (10 · cos 37°; 10 · sen 37°) = (10 · 0.8; 10 · 0.6) = (8; 6) km`. Segundo: `B = (−20; 0) km`. Tercero: `C = (0; −22) km`.",
            "Suma eje por eje: `Rx = 8 − 20 + 0 = −12 km` y `Ry = 6 + 0 − 22 = −16 km`. El desplazamiento total es `R = (−12; −16) km`.",
            "Distancia al aeródromo: `|R| = √((−12)² + (−16)²) = √(144 + 256) = √400 = 20 km`.",
            "`R` tiene las dos componentes negativas: la avioneta quedó al sudoeste del aeródromo. Para volver tiene que recorrer el vector opuesto, `−R = (12; 16) km`, que apunta al noreste (primer cuadrante).",
            "Ángulo del regreso respecto del este: `tg θ = 16 / 12 ≈ 1.33` → `θ = 53°` al norte del este.",
            "Respuestas: −16 km, 20 km y 53° al norte del este. Voló 52 km en total pero quedó a solo 20 km, porque los tramos no son paralelos. '53° al sur del oeste' es la dirección de `R` (hacia donde se alejó), no la del regreso; 37° sale de invertir el cociente (`12 / 16 = 0.75`).",
        ],
    },
    {
        "id": "f-vectores-operaciones-4",
        "node": "f-vectores-operaciones",
        "kind": "problem",
        "level": 3,
        "title": "Avioneta con viento cruzado",
        "statement": (
            "Una avioneta sanitaria tiene que volar desde un aeródromo hasta un paraje ubicado 400 km exactamente al "
            "norte. Sopla un viento constante de 60 km/h desde el oeste hacia el este, y la avioneta vuela a "
            "100 km/h respecto del aire. La velocidad respecto del suelo es la suma vectorial de la velocidad "
            "respecto del aire y la velocidad del viento: `v_suelo = v_aire + v_viento`. "
            "Datos: sen 37° = 0.6 y cos 37° = 0.8; sen 53° = 0.8 y cos 53° = 0.6."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué ángulo tiene que formar la proa con la dirección norte, desviada hacia el oeste, para que la avioneta avance exactamente hacia el norte respecto del suelo? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 37, "tolerance": 0.005, "unit": "°"},
                "answer": "37°",
            },
            {
                "prompt": "b) ¿Con qué rapidez avanza respecto del suelo? Respondé solo con el número en km/h.",
                "check": {"type": "numeric", "value": 80, "tolerance": 0, "unit": "km/h"},
                "answer": "80 km/h",
            },
            {
                "prompt": "c) ¿Cuánto tarda en llegar al paraje? Respondé solo con el número en h.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "h"},
                "answer": "5 h",
            },
        ],
        "hints": [
            "Tomá x hacia el este e y hacia el norte. Para avanzar exactamente hacia el norte, la velocidad respecto del suelo no puede tener componente x.",
            "Si la proa se desvía un ángulo θ del norte hacia el oeste, la velocidad respecto del aire es `(−100 · sen θ; 100 · cos θ)`. Su componente x tiene que cancelar a la del viento.",
            "La rapidez respecto del suelo es lo que queda en el eje y, y con ella el viaje es un MRU de 400 km.",
        ],
        "solution": [
            "Ejes: x hacia el este, y hacia el norte. Viento: `v_viento = (60; 0) km/h`. Si la proa forma un ángulo θ con el norte, desviada hacia el oeste, la velocidad respecto del aire es `v_aire = (−100 · sen θ; 100 · cos θ) km/h` (el ángulo se mide desde el eje y, por eso el seno va en x).",
            "Suma: `v_suelo = (60 − 100 · sen θ; 100 · cos θ)`. Para ir exactamente al norte la componente x tiene que ser cero: `60 − 100 · sen θ = 0` → `sen θ = 0.6` → `θ = 37°` al oeste del norte.",
            "Rapidez respecto del suelo: es la componente y, `100 · cos 37° = 100 · 0.8 = 80 km/h`.",
            "Verificación: los tres vectores forman un triángulo rectángulo con hipotenusa 100 (aire) y catetos 60 (viento) y 80 (suelo): `60² + 80² = 3600 + 6400 = 100²`.",
            "Tiempo de viaje (MRU respecto del suelo): `t = 400 / 80 = 5 h`.",
            "Respuestas: 37°, 80 km/h y 5 h. Errores típicos: apuntar la proa al norte y calcular `400 / 100 = 4 h` (el viento la sacaría `60 · 4 = 240 km` hacia el este), o sumar por Pitágoras `√(100² + 60²) ≈ 117 km/h`, que es la rapidez respecto del suelo cuando la proa apunta al norte y la avioneta se desvía.",
        ],
    },
    # ==================== MRU ====================
    {
        "id": "f-mru-encuentro-1",
        "node": "f-mru-encuentro",
        "kind": "problem",
        "level": 1,
        "title": "De Retiro a Rosario con una parada",
        "statement": (
            "Un micro sale de la terminal de Retiro (Buenos Aires) hacia Rosario. Viaja 2 h a 90 km/h constantes, se "
            "detiene 30 min en un parador y después completa el viaje en 1.5 h a 80 km/h constantes. Considerá la "
            "ruta recta y cada tramo en movimiento como un MRU."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué distancia total recorre el micro? Respondé solo con el número en km.",
                "check": {"type": "numeric", "value": 300, "tolerance": 0, "unit": "km"},
                "answer": "300 km",
            },
            {
                "prompt": "b) ¿Cuál es su rapidez media en todo el viaje, contando la parada? Respondé solo con el número en km/h.",
                "check": {"type": "numeric", "value": 75, "tolerance": 0, "unit": "km/h"},
                "answer": "75 km/h",
            },
            {
                "prompt": "c) ¿Cómo es la gráfica posición-tiempo (x-t) del viaje completo?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Tres tramos rectos: uno inclinado, uno horizontal y otro inclinado, menos empinado que el primero",
                        "Tres tramos rectos inclinados: el del medio es el más empinado",
                        "Dos tramos horizontales, a la altura 90 y a la altura 80, separados por una caída a cero",
                        "Una sola recta inclinada desde la salida hasta la llegada",
                    ],
                    "correct": 0,
                },
                "answer": "Tres tramos rectos: uno inclinado (90 km/h), uno horizontal (detenido) y otro inclinado menos empinado (80 km/h).",
            },
        ],
        "hints": [
            "Calculá la distancia de cada tramo por separado con `Δx = v · Δt` y sumalas.",
            "La rapidez media es la distancia total dividida por el tiempo total, y el reloj no se detiene durante la parada: 30 min son 0.5 h.",
            "En una gráfica x-t la pendiente es la velocidad: pensá cuánto vale en cada uno de los tres tramos.",
        ],
        "solution": [
            "Primer tramo: `Δx₁ = 90 · 2 = 180 km`. Parada: `Δx = 0` durante 0.5 h. Tercer tramo: `Δx₃ = 80 · 1.5 = 120 km`.",
            "Distancia total: `180 + 120 = 300 km`.",
            "Tiempo total, con la parada incluida: `2 + 0.5 + 1.5 = 4 h`.",
            "Rapidez media: `300 / 4 = 75 km/h`. Como el micro no cambia de sentido, coincide con el módulo de la velocidad media.",
            "Gráfica x-t: la pendiente es la velocidad. Primer tramo, recta de pendiente 90 km/h; parada, recta horizontal (la posición no cambia); último tramo, recta de pendiente 80 km/h, un poco menos empinada que la primera.",
            "Respuestas: 300 km y 75 km/h. Errores típicos: promediar las velocidades (`(90 + 80) / 2 = 85 km/h`) o no contar la parada (`300 / 3.5 ≈ 85.7 km/h`). Los dos tramos horizontales 'a 90 y a 80' corresponden a la gráfica v-t, no a la x-t.",
        ],
    },
    {
        "id": "f-mru-encuentro-2",
        "node": "f-mru-encuentro",
        "kind": "problem",
        "level": 2,
        "title": "El auto que sale una hora después",
        "statement": (
            "Un camión sale de Rosario hacia Córdoba por la autopista a las 8:00 y viaja a 80 km/h constantes. A las "
            "9:00 sale del mismo lugar, por la misma ruta y en el mismo sentido, un auto a 120 km/h constantes. "
            "Considerá la ruta recta."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto tiempo después de su propia salida el auto alcanza al camión? Respondé solo con el número en h.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "h"},
                "answer": "2 h (a las 11:00)",
            },
            {
                "prompt": "b) ¿A qué distancia de Rosario lo alcanza? Respondé solo con el número en km.",
                "check": {"type": "numeric", "value": 240, "tolerance": 0, "unit": "km"},
                "answer": "240 km",
            },
            {
                "prompt": "c) ¿Qué distancia separaba a los dos vehículos a las 10:00? Respondé solo con el número en km.",
                "check": {"type": "numeric", "value": 40, "tolerance": 0, "unit": "km"},
                "answer": "40 km",
            },
        ],
        "hints": [
            "Usá un solo reloj para los dos, por ejemplo `t = 0` a las 8:00. El auto sale una hora más tarde: cuando el reloj marca `t`, el auto lleva viajando `t − 1` horas.",
            "Escribí `x_camión = 80 · t` y `x_auto = 120 · (t − 1)` con origen en Rosario, e igualalas.",
            "Otra mirada: a las 9:00 el camión lleva 80 km de ventaja y el auto le descuenta 40 km en cada hora.",
        ],
        "solution": [
            "Sistema de referencia: origen en Rosario, positivo hacia Córdoba, `t = 0` a las 8:00 (t en horas, x en km).",
            "Camión: `x_C = 80 · t`. Auto (sale en `t = 1 h`): `x_A = 120 · (t − 1)`, válida para `t ≥ 1 h`.",
            "Encuentro: `80 · t = 120 · (t − 1)` → `80 · t = 120 · t − 120` → `40 · t = 120` → `t = 3 h`, es decir, a las 11:00.",
            "Medido desde la salida del auto: `3 − 1 = 2 h`.",
            "Posición: `x_C = 80 · 3 = 240 km` de Rosario. Verificación con el auto: `x_A = 120 · 2 = 240 km`.",
            "A las 10:00 (`t = 2 h`): `x_C = 80 · 2 = 160 km` y `x_A = 120 · 1 = 120 km`; los separan `160 − 120 = 40 km`.",
            "Respuestas: 2 h, 240 km y 40 km. Coincide con el razonamiento de la ventaja: 80 km de ventaja a las 9:00, que se achica a razón de `120 − 80 = 40 km/h` → `80 / 40 = 2 h`. El error típico es usar el mismo tiempo de viaje para los dos, como si hubieran salido juntos.",
        ],
    },
    {
        "id": "f-mru-encuentro-3",
        "node": "f-mru-encuentro",
        "kind": "problem",
        "level": 2,
        "title": "Un cruce leído en la gráfica x-t",
        "statement": (
            "En una misma gráfica posición-tiempo están dibujadas las rectas de dos ciclistas que pedalean por la "
            "misma bicisenda recta. La recta de Ana pasa por los puntos (t = 0; x = 0) y (t = 10 s; x = 50 m). La "
            "recta de Bruno pasa por los puntos (t = 0; x = 240 m) y (t = 20 s; x = 180 m)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la velocidad de Bruno? Respondé solo con el número en m/s, con su signo.",
                "check": {"type": "numeric", "value": -3, "tolerance": 0, "unit": "m/s"},
                "answer": "−3 m/s",
            },
            {
                "prompt": "b) ¿En qué instante se cruzan? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": "s"},
                "answer": "30 s",
            },
            {
                "prompt": "c) ¿En qué posición se cruzan? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 150, "tolerance": 0, "unit": "m"},
                "answer": "150 m",
            },
        ],
        "hints": [
            "La velocidad de cada ciclista es la pendiente de su recta: `Δx / Δt` entre los dos puntos que te dan.",
            "El punto de cada recta en `t = 0` es la posición inicial `x₀`. Con `x₀` y `v` escribí la ecuación horaria de cada uno.",
            "Cruzarse es estar en la misma posición en el mismo instante: igualá las dos ecuaciones horarias.",
        ],
        "solution": [
            "Velocidad de Ana (pendiente): `v_A = (50 − 0) / (10 − 0) = 5 m/s`.",
            "Velocidad de Bruno: `v_B = (180 − 240) / (20 − 0) = −60 / 20 = −3 m/s`. El signo negativo indica que avanza hacia posiciones decrecientes: viene al encuentro de Ana.",
            "Ecuaciones horarias (x en m, t en s): `x_A = 5 · t` y `x_B = 240 − 3 · t`.",
            "Encuentro: `5 · t = 240 − 3 · t` → `8 · t = 240` → `t = 30 s`.",
            "Posición: `x_A = 5 · 30 = 150 m`. Verificación con Bruno: `x_B = 240 − 3 · 30 = 150 m`.",
            "Respuestas: −3 m/s, 30 s y 150 m. En la gráfica, ese es el punto (30 s; 150 m) donde se cortan las dos rectas. El error típico es tomar la velocidad de Bruno como +3 m/s: la ecuación quedaría `5 · t = 240 + 3 · t` y daría `t = 120 s`, un 'alcance' que no existe porque van en sentidos opuestos.",
        ],
    },
    {
        "id": "f-mru-encuentro-4",
        "node": "f-mru-encuentro",
        "kind": "problem",
        "level": 3,
        "title": "Camión y auto por la Ruta 2, con salidas a distinta hora",
        "statement": (
            "Buenos Aires y Mar del Plata están separadas unos 400 km por la Ruta 2 (considerala recta). A las 8:00 "
            "sale un camión de Buenos Aires hacia Mar del Plata a 60 km/h constantes. A las 10:00 sale un auto de "
            "Mar del Plata hacia Buenos Aires, por la misma ruta, a 100 km/h constantes. Tomá el origen en Buenos "
            "Aires, el eje positivo hacia Mar del Plata y `t = 0` a las 8:00."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto tiempo después de las 8:00 se cruzan? Respondé solo con el número en h (en forma decimal).",
                "check": {"type": "numeric", "value": 3.75, "tolerance": 0, "unit": "h"},
                "answer": "3.75 h (a las 11:45)",
            },
            {
                "prompt": "b) ¿A qué distancia de Buenos Aires se cruzan? Respondé solo con el número en km.",
                "check": {"type": "numeric", "value": 225, "tolerance": 0, "unit": "km"},
                "answer": "225 km",
            },
            {
                "prompt": "c) Antes de cruzarse, ¿cuánto tiempo después de las 8:00 están separados exactamente 80 km? Respondé solo con el número en h (en forma decimal).",
                "check": {"type": "numeric", "value": 3.25, "tolerance": 0, "unit": "h"},
                "answer": "3.25 h (a las 11:15)",
            },
        ],
        "hints": [
            "El auto arranca en `x₀ = 400 km`, se mueve en sentido negativo y sale 2 h tarde: cuando el reloj marca `t`, lleva viajando `t − 2` horas.",
            "Ecuaciones: `x_camión = 60 · t` y `x_auto = 400 − 100 · (t − 2)`. Para el cruce, igualalas.",
            "Antes del cruce el auto está más adelante (x mayor) que el camión: la separación es `x_auto − x_camión`. Igualala a 80 km.",
        ],
        "solution": [
            "Camión: sale del origen en `t = 0` con velocidad positiva: `x_C = 60 · t` (x en km, t en h).",
            "Auto: sale de `x₀ = 400 km` en `t = 2 h` y va hacia el origen (velocidad negativa): `x_A = 400 − 100 · (t − 2) = 600 − 100 · t`, válida para `t ≥ 2 h`.",
            "Cruce: `60 · t = 600 − 100 · t` → `160 · t = 600` → `t = 3.75 h`, es decir, 3 h 45 min después de las 8:00: a las 11:45. Como `3.75 > 2`, el auto ya estaba en viaje y la ecuación es válida.",
            "Posición del cruce: `x_C = 60 · 3.75 = 225 km` de Buenos Aires. Verificación: `x_A = 600 − 100 · 3.75 = 225 km`.",
            "Separación antes del cruce: `x_A − x_C = (600 − 100 · t) − 60 · t = 600 − 160 · t`. Igualando a 80: `600 − 160 · t = 80` → `160 · t = 520` → `t = 3.25 h` (a las 11:15).",
            "Verificación: en `t = 3.25 h` el camión está en `60 · 3.25 = 195 km` y el auto en `600 − 325 = 275 km`; los separan 80 km. Además `3.25 > 2`, así que el auto ya había salido.",
            "Respuestas: 3.75 h, 225 km y 3.25 h. Errores típicos: darle al auto el mismo tiempo de viaje que al camión (`60 · t = 400 − 100 · t` da `t = 2.5 h`, cuando el auto lleva apenas media hora en la ruta) o ponerle velocidad positiva al que viene de frente.",
        ],
    },
    # ==================== MRUV ====================
    {
        "id": "f-mruv-graficas-1",
        "node": "f-mruv-graficas",
        "kind": "problem",
        "level": 1,
        "title": "Carril de aceleración de la autopista",
        "statement": (
            "Un auto entra a la autopista Buenos Aires–La Plata por el carril de aceleración: en un tramo recto pasa "
            "de 15 m/s a 27 m/s en 6 s, con aceleración constante."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale su aceleración? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "m/s²"},
                "answer": "2 m/s²",
            },
            {
                "prompt": "b) ¿Qué distancia recorre en esos 6 s? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 126, "tolerance": 0, "unit": "m"},
                "answer": "126 m",
            },
        ],
        "hints": [
            "La aceleración es el cambio de velocidad dividido por el tiempo: despejala de `v = v₀ + a · t`.",
            "Para la distancia usá `Δx = v₀ · t + ½ · a · t²`. No vale `v · t` con la velocidad final: el auto no fue todo el tiempo a 27 m/s.",
        ],
        "solution": [
            "Datos: `v₀ = 15 m/s`, `v = 27 m/s`, `t = 6 s`. Sentido positivo: el de avance.",
            "Aceleración: `a = (v − v₀) / t = (27 − 15) / 6 = 12 / 6 = 2 m/s²`.",
            "Distancia: `Δx = v₀ · t + ½ · a · t² = 15 · 6 + ½ · 2 · 6² = 90 + 36 = 126 m`.",
            "Verificación con el área del trapecio en la gráfica v-t: `(15 + 27) / 2 · 6 = 21 · 6 = 126 m`. Y con la ecuación sin tiempo: `v₀² + 2 · a · Δx = 225 + 2 · 2 · 126 = 729 = 27²`.",
            "Respuestas: 2 m/s² y 126 m. El error típico es calcular `27 · 6 = 162 m` (o `15 · 6 = 90 m`), como si la velocidad hubiera sido constante.",
        ],
    },
    {
        "id": "f-mruv-graficas-2",
        "node": "f-mruv-graficas",
        "kind": "problem",
        "level": 2,
        "title": "Tiempo de reacción y frenada en la ruta",
        "statement": (
            "Vas manejando por una ruta recta a 72 km/h cuando ves una vaca parada en la calzada, 70 m más adelante. "
            "Tardás 0.75 s en reaccionar (durante ese tiempo el auto sigue a velocidad constante) y después frenás "
            "con una aceleración constante de módulo 4 m/s² hasta detenerte."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué distancia recorre el auto durante el tiempo de reacción? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": "m"},
                "answer": "15 m",
            },
            {
                "prompt": "b) ¿Qué distancia total recorre desde que ves la vaca hasta detenerte? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 65, "tolerance": 0, "unit": "m"},
                "answer": "65 m",
            },
            {
                "prompt": "c) Si hubieras ido a 108 km/h, con el mismo tiempo de reacción y los mismos frenos, ¿qué distancia total habrías necesitado para detenerte? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 135, "tolerance": 0, "unit": "m"},
                "answer": "135 m",
            },
        ],
        "hints": [
            "Pasá la velocidad a m/s (dividí por 3.6) y separá el problema en dos etapas: un MRU mientras reaccionás y un MRUV mientras frenás.",
            "Para la frenada no te dan el tiempo: usá `v² = v₀² + 2 · a · Δx` con `v = 0` y `a = −4 m/s²`.",
            "La distancia total es la suma de las dos etapas. Para el inciso c repetí todo con 30 m/s.",
        ],
        "solution": [
            "Unidades: `72 km/h ÷ 3.6 = 20 m/s`. Sentido positivo: el de avance.",
            "Etapa de reacción (MRU): `d₁ = v · t = 20 · 0.75 = 15 m`.",
            "Etapa de frenado (MRUV con `a = −4 m/s²`): `0 = 20² + 2 · (−4) · d₂` → `d₂ = 400 / 8 = 50 m`.",
            "Distancia total: `15 + 50 = 65 m`. Como la vaca estaba a 70 m, el auto se detiene 5 m antes.",
            "A 108 km/h: `108 ÷ 3.6 = 30 m/s`. Reacción: `30 · 0.75 = 22.5 m`. Frenado: `30² / (2 · 4) = 900 / 8 = 112.5 m`. Total: `22.5 + 112.5 = 135 m`.",
            "Respuestas: 15 m, 65 m y 135 m. Con un 50 % más de velocidad, la distancia total es más del doble: la parte de reacción crece en proporción a `v`, pero la de frenado crece con `v²` (`1.5² = 2.25` veces). A 108 km/h no habrías podido evitar a la vaca.",
        ],
    },
    {
        "id": "f-mruv-graficas-3",
        "node": "f-mruv-graficas",
        "kind": "problem",
        "level": 2,
        "title": "Una gráfica v-t que cruza el eje del tiempo",
        "statement": (
            "La gráfica velocidad-tiempo de un carrito que se mueve sobre un riel recto es un segmento de recta que "
            "baja desde v = 12 m/s en t = 0 hasta v = −8 m/s en t = 10 s."
        ),
        "parts": [
            {
                "prompt": "a) ¿En qué instante el carrito se detiene un momento e invierte su sentido de movimiento? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": "s"},
                "answer": "6 s",
            },
            {
                "prompt": "b) ¿Cuánto vale su desplazamiento entre t = 0 y t = 10 s? Respondé solo con el número en m, con su signo.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "m"},
                "answer": "20 m",
            },
            {
                "prompt": "c) ¿Qué distancia total recorre en esos 10 s? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 52, "tolerance": 0, "unit": "m"},
                "answer": "52 m",
            },
        ],
        "hints": [
            "La pendiente de la recta es la aceleración. Con ella escribí `v = v₀ + a · t` y buscá cuándo `v = 0`.",
            "El desplazamiento es el área entre la recta y el eje del tiempo, con signo: lo que queda por debajo del eje resta.",
            "Para la distancia recorrida, las dos áreas (los dos triángulos) se suman en valor absoluto.",
        ],
        "solution": [
            "Aceleración (pendiente): `a = (−8 − 12) / (10 − 0) = −20 / 10 = −2 m/s²`. Entonces `v = 12 − 2 · t`.",
            "Se detiene cuando `v = 0`: `12 − 2 · t = 0` → `t = 6 s`. Antes de ese instante la velocidad es positiva (avanza); después es negativa (vuelve).",
            "Área del triángulo sobre el eje (de 0 a 6 s): `½ · 6 · 12 = 36 m`. El carrito avanza 36 m.",
            "Área del triángulo bajo el eje (de 6 a 10 s): `½ · 4 · 8 = 16 m`. El carrito retrocede 16 m.",
            "Desplazamiento (áreas con signo): `36 − 16 = 20 m`. Verificación con la ecuación horaria: `Δx = 12 · 10 + ½ · (−2) · 10² = 120 − 100 = 20 m`.",
            "Distancia recorrida (áreas en valor absoluto): `36 + 16 = 52 m`.",
            "Respuestas: 6 s, 20 m y 52 m. El error típico es confundir las dos últimas: la ecuación horaria da el desplazamiento (20 m), no el camino recorrido, cuando el móvil invierte el sentido.",
        ],
    },
    {
        "id": "f-mruv-graficas-4",
        "node": "f-mruv-graficas",
        "kind": "problem",
        "level": 3,
        "title": "La moto policial que persigue a un auto",
        "statement": (
            "Un auto cruza un semáforo en rojo a 72 km/h y sigue a esa velocidad constante por una avenida recta. En "
            "el instante en que pasa, un motociclista de la policía que estaba detenido junto al semáforo arranca "
            "tras él con una aceleración constante de 2.5 m/s² hasta alcanzar los 108 km/h; a partir de ese momento "
            "mantiene esa velocidad."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué distancia separa al auto de la moto en el instante en que la moto llega a 108 km/h? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": "m"},
                "answer": "60 m",
            },
            {
                "prompt": "b) ¿Cuánto tiempo después de que el auto pasó el semáforo la moto lo alcanza? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 18, "tolerance": 0, "unit": "s"},
                "answer": "18 s",
            },
            {
                "prompt": "c) ¿A qué distancia del semáforo lo alcanza? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 360, "tolerance": 0, "unit": "m"},
                "answer": "360 m",
            },
        ],
        "hints": [
            "Pasá las velocidades a m/s. El movimiento de la moto tiene dos etapas: un MRUV desde el reposo hasta 30 m/s y después un MRU.",
            "Calculá cuánto dura la etapa de aceleración y dónde están la moto y el auto cuando termina. ¿Ya lo alcanzó?",
            "A partir de ahí son dos MRU en el mismo sentido: la separación se achica con la diferencia de velocidades.",
        ],
        "solution": [
            "Unidades: `72 ÷ 3.6 = 20 m/s` (auto) y `108 ÷ 3.6 = 30 m/s` (velocidad máxima de la moto). Origen en el semáforo, positivo en el sentido de avance, `t = 0` cuando pasa el auto.",
            "Etapa de aceleración de la moto: `30 = 0 + 2.5 · t₁` → `t₁ = 12 s`. En ese tiempo recorre `x_M = ½ · 2.5 · 12² = 1.25 · 144 = 180 m`.",
            "En esos mismos 12 s el auto (MRU) llega a `x_A = 20 · 12 = 240 m`. Separación: `240 − 180 = 60 m`. La moto todavía no lo alcanzó.",
            "Segunda etapa: los dos van a velocidad constante, la moto a 30 m/s y el auto a 20 m/s. Con `t'` el tiempo desde los 12 s: `180 + 30 · t' = 240 + 20 · t'` → `10 · t' = 60` → `t' = 6 s`.",
            "Tiempo total: `12 + 6 = 18 s`.",
            "Posición del alcance: auto, `20 · 18 = 360 m`. Verificación con la moto: `180 + 30 · 6 = 360 m`.",
            "Respuestas: 60 m, 18 s y 360 m. El error típico es igualar `20 · t = ½ · 2.5 · t²`, que da `t = 16 s`: esa ecuación supone que la moto sigue acelerando, pero dejó de hacerlo a los 12 s (a los 16 s iría a 40 m/s, más que su máxima). Por eso hay que partir el problema en dos etapas.",
        ],
    },
    # ==================== CAÍDA LIBRE Y TIRO VERTICAL ====================
    {
        "id": "f-caida-libre-tiro-vertical-1",
        "node": "f-caida-libre-tiro-vertical",
        "kind": "problem",
        "level": 1,
        "title": "Una piedra desde el puente",
        "statement": (
            "Desde la baranda de un puente sobre un río de montaña, en Mendoza, soltás una piedra (sin velocidad "
            "inicial) y la ves tocar el agua 4 s después. Despreciá el rozamiento del aire y usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿A qué altura sobre el agua está la baranda? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 80, "tolerance": 0, "unit": "m"},
                "answer": "80 m",
            },
            {
                "prompt": "b) ¿Con qué rapidez llega la piedra al agua? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 40, "tolerance": 0, "unit": "m/s"},
                "answer": "40 m/s",
            },
            {
                "prompt": "c) ¿Cuántos metros cae durante el último segundo de la caída? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 35, "tolerance": 0, "unit": "m"},
                "answer": "35 m",
            },
        ],
        "hints": [
            "Parte del reposo: con el eje hacia abajo, `h = ½ · g · t²` y `v = g · t`.",
            "El último segundo va de t = 3 s a t = 4 s: calculá cuánto había caído a los 3 s y restalo del total.",
        ],
        "solution": [
            "Eje positivo hacia abajo con origen en la baranda y `v₀ = 0`: la distancia caída es `h = ½ · g · t²` y la velocidad es `v = g · t`.",
            "Altura del puente: `h = ½ · 10 · 4² = 5 · 16 = 80 m`.",
            "Rapidez al llegar: `v = 10 · 4 = 40 m/s` (144 km/h). Verificación sin el tiempo: `√(2 · g · h) = √(2 · 10 · 80) = √1600 = 40 m/s`.",
            "Último segundo: a los 3 s había caído `½ · 10 · 3² = 45 m`.",
            "Entre t = 3 s y t = 4 s cae `80 − 45 = 35 m`.",
            "Respuestas: 80 m, 40 m/s y 35 m. El error típico es repartir la caída en partes iguales (`80 / 4 = 20 m` por segundo): como el movimiento es acelerado, cae 5 m, 15 m, 25 m y 35 m en cada segundo sucesivo.",
        ],
    },
    {
        "id": "f-caida-libre-tiro-vertical-2",
        "node": "f-caida-libre-tiro-vertical",
        "kind": "problem",
        "level": 2,
        "title": "Una bengala lanzada desde el acantilado",
        "statement": (
            "Desde el borde de un acantilado, a 35 m sobre el mar, se dispara una bengala verticalmente hacia arriba "
            "a 30 m/s. En la bajada pasa junto al borde y cae al mar. Despreciá el rozamiento del aire y usá "
            "g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué altura máxima alcanza la bengala, medida desde el nivel del mar? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 80, "tolerance": 0, "unit": "m"},
                "answer": "80 m",
            },
            {
                "prompt": "b) ¿Cuánto tiempo pasa desde el disparo hasta que llega al mar? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": "s"},
                "answer": "7 s",
            },
            {
                "prompt": "c) ¿Con qué rapidez llega al mar? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 40, "tolerance": 0, "unit": "m/s"},
                "answer": "40 m/s",
            },
        ],
        "hints": [
            "Tomá el eje y hacia arriba con el origen en el nivel del mar: `y₀ = 35 m`, `v₀ = +30 m/s` y `a = −10 m/s²` durante todo el vuelo.",
            "La altura máxima se alcanza cuando `v = 0`; no te olvides de sumar los 35 m del acantilado.",
            "Llegar al mar es `y = 0`: queda una ecuación cuadrática en t. Quedate con la solución positiva.",
        ],
        "solution": [
            "Eje y hacia arriba, origen en el nivel del mar: `y = 35 + 30 · t − 5 · t²` y `v = 30 − 10 · t`.",
            "Punto más alto: `v = 0` → `t = 30 / 10 = 3 s`. Altura: `y = 35 + 30 · 3 − 5 · 3² = 35 + 90 − 45 = 80 m` (sube `30² / (2 · 10) = 45 m` por encima del borde).",
            "Llegada al mar: `y = 0` → `35 + 30 · t − 5 · t² = 0`. Dividiendo por −5: `t² − 6 · t − 7 = 0`.",
            "Resolvente: `t = (6 ± √(36 + 28)) / 2 = (6 ± 8) / 2` → `t = 7 s` o `t = −1 s`. El tiempo negativo no tiene sentido físico: `t = 7 s`.",
            "Velocidad al llegar: `v = 30 − 10 · 7 = −40 m/s`; la rapidez es 40 m/s (el signo indica que va hacia abajo).",
            "Verificación: desde la altura máxima es una caída libre de 80 m: `v = √(2 · 10 · 80) = 40 m/s` y tarda `√(2 · 80 / 10) = 4 s`, que sumados a los 3 s de subida dan 7 s.",
            "Respuestas: 80 m, 7 s y 40 m/s. Errores típicos: dar 45 m como altura máxima (falta la altura del acantilado) o cambiarle el signo a g en la bajada.",
        ],
    },
    {
        "id": "f-caida-libre-tiro-vertical-3",
        "node": "f-caida-libre-tiro-vertical",
        "kind": "problem",
        "level": 2,
        "title": "Dos veces por la misma altura",
        "statement": (
            "En una prueba, una máquina lanza una pelota de tenis verticalmente hacia arriba, desde el nivel del "
            "piso, a 35 m/s. Un dron filma quieto a 50 m de altura, al costado de la trayectoria. Despreciá el "
            "rozamiento del aire y usá g = 10 m/s². Tomá el eje y hacia arriba con origen en el piso."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto tiempo después del lanzamiento pasa la pelota por primera vez a la altura del dron? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "s"},
                "answer": "2 s",
            },
            {
                "prompt": "b) ¿Cuánto tiempo después del lanzamiento vuelve a pasar a la altura del dron? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "s"},
                "answer": "5 s",
            },
            {
                "prompt": "c) ¿Cuál es la velocidad de la pelota en esa segunda pasada? Respondé solo con el número en m/s, con su signo.",
                "check": {"type": "numeric", "value": -15, "tolerance": 0, "unit": "m/s"},
                "answer": "−15 m/s",
            },
        ],
        "hints": [
            "Escribí `y = v₀ · t − ½ · g · t²` y pedí que valga 50 m: queda una ecuación cuadrática en t.",
            "Las dos soluciones tienen sentido físico: una corresponde a la subida y la otra a la bajada.",
            "Para la velocidad usá `v = v₀ − g · t` con el instante de la segunda pasada.",
        ],
        "solution": [
            "Ecuaciones con el eje hacia arriba: `y = 35 · t − 5 · t²` y `v = 35 − 10 · t`.",
            "Antes de seguir, ¿llega a los 50 m? Altura máxima: `35² / (2 · 10) = 1225 / 20 = 61.25 m`. Sí: pasa por los 50 m al subir y al bajar.",
            "Condición `y = 50`: `35 · t − 5 · t² = 50`. Dividiendo por 5 y ordenando: `t² − 7 · t + 10 = 0`.",
            "Resolvente: `t = (7 ± √(49 − 40)) / 2 = (7 ± 3) / 2` → `t = 2 s` (subiendo) y `t = 5 s` (bajando).",
            "Velocidad en la segunda pasada: `v = 35 − 10 · 5 = −15 m/s` (negativa: está bajando). En la primera era `35 − 10 · 2 = +15 m/s`.",
            "Respuestas: 2 s, 5 s y −15 m/s. Se ve la simetría del tiro vertical: a una misma altura la rapidez es la misma al subir y al bajar, y los dos instantes quedan a igual distancia del instante de la cima (3.5 s). El error típico es descartar una de las dos soluciones de la cuadrática.",
        ],
    },
    {
        "id": "f-caida-libre-tiro-vertical-4",
        "node": "f-caida-libre-tiro-vertical",
        "kind": "problem",
        "level": 3,
        "title": "Una piedra que cae y otra que sube",
        "statement": (
            "Desde la terraza de un edificio, a 105 m del suelo, se deja caer una piedra A (sin velocidad inicial). "
            "Un segundo después se lanza desde el suelo, verticalmente hacia arriba y por una vertical muy próxima, "
            "una piedra B a 40 m/s. Despreciá el rozamiento del aire y usá g = 10 m/s². Tomá el eje y hacia arriba "
            "con origen en el suelo y `t = 0` en el instante en que se suelta A."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto tiempo después de soltar A las dos piedras se cruzan (pasan por la misma altura)? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": "s"},
                "answer": "3 s",
            },
            {
                "prompt": "b) ¿A qué altura del suelo se cruzan? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": "m"},
                "answer": "60 m",
            },
            {
                "prompt": "c) ¿Cuál es la velocidad de la piedra B en el instante del cruce? Respondé solo con el número en m/s, con su signo.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "m/s"},
                "answer": "20 m/s (positiva: todavía está subiendo)",
            },
        ],
        "hints": [
            "Es un problema de encuentro, pero vertical: un solo eje y un solo reloj para las dos piedras, e igualar las posiciones.",
            "B sale 1 s después: cuando el reloj marca `t`, B lleva `t − 1` segundos de vuelo. Usá `(t − 1)` en todas sus ecuaciones.",
            "Al igualar `y_A = y_B` los términos con t² se cancelan (las dos tienen la misma aceleración) y queda una ecuación lineal.",
        ],
        "solution": [
            "Piedra A (se suelta en `t = 0` desde `y₀ = 105 m`): `y_A = 105 − 5 · t²`.",
            "Piedra B (sale del suelo en `t = 1 s` a 40 m/s): `y_B = 40 · (t − 1) − 5 · (t − 1)²`, válida para `t ≥ 1 s`.",
            "Desarrollá `y_B`: `40 · t − 40 − 5 · (t² − 2 · t + 1) = −5 · t² + 50 · t − 45`.",
            "Cruce: `105 − 5 · t² = −5 · t² + 50 · t − 45` → `105 = 50 · t − 45` → `50 · t = 150` → `t = 3 s`.",
            "Altura: `y_A = 105 − 5 · 3² = 105 − 45 = 60 m`. Verificación con B (2 s de vuelo): `y_B = 40 · 2 − 5 · 2² = 80 − 20 = 60 m`.",
            "Velocidad de B: `v_B = 40 − 10 · (t − 1) = 40 − 10 · 2 = +20 m/s`. Es positiva: B todavía sube (llegaría a su cima a los 4 s de vuelo). A, en cambio, baja a `v_A = −10 · 3 = −30 m/s`.",
            "Respuestas: 3 s, 60 m y +20 m/s. El error típico es usar el mismo tiempo de vuelo para las dos piedras: `105 − 5 · t² = 40 · t − 5 · t²` da `t = 2.625 s`, que ignora que B salió un segundo más tarde.",
        ],
    },
    # ==================== TIRO OBLICUO ====================
    {
        "id": "f-tiro-oblicuo-1",
        "node": "f-tiro-oblicuo",
        "kind": "problem",
        "level": 1,
        "title": "Saque de arco",
        "statement": (
            "Un arquero saca desde el piso: la pelota sale a 25 m/s con un ángulo de 53° sobre la horizontal "
            "(sen 53° = 0.8 y cos 53° = 0.6) y vuelve a picar en la cancha, que es horizontal. Despreciá el "
            "rozamiento del aire y usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto tiempo está la pelota en el aire? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "s"},
                "answer": "4 s",
            },
            {
                "prompt": "b) ¿Qué altura máxima alcanza? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "m"},
                "answer": "20 m",
            },
            {
                "prompt": "c) ¿A qué distancia del arquero pica? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": "m"},
                "answer": "60 m",
            },
        ],
        "hints": [
            "Primero descomponé la velocidad inicial: `v₀x = v₀ · cos θ` y `v₀y = v₀ · sen θ`.",
            "El tiempo de vuelo y la altura máxima dependen solo de `v₀y`; el avance horizontal, de `v₀x` y del tiempo de vuelo.",
        ],
        "solution": [
            "Componentes de la velocidad inicial: `v₀x = 25 · cos 53° = 25 · 0.6 = 15 m/s` y `v₀y = 25 · sen 53° = 25 · 0.8 = 20 m/s`.",
            "Vertical: sube hasta que `vy = 0`: `t_subida = v₀y / g = 20 / 10 = 2 s`. Como vuelve al mismo nivel, baja en el mismo tiempo: `t_vuelo = 2 · 2 = 4 s`.",
            "Altura máxima: `h_max = v₀y² / (2 · g) = 20² / 20 = 20 m`.",
            "Horizontal (MRU): `alcance = v₀x · t_vuelo = 15 · 4 = 60 m`.",
            "Respuestas: 4 s, 20 m y 60 m. El error típico es meter los 25 m/s completos en las fórmulas verticales: daría 5 s de vuelo y 31.25 m de altura, que corresponden a un tiro vertical.",
        ],
    },
    {
        "id": "f-tiro-oblicuo-2",
        "node": "f-tiro-oblicuo",
        "kind": "problem",
        "level": 2,
        "title": "Víveres desde una avioneta",
        "statement": (
            "Durante una inundación en el Litoral, una avioneta vuela horizontalmente a 40 m/s, a 45 m de altura "
            "sobre el agua, y suelta un paquete de víveres que tiene que caer junto a un bote detenido. Despreciá el "
            "rozamiento del aire y usá g = 10 m/s². Datos: tg 37° = 0.75 y tg 53° ≈ 1.33."
        ),
        "parts": [
            {
                "prompt": "a) ¿A qué distancia horizontal del bote, antes de pasar sobre él, tiene que soltar el paquete? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 120, "tolerance": 0, "unit": "m"},
                "answer": "120 m",
            },
            {
                "prompt": "b) ¿Con qué rapidez llega el paquete al agua? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 50, "tolerance": 0, "unit": "m/s"},
                "answer": "50 m/s",
            },
            {
                "prompt": "c) ¿Qué ángulo forma la velocidad del paquete con la horizontal en el instante en que toca el agua? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 37, "tolerance": 0.005, "unit": "°"},
                "answer": "37° (por debajo de la horizontal)",
            },
        ],
        "hints": [
            "Al soltarlo, el paquete tiene la misma velocidad que la avioneta: 40 m/s horizontales y nada de velocidad vertical. Es un tiro horizontal.",
            "El tiempo de caída sale solo del movimiento vertical: `h = ½ · g · t²`. Con ese tiempo calculá el avance horizontal.",
            "Al llegar, la velocidad tiene dos componentes: `vx` (la misma del principio) y `vy = g · t`. Módulo por Pitágoras y ángulo con la tangente.",
        ],
        "solution": [
            "Velocidad inicial del paquete: la de la avioneta, `v₀x = 40 m/s` y `v₀y = 0`. Es un tiro horizontal desde 45 m.",
            "Vertical (caída desde el reposo): `45 = ½ · 10 · t²` → `t² = 9` → `t = 3 s`.",
            "Horizontal (MRU): `x = v₀x · t = 40 · 3 = 120 m`. Hay que soltarlo 120 m antes de pasar sobre el bote.",
            "Velocidad al llegar: `vx = 40 m/s` (no cambia) y `vy = g · t = 10 · 3 = 30 m/s` hacia abajo.",
            "Rapidez: `v = √(40² + 30²) = √(1600 + 900) = √2500 = 50 m/s`.",
            "Ángulo con la horizontal: `tg α = vy / vx = 30 / 40 = 0.75` → `α = 37°` por debajo de la horizontal.",
            "Respuestas: 120 m, 50 m/s y 37°. Errores típicos: soltar el paquete justo encima del bote (caería 120 m más adelante) o dar como rapidez final solo una componente (30 o 40 m/s).",
        ],
    },
    {
        "id": "f-tiro-oblicuo-3",
        "node": "f-tiro-oblicuo",
        "kind": "problem",
        "level": 2,
        "title": "Reconstruir el pase a partir del vuelo",
        "statement": (
            "En un partido, un pase largo sale desde el pasto y vuelve a tocar el pasto 2 s después, a 48 m del "
            "punto de partida. La cancha es horizontal. Despreciá el rozamiento del aire y usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la componente horizontal de la velocidad inicial? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 24, "tolerance": 0, "unit": "m/s"},
                "answer": "24 m/s",
            },
            {
                "prompt": "b) ¿Qué altura máxima alcanzó la pelota? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "m"},
                "answer": "5 m",
            },
            {
                "prompt": "c) ¿Con qué rapidez salió la pelota del pie? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 26, "tolerance": 0, "unit": "m/s"},
                "answer": "26 m/s",
            },
        ],
        "hints": [
            "Es el problema de siempre, pero al revés: en horizontal es un MRU, así que el alcance y el tiempo te dan `v₀x`.",
            "En vertical, la pelota tarda la mitad del vuelo en subir. Con el tiempo de subida sale `v₀y`, y con `v₀y` la altura máxima.",
            "La rapidez inicial es el módulo del vector `(v₀x; v₀y)`.",
        ],
        "solution": [
            "Horizontal (MRU): `v₀x = alcance / t_vuelo = 48 / 2 = 24 m/s`.",
            "Vertical: como sale y llega al mismo nivel, sube durante la mitad del vuelo: `t_subida = 1 s`. En la cima `vy = 0`: `0 = v₀y − 10 · 1` → `v₀y = 10 m/s`.",
            "Altura máxima: `h_max = v₀y² / (2 · g) = 10² / 20 = 5 m`. Verificación: `y(1 s) = 10 · 1 − 5 · 1² = 5 m`.",
            "Rapidez inicial: `v₀ = √(v₀x² + v₀y²) = √(24² + 10²) = √(576 + 100) = √676 = 26 m/s`.",
            "Respuestas: 24 m/s, 5 m y 26 m/s. Fue un pase rasante: `tg θ = 10 / 24 ≈ 0.42`, unos 23° sobre la horizontal. El error típico es usar los 2 s completos como tiempo de subida (daría `v₀y = 20 m/s` y 20 m de altura).",
        ],
    },
    {
        "id": "f-tiro-oblicuo-4",
        "node": "f-tiro-oblicuo",
        "kind": "problem",
        "level": 3,
        "title": "Pelotazo desde la terraza por encima de un árbol",
        "statement": (
            "Desde el borde de una terraza, a 20 m del suelo, se patea una pelota a 25 m/s con un ángulo de 37° por "
            "encima de la horizontal (sen 37° = 0.6 y cos 37° = 0.8). En la dirección del tiro, a 40 m de la base del "
            "edificio, hay un eucalipto de 25 m de altura. El terreno es horizontal. Despreciá el rozamiento del "
            "aire y usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿A qué altura sobre el suelo está la pelota cuando pasa por la vertical del eucalipto? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": "m"},
                "answer": "30 m (pasa 5 m por encima de la copa)",
            },
            {
                "prompt": "b) ¿Cuánto tiempo está la pelota en el aire hasta tocar el suelo? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "s"},
                "answer": "4 s",
            },
            {
                "prompt": "c) ¿A qué distancia horizontal de la base del edificio toca el suelo? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 80, "tolerance": 0, "unit": "m"},
                "answer": "80 m",
            },
        ],
        "hints": [
            "Origen en la base del edificio, y hacia arriba: `x = v₀x · t` e `y = 20 + v₀y · t − 5 · t²`. Acá no sirve `t_vuelo = 2 · v₀y / g`, porque no cae al mismo nivel del que salió.",
            "Para el árbol, el dato es horizontal: averiguá en qué instante la pelota está en `x = 40 m` y reemplazá ese tiempo en `y`.",
            "Tocar el suelo es `y = 0`: resolvé la cuadrática y quedate con el tiempo positivo.",
        ],
        "solution": [
            "Componentes: `v₀x = 25 · 0.8 = 20 m/s` y `v₀y = 25 · 0.6 = 15 m/s`. Con origen en la base del edificio: `x = 20 · t` e `y = 20 + 15 · t − 5 · t²`.",
            "Instante en que pasa por el eucalipto: `x = 40` → `20 · t = 40` → `t = 2 s`.",
            "Altura en ese instante: `y = 20 + 15 · 2 − 5 · 2² = 20 + 30 − 20 = 30 m`. El árbol mide 25 m: la pelota pasa 5 m por encima.",
            "Llegada al suelo: `y = 0` → `20 + 15 · t − 5 · t² = 0`. Dividiendo por −5: `t² − 3 · t − 4 = 0`.",
            "Resolvente: `t = (3 ± √(9 + 16)) / 2 = (3 ± 5) / 2` → `t = 4 s` (la otra solución, `t = −1 s`, se descarta).",
            "Alcance: `x = 20 · 4 = 80 m` desde la base del edificio.",
            "Respuestas: 30 m, 4 s y 80 m. Dato extra: la cima está a los `15 / 10 = 1.5 s`, a `20 + 15² / 20 = 31.25 m` del suelo, así que sobre el árbol la pelota ya viene bajando. El error típico es usar `t_vuelo = 2 · v₀y / g = 3 s`: ese es el tiempo en volver a la altura de la terraza, no al suelo.",
        ],
    },
    # ==================== MOVIMIENTO CIRCULAR UNIFORME ====================
    {
        "id": "f-mcu-1",
        "node": "f-mcu",
        "kind": "problem",
        "level": 1,
        "title": "El ventilador del galpón",
        "statement": (
            "El ventilador de techo de un galpón gira a 300 rpm con movimiento circular uniforme. Cada aspa mide "
            "0.5 m desde el eje hasta la punta."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es su frecuencia? Respondé solo con el número en Hz.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "Hz"},
                "answer": "5 Hz",
            },
            {
                "prompt": "b) ¿Cuál es su período? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 0.2, "tolerance": 0, "unit": "s"},
                "answer": "0.2 s",
            },
            {
                "prompt": "c) ¿Con qué velocidad tangencial se mueve la punta de un aspa? Usá π ≈ 3.14 y redondeá a 1 decimal. Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 15.7, "tolerance": 0.005, "unit": "m/s"},
                "answer": "15.7 m/s",
            },
        ],
        "hints": [
            "rpm son vueltas por minuto: para pasar a vueltas por segundo (Hz) dividí por 60. El período es el inverso de la frecuencia.",
            "En una vuelta la punta recorre una circunferencia de radio 0.5 m: `v = 2π · r / T`, o lo que es lo mismo, `v = ω · r` con `ω = 2π · f`.",
        ],
        "solution": [
            "Frecuencia: `f = 300 vueltas / 60 s = 5 Hz`.",
            "Período: `T = 1 / f = 1 / 5 = 0.2 s` por vuelta.",
            "Velocidad angular: `ω = 2π · f = 2π · 5 = 10π rad/s`.",
            "Velocidad tangencial de la punta: `v = ω · r = 10π · 0.5 = 5π ≈ 5 · 3.14 = 15.7 m/s`.",
            "Respuestas: 5 Hz, 0.2 s y 15.7 m/s (unos 57 km/h). El error típico es meter las rpm directamente en `ω = 2π · f`: daría `600π rad/s`, 60 veces más.",
        ],
    },
    {
        "id": "f-mcu-2",
        "node": "f-mcu",
        "kind": "problem",
        "level": 2,
        "title": "Una rotonda a 36 km/h",
        "statement": (
            "Un auto recorre una rotonda de 50 m de radio a 36 km/h constantes (movimiento circular uniforme)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale su aceleración centrípeta? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "m/s²"},
                "answer": "2 m/s²",
            },
            {
                "prompt": "b) ¿Cuál es su velocidad angular? Respondé solo con el número en rad/s.",
                "check": {"type": "numeric", "value": 0.2, "tolerance": 0, "unit": "rad/s"},
                "answer": "0.2 rad/s",
            },
            {
                "prompt": "c) ¿Cuánto tardaría en dar una vuelta completa a la rotonda? Usá π ≈ 3.14 y redondeá a 1 decimal. Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 31.4, "tolerance": 0.005, "unit": "s"},
                "answer": "31.4 s",
            },
        ],
        "hints": [
            "Antes que nada pasá la velocidad a m/s: el radio está en metros.",
            "Con la velocidad tangencial y el radio: `a_c = v² / r` y `ω = v / r`.",
            "El tiempo de una vuelta es el período: `T = 2π / ω` (o la longitud de la circunferencia dividida por la velocidad).",
        ],
        "solution": [
            "Unidades: `v = 36 ÷ 3.6 = 10 m/s`.",
            "Aceleración centrípeta: `a_c = v² / r = 10² / 50 = 100 / 50 = 2 m/s²`, dirigida hacia el centro de la rotonda.",
            "Velocidad angular: de `v = ω · r`, `ω = v / r = 10 / 50 = 0.2 rad/s`. Verificación: `ω² · r = 0.04 · 50 = 2 m/s²`.",
            "Período: `T = 2π / ω = 2 · 3.14 / 0.2 = 6.28 / 0.2 = 31.4 s`.",
            "Verificación por otro camino: la circunferencia mide `2π · r = 2 · 3.14 · 50 = 314 m`, y a 10 m/s se recorre en `314 / 10 = 31.4 s`.",
            "Respuestas: 2 m/s², 0.2 rad/s y 31.4 s. El error típico es usar 36 sin convertir: `36² / 50 ≈ 26 m/s²`, más de dos veces y media la aceleración de la gravedad, imposible para un auto en una rotonda.",
        ],
    },
    {
        "id": "f-mcu-3",
        "node": "f-mcu",
        "kind": "problem",
        "level": 2,
        "title": "Motor, correa y sierra circular",
        "statement": (
            "En una carpintería, un motor eléctrico gira a 1800 rpm y tiene en su eje una polea de 4 cm de radio. Una "
            "correa que no desliza la une con otra polea de 12 cm de radio, montada en el mismo eje que una sierra "
            "circular de 15 cm de radio: la polea grande y la sierra giran juntas, como un único cuerpo rígido."
        ),
        "parts": [
            {
                "prompt": "a) ¿A cuántas vueltas por minuto gira la sierra? Respondé solo con el número en rpm.",
                "check": {"type": "numeric", "value": 600, "tolerance": 0, "unit": "rpm"},
                "answer": "600 rpm",
            },
            {
                "prompt": "b) ¿Con qué velocidad avanza la correa? Usá π ≈ 3.14 y redondeá a 2 decimales. Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 7.54, "tolerance": 0.005, "unit": "m/s"},
                "answer": "7.54 m/s",
            },
            {
                "prompt": "c) ¿Qué velocidad tangencial tienen los dientes de la sierra? Usá π ≈ 3.14 y redondeá a 2 decimales. Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 9.42, "tolerance": 0.005, "unit": "m/s"},
                "answer": "9.42 m/s",
            },
        ],
        "hints": [
            "Identificá qué comparte cada par: las dos poleas unidas por la correa tienen la misma velocidad en el borde; la polea grande y la sierra, al estar en el mismo eje, tienen la misma velocidad angular.",
            "Misma `v` en el borde: `f₁ · r₁ = f₂ · r₂`. La polea de mayor radio gira más lento.",
            "Para las velocidades tangenciales pasá las rpm a Hz, los radios a metros, y usá `v = ω · r = 2π · f · r`.",
        ],
        "solution": [
            "Poleas unidas por la correa: misma velocidad tangencial en el borde, `ω₁ · r₁ = ω₂ · r₂`, que equivale a `f₁ · r₁ = f₂ · r₂`. Entonces `f₂ = 1800 · 4 / 12 = 600 rpm`.",
            "La sierra está montada en el mismo eje que la polea grande (mismo cuerpo rígido, misma ω): también gira a 600 rpm.",
            "Velocidad de la correa: es la del borde de la polea del motor. `f₁ = 1800 / 60 = 30 Hz`, `ω₁ = 2π · 30 = 60π rad/s` y `r₁ = 0.04 m`: `v = ω₁ · r₁ = 60π · 0.04 = 2.4π ≈ 2.4 · 3.14 = 7.536 ≈ 7.54 m/s`.",
            "Verificación con la polea grande: `f₂ = 600 / 60 = 10 Hz`, `ω₂ = 20π rad/s`, `v = 20π · 0.12 = 2.4π`. Coincide, como tiene que ser.",
            "Dientes de la sierra: misma `ω₂ = 20π rad/s`, radio `0.15 m`: `v = 20π · 0.15 = 3π ≈ 3 · 3.14 = 9.42 m/s`.",
            "Respuestas: 600 rpm, 7.54 m/s y 9.42 m/s. Los dientes van más rápido que la correa aunque giran con la misma ω que la polea grande, porque están más lejos del eje (15 cm contra 12 cm). El error típico es invertir la proporción y hacer girar la polea grande a `1800 · 12 / 4 = 5400 rpm`.",
        ],
    },
    {
        "id": "f-mcu-4",
        "node": "f-mcu",
        "kind": "problem",
        "level": 3,
        "title": "La boleadora que se suelta",
        "statement": (
            "Un gaucho revolea una boleadora sobre su cabeza. Modelá el movimiento de la bola como un movimiento "
            "circular uniforme en un plano horizontal, a 1.8 m del suelo, con un radio de 0.8 m. Al soltarla, la "
            "bola sale con la velocidad que tenía en ese instante (horizontal y tangente a la circunferencia) y "
            "toca el suelo, que es horizontal, a 12 m de distancia horizontal del punto donde fue soltada. "
            "Despreciá el rozamiento del aire y usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿Con qué rapidez se movía la bola mientras giraba? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "m/s"},
                "answer": "20 m/s",
            },
            {
                "prompt": "b) ¿Cuál era su velocidad angular? Respondé solo con el número en rad/s.",
                "check": {"type": "numeric", "value": 25, "tolerance": 0, "unit": "rad/s"},
                "answer": "25 rad/s",
            },
            {
                "prompt": "c) ¿Cuánto valía su aceleración centrípeta mientras giraba? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 500, "tolerance": 0, "unit": "m/s²"},
                "answer": "500 m/s²",
            },
        ],
        "hints": [
            "Empezá por el final: después de soltarla, la bola hace un tiro horizontal desde 1.8 m de altura. El tiempo de caída sale de `h = ½ · g · t²`.",
            "Con ese tiempo y los 12 m de avance horizontal obtenés la velocidad de salida, que es la velocidad tangencial del giro.",
            "Con `v` y el radio: `ω = v / r` y `a_c = v² / r`.",
        ],
        "solution": [
            "Después de soltarla, la bola es un proyectil con velocidad inicial horizontal (tiro horizontal) desde `h = 1.8 m`. Vertical: `1.8 = ½ · 10 · t²` → `t² = 0.36` → `t = 0.6 s`.",
            "Horizontal (MRU): `v = x / t = 12 / 0.6 = 20 m/s`. Esa velocidad de salida es la velocidad tangencial que tenía la bola mientras giraba.",
            "Velocidad angular: `ω = v / r = 20 / 0.8 = 25 rad/s` (unas 4 vueltas por segundo, porque `f = ω / 2π ≈ 3.98 Hz`).",
            "Aceleración centrípeta: `a_c = v² / r = 20² / 0.8 = 400 / 0.8 = 500 m/s²`. Verificación: `ω² · r = 25² · 0.8 = 625 · 0.8 = 500 m/s²`.",
            "Respuestas: 20 m/s (72 km/h), 25 rad/s y 500 m/s², unas 50 veces g: por eso hay que sostener la soga con tanta fuerza. Error típico: pensar que al soltarla la bola sale 'hacia afuera' en la dirección del radio; sale por la tangente, con la velocidad que tenía en ese instante.",
        ],
    },
]
