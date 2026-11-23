"""Ejercicios de Matemática: Geometría (ángulos, transformaciones, congruencia, círculos) y
Precálculo (complejos polares, cónicas, vectores, matrices, determinantes, combinatoria, series y
límites).

Tres problemas por tema (niveles 1, 2 y 3). Los de nivel 3 apuntan a la dificultad de un parcial
de ingreso a Ingeniería. No hay imágenes: las figuras se describen en palabras.
"""

from __future__ import annotations

EXERCISES: list[dict] = [
    # ==================== g-angulos-rectas ====================
    {
        "id": "g-angulos-rectas-1",
        "node": "g-angulos-rectas",
        "kind": "problem",
        "level": 1,
        "title": "La reja con forma de polígono regular",
        "statement": (
            "Un herrero arma el marco de una ventana con forma de **polígono regular** (todos los lados y "
            "todos los ángulos iguales). Con el transportador mide uno de sus ángulos interiores y obtiene "
            "`140°`.\n\n"
            "Querés saber cuántos lados tiene el marco y cuánto suman todos sus ángulos interiores."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuántos lados tiene el polígono? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": ""},
                "answer": "9 lados (ángulo exterior 40° y 360° ÷ 40° = 9)",
            },
            {
                "prompt": "b) ¿Cuánto suman sus ángulos interiores? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 1260, "tolerance": 0, "unit": "°"},
                "answer": "1260° ((9 − 2) · 180°)",
            },
        ],
        "hints": [
            "En cada vértice, el ángulo interior y el exterior están sobre una misma recta: son suplementarios.",
            "Si recorrés el contorno de cualquier polígono convexo, los ángulos exteriores suman una vuelta completa (`360°`).",
        ],
        "solution": [
            "En cada vértice, el ángulo exterior es el suplemento del interior: `180° − 140° = 40°`.",
            "Los ángulos exteriores de un polígono convexo suman `360°` y en un polígono regular son todos iguales, así que `n = 360° ÷ 40° = 9` lados (un **eneágono**).",
            "Suma de ángulos interiores: `(n − 2) · 180° = 7 · 180° = 1260°`.",
            "Verificación: `1260° ÷ 9 = 140°`, que es justamente el ángulo medido.",
            "Otra forma: plantear `(n − 2) · 180 / n = 140` → `180n − 360 = 140n` → `40n = 360` → `n = 9`.",
            "Error típico: dividir `360°` por el ángulo interior (`360 ÷ 140`), que no da un número entero de lados.",
        ],
    },
    {
        "id": "g-angulos-rectas-2",
        "node": "g-angulos-rectas",
        "kind": "problem",
        "level": 2,
        "title": "Ángulos con incógnita entre dos paralelas",
        "statement": (
            "Las rectas `r` y `s` son **paralelas** y la transversal `t` las corta en el punto `A` (sobre `r`) "
            "y en el punto `B` (sobre `s`).\n\n"
            "El ángulo `α`, con vértice en `A`, y el ángulo `β`, con vértice en `B`, están los dos **entre las "
            "paralelas** y **del mismo lado** de `t` (son conjugados internos). Se sabe que "
            "`α = 3x + 10°` y `β = 2x + 20°`.\n\n"
            "Llamá `γ` al ángulo con vértice en `B` que también está entre las paralelas pero **del otro lado** "
            "de `t` (es adyacente a `β`)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale x? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": "°"},
                "answer": "30° (5x + 30° = 180°)",
            },
            {
                "prompt": "b) ¿Cuánto mide γ? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 100, "tolerance": 0, "unit": "°"},
                "answer": "100° (β = 80° y γ = 180° − 80°)",
            },
            {
                "prompt": "c) ¿Qué relación hay entre α y γ?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Son alternos internos, por lo tanto iguales",
                        "Son conjugados internos, por lo tanto suman 180°",
                        "Son opuestos por el vértice, por lo tanto iguales",
                        "Son complementarios, por lo tanto suman 90°",
                    ],
                    "correct": 0,
                },
                "answer": "Son alternos internos, por lo tanto iguales",
            },
        ],
        "hints": [
            "Dos ángulos entre paralelas y del mismo lado de la transversal no son iguales: forman un «C» y suman `180°`.",
            "β y γ comparten el vértice B y juntos forman un ángulo llano.",
        ],
        "solution": [
            "Los conjugados internos (entre las paralelas y del mismo lado de `t`) son suplementarios: `α + β = 180°`.",
            "Reemplazando: `(3x + 10°) + (2x + 20°) = 180°` → `5x + 30° = 180°` → `5x = 150°` → `x = 30°`.",
            "Entonces `α = 3·30° + 10° = 100°` y `β = 2·30° + 20° = 80°` (verificación: `100° + 80° = 180°`).",
            "`β` y `γ` son adyacentes sobre la recta `s`, así que `γ = 180° − 80° = 100°`.",
            "`α` (en `A`) y `γ` (en `B`) están entre las paralelas y en lados opuestos de `t`: forman la «Z» de los **alternos internos**, que son iguales. Coincide: `α = γ = 100°`.",
            "Error típico: igualar `3x + 10 = 2x + 20` (daría `x = 10°`) como si fueran alternos; los conjugados internos no son iguales sino suplementarios.",
        ],
    },
    {
        "id": "g-angulos-rectas-3",
        "node": "g-angulos-rectas",
        "kind": "problem",
        "level": 3,
        "title": "El zigzag entre dos paralelas",
        "statement": (
            "Las rectas `r` y `s` son paralelas y horizontales, con `r` arriba. Sobre `r` están el punto `A` y, "
            "a su derecha, el punto `C`. Sobre `s` están el punto `B` y, a su derecha, el punto `D`. Un punto "
            "`P` está **entre las dos rectas** y **a la derecha de A y de B**, de modo que la poligonal "
            "`A → P → B` forma una punta que apunta hacia la derecha.\n\n"
            "Se sabe que `∠CAP = 2x + 5°`, `∠DBP = 3x` y que el ángulo convexo `∠APB` (el que se abre hacia "
            "la izquierda) mide `6x − 10°`.\n\n"
            "Además, la recta `AP` prolongada más allá de `P` corta a `s` en el punto `Q`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale x? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": "°"},
                "answer": "15° (2x + 5 + 3x = 6x − 10)",
            },
            {
                "prompt": "b) ¿Cuánto mide ∠APB? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 80, "tolerance": 0, "unit": "°"},
                "answer": "80° (35° + 45°)",
            },
            {
                "prompt": "c) ¿Cuánto mide el ángulo ∠BPQ del triángulo BPQ? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 100, "tolerance": 0, "unit": "°"},
                "answer": "100° (suplemento de ∠APB)",
            },
        ],
        "hints": [
            "Trazá por `P` una recta paralela a `r` y a `s`: parte el ángulo `∠APB` en dos pedazos.",
            "Cada pedazo es alterno interno con uno de los ángulos dados (uno con el de `A`, otro con el de `B`).",
            "Con eso, `∠APB` es igual a la suma de los otros dos: plantealo como ecuación en `x`.",
        ],
        "solution": [
            "Por `P` trazamos la recta `m` paralela a `r` y `s`. Esa recta divide `∠APB` en dos ángulos: uno con lado `PA` y otro con lado `PB`.",
            "El ángulo entre `PA` y `m` es alterno interno con `∠CAP` (paralelas `r` y `m`, transversal `AP`); el ángulo entre `PB` y `m` es alterno interno con `∠DBP` (paralelas `s` y `m`, transversal `BP`). Entonces `∠APB = ∠CAP + ∠DBP`.",
            "Ecuación: `6x − 10 = (2x + 5) + 3x` → `6x − 10 = 5x + 5` → `x = 15°`.",
            "Ángulos: `∠CAP = 35°`, `∠DBP = 45°` y `∠APB = 6·15° − 10° = 80°` (verificación: `35° + 45° = 80°`).",
            "Triángulo `BPQ`: `A`, `P` y `Q` están alineados, así que `∠BPQ = 180° − ∠APB = 180° − 80° = 100°`.",
            "Comprobación con el triángulo: `∠PQB = ∠CAP = 35°` (alternos internos entre `r` y `s` con transversal `AQ`) y `∠PBQ = ∠DBP = 45°`; la suma da `35° + 45° + 100° = 180°`. ✔",
            "Error típico: suponer que `∠APB` es el suplemento de la suma (`180° − 80°`); ese es el ángulo `∠BPQ`, no el de la punta del zigzag.",
        ],
    },
    # ==================== g-transformaciones ====================
    {
        "id": "g-transformaciones-1",
        "node": "g-transformaciones",
        "kind": "problem",
        "level": 1,
        "title": "Girar y después espejar un triángulo",
        "statement": (
            "En un programa de diseño tenés el triángulo de vértices `A(1, 2)`, `B(4, 2)` y `C(4, 6)`.\n\n"
            "Primero lo **rotás 90° en sentido antihorario alrededor del origen** y, a la figura obtenida, la "
            "**reflejás sobre el eje X**. Llamá `A''`, `B''` y `C''` a los vértices finales."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la coordenada x de C''? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -6, "tolerance": 0, "unit": ""},
                "answer": "−6 (C'' = (−6, −4))",
            },
            {
                "prompt": "b) ¿Cuál es la coordenada y de C''? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -4, "tolerance": 0, "unit": ""},
                "answer": "−4 (C'' = (−6, −4))",
            },
            {
                "prompt": "c) ¿Qué transformación única produce el mismo resultado que las dos aplicadas en ese orden?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Una reflexión sobre la recta y = −x",
                        "Una reflexión sobre la recta y = x",
                        "Una rotación de 90° en sentido horario alrededor del origen",
                        "Una rotación de 180° alrededor del origen",
                    ],
                    "correct": 0,
                },
                "answer": "Una reflexión sobre la recta y = −x",
            },
        ],
        "hints": [
            "Rotar 90° antihorario: `(x, y) → (−y, x)`. Reflejar sobre el eje X: `(x, y) → (x, −y)`.",
            "Aplicá las dos reglas en orden a un punto genérico `(x, y)` y mirá qué fórmula queda.",
        ],
        "solution": [
            "Rotación de 90° antihoraria: `C(4, 6) → C'(−6, 4)`.",
            "Reflexión sobre el eje X (cambia el signo de `y`): `C'(−6, 4) → C''(−6, −4)`.",
            "Con los otros vértices: `A(1, 2) → (−2, 1) → A''(−2, −1)` y `B(4, 2) → (−2, 4) → B''(−2, −4)`.",
            "Regla compuesta para un punto genérico: `(x, y) → (−y, x) → (−y, −x)`. Intercambiar coordenadas y cambiar ambos signos es la **reflexión sobre la recta y = −x** (los puntos de esa recta, como `(1, −1)`, quedan fijos).",
            "Verificación de que es rígida: el triángulo original tiene lados `AB = 3`, `BC = 4`, `AC = 5`; en la imagen `A''B'' = 3` (vertical), `B''C'' = 4` (horizontal) y `A''C'' = √(4² + 3²) = 5`. Perímetro `12` en ambos.",
            "Error típico: confundir con la rotación horaria `(x, y) → (y, −x)`; probá con `C`: daría `(6, −4)`, no `(−6, −4)`.",
        ],
    },
    {
        "id": "g-transformaciones-2",
        "node": "g-transformaciones",
        "kind": "problem",
        "level": 2,
        "title": "Rotar alrededor de un punto que no es el origen",
        "statement": (
            "Un brazo robótico tiene su eje de giro en el punto `Q(2, 3)` del plano de trabajo (en dm). La pinza "
            "está en `P(5, 1)` y el brazo gira **90° en sentido antihorario alrededor de Q**, llevando la pinza "
            "a `P'`.\n\n"
            "En otra etapa del proceso, una pieza se refleja primero sobre la recta vertical `x = 1` y luego sobre "
            "la recta vertical `x = 4`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la coordenada x de P'? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4 (P' = (4, 6))",
            },
            {
                "prompt": "b) ¿Cuál es la coordenada y de P'? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""},
                "answer": "6 (P' = (4, 6))",
            },
            {
                "prompt": "c) ¿A qué transformación única equivalen las dos reflexiones (primero sobre x = 1, luego sobre x = 4)?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Una traslación de 6 unidades hacia la derecha",
                        "Una traslación de 3 unidades hacia la derecha",
                        "Una traslación de 6 unidades hacia la izquierda",
                        "Una reflexión sobre la recta x = 2.5",
                    ],
                    "correct": 0,
                },
                "answer": "Una traslación de 6 unidades hacia la derecha",
            },
        ],
        "hints": [
            "La regla `(x, y) → (−y, x)` solo vale para rotar alrededor del origen: llevá primero `Q` al origen restando sus coordenadas.",
            "Rotá el vector `P − Q`, y después volvé a sumar `Q`.",
            "Para las reflexiones: reflejar sobre `x = a` lleva `x` a `2a − x` (la `y` no cambia).",
        ],
        "solution": [
            "Vector desde el centro: `P − Q = (5 − 2, 1 − 3) = (3, −2)`.",
            "Lo rotamos 90° antihorario con `(x, y) → (−y, x)`: `(3, −2) → (2, 3)`.",
            "Volvemos a sumar el centro: `P' = (2 + 2, 3 + 3) = (4, 6)`.",
            "Verificación: `|QP| = √(3² + 2²) = √13` y `|QP'| = √(2² + 3²) = √13` (se conserva la distancia al eje), y `(3, −2) · (2, 3) = 6 − 6 = 0` (forman 90°).",
            "Reflexiones: sobre `x = 1`, `x → 2 − x`; luego sobre `x = 4`, `x → 8 − (2 − x) = x + 6`. La `y` no cambia en ninguna, así que la composición es `(x, y) → (x + 6, y)`: **traslación de 6 a la derecha** (el doble de la distancia entre los espejos, en el sentido del primero al segundo).",
            "Error típico: aplicar `(−y, x)` directamente a `P(5, 1)`, que da `(−1, 5)`: esa sería la rotación alrededor del origen, no alrededor de `Q`.",
        ],
    },
    {
        "id": "g-transformaciones-3",
        "node": "g-transformaciones",
        "kind": "problem",
        "level": 3,
        "title": "Reflejar un punto sobre una recta oblicua",
        "statement": (
            "En un programa CAD se quiere obtener el simétrico del punto `P(1, 7)` respecto de la recta "
            "`L: y = (3/4)x` (es decir, el punto `P'` tal que `L` es la mediatriz del segmento `PP'`).\n\n"
            "Llamá `M` al punto de `L` más cercano a `P` (el pie de la perpendicular desde `P`)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la distancia de P a la recta L? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                "answer": "5 (M = (4, 3) y |PM| = √(3² + 4²))",
            },
            {
                "prompt": "b) ¿Cuál es la coordenada x de P'? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": ""},
                "answer": "7 (P' = (7, −1))",
            },
            {
                "prompt": "c) ¿Cuál es la coordenada y de P'? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -1, "tolerance": 0, "unit": ""},
                "answer": "−1 (P' = (7, −1))",
            },
        ],
        "hints": [
            "La recta que pasa por `P` y es perpendicular a `L` tiene pendiente opuesta e inversa a `3/4`.",
            "Cortá esa perpendicular con `L` para obtener `M`. En una reflexión, `M` es el **punto medio** de `P` y `P'`.",
        ],
        "solution": [
            "Pendiente de `L`: `3/4`. La perpendicular por `P(1, 7)` tiene pendiente `−4/3`: `y − 7 = −(4/3)(x − 1)`.",
            "Intersección con `L`: `(3/4)x = 7 − (4/3)(x − 1)`. Multiplicando por 12: `9x = 84 − 16x + 16` → `25x = 100` → `x = 4`, `y = (3/4)·4 = 3`. Entonces `M = (4, 3)`.",
            "Distancia de `P` a `L`: `|PM| = √((4 − 1)² + (3 − 7)²) = √(9 + 16) = 5`.",
            "Como `M` es el punto medio de `PP'`: `P' = 2M − P = (2·4 − 1, 2·3 − 7) = (7, −1)`.",
            "Verificación 1: `M` es el punto medio de `(1, 7)` y `(7, −1)`: `((1 + 7)/2, (7 − 1)/2) = (4, 3)`. ✔",
            "Verificación 2: el origen está sobre `L`, así que debe quedar a igual distancia de `P` y de `P'`: `|OP| = √(1 + 49) = √50` y `|OP'| = √(49 + 1) = √50`. ✔",
            "Error típico: usar la regla del espejo sobre `y = x` (intercambiar coordenadas), que daría `(7, 1)`; esa regla solo vale para la recta de pendiente 1.",
        ],
    },
    # ==================== g-congruencia ====================
    {
        "id": "g-congruencia-1",
        "node": "g-congruencia",
        "kind": "problem",
        "level": 1,
        "title": "El triángulo isósceles del cartel",
        "statement": (
            "Un cartel de chapa tiene forma de triángulo `ABC` con `AB = AC` (isósceles con vértice en `A`). Si "
            "se prolonga el lado `BC` más allá de `C`, el ángulo exterior que se forma en `C` mide `116°`.\n\n"
            "Además, medidos en cm: `AB = 2y + 3`, `AC = 5y − 9` y `BC = y + 6`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto mide el ángulo ∠BAC? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 52, "tolerance": 0, "unit": "°"},
                "answer": "52° (los ángulos de la base miden 64°)",
            },
            {
                "prompt": "b) ¿Cuál es el perímetro del cartel? Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 32, "tolerance": 0, "unit": "cm"},
                "answer": "32 cm (11 + 11 + 10)",
            },
        ],
        "hints": [
            "El ángulo exterior en `C` y el ángulo interior `∠ACB` forman un ángulo llano.",
            "En un isósceles, a lados iguales se oponen ángulos iguales. Y como `AB = AC`, podés igualar las dos expresiones.",
        ],
        "solution": [
            "Ángulo interior en `C`: `∠ACB = 180° − 116° = 64°`.",
            "Como `AB = AC`, los ángulos opuestos a esos lados son iguales: `∠ABC = ∠ACB = 64°`.",
            "Entonces `∠BAC = 180° − 2·64° = 180° − 128° = 52°`.",
            "Lados: `AB = AC` → `2y + 3 = 5y − 9` → `12 = 3y` → `y = 4`. Así `AB = AC = 11 cm` y `BC = 4 + 6 = 10 cm`.",
            "Perímetro: `11 + 11 + 10 = 32 cm`.",
            "Error típico: tomar el ángulo exterior (`116°`) como si fuera el ángulo del vértice `A`, o igualar `BC` con uno de los lados iguales.",
        ],
    },
    {
        "id": "g-congruencia-2",
        "node": "g-congruencia",
        "kind": "problem",
        "level": 2,
        "title": "Diagonales y ángulos de un paralelogramo",
        "statement": (
            "En el paralelogramo `ABCD` (vértices en ese orden), las diagonales `AC` y `BD` se cortan en el "
            "punto `O`. Medido en cm: `AO = 2x + 1` y `OC = 3x − 4`.\n\n"
            "Los ángulos interiores son `∠DAB = 3y + 15°` y `∠ABC = 2y + 15°`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto mide la diagonal AC? Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 22, "tolerance": 0, "unit": "cm"},
                "answer": "22 cm (x = 5, AO = OC = 11)",
            },
            {
                "prompt": "b) ¿Cuánto mide ∠BCD? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 105, "tolerance": 0, "unit": "°"},
                "answer": "105° (opuesto a ∠DAB)",
            },
            {
                "prompt": "c) ¿Cuál de estas justificaciones prueba correctamente que △AOB ≅ △COD?",
                "check": {
                    "type": "choice",
                    "options": [
                        "LAL: AO = OC, ∠AOB = ∠COD (opuestos por el vértice) y OB = OD",
                        "LAL: AO = OC, ∠OAB = ∠OCD y OB = OD",
                        "AAA: los tres ángulos de un triángulo son iguales a los del otro",
                        "LLA: AO = OC, OB = OD y ∠OAB = ∠OCD",
                    ],
                    "correct": 0,
                },
                "answer": "LAL: AO = OC, ∠AOB = ∠COD (opuestos por el vértice) y OB = OD",
            },
        ],
        "hints": [
            "En todo paralelogramo las diagonales se cortan en su punto medio.",
            "Dos ángulos consecutivos de un paralelogramo son suplementarios; los opuestos son iguales.",
            "Para LAL el ángulo tiene que estar **entre** los dos lados que usás.",
        ],
        "solution": [
            "Las diagonales se bisecan: `AO = OC` → `2x + 1 = 3x − 4` → `x = 5`. Entonces `AO = OC = 11 cm` y `AC = 22 cm`.",
            "Ángulos consecutivos suplementarios: `(3y + 15) + (2y + 15) = 180` → `5y + 30 = 180` → `y = 30`.",
            "`∠DAB = 3·30 + 15 = 105°` y `∠ABC = 2·30 + 15 = 75°` (suman 180°). ✔",
            "`∠BCD` es opuesto a `∠DAB`, así que `∠BCD = 105°`.",
            "Congruencia: en `△AOB` y `△COD` tenemos `AO = OC` y `OB = OD` (las diagonales se bisecan) y el ángulo comprendido entre esos lados, `∠AOB = ∠COD`, por ser opuestos por el vértice → **LAL**.",
            "Las otras opciones fallan: `∠OAB` no está entre `AO` y `OB` (sería LLA, que no es criterio), y AAA solo garantiza semejanza.",
        ],
    },
    {
        "id": "g-congruencia-3",
        "node": "g-congruencia",
        "kind": "problem",
        "level": 3,
        "title": "Dos piezas distintas con los mismos datos (el caso LLA)",
        "statement": (
            "Un taller tiene que cortar una pieza triangular `ABC` y el plano solo indica: `AB = 10 cm`, "
            "`BC = 7.5 cm` y que, si se baja la perpendicular desde `B` hasta la recta `AC`, su pie `H` cumple "
            "`AH = 8 cm` (eso fija el ángulo en `A`, que **no** está comprendido entre `AB` y `BC`). El punto "
            "`C` está sobre la semirrecta que sale de `A` y pasa por `H`.\n\n"
            "Resulta que hay **dos** posiciones posibles para `C`: llamalas `C₁` (la más lejana a `A`) y `C₂` "
            "(la más cercana)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto mide AC₁? Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 12.5, "tolerance": 0, "unit": "cm"},
                "answer": "12.5 cm (BH = 6, HC = 4.5, AC₁ = 8 + 4.5)",
            },
            {
                "prompt": "b) ¿Cuánto mide AC₂? Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 3.5, "tolerance": 0, "unit": "cm"},
                "answer": "3.5 cm (8 − 4.5)",
            },
            {
                "prompt": "c) ¿Qué justificación prueba que △BHC₁ ≅ △BHC₂ (y por lo tanto HC₁ = HC₂)?",
                "check": {
                    "type": "choice",
                    "options": [
                        "HC: son rectángulos en H, comparten el cateto BH y tienen igual hipotenusa (BC₁ = BC₂ = 7.5 cm)",
                        "LAL: comparten el lado BH y el ángulo recto en H",
                        "AAA: los dos tienen un ángulo recto",
                        "LLA: comparten BH y el ángulo en C es el mismo en los dos",
                    ],
                    "correct": 0,
                },
                "answer": "HC: son rectángulos en H, comparten el cateto BH y tienen igual hipotenusa",
            },
        ],
        "hints": [
            "Empezá por el triángulo rectángulo `ABH`: conocés la hipotenusa y un cateto.",
            "Después mirá el triángulo rectángulo `BHC`: la hipotenusa es `BC`. ¿De qué lado de `H` puede caer `C`?",
        ],
        "solution": [
            "En `△ABH` (recto en `H`): `BH = √(AB² − AH²) = √(100 − 64) = √36 = 6 cm`.",
            "En `△BHC` (recto en `H`): `HC = √(BC² − BH²) = √(56.25 − 36) = √20.25 = 4.5 cm`.",
            "Sobre la recta `AH`, `C` puede estar a `4.5 cm` de `H` hacia afuera o hacia `A`: `AC₁ = 8 + 4.5 = 12.5 cm` y `AC₂ = 8 − 4.5 = 3.5 cm`.",
            "Las dos piezas cumplen el plano (`AB = 10`, `BC = 7.5` y el mismo ángulo en `A`) pero **no** son congruentes: `AC` mide distinto. Por eso LLA no es un criterio de congruencia.",
            "Los triángulos `BHC₁` y `BHC₂` sí son congruentes por **HC**: rectos en `H`, cateto común `BH` e hipotenusas iguales. De ahí sale `HC₁ = HC₂` sin hacer cuentas: `H` es el punto medio de `C₁C₂`.",
            "En LAL el ángulo debe estar entre dos lados conocidos (con solo `BH` y el ángulo recto falta un lado) y AAA solo da semejanza.",
        ],
    },
    # ==================== g-circulos-arcos ====================
    {
        "id": "g-circulos-arcos-1",
        "node": "g-circulos-arcos",
        "kind": "problem",
        "level": 1,
        "title": "El limpiaparabrisas del colectivo",
        "statement": (
            "El limpiaparabrisas de un colectivo gira alrededor de su eje barriendo un ángulo de `120°`. El "
            "brazo mide `50 cm` desde el eje hasta la punta, y la goma está colocada desde `10 cm` hasta `50 cm` "
            "del eje.\n\n"
            "Usá `π ≈ 3.14`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué longitud recorre la punta del brazo en una pasada? Redondeá a 1 decimal. Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 104.7, "tolerance": 0.001, "unit": "cm"},
                "answer": "104.7 cm ((120/360) · 2 · 3.14 · 50)",
            },
            {
                "prompt": "b) ¿Qué área del vidrio limpia la goma en una pasada? Redondeá al entero. Respondé solo con el número en cm².",
                "check": {"type": "numeric", "value": 2512, "tolerance": 0.001, "unit": "cm²"},
                "answer": "2512 cm² ((1/3) · 3.14 · (50² − 10²))",
            },
        ],
        "hints": [
            "`120°` es una fracción de la vuelta completa: `120/360`.",
            "La goma no arranca en el eje: la zona limpia es un sector grande menos un sector chico (una «corona circular» recortada).",
        ],
        "solution": [
            "Fracción de vuelta: `120° / 360° = 1/3`.",
            "Arco de la punta: `L = (1/3) · 2πr = (1/3) · 2 · 3.14 · 50 = 314/3 ≈ 104.67 ≈ 104.7 cm`.",
            "Sector grande (radio 50): `(1/3) · π · 50² = (1/3) · 2500π`. Sector chico sin goma (radio 10): `(1/3) · π · 10² = (1/3) · 100π`.",
            "Área limpia: `(1/3) · π · (2500 − 100) = (1/3) · 2400π = 800π ≈ 800 · 3.14 = 2512 cm²`.",
            "Error típico: usar `πr²` para la longitud del arco o `2πr` para el área (son fórmulas distintas), u olvidarse de restar el tramo sin goma (daría `≈ 2616.7 cm²`).",
        ],
    },
    {
        "id": "g-circulos-arcos-2",
        "node": "g-circulos-arcos",
        "kind": "problem",
        "level": 2,
        "title": "Dos tangentes desde un punto exterior",
        "statement": (
            "Desde un punto `P` exterior a una circunferencia de centro `O` y radio `6 cm` se trazan las dos "
            "rectas tangentes, que tocan a la circunferencia en `A` y en `B`. El ángulo entre las tangentes es "
            "`∠APB = 50°`.\n\n"
            "Sea `C` un punto de la circunferencia ubicado sobre el **arco mayor** `AB` (el que no mira hacia `P`). "
            "Usá `π ≈ 3.14`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto mide el ángulo central ∠AOB (el que abarca el arco menor)? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 130, "tolerance": 0, "unit": "°"},
                "answer": "130° (360° − 90° − 90° − 50°)",
            },
            {
                "prompt": "b) ¿Cuánto mide el ángulo inscrito ∠ACB? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 65, "tolerance": 0, "unit": "°"},
                "answer": "65° (la mitad de 130°)",
            },
            {
                "prompt": "c) ¿Cuánto mide el arco menor AB? Redondeá a 2 decimales. Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 13.61, "tolerance": 0.002, "unit": "cm"},
                "answer": "13.61 cm ((130/360) · 2 · 3.14 · 6)",
            },
        ],
        "hints": [
            "Cada tangente forma `90°` con el radio en el punto de contacto. Mirá el cuadrilátero `OAPB`.",
            "Los ángulos interiores de un cuadrilátero suman `360°`.",
            "El ángulo inscrito en `C` abarca el arco menor `AB`.",
        ],
        "solution": [
            "Tangente ⊥ radio: `∠OAP = ∠OBP = 90°`.",
            "En el cuadrilátero `OAPB`: `∠AOB = 360° − 90° − 90° − 50° = 130°`.",
            "`C` está en el arco mayor, así que `∠ACB` abarca el arco menor `AB` (de `130°`): `∠ACB = 130° / 2 = 65°`.",
            "Arco menor: `L = (130/360) · 2πr = (13/36) · 2 · 3.14 · 6 = (13/3) · 3.14 ≈ 13.61 cm`.",
            "Dato extra: en general `∠AOB = 180° − ∠APB`, así que el inscrito vale `(180° − ∠APB)/2`.",
            "Error típico: tomar `∠ACB = 50°/2 = 25°` (el ángulo en `P` no es central) o usar `360° − 130° = 230°` como arco que abarca `C` (ese es el arco donde está `C`, no el que abarca).",
        ],
    },
    {
        "id": "g-circulos-arcos-3",
        "node": "g-circulos-arcos",
        "kind": "problem",
        "level": 3,
        "title": "Largo de la correa entre dos poleas",
        "statement": (
            "Una correa **abierta** (no cruzada) une dos poleas de un motor: la grande tiene radio `9 cm`, la "
            "chica radio `3 cm` y la distancia entre sus centros es `12 cm`. La correa está tensa: tiene dos "
            "tramos rectos, cada uno tangente a ambas poleas y del mismo lado de cada una, y abraza un arco de "
            "cada polea.\n\n"
            "Usá `π ≈ 3.14` y `√3 ≈ 1.732`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto mide cada tramo recto de la correa? Redondeá a 2 decimales. Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 10.39, "tolerance": 0.001, "unit": "cm"},
                "answer": "10.39 cm (√(12² − 6²) = 6√3)",
            },
            {
                "prompt": "b) ¿Cuántos grados de la polea grande quedan en contacto con la correa? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 240, "tolerance": 0, "unit": "°"},
                "answer": "240° (180° + 2 · 30°)",
            },
            {
                "prompt": "c) ¿Cuál es el largo total de la correa? Redondeá a 2 decimales. Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 64.74, "tolerance": 0.001, "unit": "cm"},
                "answer": "64.74 cm (12√3 + 14π)",
            },
        ],
        "hints": [
            "Los radios a los puntos de tangencia de un mismo tramo recto son paralelos (los dos son perpendiculares a la correa). Por el centro chico trazá una paralela al tramo recto.",
            "Queda un triángulo rectángulo con hipotenusa `12` (entre centros) y un cateto `9 − 3 = 6`. ¿Qué ángulo tiene si un cateto es la mitad de la hipotenusa?",
            "La correa abraza la polea grande más de media vuelta y la chica menos de media vuelta, en la misma cantidad.",
        ],
        "solution": [
            "Sean `O₁` (grande) y `O₂` (chica). En un tramo recto, los radios `O₁T₁ = 9` y `O₂T₂ = 3` son perpendiculares a la correa. Trazando por `O₂` la paralela a `T₁T₂` se forma un triángulo rectángulo con hipotenusa `O₁O₂ = 12`, cateto `9 − 3 = 6` y el otro cateto igual al tramo recto.",
            "Tramo recto: `√(12² − 6²) = √108 = 6√3 ≈ 6 · 1.732 = 10.392 ≈ 10.39 cm`.",
            "Como el cateto `6` es la mitad de la hipotenusa `12`, el ángulo opuesto (entre la recta de centros y la paralela al tramo) mide `30°` (triángulo 30-60-90).",
            "Por la simetría respecto de la recta de centros, la correa abraza la polea grande en `180° + 2 · 30° = 240°` y la chica en `180° − 2 · 30° = 120°`.",
            "Arcos: grande `(240/360) · 2π · 9 = 12π`; chica `(120/360) · 2π · 3 = 2π`. Total de arcos `14π ≈ 43.96 cm`.",
            "Largo total: `2 · 6√3 + 14π = 12√3 + 14π ≈ 20.784 + 43.96 = 64.744 ≈ 64.74 cm` (con π y √3 exactos da ≈ 64.77 cm).",
            "Error típico: suponer que la correa abraza media vuelta de cada polea (daría `12√3 + 12π`), lo que solo pasa si las poleas tienen el mismo radio.",
        ],
    },
    # ==================== pc-complejos-polares ====================
    {
        "id": "pc-complejos-polares-1",
        "node": "pc-complejos-polares",
        "kind": "problem",
        "level": 1,
        "title": "De binómica a polar y producto",
        "statement": (
            "Sea `z = −√3 + i` y sea `w = 3∠60°` (es decir, `w = 3(cos 60° + i·sen 60°)`).\n\n"
            "Pasá `z` a forma polar y usala para calcular el producto `z · w`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el módulo de z? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2 (√(3 + 1))",
            },
            {
                "prompt": "b) ¿Cuál es el argumento de z, tomado entre 0° y 360°? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 150, "tolerance": 0, "unit": "°"},
                "answer": "150° (segundo cuadrante)",
            },
            {
                "prompt": "c) ¿Cuál es la parte imaginaria de z · w? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -3, "tolerance": 0, "unit": ""},
                "answer": "−3 (z · w = 6∠210° = −3√3 − 3i)",
            },
        ],
        "hints": [
            "Ubicá `z` en el plano: parte real negativa e imaginaria positiva → segundo cuadrante.",
            "El ángulo de referencia sale de `tg α = |b| / |a| = 1/√3`.",
            "En polar se multiplican los módulos y se suman los argumentos.",
        ],
        "solution": [
            "Módulo: `|z| = √((−√3)² + 1²) = √(3 + 1) = 2`.",
            "Ángulo de referencia: `tg α = 1/√3` → `α = 30°`. Como `z` está en el segundo cuadrante, `θ = 180° − 30° = 150°`. Entonces `z = 2∠150°`.",
            "Producto: `z · w = (2 · 3)∠(150° + 60°) = 6∠210°`.",
            "En binómica: `6(cos 210° + i·sen 210°) = 6(−√3/2 − i/2) = −3√3 − 3i`. Parte imaginaria: `−3`.",
            "Verificación en binómica: `w = 3/2 + (3√3/2)i`, y `(−√3 + i)(3/2 + (3√3/2)i) = −3√3/2 − (9/2)i + (3/2)i + (3√3/2)i² = −3√3/2 − 3√3/2 − 3i = −3√3 − 3i`. ✔",
            "Error típico: calcular `arctg(1/(−√3)) = −30°` con la calculadora y no corregir el cuadrante (`−30°` está en el cuarto cuadrante, no en el segundo).",
        ],
    },
    {
        "id": "pc-complejos-polares-2",
        "node": "pc-complejos-polares",
        "kind": "problem",
        "level": 2,
        "title": "Corriente en un circuito de alterna",
        "statement": (
            "En un circuito de corriente alterna se aplica una tensión `V = 220∠0° V` sobre una carga de "
            "impedancia `Z = 5 + 5√3 i Ω`. Por la ley de Ohm en forma compleja, la corriente es "
            "`I = V / Z`.\n\n"
            "Calculá `I` trabajando en forma polar."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el módulo de la corriente |I|? Respondé solo con el número en A.",
                "check": {"type": "numeric", "value": 22, "tolerance": 0, "unit": "A"},
                "answer": "22 A (220 / 10)",
            },
            {
                "prompt": "b) ¿Cuál es el argumento (fase) de I, tomado en el intervalo (−180°, 180°]? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": -60, "tolerance": 0, "unit": "°"},
                "answer": "−60° (0° − 60°)",
            },
            {
                "prompt": "c) ¿Cuál es la parte real de I? Respondé solo con el número en A.",
                "check": {"type": "numeric", "value": 11, "tolerance": 0, "unit": "A"},
                "answer": "11 A (22 · cos(−60°))",
            },
        ],
        "hints": [
            "Pasá primero `Z` a polar: módulo con Pitágoras y ángulo con `tg θ = b/a`.",
            "Al dividir en polar, se dividen los módulos y se **restan** los ángulos.",
        ],
        "solution": [
            "Módulo de `Z`: `|Z| = √(5² + (5√3)²) = √(25 + 75) = √100 = 10 Ω`.",
            "Ángulo de `Z`: `tg θ = 5√3 / 5 = √3` y `Z` está en el primer cuadrante → `θ = 60°`. Entonces `Z = 10∠60° Ω`.",
            "División: `I = (220∠0°) / (10∠60°) = (220/10)∠(0° − 60°) = 22∠−60° A`.",
            "Binómica: `I = 22(cos(−60°) + i·sen(−60°)) = 22(1/2 − (√3/2)i) = 11 − 11√3 i ≈ 11 − 19.05i A`. Parte real: `11 A`.",
            "Verificación por conjugado: `220 / (5 + 5√3 i) = 220(5 − 5√3 i) / (25 + 75) = 2.2(5 − 5√3 i) = 11 − 11√3 i`. ✔",
            "Interpretación: la corriente está atrasada `60°` respecto de la tensión (carga inductiva). Error típico: sumar los ángulos al dividir (daría `+60°`).",
        ],
    },
    {
        "id": "pc-complejos-polares-3",
        "node": "pc-complejos-polares",
        "kind": "problem",
        "level": 3,
        "title": "Una potencia doce con De Moivre",
        "statement": (
            "Sea `z = (1 − i) / (√3 + i)`.\n\n"
            "Calculá `z¹²` sin desarrollar potencias en forma binómica: pasá numerador y denominador a forma "
            "polar y aplicá De Moivre."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el argumento de z, tomado en el intervalo (−180°, 180°]? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": -75, "tolerance": 0, "unit": "°"},
                "answer": "−75° (−45° − 30°)",
            },
            {
                "prompt": "b) ¿Cuál es el módulo de z¹²? Respondé con la fracción exacta o el decimal exacto.",
                "check": {"type": "numeric", "value": 0.015625, "tolerance": 0, "unit": ""},
                "answer": "1/64 = 0.015625 ((√2/2)¹² = 2⁶/2¹²)",
            },
            {
                "prompt": "c) ¿Cuánto vale z¹²?",
                "check": {
                    "type": "choice",
                    "options": ["−1/64", "1/64", "i/64", "−i/64"],
                    "correct": 0,
                },
                "answer": "−1/64",
            },
        ],
        "hints": [
            "`1 − i` está en el cuarto cuadrante con ángulo de referencia `45°`; `√3 + i` en el primero con `30°`.",
            "Dividir en polar: dividís módulos y restás ángulos. Después elevás: módulo a la 12 y ángulo por 12.",
            "Para ubicar el resultado, sumale o restale vueltas de `360°` al ángulo hasta que quede en un rango conocido.",
        ],
        "solution": [
            "Numerador: `|1 − i| = √2` y su argumento es `−45°` → `1 − i = √2∠−45°`.",
            "Denominador: `|√3 + i| = √(3 + 1) = 2` y `tg θ = 1/√3` → `30°` → `√3 + i = 2∠30°`.",
            "Cociente: `z = (√2/2)∠(−45° − 30°) = (√2/2)∠−75°`. Argumento: `−75°`.",
            "De Moivre: `|z|¹² = (√2/2)¹² = (√2)¹² / 2¹² = 2⁶ / 2¹² = 1/64`, y `arg(z¹²) = 12 · (−75°) = −900°`.",
            "Reducimos el ángulo: `−900° + 3 · 360° = 180°`. Entonces `z¹² = (1/64)∠180° = (1/64)(cos 180° + i·sen 180°) = −1/64`.",
            "Control: un número real negativo tiene argumento `180°`, y su módulo es `1/64 = 0.015625`. ✔",
            "Errores típicos: multiplicar el módulo por 12 en lugar de elevarlo a la 12, dejar `|z| = √2/2` sin elevar, o reducir mal el ángulo (`−900°` equivale a `180°`, no a `0°`, que daría `+1/64`).",
        ],
    },
    # ==================== pc-secciones-conicas ====================
    {
        "id": "pc-secciones-conicas-1",
        "node": "pc-secciones-conicas",
        "kind": "problem",
        "level": 1,
        "title": "Parábola a partir del foco y la directriz",
        "statement": (
            "Una parábola tiene **foco** `F(2, 5)` y **directriz** la recta horizontal `y = 1`. Es decir, está "
            "formada por todos los puntos que están a la misma distancia de `F` que de la recta `y = 1`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es su ecuación?",
                "check": {
                    "type": "choice",
                    "options": [
                        "(x − 2)² = 8(y − 3)",
                        "(x − 2)² = 16(y − 3)",
                        "(x − 2)² = 8(y − 5)",
                        "(y − 3)² = 8(x − 2)",
                    ],
                    "correct": 0,
                },
                "answer": "(x − 2)² = 8(y − 3)",
            },
            {
                "prompt": "b) La parábola pasa por un punto de abscisa x = 10. ¿Cuál es su ordenada? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 11, "tolerance": 0, "unit": ""},
                "answer": "11 (64 = 8(y − 3))",
            },
        ],
        "hints": [
            "El vértice está a mitad de camino entre el foco y la directriz, sobre la vertical que pasa por el foco.",
            "`p` es la distancia del vértice al foco (no del foco a la directriz).",
        ],
        "solution": [
            "El eje de simetría es la vertical `x = 2` (pasa por el foco y es perpendicular a la directriz).",
            "Vértice: punto medio entre `F(2, 5)` y la directriz `y = 1` → `V(2, 3)`. Distancia vértice-foco: `p = 5 − 3 = 2` (positivo: abre hacia arriba).",
            "Ecuación: `(x − h)² = 4p(y − k)` → `(x − 2)² = 8(y − 3)`.",
            "Con `x = 10`: `(10 − 2)² = 64 = 8(y − 3)` → `y − 3 = 8` → `y = 11`.",
            "Verificación con la definición: distancia de `(10, 11)` a `F`: `√(8² + 6²) = 10`; distancia a la recta `y = 1`: `11 − 1 = 10`. ✔",
            "Error típico: tomar `p = 4` (distancia del foco a la directriz), que da `(x − 2)² = 16(y − 3)`.",
        ],
    },
    {
        "id": "pc-secciones-conicas-2",
        "node": "pc-secciones-conicas",
        "kind": "problem",
        "level": 2,
        "title": "Completar cuadrados para reconocer una elipse",
        "statement": (
            "La ecuación `25x² + 16y² + 50x − 64y − 311 = 0` representa una cónica.\n\n"
            "Llevala a su forma canónica completando cuadrados y obtené sus elementos."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es su forma canónica?",
                "check": {
                    "type": "choice",
                    "options": [
                        "(x + 1)²/16 + (y − 2)²/25 = 1",
                        "(x − 1)²/16 + (y + 2)²/25 = 1",
                        "(x + 1)²/25 + (y − 2)²/16 = 1",
                        "(x + 1)²/4 + (y − 2)²/5 = 1",
                    ],
                    "correct": 0,
                },
                "answer": "(x + 1)²/16 + (y − 2)²/25 = 1",
            },
            {
                "prompt": "b) ¿Cuál es la ordenada (coordenada y) del foco superior? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                "answer": "5 (focos (−1, 5) y (−1, −1))",
            },
            {
                "prompt": "c) ¿Cuánto mide el eje menor (el segmento completo)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": ""},
                "answer": "8 (2b = 2 · 4)",
            },
        ],
        "hints": [
            "Agrupá: `25(x² + 2x) + 16(y² − 4y) = 311`. Completá cada paréntesis y compensá lo que sumaste, multiplicado por su coeficiente.",
            "Dividí todo por el número que te quede a la derecha para obtener `= 1`.",
            "El denominador más grande indica el eje mayor; `c² = a² − b²`.",
        ],
        "solution": [
            "Agrupamos: `25(x² + 2x) + 16(y² − 4y) = 311`.",
            "Completamos cuadrados: `x² + 2x = (x + 1)² − 1` e `y² − 4y = (y − 2)² − 4`. Queda `25(x + 1)² − 25 + 16(y − 2)² − 64 = 311` → `25(x + 1)² + 16(y − 2)² = 400`.",
            "Dividimos por 400: `(x + 1)²/16 + (y − 2)²/25 = 1`. Es una elipse de centro `(−1, 2)`.",
            "El denominador mayor (`25`) está bajo `y`: eje mayor **vertical** con `a = 5`; semieje menor `b = 4`.",
            "Focos: `c = √(25 − 16) = 3`, sobre la vertical `x = −1`: `(−1, 2 + 3) = (−1, 5)` y `(−1, 2 − 3) = (−1, −1)`. Foco superior: `y = 5`.",
            "Eje menor: `2b = 8`. Control: el punto `(3, 2)` (extremo del eje menor) cumple la ecuación original: `25·9 + 16·4 + 150 − 128 − 311 = 0`. ✔",
            "Errores típicos: olvidar multiplicar lo que se agrega al completar cuadrados por 25 y 16, o poner los focos sobre la horizontal porque `x` aparece primero.",
        ],
    },
    {
        "id": "pc-secciones-conicas-3",
        "node": "pc-secciones-conicas",
        "kind": "problem",
        "level": 3,
        "title": "El cantero elíptico del jardinero",
        "statement": (
            "Un jardinero quiere trazar un cantero con forma de **elipse**. Clava dos estacas en los puntos "
            "`F₁(−2, 1)` y `F₂(6, 1)` (coordenadas en metros), que serán los **focos**, ata a ellas una soga y, "
            "manteniéndola tensa con una varilla, recorre el borde. Quiere que el borde pase exactamente por un "
            "árbol ubicado en `P(2, 4)`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué largo de soga necesita (entre las dos estacas, pasando por la varilla)? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "m"},
                "answer": "10 m (PF₁ + PF₂ = 5 + 5)",
            },
            {
                "prompt": "b) ¿Cuál es la ecuación del borde del cantero?",
                "check": {
                    "type": "choice",
                    "options": [
                        "(x − 2)²/25 + (y − 1)²/9 = 1",
                        "(x − 2)²/25 + (y − 1)²/16 = 1",
                        "(x + 2)²/25 + (y + 1)²/9 = 1",
                        "x²/25 + y²/9 = 1",
                    ],
                    "correct": 0,
                },
                "answer": "(x − 2)²/25 + (y − 1)²/9 = 1",
            },
            {
                "prompt": "c) Justo «encima» de la estaca F₂ (con x = 6 e y > 1) hay un punto del borde. ¿Cuál es su ordenada? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 2.8, "tolerance": 0, "unit": "m"},
                "answer": "2.8 m (y − 1 = b²/a = 9/5)",
            },
        ],
        "hints": [
            "La soga tensa garantiza que la **suma** de las distancias a los dos focos es constante, e igual a `2a`.",
            "El centro es el punto medio de los focos; `c` es la mitad de la distancia entre ellos. Después usá `b² = a² − c²`.",
            "Para el inciso c, reemplazá `x = 6` en la ecuación y despejá `y`.",
        ],
        "solution": [
            "Distancias del árbol a las estacas: `PF₁ = √((2 + 2)² + (4 − 1)²) = √(16 + 9) = 5` y `PF₂ = √((2 − 6)² + 3²) = 5`. Largo de soga: `2a = 10 m`, así que `a = 5`.",
            "Centro: punto medio de los focos, `C(2, 1)`. Distancia entre focos `8` → `c = 4`. Eje mayor horizontal (los focos están sobre `y = 1`).",
            "Semieje menor: `b² = a² − c² = 25 − 16 = 9` → `b = 3`. Ecuación: `(x − 2)²/25 + (y − 1)²/9 = 1`.",
            "Control: `P(2, 4)` da `0 + 9/9 = 1` ✔ (de hecho es el extremo superior del eje menor). Vértices del eje mayor: `(−3, 1)` y `(7, 1)`.",
            "Con `x = 6`: `16/25 + (y − 1)²/9 = 1` → `(y − 1)² = 9 · 9/25 = 81/25` → `y − 1 = 9/5 = 1.8` → `y = 2.8 m`.",
            "Error típico: usar `b = c = 4` (confundir semieje con distancia focal) o poner el centro en el origen porque las ecuaciones del apunte suelen estar centradas allí.",
        ],
    },
    # ==================== pc-vectores ====================
    {
        "id": "pc-vectores-1",
        "node": "pc-vectores",
        "kind": "problem",
        "level": 1,
        "title": "Combinación lineal, módulo y producto punto",
        "statement": "Dados los vectores `u = ⟨4, 3⟩` y `v = ⟨1, −2⟩`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el módulo del vector 2u − 3v? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 13, "tolerance": 0, "unit": ""},
                "answer": "13 (2u − 3v = ⟨5, 12⟩)",
            },
            {
                "prompt": "b) ¿Cuánto vale el producto punto u · v? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -2, "tolerance": 0, "unit": ""},
                "answer": "−2 (4 − 6)",
            },
            {
                "prompt": "c) ¿Cómo es el ángulo entre u y v?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Obtuso (entre 90° y 180°), porque u · v < 0",
                        "Agudo (menor que 90°), porque u · v < 0",
                        "Recto (90°), porque u · v es cercano a 0",
                        "No se puede saber sin calcular el coseno con decimales",
                    ],
                    "correct": 0,
                },
                "answer": "Obtuso, porque u · v < 0",
            },
        ],
        "hints": [
            "Primero escalá cada vector (multiplicá cada componente) y después restá componente a componente.",
            "El signo de `u · v = |u||v|cos θ` es el signo de `cos θ`.",
        ],
        "solution": [
            "`2u = ⟨8, 6⟩` y `3v = ⟨3, −6⟩`, así que `2u − 3v = ⟨8 − 3, 6 − (−6)⟩ = ⟨5, 12⟩`.",
            "Módulo: `|⟨5, 12⟩| = √(25 + 144) = √169 = 13`.",
            "Producto punto: `u · v = 4·1 + 3·(−2) = 4 − 6 = −2`.",
            "Como `|u|` y `|v|` son positivos, el signo de `u · v` es el de `cos θ`: negativo → `θ` es **obtuso**.",
            "Comprobación: `cos θ = −2 / (5 · √5) ≈ −0.179` → `θ ≈ 100.3°`.",
            "Error típico: restar `⟨8, 6⟩ − ⟨3, −6⟩` como `⟨5, 0⟩` (signo mal), o creer que un producto punto «chico» significa ángulo recto: solo `0` exacto da `90°`.",
        ],
    },
    {
        "id": "pc-vectores-2",
        "node": "pc-vectores",
        "kind": "problem",
        "level": 2,
        "title": "Cruzar el río en lancha",
        "statement": (
            "Una lancha cruza un río de `400 m` de ancho con orillas rectas y paralelas. Respecto del agua, "
            "la lancha va a `10 km/h`; la corriente arrastra el agua a `6 km/h`, paralela a las orillas. "
            "Suponé velocidades constantes.\n\n"
            "Caso 1: el conductor apunta la proa **perpendicular** a la orilla.\n"
            "Caso 2: el conductor apunta la proa **aguas arriba**, con el ángulo justo para llegar al punto "
            "exactamente enfrente del de partida."
        ),
        "parts": [
            {
                "prompt": "a) En el caso 1, ¿cuántos metros río abajo del punto de enfrente llega? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 240, "tolerance": 0, "unit": "m"},
                "answer": "240 m (tarda 0.04 h y la corriente la lleva 6 · 0.04 km)",
            },
            {
                "prompt": "b) En el caso 2, ¿cuál es la rapidez de la lancha respecto de la orilla? Respondé solo con el número en km/h.",
                "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": "km/h"},
                "answer": "8 km/h (√(10² − 6²))",
            },
            {
                "prompt": "c) En el caso 2, ¿cuánto tarda en cruzar? Respondé solo con el número en min.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": "min"},
                "answer": "3 min (0.4 km ÷ 8 km/h = 0.05 h)",
            },
        ],
        "hints": [
            "Velocidad respecto de la orilla = velocidad de la lancha respecto del agua + velocidad de la corriente (suma de vectores).",
            "El tiempo de cruce depende solo de la componente perpendicular a la orilla.",
            "En el caso 2 la componente paralela de la lancha tiene que anular a la corriente: la resultante queda perpendicular y se forma un triángulo rectángulo con hipotenusa 10.",
        ],
        "solution": [
            "Ejes: `x` paralelo a la orilla (sentido de la corriente), `y` perpendicular. Corriente: `⟨6, 0⟩ km/h`. Ancho: `0.4 km`.",
            "Caso 1: lancha respecto del agua `⟨0, 10⟩`, resultante `⟨6, 10⟩`. Tiempo: `0.4 / 10 = 0.04 h` (= 2.4 min). Deriva: `6 · 0.04 = 0.24 km = 240 m`.",
            "Caso 2: la lancha respecto del agua es `⟨−6, v_y⟩` con módulo 10, para que la resultante sea `⟨0, v_y⟩`. Entonces `v_y = √(10² − 6²) = √64 = 8 km/h`.",
            "Tiempo de cruce en el caso 2: `0.4 / 8 = 0.05 h = 3 min`.",
            "Ángulo de la proa respecto de la perpendicular: `sen φ = 6/10` → `φ ≈ 36.9°` aguas arriba.",
            "Observación: llegar justo enfrente cuesta más tiempo (3 min contra 2.4 min), porque parte de la velocidad se usa para compensar la corriente. Error típico: sumar `10 + 6` o restar `10 − 6` como si los vectores fueran paralelos.",
        ],
    },
    {
        "id": "pc-vectores-3",
        "node": "pc-vectores",
        "kind": "problem",
        "level": 3,
        "title": "Ángulo, proyección y trabajo sobre un riel",
        "statement": (
            "Un carrito se desplaza en línea recta sobre un riel desde `A(1, 2)` hasta `B(7, 10)` (coordenadas "
            "en metros) mientras actúa sobre él una fuerza constante `F = ⟨7, 1⟩ N`.\n\n"
            "Llamá `d` al vector desplazamiento de `A` a `B`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué ángulo forman F y d? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 45, "tolerance": 0, "unit": "°"},
                "answer": "45° (cos θ = 50 / (√50 · 10) = √2/2)",
            },
            {
                "prompt": "b) ¿Cuál es el vector proyección de F sobre la dirección de d?",
                "check": {
                    "type": "choice",
                    "options": ["⟨3, 4⟩ N", "⟨30, 40⟩ N", "⟨6, 8⟩ N", "⟨7, 1⟩ N"],
                    "correct": 0,
                },
                "answer": "⟨3, 4⟩ N",
            },
            {
                "prompt": "c) ¿Qué trabajo realiza F en el trayecto? Respondé solo con el número en J.",
                "check": {"type": "numeric", "value": 50, "tolerance": 0, "unit": "J"},
                "answer": "50 J (F · d)",
            },
        ],
        "hints": [
            "`d = B − A`. Para el ángulo usá `cos θ = (F · d) / (|F| · |d|)`.",
            "Vector proyección de `F` sobre `d`: `((F · d) / |d|²) · d`. Ojo: se divide por el módulo de `d` **al cuadrado**.",
            "El trabajo de una fuerza constante es `W = F · d`.",
        ],
        "solution": [
            "Desplazamiento: `d = B − A = ⟨7 − 1, 10 − 2⟩ = ⟨6, 8⟩ m`, con `|d| = √(36 + 64) = 10 m`.",
            "Producto punto: `F · d = 7·6 + 1·8 = 42 + 8 = 50`. Módulo de la fuerza: `|F| = √(49 + 1) = √50 = 5√2 N`.",
            "Ángulo: `cos θ = 50 / (5√2 · 10) = 1/√2 = √2/2` → `θ = 45°`.",
            "Componente escalar de `F` en la dirección de `d`: `(F · d) / |d| = 50 / 10 = 5 N` (también `|F| cos 45° = 5√2 · √2/2 = 5`).",
            "Vector proyección: `(50 / 100) · ⟨6, 8⟩ = ⟨3, 4⟩ N` (módulo 5, misma dirección que `d`).",
            "Trabajo: `W = F · d = 50 J` (= componente útil 5 N × 10 m).",
            "Errores típicos: dividir solo por `|d|` (da `⟨30, 40⟩`), dividir por `|F|²` (da `⟨6, 8⟩`) o proyectar `d` sobre `F` en lugar de `F` sobre `d`.",
        ],
    },
    # ==================== pc-matrices-operaciones ====================
    {
        "id": "pc-matrices-operaciones-1",
        "node": "pc-matrices-operaciones",
        "kind": "problem",
        "level": 1,
        "title": "Costos de dos panaderías con dos proveedores",
        "statement": (
            "Una cadena tiene dos panaderías, Centro y Norte. La matriz `Q` indica lo que compra cada una por "
            "semana (filas: Centro, Norte; columnas: bolsas de harina, bolsas de azúcar, cajas de manteca):\n\n"
            "`Q = [[10, 4, 6], [8, 5, 2]]`\n\n"
            "La matriz `P` da el precio por unidad, en miles de pesos, de dos proveedores (filas: harina, "
            "azúcar, manteca; columnas: proveedor A, proveedor B):\n\n"
            "`P = [[2, 3], [3, 1], [5, 4]]`"
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué dimensión tiene Q · P y qué representa cada entrada?",
                "check": {
                    "type": "choice",
                    "options": [
                        "2 × 2: el costo semanal de cada panadería si le compra todo a cada proveedor",
                        "3 × 3: el costo de cada insumo con cada proveedor",
                        "2 × 3: el costo de cada insumo en cada panadería",
                        "No se puede calcular porque Q y P tienen distinta dimensión",
                    ],
                    "correct": 0,
                },
                "answer": "2 × 2: costo semanal de cada panadería con cada proveedor",
            },
            {
                "prompt": "b) ¿Cuánto vale la entrada (fila 2, columna 1) de Q · P? Respondé solo con el número en miles de $.",
                "check": {"type": "numeric", "value": 41, "tolerance": 0, "unit": "miles de $"},
                "answer": "41 miles de $ (8·2 + 5·3 + 2·5)",
            },
            {
                "prompt": "c) ¿Cuánto ahorra la cadena por semana si las dos panaderías le compran todo al proveedor B en lugar del A? Respondé solo con el número en miles de $.",
                "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": "miles de $"},
                "answer": "8 miles de $ ((62 + 41) − (58 + 37))",
            },
        ],
        "hints": [
            "`(2 × 3) · (3 × 2)`: los del medio coinciden y quedan los de afuera.",
            "La entrada `(i, j)` es la fila `i` de `Q` (lo que compra una panadería) por la columna `j` de `P` (los precios de un proveedor).",
        ],
        "solution": [
            "Dimensión: `Q` es `2 × 3` y `P` es `3 × 2` → `Q · P` es `2 × 2`. La fila indica la panadería y la columna el proveedor: cada entrada es un costo semanal total.",
            "Fila 1 (Centro): con A `10·2 + 4·3 + 6·5 = 20 + 12 + 30 = 62`; con B `10·3 + 4·1 + 6·4 = 30 + 4 + 24 = 58`.",
            "Fila 2 (Norte): con A `8·2 + 5·3 + 2·5 = 16 + 15 + 10 = 41`; con B `8·3 + 5·1 + 2·4 = 24 + 5 + 8 = 37`.",
            "`Q · P = [[62, 58], [41, 37]]`. La entrada (2, 1) es `41` miles de $.",
            "Total con A (columna 1): `62 + 41 = 103`; total con B (columna 2): `58 + 37 = 95`. Ahorro: `103 − 95 = 8` miles de $ por semana.",
            "Error típico: intentar `P · Q` (`3 × 2` por `2 × 3`), que sí existe pero da una matriz `3 × 3` sin sentido para este problema.",
        ],
    },
    {
        "id": "pc-matrices-operaciones-2",
        "node": "pc-matrices-operaciones",
        "kind": "problem",
        "level": 2,
        "title": "El orden de las transformaciones importa",
        "statement": (
            "En un videojuego 2D, `R = [[0, −1], [1, 0]]` es la matriz de la rotación de 90° antihoraria "
            "alrededor del origen y `S = [[1, 0], [0, −1]]` es la de la reflexión sobre el eje X. Los puntos "
            "se escriben como vectores columna y la matriz se multiplica a la izquierda.\n\n"
            "Se quiere aplicar al punto `P(2, 5)` **primero la rotación y después la reflexión**."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la matriz única M que hace las dos transformaciones en ese orden?",
                "check": {
                    "type": "choice",
                    "options": [
                        "M = S · R = [[0, −1], [−1, 0]]",
                        "M = R · S = [[0, 1], [1, 0]]",
                        "M = [[0, 1], [−1, 0]]",
                        "M = R + S = [[1, −1], [1, −1]]",
                    ],
                    "correct": 0,
                },
                "answer": "M = S · R = [[0, −1], [−1, 0]]",
            },
            {
                "prompt": "b) ¿Cuál es la coordenada x de la imagen de P? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -5, "tolerance": 0, "unit": ""},
                "answer": "−5 (M · P = (−5, −2))",
            },
            {
                "prompt": "c) Si por error se aplica primero la reflexión y después la rotación, ¿cuál es la coordenada x de la imagen de P? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                "answer": "5 (R · S · P = (5, 2))",
            },
        ],
        "hints": [
            "Si primero actúa `R` sobre `P`, tenés `R·P`; después `S` actúa sobre eso: `S·(R·P) = (S·R)·P`.",
            "Cada entrada de `S·R` es fila de `S` por columna de `R`.",
        ],
        "solution": [
            "Orden: primero `R`, después `S` → `M = S · R` (la que actúa primero queda a la derecha, pegada al vector).",
            "`S · R`: fila 1 de `S` `[1, 0]` con columnas de `R` `[0, 1]` y `[−1, 0]` → `0` y `−1`; fila 2 `[0, −1]` → `−1` y `0`. `M = [[0, −1], [−1, 0]]`.",
            "`M · P = [0·2 + (−1)·5, (−1)·2 + 0·5] = (−5, −2)`. Comprobación paso a paso: `R·P = (−5, 2)` y reflejar sobre el eje X da `(−5, −2)`. ✔",
            "Orden inverso: `R · S = [[0, 1], [1, 0]]` y `R · S · P = (5, 2)`. Paso a paso: `S·P = (2, −5)` y rotar 90° da `(5, 2)`. ✔",
            "Como `(−5, −2) ≠ (5, 2)`, queda claro que `S · R ≠ R · S`: el producto de matrices no es conmutativo. (`S·R` es la reflexión sobre `y = −x` y `R·S` la reflexión sobre `y = x`).",
            "Error típico: escribir las matrices en el orden en que se «leen» las acciones (`R · S`), cuando la primera en actuar es la de la derecha.",
        ],
    },
    {
        "id": "pc-matrices-operaciones-3",
        "node": "pc-matrices-operaciones",
        "kind": "problem",
        "level": 3,
        "title": "Hallar una matriz conociendo su cuadrado",
        "statement": (
            "Sea `A = [[1, a], [b, 2]]` con `a` y `b` números reales. Se sabe que "
            "`A² = A · A = [[7, 6], [9, 10]]`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale a? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2 (3a = 6)",
            },
            {
                "prompt": "b) ¿Cuánto vale b? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3 (3b = 9)",
            },
            {
                "prompt": "c) La matriz A² − 3A resulta igual a k · I (I es la identidad 2 × 2). ¿Cuánto vale k? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4 (A² − 3A = [[4, 0], [0, 4]])",
            },
        ],
        "hints": [
            "Calculá `A · A` con letras, entrada por entrada (fila por columna), e igualá con la matriz dada.",
            "Te quedan cuatro ecuaciones: dos sirven para despejar y las otras dos para verificar.",
            "Para `3A`, multiplicá cada entrada por 3; después restá entrada por entrada.",
        ],
        "solution": [
            "`A · A = [[1·1 + a·b, 1·a + a·2], [b·1 + 2·b, b·a + 2·2]] = [[1 + ab, 3a], [3b, ab + 4]]`.",
            "Igualando con `[[7, 6], [9, 10]]`: `3a = 6` → `a = 2`; `3b = 9` → `b = 3`.",
            "Verificación con las otras dos entradas: `1 + ab = 1 + 6 = 7` ✔ y `ab + 4 = 6 + 4 = 10` ✔. Entonces `A = [[1, 2], [3, 2]]`.",
            "`3A = [[3, 6], [9, 6]]`, así que `A² − 3A = [[7 − 3, 6 − 6], [9 − 9, 10 − 6]] = [[4, 0], [0, 4]] = 4I`. Entonces `k = 4`.",
            "Consecuencia útil: `A² − 3A = 4I` se puede escribir `A · (A − 3I) = 4I`, o sea `A⁻¹ = (A − 3I)/4 = [[−1/2, 1/2], [3/4, −1/4]]` (se comprueba que `A · A⁻¹ = I`).",
            "Error típico: elevar al cuadrado entrada por entrada (`[[1, a²], [b², 4]]`): el cuadrado de una matriz es el producto fila por columna, no el cuadrado de cada número.",
        ],
    },
    # ==================== pc-determinantes-inversas ====================
    {
        "id": "pc-determinantes-inversas-1",
        "node": "pc-determinantes-inversas",
        "kind": "problem",
        "level": 1,
        "title": "Cuánto agranda las áreas una transformación",
        "statement": (
            "La transformación del plano dada por `A = [[3, 1], [1, 2]]` se aplica a un rectángulo de lados "
            "`2 cm` y `3 cm`, que queda convertido en un paralelogramo."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale det(A)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                "answer": "5 (3·2 − 1·1)",
            },
            {
                "prompt": "b) ¿Qué área tiene el paralelogramo? Respondé solo con el número en cm².",
                "check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": "cm²"},
                "answer": "30 cm² (6 · 5)",
            },
            {
                "prompt": "c) ¿Cuál es la matriz inversa A⁻¹?",
                "check": {
                    "type": "choice",
                    "options": [
                        "(1/5) · [[2, −1], [−1, 3]]",
                        "(1/5) · [[3, −1], [−1, 2]]",
                        "(1/5) · [[2, 1], [1, 3]]",
                        "[[1/3, 1], [1, 1/2]]",
                    ],
                    "correct": 0,
                },
                "answer": "(1/5) · [[2, −1], [−1, 3]]",
            },
        ],
        "hints": [
            "`|det(A)|` es el factor por el que se multiplican todas las áreas.",
            "Para la inversa 2 × 2: intercambiá la diagonal principal, cambiá el signo de la otra diagonal y dividí por el determinante.",
        ],
        "solution": [
            "`det(A) = 3·2 − 1·1 = 6 − 1 = 5`.",
            "Área original: `2 · 3 = 6 cm²`. Área transformada: `|det(A)| · 6 = 5 · 6 = 30 cm²`.",
            "Inversa: `A⁻¹ = (1/5) · [[2, −1], [−1, 3]]`.",
            "Verificación: `A · [[2, −1], [−1, 3]] = [[3·2 + 1·(−1), 3·(−1) + 1·3], [1·2 + 2·(−1), 1·(−1) + 2·3]] = [[5, 0], [0, 5]]`, que dividido por 5 da `I`. ✔",
            "Errores típicos: no intercambiar la diagonal principal (`[[3, −1], [−1, 2]]`) o invertir cada entrada por separado (`[[1/3, 1], [1, 1/2]]`).",
        ],
    },
    {
        "id": "pc-determinantes-inversas-2",
        "node": "pc-determinantes-inversas",
        "kind": "problem",
        "level": 2,
        "title": "Un sistema con parámetro",
        "statement": (
            "Considerá el sistema de ecuaciones\n\n"
            "`k·x + 2y = 8`\n"
            "`2x + k·y = 7`\n\n"
            "donde `k` es un número real."
        ),
        "parts": [
            {
                "prompt": "a) ¿Para qué valores de k el sistema NO tiene solución única?",
                "check": {
                    "type": "choice",
                    "options": ["k = 2 o k = −2", "Solo k = 2", "k = 4", "k = 0"],
                    "correct": 0,
                },
                "answer": "k = 2 o k = −2 (det = k² − 4 = 0)",
            },
            {
                "prompt": "b) Para k = 3, ¿cuánto vale x? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2 (y = 1)",
            },
            {
                "prompt": "c) Para k = 2, ¿qué tipo de sistema es?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Incompatible: no tiene solución (rectas paralelas distintas)",
                        "Compatible indeterminado: infinitas soluciones (rectas coincidentes)",
                        "Compatible determinado: una única solución",
                    ],
                    "correct": 0,
                },
                "answer": "Incompatible: no tiene solución",
            },
        ],
        "hints": [
            "Escribí la matriz de coeficientes y calculá su determinante en función de `k`.",
            "Con `det ≠ 0` podés usar `X = A⁻¹ · B` (o la regla de Cramer).",
            "Con `det = 0` reemplazá el valor de `k` y compará las dos ecuaciones: ¿son la misma recta o rectas paralelas?",
        ],
        "solution": [
            "Matriz de coeficientes `A = [[k, 2], [2, k]]`: `det(A) = k² − 4`. Es cero si `k = 2` o `k = −2`; para esos valores no hay solución única.",
            "Con `k = 3`: `det = 9 − 4 = 5` y `A⁻¹ = (1/5) · [[3, −2], [−2, 3]]`.",
            "`x = (3·8 − 2·7)/5 = (24 − 14)/5 = 2` e `y = (−2·8 + 3·7)/5 = (−16 + 21)/5 = 1`. Verificación: `3·2 + 2·1 = 8` ✔ y `2·2 + 3·1 = 7` ✔.",
            "Con `k = 2`: `2x + 2y = 8` (o sea `x + y = 4`) y `2x + 2y = 7` (o sea `x + y = 3.5`). Misma pendiente y distinta ordenada: rectas paralelas → **incompatible**.",
            "(Con `k = −2` también es incompatible: `−2x + 2y = 8` da `x − y = −4`, y `2x − 2y = 7` da `x − y = 3.5`).",
            "Error típico: creer que `det = 0` significa siempre «infinitas soluciones»; hay que mirar los términos independientes.",
        ],
    },
    {
        "id": "pc-determinantes-inversas-3",
        "node": "pc-determinantes-inversas",
        "kind": "problem",
        "level": 3,
        "title": "Tres compras y tres precios (sistema 3 × 3)",
        "statement": (
            "En un almacén hay tres productos con precios `x`, `y`, `z` (en miles de pesos). Se registraron "
            "tres compras:\n\n"
            "- Compra 1: una unidad de cada producto, por `$9` mil.\n"
            "- Compra 2: dos del primero, una del segundo y tres del tercero, por `$17` mil.\n"
            "- Compra 3: una del primero, dos del segundo y una del tercero, por `$12` mil.\n\n"
            "Escribí el sistema como `A · X = B` con `X = [x, y, z]` en columna y resolvelo con "
            "determinantes o con la matriz inversa."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale det(A)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -1, "tolerance": 0, "unit": ""},
                "answer": "−1",
            },
            {
                "prompt": "b) ¿Cuál es A⁻¹?",
                "check": {
                    "type": "choice",
                    "options": [
                        "[[5, −1, −2], [−1, 0, 1], [−3, 1, 1]]",
                        "[[5, −1, −3], [−1, 0, 1], [−2, 1, 1]]",
                        "[[−5, 1, 2], [1, 0, −1], [3, −1, −1]]",
                    ],
                    "correct": 0,
                },
                "answer": "[[5, −1, −2], [−1, 0, 1], [−3, 1, 1]]",
            },
            {
                "prompt": "c) ¿Cuál es el precio x del primer producto? Respondé solo con el número en miles de $.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "miles de $"},
                "answer": "4 miles de $ (X = (4, 3, 2))",
            },
        ],
        "hints": [
            "`A = [[1, 1, 1], [2, 1, 3], [1, 2, 1]]` y `B = [9, 17, 12]`. Desarrollá el determinante por la primera fila (o con Sarrus).",
            "Inversa: matriz de cofactores, trasponela (adjunta) y dividí por `det(A)`. Cuidado con los signos alternados `+ − +`.",
            "Con Cramer: `x = det(Aₓ) / det(A)`, donde `Aₓ` es `A` con la primera columna reemplazada por `B`.",
        ],
        "solution": [
            "Sistema: `x + y + z = 9`, `2x + y + 3z = 17`, `x + 2y + z = 12`, con `A = [[1, 1, 1], [2, 1, 3], [1, 2, 1]]`.",
            "Determinante por la fila 1: `1·(1·1 − 3·2) − 1·(2·1 − 3·1) + 1·(2·2 − 1·1) = 1·(−5) − 1·(−1) + 1·3 = −5 + 1 + 3 = −1`.",
            "Cofactores `Cᵢⱼ = (−1)^(i+j)·Mᵢⱼ`: fila 1 `(−5, 1, 3)`, fila 2 `(1, 0, −1)`, fila 3 `(2, −1, −1)`. Adjunta (traspuesta): `[[−5, 1, 2], [1, 0, −1], [3, −1, −1]]`.",
            "Dividiendo por `det = −1`: `A⁻¹ = [[5, −1, −2], [−1, 0, 1], [−3, 1, 1]]`. Control: fila 1 de `A` por columna 1 de `A⁻¹` = `5 − 1 − 3 = 1` ✔.",
            "`X = A⁻¹ · B`: `x = 5·9 − 17 − 2·12 = 45 − 17 − 24 = 4`; `y = −9 + 0 + 12 = 3`; `z = −3·9 + 17 + 12 = 2`.",
            "Con Cramer: `det(Aₓ) = det([[9, 1, 1], [17, 1, 3], [12, 2, 1]]) = 9·(−5) − 1·(17 − 36) + 1·(34 − 12) = −45 + 19 + 22 = −4`, y `x = −4 / −1 = 4`. ✔",
            "Verificación en las compras: `4 + 3 + 2 = 9` ✔, `8 + 3 + 6 = 17` ✔, `4 + 6 + 2 = 12` ✔. Errores típicos: olvidar trasponer los cofactores (opción con `−3` y `−2` intercambiados) o no dividir por el determinante negativo (todos los signos cambiados).",
        ],
    },
    # ==================== pc-combinatoria-probabilidad ====================
    {
        "id": "pc-combinatoria-probabilidad-1",
        "node": "pc-combinatoria-probabilidad",
        "kind": "problem",
        "level": 1,
        "title": "La clave del candado de la bici",
        "statement": (
            "Un candado de bicicleta se abre con una clave de **4 dígitos** (del 0 al 9) en la que **no se "
            "repite ningún dígito**; el 0 puede ir en cualquier posición, incluso la primera."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuántas claves posibles hay? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 5040, "tolerance": 0, "unit": ""},
                "answer": "5040 (10 · 9 · 8 · 7)",
            },
            {
                "prompt": "b) ¿Cuántas de esas claves terminan en 0 o en 5? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1008, "tolerance": 0, "unit": ""},
                "answer": "1008 (2 · 9 · 8 · 7)",
            },
            {
                "prompt": "c) Si la clave se eligió al azar entre todas las posibles, ¿cuál es la probabilidad de que termine en 0 o en 5? Respondé solo con el número en decimal.",
                "check": {"type": "numeric", "value": 0.2, "tolerance": 0, "unit": ""},
                "answer": "0.2 (1008 / 5040)",
            },
        ],
        "hints": [
            "El orden de los dígitos importa (1234 no es 4321) y no se repiten: son permutaciones `10P4`.",
            "Cuando hay una restricción, empezá a llenar por la posición restringida (la última).",
        ],
        "solution": [
            "Sin repetición y con orden: `10P4 = 10 · 9 · 8 · 7 = 5040` claves.",
            "Terminadas en 0 o 5: para la última posición hay 2 opciones; quedan 9 dígitos para las otras tres posiciones: `9 · 8 · 7 = 504`. Total `2 · 504 = 1008`.",
            "Probabilidad: `1008 / 5040 = 1/5 = 0.2`.",
            "Control intuitivo: por simetría, el último dígito es cualquiera de los 10 con igual probabilidad, y 2 de 10 son favorables → `2/10 = 0.2`. ✔",
            "Error típico: usar `10⁴ = 10 000` (eso permite repetir dígitos) o combinaciones `10C4 = 210` (eso ignora el orden).",
        ],
    },
    {
        "id": "pc-combinatoria-probabilidad-2",
        "node": "pc-combinatoria-probabilidad",
        "kind": "problem",
        "level": 2,
        "title": "Comisión con condiciones",
        "statement": (
            "En un centro de estudiantes hay `6` mujeres y `4` varones. Se elige al azar una comisión de "
            "`4` personas (sin cargos: solo importa quiénes la forman)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuántas comisiones distintas se pueden formar en total? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 210, "tolerance": 0, "unit": ""},
                "answer": "210 (10C4)",
            },
            {
                "prompt": "b) ¿Cuántas comisiones tienen exactamente 2 mujeres y 2 varones? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 90, "tolerance": 0, "unit": ""},
                "answer": "90 (6C2 · 4C2 = 15 · 6)",
            },
            {
                "prompt": "c) ¿Cuál es la probabilidad de que la comisión elegida tenga exactamente 2 mujeres? Redondeá a 2 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.43, "tolerance": 0.01, "unit": ""},
                "answer": "0.43 (= 3/7)",
            },
        ],
        "hints": [
            "Como no hay cargos, el orden no importa: combinaciones `nCr`.",
            "Para «2 mujeres y 2 varones» elegí por separado las mujeres y los varones y multiplicá (principio del conteo).",
        ],
        "solution": [
            "Total: `10C4 = 10! / (4! · 6!) = (10 · 9 · 8 · 7) / (4 · 3 · 2 · 1) = 5040 / 24 = 210`.",
            "Mujeres: `6C2 = (6 · 5)/2 = 15`. Varones: `4C2 = (4 · 3)/2 = 6`. Comisiones con 2 y 2: `15 · 6 = 90`.",
            "Probabilidad: `90 / 210 = 3/7 ≈ 0.4286 ≈ 0.43`.",
            "Control: las comisiones según cantidad de mujeres (0, 1, 2, 3, 4) son `1, 24, 90, 80, 15`, que suman `210`. ✔",
            "Error típico: usar permutaciones (`10P4 = 5040`) o sumar `15 + 6` en lugar de multiplicar.",
        ],
    },
    {
        "id": "pc-combinatoria-probabilidad-3",
        "node": "pc-combinatoria-probabilidad",
        "kind": "problem",
        "level": 3,
        "title": "Control de calidad por muestreo",
        "statement": (
            "Un lote de `20` piezas tiene `4` defectuosas (no se sabe cuáles). El inspector toma al azar una "
            "muestra de `3` piezas **sin reposición** (todas las muestras de 3 piezas son igualmente "
            "probables).\n\n"
            "El lote se **rechaza** si en la muestra aparecen **2 o más** piezas defectuosas."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuántas muestras distintas de 3 piezas se pueden tomar? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1140, "tolerance": 0, "unit": ""},
                "answer": "1140 (20C3)",
            },
            {
                "prompt": "b) ¿Cuál es la probabilidad de que la muestra tenga al menos una pieza defectuosa? Redondeá a 3 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.509, "tolerance": 0.002, "unit": ""},
                "answer": "0.509 (= 1 − 560/1140 = 29/57)",
            },
            {
                "prompt": "c) ¿Cuál es la probabilidad de que el lote sea rechazado? Redondeá a 3 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.088, "tolerance": 0.01, "unit": ""},
                "answer": "0.088 (= 100/1140 = 5/57)",
            },
        ],
        "hints": [
            "Las muestras son subconjuntos (el orden no importa): contá con `nCr`.",
            "«Al menos una» → complemento: `1 − P(ninguna defectuosa)`. Para «ninguna», las 3 piezas salen de las 16 buenas.",
            "«2 o más» = «exactamente 2» + «exactamente 3», o bien `1 − P(0) − P(1)`.",
        ],
        "solution": [
            "Casos posibles: `20C3 = (20 · 19 · 18) / 6 = 1140`.",
            "Ninguna defectuosa: las 3 salen de las 16 buenas → `16C3 = (16 · 15 · 14) / 6 = 560`. `P(0) = 560/1140 = 28/57 ≈ 0.491`.",
            "Al menos una: `1 − 28/57 = 29/57 ≈ 0.5088 ≈ 0.509`.",
            "Exactamente 2 defectuosas: `4C2 · 16C1 = 6 · 16 = 96`. Exactamente 3: `4C3 = 4`. Rechazo: `(96 + 4)/1140 = 100/1140 = 5/57 ≈ 0.0877 ≈ 0.088`.",
            "Control por complemento: exactamente 1 defectuosa: `4C1 · 16C2 = 4 · 120 = 480`. `560 + 480 + 96 + 4 = 1140` ✔, y `1 − (560 + 480)/1140 = 100/1140` ✔.",
            "Error típico: tratar las extracciones como independientes con `p = 4/20` (con reposición daría `1 − 0.8³ = 0.488`); sin reposición la probabilidad cambia en cada extracción.",
        ],
    },
    # ==================== pc-series-sigma ====================
    {
        "id": "pc-series-sigma-1",
        "node": "pc-series-sigma",
        "kind": "problem",
        "level": 1,
        "title": "Butacas de una tribuna",
        "statement": (
            "La tribuna de un club tiene `20` filas. La primera fila (la más baja) tiene `30` butacas y cada "
            "fila tiene `4` butacas más que la anterior."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuántas butacas tiene la última fila? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 106, "tolerance": 0, "unit": ""},
                "answer": "106 (30 + 19 · 4)",
            },
            {
                "prompt": "b) ¿Cuántas butacas tiene la tribuna en total? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1360, "tolerance": 0, "unit": ""},
                "answer": "1360 (20 · (30 + 106) / 2)",
            },
            {
                "prompt": "c) ¿Cuál de estas sumatorias da el total de butacas?",
                "check": {
                    "type": "choice",
                    "options": [
                        "∑ (26 + 4k), con k desde 1 hasta 20",
                        "∑ (30 + 4k), con k desde 1 hasta 20",
                        "∑ (30 + 4k), con k desde 0 hasta 20",
                        "∑ (30 + 4(k + 1)), con k desde 1 hasta 20",
                    ],
                    "correct": 0,
                },
                "answer": "∑ (26 + 4k), con k desde 1 hasta 20",
            },
        ],
        "hints": [
            "Es una sucesión aritmética: `a_n = a₁ + (n − 1)·d`. De la fila 1 a la 20 hay 19 saltos.",
            "Para la suma usá el truco de Gauss `S_n = n · (a₁ + a_n) / 2`.",
            "Para elegir la sumatoria, probá cada una con `k` en el primer valor y en el último: ¿dan 30 y 106? ¿cuántos términos tiene?",
        ],
        "solution": [
            "Término general: `a_n = 30 + (n − 1)·4 = 26 + 4n`. Última fila: `a₂₀ = 30 + 19·4 = 106` butacas.",
            "Total: `S₂₀ = 20 · (30 + 106) / 2 = 10 · 136 = 1360` butacas.",
            "`∑ (26 + 4k)` de 1 a 20 tiene 20 términos, arranca en `26 + 4 = 30` y termina en `26 + 80 = 106`: es la correcta.",
            "`∑ (30 + 4k)` de 1 a 20 arranca en 34 (le suma 4 a cada fila); de 0 a 20 tiene 21 términos; `30 + 4(k + 1)` arranca en 38.",
            "Control con propiedades de la sumatoria: `∑ (26 + 4k) = 20·26 + 4 · (20·21/2) = 520 + 840 = 1360`. ✔",
            "Error típico: calcular la última fila como `30 + 20·4 = 110` (contar 20 saltos en lugar de 19).",
        ],
    },
    {
        "id": "pc-series-sigma-2",
        "node": "pc-series-sigma",
        "kind": "problem",
        "level": 2,
        "title": "Una noticia que se viraliza",
        "statement": (
            "El día 1, una noticia la comparten `5` personas. Cada día siguiente, la cantidad de personas **nuevas** "
            "que la comparten es el doble que la del día anterior (5, 10, 20, …). Suponé que nadie la comparte "
            "dos veces."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuántas personas nuevas la comparten el día 8? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 640, "tolerance": 0, "unit": ""},
                "answer": "640 (5 · 2⁷)",
            },
            {
                "prompt": "b) ¿Cuántas personas la compartieron en total en los primeros 8 días? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1275, "tolerance": 0, "unit": ""},
                "answer": "1275 (5 · (2⁸ − 1))",
            },
            {
                "prompt": "c) ¿En qué día el total acumulado supera por primera vez las 10 000 personas? Respondé solo con el número de día.",
                "check": {"type": "numeric", "value": 11, "tolerance": 0, "unit": ""},
                "answer": "11 (día 10: 5115; día 11: 10 235)",
            },
        ],
        "hints": [
            "Es geométrica con `a₁ = 5` y `r = 2`: el término del día `n` es `a₁ · r^(n − 1)`.",
            "Suma de los primeros `n` términos: `S_n = a₁(1 − rⁿ)/(1 − r)`.",
            "Para el inciso c planteá `S_n > 10 000` y buscá la menor potencia de 2 que alcance.",
        ],
        "solution": [
            "Término del día `n`: `a_n = 5 · 2^(n − 1)`. Día 8: `5 · 2⁷ = 5 · 128 = 640`.",
            "Suma de 8 días: `S₈ = 5 · (1 − 2⁸)/(1 − 2) = 5 · (256 − 1) = 5 · 255 = 1275`.",
            "En general `S_n = 5 · (2ⁿ − 1)`. Queremos `5 · (2ⁿ − 1) > 10 000` → `2ⁿ − 1 > 2000` → `2ⁿ > 2001`.",
            "`2¹⁰ = 1024` no alcanza y `2¹¹ = 2048` sí. Entonces el día buscado es el **11**.",
            "Control: `S₁₀ = 5 · 1023 = 5115` (todavía no) y `S₁₁ = 5 · 2047 = 10 235` (ya supera). ✔",
            "Error típico: confundir el término del día 11 (`5 · 2¹⁰ = 5120`) con el total acumulado, o usar `2ⁿ` en lugar de `2^(n − 1)` para el término general.",
        ],
    },
    {
        "id": "pc-series-sigma-3",
        "node": "pc-series-sigma",
        "kind": "problem",
        "level": 3,
        "title": "Un medicamento que se acumula en el cuerpo",
        "statement": (
            "Un paciente toma cada mañana una dosis de `120 mg` de un medicamento. En 24 horas el cuerpo elimina "
            "el `60%` de lo que había, de modo que al día siguiente queda el `40%`. Suponé que la dosis se "
            "absorbe de inmediato y que al empezar el tratamiento no había medicamento en el cuerpo.\n\n"
            "Llamá `Q_n` a la cantidad en el cuerpo **inmediatamente después** de tomar la dosis número `n`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale Q₅? Redondeá a 2 decimales. Respondé solo con el número en mg.",
                "check": {"type": "numeric", "value": 197.95, "tolerance": 0.0001, "unit": "mg"},
                "answer": "197.95 mg (120 · (1 − 0.4⁵)/0.6 = 197.952)",
            },
            {
                "prompt": "b) Si el tratamiento sigue indefinidamente, ¿a qué valor tiende Q_n? Respondé solo con el número en mg.",
                "check": {"type": "numeric", "value": 200, "tolerance": 0, "unit": "mg"},
                "answer": "200 mg (120 / (1 − 0.4))",
            },
            {
                "prompt": "c) ¿Qué dosis diaria haría falta para que ese valor límite sea 250 mg? Respondé solo con el número en mg.",
                "check": {"type": "numeric", "value": 150, "tolerance": 0, "unit": "mg"},
                "answer": "150 mg (D / 0.6 = 250)",
            },
        ],
        "hints": [
            "Escribí `Q₁`, `Q₂` y `Q₃`: cada dosis vieja se multiplica por 0.4 por cada día que pasó.",
            "`Q_n = 120 + 120·0.4 + 120·0.4² + … + 120·0.4^(n − 1)`: geométrica finita con `r = 0.4`.",
            "Como `|0.4| < 1`, la serie infinita converge a `a₁ / (1 − r)`.",
        ],
        "solution": [
            "`Q₁ = 120`; `Q₂ = 120 + 0.4·120`; `Q₃ = 120 + 0.4·120 + 0.4²·120`. En general `Q_n = ∑ 120 · 0.4^(k − 1)`, con `k` desde 1 hasta `n`.",
            "Geométrica finita con `a₁ = 120`, `r = 0.4`: `Q₅ = 120 · (1 − 0.4⁵)/(1 − 0.4) = 200 · (1 − 0.01024) = 200 · 0.98976 = 197.952 ≈ 197.95 mg`.",
            "Control sumando: `120 + 48 + 19.2 + 7.68 + 3.072 = 197.952`. ✔",
            "Límite: `0.4ⁿ → 0`, así que `Q_n → 120 / (1 − 0.4) = 120 / 0.6 = 200 mg` (nivel de equilibrio).",
            "Para una dosis `D`, el límite es `D / 0.6`. Igualando `D / 0.6 = 250` → `D = 150 mg`.",
            "Interpretación: en equilibrio, lo que se elimina en un día (`60%` de 200 = 120 mg) es igual a la dosis. Error típico: usar `r = 0.6` (la fracción eliminada) en lugar de `0.4` (la que queda).",
        ],
    },
    # ==================== pc-limites-continuidad ====================
    {
        "id": "pc-limites-continuidad-1",
        "node": "pc-limites-continuidad",
        "kind": "problem",
        "level": 1,
        "title": "Agujero y asíntota en la misma función",
        "statement": (
            "Sea `f(x) = (x² − x − 6) / (x² − 9)`, definida para `x ≠ 3` y `x ≠ −3`.\n\n"
            "Estudiá qué pasa con `f` cerca de cada uno de esos dos valores."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale lim(x → 3) f(x)? Respondé con la fracción exacta o redondeado a 2 decimales.",
                "check": {"type": "numeric", "value": 5 / 6, "tolerance": 0.005, "unit": ""},
                "answer": "5/6 ≈ 0.83",
            },
            {
                "prompt": "b) ¿Qué pasa con f(x) cuando x → −3?",
                "check": {
                    "type": "choice",
                    "options": [
                        "El límite no existe: f crece sin cota por un lado y decrece sin cota por el otro (asíntota vertical x = −3)",
                        "El límite existe y vale 1/6 (hay un agujero en x = −3)",
                        "El límite vale 0 porque el denominador se anula",
                    ],
                    "correct": 0,
                },
                "answer": "No existe: asíntota vertical x = −3",
            },
        ],
        "hints": [
            "Factorizá numerador y denominador: un trinomio y una diferencia de cuadrados.",
            "Después de simplificar, mirá en cuál de los dos valores el denominador sigue anulándose y el numerador no.",
        ],
        "solution": [
            "Factorizamos: `x² − x − 6 = (x − 3)(x + 2)` y `x² − 9 = (x − 3)(x + 3)`.",
            "Para `x ≠ 3`: `f(x) = (x + 2)/(x + 3)`.",
            "En `x → 3` había `0/0`; después de simplificar: `lim = (3 + 2)/(3 + 3) = 5/6 ≈ 0.83`. En `x = 3` hay un **agujero**.",
            "En `x → −3`: el numerador simplificado tiende a `−3 + 2 = −1` y el denominador `x + 3` tiende a `0`: forma `−1/0`, el límite no es finito.",
            "Por la derecha (`x + 3 > 0` chico): `f → −∞`. Por la izquierda (`x + 3 < 0`): `f → +∞`. No existe el límite y `x = −3` es **asíntota vertical**.",
            "Error típico: creer que cualquier división por cero «es un agujero»; solo lo es si el factor se cancela (`0/0`).",
        ],
    },
    {
        "id": "pc-limites-continuidad-2",
        "node": "pc-limites-continuidad",
        "kind": "problem",
        "level": 2,
        "title": "Racionalizar y factorizar cubos",
        "statement": "Calculá los siguientes dos límites, que en sustitución directa dan `0/0`.",
        "parts": [
            {
                "prompt": "a) lim(x → 5) (√(x + 4) − 3) / (x − 5). Respondé con la fracción exacta o redondeado a 3 decimales.",
                "check": {"type": "numeric", "value": 1 / 6, "tolerance": 0.005, "unit": ""},
                "answer": "1/6 ≈ 0.167",
            },
            {
                "prompt": "b) lim(x → 2) (x³ − 8) / (x² − 4). Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3 (12 / 4)",
            },
        ],
        "hints": [
            "Para el a, multiplicá numerador y denominador por el conjugado `√(x + 4) + 3`.",
            "Para el b, `x³ − 8` es una diferencia de cubos: `a³ − b³ = (a − b)(a² + ab + b²)`.",
        ],
        "solution": [
            "a) Sustitución: `(√9 − 3)/0 = 0/0`. Multiplicamos por el conjugado: `(√(x + 4) − 3)(√(x + 4) + 3) = (x + 4) − 9 = x − 5`.",
            "Queda `(x − 5) / ((x − 5)(√(x + 4) + 3)) = 1 / (√(x + 4) + 3)` para `x ≠ 5`. Límite: `1/(3 + 3) = 1/6 ≈ 0.167`.",
            "b) Sustitución: `(8 − 8)/(4 − 4) = 0/0`. Factorizamos: `x³ − 8 = (x − 2)(x² + 2x + 4)` y `x² − 4 = (x − 2)(x + 2)`.",
            "Simplificando: `(x² + 2x + 4)/(x + 2)`. Límite: `(4 + 4 + 4)/(2 + 2) = 12/4 = 3`.",
            "Control numérico: con `x = 5.001`, el cociente del a da `≈ 0.16666`; con `x = 2.001`, el del b da `≈ 3.0008`. ✔",
            "Error típico: «distribuir» la raíz (`√(x + 4) = √x + 2`) o factorizar `x³ − 8` como `(x − 2)³`.",
        ],
    },
    {
        "id": "pc-limites-continuidad-3",
        "node": "pc-limites-continuidad",
        "kind": "problem",
        "level": 3,
        "title": "Elegir parámetros para que una función partida sea continua",
        "statement": (
            "Sea `f` definida en `[−2, +∞)` por tramos:\n\n"
            "- `f(x) = (x − 2) / (√(x + 2) − 2)` si `−2 ≤ x < 2`\n"
            "- `f(x) = a·x + b` si `2 ≤ x ≤ 5`\n"
            "- `f(x) = (x² − 3x − 10) / (x − 5)` si `x > 5`\n\n"
            "Hallá `a` y `b` para que `f` sea continua en todo su dominio."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale lim(x → 2⁻) f(x)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4 (√(x + 2) + 2 → 4)",
            },
            {
                "prompt": "b) ¿Cuánto vale a? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1",
            },
            {
                "prompt": "c) ¿Cuánto vale b? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
        ],
        "hints": [
            "Cada tramo es continuo en su propio intervalo: el problema está solo en los puntos de unión `x = 2` y `x = 5`.",
            "En el primer tramo racionalizá el denominador; en el tercero factorizá el numerador.",
            "Continuidad en cada unión: límite lateral de afuera = valor del tramo del medio. Te quedan dos ecuaciones con `a` y `b`.",
        ],
        "solution": [
            "Primer tramo: multiplicamos por el conjugado `√(x + 2) + 2`: `(x − 2)(√(x + 2) + 2) / ((x + 2) − 4) = (x − 2)(√(x + 2) + 2)/(x − 2) = √(x + 2) + 2` (para `x ≠ 2`). Entonces `lim(x → 2⁻) f(x) = √4 + 2 = 4`.",
            "Tercer tramo: `x² − 3x − 10 = (x − 5)(x + 2)`, así que para `x > 5`, `f(x) = x + 2` y `lim(x → 5⁺) f(x) = 7`.",
            "Continuidad en `x = 2`: `f(2) = 2a + b` debe ser igual a 4 (el límite por derecha también es `2a + b`). Ecuación: `2a + b = 4`.",
            "Continuidad en `x = 5`: `f(5) = 5a + b` debe ser igual a 7. Ecuación: `5a + b = 7`.",
            "Restando: `3a = 3` → `a = 1`; luego `b = 4 − 2 = 2`. El tramo del medio es `f(x) = x + 2`.",
            "Verificación: en `x = 2`, `f(2) = 4` = límite izquierdo ✔; en `x = 5`, `f(5) = 7` = límite derecho ✔. En los demás puntos cada tramo es continuo (el denominador del primero solo se anula en `x = 2`, que no está en su intervalo).",
            "Error típico: igualar los valores de los tramos de afuera evaluando directamente en `x = 2` o `x = 5` (da `0/0`) en lugar de calcular primero los límites.",
        ],
    },
]
