"""Borrador: ejercicios del material oficial del ingreso (UNCuyo 2027), Física U4 (Estática) y U5 (Dinámica).

Fuentes:
  - Práctica del curso U4 y U5 (con solucionario).
  - Guía TP 4.1 parte B y Guía TP5 parte B (con grilla de respuestas).
  - Vallone, Trabajos Prácticos, U5 (estática), ej. 10 a 13 (sin respuestas).
  - Vallone, Apuntes Teóricos: ejemplos resueltos de resultante con momentos y de cupla.

Convención: g = 9,8 m/s² salvo que el enunciado diga otra cosa (algunos ítems de TP5 B usan g = 10).
Ángulos de dirección: medidos desde el semieje x positivo, en sentido antihorario.
"""

from __future__ import annotations

EXERCISES: list[dict] = [
    # ======================================================================
    # UNIDAD 4 · PRÁCTICA DEL CURSO
    # ======================================================================
    {
        "id": "f-estatica-concurrentes-u4-1",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 2,
        "source": "Física · Práctica U4, ej. 1",
        "title": "Cuerpo tironeado por tres cuerdas",
        "statement": (
            "Sabiendo que α = 50°, determinar la resultante de las fuerzas aplicadas al cuerpo de peso 200 N "
            "(módulo y dirección) y la equilibrante del sistema de fuerzas.\n\n"
            "Descripción de la figura: un cuerpo apoyado (el piso no se tiene en cuenta en el sistema) del que tiran "
            "tres cuerdas que concurren en un mismo punto:\n"
            "- 160 N hacia arriba y a la izquierda, formando α = 50° con la horizontal (dirección 130°).\n"
            "- 140 N hacia arriba y a la derecha, formando α = 50° con la horizontal (dirección 50°).\n"
            "- 60 N hacia arriba, formando 35° con la cuerda de 140 N (dirección 85°).\n"
            "Además actúa el peso del cuerpo, 200 N vertical hacia abajo (dirección 270°).\n"
            "Las direcciones se miden desde el semieje x positivo en sentido antihorario."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el módulo de la resultante? Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 89.9, "tolerance": 0.01, "unit": "N"},
                "answer": "89,9 N",
            },
            {
                "prompt": "b) ¿Qué dirección tiene la resultante (ángulo desde el semieje x positivo, antihorario)? Respondé solo con el número en grados decimales, con un decimal.",
                "check": {"type": "numeric", "value": 94.9, "tolerance": 0.002, "unit": "°"},
                "answer": "94,9° (≈ 94°52´)",
            },
            {
                "prompt": "c) ¿Qué dirección tiene la equilibrante? Respondé solo con el número en grados decimales, con un decimal.",
                "check": {"type": "numeric", "value": 274.9, "tolerance": 0.001, "unit": "°"},
                "answer": "274,9° (≈ 274°52´), con módulo 89,9 N",
            },
        ],
        "hints": [
            "Proyectá cada fuerza: `Fx = F·cos α` y `Fy = F·sen α`, usando el ángulo medido desde +x. No te olvides del peso.",
            "La resultante tiene `Rx` negativo y `Ry` positivo: está en el segundo cuadrante, así que al ángulo que te da la calculadora con `arctg(Ry/Rx)` tenés que corregirlo.",
            "La equilibrante tiene el mismo módulo que la resultante y sentido opuesto: su dirección es la de R más 180°.",
        ],
        "solution": [
            "Nota: la hoja de ejercicios no dice que el cuerpo pesa 200 N; ese dato está en la teoría y en el solucionario, y hay que incluirlo.",
            "Proyecciones en x: `160·cos 130° = −102,85 N`; `140·cos 50° = 89,99 N`; `60·cos 85° = 5,23 N`; peso: `0`. `Rx = −7,63 N`.",
            "Proyecciones en y: `160·sen 130° = 122,57 N`; `140·sen 50° = 107,25 N`; `60·sen 85° = 59,77 N`; peso: `−200 N`. `Ry = 89,59 N`.",
            "Módulo: `|R| = √(7,63² + 89,59²) ≈ 89,9 N`.",
            "Dirección: `arctg(89,59/7,63) ≈ 85,13°`; como `Rx < 0` y `Ry > 0`, R está en el 2.º cuadrante: `β = 180° − 85,13° = 94,87° ≈ 94,9°` (94°52´).",
            "Equilibrante: `|E| = |R| = 89,9 N` y `ρ = 94,87° + 180° = 274,87° ≈ 274,9°` (274°52´), como el solucionario.",
        ],
    },
    {
        "id": "f-estatica-concurrentes-u4-2",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 2,
        "source": "Física · Práctica U4, ej. 2",
        "title": "Dos remolcadores y una barcaza",
        "statement": (
            "Dos remolcadores aplican las fuerzas P y Q a la barcaza, donde P = 76 kN y Q = 52 kN. Determine la "
            "resultante de P y Q.\n\n"
            "Descripción de la figura (vista desde arriba, x hacia la derecha, y hacia arriba): la cuerda del "
            "remolcador que ejerce P va desde la barcaza hasta un punto ubicado 16 m a la izquierda y 32 m hacia "
            "arriba; la del remolcador que ejerce Q va hasta un punto ubicado 24 m a la derecha y 12 m hacia abajo. "
            "Cada fuerza tiene la dirección de su cuerda, alejándose de la barcaza."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el módulo de la resultante? Respondé solo con el número en kN, con un decimal.",
                "check": {"type": "numeric", "value": 46.4, "tolerance": 0.01, "unit": "kN"},
                "answer": "46,4 kN",
            },
            {
                "prompt": "b) ¿Qué ángulo forma la resultante con el semieje x positivo (antihorario)? Respondé solo con el número en grados decimales, con un decimal.",
                "check": {"type": "numeric", "value": 74.4, "tolerance": 0.01, "unit": "°"},
                "answer": "74,4° (≈ 74°22´)",
            },
        ],
        "hints": [
            "No tenés los ángulos, pero sí los catetos: la longitud de cada cuerda sale por Pitágoras, y `cos` y `sen` salen como cateto/hipotenusa.",
            "Para P: hipotenusa `√(16² + 32²)`; `Px` es negativa y `Py` positiva. Para Q: hipotenusa `√(24² + 12²)`; `Qx` positiva y `Qy` negativa.",
        ],
        "solution": [
            "Cuerda de P: `√(16² + 32²) = 35,78 m`. `Px = −76·16/35,78 = −33,99 kN`; `Py = 76·32/35,78 = 67,98 kN`.",
            "Cuerda de Q: `√(24² + 12²) = 26,83 m`. `Qx = 52·24/26,83 = 46,51 kN`; `Qy = −52·12/26,83 = −23,26 kN`.",
            "Sumamos: `Rx = −33,99 + 46,51 = 12,52 kN`; `Ry = 67,98 − 23,26 = 44,72 kN`.",
            "Módulo: `|R| = √(12,52² + 44,72²) ≈ 46,4 kN`.",
            "Dirección: ambas componentes positivas (1.er cuadrante): `α = arctg(44,72/12,52) ≈ 74,4°` (74°22´), igual que el solucionario.",
        ],
    },
    {
        "id": "f-estatica-concurrentes-u4-3",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 2,
        "source": "Física · Práctica U4, ej. 3",
        "title": "Conexión con cuatro fuerzas",
        "statement": (
            "Dos fuerzas P = 9800 N y Q = 14 700 N se aplican a la conexión que se muestra en la figura. Si el sistema "
            "está en equilibrio, determinar las fuerzas T1 y T2.\n\n"
            "Descripción de la figura (las cuatro fuerzas concurren en un punto):\n"
            "- P: vertical hacia abajo.\n"
            "- Q: hacia la izquierda y hacia arriba, 15° por encima de la horizontal (dirección 165°).\n"
            "- T1: horizontal hacia la derecha (dirección 0°).\n"
            "- T2: hacia arriba y a la derecha, formando 60° con T1 (dirección 60°)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale T1? Respondé solo con el número en N, redondeado a unidades.",
                "check": {"type": "numeric", "value": 10738, "tolerance": 0.01, "unit": "N"},
                "answer": "10738 N",
            },
            {
                "prompt": "b) ¿Cuánto vale T2? Respondé solo con el número en N, redondeado a unidades.",
                "check": {"type": "numeric", "value": 6923, "tolerance": 0.01, "unit": "N"},
                "answer": "6923 N",
            },
        ],
        "hints": [
            "Planteá `ΣFx = 0` y `ΣFy = 0`. En la ecuación en y aparece solo T2 (T1 es horizontal).",
            "En y: `T2·sen 60° + Q·sen 15° − P = 0`. Con T2, la ecuación en x te da T1.",
        ],
        "solution": [
            "Equilibrio de un sistema concurrente: `ΣFx = 0` y `ΣFy = 0`.",
            "En y: `T2·sen 60° + Q·sen 15° − P = 0` → `T2 = (9800 − 14 700·0,2588)/0,8660 = (9800 − 3804,6)/0,8660 ≈ 6923 N`.",
            "En x: `T1 + T2·cos 60° − Q·cos 15° = 0` → `T1 = 14 700·0,9659 − 6923·0,5 = 14 199 − 3461 ≈ 10 738 N`.",
            "El solucionario da `T1 = 10 738 N` y `T2 = 6922,2 N` (diferencia de redondeo; el valor exacto es 6922,8 N).",
        ],
    },
    {
        "id": "f-estatica-concurrentes-u4-4a",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 1,
        "source": "Física · Práctica U4, ej. 4 (nudo inferior)",
        "title": "Cuerpo colgado de dos nudos (I)",
        "statement": (
            "El objeto de la figura está en equilibrio. El cuerpo que cuelga tiene un peso Fw = 80,0 N.\n\n"
            "Descripción de la figura: el cuerpo cuelga de un nudo inferior. De ese nudo salen la cuerda T1, horizontal "
            "hacia la izquierda hasta una pared vertical, y la cuerda T2, que sube hacia la derecha formando 25° con la "
            "vertical hasta un nudo superior. Del nudo superior salen la cuerda T3, horizontal hacia la izquierda hasta "
            "la pared, y la cuerda T4, que sube hacia la derecha formando 55° con la vertical hasta el techo.\n\n"
            "En este problema trabajá con el nudo inferior: encontrá T1 y T2."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale T2? Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 88.3, "tolerance": 0.01, "unit": "N"},
                "answer": "88,3 N",
            },
            {
                "prompt": "b) ¿Cuánto vale T1? Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 37.3, "tolerance": 0.01, "unit": "N"},
                "answer": "37,3 N",
            },
        ],
        "hints": [
            "Hacé el DCL del nudo inferior: Fw hacia abajo, T1 horizontal y T2 inclinada 25° respecto de la vertical.",
            "Como el ángulo está medido desde la vertical, la componente vertical de T2 es `T2·cos 25°`.",
        ],
        "solution": [
            "DCL del nudo inferior: Fw = 80,0 N hacia abajo, T1 hacia la izquierda y T2 hacia arriba a la derecha, a 25° de la vertical.",
            "`ΣFy = 0`: `T2·cos 25° − 80,0 = 0` → `T2 = 80,0/0,9063 ≈ 88,3 N`.",
            "`ΣFx = 0`: `T2·sen 25° − T1 = 0` → `T1 = 88,27·0,4226 ≈ 37,3 N`.",
            "Coincide con el solucionario (T1 = 37,3 N; T2 = 88,3 N).",
        ],
    },
    {
        "id": "f-estatica-concurrentes-u4-4b",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 2,
        "source": "Física · Práctica U4, ej. 4 (nudo superior)",
        "title": "Cuerpo colgado de dos nudos (II)",
        "statement": (
            "El objeto de la figura está en equilibrio. El cuerpo que cuelga tiene un peso Fw = 80,0 N.\n\n"
            "Descripción de la figura: el cuerpo cuelga de un nudo inferior. De ese nudo salen la cuerda T1, horizontal "
            "hacia la izquierda hasta una pared vertical, y la cuerda T2, que sube hacia la derecha formando 25° con la "
            "vertical hasta un nudo superior. Del nudo superior salen la cuerda T3, horizontal hacia la izquierda hasta "
            "la pared, y la cuerda T4, que sube hacia la derecha formando 55° con la vertical hasta el techo.\n\n"
            "Encontrá T4 y T3 (si te hace falta, T1 = 37,3 N y T2 = 88,3 N salen del nudo inferior)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale T4? Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 139.5, "tolerance": 0.01, "unit": "N"},
                "answer": "139,5 N",
            },
            {
                "prompt": "b) ¿Cuánto vale T3? Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 76.9, "tolerance": 0.01, "unit": "N"},
                "answer": "76,9 N",
            },
        ],
        "hints": [
            "En el DCL del nudo superior, T2 aparece tirando hacia abajo y a la izquierda (es la misma cuerda que en el nudo inferior).",
            "La componente vertical de T2 es igual a Fw: eso simplifica la ecuación en y del nudo superior.",
        ],
        "solution": [
            "DCL del nudo superior: T4 hacia arriba a la derecha (55° de la vertical), T3 horizontal hacia la izquierda y T2 hacia abajo a la izquierda (25° de la vertical).",
            "`ΣFy = 0`: `T4·cos 55° − T2·cos 25° = 0`. Como `T2·cos 25° = 80,0 N`, `T4 = 80,0/0,5736 ≈ 139,5 N`.",
            "`ΣFx = 0`: `T4·sen 55° − T3 − T2·sen 25° = 0` → `T3 = 139,48·0,8192 − 37,30 = 114,26 − 37,30 ≈ 76,9 N`.",
            "El solucionario da T3 = 76,95 N y T4 = 139,5 N (coincide).",
        ],
    },
    {
        "id": "f-momento-cupla-vinculos-u4-5",
        "node": "f-momento-cupla-vinculos",
        "kind": "problem",
        "level": 1,
        "source": "Física · Práctica U4, ej. 5",
        "title": "Momento de una fuerza en tres casos",
        "statement": (
            "Calcule el momento de la fuerza en N·m respecto a O para las siguientes situaciones (positivo el sentido "
            "antihorario). En los tres casos hay una barra horizontal con el punto O en su extremo izquierdo y la "
            "fuerza aplicada en el extremo derecho, a una distancia d de O:\n"
            "a) d = 45 cm; F = 34 N, vertical hacia abajo.\n"
            "b) d = 58 cm; F = 42 N, horizontal hacia la derecha (en la dirección de la barra).\n"
            "c) d = 4 m; F = 78 N, hacia arriba y a la derecha, formando α = 30° con la prolongación de la barra."
        ),
        "parts": [
            {
                "prompt": "a) Momento respecto de O en el caso a). Respondé solo con el número en N·m, con su signo.",
                "check": {"type": "numeric", "value": -15.3, "tolerance": 0.01, "unit": "N·m"},
                "answer": "−15,3 N·m (horario)",
            },
            {
                "prompt": "b) Momento respecto de O en el caso b). Respondé solo con el número en N·m.",
                "check": {"type": "numeric", "value": 0, "tolerance": 0, "unit": "N·m"},
                "answer": "0 N·m: la recta de acción pasa por O",
            },
            {
                "prompt": "c) Momento respecto de O en el caso c). Respondé solo con el número en N·m, con su signo.",
                "check": {"type": "numeric", "value": 156, "tolerance": 0.01, "unit": "N·m"},
                "answer": "156 N·m (antihorario)",
            },
        ],
        "hints": [
            "`M = F·d`, donde d es la distancia de O a la RECTA DE ACCIÓN de la fuerza; pasá los cm a m.",
            "Si la recta de acción pasa por O, el momento es nulo. En c), solo la componente perpendicular a la barra hace girar: `F·sen 30°`.",
        ],
        "solution": [
            "a) La fuerza es perpendicular a la barra: `M = −34 N · 0,45 m = −15,3 N·m`. Es negativo porque, hacia abajo en el extremo derecho, hace girar en sentido horario.",
            "b) La fuerza tiene la dirección de la barra, así que su recta de acción pasa por O: la distancia es 0 y `M = 0`.",
            "c) Descomponemos F: la componente a lo largo de la barra (`78·cos 30°`) pasa por O y no da momento; la perpendicular vale `78·sen 30° = 39 N`.",
            "`M = 39 N · 4 m = +156 N·m` (hacia arriba en el extremo derecho: giro antihorario).",
            "Coincide con el solucionario: a) −15,3 N·m; b) 0; c) 156 N·m.",
        ],
    },
    {
        "id": "f-momento-cupla-vinculos-u4-6",
        "node": "f-momento-cupla-vinculos",
        "kind": "problem",
        "level": 2,
        "source": "Física · Práctica U4, ej. 6",
        "title": "Resultante y momento en una pieza en T",
        "statement": (
            "Observe la gráfica. a) Calcule módulo y dirección de la resultante del sistema de fuerzas. b) Calcule el "
            "momento resultante respecto a C.\n\n"
            "Descripción de la figura: una pieza rígida formada por una barra horizontal con los puntos B, C, D y E "
            "(de izquierda a derecha) y un brazo vertical que sube 10 m desde C hasta el punto A. B está 8 m a la "
            "izquierda de C, D está 6 m a la derecha de C y E está 6 m a la derecha de D. Fuerzas:\n"
            "- F_A = 100 N en A, horizontal hacia la izquierda.\n"
            "- F_D = 300 N en D, vertical hacia abajo.\n"
            "- F_E = 200 N en E, vertical hacia arriba.\n"
            "Tomá positivo el sentido antihorario para los momentos."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el módulo de la resultante? Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 141.4, "tolerance": 0.01, "unit": "N"},
                "answer": "141,4 N",
            },
            {
                "prompt": "b) ¿Qué dirección tiene la resultante (ángulo desde el semieje x positivo, antihorario)? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 225, "tolerance": 0.001, "unit": "°"},
                "answer": "225°",
            },
            {
                "prompt": "c) ¿Cuánto vale el momento resultante respecto de C? Respondé solo con el número en N·m, con su signo.",
                "check": {"type": "numeric", "value": 1600, "tolerance": 0.01, "unit": "N·m"},
                "answer": "1600 N·m (antihorario)",
            },
        ],
        "hints": [
            "Para la resultante solo importan módulos y direcciones: `Rx = −100 N` y `Ry = 200 − 300`.",
            "Para los momentos respecto de C: la distancia de F_A a C es la altura del brazo (10 m); la de F_D y F_E es su distancia horizontal a C.",
            "Pensá el sentido de giro de cada fuerza alrededor de C: una fuerza hacia la izquierda aplicada ARRIBA de C hace girar en sentido antihorario.",
        ],
        "solution": [
            "Componentes: `Rx = −100 N`; `Ry = +200 − 300 = −100 N`.",
            "Módulo: `|R| = √(100² + 100²) ≈ 141,4 N`. Ambas componentes negativas: 3.er cuadrante, `α = 180° + 45° = 225°`.",
            "Momento de F_A respecto de C: brazo 10 m, empuja hacia la izquierda por encima de C → antihorario: `+100·10 = +1000 N·m`.",
            "Momento de F_E: brazo 12 m, hacia arriba a la derecha de C → antihorario: `+200·12 = +2400 N·m`. Momento de F_D: brazo 6 m, hacia abajo a la derecha de C → horario: `−300·6 = −1800 N·m`.",
            "`M_C = 1000 + 2400 − 1800 = +1600 N·m`: la pieza giraría en sentido antihorario. Coincide con el solucionario.",
        ],
    },
    {
        "id": "f-momento-cupla-vinculos-u4-7",
        "node": "f-momento-cupla-vinculos",
        "kind": "problem",
        "level": 3,
        "source": "Física · Práctica U4, ej. 7",
        "title": "Viga con apoyo móvil y articulación",
        "statement": (
            "Calcule las reacciones de vínculo del siguiente sistema en equilibrio, tomando como despreciable el peso de "
            "la barra (no se tiene en cuenta coeficiente de seguridad).\n\n"
            "Descripción de la figura: barra horizontal AB de 5,00 m. En A hay un apoyo móvil (su reacción es "
            "vertical) y en B una articulación fija. Sobre la barra actúan:\n"
            "- F1 = 2 t, vertical hacia abajo, a 1,00 m de A.\n"
            "- F2 = 4 t, a 4,00 m de A (1,00 m antes de B), inclinada: empuja la barra hacia abajo y hacia la izquierda, "
            "y su recta de acción forma 60° con la barra (dirección 240°).\n"
            "(t = tonelada fuerza.)"
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la reacción en A? Respondé solo con el número en t, con dos decimales.",
                "check": {"type": "numeric", "value": 2.29, "tolerance": 0.01, "unit": "t"},
                "answer": "2,29 t (vertical, hacia arriba)",
            },
            {
                "prompt": "b) ¿Cuál es el módulo de la reacción en B? Respondé solo con el número en t, con dos decimales.",
                "check": {"type": "numeric", "value": 3.75, "tolerance": 0.015, "unit": "t"},
                "answer": "3,75 t",
            },
            {
                "prompt": "c) ¿Qué ángulo forma la reacción en B con la horizontal (semieje x positivo)? Respondé solo con el número en grados decimales, con un decimal.",
                "check": {"type": "numeric", "value": 57.8, "tolerance": 0.01, "unit": "°"},
                "answer": "57,8° (hacia arriba y a la derecha)",
            },
        ],
        "hints": [
            "Descomponé F2: `F2x = −4·cos 60° = −2 t` y `F2y = −4·sen 60° ≈ −3,46 t`.",
            "Tomá momentos respecto de B: así se eliminan las dos componentes de R_B y queda solo R_A como incógnita.",
            "La componente horizontal de F2 solo la puede equilibrar la articulación B (el apoyo móvil no tiene reacción horizontal).",
        ],
        "solution": [
            "Incógnitas: `R_A` (vertical), `R_Bx` y `R_By`. Componentes de F2: `−2 t` en x y `−3,464 t` en y.",
            "`ΣM_B = 0` (antihorario +): R_A, hacia arriba a 5 m a la izquierda de B, gira en sentido horario: `−R_A·5 + 2·4 + 3,464·1 = 0` → `R_A = 11,464/5 ≈ 2,29 t`.",
            "`ΣFy = 0`: `R_A + R_By − 2 − 3,464 = 0` → `R_By ≈ 3,17 t`. `ΣFx = 0`: `R_Bx − 2 = 0` → `R_Bx = 2 t`.",
            "`|R_B| = √(2² + 3,17²) ≈ 3,75 t`; `α = arctg(3,17/2) ≈ 57,8°` (57°46´).",
            "El solucionario da |Ra| = 2,3 t, |Rb| = 3,8 t y α = 57°59´: redondea R_By a 3,2 t antes de calcular el ángulo (`arctg 1,6 = 57,99°`). Sin redondear, el ángulo es 57,8°.",
            "Ojo con los vínculos: en la figura el apoyo de A tiene doble raya (móvil) y el de B no (fijo). Si se invirtieran (A fijo, B móvil) saldría R_B = 3,17 t vertical y |R_A| ≈ 3,04 t, que no coincide con el solucionario.",
        ],
    },
    {
        "id": "f-momento-cupla-vinculos-u4-8",
        "node": "f-momento-cupla-vinculos",
        "kind": "problem",
        "level": 3,
        "source": "Física · Práctica U4, ej. 8",
        "title": "Barra articulada con cuerda horizontal",
        "statement": (
            "La barra de la figura está en equilibrio, tiene un peso de 800 N, una longitud L y sostiene en su extremo "
            "una caja de 300 N de peso.\n\n"
            "Descripción de la figura: la barra (homogénea) está articulada en su extremo superior A a una pared "
            "vertical y baja hacia la derecha formando 40° con la pared. Del extremo inferior cuelga la caja, y en ese "
            "mismo extremo está atada una cuerda horizontal que va hacia la derecha hasta otra pared.\n\n"
            "a) Calcule el módulo de la reacción de la articulación, R_A. b) Calcule la dirección (ángulo) de R_A. "
            "c) ¿Cuál es la tensión de la cuerda horizontal que sostiene la barra?"
        ),
        "parts": [
            {
                "prompt": "a) Módulo de R_A. Respondé solo con el número en N, redondeado a unidades.",
                "check": {"type": "numeric", "value": 1247, "tolerance": 0.01, "unit": "N"},
                "answer": "1247 N",
            },
            {
                "prompt": "b) Dirección de R_A, medida desde el semieje x positivo en sentido antihorario. Respondé solo con el número en grados decimales, con un decimal.",
                "check": {"type": "numeric", "value": 118.1, "tolerance": 0.002, "unit": "°"},
                "answer": "118,1° (≈ 118°6´)",
            },
            {
                "prompt": "c) Tensión de la cuerda horizontal. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 587.4, "tolerance": 0.01, "unit": "N"},
                "answer": "587,4 N",
            },
        ],
        "hints": [
            "Tomá momentos respecto de A: la reacción de la articulación no aparece y te queda solo T como incógnita.",
            "Brazos respecto de A: los pesos (verticales) tienen brazo horizontal (`L/2·sen 40°` y `L·sen 40°`); la tensión (horizontal) tiene brazo vertical `L·cos 40°`. L se simplifica.",
            "Con T, las ecuaciones de fuerzas te dan `R_Ax` y `R_Ay`. Fijate en qué cuadrante queda R_A.",
        ],
        "solution": [
            "Fuerzas: peso de la barra 800 N en su punto medio, caja 300 N en el extremo inferior, T horizontal hacia la derecha en el extremo inferior y R_A en la articulación.",
            "`ΣM_A = 0`: `T·L·cos 40° − 800·(L/2)·sen 40° − 300·L·sen 40° = 0` → `T = 700·tg 40° ≈ 587,4 N`.",
            "`ΣFx = 0`: `R_Ax + 587,4 = 0` → `R_Ax = −587,4 N`. `ΣFy = 0`: `R_Ay − 800 − 300 = 0` → `R_Ay = 1100 N`.",
            "`|R_A| = √(587,4² + 1100²) ≈ 1247 N`.",
            "R_A está en el 2.º cuadrante: `arctg(1100/587,4) = 61,9°`, así que `α = 180° − 61,9° = 118,1°` (118°6´). Coincide con el solucionario.",
        ],
    },
    {
        "id": "f-momento-cupla-vinculos-u4-9",
        "node": "f-momento-cupla-vinculos",
        "kind": "problem",
        "level": 3,
        "source": "Física · Práctica U4, ej. 9",
        "title": "Viga articulada que sostiene una carga",
        "statement": (
            "Calcular del siguiente sistema la tensión T y la reacción en la articulación A, conocido el peso de la "
            "viga que es igual a 580 N. La viga forma un ángulo de 50° respecto a la pared. La longitud de la viga es "
            "L, y la cuerda que ejerce una tensión T en la barra para sostenerla está aplicada a una distancia de ¾ L "
            "respecto a A. El sistema está en equilibrio.\n\n"
            "Descripción de la figura: A es el extremo inferior de la viga (homogénea), articulado a una pared "
            "vertical; la viga sube hacia la derecha. La cuerda es horizontal y va desde la viga hasta la pared. Del "
            "extremo superior de la viga cuelga un cuerpo de 450 N."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale T? Respondé solo con el número en N, redondeado a unidades.",
                "check": {"type": "numeric", "value": 1176, "tolerance": 0.01, "unit": "N"},
                "answer": "1176 N",
            },
            {
                "prompt": "b) ¿Cuál es el módulo de la reacción en A? Respondé solo con el número en N, redondeado a unidades.",
                "check": {"type": "numeric", "value": 1563, "tolerance": 0.01, "unit": "N"},
                "answer": "1563 N",
            },
            {
                "prompt": "c) ¿Qué ángulo forma R_A con el semieje x positivo? Respondé solo con el número en grados decimales, con un decimal.",
                "check": {"type": "numeric", "value": 41.2, "tolerance": 0.01, "unit": "°"},
                "answer": "41,2° (≈ 41°13´)",
            },
        ],
        "hints": [
            "Momentos respecto de A. Los pesos tienen brazo horizontal (`L/2·sen 50°` y `L·sen 50°`); la cuerda, horizontal, tiene brazo vertical `¾L·cos 50°`.",
            "La cuerda tira hacia la pared (izquierda); la articulación tiene que empujar hacia la derecha y hacia arriba.",
        ],
        "solution": [
            "Fuerzas sobre la viga: 580 N en su punto medio, 450 N en el extremo, T horizontal hacia la pared (izquierda) a ¾L de A, y R_A.",
            "`ΣM_A = 0`: `T·(¾L)·cos 50° − 580·(L/2)·sen 50° − 450·L·sen 50° = 0` → `T = (290 + 450)·tg 50°/0,75 ≈ 1176 N`.",
            "`ΣFx = 0`: `R_Ax − T = 0` → `R_Ax = 1176 N`. `ΣFy = 0`: `R_Ay = 580 + 450 = 1030 N`.",
            "`|R_A| = √(1176² + 1030²) ≈ 1563 N`; `α = arctg(1030/1176) ≈ 41,2168°` (41°13´; el solucionario da 41°12´ porque convierte 41,2° ya redondeado).",
            "Coincide con el solucionario (T = 1176 N; |Ra| = 1563,3 N; α = 41°12´). Ojo: el enunciado no menciona el cuerpo de 450 N, pero está en la figura y el solucionario lo usa.",
        ],
    },
    {
        "id": "f-estatica-concurrentes-u4-10",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 2,
        "source": "Física · Práctica U4, ej. 10",
        "title": "Esfera entre pared y plano inclinado",
        "statement": (
            "Si la esfera homogénea de 5 kg se encuentra en equilibrio, determine la reacción en el punto P.\n\n"
            "Descripción de la figura: la esfera está apoyada en una pared vertical (a su izquierda; el punto de "
            "contacto es P) y sobre un plano inclinado 45° respecto de la horizontal, sin rozamiento."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la reacción de la pared en P? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 49, "tolerance": 0.01, "unit": "N"},
                "answer": "49 N, horizontal",
            },
            {
                "prompt": "b) ¿Cuánto vale la reacción normal del plano inclinado? Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 69.3, "tolerance": 0.01, "unit": "N"},
                "answer": "69,3 N",
            },
            {
                "prompt": "c) ¿Qué tipo de sistema de fuerzas se estudia y cuáles son las reacciones de vínculo?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Concurrente; las reacciones de vínculo son la normal de la pared y la normal del plano",
                        "No concurrente; la única reacción de vínculo es la normal del plano",
                        "Concurrente; no hay reacciones de vínculo, solo el peso",
                        "No concurrente; las reacciones de vínculo son el peso y la normal de la pared",
                    ],
                    "correct": 0,
                },
                "answer": "Concurrente: las tres fuerzas pasan por el centro de la esfera; los vínculos son la pared y el plano.",
            },
        ],
        "hints": [
            "Las tres fuerzas (peso y las dos normales) pasan por el centro de la esfera. La normal de la pared es horizontal; la del plano es perpendicular a él, o sea, forma 45° con la vertical.",
            "En y solo hay dos fuerzas: el peso y la componente vertical de la normal del plano.",
        ],
        "solution": [
            "Peso: `P = 5 kg · 9,8 m/s² = 49 N`. Sistema concurrente: todas las fuerzas pasan por el centro de la esfera.",
            "Normal del plano `N`: perpendicular al plano, forma 45° con la vertical. `ΣFy = 0`: `N·cos 45° = 49` → `N ≈ 69,3 N`.",
            "Normal de la pared `N_P`: horizontal. `ΣFx = 0`: `N_P = N·sen 45° = 49 N`.",
            "Las reacciones de vínculo son las dos normales (pared y plano); el peso es una fuerza activa, no una reacción. Coincide con el solucionario.",
        ],
    },
    {
        "id": "f-estatica-concurrentes-u4-11",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 2,
        "source": "Física · Práctica U4, ej. 11",
        "title": "Bloque a punto de despegarse",
        "statement": (
            "En la figura, el bloque m es de 10 kg. Descansa sobre una superficie lisa. Calcule m1 y la tensión T en "
            "el instante antes que m se despega del piso. En ese instante, T sería máxima en estado de equilibrio, "
            "cuando la normal es 0.\n\n"
            "Descripción de la figura: m está sobre una mesa horizontal. Por su lado izquierdo está atado a una "
            "cuerda horizontal que pasa por una polea en el borde izquierdo de la mesa y sostiene al cuerpo m1, que "
            "cuelga. Por su lado derecho se tira de m con una fuerza T, hacia arriba y a la derecha, que forma 37° con "
            "la horizontal."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale T? Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 162.8, "tolerance": 0.01, "unit": "N"},
                "answer": "162,8 N",
            },
            {
                "prompt": "b) ¿Cuánto vale m1? Respondé solo con el número en kg, con un decimal.",
                "check": {"type": "numeric", "value": 13.3, "tolerance": 0.01, "unit": "kg"},
                "answer": "13,3 kg",
            },
        ],
        "hints": [
            "Con N = 0, en el eje vertical sobre m solo quedan el peso y la componente vertical de T.",
            "En x, la cuerda que sostiene a m1 tira de m hacia la izquierda con una fuerza igual al peso de m1 (m1 está en equilibrio).",
        ],
        "solution": [
            "Sobre m actúan: peso `98 N`, normal `N = 0`, `T` a 37° y la tensión de la cuerda de m1, horizontal hacia la izquierda, igual a `m1·g`.",
            "`ΣFy = 0`: `T·sen 37° − 98 = 0` → `T = 98/0,6018 ≈ 162,8 N`.",
            "`ΣFx = 0`: `T·cos 37° − m1·g = 0` → `m1 = 162,84·0,7986/9,8 ≈ 13,3 kg`.",
            "Coincide con el solucionario (T = 162,8 N; m1 = 13,3 kg).",
        ],
    },
    # ======================================================================
    # UNIDAD 4 · GUÍA TP 4.1 PARTE B
    # ======================================================================
    {
        "id": "f-estatica-concurrentes-tp41b-1a",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 2,
        "source": "Física · TP 4.1 B, ej. 1a",
        "title": "Resultante de cuatro fuerzas (con kgf)",
        "statement": (
            "Dado el siguiente sistema de fuerzas concurrentes en el origen, determinar analíticamente la resultante "
            "(módulo y dirección) y la equilibrante.\n"
            "- F1 = 500 N, hacia arriba y a la derecha, formando 10° con el semieje y positivo (dirección 80°).\n"
            "- F2 = 3/2·F1, hacia arriba y a la izquierda, formando 40° con el semieje y positivo (dirección 130°).\n"
            "- F3 = 300 N, hacia abajo y a la izquierda, 5° por debajo del semieje x negativo (dirección 185°).\n"
            "- F4 = 30 kgf, hacia abajo y a la derecha, formando 30° con el semieje y negativo (dirección 300°).\n"
            "Usá 1 kgf = 9,8 N. Las direcciones se miden desde el semieje x positivo en sentido antihorario."
        ),
        "parts": [
            {
                "prompt": "a) Módulo de la resultante. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 957.8, "tolerance": 0.01, "unit": "N"},
                "answer": "957,8 N",
            },
            {
                "prompt": "b) Dirección de la resultante. Respondé solo con el número en grados decimales, con un decimal.",
                "check": {"type": "numeric", "value": 124.8, "tolerance": 0.002, "unit": "°"},
                "answer": "124,8°",
            },
            {
                "prompt": "c) Dirección de la equilibrante. Respondé solo con el número en grados decimales, con un decimal.",
                "check": {"type": "numeric", "value": 304.8, "tolerance": 0.001, "unit": "°"},
                "answer": "304,8° (módulo 957,8 N)",
            },
        ],
        "hints": [
            "Pasá todo a N: `F2 = 750 N` y `F4 = 30·9,8 = 294 N`.",
            "Con las direcciones medidas desde +x, `F·cos α` y `F·sen α` ya traen el signo correcto.",
        ],
        "solution": [
            "Datos en N: F1 = 500 (80°), F2 = 750 (130°), F3 = 300 (185°), F4 = 294 (300°).",
            "`Rx = 500·cos 80° + 750·cos 130° + 300·cos 185° + 294·cos 300° = 86,8 − 482,1 − 298,9 + 147,0 ≈ −547,1 N`.",
            "`Ry = 500·sen 80° + 750·sen 130° + 300·sen 185° + 294·sen 300° = 492,4 + 574,5 − 26,1 − 254,6 ≈ 786,2 N`.",
            "`|R| = √(547,1² + 786,2²) ≈ 957,8 N`. 2.º cuadrante: `α_R = 180° − arctg(786,2/547,1) = 180° − 55,2° ≈ 124,8°`.",
            "Equilibrante: mismo módulo, sentido opuesto: `E = 957,8 N`, `α_E = 124,8° + 180° = 304,8°`. Coincide con la grilla.",
        ],
    },
    {
        "id": "f-estatica-concurrentes-tp41b-1c",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 2,
        "source": "Física · TP 4.1 B, ej. 1c",
        "title": "Resultante y equilibrante de cuatro fuerzas",
        "statement": (
            "Dado el siguiente sistema de fuerzas concurrentes en el origen, determinar analíticamente la resultante "
            "(módulo y dirección) y la equilibrante.\n"
            "- F1 = 1000 N, sobre el semieje x positivo (dirección 0°).\n"
            "- F2 = F1/2, hacia abajo y a la derecha, 25° por debajo del semieje x positivo (dirección 335°).\n"
            "- F3 = 100 kgf, hacia arriba y a la derecha, formando 30° con el semieje y positivo (dirección 60°).\n"
            "- F4 = 200 N, hacia abajo y a la izquierda, 50° por debajo del semieje x negativo (dirección 230°).\n"
            "Usá 1 kgf = 9,8 N."
        ),
        "parts": [
            {
                "prompt": "a) Módulo de la resultante. Respondé solo con el número en N, redondeado a unidades.",
                "check": {"type": "numeric", "value": 1878, "tolerance": 0.01, "unit": "N"},
                "answer": "1878 N",
            },
            {
                "prompt": "b) Dirección de la resultante. Respondé solo con el número en grados decimales, con un decimal.",
                "check": {"type": "numeric", "value": 14.9, "tolerance": 0.01, "unit": "°"},
                "answer": "14,9°",
            },
            {
                "prompt": "c) Dirección de la equilibrante. Respondé solo con el número en grados decimales, con un decimal.",
                "check": {"type": "numeric", "value": 194.9, "tolerance": 0.0015, "unit": "°"},
                "answer": "194,9° (módulo 1878 N)",
            },
        ],
        "hints": [
            "Pasá F3 a newton y calculá F2 = 500 N.",
            "Sumá componentes; si las dos componentes de R son positivas, el ángulo es directamente `arctg(Ry/Rx)`.",
        ],
        "solution": [
            "Datos en N: F1 = 1000 (0°), F2 = 500 (335°), F3 = 980 (60°), F4 = 200 (230°).",
            "`Rx = 1000 + 500·cos 335° + 980·cos 60° + 200·cos 230° = 1000 + 453,2 + 490 − 128,6 ≈ 1814,6 N`.",
            "`Ry = 0 + 500·sen 335° + 980·sen 60° + 200·sen 230° = −211,3 + 848,7 − 153,2 ≈ 484,2 N`.",
            "`|R| = √(1814,6² + 484,2²) ≈ 1878 N`; 1.er cuadrante: `α_R = arctg(484,2/1814,6) ≈ 14,9°`.",
            "Equilibrante: `E = 1878 N`, `α_E = 14,9° + 180° = 194,9°`. Coincide con la grilla.",
        ],
    },
    {
        "id": "f-estatica-concurrentes-tp41b-2",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 2,
        "source": "Física · TP 4.1 B, ej. 2",
        "title": "Tres fuerzas sobre un bloque en una rampa",
        "statement": (
            "Si se sabe que α = 35°, determinar la resultante de las tres fuerzas mostradas en la figura.\n\n"
            "Descripción de la figura: un bloque sobre un plano inclinado 20° que sube hacia la derecha. Sobre el "
            "bloque actúan:\n"
            "- 300 N, paralela al plano, hacia arriba del plano (dirección 20°).\n"
            "- 400 N, hacia arriba, formando α = 35° con la fuerza de 300 N (dirección 55°).\n"
            "- 600 N, que empuja al bloque desde arriba a la izquierda: su recta de acción forma α = 35° con la "
            "perpendicular al plano, del lado izquierdo de esa perpendicular (dirección 325°, es decir, hacia abajo y a "
            "la derecha)."
        ),
        "parts": [
            {
                "prompt": "a) Módulo de la resultante. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 1006.5, "tolerance": 0.01, "unit": "N"},
                "answer": "1006,5 N",
            },
            {
                "prompt": "b) Dirección de la resultante (desde +x, antihorario). Respondé solo con el número en grados decimales, con un decimal.",
                "check": {"type": "numeric", "value": 4.9, "tolerance": 0.03, "unit": "°"},
                "answer": "4,9° (≈ 5°)",
            },
        ],
        "hints": [
            "Primero llevá cada fuerza a su dirección medida desde +x: 20°, 55° y 325°.",
            "La perpendicular al plano (hacia afuera) apunta a 110°; la de 600 N viene desde 110° + 35° = 145° y apunta en sentido contrario.",
        ],
        "solution": [
            "Direcciones: 300 N a 20°, 400 N a `20° + 35° = 55°`, 600 N a `145° − 180° = −35° = 325°`.",
            "`Rx = 300·cos 20° + 400·cos 55° + 600·cos 325° = 281,9 + 229,4 + 491,5 ≈ 1002,8 N`.",
            "`Ry = 300·sen 20° + 400·sen 55° + 600·sen 325° = 102,6 + 327,7 − 344,1 ≈ 86,1 N`.",
            "`|R| = √(1002,8² + 86,1²) ≈ 1006,5 N`; `α = arctg(86,1/1002,8) ≈ 4,9°`.",
            "La grilla da 1006,5 N y 5° (redondeado).",
        ],
    },
    {
        "id": "f-estatica-concurrentes-tp41b-4b",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 2,
        "source": "Física · TP 4.1 B, ej. 4b",
        "title": "Cuerpo colgado con cotas en mm",
        "statement": (
            "Calcular las tensiones de las cuerdas que sostienen al cuerpo, que está en equilibrio.\n\n"
            "Descripción de la figura: un cuerpo de 25 N cuelga de un nudo del que salen dos cuerdas hacia el techo. "
            "La cuerda que va al punto B sube hacia la izquierda: B está 540 mm a la izquierda y 500 mm por encima del "
            "nudo. La cuerda que va al punto A sube hacia la derecha: A está 300 mm a la derecha y 400 mm por encima "
            "del nudo."
        ),
        "parts": [
            {
                "prompt": "a) Tensión de la cuerda que va a A. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 18.4, "tolerance": 0.01, "unit": "N"},
                "answer": "18,4 N",
            },
            {
                "prompt": "b) Tensión de la cuerda que va a B. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 15.1, "tolerance": 0.01, "unit": "N"},
                "answer": "15,1 N",
            },
        ],
        "hints": [
            "Con las cotas calculás los ángulos de cada cuerda con la horizontal: `tg θ_B = 500/540` y `tg θ_A = 400/300`.",
            "Planteá `ΣFx = 0` y `ΣFy = 0` en el nudo: es un sistema de dos ecuaciones con dos incógnitas.",
        ],
        "solution": [
            "Ángulos con la horizontal: `θ_B = arctg(500/540) ≈ 42,8°`; `θ_A = arctg(400/300) ≈ 53,13°` (cos = 0,6, sen = 0,8).",
            "`ΣFx = 0`: `T_A·0,6 − T_B·cos 42,8° = 0` → `T_A·0,6 = T_B·0,7337`.",
            "`ΣFy = 0`: `T_A·0,8 + T_B·sen 42,8° = 25` → `T_A·0,8 + T_B·0,6794 = 25`.",
            "De la primera, `T_A = 1,2229·T_B`. Reemplazando: `T_B·(0,9783 + 0,6794) = 25` → `T_B ≈ 15,1 N` y `T_A ≈ 18,4 N`.",
            "Coincide con la grilla (18,4 N y 15,1 N).",
        ],
    },
    {
        "id": "f-estatica-concurrentes-tp41b-4c",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 2,
        "source": "Física · TP 4.1 B, ej. 4c",
        "title": "Nudo entre techo y pared",
        "statement": (
            "Calcular las tensiones de las cuerdas que sostienen al cuerpo, que está en equilibrio, y realizar el "
            "diagrama de cuerpo libre.\n\n"
            "Descripción de la figura: un cuerpo de 10 kgf cuelga de una cuerda vertical atada a un nudo. Del nudo "
            "sale la cuerda A, que sube hacia la derecha hasta el techo formando 60° con el techo (horizontal), y la "
            "cuerda B, que va hacia la izquierda hasta una pared vertical, bajando: forma 60° con la cuerda "
            "vertical de la que cuelga el cuerpo (o sea, va 30° por debajo de la horizontal). Expresá las tensiones en N (1 kgf = 9,8 N)."
        ),
        "parts": [
            {
                "prompt": "a) Tensión de la cuerda A. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 169.7, "tolerance": 0.01, "unit": "N"},
                "answer": "169,7 N",
            },
            {
                "prompt": "b) Tensión de la cuerda B. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 98, "tolerance": 0.01, "unit": "N"},
                "answer": "98,0 N",
            },
        ],
        "hints": [
            "Si la cuerda B forma 60° con la vertical hacia abajo, está 30° por debajo de la horizontal: su dirección es 210°.",
            "La cuerda A tiene dirección 60°. Planteá las dos ecuaciones de equilibrio del nudo con el peso de 98 N.",
        ],
        "solution": [
            "Peso: `10 kgf = 98 N`. Direcciones: T_A a 60°, T_B a 210°, peso a 270°.",
            "`ΣFx = 0`: `T_A·cos 60° + T_B·cos 210° = 0` → `0,5·T_A = 0,866·T_B` → `T_A = 1,732·T_B`.",
            "`ΣFy = 0`: `T_A·sen 60° + T_B·sen 210° − 98 = 0` → `1,732·T_B·0,866 − 0,5·T_B = 98` → `T_B·(1,5 − 0,5) = 98` → `T_B = 98,0 N`.",
            "`T_A = 1,732·98 ≈ 169,7 N`. Coincide con la grilla.",
        ],
    },
    {
        "id": "f-estatica-concurrentes-tp41b-5c",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 3,
        "source": "Física · TP 4.1 B, ej. 5c",
        "title": "Bloque sostenido por una cuerda en un plano",
        "statement": (
            "Realizando el diagrama de cuerpo libre, calcular las reacciones de vínculo (tensión y reacción normal).\n\n"
            "Descripción de la figura: un plano inclinado sin rozamiento, de 4 m de base horizontal y 3,5 m de altura. "
            "Un bloque de 1 kg está apoyado en el plano y lo sostiene una cuerda atada al punto A, por encima del "
            "extremo superior del plano. La cuerda forma 15° con la superficie del plano (por encima de ella)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué ángulo forma el plano con la horizontal? Respondé solo con el número en grados, con un decimal.",
                "check": {"type": "numeric", "value": 41.2, "tolerance": 0.01, "unit": "°"},
                "answer": "41,2°",
            },
            {
                "prompt": "b) Tensión de la cuerda. Respondé solo con el número en N, con dos decimales.",
                "check": {"type": "numeric", "value": 6.68, "tolerance": 0.01, "unit": "N"},
                "answer": "6,68 N",
            },
            {
                "prompt": "c) Reacción normal del plano. Respondé solo con el número en N, con dos decimales.",
                "check": {"type": "numeric", "value": 5.65, "tolerance": 0.01, "unit": "N"},
                "answer": "5,65 N",
            },
        ],
        "hints": [
            "El ángulo del plano sale de `tg θ = 3,5/4`.",
            "Usá ejes paralelo y perpendicular al plano. La tensión tiene componente paralela `T·cos 15°` y perpendicular `T·sen 15°` (alejándose del plano).",
            "En el eje perpendicular, la normal más la componente perpendicular de T equilibran a `P·cos θ`.",
        ],
        "solution": [
            "Ángulo del plano: `θ = arctg(3,5/4) ≈ 41,2°`. Peso: `P = 1·9,8 = 9,8 N`.",
            "Eje paralelo al plano: `T·cos 15° − P·sen θ = 0` → `T = 9,8·0,6585/0,9659 ≈ 6,68 N`.",
            "Eje perpendicular: `N + T·sen 15° − P·cos θ = 0` → `N = 9,8·0,7526 − 6,68·0,2588 = 7,38 − 1,73 ≈ 5,65 N`.",
            "La grilla da 6,7 N y 5,7 N (redondeados a un decimal; con un decimal, N da 5,6 N).",
        ],
    },
    {
        "id": "f-estatica-concurrentes-tp41b-5d",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 2,
        "source": "Física · TP 4.1 B, ej. 5d",
        "title": "Esfera de 85 kgf entre pared y rampa",
        "statement": (
            "Realizando el diagrama de cuerpo libre, calcular las reacciones de vínculo.\n\n"
            "Descripción de la figura: una esfera de 85,0 kgf está apoyada, sin rozamiento, contra una pared vertical "
            "(punto de contacto B, a su izquierda) y sobre un plano que forma 53° con la horizontal (punto de contacto A). "
            "Expresá los resultados en kgf."
        ),
        "parts": [
            {
                "prompt": "a) Reacción del plano en A. Respondé solo con el número en kgf, con un decimal.",
                "check": {"type": "numeric", "value": 141.2, "tolerance": 0.01, "unit": "kgf"},
                "answer": "141,2 kgf",
            },
            {
                "prompt": "b) Reacción de la pared en B. Respondé solo con el número en kgf, con un decimal.",
                "check": {"type": "numeric", "value": 112.8, "tolerance": 0.01, "unit": "kgf"},
                "answer": "112,8 kgf",
            },
        ],
        "hints": [
            "La normal del plano es perpendicular a él: forma 53° con la vertical. La de la pared es horizontal.",
            "No hace falta pasar a newton: trabajá todo en kgf.",
        ],
        "solution": [
            "Fuerzas sobre la esfera (concurrentes en su centro): peso 85,0 kgf hacia abajo, N_A perpendicular al plano (a 53° de la vertical) y N_B horizontal.",
            "`ΣFy = 0`: `N_A·cos 53° = 85,0` → `N_A = 85,0/0,6018 ≈ 141,2 kgf`.",
            "`ΣFx = 0`: `N_B = N_A·sen 53° = 85,0·tg 53° ≈ 112,8 kgf`.",
            "La grilla da 141,4 kgf y 112,8 kgf; el primer valor difiere apenas por redondeo (el cálculo da 141,24 kgf).",
        ],
    },
    {
        "id": "f-estatica-concurrentes-tp41b-7",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 3,
        "source": "Física · TP 4.1 B, ej. 7",
        "title": "Trapecio de cuerdas con 1000 kgf",
        "statement": (
            "Calcular la tensión en cada cuerda de la figura, si el peso suspendido es de 1000 kgf, siendo "
            "α = α´ = 37° y β = β´ = 55°.\n\n"
            "Descripción de la figura (simétrica): el cuerpo cuelga de la cuerda T7, atada al nudo A. De A salen T2, "
            "que sube hacia la izquierda hasta el nudo C, y T1, que sube hacia la derecha hasta el nudo B; ambas "
            "forman β = 55° con la horizontal. C y B están unidos por una cuerda horizontal (T4 es su tensión vista "
            "desde C y T3 vista desde B). De C sube T6 hacia la izquierda hasta el techo, y de B sube T5 hacia la "
            "derecha hasta el techo; ambas forman α = 37° con el techo (horizontal). Expresá las tensiones en kgf."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale T1 (= T2)? Respondé solo con el número en kgf, con un decimal.",
                "check": {"type": "numeric", "value": 610.4, "tolerance": 0.01, "unit": "kgf"},
                "answer": "610,4 kgf",
            },
            {
                "prompt": "b) ¿Cuánto vale T5 (= T6)? Respondé solo con el número en kgf, con un decimal.",
                "check": {"type": "numeric", "value": 830.8, "tolerance": 0.01, "unit": "kgf"},
                "answer": "830,8 kgf",
            },
            {
                "prompt": "c) ¿Cuánto vale la tensión de la cuerda horizontal, T3 (= T4)? Respondé solo con el número en kgf, con un decimal.",
                "check": {"type": "numeric", "value": 313.4, "tolerance": 0.01, "unit": "kgf"},
                "answer": "313,4 kgf",
            },
        ],
        "hints": [
            "Empezá por el nudo A: T7 = 1000 kgf y, por simetría, T1 = T2.",
            "En el nudo C, T2 tira hacia abajo y a la derecha. La ecuación en y te da T6; la ecuación en x, T4.",
        ],
        "solution": [
            "Nudo A: `T7 = 1000 kgf`. Por simetría `T1 = T2`, y `ΣFy = 0`: `2·T1·sen 55° = 1000` → `T1 = T2 = 1000/(2·0,8192) ≈ 610,4 kgf`.",
            "Nudo C: sobre él actúan T6 (arriba a la izquierda, 37° con la horizontal), T4 (horizontal hacia B) y T2 (hacia A: abajo a la derecha, 55° con la horizontal).",
            "`ΣFy = 0`: `T6·sen 37° − T2·sen 55° = 0` → `T6 = 500/0,6018 ≈ 830,8 kgf` (= T5 por simetría).",
            "`ΣFx = 0`: `−T6·cos 37° + T4 + T2·cos 55° = 0` → `T4 = 830,8·0,7986 − 610,4·0,5736 = 663,5 − 350,1 ≈ 313,4 kgf` (= T3).",
            "Coincide con la grilla (T7 = 1000; T1 = T2 = 610,4; T5 = T6 = 830,8; T3 = T4 = 313,4 kgf).",
        ],
    },
    {
        "id": "f-estatica-concurrentes-tp41b-6-8",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 1,
        "source": "Física · TP 4.1 B, ej. 6 y 8",
        "title": "Dos preguntas sobre equilibrio",
        "statement": (
            "a) (ej. 6) Un cuerpo de 1,02 kg está apoyado en reposo sobre un plano inclinado 30° respecto de la "
            "horizontal. Marcá la opción INCORRECTA.\n"
            "b) (ej. 8) Un cuerpo rígido sometido a la acción de un sistema de fuerzas concurrentes se encuentra en "
            "equilibrio de traslación si se cumple que… (marcá la correcta)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál de estas afirmaciones sobre el cuerpo en el plano es INCORRECTA?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Si el ángulo del plano aumenta a 60°, la componente del peso normal al plano también aumenta",
                        "La reacción normal del plano vale aproximadamente 8,66 N",
                        "La fuerza que se opone al deslizamiento sobre el plano tiene un módulo de 5 N",
                        "La suma de todas las fuerzas que actúan sobre el cuerpo es nula",
                    ],
                    "correct": 0,
                },
                "answer": "La de los 60°: la componente normal `P·cos α` DISMINUYE al aumentar el ángulo.",
            },
            {
                "prompt": "b) El cuerpo está en equilibrio de traslación si…",
                "check": {
                    "type": "choice",
                    "options": [
                        "El sistema puede reemplazarse por otro formado por dos fuerzas de igual intensidad, igual dirección y sentidos opuestos",
                        "El sistema de fuerzas está formado solo por dos fuerzas",
                        "Solo si la sumatoria de fuerzas en x es nula",
                        "Se mueve con MRU en el sentido de la resultante del sistema",
                    ],
                    "correct": 0,
                },
                "answer": "Si equivale a dos fuerzas opuestas de igual intensidad y dirección: la resultante es nula.",
            },
        ],
        "hints": [
            "a) Calculá el peso (≈ 10 N) y sus componentes con 30°. ¿Cómo cambia `cos α` cuando α crece?",
            "b) Equilibrio de traslación significa resultante nula: en x Y en y.",
        ],
        "solution": [
            "a) Peso: `P = 1,02·9,8 ≈ 10 N`. En reposo, `ΣF = 0` (correcta). Normal: `N = P·cos 30° ≈ 8,66 N` (correcta). Componente paralela: `P·sen 30° ≈ 5 N`, y la fuerza que se opone al deslizamiento (rozamiento) vale lo mismo (correctas).",
            "a) La componente normal es `P·cos α`; como `cos 60° = 0,5 < cos 30° = 0,866`, al aumentar el ángulo esa componente DISMINUYE. Esa es la incorrecta (opción c de la guía).",
            "b) Equilibrio de traslación: la resultante es nula. Dos fuerzas de igual intensidad, igual dirección y sentidos opuestos tienen resultante nula (opción d de la guía).",
            "b) Las otras fallan: dos fuerzas cualesquiera no tienen por qué anularse; no alcanza con que `ΣFx = 0` (también tiene que ser `ΣFy = 0`); y si hay MRU la resultante es nula, así que no hay 'sentido de la resultante'.",
        ],
    },
    # ======================================================================
    # UNIDAD 4 · BIBLIOGRAFÍA (Vallone)
    # ======================================================================
    {
        "id": "f-estatica-concurrentes-vallone-10",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 1,
        "source": "Física · Vallone TP, U5 ej. 10",
        "title": "Cuerpo sostenido por dos barras",
        "statement": (
            "Calcular las tensiones en las barras T1 y T2 de la figura.\n\n"
            "Descripción de la figura: un cuerpo de 500 N cuelga de un nudo. Del nudo sale T1, horizontal hacia la "
            "izquierda hasta una pared, y T2, que sube hacia la derecha hasta el techo formando 45° con el techo "
            "(horizontal)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale T2? Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 707.1, "tolerance": 0.01, "unit": "N"},
                "answer": "707,1 N",
            },
            {
                "prompt": "b) ¿Cuánto vale T1? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 500, "tolerance": 0.01, "unit": "N"},
                "answer": "500 N",
            },
        ],
        "hints": [
            "Solo T2 tiene componente vertical: tiene que equilibrar los 500 N.",
            "Con 45°, las dos componentes de T2 son iguales.",
        ],
        "solution": [
            "DCL del nudo: 500 N hacia abajo, T1 hacia la izquierda, T2 a 45° hacia arriba a la derecha.",
            "`ΣFy = 0`: `T2·sen 45° = 500` → `T2 = 500/0,7071 ≈ 707,1 N`.",
            "`ΣFx = 0`: `T1 = T2·cos 45° = 500 N`.",
        ],
    },
    {
        "id": "f-estatica-concurrentes-vallone-11",
        "node": "f-estatica-concurrentes",
        "kind": "problem",
        "level": 1,
        "source": "Física · Vallone TP, U5 ej. 11",
        "title": "Esfera colgada junto a una barra",
        "statement": (
            "Una esfera de 500 N está suspendida como indica la figura. La cuerda que la sostiene forma un ángulo de "
            "20° con la barra vertical. Determiná la tensión en la cuerda y la reacción de la barra.\n\n"
            "Descripción de la figura: la cuerda está atada a la barra vertical, por encima de la esfera, y llega al "
            "centro de la esfera; la esfera queda apoyada, sin rozamiento, contra la barra."
        ),
        "parts": [
            {
                "prompt": "a) Tensión de la cuerda. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 532.1, "tolerance": 0.01, "unit": "N"},
                "answer": "532,1 N",
            },
            {
                "prompt": "b) Reacción de la barra. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 182, "tolerance": 0.01, "unit": "N"},
                "answer": "182,0 N, horizontal",
            },
        ],
        "hints": [
            "La reacción de la barra es horizontal (perpendicular a la barra). Como el ángulo de la cuerda está medido desde la vertical, su componente vertical es `T·cos 20°`.",
        ],
        "solution": [
            "Fuerzas sobre la esfera (concurrentes en su centro): peso 500 N, T a 20° de la vertical y N horizontal (empuje de la barra).",
            "`ΣFy = 0`: `T·cos 20° = 500` → `T = 500/0,9397 ≈ 532,1 N`.",
            "`ΣFx = 0`: `N = T·sen 20° = 500·tg 20° ≈ 182,0 N`.",
            "La guía no trae respuestas; estos valores salen del cálculo.",
        ],
    },
    {
        "id": "f-momento-cupla-vinculos-vallone-12",
        "node": "f-momento-cupla-vinculos",
        "kind": "problem",
        "level": 2,
        "source": "Física · Vallone TP, U5 ej. 12",
        "title": "Barra con resultante nula",
        "statement": (
            "Una barra horizontal AB de 2 m de longitud está sometida a la acción de las siguientes fuerzas:\n"
            "- Peso propio de 20 N aplicado en su punto medio G.\n"
            "- Fuerza de 10 N en A, hacia abajo.\n"
            "- Fuerza de 25 N en B, hacia arriba.\n"
            "- A 0,5 m de A, una fuerza de 15 N, hacia arriba.\n"
            "- A 1,5 m de A, una fuerza de 10 N, hacia abajo.\n"
            "El extremo A está a la izquierda del extremo B. Considerando como positivo para los momentos el sentido "
            "antihorario, todo lo que sigue es verdadero, excepto…"
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la suma de momentos respecto de A? Respondé solo con el número en N·m, con su signo.",
                "check": {"type": "numeric", "value": 22.5, "tolerance": 0.01, "unit": "N·m"},
                "answer": "22,5 N·m (antihorario)",
            },
            {
                "prompt": "b) Marcá la afirmación FALSA.",
                "check": {
                    "type": "choice",
                    "options": [
                        "La suma de momentos en B es igual y de distinto signo que la suma de momentos en A",
                        "La resultante es nula",
                        "La suma de momentos en G es igual que la suma de momentos en A",
                        "La barra no está en equilibrio",
                    ],
                    "correct": 0,
                },
                "answer": "La de B con distinto signo: con resultante nula, el momento es el mismo (22,5 N·m) respecto de cualquier punto.",
            },
        ],
        "hints": [
            "Sumá primero las fuerzas verticales con su signo: ¿qué te da?",
            "Si la resultante es nula pero el momento no, el sistema es una cupla: su momento no depende del punto que elijas.",
        ],
        "solution": [
            "Resultante: `−20 − 10 + 25 + 15 − 10 = 0`. La resultante (y por lo tanto la equilibrante como fuerza única) es nula.",
            "Momentos respecto de A (A en x = 0): `−20·1 − 10·0 + 25·2 + 15·0,5 − 10·1,5 = −20 + 50 + 7,5 − 15 = +22,5 N·m`.",
            "Respecto de G (x = 1): `−10·(−1) + 25·1 + 15·(−0,5) − 10·0,5 = 10 + 25 − 7,5 − 5 = +22,5 N·m`. Respecto de B (x = 2): `−10·(−2) − 20·(−1) + 15·(−1,5) − 10·(−0,5) = 20 + 20 − 22,5 + 5 = +22,5 N·m`.",
            "El sistema es una cupla: momento constante, +22,5 N·m, respecto de cualquier punto. Por eso la barra no está en equilibrio (gira) aunque la resultante sea nula.",
            "La afirmación falsa es la d) de la guía: en B el momento es igual y del MISMO signo que en A.",
        ],
    },
    {
        "id": "f-momento-cupla-vinculos-vallone-13",
        "node": "f-momento-cupla-vinculos",
        "kind": "problem",
        "level": 2,
        "source": "Física · Vallone TP, U5 ej. 13 (resuelto en los Apuntes)",
        "title": "Reacciones en un trampolín",
        "statement": (
            "La siguiente figura esquematiza un trampolín. Determiná las reacciones en las articulaciones A y B. La "
            "fuerza es de 500 N, la distancia AB = 0,50 m y la longitud de la barra AC es de 1,75 m.\n\n"
            "Descripción de la figura: barra horizontal AC (peso despreciable). En el extremo izquierdo A hay una "
            "articulación; en B, 0,50 m a la derecha de A, la barra se apoya sobre otro vínculo ubicado debajo de "
            "ella. En el extremo libre C actúa la fuerza de 500 N, vertical hacia abajo. No hay fuerzas horizontales."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la reacción en B? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 1750, "tolerance": 0.01, "unit": "N"},
                "answer": "1750 N, hacia arriba",
            },
            {
                "prompt": "b) ¿Cuánto vale el módulo de la reacción en A? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 1250, "tolerance": 0.01, "unit": "N"},
                "answer": "1250 N",
            },
            {
                "prompt": "c) ¿Qué sentido tiene la reacción en A?",
                "check": {
                    "type": "choice",
                    "options": ["Hacia abajo", "Hacia arriba", "Horizontal, hacia la derecha"],
                    "correct": 0,
                },
                "answer": "Hacia abajo: la articulación A impide que ese extremo se levante.",
            },
        ],
        "hints": [
            "Tomá momentos respecto de A: desaparece R_A y te queda solo R_B.",
            "Con R_B, la suma de fuerzas verticales te da R_A. Si te sale negativa, el sentido es el contrario al supuesto.",
        ],
        "solution": [
            "No hay acciones horizontales, así que no hay reacciones horizontales: las incógnitas son R_A y R_B, verticales.",
            "`ΣM_A = 0`: `R_B·0,50 − 500·1,75 = 0` → `R_B = 875/0,50 = 1750 N` (hacia arriba).",
            "`ΣFy = 0`: suponiendo R_A hacia arriba, `R_A + 1750 − 500 = 0` → `R_A = −1250 N`. El signo menos indica que R_A apunta hacia abajo.",
            "Tiene sentido: B hace de pivote y la fuerza en C tiende a levantar el extremo A, que la articulación sujeta hacia abajo. Coincide con el ejemplo resuelto de los Apuntes Teóricos.",
        ],
    },
    {
        "id": "f-momento-cupla-vinculos-apuntes-resultante",
        "node": "f-momento-cupla-vinculos",
        "kind": "problem",
        "level": 3,
        "source": "Física · Apuntes Teóricos (Vallone), ejemplo de resultante con momentos",
        "title": "Posición de la resultante",
        "statement": (
            "Hallar la resultante del siguiente sistema de fuerzas no concurrentes (módulo, dirección y sentido) y el "
            "punto donde su recta de acción corta al eje x. Datos (posiciones en m; direcciones desde el semieje x "
            "positivo, antihorario):\n"
            "| Fuerza | Módulo | Dirección | Punto de aplicación |\n"
            "|---|---|---|---|\n"
            "| F1 | 50 N | 0° | (0; 5,0) |\n"
            "| F2 | 60 N | 60° | (0; 0) |\n"
            "| F3 | 40 N | 150° | (4,2; 0) |\n"
            "| F4 | 80 N | 90° | (6,3; 0) |\n"
            "| F5 | 100 N | 315° | (7,8; 0) |"
        ),
        "parts": [
            {
                "prompt": "a) Módulo de la resultante. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 141.7, "tolerance": 0.01, "unit": "N"},
                "answer": "141,7 N",
            },
            {
                "prompt": "b) Dirección de la resultante. Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 35, "tolerance": 0.01, "unit": "°"},
                "answer": "35°",
            },
            {
                "prompt": "c) ¿En qué abscisa x corta la recta de acción de la resultante al eje x? Respondé solo con el número en m, con su signo y dos decimales.",
                "check": {"type": "numeric", "value": -2.63, "tolerance": 0.01, "unit": "m"},
                "answer": "−2,63 m (a la izquierda del origen)",
            },
        ],
        "hints": [
            "Primero la resultante, sumando componentes como en un sistema concurrente.",
            "Momento de cada fuerza respecto del origen: las aplicadas sobre el eje x dan `x·Fy`; F1 es horizontal y está a 5 m de altura, así que da `−5·F1x`.",
            "Teorema de los momentos: el momento del sistema es igual al de la resultante. Si R corta al eje x en `x_R`, su momento es `x_R·Ry`.",
        ],
        "solution": [
            "Componentes x: `50 + 60·cos 60° + 40·cos 150° + 0 + 100·cos 315° = 50 + 30 − 34,6 + 70,7 = 116,1 N`.",
            "Componentes y: `0 + 52,0 + 20 + 80 − 70,7 = 81,3 N`. `|R| = √(116,1² + 81,3²) ≈ 141,7 N`; 1.er cuadrante, `θ = arctg(81,3/116,1) ≈ 35°`.",
            "Momento respecto del origen: `M_O = −50·5,0 + 0 + 20·4,2 + 80·6,3 − 70,7·7,8 = −250 + 84 + 504 − 551,5 ≈ −213,5 N·m`.",
            "Teorema de los momentos: `x_R·Ry = M_O` → `x_R = −213,5/81,3 ≈ −2,63 m`: la resultante corta al eje x a la izquierda del origen.",
            "Nota: los Apuntes escriben `cos(−135°)` para F5, pero los valores que usan (70,7 N y −70,7 N) corresponden a la dirección −45° = 315°, que es la de la figura.",
        ],
    },
    {
        "id": "f-momento-cupla-vinculos-apuntes-cupla",
        "node": "f-momento-cupla-vinculos",
        "kind": "problem",
        "level": 1,
        "source": "Física · Apuntes Teóricos (Vallone), ejemplo de cupla",
        "title": "El momento de una cupla",
        "statement": (
            "Una barra horizontal de 2 m de longitud está sometida a una cupla: en su extremo izquierdo actúa una "
            "fuerza de 20 N vertical hacia abajo y en su extremo derecho una fuerza de 20 N vertical hacia arriba. "
            "Calculá el momento del sistema respecto de distintos puntos (positivo el sentido antihorario)."
        ),
        "parts": [
            {
                "prompt": "a) Momento respecto del extremo izquierdo. Respondé solo con el número en N·m, con su signo.",
                "check": {"type": "numeric", "value": 40, "tolerance": 0.01, "unit": "N·m"},
                "answer": "40 N·m (antihorario)",
            },
            {
                "prompt": "b) Momento respecto del punto medio de la barra. Respondé solo con el número en N·m, con su signo.",
                "check": {"type": "numeric", "value": 40, "tolerance": 0.01, "unit": "N·m"},
                "answer": "40 N·m (antihorario)",
            },
            {
                "prompt": "c) Momento respecto de un punto de la recta de la barra ubicado 1 m a la izquierda del extremo izquierdo. Respondé solo con el número en N·m, con su signo.",
                "check": {"type": "numeric", "value": 40, "tolerance": 0.01, "unit": "N·m"},
                "answer": "40 N·m: el momento de una cupla no depende del punto",
            },
        ],
        "hints": [
            "Para cada fuerza: momento = fuerza × distancia, con signo + si hace girar en sentido antihorario alrededor del punto elegido.",
            "Una fuerza hacia arriba a la DERECHA del punto hace girar en sentido antihorario; una hacia abajo a la DERECHA, en sentido horario.",
        ],
        "solution": [
            "Respecto del extremo izquierdo: la fuerza de ese extremo pasa por el punto (momento nulo); la otra, hacia arriba a 2 m a la derecha: `+20·2 = +40 N·m`.",
            "Respecto del punto medio: la de la izquierda, hacia abajo a 1 m a la izquierda → antihoraria, `+20·1`; la de la derecha, hacia arriba a 1 m a la derecha → antihoraria, `+20·1`. Total `+40 N·m`.",
            "Respecto del punto 1 m a la izquierda: la fuerza hacia abajo, a 1 m a la derecha → horaria, `−20·1 = −20`; la fuerza hacia arriba, a 3 m a la derecha → `+20·3 = +60`. Total `+40 N·m`.",
            "Siempre da lo mismo: el momento de una cupla es independiente del centro de momentos. Su resultante es nula, pero produce rotación pura.",
            "Ojo: los Apuntes escriben `−40 N·m`, pero con su propia convención (antihorario positivo) y esta disposición (abajo a la izquierda, arriba a la derecha) la cupla gira en sentido antihorario: `+40 N·m`.",
        ],
    },
    # ======================================================================
    # UNIDAD 5 · PRÁCTICA DEL CURSO
    # ======================================================================
    {
        "id": "f-cuerpos-vinculados-u5-1",
        "node": "f-cuerpos-vinculados",
        "kind": "problem",
        "level": 1,
        "source": "Física · Práctica U5, ej. 1",
        "title": "Dos cajas que se mueven juntas",
        "statement": (
            "Determine el módulo de la aceleración de los bloques si se sabe que se aplica una fuerza de 10 N a la caja "
            "B haciendo que ambos bloques se muevan juntos. La masa de A es de 1 kg y la de B es de 2 kg. No se "
            "considera fricción entre las cajas y el suelo.\n\n"
            "Descripción de la figura: la caja A está apoyada encima de la caja B; el tirón horizontal de 10 N se aplica "
            "sobre B."
        ),
        "parts": [
            {
                "prompt": "Módulo de la aceleración. Respondé solo con el número en m/s², con dos decimales.",
                "check": {"type": "numeric", "value": 3.33, "tolerance": 0.01, "unit": "m/s²"},
                "answer": "3,33 m/s² (= 10/3)",
            },
        ],
        "hints": [
            "Si se mueven juntos, podés tratarlos como un solo cuerpo de 3 kg: las fuerzas entre A y B son internas.",
        ],
        "solution": [
            "Como las dos cajas se mueven juntas, tienen la misma aceleración y se pueden tratar como un único sistema de masa `1 + 2 = 3 kg`.",
            "La única fuerza externa horizontal es el tirón de 10 N (no hay fricción con el suelo).",
            "`a = F/(m_A + m_B) = 10/3 ≈ 3,33 m/s²`. El solucionario da 3,3 m/s².",
            "Para pensar: lo que acelera a A es el rozamiento estático que le hace B, de valor `1·3,33 = 3,33 N`.",
        ],
    },
    {
        "id": "f-cuerpos-vinculados-u5-2",
        "node": "f-cuerpos-vinculados",
        "kind": "problem",
        "level": 1,
        "source": "Física · Práctica U5, ej. 2",
        "title": "Cajas sobre un estanque congelado",
        "statement": (
            "Dos cajas, una de 4,00 kg y la otra de 6,00 kg, descansan en la superficie horizontal sin fricción de un "
            "estanque congelado, unidas por una cuerda delgada. Una mujer (con zapatos de golf que le dan tracción "
            "sobre el hielo) aplica una fuerza horizontal F a la caja de 6,00 kg y le imparte una aceleración de "
            "2,50 m/s². Calcule la tensión T y la fuerza F.\n\n"
            "Descripción de la figura: la caja de 4,00 kg está detrás (a la izquierda), unida por la cuerda a la de "
            "6,00 kg; la mujer tira de la de 6,00 kg hacia la derecha."
        ),
        "parts": [
            {
                "prompt": "a) Tensión de la cuerda. Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 10, "tolerance": 0.01, "unit": "N"},
                "answer": "10 N",
            },
            {
                "prompt": "b) Fuerza F. Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 25, "tolerance": 0.01, "unit": "N"},
                "answer": "25 N",
            },
        ],
        "hints": [
            "La cuerda es la única fuerza horizontal sobre la caja de 4,00 kg.",
            "Para F, tomá todo el sistema (10 kg) o la caja de 6,00 kg: `F − T = 6·a`.",
        ],
        "solution": [
            "Caja de 4,00 kg: `T = 4,00·2,50 = 10,0 N`.",
            "Caja de 6,00 kg: `F − T = 6,00·2,50` → `F = 15,0 + 10,0 = 25,0 N`.",
            "Verificación con el sistema completo: `F = (4,00 + 6,00)·2,50 = 25,0 N`. Coincide con el solucionario.",
        ],
    },
    {
        "id": "f-cuerpos-vinculados-u5-3",
        "node": "f-cuerpos-vinculados",
        "kind": "problem",
        "level": 3,
        "source": "Física · Práctica U5, ej. 3",
        "title": "Dos bloques unidos por una cuerda pesada",
        "statement": (
            "Los dos bloques de la figura están unidos por una cuerda gruesa uniforme de 4,00 kg. Se aplica una "
            "fuerza de 200 N hacia arriba, como se indica.\n\n"
            "Descripción de la figura: arriba, un bloque de 6,00 kg del que se tira con F = 200 N vertical hacia arriba; "
            "de su base cuelga la cuerda de 4,00 kg, y del extremo inferior de la cuerda cuelga un bloque de 5,00 kg. "
            "Usá g = 9,8 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué aceleración tiene el sistema? Respondé solo con el número en m/s², con dos decimales.",
                "check": {"type": "numeric", "value": 3.53, "tolerance": 0.01, "unit": "m/s²"},
                "answer": "3,53 m/s², hacia arriba",
            },
            {
                "prompt": "b) ¿Qué tensión hay en la parte superior de la cuerda? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 120, "tolerance": 0.01, "unit": "N"},
                "answer": "120 N",
            },
            {
                "prompt": "c) ¿Qué tensión hay en la parte inferior de la cuerda? Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 66.7, "tolerance": 0.01, "unit": "N"},
                "answer": "66,7 N",
            },
        ],
        "hints": [
            "Sistema completo: masa total 15 kg; fuerzas externas: F hacia arriba y el peso total hacia abajo.",
            "La tensión arriba de la cuerda sostiene y acelera a la cuerda y al bloque de abajo; la de abajo, solo al bloque de 5,00 kg.",
            "Como la cuerda tiene masa, las dos tensiones NO son iguales.",
        ],
        "solution": [
            "DCL: bloque de 6 kg (F arriba, su peso y T_sup abajo); cuerda (T_sup arriba, su peso y T_inf abajo); bloque de 5 kg (T_inf arriba y su peso).",
            "Sistema completo: `F − m_total·g = m_total·a` → `200 − 15·9,8 = 15·a` → `a = 53/15 ≈ 3,53 m/s²`.",
            "Tensión superior (cuerda + bloque de 5 kg, 9 kg): `T_sup − 9·9,8 = 9·a` → `T_sup = 9·(9,8 + 3,533) = 120 N`.",
            "Tensión inferior (bloque de 5 kg): `T_inf = 5·(9,8 + 3,533) ≈ 66,7 N`.",
            "El solucionario da 3,53 m/s², 120 N y 67 N.",
        ],
    },
    {
        "id": "f-dcl-rozamiento-plano-u5-4",
        "node": "f-dcl-rozamiento-plano",
        "kind": "problem",
        "level": 1,
        "source": "Física · Práctica U5, ej. 4",
        "title": "Esquiador remolcado cuesta arriba",
        "statement": (
            "Un esquiador de 65 kg es remolcado cuesta arriba por una ladera nevada con rapidez constante, sujeto a "
            "una cuerda paralela al suelo. La pendiente es constante de 26° sobre la horizontal y la fricción es "
            "despreciable. Dibuje su DCL y calcule la tensión en la cuerda."
        ),
        "parts": [
            {
                "prompt": "Tensión de la cuerda. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 279.2, "tolerance": 0.01, "unit": "N"},
                "answer": "279,2 N",
            },
        ],
        "hints": [
            "Rapidez constante significa aceleración nula: la fuerza neta es cero.",
            "Usá ejes paralelo y perpendicular a la ladera: en el paralelo solo están T y `P·sen 26°`.",
        ],
        "solution": [
            "DCL: peso `P = 65·9,8 = 637 N` vertical, normal N perpendicular a la ladera y tensión T paralela a la ladera, hacia arriba.",
            "Velocidad constante → `ΣF = 0`.",
            "Eje paralelo: `T − P·sen 26° = 0` → `T = 637·0,4384 ≈ 279,2 N`.",
            "(Eje perpendicular: `N = P·cos 26° ≈ 572,5 N`, no se pide.) Coincide con el solucionario.",
        ],
    },
    {
        "id": "f-leyes-newton-u5-5",
        "node": "f-leyes-newton",
        "kind": "problem",
        "level": 2,
        "source": "Física · Práctica U5, ej. 5",
        "title": "Bala que penetra en un árbol",
        "statement": (
            "Una bala de rifle calibre 22 que viaja a 350 m/s golpea un árbol grande, penetrando a una profundidad de "
            "0,130 m. La masa de la bala es de 1,80 g. Suponga una fuerza de frenado constante. a) ¿Cuánto tarda la "
            "bala en detenerse? b) ¿Qué fuerza (en N) ejerce el árbol sobre la bala?"
        ),
        "parts": [
            {
                "prompt": "a) Tiempo de frenado. Respondé solo con el número en s (podés usar notación científica), con tres cifras.",
                "check": {"type": "numeric", "value": 0.000743, "tolerance": 0.01, "unit": "s"},
                "answer": "0,000743 s (7,43·10⁻⁴ s)",
            },
            {
                "prompt": "b) Módulo de la fuerza del árbol sobre la bala. Respondé solo con el número en N, redondeado a unidades.",
                "check": {"type": "numeric", "value": 848, "tolerance": 0.01, "unit": "N"},
                "answer": "848 N",
            },
        ],
        "hints": [
            "Fuerza constante → aceleración constante (MRUV). Conocés `v₀`, `v = 0` y la distancia: usá `v² = v₀² + 2·a·Δx`.",
            "Pasá la masa a kg antes de aplicar `F = m·a`.",
        ],
        "solution": [
            "Aceleración: `0 = 350² + 2·a·0,130` → `a = −122 500/0,260 ≈ −4,71·10⁵ m/s²`.",
            "Tiempo: `0 = 350 + a·t` → `t = 350/(4,71·10⁵) ≈ 7,43·10⁻⁴ s`. (También: `Δx = (v₀ + v)/2·t` → `t = 0,130/175`.)",
            "Fuerza: `F = m·|a| = 0,00180 kg · 4,712·10⁵ m/s² ≈ 848 N`, opuesta a la velocidad.",
            "Coincide con el solucionario (7,4·10⁻⁴ s y 848 N).",
        ],
    },
    {
        "id": "f-leyes-newton-u5-6abc",
        "node": "f-leyes-newton",
        "kind": "problem",
        "level": 2,
        "source": "Física · Práctica U5, ej. 6 a–c",
        "title": "Ascensor: tensión en tres fases",
        "statement": (
            "Un ascensor lleno de personas tiene una masa total de 1430 kg. La aceleración de la gravedad es de "
            "9,80 m/s².\n"
            "a) El ascensor está en reposo y comienza a moverse hacia arriba con una aceleración de 1,00 m/s² durante "
            "2,80 s. Calcular la tensión en los cables que lo sostienen.\n"
            "b) Luego de la fase anterior, el elevador continúa moviéndose con velocidad constante hacia arriba durante "
            "5,00 s. Calcular la tensión en los cables durante esta fase.\n"
            "c) A continuación, el ascensor comienza a desacelerar a razón de −1,25 m/s². Esta etapa dura 1,50 s. "
            "¿Cuál es la tensión en los cables durante esta desaceleración?"
        ),
        "parts": [
            {
                "prompt": "a) Tensión durante la fase de aceleración. Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 15444, "tolerance": 0.01, "unit": "N"},
                "answer": "15444 N",
            },
            {
                "prompt": "b) Tensión durante la fase de velocidad constante. Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 14014, "tolerance": 0.01, "unit": "N"},
                "answer": "14014 N",
            },
            {
                "prompt": "c) Tensión durante la desaceleración. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 12226.5, "tolerance": 0.01, "unit": "N"},
                "answer": "12226,5 N",
            },
        ],
        "hints": [
            "En todas las fases: `T − m·g = m·a`, con el eje positivo hacia arriba.",
            "Velocidad constante → `a = 0`. Desacelerando mientras sube → `a` negativa.",
        ],
        "solution": [
            "Segunda ley con eje + hacia arriba: `T − m·g = m·a` → `T = m·(g + a)`.",
            "a) `T = 1430·(9,80 + 1,00) = 15 444 N`.",
            "b) `a = 0`: `T = 1430·9,80 = 14 014 N` (igual al peso).",
            "c) `a = −1,25 m/s²`: `T = 1430·(9,80 − 1,25) = 12 226,5 N`.",
            "Coincide con el solucionario. La tensión es mayor que el peso al arrancar hacia arriba y menor al frenar.",
        ],
    },
    {
        "id": "f-leyes-newton-u5-6d",
        "node": "f-leyes-newton",
        "kind": "problem",
        "level": 2,
        "source": "Física · Práctica U5, ej. 6d",
        "title": "Ascensor: altura y velocidad final",
        "statement": (
            "Un ascensor parte del reposo y sube con aceleración de 1,00 m/s² durante 2,80 s; luego sube con velocidad "
            "constante durante 5,00 s; finalmente desacelera a razón de −1,25 m/s² durante 1,50 s. Encontrar a qué "
            "altura llega el elevador luego de todo el movimiento de ascenso y con qué velocidad final lo hace. ¿El "
            "signo de la velocidad es positivo o negativo?"
        ),
        "parts": [
            {
                "prompt": "a) Altura total recorrida. Respondé solo con el número en m, con dos decimales.",
                "check": {"type": "numeric", "value": 20.71, "tolerance": 0.015, "unit": "m"},
                "answer": "20,71 m (≈ 21 m)",
            },
            {
                "prompt": "b) Velocidad al final de la tercera fase. Respondé solo con el número en m/s, con tres decimales.",
                "check": {"type": "numeric", "value": 0.925, "tolerance": 0.01, "unit": "m/s"},
                "answer": "0,925 m/s",
            },
            {
                "prompt": "c) ¿Qué signo tiene esa velocidad (eje + hacia arriba)?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Positivo: todavía sube",
                        "Negativo: ya empezó a bajar",
                        "Es cero: el ascensor se detuvo",
                    ],
                    "correct": 0,
                },
                "answer": "Positivo: al final de la fase el ascensor todavía sube, más despacio.",
            },
        ],
        "hints": [
            "Calculá la velocidad al final de la primera fase: es la de la segunda y la inicial de la tercera.",
            "Cada tramo es un MRUV o un MRU: `Δy = v₀·t + ½·a·t²`. Sumá los tres desplazamientos.",
        ],
        "solution": [
            "Fase 1: `v₁ = 1,00·2,80 = 2,80 m/s`; `Δy₁ = ½·1,00·2,80² = 3,92 m`.",
            "Fase 2 (MRU): `Δy₂ = 2,80·5,00 = 14,00 m`.",
            "Fase 3: `Δy₃ = 2,80·1,50 − ½·1,25·1,50² = 4,20 − 1,41 = 2,79 m`; `v_f = 2,80 − 1,25·1,50 = 0,925 m/s`.",
            "Altura total: `3,92 + 14,00 + 2,79 ≈ 20,71 m` (≈ 21 m). La velocidad final es positiva: el ascensor todavía sube.",
            "El solucionario da h = 21 m y v_f = 0,91 m/s; con los datos de la guía (1,50 s) la cuenta da 0,925 m/s. En la presentación de la unidad la fase 3 dura 2,24 s: con ese tiempo el ascensor termina detenido (`2,80 − 1,25·2,24 = 0`) a unos 21,06 m.",
        ],
    },
    {
        "id": "f-cuerpos-vinculados-u5-7",
        "node": "f-cuerpos-vinculados",
        "kind": "problem",
        "level": 2,
        "source": "Física · Práctica U5, ej. 7",
        "title": "Dos bloques arrastrados con rozamiento",
        "statement": (
            "Dos bloques unidos mediante una cuerda de masa despreciable son arrastrados por una fuerza horizontal F. "
            "Suponga que F = 68 N, m1 = 12 kg, m2 = 18 kg y que la fuerza de rozamiento de m1 respecto a la superficie "
            "es de 11,7 N y la de m2 es de 17,6 N. Determinar la tensión T y la magnitud de la aceleración del sistema.\n\n"
            "Descripción de la figura: m1 a la izquierda, unido por la cuerda a m2; F tira de m2 hacia la derecha."
        ),
        "parts": [
            {
                "prompt": "a) Aceleración del sistema. Respondé solo con el número en m/s², con dos decimales.",
                "check": {"type": "numeric", "value": 1.29, "tolerance": 0.01, "unit": "m/s²"},
                "answer": "1,29 m/s²",
            },
            {
                "prompt": "b) Tensión de la cuerda. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 27.2, "tolerance": 0.01, "unit": "N"},
                "answer": "27,2 N",
            },
        ],
        "hints": [
            "Sistema completo: `F − f₁ − f₂ = (m1 + m2)·a`; la tensión es interna y se cancela.",
            "Para T, mirá el bloque de atrás (m1): la cuerda es lo único que lo arrastra contra su rozamiento.",
        ],
        "solution": [
            "Sistema: `68 − 11,7 − 17,6 = 30·a` → `a = 38,7/30 = 1,29 m/s²`.",
            "Bloque m1: `T − 11,7 = 12·1,29` → `T = 15,48 + 11,7 ≈ 27,2 N`.",
            "Verificación con m2: `68 − T − 17,6 = 18·1,29` → `T = 50,4 − 23,22 = 27,18 N`. Coincide con el solucionario.",
        ],
    },
    {
        "id": "f-cuerpos-vinculados-u5-8",
        "node": "f-cuerpos-vinculados",
        "kind": "problem",
        "level": 3,
        "source": "Física · Práctica U5, ej. 8",
        "title": "Bloque en la mesa y bloque colgante",
        "statement": (
            "Considere el sistema de la figura. El bloque A pesa 90,0 N y el bloque B pesa 25,0 N. Una vez que el "
            "bloque B se pone en movimiento hacia abajo, desciende con rapidez constante.\n"
            "a) Calcule la fuerza de rozamiento entre el bloque A y la mesa.\n"
            "b) Si la fuerza de rozamiento entre el bloque A y la mesa es de 10 N y el bloque B se mueve con MRUV, "
            "calcule la aceleración (magnitud y sentido) que tendrá el sistema y la tensión de la cuerda.\n\n"
            "Descripción de la figura: A está sobre una mesa horizontal; una cuerda horizontal lo une, pasando por una "
            "polea en el borde derecho de la mesa, con B, que cuelga. Usá g = 9,8 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) Fuerza de rozamiento cuando B baja con rapidez constante. Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 25, "tolerance": 0.01, "unit": "N"},
                "answer": "25 N",
            },
            {
                "prompt": "b) Aceleración si el rozamiento es de 10 N (A hacia la derecha, B hacia abajo). Respondé solo con el número en m/s², con dos decimales.",
                "check": {"type": "numeric", "value": 1.28, "tolerance": 0.01, "unit": "m/s²"},
                "answer": "1,28 m/s²",
            },
            {
                "prompt": "c) Tensión de la cuerda en ese caso. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 21.7, "tolerance": 0.01, "unit": "N"},
                "answer": "21,7 N",
            },
        ],
        "hints": [
            "Rapidez constante: fuerza neta nula en cada bloque. ¿Qué tensión tiene la cuerda si B no acelera?",
            "Para b) necesitás las masas: `m = P/g`. Sistema: `P_B − f = (m_A + m_B)·a`.",
        ],
        "solution": [
            "a) B con rapidez constante: `T = P_B = 25,0 N`. A con rapidez constante: `f = T = 25,0 N`.",
            "b) Masas: `m_A = 90,0/9,8 = 9,18 kg`; `m_B = 25,0/9,8 = 2,55 kg`; total `11,73 kg`.",
            "Sistema: `25,0 − 10 = 11,73·a` → `a ≈ 1,28 m/s²`; A acelera hacia la derecha y B hacia abajo.",
            "Bloque B: `P_B − T = m_B·a` → `T = 25,0 − 2,55·1,278 ≈ 21,7 N` (con A: `T = 10 + 9,18·1,278 ≈ 21,7 N`).",
            "El solucionario da a = 1,28 m/s² y T = 21,8 N; la cuenta sin redondeos intermedios da 21,74 N.",
        ],
    },
    {
        "id": "f-dcl-rozamiento-plano-u5-9",
        "node": "f-dcl-rozamiento-plano",
        "kind": "problem",
        "level": 2,
        "source": "Física · Práctica U5, ej. 9",
        "title": "Cuerpo que baja por un plano con fricción",
        "statement": (
            "En un plano inclinado se abandona un cuerpo de 5 kg que se desliza por él. Su ángulo de inclinación es de "
            "30° y la fuerza de fricción es de 10 N.\n"
            "a) Calcular la aceleración del cuerpo.\n"
            "b) ¿La fuerza normal es igual al peso del cuerpo?\n"
            "c) Si inicialmente estaba a una altura de 8 metros, ¿cuál es la velocidad al llegar al suelo?"
        ),
        "parts": [
            {
                "prompt": "a) Aceleración del cuerpo. Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 2.9, "tolerance": 0.01, "unit": "m/s²"},
                "answer": "2,9 m/s²",
            },
            {
                "prompt": "b) ¿La fuerza normal es igual al peso?",
                "check": {
                    "type": "choice",
                    "options": [
                        "No: N = P·cos 30° ≈ 42,4 N, menor que el peso (49 N)",
                        "Sí: N = P = 49 N, como en cualquier superficie",
                        "No: N = P·sen 30° = 24,5 N",
                        "No: N es mayor que el peso porque además hay fricción",
                    ],
                    "correct": 0,
                },
                "answer": "No: la normal equilibra solo la componente perpendicular del peso, N = 42,4 N.",
            },
            {
                "prompt": "c) Velocidad al llegar al suelo. Respondé solo con el número en m/s, con dos decimales.",
                "check": {"type": "numeric", "value": 9.63, "tolerance": 0.01, "unit": "m/s"},
                "answer": "9,63 m/s",
            },
        ],
        "hints": [
            "En el eje paralelo al plano, a favor del movimiento va `P·sen 30°` y en contra, la fricción.",
            "Para c) necesitás la distancia sobre el plano, no la altura: `d = h/sen 30°`.",
        ],
        "solution": [
            "Peso: `P = 5·9,8 = 49 N`. Componente paralela: `49·sen 30° = 24,5 N`.",
            "a) `24,5 − 10 = 5·a` → `a = 2,9 m/s²`.",
            "b) Eje perpendicular: `N = P·cos 30° = 49·0,866 ≈ 42,4 N`, que no es igual al peso: la normal solo compensa la componente perpendicular del peso.",
            "c) Distancia sobre el plano: `d = 8/sen 30° = 16 m`. Partiendo del reposo: `v² = 2·a·d = 2·2,9·16 = 92,8` → `v ≈ 9,63 m/s`.",
            "Coincide con el solucionario (2,9 m/s²; N = 42,4 N; 9,63 m/s).",
        ],
    },
    {
        "id": "f-dcl-rozamiento-plano-u5-10",
        "node": "f-dcl-rozamiento-plano",
        "kind": "problem",
        "level": 3,
        "source": "Física · Práctica U5, ej. 10",
        "title": "¿Hasta dónde sube por la rampa?",
        "statement": (
            "Una masa de 4 kg se desliza por una superficie horizontal con rozamiento con una velocidad inicial de "
            "4 m/s. Se encuentra a 2 m de una rampa inclinada que forma un ángulo de 30° con la horizontal. ¿Hasta qué "
            "altura del plano inclinado subirá la masa si la fuerza de fricción es de 2 N durante todo el recorrido? "
            "Usá g = 9,8 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) Velocidad con la que llega al pie de la rampa. Respondé solo con el número en m/s, con dos decimales.",
                "check": {"type": "numeric", "value": 3.74, "tolerance": 0.01, "unit": "m/s"},
                "answer": "3,74 m/s",
            },
            {
                "prompt": "b) Altura máxima que alcanza sobre la rampa. Respondé solo con el número en m, con dos decimales.",
                "check": {"type": "numeric", "value": 0.648, "tolerance": 0.01, "unit": "m"},
                "answer": "0,65 m",
            },
        ],
        "hints": [
            "En el tramo horizontal la única fuerza en la dirección del movimiento es la fricción: `a = −2/4`.",
            "En la rampa frenan juntas la componente del peso `m·g·sen 30°` y la fricción de 2 N.",
            "Con la distancia recorrida sobre la rampa, la altura es `h = d·sen 30°`.",
        ],
        "solution": [
            "Tramo horizontal: `a₁ = −2/4 = −0,5 m/s²`; `v₁² = 4² + 2·(−0,5)·2 = 14` → `v₁ ≈ 3,74 m/s`.",
            "En la rampa: `−m·g·sen 30° − 2 = m·a₂` → `a₂ = −(19,6 + 2)/4 = −5,4 m/s²`.",
            "Distancia sobre la rampa hasta detenerse: `0 = 14 + 2·(−5,4)·d` → `d = 14/10,8 ≈ 1,296 m`.",
            "Altura: `h = d·sen 30° ≈ 0,648 m ≈ 0,65 m`.",
            "El solucionario da h = 0,63 m; con g = 9,8 m/s² la cuenta da 0,648 m (con g = 10 daría 0,636 m). Se toma 0,65 m.",
        ],
    },
    # ======================================================================
    # UNIDAD 5 · GUÍA TP5 PARTE B
    # ======================================================================
    {
        "id": "f-dcl-rozamiento-plano-tp5b-1b",
        "node": "f-dcl-rozamiento-plano",
        "kind": "problem",
        "level": 1,
        "source": "Física · TP5 B, ej. 1b",
        "title": "Caja arrastrada con fuerza en kgf",
        "statement": (
            "Una caja de 28,7 kg se desplaza sobre una superficie horizontal por efecto de una fuerza F = 14,7 kgf "
            "paralela a la superficie. Si el coeficiente dinámico de frotamiento vale 0,361, ¿cuál será la aceleración "
            "de la caja? Usá g = 9,8 m/s² (1 kgf = 9,8 N)."
        ),
        "parts": [
            {
                "prompt": "Aceleración de la caja. Respondé solo con el número en m/s², con dos decimales.",
                "check": {"type": "numeric", "value": 1.48, "tolerance": 0.01, "unit": "m/s²"},
                "answer": "1,48 m/s²",
            },
        ],
        "hints": [
            "Pasá F a newton. En una superficie horizontal sin otras fuerzas verticales, `N = m·g`.",
            "Rozamiento dinámico: `f = μ·N`. Después, `F − f = m·a`.",
        ],
        "solution": [
            "`F = 14,7·9,8 = 144,06 N`.",
            "`N = 28,7·9,8 = 281,26 N`; `f = 0,361·281,26 ≈ 101,53 N`.",
            "`a = (144,06 − 101,53)/28,7 ≈ 1,48 m/s²`. Coincide con la grilla.",
        ],
    },
    {
        "id": "f-cuerpos-vinculados-tp5b-1e",
        "node": "f-cuerpos-vinculados",
        "kind": "problem",
        "level": 3,
        "source": "Física · TP5 B, ej. 1e",
        "title": "Dos bloques en planos opuestos",
        "statement": (
            "Calculá la tensión en la soga para el sistema de cuerpos de la figura, sin rozamiento, con ma = 8,00 kg "
            "y mb = 5,00 kg. Considerá el eje x positivo en el sentido del movimiento y g = 10 m/s².\n\n"
            "Descripción de la figura: un prisma con dos caras inclinadas que se juntan en una cúspide con una polea. "
            "ma está sobre la cara izquierda, inclinada 30° respecto de la horizontal; mb está sobre la cara derecha, "
            "inclinada 45°. Una soga, paralela a cada cara, los une pasando por la polea."
        ),
        "parts": [
            {
                "prompt": "a) ¿Hacia dónde se mueve el sistema si parte del reposo?",
                "check": {
                    "type": "choice",
                    "options": [
                        "ma baja por su plano y mb sube",
                        "mb baja por su plano y ma sube",
                        "Queda en equilibrio",
                    ],
                    "correct": 0,
                },
                "answer": "ma baja: su componente del peso (40 N) supera a la de mb (35,4 N).",
            },
            {
                "prompt": "b) Módulo de la aceleración. Respondé solo con el número en m/s², con dos decimales.",
                "check": {"type": "numeric", "value": 0.357, "tolerance": 0.01, "unit": "m/s²"},
                "answer": "0,36 m/s²",
            },
            {
                "prompt": "c) Tensión de la soga. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 37.14, "tolerance": 0.01, "unit": "N"},
                "answer": "37,1 N",
            },
        ],
        "hints": [
            "Compará las componentes de los pesos paralelas a cada plano: `ma·g·sen 30°` y `mb·g·sen 45°`.",
            "Sistema: `ma·g·sen 30° − mb·g·sen 45° = (ma + mb)·a`. Después, la tensión con cualquiera de los dos bloques.",
        ],
        "solution": [
            "Componentes paralelas: `8·10·sen 30° = 40 N` (ma) y `5·10·sen 45° ≈ 35,36 N` (mb). Gana ma: baja por su plano y mb sube.",
            "Sistema: `40 − 35,36 = 13·a` → `a ≈ 0,357 m/s²`.",
            "Bloque mb (sube): `T − 35,36 = 5·0,357` → `T ≈ 37,14 N`. Con ma: `40 − T = 8·0,357` → `T ≈ 37,14 N`.",
            "La grilla marca 37,2 N; el valor sin redondeos intermedios es 37,1 N.",
        ],
    },
    {
        "id": "f-dcl-rozamiento-plano-tp5b-1f",
        "node": "f-dcl-rozamiento-plano",
        "kind": "problem",
        "level": 2,
        "source": "Física · TP5 B, ej. 1f",
        "title": "Bloque empujado por dos fuerzas",
        "statement": (
            "Calculá la aceleración que adquiere el bloque mostrado en la figura, considerando g = 10,0 m/s².\n\n"
            "Descripción de la figura: un bloque de 2,00 kg sobre un piso horizontal con coeficiente de rozamiento "
            "μ = 0,200. Sobre su cara izquierda actúa una fuerza horizontal de 100 N que lo empuja hacia la derecha. "
            "Sobre su cara derecha actúa una fuerza de 10,0 N que empuja al bloque hacia abajo y hacia la izquierda: "
            "su recta de acción forma 37° con la horizontal (dirección 217°)."
        ),
        "parts": [
            {
                "prompt": "a) Reacción normal del piso. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 26.0, "tolerance": 0.01, "unit": "N"},
                "answer": "26,0 N",
            },
            {
                "prompt": "b) Aceleración del bloque. Respondé solo con el número en m/s², con un decimal.",
                "check": {"type": "numeric", "value": 43.4, "tolerance": 0.01, "unit": "m/s²"},
                "answer": "43,4 m/s²",
            },
        ],
        "hints": [
            "La fuerza de 10,0 N tiene una componente vertical hacia abajo que aumenta la normal: `N = m·g + 10·sen 37°`.",
            "El bloque se mueve hacia la derecha: el rozamiento `μ·N` y la componente horizontal de la fuerza de 10 N apuntan hacia la izquierda.",
        ],
        "solution": [
            "Eje y: `N − 20 − 10·sen 37° = 0` → `N = 20 + 6,02 ≈ 26,0 N`.",
            "Rozamiento: `f = 0,200·26,02 ≈ 5,20 N`, hacia la izquierda.",
            "Eje x: `100 − 10·cos 37° − 5,20 = 2·a` → `100 − 7,99 − 5,20 = 86,81 = 2·a` → `a ≈ 43,4 m/s²`.",
            "Coincide con la grilla (43,4 m/s²).",
        ],
    },
    {
        "id": "f-leyes-newton-tp5b-2a",
        "node": "f-leyes-newton",
        "kind": "problem",
        "level": 2,
        "source": "Física · TP5 B, ej. 2a",
        "title": "Barco llevado por dos remolcadores",
        "statement": (
            "Dos remolcadores llevan un barco de 1000 toneladas hasta una dársena, tirando cada uno con una fuerza "
            "constante de 2·10¹⁰ dina. La fuerza de rozamiento que ejerce el agua sobre el barco es de 10⁵ N.\n\n"
            "Descripción de la figura: las dos fuerzas F1 y F2 tiran hacia adelante, simétricas respecto del eje del "
            "barco: cada una forma 37° con ese eje, una hacia cada lado. El rozamiento actúa a lo largo del eje, hacia "
            "atrás."
        ),
        "parts": [
            {
                "prompt": "a) Fuerza total que hacen los remolcadores sobre el barco. Respondé solo con el número en N (podés usar notación científica).",
                "check": {"type": "numeric", "value": 319454, "tolerance": 0.01, "unit": "N"},
                "answer": "319454 N (≈ 3,19·10⁵ N), hacia adelante",
            },
            {
                "prompt": "b) Aceleración del barco. Respondé solo con el número en m/s², con dos decimales.",
                "check": {"type": "numeric", "value": 0.2195, "tolerance": 0.01, "unit": "m/s²"},
                "answer": "0,22 m/s²",
            },
        ],
        "hints": [
            "Pasá unidades: `1 dina = 10⁻⁵ N` y `1 t = 1000 kg`.",
            "Las componentes laterales de F1 y F2 se cancelan; las componentes a lo largo del eje se suman: `2·F·cos 37°`.",
        ],
        "solution": [
            "Unidades: `F = 2·10¹⁰ dina = 2·10⁵ N`; `m = 1000 t = 10⁶ kg`.",
            "Componentes perpendiculares al eje: `±F·sen 37°`, se anulan. Componentes a lo largo del eje: `2·2·10⁵·cos 37° ≈ 3,19·10⁵ N`.",
            "Segunda ley a lo largo del eje: `3,1945·10⁵ − 10⁵ = 10⁶·a` → `a ≈ 0,22 m/s²`.",
            "La grilla da 0,2 m/s² (redondeado a una cifra).",
        ],
    },
    {
        "id": "f-leyes-newton-tp5b-2b",
        "node": "f-leyes-newton",
        "kind": "problem",
        "level": 1,
        "source": "Física · TP5 B, ej. 2b",
        "title": "Niño que salta",
        "statement": (
            "Un niño de 20 kg salta hacia arriba con una aceleración de despegue de 15 m/s². ¿Cuál es el módulo de la "
            "fuerza que el piso ejerció sobre el niño durante el despegue? Usá g = 9,8 m/s²."
        ),
        "parts": [
            {
                "prompt": "Fuerza del piso sobre el niño. Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 496, "tolerance": 0.01, "unit": "N"},
                "answer": "496 N",
            },
        ],
        "hints": [
            "Durante el despegue actúan el peso (abajo) y la normal del piso (arriba); la aceleración es hacia arriba.",
        ],
        "solution": [
            "Eje + hacia arriba: `N − m·g = m·a`.",
            "`N = m·(g + a) = 20·(9,8 + 15) = 20·24,8 = 496 N`.",
            "La grilla da 492 N, que no sale ni con g = 9,8 (496 N) ni con g = 10 (500 N); probablemente sea un error de cuenta.",
        ],
    },
    {
        "id": "f-cuerpos-vinculados-tp5b-2d",
        "node": "f-cuerpos-vinculados",
        "kind": "problem",
        "level": 2,
        "source": "Física · TP5 B, ej. 2d",
        "title": "Dos bloques tironeados en sentidos opuestos",
        "statement": (
            "En el siguiente sistema se aplica una fuerza de 30 N al primer bloque y 10 N al segundo. Calculá la "
            "tensión en la cuerda en kgf y la aceleración del sistema (no hay rozamiento). m1 = m2 = 10 kg.\n\n"
            "Descripción de la figura: m1 a la izquierda y m2 a la derecha, unidos por una cuerda horizontal. La fuerza "
            "de 30 N tira de m1 hacia la izquierda y la de 10 N tira de m2 hacia la derecha. Usá 1 kgf = 9,8 N."
        ),
        "parts": [
            {
                "prompt": "a) Aceleración del sistema. Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 1, "tolerance": 0.01, "unit": "m/s²"},
                "answer": "1 m/s², hacia la izquierda",
            },
            {
                "prompt": "b) Tensión de la cuerda. Respondé solo con el número en kgf, con dos decimales.",
                "check": {"type": "numeric", "value": 2.04, "tolerance": 0.01, "unit": "kgf"},
                "answer": "2,04 kgf (20 N)",
            },
        ],
        "hints": [
            "Gana la fuerza mayor: el sistema acelera hacia la izquierda con `(30 − 10)/(m1 + m2)`.",
            "Para la tensión, mirá m2: la cuerda lo arrastra hacia la izquierda contra la fuerza de 10 N.",
        ],
        "solution": [
            "Sistema (eje + hacia la izquierda): `30 − 10 = 20·a` → `a = 1 m/s²`, hacia la izquierda.",
            "Bloque m2: `T − 10 = 10·1` → `T = 20 N`.",
            "En kgf: `20/9,8 ≈ 2,04 kgf`. Coincide con la grilla.",
        ],
    },
    {
        "id": "f-dcl-rozamiento-plano-tp5b-2e",
        "node": "f-dcl-rozamiento-plano",
        "kind": "problem",
        "level": 1,
        "source": "Física · TP5 B, ej. 2e",
        "title": "Cuerpo que se desliza a velocidad constante",
        "statement": (
            "Un cuerpo de masa 10 kg se mueve con una velocidad constante de 5 m/s sobre una superficie horizontal. El "
            "coeficiente de roce dinámico entre el cuerpo y la superficie es 0,20. Usá g = 9,8 m/s².\n"
            "1) ¿Qué fuerza horizontal se requiere para mantener el movimiento?\n"
            "2) Si se suprime la fuerza, ¿cuánto tardará el bloque en detenerse?"
        ),
        "parts": [
            {
                "prompt": "a) Fuerza horizontal necesaria. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 19.6, "tolerance": 0.01, "unit": "N"},
                "answer": "19,6 N",
            },
            {
                "prompt": "b) Tiempo hasta detenerse. Respondé solo con el número en s, con dos decimales.",
                "check": {"type": "numeric", "value": 2.55, "tolerance": 0.01, "unit": "s"},
                "answer": "2,55 s",
            },
        ],
        "hints": [
            "Velocidad constante: la fuerza aplicada iguala al rozamiento `μ·m·g`.",
            "Sin la fuerza, el rozamiento es la fuerza neta: `a = −μ·g`.",
        ],
        "solution": [
            "a) MRU → `ΣF = 0`: `F = μ·m·g = 0,20·10·9,8 = 19,6 N`.",
            "b) Sin F: `−19,6 = 10·a` → `a = −1,96 m/s²`.",
            "`0 = 5 − 1,96·t` → `t ≈ 2,55 s`. Coincide con la grilla.",
        ],
    },
    {
        "id": "f-cuerpos-vinculados-tp5b-2f",
        "node": "f-cuerpos-vinculados",
        "kind": "problem",
        "level": 2,
        "source": "Física · TP5 B, ej. 2f",
        "title": "Tres bloques colgados que suben",
        "statement": (
            "Calculá la tensión de la cuerda que sostiene al último bloque (considerá g = 10 m/s², siendo m1 = 5 kg, "
            "m2 = 1 kg y m3 = 9 kg).\n\n"
            "Descripción de la figura: arriba está m3, del que se tira con F = 200 N vertical hacia arriba; de m3 cuelga "
            "m2 con una cuerda, y de m2 cuelga m1 (el último bloque) con otra cuerda. Todo el conjunto sube."
        ),
        "parts": [
            {
                "prompt": "a) Aceleración del conjunto. Respondé solo con el número en m/s², con dos decimales.",
                "check": {"type": "numeric", "value": 3.33, "tolerance": 0.01, "unit": "m/s²"},
                "answer": "3,33 m/s² (= 10/3), hacia arriba",
            },
            {
                "prompt": "b) Tensión de la cuerda que une m3 con m2. Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 80, "tolerance": 0.01, "unit": "N"},
                "answer": "80 N",
            },
            {
                "prompt": "c) Tensión de la cuerda que sostiene al último bloque (m1). Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 66.7, "tolerance": 0.01, "unit": "N"},
                "answer": "66,7 N (= 200/3)",
            },
        ],
        "hints": [
            "Conjunto: `F − (m1 + m2 + m3)·g = (m1 + m2 + m3)·a`.",
            "Cada cuerda sostiene y acelera a todo lo que cuelga debajo de ella: `T = m_debajo·(g + a)`.",
        ],
        "solution": [
            "Conjunto (15 kg): `200 − 150 = 15·a` → `a = 10/3 ≈ 3,33 m/s²`.",
            "Cuerda m3–m2 (sostiene m2 + m1 = 6 kg): `T = 6·(10 + 10/3) = 80 N`.",
            "Cuerda m2–m1 (sostiene m1 = 5 kg): `T = 5·(10 + 10/3) = 200/3 ≈ 66,7 N`.",
            "La grilla da 200/3 N para la cuerda del último bloque. El inciso b) es un agregado para practicar.",
        ],
    },
    {
        "id": "f-cuerpos-vinculados-tp5b-2h",
        "node": "f-cuerpos-vinculados",
        "kind": "problem",
        "level": 2,
        "source": "Física · TP5 B, ej. 2h",
        "title": "Masa en la mesa con rozamiento y masa colgante",
        "statement": (
            "Una masa m1 sobre una mesa totalmente horizontal está sujeta a otra masa m2 por medio de una cuerda que "
            "pasa por una polea en el borde de la mesa y de la que cuelga m2. El coeficiente de rozamiento entre m1 y "
            "la mesa es μ = 0,3. Determiná la aceleración del sistema y la tensión de la cuerda. Considerá el eje x "
            "positivo en el sentido del movimiento, g = 10 m/s², m1 = 1,00 kg y m2 = 8,00 kg."
        ),
        "parts": [
            {
                "prompt": "a) Aceleración del sistema. Respondé solo con el número en m/s², con dos decimales.",
                "check": {"type": "numeric", "value": 8.56, "tolerance": 0.01, "unit": "m/s²"},
                "answer": "8,56 m/s²",
            },
            {
                "prompt": "b) Tensión de la cuerda. Respondé solo con el número en N, con un decimal.",
                "check": {"type": "numeric", "value": 11.6, "tolerance": 0.01, "unit": "N"},
                "answer": "11,6 N",
            },
        ],
        "hints": [
            "El peso de m2 mueve el sistema; el rozamiento sobre m1 (`μ·m1·g`) se opone.",
            "Para la tensión, usá m2: `m2·g − T = m2·a`.",
        ],
        "solution": [
            "Rozamiento sobre m1: `f = 0,3·1,00·10 = 3 N`. Peso de m2: `80 N`.",
            "Sistema: `80 − 3 = 9·a` → `a = 77/9 ≈ 8,56 m/s²`.",
            "Bloque m2: `T = 8·(10 − 8,556) ≈ 11,6 N`. (Con m1: `T − 3 = 1·8,556` → `T ≈ 11,6 N`.)",
            "Coincide con la grilla (8,56 m/s² y 11,6 N).",
        ],
    },
]
