"""Trigonometry curriculum (6 units, #63-#68) adapted from Khan Academy Trigonometry.

Completes the full Khan Academy Trigonometry course building on Geometría (#46-#47)
and Álgebra 2 (#61):
  - Reciprocal trig ratios (csc, sec, cot), reference & coterminal angles
  - Phase shifts in sinusoidal functions (A·sin(B(x - C)) + D) & tangent graphs
  - Law of Sines, Law of Cosines (oblique triangles) & trigonometric area
  - Inverse trig functions (arcsin, arccos, arctan) & restricted domains
  - Trigonometric identities: derived Pythagorean, even/odd, sum/difference & double-angle
  - Solving trigonometric equations (interval & general solutions +2πk)
"""

from __future__ import annotations

TRIGONOMETRY_NODES: list[dict] = [
    # ==================== NIVEL 23: RECÍPROCAS, DESFASE Y TRIÁNGULOS OBLICUÁNGULOS ====================
    {
        "slug": "t-reciprocas-referencia",
        "title": "63. Razones recíprocas (csc, sec, cot) y ángulos de referencia",
        "level": 23,
        "order_index": 63,
        "summary": "Cosecante, secante y cotangente, ángulos coterminales y ángulos de referencia para evaluar cualquier cuadrante sin memorizar tablas.",
        "prerequisites": ["a2-circulo-unitario-ondas"],
        "metadata": {"section": "Trigonometría", "lab_tab": "trig_identities", "est_minutes": 18},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Calcular sec(θ) desde cos(θ)",
                "prompt": "La secante es el recíproco del coseno: sec(θ) = 1 / cos(θ). Si cos(θ) = 0.25 (1/4), ¿cuánto vale sec(θ)? Respondé solo con el número.",
                "answer": "4: sec(θ) = 1 / 0.25 = 4 (recordá el truco de las letras: 's' va con 'c' → sec = 1/cos y csc = 1/sen).",
                "hints": ["Invertí la fracción 1/4 → 4/1."],
                "payload": {
                    "lab_link": "math:trig_identities",
                    "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Calcular cot(θ) desde tan(θ)",
                "prompt": "Si la pendiente de un techo tiene tan(θ) = 0.5, ¿cuánto vale su recíproca cot(θ) = 1 / tan(θ)? Respondé solo con el número.",
                "answer": "2: cot(θ) = 1 / 0.5 = 2 (también equivale a Adyacente / Opuesto = cos(θ) / sen(θ)).",
                "hints": ["Calculá 1 ÷ 0.5."],
                "payload": {
                    "lab_link": "math:trig_identities",
                    "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ángulo de referencia en el 3.er cuadrante",
                "prompt": "El ángulo de referencia es siempre el ángulo agudo que forma el rayo con el eje horizontal X. ¿Cuál es el ángulo de referencia de 225° (3.er cuadrante)? Respondé solo con el número en grados.",
                "answer": "45°: en el 3.er cuadrante se calcula θ − 180° = 225° − 180° = 45°.",
                "hints": ["Medí cuánto se pasó 225° del eje horizontal (180°)."],
                "payload": {
                    "lab_link": "math:trig_identities",
                    "check": {"type": "numeric", "value": 45, "tolerance": 0, "unit": "°"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Evaluar cos(120°) con ángulo de referencia y signo",
                "prompt": "120° está en el 2.° cuadrante (x < 0) con ángulo de referencia 180° − 120° = 60°. Sabiendo que cos(60°) = 0.5, ¿cuánto vale cos(120°)? Respondé solo con el número.",
                "answer": "−0.5: el valor absoluto sale del ángulo de referencia (0.5) y el signo negativo del 2.° cuadrante donde x < 0.",
                "hints": ["En el 2.° cuadrante la coordenada x (coseno) es negativa."],
                "payload": {
                    "lab_link": "math:trig_identities",
                    "check": {"type": "numeric", "value": -0.5, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Reducir un ángulo coterminal mayor a 360°",
                "prompt": "Un motor gira 405° desde 0°. ¿A qué ángulo coterminal entre 0° y 360° apunta exactamente en la misma dirección? Respondé solo con el número en grados.",
                "answer": "45°: restar una vuelta completa (405° − 360° = 45°) deja el rayo exactamente en el mismo lugar.",
                "hints": ["Restale una vuelta completa (360°)."],
                "payload": {"check": {"type": "numeric", "value": 45, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "recall",
                "title": "Emparejar cada razón recíproca sin confundir csc y sec",
                "prompt": "¿Cuál de estas definiciones es CORRECTA?",
                "answer": "csc(θ) = 1 / sen(θ) y sec(θ) = 1 / cos(θ) (cada pareja lleva una sola 'co': seno↔cosecante, coseno↔secante).",
                "hints": ["Nunca van dos 'co' juntas: coseno se empareja con secante."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "csc(θ) = 1/sen(θ)  y  sec(θ) = 1/cos(θ)",
                            "csc(θ) = 1/cos(θ)  y  sec(θ) = 1/sen(θ)",
                            "sec(θ) = 1/tan(θ)  y  csc(θ) = 1/sen(θ)",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "t-desfase-tangente",
        "title": "64. Desfase de ondas sinusoidales y gráfica de tangente",
        "level": 23,
        "order_index": 64,
        "summary": "Corrimiento de fase en y = A·sen(B(x − C)) + D, armar modelos desde picos reales y período/asíntotas de y = tan(x).",
        "prerequisites": ["a2-circulo-unitario-ondas", "a2-transformaciones-funciones"],
        "metadata": {"section": "Trigonometría", "lab_tab": "trig_waves", "est_minutes": 20},
        "items": [
            {
                "item_type": "recall",
                "title": "Leer el desfase real factorizando B primero",
                "prompt": "Para hallar el desfase (corrimiento horizontal) de y = sen(2x − π/2), primero hay que sacar el 2 como factor común dentro del paréntesis. ¿Cuánto y hacia dónde se corrió la onda?",
                "answer": "π/4 hacia la derecha (no π/2!): al factorizar queda sen(2(x − π/4)); el desfase real siempre es C = φ / B después de sacar B como factor común.",
                "hints": ["Sacá el 2 como factor común (2x − π/2 = 2(x − π/4)) y mirá el número que resta directamente a x."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "π/4 hacia la derecha",
                            "π/2 hacia la derecha",
                            "π/4 hacia la izquierda",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Amplitud desde datos reales de temperatura diaria",
                "prompt": "La temperatura de una ciudad oscila sinusoidalmente entre una mínima de 12°C a las 03:00 y una máxima de 28°C a las 15:00. ¿Cuál es la amplitud A del modelo (en °C)? Respondé solo con el número.",
                "answer": "8°C: amplitud = (máx − mín) / 2 = (28 − 12) / 2 = 8°C (y la línea media es (28 + 12)/2 = 20°C).",
                "hints": ["Calculá (28 − 12) ÷ 2."],
                "payload": {
                    "lab_link": "math:trig_waves",
                    "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": "°C"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Línea media de un ciclo de temperatura",
                "prompt": "En el mismo ciclo diario entre 12°C (mínima) y 28°C (máxima), ¿cuál es la línea media D (en °C)? Respondé solo con el número.",
                "answer": "20°C: la línea media es el promedio entre máximo y mínimo → (28 + 12) / 2 = 20°C.",
                "hints": ["Promediá el máximo y el mínimo: (28 + 12) ÷ 2."],
                "payload": {
                    "lab_link": "math:trig_waves",
                    "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "°C"},
                },
            },
            {
                "item_type": "recall",
                "title": "Por qué y = tan(x) tiene asíntotas verticales",
                "prompt": "Como tan(x) = sen(x) / cos(x), ¿dónde aparecen las asíntotas verticales de la gráfica de y = tan(x)?",
                "answer": "Donde cos(x) = 0, es decir en x = ±90° (±π/2), ±270° (±3π/2), etc.",
                "hints": ["Una fracción explota hacia ±∞ cuando su denominador se hace cero."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Donde cos(x) = 0 (x = ±π/2, ±3π/2, ...)",
                            "Donde sen(x) = 0 (x = 0, ±π, ±2π, ...)",
                            "tan(x) no tiene asíntotas",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Período de la función tangente escalada",
                "prompt": "El período natural de y = tan(x) es 180° (π rad, la mitad que seno y coseno). ¿Cuántos grados mide el período de y = tan(3x)? Respondé solo con el número en grados.",
                "answer": "60° (π/3 rad): el período de tan(Bx) es 180° / |B| = 180° / 3 = 60°.",
                "hints": ["Dividí el período base de tangente (180°) por B = 3."],
                "payload": {"check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "recall",
                "title": "Relación de desfase entre seno y coseno",
                "prompt": "El coseno arranca en su pico (1) en x = 0 y el seno alcanza su pico (1) en x = 90° (π/2). ¿Qué equivalencia conecta ambas ondas?",
                "answer": "cos(x) = sen(x + 90°): el coseno es exactamente la misma onda seno adelantada un cuarto de ciclo (90° o π/2).",
                "hints": ["Probá x = 0 en sen(x + 90°): da sen(90°) = 1 = cos(0°)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "cos(x) = sen(x + 90°)",
                            "cos(x) = sen(x + 180°)",
                            "cos(x) = 2 · sen(x)",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "t-leyes-senos-cosenos",
        "title": "65. Ley de senos, Ley de cosenos y triángulos oblicuángulos",
        "level": 23,
        "order_index": 65,
        "summary": "Resolver cualquier triángulo aunque NO tenga ángulo de 90°: Ley de senos, Ley de cosenos (Pitágoras generalizado) y área trigonométrica.",
        "prerequisites": ["g-trigonometria", "a2-circulo-unitario-ondas"],
        "metadata": {"section": "Trigonometría", "lab_tab": "oblique_triangles", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Ley de senos para hallar una distancia en topografía",
                "prompt": "En un triángulo no rectángulo, el lado a = 10 m está frente a A = 30° (sen 30° = 0.5). Si el ángulo B cumple sen(B) = 0.8, usá a/sen(A) = b/sen(B) para calcular el lado b (en m). Respondé solo con el número.",
                "answer": "16 m: 10 / 0.5 = 20 = b / 0.8 → b = 20 × 0.8 = 16 m.",
                "hints": ["Primero calculá la razón 10 ÷ 0.5 = 20, luego multiplicá por 0.8."],
                "payload": {
                    "lab_link": "math:oblique_triangles",
                    "check": {"type": "numeric", "value": 16, "tolerance": 0, "unit": "m"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ley de cosenos: distancia entre dos barcos (ángulo 60°)",
                "prompt": "Dos barcos salen del mismo puerto formando un ángulo de 60° (cos 60° = 0.5). Uno recorre 5 km y el otro 8 km. Usando c² = a² + b² − 2ab·cos(C), ¿a cuántos km están entre sí? Respondé solo con el número.",
                "answer": "7 km: c² = 25 + 64 − 2(5)(8)(0.5) = 89 − 40 = 49 → c = √49 = 7 km.",
                "hints": ["Calculá 25 + 64 − 40 y sacá la raíz cuadrada."],
                "payload": {
                    "lab_link": "math:oblique_triangles",
                    "check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": "km"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ley de cosenos con ángulo obtuso (120°)",
                "prompt": "Dos tensores de 3 m y 5 m salen de un mástil con ángulo de 120° entre sí (cos 120° = −0.5). ¿Cuántos metros separan sus extremos? Respondé solo con el número.",
                "answer": "7 m: c² = 3² + 5² − 2(3)(5)(−0.5) = 9 + 25 + 15 = 49 → c = 7 m (con ángulo obtuso, el término −2ab·cos(C) SUMA).",
                "hints": ["Cuidado con el signo: −2(3)(5)(−0.5) = +15."],
                "payload": {
                    "lab_link": "math:oblique_triangles",
                    "check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": "m"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Área de un terreno triangular sin conocer la altura",
                "prompt": "Un lote triangular tiene dos lados de 10 m y 12 m que forman un ángulo de 30° (sen 30° = 0.5). Usando Área = (1/2)·a·b·sen(C), ¿cuántos m² mide? Respondé solo con el número.",
                "answer": "30 m²: (1/2) × 10 × 12 × 0.5 = 60 × 0.5 = 30 m² (porque b·sen(C) es precisamente la altura).",
                "hints": ["Multiplicá 0.5 × 10 × 12 × 0.5."],
                "payload": {
                    "lab_link": "math:oblique_triangles",
                    "check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": "m²"},
                },
            },
            {
                "item_type": "recall",
                "title": "Cuándo elegir Ley de senos vs. Ley de cosenos",
                "prompt": "Te dan los tres lados de un triángulo (LLL: 7 m, 8 m y 10 m) y ningún ángulo. ¿Qué ley debés usar primero para hallar un ángulo?",
                "answer": "Ley de cosenos: la Ley de senos necesita al menos una pareja completa (lado + su ángulo opuesto), que en LLL (y en LAL) no tenés.",
                "hints": ["Para la Ley de senos necesitás conocer al menos un ángulo y el lado de enfrente."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Ley de cosenos (LLL y LAL)",
                            "Ley de senos",
                            "Teorema de Pitágoras",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Por qué el caso LLA puede ser ambiguo (2 triángulos)",
                "prompt": "Al usar la Ley de senos en un caso LLA (dos lados y un ángulo no comprendido), obtenés sen(B) = 0.5. ¿Por qué hay que chequear tanto B = 30° como B = 150°?",
                "answer": "Porque ángulos suplementarios tienen el MISMO seno (sen 30° = sen 150° = 0.5); si A + 150° < 180°, ambos triángulos son válidos.",
                "hints": ["En el círculo unitario hay dos ángulos entre 0° y 180° con la misma altura y."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Porque sen(θ) = sen(180° − θ) y el ángulo obtuso también puede caber en 180°",
                            "Porque el coseno es siempre positivo",
                            "Porque todo triángulo tiene 4 lados",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 24: INVERSAS, IDENTIDADES Y ECUACIONES ====================
    {
        "slug": "t-inversas-restringidas",
        "title": "66. Funciones trigonométricas inversas (arcsen, arccos, arctan)",
        "level": 24,
        "order_index": 66,
        "summary": "Rangos principales restringidos ([−90°, 90°] vs. [0°, 180°]), por qué arcsen(sen(150°)) ≠ 150° y composiciones con triángulos.",
        "prerequisites": ["t-reciprocas-referencia", "a2-transformaciones-funciones"],
        "metadata": {"section": "Trigonometría", "lab_tab": "trig_identities", "est_minutes": 18},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Evaluar arcsen de un valor negativo",
                "prompt": "Como el rango principal de arcsen(x) es [−90°, +90°], ¿cuántos grados devuelve arcsen(−0.5)? Respondé solo con el número (con signo).",
                "answer": "−30°: sen(−30°) = −0.5 y −30° está dentro de [−90°, +90°] (210° y 330° quedan fuera del rango principal).",
                "hints": ["Buscá el ángulo entre −90° y +90° cuyo seno es −0.5."],
                "payload": {"check": {"type": "numeric", "value": -30, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Evaluar arccos de un valor negativo",
                "prompt": "Como el rango principal de arccos(x) es [0°, 180°] (Q1 y Q2), ¿cuántos grados devuelve arccos(−0.5)? Respondé solo con el número.",
                "answer": "120°: cos(120°) = −0.5 y 120° está dentro de [0°, 180°] (en cambio −60° da +0.5 y queda fuera).",
                "hints": ["Buscá el ángulo en el 2.° cuadrante (entre 90° y 180°) con coseno −0.5."],
                "payload": {"check": {"type": "numeric", "value": 120, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "La trampa de arcsen(sen(150°))",
                "prompt": "¿Cuántos grados da arcsen(sen(150°))? (Pista: evaluá primero sen(150°) = 0.5, y luego aplicá arcsen dentro de [−90°, 90°]). Respondé solo con el número.",
                "answer": "30°: NO se cancelan a 150° porque 150° cae fuera de [−90°, 90°] → arcsen(0.5) = 30°.",
                "hints": ["sen(150°) = 0.5; ¿cuánto da arcsen(0.5)?"],
                "payload": {"check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Evaluar cos(arcsen(0.6)) dibujando un triángulo 3-4-5",
                "prompt": "Si θ = arcsen(3/5) (en el 1.er cuadrante: Opuesto = 3, Hipotenusa = 5), ¿cuánto vale cos(arcsen(3/5)) en decimal? Respondé solo con el número.",
                "answer": "0.8: por Pitágoras el adyacente vale √(5² − 3²) = 4, así que cos(θ) = 4/5 = 0.8 (sin usar calculadora!).",
                "hints": ["Si Op = 3 y Hip = 5, hallá el cateto adyacente y dividilo por 5."],
                "payload": {
                    "lab_link": "math:trig_identities",
                    "check": {"type": "numeric", "value": 0.8, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Evaluar arctan(−1) en grados",
                "prompt": "El rango principal de arctan(x) es (−90°, +90°). ¿Cuántos grados vale arctan(−1)? Respondé solo con el número.",
                "answer": "−45°: tan(−45°) = −1 y −45° pertenece al intervalo (−90°, +90°).",
                "hints": ["tan(45°) = 1 y tangente es impar."],
                "payload": {"check": {"type": "numeric", "value": -45, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "recall",
                "title": "Por qué la calculadora da error con arcsen(1.5)",
                "prompt": "Si tecleás arcsen(1.5) en una calculadora sale 'Math Error'. ¿Por qué?",
                "answer": "Porque el seno de cualquier ángulo real siempre vive entre −1 y +1, así que ningún ángulo real tiene seno igual a 1.5.",
                "hints": ["¿Cuál es el valor máximo que puede alcanzar sen(θ)?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "El dominio de arcsen es [−1, 1] porque sen(θ) nunca supera 1",
                            "Porque 1.5 es decimal y solo acepta enteros",
                            "Porque está en radianes en vez de grados",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "t-identidades-angulo-doble",
        "title": "67. Identidades trigonométricas, suma de ángulos y ángulo doble",
        "level": 24,
        "order_index": 67,
        "summary": "Identidades pitagóricas derivadas (1 + tan² = sec²), par/impar, fórmulas de suma/resta y fórmulas del ángulo doble.",
        "prerequisites": ["t-reciprocas-referencia"],
        "metadata": {"section": "Trigonometría", "lab_tab": "trig_identities", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Fórmula del ángulo doble: sen(2θ) = 2·sen(θ)·cos(θ)",
                "prompt": "Si sen(θ) = 0.6 y cos(θ) = 0.8, usá sen(2θ) = 2·sen(θ)·cos(θ) para calcular sen(2θ) en decimal. Respondé solo con el número.",
                "answer": "0.96: 2 × 0.6 × 0.8 = 0.96 (ojo: NO es 2 × 0.6 = 1.2, que incluso sería imposible > 1!).",
                "hints": ["Multiplicá 2 × 0.6 × 0.8."],
                "payload": {
                    "lab_link": "math:trig_identities",
                    "check": {"type": "numeric", "value": 0.96, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Fórmula del ángulo doble: cos(2θ) = cos²(θ) − sen²(θ)",
                "prompt": "Con el mismo ángulo (sen(θ) = 0.6 y cos(θ) = 0.8), calculá cos(2θ) = cos²(θ) − sen²(θ) en decimal. Respondé solo con el número.",
                "answer": "0.28: 0.8² − 0.6² = 0.64 − 0.36 = 0.28 (chequeo: 0.96² + 0.28² = 1!).",
                "hints": ["Calculá 0.64 − 0.36."],
                "payload": {
                    "lab_link": "math:trig_identities",
                    "check": {"type": "numeric", "value": 0.28, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Identidad pitagórica derivada: 1 + tan²(θ) = sec²(θ)",
                "prompt": "Si tan(θ) = 0.75 (3/4) en el 1.er cuadrante, usá 1 + tan²(θ) = sec²(θ) para hallar sec(θ) en decimal. Respondé solo con el número.",
                "answer": "1.25 (5/4): 1 + (3/4)² = 1 + 9/16 = 25/16 → sec(θ) = √(25/16) = 5/4 = 1.25.",
                "hints": ["1 + 9/16 = 25/16; sacá la raíz cuadrada (5/4 = 1.25)."],
                "payload": {
                    "lab_link": "math:trig_identities",
                    "check": {"type": "numeric", "value": 1.25, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Identidades par e impar: cos(−θ) vs. sen(−θ)",
                "prompt": "Sabiendo que cos(−θ) = cos(θ) y sen(−θ) = −sen(θ), si sen(θ) = 0.4, ¿cuánto vale sen(−θ)? Respondé solo con el número.",
                "answer": "−0.4: el seno es una función impar (reflejar el ángulo hacia abajo invierte la coordenada y).",
                "hints": ["Girar hacia abajo cambia el signo de la coordenada y (seno)."],
                "payload": {"check": {"type": "numeric", "value": -0.4, "tolerance": 0.01, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Simplificar tan(θ) · cos(θ) pasando todo a sen y cos",
                "prompt": "¿A qué expresión simple equivale tan(θ) · cos(θ) (cuando cos(θ) ≠ 0)?",
                "answer": "sen(θ): al reemplazar tan(θ) por sen(θ)/cos(θ), el cos(θ) se cancela arriba y abajo.",
                "hints": ["Reescribí tan(θ) como sen(θ) / cos(θ)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["sen(θ)", "1", "sec(θ)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "No distribuir seno sobre una suma: sen(α + β)",
                "prompt": "¿Cuál es la fórmula correcta para el seno de una suma de ángulos, sen(α + β)?",
                "answer": "sen(α)cos(β) + cos(α)sen(β) (en cambio sen(30° + 60°) = 1 ≠ sen 30° + sen 60° ≈ 1.37).",
                "hints": ["Seno mezcla sen y cos respetando el signo +."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "sen(α)cos(β) + cos(α)sen(β)",
                            "sen(α) + sen(β)",
                            "cos(α)cos(β) − sen(α)sen(β)",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "t-ecuaciones-trigonometricas",
        "title": "68. Ecuaciones trigonométricas y soluciones generales",
        "level": 24,
        "order_index": 68,
        "summary": "Hallar todas las soluciones en una vuelta [0°, 360°), soluciones generales (+ 360°k), factorización y ecuaciones con 2x.",
        "prerequisites": ["t-inversas-restringidas", "t-identidades-angulo-doble", "al-factorizar-cuadraticas"],
        "metadata": {"section": "Trigonometría", "lab_tab": "trig_identities", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Encontrar la segunda solución en [0°, 360°) de 2·sen(x) − 1 = 0",
                "prompt": "Resolvé 2·sen(x) − 1 = 0 (sen(x) = 0.5) en [0°, 360°). La calculadora solo muestra 30°. ¿Cuál es la OTRA solución en el 2.° cuadrante (en grados)? Respondé solo con el número.",
                "answer": "150°: en el círculo unitario, sen(x) = +0.5 se cumple tanto en 30° (Q1) como en 180° − 30° = 150° (Q2).",
                "hints": ["Usá la simetría horizontal del seno: 180° − 30°."],
                "payload": {"check": {"type": "numeric", "value": 150, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Resolver 2·cos(x) + 1 = 0 en [0°, 360°)",
                "prompt": "En 2·cos(x) + 1 = 0 despejás cos(x) = −0.5. Tiene dos soluciones en [0°, 360°): una en Q2 y otra en Q3. ¿Cuál es la MENOR solución positiva (en grados)? Respondé solo con el número.",
                "answer": "120°: referencia 60° en Q2 (180° − 60° = 120°) y en Q3 (180° + 60° = 240°); la menor es 120°.",
                "hints": ["Ángulo de referencia 60° ubicado en el 2.° cuadrante: 180° − 60°."],
                "payload": {"check": {"type": "numeric", "value": 120, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Factorizar una ecuación cuadrática en seno sin perder raíces",
                "prompt": "Resolvé 2·sen²(x) − sen(x) = 0 factorizando: sen(x)·(2·sen(x) − 1) = 0. ¿Cuántas soluciones TOTALES tiene en el intervalo [0°, 360°)? Respondé solo con el número.",
                "answer": "4 soluciones: de sen(x) = 0 salen 0° y 180°; de sen(x) = 0.5 salen 30° y 150° (¡por eso nunca dividas por sen(x)!).",
                "hints": ["Contá las soluciones de sen(x) = 0 (en [0°, 360°)) más las de sen(x) = 0.5."],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Ecuación con ángulo doble: sen(2x) = 1",
                "prompt": "Resolvé sen(2x) = 1 en [0°, 360°). Como 2x = 90° + 360°k → x = 45° + 180°k, salen dos soluciones: 45° y otra más. ¿Cuál es la segunda solución (en grados)? Respondé solo con el número.",
                "answer": "225°: sumamos el período reducido 180° a 45° → 45° + 180° = 225° (chequeo: sen(450°) = sen(90°) = 1).",
                "hints": ["Sumale 180° a la primera solución (45°)."],
                "payload": {"check": {"type": "numeric", "value": 225, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Aplicación real: cuándo alcanza la marea 4 metros",
                "prompt": "Una marea sigue h(t) = 2·sen((π/6)t) + 3 (t en horas). Para hallar cuándo llega a 4 m resolvemos sen((π/6)t) = 0.5. ¿En qué primera hora t > 0 ocurre? Respondé solo con el número.",
                "answer": "1 hora: dividiendo ambos lados por π/6 da t = 1 h (chequeo: 2·sen(30°) + 3 = 1 + 3 = 4 m).",
                "hints": ["sen(π/6) = 0.5, así que igualá (π/6) · t = π/6 y despejá t."],
                "payload": {"check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": "h"}},
            },
            {
                "item_type": "recall",
                "title": "Notación de solución general (+ 2πk vs. + πk)",
                "prompt": "¿Cuál es la expresión de TODAS las infinitas soluciones reales de tan(x) = 1 (con k entero)?",
                "answer": "x = π/4 + πk (45° + 180°k): como el período de la tangente es π (180°), las soluciones se repiten cada media vuelta.",
                "hints": ["Recordá que tan(x) tiene período π, no 2π."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "x = π/4 + πk",
                            "x = π/4 + 2πk",
                            "Solo x = π/4",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
]

TRIGONOMETRY_LESSONS: dict[str, dict] = {
    "t-reciprocas-referencia": {
        "hook": "No hace falta memorizar los 16 ángulos del círculo unitario: con 3 ángulos básicos (`30°`, `45°`, `60°`) y el ángulo de referencia podés calcular cualquiera de memoria.",
        "concept": {
            "points": [
                "Las **tres razones recíprocas** invierten las básicas (una sola 'co' por pareja): **`csc(θ) = 1/sen(θ)`**, **`sec(θ) = 1/cos(θ)`** y **`cot(θ) = 1/tan(θ) = cos(θ)/sen(θ)`**.",
                "El **ángulo de referencia** de cualquier ángulo `θ` es el ángulo agudo (`0°` a `90°`) que forma con el **eje horizontal X** (nunca con el eje Y!): Q2 → `180° − θ`, Q3 → `θ − 180°`, Q4 → `360° − θ`.",
                "Para evaluar en cualquier cuadrante: **1)** reducí vueltas extras (`± 360°`, ángulos coterminales), **2)** evaluá con el ángulo de referencia y **3)** poné el signo del cuadrante (`cos` = signo de `x`, `sen` = signo de `y`).",
            ],
            "real_world": [
                {
                    "title": "Navegación aérea y rumbos de 0° a 360°",
                    "detail": "Los rumbos de barcos y aviones cubren los 4 cuadrantes; los ángulos de referencia permiten proyectar velocidad al norte y al este al instante.",
                },
                {
                    "title": "Óptica y astronomía (secante)",
                    "detail": "La masa de aire que atraviesa la luz de una estrella al bajar hacia el horizonte crece proporcionalmente a `sec(z) = 1/cos(z)`.",
                },
                {
                    "title": "Cálculo integral y física avanzada",
                    "detail": "Escribir `1/cos(θ)` como `sec(θ)` y `1/sen(θ)` como `csc(θ)` simplifica fórmulas de derivadas, integrales y trayectorias.",
                },
            ],
            "key_rule": "csc = 1/sen | sec = 1/cos | cot = 1/tan | Ángulo de referencia: siempre contra el eje X (180° o 360°).",
            "pitfall": "Emparejar `sec` con `sen` porque ambos empiezan con 's': ¡es al revés! Cada par lleva una 'co' (seno↔cosecante, coseno↔secante).",
        },
        "example": {
            "title": "Calcular sen(210°) y sec(120°) sin calculadora",
            "steps": [
                "Para `210°` (3.er cuadrante): ángulo de referencia `210° − 180° = 30°`. Como `sen(30°) = 0.5` y en Q3 `y < 0`, queda `sen(210°) = −0.5`.",
                "Para `120°` (2.° cuadrante): referencia `180° − 120° = 60°`. Como `cos(60°) = 0.5` y en Q2 `x < 0`, queda `cos(120°) = −0.5`.",
                "Invertimos para obtener la secante: `sec(120°) = 1 / (−0.5) = −2`.",
            ],
            "lab_link": "math:trig_identities",
            "lab_cta": "Practicar recíprocas y ángulos de referencia en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es el ángulo de referencia de `315°` (4.° cuadrante)?",
            "options": [
                {"text": "`45°` (`360° − 315°`)", "ok": True, "feedback": "Exacto: está a 45° del eje X positivo."},
                {"text": "`35°`", "ok": False, "feedback": "Restaste mal: 360 − 315 = 45."},
                {"text": "`135°`", "ok": False, "feedback": "El ángulo de referencia siempre es agudo (menor a 90°)."},
            ],
        },
        "checks": [
            {
                "question": "Si `sen(θ) = 0.2` (`1/5`), ¿cuánto vale `csc(θ)`?",
                "options": [
                    {"text": "`5`", "ok": True, "feedback": "Exacto: csc(θ) = 1 / sen(θ) = 1 / 0.2 = 5."},
                    {"text": "`−0.2`", "ok": False, "feedback": "Recíproco significa 1 dividido el número, no cambiar el signo."},
                    {"text": "`0.8`", "ok": False, "feedback": "No es 1 − sen(θ), sino 1 ÷ sen(θ)."},
                ],
            },
            {
                "question": "¿Qué ángulo entre `0°` y `360°` es coterminal con `−60°`?",
                "options": [
                    {"text": "`300°` (`−60° + 360°`)", "ok": True, "feedback": "Exacto: girar 60° horario apunta al mismo lugar que girar 300° antihorario."},
                    {"text": "`60°`", "ok": False, "feedback": "60° está en Q1 y −60° está en Q4."},
                    {"text": "`120°`", "ok": False, "feedback": "Sumaste 180° en vez de una vuelta completa (360°)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá el truco para no confundir `sec` y `csc` y cómo hallás el ángulo de referencia en cualquier cuadrante.",
    },
    "t-desfase-tangente": {
        "hook": "El pico de calor del día no ocurre a las `00:00` ni el pico de marea al mediodía: el desfase (`C`) mueve la onda hasta la hora exacta donde sucede el máximo real.",
        "concept": {
            "points": [
                "Forma completa de una sinusoidal: **`y = A · sen(B(x − C)) + D`** (o `cos`). Para leer el **desfase `C`** SIEMPRE factorizá `B` primero (`sen(2x − π/2) = sen(2(x − π/4))` → desfase `π/4` derecha).",
                "Para modelar datos reales desde máximo y mínimo: **amplitud `A = (máx − mín)/2`**, **línea media `D = (máx + mín)/2`**, **`B = 2π / T`** y elegís `cos(B(t − t_pico))` centrando el desfase en la hora del pico.",
                "La función **`y = tan(x) = sen(x)/cos(x)`** tiene ramas crecientes repetidas cada **período `π` (`180°`)** (en `tan(Bx)` el período es `π/|B|`) y **asíntotas verticales** donde `cos(x) = 0` (`±π/2, ±3π/2, ...`).",
            ],
            "real_world": [
                {
                    "title": "Horas de luz solar y estaciones del año",
                    "detail": "Con un coseno desfasado al solsticio (`t_pico ≈ 21 de diciembre` en el sur) modelás con precisión cuántas horas de sol hay cada día del año.",
                },
                {
                    "title": "Audio estéreo y cancelación de ruido",
                    "detail": "Desfasar una onda exactamente medio período (`180°` o `π rad`) invierte su signo: sumada a la onda original se cancela (auriculares ANC!).",
                },
                {
                    "title": "Fases en corriente alterna trifásica",
                    "detail": "La red eléctrica industrial envía tres ondas sinusoidales iguales desfasadas `120°` entre sí para entregar potencia suave y constante.",
                },
            ],
            "key_rule": "Factorizá B para ver el desfase: A·cos(B(x − C)) + D | tan(Bx): período π/|B|, asíntotas donde cos = 0.",
            "pitfall": "Leer el desfase de `sen(2x − π/2)` como `π/2` en vez de `π/4`: siempre hay que sacar `B = 2` como factor común adentro del paréntesis.",
        },
        "example": {
            "title": "Modelar una temperatura diaria entre 12°C (03:00) y 28°C (15:00)",
            "steps": [
                "Línea media `D = (28 + 12)/2 = 20°C` y amplitud `A = (28 − 12)/2 = 8°C`.",
                "Período `T = 24 h` → `B = 2π / 24 = π / 12`.",
                "Como el coseno vale `+1` en `0`, desfasamos al pico `t = 15`: `T(t) = 8 · cos((π/12)(t − 15)) + 20`. Verificación en `t = 15`: `8·cos(0) + 20 = 28°C`!",
            ],
            "lab_link": "math:trig_waves",
            "lab_cta": "Practicar ondas y desfases en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es el desfase horizontal de `y = cos(4x − π/2)`?",
            "options": [
                {"text": "`π/8` hacia la derecha (`4(x − π/8)`)", "ok": True, "feedback": "Exacto: al sacar 4 como factor común queda 4(x − (π/2)/4) = 4(x − π/8)."},
                {"text": "`π/2` hacia la derecha", "ok": False, "feedback": "Te faltó dividir el π/2 por B = 4."},
                {"text": "`π/8` hacia la izquierda", "ok": False, "feedback": "Con signo menos adentro (x − π/8) se desplaza hacia la DERECHA."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál es el período de `y = tan(2x)` en radianes?",
                "options": [
                    {"text": "`π / 2`", "ok": True, "feedback": "Exacto: el período base de tangente es π, dividido por B = 2 da π/2."},
                    {"text": "`π`", "ok": False, "feedback": "Usaste 2π/2 en vez de π/2: la tangente tiene período base π, no 2π."},
                    {"text": "`2π`", "ok": False, "feedback": "Multiplicaste `π × 2` en vez de dividir (o usaste el período del seno, `2π`, sin dividir por `B`)."},
                ],
            },
            {
                "question": "Si sumás una onda `sen(x)` con la misma onda desfasada `180°` (`sen(x − 180°) = −sen(x)`), ¿qué pasa?",
                "options": [
                    {"text": "Se cancelan completamente (`0`, interferencia destructiva)", "ok": True, "feedback": "Exacto: es el principio físico de los auriculares con cancelación activa de ruido."},
                    {"text": "Se duplica la amplitud", "ok": False, "feedback": "Se duplica cuando el desfase es 0° o 360° (en fase)."},
                    {"text": "Se duplica la frecuencia", "ok": False, "feedback": "Desfasar no cambia la frecuencia B."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá los 4 pasos para construir la fórmula `A·cos(B(t − C)) + D` a partir de la hora del máximo y del mínimo de un ciclo real.",
    },
    "t-leyes-senos-cosenos": {
        "hook": "Casi ningún terreno, ruta de avión o estructura real tiene un ángulo cómodo de `90°`: la Ley de senos y la Ley de cosenos te dejan resolver CUALQUIER triángulo.",
        "concept": {
            "points": [
                "**Ley de senos**: **`a / sen(A) = b / sen(B) = c / sen(C)`**. Usala cuando tenés una **pareja opuesta completa** (un ángulo y el lado de enfrente: `ALA`, `AAL`, `LLA`). Ojo en `LLA`: puede haber **2 triángulos** porque `sen(θ) = sen(180° − θ)`.",
                "**Ley de cosenos**: **`c² = a² + b² − 2ab·cos(C)`**. Usala en **`LAL`** (dos lados y el ángulo entre ellos) o **`LLL`** (los 3 lados). Es Pitágoras generalizado: si `C = 90°`, `cos(90°) = 0` y vuelve a ser `a² + b² = c²`.",
                "**Área trigonométrica**: **`Área = (1/2) · a · b · sen(C)`**, usando dos lados cualquiera y el ángulo comprendido (evita tener que calcular la altura).",
            ],
            "real_world": [
                {
                    "title": "Triangulación en topografía y navegación costera",
                    "detail": "Midiendo los ángulos desde dos estaciones separadas una distancia conocida (`ALA`) y la Ley de senos calcula la distancia a un barco o pico inaccesible.",
                },
                {
                    "title": "Navegación aérea con viento cruzado",
                    "detail": "Sumar el vector velocidad del avión y el vector viento formando un ángulo `C` usa directamente la Ley de cosenos.",
                },
                {
                    "title": "Cálculo de superficie de terrenos irregulares",
                    "detail": "Los agrimensores dividen un lote en triángulos y aplican `(1/2)ab·sen(C)` sin tener que medir alturas perpendiculares.",
                },
            ],
            "key_rule": "Pareja opuesta (ALA/AAL/LLA) → Ley de senos | LAL o LLL → Ley de cosenos (c² = a² + b² − 2ab·cos C) | Área = ½ab·sen C.",
            "pitfall": "Olvidar el signo de `cos(C)` cuando `C > 90°`: como el coseno es negativo, `−2ab·cos(C)` se vuelve POSITIVO (el lado opuesto a un ángulo obtuso es más largo que con Pitágoras).",
        },
        "example": {
            "title": "Distancia entre dos barcos a 60° (5 km y 8 km) y área formada",
            "steps": [
                "Conocemos dos lados (`a = 5`, `b = 8`) y el ángulo entre ellos (`C = 60°`) → caso `LAL` → **Ley de cosenos**.",
                "Sustituimos con `cos(60°) = 0.5`: `c² = 5² + 8² − 2(5)(8)(0.5) = 25 + 64 − 40 = 49` → `c = 7 km`.",
                "Si quisiéramos el área del triángulo formado: `Área = (1/2)(5)(8)·sen(60°) = 20 · (√3/2) ≈ 17.3 km²`.",
            ],
            "lab_link": "math:oblique_triangles",
            "lab_cta": "Practicar Ley de senos y cosenos en el Laboratorio",
        },
        "check": {
            "question": "¿Qué ocurre con la Ley de cosenos `c² = a² + b² − 2ab·cos(C)` cuando el ángulo `C` mide exactamente `90°`?",
            "options": [
                {"text": "Se reduce exactamente al Teorema de Pitágoras (`c² = a² + b²`)", "ok": True, "feedback": "Exacto: cos(90°) = 0 anula el tercer término."},
                {"text": "Da `c² = a² + b² − 2ab`", "ok": False, "feedback": "Eso pasa cuando cos(C) = 1 (C = 0°), no en 90°."},
                {"text": "No se puede aplicar en triángulos rectángulos", "ok": False, "feedback": "Funciona en TODOS los triángulos, incluidos los rectángulos."},
            ],
        },
        "checks": [
            {
                "question": "Conocés dos ángulos (`A = 40°`, `B = 75°`) y el lado `a = 12 m`. ¿Qué herramienta elegís para hallar el lado `b`?",
                "options": [
                    {"text": "Ley de senos (`12 / sen 40° = b / sen 75°`)", "ok": True, "feedback": "Exacto: ya tenés la pareja completa (a y A)."},
                    {"text": "Ley de cosenos", "ok": False, "feedback": "La Ley de cosenos necesita al menos dos lados conocidos."},
                    {"text": "SOH-CAH-TOA directo", "ok": False, "feedback": "El tercer ángulo es 65° (ninguno es 90°), así que no es triángulo rectángulo."},
                ],
            },
            {
                "question": "Un triángulo tiene lados `6 m` y `10 m` con un ángulo de `30°` entre ellos (`sen 30° = 0.5`). ¿Cuál es su área?",
                "options": [
                    {"text": "`15 m²` (`0.5 × 6 × 10 × 0.5`)", "ok": True, "feedback": "Exacto: (1/2)ab·sen(30°) = 30 × 0.5 = 15 m²."},
                    {"text": "`30 m²`", "ok": False, "feedback": "30 m² sería si el ángulo fuera 90° (sen 90° = 1); te faltó multiplicar por sen(30°) = 0.5."},
                    {"text": "`60 m²`", "ok": False, "feedback": "Te faltaron tanto el 1/2 como el sen(30°)."},
                ],
            },
        ],
        "takeaway_prompt": "Resumí en dos líneas cómo decidís al instante si usar Ley de senos o Ley de cosenos en un triángulo no rectángulo.",
    },
    "t-inversas-restringidas": {
        "hook": "Si le preguntás a tu calculadora `arcsen(0.5)` te responde `30°`, nunca `150°` ni `390°`. Entender por qué evita errores silenciosos al resolver ángulos.",
        "concept": {
            "points": [
                "Como `sen`, `cos` y `tan` son periódicas, infinitos ángulos dan el mismo valor. Para que la inversa devuelva **una única respuesta**, restringimos su salida a una rama principal:",
                "**`arcsen(x)`** devuelve ángulos en **`[−90°, +90°]`** (`[−π/2, π/2]`); **`arctan(x)`** en **`(−90°, +90°)`**; y **`arccos(x)`** en **`[0°, 180°]`** (`[0, π]`) porque `cos` es positivo en Q4 y Q1.",
                "El dominio de `arcsen` y `arccos` es solo **`[−1, 1]`**. Y para calcular expresiones como **`cos(arcsen(3/5))`**, dibujás un triángulo rectángulo con `Op = 3, Hip = 5` → `Ady = 4` → `cos = 4/5`.",
            ],
            "real_world": [
                {
                    "title": "Robótica y cinemática inversa (`atan2`)",
                    "detail": "Para apuntar un brazo robótico o cámara a `(x, y)`, se usa `arctan` ajustado al cuadrante correcto (`atan2`) para no errar por `180°`.",
                },
                {
                    "title": "Cálculo de ángulos en rampas y videojuegos",
                    "detail": "Hallar el ángulo entre dos vectores `u` y `v` usa `arccos((u·v)/(|u||v|))`, que funciona perfecto justamente porque `arccos` cubre de `0°` a `180°`.",
                },
                {
                    "title": "Detectar errores de geometría imposible",
                    "detail": "Si un cálculo físico te pide `arcsen(1.2)`, el dominio `[−1, 1]` te avisa de inmediato que ese rayo de luz sufre reflexión total interna o el triángulo no cierra.",
                },
            ],
            "key_rule": "arcsen ∈ [−90°, 90°] | arctan ∈ (−90°, 90°) | arccos ∈ [0°, 180°] | Dominio de arcsen/arccos = [−1, 1].",
            "pitfall": "Asumir que `arcsen(sen(θ))` siempre vale `θ`: solo vale `θ` si `θ` cae dentro de `[−90°, 90°]` (ej. `arcsen(sen(150°)) = 30°`).",
        },
        "example": {
            "title": "Evaluar arccos(−0.5) y tan(arccos(5/13))",
            "steps": [
                "Para `arccos(−0.5)`: buscamos en `[0°, 180°]` dónde `cos` es `−0.5` → 2.° cuadrante, referencia `60°` → `180° − 60° = 120°`.",
                "Para `tan(arccos(5/13))`: llamamos `θ = arccos(5/13)` (Q1 porque `5/13 > 0`), con `Ady = 5` y `Hip = 13`.",
                "Por Pitágoras `Op = √(13² − 5²) = 12`, así que `tan(θ) = Op / Ady = 12 / 5 = 2.4`.",
            ],
            "lab_link": "math:trig_identities",
            "lab_cta": "Practicar inversas e identidades en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es el rango de ángulos que devuelve `arccos(x)`?",
            "options": [
                {"text": "`[0°, 180°]` (`[0, π]`)", "ok": True, "feedback": "Exacto: en [0°, 180°] el coseno recorre todos los valores desde +1 hasta −1 sin repetirse."},
                {"text": "`[−90°, +90°]`", "ok": False, "feedback": "Ese es el rango de arcsen; en [−90°, 90°] el coseno nunca es negativo."},
                {"text": "`[0°, 360°]`", "ok": False, "feedback": "En una vuelta completa cada valor se repite dos veces, así que no sería función."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuánto vale `arccos(cos(−60°))`?",
                "options": [
                    {"text": "`60°`", "ok": True, "feedback": "Exacto: cos(−60°) = 0.5, y el único ángulo en [0°, 180°] con coseno 0.5 es +60°."},
                    {"text": "`−60°`", "ok": False, "feedback": "−60° cae fuera del rango principal [0°, 180°] de arccos."},
                    {"text": "`120°`", "ok": False, "feedback": "cos(120°) = −0.5, no +0.5."},
                ],
            },
            {
                "question": "Si `θ = arcsen(5/13)`, ¿cuánto vale `cos(θ)`?",
                "options": [
                    {"text": "`12/13`", "ok": True, "feedback": "Exacto: triángulo 5-12-13 en Q1 → Ady = 12, Hip = 13 → cos = 12/13."},
                    {"text": "`8/13`", "ok": False, "feedback": "Restaste 13 − 5 en vez de usar Pitágoras √(13² − 5²) = 12."},
                    {"text": "`5/12`", "ok": False, "feedback": "5/12 es tan(θ), no cos(θ)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué `arccos` usa el intervalo `[0°, 180°]` mientras que `arcsen` usa `[−90°, 90°]`.",
    },
    "t-identidades-angulo-doble": {
        "hook": "Las identidades trigonométricas son atajos algebraicos que convierten fórmulas imposibles en expresiones de dos términos (y te dejan hallar `sen(75°)` o `sen(2θ)` de manera exacta).",
        "concept": {
            "points": [
                "**Pitagóricas derivadas** (dividiendo `sen² + cos² = 1` por `cos²` o `sen²`): **`1 + tan²(θ) = sec²(θ)`** y **`1 + cot²(θ) = csc²(θ)`**. Paridad: **`cos(−θ) = cos(θ)`**, **`sen(−θ) = −sen(θ)`**.",
                "**Suma y resta de ángulos**: **`sen(α ± β) = sen α·cos β ± cos α·sen β`** y **`cos(α ± β) = cos α·cos β ∓ sen α·sen β`** (¡en coseno el signo se invierte!).",
                "**Ángulo doble** (poniendo `α = β = θ`): **`sen(2θ) = 2·sen(θ)·cos(θ)`** y **`cos(2θ) = cos²(θ) − sen²(θ) = 1 − 2·sen²(θ) = 2·cos²(θ) − 1`**.",
            ],
            "real_world": [
                {
                    "title": "Alcance máximo de un tiro parabólico (`45°`)",
                    "detail": "El alcance es proporcional a `2·sen(θ)·cos(θ) = sen(2θ)`, que alcanza su máximo exacto cuando `2θ = 90°` → `θ = 45°`!",
                },
                {
                    "title": "Modulación de radio AM/FM y batidos en audio",
                    "detail": "Al mezclar dos ondas sonoras o señales de radio, las identidades de suma de ángulos explican la aparición de frecuencias suma y diferencia.",
                },
                {
                    "title": "Matrices de rotación en gráficos 2D/3D",
                    "detail": "Rotar un punto `(x, y)` un ángulo `β` se deduce en 2 renglones aplicando `cos(α + β)` y `sen(α + β)`.",
                },
            ],
            "key_rule": "1 + tan² = sec² | sen(2θ) = 2·sen θ·cos θ | cos(2θ) = cos²θ − sen²θ | Truco para simplificar: pasá todo a sen y cos.",
            "pitfall": "Escribir `sen(2θ) = 2·sen(θ)` o `cos(α + β) = cos α + cos β`: las funciones trigonométricas NO son lineales, nunca se saca el 2 ni se distribuye.",
        },
        "example": {
            "title": "Calcular sen(2θ) y cos(2θ) a partir de sen(θ) y cos(θ)",
            "steps": [
                "Dado `sen(θ) = 3/5 = 0.6` y `cos(θ) = 4/5 = 0.8` en Q1:",
                "`sen(2θ) = 2 · (0.6) · (0.8) = 0.96` (casi 1 porque `2θ ≈ 73.7°`).",
                "`cos(2θ) = 0.8² − 0.6² = 0.64 − 0.36 = 0.28`. Comprobación pitagórica: `0.96² + 0.28² = 0.9216 + 0.0784 = 1` exacto!",
            ],
            "lab_link": "math:trig_identities",
            "lab_cta": "Practicar identidades y ángulo doble en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál de estas identidades se obtiene dividiendo `sen²(θ) + cos²(θ) = 1` por `cos²(θ)`?",
            "options": [
                {"text": "`tan²(θ) + 1 = sec²(θ)`", "ok": True, "feedback": "Exacto: sen²/cos² = tan², cos²/cos² = 1 y 1/cos² = sec²."},
                {"text": "`tan²(θ) + 1 = csc²(θ)`", "ok": False, "feedback": "1/cos² es sec², no csc²."},
                {"text": "`cot²(θ) + 1 = sec²(θ)`", "ok": False, "feedback": "Dividir por sen² da 1 + cot² = csc²."},
            ],
        },
        "checks": [
            {
                "question": "Simplificá `sen(θ) · csc(θ) − cos²(θ)`:",
                "options": [
                    {"text": "`sen²(θ)` (porque `sen · (1/sen) = 1`, y `1 − cos² = sen²`)", "ok": True, "feedback": "Exacto: pasar csc a 1/sen deja 1 − cos²(θ) = sen²(θ)."},
                    {"text": "`cos²(θ)`", "ok": False, "feedback": "1 − cos²(θ) equivale a sen²(θ), no a cos²(θ)."},
                    {"text": "`0`", "ok": False, "feedback": "Solo valdría 0 cuando sen(θ) = 0 (y ahí csc ni existe)."},
                ],
            },
            {
                "question": "Si `sen(θ) = 0.5`, usá `cos(2θ) = 1 − 2·sen²(θ)` para calcular `cos(2θ)`:",
                "options": [
                    {"text": "`0.5` (`1 − 2(0.25) = 0.5`)", "ok": True, "feedback": "Exacto: si θ = 30°, 2θ = 60° y efectivamente cos(60°) = 0.5!"},
                    {"text": "`0` (`1 − 2(0.5)`)", "ok": False, "feedback": "Te faltó elevar sen(θ) = 0.5 al cuadrado (0.25)."},
                    {"text": "`−0.5`", "ok": False, "feedback": "1 − 0.5 = +0.5."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá el truco más útil para demostrar o simplificar una identidad trigonométrica cuando no sabés por dónde empezar.",
    },
    "t-ecuaciones-trigonometricas": {
        "hook": "En una ecuación algebraica común `2x = 1` hay una sola solución; en `2·sen(x) = 1` la onda vuelve a pasar por `0.5` infinitas veces (dos veces por cada vuelta!).",
        "concept": {
            "points": [
                "Pasos base: **1)** despejá la razón trigonométrica (aislándola o **factorizando** sin dividir por `sen(x)` o `cos(x)` para no perder soluciones), **2)** hallá TODAS las soluciones en `[0°, 360°)` usando los cuadrantes correctos.",
                "Por simetría en el círculo unitario: para **seno**, la segunda solución es **`180° − θ`** (`π − θ`); para **coseno**, es **`360° − θ`** (`2π − θ`); para **tangente**, es **`θ + 180°`** (`θ + π`).",
                "**Solución general**: sumá `+ 360°k` (`+ 2πk`) para seno/coseno y `+ 180°k` (`+ πk`) para tangente. Con argumentos múltiples como `sen(2x) = 1`, **sumá `+ 360°k` ANTES de dividir por 2** (`x = 45° + 180°k`).",
            ],
            "real_world": [
                {
                    "title": "Ventanas horarias de marea alta para zarpar",
                    "detail": "Resolver `h(t) = 4 m` en una curva sinusoidal te da la hora exacta de entrada y de salida en que el agua supera el calado del barco.",
                },
                {
                    "title": "Cruces por cero en electrónica de potencia (dimmers)",
                    "detail": "Los reguladores de luz esperan los instantes exactos donde el voltaje `V(t) = V₀·sen(ωt)` cruza por `0` para conmutar sin chispa.",
                },
                {
                    "title": "Citas solares y fases orbitales",
                    "detail": "Predecir todos los días del año en que la duración del día supera las 14 horas es resolver una ecuación cosenoidal.",
                },
            ],
            "key_rule": "Buscá los 2 cuadrantes por vuelta → sumá +360°k (+180°k para tan) ANTES de dividir por B → factorizá, nunca dividas por sen(x).",
            "pitfall": "Dividir ambos lados de `2·sen²(x) = sen(x)` por `sen(x)`: borrás de un plumazo todas las soluciones donde `sen(x) = 0` (`0°` y `180°`).",
        },
        "example": {
            "title": "Resolver 2·cos²(x) − cos(x) = 0 en [0°, 360°)",
            "steps": [
                "Sacamos factor común `cos(x)` (NO dividimos!): `cos(x) · (2·cos(x) − 1) = 0`.",
                "Rama 1: `cos(x) = 0` → `x = 90°` y `x = 270°`.",
                "Rama 2: `cos(x) = 0.5` → Q1 y Q4 → `x = 60°` y `x = 360° − 60° = 300°`. Total: 4 soluciones (`60°, 90°, 270°, 300°`).",
            ],
            "lab_link": "math:trig_identities",
            "lab_cta": "Practicar trigonometría en el Laboratorio",
        },
        "check": {
            "question": "Si `cos(x) = 0.5`, además de `x = 60°`, ¿cuál es la otra solución en `[0°, 360°)`?",
            "options": [
                {"text": "`300°` (4.° cuadrante, `360° − 60°`)", "ok": True, "feedback": "Exacto: el coseno (x) es positivo en Q1 y Q4."},
                {"text": "`120°` (2.° cuadrante)", "ok": False, "feedback": "En 120° el coseno es −0.5 (negativo), no +0.5."},
                {"text": "`240°` (3.er cuadrante)", "ok": False, "feedback": "En 240° el coseno también es negativo (−0.5)."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuántas soluciones tiene `cos(3x) = 0` en el intervalo `[0°, 360°)`?",
                "options": [
                    {"text": "`6` soluciones (el triple de las 2 que tiene `cos(x) = 0`)", "ok": True, "feedback": "Exacto: cos(3x) da 3 ciclos completos en 360°, y cruza cero 2 veces por ciclo → 6 soluciones."},
                    {"text": "`2` soluciones (`90°` y `270°`)", "ok": False, "feedback": "Te faltó dividir también el período 360° por 3 (aparecen soluciones cada 60° desde 30°)."},
                    {"text": "`3` soluciones", "ok": False, "feedback": "Cada ciclo tiene 2 ceros, no 1."},
                ],
            },
            {
                "question": "Para resolver `sen²(x) = sen(x)`, ¿cuál es el primer paso seguro?",
                "options": [
                    {"text": "Pasar todo a un lado y factorizar: `sen(x)(sen(x) − 1) = 0`", "ok": True, "feedback": "Exacto: así conservás tanto sen(x) = 0 como sen(x) = 1."},
                    {"text": "Dividir ambos lados por `sen(x)` para quedar `sen(x) = 1`", "ok": False, "feedback": "Dividir por sen(x) hace desaparecer las soluciones x = 0° y x = 180°."},
                    {"text": "Sacar raíz cuadrada directo", "ok": False, "feedback": "Igual deja √(sen x), que no simplifica nada."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá el truco de los dos cuadrantes para hallar todas las soluciones de `sen(x) = c` y `cos(x) = c` en una vuelta.",
    },
}
