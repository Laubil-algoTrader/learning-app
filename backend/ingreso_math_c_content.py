"""Temas de funciones y trigonometría del Curso de Ingreso 2027 (Ingeniería, UNCuyo).

Cuatro nodos que se intercalan en Álgebra 2 y Trigonometría mediante `insert_after`:
  - Estudio de una función: dominio, imagen, ceros, ordenada al origen, C⁺ y C⁻
  - Funciones exponencial y logarítmica: dominio, imagen, asíntotas y desplazamientos
  - Sistemas de medición de ángulos: sexagesimal y radial
  - Relaciones entre ángulos: complementarios, suplementarios, opuestos y que difieren en π o π/2

Siguen la notación del material del ingreso: intervalos con punto y coma, IR, coma decimal,
C⁺ y C⁻, "ceros", "imagen", tg, cotg, sec y cosec.
"""

from __future__ import annotations

INGRESO_MATH_C_NODES: list[dict] = [
    # ==================== ESTUDIO DE UNA FUNCIÓN ====================
    {
        "slug": "a2-estudio-funciones",
        "title": "Estudio de una función: dominio, imagen, ceros, ordenada al origen, C⁺ y C⁻",
        "summary": "Hallar el dominio de fraccionarias e irracionales, leer dominio e imagen en un gráfico, calcular ceros y ordenada al origen y armar C⁺ y C⁻ con la tabla de signos, también en funciones por partes.",
        "prerequisites": ["a2-graficas-polinomios", "a2-inecuaciones-avanzadas"],
        "insert_after": "a2-inecuaciones-avanzadas",
        "metadata": {"section": "Álgebra 2", "lab_tab": "polynomials", "est_minutes": 30},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Dominio de una fraccionaria cuyo numerador comparte un factor",
                "prompt": "¿Cuál es el dominio de f(x) = (x + 3)/(x³ − 9x)?",
                "answer": "D = IR − {−3; 0; 3}: el denominador se factoriza como x(x − 3)(x + 3) y se anula en x = 0, x = 3 y x = −3. Aunque el factor (x + 3) también esté arriba, en x = −3 la fórmula original queda 0/0, que no está definido: el dominio se calcula sobre la función tal como está dada, antes de simplificar. El numerador no excluye nada.",
                "hints": [
                    "Sacá factor común x en el denominador y después usá diferencia de cuadrados.",
                    "Se excluyen TODOS los valores que anulan el denominador original, aunque después se pueda simplificar.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["D = IR − {−3; 0; 3}", "D = IR − {0; 3}", "D = IR − {−3; 3}", "D = IR − {−3}"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Dominio con una raíz de índice par en el denominador",
                "prompt": "¿Cuál es el dominio de f(x) = 10/√(x² − 2x)?",
                "answer": "D = (−∞; 0) ∪ (2; ∞): como la raíz par está en el denominador, el radicando tiene que ser estrictamente positivo: x² − 2x > 0 → x(x − 2) > 0. Los valores críticos son 0 y 2; con elementos de prueba, x = −1 da 3 > 0, x = 1 da −1 < 0 y x = 3 da 3 > 0. Los extremos 0 y 2 no entran porque anulan el denominador.",
                "hints": [
                    "Raíz par en el denominador: radicando > 0 (no ≥ 0), porque el denominador no puede valer 0.",
                    "Factorizá x² − 2x y armá la tabla de signos con los valores que lo anulan.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(−∞; 0) ∪ (2; ∞)", "(−∞; 0] ∪ [2; ∞)", "(0; 2)", "[2; ∞)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Dominio de la raíz cuadrada de un cociente",
                "prompt": "¿Cuál es el dominio de f(x) = √((3 − x)/(x + 2))?",
                "answer": "D = (−2; 3]: hay que resolver (3 − x)/(x + 2) ≥ 0. El numerador se anula en x = 3 y el denominador en x = −2. Probando: x = −3 da −6 (negativo), x = 0 da 1,5 (positivo) y x = 4 da −1/6 (negativo). El 3 entra porque el radicando vale 0 (√0 existe), pero el −2 no, porque anula el denominador.",
                "hints": [
                    "Planteá radicando ≥ 0 y buscá los valores que anulan el numerador y el denominador.",
                    "El valor que anula el denominador nunca entra, aunque la desigualdad tenga el igual.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(−2; 3]", "[−2; 3]", "(−∞; −2) ∪ [3; ∞)", "(−2; 3)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Misma fórmula con dominio natural y dominio restringido",
                "prompt": "Sean f: IR → IR dada por f(x) = 3x² y f₁: [0; ∞) → IR dada por f₁(x) = 3x². ¿Son la misma función?",
                "answer": "No: dos funciones son iguales solo si tienen el mismo dominio y le asignan el mismo valor a cada x de ese dominio. f tiene el dominio natural IR y f₁ un dominio restringido [0; ∞), así que son funciones distintas (la gráfica de f₁ es solo la rama derecha de la parábola). Si cambia el dominio, cambia la función.",
                "hints": ["Repasá la definición de igualdad de funciones: ¿qué dos condiciones pide?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "No: tienen la misma fórmula, pero distinto dominio",
                            "Sí: tienen la misma fórmula",
                            "Sí: en [0; ∞) las dos dan los mismos valores",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Imagen y preimagen a partir de f(3) = 5",
                "prompt": "Se sabe que f(3) = 5. ¿Qué afirmación es correcta?",
                "answer": "5 es la imagen de 3 y 3 es una preimagen de 5: el punto (3; 5) está en la gráfica, la x es la preimagen y la y es la imagen. Ojo: 3 no tiene por qué ser la ÚNICA preimagen de 5, porque una función puede asignar la misma imagen a varios valores de x.",
                "hints": ["En f(a) = b, a está en el eje x y b en el eje y.", "¿Una función puede darle el mismo valor a dos x distintos?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "5 es la imagen de 3 y 3 es una preimagen de 5",
                            "5 es la preimagen de 3",
                            "3 es la imagen de 5",
                            "3 es la única preimagen de 5",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Leer dominio e imagen con extremos abierto y cerrado",
                "prompt": "La gráfica de f es un trazo continuo y siempre creciente que empieza en el punto (−2; 1), marcado con punto lleno, y termina en el punto (3; 5), marcado con punto vacío. ¿Cuáles son su dominio y su imagen?",
                "answer": "D = [−2; 3) e Im = [1; 5): el dominio se lee proyectando la gráfica sobre el eje x y la imagen proyectándola sobre el eje y. El punto lleno en (−2; 1) incluye x = −2 e y = 1 (corchete); el punto vacío en (3; 5) excluye x = 3 e y = 5 (paréntesis). Como la función es continua y creciente, toma todos los valores entre 1 y 5.",
                "hints": [
                    "Dominio: sombra sobre el eje x. Imagen: sombra sobre el eje y.",
                    "Punto lleno → corchete; punto vacío → paréntesis.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "D = [−2; 3); Im = [1; 5)",
                            "D = [1; 5); Im = [−2; 3)",
                            "D = [−2; 3]; Im = [1; 5]",
                            "D = (−2; 3); Im = (1; 5)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ceros de una fraccionaria cuando un candidato sale del dominio",
                "prompt": "¿Cuántos ceros tiene f(x) = (x² − 4)/(x − 2)? Respondé solo con el número.",
                "answer": "1: el único cero es x = −2. El numerador x² − 4 se anula en x = 2 y en x = −2, pero x = 2 anula también el denominador: no pertenece al dominio (D = IR − {2}) y por lo tanto no puede ser cero de f. Un cero tiene que cumplir f(x) = 0 y estar en el dominio.",
                "hints": [
                    "Primero hallá el dominio; después igualá la función a 0.",
                    "Revisá si algún valor que anula el numerador también anula el denominador.",
                ],
                "payload": {"check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "C⁺ y C⁻ con un cero de multiplicidad par",
                "prompt": "Usando la tabla de signos, ¿cuáles son el conjunto de positividad y el de negatividad de f(x) = ½(x − 2)²(x − 3)?",
                "answer": "C⁺ = (3; ∞) y C⁻ = (−∞; 2) ∪ (2; 3): los ceros son 2 (doble) y 3 (simple). Con elementos de prueba: f(0) = −6 < 0, f(2,5) = −0,0625 < 0 y f(4) = 2 > 0. El factor (x − 2)² nunca es negativo, así que en x = 2 la gráfica rebota y el signo no cambia. El 2 no va en C⁻ porque f(2) = 0, que no es positivo ni negativo.",
                "hints": [
                    "Los ceros parten la recta en intervalos: probá un valor de cada uno.",
                    "En un cero de multiplicidad par el signo no cambia, pero el cero igual queda afuera de C⁺ y de C⁻.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "C⁺ = (3; ∞); C⁻ = (−∞; 2) ∪ (2; 3)",
                            "C⁺ = (3; ∞); C⁻ = (−∞; 3)",
                            "C⁺ = (−∞; 2) ∪ (3; ∞); C⁻ = (2; 3)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Estudio completo de una función por partes",
                "prompt": "Sea f(x) = x² si x < 0, y f(x) = 2x + 1 si x > 0. ¿Qué afirmación es correcta?",
                "answer": "D = IR − {0} y f no tiene ceros ni ordenada al origen: ninguna de las dos condiciones incluye x = 0. El tramo x² se anularía en x = 0, que no está en su tramo, y 2x + 1 = 0 da x = −1/2, que no cumple x > 0. Además Im = (0; ∞) (x² da (0; ∞) y 2x + 1 da (1; ∞)), C⁺ = (−∞; 0) ∪ (0; ∞) y C⁻ = ∅.",
                "hints": [
                    "Cada fórmula vale solo en su tramo: todo valor que encuentres tiene que cumplir la condición de ese tramo.",
                    "¿Alguna de las condiciones incluye al 0?",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "D = IR − {0}; no tiene ceros ni ordenada al origen",
                            "Tiene un cero en x = −1/2",
                            "Su ordenada al origen es f(0) = 1",
                            "Im = [0; ∞)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Valor de la función con letras: f(a + h)",
                "prompt": "Si f(x) = x² + 2x, ¿cuánto vale f(a + h)?",
                "answer": "a² + 2ah + h² + 2a + 2h: se reemplaza cada x por (a + h) entre paréntesis → (a + h)² + 2(a + h) = a² + 2ah + h² + 2a + 2h. El cuadrado de un binomio tiene el doble producto 2ah, y el 2 multiplica a los dos términos del paréntesis.",
                "hints": [
                    "Escribí f((a + h)) poniendo el paréntesis en cada lugar donde estaba la x.",
                    "(a + h)² = a² + 2ah + h², no a² + h².",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "a² + 2ah + h² + 2a + 2h",
                            "a² + h² + 2a + 2h",
                            "a² + 2a + h",
                            "a² + 2ah + h² + 2a + h",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== FUNCIONES EXPONENCIAL Y LOGARÍTMICA ====================
    {
        "slug": "a2-graficas-exp-log",
        "title": "Funciones exponencial y logarítmica: dominio, imagen, asíntotas y desplazamientos",
        "summary": "Completar el cuadro de una exponencial k·a^(x − h) + v o de una logarítmica log_a(x − h) + v: dominio, imagen, asíntota, cero, ordenada al origen, C⁺, C⁻ y crecimiento, con reflexiones y la relación inversa entre ambas.",
        "prerequisites": ["a2-ecuaciones-exponenciales-logaritmicas"],
        "insert_after": "a2-ecuaciones-exponenciales-logaritmicas",
        "metadata": {"section": "Álgebra 2", "lab_tab": "logarithms", "est_minutes": 30},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Imagen y asíntota de una exponencial desplazada hacia abajo",
                "prompt": "Completá el cuadro de y = 2ˣ − 4: ¿cuáles son su imagen y la ecuación de su asíntota?",
                "answer": "Im = (−4; ∞) y asíntota y = −4: la gráfica de 2ˣ (imagen (0; ∞), asíntota y = 0) baja 4 unidades, y con ella baja la asíntota. La función se acerca a −4 sin tocarlo, así que −4 no pertenece a la imagen (paréntesis). La asíntota de una exponencial es horizontal: su ecuación es y = número.",
                "hints": [
                    "Partí de y = 2ˣ y fijate qué le hace el −4 a toda la gráfica.",
                    "La asíntota horizontal se mueve junto con la gráfica.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Im = (−4; ∞); asíntota y = −4",
                            "Im = (0; ∞); asíntota y = 0",
                            "Im = (−4; ∞); asíntota x = −4",
                            "Im = [−4; ∞); asíntota y = −4",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Cero de una exponencial desplazada",
                "prompt": "¿Cuál es el cero de f(x) = 2ˣ − 4? Respondé solo con el número.",
                "answer": "2: igualamos a cero, 2ˣ − 4 = 0 → 2ˣ = 4 = 2² → x = 2 (propiedad cancelativa). Verificación: f(2) = 4 − 4 = 0. Ojo: f(0) = 1 − 4 = −3 es la ordenada al origen, no el cero.",
                "hints": ["Para el cero: f(x) = 0.", "Escribí 4 como potencia de base 2 e igualá exponentes."],
                "payload": {"check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Ordenada al origen de una exponencial corrida a la izquierda",
                "prompt": "¿Cuál es la ordenada al origen de g(x) = 3^(x + 2)? Respondé solo con el número.",
                "answer": "9: la ordenada al origen es g(0) = 3^(0 + 2) = 3² = 9. El + 2 está en el exponente, así que corre la gráfica de 3ˣ dos unidades a la izquierda (no hacia arriba); por eso no da 3⁰ + 2 = 3.",
                "hints": ["Ordenada al origen: reemplazá x por 0.", "El 2 está sumando dentro del exponente."],
                "payload": {"check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Cuadro de la reflexión −2ˣ respecto del eje x",
                "prompt": "¿Cuál es el cuadro correcto para y = −2ˣ (el signo menos afecta a toda la potencia)?",
                "answer": "Im = (−∞; 0), asíntota y = 0, ordenada al origen −1 y negativa en todo IR: −f(x) refleja la gráfica de 2ˣ respecto del eje x, así que cada y cambia de signo. La asíntota y = 0 queda igual, el punto (0; 1) pasa a (0; −1) y la función ahora es decreciente. Calcular la ordenada como (−2)⁰ = 1 es el error de meter el signo en la base.",
                "hints": ["−f(x) cambia el signo de todas las imágenes.", "−2⁰ = −(2⁰) = −1."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Im = (−∞; 0); asíntota y = 0; ordenada −1; C⁻ = IR",
                            "Im = (0; ∞); asíntota y = 0; ordenada 1; C⁺ = IR",
                            "Im = (−∞; 0); asíntota y = 0; ordenada 1; C⁻ = IR",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Reflexión 2^(−x) y simetría con (1/2)ˣ",
                "prompt": "¿Qué afirmación describe correctamente a h(x) = 2^(−x)?",
                "answer": "Es la misma función que (1/2)ˣ: es decreciente y su gráfica es simétrica de la de 2ˣ respecto del eje y. Como 2^(−x) = (2⁻¹)ˣ = (1/2)ˣ, la base efectiva es 1/2, que está entre 0 y 1. f(−x) refleja respecto del eje y; la reflexión respecto del eje x es −f(x).",
                "hints": ["Usá 2^(−x) = (2⁻¹)ˣ.", "f(−x) cambia el signo de las x, no de las y."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Es (1/2)ˣ: decreciente y simétrica de 2ˣ respecto del eje y",
                            "Es −2ˣ: simétrica de 2ˣ respecto del eje x",
                            "Es creciente, porque la base 2 es mayor que 1",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Imagen de una exponencial k·a^(x − h) + v con k negativo",
                "prompt": "¿Cuál es la imagen de f(x) = −2·3^(x − 1) + 6?",
                "answer": "Im = (−∞; 6): 3^(x − 1) toma todos los valores de (0; ∞); al multiplicar por −2 pasan a (−∞; 0) y al sumar 6 quedan en (−∞; 6). La asíntota es y = 6 y, como k = −2 < 0, la gráfica queda por debajo de ella. Su cero sale de 3^(x − 1) = 3 → x = 2 y su ordenada al origen es −2·3⁻¹ + 6 = 16/3.",
                "hints": [
                    "La asíntota de k·a^(x − h) + v es y = v.",
                    "Si k es negativo, la gráfica queda del lado de abajo de la asíntota.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(−∞; 6)", "(6; ∞)", "(−∞; 0)", "IR"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Cero de un logaritmo desplazado hacia abajo",
                "prompt": "¿Cuál es el cero de f(x) = log₂ x − 3? Respondé solo con el número.",
                "answer": "8: log₂ x − 3 = 0 → log₂ x = 3 → por definición de logaritmo, x = 2³ = 8. Verificación: log₂ 8 − 3 = 3 − 3 = 0. El dominio sigue siendo (0; ∞) y la asíntota x = 0: un desplazamiento vertical no los cambia.",
                "hints": ["Despejá el logaritmo y pasá a forma exponencial: log_a b = c ⇔ a^c = b."],
                "payload": {"check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Cuadro de un logaritmo corrido hacia la izquierda",
                "prompt": "Completá el cuadro de y = log₂(x + 3): ¿cuáles son su dominio, su cero y su ordenada al origen?",
                "answer": "D = (−3; ∞), cero x = −2 y ordenada al origen log₂ 3 ≈ 1,58: el argumento tiene que ser positivo, x + 3 > 0 → x > −3 (asíntota x = −3). El cero sale de x + 3 = 1 → x = −2, y como 0 está en el dominio, la ordenada es f(0) = log₂ 3. Además C⁻ = (−3; −2) y C⁺ = (−2; ∞).",
                "hints": [
                    "Dominio: argumento > 0.",
                    "Un logaritmo vale 0 cuando su argumento vale 1.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "D = (−3; ∞); cero x = −2; ordenada log₂ 3",
                            "D = (3; ∞); cero x = 4; no tiene ordenada al origen",
                            "D = (−3; ∞); cero x = 1; ordenada 0",
                            "D = (0; ∞); cero x = −2; ordenada 3",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Conjunto de positividad de un logaritmo de base menor que 1",
                "prompt": "¿Cuál es el conjunto de positividad de f(x) = log_{1/2} x?",
                "answer": "C⁺ = (0; 1): con base entre 0 y 1 la función logarítmica es decreciente; vale 0 en x = 1, así que es positiva a la izquierda del 1 (dentro del dominio (0; ∞)) y negativa en (1; ∞). Por ejemplo, log_{1/2}(1/4) = 2 > 0. Es la gráfica de log₂ x reflejada respecto del eje x.",
                "hints": ["¿Es creciente o decreciente si la base es 1/2?", "Calculá log_{1/2}(1/4) y log_{1/2} 4."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(0; 1)", "(1; ∞)", "(0; ∞)", "(−∞; 1)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Relación entre 3ˣ y log₃ x",
                "prompt": "¿Qué relación hay entre f(x) = 3ˣ y g(x) = log₃ x?",
                "answer": "Son funciones inversas entre sí: una deshace lo que hace la otra (log₃(3ˣ) = x y 3^(log₃ x) = x), sus gráficas son simétricas respecto de la recta y = x y el dominio de una es la imagen de la otra ((0; ∞) e IR). La simetría respecto del eje y es la de 3ˣ con (1/3)ˣ, e inversa no significa recíproca (1/3ˣ).",
                "hints": ["¿Qué recta del plano intercambia los papeles de x e y?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Son inversas: simétricas respecto de y = x",
                            "Son simétricas respecto del eje y",
                            "g es la recíproca de f: log₃ x = 1/3ˣ",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== SISTEMAS DE MEDICIÓN DE ÁNGULOS ====================
    {
        "slug": "t-sistemas-medicion",
        "title": "Sistemas de medición de ángulos: sexagesimal y radial",
        "summary": "Pasar ángulos de grados a radianes y al revés (en función de π y en decimales), operar con grados, minutos y segundos, ubicar ángulos negativos o mayores que un giro y calcular longitudes de arco con s = r·θ.",
        "prerequisites": ["g-trigonometria"],
        "insert_after": "a2-modelado-composicion",
        "metadata": {"section": "Trigonometría", "lab_tab": "trig_identities", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Pasar 135° a radianes en función de π",
                "prompt": "¿Cuánto mide 135° en radianes, expresado en función de π?",
                "answer": "3π/4: se multiplica por la razón unitaria π/180° → 135° · π/180° = (135/180)π = (3/4)π. También sale como ángulo notable: 135° = 3 · 45° = 3 · π/4.",
                "hints": ["De grados a radianes: multiplicá por π/180°.", "Simplificá la fracción 135/180."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["3π/4", "4π/3", "3π/2", "5π/6"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Pasar 25π/18 radianes a grados",
                "prompt": "¿Cuántos grados mide un ángulo de 25π/18 radianes? Respondé solo con el número, en grados.",
                "answer": "250°: de radianes a grados se multiplica por 180°/π → (25π/18) · (180°/π) = 25 · 10° = 250°. La π se simplifica: por eso conviene dejar los radianes en función de π.",
                "hints": ["De radianes a grados: multiplicá por 180°/π.", "180/18 = 10."],
                "payload": {"check": {"type": "numeric", "value": 250, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Pasar 2,5 radianes a grados con decimales",
                "prompt": "¿Cuántos grados mide un ángulo de 2,5 radianes? Redondeá a 2 decimales. Respondé solo con el número, en grados.",
                "answer": "143,24°: 2,5 · 180°/π = 450°/π ≈ 143,2394… ≈ 143,24°. Equivale a 2,5 veces 1 radián ≈ 57,296°. Multiplicar por π/180° (≈ 0,0436) es usar la razón al revés.",
                "hints": ["Un radián equivale a 180°/π ≈ 57,296°.", "Como no hay π en el dato, el resultado no se simplifica: usá la calculadora."],
                "payload": {"check": {"type": "numeric", "value": 143.24, "tolerance": 0.00003, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Pasar 220° a radianes en forma decimal",
                "prompt": "¿Cuánto mide 220° en radianes? Redondeá a 2 decimales. Respondé solo con el número.",
                "answer": "3,84: 220° · π/180° = 11π/9 ≈ 3,8397 ≈ 3,84. Tiene sentido: 220° es un poco más que un llano (π ≈ 3,14). Los radianes no llevan símbolo de unidad.",
                "hints": ["Primero escribilo en función de π simplificando 220/180.", "Después reemplazá π ≈ 3,14159."],
                "payload": {"check": {"type": "numeric", "value": 3.84, "tolerance": 0.001, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Pasar un ángulo decimal a grados, minutos y segundos",
                "prompt": "¿Cómo se escribe 25,42° en grados, minutos y segundos?",
                "answer": "25° 25' 12'': la parte entera son los grados (25°). La parte decimal se multiplica por 60: 0,42 · 60 = 25,2' → 25 minutos. Lo que sobra se vuelve a multiplicar por 60: 0,2 · 60 = 12''. En el sistema sexagesimal cada unidad se divide en 60, no en 100: por eso 25,42° no es 25° 42'.",
                "hints": ["1° = 60' y 1' = 60''.", "Multiplicá la parte decimal de los grados por 60 para obtener minutos."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["25° 25' 12''", "25° 42' 0''", "25° 4' 12''", "25° 25' 2''"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Pasar grados, minutos y segundos a grados decimales",
                "prompt": "¿Cuánto es 12° 30' 36'' expresado en grados con decimales? Respondé solo con el número, en grados.",
                "answer": "12,51°: 30' = 30/60 de grado = 0,5° y 36'' = 36/3600 de grado = 0,01°. Sumando: 12 + 0,5 + 0,01 = 12,51°. Escribir 12,3036° sería tratar minutos y segundos como si fueran decimales.",
                "hints": ["Los minutos se dividen por 60 y los segundos por 3600.", "Sumá todo a los grados enteros."],
                "payload": {"check": {"type": "numeric", "value": 12.51, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Ángulo positivo del primer giro equivalente a −120°",
                "prompt": "Un ángulo de −120° se mide en sentido horario. ¿Qué ángulo del primer giro, entre 0° y 360°, tiene el mismo lado terminal? Respondé solo con el número, en grados.",
                "answer": "240°: a un ángulo negativo se le suma un giro: −120° + 360° = 240°. Los dos tienen el mismo lado inicial (semieje positivo de x) y el mismo lado terminal, que cae en el 3.er cuadrante. En radianes: −2π/3 y 4π/3.",
                "hints": ["Sumar o restar 360° (un giro) no cambia el lado terminal.", "120° no sirve: ese ángulo está en el 2.° cuadrante."],
                "payload": {"check": {"type": "numeric", "value": 240, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Ubicar el cuadrante de un ángulo mayor que un giro",
                "prompt": "¿En qué cuadrante cae el lado terminal del ángulo 17π/4?",
                "answer": "En el 1.er cuadrante: 17π/4 = 4π + π/4, es decir dos giros completos (2 · 2π) más π/4 = 45°. En grados: 765° − 720° = 45°. Quitarle un solo giro deja 9π/4, que todavía es mayor que 2π.",
                "hints": ["Un giro es 2π = 8π/4: restá giros hasta quedar entre 0 y 2π.", "Pasalo a grados si te resulta más cómodo: 17π/4 = 765°."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["1.er cuadrante", "2.° cuadrante", "3.er cuadrante", "4.° cuadrante"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Definición de un radián",
                "prompt": "¿Qué es un ángulo de 1 radián?",
                "answer": "Es el ángulo central que abarca, sobre la circunferencia, un arco de longitud igual al radio. Equivale a 180°/π ≈ 57,296°. Lo que mide 180° son π radianes (un llano), no 1 radián.",
                "hints": ["La definición compara la longitud de un arco con el radio."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "El ángulo central que abarca un arco igual al radio",
                            "Un ángulo de 180°",
                            "El ángulo central que abarca un arco igual al diámetro",
                            "La 360.ª parte de un giro",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Longitud de arco con el ángulo dado en grados",
                "prompt": "Un arco de circunferencia de radio 15 cm abarca un ángulo central de 120°. ¿Cuánto mide el arco? Redondeá a 2 decimales. Respondé solo con el número, en cm.",
                "answer": "31,42 cm: la fórmula s = r·θ pide θ en radianes. 120° = 2π/3, así que s = 15 cm · 2π/3 = 10π cm ≈ 31,42 cm. Hacer 15 · 120 = 1800 cm mezcla grados con una fórmula que solo vale en radianes.",
                "hints": ["Pasá 120° a radianes antes de usar s = r·θ.", "Dejá el resultado en función de π y recién al final aproximá."],
                "payload": {"check": {"type": "numeric", "value": 31.42, "tolerance": 0.0001, "unit": "cm"}},
            },
        ],
    },
    # ==================== RELACIONES ENTRE ÁNGULOS ====================
    {
        "slug": "t-relaciones-angulos",
        "title": "Relaciones entre ángulos: complementarios, suplementarios, opuestos y que difieren en π o π/2",
        "summary": "Usar las fórmulas de reducción para simplificar expresiones, hallar las seis razones a partir de una y del cuadrante, demostrar identidades con sen² + cos² = 1 y resolver ecuaciones trigonométricas en [0; 2π).",
        "prerequisites": ["t-reciprocas-referencia"],
        "insert_after": "t-reciprocas-referencia",
        "metadata": {"section": "Trigonometría", "lab_tab": "trig_identities", "est_minutes": 35},
        "items": [
            {
                "item_type": "recall",
                "title": "Coseno de un ángulo que difiere en π",
                "prompt": "Según las relaciones entre ángulos que difieren en π, ¿a qué es igual cos(π + α)?",
                "answer": "−cos α: el punto de π + α en la circunferencia trigonométrica es el simétrico respecto del origen del punto de α, así que cambian de signo la abscisa (coseno) y la ordenada (seno). En cambio la tangente se mantiene: tg(π + α) = tg α.",
                "hints": ["Dibujá α y π + α: los puntos quedan opuestos por el centro."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["−cos α", "cos α", "−sen α", "sen α"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Coseno de un ángulo que difiere en π/2",
                "prompt": "Según las relaciones entre ángulos que difieren en π/2, ¿a qué es igual cos(π/2 + α)?",
                "answer": "−sen α: al sumar π/2 se pasa a la cofunción y, como para α agudo el ángulo π/2 + α está en el 2.° cuadrante (coseno negativo), aparece el signo menos. Las demás: sen(π/2 + α) = cos α y tg(π/2 + α) = −cotg α. Sin el signo, cos(π/2 − α) = sen α es la de los complementarios.",
                "hints": ["Con π/2 cambia a la cofunción.", "Para α agudo, ¿qué signo tiene el coseno de π/2 + α?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["−sen α", "sen α", "−cos α", "cos α"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Reducir una expresión con suplemento, complemento y opuesto",
                "prompt": "Expresá en función de α y simplificá: sen(π − α) + cos(90° − α) − 2·sen(−α).",
                "answer": "4·sen α: sen(π − α) = sen α (suplementarios), cos(90° − α) = sen α (complementarios: la cofunción, siempre positiva) y sen(−α) = −sen α (opuestos), así que −2·sen(−α) = +2·sen α. Total: sen α + sen α + 2·sen α = 4·sen α.",
                "hints": [
                    "Reemplazá cada término por separado antes de sumar.",
                    "Opuestos: el seno cambia de signo y el coseno no.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["4·sen α", "0", "3·sen α + cos α", "2·sen α"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Reducir una expresión con 180° + α, 90° + α y 180° − α",
                "prompt": "Expresá en función de α y simplificá: sen(180° + α) − cos(90° + α) − tg(180° − α).",
                "answer": "tg α: sen(180° + α) = −sen α, cos(90° + α) = −sen α y tg(180° − α) = −tg α. Queda −sen α − (−sen α) − (−tg α) = −sen α + sen α + tg α = tg α.",
                "hints": [
                    "Hacé cada reducción entre paréntesis y recién después aplicá los signos menos de afuera.",
                    "En el suplemento, el seno se conserva y la tangente cambia de signo.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["tg α", "−2·sen α + tg α", "−tg α", "2·sen α + tg α"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Tangente a partir de la secante en el cuarto cuadrante",
                "prompt": "Sabiendo que sec α = 3 y que α pertenece al 4.° cuadrante, ¿cuánto vale tg α (valor exacto)?",
                "answer": "−2√2: sec α = hip/ca = 3/1, así que hip = 3 y ca = 1. Por Pitágoras, co = √(9 − 1) = √8 = 2√2 (los lados siempre positivos). En el 4.° cuadrante la tangente es negativa: tg α = −co/ca = −2√2. Además sen α = −2√2/3, cos α = 1/3 y cotg α = −√2/4.",
                "hints": [
                    "Armá el triángulo con hipotenusa 3 y cateto adyacente 1, y calculá el otro cateto.",
                    "En el 4.° cuadrante solo el coseno y la secante son positivos.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["−2√2", "2√2", "−√2/4", "−2√2/3"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Seno más coseno a partir de la tangente en el tercer cuadrante",
                "prompt": "Sabiendo que tg α = 3/4 y que α pertenece al 3.er cuadrante, calculá sen α + cos α. Respondé solo con el número.",
                "answer": "−1,4: tg α = co/ca = 3/4 → co = 3, ca = 4 y, por Pitágoras, hip = 5. En el 3.er cuadrante seno y coseno son negativos: sen α = −3/5 y cos α = −4/5. Suma: −7/5 = −1,4. Con los signos del 1.er cuadrante daría 1,4.",
                "hints": [
                    "Con co = 3 y ca = 4, la hipotenusa sale por Pitágoras.",
                    "En el 3.er cuadrante, ¿qué signo tienen el seno y el coseno?",
                ],
                "payload": {"check": {"type": "numeric", "value": -1.4, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Secante al cuadrado con la identidad 1 + tg² = sec²",
                "prompt": "Si tg α = 2, ¿cuánto vale sec² α? Respondé solo con el número.",
                "answer": "5: la identidad 1 + tg² α = sec² α sale de dividir sen² α + cos² α = 1 por cos² α. Entonces sec² α = 1 + 2² = 5. No hace falta conocer el cuadrante, porque está al cuadrado.",
                "hints": ["Dividí sen² α + cos² α = 1 por cos² α y mirá qué identidad queda."],
                "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Elegir el desarrollo correcto de tg α + cotg α = sec α · cosec α",
                "prompt": "Para demostrar la identidad tg α + cotg α = sec α · cosec α se desarrolla el primer miembro. ¿Cuál es el desarrollo correcto?",
                "answer": "sen α/cos α + cos α/sen α = (sen² α + cos² α)/(sen α · cos α) = 1/(sen α · cos α) = sec α · cosec α: se pasa todo a seno y coseno, se suman las fracciones con denominador común sen α · cos α, se aplica sen² α + cos² α = 1 y se separa en el producto de las recíprocas. Sumar numerador con numerador y denominador con denominador no es válido.",
                "hints": [
                    "Escribí tg y cotg como cocientes de sen y cos.",
                    "Para sumar fracciones hace falta denominador común.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "(sen² α + cos² α)/(sen α · cos α) = 1/(sen α · cos α) = sec α · cosec α",
                            "(sen α + cos α)/(cos α + sen α) = 1",
                            "tg α · cotg α = 1",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Resolver sen x = −√2/2 en [0; 2π)",
                "prompt": "¿Cuál es el conjunto solución de sen x = −√2/2 con x ∈ [0; 2π)?",
                "answer": "S = {225°; 315°} = {5π/4; 7π/4}: el seno es negativo en el 3.er y 4.° cuadrante. La calculadora da arc sen(−√2/2) = −45°, que fuera de [0°; 360°) se mide como 360° − 45° = 315°. El ángulo del 3.er cuadrante con el mismo seno es 180° + 45° = 225°.",
                "hints": [
                    "¿En qué cuadrantes el seno es negativo?",
                    "El ángulo de referencia es 45°: armá 180° + 45° y 360° − 45°.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "S = {225°; 315°} = {5π/4; 7π/4}",
                            "S = {45°; 135°} = {π/4; 3π/4}",
                            "S = {135°; 225°} = {3π/4; 5π/4}",
                            "S = {−45°; 225°} = {−π/4; 5π/4}",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ecuación de segundo grado en seno con una solución descartada",
                "prompt": "¿Cuál es el conjunto solución de 2·sen² x − 5·sen x + 3 = 0 con x ∈ [0; 2π)?",
                "answer": "S = {90°} = {π/2}: con la resolvente en sen x, sen x = (5 ± √(25 − 24))/4 = (5 ± 1)/4, o sea sen x = 3/2 o sen x = 1. La primera no tiene solución, porque el seno siempre está entre −1 y 1. sen x = 1 tiene una sola solución en el primer giro: x = 90°, sobre el eje y.",
                "hints": [
                    "Tratá sen x como la incógnita de una cuadrática: a = 2, b = −5, c = 3.",
                    "¿Puede el seno valer 3/2? ¿Cuántos ángulos del primer giro tienen seno 1?",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["S = {90°} = {π/2}", "S = {90°; 270°} = {π/2; 3π/2}", "S = { }"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
]


INGRESO_MATH_C_LESSONS: dict[str, dict] = {
    "a2-estudio-funciones": {
        "hook": {
            "question": "¿Por qué la calculadora tira \"Math ERROR\" si querés calcular 1/(x − 3) en x = 3 o √(x − 5) en x = 2?",
            "intuition": "Porque esos valores **no están en el dominio**: no se puede dividir por 0 ni sacar raíz cuadrada de un negativo en IR. Estudiar una función es averiguar primero dónde existe y después dónde corta los ejes y dónde está por encima o por debajo del eje x. Con eso solo ya se puede bosquejar su gráfica.",
        },
        "concept": {
            "points": [
                "**Dominio** (`D`): los x a los que la función les asigna un único y. El **dominio natural** es el más grande posible; un **dominio restringido** es un subconjunto elegido (por el contexto, por ejemplo). Dos funciones son iguales solo si tienen el mismo dominio y la misma regla: si cambia el dominio, cambia la función. La **imagen** (`Im`) son los y que efectivamente toma (en otros temas de la app aparece como \"rango\"). En `f(a) = b`, `b` es la **imagen** de `a` y `a` es una **preimagen** de `b`.",
                "**Dominio analítico**: polinómicas → `D = IR`. Fraccionarias → `D = IR − {valores que anulan el denominador}`, calculados sobre la fórmula original, antes de simplificar. Irracionales de índice **par** → se resuelve la inecuación `radicando ≥ 0` (o `> 0` si la raíz está en un denominador), con tabla de signos si hace falta; si el radicando es un cociente, el valor que anula su denominador nunca entra. Índice **impar** → la raíz no agrega condiciones: el dominio es el del radicando (IR si es polinómico; si es un cociente, se excluyen los ceros del denominador).",
                "**Lectura gráfica**: el dominio es la proyección de la gráfica sobre el eje x y la imagen, la proyección sobre el eje y. Punto lleno → el extremo entra (corchete); punto vacío → no entra (paréntesis). Si el trazo se corta sin ningún punto marcado, la gráfica sigue indefinidamente en esa dirección.",
                "**Ceros**: los x del dominio con `f(x) = 0` (en otros temas, \"raíces\"); puede no haber ninguno o haber infinitos. **Ordenada al origen**: `f(0)`, solo si `0 ∈ D`; si existe, es única. En un polinomio, un cero de multiplicidad par rebota en el eje x y uno de multiplicidad impar lo cruza.",
                "**C⁺ y C⁻**: `C⁺` = los x con `f(x) > 0` (gráfica sobre el eje x) y `C⁻` = los x con `f(x) < 0`. Se leen en el eje x. Para hallarlos: marcá ceros y valores fuera del dominio, armá los intervalos, probá un **elemento de prueba** en cada uno y armá la **tabla de signos**. Los ceros y los puntos fuera del dominio no van en ninguno de los dos.",
                "**Funciones por partes**: cada fórmula vale solo en su tramo, así que todo cero u ordenada que encuentres tiene que cumplir la condición de ese tramo. **Valor con letras**: en `f(a + h)` se reemplaza cada x por `(a + h)` entre paréntesis.",
            ],
            "real_world": [
                {
                    "title": "Caja sin tapa armada con una lámina",
                    "detail": "Si a una lámina de 30 cm × 20 cm se le recortan cuadrados de lado x en las esquinas, el volumen es `V(x) = x(30 − 2x)(20 − 2x)`. La fórmula existe para todo IR, pero el contexto restringe el dominio a `(0; 10)`: el lado no puede ser negativo ni llegar a la mitad del ancho.",
                },
                {
                    "title": "Ganancia de un emprendimiento",
                    "detail": "Si `G(x)` es la ganancia al vender x unidades, `C⁺` dice para qué cantidades hay ganancia, `C⁻` cuándo hay pérdida, y los ceros son los puntos de equilibrio.",
                },
                {
                    "title": "Tarifas por tramos",
                    "detail": "Un envío que cuesta un fijo hasta 1 kg y después aumenta por kilo es una función por partes: cada fórmula se aplica solo en su tramo y el punto lleno o vacío decide en qué tramo cae el peso justo del borde.",
                },
            ],
            "key_rule": "Dominio: denominador ≠ 0, radicando par ≥ 0 (> 0 si está abajo) | Ceros: f(x) = 0 con x ∈ D | Ordenada: f(0) si 0 ∈ D | C⁺: f(x) > 0, C⁻: f(x) < 0, por tabla de signos.",
            "pitfall": "Simplificar antes de calcular el dominio, o meter en C⁺ o C⁻ un cero o un valor que no está en el dominio: en esos x la función no es positiva ni negativa.",
        },
        "example": {
            "title": "Estudio completo de f(x) = (x² − 4)/(x + 1)",
            "steps": [
                "**Dominio**: el denominador se anula en `x = −1` → `D = IR − {−1}`.",
                "**Ceros**: `f(x) = 0` → `x² − 4 = 0` → `x = 2` y `x = −2`, los dos en el dominio. **Ordenada al origen**: `f(0) = (0 − 4)/(0 + 1) = −4`.",
                "**Valores críticos**: `−2`, `−1` y `2` parten la recta en `(−∞; −2)`, `(−2; −1)`, `(−1; 2)` y `(2; ∞)`.",
                "**Elementos de prueba**: `f(−3) = −2,5 < 0`; `f(−1,5) = 3,5 > 0`; `f(0) = −4 < 0`; `f(3) = 1,25 > 0`.",
                "**Conclusión**: `C⁺ = (−2; −1) ∪ (2; ∞)` y `C⁻ = (−∞; −2) ∪ (−1; 2)`. Los ceros `±2` y el `−1` (fuera del dominio) no pertenecen a ninguno.",
            ],
            "lab_link": "math:polynomials",
            "lab_cta": "Practicar con polinomios y asíntotas",
        },
        "check": {
            "question": "¿Cuál es el dominio de `f(x) = √(3x − 6)`?",
            "options": [
                {"text": "`[2; ∞)`", "ok": True, "feedback": "Exacto: 3x − 6 ≥ 0 → x ≥ 2, y el 2 entra porque √0 = 0 existe."},
                {"text": "`(2; ∞)`", "ok": False, "feedback": "Usaste > en vez de ≥: en x = 2 el radicando vale 0 y la raíz existe, así que el 2 entra."},
                {"text": "`(−∞; 2]`", "ok": False, "feedback": "Invertiste el sentido de la desigualdad: dividir por 3 (positivo) no lo da vuelta, queda x ≥ 2."},
            ],
        },
        "checks": [
            {
                "question": "Si `f(x₁) = 0`, ¿en cuál de los conjuntos está `x₁`?",
                "options": [
                    {"text": "En ninguno de los dos", "ok": True, "feedback": "Exacto: 0 no es positivo ni negativo, así que un cero no está ni en C⁺ ni en C⁻ (por eso lleva paréntesis en los intervalos)."},
                    {"text": "En `C⁺`", "ok": False, "feedback": "C⁺ pide f(x) > 0 (estrictamente): en x₁ la función vale 0."},
                    {"text": "En `C⁻`", "ok": False, "feedback": "C⁻ pide f(x) < 0 (estrictamente): en x₁ la función vale 0."},
                ],
            },
            {
                "question": "¿Cuál es el dominio de `f(x) = 2/√(x² − 4)`?",
                "options": [
                    {"text": "`(−∞; −2) ∪ (2; ∞)`", "ok": True, "feedback": "Exacto: la raíz par está en el denominador, así que x² − 4 > 0, y eso pasa fuera de [−2; 2]."},
                    {"text": "`(−∞; −2] ∪ [2; ∞)`", "ok": False, "feedback": "En x = ±2 el radicando vale 0 y el denominador se anula: con la raíz abajo la condición es > 0, no ≥ 0."},
                    {"text": "`(−2; 2)`", "ok": False, "feedback": "En ese intervalo el radicando es negativo (por ejemplo, x = 0 da −4): es justo la parte que hay que descartar."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras por qué, al estudiar una función, primero hay que calcular el dominio, y qué pasa con un cero o con un valor excluido del dominio cuando armás C⁺ y C⁻.",
    },
    "a2-graficas-exp-log": {
        "hook": {
            "question": "Un medicamento se elimina de forma que su cantidad en sangre se reduce a la mitad cada 6 horas. ¿Llega alguna vez a cero?",
            "intuition": "En el modelo, no: la mitad de algo positivo sigue siendo positivo. La gráfica se acerca cada vez más al eje x sin tocarlo nunca: tiene una **asíntota horizontal** `y = 0`. Si la gráfica se desplaza, la asíntota se desplaza con ella, y con eso se completa casi todo el cuadro de la función.",
        },
        "concept": {
            "points": [
                "**Exponencial** `f(x) = aˣ` con `a > 0` y `a ≠ 1`: `D = IR`, `Im = IR⁺ = (0; ∞)`, ordenada al origen `f(0) = 1`, asíntota horizontal `y = 0`, sin ceros y siempre positiva. Si `a > 1` es **creciente**; si `0 < a < 1`, **decreciente**. Las gráficas de `aˣ` y `(1/a)ˣ` son simétricas respecto del eje y.",
                "**Exponencial desplazada** `f(x) = k·a^(x − h) + v`: `h` corre la gráfica en horizontal (`x − h`: h unidades a la derecha si h > 0) y `v` en vertical. La **asíntota** es `y = v`; la imagen es `(v; ∞)` si `k > 0` y `(−∞; v)` si `k < 0`. Ordenada: `f(0) = k·a^(−h) + v`. Cero: resolver `k·a^(x − h) + v = 0`, que tiene solución solo si `−v/k > 0`.",
                "**Reflexiones**: `−f(x)` refleja respecto del eje x (`−2ˣ` tiene imagen `(−∞; 0)` y ordenada `−1`); `f(−x)` refleja respecto del eje y (`2^(−x) = (1/2)ˣ`).",
                "**Logarítmica** `f(x) = log_a x`: `D = IR⁺ = (0; ∞)`, `Im = IR`, cero `x = 1`, asíntota vertical `x = 0` y sin ordenada al origen. Con `a > 1` es creciente (`C⁻ = (0; 1)`, `C⁺ = (1; ∞)`); con `0 < a < 1` es decreciente y los conjuntos se invierten. `log_a x` y `log_{1/a} x` son simétricas respecto del eje x.",
                "**Logarítmica desplazada** `f(x) = log_a(x − h) + v`: dominio `x − h > 0` → `(h; ∞)`, asíntota `x = h`, cero `x = h + a^(−v)` (de `log_a(x − h) = −v`) y ordenada solo si `0` está en el dominio (o sea, si `h < 0`). `log_a(−x)` tiene dominio `(−∞; 0)`.",
                "**Inversas**: `aˣ` y `log_a x` se deshacen entre sí (`log_a(aˣ) = x`, `a^(log_a x) = x`); sus gráficas son simétricas respecto de la recta `y = x` y el dominio de una es la imagen de la otra.",
            ],
            "real_world": [
                {
                    "title": "Yodo radiactivo en medicina",
                    "detail": "La masa de un trazador de yodo sigue `m(t) = 6·e^(−0,087t)` gramos: decreciente, con asíntota `y = 0`. Despejar cuándo quedan 3 g pide aplicar logaritmos, la función inversa.",
                },
                {
                    "title": "Enfriamiento de un objeto",
                    "detail": "Con la ley de Newton, `T(t) = Tₐ + (T₀ − Tₐ)·e^(−kt)`: es una exponencial desplazada cuya asíntota es `y = Tₐ`, la temperatura del ambiente a la que el objeto se acerca sin alcanzarla.",
                },
                {
                    "title": "Escalas logarítmicas",
                    "detail": "Los decibeles y el pH usan `log`: comprimen valores enormes en números manejables. Por el dominio, el argumento (una intensidad o una concentración) siempre tiene que ser positivo.",
                },
            ],
            "key_rule": "aˣ: D = IR, Im = (0; ∞), asíntota y = 0, pasa por (0; 1) | log_a x: D = (0; ∞), Im = IR, asíntota x = 0, pasa por (1; 0) | Los desplazamientos mueven la asíntota | a > 1 crece, 0 < a < 1 decrece.",
            "pitfall": "Confundir el tipo de asíntota (la exponencial la tiene horizontal, y = v; la logarítmica vertical, x = h) o correr la gráfica para el lado equivocado: en log₂(x + 3) el dominio es (−3; ∞), no (3; ∞).",
        },
        "example": {
            "title": "Cuadro completo de f(x) = 2^(x + 1) − 4",
            "steps": [
                "Partimos de `y = 2ˣ`: `D = IR`, `Im = (0; ∞)`, asíntota `y = 0` y pasa por `(0; 1)`.",
                "El `+ 1` del exponente corre la gráfica 1 unidad a la izquierda y el `− 4` la baja 4: la **asíntota** pasa a ser `y = −4`, `Im = (−4; ∞)` y `D = IR` no cambia.",
                "**Ordenada al origen**: `f(0) = 2¹ − 4 = −2`.",
                "**Cero**: `2^(x + 1) = 4 = 2²` → `x + 1 = 2` → `x = 1`. Verificación: `f(1) = 4 − 4 = 0`.",
                "**Crecimiento y signo**: la base 2 es mayor que 1, así que es creciente: `C⁻ = (−∞; 1)` y `C⁺ = (1; ∞)`.",
            ],
            "lab_link": "math:logarithms",
            "lab_cta": "Practicar logaritmos",
        },
        "check": {
            "question": "¿Cuál de estas funciones es **decreciente**?",
            "options": [
                {"text": "`f(x) = (3/4)ˣ`", "ok": True, "feedback": "Exacto: la base 3/4 está entre 0 y 1, así que cada vez que x aumenta 1, el valor se multiplica por 3/4 y baja."},
                {"text": "`f(x) = (5/4)ˣ`", "ok": False, "feedback": "Que sea una fracción no alcanza: 5/4 = 1,25 es mayor que 1, así que la función crece."},
                {"text": "`f(x) = 2,5ˣ`", "ok": False, "feedback": "La base 2,5 es mayor que 1: la función es creciente."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuáles son el dominio y la asíntota de `y = log₂(x − 5)`?",
                "options": [
                    {"text": "`D = (5; ∞)`; asíntota `x = 5`", "ok": True, "feedback": "Exacto: el argumento tiene que ser positivo, x − 5 > 0, y la asíntota vertical se corre a x = 5. Su cero es x = 6."},
                    {"text": "`D = (−5; ∞)`; asíntota `x = −5`", "ok": False, "feedback": "Corriste la gráfica para el lado equivocado: x − 5 > 0 da x > 5, un desplazamiento a la derecha."},
                    {"text": "`D = (5; ∞)`; asíntota `y = 5`", "ok": False, "feedback": "El dominio está bien, pero la asíntota de una logarítmica es vertical (x = número), no horizontal."},
                ],
            },
            {
                "question": "¿Cuál es la imagen de `y = 2ˣ + 2`?",
                "options": [
                    {"text": "`(2; ∞)`", "ok": True, "feedback": "Exacto: la gráfica de 2ˣ sube 2 unidades y la asíntota pasa a ser y = 2, valor que nunca se alcanza."},
                    {"text": "`(0; ∞)`", "ok": False, "feedback": "Esa es la imagen de 2ˣ sin desplazar: el + 2 sube toda la gráfica."},
                    {"text": "`[2; ∞)`", "ok": False, "feedback": "El 2 es el valor de la asíntota: la función se acerca a él pero no lo toma, así que va con paréntesis."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras cómo se mueven la asíntota y la imagen de aˣ cuando pasás a k·a^(x − h) + v, y por qué la logarítmica, al ser la inversa, tiene la asíntota vertical.",
    },
    "t-sistemas-medicion": {
        "hook": {
            "question": "¿Por qué la calculadora puede decir que sen 30 = −0,988 si todos sabemos que sen 30° = 0,5?",
            "intuition": "Porque estaba en modo **RAD**: calculó el seno de 30 **radianes** (casi cinco giros), no de 30 grados. Un mismo ángulo se puede medir en dos sistemas, el **sexagesimal** (grados) y el **radial** (radianes), y hay que saber pasar de uno al otro sin equivocarse.",
        },
        "concept": {
            "points": [
                "**Sistema sexagesimal**: la unidad es el grado (°); un ángulo recto mide 90° y un giro 360°. Cada unidad se divide en 60: `1° = 60'` (minutos) y `1' = 60''` (segundos). Para pasar de decimal a grados, minutos y segundos se multiplica la parte decimal por 60, dos veces; al revés, se divide por 60 y por 3600.",
                "**Sistema radial (circular)**: un **radián** es el ángulo central que abarca un arco de longitud igual al radio. No lleva símbolo: el ángulo se expresa con un número. La equivalencia clave es `π = 180°`, así que `1 radián = 180°/π ≅ 57,296°`.",
                "**Conversiones**: de grados a radianes se multiplica por la razón unitaria `π/180°`; de radianes a grados, por `180°/π`. En función de π se simplifica la fracción (`150° = 5π/6`); en decimal se reemplaza `π ≈ 3,14159`. Notables: `30° = π/6`, `45° = π/4`, `60° = π/3`, `90° = π/2`, y sus múltiplos (`135° = 3·45° = 3π/4`).",
                "**Ángulos orientados**: el origen de medición es el semieje positivo de las x. Sentido **antihorario** → ángulo positivo; **horario** → negativo. Sumar o restar giros (`360°` o `2π`) no cambia el lado terminal (en otros temas de la app se los llama ángulos **coterminales**), y así se ubica en qué cuadrante cae un ángulo negativo o mayor que un giro.",
                "**Longitud de arco**: `s = r·θ`, con `θ` **en radianes**. Por eso el radián es la medida natural para arcos, velocidades de giro y cálculo.",
            ],
            "real_world": [
                {
                    "title": "Coordenadas geográficas",
                    "detail": "Un GPS da la latitud de Mendoza como 32° 53' S: grados y minutos sexagesimales. Muchas apps la muestran en decimal (−32,88°), y pasar de una forma a la otra es la conversión con 60.",
                },
                {
                    "title": "Ruedas y odómetros",
                    "detail": "Una rueda de radio r que gira un ángulo θ avanza `s = r·θ` (con θ en radianes): así calcula la distancia el cuentakilómetros de una bicicleta.",
                },
                {
                    "title": "Motores y máquinas",
                    "detail": "En ingeniería la velocidad de giro se expresa en rad/s: un motor a 3000 rpm gira `3000 · 2π / 60 ≈ 314` rad/s. Mezclar grados con radianes en una fórmula da resultados absurdos.",
                },
            ],
            "key_rule": "π = 180° | grados → rad: × π/180° | rad → grados: × 180°/π | 1° = 60', 1' = 60'' | antihorario +, horario − | s = r·θ con θ en radianes.",
            "pitfall": "Tratar los minutos como decimales (25,42° NO es 25° 42') o usar s = r·θ con el ángulo en grados: la fórmula solo vale en radianes.",
        },
        "example": {
            "title": "Cuánto avanza una rueda de 30 cm de radio que gira 150°",
            "steps": [
                "Pasamos el ángulo a radianes: `150° · π/180° = (150/180)π = 5π/6`.",
                "Control con ángulos notables: `150° = 5 · 30° = 5 · π/6` ✓.",
                "Aplicamos la longitud de arco: `s = r·θ = 30 cm · 5π/6 = 25π cm`.",
                "En decimal: `25π ≈ 78,54 cm`. Si hubiéramos hecho `30 · 150` daría 4500 cm, un absurdo que delata el ángulo en grados.",
            ],
            "lab_link": "math:trig_identities",
            "lab_cta": "Practicar ángulos y razones",
        },
        "check": {
            "question": "¿Cuánto mide 300° en radianes?",
            "options": [
                {"text": "`5π/3`", "ok": True, "feedback": "Exacto: 300° · π/180° = (300/180)π = 5π/3 (también 300° = 5 · 60° = 5 · π/3)."},
                {"text": "`5π/6`", "ok": False, "feedback": "5π/6 son 150°: simplificaste 300/180 como si fuera 5/6, pero da 5/3."},
                {"text": "`3π/5`", "ok": False, "feedback": "Invertiste la fracción: 3π/5 son 108°."},
            ],
        },
        "checks": [
            {
                "question": "¿Cómo se mide un ángulo **positivo**?",
                "options": [
                    {"text": "Desde el semieje positivo de las x, en sentido antihorario", "ok": True, "feedback": "Exacto: ese es el origen de medición, y el sentido contrario a las agujas del reloj es el positivo."},
                    {"text": "Desde el semieje positivo de las x, en sentido horario", "ok": False, "feedback": "El origen está bien, pero el sentido horario da ángulos negativos."},
                    {"text": "Desde el semieje positivo de las y, en sentido antihorario", "ok": False, "feedback": "El origen de medición es el semieje positivo de las x (las abscisas), no el de las y."},
                ],
            },
            {
                "question": "¿Qué ángulo entre 0° y 360° tiene el mismo lado terminal que `−45°`?",
                "options": [
                    {"text": "`315°`", "ok": True, "feedback": "Exacto: −45° + 360° = 315°, en el 4.° cuadrante."},
                    {"text": "`45°`", "ok": False, "feedback": "45° está en el 1.er cuadrante: cambiar el signo refleja el ángulo, no le suma un giro."},
                    {"text": "`135°`", "ok": False, "feedback": "135° está en el 2.° cuadrante: restaste de 180° en vez de sumar 360°."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras qué es un radián y por qué para usar s = r·θ el ángulo tiene que estar en radianes y no en grados.",
    },
    "t-relaciones-angulos": {
        "hook": {
            "question": "Sin calculadora: si sabés que sen 30° = 1/2, ¿cuánto vale sen 150°?",
            "intuition": "También 1/2. Como `150° = 180° − 30°`, los dos ángulos son **suplementarios** y sus puntos en la circunferencia trigonométrica quedan a la misma altura (simétricos respecto del eje y). Con unas pocas simetrías como esta se pueden reducir las razones de cualquier ángulo a las de uno agudo.",
        },
        "concept": {
            "points": [
                "**Opuestos** (`α` y `−α`, simetría respecto del eje x): `sen(−α) = −sen α`, `cos(−α) = cos α`, `tg(−α) = −tg α`. **Suplementarios** (`π − α`, simetría respecto del eje y): `sen(π − α) = sen α`, `cos(π − α) = −cos α`, `tg(π − α) = −tg α`.",
                "**Difieren en π** (`π + α`, simetría respecto del origen): `sen(π + α) = −sen α`, `cos(π + α) = −cos α`, `tg(π + α) = tg α`. Cada recíproca sigue a su razón: cosec con sen, sec con cos y cotg con tg.",
                "**Complementarios** (`π/2 − α`): se pasa a la **cofunción** y todo queda positivo: `sen(π/2 − α) = cos α`, `cos(π/2 − α) = sen α`, `tg(π/2 − α) = cotg α`. **Difieren en π/2** (`π/2 + α`): `sen(π/2 + α) = cos α`, `cos(π/2 + α) = −sen α`, `tg(π/2 + α) = −cotg α`.",
                "**Las seis razones desde una**: armá un triángulo con lados positivos a partir del dato (por ejemplo `sec α = hip/ca`), hallá el lado que falta con Pitágoras y poné el signo según el cuadrante: 1.° todas +; 2.° solo sen y cosec +; 3.° solo tg y cotg +; 4.° solo cos y sec +. (En otros temas de la app aparecen como `tan`, `csc` y `cot`; acá usamos `tg`, `cosec` y `cotg`, como en el ingreso.)",
                "**Identidades fundamentales**: `sen² α + cos² α = 1`; dividiendo por `cos² α`, `1 + tg² α = sec² α`; dividiendo por `sen² α`, `1 + cotg² α = cosec² α`; además `tg α = sen α/cos α`. Para **demostrar** una identidad se desarrolla un solo miembro (pasando todo a seno y coseno) hasta llegar al otro, sin pasar términos de un miembro al otro.",
                "**Ecuaciones en [0; 2π)**: despejá la razón; si es sec, cosec o cotg, invertí los dos miembros (si el valor es 0, como en cotg x = 0, pensalo como cos x = 0); fijate en qué cuadrantes tiene ese signo; con la calculadora y el valor absoluto obtené el ángulo de referencia agudo x, y los ángulos son x, `180° − x`, `180° + x` o `360° − x` según esos cuadrantes. Si es de segundo grado, usá la resolvente y descartá valores de sen o cos fuera de `[−1; 1]`. Respondé en grados y en radianes.",
            ],
            "real_world": [
                {
                    "title": "Corriente alterna",
                    "detail": "En un capacitor la corriente va adelantada 90° respecto de la tensión. Que `cos(ωt + π/2) = −sen(ωt)` es exactamente la relación entre ángulos que difieren en π/2 aplicada a señales.",
                },
                {
                    "title": "Rumbos de navegación",
                    "detail": "El rumbo de regreso es el de ida más 180°: las componentes de avance cambian de signo porque `sen(π + α) = −sen α` y `cos(π + α) = −cos α`.",
                },
                {
                    "title": "Cómo calcula una computadora",
                    "detail": "Las bibliotecas numéricas reducen cualquier ángulo a uno chico antes de calcular su seno: usan las mismas simetrías (suplemento, diferencia en π o π/2) que aplicás vos a mano.",
                },
            ],
            "key_rule": "Opuestos: solo cos se conserva | Suplementarios: solo sen se conserva | Difieren en π: solo tg se conserva | Con π/2 se pasa a la cofunción (en π/2 + α cambian cos y tg) | sen² + cos² = 1.",
            "pitfall": "Olvidar el signo del cuadrante al hallar las razones (los lados del triángulo son positivos, las razones no siempre), o dejar como solución el ángulo negativo que da la calculadora en lugar de llevarlo a [0°; 360°).",
        },
        "example": {
            "title": "Hallar todas las razones sabiendo que cosec α = −2 y α ∈ 3.er cuadrante",
            "steps": [
                "`cosec α = hip/co = 2/1` (los lados se toman positivos): hipotenusa `2` y cateto opuesto `1`.",
                "Pitágoras: cateto adyacente `= √(2² − 1²) = √3`.",
                "Signos en el 3.er cuadrante: solo `tg` y `cotg` son positivas; `sen`, `cos`, `sec` y `cosec` son negativas.",
                "`sen α = −1/2`, `cos α = −√3/2`, `tg α = 1/√3 = √3/3`.",
                "`cosec α = −2`, `sec α = −2/√3 = −2√3/3`, `cotg α = √3`.",
                "Verificación: `sen² α + cos² α = 1/4 + 3/4 = 1` ✓.",
            ],
            "lab_link": "math:trig_identities",
            "lab_cta": "Practicar identidades",
        },
        "check": {
            "question": "¿A qué es igual `cos(π − α)`?",
            "options": [
                {"text": "`−cos α`", "ok": True, "feedback": "Exacto: los puntos de α y π − α son simétricos respecto del eje y, así que la abscisa (el coseno) cambia de signo."},
                {"text": "`cos α`", "ok": False, "feedback": "El que se conserva en los suplementarios es el seno: el coseno cambia de signo."},
                {"text": "`sen α`", "ok": False, "feedback": "El cambio a la cofunción ocurre con π/2, no con π."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál es el conjunto solución de `2·sen x = 1` en `[0; 2π)`?",
                "options": [
                    {"text": "`{π/6; 5π/6}`", "ok": True, "feedback": "Exacto: sen x = 1/2 es positivo en el 1.° y 2.° cuadrante: 30° y 180° − 30° = 150°."},
                    {"text": "`{π/6; 7π/6}`", "ok": False, "feedback": "7π/6 = 210° está en el 3.er cuadrante, donde el seno es negativo: sen 210° = −1/2."},
                    {"text": "`{π/6; 11π/6}`", "ok": False, "feedback": "11π/6 = 330° tiene el mismo coseno que 30°, no el mismo seno (sen 330° = −1/2)."},
                ],
            },
            {
                "question": "¿Cuál de estas identidades es correcta para todo α donde estén definidas?",
                "options": [
                    {"text": "`1 + cotg² α = cosec² α`", "ok": True, "feedback": "Exacto: sale de dividir sen² α + cos² α = 1 por sen² α."},
                    {"text": "`1 + tg² α = cosec² α`", "ok": False, "feedback": "Al dividir por cos² α aparece sec² α, no cosec² α: 1 + tg² α = sec² α."},
                    {"text": "`sen α + cos α = 1`", "ok": False, "feedback": "La identidad lleva cuadrados: para α = 45° da √2 ≈ 1,41, no 1."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras cómo usás la circunferencia trigonométrica para recordar qué razón se conserva y cuál cambia de signo en los ángulos opuestos, suplementarios y que difieren en π.",
    },
}
