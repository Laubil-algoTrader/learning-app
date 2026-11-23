"""Ejercicios de Álgebra 2 (primera parte): complejos, polinomios, expresiones racionales,
exponenciales, logaritmos e inecuaciones. Tres problemas por tema (niveles 1, 2 y 3)."""

EXERCISES: list[dict] = [
    # ==================== NÚMEROS COMPLEJOS ====================
    {
        "id": "a2-numeros-complejos-1",
        "node": "a2-numeros-complejos",
        "kind": "problem",
        "level": 1,
        "title": "Producto, potencia de i y forma binómica",
        "statement": "Dado el número complejo `z = (2 − 3i)(1 + 4i) + i²³`, escribilo en forma binómica `a + bi` (con `a` y `b` reales).",
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la parte real `a`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 14, "tolerance": 0, "unit": ""},
                "answer": "14",
            },
            {
                "prompt": "b) ¿Cuánto vale la parte imaginaria `b` (el coeficiente de `i`)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4",
            },
            {
                "prompt": "c) ¿Cuánto da el producto de `z` por su conjugado? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 212, "tolerance": 0, "unit": ""},
                "answer": "212",
            },
        ],
        "hints": [
            "Distribuí el producto y reemplazá `i²` por `−1`.",
            "Para `i²³` dividí 23 por 4 y quedate con el resto: las potencias de `i` se repiten cada 4.",
            "Un complejo por su conjugado da `a² + b²`.",
        ],
        "solution": [
            "Producto: `(2 − 3i)(1 + 4i) = 2 + 8i − 3i − 12i²`.",
            "Como `i² = −1`, `−12i² = +12`: queda `(2 + 12) + (8 − 3)i = 14 + 5i`.",
            "Potencia: `23 = 4 × 5 + 3`, así que `i²³ = i³ = −i`.",
            "Suma: `z = 14 + 5i − i = 14 + 4i`. Entonces `a = 14` y `b = 4`.",
            "El conjugado es `14 − 4i`, y el producto vale `14² + 4² = 196 + 16 = 212`. Error típico: dejar `−12i²` como `−12`, con lo que la parte real daría `−10`.",
        ],
    },
    {
        "id": "a2-numeros-complejos-2",
        "node": "a2-numeros-complejos",
        "kind": "problem",
        "level": 2,
        "title": "División de complejos y módulo",
        "statement": "Sea `z = (11 + 2i)/(2 − i)`. Escribí `z` en forma binómica `a + bi` y calculá su módulo.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la parte real de `z`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4",
            },
            {
                "prompt": "b) ¿Cuánto vale la parte imaginaria de `z` (el coeficiente de `i`)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3",
            },
            {
                "prompt": "c) ¿Cuánto vale el módulo `|z|`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                "answer": "5",
            },
        ],
        "hints": [
            "Para dividir complejos se multiplica arriba y abajo por el conjugado del denominador.",
            "`(2 − i)(2 + i) = 2² + 1² = 5`: el denominador queda real.",
        ],
        "solution": [
            "Multiplicamos numerador y denominador por el conjugado del denominador, `2 + i`: `z = (11 + 2i)(2 + i)/((2 − i)(2 + i))`.",
            "Denominador: `(2 − i)(2 + i) = 2² + 1² = 5`.",
            "Numerador: `(11 + 2i)(2 + i) = 22 + 11i + 4i + 2i² = 22 + 15i − 2 = 20 + 15i`.",
            "Dividimos cada parte por 5: `z = 4 + 3i`. Parte real 4, parte imaginaria 3.",
            "Módulo: `|z| = √(4² + 3²) = √25 = 5`.",
            "Verificación: `(4 + 3i)(2 − i) = 8 − 4i + 6i − 3i² = 11 + 2i` ✓. Error típico: dividir «parte por parte» (`11/2` y `2/(−1)`), que no es válido entre complejos.",
        ],
    },
    {
        "id": "a2-numeros-complejos-3",
        "node": "a2-numeros-complejos",
        "kind": "problem",
        "level": 3,
        "title": "Polinomio cúbico con una raíz compleja conocida",
        "statement": "El polinomio `P(x) = x³ − 5x² + 17x − 13` tiene coeficientes reales y se sabe que `x = 2 + 3i` es una de sus raíces. Hallá las otras dos raíces y factorizá `P` en ℝ.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el factor cuadrático con coeficientes reales que reúne a las dos raíces complejas de `P`?",
                "check": {
                    "type": "choice",
                    "options": ["x² + 4x + 13", "x² − 4x + 13", "x² − 4x − 5", "x² − 4x + 5"],
                    "correct": 1,
                },
                "answer": "x² − 4x + 13",
            },
            {
                "prompt": "b) ¿Cuál es la raíz real de `P`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1",
            },
            {
                "prompt": "c) ¿Cuánto vale el producto de las tres raíces de `P`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 13, "tolerance": 0, "unit": ""},
                "answer": "13",
            },
        ],
        "hints": [
            "En un polinomio con coeficientes reales, las raíces complejas vienen de a pares conjugados.",
            "Multiplicá `(x − (2 + 3i))(x − (2 − 3i))`: es `(x − 2)² − (3i)²`.",
            "`P` es de grado 3: el factor que falta es de grado 1. Dividí `P` por el factor cuadrático o compará los términos independientes.",
        ],
        "solution": [
            "Como los coeficientes de `P` son reales, si `2 + 3i` es raíz, su conjugado `2 − 3i` también lo es.",
            "Factor cuadrático: `(x − (2 + 3i))(x − (2 − 3i)) = (x − 2)² − (3i)² = x² − 4x + 4 + 9 = x² − 4x + 13`.",
            "`P` es de grado 3 y su coeficiente principal es 1, así que `P(x) = (x² − 4x + 13)(x − c)`. Comparando términos independientes: `13 · (−c) = −13` → `c = 1`.",
            "Comprobamos expandiendo: `(x² − 4x + 13)(x − 1) = x³ − x² − 4x² + 4x + 13x − 13 = x³ − 5x² + 17x − 13` ✓.",
            "Las raíces son `2 + 3i`, `2 − 3i` y `1`. La raíz real es `x = 1` (también se ve con `P(1) = 1 − 5 + 17 − 13 = 0`).",
            "Producto de las raíces: `(2 + 3i)(2 − 3i) · 1 = (4 + 9) · 1 = 13`. Como `x² − 4x + 13` tiene `Δ = 16 − 52 = −36 < 0`, la factorización completa en ℝ es `(x − 1)(x² − 4x + 13)`.",
        ],
    },
    # ==================== POLINOMIOS: ARITMÉTICA Y FACTORIZACIÓN ====================
    {
        "id": "a2-polinomios-factorizacion-1",
        "node": "a2-polinomios-factorizacion",
        "kind": "problem",
        "level": 1,
        "title": "Factor común, agrupación y diferencia de cuadrados",
        "statement": "Factorizá por completo el polinomio `P(x) = 2x³ + 6x² − 8x − 24`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la factorización completa de `P`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "2(x − 3)(x − 2)(x + 2)",
                        "(x + 3)(x − 2)(x + 2)",
                        "2(x + 3)(x − 2)(x + 2)",
                        "2(x + 3)(x − 2)²",
                    ],
                    "correct": 2,
                },
                "answer": "2(x + 3)(x − 2)(x + 2)",
            },
            {
                "prompt": "b) ¿Cuánto vale la suma de las tres raíces de `P`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -3, "tolerance": 0, "unit": ""},
                "answer": "−3",
            },
        ],
        "hints": [
            "Primero sacá el factor común numérico.",
            "Lo que queda tiene 4 términos: agrupá de a pares y buscá un paréntesis repetido.",
        ],
        "solution": [
            "Factor común 2: `P(x) = 2(x³ + 3x² − 4x − 12)`.",
            "Agrupamos de a pares: `x³ + 3x² = x²(x + 3)` y `−4x − 12 = −4(x + 3)`.",
            "Sacamos el paréntesis repetido: `x²(x + 3) − 4(x + 3) = (x + 3)(x² − 4)`.",
            "`x² − 4` es una diferencia de cuadrados: `(x − 2)(x + 2)`. Entonces `P(x) = 2(x + 3)(x − 2)(x + 2)`.",
            "Las raíces son `−3`, `2` y `−2`, y suman `−3`. Verificación: `P(2) = 16 + 24 − 16 − 24 = 0` ✓. Error típico: olvidarse del 2 de adelante o dejar `x² − 4` sin factorizar.",
        ],
    },
    {
        "id": "a2-polinomios-factorizacion-2",
        "node": "a2-polinomios-factorizacion",
        "kind": "problem",
        "level": 2,
        "title": "Binomio a la cuarta con el Triángulo de Pascal",
        "statement": "Desarrollá `(2x − 3)⁴` y escribí el resultado como un polinomio ordenado por potencias de `x`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el coeficiente de `x³`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -96, "tolerance": 0, "unit": ""},
                "answer": "−96",
            },
            {
                "prompt": "b) ¿Cuál es el coeficiente de `x²`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 216, "tolerance": 0, "unit": ""},
                "answer": "216",
            },
            {
                "prompt": "c) ¿Cuánto vale la suma de todos los coeficientes del polinomio (incluido el término independiente)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1",
            },
        ],
        "hints": [
            "La fila 4 del Triángulo de Pascal es 1, 4, 6, 4, 1.",
            "Tomá `a = 2x` y `b = −3`: las potencias de `a` bajan de 4 a 0 y las de `b` suben de 0 a 4. Ojo con el signo de las potencias impares de `−3`.",
            "La suma de los coeficientes de un polinomio es su valor en `x = 1`.",
        ],
        "solution": [
            "`(a + b)⁴ = a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴`, con `a = 2x` y `b = −3`.",
            "`a⁴ = (2x)⁴ = 16x⁴`.",
            "`4a³b = 4 · 8x³ · (−3) = −96x³`.",
            "`6a²b² = 6 · 4x² · 9 = 216x²`.",
            "`4ab³ = 4 · 2x · (−27) = −216x` y `b⁴ = (−3)⁴ = 81`.",
            "Resultado: `(2x − 3)⁴ = 16x⁴ − 96x³ + 216x² − 216x + 81`.",
            "Suma de coeficientes: `16 − 96 + 216 − 216 + 81 = 1`, que coincide con evaluar en `x = 1`: `(2 − 3)⁴ = 1` ✓. Error típico: escribir `16x⁴ + 81` y perder los términos cruzados.",
        ],
    },
    {
        "id": "a2-polinomios-factorizacion-3",
        "node": "a2-polinomios-factorizacion",
        "kind": "problem",
        "level": 3,
        "title": "Forma cuadrática en x³, suma y diferencia de cubos",
        "statement": "Factorizá por completo en ℝ el polinomio `P(x) = x⁶ − 7x³ − 8` y hallá sus raíces reales.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la factorización completa de `P` en ℝ?",
                "check": {
                    "type": "choice",
                    "options": [
                        "(x − 2)(x² + 2x + 4)(x + 1)(x² − x + 1)",
                        "(x − 2)(x² − 2x + 4)(x + 1)(x² + x + 1)",
                        "(x + 2)(x² − 2x + 4)(x − 1)(x² + x + 1)",
                        "(x − 2)³(x + 1)³",
                    ],
                    "correct": 0,
                },
                "answer": "(x − 2)(x² + 2x + 4)(x + 1)(x² − x + 1)",
            },
            {
                "prompt": "b) ¿Cuántas raíces reales distintas tiene `P`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
            {
                "prompt": "c) ¿Cuánto vale la suma de las raíces reales de `P`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1",
            },
        ],
        "hints": [
            "Es una forma cuadrática: probá con `u = x³`.",
            "Te van a quedar una diferencia de cubos y una suma de cubos.",
            "Mirá el discriminante de cada factor cuadrático para saber si se puede seguir factorizando en ℝ.",
        ],
        "solution": [
            "Con `u = x³`: `u² − 7u − 8 = (u − 8)(u + 1)` (dos números que multiplicados dan −8 y sumados −7: −8 y 1).",
            "Volvemos a `x`: `P(x) = (x³ − 8)(x³ + 1)`.",
            "Diferencia de cubos: `x³ − 8 = (x − 2)(x² + 2x + 4)`.",
            "Suma de cubos: `x³ + 1 = (x + 1)(x² − x + 1)`.",
            "Los factores cuadráticos no tienen raíces reales: `x² + 2x + 4` tiene `Δ = 4 − 16 = −12` y `x² − x + 1` tiene `Δ = 1 − 4 = −3`. No se factorizan más en ℝ.",
            "`P(x) = (x − 2)(x² + 2x + 4)(x + 1)(x² − x + 1)`. Las raíces reales son `2` y `−1`: son dos y suman `1`.",
            "Verificación: `P(2) = 64 − 56 − 8 = 0` y `P(−1) = 1 + 7 − 8 = 0` ✓. Error típico: confundir los signos del trinomio (en `a³ − b³` el del medio es `+ab`; en `a³ + b³` es `−ab`).",
        ],
    },
    # ==================== EXPRESIONES RACIONALES Y RACIONALIZACIÓN ====================
    {
        "id": "a2-expresiones-racionales-1",
        "node": "a2-expresiones-racionales",
        "kind": "problem",
        "level": 1,
        "title": "Producto de expresiones racionales y dominio",
        "statement": "Considerá la expresión `E(x) = (x² − 1)/(x² + 4x + 4) · (x² + 2x)/(x² − x)`.",
        "parts": [
            {
                "prompt": "a) ¿Cuántos valores reales de `x` hay que excluir del dominio de `E`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3 (x = −2, x = 0 y x = 1)",
            },
            {
                "prompt": "b) ¿Cuál es la expresión simplificada de `E(x)`, válida en ese dominio?",
                "check": {
                    "type": "choice",
                    "options": ["(x − 1)/(x + 2)", "(x + 1)/(x + 2)²", "x(x + 1)/(x + 2)", "(x + 1)/(x + 2)"],
                    "correct": 3,
                },
                "answer": "(x + 1)/(x + 2)",
            },
        ],
        "hints": [
            "Factorizá los cuatro polinomios antes de multiplicar.",
            "El dominio se decide con los denominadores ORIGINALES, antes de cancelar nada.",
        ],
        "solution": [
            "Factorizamos todo: `x² − 1 = (x − 1)(x + 1)`, `x² + 4x + 4 = (x + 2)²`, `x² + 2x = x(x + 2)` y `x² − x = x(x − 1)`.",
            "Dominio: los denominadores originales se anulan en `x = −2` (por `(x + 2)²`) y en `x = 0` y `x = 1` (por `x(x − 1)`). Son 3 valores excluidos.",
            "Producto: `E(x) = (x − 1)(x + 1) · x(x + 2) / ((x + 2)² · x(x − 1))`.",
            "Cancelamos los factores comunes `(x − 1)`, `x` y un `(x + 2)`: queda `E(x) = (x + 1)/(x + 2)`.",
            "Respuesta: `(x + 1)/(x + 2)`, con `x ≠ −2`, `x ≠ 0` y `x ≠ 1`. Verificación con `x = 2`: la original da `3/16 · 8/2 = 3/4` y la simplificada `3/4` ✓. Las restricciones `x ≠ 0` y `x ≠ 1` se conservan aunque esos factores ya no se vean.",
        ],
    },
    {
        "id": "a2-expresiones-racionales-2",
        "node": "a2-expresiones-racionales",
        "kind": "problem",
        "level": 2,
        "title": "Racionalizar dos fracciones y combinarlas",
        "statement": "Simplificá `E = 6/(√7 − 2) − 3/(√7 + 2)` hasta escribirla en la forma `a + b√7`, con `a` y `b` enteros.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale `a`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""},
                "answer": "6",
            },
            {
                "prompt": "b) ¿Cuánto vale `b`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1",
            },
        ],
        "hints": [
            "Racionalizá cada fracción multiplicando arriba y abajo por el conjugado de su denominador.",
            "`(√7 − 2)(√7 + 2) = 7 − 4 = 3` en los dos casos.",
            "Al restar la segunda fracción, el signo menos afecta a todo su numerador.",
        ],
        "solution": [
            "Primera fracción: `6/(√7 − 2) · (√7 + 2)/(√7 + 2) = 6(√7 + 2)/(7 − 4) = 6(√7 + 2)/3 = 2√7 + 4`.",
            "Segunda fracción: `3/(√7 + 2) · (√7 − 2)/(√7 − 2) = 3(√7 − 2)/3 = √7 − 2`.",
            "Restamos, cuidando el signo del paréntesis: `E = (2√7 + 4) − (√7 − 2) = 2√7 + 4 − √7 + 2`.",
            "`E = 6 + √7`, es decir `a = 6` y `b = 1`.",
            "Verificación numérica con `√7 ≈ 2.6458`: `6/0.64575 − 3/4.64575 ≈ 9.2915 − 0.6458 ≈ 8.6458 = 6 + √7` ✓. Error típico: no cambiar el signo del `−2` al restar, lo que daría `2 + √7`.",
        ],
    },
    {
        "id": "a2-expresiones-racionales-3",
        "node": "a2-expresiones-racionales",
        "kind": "problem",
        "level": 3,
        "title": "Operación combinada y una ecuación con trampa",
        "statement": "Sea `E(x) = [ (x + 3)/(x − 3) − (x − 3)/(x + 3) ] ÷ [ 1 − (x² + 9)/(x² − 9) ]`.",
        "parts": [
            {
                "prompt": "a) ¿Cuántos valores reales de `x` hay que excluir del dominio de `E`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2 (x = 3 y x = −3)",
            },
            {
                "prompt": "b) ¿Cuál es la expresión simplificada de `E(x)`, válida en su dominio?",
                "check": {
                    "type": "choice",
                    "options": ["2x/3", "−2x/3", "−3/(2x)", "−216x/(x² − 9)²"],
                    "correct": 1,
                },
                "answer": "−2x/3",
            },
            {
                "prompt": "c) ¿Cuál es la solución de la ecuación `E(x) = 2`?",
                "check": {
                    "type": "choice",
                    "options": ["x = −3", "x = 3", "x = −3/4", "No tiene solución"],
                    "correct": 3,
                },
                "answer": "No tiene solución: el único candidato, x = −3, no pertenece al dominio de E.",
            },
        ],
        "hints": [
            "Trabajá cada corchete por separado hasta dejarlo como una sola fracción con denominador `x² − 9`.",
            "Dividir es multiplicar por la recíproca del segundo corchete.",
            "Antes de dar por buena una solución de `E(x) = 2`, fijate si pertenece al dominio de la expresión original.",
        ],
        "solution": [
            "Dominio: `x² − 9 = (x − 3)(x + 3)`, así que `x ≠ 3` y `x ≠ −3`.",
            "Primer corchete, con denominador común `(x − 3)(x + 3)`: `[(x + 3)² − (x − 3)²]/(x² − 9)`.",
            "`(x + 3)² − (x − 3)² = (x² + 6x + 9) − (x² − 6x + 9) = 12x`. El primer corchete vale `12x/(x² − 9)`.",
            "Segundo corchete: `1 − (x² + 9)/(x² − 9) = (x² − 9 − x² − 9)/(x² − 9) = −18/(x² − 9)`. Nunca vale 0, así que no agrega restricciones: los valores excluidos son 2.",
            "Dividir es multiplicar por la recíproca: `E(x) = 12x/(x² − 9) · (x² − 9)/(−18) = 12x/(−18) = −2x/3`.",
            "Ecuación: `−2x/3 = 2` → `x = −3`. Pero `x = −3` anula denominadores de la expresión original: no está en el dominio, así que la ecuación no tiene solución.",
            "Verificación de la simplificación con `x = 1`: primer corchete `4/(−2) − (−2)/4 = −1.5`; segundo `1 − 10/(−8) = 2.25`; cociente `−1.5/2.25 = −2/3` ✓.",
        ],
    },
    # ==================== DIVISIÓN DE POLINOMIOS Y TEOREMA DEL RESTO ====================
    {
        "id": "a2-division-polinomios-1",
        "node": "a2-division-polinomios",
        "kind": "problem",
        "level": 1,
        "title": "Ruffini con un término faltante",
        "statement": "Dividí `P(x) = 2x⁴ − 3x³ − 10x + 5` por `(x − 2)`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el cociente de la división?",
                "check": {
                    "type": "choice",
                    "options": [
                        "2x³ + x² − 8x − 11",
                        "2x³ + x² + 2x − 6",
                        "2x³ − 7x² + 14x − 38",
                        "2x³ + x² + 2x + 6",
                    ],
                    "correct": 1,
                },
                "answer": "2x³ + x² + 2x − 6",
            },
            {
                "prompt": "b) ¿Cuánto vale el resto? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -7, "tolerance": 0, "unit": ""},
                "answer": "−7",
            },
        ],
        "hints": [
            "Fijate si en `P(x)` falta alguna potencia de `x`: su columna lleva un 0.",
            "El divisor `(x − 2)` se anula en `x = 2`: ese es el número que va a la izquierda en Ruffini.",
        ],
        "solution": [
            "Completamos con 0 el término que falta (`x²`): los coeficientes son `2, −3, 0, −10, 5`. El divisor `(x − 2)` se anula en `x = 2`.",
            "Bajamos el 2. `2 × 2 = 4` y `−3 + 4 = 1`.",
            "`1 × 2 = 2` y `0 + 2 = 2`.",
            "`2 × 2 = 4` y `−10 + 4 = −6`.",
            "`−6 × 2 = −12` y `5 − 12 = −7`. La fila final es `2, 1, 2, −6 | −7`.",
            "Cociente `2x³ + x² + 2x − 6` y resto `−7`. Verificación con el Teorema del Resto: `P(2) = 32 − 24 − 20 + 5 = −7` ✓.",
        ],
    },
    {
        "id": "a2-division-polinomios-2",
        "node": "a2-division-polinomios",
        "kind": "problem",
        "level": 2,
        "title": "División larga por un divisor de grado 2",
        "statement": "Dividí `P(x) = x⁴ − 3x³ + 2x² + 5x − 1` por `D(x) = x² − x + 2` y escribí `P(x) = D(x) · Q(x) + R(x)`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el cociente `Q(x)`?",
                "check": {
                    "type": "choice",
                    "options": ["x² − 2x + 2", "x² + 2x − 2", "x² − 2x − 2", "x² − 4x + 4"],
                    "correct": 2,
                },
                "answer": "x² − 2x − 2",
            },
            {
                "prompt": "b) ¿Cuál es el resto `R(x)`?",
                "check": {
                    "type": "choice",
                    "options": ["7x + 3", "7x − 5", "3x + 3", "−7x − 3"],
                    "correct": 0,
                },
                "answer": "7x + 3",
            },
        ],
        "hints": [
            "Ruffini no sirve acá porque el divisor es de grado 2: usá la división larga.",
            "En cada paso dividí el término de mayor grado de lo que queda por `x²`, multiplicá el resultado por todo el divisor y restá.",
            "Frená cuando lo que queda tenga grado menor que 2.",
        ],
        "solution": [
            "`x⁴ ÷ x² = x²`. Multiplicamos: `x² · D(x) = x⁴ − x³ + 2x²`. Restamos de `P(x)`: queda `−2x³ + 0x² + 5x − 1`.",
            "`−2x³ ÷ x² = −2x`. Multiplicamos: `−2x · D(x) = −2x³ + 2x² − 4x`. Restamos: `(−2x³ + 0x² + 5x − 1) − (−2x³ + 2x² − 4x) = −2x² + 9x − 1`.",
            "`−2x² ÷ x² = −2`. Multiplicamos: `−2 · D(x) = −2x² + 2x − 4`. Restamos: `(−2x² + 9x − 1) − (−2x² + 2x − 4) = 7x + 3`.",
            "`7x + 3` tiene grado 1, menor que el del divisor: es el resto. El cociente es `Q(x) = x² − 2x − 2` y el resto `R(x) = 7x + 3`.",
            "Verificación: `(x² − x + 2)(x² − 2x − 2) = x⁴ − 3x³ + 2x² − 2x − 4`, y sumando `7x + 3` da `x⁴ − 3x³ + 2x² + 5x − 1` ✓. Error típico: equivocar un signo al restar (hay que cambiar el signo de TODOS los términos del producto).",
        ],
    },
    {
        "id": "a2-division-polinomios-3",
        "node": "a2-division-polinomios",
        "kind": "problem",
        "level": 3,
        "title": "Dos parámetros para una división exacta",
        "statement": "Hallá los números reales `a` y `b` para que `P(x) = x⁴ + ax³ + bx² − 8x + 4` sea divisible por `x² − 3x + 2`, y calculá el cociente de esa división.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale `a`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -4, "tolerance": 0, "unit": ""},
                "answer": "−4",
            },
            {
                "prompt": "b) ¿Cuánto vale `b`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": ""},
                "answer": "7",
            },
            {
                "prompt": "c) ¿Cuál es el cociente de dividir `P(x)` por `x² − 3x + 2`?",
                "check": {
                    "type": "choice",
                    "options": ["x² + x + 2", "x² − x − 2", "x² − 7x + 2", "x² − x + 2"],
                    "correct": 3,
                },
                "answer": "x² − x + 2",
            },
        ],
        "hints": [
            "Factorizá el divisor: si `P` es divisible por un producto, es divisible por cada factor.",
            "Teorema del Factor: tienen que cumplirse `P(1) = 0` y `P(2) = 0`. Son dos ecuaciones con dos incógnitas.",
            "Con `a` y `b` ya calculados, dividí dos veces por Ruffini: primero por `(x − 1)` y el cociente por `(x − 2)`.",
        ],
        "solution": [
            "`x² − 3x + 2 = (x − 1)(x − 2)`. `P` es divisible por ese producto si y solo si `P(1) = 0` y `P(2) = 0`.",
            "`P(1) = 1 + a + b − 8 + 4 = a + b − 3 = 0` → `a + b = 3`.",
            "`P(2) = 16 + 8a + 4b − 16 + 4 = 8a + 4b + 4 = 0` → `2a + b = −1`.",
            "Restando las ecuaciones: `(2a + b) − (a + b) = −1 − 3` → `a = −4`, y entonces `b = 3 − (−4) = 7`.",
            "Queda `P(x) = x⁴ − 4x³ + 7x² − 8x + 4`. Ruffini con 1 sobre `1, −4, 7, −8, 4` da `1, −3, 4, −4 | 0`.",
            "Ruffini con 2 sobre `1, −3, 4, −4` da `1, −1, 2 | 0`. El cociente es `x² − x + 2`.",
            "Verificación: `(x² − 3x + 2)(x² − x + 2) = x⁴ − 4x³ + 7x² − 8x + 4` ✓. Entonces `a = −4`, `b = 7` y el cociente es `x² − x + 2`.",
        ],
    },
    # ==================== RAÍCES RACIONALES Y FACTORIZACIÓN COMPLETA ====================
    {
        "id": "a2-raices-racionales-factorizacion-1",
        "node": "a2-raices-racionales-factorizacion",
        "kind": "problem",
        "level": 1,
        "title": "Gauss y Ruffini en una cúbica",
        "statement": "Hallá todas las raíces de `P(x) = x³ + 2x² − 13x + 10` y factorizalo por completo.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la factorización completa de `P`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "(x + 1)(x + 2)(x − 5)",
                        "(x − 1)(x + 2)(x − 5)",
                        "(x − 1)(x − 2)(x + 5)",
                        "(x − 1)(x − 2)(x − 5)",
                    ],
                    "correct": 2,
                },
                "answer": "(x − 1)(x − 2)(x + 5)",
            },
            {
                "prompt": "b) ¿Cuál es la menor de las raíces de `P`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -5, "tolerance": 0, "unit": ""},
                "answer": "−5",
            },
        ],
        "hints": [
            "Los candidatos a raíz racional son los divisores del término independiente, con los dos signos.",
            "Cuando encuentres una raíz, bajá el grado con Ruffini y factorizá la cuadrática que queda.",
        ],
        "solution": [
            "Candidatos (el coeficiente principal es 1): divisores de 10 → `±1, ±2, ±5, ±10`.",
            "`P(1) = 1 + 2 − 13 + 10 = 0`: `x = 1` es raíz y `(x − 1)` es factor.",
            "Ruffini con 1 sobre `1, 2, −13, 10` da `1, 3, −10 | 0`. El cociente es `x² + 3x − 10`.",
            "`x² + 3x − 10 = (x + 5)(x − 2)` (dos números que multiplicados dan −10 y sumados 3: 5 y −2).",
            "`P(x) = (x − 1)(x − 2)(x + 5)`. Las raíces son `1`, `2` y `−5`; la menor es `−5`.",
            "Verificación: `P(−5) = −125 + 50 + 65 + 10 = 0` ✓ y `P(2) = 8 + 8 − 26 + 10 = 0` ✓. Error típico: escribir los factores con el signo de la raíz (`(x + 1)` para la raíz 1).",
        ],
    },
    {
        "id": "a2-raices-racionales-factorizacion-2",
        "node": "a2-raices-racionales-factorizacion",
        "kind": "problem",
        "level": 2,
        "title": "Raíz fraccionaria y factor cuadrático irreducible",
        "statement": "Sea `P(x) = 2x³ + x² + 3x − 2`. Encontrá sus raíces racionales y factorizalo por completo en ℝ.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la única raíz racional de `P`? Respondé solo con el número (podés escribirlo como fracción).",
                "check": {"type": "numeric", "value": 0.5, "tolerance": 0, "unit": ""},
                "answer": "1/2 (es decir, 0.5)",
            },
            {
                "prompt": "b) ¿Cuál es la factorización completa de `P` en ℝ?",
                "check": {
                    "type": "choice",
                    "options": [
                        "(2x − 1)(x² + x + 2)",
                        "(x − 1/2)(x² + x + 2)",
                        "(2x + 1)(x² + x − 2)",
                        "(2x − 1)(x − 1)(x + 2)",
                    ],
                    "correct": 0,
                },
                "answer": "(2x − 1)(x² + x + 2)",
            },
            {
                "prompt": "c) ¿Cuántas raíces reales tiene `P` en total? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1",
            },
        ],
        "hints": [
            "Candidatos `p/q`: `p` divide al término independiente (−2) y `q` divide al coeficiente principal (2).",
            "`P(0) = −2` y `P(1) = 4` tienen signos opuestos: hay una raíz entre 0 y 1. ¿Qué candidato cae ahí?",
            "Después de Ruffini, mirá el discriminante del cociente.",
        ],
        "solution": [
            "Candidatos `p/q`: `p` divide a −2 (`±1, ±2`) y `q` divide a 2 (`1, 2`) → `±1, ±2, ±1/2`.",
            "Probamos los enteros: `P(1) = 2 + 1 + 3 − 2 = 4`, `P(−1) = −2 + 1 − 3 − 2 = −6`, `P(2) = 16 + 4 + 6 − 2 = 24`, `P(−2) = −16 + 4 − 6 − 2 = −20`. Ninguno es raíz.",
            "`P(1/2) = 2 · 1/8 + 1/4 + 3/2 − 2 = 1/4 + 1/4 + 3/2 − 2 = 0`: `x = 1/2` es raíz. En cambio `P(−1/2) = −1/4 + 1/4 − 3/2 − 2 = −7/2`.",
            "Ruffini con 1/2 sobre `2, 1, 3, −2` da `2, 2, 4 | 0`. Entonces `P(x) = (x − 1/2)(2x² + 2x + 4)`.",
            "Sacamos el 2 del cociente y lo metemos en el primer factor: `P(x) = (2x − 1)(x² + x + 2)`.",
            "`x² + x + 2` tiene `Δ = 1 − 8 = −7 < 0`: no tiene raíces reales y no se factoriza más en ℝ.",
            "La única raíz racional, y también la única raíz real, es `x = 1/2`. Verificación: `(2x − 1)(x² + x + 2) = 2x³ + 2x² + 4x − x² − x − 2 = 2x³ + x² + 3x − 2` ✓.",
        ],
    },
    {
        "id": "a2-raices-racionales-factorizacion-3",
        "node": "a2-raices-racionales-factorizacion",
        "kind": "problem",
        "level": 3,
        "title": "Grado 4 con coeficiente principal 2 y una raíz doble",
        "statement": "Factorizá por completo `P(x) = 2x⁴ − 5x³ − 3x² + 8x + 4` y analizá sus raíces.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la factorización completa de `P`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "(2x − 1)(x − 1)(x + 2)²",
                        "(x + 1/2)(x + 1)(x − 2)²",
                        "(2x + 1)(x + 1)(x − 2)(x + 2)",
                        "(2x + 1)(x + 1)(x − 2)²",
                    ],
                    "correct": 3,
                },
                "answer": "(2x + 1)(x + 1)(x − 2)²",
            },
            {
                "prompt": "b) ¿Cuál es la multiplicidad de la raíz `x = 2`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2 (raíz doble)",
            },
            {
                "prompt": "c) ¿Cuánto vale la suma de las raíces DISTINTAS de `P` (cada una contada una sola vez)? Respondé solo con el número (podés escribirlo como fracción).",
                "check": {"type": "numeric", "value": 0.5, "tolerance": 0, "unit": ""},
                "answer": "1/2 (es decir, 0.5): −1 + (−1/2) + 2",
            },
        ],
        "hints": [
            "Candidatos: divisores de 4 sobre divisores de 2. Empezá por los enteros.",
            "Cada raíz que encuentres baja un grado con Ruffini; seguí trabajando sobre el cociente, no sobre `P`.",
            "Al llegar a la cuadrática usá la resolvente y no te olvides del coeficiente principal 2 al escribir los factores.",
        ],
        "solution": [
            "Candidatos: divisores de 4 sobre divisores de 2 → `±1, ±2, ±4, ±1/2`.",
            "`P(1) = 2 − 5 − 3 + 8 + 4 = 6` (no es raíz); `P(−1) = 2 + 5 − 3 − 8 + 4 = 0` ✓. Ruffini con −1 sobre `2, −5, −3, 8, 4` da `2, −7, 4, 4 | 0`: el cociente es `Q(x) = 2x³ − 7x² + 4x + 4`.",
            "En el cociente, `Q(2) = 16 − 28 + 8 + 4 = 0` ✓. Ruffini con 2 sobre `2, −7, 4, 4` da `2, −3, −2 | 0`: el nuevo cociente es `2x² − 3x − 2`.",
            "Resolvente: `x = (3 ± √(9 + 16))/4 = (3 ± 5)/4` → `x = 2` o `x = −1/2`. Entonces `2x² − 3x − 2 = 2(x − 2)(x + 1/2) = (x − 2)(2x + 1)`.",
            "`P(x) = (x + 1)(x − 2)(x − 2)(2x + 1) = (2x + 1)(x + 1)(x − 2)²`.",
            "El factor `(x − 2)` aparece dos veces: `x = 2` es raíz doble (multiplicidad 2). Las raíces distintas son `−1`, `−1/2` y `2`, y suman `1/2`.",
            "Verificación: el término independiente del producto es `1 · 1 · (−2)² = 4` ✓ y el coeficiente principal es `2` ✓. Error típico: escribir `(x + 1/2)` sin el 2, con lo que el producto ya no reconstruye a `P`.",
        ],
    },
    # ==================== GRÁFICAS DE POLINOMIOS ====================
    {
        "id": "a2-graficas-polinomios-1",
        "node": "a2-graficas-polinomios",
        "kind": "problem",
        "level": 1,
        "title": "Leer una gráfica desde la forma factorizada",
        "statement": "Considerá el polinomio `P(x) = −x(x − 2)²(x + 3)`. Sin hacer una tabla de valores, describí su gráfica.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el grado de `P`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4",
            },
            {
                "prompt": "b) ¿Cómo se comporta la gráfica en los extremos (`x → −∞` y `x → +∞`)?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Los dos extremos van hacia arriba (+∞)",
                        "Baja a la izquierda (−∞) y sube a la derecha (+∞)",
                        "Los dos extremos van hacia abajo (−∞)",
                        "Sube a la izquierda (+∞) y baja a la derecha (−∞)",
                    ],
                    "correct": 2,
                },
                "answer": "Los dos extremos van hacia abajo (−∞)",
            },
            {
                "prompt": "c) ¿En qué valor de `x` la gráfica toca el eje X sin cruzarlo? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
        ],
        "hints": [
            "El grado es la suma de los exponentes de todos los factores que tienen `x`.",
            "Para los extremos solo importa el término líder: multiplicá la potencia más alta de cada factor, sin olvidar el signo menos de adelante.",
            "La gráfica rebota donde el factor tiene exponente par.",
        ],
        "solution": [
            "Grado: sumamos los exponentes de los factores con `x`: `1 + 2 + 1 = 4`.",
            "Término líder: `−x · x² · x = −x⁴`. Grado par y coeficiente negativo → los dos extremos van hacia `−∞`.",
            "Ceros: `x = 0` (multiplicidad 1), `x = 2` (multiplicidad 2) y `x = −3` (multiplicidad 1).",
            "Multiplicidad impar → cruza (en `x = −3` y en `x = 0`); multiplicidad par → rebota (en `x = 2`).",
            "Respuestas: grado 4, ambos extremos hacia abajo y rebote en `x = 2`. Control: `P(1) = −1 · 1 · 4 = −4` y `P(3) = −3 · 1 · 6 = −18`, negativo a ambos lados de 2, como corresponde a un rebote.",
        ],
    },
    {
        "id": "a2-graficas-polinomios-2",
        "node": "a2-graficas-polinomios",
        "kind": "problem",
        "level": 2,
        "title": "Reconstruir el polinomio a partir de su gráfica",
        "statement": "La gráfica de un polinomio `P` de grado 3 toca el eje X sin cruzarlo en `x = 2`, lo cruza en `x = −1` y pasa por el punto `(0, 8)`.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale el coeficiente principal de `P`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
            {
                "prompt": "b) ¿Cuánto vale `P(1)`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4",
            },
            {
                "prompt": "c) ¿En qué conjunto se cumple `P(x) > 0`?",
                "check": {
                    "type": "choice",
                    "options": ["(−1, +∞)", "(−1, 2) ∪ (2, +∞)", "(−∞, −1)", "(−∞, −1) ∪ (2, +∞)"],
                    "correct": 1,
                },
                "answer": "(−1, 2) ∪ (2, +∞)",
            },
        ],
        "hints": [
            "Un rebote indica multiplicidad par y un cruce, multiplicidad impar. El grado total tiene que ser 3.",
            "Escribí `P(x) = a(x − 2)²(x + 1)` y usá el punto `(0, 8)` para hallar `a`.",
            "Para el signo, fijate que un factor elevado al cuadrado nunca es negativo.",
        ],
        "solution": [
            "Rebote en `x = 2` → el factor `(x − 2)` tiene multiplicidad par; cruce en `x = −1` → el factor `(x + 1)` tiene multiplicidad impar. Para que el grado sea 3, la única posibilidad es `(x − 2)²(x + 1)`.",
            "`P(x) = a(x − 2)²(x + 1)`. Con el punto `(0, 8)`: `P(0) = a · 4 · 1 = 4a = 8` → `a = 2`.",
            "`P(x) = 2(x − 2)²(x + 1)`; al expandir, el término líder es `2x³`: el coeficiente principal es 2.",
            "`P(1) = 2 · (1 − 2)² · (1 + 1) = 2 · 1 · 2 = 4`.",
            "Signo: `2(x − 2)²` es positivo salvo en `x = 2`, donde vale 0. Entonces el signo de `P` es el de `(x + 1)`: positivo si `x > −1`, quitando `x = 2`.",
            "`P(x) > 0` en `(−1, 2) ∪ (2, +∞)`. Error típico: responder `(−1, +∞)`, que incluye a `x = 2`, donde `P` vale 0 y no es positivo.",
        ],
    },
    {
        "id": "a2-graficas-polinomios-3",
        "node": "a2-graficas-polinomios",
        "kind": "problem",
        "level": 3,
        "title": "Análisis completo de un polinomio de grado 5",
        "statement": "Sea `P(x) = x⁵ − 3x⁴ − 4x³ + 12x²`. Factorizalo por completo y usá sus ceros, las multiplicidades y el término líder para bosquejar la gráfica.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la factorización completa de `P`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "x²(x + 3)(x − 2)(x + 2)",
                        "x²(x − 3)(x − 2)(x + 2)",
                        "x²(x − 3)(x − 2)²",
                        "x(x − 3)(x − 2)(x + 2)",
                    ],
                    "correct": 1,
                },
                "answer": "x²(x − 3)(x − 2)(x + 2)",
            },
            {
                "prompt": "b) Recorriendo la gráfica de izquierda a derecha, ¿cuál es la descripción correcta?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Sube desde −∞, cruza en x = −2, rebota en x = 0 quedando por encima del eje, cruza en x = 2, cruza en x = 3 y sigue hacia +∞",
                        "Sube desde −∞, cruza en x = −2, rebota en x = 0 quedando por debajo del eje, cruza en x = 2, cruza en x = 3 y sigue hacia +∞",
                        "Sube desde −∞, cruza en x = −2, cruza en x = 0, cruza en x = 2, cruza en x = 3 y sigue hacia +∞",
                        "Baja desde +∞, cruza en x = −2, rebota en x = 0 quedando por debajo del eje, cruza en x = 2, cruza en x = 3 y sigue hacia −∞",
                    ],
                    "correct": 0,
                },
                "answer": "Sube desde −∞, cruza en x = −2, rebota en x = 0 quedando por encima del eje, cruza en x = 2, cruza en x = 3 y sigue hacia +∞",
            },
            {
                "prompt": "c) ¿Cuántos giros (máximos y mínimos locales) tiene exactamente la gráfica? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4",
            },
        ],
        "hints": [
            "Sacá factor común `x²` y factorizá por agrupación lo que queda.",
            "Probá el signo de `P` con un valor en cada intervalo entre ceros consecutivos.",
            "Entre dos ceros consecutivos la curva tiene que darse vuelta al menos una vez, y un rebote también es un giro. Compará con el máximo posible, `n − 1`.",
        ],
        "solution": [
            "Factor común `x²`: `P(x) = x²(x³ − 3x² − 4x + 12)`.",
            "Agrupación: `x³ − 3x² − 4x + 12 = x²(x − 3) − 4(x − 3) = (x − 3)(x² − 4) = (x − 3)(x − 2)(x + 2)`. Entonces `P(x) = x²(x − 3)(x − 2)(x + 2)`.",
            "Ceros: `−2`, `2` y `3` (multiplicidad 1: la gráfica cruza) y `0` (multiplicidad 2: rebota). Término líder `x⁵` (grado impar, coeficiente positivo): viene de `−∞` por la izquierda y va a `+∞` por la derecha.",
            "Signos por intervalo: `P(−3) = 9 · (−6)(−5)(−1) = −270 < 0`; `P(−1) = 1 · (−4)(−3)(1) = 12 > 0`; `P(1) = 1 · (−2)(−1)(3) = 6 > 0`; `P(2.5) = 6.25 · (−0.5)(0.5)(4.5) < 0`; `P(4) = 16 · 1 · 2 · 6 = 192 > 0`.",
            "Recorrido: sube desde `−∞`, cruza en `x = −2` y queda por encima del eje; baja hasta tocar `x = 0` y rebota por arriba; vuelve a bajar y cruza en `x = 2`; queda por debajo y cruza hacia arriba en `x = 3`.",
            "Giros: un máximo entre `−2` y `0`, un mínimo en `x = 0` (el rebote), un máximo entre `0` y `2` y un mínimo entre `2` y `3`. Son al menos 4, y un polinomio de grado 5 tiene como máximo `5 − 1 = 4`: la gráfica tiene exactamente 4 giros.",
        ],
    },
    # ==================== MODELOS EXPONENCIALES ====================
    {
        "id": "a2-modelos-exponenciales-1",
        "node": "a2-modelos-exponenciales",
        "kind": "problem",
        "level": 1,
        "title": "Levaduras que se triplican",
        "statement": "En una cervecería artesanal de Bariloche, un cultivo de levaduras arranca con 200 millones de células y, mientras hay azúcar disponible, se triplica cada 5 horas. Modelá la cantidad `N(t)` (en millones de células) en función del tiempo `t` en horas.",
        "parts": [
            {
                "prompt": "a) ¿Cuántos millones de células hay a las 15 horas? Respondé solo con el número en millones de células.",
                "check": {"type": "numeric", "value": 5400, "tolerance": 0, "unit": "millones"},
                "answer": "5400 millones de células",
            },
            {
                "prompt": "b) ¿A las cuántas horas de empezar el cultivo llega a 16 200 millones de células? Respondé solo con el número en h.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "h"},
                "answer": "20 h",
            },
        ],
        "hints": [
            "Si una cantidad se multiplica por `b` cada `T` horas, el modelo es `N(t) = N₀ · b^(t/T)`.",
            "Para el inciso b, dividí por 200 y escribí el resultado como potencia de 3.",
        ],
        "solution": [
            "Modelo: valor inicial 200 y factor 3 cada 5 h → `N(t) = 200 · 3^(t/5)`.",
            "a) `N(15) = 200 · 3^(15/5) = 200 · 3³ = 200 · 27 = 5400` millones de células.",
            "b) `200 · 3^(t/5) = 16 200` → `3^(t/5) = 16 200/200 = 81`.",
            "`81 = 3⁴`, así que `t/5 = 4` → `t = 20 h`.",
            "Verificación: en 20 h hay 4 triplicaciones: `200 → 600 → 1800 → 5400 → 16 200` ✓. Error típico: usar `3^t` en lugar de `3^(t/5)`, como si se triplicara cada hora.",
        ],
    },
    {
        "id": "a2-modelos-exponenciales-2",
        "node": "a2-modelos-exponenciales",
        "kind": "problem",
        "level": 2,
        "title": "Del aumento trimestral a la tasa mensual",
        "statement": "En un período de inflación alta, una canasta de productos que hoy cuesta $ 400 000 aumenta 33.1% cada trimestre, a un ritmo mensual constante (crecimiento exponencial).",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la tasa de aumento mensual equivalente? Respondé solo con el número en %.",
                "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "%"},
                "answer": "10 %",
            },
            {
                "prompt": "b) ¿Cuánto cuesta la canasta al cabo de 2 meses? Respondé solo con el número en $.",
                "check": {"type": "numeric", "value": 484000, "tolerance": 0, "unit": "$"},
                "answer": "484 000 pesos",
            },
            {
                "prompt": "c) ¿Qué aumento porcentual acumula la canasta en 6 meses? Redondeá a 1 decimal. Respondé solo con el número en %.",
                "check": {"type": "numeric", "value": 77.2, "tolerance": 0.001, "unit": "%"},
                "answer": "77.2 % (el factor es 1.331² = 1.771561)",
            },
        ],
        "hints": [
            "Trabajá con factores, no con porcentajes: +33.1% es multiplicar por 1.331.",
            "El factor mensual `b` se aplica tres veces en un trimestre: `b³ = 1.331`.",
            "Seis meses son dos trimestres: los factores se multiplican, los porcentajes no se suman.",
        ],
        "solution": [
            "Factor trimestral: `1.331`. Si `b` es el factor mensual, en 3 meses se aplica tres veces: `b³ = 1.331`.",
            "`b = 1.331^(1/3) = 1.1`, porque `1.1³ = 1.331`. La tasa mensual es 10% (no `33.1% ÷ 3 ≈ 11.03%`: el aumento se compone).",
            "Modelo mensual: `C(t) = 400 000 · 1.1^t`, con `t` en meses.",
            "b) `C(2) = 400 000 · 1.1² = 400 000 · 1.21 = 484 000` pesos.",
            "c) En 6 meses hay 2 trimestres: el factor es `1.331² = 1.771561` (lo mismo que `1.1⁶`).",
            "Aumento acumulado: `1.771561 − 1 = 0.771561` → 77.2%. Error típico: sumar `33.1% + 33.1% = 66.2%`, que ignora que el segundo aumento se aplica sobre el precio ya aumentado.",
        ],
    },
    {
        "id": "a2-modelos-exponenciales-3",
        "node": "a2-modelos-exponenciales",
        "kind": "problem",
        "level": 3,
        "title": "Depreciación a partir de dos tasaciones",
        "statement": "Un taller metalúrgico de Rafaela compró un torno CNC cuyo valor de reventa cae un porcentaje fijo cada año, es decir, sigue un modelo exponencial `V(t) = V₀ · bᵗ` (`t` en años desde la compra). A los 2 años el torno se tasó en USD 32 000 y a los 5 años en USD 16 384.",
        "parts": [
            {
                "prompt": "a) ¿Qué porcentaje de su valor pierde el torno cada año? Respondé solo con el número en %.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "%"},
                "answer": "20 %",
            },
            {
                "prompt": "b) ¿Cuál fue el valor de compra `V₀`? Respondé solo con el número en USD.",
                "check": {"type": "numeric", "value": 50000, "tolerance": 0, "unit": "USD"},
                "answer": "50 000 USD",
            },
            {
                "prompt": "c) ¿A los cuántos años de la compra el torno vale USD 20 480? Respondé solo con el número en años.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "años"},
                "answer": "4 años",
            },
        ],
        "hints": [
            "Dividí las dos tasaciones: `V(5)/V(2)` elimina `V₀` y deja una potencia de `b`.",
            "Queda `b³ = 0.512`: buscá el número que elevado al cubo da 0.512.",
            "Con `b` conocido, despejá `V₀` de `V(2) = V₀ · b²`.",
        ],
        "solution": [
            "Datos: `V(2) = V₀ · b² = 32 000` y `V(5) = V₀ · b⁵ = 16 384`.",
            "Dividiendo miembro a miembro: `V(5)/V(2) = b³ = 16 384/32 000 = 0.512`.",
            "`b = 0.512^(1/3) = 0.8`, porque `0.8³ = 0.512`. El torno conserva el 80% de su valor cada año: pierde 20% anual.",
            "`V₀ = 32 000/b² = 32 000/0.64 = 50 000` USD.",
            "c) `50 000 · 0.8ᵗ = 20 480` → `0.8ᵗ = 0.4096`. Como `0.8² = 0.64` y `0.64² = 0.4096`, resulta `0.8⁴ = 0.4096` → `t = 4` años.",
            "Verificación: `50 000 · 0.8⁵ = 50 000 · 0.32768 = 16 384` ✓. Error típico: suponer una caída lineal (restar la misma cantidad de dólares por año), que no corresponde a un porcentaje fijo.",
        ],
    },
    # ==================== LOGARITMOS ====================
    {
        "id": "a2-logaritmos-1",
        "node": "a2-logaritmos",
        "kind": "problem",
        "level": 1,
        "title": "Evaluar con las propiedades de los logaritmos",
        "statement": "Calculá el valor exacto de cada expresión sin usar calculadora, aplicando las propiedades de los logaritmos.",
        "parts": [
            {
                "prompt": "a) `log₆(12) + log₆(18)`. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3",
            },
            {
                "prompt": "b) `2 · log₅(10) − log₅(4)`. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
            {
                "prompt": "c) `log₂(1/8) + ln(√e)`. Respondé solo con el número.",
                "check": {"type": "numeric", "value": -2.5, "tolerance": 0, "unit": ""},
                "answer": "−2.5 (es decir, −5/2)",
            },
        ],
        "hints": [
            "Suma de logaritmos de igual base → logaritmo del producto; resta → logaritmo del cociente.",
            "Un número que multiplica a un logaritmo sube como exponente del argumento: `2 · log₅(10) = log₅(10²)`.",
            "`1/8 = 2⁻³` y `√e = e^(1/2)`.",
        ],
        "solution": [
            "a) `log₆(12) + log₆(18) = log₆(12 · 18) = log₆(216)`. Como `6³ = 216`, vale 3.",
            "b) `2 · log₅(10) = log₅(10²) = log₅(100)`. Entonces `log₅(100) − log₅(4) = log₅(100/4) = log₅(25) = 2`.",
            "c) `log₂(1/8) = log₂(2⁻³) = −3`.",
            "`ln(√e) = ln(e^(1/2)) = 1/2`.",
            "`−3 + 1/2 = −5/2 = −2.5`. Error típico en a): sumar los argumentos (`log₆(30)`) en vez de multiplicarlos.",
        ],
    },
    {
        "id": "a2-logaritmos-2",
        "node": "a2-logaritmos",
        "kind": "problem",
        "level": 2,
        "title": "Expresar logaritmos en función de otros dos",
        "statement": "Sean `p = log 2` y `q = log 3` (logaritmos en base 10). Sin calculadora, escribí cada uno de los siguientes logaritmos en función de `p` y `q`.",
        "parts": [
            {
                "prompt": "a) `log 72`",
                "check": {
                    "type": "choice",
                    "options": ["2p + 3q", "6pq", "3p + 2q", "p³ + q²"],
                    "correct": 2,
                },
                "answer": "3p + 2q",
            },
            {
                "prompt": "b) `log 15`",
                "check": {
                    "type": "choice",
                    "options": ["q − p", "q − p + 1", "p + q + 1", "(q + 1)/p"],
                    "correct": 1,
                },
                "answer": "q − p + 1",
            },
            {
                "prompt": "c) `log₂ 3`",
                "check": {
                    "type": "choice",
                    "options": ["q/p", "q − p", "p/q", "p · q"],
                    "correct": 0,
                },
                "answer": "q/p",
            },
        ],
        "hints": [
            "Descomponé en factores primos: `72 = 2³ · 3²`.",
            "15 no tiene al 2 como factor, pero `15 = 30/2 = (3 · 10)/2`, y `log 10 = 1`.",
            "Para cambiar de base: `log_b(y) = log(y)/log(b)`.",
        ],
        "solution": [
            "a) `72 = 8 · 9 = 2³ · 3²`. Entonces `log 72 = log(2³) + log(3²) = 3 · log 2 + 2 · log 3 = 3p + 2q`.",
            "b) `15 = 3 · 5` y `5 = 10/2`, así que `log 5 = log 10 − log 2 = 1 − p`.",
            "`log 15 = log 3 + log 5 = q + (1 − p) = q − p + 1`.",
            "c) Cambio de base: `log₂ 3 = log 3 / log 2 = q/p`.",
            "Control numérico con `p ≈ 0.3010` y `q ≈ 0.4771`: `3p + 2q ≈ 1.8572 ≈ log 72` ✓; `q − p + 1 ≈ 1.1761 ≈ log 15` ✓; `q/p ≈ 1.585 ≈ log₂ 3` ✓. Error típico: confundir `log 3 / log 2` con `log(3/2) = q − p`.",
        ],
    },
    {
        "id": "a2-logaritmos-3",
        "node": "a2-logaritmos",
        "kind": "problem",
        "level": 3,
        "title": "Dominio y valor máximo de una función logarítmica",
        "statement": "Sea `f(x) = log₂(x + 3) + log₂(5 − x)`. Hallá su dominio y el mayor valor que toma.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el dominio de `f`?",
                "check": {
                    "type": "choice",
                    "options": ["[−3, 5]", "(−∞, −3) ∪ (5, +∞)", "(−3, +∞)", "(−3, 5)"],
                    "correct": 3,
                },
                "answer": "(−3, 5)",
            },
            {
                "prompt": "b) ¿En qué valor de `x` alcanza `f` su máximo? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1",
            },
            {
                "prompt": "c) ¿Cuánto vale ese máximo? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4",
            },
        ],
        "hints": [
            "Cada logaritmo necesita su argumento positivo: son dos condiciones que deben cumplirse a la vez.",
            "Dentro del dominio, juntá los dos logaritmos en uno solo con la propiedad del producto.",
            "`log₂` es creciente: `f` es máxima donde el argumento (una cuadrática) es máximo. Buscá su vértice.",
        ],
        "solution": [
            "Dominio: `x + 3 > 0` → `x > −3`, y `5 − x > 0` → `x < 5`. Las dos a la vez: `(−3, 5)`.",
            "En el dominio, `f(x) = log₂((x + 3)(5 − x)) = log₂(−x² + 2x + 15)`.",
            "Como `log₂` es creciente (su base es mayor que 1), `f` es máxima cuando `g(x) = −x² + 2x + 15` es máxima.",
            "`g` es una parábola hacia abajo con raíces `−3` y `5`; su vértice está en el punto medio, `x = (−3 + 5)/2 = 1` (o `x = −b/(2a) = −2/(−2) = 1`), que pertenece al dominio.",
            "`g(1) = (1 + 3)(5 − 1) = 16`, así que el máximo es `f(1) = log₂(16) = 4`.",
            "Verificación: `f(1) = log₂ 4 + log₂ 4 = 2 + 2 = 4` ✓, y por ejemplo `f(3) = log₂ 6 + log₂ 2 = log₂ 12 ≈ 3.58 < 4`. Error típico: incluir los extremos `−3` y `5` en el dominio; ahí un argumento vale 0 y el logaritmo no existe.",
        ],
    },
    # ==================== ECUACIONES EXPONENCIALES Y LOGARÍTMICAS ====================
    {
        "id": "a2-ecuaciones-exponenciales-logaritmicas-1",
        "node": "a2-ecuaciones-exponenciales-logaritmicas",
        "kind": "problem",
        "level": 1,
        "title": "Dos ecuaciones que se resuelven igualando bases",
        "statement": "Resolvé en ℝ las ecuaciones exponenciales `2^(x² − 3x) = 16` y `(1/9)^(x − 1) = 3 · 27^(x + 2)`.",
        "parts": [
            {
                "prompt": "a) En `2^(x² − 3x) = 16`, ¿cuál es la mayor de las soluciones? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4 (las soluciones son −1 y 4)",
            },
            {
                "prompt": "b) En `(1/9)^(x − 1) = 3 · 27^(x + 2)`, ¿cuánto vale `x`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -1, "tolerance": 0, "unit": ""},
                "answer": "−1",
            },
        ],
        "hints": [
            "Escribí los dos lados de cada ecuación como potencias de la misma base: 2 en la primera, 3 en la segunda.",
            "`1/9 = 3⁻²`, `27 = 3³` y el 3 suelto es `3¹`: al multiplicar potencias de igual base se suman los exponentes.",
        ],
        "solution": [
            "a) `16 = 2⁴`, así que `2^(x² − 3x) = 2⁴` → `x² − 3x = 4`.",
            "`x² − 3x − 4 = 0` → `(x − 4)(x + 1) = 0` → `x = 4` o `x = −1`. La mayor es `4`.",
            "Verificación: con `x = 4`, `2^(16 − 12) = 2⁴ = 16` ✓; con `x = −1`, `2^(1 + 3) = 16` ✓.",
            "b) Lado izquierdo: `(3⁻²)^(x − 1) = 3^(−2x + 2)`. Lado derecho: `3¹ · (3³)^(x + 2) = 3^(1 + 3x + 6) = 3^(3x + 7)`.",
            "Igualamos exponentes: `−2x + 2 = 3x + 7` → `−5x = 5` → `x = −1`.",
            "Verificación: `(1/9)^(−2) = 81` y `3 · 27¹ = 81` ✓. Error típico: olvidarse del `3¹` suelto y plantear `−2x + 2 = 3x + 6`.",
        ],
    },
    {
        "id": "a2-ecuaciones-exponenciales-logaritmicas-2",
        "node": "a2-ecuaciones-exponenciales-logaritmicas",
        "kind": "problem",
        "level": 2,
        "title": "Cambio de variable con exponentes opuestos y con base e",
        "statement": "Resolvé en ℝ las ecuaciones `3^(x + 1) + 3^(2 − x) = 28` y `e^(2x) − 5eˣ + 6 = 0`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el conjunto solución de `3^(x + 1) + 3^(2 − x) = 28`?",
                "check": {
                    "type": "choice",
                    "options": ["{2}", "{1/3, 9}", "{−1, 2}", "{−2, 1}"],
                    "correct": 2,
                },
                "answer": "{−1, 2}",
            },
            {
                "prompt": "b) ¿Cuánto vale la suma de las soluciones de `e^(2x) − 5eˣ + 6 = 0`?",
                "check": {
                    "type": "choice",
                    "options": ["ln 5", "ln 6", "5", "6"],
                    "correct": 1,
                },
                "answer": "ln 6 (las soluciones son ln 2 y ln 3)",
            },
        ],
        "hints": [
            "En la primera, `3^(x + 1) = 3 · 3ˣ` y `3^(2 − x) = 9/3ˣ`. Llamá `u = 3ˣ` y multiplicá toda la ecuación por `u`.",
            "En la segunda, `e^(2x) = (eˣ)²`.",
            "Después de hallar `u` falta volver a `x`; recordá que `ln a + ln b = ln(a · b)`.",
        ],
        "solution": [
            "Primera ecuación: con `u = 3ˣ > 0` queda `3u + 9/u = 28`. Multiplicamos por `u`: `3u² − 28u + 9 = 0`.",
            "Resolvente: `u = (28 ± √(784 − 108))/6 = (28 ± 26)/6` → `u = 9` o `u = 1/3`. Los dos son positivos, así que sirven.",
            "`3ˣ = 9` → `x = 2`; `3ˣ = 1/3` → `x = −1`. Conjunto solución: `{−1, 2}`.",
            "Verificación: con `x = 2`, `3³ + 3⁰ = 27 + 1 = 28` ✓; con `x = −1`, `3⁰ + 3³ = 1 + 27 = 28` ✓.",
            "Segunda ecuación: con `u = eˣ > 0` queda `u² − 5u + 6 = 0` → `(u − 2)(u − 3) = 0` → `u = 2` o `u = 3`.",
            "`eˣ = 2` → `x = ln 2`; `eˣ = 3` → `x = ln 3`.",
            "Suma: `ln 2 + ln 3 = ln(2 · 3) = ln 6 ≈ 1.79`. Error típico: responder con los valores de `u` (`{1/3, 9}`, o suma 5) sin volver a `x`, o escribir `ln 2 + ln 3 = ln 5`.",
        ],
    },
    {
        "id": "a2-ecuaciones-exponenciales-logaritmicas-3",
        "node": "a2-ecuaciones-exponenciales-logaritmicas",
        "kind": "problem",
        "level": 3,
        "title": "Solución extraña y ecuación cuadrática en log x",
        "statement": "Resolvé en ℝ las ecuaciones `2 · log₃(x − 1) − log₃(x + 5) = 1` y `(log x)² − log(x³) + 2 = 0` (en la segunda, `log` es el logaritmo en base 10).",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el conjunto solución de `2 · log₃(x − 1) − log₃(x + 5) = 1`?",
                "check": {
                    "type": "choice",
                    "options": ["{−2, 7}", "{−2}", "{7}", "No tiene solución"],
                    "correct": 2,
                },
                "answer": "{7}",
            },
            {
                "prompt": "b) ¿Cuánto vale la suma de las soluciones de `(log x)² − log(x³) + 2 = 0`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 110, "tolerance": 0, "unit": ""},
                "answer": "110 (las soluciones son 10 y 100)",
            },
        ],
        "hints": [
            "Antes de operar, anotá el dominio: en la primera hace falta `x − 1 > 0` y `x + 5 > 0`.",
            "`2 · log₃(x − 1) = log₃((x − 1)²)`; después, la resta de logaritmos es el logaritmo del cociente.",
            "En la segunda, `log(x³) = 3 · log x`: queda una cuadrática en `u = log x`.",
        ],
        "solution": [
            "Primera ecuación, dominio: `x − 1 > 0` y `x + 5 > 0` → `x > 1`.",
            "`log₃((x − 1)²) − log₃(x + 5) = 1` → `log₃((x − 1)²/(x + 5)) = 1` → `(x − 1)²/(x + 5) = 3¹ = 3`.",
            "`(x − 1)² = 3(x + 5)` → `x² − 2x + 1 = 3x + 15` → `x² − 5x − 14 = 0` → `(x − 7)(x + 2) = 0` → `x = 7` o `x = −2`.",
            "`x = −2` no cumple `x > 1`: dejaría `log₃(−3)`, que no existe. Es una solución extraña (aparece porque `(x − 1)²` es positivo aunque `x − 1` sea negativo). Queda `{7}`.",
            "Verificación con `x = 7`: `2 · log₃ 6 − log₃ 12 = log₃(36/12) = log₃ 3 = 1` ✓.",
            "Segunda ecuación (dominio `x > 0`): con `u = log x`, `u² − 3u + 2 = 0` → `(u − 1)(u − 2) = 0` → `u = 1` o `u = 2`.",
            "`log x = 1` → `x = 10`; `log x = 2` → `x = 100`. Ambas son positivas. Verificación con `x = 100`: `2² − 6 + 2 = 0` ✓. La suma es `10 + 100 = 110` (no `1 + 2 = 3`, que son los valores de `u`).",
        ],
    },
    # ==================== INECUACIONES AVANZADAS ====================
    {
        "id": "a2-inecuaciones-avanzadas-1",
        "node": "a2-inecuaciones-avanzadas",
        "kind": "problem",
        "level": 1,
        "title": "Inecuación cuadrática con coeficiente principal 2",
        "statement": "Resolvé la inecuación `2x² + 5x ≤ 3`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el conjunto solución?",
                "check": {
                    "type": "choice",
                    "options": ["(−3, 1/2)", "(−∞, −3] ∪ [1/2, +∞)", "[−1/2, 3]", "[−3, 1/2]"],
                    "correct": 3,
                },
                "answer": "[−3, 1/2]",
            },
            {
                "prompt": "b) ¿Cuántos números enteros cumplen la inecuación? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4 (son −3, −2, −1 y 0)",
            },
        ],
        "hints": [
            "Primero dejá 0 de un lado: pasá el 3 restando.",
            "Hallá las raíces con la resolvente y pensá hacia dónde abre la parábola.",
        ],
        "solution": [
            "Todo de un lado: `2x² + 5x − 3 ≤ 0`.",
            "Raíces: `x = (−5 ± √(25 + 24))/4 = (−5 ± 7)/4` → `x = 1/2` o `x = −3`. Factorizado: `2(x − 1/2)(x + 3) = (2x − 1)(x + 3)`.",
            "La parábola abre hacia arriba (`a = 2 > 0`): es negativa entre las raíces y positiva afuera. Control con `x = 0`: `−3 ≤ 0` ✓.",
            "Como la desigualdad es `≤`, las raíces entran: la solución es `[−3, 1/2]`.",
            "Enteros en `[−3, 1/2]`: `−3, −2, −1, 0` → son 4. Error típico: tratar `x(2x + 5) ≤ 3` como si fuera un producto igualado a cero y separar `x ≤ 3` y `2x + 5 ≤ 3`.",
        ],
    },
    {
        "id": "a2-inecuaciones-avanzadas-2",
        "node": "a2-inecuaciones-avanzadas",
        "kind": "problem",
        "level": 2,
        "title": "Valor absoluto e inecuación racional a la vez",
        "statement": "Se buscan los números reales `x` que cumplen a la vez las dos condiciones `|2x − 1| ≥ 3` y `x/(x − 3) ≤ 2/(x + 1)`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el conjunto solución de `|2x − 1| ≥ 3`?",
                "check": {
                    "type": "choice",
                    "options": ["[−1, 2]", "(−∞, −1] ∪ [2, +∞)", "(−∞, −2] ∪ [1, +∞)", "[2, +∞)"],
                    "correct": 1,
                },
                "answer": "(−∞, −1] ∪ [2, +∞)",
            },
            {
                "prompt": "b) ¿Cuál es el conjunto solución de `x/(x − 3) ≤ 2/(x + 1)`?",
                "check": {
                    "type": "choice",
                    "options": ["(−1, 3)", "[−1, 3]", "(−∞, −1) ∪ (3, +∞)", "∅ (no tiene solución)"],
                    "correct": 0,
                },
                "answer": "(−1, 3)",
            },
            {
                "prompt": "c) ¿Cuál es el conjunto de los `x` que cumplen las dos condiciones a la vez?",
                "check": {
                    "type": "choice",
                    "options": ["[2, 3]", "(−1, 2]", "[2, 3)", "(−∞, −1] ∪ [2, 3)"],
                    "correct": 2,
                },
                "answer": "[2, 3)",
            },
        ],
        "hints": [
            "`|A| ≥ r` (con `r > 0`) se separa en `A ≥ r` o `A ≤ −r`.",
            "En la racional no multipliques en cruz: pasá todo a un lado y restá con denominador común.",
            "Si el numerador que queda no tiene raíces reales, su signo es siempre el mismo y manda el denominador. Al final, intersecá las dos soluciones.",
        ],
        "solution": [
            "Valor absoluto: `|2x − 1| ≥ 3` ⇔ `2x − 1 ≥ 3` o `2x − 1 ≤ −3` ⇔ `x ≥ 2` o `x ≤ −1`. Solución: `(−∞, −1] ∪ [2, +∞)`.",
            "Racional: pasamos todo a un lado, `x/(x − 3) − 2/(x + 1) ≤ 0`, con `x ≠ 3` y `x ≠ −1`.",
            "Denominador común: `[x(x + 1) − 2(x − 3)]/((x − 3)(x + 1)) = (x² − x + 6)/((x − 3)(x + 1)) ≤ 0`.",
            "El numerador `x² − x + 6` tiene `Δ = 1 − 24 = −23 < 0` y `a > 0`: es positivo para todo `x`. El signo del cociente es entonces el del denominador, y nunca vale 0.",
            "`(x − 3)(x + 1) < 0` entre sus raíces: `−1 < x < 3`. Los extremos anulan el denominador, así que no entran: `(−1, 3)`.",
            "Intersección: `(−∞, −1] ∩ (−1, 3) = ∅` y `[2, +∞) ∩ (−1, 3) = [2, 3)`.",
            "Solución del sistema: `[2, 3)`. Control con `x = 2`: `|3| ≥ 3` ✓ y `2/(−1) = −2 ≤ 2/3` ✓; `x = 3` no está en el dominio. Error típico: multiplicar en cruz (`x(x + 1) ≤ 2(x − 3)`), que ignora el signo de los denominadores y lleva a decir que no hay solución.",
        ],
    },
    {
        "id": "a2-inecuaciones-avanzadas-3",
        "node": "a2-inecuaciones-avanzadas",
        "kind": "problem",
        "level": 3,
        "title": "Polinomio de grado 4: factorizar y estudiar el signo",
        "statement": "Sea `P(x) = x⁴ − 3x³ − 3x² + 11x − 6`. Factorizalo por completo y resolvé la inecuación `P(x) < 0`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la factorización completa de `P`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "(x + 1)²(x − 2)(x + 3)",
                        "(x − 1)(x + 1)(x + 2)(x − 3)",
                        "(x − 1)²(x + 2)(x − 3)",
                        "(x − 1)²(x − 2)(x + 3)",
                    ],
                    "correct": 2,
                },
                "answer": "(x − 1)²(x + 2)(x − 3)",
            },
            {
                "prompt": "b) ¿Cuál es el conjunto solución de `P(x) < 0`?",
                "check": {
                    "type": "choice",
                    "options": ["(−2, 3)", "(−2, 1) ∪ (1, 3)", "[−2, 3]", "(−∞, −2) ∪ (3, +∞)"],
                    "correct": 1,
                },
                "answer": "(−2, 1) ∪ (1, 3)",
            },
            {
                "prompt": "c) ¿Cuántos números enteros cumplen `P(x) < 0`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3 (son −1, 0 y 2)",
            },
        ],
        "hints": [
            "Buscá raíces enteras entre los divisores de −6 y bajá el grado con Ruffini.",
            "Probá si la raíz que encontraste también anula al cociente: puede ser doble.",
            "Un factor elevado al cuadrado no cambia el signo del producto, pero donde se anula el polinomio vale 0, y 0 no es menor que 0.",
        ],
        "solution": [
            "Candidatos: divisores de −6 → `±1, ±2, ±3, ±6`. `P(1) = 1 − 3 − 3 + 11 − 6 = 0` ✓.",
            "Ruffini con 1 sobre `1, −3, −3, 11, −6` da `1, −2, −5, 6 | 0`. El cociente es `x³ − 2x² − 5x + 6`.",
            "El cociente también se anula en 1 (`1 − 2 − 5 + 6 = 0`). Ruffini con 1 sobre `1, −2, −5, 6` da `1, −1, −6 | 0`: queda `x² − x − 6 = (x − 3)(x + 2)`.",
            "`P(x) = (x − 1)²(x + 2)(x − 3)`, con raíz doble en `x = 1`.",
            "Signo: `(x − 1)² ≥ 0` siempre, y vale 0 solo en `x = 1`. Para `x ≠ 1`, el signo de `P` es el de `(x + 2)(x − 3)`, que es negativo entre `−2` y `3`.",
            "En `x = 1`, `P(1) = 0`, que no es menor que 0: hay que quitarlo. Solución: `(−2, 1) ∪ (1, 3)`.",
            "Enteros que cumplen: `−1, 0, 2` → son 3. Control: `P(0) = −6 < 0` ✓, `P(2) = 16 − 24 − 12 + 22 − 6 = −4 < 0` ✓ y `P(4) = 256 − 192 − 48 + 44 − 6 = 54 > 0` ✓. Error típico: responder `(−2, 3)` sin excluir la raíz doble.",
        ],
    },
]
