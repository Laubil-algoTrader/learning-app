"""Física del ingreso UNCuyo 2027, Unidad 1 (Sistemas de unidades).

Tres nodos que se intercalan después de `f-intro-fisica` mediante `insert_after`:
  - Sistemas de unidades: SI, c.g.s., técnico y fracciones unitarias
  - Medición, cifras significativas, redondeo y notación científica
  - Ecuaciones de dimensión y homogeneidad

Siguen la notación del material del curso (Guía TP1 partes A y B, clase de la Unidad 1 y
apunte del Ing. Vallone): coma decimal, producto con punto (kg.m/s², 1,23.10³), dina, utm, kgf.
"""

from __future__ import annotations

INGRESO_PHYSICS_A_NODES: list[dict] = [
    # ==================== SISTEMAS DE UNIDADES ====================
    {
        "slug": "f-sistemas-unidades",
        "title": "Sistemas de unidades: SI, c.g.s., técnico y fracciones unitarias",
        "summary": "Distinguir magnitudes fundamentales y derivadas en el SIMELA, el c.g.s. y el técnico, y convertir unidades con fracciones unitarias.",
        "prerequisites": ["f-intro-fisica"],
        "insert_after": "f-intro-fisica",
        "metadata": {"section": "Cinemática y base", "lab_tab": "kinematics", "est_minutes": 30},
        "items": [
            {
                "item_type": "recall",
                "title": "Magnitudes fundamentales del sistema técnico español",
                "prompt": "En el SIMELA las magnitudes de base de la mecánica son longitud, masa y tiempo. ¿Cuáles son las magnitudes fundamentales del sistema técnico español?",
                "answer": "Longitud, fuerza y tiempo (dimensiones L, F, T), con unidades m, kgf y s. En el sistema técnico la fuerza es fundamental y la masa pasa a ser derivada: su unidad, la utm, se obtiene de m = F/a.",
                "hints": ["En este sistema la unidad estrella es el kilogramo fuerza (kgf).", "Una de las magnitudes que en el SI es de base acá es derivada."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Longitud, masa y tiempo",
                            "Longitud, fuerza y tiempo",
                            "Fuerza, masa y tiempo",
                            "Longitud, masa y fuerza",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Unidad técnica de masa en kgf, m y s",
                "prompt": "En el sistema técnico la masa es derivada y se define con m = F/a. ¿A qué combinación de kgf, m y s equivale 1 utm (unidad técnica de masa)?",
                "answer": "1 utm = 1 kgf.s²/m: m = F/a, y dividir kgf por m/s² es multiplicar por s²/m. Como 1 kgf = 9,8 N, resulta 1 utm = 9,8 kg.",
                "hints": ["Reemplazá F por kgf y a por m/s² en m = F/a.", "Dividir por una fracción es multiplicar por la recíproca."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["kgf.s²/m", "kgf.m/s²", "kgf/m", "kg.m/s²"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Unidad de fuerza en el SI, el c.g.s. y el técnico",
                "prompt": "¿Cuál es la terna de unidades de FUERZA en el SI, el c.g.s. y el sistema técnico, en ese orden?",
                "answer": "N, dina (dyn) y kgf: newton = kg.m/s², dina = g.cm/s² (ambas derivadas) y kilogramo fuerza, que en el técnico es unidad fundamental. kg, g y utm son unidades de masa; J, erg y kgm son de trabajo.",
                "hints": ["La fuerza es masa por aceleración: en el SI, kg.m/s²; en el c.g.s., g.cm/s².", "kg, g y utm miden otra magnitud."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["N, dyn y kgf", "kg, g y utm", "J, erg y kgm", "N, kgf y dyn"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Pasar 90 km/h a m/s con fracciones unitarias",
                "prompt": "Un auto va a 90 km/h. Expresá esa velocidad en m/s usando fracciones unitarias. Respondé solo con el número (en m/s).",
                "answer": "25 m/s: 90 km/h . (1000 m / 1 km) . (1 h / 3600 s) = 90 000 m / 3600 s = 25 m/s. Los km se simplifican con los km y las h con las h.",
                "hints": ["Usá 1 km = 1000 m y 1 h = 3600 s.", "Cada fracción tiene que dejar arriba la unidad nueva y abajo la que querés cancelar."],
                "payload": {"check": {"type": "numeric", "value": 25, "tolerance": 0, "unit": "m/s"}},
            },
            {
                "item_type": "worked_example",
                "title": "Densidad del aluminio de g/cm³ a kg/m³",
                "prompt": "La densidad del aluminio es 2,7 g/cm³. Expresala en kg/m³ con fracciones unitarias. Respondé solo con el número (en kg/m³).",
                "answer": "2700 kg/m³: 2,7 g/cm³ . (1 kg / 1000 g) . (100 cm / 1 m)³ = 2,7 . 1 000 000 / 1000 kg/m³ = 2700 kg/m³. La fracción de longitud se eleva al cubo porque los cm están al cubo.",
                "hints": ["Necesitás dos fracciones: una para la masa y otra para el volumen.", "(100 cm / 1 m)³ = 1 000 000 cm³ / 1 m³."],
                "payload": {"check": {"type": "numeric", "value": 2700, "tolerance": 0, "unit": "kg/m³"}},
            },
            {
                "item_type": "worked_example",
                "title": "Pasar un área de m² a cm²",
                "prompt": "Una placa tiene 2,5 m² de superficie. ¿Cuántos cm² son? Respondé solo con el número (en cm²).",
                "answer": "25 000 cm²: 2,5 m² . (100 cm / 1 m)² = 2,5 . 10 000 cm² = 25 000 cm² (2,5.10⁴ cm² en notación científica). Multiplicar solo por 100 sería tratar el área como si fuera una longitud.",
                "hints": ["La equivalencia de longitud 1 m = 100 cm se eleva al cuadrado.", "1 m² = 10 000 cm²."],
                "payload": {"check": {"type": "numeric", "value": 25000, "tolerance": 0, "unit": "cm²"}},
            },
            {
                "item_type": "worked_example",
                "title": "Presión de kgf/cm² a pascal",
                "prompt": "Un manómetro marca 2 kgf/cm². Expresá esa presión en Pa (Pa = N/m²), con 1 kgf = 9,8 N. Respondé solo con el número (en Pa).",
                "answer": "196 000 Pa: 2 kgf/cm² . (9,8 N / 1 kgf) . (100 cm / 1 m)² = 2 . 9,8 . 10 000 N/m² = 196 000 Pa (1,96.10⁵ Pa).",
                "hints": ["Una fracción cambia kgf por N y otra cambia cm² por m².", "Ojo: 1 m² = 10 000 cm², así que los cm² de abajo se convierten multiplicando por 10 000."],
                "payload": {"check": {"type": "numeric", "value": 196000, "tolerance": 0, "unit": "Pa"}},
            },
            {
                "item_type": "worked_example",
                "title": "Libra fuerza a newton en cadena",
                "prompt": "Pasá 50 lbf a newtons encadenando fracciones unitarias, con 1 lbf = 0,454 kgf y 1 kgf = 9,8 N. Respondé solo con el número (en N, podés redondear a la décima).",
                "answer": "222,46 N (≈ 222,5 N): 50 lbf . (0,454 kgf / 1 lbf) . (9,8 N / 1 kgf) = 22,7 kgf . 9,8 N/kgf = 222,46 N.",
                "hints": ["Primero pasá de lbf a kgf y después de kgf a N.", "50 . 0,454 = 22,7."],
                "payload": {"check": {"type": "numeric", "value": 222.46, "tolerance": 0.003, "unit": "N"}},
            },
            {
                "item_type": "worked_example",
                "title": "Kilogramo fuerza a dinas",
                "prompt": "¿A cuántas dinas (dyn) equivale una fuerza de 3 kgf? Usá 1 kgf = 9,8 N y 1 N = 10⁵ dyn. Respondé solo con el número (en dyn).",
                "answer": "2 940 000 dyn (2,94.10⁶ dyn): 3 kgf . (9,8 N / 1 kgf) . (10⁵ dyn / 1 N) = 29,4 N . 10⁵ dyn/N = 2,94.10⁶ dyn.",
                "hints": ["Pasá primero a newtons.", "Multiplicar por 10⁵ es correr la coma cinco lugares a la derecha."],
                "payload": {"check": {"type": "numeric", "value": 2940000, "tolerance": 0, "unit": "dyn"}},
            },
            {
                "item_type": "recall",
                "title": "Escritura correcta de un símbolo según el SIMELA",
                "prompt": "Según las reglas del SIMELA, ¿cuál de estas cantidades está bien escrita?",
                "answer": "25 kg. Los símbolos no son abreviaturas: no llevan punto ni s de plural. Además, el prefijo kilo se escribe con k minúscula (los prefijos desde mega para arriba —M, G, T, P, E…— van en mayúscula; de kilo para abajo, en minúscula).",
                "hints": ["Pensá en los símbolos como letras de un código, no como palabras abreviadas.", "¿Qué prefijos se escriben con mayúscula?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["25 kg", "25 Kg", "25 kg.", "25 kgs"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== CIFRAS SIGNIFICATIVAS ====================
    {
        "slug": "f-cifras-significativas",
        "title": "Medición, cifras significativas, redondeo y notación científica",
        "summary": "Contar cifras significativas, redondear, operar con cantidades medidas y elegir notación científica o un prefijo adecuado.",
        "prerequisites": ["f-sistemas-unidades"],
        "insert_after": "f-sistemas-unidades",
        "metadata": {"section": "Cinemática y base", "lab_tab": "kinematics", "est_minutes": 30},
        "items": [
            {
                "item_type": "recall",
                "title": "Contar cifras significativas con ceros a ambos lados",
                "prompt": "¿Cuántas cifras significativas tiene la medición 0,00250 m? Respondé solo con el número.",
                "answer": "3: el 2, el 5 y el 0 final. Los ceros que están después de la coma pero antes del primer dígito distinto de cero no son significativos (solo ubican la coma); el cero escrito a la derecha del 5 sí lo es.",
                "hints": ["Los ceros del principio solo marcan dónde va la coma.", "Un cero escrito al final de un número medido cuenta."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Cifras significativas de 3 600 s según el curso",
                "prompt": "En la guía del ingreso aparece '3 600 s, número de segundos en una hora'. Con el criterio del curso, ¿cuántas cifras significativas tiene 3 600 s? Respondé solo con el número.",
                "answer": "4: el material establece que los ceros, si están escritos, son significativos (lo mismo da 6 000 K → 4 cifras). Si se quisiera informar solo 2 cifras habría que escribir 3,6.10³ s.",
                "hints": ["Regla del apunte: los ceros a la derecha del último dígito distinto de cero son significativos.", "Para mostrar menos cifras se usa notación científica."],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Redondear 22478 a tres cifras significativas",
                "prompt": "¿Cómo se expresa 22478 con solo 3 cifras significativas?",
                "answer": "2,25.10⁴: se corta después del tercer dígito (224|78). El primer dígito que se descarta es 7, mayor que 4, así que el 4 sube a 5. Hace falta la notación científica para no agregar ceros que contarían como cifras.",
                "hints": ["Mirá el primer dígito que queda afuera del corte.", "Si es mayor que 4, el último dígito que conservás aumenta en uno."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["2,25.10⁴", "2,24.10⁴", "225", "2,2478.10⁴"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Sumar longitudes medidas con distintos decimales",
                "prompt": "Sumá 18,425 cm + 7,21 cm + 5,0 cm aplicando la regla de la suma del cálculo aproximado. Respondé solo con el número (en cm), con las cifras que corresponden.",
                "answer": "30,6 cm: la calculadora da 30,635, pero 5,0 cm tiene un solo decimal, así que el resultado se informa con un decimal. El dígito siguiente es 3 (menor o igual que 4) y el 6 queda igual. Redondeando antes cada sumando: 18,4 + 7,2 + 5,0 = 30,6.",
                "hints": ["En sumas y restas manda la cantidad de DECIMALES, no la de cifras significativas.", "Buscá el sumando con menos decimales."],
                "payload": {"check": {"type": "numeric", "value": 30.6, "tolerance": 0, "unit": "cm"}},
            },
            {
                "item_type": "worked_example",
                "title": "Área de una mesada con cifras significativas",
                "prompt": "Una mesada mide 4,52 m por 2,1 m. Calculá su área aplicando la regla del producto del cálculo aproximado. Respondé solo con el número (en m²).",
                "answer": "9,5 m²: 4,52 . 2,1 = 9,492, pero 2,1 tiene solo 2 cifras significativas, así que el resultado se informa con 2. El dígito descartado es 9, entonces 9,4 sube a 9,5.",
                "hints": ["En productos y cocientes manda la cantidad de CIFRAS SIGNIFICATIVAS.", "El factor 'más pobre' es el que tiene menos cifras."],
                "payload": {"check": {"type": "numeric", "value": 9.5, "tolerance": 0, "unit": "m²"}},
            },
            {
                "item_type": "worked_example",
                "title": "Producto con un factor de una sola cifra significativa",
                "prompt": "¿Cómo se informa el resultado de 1023 x 0,3 respetando las cifras significativas?",
                "answer": "3.10²: 1023 . 0,3 = 306,9, y 0,3 tiene una sola cifra significativa, así que el resultado lleva una. Escribir 300 no sirve: con el criterio del curso, los ceros escritos son significativos y 300 tendría 3 cifras.",
                "hints": ["Contá las cifras significativas de 0,3.", "¿Cómo se escribe 'unos trescientos' con una sola cifra significativa?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["3.10²", "300", "306,9"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Operación combinada: producto y después suma",
                "prompt": "Resolvé (2,4 x 35,1) + 300,1 aplicando las reglas del cálculo aproximado (primero el producto, después la suma). Respondé solo con el número.",
                "answer": "384: 2,4 . 35,1 = 84,24 → con 2 cifras significativas (las de 2,4) queda 84. Luego 84 + 300,1 = 384,1, y como 84 no tiene decimales, la suma se informa sin decimales: 384.",
                "hints": ["El producto se redondea por cifras significativas; la suma, por decimales.", "Después del producto, ¿cuántos decimales tiene el resultado parcial?"],
                "payload": {"check": {"type": "numeric", "value": 384, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Exponente de 10 en notación científica de un número chico",
                "prompt": "Al escribir 0,00047 en notación científica (una sola cifra distinta de cero a la izquierda de la coma), ¿cuál es el exponente de 10? Respondé solo con el número.",
                "answer": "−4: 0,00047 = 4,7.10⁻⁴. Hay que correr la coma 4 lugares a la derecha para que quede 4,7, y por eso el exponente es negativo.",
                "hints": ["Contá cuántos lugares se mueve la coma hasta dejar 4,7.", "Si el número es menor que 1, el exponente es negativo."],
                "payload": {"check": {"type": "numeric", "value": -4, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Prefijo adecuado para una carga eléctrica muy chica",
                "prompt": "Se midió una carga de 0,0000000052976 C. ¿Cuál es la expresión con un prefijo que deja el valor numérico entre 0,1 y 1000?",
                "answer": "5,2976 nC: 0,0000000052976 C . (1 nC / 1.10⁻⁹ C) = 5,2976 nC, y conserva las 5 cifras significativas. 5297,6 pC está bien convertido pero supera 1000, y 0,0052976 µC queda por debajo de 0,1.",
                "hints": ["Contá cuántos lugares hay que correr la coma para llegar a 5,2976.", "nano = 10⁻⁹, micro = 10⁻⁶, pico = 10⁻¹²."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["5,2976 nC", "5,2976 µC", "5297,6 pC", "0,0052976 µC"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Modo de la calculadora para un producto de mediciones",
                "prompt": "Vas a calcular 1,4.10³ ÷ 2,6.10⁵ y los dos datos tienen 2 cifras significativas. Según el material, ¿en qué modo programás la calculadora para que redondee sola el resultado?",
                "answer": "SCI 2: el modo SCI (científico) fija la cantidad de cifras significativas, que en productos y cocientes es la del factor 'más pobre' (2). Da 5,4.10⁻³. FIX fija decimales (sirve para sumas y restas) y ENG muestra potencias múltiplos de 3, útiles para elegir prefijos.",
                "hints": ["En un cociente manda la cantidad de cifras significativas.", "Hay un modo que fija cifras significativas y otro que fija decimales."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["SCI 2", "FIX 2", "ENG"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== ECUACIONES DE DIMENSIÓN ====================
    {
        "slug": "f-analisis-dimensional",
        "title": "Ecuaciones de dimensión y homogeneidad",
        "summary": "Escribir ecuaciones de dimensión con L, M y T, verificar fórmulas por homogeneidad y hallar la dimensión o la unidad SI de una constante.",
        "prerequisites": ["f-sistemas-unidades"],
        "insert_after": "f-cifras-significativas",
        "metadata": {"section": "Cinemática y base", "lab_tab": "kinematics", "est_minutes": 25},
        "items": [
            {
                "item_type": "recall",
                "title": "Ecuación de dimensión de la fuerza",
                "prompt": "A partir de F = m.a, ¿cuál es la ecuación de dimensión de la fuerza en el SIMELA?",
                "answer": "[F] = L.M.T⁻²: [m] = M y [a] = L.M⁰.T⁻², y al multiplicar se suman los exponentes. Coincide con la unidad N = kg.m/s².",
                "hints": ["[a] = L.T⁻² (metros sobre segundo al cuadrado).", "Al multiplicar magnitudes se suman los exponentes de cada dimensión."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["L.M.T⁻²", "L.M.T⁻¹", "L².M.T⁻²", "L.M⁰.T⁻²"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Exponente de L en la dimensión de la presión",
                "prompt": "La presión es fuerza sobre superficie (p = F/S). En su ecuación de dimensión [p] = Lˣ.M.T⁻², ¿cuánto vale el exponente x? Respondé solo con el número.",
                "answer": "−1: [p] = [F]/[S] = L.M.T⁻² / L² = L⁻¹.M.T⁻². Al dividir se restan los exponentes: 1 − 2 = −1.",
                "hints": ["[S] = L².", "Al dividir, al exponente de arriba se le resta el de abajo."],
                "payload": {"check": {"type": "numeric", "value": -1, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Dimensión de S = F.d / (m.v²)",
                "prompt": "Hallá la dimensión de S en S = F.d / (m.v²), con F: fuerza, d: distancia, m: masa y v: velocidad.",
                "answer": "S es adimensional (L⁰.M⁰.T⁰): arriba [F.d] = L.M.T⁻² . L = L².M.T⁻²; abajo [m.v²] = M . (L.T⁻¹)² = L².M.T⁻². Numerador y denominador tienen la misma dimensión y se cancelan.",
                "hints": ["Calculá por separado la dimensión del numerador y la del denominador.", "(L.T⁻¹)² = L².T⁻²."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["L⁰.M⁰.T⁰ (adimensional)", "L.T⁻¹", "L⁻¹"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Qué magnitud es K en K = F.v⁻¹ + Q",
                "prompt": "En K = F.v⁻¹ + Q, con F: fuerza y v: velocidad, ¿qué dimensión tiene K?",
                "answer": "M.T⁻¹ (masa por unidad de tiempo: caudal másico, en kg/s). Por homogeneidad K tiene la dimensión del término F.v⁻¹: L.M.T⁻² / (L.T⁻¹): para L, 1 − 1 = 0; para T, −2 − (−1) = −1; así que queda L⁰.M.T⁻¹ = M.T⁻¹. Q también tiene esa dimensión.",
                "hints": ["Cada término de una suma tiene la misma dimensión que el resultado.", "v⁻¹ significa dividir por la velocidad: se restan los exponentes."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["M.T⁻¹", "L².M.T⁻³", "M.T⁻³"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Dimensión de α/β en W = v²/α + F/β",
                "prompt": "Sabiendo que W = v²/α + F/β es homogénea, con W: trabajo, v: velocidad y F: fuerza, ¿cuál es la dimensión de α/β?",
                "answer": "[α/β] = L.M⁻¹: de [W] = [v²]/[α] sale [α] = L².T⁻² / (L².M.T⁻²) = M⁻¹; de [W] = [F]/[β] sale [β] = L.M.T⁻² / (L².M.T⁻²) = L⁻¹. Entonces [α/β] = M⁻¹ / L⁻¹ = L.M⁻¹.T⁰.",
                "hints": ["Cada sumando tiene la dimensión del trabajo, L².M.T⁻².", "Despejá primero [α] y [β] por separado y recién después dividí."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["L.M⁻¹", "L⁻¹.M", "L⁻¹.M⁻¹"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Dimensión de k = m.v² / F",
                "prompt": "Hallá la dimensión de k en k = m.v² / F, con m: masa, v: velocidad y F: fuerza.",
                "answer": "[k] = L: [m.v²] = M . L².T⁻² = L².M.T⁻², y al dividir por [F] = L.M.T⁻² queda L¹.M⁰.T⁰. k es una longitud.",
                "hints": ["No te olvides de elevar al cuadrado la dimensión de la velocidad.", "Al dividir se restan los exponentes de L, de M y de T."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["L", "T", "M².L³.T⁻⁴"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Unidad SI de la constante B en E = A.F + B.v² + C.a",
                "prompt": "La fórmula E = A.F + B.v² + C.a es homogénea, con E: trabajo, F: fuerza, v: velocidad y a: aceleración. ¿Cuál es la unidad SI de la constante B?",
                "answer": "kg: por homogeneidad [B.v²] = [E], así que [B] = L².M.T⁻² / (L.T⁻¹)² = L².M.T⁻² / (L².T⁻²) = M. B es una masa y se mide en kg.",
                "hints": ["El término B.v² tiene que tener la dimensión del trabajo.", "Despejá [B] dividiendo [E] por [v²]."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["kg", "J", "kg.m/s"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Exponente de L en la constante β de V = α.A + β.D",
                "prompt": "En V = α.A + β.D (V: volumen, A: área, D: densidad), la dimensión de β es Lⁿ.M⁻¹. ¿Cuánto vale n? Respondé solo con el número.",
                "answer": "6: por homogeneidad [β.D] = [V], así que [β] = L³ / (L⁻³.M) = L⁶.M⁻¹. Al dividir, el exponente de L es 3 − (−3) = 6.",
                "hints": ["[D] = [m/V] = L⁻³.M.", "Restar un exponente negativo es sumar."],
                "payload": {"check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Ecuación de dimensión de la masa en el sistema técnico",
                "prompt": "En el sistema técnico las dimensiones de base son L, F y T. ¿Cuál es la ecuación de dimensión de la masa en ese sistema?",
                "answer": "[m] = F.L⁻¹.T²: de m = F/a y [a] = L.T⁻², resulta F / (L.T⁻²) = F.L⁻¹.T². Es la dimensión de la utm = kgf.s²/m.",
                "hints": ["En el técnico la masa es derivada: despejala de F = m.a.", "Dividir por T⁻² es multiplicar por T²."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["F.L⁻¹.T²", "F.L.T⁻²", "M (es fundamental)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Detectar una fórmula que no es homogénea",
                "prompt": "Con x: posición, v: velocidad, a: aceleración y t: tiempo, ¿cuál de estas fórmulas NO puede ser correcta porque no es dimensionalmente homogénea?",
                "answer": "x = v + a.t: el primer miembro es L, pero el segundo es L.T⁻¹ (v y a.t son velocidades). Las otras tres sí son homogéneas: v.t y a.t² son L; v² y a.x son L².T⁻²; a.t es L.T⁻¹. Ojo: la homogeneidad no garantiza que una fórmula sea correcta, pero su falta sí garantiza que está mal.",
                "hints": ["Calculá la dimensión de cada término de cada fórmula.", "Los números como ½ o 2 son adimensionales."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["x = v + a.t", "x = v.t + ½.a.t²", "v² = 2.a.x", "v = a.t"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
]


INGRESO_PHYSICS_A_LESSONS: dict[str, dict] = {
    "f-sistemas-unidades": {
        "hook": {
            "question": "Si apoyás una bolsa de 1 kg de yerba sobre una balanza de resortes, ¿cuánto la empuja la Tierra hacia abajo: 1 kg, 1 kgf o 9,8 N?",
            "intuition": "Kilogramo es masa; kilogramo fuerza y newton son fuerza. La Tierra la tira con **1 kgf**, que es lo mismo que **9,8 N**. Según el sistema de unidades que elijas, la misma fuerza tiene otro número y otro nombre, y la masa puede ser magnitud fundamental (SI) o derivada (técnico). Para no mezclarlas existen los **sistemas de unidades** y un método seguro para pasar de uno a otro: las **fracciones unitarias**.",
        },
        "concept": {
            "points": [
                "**Magnitudes fundamentales y derivadas**: las fundamentales se eligen como base; las derivadas se forman relacionándolas (velocidad = longitud/tiempo). En Argentina rige el **SIMELA** (Sistema Métrico Legal Argentino, ley 19 511), que adopta el SI: sus 7 unidades de base son m, kg, s, A, K, mol y cd. En mecánica alcanzan **longitud, masa y tiempo** (L, M, T). En el **sistema técnico español** las fundamentales son **longitud, fuerza y tiempo** (L, F, T): la masa es derivada.",
                "**Cuadro de los tres sistemas** (la utm sale de m = F/a: kgf/(m/s²) = kgf.s²/m):\n| Magnitud | SI (SIMELA) | c.g.s. | Técnico español |\n|---|---|---|---|\n| Longitud | m | cm | m |\n| Masa | kg | g | utm = kgf.s²/m |\n| Tiempo | s | s | s |\n| Fuerza | N = kg.m/s² | dina (dyn) = g.cm/s² | kgf (fundamental) |\n| Trabajo, energía | J = N.m | erg = dyn.cm | kgm = kgf.m |\n| Potencia | W = J/s | erg/s | kgm/s |\n| Presión | Pa = N/m² | baria = dyn/cm² | kgf/m² |",
                "**Equivalencias del curso**: 1 kgf = 9,8 N; 1 N = 10⁵ dyn; 1 utm = 9,8 kg; 1 J = 10⁷ erg; 1 kgm = 9,8 J; 1 Pa = 10 baria; 1 kgf/m² = 9,8 Pa. Unidades prácticas: 1 CV = 735,5 W (≈ 75 kgm/s; con 1 kgm = 9,8 J da 735 W), 1 HP = 746 W; 1 atm = 760 mmHg = 1,013.10⁵ Pa ≈ 1,033 kgf/cm². **Técnico inglés** (el que aparece en el material): 1 lbf = 0,454 kgf; 1 pie = 30,48 cm = 12 pulg; 1 pulg = 2,54 cm; 1 yarda = 3 pies; 1 milla = 5280 pies.",
                "**Método de fracciones unitarias**: se multiplica la cantidad por fracciones que valen 1 porque arriba y abajo hay lo mismo en distinta unidad (1 m / 100 cm). Se elige la fracción que deja **abajo la unidad que querés cancelar** y arriba la nueva: 250 cm . (1 m / 100 cm) = 2,5 m. Para unidades compuestas se encadena una fracción por cada unidad: km/h → m/s usa (1000 m / 1 km) y (1 h / 3600 s).",
                "**Áreas y volúmenes**: la fracción de longitud se eleva al cuadrado o al cubo: 2,5 hm² . (10 000 cm / 1 hm)² = 2,5.10⁸ cm²; 1 g/cm³ . (1 kg / 1000 g) . (100 cm / 1 m)³ = 1000 kg/m³.",
                "**Reglas de escritura del SIMELA**: los símbolos no son abreviaturas (sin punto y sin plural: 5 kg, no 5 kgs.); van en mayúscula solo si la unidad viene de un nombre propio (N, J, W, Pa) y los prefijos M, G, T, P, E (k es minúscula: km, kW); el prefijo va pegado a la unidad y **no se combinan prefijos** (7,49 ns, nunca 7,49 mμs); los miles se separan con un espacio (5 000 kW) y se usa **coma decimal** (en otros temas de la app vas a ver 1.5 con punto: es lo mismo que 1,5).",
            ],
            "real_world": [
                {
                    "title": "Potencia de un auto en CV o en kW",
                    "detail": "Una ficha técnica que dice 100 CV equivale a 100 . 735,5 W = 73 550 W ≈ 73,6 kW. Los fabricantes europeos ya informan las dos.",
                },
                {
                    "title": "Pantallas y caños en pulgadas",
                    "detail": "Un televisor de 32 pulg tiene 32 . 2,54 cm = 81,28 cm de diagonal; en plomería las roscas de 1/2 pulg siguen siendo el estándar aunque todo lo demás esté en mm.",
                },
                {
                    "title": "Presión arterial en mmHg",
                    "detail": "Una presión de 120 mmHg, con 760 mmHg = 1,013.10⁵ Pa, son unos 1,6.10⁴ Pa: los médicos siguen usando la unidad de la columna de mercurio.",
                },
            ],
            "key_rule": "Fundamentales: SI y c.g.s. → L, M, T; técnico → L, F, T (masa derivada: utm = kgf.s²/m) | 1 kgf = 9,8 N, 1 N = 10⁵ dyn, 1 utm = 9,8 kg | Fracción unitaria: abajo la unidad que se cancela, arriba la nueva; al cuadrado o al cubo para áreas y volúmenes.",
            "pitfall": "Convertir m² o m³ con la equivalencia de longitud sin elevarla (creer que 1 m² = 100 cm²), y confundir kg (masa) con kgf (fuerza): una bolsa de 1 kg pesa 1 kgf = 9,8 N.",
        },
        "example": {
            "title": "Pasar la presión de un neumático, 3,5 kgf/cm², a pascal",
            "steps": [
                "Planteo: hay que cambiar dos unidades, kgf → N y cm² → m², así que se encadenan dos fracciones unitarias.",
                "Fuerza: (9,8 N / 1 kgf) deja los kgf abajo para cancelarlos.",
                "Superficie: los cm² están en el denominador, así que la fracción debe tener cm² arriba: (100 cm / 1 m)² = 10 000 cm² / 1 m².",
                "Cuenta: 3,5 kgf/cm² . (9,8 N / 1 kgf) . (10 000 cm² / 1 m²) = 3,5 . 9,8 . 10 000 N/m² = 343 000 Pa.",
                "Con prefijo: 343 000 Pa = 343 kPa (3,43.10⁵ Pa). Control: 1 atm ≈ 1,013.10⁵ Pa, así que el neumático está a unas 3,4 atm. Tiene sentido.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "¿Cuál es la unidad de masa del sistema técnico español?",
            "options": [
                {"text": "La utm (unidad técnica de masa), equivalente a 1 kgf.s²/m", "ok": True, "feedback": "Exacto: en el técnico la masa es derivada y su unidad sale de m = F/a. Vale 9,8 kg."},
                {"text": "El kgf", "ok": False, "feedback": "El kgf es la unidad de FUERZA del técnico, y además es fundamental. La masa se deriva de ella."},
                {"text": "El kg", "ok": False, "feedback": "El kg es la unidad de masa del SI, donde la masa es fundamental. En el técnico la masa no es de base."},
            ],
        },
        "checks": [
            {
                "question": "Para pasar 250 cm a metros, ¿por qué fracción unitaria multiplicás?",
                "options": [
                    {"text": "1 m / 100 cm", "ok": True, "feedback": "Exacto: los cm quedan abajo y se cancelan con los de 250 cm. Resultado: 2,5 m."},
                    {"text": "100 cm / 1 m", "ok": False, "feedback": "Así los cm quedan arriba y no se cancelan: obtendrías 25 000 cm²/m, que no es una longitud en metros."},
                    {"text": "1 m / 10 cm", "ok": False, "feedback": "La equivalencia está mal: 1 m son 100 cm (10 cm es 1 dm). Te daría 25 m."},
                ],
            },
            {
                "question": "Un intervalo de tiempo vale 7,49.10⁻⁹ s. ¿Cómo se escribe correctamente con prefijo?",
                "options": [
                    {"text": "7,49 ns", "ok": True, "feedback": "Exacto: nano = 10⁻⁹, un solo prefijo pegado al símbolo s."},
                    {"text": "7,49 mμs", "ok": False, "feedback": "Aunque mili por micro dé 10⁻⁹, el SIMELA prohíbe combinar prefijos: se usa el prefijo único nano."},
                    {"text": "7,49 nseg.", "ok": False, "feedback": "El símbolo del segundo es s: 'seg' no existe y los símbolos no llevan punto."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras por qué en el sistema técnico la masa es una magnitud derivada y cómo elegís qué fracción unitaria usar en una conversión.",
    },
    "f-cifras-significativas": {
        "hook": {
            "question": "Medís un cilindro con una regla milimetrada y anotás 15,4 mm. ¿Podrías anotar 15,40 mm o 15,400 mm, que 'es el mismo número'?",
            "intuition": "No. Con una regla en mm el 1 y el 5 son seguros y el 4 ya es **estimado a ojo**: es una cifra dudosa. Escribir 15,40 mm sería decir que también conocés las centésimas, y tu regla no da para tanto. Las **cifras significativas** son la forma de que un número cuente con honestidad qué tan precisa fue la medición.",
        },
        "concept": {
            "points": [
                "**Cifras significativas (cs)**: las cifras que sabemos exactas **más una dudosa**. 15,4 mm tiene 3 cs. Un cambio de unidades no mejora ni empeora la medición: 15,4 mm = 0,0154 m = 1,54.10⁴ µm, siempre 3 cs.",
                "**Reglas de los ceros**: (1) los ceros después de la coma pero **antes** del primer dígito distinto de cero **no** son significativos (0,0025 mm → 2 cs); (2) los ceros a la **derecha** de los dígitos distintos de cero **sí** lo son (1,2500 mm → 5 cs). Criterio del curso: **los ceros, si están escritos, son significativos** (3 600 s → 4 cs; 6 000 K → 4 cs).",
                "**Redondeo y notación científica**: se corta en la última cifra que se conserva; si el dígito siguiente es **mayor que 4**, la última sube una unidad; si es **4 o menos**, queda igual. Para no agregar ceros que contarían como cifras se usa notación científica, con **una sola cifra distinta de cero** a la izquierda de la coma: 22478 con 3 cs = 2,25.10⁴; 1 230 con 3 cs = 1,23.10³. Exponente positivo: la coma se corre a la derecha; negativo: a la izquierda (7,8.10⁻³ = 0,0078).",
                "**Cálculo aproximado**: en **sumas y restas**, el resultado lleva tantos **decimales** como el término con menos decimales (1,2822 + 0,328 + 12,12 = 13,7302 → 13,73). En **productos, cocientes, potencias y raíces**, lleva tantas **cifras significativas** como el factor 'más pobre' (1,2822 x 0,328 = 0,4205616 → 0,421). En operaciones combinadas se resuelve primero cada paso con su regla.",
                "**Prefijos**: se recomienda elegir el prefijo que deje el valor numérico **entre 0,1 y 1000**, respetando las cs: 0,000324 s . (1 µs / 1.10⁻⁶ s) = 324 µs; 128 563 m = 128,563 km.",
                "**Uso de la calculadora**: **FIX n** fija n decimales (para sumas y restas); **SCI n** fija n cifras significativas en notación científica (para productos y cocientes); **ENG** muestra el número con potencias múltiplos de 3, que se leen directo como prefijos (7,5.10⁻⁴ W → 750.10⁻⁶ W = 750 µW).",
            ],
            "real_world": [
                {
                    "title": "La balanza de la verdulería",
                    "detail": "Si la balanza muestra 1,25 kg, el 5 ya es dudoso. Informar '1,2500 kg' inventaría una precisión que la balanza no tiene.",
                },
                {
                    "title": "Planos de ingeniería",
                    "detail": "En un plano, 25 mm y 25,00 mm no son lo mismo: el segundo le exige al taller trabajar al centésimo de milímetro, y eso cuesta otra máquina y otro precio.",
                },
                {
                    "title": "Datos científicos en notación científica",
                    "detail": "La masa del electrón, 9,109.10⁻³¹ kg, y la distancia Tierra-Luna, 3,84.10⁵ km, se escriben así para mostrar a la vez el tamaño y la precisión: 4 y 3 cs.",
                },
            ],
            "key_rule": "Ceros iniciales: no cuentan | ceros escritos a la derecha: cuentan | Suma y resta → menor cantidad de DECIMALES | Producto y cociente → menor cantidad de CIFRAS SIGNIFICATIVAS | Redondeo: >4 sube, ≤4 queda | Prefijo: valor entre 0,1 y 1000.",
            "pitfall": "Aplicar la regla equivocada: redondear una suma por cifras significativas o un producto por decimales. Y copiar todos los dígitos de la calculadora (306,9 en vez de 3.10² cuando un factor tiene 1 cs).",
        },
        "example": {
            "title": "Perímetro y superficie de un terreno de 26,71 m por 23 dm",
            "steps": [
                "Unidades homogéneas: 23 dm . (1 m / 10 dm) = 2,3 m (sigue con 2 cs y ahora tiene un decimal).",
                "Perímetro (suma): 26,71 + 26,71 + 2,3 + 2,3 = 58,02 m. El término con menos decimales es 2,3 (uno), así que se informa con un decimal: **58,0 m** (el dígito descartado es 2, queda igual).",
                "Superficie (producto): 26,71 m . 2,3 m = 61,433 m². El factor más pobre es 2,3 (2 cs), así que el resultado lleva 2 cs: **61 m²** (el dígito descartado es 4, queda igual).",
                "Con calculadora: FIX 1 para el perímetro (muestra 58,0) y SCI 2 para la superficie (muestra 6,1.10¹, o sea 61 m²).",
                "Conclusión: perímetro 58,0 m y superficie 61 m², que es la respuesta que da la guía del curso.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "¿Cuántas cifras significativas tiene una medición de 0,0025 mm?",
            "options": [
                {"text": "2", "ok": True, "feedback": "Exacto: solo el 2 y el 5. Los ceros de adelante únicamente ubican la coma."},
                {"text": "4", "ok": False, "feedback": "Contaste todos los dígitos después de la coma, pero los ceros antes del primer dígito distinto de cero no son significativos."},
                {"text": "5", "ok": False, "feedback": "Contaste todos los dígitos, incluido el cero entero. Ni ese cero ni los dos siguientes son significativos."},
            ],
        },
        "checks": [
            {
                "question": "La suma 1,2822 + 0,328 + 12,12 da 13,7302 en la calculadora. ¿Cómo se informa el resultado?",
                "options": [
                    {"text": "13,73", "ok": True, "feedback": "Exacto: 12,12 tiene solo dos decimales, así que el resultado se corta en la centésima."},
                    {"text": "13,7", "ok": False, "feedback": "Aplicaste la regla del producto (3 cs, por 0,328). En las sumas manda la cantidad de decimales, y el más pobre tiene dos."},
                    {"text": "13,7302", "ok": False, "feedback": "Es el número de la calculadora: sus últimas cifras no significan nada porque los datos no tienen esa precisión."},
                ],
            },
            {
                "question": "¿Qué hace el modo ENG de la calculadora?",
                "options": [
                    {"text": "Muestra el número con una potencia de 10 múltiplo de 3, que corresponde a un prefijo", "ok": True, "feedback": "Exacto: por eso sirve para elegir el prefijo (10³ = k, 10⁻⁶ = µ, 10⁹ = G...)."},
                    {"text": "Fija la cantidad de decimales del resultado", "ok": False, "feedback": "Eso hace el modo FIX, que se usa en sumas y restas."},
                    {"text": "Fija la cantidad de cifras significativas en notación científica", "ok": False, "feedback": "Eso hace el modo SCI, que se usa en productos y cocientes."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras por qué en una suma manda la cantidad de decimales y en un producto la cantidad de cifras significativas.",
    },
    "f-analisis-dimensional": {
        "hook": {
            "question": "Si alguien te dice que la distancia recorrida es d = v + t, ¿podés saber que está mal sin conocer nada del problema?",
            "intuition": "Sí: no se pueden sumar metros por segundo con segundos, igual que no se suman manzanas con litros. Cada término de una fórmula física tiene que tener la **misma dimensión**. Escribiendo cada magnitud en función de L, M y T, una fórmula se revisa en un minuto y hasta se puede descubrir qué es una constante desconocida.",
        },
        "concept": {
            "points": [
                "**Ecuación de dimensión**: es la ecuación entre unidades sin los coeficientes numéricos, escrita con las dimensiones de base. En el SIMELA (mecánica): **L** (longitud), **M** (masa), **T** (tiempo). Se anota con corchetes y la magnitud que no interviene va elevada a 0: [a] = L.M⁰.T⁻², [v] = L.M⁰.T⁻¹.",
                "**Dimensiones que conviene conocer**:\n| Magnitud | Ecuación de dimensión |\n|---|---|\n| Superficie | L² |\n| Volumen | L³ |\n| Velocidad | L.T⁻¹ |\n| Aceleración | L.T⁻² |\n| Fuerza | L.M.T⁻² |\n| Trabajo, energía, momento | L².M.T⁻² |\n| Potencia | L².M.T⁻³ |\n| Presión | L⁻¹.M.T⁻² |\n| Densidad | L⁻³.M |\n| Peso específico | L⁻².M.T⁻² |",
                "**Operar**: al multiplicar se suman los exponentes; al dividir se restan; al elevar se multiplican. Los números puros (½, 2, π) son **adimensionales**: no aportan dimensión. Trabajo y momento de una fuerza son **equidimensionales** (L².M.T⁻²) aunque sean conceptos distintos; solo el trabajo usa el joule.",
                "**Principio de homogeneidad**: en una ecuación física válida, **todos los términos** de ambos miembros tienen la misma dimensión. Si no se cumple, la fórmula está mal. Si se cumple, puede ser correcta (los números adimensionales no se pueden controlar así).",
                "**Hallar una constante**: se iguala el término que la contiene con la dimensión de la magnitud conocida y se despeja. En E = A.F + B.v² + C.a con E trabajo: [A] = L, [B] = M, [C] = L.M. Con la dimensión se lee la **unidad SI** (L → m, M → kg, T → s): [B] = M → B en kg.",
                "**Sistema técnico**: las dimensiones de base son **L, F, T**. La masa es derivada: [m] = [F/a] = F.L⁻¹.T², que corresponde a la utm = kgf.s²/m.",
            ],
            "real_world": [
                {
                    "title": "Control rápido en un examen",
                    "detail": "Si despejaste una velocidad y la dimensión te da L.T⁻², hay un error algebraico antes del resultado. Revisar dimensiones lleva segundos y evita entregar una respuesta imposible.",
                },
                {
                    "title": "Fórmulas empíricas en ingeniería",
                    "detail": "Muchas fórmulas de hidráulica o resistencia de materiales salen de ensayos y traen constantes con dimensión. Saber la dimensión de la constante dice en qué unidades hay que cargar los datos.",
                },
                {
                    "title": "Planillas de cálculo y programas",
                    "detail": "Un programa no sabe si sumaste N con kgf. Verificar dimensiones de cada término antes de programar una fórmula evita errores que ningún compilador detecta.",
                },
            ],
            "key_rule": "Base SI: L, M, T (técnico: L, F, T) | Multiplicar → sumar exponentes, dividir → restar | Números puros: adimensionales | Homogeneidad: todos los términos con la misma dimensión | Constante: igualar su término con la magnitud conocida y despejar.",
            "pitfall": "Olvidarse de elevar la dimensión cuando la magnitud está al cuadrado ([v²] = L².T⁻², no L.T⁻¹), o equivocar el signo al restar exponentes negativos (T⁻² / T⁻¹ = T⁻¹, no T⁻³).",
        },
        "example": {
            "title": "Unidades SI de x = F².v / (2.m.t)",
            "steps": [
                "Datos de la tabla: [F] = L.M.T⁻², [v] = L.T⁻¹, [m] = M, [t] = T. El 2 es un número puro: no tiene dimensión.",
                "Numerador: [F²] = (L.M.T⁻²)² = L².M².T⁻⁴; por [v]: L².M².T⁻⁴ . L.T⁻¹ = L³.M².T⁻⁵.",
                "Denominador: [m.t] = M.T.",
                "Dividir restando exponentes: L³.M^(2−1).T^(−5−1) = L³.M.T⁻⁶.",
                "Unidad SI: cambiando L → m, M → kg, T → s, la magnitud x se mide en kg.m³/s⁶.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "¿Cuál es la ecuación de dimensión de la velocidad, escrita como en el curso?",
            "options": [
                {"text": "[v] = L.M⁰.T⁻¹", "ok": True, "feedback": "Exacto: longitud sobre tiempo, y la masa no interviene (exponente 0)."},
                {"text": "[v] = L.M⁰.T", "ok": False, "feedback": "Eso sería longitud POR tiempo. La velocidad divide por el tiempo, así que su exponente es −1."},
                {"text": "[v] = L.M⁰.T⁻²", "ok": False, "feedback": "Esa es la dimensión de la aceleración (m/s²), que divide dos veces por el tiempo."},
            ],
        },
        "checks": [
            {
                "question": "El trabajo mecánico y el momento de una fuerza (ambos fuerza por distancia), ¿qué relación tienen?",
                "options": [
                    {"text": "Tienen la misma ecuación de dimensión, L².M.T⁻², aunque son conceptos distintos", "ok": True, "feedback": "Exacto: son equidimensionales. El trabajo se mide en joule y el momento en N.m, sin nombre propio."},
                    {"text": "Tienen dimensiones distintas porque son conceptos distintos", "ok": False, "feedback": "La dimensión depende solo de cómo se calcula la magnitud: las dos son fuerza por distancia, L.M.T⁻² . L."},
                    {"text": "El momento es adimensional porque la distancia se cancela", "ok": False, "feedback": "Nada se cancela: se multiplica fuerza por distancia, así que la L se suma a la de la fuerza."},
                ],
            },
            {
                "question": "En x = ½.a.t², ¿qué dimensión aporta el ½?",
                "options": [
                    {"text": "Ninguna: es un número puro (adimensional)", "ok": True, "feedback": "Exacto: los coeficientes numéricos no tienen dimensión, por eso desaparecen en la ecuación de dimensión."},
                    {"text": "T⁻¹, porque divide por 2", "ok": False, "feedback": "Dividir por un número no agrega dimensión: 2 no es un tiempo."},
                    {"text": "La misma que x, es decir L", "ok": False, "feedback": "Si ½ tuviera dimensión L, el segundo miembro sería L.L.T⁻².T² = L², distinto de [x]."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras qué dice el principio de homogeneidad y cómo lo usás para encontrar la dimensión de una constante desconocida.",
    },
}
