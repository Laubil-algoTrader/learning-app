"""BORRADOR · Ejercicios del material oficial del ingreso (UNCuyo 2027), Matemática, TP4 a TP7.

TP4 Polinomios · TP5 Funciones · TP6 Logaritmos y exponenciales · TP7 Trigonometría.
Ningún TP trae respuestas: todas se resolvieron a mano y se verificaron con Python.
"""


def _n(prompt: str, value, answer: str, tol: float = 0, unit: str = "") -> dict:
    return {"prompt": prompt, "check": {"type": "numeric", "value": value, "tolerance": tol, "unit": unit}, "answer": answer}


def _c(prompt: str, options: list[str], answer: str) -> dict:
    """La primera opción es la correcta (la app las mezcla)."""
    return {"prompt": prompt, "check": {"type": "choice", "options": options, "correct": 0}, "answer": answer}


def _p(id_: str, node: str, level: int, source: str, title: str, statement: str, parts, hints, solution) -> dict:
    return {
        "id": f"{node}-{id_}",
        "node": node,
        "kind": "problem",
        "level": level,
        "source": source,
        "title": title,
        "statement": statement,
        "parts": parts,
        "hints": hints,
        "solution": solution,
    }


FACT = "a2-polinomios-factorizacion"
CASOS = "a2-casos-factoreo"
RAC = "a2-expresiones-racionales"
ECU = "a2-ecuaciones-avanzadas"
INEC = "a2-inecuaciones-avanzadas"
CIRC = "g-ecuacion-circulo"

