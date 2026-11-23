"""Ejercicios de Matemática: Cálculo 1 / Análisis Matemático I (temas 77-84).

Tres problemas por tema (niveles 1, 2 y 3). Los de nivel 3 apuntan a la dificultad de un parcial
de Análisis Matemático I. Todos los resultados se recalcularon numéricamente (diferencias finitas,
regla de Simpson y evaluación directa).
"""

from __future__ import annotations

EXERCISES: list[dict] = [
    # ==================== c1-limites-avanzados ====================
    {
        "id": "c1-limites-avanzados-1",
        "node": "c1-limites-avanzados",
        "kind": "problem",
        "level": 1,
        "title": "Tres límites al infinito con trampa",
        "statement": (
            "Calculá los siguientes límites. Ninguno se resuelve «reemplazando por infinito»: en cada uno "
            "aparece una forma indeterminada que hay que destrabar.\n\n"
            "1. `lim(x → +∞) [√(x² + 6x) − x]`\n"
            "2. `lim(x → −∞) (3x + 1) / √(x² + 4)`\n"
            "3. `lim(x → +∞) (eˣ + x⁵) / (2eˣ − x²)`"
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale el límite 1? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3 (racionalizando queda 6x / (√(x² + 6x) + x) → 6/2)",
            },
            {
                "prompt": "b) ¿Cuánto vale el límite 2? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -3, "tolerance": 0, "unit": ""},
                "answer": "−3 (para x < 0, √(x²) = |x| = −x)",
            },
            {
                "prompt": "c) ¿Cuánto vale el límite 3? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.5, "tolerance": 0, "unit": ""},
                "answer": "0.5 (manda eˣ arriba y abajo: 1/2)",
            },
        ],
        "hints": [
            "En el 1 tenés `∞ − ∞`: multiplicá y dividí por el conjugado `√(x² + 6x) + x`.",
            "En el 2 sacá `x²` de la raíz con cuidado: `√(x²) = |x|`, y cuando `x → −∞` eso es `−x`.",
            "En el 3 dividí todo por `eˣ` y usá la jerarquía `xⁿ ≪ eˣ`.",
        ],
        "solution": [
            "Límite 1 (forma `∞ − ∞`): multiplicamos por el conjugado: `[√(x² + 6x) − x]·[√(x² + 6x) + x] / [√(x² + 6x) + x] = (x² + 6x − x²) / [√(x² + 6x) + x] = 6x / [√(x² + 6x) + x]`.",
            "Para `x > 0`, `√(x² + 6x) = x·√(1 + 6/x)`. Dividiendo arriba y abajo por `x`: `6 / [√(1 + 6/x) + 1] → 6 / (1 + 1) = 3`.",
            "Límite 2 (forma `∞/∞`): `√(x² + 4) = |x|·√(1 + 4/x²)`. Como `x → −∞`, `|x| = −x`, entonces `(3x + 1) / √(x² + 4) = (3x + 1) / [−x·√(1 + 4/x²)]`.",
            "Dividiendo arriba y abajo por `x`: `(3 + 1/x) / [−√(1 + 4/x²)] → 3 / (−1) = −3`. Error típico: responder `+3` por escribir `√(x²) = x`.",
            "Límite 3 (forma `∞/∞`): dividimos todo por `eˣ`: `(1 + x⁵/eˣ) / (2 − x²/eˣ)`. Como la exponencial le gana a cualquier potencia, `x⁵/eˣ → 0` y `x²/eˣ → 0`.",
            "Queda `(1 + 0) / (2 − 0) = 1/2 = 0.5`.",
        ],
    },
    {
        "id": "c1-limites-avanzados-2",
        "node": "c1-limites-avanzados",
        "kind": "problem",
        "level": 2,
        "title": "Un límite trigonométrico y un sándwich",
        "statement": (
            "Calculá (con los ángulos en radianes):\n\n"
            "1. `lim(x → 0) [1 − cos(4x)] / x²`\n"
            "2. `lim(x → +∞) (6x − sen x) / (2x + 7)`\n\n"
            "No uses la Regla de L'Hôpital: resolvelos con el límite fundamental `sen(u)/u → 1` y con el "
            "Teorema del Sándwich."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale el límite 1? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": ""},
                "answer": "8 (1 − cos(4x) = 2·sen²(2x) y 2·[sen(2x)/x]² → 2·2² = 8)",
            },
            {
                "prompt": "b) ¿Cuánto vale el límite 2? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3 (sen x está acotado entre −1 y 1, así que el cociente queda encerrado entre dos funciones que tienden a 3)",
            },
        ],
        "hints": [
            "Usá la identidad `1 − cos θ = 2·sen²(θ/2)` para transformar el numerador del límite 1.",
            "En el límite 1 te queda `2·[sen(2x)/x]²`; escribí `sen(2x)/x = 2·sen(2x)/(2x)`.",
            "Para el límite 2, partí de `−1 ≤ sen x ≤ 1` y armá cotas para el cociente cuando `x > 0`.",
        ],
        "solution": [
            "Límite 1: con `1 − cos θ = 2·sen²(θ/2)` y `θ = 4x`, el numerador es `2·sen²(2x)`. Entonces `[1 − cos(4x)] / x² = 2·[sen(2x)/x]²`.",
            "`sen(2x)/x = 2·[sen(2x)/(2x)] → 2·1 = 2` cuando `x → 0`. Por lo tanto el límite es `2·2² = 8`.",
            "Verificación numérica: con `x = 0.0001`, `[1 − cos(0.0004)] / 10⁻⁸ ≈ 7.9999999`.",
            "Límite 2: como `−1 ≤ sen x ≤ 1`, tenemos `6x − 1 ≤ 6x − sen x ≤ 6x + 1`. Para `x > 0` el denominador `2x + 7` es positivo, así que dividimos sin cambiar las desigualdades: `(6x − 1)/(2x + 7) ≤ (6x − sen x)/(2x + 7) ≤ (6x + 1)/(2x + 7)`.",
            "Las dos cotas son cocientes de polinomios de grado 1: ambas tienden a `6/2 = 3` cuando `x → +∞`.",
            "Por el Teorema del Sándwich, el límite 2 vale `3`. Error típico: decir que `sen x` «no tiene límite» y que entonces el cociente tampoco; lo que importa es que está acotado y queda dividido por algo que crece.",
        ],
    },
    {
        "id": "c1-limites-avanzados-3",
        "node": "c1-limites-avanzados",
        "kind": "problem",
        "level": 3,
        "title": "Ajustar una función partida y aplicar el TVI",
        "statement": (
            "Sea `f` la función definida por\n\n"
            "- `f(x) = sen(a·x) / x` si `x < 0`\n"
            "- `f(0) = 3`\n"
            "- `f(x) = b·(√(x + 1) − 1) / x` si `x > 0`\n\n"
            "donde `a` y `b` son constantes reales. Se quiere que `f` sea continua en `x = 0`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué valor tiene que tener a? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3 (el límite por izquierda es a y tiene que ser f(0) = 3)",
            },
            {
                "prompt": "b) ¿Qué valor tiene que tener b? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""},
                "answer": "6 (racionalizando, el límite por derecha es b/2 = 3)",
            },
            {
                "prompt": "c) Con esos valores, f es continua en [0, 8]. ¿Cuál de estas afirmaciones GARANTIZA el Teorema del Valor Intermedio en ese intervalo?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Existe algún c en (0, 8) con f(c) = 2",
                        "Existe algún c en (0, 8) con f(c) = 1",
                        "Existe algún c en (0, 8) con f(c) = 0",
                        "f(4) = 9/4, el promedio entre f(0) y f(8)",
                    ],
                    "correct": 0,
                },
                "answer": "Existe algún c en (0, 8) con f(c) = 2 (porque f(0) = 3 y f(8) = 3/2, y 2 está entre ambos)",
            },
        ],
        "hints": [
            "Continuidad en 0: los dos límites laterales tienen que valer `f(0) = 3`.",
            "Por izquierda armá `a·[sen(ax)/(ax)]`. Por derecha multiplicá por el conjugado `√(x + 1) + 1`.",
            "Para el TVI calculá `f(0)` y `f(8)`; el teorema solo asegura los valores que quedan ENTRE esos dos.",
        ],
        "solution": [
            "Límite por izquierda: si `a ≠ 0`, `sen(ax)/x = a·[sen(ax)/(ax)] → a·1 = a` (si `a = 0` la función vale 0 y el límite sería 0). Para que coincida con `f(0) = 3` hace falta **a = 3**.",
            "Límite por derecha: multiplicando por el conjugado, `(√(x + 1) − 1)/x = [(x + 1) − 1] / [x·(√(x + 1) + 1)] = 1 / (√(x + 1) + 1)`.",
            "Entonces `f(x) = b / (√(x + 1) + 1) → b / (1 + 1) = b/2` cuando `x → 0⁺`. Igualando `b/2 = 3` → **b = 6**.",
            "Con `b = 6`, para `x > 0` la función es `f(x) = 6 / (√(x + 1) + 1)`, continua. Valores en los bordes: `f(0) = 3` y `f(8) = 6 / (3 + 1) = 3/2`.",
            "TVI: como `f` es continua en `[0, 8]` y `3/2 < 2 < 3`, existe `c ∈ (0, 8)` con `f(c) = 2` (de hecho `√(c + 1) = 2` → `c = 3`).",
            "Las otras opciones son falsas: `1` y `0` no están entre `3/2` y `3` (en `x > 0` siempre `f(x) > 0`, y `f(x) = 1` recién pasa en `x = 24`); y `f(4) = 6/(√5 + 1) ≈ 1.854 ≠ 9/4`: el TVI no dice nada sobre el valor en el punto medio.",
        ],
    },
    # ==================== c1-derivadas-reglas ====================
    {
        "id": "c1-derivadas-reglas-1",
        "node": "c1-derivadas-reglas",
        "kind": "problem",
        "level": 1,
        "title": "Recta tangente con raíces y potencias negativas",
        "statement": (
            "Sea `f(x) = 3√x − 4/x`, definida para `x > 0`. Se quiere la recta tangente a la gráfica de `f` "
            "en el punto de abscisa `x = 4`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la derivada de f?",
                "check": {
                    "type": "choice",
                    "options": [
                        "f'(x) = 3 / (2√x) + 4 / x²",
                        "f'(x) = 3 / (2√x) − 4 / x²",
                        "f'(x) = 3 / √x + 4 / x²",
                        "f'(x) = 3 / (2√x) + 4 / x",
                    ],
                    "correct": 0,
                },
                "answer": "f'(x) = 3 / (2√x) + 4 / x²",
            },
            {
                "prompt": "b) ¿Cuánto vale la pendiente de la tangente en x = 4? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1 (3/4 + 1/4)",
            },
            {
                "prompt": "c) ¿En qué ordenada corta esa recta tangente al eje y? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1 (la tangente es y = x + 1)",
            },
        ],
        "hints": [
            "Escribí `f(x) = 3·x^(1/2) − 4·x^(−1)` y aplicá la regla de la potencia a cada término.",
            "La recta tangente es `y = f(4) + f'(4)·(x − 4)`.",
        ],
        "solution": [
            "Reescribimos con potencias: `f(x) = 3x^(1/2) − 4x^(−1)`.",
            "Derivamos: `(3x^(1/2))' = 3·(1/2)·x^(−1/2) = 3/(2√x)` y `(−4x^(−1))' = −4·(−1)·x^(−2) = +4/x²`. Entonces `f'(x) = 3/(2√x) + 4/x²`.",
            "Ojo con el signo: el «menos» de `−4/x` y el «menos» del exponente `−1` se cancelan (el distractor `− 4/x²` sale de olvidarse uno de los dos).",
            "Pendiente: `f'(4) = 3/(2·2) + 4/16 = 3/4 + 1/4 = 1`.",
            "Punto de tangencia: `f(4) = 3·2 − 4/4 = 6 − 1 = 5`, o sea `(4, 5)`.",
            "Recta: `y = 5 + 1·(x − 4) = x + 1`. Corta al eje y en **1**.",
        ],
    },
    {
        "id": "c1-derivadas-reglas-2",
        "node": "c1-derivadas-reglas",
        "kind": "problem",
        "level": 2,
        "title": "Cociente, producto y tangentes horizontales",
        "statement": (
            "Considerá las funciones `g(x) = x / (x² + 4)` y `h(x) = (x² − 3)·eˣ`, definidas en todos los reales."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la derivada de g?",
                "check": {
                    "type": "choice",
                    "options": [
                        "g'(x) = (4 − x²) / (x² + 4)²",
                        "g'(x) = (x² − 4) / (x² + 4)²",
                        "g'(x) = 1 / (2x)",
                        "g'(x) = (3x² + 4) / (x² + 4)²",
                    ],
                    "correct": 0,
                },
                "answer": "g'(x) = (4 − x²) / (x² + 4)²",
            },
            {
                "prompt": "b) ¿Cuánto vale g'(1)? Respondé solo con el número (en decimal o como fracción).",
                "check": {"type": "numeric", "value": 0.12, "tolerance": 0, "unit": ""},
                "answer": "0.12 (3/25)",
            },
            {
                "prompt": "c) La gráfica de h tiene tangente horizontal en dos puntos. ¿Cuál es la abscisa POSITIVA de esos puntos? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1 (h'(x) = eˣ(x + 3)(x − 1); los puntos son x = −3 y x = 1)",
            },
        ],
        "hints": [
            "Cociente: `(f/g)' = (f'g − fg') / g²`; el orden del numerador importa.",
            "Producto: `(u·v)' = u'v + uv'` con `u = x² − 3` y `v = eˣ`. Sacá `eˣ` de factor común.",
            "Tangente horizontal significa `h'(x) = 0`, y `eˣ` nunca vale 0.",
        ],
        "solution": [
            "Cociente con numerador `x` (derivada 1) y denominador `x² + 4` (derivada `2x`): `g'(x) = [1·(x² + 4) − x·2x] / (x² + 4)² = (4 − x²) / (x² + 4)²`.",
            "Distractores: `(x² − 4)/(…)²` invierte el orden del numerador (cambia el signo); `1/(2x)` deriva arriba y abajo por separado; `(3x² + 4)/(…)²` suma en vez de restar.",
            "`g'(1) = (4 − 1) / (1 + 4)² = 3/25 = 0.12`.",
            "Producto: `h'(x) = 2x·eˣ + (x² − 3)·eˣ = eˣ·(x² + 2x − 3) = eˣ·(x + 3)·(x − 1)`.",
            "Como `eˣ > 0` siempre, `h'(x) = 0` ⇔ `(x + 3)(x − 1) = 0` ⇔ `x = −3` o `x = 1`.",
            "La abscisa positiva es **1** (ahí `h(1) = −2e`). Error típico: derivar el producto como `2x·eˣ` y concluir que solo hay tangente horizontal en `x = 0`.",
        ],
    },
    {
        "id": "c1-derivadas-reglas-3",
        "node": "c1-derivadas-reglas",
        "kind": "problem",
        "level": 3,
        "title": "Pegar dos tramos sin esquina",
        "statement": (
            "Sea `f(x) = x² + a·x` si `x ≤ 1`, y `f(x) = b·√x` si `x > 1`, donde `a` y `b` son constantes "
            "reales.\n\n"
            "Hallá `a` y `b` para que `f` sea **derivable** en `x = 1` (justificá con las derivadas laterales "
            "calculadas como límites del cociente incremental)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale a? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -3, "tolerance": 0, "unit": ""},
                "answer": "−3",
            },
            {
                "prompt": "b) ¿Cuánto vale b? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -2, "tolerance": 0, "unit": ""},
                "answer": "−2",
            },
            {
                "prompt": "c) Con esos valores, ¿en qué ordenada corta al eje y la recta tangente a f en x = 1? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -1, "tolerance": 0, "unit": ""},
                "answer": "−1 (la tangente es y = −x − 1)",
            },
        ],
        "hints": [
            "Derivable implica continua: primero pedí que los dos tramos den lo mismo en `x = 1`.",
            "Después igualá la derivada lateral izquierda (`2x + a` en `x = 1`) con la derecha (`b/(2√x)` en `x = 1`).",
            "Te queda un sistema lineal de dos ecuaciones con dos incógnitas.",
        ],
        "solution": [
            "Continuidad en 1: `f(1) = 1 + a` (tramo izquierdo, que incluye x = 1) y `lim(x → 1⁺) b√x = b`. Condición: `1 + a = b`.",
            "Derivada lateral izquierda: `lim(h → 0⁻) [f(1 + h) − f(1)]/h = lim [(1 + h)² + a(1 + h) − 1 − a]/h = lim (2h + h² + ah)/h = 2 + a`.",
            "Derivada lateral derecha (usando que `f(1) = 1 + a = b`): `lim(h → 0⁺) [b√(1 + h) − b]/h = b·lim (√(1 + h) − 1)/h = b·lim 1/(√(1 + h) + 1) = b/2`.",
            "Condición de derivabilidad: `2 + a = b/2`. Reemplazando `b = 1 + a`: `2 + a = (1 + a)/2` → `4 + 2a = 1 + a` → **a = −3**, y entonces **b = −2**.",
            "Verificación: `f(1) = 1 − 3 = −2 = −2·√1` ✓; derivada izquierda `2 − 3 = −1`, derecha `−2/(2·1) = −1` ✓.",
            "Tangente en `(1, −2)` con pendiente `−1`: `y = −2 − (x − 1) = −x − 1`. Corta al eje y en **−1**.",
            "Error típico: pedir solo que coincidan las derivadas (`2 + a = b/2`) sin exigir continuidad; ese sistema tiene infinitas soluciones y la mayoría da una función con salto.",
        ],
    },
    # ==================== c1-cadena-implicita ====================
    {
        "id": "c1-cadena-implicita-1",
        "node": "c1-cadena-implicita",
        "kind": "problem",
        "level": 1,
        "title": "Tres capas de regla de la cadena",
        "statement": (
            "Considerá las funciones `f(x) = e^(sen(2x))`, `g(x) = √(3x² + 4)` y `h(x) = sen²(3x)` "
            "(ángulos en radianes)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es f'(x)?",
                "check": {
                    "type": "choice",
                    "options": [
                        "2·cos(2x)·e^(sen(2x))",
                        "cos(2x)·e^(sen(2x))",
                        "e^(2·cos(2x))",
                        "2·e^(cos(2x))",
                    ],
                    "correct": 0,
                },
                "answer": "2·cos(2x)·e^(sen(2x))",
            },
            {
                "prompt": "b) ¿Cuánto vale g'(2)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1.5, "tolerance": 0, "unit": ""},
                "answer": "1.5 (g'(x) = 3x / √(3x² + 4) → 6/4)",
            },
            {
                "prompt": "c) ¿Cuánto vale h'(π/12)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3 (h'(x) = 6·sen(3x)·cos(3x) = 3·sen(6x))",
            },
        ],
        "hints": [
            "Identificá las capas de afuera hacia adentro y multiplicá la derivada de cada una, evaluada en lo que tiene adentro.",
            "`h(x) = [sen(3x)]²`: la capa de afuera es «elevar al cuadrado», la del medio es seno y la de adentro es `3x`.",
        ],
        "solution": [
            "`f`: afuera `e^u` (derivada `e^u`), medio `u = sen(v)` (derivada `cos v`), adentro `v = 2x` (derivada 2). Producto: `f'(x) = e^(sen(2x))·cos(2x)·2`.",
            "Los distractores salen de olvidarse el factor 2 de adentro, o de «derivar el exponente dentro de la e» en vez de multiplicar.",
            "`g = (3x² + 4)^(1/2)`: `g'(x) = (1/2)(3x² + 4)^(−1/2)·6x = 3x / √(3x² + 4)`. En `x = 2`: `6 / √16 = 6/4 = 1.5`.",
            "`h = [sen(3x)]²`: `h'(x) = 2·sen(3x)·cos(3x)·3 = 6·sen(3x)·cos(3x) = 3·sen(6x)`.",
            "En `x = π/12`: `6x = π/2`, así que `h'(π/12) = 3·sen(π/2) = 3`.",
        ],
    },
    {
        "id": "c1-cadena-implicita-2",
        "node": "c1-cadena-implicita",
        "kind": "problem",
        "level": 2,
        "title": "Tangentes a una elipse inclinada",
        "statement": (
            "La curva `x² + x·y + y² = 7` es una elipse con los ejes girados. El punto `P = (1, 2)` pertenece "
            "a la curva. Usá derivación implícita (no despejes y)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale dy/dx en P? Respondé solo con el número (en decimal o como fracción).",
                "check": {"type": "numeric", "value": -0.8, "tolerance": 0, "unit": ""},
                "answer": "−0.8 (−4/5)",
            },
            {
                "prompt": "b) ¿En qué ordenada corta al eje y la recta tangente en P? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2.8, "tolerance": 0, "unit": ""},
                "answer": "2.8 (la tangente es y = −0.8x + 2.8)",
            },
            {
                "prompt": "c) La elipse corta al semieje x positivo en un punto Q. ¿Cuál es la pendiente de la tangente en Q? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -2, "tolerance": 0, "unit": ""},
                "answer": "−2 (Q = (√7, 0))",
            },
        ],
        "hints": [
            "Derivá cada término respecto de x: el término `x·y` es un producto, y cada `y` que derivás aporta un factor `dy/dx`.",
            "Agrupá los términos con `dy/dx` y despejá: te queda `dy/dx = −(2x + y)/(x + 2y)`.",
            "Q está sobre el eje x, así que tiene `y = 0`; buscá su abscisa en la ecuación de la curva.",
        ],
        "solution": [
            "Comprobamos P: `1 + 1·2 + 4 = 7` ✓.",
            "Derivando respecto de x: `2x + (1·y + x·y') + 2y·y' = 0` (el término `xy` va por regla del producto).",
            "Agrupando: `y'·(x + 2y) = −(2x + y)` → `dy/dx = −(2x + y)/(x + 2y)`. En P: `−(2 + 2)/(1 + 4) = −4/5 = −0.8`.",
            "Tangente en P: `y = 2 − 0.8·(x − 1) = −0.8x + 2.8`. Ordenada al origen: **2.8**.",
            "Q: con `y = 0`, `x² = 7` → `x = √7` (tomamos el positivo). Pendiente: `−(2√7 + 0)/(√7 + 0) = −2`.",
            "Error típico: derivar `x·y` como `1·y'` (o como `y`) en lugar de `y + x·y'`; con eso la pendiente en P da mal.",
        ],
    },
    {
        "id": "c1-cadena-implicita-3",
        "node": "c1-cadena-implicita",
        "kind": "problem",
        "level": 3,
        "title": "Derivadas de una inversa y derivación logarítmica",
        "statement": (
            "Sea `f(x) = x³ + 2x + 1`. Como `f'(x) = 3x² + 2 > 0`, `f` es estrictamente creciente y tiene "
            "inversa `g = f⁻¹`, que es derivable dos veces. No se puede despejar `g` con una fórmula sencilla, "
            "pero se pueden calcular sus derivadas en puntos concretos.\n\n"
            "Además, se considera `p(x) = xˣ` para `x > 0`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale g'(4)? Respondé solo con el número (en decimal o como fracción).",
                "check": {"type": "numeric", "value": 0.2, "tolerance": 0, "unit": ""},
                "answer": "0.2 (f(1) = 4 y f'(1) = 5 → 1/5)",
            },
            {
                "prompt": "b) ¿Cuánto vale g''(4)? Respondé solo con el número (en decimal o como fracción).",
                "check": {"type": "numeric", "value": -0.048, "tolerance": 0, "unit": ""},
                "answer": "−0.048 (−6/125)",
            },
            {
                "prompt": "c) ¿Cuánto vale p'(2)? Redondeá a 2 decimales y respondé solo con el número.",
                "check": {"type": "numeric", "value": 6.7726, "tolerance": 0.001, "unit": ""},
                "answer": "6.77 (p'(x) = xˣ·(ln x + 1) → 4·(ln 2 + 1))",
            },
        ],
        "hints": [
            "Primero buscá qué `x` cumple `f(x) = 4` (probá con enteros chicos).",
            "Derivá dos veces la identidad `f(g(x)) = x` respecto de x y despejá `g''`.",
            "Para `xˣ` tomá logaritmo: `ln p = x·ln x`, y derivá implícitamente.",
        ],
        "solution": [
            "`f(1) = 1 + 2 + 1 = 4`, así que `g(4) = 1`. Además `f'(1) = 3 + 2 = 5`.",
            "Derivando `f(g(x)) = x`: `f'(g(x))·g'(x) = 1` → `g'(4) = 1/f'(1) = 1/5 = 0.2`.",
            "Derivando otra vez (producto + cadena): `f''(g(x))·[g'(x)]² + f'(g(x))·g''(x) = 0` → `g''(x) = −f''(g(x))·[g'(x)]² / f'(g(x))`.",
            "Con `f''(x) = 6x` → `f''(1) = 6`: `g''(4) = −6·(1/5)² / 5 = −6/125 = −0.048`. (Que dé negativa tiene sentido: `f` es convexa para `x > 0`, y su inversa es cóncava ahí.)",
            "`p(x) = xˣ`: no es potencia (el exponente varía) ni exponencial (la base varía). Tomando logaritmo: `ln p = x·ln x`. Derivando implícitamente: `p'/p = ln x + x·(1/x) = ln x + 1`.",
            "Entonces `p'(x) = xˣ·(ln x + 1)` y `p'(2) = 4·(ln 2 + 1) ≈ 4·1.6931 = 6.7726 ≈ 6.77`.",
            "Errores típicos: derivar `xˣ` como `x·xˣ⁻¹` (regla de la potencia) o como `xˣ·ln x` (regla de la exponencial); cada una olvida la mitad.",
        ],
    },
    # ==================== c1-aplicaciones-contexto ====================
    {
        "id": "c1-aplicaciones-contexto-1",
        "node": "c1-aplicaciones-contexto",
        "kind": "problem",
        "level": 1,
        "title": "Un carrito que va, vuelve y vuelve a ir",
        "statement": (
            "Un carrito se mueve sobre un riel recto. Su posición, en metros, es "
            "`x(t) = t³ − 9t² + 24t`, con `t` en segundos y `0 ≤ t ≤ 5`."
        ),
        "parts": [
            {
                "prompt": "a) ¿En qué instante se detiene por PRIMERA vez? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "s"},
                "answer": "2 s (v(t) = 3(t − 2)(t − 4))",
            },
            {
                "prompt": "b) ¿En qué intervalos de tiempo aumenta su rapidez?",
                "check": {
                    "type": "choice",
                    "options": [
                        "En (2, 3) y en (4, 5)",
                        "En (0, 2) y en (4, 5)",
                        "En (3, 5)",
                        "En (2, 4)",
                    ],
                    "correct": 0,
                },
                "answer": "En (2, 3) y en (4, 5): ahí v y a tienen el mismo signo",
            },
            {
                "prompt": "c) ¿Qué distancia total recorre entre t = 0 y t = 5 s? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 28, "tolerance": 0, "unit": "m"},
                "answer": "28 m (20 + 4 + 4)",
            },
        ],
        "hints": [
            "Derivá para obtener `v(t)` y `a(t)`; factorizá `v(t)`.",
            "Hacé una tabla de signos de `v` y de `a` en los intervalos que determinan sus ceros.",
            "La distancia total suma los tramos entre cambios de sentido en valor absoluto: calculá `x` en 0, 2, 4 y 5.",
        ],
        "solution": [
            "`v(t) = x'(t) = 3t² − 18t + 24 = 3(t² − 6t + 8) = 3(t − 2)(t − 4)`. Se detiene en `t = 2 s` y `t = 4 s`; la primera vez es **2 s**.",
            "`a(t) = v'(t) = 6t − 18 = 6(t − 3)`: negativa para `t < 3` y positiva para `t > 3`.",
            "Signos: en `(0, 2)` v > 0, a < 0 (frena); en `(2, 3)` v < 0, a < 0 (acelera); en `(3, 4)` v < 0, a > 0 (frena); en `(4, 5)` v > 0, a > 0 (acelera). La rapidez aumenta en **(2, 3) y (4, 5)**.",
            "Posiciones: `x(0) = 0`, `x(2) = 8 − 36 + 48 = 20`, `x(4) = 64 − 144 + 96 = 16`, `x(5) = 125 − 225 + 120 = 20`.",
            "Distancia total: `|20 − 0| + |16 − 20| + |20 − 16| = 20 + 4 + 4 = 28 m`.",
            "Error típico: calcular `x(5) − x(0) = 20 m`, que es el desplazamiento y no la distancia recorrida.",
        ],
    },
    {
        "id": "c1-aplicaciones-contexto-2",
        "node": "c1-aplicaciones-contexto",
        "kind": "problem",
        "level": 2,
        "title": "Aproximar sin calculadora y destrabar límites",
        "statement": (
            "1. Usá la linealización de `f(x) = ∛x` en `a = 8` para estimar `∛8.12`.\n"
            "2. Calculá `lim(x → 0) (eˣ − 1 − x) / x²`.\n"
            "3. Calculá `lim(x → 0) (x − sen x) / x³` (ángulos en radianes)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué valor da la linealización para ∛8.12? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2.01, "tolerance": 0, "unit": ""},
                "answer": "2.01 (2 + (1/12)·0.12)",
            },
            {
                "prompt": "b) ¿Cuánto vale el límite 2? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.5, "tolerance": 0, "unit": ""},
                "answer": "0.5 (1/2)",
            },
            {
                "prompt": "c) ¿Cuánto vale el límite 3? Respondé con la fracción o redondeado a 3 decimales.",
                "check": {"type": "numeric", "value": 0.16666666666666666, "tolerance": 0.003, "unit": ""},
                "answer": "1/6 ≈ 0.167",
            },
        ],
        "hints": [
            "`f'(x) = 1/(3·∛(x²))`; en `x = 8`, `∛64 = 4`.",
            "Antes de cada aplicación de L'Hôpital, verificá que siga siendo `0/0`.",
            "El límite 3 necesita tres aplicaciones seguidas.",
        ],
        "solution": [
            "Linealización: `f(8) = 2`, `f'(x) = (1/3)x^(−2/3)` → `f'(8) = 1/(3·4) = 1/12`. `L(x) = 2 + (x − 8)/12` → `L(8.12) = 2 + 0.12/12 = 2.01` (el valor real es 2.00995…).",
            "Límite 2: en `x = 0` da `(1 − 1 − 0)/0 = 0/0`. L'Hôpital: `lim (eˣ − 1)/(2x)`, que sigue siendo `0/0`.",
            "Otra vez L'Hôpital: `lim eˣ/2 = 1/2 = 0.5`.",
            "Límite 3: `(0 − 0)/0` → L'Hôpital: `(1 − cos x)/(3x²)`, sigue `0/0` → `sen x/(6x)`, sigue `0/0` → `cos x/6 → 1/6`.",
            "Verificación numérica: con `x = 0.001`, `(x − sen x)/x³ ≈ 0.1666667`.",
            "Error típico: aplicar L'Hôpital derivando el cociente entero con la regla del cociente; se derivan numerador y denominador POR SEPARADO.",
        ],
    },
    {
        "id": "c1-aplicaciones-contexto-3",
        "node": "c1-aplicaciones-contexto",
        "kind": "problem",
        "level": 3,
        "title": "Tanque cónico que se llena",
        "statement": (
            "Un tanque de agua tiene forma de cono circular recto con el vértice hacia abajo: mide 6 m de "
            "altura y el radio de la boca (arriba) es de 3 m. Una bomba le carga agua a razón constante de "
            "2 m³/min. Considerá el instante en que el nivel del agua está a 2 m de altura (medidos desde el "
            "vértice)."
        ),
        "parts": [
            {
                "prompt": "a) ¿A qué velocidad sube el nivel del agua en ese instante? Redondeá a 2 decimales y respondé solo con el número en m/min.",
                "check": {"type": "numeric", "value": 0.6366, "tolerance": 0.01, "unit": "m/min"},
                "answer": "0.64 m/min (exactamente 2/π)",
            },
            {
                "prompt": "b) ¿A qué velocidad crece el radio de la superficie del agua? Redondeá a 2 decimales y respondé solo con el número en m/min.",
                "check": {"type": "numeric", "value": 0.3183, "tolerance": 0.01, "unit": "m/min"},
                "answer": "0.32 m/min (exactamente 1/π)",
            },
            {
                "prompt": "c) ¿A qué velocidad crece el área de la superficie libre del agua? Respondé solo con el número en m²/min.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "m²/min"},
                "answer": "2 m²/min",
            },
        ],
        "hints": [
            "Por semejanza de triángulos, el radio del agua es proporcional a la altura del agua: `r/h = 3/6`.",
            "Escribí el volumen de agua solo en función de `h` ANTES de derivar respecto de t; recién después reemplazá `h = 2`.",
            "La superficie libre es un círculo de radio `r`: `A = π·r²`.",
        ],
        "solution": [
            "Semejanza: `r/h = 3/6` → `r = h/2` en todo momento (vale para cualquier nivel, por eso se puede reemplazar antes de derivar).",
            "Volumen de agua: `V = (1/3)·π·r²·h = (1/3)·π·(h/2)²·h = π·h³/12`.",
            "Derivando respecto de t: `dV/dt = (π·h²/4)·dh/dt`. Con `dV/dt = 2` y `h = 2`: `2 = (π·4/4)·dh/dt` → `dh/dt = 2/π ≈ 0.64 m/min`.",
            "Radio: `r = h/2` → `dr/dt = (1/2)·dh/dt = 1/π ≈ 0.32 m/min`.",
            "Área de la superficie: `A = π·r²` → `dA/dt = 2π·r·dr/dt`. En ese instante `r = 1 m`: `dA/dt = 2π·1·(1/π) = 2 m²/min`.",
            "Error típico: reemplazar `h = 2` en `V = πh³/12` antes de derivar (queda un número y la derivada da 0), o usar el radio de la boca (3 m) en lugar del radio del agua.",
        ],
    },
    # ==================== c1-analisis-optimizacion ====================
    {
        "id": "c1-analisis-optimizacion-1",
        "node": "c1-analisis-optimizacion",
        "kind": "problem",
        "level": 1,
        "title": "Extremos absolutos en un intervalo cerrado",
        "statement": (
            "Sea `f(x) = x³ − 3x² − 9x + 5` en el intervalo cerrado `[−2, 6]`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el valor MÁXIMO absoluto de f en [−2, 6]? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 59, "tolerance": 0, "unit": ""},
                "answer": "59 (en el borde x = 6)",
            },
            {
                "prompt": "b) ¿Cuál es el valor MÍNIMO absoluto de f en [−2, 6]? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -22, "tolerance": 0, "unit": ""},
                "answer": "−22 (en x = 3)",
            },
            {
                "prompt": "c) ¿Cuántos valores c en (−2, 6) cumplen la conclusión del Teorema del Valor Medio para f en ese intervalo? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2 (c = 1 ± √(19/3), ambos dentro del intervalo)",
            },
        ],
        "hints": [
            "Los candidatos a extremo absoluto son los puntos críticos que caen en el intervalo y los dos bordes.",
            "Para el TVM, calculá la pendiente promedio `[f(6) − f(−2)]/8` y resolvé `f'(c)` igual a ese número.",
        ],
        "solution": [
            "`f'(x) = 3x² − 6x − 9 = 3(x − 3)(x + 1)`: puntos críticos `x = −1` y `x = 3`, ambos en `[−2, 6]`.",
            "Evaluamos los candidatos: `f(−2) = −8 − 12 + 18 + 5 = 3`; `f(−1) = −1 − 3 + 9 + 5 = 10`; `f(3) = 27 − 27 − 27 + 5 = −22`; `f(6) = 216 − 108 − 54 + 5 = 59`.",
            "Máximo absoluto: **59**, en el borde `x = 6` (el máximo local `f(−1) = 10` NO es el absoluto). Mínimo absoluto: **−22**, en `x = 3`.",
            "TVM: `f` es polinómica, así que es continua y derivable. Pendiente promedio: `(59 − 3)/(6 − (−2)) = 56/8 = 7`.",
            "`3c² − 6c − 9 = 7` → `3c² − 6c − 16 = 0` → `c = 1 ± √(1 + 16/3) = 1 ± √(19/3)` → `c ≈ 3.517` y `c ≈ −1.517`.",
            "Los dos están en `(−2, 6)`, así que hay **2** valores. Error típico: quedarse solo con la raíz positiva; el TVM asegura al menos uno, pero puede haber más.",
        ],
    },
    {
        "id": "c1-analisis-optimizacion-2",
        "node": "c1-analisis-optimizacion",
        "kind": "problem",
        "level": 2,
        "title": "Estudio de una cuártica",
        "statement": (
            "Hacé el estudio de `f(x) = x⁴ − 4x³` en todos los reales: puntos críticos, crecimiento, "
            "extremos locales, concavidad y puntos de inflexión."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale el mínimo local de f (el valor de f, no la abscisa)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -27, "tolerance": 0, "unit": ""},
                "answer": "−27 (en x = 3)",
            },
            {
                "prompt": "b) ¿Qué pasa en x = 0?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Es punto crítico pero no extremo: es un punto de inflexión con tangente horizontal",
                        "Es un máximo local",
                        "Es un mínimo local",
                        "No es punto crítico",
                    ],
                    "correct": 0,
                },
                "answer": "Punto crítico que no es extremo (f' no cambia de signo) y punto de inflexión con tangente horizontal",
            },
            {
                "prompt": "c) ¿En qué intervalo la gráfica es cóncava hacia abajo?",
                "check": {
                    "type": "choice",
                    "options": ["(0, 2)", "(2, +∞)", "(−∞, 0) ∪ (2, +∞)", "(0, 3)"],
                    "correct": 0,
                },
                "answer": "(0, 2)",
            },
        ],
        "hints": [
            "Factorizá `f'(x) = 4x²(x − 3)` y mirá el signo: `x²` nunca es negativo.",
            "Factorizá `f''(x) = 12x(x − 2)` y armá la tabla de signos.",
        ],
        "solution": [
            "`f'(x) = 4x³ − 12x² = 4x²(x − 3)`. Puntos críticos: `x = 0` y `x = 3`.",
            "Signo de `f'`: para `x < 0` es negativa (`4x² > 0`, `x − 3 < 0`); para `0 < x < 3` también negativa; para `x > 3` positiva. Decrece en `(−∞, 3)` y crece en `(3, +∞)`.",
            "En `x = 3`, `f'` pasa de − a +: mínimo local `f(3) = 81 − 108 = −27` (además `f''(3) = 36 > 0`). Como es el único cambio de decrecer a crecer, es también el mínimo absoluto.",
            "En `x = 0`, `f'` NO cambia de signo (es negativa a los dos lados): no hay extremo, aunque la tangente sea horizontal.",
            "`f''(x) = 12x² − 24x = 12x(x − 2)`: positiva en `(−∞, 0)`, negativa en `(0, 2)`, positiva en `(2, +∞)`. Cóncava hacia abajo en **(0, 2)**.",
            "`f''` cambia de signo en `x = 0` y en `x = 2`: inflexiones en `(0, 0)` (con tangente horizontal) y en `(2, −16)`.",
            "Error típico: afirmar que todo punto con `f'(c) = 0` es máximo o mínimo; en `x = 0` el criterio de la 2.ª derivada no decide (`f''(0) = 0`) y hay que mirar el signo de `f'`.",
        ],
    },
    {
        "id": "c1-analisis-optimizacion-3",
        "node": "c1-analisis-optimizacion",
        "kind": "problem",
        "level": 3,
        "title": "La lata más barata",
        "statement": (
            "Una fábrica de conservas de Mendoza quiere hacer latas cilíndricas cerradas (con tapa y fondo) "
            "de volumen `500π cm³` (≈ 1571 cm³). El material de la tapa y del fondo es más grueso y cuesta "
            "$1 por cm², mientras que el de la pared lateral cuesta $0,50 por cm². Se desprecian los "
            "solapamientos y desperdicios. Se busca el radio `r` y la altura `h` que minimizan el costo de "
            "material de cada lata."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el radio óptimo? Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "cm"},
                "answer": "5 cm",
            },
            {
                "prompt": "b) ¿Cuál es la altura óptima? Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "cm"},
                "answer": "20 cm",
            },
            {
                "prompt": "c) ¿Cuál es el costo mínimo de material por lata? Redondeá a 2 decimales y respondé solo con el número en $.",
                "check": {"type": "numeric", "value": 471.24, "tolerance": 0.001, "unit": "$"},
                "answer": "471.24 $ (exactamente 150π)",
            },
        ],
        "hints": [
            "Costo = 1 × (área de tapa + fondo) + 0,5 × (área lateral). Escribilo con `r` y `h`.",
            "Usá el volumen `π·r²·h = 500π` para despejar `h` y dejar el costo solo en función de `r`.",
            "Derivá, igualá a cero y confirmá que es un mínimo (por ejemplo con la 2.ª derivada).",
        ],
        "solution": [
            "Áreas: tapa + fondo `= 2πr²`; lateral `= 2πr·h`. Costo: `C = 1·2πr² + 0,5·2πr·h = 2πr² + πr·h`.",
            "Restricción: `πr²h = 500π` → `h = 500/r²`. Entonces `C(r) = 2πr² + πr·(500/r²) = 2πr² + 500π/r`, con `r > 0`.",
            "`C'(r) = 4πr − 500π/r² = 0` → `4r³ = 500` → `r³ = 125` → **r = 5 cm**.",
            "`C''(r) = 4π + 1000π/r³ > 0` para todo `r > 0`: es un mínimo, y como es el único punto crítico en `(0, +∞)` es el mínimo absoluto.",
            "Altura: `h = 500/25 = 20 cm` (la lata óptima es «alta»: `h = 4r`, porque las tapas son más caras).",
            "Costo mínimo: `C(5) = 2π·25 + 500π/5 = 50π + 100π = 150π ≈ 471.24` pesos.",
            "Verificación: con `r = 4`, `C = 32π + 125π = 157π`; con `r = 6`, `C = 72π + 83.3π ≈ 155.3π`; ambos mayores que `150π`. Error típico: usar la misma tarifa para todo y obtener `h = 2r`.",
        ],
    },
    # ==================== c1-integrales-tfc ====================
    {
        "id": "c1-integrales-tfc-1",
        "node": "c1-integrales-tfc",
        "kind": "problem",
        "level": 1,
        "title": "Rectángulos contra la integral exacta",
        "statement": (
            "Se quiere el área bajo `f(x) = x² + 1` entre `x = 0` y `x = 2`. Primero se aproxima con una suma de "
            "Riemann de 4 rectángulos de igual ancho, tomando la altura en el extremo DERECHO de cada "
            "subintervalo; después se calcula el valor exacto con el Teorema Fundamental del Cálculo."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la suma de Riemann? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 5.75, "tolerance": 0, "unit": ""},
                "answer": "5.75",
            },
            {
                "prompt": "b) ¿Cuánto vale la integral exacta? Respondé con la fracción o redondeado a 3 decimales.",
                "check": {"type": "numeric", "value": 4.666666666666667, "tolerance": 0.001, "unit": ""},
                "answer": "14/3 ≈ 4.667",
            },
            {
                "prompt": "c) ¿Por qué la suma de Riemann da más que el valor exacto?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Porque f es creciente en [0, 2]: la altura del extremo derecho es la mayor de cada subintervalo",
                        "Porque f es cóncava hacia arriba, y eso siempre hace que cualquier suma de Riemann sobreestime",
                        "Porque con 4 rectángulos cualquier suma de Riemann da más que la integral",
                        "Porque la integral exacta no cuenta el área por encima de y = 1",
                    ],
                    "correct": 0,
                },
                "answer": "Porque f es creciente en [0, 2]: cada rectángulo usa la altura máxima de su subintervalo",
            },
        ],
        "hints": [
            "`Δx = (2 − 0)/4 = 0.5`; los extremos derechos son 0.5, 1, 1.5 y 2.",
            "Una primitiva de `x² + 1` es `x³/3 + x`.",
        ],
        "solution": [
            "`Δx = 0.5`. Alturas en los extremos derechos: `f(0.5) = 1.25`, `f(1) = 2`, `f(1.5) = 3.25`, `f(2) = 5`.",
            "Suma: `0.5·(1.25 + 2 + 3.25 + 5) = 0.5·11.5 = 5.75`.",
            "Exacta por TFC: `F(x) = x³/3 + x` → `F(2) − F(0) = 8/3 + 2 = 14/3 ≈ 4.667`.",
            "Como `f' = 2x ≥ 0` en `[0, 2]`, `f` es creciente: en cada subintervalo el valor del extremo derecho es el máximo, y cada rectángulo «se pasa» de la curva. Por eso `5.75 > 4.667`.",
            "La concavidad no decide esto (una suma por la izquierda de la misma función subestima). Con más rectángulos la diferencia baja: la suma por derecha con `n` rectángulos se acerca a `14/3` cuando `n → ∞`.",
        ],
    },
    {
        "id": "c1-integrales-tfc-2",
        "node": "c1-integrales-tfc",
        "kind": "problem",
        "level": 2,
        "title": "Sustitución y TFC con límite variable",
        "statement": (
            "1. Hallá una primitiva de `x / √(x² + 9)` y calculá `∫(de 0 a 4) x / √(x² + 9) dx`.\n"
            "2. Sea `G(x) = ∫(de 1 a x²) √(t + 5) dt`. Calculá `G'(2)` sin calcular la integral."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es una primitiva de x / √(x² + 9)?",
                "check": {
                    "type": "choice",
                    "options": [
                        "√(x² + 9)",
                        "(1/2)·√(x² + 9)",
                        "ln(x² + 9)",
                        "x² / (2√(x² + 9))",
                    ],
                    "correct": 0,
                },
                "answer": "√(x² + 9)",
            },
            {
                "prompt": "b) ¿Cuánto vale ∫(de 0 a 4) x / √(x² + 9) dx? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2 (√25 − √9)",
            },
            {
                "prompt": "c) ¿Cuánto vale G'(2)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": ""},
                "answer": "12 (G'(x) = √(x² + 5)·2x)",
            },
        ],
        "hints": [
            "Probá `u = x² + 9`, `du = 2x dx`; ojo con el factor 1/2 y con el exponente `−1/2`.",
            "Si `F' = f`, entonces `G(x) = F(x²) − F(1)`; derivá con regla de la cadena.",
        ],
        "solution": [
            "Con `u = x² + 9`, `du = 2x dx` → `x dx = du/2`: `∫ x/√(x² + 9) dx = (1/2)∫ u^(−1/2) du = (1/2)·2u^(1/2) + C = √(x² + 9) + C`.",
            "Comprobación derivando: `(√(x² + 9))' = 2x / (2√(x² + 9)) = x/√(x² + 9)` ✓. El distractor `(1/2)√(x² + 9)` olvida que al integrar `u^(−1/2)` aparece un factor 2; `ln(x² + 9)` sería la primitiva (salvo factor) de `x/(x² + 9)`, sin raíz.",
            "Integral definida: `[√(x² + 9)]` de 0 a 4 `= √25 − √9 = 5 − 3 = 2`.",
            "TFC parte 1 con límite superior `x²`: `G(x) = F(x²) − F(1)` con `F' = √(t + 5)`, así que `G'(x) = F'(x²)·(x²)' = √(x² + 5)·2x`.",
            "`G'(2) = √(4 + 5)·4 = 3·4 = 12`. Error típico: responder `√9 = 3`, olvidando el factor `2x` de la regla de la cadena.",
        ],
    },
    {
        "id": "c1-integrales-tfc-3",
        "node": "c1-integrales-tfc",
        "kind": "problem",
        "level": 3,
        "title": "Reconstruir una función a partir de una integral",
        "statement": (
            "Existen una función continua `f` (definida para `x > 0`) y una constante `a > 0` tales que, para "
            "todo `x > 0`,\n\n"
            "`6 + ∫(de a a x) f(t) / t² dt = 2√x`.\n\n"
            "Hallá `f` y `a`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale a? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": ""},
                "answer": "9 (en x = a la integral es 0: 6 = 2√a)",
            },
            {
                "prompt": "b) ¿Cuánto vale f(4)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": ""},
                "answer": "8 (f(x) = x^(3/2))",
            },
            {
                "prompt": "c) ¿Cuánto vale ∫(de 0 a 4) f(x) dx? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 12.8, "tolerance": 0, "unit": ""},
                "answer": "12.8 (64/5)",
            },
        ],
        "hints": [
            "Derivá los dos miembros respecto de x usando el TFC parte 1.",
            "Para hallar `a`, elegí un valor de x que haga desaparecer la integral.",
        ],
        "solution": [
            "Derivando ambos lados respecto de x: la constante 6 da 0 y, por el TFC parte 1, `d/dx ∫(a a x) f(t)/t² dt = f(x)/x²`. A la derecha, `(2√x)' = 1/√x`.",
            "Entonces `f(x)/x² = 1/√x` → `f(x) = x²/x^(1/2) = x^(3/2)`.",
            "Para `a`: reemplazamos `x = a`; la integral de `a` a `a` vale 0, así que `6 = 2√a` → `√a = 3` → **a = 9**.",
            "Verificación: `∫(9 a x) t^(3/2)/t² dt = ∫(9 a x) t^(−1/2) dt = [2√t] de 9 a x = 2√x − 6`, y `6 + (2√x − 6) = 2√x` ✓.",
            "`f(4) = 4^(3/2) = (√4)³ = 8`.",
            "`∫(0 a 4) x^(3/2) dx = [(2/5)x^(5/2)] de 0 a 4 = (2/5)·32 = 64/5 = 12.8`.",
            "Error típico: derivar `2√x` como `√x` o como `1/(2√x)`; con eso `f` sale mal y `a` igual da 9, así que conviene verificar al final.",
        ],
    },
    # ==================== c1-ecuaciones-diferenciales ====================
    {
        "id": "c1-ecuaciones-diferenciales-1",
        "node": "c1-ecuaciones-diferenciales",
        "kind": "problem",
        "level": 1,
        "title": "Separar, integrar y usar la condición inicial",
        "statement": (
            "Resolvé el problema de valor inicial `dy/dx = (2x + 1) / (2y)`, con `y(0) = 2` (buscá la solución "
            "con `y > 0`)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la solución?",
                "check": {
                    "type": "choice",
                    "options": [
                        "y = √(x² + x + 4)",
                        "y = √(x² + x) + 2",
                        "y = x² + x + 2",
                        "y = √(2x² + 2x + 4)",
                    ],
                    "correct": 0,
                },
                "answer": "y = √(x² + x + 4)",
            },
            {
                "prompt": "b) ¿Cuánto vale y(3)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4 (√(9 + 3 + 4) = √16)",
            },
            {
                "prompt": "c) ¿Cuál es la pendiente de la solución en x = 3? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.875, "tolerance": 0, "unit": ""},
                "answer": "0.875 (7/8)",
            },
        ],
        "hints": [
            "Pasá `2y` multiplicando: `2y dy = (2x + 1) dx`.",
            "Poné la constante de integración en un solo lado y fijala con `x = 0`, `y = 2` ANTES de despejar y.",
            "Para la pendiente no hace falta derivar la solución: la ecuación diferencial ya te da `dy/dx` en cada punto `(x, y)`.",
        ],
        "solution": [
            "Separamos: `2y dy = (2x + 1) dx`.",
            "Integramos: `y² = x² + x + C`.",
            "Condición inicial: `2² = 0 + 0 + C` → `C = 4`. Entonces `y² = x² + x + 4` y, como `y > 0`, `y = √(x² + x + 4)`.",
            "Distractores: `√(x² + x) + 2` pone la constante afuera de la raíz (no cumple la ecuación); `x² + x + 2` integra solo el lado de x; `√(2x² + 2x + 4)` sale de integrar `2y` como `y²/2`.",
            "`y(3) = √(9 + 3 + 4) = √16 = 4`.",
            "Pendiente en `(3, 4)`: `dy/dx = (2·3 + 1)/(2·4) = 7/8 = 0.875`. (Comprobación derivando: `y' = (2x + 1)/(2√(x² + x + 4)) = 7/(2·4)` ✓.)",
        ],
    },
    {
        "id": "c1-ecuaciones-diferenciales-2",
        "node": "c1-ecuaciones-diferenciales",
        "kind": "problem",
        "level": 2,
        "title": "Un cultivo de bacterias",
        "statement": (
            "En un laboratorio de microbiología, un cultivo de bacterias crece con una velocidad proporcional "
            "a la cantidad presente: `dP/dt = k·P`, con `t` en horas. Al comenzar hay 1000 bacterias y a las "
            "2 h hay 4000."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la constante k? Redondeá a 3 decimales y respondé solo con el número en 1/h.",
                "check": {"type": "numeric", "value": 0.693147, "tolerance": 0.001, "unit": "1/h"},
                "answer": "0.693 1/h (k = ln 2)",
            },
            {
                "prompt": "b) ¿Cuántas bacterias hay a las 5 h? Respondé solo con el número en bacterias.",
                "check": {"type": "numeric", "value": 32000, "tolerance": 0, "unit": "bacterias"},
                "answer": "32000 bacterias",
            },
            {
                "prompt": "c) ¿Al cabo de cuántas horas el cultivo llega a 1 024 000 bacterias? Respondé solo con el número en h.",
                "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "h"},
                "answer": "10 h",
            },
        ],
        "hints": [
            "Separando variables se llega a `P(t) = P₀·e^(kt)`; usá el dato de las 2 h para despejar `k` con logaritmo.",
            "Fijate que `e^k` resulta un número muy simple: eso te permite escribir `P(t)` sin la e.",
        ],
        "solution": [
            "Separando: `dP/P = k dt` → `ln P = kt + C` → `P(t) = A·e^(kt)`. Con `P(0) = 1000`: `A = 1000`.",
            "`P(2) = 1000·e^(2k) = 4000` → `e^(2k) = 4` → `2k = ln 4` → `k = ln 4 / 2 = ln 2 ≈ 0.693 1/h`.",
            "Como `e^k = 2`, el modelo es `P(t) = 1000·2^t`: el cultivo se duplica cada hora.",
            "`P(5) = 1000·2⁵ = 32 000` bacterias.",
            "`1000·2^t = 1 024 000` → `2^t = 1024 = 2¹⁰` → `t = 10 h`.",
            "Error típico: suponer crecimiento lineal (de 1000 a 4000 en 2 h → +1500 por hora) y predecir 8500 a las 5 h.",
        ],
    },
    {
        "id": "c1-ecuaciones-diferenciales-3",
        "node": "c1-ecuaciones-diferenciales",
        "kind": "problem",
        "level": 3,
        "title": "La pava que se enfría",
        "statement": (
            "Apagás el fuego cuando el agua de la pava está a 100°C. La cocina está a 20°C constantes y el "
            "agua se enfría según la Ley de Newton: `dT/dt = −k·(T − 20)`, con `t` en minutos y `k > 0`. "
            "A los 5 minutos el termómetro marca 80°C. Querés usar el agua cuando esté a 65°C."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale k? Redondeá a 4 decimales y respondé solo con el número en 1/min.",
                "check": {"type": "numeric", "value": 0.057536, "tolerance": 0.001, "unit": "1/min"},
                "answer": "0.0575 1/min (k = ln(4/3)/5)",
            },
            {
                "prompt": "b) ¿Cuántos minutos después de apagar el fuego el agua llega a 65°C? Respondé solo con el número en min.",
                "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "min"},
                "answer": "10 min",
            },
            {
                "prompt": "c) ¿Qué temperatura tiene el agua a los 15 minutos? Respondé solo con el número en °C.",
                "check": {"type": "numeric", "value": 53.75, "tolerance": 0, "unit": "°C"},
                "answer": "53.75 °C",
            },
        ],
        "hints": [
            "Separá variables con la diferencia `T − 20`: `dT/(T − 20) = −k dt`.",
            "Vas a llegar a `T(t) = 20 + 80·e^(−kt)`. Con el dato de los 5 min, mirá qué fracción de la diferencia inicial queda cada 5 minutos.",
            "Para los 65°C, simplificá `45/80` y escribilo como una potencia de `3/4`.",
        ],
        "solution": [
            "Separando: `dT/(T − 20) = −k dt` → `ln|T − 20| = −kt + C` → `T − 20 = A·e^(−kt)`. Con `T(0) = 100`: `A = 80`, así que `T(t) = 20 + 80·e^(−kt)`.",
            "Dato: `T(5) = 80` → `80·e^(−5k) = 60` → `e^(−5k) = 3/4` → `k = ln(4/3)/5 ≈ 0.28768/5 ≈ 0.0575 1/min`.",
            "Como `e^(−5k) = 3/4`, se puede escribir `T(t) = 20 + 80·(3/4)^(t/5)`: cada 5 minutos la diferencia con la cocina se multiplica por 3/4.",
            "65°C: `80·(3/4)^(t/5) = 45` → `(3/4)^(t/5) = 45/80 = 9/16 = (3/4)²` → `t/5 = 2` → `t = 10 min`.",
            "A los 15 min: `T(15) = 20 + 80·(3/4)³ = 20 + 80·27/64 = 20 + 33.75 = 53.75°C`.",
            "Control de sentido: la temperatura baja cada vez más lento y tiende a 20°C sin alcanzarla. Error típico: suponer que baja 20°C cada 5 min (lineal) y predecir 65°C a los 8.75 min.",
        ],
    },
    # ==================== c1-aplicaciones-integrales ====================
    {
        "id": "c1-aplicaciones-integrales-1",
        "node": "c1-aplicaciones-integrales",
        "kind": "problem",
        "level": 1,
        "title": "Una bici que frena y retrocede",
        "statement": (
            "Una ciclista se mueve sobre una calle recta con velocidad `v(t) = 6 − 2t` (en m/s), para "
            "`0 ≤ t ≤ 5` s. Velocidad positiva significa avanzar y negativa, retroceder."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es su desplazamiento entre t = 0 y t = 5 s? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "m"},
                "answer": "5 m",
            },
            {
                "prompt": "b) ¿Qué distancia total recorre en ese lapso? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 13, "tolerance": 0, "unit": "m"},
                "answer": "13 m (9 de ida y 4 de vuelta)",
            },
            {
                "prompt": "c) ¿Cuál es el valor promedio de la velocidad v(t) en [0, 5]? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": "m/s"},
                "answer": "1 m/s",
            },
        ],
        "hints": [
            "Desplazamiento `= ∫ v dt`; distancia `= ∫ |v| dt`.",
            "Buscá cuándo `v(t) = 0` y partí la integral en ese instante.",
        ],
        "solution": [
            "Desplazamiento: `∫(0 a 5) (6 − 2t) dt = [6t − t²] de 0 a 5 = 30 − 25 = 5 m`.",
            "`v(t) = 0` en `t = 3 s`: avanza en `[0, 3]` y retrocede en `[3, 5]`.",
            "Ida: `∫(0 a 3) (6 − 2t) dt = 18 − 9 = 9 m`. Vuelta: `∫(3 a 5) (6 − 2t) dt = (30 − 25) − (18 − 9) = −4 m`.",
            "Distancia total: `9 + |−4| = 13 m`. (Comprobación: `9 − 4 = 5 m` es el desplazamiento.)",
            "Valor promedio de v: `(1/(5 − 0))·∫(0 a 5) v dt = 5/5 = 1 m/s`.",
            "Ojo: la RAPIDEZ promedio sería `13/5 = 2.6 m/s`, distinta del promedio de la velocidad.",
        ],
    },
    {
        "id": "c1-aplicaciones-integrales-2",
        "node": "c1-aplicaciones-integrales",
        "kind": "problem",
        "level": 2,
        "title": "Dos parábolas que se cruzan",
        "statement": (
            "Considerá las parábolas `y = 4 − x²` y `y = x² − 2x`."
        ),
        "parts": [
            {
                "prompt": "a) ¿En qué abscisas se cortan?",
                "check": {
                    "type": "choice",
                    "options": ["x = −1 y x = 2", "x = 1 y x = −2", "x = 0 y x = 2", "x = −2 y x = 2"],
                    "correct": 0,
                },
                "answer": "x = −1 y x = 2",
            },
            {
                "prompt": "b) ¿Cuánto vale el área de la región encerrada entre las dos curvas? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": ""},
                "answer": "9",
            },
            {
                "prompt": "c) ¿Cuánto vale el área total entre las dos curvas desde x = 0 hasta x = 3? Respondé con la fracción o redondeado a 3 decimales.",
                "check": {"type": "numeric", "value": 10.333333333333334, "tolerance": 0.001, "unit": ""},
                "answer": "31/3 ≈ 10.333",
            },
        ],
        "hints": [
            "Igualá las dos expresiones y resolvé la cuadrática.",
            "Probá un valor intermedio (por ejemplo `x = 0`) para saber cuál va arriba.",
            "En `[0, 3]` las curvas se cruzan en `x = 2`: partí la integral ahí y cambiá el orden de la resta.",
        ],
        "solution": [
            "`4 − x² = x² − 2x` → `2x² − 2x − 4 = 0` → `x² − x − 2 = 0` → `(x − 2)(x + 1) = 0` → `x = −1` y `x = 2`.",
            "En `x = 0`: `4 − 0 = 4` contra `0`: arriba va `4 − x²`. Diferencia: `(4 − x²) − (x² − 2x) = −2x² + 2x + 4`.",
            "Primitiva: `H(x) = −2x³/3 + x² + 4x`. `H(2) = −16/3 + 4 + 8 = 20/3`; `H(−1) = 2/3 + 1 − 4 = −7/3`.",
            "Área encerrada: `20/3 − (−7/3) = 27/3 = 9`.",
            "En `[0, 3]`: de 0 a 2 arriba va `4 − x²` → `H(2) − H(0) = 20/3`. De 2 a 3 arriba va `x² − 2x` (en `x = 3`: 3 contra −5) → `∫(2 a 3) (2x² − 2x − 4) dx = −[H(3) − H(2)] = −(3 − 20/3) = 11/3`.",
            "Área total: `20/3 + 11/3 = 31/3 ≈ 10.333`. Error típico: integrar `−2x² + 2x + 4` de 0 a 3 sin partir, lo que da `20/3 − 11/3 = 3` (resta el pedazo donde se invierten).",
        ],
    },
    {
        "id": "c1-aplicaciones-integrales-3",
        "node": "c1-aplicaciones-integrales",
        "kind": "problem",
        "level": 3,
        "title": "Una pieza torneada con hueco",
        "statement": (
            "Sea R la región del primer cuadrante encerrada entre la recta `y = 2x` y la parábola `y = x²`. "
            "Se calcula su área y los volúmenes de los sólidos que se generan al hacerla girar alrededor de "
            "cada eje coordenado (por el método de arandelas)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale el área de R? Respondé con la fracción o redondeado a 3 decimales.",
                "check": {"type": "numeric", "value": 1.3333333333333333, "tolerance": 0.001, "unit": ""},
                "answer": "4/3 ≈ 1.333",
            },
            {
                "prompt": "b) ¿Cuánto vale el volumen al girar R alrededor del eje x? Redondeá a 2 decimales y respondé solo con el número.",
                "check": {"type": "numeric", "value": 13.404128655316, "tolerance": 0.001, "unit": ""},
                "answer": "13.40 (exactamente 64π/15)",
            },
            {
                "prompt": "c) ¿Cuánto vale el volumen al girar R alrededor del eje y? Redondeá a 2 decimales y respondé solo con el número.",
                "check": {"type": "numeric", "value": 8.377580409572781, "tolerance": 0.001, "unit": ""},
                "answer": "8.38 (exactamente 8π/3)",
            },
        ],
        "hints": [
            "Las curvas se cortan en `x = 0` y `x = 2`; entre ellas la recta va arriba.",
            "Alrededor del eje x, cada arandela tiene radio exterior `2x` y radio interior `x²`: área `π[(2x)² − (x²)²]`.",
            "Alrededor del eje y, cortá en rebanadas horizontales: despejá x de cada curva en función de y (`x = y/2` y `x = √y`) y fijate cuál queda más lejos del eje.",
        ],
        "solution": [
            "Cortes: `2x = x²` → `x(x − 2) = 0` → `x = 0` y `x = 2` (puntos `(0, 0)` y `(2, 4)`). En `x = 1`: `2 > 1`, la recta va arriba.",
            "Área: `∫(0 a 2) (2x − x²) dx = [x² − x³/3] de 0 a 2 = 4 − 8/3 = 4/3 ≈ 1.333`.",
            "Eje x: `V = π∫(0 a 2) [(2x)² − (x²)²] dx = π∫(0 a 2) (4x² − x⁴) dx = π[4x³/3 − x⁵/5] de 0 a 2 = π(32/3 − 32/5) = 64π/15 ≈ 13.40`.",
            "Error típico en el eje x: usar `π(R − r)² = π(2x − x²)²`, que da `16π/15 ≈ 3.35`.",
            "Eje y: para cada `y ∈ [0, 4]`, la región va de `x = y/2` (recta) a `x = √y` (parábola), y `√y ≥ y/2` en ese rango. Radio exterior `√y`, interior `y/2`.",
            "`V = π∫(0 a 4) [(√y)² − (y/2)²] dy = π∫(0 a 4) (y − y²/4) dy = π[y²/2 − y³/12] de 0 a 4 = π(8 − 16/3) = 8π/3 ≈ 8.38`.",
            "Los dos volúmenes son distintos aunque la región sea la misma: depende de lo lejos que esté el área del eje de giro.",
        ],
    },
]
