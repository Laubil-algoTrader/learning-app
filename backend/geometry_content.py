"""Geometry curriculum (10 units, #42-#51) adapted from Khan Academy High School Geometry.

Covers all High School Geometry units building on Aritmética (#1-#17), Preálgebra (#18-#29)
and Álgebra 1 (#30-#41):
  - Angles, parallel lines & transversals, triangles & polygons
  - Rigid transformations (translations, reflections, rotations) & symmetry
  - Triangle congruence criteria & quadrilateral properties
  - Dilations, triangle similarity & Thales' theorem
  - Pythagorean theorem & special right triangles (45-45-90, 30-60-90)
  - Right-triangle trigonometry (SOH-CAH-TOA & inverse trig)
  - Analytic geometry: distance, midpoint, segment partitioning & proofs with slopes
  - Circle equations, completing the square & conic sections
  - Circle geometry: central/inscribed angles, tangents, arc length, sectors & radians
  - Solid geometry 3D: cylinders, cones, pyramids, spheres, Cavalieri, 3D scaling & density
"""

from __future__ import annotations

GEOMETRY_NODES: list[dict] = [
    # ==================== NIVEL 15: ÁNGULOS Y TRANSFORMACIONES ====================
    {
        "slug": "g-angulos-rectas",
        "title": "42. Ángulos, rectas paralelas y polígonos",
        "level": 15,
        "order_index": 42,
        "summary": "Ángulos complementarios y suplementarios, paralelas cortadas por una secante y suma de ángulos en triángulos y polígonos.",
        "prerequisites": ["p-medicion-geometria", "p-ecuaciones-un-paso"],
        "metadata": {"section": "Geometría", "lab_tab": "geometry_angles", "est_minutes": 18},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Ángulo suplementario en un corte de carpintería",
                "prompt": "Dos listones se cruzan formando una línea recta (180°). Si uno de los ángulos mide 65°, ¿cuánto mide su ángulo suplementario? Respondé solo con el número en grados.",
                "answer": "115°: dos ángulos suplementarios suman 180°, así que 180° − 65° = 115°.",
                "hints": ["Una línea recta completa mide 180°."],
                "payload": {
                    "lab_link": "math:geometry_angles",
                    "check": {"type": "numeric", "value": 115, "tolerance": 0, "unit": "°"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ángulos complementarios en una esquina recta",
                "prompt": "Cortás una esquina a escuadra (90°) en dos partes: una mide 37°. ¿Cuánto mide el ángulo complementario? Respondé solo con el número en grados.",
                "answer": "53°: los ángulos complementarios suman 90°, así que 90° − 37° = 53°.",
                "hints": ["Una escuadra recta mide 90°."],
                "payload": {
                    "lab_link": "math:geometry_angles",
                    "check": {"type": "numeric", "value": 53, "tolerance": 0, "unit": "°"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Paralelas cortadas por una avenida diagonal (secante)",
                "prompt": "Dos calles paralelas son cruzadas por una avenida diagonal. En la primera esquina, el ángulo agudo mide 52°. ¿Cuánto mide el ángulo obtuso adyacente en la segunda esquina? Respondé solo con el número en grados.",
                "answer": "128°: cuando una secante corta paralelas solo aparecen dos medidas que suman 180° (52° y 180° − 52° = 128°).",
                "hints": ["Todos los ángulos agudos valen 52° y todos los obtusos son su suplemento (180° − 52°)."],
                "payload": {"check": {"type": "numeric", "value": 128, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Tercer ángulo de un triángulo",
                "prompt": "En una cabriada triangular de techo, dos ángulos internos miden 48° y 75°. ¿Cuánto mide el tercer ángulo? Respondé solo con el número en grados.",
                "answer": "57°: los tres ángulos internos de cualquier triángulo suman 180° → 180° − (48° + 75°) = 180° − 123° = 57°.",
                "hints": ["Sumá 48 + 75 y restáselo a 180."],
                "payload": {
                    "lab_link": "math:geometry_angles",
                    "check": {"type": "numeric", "value": 57, "tolerance": 0, "unit": "°"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Suma de ángulos internos de una tuerca hexagonal",
                "prompt": "Una tuerca tiene forma de hexágono (6 lados). Usando la fórmula (n − 2) · 180°, ¿cuánto suman sus 6 ángulos internos en total? Respondé solo con el número en grados.",
                "answer": "720°: un hexágono se divide en 6 − 2 = 4 triángulos → 4 × 180° = 720° (y si es regular, cada esquina mide 120°).",
                "hints": ["Reemplazá n = 6 en (n − 2) · 180."],
                "payload": {
                    "lab_link": "math:geometry_angles",
                    "check": {"type": "numeric", "value": 720, "tolerance": 0, "unit": "°"},
                },
            },
            {
                "item_type": "recall",
                "title": "Ángulos opuestos por el vértice y alternos internos",
                "prompt": "Dos rectas paralelas son cortadas por una transversal. Si dos ángulos están entre las paralelas y en lados opuestos de la transversal (en forma de 'Z'), ¿cómo son entre sí?",
                "answer": "Iguales (se llaman alternos internos). Por el patrón de la 'Z', tienen exactamente la misma medida.",
                "hints": ["Imaginá una letra Z trazada sobre dos renglones paralelos."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Son iguales (alternos internos)",
                            "Siempre suman 90°",
                            "No tienen relación fija",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "g-transformaciones",
        "title": "43. Transformaciones rígidas y simetría en el plano",
        "level": 15,
        "order_index": 43,
        "summary": "Traslaciones, reflexiones, rotaciones en coordenadas, simetría axial/rotacional y propiedades que se conservan.",
        "prerequisites": ["p-plano-rectas", "g-angulos-rectas"],
        "metadata": {"section": "Geometría", "lab_tab": "geometry_coords", "est_minutes": 18},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Trasladar un personaje en un mapa 2D",
                "prompt": "Un personaje en un videojuego está en (2, −3) y se mueve 4 unidades a la derecha y 5 hacia arriba: (x + 4, y + 5). ¿Cuál es su nueva coordenada x? Respondé solo con el número.",
                "answer": "6: el punto pasa a (2 + 4, −3 + 5) = (6, 2), así que x = 6.",
                "hints": ["Sumá 4 a la coordenada x inicial (2)."],
                "payload": {"check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Reflexión (espejo) sobre el eje X",
                "prompt": "Si reflejás el punto P(3, −5) usando el eje X como espejo horizontal, ¿en qué coordenadas queda su imagen P'?",
                "answer": "(3, 5): al reflejar sobre el eje X, la posición horizontal x no cambia y la altura y invierte su signo.",
                "hints": ["El eje X es horizontal: lo que estaba abajo (−5) pasa arriba (+5)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(3, 5)", "(−3, −5)", "(−3, 5)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Rotación de 90° antihoraria alrededor del origen",
                "prompt": "Al rotar el punto (3, 2) un ángulo de 90° en sentido antihorario alrededor de (0, 0), se aplica (x, y) → (−y, x). ¿Dónde cae?",
                "answer": "(−2, 3): pasa del primer cuadrante al segundo, intercambiando coordenadas y cambiando el signo de la nueva x.",
                "hints": ["Sustituí x = 3 e y = 2 en (−y, x)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(−2, 3)", "(2, −3)", "(−3, −2)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Rotación de 180° (media vuelta) alrededor del origen",
                "prompt": "Rotás el vértice (5, −1) exactamente 180° alrededor del origen (0, 0). ¿Cuál es la nueva coordenada x? Respondé solo con el número.",
                "answer": "−5: una rotación de 180° invierte ambos signos: (x, y) → (−x, −y), así que (5, −1) va a (−5, 1).",
                "hints": ["Dar media vuelta alrededor del origen cambia ambos signos."],
                "payload": {"check": {"type": "numeric", "value": -5, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Qué conservan las transformaciones rígidas",
                "prompt": "Si trasladás, rotás y reflejás un plano de una pieza mecánica sin estirarla, ¿qué hacen esas transformaciones con sus medidas?",
                "answer": "Conservan todas las distancias, ángulos y el área (la figura resultante es congruente con la original).",
                "hints": ["Pensá en mover un objeto sólido de madera sobre una mesa."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Conservan longitudes, ángulos y área",
                            "Duplican las longitudes pero mantienen ángulos",
                            "Mantienen el área pero cambian los ángulos",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Contar ejes de simetría de un cuadrado",
                "prompt": "¿Cuántos ejes de simetría (líneas de doblado donde ambas mitades coinciden exactas) tiene un cuadrado? Respondé solo con el número.",
                "answer": "4 ejes: uno vertical, uno horizontal y las dos diagonales (un rectángulo no cuadrado solo tiene 2).",
                "hints": ["Contá vertical, horizontal y las dos diagonales."],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    # ==================== NIVEL 16: CONGRUENCIA, SEMEJANZA Y PITÁGORAS ====================
    {
        "slug": "g-congruencia",
        "title": "44. Congruencia de triángulos y cuadriláteros",
        "level": 16,
        "order_index": 44,
        "summary": "Criterios LLL, LAL, ALA y AAL para asegurar piezas idénticas, trampas AAA/LLA y propiedades de isósceles y paralelogramos.",
        "prerequisites": ["g-transformaciones"],
        "metadata": {"section": "Geometría", "lab_tab": "geometry_angles", "est_minutes": 18},
        "items": [
            {
                "item_type": "recall",
                "title": "Por qué AAA no garantiza congruencia",
                "prompt": "Dos triángulos tienen los mismos tres ángulos: 50°, 60° y 70°. ¿Alcanza con eso para asegurar que son congruentes (idénticos en tamaño)?",
                "answer": "No: AAA solo garantiza que tienen la misma forma (son semejantes), pero uno puede ser una versión gigante del otro.",
                "hints": ["Pensá en hacer zoom a un triángulo en la pantalla: los ángulos no cambian, ¿pero el tamaño sí?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "No, AAA solo asegura semejanza (misma forma, distinto tamaño)",
                            "Sí, mismos ángulos implican siempre mismos lados",
                            "Sí, siempre que sean agudos",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Elegir el criterio de congruencia correcto",
                "prompt": "En dos escuadras metálicas sabés que coinciden dos lados (10 cm y 14 cm) y el ángulo comprendido justo entre esos dos lados (40°). ¿Qué criterio garantiza que son congruentes?",
                "answer": "LAL (Lado-Ángulo-Lado): dos lados iguales y el ángulo encerrado entre ellos fijan de manera única el tercer lado.",
                "hints": ["El ángulo está justo en el medio de los dos lados conocidos."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["LAL (Lado-Ángulo-Lado)", "LLL (Lado-Lado-Lado)", "AAA (Ángulo-Ángulo-Ángulo)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ángulos de la base en un triángulo isósceles",
                "prompt": "Un techo a dos aguas simétrico forma un triángulo isósceles donde el ángulo superior (vértice) mide 40°. ¿Cuánto mide cada uno de los dos ángulos iguales de la base? Respondé solo con el número en grados.",
                "answer": "70°: quedan 180° − 40° = 140° para repartir en partes iguales entre los dos ángulos de la base → 140° ÷ 2 = 70°.",
                "hints": ["Restá 40° a 180° y dividí por 2."],
                "payload": {
                    "lab_link": "math:geometry_angles",
                    "check": {"type": "numeric", "value": 70, "tolerance": 0, "unit": "°"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ángulo consecutivo de un paralelogramo",
                "prompt": "En una estructura en forma de paralelogramo, una esquina mide 62°. ¿Cuánto mide la esquina consecutiva (la que comparte un lado con ella)? Respondé solo con el número en grados.",
                "answer": "118°: en todo paralelogramo los ángulos opuestos son iguales y dos consecutivos siempre suman 180° → 180° − 62° = 118°.",
                "hints": ["Los lados opuestos son paralelos, así que los ángulos consecutivos son suplementarios."],
                "payload": {"check": {"type": "numeric", "value": 118, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "recall",
                "title": "Leer correspondencia en △ABC ≅ △DEF",
                "prompt": "Si △ABC ≅ △DEF y sabés que el lado AC mide 9 cm, ¿qué lado del segundo triángulo mide obligatoriamente 9 cm?",
                "answer": "DF: el orden de las letras importa (A↔D, B↔E, C↔F), así que el segmento entre la 1.ª y la 3.ª letra corresponde a DF.",
                "hints": ["Emparejá 1.ª letra con 1.ª (A↔D) y 3.ª con 3.ª (C↔F)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["DF", "DE", "EF"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Propiedad de las diagonales en rombos y rectángulos",
                "prompt": "¿En qué cuadrilátero las diagonales se cortan SIEMPRE a 90° (perpendiculares) además de dividirse por la mitad?",
                "answer": "En el rombo (y en el cuadrado, que es un rombo con ángulos rectos). En un rectángulo común son iguales pero no perpendiculares.",
                "hints": ["Pensá en un barrilete simétrico de cuatro lados iguales."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Rombo (y cuadrado)", "Cualquier paralelogramo", "Trapecio isósceles"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "g-semejanza",
        "title": "45. Homotecias, semejanza y Teorema de Tales",
        "level": 16,
        "order_index": 45,
        "summary": "Escalas y homotecias (lados × k, áreas × k²), criterios de semejanza (AA, LAL, LLL), alturas con sombras y Teorema de Tales.",
        "prerequisites": ["g-congruencia", "p-razones-tasas"],
        "metadata": {"section": "Geometría", "lab_tab": "geometry_angles", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Medir la altura de un árbol con su sombra (AA)",
                "prompt": "A la misma hora del día, una persona de 1.8 m proyecta una sombra de 1.2 m y un árbol cercano proyecta una sombra de 8 m. ¿Cuántos metros mide el árbol? Respondé solo con el número.",
                "answer": "12 m: los rayos del sol forman triángulos semejantes (criterio AA) → h / 8 = 1.8 / 1.2 = 1.5 → h = 8 × 1.5 = 12 m.",
                "hints": ["Planteá la proporción: altura / sombra = 1.8 / 1.2 = h / 8."],
                "payload": {
                    "lab_link": "math:geometry_angles",
                    "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": "m"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Escala de un plano arquitectónico (homotecia)",
                "prompt": "En un plano en escala 1:50 (factor k = 50), una pared mide 6 cm. ¿Cuántos metros mide en la realidad? Respondé solo con el número en metros.",
                "answer": "3 m: 6 cm × 50 = 300 cm = 3 metros.",
                "hints": ["Multiplicá 6 cm por 50 y pasá de centímetros a metros (÷ 100)."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0.01, "unit": "m"}},
            },
            {
                "item_type": "worked_example",
                "title": "Cómo escala el área (el mito de las dos pizzas)",
                "prompt": "Una pizza grande tiene el doble de diámetro que una pizza chica (factor de escala k = 2). ¿Cuántas veces más área (superficie de pizza) tiene la grande respecto de la chica? Respondé solo con el número.",
                "answer": "4 veces más: cuando todas las longitudes se multiplican por k, el área se multiplica por k² = 2² = 4.",
                "hints": ["El área es bidimensional (largo × ancho), así que escala con k², no con k."],
                "payload": {
                    "lab_link": "math:geometry_angles",
                    "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "×"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Teorema de Tales (segmento paralelo en un triángulo)",
                "prompt": "Una línea paralela a la base corta los dos lados de un triángulo. En el lado izquierdo deja tramos de 4 cm (arriba) y 6 cm (abajo). En el derecho el tramo de abajo mide 9 cm. ¿Cuánto mide el tramo superior x? Respondé solo con el número en cm.",
                "answer": "6 cm: por el Teorema de Tales, 4 / 6 = x / 9 → x = (4 × 9) / 6 = 6 cm.",
                "hints": ["Igualá las razones: 4 / 6 = x / 9."],
                "payload": {
                    "lab_link": "math:geometry_angles",
                    "check": {"type": "numeric", "value": 6, "tolerance": 0.01, "unit": "cm"},
                },
            },
            {
                "item_type": "recall",
                "title": "Criterio mínimo para probar semejanza de triángulos",
                "prompt": "¿Cuál es la información mínima que alcanza para asegurar que dos triángulos son semejantes?",
                "answer": "AA (dos pares de ángulos iguales): como los tres suman 180°, el tercer ángulo coincide automáticamente.",
                "hints": ["Si dos ángulos ya coinciden, ¿puede ser distinto el tercero?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Dos ángulos iguales (criterio AA)",
                            "Un solo ángulo igual y un lado igual",
                            "Igual perímetro",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ampliar una foto con factor de escala k = 3",
                "prompt": "Un cartel rectangular tiene área de 20 cm². Si lo ampliás manteniendo la proporción con un factor k = 3 (triple de ancho y triple de alto), ¿cuántos cm² medirá el cartel nuevo? Respondé solo con el número.",
                "answer": "180 cm²: el área escala por k² = 3² = 9 → 20 × 9 = 180 cm².",
                "hints": ["Multiplicá el área original por 3² = 9."],
                "payload": {"check": {"type": "numeric", "value": 180, "tolerance": 0, "unit": "cm²"}},
            },
        ],
    },
    {
        "slug": "g-pitagoras-especiales",
        "title": "46. Teorema de Pitágoras y triángulos especiales",
        "level": 16,
        "order_index": 46,
        "summary": "Calcular hipotenusas y catetos con a² + b² = c², verificar escuadras (3-4-5) y atajos 45°−45°−90° y 30°−60°−90°.",
        "prerequisites": ["g-semejanza", "al-exponentes-radicales"],
        "metadata": {"section": "Geometría", "lab_tab": "pythagoras_trig", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Diagonal de una pantalla (hallar hipotenusa)",
                "prompt": "Un monitor mide 80 cm de ancho y 60 cm de alto. ¿Cuántos cm mide su diagonal? Respondé solo con el número.",
                "answer": "100 cm: √(80² + 60²) = √(6400 + 3600) = √10000 = 100 cm (es un triángulo 3-4-5 multiplicado por 20).",
                "hints": ["Usá c = √(80² + 60²), o reconocé la terna 6-8-10."],
                "payload": {
                    "lab_link": "math:pythagoras_trig",
                    "check": {"type": "numeric", "value": 100, "tolerance": 0, "unit": "cm"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Escalera apoyada en la pared (hallar un cateto)",
                "prompt": "Una escalera de 13 m (hipotenusa) se apoya en una pared con la base a 5 m de distancia. ¿A qué altura llega sobre la pared? Respondé solo con el número en metros.",
                "answer": "12 m: como buscamos un cateto, RESTAMOS cuadrados → h = √(13² − 5²) = √(169 − 25) = √144 = 12 m (terna 5-12-13).",
                "hints": ["Ojo: 13 es la hipotenusa (el lado más largo), así que h² = 13² − 5²."],
                "payload": {
                    "lab_link": "math:pythagoras_trig",
                    "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": "m"},
                },
            },
            {
                "item_type": "recall",
                "title": "Recíproco de Pitágoras: chequear si una pared está a escuadra",
                "prompt": "Un albañil marca 3 m sobre una pared, 4 m sobre la otra y mide la diagonal entre ambas marcas: le da 5.3 m. ¿La esquina está a 90° exactos?",
                "answer": "No: para ser 90° la diagonal debería medir √(3² + 4²) = 5 m. Como 5.3 m > 5 m, la esquina está más abierta (ángulo obtuso).",
                "hints": ["Comprobá si 3² + 4² es igual a 5.3²."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "No, está más abierta que 90° (debería dar 5 m exactos)",
                            "Sí, siempre que los lados sean 3 y 4 es ángulo recto",
                            "No, está más cerrada que 90°",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Triángulo especial 30°−60°−90° (proporción 1 : √3 : 2)",
                "prompt": "Una rampa de 12 m de largo (hipotenusa) forma un ángulo de 30° con el suelo. ¿Qué altura alcanza la rampa? Respondé solo con el número en metros.",
                "answer": "6 m: en un 30°−60°−90° los lados siguen la relación x : x√3 : 2x, así que frente a 30° mide 12 / 2 = 6 m.",
                "hints": ["Es un triángulo 30°−60°−90°: sus lados siguen la proporción 1 : √3 : 2.", "El cateto más corto (frente a 30°) vale exactamente la mitad de la hipotenusa."],
                "payload": {
                    "lab_link": "math:pythagoras_trig",
                    "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": "m"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Diagonal de una baldosa cuadrada (45°−45°−90°)",
                "prompt": "Una baldosa cuadrada mide 10 cm de lado. Su diagonal forma un triángulo 45°−45°−90° (hipotenusa = lado · √2, con √2 ≈ 1.414). ¿Cuántos cm mide la diagonal? Redondeá a 1 decimal.",
                "answer": "14.1 cm (exactamente 10√2 ≈ 14.14 cm).",
                "hints": ["Multiplicá 10 × 1.414."],
                "payload": {
                    "lab_link": "math:pythagoras_trig",
                    "check": {"type": "numeric", "value": 14.14, "tolerance": 0.005, "unit": "cm"},
                },
            },
            {
                "item_type": "recall",
                "title": "Reconocer la hipotenusa sin equivocarse",
                "prompt": "En cualquier triángulo rectángulo, ¿cómo identificás SIEMPRE cuál lado va solo a la derecha en a² + b² = c²?",
                "answer": "Es la hipotenusa: el lado opuesto al ángulo de 90° y siempre el más largo de los tres.",
                "hints": ["Mirá frente a qué ángulo está y compará su longitud."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "El lado opuesto al ángulo de 90° (siempre el más largo)",
                            "Siempre el lado horizontal de abajo",
                            "El lado que queremos calcular (la incógnita x)",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 17: TRIGONOMETRÍA Y GEOMETRÍA ANALÍTICA ====================
    {
        "slug": "g-trigonometria",
        "title": "47. Trigonometría del triángulo rectángulo (SOH-CAH-TOA)",
        "level": 17,
        "order_index": 47,
        "summary": "Seno, coseno y tangente como razones entre lados, despejar alturas y distancias, y hallar ángulos con inversas.",
        "prerequisites": ["g-pitagoras-especiales"],
        "metadata": {"section": "Geometría", "lab_tab": "pythagoras_trig", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Calcular sen(θ) en un triángulo 3-4-5",
                "prompt": "En un triángulo rectángulo de lados 3, 4 y 5, el cateto opuesto al ángulo θ mide 3 y la hipotenusa mide 5. ¿Cuánto vale sen(θ) en decimal? Respondé solo con el número.",
                "answer": "0.6: por SOH, sen(θ) = Opuesto / Hipotenusa = 3 / 5 = 0.6.",
                "hints": ["SOH: Seno = Opuesto ÷ Hipotenusa."],
                "payload": {
                    "lab_link": "math:pythagoras_trig",
                    "check": {"type": "numeric", "value": 0.6, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Calcular tan(θ) como pendiente de una rampa",
                "prompt": "Una rampa sube 3 m en vertical por cada 4 m en horizontal. ¿Cuánto vale tan(θ) = Opuesto / Adyacente en decimal? Respondé solo con el número.",
                "answer": "0.75: tan(θ) = 3 / 4 = 0.75 (coincide exactamente con la pendiente m = Δy/Δx de la rampa).",
                "hints": ["TOA: Tangente = Opuesto ÷ Adyacente."],
                "payload": {
                    "lab_link": "math:pythagoras_trig",
                    "check": {"type": "numeric", "value": 0.75, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Altura de un barrilete usando sen(30°) = 0.5",
                "prompt": "Soltaste 40 m de hilo tirante de un barrilete (hipotenusa) con un ángulo de elevación de 30° sobre tu mano. Sabiendo que sen(30°) = 0.5, ¿cuántos metros por encima de tu mano vuela? Respondé solo con el número.",
                "answer": "20 m: sen(30°) = h / 40 → h = 40 × 0.5 = 20 m.",
                "hints": ["Despejá el opuesto: h = hipotenusa × sen(30°)."],
                "payload": {
                    "lab_link": "math:pythagoras_trig",
                    "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "m"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Medir la altura de una torre con ángulo de elevación 45°",
                "prompt": "Te parás a 25 m de la base de una torre y mirás la punta con un ángulo de elevación de 45° (tan(45°) = 1). Despreciando la altura de tus ojos, ¿cuántos metros mide la torre? Respondé solo con el número.",
                "answer": "25 m: tan(45°) = h / 25 = 1 → h = 25 m (cuando el ángulo es 45°, altura y distancia horizontal son iguales).",
                "hints": ["tan(45°) = Opuesto / Adyacente = 1."],
                "payload": {"check": {"type": "numeric", "value": 25, "tolerance": 0, "unit": "m"}},
            },
            {
                "item_type": "recall",
                "title": "Elegir la razón correcta según qué lados tenés",
                "prompt": "Conocés el ángulo θ y la hipotenusa de un techo, y querés calcular la proyección horizontal (cateto adyacente). ¿Qué función trigonométrica usás?",
                "answer": "Coseno (CAH): cos(θ) = Adyacente / Hipotenusa → Adyacente = Hipotenusa · cos(θ).",
                "hints": ["Tenés Hipotenusa y buscás Adyacente → recordá CAH."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "cos(θ) (CAH: Adyacente / Hipotenusa)",
                            "sen(θ) (SOH: Opuesto / Hipotenusa)",
                            "tan(θ) (TOA: Opuesto / Adyacente)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Cofunciones: relación entre seno y coseno de ángulos complementarios",
                "prompt": "En un triángulo rectángulo, los dos ángulos agudos suman 90° y el opuesto de uno es el adyacente del otro. Si sen(35°) = cos(x°), ¿cuánto vale x? Respondé solo con el número en grados.",
                "answer": "55°: siempre se cumple sen(θ) = cos(90° − θ), así que sen(35°) = cos(55°).",
                "hints": ["Restá 35° a 90°."],
                "payload": {"check": {"type": "numeric", "value": 55, "tolerance": 0, "unit": "°"}},
            },
        ],
    },
    {
        "slug": "g-analitica-plano",
        "title": "48. Geometría analítica: distancia, punto medio y partición",
        "level": 17,
        "order_index": 48,
        "summary": "Fórmula de distancia (Pitágoras en coordenadas), punto medio, dividir segmentos en una razón y clasificar figuras con pendientes.",
        "prerequisites": ["g-pitagoras-especiales", "al-formas-lineales"],
        "metadata": {"section": "Geometría", "lab_tab": "geometry_coords", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Distancia en línea recta entre dos puntos de un mapa",
                "prompt": "En un mapa cuadriculado (1 unidad = 1 km), tu casa está en (1, 2) y el parque en (4, 6). ¿Cuál es la distancia en línea recta? Respondé solo con el número en km.",
                "answer": "5 km: Δx = 4 − 1 = 3 y Δy = 6 − 2 = 4 → d = √(3² + 4²) = √25 = 5 km.",
                "hints": ["Armá el triángulo rectángulo con Δx = 3 y Δy = 4."],
                "payload": {
                    "lab_link": "math:geometry_coords",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0.01, "unit": "km"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Distancia con coordenadas negativas",
                "prompt": "Calculá la distancia entre los puntos A(−2, 1) y B(4, 9). Respondé solo con el número.",
                "answer": "10: Δx = 4 − (−2) = 6, Δy = 9 − 1 = 8 → d = √(6² + 8²) = √100 = 10.",
                "hints": ["Ojo al restar negativos: 4 − (−2) = 6."],
                "payload": {
                    "lab_link": "math:geometry_coords",
                    "check": {"type": "numeric", "value": 10, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Punto medio para encontrarse a mitad de camino",
                "prompt": "Dos amigos están en (2, 5) y (8, 11) y quieren encontrarse exactamente en el punto medio. ¿Cuál es la coordenada x del punto medio? Respondé solo con el número.",
                "answer": "5: el punto medio es el promedio de cada coordenada → ((2 + 8)/2, (5 + 11)/2) = (5, 8).",
                "hints": ["Promediá las dos coordenadas x: (2 + 8) ÷ 2."],
                "payload": {
                    "lab_link": "math:geometry_coords",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Punto medio con coordenadas negativas",
                "prompt": "Hallá la coordenada y del punto medio entre (−4, 6) y (2, −2). Respondé solo con el número.",
                "answer": "2: promedio de y = (6 + (−2)) / 2 = 4 / 2 = 2 (el punto medio completo es (−1, 2)).",
                "hints": ["Sumá 6 + (−2) y dividí por 2."],
                "payload": {
                    "lab_link": "math:geometry_coords",
                    "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Dividir un segmento en razón 1:3 (partición)",
                "prompt": "Un cable recto va de A(0, 0) a B(8, 12). Ponés un empalme a 1/4 del recorrido desde A (razón 1:3). ¿Cuál es la coordenada y del empalme? Respondé solo con el número.",
                "answer": "3: avanzás 1/4 del desplazamiento total (Δx = 8, Δy = 12) → (0 + 2, 0 + 3) = (2, 3).",
                "hints": ["Calculá un cuarto de 12."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Comprobar si una esquina en el plano es de 90°",
                "prompt": "En el plano cartesiano, el lado AB tiene pendiente m₁ = 2/3 y el lado BC tiene pendiente m₂ = −3/2. ¿Qué ángulo forman en B?",
                "answer": "90° (son perpendiculares): porque el producto de sus pendientes es (2/3) · (−3/2) = −1.",
                "hints": ["Multiplicá las dos pendientes: si da −1, forman ángulo recto."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "90° (perpendiculares, pues m₁ · m₂ = −1)",
                            "0° (son paralelos)",
                            "45° (opuestos)",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 18: CÍRCULOS, CÓNICAS Y GEOMETRÍA SÓLIDA 3D ====================
    {
        "slug": "g-ecuacion-circulo",
        "title": "49. Ecuación de la circunferencia y secciones cónicas",
        "level": 18,
        "order_index": 49,
        "summary": "Forma estándar (x − h)² + (y − k)² = r², leer centro y radio, completar cuadrados e introducción a elipses, parábolas e hipérbolas.",
        "prerequisites": ["g-analitica-plano", "al-polinomios-binomios"],
        "metadata": {"section": "Geometría", "lab_tab": "geometry_coords", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Leer el radio en la ecuación estándar",
                "prompt": "La zona de cobertura de una antena Wi-Fi sigue la ecuación (x − 3)² + (y + 2)² = 25 (en metros). ¿Cuál es el radio de cobertura en metros? Respondé solo con el número.",
                "answer": "5 m: el número de la derecha es r² (el radio al cuadrado), así que r = √25 = 5 m.",
                "hints": ["Ojo: 25 es r², tenés que sacar la raíz cuadrada."],
                "payload": {
                    "lab_link": "math:geometry_coords",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "m"},
                },
            },
            {
                "item_type": "recall",
                "title": "Leer el centro sin caer en la trampa de signos",
                "prompt": "¿Cuál es el centro (h, k) de la circunferencia (x − 3)² + (y + 2)² = 25?",
                "answer": "(3, −2): la fórmula es (x − h)² + (y − k)², así que los signos del centro siempre se ven 'invertidos' (x − 3 → h = 3; y + 2 = y − (−2) → k = −2).",
                "hints": ["Buscá qué valores de x e y hacen cero a cada paréntesis."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(3, −2)", "(−3, 2)", "(3, 2)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Escribir la ecuación de una zona de radar",
                "prompt": "Un radar está ubicado en (−1, 4) y cubre un radio de 6 km. ¿Qué ecuación describe el borde de su cobertura?",
                "answer": "(x + 1)² + (y − 4)² = 36: reemplazamos h = −1 (da x + 1), k = 4 (da y − 4) y r² = 6² = 36.",
                "hints": ["Usá (x − h)² + (y − k)² = r² con r² = 36."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "(x + 1)² + (y − 4)² = 36",
                            "(x − 1)² + (y + 4)² = 36",
                            "(x + 1)² + (y − 4)² = 6",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Comprobar si un punto está dentro, sobre o fuera del círculo",
                "prompt": "La zona de envío gratis es el círculo x² + y² ≤ 25 (centro en el origen, radio 5 km). Un cliente vive en (4, 4). ¿Le llega el envío gratis?",
                "answer": "No, está afuera: 4² + 4² = 16 + 16 = 32, que es mayor que 25 (está a √32 ≈ 5.66 km del local).",
                "hints": ["Evaluá 4² + 4² y comparalo con 25."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "No, está afuera (4² + 4² = 32 > 25)",
                            "Sí, está justo en el borde",
                            "Sí, está adentro (4 + 4 = 8 < 25)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Hallar el radio completando cuadrados",
                "prompt": "Pasá x² + 4x + y² − 10y = 7 a la forma estándar (x − h)² + (y − k)² = r² completando cuadrados. ¿Cuánto vale el radio r? Respondé solo con el número.",
                "answer": "6: sumás 4 (para x) y 25 (para y) en ambos lados → (x + 2)² + (y − 5)² = 7 + 4 + 25 = 36 = r², por lo tanto r = √36 = 6.",
                "hints": ["Para completar cada cuadrado sumá (mitad del coeficiente lineal)²: (4/2)² = 4 y (10/2)² = 25.", "A la derecha queda 7 + 4 + 25 = 36 = r²."],
                "payload": {
                    "lab_link": "math:geometry_coords",
                    "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Reconocer las 4 secciones cónicas en la vida real",
                "prompt": "Las órbitas de los planetas alrededor del Sol y las antenas parabólicas de TV son ejemplos de secciones cónicas (cortes de un plano sobre un cono). ¿Qué cónica describe una órbita planetaria cerrada y achatada?",
                "answer": "La elipse (corte oblicuo completo del cono; cuando el corte es horizontal se obtiene un círculo, y paralelo a la pared da una parábola).",
                "hints": ["Es como un círculo estirado con dos focos."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Elipse", "Hipérbola", "Parábola"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "g-circulos-arcos",
        "title": "50. Círculos: ángulos, tangentes, arcos, sectores y radianes",
        "level": 18,
        "order_index": 50,
        "summary": "Ángulos centrales e inscritos, rectas tangentes a 90° del radio, longitud de arco, área de sector y conversión a radianes.",
        "prerequisites": ["g-angulos-rectas", "g-pitagoras-especiales"],
        "metadata": {"section": "Geometría", "lab_tab": "geometry_3d", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Ángulo inscrito vs. ángulo central",
                "prompt": "En un círculo, un arco mide 110° (su ángulo central es 110°). ¿Cuánto mide un ángulo inscrito (con vértice sobre el borde) que abarca ese mismo arco? Respondé solo con el número en grados.",
                "answer": "55°: todo ángulo inscrito mide exactamente la MITAD del ángulo central (o arco) que abarca.",
                "hints": ["Dividí el ángulo central por 2."],
                "payload": {
                    "lab_link": "math:geometry_3d",
                    "check": {"type": "numeric", "value": 55, "tolerance": 0, "unit": "°"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Teorema del ángulo inscrito en un semicírculo",
                "prompt": "Si trazás un triángulo usando el diámetro completo de un círculo como base y cualquier punto del borde como tercer vértice, ¿cuántos grados mide siempre ese ángulo del borde? Respondé solo con el número.",
                "answer": "90°: el diámetro abarca un semicírculo de 180°, y el ángulo inscrito mide la mitad → 180° ÷ 2 = 90°.",
                "hints": ["El arco es medio círculo (180°); dividilo por 2."],
                "payload": {"check": {"type": "numeric", "value": 90, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Longitud de una tangente a una polea circular",
                "prompt": "Una correa sale tangente a una polea de radio 5 cm desde un punto ubicado a 13 cm del centro de la polea. Como la tangente forma 90° con el radio, ¿cuántos cm mide el tramo recto tangente? Respondé solo con el número.",
                "answer": "12 cm: radio (5) y tangente (t) son los catetos, y 13 es la hipotenusa → t = √(13² − 5²) = 12 cm.",
                "hints": ["Usá Pitágoras con hipotenusa = 13 y cateto = 5."],
                "payload": {
                    "lab_link": "math:pythagoras_trig",
                    "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": "cm"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Longitud de arco (un cuarto de rotonda)",
                "prompt": "Una curva circular tiene radio r = 10 m y gira 90° (un cuarto de vuelta). Usando π ≈ 3.14, ¿cuántos metros mide ese arco? Redondeá a 1 decimal.",
                "answer": "15.7 m: perímetro completo = 2π(10) ≈ 62.83 m; un cuarto (90°/360°) mide 5π ≈ 15.7 m.",
                "hints": ["Calculá (90 / 360) × 2 × 3.14 × 10."],
                "payload": {
                    "lab_link": "math:geometry_3d",
                    "check": {"type": "numeric", "value": 15.7, "tolerance": 0.005, "unit": "m"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Área de una porción de pizza (sector circular)",
                "prompt": "Una pizza de radio 12 cm se corta en 6 porciones iguales (cada una de 60°). Usando π ≈ 3.14, ¿cuántos cm² tiene UNA porción? Redondeá al entero más cercano.",
                "answer": "75 cm² (75.4 cm²): área total = π · 12² = 144π; una sexta parte = 24π ≈ 75.4 cm².",
                "hints": ["Calculá (1/6) × 3.14 × 12² = 24 × 3.14."],
                "payload": {
                    "lab_link": "math:geometry_3d",
                    "check": {"type": "numeric", "value": 75.4, "tolerance": 0.006, "unit": "cm²"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Convertir radianes a grados",
                "prompt": "Sabiendo que π radianes equivale exactamente a 180°, ¿a cuántos grados equivale un ángulo de 2π/3 radianes? Respondé solo con el número en grados.",
                "answer": "120°: reemplazás π por 180° → (2 × 180°) / 3 = 120°.",
                "hints": ["Sustituí π por 180° y hacé (2 × 180) ÷ 3."],
                "payload": {"check": {"type": "numeric", "value": 120, "tolerance": 0, "unit": "°"}},
            },
        ],
    },
    {
        "slug": "g-geometria-solida",
        "title": "51. Geometría sólida 3D: cilindros, conos, esferas y densidad",
        "level": 18,
        "order_index": 51,
        "summary": "Volumen y superficie de cilindros, pirámides, conos y esferas, Principio de Cavalieri, escalado 3D (k³) y densidad.",
        "prerequisites": ["g-circulos-arcos", "p-medicion-geometria"],
        "metadata": {"section": "Geometría", "lab_tab": "geometry_3d", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Volumen de un tanque cilíndrico de agua",
                "prompt": "Un tanque cilíndrico tiene radio r = 3 m y altura h = 5 m. Usando V = πr²h y π ≈ 3.14, ¿cuántos m³ de agua carga? Redondeá a 1 decimal.",
                "answer": "141.3 m³: V = 3.14 × 3² × 5 = 45 × 3.14 = 141.3 m³ (equivalen a 141 300 litros).",
                "hints": ["Primero elevá el radio al cuadrado (3² = 9), multiplicá por 5 y por 3.14."],
                "payload": {
                    "lab_link": "math:geometry_3d",
                    "check": {"type": "numeric", "value": 141.3, "tolerance": 0.001, "unit": "m³"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Relación 1/3 entre cono y cilindro",
                "prompt": "Un vaso cilíndrico carga 900 mL. Una copa cónica tiene exactamente el mismo radio y la misma altura. ¿Cuántos mL carga la copa cónica? Respondé solo con el número.",
                "answer": "300 mL: cualquier cono o pirámide tiene exactamente 1/3 del volumen del cilindro o prisma de igual base y altura.",
                "hints": ["Dividí el volumen del cilindro por 3."],
                "payload": {
                    "lab_link": "math:geometry_3d",
                    "check": {"type": "numeric", "value": 300, "tolerance": 0, "unit": "mL"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Volumen de una pirámide de base cuadrada",
                "prompt": "Una carpa piramidal tiene base cuadrada de 6 m × 6 m y altura de 10 m. Usando V = (1/3) · A_base · h, ¿cuántos m³ de aire encierra? Respondé solo con el número.",
                "answer": "120 m³: A_base = 6 × 6 = 36 m² → V = (1/3) × 36 × 10 = 12 × 10 = 120 m³.",
                "hints": ["Calculá el área del cuadrado (36), multiplicá por 10 y dividí por 3."],
                "payload": {
                    "lab_link": "math:geometry_3d",
                    "check": {"type": "numeric", "value": 120, "tolerance": 0, "unit": "m³"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Volumen de una esfera (V = 4/3 · πr³)",
                "prompt": "Una bola de acero maciza tiene radio r = 6 cm. Usando V = (4/3) · πr³ y π ≈ 3.14, ¿cuántos cm³ mide su volumen? Redondeá al entero más cercano.",
                "answer": "904 cm³: (4/3) × 3.14 × 216 = 288 × 3.14 = 904.32 ≈ 904 cm³ (con π exacto da 904.8, o sea 905).",
                "hints": ["6³ = 216; (4/3) × 216 = 288; luego 288 × 3.14."],
                "payload": {
                    "lab_link": "math:geometry_3d",
                    "check": {"type": "numeric", "value": 904.5, "tolerance": 0.001, "unit": "cm³"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Cómo escala el volumen en 3D (k³)",
                "prompt": "Imprimís en 3D una caja al doble de tamaño en largo, ancho y alto (factor k = 2). ¿Cuántas veces más volumen interno tiene la caja grande? Respondé solo con el número.",
                "answer": "8 veces más: el volumen tiene 3 dimensiones, así que escala con k³ = 2³ = 8.",
                "hints": ["Multiplicás largo ×2, ancho ×2 y alto ×2."],
                "payload": {
                    "lab_link": "math:geometry_3d",
                    "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": "×"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Modelado con densidad (masa = densidad × volumen)",
                "prompt": "Un bloque de hormigón ocupa 0.5 m³ y su densidad es 2400 kg/m³. ¿Cuántos kg pesa el bloque? Respondé solo con el número.",
                "answer": "1200 kg: masa = densidad × volumen = 2400 × 0.5 = 1200 kg.",
                "hints": ["Multiplicá 2400 por 0.5 (la mitad)."],
                "payload": {"check": {"type": "numeric", "value": 1200, "tolerance": 0, "unit": "kg"}},
            },
        ],
    },
]

GEOMETRY_LESSONS: dict[str, dict] = {
    "g-angulos-rectas": {
        "hook": "Con solo medir un ángulo en una estructura o cruce de calles podés deducir todos los demás sin moverte del lugar.",
        "concept": {
            "points": [
                "Dos ángulos son **complementarios** si suman `90°` (una esquina a escuadra) y **suplementarios** si suman `180°` (una línea recta).",
                "Cuando una recta transversal corta dos **paralelas**, los 8 ángulos que aparecen toman solo **dos medidas** que suman `180°` (todos los agudos son iguales entre sí y todos los obtusos también).",
                "En cualquier **triángulo**, los tres ángulos internos suman `180°`. Cualquier polígono de `n` lados se parte en `(n − 2)` triángulos, así que sus ángulos suman `(n − 2) · 180°`.",
            ],
            "real_world": [
                {
                    "title": "Cortes a inglete en carpintería",
                    "detail": "Para unir dos molduras formando una esquina de `90°`, cada madera se corta a `45°` (ángulos complementarios exactos).",
                },
                {
                    "title": "Avenidas diagonales en la ciudad",
                    "detail": "Una diagonal que cruza calles paralelas repite exactamente el mismo ángulo agudo y obtuso en cada cuadra que atraviesa.",
                },
                {
                    "title": "Tuercas hexagonales y panales",
                    "detail": "En un hexágono regular (`6` lados), cada esquina mide `720° ÷ 6 = 120°`, por eso 3 hexágonos encajan exacto (`3 × 120° = 360°`) sin huecos.",
                },
            ],
            "key_rule": "Complementarios = 90°; suplementarios = 180°; triángulo = 180°; polígono de n lados = (n − 2) · 180°.",
            "pitfall": "Asumir que dos rectas son paralelas solo porque 'se ven parecidas' en el dibujo: si no lo dice el enunciado o las marcas, las reglas de paralelas no aplican.",
        },
        "example": {
            "title": "Hallar el ángulo faltante y la suma de un pentágono",
            "steps": [
                "En un triángulo con ángulos `48°` y `75°`, sumamos los conocidos: `48° + 75° = 123°`.",
                "Restamos a `180°`: el tercer ángulo mide `180° − 123° = 57°`.",
                "Para un pentágono (`n = 5` lados), lo partimos en `5 − 2 = 3` triángulos → suma interna = `3 × 180° = 540°`.",
            ],
            "lab_link": "math:geometry_angles",
            "lab_cta": "Practicar ángulos y polígonos en el Laboratorio",
        },
        "check": {
            "question": "Dos ángulos forman una línea recta (`180°`). Si uno mide `132°`, ¿cuánto mide el otro?",
            "options": [
                {"text": "`48°`", "ok": True, "feedback": "Exacto: 180° − 132° = 48° (son suplementarios)."},
                {"text": "`58°`", "ok": False, "feedback": "132 + 58 da 190°, te pasaste 10° de la recta."},
                {"text": "`132°`", "ok": False, "feedback": "Solo son iguales si son opuestos por el vértice o ambos miden 90°."},
            ],
        },
        "checks": [
            {
                "question": "Un triángulo tiene ángulos `90°` y `34°`. ¿Cuánto mide el tercer ángulo?",
                "options": [
                    {"text": "`56°`", "ok": True, "feedback": "Exacto: en un triángulo rectángulo los dos ángulos agudos siempre suman 90° → 90° − 34° = 56°."},
                    {"text": "`66°`", "ok": False, "feedback": "34 + 66 = 100°, sumado a 90° daría 190°."},
                    {"text": "`146°`", "ok": False, "feedback": "Restaste 34 a 180 pero te faltó restar también el ángulo de 90°."},
                ],
            },
            {
                "question": "¿Cuánto suman los ángulos internos de cualquier cuadrilátero (`4` lados)?",
                "options": [
                    {"text": "`360°` (`(4 − 2) × 180°`)", "ok": True, "feedback": "Exacto: una diagonal divide cualquier cuadrilátero en 2 triángulos de 180°."},
                    {"text": "`180°`", "ok": False, "feedback": "180° es la suma de un triángulo (3 lados)."},
                    {"text": "`540°`", "ok": False, "feedback": "540° corresponde a un pentágono (5 lados)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras por qué al cruzar dos paralelas con una secante solo aparecen dos medidas de ángulos.",
    },
    "g-transformaciones": {
        "hook": "Mover, girar o espejar un objeto en un videojuego o programa de diseño CAD usa exactamente tres reglas de coordenadas.",
        "concept": {
            "points": [
                "Las **transformaciones rígidas** (traslación, reflexión y rotación) mueven una figura sin deformarla: conservan **todas las longitudes, ángulos y el área**.",
                "En coordenadas: **trasladar** suma constantes `(x + a, y + b)`; **reflejar** en el eje X cambia `y` → `(x, −y)` y en el eje Y cambia `x` → `(−x, y)`.",
                "Al **rotar** alrededor del origen `(0, 0)`: `90°` antihorario lleva `(x, y) → (−y, x)`, y `180°` invierte ambos signos `(x, y) → (−x, −y)`.",
            ],
            "real_world": [
                {
                    "title": "Motores gráficos y videojuegos 2D",
                    "detail": "Cada vez que un personaje camina, gira o mira hacia el otro lado, el motor aplica una traslación, rotación o reflexión sobre sus vértices.",
                },
                {
                    "title": "Diseño vectorial y logos (simetría)",
                    "detail": "Los diseñadores dibujan solo la mitad de un ícono y lo reflejan sobre un eje de simetría para garantizar equilibrio perfecto.",
                },
                {
                    "title": "Brazo robótico industrial",
                    "detail": "Para trasladar una pieza de una cinta a otra sin aplastarla ni estirarla, el software calcula una secuencia de movimientos rígidos.",
                },
            ],
            "key_rule": "Traslación: (x+a, y+b) | Espejo eje X: (x, −y) | Espejo eje Y: (−x, y) | Rotación 180°: (−x, −y).",
            "pitfall": "Confundir reflexión sobre el eje X con cambiar el signo de x: el eje X es horizontal, así que lo que cruza al otro lado es la altura y.",
        },
        "example": {
            "title": "Aplicar traslación y reflexión a un punto P(4, −2)",
            "steps": [
                "Trasladamos `P(4, −2)` 3 unidades a la izquierda y 5 hacia arriba: `(4 − 3, −2 + 5) = (1, 3)`.",
                "Ahora reflejamos `(1, 3)` sobre el eje Y (espejo vertical): cambia solo el signo de `x` → `(−1, 3)`.",
                "Si en cambio rotamos `(1, 3)` `180°` alrededor del origen: cambian ambos signos → `(−1, −3)`.",
            ],
            "lab_link": "math:geometry_coords",
            "lab_cta": "Practicar coordenadas en el Laboratorio",
        },
        "check": {
            "question": "Si reflejás el punto `(−5, 2)` sobre el eje Y, ¿dónde queda?",
            "options": [
                {"text": "`(5, 2)`", "ok": True, "feedback": "Exacto: el eje Y es vertical, así que se invierte solo el signo de x."},
                {"text": "`(−5, −2)`", "ok": False, "feedback": "Eso sería reflejar sobre el eje X (cambiando y)."},
                {"text": "`(5, −2)`", "ok": False, "feedback": "Cambiar ambos signos es una rotación de 180°, no una reflexión sobre el eje Y."},
            ],
        },
        "checks": [
            {
                "question": "Una figura se mueve con la regla `(x, y) → (x + 6, y − 2)`. ¿Qué transformación es?",
                "options": [
                    {"text": "Traslación: 6 a la derecha y 2 hacia abajo", "ok": True, "feedback": "Exacto: sumar/restar constantes desplaza toda la figura sin girarla."},
                    {"text": "Rotación de 90°", "ok": False, "feedback": "La rotación intercambia x e y, no suma constantes."},
                    {"text": "Homotecia (cambio de tamaño)", "ok": False, "feedback": "La homotecia multiplica las coordenadas por un factor k."},
                ],
            },
            {
                "question": "¿Cuál de las siguientes transformaciones NO es rígida (cambia el tamaño de la figura)?",
                "options": [
                    {"text": "Homotecia / dilatación (`(2x, 2y)`)", "ok": True, "feedback": "Exacto: multiplicar por 2 duplica los lados; traslación, rotación y reflexión mantienen el tamaño."},
                    {"text": "Reflexión sobre el eje X", "ok": False, "feedback": "Espejar cambia la orientación, pero conserva exactamente longitudes y ángulos."},
                    {"text": "Rotación de 90°", "ok": False, "feedback": "Rotar mantiene intactas todas las distancias."},
                ],
            },
        ],
        "takeaway_prompt": "Resumí qué cambia y qué permanece igual al reflejar un punto sobre el eje X frente al eje Y.",
    },
    "g-congruencia": {
        "hook": "¿Cuántas medidas mínimas necesitás tomarle a un triángulo para fabricar un repuesto idéntico sin medir los 6 datos (3 lados y 3 ángulos)?",
        "concept": {
            "points": [
                "Dos figuras son **congruentes (`≅`)** si una puede superponerse exactamente sobre la otra mediante transformaciones rígidas (misma forma y tamaño).",
                "Para triángulos bastan solo **3 datos elegidos bien**: **`LLL`**, **`LAL`** (ángulo entre los dos lados), **`ALA`**, **`AAL`** o **`HC`** (hipotenusa y cateto en rectángulos).",
                "**`AAA`** no asegura congruencia (solo semejanza) y **`LLA`** tampoco (puede cerrar dos triángulos distintos). En un **triángulo isósceles**, a lados iguales se oponen ángulos iguales.",
            ],
            "real_world": [
                {
                    "title": "Estructuras trianguladas (puentes y torres)",
                    "detail": "Por el criterio `LLL`, tres barras unidas en triángulo no se pueden deformar sin cambiar su largo; un cuadrado sí se aplasta en rombo.",
                },
                {
                    "title": "Control de calidad en piezas CNC",
                    "detail": "En vez de medir todas las cotas de una pieza triangular, basta verificar `LAL` o `LLL` para garantizar que es congruente con el molde.",
                },
                {
                    "title": "Escuadras y marcos rectangulares",
                    "detail": "Un carpintero verifica que un marco rectangular no esté chueco midiendo sus dos diagonales: si los lados opuestos ya miden lo mismo y las diagonales son iguales, los triángulos son congruentes y las esquinas miden `90°`.",
                },
            ],
            "key_rule": "Criterios válidos: LLL, LAL, ALA, AAL y HC. Trampas que NO alcanzan: AAA y LLA.",
            "pitfall": "Usar LAL cuando el ángulo conocido NO está entre los dos lados conocidos (eso es LLA y es ambiguo).",
        },
        "example": {
            "title": "Hallar todos los ángulos de un triángulo isósceles y un paralelogramo",
            "steps": [
                "En un triángulo isósceles con ángulo superior `40°`, los dos ángulos de la base son iguales (`x`).",
                "Planteamos `40° + 2x = 180°` → `2x = 140°` → cada ángulo de la base mide `70°`.",
                "En un paralelogramo donde una esquina mide `62°`, la opuesta también mide `62°` y las dos consecutivas miden `180° − 62° = 118°`.",
            ],
            "lab_link": "math:geometry_angles",
            "lab_cta": "Practicar ángulos y triángulos en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál de estos pares de datos NO garantiza congruencia entre dos triángulos?",
            "options": [
                {"text": "Los tres ángulos iguales (`AAA`)", "ok": True, "feedback": "Exacto: un triángulo equilátero de 2 cm y uno de 2 m tienen los mismos ángulos (60°) pero distinto tamaño."},
                {"text": "Los tres lados iguales (`LLL`)", "ok": False, "feedback": "LLL sí garantiza congruencia única: tres varillas de largo fijo forman un único triángulo."},
                {"text": "Dos ángulos y el lado entre ellos (`ALA`)", "ok": False, "feedback": "ALA sí fija de forma única el punto donde se cruzan los otros dos lados."},
            ],
        },
        "checks": [
            {
                "question": "Un triángulo isósceles tiene dos ángulos iguales de `55°` en la base. ¿Cuánto mide el ángulo superior?",
                "options": [
                    {"text": "`70°`", "ok": True, "feedback": "Exacto: 55° + 55° = 110°, y 180° − 110° = 70°."},
                    {"text": "`55°`", "ok": False, "feedback": "Si los tres fueran 55° sumarían 165°, no 180°."},
                    {"text": "`125°`", "ok": False, "feedback": "Solo restaste uno de los dos ángulos de 55°."},
                ],
            },
            {
                "question": "Si `△PQR ≅ △XYZ` y `∠Q = 82°`, ¿qué ángulo del segundo triángulo mide `82°`?",
                "options": [
                    {"text": "`∠Y`", "ok": True, "feedback": "Exacto: Q es la segunda letra en PQR, así que corresponde a la segunda letra Y en XYZ."},
                    {"text": "`∠X`", "ok": False, "feedback": "X corresponde a P (primera letra)."},
                    {"text": "`∠Z`", "ok": False, "feedback": "Z corresponde a R (tercera letra)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué una estructura triangular es rígida (`LLL`) mientras que un marco rectangular sin diagonal se deforma.",
    },
    "g-semejanza": {
        "hook": "Tales de Mileto midió la altura de la Gran Pirámide hace 2600 años sin escalarla: solo comparó su sombra con la de un bastón.",
        "concept": {
            "points": [
                "Dos figuras son **semejantes (`~`)** cuando tienen los **mismos ángulos** y sus lados correspondientes están en la misma proporción (factor de escala `k`).",
                "En triángulos, basta el criterio **`AA`** (dos ángulos iguales) o **`LAL` / `LLL` proporcionales** para plantear reglas de proporción entre lados.",
                "**Regla de oro del escalado**: si multiplicás todos los lados por `k`, el perímetro se multiplica por `k`, pero el **área se multiplica por `k²`**.",
            ],
            "real_world": [
                {
                    "title": "Planos y maquetas a escala",
                    "detail": "Una escala `1:100` significa que cada `1 cm` del plano equivale a `100 cm` (`1 m`) reales, conservando todos los ángulos idénticos.",
                },
                {
                    "title": "El truco de las pizzas (`k²`)",
                    "detail": "Una pizza de `40 cm` cuesta menos del doble que una de `20 cm`, pero trae `2² = 4` veces más comida.",
                },
                {
                    "title": "Altura de edificios o árboles por sombra",
                    "detail": "A la misma hora, los rayos del sol llegan paralelos: forman triángulos semejantes (`AA`) entre un poste conocido y un edificio alto.",
                },
            ],
            "key_rule": "Semejanza (AA): lados en proporción k = lado_grande / lado_chico; áreas en proporción k².",
            "pitfall": "Creer que duplicar el ancho y el alto de una figura duplica su área: en realidad la cuadruplica (`2² = 4`).",
        },
        "example": {
            "title": "Calcular la altura de un poste con su sombra",
            "steps": [
                "Una persona de `1.8 m` proyecta sombra de `1.2 m`; un poste cercano proyecta sombra de `8 m`.",
                "Los triángulos son semejantes (`AA`: ángulo recto + mismo ángulo solar) → `h / 8 = 1.8 / 1.2`.",
                "Simplificamos `1.8 / 1.2 = 1.5`, así que `h = 8 × 1.5 = 12 m`.",
            ],
            "lab_link": "math:geometry_angles",
            "lab_cta": "Practicar semejanza y escalas en el Laboratorio",
        },
        "check": {
            "question": "Si una figura se amplía con factor de escala `k = 3`, ¿por cuánto se multiplica su área?",
            "options": [
                {"text": "Por `9` (`3²`)", "ok": True, "feedback": "Exacto: el área crece con el cuadrado del factor de escala."},
                {"text": "Por `3`", "ok": False, "feedback": "Por 3 crece el perímetro (longitudes), no el área."},
                {"text": "Por `6`", "ok": False, "feedback": "Es 3 × 3 = 9, no 3 × 2."},
            ],
        },
        "checks": [
            {
                "question": "Dos triángulos son semejantes con razón `k = 2.5`. Si un lado del chico mide `4 cm`, ¿cuánto mide su correspondiente en el grande?",
                "options": [
                    {"text": "`10 cm`", "ok": True, "feedback": "Exacto: 4 × 2.5 = 10 cm."},
                    {"text": "`6.5 cm`", "ok": False, "feedback": "Sumaste 2.5 en vez de multiplicar por 2.5."},
                    {"text": "`25 cm`", "ok": False, "feedback": "Eso multiplicó por k² = 6.25, que es para áreas y no para lados."},
                ],
            },
            {
                "question": "Según el Teorema de Tales, una paralela divide un lado en tramos `3` y `6`, y al otro lado en `5` y `x`. ¿Cuánto vale `x`?",
                "options": [
                    {"text": "`10`", "ok": True, "feedback": "Exacto: 3 / 6 = 5 / x → como 6 es el doble de 3, x es el doble de 5 (10)."},
                    {"text": "`8`", "ok": False, "feedback": "Sumaste +3 en vez de mantener la razón (multiplicar ×2)."},
                    {"text": "`2.5`", "ok": False, "feedback": "Invertiste la proporción (dividiste por 2 en vez de multiplicar por 2)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué duplicar el diámetro de una pizza da 4 veces más superficie y no el doble.",
    },
    "g-pitagoras-especiales": {
        "hook": "Para cruzar una plaza en diagonal caminás menos que bordeando dos cuadras: Pitágoras te dice exactamente cuánto menos.",
        "concept": {
            "points": [
                "En todo **triángulo rectángulo**, los catetos (`a`, `b`) y la **hipotenusa** (`c`, el lado más largo frente al ángulo de `90°`) cumplen **`a² + b² = c²`**.",
                "Si buscás la hipotenusa **sumás** cuadrados (`c = √(a² + b²)`); si buscás un cateto **restás** (`a = √(c² − b²)`). Aprendete las ternas clásicas: **`3-4-5`**, **`5-12-13`**, **`8-15-17`**.",
                "Dos atajos aparecen todo el tiempo: **`45°−45°−90°`** (mitad de un cuadrado: lados `L : L : L√2`) y **`30°−60°−90°`** (mitad de un equilátero: lados `x : x√3 : 2x`).",
            ],
            "real_world": [
                {
                    "title": "Escuadra 3-4-5 en obra y carpintería",
                    "detail": "Para marcar un ángulo recto gigante en un terreno, medís `3 m` y `4 m` en los lados y ajustás hasta que la diagonal mida `5 m` exactos.",
                },
                {
                    "title": "Pulgadas de televisores y celulares",
                    "detail": "Las '55 pulgadas' de una TV son la diagonal (`c`) calculada por Pitágoras desde el ancho y el alto de la pantalla.",
                },
                {
                    "title": "Seguridad al apoyar una escalera",
                    "detail": "Si una escalera de `5 m` se apoya a `3 m` de la pared, solo llega hasta `4 m` de altura (no a `5 m`).",
                },
            ],
            "key_rule": "a² + b² = c² (c = hipotenusa, siempre el lado mayor). Especiales: 45-45-90 → 1 : 1 : √2 | 30-60-90 → 1 : √3 : 2.",
            "pitfall": "Sumar cuadrados cuando el dato que ya tenés es la hipotenusa: si conocés `c` y un cateto, hay que RESTAR (`c² − b²`).",
        },
        "example": {
            "title": "Altura de una escalera de 13 m separada 5 m de la pared",
            "steps": [
                "Identificamos la hipotenusa: es la escalera inclinada (`c = 13 m`), frente al ángulo recto entre pared y piso.",
                "Como falta un cateto (`h`), despejamos restando: `h² = 13² − 5² = 169 − 25 = 144`.",
                "Sacamos raíz cuadrada: `h = √144 = 12 m` (terna clásica `5-12-13`).",
            ],
            "lab_link": "math:pythagoras_trig",
            "lab_cta": "Practicar Pitágoras en el Laboratorio",
        },
        "check": {
            "question": "Un triángulo rectángulo tiene catetos `6 cm` y `8 cm`. ¿Cuánto mide su hipotenusa?",
            "options": [
                {"text": "`10 cm`", "ok": True, "feedback": "Exacto: √(36 + 64) = √100 = 10 cm (el doble de la terna 3-4-5)."},
                {"text": "`14 cm`", "ok": False, "feedback": "Sumaste 6 + 8 directo sin elevar al cuadrado ni sacar raíz."},
                {"text": "`100 cm`", "ok": False, "feedback": "Te faltó el último paso: sacar la raíz cuadrada de 100."},
            ],
        },
        "checks": [
            {
                "question": "Si la hipotenusa mide `10 m` y un cateto mide `6 m`, ¿cuánto mide el otro cateto?",
                "options": [
                    {"text": "`8 m`", "ok": True, "feedback": "Exacto: √(10² − 6²) = √(100 − 36) = √64 = 8 m."},
                    {"text": "`11.7 m` (`√136`)", "ok": False, "feedback": "Sumaste 100 + 36, pero un cateto nunca puede ser más largo que la hipotenusa (10 m)."},
                    {"text": "`4 m`", "ok": False, "feedback": "Restaste 10 − 6 en vez de restar los cuadrados 10² − 6²."},
                ],
            },
            {
                "question": "En un triángulo `30°−60°−90°`, la hipotenusa mide `20 cm`. ¿Cuánto mide el cateto opuesto a `30°`?",
                "options": [
                    {"text": "`10 cm`", "ok": True, "feedback": "Exacto: frente a 30° siempre mide exactamente la mitad de la hipotenusa."},
                    {"text": "`20√2 cm`", "ok": False, "feedback": "√2 aparece en el 45°-45°-90°, y el cateto nunca supera a la hipotenusa."},
                    {"text": "`5 cm`", "ok": False, "feedback": "Dividiste por 4 en vez de por 2."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá cómo saber rápido si en un problema de Pitágoras tenés que sumar cuadrados o restarlos.",
    },
    "g-trigonometria": {
        "hook": "Seno, coseno y tangente no son botones misteriosos de la calculadora: son simplemente tres fracciones entre los lados de un triángulo rectángulo.",
        "concept": {
            "points": [
                "Respecto a un ángulo agudo `θ`, llamamos **Opuesto (O)** al cateto de enfrente, **Adyacente (A)** al cateto pegado a `θ`, e **Hipotenusa (H)** al lado más largo.",
                "Regla **`SOH-CAH-TOA`**: **`sen(θ) = O/H`**, **`cos(θ) = A/H`**, **`tan(θ) = O/A`** (nota: `tan(θ)` es exactamente la pendiente `Δy/Δx`).",
                "Para hallar un **lado** multiplicás o dividís por `sen`/`cos`/`tan`; para hallar un **ángulo** a partir de los lados usás las funciones inversas (`arcsen`, `arccos`, `arctan`). Además, **`sen(θ) = cos(90° − θ)`**.",
            ],
            "real_world": [
                {
                    "title": "Descomponer fuerzas y vectores en Física",
                    "detail": "Una fuerza `F` inclinada un ángulo `θ` se separa al instante en `F_x = F·cos(θ)` y `F_y = F·sen(θ)`.",
                },
                {
                    "title": "Rampas accesibles y techos",
                    "detail": "La pendiente de una rampa o un techo es `tan(θ) = subida / recorrido horizontal`; con `arctan` sabés el ángulo exacto de inclinación.",
                },
                {
                    "title": "Topografía y altura de antenas",
                    "detail": "Con un clinómetro (ángulo de elevación `θ`) y la distancia horizontal `d` a una torre, su altura es `d · tan(θ)`.",
                },
            ],
            "key_rule": "SOH: sen = O/H | CAH: cos = A/H | TOA: tan = O/A | Cofunción: sen(θ) = cos(90° − θ).",
            "pitfall": "Confundir Opuesto y Adyacente al cambiar de esquina: el Opuesto depende de QUÉ ángulo estés mirando (el opuesto de uno es el adyacente del otro).",
        },
        "example": {
            "title": "Hallar la altura de un barrilete con 40 m de hilo a 30°",
            "steps": [
                "Respecto al ángulo de `30°`, conocemos la hipotenusa (`H = 40 m`) y buscamos la altura vertical, que es el cateto **Opuesto** (`h`).",
                "Como relaciona Opuesto e Hipotenusa, elegimos **SOH**: `sen(30°) = h / 40`.",
                "Sabiendo que `sen(30°) = 0.5`, despejamos: `h = 40 × 0.5 = 20 m`.",
            ],
            "lab_link": "math:pythagoras_trig",
            "lab_cta": "Practicar SOH-CAH-TOA en el Laboratorio",
        },
        "check": {
            "question": "En un triángulo rectángulo `5-12-13`, el cateto adyacente a `θ` es `12` y la hipotenusa es `13`. ¿Cuánto vale `cos(θ)`?",
            "options": [
                {"text": "`12/13`", "ok": True, "feedback": "Exacto: por CAH, cos(θ) = Adyacente / Hipotenusa = 12/13."},
                {"text": "`5/13`", "ok": False, "feedback": "5/13 es sen(θ) (Opuesto / Hipotenusa)."},
                {"text": "`5/12`", "ok": False, "feedback": "5/12 es tan(θ) (Opuesto / Adyacente)."},
            ],
        },
        "checks": [
            {
                "question": "Querés hallar el ángulo `θ` de una rampa conociendo su altura (`O`) y su base horizontal (`A`). ¿Qué operación usás?",
                "options": [
                    {"text": "`arctan(O / A)`", "ok": True, "feedback": "Exacto: tan relaciona O y A, y la función inversa arctan devuelve el ángulo."},
                    {"text": "`tan(O / A)`", "ok": False, "feedback": "tan espera un ángulo como entrada; cuando la entrada es una razón de lados se usa arctan (tan⁻¹)."},
                    {"text": "`arcsen(O / A)`", "ok": False, "feedback": "Seno usa Hipotenusa, no Adyacente."},
                ],
            },
            {
                "question": "Si `cos(60°) = 0.5`, ¿para qué ángulo agudo vale `sen(θ) = 0.5`?",
                "options": [
                    {"text": "`30°` (`90° − 60°`)", "ok": True, "feedback": "Exacto: sen(30°) = cos(60°) = 0.5 por ser ángulos complementarios."},
                    {"text": "`60°`", "ok": False, "feedback": "sen(60°) ≈ 0.866; solo coinciden en 45°."},
                    {"text": "`45°`", "ok": False, "feedback": "sen(45°) = cos(45°) ≈ 0.707."},
                ],
            },
        ],
        "takeaway_prompt": "Escribí de memoria SOH-CAH-TOA y un ejemplo cotidiano donde usarías `tan(θ)`.",
    },
    "g-analitica-plano": {
        "hook": "Poner las figuras sobre el plano cartesiano convierte preguntas geométricas ('¿es un rectángulo?', '¿dónde queda el medio?') en cuentas exactas.",
        "concept": {
            "points": [
                "**Distancia entre dos puntos** `A(x₁, y₁)` y `B(x₂, y₂)`: es solo Pitágoras sobre los catetos `Δx` y `Δy`: **`d = √((x₂ − x₁)² + (y₂ − y₁)²)`**.",
                "**Punto medio**: es el promedio simple de las coordenadas: **`M = ((x₁ + x₂)/2, (y₁ + y₂)/2)`**.",
                "Para **dividir un segmento** en una fracción `t` del recorrido (ej. razón `1:3` → `t = 1/4`), sumás esa fracción del avance: `A + t · (B − A)`. Y para probar paralelas o ángulos de `90°`, usás **pendientes** (`m₁ = m₂` vs. `m₁ · m₂ = −1`).",
            ],
            "real_world": [
                {
                    "title": "GPS y apps de delivery",
                    "detail": "Calcular el radio de entrega desde un local hasta un domicilio usa la fórmula de distancia sobre coordenadas.",
                },
                {
                    "title": "Interpolación de animaciones (lerp)",
                    "detail": "Mover un botón suavemente de A a B al 25% del tiempo es exactamente particionar el segmento con `t = 0.25`.",
                },
                {
                    "title": "Verificar figuras en CAD",
                    "detail": "Un programa decide si cuatro puntos forman un rectángulo chequeando que las pendientes adyacentes cumplan `m₁ · m₂ = −1` (un lado vertical no tiene pendiente: es perpendicular solo a los horizontales).",
                },
            ],
            "key_rule": "d = √((x₂ − x₁)² + (y₂ − y₁)²) | Punto medio = ((x₁ + x₂)/2, (y₁ + y₂)/2).",
            "pitfall": "Restar las coordenadas al calcular el punto medio: para distancia se RESTA (`x₂ − x₁`), pero para punto medio se SUMA y divide por 2 (`(x₁ + x₂)/2`).",
        },
        "example": {
            "title": "Distancia y punto medio entre A(−2, 1) y B(4, 9)",
            "steps": [
                "Calculamos los desplazamientos: `Δx = 4 − (−2) = 6` y `Δy = 9 − 1 = 8`.",
                "Aplicamos Pitágoras (distancia): `d = √(6² + 8²) = √(36 + 64) = √100 = 10`.",
                "Para el punto medio promediamos: `x_M = (−2 + 4)/2 = 1`, `y_M = (1 + 9)/2 = 5` → `M(1, 5)`.",
            ],
            "lab_link": "math:geometry_coords",
            "lab_cta": "Practicar distancia y punto medio en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es la distancia entre `(0, 0)` y `(5, 12)`?",
            "options": [
                {"text": "`13`", "ok": True, "feedback": "Exacto: √(5² + 12²) = √(25 + 144) = √169 = 13."},
                {"text": "`17`", "ok": False, "feedback": "17 es la distancia 'por cuadras' (5 + 12), no en línea recta."},
                {"text": "`169`", "ok": False, "feedback": "Te faltó sacar la raíz cuadrada de 169."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál es el punto medio entre `(−6, 4)` y `(2, 10)`?",
                "options": [
                    {"text": "`(−2, 7)`", "ok": True, "feedback": "Exacto: (−6 + 2)/2 = −2 y (4 + 10)/2 = 7."},
                    {"text": "`(−4, 3)`", "ok": False, "feedback": "Restaste las coordenadas en vez de sumarlas antes de dividir por 2."},
                    {"text": "`(−4, 14)`", "ok": False, "feedback": "Sumaste bien, pero te faltó dividir cada coordenada por 2."},
                ],
            },
            {
                "question": "Si dos segmentos del plano tienen pendientes `m₁ = 3` y `m₂ = −1/3`, ¿cómo son entre sí?",
                "options": [
                    {"text": "Perpendiculares (forman `90°`)", "ok": True, "feedback": "Exacto: 3 · (−1/3) = −1, recíprocas y opuestas."},
                    {"text": "Paralelos", "ok": False, "feedback": "Para ser paralelos tendrían que tener exactamente la misma pendiente."},
                    {"text": "Coincidentes", "ok": False, "feedback": "Sus inclinaciones son completamente distintas."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en una frase cómo distinguir cuándo se resta (`x₂ − x₁`) y cuándo se suma (`x₁ + x₂`) en geometría analítica.",
    },
    "g-ecuacion-circulo": {
        "hook": "La ecuación de un círculo no es una fórmula para memorizar: es literalmente la fórmula de distancia diciendo 'todos los puntos a distancia r del centro'.",
        "concept": {
            "points": [
                "Una circunferencia de centro `(h, k)` y radio `r` tiene ecuación estándar **`(x − h)² + (y − k)² = r²`**.",
                "Dos cuidados clave al leerla: **invertí el signo** al leer el centro (`(x + 2)²` significa `h = −2`), y **sacá raíz** al número de la derecha (`= 25` significa `r = 5`, no `25`).",
                "Si la ecuación viene expandida (`x² − 6x + y² + 4y = 3`), **completás cuadrados** sumando `(b/2)²` a ambos lados. Además, el círculo es una de las 4 **secciones cónicas** junto con elipse, parábola e hipérbola.",
            ],
            "real_world": [
                {
                    "title": "Zonas de cobertura (Wi-Fi, radar, geolocalización)",
                    "detail": "Chequear si un usuario está dentro de un radio `r` es solo evaluar si `(x − h)² + (y − k)² ≤ r²`.",
                },
                {
                    "title": "Colisiones circulares en juegos",
                    "detail": "Los motores comparan `dx² + dy² ≤ (r₁ + r₂)²` sin siquiera calcular raíces cuadradas para ser ultra rápidos.",
                },
                {
                    "title": "Antenas parabólicas y órbitas elípticas",
                    "detail": "Cambiar la inclinación con que un plano corta un cono produce círculos, elipses (planetas), parábolas (antenas) e hipérbolas.",
                },
            ],
            "key_rule": "(x − h)² + (y − k)² = r² → centro (h, k) con signos invertidos y radio r = √(lado derecho).",
            "pitfall": "Leer `r = 36` en `(x − 1)² + (y − 2)² = 36`: el lado derecho siempre es `r²`, así que el radio real es `√36 = 6`.",
        },
        "example": {
            "title": "Pasar x² − 6x + y² + 4y = 3 a forma estándar",
            "steps": [
                "Para `x² − 6x`, tomamos la mitad de `−6` (`−3`) y la elevamos al cuadrado: `(−3)² = 9`.",
                "Para `y² + 4y`, tomamos la mitad de `+4` (`+2`) y la elevamos al cuadrado: `2² = 4`.",
                "Sumamos `9` y `4` en AMBOS lados: `(x − 3)² + (y + 2)² = 3 + 9 + 4 = 16` → centro `(3, −2)` y radio `r = √16 = 4`.",
            ],
            "lab_link": "math:geometry_coords",
            "lab_cta": "Practicar círculos en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es el centro y el radio de `(x + 4)² + (y − 1)² = 49`?",
            "options": [
                {"text": "Centro `(−4, 1)` y radio `7`", "ok": True, "feedback": "Exacto: signos invertidos para el centro y √49 = 7 para el radio."},
                {"text": "Centro `(4, −1)` y radio `7`", "ok": False, "feedback": "Fijate qué valor anula cada paréntesis: (−4) + 4 = 0 y (1) − 1 = 0."},
                {"text": "Centro `(−4, 1)` y radio `49`", "ok": False, "feedback": "49 es r², no r: falta sacar raíz cuadrada."},
            ],
        },
        "checks": [
            {
                "question": "El círculo `x² + y² = 100` tiene radio `10`. ¿Dónde queda el punto `(6, 8)`?",
                "options": [
                    {"text": "Exactamente sobre la circunferencia (`36 + 64 = 100`)", "ok": True, "feedback": "Exacto: 6² + 8² = 100, su distancia al origen es exactamente 10."},
                    {"text": "Adentro del círculo", "ok": False, "feedback": "Estaría adentro solo si x² + y² fuera menor que 100."},
                    {"text": "Afuera del círculo", "ok": False, "feedback": "Estaría afuera solo si x² + y² fuera mayor que 100."},
                ],
            },
            {
                "question": "Para completar el cuadrado en `x² + 10x`, ¿qué número debés sumar a ambos lados?",
                "options": [
                    {"text": "`25` (`(10 / 2)²`)", "ok": True, "feedback": "Exacto: x² + 10x + 25 = (x + 5)²."},
                    {"text": "`10`", "ok": False, "feedback": "Tenés que tomar la mitad (5) y elevarla al cuadrado (25)."},
                    {"text": "`100`", "ok": False, "feedback": "Elevaste 10 sin dividirlo primero por 2."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá los dos errores más comunes al leer `(x − h)² + (y − k)² = r²` y cómo evitarlos.",
    },
    "g-circulos-arcos": {
        "hook": "Una porción de pizza, una curva de autopista o una polea con correa son todas fracciones del mismo círculo completo de `360°`.",
        "concept": {
            "points": [
                "Un **ángulo inscrito** (vértice en el borde) mide siempre la **mitad del ángulo central** que abarca el mismo arco. En particular, todo triángulo inscrito sobre un diámetro es rectángulo (`90°`).",
                "Toda **recta tangente** toca al círculo en un solo punto y forma exactamente **`90°` con el radio** en ese punto (ideal para aplicar Pitágoras).",
                "Para **arcos y sectores**, usás la fracción de vuelta `θ / 360°`: longitud de arco **`L = (θ/360) · 2πr`** y área de sector **`A = (θ/360) · πr²`**. En **radianes**, media vuelta es **`π rad = 180°`** (`2π = 360°`).",
            ],
            "real_world": [
                {
                    "title": "Limpiaparabrisas y aspersores de riego",
                    "detail": "El área que barre un aspersor girando `120°` (`1/3` de vuelta) es un sector circular de área `(1/3) · πr²`.",
                },
                {
                    "title": "Correas y poleas mecánicas",
                    "detail": "La correa sale tangente formando `90°` con el radio de la polea, lo que permite calcular el largo exacto de correa necesaria.",
                },
                {
                    "title": "Velocidad angular en física y robótica",
                    "detail": "En ingeniería los ángulos se miden en radianes (`π rad = 180°`) porque simplifican la fórmula de arco a simplemente `L = r · θ`.",
                },
            ],
            "key_rule": "Inscrito = Central / 2 | Tangente ⊥ radio (90°) | Arco = (θ/360)·2πr | Sector = (θ/360)·πr² | π rad = 180°.",
            "pitfall": "Mezclar `2πr` (perímetro, para longitud de arco) con `πr²` (área, para sector circular).",
        },
        "example": {
            "title": "Porción de pizza de 60° (r = 12 cm) y conversión a radianes",
            "steps": [
                "La fracción del círculo es `60° / 360° = 1/6` de la pizza completa.",
                "Área del sector: `(1/6) · π · 12² = (1/6) · 144π = 24π ≈ 75.4 cm²`.",
                "En radianes: como `180° = π`, entonces `60°` es la tercera parte → `π / 3 rad`.",
            ],
            "lab_link": "math:geometry_3d",
            "lab_cta": "Practicar arcos y sectores en el Laboratorio",
        },
        "check": {
            "question": "Si un ángulo inscrito mide `38°`, ¿cuánto mide el ángulo central que abarca el mismo arco?",
            "options": [
                {"text": "`76°` (el doble)", "ok": True, "feedback": "Exacto: el ángulo central siempre mide el doble que el inscrito."},
                {"text": "`19°` (la mitad)", "ok": False, "feedback": "Al revés: el inscrito es el más chico (la mitad del central)."},
                {"text": "`38°` (lo mismo)", "ok": False, "feedback": "El central tiene el vértice más cerca del arco, así que abre el doble."},
            ],
        },
        "checks": [
            {
                "question": "Un aspersor riega un ángulo de `90°` con alcance `r = 6 m`. ¿Qué fracción del círculo completo riega?",
                "options": [
                    {"text": "`1/4` del círculo (`9π ≈ 28.3 m²`)", "ok": True, "feedback": "Exacto: 90°/360° = 1/4, y (1/4)·π·36 = 9π."},
                    {"text": "`1/3` del círculo", "ok": False, "feedback": "1/3 corresponde a 120°."},
                    {"text": "`1/2` del círculo", "ok": False, "feedback": "1/2 corresponde a 180°."},
                ],
            },
            {
                "question": "¿A cuántos grados equivale `π/2` radianes?",
                "options": [
                    {"text": "`90°`", "ok": True, "feedback": "Exacto: si π rad = 180°, entonces la mitad (π/2) es 90°."},
                    {"text": "`180°`", "ok": False, "feedback": "180° es π radianes completos."},
                    {"text": "`45°`", "ok": False, "feedback": "45° es π/4 radianes."},
                ],
            },
        ],
        "takeaway_prompt": "Resumí la diferencia entre la fórmula de longitud de arco y la de área de sector circular.",
    },
    "g-geometria-solida": {
        "hook": "Todos los volúmenes 3D importantes siguen una sola familia: prismas/cilindros son 'base × altura', conos/pirámides son un tercio de eso, y al duplicar tamaño el volumen crece ×8.",
        "concept": {
            "points": [
                "**Prismas y cilindros**: **`V = A_base · h`** (cilindro: `V = πr²h`). Por el **Principio de Cavalieri**, aunque inclines una pila de monedas, si cada corte mantiene la misma área y altura, el volumen no cambia.",
                "**Pirámides y conos** (terminan en punta): siempre ocupan exactamente **`1/3`** del prisma o cilindro de igual base y altura → **`V = (1/3) · A_base · h`**.",
                "**Esfera**: **`V = (4/3)πr³`** y área superficial **`A = 4πr²`**. Al escalar un sólido por `k`, su volumen crece por **`k³`**, y su masa es **`masa = densidad × volumen`**.",
            ],
            "real_world": [
                {
                    "title": "Tanques de agua y envases",
                    "detail": "Como `1 m³ = 1000 litros`, calcular `V = πr²h` te dice exactamente cuántos litros carga un tanque cilíndrico.",
                },
                {
                    "title": "Impresión 3D y costos de filamento (`k³`)",
                    "detail": "Si imprimís una figura maciza al doble de altura (`k = 2`), usa `2³ = 8` veces más plástico y tarda mucho más en imprimirse.",
                },
                {
                    "title": "Cálculo de peso en envíos y construcción",
                    "detail": "Multiplicando el volumen de una viga o bloque por la densidad del material (`kg/m³`) sabés si la estructura o el flete soporta el peso.",
                },
            ],
            "key_rule": "Cilindro/Prisma: A_base·h | Cono/Pirámide: (1/3)·A_base·h | Esfera: (4/3)πr³ | Escala 3D: V × k³.",
            "pitfall": "Usar el diámetro en lugar del radio en `πr²h` o `(4/3)πr³`: siempre dividí el diámetro por 2 antes de elevar al cuadrado o al cubo.",
        },
        "example": {
            "title": "Volumen de un cilindro y un cono con r = 3 cm y h = 10 cm",
            "steps": [
                "Área de la base circular: `A_base = π · 3² = 9π ≈ 28.27 cm²`.",
                "Volumen del cilindro: `V_cil = 9π × 10 = 90π ≈ 282.7 cm³`.",
                "Volumen del cono de igual base y altura: exactamente un tercio → `V_cono = 90π / 3 = 30π ≈ 94.2 cm³`.",
            ],
            "lab_link": "math:geometry_3d",
            "lab_cta": "Practicar volúmenes 3D en el Laboratorio",
        },
        "check": {
            "question": "Un cilindro y un cono tienen el mismo radio y la misma altura. Si el cono carga `200 mL`, ¿cuánto carga el cilindro?",
            "options": [
                {"text": "`600 mL` (el triple)", "ok": True, "feedback": "Exacto: el cilindro equivale a 3 conos iguales."},
                {"text": "`400 mL` (el doble)", "ok": False, "feedback": "En 3D la relación entre cono y cilindro es 1/3, no 1/2."},
                {"text": "`200 mL` (lo mismo)", "ok": False, "feedback": "Al afinarse hasta la punta el cono pierde dos tercios del volumen."},
            ],
        },
        "checks": [
            {
                "question": "Si una botella semejante tiene el triple de alto, ancho y profundidad (`k = 3`), ¿cuántas veces más líquido entra?",
                "options": [
                    {"text": "`27` veces más (`3³`)", "ok": True, "feedback": "Exacto: el volumen escala con el cubo del factor de escala (3 × 3 × 3 = 27)."},
                    {"text": "`9` veces más (`3²`)", "ok": False, "feedback": "3² = 9 es cómo escala el área de la etiqueta, no el volumen."},
                    {"text": "`3` veces más", "ok": False, "feedback": "Solo crecería ×3 si únicamente estiraras la altura manteniendo igual la base."},
                ],
            },
            {
                "question": "Una pila de 20 monedas está perfectamente derecha y otra idéntica está inclinada de costado. Según Cavalieri, ¿cuál tiene mayor volumen?",
                "options": [
                    {"text": "Tienen exactamente el mismo volumen", "ok": True, "feedback": "Exacto: misma altura y misma área en cada corte horizontal implica igual volumen."},
                    {"text": "La inclinada, porque sus paredes laterales son más largas", "ok": False, "feedback": "Aumenta el área lateral, pero el volumen interno de las 20 monedas no cambia."},
                    {"text": "La derecha, porque es más compacta", "ok": False, "feedback": "Ambas están formadas exactamente por las mismas 20 monedas."},
                ],
            },
        ],
        "takeaway_prompt": "Compará cómo escala una figura con factor `k` en longitudes (`k`), área (`k²`) y volumen (`k³`) usando un ejemplo cotidiano.",
    },
}