# ======================================================================
# TP4 · POLINOMIOS
# ======================================================================
TP4 = [
    # ---------- Ej. 27: factorización combinada ----------
    _p(
        "tp4-27-cubos", FACT, 2, "Matemática · TP4, ej. 27 c, h, k",
        "Factor común y suma o diferencia de cubos",
        "Factorizá los siguientes polinomios hasta llegar a los factores primos:\n\n"
        "c) `5x³ + 5`\n\nh) `x⁸ − x⁵`\n\nk) `x⁴a + xa`",
        [
            _c("c) ¿Cuál es la factorización de `5x³ + 5`?",
               ["5(x + 1)(x² − x + 1)", "5(x + 1)(x² + x + 1)", "5(x + 1)³", "(5x + 5)(x² + 1)"],
               "5(x + 1)(x² − x + 1)"),
            _c("h) ¿Cuál es la factorización de `x⁸ − x⁵`?",
               ["x⁵(x − 1)(x² + x + 1)", "x⁵(x − 1)(x² − x + 1)", "x⁵(x − 1)³", "x⁵(x + 1)(x² − x + 1)"],
               "x⁵(x − 1)(x² + x + 1)"),
            _c("k) ¿Cuál es la factorización de `x⁴a + xa`?",
               ["ax(x + 1)(x² − x + 1)", "ax(x + 1)(x² + x + 1)", "ax(x + 1)³", "ax³(x + 1)"],
               "ax(x + 1)(x² − x + 1)"),
        ],
        [
            "Primero sacá factor común: el número o la letra con la menor potencia.",
            "Lo que queda adentro es una suma o diferencia de cubos: `a³ + b³ = (a + b)(a² − ab + b²)` y `a³ − b³ = (a − b)(a² + ab + b²)`.",
        ],
        [
            "c) Factor común 5: `5x³ + 5 = 5(x³ + 1)`.",
            "`x³ + 1` es suma de cubos (`x³ + 1³`): `x³ + 1 = (x + 1)(x² − x + 1)`. Resultado: `5(x + 1)(x² − x + 1)`.",
            "h) Factor común `x⁵` (la menor potencia): `x⁸ − x⁵ = x⁵(x³ − 1)`.",
            "`x³ − 1` es diferencia de cubos: `(x − 1)(x² + x + 1)`. Resultado: `x⁵(x − 1)(x² + x + 1)`.",
            "k) Factor común `ax`: `x⁴a + xa = ax(x³ + 1) = ax(x + 1)(x² − x + 1)`.",
            "Los trinomios `x² ± x + 1` son primos en IR (discriminante `1 − 4 < 0`). Error típico: escribir `(x + 1)³` en lugar de la suma de cubos; `(x + 1)³` tiene términos `3x² + 3x` que no aparecen.",
        ],
    ),
    _p(
        "tp4-27-cuadrados", FACT, 2, "Matemática · TP4, ej. 27 a, e, g",
        "Cuatrinomio cubo, trinomio cuadrado y diferencia de cuadrados",
        "Factorizá los siguientes polinomios hasta llegar a los factores primos (con coeficientes racionales):\n\n"
        "a) `x⁶ − 6x⁴ + 12x² − 8`\n\ne) `x⁴ − 2x² + 1`\n\ng) `x⁷ − x⁵`",
        [
            _c("a) ¿Cuál es la factorización de `x⁶ − 6x⁴ + 12x² − 8`?",
               ["(x² − 2)³", "(x − 2)³(x + 2)³", "(x² − 2)²(x² + 2)", "(x² + 2)³"],
               "(x² − 2)³"),
            _c("e) ¿Cuál es la factorización de `x⁴ − 2x² + 1`?",
               ["(x − 1)²(x + 1)²", "(x² + 1)²", "(x − 1)⁴", "(x − 1)(x + 1)(x² + 1)"],
               "(x − 1)²(x + 1)²"),
            _c("g) ¿Cuál es la factorización de `x⁷ − x⁵`?",
               ["x⁵(x − 1)(x + 1)", "x⁵(x − 1)²", "x⁵(x² + 1)", "x⁵(x + 1)²"],
               "x⁵(x − 1)(x + 1)"),
        ],
        [
            "a) Tiene cuatro términos con `x⁶ = (x²)³` y `−8 = (−2)³`: probá cuatrinomio cubo perfecto.",
            "e) Es un trinomio cuadrado perfecto en `x²`; después, lo que queda adentro es una diferencia de cuadrados.",
        ],
        [
            "a) `x⁶ = (x²)³` y `−8 = (−2)³`. Dobles productos: `3·(x²)²·(−2) = −6x⁴` ✓ y `3·x²·(−2)² = 12x²` ✓. Entonces `x⁶ − 6x⁴ + 12x² − 8 = (x² − 2)³`.",
            "`x² − 2` no se factoriza con coeficientes racionales (en IR sería `(x − √2)(x + √2)`, y quedaría `(x − √2)³(x + √2)³`).",
            "e) `x⁴ = (x²)²`, `1 = 1²` y `−2·x²·1 = −2x²` ✓: `x⁴ − 2x² + 1 = (x² − 1)²`.",
            "`x² − 1 = (x − 1)(x + 1)`, así que `(x² − 1)² = (x − 1)²(x + 1)²`.",
            "g) Factor común `x⁵`: `x⁷ − x⁵ = x⁵(x² − 1) = x⁵(x − 1)(x + 1)`.",
            "Error típico en a): confundir `(x² − 2)³` con `(x − 2)³(x + 2)³ = (x² − 4)³`; su término independiente sería `−64`, no `−8`.",
        ],
    ),
    _p(
        "tp4-27-grupos", FACT, 3, "Matemática · TP4, ej. 27 l, m, q",
        "Factor común por grupos y casos combinados",
        "Factorizá los siguientes polinomios hasta llegar a los factores primos:\n\n"
        "l) `32x⁵ − 8x³ − 4x² + 1`\n\nm) `x⁴ + 2x³ + 8x + 16`\n\nq) `x⁴ + x³ + x + 1`",
        [
            _c("l) ¿Cuál es la factorización de `32x⁵ − 8x³ − 4x² + 1`?",
               ["(2x − 1)²(2x + 1)(4x² + 2x + 1)", "(2x − 1)(2x + 1)²(4x² + 2x + 1)",
                "(2x − 1)²(2x + 1)(4x² − 2x + 1)", "(4x² − 1)(8x³ + 1)"],
               "(2x − 1)²(2x + 1)(4x² + 2x + 1)"),
            _c("m) ¿Cuál es la factorización de `x⁴ + 2x³ + 8x + 16`?",
               ["(x + 2)²(x² − 2x + 4)", "(x + 2)²(x² + 2x + 4)", "(x + 2)(x − 2)(x² + 2x + 4)", "(x + 2)⁴"],
               "(x + 2)²(x² − 2x + 4)"),
            _c("q) ¿Cuál es la factorización de `x⁴ + x³ + x + 1`?",
               ["(x + 1)²(x² − x + 1)", "(x + 1)²(x² + x + 1)", "(x + 1)(x − 1)(x² + x + 1)", "(x + 1)⁴"],
               "(x + 1)²(x² − x + 1)"),
        ],
        [
            "Agrupá de a dos términos y sacá factor común en cada grupo: tiene que aparecer el mismo binomio.",
            "l) Agrupá `(32x⁵ − 8x³) + (−4x² + 1)`; m) y q) agrupá los dos primeros y los dos últimos.",
            "Después de agrupar te quedan una diferencia de cuadrados y sumas o diferencias de cubos.",
        ],
        [
            "l) `32x⁵ − 8x³ − 4x² + 1 = 8x³(4x² − 1) − (4x² − 1) = (4x² − 1)(8x³ − 1)`.",
            "`4x² − 1 = (2x − 1)(2x + 1)` y `8x³ − 1 = (2x)³ − 1³ = (2x − 1)(4x² + 2x + 1)`. Juntando: `(2x − 1)²(2x + 1)(4x² + 2x + 1)`.",
            "m) `x⁴ + 2x³ + 8x + 16 = x³(x + 2) + 8(x + 2) = (x + 2)(x³ + 8)`.",
            "`x³ + 8 = (x + 2)(x² − 2x + 4)`, entonces queda `(x + 2)²(x² − 2x + 4)`.",
            "q) `x⁴ + x³ + x + 1 = x³(x + 1) + (x + 1) = (x + 1)(x³ + 1) = (x + 1)²(x² − x + 1)`.",
            "Verificación rápida de m) en `x = 1`: `1 + 2 + 8 + 16 = 27` y `(3)²(1 − 2 + 4) = 9·3 = 27` ✓. Los trinomios de grado 2 que quedan tienen discriminante negativo: son primos.",
        ],
    ),
    _p(
        "tp4-27-parametro", FACT, 3, "Matemática · TP4, ej. 27 n, o, p",
        "Factorización con dos letras",
        "Factorizá los siguientes polinomios hasta llegar a los factores primos (la variable es `x`; `y` y `a` son letras que se tratan como números):\n\n"
        "n) `4x² + 4xy + y²`\n\no) `8x³ + 20x² − 2a²x − 5a²`\n\np) `x⁴ + ax³ − x − a`",
        [
            _c("n) ¿Cuál es la factorización de `4x² + 4xy + y²`?",
               ["(2x + y)²", "(2x − y)²", "(4x + y)²", "(2x + y)(2x − y)"], "(2x + y)²"),
            _c("o) ¿Cuál es la factorización de `8x³ + 20x² − 2a²x − 5a²`?",
               ["(2x + 5)(2x − a)(2x + a)", "(2x + 5)(2x − a)²", "(2x − 5)(2x − a)(2x + a)", "(2x + 5)(4x² + a²)"],
               "(2x + 5)(2x − a)(2x + a)"),
            _c("p) ¿Cuál es la factorización de `x⁴ + ax³ − x − a`?",
               ["(x + a)(x − 1)(x² + x + 1)", "(x + a)(x + 1)(x² − x + 1)", "(x + a)(x − 1)³", "(x − a)(x − 1)(x² + x + 1)"],
               "(x + a)(x − 1)(x² + x + 1)"),
        ],
        [
            "n) Fijate si los extremos son cuadrados y el término del medio es el doble producto de sus bases.",
            "o) y p) Agrupá de a dos: en o) `4x²(…) − a²(…)`, en p) `x³(…) − (…)`.",
        ],
        [
            "n) `4x² = (2x)²`, `y² = y²` y `2·2x·y = 4xy` ✓. Entonces `4x² + 4xy + y² = (2x + y)²`.",
            "o) `8x³ + 20x² − 2a²x − 5a² = 4x²(2x + 5) − a²(2x + 5) = (2x + 5)(4x² − a²)`.",
            "`4x² − a²` es diferencia de cuadrados: `(2x − a)(2x + a)`. Resultado: `(2x + 5)(2x − a)(2x + a)`.",
            "p) `x⁴ + ax³ − x − a = x³(x + a) − 1·(x + a) = (x + a)(x³ − 1)`.",
            "`x³ − 1 = (x − 1)(x² + x + 1)`. Resultado: `(x + a)(x − 1)(x² + x + 1)`.",
            "Verificación de o) con `x = 1`, `a = 1`: `8 + 20 − 2 − 5 = 21` y `7·1·3 = 21` ✓.",
        ],
    ),
    # ---------- Ej. 21 y 22: trinomio cuadrado perfecto ----------
    _p(
        "tp4-21", CASOS, 1, "Matemática · TP4, ej. 21 a, c, f",
        "Trinomio cuadrado perfecto",
        "Factorizá los siguientes polinomios:\n\n"
        "a) `4x⁴ + 20x² + 25`\n\nc) `y⁴ − 2y³ + y²`\n\nf) `¼x²y⁴ + 4/25 + ⅖xy²`",
        [
            _c("a) ¿Cuál es la factorización de `4x⁴ + 20x² + 25`?",
               ["(2x² + 5)²", "(2x + 5)²", "(4x² + 5)²", "(2x² − 5)²"], "(2x² + 5)²"),
            _c("c) ¿Cuál es la factorización de `y⁴ − 2y³ + y²`?",
               ["y²(y − 1)²", "y²(y + 1)²", "(y² − 1)²", "y²(y − 1)(y + 1)"], "y²(y − 1)²"),
            _c("f) ¿Cuál es la factorización de `¼x²y⁴ + 4/25 + ⅖xy²`?",
               ["(½xy² + ⅖)²", "(½xy² − ⅖)²", "(¼xy² + ⅖)²", "(½xy + ⅖)²"], "(½xy² + ⅖)²"),
        ],
        [
            "Buscá los dos términos que son cuadrados, tomá sus bases y verificá que el tercero sea el doble producto de las bases (con su signo).",
            "En c) primero sacá factor común `y²`.",
        ],
        [
            "a) `4x⁴ = (2x²)²` y `25 = 5²`. Doble producto: `2·2x²·5 = 20x²` ✓. Entonces `4x⁴ + 20x² + 25 = (2x² + 5)²`.",
            "c) Factor común `y²`: `y⁴ − 2y³ + y² = y²(y² − 2y + 1)`.",
            "`y² − 2y + 1` es TCP: bases `y` y `1`, doble producto `−2y` ✓. Resultado: `y²(y − 1)²`.",
            "f) `¼x²y⁴ = (½xy²)²` y `4/25 = (⅖)²`. Doble producto: `2·½xy²·⅖ = ⅖xy²` ✓.",
            "Resultado: `(½xy² + ⅖)²`. El signo del binomio es `+` porque el doble producto es positivo.",
        ],
    ),
    _p(
        "tp4-22", CASOS, 2, "Matemática · TP4, ej. 22 a, b, d",
        "Completar un trinomio cuadrado perfecto",
        "Completá los polinomios con el término que falta para que sean trinomios cuadrados perfectos:\n\n"
        "a) `16/9 x⁴ + 1 + …`\n\nb) `25/4 x⁴ − 4x²y⁴ + …`\n\nd) `x²y² − 8xyz + …`",
        [
            _n("a) El término que falta es de la forma `k·x²` (tomá el signo positivo). ¿Cuánto vale `k`? Respondé con una fracción o decimal.",
               8 / 3, "8/3 (el término es `+8/3 x²`; también sirve `−8/3 x²`)", 0.01),
            _n("b) El término que falta es de la forma `k·y⁸`. ¿Cuánto vale `k`?", 16 / 25, "16/25 (el término es `16/25 y⁸`)", 0.01),
            _n("d) El término que falta es de la forma `k·z²`. ¿Cuánto vale `k`?", 16, "16 (el término es `16z²`)"),
        ],
        [
            "En a) faltan el doble producto: las bases son las raíces de los cuadrados que ya están.",
            "En b) y d) falta un cuadrado: despejá la base `b` del doble producto `2·a·b`.",
        ],
        [
            "a) `16/9 x⁴ = (4/3 x²)²` y `1 = 1²`. Falta el doble producto: `2·(4/3 x²)·1 = 8/3 x²`. Queda `(4/3 x² + 1)²` (o `(4/3 x² − 1)²` con `−8/3 x²`). También sería un trinomio cuadrado perfecto con `+64/81 x⁸`, tomando `16/9 x⁴` como doble producto, pero el inciso pide un término de la forma `k·x²`.",
            "b) `25/4 x⁴ = (5/2 x²)²`. El doble producto es `2·(5/2 x²)·b = 5x²·b = 4x²y⁴`, entonces `b = 4/5 y⁴`.",
            "Falta `b² = (4/5 y⁴)² = 16/25 y⁸`, y el trinomio es `(5/2 x² − 4/5 y⁴)²`.",
            "d) `x²y² = (xy)²`. Doble producto: `2·xy·b = 8xyz` → `b = 4z`. Falta `(4z)² = 16z²`: `(xy − 4z)²`.",
            "(El ítem c) se resuelve igual: `9a² + 12ab + 4b² = (3a + 2b)²`.)",
        ],
    ),
    # ---------- Ej. 23: cuatrinomio cubo perfecto ----------
    _p(
        "tp4-23", CASOS, 2, "Matemática · TP4, ej. 23 a, c, d",
        "Cuatrinomio cubo perfecto",
        "Factorizá los siguientes polinomios:\n\n"
        "a) `27x³ + 8 + 54x² + 36x`\n\nc) `x³ + 3xy² + y³ + 3x²y`\n\nd) `1 − 27m³ − 9m + 27m²`",
        [
            _c("a) ¿Cuál es la factorización de `27x³ + 8 + 54x² + 36x`?",
               ["(3x + 2)³", "(3x − 2)³", "(2x + 3)³", "27(x + 2)³"], "(3x + 2)³"),
            _c("c) ¿Cuál es la factorización de `x³ + 3xy² + y³ + 3x²y`?",
               ["(x + y)³", "(x − y)³", "(x + y)(x² − xy + y²)", "(x + y)²(x − y)"], "(x + y)³"),
            _c("d) ¿Cuál es la factorización de `1 − 27m³ − 9m + 27m²`?",
               ["(1 − 3m)³", "(1 + 3m)³", "(3m − 1)³", "(1 − 3m)(1 + 3m + 9m²)"], "(1 − 3m)³"),
        ],
        [
            "Ordená el polinomio y buscá los dos cubos de los extremos: sus bases `a` y `b`.",
            "Verificá los dos términos del medio: tienen que ser `3a²b` y `3ab²`.",
        ],
        [
            "a) Ordenado: `27x³ + 54x² + 36x + 8`. Cubos: `27x³ = (3x)³` y `8 = 2³`.",
            "Controles: `3·(3x)²·2 = 54x²` ✓ y `3·3x·2² = 36x` ✓. Resultado: `(3x + 2)³`.",
            "c) Ordenado: `x³ + 3x²y + 3xy² + y³ = (x + y)³` (todos los signos `+`).",
            "d) Ordenado según potencias decrecientes de m: `−27m³ + 27m² − 9m + 1`. Cubos: `1 = 1³` y `−27m³ = (−3m)³`.",
            "Controles: `3·1²·(−3m) = −9m` ✓ y `3·1·(−3m)² = 27m²` ✓. Resultado: `(1 − 3m)³`.",
            "Ojo: `(3m − 1)³ = −(1 − 3m)³`, no es lo mismo. Y `(1 − 3m)(1 + 3m + 9m²) = 1 − 27m³` es solo la diferencia de cubos, le faltan los términos del medio.",
        ],
    ),
    # ---------- Ej. 25: suma o diferencia de potencias ----------
    _p(
        "tp4-25", CASOS, 2, "Matemática · TP4, ej. 25 a, c, d",
        "Suma o diferencia de potencias de igual exponente",
        "Factorizá los siguientes polinomios:\n\na) `y⁵ − 243`\n\nc) `a⁵ + 32`\n\nd) `1 + 128x⁷`",
        [
            _c("a) ¿Cuál es la factorización de `y⁵ − 243`?",
               ["(y − 3)(y⁴ + 3y³ + 9y² + 27y + 81)", "(y − 3)(y⁴ − 3y³ + 9y² − 27y + 81)",
                "(y + 3)(y⁴ − 3y³ + 9y² − 27y + 81)", "(y − 3)⁵"],
               "(y − 3)(y⁴ + 3y³ + 9y² + 27y + 81)"),
            _c("c) ¿Cuál es la factorización de `a⁵ + 32`?",
               ["(a + 2)(a⁴ − 2a³ + 4a² − 8a + 16)", "(a + 2)(a⁴ + 2a³ + 4a² + 8a + 16)",
                "(a − 2)(a⁴ + 2a³ + 4a² + 8a + 16)", "(a + 2)⁵"],
               "(a + 2)(a⁴ − 2a³ + 4a² − 8a + 16)"),
            _c("d) ¿Cuál es la factorización de `1 + 128x⁷`?",
               ["(1 + 2x)(1 − 2x + 4x² − 8x³ + 16x⁴ − 32x⁵ + 64x⁶)",
                "(1 + 2x)(1 + 2x + 4x² + 8x³ + 16x⁴ + 32x⁵ + 64x⁶)",
                "(1 − 2x)(1 + 2x + 4x² + 8x³ + 16x⁴ + 32x⁵ + 64x⁶)", "(1 + 2x)⁷"],
               "(1 + 2x)(1 − 2x + 4x² − 8x³ + 16x⁴ − 32x⁵ + 64x⁶)"),
        ],
        [
            "Escribí cada término como potencia de igual exponente: `243 = 3⁵`, `32 = 2⁵`, `128x⁷ = (2x)⁷`.",
            "Diferencia `aⁿ − bⁿ`: divisible por `a − b`, cociente con todos los signos `+`. Suma con n impar: divisible por `a + b`, cociente con signos alternados.",
        ],
        [
            "a) `y⁵ − 243 = y⁵ − 3⁵`. Es divisible por `y − 3` (y por Ruffini el cociente es `y⁴ + 3y³ + 9y² + 27y + 81`).",
            "Resultado: `(y − 3)(y⁴ + 3y³ + 9y² + 27y + 81)`.",
            "c) `a⁵ + 32 = a⁵ + 2⁵`, exponente impar: divisible por `a + 2`. Cociente con signos alternados: `a⁴ − 2a³ + 4a² − 8a + 16`.",
            "d) `1 + 128x⁷ = 1⁷ + (2x)⁷`, exponente impar: divisible por `1 + 2x`. Cociente: potencias de `2x` de 0 a 6 con signos alternados: `1 − 2x + 4x² − 8x³ + 16x⁴ − 32x⁵ + 64x⁶`.",
            "Verificación de a) en `y = 1`: `1 − 243 = −242` y `(−2)(1 + 3 + 9 + 27 + 81) = −2·121 = −242` ✓.",
        ],
    ),
    # ---------- Ej. 26: trinomio de segundo grado ----------
    _p(
        "tp4-26", CASOS, 1, "Matemática · TP4, ej. 26 a, c, d",
        "Trinomio de segundo grado",
        "Factorizá los siguientes polinomios usando `ax² + bx + c = a(x − x₁)(x − x₂)`:\n\n"
        "a) `2x² − 10x − 28`\n\nc) `3x² + 4x + 1`\n\nd) `−12x + x² − 108`",
        [
            _c("a) ¿Cuál es la factorización de `2x² − 10x − 28`?",
               ["2(x − 7)(x + 2)", "2(x + 7)(x − 2)", "(x − 7)(x + 2)", "2(x − 7)(x − 2)"], "2(x − 7)(x + 2)"),
            _c("c) ¿Cuál es la factorización de `3x² + 4x + 1`?",
               ["3(x + 1)(x + ⅓)", "3(x − 1)(x − ⅓)", "(x + 1)(x + ⅓)", "3(x + 1)(x − ⅓)"], "3(x + 1)(x + ⅓)"),
            _c("d) ¿Cuál es la factorización de `−12x + x² − 108`?",
               ["(x − 18)(x + 6)", "(x + 18)(x − 6)", "(x − 12)(x + 9)", "(x − 18)(x − 6)"], "(x − 18)(x + 6)"),
        ],
        [
            "Hallá las raíces con la fórmula resolvente (o Bhaskara) y no te olvides del coeficiente principal `a` delante.",
        ],
        [
            "a) `a = 2`. Raíces de `2x² − 10x − 28 = 0` (o de `x² − 5x − 14 = 0`): `x = (5 ± √(25 + 56))/2 = (5 ± 9)/2` → `x₁ = 7`, `x₂ = −2`.",
            "Factorización: `2(x − 7)(x + 2)`.",
            "c) `x = (−4 ± √(16 − 12))/6 = (−4 ± 2)/6` → `x₁ = −⅓`, `x₂ = −1`. Factorización: `3(x + 1)(x + ⅓)`, que también se escribe `(x + 1)(3x + 1)`.",
            "d) Ordenado: `x² − 12x − 108`. `x = (12 ± √(144 + 432))/2 = (12 ± 24)/2` → `x₁ = 18`, `x₂ = −6`.",
            "Factorización: `(x − 18)(x + 6)`. Error típico: olvidar el `2` o el `3` delante, que cambia el polinomio.",
        ],
    ),
    # ---------- Ej. 28: circunferencia ----------
    _p(
        "tp4-28", CIRC, 2, "Matemática · TP4, ej. 28 a, b, c",
        "Circunferencia: completar cuadrados",
        "Dadas las ecuaciones generales de la circunferencia, completá cuadrados en `x` y en `y` para encontrar la ecuación canónica `(x − h)² + (y − k)² = r²` y determiná centro y radio:\n\n"
        "a) `x² + y² + 2x − 4y − 4 = 0`\n\nb) `2x² + 2y² − 36x − 12y − 20 = 0`\n\nc) `x² + y² − 20x + 16y + 128 = 0`",
        [
            _n("a) ¿Cuánto mide el radio?", 3, "3"),
            _c("b) ¿Cuáles son el centro y el radio?",
               ["C(9; 3) y r = 10", "C(−9; −3) y r = 10", "C(18; 6) y r = 10", "C(9; 3) y r = √10"], "C(9; 3) y r = 10"),
            _n("c) ¿Cuánto mide el radio?", 6, "6"),
        ],
        [
            "Si `x²` e `y²` tienen coeficiente distinto de 1 (como en b), dividí toda la ecuación por ese número.",
            "`x² + px = (x + p/2)² − (p/2)²`: lo que sumás para completar el cuadrado lo tenés que restar (o pasar al otro miembro).",
        ],
        [
            "a) `(x² + 2x + 1) + (y² − 4y + 4) = 4 + 1 + 4` → `(x + 1)² + (y − 2)² = 9`. Centro `(−1; 2)`, radio `3`.",
            "b) Dividimos por 2: `x² + y² − 18x − 6y − 10 = 0`.",
            "`(x² − 18x + 81) + (y² − 6y + 9) = 10 + 81 + 9` → `(x − 9)² + (y − 3)² = 100`. Centro `(9; 3)`, radio `10`.",
            "c) `(x² − 20x + 100) + (y² + 16y + 64) = −128 + 100 + 64` → `(x − 10)² + (y + 8)² = 36`. Centro `(10; −8)`, radio `6`.",
            "Ojo con los signos del centro: `(x + 1)²` corresponde a `h = −1`.",
        ],
    ),
    # ---------- Ej. 35: operaciones con expresiones fraccionarias ----------
    _p(
        "tp4-35-producto", RAC, 2, "Matemática · TP4, ej. 35 c, d, e",
        "Producto y cociente de expresiones fraccionarias",
        "Resolvé y simplificá las siguientes expresiones algebraicas. Indicá las condiciones de validez de cada ejercicio.\n\n"
        "c) `(x² + 2x − 3)/(x² + 8x + 16) · (3x + 12)/(x − 1)`\n\n"
        "d) `(x² + 2x)/(x² − 5x + 6) : (x² + 4x + 4)/(x² − 4)`\n\n"
        "e) `[x/(x − 1) + x²/(x² − 1)] : (x² + ½x)/(x + 1)`",
        [
            _c("c) ¿Cuál es el resultado con sus condiciones?",
               ["3(x + 3)/(x + 4), con x ≠ −4 y x ≠ 1", "3(x + 3)/(x + 4), con x ≠ −4",
                "3(x − 3)/(x + 4), con x ≠ −4 y x ≠ 1", "(x + 3)/(3(x + 4)), con x ≠ −4 y x ≠ 1"],
               "3(x + 3)/(x + 4), con x ≠ −4 y x ≠ 1"),
            _c("d) ¿Cuál es el resultado con sus condiciones?",
               ["x/(x − 3), con x ≠ −2, x ≠ 2 y x ≠ 3", "x/(x − 3), con x ≠ 2 y x ≠ 3",
                "x/(x + 3), con x ≠ −2, x ≠ 2 y x ≠ 3", "(x + 2)/(x − 3), con x ≠ −2, x ≠ 2 y x ≠ 3"],
               "x/(x − 3), con x ≠ −2, x ≠ 2 y x ≠ 3"),
            _c("e) ¿Cuál es el resultado con sus condiciones?",
               ["2/(x − 1), con x ≠ −1, x ≠ −½, x ≠ 0 y x ≠ 1", "2/(x − 1), con x ≠ −1 y x ≠ 1",
                "2x/(x − 1), con x ≠ −1, x ≠ −½, x ≠ 0 y x ≠ 1", "(x − 1)/2, con x ≠ −1, x ≠ −½, x ≠ 0 y x ≠ 1"],
               "2/(x − 1), con x ≠ −1, x ≠ −½, x ≠ 0 y x ≠ 1"),
        ],
        [
            "Factorizá todos los numeradores y denominadores antes de operar.",
            "Las condiciones salen de todos los denominadores y, en una división, también del numerador del divisor (no se puede dividir por cero).",
        ],
        [
            "c) `x² + 2x − 3 = (x + 3)(x − 1)`, `x² + 8x + 16 = (x + 4)²`, `3x + 12 = 3(x + 4)`. Producto: `(x + 3)(x − 1)·3(x + 4)/((x + 4)²(x − 1)) = 3(x + 3)/(x + 4)`, con `x ≠ −4`, `x ≠ 1`.",
            "d) `x² + 2x = x(x + 2)`, `x² − 5x + 6 = (x − 2)(x − 3)`, `x² + 4x + 4 = (x + 2)²`, `x² − 4 = (x − 2)(x + 2)`.",
            "Dividir es multiplicar por el inverso: `x(x + 2)/((x − 2)(x − 3)) · (x − 2)(x + 2)/(x + 2)² = x/(x − 3)`.",
            "Condiciones de d): denominadores (`x ≠ 2`, `x ≠ 3`, `x ≠ −2`) y divisor distinto de cero (`x ≠ −2`): `x ≠ −2, 2, 3`.",
            "e) Corchete: `x(x + 1)/(x² − 1) + x²/(x² − 1) = (2x² + x)/(x² − 1) = x(2x + 1)/((x − 1)(x + 1))`.",
            "Divisor: `x² + ½x = x(2x + 1)/2`, así que vale `x(2x + 1)/(2(x + 1))`. Cociente: `x(2x + 1)/((x − 1)(x + 1)) · 2(x + 1)/(x(2x + 1)) = 2/(x − 1)`.",
            "Condiciones de e): `x ≠ ±1` (denominadores) y el divisor no puede ser 0: `x ≠ 0`, `x ≠ −½`.",
        ],
    ),
    _p(
        "tp4-35-suma", RAC, 3, "Matemática · TP4, ej. 35 a, b, f",
        "Suma y resta de expresiones fraccionarias",
        "Resolvé y simplificá las siguientes expresiones algebraicas. Indicá las condiciones de validez de cada ejercicio.\n\n"
        "a) `1/(x + 1) + 2x/(x² − 1)`\n\n"
        "b) `4/(x² − 25) − (x + 3)/(x² − 2x − 15)`\n\n"
        "f) `(x² + x + 1)/(2x² + x) − (x² + 2)/(2x² − x − 1) + (2x − 1)/(x² − x)`",
        [
            _c("a) ¿Cuál es el resultado con sus condiciones?",
               ["(3x − 1)/(x² − 1), con x ≠ −1 y x ≠ 1", "(3x + 1)/(x² − 1), con x ≠ −1 y x ≠ 1",
                "(2x + 1)/(x² − 1), con x ≠ −1 y x ≠ 1", "(3x − 1)/(x + 1), con x ≠ −1"],
               "(3x − 1)/(x² − 1), con x ≠ −1 y x ≠ 1"),
            _c("b) ¿Cuál es el resultado con sus condiciones?",
               ["−(x + 1)/(x² − 25), con x ≠ −5, x ≠ −3 y x ≠ 5", "−(x + 1)/(x² − 25), con x ≠ −5 y x ≠ 5",
                "(9 − x)/(x² − 25), con x ≠ −5, x ≠ −3 y x ≠ 5", "(x + 1)/(x² − 25), con x ≠ −5, x ≠ −3 y x ≠ 5"],
               "−(x + 1)/(x² − 25), con x ≠ −5, x ≠ −3 y x ≠ 5"),
            _c("f) ¿Cuál es el resultado con sus condiciones?",
               ["2/x, con x ≠ −½, x ≠ 0 y x ≠ 1", "2/x, con x ≠ 0", "1/x, con x ≠ −½, x ≠ 0 y x ≠ 1",
                "2/(x − 1), con x ≠ −½, x ≠ 0 y x ≠ 1"],
               "2/x, con x ≠ −½, x ≠ 0 y x ≠ 1"),
        ],
        [
            "Factorizá los denominadores y buscá el m.c.m.: `x² − 1`, `x² − 25`, `x² − 2x − 15 = (x − 5)(x + 3)`, `2x² − x − 1 = (2x + 1)(x − 1)`.",
            "Las condiciones de validez salen de los denominadores ORIGINALES, aunque después se simplifique algún factor.",
        ],
        [
            "a) `x² − 1 = (x + 1)(x − 1)`. `1/(x + 1) = (x − 1)/(x² − 1)`, entonces la suma es `(x − 1 + 2x)/(x² − 1) = (3x − 1)/(x² − 1)`, con `x ≠ ±1`.",
            "b) `(x + 3)/((x − 5)(x + 3)) = 1/(x − 5)` si `x ≠ −3`. Común denominador `(x − 5)(x + 5)`: `[4 − (x + 5)]/(x² − 25) = (−x − 1)/(x² − 25)`.",
            "Condiciones de b): `x ≠ 5`, `x ≠ −5` y también `x ≠ −3` (anulaba el denominador original). Error típico: `4 − x + 5`, olvidando que el menos afecta a todo el `(x + 5)`.",
            "f) Denominadores: `2x² + x = x(2x + 1)`, `2x² − x − 1 = (2x + 1)(x − 1)`, `x² − x = x(x − 1)`. m.c.m.: `x(2x + 1)(x − 1)`.",
            "Numerador: `(x² + x + 1)(x − 1) − (x² + 2)x + (2x − 1)(2x + 1) = (x³ − 1) − x³ − 2x + 4x² − 1 = 4x² − 2x − 2`.",
            "`4x² − 2x − 2 = 2(2x² − x − 1) = 2(2x + 1)(x − 1)`. Simplificando: `2(2x + 1)(x − 1)/(x(2x + 1)(x − 1)) = 2/x`, con `x ≠ 0`, `x ≠ −½`, `x ≠ 1`.",
        ],
    ),
    # ---------- Ej. 37 y 38: ecuaciones fraccionarias ----------
    _p(
        "tp4-37-a", ECU, 1, "Matemática · TP4, ej. 37 a, b, c",
        "Ecuaciones fraccionarias",
        "Resolvé las siguientes ecuaciones fraccionarias e indicá las condiciones de validez de cada una:\n\n"
        "a) `(x + 5)/(x − 3) = 3`\n\nb) `(x + 2)/(x − 4) = (x − 1)/(x + 1)`\n\nc) `2/(x + 4) = 3/(x − 5)`",
        [
            _n("a) ¿Cuál es la solución?", 7, "7 (con x ≠ 3)"),
            _n("b) ¿Cuál es la solución? Podés responder con fracción.", 0.25, "1/4 (con x ≠ 4 y x ≠ −1)"),
            _n("c) ¿Cuál es la solución?", -22, "−22 (con x ≠ −4 y x ≠ 5)"),
        ],
        [
            "Primero anotá los valores que anulan denominadores; después multiplicá en cruz.",
            "Al final verificá que la solución no sea uno de los valores excluidos.",
        ],
        [
            "a) Condición `x ≠ 3`. `x + 5 = 3(x − 3) = 3x − 9` → `14 = 2x` → `x = 7` ✓.",
            "b) Condiciones `x ≠ 4`, `x ≠ −1`. En cruz: `(x + 2)(x + 1) = (x − 1)(x − 4)`.",
            "`x² + 3x + 2 = x² − 5x + 4` → `8x = 2` → `x = ¼` ✓ (no está excluido).",
            "c) Condiciones `x ≠ −4`, `x ≠ 5`. `2(x − 5) = 3(x + 4)` → `2x − 10 = 3x + 12` → `x = −22` ✓.",
            "Verificación de c): `2/(−18) = −1/9` y `3/(−27) = −1/9` ✓.",
        ],
    ),
    _p(
        "tp4-37-b", ECU, 3, "Matemática · TP4, ej. 37 d, e y ej. 38",
        "Ecuaciones fraccionarias y un parámetro",
        "d) Resolvé `1/(x + 5) − 1/(x + 8) = 1/(x + 3) − 1/(x + 6)`.\n\n"
        "e) Resolvé `(x − 5)/(x + 3) + (x + 2)/(x − 2) = (2x² − 3x − 14)/(x² + x − 6)`.\n\n"
        "Ej. 38) Hallá los valores de `m` para que la ecuación `(2m + x)/(x − 3) − (x + m)/(x + 3) = 6/(x² − 9)` tenga solución `x = 1`.",
        [
            _n("d) ¿Cuál es la solución? Podés responder con fracción o decimal.", -5.5, "−11/2 (= −5,5)"),
            _n("e) ¿Cuál es la solución?", -30, "−30 (con x ≠ −3 y x ≠ 2)"),
            _n("Ej. 38) ¿Qué valor debe tener `m`?", 0, "0"),
        ],
        [
            "d) Restá cada miembro por separado: en ambos el numerador queda 3.",
            "e) `x² + x − 6 = (x + 3)(x − 2)` es el común denominador.",
            "Ej. 38) Reemplazá `x = 1` y resolvé la ecuación de primer grado en `m`.",
        ],
        [
            "d) Izquierda: `[(x + 8) − (x + 5)]/((x + 5)(x + 8)) = 3/((x + 5)(x + 8))`. Derecha: `3/((x + 3)(x + 6))`.",
            "Igualando denominadores: `x² + 13x + 40 = x² + 9x + 18` → `4x = −22` → `x = −11/2`, que no anula ningún denominador ✓.",
            "e) Condiciones `x ≠ −3`, `x ≠ 2`. Multiplicando por `(x + 3)(x − 2)`: `(x − 5)(x − 2) + (x + 2)(x + 3) = 2x² − 3x − 14`.",
            "`x² − 7x + 10 + x² + 5x + 6 = 2x² − 2x + 16`, entonces `−2x + 16 = −3x − 14` → `x = −30` ✓.",
            "Ej. 38) Con `x = 1`: `(2m + 1)/(−2) − (1 + m)/4 = 6/(−8)`. Multiplicando por 4: `−2(2m + 1) − (1 + m) = −3` → `−5m − 3 = −3` → `m = 0`.",
            "Verificación con `m = 0`: `x/(x − 3) − x/(x + 3) = 6x/(x² − 9)`, que vale `6/(x² − 9)` justo cuando `x = 1` ✓.",
        ],
    ),
    # ---------- Ej. 39 y 40: inecuaciones ----------
    _p(
        "tp4-39-a", INEC, 2, "Matemática · TP4, ej. 39 a, e, h",
        "Inecuaciones polinómicas",
        "Resolvé las siguientes desigualdades:\n\na) `x³ − 4x > 0`\n\ne) `x² + 2x < 3`\n\nh) `x⁴ ≤ x²`",
        [
            _c("a) ¿Cuál es el conjunto solución?", ["(−2; 0) ∪ (2; +∞)", "(−∞; −2) ∪ (0; 2)", "(2; +∞)", "(−2; 2)"], "(−2; 0) ∪ (2; +∞)"),
            _c("e) ¿Cuál es el conjunto solución?", ["(−3; 1)", "(−∞; −3) ∪ (1; +∞)", "(−1; 3)", "(−∞; 1)"], "(−3; 1)"),
            _c("h) ¿Cuál es el conjunto solución?", ["[−1; 1]", "[−1; 0) ∪ (0; 1]", "(−∞; −1] ∪ [1; +∞)", "[0; 1]"], "[−1; 1]"),
        ],
        [
            "Pasá todo a un miembro, factorizá y armá la tabla de signos con las raíces.",
            "No dividas por `x` ni por `x²`: podés perder soluciones o invertir mal el signo.",
        ],
        [
            "a) `x³ − 4x = x(x − 2)(x + 2)`. Raíces `−2, 0, 2`. Signos: `(−∞; −2)` negativo, `(−2; 0)` positivo, `(0; 2)` negativo, `(2; +∞)` positivo.",
            "Solución de a): `(−2; 0) ∪ (2; +∞)` (abiertos porque la desigualdad es estricta).",
            "e) `x² + 2x − 3 < 0` → `(x + 3)(x − 1) < 0`: la parábola es negativa entre las raíces. Solución: `(−3; 1)`.",
            "h) `x⁴ − x² ≤ 0` → `x²(x − 1)(x + 1) ≤ 0`. Como `x² ≥ 0`, el signo lo da `(x − 1)(x + 1)`, que es `≤ 0` en `[−1; 1]`; además `x = 0` cumple (`0 ≤ 0`).",
            "Solución de h): `[−1; 1]`. Error típico: dividir por `x²` y perder `x = 0`.",
        ],
    ),
    _p(
        "tp4-39-b", INEC, 2, "Matemática · TP4, ej. 39 d, f, i",
        "Inecuaciones polinómicas con tabla de signos",
        "Resolvé las siguientes desigualdades:\n\nd) `5x² + 3x ≥ 3x² + 2`\n\nf) `(2x − 1)(3x + 6)(x − 2) > 0`\n\ni) `x⁵ > 4x³`",
        [
            _c("d) ¿Cuál es el conjunto solución?", ["(−∞; −2] ∪ [½; +∞)", "[−2; ½]", "(−∞; −½] ∪ [2; +∞)", "[½; +∞)"], "(−∞; −2] ∪ [½; +∞)"),
            _c("f) ¿Cuál es el conjunto solución?", ["(−2; ½) ∪ (2; +∞)", "(−∞; −2) ∪ (½; 2)", "(2; +∞)", "(−2; 2)"], "(−2; ½) ∪ (2; +∞)"),
            _c("i) ¿Cuál es el conjunto solución?", ["(−2; 0) ∪ (2; +∞)", "(−∞; −2) ∪ (2; +∞)", "(2; +∞)", "(−∞; −2) ∪ (0; 2)"], "(−2; 0) ∪ (2; +∞)"),
        ],
        [
            "d) Pasá todo a la izquierda: queda una cuadrática.",
            "Ubicá las raíces en la recta y probá un valor en cada intervalo.",
        ],
        [
            "d) `2x² + 3x − 2 ≥ 0` → raíces `x = (−3 ± 5)/4`: `½` y `−2`. `(2x − 1)(x + 2) ≥ 0` fuera de las raíces (parábola con `a > 0`).",
            "Solución de d): `(−∞; −2] ∪ [½; +∞)` (cerrados por el `≥`).",
            "f) Raíces `−2, ½, 2`. Con `x = 3`: `5·15·1 > 0`; los signos alternan: `+` en `(2; +∞)`, `−` en `(½; 2)`, `+` en `(−2; ½)`, `−` en `(−∞; −2)`.",
            "Solución de f): `(−2; ½) ∪ (2; +∞)`.",
            "i) `x⁵ − 4x³ > 0` → `x³(x − 2)(x + 2) > 0`. Raíces `−2, 0, 2` (todas de multiplicidad impar, el signo cambia en cada una).",
            "Con `x = 3`: positivo; alternando: `(0; 2)` negativo, `(−2; 0)` positivo, `(−∞; −2)` negativo. Solución: `(−2; 0) ∪ (2; +∞)`. Error típico: dividir por `x³` como si fuera positivo.",
        ],
    ),
    _p(
        "tp4-40", INEC, 3, "Matemática · TP4, ej. 40 a, c, e",
        "Inecuaciones fraccionarias",
        "Resolvé las siguientes desigualdades:\n\na) `(x − 3)/(x + 1) ≥ 0`\n\nc) `(x² − 1)/(x² − 4) < 0`\n\ne) `(2x + 3)/((x + 1)(x + 2)) ≤ 0`",
        [
            _c("a) ¿Cuál es el conjunto solución?", ["(−∞; −1) ∪ [3; +∞)", "(−∞; −1] ∪ [3; +∞)", "(−1; 3]", "[3; +∞)"], "(−∞; −1) ∪ [3; +∞)"),
            _c("c) ¿Cuál es el conjunto solución?", ["(−2; −1) ∪ (1; 2)", "(−1; 1)", "(−∞; −2) ∪ (2; +∞)", "(−2; 2)"], "(−2; −1) ∪ (1; 2)"),
            _c("e) ¿Cuál es el conjunto solución?", ["(−∞; −2) ∪ [−3/2; −1)", "(−2; −3/2] ∪ (−1; +∞)", "(−∞; −2] ∪ [−3/2; −1]", "[−3/2; +∞)"], "(−∞; −2) ∪ [−3/2; −1)"),
        ],
        [
            "Marcá en la recta las raíces del numerador y del denominador y armá la tabla de signos.",
            "Las raíces del denominador SIEMPRE quedan afuera (intervalo abierto), aunque la desigualdad tenga `=`.",
        ],
        [
            "a) Puntos críticos `−1` (denominador) y `3` (numerador). Signo positivo en `(−∞; −1)` y en `(3; +∞)`; vale 0 en `x = 3`.",
            "Solución de a): `(−∞; −1) ∪ [3; +∞)`; `x = −1` se excluye porque anula el denominador.",
            "c) `(x − 1)(x + 1)/((x − 2)(x + 2)) < 0`. Críticos `−2, −1, 1, 2`. Con `x = 0`: `(−1)/(−4) > 0`; con `x = 1,5`: `1,25/(−1,75) < 0`; con `x = −1,5`: también negativo; afuera de `[−2; 2]` es positivo.",
            "Solución de c): `(−2; −1) ∪ (1; 2)`.",
            "e) Críticos `−2`, `−3/2` y `−1`. Con `x = −3`: `(−3)/((−2)(−1)) < 0` ✓; en `(−2; −3/2)`, con `x = −1,8`: `(−0,6)/((−0,8)(0,2)) > 0`; en `(−3/2; −1)`, con `x = −1,2`: `(0,6)/((−0,2)(0,8)) < 0` ✓; para `x > −1` es positivo.",
            "Solución de e): `(−∞; −2) ∪ [−3/2; −1)`: se incluye `−3/2` (anula el numerador) y se excluyen `−2` y `−1`.",
        ],
    ),
]

