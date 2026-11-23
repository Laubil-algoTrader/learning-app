"""Differential Equations curriculum (6 units, #100-#105) adapted from Khan Academy.

Covers all college Differential Equations methods building on Cálculo 1/2 (#83, #87)
and Cálculo multivariable (#95):
  - First-order linear ODEs (integrating factor μ(x) = e^(∫P dx)) & homogeneous 1st-order
  - Exact differential equations (M dx + N dy = 0, ∂M/∂y = ∂N/∂x) & potential reconstruction
  - Second-order homogeneous linear ODEs: characteristic equation & damping regimes
  - Non-homogeneous 2nd-order ODEs: undetermined coefficients, superposition & resonance
  - Laplace transform: table, derivatives L{y'} = sY - y(0), inverse Laplace & IVPs
  - Shifting theorems, unit step (Heaviside), Dirac delta impulse & Convolution Theorem
"""

from __future__ import annotations

DIFFEQ_NODES: list[dict] = [
    # ==================== NIVEL 37: 1.ER ORDEN Y 2.° ORDEN LINEAL ====================
    {
        "slug": "de-factor-integrante",
        "title": "100. EDOs lineales de 1.er orden: factor integrante y homogéneas",
        "level": 37,
        "order_index": 100,
        "summary": "Resolver y' + P(x)y = Q(x) con μ(x) = e^(∫P dx), problemas de mezclas/circuitos RL y sustitución v = y/x.",
        "prerequisites": ["c1-ecuaciones-diferenciales", "c2-partes-fracciones"],
        "metadata": {"section": "Ecuaciones diferenciales", "lab_tab": "diff_eqs", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Resolver y' + 3y = 6 con factor integrante e^(3x)",
                "prompt": "Multiplicando y' + 3y = 6 por μ(x) = e^(3x) queda (e^(3x)·y)' = 6e^(3x) → y(x) = 2 + C·e^(−3x). Si la condición inicial es y(0) = 5, ¿cuánto vale la constante C? Respondé solo con el número.",
                "answer": "3: en x = 0, 5 = 2 + C·e⁰ → C = 3 (solución exacta: y(x) = 2 + 3e^(−3x)).",
                "hints": ["Sustituí x = 0 e y = 5 en y(x) = 2 + C·e^(−3x)."],
                "payload": {
                    "lab_link": "math:diff_eqs",
                    "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Valor de equilibrio (estado estacionario) cuando x → ∞",
                "prompt": "En la solución anterior y(x) = 2 + 3e^(−3x) (por ejemplo, la corriente de un circuito RL o sal en un tanque), ¿a qué valor constante se estabiliza y cuando x → ∞? Respondé solo con el número.",
                "answer": "2: el término transitorio 3e^(−3x) cae a 0, dejando únicamente el estado estacionario y = 2.",
                "hints": ["Calculá lim(x → ∞) de (2 + 3e^(−3x))."],
                "payload": {"check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Calcular el factor integrante μ(x) = e^(∫ (2/x) dx)",
                "prompt": "En la ecuación lineal normalizada y' + (2/x)y = x², tenés P(x) = 2/x (para x > 0). ¿Cuál es su factor integrante μ(x) = e^(∫ (2/x) dx)?",
                "answer": "x²: ∫ (2/x) dx = 2·ln(x) = ln(x²) → e^(ln(x²)) = x² (¡ojo: no es 2x!).",
                "hints": ["Subí el 2 como exponente dentro del logaritmo antes de cancelar e y ln: e^(ln(x²))."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["x²", "2x", "e^(2/x)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Paso obligatorio antes de leer P(x)",
                "prompt": "Para hallar el factor integrante de x·y' + 4y = x³, ¿qué tenés que hacer ANTES de leer P(x)?",
                "answer": "Dividir toda la ecuación por x para dejar y' sola con coeficiente 1: y' + (4/x)y = x² (entonces P(x) = 4/x, no 4!).",
                "hints": ["La fórmula μ = e^(∫P dx) solo funciona en forma estándar 1·y' + P(x)y = Q(x)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Dividir todo por x para dejar y' con coeficiente 1 (P(x) = 4/x)",
                            "Tomar directamente P(x) = 4",
                            "Integrar x³ directamente",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Por qué funciona el truco del factor integrante",
                "prompt": "¿Qué regla de derivación transforma el lado izquierdo μ(x)·y' + μ(x)·P(x)·y en una sola derivada (μ·y)'?",
                "answer": "La regla del producto en reversa: elegimos μ tal que μ' = μ·P, haciendo que μ·y' + μ'·y = (μ·y)' se integre de un golpe!",
                "hints": ["Expandí (μ · y)' por regla del producto."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Regla del producto en reversa: (μ·y)' = μ·y' + μ'·y",
                            "Regla de L'Hôpital",
                            "Integración por partes",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Sustitución para EDOs homogéneas de 1.er orden",
                "prompt": "Una EDO de primer orden donde todo se puede escribir como función del cociente y/x (ej. dy/dx = (x + y)/x = 1 + y/x) se llama homogénea de 1.er orden. ¿Qué sustitución la convierte en separable?",
                "answer": "v = y / x (es decir y = v·x, dy/dx = v + x·dv/dx): siempre cancela la x y deja una ecuación separable en v y x.",
                "hints": ["Renombrá el cociente y/x con una nueva variable v."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["v = y / x (y = v·x)", "v = x + y", "v = x · y"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "de-ecuaciones-exactas",
        "title": "101. Ecuaciones diferenciales exactas (M dx + N dy = 0)",
        "level": 37,
        "order_index": 101,
        "summary": "Test de exactitud ∂M/∂y = ∂N/∂x, reconstrucción de la función potencial Ψ(x, y) = C y factores integrantes de exactitud.",
        "prerequisites": ["de-factor-integrante", "mv-divergencia-rotacional"],
        "metadata": {"section": "Ecuaciones diferenciales", "lab_tab": "diff_eqs", "est_minutes": 18},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Ajustar una constante k para que la ecuación sea exacta",
                "prompt": "Una EDO M dx + N dy = 0 es exacta cuando ∂M/∂y = ∂N/∂x. ¿Cuánto debe valer k para que (k·x·y + 1) dx + (2x² + 3y) dy = 0 sea exacta? Respondé solo con el número.",
                "answer": "4: ∂M/∂y = kx y ∂N/∂x = 4x; igualando kx = 4x obtenemos k = 4.",
                "hints": ["Derivá M = kxy + 1 respecto de y, y N = 2x² + 3y respecto de x.", "Igualá ∂M/∂y = kx con ∂N/∂x = 4x."],
                "payload": {
                    "lab_link": "math:diff_eqs",
                    "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Evaluar la constante C del potencial Ψ(x, y) = C",
                "prompt": "La ecuación exacta (2x + y) dx + (x + 6y) dy = 0 tiene solución potencial Ψ(x, y) = x² + xy + 3y² = C. Si la curva solución pasa por el punto (1, 2), ¿cuánto vale C? Respondé solo con el número.",
                "answer": "15: Ψ(1, 2) = 1² + (1)(2) + 3(2²) = 1 + 2 + 12 = 15.",
                "hints": ["Evaluá x² + xy + 3y² en x = 1, y = 2."],
                "payload": {"check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Comprobar si una ecuación es exacta",
                "prompt": "¿Es exacta la ecuación diferencial (3x² + y) dx + (x + 2y) dy = 0?",
                "answer": "Sí: ∂M/∂y = 1 y ∂N/∂x = 1 (son iguales, así que existe un potencial Ψ = x³ + xy + y² = C).",
                "hints": ["Calculá ∂(3x² + y)/∂y y ∂(x + 2y)/∂x."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Sí, es exacta (∂M/∂y = 1 = ∂N/∂x)",
                            "No es exacta",
                            "Solo es exacta en x = 0",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Conexión entre ecuaciones exactas y Cálculo multivariable",
                "prompt": "¿A qué concepto de Cálculo multivariable equivale exactamente una ecuación diferencial exacta M dx + N dy = 0?",
                "answer": "A un campo conservativo F = ⟨M, N⟩ = ∇Ψ: las soluciones son las curvas de nivel Ψ(x, y) = C donde dΨ = 0.",
                "hints": ["Mirá el test ∂M/∂y = ∂N/∂x: es exactamente rot₂D(F) = 0."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "A un campo conservativo ⟨M, N⟩ = ∇Ψ con soluciones Ψ(x, y) = C",
                            "Al Teorema de Gauss en 3D",
                            "A una divergencia nula",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Cuidado al integrar M respecto de x en el método de exactas",
                "prompt": "Al reconstruir Ψ(x, y) integrando M(x, y) respecto de x, ¿qué 'constante de integración' debés sumar?",
                "answer": "Una función arbitraria h(y) que puede depender de y (no un simple número C!), porque cualquier h(y) desaparece al derivar respecto de x.",
                "hints": ["¿Qué se vuelve 0 al calcular ∂/∂x? Todo lo que dependa solo de y!"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Una función desconocida h(y) que luego determinás con ∂Ψ/∂y = N",
                            "Solo un número constante C",
                            "Una función g(x)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Rescatar una ecuación no exacta con un factor integrante",
                "prompt": "La ecuación y dx − x dy = 0 NO es exacta (∂M/∂y = 1 ≠ −1 = ∂N/∂x). ¿Qué pasa si multiplicás toda la ecuación por μ(x) = 1 / x²?",
                "answer": "Se vuelve exacta: (y/x²) dx − (1/x) dy = 0 cumple ∂M/∂y = 1/x² = ∂N/∂x (su potencial es −y/x = C → y = kx).",
                "hints": ["Comprobá ∂(y/x²)/∂y y ∂(−1/x)/∂x."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Se vuelve exacta (∂M/∂y = 1/x² = ∂N/∂x)",
                            "Sigue siendo no exacta",
                            "Se vuelve de segundo orden",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "de-segundo-orden-homogeneas",
        "title": "102. EDOs de 2.° orden homogéneas: ecuación característica y osciladores",
        "level": 37,
        "order_index": 102,
        "summary": "Resolver ay'' + by' + cy = 0 mediante ar² + br + c = 0: raíces reales, repetidas (amortiguamiento crítico) y complejas (oscilaciones).",
        "prerequisites": ["c1-ecuaciones-diferenciales", "a2-numeros-complejos"],
        "metadata": {"section": "Ecuaciones diferenciales", "lab_tab": "diff_eqs", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Hallar las raíces de la ecuación característica",
                "prompt": "La EDO y'' − 5y' + 6y = 0 tiene ecuación característica r² − 5r + 6 = 0 → (r − 2)(r − 3) = 0. ¿Cuál es la MAYOR raíz r? Respondé solo con el número.",
                "answer": "3 (la solución general es y(t) = c₁e^(2t) + c₂e^(3t)).",
                "hints": ["Factorizá r² − 5r + 6 = 0."],
                "payload": {
                    "lab_link": "math:diff_eqs",
                    "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Caso raíz doble repetida (amortiguamiento crítico)",
                "prompt": "Para y'' + 6y' + 9y = 0, la ecuación característica (r + 3)² = 0 tiene una única raíz repetida r = −3. ¿Cuál es la solución general completa?",
                "answer": "(c₁ + c₂·t) · e^(−3t): multiplicamos la segunda solución por t para tener dos soluciones linealmente independientes.",
                "hints": ["Una EDO de 2.° orden necesita SIEMPRE dos soluciones independientes."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "y(t) = (c₁ + c₂·t) · e^(−3t)",
                            "y(t) = c₁e^(−3t) + c₂e^(−3t)",
                            "y(t) = c₁e^(−3t) + c₂e^(3t)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Frecuencia angular desde raíces complejas (oscilador amortiguado)",
                "prompt": "En y'' + 2y' + 5y = 0, las raíces características son r = −1 ± 2i, dando y(t) = e^(−t)(c₁cos(ωt) + c₂sen(ωt)). ¿Cuál es la frecuencia angular ω (en rad/s)? Respondé solo con el número.",
                "answer": "2 rad/s: la parte real (−1) gobierna el decaimiento e^(−t) y la parte imaginaria (2) es la frecuencia de oscilación ω!",
                "hints": ["En r = α ± βi, la frecuencia de oscilación es β."],
                "payload": {"check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "rad/s"}},
            },
            {
                "item_type": "worked_example",
                "title": "Frecuencia de un oscilador armónico sin fricción",
                "prompt": "Un sistema masa-resorte ideal cumple y'' + 16y = 0 (r² + 16 = 0 → r = ±4i). ¿Cuál es su frecuencia angular ω en rad/s? Respondé solo con el número.",
                "answer": "4 rad/s: y(t) = c₁·cos(4t) + c₂·sen(4t) (oscila eternamente sin perder amplitud porque α = 0).",
                "hints": ["Sacá la raíz cuadrada de 16."],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "rad/s"}},
            },
            {
                "item_type": "worked_example",
                "title": "Aplicar dos condiciones iniciales en 2.° orden",
                "prompt": "Para y'' − y = 0 (solución y(t) = c₁e^t + c₂e^(−t)), si y(0) = 4 (c₁ + c₂ = 4) y y'(0) = 2 (c₁ − c₂ = 2), ¿cuánto vale c₁? Respondé solo con el número.",
                "answer": "3: sumando ambas ecuaciones queda 2c₁ = 6 → c₁ = 3 (y c₂ = 1).",
                "hints": ["Sumá c₁ + c₂ = 4 con c₁ − c₂ = 2 y dividí por 2."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Los 3 regímenes físicos de un amortiguador (auto / circuito RLC)",
                "prompt": "Al diseñar la suspensión de un auto o un cierrapuertas (my'' + by' + ky = 0), querés que vuelva al reposo lo MÁS RÁPIDO posible sin rebotar. ¿Qué caso de la ecuación característica necesitás?",
                "answer": "Amortiguamiento crítico (Δ = b² − 4mk = 0, raíz real doble): vuelve sin oscilar y más rápido que el sobreamortiguado.",
                "hints": ["Δ < 0 rebota (subamortiguado); Δ > 0 tarda demasiado (sobreamortiguado); justo en el límite Δ = 0 es el óptimo."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Amortiguamiento crítico (Δ = 0, raíz repetida)",
                            "Subamortiguado (Δ < 0, raíces complejas)",
                            "Sin amortiguamiento (b = 0)",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "de-coeficientes-indeterminados",
        "title": "103. EDOs no homogéneas: coeficientes indeterminados y resonancia",
        "level": 37,
        "order_index": 103,
        "summary": "Solución general y = y_h + y_p, proponer plantillas para entradas externas, regla de modificación y fenómeno de resonancia.",
        "prerequisites": ["de-segundo-orden-homogeneas"],
        "metadata": {"section": "Ecuaciones diferenciales", "lab_tab": "diff_eqs", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Hallar una solución particular exponencial y_p = A·e^(3t)",
                "prompt": "En y'' − y' − 2y = 12·e^(3t) probás una solución particular y_p = A·e^(3t). Sustituila en la ecuación y hallá A. Respondé solo con el número.",
                "answer": "3: y_p' = 3A·e^(3t) e y_p'' = 9A·e^(3t), así que (9A − 3A − 2A)e^(3t) = 4A·e^(3t) = 12e^(3t) → A = 3 → solución particular y_p = 3e^(3t) (y la general es c₁e^(2t) + c₂e^(−t) + 3e^(3t)).",
                "hints": ["Derivá: y_p' = 3A·e^(3t) e y_p'' = 9A·e^(3t).", "Al sustituir queda 4A·e^(3t) = 12e^(3t); despejá A."],
                "payload": {
                    "lab_link": "math:diff_eqs",
                    "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Solución particular constante de estado estacionario",
                "prompt": "Para y'' + 3y' + 2y = 14 (fuerza constante 14), proponés una constante y_p = A (sus derivadas valen 0). ¿Cuánto vale A? Respondé solo con el número.",
                "answer": "7: 0 + 0 + 2A = 14 → A = 7 (como y_h = c₁e^(−t) + c₂e^(−2t) → 0, el sistema termina quieto en y = 7!).",
                "hints": ["Sustituí y_p = A, y'_p = 0, y''_p = 0 en y'' + 3y' + 2y = 14."],
                "payload": {
                    "lab_link": "math:diff_eqs",
                    "check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Plantilla obligatoria para una entrada senoidal o cosenoidal",
                "prompt": "En y'' + 2y' + 5y = 8·cos(3t), ¿qué forma debés proponer para la solución particular y_p(t)?",
                "answer": "A·cos(3t) + B·sen(3t): SIEMPRE incluís tanto seno como coseno porque la primera derivada 2y' mezcla cosenos con senos.",
                "hints": ["Si solo probás A·cos(3t), el término 2y' genera un sen(3t) que no se puede cancelar."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "y_p = A·cos(3t) + B·sen(3t)",
                            "y_p = A·cos(3t) solamente",
                            "y_p = A·e^(3t)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Regla de modificación y RESONANCIA en y'' + 4y = cos(2t)",
                "prompt": "En y'' + 4y = cos(2t), la solución homogénea ya es c₁cos(2t) + c₂sen(2t) (coincide con la frecuencia externa ω = 2!). ¿Cómo modificás la propuesta y_p?",
                "answer": "Multiplicás por t: y_p = t · (A·cos(2t) + B·sen(2t)). Físicamente esto significa RESONANCIA: la amplitud crece sin límite con el tiempo!",
                "hints": ["Cuando la fuerza externa empuja a la misma frecuencia natural, hay que multiplicar la plantilla por t."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Multiplicar por t: y_p = t(A·cos(2t) + B·sen(2t)) (resonancia)",
                            "Proponer y_p = A·cos(2t) + B·sen(2t) sin cambios",
                            "Proponer y_p = A (constante)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Estructura completa de la solución no homogénea",
                "prompt": "¿Cómo se arma SIEMPRE la solución general de ay'' + by' + cy = g(t)?",
                "answer": "y(t) = y_h(t) + y_p(t): la suma de la solución homogénea general (con c₁, c₂) más una solución particular (sin constantes libres).",
                "hints": ["Al meter y_h + y_p en el operador lineal, y_h da 0 e y_p da g(t)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "y = y_h + y_p (homogénea general + particular)",
                            "y = y_h · y_p",
                            "y = y_p solamente",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Transitorio vs. estado estacionario en sistemas amortiguados",
                "prompt": "Un circuito RLC amortiguado tiene solución y(t) = e^(−2t)(c₁cos 3t + c₂sen 3t) + 5·sen(4t). Después de unos segundos (t grande), ¿qué término describe el comportamiento real del circuito?",
                "answer": "Solo la solución particular 5·sen(4t) (estado estacionario): la parte homogénea tiene e^(−2t) → 0 y desaparece como transitorio inicial.",
                "hints": ["Mirá qué le pasa a e^(−2t) cuando t crece."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "5·sen(4t) (estado estacionario; la parte homogénea decae a 0)",
                            "Solo la parte homogénea",
                            "Ambos crecen al infinito",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 38: TRANSFORMADA DE LAPLACE ====================
    {
        "slug": "de-laplace-basica",
        "title": "104. Transformada de Laplace: de derivadas a álgebra",
        "level": 38,
        "order_index": 104,
        "summary": "Tabla esencial de Laplace, propiedad mágica L{y'} = sY − y(0), resolver PVI con álgebra y volver con Laplace inversa.",
        "prerequisites": ["c2-impropias-longitud", "de-segundo-orden-homogeneas"],
        "metadata": {"section": "Ecuaciones diferenciales", "lab_tab": "laplace_lab", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Transformada de Laplace de una potencia t³",
                "prompt": "La transformada de Laplace de una potencia sigue L{tⁿ} = n! / s^(n+1). Para t³ queda k / s⁴. ¿Cuánto vale el numerador k? Respondé solo con el número.",
                "answer": "6: L{t³} = 3! / s⁴ = 6 / s⁴.",
                "hints": ["Acá n = 3, así que el numerador es 3!.", "3! = 3 × 2 × 1."],
                "payload": {
                    "lab_link": "math:laplace_lab",
                    "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Transformada de Laplace de sen(4t)",
                "prompt": "La transformada de sen(ωt) es ω / (s² + ω²). En L{sen(4t)} = 4 / (s² + k), ¿cuánto vale la constante k del denominador? Respondé solo con el número.",
                "answer": "16: ω = 4 → ω² = 16 → L{sen(4t)} = 4 / (s² + 16) (en cambio L{cos(4t)} lleva s arriba: s / (s² + 16)).",
                "hints": ["Calculá ω² = 4²."],
                "payload": {
                    "lab_link": "math:laplace_lab",
                    "check": {"type": "numeric", "value": 16, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Evaluar la transformada de una exponencial 5·e^(3t)",
                "prompt": "Usando L{e^(at)} = 1 / (s − a) (para s > a), L{5·e^(3t)} = 5 / (s − 3). ¿Cuánto vale esa transformada F(s) evaluada en s = 5 en decimal? Respondé solo con el número.",
                "answer": "2.5: F(5) = 5 / (5 − 3) = 5 / 2 = 2.5.",
                "hints": ["Evaluá 5 / (5 − 3)."],
                "payload": {
                    "lab_link": "math:laplace_lab",
                    "check": {"type": "numeric", "value": 2.5, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Propiedad estrella: transformar una derivada L{y'}",
                "prompt": "¿En qué se convierte la derivada L{y'(t)} al aplicar la Transformada de Laplace (con Y(s) = L{y(t)})?",
                "answer": "s·Y(s) − y(0): derivar en el tiempo se transforma simplemente en MULTIPLICAR por s (e incorpora automáticamente la condición inicial y(0)!).",
                "hints": ["Se deduce en 2 renglones integrando ∫ e^(−st) y'(t) dt por partes."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "s·Y(s) − y(0)",
                            "Y(s) / s",
                            "s²·Y(s) − y'(0)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Resolver un PVI completo usando Laplace y su inversa",
                "prompt": "Aplicás Laplace a y' + 2y = 0 con y(0) = 5: queda (sY − 5) + 2Y = 0 → Y(s) = 5 / (s + 2). Volviendo al tiempo con L⁻¹{1/(s − a)} = e^(at), ¿cuál es y(t)?",
                "answer": "y(t) = 5·e^(−2t): como s + 2 = s − (−2), tenemos a = −2 y el 5 sale por linealidad.",
                "hints": ["Leé a = −2 en 5 / (s − (−2))."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["y(t) = 5·e^(−2t)", "y(t) = 5·e^(2t)", "y(t) = 5·cos(2t)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Laplace inversa por linealidad evaluada en t = 0",
                "prompt": "Si Y(s) = 3/s + 4/(s − 2), su transformada inversa es y(t) = 3 + 4·e^(2t). ¿Cuánto vale y(0)? Respondé solo con el número.",
                "answer": "7: 3 + 4·e⁰ = 3 + 4 = 7.",
                "hints": ["Sustituí t = 0 en 3 + 4·e^(2t)."],
                "payload": {"check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    {
        "slug": "de-laplace-escalon-impulso",
        "title": "105. Traslaciones, escalón (Heaviside), delta de Dirac y convolución",
        "level": 38,
        "order_index": 105,
        "summary": "Primer y segundo teorema de traslación, encender entradas con u_c(t), golpes instantáneos δ(t − c) y Teorema de Convolución.",
        "prerequisites": ["de-laplace-basica", "de-coeficientes-indeterminados"],
        "metadata": {"section": "Ecuaciones diferenciales", "lab_tab": "laplace_lab", "est_minutes": 22},
        "items": [
            {
                "item_type": "recall",
                "title": "Primer teorema de traslación (desplazamiento en s)",
                "prompt": "Sabés que L{cos(3t)} = s / (s² + 9). Por el 1.er teorema de traslación L{e^(at)·f(t)} = F(s − a), ¿cuál es L{e^(2t)·cos(3t)}?",
                "answer": "(s − 2) / ((s − 2)² + 9): multiplicar por e^(2t) en el tiempo simplemente reemplaza cada s por (s − 2)!",
                "hints": ["Sustituí TODAS las s de s / (s² + 9) por (s − 2)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "(s − 2) / ((s − 2)² + 9)",
                            "s / ((s − 2)² + 9)",
                            "(s + 2) / ((s + 2)² + 9)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Función escalón unitario u_c(t) (encender un interruptor)",
                "prompt": "¿Qué modela la función escalón de Heaviside u_5(t) (vale 0 si t < 5 y salta a 1 si t ≥ 5) y cuál es su transformada de Laplace?",
                "answer": "Modela encender una entrada/voltaje en t = 5 s, y su transformada es e^(−5s) / s (el factor e^(−cs) siempre indica un retardo de c segundos!).",
                "hints": ["Retardo de c segundos en el tiempo ↔ multiplicar por e^(−cs) en Laplace."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Un interruptor que se prende en t = 5; L{u_5(t)} = e^(−5s) / s",
                            "Un pulso instantáneo; L{u_5(t)} = 5",
                            "Una rampa lineal; L{u_5(t)} = 1 / s²",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Transformada de la delta de Dirac en t = 0",
                "prompt": "Un circuito o resorte recibe un golpe instantáneo de impulso unitario δ(t) en t = 0. ¿Cuál es su transformada de Laplace L{δ(t)}? Respondé solo con el número.",
                "answer": "1: L{δ(t)} = 1 (y para un golpe retrasado en t = c: L{δ(t − c)} = e^(−cs)).",
                "hints": ["Al evaluar e^(−s·0) da exactamente 1."],
                "payload": {"check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Propiedad de muestreo de la delta de Dirac",
                "prompt": "La delta de Dirac δ(t − c) 'pesca' el valor de una función exactamente en t = c: ∫(de 0 a ∞) f(t)·δ(t − c) dt = f(c). Calculá ∫(de 0 a ∞) (t² + 3)·δ(t − 4) dt. Respondé solo con el número.",
                "answer": "19: basta evaluar t² + 3 en t = 4 → 4² + 3 = 19!",
                "hints": ["Evaluá f(4) = 4² + 3."],
                "payload": {
                    "lab_link": "math:laplace_lab",
                    "check": {"type": "numeric", "value": 19, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Teorema de Convolución: L{f * g} = F(s) · G(s)",
                "prompt": "Si en el dominio de Laplace obtenés un producto Y(s) = H(s) · X(s), ¿a qué operación en el dominio del tiempo corresponde?",
                "answer": "A la CONVOLUCIÓN (h * x)(t) = ∫_0^t h(t − τ)·x(τ) dτ (¡nunca al producto simple h(t)·x(t)!).",
                "hints": ["Laplace convierte la difícil convolución integral en una simple multiplicación algebraica."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "A la convolución (h * x)(t) = ∫_0^t h(t − τ)x(τ) dτ",
                            "Al producto simple h(t) · x(t)",
                            "A la suma h(t) + x(t)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Denominador en el 1.er teorema de traslación",
                "prompt": "En L{e^(3t)·sen(4t)} = 4 / ((s − 3)² + 16), evaluá el denominador (s − 3)² + 16 cuando s = 6. Respondé solo con el número.",
                "answer": "25: (6 − 3)² + 16 = 9 + 16 = 25.",
                "hints": ["Calculá (6 − 3)² + 16."],
                "payload": {
                    "lab_link": "math:laplace_lab",
                    "check": {"type": "numeric", "value": 25, "tolerance": 0, "unit": ""},
                },
            },
        ],
    },
]

DIFFEQ_LESSONS: dict[str, dict] = {
    "de-factor-integrante": {
        "hook": "Casi ninguna ecuación lineal real como `y' + 3y = 6x` es separable, pero multiplicar ambos lados por el 'factor mágico' `e^(∫P dx)` la colapsa en una sola derivada integrable en 2 pasos.",
        "concept": {
            "points": [
                "Primero poné la ecuación en **forma estándar** (dividiendo para dejar `1·y'`): **`y' + P(x)·y = Q(x)`**.",
                "Calculás el **factor integrante `μ(x) = e^(∫ P(x) dx)`**. Al multiplicar toda la ecuación por `μ(x)`, el lado izquierdo se vuelve SIEMPRE la regla del producto: **`(μ(x) · y)' = μ(x) · Q(x)`**.",
                "Integrás ambos lados y dividís por `μ(x)`. Si en cambio la ecuación es **homogénea de 1.er orden** (`dy/dx = F(y/x)`), la sustitución **`v = y/x`** la vuelve separable.",
            ],
            "real_world": [
                {
                    "title": "Circuitos RL y RC con fuente conectada",
                    "detail": "La corriente en una bobina `L(dI/dt) + R·I = V` es una EDO lineal de 1.er orden: el factor integrante `e^((R/L)t)` da la curva exacta de carga.",
                },
                {
                    "title": "Problemas de mezclas y salmuera en tanques",
                    "detail": "Si entra agua salada y sale mezcla del tanque, la cantidad de sal cumple `S' + (r/V)S = tasa_entrada`, resuelta directo con factor integrante.",
                },
                {
                    "title": "Caída libre con resistencia del aire",
                    "detail": "La velocidad de un paracaidista `m·v' + b·v = mg` se resuelve con `μ(t) = e^((b/m)t)`, revelando su velocidad terminal `v_term = mg/b`.",
                },
            ],
            "key_rule": "1) Forma estándar y' + P(x)y = Q(x) | 2) μ = e^(∫P dx) | 3) (μ·y)' = μ·Q → integrar y despejar y.",
            "pitfall": "Olvidar dividir primero por el coeficiente de `y'` (ej. en `x·y' + 2y = x³`, `P(x)` es `2/x`, NO `2`) o olvidar la constante `+ C` ANTES de dividir por `μ(x)`!",
        },
        "example": {
            "title": "Resolver y' + 3y = 6 con condición inicial y(0) = 5",
            "steps": [
                "Ya está en forma estándar con `P(x) = 3` → factor integrante `μ(x) = e^(∫ 3 dx) = e^(3x)`.",
                "Multiplicamos todo por `e^(3x)`: `(e^(3x)·y)' = 6e^(3x)` → integramos ambos lados: `e^(3x)·y = 2e^(3x) + C`.",
                "Dividimos por `e^(3x)`: `y(x) = 2 + C·e^(−3x)`. Con `y(0) = 5` → `C = 3` → `y(x) = 2 + 3e^(−3x)`.",
            ],
            "lab_link": "math:diff_eqs",
            "lab_cta": "Practicar ecuaciones diferenciales en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es el factor integrante `μ(x)` para `y' − 4y = e^x`?",
            "options": [
                {"text": "`e^(−4x)`", "ok": True, "feedback": "Exacto: P(x) = −4 → ∫(−4)dx = −4x → μ(x) = e^(−4x)."},
                {"text": "`e^(4x)`", "ok": False, "feedback": "Ojo con el signo negativo en −4y."},
                {"text": "`−4x`", "ok": False, "feedback": "Falta elevar e a la integral: μ(x) = e^(∫P dx)."},
            ],
        },
        "checks": [
            {
                "question": "Si multiplicás `y' + (1/x)y = 3` por `μ(x) = x` (`x > 0`), ¿en qué derivada única se compacta el lado izquierdo?",
                "options": [
                    {"text": "`(x · y)'`", "ok": True, "feedback": "Exacto: por regla del producto (x·y)' = x·y' + 1·y, que coincide término a término!"},
                    {"text": "`(y / x)'`", "ok": False, "feedback": "Al multiplicar por x queda x·y' + y = (x·y)'."},
                    {"text": "`x · y'`", "ok": False, "feedback": "Desaparecería el término +y."},
                ],
            },
            {
                "question": "En `(e^(2x)·y)' = 4e^(2x)`, al integrar ambos lados queda `e^(2x)·y = 2e^(2x) + C`. ¿Cómo queda `y(x)` al despejar?",
                "options": [
                    {"text": "`y(x) = 2 + C·e^(−2x)` (la `C` también se divide por `e^(2x)`!)", "ok": True, "feedback": "Exacto: nunca pongas + C suelto al final sin dividirlo por μ(x)."},
                    {"text": "`y(x) = 2 + C`", "ok": False, "feedback": "Error clásico: C también queda dividido por e^(2x), convirtiéndose en C·e^(−2x)."},
                    {"text": "`y(x) = 2e^(2x) + C`", "ok": False, "feedback": "Te faltó dividir ambos términos de la derecha por e^(2x)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en tus palabras los 3 pasos del método del factor integrante y por qué `+ C` debe dividirse por `μ(x)`.",
    },
    "de-ecuaciones-exactas": {
        "hook": "Una ecuación exacta es simplemente un campo conservativo disfrazado: si pasa el test `∂M/∂y = ∂N/∂x`, su solución sale reconstruyendo la 'montaña de potencial' `Ψ(x, y) = C`.",
        "concept": {
            "points": [
                "Escrita como **`M(x, y) dx + N(x, y) dy = 0`**, es **exacta** si y solo si **`∂M/∂y = ∂N/∂x`** (el mismo test de rotacional cero de Cálculo multivariable).",
                "Cuando es exacta existe una función potencial `Ψ(x, y)` con `Ψ_x = M` y `Ψ_y = N`, así que la ecuación dice `dΨ = 0` y la solución general implícita es **`Ψ(x, y) = C`**.",
                "**Receta**: **1)** integrás `M` respecto de `x` sumando `h(y)`; **2)** derivás ese resultado respecto de `y` y lo igualás a `N` para hallar `h'(y)`; **3)** integrás `h'(y)` y escribís `Ψ(x, y) = C`.",
            ],
            "real_world": [
                {
                    "title": "Termodinámica: energía interna y entropía (diferenciales exactas)",
                    "detail": "Que `dU` sea una diferencial exacta significa que la energía de un gas depende solo del estado `(P, V, T)`, mientras el calor `δQ` NO es exacto y depende del proceso.",
                },
                {
                    "title": "Líneas equipotenciales en electrostática",
                    "detail": "Las soluciones `Ψ(x, y) = C` de `E_x dx + E_y dy = 0` dibujan directamente los contornos de voltaje constante.",
                },
                {
                    "title": "Líneas de corriente en fluidos ideales",
                    "detail": "Para un flujo incompresible 2D (`u_x + v_y = 0`), la ecuación `−v dx + u dy = 0` es exacta y sus curvas de nivel son las trayectorias exactas del fluido!",
                },
            ],
            "key_rule": "Test: ∂M/∂y = ∂N/∂x | Reconstruir: Ψ = ∫ M dx + h(y), luego ∂Ψ/∂y = N → solución Ψ(x, y) = C.",
            "pitfall": "Olvidar que `h(y)` puede ser una función de `y` (no solo una constante) al integrar `M` respecto de `x`, o escribir `Ψ(x, y)` solo sin igualarlo a `= C`.",
        },
        "example": {
            "title": "Resolver (2x + y) dx + (x + 6y) dy = 0",
            "steps": [
                "Test de exactitud: `∂(2x + y)/∂y = 1` y `∂(x + 6y)/∂x = 1` → coinciden, ¡es exacta!",
                "Integramos `M` respecto de `x`: `Ψ(x, y) = ∫(2x + y) dx = x² + xy + h(y)`.",
                "Derivamos en `y` e igualamos a `N`: `x + h'(y) = x + 6y` → `h'(y) = 6y` → `h(y) = 3y²` → solución: `x² + xy + 3y² = C`.",
            ],
            "lab_link": "math:diff_eqs",
            "lab_cta": "Practicar exactas y EDOs en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál de estas ecuaciones es EXACTA (`∂M/∂y = ∂N/∂x`)?",
            "options": [
                {"text": "`(2xy) dx + (x² + 5) dy = 0` (`2x = 2x`)", "ok": True, "feedback": "Exacto: ∂(2xy)/∂y = 2x y ∂(x² + 5)/∂x = 2x."},
                {"text": "`(2xy) dx + (x²y) dy = 0`", "ok": False, "feedback": "∂M/∂y = 2x, pero ∂N/∂x = 2xy (no coinciden)."},
                {"text": "`y dx + 2x dy = 0`", "ok": False, "feedback": "∂M/∂y = 1 ≠ 2 = ∂N/∂x."},
            ],
        },
        "checks": [
            {
                "question": "Si reconstruís `Ψ(x, y) = x²y + h(y)` y la ecuación tiene `N = x² + 4y`, ¿cuánto vale `h'(y)`?",
                "options": [
                    {"text": "`4y` (luego `h(y) = 2y²`)", "ok": True, "feedback": "Exacto: ∂Ψ/∂y = x² + h'(y) = x² + 4y → los x² se cancelan y queda h'(y) = 4y!"},
                    {"text": "`x² + 4y`", "ok": False, "feedback": "El x² ya vino de derivar x²y respecto de y; si lo volvés a sumar lo contás doble."},
                    {"text": "`0`", "ok": False, "feedback": "Falta el término +4y que depende solo de y."},
                ],
            },
            {
                "question": "En el paso `∂Ψ/∂y = N`, ¿qué pasa SIEMPRE si la ecuación de verdad era exacta?",
                "options": [
                    {"text": "Todos los términos con `x` se cancelan y `h'(y)` queda dependiendo SOLO de `y`", "ok": True, "feedback": "Exacto: es el mejor chequeo automático para saber que no te equivocaste en las cuentas!"},
                    {"text": "Desaparecen todas las `y`", "ok": False, "feedback": "h'(y) solo puede depender de y, nunca de x."},
                    {"text": "Siempre queda `h'(y) = 0`", "ok": False, "feedback": "Si N tiene términos puros en y (como 6y), h'(y) los captura."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en tres pasos cómo verificás y resolvés una ecuación diferencial exacta `M dx + N dy = 0`.",
    },
    "de-segundo-orden-homogeneas": {
        "hook": "Un péndulo, la suspensión de un auto y un circuito RLC con bobina y capacitor obedecen TODOS la misma ecuación `ay'' + by' + cy = 0` — y una simple cuadrática `ar² + br + c = 0` predice si rebotan o se frenan.",
        "concept": {
            "points": [
                "Al probar `y = e^(rt)` en **`ay'' + by' + cy = 0`** aparece la **ecuación característica `ar² + br + c = 0`** (la derivada solo baja `r` multiplicando!).",
                "**Los 3 casos del discriminante `Δ = b² − 4ac`** (los nombres entre paréntesis valen para un oscilador, con `a, b, c > 0`): **1) `Δ > 0`** (raíces reales `r₁ ≠ r₂`): `c₁e^(r₁t) + c₂e^(r₂t)` (sobreamortiguado). **2) `Δ = 0`** (raíz doble `r`): **`(c₁ + c₂t)e^(rt)`** (amortiguamiento crítico).",
                "**3) `Δ < 0`** (raíces complejas `α ± βi`): por la Fórmula de Euler se escribe en forma real como **`e^(αt) · (c₁cos(βt) + c₂sen(βt))`** (subamortiguado: oscila a frecuencia `β` mientras la envolvente `e^(αt)` decae, porque `α < 0`!).",
            ],
            "real_world": [
                {
                    "title": "Amortiguadores de autos y cierrapuertas (`Δ = 0`)",
                    "detail": "El amortiguamiento crítico devuelve la rueda al asfalto lo más rápido posible sin quedar rebotando (como pasa con amortiguadores gastados, `Δ < 0`).",
                },
                {
                    "title": "Circuitos RLC sintonizadores de radio",
                    "detail": "`L·q'' + R·q' + (1/C)·q = 0` es literalmente un oscilador amortiguado cuya frecuencia natural `ω = 1/√(LC)` sintoniza una emisora.",
                },
                {
                    "title": "Rascacielos y puentes frente al viento",
                    "detail": "Los ingenieros agregan grandes péndulos amortiguadores arriba de los rascacielos para empujar `α < 0` y apagar las oscilaciones rápido.",
                },
            ],
            "key_rule": "ar² + br + c = 0 | Reales: c₁e^(r₁t)+c₂e^(r₂t) | Doble: (c₁+c₂t)e^(rt) | Complejas α±βi: e^(αt)(c₁cos βt + c₂sen βt).",
            "pitfall": "Olvidar la `t` en el caso de raíz doble `(c₁ + c₂t)e^(rt)`, o confundir `α` (decaimiento) con `β` (frecuencia) en raíces complejas.",
        },
        "example": {
            "title": "Resolver y'' − 5y' + 6y = 0 y y'' + 2y' + 5y = 0",
            "steps": [
                "Para `y'' − 5y' + 6y = 0`: `r² − 5r + 6 = (r − 2)(r − 3) = 0` → `y(t) = c₁e^(2t) + c₂e^(3t)`.",
                "Para `y'' + 2y' + 5y = 0`: `r = (−2 ± √(4 − 20)) / 2 = −1 ± 2i` (`α = −1, β = 2`).",
                "Solución real oscilatoria: `y(t) = e^(−t) · (c₁·cos(2t) + c₂·sen(2t))`.",
            ],
            "lab_link": "math:diff_eqs",
            "lab_cta": "Practicar ecuaciones características en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es la solución general de `y'' − 4y' + 4y = 0` (`(r − 2)² = 0`)?",
            "options": [
                {"text": "`(c₁ + c₂t) · e^(2t)`", "ok": True, "feedback": "Exacto: raíz doble r = 2 lleva el factor t en el segundo término."},
                {"text": "`c₁e^(2t) + c₂e^(−2t)`", "ok": False, "feedback": "Eso corresponde a r² − 4 = 0 (y'' − 4y = 0), no a (r − 2)² = 0."},
                {"text": "`c₁cos(2t) + c₂sen(2t)`", "ok": False, "feedback": "Eso corresponde a raíces imaginarias ±2i (y'' + 4y = 0)."},
            ],
        },
        "checks": [
            {
                "question": "Si una ecuación característica tiene raíces `r = −3 ± 5i`, ¿cómo se comporta `y(t)` cuando `t → ∞`?",
                "options": [
                    {"text": "Oscila con frecuencia `5 rad/s` mientras su amplitud decae a `0` (`e^(−3t)`)", "ok": True, "feedback": "Exacto: parte real negativa (−3) garantiza estabilidad y amortiguamiento."},
                    {"text": "Crece sin límite oscilando", "ok": False, "feedback": "Crecería si la parte real α fuera positiva (+3)."},
                    {"text": "Oscila eternamente con amplitud constante", "ok": False, "feedback": "Eso ocurre solo cuando α = 0 (sin fricción)."},
                ],
            },
            {
                "question": "¿Qué ecuación diferencial tiene exactamente la solución general `c₁cos(3t) + c₂sen(3t)`?",
                "options": [
                    {"text": "`y'' + 9y = 0` (`r = ±3i`)", "ok": True, "feedback": "Exacto: r² + 9 = 0 da r = ±3i."},
                    {"text": "`y'' − 9y = 0`", "ok": False, "feedback": "y'' − 9y = 0 da exponenciales reales c₁e^(3t) + c₂e^(−3t)."},
                    {"text": "`y'' + 3y = 0`", "ok": False, "feedback": "Esa tendría frecuencia √3, no 3."},
                ],
            },
        ],
        "takeaway_prompt": "Resumí los 3 casos de `ar² + br + c = 0` (Δ > 0, Δ = 0, Δ < 0) y qué hace cada uno en un resorte real.",
    },
    "de-coeficientes-indeterminados": {
        "hook": "Cuando además de masa y resorte hay un motor o viento empujando desde afuera (`= g(t)`), la respuesta suma la reacción propia (`y_h`) más la respuesta forzada (`y_p`) — y si empujás al ritmo natural ocurre la resonancia.",
        "concept": {
            "points": [
                "En **`ay'' + by' + cy = g(t)`**, la solución general es SIEMPRE **`y = y_h + y_p`**: primero resolvés la homogénea `y_h` (`= 0`) y luego buscás una **solución particular `y_p`** imitando la forma de `g(t)`.",
                "**Tabla de plantillas `y_p`**: polinomio de grado `n` → polinomio completo de grado `n`; `k·e^(mt)` → `A·e^(mt)`; `cos(ωt)` o `sen(ωt)` → **`A·cos(ωt) + B·sen(ωt)`** (siempre ambos!).",
                "**Regla de modificación (Resonancia)**: si tu plantilla `y_p` ya aparece repetida adentro de `y_h`, **multiplicá `y_p` por `t`** (o `t²` si era raíz doble). En un oscilador sin fricción, eso hace crecer la amplitud sin límite!",
            ],
            "real_world": [
                {
                    "title": "Empujar una hamaca y resonancia estructural",
                    "detail": "Empujar justo a la frecuencia natural del columpio (`y_p = t·sen(ωt)`) inyecta energía en fase en cada ciclo; por eso los soldados rompen el paso al cruzar puentes.",
                },
                {
                    "title": "Sintonizar una radio o filtro de audio",
                    "detail": "En un circuito RLC forzado por una señal `V₀cos(ωt)`, la amplitud de estado estacionario `y_p` tiene un pico gigante en la frecuencia resonante de la estación deseada.",
                },
                {
                    "title": "Respuesta de un edificio ante un sismo",
                    "detail": "La parte homogénea `y_h` se apaga por amortiguamiento y `y_p` predice cuánto se sacudirá el edificio frente a una onda sísmica de frecuencia `ω`.",
                },
            ],
            "key_rule": "y = y_h + y_p | Proponé y_p con la misma familia que g(t) | Si choca con y_h, multiplicá por t (resonancia!).",
            "pitfall": "Proponer solo `A·sen(ωt)` cuando `g(t) = sen(ωt)` (siempre hacen falta seno Y coseno), o despejar `c₁, c₂` usando `y_h` sola en vez de la suma completa `y_h + y_p`!",
        },
        "example": {
            "title": "Resolver y'' − y' − 2y = 12·e^(3t)",
            "steps": [
                "Paso 1 (homogénea): `r² − r − 2 = (r − 2)(r + 1) = 0` → `y_h = c₁e^(2t) + c₂e^(−t)`.",
                "Paso 2 (particular): como `e^(3t)` NO choca con `e^(2t)` ni `e^(−t)`, proponemos `y_p = A·e^(3t)`.",
                "Sustituimos: `(9A − 3A − 2A)e^(3t) = 12e^(3t)` → `4A = 12` → `A = 3`. Solución general: `y = c₁e^(2t) + c₂e^(−t) + 3e^(3t)`.",
            ],
            "lab_link": "math:diff_eqs",
            "lab_cta": "Practicar coeficientes indeterminados en el Laboratorio",
        },
        "check": {
            "question": "Para `y'' − 5y' + 6y = 4·e^(2t)` (donde `y_h = c₁e^(2t) + c₂e^(3t)`), ¿qué plantilla correcta debés proponer para `y_p`?",
            "options": [
                {"text": "`A · t · e^(2t)` (multiplicada por `t` porque `e^(2t)` ya está en `y_h`!)", "ok": True, "feedback": "Exacto: sin la t, sustituir A·e^(2t) daría 0 = 4e^(2t) (imposible)."},
                {"text": "`A · e^(2t)`", "ok": False, "feedback": "Como r = 2 es raíz de la homogénea, A·e^(2t) se anula completamente en el lado izquierdo."},
                {"text": "`A · e^(3t)`", "ok": False, "feedback": "Cambiar el exponente a 3 nunca igualará a 4e^(2t)."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál es la plantilla `y_p` correcta para `y'' + 4y' + 3y = 6t + 1`?",
                "options": [
                    {"text": "`A·t + B` (polinomio lineal completo)", "ok": True, "feedback": "Exacto: derivar At genera una constante A, así que se necesita el término B."},
                    {"text": "`A·t` solamente", "ok": False, "feedback": "Te faltó el término independiente +B."},
                    {"text": "`A·t² + B·t + C`", "ok": False, "feedback": "Como r = 0 no es raíz de la homogénea, no hace falta subir a grado 2."},
                ],
            },
            {
                "question": "Si te dan condiciones iniciales `y(0)` y `y'(0)` en una EDO no homogénea, ¿en qué ecuación las sustituís para hallar `c₁` y `c₂`?",
                "options": [
                    {"text": "En la solución COMPLETA `y = y_h + y_p`", "ok": True, "feedback": "Exacto: y_p(0) también aporta al valor inicial; si solo usás y_h te quedan mal c₁ y c₂!"},
                    {"text": "Primero solo en `y_h`, y después sumás `y_p`", "ok": False, "feedback": "Eso viola y(0) porque y_p(0) se sumaría encima desplazando el valor inicial."},
                    {"text": "Solo en `y_p`", "ok": False, "feedback": "y_p no tiene constantes libres c₁, c₂."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en tus palabras qué es la resonancia y cómo se manifiesta algebraicamente al elegir `y_p`.",
    },
    "de-laplace-basica": {
        "hook": "La Transformada de Laplace es el atajo favorito de los ingenieros: convierte derivadas en multiplicaciones por `s`, resuelve la ecuación con álgebra elemental y mete las condiciones iniciales desde la línea 1.",
        "concept": {
            "points": [
                "Definición: **`F(s) = L{f(t)} = ∫_0^∞ e^(−st) f(t) dt`** (pasa del dominio del tiempo `t` al dominio de la frecuencia compleja `s`, y es **lineal**).",
                "**Tabla de bolsillo**: `1 → 1/s` | `tⁿ → n!/s^(n+1)` | `e^(at) → 1/(s − a)` | `sen(ωt) → ω/(s² + ω²)` | `cos(ωt) → s/(s² + ω²)`.",
                "**El superpoder (derivadas)**: **`L{y'} = s·Y(s) − y(0)`** y **`L{y''} = s²·Y(s) − s·y(0) − y'(0)`**. Despejás `Y(s)` con álgebra, separás en fracciones parciales y volvés al tiempo con **`L⁻¹{Y(s)}`**!",
            ],
            "real_world": [
                {
                    "title": "Ingeniería de control (drones, piloto automático, PID)",
                    "detail": "El diseño de controladores estables se hace casi 100% en el dominio de Laplace mirando dónde caen los polos (ceros del denominador de `Y(s)`).",
                },
                {
                    "title": "Análisis de circuitos RLC con impedancias `sL` y `1/(sC)`",
                    "detail": "Con Laplace, bobinas y capacitores se tratan como simples resistencias usando la Ley de Ohm algebraica sin resolver EDOs a mano.",
                },
                {
                    "title": "Estabilidad instantánea por polos",
                    "detail": "Si todos los polos de `Y(s)` tienen parte real negativa (`Re(s) < 0`), el sistema es estable y decae; si alguno es positivo, explota!",
                },
            ],
            "key_rule": "L{y'} = sY − y(0) | L{y''} = s²Y − s·y(0) − y'(0) | 1→1/s, e^(at)→1/(s−a), sen(ωt)→ω/(s²+ω²), cos(ωt)→s/(s²+ω²).",
            "pitfall": "Confundir `L{sen(ωt)}` (lleva constante `ω` arriba) con `L{cos(ωt)}` (lleva variable `s` arriba), o escribir `1/(s + a)` para `e^(+at)` (el signo va invertido!).",
        },
        "example": {
            "title": "Resolver y' + 2y = 0, y(0) = 5 usando Laplace",
            "steps": [
                "Transformamos toda la ecuación: `[s·Y(s) − y(0)] + 2·Y(s) = 0`.",
                "Sustituimos `y(0) = 5` y despejamos algebraicamente: `(s + 2)·Y(s) = 5` → `Y(s) = 5 / (s + 2)`.",
                "Aplicamos Laplace inversa mirando la tabla (`1/(s − a) ↔ e^(at)` con `a = −2`): `y(t) = 5·e^(−2t)`!",
            ],
            "lab_link": "math:laplace_lab",
            "lab_cta": "Practicar Transformada de Laplace en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es la Transformada de Laplace de `f(t) = 3·cos(5t)`?",
            "options": [
                {"text": "`3s / (s² + 25)`", "ok": True, "feedback": "Exacto: coseno lleva s en el numerador y ω² = 25 en el denominador."},
                {"text": "`15 / (s² + 25)`", "ok": False, "feedback": "Eso corresponde a 3·sen(5t), no a 3·cos(5t)."},
                {"text": "`3s / (s² + 5)`", "ok": False, "feedback": "En el denominador va ω² = 5² = 25, no 5."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál es la Transformada de Laplace inversa `L⁻¹{ 10 / (s² + 25) }`?",
                "options": [
                    {"text": "`2 · sen(5t)` (reescribiendo `2 · [5 / (s² + 5²)]`)", "ok": True, "feedback": "Exacto: ajustamos el numerador a ω = 5 sacando el factor 2 afuera."},
                    {"text": "`10 · sen(5t)`", "ok": False, "feedback": "Como L{sen(5t)} ya aporta un 5 arriba, 10 = 2 × 5 → coeficiente 2."},
                    {"text": "`2 · cos(5t)`", "ok": False, "feedback": "Para coseno necesitaría una s en el numerador."},
                ],
            },
            {
                "question": "Al aplicar Laplace a `y'' + 4y = 0` con `y(0) = 1` y `y'(0) = 0`, ¿qué ecuación algebraica obtenés?",
                "options": [
                    {"text": "`(s² + 4)·Y(s) = s` → `Y(s) = s / (s² + 4)` (`y = cos(2t)`)", "ok": True, "feedback": "Exacto: L{y''} = s²Y − s(1) − 0 = s²Y − s!"},
                    {"text": "`(s² + 4)·Y(s) = 1`", "ok": False, "feedback": "En L{y''}, y(0) va multiplicado por s (s·y(0)), no solo."},
                    {"text": "`(s + 4)·Y(s) = s`", "ok": False, "feedback": "La segunda derivada multiplica por s², no por s."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá los 3 pasos del método de Laplace para resolver un problema de valor inicial y qué ventaja tiene sobre el método clásico.",
    },
    "de-laplace-escalon-impulso": {
        "hook": "¿Cómo modelás un interruptor que se prende a los 5 segundos o un golpe seco de martillo en `t = 2`? Los métodos clásicos se traban con funciones a saltos, pero Laplace los maneja sin pestañear.",
        "concept": {
            "points": [
                "**1.er Teorema de Traslación (en `s`)**: multiplicar por una exponencial `e^(at)` en el tiempo simplemente corre `s → (s − a)`: **`L{e^(at)·f(t)} = F(s − a)`** (ideal para oscilaciones amortiguadas!).",
                "**Escalón de Heaviside `u_c(t)` y 2.° Teorema (en `t`)**: `u_c(t)` vale `0` antes de `c` y `1` desde `c` en adelante. Retrasar una función `c` segundos multiplica su transformada por **`e^(−cs)`**: **`L{u_c(t)·f(t − c)} = e^(−cs)·F(s)`**.",
                "**Impulso delta de Dirac `δ(t − c)`** (golpe instantáneo de área `1`): **`L{δ(t − c)} = e^(−cs)`** (`L{δ(t)} = 1`) y muestreo `∫ f(t)δ(t − c)dt = f(c)`. Y **Convolución**: **`L{f * g} = F(s)·G(s)`**.",
            ],
            "real_world": [
                {
                    "title": "Respuesta al impulso y reverberación en audio",
                    "detail": "Grabar un solo chasquido `δ(t)` en una catedral captura su respuesta al impulso `h(t)`; convolucionar cualquier guitarra con `h(t)` la hace sonar adentro de la catedral!",
                },
                {
                    "title": "Circuitos digitales y fuentes conmutadas (PWM)",
                    "detail": "Prender y apagar pulsos cuadrados de voltaje en milisegundos se escribe directo como diferencias de escalones `u_a(t) − u_b(t)`.",
                },
                {
                    "title": "Impactos y choques mecánicos",
                    "detail": "Una pelota golpeada por una raqueta o una descarga de rayo en una línea eléctrica se modelan exactamente con `J · δ(t − c)`.",
                },
            ],
            "key_rule": "e^(at)f(t) ↔ F(s−a) | u_c(t)f(t−c) ↔ e^(−cs)F(s) | δ(t−c) ↔ e^(−cs) | (f * g) ↔ F(s)·G(s).",
            "pitfall": "Usar `e^(−cs)` en el segundo teorema olvidando que la función también debe estar desplazada como `f(t − c)` (no `f(t)` sin correr!), o confundir convolución con multiplicación ordinaria.",
        },
        "example": {
            "title": "Usar traslación en L{e^(3t)·sen(4t)} y evaluar ∫ (t² + 3)δ(t − 4) dt",
            "steps": [
                "Sabemos que `L{sen(4t)} = 4 / (s² + 16)`.",
                "Por el 1.er teorema de traslación, multiplicar por `e^(3t)` cambia `s → (s − 3)`: `4 / ((s − 3)² + 16)`.",
                "Por la propiedad de muestreo de Dirac, `∫_0^∞ (t² + 3)·δ(t − 4) dt` simplemente evalúa `t² + 3` en `t = 4` → `19`!",
            ],
            "lab_link": "math:laplace_lab",
            "lab_cta": "Practicar traslaciones y Laplace en el Laboratorio",
        },
        "check": {
            "question": "¿Qué representa la expresión `u_2(t) − u_5(t)` en función del tiempo `t`?",
            "options": [
                {"text": "Un pulso cuadrado que vale `1` entre `t = 2` y `t = 5`, y `0` afuera", "ok": True, "feedback": "Exacto: en t = 2 se prende (+1) y en t = 5 se apaga (−1)."},
                {"text": "Una rampa que sube de 2 a 5", "ok": False, "feedback": "Son escalones planos de altura 1, no rampas."},
                {"text": "Vale `1` en todo `t ≥ 0`", "ok": False, "feedback": "Antes de t = 2 vale 0 − 0 = 0, y después de t = 5 vale 1 − 1 = 0."},
            ],
        },
        "checks": [
            {
                "question": "Si ves `e^(−4s) · (1 / s²)` al hacer una Transformada de Laplace inversa, ¿qué función del tiempo es?",
                "options": [
                    {"text": "`u_4(t) · (t − 4)` (una rampa `t` encendida y retrasada `4` segundos)", "ok": True, "feedback": "Exacto: 1/s² ↔ t, y el factor e^(−4s) enciende y desplaza t → (t − 4) en t = 4!"},
                    {"text": "`e^(−4t) · t`", "ok": False, "feedback": "e^(−4t)·t tendría (s + 4)² abajo (1.er teorema), no e^(−4s) multiplicando arriba."},
                    {"text": "`u_4(t) · t` (sin desplazar `t`)", "ok": False, "feedback": "El 2.° teorema exige desplazar también el argumento: f(t − 4) = t − 4."},
                ],
            },
            {
                "question": "¿Cuál es la transformada de Laplace de un impulso unitario retrasado a los `3` segundos, `δ(t − 3)`?",
                "options": [
                    {"text": "`e^(−3s)`", "ok": True, "feedback": "Exacto: sin dividir por s (e^(−3s)/s sería el escalón u_3(t))."},
                    {"text": "`e^(−3s) / s`", "ok": False, "feedback": "Eso corresponde al escalón unitario u_3(t), no al impulso δ(t − 3)."},
                    {"text": "`3`", "ok": False, "feedback": "3 sería L{3·δ(t)} (golpe de intensidad 3 en t = 0)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá la diferencia práctica entre un escalón `u_c(t)` y una delta de Dirac `δ(t − c)`, y cómo Laplace simplifica la convolución.",
    },
}
