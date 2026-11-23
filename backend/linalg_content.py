"""Linear Algebra curriculum (7 units, #106-#112) adapted from Khan Academy.

Covers all 3 units of Khan Academy Linear Algebra building on Precálculo (#71-#73)
and Cálculo multivariable (#92):
  - Linear combinations, span, linear independence, subspaces & bases
  - Gaussian elimination (RREF), null space, column space & Rank-Nullity Theorem
  - Linear transformations as matrices, rotations, transposes & change of basis
  - Orthogonal complements, projections, orthonormal bases & orthogonal matrices
  - Gram-Schmidt orthonormalization (QR) & least squares regression (A^T A x = A^T b)
  - Eigenvalues & eigenvectors (Av = λv, det(A - λI) = 0, trace & determinant tricks)
  - Diagonalization (A = PDP⁻¹), fast matrix powers Aⁿ, Spectral Theorem, Markov & PCA
"""

from __future__ import annotations

LINALG_NODES: list[dict] = [
    # ==================== NIVEL 39: ESPACIOS, SUBESPACIOS Y TRANSFORMACIONES ====================
    {
        "slug": "la-espacios-independencia",
        "title": "106. Espacio generado (span), independencia lineal y bases",
        "level": 39,
        "order_index": 106,
        "summary": "Combinaciones lineales, qué genera un conjunto de vectores (span), independencia lineal, subespacios y dimensión.",
        "prerequisites": ["pc-vectores", "pc-determinantes-inversas"],
        "metadata": {"section": "Álgebra lineal", "lab_tab": "linear_algebra", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Calcular una combinación lineal c₁v₁ + c₂v₂",
                "prompt": "Calculá la combinación lineal 2·⟨1, 3⟩ + 3·⟨2, −1⟩. ¿Cuál es la primera componente (x) del vector resultante? Respondé solo con el número.",
                "answer": "8: 2(1) + 3(2) = 8 y 2(3) + 3(−1) = 3 → ⟨8, 3⟩.",
                "hints": ["Sumá las primeras componentes: 2(1) + 3(2)."],
                "payload": {"check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Detectar dependencia lineal usando el determinante",
                "prompt": "Dos vectores en ℝ², ⟨2, 3⟩ y ⟨6, k⟩, son linealmente DEPENDIENTES (apuntan en la misma recta) cuando el determinante 2k − 3(6) = 0. ¿Qué valor de k los vuelve dependientes? Respondé solo con el número.",
                "answer": "9: ⟨6, 9⟩ = 3 · ⟨2, 3⟩ (es simplemente un múltiplo redundante del primero!).",
                "hints": ["Despejá k de 2k − 18 = 0."],
                "payload": {
                    "lab_link": "math:linear_algebra",
                    "check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Por qué una recta que NO pasa por el origen NO es subespacio",
                "prompt": "¿Es un subespacio vectorial de ℝ² la recta y = 2x + 3?",
                "answer": "No: todo subespacio vectorial debe contener obligatoriamente al vector cero ⟨0, 0⟩ (y ser cerrado bajo sumas y escalares); aquí (0, 0) no cumple 0 = 3.",
                "hints": ["Probá sustituir el vector nulo (0, 0) en y = 2x + 3."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "No, porque no contiene al origen ⟨0, 0⟩",
                            "Sí, porque es una línea recta",
                            "Sí, porque tiene pendiente constante",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Cantidad exacta de vectores en cualquier base de ℝ³",
                "prompt": "¿Cuántos vectores linealmente independientes tiene EXACTAMENTE cualquier base del espacio 3D (ℝ³)? Respondé solo con el número.",
                "answer": "3 vectores: la dimensión de un espacio es igual al número de vectores en cualquiera de sus bases (2 no alcanzan; 4 siempre son redundantes).",
                "hints": ["La cantidad de vectores de una base siempre coincide con la dimensión."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Espacio generado (span) por dos vectores independientes en ℝ³",
                "prompt": "Tomás dos vectores linealmente independientes en ℝ³ (por ejemplo ⟨1, 0, 0⟩ y ⟨0, 1, 1⟩). ¿Qué figura geométrica forma su espacio generado (span)?",
                "answer": "Un plano que pasa por el origen (un subespacio de dimensión 2 dentro de ℝ³).",
                "hints": ["Dos direcciones independientes te permiten moverte en 2 dimensiones."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Un plano que pasa por el origen (dimensión 2)",
                            "Todo el espacio 3D (ℝ³)",
                            "Una sola recta (dimensión 1)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Definición exacta de base de un subespacio",
                "prompt": "¿Qué dos condiciones juntas convierten a un conjunto de vectores en una BASE de un subespacio W?",
                "answer": "1) Que genere (span) a todo W, y 2) que sea linealmente independiente (sin ningún vector sobrante).",
                "hints": ["Ni le faltan direcciones (genera) ni le sobran vectores repetidos (independiente)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Genera todo W y es linealmente independiente",
                            "Contiene al vector cero y tiene magnitud 1",
                            "Son todos múltiplos entre sí",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "la-nucleo-columna-rango",
        "title": "107. Eliminación gaussiana, espacio nulo, columna y rango",
        "level": 39,
        "order_index": 107,
        "summary": "Forma escalonada reducida (RREF), espacio columna Col(A), núcleo Nul(A) y el Teorema del Rango-Nulidad.",
        "prerequisites": ["la-espacios-independencia"],
        "metadata": {"section": "Álgebra lineal", "lab_tab": "linear_algebra", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Teorema del Rango-Nulidad (rango + nulidad = columnas)",
                "prompt": "Una matriz A de 4 × 7 (4 filas y 7 columnas) tiene rango igual a 3 (3 columnas pivote en RREF). Por el Teorema del Rango-Nulidad, ¿cuál es la dimensión de su espacio nulo (nulidad)? Respondé solo con el número.",
                "answer": "4: rango(A) + nulidad(A) = número de columnas (7) → 3 + nulidad = 7 → nulidad = 4 (4 variables libres!).",
                "hints": ["Restá el rango (3) a la cantidad de COLUMNAS (7)."],
                "payload": {
                    "lab_link": "math:linear_algebra",
                    "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Rango máximo posible de una matriz rectangular",
                "prompt": "¿Cuál es el MAYOR rango que podría llegar a tener una matriz de 3 × 5 (3 filas, 5 columnas)? Respondé solo con el número.",
                "answer": "3: como cada pivote ocupa una fila distinta, el rango nunca puede superar min(filas, columnas) = min(3, 5) = 3.",
                "hints": ["No puede haber más pivotes que filas (3) ni más que columnas (5)."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Leer el rango directamente en forma escalonada (RREF)",
                "prompt": "Tras eliminación gaussiana, una matriz queda [[1, 2, 0], [0, 0, 1], [0, 0, 0]]. ¿Cuál es su rango (cantidad de filas no nulas / pivotes)? Respondé solo con el número.",
                "answer": "2: hay 2 pivotes (en las columnas 1 y 3), así que dim(Col(A)) = rango = 2 y nulidad = 3 − 2 = 1.",
                "hints": ["Contá los 1 líderes (pivotes) en las filas no nulas."],
                "payload": {"check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Qué significa geométricamente el espacio columna Col(A)",
                "prompt": "Dada una matriz A y la ecuación Ax = b, ¿qué representa el espacio columna Col(A)?",
                "answer": "El conjunto exacto de todos los vectores salida b alcanzables (todos los b para los que Ax = b tiene al menos una solución).",
                "hints": ["Recordá que Ax es una combinación lineal de las columnas de A."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Todos los vectores b para los que Ax = b tiene solución (imagen de A)",
                            "Todos los vectores x que cumplen Ax = 0",
                            "El determinante de A",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Verificar qué vector vive en el espacio nulo Nul(A)",
                "prompt": "Para A = [[1, −2], [3, −6]], ¿cuál de estos vectores no nulos pertenece al espacio nulo Nul(A) (cumple Ax = 0)?",
                "answer": "⟨2, 1⟩: 1(2) − 2(1) = 0 y 3(2) − 6(1) = 0 (toda la recta t⟨2, 1⟩ se aplasta al origen!).",
                "hints": ["Probá multiplicar A por cada candidato hasta obtener ⟨0, 0⟩."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["⟨2, 1⟩", "⟨1, 2⟩", "⟨1, −2⟩"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Consecuencia de tener espacio nulo trivial (Nul(A) = {0})",
                "prompt": "Si el único vector que cumple Ax = 0 es x = 0 (nulidad = 0), ¿qué podés asegurar sobre las columnas de A?",
                "answer": "Que todas las columnas son linealmente independientes (y por tanto Ax = b nunca tiene infinitas soluciones: si existe, es única).",
                "hints": ["Si ninguna combinación no trivial de las columnas da 0, son independientes."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Sus columnas son linealmente independientes (solución única si existe)",
                            "Todas las columnas son cero",
                            "Siempre tiene infinitas soluciones",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "la-transformaciones-lineales",
        "title": "108. Transformaciones lineales, transpuesta y cambio de base",
        "level": 39,
        "order_index": 108,
        "summary": "Leer una matriz desde T(e₁) y T(e₂), matriz de rotación, propiedad (AB)ᵀ = BᵀAᵀ y cambiar de sistema de coordenadas (P⁻¹AP).",
        "prerequisites": ["la-nucleo-columna-rango", "pc-matrices-operaciones"],
        "metadata": {"section": "Álgebra lineal", "lab_tab": "linear_algebra", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Armar y aplicar una matriz desde T(e₁) y T(e₂)",
                "prompt": "Una transformación lineal T lleva e₁ = ⟨1, 0⟩ a ⟨3, 1⟩ y e₂ = ⟨0, 1⟩ a ⟨−2, 4⟩ (así A = [[3, −2], [1, 4]]). ¿Cuál es la primera coordenada x de T(⟨2, 1⟩)? Respondé solo con el número.",
                "answer": "4: T(⟨2, 1⟩) = 2⟨3, 1⟩ + 1⟨−2, 4⟩ = ⟨6 − 2, 2 + 4⟩ = ⟨4, 6⟩.",
                "hints": ["Calculá 2(3) + 1(−2)."],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Reconocer la matriz de rotación 90° antihoraria",
                "prompt": "Si rotás el plano 90° antihorario, e₁ = ⟨1, 0⟩ va a ⟨0, 1⟩ y e₂ = ⟨0, 1⟩ va a ⟨−1, 0⟩. ¿Qué matriz representa esa rotación?",
                "answer": "[[0, −1], [1, 0]]: la 1.ª columna es T(e₁) = [0, 1]ᵀ y la 2.ª columna es T(e₂) = [−1, 0]ᵀ.",
                "hints": ["Poné ⟨0, 1⟩ como primera columna y ⟨−1, 0⟩ como segunda columna."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "[[0, −1], [1, 0]]",
                            "[[0, 1], [−1, 0]]",
                            "[[−1, 0], [0, −1]]",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Test instantáneo de transformación NO lineal",
                "prompt": "¿Por qué la traslación T(x, y) = ⟨x + 5, y⟩ NO es una transformación lineal en ℝ²?",
                "answer": "Porque mueve el origen (T(0, 0) = ⟨5, 0⟩ ≠ ⟨0, 0⟩): toda transformación lineal fija obligatoriamente el origen y preserva sumas.",
                "hints": ["Evaluá T en el vector nulo ⟨0, 0⟩."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Porque no fija el origen: T(0, 0) ≠ ⟨0, 0⟩",
                            "Porque suma solo a la coordenada x",
                            "Sí es una transformación lineal",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Transpuesta de un producto de matrices (AB)ᵀ",
                "prompt": "Al trasponer un producto de matrices (intercambiar filas por columnas), ¿a qué equivale (A · B)ᵀ?",
                "answer": "Bᵀ · Aᵀ: igual que con inversas ((AB)⁻¹ = B⁻¹A⁻¹), el orden se invierte!",
                "hints": ["Regla de medias y zapatos: para deshacer/trasponer un producto se invierte el orden."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Bᵀ · Aᵀ", "Aᵀ · Bᵀ", "A · Bᵀ"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Coordenadas de un vector en una base alternativa B",
                "prompt": "Definimos una base nueva con b₁ = ⟨2, 0⟩ y b₂ = ⟨0, 3⟩. Si el vector estándar v = ⟨8, 15⟩ se escribe c₁b₁ + c₂b₂, ¿cuánto vale su primera coordenada c₁ en la base B? Respondé solo con el número.",
                "answer": "4: ⟨8, 15⟩ = 4⟨2, 0⟩ + 5⟨0, 3⟩, así que [v]_B = ⟨4, 5⟩.",
                "hints": ["¿Por cuánto multiplicás b₁ = ⟨2, 0⟩ para obtener 8 en x?"],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Fórmula de cambio de base de una transformación (P⁻¹AP)",
                "prompt": "Si P traduce coordenadas de la base nueva B a la estándar (v = P[v]_B) y A actúa en coordenadas estándar, ¿qué matriz representa la MISMA transformación escrita en la base B?",
                "answer": "P⁻¹ A P: primero P traduce a estándar, luego A aplica la transformación y por último P⁻¹ devuelve el resultado a la base B!",
                "hints": ["Leé las matrices de derecha a izquierda: B → estándar (P) → aplicar A → volver a B (P⁻¹)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["P⁻¹ A P", "P A P", "A P⁻¹"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 40: ORTOGONALIDAD, GRAM-SCHMIDT Y MÍNIMOS CUADRADOS ====================
    {
        "slug": "la-proyecciones-ortogonales",
        "title": "109. Proyecciones ortogonales, bases ortonormales y matrices Q",
        "level": 40,
        "order_index": 109,
        "summary": "Proyectar vectores sobre rectas y planos, complemento ortogonal W⊥, coordenadas sin sistemas y matrices ortogonales Qᵀ = Q⁻¹.",
        "prerequisites": ["la-transformaciones-lineales"],
        "metadata": {"section": "Álgebra lineal", "lab_tab": "linear_algebra", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Proyección ortogonal de un vector sobre una recta",
                "prompt": "Proyectá v = ⟨4, 6⟩ sobre la dirección u = ⟨1, 1⟩ usando proj_u(v) = [(v · u) / (u · u)] · u. ¿Cuál es la primera componente (x) del vector proyección? Respondé solo con el número.",
                "answer": "5: v · u = 10 y u · u = 2 → 10 / 2 = 5 → proj_u(v) = 5⟨1, 1⟩ = ⟨5, 5⟩ (el error ⟨−1, 1⟩ es perpendicular a ⟨1, 1⟩!).",
                "hints": ["Calculá (4 + 6) / (1 + 1) y multiplicalo por u = ⟨1, 1⟩."],
                "payload": {
                    "lab_link": "math:linear_algebra",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Coordenada en una base ortonormal (solo producto punto!)",
                "prompt": "En una base ortonormal {q₁, q₂}, la coordenada de v sobre q₁ es simplemente v · q₁. Si q₁ = ⟨0.6, 0.8⟩ (unitario) y v = ⟨10, 5⟩, ¿cuánto vale v · q₁? Respondé solo con el número.",
                "answer": "10: 10(0.6) + 5(0.8) = 6 + 4 = 10 (no hace falta resolver ningún sistema de ecuaciones!).",
                "hints": ["Calculá 10(0.6) + 5(0.8)."],
                "payload": {
                    "lab_link": "math:linear_algebra",
                    "check": {"type": "numeric", "value": 10, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Dimensión del complemento ortogonal W⊥",
                "prompt": "Dentro de ℝ⁵, un subespacio W tiene dimensión 2. Usando dim(W) + dim(W⊥) = n, ¿qué dimensión tiene su complemento ortogonal W⊥? Respondé solo con el número.",
                "answer": "3: 2 + 3 = 5 (cada vector de ℝ⁵ se descompone de forma única en una parte en W más una perpendicular en W⊥).",
                "hints": ["Restá dim(W) = 2 a la dimensión total n = 5."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Distancia más corta de un punto al plano XY",
                "prompt": "Proyectar ortogonalmente el punto ⟨3, −5, 7⟩ sobre el plano XY (z = 0) da ⟨3, −5, 0⟩. ¿Cuál es la distancia perpendicular más corta del punto al plano? Respondé solo con el número.",
                "answer": "7: el vector error es ⟨0, 0, 7⟩, cuya magnitud es 7 (la proyección ortogonal SIEMPRE encuentra el punto más cercano!).",
                "hints": ["Es la magnitud del componente perpendicular z."],
                "payload": {"check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Inversa instantánea de una matriz ortogonal Q",
                "prompt": "Una matriz cuadrada Q tiene columnas ortonormales (por ejemplo, una matriz de rotación en 3D), cumpliendo Qᵀ · Q = I. ¿Cuál es su inversa Q⁻¹?",
                "answer": "Q⁻¹ = Qᵀ (su simple transpuesta!): invertir una rotación 3D en un motor de videojuegos cuesta prácticamente cero operaciones.",
                "hints": ["Si Qᵀ · Q = I, ¿qué matriz multiplica a Q para dar la identidad I?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Q⁻¹ = Qᵀ (su transpuesta)", "Q⁻¹ = −Q", "Q⁻¹ = 2Q"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Qué propiedades geométricas conserva una matriz ortogonal Q",
                "prompt": "Cuando aplicás una matriz ortogonal Q (como rotación o reflexión) a todos los vectores del espacio, ¿qué propiedad se mantiene intacta?",
                "answer": "Todas las longitudes y todos los ángulos (|Qv| = |v| y (Qu)·(Qv) = u·v): es un movimiento rígido puro.",
                "hints": ["Rotar o espejar una figura 3D nunca la estira ni la deforma."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Conserva todas las longitudes y ángulos (|Qv| = |v|)",
                            "Duplica las longitudes",
                            "Aplasta el espacio a dimensión 1",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "la-gram-schmidt-minimos",
        "title": "110. Gram-Schmidt (QR) y mínimos cuadrados (AᵀAx̂ = Aᵀb)",
        "level": 40,
        "order_index": 110,
        "summary": "Enderezar cualquier base con Gram-Schmidt, factorización QR y resolver sistemas inconsistentes por mínimos cuadrados (regresión lineal).",
        "prerequisites": ["la-proyecciones-ortogonales"],
        "metadata": {"section": "Álgebra lineal", "lab_tab": "linear_algebra", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Un paso de Gram-Schmidt para ortogonalizar dos vectores",
                "prompt": "Empezás con v₁ = ⟨1, 1⟩ y v₂ = ⟨2, 6⟩. La proyección de v₂ sobre v₁ es 4⟨1, 1⟩ = ⟨4, 4⟩. Restando w₂ = v₂ − proj_{v₁}(v₂) obtenés un vector perpendicular a v₁. ¿Cuál es la coordenada y de w₂? Respondé solo con el número.",
                "answer": "2: w₂ = ⟨2 − 4, 6 − 4⟩ = ⟨−2, 2⟩ (chequeo de perpendicularidad: ⟨1, 1⟩ · ⟨−2, 2⟩ = −2 + 2 = 0!).",
                "hints": ["Calculá 6 − 4."],
                "payload": {
                    "lab_link": "math:linear_algebra",
                    "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Regresión lineal por mínimos cuadrados (AᵀA x̂ = Aᵀb)",
                "prompt": "Querés ajustar y = m·x a los puntos (1, 2) y (2, 5) (ninguna recta por el origen pasa por los dos: 2/1 ≠ 5/2!). Con A = [1, 2]ᵀ y b = [2, 5]ᵀ, resolvé la ecuación normal AᵀA·m = Aᵀb. ¿Cuánto vale la mejor pendiente m en decimal? Respondé solo con el número.",
                "answer": "2.4: AᵀA = 1² + 2² = 5 y Aᵀb = 1(2) + 2(5) = 12 → 5m = 12 → m = 2.4, que minimiza la suma de los errores cuadráticos (2.4 − 2)² + (4.8 − 5)²!",
                "hints": ["AᵀA = 1² + 2² y Aᵀb = 1(2) + 2(5).", "Queda 5m = 12; dividí 12 ÷ 5."],
                "payload": {
                    "lab_link": "math:linear_algebra",
                    "check": {"type": "numeric", "value": 2.4, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Gram-Schmidt simple sobre el eje X",
                "prompt": "Ortogonalizá v₂ = ⟨4, 3⟩ respecto de v₁ = ⟨1, 0⟩ restándole su proyección sobre v₁. ¿Cuál es la magnitud |w₂| del vector que queda (por la que hay que dividirlo para normalizarlo)? Respondé solo con el número.",
                "answer": "3: la proyección de v₂ sobre v₁ es su sombra horizontal ⟨4, 0⟩, así que w₂ = ⟨0, 3⟩ y |w₂| = 3. Gram-Schmidt primero resta la proyección para lograr 90° y al final divide por la magnitud para lograr largo 1 (q₂ = ⟨0, 1⟩).",
                "hints": ["La proyección de ⟨4, 3⟩ sobre el eje X es ⟨4, 0⟩; restala.", "¿Cuánto mide el vector ⟨0, 3⟩?"],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Ecuaciones normales de mínimos cuadrados",
                "prompt": "Cuando un sistema sobredeterminado Ax = b (más mediciones que incógnitas) NO tiene solución exacta, ¿qué ecuación matricial encuentra el x̂ que minimiza el error |Ax − b|²?",
                "answer": "Aᵀ A x̂ = Aᵀ b: exige que el vector error (b − Ax̂) sea perpendicular a todas las columnas de A (es decir Aᵀ(b − Ax̂) = 0!).",
                "hints": ["Multiplicá ambos lados de Ax = b por Aᵀ por la izquierda."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Aᵀ A x̂ = Aᵀ b", "A Aᵀ x̂ = b", "A⁻¹ b = x̂"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Intuición geométrica de mínimos cuadrados",
                "prompt": "Geométricamente, ¿qué es el vector predicho ŷ = A x̂ hallado por mínimos cuadrados respecto del vector de datos reales b?",
                "answer": "Es exactamente la proyección ortogonal de b sobre el espacio columna Col(A) (el punto de Col(A) más cercano posible a b!).",
                "hints": ["Buscás el vector dentro de Col(A) a mínima distancia euclidiana de b."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "La proyección ortogonal de b sobre Col(A)",
                            "Un vector perpendicular a Col(A)",
                            "El vector cero",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Qué matrices produce la factorización A = QR (Gram-Schmidt)",
                "prompt": "Al aplicar Gram-Schmidt a las columnas independientes de A se obtiene la factorización A = Q · R. ¿Qué tipo de matrices son Q y R?",
                "answer": "Q tiene columnas ortonormales (QᵀQ = I) y R es triangular superior (permite resolver mínimos cuadrados con Rx̂ = Qᵀb sin formar AᵀA!).",
                "hints": ["Q = 'orthogonal' (ortonormal) y R = 'right' (triangular superior)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Q con columnas ortonormales y R triangular superior",
                            "Ambas diagonales",
                            "Q simétrica y R con determinante 0",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 41: EIGENVALORES, EIGENVECTORES Y DIAGONALIZACIÓN ====================
    {
        "slug": "la-eigenvalores-eigenvectores",
        "title": "111. Valores propios (λ) y vectores propios (Av = λv)",
        "level": 41,
        "order_index": 111,
        "summary": "Direcciones invariantes bajo una matriz (Av = λv), polinomio característico det(A − λI) = 0, atajos de traza/determinante y autoespacios.",
        "prerequisites": ["la-transformaciones-lineales", "pc-determinantes-inversas"],
        "metadata": {"section": "Álgebra lineal", "lab_tab": "eigen_lab", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Leer un valor propio λ desde Av = λv",
                "prompt": "Para A = [[4, 1], [2, 3]], el vector v = ⟨1, 1⟩ es un vector propio. Calculá Av y respondé: ¿cuál es su valor propio (eigenvalor) λ en Av = λv? Respondé solo con el número.",
                "answer": "5: Av = ⟨4 + 1, 2 + 3⟩ = ⟨5, 5⟩ = 5 · ⟨1, 1⟩; el vector ⟨1, 1⟩ no rotó nada bajo A, solo se estiró exactamente por un factor λ = 5!",
                "hints": ["Multiplicá cada fila de A por ⟨1, 1⟩: (4 + 1) y (2 + 3).", "¿Por qué número se multiplicó ⟨1, 1⟩ para volverse ⟨5, 5⟩?"],
                "payload": {
                    "lab_link": "math:eigen_lab",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Atajo de la traza (λ₁ + λ₂ = a + d) para hallar el segundo eigenvalor",
                "prompt": "En toda matriz 2×2, la suma de los eigenvalores es SIEMPRE igual a la traza (suma de la diagonal). En A = [[4, 1], [2, 3]] la traza es 4 + 3 = 7 y ya sabés que λ₁ = 5. ¿Cuánto vale el otro eigenvalor λ₂? Respondé solo con el número.",
                "answer": "2: λ₁ + λ₂ = 7 → λ₂ = 2 (verificación por determinante: det(A) = 12 − 2 = 10 = 5 × 2!).",
                "hints": ["Restale 5 a la traza (4 + 3 = 7)."],
                "payload": {
                    "lab_link": "math:eigen_lab",
                    "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Eigenvalores instantáneos de una matriz triangular",
                "prompt": "Los eigenvalores de cualquier matriz triangular (o diagonal) son directamente los números de su diagonal principal. ¿Cuál es el MAYOR eigenvalor de [[6, 9], [0, −2]]? Respondé solo con el número.",
                "answer": "6 (sus eigenvalores son 6 y −2, sin necesidad de expandir nada!).",
                "hints": ["Leé los dos elementos de la diagonal principal y elegí el mayor."],
                "payload": {
                    "lab_link": "math:eigen_lab",
                    "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Ecuación característica det(A − λI) = 0",
                "prompt": "¿Por qué para hallar los valores propios λ resolvemos obligatoriamente det(A − λI) = 0?",
                "answer": "Porque Av = λv equivale a (A − λI)v = 0, y para que exista un eigenvector v ≠ 0 la matriz (A − λI) debe ser singular (determinante 0).",
                "hints": ["Si det(A − λI) ≠ 0, la única solución sería v = 0, que no sirve como eigenvector."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Para que (A − λI)v = 0 tenga soluciones no nulas (v ≠ 0)",
                            "Porque todo eigenvector es el vector cero",
                            "Para forzar que det(A) = 0 siempre",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Relación entre λ = 0 y matriz invertible",
                "prompt": "Si descubrís que λ = 0 es un valor propio de una matriz cuadrada A, ¿puede A tener matriz inversa?",
                "answer": "NO: si λ = 0 es eigenvalor existe v ≠ 0 con Av = 0, lo que significa que det(A) = λ₁·λ₂·... = 0 (A es singular, no invertible).",
                "hints": ["Recordá que det(A) es igual al producto de todos los eigenvalores."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "No, porque det(A) = 0 (es singular y aplasta v al cero)",
                            "Sí, siempre que los otros eigenvalores no sean 0",
                            "Sí, y su inversa tiene eigenvalor 0",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Por qué una rotación 90° en ℝ² no tiene eigenvalores reales",
                "prompt": "La matriz de rotación 90° [[0, −1], [1, 0]] tiene ecuación característica λ² + 1 = 0 (raíces ±i). Geométricamente, ¿por qué no tiene eigenvectores reales?",
                "answer": "Porque gira 90° a TODOS los vectores del plano: ninguno permanece sobre su propia recta (ningún vector no nulo se estira sin girar).",
                "hints": ["Pensá si alguna flecha del plano queda apuntando en su misma recta tras girar 90°."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Porque gira todos los vectores 90° y ninguna recta queda invariante",
                            "Porque su determinante es 0",
                            "Porque solo tiene un eigenvalor igual a 1",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "la-diagonalizacion-aplicaciones",
        "title": "112. Diagonalización (A = PDP⁻¹), potencias Aⁿ, Markov y PCA",
        "level": 41,
        "order_index": 112,
        "summary": "Descomponer A = PDP⁻¹ en base de eigenvectores, calcular Aⁿ al instante, Teorema Espectral, cadenas de Markov/PageRank y PCA.",
        "prerequisites": ["la-eigenvalores-eigenvectores", "la-proyecciones-ortogonales"],
        "metadata": {"section": "Álgebra lineal", "lab_tab": "eigen_lab", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Elevar una matriz diagonal a una potencia (D⁴)",
                "prompt": "Para la matriz diagonal D = [[2, 0], [0, 3]], elevarla a la cuarta potencia simplemente eleva cada elemento de la diagonal: D⁴ = [[2⁴, 0], [0, 3⁴]]. ¿Cuánto vale la entrada inferior derecha de D⁴? Respondé solo con el número.",
                "answer": "81: 3⁴ = 81 (así es como diagonalizar convierte multiplicar matrices 100 veces en elevar simples números!).",
                "hints": ["Calculá 3⁴."],
                "payload": {
                    "lab_link": "math:eigen_lab",
                    "check": {"type": "numeric", "value": 81, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Cómo acelerar A¹⁰⁰ usando A = P D P⁻¹",
                "prompt": "Si una matriz se diagonaliza como A = P D P⁻¹, ¿a qué se simplifica A¹⁰⁰?",
                "answer": "P · D¹⁰⁰ · P⁻¹: al multiplicar 100 copias de (P D P⁻¹), todos los pares internos P⁻¹·P se cancelan en la identidad I!",
                "hints": ["Probá con A² = (P D P⁻¹)(P D P⁻¹) = P D (P⁻¹P) D P⁻¹ = P D² P⁻¹."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "P · D¹⁰⁰ · P⁻¹",
                            "P¹⁰⁰ · D¹⁰⁰ · (P⁻¹)¹⁰⁰",
                            "100 · P D P⁻¹",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Qué contiene P y qué contiene D en A = P D P⁻¹",
                "prompt": "Para armar la diagonalización A = P D P⁻¹ de una matriz n × n diagonalizable, ¿cómo se construyen P y D?",
                "answer": "Las columnas de P son n eigenvectores linealmente independientes y la diagonal de D contiene sus eigenvalores correspondientes en el mismo orden.",
                "hints": ["A·P = P·D dice columna por columna que A·v_i = λ_i·v_i."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Columnas de P = eigenvectores independientes; diagonal de D = eigenvalores en igual orden",
                            "Columnas de P = eigenvalores; D = matriz identidad",
                            "P = Aᵀ y D = det(A)·I",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Teorema Espectral para matrices simétricas (A = Aᵀ)",
                "prompt": "¿Qué propiedad extraordinaria garantiza el Teorema Espectral para TODA matriz simétrica real (A = Aᵀ, como las matrices de covarianza o inercia)?",
                "answer": "Siempre tiene eigenvalores reales y se puede diagonalizar con una base ORTONORMAL de eigenvectores: A = Q D Qᵀ!",
                "hints": ["Nunca salen raíces complejas y los eigenvectores de distintos λ son siempre perpendiculares (90°)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Eigenvalores siempre reales y eigenvectores ortogonales (A = Q D Qᵀ)",
                            "Siempre tiene determinante igual a 1",
                            "Nunca es diagonalizable",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Estado estacionario de una cadena de Markov / Google PageRank",
                "prompt": "En una cadena de Markov (matriz de transición P donde cada columna suma 1), el estado estacionario de equilibrio a largo plazo cumple P·v = v. ¿A qué valor propio λ corresponde SIEMPRE ese vector de equilibrio? Respondé solo con el número.",
                "answer": "1: P·v = 1·v (así calculó el algoritmo original PageRank de Google la importancia de todas las páginas de Internet!).",
                "hints": ["Compará P·v = v con P·v = λ·v."],
                "payload": {"check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Cómo usa PCA (ciencia de datos e IA) los eigenvectores",
                "prompt": "El Análisis de Componentes Principales (PCA) busca reducir un dataset de 100 columnas a solo 2 o 3 ejes que conserven la mayor información. ¿Qué ejes elige PCA?",
                "answer": "Los eigenvectores de la matriz de covarianza asociados a los MAYORES eigenvalores (las direcciones donde los datos tienen mayor varianza).",
                "hints": ["Cada eigenvalor de la matriz de covarianza mide cuánta varianza hay en la dirección de su eigenvector."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Los eigenvectores de la matriz de covarianza con los mayores eigenvalores",
                            "Los vectores del espacio nulo (λ = 0)",
                            "Las dos primeras columnas originales sin transformar",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
]

LINALG_LESSONS: dict[str, dict] = {
    "la-espacios-independencia": {
        "hook": "Toda el Álgebra Lineal gira en torno a dos preguntas sencillas: ¿a qué lugares podés llegar combinando tus vectores (`span`) y alguno de ellos está sobrando (`dependencia`)?",
        "concept": {
            "points": [
                "Una **combinación lineal** `c₁v₁ + c₂v₂ + ...` es cualquier punto que alcanzás escalando y sumando tus vectores. El conjunto de todos los puntos alcanzables se llama **espacio generado (`span`)**.",
                "Un conjunto es **linealmente independiente** si ningún vector es combinación de los otros (ninguno sobra; la única forma de sumar `0` es con todos los `c_i = 0`). Si sobra alguno, es **dependiente** (en `2×2`, `det = 0`).",
                "Un **subespacio `W`** (rectas/planos que **pasan por el origen `0`** y son cerrados bajo suma y escalar) tiene una **base**: un conjunto mínimo que genera todo `W` sin vectores redundantes. El número de vectores de esa base es la **dimensión**.",
            ],
            "real_world": [
                {
                    "title": "Colores RGB en tu pantalla (base de dimensión 3)",
                    "detail": "Rojo, Verde y Azul son 3 vectores independientes: cualquier color visible en pantalla es una combinación lineal `r·R + g·G + b·B` en su `span`.",
                },
                {
                    "title": "Compresión y eliminación de datos redundantes",
                    "detail": "Si en una tabla de sensores una columna es combinación lineal de otras dos, es linealmente dependiente y puede eliminarse sin perder información.",
                },
                {
                    "title": "Grados de libertad en robótica",
                    "detail": "Para que un dron o brazo alcance cualquier punto de un espacio 3D necesita al menos 3 direcciones independientes de empuje (dimensión 3).",
                },
            ],
            "key_rule": "Subespacio: contiene al 0 + cerrado en suma y escalar | Base = genera (span) + independiente | Dimensión = # de vectores de la base.",
            "pitfall": "Creer que 4 vectores en `ℝ³` pueden ser linealmente independientes: ¡imposible! En `ℝⁿ`, cualquier grupo de más de `n` vectores es SIEMPRE linealmente dependiente.",
        },
        "example": {
            "title": "Probar independencia lineal en ℝ² y chequear subespacios",
            "steps": [
                "¿Son independientes `⟨2, 3⟩` y `⟨6, 9⟩`? Calculamos `det([[2, 6], [3, 9]]) = 18 − 18 = 0` → **dependientes** (`⟨6, 9⟩ = 3⟨2, 3⟩`).",
                "¿Son independientes `⟨2, 3⟩` y `⟨1, 4⟩`? `det = 8 − 3 = 5 ≠ 0` → **independientes**, forman una **base de `ℝ²`**!",
                "La recta `y = 2x` pasa por `(0, 0)` → SÍ es subespacio (base `{⟨1, 2⟩}`, dim `1`). La recta `y = 2x + 3` no pasa por `(0, 0)` → NO es subespacio.",
            ],
            "lab_link": "math:linear_algebra",
            "lab_cta": "Practicar Álgebra lineal en el Laboratorio",
        },
        "check": {
            "question": "¿Pueden `2` vectores solos formar una base de todo `ℝ³`?",
            "options": [
                {"text": "No: solo generan como máximo un plano (dimensión `2`), nunca alcanzan todo `ℝ³`", "ok": True, "feedback": "Exacto: toda base de ℝ³ necesita exactamente 3 vectores independientes."},
                {"text": "Sí, si son perpendiculares entre sí", "ok": False, "feedback": "Dos vectores perpendiculares en 3D solo abarcan un plano, les falta la tercera dimensión."},
                {"text": "Sí, si son suficientemente largos", "ok": False, "feedback": "El largo no cambia el span porque los escalares c₁, c₂ ya pueden ser tan grandes como quieras."},
            ],
        },
        "checks": [
            {
                "question": "Si un conjunto de vectores incluye al vector cero `⟨0, 0, 0⟩`, ¿es linealmente independiente o dependiente?",
                "options": [
                    {"text": "Siempre **dependiente** (podés multiplicar al cero por `5` y al resto por `0`, sumando cero sin ser todos ceros!)", "ok": True, "feedback": "Exacto: el vector cero no aporta ninguna dirección nueva."},
                    {"text": "Independiente, porque no es múltiplo de nadie", "ok": False, "feedback": "El vector cero ES 0 veces cualquier otro vector!"},
                    {"text": "Depende de los otros vectores", "ok": False, "feedback": "Cualquier conjunto que contenga al vector nulo es automáticamente dependiente."},
                ],
            },
            {
                "question": "¿Cuál de estos conjuntos SÍ es un subespacio vectorial de `ℝ²`?",
                "options": [
                    {"text": "Todos los puntos de la recta `y = −3x`", "ok": True, "feedback": "Exacto: pasa por (0, 0) y sumar o escalar múltiplos de ⟨1, −3⟩ siempre queda en la misma recta."},
                    {"text": "El primer cuadrante (`x ≥ 0, y ≥ 0`)", "ok": False, "feedback": "Falla el cierre por escalares negativos: −1 · ⟨1, 1⟩ = ⟨−1, −1⟩ se sale del primer cuadrante."},
                    {"text": "El círculo `x² + y² = 1`", "ok": False, "feedback": "No contiene al origen (0, 0) ni es cerrado bajo suma."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en una frase qué relación hay entre espacio generado (`span`), independencia lineal y base.",
    },
    "la-nucleo-columna-rango": {
        "hook": "Toda matriz `A` divide el universo de entrada en dos mundos complementarios: las direcciones que sobreviven (`rango`) y las direcciones que aplasta a cero (`nulidad`) — y ambos siempre suman el total de columnas.",
        "concept": {
            "points": [
                "**Eliminación gaussiana (RREF)**: reducir una matriz por operaciones elementales de fila revela cuántos **pivotes** tiene (**rango `r`**) y cuántas **variables libres** sobran (**nulidad**).",
                "**Espacio columna `Col(A)`**: es el span de las columnas de `A` (todos los resultados `b` alcanzables por `Ax = b`). Su dimensión es el **rango**, y su base son las columnas pivote de la matriz ORIGINAL `A`.",
                "**Espacio nulo `Nul(A)`**: todos los `x` que van a cero (`Ax = 0`). **Teorema del Rango-Nulidad**: **`rango(A) + nulidad(A) = n`** (cantidad de columnas de `A`!).",
            ],
            "real_world": [
                {
                    "title": "Proyección 3D a pantalla 2D (espacio nulo = línea de visión)",
                    "detail": "Una cámara proyecta `ℝ³ → ℝ²` (`rango = 2`, `n = 3`): por Rango-Nulidad, su núcleo tiene dimensión `1` (toda la línea de profundidad hacia el lente colapsa en un solo píxel!).",
                },
                {
                    "title": "Códigos correctores de errores (matriz de paridad)",
                    "detail": "Los mensajes válidos en comunicaciones digitales son exactamente el espacio nulo `H·x = 0` de una matriz de paridad `H`: si `H·x ≠ 0`, ¡hubo un bit corrupto!",
                },
                {
                    "title": "Compresión de imágenes de bajo rango",
                    "detail": "Una imagen de `1000 × 1000` puede aproximarse muy bien con una matriz de `rango = 30`, guardando menos del 10% de los datos.",
                },
            ],
            "key_rule": "rango(A) = # pivotes = dim(Col(A)) | nulidad(A) = # variables libres = dim(Nul(A)) | rango + nulidad = # columnas.",
            "pitfall": "Sumar `rango + nulidad = filas` en vez de `= columnas`! Acordate siempre: las variables `x` en `Ax` corresponden a las **columnas** de `A`.",
        },
        "example": {
            "title": "Aplicar Rango-Nulidad a A = [[1, −2, 3], [2, −4, 6]]",
            "steps": [
                "La fila 2 es el doble de la fila 1 → al hacer `F₂ − 2F₁` queda RREF: `[[1, −2, 3], [0, 0, 0]]`.",
                "Hay **1 solo pivote** (columna 1) → **`rango(A) = 1`** (`Col(A)` es la recta generada por `⟨1, 2⟩`).",
                "Como tiene `n = 3` columnas, por Rango-Nulidad: **`nulidad(A) = 3 − 1 = 2`** (hay 2 variables libres `x₂, x₃`, así que `Nul(A)` es un plano en `ℝ³`!).",
            ],
            "lab_link": "math:linear_algebra",
            "lab_cta": "Practicar rango y nulidad en el Laboratorio",
        },
        "check": {
            "question": "Una matriz `A` de `5 × 8` tiene `nulidad(A) = 5`. ¿Cuál es su rango?",
            "options": [
                {"text": "`3` (`rango + 5 = 8` columnas)", "ok": True, "feedback": "Exacto: 3 + 5 = 8."},
                {"text": "`0` (`5 − 5`)", "ok": False, "feedback": "Usaste el número de filas (5) en vez del número de columnas (8)!"},
                {"text": "`5`", "ok": False, "feedback": "5 es la nulidad; el rango es columnas − nulidad = 8 − 5 = 3."},
            ],
        },
        "checks": [
            {
                "question": "Si una matriz cuadrada `4 × 4` es invertible (`det ≠ 0`), ¿cuáles son su rango y su nulidad?",
                "options": [
                    {"text": "`rango = 4` y `nulidad = 0`", "ok": True, "feedback": "Exacto: alcanza todo ℝ⁴ y nada no nulo se aplasta al origen."},
                    {"text": "`rango = 0` y `nulidad = 4`", "ok": False, "feedback": "Eso es la matriz nula llena de ceros."},
                    {"text": "`rango = 2` y `nulidad = 2`", "ok": False, "feedback": "Si nulidad > 0, no es invertible (det = 0)."},
                ],
            },
            {
                "question": "Si una matriz de `3 × 3` tiene `rango = 2`, ¿qué figura geométrica es su espacio nulo `Nul(A)`?",
                "options": [
                    {"text": "Una recta pasando por el origen (`dim = 3 − 2 = 1`)", "ok": True, "feedback": "Exacto: nulidad 1 = una recta de vectores que van a 0."},
                    {"text": "Un plano (`dim = 2`)", "ok": False, "feedback": "El plano es su espacio columna Col(A) (dim 2); el núcleo tiene dim 3 − 2 = 1."},
                    {"text": "Solo el punto `⟨0, 0, 0⟩`", "ok": False, "feedback": "Eso ocurre solo cuando rango = 3 (nulidad = 0)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá el Teorema del Rango-Nulidad con el ejemplo de una cámara proyectando el espacio 3D sobre una foto 2D.",
    },
    "la-transformaciones-lineales": {
        "hook": "Dejá de ver una matriz como una tabla aburrida de números: sus columnas son literalmente las fotos de dónde aterrizan los ejes `e₁` y `e₂` cuando deformás el espacio.",
        "concept": {
            "points": [
                "Una función `T` es **lineal** si `T(u + v) = T(u) + T(v)` y `T(cv) = cT(v)`: geométricamente, **fija el origen** y mantiene todas las rectas rectas y paralelas (sin curvar!).",
                "**El secreto maestro de las matrices**: las columnas de la matriz de `T` son simplemente **`[ T(e₁) | T(e₂) | ... ]`**. Para rotar un ángulo `θ`: **`R_θ = [[cos θ, −sen θ], [sen θ, cos θ]]`**.",
                "**Transpuesta y Cambio de base**: `(AB)ᵀ = BᵀAᵀ`. Y si mirás la transformación `A` desde otra base cuyas columnas forman `P`, su nueva matriz es **`B = P⁻¹ A P`** (matrices semejantes!).",
            ],
            "real_world": [
                {
                    "title": "Cámaras 3D en videojuegos (View Matrix)",
                    "detail": "Cambiar de coordenadas del 'mundo' a las coordenadas de la 'cámara del jugador' es literalmente aplicar un cambio de base `P⁻¹`.",
                },
                {
                    "title": "Rotaciones y cizalladuras (skew) en CSS y SVG",
                    "detail": "El comando CSS `transform: matrix(a, b, c, d, ...)` recibe directamente las columnas `T(e₁) = ⟨a, b⟩` y `T(e₂) = ⟨c, d⟩`!",
                },
                {
                    "title": "Procesamiento de señales (Fourier = cambio de base!)",
                    "detail": "Pasar un audio del dominio del tiempo al dominio de las frecuencias es un cambio de base desde impulsos hacia ondas senoidales.",
                },
            ],
            "key_rule": "Columnas de A = imágenes de los ejes T(e₁), T(e₂) | Rotación: [[cos θ, −sen θ], [sen θ, cos θ]] | Cambio de base: P⁻¹AP.",
            "pitfall": "Escribir `T(e₁)` y `T(e₂)` en las FILAS en vez de las COLUMNAS, o confundir `(AB)ᵀ` con `AᵀBᵀ` (siempre se invierte a `BᵀAᵀ`).",
        },
        "example": {
            "title": "Construir la matriz que refleja sobre el eje X y estira ×2 en Y",
            "steps": [
                "Miramos dónde va `e₁ = ⟨1, 0⟩`: sobre el eje X no cambia → `T(e₁) = ⟨1, 0⟩` (1.ª columna).",
                "Miramos dónde va `e₂ = ⟨0, 1⟩`: se refleja a `⟨0, −1⟩` y se estira ×2 → `T(e₂) = ⟨0, −2⟩` (2.ª columna).",
                "Matriz resultante: `A = [[1, 0], [0, −2]]` (chequeo: `det = −2`, duplica áreas e invierte orientación!).",
            ],
            "lab_link": "math:linear_algebra",
            "lab_cta": "Practicar transformaciones y proyecciones en el Laboratorio",
        },
        "check": {
            "question": "Si una transformación lineal lleva `e₁ = ⟨1, 0⟩` a `⟨2, 5⟩` y `e₂ = ⟨0, 1⟩` a `⟨−1, 3⟩`, ¿cuál es su matriz `A`?",
            "options": [
                {"text": "`[[2, −1], [5, 3]]`", "ok": True, "feedback": "Exacto: cada imagen T(e_i) va parada como una COLUMNA."},
                {"text": "`[[2, 5], [−1, 3]]`", "ok": False, "feedback": "Las pusiste acostadas como filas en vez de paradas como columnas!"},
                {"text": "`[[5, 3], [2, −1]]`", "ok": False, "feedback": "Intercambiaste las filas y las pusiste al revés."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál de las siguientes funciones SÍ es una transformación lineal?",
                "options": [
                    {"text": "`T(x, y) = ⟨3x − y, 2y⟩`", "ok": True, "feedback": "Exacto: solo combinaciones lineales puras de x e y, y T(0, 0) = ⟨0, 0⟩."},
                    {"text": "`T(x, y) = ⟨x², y⟩`", "ok": False, "feedback": "Al elevar al cuadrado curva el espacio: T(2x) = 4x² ≠ 2·T(x)."},
                    {"text": "`T(x, y) = ⟨x + 1, y − 2⟩`", "ok": False, "feedback": "Mueve el origen a ⟨1, −2⟩ ≠ ⟨0, 0⟩, así que no es lineal (es afín)."},
                ],
            },
            {
                "question": "Si `B = P⁻¹ A P` (la misma transformación en otra base), ¿cómo se compara `det(B)` con `det(A)`?",
                "options": [
                    {"text": "Son exactamente iguales (`det(P⁻¹AP) = det(P⁻¹)·det(A)·det(P) = det(A)`)", "ok": True, "feedback": "Exacto: el factor de escala de volumen no depende de qué ejes elijas para medirlo!"},
                    {"text": "`det(B) = det(A) · det(P)`", "ok": False, "feedback": "det(P⁻¹) = 1/det(P) se cancela exactamente con det(P)."},
                    {"text": "No tienen relación", "ok": False, "feedback": "Determinante, traza y eigenvalores son invariantes bajo cambio de base."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá el truco de mirar `T(e₁)` y `T(e₂)` para leer o construir cualquier matriz 2×2 sin memorizar fórmulas.",
    },
    "la-proyecciones-ortogonales": {
        "hook": "Usar ejes perpendiculares de largo 1 (bases ortonormales) convierte cualquier cálculo matricial pesadísimo en simples productos punto — y hace que invertir una rotación sea tan fácil como trasponerla.",
        "concept": {
            "points": [
                "**Proyección ortogonal sobre una recta `u`**: **`proj_u(v) = [(v · u) / (u · u)] · u`** (la 'sombra perpendicular' de `v` sobre `u`, y el punto de la recta más cercano a `v`!).",
                "**Bases ortonormales `{q₁, ..., q_n}`** (perpendiculares entre sí y de largo `1`): hallar las coordenadas de cualquier `v` es instantáneo — solo hacés productos punto **`c_i = v · q_i`** (cero eliminación gaussiana!).",
                "**Matrices ortogonales `Q`** (columnas ortonormales): cumplen **`Qᵀ Q = I` ⇒ `Q⁻¹ = Qᵀ`**, conservan longitudes y ángulos (`|Qv| = |v|`). Y para cualquier subespacio `W` en `ℝⁿ`, **`dim(W) + dim(W⊥) = n`**.",
            ],
            "real_world": [
                {
                    "title": "Motores 3D y realidad virtual (`Q⁻¹ = Qᵀ`)",
                    "detail": "Para deshacer la rotación de la cabeza en gafas VR a 120 FPS, basta trasponer la matriz de rotación `3×3` en vez de calcular una inversa costosa.",
                },
                {
                    "title": "Compresión JPEG y MP3 (bases ortonormales de cosenos)",
                    "detail": "JPEG proyecta bloques de `8×8` píxeles sobre una base ortonormal de cosenos (DCT) usando simples productos punto y descarta los coeficientes casi nulos.",
                },
                {
                    "title": "Descomponer fuerzas en plano inclinado",
                    "detail": "Separar el peso `mg` en componente paralela a la rampa (`proj_u`) y normal perpendicular (`v − proj_u`) es exactamente una descomposición ortogonal `W ⊕ W⊥`.",
                },
            ],
            "key_rule": "proj_u(v) = ((v·u)/(u·u))·u | Base ortonormal: c_i = v · q_i | Matriz ortogonal: Q⁻¹ = Qᵀ | dim W + dim W⊥ = n.",
            "pitfall": "Olvidar dividir por `u · u` (`|u|²`) en `proj_u(v)` cuando `u` NO es unitario (si `u` ya mide 1, `u · u = 1` y se simplifica a `(v · u)u`).",
        },
        "example": {
            "title": "Proyectar v = ⟨4, 6⟩ sobre u = ⟨1, 1⟩ y verificar el error perpendicular",
            "steps": [
                "Calculamos `v · u = 4(1) + 6(1) = 10` y `u · u = 1² + 1² = 2`.",
                "Proyección: `proj_u(v) = (10 / 2) · ⟨1, 1⟩ = ⟨5, 5⟩`.",
                "Vector error perpendicular: `e = v − proj = ⟨4 − 5, 6 − 5⟩ = ⟨−1, 1⟩`. Chequeo: `⟨−1, 1⟩ · ⟨1, 1⟩ = 0` exacto!",
            ],
            "lab_link": "math:linear_algebra",
            "lab_cta": "Practicar proyecciones ortogonales en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es la proyección ortogonal de `v = ⟨6, 2⟩` sobre `u = ⟨3, 0⟩`?",
            "options": [
                {"text": "`⟨6, 0⟩` (`(18 / 9) · ⟨3, 0⟩ = 2⟨3, 0⟩`)", "ok": True, "feedback": "Exacto: la sombra sobre el eje X simplemente conserva x = 6 y pone y = 0."},
                {"text": "`⟨18, 0⟩`", "ok": False, "feedback": "Dividiste por `|u| = 3` en vez de por `u · u = 3² = 9`!"},
                {"text": "`⟨0, 2⟩`", "ok": False, "feedback": "⟨0, 2⟩ es la componente perpendicular (el error), no la proyección sobre u."},
            ],
        },
        "checks": [
            {
                "question": "Si una matriz `Q` cumple `Qᵀ Q = I`, ¿qué podés asegurar sobre su determinante `det(Q)`?",
                "options": [
                    {"text": "Solo puede valer `+1` (rotación) o `−1` (reflexión)", "ok": True, "feedback": "Exacto: det(QᵀQ) = (det Q)² = det(I) = 1 → det(Q) = ±1."},
                    {"text": "Siempre vale `0`", "ok": False, "feedback": "Q siempre es invertible (Q⁻¹ = Qᵀ), así que det nunca es 0."},
                    {"text": "Puede ser cualquier número positivo", "ok": False, "feedback": "Como conserva longitudes y áreas exactamente, |det(Q)| = 1."},
                ],
            },
            {
                "question": "En `ℝ³`, ¿qué es el complemento ortogonal `W⊥` de un plano `W` que pasa por el origen?",
                "options": [
                    {"text": "La recta normal perpendicular al plano que pasa por el origen (`dim = 3 − 2 = 1`)", "ok": True, "feedback": "Exacto: el vector normal del plano genera W⊥."},
                    {"text": "Otro plano paralelo", "ok": False, "feedback": "Un plano desplazado ni siquiera pasa por el origen ni tiene dimensión 1."},
                    {"text": "Todo `ℝ³`", "ok": False, "feedback": "dim(W) + dim(W⊥) = 3 → dim(W⊥) = 1."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué las bases ortonormales simplifican tanto el cálculo de coordenadas y la inversión de matrices.",
    },
    "la-gram-schmidt-minimos": {
        "hook": "¿Cómo traza Excel o Python la 'mejor recta' sobre 1000 puntos ruidosos que no caen en ninguna línea? Proyecta los datos sobre el espacio columna usando mínimos cuadrados (`AᵀAx̂ = Aᵀb`).",
        "concept": {
            "points": [
                "**Proceso de Gram-Schmidt**: toma una base inclinada `{v₁, v₂, ...}` y la 'endereza' a `90°` paso a paso: dejás `w₁ = v₁`, y a cada nuevo vector le **restás sus proyecciones** sobre los anteriores (`w₂ = v₂ − proj_{w₁}(v₂)`). Al final normalizás cada uno (`q_i = w_i / |w_i|`) → **factorización `A = QR`**.",
                "**Mínimos cuadrados**: en ciencia de datos casi siempre tenés más ecuaciones que incógnitas (`Ax = b` no tiene solución exacta porque `b ∉ Col(A)`). Buscamos el `x̂` que minimiza el error `|Ax − b|²`.",
                "**Ecuaciones normales**: el mínimo error ocurre cuando `(b − Ax̂)` es perpendicular a todas las columnas de `A` (`Aᵀ(b − Ax̂) = 0`) → **`Aᵀ A x̂ = Aᵀ b`** (o con QR: `Rx̂ = Qᵀb`!).",
            ],
            "real_world": [
                {
                    "title": "Regresión lineal y machine learning",
                    "detail": "Ajustar una recta `y = mx + b` o un modelo de múltiples variables a datos reales resuelve exactamente `AᵀA x̂ = Aᵀb` (Ordinary Least Squares).",
                },
                {
                    "title": "Posicionamiento GPS (más de 4 satélites)",
                    "detail": "Tu celular recibe señales con ruido de 8–12 satélites (sistema sobredeterminado) y calcula tu ubicación óptima por mínimos cuadrados.",
                },
                {
                    "title": "Estabilidad numérica en librerías científicas",
                    "detail": "En vez de formar `AᵀA` (que eleva al cuadrado el número de condición y amplifica los errores de redondeo), las librerías usan `A = QR` con reflexiones de Householder o la descomposición SVD (como `numpy.linalg.lstsq`).",
                },
            ],
            "key_rule": "Gram-Schmidt: w₂ = v₂ − proj_{w₁}(v₂), luego normalizar | Mínimos cuadrados: AᵀA x̂ = Aᵀb (equivale a proyectar b sobre Col(A)).",
            "pitfall": "Intentar resolver `Ax = b` sobredeterminado haciendo `A⁻¹b`: una matriz rectangular (ej. `100 × 2`) NO tiene inversa, pero `AᵀA` (`2 × 2`) sí, siempre que las columnas de `A` sean independientes!",
        },
        "example": {
            "title": "Ajustar y = m·x a los puntos (1, 2) y (2, 5) por mínimos cuadrados",
            "steps": [
                "Planteamos el sistema imposible `1·m = 2` y `2·m = 5`: `A = [1, 2]ᵀ`, `b = [2, 5]ᵀ`.",
                "Armamos las ecuaciones normales: `AᵀA = 1² + 2² = 5` y `Aᵀb = 1(2) + 2(5) = 12`.",
                "Resolvemos `5m = 12` → `m = 2.4` (predice `2.4` y `4.8`, con error cuadrático mínimo `0.16 + 0.04 = 0.20`).",
            ],
            "lab_link": "math:linear_algebra",
            "lab_cta": "Practicar proyecciones y mínimos cuadrados en el Laboratorio",
        },
        "check": {
            "question": "Si aplicás Gram-Schmidt a `v₁ = ⟨2, 0⟩` y `v₂ = ⟨5, 4⟩`, ¿qué vector perpendicular `w₂ = v₂ − proj_{v₁}(v₂)` obtenés antes de normalizar?",
            "options": [
                {"text": "`⟨0, 4⟩`", "ok": True, "feedback": "Exacto: le restamos su sombra horizontal ⟨5, 0⟩ y queda solo la componente vertical ⟨0, 4⟩!"},
                {"text": "`⟨5, 0⟩`", "ok": False, "feedback": "⟨5, 0⟩ es la proyección paralela a v₁, no la parte perpendicular restante."},
                {"text": "`⟨3, 4⟩`", "ok": False, "feedback": "Restaste v₁ directamente en vez de restar la proyección de v₂ sobre v₁."},
            ],
        },
        "checks": [
            {
                "question": "En el método de mínimos cuadrados, si `A` tiene `100` filas (datos) y `3` columnas (parámetros), ¿qué dimensión tiene la matriz cuadrada `Aᵀ A`?",
                "options": [
                    {"text": "`3 × 3` (pequeñísima y súper rápida de resolver!)", "ok": True, "feedback": "Exacto: (3 × 100) · (100 × 3) = 3 × 3."},
                    {"text": "`100 × 100`", "ok": False, "feedback": "Eso sería A·Aᵀ; en las ecuaciones normales va Aᵀ·A."},
                    {"text": "`100 × 3`", "ok": False, "feedback": "Multiplicar Aᵀ por A siempre devuelve una matriz cuadrada simétrica."},
                ],
            },
            {
                "question": "Si el vector residual `e = b − Ax̂` de un ajuste por mínimos cuadrados da exactamente `⟨0, 0, ...⟩`, ¿qué significa?",
                "options": [
                    {"text": "Que `b` ya estaba dentro de `Col(A)` y el sistema tenía solución exacta sin error", "ok": True, "feedback": "Exacto: todos los puntos caen perfectamente sobre la recta o modelo."},
                    {"text": "Que el método falló", "ok": False, "feedback": "Al contrario, es el ajuste perfecto (error 0)!"},
                    {"text": "Que `x̂ = 0`", "ok": False, "feedback": "No: significa que Ax̂ = b exactamente."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá cómo se conectan las proyecciones ortogonales con encontrar la mejor recta de regresión lineal sobre datos ruidosos.",
    },
    "la-eigenvalores-eigenvectores": {
        "hook": "Cuando una matriz deforma el espacio, casi todos los vectores se tuercen de dirección — pero existen unos pocos ejes privilegiados que SOLO se estiran o encogen: los **eigenvectores**.",
        "concept": {
            "points": [
                "Un vector no nulo `v` es **vector propio (eigenvector)** de `A` con **valor propio (eigenvalor) `λ`** si **`A·v = λ·v`** (la transformación simplemente lo escala por `λ`, sin girarlo de su recta!).",
                "**Cómo hallarlos**: `Av = λv ⇔ (A − λI)v = 0` tiene solución `v ≠ 0` solo cuando **`det(A − λI) = 0`** (ecuación característica). Luego, para cada `λ`, sus eigenvectores son el espacio nulo **`Nul(A − λI)`**.",
                "**Atajos de oro**: en matrices triangulares/diagonales, los `λ` son la **diagonal**. En cualquier `2×2`: **`λ₁ + λ₂ = traza (a + d)`** y **`λ₁ · λ₂ = det(A)`**!",
            ],
            "real_world": [
                {
                    "title": "Frecuencias naturales de vibración (puentes, cuerdas, edificios)",
                    "detail": "Los modos normales en que vibra una cuerda de guitarra o un rascacielos son los eigenvectores del sistema, y los eigenvalores dan sus frecuencias resonantes.",
                },
                {
                    "title": "Mecánica cuántica (niveles de energía cuantizados)",
                    "detail": "La ecuación de Schrödinger `H ψ = E ψ` es literalmente una ecuación de eigenvalores: los niveles de energía permitidos de un átomo son los eigenvalores `E`!",
                },
                {
                    "title": "Ejes principales de rotación (inercia)",
                    "detail": "Un objeto 3D gira estable sin tambalearse únicamente alrededor de los eigenvectores de su tensor de inercia.",
                },
            ],
            "key_rule": "Av = λv | Hallar λ: det(A − λI) = 0 | En 2×2: λ₁ + λ₂ = traza y λ₁·λ₂ = det | Triangular: λ en la diagonal.",
            "pitfall": "Aceptar el vector nulo `v = 0` como eigenvector (por definición un eigenvector SIEMPRE debe ser `v ≠ 0`, porque `A·0 = λ·0` se cumple trivialmente para cualquier `λ`!).",
        },
        "example": {
            "title": "Hallar los eigenvalores de A = [[4, 1], [2, 3]] con traza y determinante",
            "steps": [
                "Calculamos traza (`4 + 3 = 7`) y determinante (`4·3 − 1·2 = 10`).",
                "Buscamos dos números que sumen `7` y multipliquen `10` (equivale a `λ² − 7λ + 10 = 0`): son **`λ₁ = 5`** y **`λ₂ = 2`**!",
                "Para `λ = 5`, `(A − 5I)v = [[−1, 1], [2, −2]]v = 0` → `−x + y = 0` → eigenvector `v₁ = ⟨1, 1⟩` (chequeo: `A⟨1, 1⟩ = ⟨5, 5⟩ = 5⟨1, 1⟩`!).",
            ],
            "lab_link": "math:eigen_lab",
            "lab_cta": "Practicar eigenvalores y eigenvectores en el Laboratorio",
        },
        "check": {
            "question": "Para `A = [[5, 2], [0, 3]]`, ¿cuáles son sus eigenvalores `λ₁` y `λ₂`?",
            "options": [
                {"text": "`5` y `3` (matriz triangular: se leen directo en la diagonal!)", "ok": True, "feedback": "Exacto: det(A − λI) = (5 − λ)(3 − λ) = 0 → λ = 5, 3."},
                {"text": "`5` y `2`", "ok": False, "feedback": "El 2 está fuera de la diagonal principal."},
                {"text": "`15` y `8`", "ok": False, "feedback": "15 es el producto (det) y 8 es la suma (traza): los eigenvalores son 5 y 3."},
            ],
        },
        "checks": [
            {
                "question": "Una matriz `2 × 2` tiene `traza = 10` y `determinante = 21`. ¿Cuáles son sus dos eigenvalores?",
                "options": [
                    {"text": "`7` y `3` (`7 + 3 = 10` y `7 × 3 = 21`)", "ok": True, "feedback": "Exacto: traza y determinante resuelven cualquier 2×2 casi mentalmente!"},
                    {"text": "`10` y `21`", "ok": False, "feedback": "10 es la suma y 21 el producto, no los valores individuales."},
                    {"text": "`5` y `5`", "ok": False, "feedback": "5 × 5 = 25 ≠ 21."},
                ],
            },
            {
                "question": "Si `v` es eigenvector de `A` con eigenvalor `λ = 3`, ¿qué hace `A²` sobre ese mismo vector `v`?",
                "options": [
                    {"text": "`A² v = 9 v` (el eigenvalor se eleva al cuadrado: `λ² = 3² = 9`!)", "ok": True, "feedback": "Exacto: A(Av) = A(3v) = 3(Av) = 3(3v) = 9v."},
                    {"text": "`A² v = 6 v`", "ok": False, "feedback": "Se multiplica por λ dos veces (3 × 3 = 9), no 2 × 3."},
                    {"text": "`v` deja de ser eigenvector de `A²`", "ok": False, "feedback": "Sigue siendo el mismo eigenvector con eigenvalor λ²."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá el significado geométrico de `Av = λv` y cómo usás la traza y el determinante en una matriz `2×2`.",
    },
    "la-diagonalizacion-aplicaciones": {
        "hook": "Si cambiás de ejes para alinearte con los eigenvectores, cualquier matriz complicada se vuelve simplemente diagonal — destrabando `A¹⁰⁰`, Google PageRank y la compresión PCA en IA.",
        "concept": {
            "points": [
                "**Diagonalización (`A = P D P⁻¹`)**: si una matriz `n × n` tiene `n` eigenvectores independientes, los ponés en las columnas de `P` y sus eigenvalores en la diagonal de `D`. Así elevar a cualquier potencia colapsa a **`Aⁿ = P Dⁿ P⁻¹`**!",
                "**Teorema Espectral**: si `A` es **simétrica (`A = Aᵀ`)**, SIEMPRE es diagonalizable con eigenvalores reales y eigenvectores **ortonormales** (**`A = Q D Qᵀ`**).",
                "**Aplicaciones modernas**: en **cadenas de Markov / PageRank**, el equilibrio a largo plazo es el eigenvector de **`λ = 1`**; en **PCA (ciencia de datos)**, los eigenvectores de la matriz de covarianza revelan los ejes principales donde varía la información.",
            ],
            "real_world": [
                {
                    "title": "Google PageRank y cadenas de Markov",
                    "detail": "Modelando un navegante saltando al azar entre links web, la distribución estacionaria de visitas (`P·v = 1·v`) es el eigenvector principal con `λ = 1`.",
                },
                {
                    "title": "PCA y compresión facial / embeddings en IA",
                    "detail": "Diagonalizar la matriz de covarianza (`Q D Qᵀ`) separa direcciones de alta varianza (`λ` grande) del ruido (`λ ≈ 0`), comprimiendo miles de dimensiones en unas pocas.",
                },
                {
                    "title": "Sistemas acoplados de ecuaciones diferenciales (`x' = Ax`)",
                    "detail": "Diagonalizar `A` desacopla un sistema enredado de `n` ecuaciones diferenciales en `n` ecuaciones independientes facilísimas `u_i' = λ_i u_i`!",
                },
            ],
            "key_rule": "A = P D P⁻¹ ⇒ Aⁿ = P Dⁿ P⁻¹ | Simétrica (A = Aᵀ): A = Q D Qᵀ | Markov equilibrio: λ = 1 | PCA: mayores λ.",
            "pitfall": "Suponer que TODA matriz cuadrada es diagonalizable: matrices de cizalladura como `[[1, 1], [0, 1]]` tienen raíz repetida `λ = 1` pero solo 1 eigenvector independiente, así que NO se pueden diagonalizar!",
        },
        "example": {
            "title": "Ver el poder de Aⁿ = P Dⁿ P⁻¹ en una cadena de Markov 2×2",
            "steps": [
                "En `A = P [[1, 0], [0, 0.5]] P⁻¹`, el primer eigenvalor es `λ₁ = 1` y el segundo es `λ₂ = 0.5`.",
                "Al calcular `Aⁿ = P [[1ⁿ, 0], [0, (0.5)ⁿ]] P⁻¹` para `n` grande, `(0.5)ⁿ → 0` mientras `1ⁿ = 1` sobrevive!",
                "Por eso, sin importar desde qué estado inicial arranques, el sistema converge siempre al eigenvector del estado estacionario (`λ = 1`).",
            ],
            "lab_link": "math:eigen_lab",
            "lab_cta": "Practicar eigenvalores y diagonalización en el Laboratorio",
        },
        "check": {
            "question": "Si `A = P D P⁻¹` con `D = [[1, 0], [0, 2]]`, ¿cuál es la matriz diagonal `D⁵` dentro de `A⁵ = P D⁵ P⁻¹`?",
            "options": [
                {"text": "`[[1, 0], [0, 32]]` (`1⁵ = 1` y `2⁵ = 32`)", "ok": True, "feedback": "Exacto: en una matriz diagonal solo elevás cada entrada de la diagonal."},
                {"text": "`[[5, 0], [0, 10]]`", "ok": False, "feedback": "Multiplicaste por 5 en vez de elevar a la potencia 5."},
                {"text": "`[[1, 0], [0, 2]]`", "ok": False, "feedback": "2⁵ vale 32, no 2."},
            ],
        },
        "checks": [
            {
                "question": "La matriz `A = [[4, 7], [7, −2]]` es simétrica (`A = Aᵀ`). ¿Qué te garantiza el Teorema Espectral sin hacer ni una cuenta?",
                "options": [
                    {"text": "Que sus dos eigenvalores son reales y sus dos eigenvectores son perpendiculares (`90°`)", "ok": True, "feedback": "Exacto: toda matriz simétrica real es ortogonalmente diagonalizable (Q D Qᵀ)."},
                    {"text": "Que sus eigenvalores son `4` y `−2`", "ok": False, "feedback": "Leer la diagonal solo funciona en matrices triangulares o diagonales; aquí el 7 fuera de la diagonal cambia los eigenvalores."},
                    {"text": "Que no es invertible", "ok": False, "feedback": "det = −8 − 49 = −57 ≠ 0, sí es invertible."},
                ],
            },
            {
                "question": "¿Por qué la matriz de cizalladura `[[1, 1], [0, 1]]` NO es diagonalizable?",
                "options": [
                    {"text": "Porque solo tiene un eigenvalor repetido (`λ = 1`) con una única dirección de eigenvector (no alcanza para formar `P` de 2 columnas independientes)", "ok": True, "feedback": "Exacto: necesita 2 eigenvectores independientes para invertir P, pero solo tiene la recta ⟨1, 0⟩."},
                    {"text": "Porque su determinante es `0`", "ok": False, "feedback": "Su determinante es 1 ≠ 0 (es invertible, pero igual no es diagonalizable!)."},
                    {"text": "Porque tiene eigenvalores complejos", "ok": False, "feedback": "Su eigenvalor λ = 1 es real."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en tus palabras por qué cambiar a la base de eigenvectores (`A = PDP⁻¹`) simplifica drásticamente el cálculo de `Aⁿ` y el análisis de sistemas complejos.",
    },
}