# ======================================================================
# TP5 · FUNCIONES
# ======================================================================
FORMAS = "al-cuadratica-formas"
PARAB = "al-parabolas-formula"
ESTUDIO = "a2-estudio-funciones"
DOM = "al-dominio-rango"
FUN = "p-funciones"

TP5 = [
    # ---------- Ej. 8: las tres formas de la cuadrática ----------
    _p(
        "tp5-8-fila1", FORMAS, 2, "Matemática · TP5, ej. 8 (fila 1)",
        "De la forma polinómica a las otras",
        "El ej. 8 pide completar un cuadro con expresión polinómica, vértice, eje de simetría, expresión canónica, ceros y expresión factorizada de una cuadrática.\n\n"
        "Primera fila: `f(x) = 3x² + 6x − 9`.",
        [
            _c("a) ¿Cuál es el vértice?", ["V(−1; −12)", "V(1; 0)", "V(−1; −4)", "V(−3; 0)"], "V(−1; −12)"),
            _c("b) ¿Cuál es la expresión canónica?", ["f(x) = 3(x + 1)² − 12", "f(x) = 3(x − 1)² − 12", "f(x) = (x + 1)² − 4", "f(x) = 3(x + 1)² − 4"], "f(x) = 3(x + 1)² − 12"),
            _c("c) ¿Cuál es la expresión factorizada?", ["f(x) = 3(x + 3)(x − 1)", "f(x) = (x + 3)(x − 1)", "f(x) = 3(x − 3)(x + 1)", "f(x) = 3(x + 3)(x + 1)"], "f(x) = 3(x + 3)(x − 1)"),
        ],
        [
            "Abscisa del vértice: `xᵥ = −b/(2a)`; la ordenada es `f(xᵥ)`.",
            "Canónica: `a(x − xᵥ)² + yᵥ`. Factorizada: `a(x − x₁)(x − x₂)`, siempre con la misma `a`.",
        ],
        [
            "`a = 3`, `b = 6`, `c = −9`. `xᵥ = −6/(2·3) = −1`; `yᵥ = f(−1) = 3 − 6 − 9 = −12`. Vértice `V(−1; −12)`, eje de simetría `x = −1`.",
            "Canónica: `f(x) = 3(x + 1)² − 12`. Control: `3(x² + 2x + 1) − 12 = 3x² + 6x − 9` ✓.",
            "Ceros: `3(x + 1)² = 12` → `(x + 1)² = 4` → `x + 1 = ±2` → `x₁ = 1`, `x₂ = −3`.",
            "Factorizada: `f(x) = 3(x − 1)(x + 3)`.",
            "Error típico: olvidar la `a = 3` en la canónica o en la factorizada; `(x + 1)² − 4` tiene los mismos ceros pero es otra función.",
        ],
    ),
    _p(
        "tp5-8-fila2", PARAB, 2, "Matemática · TP5, ej. 8 (fila 2)",
        "Del vértice a la forma polinómica",
        "Ej. 8, segunda fila: solo se conoce el vértice `V(½; −9/4)`. Como no se conoce `a`, el material indica tomar `a = 1`. "
        "Hallá la expresión polinómica `f(x) = x² + bx + c`, los ceros y la expresión factorizada.",
        [
            _n("a) ¿Cuánto vale `b`?", -1, "−1"),
            _n("b) ¿Cuánto vale `c`?", -2, "−2"),
            _c("c) ¿Cuál es la expresión factorizada?", ["f(x) = (x − 2)(x + 1)", "f(x) = (x + 2)(x − 1)", "f(x) = (x − ½)(x + 9/4)", "f(x) = (x − 2)(x − 1)"], "f(x) = (x − 2)(x + 1)"),
        ],
        [
            "Empezá por la canónica: `f(x) = (x − ½)² − 9/4`, y desarrollá el cuadrado.",
        ],
        [
            "Canónica con `a = 1`: `f(x) = (x − ½)² − 9/4`. Eje de simetría `x = ½`.",
            "Desarrollando: `x² − x + ¼ − 9/4 = x² − x − 2`. Entonces `b = −1` y `c = −2`.",
            "Ceros: `(x − ½)² = 9/4` → `x − ½ = ±3/2` → `x₁ = 2`, `x₂ = −1`.",
            "Factorizada: `f(x) = (x − 2)(x + 1)`. Control: `x² + x − 2x − 2 = x² − x − 2` ✓.",
        ],
    ),
    _p(
        "tp5-8-filas3a5", FORMAS, 2, "Matemática · TP5, ej. 8 (filas 3, 4 y 5)",
        "Completar el cuadro de la cuadrática",
        "Ej. 8, filas 3 a 5 (si no se conoce `a`, tomá `a = 1`):\n\n"
        "Fila 3: se conoce la expresión factorizada `f(x) = (x − 1)(x − 3)`.\n\n"
        "Fila 4: se sabe que los ceros son `x₁ = x₂ = 3`.\n\n"
        "Fila 5: se conoce la expresión canónica `f(x) = (x − 2)² + 1`.",
        [
            _c("a) Fila 3: ¿cuál es el vértice?", ["V(2; −1)", "V(2; 1)", "V(−2; −1)", "V(1; 3)"], "V(2; −1)"),
            _c("b) Fila 4: ¿cuál es la expresión polinómica?", ["f(x) = x² − 6x + 9", "f(x) = x² + 6x + 9", "f(x) = x² − 9", "f(x) = x² − 3x + 9"], "f(x) = x² − 6x + 9"),
            _c("c) Fila 5: ¿cuáles son los ceros?", ["No tiene ceros reales", "x₁ = 1 y x₂ = 3", "x₁ = x₂ = 2", "x₁ = −1 y x₂ = 5"], "No tiene ceros reales"),
        ],
        [
            "El vértice está en el punto medio de los ceros.",
            "Si `x₁ = x₂ = 3`, la factorizada es `(x − 3)²`.",
            "En la canónica `(x − 2)² + 1`, el vértice es el punto más bajo: ¿puede valer 0?",
        ],
        [
            "Fila 3: ceros 1 y 3, `xᵥ = (1 + 3)/2 = 2`, `yᵥ = (2 − 1)(2 − 3) = −1`. Vértice `V(2; −1)`, eje `x = 2`; canónica `(x − 2)² − 1`; polinómica `x² − 4x + 3`.",
            "Fila 4: factorizada `(x − 3)²`, polinómica `x² − 6x + 9`, vértice `V(3; 0)`, eje `x = 3`, canónica `(x − 3)² + 0`.",
            "Fila 5: polinómica `x² − 4x + 5`, vértice `V(2; 1)`, eje `x = 2`.",
            "Como `(x − 2)² ≥ 0`, `f(x) ≥ 1` para todo x: nunca vale 0. También `Δ = 16 − 20 < 0`. No tiene ceros reales y no se puede factorizar en IR.",
        ],
    ),
    # ---------- Ej. 21: ceros y ordenada al origen ----------
    _p(
        "tp5-21-a", ESTUDIO, 1, "Matemática · TP5, ej. 21 c, e, f",
        "Ceros y ordenada al origen (polinómicas)",
        "Hallá los ceros y la ordenada al origen de las siguientes funciones:\n\n"
        "c) `f(x) = x² − 5x + 6`\n\ne) `f(x) = x² + 2x + 4`\n\nf) `f(x) = (x² − 1)(2x − 5)`",
        [
            _c("c) ¿Cuáles son los ceros y la ordenada al origen?",
               ["Ceros: 2 y 3; ordenada: 6", "Ceros: −2 y −3; ordenada: 6", "Ceros: 2 y 3; ordenada: −6", "Ceros: 1 y 6; ordenada: 6"],
               "Ceros: 2 y 3; ordenada: 6"),
            _c("e) ¿Cuáles son los ceros y la ordenada al origen?",
               ["No tiene ceros reales; ordenada: 4", "Ceros: −2 y 2; ordenada: 4", "Cero: −1; ordenada: 4", "No tiene ceros reales; ordenada: 3"],
               "No tiene ceros reales; ordenada: 4"),
            _c("f) ¿Cuáles son los ceros y la ordenada al origen?",
               ["Ceros: −1, 1 y 5/2; ordenada: 5", "Ceros: 1 y 5/2; ordenada: −5", "Ceros: −1, 1 y 5/2; ordenada: −5", "Ceros: −1, 1 y −5/2; ordenada: 5"],
               "Ceros: −1, 1 y 5/2; ordenada: 5"),
        ],
        [
            "Ceros: resolvé `f(x) = 0`. Ordenada al origen: calculá `f(0)`.",
            "Para un producto igualado a cero, cada factor da ceros por separado.",
        ],
        [
            "c) `x² − 5x + 6 = (x − 2)(x − 3)`: ceros `2` y `3`. `f(0) = 6`.",
            "e) `Δ = 2² − 4·1·4 = −12 < 0`: no tiene ceros reales. `f(0) = 4`.",
            "f) `x² − 1 = 0` → `x = ±1`; `2x − 5 = 0` → `x = 5/2`. Ceros: `−1`, `1` y `5/2`.",
            "`f(0) = (0 − 1)(0 − 5) = (−1)(−5) = 5`.",
        ],
    ),
    _p(
        "tp5-21-b", ESTUDIO, 2, "Matemática · TP5, ej. 21 j, l, p",
        "Ceros y ordenada al origen (irracionales y racionales)",
        "Hallá los ceros y la ordenada al origen de las siguientes funciones:\n\n"
        "j) `f(x) = 2 − √(4 − x²)`\n\nl) `f(x) = 2 − ∛(x² − 1)`\n\np) `f(x) = (x² − 4)/(x + 1)`",
        [
            _c("j) ¿Cuáles son los ceros y la ordenada al origen?",
               ["Cero: 0; ordenada: 0", "Ceros: −2 y 2; ordenada: 0", "Ceros: −2 y 2; ordenada: 2", "No tiene ceros; ordenada: 0"],
               "Cero: 0; ordenada: 0"),
            _c("l) ¿Cuáles son los ceros y la ordenada al origen?",
               ["Ceros: −3 y 3; ordenada: 3", "Ceros: −3 y 3; ordenada: 1", "Ceros: −√5 y √5; ordenada: 3", "Cero: 3; ordenada: 3"],
               "Ceros: −3 y 3; ordenada: 3"),
            _c("p) ¿Cuáles son los ceros y la ordenada al origen?",
               ["Ceros: −2 y 2; ordenada: −4", "Ceros: −2, 2 y −1; ordenada: −4", "Ceros: −2 y 2; ordenada: 4", "Cero: −1; ordenada: −4"],
               "Ceros: −2 y 2; ordenada: −4"),
        ],
        [
            "j) y l): aislá la raíz y elevá a la potencia que corresponda (al cuadrado o al cubo).",
            "En una fracción, los ceros son los ceros del numerador que estén en el dominio.",
        ],
        [
            "j) `2 − √(4 − x²) = 0` → `√(4 − x²) = 2` → `4 − x² = 4` → `x = 0`. Ordenada: `f(0) = 2 − √4 = 0` (el origen es cero y ordenada a la vez).",
            "l) `∛(x² − 1) = 2` → `x² − 1 = 8` → `x² = 9` → `x = ±3`.",
            "Ordenada de l): `f(0) = 2 − ∛(−1) = 2 − (−1) = 3`. La raíz cúbica de un negativo existe.",
            "p) Numerador `x² − 4 = 0` → `x = ±2`, y ninguno anula el denominador. `x = −1` no es cero: está fuera del dominio.",
            "Ordenada de p): `f(0) = (−4)/1 = −4`.",
        ],
    ),
    # ---------- Ej. 22 y 23: dominios ----------
    _p(
        "tp5-22", DOM, 1, "Matemática · TP5, ej. 22 c, f, i",
        "Dominio de funciones fraccionarias",
        "Hallá el dominio de las siguientes funciones fraccionarias:\n\n"
        "c) `f(x) = (x³ + 1)/(5x² − 2x)`\n\nf) `f(x) = (x + 1)/((3x + 1)(3x − 2))`\n\ni) `f(x) = (x³ + 1)/(x⁴ − x²)`",
        [
            _c("c) ¿Cuál es el dominio?", ["D = IR − {0; 2/5}", "D = IR − {0; 5/2}", "D = IR − {2/5}", "D = IR − {0; −2/5}"], "D = IR − {0; 2/5}"),
            _c("f) ¿Cuál es el dominio?", ["D = IR − {−1/3; 2/3}", "D = IR − {1/3; −2/3}", "D = IR − {−1; −1/3; 2/3}", "D = IR − {−3; 3/2}"], "D = IR − {−1/3; 2/3}"),
            _c("i) ¿Cuál es el dominio?", ["D = IR − {−1; 0; 1}", "D = IR − {0; 1}", "D = IR − {−1; 1}", "D = IR − {0}"], "D = IR − {−1; 0; 1}"),
        ],
        [
            "El dominio de una fracción son todos los reales menos los que anulan el denominador.",
            "Factorizá el denominador; el numerador no influye (aunque se pueda simplificar).",
        ],
        [
            "c) `5x² − 2x = x(5x − 2) = 0` → `x = 0` o `x = 2/5`. `D = IR − {0; 2/5}`.",
            "f) `3x + 1 = 0` → `x = −1/3`; `3x − 2 = 0` → `x = 2/3`. `D = IR − {−1/3; 2/3}`. El `x = −1` anula el numerador, no el denominador.",
            "i) `x⁴ − x² = x²(x − 1)(x + 1) = 0` → `x = 0, 1, −1`. `D = IR − {−1; 0; 1}`.",
            "Ojo en i): `x³ + 1 = (x + 1)(x² − x + 1)` permite simplificar `(x + 1)`, pero `x = −1` igual queda fuera del dominio de la función dada.",
        ],
    ),
    _p(
        "tp5-23", ESTUDIO, 3, "Matemática · TP5, ej. 23 g, h, i",
        "Dominio de funciones irracionales",
        "Hallá el dominio de las siguientes funciones irracionales:\n\n"
        "g) `f(x) = √((3 − x)/(x + 2))`\n\nh) `f(x) = √((5 + x)/(x(x − 3)))`\n\ni) `f(x) = ⁶√((x + 1)/(x(x − 4)))` (raíz sexta)",
        [
            _c("g) ¿Cuál es el dominio?", ["(−2; 3]", "[−2; 3]", "(−∞; −2) ∪ [3; +∞)", "(−2; 3)"], "(−2; 3]"),
            _c("h) ¿Cuál es el dominio?", ["[−5; 0) ∪ (3; +∞)", "[−5; 0] ∪ [3; +∞)", "(−∞; −5] ∪ (0; 3)", "(−5; 0) ∪ (3; +∞)"], "[−5; 0) ∪ (3; +∞)"),
            _c("i) ¿Cuál es el dominio?", ["[−1; 0) ∪ (4; +∞)", "(−∞; −1] ∪ (0; 4)", "[−1; 0] ∪ [4; +∞)", "IR − {0; 4}"], "[−1; 0) ∪ (4; +∞)"),
        ],
        [
            "Una raíz de índice par exige radicando `≥ 0`; además, el denominador no puede ser 0.",
            "Resolvé cada inecuación fraccionaria con una tabla de signos.",
        ],
        [
            "g) `(3 − x)/(x + 2) ≥ 0`. Críticos `−2` (denominador) y `3` (numerador). Con `x = 0`: `3/2 > 0` ✓; para `x < −2` o `x > 3`, negativo.",
            "Dominio de g): `(−2; 3]` (se incluye 3 porque da radicando 0; `−2` no).",
            "h) `(5 + x)/(x(x − 3)) ≥ 0`. Críticos `−5, 0, 3`. Signos: `(−∞; −5)` negativo, `(−5; 0)` positivo, `(0; 3)` negativo, `(3; +∞)` positivo.",
            "Dominio de h): `[−5; 0) ∪ (3; +∞)`.",
            "i) Índice 6 (par): `(x + 1)/(x(x − 4)) ≥ 0`. Críticos `−1, 0, 4`. Signos: `(−∞; −1)` negativo, `(−1; 0)` positivo, `(0; 4)` negativo, `(4; +∞)` positivo.",
            "Dominio de i): `[−1; 0) ∪ (4; +∞)`. Los valores que anulan el denominador (0 y 4) siempre quedan afuera.",
        ],
    ),
    # ---------- Ej. 24: ceros, C⁺ y C⁻ de polinómicas ----------
    _p(
        "tp5-24-i", ESTUDIO, 2, "Matemática · TP5, ej. 24 i (a y b)",
        "Polinómica con una raíz doble",
        "Dada `f(x) = 2(x − 1)²(x + 3)`, determiná ceros y ordenada al origen, e intervalos de positividad y negatividad.",
        [
            _n("a) ¿Cuánto vale la ordenada al origen?", 6, "6"),
            _c("b) ¿Cuáles son los ceros?", ["x = 1 (doble) y x = −3 (simple)", "x = −1 (doble) y x = 3 (simple)", "x = 1 (simple) y x = −3 (doble)", "x = 1, x = −3 y x = 2"], "x = 1 (doble) y x = −3 (simple)"),
            _c("c) ¿Cuáles son los conjuntos de positividad y negatividad?",
               ["C⁺ = (−3; 1) ∪ (1; +∞); C⁻ = (−∞; −3)", "C⁺ = (−3; +∞); C⁻ = (−∞; −3)",
                "C⁺ = (1; +∞); C⁻ = (−∞; −3) ∪ (−3; 1)", "C⁺ = (−∞; −3) ∪ (1; +∞); C⁻ = (−3; 1)"],
               "C⁺ = (−3; 1) ∪ (1; +∞); C⁻ = (−∞; −3)"),
        ],
        [
            "En un cero de multiplicidad par la gráfica toca el eje y rebota: el signo NO cambia.",
        ],
        [
            "Ceros: `(x − 1)² = 0` → `x = 1` (doble); `x + 3 = 0` → `x = −3` (simple).",
            "Ordenada: `f(0) = 2·(−1)²·3 = 6`.",
            "`2(x − 1)² ≥ 0` siempre, así que el signo lo decide `(x + 3)`: positivo si `x > −3`, negativo si `x < −3`.",
            "En `x = 1` la función vale 0 (no es positiva), así que se excluye: `C⁺ = (−3; 1) ∪ (1; +∞)`, `C⁻ = (−∞; −3)`.",
        ],
    ),
    _p(
        "tp5-24-iv", ESTUDIO, 3, "Matemática · TP5, ej. 24 iv (a y b)",
        "Polinómica con raíces triple, doble y simple",
        "Dada `f(x) = (x + 1)³(x − 2)²(x + 4)`, determiná ceros y ordenada al origen, e intervalos de positividad y negatividad.",
        [
            _n("a) ¿Cuánto vale la ordenada al origen?", 16, "16"),
            _c("b) ¿Cuáles son los ceros?", ["x = −1 (triple), x = 2 (doble) y x = −4 (simple)", "x = 1 (triple), x = −2 (doble) y x = 4 (simple)",
                                            "x = −1 (doble), x = 2 (triple) y x = −4 (simple)", "x = −1, x = 2 y x = −4, los tres simples"],
               "x = −1 (triple), x = 2 (doble) y x = −4 (simple)"),
            _c("c) ¿Cuáles son los conjuntos de positividad y negatividad?",
               ["C⁺ = (−∞; −4) ∪ (−1; 2) ∪ (2; +∞); C⁻ = (−4; −1)", "C⁺ = (−4; −1); C⁻ = (−∞; −4) ∪ (−1; 2) ∪ (2; +∞)",
                "C⁺ = (−∞; −4) ∪ (−1; +∞); C⁻ = (−4; −1)", "C⁺ = (−∞; −4) ∪ (2; +∞); C⁻ = (−4; −1) ∪ (−1; 2)"],
               "C⁺ = (−∞; −4) ∪ (−1; 2) ∪ (2; +∞); C⁻ = (−4; −1)"),
        ],
        [
            "Multiplicidad impar: la gráfica atraviesa el eje (cambia el signo). Par: rebota.",
            "Probá un valor grande, por ejemplo `x = 3`, y recorré la recta hacia la izquierda.",
        ],
        [
            "Ceros: `x = −1` (triple), `x = 2` (doble), `x = −4` (simple).",
            "Ordenada: `f(0) = 1³·(−2)²·4 = 16`.",
            "Para `x > 2` todos los factores son positivos: `f > 0`. En `x = 2` (doble) no cambia: también positiva en `(−1; 2)`.",
            "En `x = −1` (triple) cambia: negativa en `(−4; −1)`. En `x = −4` (simple) cambia otra vez: positiva en `(−∞; −4)`.",
            "`C⁺ = (−∞; −4) ∪ (−1; 2) ∪ (2; +∞)`; `C⁻ = (−4; −1)`.",
        ],
    ),
    _p(
        "tp5-24-v", ESTUDIO, 2, "Matemática · TP5, ej. 24 v (a y b)",
        "Polinómica con coeficiente principal negativo",
        "Dada `f(x) = −2(x + 2)²(x − 4)³`, determiná ceros y ordenada al origen, e intervalos de positividad y negatividad.",
        [
            _n("a) ¿Cuánto vale la ordenada al origen?", 512, "512"),
            _c("b) ¿Cuáles son los ceros?", ["x = −2 (doble) y x = 4 (triple)", "x = 2 (doble) y x = −4 (triple)", "x = −2 (triple) y x = 4 (doble)", "x = −2, x = 4 y x = −1"], "x = −2 (doble) y x = 4 (triple)"),
            _c("c) ¿Cuáles son los conjuntos de positividad y negatividad?",
               ["C⁺ = (−∞; −2) ∪ (−2; 4); C⁻ = (4; +∞)", "C⁺ = (4; +∞); C⁻ = (−∞; −2) ∪ (−2; 4)",
                "C⁺ = (−2; 4); C⁻ = (−∞; −2) ∪ (4; +∞)", "C⁺ = (−∞; 4); C⁻ = (4; +∞)"],
               "C⁺ = (−∞; −2) ∪ (−2; 4); C⁻ = (4; +∞)"),
        ],
        [
            "Cuidado con los signos al calcular `f(0)`: `(−4)³` es negativo.",
            "El factor `(x + 2)²` nunca es negativo; el signo lo deciden `−2` y `(x − 4)³`.",
        ],
        [
            "Ceros: `x = −2` (doble) y `x = 4` (triple).",
            "Ordenada: `f(0) = −2·2²·(−4)³ = −2·4·(−64) = 512`.",
            "Para `x > 4`: `(x − 4)³ > 0`, y con el `−2` adelante, `f < 0`. Para `x < 4` (y `x ≠ −2`): `(x − 4)³ < 0`, entonces `f > 0`.",
            "`C⁺ = (−∞; −2) ∪ (−2; 4)`; `C⁻ = (4; +∞)`. En `x = −2` la gráfica rebota sin cambiar de signo.",
        ],
    ),
    # ---------- Ej. 16, 17 y 18: valores y preimágenes ----------
    _p(
        "tp5-16", FUN, 1, "Matemática · TP5, ej. 16",
        "Evaluar funciones en expresiones",
        "Dadas las funciones I) `f(x) = −3x² + 2x` y II) `f(x) = x/(x + 1)`, determiná para cada una `f(2a)`, `f(a²)`, `f(5x)` y `f(a + 1)`.",
        [
            _c("a) Para I), ¿cuánto vale `f(2a)`?", ["−12a² + 4a", "−6a² + 4a", "−36a² + 4a", "−12a² + 2a"], "−12a² + 4a"),
            _c("b) Para I), ¿cuánto vale `f(a + 1)`?", ["−3a² − 4a − 1", "−3a² + 2a + 1", "−3a² − 6a − 1", "−3a² + 2a − 1"], "−3a² − 4a − 1"),
            _c("c) Para II), ¿cuánto vale `f(a + 1)`?", ["(a + 1)/(a + 2)", "a/(a + 1) + 1", "(a + 1)/(a + 1)", "a/(a + 2)"], "(a + 1)/(a + 2)"),
        ],
        [
            "Reemplazá cada `x` por la expresión completa, entre paréntesis.",
        ],
        [
            "I) `f(2a) = −3(2a)² + 2(2a) = −3·4a² + 4a = −12a² + 4a`. Error típico: `−3·2a²`, sin elevar el 2.",
            "I) `f(a + 1) = −3(a + 1)² + 2(a + 1) = −3a² − 6a − 3 + 2a + 2 = −3a² − 4a − 1`.",
            "I) Los otros: `f(a²) = −3a⁴ + 2a²`, `f(5x) = −75x² + 10x`.",
            "II) `f(a + 1) = (a + 1)/((a + 1) + 1) = (a + 1)/(a + 2)`.",
            "II) Los otros: `f(2a) = 2a/(2a + 1)`, `f(a²) = a²/(a² + 1)`, `f(5x) = 5x/(5x + 1)`.",
        ],
    ),
    _p(
        "tp5-17", FUN, 1, "Matemática · TP5, ej. 17 c, d",
        "Valores de funciones",
        "Calculá los valores indicados:\n\nc) `f(x) = (1 − x)/(1 + x)`: `f(½)`, `f(t)`, `f(1/a)`, `f(x + h)`.\n\nd) `g(x) = x + 1/x`: `g(−2)`, `g(⅓)`, `g(3a)`, `g(a²)`, `g(x + h)`.",
        [
            _n("a) ¿Cuánto vale `f(½)`? Podés responder con fracción.", 1 / 3, "1/3", 0.002),
            _c("b) ¿Cuánto vale `f(1/a)` (con `a ≠ 0`, `a ≠ −1`)?", ["(a − 1)/(a + 1)", "(1 − a)/(1 + a)", "(a + 1)/(a − 1)", "a(1 − a)/(1 + a)"], "(a − 1)/(a + 1)"),
            _n("c) ¿Cuánto vale `g(⅓)`? Podés responder con fracción.", 10 / 3, "10/3", 0.001),
        ],
        [
            "En `f(1/a)`, multiplicá numerador y denominador por `a` para sacar las fracciones internas.",
        ],
        [
            "c) `f(½) = (1 − ½)/(1 + ½) = (½)/(3/2) = 1/3`. `f(t) = (1 − t)/(1 + t)`.",
            "c) `f(1/a) = (1 − 1/a)/(1 + 1/a)`; multiplicando arriba y abajo por `a`: `(a − 1)/(a + 1)`. Además `f(x + h) = (1 − x − h)/(1 + x + h)`.",
            "d) `g(⅓) = ⅓ + 1/(⅓) = ⅓ + 3 = 10/3`. Error típico: calcular `1/(⅓)` como `⅓`.",
            "d) Además `g(−2) = −2 + 1/(−2) = −5/2`.",
            "d) Los otros: `g(3a) = 3a + 1/(3a)`, `g(a²) = a² + 1/a²`, `g(x + h) = x + h + 1/(x + h)`.",
        ],
    ),
    _p(
        "tp5-18-a", FUN, 1, "Matemática · TP5, ej. 18 a, b, e",
        "Preimágenes: ¿para qué x la función vale tanto?",
        "Determiná:\n\na) ¿Para qué valores de x la función `f(x) = 6x² − 1` es igual a 23?\n\n"
        "b) ¿Para qué valores de x la función `g(x) = √(x − 4)` es igual a 2?\n\n"
        "e) ¿Para qué valores de x la función `h(x) = (x − 1)³ + 2` es igual a −6?",
        [
            _c("a) ¿Para qué valores de x?", ["x = −2 y x = 2", "x = 2", "x = 4", "x = −4 y x = 4"], "x = −2 y x = 2"),
            _n("b) ¿Para qué valor de x?", 8, "8"),
            _n("e) ¿Para qué valor de x?", -1, "−1"),
        ],
        [
            "Planteá la ecuación `f(x) = valor` y despejá x.",
            "Si una potencia par es igual a un número positivo hay dos soluciones (±); si es impar, hay una sola.",
        ],
        [
            "a) `6x² − 1 = 23` → `x² = 4` → `x = ±2`.",
            "b) `√(x − 4) = 2` → `x − 4 = 4` → `x = 8`. Verificación: `√4 = 2` ✓.",
            "e) `(x − 1)³ + 2 = −6` → `(x − 1)³ = −8` → `x − 1 = −2` → `x = −1`.",
            "Verificación de e): `(−2)³ + 2 = −8 + 2 = −6` ✓.",
        ],
    ),
    _p(
        "tp5-18-b", FUN, 2, "Matemática · TP5, ej. 18 c, d",
        "Preimágenes con valor absoluto y con cuadrado",
        "Determiná:\n\nc) ¿Para qué valores de x la función `h(x) = |2x − 5|` es igual a 3?\n\n"
        "d) ¿Para qué valores de x la función `f(x) = (x + 3)² − 1` es igual a 7?",
        [
            _c("c) ¿Para qué valores de x?", ["x = 1 y x = 4", "x = 4", "x = −1 y x = 4", "x = 1 y x = −4"], "x = 1 y x = 4"),
            _c("d) ¿Para qué valores de x?", ["x = −3 − 2√2 y x = −3 + 2√2", "x = −3 + 2√2", "x = 3 − 2√2 y x = 3 + 2√2", "x = −1 y x = −5"], "x = −3 − 2√2 y x = −3 + 2√2"),
        ],
        [
            "`|A| = 3` significa `A = 3` o `A = −3`.",
            "En d), aislá el cuadrado y tomá raíz con `±`.",
        ],
        [
            "c) `2x − 5 = 3` → `x = 4`; `2x − 5 = −3` → `x = 1`. Verificación: `|3| = 3` y `|−3| = 3` ✓.",
            "d) `(x + 3)² − 1 = 7` → `(x + 3)² = 8` → `x + 3 = ±√8 = ±2√2`.",
            "Entonces `x = −3 + 2√2 ≈ −0,17` o `x = −3 − 2√2 ≈ −5,83`.",
            "Error típico en d): `(x + 3)² = 8` no da `x + 3 = 4` ni `x + 3 = ±2`; la raíz de 8 es `2√2`.",
        ],
    ),
    # ---------- Ej. 9: modelización con dominio ----------
    _p(
        "tp5-9-a", DOM, 2, "Matemática · TP5, ej. 9 b, c, d",
        "Modelos geométricos y su dominio",
        "Expresá la variable indicada en función de la otra e indicá el dominio teniendo en cuenta el contexto:\n\n"
        "b) Un rectángulo tiene un ancho `x` y su largo es 5 unidades mayor que su ancho. Expresá el área en función del ancho.\n\n"
        "c) Un cuadrado tiene una diagonal de longitud `x`. Expresá el área del cuadrado en función de su diagonal.\n\n"
        "d) Un rectángulo tiene un área de 48 cm². Si su base mide `x` cm, expresá su perímetro P en función de la base.",
        [
            _c("b) ¿Cuál es el modelo?", ["A(x) = x(x + 5), D = (0; +∞)", "A(x) = x + 5, D = (0; +∞)", "A(x) = x(x + 5), D = IR", "A(x) = 2x + 2(x + 5), D = (0; +∞)"], "A(x) = x(x + 5), D = (0; +∞)"),
            _c("c) ¿Cuál es el modelo?", ["A(x) = x²/2, D = (0; +∞)", "A(x) = x², D = (0; +∞)", "A(x) = x²/4, D = (0; +∞)", "A(x) = 2x², D = (0; +∞)"], "A(x) = x²/2, D = (0; +∞)"),
            _c("d) ¿Cuál es el modelo?", ["P(x) = 2x + 96/x, D = (0; +∞)", "P(x) = 2x + 48/x, D = (0; +∞)", "P(x) = 2x + 96/x, D = IR − {0}", "P(x) = x + 48/x, D = (0; +∞)"], "P(x) = 2x + 96/x, D = (0; +∞)"),
        ],
        [
            "Las longitudes tienen que ser positivas: eso define el dominio aunque la fórmula admita otros valores.",
            "c) Si el lado es `ℓ`, por Pitágoras la diagonal cumple `x² = ℓ² + ℓ²`.",
        ],
        [
            "b) Largo `x + 5`, área `A(x) = x(x + 5) = x² + 5x`. El ancho tiene que ser positivo: `D = (0; +∞)`.",
            "c) `x² = 2ℓ²` → `ℓ² = x²/2`. Como el área es `ℓ²`, `A(x) = x²/2`, con `D = (0; +∞)`.",
            "d) Altura: `48/x`. Perímetro: `P(x) = 2x + 2·48/x = 2x + 96/x`.",
            "La base es una longitud: `x > 0`, `D = (0; +∞)`. Matemáticamente la fórmula admite negativos, pero el contexto no.",
        ],
    ),
    _p(
        "tp5-9-b", DOM, 2, "Matemática · TP5, ej. 9 e, f",
        "Modelos del consumo de datos y de la caja sin tapa",
        "Expresá la variable indicada en función de la otra e indicá el dominio teniendo en cuenta el contexto:\n\n"
        "e) Karina contrató un plan de telefonía celular por el cual cada 30 días dispone de 10 Gb para navegar. En ese período usa la misma cantidad de gigabytes cada día, y al final del período le queda exactamente 1 Gb sin consumir. Expresá la cantidad de gigabytes consumidos C en función de los días t transcurridos.\n\n"
        "f) Se dispone de una lámina rectangular de 30 cm de largo y 20 cm de ancho. Se recortan cuadrados de lado `x` en cada una de sus cuatro esquinas y se doblan los bordes para formar una caja sin tapa. Expresá el volumen de la caja en función de `x`.",
        [
            _c("e) ¿Cuál es el modelo?", ["C(t) = 0,3·t, D = [0; 30]", "C(t) = t/3, D = [0; 30]", "C(t) = 0,3·t, D = [0; +∞)", "C(t) = 10 − 0,3·t, D = [0; 30]"], "C(t) = 0,3·t, D = [0; 30]"),
            _c("f) ¿Cuál es el modelo?", ["V(x) = x(30 − 2x)(20 − 2x), D = (0; 10)", "V(x) = x(30 − x)(20 − x), D = (0; 20)",
                                         "V(x) = x(30 − 2x)(20 − 2x), D = (0; 15)", "V(x) = (30 − 2x)(20 − 2x), D = (0; 10)"],
               "V(x) = x(30 − 2x)(20 − 2x), D = (0; 10)"),
        ],
        [
            "e) ¿Cuántos Gb consume en total en los 30 días? Dividilo por la cantidad de días.",
            "f) Al recortar `x` en cada esquina, cada lado de la base pierde `2x`; la altura de la caja es `x`.",
        ],
        [
            "e) En 30 días consume `10 − 1 = 9` Gb, es decir `9/30 = 0,3` Gb por día. Entonces `C(t) = 0,3·t`.",
            "El período dura 30 días: `D = [0; 30]` (en `t = 30`, `C = 9` Gb y le queda 1 Gb ✓).",
            "f) Base de la caja: `(30 − 2x)` por `(20 − 2x)`; altura `x`. `V(x) = x(30 − 2x)(20 − 2x)`.",
            "Hace falta `x > 0` y que el lado menor siga siendo positivo: `20 − 2x > 0` → `x < 10`. `D = (0; 10)`.",
            "Error típico en e): usar los 10 Gb completos (`t/3`), pero le sobra 1 Gb.",
        ],
    ),
]

