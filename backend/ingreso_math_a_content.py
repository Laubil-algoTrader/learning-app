"""Temas de Álgebra 1 basados en el material del Curso de Ingreso 2027 (Ingeniería, UNCuyo).

Cuatro nodos que se intercalan en Álgebra 1 mediante `insert_after`:
  - Teoría de conjuntos (Unidad 0)
  - Números reales: propiedades, periódicos y cálculos combinados (Unidad 1.1 y 1.2)
  - Radicales: extracción, operaciones y racionalización (Unidad 1.3)
  - Valor absoluto: distancia, ecuaciones e inecuaciones modulares (Unidad 3.1)

Se respeta la notación del ingreso: IN (sin el 0), IN₀, Z, Q, II, IR; "/" = "tal que";
intervalos con punto y coma; S = {…}, S = IR, S = { }; coma decimal.
"""

from __future__ import annotations

INGRESO_MATH_A_NODES: list[dict] = [
    # ==================== TEORÍA DE CONJUNTOS ====================
    {
        "slug": "al-teoria-conjuntos",
        "title": "Teoría de conjuntos: extensión, comprensión, Venn y operaciones",
        "summary": "Definir conjuntos por extensión y por comprensión, distinguir pertenencia de inclusión, operar con unión, intersección, complemento y diferencia, y contar con diagramas de Venn.",
        "prerequisites": ["p-desigualdades"],
        "insert_after": "p-sistemas-ecuaciones",
        "metadata": {"section": "Álgebra 1", "lab_tab": "linear_eq", "est_minutes": 18},
        "items": [
            {
                "item_type": "recall",
                "title": "Elegir entre pertenencia e inclusión",
                "prompt": "Sea A = {a; e; i; o; u}. ¿Cuál de estas afirmaciones es correcta?",
                "answer": "{a; e} ⊂ A: {a; e} es un conjunto y todos sus elementos están en A, así que se usa inclusión. En cambio a es un elemento (a ∈ A, no a ⊂ A), {a} no es elemento de A (sus elementos son letras, no conjuntos) y u sí pertenece a A.",
                "hints": [
                    "∈ relaciona ELEMENTO con conjunto; ⊂ relaciona CONJUNTO con conjunto.",
                    "Fijate si lo que está a la izquierda del símbolo lleva llaves o no.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["{a} ∈ A", "a ⊂ A", "{a; e} ⊂ A", "u ∉ A"],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Escribir por extensión un conjunto definido en IN₀",
                "prompt": "Sea M = {x ∈ IN₀ / x es par ∧ x ≤ 10} (el símbolo ∧ se lee \"y\"). Escribilo por extensión. ¿Cuántos elementos tiene M? Respondé solo con el número.",
                "answer": "6: M = {0; 2; 4; 6; 8; 10}. El 0 entra porque IN₀ incluye al cero (y 0 es par), y el 10 entra porque la condición es x ≤ 10.",
                "hints": [
                    "IN₀ es IN con el 0 agregado: IN₀ = {0; 1; 2; 3; …}.",
                    "Revisá los dos extremos: ¿el 0 cumple la propiedad? ¿y el 10?",
                ],
                "payload": {"check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Pasar de extensión a comprensión sin agregar elementos",
                "prompt": "¿Cuál de estas expresiones define por comprensión exactamente al conjunto T = {3; 6; 9; 12}?",
                "answer": "{x ∈ IN / x es múltiplo de 3 ∧ x ≤ 12}: los múltiplos naturales de 3 hasta el 12 inclusive son 3, 6, 9 y 12. Sin tope el conjunto sería infinito; con x < 12 se pierde el 12, y en IN₀ aparecería el 0, que también es múltiplo de 3.",
                "hints": [
                    "La propiedad tiene que describir TODOS los elementos y NINGUNO más.",
                    "Probá cada opción con los extremos: ¿entra el 12? ¿entra el 0?",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "{x / x es múltiplo de 3}",
                            "{x ∈ IN / x es múltiplo de 3 ∧ x ≤ 12}",
                            "{x ∈ IN / x es múltiplo de 3 ∧ x < 12}",
                            "{x ∈ IN₀ / x es múltiplo de 3 ∧ x ≤ 12}",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Complemento de una unión de conjuntos",
                "prompt": "Sean U = {x ∈ IN / x < 10}, A = {1; 2; 3; 4; 5} y B = {4; 5; 6; 7}. ¿Cuántos elementos tiene el complemento de A ∪ B? Respondé solo con el número.",
                "answer": "2: U = {1; 2; …; 9} (en el ingreso IN no tiene el 0) y A ∪ B = {1; 2; 3; 4; 5; 6; 7}. Los elementos de U que no están en la unión son 8 y 9, así que el complemento es {8; 9}.",
                "hints": [
                    "Primero escribí U por extensión: ¿empieza en 0 o en 1? ¿incluye al 10?",
                    "Hacé la unión (los repetidos se escriben una sola vez) y fijate qué elementos de U quedan afuera.",
                ],
                "payload": {"check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "La diferencia de conjuntos no es conmutativa",
                "prompt": "Sean A = {2; 4; 6; 8; 10} y B = {1; 2; 3; 4; 5}. ¿Cuánto es B − A?",
                "answer": "B − A = {1; 3; 5}: son los elementos que pertenecen a B pero NO a A. Ojo que A − B = {6; 8; 10} es otro conjunto: la diferencia no es conmutativa.",
                "hints": [
                    "B − A arranca desde B: recorré los elementos de B y tachá los que también están en A.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["{6; 8; 10}", "{1; 3; 5}", "{2; 4}", "{1; 3; 5; 6; 8; 10}"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Reconocer dos conjuntos disjuntos",
                "prompt": "Dos conjuntos son disjuntos cuando su intersección es el conjunto vacío. ¿Cuál de estos pares es de conjuntos disjuntos?",
                "answer": "Los pares y los impares naturales: ningún natural es par e impar a la vez, así que su intersección es { }. Los otros pares comparten elementos: la i, el 4, y en el caso de IN y Z todos los naturales (IN ⊂ Z).",
                "hints": ["Buscá algún elemento que esté en los dos conjuntos; si lo encontrás, no son disjuntos."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "{a; e; i} y {i; o; u}",
                            "{x ∈ IN / x < 5} y {x ∈ IN / x > 3}",
                            "{x ∈ IN / x es par} y {x ∈ IN / x es impar}",
                            "IN y Z",
                        ],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Contar con Venn los que no cumplen ninguna condición",
                "prompt": "En un curso de 40 estudiantes, 25 aprobaron Matemática, 18 aprobaron Física y 10 aprobaron las dos. ¿Cuántos estudiantes no aprobaron ninguna de las dos? Respondé solo con el número.",
                "answer": "7: solo Matemática son 25 − 10 = 15 y solo Física 18 − 10 = 8. La unión tiene 15 + 10 + 8 = 33 estudiantes (o 25 + 18 − 10). Fuera de los dos círculos quedan 40 − 33 = 7.",
                "hints": [
                    "Completá el Venn de adentro hacia afuera: primero la intersección.",
                    "Si sumás 25 + 18, los 10 que aprobaron las dos quedan contados dos veces.",
                ],
                "payload": {"check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Contar con Venn los que cumplen una sola condición",
                "prompt": "De 60 personas encuestadas, 35 viajan en colectivo, 28 en bicicleta y 12 usan los dos medios. ¿Cuántas personas usan solo uno de los dos medios? Respondé solo con el número.",
                "answer": "39: solo colectivo son 35 − 12 = 23 y solo bicicleta 28 − 12 = 16; en total 23 + 16 = 39. Es la cantidad de elementos de (C − B) ∪ (B − C).",
                "hints": [
                    "Las 12 personas de la intersección NO cuentan: usan los dos medios.",
                    "A cada total restale la intersección y después sumá las dos partes.",
                ],
                "payload": {"check": {"type": "numeric", "value": 39, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Propiedades del conjunto vacío y del universal",
                "prompt": "¿Cuál de estas afirmaciones es verdadera?",
                "answer": "∅ ⊂ A para cualquier conjunto A: el vacío está incluido en todo conjunto. El complemento de U es ∅ (no U), ∅ no es un elemento de {1; 2; 3} (sus elementos son números) y {0} no es vacío: tiene un elemento, el 0.",
                "hints": [
                    "El vacío no tiene elementos, así que no hay ninguno que pueda faltar en A.",
                    "El complemento de U son los elementos de U que no están en U.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "∅ ⊂ A para cualquier conjunto A",
                            "El complemento de U es U",
                            "∅ ∈ {1; 2; 3}",
                            "{0} es el conjunto vacío",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== NÚMEROS REALES ====================
    {
        "slug": "al-reales-propiedades-combinados",
        "title": "Números reales: propiedades, periódicos y cálculos combinados",
        "summary": "Clasificar en IN, IN₀, Z, Q, II e IR, pasar periódicos a fracción, usar las propiedades con su nombre (y sus límites), resolver combinados y clasificar ecuaciones en ECD, ECI o EI.",
        "prerequisites": ["al-conjuntos-intervalos"],
        "insert_after": "al-conjuntos-intervalos",
        "metadata": {"section": "Álgebra 1", "lab_tab": "fractions", "est_minutes": 25},
        "items": [
            {
                "item_type": "recall",
                "title": "Conjuntos numéricos a los que pertenece el cero",
                "prompt": "Con la convención del ingreso (IN no incluye al 0), ¿a qué conjuntos numéricos pertenece el número 0?",
                "answer": "IN₀, Z, Q e IR: el 0 es entero, es racional (0 = 0/1) y es real. No pertenece a IN, porque en el ingreso IN = {1; 2; 3; …}, ni a II, porque Q ∩ II = { }.",
                "hints": [
                    "IN₀ = IN ∪ {0}.",
                    "Un número no puede ser racional e irracional a la vez.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["IN₀, Z, Q e IR", "IN, Z, Q e IR", "IN₀, Z e II", "Solo a IR"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Periódico mixto a fracción con la regla del ingreso",
                "prompt": "Pasá a fracción irreducible el número 1,23̂ (solo el 3 se repite: 1,2333…).",
                "answer": "37/30: numerador = número sin coma − número sin período = 123 − 12 = 111. Denominador: un 9 por la cifra periódica y un 0 por la cifra decimal no periódica = 90. Queda 111/90 = 37/30.",
                "hints": [
                    "El número sin período es lo que queda al borrar las cifras que se repiten: 12.",
                    "Contá: ¿cuántas cifras periódicas hay (nueves) y cuántas decimales NO periódicas (ceros)?",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["37/30", "41/30", "37/33", "123/100"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Sumar dos periódicos puros pasándolos a fracción",
                "prompt": "Calculá 0,3̂ + 0,6̂ (es decir, 0,333… + 0,666…) pasando cada número a fracción. Respondé solo con el número.",
                "answer": "1: 0,3̂ = 3/9 y 0,6̂ = 6/9, así que la suma es 9/9 = 1. Sumar los decimales truncados (0,333 + 0,666 = 0,999) hace creer que da menos que 1, pero 0,9̂ = 9/9 = 1.",
                "hints": ["Periódico puro: numerador = número sin coma − número sin período; denominador = un 9 por cada cifra periódica."],
                "payload": {"check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Respecto de qué operación se distribuye la potencia",
                "prompt": "Con a y b números reales, ¿cuál de estas igualdades se cumple SIEMPRE?",
                "answer": "(a . b)³ = a³ . b³: la potencia es distributiva respecto del producto (y del cociente), pero NO respecto de la suma. Contraejemplos: con a = 1 y b = 2, (1 + 2)² = 9 ≠ 1 + 4 = 5; √(9 + 16) = 5 ≠ 3 + 4 = 7; (1 + 1)⁻¹ = 1/2 ≠ 1 + 1 = 2.",
                "hints": [
                    "Para descartar una opción alcanza con UN contraejemplo: probá con números chicos.",
                    "Una raíz es una potencia de exponente fraccionario: sigue la misma regla.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "(a + b)² = a² + b²",
                            "(a . b)³ = a³ . b³",
                            "√(a + b) = √a + √b, con a ≥ 0 y b ≥ 0",
                            "(a + b)⁻¹ = a⁻¹ + b⁻¹, con a ≠ 0, b ≠ 0 y a + b ≠ 0",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Base negativa con y sin paréntesis",
                "prompt": "Calculá −2⁴ − (−2)³. Respondé solo con el número.",
                "answer": "−8: sin paréntesis el exponente afecta solo al 2, así que −2⁴ = −16. Con paréntesis, (−2)³ = −8 (base negativa, exponente impar). Queda −16 − (−8) = −16 + 8 = −8.",
                "hints": [
                    "−2⁴ significa −(2 . 2 . 2 . 2).",
                    "Restar un negativo es sumar su opuesto.",
                ],
                "payload": {"check": {"type": "numeric", "value": -8, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Potencia de exponente negativo con base fraccionaria",
                "prompt": "Calculá (2/5)⁻² − 2⁻¹. Respondé solo con el número.",
                "answer": "5,75 (= 23/4): (2/5)⁻² = (5/2)² = 25/4 y 2⁻¹ = 1/2. Entonces 25/4 − 2/4 = 23/4 = 5,75.",
                "hints": [
                    "a⁻ⁿ = (1/a)ⁿ: el exponente negativo invierte la base, no cambia el signo del resultado.",
                    "Para restar, pasá 1/2 a cuartos.",
                ],
                "payload": {"check": {"type": "numeric", "value": 5.75, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Resolver una fracción anidada escribiéndola en horizontal",
                "prompt": "Calculá la fracción anidada (1/2 + 1/3) / (1 − 1/(1 + 1/2)). Respondé solo con el número.",
                "answer": "2,5 (= 5/2): en horizontal es (1/2 + 1/3) : [1 − 1 : (1 + 1/2)]. Arriba: 1/2 + 1/3 = 5/6. Abajo: 1 + 1/2 = 3/2, 1 : 3/2 = 2/3 y 1 − 2/3 = 1/3. Finalmente 5/6 : 1/3 = 5/6 . 3 = 5/2.",
                "hints": [
                    "Reescribí cada línea de fracción con \":\" y encerrá numeradores y denominadores entre paréntesis.",
                    "Empezá por la fracción más chica, la del fondo: 1 + 1/2.",
                ],
                "payload": {"check": {"type": "numeric", "value": 2.5, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Combinado con periódico, raíz y exponente negativo",
                "prompt": "Calculá (1/2 − 1)⁻² − 3.√(1 − 0,8̂). Respondé solo con el número.",
                "answer": "3: hay dos términos. Primero: 1/2 − 1 = −1/2 y (−1/2)⁻² = (−2)² = 4. Segundo: 0,8̂ = 8/9, 1 − 8/9 = 1/9 y √(1/9) = 1/3, así que 3 . 1/3 = 1. Resultado: 4 − 1 = 3.",
                "hints": [
                    "Paso 1 del material: convertí el decimal periódico en fracción.",
                    "Separá en términos (los + y − que no están dentro de paréntesis) y resolvé cada uno por separado.",
                ],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Clasificar una ecuación que termina en 0.x = 0",
                "prompt": "Resolvé y clasificá la ecuación 4(x − 1) + 2 = 2(2x − 1).",
                "answer": "ECI, S = IR: aplicando distributiva queda 4x − 2 = 4x − 2, o sea 0.x = 0. Cualquier número real la verifica, así que tiene infinitas soluciones: es compatible indeterminada.",
                "hints": [
                    "Aplicá la distributiva en los dos miembros y pasá todas las x al primero.",
                    "0.x = 0 es una identidad; 0.x = k con k ≠ 0 es un absurdo.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["ECD, S = {0}", "ECI, S = IR", "EI, S = { }"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ecuación de primer grado con denominadores",
                "prompt": "Resolvé x/3 + (x + 2)/5 = 2. ¿Cuánto vale x? Respondé solo con el número.",
                "answer": "3: multiplicando ambos miembros por 15 (mcm de 3 y 5) queda 5x + 3(x + 2) = 30, es decir 8x + 6 = 30, 8x = 24 y x = 3. Es una ECD con S = {3}. Verificación: 3/3 + 5/5 = 2.",
                "hints": [
                    "Multiplicá TODOS los términos por el mcm de los denominadores.",
                    "El 3 que multiplica a (x + 2) se distribuye a los dos términos del paréntesis.",
                ],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    # ==================== RADICALES ====================
    {
        "slug": "al-radicales-operaciones",
        "title": "Radicales: extracción de factores, operaciones y racionalización",
        "summary": "Extraer factores con letras e índices 2 a 5, sumar radicales semejantes, multiplicar y dividir con distinto índice usando el mcm y racionalizar en los tres casos del material.",
        "prerequisites": ["al-exponentes-radicales"],
        "insert_after": "al-exponentes-radicales",
        "metadata": {"section": "Álgebra 1", "lab_tab": "powers", "est_minutes": 25},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Extraer factores de una raíz cúbica con letras",
                "prompt": "Extraé todos los factores posibles de ∛(54 x⁵ y⁷), con x > 0 e y > 0.",
                "answer": "3xy² ∛(2x²y): 54 = 2 . 3³. Dividiendo cada exponente por el índice 3: el 3³ sale como 3; x⁵ da cociente 1 y resto 2 (sale x, queda x²); y⁷ da cociente 2 y resto 1 (sale y², queda y). El 2 tiene exponente 1 < 3 y se queda adentro.",
                "hints": [
                    "Factorizá 54 en primos.",
                    "Exponente ÷ índice: el cociente es el exponente con que sale y el resto el exponente con que queda adentro.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["3xy² ∛(2x²y)", "3x²y ∛(2xy²)", "27xy² ∛(2x²y)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Exponente que queda dentro de una raíz cuarta",
                "prompt": "Al extraer factores de ⁴√(a¹⁸ m¹¹) (a > 0, m > 0), ¿con qué exponente queda m DENTRO de la raíz? Respondé solo con el número.",
                "answer": "3: 11 ÷ 4 da cociente 2 y resto 3, así que sale m² y queda m³. Para a: 18 ÷ 4 da cociente 4 y resto 2. Completo: ⁴√(a¹⁸ m¹¹) = a⁴ m² ⁴√(a² m³).",
                "hints": ["Hacé la división entera del exponente por el índice y mirá el resto."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Extraer factores de una raíz quinta",
                "prompt": "Extraé todos los factores posibles de ⁵√(64 b¹³), con b > 0.",
                "answer": "2b² ⁵√(2b³): 64 = 2⁶ = 2⁵ . 2, así que sale un 2 y queda un 2. Para b¹³: 13 ÷ 5 da cociente 2 y resto 3, sale b² y queda b³.",
                "hints": [
                    "Escribí 64 como potencia de 2 y compará su exponente con el índice 5.",
                    "El número también se extrae, no solo las letras.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["2b² ⁵√(2b³)", "2b³ ⁵√(2b²)", "2b² ⁵√(b³)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Suma algebraica de radicales que no parecen semejantes",
                "prompt": "Calculá √50 − √18 + √8.",
                "answer": "4√2: extrayendo factores, √50 = √(5² . 2) = 5√2, √18 = √(3² . 2) = 3√2 y √8 = √(2² . 2) = 2√2. Ahora son semejantes: (5 − 3 + 2)√2 = 4√2.",
                "hints": [
                    "Antes de decidir si se pueden sumar, extraé factores de cada raíz.",
                    "Solo se suman los coeficientes; el radical común queda igual (factor común).",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["4√2", "√40", "10√2"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Radicales que resultan semejantes después de extraer",
                "prompt": "Dos radicales son semejantes si tienen el mismo índice y el mismo radicando. ¿Qué par resulta de radicales semejantes después de extraer factores?",
                "answer": "√12 y √27: √12 = 2√3 y √27 = 3√3, los dos de índice 2 y radicando 3. En cambio √8 = 2√2 y ∛16 = 2∛2 tienen distinto índice, y √18 = 3√2 y √12 = 2√3 tienen distinto radicando.",
                "hints": ["Extraé factores de cada uno y recién ahí compará índice y radicando."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["√12 y √27", "√8 y ∛16", "√18 y √12"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Producto de radicales con distinto índice",
                "prompt": "Calculá √(2a) . ∛(4a²), con a > 0, y extraé todos los factores posibles.",
                "answer": "2a ⁶√(2a): el índice común es mcm(2; 3) = 6. √(2a) = ⁶√(2³a³) y ∛(4a²) = ∛(2²a²) = ⁶√(2⁴a⁴). Multiplicando: ⁶√(2⁷a⁷) = 2a ⁶√(2a).",
                "hints": [
                    "Para pasar a índice 6, multiplicá el índice y los exponentes del radicando por el mismo número.",
                    "Escribí 4 como 2² antes de amplificar.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["2a ⁶√(2a)", "⁵√(8a³)", "⁶√(8a³)", "2a² ⁶√(2a)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Cociente de radicales con distinto índice",
                "prompt": "Calculá ⁴√(x³) : √x, con x > 0.",
                "answer": "⁴√x: el índice común es mcm(4; 2) = 4 y √x = ⁴√(x²). Entonces ⁴√(x³) : ⁴√(x²) = ⁴√(x³ : x²) = ⁴√x.",
                "hints": ["Al amplificar √x a índice 4, el exponente del radicando también se multiplica por 2."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["⁴√x", "⁴√(x²)", "x"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Racionalizar con una raíz cuadrada en el denominador",
                "prompt": "Racionalizá el denominador de 10/(3√5) y simplificá.",
                "answer": "2√5/3: se multiplica numerador y denominador por √5 (1° caso). Queda 10√5/(3 . (√5)²) = 10√5/15 = 2√5/3.",
                "hints": [
                    "Multiplicá arriba y abajo solo por la raíz, no por el 3.",
                    "(√5)² = 5.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["2√5/3", "10√5/3", "2/3"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Racionalizar una raíz cuarta con dos factores",
                "prompt": "Racionalizá el denominador de 3/⁴√(x³y), con x > 0 e y > 0.",
                "answer": "3 ⁴√(xy³)/(xy): es el 2° caso. A x³ le falta x¹ para llegar al exponente 4 y a y¹ le falta y³, así que se multiplica arriba y abajo por ⁴√(xy³). Abajo queda ⁴√(x⁴y⁴) = xy.",
                "hints": [
                    "Buscá los exponentes que, sumados a los del denominador, den el índice 4.",
                    "Multiplicar por la misma raíz solo sirve con raíces cuadradas.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["3 ⁴√(xy³)/(xy)", "3 ⁴√(x³y)/(x³y)", "3 ⁴√(xy³)/(x⁴y⁴)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Racionalizar un binomio con el conjugado",
                "prompt": "Racionalizá el denominador de 4/(√7 − √3) y simplificá.",
                "answer": "√7 + √3: es el 3° caso; se multiplica por el conjugado √7 + √3. Abajo queda (√7)² − (√3)² = 7 − 3 = 4, que se simplifica con el 4 del numerador.",
                "hints": [
                    "Usá la diferencia de cuadrados: (a − b)(a + b) = a² − b².",
                    "El conjugado tiene los mismos términos con el signo del medio cambiado.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["√7 + √3", "√7 − √3", "2(√7 + √3)/5"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== VALOR ABSOLUTO: ECUACIONES E INECUACIONES ====================
    {
        "slug": "al-modulo-ecuaciones-inecuaciones",
        "title": "Valor absoluto: distancia, ecuaciones e inecuaciones modulares",
        "summary": "Calcular distancias en la recta, resolver |A| = k, |A| = |B| y |A| = expresión con x, inecuaciones |A| < k y |A| > k con respuesta en intervalos, y ecuaciones con potencias y raíces verificando.",
        "prerequisites": ["al-valor-absoluto-partes"],
        "insert_after": "al-valor-absoluto-partes",
        "metadata": {"section": "Álgebra 1", "lab_tab": "linear_eq", "est_minutes": 25},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Distancia entre dos puntos de la recta numérica",
                "prompt": "Sobre la recta numérica están los puntos A(−3,5) y B(4). ¿Cuánto vale d(A; B)? Respondé solo con el número.",
                "answer": "7,5: d(A; B) = |b − a| = |4 − (−3,5)| = |7,5| = 7,5. Da lo mismo restar al revés: |−3,5 − 4| = |−7,5| = 7,5. Una distancia nunca es negativa.",
                "hints": [
                    "d(A; B) es el valor absoluto de la diferencia de las coordenadas.",
                    "Restar −3,5 es sumar 3,5.",
                ],
                "payload": {"check": {"type": "numeric", "value": 7.5, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Despejar el módulo antes de aplicar la propiedad",
                "prompt": "¿Cuál es el conjunto solución de 7 + |3x − 1| = 4?",
                "answer": "S = { }: despejando, |3x − 1| = 4 − 7 = −3. Un valor absoluto nunca es negativo, así que ningún x verifica la ecuación.",
                "hints": ["Dejá el valor absoluto solo en un miembro y mirá el signo del otro."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["S = { }", "S = {−2/3; 4/3}", "S = IR"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ecuación modular con coeficiente fraccionario",
                "prompt": "Resolvé |x/2 + 1| = 3. ¿Cuál es la MENOR de las soluciones? Respondé solo con el número.",
                "answer": "−8: como 3 > 0, x/2 + 1 = 3 o x/2 + 1 = −3. La primera da x/2 = 2, x = 4; la segunda da x/2 = −4, x = −8. S = {−8; 4}.",
                "hints": [
                    "|A| = k con k > 0 se abre en dos ecuaciones: A = k o A = −k.",
                    "Para despejar x/2, multiplicá por 2.",
                ],
                "payload": {"check": {"type": "numeric", "value": -8, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Igualdad de dos valores absolutos",
                "prompt": "Resolvé |x − 5| = |3x + 1|.",
                "answer": "S = {−3; 1}: dos números tienen igual valor absoluto si son iguales u opuestos. x − 5 = 3x + 1 da x = −3; x − 5 = −(3x + 1) = −3x − 1 da 4x = 4, x = 1. Verificación: |−8| = |−8| y |−4| = |4|.",
                "hints": [
                    "|A| = |B| ⇔ A = B o A = −B.",
                    "En −(3x + 1) el signo menos afecta a los dos términos.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["S = {−3; 1}", "S = {−3}", "S = {−3; 3/2}"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Módulo igualado a una expresión con x",
                "prompt": "Resolvé |x − 2| = 3x − 10.",
                "answer": "S = {4}: el segundo miembro no puede ser negativo, así que hace falta 3x − 10 ≥ 0, o sea x ≥ 10/3. x − 2 = 3x − 10 da x = 4 (cumple). x − 2 = −(3x − 10) da 4x = 12, x = 3, que NO cumple la condición: |3 − 2| = 1 pero 3 . 3 − 10 = −1.",
                "hints": [
                    "Antes de abrir el módulo, planteá la condición: el segundo miembro debe ser ≥ 0.",
                    "Resolvé las dos ecuaciones y descartá las soluciones que no cumplan la condición.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["S = {4}", "S = {3; 4}", "S = {3}", "S = { }"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Inecuación modular de menor o igual con fracción",
                "prompt": "Resolvé |x/3 − 1| ≤ 2 y expresá el conjunto solución como intervalo.",
                "answer": "S = [−3; 9]: |A| ≤ 2 equivale a −2 ≤ x/3 − 1 ≤ 2. Sumando 1: −1 ≤ x/3 ≤ 3. Multiplicando por 3: −3 ≤ x ≤ 9. Los extremos entran por el ≤ (corchetes).",
                "hints": [
                    "|A| ≤ k ⇔ −k ≤ A ≤ k: se convierte en una desigualdad doble.",
                    "Lo que hagas a un miembro hacelo a los tres.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["[−3; 9]", "(−∞; −3] ∪ [9; ∞)", "[−1; 3]", "(−3; 9)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Inecuación modular de mayor con x negativa",
                "prompt": "Resolvé |4 − 2x| > 6 y expresá el conjunto solución con intervalos.",
                "answer": "S = (−∞; −1) ∪ (5; ∞): |A| > 6 equivale a 4 − 2x > 6 o 4 − 2x < −6. La primera: −2x > 2, y al dividir por −2 se invierte: x < −1. La segunda: −2x < −10, entonces x > 5.",
                "hints": [
                    "|A| > k ⇔ A > k o A < −k: quedan dos desigualdades separadas.",
                    "Dividir por un número negativo invierte el sentido de la desigualdad.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(−∞; −1) ∪ (5; ∞)", "(−1; 5)", "(−∞; −1] ∪ [5; ∞)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ecuación con potencia de exponente par",
                "prompt": "Resolvé (x − 2)² = 49.",
                "answer": "S = {−5; 9}: con exponente par, al sacar raíz aparece el valor absoluto: √((x − 2)²) = |x − 2| = 7. Entonces x − 2 = 7 (x = 9) o x − 2 = −7 (x = −5).",
                "hints": [
                    "√(A²) = |A|, no A.",
                    "Para despejar x en x − 2 = −7, sumá 2 en los dos miembros.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["S = {−5; 9}", "S = {9}", "S = {−9; 5}"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ecuación con potencia de exponente impar",
                "prompt": "Resolvé 2(x − 1)³ + 3 = −51. ¿Cuánto vale x? Respondé solo con el número.",
                "answer": "−2: 2(x − 1)³ = −54, (x − 1)³ = −27. Con índice impar la raíz conserva el signo y hay una sola solución: x − 1 = ∛(−27) = −3, entonces x = −2.",
                "hints": [
                    "Despejá primero la potencia: restá 3 y después dividí por 2.",
                    "La raíz cúbica de un negativo existe y es negativa.",
                ],
                "payload": {"check": {"type": "numeric", "value": -2, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Ecuación con raíz que no supera la verificación",
                "prompt": "Resolvé √(2x + 5) + 3 = 0 y verificá.",
                "answer": "S = { }: queda √(2x + 5) = −3, y una raíz cuadrada nunca da negativo. Si se eleva al cuadrado sin pensar, sale 2x + 5 = 9 y x = 2, pero al verificar √9 + 3 = 6 ≠ 0: es una solución falsa que apareció al elevar a potencia par.",
                "hints": [
                    "Despejá la raíz y mirá el signo del otro miembro.",
                    "Elevar a una potencia par puede agregar soluciones: verificá siempre en la ecuación original.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["S = { }", "S = {2}", "S = {−7}"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
]


INGRESO_MATH_A_LESSONS: dict[str, dict] = {
    "al-teoria-conjuntos": {
        "hook": {
            "question": "Se encuestó a 50 personas: 30 toman mate y 25 toman café, y todas toman al menos una de las dos cosas. ¿Cómo puede ser que 30 + 25 dé más que 50?",
            "intuition": "Porque hay gente que toma las dos cosas y la contaste dos veces. Si nadie quedó afuera, los que toman las dos son 30 + 25 − 50 = 5. Un **diagrama de Venn** hace visible esa zona compartida (la **intersección**) y evita el doble conteo.",
        },
        "concept": {
            "points": [
                "Un **conjunto** es una colección de objetos llamados **elementos**; se nombra con mayúscula y sus elementos van entre llaves. **Por extensión** se enumeran: `V = {a; e; i; o; u}`. **Por comprensión** se da la propiedad, con la barra \"/\" que se lee \"tal que\": `V = {x / x es una vocal}`.",
                "**Pertenencia** (`∈`, `∉`) vincula un ELEMENTO con un conjunto: `a ∈ V`. **Inclusión** (`⊂`, `⊄`) vincula un CONJUNTO con otro: `A ⊂ B` si todo elemento de A está en B, por ejemplo `{a; e} ⊂ V`.",
                "**Conjunto vacío** `∅` o `{ }`: no tiene elementos y está incluido en todo conjunto. **Conjunto universal** `U`: contiene todos los elementos de referencia; en el Venn es el rectángulo y cada conjunto es una curva cerrada dentro de él.",
                "**Unión** `A ∪ B`: los elementos de A o de B (los repetidos se escriben una vez). **Intersección** `A ∩ B`: los que están en los dos. Si `A ∩ B = { }`, A y B son **disjuntos**.",
                "**Complemento** `A̅` (en otros libros `Aᶜ`): los elementos de U que no están en A; `∅̅ = U` y `U̅ = ∅`. **Diferencia** `A − B`: los que están en A pero no en B. No es conmutativa: en general `A − B ≠ B − A` (con A = {1; 2} y B = {2}: A − B = {1} y B − A = { }).",
                "**Conteo con Venn**: completá primero la intersección y después cada parte \"solo A\" = total de A − intersección. Cantidad en la unión = total A + total B − intersección; los que no cumplen ninguna = total de U − cantidad en la unión.",
            ],
            "real_world": [
                {
                    "title": "Encuestas y estudios de mercado",
                    "detail": "Cuando una consultora informa cuántos usan una app, otra o ambas, arma un Venn: los porcentajes de cada app suman más de 100 % justamente por la intersección.",
                },
                {
                    "title": "Filtros y buscadores",
                    "detail": "Filtrar \"notebooks Y con 16 GB\" es una intersección, \"marca X O marca Y\" es una unión y \"excluir usados\" es un complemento. Las bases de datos de ingeniería trabajan con estas mismas operaciones.",
                },
                {
                    "title": "Geometría: puntos, rectas y planos",
                    "detail": "Un punto A de una recta r cumple `A ∈ r` (elemento), mientras que la recta contenida en el plano π cumple `r ⊂ π` (conjunto dentro de conjunto). Confundir los símbolos es un error clásico de examen.",
                },
            ],
            "key_rule": "∈ relaciona elemento con conjunto; ⊂ relaciona conjunto con conjunto | ∪ = \"o\", ∩ = \"y\", A̅ = \"no está en A\", A − B = \"está en A y no en B\" | En los conteos, completá primero la intersección.",
            "pitfall": "En un problema de conteo, poner en la zona \"solo A\" el total de A sin restar la intersección: los que cumplen las dos condiciones quedan contados dos veces. Otro error frecuente: escribir `2 ⊂ A` cuando 2 es un elemento (va `2 ∈ A`).",
        },
        "example": {
            "title": "Encuesta deportiva: quiénes practican solo uno y quiénes ninguno",
            "steps": [
                "Datos: en un curso de 45 estudiantes, 28 juegan al fútbol (F), 20 al vóley (V) y 9 a los dos. En el Venn, la intersección `F ∩ V` tiene 9.",
                "Solo fútbol: `28 − 9 = 19`. Solo vóley: `20 − 9 = 11`. Son las zonas `F − V` y `V − F`.",
                "Unión: `19 + 9 + 11 = 39` estudiantes juegan a algo (lo mismo que `28 + 20 − 9`).",
                "Ninguno de los dos: `45 − 39 = 6`. Es la cantidad de elementos del complemento de `F ∪ V`, la zona del rectángulo fuera de los círculos.",
                "Solo uno de los dos: `19 + 11 = 30`. Control: `30 + 9 + 6 = 45`, el total del curso.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Si `A = {2; 3; 5; 7}` y `B = {1; 3; 5; 7; 9}`, ¿cuánto es `A ∩ B`?",
            "options": [
                {"text": "`{3; 5; 7}`", "ok": True, "feedback": "Exacto: son los elementos que están en A y en B a la vez."},
                {"text": "`{1; 2; 3; 5; 7; 9}`", "ok": False, "feedback": "Eso es la unión A ∪ B: juntaste todo. La intersección pide estar en los dos conjuntos."},
                {"text": "`{2}`", "ok": False, "feedback": "Eso es A − B: lo que está en A pero no en B. La intersección es lo compartido."},
            ],
        },
        "checks": [
            {
                "question": "Con `U = {x ∈ IN / x < 9}` y `A = {2; 4; 6; 8}`, ¿cuánto es el complemento `A̅`?",
                "options": [
                    {"text": "`{1; 3; 5; 7}`", "ok": True, "feedback": "Exacto: U = {1; 2; …; 8} y quedan los elementos de U que no están en A."},
                    {"text": "`{1; 3; 5; 7; 9}`", "ok": False, "feedback": "El 9 no está en U: la condición es x < 9, no x ≤ 9. El complemento solo toma elementos del universo."},
                    {"text": "`{0; 1; 3; 5; 7}`", "ok": False, "feedback": "En el ingreso IN no incluye al 0, así que el 0 no está en U y no puede estar en el complemento."},
                ],
            },
            {
                "question": "En un grupo, 12 personas hablan inglés, 8 hablan portugués y 3 hablan los dos idiomas. Si todas hablan al menos uno, ¿cuántas personas hay?",
                "options": [
                    {"text": "17", "ok": True, "feedback": "Exacto: 12 + 8 − 3 = 17 (o 9 solo inglés + 3 los dos + 5 solo portugués)."},
                    {"text": "20", "ok": False, "feedback": "Sumaste 12 + 8 sin restar la intersección: las 3 personas bilingües quedaron contadas dos veces."},
                    {"text": "14", "ok": False, "feedback": "Restaste la intersección dos veces (12 + 8 − 6): a cada total se le resta una vez, o se resta 3 una sola vez a la suma."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras la diferencia entre ∈ y ⊂, y por qué en un diagrama de Venn conviene completar primero la intersección.",
    },
    "al-reales-propiedades-combinados": {
        "hook": {
            "question": "¿Es cierto que 0,999… (el 9 se repite sin fin) es un poquito menor que 1?",
            "intuition": "No: con la regla del ingreso para periódicos, `0,9̂ = 9/9 = 1`. Son dos escrituras del mismo número real. Pasar los periódicos a fracción evita estas trampas y hace exactos los cálculos combinados, que es lo primero que pide el material.",
        },
        "concept": {
            "points": [
                "**Conjuntos numéricos** (notación del ingreso): `IN = {1; 2; 3; …}` (sin el 0), `IN₀ = IN ∪ {0}`, `Z` enteros, `Q` cocientes `a/b` de enteros con `b ≠ 0` (enteros, fracciones, decimales exactos y periódicos), `II` irracionales (infinitas cifras decimales no periódicas: `√2`, `π`, `e`, `0,010010001…`) e `IR = Q ∪ II`, con `Q ∩ II = { }` e `IN ⊂ Z ⊂ Q ⊂ IR`. En otros temas de la app verás `ℕ, ℤ, ℚ, ℝ`: son los mismos conjuntos.",
                "**Periódico a fracción** (marcamos con ^ la cifra que se repite; el material usa un arco): numerador = número sin coma − número sin período; denominador = un 9 por cada cifra periódica seguido de un 0 por cada cifra decimal no periódica. Ejemplo: `2,34̂ = (234 − 23)/90 = 211/90`.",
                "**Propiedades con nombre**: asociativa, conmutativa, elemento neutro (0 en la suma, 1 en el producto), inverso aditivo u opuesto, inverso multiplicativo o recíproco (`a ≠ 0`), distributiva del producto respecto de la suma y elemento absorbente (`a . 0 = 0`). La **potencia y la raíz son distributivas respecto del producto y del cociente** (`(a . b)ⁿ = aⁿ . bⁿ`; con índice par, `ⁿ√(a . b) = ⁿ√a . ⁿ√b` si `a ≥ 0` y `b ≥ 0`), pero **NO respecto de la suma ni de la resta**. Un contraejemplo alcanza para probar que un enunciado es falso.",
                "**Potencias**: `a⁰ = 1` y `a⁻ⁿ = (1/a)ⁿ` (con `a ≠ 0`), así que `(a/b)⁻ⁿ = (b/a)ⁿ`. Si la base es negativa va entre paréntesis: `−5² = −25`, pero `(−5)² = 25`.",
                "**Combinados** (orden del material): pasar decimales a fracción, separar en términos (los `+` y `−` que no están dentro de paréntesis), resolver paréntesis y corchetes, después potencias y raíces, después productos y cocientes, y al final la suma algebraica. Las fracciones anidadas se reescriben en horizontal con `:` y paréntesis.",
                "**Ecuaciones de 1° grado según su conjunto solución**: solución única → **ECD** (`S = {…}`); si se llega a `0.x = 0` → **ECI** (`S = IR`); si se llega a `0.x = k` con `k ≠ 0` → **EI** (`S = { }`).",
            ],
            "real_world": [
                {
                    "title": "Dividir una cuenta entre tres",
                    "detail": "$ 100 entre 3 personas da 33,3̂ cada una. Como fracción, 100/3 es exacto; al redondear a centavos queda $ 33,33 y, si sumás tres veces ese redondeo, te falta un centavo.",
                },
                {
                    "title": "La diagonal de una baldosa",
                    "detail": "En una baldosa cuadrada de 1 m de lado la diagonal mide √2 m, un irracional: en la obra se usa 1,41 m, pero en el cálculo conviene arrastrar √2 exacto hasta el final.",
                },
                {
                    "title": "Fórmulas en planillas de cálculo",
                    "detail": "En una planilla, `=1/2+1/3` y `=(1/2+1)/3` dan resultados distintos: el programa respeta la jerarquía de operaciones igual que en un combinado, y un paréntesis olvidado cambia el resultado.",
                },
            ],
            "key_rule": "Potencia y raíz se distribuyen en productos y cocientes, nunca en sumas o restas | a⁻ⁿ = (1/a)ⁿ | Periódico: (número sin coma − número sin período) / (un 9 por cifra periódica y un 0 por cifra decimal no periódica) | 0.x = 0 → ECI, S = IR; 0.x = k (k ≠ 0) → EI, S = { }.",
            "pitfall": "Distribuir el cuadrado en una suma: `(3 + 4)² = 49`, no `9 + 16 = 25`. Y con exponente negativo, cambiar el signo en lugar de invertir la base: `2⁻³ = 1/8`, no `−8`.",
        },
        "example": {
            "title": "Combinado con fracción anidada y exponente negativo",
            "steps": [
                "Calcular `(3/4 − 1/2) / (1 − 1/(1 + 1/3)) + (2/3)⁻²`. En horizontal: `(3/4 − 1/2) : [1 − 1 : (1 + 1/3)] + (2/3)⁻²`. Hay dos términos.",
                "Paréntesis: `3/4 − 1/2 = 3/4 − 2/4 = 1/4` y `1 + 1/3 = 4/3`.",
                "Corchete: `1 : 4/3 = 3/4` y `1 − 3/4 = 1/4`.",
                "Potencia: `(2/3)⁻² = (3/2)² = 9/4` (el exponente negativo invierte la base).",
                "Cociente y suma: `1/4 : 1/4 = 1`, y `1 + 9/4 = 13/4`.",
            ],
            "lab_link": "math:fractions",
            "lab_cta": "Practicar fracciones en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál de estos números pertenece a II (irracionales)?",
            "options": [
                {"text": "`0,1010010001…` (cada vez un 0 más)", "ok": True, "feedback": "Exacto: tiene infinitas cifras decimales y no hay un bloque que se repita, así que no es periódico."},
                {"text": "`0,151515…` (se repite 15)", "ok": False, "feedback": "Es periódico, entonces es racional: vale 15/99 = 5/33."},
                {"text": "`√81`", "ok": False, "feedback": "81 es un cuadrado perfecto: √81 = 9, un número natural (y por lo tanto racional)."},
            ],
        },
        "checks": [
            {
                "question": "Al resolver `2(x + 3) = 2x + 5`, ¿qué tipo de ecuación es?",
                "options": [
                    {"text": "EI, `S = { }`", "ok": True, "feedback": "Exacto: queda 2x + 6 = 2x + 5, o sea 0.x = −1, un absurdo. Ningún x la verifica."},
                    {"text": "ECI, `S = IR`", "ok": False, "feedback": "Que se cancelen las x no alcanza: hay que mirar lo que queda. 0.x = −1 es falso para todo x; ECI sería si quedara 0 = 0."},
                    {"text": "ECD, `S = {0}`", "ok": False, "feedback": "Que la x desaparezca no significa que x valga 0: con x = 0 queda 6 = 5, que es falso."},
                ],
            },
            {
                "question": "¿Cuánto vale `(1/3)⁻²`?",
                "options": [
                    {"text": "9", "ok": True, "feedback": "Exacto: (1/3)⁻² = 3² = 9. El exponente negativo invierte la base."},
                    {"text": "−9", "ok": False, "feedback": "El exponente negativo no cambia el signo del resultado: invierte la base. (1/3)⁻² = 3² = 9."},
                    {"text": "1/9", "ok": False, "feedback": "Eso es (1/3)²: elevaste al cuadrado pero no invertiste la base."},
                ],
            },
        ],
        "takeaway_prompt": "Inventá un contraejemplo propio que muestre que la potencia no se distribuye respecto de la suma, y explicá cómo reconocés si una ecuación es ECI o EI.",
    },
    "al-radicales-operaciones": {
        "hook": {
            "question": "Un cuadrado tiene 50 cm² de área. ¿Cuánto mide su lado, escrito en forma exacta y sin calculadora?",
            "intuition": "El lado es `√50`, y como `50 = 5² . 2`, se puede sacar el 5 afuera: `√50 = 5√2` cm (≈ 7,07 cm). Extraer factores, sumar solo lo semejante y sacar las raíces del denominador son las tres herramientas para dejar cualquier radical en su forma más simple.",
        },
        "concept": {
            "points": [
                "**Extracción de factores**: se factoriza el radicando y sale todo factor con exponente **mayor o igual que el índice**. Regla rápida: se divide cada exponente por el índice; el **cociente** es el exponente con que sale y el **resto** el exponente con que queda adentro: `⁴√(a¹⁶m²³) = a⁴m⁵ ⁴√(m³)`. Trabajamos con letras positivas, como en el material (con índice par, `√(a²) = |a|`).",
                "**Radicales semejantes**: mismo índice y mismo radicando. Solo ellos se suman o restan, sacando factor común el radical: `3√2 − √2/4 − √2/2 = (3 − 1/4 − 1/2)√2 = (9/4)√2`. Si no parecen semejantes, primero extraé factores: `√8 − √32 = 2√2 − 4√2 = −2√2`.",
                "**Producto y cociente con igual índice**: se mete todo en una sola raíz (`ⁿ√a . ⁿ√b = ⁿ√(a . b)`), se simplifica y se extrae. **Con distinto índice**: el índice común es el **mcm** de los índices, y cada raíz se amplifica multiplicando su índice y los exponentes del radicando por el mismo número: `∛(2a²) = ¹⁵√(2⁵a¹⁰)`.",
                "**Racionalizar** es transformar el cociente en otro equivalente con denominador racional. **1° caso** (un término con raíz cuadrada): multiplicar numerador y denominador por esa raíz. **2° caso** (un término con raíz no cuadrada `ⁿ√(aᵏ…)`): multiplicar por `ⁿ√(aⁿ⁻ᵏ…)` para que cada exponente llegue al índice; si algún exponente ya es mayor o igual que el índice, conviene extraer antes.",
                "**3° caso** (dos términos con al menos una raíz cuadrada): multiplicar por el **conjugado**, que tiene los mismos términos con el signo del medio cambiado, y usar la diferencia de cuadrados `(a + b)(a − b) = a² − b²`: `3/(√5 + √2) = 3(√5 − √2)/(5 − 2) = √5 − √2`.",
            ],
            "real_world": [
                {
                    "title": "Velocidad de caída libre",
                    "detail": "Un objeto que cae desde 5 m llega con `v = √(2 . 9,8 . 5) = √98 = 7√2 ≈ 9,9 m/s`. Extraer el 7 deja la expresión lista para seguir operando sin arrastrar redondeos.",
                },
                {
                    "title": "Tensión eficaz de la red eléctrica",
                    "detail": "La tensión eficaz es `V_ef = V_máx/√2`, que racionalizada queda `V_máx . √2/2`. Con un pico de 311 V da unos 220 V, el valor de los enchufes.",
                },
                {
                    "title": "Diagonales en planos y estructuras",
                    "detail": "La diagonal de un cuadrado de lado ℓ es `ℓ√2` y la de un cubo `ℓ√3`. Al sumar barras de una estructura aparecen sumas de radicales semejantes como `3√2 + 5√2 = 8√2`.",
                },
            ],
            "key_rule": "Sale de la raíz todo factor con exponente ≥ índice (cociente afuera, resto adentro) | Solo se suman radicales semejantes | Distinto índice → índice común con el mcm | Racionalizar: √a → por √a; ⁿ√(aᵏ) → por ⁿ√(aⁿ⁻ᵏ); binomio con raíz cuadrada → por el conjugado.",
            "pitfall": "Sumar radicandos: `√9 + √16 = 3 + 4 = 7`, no `√25 = 5`. Y en el 2° caso, multiplicar por la misma raíz como si fuera cuadrada: `∛2 . ∛2 = ∛4`, que sigue siendo irracional.",
        },
        "example": {
            "title": "Simplificar √18 + √50 − 4/√2",
            "steps": [
                "Extraer factores: `18 = 3² . 2` y `50 = 5² . 2`, así que `√18 = 3√2` y `√50 = 5√2`.",
                "Racionalizar el tercer término (1° caso): `4/√2 . √2/√2 = 4√2/(√2)² = 4√2/2 = 2√2`.",
                "Los tres radicales son semejantes (índice 2, radicando 2): factor común `√2` → `(3 + 5 − 2)√2 = 6√2`.",
                "Control con calculadora: `√18 + √50 − 4/√2 ≈ 4,243 + 7,071 − 2,828 = 8,486` y `6√2 ≈ 8,485`; la diferencia es solo de redondeo.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "¿Cuánto da `√75 − √12`?",
            "options": [
                {"text": "`3√3`", "ok": True, "feedback": "Exacto: √75 = √(5² . 3) = 5√3 y √12 = √(2² . 3) = 2√3; entonces (5 − 2)√3 = 3√3."},
                {"text": "`√63`", "ok": False, "feedback": "Restaste los radicandos (75 − 12). Las raíces no se distribuyen en la resta: primero extraé factores y operá con los coeficientes."},
                {"text": "`7√3`", "ok": False, "feedback": "Extrajiste bien (5√3 y 2√3) pero sumaste los coeficientes: la operación es una resta, 5 − 2 = 3."},
            ],
        },
        "checks": [
            {
                "question": "Para racionalizar `5/∛(x²)` (con x > 0), ¿por qué expresión multiplicás numerador y denominador?",
                "options": [
                    {"text": "`∛x`", "ok": True, "feedback": "Exacto: a x² le falta x¹ para llegar al índice 3, y ∛(x²) . ∛x = ∛(x³) = x."},
                    {"text": "`∛(x²)`", "ok": False, "feedback": "Eso funciona con raíces cuadradas. Acá ∛(x²) . ∛(x²) = ∛(x⁴) = x∛x, y la raíz sigue en el denominador."},
                    {"text": "`√x`", "ok": False, "feedback": "Las raíces tienen distinto índice y no se combinan así: hay que multiplicar por otra raíz cúbica."},
                ],
            },
            {
                "question": "Para racionalizar `2/(3 + √5)`, ¿por qué expresión multiplicás numerador y denominador?",
                "options": [
                    {"text": "`3 − √5`", "ok": True, "feedback": "Exacto: es el conjugado. (3 + √5)(3 − √5) = 9 − 5 = 4, un número racional."},
                    {"text": "`√5`", "ok": False, "feedback": "Así queda (3 + √5)√5 = 3√5 + 5, que sigue teniendo raíz. Con dos términos hace falta el conjugado (3° caso)."},
                    {"text": "`3 + √5`", "ok": False, "feedback": "Es el mismo binomio: (3 + √5)² = 14 + 6√5, todavía irracional. Hay que cambiar el signo del medio."},
                ],
            },
        ],
        "takeaway_prompt": "Contá con tus palabras cómo decidís cuál de los tres casos de racionalización usar y qué factor elegís en cada uno.",
    },
    "al-modulo-ecuaciones-inecuaciones": {
        "hook": {
            "question": "Una pieza debe medir 15 cm y se rechaza si su longitud difiere de 15 cm en más de 0,2 cm. ¿Qué longitudes se aceptan?",
            "intuition": "\"Diferir\" es una distancia, y la distancia se mide con valor absoluto: se acepta si `|L − 15| ≤ 0,2`, o sea `14,8 ≤ L ≤ 15,2`. En intervalo: `[14,8; 15,2]`. Las inecuaciones modulares traducen tolerancias como esta.",
        },
        "concept": {
            "points": [
                "`|x| = x` si `x ≥ 0` y `|x| = −x` si `x < 0`. Geométricamente, `|x|` es la distancia de x al origen. Entre dos puntos A(a) y B(b): `d(A; B) = |b − a| = |a − b|`, que nunca es negativa.",
                "**|A| = k**: si `k > 0`, `A = k` o `A = −k` (dos ecuaciones); si `k = 0`, `A = 0` (una sola solución); si `k < 0`, `S = { }`. Primero dejá el módulo solo en un miembro: `7 + |3x − 1| = 4` lleva a `|3x − 1| = −3`.",
                "**|A| = |B|** ⇔ `A = B` o `A = −B`. **|A| = expresión con x**: el segundo miembro no puede ser negativo, así que se plantea esa condición, se resuelven las dos ecuaciones y se descartan las soluciones que no la cumplen (verificando).",
                "**Inecuaciones** (con `a > 0`): `|x| < a ⇔ −a < x < a` (un intervalo acotado) y `|x| > a ⇔ x < −a o x > a` (unión de dos intervalos no acotados); con `≤` y `≥` los extremos entran. Al multiplicar o dividir por un negativo se invierte la desigualdad. La respuesta va con punto y coma, `S = (−∞; 4) ∪ (6; ∞)`; en otros temas de la app verás la coma, `(−∞, 4)`: es lo mismo.",
                "**Potencias y raíces**: con exponente **par**, `Aⁿ = c` (c > 0) da `|A| = ⁿ√c` y dos soluciones (±); con exponente **impar** hay una sola solución y la raíz conserva el signo. Al elevar a una potencia par para eliminar una raíz pueden aparecer soluciones falsas: **verificá siempre** en la ecuación original.",
            ],
            "real_world": [
                {
                    "title": "Tolerancias de fabricación",
                    "detail": "Un eje de 15 cm con tolerancia de 0,2 cm se acepta si `|L − 15| ≤ 0,2`. Los planos de ingeniería indican cotas como `15 ± 0,2`, que es exactamente esta inecuación.",
                },
                {
                    "title": "Control de temperatura",
                    "detail": "Una cámara que debe estar a 20 °C con un margen de 2 °C cumple `|T − 20| ≤ 2`, es decir `T ∈ [18; 22]`. Un termostato aplica justamente esa condición.",
                },
                {
                    "title": "Posiciones en Física",
                    "detail": "Si un móvil está en x = −3,5 m y otro en x = 4 m sobre el mismo eje, la distancia entre ellos es `|4 − (−3,5)| = 7,5 m`, sin importar cuál esté a la izquierda.",
                },
            ],
            "key_rule": "|A| = k: dos soluciones si k > 0, una si k = 0, ninguna si k < 0 | |A| < k → −k < A < k | |A| > k → A < −k o A > k | Exponente par → ±; impar → una solución | Si elevaste a una potencia par, verificá.",
            "pitfall": "En `|5 − x| > 1`, olvidarse de invertir la desigualdad al despejar `−x`. O, en `|A| = 2x − 3`, aceptar las dos soluciones sin comprobar que el segundo miembro sea no negativo.",
        },
        "example": {
            "title": "Resolver |3 − x/2| ≥ 2 y expresar S con intervalos",
            "steps": [
                "Es de la forma `|A| ≥ k` con `k = 2 > 0`: equivale a `3 − x/2 ≥ 2` o `3 − x/2 ≤ −2`.",
                "Primera: `−x/2 ≥ −1`. Multiplicando por −2 se invierte la desigualdad: `x ≤ 2`.",
                "Segunda: `−x/2 ≤ −5`. Multiplicando por −2 se invierte: `x ≥ 10`.",
                "Unión con corchetes, porque el `≥` incluye los extremos: `S = (−∞; 2] ∪ [10; ∞)`.",
                "Control: `x = 0` da `|3| = 3 ≥ 2` (está en S); `x = 6` da `|0| = 0`, que no cumple (queda afuera); `x = 10` da `|3 − 5| = 2` (extremo incluido).",
            ],
            "lab_link": "math:linear_eq",
            "lab_cta": "Practicar despejes en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es el conjunto solución de `|x + 2| < 5`?",
            "options": [
                {"text": "`(−7; 3)`", "ok": True, "feedback": "Exacto: −5 < x + 2 < 5; restando 2 a los tres miembros queda −7 < x < 3."},
                {"text": "`(−∞; −7) ∪ (3; ∞)`", "ok": False, "feedback": "Esa es la solución de |x + 2| > 5. Con \"<\" los números quedan cerca del centro: es un solo intervalo acotado."},
                {"text": "`(−3; 7)`", "ok": False, "feedback": "Sumaste 2 en lugar de restarlo: para despejar x de x + 2 hay que restar 2 en los tres miembros."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuántas soluciones tiene `|5x − 1| = 0`?",
                "options": [
                    {"text": "Una: `x = 1/5`", "ok": True, "feedback": "Exacto: el valor absoluto vale 0 solo si lo de adentro es 0, así que 5x − 1 = 0 y x = 1/5."},
                    {"text": "Dos: `x = 1/5` y `x = −1/5`", "ok": False, "feedback": "Aplicaste el ± como si k fuera positivo. 5x − 1 = −0 es la misma ecuación 5x − 1 = 0, y x = −1/5 da |−2| = 2 ≠ 0."},
                    {"text": "Ninguna, porque un valor absoluto no puede valer 0", "ok": False, "feedback": "El valor absoluto nunca es NEGATIVO, pero sí puede valer 0: |0| = 0. Sin solución es el caso k < 0."},
                ],
            },
            {
                "question": "¿Cuál es el conjunto solución de `(x − 1)³ = −8`?",
                "options": [
                    {"text": "`S = {−1}`", "ok": True, "feedback": "Exacto: con exponente impar hay una sola solución. x − 1 = ∛(−8) = −2, así que x = −1."},
                    {"text": "`S = {−1; 3}`", "ok": False, "feedback": "Pusiste ± como con exponente par. Con x = 3: (3 − 1)³ = 8 ≠ −8."},
                    {"text": "`S = { }`", "ok": False, "feedback": "La raíz de índice impar de un negativo existe: ∛(−8) = −2. Las que no existen en IR son las de índice par."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras por qué |x| < a da un solo intervalo y |x| > a da dos, y en qué casos tenés que verificar las soluciones.",
    },
}
