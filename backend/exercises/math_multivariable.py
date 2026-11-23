"""Ejercicios de Matemática: Cálculo multivariable (Análisis Matemático II, temas 92-99).

Tres problemas por tema (niveles 1, 2 y 3). Los de nivel 3 apuntan a la dificultad de un parcial
de Análisis II. Todos los resultados se recalcularon con integración y derivación numérica en Python.
"""

from __future__ import annotations

EXERCISES: list[dict] = [
    # ==================== mv-espacio-superficies ====================
    {
        "id": "mv-espacio-superficies-1",
        "node": "mv-espacio-superficies",
        "kind": "problem",
        "level": 1,
        "title": "El mapa topográfico de un cerro",
        "statement": (
            "La altura de un cerro de las Sierras de Córdoba se modela con `z = f(x, y) = 100 − x² − 4y²`, "
            "con `z` en metros sobre la base y `x`, `y` en hectómetros (hm) medidos desde la cima "
            "(`x` hacia el este, `y` hacia el norte).\n\n"
            "Un guardaparque dibuja el mapa de curvas de nivel del cerro, entre ellas las de `z = 64` y `z = 36`."
        ),
        "parts": [
            {
                "prompt": "a) ¿A qué altura está el punto del cerro ubicado en (x, y) = (4, 3)? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 48, "tolerance": 0, "unit": "m"},
                "answer": "48 m (100 − 16 − 36)",
            },
            {
                "prompt": "b) ¿Qué forma tiene la curva de nivel z = 64?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Una elipse centrada en el origen, con semieje 6 sobre el eje x y semieje 3 sobre el eje y",
                        "Una circunferencia de radio 6 centrada en el origen",
                        "Una elipse centrada en el origen, con semieje 3 sobre el eje x y semieje 6 sobre el eje y",
                        "Una elipse centrada en el origen, con semieje 36 sobre el eje x y semieje 9 sobre el eje y",
                    ],
                    "correct": 0,
                },
                "answer": "Una elipse centrada en el origen, con semieje 6 sobre el eje x y semieje 3 sobre el eje y",
            },
            {
                "prompt": "c) Saliendo de la zona de la cima, ¿en qué dirección baja más rápido el cerro entre las curvas z = 64 y z = 36?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Hacia el norte o el sur (eje y): ahí las dos curvas están a 1 hm, contra 2 hm sobre el eje x",
                        "Hacia el este o el oeste (eje x): ahí las dos curvas están más separadas",
                        "Baja igual en todas las direcciones, porque las curvas de nivel son cerradas",
                        "Hacia el este o el oeste (eje x), porque la elipse es más larga en esa dirección",
                    ],
                    "correct": 0,
                },
                "answer": "Hacia el norte o el sur (eje y): ahí las dos curvas están a 1 hm, contra 2 hm sobre el eje x",
            },
        ],
        "hints": [
            "Una curva de nivel se obtiene igualando `f(x, y)` a la altura fija: `100 − x² − 4y² = 64`.",
            "Llevá la ecuación a la forma `x²/a² + y²/b² = 1` y leé los semiejes. Repetí con `z = 36` y compará las distancias entre curvas sobre cada eje.",
        ],
        "solution": [
            "a) `f(4, 3) = 100 − 4² − 4·3² = 100 − 16 − 36 = 48` m.",
            "b) `z = 64`: `100 − x² − 4y² = 64` → `x² + 4y² = 36` → dividiendo por 36: `x²/36 + y²/9 = 1`. Es una elipse con semiejes `√36 = 6` (sobre x) y `√9 = 3` (sobre y).",
            "c) `z = 36`: `x² + 4y² = 64` → `x²/64 + y²/16 = 1`, elipse con semiejes 8 (sobre x) y 4 (sobre y).",
            "Sobre el eje x las curvas cortan en 6 y 8 hm: para bajar 28 m hay que avanzar 2 hm. Sobre el eje y cortan en 3 y 4 hm: se bajan los mismos 28 m en solo 1 hm.",
            "Curvas más juntas = pendiente más empinada, así que el cerro es más empinado hacia el norte y el sur.",
            "Error típico: olvidar la raíz y tomar 36 y 9 como semiejes, o pensar que la curva que «llega más lejos» es la más empinada (es al revés).",
        ],
    },
    {
        "id": "mv-espacio-superficies-2",
        "node": "mv-espacio-superficies",
        "kind": "problem",
        "level": 2,
        "title": "Una chapa triangular en el espacio",
        "statement": (
            "Para una escultura en un parque de Rosario se corta una chapa triangular plana cuyos vértices, "
            "en metros, son `A(1, 0, 0)`, `B(0, 2, 0)` y `C(0, 0, 3)` (el piso es el plano `z = 0`).\n\n"
            "Usá los vectores `AB` y `AC`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale el producto cruz AB × AC?",
                "check": {
                    "type": "choice",
                    "options": ["⟨6, 3, 2⟩", "⟨−6, −3, −2⟩", "⟨6, −3, 2⟩", "⟨2, 3, 6⟩"],
                    "correct": 0,
                },
                "answer": "⟨6, 3, 2⟩",
            },
            {
                "prompt": "b) ¿Cuál es el área de la chapa? Respondé solo con el número en m².",
                "check": {"type": "numeric", "value": 3.5, "tolerance": 0, "unit": "m²"},
                "answer": "3.5 m² (la mitad de |AB × AC| = 7)",
            },
            {
                "prompt": "c) Un hilo vertical sube desde el punto (0.5, 0.5, 0) del piso hasta tocar la chapa. ¿A qué altura la toca? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 0.75, "tolerance": 0, "unit": "m"},
                "answer": "0.75 m (plano 6x + 3y + 2z = 6)",
            },
        ],
        "hints": [
            "`AB = B − A` y `AC = C − A`. El producto cruz da un vector normal a la chapa y su módulo es el área del paralelogramo.",
            "El triángulo es la mitad del paralelogramo. Con el normal `⟨a, b, c⟩` y el punto A armá el plano `ax + by + cz = d` y despejá z con x = y = 0.5.",
        ],
        "solution": [
            "`AB = ⟨−1, 2, 0⟩`, `AC = ⟨−1, 0, 3⟩`.",
            "`AB × AC = ⟨2·3 − 0·0, 0·(−1) − (−1)·3, (−1)·0 − 2·(−1)⟩ = ⟨6, 3, 2⟩`. (Ojo con la componente del medio: es `u₃v₁ − u₁v₃`.)",
            "`|AB × AC| = √(36 + 9 + 4) = √49 = 7`, que es el área del paralelogramo; el triángulo mide la mitad: `7/2 = 3.5` m².",
            "Plano de la chapa con normal `⟨6, 3, 2⟩` por `A(1, 0, 0)`: `6(x − 1) + 3y + 2z = 0` → `6x + 3y + 2z = 6`. Verificación: B da `6` y C da `6`. ✓",
            "c) Con `x = y = 0.5`: `3 + 1.5 + 2z = 6` → `2z = 1.5` → `z = 0.75` m. El punto está sobre la chapa porque `(0.5, 0.5)` cae dentro del triángulo proyectado (`x + y/2 = 0.75 ≤ 1`).",
            "Error típico: calcular `AC × AB`, que da `⟨−6, −3, −2⟩` (sentido opuesto), o olvidarse de dividir por 2 el área.",
        ],
    },
    {
        "id": "mv-espacio-superficies-3",
        "node": "mv-espacio-superficies",
        "kind": "problem",
        "level": 3,
        "title": "Recta intersección de dos planos y plano que la contiene",
        "statement": (
            "Los planos `π₁: x + y + z = 6` y `π₂: 2x − y + z = 3` se cortan en una recta `L`.\n\n"
            "Se busca además el plano `π₃` que contiene a la recta `L` y al punto `Q(1, 0, 0)`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál de estos vectores es un vector director de L?",
                "check": {
                    "type": "choice",
                    "options": ["⟨2, 1, −3⟩", "⟨2, −1, −3⟩", "⟨3, 0, 2⟩", "⟨1, 1, 1⟩"],
                    "correct": 0,
                },
                "answer": "⟨2, 1, −3⟩ (n₁ × n₂)",
            },
            {
                "prompt": "b) L corta al plano z = 0 en un punto P₀. ¿Cuánto vale la coordenada x de P₀? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3 (P₀ = (3, 3, 0))",
            },
            {
                "prompt": "c) ¿En qué valor de z corta el plano π₃ al eje z? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2.25, "tolerance": 0, "unit": ""},
                "answer": "2.25 (π₃: 9x − 6y + 4z = 9)",
            },
        ],
        "hints": [
            "La recta está en los dos planos, así que su dirección es perpendicular a ambas normales: usá el producto cruz `n₁ × n₂`.",
            "Para un punto de L, poné `z = 0` y resolvé el sistema 2×2 en x e y.",
            "El normal de π₃ es perpendicular a la dirección de L y al vector `P₀Q`: otro producto cruz.",
        ],
        "solution": [
            "Normales: `n₁ = ⟨1, 1, 1⟩`, `n₂ = ⟨2, −1, 1⟩`. Dirección de L: `d = n₁ × n₂ = ⟨1·1 − 1·(−1), 1·2 − 1·1, 1·(−1) − 1·2⟩ = ⟨2, 1, −3⟩`. Verificación: `d · n₁ = 0` y `d · n₂ = 4 − 1 − 3 = 0`.",
            "b) Con `z = 0`: `x + y = 6` y `2x − y = 3`. Sumando: `3x = 9` → `x = 3`, `y = 3`. Entonces `P₀ = (3, 3, 0)` y `L: (3, 3, 0) + t⟨2, 1, −3⟩`.",
            "c) `P₀Q = Q − P₀ = ⟨−2, −3, 0⟩`. Normal de π₃: `N = d × P₀Q = ⟨1·0 − (−3)(−3), (−3)(−2) − 2·0, 2·(−3) − 1·(−2)⟩ = ⟨−9, 6, −4⟩`.",
            "Plano por Q: `−9(x − 1) + 6y − 4z = 0` → `9x − 6y + 4z = 9`. Verificación: P₀ da `27 − 18 = 9` ✓ y el punto de L con t = 1, `(5, 4, −3)`, da `45 − 24 − 12 = 9` ✓.",
            "Corte con el eje z (`x = y = 0`): `4z = 9` → `z = 2.25`.",
            "Otra forma: los planos que contienen a L son `π₁ + k·π₂`; imponer que pase por Q da `k = −5` y el mismo plano. Error típico: equivocar el signo de la componente del medio del producto cruz (sale `⟨2, −1, −3⟩`, que no es perpendicular a n₁).",
        ],
    },
    # ==================== mv-parciales-gradiente ====================
    {
        "id": "mv-parciales-gradiente-1",
        "node": "mv-parciales-gradiente",
        "kind": "problem",
        "level": 1,
        "title": "Gradiente y derivada direccional con un vector sin normalizar",
        "statement": (
            "Sea `f(x, y) = x²y + y³` y el punto `P(1, 2)`.\n\n"
            "Interesa cómo cambia `f` si desde P te movés en la dirección del vector `v = ⟨−4, 3⟩`, "
            "y en qué dirección `f` no cambia."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale ∇f(1, 2)?",
                "check": {
                    "type": "choice",
                    "options": ["⟨4, 13⟩", "⟨4, 12⟩", "⟨13, 4⟩", "⟨2, 13⟩"],
                    "correct": 0,
                },
                "answer": "⟨4, 13⟩",
            },
            {
                "prompt": "b) Calculá la derivada direccional de f en P en la dirección de v. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4.6, "tolerance": 0, "unit": ""},
                "answer": "4.6 (∇f · ⟨−0.8, 0.6⟩)",
            },
            {
                "prompt": "c) ¿En cuál de estas direcciones la derivada direccional de f en P vale 0?",
                "check": {
                    "type": "choice",
                    "options": ["⟨13, −4⟩", "⟨4, 13⟩", "⟨4, −13⟩", "⟨−4, −13⟩"],
                    "correct": 0,
                },
                "answer": "⟨13, −4⟩ (perpendicular al gradiente)",
            },
        ],
        "hints": [
            "Para `f_x` congelá `y`; para `f_y` congelá `x` (ojo: `x²y` también depende de y).",
            "`v` no es unitario: dividilo por `|v| = 5` antes de hacer el producto punto.",
        ],
        "solution": [
            "`f_x = 2xy` → `f_x(1, 2) = 4`. `f_y = x² + 3y²` → `f_y(1, 2) = 1 + 12 = 13`. Entonces `∇f(1, 2) = ⟨4, 13⟩`.",
            "`|v| = √(16 + 9) = 5`, así que `u = v/5 = ⟨−0.8, 0.6⟩`.",
            "`D_u f = ∇f · u = 4·(−0.8) + 13·0.6 = −3.2 + 7.8 = 4.6`.",
            "c) La derivada direccional es 0 cuando `u` es perpendicular a `∇f` (te movés sobre la curva de nivel): `⟨13, −4⟩ · ⟨4, 13⟩ = 52 − 52 = 0`. ✓ (El opuesto `⟨−13, 4⟩` también sirve.)",
            "Error típico: usar `v` sin normalizar, que da `∇f · v = −16 + 39 = 23`, cinco veces el valor correcto.",
        ],
    },
    {
        "id": "mv-parciales-gradiente-2",
        "node": "mv-parciales-gradiente",
        "kind": "problem",
        "level": 2,
        "title": "La temperatura que mide un dron en el campo",
        "statement": (
            "Un dron de relevamiento vuela sobre un campo de la provincia de Buenos Aires. La temperatura del suelo es "
            "`T(x, y) = 20 + x²y − 5y²` (°C), con `x`, `y` en hectómetros (hm).\n\n"
            "La posición del dron proyectada sobre el suelo es `x(t) = t²`, `y(t) = 3 − t`, con `t` en minutos."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué temperatura mide el dron en t = 2 min? Respondé solo con el número en °C.",
                "check": {"type": "numeric", "value": 31, "tolerance": 0, "unit": "°C"},
                "answer": "31 °C (en el punto (4, 1))",
            },
            {
                "prompt": "b) ¿A qué ritmo cambia la temperatura que mide el dron en t = 2 min? Respondé solo con el número en °C/min.",
                "check": {"type": "numeric", "value": 26, "tolerance": 0, "unit": "°C/min"},
                "answer": "26 °C/min",
            },
            {
                "prompt": "c) Si en ese instante el dron pudiera elegir libremente la dirección, ¿cuál es el máximo aumento de temperatura por hectómetro recorrido? Respondé solo con el número en °C/hm.",
                "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "°C/hm"},
                "answer": "10 °C/hm (|∇T(4, 1)|)",
            },
        ],
        "hints": [
            "Primero ubicá al dron: evaluá `x(2)` e `y(2)`.",
            "Regla de la cadena: `dT/dt = T_x·x'(t) + T_y·y'(t)`, todo evaluado en t = 2 y en el punto correspondiente.",
            "La tasa máxima de aumento por unidad de distancia es el módulo del gradiente.",
        ],
        "solution": [
            "En `t = 2`: `x = 4`, `y = 1`. `T(4, 1) = 20 + 16·1 − 5·1 = 31` °C.",
            "Parciales: `T_x = 2xy` → `T_x(4, 1) = 8`; `T_y = x² − 10y` → `T_y(4, 1) = 16 − 10 = 6`. O sea `∇T(4, 1) = ⟨8, 6⟩` °C/hm.",
            "Velocidad: `x'(t) = 2t = 4` hm/min, `y'(t) = −1` hm/min.",
            "b) `dT/dt = 8·4 + 6·(−1) = 32 − 6 = 26` °C/min. Verificación: componiendo, `T(t) = 20 + t⁴(3 − t) − 5(3 − t)²` y derivando en t = 2 se obtiene `4·8·1 − 16 + 10·1 = 26`. ✓",
            "c) La máxima derivada direccional es `|∇T| = √(8² + 6²) = 10` °C/hm, en la dirección `⟨0.8, 0.6⟩`.",
            "Error típico: en b) olvidar el signo de `y'(t) = −1`, que daría 38 °C/min.",
        ],
    },
    {
        "id": "mv-parciales-gradiente-3",
        "node": "mv-parciales-gradiente",
        "kind": "problem",
        "level": 3,
        "title": "Plano tangente, aproximación lineal y pendiente máxima",
        "statement": (
            "Se considera la superficie `S: z = f(x, y) = x²y − y` y el punto de `S` con `(x, y) = (3, 1)`.\n\n"
            "Se pide el plano tangente a S en ese punto, usarlo para aproximar un valor de f cerca, y analizar "
            "la pendiente más empinada de S en ese punto."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la ecuación del plano tangente a S en (3, 1, f(3, 1))?",
                "check": {
                    "type": "choice",
                    "options": [
                        "z = 6x + 8y − 18",
                        "z = 6x + 8y − 10",
                        "z = 8x + 6y − 22",
                        "6x + 8y + z = 34",
                    ],
                    "correct": 0,
                },
                "answer": "z = 6x + 8y − 18",
            },
            {
                "prompt": "b) Usando el plano tangente, aproximá f(3.1, 0.9). Respondé solo con el número.",
                "check": {"type": "numeric", "value": 7.8, "tolerance": 0, "unit": ""},
                "answer": "7.8 (el valor exacto es 7.749)",
            },
            {
                "prompt": "c) ¿Cuál es el valor máximo de la derivada direccional de f en (3, 1)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": ""},
                "answer": "10 (|∇f(3, 1)| = |⟨6, 8⟩|)",
            },
        ],
        "hints": [
            "Plano tangente: `z = f(x₀, y₀) + f_x(x₀, y₀)(x − x₀) + f_y(x₀, y₀)(y − y₀)`.",
            "Para b), evaluá el plano (no f) en (3.1, 0.9): `Δx = 0.1`, `Δy = −0.1`.",
            "La derivada direccional máxima se alcanza en la dirección del gradiente y vale su módulo.",
        ],
        "solution": [
            "`f(3, 1) = 9·1 − 1 = 8`, así que el punto es `(3, 1, 8)`.",
            "`f_x = 2xy` → `f_x(3, 1) = 6`; `f_y = x² − 1` → `f_y(3, 1) = 8`.",
            "Plano tangente: `z = 8 + 6(x − 3) + 8(y − 1) = 6x + 8y − 18 − 8 + 8 = 6x + 8y − 18`. Verificación: en (3, 1) da `18 + 8 − 18 = 8`. ✓",
            "Los distractores: `z = 8x + 6y − 22` intercambia las parciales; `6x + 8y + z = 34` pasa por el punto pero tiene normal `⟨6, 8, 1⟩` en vez de `⟨6, 8, −1⟩`; `z = 6x + 8y − 10` no pasa por (3, 1, 8).",
            "b) `L(3.1, 0.9) = 8 + 6·0.1 + 8·(−0.1) = 8 + 0.6 − 0.8 = 7.8`. El valor real es `f(3.1, 0.9) = 9.61·0.9 − 0.9 = 7.749` (error ≈ 0.05).",
            "c) `∇f(3, 1) = ⟨6, 8⟩`; la derivada direccional máxima es `|∇f| = √(36 + 64) = 10`, en la dirección `u = ⟨0.6, 0.8⟩`.",
        ],
    },
    # ==================== mv-optimizacion-lagrange ====================
    {
        "id": "mv-optimizacion-lagrange-1",
        "node": "mv-optimizacion-lagrange",
        "kind": "problem",
        "level": 1,
        "title": "Hallar y clasificar los puntos críticos",
        "statement": (
            "Sea `f(x, y) = x³ − 3x + y² − 4y`, definida en todo el plano.\n\n"
            "Encontrá todos sus puntos críticos y clasificalos con el criterio del Hessiano."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuántos puntos críticos tiene f? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2: (1, 2) y (−1, 2)",
            },
            {
                "prompt": "b) ¿Cómo se clasifican?",
                "check": {
                    "type": "choice",
                    "options": [
                        "(1, 2) es mínimo local y (−1, 2) es punto silla",
                        "(1, 2) es mínimo local y (−1, 2) es máximo local",
                        "(1, 2) es punto silla y (−1, 2) es mínimo local",
                        "Los dos son mínimos locales porque f_yy = 2 > 0",
                    ],
                    "correct": 0,
                },
                "answer": "(1, 2) es mínimo local y (−1, 2) es punto silla",
            },
            {
                "prompt": "c) ¿Cuál es el valor de f en el mínimo local? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -6, "tolerance": 0, "unit": ""},
                "answer": "−6 (f(1, 2))",
            },
        ],
        "hints": [
            "Igualá `f_x = 3x² − 3` y `f_y = 2y − 4` a cero al mismo tiempo.",
            "Calculá `H = f_xx·f_yy − (f_xy)²` en cada punto crítico: el signo de H decide si es extremo o silla.",
        ],
        "solution": [
            "`f_x = 3x² − 3 = 0` → `x = 1` o `x = −1`. `f_y = 2y − 4 = 0` → `y = 2`. Puntos críticos: `(1, 2)` y `(−1, 2)` → son 2.",
            "Segundas derivadas: `f_xx = 6x`, `f_yy = 2`, `f_xy = 0`, así que `H = 12x`.",
            "En `(1, 2)`: `H = 12 > 0` y `f_xx = 6 > 0` → **mínimo local**.",
            "En `(−1, 2)`: `H = −12 < 0` → **punto silla** (aunque `f_yy > 0`, en la dirección x la función tiene un máximo).",
            "c) `f(1, 2) = 1 − 3 + 4 − 8 = −6`. (En la silla, `f(−1, 2) = −1 + 3 + 4 − 8 = −2`.)",
            "Error típico: clasificar (−1, 2) como máximo mirando solo `f_xx = −6 < 0`, sin calcular H.",
        ],
    },
    {
        "id": "mv-optimizacion-lagrange-2",
        "node": "mv-optimizacion-lagrange",
        "kind": "problem",
        "level": 2,
        "title": "El cantero más grande dentro de una plaza elíptica",
        "statement": (
            "Una plaza de Mendoza tiene forma de elipse de semiejes 40 m y 30 m; con el origen en el centro, su borde es "
            "`x²/1600 + y²/900 = 1`.\n\n"
            "Se quiere armar un cantero rectangular con lados paralelos a los ejes y sus cuatro vértices sobre el borde de la "
            "plaza, de área máxima. Resolvelo con multiplicadores de Lagrange."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto mide el lado del cantero paralelo al eje x? Redondeá a 2 decimales. Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 56.57, "tolerance": 0.01, "unit": "m"},
                "answer": "56.57 m (2x = 40√2)",
            },
            {
                "prompt": "b) ¿Cuál es el área máxima del cantero? Respondé solo con el número en m².",
                "check": {"type": "numeric", "value": 2400, "tolerance": 0, "unit": "m²"},
                "answer": "2400 m²",
            },
        ],
        "hints": [
            "Si `(x, y)` es el vértice del primer cuadrante, el rectángulo mide `2x` por `2y`: maximizá `A = 4xy` con la restricción `g = x²/1600 + y²/900 = 1`.",
            "De `∇A = λ∇g` despejá λ en las dos ecuaciones e igualá: sale una relación entre y y x. Después reemplazá en la restricción.",
        ],
        "solution": [
            "`∇A = ⟨4y, 4x⟩`, `∇g = ⟨2x/1600, 2y/900⟩ = ⟨x/800, y/450⟩`.",
            "`4y = λx/800` y `4x = λy/450` → `λ = 3200y/x = 1800x/y` → `3200y² = 1800x²` → `y² = (9/16)x²` → `y = (3/4)x`.",
            "Restricción: `x²/1600 + (9/16)x²/900 = x²/1600 + x²/1600 = 1` → `x² = 800` → `x = 20√2 ≈ 28.284` m; `y = 15√2 ≈ 21.213` m.",
            "a) Lado paralelo a x: `2x = 40√2 ≈ 56.57` m (el otro lado mide `2y = 30√2 ≈ 42.43` m).",
            "b) `A = 4xy = 4·20√2·15√2 = 4·600 = 2400` m².",
            "Control: el rectángulo óptimo tiene sus vértices en `x = a/√2`, `y = b/√2` y área `2ab = 2·40·30`; ocupa `2/π ≈ 64 %` de la plaza. Error típico: maximizar `xy` y olvidarse de que el rectángulo completo mide `2x × 2y`.",
        ],
    },
    {
        "id": "mv-optimizacion-lagrange-3",
        "node": "mv-optimizacion-lagrange",
        "kind": "problem",
        "level": 3,
        "title": "Extremos absolutos de la temperatura en una placa circular",
        "statement": (
            "Una placa metálica ocupa el disco `D: x² + y² ≤ 4` (x e y en dm). Su temperatura es "
            "`T(x, y) = x² + 2y² − 2x + 3` (°C).\n\n"
            "Hallá los extremos absolutos de T en D: analizá el interior con el Hessiano y el borde "
            "`x² + y² = 4` (con Lagrange o sustituyendo)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué punto crítico tiene T en el interior del disco y cómo se clasifica?",
                "check": {
                    "type": "choice",
                    "options": [
                        "(1, 0), mínimo local con T = 2 °C",
                        "(1, 0), máximo local con T = 2 °C",
                        "(1, 0), punto silla con T = 2 °C",
                        "(−1, 0), mínimo local con T = 6 °C",
                    ],
                    "correct": 0,
                },
                "answer": "(1, 0), mínimo local con T = 2 °C",
            },
            {
                "prompt": "b) ¿Cuál es la temperatura máxima absoluta en la placa? Respondé solo con el número en °C.",
                "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": "°C"},
                "answer": "12 °C, en (−1, ±√3)",
            },
            {
                "prompt": "c) ¿Cuál es la temperatura mínima sobre el BORDE de la placa? Respondé solo con el número en °C.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": "°C"},
                "answer": "3 °C, en (2, 0)",
            },
        ],
        "hints": [
            "Interior: resolvé `T_x = 0`, `T_y = 0` y chequeá que el punto esté dentro del disco.",
            "Borde: con `y² = 4 − x²`, T queda función de una sola variable `x ∈ [−2, 2]`; no te olvides de los extremos del intervalo.",
            "Con Lagrange: `⟨2x − 2, 4y⟩ = λ⟨2x, 2y⟩`; separá los casos `y = 0` y `λ = 2`.",
        ],
        "solution": [
            "Interior: `T_x = 2x − 2 = 0` → `x = 1`; `T_y = 4y = 0` → `y = 0`. `(1, 0)` está en D (`1 < 4`). `T_xx = 2`, `T_yy = 4`, `T_xy = 0` → `H = 8 > 0` y `T_xx > 0`: mínimo local, con `T(1, 0) = 1 − 2 + 3 = 2` °C.",
            "Borde: `y² = 4 − x²` → `T = x² + 2(4 − x²) − 2x + 3 = −x² − 2x + 11`, con `x ∈ [−2, 2]`.",
            "`dT/dx = −2x − 2 = 0` → `x = −1`, `y = ±√3`, `T = −1 + 2 + 11 = 12` °C. Extremos del intervalo: `x = 2` (punto (2, 0)): `T = −4 − 4 + 11 = 3` °C; `x = −2` (punto (−2, 0)): `T = −4 + 4 + 11 = 11` °C.",
            "Con Lagrange se llega a lo mismo: `4y = 2λy` da `y = 0` (puntos (±2, 0)) o `λ = 2`, y entonces `2x − 2 = 4x` → `x = −1`.",
            "Comparación de candidatos: 2 (interior), 12, 3 y 11 (borde). Máximo absoluto `12` °C en `(−1, ±√3)`; mínimo absoluto `2` °C en `(1, 0)`.",
            "c) Sobre el borde solo, el mínimo es `3` °C en `(2, 0)`. Error típico: olvidar los extremos `x = ±2` del intervalo del borde, o aceptar un punto crítico que cae fuera del disco.",
        ],
    },
    # ==================== mv-divergencia-rotacional ====================
    {
        "id": "mv-divergencia-rotacional-1",
        "node": "mv-divergencia-rotacional",
        "kind": "problem",
        "level": 1,
        "title": "Fuente o sumidero, giro horario o antihorario",
        "statement": (
            "La velocidad del agua en la superficie de una laguna se modela con el campo "
            "`F(x, y) = ⟨x²y, x − y²⟩`.\n\n"
            "Analizá qué pasa en el punto `(2, 1)`: si el agua se expande o se comprime y hacia dónde giraría una ruedita de paletas."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale div(F) en (2, 1)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2 (div F = 2xy − 2y)",
            },
            {
                "prompt": "b) ¿Cuánto vale el rotacional 2D de F en (2, 1)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -3, "tolerance": 0, "unit": ""},
                "answer": "−3 (rot F = 1 − x²)",
            },
            {
                "prompt": "c) ¿Qué describe el campo en (2, 1)?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Una fuente (el agua se expande) y la ruedita gira en sentido horario",
                        "Una fuente (el agua se expande) y la ruedita gira en sentido antihorario",
                        "Un sumidero (el agua se comprime) y la ruedita gira en sentido horario",
                        "Un sumidero (el agua se comprime) y la ruedita gira en sentido antihorario",
                    ],
                    "correct": 0,
                },
                "answer": "Una fuente (el agua se expande) y la ruedita gira en sentido horario",
            },
        ],
        "hints": [
            "`div F = ∂P/∂x + ∂Q/∂y` (cada componente con su propia variable, y se SUMA).",
            "`rot F = ∂Q/∂x − ∂P/∂y` (derivadas cruzadas, y se RESTA). Signo negativo = giro horario.",
        ],
        "solution": [
            "`P = x²y`, `Q = x − y²`.",
            "`div F = ∂(x²y)/∂x + ∂(x − y²)/∂y = 2xy − 2y`. En (2, 1): `4 − 2 = 2`.",
            "`rot F = ∂(x − y²)/∂x − ∂(x²y)/∂y = 1 − x²`. En (2, 1): `1 − 4 = −3`.",
            "`div = 2 > 0` → fuente (el fluido se expande); `rot = −3 < 0` → la ruedita gira en sentido horario.",
            "Error típico: cruzar las derivadas en la divergencia (`∂P/∂y + ∂Q/∂x = x² + 1 = 5`) o restar al revés en el rotacional (daría +3, antihorario).",
        ],
    },
    {
        "id": "mv-divergencia-rotacional-2",
        "node": "mv-divergencia-rotacional",
        "kind": "problem",
        "level": 2,
        "title": "¿Cuál de los dos campos es conservativo?",
        "statement": (
            "Se tienen dos campos definidos en todo el plano, que usan las mismas expresiones en distinto orden:\n\n"
            "`F(x, y) = ⟨2xy + 3, x² + 4y⟩` y `G(x, y) = ⟨x² + 4y, 2xy + 3⟩`.\n\n"
            "Decidí cuál es conservativo, encontrá su potencial y medí cuánto gira el otro."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué podés afirmar?",
                "check": {
                    "type": "choice",
                    "options": [
                        "F es conservativo y G no",
                        "G es conservativo y F no",
                        "Los dos son conservativos, porque tienen las mismas expresiones",
                        "Ninguno es conservativo",
                    ],
                    "correct": 0,
                },
                "answer": "F es conservativo y G no",
            },
            {
                "prompt": "b) Sea φ el potencial del campo conservativo con φ(0, 0) = 0. ¿Cuánto vale φ(1, 2)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 13, "tolerance": 0, "unit": ""},
                "answer": "13 (φ = x²y + 3x + 2y²)",
            },
            {
                "prompt": "c) ¿Cuánto vale el rotacional 2D del campo NO conservativo en el punto (1, 3)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2 (rot G = 2y − 4)",
            },
        ],
        "hints": [
            "Calculá `∂Q/∂x − ∂P/∂y` para cada campo (el plano no tiene agujeros, así que rot = 0 alcanza).",
            "Para el potencial integrá P respecto de x (sumando una función h(y)) y después derivá respecto de y para comparar con Q.",
        ],
        "solution": [
            "F: `∂(x² + 4y)/∂x − ∂(2xy + 3)/∂y = 2x − 2x = 0` en todo el plano → F es conservativo.",
            "G: `∂(2xy + 3)/∂x − ∂(x² + 4y)/∂y = 2y − 4`, que no es idénticamente 0 → G no es conservativo.",
            "Potencial de F: `φ = ∫(2xy + 3) dx = x²y + 3x + h(y)`. Derivando: `φ_y = x² + h'(y)`, que debe ser `x² + 4y` → `h'(y) = 4y` → `h = 2y² + C`. Con `φ(0, 0) = 0`, `C = 0`: `φ = x²y + 3x + 2y²`.",
            "b) `φ(1, 2) = 1·2 + 3 + 2·4 = 2 + 3 + 8 = 13`. Verificación: `∇φ = ⟨2xy + 3, x² + 4y⟩ = F`. ✓",
            "c) `rot G(1, 3) = 2·3 − 4 = 2` (giro antihorario en ese punto).",
            "Error típico: armar el potencial sumando las dos integrales completas (`x²y + 3x + x²y + 2y²`), que repite el término `x²y`.",
        ],
    },
    {
        "id": "mv-divergencia-rotacional-3",
        "node": "mv-divergencia-rotacional",
        "kind": "problem",
        "level": 3,
        "title": "Rotacional 3D y un parámetro que vuelve conservativo al campo",
        "statement": (
            "Para cada número real `a` se define el campo en el espacio\n\n"
            "`F(x, y, z) = ⟨2xy + z², x² + a·z, 2xz + 3y⟩`.\n\n"
            "Calculá su rotacional, encontrá el valor de `a` que lo hace conservativo y, para ese valor, su función potencial."
        ),
        "parts": [
            {
                "prompt": "a) Para a = 1, ¿cuánto vale ∇ × F?",
                "check": {
                    "type": "choice",
                    "options": ["⟨2, 0, 0⟩", "⟨−2, 0, 0⟩", "⟨0, 0, 0⟩", "⟨4, 4z, 4x⟩"],
                    "correct": 0,
                },
                "answer": "⟨2, 0, 0⟩",
            },
            {
                "prompt": "b) ¿Para qué valor de a el campo F es conservativo? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3",
            },
            {
                "prompt": "c) Con ese valor de a, sea f el potencial de F con f(0, 0, 0) = 0. ¿Cuánto vale f(1, 2, −1)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -3, "tolerance": 0, "unit": ""},
                "answer": "−3 (f = x²y + xz² + 3yz)",
            },
        ],
        "hints": [
            "`∇ × F = ⟨∂R/∂y − ∂Q/∂z, ∂P/∂z − ∂R/∂x, ∂Q/∂x − ∂P/∂y⟩`.",
            "Calculalo con `a` genérico: solo una componente depende de `a`. El espacio entero no tiene agujeros, así que rotacional nulo alcanza.",
            "Para el potencial integrá P en x, después ajustá con Q y con R las funciones que «faltan».",
        ],
        "solution": [
            "Con `P = 2xy + z²`, `Q = x² + az`, `R = 2xz + 3y`: `∂R/∂y − ∂Q/∂z = 3 − a`; `∂P/∂z − ∂R/∂x = 2z − 2z = 0`; `∂Q/∂x − ∂P/∂y = 2x − 2x = 0`. Entonces `∇ × F = ⟨3 − a, 0, 0⟩`.",
            "a) Con `a = 1`: `∇ × F = ⟨2, 0, 0⟩`. (El distractor `⟨4, 4z, 4x⟩` sale de sumar en lugar de restar; `⟨−2, 0, 0⟩`, de restar en el orden inverso.)",
            "b) `∇ × F = 0` ⇔ `3 − a = 0` ⇔ `a = 3`.",
            "Potencial con `a = 3`: `f = ∫(2xy + z²) dx = x²y + xz² + g(y, z)`. `f_y = x² + g_y = x² + 3z` → `g_y = 3z` → `g = 3yz + k(z)`. `f_z = 2xz + 3y + k'(z) = 2xz + 3y` → `k' = 0`. Con `f(0, 0, 0) = 0`: `f = x²y + xz² + 3yz`.",
            "Verificación: `∇f = ⟨2xy + z², x² + 3z, 2xz + 3y⟩`. ✓",
            "c) `f(1, 2, −1) = 1·2 + 1·1 + 3·2·(−1) = 2 + 1 − 6 = −3`.",
        ],
    },
    # ==================== mv-integrales-dobles-triples ====================
    {
        "id": "mv-integrales-dobles-triples-1",
        "node": "mv-integrales-dobles-triples",
        "kind": "problem",
        "level": 1,
        "title": "Masa de una chapa triangular",
        "statement": (
            "Una chapa ocupa el triángulo `T` de vértices `(0, 0)`, `(2, 0)` y `(2, 2)` (en metros), es decir, "
            "`0 ≤ y ≤ x ≤ 2`. Su densidad superficial es `ρ(x, y) = x + y` (kg/m²).\n\n"
            "Su masa es `M = ∬_T (x + y) dA`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cómo se escribe M integrando primero en x y después en y?",
                "check": {
                    "type": "choice",
                    "options": [
                        "∫_0^2 ∫_y^2 (x + y) dx dy",
                        "∫_0^2 ∫_0^y (x + y) dx dy",
                        "∫_0^2 ∫_0^2 (x + y) dx dy",
                        "∫_0^2 ∫_x^2 (x + y) dx dy",
                    ],
                    "correct": 0,
                },
                "answer": "∫_0^2 ∫_y^2 (x + y) dx dy",
            },
            {
                "prompt": "b) ¿Cuál es la masa de la chapa? Respondé solo con el número en kg.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "kg"},
                "answer": "4 kg",
            },
        ],
        "hints": [
            "Dibujá el triángulo: para un x fijo, y va de 0 hasta la recta y = x. Para un y fijo, ¿desde dónde hasta dónde va x?",
            "Con el orden dy dx: la integral de adentro es `∫_0^x (x + y) dy`.",
        ],
        "solution": [
            "La región es `0 ≤ y ≤ x ≤ 2`. Para un y fijo entre 0 y 2, x va desde la diagonal `x = y` hasta el lado vertical `x = 2`: `M = ∫_0^2 ∫_y^2 (x + y) dx dy`.",
            "Con el orden dy dx: `∫_0^x (x + y) dy = [xy + y²/2]_0^x = x² + x²/2 = (3/2)x²`.",
            "`M = ∫_0^2 (3/2)x² dx = (3/2)·[x³/3]_0^2 = (3/2)·(8/3) = 4` kg.",
            "Verificación con el otro orden: `∫_y^2 (x + y) dx = [x²/2 + xy]_y^2 = 2 + 2y − (3/2)y²`; `∫_0^2 (2 + 2y − 1.5y²) dy = 4 + 4 − 4 = 4`. ✓",
            "Error típico: usar `∫_0^y` (eso describe el otro triángulo, `0 ≤ x ≤ y`) o poner límites que dependen de la misma variable que se integra.",
        ],
    },
    {
        "id": "mv-integrales-dobles-triples-2",
        "node": "mv-integrales-dobles-triples",
        "kind": "problem",
        "level": 2,
        "title": "Una pieza con forma de paraboloide: volumen y masa",
        "statement": (
            "Una pieza maciza de resina ocupa el sólido `E` comprendido entre el paraboloide `z = x² + y²` y el plano "
            "`z = 4` (medidas en dm), es decir `x² + y² ≤ z ≤ 4`.\n\n"
            "La resina es más densa arriba: su densidad es `ρ(x, y, z) = z/2` (kg/dm³). Usá coordenadas cilíndricas."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el volumen de la pieza?",
                "check": {
                    "type": "choice",
                    "options": ["8π dm³", "32π/3 dm³", "16π dm³", "4π dm³"],
                    "correct": 0,
                },
                "answer": "8π dm³",
            },
            {
                "prompt": "b) ¿Cuál es la masa de la pieza? Usá π ≈ 3.14 y redondeá a 2 decimales. Respondé solo con el número en kg.",
                "check": {"type": "numeric", "value": 33.49, "tolerance": 0.01, "unit": "kg"},
                "answer": "33.49 kg (32π/3)",
            },
        ],
        "hints": [
            "En cilíndricas el sólido es `0 ≤ θ ≤ 2π`, `0 ≤ r ≤ 2` (donde el paraboloide alcanza z = 4) y `r² ≤ z ≤ 4`, con `dV = r dz dr dθ`.",
            "Para la masa integrá `z/2` primero en z, entre `r²` y `4`; después multiplicá por r antes de integrar en r.",
        ],
        "solution": [
            "Paraboloide y plano se cortan donde `x² + y² = 4`, o sea `r = 2`. En cilíndricas: `r² ≤ z ≤ 4`, `0 ≤ r ≤ 2`, `0 ≤ θ ≤ 2π`, `dV = r dz dr dθ`.",
            "a) `V = ∫_0^(2π) ∫_0^2 (4 − r²) r dr dθ = 2π·[2r² − r⁴/4]_0^2 = 2π·(8 − 4) = 8π` dm³.",
            "b) Integral de adentro: `∫_(r²)^4 (z/2) dz = [z²/4]_(r²)^4 = (16 − r⁴)/4`.",
            "`M = ∫_0^(2π) ∫_0^2 ((16 − r⁴)/4)·r dr dθ = 2π·(1/4)·[8r² − r⁶/6]_0^2 = (π/2)·(32 − 64/6) = (π/2)·(64/3) = 32π/3`.",
            "Con π ≈ 3.14: `32·3.14/3 ≈ 33.49` kg (con π exacto, 33.51 kg).",
            "Los distractores de a): `32π/3` sale de olvidar el factor r (`∫(4 − r²) dr`), `16π` es el cilindro completo sin restar el hueco y `4π` es usar π en lugar de 2π al integrar en θ.",
        ],
    },
    {
        "id": "mv-integrales-dobles-triples-3",
        "node": "mv-integrales-dobles-triples",
        "kind": "problem",
        "level": 3,
        "title": "Una integral imposible que se vuelve fácil cambiando el orden",
        "statement": (
            "Calculá `I = ∫_0^π ∫_x^π (sen y)/y dy dx`.\n\n"
            "(En `y = 0` el integrando se extiende por continuidad con el valor 1.)"
        ),
        "parts": [
            {
                "prompt": "a) ¿Por qué no conviene resolverla en el orden dado?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Porque (sen y)/y no tiene primitiva elemental en y",
                        "Porque la región de integración no es acotada",
                        "Porque el integrando no es continuo en la región",
                        "Porque el teorema de Fubini solo vale en rectángulos",
                    ],
                    "correct": 0,
                },
                "answer": "Porque (sen y)/y no tiene primitiva elemental en y",
            },
            {
                "prompt": "b) ¿Cómo queda I con el orden de integración invertido?",
                "check": {
                    "type": "choice",
                    "options": [
                        "∫_0^π ∫_0^y (sen y)/y dx dy",
                        "∫_0^π ∫_y^π (sen y)/y dx dy",
                        "∫_0^π ∫_0^π (sen y)/y dx dy",
                        "∫_0^y ∫_0^π (sen y)/y dx dy",
                    ],
                    "correct": 0,
                },
                "answer": "∫_0^π ∫_0^y (sen y)/y dx dy",
            },
            {
                "prompt": "c) ¿Cuánto vale I? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
        ],
        "hints": [
            "Dibujá la región: `0 ≤ x ≤ π` y `x ≤ y ≤ π`. Es un triángulo; ¿cuáles son sus vértices?",
            "Para un y fijo, x va de 0 hasta la diagonal `x = y`. Al integrar primero en x, el integrando es constante.",
        ],
        "solution": [
            "a) La integral de adentro pide una primitiva de `(sen y)/y` respecto de y, que no se puede expresar con funciones elementales (es la función «seno integral»).",
            "Región: `0 ≤ x ≤ π`, `x ≤ y ≤ π`: el triángulo de vértices `(0, 0)`, `(0, π)` y `(π, π)`, por encima de la diagonal `y = x`.",
            "b) Mirada «por filas»: `0 ≤ y ≤ π` y, para cada y, `0 ≤ x ≤ y`. Por Fubini, `I = ∫_0^π ∫_0^y (sen y)/y dx dy`.",
            "Integral de adentro (y queda fija): `∫_0^y (sen y)/y dx = (sen y)/y · y = sen y`.",
            "c) `I = ∫_0^π sen y dy = [−cos y]_0^π = −(−1) − (−1) = 2`.",
            "Verificación numérica: integrando en el orden original con una regla de Simpson se obtiene 2.0000. Error típico: invertir el orden sin redibujar la región y poner `∫_y^π` (eso es el triángulo de abajo de la diagonal).",
        ],
    },
    # ==================== mv-linea-superficie ====================
    {
        "id": "mv-linea-superficie-1",
        "node": "mv-linea-superficie",
        "kind": "problem",
        "level": 1,
        "title": "Mismo inicio, mismo final, distinto trabajo",
        "statement": (
            "Un robot se mueve en un plano bajo la fuerza `F(x, y) = ⟨xy, 2x²⟩` (N, con x e y en metros), desde `O(0, 0)` "
            "hasta `B(2, 4)`, por dos caminos:\n\n"
            "- `C₁`: el segmento recto de O a B.\n"
            "- `C₂`: el arco de la parábola `y = x²` de O a B."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto trabajo hace F sobre el robot a lo largo de C₁? Respondé solo con el número en J.",
                "check": {"type": "numeric", "value": 16, "tolerance": 0, "unit": "J"},
                "answer": "16 J",
            },
            {
                "prompt": "b) ¿Cuánto trabajo hace F a lo largo de C₂? Respondé solo con el número en J.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "J"},
                "answer": "20 J",
            },
            {
                "prompt": "c) ¿Qué se concluye?",
                "check": {
                    "type": "choice",
                    "options": [
                        "F no es conservativo: el trabajo depende del camino (y su rotacional 3x no es nulo)",
                        "F es conservativo, porque los dos caminos empiezan y terminan en los mismos puntos",
                        "Alguna de las cuentas está mal: el trabajo entre dos puntos siempre es el mismo",
                        "F es conservativo solo sobre la parábola",
                    ],
                    "correct": 0,
                },
                "answer": "F no es conservativo: el trabajo depende del camino (y su rotacional 3x no es nulo)",
            },
        ],
        "hints": [
            "Parametrizá: `C₁: r(t) = ⟨t, 2t⟩` y `C₂: r(t) = ⟨t, t²⟩`, con `0 ≤ t ≤ 2` en los dos casos.",
            "`W = ∫ F(r(t)) · r'(t) dt`: reemplazá x e y en F y hacé el producto punto con r'(t).",
        ],
        "solution": [
            "C₁: `r(t) = ⟨t, 2t⟩`, `r'(t) = ⟨1, 2⟩`, `F(r(t)) = ⟨t·2t, 2t²⟩ = ⟨2t², 2t²⟩`. `F · r' = 2t² + 4t² = 6t²`.",
            "a) `W₁ = ∫_0^2 6t² dt = [2t³]_0^2 = 16` J.",
            "C₂: `r(t) = ⟨t, t²⟩`, `r'(t) = ⟨1, 2t⟩`, `F(r(t)) = ⟨t³, 2t²⟩`. `F · r' = t³ + 4t³ = 5t³`.",
            "b) `W₂ = ∫_0^2 5t³ dt = [5t⁴/4]_0^2 = 20` J.",
            "c) Mismos extremos y distinto trabajo: F no es conservativo. Coincide con `rot F = ∂(2x²)/∂x − ∂(xy)/∂y = 4x − x = 3x ≠ 0`.",
            "Dato extra: ir por C₂ y volver por C₁ da una circulación de `20 − 16 = 4` J ≠ 0, otra señal de campo no conservativo.",
        ],
    },
    {
        "id": "mv-linea-superficie-2",
        "node": "mv-linea-superficie",
        "kind": "problem",
        "level": 2,
        "title": "Un camino horrible y un atajo por el potencial",
        "statement": (
            "Una partícula recorre la curva\n\n"
            "`r(t) = ⟨1 + t³, sen(πt/2), t·e^(t − 1)⟩`, con `0 ≤ t ≤ 1`,\n\n"
            "bajo la fuerza `F(x, y, z) = ⟨yz, xz, xy + 2z⟩` (N, coordenadas en m)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál de estas funciones es un potencial de F (∇f = F)?",
                "check": {
                    "type": "choice",
                    "options": [
                        "f = xyz + z²",
                        "f = 3xyz + z²",
                        "f = xyz + 2z²",
                        "f = xy + xz + yz + z²",
                    ],
                    "correct": 0,
                },
                "answer": "f = xyz + z²",
            },
            {
                "prompt": "b) ¿Cuánto trabajo hace F sobre la partícula a lo largo de la curva? Respondé solo con el número en J.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": "J"},
                "answer": "3 J (f(2, 1, 1) − f(1, 0, 0))",
            },
            {
                "prompt": "c) Si la fuerza fuera G = ⟨yz, 2xz, xy + 2z⟩, ¿podrías usar el mismo atajo?",
                "check": {
                    "type": "choice",
                    "options": [
                        "No: ∇ × G = ⟨−x, 0, z⟩ ≠ 0, G no es conservativo y hay que parametrizar",
                        "Sí: G también es conservativo, con potencial 2xyz + z²",
                        "Sí: alcanza con que la curva sea la misma, porque el trabajo solo depende de los extremos",
                        "Sí, porque div(G) es constante",
                    ],
                    "correct": 0,
                },
                "answer": "No: ∇ × G = ⟨−x, 0, z⟩ ≠ 0, G no es conservativo y hay que parametrizar",
            },
        ],
        "hints": [
            "Antes de parametrizar, mirá si F es conservativo: buscá f con `f_x = yz`, `f_y = xz`, `f_z = xy + 2z`.",
            "Teorema fundamental: `W = f(r(1)) − f(r(0))`. Solo hacen falta los puntos inicial y final de la curva.",
        ],
        "solution": [
            "`f = xyz + z²` cumple `f_x = yz`, `f_y = xz`, `f_z = xy + 2z`. ✓ (Las otras opciones fallan: `3xyz` da `f_x = 3yz`; `2z²` da `f_z = xy + 4z`; `xy + xz + yz` da `f_x = y + z`.)",
            "Extremos de la curva: `r(0) = ⟨1, sen 0, 0⟩ = (1, 0, 0)`; `r(1) = ⟨2, sen(π/2), 1·e⁰⟩ = (2, 1, 1)`.",
            "b) `W = f(2, 1, 1) − f(1, 0, 0) = (2 + 1) − 0 = 3` J. (Integrando numéricamente `F(r(t)) · r'(t)` entre 0 y 1 también da 3.)",
            "c) `∇ × G = ⟨∂(xy + 2z)/∂y − ∂(2xz)/∂z, ∂(yz)/∂z − ∂(xy + 2z)/∂x, ∂(2xz)/∂x − ∂(yz)/∂y⟩ = ⟨x − 2x, y − y, 2z − z⟩ = ⟨−x, 0, z⟩ ≠ 0`.",
            "G no es conservativo: su trabajo depende de la curva y no hay atajo. Error típico: usar el teorema fundamental sin comprobar antes que el campo sea un gradiente.",
        ],
    },
    {
        "id": "mv-linea-superficie-3",
        "node": "mv-linea-superficie",
        "kind": "problem",
        "level": 3,
        "title": "Flujo a través de un domo parabólico",
        "statement": (
            "Sea `S` la parte del paraboloide `z = 4 − x² − y²` que está por encima del plano `z = 0`, orientada con la normal "
            "hacia arriba (hacia afuera del domo). Se quiere el flujo del campo `F(x, y, z) = ⟨x, y, 3z⟩` a través de S, "
            "`Φ = ∬_S F · dS`, parametrizando S con `(x, y)` y usando polares en el dominio."
        ),
        "parts": [
            {
                "prompt": "a) Con r(x, y) = ⟨x, y, 4 − x² − y²⟩, ¿qué vector N tal que dS = N dA tiene la orientación pedida?",
                "check": {
                    "type": "choice",
                    "options": ["⟨2x, 2y, 1⟩", "⟨−2x, −2y, 1⟩", "⟨2x, 2y, −1⟩", "⟨−2x, −2y, −1⟩"],
                    "correct": 0,
                },
                "answer": "⟨2x, 2y, 1⟩",
            },
            {
                "prompt": "b) ¿Cuánto vale el flujo Φ? Usá π ≈ 3.14 y redondeá a 1 decimal. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 125.6, "tolerance": 0.01, "unit": ""},
                "answer": "125.6 (Φ = 40π)",
            },
        ],
        "hints": [
            "Para `z = g(x, y)`, `r_x × r_y = ⟨−g_x, −g_y, 1⟩`, que tiene componente z positiva (hacia arriba).",
            "Calculá `F · N` sobre la superficie reemplazando `z = 4 − x² − y²`, y pasá a polares en el disco `x² + y² ≤ 4` (sin olvidar el factor r).",
        ],
        "solution": [
            "`r_x = ⟨1, 0, −2x⟩`, `r_y = ⟨0, 1, −2y⟩`, `r_x × r_y = ⟨2x, 2y, 1⟩`. Su componente z es positiva: apunta hacia arriba, como se pide.",
            "Sobre S: `F = ⟨x, y, 3(4 − x² − y²)⟩`, así que `F · N = 2x² + 2y² + 12 − 3x² − 3y² = 12 − (x² + y²)`.",
            "El dominio es la sombra de S en el plano xy: el disco `x² + y² ≤ 4` (donde z ≥ 0). En polares: `F · N = 12 − r²`, `dA = r dr dθ`.",
            "`Φ = ∫_0^(2π) ∫_0^2 (12 − r²) r dr dθ = 2π·[6r² − r⁴/4]_0^2 = 2π·(24 − 4) = 40π`.",
            "Con π ≈ 3.14: `40·3.14 = 125.6` (con π exacto, 125.66).",
            "Control con Gauss (tema siguiente): `div F = 1 + 1 + 3 = 5` y el sólido bajo el domo tiene volumen `8π`, así que el flujo total saliente es `40π`; por la base `z = 0` el flujo es 0 (`F · (−k) = −3z = 0`), lo que confirma `40π` por el domo. Error típico: olvidar la r del jacobiano (da `128π/3`).",
        ],
    },
    # ==================== mv-teorema-green ====================
    {
        "id": "mv-teorema-green-1",
        "node": "mv-teorema-green",
        "kind": "problem",
        "level": 1,
        "title": "Circulación y flujo por el borde de un rectángulo",
        "statement": (
            "Sea `F(x, y) = ⟨xy, x² + 3x⟩` y `C` el borde del rectángulo `R = [0, 2] × [0, 3]`, recorrido en sentido antihorario.\n\n"
            "Usá las dos formas del teorema de Green: la de circulación y la de flujo (normal hacia afuera)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la circulación ∮_C F · dr? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 24, "tolerance": 0, "unit": ""},
                "answer": "24 (∬_R (x + 3) dA)",
            },
            {
                "prompt": "b) ¿Cuánto vale el flujo saliente ∮_C F · n ds? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": ""},
                "answer": "9 (∬_R y dA)",
            },
        ],
        "hints": [
            "Circulación: integrá `∂Q/∂x − ∂P/∂y` sobre R. Flujo: integrá `div F = ∂P/∂x + ∂Q/∂y` sobre R.",
            "Sobre un rectángulo los límites son constantes: `0 ≤ x ≤ 2`, `0 ≤ y ≤ 3`.",
        ],
        "solution": [
            "`P = xy`, `Q = x² + 3x`. Rotacional: `∂Q/∂x − ∂P/∂y = (2x + 3) − x = x + 3`.",
            "a) `∮ F · dr = ∫_0^2 ∫_0^3 (x + 3) dy dx = 3·∫_0^2 (x + 3) dx = 3·(2 + 6) = 24`.",
            "Divergencia: `∂P/∂x + ∂Q/∂y = y + 0 = y`.",
            "b) `∮ F · n ds = ∫_0^2 ∫_0^3 y dy dx = 2·(9/2) = 9`.",
            "Verificación directa del flujo por lados (normal hacia afuera): abajo `−∫Q(x, 0) dx = −(8/3 + 6)`, derecha `∫P(2, y) dy = 9`, arriba `∫Q(x, 3) dx = 8/3 + 6`, izquierda `−∫P(0, y) dy = 0`; total `9`. ✓",
            "Error típico: usar la divergencia para la circulación (o al revés): son dos integrandos distintos.",
        ],
    },
    {
        "id": "mv-teorema-green-2",
        "node": "mv-teorema-green",
        "kind": "problem",
        "level": 2,
        "title": "El área de un lote caminando su perímetro",
        "statement": (
            "Un agrimensor recorre con un GPS el borde de un lote cuadrilátero en las afueras de La Plata. Los vértices, en metros, "
            "son `A(0, 0)`, `B(40, 0)`, `C(50, 30)` y `D(10, 40)`.\n\n"
            "La app calcula el área con la fórmula que sale de Green, `Área = ½ ∮_C (x dy − y dx)`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale ∫(x dy − y dx) sobre el lado recorrido de B a C? Respondé solo con el número en m².",
                "check": {"type": "numeric", "value": 1200, "tolerance": 0, "unit": "m²"},
                "answer": "1200 m²",
            },
            {
                "prompt": "b) Recorriendo A → B → C → D → A, ¿cuál es el área del lote? Respondé solo con el número en m².",
                "check": {"type": "numeric", "value": 1450, "tolerance": 0, "unit": "m²"},
                "answer": "1450 m²",
            },
            {
                "prompt": "c) Si el agrimensor hubiera recorrido el borde en sentido horario (A → D → C → B → A), ¿qué número mostraría la app? Respondé solo con el número en m².",
                "check": {"type": "numeric", "value": -1450, "tolerance": 0, "unit": "m²"},
                "answer": "−1450 m² (la orientación cambia el signo)",
            },
        ],
        "hints": [
            "Parametrizá el lado de `(x₁, y₁)` a `(x₂, y₂)` como `r(t) = (x₁ + t(x₂ − x₁), y₁ + t(y₂ − y₁))`, `0 ≤ t ≤ 1`.",
            "Sobre cada segmento la integral da `x₁y₂ − x₂y₁` (fórmula del cordón). Sumá los cuatro lados y dividí por 2.",
        ],
        "solution": [
            "¿Por qué funciona? Con `P = −y`, `Q = x`: `∂Q/∂x − ∂P/∂y = 1 + 1 = 2`, así que `∮(x dy − y dx) = ∬ 2 dA = 2·Área`.",
            "Lado B → C: `x = 40 + 10t`, `y = 30t`, `dx = 10 dt`, `dy = 30 dt`. `x dy − y dx = [(40 + 10t)·30 − 30t·10] dt = 1200 dt` → `∫_0^1 1200 dt = 1200`.",
            "En general cada lado aporta `x₁y₂ − x₂y₁`: A → B: `0·0 − 40·0 = 0`; B → C: `40·30 − 50·0 = 1200`; C → D: `50·40 − 10·30 = 1700`; D → A: `10·0 − 0·40 = 0`.",
            "b) Suma `= 2900` → Área `= 2900/2 = 1450` m². El recorrido A → B → C → D es antihorario (el lote queda a la izquierda), así que el signo es positivo.",
            "c) Al invertir el sentido cada integral de línea cambia de signo: la app mostraría `−1450` m².",
            "Error típico: olvidar el ½ (darías 2900) o no fijarse en la orientación.",
        ],
    },
    {
        "id": "mv-teorema-green-3",
        "node": "mv-teorema-green",
        "kind": "problem",
        "level": 3,
        "title": "Trabajo sobre un triángulo: directo y con Green",
        "statement": (
            "Un robot de limpieza recorre el borde del triángulo de vértices `O(0, 0)`, `A(3, 0)` y `B(3, 3)` (en metros), en el "
            "orden `O → A → B → O`, sometido a la fuerza `F(x, y) = ⟨y², 3xy⟩` (N).\n\n"
            "Calculá el trabajo total de F en la vuelta completa de dos maneras: lado por lado y con el teorema de Green."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto trabajo hace F en el tramo de B a O (la hipotenusa)? Respondé solo con el número en J.",
                "check": {"type": "numeric", "value": -36, "tolerance": 0, "unit": "J"},
                "answer": "−36 J",
            },
            {
                "prompt": "b) ¿Cuánto vale el trabajo total en la vuelta completa? Respondé solo con el número en J.",
                "check": {"type": "numeric", "value": 4.5, "tolerance": 0, "unit": "J"},
                "answer": "4.5 J",
            },
            {
                "prompt": "c) ¿Qué se concluye del resultado?",
                "check": {
                    "type": "choice",
                    "options": [
                        "F no es conservativo: su circulación sobre una curva cerrada no es 0 (rot F = y)",
                        "F es conservativo, porque la curva es cerrada",
                        "El trabajo en una curva cerrada debería ser 0, así que hay un error de cuentas",
                        "Green no se puede aplicar porque el triángulo tiene esquinas",
                    ],
                    "correct": 0,
                },
                "answer": "F no es conservativo: su circulación sobre una curva cerrada no es 0 (rot F = y)",
            },
        ],
        "hints": [
            "Parametrizá cada lado respetando el sentido: la hipotenusa de B a O es `r(t) = (t, t)` con t de 3 a 0 (o `(3 − t, 3 − t)` con t de 0 a 3).",
            "O → A → B → O es antihorario. Green: `∬_T (∂Q/∂x − ∂P/∂y) dA` sobre `0 ≤ y ≤ x ≤ 3`.",
        ],
        "solution": [
            "Lado O → A: `y = 0`, `dy = 0` → `P dx = 0·dx` → trabajo `0`.",
            "Lado A → B: `x = 3`, `dx = 0`, y de 0 a 3 → `∫_0^3 Q(3, y) dy = ∫_0^3 9y dy = 40.5` J.",
            "a) Hipotenusa B → O: `x = y = t`, t de 3 a 0 → `P dx + Q dy = (t² + 3t²) dt = 4t² dt` → `∫_3^0 4t² dt = −[4t³/3]_0^3 = −36` J.",
            "b) Total directo: `0 + 40.5 − 36 = 4.5` J.",
            "Con Green (el recorrido es antihorario): `∂Q/∂x − ∂P/∂y = 3y − 2y = y` → `∬_T y dA = ∫_0^3 ∫_0^x y dy dx = ∫_0^3 x²/2 dx = 27/6 = 4.5` J. ✓",
            "c) La circulación es distinta de 0, así que F no es conservativo (su rotacional `y` no es nulo). Green vale para curvas suaves a trozos como el triángulo. Error típico: recorrer la hipotenusa de O a B y obtener +36, que da un total de 76.5 J.",
        ],
    },
    # ==================== mv-stokes-divergencia ====================
    {
        "id": "mv-stokes-divergencia-1",
        "node": "mv-stokes-divergencia",
        "kind": "problem",
        "level": 1,
        "title": "Gauss en una caja con divergencia variable",
        "statement": (
            "Sea `F(x, y, z) = ⟨x², y², z²⟩` y `S` la superficie de la caja `[0, 1] × [0, 2] × [0, 3]` (seis caras), con "
            "normales hacia afuera."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale el flujo total saliente ∯_S F · dS? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 36, "tolerance": 0, "unit": ""},
                "answer": "36",
            },
            {
                "prompt": "b) ¿Cuánto de ese flujo sale por la tapa superior (z = 3)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 18, "tolerance": 0, "unit": ""},
                "answer": "18 (z² = 9 por área 2)",
            },
        ],
        "hints": [
            "La caja es una superficie cerrada: `∯ F · dS = ∭ div F dV`, con `div F = 2x + 2y + 2z`.",
            "En la tapa `z = 3` la normal es `k`, así que `F · n = z² = 9`, constante.",
        ],
        "solution": [
            "`div F = 2x + 2y + 2z`.",
            "`∭ 2x dV = 2·(∫_0^1 x dx)·2·3 = 2·(1/2)·6 = 6`; `∭ 2y dV = 2·1·(∫_0^2 y dy)·3 = 2·2·3 = 12`; `∭ 2z dV = 2·1·2·(∫_0^3 z dz) = 2·2·4.5 = 18`.",
            "a) Flujo total `= 6 + 12 + 18 = 36`.",
            "b) Tapa `z = 3`, normal `⟨0, 0, 1⟩`: `F · n = 9` en toda la cara, de área `1·2 = 2` → flujo `18`.",
            "Verificación cara por cara: x = 1 da `1·6 = 6`, y = 2 da `4·3 = 12`, z = 3 da `9·2 = 18`; las caras x = 0, y = 0, z = 0 dan 0 (allí la componente normal de F vale 0). Total 36. ✓",
        ],
    },
    {
        "id": "mv-stokes-divergencia-2",
        "node": "mv-stokes-divergencia",
        "kind": "problem",
        "level": 2,
        "title": "Stokes: cambiar el domo por su tapa plana",
        "statement": (
            "Sea `S` el domo `z = 4 − x² − y²`, `z ≥ 0`, orientado con la normal hacia arriba, y "
            "`F(x, y, z) = ⟨z² − 2y, x + z³, xyz⟩`.\n\n"
            "Se quiere el flujo del rotacional `∬_S (∇ × F) · dS`. En lugar de integrar sobre el domo, usá el teorema de Stokes "
            "y una superficie más simple con el mismo borde."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la componente z de ∇ × F (en cualquier punto)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3",
            },
            {
                "prompt": "b) ¿Cuánto vale ∬_S (∇ × F) · dS?",
                "check": {
                    "type": "choice",
                    "options": ["12π", "−12π", "4π", "0"],
                    "correct": 0,
                },
                "answer": "12π",
            },
        ],
        "hints": [
            "El borde del domo es la circunferencia `x² + y² = 4` en `z = 0`, recorrida en sentido antihorario visto desde arriba (regla de la mano derecha con la normal hacia arriba).",
            "El disco `x² + y² ≤ 4`, `z = 0`, con normal `k`, tiene el mismo borde: ahí solo importa la componente z del rotacional.",
        ],
        "solution": [
            "`∇ × F = ⟨∂(xyz)/∂y − ∂(x + z³)/∂z, ∂(z² − 2y)/∂z − ∂(xyz)/∂x, ∂(x + z³)/∂x − ∂(z² − 2y)/∂y⟩ = ⟨xz − 3z², 2z − yz, 1 + 2⟩`.",
            "a) La componente z es `1 − (−2) = 3`, constante.",
            "Por Stokes, el domo y el disco `D: x² + y² ≤ 4, z = 0` (normal `k`) tienen el mismo borde con la misma orientación, así que el flujo del rotacional es igual.",
            "b) En D: `(∇ × F) · k = 3` → `∬_D 3 dA = 3·π·2² = 12π`.",
            "Verificación con la integral de línea: en `r(t) = ⟨2cos t, 2sen t, 0⟩`, `F = ⟨−4sen t, 2cos t, 0⟩`, `r' = ⟨−2sen t, 2cos t, 0⟩`; `F · r' = 8sen²t + 4cos²t` → `∫_0^(2π) = 8π + 4π = 12π`. ✓",
            "Errores típicos: orientar mal el borde (da −12π), olvidar el factor 3 (da 4π, el área del disco) o creer que el flujo de un rotacional siempre es 0 (eso vale solo para superficies cerradas, sin borde).",
        ],
    },
    {
        "id": "mv-stokes-divergencia-3",
        "node": "mv-stokes-divergencia",
        "kind": "problem",
        "level": 3,
        "title": "Flujo por la pared de un tanque usando Gauss",
        "statement": (
            "Un tanque cilíndrico ocupa `V: x² + y² ≤ 4`, `0 ≤ z ≤ 3`. Su superficie cerrada está formada por la pared lateral, "
            "la tapa `z = 3` y el fondo `z = 0`, todas con normal hacia afuera. Se considera el campo\n\n"
            "`F(x, y, z) = ⟨x + y², y − xz, z²⟩`.\n\n"
            "Calcular el flujo por la pared lateral en forma directa es largo: obtenelo con el teorema de la divergencia y las tapas."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el flujo total saliente por la superficie cerrada del tanque?",
                "check": {
                    "type": "choice",
                    "options": ["60π", "42π", "36π", "15π"],
                    "correct": 0,
                },
                "answer": "60π",
            },
            {
                "prompt": "b) ¿Cuál es el flujo saliente por la tapa z = 3? Usá π ≈ 3.14 y redondeá a 2 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 113.04, "tolerance": 0.01, "unit": ""},
                "answer": "113.04 (36π)",
            },
            {
                "prompt": "c) ¿Cuál es el flujo saliente por la pared lateral? Usá π ≈ 3.14 y redondeá a 2 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 75.36, "tolerance": 0.01, "unit": ""},
                "answer": "75.36 (24π)",
            },
        ],
        "hints": [
            "`div F = 1 + 1 + 2z`. Integrala en cilíndricas: la base es un disco de área 4π y z va de 0 a 3.",
            "En la tapa la normal es `k` y `F · k = z² = 9`; en el fondo la normal es `−k` y `F · (−k) = −z² = 0`.",
            "Flujo lateral = flujo total − tapa − fondo.",
        ],
        "solution": [
            "`div F = ∂(x + y²)/∂x + ∂(y − xz)/∂y + ∂(z²)/∂z = 1 + 1 + 2z = 2 + 2z`.",
            "a) `∭_V (2 + 2z) dV = (área de la base)·∫_0^3 (2 + 2z) dz = 4π·[2z + z²]_0^3 = 4π·15 = 60π`.",
            "b) Tapa `z = 3`: `F · k = 9` → flujo `9·4π = 36π ≈ 36·3.14 = 113.04`.",
            "Fondo `z = 0`: `F · (−k) = −0² = 0` → flujo `0`.",
            "c) Lateral: `60π − 36π − 0 = 24π ≈ 24·3.14 = 75.36`.",
            "Verificación directa: en la pared `n = ⟨x, y, 0⟩/2` y `F · n = (x² + y² + xy² − xyz)/2`; los términos `xy²` y `xyz` se anulan al integrar en θ y queda `∬ 2 dS = 2·(2π·2·3) = 24π`. ✓",
            "Errores típicos: olvidar que el fondo también es parte de la superficie (acá aporta 0, pero hay que verificarlo), integrar `div F` como si fuera `2 + z` (da 42π) o tomar el área de la base como `π` en vez de `π·2² = 4π` (da 15π).",
        ],
    },
]