# ======================================================================
# TP6 · FUNCIONES EXPONENCIALES Y LOGARÍTMICAS
# ======================================================================
EXPLOG = "a2-ecuaciones-exponenciales-logaritmicas"
LOG = "a2-logaritmos"
GRAF = "a2-graficas-exp-log"
MOD = "a2-modelos-exponenciales"

TP6 = [
    # ---------- Ej. 19 y 20: ecuaciones exponenciales ----------
    _p(
        "tp6-19-a", EXPLOG, 2, "Matemática · TP6, ej. 19 b, c, g",
        "Ecuaciones exponenciales: igualar bases",
        "Resolvé las siguientes ecuaciones y verificá:\n\n"
        "b) `∛36 / 36^(x+1) = 6^(−x) / 6`\n\nc) `(2/3)^(5x) = 27/8`\n\ng) `3·2^(x+1) − 4·2^(x−2) − 6·2^x = −4`",
        [
            _n("b) ¿Cuánto vale x? Podés responder con fracción.", -1 / 3, "−1/3", 0.002),
            _n("c) ¿Cuánto vale x? Podés responder con fracción.", -0.6, "−3/5 (= −0,6)"),
            _n("g) ¿Cuánto vale x?", 2, "2"),
        ],
        [
            "b) Escribí todo como potencia de 6: `36 = 6²`, `∛36 = 6^(2/3)`.",
            "c) `27/8 = (3/2)³ = (2/3)^(−3)`.",
            "g) Escribí cada potencia como `2^x` por un número y sacá factor común `2^x`.",
        ],
        [
            "b) Izquierda: `6^(2/3) / 6^(2x+2) = 6^(2/3 − 2x − 2)`. Derecha: `6^(−x − 1)`.",
            "Igualando exponentes: `2/3 − 2x − 2 = −x − 1` → `−x = 1/3` → `x = −1/3`.",
            "c) `(2/3)^(5x) = (2/3)^(−3)` → `5x = −3` → `x = −3/5`.",
            "g) `3·2·2^x − 4·(1/4)·2^x − 6·2^x = (6 − 1 − 6)·2^x = −2^x`. Entonces `−2^x = −4` → `2^x = 4` → `x = 2`.",
            "Verificación de g): `3·8 − 4·1 − 6·4 = 24 − 4 − 24 = −4` ✓.",
        ],
    ),
    _p(
        "tp6-19-b", EXPLOG, 2, "Matemática · TP6, ej. 19 h, j, k",
        "Ecuaciones exponenciales: factor común y bases iguales",
        "Resolvé las siguientes ecuaciones y verificá:\n\n"
        "h) `2^(x−2) + 2^(x−1) + 2^x + 2^(x+1) = 30`\n\nj) `25^(x−3) = (1/5)^(3x+18)`\n\nk) `9^x = (1/3)^(x² − x)`",
        [
            _n("h) ¿Cuánto vale x?", 3, "3"),
            _n("j) ¿Cuánto vale x? Podés responder con fracción.", -2.4, "−12/5 (= −2,4)"),
            _c("k) ¿Cuál es el conjunto solución?", ["S = {−1; 0}", "S = {0; 1}", "S = {−1}", "S = {0; 3}"], "S = {−1; 0}"),
        ],
        [
            "h) Sacá factor común `2^x`: `2^(x−2) = 2^x/4`.",
            "j) y k) Pasá todo a base 5 o base 3: `25 = 5²`, `1/5 = 5^(−1)`, `9 = 3²`, `1/3 = 3^(−1)`.",
        ],
        [
            "h) `2^x(¼ + ½ + 1 + 2) = 2^x·15/4 = 30` → `2^x = 8` → `x = 3`. Verificación: `2 + 4 + 8 + 16 = 30` ✓.",
            "j) `5^(2x − 6) = 5^(−3x − 18)` → `2x − 6 = −3x − 18` → `5x = −12` → `x = −12/5`.",
            "k) `3^(2x) = 3^(−x² + x)` → `2x = −x² + x` → `x² + x = 0` → `x(x + 1) = 0`.",
            "Soluciones de k): `x = 0` o `x = −1`. Verificación: con `x = −1`, `9^(−1) = 1/9` y `(1/3)^(1 + 1) = 1/9` ✓.",
        ],
    ),
    _p(
        "tp6-20", EXPLOG, 3, "Matemática · TP6, ej. 20 a, c, h",
        "Ecuaciones exponenciales con cambio de variable",
        "Resolvé las siguientes ecuaciones y verificá:\n\n"
        "a) `2^(2x) + 3·2^x = 10`\n\nc) `3^(2(x+1)) − 28·3^x = −3`\n\nh) `4^(x−1) − 2^(x+2) = 128`",
        [
            _n("a) ¿Cuánto vale x?", 1, "1"),
            _c("c) ¿Cuál es el conjunto solución?", ["S = {−2; 1}", "S = {1}", "S = {−2; 3}", "S = {2; −1}"], "S = {−2; 1}"),
            _n("h) ¿Cuánto vale x?", 5, "5"),
        ],
        [
            "Llamá `t = 2^x` (o `t = 3^x`); entonces `2^(2x) = t²` y te queda una cuadrática.",
            "Descartá las soluciones `t ≤ 0`: una exponencial nunca vale cero ni es negativa.",
        ],
        [
            "a) Con `t = 2^x`: `t² + 3t − 10 = 0` → `t = 2` o `t = −5`. Solo `2^x = 2` → `x = 1`.",
            "c) `3^(2x + 2) = 9·(3^x)²`. Con `t = 3^x`: `9t² − 28t + 3 = 0` → `t = (28 ± 26)/18` → `t = 3` o `t = 1/9`.",
            "`3^x = 3` → `x = 1`; `3^x = 1/9` → `x = −2`. `S = {−2; 1}`.",
            "h) `4^(x−1) = (2^x)²/4` y `2^(x+2) = 4·2^x`. Con `t = 2^x`: `t²/4 − 4t − 128 = 0` → `t² − 16t − 512 = 0` → `t = (16 ± 48)/2`.",
            "`t = 32` o `t = −16` (se descarta). `2^x = 32` → `x = 5`. Verificación: `4⁴ − 2⁷ = 256 − 128 = 128` ✓.",
        ],
    ),
    # ---------- Ej. 21: valor exacto y aproximado ----------
    _p(
        "tp6-21-a", EXPLOG, 2, "Matemática · TP6, ej. 21 d, h",
        "Ecuaciones exponenciales con logaritmos (valor exacto y aproximado)",
        "Resolvé las siguientes ecuaciones. Indicá la respuesta en valor exacto y luego aproximala redondeando a 3 cifras decimales:\n\n"
        "d) `e^(3−5x) = 16`\n\nh) `50/(1 + e^(−x)) = 4`",
        [
            _c("d) ¿Cuál es el valor exacto?", ["x = (3 − ln 16)/5", "x = (ln 16 − 3)/5", "x = 3/5 − ln 16", "x = (3 − log 16)/5"], "x = (3 − ln 16)/5"),
            _n("d) ¿Cuánto vale x redondeado a 3 decimales?", 0.04548, "0,045 (valor de calculadora: 0,04548…)", 0.02),
            _n("h) ¿Cuánto vale x redondeado a 3 decimales?", -2.442, "−2,442 (x = −ln 11,5)", 0.01),
        ],
        [
            "Aislá la exponencial y aplicá `ln` a ambos miembros: `ln(e^A) = A`.",
            "h) Primero despejá `1 + e^(−x)`.",
        ],
        [
            "d) `3 − 5x = ln 16` → `5x = 3 − ln 16` → `x = (3 − ln 16)/5`.",
            "`ln 16 ≈ 2,772589`, entonces `x ≈ 0,227411/5 ≈ 0,045`.",
            "h) `1 + e^(−x) = 50/4 = 12,5` → `e^(−x) = 11,5` → `−x = ln 11,5` → `x = −ln 11,5`.",
            "`ln 11,5 ≈ 2,442347`, entonces `x ≈ −2,442`.",
            "Verificación de h): `e^(2,442) ≈ 11,5` y `50/12,5 = 4` ✓.",
        ],
    ),
    _p(
        "tp6-21-b", EXPLOG, 3, "Matemática · TP6, ej. 21 i, j",
        "Exponenciales con distinta base en ambos miembros",
        "Resolvé las siguientes ecuaciones. Indicá la respuesta en valor exacto y luego aproximala redondeando a 3 cifras decimales:\n\n"
        "i) `5^x = 4^(x+1)`\n\nj) `2^(3x+1) = 3^(x−2)`",
        [
            _n("i) ¿Cuánto vale x redondeado a 3 decimales?", 6.213, "6,213 (x = ln 4/(ln 5 − ln 4))", 0.01),
            _c("j) ¿Cuál es el valor exacto?", ["x = −(ln 2 + 2 ln 3)/(3 ln 2 − ln 3)", "x = (ln 2 + 2 ln 3)/(3 ln 2 − ln 3)",
                                                "x = (2 ln 3 − ln 2)/(3 ln 2 − ln 3)", "x = −(ln 2 + 2 ln 3)/(3 ln 2 + ln 3)"],
               "x = −(ln 2 + 2 ln 3)/(3 ln 2 − ln 3)"),
            _n("j) ¿Cuánto vale x redondeado a 3 decimales?", -2.947, "−2,947", 0.01),
        ],
        [
            "Aplicá logaritmo a ambos miembros y bajá los exponentes: `ln(aᵘ) = u·ln a`.",
            "Agrupá los términos con x de un lado y sacá x factor común.",
        ],
        [
            "i) `x·ln 5 = (x + 1)·ln 4` → `x(ln 5 − ln 4) = ln 4` → `x = ln 4/(ln 5 − ln 4) = ln 4/ln(5/4)`.",
            "`x ≈ 1,386294/0,223144 ≈ 6,213`.",
            "j) `(3x + 1) ln 2 = (x − 2) ln 3` → `3x ln 2 − x ln 3 = −2 ln 3 − ln 2`.",
            "`x = −(ln 2 + 2 ln 3)/(3 ln 2 − ln 3) = −ln 18/ln(8/3)`.",
            "`x ≈ −2,890372/0,980829 ≈ −2,947`. Verificación: `2^(−7,841) ≈ 0,00436` y `3^(−4,947) ≈ 0,00436` ✓.",
        ],
    ),
    # ---------- Ej. 22: ecuaciones logarítmicas ----------
    _p(
        "tp6-22-a", EXPLOG, 2, "Matemática · TP6, ej. 22 h, n, o",
        "Ecuaciones logarítmicas: verificar el dominio",
        "Resolvé las siguientes ecuaciones logarítmicas y verificá:\n\n"
        "h) `log x + log(x − 3) = 1`\n\nn) `log₅(x + 1) − log₅(x − 1) = 2`\n\no) `log₉(x − 5) + log₉(x + 3) = 1`",
        [
            _n("h) ¿Cuál es la solución?", 5, "5 (x = −2 se descarta)"),
            _n("n) ¿Cuál es la solución? Podés responder con fracción.", 13 / 12, "13/12", 0.002),
            _n("o) ¿Cuál es la solución?", 6, "6 (x = −4 se descarta)"),
        ],
        [
            "Juntá los logaritmos en uno solo (producto o cociente) y pasá a forma exponencial.",
            "Al final verificá que todos los argumentos originales sean positivos.",
        ],
        [
            "h) `log[x(x − 3)] = 1` → `x² − 3x = 10` → `x² − 3x − 10 = 0` → `x = 5` o `x = −2`.",
            "Con `x = −2`, `log(−2)` no existe: se descarta. Solución `x = 5` (`log 5 + log 2 = log 10 = 1` ✓).",
            "n) `log₅[(x + 1)/(x − 1)] = 2` → `(x + 1)/(x − 1) = 25` → `x + 1 = 25x − 25` → `x = 26/24 = 13/12`.",
            "Como `13/12 > 1`, ambos argumentos son positivos ✓.",
            "o) `log₉[(x − 5)(x + 3)] = 1` → `x² − 2x − 15 = 9` → `x² − 2x − 24 = 0` → `x = 6` o `x = −4`.",
            "Con `x = −4`, `x − 5 < 0`: se descarta. Solución `x = 6` (`log₉1 + log₉9 = 0 + 1` ✓).",
        ],
    ),
    _p(
        "tp6-22-b", EXPLOG, 3, "Matemática · TP6, ej. 22 g, j, l",
        "Ecuaciones logarítmicas con dos candidatos",
        "Resolvé las siguientes ecuaciones logarítmicas y verificá:\n\n"
        "g) `log₂(x² − x − 2) = 2`\n\nj) `ln(x − 1) + ln(x + 2) = 1`\n\nl) `2·log x = log 2 + log(3x − 4)`",
        [
            _c("g) ¿Cuál es el conjunto solución?", ["S = {−2; 3}", "S = {3}", "S = {−1; 2}", "S = {2; −3}"], "S = {−2; 3}"),
            _n("j) ¿Cuál es la solución, redondeada a 3 decimales?", 1.729, "1,729 (x = (−1 + √(9 + 4e))/2)", 0.01),
            _c("l) ¿Cuál es el conjunto solución?", ["S = {2; 4}", "S = {4}", "S = {2}", "S = {−2; −4}"], "S = {2; 4}"),
        ],
        [
            "No descartes por costumbre: comprobá cada candidato en los argumentos de la ecuación ORIGINAL.",
            "j) Te queda una cuadrática con `e` en el término independiente: usá la resolvente.",
        ],
        [
            "g) `x² − x − 2 = 2² = 4` → `x² − x − 6 = 0` → `x = 3` o `x = −2`. En ambos el argumento vale 4 > 0: valen los dos. `S = {−2; 3}`.",
            "j) `ln[(x − 1)(x + 2)] = 1` → `x² + x − 2 = e` → `x² + x − (2 + e) = 0`.",
            "`x = (−1 ± √(1 + 4(2 + e)))/2 = (−1 ± √(9 + 4e))/2`. La raíz negativa da `x − 1 < 0` (se descarta). `x ≈ (−1 + 4,4579)/2 ≈ 1,729`.",
            "l) `log x² = log[2(3x − 4)]` → `x² = 6x − 8` → `x² − 6x + 8 = 0` → `x = 2` o `x = 4`.",
            "Ambos cumplen `x > 0` y `3x − 4 > 0`: `S = {2; 4}`. Verificación con 2: `2 log 2 = log 4` y `log 2 + log 2 = log 4` ✓.",
        ],
    ),
    # ---------- Ej. 24 y 25: ceros, ordenada, dominio ----------
    _p(
        "tp6-24", GRAF, 1, "Matemática · TP6, ej. 24 d, h",
        "Cero y ordenada al origen de exponenciales",
        "Buscá en forma analítica el cero y la ordenada al origen, si existen, de las siguientes funciones exponenciales:\n\n"
        "d) `f(x) = (½)^(x−2) − 8`\n\nh) `f(x) = (⅓)^(x+1) − 27`",
        [
            _n("d) ¿Cuál es el cero?", -1, "−1"),
            _n("d) ¿Cuál es la ordenada al origen?", -4, "−4"),
            _n("h) ¿Cuál es el cero?", -4, "−4 (la ordenada es −80/3)"),
        ],
        [
            "Cero: igualá a 0 y escribí el número como potencia de la misma base: `8 = (½)^(−3)`, `27 = (⅓)^(−3)`.",
            "Ordenada: calculá `f(0)`.",
        ],
        [
            "d) `(½)^(x−2) = 8 = (½)^(−3)` → `x − 2 = −3` → `x = −1`.",
            "d) `f(0) = (½)^(−2) − 8 = 4 − 8 = −4`.",
            "h) `(⅓)^(x+1) = 27 = (⅓)^(−3)` → `x + 1 = −3` → `x = −4`.",
            "h) `f(0) = (⅓)¹ − 27 = −80/3`.",
        ],
    ),
    _p(
        "tp6-25-a", GRAF, 2, "Matemática · TP6, ej. 25 e",
        "Dominio, cero y ordenada de una logarítmica",
        "Dada `f(x) = log₂(6 − 5x)`, hallá el dominio, el cero de la función y la ordenada al origen.",
        [
            _c("a) ¿Cuál es el dominio?", ["D = (−∞; 6/5)", "D = (6/5; +∞)", "D = (−∞; 6/5]", "D = (−∞; 5/6)"], "D = (−∞; 6/5)"),
            _n("b) ¿Cuál es el cero?", 1, "1"),
            _n("c) ¿Cuál es la ordenada al origen, redondeada a 3 decimales?", 2.585, "2,585 (= log₂ 6)", 0.01),
        ],
        [
            "El argumento del logaritmo tiene que ser estrictamente positivo.",
            "`log₂ A = 0` cuando `A = 1`.",
        ],
        [
            "Dominio: `6 − 5x > 0` → `x < 6/5`. `D = (−∞; 6/5)`.",
            "Cero: `6 − 5x = 1` → `x = 1` (está en el dominio ✓).",
            "Ordenada: `f(0) = log₂ 6 = ln 6/ln 2 ≈ 2,585`.",
            "Ojo al despejar: `−5x > −6` → al dividir por `−5` se invierte la desigualdad: `x < 6/5`.",
        ],
    ),
    _p(
        "tp6-25-b", GRAF, 3, "Matemática · TP6, ej. 25 g, h",
        "Logarítmicas con argumento cuadrático",
        "Dadas las funciones g) `f(x) = log₃(x² − 1)` y h) `f(x) = ln(2x − x²)`, hallá el dominio, los ceros y la ordenada al origen.",
        [
            _c("g) ¿Cuál es el dominio?", ["D = (−∞; −1) ∪ (1; +∞)", "D = (−1; 1)", "D = IR − {−1; 1}", "D = (1; +∞)"], "D = (−∞; −1) ∪ (1; +∞)"),
            _c("g) ¿Cuáles son los ceros y la ordenada al origen?", ["Ceros: −√2 y √2; no tiene ordenada al origen", "Ceros: −√2 y √2; ordenada: 0",
                                                                    "Cero: √2; no tiene ordenada al origen", "Ceros: −1 y 1; ordenada: −1"],
               "Ceros: −√2 y √2; no tiene ordenada al origen"),
            _c("h) ¿Cuáles son el dominio, los ceros y la ordenada?", ["D = (0; 2); cero: 1; no tiene ordenada al origen", "D = (0; 2); ceros: 0 y 2; ordenada: 0",
                                                                       "D = (−∞; 0) ∪ (2; +∞); cero: 1; no tiene ordenada", "D = (0; 2); cero: 1; ordenada: 0"],
               "D = (0; 2); cero: 1; no tiene ordenada al origen"),
        ],
        [
            "Dominio: resolvé la inecuación cuadrática `argumento > 0`.",
            "Hay ordenada al origen solo si `x = 0` pertenece al dominio.",
        ],
        [
            "g) `x² − 1 > 0` → `|x| > 1` → `D = (−∞; −1) ∪ (1; +∞)`.",
            "g) Ceros: `x² − 1 = 1` → `x² = 2` → `x = ±√2` (ambos en el dominio). Como `0 ∉ D`, no tiene ordenada al origen.",
            "h) `2x − x² = x(2 − x) > 0` → `D = (0; 2)`.",
            "h) Cero: `2x − x² = 1` → `x² − 2x + 1 = 0` → `(x − 1)² = 0` → `x = 1`. Como `0 ∉ D`, no tiene ordenada al origen.",
        ],
    ),
    # ---------- Ej. 11 y 12: propiedades ----------
    _p(
        "tp6-11", LOG, 2, "Matemática · TP6, ej. 11 m, n, o",
        "Desarrollar logaritmos con propiedades",
        "Usá las propiedades del logaritmo para desarrollar la expresión dada:\n\n"
        "m) `log(x³y⁴/z⁶)`\n\nn) `log √((x² + 4)/((x² + 1)(x³ − 7)²))`\n\no) `log √(x·√(y·√z))`",
        [
            _c("m) ¿Cuál es el desarrollo?", ["3 log x + 4 log y − 6 log z", "3 log x + 4 log y + 6 log z", "12 log(xy) − 6 log z", "3 log x · 4 log y − 6 log z"], "3 log x + 4 log y − 6 log z"),
            _c("n) ¿Cuál es el desarrollo?", ["½ log(x² + 4) − ½ log(x² + 1) − log(x³ − 7)", "½ log(x² + 4) − ½ log(x² + 1) − 2 log(x³ − 7)",
                                              "½ log(x² + 4) − ½ log(x² + 1) + log(x³ − 7)", "log x + log 2 − ½ log(x² + 1) − log(x³ − 7)"],
               "½ log(x² + 4) − ½ log(x² + 1) − log(x³ − 7)"),
            _c("o) ¿Cuál es el desarrollo?", ["½ log x + ¼ log y + ⅛ log z", "½ log x + ½ log y + ½ log z", "½ log x + ¼ log y + ¼ log z", "log x + ½ log y + ¼ log z"], "½ log x + ¼ log y + ⅛ log z"),
        ],
        [
            "`log(A·B) = log A + log B`, `log(A/B) = log A − log B`, `log Aⁿ = n·log A` y `√A = A^(1/2)`.",
            "El logaritmo de una suma (como `x² + 4`) NO se separa.",
        ],
        [
            "m) `log(x³y⁴) − log z⁶ = 3 log x + 4 log y − 6 log z`.",
            "n) La raíz es potencia ½: `½·[log(x² + 4) − log(x² + 1) − log(x³ − 7)²]`.",
            "Como `log(x³ − 7)² = 2 log(x³ − 7)` (válido para `x³ − 7 > 0`; en general es `2·log|x³ − 7|`), multiplicado por ½ queda `log(x³ − 7)`: resultado `½ log(x² + 4) − ½ log(x² + 1) − log(x³ − 7)`.",
            "o) `√(x·√(y·√z)) = x^(1/2)·y^(1/4)·z^(1/8)` (cada raíz anidada vuelve a dividir por 2).",
            "Resultado de o): `½ log x + ¼ log y + ⅛ log z`.",
        ],
    ),
    _p(
        "tp6-12", LOG, 2, "Matemática · TP6, ej. 12 b, f, h",
        "Agrupar en un solo logaritmo",
        "Usá las propiedades del logaritmo para escribir las siguientes expresiones usando un solo logaritmo:\n\n"
        "b) `log 12 + ½·log 7 − log 2`\n\nf) `4·log x − ⅓·log(x² + 1) + 2·log(x − 1)`\n\nh) `2(log₅x + 2 log₅y − 3·log₅z)`",
        [
            _c("b) ¿Cuál es la expresión?", ["log(6√7)", "log 42", "log(24√7)", "log(12√7 − 2)"], "log(6√7)"),
            _c("f) ¿Cuál es la expresión?", ["log[x⁴(x − 1)²/∛(x² + 1)]", "log[x⁴(x − 1)²·∛(x² + 1)]", "log[x⁴(x − 1)²/(x² + 1)³]", "log[8x(x − 1)/(x² + 1)]"], "log[x⁴(x − 1)²/∛(x² + 1)]"),
            _c("h) ¿Cuál es la expresión?", ["log₅(x²y⁴/z⁶)", "log₅(xy²/z³)", "log₅(x²y⁴z⁶)", "log₅(2xy²/z³)"], "log₅(x²y⁴/z⁶)"),
        ],
        [
            "Primero subí los coeficientes como exponentes (`n·log A = log Aⁿ`), después juntá sumas en productos y restas en cocientes.",
        ],
        [
            "b) `½ log 7 = log √7`. Entonces `log(12·√7/2) = log(6√7)`.",
            "f) `log x⁴ − log(x² + 1)^(1/3) + log(x − 1)² = log[x⁴(x − 1)²/∛(x² + 1)]`.",
            "h) Adentro: `log₅x + log₅y² − log₅z³ = log₅(xy²/z³)`. Por 2: `log₅(xy²/z³)² = log₅(x²y⁴/z⁶)`.",
            "Verificación numérica de b): `log 12 + ½ log 7 − log 2 ≈ 1,0792 + 0,4225 − 0,3010 = 1,2007` y `log(6√7) = log 15,875 ≈ 1,2007` ✓.",
        ],
    ),
    # ---------- Cuadros de los ej. 2-4 y 14-16 ----------
    _p(
        "tp6-cuadros-exp", GRAF, 1, "Matemática · TP6, ej. 2, 3 y 4 (cuadros)",
        "Cuadros de funciones exponenciales",
        "Los ej. 2 a 4 piden graficar por desplazamientos y reflexiones a partir de `2^x` y `3^x`, y completar cuadros con imagen, ecuación de la asíntota, positividad, negatividad, cero, ordenada al origen y crecimiento. Completá estos datos:\n\n"
        "a) `y = 2^x − 4` (ej. 2): el cero.\n\nb) `y = 3^(x+2)` (ej. 3): la ordenada al origen.\n\nc) `y = −2^x` (ej. 4): imagen, asíntota y crecimiento.",
        [
            _n("a) ¿Cuál es el cero de `y = 2^x − 4`?", 2, "2"),
            _n("b) ¿Cuál es la ordenada al origen de `y = 3^(x+2)`?", 9, "9"),
            _c("c) ¿Qué corresponde a `y = −2^x`?", ["Im = (−∞; 0); asíntota y = 0; decreciente", "Im = (0; +∞); asíntota y = 0; decreciente",
                                                    "Im = (−∞; 0); asíntota x = 0; creciente", "Im = IR; asíntota y = −1; decreciente"],
               "Im = (−∞; 0); asíntota y = 0; decreciente"),
        ],
        [
            "Un desplazamiento vertical `+k` mueve la asíntota a `y = k`; uno horizontal no la mueve.",
            "`−2^x` es la reflexión de `2^x` respecto del eje x.",
        ],
        [
            "a) `2^x − 4 = 0` → `2^x = 4` → `x = 2`. Cuadro completo: Im `(−4; +∞)`, asíntota `y = −4`, C⁺ `(2; +∞)`, C⁻ `(−∞; 2)`, ordenada `−3`.",
            "(`y = 2^x + 2`: Im `(2; +∞)`, asíntota `y = 2`, C⁺ = IR, ordenada 3.)",
            "b) `f(0) = 3² = 9`. Im `(0; +∞)`, asíntota `y = 0`. (`y = 3^(x−1)`: asíntota `y = 0`, ordenada `⅓`, creciente.)",
            "c) `−2^x` toma los valores de `2^x` cambiados de signo: Im `(−∞; 0)`, asíntota `y = 0`, ordenada `−1`, C⁻ = IR y es decreciente en todo IR.",
            "(`y = 2^(−x)`: Im `(0; +∞)`, asíntota `y = 0`, ordenada 1, decreciente.)",
        ],
    ),
    _p(
        "tp6-cuadros-log", GRAF, 2, "Matemática · TP6, ej. 14, 15 y 16 (cuadros)",
        "Cuadros de funciones logarítmicas",
        "Los ej. 14 a 16 piden graficar por desplazamientos y reflexiones a partir de `log₂x` y completar cuadros con dominio, cero, ordenada al origen, asíntota, positividad y negatividad. Completá estos datos:\n\n"
        "a) `y = log₂(x + 3)` (ej. 14): la ordenada al origen.\n\nb) `y = log₂(x) − 3` (ej. 15): el cero.\n\nc) `y = log₂(−x)` (ej. 16): el cuadro completo.",
        [
            _n("a) ¿Cuál es la ordenada al origen de `y = log₂(x + 3)`, redondeada a 3 decimales?", 1.585, "1,585 (= log₂ 3)", 0.01),
            _n("b) ¿Cuál es el cero de `y = log₂(x) − 3`?", 8, "8"),
            _c("c) ¿Qué corresponde a `y = log₂(−x)`?", ["D = (−∞; 0); cero −1; asíntota x = 0; C⁺ = (−∞; −1); C⁻ = (−1; 0)",
                                                       "D = (−∞; 0); cero −1; asíntota x = 0; C⁺ = (−1; 0); C⁻ = (−∞; −1)",
                                                       "D = (0; +∞); cero 1; asíntota x = 0; C⁺ = (0; 1); C⁻ = (1; +∞)",
                                                       "D = (−∞; 0); cero 1; asíntota y = 0; C⁺ = (−∞; −1); C⁻ = (−1; 0)"],
               "D = (−∞; 0); cero −1; asíntota x = 0; C⁺ = (−∞; −1); C⁻ = (−1; 0)"),
        ],
        [
            "Un desplazamiento horizontal mueve la asíntota vertical; uno vertical no la mueve, pero cambia el cero.",
            "`log₂(−x)` es la reflexión de `log₂x` respecto del eje y.",
        ],
        [
            "a) `f(0) = log₂ 3 ≈ 1,585`. Cuadro: D `(−3; +∞)`, cero `−2`, asíntota `x = −3`, C⁺ `(−2; +∞)`, C⁻ `(−3; −2)`.",
            "(`y = log₂(x − 5)`: D `(5; +∞)`, cero 6, asíntota `x = 5`, C⁺ `(6; +∞)`, C⁻ `(5; 6)`.)",
            "b) `log₂x = 3` → `x = 2³ = 8`. D `(0; +∞)`, asíntota `x = 0`, C⁺ `(8; +∞)`, C⁻ `(0; 8)`. (`y = log₂x + 2`: cero `¼`, C⁺ `(¼; +∞)`, C⁻ `(0; ¼)`.)",
            "c) `−x > 0` → `D = (−∞; 0)`. Cero: `−x = 1` → `x = −1`. Asíntota `x = 0`. Positiva cuando `−x > 1`, o sea `x < −1`.",
            "(`y = −log₂x`: D `(0; +∞)`, cero 1, asíntota `x = 0`, C⁺ `(0; 1)`, C⁻ `(1; +∞)`.)",
        ],
    ),
    # ---------- Ej. 23, 26 y 27: modelos ----------
    _p(
        "tp6-23", MOD, 2, "Matemática · TP6, ej. 23 a, b, d",
        "Despejar en fórmulas exponenciales y logarítmicas",
        "Dadas las siguientes igualdades, despejá la variable indicada:\n\n"
        "a) `N = N₀·e^(−λt)`: despejá `t`.\n\nb) `A = log(I₀/I)`: despejá `I₀`.\n\nd) `V = V₀·e^(−t/(R·C))`: despejá `t`.",
        [
            _c("a) ¿Cuánto vale `t`?", ["t = ln(N₀/N)/λ", "t = ln(N/N₀)/λ", "t = (N₀/N)/(λ·e)", "t = ln(N₀ − N)/λ"], "t = ln(N₀/N)/λ"),
            _c("b) ¿Cuánto vale `I₀`?", ["I₀ = I·10^A", "I₀ = I·10^(−A)", "I₀ = I·e^A", "I₀ = I + 10^A"], "I₀ = I·10^A"),
            _c("d) ¿Cuánto vale `t`?", ["t = R·C·ln(V₀/V)", "t = −R·C·ln(V₀/V)", "t = ln(V₀/V)/(R·C)", "t = ln(V₀/V)/(R + C)"], "t = R·C·ln(V₀/V)"),
        ],
        [
            "Aislá primero la exponencial (dividiendo) y después aplicá `ln`.",
            "`log` es logaritmo decimal: su inversa es `10^`.",
        ],
        [
            "a) `e^(−λt) = N/N₀` → `−λt = ln(N/N₀)` → `t = −ln(N/N₀)/λ = ln(N₀/N)/λ`. (Igual se despeja `λ = ln(N₀/N)/t`.)",
            "b) `I₀/I = 10^A` → `I₀ = I·10^A`. (Y `I = I₀·10^(−A)`.)",
            "d) `e^(−t/(RC)) = V/V₀` → `−t/(RC) = ln(V/V₀)` → `t = −RC·ln(V/V₀) = RC·ln(V₀/V)`.",
            "(De ahí `R = t/(C·ln(V₀/V))` y `C = t/(R·ln(V₀/V))`.) El signo menos se absorbe invirtiendo el cociente: `−ln(a/b) = ln(b/a)`.",
        ],
    ),
    _p(
        "tp6-26-27", MOD, 2, "Matemática · TP6, ej. 26 y 27",
        "Yodo radiactivo y bacterias",
        "Ej. 26) El yodo radiactivo que se usa como trazador se desintegra de modo que la masa restante (en gramos) después de `t` días es `m(t) = 6·e^(−0,087t)`. ¿Cuánto tiempo debe transcurrir para que la masa sea 3 gramos?\n\n"
        "Ej. 27) Una bacteria del oído medio se incrementa a razón del 2 % por hora. Si al inicio de la infección había 120 bacterias, la cantidad al cabo de `t` horas es `N(t) = 120·e^(0,02t)`. ¿Cuánto tiempo debe transcurrir para que la cantidad de bacterias se duplique?",
        [
            _n("Ej. 26) ¿Cuántos días? Redondeá a 2 decimales.", 7.97, "7,97 días", 0.01, "días"),
            _n("Ej. 27) ¿Cuántas horas? Redondeá a 2 decimales.", 34.66, "34,66 horas", 0.01, "h"),
        ],
        [
            "Igualá la función al valor pedido, dividí por el valor inicial y aplicá `ln`.",
            "En ambos casos aparece `ln 2` (o `ln ½`): la mitad o el doble del valor inicial.",
        ],
        [
            "Ej. 26) `6·e^(−0,087t) = 3` → `e^(−0,087t) = ½` → `−0,087t = ln ½ = −ln 2`.",
            "`t = ln 2/0,087 ≈ 0,693147/0,087 ≈ 7,97` días (es la vida media del yodo).",
            "Ej. 27) `120·e^(0,02t) = 240` → `e^(0,02t) = 2` → `0,02t = ln 2`.",
            "`t = ln 2/0,02 ≈ 34,66` horas (tiempo de duplicación). Observá que no depende de las 120 bacterias iniciales.",
        ],
    ),
]

