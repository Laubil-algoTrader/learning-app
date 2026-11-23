"""Algebra 2 curriculum (11 units, #52-#62) adapted from Khan Academy Algebra 2.

Covers all Algebra 2 units building on Aritmética (#1-#17), Preálgebra (#18-#29),
Álgebra 1 (#30-#41) and Geometría (#42-#51):
  - Complex numbers (i, powers of i, operations, conjugates, complex quadratic roots)
  - Higher-degree polynomial arithmetic, factoring by grouping, quadratic form & cubes
  - Polynomial division, Remainder Theorem & Factor Theorem
  - Polynomial graphs: zeros, multiplicity & end behavior
  - Advanced exponential models: period conversion, half-life & Euler's number e
  - Logarithms (log, ln), properties, change of base & solving exponential equations
  - Function transformations, even/odd symmetry & inverse functions
  - Rational functions: domain restrictions, holes vs. vertical & horizontal asymptotes
  - Radical & rational equations, extraneous solutions & nonlinear systems
  - Unit circle, Pythagorean identity & sinusoidal waves (amplitude, midline, period)
  - Function composition (f o g), combinations & real-world model selection
"""

from __future__ import annotations

ALGEBRA2_NODES: list[dict] = [
    # ==================== NIVEL 19: NÚMEROS COMPLEJOS Y POLINOMIOS ====================
    {
        "slug": "a2-numeros-complejos",
        "title": "52. Números complejos (unidad imaginaria i y operaciones)",
        "level": 19,
        "order_index": 52,
        "summary": "La unidad imaginaria i = √(−1), ciclo de potencias iⁿ, suma/producto/conjugado de complejos y raíces cuando Δ < 0.",
        "prerequisites": ["al-parabolas-formula", "al-irracionales"],
        "metadata": {"section": "Álgebra 2", "lab_tab": "complex_nums", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Evaluar una potencia alta de i (ciclo de 4)",
                "prompt": "Como i¹ = i, i² = −1, i³ = −i e i⁴ = 1, las potencias de i se repiten cada 4. ¿Cuánto vale i¹⁴? Respondé solo con el número.",
                "answer": "−1: como 14 = 4 × 3 + 2, i¹⁴ equivale exactamente a i² = −1.",
                "hints": ["Buscá el resto de dividir 14 por 4.", "El resto es 2, así que i¹⁴ vale lo mismo que i²."],
                "payload": {
                    "lab_link": "math:complex_nums",
                    "check": {"type": "numeric", "value": -1, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Sumar y restar números complejos por componentes",
                "prompt": "Calculá (3 + 4i) + (2 − 7i). ¿Cuál es el coeficiente de la parte imaginaria (el número que acompaña a i)? Respondé solo con el número.",
                "answer": "−3: se suman reales con reales (3 + 2 = 5) e imaginarios con imaginarios (4i − 7i = −3i) → 5 − 3i.",
                "hints": ["Sumá solo los coeficientes de i: 4 + (−7)."],
                "payload": {
                    "lab_link": "math:complex_nums",
                    "check": {"type": "numeric", "value": -3, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Multiplicar dos complejos recordando i² = −1",
                "prompt": "Expandí (2 + 3i)(4 − i) reemplazando i² por −1. ¿Cuál es la parte REAL del resultado? Respondé solo con el número.",
                "answer": "11: 8 − 2i + 12i − 3i² = 8 + 10i − 3(−1) = 11 + 10i.",
                "hints": ["El producto −3i² se convierte en +3 y se suma con 2 × 4 = 8."],
                "payload": {
                    "lab_link": "math:complex_nums",
                    "check": {"type": "numeric", "value": 11, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Multiplicar un complejo por su conjugado",
                "prompt": "El conjugado de 3 + 4i es 3 − 4i. ¿Cuánto da el producto (3 + 4i)(3 − 4i)? Respondé solo con el número.",
                "answer": "25: por diferencia de cuadrados da 3² − (4i)² = 9 − 16(−1) = 9 + 16 = 25 (la parte imaginaria se cancela siempre).",
                "hints": ["Al multiplicar (a + bi)(a − bi) siempre queda a² + b²."],
                "payload": {
                    "lab_link": "math:complex_nums",
                    "check": {"type": "numeric", "value": 25, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Módulo (magnitud) de un complejo en electricidad AC",
                "prompt": "En circuitos de corriente alterna, una impedancia se escribe Z = 3 + 4i Ω. Su magnitud total es |Z| = √(3² + 4²). ¿Cuántos Ω mide |Z|? Respondé solo con el número.",
                "answer": "5 Ω: el módulo en el plano complejo es simplemente Pitágoras sobre parte real (3) e imaginaria (4) → √(9 + 16) = 5.",
                "hints": ["Calculá √(3² + 4²)."],
                "payload": {
                    "lab_link": "math:complex_nums",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "Ω"},
                },
            },
            {
                "item_type": "recall",
                "title": "Soluciones complejas de una cuadrática con Δ < 0",
                "prompt": "La ecuación x² − 2x + 5 = 0 tiene discriminante Δ = (−2)² − 4(1)(5) = −16. ¿Cuáles son sus dos soluciones complejas?",
                "answer": "1 + 2i y 1 − 2i: x = (2 ± √(−16)) / 2 = (2 ± 4i) / 2 = 1 ± 2i (siempre vienen en pares conjugados).",
                "hints": ["Reemplazá √(−16) por 4i y dividí todo por 2."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["1 ± 2i", "1 ± 4i", "2 ± 4i"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "a2-polinomios-factorizacion",
        "title": "53. Polinomios avanzados: aritmética y factorización",
        "level": 19,
        "order_index": 53,
        "summary": "Grado de polinomios, factorización por agrupación, formas cuadráticas (x⁴ + bx² + c), cubos y expansión binomial.",
        "prerequisites": ["al-factorizar-cuadraticas"],
        "metadata": {"section": "Álgebra 2", "lab_tab": "factoring", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Identificar el grado de un polinomio desordenado",
                "prompt": "¿Cuál es el grado del polinomio P(x) = 4x³ − 7x⁵ + 2x − 1? Respondé solo con el número.",
                "answer": "5: el grado es el MAYOR exponente que aparece en el polinomio (el término líder es −7x⁵, aunque no esté escrito primero).",
                "hints": ["Buscá el exponente más grande, no el primero que aparece a la izquierda."],
                "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Resolver una bicuadrática (forma cuadrática)",
                "prompt": "Factorizá x⁴ − 5x² + 4 = 0 pensando u = x² → (x² − 4)(x² − 1) = 0. ¿Cuál es la MAYOR solución real x? Respondé solo con el número.",
                "answer": "2: las cuatro soluciones reales son x = −2, −1, 1 y 2; la mayor es 2.",
                "hints": ["De x² − 4 = 0 sale x = ±2, y de x² − 1 = 0 sale x = ±1."],
                "payload": {
                    "lab_link": "math:factoring",
                    "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Factorizar por agrupación en 4 términos",
                "prompt": "Al agrupar de a pares en x³ + 2x² + 3x + 6 queda x²(x + 2) + 3(x + 2). ¿Cómo queda completamente factorizado?",
                "answer": "(x² + 3)(x + 2): sacamos el paréntesis repetido (x + 2) como factor común.",
                "hints": ["Juntá lo que multiplica al paréntesis repetido (x + 2)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(x² + 3)(x + 2)", "(x² + 2)(x + 3)", "x²(x + 5) + 6"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Factor común + diferencia de cuadrados en grado 3",
                "prompt": "¿Cuál es la factorización completa de 2x³ − 18x?",
                "answer": "2x(x − 3)(x + 3): primero sacamos factor común 2x → 2x(x² − 9), y luego factorizamos la diferencia de cuadrados.",
                "hints": ["Sacá 2x primero; te va a quedar (x² − 9) adentro."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "2x(x − 3)(x + 3)",
                            "2x(x − 9)",
                            "2(x − 3)³",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Diferencia de cubos: a³ − b³",
                "prompt": "Usando a³ − b³ = (a − b)(a² + ab + b²), ¿cómo se factoriza x³ − 8 (donde 8 = 2³)?",
                "answer": "(x − 2)(x² + 2x + 4): el primer signo coincide (−), el del medio se invierte (+) y el último siempre es positivo (+).",
                "hints": ["Reemplazá a = x y b = 2 en (a − b)(a² + ab + b²)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "(x − 2)(x² + 2x + 4)",
                            "(x − 2)(x² − 2x + 4)",
                            "(x − 2)³",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Coeficiente de un binomio al cubo (Triángulo de Pascal)",
                "prompt": "Al expandir (x + 1)³ = x³ + ax² + bx + 1 con el Triángulo de Pascal, ¿cuánto vale el coeficiente a que acompaña a x²? Respondé solo con el número.",
                "answer": "3: la fila 3 del Triángulo de Pascal es 1, 3, 3, 1, así que (x + 1)³ = x³ + 3x² + 3x + 1 (nunca es simplemente x³ + 1).",
                "hints": ["Armá las filas de Pascal sumando de a dos vecinos: 1 · 1 1 · 1 2 1 · …", "La fila 3 es 1, 3, 3, 1."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    {
        "slug": "a2-division-polinomios",
        "title": "54. División de polinomios y Teorema del Resto",
        "level": 19,
        "order_index": 54,
        "summary": "División larga y sintética (Ruffini), atajo del Teorema del Resto P(c) y Teorema del Factor para encontrar raíces.",
        "prerequisites": ["a2-polinomios-factorizacion"],
        "metadata": {"section": "Álgebra 2", "lab_tab": "polynomials", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Teorema del Resto con (x − 2)",
                "prompt": "Sin hacer toda la división larga, usá el Teorema del Resto para hallar el resto de dividir P(x) = x³ − 2x + 5 por (x − 2). Respondé solo con el número.",
                "answer": "9: el resto al dividir por (x − c) es exactamente P(c) → P(2) = 2³ − 2(2) + 5 = 8 − 4 + 5 = 9.",
                "hints": ["Evaluá P(2) sustituyendo x = 2."],
                "payload": {
                    "lab_link": "math:polynomials",
                    "check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Teorema del Resto con signo positivo (x + 3)",
                "prompt": "¿Cuál es el resto de dividir P(x) = x² + 5x + 10 por (x + 3)? (Ojo: x + 3 = x − (−3)). Respondé solo con el número.",
                "answer": "4: evaluamos en c = −3 → P(−3) = (−3)² + 5(−3) + 10 = 9 − 15 + 10 = 4.",
                "hints": ["El valor que anula (x + 3) es x = −3; evaluá P(−3)."],
                "payload": {
                    "lab_link": "math:polynomials",
                    "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Teorema del Factor: detectar división exacta",
                "prompt": "Probás x = 2 en P(x) = x³ − 4x² + x + 6 y obtenés P(2) = 8 − 16 + 2 + 6 = 0. ¿Qué garantiza eso?",
                "answer": "Que (x − 2) es un factor exacto de P(x) (al dividirlo da resto 0).",
                "hints": ["Resto igual a 0 significa división exacta."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "(x − 2) es un factor exacto de P(x)",
                            "(x + 2) es un factor exacto de P(x)",
                            "El grado de P(x) es 2",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ajustar un coeficiente k para que divida exacto",
                "prompt": "¿Cuánto debe valer k para que (x − 1) sea factor exacto de P(x) = x³ + kx − 5 (es decir, P(1) = 0)? Respondé solo con el número.",
                "answer": "4: P(1) = 1³ + k(1) − 5 = 0 → k − 4 = 0 → k = 4.",
                "hints": ["Planteá 1 + k − 5 = 0."],
                "payload": {
                    "lab_link": "math:polynomials",
                    "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Simplificar un cociente exacto de polinomios",
                "prompt": "Al dividir (x³ − 1) por (x − 1) (para x ≠ 1), ¿qué polinomio cociente se obtiene?",
                "answer": "x² + x + 1: podés comprobarlo multiplicando (x − 1)(x² + x + 1) = x³ − 1.",
                "hints": ["Usá diferencia de cubos o comprobá multiplicando por (x − 1)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["x² + x + 1", "x² − 1", "x² − x + 1"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Cero fantasma en división sintética (Ruffini)",
                "prompt": "Vas a dividir P(x) = x³ − 5x + 2 por (x − 2) usando regla de Ruffini. ¿Qué fila de coeficientes tenés que escribir arriba?",
                "answer": "1, 0, −5, 2: como falta el término x², hay que colocar obligatoriamente un 0 para guardar su columna.",
                "hints": ["Mirá si falta alguna potencia entre x³ y x¹."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["1, 0, −5, 2", "1, −5, 2", "1, 1, −5, 2"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "a2-graficas-polinomios",
        "title": "55. Gráficas de polinomios: ceros, multiplicidad y extremos",
        "level": 19,
        "order_index": 55,
        "summary": "Cómo leer y bosquejar cualquier polinomio factorizado: cruces vs. rebotes (multiplicidad) y comportamiento hacia ±∞.",
        "prerequisites": ["a2-division-polinomios"],
        "metadata": {"section": "Álgebra 2", "lab_tab": "polynomials", "est_minutes": 18},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Calcular el grado total de un polinomio factorizado",
                "prompt": "¿Cuál es el grado total del polinomio P(x) = −2(x − 1)²(x + 3)³? Respondé solo con el número.",
                "answer": "5: sumamos las multiplicidades (exponentes) de los factores con x → 2 + 3 = 5.",
                "hints": ["Al expandir, la potencia más alta viene de x² · x³."],
                "payload": {
                    "lab_link": "math:polynomials",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Multiplicidad par (rebote) vs. impar (cruce)",
                "prompt": "En P(x) = (x − 4)(x + 1)², ¿qué hace la gráfica cuando toca el eje X en la raíz x = −1?",
                "answer": "Rebota (toca el eje X y vuelve del mismo lado sin cruzar), porque el factor (x + 1) tiene exponente PAR (2).",
                "hints": ["El signo de (x + 1)² nunca cambia al pasar por −1: siempre es positivo."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Rebota sin cruzar el eje X (multiplicidad par)",
                            "Cruza el eje X de abajo hacia arriba",
                            "Tiene una asíntota vertical en x = −1",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Comportamiento en los extremos (end behavior)",
                "prompt": "Un polinomio tiene término líder −3x⁴ (grado PAR y coeficiente principal NEGATIVO). ¿Hacia dónde apuntan sus dos extremos cuando x → −∞ y x → +∞?",
                "answer": "Ambos extremos apuntan hacia abajo (−∞): grado par hace que ambos lados vayan igual, y el signo negativo los manda hacia abajo.",
                "hints": ["Evaluá mentalmente −3(100)⁴ y −3(−100)⁴: ambos son números negativos gigantes."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Ambos hacia abajo (−∞)",
                            "Ambos hacia arriba (+∞)",
                            "Izquierda hacia abajo, derecha hacia arriba",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ordenada al origen desde forma factorizada",
                "prompt": "¿En qué valor de y corta al eje vertical la gráfica de P(x) = (x − 2)²(x + 3)? (Evaluá P(0)). Respondé solo con el número.",
                "answer": "12: P(0) = (0 − 2)² · (0 + 3) = 4 × 3 = 12.",
                "hints": ["Reemplazá x = 0 en ambos paréntesis y multiplicá."],
                "payload": {"check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Cantidad máxima de giros (picos/valles)",
                "prompt": "Un polinomio de grado n puede tener como máximo (n − 1) giros o cambios de dirección. ¿Cuántos giros como máximo puede tener un polinomio de grado 4?",
                "answer": "3 giros (como una letra 'W' o 'M').",
                "hints": ["Restá 1 al grado 4."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Identificar un polinomio cúbico desde sus raíces",
                "prompt": "Una gráfica polinómica de grado 3 cruza el eje X exactamente en x = −2, x = 0 y x = 5. ¿Qué expresión puede corresponderle?",
                "answer": "x(x + 2)(x − 5): cada raíz r aporta un factor (x − r) con signo invertido.",
                "hints": ["Buscá la expresión que se haga 0 al probar x = −2, 0 y 5."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "x(x + 2)(x − 5)",
                            "x(x − 2)(x + 5)",
                            "(x + 2)(x − 5)",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 20: MODELOS EXPONENCIALES Y LOGARITMOS ====================
    {
        "slug": "a2-modelos-exponenciales",
        "title": "56. Modelos exponenciales avanzados y número e",
        "level": 20,
        "order_index": 56,
        "summary": "Ajustar períodos con exponentes fraccionarios (t/T), convertir tasas compuestas, vida media y crecimiento continuo con e.",
        "prerequisites": ["al-exponenciales", "al-exponentes-radicales"],
        "metadata": {"section": "Álgebra 2", "lab_tab": "exponentials", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Población que se duplica cada 4 años",
                "prompt": "Un modelo sigue P(t) = 100 · 2^(t/4), donde t está en años. ¿Cuánto vale P(12) al cabo de 12 años? Respondé solo con el número.",
                "answer": "800: en 12 años pasan 12 / 4 = 3 duplicaciones → 100 × 2³ = 100 × 8 = 800.",
                "hints": ["Primero calculá el exponente 12 ÷ 4 = 3, luego 100 × 2³."],
                "payload": {
                    "lab_link": "math:exponentials",
                    "check": {"type": "numeric", "value": 800, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Convertir una tasa bienal (+21% cada 2 años) a tasa anual",
                "prompt": "Un fondo crece +21% cada 2 años (factor ×1.21 cada 2 años). ¿Qué tasa anual compuesta equivale exactamente a eso? Respondé solo con el número del porcentaje.",
                "answer": "10%: el factor anual es (1.21)^(1/2) = √1.21 = 1.10, porque 1.10 × 1.10 = 1.21 (no se divide 21% por 2, porque el interés se compone sobre sí mismo).",
                "hints": ["Buscá el factor anual b tal que b × b = 1.21 (o sea √1.21).", "Si el factor anual es 1.10, restá 1 y pasá a porcentaje."],
                "payload": {
                    "lab_link": "math:exponentials",
                    "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "%"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Decaimiento de un medicamento con vida media de 6 horas",
                "prompt": "Una dosis de 200 mg sigue C(t) = 200 · (0.5)^(t/6) (baja a la mitad cada 6 h). ¿Cuántos mg quedan después de 18 horas? Respondé solo con el número.",
                "answer": "25 mg: en 18 h pasan 18 / 6 = 3 vidas medias → 200 ÷ 2³ = 200 ÷ 8 = 25 mg.",
                "hints": ["Dividí 200 por 2 tres veces seguidas (18 ÷ 6 = 3)."],
                "payload": {
                    "lab_link": "math:exponentials",
                    "check": {"type": "numeric", "value": 25, "tolerance": 0, "unit": "mg"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Leer la tasa porcentual de depreciación de un auto",
                "prompt": "El valor de un auto se modela con V(t) = 18 000 · (0.85)^t (t en años). ¿Qué porcentaje de su valor pierde cada año? Respondé solo con el número.",
                "answer": "15%: retiene el 85% cada año, así que pierde 100% − 85% = 15% anual.",
                "hints": ["Restá 0.85 a 1.00 y pasalo a porcentaje."],
                "payload": {"check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": "%"}},
            },
            {
                "item_type": "recall",
                "title": "De dónde sale el número e ≈ 2.718",
                "prompt": "Si invertís $1 al 100% anual pero capitalizando intereses cada vez más seguido (mensual, diario, por segundo, de forma continua), ¿a qué valor se acerca tu capital al final del año?",
                "answer": "Al número de Euler e ≈ 2.71828: es el límite natural del crecimiento compuesto continuo P = P₀ · e^(rt).",
                "hints": ["(1 + 1/n)^n no crece al infinito: se frena en una constante famosa entre 2 y 3."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "e ≈ 2.718 (constante del crecimiento continuo)",
                            "Infinito (crece sin límite)",
                            "Exactamente $2.00",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Equivalencia algebraica al reescribir exponentes",
                "prompt": "Un cultivo crece según N(t) = 50 · (1.05)^(12t), donde t está en años. ¿Cómo se ve su factor de crecimiento ANUAL aproximado?",
                "answer": "(1.05¹²)^t ≈ (1.796)^t: un +5% mensual compuesto equivale casi a +80% por año (mucho más que 12 × 5% = 60%).",
                "hints": ["Usá la ley de potencias a^(12t) = (a¹²)^t."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "50 · (1.05¹²)^t ≈ 50 · (1.796)^t (+79.6% anual)",
                            "50 · (1.60)^t (+60% anual)",
                            "50 · (12.05)^t",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "a2-logaritmos",
        "title": "57. Logaritmos (log, ln), propiedades y despeje de exponentes",
        "level": 20,
        "order_index": 57,
        "summary": "El logaritmo como inverso de la exponencial (log_b y = x ⇔ bˣ = y), reglas de producto/cociente/potencia, escalas reales y despeje.",
        "prerequisites": ["a2-modelos-exponenciales"],
        "metadata": {"section": "Álgebra 2", "lab_tab": "logarithms", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Evaluar un logaritmo como pregunta de exponente",
                "prompt": "log₂(32) pregunta '¿a qué potencia hay que elevar 2 para obtener 32?'. ¿Cuánto vale log₂(32)? Respondé solo con el número.",
                "answer": "5: porque 2⁵ = 32.",
                "hints": ["Multiplicá 2 por sí mismo hasta llegar a 32: 2, 4, 8, 16, 32."],
                "payload": {
                    "lab_link": "math:logarithms",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Logaritmo base 10 de un número decimal chico",
                "prompt": "¿Cuánto vale log₁₀(0.01)? (Pensá: 0.01 = 1/100 = 10^(?)). Respondé solo con el número.",
                "answer": "−2: porque 10⁻² = 1 / 100 = 0.01 (con base mayor que 1, como la base 10, el logaritmo de un número entre 0 y 1 es negativo).",
                "hints": ["10⁻² = 0.01."],
                "payload": {
                    "lab_link": "math:logarithms",
                    "check": {"type": "numeric", "value": -2, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Regla del producto: suma de logaritmos",
                "prompt": "Usando log_b(A) + log_b(B) = log_b(A · B), ¿cuánto vale log₂(4) + log₂(8)? Respondé solo con el número.",
                "answer": "5: equivale a log₂(4 × 8) = log₂(32) = 5 (y también 2 + 3 = 5).",
                "hints": ["Sumar logaritmos de igual base multiplica sus argumentos: 4 × 8 = 32."],
                "payload": {
                    "lab_link": "math:logarithms",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Logaritmo natural ln y el número e",
                "prompt": "Como ln(x) es el logaritmo en base e, se cancelan mutuamente: ln(eˣ) = x. ¿Cuánto vale ln(e⁴)? Respondé solo con el número.",
                "answer": "4: pregunta a qué potencia elevar e para obtener e⁴, que es directamente 4.",
                "hints": ["ln y e^(...) son funciones inversas exactas."],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Escala logarítmica en la vida real (terremotos Richter)",
                "prompt": "La escala de Richter es base 10: cada +1 punto multiplica por 10 la amplitud sísmica. ¿Cuántas veces mayor amplitud tiene un sismo de magnitud 7 respecto a uno de magnitud 5? Respondé solo con el número.",
                "answer": "100 veces mayor: la diferencia es 7 − 5 = 2 puntos → 10² = 100 veces.",
                "hints": ["Restá las magnitudes (7 − 5 = 2) y calculá 10²."],
                "payload": {"check": {"type": "numeric", "value": 100, "tolerance": 0, "unit": "×"}},
            },
            {
                "item_type": "recall",
                "title": "Bajar el exponente para despejar el tiempo t",
                "prompt": "Querés saber en cuántos años t se duplica un capital al 10% anual: 1.10^t = 2. ¿Cómo despejás t usando logaritmos?",
                "answer": "t = log(2) / log(1.10) (≈ 7.27 años): aplicamos log a ambos lados → t · log(1.10) = log(2) y dividimos.",
                "hints": ["Usá la regla log(a^t) = t · log(a) y luego despejá t."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "t = log(2) / log(1.10)",
                            "t = 2 / 1.10",
                            "t = log(2 − 1.10)",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 21: TRANSFORMACIONES, RACIONALES Y ECUACIONES ====================
    {
        "slug": "a2-transformaciones-funciones",
        "title": "58. Transformaciones de funciones, simetría e inversas",
        "level": 21,
        "order_index": 58,
        "summary": "Desplazar, estirar y reflejar cualquier gráfica f(x), distinguir funciones pares/impares y hallar inversas f⁻¹(x).",
        "prerequisites": ["al-dominio-rango", "al-valor-absoluto-partes", "g-transformaciones"],
        "metadata": {"section": "Álgebra 2", "lab_tab": "quadratics", "est_minutes": 18},
        "items": [
            {
                "item_type": "recall",
                "title": "Desplazamiento horizontal y vertical en g(x) = f(x − 3) + 5",
                "prompt": "Partiendo de la gráfica de f(x), ¿cómo se mueve la gráfica de g(x) = f(x − 3) + 5?",
                "answer": "3 unidades hacia la DERECHA y 5 hacia ARRIBA: lo que pasa dentro del paréntesis afecta horizontalmente con signo invertido.",
                "hints": ["Adentro del paréntesis va al revés (x − 3 corre a la derecha); afuera va directo (+5 sube)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "3 a la derecha y 5 hacia arriba",
                            "3 a la izquierda y 5 hacia arriba",
                            "5 a la derecha y 3 hacia arriba",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Diferencia entre −f(x) y f(−x)",
                "prompt": "Si la gráfica de y = √x se transforma en y = −√x (el menos está AFUERA), ¿qué le pasa visualmente?",
                "answer": "Se refleja verticalmente (espejo sobre el eje X): todas las salidas positivas pasan a ser negativas.",
                "hints": ["Cambiar el signo del resultado y voltea la curva de arriba hacia abajo."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Se refleja verticalmente (sobre el eje X)",
                            "Se refleja horizontalmente (sobre el eje Y)",
                            "Baja 1 unidad",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Reconocer función par vs. impar",
                "prompt": "Una función cumple f(−x) = f(x) para todo x (por ejemplo f(x) = x² + 3 o f(x) = |x|). ¿Qué tipo de función es y qué simetría tiene?",
                "answer": "Es una función PAR y su gráfica es perfectamente simétrica respecto del eje vertical Y.",
                "hints": ["Evaluar en −2 y en +2 da exactamente la misma altura y."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Función par (simétrica respecto al eje Y)",
                            "Función impar (simétrica respecto al origen)",
                            "Función exponencial",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Evaluar la función inversa f⁻¹ sin confundirse",
                "prompt": "Dada f(x) = 3x − 6, su función inversa es f⁻¹(x) = (x + 6) / 3. ¿Cuánto vale f⁻¹(9)? Respondé solo con el número.",
                "answer": "5: (9 + 6) / 3 = 15 / 3 = 5. Verificación: f(5) = 3(5) − 6 = 9.",
                "hints": ["También podés preguntar: ¿qué valor de x hace que 3x − 6 = 9?"],
                "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Estiramiento vertical de un punto",
                "prompt": "El punto (2, 4) pertenece a la gráfica de f(x). ¿Qué coordenada y tendrá el punto correspondiente en g(x) = 3 · f(x) − 2? Respondé solo con el número.",
                "answer": "10: primero multiplicamos la altura por 3 (3 × 4 = 12) y luego bajamos 2 (12 − 2 = 10).",
                "hints": ["Calculá 3 × 4 − 2."],
                "payload": {"check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Simetría gráfica entre f y su inversa f⁻¹",
                "prompt": "Si graficás una función f y su inversa f⁻¹ en el mismo plano cartesiano (por ejemplo y = 2ˣ y y = log₂(x)), ¿respecto a qué recta son espejos exactos?",
                "answer": "Respecto a la diagonal y = x, porque la inversa simplemente intercambia cada punto (a, b) en (b, a).",
                "hints": ["Cambiar x por y refleja sobre la diagonal principal."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["La diagonal y = x", "El eje X (y = 0)", "El eje Y (x = 0)"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "a2-racionales-asintotas",
        "title": "59. Funciones racionales: restricciones y asíntotas",
        "level": 21,
        "order_index": 59,
        "summary": "Cocientes de polinomios, valores prohibidos, agujeros (cancelación) vs. asíntotas verticales, y asíntotas horizontales.",
        "prerequisites": ["a2-polinomios-factorizacion", "al-dominio-rango"],
        "metadata": {"section": "Álgebra 2", "lab_tab": "polynomials", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Encontrar la asíntota vertical (denominador cero)",
                "prompt": "¿En qué valor de x tiene una asíntota vertical la función racional f(x) = (x + 2) / (x − 5)? Respondé solo con el número.",
                "answer": "5: en x = 5 el denominador se hace 0 mientras el numerador vale 7 (no se cancela), así que f(x) se dispara hacia ±∞.",
                "hints": ["Igualá el denominador a 0: x − 5 = 0."],
                "payload": {
                    "lab_link": "math:polynomials",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Distinguir agujero vs. asíntota vertical",
                "prompt": "En f(x) = (x² − 4) / (x − 2) = (x − 2)(x + 2) / (x − 2), el factor (x − 2) se cancela arriba y abajo. ¿Qué hay en x = 2?",
                "answer": "Un agujero (discontinuidad evitable) en el punto (2, 4): la función no está definida en x = 2, pero cerca de 2 se comporta suavemente como y = x + 2.",
                "hints": ["Cuando el factor que da 0 abajo también se cancela arriba, la gráfica NO se va al infinito."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Un agujero (discontinuidad evitable) en (2, 4)",
                            "Una asíntota vertical donde y → ±∞",
                            "Un punto normal continuo sin problema",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Asíntota horizontal cuando los grados empatan",
                "prompt": "¿A qué valor horizontal y se acerca f(x) = (6x + 1) / (2x − 5) cuando x se hace gigantesco (x → ∞)? Respondé solo con el número.",
                "answer": "3: como numerador y denominador tienen el mismo grado (1), para x enorme mandan los términos líderes → 6x / 2x = 3.",
                "hints": ["Dividí los coeficientes principales: 6 ÷ 2."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Costo promedio por unidad en un emprendimiento",
                "prompt": "Un taller tiene $1000 de costo fijo más $5 por remera. El costo promedio por remera es C(x) = (1000 + 5x) / x. Si fabricás x = 100 remeras, ¿cuántos pesos cuesta cada una? Respondé solo con el número.",
                "answer": "15 pesos: (1000 + 500) / 100 = 15 (y a medida que fabricás miles, baja acercándose a la asíntota horizontal de $5).",
                "hints": ["Evaluá (1000 + 5 × 100) ÷ 100."],
                "payload": {"check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": "$"}},
            },
            {
                "item_type": "worked_example",
                "title": "Asíntota horizontal cuando gana el denominador",
                "prompt": "¿Cuál es la asíntota horizontal y de f(x) = (4x + 7) / (x² + 1) cuando x → ∞? Respondé solo con el número.",
                "answer": "0: el denominador (x²) crece mucho más rápido que el numerador (4x), así que el cociente se aplasta hacia y = 0.",
                "hints": ["Si el grado de abajo es mayor que el de arriba, la fracción tiende siempre a 0."],
                "payload": {"check": {"type": "numeric", "value": 0, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Sumar fracciones algebraicas (1/x + 1/(2x))",
                "prompt": "Sumá 1/x + 1/(2x) llevando ambas fracciones a denominador común 2x y después evaluá el resultado para x = 3 en decimal. Respondé solo con el número.",
                "answer": "0.5: 1/x + 1/(2x) = 2/(2x) + 1/(2x) = 3/(2x); con x = 3 da 3 / 6 = 0.5 (comprobación: 1/3 + 1/6 = 1/2 = 0.5).",
                "hints": ["Multiplicá arriba y abajo de 1/x por 2 para que tenga denominador 2x.", "Sustituí x = 3 en 3 / (2x)."],
                "payload": {"check": {"type": "numeric", "value": 0.5, "tolerance": 0.01, "unit": ""}},
            },
        ],
    },
    {
        "slug": "a2-ecuaciones-avanzadas",
        "title": "60. Ecuaciones radicales, racionales y sistemas no lineales",
        "level": 21,
        "order_index": 60,
        "summary": "Despejar raíces y fracciones con x, atrapar soluciones extrañas verificando siempre, trabajo conjunto y recta + parábola.",
        "prerequisites": ["a2-racionales-asintotas", "al-parabolas-formula"],
        "metadata": {"section": "Álgebra 2", "lab_tab": "logarithms", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Resolver una ecuación radical despejando y elevando al cuadrado",
                "prompt": "Resolvé √(x + 5) = 4. ¿Cuánto vale x? Respondé solo con el número.",
                "answer": "11: elevamos ambos lados al cuadrado → x + 5 = 16 → x = 11. Verificación: √(11 + 5) = √16 = 4 (válida).",
                "hints": ["Elevá ambos lados al cuadrado para eliminar la raíz."],
                "payload": {
                    "lab_link": "math:logarithms",
                    "check": {"type": "numeric", "value": 11, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Atrapar una solución extraña en √(x + 2) = −3",
                "prompt": "Un alumno eleva al cuadrado ambos lados de √(x + 2) = −3, obtiene x + 2 = 9 → x = 7 y entrega esa respuesta. ¿Está bien?",
                "answer": "No, es una solución extraña (la ecuación NO tiene solución real): el símbolo √ devuelve siempre un resultado ≥ 0, nunca −3.",
                "hints": ["Probá x = 7 en la ecuación original: ¿√(7 + 2) da −3 o +3?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "No: x = 7 es extraña y la ecuación no tiene solución real",
                            "Sí: porque (−3)² = 9 y 7 + 2 = 9",
                            "La solución correcta es x = −11",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ecuación radical con dos candidatos (uno extraño)",
                "prompt": "Al resolver √(x + 6) = x, elevás al cuadrado: x + 6 = x² → (x − 3)(x + 2) = 0, dando candidatos x = 3 y x = −2. ¿Cuál es la ÚNICA solución real válida? Respondé solo con el número.",
                "answer": "3: probando en la original, √(3 + 6) = 3 sí cumple, pero √(−2 + 6) = 2 ≠ −2 (x = −2 es extraña).",
                "hints": ["Verificá x = 3 y x = −2 dentro de √(x + 6) = x."],
                "payload": {
                    "lab_link": "math:logarithms",
                    "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Problema real de tasas combinadas (dos bombas llenando un tanque)",
                "prompt": "La bomba A llena una pileta en 3 horas (1/3 por hora) y la bomba B sola tarda 6 horas (1/6 por hora). Usando 1/3 + 1/6 = 1/t, ¿en cuántas horas t la llenan trabajando juntas? Respondé solo con el número.",
                "answer": "2 horas: juntas llenan 1/3 + 1/6 = 3/6 = 1/2 pileta por hora, así que completan la pileta en 2 horas.",
                "hints": ["Sumá las velocidades por hora: 1/3 + 1/6 = 1/2."],
                "payload": {"check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "h"}},
            },
            {
                "item_type": "recall",
                "title": "Solución prohibida en una ecuación racional",
                "prompt": "En x / (x − 2) = 2 / (x − 2), si multiplicás ambos lados por (x − 2) te queda x = 2. ¿Por qué esta ecuación NO tiene solución?",
                "answer": "Porque x = 2 anula el denominador (divide por 0), así que no pertenece al dominio de la ecuación original.",
                "hints": ["Reemplazá x = 2 en el denominador (x − 2)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Porque x = 2 hace cero el denominador (división por cero)",
                            "Porque 2 no es negativo",
                            "Sí tiene solución: x = 2",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Sistema no lineal: intersección de parábola y recta",
                "prompt": "¿En qué coordenada x POSITIVA se cruzan la parábola y = x² y la recta y = x + 6? (Igualá x² = x + 6). Respondé solo con el número.",
                "answer": "3: x² − x − 6 = 0 → (x − 3)(x + 2) = 0 → se cruzan en x = −2 y x = 3 (en el punto (3, 9)).",
                "hints": ["Factorizá x² − x − 6 = 0."],
                "payload": {
                    "lab_link": "math:factoring",
                    "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                },
            },
        ],
    },
    # ==================== NIVEL 22: CÍRCULO UNITARIO, ONDAS Y MODELADO ====================
    {
        "slug": "a2-circulo-unitario-ondas",
        "title": "61. Círculo unitario, identidad pitagórica y ondas sinusoidales",
        "level": 22,
        "order_index": 61,
        "summary": "Seno y coseno para cualquier ángulo en el círculo unitario, sen²θ + cos²θ = 1, y amplitud/período/línea media de ondas.",
        "prerequisites": ["g-trigonometria", "g-circulos-arcos"],
        "metadata": {"section": "Álgebra 2", "lab_tab": "trig_waves", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Leer cos(180°) en el círculo unitario",
                "prompt": "En el círculo unitario (radio 1), cada ángulo θ marca el punto (cos θ, sen θ). A 180° (π rad) estás en el extremo izquierdo (−1, 0). ¿Cuánto vale cos(180°)? Respondé solo con el número.",
                "answer": "−1: la coordenada x es coseno y la coordenada y es seno; en (−1, 0), cos(180°) = −1 y sen(180°) = 0.",
                "hints": ["Coseno es siempre la coordenada horizontal x del punto en el círculo unitario."],
                "payload": {
                    "lab_link": "math:trig_waves",
                    "check": {"type": "numeric", "value": -1, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Identidad pitagórica: sen²(θ) + cos²(θ) = 1",
                "prompt": "Un ángulo del 1.er cuadrante tiene sen(θ) = 0.6. Usando sen²(θ) + cos²(θ) = 1, ¿cuánto vale cos(θ) en decimal? Respondé solo con el número.",
                "answer": "0.8: cos²(θ) = 1 − 0.6² = 1 − 0.36 = 0.64 → cos(θ) = √0.64 = 0.8 (en el 1.er cuadrante es positivo).",
                "hints": ["Calculá √(1 − 0.36)."],
                "payload": {
                    "lab_link": "math:trig_waves",
                    "check": {"type": "numeric", "value": 0.8, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Signos de seno y coseno en el 2.° cuadrante (90° a 180°)",
                "prompt": "Para un ángulo entre 90° y 180° (segundo cuadrante, arriba a la izquierda), ¿qué signos tienen cos(θ) y sen(θ)?",
                "answer": "cos(θ) es negativo (x < 0) y sen(θ) es positivo (y > 0).",
                "hints": ["Mirando el 2.° cuadrante: x está a la izquierda (−) e y está arriba (+)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "cos(θ) < 0 y sen(θ) > 0",
                            "Ambos positivos",
                            "cos(θ) > 0 y sen(θ) < 0",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Altura máxima de una marea sinusoidal",
                "prompt": "La altura de la marea en un puerto sigue h(t) = 1.5 · sen(0.5t) + 2.5 (en metros). Como el seno llega como máximo a +1, ¿cuántos metros alcanza la marea alta? Respondé solo con el número.",
                "answer": "4 m: línea media (2.5) + amplitud (1.5) = 4 m (y la marea baja es 2.5 − 1.5 = 1 m).",
                "hints": ["Sumá la línea media D = 2.5 más la amplitud A = 1.5."],
                "payload": {
                    "lab_link": "math:trig_waves",
                    "check": {"type": "numeric", "value": 4, "tolerance": 0.01, "unit": "m"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Leer la amplitud de una señal de voltaje alterno",
                "prompt": "Una señal de audio sinusoidal oscila entre −6 V (mínimo) y +6 V (máximo): v(t) = 6 · sen(ωt). ¿Cuál es su amplitud en voltios? Respondé solo con el número.",
                "answer": "6 V: la amplitud es la distancia desde el centro (0 V) hasta el pico (+6 V), es decir (máx − mín) / 2.",
                "hints": ["La amplitud es la mitad de la altura pico-a-pico."],
                "payload": {
                    "lab_link": "math:trig_waves",
                    "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": "V"},
                },
            },
            {
                "item_type": "recall",
                "title": "Cómo afecta B al período en y = sen(Bx)",
                "prompt": "El período normal de y = sen(x) es 2π. ¿Qué le ocurre al período de la onda en y = sen(2x)?",
                "answer": "Se reduce a la mitad (T = 2π / 2 = π): duplica la frecuencia, así que completa 2 ciclos donde antes hacía 1.",
                "hints": ["Fórmula del período: T = 2π / |B|."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Se acorta a la mitad (T = π, doble frecuencia)",
                            "Se duplica (T = 4π)",
                            "Sube la amplitud al doble",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "a2-modelado-composicion",
        "title": "62. Composición de funciones y elección de modelos reales",
        "level": 22,
        "order_index": 62,
        "summary": "Encadenar funciones f(g(x)) de adentro hacia afuera, combinar funciones (ingreso − costo) y elegir qué familia modela cada fenómeno.",
        "prerequisites": ["a2-logaritmos", "a2-transformaciones-funciones", "a2-circulo-unitario-ondas"],
        "metadata": {"section": "Álgebra 2", "lab_tab": "trig_waves", "est_minutes": 18},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Evaluar una composición f(g(x)) de adentro hacia afuera",
                "prompt": "Dadas g(x) = 2x + 1 y f(x) = x², calculá f(g(3)). Respondé solo con el número.",
                "answer": "49: primero evaluamos adentro g(3) = 2(3) + 1 = 7, y luego metemos ese resultado en f → f(7) = 7² = 49.",
                "hints": ["Calculá g(3) primero y elevá ese resultado al cuadrado."],
                "payload": {
                    "lab_link": "math:trig_waves",
                    "check": {"type": "numeric", "value": 49, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "El orden importa en la composición (descuento + cupón)",
                "prompt": "Una tienda aplica primero 20% de descuento (g(p) = 0.8p) y después un cupón fijo de −$1000 (f(x) = x − 1000). En una compra de $10 000, ¿cuánto pagás al aplicar f(g(10 000))? Respondé solo con el número.",
                "answer": "7000: primero 0.8 × 10 000 = 8000, luego 8000 − 1000 = $7000 (si aplicaran primero el cupón y luego el 20% pagarías $7200).",
                "hints": ["Sacá el 20% a 10 000 (queda 8000) y luego restá 1000."],
                "payload": {"check": {"type": "numeric", "value": 7000, "tolerance": 0, "unit": "$"}},
            },
            {
                "item_type": "worked_example",
                "title": "Combinar funciones: ganancia = ingreso − costo",
                "prompt": "Un emprendimiento tiene ingreso I(x) = 50x y costo C(x) = 20x + 600. Con G(x) = I(x) − C(x), ¿cuál es la ganancia para x = 30 unidades? Respondé solo con el número.",
                "answer": "300: I(30) = 1500, C(30) = 1200 → G(30) = 1500 − 1200 = 300 (o directo 30x − 600 = 900 − 600 = 300).",
                "hints": ["Calculá I(30) = 50 × 30 y restale C(30) = 20 × 30 + 600."],
                "payload": {"check": {"type": "numeric", "value": 300, "tolerance": 0, "unit": "$"}},
            },
            {
                "item_type": "recall",
                "title": "Elegir modelo para un fenómeno cíclico (temperatura anual)",
                "prompt": "Registrás la temperatura promedio mensual de tu ciudad durante 5 años: sube en verano, baja en invierno y repite el mismo ciclo cada 12 meses. ¿Qué familia de funciones la modela mejor?",
                "answer": "Una función sinusoidal (seno o coseno), porque oscila periódicamente entre un mínimo y un máximo fijos.",
                "hints": ["Buscá la función diseñada específicamente para ciclos periódicos."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Sinusoidal (seno / coseno)",
                            "Exponencial creciente",
                            "Lineal",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Distinguir modelo lineal vs. exponencial desde una tabla",
                "prompt": "En una tabla de valores equidistantes (x = 0, 1, 2, 3), las salidas y son 100, 120, 144, 172.8. ¿Qué modelo corresponde?",
                "answer": "Exponencial: las diferencias no son iguales (+20, +24, +28.8), pero la RAZÓN entre consecutivos es constante (×1.20 cada paso).",
                "hints": ["Dividí 120/100, 144/120 y 172.8/144."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Exponencial (multiplica por ×1.20 en cada paso)",
                            "Lineal (suma constante)",
                            "Logarítmico",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Composición de una función con su inversa",
                "prompt": "Si g es exactamente la función inversa de f (g = f⁻¹), ¿qué resultado devuelve SIEMPRE f(g(x)) para cualquier x válido?",
                "answer": "Devuelve el mismo valor x de entrada: una función y su inversa se cancelan mutuamente (como elevar al cubo y sacar raíz cúbica).",
                "hints": ["Pensá en calcular 10^(log₁₀(x)) o (√x)²."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["x (la entrada original intacta)", "1", "0"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
]

ALGEBRA2_LESSONS: dict[str, dict] = {
    "a2-numeros-complejos": {
        "hook": "Durante siglos se dijo que `√(−1)` era imposible, hasta que definir `i² = −1` destrabó las ecuaciones cúbicas, la corriente alterna y el procesamiento de señales.",
        "concept": {
            "points": [
                "La unidad imaginaria **`i`** se define por **`i² = −1`**. Sus potencias giran en un ciclo de 4: `i¹ = i`, `i² = −1`, `i³ = −i`, `i⁴ = 1` (usá el resto de dividir por 4).",
                "Un **número complejo `a + bi`** combina parte real (`a`) e imaginaria (`b`). Se suma por separado; al multiplicar aplicás distributiva y reemplazás **`i² → −1`**.",
                "El **conjugado** de `a + bi` es `a − bi`: su producto `(a + bi)(a − bi) = a² + b²` siempre da un número real que nunca es negativo (sirve para dividir complejos), y su módulo es `|a + bi| = √(a² + b²)`.",
            ],
            "real_world": [
                {
                    "title": "Electricidad de corriente alterna (impedancia)",
                    "detail": "En electrónica, la resistencia (real) y la reactancia de bobinas/capacitores (imaginaria) se combinan en un único número `Z = R + jX`.",
                },
                {
                    "title": "Audio, Wi-Fi y compresión (Transformada de Fourier)",
                    "detail": "Los filtros de ecualización y las señales de radio usan números complejos para representar amplitud y fase al mismo tiempo.",
                },
                {
                    "title": "Rotaciones en gráficos y física cuántica",
                    "detail": "Multiplicar un número complejo por `i` rota el punto exactamente `90°` antihorario en el plano complejo sin usar matrices.",
                },
            ],
            "key_rule": "i² = −1 | Ciclo de 4 para iⁿ | (a + bi)(a − bi) = a² + b² | Si Δ < 0, las raíces son pares conjugados a ± bi.",
            "pitfall": "Dejar `i²` sin reemplazar o olvidar el cambio de signo: `−3i²` vale `+3`, no `−3`.",
        },
        "example": {
            "title": "Multiplicar (2 + 3i)(4 − i) y resolver x² − 2x + 5 = 0",
            "steps": [
                "Distribuimos `(2 + 3i)(4 − i) = 8 − 2i + 12i − 3i²`.",
                "Reemplazamos `i² = −1`: `−3(−1) = +3`, así que juntando reales e imaginarios da `(8 + 3) + (−2 + 12)i = 11 + 10i`.",
                "En `x² − 2x + 5 = 0`: `Δ = 4 − 20 = −16` → `√(−16) = 4i` → `x = (2 ± 4i) / 2 = 1 ± 2i`.",
            ],
            "lab_link": "math:complex_nums",
            "lab_cta": "Practicar números complejos en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto vale `i³`?",
            "options": [
                {"text": "`−i`", "ok": True, "feedback": "Exacto: i³ = i² · i = (−1) · i = −i."},
                {"text": "`−1`", "ok": False, "feedback": "−1 es i², no i³."},
                {"text": "`1`", "ok": False, "feedback": "1 es i⁴ (vuelta completa del ciclo de 4)."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuánto da `(5 − 2i) − (1 + 4i)`?",
                "options": [
                    {"text": "`4 − 6i`", "ok": True, "feedback": "Exacto: 5 − 1 = 4 y −2i − 4i = −6i."},
                    {"text": "`4 + 2i`", "ok": False, "feedback": "El signo menos delante del paréntesis cambia también el +4i a −4i."},
                    {"text": "`6 − 6i`", "ok": False, "feedback": "Sumaste 5 + 1 en vez de restar 5 − 1."},
                ],
            },
            {
                "question": "¿Cuánto vale el producto con conjugado `(2 + 5i)(2 − 5i)`?",
                "options": [
                    {"text": "`29` (`2² + 5²`)", "ok": True, "feedback": "Exacto: 4 − 25i² = 4 + 25 = 29."},
                    {"text": "`−21` (`4 − 25`)", "ok": False, "feedback": "Te faltó multiplicar por i² = −1, que cambia el −25 a +25."},
                    {"text": "`4 + 25i`", "ok": False, "feedback": "Las partes imaginarias +10i y −10i se cancelan entre sí."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué multiplicar un número complejo por su conjugado siempre elimina la letra `i`.",
    },
    "a2-polinomios-factorizacion": {
        "hook": "Factorizar un polinomio de grado 3 o 4 parece intimidante, pero casi siempre se reduce a los mismos tres moldes que ya sabés de cuadráticas.",
        "concept": {
            "points": [
                "Siempre seguí un orden: **1) Factor común** primero; **2) Contar términos**: 2 términos → diferencia de cuadrados o suma/diferencia de cubos; 3 términos → forma cuadrática (`u = x²`); 4 términos → **agrupación de a pares**.",
                "En **formas cuadráticas** como `x⁴ − 5x² + 4`, renombrá `u = x²`: queda `u² − 5u + 4 = (u − 4)(u − 1)` y luego volvés a `x`.",
                "Para **cubos**: `a³ − b³ = (a − b)(a² + ab + b²)` y `a³ + b³ = (a + b)(a² − ab + b²)`. Y el **Triángulo de Pascal** da directo los coeficientes de `(a + b)ⁿ`.",
            ],
            "real_world": [
                {
                    "title": "Curvas de diseño (Bézier y fuentes tipográficas)",
                    "detail": "Las letras que estás leyendo y los trazos de Illustrator son curvas de Bézier: polinomios de grado 2 o 3 evaluados a toda velocidad.",
                },
                {
                    "title": "Optimizar el volumen de una caja",
                    "detail": "Al doblar solapas de largo `x` en una plancha de cartón, el volumen es `V(x) = x(L − 2x)(A − 2x)`, un polinomio de grado 3.",
                },
                {
                    "title": "Aproximación de funciones en calculadoras",
                    "detail": "Calculadoras y computadoras aproximan `sen(x)` o `eˣ` con polinomios (la misma idea que está detrás de las series de Taylor).",
                },
            ],
            "key_rule": "Orden de ataque: 1) Factor común → 2) Agrupación (4 términos) / Forma cuadrática (u = x²) / Cubos (a³ ± b³).",
            "pitfall": "Creer que `(x + 2)³ = x³ + 8`: faltan los términos cruzados (`x³ + 6x² + 12x + 8`).",
        },
        "example": {
            "title": "Factorizar completamente 2x³ − 18x y x⁴ − 5x² + 4",
            "steps": [
                "En `2x³ − 18x`, sacamos factor común `2x`: queda `2x(x² − 9)`.",
                "Reconocemos diferencia de cuadrados en `x² − 9`: resultado final `2x(x − 3)(x + 3)`.",
                "En `x⁴ − 5x² + 4`, sustituimos `u = x²` → `(u − 4)(u − 1) = (x² − 4)(x² − 1) = (x − 2)(x + 2)(x − 1)(x + 1)`.",
            ],
            "lab_link": "math:factoring",
            "lab_cta": "Practicar factorización en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es la factorización completa de `x³ + 3x² + 2x + 6` por agrupación?",
            "options": [
                {"text": "`(x² + 2)(x + 3)`", "ok": True, "feedback": "Exacto: x²(x + 3) + 2(x + 3) = (x² + 2)(x + 3)."},
                {"text": "`(x² + 3)(x + 2)`", "ok": False, "feedback": "Si expandís eso te da x³ + 2x² + 3x + 6 (los coeficientes del medio quedan al revés)."},
                {"text": "`x(x² + 3x + 2) + 6`", "ok": False, "feedback": "Eso todavía tiene un '+ 6' suelto afuera, no está factorizado."},
            ],
        },
        "checks": [
            {
                "question": "Usando `u = x²`, ¿cómo se factoriza `x⁴ − 9x² + 8`?",
                "options": [
                    {"text": "`(x² − 8)(x² − 1)` (y luego `(x² − 8)(x − 1)(x + 1)`)", "ok": True, "feedback": "Exacto: −8 y −1 suman −9 y multiplican +8."},
                    {"text": "`(x² − 4)(x² − 2)`", "ok": False, "feedback": "−4 y −2 suman −6, no −9."},
                    {"text": "`(x − 8)(x − 1)`", "ok": False, "feedback": "Al expandir eso te da grado 2 (x²), no grado 4 (x⁴)."},
                ],
            },
            {
                "question": "¿Cuál es el coeficiente principal y el grado de `5x² − 3x⁴ + 7`?",
                "options": [
                    {"text": "Grado `4`, coeficiente principal `−3`", "ok": True, "feedback": "Exacto: el término líder es −3x⁴ (el de mayor exponente)."},
                    {"text": "Grado `2`, coeficiente principal `5`", "ok": False, "feedback": "5x² está escrito primero, pero x⁴ tiene mayor exponente."},
                    {"text": "Grado `4`, coeficiente principal `3`", "ok": False, "feedback": "No te olvides del signo negativo delante del 3."},
                ],
            },
        ],
        "takeaway_prompt": "Anotá tu lista ordenada de pasos para factorizar cualquier polinomio de grado 3 o 4 sin quedarte trabado.",
    },
    "a2-division-polinomios": {
        "hook": "Si solo necesitás saber si `(x − 2)` divide exacto a un polinomio de grado 5, no hace falta hacer ninguna división larga: el Teorema del Resto te da la respuesta en 3 segundos.",
        "concept": {
            "points": [
                "Igual que con números (`17 = 5·3 + 2`), dividir polinomios da **`P(x) = D(x)·Q(x) + R(x)`**, donde el resto `R` tiene grado menor que el divisor `D`.",
                "**Teorema del Resto**: el resto de dividir `P(x)` por `(x − c)` es simplemente evaluar **`P(c)`** (ojo al signo: para `(x + 3)` evaluás `P(−3)`).",
                "**Teorema del Factor**: `(x − c)` es factor exacto de `P(x)` **si y solo si `P(c) = 0`**. Para obtener el cociente rápido usás **división sintética (Ruffini)**, poniendo `0` en cualquier potencia que falte.",
            ],
            "real_world": [
                {
                    "title": "Códigos de verificación de errores (CRC)",
                    "detail": "Wi-Fi, Ethernet y archivos ZIP detectan bytes corruptos calculando el resto de dividir un polinomio de bits por un divisor estándar.",
                },
                {
                    "title": "Encontrar raíces de ecuaciones cúbicas en ingeniería",
                    "detail": "Probás un candidato entero con el Teorema del Resto (`P(c) = 0`), bajás el grado con Ruffini y resolvés la cuadrática restante.",
                },
                {
                    "title": "Simplificar fórmulas racionales",
                    "detail": "Dividir el numerador por el denominador separa la parte entera (tendencia a largo plazo) del resto que se achica cuando `x` crece.",
                },
            ],
            "key_rule": "Resto de P(x) ÷ (x − c) = P(c). Es factor exacto ⇔ P(c) = 0.",
            "pitfall": "Evaluar `P(+3)` cuando el divisor es `(x + 3)` o saltear columnas con coeficiente `0` al armar Ruffini.",
        },
        "example": {
            "title": "Comprobar si (x − 2) divide a P(x) = x³ − 4x² + x + 6",
            "steps": [
                "Buscamos el valor que anula al divisor `(x − 2)`: es `c = 2`.",
                "Aplicamos el Teorema del Resto evaluando `P(2) = 2³ − 4(2²) + 2 + 6 = 8 − 16 + 2 + 6 = 0`.",
                "Como el resto dio `0`, por el Teorema del Factor `(x − 2)` divide exactamente a `P(x)` (y el cociente por Ruffini es `x² − 2x − 3 = (x − 3)(x + 1)`).",
            ],
            "lab_link": "math:polynomials",
            "lab_cta": "Practicar Teorema del Resto en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es el resto de dividir `P(x) = x³ + 2x − 4` por `(x − 1)`?",
            "options": [
                {"text": "`−1`", "ok": True, "feedback": "Exacto: P(1) = 1 + 2 − 4 = −1."},
                {"text": "`−7`", "ok": False, "feedback": "Eso evaluó P(−1), pero para (x − 1) se evalúa en +1."},
                {"text": "`0`", "ok": False, "feedback": "1 + 2 − 4 no da cero, así que (x − 1) no es factor."},
            ],
        },
        "checks": [
            {
                "question": "Si al evaluar `P(−4)` obtenés `0`, ¿cuál es obligatoriamente un factor de `P(x)`?",
                "options": [
                    {"text": "`(x + 4)`", "ok": True, "feedback": "Exacto: el factor que se anula en x = −4 es (x − (−4)) = (x + 4)."},
                    {"text": "`(x − 4)`", "ok": False, "feedback": "En x = −4, (x − 4) vale −8, no 0."},
                    {"text": "`(x − 0)`", "ok": False, "feedback": "x = 0 sería raíz si P(0) = 0."},
                ],
            },
            {
                "question": "Al dividir `P(x) = 2x⁴ − 3x + 1` con Ruffini, ¿cuántos ceros faltantes debés intercalar en los coeficientes?",
                "options": [
                    {"text": "Dos ceros (`2, 0, 0, −3, 1`, faltan `x³` y `x²`)", "ok": True, "feedback": "Exacto: siempre van todas las potencias en orden desde grado 4 hasta grado 0."},
                    {"text": "Ninguno (`2, −3, 1`)", "ok": False, "feedback": "Sin los ceros de x³ y x², Ruffini trataría el polinomio como si fuera de grado 2."},
                    {"text": "Uno solo", "ok": False, "feedback": "Faltan tanto x³ como x²."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en tus palabras cómo te ahorra cuentas el Teorema del Resto antes de hacer una división larga.",
    },
    "a2-graficas-polinomios": {
        "hook": "Con solo mirar el exponente de cada paréntesis y el término más grande podés dibujar la forma exacta de cualquier polinomio de grado 5 sin hacer tablas de 20 puntos.",
        "concept": {
            "points": [
                "Cada factor `(x − r)^m` te da una **raíz (cero) en `x = r`** con **multiplicidad `m`**: si `m` es **impar** la curva **cruza** el eje X; si `m` es **par** **rebota** sin cruzar.",
                "El **comportamiento en los extremos** (`x → ±∞`) depende SOLO del término líder `a · xⁿ`: **grado par** = ambos brazos van para el mismo lado (`a > 0` arriba, `a < 0` abajo); **grado impar** = brazos opuestos (`a > 0` sube de izq. a der.).",
                "La **ordenada al origen** es `P(0)` y un polinomio de grado `n` tiene a lo sumo `n` raíces reales y **`n − 1` giros**.",
            ],
            "real_world": [
                {
                    "title": "Análisis de estabilidad y puntos de equilibrio",
                    "detail": "Donde la curva cruza el eje X (multiplicidad impar) una magnitud cambia de signo (ej. pasar de pérdida a ganancia); donde rebota solo roza el cero.",
                },
                {
                    "title": "Predecir tendencias extremas",
                    "detail": "Cuando `x` es grande, el término de mayor grado aplasta a todos los demás: define por sí solo si el modelo se dispara hacia `+∞` o `−∞`.",
                },
                {
                    "title": "Diseño de montañas rusas y trayectorias suaves",
                    "detail": "Los polinomios son curvas continuas sin esquinas ni saltos; elegir sus raíces y multiplicidades permite fijar dónde tocan el suelo suavemente.",
                },
            ],
            "key_rule": "Multiplicidad impar = cruza | Multiplicidad par = rebota | Extremos: solo importa el término líder a·xⁿ.",
            "pitfall": "Mirar solo el número de factores y olvidar sumar sus exponentes al calcular el grado total del polinomio.",
        },
        "example": {
            "title": "Bosquejar P(x) = (x + 1)²(x − 3)",
            "steps": [
                "Raíces y multiplicidad: en `x = −1` (mult. 2, par) la gráfica **rebota**; en `x = 3` (mult. 1, impar) **cruza** el eje X.",
                "Término líder: `x² · x = +1x³` (grado 3 impar, coef. positivo) → viene desde `−∞` a la izquierda y sube a `+∞` a la derecha.",
                "Corte con eje Y: `P(0) = (1)²(−3) = −3`. Con esos tres datos ya sabés toda la silueta exacta.",
            ],
            "lab_link": "math:polynomials",
            "lab_cta": "Practicar polinomios en el Laboratorio",
        },
        "check": {
            "question": "En `P(x) = (x − 2)³(x + 5)²`, ¿qué hace la curva en `x = 2` y en `x = −5`?",
            "options": [
                {"text": "Cruza en `x = 2` (mult. impar) y rebota en `x = −5` (mult. par)", "ok": True, "feedback": "Exacto: exponente 3 es impar (cruza) y exponente 2 es par (rebota)."},
                {"text": "Rebota en ambos puntos", "ok": False, "feedback": "Solo rebota cuando el exponente del factor es par."},
                {"text": "Cruza en `x = −2` y rebota en `x = 5`", "ok": False, "feedback": "Recordá invertir el signo al leer las raíces desde (x − r)."},
            ],
        },
        "checks": [
            {
                "question": "Un polinomio tiene grado `4` y coeficiente principal `+2`. ¿Hacia dónde van sus dos extremos?",
                "options": [
                    {"text": "Ambos hacia `+∞` (arriba)", "ok": True, "feedback": "Exacto: grado par y coeficiente positivo hacen que ambos brazos suban."},
                    {"text": "Ambos hacia `−∞` (abajo)", "ok": False, "feedback": "Eso ocurriría si el coeficiente principal fuera negativo."},
                    {"text": "Izquierda abajo y derecha arriba", "ok": False, "feedback": "Brazos opuestos corresponde a grado impar."},
                ],
            },
            {
                "question": "¿Cuál es el grado total de `P(x) = 3x(x − 1)²(x + 4)`?",
                "options": [
                    {"text": "`4` (`1 + 2 + 1`)", "ok": True, "feedback": "Exacto: no te olvides del factor x¹ de adelante."},
                    {"text": "`3`", "ok": False, "feedback": "Te olvidaste de contar la x de adelante o el exponente 2."},
                    {"text": "`2`", "ok": False, "feedback": "Hay que sumar los exponentes de todos los factores con x."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá la diferencia visual en el eje X entre una raíz de multiplicidad par y una de multiplicidad impar.",
    },
    "a2-modelos-exponenciales": {
        "hook": "Un préstamo al 5% mensual NO es un 60% anual: por el efecto compuesto es casi un 80%. Reescribir exponentes te muestra la tasa real en la unidad de tiempo que necesitás.",
        "concept": {
            "points": [
                "Si un proceso multiplica por `b` cada `T` unidades de tiempo, la fórmula es **`y(t) = a · b^(t/T)`** (ej. vida media de 6 h: `a · (0.5)^(t/6)`).",
                "Para cambiar la unidad de tiempo usás las leyes de potencias: **`b^(t/T) = (b^(1/T))^t`**. Así convertís tasas anuales a mensuales (o viceversa) sin cometer el error lineal de dividir porcentajes.",
                "El **número de Euler `e ≈ 2.71828`** surge cuando el crecimiento compuesto es continuo (**`P(t) = P₀ · e^(rt)`**), clave en biología, física radiactiva y finanzas.",
            ],
            "real_world": [
                {
                    "title": "TEA vs. tasa mensual en tarjetas y préstamos",
                    "detail": "Una tasa mensual del `5%` equivale a `(1.05)¹² − 1 ≈ 79.6%` efectivo anual, nunca `12 × 5% = 60%`.",
                },
                {
                    "title": "Farmacocinética (cada cuántas horas tomar un remedio)",
                    "detail": "Si un antibiótico tiene vida media de 6 horas, `C(t) = C₀ · (0.5)^(t/6)` determina cuándo vuelve a caer bajo el umbral efectivo.",
                },
                {
                    "title": "Datación por carbono-14",
                    "detail": "El C-14 cae a la mitad cada `5730` años (`(0.5)^(t/5730)`), permitiendo datar restos orgánicos (madera, huesos, telas) de hasta unos `50 000` años.",
                },
            ],
            "key_rule": "Cada período T: y = a · b^(t/T) | Cambiar unidad: b^(kt) = (b^k)^t | Continuo: P₀ · e^(rt).",
            "pitfall": "Dividir una tasa compuesta de 2 años por 2 (creer que +21% en 2 años es +10.5% anual): la tasa anual real es `√1.21 − 1 = 10%`.",
        },
        "example": {
            "title": "Reescribir P(t) = 100 · 4^(t/2) para ver la tasa por año",
            "steps": [
                "Separamos el exponente usando `(a^m)^n`: `4^(t/2) = (4^(1/2))^t`.",
                "Calculamos la base anual: `4^(1/2) = √4 = 2`.",
                "Queda `P(t) = 100 · 2^t`: cuadruplicarse cada 2 años equivale exactamente a **duplicarse (+100%) cada 1 año**.",
            ],
            "lab_link": "math:exponentials",
            "lab_cta": "Practicar modelos exponenciales en el Laboratorio",
        },
        "check": {
            "question": "Un cultivo se multiplica por `9` cada `2` horas (`P(t) = 50 · 9^(t/2)`). ¿Por cuánto se multiplica cada `1` hora?",
            "options": [
                {"text": "Por `3` (`√9 = 3`)", "ok": True, "feedback": "Exacto: en 2 horas hace ×3 ×3 = ×9."},
                {"text": "Por `4.5` (`9 ÷ 2`)", "ok": False, "feedback": "Dividir por 2 sería lineal; en exponenciales se saca la raíz cuadrada."},
                {"text": "Por `81` (`9²`)", "ok": False, "feedback": "81 sería el factor en 4 horas, no en 1 hora."},
            ],
        },
        "checks": [
            {
                "question": "Si una sustancia sigue `M(t) = 80 · (0.5)^(t/5)` (t en días), ¿cuánto queda a los `15` días?",
                "options": [
                    {"text": "`10` (`80 ÷ 8`)", "ok": True, "feedback": "Exacto: 15/5 = 3 vidas medias → 80 × (0.5)³ = 10."},
                    {"text": "`40`", "ok": False, "feedback": "40 es a los 5 días (1 sola vida media)."},
                    {"text": "`20`", "ok": False, "feedback": "20 es a los 10 días (2 vidas medias)."},
                ],
            },
            {
                "question": "En `V(t) = 5000 · (0.92)^t`, ¿la cantidad crece o decae, y a qué porcentaje por período?",
                "options": [
                    {"text": "Decae un `8%` por período", "ok": True, "feedback": "Exacto: 1 − 0.92 = 0.08 = 8% de caída por período."},
                    {"text": "Decae un `92%` por período", "ok": False, "feedback": "0.92 es lo que QUEDA, así que lo que se pierde es 8%."},
                    {"text": "Crece un `92%` por período", "ok": False, "feedback": "Como la base 0.92 es menor que 1, siempre decae."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué un +10% anual durante 2 años da +21% y no +20%, y cómo se revierte ese cálculo con exponentes fraccionarios.",
    },
    "a2-logaritmos": {
        "hook": "¿Cómo despejás `t` cuando está atrapado en el exponente (`2^t = 50`)? Para eso existen los logaritmos: son la herramienta exacta que 'baja' el exponente.",
        "concept": {
            "points": [
                "Un logaritmo solo reescribe una potencia: **`log_b(y) = x  ⇔  bˣ = y`** (lee siempre: *'¿a qué exponente elevo `b` para llegar a `y`?'*). Solo está definido para **`y > 0`**.",
                "Dos bases famosas: **`log(x)`** es base `10`, y **`ln(x)`** es base `e`. Para cualquier otra base usás el **cambio de base**: `log_b(y) = ln(y) / ln(b)`.",
                "**Tres propiedades de oro** (porque los logaritmos son exponentes!): producto → suma **`log(AB) = log A + log B`**; cociente → resta **`log(A/B) = log A − log B`**; potencia → baja multiplicando **`log(A^k) = k · log A`**.",
            ],
            "real_world": [
                {
                    "title": "Decibeles (audio) y escala de Richter (terremotos)",
                    "detail": "Nuestro oído percibe el volumen en escala logarítmica: multiplicar la potencia sonora por `10` suma apenas `+10 dB`.",
                },
                {
                    "title": "Tiempo de duplicación de inversiones",
                    "detail": "Despejar `1.08^t = 2` con logaritmos da `t = ln(2) / ln(1.08) ≈ 9` años.",
                },
                {
                    "title": "Eficiencia de algoritmos (`O(log n)`)",
                    "detail": "Buscar un nombre en 1 000 000 de registros ordenados (búsqueda binaria) toma solo `log₂(1 000 000) ≈ 20` comparaciones.",
                },
            ],
            "key_rule": "log_b(y) = x ⇔ bˣ = y | log(A·B) = log A + log B | log(A^k) = k·log A | Cambio de base: ln(y)/ln(b).",
            "pitfall": "Inventar `log(A + B) = log A + log B`: el logaritmo transforma MULTIPLICACIONES en sumas, nunca separa una suma adentro del paréntesis.",
        },
        "example": {
            "title": "Resolver 3 · 2^x = 48 y evaluar log₃(81)",
            "steps": [
                "Primero aislamos la potencia dividiendo por 3: `2^x = 48 / 3 = 16`.",
                "Aplicamos la definición de logaritmo: `x = log₂(16) = 4` (porque `2⁴ = 16`).",
                "Para `log₃(81)`: preguntamos `3^(?) = 81` → `3⁴ = 81` → `log₃(81) = 4`.",
            ],
            "lab_link": "math:logarithms",
            "lab_cta": "Practicar logaritmos en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto vale `log₅(125)`?",
            "options": [
                {"text": "`3`", "ok": True, "feedback": "Exacto: 5³ = 5 × 5 × 5 = 125."},
                {"text": "`25`", "ok": False, "feedback": "Dividiste 125 ÷ 5, pero el logaritmo busca el exponente."},
                {"text": "`5`", "ok": False, "feedback": "5⁵ = 3125, demasiado grande."},
            ],
        },
        "checks": [
            {
                "question": "Simplificá `log₁₀(200) − log₁₀(2)` usando propiedades de logaritmos:",
                "options": [
                    {"text": "`2` (`log₁₀(200 / 2) = log₁₀(100) = 2`)", "ok": True, "feedback": "Exacto: resta de logaritmos se convierte en división de argumentos."},
                    {"text": "`log₁₀(198)`", "ok": False, "feedback": "Restar logaritmos DIVIDE los números de adentro, no los resta."},
                    {"text": "`100`", "ok": False, "feedback": "100 es el argumento; falta tomar log₁₀(100) = 2."},
                ],
            },
            {
                "question": "¿Cuánto vale `log_b(1)` para cualquier base válida `b > 0, b ≠ 1`?",
                "options": [
                    {"text": "`0` (porque `b⁰ = 1`)", "ok": True, "feedback": "Exacto: cualquier base elevada a 0 da 1."},
                    {"text": "`1`", "ok": False, "feedback": "Da 1 cuando el argumento es b (log_b(b) = 1)."},
                    {"text": "No existe", "ok": False, "feedback": "No existe para 0 o negativos; para 1 siempre vale 0."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en una frase qué pregunta responde `log_b(y)` y cómo se usa para despejar una `x` en el exponente.",
    },
    "a2-transformaciones-funciones": {
        "hook": "Si sabés cómo se transforma UNA sola gráfica (mover, estirar, espejar), automáticamente sabés graficar parábolas, raíces, exponenciales, logaritmos y ondas sin empezar de cero.",
        "concept": {
            "points": [
                "Regla universal para **`g(x) = a · f(x − h) + k`**: **`+k`** sube, **`−k`** baja; **`(x − h)`** corre a la **derecha** y **`(x + h)`** a la **izquierda** (adentro va al revés!); **`a`** estira/comprime verticalmente y un signo menos afuera (`−f(x)`) refleja sobre el eje X.",
                "Simetría: una función es **par** si **`f(−x) = f(x)`** (espejo en eje Y, como `x²` o `cos x`), e **impar** si **`f(−x) = −f(x)`** (rotación 180° respecto al origen, como `x³` o `sen x`).",
                "La **función inversa `f⁻¹`** invierte entradas y salidas (refleja la gráfica sobre `y = x`): para hallarla despejás `x` en `y = f(x)` e intercambias `x` e `y`.",
            ],
            "real_world": [
                {
                    "title": "Calibración de sensores (gain y offset)",
                    "detail": "Ajustar un micrófono o termómetro con `g(x) = a·f(x) + k` es literalmente un estiramiento vertical (ganancia `a`) más un desplazamiento (offset `k`).",
                },
                {
                    "title": "Desfase temporal en señales (`f(t − τ)`)",
                    "detail": "Un eco o retardo de `2` segundos en un sonido se escribe `f(t − 2)`: corre la onda 2 segundos hacia la derecha en el tiempo.",
                },
                {
                    "title": "Cifrado y conversión reversible (`f` y `f⁻¹`)",
                    "detail": "Pasar de Celsius a Fahrenheit (`f`) y volver de Fahrenheit a Celsius (`f⁻¹`) es un par de funciones inversas exactas.",
                },
            ],
            "key_rule": "Afuera = vertical y directo (a·f + k) | Adentro = horizontal e invertido (f(x − h)) | Inversa = espejo en y = x.",
            "pitfall": "Mover `f(x + 4)` hacia la derecha por ver un signo '+': para que `x + 4` vuelva a valer 0, `x` tiene que ser `−4` (se mueve a la IZQUIERDA).",
        },
        "example": {
            "title": "Hallar la inversa de f(x) = 3x − 6 y transformar y = x²",
            "steps": [
                "Para la inversa: escribimos `y = 3x − 6`, despejamos `x`: `y + 6 = 3x` → `x = (y + 6) / 3`.",
                "Intercambiamos letras: `f⁻¹(x) = (x + 6) / 3`. Chequeo: `f(5) = 9` y `f⁻¹(9) = 5`.",
                "Para `g(x) = −(x − 2)² + 5`: tomamos `y = x²`, la invertimos boca abajo (`−`), la movemos `2` a la derecha y `5` arriba → vértice en `(2, 5)`.",
            ],
            "lab_link": "math:quadratics",
            "lab_cta": "Practicar vértices y transformaciones en el Laboratorio",
        },
        "check": {
            "question": "¿Cómo se mueve la gráfica de `y = |x|` para obtener `y = |x + 4| − 7`?",
            "options": [
                {"text": "`4` a la izquierda y `7` hacia abajo", "ok": True, "feedback": "Exacto: adentro es invertido (+4 → izquierda) y afuera es directo (−7 → abajo)."},
                {"text": "`4` a la derecha y `7` hacia abajo", "ok": False, "feedback": "Adentro del paréntesis el signo funciona al revés: x + 4 = 0 da x = −4."},
                {"text": "`7` a la izquierda y `4` hacia abajo", "ok": False, "feedback": "Mezclaste el desplazamiento horizontal con el vertical."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál de estas funciones es IMPAR (`f(−x) = −f(x)`)?",
                "options": [
                    {"text": "`f(x) = x³ − 2x`", "ok": True, "feedback": "Exacto: (−x)³ − 2(−x) = −x³ + 2x = −(x³ − 2x)."},
                    {"text": "`f(x) = x² + 1`", "ok": False, "feedback": "Esa es PAR: f(−x) = x² + 1 = f(x)."},
                    {"text": "`f(x) = x³ + 1`", "ok": False, "feedback": "El +1 rompe la simetría respecto del origen: no es ni par ni impar."},
                ],
            },
            {
                "question": "Si `f(2) = 7` y `f` tiene inversa, ¿cuánto vale obligatoriamente `f⁻¹(7)`?",
                "options": [
                    {"text": "`2`", "ok": True, "feedback": "Exacto: la inversa intercambia entrada y salida."},
                    {"text": "`1/7`", "ok": False, "feedback": "Cuidado con la notación: f⁻¹ significa función inversa, NO 1 dividido f."},
                    {"text": "`−7`", "ok": False, "feedback": "No es el opuesto; deshace lo que hizo f."},
                ],
            },
        ],
        "takeaway_prompt": "Resumí en una frase la regla de 'adentro vs. afuera' para mover cualquier función sin equivocarte de dirección.",
    },
    "a2-racionales-asintotas": {
        "hook": "Al dividir por una expresión con `x`, aparecen zonas prohibidas y barreras invisibles (asíntotas): la curva nunca toca una asíntota vertical, y a la horizontal se le acerca cada vez más cuando `x` se hace enorme.",
        "concept": {
            "points": [
                "Una **función racional** es un cociente `P(x) / Q(x)`. Primero factorizá arriba y abajo para ver los ceros del denominador (`Q(x) = 0`, siempre excluidos del dominio).",
                "Si un factor `(x − a)` del denominador **se cancela por completo** con el numerador, hay un **agujero** en `x = a`. Si después de simplificar **sigue quedando abajo**, hay una **asíntota vertical** en `x = a`.",
                "**Asíntota horizontal** (cuando `x → ±∞`): compará grados → **gana abajo**: `y = 0`; **empatan**: cociente de coeficientes líderes (`a/b`); **gana arriba**: no hay horizontal.",
            ],
            "real_world": [
                {
                    "title": "Costo promedio por unidad producida",
                    "detail": "Con costo fijo `$F` y variable `$v`, `C(x) = (F + vx)/x` cae rápido al inicio y tiende a la asíntota horizontal `$v` (nunca baja de ahí).",
                },
                {
                    "title": "Ley de Ohm y cortocircuitos (`I = V / R`)",
                    "detail": "Cuando la resistencia `R → 0` (asíntota vertical), la corriente `I` se dispara hacia infinito y quema el fusible.",
                },
                {
                    "title": "Concentración al diluir una mezcla",
                    "detail": "Si agregás agua pura a una solución salina, la concentración `(sal) / (V₀ + x)` tiende a la asíntota horizontal `0` pero nunca llega a cero exacto.",
                },
            ],
            "key_rule": "Factorizá primero: factor cancelado = agujero | factor sin cancelar abajo = asíntota vertical | Horizontal: compará grados.",
            "pitfall": "Olvidar que aunque canceles `(x − 2)` arriba y abajo, `x = 2` SIGUE excluido del dominio (queda un agujero).",
        },
        "example": {
            "title": "Analizar f(x) = (2x² − 8) / (x² − x − 2)",
            "steps": [
                "Factorizamos arriba y abajo: `2(x − 2)(x + 2) / ((x − 2)(x + 1))`.",
                "El factor `(x − 2)` se cancela → hay un **agujero** en `x = 2`. El factor `(x + 1)` queda abajo → **asíntota vertical** en `x = −1`.",
                "Mismo grado arriba y abajo (`2x²` y `1x²`) → **asíntota horizontal** en `y = 2 / 1 = 2`.",
            ],
            "lab_link": "math:polynomials",
            "lab_cta": "Practicar asíntotas y polinomios en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es la asíntota horizontal de `f(x) = (8x² + 3) / (2x² − 5x + 1)`?",
            "options": [
                {"text": "`y = 4` (`8 / 2`)", "ok": True, "feedback": "Exacto: empatan en grado 2, así que manda el cociente de coeficientes líderes 8/2 = 4."},
                {"text": "`y = 0`", "ok": False, "feedback": "y = 0 ocurre solo cuando el grado del denominador es estrictamente mayor."},
                {"text": "`y = 3`", "ok": False, "feedback": "Los términos constantes (+3 y +1) no importan cuando x es enorme."},
            ],
        },
        "checks": [
            {
                "question": "En `f(x) = (x + 3) / ((x + 3)(x − 4))`, ¿qué hay en `x = −3` y qué hay en `x = 4`?",
                "options": [
                    {"text": "Agujero en `x = −3` y asíntota vertical en `x = 4`", "ok": True, "feedback": "Exacto: (x + 3) se cancela (agujero) y (x − 4) queda abajo (asíntota vertical)."},
                    {"text": "Asíntotas verticales en ambos", "ok": False, "feedback": "Como (x + 3) se cancela con el numerador, en x = −3 hay un agujero, no una asíntota."},
                    {"text": "Agujero en `x = 4` y asíntota vertical en `x = −3`", "ok": False, "feedback": "Es exactamente al revés."},
                ],
            },
            {
                "question": "¿Para qué valor de `x` NO está definida `g(x) = 5 / (2x − 6)`?",
                "options": [
                    {"text": "`x = 3`", "ok": True, "feedback": "Exacto: 2(3) − 6 = 0 anula el denominador."},
                    {"text": "`x = 6`", "ok": False, "feedback": "En x = 6 el denominador da 6, no 0."},
                    {"text": "`x = −3`", "ok": False, "feedback": "2(−3) − 6 = −12 ≠ 0."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá cómo saber de un vistazo la asíntota horizontal y si un cero del denominador produce agujero o asíntota vertical.",
    },
    "a2-ecuaciones-avanzadas": {
        "hook": "Elevar al cuadrado o multiplicar por `(x − 2)` te ayuda a resolver ecuaciones difíciles, pero puede colar 'soluciones impostoras' que fallan si no las comprobás.",
        "concept": {
            "points": [
                "**Ecuaciones radicales**: aislá la raíz primero (`√(...) = ...`), elevá al cuadrado ambos lados, resolvé y **VERIFICÁ SIEMPRE** en la ecuación original para descartar **soluciones extrañas**.",
                "**Ecuaciones racionales**: multiplicá todo por el denominador común para limpiar fracciones, pero descartá cualquier candidato que haga **cero algún denominador**.",
                "**Sistemas no lineales** (ej. recta + parábola): igualás las `y`, resolvés la cuadrática y hallás 0, 1 o 2 puntos de cruce.",
            ],
            "real_world": [
                {
                    "title": "Trabajo en equipo (tasas sumadas)",
                    "detail": "Si una impresora tarda `A` horas y otra `B` horas, juntas cumplen `1/A + 1/B = 1/t` (se suman velocidades, nunca los tiempos).",
                },
                {
                    "title": "Física: distancia de frenado o péndulo (`T = 2π√(L/g)`)",
                    "detail": "Despejar el largo `L` del péndulo desde su período `T` requiere aislar la raíz cuadrada y elevar al cuadrado.",
                },
                {
                    "title": "Trayectorias que se interceptan",
                    "detail": "Calcular en qué instante un proyectil (parábola) alcanza la altura de un dron en ascenso (recta) es resolver un sistema no lineal.",
                },
            ],
            "key_rule": "Aislá la raíz o limpiá denominadores → resolvé → VERIFICÁ SIEMPRE en la ecuación original (ojo con √ = negativo y ÷ 0).",
            "pitfall": "Elevar al cuadrado `(√x + 3)²` como `x + 9`: primero tenés que aislar la raíz sola de un lado antes de elevar al cuadrado.",
        },
        "example": {
            "title": "Resolver √(x + 6) = x y filtrar la solución extraña",
            "steps": [
                "La raíz ya está aislada. Elevamos ambos lados al cuadrado: `x + 6 = x²`.",
                "Pasamos todo de un lado y factorizamos: `x² − x − 6 = 0` → `(x − 3)(x + 2) = 0` → candidatos `x = 3` y `x = −2`.",
                "Verificamos en la original: con `x = 3`, `√9 = 3` (SÍ). Con `x = −2`, `√4 = 2 ≠ −2` (extraña, se descarta). Única solución: `x = 3`.",
            ],
            "lab_link": "math:logarithms",
            "lab_cta": "Practicar ecuaciones radicales en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es la solución de `√(2x − 1) = 3`?",
            "options": [
                {"text": "`x = 5`", "ok": True, "feedback": "Exacto: 2x − 1 = 9 → 2x = 10 → x = 5. Comprobación: √(10 − 1) = √9 = 3."},
                {"text": "`x = 2`", "ok": False, "feedback": "Te faltó elevar el 3 al cuadrado (9, no 3)."},
                {"text": "`x = 4`", "ok": False, "feedback": "Sumaste mal al despejar: 9 + 1 = 10, y 10 ÷ 2 = 5."},
            ],
        },
        "checks": [
            {
                "question": "Si dos canillas llenan un tanque solas en `4 h` y `4 h`, ¿en cuánto tiempo lo llenan abiertas juntas?",
                "options": [
                    {"text": "`2` horas (`1/4 + 1/4 = 1/2` por hora)", "ok": True, "feedback": "Exacto: dos canillas idénticas duplican el caudal y reducen el tiempo a la mitad."},
                    {"text": "`8` horas (`4 + 4`)", "ok": False, "feedback": "Sumar los tiempos daría más lento con dos canillas que con una sola!"},
                    {"text": "`4` horas", "ok": False, "feedback": "Con el doble de caudal tarda la mitad del tiempo."},
                ],
            },
            {
                "question": "¿Por qué puede aparecer una solución extraña al resolver una ecuación radical?",
                "options": [
                    {"text": "Porque elevar al cuadrado borra signos negativos (`(−3)² = (+3)²`), aceptando raíces falsas", "ok": True, "feedback": "Exacto: por eso siempre hay que chequear en la ecuación original."},
                    {"text": "Porque las raíces cuadradas no tienen solución nunca", "ok": False, "feedback": "Muchas sí tienen solución (por ejemplo `√(x + 5) = 4` da `x = 11`); lo que no puede pasar es que una raíz cuadrada dé un resultado negativo."},
                    {"text": "Porque no se puede factorizar una cuadrática", "ok": False, "feedback": "La cuadrática se resuelve bien; el problema viene del paso de elevar al cuadrado."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué verificar los resultados es obligatorio (y no opcional) en ecuaciones radicales y racionales.",
    },
    "a2-circulo-unitario-ondas": {
        "hook": "Los triángulos rectángulos solo llegan hasta `90°`. El círculo unitario libera al seno y al coseno para CUALQUIER ángulo y genera las ondas que describen sonido, luz y corriente alterna.",
        "concept": {
            "points": [
                "En el **círculo unitario** (centro `(0, 0)`, radio `1`), girar un ángulo `θ` desde el eje `+X` marca el punto **`(cos θ, sen θ)`**. Como está sobre `x² + y² = 1`, siempre se cumple **`sen²θ + cos²θ = 1`**.",
                "Eso define `sen` y `cos` en los 4 cuadrantes (incluso negativos y mayores a `360°`): el signo sale directo del cuadrante (`cos` = signo de `x`, `sen` = signo de `y`).",
                "Al graficar **`y = A · sen(Bx) + D`** (o `cos`): **`|A|`** = amplitud (altura desde el centro), **`D`** = línea media (máx `D + |A|`, mín `D − |A|`) y **`T = 2π / |B|`** = período.",
            ],
            "real_world": [
                {
                    "title": "Corriente alterna de tu enchufe (50/60 Hz)",
                    "detail": "El voltaje de la pared oscila como una onda sinusoidal perfecta `50` veces por segundo (período `T = 0.02 s`).",
                },
                {
                    "title": "Notas musicales y sintetizadores",
                    "detail": "La nota La 440 Hz es una onda `A · sen(2π · 440 · t)`: cambiar `A` cambia el volumen y cambiar `B` cambia el tono musical.",
                },
                {
                    "title": "Rueda de la fortuna y mareas",
                    "detail": "La altura de una cabina en una noria de radio `15 m` con centro a `18 m` oscila entre `3 m` y `33 m` siguiendo una onda sinusoidal.",
                },
            ],
            "key_rule": "Círculo unitario: (x, y) = (cos θ, sen θ) | sen²θ + cos²θ = 1 | Onda A·sen(Bx) + D: amp |A|, centro D, período 2π/|B|.",
            "pitfall": "Creer que un `B` más grande hace la onda más ancha: al revés, `T = 2π / B` comprime la onda (más ciclos en el mismo tiempo).",
        },
        "example": {
            "title": "Leer amplitud, rango y período de y = 3 · cos(2x) + 4",
            "steps": [
                "Línea media `D = 4` y amplitud `|A| = 3`.",
                "Rango vertical: máximo `4 + 3 = 7` y mínimo `4 − 3 = 1` (la onda oscila siempre entre `1` y `7`).",
                "Período: `T = 2π / 2 = π` (completa un ciclo entero cada `π` radianes).",
            ],
            "lab_link": "math:trig_waves",
            "lab_cta": "Practicar ondas y círculo unitario en el Laboratorio",
        },
        "check": {
            "question": "En el círculo unitario, el ángulo `90°` (`π/2`) cae en `(0, 1)`. ¿Cuánto valen `cos(90°)` y `sen(90°)`?",
            "options": [
                {"text": "`cos(90°) = 0` y `sen(90°) = 1`", "ok": True, "feedback": "Exacto: (x, y) = (cos, sen) = (0, 1)."},
                {"text": "`cos(90°) = 1` y `sen(90°) = 0`", "ok": False, "feedback": "Al revés: x es coseno (0) e y es seno (1)."},
                {"text": "Ambos valen `1`", "ok": False, "feedback": "En (1, 1) el radio sería √2, fuera del círculo unitario."},
            ],
        },
        "checks": [
            {
                "question": "Una noria tiene altura `h(t) = 10 · sen(t) + 12` (en metros). ¿Cuál es la altura MÍNIMA que alcanza una cabina?",
                "options": [
                    {"text": "`2 m` (`12 − 10`)", "ok": True, "feedback": "Exacto: cuando sen(t) llega a su mínimo (−1), h = 12 − 10 = 2 m."},
                    {"text": "`10 m`", "ok": False, "feedback": "10 m es la amplitud (el radio de la noria), no la altura mínima."},
                    {"text": "`22 m`", "ok": False, "feedback": "22 m es la altura máxima (12 + 10)."},
                ],
            },
            {
                "question": "Si `cos(θ) = 0.8` y `θ` está en el 4.° cuadrante (abajo a la derecha, `y < 0`), ¿cuánto vale `sen(θ)`?",
                "options": [
                    {"text": "`−0.6`", "ok": True, "feedback": "Exacto: √(1 − 0.64) = 0.6, y en el 4.° cuadrante y (seno) es negativo."},
                    {"text": "`+0.6`", "ok": False, "feedback": "Fijate el cuadrante: abajo del eje X el seno es negativo."},
                    {"text": "`−0.2`", "ok": False, "feedback": "Restaste 1 − 0.8 sin elevar al cuadrado ni sacar raíz."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué representa cada letra (`A`, `B`, `D`) en una onda `y = A · sen(Bx) + D` usando un ejemplo físico.",
    },
    "a2-modelado-composicion": {
        "hook": "En la vida real casi nunca hay una sola fórmula aislada: la salida de un paso alimenta al siguiente (composición), y la habilidad clave es saber qué familia de funciones elegir.",
        "concept": {
            "points": [
                "**Composición `(f ∘ g)(x) = f(g(x))`**: se evalúa siempre **de adentro hacia afuera** (primero `g(x)`, y ese resultado entra en `f`). En general **`f(g(x)) ≠ g(f(x))`**: el orden importa.",
                "**Combinar funciones**: podés sumar, restar o multiplicar modelos (ej. `Ganancia(x) = Ingreso(x) − Costo(x)` o `Área(x) = Base(x) · Altura(x)`).",
                "**Mapa rápido para elegir modelo**: cambio aditivo constante → **lineal**; cambio porcentual/multiplicativo constante → **exponencial**; sube y baja con un pico simétrico → **cuadrático**; repite ciclos regulares → **sinusoidal**.",
            ],
            "real_world": [
                {
                    "title": "Cadena de descuentos e impuestos",
                    "detail": "Aplicar primero un cupón fijo y luego un descuento porcentual da un precio distinto que hacerlo al revés (`f(g(p)) ≠ g(f(p))`).",
                },
                {
                    "title": "Conversión de unidades encadenada",
                    "detail": "Pasar de horas a km recorridos (`d(t)`) y luego de km a litros de nafta (`L(d)`) es literalmente `L(d(t))`.",
                },
                {
                    "title": "Ciencia de datos y pronósticos",
                    "detail": "Antes de ajustar una curva a datos reales, elegís la familia correcta mirando si crece sumando, multiplicando o ciclando.",
                },
            ],
            "key_rule": "(f ∘ g)(x) = f(g(x)) (de adentro hacia afuera) | Lineal (+c), Exponencial (×r), Cuadrático (pico), Sinusoidal (ciclo).",
            "pitfall": "Confundir `(f ∘ g)(x)` (composición: meter `g` adentro de `f`) con `(f · g)(x)` (multiplicar los dos resultados).",
        },
        "example": {
            "title": "Comparar f(g(3)) y g(f(3)) con f(x) = x² y g(x) = 2x + 1",
            "steps": [
                "Para `f(g(3))`: evaluamos adentro `g(3) = 2(3) + 1 = 7`, y luego `f(7) = 7² = 49`.",
                "Para `g(f(3))`: evaluamos adentro `f(3) = 3² = 9`, y luego `g(9) = 2(9) + 1 = 19`.",
                "Conclusión: `49 ≠ 19`, lo que prueba que en composición el orden cambia por completo el resultado.",
            ],
            "lab_link": "math:trig_waves",
            "lab_cta": "Practicar composición y ondas en el Laboratorio",
        },
        "check": {
            "question": "Si `f(x) = x + 5` y `g(x) = 3x`, ¿cuánto vale `g(f(2))`?",
            "options": [
                {"text": "`21`", "ok": True, "feedback": "Exacto: primero f(2) = 7, luego g(7) = 3 × 7 = 21."},
                {"text": "`11`", "ok": False, "feedback": "11 es f(g(2)): hiciste el orden al revés."},
                {"text": "`42`", "ok": False, "feedback": "Multiplicaste f(2) × g(2) = 7 × 6 = 42 en vez de componer."},
            ],
        },
        "checks": [
            {
                "question": "El brillo de una lámpara que pierde `8%` de intensidad cada año se modela mejor con una función:",
                "options": [
                    {"text": "Exponencial decreciente (`y = a · 0.92^t`)", "ok": True, "feedback": "Exacto: perder un porcentaje fijo cada período es un factor multiplicativo constante."},
                    {"text": "Lineal decreciente", "ok": False, "feedback": "Una lineal perdería siempre la misma cantidad fija, no el mismo porcentaje."},
                    {"text": "Sinusoidal", "ok": False, "feedback": "La lámpara no vuelve a subir su brillo cíclicamente."},
                ],
            },
            {
                "question": "Un objeto lanzado hacia arriba alcanza su altura máxima a los `2 s` y cae simétricamente al suelo a los `4 s`. ¿Qué modelo lo describe?",
                "options": [
                    {"text": "Cuadrático (parábola boca abajo)", "ok": True, "feedback": "Exacto: gravedad constante produce una trayectoria cuadrática con un único máximo simétrico."},
                    {"text": "Logarítmico", "ok": False, "feedback": "El logaritmo crece siempre más lento pero nunca baja."},
                    {"text": "Lineal", "ok": False, "feedback": "Una recta no puede subir y luego volver a bajar."},
                ],
            },
        ],
        "takeaway_prompt": "Nombrá las cuatro grandes familias de modelos (lineal, cuadrático, exponencial, sinusoidal) con un ejemplo real de cada una.",
    },
}
