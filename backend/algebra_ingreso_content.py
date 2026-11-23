"""Temas de álgebra que completan el temario de ingreso a ingeniería (UTN/UBA/UNLP).

Cinco nodos que se intercalan en Álgebra 1 y Álgebra 2 mediante `insert_after`:
  - Conjuntos numéricos, intervalos y notación
  - Expresiones algebraicas racionales y racionalización
  - Raíces racionales (Gauss) y factorización completa de polinomios
  - Ecuaciones exponenciales y logarítmicas
  - Inecuaciones cuadráticas, racionales y con valor absoluto
"""

from __future__ import annotations

ALGEBRA_INGRESO_NODES: list[dict] = [
    # ==================== CONJUNTOS NUMÉRICOS E INTERVALOS ====================
    {
        "slug": "al-conjuntos-intervalos",
        "title": "Conjuntos numéricos, intervalos y notación",
        "summary": "Clasificar números en ℕ, ℤ, ℚ, irracionales y ℝ, escribir desigualdades como intervalos y operar con unión e intersección.",
        "prerequisites": ["p-desigualdades"],
        "insert_after": "p-sistemas-ecuaciones",
        "metadata": {"section": "Álgebra 1", "lab_tab": "linear_eq", "est_minutes": 15},
        "items": [
            {
                "item_type": "recall",
                "title": "Ubicar un número en el conjunto más chico que lo contiene",
                "prompt": "Los conjuntos numéricos van uno dentro del otro: ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ. ¿Cuál es el MÁS CHICO de ellos que contiene al número −12/4?",
                "answer": "ℤ: −12/4 = −3, que es un entero negativo. No es natural (los naturales no llevan signo menos) y, aunque también es racional y real, el conjunto más chico que lo contiene es ℤ. Que esté escrito como fracción no lo saca de los enteros.",
                "hints": ["Hacé la división antes de clasificar.", "El resultado no tiene parte decimal, pero sí signo menos."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["ℕ (naturales)", "ℤ (enteros)", "ℚ (racionales), pero no ℤ", "ℝ, porque es irracional"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Contar los irracionales de una lista",
                "prompt": "Mirá esta lista de números: √16; √10; 0.333…; π; −5/2; √2/2. ¿Cuántos de ellos son irracionales? Respondé solo con el número.",
                "answer": "3: son irracionales √10, π y √2/2. En cambio √16 = 4 es entero, 0.333… = 1/3 es periódico (racional) y −5/2 es un cociente de enteros.",
                "hints": [
                    "La raíz cuadrada de un natural es irracional solo cuando ese natural no es un cuadrado perfecto.",
                    "Un decimal periódico siempre se puede escribir como fracción; dividir un irracional por 2 no lo vuelve racional.",
                ],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Pasar de una desigualdad doble a un intervalo",
                "prompt": "¿Qué intervalo representa a todos los x que cumplen −2 ≤ x < 5?",
                "answer": "[−2, 5): el ≤ del lado de −2 indica que −2 entra (corchete) y el < del lado de 5 indica que 5 no entra (paréntesis).",
                "hints": ["≤ y ≥ van con corchete (el extremo entra); < y > van con paréntesis (no entra)."],
                "payload": {
                    "lab_link": "math:linear_eq",
                    "check": {
                        "type": "choice",
                        "options": ["(−2, 5]", "[−2, 5)", "[−2, 5]", "(−2, 5)"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Escribir x ≥ 3 con un intervalo infinito",
                "prompt": "¿Cómo se escribe en notación de intervalos el conjunto de los x que cumplen x ≥ 3?",
                "answer": "[3, +∞): el 3 entra (corchete, por el ≥) y el infinito siempre lleva paréntesis, porque no es un número que se pueda alcanzar ni incluir.",
                "hints": ["Preguntate si el 3 cumple la desigualdad.", "+∞ no es un número: nunca lleva corchete."],
                "payload": {
                    "lab_link": "math:linear_eq",
                    "check": {
                        "type": "choice",
                        "options": ["(3, +∞)", "[3, +∞]", "[3, +∞)", "(−∞, 3]"],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Contar los enteros de un intervalo abierto",
                "prompt": "¿Cuántos números enteros pertenecen al intervalo abierto (−3, 4)? Respondé solo con el número.",
                "answer": "6: los extremos no entran, así que los enteros son −2, −1, 0, 1, 2 y 3. Ojo: la resta 4 − (−3) = 7 da la longitud del intervalo, no la cantidad de enteros.",
                "hints": ["Listalos: el primero es el entero que le sigue a −3.", "No te olvides del 0."],
                "payload": {"check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Intersección de dos intervalos que se solapan",
                "prompt": "¿Cuánto da [−1, 6) ∩ (2, 9]?",
                "answer": "(2, 6): la intersección tiene los números que están en los DOS intervalos a la vez, o sea los que cumplen x > 2 y x < 6. El 2 no entra (queda afuera del segundo intervalo) y el 6 tampoco (queda afuera del primero).",
                "hints": [
                    "Dibujá los dos en la recta numérica y quedate con la parte donde se pisan.",
                    "Un extremo entra solo si pertenece a AMBOS intervalos.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["[−1, 9]", "(2, 6)", "[2, 6]", "(2, 6]"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Unión de dos intervalos que se solapan",
                "prompt": "¿Cuánto da (−∞, 2) ∪ [0, 5]?",
                "answer": "(−∞, 5]: la unión junta todo lo que está en al menos uno de los dos. Como se solapan entre 0 y 2, queda un solo intervalo desde −∞ hasta 5, y el 5 entra porque pertenece a [0, 5]. En cambio [0, 2) es la intersección.",
                "hints": ["Unión significa 'o': alcanza con estar en uno de los dos.", "Fijate si el 5 pertenece a alguno de los dos intervalos."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["[0, 2)", "(−∞, 5)", "(−∞, 5]"],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Mayor entero de una intersección de intervalos",
                "prompt": "Sea A = (−∞, 7) ∩ [2, 10]. ¿Cuál es el mayor número entero que pertenece a A? Respondé solo con el número.",
                "answer": "6: la intersección es [2, 7), porque hay que cumplir x < 7 y 2 ≤ x ≤ 10 a la vez. El 7 no entra (paréntesis), así que el mayor entero de A es 6.",
                "hints": ["Primero escribí la intersección como un solo intervalo.", "Mirá si el extremo derecho está incluido o no."],
                "payload": {"check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    # ==================== EXPRESIONES RACIONALES Y RACIONALIZACIÓN ====================
    {
        "slug": "a2-expresiones-racionales",
        "title": "Expresiones algebraicas racionales y racionalización",
        "summary": "Simplificar, multiplicar, dividir y sumar cocientes de polinomios cuidando el dominio, y racionalizar denominadores con raíces.",
        "prerequisites": ["a2-polinomios-factorizacion", "al-exponentes-radicales"],
        "insert_after": "a2-polinomios-factorizacion",
        "metadata": {"section": "Álgebra 2", "lab_tab": "factoring", "est_minutes": 25},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Simplificar una expresión racional sin perder la restricción",
                "prompt": "Simplificá (x² − 9)/(x² − 5x + 6) factorizando numerador y denominador. ¿Cuál es el resultado correcto?",
                "answer": "(x + 3)/(x − 2), válido para x ≠ 2 y x ≠ 3: el numerador es (x − 3)(x + 3) y el denominador es (x − 2)(x − 3). Se cancela el factor (x − 3), pero la expresión original no existe en x = 3 (da 0/0), así que esa restricción se conserva. Tachar los x² no vale: solo se cancelan factores, nunca términos.",
                "hints": [
                    "x² − 9 es una diferencia de cuadrados; para x² − 5x + 6 buscá dos números que multiplicados den 6 y sumados −5.",
                    "El factor que cancelás igual anulaba el denominador original.",
                ],
                "payload": {
                    "lab_link": "math:factoring",
                    "check": {
                        "type": "choice",
                        "options": [
                            "(x + 3)/(x − 2), válido para todo x ≠ 2",
                            "(x + 3)/(x − 2), válido para x ≠ 2 y x ≠ 3",
                            "9/(5x − 6)",
                            "(x − 3)/(x − 2), válido para x ≠ 2 y x ≠ 3",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Contar los valores excluidos del dominio",
                "prompt": "¿Cuántos valores reales de x hay que excluir del dominio de (x − 1)/(x³ − 4x)? Respondé solo con el número.",
                "answer": "3: el denominador se factoriza como x(x − 2)(x + 2), que se anula en x = 0, x = 2 y x = −2. El numerador no influye en el dominio.",
                "hints": ["Factorizá el denominador: primero sacá factor común x.", "Lo que queda adentro es una diferencia de cuadrados."],
                "payload": {
                    "lab_link": "math:factoring",
                    "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Dividir expresiones racionales multiplicando por la recíproca",
                "prompt": "Calculá [(x² − 4)/(x + 3)] ÷ [(x − 2)/(x² + 3x)] y simplificá (suponé que x no anula ningún denominador).",
                "answer": "x(x + 2): dividir es multiplicar por la recíproca de la segunda fracción → (x − 2)(x + 2)/(x + 3) · x(x + 3)/(x − 2). Se cancelan (x − 2) y (x + 3), y queda x(x + 2).",
                "hints": ["Da vuelta la SEGUNDA fracción y multiplicá.", "x² + 3x = x(x + 3) y x² − 4 = (x − 2)(x + 2)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["1/(x(x + 2))", "(x − 2)²(x + 2)/(x(x + 3)²)", "x(x + 2)"],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Grado del denominador común mínimo",
                "prompt": "Para sumar 3/(x² − 4) + 5/(x² + 2x) hace falta el denominador común mínimo (el mcm de los dos denominadores). ¿Qué grado tiene ese polinomio? Respondé solo con el número.",
                "answer": "3: x² − 4 = (x − 2)(x + 2) y x² + 2x = x(x + 2). El mcm toma cada factor distinto con su mayor exponente: x(x − 2)(x + 2), de grado 3. Multiplicar directamente los dos denominadores daría grado 4, con el factor (x + 2) repetido de más.",
                "hints": ["Factorizá cada denominador.", "El factor que comparten se pone una sola vez."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Sumar fracciones algebraicas con denominadores distintos",
                "prompt": "¿Cuánto da 2/(x − 1) + 3/(x + 2), escrito como una sola fracción?",
                "answer": "(5x + 1)/((x − 1)(x + 2)): el denominador común es (x − 1)(x + 2). Amplificando cada fracción, el numerador queda 2(x + 2) + 3(x − 1) = 2x + 4 + 3x − 3 = 5x + 1.",
                "hints": [
                    "Multiplicá cada numerador por el factor que le falta a su denominador.",
                    "Nunca se suman numeradores con numeradores y denominadores con denominadores.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "5/(2x + 1)",
                            "(5x + 1)/((x − 1)(x + 2))",
                            "(5x + 7)/((x − 1)(x + 2))",
                            "5/((x − 1)(x + 2))",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Simplificar una fracción compleja",
                "prompt": "Simplificá la fracción compleja (1/x − 1/3)/(x − 3), con x ≠ 0 y x ≠ 3.",
                "answer": "−1/(3x): arriba, 1/x − 1/3 = (3 − x)/(3x). Dividir por (x − 3) es multiplicar por 1/(x − 3), así que queda (3 − x)/(3x(x − 3)). Como 3 − x = −(x − 3), el cociente de esos factores es −1 y el resultado es −1/(3x).",
                "hints": [
                    "Primero uní el numerador en una sola fracción con denominador 3x.",
                    "3 − x y x − 3 son opuestos: fijate qué signo queda al cancelarlos.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["1/(3x)", "−1/(3x)", "−3x"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Racionalizar un denominador con una sola raíz",
                "prompt": "Al racionalizar 15/√5 el resultado se puede escribir como k·√5, con k entero. ¿Cuánto vale k? Respondé solo con el número.",
                "answer": "3: multiplicando numerador y denominador por √5 queda 15√5/5 = 3√5.",
                "hints": ["Multiplicá arriba y abajo por √5.", "√5 · √5 = 5; después simplificá el número que quedó adelante."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Denominador que queda al multiplicar por el conjugado",
                "prompt": "Para racionalizar 14/(3 − √2) multiplicás numerador y denominador por el conjugado del denominador. ¿Qué número entero queda en el denominador? Respondé solo con el número.",
                "answer": "7: el conjugado es 3 + √2 y (3 − √2)(3 + √2) = 3² − (√2)² = 9 − 2 = 7. La fracción queda 14(3 + √2)/7 = 6 + 2√2.",
                "hints": ["El conjugado de a − √b es a + √b.", "Usá la diferencia de cuadrados: (a − b)(a + b) = a² − b²."],
                "payload": {"check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    # ==================== RAÍCES RACIONALES Y FACTORIZACIÓN COMPLETA ====================
    {
        "slug": "a2-raices-racionales-factorizacion",
        "title": "Raíces racionales (Gauss) y factorización completa de polinomios",
        "summary": "Listar candidatos p/q, probarlos con el teorema del resto, bajar el grado con Ruffini y factorizar por completo polinomios de grado 3 y 4.",
        "prerequisites": ["a2-division-polinomios"],
        "insert_after": "a2-division-polinomios",
        "metadata": {"section": "Álgebra 2", "lab_tab": "polynomials", "est_minutes": 25},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Contar los candidatos a raíz racional (Gauss)",
                "prompt": "Según el teorema de las raíces racionales, ¿cuántos candidatos a raíz racional tiene P(x) = x³ − 4x² + x + 6, contando positivos y negativos? Respondé solo con el número.",
                "answer": "8: como el coeficiente principal es 1, los candidatos son los divisores del término independiente 6 con ambos signos: ±1, ±2, ±3 y ±6.",
                "hints": ["Listá los divisores positivos del término independiente.", "Cada divisor vale con signo + y con signo −."],
                "payload": {
                    "lab_link": "math:polynomials",
                    "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Descartar un número que no puede ser raíz racional",
                "prompt": "P(x) = 3x³ − 2x² − 7x − 2 tiene coeficientes enteros. Según el teorema de Gauss, ¿cuál de estos números NO puede ser raíz de P?",
                "answer": "3/2: una raíz racional p/q (irreducible) necesita que p divida al término independiente (−2) y que q divida al coeficiente principal (3). Los candidatos son ±1, ±2, ±1/3 y ±2/3. En 3/2 la fracción está invertida.",
                "hints": ["Numerador: divisores del término independiente. Denominador: divisores del coeficiente principal."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["−1/3", "2/3", "3/2", "−2"],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Probar candidatos con el teorema del resto",
                "prompt": "Buscá una raíz de P(x) = x³ − 7x − 6 probando los candidatos POSITIVOS de menor a mayor con el teorema del resto. ¿Cuál es el primero que da P(c) = 0? Respondé solo con el número.",
                "answer": "3: P(1) = 1 − 7 − 6 = −12, P(2) = 8 − 14 − 6 = −12 y P(3) = 27 − 21 − 6 = 0. Como el resto de dividir por (x − 3) es P(3) = 0, x = 3 es raíz y (x − 3) es factor.",
                "hints": [
                    "Los candidatos positivos son los divisores positivos del término independiente.",
                    "Reemplazá cada uno en P(x) hasta que el resultado sea 0.",
                ],
                "payload": {
                    "lab_link": "math:polynomials",
                    "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Bajar el grado con Ruffini usando una raíz conocida",
                "prompt": "x = 1 es raíz de P(x) = x³ − 2x² − 5x + 6. Dividí P(x) por (x − 1) con Ruffini. ¿Cuál es el término independiente del cociente? Respondé solo con el número.",
                "answer": "−6: Ruffini con 1 sobre los coeficientes 1, −2, −5, 6 da 1, −1, −6 y resto 0. El cociente es x² − x − 6, así que P(x) = (x − 1)(x² − x − 6) = (x − 1)(x − 3)(x + 2).",
                "hints": [
                    "Bajá el primer coeficiente, multiplicalo por la raíz y sumá en la columna siguiente.",
                    "El último número es el resto (tiene que dar 0); el anterior es el término independiente del cociente.",
                ],
                "payload": {
                    "lab_link": "math:polynomials",
                    "check": {"type": "numeric", "value": -6, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Factorización completa con coeficiente principal distinto de 1",
                "prompt": "P(x) = 2x³ + 3x² − 8x + 3 tiene a x = 1 como raíz. ¿Cuál es su factorización completa?",
                "answer": "(x − 1)(2x − 1)(x + 3): Ruffini con 1 da el cociente 2x² + 5x − 3, cuyas raíces son 1/2 y −3. Entonces P(x) = 2(x − 1)(x − 1/2)(x + 3) y, metiendo el 2 en el segundo factor, queda (x − 1)(2x − 1)(x + 3). Sin el coeficiente principal 2 el producto no reconstruye a P.",
                "hints": [
                    "Dividí por (x − 1) con Ruffini y resolvé la cuadrática que queda.",
                    "P(x) = a(x − r₁)(x − r₂)(x − r₃): no te olvides del coeficiente principal a.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "(x − 1)(x − 1/2)(x + 3)",
                            "(x + 1)(2x + 1)(x − 3)",
                            "(x − 1)(2x − 1)(x + 3)",
                            "(x − 1)(2x + 1)(x − 3)",
                        ],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Multiplicidad de una raíz repetida",
                "prompt": "x = 1 es raíz de P(x) = x³ − 3x + 2. ¿Con qué multiplicidad (cuántas veces aparece el factor (x − 1) en la factorización completa de P)? Respondé solo con el número.",
                "answer": "2: Ruffini con 1 sobre los coeficientes 1, 0, −3, 2 (ojo con el 0 del término x² que falta) da el cociente x² + x − 2 = (x − 1)(x + 2). Entonces P(x) = (x − 1)²(x + 2): la raíz 1 es doble.",
                "hints": [
                    "Al armar Ruffini poné un 0 en el lugar del término x² que falta.",
                    "Después de dividir, fijate si x = 1 también anula al cociente.",
                ],
                "payload": {"check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Completar la factorización de un polinomio de grado 4",
                "prompt": "Sabiendo que x = 1 y x = −1 son raíces de P(x) = x⁴ − x³ − 13x² + x + 12, ¿cuál es la MAYOR de sus cuatro raíces? Respondé solo con el número.",
                "answer": "4: Ruffini con 1 da el cociente x³ − 13x − 12, y Ruffini con −1 sobre ese cociente da x² − x − 12 = (x − 4)(x + 3). Entonces P(x) = (x − 1)(x + 1)(x − 4)(x + 3), con raíces −3, −1, 1 y 4.",
                "hints": [
                    "Dividí por (x − 1) y después dividí el cociente por (x + 1): Ruffini dos veces.",
                    "Queda una cuadrática: factorizala o usá la resolvente.",
                ],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Cantidad máxima de raíces reales según el grado",
                "prompt": "Un polinomio de grado 4 con coeficientes reales, ¿cuántas raíces reales distintas puede tener?",
                "answer": "Como máximo 4 (puede tener 0, 1, 2, 3 o 4): cada raíz real r aporta un factor (x − r), y en un polinomio de grado 4 no entran más de 4 factores de grado 1. Puede no tener ninguna: x⁴ + 1 no se anula para ningún x real. Los que tienen al menos una raíz real asegurada son los de grado impar.",
                "hints": [
                    "Cada raíz r corresponde a un factor (x − r): pensá cuántos entran en grado 4.",
                    "Pensá en x⁴ + 1: ¿se anula para algún x real?",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Exactamente 4, siempre",
                            "Como máximo 4: puede tener 0, 1, 2, 3 o 4",
                            "Como mínimo 1 y como máximo 4",
                            "Puede tener más de 4 si los coeficientes son grandes",
                        ],
                        "correct": 1,
                    },
                },
            },
        ],
    },
    # ==================== ECUACIONES EXPONENCIALES Y LOGARÍTMICAS ====================
    {
        "slug": "a2-ecuaciones-exponenciales-logaritmicas",
        "title": "Ecuaciones exponenciales y logarítmicas",
        "summary": "Resolver ecuaciones con la incógnita en el exponente o dentro de un logaritmo: igualar bases, aplicar logaritmos, cambio de variable y verificación del dominio.",
        "prerequisites": ["a2-logaritmos"],
        "insert_after": "a2-logaritmos",
        "metadata": {"section": "Álgebra 2", "lab_tab": "logarithms", "est_minutes": 25},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Igualar bases para resolver una ecuación exponencial",
                "prompt": "Resolvé 4^(x + 1) = 8^(x − 1) escribiendo ambos lados como potencias de 2. ¿Cuánto vale x? Respondé solo con el número.",
                "answer": "5: como 4 = 2² y 8 = 2³, queda 2^(2(x + 1)) = 2^(3(x − 1)). Igualando exponentes: 2x + 2 = 3x − 3 → x = 5.",
                "hints": [
                    "Escribí 4 y 8 como potencias de 2.",
                    "Potencia de potencia: los exponentes se multiplican, distribuyendo en todo el paréntesis.",
                ],
                "payload": {
                    "lab_link": "math:logarithms",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Aplicar logaritmo cuando no se pueden igualar las bases",
                "prompt": "¿Cuál es la solución exacta de 3^(x + 1) = 7?",
                "answer": "x = ln 7 / ln 3 − 1: aplicando ln a ambos lados, (x + 1) · ln 3 = ln 7 → x + 1 = ln 7 / ln 3. Ojo: ln 7 / ln 3 (≈ 1.77) no es lo mismo que ln(7/3) (≈ 0.85).",
                "hints": [
                    "Aplicá ln a los dos lados y bajá el exponente: ln(aⁿ) = n · ln a.",
                    "El cociente de dos logaritmos NO es el logaritmo del cociente.",
                ],
                "payload": {
                    "lab_link": "math:logarithms",
                    "check": {
                        "type": "choice",
                        "options": ["x = ln(7/3) − 1", "x = 7/3 − 1", "x = ln 7 / ln 3 − 1"],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Cambio de variable en una exponencial con forma cuadrática",
                "prompt": "Resolvé 9ˣ − 12 · 3ˣ + 27 = 0 con el cambio u = 3ˣ. ¿Cuál es la MAYOR solución x? Respondé solo con el número.",
                "answer": "2: como 9ˣ = (3ˣ)², queda u² − 12u + 27 = 0 → (u − 3)(u − 9) = 0. Volviendo a x: 3ˣ = 3 → x = 1, y 3ˣ = 9 → x = 2. La mayor es x = 2 (el 9 es un valor de u, no de x).",
                "hints": ["9ˣ = (3ˣ)² = u².", "Después de hallar u todavía falta resolver 3ˣ = u."],
                "payload": {"check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Descartar valores negativos en el cambio de variable",
                "prompt": "Resolvé 4ˣ − 2ˣ − 12 = 0 con el cambio u = 2ˣ. ¿Cuáles son todas las soluciones reales?",
                "answer": "Solo x = 2: queda u² − u − 12 = 0 → (u − 4)(u + 3) = 0. De u = 4 sale 2ˣ = 4 → x = 2. En cambio u = −3 se descarta, porque 2ˣ es positivo para todo x real.",
                "hints": ["4ˣ = (2ˣ)² = u².", "Preguntate si una potencia de base 2 puede dar un resultado negativo."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["x = 4 y x = −3", "Solo x = 2", "x = 2 y x = −log₂ 3", "No tiene solución real"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ecuación logarítmica con resta de logaritmos",
                "prompt": "Resolvé log₃(x + 6) − log₃(x − 2) = 2. ¿Cuánto vale x? Respondé solo con el número.",
                "answer": "3: la resta de logaritmos es el logaritmo del cociente, log₃((x + 6)/(x − 2)) = 2 → (x + 6)/(x − 2) = 3² = 9 → x + 6 = 9x − 18 → x = 3. Verificación: los argumentos quedan 9 y 1, ambos positivos.",
                "hints": ["log A − log B = log(A/B) cuando la base es la misma.", "Pasá a forma exponencial: el cociente vale 3 elevado al número de la derecha."],
                "payload": {
                    "lab_link": "math:logarithms",
                    "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Solución extraña en una suma de logaritmos",
                "prompt": "Resolvé log(x) + log(x + 3) = 1 (logaritmos en base 10). ¿Cuál es el conjunto solución?",
                "answer": "{2}: log(x(x + 3)) = 1 → x² + 3x = 10 → (x + 5)(x − 2) = 0. Los candidatos son −5 y 2, pero x = −5 deja log(−5), que no existe en los reales: es una solución extraña. Solo vale x = 2 (log 2 + log 5 = log 10 = 1).",
                "hints": [
                    "log A + log B = log(A · B), no log(A + B).",
                    "Probá cada candidato en la ecuación ORIGINAL: todos los argumentos deben ser positivos.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["{−5, 2}", "{7/2}", "{2}", "{−5}"],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Tiempo de duplicación de precios con inflación constante",
                "prompt": "Con una inflación constante del 5% mensual, los precios siguen P(t) = P₀ · 1.05^t (t en meses). ¿Cuántos meses tardan en duplicarse? Redondeá a 1 decimal. Respondé solo con el número, en meses.",
                "answer": "14.2 meses: hay que resolver 1.05^t = 2. Aplicando ln: t · ln 1.05 = ln 2 → t = ln 2 / ln 1.05 ≈ 0.6931 / 0.04879 ≈ 14.2. No son 20 meses, porque cada aumento se calcula sobre el precio ya aumentado.",
                "hints": ["Planteá P₀ · 1.05^t = 2 · P₀ y simplificá P₀.", "Aplicá logaritmo a ambos lados para bajar la t."],
                "payload": {
                    "lab_link": "math:logarithms",
                    "check": {"type": "numeric", "value": 14.2, "tolerance": 0.005, "unit": "meses"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Comparar concentraciones con la escala de pH",
                "prompt": "El pH se define como pH = −log[H⁺], donde [H⁺] es la concentración de iones hidrógeno. El jugo de limón tiene pH 2 y el café, pH 5. ¿Cuántas veces mayor es [H⁺] en el limón que en el café? Respondé solo con el número.",
                "answer": "1000 veces: despejando, [H⁺] = 10^(−pH). Limón: 10⁻²; café: 10⁻⁵. El cociente es 10⁻² / 10⁻⁵ = 10³ = 1000. Cada unidad de pH es un factor 10.",
                "hints": ["Despejá [H⁺] = 10^(−pH) para cada bebida.", "Dividí las dos concentraciones restando los exponentes."],
                "payload": {"check": {"type": "numeric", "value": 1000, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    # ==================== INECUACIONES AVANZADAS ====================
    {
        "slug": "a2-inecuaciones-avanzadas",
        "title": "Inecuaciones cuadráticas, racionales y con valor absoluto",
        "summary": "Resolver inecuaciones con la tabla de signos (puntos críticos e intervalos) y expresar la solución en notación de intervalos.",
        "prerequisites": [
            "al-conjuntos-intervalos",
            "al-factorizar-cuadraticas",
            "al-valor-absoluto-partes",
            "a2-racionales-asintotas",
        ],
        "insert_after": "a2-ecuaciones-avanzadas",
        "metadata": {"section": "Álgebra 2", "lab_tab": "quadratics", "est_minutes": 30},
        "items": [
            {
                "item_type": "recall",
                "title": "Contar los intervalos de una tabla de signos",
                "prompt": "Para resolver (x − 1)(x + 4)/(x − 3) > 0 con la tabla de signos, los puntos críticos dividen la recta real en intervalos. ¿Cuántos intervalos hay que analizar? Respondé solo con el número.",
                "answer": "4: los puntos críticos son los ceros del numerador (x = 1 y x = −4) y el del denominador (x = 3). Tres puntos cortan la recta en cuatro intervalos: (−∞, −4), (−4, 1), (1, 3) y (3, +∞).",
                "hints": [
                    "Los puntos críticos son los ceros del numerador Y los del denominador.",
                    "Si marcás n puntos distintos en una recta, quedan n + 1 tramos.",
                ],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Resolver una inecuación cuadrática con menor estricto",
                "prompt": "¿Cuál es el conjunto solución de x² − 5x + 6 < 0?",
                "answer": "(2, 3): x² − 5x + 6 = (x − 2)(x − 3). El producto es negativo cuando los factores tienen signos opuestos, y eso pasa entre las raíces (probá x = 2.5: 0.5 · (−0.5) < 0). Como la desigualdad es estricta, 2 y 3 no entran.",
                "hints": ["Factorizá y marcá las raíces en la recta.", "Probá un número de cada intervalo para ver el signo del producto."],
                "payload": {
                    "lab_link": "math:quadratics",
                    "check": {
                        "type": "choice",
                        "options": ["(−∞, 2) ∪ (3, +∞)", "[2, 3]", "(2, 3)", "(−∞, 2)"],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Resolver x² > 9 sin perder la rama negativa",
                "prompt": "¿Cuál es el conjunto solución de x² > 9?",
                "answer": "(−∞, −3) ∪ (3, +∞): x² − 9 > 0 → (x − 3)(x + 3) > 0, que es positivo fuera de las raíces. Sacar raíz y escribir solo x > 3 pierde los negativos: por ejemplo (−4)² = 16 > 9. Es lo mismo que |x| > 3.",
                "hints": ["Pasá el 9 restando y factorizá como diferencia de cuadrados.", "Probá x = −4: fijate si cumple."],
                "payload": {
                    "lab_link": "math:quadratics",
                    "check": {
                        "type": "choice",
                        "options": ["(3, +∞)", "(−3, 3)", "(−∞, −3] ∪ [3, +∞)", "(−∞, −3) ∪ (3, +∞)"],
                        "correct": 3,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Contar los enteros que cumplen una inecuación cuadrática",
                "prompt": "¿Cuántos números enteros cumplen x² − 2x − 8 ≤ 0? Respondé solo con el número.",
                "answer": "7: x² − 2x − 8 = (x − 4)(x + 2), que es ≤ 0 entre las raíces, incluyéndolas: [−2, 4]. Los enteros son −2, −1, 0, 1, 2, 3 y 4.",
                "hints": [
                    "Factorizá: buscá dos números que multiplicados den −8 y sumados −2.",
                    "Con ≤ los extremos también cuentan.",
                ],
                "payload": {
                    "lab_link": "math:quadratics",
                    "check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Inecuación racional con ≥: qué extremos entran",
                "prompt": "¿Cuál es el conjunto solución de (x − 1)/(x + 2) ≥ 0?",
                "answer": "(−∞, −2) ∪ [1, +∞): los puntos críticos son −2 y 1. El cociente es positivo si x < −2 (negativo sobre negativo) o si x > 1 (positivo sobre positivo), y negativo entre ambos. x = 1 entra porque da 0, pero x = −2 no puede entrar porque anula el denominador.",
                "hints": [
                    "Armá la tabla de signos con el cero del numerador y el del denominador.",
                    "Fijate qué pasa con la expresión en el valor que anula el denominador.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(−∞, −2] ∪ [1, +∞)", "[1, +∞)", "(−2, 1]", "(−∞, −2) ∪ [1, +∞)"],
                        "correct": 3,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Inecuación racional comparada con 1",
                "prompt": "¿Cuál es el conjunto solución de (2x − 1)/(x − 4) < 1?",
                "answer": "(−3, 4): no se puede multiplicar por (x − 4) porque su signo depende de x. Se pasa el 1 restando: (2x − 1)/(x − 4) − 1 = (x + 3)/(x − 4) < 0. El cociente es negativo entre los puntos críticos −3 y 4, ambos excluidos. Multiplicar directamente daría x < −3, que es falso: con x = −5 la expresión vale 11/9, que es mayor que 1.",
                "hints": [
                    "Pasá el 1 al otro lado y restá con denominador común.",
                    "Te queda un solo cociente comparado con 0: ahí va la tabla de signos.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(−∞, −3)", "(−3, 4)", "(−∞, −3) ∪ (4, +∞)", "(−3, 4]"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Valor absoluto mayor o igual que un número",
                "prompt": "¿Cuál es el conjunto solución de |x + 1| ≥ 4?",
                "answer": "(−∞, −5] ∪ [3, +∞): |x + 1| es la distancia de x a −1. Que sea al menos 4 significa x + 1 ≥ 4 (x ≥ 3) o x + 1 ≤ −4 (x ≤ −5). El centro es −1, no 1.",
                "hints": ["|A| ≥ r (con r > 0) se separa en A ≥ r o A ≤ −r.", "|x + 1| = |x − (−1)|: es la distancia al punto −1."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["[−5, 3]", "(−∞, −5] ∪ [3, +∞)", "(−∞, −3] ∪ [5, +∞)", "[3, +∞)"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Escribir un intervalo como |x − a| < r",
                "prompt": "El intervalo (−2, 8) se puede escribir como |x − a| < r. ¿Cuánto vale r? Respondé solo con el número.",
                "answer": "5: a es el punto medio, a = (−2 + 8)/2 = 3, y r es la distancia del centro a cada extremo: 8 − 3 = 5 (la mitad de la longitud, que es 10). Queda |x − 3| < 5.",
                "hints": ["a es el centro del intervalo (el promedio de los extremos).", "r es la distancia del centro a cualquiera de los extremos."],
                "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""}},
            },
        ],
    },
]


ALGEBRA_INGRESO_LESSONS: dict[str, dict] = {
    "al-conjuntos-intervalos": {
        "hook": {
            "question": "En un tramo de autopista los carteles marcan mínima 65 km/h y máxima 130 km/h. ¿Cuántas velocidades permitidas hay?",
            "intuition": "Infinitas: no solo 65, 66, 67…, también 87.5 o 100.25. Para nombrar de un saque a todos esos números se usa un **intervalo**: `[65, 130]`. Dos extremos y un par de corchetes alcanzan para describir infinitos números reales.",
        },
        "concept": {
            "points": [
                "**Conjuntos numéricos**: `ℕ` naturales (1, 2, 3, …; algunas cátedras incluyen el 0), `ℤ` enteros (suman el 0 y los negativos), `ℚ` racionales (cocientes `a/b` de enteros con `b ≠ 0`: su decimal es finito o periódico). Los **irracionales** tienen decimal infinito no periódico (`√2`, `π`). `ℝ` reúne racionales e irracionales, y vale `ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ`.",
                "**Intervalos acotados**: `(a, b)` abierto es `a < x < b`; `[a, b]` cerrado es `a ≤ x ≤ b`; los semiabiertos `[a, b)` y `(a, b]` incluyen un solo extremo. **Corchete** = el extremo entra (`≤`, `≥`, punto lleno en la recta); **paréntesis** = no entra (`<`, `>`, punto vacío).",
                "**Intervalos infinitos**: `x ≥ a` es `[a, +∞)` y `x < b` es `(−∞, b)`. Como `∞` no es un número, siempre lleva paréntesis. Toda la recta es `ℝ = (−∞, +∞)`.",
                "**Intersección** `A ∩ B`: los números que están en los dos conjuntos a la vez (\"y\"). **Unión** `A ∪ B`: los que están en al menos uno (\"o\"). Dibujar ambos intervalos en la recta numérica evita casi todos los errores.",
                "**Pertenencia**: `x ∈ A` se lee \"x pertenece a A\". Por ejemplo `3 ∈ [3, 5)` pero `5 ∉ [3, 5)`.",
            ],
            "real_world": [
                {
                    "title": "Cadena de frío de las vacunas",
                    "detail": "Una heladera de vacunatorio tiene que mantenerse en `[2, 8]` °C: los dos extremos están permitidos y cualquier valor intermedio también.",
                },
                {
                    "title": "Escalas y tramos de tarifas",
                    "detail": "Los cuadros tarifarios de luz o las escalas de un impuesto usan tramos semiabiertos como `[0, 150)` y `[150, 400)`: así cada consumo cae en un único tramo, sin superponerse en el borde.",
                },
                {
                    "title": "Dominio de funciones en ingeniería",
                    "detail": "`√(x − 2)` solo existe en los reales para `x ∈ [2, +∞)`. En Análisis, el dominio y la solución de una inecuación se informan siempre como intervalos.",
                },
            ],
            "key_rule": "Corchete = el extremo entra (≤, ≥) | Paréntesis = no entra (<, >) | ±∞ siempre con paréntesis | ∩ = \"y\" (están en los dos) | ∪ = \"o\" (están en alguno).",
            "pitfall": "Ponerle corchete al infinito (`[3, +∞]`) o escribir los extremos al revés (`(5, 2)`): el menor va siempre a la izquierda, y `∞` nunca se incluye.",
        },
        "example": {
            "title": "Escribir −1 ≤ x < 4 como intervalo y combinarlo con (2, +∞)",
            "steps": [
                "El `≤` del lado de `−1` indica que `−1` entra (corchete); el `<` del lado de `4` indica que `4` no entra (paréntesis): `A = [−1, 4)`.",
                "En la recta: punto lleno en `−1`, punto vacío en `4` y el tramo entre ambos pintado. Para `B = (2, +∞)`: punto vacío en `2` y una flecha hacia la derecha.",
                "**Intersección** (donde se pisan los dos dibujos): hay que cumplir `x > 2` y `x < 4` a la vez → `A ∩ B = (2, 4)`.",
                "**Unión** (todo lo pintado por alguno): arranca en `−1`, que pertenece a `A`, y no termina → `A ∪ B = [−1, +∞)`.",
            ],
            "lab_link": "math:linear_eq",
            "lab_cta": "Practicar desigualdades",
        },
        "check": {
            "question": "¿Qué intervalo representa a `x > −2`?",
            "options": [
                {"text": "`[−2, +∞)`", "ok": False, "feedback": "El corchete incluiría al −2, pero la desigualdad es estricta (>): −2 no cumple −2 > −2."},
                {"text": "`(−2, +∞)`", "ok": True, "feedback": "Exacto: −2 no entra (paréntesis) y el intervalo sigue hacia la derecha sin fin."},
                {"text": "`(−∞, −2)`", "ok": False, "feedback": "Esos son los números MENORES que −2 (x < −2): quedó para el lado contrario."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál de estos números es racional?",
                "options": [
                    {"text": "`0.1666…` (el 6 se repite sin fin)", "ok": True, "feedback": "Exacto: es periódico y vale 1/6, un cociente de enteros."},
                    {"text": "`√5`", "ok": False, "feedback": "5 no es un cuadrado perfecto, así que √5 tiene decimal infinito no periódico: es irracional."},
                    {"text": "`π/2`", "ok": False, "feedback": "Dividir un irracional por 2 da otro irracional: si π/2 fuera una fracción, π también lo sería."},
                ],
            },
            {
                "question": "¿Cuánto da `[0, 5] ∩ (3, 8)`?",
                "options": [
                    {"text": "`[0, 8)`", "ok": False, "feedback": "Eso es la unión (todo lo que está en alguno de los dos). La intersección pide estar en los dos a la vez."},
                    {"text": "`(3, 5)`", "ok": False, "feedback": "El 5 sí entra: pertenece a [0, 5] (extremo cerrado) y también a (3, 8), porque 3 < 5 < 8."},
                    {"text": "`(3, 5]`", "ok": True, "feedback": "Exacto: hay que cumplir x > 3 y x ≤ 5. El 3 queda afuera (no está en el segundo) y el 5 entra (está en los dos)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras por qué `+∞` siempre lleva paréntesis y cuál es la diferencia entre `A ∩ B` y `A ∪ B`.",
    },
    "a2-expresiones-racionales": {
        "hook": {
            "question": "¿Se puede \"tachar\" la x en `(x + 6)/(x + 2)` y decir que da `6/2 = 3`?",
            "intuition": "No. Probá con `x = 1`: da `7/3`, no `3`. Solo se pueden cancelar **factores** (cosas que multiplican a todo el numerador y a todo el denominador), nunca términos que están sumando. Por eso el primer paso con una expresión racional es siempre **factorizar**.",
        },
        "concept": {
            "points": [
                "Una **expresión racional** es un cociente de polinomios `P(x)/Q(x)`. Su dominio excluye los valores que anulan a `Q`.",
                "**Simplificar**: factorizá numerador y denominador y cancelá los factores comunes. La restricción del factor cancelado se conserva: `(x² − 9)/(x − 3) = x + 3` solo para `x ≠ 3`.",
                "**Multiplicar**: numerador por numerador y denominador por denominador (conviene factorizar y cancelar antes). **Dividir**: multiplicar por la recíproca de la segunda fracción.",
                "**Sumar y restar**: el denominador común es el **mcm** de los denominadores (cada factor distinto, con su mayor exponente). Se amplifica cada fracción y se operan los numeradores. En una **fracción compleja**, primero se une cada piso en una sola fracción y después se divide.",
                "**Racionalizar**: si abajo hay `√a`, se multiplica arriba y abajo por `√a`. Si hay un binomio `a ± √b`, se multiplica por su **conjugado**: `(a − √b)(a + √b) = a² − b`, sin raíces.",
            ],
            "real_world": [
                {
                    "title": "Resistencias en paralelo",
                    "detail": "De `1/R = 1/R₁ + 1/R₂` sale, sumando fracciones con denominador común, `R = R₁·R₂/(R₁ + R₂)`: es la cuenta de todos los días en electrotecnia.",
                },
                {
                    "title": "Velocidad media de un viaje de ida y vuelta",
                    "detail": "Si vas a `v₁` y volvés a `v₂` por la misma ruta, la velocidad media es `2d/(d/v₁ + d/v₂) = 2·v₁·v₂/(v₁ + v₂)`: una fracción compleja simplificada.",
                },
                {
                    "title": "Límites en Análisis Matemático",
                    "detail": "Las indeterminaciones `0/0` se resuelven con estas dos herramientas: factorizar y cancelar, o multiplicar por el conjugado cuando hay raíces.",
                },
            ],
            "key_rule": "Factorizar primero | Solo se cancelan factores, nunca términos | Dividir = multiplicar por la recíproca | Sumar: mcm de los denominadores | Conjugado: (a − √b)(a + √b) = a² − b.",
            "pitfall": "Sumar \"derecho\": `1/a + 1/b` NO es `2/(a + b)`. Y al simplificar, olvidarse de que el valor que anulaba el factor cancelado sigue prohibido.",
        },
        "example": {
            "title": "Restar x/(x − 2) − 8/(x² − 4) y simplificar",
            "steps": [
                "Factorizamos los denominadores: `x² − 4 = (x − 2)(x + 2)`. El mcm es `(x − 2)(x + 2)`, con `x ≠ 2` y `x ≠ −2`.",
                "Amplificamos la primera fracción por `(x + 2)`: `x(x + 2)/((x − 2)(x + 2))`. La segunda ya tiene el denominador común.",
                "Restamos numeradores: `x(x + 2) − 8 = x² + 2x − 8 = (x + 4)(x − 2)`.",
                "Cancelamos el factor `(x − 2)`: queda `(x + 4)/(x + 2)`, válido para `x ≠ 2` y `x ≠ −2`.",
            ],
            "lab_link": "math:factoring",
            "lab_cta": "Practicar factorización",
        },
        "check": {
            "question": "¿Cuál es la forma simplificada de `(x² − 4)/(x − 2)`?",
            "options": [
                {"text": "`x − 2`", "ok": False, "feedback": "x² − 4 = (x − 2)(x + 2): al cancelar (x − 2) con el denominador, el factor que queda es x + 2."},
                {"text": "`x + 2`, para todo x real", "ok": False, "feedback": "En x = 2 la expresión original da 0/0 y no está definida: la restricción x ≠ 2 se conserva después de cancelar."},
                {"text": "`x + 2`, con `x ≠ 2`", "ok": True, "feedback": "Exacto: (x − 2)(x + 2)/(x − 2) = x + 2, pero x = 2 sigue excluido."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuánto da `1/x + 1/(x + 1)`?",
                "options": [
                    {"text": "`(2x + 1)/(x(x + 1))`", "ok": True, "feedback": "Exacto: con denominador común x(x + 1), el numerador es (x + 1) + x = 2x + 1."},
                    {"text": "`2/(2x + 1)`", "ok": False, "feedback": "Sumaste numerador con numerador y denominador con denominador. Con x = 1 da 2/3, pero la suma real es 1 + 1/2 = 3/2."},
                    {"text": "`1/(x(x + 1))`", "ok": False, "feedback": "Pusiste bien el denominador común, pero faltó amplificar los numeradores: son (x + 1) + x, no 1."},
                ],
            },
            {
                "question": "Para racionalizar `3/(√7 + 2)`, ¿por qué expresión multiplicás arriba y abajo?",
                "options": [
                    {"text": "`√7 + 2`", "ok": False, "feedback": "(√7 + 2)² = 11 + 4√7: la raíz sigue en el denominador por el doble producto."},
                    {"text": "`√7 − 2`", "ok": True, "feedback": "Exacto: es el conjugado, y (√7 + 2)(√7 − 2) = 7 − 4 = 3, sin raíces."},
                    {"text": "`√7`", "ok": False, "feedback": "√7 · (√7 + 2) = 7 + 2√7: multiplicar por √7 solo sirve cuando el denominador es un único término."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué en `(x + 6)/(x + 2)` no se puede cancelar la `x`, pero en `x(x + 6)/(x(x + 2))` sí (y con qué restricción).",
    },
    "a2-raices-racionales-factorizacion": {
        "hook": {
            "question": "Para resolver `x³ − 4x² + x + 6 = 0` no hay una fórmula cómoda como la resolvente. ¿Hay que probar números al azar?",
            "intuition": "Al azar no. Si los coeficientes son enteros, toda raíz racional sale de una lista corta: divisores del término independiente sobre divisores del coeficiente principal. Acá los únicos candidatos son `±1, ±2, ±3, ±6`. Cuando encontrás una raíz, Ruffini baja el grado y lo que queda es una cuadrática.",
        },
        "concept": {
            "points": [
                "**Teorema de las raíces racionales (Gauss)**: si `P` tiene coeficientes enteros y `p/q` (fracción irreducible) es raíz, entonces `p` divide al término independiente y `q` divide al coeficiente principal. Da una lista de **candidatos**; no garantiza que alguno sea raíz (las raíces pueden ser irracionales o complejas).",
                "**Probar un candidato**: por el teorema del resto, `c` es raíz ⇔ `P(c) = 0` ⇔ `(x − c)` es factor de `P`.",
                "**Bajar el grado**: dividiendo por `(x − c)` con Ruffini queda `P(x) = (x − c)·Q(x)`, con `Q` de un grado menor. Se repite hasta llegar a una cuadrática, que se resuelve con la resolvente.",
                "**Factorización completa**: `P(x) = a(x − r₁)(x − r₂)…`, sin olvidar el coeficiente principal `a`. Si una raíz vuelve a anular al cociente es **múltiple** y su factor aparece repetido: `(x − r)²`.",
                "Un polinomio de grado `n` tiene **como máximo `n` raíces reales**. Los de grado impar tienen al menos una; los de grado par pueden no tener ninguna. Un factor cuadrático con `Δ < 0` no se puede seguir factorizando en `ℝ`.",
            ],
            "real_world": [
                {
                    "title": "Estabilidad de sistemas de control",
                    "detail": "Que un motor o un piloto automático sea estable depende de las raíces de su polinomio característico: factorizarlo es el primer paso del análisis.",
                },
                {
                    "title": "Dimensiones de una caja con volumen dado",
                    "detail": "Si recortás esquinas de lado `x` a una plancha de 10 × 16 cm y querés un volumen de 144 cm³, tenés que resolver `x(10 − 2x)(16 − 2x) = 144`, una cúbica con raíz entera `x = 2`.",
                },
                {
                    "title": "Autovalores en Álgebra Lineal",
                    "detail": "Los autovalores de una matriz 3 × 3 (que describen, por ejemplo, los modos de vibración de una estructura) son las raíces de un polinomio de grado 3: en los ejercicios se factoriza con Gauss y Ruffini.",
                },
            ],
            "key_rule": "Candidatos: ± (divisores del término independiente) / (divisores del coeficiente principal) | P(c) = 0 ⇔ (x − c) es factor | Ruffini baja un grado | Grado n → a lo sumo n raíces reales.",
            "pitfall": "Invertir la fracción de candidatos (los divisores del coeficiente principal van ABAJO), olvidarse de los negativos, o no volver a probar la misma raíz en el cociente (así se escapan las raíces dobles).",
        },
        "example": {
            "title": "Factorizar por completo P(x) = 2x³ − 3x² − 3x + 2",
            "steps": [
                "**Candidatos**: divisores de `2` (término independiente) sobre divisores de `2` (coeficiente principal) → `±1, ±2, ±1/2`.",
                "**Probamos**: `P(1) = 2 − 3 − 3 + 2 = −2`, no es raíz. `P(−1) = −2 − 3 + 3 + 2 = 0` → `x = −1` es raíz y `(x + 1)` es factor.",
                "**Ruffini con −1** sobre los coeficientes `2, −3, −3, 2`: da `2, −5, 2` y resto `0`. El cociente es `2x² − 5x + 2`.",
                "**Resolvente** del cociente: `x = (5 ± √(25 − 16))/4 = (5 ± 3)/4` → `x = 2` y `x = 1/2`.",
                "**Factorización completa**: `P(x) = 2(x + 1)(x − 2)(x − 1/2) = (x + 1)(x − 2)(2x − 1)`.",
            ],
            "lab_link": "math:polynomials",
            "lab_cta": "Practicar polinomios",
        },
        "check": {
            "question": "¿Cuáles son los candidatos a raíz racional de `x³ + 2x² − 5x − 6`?",
            "options": [
                {"text": "`1, 2, 3, 6`", "ok": False, "feedback": "Faltan los negativos: cada divisor vale con los dos signos. De hecho x = −1 es raíz: −1 + 2 + 5 − 6 = 0."},
                {"text": "`±1, ±2, ±3, ±6`", "ok": True, "feedback": "Exacto: divisores de 6 (con ambos signos) sobre divisores de 1."},
                {"text": "`±1, ±1/2, ±1/3, ±1/6`", "ok": False, "feedback": "Invertiste la fracción: los divisores del término independiente (6) van arriba y los del coeficiente principal (1) abajo."},
            ],
        },
        "checks": [
            {
                "question": "Dividís `P(x)` por `(x − 2)` con Ruffini y el resto da `0`. ¿Qué podés afirmar?",
                "options": [
                    {"text": "`x = 2` es raíz de `P` y `(x − 2)` es uno de sus factores", "ok": True, "feedback": "Exacto: el resto es P(2), y si vale 0 entonces P(x) = (x − 2)·Q(x)."},
                    {"text": "`x = −2` es raíz de `P`", "ok": False, "feedback": "Error de signo: el divisor (x − 2) se anula en x = 2, y el resto es P(2), no P(−2)."},
                    {"text": "`P(x)` tiene grado 2", "ok": False, "feedback": "El resto no dice nada sobre el grado de P. Lo que tiene un grado menos que P es el cociente."},
                ],
            },
            {
                "question": "`P(x) = (x − 1)²(x + 3)`. ¿Cuáles son sus raíces reales?",
                "options": [
                    {"text": "Tres raíces distintas: `1`, `−1` y `−3`", "ok": False, "feedback": "(x − 1)² es (x − 1)(x − 1), no (x − 1)(x + 1): la raíz 1 aparece dos veces y −1 no es raíz (P(−1) = 4 · 2 = 8)."},
                    {"text": "`−1` (doble) y `3` (simple)", "ok": False, "feedback": "Signos invertidos: el factor (x − 1) se anula en x = 1 y el factor (x + 3) en x = −3."},
                    {"text": "`1` (doble) y `−3` (simple)", "ok": True, "feedback": "Exacto: grado 3 = 2 + 1 contando multiplicidades, pero solo hay dos raíces distintas."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué el teorema de Gauss da una lista de candidatos pero no asegura que alguno sea raíz, y qué hacés una vez que encontrás la primera.",
    },
    "a2-ecuaciones-exponenciales-logaritmicas": {
        "hook": {
            "question": "Si los precios suben 5% por mes, ¿tardan 20 meses en duplicarse (porque 20 × 5% = 100%)?",
            "intuition": "Tardan bastante menos: unos 14 meses. Cada aumento se aplica sobre el precio ya aumentado, así que la cuenta es `1.05ᵗ = 2`. La incógnita quedó en el exponente, y la única herramienta que la baja de ahí es el logaritmo: `t = ln 2 / ln 1.05 ≈ 14.2`.",
        },
        "concept": {
            "points": [
                "**Igualar bases**: si los dos lados se pueden escribir como potencias de la misma base `a` (con `a > 0`, `a ≠ 1`), entonces `aᵘ = aᵛ` implica `u = v`. Ejemplo: `4ˣ = 8` → `2²ˣ = 2³` → `x = 3/2`.",
                "**Aplicar logaritmo**: si no hay base común, `aˣ = b` (con `b > 0`) se resuelve tomando logaritmo de los dos lados: `x·ln a = ln b` → `x = ln b / ln a`.",
                "**Cambio de variable**: en `4ˣ − 5·2ˣ + 4 = 0`, como `4ˣ = (2ˣ)²`, con `u = 2ˣ` queda una cuadrática. Como `u = 2ˣ > 0`, los valores de `u` negativos o nulos se descartan.",
                "**Ecuaciones logarítmicas**: se juntan los logaritmos con las propiedades, se pasa a forma exponencial (`logₐ M = c` ⇔ `M = aᶜ`) y se **verifica** cada candidato en la ecuación original: todos los argumentos deben quedar positivos. Los que no cumplen son **soluciones extrañas**.",
            ],
            "real_world": [
                {
                    "title": "Inflación e interés compuesto",
                    "detail": "El tiempo de duplicación de un precio o de un plazo fijo sale de `(1 + i)ᵗ = 2` → `t = ln 2 / ln(1 + i)`.",
                },
                {
                    "title": "Escala de pH en química",
                    "detail": "`pH = −log[H⁺]`: para saber la concentración a partir del pH se resuelve una ecuación logarítmica, `[H⁺] = 10^(−pH)`. Cada unidad de pH es un factor 10.",
                },
                {
                    "title": "Decibeles en acústica",
                    "detail": "El nivel sonoro es `β = 10·log(I/I₀)`. Despejar la intensidad `I` de un recital de 110 dB es resolver una ecuación logarítmica: `I = I₀·10¹¹`.",
                },
            ],
            "key_rule": "aᵘ = aᵛ ⇒ u = v | aˣ = b ⇒ x = ln b / ln a | logₐ M = c ⇔ M = aᶜ | En ecuaciones logarítmicas, verificar siempre que los argumentos queden positivos.",
            "pitfall": "Creer que `ln 12 / ln 5` es `ln(12/5)`: el cociente de logaritmos NO es el logaritmo del cociente. Y quedarse con candidatos que dejan un logaritmo con argumento negativo.",
        },
        "example": {
            "title": "Resolver 4ˣ − 5·2ˣ + 4 = 0 con cambio de variable",
            "steps": [
                "Reescribimos `4ˣ = (2²)ˣ = (2ˣ)²` y llamamos `u = 2ˣ` (con `u > 0`).",
                "La ecuación queda `u² − 5u + 4 = 0` → `(u − 1)(u − 4) = 0` → `u = 1` o `u = 4`. Los dos son positivos, así que sirven.",
                "Volvemos a `x`: `2ˣ = 1` → `x = 0`; `2ˣ = 4` → `x = 2`.",
                "Verificamos: con `x = 0`, `1 − 5 + 4 = 0` ✓; con `x = 2`, `16 − 20 + 4 = 0` ✓.",
            ],
            "lab_link": "math:logarithms",
            "lab_cta": "Practicar logaritmos",
        },
        "check": {
            "question": "¿Cuál es la solución de `2^(x + 3) = 32`?",
            "options": [
                {"text": "`x = 5`", "ok": False, "feedback": "5 es el exponente completo (32 = 2⁵). Falta igualar x + 3 = 5 y despejar."},
                {"text": "`x = 2`", "ok": True, "feedback": "Exacto: 32 = 2⁵, entonces x + 3 = 5 y x = 2."},
                {"text": "`x = 13`", "ok": False, "feedback": "Dividiste 32 por 2 y restaste 3, como si fuera 2·(x + 3) = 32. La incógnita está en el exponente: hay que igualar bases."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál es la solución exacta de `3ˣ = 10`?",
                "options": [
                    {"text": "`x = ln(10/3)`", "ok": False, "feedback": "Confundiste cociente de logaritmos con logaritmo del cociente: ln(10/3) ≈ 1.20, y 3 elevado a ese número da apenas 3.75, no 10."},
                    {"text": "`x = 10/3`", "ok": False, "feedback": "Dividir no deshace una potencia: 3^(10/3) ≈ 38.9, no 10. Hace falta un logaritmo."},
                    {"text": "`x = ln 10 / ln 3`", "ok": True, "feedback": "Exacto: x · ln 3 = ln 10, y vale aproximadamente 2.096."},
                ],
            },
            {
                "question": "Al resolver `log₂(x) + log₂(x − 6) = 4` llegás a `x² − 6x − 16 = 0`, con raíces `8` y `−2`. ¿Cuál es la solución de la ecuación original?",
                "options": [
                    {"text": "Solo `x = 8`", "ok": True, "feedback": "Exacto: log₂ 8 + log₂ 2 = 3 + 1 = 4. Con x = −2 los argumentos serían negativos."},
                    {"text": "`x = 8` y `x = −2`", "ok": False, "feedback": "x = −2 cumple la cuadrática pero no la ecuación original: log₂(−2) no existe en los reales. Es una solución extraña."},
                    {"text": "Solo `x = −2`", "ok": False, "feedback": "Quedó al revés: −2 es la que se descarta (argumentos −2 y −8, negativos) y 8 es la que verifica."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué en una ecuación logarítmica hay que verificar los candidatos en la ecuación original, y por qué en el cambio `u = 2ˣ` se descartan los valores negativos de `u`.",
    },
    "a2-inecuaciones-avanzadas": {
        "hook": {
            "question": "Para resolver `(x + 1)/(x − 2) > 0`, ¿podés \"pasar multiplicando\" el `x − 2` como hacés en una ecuación?",
            "intuition": "No sin saber su signo. Si `x − 2` es negativo, multiplicar da vuelta la desigualdad; si es positivo, no. Y el signo depende justamente de la `x` que estás buscando. La salida es otra: estudiar el signo de cada factor por separado en una **tabla de signos**.",
        },
        "concept": {
            "points": [
                "**Método de la tabla de signos**: 1) dejá todo de un lado y `0` del otro; 2) factorizá; 3) marcá los **puntos críticos** (ceros del numerador y del denominador); 4) en cada intervalo que queda el signo no cambia: probá un valor o multiplicá los signos de los factores; 5) elegí los intervalos que cumplen la desigualdad.",
                "**Cuadráticas**: si `a > 0` y hay dos raíces reales distintas, `a(x − r₁)(x − r₂)` es negativo entre las raíces y positivo afuera (con `a < 0` se invierte). Por eso `x² > 9` es `(−∞, −3) ∪ (3, +∞)` y no solamente `x > 3`.",
                "**Racionales**: nunca multipliques por un denominador que tiene `x` sin conocer su signo. Pasá todo a un lado y operá con denominador común. Los ceros del denominador **no se incluyen** en la solución (siempre paréntesis), aunque la desigualdad sea `≤` o `≥`.",
                "**Valor absoluto** (con `r > 0`): `|x − a| < r` dice \"la distancia de x a `a` es menor que `r`\" → `(a − r, a + r)`. `|x − a| > r` dice \"x está lejos de `a`\" → `(−∞, a − r) ∪ (a + r, +∞)`.",
                "**Extremos**: con `≤` o `≥` los ceros del numerador entran (corchete); con `<` o `>` no entran (paréntesis).",
            ],
            "real_world": [
                {
                    "title": "Tolerancias de fabricación",
                    "detail": "Un eje de 20 mm con tolerancia de 0.05 mm se especifica como `|d − 20| ≤ 0.05`, es decir `d ∈ [19.95, 20.05]`.",
                },
                {
                    "title": "Tiempo por encima de una altura",
                    "detail": "Una pelota con altura `h(t) = −5t² + 20t` está a más de 15 m cuando `−5t² + 20t > 15`, que es una inecuación cuadrática con solución `t ∈ (1, 3)` segundos.",
                },
                {
                    "title": "Dominios en Análisis Matemático",
                    "detail": "Para saber dónde existe `√((x − 1)/(x + 2))` hay que resolver la inecuación racional `(x − 1)/(x + 2) ≥ 0`. Es un clásico de los parciales de ingreso.",
                },
            ],
            "key_rule": "Todo de un lado → factorizar → puntos críticos → tabla de signos | El cero del denominador no se incluye | |x − a| < r ⇔ a − r < x < a + r | |x − a| > r ⇔ x < a − r o x > a + r.",
            "pitfall": "Multiplicar por un denominador con `x` como si fuera positivo, o resolver `x² > 9` sacando raíz como `x > 3` (se pierde toda la rama `x < −3`).",
        },
        "example": {
            "title": "Resolver (x + 1)/(x − 2) ≥ 0 con tabla de signos",
            "steps": [
                "Ya está comparado con `0`. **Puntos críticos**: `x = −1` (anula el numerador) y `x = 2` (anula el denominador).",
                "Esos dos puntos parten la recta en tres intervalos: `(−∞, −1)`, `(−1, 2)` y `(2, +∞)`.",
                "Probamos un valor en cada uno: `x = −2` → `(−)/(−) = +`; `x = 0` → `(+)/(−) = −`; `x = 3` → `(+)/(+) = +`.",
                "Buscamos `≥ 0`: sirven los intervalos con `+`, más `x = −1` (ahí el cociente vale `0`). `x = 2` queda afuera porque anula el denominador.",
                "**Solución**: `(−∞, −1] ∪ (2, +∞)`.",
            ],
            "lab_link": "math:quadratics",
            "lab_cta": "Practicar cuadráticas",
        },
        "check": {
            "question": "¿Cuál es la solución de `(x − 1)(x − 4) < 0`?",
            "options": [
                {"text": "`(−∞, 1) ∪ (4, +∞)`", "ok": False, "feedback": "Ahí el producto es positivo: con x = 0 da (−1)(−4) = 4 > 0. Esa es la solución de > 0."},
                {"text": "`(1, 4)`", "ok": True, "feedback": "Exacto: entre las raíces un factor es positivo y el otro negativo (con x = 2: 1 · (−2) = −2 < 0)."},
                {"text": "`(−∞, 1)`", "ok": False, "feedback": "Pediste que los dos factores sean negativos (x < 1 y x < 4), pero negativo por negativo da positivo."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál es la solución de `|x − 2| < 3`?",
                "options": [
                    {"text": "`(−1, 5)`", "ok": True, "feedback": "Exacto: −3 < x − 2 < 3 → −1 < x < 5 (centro 2, radio 3)."},
                    {"text": "`(−∞, 5)`", "ok": False, "feedback": "Resolviste solo x − 2 < 3. Falta la otra mitad: x − 2 > −3, o sea x > −1."},
                    {"text": "`(−5, 1)`", "ok": False, "feedback": "Tomaste como centro −2: ese es el intervalo de |x + 2| < 3. |x − 2| mide la distancia a 2: de 2 − 3 a 2 + 3."},
                ],
            },
            {
                "question": "¿Cuál es la solución de `(x − 3)/(x + 1) ≤ 0`?",
                "options": [
                    {"text": "`[−1, 3]`", "ok": False, "feedback": "x = −1 anula el denominador: ahí la expresión no existe, así que no puede incluirse aunque la desigualdad sea ≤."},
                    {"text": "`(−∞, 3]`", "ok": False, "feedback": "Multiplicaste por (x + 1) como si fuera positivo y quedó x − 3 ≤ 0. Pero para x < −1 el cociente es positivo: con x = −2 da (−5)/(−1) = 5."},
                    {"text": "`(−1, 3]`", "ok": True, "feedback": "Exacto: el cociente es negativo entre −1 y 3, vale 0 en x = 3 (entra) y no existe en x = −1 (no entra)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué en una inecuación racional no se puede multiplicar por el denominador sin conocer su signo, y por qué sus ceros no entran en la solución aunque la desigualdad sea `≤` o `≥`.",
    },
}