# ======================================================================
# TP7 · TRIGONOMETRÍA
# ======================================================================
MED = "t-sistemas-medicion"
RECI = "t-reciprocas-referencia"
REL = "t-relaciones-angulos"
IDEN = "t-identidades-angulo-doble"
ECT = "t-ecuaciones-trigonometricas"
CIRCU = "a2-circulo-unitario-ondas"

TP7 = [
    # ---------- Ej. 1 y 2: conversiones ----------
    _p(
        "tp7-1", MED, 1, "Matemática · TP7, ej. 1",
        "De radianes a grados y viceversa",
        "Completá la tabla teniendo en cuenta las equivalencias de los ángulos notables (`30° = π/6`, `45° = π/4`, `60° = π/3`, `90° = π/2`):\n\n"
        "| ° | −210° | … | −120° | 150° | … | … | 330° | … |\n|---|---|---|---|---|---|---|---|---|\n| rad | … | −3π/4 | … | … | 5π/4 | 3π/2 | … | 2π |",
        [
            _n("a) ¿Cuántos grados son `−3π/4`?", -135, "−135°", 0, "°"),
            _n("b) ¿Cuántos grados son `3π/2`?", 270, "270°", 0, "°"),
            _c("c) ¿Cuánto es `−210°` en radianes?", ["−7π/6", "−5π/6", "−7π/4", "−4π/3"], "−7π/6"),
        ],
        [
            "`π rad = 180°`. De radianes a grados: multiplicá por `180°/π`; de grados a radianes: por `π/180°`.",
        ],
        [
            "a) `−3π/4 · 180°/π = −3·45° = −135°`.",
            "b) `3π/2 · 180°/π = 3·90° = 270°`. Además `5π/4 = 225°` y `2π = 360°`.",
            "c) `−210° · π/180° = −21π/18 = −7π/6`.",
            "Resto de la tabla: `−120° = −2π/3`, `150° = 5π/6`, `330° = 11π/6`.",
        ],
    ),
    _p(
        "tp7-2", MED, 1, "Matemática · TP7, ej. 2",
        "Conversiones con fracciones de π",
        "Completá el cuadro expresando los ángulos en radianes (en términos de π) o en grados según corresponda:\n\n"
        "| Grados | 80° | … | … | 160° | 220° | … | 320° | … | 350° | … |\n|---|---|---|---|---|---|---|---|---|---|---|\n"
        "| Radianes | … | 5π/9 | 7π/9 | … | … | 25π/18 | … | 17π/9 | … | 71π/36 |",
        [
            _n("a) ¿Cuántos grados son `25π/18`?", 250, "250°", 0, "°"),
            _n("b) ¿Cuántos grados son `71π/36`?", 355, "355°", 0, "°"),
            _c("c) ¿Cuánto es `220°` en radianes?", ["11π/9", "11π/18", "22π/9", "9π/11"], "11π/9"),
        ],
        [
            "`π/18 = 10°` y `π/36 = 5°`: usalo para convertir rápido.",
            "Para pasar a radianes, simplificá la fracción `grados/180` y multiplicá por π.",
        ],
        [
            "a) `25π/18 = 25·10° = 250°`.",
            "b) `71π/36 = 71·5° = 355°`.",
            "c) `220/180 = 11/9` → `220° = 11π/9`.",
            "Resto: `80° = 4π/9`, `5π/9 = 100°`, `7π/9 = 140°`, `160° = 8π/9`, `320° = 16π/9`, `17π/9 = 340°`, `350° = 35π/18`.",
        ],
    ),
    # ---------- Ej. 4, 5 y 6: razones a partir de una ----------
    _p(
        "tp7-4b", RECI, 1, "Matemática · TP7, ej. 4 b",
        "Razones a partir de la tangente",
        "Determiná las restantes razones trigonométricas sabiendo que `tg α = ¾` y que `α` pertenece al 3° cuadrante. Trabajá con valores exactos.",
        [
            _n("a) ¿Cuánto vale `sen α`? Podés responder con fracción.", -0.6, "−3/5"),
            _n("b) ¿Cuánto vale `cos α`?", -0.8, "−4/5"),
            _n("c) ¿Cuánto vale `cosec α`?", -5 / 3, "−5/3", 0.002),
        ],
        [
            "Usá `1 + tg²α = sec²α`, o dibujá un triángulo de catetos 3 y 4.",
            "En el 3° cuadrante seno y coseno son negativos; la tangente, positiva.",
        ],
        [
            "`sec²α = 1 + 9/16 = 25/16` → `|sec α| = 5/4`. En el 3° cuadrante `cos α < 0`, así que `sec α = −5/4` y `cos α = −4/5`.",
            "`sen α = tg α · cos α = ¾·(−4/5) = −3/5`.",
            "Recíprocas: `cosec α = −5/3`, `sec α = −5/4`, `cotg α = 4/3`.",
            "Control: `(−3/5)² + (−4/5)² = 9/25 + 16/25 = 1` ✓.",
        ],
    ),
    _p(
        "tp7-4d", RECI, 2, "Matemática · TP7, ej. 4 d",
        "Razones a partir de la cotangente",
        "Determiná las restantes razones trigonométricas sabiendo que `cotg α = −¼` y que `α` pertenece al 2° cuadrante. Trabajá con valores exactos.",
        [
            _n("a) ¿Cuánto vale `tg α`?", -4, "−4"),
            _c("b) ¿Cuánto vale `sec α`?", ["−√17", "√17", "−√17/4", "−17"], "−√17"),
            _c("c) ¿Cuánto vale `sen α`?", ["4√17/17", "−4√17/17", "√17/17", "4/17"], "4√17/17"),
        ],
        [
            "`tg α = 1/cotg α` y `1 + tg²α = sec²α`.",
            "En el 2° cuadrante el seno es positivo y el coseno negativo.",
        ],
        [
            "`tg α = 1/(−¼) = −4`.",
            "`sec²α = 1 + 16 = 17` → en el 2° cuadrante `cos α < 0`, así que `sec α = −√17` y `cos α = −1/√17 = −√17/17`.",
            "`sen α = tg α · cos α = (−4)(−√17/17) = 4√17/17` (positivo ✓).",
            "`cosec α = √17/4`. Control: `16/17 + 1/17 = 1` ✓.",
        ],
    ),
    _p(
        "tp7-5", RECI, 2, "Matemática · TP7, ej. 5 c, f",
        "Razones a partir de una razón y un signo",
        "Sin calcular el valor de `α`, encontrá sus razones trigonométricas con la información dada:\n\n"
        "c) `sen α = −⅓` y `cos α < 0`.\n\nf) `cotg α = −½` y `0° < α < 270°`.",
        [
            _c("c) ¿Cuánto vale `cos α`?", ["−2√2/3", "2√2/3", "−√2/3", "−8/9"], "−2√2/3"),
            _n("c) ¿Cuánto vale `cosec α`?", -3, "−3"),
            _c("f) ¿Cuánto vale `sen α`?", ["2√5/5", "−2√5/5", "√5/5", "2/5"], "2√5/5"),
        ],
        [
            "Primero ubicá el cuadrante con los signos dados.",
            "f) La cotangente es negativa en el 2° y 4° cuadrante; la condición `0° < α < 270°` deja uno solo.",
        ],
        [
            "c) Seno y coseno negativos: 3° cuadrante. `cos²α = 1 − 1/9 = 8/9` → `cos α = −√8/3 = −2√2/3`.",
            "c) `cosec α = 1/sen α = −3`; `tg α = (−⅓)/(−2√2/3) = 1/(2√2) = √2/4`; `cotg α = 2√2`; `sec α = −3/(2√2) = −3√2/4`.",
            "f) `cotg α < 0` y `0° < α < 270°`: 2° cuadrante. `tg α = −2`, `sec²α = 1 + 4 = 5` → `sec α = −√5`, `cos α = −√5/5`.",
            "f) `sen α = tg α · cos α = (−2)(−√5/5) = 2√5/5`; `cosec α = √5/2`.",
        ],
    ),
    _p(
        "tp7-6", IDEN, 3, "Matemática · TP7, ej. 6",
        "Calcular expresiones trigonométricas",
        "Sabiendo que:\n\n"
        "a) `sec α = −√2` y `α ∈ 3° cuadrante`, calculá `(4·cotg α + tg α)·(3/2)·sen α`.\n\n"
        "b) `sen α = ⅔` y `cos α < 0`, calculá `√(cotg²α − cos²α)`.\n\n"
        "c) `cos x = −√5/3` y `x ∈ 2° cuadrante`, calculá `(sen²x + 3)·1/tg²x`.",
        [
            _c("a) ¿Cuánto vale la expresión?", ["−15√2/4", "15√2/4", "−5√2/2", "−3√2/4"], "−15√2/4"),
            _n("b) ¿Cuánto vale? Podés responder con fracción.", 5 / 6, "5/6", 0.002),
            _n("c) ¿Cuánto vale? Podés responder con fracción.", 155 / 36, "155/36 (≈ 4,31)", 0.002),
        ],
        [
            "Calculá primero seno, coseno y tangente con la identidad pitagórica y el signo del cuadrante.",
            "En b) y c) trabajá con los cuadrados: el signo de `cotg` o `tg` no importa al elevar al cuadrado.",
        ],
        [
            "a) `cos α = −1/√2 = −√2/2`; en el 3° cuadrante `sen α = −√2/2`, `tg α = 1`, `cotg α = 1`.",
            "a) `(4·1 + 1)·(3/2)·(−√2/2) = 5·(−3√2/4) = −15√2/4`.",
            "b) `cos²α = 1 − 4/9 = 5/9` (`cos α = −√5/3`). `cotg²α = cos²α/sen²α = (5/9)/(4/9) = 5/4`.",
            "b) `cotg²α − cos²α = 5/4 − 5/9 = 45/36 − 20/36 = 25/36` → `√(25/36) = 5/6`.",
            "c) `sen²x = 1 − 5/9 = 4/9`; `tg²x = sen²x/cos²x = (4/9)/(5/9) = 4/5` → `1/tg²x = 5/4`.",
            "c) `(4/9 + 3)·5/4 = (31/9)·(5/4) = 155/36`.",
        ],
    ),
    # ---------- Ej. 7: reducción ----------
    _p(
        "tp7-7-a", REL, 2, "Matemática · TP7, ej. 7 a, d, e",
        "Reducir al primer cuadrante (I)",
        "Expresá en función de `α` y simplificá:\n\n"
        "a) `sen(π − α) + cos(90° − α)`\n\nd) `2·tg(−α) + 2·tg(π − α)`\n\ne) `sen(180° + α) − cos(90° + α) − tg(180° − α)`",
        [
            _c("a) ¿A qué es igual?", ["2·sen α", "0", "sen α + cos α", "2·cos α"], "2·sen α"),
            _c("d) ¿A qué es igual?", ["−4·tg α", "0", "4·tg α", "−2·tg α"], "−4·tg α"),
            _c("e) ¿A qué es igual?", ["tg α", "−2·sen α − tg α", "−tg α", "2·sen α + tg α"], "tg α"),
        ],
        [
            "Suplementarios (`π − α`): mismo seno, coseno y tangente opuestos. Complementarios (`90° − α`): seno y coseno se intercambian.",
            "Opuestos (`−α`): el coseno se mantiene, seno y tangente cambian de signo. `180° + α`: seno y coseno cambian de signo, la tangente se mantiene.",
            "`cos(90° + α) = −sen α`.",
        ],
        [
            "a) `sen(π − α) = sen α` y `cos(90° − α) = sen α`: suma `2·sen α`.",
            "d) `tg(−α) = −tg α` y `tg(π − α) = −tg α`: `2(−tg α) + 2(−tg α) = −4·tg α`.",
            "e) `sen(180° + α) = −sen α`; `cos(90° + α) = −sen α`; `tg(180° − α) = −tg α`.",
            "e) `−sen α − (−sen α) − (−tg α) = −sen α + sen α + tg α = tg α`.",
            "Podés controlar con un valor, por ejemplo `α = 30°`: en e) `sen 210° − cos 120° − tg 150° = −½ + ½ + √3/3 = tg 30°` ✓.",
        ],
    ),
    _p(
        "tp7-7-b", REL, 3, "Matemática · TP7, ej. 7 f, h, i",
        "Reducir al primer cuadrante (II)",
        "Expresá en función de `α` y simplificá:\n\n"
        "f) `cos(90° + α)·sen(180° − α) + cos(−α)·cos(180° + α) − sen(−α)`\n\n"
        "h) `−sen(π + α)·cos(π/2 − α) − sen(π/2 + α)·cos(π − α) − sen²(−α)`\n\n"
        "i) `sen(π + α)·cos(π/2 + α) − sen(π/2 − α)·cos(π − α) − cos²(−α)`",
        [
            _c("f) ¿A qué es igual?", ["sen α − 1", "1 + sen α", "−sen α − 1", "sen²α − cos²α + sen α"], "sen α − 1"),
            _c("h) ¿A qué es igual?", ["cos²α", "sen²α", "1", "cos²α − 2·sen²α"], "cos²α"),
            _c("i) ¿A qué es igual?", ["sen²α", "cos²α", "−sen²α", "1"], "sen²α"),
        ],
        [
            "Reducí cada factor por separado antes de multiplicar.",
            "Al final vas a usar `sen²α + cos²α = 1`.",
        ],
        [
            "f) `cos(90° + α) = −sen α`, `sen(180° − α) = sen α`, `cos(−α) = cos α`, `cos(180° + α) = −cos α`, `sen(−α) = −sen α`.",
            "f) `(−sen α)(sen α) + (cos α)(−cos α) + sen α = −(sen²α + cos²α) + sen α = sen α − 1`.",
            "h) `−(−sen α)(sen α) − (cos α)(−cos α) − sen²α = sen²α + cos²α − sen²α = cos²α`.",
            "i) `sen(π + α) = −sen α`, `cos(π/2 + α) = −sen α`, `sen(π/2 − α) = cos α`, `cos(π − α) = −cos α`.",
            "i) `(−sen α)(−sen α) − (cos α)(−cos α) − cos²α = sen²α + cos²α − cos²α = sen²α`.",
        ],
    ),
    # ---------- Ej. 10: verdadero o falso ----------
    _p(
        "tp7-10-signos", CIRCU, 1, "Matemática · TP7, ej. 10 b, d, f",
        "Signos de las razones por cuadrante",
        "Indicá si los siguientes enunciados son verdaderos o falsos:\n\n"
        "b) En el segundo cuadrante, la cosecante y la secante tienen signos opuestos.\n\n"
        "d) Si el seno de un ángulo es positivo, necesariamente su coseno también es positivo.\n\n"
        "f) Las razones trigonométricas recíprocas pueden tener distinto signo en algunos cuadrantes.",
        [
            _c("b) ¿Es verdadero o falso?", ["Verdadero", "Falso: en el 2° cuadrante ambas son negativas", "Falso: en el 2° cuadrante ambas son positivas"], "Verdadero"),
            _c("d) ¿Es verdadero o falso?", ["Falso: en el 2° cuadrante el seno es positivo y el coseno negativo", "Verdadero", "Falso: el seno positivo obliga a que el coseno sea negativo"],
               "Falso: en el 2° cuadrante el seno es positivo y el coseno negativo"),
            _c("f) ¿Es verdadero o falso?", ["Falso: una razón y su recíproca siempre tienen el mismo signo", "Verdadero: en el 2° cuadrante seno y cosecante tienen distinto signo", "Verdadero: en el 4° cuadrante coseno y secante tienen distinto signo"],
               "Falso: una razón y su recíproca siempre tienen el mismo signo"),
        ],
        [
            "En el 2° cuadrante: x negativo, y positivo. Seno ~ y, coseno ~ x.",
            "`1/a` tiene siempre el mismo signo que `a`.",
        ],
        [
            "b) En el 2° cuadrante `sen α > 0`, entonces `cosec α > 0`; `cos α < 0`, entonces `sec α < 0`. Signos opuestos: verdadero.",
            "d) Falso: por ejemplo `α = 120°`, `sen 120° = √3/2 > 0` pero `cos 120° = −½ < 0`.",
            "f) Falso: la cosecante es `1/sen`, la secante `1/cos` y la cotangente `1/tg`; un número y su inverso tienen siempre el mismo signo.",
            "Resumen de signos: 1° todas positivas; 2° solo seno y cosecante; 3° solo tangente y cotangente; 4° solo coseno y secante.",
        ],
    ),
    _p(
        "tp7-10-relaciones", REL, 2, "Matemática · TP7, ej. 10 h, i, j",
        "Relaciones entre ángulos: verdadero o falso",
        "Indicá si los siguientes enunciados son verdaderos o falsos:\n\n"
        "h) El coseno de dos ángulos opuestos tiene valores opuestos.\n\n"
        "i) Dos ángulos que difieren en π tienen el mismo seno y el mismo coseno.\n\n"
        "j) La tangente de un ángulo es igual a la cotangente de su complemento.",
        [
            _c("h) ¿Es verdadero o falso?", ["Falso: cos(−α) = cos α, son iguales", "Verdadero", "Falso: cos(−α) = sen α"], "Falso: cos(−α) = cos α, son iguales"),
            _c("i) ¿Es verdadero o falso?", ["Falso: sen(α + π) = −sen α y cos(α + π) = −cos α", "Verdadero", "Falso: tienen igual seno pero coseno opuesto"], "Falso: sen(α + π) = −sen α y cos(α + π) = −cos α"),
            _c("j) ¿Es verdadero o falso?", ["Verdadero", "Falso: tg α = −cotg(90° − α)", "Falso: tg α = tg(90° − α)"], "Verdadero"),
        ],
        [
            "Pensá en el círculo trigonométrico: `−α` es el simétrico respecto del eje x; `α + π`, el simétrico respecto del origen.",
        ],
        [
            "h) `−α` tiene la misma abscisa que `α`: `cos(−α) = cos α` (iguales, no opuestos). Falso. Lo que cambia de signo es el seno.",
            "i) `α + π` es el punto diametralmente opuesto: cambian de signo seno y coseno (la tangente se mantiene). Falso. Ejemplo: `sen 30° = ½`, `sen 210° = −½`.",
            "j) `cotg(90° − α) = cos(90° − α)/sen(90° − α) = sen α/cos α = tg α`. Verdadero.",
        ],
    ),
    # ---------- Ej. 12 y 13: ecuaciones trigonométricas ----------
    _p(
        "tp7-12-a", ECT, 1, "Matemática · TP7, ej. 12 b, f, g",
        "Ecuaciones trigonométricas elementales (I)",
        "Calculá los valores de `x ∈ [0; 2π)` que verifican las siguientes ecuaciones. Expresá los ángulos en grados y en radianes:\n\n"
        "b) `csc x = −2`\n\nf) `cotg x = −√3`\n\ng) `√3·ctg x + 1 = 0`",
        [
            _c("b) ¿Cuáles son las soluciones?", ["210° = 7π/6 y 330° = 11π/6", "30° = π/6 y 150° = 5π/6", "240° = 4π/3 y 300° = 5π/3", "150° = 5π/6 y 210° = 7π/6"], "210° = 7π/6 y 330° = 11π/6"),
            _c("f) ¿Cuáles son las soluciones?", ["150° = 5π/6 y 330° = 11π/6", "120° = 2π/3 y 300° = 5π/3", "30° = π/6 y 210° = 7π/6", "150° = 5π/6 y 210° = 7π/6"], "150° = 5π/6 y 330° = 11π/6"),
            _c("g) ¿Cuáles son las soluciones?", ["120° = 2π/3 y 300° = 5π/3", "150° = 5π/6 y 330° = 11π/6", "60° = π/3 y 240° = 4π/3", "120° = 2π/3 y 240° = 4π/3"], "120° = 2π/3 y 300° = 5π/3"),
        ],
        [
            "Pasá a seno o tangente: `csc x = 1/sen x`, `cotg x = 1/tg x`.",
            "Buscá el ángulo de referencia en el 1° cuadrante y ubicá los cuadrantes según el signo.",
            "La tangente tiene período π: las dos soluciones en una vuelta difieren en 180°.",
        ],
        [
            "b) `sen x = −½`. Referencia 30°; seno negativo en 3° y 4° cuadrante: `x = 180° + 30° = 210° = 7π/6` y `x = 360° − 30° = 330° = 11π/6`.",
            "f) `tg x = −1/√3 = −√3/3`. Referencia 30°; tangente negativa en 2° y 4°: `x = 150° = 5π/6` y `x = 330° = 11π/6`.",
            "g) `ctg x = −1/√3` → `tg x = −√3`. Referencia 60°; 2° y 4° cuadrante: `x = 120° = 2π/3` y `x = 300° = 5π/3`.",
            "Error típico: confundir `tg x = −√3` (referencia 60°) con `tg x = −√3/3` (referencia 30°).",
        ],
    ),
    _p(
        "tp7-12-b", ECT, 1, "Matemática · TP7, ej. 12 i, m, n",
        "Ecuaciones trigonométricas elementales (II)",
        "Calculá los valores de `x ∈ [0; 2π)` que verifican las siguientes ecuaciones. Expresá los ángulos en grados y en radianes:\n\n"
        "i) `2·tg x + 2 = 0`\n\nm) `sec x + √2 = 0`\n\nn) `−2·sen x + √3 = 0`",
        [
            _c("i) ¿Cuáles son las soluciones?", ["135° = 3π/4 y 315° = 7π/4", "45° = π/4 y 225° = 5π/4", "135° = 3π/4 y 225° = 5π/4", "225° = 5π/4 y 315° = 7π/4"], "135° = 3π/4 y 315° = 7π/4"),
            _c("m) ¿Cuáles son las soluciones?", ["135° = 3π/4 y 225° = 5π/4", "45° = π/4 y 315° = 7π/4", "135° = 3π/4 y 315° = 7π/4", "225° = 5π/4 y 315° = 7π/4"], "135° = 3π/4 y 225° = 5π/4"),
            _c("n) ¿Cuáles son las soluciones?", ["60° = π/3 y 120° = 2π/3", "30° = π/6 y 150° = 5π/6", "60° = π/3 y 300° = 5π/3", "240° = 4π/3 y 300° = 5π/3"], "60° = π/3 y 120° = 2π/3"),
        ],
        [
            "Despejá la razón y pasá la secante a coseno: `sec x = 1/cos x`.",
            "Ubicá los cuadrantes según el signo del valor obtenido.",
        ],
        [
            "i) `tg x = −1`. Referencia 45°; 2° y 4° cuadrante: `x = 135° = 3π/4` y `x = 315° = 7π/4`.",
            "m) `sec x = −√2` → `cos x = −1/√2 = −√2/2`. Referencia 45°; coseno negativo en 2° y 3°: `x = 135° = 3π/4` y `x = 225° = 5π/4`.",
            "n) `sen x = √3/2`. Referencia 60°; seno positivo en 1° y 2°: `x = 60° = π/3` y `x = 120° = 2π/3`.",
            "Control de m): `cos 135° = −√2/2`, entonces `sec 135° = −2/√2 = −√2` ✓.",
        ],
    ),
    _p(
        "tp7-13-a", ECT, 2, "Matemática · TP7, ej. 13 a, b, c",
        "Ecuaciones con cuadrados: cuatro soluciones",
        "Calculá los valores de `x ∈ [0; 2π)` que verifican las siguientes ecuaciones. Expresá los ángulos en grados y en radianes:\n\n"
        "a) `9·tg²x − 3 = 0`\n\nb) `4·sen²x − 3 = 0`\n\nc) `2·cos²x − 1 = 0`",
        [
            _c("a) ¿Cuáles son las soluciones?", ["30°, 150°, 210° y 330° (π/6, 5π/6, 7π/6, 11π/6)", "30° y 210° (π/6, 7π/6)",
                                                 "60°, 120°, 240° y 300° (π/3, 2π/3, 4π/3, 5π/3)", "30° y 150° (π/6, 5π/6)"],
               "30°, 150°, 210° y 330° (π/6, 5π/6, 7π/6, 11π/6)"),
            _c("b) ¿Cuáles son las soluciones?", ["60°, 120°, 240° y 300° (π/3, 2π/3, 4π/3, 5π/3)", "60° y 120° (π/3, 2π/3)",
                                                 "30°, 150°, 210° y 330° (π/6, 5π/6, 7π/6, 11π/6)", "60° y 240° (π/3, 4π/3)"],
               "60°, 120°, 240° y 300° (π/3, 2π/3, 4π/3, 5π/3)"),
            _c("c) ¿Cuáles son las soluciones?", ["45°, 135°, 225° y 315° (π/4, 3π/4, 5π/4, 7π/4)", "45° y 315° (π/4, 7π/4)",
                                                 "45° y 225° (π/4, 5π/4)", "30°, 150°, 210° y 330° (π/6, 5π/6, 7π/6, 11π/6)"],
               "45°, 135°, 225° y 315° (π/4, 3π/4, 5π/4, 7π/4)"),
        ],
        [
            "Al sacar raíz cuadrada aparecen dos valores: `+` y `−`.",
            "Cada valor da dos ángulos en una vuelta: en total, cuatro.",
        ],
        [
            "a) `tg²x = 1/3` → `tg x = ±√3/3`. Referencia 30°. Positiva: 30° y 210°; negativa: 150° y 330°.",
            "b) `sen²x = 3/4` → `sen x = ±√3/2`. Referencia 60°. Positivo: 60° y 120°; negativo: 240° y 300°.",
            "c) `cos²x = ½` → `cos x = ±√2/2`. Referencia 45°. Positivo: 45° y 315°; negativo: 135° y 225°.",
            "En radianes: `30° = π/6`, `150° = 5π/6`, `210° = 7π/6`, `330° = 11π/6`; `60° = π/3`, `120° = 2π/3`, `240° = 4π/3`, `300° = 5π/3`; `45° = π/4`, `135° = 3π/4`, `225° = 5π/4`, `315° = 7π/4`.",
            "Error típico: olvidar la raíz negativa y quedarse con solo dos soluciones.",
        ],
    ),
    _p(
        "tp7-13-b", ECT, 2, "Matemática · TP7, ej. 13 e, g, h",
        "Ecuaciones trigonométricas factorizables y cuadráticas",
        "Calculá los valores de `x ∈ [0; 2π)` que verifican las siguientes ecuaciones. Expresá los ángulos en grados y en radianes:\n\n"
        "e) `2·cos²x − cos x = 0`\n\ng) `2·cos²x + cos x − 1 = 0`\n\nh) `2·sen²x − 5·sen x + 3 = 0`",
        [
            _c("e) ¿Cuáles son las soluciones?", ["60°, 90°, 270° y 300° (π/3, π/2, 3π/2, 5π/3)", "60° y 300° (π/3, 5π/3)",
                                                 "60°, 90°, 120° y 270° (π/3, π/2, 2π/3, 3π/2)", "0°, 60° y 300° (0, π/3, 5π/3)"],
               "60°, 90°, 270° y 300° (π/3, π/2, 3π/2, 5π/3)"),
            _c("g) ¿Cuáles son las soluciones?", ["60°, 180° y 300° (π/3, π, 5π/3)", "60° y 300° (π/3, 5π/3)", "0°, 120° y 240° (0, 2π/3, 4π/3)", "30°, 180° y 330° (π/6, π, 11π/6)"],
               "60°, 180° y 300° (π/3, π, 5π/3)"),
            _c("h) ¿Cuáles son las soluciones?", ["90° (π/2)", "90° y 270° (π/2, 3π/2)", "30°, 90° y 150° (π/6, π/2, 5π/6)", "No tiene solución"], "90° (π/2)"),
        ],
        [
            "e) Sacá factor común `cos x`; no dividas por `cos x` porque perdés soluciones.",
            "g) y h) Llamá `t = cos x` o `t = sen x`, resolvé la cuadrática y descartá los valores fuera de `[−1; 1]`.",
        ],
        [
            "e) `cos x·(2cos x − 1) = 0` → `cos x = 0` (90° y 270°) o `cos x = ½` (60° y 300°).",
            "g) `2t² + t − 1 = 0` → `t = (−1 ± 3)/4` → `t = ½` o `t = −1`.",
            "g) `cos x = ½` → 60° y 300°; `cos x = −1` → 180°. Soluciones: `π/3`, `π`, `5π/3`.",
            "h) `2t² − 5t + 3 = 0` → `t = (5 ± 1)/4` → `t = 3/2` o `t = 1`. `sen x = 3/2` es imposible (`|sen x| ≤ 1`).",
            "h) `sen x = 1` → `x = 90° = π/2`, única solución.",
        ],
    ),
    _p(
        "tp7-13-c", ECT, 3, "Matemática · TP7, ej. 13 d, i, l",
        "Ecuaciones trigonométricas con trampas",
        "Calculá los valores de `x ∈ [0; 2π)` que verifican las siguientes ecuaciones. Expresá los ángulos en grados y en radianes (si hace falta, aproximá a dos decimales):\n\n"
        "d) `tan²x − √3·tan x = 0`\n\ni) `tan²x − tan x − 2 = 0`\n\nl) `sen x·(cosec x + 2) = 0`",
        [
            _c("d) ¿Cuáles son las soluciones?", ["0°, 60°, 180° y 240° (0, π/3, π, 4π/3)", "60° y 240° (π/3, 4π/3)",
                                                 "0°, 60°, 120° y 180° (0, π/3, 2π/3, π)", "0°, 30°, 180° y 210° (0, π/6, π, 7π/6)"],
               "0°, 60°, 180° y 240° (0, π/3, π, 4π/3)"),
            _c("i) ¿Cuáles son las soluciones?", ["63,43°, 135°, 243,43° y 315° (≈ 1,11; 3π/4; ≈ 4,25; 7π/4)", "45°, 63,43°, 225° y 243,43° (π/4; ≈ 1,11; 5π/4; ≈ 4,25)",
                                                 "135° y 315° (3π/4, 7π/4)", "45°, 116,57°, 225° y 296,57° (π/4; ≈ 2,03; 5π/4; ≈ 5,18)"],
               "63,43°, 135°, 243,43° y 315° (≈ 1,11; 3π/4; ≈ 4,25; 7π/4)"),
            _c("l) ¿Cuáles son las soluciones?", ["210° y 330° (7π/6, 11π/6)", "0°, 180°, 210° y 330° (0, π, 7π/6, 11π/6)", "30° y 150° (π/6, 5π/6)", "0° y 180° (0, π)"],
               "210° y 330° (7π/6, 11π/6)"),
        ],
        [
            "d) Sacá factor común `tan x`.",
            "i) Con `t = tan x` queda `t² − t − 2 = 0`. El valor que no es notable se obtiene con la calculadora (`tan⁻¹`).",
            "l) ¿Qué pasa con `cosec x` cuando `sen x = 0`?",
        ],
        [
            "d) `tan x·(tan x − √3) = 0` → `tan x = 0` (0° y 180°) o `tan x = √3` (60° y 240°).",
            "i) `t² − t − 2 = (t − 2)(t + 1) = 0` → `tan x = 2` o `tan x = −1`.",
            "i) `tan x = −1` → 135° y 315°. `tan x = 2` → `x = tan⁻¹ 2 ≈ 63,43°` (≈ 1,11 rad) y `63,43° + 180° = 243,43°` (≈ 4,25 rad).",
            "l) Si `sen x = 0`, `cosec x = 1/sen x` no existe: esos valores (0° y 180°) NO son solución.",
            "l) Queda `cosec x = −2` → `sen x = −½` → `x = 210° = 7π/6` y `x = 330° = 11π/6`. (Otra forma: `sen x·cosec x = 1`, así que la ecuación es `1 + 2 sen x = 0`.)",
        ],
    ),
]

EXERCISES: list[dict] = TP4 + TP5 + TP6 + TP7
