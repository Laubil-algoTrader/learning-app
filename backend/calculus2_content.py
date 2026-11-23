"""Calculus 2 (AP Calculus BC) curriculum (7 units, #85-#91) adapted from Khan Academy.

Covers every AP Calculus BC / Calculus 2 extension building on Cálculo 1 (#77-#84):
  - Integration by parts (LIATE) & partial fraction decomposition
  - Improper integrals (infinite bounds & vertical asymptotes) & arc length
  - Euler's numerical method & logistic growth models (carrying capacity & K/2)
  - Parametric equations & 2D vector-valued motion (speed, velocity, acceleration)
  - Polar coordinates calculus: polar curves, slopes & wedge areas (1/2 ∫ r² dθ)
  - Infinite series & convergence tests (nth-term, p-series, alternating, ratio)
  - Power series, Taylor & Maclaurin polynomials, radius of convergence & Euler's Formula
"""

from __future__ import annotations

CALCULUS2_NODES: list[dict] = [
    # ==================== NIVEL 31: INTEGRACIÓN AVANZADA, EULER Y LOGÍSTICO ====================
    {
        "slug": "c2-partes-fracciones",
        "title": "85. Integración por partes y fracciones parciales",
        "level": 31,
        "order_index": 85,
        "summary": "Invertir la regla del producto con ∫ u dv = uv − ∫ v du (LIATE) y partir fracciones racionales para integrar con logaritmos.",
        "prerequisites": ["c1-integrales-tfc"],
        "metadata": {"section": "Cálculo 2", "lab_tab": "integrals_adv", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Integración por partes en ∫(0 a 1) x · eˣ dx",
                "prompt": "Calculá ∫(de 0 a 1) x·eˣ dx usando integración por partes con u = x y dv = eˣ dx. Respondé solo con el número.",
                "answer": "1: ∫ x·eˣ dx = x·eˣ − eˣ; al evaluar de 0 a 1, el límite superior (e − e) da 0 y el inferior (0 − 1) da −1, así que 0 − (−1) = 1 exacto!",
                "hints": ["∫ u dv = u·v − ∫ v du, con du = dx y v = eˣ.", "La primitiva es x·eˣ − eˣ; evaluala en 1 y en 0 recordando que e⁰ = 1."],
                "payload": {
                    "lab_link": "math:integrals_adv",
                    "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Elegir u con el orden LIATE en ∫ x · ln(x) dx",
                "prompt": "Para resolver ∫ x · ln(x) dx por partes, ¿qué conviene elegir como u (la parte que derivás) siguiendo la prioridad LIATE?",
                "answer": "u = ln(x) (Logarítmica va antes que Algebraica): su derivada es 1/x, que se simplifica limpio con la integral de x (x²/2).",
                "hints": ["LIATE: Logarítmicas → Inversas trig → Algebraicas → Trigonométricas → Exponenciales."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "u = ln(x) y dv = x dx",
                            "u = x y dv = ln(x) dx",
                            "u = x · ln(x) y dv = dx",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Antiderivada clásica de ln(x) por partes",
                "prompt": "Tomando u = ln(x) y dv = 1 dx en ∫ u dv = uv − ∫ v du, ¿qué antiderivada se obtiene para ∫ ln(x) dx?",
                "answer": "x·ln(x) − x + C (comprobación derivando: 1·ln(x) + x·(1/x) − 1 = ln(x)!).",
                "hints": ["Aplicá uv − ∫ v du con v = x y du = (1/x) dx."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["x·ln(x) − x + C", "1/x + C", "x·ln(x) + C"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Descomposición en fracciones parciales (hallar A)",
                "prompt": "Para integrar 5 / ((x − 1)(x + 4)), la separás en A/(x − 1) + B/(x + 4) → 5 = A(x + 4) + B(x − 1). Sustituyendo x = 1 para anular B, ¿cuánto vale A? Respondé solo con el número.",
                "answer": "1: 5 = A(5) + 0 → A = 1 (y probando x = −4 sale B = −1, dejando ∫ [1/(x − 1) − 1/(x + 4)] dx).",
                "hints": ["Reemplazá x = 1 en 5 = A(x + 4) + B(x − 1)."],
                "payload": {"check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Fracciones parciales con numerador 6",
                "prompt": "Descomponé 6 / ((x − 1)(x + 2)) = A/(x − 1) + B/(x + 2) → 6 = A(x + 2) + B(x − 1). Evaluando en x = −2, ¿cuánto vale B (con signo)? Respondé solo con el número.",
                "answer": "−2: 6 = A(0) + B(−3) → B = 6 / (−3) = −2 (y A = +2).",
                "hints": ["Sustituí x = −2 en 6 = A(x + 2) + B(x − 1)."],
                "payload": {"check": {"type": "numeric", "value": -2, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Integrar una vez separadas las fracciones parciales",
                "prompt": "Una vez reescrita la fracción como 2/(x − 1) − 2/(x + 2), ¿cuál es su integral indefinida?",
                "answer": "2·ln|x − 1| − 2·ln|x + 2| + C (cada fracción simple 1/(x − a) integra directo a ln|x − a|).",
                "hints": ["Recordá que ∫ 1/(x − a) dx = ln|x − a| + C."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "2·ln|x − 1| − 2·ln|x + 2| + C",
                            "−2/(x − 1)² + 2/(x + 2)² + C",
                            "2·ln|(x − 1)(x + 2)| + C",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "c2-impropias-longitud",
        "title": "86. Integrales impropias y longitud de arco",
        "level": 31,
        "order_index": 86,
        "summary": "Áreas finitas sobre intervalos infinitos (∫ 1/x^p dx), asíntotas dentro de la integral y medir el largo real de una curva.",
        "prerequisites": ["c2-partes-fracciones", "c1-aplicaciones-integrales"],
        "metadata": {"section": "Cálculo 2", "lab_tab": "integrals_adv", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Integral impropia convergente hasta infinito",
                "prompt": "Evaluá ∫(de 1 a ∞) (6 / x²) dx tomando lim(b → ∞) [−6 / x] de 1 a b. Respondé solo con el número.",
                "answer": "6: cuando b → ∞, −6/b → 0, así que queda 0 − (−6/1) = 6 (un tramo infinito encierra área finita!).",
                "hints": ["Evaluá 0 − (−6 / 1)."],
                "payload": {
                    "lab_link": "math:integrals_adv",
                    "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Integral impropia con potencia cúbica (p = 3)",
                "prompt": "Calculá ∫(de 1 a ∞) (8 / x³) dx = lim(b → ∞) [−4 / x²] de 1 a b. Respondé solo con el número.",
                "answer": "4: 0 − (−4 / 1²) = 4.",
                "hints": ["La antiderivada de 8x⁻³ es −4x⁻²; evaluá 0 − (−4)."],
                "payload": {
                    "lab_link": "math:integrals_adv",
                    "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "El umbral p = 1 para ∫(1 a ∞) 1 / x^p dx",
                "prompt": "¿Para qué valores del exponente p CONVERGE a un área finita la integral impropia ∫(de 1 a ∞) (1 / x^p) dx?",
                "answer": "Únicamente cuando p > 1: en p = 1 (∫ 1/x dx = ln(b) → ∞) diverge lentamente hacia infinito.",
                "hints": ["1/x² converge (p = 2), pero 1/x (p = 1) y 1/√x (p = 0.5) divergen."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Solo cuando p > 1",
                            "Para todo p > 0",
                            "Solo cuando p ≥ 1",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Integral impropia con asíntota vertical en x = 0",
                "prompt": "Aunque 1 / √x se dispara a infinito en x = 0, evaluá ∫(de 0 a 1) (1 / √x) dx = lim(a → 0⁺) [2√x] de a a 1. Respondé solo con el número.",
                "answer": "2: 2√1 − 2√0 = 2 (sí converge a un área finita!).",
                "hints": ["Evaluá 2√1 − 0."],
                "payload": {
                    "lab_link": "math:integrals_adv",
                    "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Longitud de arco usando L = ∫ √(1 + [f'(x)]²) dx",
                "prompt": "Para la recta y = (3/4)x + 2 en [0, 4], f'(x) = 3/4 y √(1 + 9/16) = 5/4. Calculá su longitud de arco ∫(de 0 a 4) (5/4) dx. Respondé solo con el número.",
                "answer": "5: (5/4) × 4 = 5 (coincide exacto con Pitágoras sobre Δx = 4, Δy = 3!).",
                "hints": ["Multiplicá la constante 5/4 por el ancho del intervalo (4)."],
                "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "De dónde sale la fórmula de longitud de arco",
                "prompt": "En L = ∫ √(1 + [f'(x)]²) dx, ¿de qué teorema geométrico proviene la raíz cuadrada?",
                "answer": "Del Teorema de Pitágoras aplicado a cada mini-segmento: ds = √(dx² + dy²) = √(1 + (dy/dx)²) dx.",
                "hints": ["Pensá en la hipotenusa de un triangulito diminuto de catetos dx y dy."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "De Pitágoras en cada tramo infinitesimal ds = √(dx² + dy²)",
                            "De la fórmula del área del círculo πr²",
                            "De la regla del cociente",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "c2-euler-logistico",
        "title": "87. Método de Euler y crecimiento logístico",
        "level": 31,
        "order_index": 87,
        "summary": "Aproximar ecuaciones diferenciales paso a paso con rectas tangentes (Euler) y modelar poblaciones con techo (capacidad de carga K).",
        "prerequisites": ["c1-ecuaciones-diferenciales"],
        "metadata": {"section": "Cálculo 2", "lab_tab": "integrals_adv", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Primer paso del Método de Euler",
                "prompt": "Dada dy/dx = x + y con punto inicial (0, 1) y paso Δx = 0.5, la pendiente inicial es 0 + 1 = 1. Calculá y₁ = y₀ + Δx · pendiente en x₁ = 0.5. Respondé solo con el número.",
                "answer": "1.5: y₁ = 1 + 0.5 × 1 = 1.5 (en el punto (0.5, 1.5)).",
                "hints": ["Usá y₁ = 1 + 0.5 × (0 + 1)."],
                "payload": {
                    "lab_link": "math:integrals_adv",
                    "check": {"type": "numeric", "value": 1.5, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Segundo paso del Método de Euler",
                "prompt": "Siguiendo el mismo problema (dy/dx = x + y, Δx = 0.5) desde (0.5, 1.5): la nueva pendiente es 0.5 + 1.5 = 2. ¿Qué valor y₂ estima Euler en x = 1.0? Respondé solo con el número.",
                "answer": "2.5: y₂ = 1.5 + 0.5 × 2 = 2.5 (recalculando la tangente en cada escalón).",
                "hints": ["Calculá 1.5 + 0.5 × 2."],
                "payload": {
                    "lab_link": "math:integrals_adv",
                    "check": {"type": "numeric", "value": 2.5, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Cuándo sobreestima o subestima el Método de Euler",
                "prompt": "Si la curva solución exacta es cóncava hacia ARRIBA (y'' > 0) en todo el tramo, ¿las aproximaciones del Método de Euler quedan por encima o por debajo del valor real?",
                "answer": "Por DEBAJO (subestiman): en una curva cóncava hacia arriba (∪), cada recta tangente pasa siempre por debajo de la curva.",
                "hints": ["Dibujá una parábola feliz (∪) y trazá una tangente: ¿queda arriba o abajo?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Por debajo (subestiman el valor real)",
                            "Por encima (sobreestiman el valor real)",
                            "Son siempre exactas sin error",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Leer la capacidad de carga K en un modelo logístico",
                "prompt": "Una población de peces sigue la ecuación logística dP/dt = 0.2 · P · (1 − P / 500). ¿Cuál es la capacidad de carga K (población límite a largo plazo)? Respondé solo con el número.",
                "answer": "500 peces: cuando P = 500 el factor (1 − 500/500) = 0, así que el crecimiento se estabiliza ahí.",
                "hints": ["Buscá el valor de P que anula el paréntesis (1 − P/500)."],
                "payload": {
                    "lab_link": "math:integrals_adv",
                    "check": {"type": "numeric", "value": 500, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Población donde el crecimiento logístico es MÁS RÁPIDO",
                "prompt": "En el mismo modelo dP/dt = 0.2 · P · (1 − P / 500), ¿para qué cantidad de peces P crece la población a su velocidad MÁXIMA (punto de inflexión)? Respondé solo con el número.",
                "answer": "250 peces: en todo modelo logístico, dP/dt alcanza su máximo exactamente a la mitad de la capacidad de carga (P = K / 2 = 250).",
                "hints": ["Dividí la capacidad de carga K = 500 por 2."],
                "payload": {
                    "lab_link": "math:integrals_adv",
                    "check": {"type": "numeric", "value": 250, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Extraer la capacidad de carga K desde forma expandida",
                "prompt": "Una epidemia sigue dP/dt = 0.4P − 0.0005P². Escrita en forma logística es r·P·(1 − P/K). ¿Cuánto vale la capacidad de carga K? Respondé solo con el número.",
                "answer": "800: factorizando 0.4P queda 0.4P(1 − P/800). También sale de pedir dP/dt = 0 con P > 0: 0.4 − 0.0005P = 0 → P = 0.4 / 0.0005 = 800.",
                "hints": ["K es la población donde el crecimiento se frena: dP/dt = 0 con P > 0.", "Igualá 0.4 − 0.0005P = 0 y despejá P."],
                "payload": {"check": {"type": "numeric", "value": 800, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    # ==================== NIVEL 32: PARAMÉTRICAS, VECTORES Y POLARES ====================
    {
        "slug": "c2-parametricas-vectores",
        "title": "88. Curvas paramétricas y movimiento vectorial 2D",
        "level": 32,
        "order_index": 88,
        "summary": "Pendiente dy/dx = (dy/dt)/(dx/dt), velocidad y aceleración vectoriales, rapidez instantánea √(x'² + y'²) y distancia recorrida.",
        "prerequisites": ["pc-vectores", "c2-impropias-longitud"],
        "metadata": {"section": "Cálculo 2", "lab_tab": "parametric_series", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Pendiente dy/dx de una curva paramétrica",
                "prompt": "Una partícula sigue x(t) = t² e y(t) = t³ − 3t (así dx/dt = 2t y dy/dt = 3t² − 3). Usando dy/dx = (dy/dt) / (dx/dt), ¿cuál es la pendiente en t = 2 en decimal? Respondé solo con el número.",
                "answer": "2.25 (9/4): en t = 2, dy/dt = 12 − 3 = 9 y dx/dt = 4 → 9 / 4 = 2.25.",
                "hints": ["Dividí dy/dt = 3(2²) − 3 por dx/dt = 2(2)."],
                "payload": {
                    "lab_link": "math:parametric_series",
                    "check": {"type": "numeric", "value": 2.25, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Rapidez instantánea 2D desde el vector posición",
                "prompt": "Un dron sigue r(t) = ⟨3t², 4t²⟩ (m), así su vector velocidad es v(t) = ⟨6t, 8t⟩. ¿Cuál es su rapidez instantánea |v(1)| = √(x'² + y'²) en t = 1 s (en m/s)? Respondé solo con el número.",
                "answer": "10 m/s: v(1) = ⟨6, 8⟩ → |v(1)| = √(36 + 64) = 10 m/s.",
                "hints": ["Evaluá v(1) = ⟨6, 8⟩ y sacá su magnitud con Pitágoras."],
                "payload": {
                    "lab_link": "math:parametric_series",
                    "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "m/s"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Distancia total recorrida integrando la rapidez",
                "prompt": "Una partícula se mueve con x(t) = 3t e y(t) = 4t (en metros, con t en segundos). Calculá la distancia recorrida entre t = 0 y t = 4: ∫(de 0 a 4) √(x'² + y'²) dt. Respondé solo con el número.",
                "answer": "20 m: la velocidad es ⟨3, 4⟩ y su rapidez √(3² + 4²) = 5 m/s es constante, así que ∫(0 a 4) 5 dt = 5 × 4 = 20 m.",
                "hints": ["Derivá: x' = 3 e y' = 4; la rapidez es √(3² + 4²).", "La rapidez es constante e igual a 5; integrá 5 desde t = 0 hasta t = 4."],
                "payload": {"check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "m"}},
            },
            {
                "item_type": "worked_example",
                "title": "Vector aceleración derivando v(t) componente a componente",
                "prompt": "Si el vector velocidad es v(t) = ⟨t³, 2t² − 5t⟩, entonces a(t) = v'(t) = ⟨3t², 4t − 5⟩. ¿Cuál es la componente vertical a_y(3) en t = 3 s? Respondé solo con el número.",
                "answer": "7: 4(3) − 5 = 12 − 5 = 7.",
                "hints": ["Evaluá 4t − 5 en t = 3."],
                "payload": {"check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Tangentes horizontales vs. verticales en paramétricas",
                "prompt": "En una curva paramétrica (x(t), y(t)), ¿cuándo tiene una recta tangente VERTICAL?",
                "answer": "Cuando dx/dt = 0 (no avanza en x) mientras dy/dt ≠ 0 (sí se mueve en y).",
                "hints": ["En dy/dx = (dy/dt)/(dx/dt), una pendiente infinita (vertical) anula el denominador."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Cuando dx/dt = 0 y dy/dt ≠ 0",
                            "Cuando dy/dt = 0 y dx/dt ≠ 0",
                            "Cuando x(t) = 0",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "La trampa de la segunda derivada paramétrica d²y/dx²",
                "prompt": "¿Cuál es la fórmula CORRECTA para la concavidad d²y/dx² de una curva paramétrica?",
                "answer": "[d/dt (dy/dx)] / (dx/dt): derivás dy/dx respecto de t y volvés a dividir por dx/dt (NO es y''(t) / x''(t)!).",
                "hints": ["Aplicá la regla de la cadena sobre la pendiente m(t) = dy/dx: dm/dx = (dm/dt) / (dx/dt)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "[d/dt (dy/dx)] / (dx/dt)",
                            "(d²y/dt²) / (d²x/dt²)",
                            "d/dt (dy/dx) sin dividir",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "c2-polares-areas",
        "title": "89. Cálculo en coordenadas polares y áreas polares",
        "level": 32,
        "order_index": 89,
        "summary": "Curvas polares r = f(θ) (cardioides y rosas), conversión a paramétricas para pendientes y áreas con A = (1/2) ∫ r(θ)² dθ.",
        "prerequisites": ["c2-parametricas-vectores", "pc-complejos-polares"],
        "metadata": {"section": "Cálculo 2", "lab_tab": "parametric_series", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Pasar de coordenadas polares a cartesianas (x = r·cos θ)",
                "prompt": "Un radar detecta un blanco en coordenadas polares (r, θ) = (8 km, 60°) (cos 60° = 0.5). ¿Cuál es su coordenada horizontal x (en km)? Respondé solo con el número.",
                "answer": "4 km: x = r · cos(θ) = 8 × 0.5 = 4 km.",
                "hints": ["Multiplicá r = 8 por cos(60°) = 0.5."],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0.01, "unit": "km"}},
            },
            {
                "item_type": "worked_example",
                "title": "Calcular un área polar con A = (1/2) ∫ r(θ)² dθ",
                "prompt": "Una espiral polar cumple r(θ) = 2√θ (así r² = 4θ). Calculá el área barrida de θ = 0 a θ = 3 usando A = (1/2) ∫(de 0 a 3) 4θ dθ = [θ²] de 0 a 3. Respondé solo con el número.",
                "answer": "9: (1/2) × 4θ = 2θ, cuya integral es [θ²] de 0 a 3 = 9 − 0 = 9.",
                "hints": ["Evaluá θ² en θ = 3 y restale θ = 0."],
                "payload": {
                    "lab_link": "math:parametric_series",
                    "check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Contar los pétalos de una rosa polar r = cos(2θ)",
                "prompt": "Las rosas polares r = a·cos(nθ) tienen n pétalos si n es impar y 2n pétalos si n es par. ¿Cuántos pétalos tiene r = 3·cos(2θ)? Respondé solo con el número.",
                "answer": "4 pétalos: como n = 2 es par, la curva dibuja 2 × 2 = 4 pétalos en [0, 2π].",
                "hints": ["2 es par → 2n pétalos."],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Contar los pétalos de una rosa polar con n impar",
                "prompt": "¿Cuántos pétalos tiene la rosa polar r = 5·sen(3θ)? Respondé solo con el número.",
                "answer": "3 pétalos: cuando n es impar, la curva traza los n pétalos completos en [0, π] (de π a 2π los vuelve a remarcar encima!).",
                "hints": ["3 es impar → exactamente n pétalos."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Por qué el área polar lleva (1/2) y r²",
                "prompt": "En coordenadas cartesianas el área es ∫ y dx, pero en polares es (1/2) ∫ r(θ)² dθ. ¿Por qué aparece ese (1/2)·r²?",
                "answer": "Porque cada rebanada polar es un sector circular (cuña de pizza de radio r y ángulo dθ), cuya área es (1/2)·r²·dθ.",
                "hints": ["Recordá la fórmula de área de un sector circular en radianes: (θ / 2π) · πr² = (1/2)r²θ."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Cada rebanada es un sector circular (cuña) de área (1/2)·r²·dθ",
                            "Porque se integra solo medio círculo",
                            "Por la regla de la cadena",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Área encerrada ENTRE dos curvas polares",
                "prompt": "Para hallar el área que queda afuera del círculo interior r_int(θ) y adentro de la curva exterior r_ext(θ), ¿qué integral usás?",
                "answer": "(1/2) ∫ (r_ext² − r_int²) dθ: igual que en arandelas, restás los cuadrados por separado (¡nunca (r_ext − r_int)²!).",
                "hints": ["Restá el área del sector interior al área del sector exterior."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "(1/2) ∫ [r_ext(θ)² − r_int(θ)²] dθ",
                            "(1/2) ∫ [r_ext(θ) − r_int(θ)]² dθ",
                            "∫ [r_ext(θ) − r_int(θ)] dθ",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 33: SERIES INFINITAS Y TAYLOR ====================
    {
        "slug": "c2-series-convergencia",
        "title": "90. Series infinitas y pruebas de convergencia",
        "level": 33,
        "order_index": 90,
        "summary": "Prueba del n-ésimo término, paradoja de la serie armónica, p-series, series alternantes (cota de error) y Prueba de la Razón.",
        "prerequisites": ["pc-series-sigma", "c2-impropias-longitud"],
        "metadata": {"section": "Cálculo 2", "lab_tab": "parametric_series", "est_minutes": 24},
        "items": [
            {
                "item_type": "recall",
                "title": "Prueba del n-ésimo término (solo detecta divergencia)",
                "prompt": "En la serie ∑ 3n / (n + 1), el límite del término general cuando n → ∞ es 3 (distinto de 0). ¿Qué concluís de inmediato?",
                "answer": "Diverge seguro: si los términos ni siquiera tienden a 0, la suma infinita jamás puede converger (¡ojo: que tienda a 0 es necesario pero NO suficiente!).",
                "hints": ["Estás sumando infinitos números que se acercan a 3."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Diverge (porque lim a_n = 3 ≠ 0)",
                            "Converge exactamente a 3",
                            "No se puede saber sin la prueba de la razón",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "La serie armónica ∑ 1/n vs. p-series",
                "prompt": "Aunque los términos 1/n tienden a 0, ¿qué ocurre con la serie armónica 1 + 1/2 + 1/3 + 1/4 + ... (p = 1)?",
                "answer": "Diverge lentamente hacia +∞: una p-serie ∑ 1/n^p converge ÚNICAMENTE cuando p > 1 (por ej. ∑ 1/n² = π²/6 sí converge).",
                "hints": ["Compara con la integral impropia ∫_1^∞ (1/x) dx = ∞."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Diverge hacia infinito (p = 1 no alcanza; hace falta p > 1)",
                            "Converge porque 1/n → 0",
                            "Converge exactamente a 2",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Convergencia condicional: la serie armónica alternante",
                "prompt": "Ahora alternamos los signos: 1 − 1/2 + 1/3 − 1/4 + 1/5 − ... ¿Converge o diverge?",
                "answer": "Converge condicionalmente (a ln 2 ≈ 0.693): cumple el criterio de series alternantes (signos alternos, |a_n| decrece hacia 0), aunque sin los signos divergiría.",
                "hints": ["El criterio de Leibniz solo pide términos alternantes que bajen monótonamente hacia 0."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Converge (condicionalmente, por criterio de series alternantes)",
                            "Diverge igual que la serie armónica positiva",
                            "Converge absolutamente",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Cota de error en una serie alternante",
                "prompt": "Aproximás la serie alternante 1 − 1/2 + 1/3 − 1/4 + 1/5 − ... usando solo los primeros 3 términos (1 − 1/2 + 1/3). ¿Cuál es el error MÁXIMO garantizado (el valor absoluto del primer término que dejaste afuera, en decimal)? Respondé solo con el número.",
                "answer": "0.25 (1/4): en toda serie alternante convergente, la suma real queda atrapada a menos del primer término omitido (|−1/4| = 0.25).",
                "hints": ["Mirá cuál es el 4.° término de la serie en valor absoluto."],
                "payload": {"check": {"type": "numeric", "value": 0.25, "tolerance": 0.01, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Prueba de la Razón con factoriales (∑ 2ⁿ / n!)",
                "prompt": "En ∑ 2ⁿ / n!, la razón |a_{n+1} / a_n| se simplifica a 2 / (n + 1). Al tomar lim(n → ∞) da L = 0 < 1. ¿Qué concluye la Prueba de la Razón?",
                "answer": "Converge absolutamente (de hecho, empezando en n = 0 suma exactamente e²!): siempre que L < 1 converge, si L > 1 diverge, y si L = 1 la prueba no decide.",
                "hints": ["Compará L = 0 con el umbral 1."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Converge absolutamente (porque L = 0 < 1)",
                            "Diverge (porque 2ⁿ crece exponencialmente)",
                            "La prueba no concluye",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Qué pasa si la Prueba de la Razón da L = 1",
                "prompt": "Aplicás la Prueba de la Razón a una serie y obtenés L = 1. ¿Qué debés hacer?",
                "answer": "Usar otra prueba (como p-series, comparación o integral): tanto ∑ 1/n (diverge) como ∑ 1/n² (converge) dan L = 1!",
                "hints": ["L = 1 es la zona indecisa donde conviven series convergentes y divergentes."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Es inconcluyente: hay que aplicar otra prueba",
                            "Significa que siempre diverge",
                            "Significa que converge exactamente a 1",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "c2-taylor-maclaurin",
        "title": "91. Series de potencias, Taylor/Maclaurin y Fórmula de Euler",
        "level": 33,
        "order_index": 91,
        "summary": "Aproximar funciones con polinomios de Taylor, las 4 series de Maclaurin esenciales, radio de convergencia y e^(iπ) + 1 = 0.",
        "prerequisites": ["c2-series-convergencia", "c1-cadena-implicita"],
        "metadata": {"section": "Cálculo 2", "lab_tab": "parametric_series", "est_minutes": 24},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Calcular un coeficiente de Taylor: f^(n)(a) / n!",
                "prompt": "Una función cumple f'''(0) = 12. En su serie de Maclaurin ∑ [f^(n)(0) / n!] · xⁿ, ¿qué coeficiente acompaña a x³ (recordá que 3! = 6)? Respondé solo con el número.",
                "answer": "2: c₃ = f'''(0) / 3! = 12 / 6 = 2 (el factorial n! compensa los exponentes que bajan al derivar n veces).",
                "hints": ["Dividí 12 por 3! = 3 × 2 × 1 = 6."],
                "payload": {
                    "lab_link": "math:parametric_series",
                    "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Aproximar e^(0.2) con el polinomio de Maclaurin de grado 2",
                "prompt": "La serie de Maclaurin de eˣ es 1 + x + x²/2! + x³/3! + ... Usá los primeros 3 términos (1 + x + x²/2) para estimar e^(0.2). Respondé solo con el número.",
                "answer": "1.22: 1 + 0.2 + (0.04 / 2) = 1.22 (el valor exacto es 1.2214 — ¡error de apenas 0.1%!).",
                "hints": ["Calculá 1 + 0.2 + 0.04 ÷ 2."],
                "payload": {
                    "lab_link": "math:parametric_series",
                    "check": {"type": "numeric", "value": 1.22, "tolerance": 0.005, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Aproximar cos(0.2) con Maclaurin (potencias pares)",
                "prompt": "La serie de Maclaurin de cos(x) es 1 − x²/2! + x⁴/4! − ... Usá la aproximación cuadrática 1 − x²/2 para estimar cos(0.2 rad). Respondé solo con el número.",
                "answer": "0.98: 1 − (0.04 / 2) = 0.98 (el valor real es 0.98007 — ¡4 decimales de precisión mentalmente!).",
                "hints": ["Calculá 1 − 0.04 ÷ 2."],
                "payload": {
                    "lab_link": "math:parametric_series",
                    "check": {"type": "numeric", "value": 0.98, "tolerance": 0.005, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Radio de convergencia de una serie geométrica de potencias",
                "prompt": "La serie 1 / (1 − x/3) = ∑ (x / 3)ⁿ converge cuando |x / 3| < 1, es decir |x| < 3. ¿Cuál es su radio de convergencia R? Respondé solo con el número.",
                "answer": "3: converge para todo x en (−3, 3) y diverge fuera de ese intervalo (radio R = 3 centrado en 0).",
                "hints": ["De |x / 3| < 1 despejá |x| < R."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Distinguir las 3 series de Maclaurin esenciales",
                "prompt": "¿Cuál de las siguientes corresponde a la serie de Maclaurin de sen(x) (función impar)?",
                "answer": "x − x³/3! + x⁵/5! − ... (solo potencias IMPARES con signos alternos; cos(x) lleva las PARES y eˣ lleva TODAS positivas).",
                "hints": ["Como sen(x) es función impar, solo puede tener exponentes impares (1, 3, 5...)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "x − x³/3! + x⁵/5! − ...",
                            "1 − x²/2! + x⁴/4! − ...",
                            "1 + x + x²/2! + x³/3! + ...",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "La Fórmula de Euler: e^(iθ) = cos(θ) + i·sen(θ)",
                "prompt": "Sustituyendo θ = π en la Fórmula de Euler e^(iθ) = cos(θ) + i·sen(θ) (donde cos π = −1 y sen π = 0), ¿a qué célebre identidad se llega?",
                "answer": "e^(iπ) + 1 = 0: conecta en una sola ecuación las cinco constantes fundamentales de toda la matemática (e, i, π, 1 y 0).",
                "hints": ["Evaluá cos(π) + i·sen(π) = −1 + 0i = −1."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "e^(iπ) + 1 = 0",
                            "e^(iπ) − 1 = 0",
                            "e^(iπ) = i",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
]

CALCULUS2_LESSONS: dict[str, dict] = {
    "c2-partes-fracciones": {
        "hook": "Cuando la sustitución `u` no alcanza —como en `∫ x·eˣ dx` o `∫ 1/(x² − 1) dx`— dos técnicas desarman casi cualquier integral difícil en piezas elementales.",
        "concept": {
            "points": [
                "**Integración por partes** (la regla del producto en reversa): **`∫ u dv = u·v − ∫ v du`**. Elegí `u` (la que derivás para simplificarla) con la regla **LIATE**: **L**ogarítmicas, **I**nversas trig, **A**lgebraicas (`xⁿ`), **T**rigonométricas, **E**xponenciales.",
                "**Fracciones parciales**: cuando integrás un cociente racional `P(x) / ((x − a)(x − b))`, lo partís en **`A/(x − a) + B/(x − b)`**; multiplicás por el denominador común, elegís `x = a` y `x = b` para despejar `A` y `B` al toque, e integrás directo a **`A·ln|x − a| + B·ln|x − b|`**.",
                "Si el grado de arriba es mayor o igual al de abajo, primero hacés división de polinomios; luego aplicás fracciones parciales al resto.",
            ],
            "real_world": [
                {
                    "title": "Transformadas de Fourier y Laplace (telecomunicaciones)",
                    "detail": "Calcular el espectro de frecuencias de una señal requiere integrales como `∫ t·e^(−st) dt` resueltas directamente por partes.",
                },
                {
                    "title": "Modelos logísticos y química de reacciones",
                    "detail": "Integrar `dP / [P(K − P)]` para resolver poblaciones o velocidad de reacciones químicas de segundo orden usa fracciones parciales.",
                },
                {
                    "title": "Valor esperado en probabilidad continua",
                    "detail": "Calcular la vida media de componentes electrónicos (`∫ t · λe^(−λt) dt`) es exactamente una integración por partes.",
                },
            ],
            "key_rule": "Partes: ∫ u dv = uv − ∫ v du (elegí u con LIATE) | Parciales: partir denominadores factorizados para integrar con ln.",
            "pitfall": "Elegir `u = eˣ` y `dv = x dx` en `∫ x·eˣ dx`: la integral nueva queda `∫ (x²/2)·eˣ dx` (empeora el grado!). `u = x` baja el grado y resuelve en 1 paso.",
        },
        "example": {
            "title": "Integrar ∫ x·eˣ dx por partes y descomponer 5 / ((x − 1)(x + 4))",
            "steps": [
                "En `∫ x·eˣ dx`: por LIATE elegimos `u = x` (`du = dx`) y `dv = eˣ dx` (`v = eˣ`).",
                "Aplicamos `uv − ∫ v du = x·eˣ − ∫ eˣ dx = x·eˣ − eˣ + C`.",
                "Para `5/((x − 1)(x + 4)) = A/(x − 1) + B/(x + 4)` → `5 = A(x + 4) + B(x − 1)`: en `x = 1` da `A = 1`; en `x = −4` da `B = −1` → integral `ln|x − 1| − ln|x + 4| + C`.",
            ],
            "lab_link": "math:integrals_adv",
            "lab_cta": "Practicar integración avanzada en el Laboratorio",
        },
        "check": {
            "question": "En `∫ x · cos(x) dx`, según LIATE, ¿qué elegís como `u` y qué como `dv`?",
            "options": [
                {"text": "`u = x` y `dv = cos(x) dx`", "ok": True, "feedback": "Exacto: Algebraica (x) va antes que Trigonométrica (cos x), y al derivar x desaparece."},
                {"text": "`u = cos(x)` y `dv = x dx`", "ok": False, "feedback": "Eso sube x a x²/2 y empeora la integral."},
                {"text": "No se puede hacer por partes", "ok": False, "feedback": "Es uno de los casos más limpios de integración por partes: x·sen(x) + cos(x) + C."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuánto da `∫ [1/(x − 3) + 2/(x + 1)] dx`?",
                "options": [
                    {"text": "`ln|x − 3| + 2·ln|x + 1| + C`", "ok": True, "feedback": "Exacto: cada término lineal simple integra directo a un logaritmo natural."},
                    {"text": "`−1/(x − 3)² − 2/(x + 1)² + C`", "ok": False, "feedback": "Derivaste en vez de integrar."},
                    {"text": "`3·ln|(x − 3)(x + 1)| + C`", "ok": False, "feedback": "Solo el segundo término tiene coeficiente 2."},
                ],
            },
            {
                "question": "Si `4 / ((x − 2)(x + 2)) = A/(x − 2) + B/(x + 2)`, ¿cuánto vale `A`?",
                "options": [
                    {"text": "`1` (`4 = A(2 + 2)` → `A = 1`)", "ok": True, "feedback": "Exacto: y B = −1."},
                    {"text": "`4`", "ok": False, "feedback": "Te faltó dividir por (2 + 2) = 4."},
                    {"text": "`2`", "ok": False, "feedback": "Al evaluar en x = 2 queda 4 = 4A, así que A = 1."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en tus palabras cuándo usarías integración por partes y cuándo fracciones parciales.",
    },
    "c2-impropias-longitud": {
        "hook": "Una cola infinitamente larga puede encerrar un área perfectamente finita (como `∫_1^∞ 1/x² dx = 1`), y con Pitágoras infinitesimal podés medir el largo exacto de cualquier curva.",
        "concept": {
            "points": [
                "**Integrales impropias**: ocurren cuando un límite es `±∞` o hay una **asíntota vertical** dentro de `[a, b]`. Siempre se reemplaza el problema por un **límite**: si da un número finito **converge**; si da `±∞` o no existe, **diverge**.",
                "**Regla `p` de referencia**: `∫_1^∞ (1/x^p) dx` **converge ⇔ `p > 1`** (en cambio `∫_0^1 (1/x^p) dx` cerca del `0` funciona al revés: converge ⇔ `p < 1`!).",
                "**Longitud de arco**: sumando mini-hipotenusas `ds = √(dx² + dy²)` se obtiene **`L = ∫_a^b √(1 + [f'(x)]²) dx`**.",
            ],
            "real_world": [
                {
                    "title": "Velocidad de escape de un cohete (Física)",
                    "detail": "El trabajo para escapar de la gravedad hasta distancia infinita es `∫_R^∞ (GMm / r²) dr = GMm / R` — ¡finito justamente porque `p = 2 > 1`!",
                },
                {
                    "title": "Distribuciones de probabilidad (campana de Gauss)",
                    "detail": "El área total bajo la campana normal desde `−∞` hasta `+∞` es una integral impropia convergente igual a `1` (100%).",
                },
                {
                    "title": "Largo exacto de cables colgantes y puentes",
                    "detail": "Calcular cuántos metros de acero lleva un cable parabólico o catenario entre dos torres usa directamente la integral de longitud de arco.",
                },
            ],
            "key_rule": "Impropias: reemplazá ∞ o asíntota por un límite | ∫_1^∞ 1/x^p dx converge ⇔ p > 1 | Arco: ∫ √(1 + [f'(x)]²) dx.",
            "pitfall": "Evaluar `∫_{−1}^{1} (1/x²) dx` aplicando TFC ciegamente (`−1 − 1 = −2` negativo!): en `x = 0` hay una asíntota vertical y esa integral en realidad DIVERGE a `+∞`.",
        },
        "example": {
            "title": "Evaluar ∫(1 a ∞) 6/x² dx y verificar divergencia de ∫(1 a ∞) 1/x dx",
            "steps": [
                "Para `∫_1^∞ 6/x² dx`: escribimos `lim_{b→∞} [−6/x]_1^b = lim_{b→∞} (−6/b + 6) = 6` (converge a 6).",
                "Para `∫_1^∞ 1/x dx`: escribimos `lim_{b→∞} [ln(x)]_1^b = lim_{b→∞} (ln(b) − 0) = +∞` (diverge!).",
                "Misma cola que tiende a 0, pero `1/x²` cae lo bastante rápido para encerrar área finita y `1/x` no.",
            ],
            "lab_link": "math:integrals_adv",
            "lab_cta": "Practicar integrales impropias en el Laboratorio",
        },
        "check": {
            "question": "¿Converge o diverge `∫(de 1 a ∞) (1 / √x) dx` (`p = 0.5`)?",
            "options": [
                {"text": "Diverge (porque `p = 0.5 ≤ 1`; `[2√b − 2] → ∞`)", "ok": True, "feedback": "Exacto: cae demasiado lento en el infinito para encerrar área finita."},
                {"text": "Converge a `2`", "ok": False, "feedback": "Converge a 2 entre 0 y 1, pero de 1 a ∞ diverge."},
                {"text": "Converge a `0.5`", "ok": False, "feedback": "En [1, ∞) necesita p > 1 para converger."},
            ],
        },
        "checks": [
            {
                "question": "¿Por qué es impropia la integral `∫(de 0 a 4) 1 / (x − 2) dx` aunque sus límites `0` y `4` son finitos?",
                "options": [
                    {"text": "Porque el integrando tiene una asíntota vertical en `x = 2`, justo dentro de `[0, 4]`", "ok": True, "feedback": "Exacto: hay que partirla en x = 2 y tomar límites (esta en particular diverge)."},
                    {"text": "No es impropia", "ok": False, "feedback": "Siempre revisá si el denominador se anula dentro del intervalo."},
                    {"text": "Porque `0` está en el límite inferior", "ok": False, "feedback": "En x = 0 vale −0.5 sin problema; el problema está en x = 2."},
                ],
            },
            {
                "question": "¿Cuál es la integral correcta para la longitud de arco de `y = x²` entre `x = 0` y `x = 3`?",
                "options": [
                    {"text": "`∫(de 0 a 3) √(1 + 4x²) dx` (porque `f'(x) = 2x` → `[f'(x)]² = 4x²`)", "ok": True, "feedback": "Exacto: sustituimos f'(x) = 2x en √(1 + [f'(x)]²)."},
                    {"text": "`∫(de 0 a 3) √(1 + x⁴) dx`", "ok": False, "feedback": "Usaste f(x)² en vez de la derivada f'(x)²."},
                    {"text": "`∫(de 0 a 3) √(1 + 2x) dx`", "ok": False, "feedback": "Te faltó elevar al cuadrado f'(x) = 2x."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá la diferencia entre `∫_1^∞ (1/x) dx` y `∫_1^∞ (1/x²) dx` y por qué hay que vigilar asíntotas internas.",
    },
    "c2-euler-logistico": {
        "hook": "Casi ninguna ecuación diferencial del mundo real (clima, órbitas, epidemiología) se puede resolver con lápiz y papel: el Método de Euler es la idea detrás de TODAS las simulaciones por computadora.",
        "concept": {
            "points": [
                "**Método de Euler**: arrancás en `(x₀, y₀)` y avanzás en pasitos `Δx` siguiendo la tangente local: **`y_{n+1} = y_n + Δx · f(x_n, y_n)`** (donde `dy/dx = f(x, y)` es la pendiente). Cuanto más chico `Δx`, más fiel a la curva real.",
                "**Sesgo geométrico**: si la curva real es cóncava hacia arriba (`y'' > 0`), las tangentes quedan por debajo (**subestima**); si es cóncava hacia abajo (`y'' < 0`), **sobreestima**.",
                "**Crecimiento logístico**: **`dP/dt = k · P · (1 − P / K)`** modela poblaciones con límite de recursos (**capacidad de carga `K`**). Tiene forma de 'S', crece a su **máxima velocidad en `P = K / 2`** (punto de inflexión) y si `P > K`, decrece hacia `K`.",
            ],
            "real_world": [
                {
                    "title": "Motores de física en videojuegos (integración paso a paso)",
                    "detail": "60 veces por segundo (`Δt = 1/60 s`), el juego actualiza posición y velocidad con pasos tipo Euler (`x += v·Δt`, `v += a·Δt`).",
                },
                {
                    "title": "Adopción de nuevas tecnologías y mercados",
                    "detail": "Al principio pocos adoptan un producto, luego se viraliza a ritmo máximo al 50% del mercado (`K/2`), y finalmente satura en `K`.",
                },
                {
                    "title": "Ecología y pesca sustentable",
                    "detail": "El rendimiento máximo sostenible de un ecosistema ocurre manteniendo la población cerca de `K/2`, donde la tasa de reposición `dP/dt` es máxima.",
                },
            ],
            "key_rule": "Euler: y_nuevo = y_actual + Δx · pendiente | Logístico: dP/dt = kP(1 − P/K), tope K, crecimiento máximo en K/2.",
            "pitfall": "Usar siempre la pendiente inicial en todos los pasos de Euler: ¡tenés que RECALCULAR la pendiente con el nuevo `(x_n, y_n)` en cada paso!",
        },
        "example": {
            "title": "Dos pasos de Euler en dy/dx = x + y desde (0, 1) y analizar dP/dt = 0.2P(1 − P/500)",
            "steps": [
                "Euler (`Δx = 0.5`): en `(0, 1)`, pendiente = `0 + 1 = 1` → `y(0.5) ≈ 1 + 0.5(1) = 1.5`.",
                "Paso 2 desde `(0.5, 1.5)`: nueva pendiente = `0.5 + 1.5 = 2` → `y(1.0) ≈ 1.5 + 0.5(2) = 2.5`.",
                "En `dP/dt = 0.2P(1 − P/500)`: capacidad de carga `K = 500`, máximo crecimiento en `P = 250` (`dP/dt = 0.2(250)(0.5) = 25`).",
            ],
            "lab_link": "math:integrals_adv",
            "lab_cta": "Practicar Euler y logístico en el Laboratorio",
        },
        "check": {
            "question": "En `dy/dx = 2x` empezando en `(1, 3)` con paso `Δx = 0.5`, ¿cuánto vale `y` tras UN paso (en `x = 1.5`)?",
            "options": [
                {"text": "`4` (`3 + 0.5 × 2(1) = 4`)", "ok": True, "feedback": "Exacto: en x = 1 la pendiente es 2, así que sube 0.5 × 2 = 1 → y = 4."},
                {"text": "`4.5`", "ok": False, "feedback": "Evaluaste la pendiente en el punto final (1.5) en vez del punto inicial (1)."},
                {"text": "`5`", "ok": False, "feedback": "Sumaste la pendiente completa (2) sin multiplicarla por el paso Δx = 0.5."},
            ],
        },
        "checks": [
            {
                "question": "Una reserva sigue `dP/dt = 0.1P(1 − P/1000)` y hoy se introducen `P = 1200` animales (por encima de `K`). ¿Qué pasará con `P`?",
                "options": [
                    {"text": "Decrecerá (`dP/dt < 0`) hasta estabilizarse en `1000`", "ok": True, "feedback": "Exacto: como 1 − 1200/1000 = −0.2 < 0, la población baja hacia la capacidad de carga K = 1000."},
                    {"text": "Seguirá creciendo sin límite", "ok": False, "feedback": "Cuando P > K el factor (1 − P/K) se vuelve negativo."},
                    {"text": "Caerá inmediatamente a `0`", "ok": False, "feedback": "Se frena al llegar a K = 1000, donde dP/dt vuelve a ser 0."},
                ],
            },
            {
                "question": "Si una solución exacta es cóncava hacia ABAJO (`y'' < 0`), el Método de Euler:",
                "options": [
                    {"text": "Sobreestima el valor real (las tangentes quedan arriba)", "ok": True, "feedback": "Exacto: en una curva en forma de arco (∩), las tangentes vuelan por encima."},
                    {"text": "Subestima el valor real", "ok": False, "feedback": "Subestima cuando es cóncava hacia arriba (∪)."},
                    {"text": "Da el valor exacto", "ok": False, "feedback": "Solo es exacto si la solución es una línea recta (y'' = 0)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá cómo funciona el Método de Euler y qué representan `K` y `K/2` en una curva logística.",
    },
    "c2-parametricas-vectores": {
        "hook": "Un bucle, una órbita o un tiro parabólico con viento no siempre pasan la prueba de la recta vertical `y = f(x)`: escribir `x(t)` e `y(t)` por separado respecto del tiempo resuelve cualquier trayectoria 2D.",
        "concept": {
            "points": [
                "Una curva paramétrica / vectorial **`r(t) = ⟨x(t), y(t)⟩`** separa movimiento horizontal y vertical. Su pendiente espacial es **`dy/dx = (dy/dt) / (dx/dt)`** (tangente horizontal: `y' = 0`; vertical: `x' = 0`).",
                "La segunda derivada paramétrica requiere volver a dividir por `dx/dt`: **`d²y/dx² = [d/dt (dy/dx)] / (dx/dt)`**.",
                "Velocidad **`v(t) = ⟨x'(t), y'(t)⟩`**, aceleración **`a(t) = ⟨x''(t), y''(t)⟩`**, **rapidez** **`|v(t)| = √(x'² + y'²)`**, y **distancia recorrida** **`L = ∫_a^b √(x'(t)² + y'(t)²) dt`**.",
            ],
            "real_world": [
                {
                    "title": "Trayectorias de drones, satélites y proyectiles",
                    "detail": "La posición en función del tiempo `r(t) = ⟨x(t), y(t)⟩` dice no solo la forma del camino, sino dónde está y a qué rapidez en cada segundo.",
                },
                {
                    "title": "Curvas Bézier en diseño gráfico y fuentes",
                    "detail": "Los trazos curvos en SVG y tipografía son curvas de Bézier: ecuaciones paramétricas cuadráticas o cúbicas `(x(t), y(t))` con `t ∈ [0, 1]`.",
                },
                {
                    "title": "Control de robots industriales (CNC / impresora 3D)",
                    "detail": "Los motores X e Y reciben órdenes separadas `x(t)` e `y(t)`, manteniendo controlada la rapidez total `√(x'² + y'²)` de la boquilla.",
                },
            ],
            "key_rule": "dy/dx = y'(t)/x'(t) | Rapidez = √(x'² + y'²) | Distancia = ∫ √(x'² + y'²) dt | d²y/dx² = (d/dt(dy/dx)) / x'(t).",
            "pitfall": "Confundir el vector velocidad `⟨x'(t), y'(t)⟩` con la rapidez escalar `√(x'² + y'²)`, o calcular `d²y/dx²` como `y''/x''`.",
        },
        "example": {
            "title": "Analizar r(t) = ⟨t², t³ − 3t⟩ en t = 2",
            "steps": [
                "Derivamos cada componente: `v(t) = ⟨2t, 3t² − 3⟩` → en `t = 2`, `v(2) = ⟨4, 9⟩`.",
                "Pendiente de la trayectoria: `dy/dx = 9 / 4 = 2.25`.",
                "Rapidez instantánea: `|v(2)| = √(4² + 9²) = √97 ≈ 9.85`; aceleración `a(t) = ⟨2, 6t⟩` → `a(2) = ⟨2, 12⟩`.",
            ],
            "lab_link": "math:parametric_series",
            "lab_cta": "Practicar curvas paramétricas en el Laboratorio",
        },
        "check": {
            "question": "Si un dron sigue `x(t) = 3·cos(t)` e `y(t) = 3·sen(t)`, ¿cuál es su rapidez constante `√(x'² + y'²)`?",
            "options": [
                {"text": "`3` (`√(9·sen²t + 9·cos²t) = √9 = 3`)", "ok": True, "feedback": "Exacto: gira en círculo de radio 3 con rapidez uniforme igual a 3."},
                {"text": "`9`", "ok": False, "feedback": "Te faltó sacar la raíz cuadrada de 9."},
                {"text": "`0`", "ok": False, "feedback": "sen² + cos² = 1, nunca se anulan simultáneamente."},
            ],
        },
        "checks": [
            {
                "question": "Dada `x(t) = t² − 4t` e `y(t) = 2t + 1`, ¿en qué instante `t` la curva tiene tangente VERTICAL (`dx/dt = 0`)?",
                "options": [
                    {"text": "`t = 2` (`2t − 4 = 0`, mientras `dy/dt = 2 ≠ 0`)", "ok": True, "feedback": "Exacto: en t = 2 la componente x se frena y da la vuelta mientras y sigue subiendo."},
                    {"text": "`t = 4`", "ok": False, "feedback": "En t = 4, x(4) = 0 pero dx/dt = 4 ≠ 0."},
                    {"text": "Nunca", "ok": False, "feedback": "Sí ocurre cuando dx/dt = 2t − 4 se hace 0."},
                ],
            },
            {
                "question": "Si conocés la velocidad `v(t) = ⟨v_x(t), v_y(t)⟩` y la posición inicial `r(0) = ⟨1, 2⟩`, ¿cómo hallás la nueva posición en `t = 5`?",
                "options": [
                    {"text": "`⟨1 + ∫_0^5 v_x(t)dt, 2 + ∫_0^5 v_y(t)dt⟩`", "ok": True, "feedback": "Exacto: sumás la integral de cada componente de velocidad a la posición inicial."},
                    {"text": "`⟨1 + ∫_0^5 |v(t)|dt, 2⟩`", "ok": False, "feedback": "Integrar |v(t)| da la distancia total recorrida a lo largo de la curva, no el vector posición."},
                    {"text": "Derivando `v(t)` en `t = 5`", "ok": False, "feedback": "Derivar v(t) te da la aceleración a(t), no la posición."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué diferencia hay entre el desplazamiento vectorial `∫ v(t) dt` y la distancia recorrida `∫ |v(t)| dt` en 2D.",
    },
    "c2-polares-areas": {
        "hook": "Para antenas, radares, pétalos y órbitas planetarias, describir un punto con distancia `r` y ángulo `θ` convierte ecuaciones horribles en fórmulas de una línea.",
        "concept": {
            "points": [
                "En **coordenadas polares `r = f(θ)`**, cada punto se traduce a cartesianas mediante **`x = r·cos(θ)`** e **`y = r·sen(θ)`** (con `r² = x² + y²`).",
                "**Pendiente en polares**: tratás `θ` como parámetro usando `x(θ) = r(θ)cos θ` e `y(θ) = r(θ)sen θ` → **`dy/dx = (dy/dθ) / (dx/dθ)`** (¡ojo: `dr/dθ` NO es la pendiente `dy/dx`!).",
                "**Área polar**: sumamos infinitas cuñas triangulares / sectores de radio `r` y ángulo `dθ` → **`A = (1/2) ∫_α^β r(θ)² dθ`**. Entre dos curvas: **`(1/2) ∫ (r_ext² − r_int²) dθ`**.",
            ],
            "real_world": [
                {
                    "title": "Micrófonos cardioides y patrones de antenas",
                    "detail": "Un micrófono cardioide capta según `r = 1 + cos(θ)`: máximo al frente (`θ = 0°`) y nulo atrás (`θ = 180°`) para rechazar ruido de escenario.",
                },
                {
                    "title": "Radares aeronáuticos y sonares",
                    "detail": "Un radar mide directamente distancia `r` (tiempo de eco) y ángulo `θ` (giro de la antena): su mapa nativo es polar.",
                },
                {
                    "title": "Segunda Ley de Kepler (áreas iguales en tiempos iguales)",
                    "detail": "La velocidad con que un planeta barre área orbital es literalmente `dA/dt = (1/2)r² (dθ/dt)` constante!",
                },
            ],
            "key_rule": "x = r·cos θ, y = r·sen θ | Área polar = (1/2) ∫ r(θ)² dθ | Entre curvas = (1/2) ∫ (r_ext² − r_int²) dθ.",
            "pitfall": "Creer que `dr/dθ` es la pendiente `dy/dx`, o olvidar el factor `1/2` al calcular un área polar.",
        },
        "example": {
            "title": "Área de la espiral r = 2√θ en [0, 3] y del círculo r = 4",
            "steps": [
                "Para `r = 2√θ`, elevamos al cuadrado: `r² = 4θ`.",
                "Aplicamos `A = (1/2) ∫(0 a 3) 4θ dθ = ∫(0 a 3) 2θ dθ = [θ²]_0^3 = 9`.",
                "Verificación en el círculo `r = 4` en `[0, 2π]`: `(1/2) ∫_0^(2π) 16 dθ = 8 · 2π = 16π = π·4²` exacto!",
            ],
            "lab_link": "math:parametric_series",
            "lab_cta": "Practicar polares y paramétricas en el Laboratorio",
        },
        "check": {
            "question": "¿Qué representa la ecuación polar `r = 6`?",
            "options": [
                {"text": "Un círculo centrado en el origen de radio `6`", "ok": True, "feedback": "Exacto: todos los puntos a distancia 6 del origen para cualquier ángulo θ."},
                {"text": "Una recta vertical en `x = 6`", "ok": False, "feedback": "Una recta vertical sería r·cos(θ) = 6 (r = 6·sec θ)."},
                {"text": "Una espiral", "ok": False, "feedback": "Una espiral requiere que r crezca con θ, como r = θ."},
            ],
        },
        "checks": [
            {
                "question": "Si `r = 3` y `θ = π` (`180°`), ¿cuáles son sus coordenadas cartesianas `(x, y)`?",
                "options": [
                    {"text": "`(−3, 0)`", "ok": True, "feedback": "Exacto: x = 3·cos(π) = −3 e y = 3·sen(π) = 0."},
                    {"text": "`(3, 0)`", "ok": False, "feedback": "cos(180°) es −1, no +1."},
                    {"text": "`(0, 3)`", "ok": False, "feedback": "Eso corresponde a θ = π/2 (90°)."},
                ],
            },
            {
                "question": "Al plantear el área de UN solo pétalo de `r = 2·cos(3θ)`, ¿qué expresión va dentro de la integral?",
                "options": [
                    {"text": "`(1/2) · (2·cos(3θ))² = 2·cos²(3θ)`", "ok": True, "feedback": "Exacto: siempre es (1/2)·r²."},
                    {"text": "`2·cos(3θ)`", "ok": False, "feedback": "Te faltó elevar r al cuadrado y multiplicar por 1/2."},
                    {"text": "`π · (2·cos(3θ))²`", "ok": False, "feedback": "No lleva π afuera: el ángulo dθ en radianes ya aporta el factor circular (1/2)r²dθ."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras por qué la fórmula del área polar es `(1/2) ∫ r² dθ` y cómo se aplica entre dos curvas.",
    },
    "c2-series-convergencia": {
        "hook": "Sumar infinitos números es engañoso: `1 + 1/2 + 1/3 + 1/4 + ...` explota a infinito, pero basta cambiarle un signo sí y uno no (`1 − 1/2 + 1/3 − 1/4 + ...`) para que converja exactamente a `ln(2)`!",
        "concept": {
            "points": [
                "**1.er filtro (n-ésimo término)**: si `lim a_n ≠ 0`, la serie **diverge seguro**. Si `lim a_n = 0`, NO alcanza (ejemplo famoso: la **serie armónica `∑ 1/n`** diverge!).",
                "**Familias de referencia**: geométrica `∑ a·rⁿ` converge ⇔ **`|r| < 1`**; **p-serie** `∑ 1/n^p` converge ⇔ **`p > 1`**. Usalas para comparar series parecidas.",
                "**Pruebas estrella**: **Alternantes** (`∑ (−1)ⁿ b_n`): converge si `b_n` baja hacia `0`, y el error al cortar es **`≤ primer término omitido`**. **Prueba de la Razón** (ideal con factoriales `n!` y potencias `cⁿ`): `L = lim |a_{n+1}/a_n|` → **`L < 1`** converge absolutamente, **`L > 1`** diverge, **`L = 1`** indeciso.",
            ],
            "real_world": [
                {
                    "title": "Estabilidad de filtros digitales y audio (IIR)",
                    "detail": "Un filtro de audio es estable (no satura ni revienta los parlantes) si y solo si la serie infinita de su respuesta al impulso converge absolutamente.",
                },
                {
                    "title": "Precisión garantizada en cálculo científico",
                    "detail": "La cota de error alternante te dice exactamente cuántos términos sumar para garantizar `10` decimales exactos sin desperdiciar CPU.",
                },
                {
                    "title": "Valoración financiera perpetua y física estadística",
                    "detail": "Probar convergencia asegura que la energía total o el valor de un flujo infinito tenga un resultado físico finito y real.",
                },
            ],
            "key_rule": "lim a_n ≠ 0 ⇒ diverge | p-serie converge ⇔ p > 1 | Alternante: error ≤ 1er término omitido | Razón: L < 1 converge.",
            "pitfall": "Creer que `lim a_n = 0` prueba convergencia: ¡FALSO! La serie armónica `∑ 1/n` tiene `1/n → 0` y sin embargo diverge a `+∞`.",
        },
        "example": {
            "title": "Clasificar ∑ 1/n², ∑ 1/√n y ∑ 2ⁿ/n!",
            "steps": [
                "`∑ 1/n²` es una p-serie con `p = 2 > 1` → **converge**.",
                "`∑ 1/√n = ∑ 1/n^(1/2)` es una p-serie con `p = 0.5 ≤ 1` → **diverge**.",
                "`∑ 2ⁿ/n!` con Prueba de la Razón: `|a_{n+1}/a_n| = (2ⁿ⁺¹/(n+1)!) · (n!/2ⁿ) = 2/(n + 1) → 0 < 1` → **converge absolutamente**.",
            ],
            "lab_link": "math:parametric_series",
            "lab_cta": "Practicar series y Taylor en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál de estas series CONVERGE?",
            "options": [
                {"text": "`∑ 1 / n³` (`p = 3 > 1`)", "ok": True, "feedback": "Exacto: es una p-serie con exponente mayor a 1."},
                {"text": "`∑ 1 / n` (`p = 1`)", "ok": False, "feedback": "Es la serie armónica, que diverge."},
                {"text": "`∑ n / (n + 5)` (`lim = 1 ≠ 0`)", "ok": False, "feedback": "Diverge por la prueba del n-ésimo término."},
            ],
        },
        "checks": [
            {
                "question": "Si una serie alternante `∑ (−1)ⁿ b_n` converge, ¿qué diferencia hay entre convergencia absoluta y condicional?",
                "options": [
                    {"text": "Absoluta = también converge `∑ |a_n|` sin signos; condicional = solo converge gracias a los signos alternos", "ok": True, "feedback": "Exacto: por ej. ∑ (−1)ⁿ/n² es absoluta, mientras ∑ (−1)ⁿ/n es condicional."},
                    {"text": "Absoluta significa que suma a un número positivo", "ok": False, "feedback": "Se refiere a si la serie de valores absolutos ∑ |a_n| sigue convergiendo."},
                    {"text": "No existe ninguna diferencia", "ok": False, "feedback": "Las condicionalmente convergentes son tan delicadas que reordenar sus términos cambia la suma!"},
                ],
            },
            {
                "question": "Al aplicar la Prueba de la Razón a `∑ n! / 3ⁿ`, `|a_{n+1}/a_n| = (n + 1) / 3 → ∞`. ¿Qué concluís?",
                "options": [
                    {"text": "Diverge (`L = ∞ > 1`: el factorial le gana siempre a la exponencial)", "ok": True, "feedback": "Exacto: n! crece mucho más rápido que 3ⁿ."},
                    {"text": "Converge", "ok": False, "feedback": "Converge cuando L < 1; aquí L = ∞ > 1."},
                    {"text": "Indeciso", "ok": False, "feedback": "Solo es indeciso cuando L = 1."},
                ],
            },
        ],
        "takeaway_prompt": "Armá tu orden rápido de chequeo para decidir si una serie infinita converge o diverge.",
    },
    "c2-taylor-maclaurin": {
        "hook": "¿Cómo calcula tu computadora `sen(0.4)` o `e^(0.2)` si un procesador solo sabe sumar y multiplicar? Los aproxima con polinomios: series de Taylor cortadas después de unos pocos términos.",
        "concept": {
            "points": [
                "**Polinomio de Taylor centrado en `a`**: iguala el valor y todas las derivadas de `f` en `a`: **`f(x) ≈ ∑ [f^(n)(a) / n!] · (x − a)ⁿ`** (cuando `a = 0` se llama **Maclaurin**).",
                "**4 series de Maclaurin para saber de memoria**: **`1/(1 − x) = 1 + x + x² + x³ + ...`** (`|x| < 1`); **`eˣ = 1 + x + x²/2! + x³/3! + ...`**; **`cos(x) = 1 − x²/2! + x⁴/4! − ...`** (pares); **`sen(x) = x − x³/3! + x⁵/5! − ...`** (impares).",
                "**Radio de convergencia `R`** (hallado con Prueba de la Razón + chequear extremos) indica dónde la serie representa exactamente a `f`. Y enchufando `x = iθ` en `eˣ` brota la **Fórmula de Euler: `e^(iθ) = cos θ + i·sen θ`**!",
            ],
            "real_world": [
                {
                    "title": "Cómo calculan sen, cos y exp los chips y librerías `math`",
                    "detail": "Dentro de tu CPU y de Python, `math.sin(x)` y `math.exp(x)` se evalúan con polinomios inspirados en Taylor a velocidad de nanosegundos.",
                },
                {
                    "title": "Física: relatividad y pequeñas oscilaciones",
                    "detail": "Expandir `E = γmc²` con `γ = 1/√(1 − v²/c²)` en serie de Taylor da `mc² + ½mv² + …`: después de la energía en reposo, el primer término es la energía cinética clásica!",
                },
                {
                    "title": "Fórmula de Euler en electrónica, mecánica cuántica y audio",
                    "detail": "`e^(iωt) = cos(ωt) + i·sen(ωt)` convierte derivar una onda sinusoidal en multiplicar por `iω`, e integrarla en dividir por `iω`.",
                },
            ],
            "key_rule": "Taylor: ∑ [f^(n)(a)/n!](x − a)ⁿ | eˣ = ∑ xⁿ/n! | cos = pares ± | sen = impares ± | e^(iθ) = cos θ + i·sen θ.",
            "pitfall": "Olvidar dividir por `n!` en cada término de Taylor o usar grados en vez de radianes al enchufar un ángulo en la serie de `sen(x)` o `cos(x)`.",
        },
        "example": {
            "title": "Aproximar cos(0.2) y derivar la serie de e^(−x²) por sustitución",
            "steps": [
                "Con `cos(x) ≈ 1 − x²/2`, en `x = 0.2 rad`: `1 − 0.04/2 = 0.98` (real `0.98007`!).",
                "Para hallar la serie de `e^(−x²)` NO hace falta derivar 5 veces: simplemente reemplazás `x` por `−x²` en `eˣ = 1 + x + x²/2! + ...`!",
                "Queda `e^(−x²) = 1 − x² + x⁴/2! − x⁶/3! + ...`, lo que hasta te permite integrar la campana de Gauss término a término!",
            ],
            "lab_link": "math:parametric_series",
            "lab_cta": "Practicar Taylor y aproximaciones en el Laboratorio",
        },
        "check": {
            "question": "Si una función tiene `f(0) = 3`, `f'(0) = −2` y `f''(0) = 10`, ¿cuál es su polinomio de Maclaurin de grado 2?",
            "options": [
                {"text": "`3 − 2x + 5x²` (porque `10 / 2! = 5`)", "ok": True, "feedback": "Exacto: c₀ = 3, c₁ = −2/1! = −2 y c₂ = 10/2! = 5."},
                {"text": "`3 − 2x + 10x²`", "ok": False, "feedback": "Te faltó dividir la segunda derivada por 2! = 2."},
                {"text": "`3 + 2x + 5x²`", "ok": False, "feedback": "Revisá el signo de f'(0) = −2."},
            ],
        },
        "checks": [
            {
                "question": "Usando `eˣ = 1 + x + x²/2! + ...`, ¿cuáles son los primeros 3 términos de la serie de Maclaurin de `e^(2x)`?",
                "options": [
                    {"text": "`1 + 2x + 2x²` (`(2x)² / 2 = 4x²/2 = 2x²`)", "ok": True, "feedback": "Exacto: sustituís x → 2x y simplificás 4x²/2 = 2x²."},
                    {"text": "`1 + 2x + 4x²`", "ok": False, "feedback": "Te faltó dividir (2x)² por 2! = 2."},
                    {"text": "`2 + 2x + x²`", "ok": False, "feedback": "e^(2·0) = e⁰ = 1, no 2."},
                ],
            },
            {
                "question": "Si el radio de convergencia de una serie centrada en `a = 5` es `R = 2`, ¿en qué intervalo abierto converge seguro?",
                "options": [
                    {"text": "`(3, 7)` (de `5 − 2` a `5 + 2`)", "ok": True, "feedback": "Exacto: el intervalo siempre es simétrico alrededor del centro a = 5 (luego se chequean los bordes 3 y 7)."},
                    {"text": "`(−2, 2)`", "ok": False, "feedback": "Eso sería si estuviera centrada en a = 0."},
                    {"text": "`(0, 7)`", "ok": False, "feedback": "El radio 2 se mide para ambos lados desde el centro 5."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras cómo te permiten las series de Taylor integrar funciones difíciles (como `e^(−x²)`) y deducir `e^(iπ) + 1 = 0`.",
    },
}
