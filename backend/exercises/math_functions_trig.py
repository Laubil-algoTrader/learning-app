"""Ejercicios de Matemática: funciones (Álgebra 2, temas 58-62) y Trigonometría (temas 63-68).

Tres problemas por tema (niveles 1, 2 y 3). Los de nivel 3 apuntan a la dificultad de un parcial
de ingreso a Ingeniería.
"""

from __future__ import annotations

EXERCISES: list[dict] = [
    # ==================== a2-transformaciones-funciones ====================
    {
        "id": "a2-transformaciones-funciones-1",
        "node": "a2-transformaciones-funciones",
        "kind": "problem",
        "level": 1,
        "title": "Seguirle el rastro a un punto",
        "statement": (
            "El punto `P = (1, 5)` pertenece a la gráfica de una función `f`. Se define la función "
            "`g(x) = −2·f(x + 3) + 4`.\n\n"
            "Llamá `P'` al punto de la gráfica de `g` que corresponde a `P` (es decir, el punto en el que "
            "`g` usa el valor `f(1) = 5`)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la abscisa (coordenada x) de P'? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -2, "tolerance": 0, "unit": ""},
                "answer": "−2 (hace falta x + 3 = 1)",
            },
            {
                "prompt": "b) ¿Cuál es la ordenada (coordenada y) de P'? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -6, "tolerance": 0, "unit": ""},
                "answer": "−6 (−2·5 + 4)",
            },
            {
                "prompt": "c) ¿Qué secuencia de transformaciones lleva la gráfica de f a la de g?",
                "check": {
                    "type": "choice",
                    "options": [
                        "3 a la izquierda; estiramiento vertical ×2 con reflexión sobre el eje X; 4 hacia arriba",
                        "3 a la derecha; estiramiento vertical ×2 con reflexión sobre el eje X; 4 hacia arriba",
                        "3 a la izquierda; estiramiento vertical ×2 con reflexión sobre el eje Y; 4 hacia arriba",
                        "4 a la izquierda; estiramiento vertical ×2 con reflexión sobre el eje X; 3 hacia arriba",
                    ],
                    "correct": 0,
                },
                "answer": "3 a la izquierda; estiramiento vertical ×2 con reflexión sobre el eje X; 4 hacia arriba",
            },
        ],
        "hints": [
            "Lo de ADENTRO del paréntesis actúa sobre la x (y al revés de lo que parece); lo de AFUERA actúa sobre la y (directo).",
            "Para que `g` use `f(1)`, lo que está adentro de `f` tiene que valer 1: planteá `x + 3 = 1`.",
        ],
        "solution": [
            "Horizontal: `g` evalúa a `f` en `x + 3`. Para que aparezca `f(1)` hace falta `x + 3 = 1`, o sea `x = −2`. El punto se corrió **3 a la izquierda**.",
            "Vertical: en `x = −2`, `g(−2) = −2·f(1) + 4 = −2·5 + 4 = −10 + 4 = −6`.",
            "Entonces `P' = (−2, −6)`.",
            "Lectura general con la regla `a·f(x − h) + k`: `x + 3 = x − (−3)` → `h = −3` (izquierda); `a = −2` → estira ×2 y refleja sobre el eje X (el signo menos está AFUERA); `k = +4` → sube 4.",
            "Error típico: leer `x + 3` como «3 a la derecha», o creer que el menos de afuera refleja sobre el eje Y (eso lo haría `f(−x)`).",
        ],
    },
    {
        "id": "a2-transformaciones-funciones-2",
        "node": "a2-transformaciones-funciones",
        "kind": "problem",
        "level": 2,
        "title": "Par, impar o ninguna de las dos",
        "statement": (
            "Considerá las funciones `f(x) = x⁴ − 3x² + 2`, `g(x) = x³ − 4x` y `h(x) = x³ − 4x + 1`, "
            "todas definidas en los reales.\n\n"
            "Además, de otras dos funciones solo se sabe que `p` es **par**, que `q` es **impar**, y que "
            "`p(2) = 5` y `q(2) = −3`."
        ),
        "parts": [
            {
                "prompt": "a) Clasificá f, g y h según su simetría.",
                "check": {
                    "type": "choice",
                    "options": [
                        "f es par, g es impar y h no es ni par ni impar",
                        "f es par, g es impar y h es impar",
                        "f es impar, g es par y h no es ni par ni impar",
                        "f es par, g no es ni par ni impar y h es impar",
                    ],
                    "correct": 0,
                },
                "answer": "f es par, g es impar y h no es ni par ni impar",
            },
            {
                "prompt": "b) Calculá h(1) + h(−1). Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2 (h(1) = −2 y h(−1) = 4)",
            },
            {
                "prompt": "c) Calculá 3·p(−2) + q(−2). Respondé solo con el número.",
                "check": {"type": "numeric", "value": 18, "tolerance": 0, "unit": ""},
                "answer": "18 (3·5 + 3)",
            },
        ],
        "hints": [
            "Reemplazá `x` por `−x` en cada fórmula y compará el resultado con la función original y con su opuesta.",
            "Potencias pares «se comen» el signo: `(−x)⁴ = x⁴`. Potencias impares lo conservan: `(−x)³ = −x³`.",
            "Par: `p(−2) = p(2)`. Impar: `q(−2) = −q(2)`.",
        ],
        "solution": [
            "`f(−x) = (−x)⁴ − 3(−x)² + 2 = x⁴ − 3x² + 2 = f(x)` → **f es par** (simétrica respecto del eje Y).",
            "`g(−x) = (−x)³ − 4(−x) = −x³ + 4x = −(x³ − 4x) = −g(x)` → **g es impar** (simétrica respecto del origen).",
            "`h(−x) = −x³ + 4x + 1`. No coincide con `h(x) = x³ − 4x + 1` ni con `−h(x) = −x³ + 4x − 1` → **h no es ni par ni impar** (el `+1` rompe la simetría).",
            "Con números: `h(1) = 1 − 4 + 1 = −2` y `h(−1) = −1 + 4 + 1 = 4`. Como `4 ≠ −2` y `4 ≠ 2`, se confirma que no es par ni impar. La suma da `−2 + 4 = 2`.",
            "Observación: `h = g + 1`, y como `g` es impar, `g(1) + g(−1) = 0`; por eso la suma es `1 + 1 = 2`.",
            "Para `p` y `q`: `p(−2) = p(2) = 5` (par) y `q(−2) = −q(2) = −(−3) = 3` (impar). Entonces `3·p(−2) + q(−2) = 15 + 3 = 18`.",
        ],
    },
    {
        "id": "a2-transformaciones-funciones-3",
        "node": "a2-transformaciones-funciones",
        "kind": "problem",
        "level": 3,
        "title": "Inversa de una cuadrática con dominio restringido",
        "statement": (
            "Sea `f(x) = x² − 4x + 7` con dominio restringido a `x ≥ 2` (en todo ℝ la parábola no es "
            "inyectiva y no tendría inversa).\n\n"
            "Hallá la función inversa `f⁻¹`, su dominio, y evaluala."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la fórmula de f⁻¹(x)?",
                "check": {
                    "type": "choice",
                    "options": [
                        "f⁻¹(x) = 2 + √(x − 3)",
                        "f⁻¹(x) = 2 − √(x − 3)",
                        "f⁻¹(x) = 2 + √(x + 3)",
                        "f⁻¹(x) = 1 / (x² − 4x + 7)",
                    ],
                    "correct": 0,
                },
                "answer": "f⁻¹(x) = 2 + √(x − 3)",
            },
            {
                "prompt": "b) ¿Cuál es el dominio de f⁻¹?",
                "check": {
                    "type": "choice",
                    "options": ["[3, +∞)", "[2, +∞)", "[7, +∞)", "Todos los reales"],
                    "correct": 0,
                },
                "answer": "[3, +∞)",
            },
            {
                "prompt": "c) Calculá f⁻¹(12). Respondé solo con el número.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                "answer": "5 (2 + √9)",
            },
        ],
        "hints": [
            "Completá cuadrados para escribir `f(x) = (x − h)² + k`: así la `x` aparece una sola vez y se puede despejar.",
            "Al sacar raíz cuadrada aparece un `±`. La restricción `x ≥ 2` te dice con cuál de los dos signos quedarte.",
            "El dominio de `f⁻¹` es la imagen (rango) de `f`: ¿cuál es el valor mínimo de `f` en `x ≥ 2`?",
        ],
        "solution": [
            "Completamos cuadrados: `x² − 4x + 7 = (x² − 4x + 4) + 3 = (x − 2)² + 3`. El vértice es `(2, 3)` y en `x ≥ 2` la función es creciente (inyectiva).",
            "Planteamos `y = (x − 2)² + 3` y despejamos `x`: `(x − 2)² = y − 3` → `x − 2 = ±√(y − 3)`.",
            "Como `x ≥ 2`, `x − 2 ≥ 0`: corresponde el signo **+**. Queda `x = 2 + √(y − 3)`.",
            "Intercambiamos letras: `f⁻¹(x) = 2 + √(x − 3)`.",
            "Dominio de `f⁻¹` = imagen de `f`: como `(x − 2)² ≥ 0`, `f(x) ≥ 3`, así que el dominio es `[3, +∞)` (coincide con pedir `x − 3 ≥ 0` dentro de la raíz). Su imagen es `[2, +∞)`, el dominio de `f`.",
            "`f⁻¹(12) = 2 + √(12 − 3) = 2 + 3 = 5`. Verificación: `f(5) = 25 − 20 + 7 = 12`.",
            "Error típico: elegir `2 − √(x − 3)` (esa es la inversa de la OTRA rama, `x ≤ 2`) o confundir `f⁻¹` con `1/f`.",
        ],
    },
    # ==================== a2-racionales-asintotas ====================
    {
        "id": "a2-racionales-asintotas-1",
        "node": "a2-racionales-asintotas",
        "kind": "problem",
        "level": 1,
        "title": "Radiografía de una función homográfica",
        "statement": (
            "Analizá la función racional `f(x) = (3x − 6) / (2x + 8)`: buscá su valor prohibido, su "
            "comportamiento para `x` muy grande y dónde corta al eje X."
        ),
        "parts": [
            {
                "prompt": "a) ¿En qué valor de x tiene la asíntota vertical? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -4, "tolerance": 0, "unit": ""},
                "answer": "−4 (2x + 8 = 0)",
            },
            {
                "prompt": "b) ¿En qué valor de y tiene la asíntota horizontal? Respondé solo con el número (decimal o fracción).",
                "check": {"type": "numeric", "value": 1.5, "tolerance": 0, "unit": ""},
                "answer": "1.5 (= 3/2)",
            },
            {
                "prompt": "c) ¿En qué valor de x corta la gráfica al eje X (raíz de f)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2 (3x − 6 = 0)",
            },
        ],
        "hints": [
            "Asíntota vertical: cero del denominador que NO anula al numerador. Raíz: cero del numerador que no anula al denominador.",
            "Asíntota horizontal con grados iguales: cociente de los coeficientes principales.",
        ],
        "solution": [
            "Denominador: `2x + 8 = 0` → `x = −4`. En `x = −4` el numerador vale `3(−4) − 6 = −18 ≠ 0`, así que no se cancela nada: hay **asíntota vertical en `x = −4`** (y el dominio es ℝ − {−4}).",
            "Asíntota horizontal: numerador y denominador tienen grado 1, así que para `x` enorme mandan los términos líderes: `3x / 2x = 3/2`. **`y = 1.5`**.",
            "Raíz: una fracción vale 0 cuando su numerador vale 0 (y el denominador no): `3x − 6 = 0` → `x = 2`. En `x = 2` el denominador vale `12 ≠ 0`, así que es válida.",
            "Chequeo rápido con un valor grande: `f(1000) = 2994 / 2008 ≈ 1.49`, bien cerca de `1.5`.",
            "Error típico: dar como asíntota horizontal `−6/8` (cociente de los términos independientes; eso es `f(0) = −0.75`, la ordenada al origen).",
        ],
    },
    {
        "id": "a2-racionales-asintotas-2",
        "node": "a2-racionales-asintotas",
        "kind": "problem",
        "level": 2,
        "title": "Salmuera que entra a un tanque",
        "statement": (
            "Un tanque contiene inicialmente **60 L de agua pura**. Se abre una canilla por la que entra "
            "salmuera con concentración **0.4 kg de sal por litro**, a razón de **3 L por minuto**.\n\n"
            "Suponé que la mezcla se mantiene homogénea, que no sale líquido y que el tanque es lo bastante "
            "grande como para no rebalsar. Llamá `C(t)` a la concentración de sal del tanque (en kg/L) a los "
            "`t` minutos."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la concentración a los 20 minutos? Respondé solo con el número en kg/L.",
                "check": {"type": "numeric", "value": 0.2, "tolerance": 0, "unit": "kg/L"},
                "answer": "0.2 kg/L (24 kg en 120 L)",
            },
            {
                "prompt": "b) ¿A qué valor se acerca la concentración si la canilla queda abierta muchísimo tiempo (asíntota horizontal de C)? Respondé solo con el número en kg/L.",
                "check": {"type": "numeric", "value": 0.4, "tolerance": 0, "unit": "kg/L"},
                "answer": "0.4 kg/L (1.2 / 3)",
            },
            {
                "prompt": "c) ¿A los cuántos minutos la concentración llega a 0.3 kg/L? Respondé solo con el número en min.",
                "check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": "min"},
                "answer": "60 min",
            },
        ],
        "hints": [
            "Concentración = (kg de sal) / (litros totales). Escribí cada uno en función de `t`.",
            "Cada minuto entran 3 L, que traen `3 × 0.4` kg de sal. El volumen arranca en 60 L.",
            "Para c) igualá `C(t) = 0.3` y multiplicá por el denominador (que nunca es 0 para `t ≥ 0`).",
        ],
        "solution": [
            "Sal acumulada: cada minuto entran `3 L × 0.4 kg/L = 1.2 kg` → `sal(t) = 1.2·t`.",
            "Volumen total: `V(t) = 60 + 3·t` litros.",
            "Modelo racional: `C(t) = 1.2t / (60 + 3t)` (simplificando por 3: `C(t) = 0.4t / (20 + t)`).",
            "a) `C(20) = 1.2·20 / (60 + 60) = 24 / 120 = 0.2 kg/L`.",
            "b) Numerador y denominador tienen grado 1 → asíntota horizontal `y = 1.2 / 3 = 0.4 kg/L`. Tiene sentido físico: con el tiempo el agua pura inicial pesa cada vez menos y el tanque se parece a la salmuera que entra, pero nunca llega exactamente a 0.4.",
            "c) `1.2t / (60 + 3t) = 0.3` → `1.2t = 0.3·(60 + 3t) = 18 + 0.9t` → `0.3t = 18` → `t = 60 min`.",
            "Verificación: a los 60 min hay `72 kg` de sal en `240 L` → `72 / 240 = 0.3 kg/L`.",
        ],
    },
    {
        "id": "a2-racionales-asintotas-3",
        "node": "a2-racionales-asintotas",
        "kind": "problem",
        "level": 3,
        "title": "Agujero, asíntotas y raíces: análisis completo",
        "statement": (
            "Hacé el estudio completo de la función\n\n"
            "`f(x) = (3x² − 3x − 18) / (x² − 2x − 3)`\n\n"
            "indicando dominio, discontinuidades (agujeros y asíntotas verticales), asíntota horizontal y raíces."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué ocurre en los valores que anulan el denominador?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Agujero en x = 3 y asíntota vertical en x = −1",
                        "Asíntotas verticales en x = 3 y en x = −1",
                        "Agujero en x = −1 y asíntota vertical en x = 3",
                        "Agujero en x = −2 y asíntota vertical en x = −1",
                    ],
                    "correct": 0,
                },
                "answer": "Agujero en x = 3 y asíntota vertical en x = −1",
            },
            {
                "prompt": "b) ¿Cuál es la ordenada (coordenada y) del agujero? Respondé solo con el número (decimal o fracción).",
                "check": {"type": "numeric", "value": 3.75, "tolerance": 0, "unit": ""},
                "answer": "3.75 (= 15/4)",
            },
            {
                "prompt": "c) ¿Cuáles son las raíces de f y su asíntota horizontal?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Única raíz x = −2; asíntota horizontal y = 3",
                        "Raíces x = −2 y x = 3; asíntota horizontal y = 3",
                        "Única raíz x = −2; asíntota horizontal y = 6",
                        "Raíces x = −2 y x = 3; no tiene asíntota horizontal",
                    ],
                    "correct": 0,
                },
                "answer": "Única raíz x = −2; asíntota horizontal y = 3",
            },
        ],
        "hints": [
            "Antes de mirar nada, factorizá numerador y denominador (sacá factor común 3 arriba).",
            "Un factor que se cancela por completo marca un agujero; el que sobrevive abajo, una asíntota vertical.",
            "La altura del agujero se obtiene evaluando la expresión YA simplificada en ese `x`. Ojo: un valor fuera del dominio no puede ser raíz.",
        ],
        "solution": [
            "Numerador: `3x² − 3x − 18 = 3(x² − x − 6) = 3(x − 3)(x + 2)`. Denominador: `x² − 2x − 3 = (x − 3)(x + 1)`.",
            "Dominio: el denominador se anula en `x = 3` y `x = −1` → `Dom f = ℝ − {−1, 3}`.",
            "Simplificamos: `f(x) = 3(x + 2) / (x + 1)` para todo `x ≠ 3` (y `x ≠ −1`).",
            "El factor `(x − 3)` se canceló → **agujero en `x = 3`**. El factor `(x + 1)` quedó abajo y el numerador simplificado vale `3 ≠ 0` en `x = −1` → **asíntota vertical `x = −1`**.",
            "Ordenada del agujero: evaluamos la forma simplificada en `x = 3`: `3·(3 + 2) / (3 + 1) = 15/4 = 3.75`. El agujero está en `(3, 15/4)`.",
            "Asíntota horizontal: grados iguales (2 y 2) → `y = 3/1 = 3`.",
            "Raíces: el numerador original se anula en `x = 3` y `x = −2`, pero `x = 3` NO está en el dominio (ahí hay un agujero a altura 3.75, no un cero). **Única raíz: `x = −2`**.",
            "Error típico: declarar asíntota vertical en `x = 3` sin factorizar, o contar `x = 3` como raíz.",
        ],
    },
    # ==================== a2-ecuaciones-avanzadas ====================
    {
        "id": "a2-ecuaciones-avanzadas-1",
        "node": "a2-ecuaciones-avanzadas",
        "kind": "problem",
        "level": 1,
        "title": "Una ecuación radical con trampa",
        "statement": "Resolvé en los reales la ecuación `√(3x + 1) = x − 3`.",
        "parts": [
            {
                "prompt": "a) Después de elevar al cuadrado y resolver la cuadrática, ¿qué candidatos aparecen?",
                "check": {
                    "type": "choice",
                    "options": ["x = 1 y x = 8", "x = −2 y x = 5", "x = −1 y x = −8"],
                    "correct": 0,
                },
                "answer": "x = 1 y x = 8",
            },
            {
                "prompt": "b) ¿Cuál es la única solución de la ecuación original? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": ""},
                "answer": "8 (x = 1 es una solución extraña)",
            },
        ],
        "hints": [
            "La raíz ya está aislada: elevá ambos miembros al cuadrado. Cuidado con `(x − 3)²`: es un binomio, tiene doble producto.",
            "Probá cada candidato en la ecuación ORIGINAL: el lado derecho `x − 3` tiene que dar un número no negativo.",
        ],
        "solution": [
            "Elevamos al cuadrado: `3x + 1 = (x − 3)² = x² − 6x + 9`.",
            "Pasamos todo a un miembro: `0 = x² − 9x + 8`.",
            "Factorizamos (dos números que multiplicados den 8 y sumados 9): `(x − 1)(x − 8) = 0` → candidatos `x = 1` y `x = 8`.",
            "Verificamos `x = 1`: `√(3 + 1) = 2`, pero `1 − 3 = −2`. Como `2 ≠ −2`, **es extraña** (una raíz cuadrada nunca da negativo).",
            "Verificamos `x = 8`: `√(24 + 1) = 5` y `8 − 3 = 5`. Cumple.",
            "Única solución: `x = 8`. Error típico: desarrollar `(x − 3)² = x² − 9` (da los candidatos falsos −2 y 5) o entregar los dos candidatos sin verificar.",
        ],
    },
    {
        "id": "a2-ecuaciones-avanzadas-2",
        "node": "a2-ecuaciones-avanzadas",
        "kind": "problem",
        "level": 2,
        "title": "Dos bombas para el tanque australiano",
        "statement": (
            "En un campo de La Pampa, dos bombas trabajando juntas llenan un tanque australiano en **6 horas**. "
            "Se sabe que la bomba A, sola, tardaría **5 horas menos** que la bomba B sola.\n\n"
            "Suponé que cada bomba entrega un caudal constante."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto tarda la bomba A sola en llenar el tanque? Respondé solo con el número en h.",
                "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "h"},
                "answer": "10 h",
            },
            {
                "prompt": "b) ¿Cuánto tarda la bomba B sola? Respondé solo con el número en h.",
                "check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": "h"},
                "answer": "15 h",
            },
        ],
        "hints": [
            "Se suman las VELOCIDADES de llenado (fracción de tanque por hora), nunca los tiempos.",
            "Si A tarda `t` horas, B tarda `t + 5`. Planteá `1/t + 1/(t + 5) = 1/6`.",
            "Multiplicá toda la ecuación por `6·t·(t + 5)` para sacar los denominadores; te queda una cuadrática.",
        ],
        "solution": [
            "Llamamos `t` al tiempo de A sola (en horas); B sola tarda `t + 5`. En una hora A llena `1/t` del tanque, B llena `1/(t + 5)` y juntas `1/6`.",
            "Ecuación: `1/t + 1/(t + 5) = 1/6`, con `t ≠ 0` y `t ≠ −5`.",
            "Multiplicamos por `6t(t + 5)`: `6(t + 5) + 6t = t(t + 5)` → `12t + 30 = t² + 5t`.",
            "Ordenamos: `t² − 7t − 30 = 0` → `(t − 10)(t + 3) = 0` → `t = 10` o `t = −3`.",
            "Un tiempo negativo no tiene sentido: descartamos `t = −3`. Entonces **A tarda 10 h** y **B tarda 15 h**.",
            "Verificación: `1/10 + 1/15 = 3/30 + 2/30 = 5/30 = 1/6`. Juntas, 6 horas.",
            "Chequeo de sentido común: trabajando juntas tardan menos que la más rápida sola (6 < 10).",
        ],
    },
    {
        "id": "a2-ecuaciones-avanzadas-3",
        "node": "a2-ecuaciones-avanzadas",
        "kind": "problem",
        "level": 3,
        "title": "Recta secante, recta tangente",
        "statement": (
            "Considerá la parábola `y = x² − 4x + 5` y la familia de rectas paralelas `y = 2x + k`, "
            "donde `k` es un número real.\n\n"
            "Según el valor de `k`, la recta corta a la parábola en dos puntos, en uno solo (tangente) o en ninguno."
        ),
        "parts": [
            {
                "prompt": "a) Para k = −3, la recta corta a la parábola en dos puntos. ¿Cuál es la ordenada (y) del punto de MAYOR abscisa? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                "answer": "5 (el punto es (4, 5))",
            },
            {
                "prompt": "b) ¿Para qué valor de k la recta es tangente a la parábola? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -4, "tolerance": 0, "unit": ""},
                "answer": "−4",
            },
            {
                "prompt": "c) ¿Cuál es la ordenada (y) del punto de tangencia? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2 (el punto es (3, 2))",
            },
        ],
        "hints": [
            "Igualá las dos expresiones de `y` y llevá todo a la forma `ax² + bx + c = 0` (la `k` queda dentro de `c`).",
            "La cantidad de puntos de cruce la decide el discriminante `Δ = b² − 4ac`: tangente significa UNA sola solución.",
            "Una vez que tengas la `x` del cruce, la `y` sale más fácil reemplazando en la recta.",
        ],
        "solution": [
            "Igualamos: `x² − 4x + 5 = 2x + k` → `x² − 6x + (5 − k) = 0`.",
            "a) Con `k = −3`: `x² − 6x + 8 = 0` → `(x − 2)(x − 4) = 0` → `x = 2` o `x = 4`.",
            "Las ordenadas salen de la recta `y = 2x − 3`: para `x = 2`, `y = 1`; para `x = 4`, `y = 5`. Puntos `(2, 1)` y `(4, 5)`; el de mayor abscisa tiene `y = 5`. (Chequeo en la parábola: `16 − 16 + 5 = 5`.)",
            "b) Tangente ⇔ solución única ⇔ `Δ = 0`: `Δ = (−6)² − 4·1·(5 − k) = 36 − 20 + 4k = 16 + 4k`.",
            "`16 + 4k = 0` → `k = −4`. (Si `k > −4` hay dos cruces; si `k < −4`, ninguno.)",
            "c) Con `k = −4`: `x² − 6x + 9 = 0` → `(x − 3)² = 0` → `x = 3` (raíz doble). En la recta: `y = 2·3 − 4 = 2`.",
            "Punto de tangencia: `(3, 2)`. Verificación en la parábola: `9 − 12 + 5 = 2`.",
        ],
    },
    # ==================== a2-circulo-unitario-ondas ====================
    {
        "id": "a2-circulo-unitario-ondas-1",
        "node": "a2-circulo-unitario-ondas",
        "kind": "problem",
        "level": 1,
        "title": "Un punto del círculo unitario en el segundo cuadrante",
        "statement": (
            "Un ángulo `θ` del **segundo cuadrante** determina sobre el círculo unitario un punto cuya "
            "abscisa es `−0.6`, es decir, `cos(θ) = −0.6`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale sen(θ)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.8, "tolerance": 0, "unit": ""},
                "answer": "0.8",
            },
            {
                "prompt": "b) ¿Cuánto vale tan(θ) = sen(θ)/cos(θ)? Respondé solo con el número (fracción o decimal redondeado a 2 decimales).",
                "check": {"type": "numeric", "value": -4 / 3, "tolerance": 0.005, "unit": ""},
                "answer": "−4/3 ≈ −1.33",
            },
            {
                "prompt": "c) ¿Cuánto vale sen(θ + 180°)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -0.8, "tolerance": 0, "unit": ""},
                "answer": "−0.8",
            },
        ],
        "hints": [
            "El punto `(cos θ, sen θ)` está sobre `x² + y² = 1`: usá `sen²θ + cos²θ = 1` y elegí el signo según el cuadrante.",
            "Sumar 180° es dar media vuelta: caés en el punto diametralmente opuesto del círculo.",
        ],
        "solution": [
            "Identidad pitagórica: `sen²θ = 1 − cos²θ = 1 − (−0.6)² = 1 − 0.36 = 0.64` → `sen θ = ±0.8`.",
            "En el 2.° cuadrante la ordenada es positiva → `sen θ = +0.8`. El punto es `(−0.6, 0.8)`.",
            "`tan θ = sen θ / cos θ = 0.8 / (−0.6) = −4/3 ≈ −1.33` (negativa, como corresponde al 2.° cuadrante).",
            "`θ + 180°` apunta al punto diametralmente opuesto: `(0.6, −0.8)`, en el 4.° cuadrante. Su ordenada es `sen(θ + 180°) = −0.8`.",
            "En general, `sen(θ + 180°) = −sen θ` y `cos(θ + 180°) = −cos θ`. Error típico: olvidar el signo del cuadrante y responder `sen θ = −0.8` o `tan θ = +4/3`.",
        ],
    },
    {
        "id": "a2-circulo-unitario-ondas-2",
        "node": "a2-circulo-unitario-ondas",
        "kind": "problem",
        "level": 2,
        "title": "La tensión del enchufe",
        "statement": (
            "La tensión de la red domiciliaria argentina (220 V eficaces) se puede modelar como\n\n"
            "`v(t) = 311·sen(100π·t)`\n\n"
            "con `v` en voltios y `t` en segundos (el argumento del seno está en radianes)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el período de la onda? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 0.02, "tolerance": 0, "unit": "s"},
                "answer": "0.02 s",
            },
            {
                "prompt": "b) ¿Cuántos ciclos completa por segundo (frecuencia)? Respondé solo con el número en Hz.",
                "check": {"type": "numeric", "value": 50, "tolerance": 0, "unit": "Hz"},
                "answer": "50 Hz",
            },
            {
                "prompt": "c) ¿Cuánto vale la tensión en el instante t = 1/600 s? Respondé solo con el número en V.",
                "check": {"type": "numeric", "value": 155.5, "tolerance": 0, "unit": "V"},
                "answer": "155.5 V",
            },
        ],
        "hints": [
            "Compará con `A·sen(B·t)`: acá `B = 100π`. El período es `T = 2π / |B|`.",
            "La frecuencia es la inversa del período: `f = 1/T`.",
            "Para c) calculá primero el ángulo `100π·t` y pasalo a grados si te resulta más cómodo (`π rad = 180°`).",
        ],
        "solution": [
            "Identificamos `A = 311 V` (valor pico) y `B = 100π rad/s`.",
            "Período: `T = 2π / B = 2π / (100π) = 1/50 = 0.02 s`.",
            "Frecuencia: `f = 1 / T = 1 / 0.02 = 50 Hz` (los 50 ciclos por segundo de la red argentina).",
            "En `t = 1/600 s`: el argumento vale `100π · (1/600) = π/6 rad = 30°`.",
            "`v = 311 · sen(30°) = 311 · 0.5 = 155.5 V`.",
            "Chequeo: `1/600 s` es la doceava parte del período (`0.02/12`), o sea `360°/12 = 30°` de ciclo. Error típico: creer que un `B` más grande alarga el período; es al revés.",
        ],
    },
    {
        "id": "a2-circulo-unitario-ondas-3",
        "node": "a2-circulo-unitario-ondas",
        "kind": "problem",
        "level": 3,
        "title": "La vuelta al mundo del parque",
        "statement": (
            "Una vuelta al mundo (noria) tiene **40 m de diámetro** y su punto más bajo está a **2 m del suelo**. "
            "Gira con velocidad constante y completa una vuelta cada **120 segundos**.\n\n"
            "Una cabina arranca en `t = 0` desde el punto más bajo. Llamá `h(t)` a su altura sobre el suelo "
            "(en metros) a los `t` segundos."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué función modela la altura de la cabina?",
                "check": {
                    "type": "choice",
                    "options": [
                        "h(t) = 22 − 20·cos((π/60)·t)",
                        "h(t) = 22 + 20·cos((π/60)·t)",
                        "h(t) = 22 − 20·cos((π/120)·t)",
                        "h(t) = 20 − 22·cos((π/60)·t)",
                    ],
                    "correct": 0,
                },
                "answer": "h(t) = 22 − 20·cos((π/60)·t)",
            },
            {
                "prompt": "b) ¿A qué altura está la cabina a los 20 segundos? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": "m"},
                "answer": "12 m",
            },
            {
                "prompt": "c) En cada vuelta, ¿durante cuántos segundos la cabina está a MÁS de 32 m de altura? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 40, "tolerance": 0, "unit": "s"},
                "answer": "40 s (entre t = 40 s y t = 80 s)",
            },
        ],
        "hints": [
            "Amplitud = radio. Línea media = altura del centro. `B = 2π / T`. Como arranca en el MÍNIMO, conviene un coseno con signo menos.",
            "Para b) el ángulo `(π/60)·20` es un ángulo notable.",
            "Para c) resolvé primero la igualdad `h(t) = 32` dentro de una vuelta (`0 ≤ t < 120`): salen dos instantes, y la cabina está más alta ENTRE ellos.",
        ],
        "solution": [
            "Amplitud = radio = `40/2 = 20 m`. Centro de la rueda (línea media): `2 + 20 = 22 m`. La altura oscila entre `2 m` y `42 m`.",
            "Período `T = 120 s` → `B = 2π/120 = π/60`.",
            "En `t = 0` la cabina está en el mínimo. Como `cos(0) = 1`, usamos `−cos`: `h(t) = 22 − 20·cos((π/60)·t)`. Chequeo: `h(0) = 22 − 20 = 2 m` y `h(60) = 22 − 20·cos(π) = 42 m`.",
            "b) `h(20) = 22 − 20·cos(π/3) = 22 − 20·0.5 = 12 m`.",
            "c) `h(t) = 32` → `22 − 20·cos((π/60)t) = 32` → `cos((π/60)t) = −1/2`.",
            "En una vuelta (`0 ≤ (π/60)t < 2π`), el coseno vale `−1/2` en `2π/3` (120°) y en `4π/3` (240°) → `t = 40 s` y `t = 80 s`.",
            "Entre esos instantes la cabina pasa por el tope (42 m en `t = 60 s`), así que está por encima de 32 m durante `80 − 40 = 40 s`.",
            "Ojo: esos 10 m superiores (de 32 m a 42 m) son apenas la cuarta parte del recorrido vertical (40 m), pero la cabina pasa ahí un tercio de la vuelta (`40/120`): cerca del tope la altura cambia más lento.",
        ],
    },
    # ==================== a2-modelado-composicion ====================
    {
        "id": "a2-modelado-composicion-1",
        "node": "a2-modelado-composicion",
        "kind": "problem",
        "level": 1,
        "title": "Dos cultivos de bacterias",
        "statement": (
            "En un laboratorio se cuenta cada hora la cantidad de bacterias de dos cultivos:\n\n"
            "**Cultivo A:** `t = 0 → 50`, `t = 1 → 200`, `t = 2 → 350`, `t = 3 → 500`.\n\n"
            "**Cultivo B:** `t = 0 → 50`, `t = 1 → 100`, `t = 2 → 200`, `t = 3 → 400`.\n\n"
            "Suponé que cada cultivo sigue creciendo con el mismo patrón que muestra su tabla."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué familia de funciones modela cada cultivo?",
                "check": {
                    "type": "choice",
                    "options": [
                        "A es lineal y B es exponencial",
                        "A es exponencial y B es lineal",
                        "Los dos son lineales",
                        "A es lineal y B es cuadrático",
                    ],
                    "correct": 0,
                },
                "answer": "A es lineal y B es exponencial",
            },
            {
                "prompt": "b) Según su modelo, ¿cuántas bacterias tendrá el cultivo B a las 6 horas? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3200, "tolerance": 0, "unit": "bacterias"},
                "answer": "3200 bacterias",
            },
            {
                "prompt": "c) ¿En qué hora entera t el cultivo B supera por primera vez al cultivo A? Respondé solo con el número en h.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "h"},
                "answer": "4 h (800 contra 650)",
            },
        ],
        "hints": [
            "En cada tabla calculá las DIFERENCIAS entre valores consecutivos y también los COCIENTES. ¿Cuál de los dos se mantiene constante?",
            "Lineal: `y = y₀ + m·t`. Exponencial: `y = y₀ · rᵗ`.",
        ],
        "solution": [
            "Cultivo A: diferencias `200 − 50 = 150`, `350 − 200 = 150`, `500 − 350 = 150` → suma constante → **lineal**: `A(t) = 50 + 150·t`.",
            "Cultivo B: diferencias `50, 100, 200` (no constantes), pero cocientes `100/50 = 2`, `200/100 = 2`, `400/200 = 2` → factor constante → **exponencial**: `B(t) = 50 · 2ᵗ`.",
            "B no es cuadrático: en una cuadrática las SEGUNDAS diferencias son constantes, y acá son `50` y `100`.",
            "b) `B(6) = 50 · 2⁶ = 50 · 64 = 3200` bacterias.",
            "c) Comparamos hora por hora: `t = 3`: `A = 500`, `B = 400` (todavía gana A). `t = 4`: `A = 50 + 600 = 650`, `B = 50 · 16 = 800` → B supera a A por primera vez en `t = 4 h`.",
            "Moraleja: una exponencial puede arrancar más lenta que una lineal, pero a la larga siempre la pasa.",
        ],
    },
    {
        "id": "a2-modelado-composicion-2",
        "node": "a2-modelado-composicion",
        "kind": "problem",
        "level": 2,
        "title": "El precio de las remeras estampadas",
        "statement": (
            "Un emprendimiento de remeras estampadas estima que, si cobra `p` **miles de pesos** por remera "
            "(con `8 ≤ p ≤ 30`), vende `q(p) = 300 − 10p` remeras por mes.\n\n"
            "Producir `q` remeras le cuesta `C(q) = 8q + 400` miles de pesos (8 mil por remera más 400 mil "
            "de gastos fijos).\n\n"
            "La ganancia mensual es **ingreso − costo**, donde el ingreso es precio × cantidad vendida y el "
            "costo se calcula sobre la cantidad que efectivamente se vende: `G(p) = p·q(p) − C(q(p))`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la ganancia mensual si cobra p = 15? Respondé solo con el número en miles de pesos.",
                "check": {"type": "numeric", "value": 650, "tolerance": 0, "unit": "miles de $"},
                "answer": "650 miles de pesos",
            },
            {
                "prompt": "b) ¿Qué precio p maximiza la ganancia? Respondé solo con el número en miles de pesos.",
                "check": {"type": "numeric", "value": 19, "tolerance": 0, "unit": "miles de $"},
                "answer": "19 miles de pesos por remera",
            },
            {
                "prompt": "c) ¿Cuál es esa ganancia máxima? Respondé solo con el número en miles de pesos.",
                "check": {"type": "numeric", "value": 810, "tolerance": 0, "unit": "miles de $"},
                "answer": "810 miles de pesos",
            },
        ],
        "hints": [
            "Para a) andá de adentro hacia afuera: primero `q(15)`, después el ingreso `15·q(15)` y el costo `C(q(15))`.",
            "Para b) escribí `G(p)` como un único polinomio en `p`: reemplazá `q` por `300 − 10p` en el ingreso y en el costo.",
            "Te queda una cuadrática con coeficiente principal negativo: el máximo está en el vértice, `p = −b/(2a)`.",
        ],
        "solution": [
            "a) `q(15) = 300 − 150 = 150` remeras. Ingreso: `15 · 150 = 2250`. Costo: `C(150) = 8·150 + 400 = 1600`. Ganancia: `2250 − 1600 = 650` miles de pesos.",
            "Ingreso en función del precio: `I(p) = p·q(p) = p(300 − 10p) = 300p − 10p²`.",
            "Costo en función del precio (composición `C(q(p))`): `8(300 − 10p) + 400 = 2800 − 80p`.",
            "Ganancia: `G(p) = 300p − 10p² − (2800 − 80p) = −10p² + 380p − 2800`. Chequeo: `G(15) = −2250 + 5700 − 2800 = 650`.",
            "b) Es una parábola hacia abajo (`a = −10`): el máximo está en el vértice `p = −b/(2a) = −380 / (−20) = 19`, que está dentro del intervalo `8 ≤ p ≤ 30`.",
            "c) `G(19) = −10·361 + 380·19 − 2800 = −3610 + 7220 − 2800 = 810` miles de pesos (vendiendo `q(19) = 110` remeras).",
            "Error típico: restar mal el costo (`− 2800 − 80p` en lugar de `− 2800 + 80p`) o calcular el costo como `C(p)` en vez de `C(q(p))`.",
        ],
    },
    {
        "id": "a2-modelado-composicion-3",
        "node": "a2-modelado-composicion",
        "kind": "problem",
        "level": 3,
        "title": "Componer en los dos órdenes y cuidar el dominio",
        "statement": (
            "Dadas `f(x) = √(x − 1)` y `g(x) = x² − 8`, hallá las composiciones `(f ∘ g)(x) = f(g(x))` y "
            "`(g ∘ f)(x) = g(f(x))`, cada una con su dominio (trabajando en los reales)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la fórmula y el dominio de (f ∘ g)(x)?",
                "check": {
                    "type": "choice",
                    "options": [
                        "√(x² − 9), con dominio (−∞, −3] ∪ [3, +∞)",
                        "√(x² − 9), con dominio [3, +∞)",
                        "√(x² − 9), con dominio [−3, 3]",
                        "x − 9, con dominio [1, +∞)",
                    ],
                    "correct": 0,
                },
                "answer": "√(x² − 9), con dominio (−∞, −3] ∪ [3, +∞)",
            },
            {
                "prompt": "b) ¿Cuál es la fórmula y el dominio de (g ∘ f)(x)?",
                "check": {
                    "type": "choice",
                    "options": [
                        "x − 9, con dominio [1, +∞)",
                        "x − 9, con dominio todos los reales",
                        "x − 9, con dominio [9, +∞)",
                        "√(x² − 9), con dominio [1, +∞)",
                    ],
                    "correct": 0,
                },
                "answer": "x − 9, con dominio [1, +∞)",
            },
            {
                "prompt": "c) La ecuación (f ∘ g)(x) = 4 tiene dos soluciones. ¿Cuál es la MENOR? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -5, "tolerance": 0, "unit": ""},
                "answer": "−5 (las soluciones son −5 y 5)",
            },
        ],
        "hints": [
            "`f(g(x))`: reemplazá la `x` de `f` por toda la expresión `x² − 8`. `g(f(x))`: reemplazá la `x` de `g` por `√(x − 1)`.",
            "En `f ∘ g` hay que pedir `g(x) ≥ 1` (lo que entra en `f` debe estar en su dominio). Resolvé esa inecuación cuadrática.",
            "En `g ∘ f` la fórmula simplificada ya no muestra la raíz, pero la `x` tuvo que pasar primero por `f`.",
        ],
        "solution": [
            "Dominios de partida: `Dom f = [1, +∞)` (hace falta `x − 1 ≥ 0`) y `Dom g = ℝ`.",
            "`(f ∘ g)(x) = f(x² − 8) = √((x² − 8) − 1) = √(x² − 9)`.",
            "Su dominio: `g(x)` debe estar en `Dom f` → `x² − 8 ≥ 1` → `x² ≥ 9` → `|x| ≥ 3` → `(−∞, −3] ∪ [3, +∞)`.",
            "`(g ∘ f)(x) = g(√(x − 1)) = (√(x − 1))² − 8 = (x − 1) − 8 = x − 9`.",
            "Su dominio: `x` tiene que poder entrar primero en `f` → `x ≥ 1`; después `g` acepta cualquier número. Dominio `[1, +∞)`, aunque la fórmula `x − 9` «parezca» valer para todo real. Por ejemplo, `(g ∘ f)(0)` no existe porque `f(0) = √(−1)` no es real.",
            "c) `√(x² − 9) = 4` → como `4 ≥ 0` podemos elevar al cuadrado: `x² − 9 = 16` → `x² = 25` → `x = 5` o `x = −5`. Los dos están en el dominio (`|x| ≥ 3`) y verifican: `√(25 − 9) = √16 = 4`. La menor es `x = −5`.",
            "Conclusión: `f ∘ g ≠ g ∘ f` (ni la fórmula ni el dominio coinciden). Error típico: olvidarse de la rama negativa `(−∞, −3]` o dar dominio ℝ a `g ∘ f`.",
        ],
    },
    # ==================== t-reciprocas-referencia ====================
    {
        "id": "t-reciprocas-referencia-1",
        "node": "t-reciprocas-referencia",
        "kind": "problem",
        "level": 1,
        "title": "Recíprocas de ángulos notables",
        "statement": (
            "Sin calculadora, usando ángulos de referencia y los valores notables "
            "(`sen 30° = 1/2`, `cos 60° = 1/2`, `tan 45° = 1`), calculá las siguientes razones recíprocas."
        ),
        "parts": [
            {
                "prompt": "a) sec(300°). Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2 (1 / cos 300° = 1 / 0.5)",
            },
            {
                "prompt": "b) csc(210°). Respondé solo con el número.",
                "check": {"type": "numeric", "value": -2, "tolerance": 0, "unit": ""},
                "answer": "−2 (1 / sen 210° = 1 / (−0.5))",
            },
            {
                "prompt": "c) cot(225°). Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1 (1 / tan 225° = 1 / 1)",
            },
        ],
        "hints": [
            "Primero pasá a la razón básica: `sec = 1/cos`, `csc = 1/sen`, `cot = 1/tan`.",
            "Para cada ángulo: ubicá el cuadrante, calculá el ángulo de referencia (contra el eje X) y poné el signo que corresponde.",
        ],
        "solution": [
            "`300°` está en el 4.° cuadrante: referencia `360° − 300° = 60°`. Ahí `x > 0` → `cos 300° = +cos 60° = 1/2` → `sec 300° = 1 / (1/2) = 2`.",
            "`210°` está en el 3.er cuadrante: referencia `210° − 180° = 30°`. Ahí `y < 0` → `sen 210° = −sen 30° = −1/2` → `csc 210° = 1 / (−1/2) = −2`.",
            "`225°` está en el 3.er cuadrante: referencia `225° − 180° = 45°`. Seno y coseno son ambos negativos, así que la tangente es positiva: `tan 225° = +tan 45° = 1` → `cot 225° = 1/1 = 1`.",
            "Resumen: `sec 300° = 2`, `csc 210° = −2`, `cot 225° = 1`. La recíproca siempre tiene el mismo signo que su razón básica.",
            "Error típico: emparejar `sec` con `sen` (daría `sec 300° = 1/sen 300° = −2/√3`, incorrecto).",
        ],
    },
    {
        "id": "t-reciprocas-referencia-2",
        "node": "t-reciprocas-referencia",
        "kind": "problem",
        "level": 2,
        "title": "Un ángulo negativo de varias vueltas",
        "statement": (
            "Un brazo robótico gira `θ = −840°` (el signo negativo indica giro en sentido horario) a partir "
            "del semieje positivo X. Querés conocer `csc(θ)` de forma exacta, sin calculadora."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el ángulo coterminal con θ que está entre 0° y 360°? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 240, "tolerance": 0, "unit": "°"},
                "answer": "240° (−840° + 3·360°)",
            },
            {
                "prompt": "b) ¿Cuál es su ángulo de referencia? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": "°"},
                "answer": "60° (240° − 180°)",
            },
            {
                "prompt": "c) ¿Cuál es el valor exacto de csc(−840°)?",
                "check": {
                    "type": "choice",
                    "options": ["−2√3/3", "2√3/3", "−2", "−√3/2"],
                    "correct": 0,
                },
                "answer": "−2√3/3 (= −2/√3 ≈ −1.155)",
            },
        ],
        "hints": [
            "Sumá vueltas completas (360°) hasta caer entre 0° y 360°.",
            "Ubicá el cuadrante: de eso dependen la fórmula del ángulo de referencia y el signo del seno.",
            "`csc = 1/sen`. Usá `sen 60° = √3/2` y racionalizá el resultado.",
        ],
        "solution": [
            "Coterminal: `−840° + 360° = −480°`; `−480° + 360° = −120°`; `−120° + 360° = 240°`. O sea `−840° + 3·360° = 240°`.",
            "`240°` está entre 180° y 270° → **3.er cuadrante**. Ángulo de referencia: `240° − 180° = 60°`.",
            "En el 3.er cuadrante `y < 0`, así que el seno es negativo: `sen(−840°) = sen 240° = −sen 60° = −√3/2`.",
            "`csc(−840°) = 1 / (−√3/2) = −2/√3`.",
            "Racionalizamos: `−2/√3 · (√3/√3) = −2√3/3 ≈ −1.155`.",
            "Chequeo de coherencia: toda cosecante cumple `|csc| ≥ 1`, y `1.155 ≥ 1`. Los distractores típicos son `−√3/2` (ese es el seno, faltó invertir), `−2` (referencia mal tomada, 30° en vez de 60°) y `+2√3/3` (signo del cuadrante).",
        ],
    },
    {
        "id": "t-reciprocas-referencia-3",
        "node": "t-reciprocas-referencia",
        "kind": "problem",
        "level": 3,
        "title": "De una razón a todas las demás",
        "statement": (
            "De un ángulo `θ` se sabe que `cot(θ) = −3/4` y que `csc(θ) > 0`.\n\n"
            "Determiná en qué cuadrante está y calculá, sin hallar el ángulo, el valor de la expresión\n\n"
            "`E = (sec θ + tan θ) / (csc θ − cot θ)`."
        ),
        "parts": [
            {
                "prompt": "a) ¿En qué cuadrante está θ?",
                "check": {
                    "type": "choice",
                    "options": ["Segundo cuadrante", "Primer cuadrante", "Tercer cuadrante", "Cuarto cuadrante"],
                    "correct": 0,
                },
                "answer": "Segundo cuadrante",
            },
            {
                "prompt": "b) ¿Cuánto vale cos(θ)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -0.6, "tolerance": 0, "unit": ""},
                "answer": "−0.6 (= −3/5)",
            },
            {
                "prompt": "c) ¿Cuánto vale E? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -1.5, "tolerance": 0, "unit": ""},
                "answer": "−1.5 (= −3/2)",
            },
        ],
        "hints": [
            "`csc` tiene el signo del seno. `cot = cos/sen`: si es negativa, seno y coseno tienen signos opuestos.",
            "`cot θ = x/y` para un punto `(x, y)` del lado terminal. Elegí `|x| = 3` y `|y| = 4`, poneles los signos del cuadrante que hallaste y calculá `r = √(x² + y²)`.",
            "Con `sen θ` y `cos θ` armá las cuatro razones que aparecen en `E` y operá con fracciones.",
        ],
        "solution": [
            "`csc θ > 0` → `sen θ > 0` (cuadrantes 1 o 2). `cot θ = cos θ / sen θ < 0` con seno positivo → `cos θ < 0`. Seno positivo y coseno negativo: **2.° cuadrante**.",
            "Tomamos un punto del lado terminal con `x/y = −3/4`, `x < 0`, `y > 0`: `(x, y) = (−3, 4)`. Radio: `r = √(9 + 16) = 5`.",
            "`sen θ = y/r = 4/5` y `cos θ = x/r = −3/5 = −0.6`. (Chequeo: `(4/5)² + (−3/5)² = 1`.)",
            "Recíprocas y tangente: `sec θ = −5/3`, `csc θ = 5/4`, `tan θ = −4/3`, `cot θ = −3/4`.",
            "Numerador: `sec θ + tan θ = −5/3 − 4/3 = −9/3 = −3`.",
            "Denominador: `csc θ − cot θ = 5/4 − (−3/4) = 8/4 = 2`.",
            "`E = −3 / 2 = −1.5`.",
            "Error típico: usar el triángulo 3-4-5 sin signos (daría `cos θ = +3/5` y `E` equivocado) o restar `cot θ` sin cambiar el signo.",
        ],
    },
    # ==================== t-desfase-tangente ====================
    {
        "id": "t-desfase-tangente-1",
        "node": "t-desfase-tangente",
        "kind": "problem",
        "level": 1,
        "title": "Leer una sinusoidal completa",
        "statement": (
            "Considerá la onda `y = 5·sen(2x + π/3) − 2`, con `x` en radianes. Comparala con la onda "
            "sin desfase `y = 5·sen(2x) − 2`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el valor máximo que alcanza y? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3 (−2 + 5)",
            },
            {
                "prompt": "b) ¿Cuál es su período?",
                "check": {"type": "choice", "options": ["π", "2π", "π/2", "4π"], "correct": 0},
                "answer": "π",
            },
            {
                "prompt": "c) ¿Cuánto y hacia dónde está corrida respecto de y = 5·sen(2x) − 2? (Elegí el corrimiento más corto.)",
                "check": {
                    "type": "choice",
                    "options": [
                        "π/6 hacia la izquierda",
                        "π/3 hacia la izquierda",
                        "π/6 hacia la derecha",
                        "π/3 hacia la derecha",
                    ],
                    "correct": 0,
                },
                "answer": "π/6 hacia la izquierda",
            },
        ],
        "hints": [
            "Llevala a la forma `A·sen(B(x − C)) + D`: para eso sacá `B` como factor común dentro del paréntesis.",
            "Máximo = `D + |A|`. Período = `2π / |B|`. Desfase = `C` (positivo → derecha, negativo → izquierda).",
        ],
        "solution": [
            "Sacamos factor común 2 adentro: `2x + π/3 = 2(x + π/6)`. Entonces `y = 5·sen(2(x + π/6)) − 2`.",
            "Comparando con `A·sen(B(x − C)) + D`: `A = 5`, `B = 2`, `C = −π/6`, `D = −2`.",
            "Máximo: `D + |A| = −2 + 5 = 3` (y el mínimo es `−2 − 5 = −7`).",
            "Período: `T = 2π / 2 = π`.",
            "Desfase: `x − C = x + π/6` → `C = −π/6` → la onda está corrida `π/6` hacia la **izquierda**.",
            "Verificación: `5·sen(2x) − 2` cruza su línea media subiendo en `x = 0`; la onda dada lo hace cuando `2x + π/3 = 0`, es decir en `x = −π/6`.",
            "Error típico: leer el desfase directo como `π/3` sin factorizar el 2.",
        ],
    },
    {
        "id": "t-desfase-tangente-2",
        "node": "t-desfase-tangente",
        "kind": "problem",
        "level": 2,
        "title": "Asíntotas de una tangente transformada",
        "statement": (
            "Considerá la función `f(x) = 3·tan(2x − 60°)`, con `x` medido en grados.\n\n"
            "Estudiá su período y la ubicación de sus asíntotas verticales."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el período de f? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 90, "tolerance": 0, "unit": "°"},
                "answer": "90° (180° / 2)",
            },
            {
                "prompt": "b) ¿En qué valor de x está la asíntota vertical positiva más cercana al origen? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 75, "tolerance": 0, "unit": "°"},
                "answer": "75°",
            },
            {
                "prompt": "c) ¿Cuántas asíntotas verticales tiene f en el intervalo [0°, 360°)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4 (en 75°, 165°, 255° y 345°)",
            },
        ],
        "hints": [
            "El período de `tan(Bx)` es `180° / |B|`; el factor 3 de afuera no lo cambia.",
            "`tan(u)` tiene asíntotas donde `cos(u) = 0`: `u = 90° + 180°·k`. Acá `u = 2x − 60°`.",
            "Despejá `x` en función de `k` y probá `k = −1, 0, 1, 2, ...` para ver cuáles caen en `[0°, 360°)`.",
        ],
        "solution": [
            "Período: `180° / 2 = 90°`. (El 3 estira verticalmente pero no cambia período ni asíntotas.)",
            "Asíntotas: el argumento debe valer `90° + 180°k`: `2x − 60° = 90° + 180°k`.",
            "Despejamos: `2x = 150° + 180°k` → `x = 75° + 90°k`, con `k` entero. Están separadas exactamente un período (90°).",
            "Con `k = −1`: `x = −15°` (negativa). Con `k = 0`: `x = 75°` → es la primera positiva.",
            "En `[0°, 360°)`: `k = 0, 1, 2, 3` → `75°, 165°, 255°, 345°`. Con `k = 4` daría `435°`, fuera del intervalo. Total: **4 asíntotas**.",
            "Chequeo: en `x = 75°` el argumento es `2·75° − 60° = 90°` y `cos 90° = 0`. Además los ceros de `f` están a mitad de camino entre asíntotas: `2x − 60° = 0` → `x = 30°`.",
            "Error típico: dividir por 2 antes de sumar `180°k` (daría asíntotas cada 180° y se perdería la mitad).",
        ],
    },
    {
        "id": "t-desfase-tangente-3",
        "node": "t-desfase-tangente",
        "kind": "problem",
        "level": 3,
        "title": "Horas de luz en Ushuaia",
        "statement": (
            "En Ushuaia la duración del día (horas de luz solar) varía a lo largo del año de forma "
            "aproximadamente sinusoidal: el máximo, de unas **17 h**, ocurre el 21 de diciembre, y el mínimo, "
            "de unas **7 h**, el 21 de junio. El ciclo se repite cada **12 meses**.\n\n"
            "Llamá `t` al tiempo en meses contado desde el **21 de marzo** (`t = 0`), de modo que el 21 de "
            "junio es `t = 3` y el 21 de diciembre es `t = 9`, y `L(t)` a las horas de luz. Suponé que todos "
            "los meses duran lo mismo."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué función modela las horas de luz?",
                "check": {
                    "type": "choice",
                    "options": [
                        "L(t) = 5·cos((π/6)(t − 9)) + 12",
                        "L(t) = 5·cos((π/6)(t − 3)) + 12",
                        "L(t) = 10·cos((π/6)(t − 9)) + 12",
                        "L(t) = 5·cos((π/12)(t − 9)) + 12",
                    ],
                    "correct": 0,
                },
                "answer": "L(t) = 5·cos((π/6)(t − 9)) + 12",
            },
            {
                "prompt": "b) Según el modelo, ¿cuántas horas de luz hay el 21 de octubre (t = 7)? Respondé solo con el número en h.",
                "check": {"type": "numeric", "value": 14.5, "tolerance": 0, "unit": "h"},
                "answer": "14.5 h",
            },
            {
                "prompt": "c) ¿Para qué valor de t, con 0 ≤ t < 12, el día dura 9.5 h por PRIMERA vez? Respondé solo con el número en meses.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": "meses"},
                "answer": "1 mes (el 21 de abril; la otra vez es t = 5)",
            },
        ],
        "hints": [
            "Amplitud `A = (máx − mín)/2`, línea media `D = (máx + mín)/2`, `B = 2π/T`. El coseno vale 1 cuando su argumento es 0: centrá el desfase en el instante del máximo.",
            "Para b) el argumento da un ángulo notable: `(π/6)·(7 − 9) = −π/3`, y el coseno es par.",
            "Para c) despejá el coseno, buscá TODOS los ángulos que cumplen (sumando `2πk`) y recién después despejá `t`.",
        ],
        "solution": [
            "Amplitud: `A = (17 − 7)/2 = 5 h`. Línea media: `D = (17 + 7)/2 = 12 h`. Período 12 meses → `B = 2π/12 = π/6`.",
            "El máximo ocurre en `t = 9`: con un coseno, el desfase es `C = 9` → `L(t) = 5·cos((π/6)(t − 9)) + 12`. Chequeo: `L(9) = 5·1 + 12 = 17` y `L(3) = 5·cos(−π) + 12 = 7`.",
            "b) `L(7) = 5·cos((π/6)(−2)) + 12 = 5·cos(−π/3) + 12 = 5·0.5 + 12 = 14.5 h`.",
            "c) `5·cos((π/6)(t − 9)) + 12 = 9.5` → `cos((π/6)(t − 9)) = −2.5/5 = −1/2`.",
            "El coseno vale `−1/2` en `±2π/3 + 2πk`: `(π/6)(t − 9) = ±2π/3 + 2πk`. Multiplicando por `6/π`: `t − 9 = ±4 + 12k` → `t = 13 + 12k` o `t = 5 + 12k`.",
            "En `0 ≤ t < 12`: de la primera familia, `k = −1` da `t = 1`; de la segunda, `k = 0` da `t = 5`. La primera vez es `t = 1` (21 de abril) y la segunda `t = 5` (21 de agosto).",
            "Tiene sentido: son instantes simétricos respecto del mínimo de `t = 3` (dos meses antes y dos después). Verificación: `L(1) = 5·cos(−4π/3) + 12 = 5·(−0.5) + 12 = 9.5 h`.",
        ],
    },
    # ==================== t-leyes-senos-cosenos ====================
    {
        "id": "t-leyes-senos-cosenos-1",
        "node": "t-leyes-senos-cosenos",
        "kind": "problem",
        "level": 1,
        "title": "Un lote triangular en esquina",
        "statement": (
            "Un lote con forma de triángulo tiene lados de **70 m**, **80 m** y **130 m**. No se conoce "
            "ningún ángulo.\n\n"
            "Dato: `sen 120° = sen 60° = √3/2`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto mide el ángulo mayor del lote (el opuesto al lado de 130 m)? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 120, "tolerance": 0, "unit": "°"},
                "answer": "120°",
            },
            {
                "prompt": "b) ¿Cuál es la superficie exacta del lote?",
                "check": {
                    "type": "choice",
                    "options": [
                        "1400√3 m² (≈ 2425 m²)",
                        "2800√3 m² (≈ 4850 m²)",
                        "1400 m²",
                        "2800 m²",
                    ],
                    "correct": 0,
                },
                "answer": "1400√3 m² (≈ 2425 m²)",
            },
        ],
        "hints": [
            "Tres lados y ningún ángulo (LLL): la única ley que podés arrancar es la de cosenos. Despejá `cos(C)` con `c = 130`.",
            "Para la superficie usá `Área = (1/2)·a·b·sen(C)` con los dos lados que forman el ángulo que acabás de hallar.",
        ],
        "solution": [
            "Caso LLL → Ley de cosenos. Con `a = 70`, `b = 80`, `c = 130`: `c² = a² + b² − 2ab·cos(C)`.",
            "Despejamos: `cos(C) = (a² + b² − c²) / (2ab) = (4900 + 6400 − 16900) / (2·70·80) = −5600 / 11200 = −0.5`.",
            "Coseno negativo → ángulo obtuso. `cos(C) = −0.5` con `0° < C < 180°` → `C = 120°`.",
            "Los lados de 70 m y 80 m son los que forman ese ángulo. `Área = (1/2)·70·80·sen(120°) = 2800 · (√3/2) = 1400√3 m² ≈ 2425 m²`.",
            "Errores típicos: olvidar el `1/2` (da `2800√3`), usar `sen 120° = 0.5` (da `1400`) o tratarlo como triángulo rectángulo (`70·80/2 = 2800`).",
        ],
    },
    {
        "id": "t-leyes-senos-cosenos-2",
        "node": "t-leyes-senos-cosenos",
        "kind": "problem",
        "level": 2,
        "title": "El caso ambiguo: ¿uno o dos triángulos?",
        "statement": (
            "De un triángulo `ABC` se conocen el ángulo `A = 30°`, su lado opuesto `a = 10 cm` y el lado "
            "`b = 10√2 cm` (≈ 14.14 cm), opuesto al ángulo `B`. Es un caso LLA: dos lados y un ángulo que "
            "NO está entre ellos.\n\n"
            "Datos: `sen 30° = 1/2`, `sen 45° = sen 135° = √2/2`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuántos triángulos distintos cumplen estos datos? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2 triángulos",
            },
            {
                "prompt": "b) En el triángulo donde B es agudo, ¿cuánto mide B? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 45, "tolerance": 0, "unit": "°"},
                "answer": "45°",
            },
            {
                "prompt": "c) En el triángulo donde B es obtuso, ¿cuánto mide el ángulo C? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": "°"},
                "answer": "15° (180° − 30° − 135°)",
            },
        ],
        "hints": [
            "Tenés una pareja completa (`a` y `A`): usá la Ley de senos para hallar `sen(B)`.",
            "Un mismo valor de seno corresponde a dos ángulos entre 0° y 180°: `B` y `180° − B`.",
            "Cada candidato sirve solo si `A + B < 180°` (tiene que quedar un ángulo `C` positivo).",
        ],
        "solution": [
            "Ley de senos: `a / sen(A) = b / sen(B)` → `sen(B) = b·sen(A) / a = 10√2 · (1/2) / 10 = √2/2`.",
            "Entre 0° y 180° hay dos ángulos con ese seno: `B₁ = 45°` y `B₂ = 180° − 45° = 135°`.",
            "Chequeamos cada uno: `A + B₁ = 30° + 45° = 75° < 180°` → válido. `A + B₂ = 30° + 135° = 165° < 180°` → también válido.",
            "Hay **2 triángulos** posibles. (Era esperable: `a < b` y `a > b·sen A = 5√2 ≈ 7.07`, la condición del caso ambiguo.)",
            "Triángulo 1 (B agudo): `B = 45°`, `C = 180° − 30° − 45° = 105°`.",
            "Triángulo 2 (B obtuso): `B = 135°`, `C = 180° − 30° − 135° = 15°`.",
            "Error típico: quedarse solo con `B = 45°` porque es lo único que devuelve `arcsen` en la calculadora.",
        ],
    },
    {
        "id": "t-leyes-senos-cosenos-3",
        "node": "t-leyes-senos-cosenos",
        "kind": "problem",
        "level": 3,
        "title": "Relevamiento a orillas del Paraná",
        "statement": (
            "Una agrimensora trabaja sobre una costa recta del río Paraná. Clava dos estacas `A` y `B` "
            "separadas **100 m** sobre la costa. En la orilla opuesta, justo en el borde del agua, hay un "
            "árbol `P`. Con el teodolito mide los ángulos `PÂB = 30°` y `PB̂A = 120°`.\n\n"
            "Sobre la misma costa, en la prolongación de `AB` más allá de `B`, hay un muelle `Q` a **200 m** "
            "de `A` (o sea, 100 m después de `B`).\n\n"
            "Suponé que las dos orillas son rectas y paralelas. Datos: `sen 30° = 1/2`, "
            "`sen 120° = √3/2`, `cos 30° = √3/2`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la distancia exacta de la estaca A al árbol P?",
                "check": {
                    "type": "choice",
                    "options": [
                        "100√3 m (≈ 173.2 m)",
                        "100 m",
                        "100√2 m (≈ 141.4 m)",
                        "200√3/3 m (≈ 115.5 m)",
                    ],
                    "correct": 0,
                },
                "answer": "100√3 m (≈ 173.2 m)",
            },
            {
                "prompt": "b) ¿Cuál es el ancho del río (distancia de P a la recta de la costa AB)? Usá √3 ≈ 1.732 y redondeá a 1 decimal. Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 86.6, "tolerance": 0.005, "unit": "m"},
                "answer": "86.6 m (= 50√3 m)",
            },
            {
                "prompt": "c) ¿A qué distancia está el árbol P del muelle Q? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 100, "tolerance": 0, "unit": "m"},
                "answer": "100 m",
            },
        ],
        "hints": [
            "En el triángulo `ABP` conocés dos ángulos y el lado entre ellos (ALA): calculá el tercer ángulo y aplicá la Ley de senos. El lado `AB` es opuesto al ángulo en `P`.",
            "El ancho del río es la altura del triángulo desde `P`: en el triángulo rectángulo que forma con `A`, es `AP·sen(30°)`.",
            "Para `PQ` mirá el triángulo `APQ`: conocés `AP`, `AQ` y el ángulo en `A` (es el mismo `30°`, porque `Q` está sobre la semirrecta `AB`). Dos lados y el ángulo comprendido → Ley de cosenos.",
        ],
        "solution": [
            "Tercer ángulo de `ABP`: `P̂ = 180° − 30° − 120° = 30°`.",
            "Ley de senos (el lado `AB = 100` es opuesto a `P̂`; el lado `AP` es opuesto a `B̂`): `AP / sen(120°) = AB / sen(30°)` → `AP = 100 · (√3/2) / (1/2) = 100√3 ≈ 173.2 m`.",
            "(De paso: como `Â = P̂ = 30°`, el triángulo es isósceles y `BP = AB = 100 m`.)",
            "Ancho del río = distancia de `P` a la recta `AB`. Bajando la perpendicular desde `P` se forma un triángulo rectángulo con hipotenusa `AP` y ángulo `30°` en `A`: `ancho = AP·sen(30°) = 100√3 · (1/2) = 50√3 ≈ 50 · 1.732 = 86.6 m`.",
            "Triángulo `APQ`: `AP = 100√3`, `AQ = 200` y el ángulo comprendido `PÂQ = 30°` (caso LAL) → Ley de cosenos: `PQ² = AP² + AQ² − 2·AP·AQ·cos(30°)`.",
            "`PQ² = (100√3)² + 200² − 2·(100√3)·200·(√3/2) = 30 000 + 40 000 − 60 000 = 10 000` → `PQ = 100 m`.",
            "Verificación por otro camino: en el triángulo `BPQ`, `BP = 100`, `BQ = 100` y el ángulo en `B` es `180° − 120° = 60°` → es equilátero, así que `PQ = 100 m`.",
            "Error típico: aplicar la Ley de senos con parejas mal armadas (`AP / sen 30°`), que da `AP = 100 m`.",
        ],
    },
    # ==================== t-inversas-restringidas ====================
    {
        "id": "t-inversas-restringidas-1",
        "node": "t-inversas-restringidas",
        "kind": "problem",
        "level": 1,
        "title": "Inversas con valores notables",
        "statement": (
            "Calculá sin calculadora, en grados, respetando el rango principal de cada función inversa.\n\n"
            "Datos: `sen 60° = √3/2`, `cos 45° = √2/2`, `tan 60° = √3`, `cos 180° = −1`."
        ),
        "parts": [
            {
                "prompt": "a) arcsen(−√3/2). Respondé solo con el número en grados (con signo).",
                "check": {"type": "numeric", "value": -60, "tolerance": 0, "unit": "°"},
                "answer": "−60°",
            },
            {
                "prompt": "b) arccos(−√2/2). Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 135, "tolerance": 0, "unit": "°"},
                "answer": "135°",
            },
            {
                "prompt": "c) arctan(√3) + arccos(−1). Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 240, "tolerance": 0, "unit": "°"},
                "answer": "240° (60° + 180°)",
            },
        ],
        "hints": [
            "Rangos principales: `arcsen` en `[−90°, 90°]`, `arccos` en `[0°, 180°]`, `arctan` en `(−90°, 90°)`.",
            "Para un argumento negativo: `arcsen` devuelve un ángulo entre `−90°` y `0°`, mientras que `arccos` devuelve uno mayor que `90°` y de hasta `180°` (2.° cuadrante, o justo `180°` si el argumento es `−1`).",
        ],
        "solution": [
            "a) Buscamos en `[−90°, 90°]` el ángulo con seno `−√3/2`. Como `sen 60° = √3/2` y el seno es impar, `sen(−60°) = −√3/2` → `arcsen(−√3/2) = −60°`. (240° y 300° tienen el mismo seno pero están fuera del rango.)",
            "b) Buscamos en `[0°, 180°]` el ángulo con coseno `−√2/2`. Referencia 45°, coseno negativo → 2.° cuadrante: `180° − 45° = 135°`.",
            "c) `arctan(√3) = 60°` (está en `(−90°, 90°)`) y `arccos(−1) = 180°` (extremo del rango `[0°, 180°]`).",
            "Suma: `60° + 180° = 240°`.",
            "Error típico: responder `arccos(−√2/2) = −45°` copiando la regla del arcoseno; `−45°` no está en `[0°, 180°]` y además `cos(−45°) = +√2/2`.",
        ],
    },
    {
        "id": "t-inversas-restringidas-2",
        "node": "t-inversas-restringidas",
        "kind": "problem",
        "level": 2,
        "title": "Cuando la inversa no «deshace»",
        "statement": (
            "Las funciones trigonométricas inversas solo deshacen a las directas dentro de su rango principal. "
            "Evaluá, sin calculadora, las siguientes composiciones.\n\n"
            "Datos: `cos 60° = 1/2`, `sen 60° = √3/2`."
        ),
        "parts": [
            {
                "prompt": "a) arccos(cos(300°)). Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": "°"},
                "answer": "60°",
            },
            {
                "prompt": "b) arcsen(sen(240°)). Respondé solo con el número en grados (con signo).",
                "check": {"type": "numeric", "value": -60, "tolerance": 0, "unit": "°"},
                "answer": "−60°",
            },
            {
                "prompt": "c) tan(arccos(−4/5)). Respondé solo con el número (decimal o fracción).",
                "check": {"type": "numeric", "value": -0.75, "tolerance": 0, "unit": ""},
                "answer": "−0.75 (= −3/4)",
            },
        ],
        "hints": [
            "En a) y b) trabajá de adentro hacia afuera: primero el valor de `cos(300°)` o `sen(240°)`, después la inversa en su rango principal.",
            "En c) llamá `θ = arccos(−4/5)`. ¿En qué cuadrante está `θ` si el coseno es negativo y `θ` pertenece a `[0°, 180°]`?",
            "Con `cos θ = −4/5` sacá `sen θ` por la identidad pitagórica (con el signo de ese cuadrante) y dividí.",
        ],
        "solution": [
            "a) `cos(300°) = cos(60°) = 1/2` (4.° cuadrante, coseno positivo). Luego `arccos(1/2) = 60°`, que sí está en `[0°, 180°]`. No da 300° porque 300° está fuera del rango de `arccos`.",
            "b) `sen(240°) = −sen(60°) = −√3/2` (3.er cuadrante). Luego `arcsen(−√3/2) = −60°`, dentro de `[−90°, 90°]`.",
            "c) Sea `θ = arccos(−4/5)`: `cos θ = −4/5` y `θ` está en `[0°, 180°]`. Con coseno negativo, `θ` está en el **2.° cuadrante**, donde el seno es positivo.",
            "`sen²θ = 1 − 16/25 = 9/25` → `sen θ = +3/5`.",
            "`tan θ = sen θ / cos θ = (3/5) / (−4/5) = −3/4 = −0.75`.",
            "Error típico en c): dibujar el triángulo 3-4-5 y responder `+3/4` sin mirar el cuadrante.",
        ],
    },
    {
        "id": "t-inversas-restringidas-3",
        "node": "t-inversas-restringidas",
        "kind": "problem",
        "level": 3,
        "title": "Invertir una sinusoidal restringida",
        "statement": (
            "Sea `f(x) = 2·sen(3x) + 1`, con `x` en grados y dominio restringido a `−30° ≤ x ≤ 30°` "
            "(en ese intervalo `f` es creciente, así que tiene inversa).\n\n"
            "Hallá `f⁻¹`, su dominio, y evaluala. Tomá `arcsen` en grados."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la fórmula de f⁻¹(x)?",
                "check": {
                    "type": "choice",
                    "options": [
                        "f⁻¹(x) = (1/3)·arcsen((x − 1)/2)",
                        "f⁻¹(x) = (1/3)·arcsen(x/2 − 1)",
                        "f⁻¹(x) = (1/2)·arcsen((x − 1)/3)",
                        "f⁻¹(x) = arcsen((x − 1)/6)",
                    ],
                    "correct": 0,
                },
                "answer": "f⁻¹(x) = (1/3)·arcsen((x − 1)/2)",
            },
            {
                "prompt": "b) ¿Cuál es el dominio de f⁻¹?",
                "check": {
                    "type": "choice",
                    "options": ["[−1, 3]", "[−1, 1]", "[−3, 3]", "[−2, 2]"],
                    "correct": 0,
                },
                "answer": "[−1, 3]",
            },
            {
                "prompt": "c) Calculá f⁻¹(2). Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "°"},
                "answer": "10°",
            },
        ],
        "hints": [
            "Escribí `y = 2·sen(3x) + 1` y despejá `x` deshaciendo las operaciones de afuera hacia adentro: restar 1, dividir por 2, aplicar `arcsen`, dividir por 3.",
            "Podés aplicar `arcsen` sin perder nada porque `3x` está entre `−90°` y `90°`, justo el rango principal.",
            "El dominio de `f⁻¹` es la imagen de `f`. También sale de pedir que el argumento del `arcsen` esté entre `−1` y `1`.",
        ],
        "solution": [
            "`y = 2·sen(3x) + 1` → `y − 1 = 2·sen(3x)` → `sen(3x) = (y − 1)/2`.",
            "Como `−30° ≤ x ≤ 30°`, el ángulo `3x` está en `[−90°, 90°]`, que es exactamente el rango de `arcsen`. Por eso `3x = arcsen((y − 1)/2)` sin ambigüedad.",
            "`x = (1/3)·arcsen((y − 1)/2)`. Intercambiando letras: `f⁻¹(x) = (1/3)·arcsen((x − 1)/2)`.",
            "Dominio: el argumento del arcoseno debe cumplir `−1 ≤ (x − 1)/2 ≤ 1` → `−2 ≤ x − 1 ≤ 2` → `−1 ≤ x ≤ 3`. Dominio `[−1, 3]`.",
            "Coincide con la imagen de `f`: como `sen(3x)` recorre `[−1, 1]`, `f` recorre `[2·(−1) + 1, 2·1 + 1] = [−1, 3]`. Y la imagen de `f⁻¹` es `[−30°, 30°]`.",
            "`f⁻¹(2) = (1/3)·arcsen((2 − 1)/2) = (1/3)·arcsen(1/2) = (1/3)·30° = 10°`.",
            "Verificación: `f(10°) = 2·sen(30°) + 1 = 2·0.5 + 1 = 2`.",
            "Error típico: despejar en el orden equivocado (dividir por 3 «adentro» del arcoseno) o dar como dominio `[−1, 1]`, que es el dominio de `arcsen` y no el de `f⁻¹`.",
        ],
    },
    # ==================== t-identidades-angulo-doble ====================
    {
        "id": "t-identidades-angulo-doble-1",
        "node": "t-identidades-angulo-doble",
        "kind": "problem",
        "level": 1,
        "title": "Valores exactos con suma de ángulos",
        "statement": (
            "Los ángulos de 75° y 105° no son notables, pero se pueden escribir como suma de dos que sí lo "
            "son: `75° = 45° + 30°` y `105° = 60° + 45°`.\n\n"
            "Datos: `sen 30° = cos 60° = 1/2`, `cos 30° = sen 60° = √3/2`, `sen 45° = cos 45° = √2/2`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el valor exacto de sen(75°)?",
                "check": {
                    "type": "choice",
                    "options": ["(√6 + √2)/4", "(√6 − √2)/4", "(1 + √2)/2", "(√3 + √2)/4"],
                    "correct": 0,
                },
                "answer": "(√6 + √2)/4 ≈ 0.966",
            },
            {
                "prompt": "b) ¿Cuál es el valor exacto de cos(105°)?",
                "check": {
                    "type": "choice",
                    "options": ["(√2 − √6)/4", "(√6 − √2)/4", "(√2 + √6)/4", "(1 + √2)/2"],
                    "correct": 0,
                },
                "answer": "(√2 − √6)/4 ≈ −0.259",
            },
        ],
        "hints": [
            "`sen(α + β) = sen α·cos β + cos α·sen β`. `cos(α + β) = cos α·cos β − sen α·sen β` (en el coseno el signo se invierte).",
            "Antes de elegir, pensá el signo: 105° está en el 2.° cuadrante, así que su coseno tiene que ser negativo.",
        ],
        "solution": [
            "`sen(75°) = sen(45° + 30°) = sen 45°·cos 30° + cos 45°·sen 30°`.",
            "`= (√2/2)(√3/2) + (√2/2)(1/2) = √6/4 + √2/4 = (√6 + √2)/4 ≈ (2.449 + 1.414)/4 ≈ 0.966`.",
            "`cos(105°) = cos(60° + 45°) = cos 60°·cos 45° − sen 60°·sen 45°`.",
            "`= (1/2)(√2/2) − (√3/2)(√2/2) = √2/4 − √6/4 = (√2 − √6)/4 ≈ (1.414 − 2.449)/4 ≈ −0.259`.",
            "Chequeo de signos: 75° está en el 1.er cuadrante cerca de 90° (seno casi 1) y 105° en el 2.° (coseno negativo y chico). Además `cos 105° = −cos 75° = −sen 15°`, coherente.",
            "Error típico: «distribuir» la función, `sen(45° + 30°) = sen 45° + sen 30° = (√2 + 1)/2 ≈ 1.21`, imposible porque un seno nunca supera 1.",
        ],
    },
    {
        "id": "t-identidades-angulo-doble-2",
        "node": "t-identidades-angulo-doble",
        "kind": "problem",
        "level": 2,
        "title": "De la tangente al ángulo doble",
        "statement": (
            "De un ángulo `θ` del **segundo cuadrante** se sabe que `tan(θ) = −2`.\n\n"
            "Sin calcular `θ`, hallá `sec²(θ)`, `sen(2θ)` y `cos(2θ)`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale sec²(θ)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                "answer": "5 (1 + tan²θ)",
            },
            {
                "prompt": "b) ¿Cuánto vale sen(2θ)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -0.8, "tolerance": 0, "unit": ""},
                "answer": "−0.8 (= −4/5)",
            },
            {
                "prompt": "c) ¿Cuánto vale cos(2θ)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -0.6, "tolerance": 0, "unit": ""},
                "answer": "−0.6 (= −3/5)",
            },
        ],
        "hints": [
            "Identidad pitagórica derivada: `1 + tan²θ = sec²θ`. De ahí sale `cos²θ = 1/sec²θ`.",
            "Elegí los signos de `cos θ` y `sen θ` según el 2.° cuadrante; el seno sale de `sen θ = tan θ · cos θ`.",
            "`sen(2θ) = 2·sen θ·cos θ` y `cos(2θ) = cos²θ − sen²θ`.",
        ],
        "solution": [
            "`sec²θ = 1 + tan²θ = 1 + (−2)² = 5`.",
            "`cos²θ = 1/5`. En el 2.° cuadrante el coseno es negativo: `cos θ = −1/√5`.",
            "`sen θ = tan θ · cos θ = (−2)(−1/√5) = 2/√5` (positivo, como corresponde). Chequeo: `sen²θ + cos²θ = 4/5 + 1/5 = 1`.",
            "`sen(2θ) = 2·sen θ·cos θ = 2 · (2/√5) · (−1/√5) = −4/5 = −0.8`.",
            "`cos(2θ) = cos²θ − sen²θ = 1/5 − 4/5 = −3/5 = −0.6`.",
            "Verificación: `sen²(2θ) + cos²(2θ) = 0.64 + 0.36 = 1`. Además `θ ≈ 116.6°`, así que `2θ ≈ 233.1°` cae en el 3.er cuadrante: seno y coseno negativos, como obtuvimos.",
            "Error típico: escribir `sen(2θ) = 2·sen θ` o tomar seno y coseno ambos positivos del triángulo 1-2-√5, sin mirar el cuadrante (daría `sen(2θ) = +4/5`).",
        ],
    },
    {
        "id": "t-identidades-angulo-doble-3",
        "node": "t-identidades-angulo-doble",
        "kind": "problem",
        "level": 3,
        "title": "Elevar al cuadrado para llegar al ángulo doble",
        "statement": (
            "De un ángulo `θ` con `90° < θ < 180°` se sabe que\n\n"
            "`sen(θ) + cos(θ) = 1/5`.\n\n"
            "Sin calcular `θ`, hallá `sen(2θ)`, `cos(2θ)` y el valor de `E = (1 − cos(2θ)) / sen(2θ)`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale sen(2θ)? Respondé solo con el número (decimal o fracción).",
                "check": {"type": "numeric", "value": -0.96, "tolerance": 0, "unit": ""},
                "answer": "−0.96 (= −24/25)",
            },
            {
                "prompt": "b) ¿Cuánto vale cos(2θ)? Respondé solo con el número (decimal o fracción).",
                "check": {"type": "numeric", "value": -0.28, "tolerance": 0, "unit": ""},
                "answer": "−0.28 (= −7/25)",
            },
            {
                "prompt": "c) ¿Cuánto vale E? Respondé solo con el número (fracción o decimal redondeado a 2 decimales).",
                "check": {"type": "numeric", "value": -4 / 3, "tolerance": 0.005, "unit": ""},
                "answer": "−4/3 ≈ −1.33 (E = tan θ)",
            },
        ],
        "hints": [
            "Elevá al cuadrado los dos miembros de `sen θ + cos θ = 1/5`: aparecen `sen²θ + cos²θ` y el doble producto `2·sen θ·cos θ`.",
            "Para `cos(2θ)` necesitás el signo. Probá calcular `(cos θ − sen θ)²` y usá que en el 2.° cuadrante `cos θ < 0 < sen θ`; después `cos(2θ) = (cos θ − sen θ)(cos θ + sen θ)`.",
            "Para `E` podés reemplazar los valores, o simplificar antes con `1 − cos(2θ) = 2·sen²θ` y `sen(2θ) = 2·sen θ·cos θ`.",
        ],
        "solution": [
            "Elevamos al cuadrado: `(sen θ + cos θ)² = sen²θ + 2·sen θ·cos θ + cos²θ = 1 + sen(2θ)`. Entonces `1 + sen(2θ) = 1/25` → `sen(2θ) = −24/25 = −0.96`.",
            "Para el coseno del doble: `(cos θ − sen θ)² = 1 − sen(2θ) = 1 + 24/25 = 49/25` → `cos θ − sen θ = ±7/5`.",
            "En el 2.° cuadrante `cos θ < 0` y `sen θ > 0`, así que `cos θ − sen θ < 0` → `cos θ − sen θ = −7/5`.",
            "`cos(2θ) = cos²θ − sen²θ = (cos θ − sen θ)(cos θ + sen θ) = (−7/5)(1/5) = −7/25 = −0.28`. Chequeo: `0.96² + 0.28² = 0.9216 + 0.0784 = 1`.",
            "Simplificamos `E`: `1 − cos(2θ) = 2·sen²θ` y `sen(2θ) = 2·sen θ·cos θ` → `E = 2·sen²θ / (2·sen θ·cos θ) = sen θ / cos θ = tan θ`.",
            "Con números: `E = (1 + 0.28) / (−0.96) = 1.28 / (−0.96) = −4/3 ≈ −1.33`.",
            "Verificación completa: sumando y restando `sen θ + cos θ = 1/5` y `cos θ − sen θ = −7/5` sale `cos θ = −3/5` y `sen θ = 4/5` (2.° cuadrante), y `tan θ = −4/3`.",
            "Error típico: tomar `cos(2θ) = +7/25` por no analizar el signo (con `sen θ + cos θ > 0` en el 2.° cuadrante, `θ` está entre 90° y 135°, así que `2θ` cae en el 3.er cuadrante).",
        ],
    },
    # ==================== t-ecuaciones-trigonometricas ====================
    {
        "id": "t-ecuaciones-trigonometricas-1",
        "node": "t-ecuaciones-trigonometricas",
        "kind": "problem",
        "level": 1,
        "title": "Una ecuación con tangente",
        "statement": (
            "Resolvé la ecuación `tan(x) + √3 = 0`.\n\n"
            "Dato: `tan 60° = √3`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la MENOR solución en [0°, 360°)? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 120, "tolerance": 0, "unit": "°"},
                "answer": "120°",
            },
            {
                "prompt": "b) ¿Cuál es la otra solución en [0°, 360°)? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 300, "tolerance": 0, "unit": "°"},
                "answer": "300°",
            },
            {
                "prompt": "c) ¿Cuál es la solución general (k entero)?",
                "check": {
                    "type": "choice",
                    "options": [
                        "x = 120° + 180°·k",
                        "x = 120° + 360°·k",
                        "x = 60° + 180°·k",
                        "x = 150° + 180°·k",
                    ],
                    "correct": 0,
                },
                "answer": "x = 120° + 180°·k",
            },
        ],
        "hints": [
            "Despejá `tan(x) = −√3`. El ángulo de referencia es 60°; falta decidir en qué cuadrantes la tangente es NEGATIVA.",
            "La tangente es negativa donde seno y coseno tienen signos opuestos: 2.° y 4.° cuadrante. Su período es 180°.",
        ],
        "solution": [
            "Despejamos: `tan(x) = −√3`.",
            "Ángulo de referencia: `tan 60° = √3` → referencia `60°`.",
            "La tangente es negativa en el 2.° y en el 4.° cuadrante. En el 2.°: `x = 180° − 60° = 120°`. En el 4.°: `x = 360° − 60° = 300°`.",
            "Las dos soluciones están separadas exactamente 180° (el período de la tangente): `300° = 120° + 180°`.",
            "Solución general: `x = 120° + 180°·k`, con `k` entero (con `k = 0` y `k = 1` salen las dos del intervalo).",
            "Verificación: `tan 120° = sen 120° / cos 120° = (√3/2) / (−1/2) = −√3`. Error típico: sumar `360°·k` (se pierde la mitad de las soluciones) o quedarse con 60° olvidando el signo.",
        ],
    },
    {
        "id": "t-ecuaciones-trigonometricas-2",
        "node": "t-ecuaciones-trigonometricas",
        "kind": "problem",
        "level": 2,
        "title": "Coseno de un ángulo triple",
        "statement": (
            "Resolvé la ecuación `2·cos(3x) + 1 = 0` en el intervalo `[0°, 360°)`.\n\n"
            "Dato: `cos 60° = 1/2`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuántas soluciones tiene en [0°, 360°)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""},
                "answer": "6 soluciones",
            },
            {
                "prompt": "b) ¿Cuál es la menor solución? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 40, "tolerance": 0, "unit": "°"},
                "answer": "40°",
            },
            {
                "prompt": "c) ¿Cuál es la mayor solución? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 320, "tolerance": 0, "unit": "°"},
                "answer": "320°",
            },
        ],
        "hints": [
            "Llamá `u = 3x` y resolvé primero `cos(u) = −1/2`: hay dos soluciones por vuelta.",
            "Escribí la solución general en `u` (sumando `360°·k`) ANTES de dividir por 3.",
            "Si `x` recorre `[0°, 360°)`, entonces `u = 3x` recorre `[0°, 1080°)`: tres vueltas completas.",
        ],
        "solution": [
            "Despejamos: `cos(3x) = −1/2`.",
            "Con `u = 3x`: el coseno vale `−1/2` con referencia 60° en el 2.° y 3.er cuadrante → `u = 120°` o `u = 240°` (más vueltas).",
            "Solución general en `u`: `3x = 120° + 360°·k` o `3x = 240° + 360°·k`.",
            "Recién ahora dividimos por 3: `x = 40° + 120°·k` o `x = 80° + 120°·k`.",
            "En `[0°, 360°)` con `k = 0, 1, 2`: de la primera familia `40°, 160°, 280°`; de la segunda `80°, 200°, 320°`.",
            "Total: **6 soluciones**: `40°, 80°, 160°, 200°, 280°, 320°`. La menor es `40°` y la mayor `320°`.",
            "Verificación: `x = 320°` → `3x = 960° = 240° + 2·360°` → `cos 240° = −1/2`. Error típico: dividir por 3 antes de sumar las vueltas y quedarse solo con 40° y 80°.",
        ],
    },
    {
        "id": "t-ecuaciones-trigonometricas-3",
        "node": "t-ecuaciones-trigonometricas",
        "kind": "problem",
        "level": 3,
        "title": "Identidad, cuadrática y una raíz que no sirve",
        "statement": (
            "Resolvé en el intervalo `[0°, 360°)` la ecuación\n\n"
            "`cos(2x) + 5·sen(x) + 2 = 0`."
        ),
        "parts": [
            {
                "prompt": "a) Después de usar una identidad de ángulo doble y ordenar, ¿qué ecuación cuadrática en sen(x) queda?",
                "check": {
                    "type": "choice",
                    "options": [
                        "2·sen²(x) − 5·sen(x) − 3 = 0",
                        "2·sen²(x) + 5·sen(x) + 3 = 0",
                        "2·sen²(x) − 5·sen(x) + 3 = 0",
                        "sen²(x) − 5·sen(x) − 3 = 0",
                    ],
                    "correct": 0,
                },
                "answer": "2·sen²(x) − 5·sen(x) − 3 = 0",
            },
            {
                "prompt": "b) ¿Cuántas soluciones tiene la ecuación original en [0°, 360°)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2 soluciones (210° y 330°)",
            },
            {
                "prompt": "c) ¿Cuánto vale la suma de todas las soluciones en [0°, 360°)? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 540, "tolerance": 0, "unit": "°"},
                "answer": "540° (210° + 330°)",
            },
        ],
        "hints": [
            "La ecuación mezcla `cos(2x)` con `sen(x)`. De las tres formas de `cos(2x)`, elegí la que solo tiene seno: `cos(2x) = 1 − 2·sen²(x)`.",
            "Llamá `s = sen(x)` y resolvé la cuadrática en `s` (factorizando o con la fórmula resolvente).",
            "No toda raíz de la cuadrática sirve: recordá que `−1 ≤ sen(x) ≤ 1`.",
        ],
        "solution": [
            "Usamos `cos(2x) = 1 − 2·sen²(x)`: `1 − 2·sen²(x) + 5·sen(x) + 2 = 0` → `−2·sen²(x) + 5·sen(x) + 3 = 0`.",
            "Multiplicamos por `−1`: `2·sen²(x) − 5·sen(x) − 3 = 0`.",
            "Con `s = sen(x)`: `2s² − 5s − 3 = 0`. Resolvente: `s = (5 ± √(25 + 24)) / 4 = (5 ± 7) / 4` → `s = 3` o `s = −1/2`. (Factorizado: `(2s + 1)(s − 3) = 0`.)",
            "`sen(x) = 3` es **imposible** (el seno vive entre −1 y 1): esa rama no aporta soluciones.",
            "`sen(x) = −1/2`: referencia 30°, seno negativo → 3.er y 4.° cuadrante: `x = 180° + 30° = 210°` y `x = 360° − 30° = 330°`.",
            "Hay **2 soluciones** en `[0°, 360°)`, y su suma es `210° + 330° = 540°`.",
            "Verificación con `x = 210°`: `cos(420°) = cos(60°) = 0.5`; `5·sen(210°) = −2.5`; `0.5 − 2.5 + 2 = 0`. Con `x = 330°`: `cos(660°) = cos(300°) = 0.5` y `5·sen(330°) = −2.5`, también da 0.",
            "Error típico: contar 4 soluciones creyendo que las dos raíces de la cuadrática aportan ángulos, o equivocar el signo al pasar `cos(2x)` a senos.",
        ],
    },
]
