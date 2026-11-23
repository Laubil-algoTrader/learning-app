"""Temas de matemática del Curso de Ingreso 2027 (Ingeniería, UNCuyo) — bloque B.

Cuatro nodos que se intercalan en la materia `matematicas` mediante `insert_after`:
  - Sistemas de ecuaciones lineales: métodos, clasificación y parámetros (con la recta)
  - Función cuadrática: formas polinómica, canónica y factorizada
  - Polígonos y cuadriláteros: ángulos interiores y exteriores, clasificación y áreas
  - Los siete casos de factoreo y la factorización combinada

Siguen la notación del material del ingreso: coma decimal, pares (3; 1), intervalos con
punto y coma, IR, S = {…}, tg, "ceros", "imagen", C⁺ y C⁻.
"""

from __future__ import annotations

INGRESO_MATH_B_NODES: list[dict] = [
    # ==================== SEL: MÉTODOS, CLASIFICACIÓN Y PARÁMETROS ====================
    {
        "slug": "al-sel-metodos-clasificacion",
        "title": "Sistemas de ecuaciones lineales: métodos, clasificación y parámetros",
        "summary": "Resolver un SEL 2×2 por los métodos gráfico, de sustitución, igualación y reducción, clasificarlo en SCD, SCI o SI sin resolverlo (también con un parámetro k) y manejar la recta: inclinación, ecuación general, paralelas y perpendiculares.",
        "prerequisites": ["p-sistemas-ecuaciones", "al-formas-lineales"],
        "insert_after": "al-formas-lineales",
        "metadata": {"section": "Álgebra 1", "lab_tab": "systems", "est_minutes": 30},
        "items": [
            {
                "item_type": "recall",
                "title": "Pendiente a partir del ángulo de inclinación",
                "prompt": "El ángulo de inclinación de una recta (el que forma con el semieje positivo de las x) es α = 135°. ¿Cuál es su pendiente? Respondé solo con el número.",
                "answer": "−1: la pendiente es m = tg α = tg 135° = −1. Un ángulo de inclinación obtuso (entre 90° y 180°) siempre da pendiente negativa: la recta baja de izquierda a derecha.",
                "hints": [
                    "La pendiente se define como la tangente del ángulo de inclinación: m = tg α.",
                    "135° = 180° − 45°, y en el segundo cuadrante la tangente es negativa.",
                ],
                "payload": {"check": {"type": "numeric", "value": -1, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Ecuación general con el coeficiente de x nulo",
                "prompt": "En la ecuación general de una recta Ax + By + C = 0, supongamos que A = 0 y B ≠ 0. ¿Qué tipo de recta representa?",
                "answer": "Una recta horizontal: queda By + C = 0, o sea y = −C/B, y todos sus puntos tienen la misma ordenada. Si en cambio B = 0 (y A ≠ 0) queda x = −C/A, una recta vertical. A y B no pueden ser nulos a la vez, porque entonces la expresión no representa una recta.",
                "hints": ["Reemplazá A = 0 y despejá la variable que queda.", "¿Qué coordenada es igual en todos los puntos?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Una recta horizontal (y = constante)",
                            "Una recta vertical (x = constante)",
                            "Una recta que pasa siempre por el origen",
                            "No representa ninguna recta",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Parámetro t para que dos rectas sean perpendiculares",
                "prompt": "Dadas r: 2x − 3y + 6 = 0 y s: tx + 4y − 1 = 0, ¿qué valor debe tomar t para que r y s sean perpendiculares? Respondé solo con el número.",
                "answer": "6: despejando y, la pendiente de r es m_r = 2/3 y la de s es m_s = −t/4. Para que sean perpendiculares las pendientes tienen que ser opuestas y recíprocas: m_s = −3/2. Entonces −t/4 = −3/2 → t = 6.",
                "hints": [
                    "Despejá y en cada ecuación para leer las pendientes.",
                    "Perpendiculares: m₁ = −1/m₂ (cambiar el signo y dar vuelta la fracción).",
                ],
                "payload": {"check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Clasificar un SEL por proporcionalidad de coeficientes",
                "prompt": "Sin resolverlo, clasificá el sistema { 3x − 2y = 5 ; −6x + 4y = 7 }.",
                "answer": "Sistema incompatible (SI): los coeficientes son proporcionales, 3/(−6) = −2/4 = −1/2, pero los términos independientes no guardan esa proporción: 5/7 ≠ −1/2. Las rectas tienen la misma pendiente (3/2) y distinta ordenada al origen: son paralelas disjuntas y S = { }.",
                "hints": [
                    "Compará a/a′ con b/b′: si son distintos, el sistema es SCD.",
                    "Si a/a′ = b/b′, mirá también c/c′.",
                ],
                "payload": {
                    "lab_link": "math:systems",
                    "check": {
                        "type": "choice",
                        "options": [
                            "Compatible determinado: rectas secantes",
                            "Compatible indeterminado: rectas paralelas coincidentes",
                            "Incompatible: rectas paralelas disjuntas",
                        ],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Interpretar un absurdo al resolver un SEL",
                "prompt": "Al resolver un sistema 2×2 por sustitución, las dos incógnitas se cancelan y llegás a 0 = 7. ¿Qué significa?",
                "answer": "Que el sistema es incompatible (SI): no hay ningún par (x; y) que verifique las dos ecuaciones, las rectas son paralelas disjuntas y S = { }. No es un error de cuentas. Si en cambio llegaras a una identidad como 0 = 0, el sistema sería compatible indeterminado (infinitas soluciones).",
                "hints": ["Una igualdad falsa que no depende de x ni de y no se puede cumplir nunca."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "El sistema es incompatible: S = { }",
                            "El sistema es compatible indeterminado: infinitas soluciones",
                            "La solución es x = 0 e y = 7",
                            "Seguro hay un error de cuentas: todo SEL tiene solución",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Valor de k que vuelve incompatible un sistema",
                "prompt": "Dado el sistema { kx + 2y = 4 ; 3x + y = 5 }, ¿para qué valor de k es incompatible? Respondé solo con el número.",
                "answer": "6: para que no sea SCD los coeficientes deben ser proporcionales: k/3 = 2/1 → k = 6. Con k = 6 la razón de los términos independientes es 4/5, distinta de 2, así que el sistema es incompatible (rectas paralelas disjuntas). Para cualquier k ≠ 6 es compatible determinado, y nunca es SCI.",
                "hints": ["Igualá a/a′ con b/b′ y despejá k.", "Con ese k, compará c/c′ con la razón de los coeficientes."],
                "payload": {"check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Clasificar un SEL según el parámetro k",
                "prompt": "¿Cómo se clasifica el sistema { 2x − y = 3 ; 6x + ky = 9 } según los valores de k?",
                "answer": "SCD si k ≠ −3 y SCI si k = −3; nunca es SI. Los coeficientes son proporcionales cuando 2/6 = −1/k, o sea k = −3. Con k = −3 también 3/9 = 1/3: los tres cocientes son iguales, las rectas son coincidentes (la segunda ecuación es la primera multiplicada por 3). Con k = 3 los cocientes 1/3 y −1/3 son distintos, así que es SCD.",
                "hints": [
                    "Planteá 2/6 = −1/k y cuidá el signo.",
                    "Para ese k, compará 3/9 con 2/6.",
                ],
                "payload": {
                    "lab_link": "math:systems",
                    "check": {
                        "type": "choice",
                        "options": [
                            "SCD si k ≠ −3; SCI si k = −3; nunca SI",
                            "SCD si k ≠ −3; SI si k = −3; nunca SCI",
                            "SCD si k ≠ 3; SCI si k = 3; nunca SI",
                            "SCI para cualquier valor de k",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Método de reducción con coeficientes opuestos",
                "prompt": "Resolvé por reducción (sumas y restas) el sistema { 2x + 3y = 12 ; 5x − 3y = 9 }. ¿Cuánto vale y? Respondé solo con el número.",
                "answer": "2: los coeficientes de y son opuestos (3 y −3), así que sumando miembro a miembro se elimina y: 7x = 21 → x = 3. Reemplazando en la primera: 2.3 + 3y = 12 → 3y = 6 → y = 2. S = {(3; 2)}; verificación en la segunda: 5.3 − 3.2 = 9 ✓.",
                "hints": ["Sumá las dos ecuaciones: ¿qué incógnita desaparece?", "Con x hallado, reemplazá en cualquiera de las ecuaciones."],
                "payload": {"check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Método de igualación con dos rectas despejadas",
                "prompt": "Resolvé por igualación el sistema { y = 2x − 1 ; y = −x + 8 }. ¿Cuánto vale y en la solución? Respondé solo con el número.",
                "answer": "5: como las dos ecuaciones ya tienen y despejada, se igualan: 2x − 1 = −x + 8 → 3x = 9 → x = 3. Reemplazando en cualquiera: y = 2.3 − 1 = 5. S = {(3; 5)}: es el punto donde se cortan las dos rectas.",
                "hints": ["Igualá los segundos miembros y resolvé la ecuación en x.", "Después reemplazá x en una de las expresiones despejadas."],
                "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Plantear un SEL: autos y motos en un estacionamiento",
                "prompt": "En un estacionamiento hay autos y motos: en total son 40 vehículos y suman 130 ruedas. ¿Cuántas motos hay? Respondé solo con el número.",
                "answer": "15: con a = cantidad de autos y m = cantidad de motos, el sistema es { a + m = 40 ; 4a + 2m = 130 }. Despejando m = 40 − a y sustituyendo: 4a + 2(40 − a) = 130 → 2a = 50 → a = 25 y m = 15. Verificación: 4.25 + 2.15 = 100 + 30 = 130 ✓.",
                "hints": [
                    "Una ecuación cuenta vehículos y la otra cuenta ruedas: \"la suma de las partes es igual al todo\".",
                    "Cada auto aporta 4 ruedas y cada moto 2.",
                ],
                "payload": {"check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    # ==================== FUNCIÓN CUADRÁTICA: TRES FORMAS ====================
    {
        "slug": "al-cuadratica-formas",
        "title": "Función cuadrática: formas polinómica, canónica y factorizada",
        "summary": "Pasar una cuadrática entre sus formas polinómica, canónica y factorizada, leer vértice, eje de simetría, imagen, ceros y ordenada al origen, decidir con el discriminante (también con parámetro) cuántos ceros tiene y hallar C⁺ y C⁻.",
        "prerequisites": ["al-parabolas-formula"],
        "insert_after": "al-parabolas-formula",
        "metadata": {"section": "Álgebra 1", "lab_tab": "quadratics", "est_minutes": 28},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Ordenada del vértice desde la forma polinómica",
                "prompt": "Para f(x) = 2x² − 12x + 7, calculá la ordenada del vértice yᵥ. Respondé solo con el número.",
                "answer": "−11: primero xᵥ = −b/(2a) = 12/4 = 3, y después yᵥ = f(3) = 2.9 − 12.3 + 7 = 18 − 36 + 7 = −11. El vértice es V = (3; −11).",
                "hints": ["Empezá por la abscisa del vértice: xᵥ = −b/(2a).", "La ordenada del vértice es la imagen de xᵥ."],
                "payload": {"lab_link": "math:quadratics", "check": {"type": "numeric", "value": -11, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Pasar a forma canónica completando cuadrados",
                "prompt": "Escribí f(x) = x² + 6x + 5 en forma canónica completando cuadrados.",
                "answer": "f(x) = (x + 3)² − 4: comparando x² + 6x con x² + 2ax + a² sale 2a = 6, a = 3 y a² = 9. Se suma y resta 9: x² + 6x + 9 − 9 + 5 = (x + 3)² − 4. El vértice es V = (−3; −4).",
                "hints": [
                    "El número que completa el cuadrado es (la mitad del coeficiente de x)².",
                    "Lo que sumás para completar lo tenés que restar para no cambiar la función.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(x + 3)² − 4", "(x + 3)² + 5", "(x − 3)² − 4", "(x + 6)² − 31"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Imagen de una cuadrática con ramas hacia abajo",
                "prompt": "¿Cuál es el conjunto imagen de f(x) = −2(x − 1)² + 5?",
                "answer": "(−∞; 5]: como a = −2 < 0, las ramas van hacia abajo y el vértice V = (1; 5) es el punto más alto. La función toma el valor 5 y todos los menores. La abscisa del vértice (1) no interviene en la imagen.",
                "hints": ["El signo de a dice si el vértice es el punto más alto o el más bajo.", "La imagen se lee en el eje y: usá yᵥ."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(−∞; 5]", "[5; +∞)", "(−∞; 1]", "IR"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Ecuación del eje de simetría desde la forma canónica",
                "prompt": "¿Cuál es la ecuación del eje de simetría de la parábola f(x) = 3(x + 2)² − 7?",
                "answer": "x = −2: en la forma canónica a(x − xᵥ)² + yᵥ, el paréntesis (x + 2) es (x − (−2)), así que xᵥ = −2. El eje de simetría es la recta vertical que pasa por el vértice V = (−2; −7), y su ecuación es x = xᵥ.",
                "hints": ["El eje de simetría es una recta vertical: su ecuación es x = número.", "En (x − xᵥ) el signo de adentro aparece cambiado."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["x = −2", "x = 2", "y = −7", "x = −7"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Forma factorizada a partir de los ceros y un punto",
                "prompt": "Una parábola tiene ceros x₁ = −1 y x₂ = 4 y corta al eje y en (0; −8). ¿Cuál es su forma factorizada?",
                "answer": "f(x) = 2(x + 1)(x − 4): la forma factorizada es a(x − x₁)(x − x₂) = a(x + 1)(x − 4). Para hallar a se usa el punto (0; −8): a.(0 + 1).(0 − 4) = −4a = −8 → a = 2. Sin el 2, la ordenada al origen daría −4.",
                "hints": [
                    "Escribí a(x − x₁)(x − x₂) cuidando los signos: el cero −1 aparece como (x + 1).",
                    "Reemplazá x = 0 y usá que f(0) = −8 para despejar a.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["2(x + 1)(x − 4)", "2(x − 1)(x + 4)", "(x + 1)(x − 4)", "−2(x + 1)(x − 4)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Parámetro m para que la parábola tenga un solo cero",
                "prompt": "¿Para qué valor de m la función f(x) = x² − 6x + m tiene un único cero (la parábola toca el eje x solo en su vértice)? Respondé solo con el número.",
                "answer": "9: un único cero significa discriminante nulo. Δ = b² − 4ac = (−6)² − 4.1.m = 36 − 4m = 0 → m = 9. Queda f(x) = x² − 6x + 9 = (x − 3)², con cero doble en x = 3.",
                "hints": ["Un cero doble ↔ Δ = 0.", "Δ = b² − 4ac con a = 1, b = −6 y c = m."],
                "payload": {"check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Valores de k para que una cuadrática no tenga ceros",
                "prompt": "¿Para qué valores de k la función f(x) = x² + 4x + k no tiene ceros reales?",
                "answer": "k > 4: no tiene ceros reales cuando Δ < 0. Δ = 4² − 4.1.k = 16 − 4k < 0 → 16 < 4k → k > 4. Con k = 4 tiene un cero doble y con k < 4 tiene dos ceros distintos.",
                "hints": ["Sin ceros reales ↔ Δ < 0.", "Al despejar k de 16 − 4k < 0, fijate hacia dónde queda la desigualdad."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["k > 4", "k < 4", "k = 4"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Conjunto de positividad de una cuadrática con a negativo",
                "prompt": "Para f(x) = −(x − 1)(x − 5), ¿cuál es el conjunto de positividad C⁺?",
                "answer": "C⁺ = (1; 5): los ceros son 1 y 5 y, como a = −1 < 0, la parábola tiene las ramas hacia abajo, así que queda por encima del eje x solo entre los ceros. Los ceros no entran (allí f vale 0). Afuera, C⁻ = (−∞; 1) ∪ (5; +∞). Prueba: f(3) = −(2)(−2) = 4 > 0.",
                "hints": ["Marcá los ceros en la recta y pensá hacia dónde van las ramas.", "Probá con un valor entre los ceros, por ejemplo x = 3."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(1; 5)", "(−∞; 1) ∪ (5; +∞)", "[1; 5]"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ordenada al origen de una cuadrática en forma canónica",
                "prompt": "¿Cuál es la ordenada al origen de f(x) = 2(x − 3)² − 5? Respondé solo con el número.",
                "answer": "13: la ordenada al origen es f(0) = 2.(0 − 3)² − 5 = 2.9 − 5 = 13. El −5 de la forma canónica es la ordenada del vértice, no la ordenada al origen; en la forma polinómica f(x) = 2x² − 12x + 13 se ve directo como término independiente.",
                "hints": ["La ordenada al origen es el valor de la función cuando x = 0."],
                "payload": {"check": {"type": "numeric", "value": 13, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "De polinómica a factorizada con la resolvente",
                "prompt": "Escribí f(x) = 2x² − 2x − 12 en forma factorizada.",
                "answer": "f(x) = 2(x − 3)(x + 2): con la resolvente, x₁,₂ = (2 ± √(4 + 96))/4 = (2 ± 10)/4, o sea x₁ = 3 y x₂ = −2. La forma factorizada es a(x − x₁)(x − x₂) y no hay que olvidar a = 2. Dividir por 2 en vez de por 2a = 4 da los ceros falsos 6 y −4.",
                "hints": ["Calculá Δ = b² − 4ac y los ceros con la resolvente.", "El coeficiente principal queda adelante: a(x − x₁)(x − x₂)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["2(x − 3)(x + 2)", "(x − 3)(x + 2)", "2(x + 3)(x − 2)", "2(x − 6)(x + 4)"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== POLÍGONOS Y CUADRILÁTEROS ====================
    {
        "slug": "g-poligonos-cuadrilateros",
        "title": "Polígonos y cuadriláteros: ángulos interiores y exteriores, clasificación y áreas",
        "summary": "Nombrar y usar los pares de ángulos entre paralelas y entre rectas que se cortan, calcular ángulos interiores y exteriores de polígonos (en grados y minutos), clasificar cuadriláteros como en el ingreso y hallar perímetros y áreas de figuras compuestas con arcos.",
        "prerequisites": ["g-angulos-rectas"],
        "insert_after": "g-angulos-rectas",
        "metadata": {"section": "Geometría", "lab_tab": "geometry_angles", "est_minutes": 30},
        "items": [
            {
                "item_type": "recall",
                "title": "Nombre y propiedad de los conjugados internos",
                "prompt": "Dos paralelas son cortadas por una transversal. Dos de los ocho ángulos que se forman son no adyacentes, ambos internos (entre las paralelas) y están del mismo lado de la transversal. ¿Cómo se llaman y qué propiedad cumplen?",
                "answer": "Conjugados internos, y son suplementarios (suman 180°). Si estuvieran en distinto semiplano respecto de la transversal serían alternos internos (congruentes); si uno fuera interno y el otro externo, del mismo lado, serían correspondientes (congruentes).",
                "hints": [
                    "\"Alternos\" = de distinto lado de la transversal; \"conjugados\" = del mismo lado.",
                    "Los conjugados son los únicos pares entre paralelas que no son iguales.",
                ],
                "payload": {
                    "lab_link": "math:geometry_angles",
                    "check": {
                        "type": "choice",
                        "options": [
                            "Conjugados internos: son suplementarios",
                            "Alternos internos: son congruentes",
                            "Correspondientes: son congruentes",
                            "Conjugados externos: son suplementarios",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ángulos conjugados externos con una incógnita",
                "prompt": "Entre dos paralelas cortadas por una transversal, α = 3x + 10° y β = 2x + 20° son conjugados externos. ¿Cuánto mide α? Respondé solo con el número (en grados).",
                "answer": "100°: los conjugados externos son suplementarios, así que (3x + 10°) + (2x + 20°) = 180° → 5x + 30° = 180° → x = 30°. Entonces α = 3.30° + 10° = 100° y β = 80°; verificación: 100° + 80° = 180° ✓.",
                "hints": ["Conjugados (internos o externos) ⇒ suman 180°.", "Primero hallá x y después reemplazalo en α."],
                "payload": {"check": {"type": "numeric", "value": 100, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Ángulo interior de un octógono regular",
                "prompt": "¿Cuánto mide cada ángulo interior de un octógono regular? Respondé solo con el número (en grados).",
                "answer": "135°: la suma de los ángulos interiores es 180°.(n − 2) = 180°.6 = 1080°, y en un polígono regular todos son iguales: 1080° : 8 = 135°. Otra forma: cada exterior mide 360° : 8 = 45° y el interior es su suplemento, 180° − 45° = 135°.",
                "hints": ["Suma de interiores: 180°.(n − 2).", "Regular: repartí esa suma en partes iguales."],
                "payload": {"check": {"type": "numeric", "value": 135, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Cantidad de lados a partir del ángulo exterior",
                "prompt": "Cada ángulo exterior de un polígono regular mide 24°. ¿Cuántos lados tiene? Respondé solo con el número.",
                "answer": "15: en todo polígono convexo los ángulos exteriores suman 360°, y en uno regular son todos iguales: n = 360° : 24° = 15 (un pentadecágono). Cada ángulo interior mide 180° − 24° = 156°.",
                "hints": ["La suma de los exteriores no depende de la cantidad de lados."],
                "payload": {"check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Ángulo exterior de un triángulo con una incógnita",
                "prompt": "En un triángulo, un ángulo exterior mide 2x + 15° y los dos ángulos interiores no adyacentes a él miden x + 20° y 40°. ¿Cuánto mide el ángulo exterior? Respondé solo con el número (en grados).",
                "answer": "105°: un ángulo exterior de un triángulo es igual a la suma de los dos interiores no adyacentes a él: 2x + 15° = (x + 20°) + 40° → x = 45°. El exterior mide 2.45° + 15° = 105°; los interiores son 65°, 40° y 75° (el adyacente, 180° − 105°), que suman 180° ✓.",
                "hints": ["No hace falta el tercer ángulo interior: usá la propiedad del ángulo exterior."],
                "payload": {"check": {"type": "numeric", "value": 105, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "recall",
                "title": "Cuadrilátero con un solo par de lados paralelos",
                "prompt": "Según la clasificación del material del ingreso, ¿cómo se llama un cuadrilátero que tiene UN solo par de lados paralelos?",
                "answer": "Trapecio: tiene un solo par de lados paralelos, llamados bases. Los paralelogramos tienen dos pares de lados opuestos paralelos y los trapezoides no tienen ningún lado paralelo. (Otras bibliografías definen el trapecio distinto; en el ingreso se usa esta.)",
                "hints": ["Paralelogramo: dos pares de lados paralelos; trapezoide: ninguno."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Trapecio", "Trapezoide", "Paralelogramo"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ángulos iguales de una cometa o deltoide",
                "prompt": "ABCD es una cometa (deltoide) con AB = AD y CB = CD, simétrica respecto de la diagonal AC. Si Â = 100° y Ĉ = 48°, ¿cuánto mide B̂? Respondé solo con el número (en grados).",
                "answer": "106°: por la simetría respecto de AC, los ángulos B̂ y D̂ son iguales. Como los interiores de un cuadrilátero suman 360°: 100° + 48° + 2.B̂ = 360° → 2.B̂ = 212° → B̂ = 106°.",
                "hints": ["¿Qué par de ángulos queda igual por la simetría respecto de AC?", "Los ángulos interiores de cualquier cuadrilátero suman 360°."],
                "payload": {"check": {"type": "numeric", "value": 106, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Ángulo suplementario en grados y minutos",
                "prompt": "En un trapecio isósceles, cada ángulo de la base mayor mide 67°25′. ¿Cuánto mide cada ángulo de la base menor?",
                "answer": "112°35′: cada ángulo de la base menor y el de la base mayor del mismo lado son conjugados internos entre las bases paralelas, así que suman 180°. Para restar se pide prestado un grado: 180° = 179°60′, y 179°60′ − 67°25′ = 112°35′. Tomar 67°25′ como si fuera 67,25° (y obtener 112,75°) es un error: 25′ son 25/60 de grado.",
                "hints": ["Ángulos consecutivos sobre un lado no paralelo del trapecio suman 180°.", "1° = 60′: escribí 180° como 179°60′ antes de restar."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["112°35′", "113°35′", "22°35′", "112,75°"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Área sombreada de un rectángulo con dos círculos",
                "prompt": "Un rectángulo ABCD tiene el lado mayor AB = 20 cm y contiene dos círculos iguales, uno al lado del otro, tangentes entre sí y tangentes a los lados del rectángulo (cada círculo toca tres lados). La región sombreada es la parte del rectángulo que queda fuera de los círculos. ¿Cuál es su área? Respondé solo con el número, en cm², redondeado a dos decimales.",
                "answer": "42,92 cm²: los dos diámetros ocupan el largo, así que 2.2r = 20 cm → r = 5 cm, y el ancho del rectángulo es un diámetro, 10 cm. Área = 20.10 − 2.π.5² = 200 − 50π ≈ 42,92 cm².",
                "hints": [
                    "El largo del rectángulo equivale a dos diámetros y el ancho, a uno.",
                    "Área sombreada = área del rectángulo − área de los dos círculos.",
                ],
                "payload": {"check": {"type": "numeric", "value": 42.92, "tolerance": 0.002, "unit": "cm²"}},
            },
            {
                "item_type": "worked_example",
                "title": "Perímetro de una región limitada por un arco",
                "prompt": "En un cuadrado ABCD de 10 cm de lado se traza el arco de circunferencia con centro en A y radio 10 cm, que va de B a D. La región sombreada es la parte del cuadrado que queda fuera de ese cuarto de círculo. ¿Cuál es su perímetro? Respondé solo con el número, en cm, redondeado a dos decimales.",
                "answer": "35,71 cm: el borde de la región está formado por los lados BC y CD (10 cm cada uno) y por el arco BD, que es un cuarto de circunferencia: 2.π.10/4 = 5π cm. Perímetro = 20 + 5π ≈ 35,71 cm. Los lados AB y AD no forman parte del borde sombreado.",
                "hints": [
                    "Recorré el borde de la región sombreada: ¿qué lados del cuadrado toca?",
                    "Longitud de arco = (ángulo/360°).2πr.",
                ],
                "payload": {"check": {"type": "numeric", "value": 35.71, "tolerance": 0.002, "unit": "cm"}},
            },
        ],
    },
    # ==================== LOS SIETE CASOS DE FACTOREO ====================
    {
        "slug": "a2-casos-factoreo",
        "title": "Los siete casos de factoreo y la factorización combinada",
        "summary": "Reconocer y aplicar los siete casos de factoreo del ingreso, elegir cuáles probar según la cantidad de términos, combinarlos hasta llegar a factores primos y calcular el m.c.m. de polinomios.",
        "prerequisites": ["a2-division-polinomios"],
        "insert_after": "a2-division-polinomios",
        "metadata": {"section": "Álgebra 2", "lab_tab": "factoring", "est_minutes": 30},
        "items": [
            {
                "item_type": "recall",
                "title": "Casos de factoreo para un binomio según la tabla",
                "prompt": "Según la tabla de casos de factoreo por cantidad de términos, ¿qué casos se prueban (y en qué orden) cuando el polinomio tiene 2 términos?",
                "answer": "1° − 5° − 6°: factor común, diferencia de cuadrados y suma o diferencia de potencias de igual exponente. Para 3 términos son 1° − 3° − 7°, para 4 términos 1° − 4° − 2°, para 5 términos solo el 1° y para 6 términos 1° − 2°. El 1° caso se intenta siempre primero.",
                "hints": ["Pensá qué casos tienen exactamente dos términos: a² − b² y xⁿ ± aⁿ."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["1° − 5° − 6°", "1° − 3° − 7°", "1° − 4° − 2°", "1° − 2°"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Factor común por grupos en un polinomio de cuatro términos",
                "prompt": "Factorizá x³ − 2x² + 5x − 10 con el 2° caso (factor común por grupos).",
                "answer": "(x − 2)(x² + 5): agrupando de a dos, x²(x − 2) + 5(x − 2); los paréntesis quedan iguales y se extraen como factor común. Ojo con el signo: de 5x − 10 se saca +5, porque 5(x − 2) = 5x − 10. x² + 5 no se factoriza en IR.",
                "hints": ["Sacá factor común en (x³ − 2x²) y en (5x − 10) por separado.", "Los dos paréntesis tienen que quedar iguales."],
                "payload": {
                    "lab_link": "math:factoring",
                    "check": {
                        "type": "choice",
                        "options": ["(x − 2)(x² + 5)", "(x − 2)(x² − 5)", "(x + 2)(x² + 5)", "(x² − 2)(x + 5)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Reconocer un trinomio cuadrado perfecto con término negativo",
                "prompt": "Factorizá 9x² − 30x + 25 con el 3° caso.",
                "answer": "(3x − 5)²: los términos cuadrados son 9x² y 25, con raíces 3x y 5; el doble producto 2.3x.5 = 30x coincide en valor absoluto con el término restante, y como es −30x el binomio lleva un signo menos. No es una diferencia de cuadrados: tiene tres términos.",
                "hints": ["Buscá las raíces cuadradas de los dos términos cuadrados.", "Verificá que el término restante sea ±2ab y mirá su signo."],
                "payload": {
                    "lab_link": "math:factoring",
                    "check": {
                        "type": "choice",
                        "options": ["(3x − 5)²", "(3x + 5)²", "(3x − 5)(3x + 5)", "(9x − 5)²"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Término que completa un trinomio cuadrado perfecto",
                "prompt": "¿Qué término independiente hay que sumarle a x² − 10x para que sea un trinomio cuadrado perfecto? Respondé solo con el número.",
                "answer": "25: comparando con x² + 2ax + a², 2a = −10 → a = −5 y el término que falta es a² = 25. Queda x² − 10x + 25 = (x − 5)². Atajo: es el cuadrado de la mitad del coeficiente de x.",
                "hints": ["Compará x² − 10x con x² + 2ax + a²: ¿cuánto vale a?"],
                "payload": {"check": {"type": "numeric", "value": 25, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Cuatrinomio cubo perfecto con signos alternados",
                "prompt": "Factorizá 8x³ − 12x² + 6x − 1 con el 4° caso.",
                "answer": "(2x − 1)³: los términos cubos son 8x³ y −1, con raíces cúbicas 2x y −1 (con su signo). Se verifica 3.(2x)².(−1) = −12x² y 3.(2x).(−1)² = 6x, que coinciden en valor y en signo con los otros dos términos. El patrón de signos + − + − corresponde a (a − b)³.",
                "hints": [
                    "Calculá las raíces cúbicas de los términos cubos, cada una con su signo.",
                    "Comprobá 3a²b y 3ab² con signo incluido.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(2x − 1)³", "(2x + 1)³", "(8x − 1)³", "(2x − 1)²(2x + 1)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Diferencia de cuadrados con el orden correcto",
                "prompt": "Factorizá 25x² − 64 con el 5° caso.",
                "answer": "(5x − 8)(5x + 8): las raíces cuadradas de los términos son 5x y 8, y la diferencia de cuadrados se factoriza como (suma de las raíces).(resta de las raíces). Escribir (8 − 5x)(8 + 5x) está mal: ese producto da 64 − 25x², el opuesto.",
                "hints": ["a² − b² = (a + b)(a − b): identificá a y b.", "Respetá cuál término es positivo y cuál negativo."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(5x − 8)(5x + 8)", "(8 − 5x)(8 + 5x)", "(5x − 8)²"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Diferencia de potencias quintas con Ruffini",
                "prompt": "Factorizá x⁵ − 32 con el 6° caso (el segundo factor se obtiene por Ruffini).",
                "answer": "(x − 2)(x⁴ + 2x³ + 4x² + 8x + 16): 32 = 2⁵, así que el primer factor es (x − 2), con las raíces quintas de los términos y su signo. Dividiendo x⁵ + 0x⁴ + 0x³ + 0x² + 0x − 32 por (x − 2) con Ruffini se obtienen los coeficientes 1, 2, 4, 8, 16 y resto 0. En una diferencia, todos los signos del segundo factor son +.",
                "hints": [
                    "Completá con ceros los coeficientes que faltan antes de usar Ruffini.",
                    "En Ruffini se usa la raíz de x − 2, o sea 2.",
                ],
                "payload": {
                    "lab_link": "math:factoring",
                    "check": {
                        "type": "choice",
                        "options": [
                            "(x − 2)(x⁴ + 2x³ + 4x² + 8x + 16)",
                            "(x − 2)(x⁴ − 2x³ + 4x² − 8x + 16)",
                            "(x + 2)(x⁴ − 2x³ + 4x² − 8x + 16)",
                            "(x − 2)⁵",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Trinomio de segundo grado con coeficiente principal 2",
                "prompt": "Factorizá 2x² + 5x − 3 con el 7° caso.",
                "answer": "2(x − 1/2)(x + 3): con la resolvente, x₁,₂ = (−5 ± √(25 + 24))/4 = (−5 ± 7)/4, o sea x₁ = 1/2 y x₂ = −3. La factorización es a(x − x₁)(x − x₂), con los ceros con signo opuesto y sin olvidar a = 2. Es equivalente a (2x − 1)(x + 3).",
                "hints": ["Δ = 25 + 24 = 49; el denominador de la resolvente es 2a = 4.", "Adelante va el coeficiente principal a."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["2(x − 1/2)(x + 3)", "(x − 1/2)(x + 3)", "2(x + 1/2)(x − 3)", "2(x − 1)(x + 6)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Factorización combinada hasta factores primos",
                "prompt": "Factorizá por completo 2x⁵ − 32x (hasta que ningún factor se pueda factorizar más).",
                "answer": "2x(x² + 4)(x − 2)(x + 2): 1° caso → 2x(x⁴ − 16); 5° caso → 2x(x² − 4)(x² + 4); otra vez 5° caso en x² − 4 → 2x(x − 2)(x + 2)(x² + 4). x² + 4 es primo en IR. Verificación con x = 1: 2 − 32 = −30 y 2.1.5.(−1).3 = −30 ✓.",
                "hints": [
                    "Empezá siempre por el factor común.",
                    "Después de cada paso, revisá si algún factor todavía es una diferencia de cuadrados.",
                ],
                "payload": {
                    "lab_link": "math:factoring",
                    "check": {
                        "type": "choice",
                        "options": [
                            "2x(x² + 4)(x − 2)(x + 2)",
                            "2x(x − 2)²(x + 2)²",
                            "2(x² + 4)(x − 2)(x + 2)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Mínimo común múltiplo de tres polinomios",
                "prompt": "Hallá el m.c.m. de P = x² − 9, Q = x² + 6x + 9 y R = 2x + 6.",
                "answer": "2(x − 3)(x + 3)²: factorizando, P = (x − 3)(x + 3), Q = (x + 3)² y R = 2(x + 3). El m.c.m. multiplica los factores comunes y no comunes con su mayor exponente: 2, (x − 3) y (x + 3)². Multiplicar los tres polinomios daría 2(x − 3)(x + 3)⁴, un múltiplo común pero no el mínimo.",
                "hints": ["Factorizá cada polinomio primero.", "Cada factor distinto va una sola vez, con el mayor exponente con que aparece."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["2(x − 3)(x + 3)²", "x + 3", "2(x − 3)(x + 3)⁴", "(x − 3)(x + 3)"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
]


INGRESO_MATH_B_LESSONS: dict[str, dict] = {
    "al-sel-metodos-clasificacion": {
        "hook": {
            "question": "Un plan de celular cobra $2000 fijos más $500 por GB y otro cobra $5000 fijos más $200 por GB. ¿Hay algún consumo en el que cuesten lo mismo? ¿Pasa siempre con dos planes cualesquiera?",
            "intuition": "Cada plan es una recta: `y = 500x + 2000` e `y = 200x + 5000`. Se cortan en `x = 10` GB, donde los dos cuestan $7000: es un sistema con **solución única**. Pero si dos planes tuvieran el mismo precio por GB (misma pendiente), nunca se cruzarían (sin solución) o serían el mismo plan (infinitas soluciones). Mirando pendientes y ordenadas se sabe qué pasa **sin resolver**.",
        },
        "concept": {
            "points": [
                "**La recta**: el ángulo de inclinación α es el que forma con el semieje positivo de las x (`0° ≤ α < 180°`) y la pendiente es `m = tg α = (y₂ − y₁)/(x₂ − x₁)`. Explícita: `y = mx + b`. **General**: `Ax + By + C = 0`, con A y B no nulos a la vez; no es única (se puede multiplicar por cualquier número ≠ 0). Equivale a la forma estándar `Ax + By = D` que usa la app, con `D = −C` (C pasa de miembro cambiando el signo).",
                "**Horizontales y verticales**: `y = b` tiene pendiente 0 (α = 0°); `x = a` es vertical y **no tiene pendiente** ni ecuación explícita. **Paralelas**: `m₁ = m₂`. **Perpendiculares**: pendientes opuestas y recíprocas, `m₁ = −1/m₂`. Las verticales son paralelas entre sí y perpendiculares a cualquier horizontal.",
                "**SEL 2×2**: cada ecuación lineal es una recta, y la solución son los puntos comunes. Métodos: **gráfico** (graficar y leer el cruce), **sustitución** (despejar una incógnita y reemplazarla en la otra ecuación), **igualación** (despejar la misma incógnita en las dos e igualar) y **reducción** o sumas y restas (multiplicar para que una incógnita tenga coeficientes iguales u opuestos y restar o sumar).",
                "**Clasificación**: **SCD** (compatible determinado): rectas secantes, pendientes distintas, `S = {(x₀; y₀)}`. **SCI** (compatible indeterminado): paralelas coincidentes, igual pendiente e igual ordenada al origen, por ejemplo `S = {(x; 2x − 3), x ∈ IR}`. **SI** (incompatible): paralelas disjuntas, igual pendiente y distinta ordenada, `S = { }`. Al resolver, una identidad (`0 = 0`) indica SCI y un absurdo (`−2 = 5`) indica SI.",
                "**Sin resolver, por proporcionalidad** en `{ax + by = c ; a′x + b′y = c′}`: `a/a′ ≠ b/b′` → SCD; `a/a′ = b/b′ = c/c′` → SCI; `a/a′ = b/b′ ≠ c/c′` → SI. **Con un parámetro k**: se plantea `a/a′ = b/b′`, se despeja el o los valores críticos de k (para los demás es SCD) y, para cada uno, se compara `c/c′`. Si algún coeficiente es 0, conviene comparar pendientes despejando y.",
                "**Problemas de planteo**: definí las incógnitas con precisión (\"x: cantidad de mesas de 3 patas\", no \"x: mesas\"), armá cada ecuación con la idea \"la suma de las partes es igual al todo\", resolvé y **verificá** en las dos ecuaciones y en el enunciado.",
            ],
            "real_world": [
                {
                    "title": "Rampas y caminos en obra",
                    "detail": "Una rampa con pendiente del 8 % tiene `m = 0,08`, y su ángulo de inclinación es `α = arctg 0,08 ≈ 4,6°`. En planos y en topografía, la pendiente es la tangente del ángulo.",
                },
                {
                    "title": "Mezclas en el laboratorio",
                    "detail": "Para preparar 1000 ml de salmuera al 14 % mezclando soluciones al 5 % y al 20 % se plantean dos ecuaciones: una para el volumen total y otra para la cantidad de sal. Es un SEL 2×2 de los que aparecen en el práctico.",
                },
                {
                    "title": "Circuitos y estructuras",
                    "detail": "Las leyes de Kirchhoff en un circuito con dos mallas, o el equilibrio de un nudo de una cercha con dos barras, dan sistemas lineales: si el sistema resulta incompatible o indeterminado, el modelo está mal planteado.",
                },
            ],
            "key_rule": "m = tg α = Δy/Δx | Paralelas: m₁ = m₂ | Perpendiculares: m₁ = −1/m₂ | SCD: a/a′ ≠ b/b′ (secantes) | SCI: a/a′ = b/b′ = c/c′ (coincidentes) | SI: a/a′ = b/b′ ≠ c/c′ (paralelas disjuntas).",
            "pitfall": "Al llegar a `0 = 0`, creer que la solución es x = 0 (en realidad hay infinitas: SCI); y al llegar a `0 = 5`, pensar que hubo un error (es un SI, `S = { }`). En perpendiculares, cambiar solo el signo o solo dar vuelta la fracción: hay que hacer las dos cosas.",
        },
        "example": {
            "title": "Clasificar { x + ky = 1 ; kx + y = 1 } según k y resolverlo para k = 2",
            "steps": [
                "Para k ≠ 0 comparamos los coeficientes: `1/k = k/1` → `k² = 1` → `k = 1` o `k = −1`. Para cualquier otro k los cocientes son distintos: rectas secantes, **SCD**. (Con k = 0 queda x = 1, y = 1: también SCD.)",
                "**k = 1**: las dos ecuaciones son `x + y = 1`; también `c/c′ = 1/1 = 1`. Rectas coincidentes: **SCI**, `S = {(x; 1 − x), x ∈ IR}`.",
                "**k = −1**: queda `{x − y = 1 ; −x + y = 1}`. Los coeficientes dan `1/(−1) = (−1)/1 = −1`, pero `c/c′ = 1/1 = 1 ≠ −1`. Paralelas disjuntas: **SI**, `S = { }`.",
                "**k = 2** por reducción: `{x + 2y = 1 ; 2x + y = 1}`. Multiplicamos la primera por 2: `2x + 4y = 2`, y le restamos la segunda: `3y = 1` → `y = 1/3`. Reemplazando: `x = 1 − 2.(1/3) = 1/3`.",
                "Verificación: `1/3 + 2.(1/3) = 1` ✓ y `2.(1/3) + 1/3 = 1` ✓. `S = {(1/3; 1/3)}`: el punto donde se cortan las dos rectas.",
            ],
            "lab_link": "math:systems",
            "lab_cta": "Practicar sistemas 2×2",
        },
        "check": {
            "question": "¿Qué pendiente tiene una recta perpendicular a `4x − 2y + 1 = 0`?",
            "options": [
                {"text": "`−1/2`", "ok": True, "feedback": "Exacto: despejando, y = 2x + 1/2, así que m = 2; la perpendicular tiene pendiente opuesta y recíproca, −1/2."},
                {"text": "`−2`", "ok": False, "feedback": "Cambiaste el signo pero no diste vuelta la fracción: (−2).2 = −4, no −1. Tiene que ser opuesta y recíproca."},
                {"text": "`1/2`", "ok": False, "feedback": "Diste vuelta la fracción pero no cambiaste el signo: (1/2).2 = 1, no −1. Falta el signo opuesto."},
            ],
        },
        "checks": [
            {
                "question": "Resolviendo `{ y = 2x − 3 ; x − y/2 = 3/2 }` por sustitución, las x se cancelan y queda `3/2 = 3/2`. ¿Cuál es el conjunto solución?",
                "options": [
                    {"text": "`S = {(x; 2x − 3), x ∈ IR}`", "ok": True, "feedback": "Exacto: una identidad indica SCI (rectas coincidentes); cada par de la recta y = 2x − 3 es solución."},
                    {"text": "`S = { }`", "ok": False, "feedback": "El conjunto vacío corresponde a un absurdo (por ejemplo −2 = 5). Acá se llegó a una igualdad verdadera, que vale para todo x."},
                    {"text": "`S = {(3/2; 0)}`", "ok": False, "feedback": "El 3/2 no es un valor de x: la x desapareció. Con una identidad hay infinitas soluciones, no una sola."},
                ],
            },
            {
                "question": "Sin resolverlo, ¿cómo es el sistema `{ y = 3x + 6 ; 6x − 2y = 4 }`?",
                "options": [
                    {"text": "Compatible determinado", "ok": False, "feedback": "Despejando la segunda, y = 3x − 2: la pendiente es 3 en las dos rectas, así que no son secantes."},
                    {"text": "Compatible indeterminado", "ok": False, "feedback": "Para ser coincidentes también tendría que coincidir la ordenada al origen, y es 6 en una y −2 en la otra."},
                    {"text": "Incompatible", "ok": True, "feedback": "Exacto: misma pendiente (3) y distinta ordenada al origen (6 y −2): paralelas disjuntas, S = { }."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá cómo te das cuenta, sin resolverlo, de si un sistema 2×2 es SCD, SCI o SI: con pendientes y ordenadas al origen y con la proporcionalidad de los coeficientes.",
    },
    "al-cuadratica-formas": {
        "hook": {
            "question": "El chorro de una fuente sigue la curva `h(x) = −x² + 4x` (en metros). ¿Qué altura máxima alcanza y a qué distancia vuelve a caer al nivel del piso?",
            "intuition": "La misma parábola se puede escribir de tres maneras, y cada una muestra algo distinto: `−(x − 2)² + 4` muestra el **vértice** (2; 4), o sea, altura máxima de 4 m; `−x(x − 4)` muestra los **ceros** 0 y 4 (sale del piso y vuelve a caer a 4 m); y `−x² + 4x` muestra la **ordenada al origen**, 0. Saber pasar de una forma a otra es saber leer la parábola.",
        },
        "concept": {
            "points": [
                "**Tres formas, el mismo a**: polinómica `f(x) = ax² + bx + c` (c es la ordenada al origen); canónica `f(x) = a(x − xᵥ)² + yᵥ` (vértice `V = (xᵥ; yᵥ)` a la vista; en la app aparece como `a(x − h)² + k`, con h = xᵥ y k = yᵥ); factorizada `f(x) = a(x − x₁)(x − x₂)` (ceros a la vista, solo si Δ ≥ 0).",
                "**Vértice y eje**: `xᵥ = −b/(2a)` y `yᵥ = f(xᵥ)`; si hay ceros, también `xᵥ = (x₁ + x₂)/2`. El **eje de simetría** es la recta vertical `x = xᵥ` (es una ecuación, no un número). Dominio: IR. Si a > 0 las ramas van hacia arriba e `Im = [yᵥ; +∞)`; si a < 0 van hacia abajo e `Im = (−∞; yᵥ]`.",
                "**Pasar de forma**: de polinómica a canónica se **completan cuadrados** (`x² + 6x + 5 = (x² + 6x + 9) − 9 + 5 = (x + 3)² − 4`) o se calculan xᵥ e yᵥ y se reemplazan. De polinómica a factorizada, se buscan los ceros con la resolvente. De canónica o factorizada a polinómica, se desarrolla.",
                "**Ceros y discriminante**: `x₁,₂ = (−b ± √Δ)/(2a)` con `Δ = b² − 4ac`. Δ > 0: dos ceros distintos (corta el eje x en dos puntos); Δ = 0: un cero doble (toca el eje en el vértice); Δ < 0: no tiene ceros reales. **Con un parámetro**, se plantea Δ > 0, Δ = 0 o Δ < 0 y se despeja.",
                "**C⁺ y C⁻**: con a > 0 la función es negativa entre los ceros y positiva afuera; con a < 0, al revés. Los ceros no entran (intervalos abiertos). Si Δ < 0, la parábola queda entera de un lado: `C⁺ = IR` si a > 0, o `C⁻ = IR` si a < 0.",
                "**Ordenada al origen**: es `f(0)`. En la polinómica es c; en la canónica es `a.xᵥ² + yᵥ` y en la factorizada `a.x₁.x₂`: hay que calcularla, no es yᵥ.",
            ],
            "real_world": [
                {
                    "title": "Tiro oblicuo",
                    "detail": "La altura de un proyectil en función de la distancia horizontal es una cuadrática con a < 0: el vértice da la altura máxima y el cero positivo, el alcance.",
                },
                {
                    "title": "Optimizar un corral",
                    "detail": "Con 40 m de alambre para un corral rectangular, el área es `A(x) = x(20 − x)`: ceros 0 y 20, vértice en x = 10, área máxima 100 m² (un cuadrado).",
                },
                {
                    "title": "Arcos y antenas",
                    "detail": "Muchos arcos de puentes y los reflectores de antenas tienen perfil parabólico; para replantearlos en obra se usa la forma canónica, centrada en el vértice.",
                },
            ],
            "key_rule": "Polinómica ax² + bx + c → ordenada c | Canónica a(x − xᵥ)² + yᵥ → vértice | Factorizada a(x − x₁)(x − x₂) → ceros | xᵥ = −b/(2a) = (x₁ + x₂)/2 | Δ > 0: 2 ceros; Δ = 0: 1; Δ < 0: ninguno.",
            "pitfall": "Leer mal los signos de la canónica: en `2(x + 3)² − 1` el vértice es (−3; −1), no (3; −1). Y olvidarse de a al escribir la factorizada: `2x² − 2x − 12` es `2(x − 3)(x + 2)`, no `(x − 3)(x + 2)`.",
        },
        "example": {
            "title": "Las tres formas de f(x) = 2x² − 4x − 6",
            "steps": [
                "**Vértice**: `xᵥ = −(−4)/(2.2) = 1` e `yᵥ = f(1) = 2 − 4 − 6 = −8`. `V = (1; −8)`, eje de simetría `x = 1`.",
                "**Canónica** completando cuadrados: `2(x² − 2x) − 6 = 2[(x − 1)² − 1] − 6 = 2(x − 1)² − 8`. Coincide con el vértice hallado.",
                "**Ceros**: `Δ = 16 + 48 = 64 > 0`, así que hay dos ceros: `x₁,₂ = (4 ± 8)/4` → `x₁ = 3`, `x₂ = −1`. **Factorizada**: `f(x) = 2(x − 3)(x + 1)`. Control: `(3 + (−1))/2 = 1 = xᵥ` ✓.",
                "**Ordenada al origen**: `f(0) = −6`. Como a = 2 > 0: `Im = [−8; +∞)`.",
                "**Signo**: `C⁻ = (−1; 3)` (entre los ceros) y `C⁺ = (−∞; −1) ∪ (3; +∞)`. Prueba: `f(0) = −6 < 0` ✓.",
            ],
            "lab_link": "math:quadratics",
            "lab_cta": "Explorar parábolas",
        },
        "check": {
            "question": "¿Cuál es el vértice de `f(x) = −3(x − 2)² + 5`?",
            "options": [
                {"text": "`(2; 5)`", "ok": True, "feedback": "Exacto: en a(x − xᵥ)² + yᵥ se lee xᵥ = 2 e yᵥ = 5; como a < 0, es el punto más alto."},
                {"text": "`(−2; 5)`", "ok": False, "feedback": "El paréntesis es (x − 2): el signo menos ya es parte de la fórmula, así que xᵥ = 2, no −2."},
                {"text": "`(5; 2)`", "ok": False, "feedback": "Invertiste las coordenadas: la abscisa sale del paréntesis (2) y la ordenada es el término sumado (5)."},
            ],
        },
        "checks": [
            {
                "question": "`f(x) = x² + 2x + k` tiene exactamente un cero. ¿Cuánto vale k?",
                "options": [
                    {"text": "`k = 1`", "ok": True, "feedback": "Exacto: Δ = 2² − 4.1.k = 4 − 4k = 0 → k = 1, y queda (x + 1)²."},
                    {"text": "`k = −1`", "ok": False, "feedback": "Error de signo en Δ: es b² − 4ac = 4 − 4k, no 4 + 4k. Con k = −1, Δ = 8 > 0 y hay dos ceros."},
                    {"text": "`k = 4`", "ok": False, "feedback": "Te faltó el 4 de 4ac: planteaste 4 − k = 0. Con k = 4, Δ = 4 − 16 = −12 < 0 y no hay ceros."},
                ],
            },
            {
                "question": "Si `f(x) = a(x − x₁)(x − x₂)` con a > 0 y x₁ < x₂, ¿dónde es negativa f?",
                "options": [
                    {"text": "En `(x₁; x₂)`, entre los ceros", "ok": True, "feedback": "Exacto: con las ramas hacia arriba, la parábola baja del eje x solo entre los ceros."},
                    {"text": "En `(−∞; x₁) ∪ (x₂; +∞)`", "ok": False, "feedback": "Eso sería con a < 0. Con a > 0 las ramas suben, así que afuera de los ceros la función es positiva."},
                    {"text": "En todo IR", "ok": False, "feedback": "Una parábola con dos ceros cambia de signo: no puede ser negativa en todo IR."},
                ],
            },
        ],
        "takeaway_prompt": "Contá qué dato se lee directo en cada una de las tres formas de una cuadrática y cómo pasás de la forma polinómica a las otras dos.",
    },
    "g-poligonos-cuadrilateros": {
        "hook": {
            "question": "¿Por qué las baldosas hexagonales encajan sin dejar huecos y las pentagonales regulares no?",
            "intuition": "En cada vértice donde se juntan baldosas, los ángulos tienen que sumar 360°. El ángulo interior de un hexágono regular mide `(6 − 2).180°/6 = 120°`, y tres de ellos dan justo 360°. El de un pentágono regular mide 108°, y 360°/108° ≈ 3,33 no es entero: siempre queda un hueco. Todo sale de una fórmula: la suma de los ángulos interiores.",
        },
        "concept": {
            "points": [
                "**Entre dos rectas que se cortan**: **consecutivos** (mismo vértice y un lado común, sin superponerse); **adyacentes** (un lado común y los otros dos son semirrectas opuestas): suman 180°; **opuestos por el vértice** (los lados de uno son semirrectas opuestas a los del otro): son congruentes.",
                "**Paralelas cortadas por una transversal** (8 ángulos: 4 internos y 4 externos, siempre pares no adyacentes): **correspondientes** (uno interno y otro externo, del mismo lado de la transversal), **alternos internos** y **alternos externos** (de distinto lado): son **congruentes**. **Conjugados internos** y **conjugados externos** (del mismo lado): son **suplementarios**.",
                "**Polígono convexo de n lados**: la suma de los interiores es `180°.(n − 2)` y la de los exteriores es **360°** para cualquier n. En un polígono **regular** (lados y ángulos iguales), cada interior mide `180°.(n − 2)/n` y cada exterior `360°/n`; interior + exterior = 180°. En un **triángulo**, un ángulo exterior es igual a la suma de los dos interiores no adyacentes.",
                "**Cuadriláteros** (como en el material del ingreso; la bibliografía varía): **paralelogramos**, con dos pares de lados opuestos paralelos (rectángulo, rombo, cuadrado); **trapecios**, con UN solo par de lados paralelos, las bases (escaleno, isósceles, rectángulo); **trapezoides**, sin lados paralelos, entre ellos la **cometa o deltoide** (trapezoide simétrico: dos pares de lados consecutivos congruentes; el material de apoyo lo llama romboide). En cualquier cuadrilátero los interiores suman 360°.",
                "**Grados y minutos**: `1° = 60′`. Para restar se pide prestado un grado: `180° − 67°25′ = 179°60′ − 67°25′ = 112°35′`. Y `104,5° = 104°30′`.",
                "**Figuras compuestas**: descomponé en figuras conocidas y sumá o restá áreas. Longitud de arco = `(ángulo/360°).2πr`. El perímetro es solo el borde de la región pedida: arcos más segmentos, sin contar líneas interiores.",
            ],
            "real_world": [
                {
                    "title": "Panales y pisos",
                    "detail": "Las abejas y los fabricantes de cerámicos usan hexágonos: tres ángulos de 120° cierran exactamente 360° y cubren el plano sin huecos.",
                },
                {
                    "title": "Marcos a inglete",
                    "detail": "Para un marco octogonal regular, cada ángulo exterior mide 360°/8 = 45° y cada pieza se corta a 22,5° en sus extremos: la mitad del exterior.",
                },
                {
                    "title": "Cerchas y vigas",
                    "detail": "En una cercha con cordones paralelos, las diagonales forman ángulos alternos internos iguales con los dos cordones: con un solo ángulo medido se conocen todos.",
                },
            ],
            "key_rule": "Correspondientes, alternos internos y alternos externos: congruentes | Conjugados (internos o externos) y adyacentes: suplementarios | Opuestos por el vértice: congruentes | Σ interiores = 180°.(n − 2) | Σ exteriores = 360° | Exterior del triángulo = suma de los dos interiores no adyacentes.",
            "pitfall": "Confundir conjugados con alternos: los conjugados **suman** 180°, no son iguales. Y restar grados y minutos como si fueran decimales: `180° − 67°25′` no es 112,75° ni 113°35′, sino 112°35′.",
        },
        "example": {
            "title": "Un polígono regular cuyo ángulo interior es 4 veces el exterior",
            "steps": [
                "En cada vértice, el ángulo interior y el exterior son adyacentes: `i + e = 180°`. Con `i = 4e`: `5e = 180°` → `e = 36°`.",
                "Los exteriores suman 360° y en un polígono regular son todos iguales: `n = 360° : 36° = 10`. Es un **decágono**.",
                "El ángulo interior mide `i = 4.36° = 144°`. Control con la fórmula: `180°.(10 − 2)/10 = 1440°/10 = 144°` ✓.",
                "La suma de los interiores es 1440° y la de los exteriores, como en todo polígono convexo, 360°.",
            ],
            "lab_link": "math:geometry_angles",
            "lab_cta": "Practicar ángulos",
        },
        "check": {
            "question": "Dos paralelas son cortadas por una transversal y uno de los ángulos internos mide 65°. ¿Cuánto mide su conjugado interno?",
            "options": [
                {"text": "115°", "ok": True, "feedback": "Exacto: los conjugados internos son suplementarios, así que 180° − 65° = 115°."},
                {"text": "65°", "ok": False, "feedback": "Ese sería el alterno interno (congruente). El conjugado está del mismo lado de la transversal y suma 180° con el dado."},
                {"text": "25°", "ok": False, "feedback": "Calculaste el complemento (90° − 65°). Los conjugados suman 180°, no 90°."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuánto suman los ángulos interiores de un heptágono?",
                "options": [
                    {"text": "900°", "ok": True, "feedback": "Exacto: 180°.(7 − 2) = 180°.5 = 900°."},
                    {"text": "1260°", "ok": False, "feedback": "Multiplicaste 180° por 7. La fórmula es 180°.(n − 2): el heptágono se divide en 5 triángulos, no en 7."},
                    {"text": "360°", "ok": False, "feedback": "360° es la suma de los ángulos exteriores (de cualquier polígono convexo), no la de los interiores."},
                ],
            },
            {
                "question": "Según la clasificación del ingreso, todo cuadrado es…",
                "options": [
                    {"text": "rombo y rectángulo a la vez", "ok": True, "feedback": "Exacto: tiene los cuatro lados congruentes (rombo) y los cuatro ángulos rectos (rectángulo)."},
                    {"text": "un trapecio, porque tiene lados paralelos", "ok": False, "feedback": "En este material el trapecio tiene UN solo par de lados paralelos; el cuadrado tiene dos, así que es un paralelogramo."},
                    {"text": "un trapezoide", "ok": False, "feedback": "Los trapezoides no tienen ningún lado paralelo, y el cuadrado tiene dos pares."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá cómo distinguís ángulos alternos, correspondientes y conjugados entre paralelas, y por qué los ángulos exteriores de cualquier polígono convexo suman 360°.",
    },
    "a2-casos-factoreo": {
        "hook": {
            "question": "¿Cómo simplificarías `(x³ − 4x)/(x² + 2x)`? ¿Se puede tachar algo así como está?",
            "intuition": "Así no se puede tachar nada: solo se cancelan **factores**, y acá hay sumas y restas. Factorizando, queda `x(x − 2)(x + 2) / [x(x + 2)] = x − 2` (para x ≠ 0 y x ≠ −2). Los **casos de factoreo** son las herramientas para convertir una suma de términos en un producto de factores.",
        },
        "concept": {
            "points": [
                "**Factorizar** es escribir un polinomio como producto de polinomios **primos** (que no se pueden factorizar más). Los signos + y − separan términos; el producto separa factores. Para verificar, se multiplica y se tiene que obtener el polinomio original.",
                "**1° caso, factor común**: se prueba siempre primero (a veces solo se puede sacar una constante, y a veces no hay factor común); si una variable aparece con distintos exponentes, se extrae con el **menor**. **2° caso, factor común por grupos**: con 4, 6, 8, 9… términos, se forman grupos con igual cantidad de términos y, después de sacar factor común en cada uno, los paréntesis deben quedar iguales. **3° caso, trinomio cuadrado perfecto**: dos términos cuadrados (a², b²) y el otro ±2ab → `(a ± b)²`. **4° caso, cuatrinomio cubo perfecto**: dos cubos (a³, b³) y los otros `3a²b` y `3ab²` con signo → `(a + b)³`, con a y b tomados con su signo.",
                "**5° caso, diferencia de cuadrados**: `a² − b² = (a + b)(a − b)`; conviene ordenar primero (`−81 + x² = x² − 81`). **6° caso, suma o diferencia de potencias de igual exponente** `xⁿ ± aⁿ`: el primer factor es `(x ± a)`, con las raíces enésimas, y el segundo se obtiene dividiendo por Ruffini. Las diferencias se dividen por `(x − a)`; las sumas, por `(x + a)` solo si n es impar. Sumas como `x² + 4` o `x⁴ + 16` no se factorizan con estos casos (`x² + a²` es primo en IR); si el exponente par tiene un factor impar, como `x⁶ + 64 = (x²)³ + 4³`, sí se aplica el 6° caso.",
                "**7° caso, trinomio de segundo grado** con Δ ≥ 0: `ax² + bx + c = a(x − x₁)(x − x₂)`, con x₁ y x₂ de la resolvente. En los paréntesis los ceros aparecen con el signo cambiado, y **no hay que olvidar a**.",
                "**Tabla por cantidad de términos** (casos a probar, en orden): 2 → 1°, 5°, 6° | 3 → 1°, 3°, 7° | 4 → 1°, 4°, 2° | 5 → 1° | 6 → 1°, 2°. **Factorización combinada**: empezá por el factor común y volvé a mirar cada factor nuevo con la tabla hasta que ninguno se pueda factorizar. Para completar un trinomio cuadrado perfecto `x² + bx + …`, falta `(b/2)²`.",
                "**m.c.m. de polinomios**: se factoriza cada uno y se multiplican los factores comunes y no comunes con su **mayor** exponente. Por ejemplo, `m.c.m.(x² + 2x + 1; x² − 1; x³ + x²) = x².(x − 1).(x + 1)²`.",
            ],
            "real_world": [
                {
                    "title": "Límites en Análisis Matemático",
                    "detail": "Las indeterminaciones 0/0 de primer año se resuelven factorizando numerador y denominador y cancelando el factor que se anula: es aplicar estos casos.",
                },
                {
                    "title": "Sumar fracciones algebraicas",
                    "detail": "Para sumar expresiones como las de resistencias en paralelo o tiempos de trabajo combinados, el denominador común es el m.c.m. de los denominadores factorizados.",
                },
                {
                    "title": "Cálculo mental",
                    "detail": "La diferencia de cuadrados sirve para hacer cuentas a mano: `47² − 3² = (47 − 3)(47 + 3) = 44.50 = 2200`.",
                },
            ],
            "key_rule": "2 términos: 1°, 5°, 6° | 3 términos: 1°, 3°, 7° | 4 términos: 1°, 4°, 2° | 5 términos: 1° | 6 términos: 1°, 2° | Siempre primero el factor común | Seguí hasta que todos los factores sean primos.",
            "pitfall": "Dejar la factorización a medias: `x⁴ − 16 = (x² − 4)(x² + 4)` no está terminada, porque `x² − 4 = (x − 2)(x + 2)`. Y en el 7° caso, olvidarse de a: `3x² + 6x − 45 = 3(x − 3)(x + 5)`, no `(x − 3)(x + 5)`.",
        },
        "example": {
            "title": "Factorizar por completo x⁵ − x⁴ − x + 1",
            "steps": [
                "Tiene 4 términos, así que según la tabla se prueban el 1°, el 4° y el 2° caso. No hay factor común a los cuatro términos (el último es 1) y no es un cubo perfecto (x⁵ no es un cubo).",
                "**2° caso**: `(x⁵ − x⁴) + (−x + 1) = x⁴(x − 1) − 1.(x − 1) = (x − 1)(x⁴ − 1)`. Los paréntesis quedaron iguales.",
                "`x⁴ − 1` tiene 2 términos: **5° caso**, `x⁴ − 1 = (x² − 1)(x² + 1)`.",
                "Otra vez el 5° caso en `x² − 1 = (x − 1)(x + 1)`; `x² + 1` es primo en IR. Juntando: `x⁵ − x⁴ − x + 1 = (x − 1)²(x + 1)(x² + 1)`.",
                "Verificación con x = 2: `32 − 16 − 2 + 1 = 15` y `1².3.5 = 15` ✓.",
            ],
            "lab_link": "math:factoring",
            "lab_cta": "Practicar factorización",
        },
        "check": {
            "question": "¿Qué caso se aplica a `4x² − 12x + 9` y cómo queda?",
            "options": [
                {"text": "3° caso: `(2x − 3)²`", "ok": True, "feedback": "Exacto: 4x² y 9 son cuadrados (raíces 2x y 3) y 2.2x.3 = 12x; el signo − del término restante va en el binomio."},
                {"text": "5° caso: `(2x − 3)(2x + 3)`", "ok": False, "feedback": "La diferencia de cuadrados es para binomios; ese producto da 4x² − 9, sin el término −12x."},
                {"text": "7° caso: `(x − 3/2)²`", "ok": False, "feedback": "El cero doble x = 3/2 está bien, pero falta a = 4: (x − 3/2)² = x² − 3x + 9/4, que no es el polinomio dado."},
            ],
        },
        "checks": [
            {
                "question": "Con el 6° caso, ¿cómo se factoriza `x³ + 8`?",
                "options": [
                    {"text": "`(x + 2)(x² − 2x + 4)`", "ok": True, "feedback": "Exacto: 8 = 2³, el primer factor es (x + 2) y Ruffini con −2 da los coeficientes 1, −2, 4 con resto 0."},
                    {"text": "`(x + 2)(x² + 2x + 4)`", "ok": False, "feedback": "Los signos del segundo factor están mal: ese producto da x³ + 4x² + 8x + 8. En Ruffini se usa −2, la raíz de x + 2, y los signos se alternan."},
                    {"text": "`(x + 2)³`", "ok": False, "feedback": "(x + 2)³ = x³ + 6x² + 12x + 8, un cuatrinomio. Una suma de cubos no es el cubo de una suma."},
                ],
            },
            {
                "question": "¿Está terminada la factorización `x⁴ − 16 = (x² − 4)(x² + 4)`?",
                "options": [
                    {"text": "No: falta factorizar `x² − 4 = (x − 2)(x + 2)`", "ok": True, "feedback": "Exacto: x² − 4 todavía es una diferencia de cuadrados. Completa: (x − 2)(x + 2)(x² + 4)."},
                    {"text": "Sí, porque ya es un producto", "ok": False, "feedback": "Ser un producto no alcanza: cada factor tiene que ser primo, y x² − 4 se puede seguir factorizando."},
                    {"text": "No: también hay que escribir `x² + 4 = (x + 2)²`", "ok": False, "feedback": "(x + 2)² = x² + 4x + 4, no x² + 4. Una suma de cuadrados como x² + 4 no se factoriza en IR."},
                ],
            },
        ],
        "takeaway_prompt": "Describí tu recorrido para factorizar cualquier polinomio usando la tabla de cantidad de términos, y explicá cómo verificás que el resultado es correcto y que está terminado.",
    },
}
