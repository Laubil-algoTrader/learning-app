"""Precalculus curriculum (8 units, #69-#76) adapted from Khan Academy Precalculus.

Covers all new Precalculus units building on Álgebra 2 (#52-#62) and Trigonometría (#63-#68):
  - Complex plane, polar form & De Moivre's Theorem
  - Conic sections: ellipses, hyperbolas & focus-directrix parabolas
  - 2D Vectors: components, magnitude, unit vectors & dot product
  - Matrices: dimensions, operations, matrix multiplication & 2D transforms
  - Determinants, 2x2 matrix inverses & solving linear systems AX = B
  - Combinatorics & probability: counting principle, permutations (nPr) & combinations (nCr)
  - Series & sigma notation: arithmetic, finite & infinite geometric series, Binomial Theorem
  - Introduction to limits & continuity (bridge to Calculus)
"""

from __future__ import annotations

PRECALCULUS_NODES: list[dict] = [
    # ==================== NIVEL 25: COMPLEJOS POLARES, CÓNICAS Y VECTORES ====================
    {
        "slug": "pc-complejos-polares",
        "title": "69. Plano complejo, forma polar y Teorema de De Moivre",
        "level": 25,
        "order_index": 69,
        "summary": "División con conjugados, coordenadas polares r(cos θ + i·sen θ), multiplicar girando ángulos y potencias con De Moivre.",
        "prerequisites": ["a2-numeros-complejos", "t-reciprocas-referencia"],
        "metadata": {"section": "Precálculo", "lab_tab": "complex_nums", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Multiplicar dos números complejos en forma polar",
                "prompt": "En forma polar, al multiplicar dos complejos se MULTIPLICAN los radios y se SUMAN los ángulos: (3∠40°) · (5∠25°). ¿Cuál es el módulo (radio) resultante? Respondé solo con el número.",
                "answer": "15 (el resultado completo es 15∠65°: 3 × 5 = 15 y 40° + 25° = 65°).",
                "hints": ["Multiplicá los módulos: 3 × 5."],
                "payload": {
                    "lab_link": "math:complex_nums",
                    "check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ángulo resultante al multiplicar complejos polares",
                "prompt": "En el mismo producto (3∠40°) · (5∠25°), ¿cuántos grados mide el ángulo resultante? Respondé solo con el número.",
                "answer": "65°: multiplicar por un complejo rota el vector sumando los ángulos (40° + 25° = 65°).",
                "hints": ["Sumá ambos ángulos: 40° + 25°."],
                "payload": {"check": {"type": "numeric", "value": 65, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Teorema de De Moivre: elevar un complejo al cubo",
                "prompt": "Por De Moivre, (r∠θ)ⁿ = rⁿ∠(n·θ). Al calcular (2∠30°)³ obtenés 8∠90°. ¿Cuál es la parte imaginaria (coeficiente de i) de 8∠90°? Respondé solo con el número.",
                "answer": "8: 8(cos 90° + i·sen 90°) = 8(0 + 1i) = 8i.",
                "hints": ["2³ = 8 y 3 × 30° = 90° (apunta directo hacia arriba sobre el eje imaginario)."],
                "payload": {"check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Pasar de forma polar a rectangular (parte real)",
                "prompt": "Un fasor eléctrico tiene magnitud r = 10 y ángulo θ = 60° (cos 60° = 0.5). ¿Cuál es su parte real a = r · cos(θ)? Respondé solo con el número.",
                "answer": "5: a = 10 × cos(60°) = 10 × 0.5 = 5 (y la parte imaginaria es 10·sen(60°) ≈ 8.66).",
                "hints": ["Multiplicá r × cos(60°)."],
                "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0.01, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Distancia entre dos números en el plano complejo",
                "prompt": "Calculá la distancia |z₂ − z₁| entre z₁ = 1 + 2i y z₂ = 4 + 6i. Respondé solo con el número.",
                "answer": "5: z₂ − z₁ = 3 + 4i → |3 + 4i| = √(3² + 4²) = 5.",
                "hints": ["Restá las partes reales (4 − 1 = 3) e imaginarias (6 − 2 = 4) y aplicá Pitágoras."],
                "payload": {
                    "lab_link": "math:complex_nums",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Dividir complejos multiplicando por el conjugado",
                "prompt": "Dividí (2 + 6i) / (1 + i) multiplicando numerador y denominador por (1 − i): arriba queda (2 + 6i)(1 − i) = 8 + 4i y abajo 1² + 1² = 2. ¿Cuál es la parte REAL del cociente? Respondé solo con el número.",
                "answer": "4: (8 + 4i) / 2 = 4 + 2i (parte real = 4, parte imaginaria = 2).",
                "hints": ["Dividí 8 ÷ 2."],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    {
        "slug": "pc-secciones-conicas",
        "title": "70. Secciones cónicas: elipses, hipérbolas y focos",
        "level": 25,
        "order_index": 70,
        "summary": "Ecuaciones estándar de elipses e hipérbolas, cálculo de focos (c² = a² ± b²), asíntotas y parábola foco-directriz.",
        "prerequisites": ["g-ecuacion-circulo", "al-parabolas-formula"],
        "metadata": {"section": "Precálculo", "lab_tab": "geometry_coords", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Leer el semieje mayor de una elipse",
                "prompt": "Una pista ovalada sigue la ecuación de elipse x²/25 + y²/9 = 1 (en metros). ¿Cuántos metros mide el semieje mayor a (del centro al extremo más lejano)? Respondé solo con el número.",
                "answer": "5 m: los denominadores son a² = 25 y b² = 9, así que los semiejes miden a = 5 m (horizontal) y b = 3 m (vertical).",
                "hints": ["Sacá la raíz cuadrada del denominador mayor (25)."],
                "payload": {
                    "lab_link": "math:geometry_coords",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "m"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Hallar la distancia c del centro a cada foco de una elipse",
                "prompt": "En la elipse x²/25 + y²/9 = 1, los focos están a distancia c del centro cumpliendo c² = a² − b² (restás los denominadores). ¿Cuánto vale c? Respondé solo con el número.",
                "answer": "4: c² = 25 − 9 = 16 → c = 4 (los focos están en (−4, 0) y (4, 0), siempre adentro de la elipse!).",
                "hints": ["Calculá √(25 − 9)."],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Hallar los focos de una hipérbola (c² = a² + b²)",
                "prompt": "En la hipérbola x²/9 − y²/16 = 1, los focos cumplen c² = a² + b² (sumás los denominadores). ¿Cuánto vale c? Respondé solo con el número.",
                "answer": "5: c² = 9 + 16 = 25 → c = 5 (en una hipérbola los focos están más lejos que los vértices: 5 > 3).",
                "hints": ["Calculá √(9 + 16)."],
                "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Leer hacia dónde abre y las asíntotas de una hipérbola",
                "prompt": "En la hipérbola x²/9 − y²/16 = 1 (donde x² es el término positivo, a = 3, b = 4), ¿hacia dónde abren sus ramas y cuáles son sus asíntotas?",
                "answer": "Abre a izquierda y derecha (eje X) con asíntotas y = ±(4/3)x (pendiente = ±b/a).",
                "hints": ["El término con signo + marca el eje de apertura, y la pendiente es ±(raíz bajo y)/(raíz bajo x)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Abre izquierda/derecha con asíntotas y = ±(4/3)x",
                            "Abre arriba/abajo con asíntotas y = ±(3/4)x",
                            "Es un óvalo cerrado sin asíntotas",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Foco de una antena parabólica (x² = 4py)",
                "prompt": "Una antena satelital tiene perfil x² = 12y (en cm). Comparando con x² = 4py, ¿a cuántos cm del vértice (0, 0) hay que colocar el receptor en el foco (0, p)? Respondé solo con el número.",
                "answer": "3 cm: 4p = 12 → p = 3 cm (todos los rayos paralelos que rebotan en la parábola convergen exacto en (0, 3)!).",
                "hints": ["Igualá 4p = 12 y despejá p."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": "cm"}},
            },
            {
                "item_type": "recall",
                "title": "Identificar cualquier cónica de un vistazo",
                "prompt": "Sin graficar, mirá la ecuación 4x² − 9y² = 36. ¿Qué sección cónica representa?",
                "answer": "Una hipérbola: ambos términos están al cuadrado pero tienen SIGNOS OPUESTOS (+4 y −9).",
                "hints": ["Mismos coeficientes positivos = círculo; distintos pero mismo signo = elipse; signos opuestos = hipérbola."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Hipérbola", "Elipse", "Parábola"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "pc-vectores",
        "title": "71. Vectores 2D: componentes, magnitud y producto punto",
        "level": 25,
        "order_index": 71,
        "summary": "Operar vectores en componentes ⟨vx, vy⟩, normalizar a vector unitario, pasar de ángulo a componentes y usar el producto punto.",
        "prerequisites": ["g-analitica-plano", "t-reciprocas-referencia"],
        "metadata": {"section": "Precálculo", "lab_tab": "vectors_matrices", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Magnitud de una suma de vectores (viento + dron)",
                "prompt": "Un dron avanza con vector u = ⟨3, −2⟩ m/s y el viento lo empuja con v = ⟨1, 5⟩ m/s. El vector resultante es u + v = ⟨4, 3⟩. ¿Cuál es su rapidez total |u + v| (en m/s)? Respondé solo con el número.",
                "answer": "5 m/s: |⟨4, 3⟩| = √(4² + 3²) = √25 = 5 m/s.",
                "hints": ["Aplicá Pitágoras sobre ⟨4, 3⟩."],
                "payload": {
                    "lab_link": "math:vectors_matrices",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "m/s"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Descomponer un vector desde magnitud y ángulo",
                "prompt": "Un barco navega a 20 km/h con rumbo a 60° respecto al eje horizontal (cos 60° = 0.5). ¿Cuál es su componente horizontal v_x = |v| · cos(60°) en km/h? Respondé solo con el número.",
                "answer": "10 km/h: 20 × 0.5 = 10 km/h hacia el este.",
                "hints": ["Multiplicá 20 por cos(60°) = 0.5."],
                "payload": {"check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "km/h"}},
            },
            {
                "item_type": "worked_example",
                "title": "Normalizar a vector unitario (dirección pura)",
                "prompt": "El vector v = ⟨6, 8⟩ tiene magnitud |v| = 10. Para obtener el vector unitario u = v / |v| (misma dirección, largo 1), dividís cada componente por 10. ¿Cuál es la componente x de u en decimal? Respondé solo con el número.",
                "answer": "0.6: u = ⟨6/10, 8/10⟩ = ⟨0.6, 0.8⟩ (chequeo: √(0.6² + 0.8²) = 1).",
                "hints": ["Dividí la componente x (6) por la magnitud (10)."],
                "payload": {"check": {"type": "numeric", "value": 0.6, "tolerance": 0.01, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Calcular el producto punto u · v",
                "prompt": "Calculá el producto punto (escalar) de u = ⟨2, 5⟩ y v = ⟨3, −1⟩ usando u_x·v_x + u_y·v_y. Respondé solo con el número.",
                "answer": "1: (2)(3) + (5)(−1) = 6 − 5 = 1 (el producto punto siempre devuelve un NÚMERO escalar, no un vector).",
                "hints": ["Multiplicá x con x, y con y, y sumá ambos resultados."],
                "payload": {
                    "lab_link": "math:vectors_matrices",
                    "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Detectar vectores perpendiculares con el producto punto",
                "prompt": "Calculá el producto punto entre u = ⟨3, 4⟩ y v = ⟨−4, 3⟩. Respondé solo con el número.",
                "answer": "0: (3)(−4) + (4)(3) = −12 + 12 = 0. Entre vectores no nulos, producto punto igual a 0 significa SIEMPRE que forman exactamente 90°!",
                "hints": ["Hacé 3(−4) + 4(3)."],
                "payload": {
                    "lab_link": "math:vectors_matrices",
                    "check": {"type": "numeric", "value": 0, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Qué indica el signo del producto punto",
                "prompt": "En un motor de videojuegos 3D, el producto punto entre la dirección de mirada de un enemigo y el vector hacia el jugador da un número NEGATIVO (u · v < 0). ¿Dónde está el jugador?",
                "answer": "Detrás del enemigo (ángulo mayor a 90°): porque u · v = |u||v|cos(θ), y cos(θ) < 0 cuando el ángulo es obtuso.",
                "hints": ["Recordá que u · v = |u||v|cos(θ): positivo = agudo (adelante), cero = 90° (costado), negativo = obtuso (atrás)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Detrás del enemigo (ángulo obtuso > 90°)",
                            "Exactamente frente a él (ángulo agudo < 90°)",
                            "A 90° exactos de costado",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 26: MATRICES, DETERMINANTES E INVERSAS ====================
    {
        "slug": "pc-matrices-operaciones",
        "title": "72. Matrices: dimensiones, producto matricial y transformaciones",
        "level": 26,
        "order_index": 72,
        "summary": "Regla de dimensiones (m×n)·(n×p), multiplicación fila por columna, no conmutatividad (AB ≠ BA) y transformaciones 2D.",
        "prerequisites": ["pc-vectores", "p-sistemas-ecuaciones"],
        "metadata": {"section": "Precálculo", "lab_tab": "vectors_matrices", "est_minutes": 20},
        "items": [
            {
                "item_type": "recall",
                "title": "Compatibilidad y dimensión del producto matricial",
                "prompt": "Si A es una matriz de 2 × 3 (2 filas, 3 columnas) y B es de 3 × 4, ¿se puede calcular el producto A · B y qué dimensión tendrá?",
                "answer": "Sí, resulta una matriz de 2 × 4: los números internos coinciden (3 = 3) y los extremos dan el tamaño final (2 × 4).",
                "hints": ["(m × n) · (n × p) exige que los del medio sean iguales y deja (m × p)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Sí, da una matriz de 2 × 4", "Sí, da una matriz de 3 × 3", "No se puede multiplicar"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Multiplicar matrices 2×2 (fila por columna)",
                "prompt": "En el producto [[2, 1], [0, 3]] · [[4, 5], [1, 2]], la entrada superior izquierda es el producto punto de la Fila 1 [2, 1] con la Columna 1 [4, 1]. ¿Cuánto vale esa entrada? Respondé solo con el número.",
                "answer": "9: (2)(4) + (1)(1) = 8 + 1 = 9 (el producto completo da [[9, 12], [3, 6]]).",
                "hints": ["Calculá 2 × 4 + 1 × 1."],
                "payload": {
                    "lab_link": "math:vectors_matrices",
                    "check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Segunda entrada de un producto matricial 2×2",
                "prompt": "En el mismo producto [[2, 1], [0, 3]] · [[4, 5], [1, 2]], ¿cuánto vale la entrada superior derecha (Fila 1 [2, 1] · Columna 2 [5, 2])? Respondé solo con el número.",
                "answer": "12: (2)(5) + (1)(2) = 10 + 2 = 12.",
                "hints": ["Multiplicá Fila 1 [2, 1] por Columna 2 [5, 2]."],
                "payload": {
                    "lab_link": "math:vectors_matrices",
                    "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Aplicar una matriz de escala a un punto 2D",
                "prompt": "En gráficos 2D, la matriz [[2, 0], [0, 3]] transforma el punto (x, y) multiplicando el vector columna [4, 5]. ¿Cuál es la nueva coordenada y? Respondé solo con el número.",
                "answer": "15: Fila 2 [0, 3] · [4, 5] = 0(4) + 3(5) = 15 (duplica x a 8 y triplica y a 15).",
                "hints": ["Calculá 0(4) + 3(5)."],
                "payload": {"check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "El producto de matrices NO es conmutativo (AB ≠ BA)",
                "prompt": "Con números comunes siempre vale 3 × 5 = 5 × 3. ¿Es cierto en general que para dos matrices cuadradas A · B = B · A?",
                "answer": "No: el orden importa casi siempre (A · B ≠ B · A), porque aplicar una rotación y luego un estiramiento da distinto que al revés.",
                "hints": ["Pensá en matrices como transformaciones aplicadas en cadena (igual que composición de funciones)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "No, en general A · B ≠ B · A (el orden importa)",
                            "Sí, siempre da exactamente la misma matriz",
                            "Sí, siempre que sean 2 × 2",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "La matriz identidad I (el '1' de las matrices)",
                "prompt": "¿Cuál es la matriz identidad 2 × 2 tal que A · I = I · A = A para cualquier matriz A de 2 × 2?",
                "answer": "[[1, 0], [0, 1]]: unos en la diagonal principal y ceros en el resto (no es una matriz llena de unos!).",
                "hints": ["Unos en la diagonal principal y ceros fuera de ella."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "[[1, 0], [0, 1]]",
                            "[[1, 1], [1, 1]]",
                            "[[0, 1], [1, 0]]",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "pc-determinantes-inversas",
        "title": "73. Determinantes, matriz inversa 2×2 y sistemas AX = B",
        "level": 26,
        "order_index": 73,
        "summary": "Calcular det(A) = ad − bc, significado geométrico de área, matrices singulares (det = 0), inversa 2×2 y resolver sistemas.",
        "prerequisites": ["pc-matrices-operaciones"],
        "metadata": {"section": "Precálculo", "lab_tab": "vectors_matrices", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Calcular un determinante 2×2 (ad − bc)",
                "prompt": "Calculá el determinante de la matriz A = [[4, 2], [1, 3]] usando det(A) = a·d − b·c. Respondé solo con el número.",
                "answer": "10: (4)(3) − (2)(1) = 12 − 2 = 10.",
                "hints": ["Diagonal principal (4 × 3) menos la otra diagonal (2 × 1)."],
                "payload": {
                    "lab_link": "math:vectors_matrices",
                    "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Detectar una matriz singular (sin inversa)",
                "prompt": "Calculá el determinante de B = [[2, 4], [3, 6]]. Respondé solo con el número.",
                "answer": "0: (2)(6) − (4)(3) = 12 − 12 = 0. Como det = 0, B es singular y NO tiene matriz inversa (sus filas son proporcionales).",
                "hints": ["Hacé 2 × 6 − 4 × 3."],
                "payload": {
                    "lab_link": "math:vectors_matrices",
                    "check": {"type": "numeric", "value": 0, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Fórmula de la matriz inversa 2×2",
                "prompt": "Para A = [[5, 2], [2, 1]], el determinante vale det(A) = 5(1) − 2(2) = 1. Aplicando A⁻¹ = (1/det) · [[d, −b], [−c, a]], ¿cuál es A⁻¹?",
                "answer": "[[1, −2], [−2, 5]]: intercambiás los elementos de la diagonal principal (5 y 1) y cambiás el signo a la otra diagonal (−2 y −2).",
                "hints": ["Intercambiá a con d, negá b y c, y dividí por det = 1."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "[[1, −2], [−2, 5]]",
                            "[[5, −2], [−2, 1]]",
                            "[[1/5, 1/2], [1/2, 1]]",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Resolver un sistema AX = B multiplicando por A⁻¹",
                "prompt": "El sistema 5x + 2y = 9 y 2x + y = 4 se resuelve haciendo X = A⁻¹ · B = [[1, −2], [−2, 5]] · [9, 4]. ¿Cuánto vale x (Fila 1 · [9, 4])? Respondé solo con el número.",
                "answer": "1: x = 1(9) + (−2)(4) = 9 − 8 = 1 (y luego y = −2(9) + 5(4) = 2; verificación: 5(1)+2(2)=9).",
                "hints": ["Calculá 1 × 9 + (−2) × 4."],
                "payload": {"check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Significado geométrico del determinante",
                "prompt": "Una matriz 2 × 2 transforma un cuadrado de área 1 cm² en un paralelogramo. Si det(A) = 6, ¿qué área tiene la figura transformada?",
                "answer": "6 cm²: el valor absoluto del determinante |det(A)| es exactamente el factor de escala del área (y si det < 0, además voltea la orientación como un espejo).",
                "hints": ["El determinante mide cuánto agranda o achica las áreas la transformación."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "6 cm² (|det(A)| es el factor de área)",
                            "36 cm² (det²)",
                            "1 cm² (las matrices nunca cambian el área)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Qué pasa con un sistema AX = B cuando det(A) = 0",
                "prompt": "Al pasar un sistema 2 × 2 a forma matricial AX = B encontrás que det(A) = 0. ¿Qué significa para las soluciones del sistema?",
                "answer": "Que NO tiene una única solución: las dos rectas son paralelas (0 soluciones) o coincidentes (infinitas soluciones).",
                "hints": ["Si no existe A⁻¹, no podés despejar una única X = A⁻¹B."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "No tiene solución única (0 soluciones o infinitas soluciones)",
                            "Tiene solución única x = 0, y = 0",
                            "Siempre tiene exactamente 2 soluciones",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 27: COMBINATORIA, SERIES Y LÍMITES ====================
    {
        "slug": "pc-combinatoria-probabilidad",
        "title": "74. Combinatoria y probabilidad (permutaciones nPr y combinaciones nCr)",
        "level": 27,
        "order_index": 74,
        "summary": "Principio del conteo, factoriales, cuándo importa el orden (nPr) vs. cuándo no (nCr), probabilidad independiente y complemento.",
        "prerequisites": ["p-patrones-datos", "a2-polinomios-factorizacion"],
        "metadata": {"section": "Precálculo", "lab_tab": "combinatorics_series", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Principio fundamental del conteo (combinar atuendos)",
                "prompt": "Tenés 4 remeras, 3 pantalones y 2 pares de zapatillas. ¿Cuántos conjuntos diferentes podés armar? Respondé solo con el número.",
                "answer": "24 conjuntos: cuando las elecciones son independientes, las cantidades se multiplican → 4 × 3 × 2 = 24.",
                "hints": ["Multiplicá 4 × 3 × 2."],
                "payload": {
                    "lab_link": "math:combinatorics_series",
                    "check": {"type": "numeric", "value": 24, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Permutaciones nPr (el orden IMPORTA: podio)",
                "prompt": "5 atletas corren una final y se entregan oro, plata y bronce (importa el orden!). ¿Cuántos podios distintos existen (5P3 = 5 × 4 × 3)? Respondé solo con el número.",
                "answer": "60 podios: 5 opciones para oro × 4 restantes para plata × 3 restantes para bronce = 60.",
                "hints": ["Multiplicá 5 × 4 × 3."],
                "payload": {
                    "lab_link": "math:combinatorics_series",
                    "check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Combinaciones nCr (el orden NO importa: comité)",
                "prompt": "De un equipo de 5 personas elegís un comité de 3 (el orden NO importa). Dividiendo los 60 ordenamientos por 3! = 6, ¿cuántos comités distintos existen (5C3)? Respondé solo con el número.",
                "answer": "10 comités: 5C3 = (5 × 4 × 3) / (3 × 2 × 1) = 60 / 6 = 10.",
                "hints": ["Dividí 60 por 3! = 6."],
                "payload": {
                    "lab_link": "math:combinatorics_series",
                    "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Truco del complemento: 'al menos una cara'",
                "prompt": "Tirás dos monedas equilibradas. ¿Cuál es la probabilidad en decimal de sacar AL MENOS una cara? (Pista: 1 − P(dos cruces)). Respondé solo con el número.",
                "answer": "0.75 (3/4): la única forma de fallar es sacar dos cruces (0.5 × 0.5 = 0.25), así que 1 − 0.25 = 0.75.",
                "hints": ["Calculá 1 − (0.5 × 0.5)."],
                "payload": {"check": {"type": "numeric", "value": 0.75, "tolerance": 0.01, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Probabilidad de eventos independientes seguidos",
                "prompt": "Un sensor falla con probabilidad 0.10 cada día de manera independiente. Si instalás 2 sensores de respaldo en paralelo, ¿cuál es la probabilidad en decimal de que fallen AMBOS el mismo día (0.10 × 0.10)? Respondé solo con el número.",
                "answer": "0.01 (1%): para eventos independientes, P(A y B) = P(A) × P(B) = 0.10 × 0.10 = 0.01.",
                "hints": ["Multiplicá 0.10 × 0.10."],
                "payload": {"check": {"type": "numeric", "value": 0.01, "tolerance": 0.001, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Elegir permutación vs. combinación en la vida real",
                "prompt": "¿En cuál de estas situaciones el orden NO importa (corresponde usar combinaciones nCr)?",
                "answer": "Elegir 3 gustos de helado para poner en el mismo pote (chocolate-vainilla-frutilla es el mismo pote en cualquier orden).",
                "hints": ["Probá cambiar de orden los elementos elegidos: si el resultado sigue siendo idéntico, es combinación."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Elegir 3 gustos de helado para un mismo pote",
                            "Crear un PIN de 4 dígitos sin repetir",
                            "Asignar puestos de presidente, tesorero y secretario",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "pc-series-sigma",
        "title": "75. Notación sigma (∑), series y sumas infinitas",
        "level": 27,
        "order_index": 75,
        "summary": "Sumatorias ∑, truco de Gauss para series aritméticas, series geométricas finitas, sumas infinitas convergentes (|r| < 1) y Binomio.",
        "prerequisites": ["al-sucesiones", "pc-combinatoria-probabilidad"],
        "metadata": {"section": "Precálculo", "lab_tab": "combinatorics_series", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Evaluar una sumatoria en notación sigma",
                "prompt": "Calculá la suma ∑(2k + 1) desde k = 1 hasta k = 4 (es decir: 3 + 5 + 7 + 9). Respondé solo con el número.",
                "answer": "24: reemplazando k = 1, 2, 3, 4 obtenés 3 + 5 + 7 + 9 = 24.",
                "hints": ["Sumá 3 + 5 + 7 + 9 (son dos pares que suman 12)."],
                "payload": {
                    "lab_link": "math:combinatorics_series",
                    "check": {"type": "numeric", "value": 24, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Serie aritmética con el truco de Gauss",
                "prompt": "Usá la fórmula S_n = n · (a₁ + a_n) / 2 para sumar todos los enteros del 1 al 20 (1 + 2 + ... + 20). Respondé solo con el número.",
                "answer": "210: 20 × (1 + 20) / 2 = 10 × 21 = 210 (hay 10 parejas que suman 21 cada una).",
                "hints": ["Calculá 20 × 21 ÷ 2."],
                "payload": {
                    "lab_link": "math:combinatorics_series",
                    "check": {"type": "numeric", "value": 210, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Serie geométrica finita (duplicación de 5 pasos)",
                "prompt": "Calculá la suma 1 + 2 + 4 + 8 + 16 usando S_5 = a₁(1 − r⁵)/(1 − r) = (1 − 32)/(1 − 2). Respondé solo con el número.",
                "answer": "31: 1 + 2 + 4 + 8 + 16 = 31 (siempre 1 menos que la siguiente potencia de 2).",
                "hints": ["Calculá 32 − 1 (o sumá directo los 5 términos)."],
                "payload": {"check": {"type": "numeric", "value": 31, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Suma infinita de una serie geométrica convergente",
                "prompt": "Una pelota rebota recorriendo 12 m, luego 4 m, luego 4/3 m... (a₁ = 12, razón r = 1/3). Como |r| < 1, la suma infinita converge a S_∞ = a₁ / (1 − r). ¿Cuántos metros totales recorre? Respondé solo con el número.",
                "answer": "18 m: 12 / (1 − 1/3) = 12 / (2/3) = 12 × 3 / 2 = 18 m (infinitos rebotes suman una distancia finita!).",
                "hints": ["Dividí 12 por (1 − 1/3) = 2/3."],
                "payload": {
                    "lab_link": "math:combinatorics_series",
                    "check": {"type": "numeric", "value": 18, "tolerance": 0, "unit": "m"},
                },
            },
            {
                "item_type": "recall",
                "title": "Condición obligatoria para sumar una serie geométrica infinita",
                "prompt": "¿Cuándo converge a un número finito la serie geométrica infinita a₁ + a₁r + a₁r² + ... (para poder usar a₁ / (1 − r))?",
                "answer": "Únicamente cuando |r| < 1 (la razón está estrictamente entre −1 y 1, haciendo que los términos se achiquen hacia 0).",
                "hints": ["Si |r| ≥ 1 los términos nunca se achican hacia cero."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Solo cuando |r| < 1 (−1 < r < 1)",
                            "Para cualquier número r ≠ 1",
                            "Solo cuando r > 1",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Teorema del Binomio usando combinaciones nCr",
                "prompt": "Al expandir (x + y)⁴, el coeficiente de x²y² es 4C2 = (4 × 3) / 2. ¿Cuánto vale ese coeficiente? Respondé solo con el número.",
                "answer": "6: (x + y)⁴ = x⁴ + 4x³y + 6x²y² + 4xy³ + y⁴ (cada fila del Triángulo de Pascal son los números combinatorios nCr).",
                "hints": ["Calculá 4C2 = (4 × 3) ÷ 2."],
                "payload": {"check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    {
        "slug": "pc-limites-continuidad",
        "title": "76. Introducción a límites y continuidad (puente a Cálculo)",
        "level": 27,
        "order_index": 76,
        "summary": "Qué mide lim_{x→a} f(x), límites laterales, destrabar formas 0/0 factorizando y las 3 condiciones de continuidad.",
        "prerequisites": ["a2-racionales-asintotas", "pc-series-sigma"],
        "metadata": {"section": "Precálculo", "lab_tab": "limits_intro", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Límite por sustitución directa en función continua",
                "prompt": "Calculá lim(x → 3) de (x² + 2x − 1). Respondé solo con el número.",
                "answer": "14: como los polinomios son continuos en todas partes, basta sustituir x = 3 → 9 + 6 − 1 = 14.",
                "hints": ["Evaluá 3² + 2(3) − 1."],
                "payload": {
                    "lab_link": "math:limits_intro",
                    "check": {"type": "numeric", "value": 14, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Destrabar una indeterminación 0/0 (diferencia de cuadrados)",
                "prompt": "Si sustituís x = 4 en (x² − 16)/(x − 4) da 0/0 (agujero). Factorizando queda (x − 4)(x + 4)/(x − 4) = x + 4. ¿Cuánto vale el límite cuando x → 4? Respondé solo con el número.",
                "answer": "8: aunque en x = 4 exacto hay un agujero, al acercarse a 4 la altura tiende exactamente a 4 + 4 = 8.",
                "hints": ["Cancelá (x − 4) y evaluá x + 4 en x = 4."],
                "payload": {
                    "lab_link": "math:limits_intro",
                    "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Destrabar 0/0 factorizando un trinomio",
                "prompt": "Calculá lim(x → 2) de (x² − 5x + 6) / (x − 2) factorizando el numerador como (x − 2)(x − 3). Respondé solo con el número.",
                "answer": "−1: al cancelar (x − 2) queda x − 3, que al acercarse x → 2 vale 2 − 3 = −1.",
                "hints": ["Cancelá (x − 2) y sustituí x = 2 en lo que queda (x − 3)."],
                "payload": {
                    "lab_link": "math:limits_intro",
                    "check": {"type": "numeric", "value": -1, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Cuándo NO existe un límite (límites laterales distintos)",
                "prompt": "En una tarifa por tramos, al acercarte a x = 10 por la izquierda el costo tiende a $200, pero por la derecha tiende a $250. ¿Cuánto vale lim(x → 10) f(x)?",
                "answer": "No existe: para que el límite bilateral exista, los límites por izquierda y por derecha tienen que coincidir en el mismo número.",
                "hints": ["¿Llegan a la misma altura ambos lados del escalón?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "No existe (los límites laterales no coinciden)",
                            "225 (el promedio entre 200 y 250)",
                            "250 (el límite por derecha siempre gana)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Límite existente con agujero (continuidad vs. límite)",
                "prompt": "Una función tiene un agujero en x = 5, pero por ambos lados la curva se acerca suavemente a altura y = 7. ¿Existe el límite y es continua en x = 5?",
                "answer": "El límite SÍ existe (vale 7), pero la función NO es continua en x = 5 porque falta el punto f(5) = 7.",
                "hints": ["Al límite solo le importa el vecindario cercano; a la continuidad también le importa que el punto f(5) exista y coincida."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "El límite existe (= 7), pero NO es continua en x = 5",
                            "Ni existe el límite ni es continua",
                            "Es continua porque el límite existe",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Las 3 condiciones de continuidad en un punto x = a",
                "prompt": "Para que una función sea continua (sin levantar el lápiz) en x = a, ¿qué condición completa se debe cumplir?",
                "answer": "1) Existe f(a), 2) existe el límite cuando x → a, y 3) ambos valen exactamente lo mismo: lim_{x→a} f(x) = f(a).",
                "hints": ["No alcanza con que el límite exista ni con que f(a) exista por separado: tienen que coincidir."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Existe f(a), existe el límite en a y ambos son iguales",
                            "Solo que f(a) esté definido",
                            "Solo que los límites laterales sean finitos",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
]

PRECALCULUS_LESSONS: dict[str, dict] = {
    "pc-complejos-polares": {
        "hook": "Multiplicar `(1 + i)¹⁰` a mano lleva 10 páginas de distributivas; en forma polar con De Moivre se resuelve mentalmente en 3 segundos.",
        "concept": {
            "points": [
                "Todo complejo `z = a + bi` es un punto `(a, b)` en el plano complejo: en **forma polar** se describe por su radio **`r = √(a² + b²)`** y ángulo **`θ`** → **`z = r(cos θ + i·sen θ)`** (o abreviado `r∠θ`).",
                "**Magia de la forma polar**: al **multiplicar** dos complejos, **multiplicás sus radios y sumás sus ángulos** (`(r₁∠θ₁)(r₂∠θ₂) = (r₁r₂)∠(θ₁ + θ₂)`). Al dividir, dividís radios y restás ángulos.",
                "**Teorema de De Moivre**: para elevar a cualquier potencia `n`, **`(r∠θ)ⁿ = rⁿ∠(n·θ)`**. Y en forma rectangular, dividís complejos multiplicando arriba y abajo por el **conjugado** del denominador.",
            ],
            "real_world": [
                {
                    "title": "Fasores en ingeniería eléctrica (AC)",
                    "detail": "Voltajes y corrientes alternas se escriben en forma polar (`220∠0° V`, `5∠−30° A`) porque la Ley de Ohm `V = I · Z` se reduce a multiplicar magnitudes y sumar fases.",
                },
                {
                    "title": "Rotaciones en gráficos y robótica",
                    "detail": "Multiplicar cualquier punto `z` por `1∠θ` lo rota exactamente `θ` grados alrededor del origen sin cambiar su longitud.",
                },
                {
                    "title": "Procesamiento digital de señales (DSP)",
                    "detail": "Las raíces complejas de la unidad (`1∠(360°k/N)`) obtenidas por De Moivre son el corazón de la Transformada Rápida de Fourier (FFT) en MP3 y 5G.",
                },
            ],
            "key_rule": "Polar: z = r∠θ | Multiplicar: (r₁r₂)∠(θ₁+θ₂) | De Moivre: (r∠θ)ⁿ = rⁿ∠(nθ) | Dividir rect.: × conjugado.",
            "pitfall": "Sumar los módulos en vez de multiplicarlos al hacer `(3∠40°)(5∠25°)`: los módulos se MULTIPLICAN (`15`) y solo los ángulos se SUMAN (`65°`).",
        },
        "example": {
            "title": "Calcular (2∠30°)³ con De Moivre y dividir (2 + 6i)/(1 + i)",
            "steps": [
                "Aplicamos De Moivre: módulo `2³ = 8`, ángulo `3 × 30° = 90°` → `8∠90° = 8(cos 90° + i·sen 90°) = 8i`.",
                "Para dividir `(2 + 6i)/(1 + i)`: multiplicamos arriba y abajo por el conjugado `(1 − i)`.",
                "Arriba: `(2 + 6i)(1 − i) = 2 − 2i + 6i − 6i² = 8 + 4i`. Abajo: `1² + 1² = 2` → resultado `(8 + 4i)/2 = 4 + 2i`.",
            ],
            "lab_link": "math:complex_nums",
            "lab_cta": "Practicar números complejos en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto da el producto polar `(4∠20°) · (3∠50°)`?",
            "options": [
                {"text": "`12∠70°`", "ok": True, "feedback": "Exacto: 4 × 3 = 12 y 20° + 50° = 70°."},
                {"text": "`7∠70°`", "ok": False, "feedback": "Sumaste los módulos (4 + 3) en vez de multiplicarlos (4 × 3 = 12)."},
                {"text": "`12∠1000°`", "ok": False, "feedback": "Los ángulos se SUMAN (20° + 50°), no se multiplican."},
            ],
        },
        "checks": [
            {
                "question": "Usando De Moivre, ¿cuánto vale `(3∠45°)²`?",
                "options": [
                    {"text": "`9∠90°` (`= 9i`)", "ok": True, "feedback": "Exacto: 3² = 9 y 2 × 45° = 90°."},
                    {"text": "`6∠90°`", "ok": False, "feedback": "El módulo se eleva a la potencia n (3² = 9), no se multiplica por 2."},
                    {"text": "`9∠2025°`", "ok": False, "feedback": "El ángulo se multiplica por n (2 × 45° = 90°), no se eleva al cuadrado."},
                ],
            },
            {
                "question": "Al dividir `10 / (3 + i)`, ¿por qué expresión multiplicás numerador y denominador?",
                "options": [
                    {"text": "`(3 − i)` (el conjugado del denominador)", "ok": True, "feedback": "Exacto: (3 + i)(3 − i) = 10, que limpia por completo la i del denominador."},
                    {"text": "`(3 + i)`", "ok": False, "feedback": "(3 + i)² = 8 + 6i, sigue dejando la i en el denominador."},
                    {"text": "`(−3 − i)`", "ok": False, "feedback": "El conjugado solo cambia el signo de la parte imaginaria."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué le pasa gráficamente a un número complejo en el plano cuando lo multiplicás por otro complejo `r∠θ`.",
    },
    "pc-secciones-conicas": {
        "hook": "Las órbitas de los planetas, las antenas satelitales y los sistemas de localización por radar nacen todos de cortar el mismo cono en distintos ángulos.",
        "concept": {
            "points": [
                "**Elipse** `((x − h)² / a²) + ((y − k)² / b²) = 1`: óvalo cerrado con semiejes `a` y `b` (el denominador más grande indica el eje mayor). Sus **focos** están adentro, sobre el eje mayor, a distancia **`c = √(a² − b²)`** del centro (siempre denominador mayor menos denominador menor).",
                "**Hipérbola** `((x − h)² / a²) − ((y − k)² / b²) = 1`: dos ramas abiertas guiadas por **asíntotas** de pendiente `±b/a` (abre en el eje del término positivo). Sus **focos** están afuera a distancia **`c = √(a² + b²)`**.",
                "**Parábola geométrica** `(x − h)² = 4p(y − k)`: conjunto de puntos equidistantes de un **foco** (a distancia `p` adentro) y una recta **directriz** (a distancia `p` afuera).",
            ],
            "real_world": [
                {
                    "title": "Órbitas planetarias y cometas",
                    "detail": "Primera Ley de Kepler: cada planeta describe una elipse con el Sol en uno de sus focos; los cometas interestelares pasan en hipérbolas.",
                },
                {
                    "title": "Antenas parabólicas y reflectores",
                    "detail": "Cualquier señal paralela que golpea una parábola rebota directo al foco `(0, p)`; al revés, una lámpara en el foco proyecta un haz recto (faros de auto).",
                },
                {
                    "title": "Navegación hiperbólica y acústica",
                    "detail": "Si dos micrófonos miden una diferencia constante de tiempo de llegada de un sonido, la fuente está obligatoriamente sobre una hipérbola.",
                },
            ],
            "key_rule": "Elipse (+): c² = a² − b² | Hipérbola (−): c² = a² + b², asíntotas ±(b/a)x | Parábola: x² = 4py (foco en p).",
            "pitfall": "Cruzar la fórmula de `c²`: acordate que el signo en `c²` siempre es OPUESTO al signo de la ecuación (elipse tiene `+` → `c² = a² − b²`; hipérbola tiene `−` → `c² = a² + b²`).",
        },
        "example": {
            "title": "Comparar la elipse x²/25 + y²/9 = 1 y la hipérbola x²/9 − y²/16 = 1",
            "steps": [
                "En la elipse `x²/25 + y²/9 = 1`: `a = 5` (horizontal), `b = 3` (vertical), focos adentro en `c = √(25 − 9) = 4` → `(±4, 0)`.",
                "En la hipérbola `x²/9 − y²/16 = 1`: abre en X (`x²` es positivo), vértices `(±3, 0)`, asíntotas `y = ±(4/3)x`.",
                "Focos de la hipérbola (sumando denominadores): `c = √(9 + 16) = 5` → `(±5, 0)`.",
            ],
            "lab_link": "math:geometry_coords",
            "lab_cta": "Practicar coordenadas y cónicas en el Laboratorio",
        },
        "check": {
            "question": "¿A qué distancia `c` del centro está cada foco de la elipse `x²/100 + y²/36 = 1`?",
            "options": [
                {"text": "`8` (`√(100 − 36) = √64`)", "ok": True, "feedback": "Exacto: en la elipse se restan los denominadores a² − b² = 64 → c = 8."},
                {"text": "`10`", "ok": False, "feedback": "10 es el semieje mayor a, no la distancia c del centro al foco."},
                {"text": "`√136`", "ok": False, "feedback": "Sumar a² + b² corresponde a la hipérbola, no a la elipse."},
            ],
        },
        "checks": [
            {
                "question": "¿Qué sección cónica representa `9x² + 4y² = 36`?",
                "options": [
                    {"text": "Elipse (ambos cuadrados positivos pero coeficientes distintos)", "ok": True, "feedback": "Exacto: dividiendo por 36 queda x²/4 + y²/9 = 1 (elipse vertical)."},
                    {"text": "Círculo", "ok": False, "feedback": "Para ser círculo los coeficientes de x² e y² tendrían que ser iguales."},
                    {"text": "Hipérbola", "ok": False, "feedback": "La hipérbola tiene un signo más y un signo menos."},
                ],
            },
            {
                "question": "En la parábola `x² = 20y`, ¿dónde está ubicado su foco?",
                "options": [
                    {"text": "`(0, 5)` (`4p = 20 → p = 5`)", "ok": True, "feedback": "Exacto: al igualar 4p = 20 sale p = 5 en el eje vertical."},
                    {"text": "`(0, 20)`", "ok": False, "feedback": "Te faltó dividir 20 por 4 (la fórmula es x² = 4py)."},
                    {"text": "`(5, 0)`", "ok": False, "feedback": "Como x está al cuadrado, abre hacia arriba (eje Y), así que el foco está en (0, 5)."},
                ],
            },
        ],
        "takeaway_prompt": "Resumí en una regla corta cómo distinguir círculo, elipse, hipérbola y parábola desde su ecuación.",
    },
    "pc-vectores": {
        "hook": "Un vector guarda dirección y magnitud en un solo paquete `⟨x, y⟩`, y el producto punto te dice al instante cuánto apuntan dos vectores en la misma dirección.",
        "concept": {
            "points": [
                "Un vector **`v = ⟨v_x, v_y⟩`** se suma y escala componente a componente. Su **magnitud** es **`|v| = √(v_x² + v_y²)`** y su **vector unitario** (largo `1`, dirección pura) es **`u = v / |v|`**.",
                "Para convertir de forma polar (magnitud `|v|` y ángulo `θ`) a componentes usás **`v = ⟨|v|·cos θ, |v|·sen θ⟩`**.",
                "**Producto punto (escalar)**: **`u · v = u_x v_x + u_y v_y = |u||v|cos(θ)`**. Devuelve un NÚMERO: si da **`0`** son **perpendiculares (`90°`)**; positivo = ángulo agudo; negativo = ángulo obtuso.",
            ],
            "real_world": [
                {
                    "title": "Iluminación y shaders en videojuegos 3D",
                    "detail": "El brillo de cada píxel de un objeto 3D se calcula con `N · L` (producto punto entre la normal de la superficie y el vector hacia la luz).",
                },
                {
                    "title": "Trabajo mecánico en Física (`W = F · d`)",
                    "detail": "El trabajo de una fuerza es el producto punto entre fuerza y desplazamiento: si empujás perpendicular al movimiento (`90°`), `F · d = 0` (no realiza trabajo).",
                },
                {
                    "title": "Similitud de texto e inteligencia artificial (cosine similarity)",
                    "detail": "Los modelos de IA comparan significados calculando el producto punto entre vectores unitarios de palabras o documentos.",
                },
            ],
            "key_rule": "u · v = u_x·v_x + u_y·v_y = |u||v|cos(θ) | u · v = 0 ⇔ perpendiculares (90°) | Unitario: v / |v|.",
            "pitfall": "Creer que el producto punto `⟨2, 3⟩ · ⟨4, 5⟩` da un vector `⟨8, 15⟩`: NO, tenés que SUMAR esos productos (`8 + 15 = 23`, un solo número).",
        },
        "example": {
            "title": "Normalizar ⟨6, 8⟩ y probar si ⟨3, 4⟩ y ⟨−4, 3⟩ son perpendiculares",
            "steps": [
                "Magnitud de `⟨6, 8⟩`: `√(36 + 64) = 10` → vector unitario `⟨6/10, 8/10⟩ = ⟨0.6, 0.8⟩`.",
                "Producto punto `⟨3, 4⟩ · ⟨−4, 3⟩ = 3(−4) + 4(3) = −12 + 12 = 0`.",
                "Como el producto punto dio exactamente `0`, los dos vectores forman `90°` (son ortogonales).",
            ],
            "lab_link": "math:vectors_matrices",
            "lab_cta": "Practicar vectores y producto punto en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto vale el producto punto `⟨4, −2⟩ · ⟨3, 5⟩`?",
            "options": [
                {"text": "`2` (`12 − 10`)", "ok": True, "feedback": "Exacto: (4)(3) + (−2)(5) = 12 − 10 = 2."},
                {"text": "`⟨12, −10⟩`", "ok": False, "feedback": "Te faltó sumar las dos multiplicaciones: el producto punto es un solo número escalar."},
                {"text": "`22`", "ok": False, "feedback": "Cuidado con el signo de (−2)(5) = −10."},
            ],
        },
        "checks": [
            {
                "question": "¿Qué valor de `k` hace que `⟨2, 6⟩` y `⟨−3, k⟩` sean perpendiculares?",
                "options": [
                    {"text": "`k = 1` (`2(−3) + 6(1) = 0`)", "ok": True, "feedback": "Exacto: −6 + 6k = 0 → k = 1."},
                    {"text": "`k = −1`", "ok": False, "feedback": "Con −1 da −6 − 6 = −12 ≠ 0."},
                    {"text": "`k = 3`", "ok": False, "feedback": "Con 3 da −6 + 18 = 12 ≠ 0."},
                ],
            },
            {
                "question": "Si multiplicás un vector `v` por el escalar `−2`, ¿qué cambia?",
                "options": [
                    {"text": "Duplica su magnitud y apunta en sentido exactamente opuesto (`180°`)", "ok": True, "feedback": "Exacto: el 2 duplica el largo y el signo menos invierte el sentido."},
                    {"text": "Se rota `90°`", "ok": False, "feedback": "Multiplicar por un escalar real mantiene la misma recta (0° o 180°)."},
                    {"text": "Su magnitud se vuelve negativa", "ok": False, "feedback": "La magnitud (largo) siempre es ≥ 0."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué te dicen el valor `0`, positivo o negativo del producto punto `u · v` sobre el ángulo entre dos vectores.",
    },
    "pc-matrices-operaciones": {
        "hook": "Cada fotograma de un videojuego 3D y cada capa de una red neuronal son millones de multiplicaciones de matrices ocurriendo en paralelo.",
        "concept": {
            "points": [
                "Una matriz de **`m × n`** tiene `m` filas y `n` columnas. Para **sumar** matrices deben tener el mismo tamaño exacto (se suma entrada por entrada).",
                "**Producto matricial `A · B`**: solo existe si las columnas de `A` igualan las filas de `B` (`(m × n) · (n × p) = m × p`). Cada entrada `(fila i, col j)` es el **producto punto de la Fila `i` de `A` con la Columna `j` de `B`**.",
                "**Propiedad clave**: el producto de matrices **NO es conmutativo** (`A · B ≠ B · A`), porque las matrices representan transformaciones aplicadas una tras otra. La **matriz identidad `I`** (unos en diagonal, ceros fuera) actúa como el número `1`.",
            ],
            "real_world": [
                {
                    "title": "Gráficos 3D y GPUs",
                    "detail": "Rotar, escalar y proyectar un modelo 3D de 100 000 vértices a la pantalla se hace multiplicando todos los vértices por una sola matriz `4 × 4`.",
                },
                {
                    "title": "Redes neuronales e inteligencia artificial",
                    "detail": "Cada capa de un LLM transforma un vector de activaciones multiplicándolo por una matriz de pesos entrenados (`W · x + b`).",
                },
                {
                    "title": "Logística y costos de producción",
                    "detail": "Multiplicar una matriz de ingredientes por producto con una matriz de precios por proveedor calcula automáticamente todos los costos totales.",
                },
            ],
            "key_rule": "(m × n) · (n × p) = (m × p) | Entrada (i, j) = Fila i · Columna j | En general A · B ≠ B · A.",
            "pitfall": "Multiplicar matrices entrada por entrada como en la suma: el producto matricial siempre hace producto punto de **fila por columna**.",
        },
        "example": {
            "title": "Multiplicar [[2, 1], [0, 3]] · [[4, 5], [1, 2]]",
            "steps": [
                "Fila 1 `[2, 1]` con Col 1 `[4, 1]` → `2(4) + 1(1) = 9`; con Col 2 `[5, 2]` → `2(5) + 1(2) = 12`.",
                "Fila 2 `[0, 3]` con Col 1 `[4, 1]` → `0(4) + 3(1) = 3`; con Col 2 `[5, 2]` → `0(5) + 3(2) = 6`.",
                "Resultado: `[[9, 12], [3, 6]]`.",
            ],
            "lab_link": "math:vectors_matrices",
            "lab_cta": "Practicar matrices y determinantes en el Laboratorio",
        },
        "check": {
            "question": "Si `A` es de `3 × 2` y `B` es de `2 × 5`, ¿qué dimensión tiene `A · B`?",
            "options": [
                {"text": "`3 × 5`", "ok": True, "feedback": "Exacto: los internos coinciden (2 = 2) y quedan las dimensiones externas 3 × 5."},
                {"text": "`2 × 2`", "ok": False, "feedback": "El 2 del medio desaparece al hacer el producto punto; quedan 3 filas y 5 columnas."},
                {"text": "No existe", "ok": False, "feedback": "B · A (2×5 por 3×2) no existe, pero A · B sí."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuánto da `[[1, 2], [3, 0]] · [4, 1]^T`?",
                "options": [
                    {"text": "`[6, 12]^T` (`1(4)+2(1) = 6` y `3(4)+0(1) = 12`)", "ok": True, "feedback": "Exacto: cada fila hace producto punto con la columna [4, 1]."},
                    {"text": "`[4, 3]^T`", "ok": False, "feedback": "Multiplicaste entrada por entrada con la primera columna (`1·4` y `3·1`); hay que hacer fila por columna y sumar."},
                    {"text": "`[10, 8]^T`", "ok": False, "feedback": "Revisá: Fila 1 es 1(4) + 2(1) = 6 y Fila 2 es 3(4) + 0(1) = 12."},
                ],
            },
            {
                "question": "Si `I` es la matriz identidad `2 × 2` y `A` es cualquier matriz `2 × 2`, ¿cuánto da `I · A`?",
                "options": [
                    {"text": "La misma matriz `A` sin cambios", "ok": True, "feedback": "Exacto: I es el elemento neutro del producto matricial."},
                    {"text": "La matriz nula (todos ceros)", "ok": False, "feedback": "La identidad deja todo intacto, como multiplicar por 1."},
                    {"text": "Duplica todos los valores de `A`", "ok": False, "feedback": "Eso lo hace 2·I = [[2, 0], [0, 2]]."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en tus palabras cómo se calcula una entrada del producto `A · B` y por qué `A · B` no suele ser igual a `B · A`.",
    },
    "pc-determinantes-inversas": {
        "hook": "Para despejar `ax = b` dividís por `a` (si `a ≠ 0`). Con matrices no existe la división, pero existe la matriz inversa `A⁻¹`, siempre que el determinante no sea cero.",
        "concept": {
            "points": [
                "Para `A = [[a, b], [c, d]]`, su **determinante** es **`det(A) = ad − bc`**. Geométricamente, `|det(A)|` es el **factor por el que `A` multiplica las áreas** del plano.",
                "Si **`det(A) = 0`**, la matriz aplasta todo a una recta o punto (área 0): es **singular** y **NO tiene inversa** (no se puede deshacer!).",
                "Si **`det(A) ≠ 0`**, existe su inversa **`A⁻¹ = (1 / det(A)) · [[d, −b], [−c, a]]`** (cumple `A · A⁻¹ = I`). Así un sistema `AX = B` se resuelve de un saque haciendo **`X = A⁻¹ · B`**.",
            ],
            "real_world": [
                {
                    "title": "Resolver circuitos eléctricos y estructuras de 100 ecuaciones",
                    "detail": "Simuladores como SPICE o software de ingeniería escriben el sistema entero como `AX = B` y lo resuelven mediante álgebra matricial.",
                },
                {
                    "title": "Deshacer transformaciones en gráficos (ray casting)",
                    "detail": "Cuando hacés clic en un objeto 3D en pantalla, el motor usa la matriz inversa `M⁻¹` para volver de coordenadas de pantalla al espacio del mundo.",
                },
                {
                    "title": "Detectar datos redundantes en ciencia de datos",
                    "detail": "Un determinante igual a `0` avisa que una columna es combinación lineal de otra (multicolinealidad) y el sistema no tiene solución única.",
                },
            ],
            "key_rule": "det([[a,b],[c,d]]) = ad − bc | Inversa existe ⇔ det ≠ 0 | A⁻¹ = (1/det)[[d, −b], [−c, a]] | X = A⁻¹B.",
            "pitfall": "Intentar invertir una matriz invirtiendo cada número individual (`1/a`, `1/b`...) o olvidar cambiar los signos de `b` y `c`.",
        },
        "example": {
            "title": "Invertir A = [[5, 2], [2, 1]] y resolver 5x + 2y = 9, 2x + y = 4",
            "steps": [
                "Determinante: `det(A) = (5)(1) − (2)(2) = 5 − 4 = 1 ≠ 0` (sí es invertible!).",
                "Armamos `A⁻¹ = (1/1) · [[1, −2], [−2, 5]] = [[1, −2], [−2, 5]]`.",
                "Resolvemos `X = A⁻¹ · [9, 4]^T`: `x = 1(9) − 2(4) = 1`, `y = −2(9) + 5(4) = 2`.",
            ],
            "lab_link": "math:vectors_matrices",
            "lab_cta": "Practicar determinantes en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto vale el determinante de `[[3, 5], [2, 4]]`?",
            "options": [
                {"text": "`2` (`3·4 − 5·2 = 12 − 10`)", "ok": True, "feedback": "Exacto: diagonal principal menos la secundaria."},
                {"text": "`22`", "ok": False, "feedback": "Sumaste 12 + 10 en vez de restar ad − bc."},
                {"text": "`−2`", "ok": False, "feedback": "Restaste al revés (bc − ad)."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál de estas matrices NO tiene inversa (`det = 0`)?",
                "options": [
                    {"text": "`[[3, 6], [2, 4]]` (`12 − 12 = 0`)", "ok": True, "feedback": "Exacto: la segunda fila es 2/3 de la primera, así que det = 0."},
                    {"text": "`[[1, 0], [0, 1]]`", "ok": False, "feedback": "La identidad tiene det = 1 y es su propia inversa."},
                    {"text": "`[[2, 1], [1, 2]]`", "ok": False, "feedback": "Su determinante es 4 − 1 = 3 ≠ 0, sí tiene inversa."},
                ],
            },
            {
                "question": "Si `A · X = B` y conocés `A⁻¹`, ¿en qué orden debés multiplicar por `A⁻¹`?",
                "options": [
                    {"text": "`X = A⁻¹ · B` (por la izquierda, donde estaba `A`)", "ok": True, "feedback": "Exacto: multiplicar por la izquierda cancela A⁻¹·A = I dejando X = A⁻¹B."},
                    {"text": "`X = B · A⁻¹` (da lo mismo)", "ok": False, "feedback": "En matrices el orden importa (y B·A⁻¹ ni siquiera tiene dimensiones compatibles!)."},
                    {"text": "`X = B / det(A)`", "ok": False, "feedback": "Falta multiplicar por la matriz adjunta [[d, −b], [−c, a]]."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras qué revela `det(A) = 0` tanto geométricamente (áreas) como para un sistema de ecuaciones.",
    },
    "pc-combinatoria-probabilidad": {
        "hook": "Antes de calcular una probabilidad tenés que saber contar sin enumerar millones de casos a mano: la pregunta clave es una sola, '¿importa el orden?'.",
        "concept": {
            "points": [
                "**Principio fundamental del conteo**: si un paso tiene `a` opciones y otro independiente `b`, hay **`a × b`** resultados posibles. Ordenar `n` objetos distintos da **`n!`** (`n` factorial).",
                "**¿Importa el orden?** SÍ → **Permutaciones `nPr = n! / (n − r)!`** (podios, cargos distintos, un PIN sin repetir dígitos). NO → **Combinaciones `nCr = n! / (r!(n − r)!)`** (equipos, cartas, ingredientes: dividís por `r!` para borrar repeticiones de orden).",
                "**Probabilidad clave**: `P(A) = favorables / posibles`; eventos independientes → **`P(A y B) = P(A) · P(B)`**; truco de 'al menos uno' → **`P(al menos 1) = 1 − P(ninguno)`**.",
            ],
            "real_world": [
                {
                    "title": "Seguridad de contraseñas y claves",
                    "detail": "Una clave de 8 caracteres usando 62 símbolos tiene `62⁸ ≈ 218` billones de claves posibles (62 opciones por cada posición, porque se pueden repetir caracteres): cada carácter extra multiplica la seguridad ×62.",
                },
                {
                    "title": "Manos de póker y loterías (`nCr`)",
                    "detail": "Como el orden en que recibís 5 cartas no cambia tu mano, de un mazo de 52 cartas hay `52C5 = 2 598 960` manos posibles.",
                },
                {
                    "title": "Redundancia en servidores y aviones",
                    "detail": "Si un motor falla con probabilidad `0.001`, la probabilidad de que fallen 2 independientes a la vez cae a `0.001² = 0.000001` (uno en un millón).",
                },
            ],
            "key_rule": "Orden SÍ importa → nPr | Orden NO importa → nCr = nPr / r! | Independientes: × | Al menos uno: 1 − P(ninguno).",
            "pitfall": "Usar permutaciones cuando el orden no importa (contás el mismo equipo de 3 personas `3! = 6` veces repetido!).",
        },
        "example": {
            "title": "Comparar podio (5P3) vs. comité (5C3) con 5 personas",
            "steps": [
                "Para un podio de 3 puestos distintos (oro, plata, bronce), el orden IMPORTA: `5P3 = 5 × 4 × 3 = 60`.",
                "Para un comité de 3 personas sin cargos distintos, el orden NO importa: cada grupo aparece `3! = 6` veces en esos 60.",
                "Dividimos: `5C3 = 60 / 6 = 10` comités posibles.",
            ],
            "lab_link": "math:combinatorics_series",
            "lab_cta": "Practicar conteo y combinatoria en el Laboratorio",
        },
        "check": {
            "question": "¿De cuántas formas podés elegir `2` personas de un grupo de `6` para formar una pareja de trabajo (sin jerarquía)?",
            "options": [
                {"text": "`15` (`6C2 = (6 × 5) / 2`)", "ok": True, "feedback": "Exacto: el orden no importa, así que dividimos 30 por 2! = 2."},
                {"text": "`30` (`6P2 = 6 × 5`)", "ok": False, "feedback": "30 cuenta a (Ana, Luis) y (Luis, Ana) como dos parejas distintas."},
                {"text": "`12` (`6 × 2`)", "ok": False, "feedback": "No se multiplica n por r; se usa nCr = n(n − 1)/2."},
            ],
        },
        "checks": [
            {
                "question": "Tirás un dado de 6 caras dos veces. ¿Cuál es la probabilidad de sacar `6` las dos veces?",
                "options": [
                    {"text": "`1 / 36` (`(1/6) × (1/6)`)", "ok": True, "feedback": "Exacto: dos tiros independientes multiplican sus probabilidades."},
                    {"text": "`2 / 6` (`1/3`)", "ok": False, "feedback": "Sumar probabilidades da 'o' en eventos excluyentes, no 'y' en eventos seguidos."},
                    {"text": "`1 / 12`", "ok": False, "feedback": "Multiplicaste 6 × 2 en vez de 6 × 6."},
                ],
            },
            {
                "question": "Si la probabilidad de lluvia hoy es `0.3`, ¿cuál es la probabilidad de que NO llueva?",
                "options": [
                    {"text": "`0.7` (`1 − 0.3`)", "ok": True, "feedback": "Exacto: un evento y su complemento siempre suman 1 (100%)."},
                    {"text": "`0.3`", "ok": False, "feedback": "Solo son iguales si ambos valen 0.5."},
                    {"text": "`0.09`", "ok": False, "feedback": "0.09 sería probabilidad de lluvia dos días seguidos independientes."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con un ejemplo propio la diferencia entre permutación (`nPr`) y combinación (`nCr`).",
    },
    "pc-series-sigma": {
        "hook": "¿Cómo puede una suma de INFINITOS números positivos (`1 + 1/2 + 1/4 + 1/8 + ...`) dar exactamente `2` y nunca pasarse?",
        "concept": {
            "points": [
                "La **notación sigma `∑`** abrevia sumas largas: `∑_{k=1}^{n} a_k` evalúa la fórmula desde `k = 1` hasta `n` y suma todos los resultados.",
                "**Serie aritmética** (truco de Gauss): emparejás primero y último → **`S_n = n · (a₁ + a_n) / 2`**. **Serie geométrica finita**: **`S_n = a₁(1 − rⁿ) / (1 − r)`**.",
                "**Serie geométrica infinita**: solo si **`|r| < 1`** (los términos se achican a cero), la suma de infinitos términos converge a un valor exacto: **`S_∞ = a₁ / (1 − r)`**.",
            ],
            "real_world": [
                {
                    "title": "Dosis repetida de un medicamento (estado estacionario)",
                    "detail": "Si tomás `100 mg` diarios y cada día queda el `50%` del día anterior, el nivel acumulado en sangre nunca explota: converge a `100 / (1 − 0.5) = 200 mg`!",
                },
                {
                    "title": "Cuotas de un préstamo o hipoteca (anualidades)",
                    "detail": "El valor presente de todas las cuotas mensuales de un crédito es literalmente una serie geométrica finita.",
                },
                {
                    "title": "Decimales periódicos (`0.333... = 1/3`)",
                    "detail": "`0.333... = 0.3 + 0.03 + 0.003 + ...` es una serie geométrica con `a₁ = 0.3` y `r = 0.1` → `0.3 / 0.9 = 1/3` exacto.",
                },
            ],
            "key_rule": "Aritmética: n(a₁+a_n)/2 | Geom. finita: a₁(1−rⁿ)/(1−r) | Geom. infinita (|r|<1): a₁/(1−r).",
            "pitfall": "Aplicar `a₁ / (1 − r)` cuando `|r| ≥ 1`: si `r = 2`, `1 + 2 + 4 + 8 + ...` explota a `+∞` (diverge), nunca da `−1`.",
        },
        "example": {
            "title": "Sumar del 1 al 100 (Gauss) y calcular 10 + 5 + 2.5 + ...",
            "steps": [
                "Aritmética `1 + 2 + ... + 100`: `n = 100`, `a₁ = 1`, `a₁₀₀ = 100` → `S = 100 × 101 / 2 = 5050`.",
                "Geométrica infinita `10 + 5 + 2.5 + ...`: `a₁ = 10` y razón `r = 0.5` (cumple `|0.5| < 1`, converge!).",
                "Aplicamos `S_∞ = 10 / (1 − 0.5) = 10 / 0.5 = 20`.",
            ],
            "lab_link": "math:combinatorics_series",
            "lab_cta": "Practicar series y sumatorias en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es la suma infinita de `8 + 4 + 2 + 1 + 0.5 + ...` (`a₁ = 8`, `r = 0.5`)?",
            "options": [
                {"text": "`16` (`8 / (1 − 0.5)`)", "ok": True, "feedback": "Exacto: cada paso recorre la mitad de lo que faltaba para llegar a 16."},
                {"text": "`15.5`", "ok": False, "feedback": "15.5 es solo la suma de los primeros 5 términos mostrados; faltan infinitos términos más."},
                {"text": "Infinito (diverge)", "ok": False, "feedback": "Como |r| = 0.5 < 1, la suma sí converge a un número finito."},
            ],
        },
        "checks": [
            {
                "question": "Usando el truco de Gauss, ¿cuánto suman los enteros del `1` al `10` (`1 + 2 + ... + 10`)?",
                "options": [
                    {"text": "`55` (`10 × 11 / 2`)", "ok": True, "feedback": "Exacto: cinco parejas de 11 (1+10, 2+9, ..., 5+6) = 55."},
                    {"text": "`50`", "ok": False, "feedback": "Te olvidaste del +1 en (1 + 10 = 11)."},
                    {"text": "`110`", "ok": False, "feedback": "Te faltó dividir por 2."},
                ],
            },
            {
                "question": "¿Converge o diverge la serie geométrica infinita `3 + 4.5 + 6.75 + ...` (`r = 1.5`)?",
                "options": [
                    {"text": "Diverge (crece sin límite porque `|r| = 1.5 ≥ 1`)", "ok": True, "feedback": "Exacto: cada término es más grande que el anterior, así que la suma tiende a infinito."},
                    {"text": "Converge a `−6` (`3 / (1 − 1.5)`)", "ok": False, "feedback": "Trampa clásica: la fórmula a₁/(1 − r) es inválida cuando |r| ≥ 1."},
                    {"text": "Converge a `15`", "ok": False, "feedback": "Los términos nunca dejan de crecer."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con un ejemplo real (como dosis diaria o rebotes) por qué una suma de infinitos términos puede converger a un número finito.",
    },
    "pc-limites-continuidad": {
        "hook": "Cálculo entero (derivadas e integrales) nace de una sola idea brillante: preguntarse qué pasa cuando te acercás infinitamente a un punto SIN tener que pararte encima de él.",
        "concept": {
            "points": [
                "**Límite `lim_{x→a} f(x) = L`**: pregunta a qué altura `y` se acerca la curva cuando `x` se aproxima a `a` desde **ambos lados** (`a⁻` y `a⁺`). No importa si en `x = a` exacto hay un agujero!",
                "**Cómo calcular límites**: **1)** probá **sustitución directa**; **2)** si da **`0/0`** (indeterminación: todavía no sabés nada; en estos ejemplos esconde un agujero), **factorizá y cancelá** el factor `(x − a)` y volvé a sustituir; **3)** si izquierda y derecha tienden a valores distintos, el límite **NO existe**.",
                "**Continuidad en `x = a`** (dibujar sin levantar el lápiz): requiere tres cosas juntas: que **exista `f(a)`**, que **exista el límite**, y que **sean iguales (`lim_{x→a} f(x) = f(a)`)**.",
            ],
            "real_world": [
                {
                    "title": "Velocidad instantánea del velocímetro",
                    "detail": "La velocidad media `Δx / Δt` da `0/0` cuando `Δt = 0`; el límite cuando `Δt → 0` destraba `0/0` y define la velocidad exacta en un instante (la derivada!).",
                },
                {
                    "title": "Estabilidad y estado final de sistemas",
                    "detail": "El límite cuando `t → ∞` predice la velocidad terminal de un paracaidista o la temperatura final de un café enfriándose.",
                },
                {
                    "title": "Fallas por discontinuidad de salto",
                    "detail": "En ingeniería de control, un salto discontinuo en una señal de mando provoca picos bruscos que pueden dañar motores o válvulas.",
                },
            ],
            "key_rule": "Límite existe ⇔ izq. = der. | Forma 0/0 → factorizá y cancelá (x − a) | Continua ⇔ lim_{x→a} f(x) = f(a).",
            "pitfall": "Creer que `0/0` significa 'el límite vale 0' o 'no existe': `0/0` es solo una señal de que hay que simplificar algebraicamente para descubrir qué pasa de verdad (casi siempre aparece un valor finito; a veces el límite no existe).",
        },
        "example": {
            "title": "Resolver el límite 0/0: lim(x → 4) (x² − 16)/(x − 4)",
            "steps": [
                "Probamos sustitución directa: `(16 − 16)/(4 − 4) = 0/0` → hay un factor común oculto `(x − 4)`.",
                "Factorizamos el numerador: `(x − 4)(x + 4) / (x − 4)` y cancelamos `(x − 4)` (válido porque `x` se acerca a `4` sin ser `4`).",
                "Evaluamos lo que quedó (`x + 4`) en `x = 4`: el límite vale exactamente `8`!",
            ],
            "lab_link": "math:limits_intro",
            "lab_cta": "Practicar límites y formas 0/0 en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto vale `lim(x → 3) (x² − 9) / (x − 3)`?",
            "options": [
                {"text": "`6` (factorizando `(x − 3)(x + 3)/(x − 3) = x + 3`)", "ok": True, "feedback": "Exacto: al cancelar el factor 0/0 queda x + 3 → 3 + 3 = 6."},
                {"text": "`0`", "ok": False, "feedback": "0/0 no vale 0: hay que factorizar y cancelar (x − 3)."},
                {"text": "No existe", "ok": False, "feedback": "Hay un agujero en x = 3, pero el límite sí existe y vale 6."},
            ],
        },
        "checks": [
            {
                "question": "Si `lim(x → 2⁻) f(x) = 4` y `lim(x → 2⁺) f(x) = −1`, ¿qué concluís?",
                "options": [
                    {"text": "`lim(x → 2) f(x)` NO existe (discontinuidad de salto)", "ok": True, "feedback": "Exacto: izquierda y derecha deben apuntar al mismo valor."},
                    {"text": "El límite vale `4`", "ok": False, "feedback": "No puede ser 4 porque por la derecha se acerca a −1."},
                    {"text": "El límite vale `1.5`", "ok": False, "feedback": "Los límites nunca se promedian cuando hay un salto."},
                ],
            },
            {
                "question": "En `f(x)`, `lim(x → 5) f(x) = 10`, pero alguien definió `f(5) = 2` (un punto descolgado). ¿Es continua en `x = 5`?",
                "options": [
                    {"text": "No, porque el límite (`10`) no coincide con `f(5)` (`2`)", "ok": True, "feedback": "Exacto: falta la tercera condición de continuidad (lim = f(a))."},
                    {"text": "Sí, porque tanto el límite como `f(5)` existen", "ok": False, "feedback": "Además de existir ambos, tienen que valer exactamente lo mismo."},
                    {"text": "No existe el límite", "ok": False, "feedback": "El límite sí existe y vale 10 (al límite no le importa el punto descolgado)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué `0/0` en un límite no es un callejón sin salida y cuál es la diferencia entre que exista un límite y que la función sea continua.",
    },
}
