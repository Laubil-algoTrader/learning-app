"""Ejercicios de Matemática: Cálculo 2 (Análisis Matemático II, una variable; temas 85-91).

Tres problemas por tema (niveles 1, 2 y 3). Los de nivel 3 apuntan a la dificultad de un parcial.
Borrador: la app ignora los archivos que empiezan con `_draft_` hasta que se revisen.
"""

from __future__ import annotations

EXERCISES: list[dict] = [
    # ==================== c2-partes-fracciones ====================
    {
        "id": "c2-partes-fracciones-1",
        "node": "c2-partes-fracciones",
        "kind": "problem",
        "level": 1,
        "title": "Por partes con un seno",
        "statement": (
            "Calculá la integral definida `∫(de 0 a π) x·sen(x) dx` usando integración por partes."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es una primitiva de `x·sen(x)`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "−x·cos(x) + sen(x) + C",
                        "x·cos(x) − sen(x) + C",
                        "−x·cos(x) − sen(x) + C",
                        "−(x²/2)·cos(x) + C",
                    ],
                    "correct": 0,
                },
                "answer": "−x·cos(x) + sen(x) + C",
            },
            {
                "prompt": "b) ¿Cuánto vale `∫(de 0 a π) x·sen(x) dx`? Redondeá a 3 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3.142, "tolerance": 0.001, "unit": ""},
                "answer": "3.142 (el valor exacto es π)",
            },
        ],
        "hints": [
            "Por LIATE, la parte Algebraica (`x`) va antes que la Trigonométrica: `u = x`, `dv = sen(x) dx`.",
            "Ojo con el signo: si `dv = sen(x) dx`, entonces `v = −cos(x)`.",
        ],
        "solution": [
            "Elegimos `u = x` → `du = dx`, y `dv = sen(x) dx` → `v = −cos(x)`.",
            "`∫ x·sen(x) dx = u·v − ∫ v du = −x·cos(x) − ∫ (−cos(x)) dx = −x·cos(x) + ∫ cos(x) dx = −x·cos(x) + sen(x) + C`.",
            "Verificación derivando: `(−x·cos(x) + sen(x))' = −cos(x) + x·sen(x) + cos(x) = x·sen(x)` ✓.",
            "Evaluamos: en `x = π`: `−π·cos(π) + sen(π) = −π·(−1) + 0 = π`; en `x = 0`: `−0·1 + 0 = 0`.",
            "Resultado: `π − 0 = π ≈ 3.142`. Error típico: tomar `v = cos(x)` (sin el signo menos), que da `x·cos(x) − sen(x)` y el resultado `−π`, imposible porque `x·sen(x) ≥ 0` en `[0, π]`.",
        ],
    },
    {
        "id": "c2-partes-fracciones-2",
        "node": "c2-partes-fracciones",
        "kind": "problem",
        "level": 2,
        "title": "Primero dividir, después partir",
        "statement": (
            "Calculá `∫(de 2 a 3) (x² + 3) / (x² − 1) dx`.\n\n"
            "Observá que el grado del numerador no es menor que el del denominador."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la descomposición correcta del integrando?",
                "check": {
                    "type": "choice",
                    "options": [
                        "1 + 2/(x − 1) − 2/(x + 1)",
                        "2/(x − 1) − 2/(x + 1)",
                        "1 + 4/(x − 1) − 4/(x + 1)",
                        "1 + 2/(x − 1) + 2/(x + 1)",
                    ],
                    "correct": 0,
                },
                "answer": "1 + 2/(x − 1) − 2/(x + 1)",
            },
            {
                "prompt": "b) ¿Cuánto vale la integral? Redondeá a 3 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1.811, "tolerance": 0.001, "unit": ""},
                "answer": "1.811 (valor exacto 1 + 2·ln(3/2))",
            },
        ],
        "hints": [
            "Como los grados son iguales, dividí: `(x² + 3)/(x² − 1) = 1 + (algo)/(x² − 1)`.",
            "Factorizá `x² − 1 = (x − 1)(x + 1)` y buscá `A` y `B` evaluando en `x = 1` y `x = −1`.",
        ],
        "solution": [
            "División: `x² + 3 = 1·(x² − 1) + 4`, así que `(x² + 3)/(x² − 1) = 1 + 4/(x² − 1)`.",
            "Fracciones simples: `4/((x − 1)(x + 1)) = A/(x − 1) + B/(x + 1)` → `4 = A(x + 1) + B(x − 1)`. En `x = 1`: `4 = 2A` → `A = 2`. En `x = −1`: `4 = −2B` → `B = −2`.",
            "Integrando queda `1 + 2/(x − 1) − 2/(x + 1)`, con primitiva `x + 2·ln|x − 1| − 2·ln|x + 1|`.",
            "En `x = 3`: `3 + 2·ln 2 − 2·ln 4`. En `x = 2`: `2 + 2·ln 1 − 2·ln 3 = 2 − 2·ln 3`.",
            "Resta: `1 + 2·ln 2 − 2·ln 4 + 2·ln 3 = 1 + 2·ln(2·3/4) = 1 + 2·ln(3/2) ≈ 1 + 0.8109 = 1.811`.",
            "Errores típicos: olvidarse del `1` de la división (te da `0.811`) o no dividir `4` por `2` al despejar `A` y `B`.",
        ],
    },
    {
        "id": "c2-partes-fracciones-3",
        "node": "c2-partes-fracciones",
        "kind": "problem",
        "level": 3,
        "title": "Partes que desembocan en fracciones simples",
        "statement": (
            "Calculá `∫(de 1 a 3) ln(x) / (x + 1)² dx`.\n\n"
            "Vas a necesitar integración por partes y, después, una descomposición en fracciones simples."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es una primitiva de `ln(x)/(x + 1)²` para `x > 0`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "−ln(x)/(x + 1) + ln(x) − ln(x + 1) + C",
                        "−ln(x)/(x + 1) − ln(x) + ln(x + 1) + C",
                        "ln(x)/(x + 1) + ln(x) − ln(x + 1) + C",
                        "−ln(x)/(x + 1) + ln(x) + ln(x + 1) + C",
                    ],
                    "correct": 0,
                },
                "answer": "−ln(x)/(x + 1) + ln(x) − ln(x + 1) + C",
            },
            {
                "prompt": "b) ¿Cuánto vale `∫(de 1 a 3) ln(x)/(x + 1)² dx`? Redondeá a 3 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.131, "tolerance": 0.005, "unit": ""},
                "answer": "0.131 (valor exacto (3/4)·ln 3 − ln 2 ≈ 0.1308)",
            },
        ],
        "hints": [
            "LIATE: el logaritmo va como `u`. Entonces `dv = dx/(x + 1)²` y `v = −1/(x + 1)`.",
            "La integral que queda es `∫ 1/(x·(x + 1)) dx`: partila como `A/x + B/(x + 1)`.",
        ],
        "solution": [
            "Partes: `u = ln(x)` → `du = dx/x`; `dv = (x + 1)⁻² dx` → `v = −1/(x + 1)`.",
            "`∫ ln(x)/(x + 1)² dx = −ln(x)/(x + 1) − ∫ (−1/(x + 1))·(1/x) dx = −ln(x)/(x + 1) + ∫ 1/(x(x + 1)) dx`.",
            "Fracciones simples: `1 = A(x + 1) + Bx`. En `x = 0`: `A = 1`; en `x = −1`: `B = −1`. Así `∫ 1/(x(x + 1)) dx = ln|x| − ln|x + 1|`.",
            "Primitiva: `F(x) = −ln(x)/(x + 1) + ln(x) − ln(x + 1)`.",
            "`F(3) = −ln 3/4 + ln 3 − ln 4 = (3/4)·ln 3 − 2·ln 2`; `F(1) = 0 + 0 − ln 2 = −ln 2`.",
            "`F(3) − F(1) = (3/4)·ln 3 − 2·ln 2 + ln 2 = (3/4)·ln 3 − ln 2 ≈ 0.82396 − 0.69315 = 0.1308 ≈ 0.131`.",
            "Control: en `[1, 3]` el integrando es positivo y menor que `ln 3/4 ≈ 0.27`, así que la integral debe estar entre `0` y `0.55` ✓. Error típico: perder el signo de `v = −1/(x + 1)`, que invierte los signos de los logaritmos.",
        ],
    },
    # ==================== c2-impropias-longitud ====================
    {
        "id": "c2-impropias-longitud-1",
        "node": "c2-impropias-longitud",
        "kind": "problem",
        "level": 1,
        "title": "La vida útil de una lámpara LED",
        "statement": (
            "Un fabricante de Córdoba modela la duración `T` (en años) de sus lámparas LED con la densidad de "
            "probabilidad `f(t) = 0.5·e^(−0.5t)` para `t ≥ 0`. La probabilidad de que una lámpara dure más de "
            "`a` años es `∫(de a a ∞) f(t) dt`."
        ),
        "parts": [
            {
                "prompt": "a) Comprobá que es una densidad: ¿cuánto vale `∫(de 0 a ∞) 0.5·e^(−0.5t) dt`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1",
            },
            {
                "prompt": "b) ¿Cuál es la probabilidad de que una lámpara dure más de 4 años? Redondeá a 3 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.135, "tolerance": 0.004, "unit": ""},
                "answer": "0.135 (valor exacto e⁻² ≈ 0.1353)",
            },
        ],
        "hints": [
            "Reemplazá `∞` por `b` y tomá el límite cuando `b → ∞`.",
            "Una primitiva de `0.5·e^(−0.5t)` es `−e^(−0.5t)`.",
        ],
        "solution": [
            "Primitiva: `∫ 0.5·e^(−0.5t) dt = −e^(−0.5t)` (derivando: `−e^(−0.5t)·(−0.5) = 0.5·e^(−0.5t)` ✓).",
            "a) `∫(de 0 a ∞) = lim(b → ∞) [−e^(−0.5t)] de 0 a b = lim(b → ∞) (−e^(−0.5b) + 1) = 0 + 1 = 1`. Converge y el área total es 1, como debe ser.",
            "b) `∫(de 4 a ∞) = lim(b → ∞) (−e^(−0.5b) + e^(−2)) = e^(−2)`.",
            "`e^(−2) ≈ 0.1353`, o sea alrededor del 13.5 % de las lámparas dura más de 4 años.",
            "Error típico: evaluar `−e^(−0.5t)` en `∞` como `−∞` en vez de `0`: la exponencial negativa tiende a cero.",
        ],
    },
    {
        "id": "c2-impropias-longitud-2",
        "node": "c2-impropias-longitud",
        "kind": "problem",
        "level": 2,
        "title": "Cuánto mide el borde de una rampa",
        "statement": (
            "El borde de una rampa de un skatepark de Rosario sigue la curva `y = x³/6 + 1/(2x)` para "
            "`1 ≤ x ≤ 2` (`x` e `y` en metros). Se quiere saber cuántos metros de perfil metálico hacen falta "
            "para cubrir ese borde."
        ),
        "parts": [
            {
                "prompt": "a) ¿A qué se simplifica `√(1 + [y'(x)]²)` en `[1, 2]`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "x²/2 + 1/(2x²)",
                        "x²/2 − 1/(2x²)",
                        "1 + x²/2 − 1/(2x²)",
                        "√(1 + x⁴/4)",
                    ],
                    "correct": 0,
                },
                "answer": "x²/2 + 1/(2x²)",
            },
            {
                "prompt": "b) ¿Cuál es la longitud del borde? Podés responder con una fracción o redondear a 3 decimales. Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 1.4166666666666667, "tolerance": 0.001, "unit": "m"},
                "answer": "17/12 m ≈ 1.417 m",
            },
        ],
        "hints": [
            "Derivá: `y' = x²/2 − 1/(2x²)`. Elevalo al cuadrado y sumale 1.",
            "`1 + (a − b)²` con `a·b = 1/4` se convierte en `(a + b)²`: es un cuadrado perfecto.",
        ],
        "solution": [
            "`y' = 3x²/6 − 1/(2x²) = x²/2 − 1/(2x²)`.",
            "`[y']² = x⁴/4 − 2·(x²/2)·(1/(2x²)) + 1/(4x⁴) = x⁴/4 − 1/2 + 1/(4x⁴)`.",
            "`1 + [y']² = x⁴/4 + 1/2 + 1/(4x⁴) = (x²/2 + 1/(2x²))²`, y como es positivo, `√(1 + [y']²) = x²/2 + 1/(2x²)`.",
            "`L = ∫(de 1 a 2) (x²/2 + 1/(2x²)) dx = [x³/6 − 1/(2x)] de 1 a 2`.",
            "En `x = 2`: `8/6 − 1/4 = 13/12`. En `x = 1`: `1/6 − 1/2 = −1/3 = −4/12`. `L = 13/12 + 4/12 = 17/12 ≈ 1.417 m`.",
            "Control: la cuerda entre `(1, 2/3)` y `(2, 19/12)` mide `√(1 + (11/12)²) ≈ 1.357 m`, un poco menos que el arco ✓.",
        ],
    },
    {
        "id": "c2-impropias-longitud-3",
        "node": "c2-impropias-longitud",
        "kind": "problem",
        "level": 3,
        "title": "Una familia de impropias con parámetro",
        "statement": (
            "Para `p > 0` se definen las integrales impropias\n\n"
            "`I(p) = ∫(de e a ∞) dx / (x·(ln x)^p)`   y   `J(p) = ∫(de 1 a e) dx / (x·(ln x)^p)`.\n\n"
            "(`J` es impropia porque `ln x = 0` en `x = 1`.)"
        ),
        "parts": [
            {
                "prompt": "a) ¿Para qué valor de `p` se cumple `I(p) = 4`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1.25, "tolerance": 0, "unit": ""},
                "answer": "1.25 (p = 5/4)",
            },
            {
                "prompt": "b) ¿Cuánto vale `J(1/2)`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
            {
                "prompt": "c) ¿Para qué valores de `p > 0` converge `∫(de 1 a ∞) dx / (x·(ln x)^p) = J(p) + I(p)`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Para ningún p > 0",
                        "Solo para p > 1",
                        "Solo para p < 1",
                        "Solo para p = 1",
                    ],
                    "correct": 0,
                },
                "answer": "Para ningún p > 0",
            },
        ],
        "hints": [
            "Sustituí `u = ln x`, `du = dx/x`: las dos integrales se vuelven del tipo `∫ du/u^p`.",
            "Con la sustitución, `I(p) = ∫(de 1 a ∞) u^(−p) du` y `J(p) = ∫(de 0 a 1) u^(−p) du`: acordate de la regla `p` para cada caso.",
        ],
        "solution": [
            "Con `u = ln x` (`du = dx/x`): `x = e → u = 1`, `x → ∞ → u → ∞`, `x = 1 → u = 0`. Queda `I(p) = ∫(de 1 a ∞) u^(−p) du` y `J(p) = ∫(de 0 a 1) u^(−p) du`.",
            "`I(p)`: para `p ≠ 1`, `lim(b → ∞) [u^(1−p)/(1 − p)] de 1 a b`. Si `p > 1`, `b^(1−p) → 0` y `I(p) = 1/(p − 1)`; si `p < 1` diverge; si `p = 1` da `lim ln b = ∞`. Converge ⇔ `p > 1`.",
            "a) `1/(p − 1) = 4` → `p − 1 = 1/4` → `p = 5/4 = 1.25` (cumple `p > 1` ✓).",
            "`J(p)`: para `p ≠ 1`, `lim(a → 0⁺) [u^(1−p)/(1 − p)] de a a 1`. Si `p < 1`, `a^(1−p) → 0` y `J(p) = 1/(1 − p)`; si `p > 1`, `a^(1−p) → ∞`; si `p = 1`, `−ln a → ∞`. Converge ⇔ `p < 1`.",
            "b) `J(1/2) = 1/(1 − 1/2) = 2` (directo: `[2√u] de 0 a 1 = 2`).",
            "c) La integral sobre `[1, ∞)` converge solo si convergen las DOS partes: hace falta `p > 1` y `p < 1` a la vez, imposible. No converge para ningún `p`.",
            "Error típico: aplicar la regla `p > 1` también cerca de `0` (ahí es al revés: converge con `p < 1`).",
        ],
    },
    # ==================== c2-euler-logistico ====================
    {
        "id": "c2-euler-logistico-1",
        "node": "c2-euler-logistico",
        "kind": "problem",
        "level": 1,
        "title": "Dos pasos de Euler",
        "statement": (
            "Se quiere aproximar la solución de `dy/dx = x² − y` con `y(0) = 1` usando el método de Euler "
            "con paso `Δx = 0.5`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué valor aproxima Euler para `y(0.5)`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.5, "tolerance": 0, "unit": ""},
                "answer": "0.5",
            },
            {
                "prompt": "b) ¿Qué valor aproxima Euler para `y(1)`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.375, "tolerance": 0, "unit": ""},
                "answer": "0.375",
            },
        ],
        "hints": [
            "Fórmula: `y_(n+1) = y_n + Δx · f(x_n, y_n)`, con `f(x, y) = x² − y`.",
            "En el segundo paso la pendiente se recalcula en el punto `(0.5, y₁)`.",
        ],
        "solution": [
            "Paso 1, desde `(x₀, y₀) = (0, 1)`: pendiente `f(0, 1) = 0² − 1 = −1`.",
            "`y₁ = 1 + 0.5·(−1) = 0.5`, en `x₁ = 0.5`.",
            "Paso 2, desde `(0.5, 0.5)`: pendiente `f(0.5, 0.5) = 0.25 − 0.5 = −0.25`.",
            "`y₂ = 0.5 + 0.5·(−0.25) = 0.375`, en `x₂ = 1`.",
            "Comparación: la solución exacta es `y = x² − 2x + 2 − e^(−x)`, con `y(1) ≈ 0.632`. El paso grande deja un error de casi `0.26`. Error típico: reusar la pendiente inicial `−1` en el segundo paso (daría `0`).",
        ],
    },
    {
        "id": "c2-euler-logistico-2",
        "node": "c2-euler-logistico",
        "kind": "problem",
        "level": 2,
        "title": "Usuarios de una app de delivery",
        "statement": (
            "La cantidad de usuarios `P(t)` de una app de delivery en Mendoza (`t` en meses) sigue el modelo "
            "logístico `dP/dt = k·P·(1 − P/10000)`. Al lanzarla había `P(0) = 1000` usuarios y a los 2 meses "
            "había `P(2) = 2500`.\n\n"
            "La solución de este modelo tiene la forma `P(t) = K / (1 + A·e^(−kt))`, donde `K` es la "
            "capacidad de carga."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la constante `k`? Redondeá a 3 decimales. Respondé solo con el número en 1/mes.",
                "check": {"type": "numeric", "value": 0.549, "tolerance": 0.002, "unit": "1/mes"},
                "answer": "0.549 1/mes (valor exacto ln(3)/2)",
            },
            {
                "prompt": "b) ¿En qué instante la cantidad de usuarios crece más rápido? Respondé solo con el número en meses.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "meses"},
                "answer": "4 meses",
            },
            {
                "prompt": "c) ¿Cuál es esa tasa máxima de crecimiento? Redondeá al entero. Respondé solo con el número en usuarios/mes.",
                "check": {"type": "numeric", "value": 1373, "tolerance": 0.001, "unit": "usuarios/mes"},
                "answer": "1373 usuarios/mes (valor exacto 1250·ln 3)",
            },
        ],
        "hints": [
            "Con `t = 0` obtenés `A` a partir de `P(0)`; con `P(2) = 2500` despejás `e^(−2k)`.",
            "El crecimiento es máximo cuando `P = K/2`: buscá el `t` en que eso pasa y evaluá `dP/dt` ahí.",
        ],
        "solution": [
            "`K = 10000`. En `t = 0`: `1000 = 10000/(1 + A)` → `1 + A = 10` → `A = 9`.",
            "En `t = 2`: `2500 = 10000/(1 + 9e^(−2k))` → `1 + 9e^(−2k) = 4` → `e^(−2k) = 1/3` → `k = ln(3)/2 ≈ 0.549` por mes.",
            "El crecimiento es máximo en el punto de inflexión `P = K/2 = 5000`: `10000/(1 + 9e^(−kt)) = 5000` → `9e^(−kt) = 1` → `t = ln(9)/k = 2·ln 3 / (ln(3)/2) = 4` meses.",
            "Tasa máxima: `dP/dt = k·5000·(1 − 1/2) = k·K/4 = (ln(3)/2)·2500 = 1250·ln 3 ≈ 1373.27` → `1373` usuarios/mes.",
            "Control: `P(4) = 10000/(1 + 9·(1/9)) = 5000` ✓ (como `e^(−4k) = (e^(−2k))² = 1/9`).",
            "Error típico: tomar `A = 1000` (el valor inicial) en vez de `A = (K − P₀)/P₀ = 9`.",
        ],
    },
    {
        "id": "c2-euler-logistico-3",
        "node": "c2-euler-logistico",
        "kind": "problem",
        "level": 3,
        "title": "Euler contra la solución exacta",
        "statement": (
            "Considerá el problema de valor inicial `dy/dx = 2x·y`, `y(0) = 1`.\n\n"
            "Aproximá `y(1)` con el método de Euler usando 4 pasos de `Δx = 0.25`, y después compará con el "
            "valor exacto, que podés obtener resolviendo la ecuación por separación de variables."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué valor aproxima Euler para `y(1)`? Redondeá a 4 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1.9336, "tolerance": 0.0005, "unit": ""},
                "answer": "1.9336 (exacto 1.93359375)",
            },
            {
                "prompt": "b) ¿Cuál es el error absoluto |y(1) exacto − aproximación de Euler|? Redondeá a 3 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.785, "tolerance": 0.002, "unit": ""},
                "answer": "0.785 (e − 1.93359375 ≈ 0.7847)",
            },
            {
                "prompt": "c) ¿Por qué Euler queda por debajo del valor exacto en este problema?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Porque la solución es cóncava hacia arriba en [0, 1] y las tangentes quedan debajo de la curva",
                        "Porque la solución es cóncava hacia abajo en [0, 1] y las tangentes quedan debajo de la curva",
                        "Porque Euler siempre subestima cuando la solución es creciente",
                        "Porque el primer paso tiene pendiente 0 y Euler nunca recupera ese error",
                    ],
                    "correct": 0,
                },
                "answer": "Porque la solución es cóncava hacia arriba en [0, 1] y las tangentes quedan debajo de la curva",
            },
        ],
        "hints": [
            "Armá una tabla con `x_n`, `y_n`, pendiente `2·x_n·y_n` e `y_(n+1) = y_n + 0.25·pendiente`.",
            "Separando variables: `dy/y = 2x dx` → `ln|y| = x² + C`. Usá `y(0) = 1` para hallar `C`.",
            "Para la concavidad calculá `y''` derivando `y' = 2xy` (o derivando la solución exacta).",
        ],
        "solution": [
            "Paso 1: `(0, 1)`, pendiente `2·0·1 = 0` → `y₁ = 1`. Paso 2: `(0.25, 1)`, pendiente `0.5` → `y₂ = 1 + 0.25·0.5 = 1.125`.",
            "Paso 3: `(0.5, 1.125)`, pendiente `2·0.5·1.125 = 1.125` → `y₃ = 1.125 + 0.28125 = 1.40625`.",
            "Paso 4: `(0.75, 1.40625)`, pendiente `2·0.75·1.40625 = 2.109375` → `y₄ = 1.40625 + 0.52734375 = 1.93359375 ≈ 1.9336`.",
            "Exacta: `dy/y = 2x dx` → `ln|y| = x² + C`; con `y(0) = 1`, `C = 0` → `y = e^(x²)`. Entonces `y(1) = e ≈ 2.71828`.",
            "Error: `2.71828 − 1.93359 = 0.78469 ≈ 0.785` (casi un 29 % del valor real: el paso es grande para una función que crece tan rápido).",
            "Concavidad: `y'' = (e^(x²))'' = (2 + 4x²)·e^(x²) > 0`. Curva cóncava hacia arriba → cada tangente queda por debajo → Euler subestima en cada paso y los errores se acumulan.",
            "Error típico: usar siempre la pendiente del punto inicial (que es 0) y obtener `y(1) ≈ 1`.",
        ],
    },
    # ==================== c2-parametricas-vectores ====================
    {
        "id": "c2-parametricas-vectores-1",
        "node": "c2-parametricas-vectores",
        "kind": "problem",
        "level": 1,
        "title": "Un tiro libre en paramétricas",
        "statement": (
            "Una pelota pateada en una canchita de Lanús sigue `x(t) = 12t`, `y(t) = 16t − 5t²` "
            "(`x`, `y` en metros, `t` en segundos; se toma `g = 10 m/s²` y se desprecia el rozamiento con el aire)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la rapidez con la que sale la pelota (en `t = 0`)? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "m/s"},
                "answer": "20 m/s",
            },
            {
                "prompt": "b) ¿Cuál es la pendiente `dy/dx` de la trayectoria en `t = 1 s`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.5, "tolerance": 0, "unit": ""},
                "answer": "0.5",
            },
            {
                "prompt": "c) ¿Cuál es la rapidez mínima de la pelota durante el vuelo? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": "m/s"},
                "answer": "12 m/s",
            },
        ],
        "hints": [
            "Velocidad: `v(t) = ⟨x'(t), y'(t)⟩`; rapidez `|v| = √(x'² + y'²)`.",
            "La componente horizontal es constante; la rapidez es mínima cuando la vertical se anula.",
        ],
        "solution": [
            "`x'(t) = 12`, `y'(t) = 16 − 10t`, así `v(t) = ⟨12, 16 − 10t⟩`.",
            "a) `v(0) = ⟨12, 16⟩` → `|v(0)| = √(144 + 256) = √400 = 20 m/s`.",
            "b) En `t = 1`: `dy/dx = y'(1)/x'(1) = (16 − 10)/12 = 6/12 = 0.5`.",
            "c) `|v(t)|² = 144 + (16 − 10t)²` es mínimo cuando `16 − 10t = 0`, o sea `t = 1.6 s` (la altura máxima). Ahí `|v| = √144 = 12 m/s`.",
            "Error típico: decir que en la altura máxima la rapidez es 0; solo se anula la componente vertical, la horizontal sigue valiendo 12 m/s.",
        ],
    },
    {
        "id": "c2-parametricas-vectores-2",
        "node": "c2-parametricas-vectores",
        "kind": "problem",
        "level": 2,
        "title": "Tangentes y concavidad de una curva paramétrica",
        "statement": "Analizá la curva paramétrica `x(t) = t² − 2t`, `y(t) = t³ − 12t`, con `t ∈ ℝ`.",
        "parts": [
            {
                "prompt": "a) ¿En qué puntos `(x, y)` la curva tiene tangente horizontal?",
                "check": {
                    "type": "choice",
                    "options": [
                        "(0, −16) y (8, 16)",
                        "(0, 16) y (8, −16)",
                        "(−1, −11) solamente",
                        "(0, −16) solamente",
                    ],
                    "correct": 0,
                },
                "answer": "(0, −16) y (8, 16)",
            },
            {
                "prompt": "b) La curva tiene un único punto con tangente vertical. ¿Cuál es su ordenada `y`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -11, "tolerance": 0, "unit": ""},
                "answer": "−11 (el punto es (−1, −11), en t = 1)",
            },
            {
                "prompt": "c) ¿Cuánto vale `d²y/dx²` en `t = 3`? Podés responder con una fracción o con el decimal exacto. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.65625, "tolerance": 0, "unit": ""},
                "answer": "21/32 = 0.65625",
            },
        ],
        "hints": [
            "Horizontal: `dy/dt = 0` con `dx/dt ≠ 0`. Vertical: `dx/dt = 0` con `dy/dt ≠ 0`.",
            "`d²y/dx² = [d/dt (dy/dx)] / (dx/dt)`, NO `y''(t)/x''(t)`.",
        ],
        "solution": [
            "`x'(t) = 2t − 2`, `y'(t) = 3t² − 12`.",
            "a) `y' = 0` → `t² = 4` → `t = ±2` (y ahí `x' = 2` o `−6`, no nulo). `t = 2`: `(4 − 4, 8 − 24) = (0, −16)`; `t = −2`: `(4 + 4, −8 + 24) = (8, 16)`.",
            "b) `x' = 0` → `t = 1` (con `y'(1) = −9 ≠ 0`). Punto: `(1 − 2, 1 − 12) = (−1, −11)`.",
            "c) `dy/dx = (3t² − 12)/(2t − 2)`. Por la regla del cociente: `d/dt (dy/dx) = [6t(2t − 2) − 2(3t² − 12)]/(2t − 2)² = (6t² − 12t + 24)/(2t − 2)²`.",
            "En `t = 3`: `(54 − 36 + 24)/4² = 42/16 = 21/8`. Dividimos por `x'(3) = 4`: `d²y/dx² = 21/32 = 0.65625` (cóncava hacia arriba ahí).",
            "Error típico: calcular `y''(3)/x''(3) = 18/2 = 9`, que no es la concavidad de la curva.",
        ],
    },
    {
        "id": "c2-parametricas-vectores-3",
        "node": "c2-parametricas-vectores",
        "kind": "problem",
        "level": 3,
        "title": "El recorrido de un dron",
        "statement": (
            "Un dron que releva un campo en la provincia de Buenos Aires se mueve en un plano según "
            "`r(t) = ⟨t³ − 3t, 3t²⟩` (en metros, con `t` en segundos), entre `t = 0` y `t = 2`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué distancia recorre el dron entre `t = 0` y `t = 2`? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 14, "tolerance": 0, "unit": "m"},
                "answer": "14 m",
            },
            {
                "prompt": "b) ¿Cuál es el módulo de su desplazamiento entre `t = 0` y `t = 2`? Redondeá a 2 decimales. Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 12.17, "tolerance": 0.001, "unit": "m"},
                "answer": "12.17 m (√148 = 2√37)",
            },
            {
                "prompt": "c) ¿Qué rapidez tiene el dron en el único instante `t > 0` en que su trayectoria tiene tangente vertical? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": "m/s"},
                "answer": "6 m/s (en t = 1 s)",
            },
        ],
        "hints": [
            "Calculá `x'² + y'²` y fijate que es un cuadrado perfecto.",
            "El desplazamiento es `r(2) − r(0)`; la distancia recorrida es `∫ |v(t)| dt`. No son lo mismo.",
            "Tangente vertical: `x'(t) = 0` con `y'(t) ≠ 0`.",
        ],
        "solution": [
            "`v(t) = ⟨3t² − 3, 6t⟩`. `|v|² = 9t⁴ − 18t² + 9 + 36t² = 9t⁴ + 18t² + 9 = 9(t² + 1)²`, así `|v(t)| = 3(t² + 1)`.",
            "a) Distancia: `∫(de 0 a 2) 3(t² + 1) dt = [t³ + 3t] de 0 a 2 = 8 + 6 = 14 m`.",
            "b) `r(0) = ⟨0, 0⟩`, `r(2) = ⟨8 − 6, 12⟩ = ⟨2, 12⟩`. Desplazamiento `|⟨2, 12⟩| = √(4 + 144) = √148 ≈ 12.17 m`.",
            "Es menor que 14 m porque el dron primero va hacia `x` negativos (en `t = 1` está en `x = −2`) y después vuelve: la trayectoria no es recta.",
            "c) `x'(t) = 3t² − 3 = 0` → `t = 1` (con `y'(1) = 6 ≠ 0`). Rapidez: `|v(1)| = 3(1 + 1) = 6 m/s` (`v(1) = ⟨0, 6⟩`, vertical, coherente con la tangente).",
            "Error típico: responder en a) el módulo del desplazamiento (12.17 m) en vez de integrar la rapidez.",
        ],
    },
    # ==================== c2-polares-areas ====================
    {
        "id": "c2-polares-areas-1",
        "node": "c2-polares-areas",
        "kind": "problem",
        "level": 1,
        "title": "Área de una rosa de tres pétalos",
        "statement": "Considerá la rosa polar `r = 2·cos(3θ)`, que tiene 3 pétalos iguales.",
        "parts": [
            {
                "prompt": "a) ¿Qué intervalo de `θ` recorre exactamente el pétalo que apunta hacia el eje x positivo?",
                "check": {
                    "type": "choice",
                    "options": [
                        "[−π/6, π/6]",
                        "[0, π/6]",
                        "[−π/3, π/3]",
                        "[0, 2π]",
                    ],
                    "correct": 0,
                },
                "answer": "[−π/6, π/6]",
            },
            {
                "prompt": "b) ¿Cuál es el área de un pétalo? Redondeá a 3 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1.047, "tolerance": 0.001, "unit": ""},
                "answer": "1.047 (valor exacto π/3)",
            },
            {
                "prompt": "c) ¿Cuál es el área total encerrada por la rosa? Redondeá a 3 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3.142, "tolerance": 0.001, "unit": ""},
                "answer": "3.142 (valor exacto π)",
            },
        ],
        "hints": [
            "Un pétalo empieza y termina donde `r = 0`: resolvé `cos(3θ) = 0` alrededor de `θ = 0`.",
            "Usá `cos²(u) = (1 + cos(2u))/2` para integrar `r² = 4cos²(3θ)`.",
        ],
        "solution": [
            "a) `r = 0` cuando `3θ = ±π/2`, o sea `θ = ±π/6`; entre esos ángulos `r > 0` y se dibuja el pétalo centrado en `θ = 0`.",
            "b) `A = (1/2)∫(de −π/6 a π/6) 4cos²(3θ) dθ = ∫(de −π/6 a π/6) (1 + cos(6θ)) dθ`.",
            "`= [θ + sen(6θ)/6] de −π/6 a π/6 = (π/6 + 0) − (−π/6 + 0) = π/3 ≈ 1.047`.",
            "c) Los 3 pétalos son iguales: `3·π/3 = π ≈ 3.142`.",
            "Error típico: integrar `(1/2)∫ r² dθ` de `0` a `2π` y obtener `2π`: con `n` impar la rosa se recorre DOS veces en `[0, 2π]` (alcanza con `[0, π]`).",
        ],
    },
    {
        "id": "c2-polares-areas-2",
        "node": "c2-polares-areas",
        "kind": "problem",
        "level": 2,
        "title": "El diagrama de un micrófono cardioide",
        "statement": (
            "El patrón de captación de un micrófono cardioide de una sala de ensayo se modela con la curva "
            "polar `r = 1 + cos(θ)` (en unidades arbitrarias)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la pendiente `dy/dx` de la curva en el punto con `θ = π/2`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1",
            },
            {
                "prompt": "b) ¿Cuál es la ecuación de la recta tangente en ese punto?",
                "check": {
                    "type": "choice",
                    "options": ["y = x + 1", "y = −x + 1", "y = 1", "y = x"],
                    "correct": 0,
                },
                "answer": "y = x + 1",
            },
            {
                "prompt": "c) ¿Cuál es el área encerrada por la cardioide? Redondeá a 3 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4.712, "tolerance": 0.001, "unit": ""},
                "answer": "4.712 (valor exacto 3π/2)",
            },
        ],
        "hints": [
            "Usá `θ` como parámetro: `x(θ) = (1 + cos θ)·cos θ`, `y(θ) = (1 + cos θ)·sen θ`, y `dy/dx = (dy/dθ)/(dx/dθ)`.",
            "Para el área, desarrollá `(1 + cos θ)²` y reemplazá `cos²θ = (1 + cos 2θ)/2`.",
        ],
        "solution": [
            "`x(θ) = cos θ + cos²θ` → `dx/dθ = −sen θ − 2·sen θ·cos θ`. `y(θ) = sen θ + sen θ·cos θ` → `dy/dθ = cos θ + cos²θ − sen²θ`.",
            "a) En `θ = π/2`: `dx/dθ = −1 − 0 = −1`, `dy/dθ = 0 + 0 − 1 = −1`. `dy/dx = (−1)/(−1) = 1`.",
            "b) El punto es `r = 1`, `θ = π/2` → `(x, y) = (0, 1)`. Recta: `y − 1 = 1·(x − 0)` → `y = x + 1`.",
            "Ojo: `dr/dθ = −sen(π/2) = −1` NO es la pendiente; usarlo daría la recta incorrecta `y = −x + 1`.",
            "c) `A = (1/2)∫(de 0 a 2π) (1 + 2cos θ + cos²θ) dθ = (1/2)∫(de 0 a 2π) (3/2 + 2cos θ + cos(2θ)/2) dθ`.",
            "Las integrales de `cos θ` y `cos 2θ` en un período completo valen 0: `A = (1/2)·(3/2)·2π = 3π/2 ≈ 4.712`.",
        ],
    },
    {
        "id": "c2-polares-areas-3",
        "node": "c2-polares-areas",
        "kind": "problem",
        "level": 3,
        "title": "Adentro del círculo, afuera de la cardioide",
        "statement": (
            "Considerá el círculo `r = 3·cos(θ)` y la cardioide `r = 1 + cos(θ)`.\n\n"
            "Se quiere el área de la región que queda **adentro del círculo y afuera de la cardioide**."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el área encerrada por el círculo `r = 3·cos(θ)`? Redondeá a 3 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 7.069, "tolerance": 0.001, "unit": ""},
                "answer": "7.069 (valor exacto 9π/4)",
            },
            {
                "prompt": "b) Sin contar el polo, ¿en qué ángulos se cortan las dos curvas (con θ entre −π y π)?",
                "check": {
                    "type": "choice",
                    "options": ["θ = ±π/3", "θ = ±π/6", "θ = ±π/2", "θ = 0 y θ = π"],
                    "correct": 0,
                },
                "answer": "θ = ±π/3",
            },
            {
                "prompt": "c) ¿Cuál es el área de la región adentro del círculo y afuera de la cardioide? Redondeá a 3 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3.142, "tolerance": 0.001, "unit": ""},
                "answer": "3.142 (valor exacto π)",
            },
        ],
        "hints": [
            "`r = 3·cos θ` es un círculo de diámetro 3 que se recorre una sola vez con `θ ∈ [−π/2, π/2]`.",
            "Igualá `3cos θ = 1 + cos θ` para hallar los cortes.",
            "Área entre curvas: `(1/2)∫ (r_ext² − r_int²) dθ`, aprovechando la simetría respecto del eje x.",
        ],
        "solution": [
            "a) El círculo se recorre una vez en `[−π/2, π/2]`: `A = (1/2)∫ 9cos²θ dθ = (9/2)·(π/2) = 9π/4 ≈ 7.069` (coincide con `π·(3/2)²`). Integrar de `0` a `2π` lo cuenta dos veces.",
            "b) `3cos θ = 1 + cos θ` → `cos θ = 1/2` → `θ = ±π/3`. Las curvas también pasan por el polo, pero con ángulos distintos.",
            "En `(−π/3, π/3)` el círculo va por afuera (`3cos θ > 1 + cos θ` porque `cos θ > 1/2`).",
            "c) `A = (1/2)∫(de −π/3 a π/3) [9cos²θ − (1 + cos θ)²] dθ = ∫(de 0 a π/3) (8cos²θ − 1 − 2cos θ) dθ` (por simetría).",
            "Con `8cos²θ = 4 + 4cos 2θ`: `∫(de 0 a π/3) (3 + 4cos 2θ − 2cos θ) dθ = [3θ + 2sen 2θ − 2sen θ] de 0 a π/3`.",
            "`= π + 2·(√3/2) − 2·(√3/2) = π ≈ 3.142`.",
            "Error típico: usar `(1/2)∫ (r_ext − r_int)² dθ`, que da `≈ 0.544`; hay que restar los cuadrados por separado.",
        ],
    },
    # ==================== c2-series-convergencia ====================
    {
        "id": "c2-series-convergencia-1",
        "node": "c2-series-convergencia",
        "kind": "problem",
        "level": 1,
        "title": "La pelota que rebota para siempre",
        "statement": (
            "Una pelota de goma se deja caer desde 2 m de altura sobre un piso firme. Después de cada pique "
            "sube hasta `3/4` de la altura desde la que cayó. Suponé que rebota indefinidamente."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué altura alcanza después del tercer pique? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 0.84375, "tolerance": 0, "unit": "m"},
                "answer": "0.84375 m (27/32 m)",
            },
            {
                "prompt": "b) ¿Qué distancia vertical total recorre la pelota (subidas y bajadas)? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 14, "tolerance": 0, "unit": "m"},
                "answer": "14 m",
            },
        ],
        "hints": [
            "Las alturas forman una sucesión geométrica de razón `3/4`.",
            "Salvo la primera caída, cada altura se recorre dos veces (subida y bajada). Usá `∑ a·rⁿ = a/(1 − r)`.",
        ],
        "solution": [
            "Altura tras el pique `n`: `h_n = 2·(3/4)ⁿ`.",
            "a) `h₃ = 2·27/64 = 27/32 = 0.84375 m`.",
            "b) Distancia: `D = 2 + 2·(h₁ + h₂ + h₃ + …) = 2 + 2·∑(n ≥ 1) 2·(3/4)ⁿ`.",
            "La geométrica `∑(n ≥ 1) 2·(3/4)ⁿ` tiene primer término `1.5` y razón `3/4` (`|r| < 1`, converge): suma `1.5/(1 − 3/4) = 6`.",
            "`D = 2 + 2·6 = 14 m`. Error típico: no duplicar las alturas de los rebotes (daría `8 m`) o duplicar también la caída inicial (daría `16 m`).",
        ],
    },
    {
        "id": "c2-series-convergencia-2",
        "node": "c2-series-convergencia",
        "kind": "problem",
        "level": 2,
        "title": "Una serie telescópica",
        "statement": "Considerá la serie `S = ∑(de n = 1 a ∞) 6 / (n·(n + 2))` y sus sumas parciales `S_N = ∑(de n = 1 a N) 6/(n(n + 2))`.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale `S`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4.5, "tolerance": 0, "unit": ""},
                "answer": "4.5 (9/2)",
            },
            {
                "prompt": "b) ¿Cuál es el menor `N` para el que `S − S_N < 0.1`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 59, "tolerance": 0, "unit": ""},
                "answer": "59",
            },
        ],
        "hints": [
            "Descomponé `6/(n(n + 2)) = A/n + B/(n + 2)`.",
            "Escribí los primeros términos de `S_N`: casi todo se cancela y quedan dos términos del principio y dos del final.",
        ],
        "solution": [
            "Fracciones simples: `6 = A(n + 2) + Bn`. Con `n = 0`: `A = 3`; con `n = −2`: `B = −3`. Término general: `3/n − 3/(n + 2)`.",
            "`S_N = 3·[(1 − 1/3) + (1/2 − 1/4) + (1/3 − 1/5) + … + (1/N − 1/(N + 2))]`. Se cancelan todos menos `1 + 1/2` y `−1/(N + 1) − 1/(N + 2)`.",
            "`S_N = 3·(3/2 − 1/(N + 1) − 1/(N + 2))`. Como `1/(N + 1), 1/(N + 2) → 0`: `S = 9/2 = 4.5`.",
            "b) `S − S_N = 3·(1/(N + 1) + 1/(N + 2)) < 0.1` ⇔ `1/(N + 1) + 1/(N + 2) < 1/30`.",
            "`N = 58`: `1/59 + 1/60 ≈ 0.03362 > 0.03333` ✗. `N = 59`: `1/60 + 1/61 ≈ 0.03306 < 0.03333` ✓. El menor es `N = 59`.",
            "Error típico: creer que quedan solo el primer y el último término; como el salto es de 2, sobreviven dos de cada lado.",
        ],
    },
    {
        "id": "c2-series-convergencia-3",
        "node": "c2-series-convergencia",
        "kind": "problem",
        "level": 3,
        "title": "Tres series, tres criterios",
        "statement": (
            "Estudiá estas tres series:\n\n"
            "(I) `∑(n ≥ 1) (−1)^(n+1) · n/(n² + 1)`\n\n"
            "(II) `∑(n ≥ 1) n!/nⁿ`\n\n"
            "(III) `∑(n ≥ 1) (−1)^(n+1) / n³`"
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué podés afirmar de la serie (I)?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Converge condicionalmente",
                        "Converge absolutamente",
                        "Diverge, porque ∑ n/(n² + 1) diverge",
                        "Diverge, porque su término general no tiende a 0",
                    ],
                    "correct": 0,
                },
                "answer": "Converge condicionalmente",
            },
            {
                "prompt": "b) En la serie (II), ¿cuánto vale el límite `L = lim |a_(n+1)/a_n|` de la prueba de la razón? Redondeá a 3 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.368, "tolerance": 0.002, "unit": ""},
                "answer": "0.368 (L = 1/e < 1: converge)",
            },
            {
                "prompt": "c) En la serie (III), ¿cuál es el menor número de términos `N` que garantiza, por la cota de las series alternantes, un error menor que 0.001? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": ""},
                "answer": "10",
            },
        ],
        "hints": [
            "(I): mirá primero `∑ |a_n|` (comparala con `∑ 1/n`) y después el criterio de Leibniz.",
            "(II): `(n + 1)!/n! = n + 1`, y `(n/(n + 1))ⁿ = 1/(1 + 1/n)ⁿ`.",
            "(III): el error al cortar en `N` términos es menor o igual que el primer término omitido, `1/(N + 1)³`.",
        ],
        "solution": [
            "(I) Valores absolutos: `n/(n² + 1) ≥ n/(2n²) = 1/(2n)` para `n ≥ 1`, y `∑ 1/(2n)` diverge (armónica) → NO converge absolutamente.",
            "(I) Leibniz: `b_n = n/(n² + 1) → 0`, y decrece porque `f(x) = x/(x² + 1)` tiene `f'(x) = (1 − x²)/(x² + 1)² ≤ 0` para `x ≥ 1`. Converge → **condicionalmente**.",
            "(II) `a_(n+1)/a_n = [(n + 1)!/(n + 1)^(n+1)]·[nⁿ/n!] = (n + 1)·nⁿ/(n + 1)^(n+1) = (n/(n + 1))ⁿ = 1/(1 + 1/n)ⁿ`.",
            "(II) Como `(1 + 1/n)ⁿ → e`, `L = 1/e ≈ 0.368 < 1` → converge (absolutamente).",
            "(III) Sumando `N` términos, `|error| ≤ 1/(N + 1)³`. Pedimos `1/(N + 1)³ < 0.001` ⇔ `(N + 1)³ > 1000` ⇔ `N + 1 > 10`.",
            "Con `N = 9` la cota es `1/1000`, que NO es menor que 0.001; con `N = 10` es `1/1331 ≈ 0.00075` ✓. Respuesta: `N = 10`.",
            "Error típico en (I): concluir 'converge absolutamente' porque el término tiende a 0, o 'diverge' porque la serie de valores absolutos diverge (los signos alternos la salvan).",
        ],
    },
    # ==================== c2-taylor-maclaurin ====================
    {
        "id": "c2-taylor-maclaurin-1",
        "node": "c2-taylor-maclaurin",
        "kind": "problem",
        "level": 1,
        "title": "Una raíz cuadrada sin calculadora",
        "statement": (
            "Se quiere aproximar `√4.2` con el polinomio de Taylor de grado 2 de `f(x) = √x` centrado en `a = 4`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es ese polinomio `P₂(x)`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "2 + (x − 4)/4 − (x − 4)²/64",
                        "2 + (x − 4)/4 − (x − 4)²/32",
                        "2 + (x − 4)/4 + (x − 4)²/64",
                        "2 + x/4 − x²/64",
                    ],
                    "correct": 0,
                },
                "answer": "2 + (x − 4)/4 − (x − 4)²/64",
            },
            {
                "prompt": "b) ¿Qué valor da `P₂(4.2)`? Redondeá a 5 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2.049375, "tolerance": 0.000003, "unit": ""},
                "answer": "2.04938 (exacto 2.049375; √4.2 ≈ 2.049390)",
            },
        ],
        "hints": [
            "Necesitás `f(4)`, `f'(4)` y `f''(4)`, con `f'(x) = 1/(2√x)` y `f''(x) = −1/(4·x^(3/2))`.",
            "No te olvides de dividir `f''(4)` por `2!`.",
        ],
        "solution": [
            "`f(4) = 2`; `f'(4) = 1/(2·2) = 1/4`; `f''(4) = −1/(4·8) = −1/32`.",
            "`P₂(x) = f(4) + f'(4)(x − 4) + [f''(4)/2!](x − 4)² = 2 + (x − 4)/4 − (x − 4)²/64`.",
            "En `x = 4.2`: `x − 4 = 0.2`, así `P₂(4.2) = 2 + 0.05 − 0.04/64 = 2 + 0.05 − 0.000625 = 2.049375 ≈ 2.04938`.",
            "Comparación: `√4.2 ≈ 2.0493902`; el error es `≈ 0.000015`, coherente con la cota de Lagrange `(3/8)·4^(−5/2)/3!·0.2³ ≈ 0.0000156`.",
            "Error típico: no dividir por `2!` (te da `−(x − 4)²/32` y `2.04875`) o centrar en 0, donde `√x` ni siquiera es derivable.",
        ],
    },
    {
        "id": "c2-taylor-maclaurin-2",
        "node": "c2-taylor-maclaurin",
        "kind": "problem",
        "level": 2,
        "title": "La serie de cos(x²) por sustitución",
        "statement": (
            "Sea `f(x) = cos(x²)`. Obtené su serie de Maclaurin a partir de la de `cos(u)` y usala para "
            "calcular derivadas en 0 y una integral que no tiene primitiva elemental."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuáles son los tres primeros términos no nulos de la serie de Maclaurin de `cos(x²)`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "1 − x⁴/2 + x⁸/24",
                        "1 − x²/2 + x⁴/24",
                        "1 − x⁴/2 + x⁸/4",
                        "1 + x⁴/2 + x⁸/24",
                    ],
                    "correct": 0,
                },
                "answer": "1 − x⁴/2 + x⁸/24",
            },
            {
                "prompt": "b) ¿Cuánto vale `f⁽⁸⁾(0)` (la octava derivada en 0)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1680, "tolerance": 0, "unit": ""},
                "answer": "1680",
            },
            {
                "prompt": "c) Integrando esos tres términos, ¿qué aproximación obtenés para `∫(de 0 a 1) cos(x²) dx`? Redondeá a 4 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.9046, "tolerance": 0.00005, "unit": ""},
                "answer": "0.9046 (exacto 977/1080)",
            },
        ],
        "hints": [
            "En `cos(u) = 1 − u²/2! + u⁴/4! − …` reemplazá `u = x²`.",
            "El coeficiente de `x⁸` es `f⁽⁸⁾(0)/8!`: igualalo con el de la serie.",
        ],
        "solution": [
            "`cos(u) = 1 − u²/2 + u⁴/24 − …`; con `u = x²`: `cos(x²) = 1 − x⁴/2 + x⁸/24 − x¹²/720 + …`.",
            "b) Coeficiente de `x⁸`: `f⁽⁸⁾(0)/8! = 1/24` → `f⁽⁸⁾(0) = 40320/24 = 1680`.",
            "c) `∫(de 0 a 1) (1 − x⁴/2 + x⁸/24) dx = 1 − 1/10 + 1/216 = 977/1080 ≈ 0.90463`.",
            "La serie integrada es alternante con términos decrecientes: el error es menor que el siguiente, `1/(13·720) ≈ 0.00011` (el valor real es `≈ 0.90452`).",
            "Error típico: usar la serie de `cos(x)` sin sustituir (`1 − x²/2 + x⁴/24`) o elevar mal: `(x²)⁴ = x⁸` va dividido por `4! = 24`, no por 4.",
        ],
    },
    {
        "id": "c2-taylor-maclaurin-3",
        "node": "c2-taylor-maclaurin",
        "kind": "problem",
        "level": 3,
        "title": "ln(2.2) con Taylor, cota de error e intervalo",
        "statement": (
            "Sea `f(x) = ln(x)`. Usá el polinomio de Taylor de grado 3 de `f` centrado en `a = 2` para "
            "aproximar `ln(2.2)`, tomando `ln 2 ≈ 0.693147`. Después acotá el error con el resto de Lagrange "
            "y estudiá dónde converge la serie de Taylor completa de `ln x` centrada en 2."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué valor da `P₃(2.2)`? Redondeá a 5 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.78848, "tolerance": 0.00001, "unit": ""},
                "answer": "0.78848",
            },
            {
                "prompt": "b) Con el resto de Lagrange `R₃ = f⁽⁴⁾(c)/4!·(x − 2)⁴`, ¿cuál es la mejor cota de `|ln(2.2) − P₃(2.2)|` que se obtiene acotando `|f⁽⁴⁾(c)|` para `c` en `[2, 2.2]`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.000025, "tolerance": 0, "unit": ""},
                "answer": "0.000025",
            },
            {
                "prompt": "c) ¿Cuál es el intervalo de convergencia de la serie de Taylor de `ln x` centrada en 2?",
                "check": {
                    "type": "choice",
                    "options": ["(0, 4]", "(0, 4)", "[0, 4]", "(−2, 2]"],
                    "correct": 0,
                },
                "answer": "(0, 4]",
            },
        ],
        "hints": [
            "`f'(x) = 1/x`, `f''(x) = −1/x²`, `f'''(x) = 2/x³`, `f⁽⁴⁾(x) = −6/x⁴`. Evaluá en 2 y dividí por `n!`.",
            "`|f⁽⁴⁾(c)| = 6/c⁴` es decreciente: su máximo en `[2, 2.2]` está en `c = 2`.",
            "El término general es `(−1)^(n+1)·(x − 2)ⁿ/(n·2ⁿ)`. Aplicá la razón y después probá los extremos por separado.",
        ],
        "solution": [
            "Coeficientes: `f(2) = ln 2`; `f'(2) = 1/2`; `f''(2)/2! = (−1/4)/2 = −1/8`; `f'''(2)/3! = (2/8)/6 = 1/24`. `P₃(x) = ln 2 + (x − 2)/2 − (x − 2)²/8 + (x − 2)³/24`.",
            "a) Con `x − 2 = 0.2`: `0.1 − 0.005 + 0.008/24 = 0.0953333…`; `P₃(2.2) = 0.693147 + 0.095333 = 0.788480 ≈ 0.78848` (el valor real es `ln 2.2 ≈ 0.788457`).",
            "b) `|R₃| ≤ (6/2⁴)/4! · 0.2⁴ = (0.375/24)·0.0016 = 0.015625·0.0016 = 0.000025`. El error real (`≈ 0.0000232`) la respeta ✓.",
            "c) En general `f⁽ⁿ⁾(2)/n! = (−1)^(n+1)/(n·2ⁿ)`, así la serie es `ln 2 + ∑(n ≥ 1) (−1)^(n+1)(x − 2)ⁿ/(n·2ⁿ)`. Razón: `|a_(n+1)/a_n| = (n/(n + 1))·|x − 2|/2 → |x − 2|/2 < 1` → `R = 2`, intervalo abierto `(0, 4)`.",
            "Extremo `x = 4`: `∑ (−1)^(n+1)/n`, armónica alternante → converge. Extremo `x = 0`: `∑ (−1)^(n+1)(−1)ⁿ/n = −∑ 1/n` → diverge (y además `ln 0` no existe).",
            "Intervalo de convergencia: `(0, 4]`. Error típico: dar el intervalo abierto sin analizar los extremos, o centrarlo en 0 (`(−2, 2]`).",
        ],
    },
]
