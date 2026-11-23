"""Calculus 1 (AP Calculus AB) curriculum (8 units, #77-#84) adapted from Khan Academy.

Covers all 8 core AP Calculus AB units building on Precálculo (#69-#76):
  - Limits at infinity, rationalizing 0/0, Squeeze Theorem & Intermediate Value Theorem
  - Differentiation: tangent slope, power, product, quotient, trig, exp & log rules
  - Chain Rule, implicit differentiation, inverse & higher-order derivatives
  - Contextual applications: kinematics (x -> v -> a), related rates, linearization & L'Hopital
  - Analytical applications: Mean Value Theorem, extrema, concavity & real-world optimization
  - Integration: Riemann sums, Fundamental Theorem of Calculus (1 & 2) & u-substitution
  - Differential equations: slope fields, separation of variables & exponential/cooling models
  - Applications of integration: average value, total distance, area between curves & volumes
"""

from __future__ import annotations

CALCULUS1_NODES: list[dict] = [
    # ==================== NIVEL 28: LÍMITES AVANZADOS Y DERIVADAS ====================
    {
        "slug": "c1-limites-avanzados",
        "title": "77. Límites al infinito, Sándwich y Valor Intermedio",
        "level": 28,
        "order_index": 77,
        "summary": "Comportamiento al infinito, racionalizar 0/0 con raíces, límite sen(x)/x, Teorema del Sándwich y Valor Intermedio (TVI).",
        "prerequisites": ["pc-limites-continuidad"],
        "metadata": {"section": "Cálculo 1", "lab_tab": "limits_intro", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Límite al infinito de un cociente de polinomios",
                "prompt": "Calculá lim(x → ∞) de (10x³ − 2x) / (2x³ + 5x² + 1). Respondé solo con el número.",
                "answer": "5: cuando x → ∞ solo importan los términos de mayor grado (10x³ / 2x³ = 5).",
                "hints": ["Compará los términos líderes arriba (10x³) y abajo (2x³)."],
                "payload": {
                    "lab_link": "math:limits_intro",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Destrabar 0/0 con raíz cuadrada (racionalizando)",
                "prompt": "Al racionalizar (√x − 2) / (x − 4) multiplicando arriba y abajo por (√x + 2), se cancela (x − 4) y queda 1 / (√x + 2). ¿Cuánto vale el límite cuando x → 4 en decimal? Respondé solo con el número.",
                "answer": "0.25 (1/4): evaluando 1 / (√4 + 2) = 1 / (2 + 2) = 1/4 = 0.25.",
                "hints": ["Sustituí x = 4 en 1 / (√x + 2)."],
                "payload": {
                    "lab_link": "math:limits_intro",
                    "check": {"type": "numeric", "value": 0.25, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Límite trigonométrico fundamental: sen(kx) / x",
                "prompt": "Sabiendo que lim(u → 0) sen(u) / u = 1 (en radianes), ¿cuánto vale lim(x → 0) sen(5x) / x? Respondé solo con el número.",
                "answer": "5: reescribimos como 5 · [sen(5x) / (5x)] → 5 × 1 = 5.",
                "hints": ["Multiplicá y dividí por 5 para armar 5 · sen(5x)/(5x)."],
                "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Aplicar el Teorema del Sándwich (compresión)",
                "prompt": "Una función g(x) siempre queda encerrada entre 2x − 1 ≤ g(x) ≤ x² cerca de x = 1. Como ambos bordes tienden al mismo valor cuando x → 1, ¿cuánto vale lim(x → 1) g(x)? Respondé solo con el número.",
                "answer": "1: por abajo 2(1) − 1 = 1 y por arriba 1² = 1, así que g(x) queda aplastada hacia 1.",
                "hints": ["Evaluá los dos extremos 2x − 1 y x² en x = 1."],
                "payload": {"check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Teorema del Valor Intermedio (TVI) para garantizar raíces",
                "prompt": "La temperatura f(t) es una función continua: a las 06:00 marcaba −3°C y a las 10:00 marcaba +5°C. ¿Qué asegura el Teorema del Valor Intermedio?",
                "answer": "Que en algún instante entre las 06:00 y las 10:00 la temperatura marcó exactamente 0°C (y cualquier valor entre −3 y +5).",
                "hints": ["Para pasar de −3 a +5 sin saltos, la curva tiene que cruzar obligatoriamente por 0."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Cruzó por 0°C al menos una vez entre las 06:00 y las 10:00",
                            "Subió a velocidad constante todo el tiempo",
                            "Alcanzó exactamente 0°C a las 08:00",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Jerarquía de crecimiento al infinito (exponencial vs. polinomio)",
                "prompt": "Cuando x → ∞, la exponencial eˣ crece infinitamente más rápido que cualquier potencia xⁿ. ¿Cuánto vale lim(x → ∞) x² / eˣ? Respondé solo con el número.",
                "answer": "0: el denominador eˣ aplasta a x² cuando x se hace gigante, llevando el cociente a 0.",
                "hints": ["Recordá el orden de velocidades: ln(x) ≪ xⁿ ≪ eˣ."],
                "payload": {"check": {"type": "numeric", "value": 0, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    {
        "slug": "c1-derivadas-reglas",
        "title": "78. La derivada: pendiente tangente y reglas básicas",
        "level": 28,
        "order_index": 78,
        "summary": "Derivada como tasa instantánea de cambio, regla de la potencia, producto, cociente y derivadas de sen, cos, eˣ y ln(x).",
        "prerequisites": ["c1-limites-avanzados"],
        "metadata": {"section": "Cálculo 1", "lab_tab": "derivatives", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Regla de la potencia evaluada en un punto",
                "prompt": "Dada f(x) = 4x³ − 5x + 7, su derivada es f'(x) = 12x² − 5. ¿Cuánto vale la pendiente de la recta tangente en x = 2 (es decir f'(2))? Respondé solo con el número.",
                "answer": "43: f'(2) = 12(2²) − 5 = 48 − 5 = 43 (la derivada de la constante +7 es 0).",
                "hints": ["Bajá el exponente multiplicando y restale 1: (4x³)' = 12x²; luego evaluá en x = 2."],
                "payload": {
                    "lab_link": "math:derivatives",
                    "check": {"type": "numeric", "value": 43, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Derivar una raíz cuadrada usando potencia fraccionaria",
                "prompt": "Como √x = x^(1/2), su derivada es (1/2)x^(−1/2) = 1 / (2√x). ¿Cuál es la pendiente de y = √x en x = 4 en decimal? Respondé solo con el número.",
                "answer": "0.25: 1 / (2√4) = 1 / 4 = 0.25.",
                "hints": ["Evaluá 1 / (2 × √4)."],
                "payload": {
                    "lab_link": "math:derivatives",
                    "check": {"type": "numeric", "value": 0.25, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Regla del producto: (f · g)' = f'g + fg'",
                "prompt": "Aplicá la regla del producto a h(x) = x² · (3x + 1) → h'(x) = 2x(3x + 1) + x²(3). ¿Cuánto vale h'(1)? Respondé solo con el número.",
                "answer": "11: 2(1)(4) + 1(3) = 8 + 3 = 11 (ojo: nunca es simplemente f' · g' = 2x · 3 = 6x!).",
                "hints": ["Evaluá 2(1)(3·1 + 1) + 1²(3)."],
                "payload": {
                    "lab_link": "math:derivatives",
                    "check": {"type": "numeric", "value": 11, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Regla del cociente: (f / g)' = (f'g − fg') / g²",
                "prompt": "Para f(x) = x / (x + 1), la regla del cociente da f'(x) = [1(x + 1) − x(1)] / (x + 1)² = 1 / (x + 1)². ¿Cuánto vale f'(1) en decimal? Respondé solo con el número.",
                "answer": "0.25: 1 / (1 + 1)² = 1 / 4 = 0.25.",
                "hints": ["Evaluá 1 / (1 + 1)²."],
                "payload": {"check": {"type": "numeric", "value": 0.25, "tolerance": 0.01, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Derivadas elementales imprescindibles (eˣ, ln x, sen x, cos x)",
                "prompt": "¿Cuál de estas tres listas de cuatro derivadas es 100% CORRECTA?",
                "answer": "(eˣ)' = eˣ, (ln x)' = 1/x, (sen x)' = cos x y (cos x)' = −sen x (ojo con el signo menos en la derivada del coseno!).",
                "hints": ["Recordá que todas las funciones 'co-' (cos, cot, csc) llevan signo negativo al derivar."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "(eˣ)' = eˣ, (ln x)' = 1/x, (sen x)' = cos x, (cos x)' = −sen x",
                            "(eˣ)' = x·eˣ⁻¹, (ln x)' = 1/x, (sen x)' = cos x, (cos x)' = sen x",
                            "(eˣ)' = eˣ, (ln x)' = eˣ, (sen x)' = −cos x, (cos x)' = sen x",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Continua pero NO derivable (esquinas y picos)",
                "prompt": "La función f(x) = |x| (en forma de 'V') es continua en x = 0. ¿Es derivable en x = 0?",
                "answer": "No: a la izquierda la pendiente es −1 y a la derecha es +1, así que no existe una única recta tangente en la esquina (x = 0).",
                "hints": ["Derivabilidad implica continuidad, pero el recíproco falla en esquinas filosas."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "No, porque tiene un pico donde la pendiente salta de −1 a +1",
                            "Sí, y su derivada en 0 es 0",
                            "Sí, toda función continua es derivable",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "c1-cadena-implicita",
        "title": "79. Regla de la cadena, derivación implícita e inversas",
        "level": 28,
        "order_index": 79,
        "summary": "Derivar funciones compuestas (afuera × adentro), curvas cerradas implícitas (x² + y² = r²), inversas y derivadas de orden superior.",
        "prerequisites": ["c1-derivadas-reglas", "a2-modelado-composicion"],
        "metadata": {"section": "Cálculo 1", "lab_tab": "derivatives", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Regla de la cadena: derivar afuera y multiplicar por lo de adentro",
                "prompt": "Para f(x) = (2x + 1)³, por regla de la cadena f'(x) = 3(2x + 1)² · 2 = 6(2x + 1)². ¿Cuánto vale f'(1)? Respondé solo con el número.",
                "answer": "54: 6 × (2·1 + 1)² = 6 × 9 = 54 (el error típico es olvidar el factor ×2 de adentro!).",
                "hints": ["Evaluá 6 × (3)²."],
                "payload": {
                    "lab_link": "math:derivatives",
                    "check": {"type": "numeric", "value": 54, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Regla de la cadena con exponencial e^(3x)",
                "prompt": "Calculá la derivada de f(x) = e^(3x) evaluada en x = 0 (recordá que (e^(kx))' = k·e^(kx) y e⁰ = 1). Respondé solo con el número.",
                "answer": "3: f'(x) = 3·e^(3x) → f'(0) = 3 × 1 = 3.",
                "hints": ["Derivada de afuera (e^(3x)) por derivada de adentro (3)."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Derivación implícita en un círculo x² + y² = 25",
                "prompt": "Al derivar x² + y² = 25 respecto de x obtenés 2x + 2y(dy/dx) = 0 → dy/dx = −x / y. ¿Cuál es la pendiente de la tangente al círculo en el punto (3, 4) en decimal? Respondé solo con el número.",
                "answer": "−0.75 (−3/4): en (3, 4) la tangente es perpendicular al radio (pendiente 4/3), así que vale −3/4 = −0.75!",
                "hints": ["Sustituí x = 3 e y = 4 en −x / y."],
                "payload": {
                    "lab_link": "math:derivatives",
                    "check": {"type": "numeric", "value": -0.75, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Segunda derivada f''(x) (tasa de cambio de la pendiente)",
                "prompt": "Para f(x) = x⁴ − 3x² + 2, la primera derivada es f'(x) = 4x³ − 6x y la segunda es f''(x) = 12x² − 6. ¿Cuánto vale f''(2)? Respondé solo con el número.",
                "answer": "42: f''(2) = 12(2²) − 6 = 48 − 6 = 42.",
                "hints": ["Evaluá 12(4) − 6."],
                "payload": {"check": {"type": "numeric", "value": 42, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Pendiente de una función inversa en un punto",
                "prompt": "La pendiente de la inversa f⁻¹ en y es el recíproco de la pendiente de f en el x correspondiente: (f⁻¹)'(b) = 1 / f'(a). Si f(2) = 5 y f'(2) = 4, ¿cuánto vale (f⁻¹)'(5) en decimal? Respondé solo con el número.",
                "answer": "0.25 (1/4): como f⁻¹ intercambia x e y, la pendiente Δy/Δx se invierte a Δx/Δy = 1/4 = 0.25.",
                "hints": ["Calculá el recíproco de f'(2) = 4."],
                "payload": {"check": {"type": "numeric", "value": 0.25, "tolerance": 0.01, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Derivada de arctan(x)",
                "prompt": "Una derivada famosa que aparece seguido al integrar es (arctan x)' = 1 / (1 + x²). ¿Cuánto vale la pendiente de y = arctan(x) en x = 1 en decimal? Respondé solo con el número.",
                "answer": "0.5: 1 / (1 + 1²) = 1 / 2 = 0.5.",
                "hints": ["Sustituí x = 1 en 1 / (1 + x²)."],
                "payload": {"check": {"type": "numeric", "value": 0.5, "tolerance": 0.01, "unit": ""}},
            },
        ],
    },
    # ==================== NIVEL 29: APLICACIONES DE LA DERIVADA ====================
    {
        "slug": "c1-aplicaciones-contexto",
        "title": "80. Cinemática, tasas relacionadas, linealización y L'Hôpital",
        "level": 29,
        "order_index": 80,
        "summary": "Posición-velocidad-aceleración, tasas ligadas por regla de la cadena, aproximar con la tangente y Regla de L'Hôpital (0/0, ∞/∞).",
        "prerequisites": ["c1-cadena-implicita"],
        "metadata": {"section": "Cálculo 1", "lab_tab": "derivatives", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Velocidad instantánea derivando la posición x(t)",
                "prompt": "Un móvil sobre una recta tiene posición x(t) = t³ − 6t² + 9t (en metros). Su velocidad es v(t) = x'(t) = 3t² − 12t + 9. ¿Cuál es su velocidad en t = 2 s (en m/s, con signo)? Respondé solo con el número.",
                "answer": "−3 m/s: v(2) = 3(4) − 12(2) + 9 = 12 − 24 + 9 = −3 m/s (el signo negativo indica que en ese instante retrocede).",
                "hints": ["Evaluá 3(2²) − 12(2) + 9."],
                "payload": {
                    "lab_link": "math:derivatives",
                    "check": {"type": "numeric", "value": -3, "tolerance": 0, "unit": "m/s"},
                },
            },
            {
                "item_type": "recall",
                "title": "Cuándo aumenta la rapidez vs. cuándo frena un objeto",
                "prompt": "En cierto instante un auto retrocede con velocidad v = −8 m/s y aceleración a = −2 m/s². ¿Su rapidez (magnitud de la velocidad) está aumentando o frenando?",
                "answer": "Está aumentando (acelerando hacia atrás): siempre que velocidad y aceleración tienen el MISMO signo, la rapidez crece.",
                "hints": ["Fijate si v y a empujan para el mismo lado (mismo signo) o en contra (signos opuestos)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Aumenta su rapidez (v y a tienen el mismo signo)",
                            "Está frenando porque a es negativa",
                            "Mantiene rapidez constante",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Tasas relacionadas: placa cuadrada que se expande por calor",
                "prompt": "Al calentar una placa cuadrada (A = L²), su lado crece a razón dL/dt = 2 cm/s. Derivando respecto del tiempo, dA/dt = 2L · (dL/dt). Cuando el lado mide L = 6 cm, ¿a cuántos cm²/s crece el área? Respondé solo con el número.",
                "answer": "24 cm²/s: dA/dt = 2(6)(2) = 24 cm²/s (no es constante: cuanto más grande es la placa, más rápido suma área!).",
                "hints": ["Reemplazá L = 6 y dL/dt = 2 en 2L · (dL/dt)."],
                "payload": {"check": {"type": "numeric", "value": 24, "tolerance": 0, "unit": "cm²/s"}},
            },
            {
                "item_type": "worked_example",
                "title": "Aproximación lineal (estimar √102 mentalmente)",
                "prompt": "Usá la recta tangente de f(x) = √x en a = 100 (f(100) = 10, f'(100) = 1/20 = 0.05): L(x) = 10 + 0.05(x − 100). ¿Qué aproximación da para √102? Respondé solo con el número.",
                "answer": "10.1: 10 + 0.05(2) = 10.1 (el valor real es 10.0995, un error menor al 0.005% sin calculadora!).",
                "hints": ["Evaluá 10 + 0.05 × (102 − 100)."],
                "payload": {"check": {"type": "numeric", "value": 10.1, "tolerance": 0.001, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Regla de L'Hôpital para destrabar 0/0",
                "prompt": "lim(x → 0) (e^(4x) − 1) / x da 0/0. Por L'Hôpital derivamos numerador y denominador por separado → lim(x → 0) 4e^(4x) / 1. ¿Cuánto vale el límite? Respondé solo con el número.",
                "answer": "4: al evaluar en x = 0 queda 4·e⁰ / 1 = 4.",
                "hints": ["Derivá arriba (4e^(4x)) y abajo (1), luego sustituí x = 0."],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Cuándo está PROHIBIDO usar la Regla de L'Hôpital",
                "prompt": "Querés calcular lim(x → 2) (x² + 1) / (x + 1). Al sustituir x = 2 da 5 / 3. ¿Podés aplicar L'Hôpital derivando arriba y abajo (2x / 1 = 4)?",
                "answer": "NO: L'Hôpital solo es válido cuando el límite da una forma indeterminada 0/0 o ∞/∞; en 5/3 el límite ya es directamente 5/3.",
                "hints": ["Comprobá si da 0/0 o ∞/∞ antes de derivar."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "No: L'Hôpital solo aplica a 0/0 o ∞/∞ (aquí el límite ya es 5/3)",
                            "Sí, siempre sirve para cualquier fracción",
                            "Sí, siempre que el denominador no sea cero",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "c1-analisis-optimizacion",
        "title": "81. Extremos, concavidad, Valor Medio y optimización",
        "level": 29,
        "order_index": 81,
        "summary": "Teorema del Valor Medio, puntos críticos, criterios de 1.ª y 2.ª derivada, inflexión y optimización de problemas reales.",
        "prerequisites": ["c1-derivadas-reglas", "al-parabolas-formula"],
        "metadata": {"section": "Cálculo 1", "lab_tab": "derivatives", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Optimización real: corral de máxima área con 40 m de cerca",
                "prompt": "Tenés 40 m de alambrado para cerrar un rectángulo (perímetro 2x + 2y = 40 → y = 20 − x). El área es A(x) = 20x − x². Derivando A'(x) = 20 − 2x = 0 hallás el lado óptimo x = 10 m. ¿Cuál es el área MÁXIMA en m²? Respondé solo con el número.",
                "answer": "100 m²: el rectángulo de mayor área para un perímetro fijo siempre es el cuadrado (10 m × 10 m = 100 m²).",
                "hints": ["Evaluá A(10) = 10 × (20 − 10)."],
                "payload": {
                    "lab_link": "math:derivatives",
                    "check": {"type": "numeric", "value": 100, "tolerance": 0, "unit": "m²"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Optimización contra una pared (3 lados de alambrado)",
                "prompt": "Ahora usás los mismos 40 m de cerca apoyados contra una pared recta (solo cercás 3 lados: x + 2y = 40 → x = 40 − 2y). Área A(y) = 40y − 2y² → A'(y) = 40 − 4y = 0 → y = 10 m, x = 20 m. ¿Cuál es el área máxima (m²)? Respondé solo con el número.",
                "answer": "200 m²: 20 m × 10 m = 200 m² (aprovechar la pared duplica el área encerrada!).",
                "hints": ["Multiplicá x = 20 m por y = 10 m."],
                "payload": {"check": {"type": "numeric", "value": 200, "tolerance": 0, "unit": "m²"}},
            },
            {
                "item_type": "worked_example",
                "title": "Hallar un punto de inflexión (donde f'' cambia de signo)",
                "prompt": "En f(x) = x³ − 6x² + 5, la segunda derivada es f''(x) = 6x − 12. ¿En qué valor de x ocurre el punto de inflexión (f''(x) = 0)? Respondé solo con el número.",
                "answer": "2: 6x − 12 = 0 → x = 2 (para x < 2 es cóncava hacia abajo y para x > 2 es cóncava hacia arriba).",
                "hints": ["Igualá 6x − 12 = 0 y despejá x."],
                "payload": {
                    "lab_link": "math:derivatives",
                    "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Criterio de la segunda derivada para clasificar un extremo",
                "prompt": "En un punto crítico sabés que f'(c) = 0 (tangente horizontal) y que f''(c) = −5 < 0 (cóncava hacia abajo). ¿Qué hay en x = c?",
                "answer": "Un máximo local: cóncava hacia abajo tiene forma de montaña (∩), así que la cima plana es un máximo.",
                "hints": ["Dibujá una curva triste (∩, f'' < 0) con techo plano en c."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Un máximo local (forma de cima ∩)",
                            "Un mínimo local (forma de valle ∪)",
                            "Una asíntota vertical",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Teorema del Valor Medio (multa de velocidad promedio)",
                "prompt": "Un auto cruza dos peajes separados 200 km en exactamente 2 horas (velocidad promedio 100 km/h). Según el Teorema del Valor Medio (TVM), ¿qué quedó demostrado matemáticamente?",
                "answer": "Que en al menos un instante del viaje la velocidad instantánea fue exactamente 100 km/h (si el límite era 80 km/h, seguro excedió el límite!).",
                "hints": ["El TVM garantiza que f'(c) iguala a la tasa promedio (f(b) − f(a))/(b − a) en algún c intermedio."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "En algún instante su velocímetro marcó exactamente 100 km/h",
                            "Viajó a 100 km/h constantes durante las 2 horas",
                            "Nunca superó los 100 km/h",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Criterio de la primera derivada (cambio de signo de f')",
                "prompt": "Si f'(x) cambia de NEGATIVA (bajando) a POSITIVA (subiendo) al cruzar x = 3, ¿qué tipo de punto hay en x = 3?",
                "answer": "Un mínimo local: primero decrece y después crece, formando un valle en x = 3.",
                "hints": ["Seguí el dibujo con el dedo: baja y luego sube."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Un mínimo local", "Un máximo local", "Un punto de inflexión"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 30: INTEGRALES, EDOs Y VOLÚMENES ====================
    {
        "slug": "c1-integrales-tfc",
        "title": "82. Sumas de Riemann, Teorema Fundamental del Cálculo y sustitución u",
        "level": 30,
        "order_index": 82,
        "summary": "Aproximar áreas con rectángulos, integral definida como acumulación neta, TFC (partes 1 y 2) y sustitución u.",
        "prerequisites": ["c1-cadena-implicita", "pc-series-sigma"],
        "metadata": {"section": "Cálculo 1", "lab_tab": "integrals", "est_minutes": 24},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Teorema Fundamental del Cálculo (Parte 2): evaluar una integral definida",
                "prompt": "Evaluá ∫(de 1 a 3) de 3x² dx usando la antiderivada F(x) = x³: F(3) − F(1). Respondé solo con el número.",
                "answer": "26: 3³ − 1³ = 27 − 1 = 26 (es el área exacta bajo la parábola y = 3x² entre x = 1 y x = 3).",
                "hints": ["Calculá F(3) − F(1) = 3³ − 1³."],
                "payload": {
                    "lab_link": "math:integrals",
                    "check": {"type": "numeric", "value": 26, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Teorema Fundamental del Cálculo (Parte 1): derivar una integral",
                "prompt": "Definimos g(x) = ∫(de 2 a x) de (t³ + 5) dt. Por el TFC Parte 1, g'(x) = x³ + 5. ¿Cuánto vale g'(2)? Respondé solo con el número.",
                "answer": "13: derivar e integrar son operaciones inversas → g'(2) = 2³ + 5 = 13 (ni hace falta calcular la integral!).",
                "hints": ["Evaluá directamente la función interior en x = 2: 2³ + 5."],
                "payload": {"check": {"type": "numeric", "value": 13, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Integral por sustitución u (inversa de la regla de la cadena)",
                "prompt": "En ∫(de 0 a 2) 2x · (x² + 1) dx, hacés u = x² + 1 (du = 2x dx). Los límites cambian de x = 0..2 a u = 1..5 → ∫(de 1 a 5) u du = [u²/2] de 1 a 5. ¿Cuánto da? Respondé solo con el número.",
                "answer": "12: 5²/2 − 1²/2 = 25/2 − 1/2 = 24/2 = 12.",
                "hints": ["Calculá (25 − 1) ÷ 2."],
                "payload": {
                    "lab_link": "math:integrals",
                    "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Integral definida como área neta con signo",
                "prompt": "¿Cuánto vale ∫(de 0 a 2π) sen(x) dx en un ciclo completo de seno (pista: mirá la simetría entre la mitad positiva y la negativa)? Respondé solo con el número.",
                "answer": "0: el área sobre el eje X (+2) y el área debajo del eje X (−2) se cancelan exactamente.",
                "hints": ["La integral definida resta las áreas que quedan por debajo del eje X."],
                "payload": {"check": {"type": "numeric", "value": 0, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Suma de Riemann izquierda con 2 rectángulos",
                "prompt": "Aproximá ∫(de 0 a 4) x dx con 2 rectángulos de ancho Δx = 2 usando las alturas del borde izquierdo (f(0) = 0 y f(2) = 2): Δx · (f(0) + f(2)). Respondé solo con el número.",
                "answer": "4: 2 × (0 + 2) = 4 (subestima el área exacta de 8 porque y = x es creciente; con más rectángulos se acerca a 8).",
                "hints": ["Calculá 2 × (0 + 2)."],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Por qué siempre se agrega '+ C' en integrales indefinidas",
                "prompt": "¿Por qué escribimos ∫ 2x dx = x² + C en lugar de solamente x²?",
                "answer": "Porque x², x² + 5 y x² − 100 tienen TODAS exactamente la misma derivada 2x (la derivada borra cualquier constante aditiva).",
                "hints": ["¿Cuánto vale la derivada de una constante cualquiera?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Porque cualquier constante sumada desaparece al derivar (hay infinitas antiderivadas)",
                            "Porque C siempre vale 1",
                            "Solo hace falta cuando la integral es definida",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "c1-ecuaciones-diferenciales",
        "title": "83. Ecuaciones diferenciales y separación de variables",
        "level": 30,
        "order_index": 83,
        "summary": "Campos de pendientes, resolver EDOs separando variables (g(y)dy = f(x)dx), condición inicial y modelos exponenciales/térmicos.",
        "prerequisites": ["c1-integrales-tfc", "a2-logaritmos"],
        "metadata": {"section": "Cálculo 1", "lab_tab": "integrals", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Leer un campo de pendientes (slope field)",
                "prompt": "Para la ecuación diferencial dy/dx = x − y, ¿cuál es la pendiente de la pequeña rayita dibujada en el punto (5, 2) del campo de pendientes? Respondé solo con el número.",
                "answer": "3: simplemente sustituís las coordenadas (5, 2) en la fórmula → 5 − 2 = 3.",
                "hints": ["Reemplazá x = 5 e y = 2 en x − y."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Resolver dy/dx = 2x con condición inicial y(0) = 5",
                "prompt": "Resolvé dy/dx = 2x con la condición inicial y(0) = 5. ¿Cuánto vale y(3)? Respondé solo con el número.",
                "answer": "14: integrando queda y = x² + C; la condición y(0) = 5 fija C = 5, así que y(x) = x² + 5 → y(3) = 3² + 5 = 14.",
                "hints": ["Integrá 2x: y = x² + C.", "Usá y(0) = 5 para hallar C y después calculá 3² + C."],
                "payload": {
                    "lab_link": "math:integrals",
                    "check": {"type": "numeric", "value": 14, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Separación de variables: dy/dx = x / y",
                "prompt": "Separando variables en dy/dx = x / y queda y dy = x dx → al integrar, y² − x² = K. Si y(0) = 3 (entonces K = 9), ¿cuánto vale la solución positiva y(4)? Respondé solo con el número.",
                "answer": "5: y² − 4² = 9 → y² = 25 → y = 5 (la condición inicial y(0) = 3 elige la rama positiva).",
                "hints": ["Despejá y de y² − 16 = 9."],
                "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "De dónde nace la ley exponencial dy/dt = k · y",
                "prompt": "Una población o capital crece a una tasa proporcional a su tamaño actual: dy/dt = k · y. Al separar variables (1/y)dy = k dt e integrar ambos lados, ¿qué familia de soluciones aparece?",
                "answer": "y(t) = y₀ · e^(kt): el crecimiento exponencial es la consecuencia directa de que la tasa de cambio sea proporcional a la cantidad presente.",
                "hints": ["La integral de (1/y) dy es ln|y|; al despejar y aparece la exponencial e^(kt)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "y(t) = y₀ · e^(kt)",
                            "y(t) = y₀ + k · t",
                            "y(t) = k · t²",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Temperatura de equilibrio en la Ley de enfriamiento de Newton",
                "prompt": "Una taza de café se enfría según dT/dt = −0.1 · (T − 20) (en °C). ¿A qué temperatura T se detiene el enfriamiento (dT/dt = 0)? Respondé solo con el número en °C.",
                "answer": "20°C (la temperatura ambiente): cuando T = 20, el paréntesis se anula y la tasa de cambio vale 0.",
                "hints": ["Igualá −0.1(T − 20) = 0."],
                "payload": {"check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "°C"}},
            },
            {
                "item_type": "recall",
                "title": "Verificar si una función resuelve una ecuación diferencial",
                "prompt": "Sin integrar nada, ¿cómo verificás rápidamente si y = 3e^(2x) es solución de dy/dx = 2y?",
                "answer": "Derivando y = 3e^(2x) → dy/dx = 6e^(2x), que efectivamente es igual a 2 · (3e^(2x)) = 2y.",
                "hints": ["Derivá la candidata y comprobá si ambos lados de la ecuación coinciden."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Derivando y comprobando que dy/dx = 6e^(2x) = 2y",
                            "Integrando 2y respecto de x",
                            "Evaluando solo en x = 0",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "c1-aplicaciones-integrales",
        "title": "84. Valor promedio, áreas entre curvas y volúmenes 3D",
        "level": 30,
        "order_index": 84,
        "summary": "Valor promedio de funciones continuas, desplazamiento vs. distancia total, área entre curvas y volúmenes por discos/arandelas.",
        "prerequisites": ["c1-integrales-tfc", "g-geometria-solida"],
        "metadata": {"section": "Cálculo 1", "lab_tab": "integrals", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Valor promedio de una función continua en [a, b]",
                "prompt": "El valor promedio de f(x) en [a, b] es [1 / (b − a)] · ∫(de a a b) f(x) dx. Para f(x) = 3x² en [0, 2], la integral vale [x³] de 0 a 2 = 8. ¿Cuál es su valor promedio? Respondé solo con el número.",
                "answer": "4: dividimos la integral (8) por el ancho del intervalo (2 − 0 = 2) → 8 / 2 = 4.",
                "hints": ["Dividí el área acumulada (8) por el ancho del intervalo (2)."],
                "payload": {
                    "lab_link": "math:integrals",
                    "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Desplazamiento neto vs. distancia total recorrida",
                "prompt": "Un robot avanza a +4 m/s durante 3 s y luego retrocede a −2 m/s durante 3 s. ¿Cuál es la DISTANCIA TOTAL recorrida ∫|v(t)|dt (en metros)? Ojo: no es lo mismo que su desplazamiento neto ∫v(t)dt. Respondé solo con el número.",
                "answer": "18 m: avanza 4 × 3 = 12 m y retrocede 2 × 3 = 6 m; la distancia total suma los valores absolutos sin cancelar retrocesos → |+12| + |−6| = 18 m (el desplazamiento neto es solo 12 − 6 = 6 m).",
                "hints": ["Calculá cuánto recorre en cada tramo: velocidad × tiempo.", "Sumá las distancias de ida y de vuelta ambas en positivo: 12 + 6."],
                "payload": {"check": {"type": "numeric", "value": 18, "tolerance": 0, "unit": "m"}},
            },
            {
                "item_type": "worked_example",
                "title": "Área encerrada entre dos curvas (arriba − abajo)",
                "prompt": "La recta y = 6x queda por encima de la parábola y = 3x² entre x = 0 y x = 2. Calculá el área encerrada ∫(de 0 a 2) (6x − 3x²) dx = [3x² − x³] de 0 a 2. Respondé solo con el número.",
                "answer": "4: (3(4) − 8) − 0 = 12 − 8 = 4 unidades cuadradas.",
                "hints": ["Evaluá 3x² − x³ en x = 2 y restale lo de x = 0."],
                "payload": {
                    "lab_link": "math:integrals",
                    "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Volumen de revolución por método de discos",
                "prompt": "Al girar y = √x alrededor del eje X entre x = 0 y x = 4, cada rebanada es un disco de área π(√x)² = πx → V = π · ∫(de 0 a 4) x dx = k · π. ¿Cuánto vale el número k? Respondé solo con el número.",
                "answer": "8 (volumen = 8π ≈ 25.13): [x²/2] de 0 a 4 = 16 / 2 = 8.",
                "hints": ["Calculá ∫(de 0 a 4) x dx = [x² / 2] de 0 a 4."],
                "payload": {
                    "lab_link": "math:integrals",
                    "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Volumen por secciones transversales cuadradas",
                "prompt": "Un sólido tiene base en [0, 3] y cada corte vertical es un cuadrado de lado s(x) = x (área de cada rebanada A(x) = x²). Calculá su volumen V = ∫(de 0 a 3) x² dx = [x³/3] de 0 a 3. Respondé solo con el número.",
                "answer": "9: 3³ / 3 − 0 = 27 / 3 = 9 (es exactamente una pirámide de base 3×3 y altura 3!).",
                "hints": ["Evaluá x³ / 3 en x = 3."],
                "payload": {
                    "lab_link": "math:integrals",
                    "check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Trampa clásica del método de arandelas (sólido con hueco)",
                "prompt": "Al girar la región entre un radio exterior R(x) y un radio interior hueco r(x) alrededor del eje X, ¿cuál es el área de cada arandela (anillo)?",
                "answer": "π(R² − r²): restás el área del círculo interno al área del círculo externo (¡NUNCA π(R − r)²!).",
                "hints": ["Área de un disco grande menos área del agujero central."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "π · (R(x)² − r(x)²)",
                            "π · (R(x) − r(x))²",
                            "2π · (R(x) − r(x))",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
]

CALCULUS1_LESSONS: dict[str, dict] = {
    "c1-limites-avanzados": {
        "hook": "Con cuatro herramientas (racionalizar, límites al infinito, Sándwich y Valor Intermedio) podés dominar cualquier límite y demostrar que una ecuación tiene solución sin siquiera resolverla.",
        "concept": {
            "points": [
                "**Límites al infinito (`x → ±∞`)**: compará los términos de mayor potencia (`(10x³)/(2x³) → 5`). Recordá la jerarquía de crecimiento: **`ln(x) ≪ xⁿ ≪ eˣ`**.",
                "**Trucos para `0/0`**: con raíces cuadradas, **racionalizá** multiplicando por el conjugado; en trigonometría (siempre en radianes!), usá el límite base **`lim_{u→0} sen(u)/u = 1`**.",
                "**Dos teoremas clave**: el **Teorema del Sándwich** atrapa una función difícil entre dos fáciles con igual límite; el **Teorema del Valor Intermedio (TVI)** garantiza que una función continua que cambia de signo en `[a, b]` cruza por `0` al menos una vez.",
            ],
            "real_world": [
                {
                    "title": "Búsqueda de raíces por bisección (computación)",
                    "detail": "Cuando un algoritmo detecta `f(a) < 0` y `f(b) > 0` en una función continua, el TVI le garantiza que la raíz está adentro y parte el intervalo a la mitad hasta encontrarla.",
                },
                {
                    "title": "Aproximación de ángulos pequeños (`sen θ ≈ θ`)",
                    "detail": "Que `lim_{θ→0} sen(θ)/θ = 1` es exactamente la razón por la que en Física el péndulo simple se aproxima con `sen(θ) ≈ θ` (en radianes).",
                },
                {
                    "title": "Complejidad de algoritmos (`O(log n)` vs `O(n²)` vs `O(2ⁿ)`)",
                    "detail": "Los límites al infinito muestran por qué un algoritmo exponencial colapsa mucho antes que uno polinómico o logarítmico.",
                },
            ],
            "key_rule": "x→∞: dominan términos líderes (ln ≪ xⁿ ≪ eˣ) | sen(kx)/x → k | TVI: continua + cambio de signo ⇒ existe raíz.",
            "pitfall": "Aplicar el TVI a una función con un salto o asíntota (ej. `1/x` pasa de `−1` a `+1` entre `−1` y `1`, pero nunca cruza `0` porque no es continua en `0`!).",
        },
        "example": {
            "title": "Racionalizar (√x − 2)/(x − 4) cuando x → 4 y hallar lim sen(5x)/x",
            "steps": [
                "Multiplicamos arriba y abajo por el conjugado `(√x + 2)`: arriba da `(√x)² − 2² = x − 4`.",
                "Cancelamos `(x − 4)` arriba y abajo: queda `1 / (√x + 2)`, que en `x = 4` vale `1 / 4 = 0.25`.",
                "Para `lim_{x→0} sen(5x) / x`, reescribimos `5 · [sen(5x)/(5x)]` → como `sen(u)/u → 1`, el límite es `5`.",
            ],
            "lab_link": "math:limits_intro",
            "lab_cta": "Practicar límites en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto vale `lim(x → ∞) (6x² + 9x) / (3x² − 1)`?",
            "options": [
                {"text": "`2` (`6x² / 3x²`)", "ok": True, "feedback": "Exacto: para x gigante mandan los términos líderes 6x²/3x² = 2."},
                {"text": "`0`", "ok": False, "feedback": "Solo da 0 si el grado del denominador es estrictamente mayor."},
                {"text": "`−9`", "ok": False, "feedback": "Los términos de grado menor no influyen en x → ∞."},
            ],
        },
        "checks": [
            {
                "question": "Si `f` es continua en `[1, 5]`, `f(1) = 4` y `f(5) = 12`, ¿qué garantiza el TVI?",
                "options": [
                    {"text": "Existe algún `c` entre `1` y `5` donde `f(c) = 10`", "ok": True, "feedback": "Exacto: 10 está entre 4 y 12, y f es continua."},
                    {"text": "Existe algún `c` entre `1` y `5` donde `f(c) = 0`", "ok": False, "feedback": "0 no está entre 4 y 12, así que el TVI no garantiza ningún cero."},
                    {"text": "`f(3) = 8` exacto", "ok": False, "feedback": "La curva puede no ser recta; solo garantiza que pasa por 8 en algún punto."},
                ],
            },
            {
                "question": "¿Cuál es el límite `lim(x → 0) sen(3x) / x`?",
                "options": [
                    {"text": "`3`", "ok": True, "feedback": "Exacto: 3 · [sen(3x)/(3x)] → 3 × 1 = 3."},
                    {"text": "`1`", "ok": False, "feedback": "Da 1 cuando el coeficiente dentro del seno coincide con el denominador (sen(x)/x)."},
                    {"text": "`0`", "ok": False, "feedback": "Es forma 0/0, no 0."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con un ejemplo cotidiano por qué el Teorema del Valor Intermedio requiere que la función sea continua.",
    },
    "c1-derivadas-reglas": {
        "hook": "La derivada es el zoom infinito: si ampliás cualquier curva suave millones de veces en un punto, se vuelve una línea recta, y su pendiente es exactamente `f'(x)`.",
        "concept": {
            "points": [
                "Definición: **`f'(x) = lim_{h→0} [f(x + h) − f(x)] / h`** mide la **tasa instantánea de cambio** (pendiente de la recta tangente). Si `f` es derivable en `a`, es continua allí (pero una esquina como `|x|` es continua y NO derivable).",
                "**Reglas rápidas**: potencia **`(xⁿ)' = n·xⁿ⁻¹`** (sirve también para negativos y raíces!), constante → `0`, **`(eˣ)' = eˣ`**, **`(ln x)' = 1/x`**, **`(sen x)' = cos x`**, **`(cos x)' = −sen x`**.",
                "**Producto y cociente**: **`(f·g)' = f'g + fg'`** y **`(f/g)' = (f'g − fg') / g²`** (¡nunca derives arriba y abajo o factor por factor sueltos!).",
            ],
            "real_world": [
                {
                    "title": "Velocímetro instantáneo de un auto",
                    "detail": "La derivada de la posición respecto del tiempo (`dx/dt`) te dice a qué velocidad exacta vas en este segundo, no tu promedio del viaje.",
                },
                {
                    "title": "Costo marginal en economía",
                    "detail": "`C'(x)` indica cuánto cuesta fabricar UNA unidad adicional cuando ya producís `x` unidades.",
                },
                {
                    "title": "Entrenamiento de inteligencia artificial (gradient descent)",
                    "detail": "Las redes neuronales ajustan sus pesos calculando derivadas del error para bajar siempre hacia el mínimo.",
                },
            ],
            "key_rule": "(xⁿ)' = n·xⁿ⁻¹ | (fg)' = f'g + fg' | (f/g)' = (f'g − fg')/g² | (eˣ)' = eˣ | (ln x)' = 1/x.",
            "pitfall": "Hacer `(f · g)' = f' · g'` o `(f / g)' = f' / g'`: para producto y cociente hay que usar siempre sus reglas completas.",
        },
        "example": {
            "title": "Derivar f(x) = 4x³ − 5x + 7 y g(x) = x² · sen(x)",
            "steps": [
                "En `f(x) = 4x³ − 5x + 7`, derivamos término a término: `f'(x) = 12x² − 5 + 0 = 12x² − 5`.",
                "Evaluando en `x = 2`: la tangente tiene pendiente `f'(2) = 12(4) − 5 = 43`.",
                "En `g(x) = x² · sen(x)`, usamos regla del producto: `g'(x) = (2x)·sen(x) + x²·cos(x)`.",
            ],
            "lab_link": "math:derivatives",
            "lab_cta": "Practicar derivadas en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es la derivada de `f(x) = 5x⁴ − 3x² + 9`?",
            "options": [
                {"text": "`20x³ − 6x`", "ok": True, "feedback": "Exacto: 5·4x³ − 3·2x + 0 = 20x³ − 6x."},
                {"text": "`20x³ − 6x + 9`", "ok": False, "feedback": "La derivada de una constante sola (+9) siempre es 0."},
                {"text": "`5x³ − 3x`", "ok": False, "feedback": "Te faltó multiplicar por el exponente que baja (4 y 2)."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál es la derivada de `y = 1 / x` (escrito como `x⁻¹`)?",
                "options": [
                    {"text": "`−1 / x²` (`−1 · x⁻²`)", "ok": True, "feedback": "Exacto: baja −1 y el exponente pasa de −1 a −2."},
                    {"text": "`1 / 1 = 1`", "ok": False, "feedback": "No se deriva numerador y denominador por separado."},
                    {"text": "`ln(x)`", "ok": False, "feedback": "Al revés: la derivada de ln(x) es 1/x (ln(x) es la antiderivada de 1/x!)."},
                ],
            },
            {
                "question": "Usando regla del producto, ¿cuál es la derivada de `x · eˣ`?",
                "options": [
                    {"text": "`1 · eˣ + x · eˣ = (1 + x)eˣ`", "ok": True, "feedback": "Exacto: f'g + fg' con f = x y g = eˣ."},
                    {"text": "`1 · eˣ = eˣ`", "ok": False, "feedback": "Derivaste cada factor por separado sin aplicar f'g + fg'."},
                    {"text": "`x · eˣ`", "ok": False, "feedback": "Solo derivaste eˣ y olvidaste el término f'g."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué significa geométricamente `f'(a)` y por qué la derivada de cualquier constante es cero.",
    },
    "c1-cadena-implicita": {
        "hook": "Casi todas las funciones reales vienen 'anidadas' como una muñeca rusa (`sen(3x)`, `e^(−t²)`, `(x² + 1)⁵`): la Regla de la Cadena te permite derivar cualquier capa.",
        "concept": {
            "points": [
                "**Regla de la cadena**: si tenés `f(g(x))`, derivás la capa **exterior** dejando intacto lo de adentro, y **multiplicás por la derivada de lo de adentro**: **`[f(g(x))]' = f'(g(x)) · g'(x)`**.",
                "**Derivación implícita**: cuando `y` no está despejada (como `x² + y² = 25`), derivás ambos lados respecto de `x` recordando que cada vez que derivás una `y` sale un factor **`dy/dx`** por la regla de la cadena, y luego despejás `dy/dx`.",
                "**Inversas y orden superior**: `(f⁻¹)'(b) = 1 / f'(a)`, `(arctan x)' = 1/(1 + x²)`, `(arcsen x)' = 1/√(1 − x²)`. Derivar otra vez da **`f''(x)`** (aceleración / curvatura).",
            ],
            "real_world": [
                {
                    "title": "Backpropagation en redes neuronales",
                    "detail": "El algoritmo que entrena toda la IA moderna es literalmente aplicar la Regla de la Cadena capa por capa desde la salida hasta los pesos de entrada.",
                },
                {
                    "title": "Engranajes y cadenas de transmisión",
                    "detail": "Si el pedal gira `du/dt` y la rueda gira `dy/du` por cada vuelta de pedal, la velocidad final de la rueda es `dy/dt = (dy/du) · (du/dt)`.",
                },
                {
                    "title": "Tangentes a trayectorias cerradas (órbitas y lentes)",
                    "detail": "Para saber el ángulo de reflexión en una elipse o círculo, derivación implícita te da la pendiente exacta sin despejar raíces `±√`.",
                },
            ],
            "key_rule": "Cadena: [f(g(x))]' = f'(g(x)) · g'(x) | Implícita: cada término con y multiplica por dy/dx.",
            "pitfall": "Olvidar multiplicar por la derivada interna `g'(x)` (por ej. derivar `sen(4x)` como `cos(4x)` en vez de `4·cos(4x)`).",
        },
        "example": {
            "title": "Derivar sen(3x²) por cadena y x² + y² = 25 de forma implícita",
            "steps": [
                "En `sen(3x²)`: afuera es `sen(u)` → `cos(u)`; adentro es `u = 3x²` → `6x`. Producto: `6x · cos(3x²)`.",
                "En `x² + y² = 25`: derivamos respecto de `x` → `2x + 2y · (dy/dx) = 0`.",
                "Despejamos `dy/dx = −2x / (2y) = −x / y`. En `(3, 4)` la pendiente es `−3/4 = −0.75`.",
            ],
            "lab_link": "math:derivatives",
            "lab_cta": "Practicar regla de la cadena en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es la derivada de `f(x) = cos(5x)`?",
            "options": [
                {"text": "`−5 · sen(5x)`", "ok": True, "feedback": "Exacto: derivada afuera (−sen(5x)) multiplicada por la derivada de adentro (5)."},
                {"text": "`−sen(5x)`", "ok": False, "feedback": "Te faltó multiplicar por la derivada interna de 5x (que es 5)."},
                {"text": "`5 · sen(5x)`", "ok": False, "feedback": "Recordá el signo negativo en la derivada del coseno."},
            ],
        },
        "checks": [
            {
                "question": "Al derivar implícitamente `y³ = x²` respecto de `x`, ¿qué queda en el lado izquierdo?",
                "options": [
                    {"text": "`3y² · (dy/dx)`", "ok": True, "feedback": "Exacto: como y depende de x, la regla de la cadena multiplica por dy/dx."},
                    {"text": "`3y²`", "ok": False, "feedback": "Sin dy/dx estarías derivando respecto de y en vez de respecto de x."},
                    {"text": "`3x²`", "ok": False, "feedback": "y no es igual a x; se conserva y² y se multiplica por dy/dx."},
                ],
            },
            {
                "question": "¿Cuál es la derivada de `ln(x² + 1)`?",
                "options": [
                    {"text": "`2x / (x² + 1)`", "ok": True, "feedback": "Exacto: [ln(u)]' = u' / u = 2x / (x² + 1)."},
                    {"text": "`1 / (x² + 1)`", "ok": False, "feedback": "Te faltó multiplicar por la derivada interna de (x² + 1), que es 2x."},
                    {"text": "`1 / (2x)`", "ok": False, "feedback": "Debajo queda el argumento completo (x² + 1), no su derivada."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en tus palabras la receta 'afuera × adentro' de la Regla de la Cadena con un ejemplo propio.",
    },
    "c1-aplicaciones-contexto": {
        "hook": "Aquí las derivadas salen del pizarrón: calculan qué tan rápido se llena un tanque, estiman `√102` mentalmente y destraban límites `0/0` en un segundo con L'Hôpital.",
        "concept": {
            "points": [
                "**Movimiento rectilíneo**: **`v(t) = x'(t)`** y **`a(t) = v'(t) = x''(t)`**. La rapidez aumenta cuando `v` y `a` tienen el **mismo signo**, y frena cuando tienen signos opuestos.",
                "**Tasas relacionadas**: escribís una ecuación geométrica que ligue las variables (ej. `A = L²` o `x² + y² = L²`), derivás ambos lados respecto del **tiempo `t`** (cadena!), y recién al final sustituís los números del instante.",
                "**Linealización**: cerca de `a`, **`f(x) ≈ f(a) + f'(a)(x − a)`**. Y **Regla de L'Hôpital**: si `lim f(x)/g(x)` da **`0/0` o `∞/∞`**, entonces **`lim f(x)/g(x) = lim f'(x)/g'(x)`**.",
            ],
            "real_world": [
                {
                    "title": "Llenado de tanques cónicos y globos",
                    "detail": "Aunque cargues agua a caudal constante `dV/dt`, en un cono el nivel `dh/dt` sube rapidísimo al principio y cada vez más lento a medida que se ensancha.",
                },
                {
                    "title": "Sensores y aproximaciones rápidas en microcontroladores",
                    "detail": "Cuando un chip barato no quiere calcular `√x` o `sen(x)`, usa la linealización tangente alrededor de un punto cercano conocido.",
                },
                {
                    "title": "Análisis de aceleración en vehículos y cohetes",
                    "detail": "Los acelerómetros miden `a(t) = x''(t)`; saber cuándo `v` y `a` cambian de signo indica frenado, detención momentánea o retroceso.",
                },
            ],
            "key_rule": "v = x', a = v' | Tasas: derivá respecto de t ANTES de sustituir | Tangente: f(a) + f'(a)(x − a) | L'Hôpital: solo 0/0 o ∞/∞.",
            "pitfall": "Sustituir los números variables (como `L = 6`) ANTES de derivar en tasas relacionadas: si ponés `A = 6² = 36` antes de derivar, la derivada te da `0`!",
        },
        "example": {
            "title": "Estimar √102 por linealización y resolver lim (e^(4x) − 1)/x con L'Hôpital",
            "steps": [
                "En `f(x) = √x` cerca de `a = 100`: `f(100) = 10`, `f'(100) = 1/(2√100) = 0.05`.",
                "Tangente: `L(102) = 10 + 0.05(102 − 100) = 10.1` (exactísimo frente a `10.0995`).",
                "En `lim_{x→0} (e^(4x) − 1) / x`: verificamos que da `0/0` → aplicamos L'Hôpital: `lim_{x→0} 4e^(4x) / 1 = 4`.",
            ],
            "lab_link": "math:derivatives",
            "lab_cta": "Practicar derivadas y tangentes en el Laboratorio",
        },
        "check": {
            "question": "Si la posición es `x(t) = 5t² − 20t`, ¿en qué instante `t` se detiene momentáneamente la partícula (`v(t) = 0`)?",
            "options": [
                {"text": "`t = 2 s` (`v(t) = 10t − 20 = 0`)", "ok": True, "feedback": "Exacto: en t = 2 s la velocidad pasa de negativa a positiva."},
                {"text": "`t = 4 s`", "ok": False, "feedback": "En t = 4 s regresa a la posición x = 0, pero su velocidad ahí es +20 m/s."},
                {"text": "`t = 0 s`", "ok": False, "feedback": "En t = 0 s arranca moviéndose a −20 m/s."},
            ],
        },
        "checks": [
            {
                "question": "En un problema de tasas relacionadas donde el radio `r` crece con el tiempo, ¿cuándo debés reemplazar `r = 5`?",
                "options": [
                    {"text": "DESPUÉS de derivar la ecuación respecto de `t`", "ok": True, "feedback": "Exacto: si sustituís r = 5 antes de derivar, tratás r como constante y perdés dr/dt."},
                    {"text": "ANTES de derivar para simplificar las cuentas", "ok": False, "feedback": "Sustituir antes de derivar hace que la derivada dé 0."},
                    {"text": "Es indistinto", "ok": False, "feedback": "Solo se sustituyen antes las constantes que NO cambian con el tiempo (como el largo rígido de una escalera)."},
                ],
            },
            {
                "question": "Usando L'Hôpital en `lim(x → 0) (1 − cos x) / x²` (da `0/0`), derivás dos veces: ¿cuánto vale el límite?",
                "options": [
                    {"text": "`0.5` (`sen x / (2x)` → `cos x / 2` → `1/2`)", "ok": True, "feedback": "Exacto: tras la 1.ª vez sigue siendo 0/0, así que podés aplicar L'Hôpital una 2.ª vez → 1/2."},
                    {"text": "`0`", "ok": False, "feedback": "Después de derivar una vez queda sen(x)/(2x), que sigue siendo 0/0 y tiende a 1/2."},
                    {"text": "`1`", "ok": False, "feedback": "Te faltó el factor 2 al derivar x² → 2x."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué condición tenés que verificar siempre antes de aplicar la Regla de L'Hôpital.",
    },
    "c1-analisis-optimizacion": {
        "hook": "¿Qué forma debe tener una lata de gaseosa para gastar la mínima cantidad de aluminio posible? El cálculo diferencial resuelve cualquier problema de 'máximo' o 'mínimo' igualando `f'(x) = 0`.",
        "concept": {
            "points": [
                "**1.ª derivada (`f'`)**: `f' > 0` = sube, `f' < 0` = baja. Los **puntos críticos** (`f'(c) = 0` o no existe) son los candidatos a máximos/mínimos locales (para extremos absolutos en `[a, b]`, chequeá también los bordes `a` y `b`).",
                "**2.ª derivada (`f''`)**: mide la **concavidad**: `f'' > 0` = cóncava hacia arriba (`∪`, en `f' = 0` hay **mínimo**); `f'' < 0` = cóncava hacia abajo (`∩`, en `f' = 0` hay **máximo**); donde `f''` cambia de signo hay un **punto de inflexión**.",
                "**Teorema del Valor Medio (TVM)**: en `[a, b]` derivable, siempre hay un `c` donde la pendiente instantánea iguala a la pendiente promedio (`f'(c) = [f(b) − f(a)] / (b − a)`).",
            ],
            "real_world": [
                {
                    "title": "Diseño de envases y empaques (optimización)",
                    "detail": "Fábricas de latas y cajas minimizan el área superficial (material) para un volumen fijo derivando la función costo e igualando a cero.",
                },
                {
                    "title": "Precio óptimo que maximiza ganancias",
                    "detail": "Si subís mucho el precio vendés menos unidades; `Ganancia'(p) = 0` encuentra el punto exacto donde el beneficio total es máximo.",
                },
                {
                    "title": "Punto de inflexión en epidemias y ventas",
                    "detail": "El punto de inflexión (`f'' = 0`) marca el momento exacto en que los contagios o ventas siguen creciendo pero empiezan a DESACELERARSE.",
                },
            ],
            "key_rule": "Extremos: f'(c) = 0 | Mínimo: f'' > 0 (∪) | Máximo: f'' < 0 (∩) | Inflexión: f'' cambia de signo.",
            "pitfall": "Olvidar chequear los extremos del intervalo `[a, b]` cuando buscás el máximo o mínimo ABSOLUTO (a veces el valor más alto está en un borde y no donde `f' = 0`).",
        },
        "example": {
            "title": "Maximizar el área de un corral con 40 m de cerca (3 lados contra una pared)",
            "steps": [
                "Restricción: `x + 2y = 40` → despejamos `x = 40 − 2y` para dejar el área en una sola variable.",
                "Objetivo: `A(y) = y(40 − 2y) = 40y − 2y²` → derivamos e igualamos a cero: `A'(y) = 40 − 4y = 0` → `y = 10 m`.",
                "Comprobamos con 2.ª derivada: `A''(y) = −4 < 0` (máximo garantizado!). Entonces `x = 20 m` y área máxima = `200 m²`.",
            ],
            "lab_link": "math:derivatives",
            "lab_cta": "Practicar puntos críticos y derivadas en el Laboratorio",
        },
        "check": {
            "question": "Dada `f(x) = x² − 8x + 3`, ¿en qué valor de `x` alcanza su mínimo (donde `f'(x) = 0`)?",
            "options": [
                {"text": "`x = 4` (`2x − 8 = 0`, y `f'' = 2 > 0`)", "ok": True, "feedback": "Exacto: coincide también con la fórmula del vértice −b/(2a) = 8/2 = 4!"},
                {"text": "`x = −4`", "ok": False, "feedback": "De 2x − 8 = 0 sale x = +4."},
                {"text": "`x = 8`", "ok": False, "feedback": "Te faltó dividir por 2 al despejar 2x = 8."},
            ],
        },
        "checks": [
            {
                "question": "Si una función tiene `f'(x) > 0` y `f''(x) < 0` en un tramo, ¿cómo se comporta?",
                "options": [
                    {"text": "Está creciendo, pero cada vez más lento (cóncava hacia abajo)", "ok": True, "feedback": "Exacto: f' > 0 significa que sube, y f'' < 0 que su pendiente va disminuyendo."},
                    {"text": "Está bajando cada vez más rápido", "ok": False, "feedback": "Bajaría si f'(x) < 0."},
                    {"text": "Está creciendo cada vez más rápido", "ok": False, "feedback": "Crecería acelerando si también f''(x) > 0."},
                ],
            },
            {
                "question": "En un problema de optimización con dos variables (ej. largo `x` y ancho `y`), ¿cuál es el paso clave antes de derivar?",
                "options": [
                    {"text": "Usar la ecuación de restricción para escribir el objetivo en función de UNA sola variable", "ok": True, "feedback": "Exacto: así podés derivar directamente e igualar a cero."},
                    {"text": "Igualar `x = y` desde el principio siempre", "ok": False, "feedback": "Contra una pared dio x = 20, y = 10 (no eran iguales!): hay que dejar que el cálculo lo decida."},
                    {"text": "Integrar la restricción", "ok": False, "feedback": "La optimización busca máximos/mínimos derivando, no integrando."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá la diferencia práctica entre lo que te informa el signo de `f'(x)` y el signo de `f''(x)` sobre una gráfica.",
    },
    "c1-integrales-tfc": {
        "hook": "Si derivar desarma una curva en velocidades instantáneas, integrar vuelve a sumar infinitas rebanadas diminutas para recuperar el área y la acumulación total.",
        "concept": {
            "points": [
                "La **integral definida `∫_a^b f(x)dx`** es el límite de las **Sumas de Riemann** (infinitos rectángulos de ancho `dx → 0`) y calcula el **área neta con signo** (arriba del eje X suma `+`, debajo resta `−`).",
                "**Teorema Fundamental del Cálculo (TFC)** — el puente entre derivadas e integrales: **Parte 1**: `d/dx ∫_a^x f(t)dt = f(x)` (derivar deshace integrar). **Parte 2**: **`∫_a^b f(x)dx = F(b) − F(a)`** donde `F' = f`.",
                "**Antiderivadas y sustitución `u`**: regla inversa de la potencia **`∫ xⁿ dx = xⁿ⁺¹/(n + 1) + C`** (`n ≠ −1`; para `1/x` da `ln|x| + C`). Cuando ves una función compuesta junto a su derivada interna, hacés **`u = g(x), du = g'(x)dx`**.",
            ],
            "real_world": [
                {
                    "title": "Distancia recorrida desde el velocímetro (`∫ v(t) dt`)",
                    "detail": "El odómetro de tu auto integra la velocidad en el tiempo: acumula pequeñas distancias `v · dt` para obtener los kilómetros totales.",
                },
                {
                    "title": "Consumo eléctrico en tu factura (kWh)",
                    "detail": "La energía que pagás es la integral de la potencia instantánea (kW) a lo largo de todas las horas del mes.",
                },
                {
                    "title": "Trabajo de un resorte y carga eléctrica",
                    "detail": "Cuando la fuerza varía con la distancia (`F(x) = kx`), el trabajo total es el área bajo la curva `∫ F(x) dx = ½kx²`.",
                },
            ],
            "key_rule": "TFC: ∫_a^b f(x)dx = F(b) − F(a) | ∫ xⁿ dx = xⁿ⁺¹/(n+1) + C | Sustitución u deshace la regla de la cadena.",
            "pitfall": "En una integral definida con sustitución `u`, olvidar cambiar también los límites `a, b` a valores de `u` (o volver a escribir en términos de `x` antes de evaluar!).",
        },
        "example": {
            "title": "Evaluar ∫(1 a 3) 3x² dx y ∫(0 a 2) 2x(x² + 1) dx",
            "steps": [
                "Para `∫(1 a 3) 3x² dx`: una antiderivada es `F(x) = x³` (comprobación: `(x³)' = 3x²`) → `F(3) − F(1) = 27 − 1 = 26`.",
                "Para `∫(0 a 2) 2x(x² + 1) dx`: elegimos `u = x² + 1`, así `du = 2x dx` aparece exacto!",
                "Cambiamos los límites: si `x = 0 → u = 1`; si `x = 2 → u = 5`. Evaluamos `∫(1 a 5) u du = [u²/2]_1^5 = 12.5 − 0.5 = 12`.",
            ],
            "lab_link": "math:integrals",
            "lab_cta": "Practicar integrales definidas en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es la antiderivada general `∫ 4x³ dx`?",
            "options": [
                {"text": "`x⁴ + C`", "ok": True, "feedback": "Exacto: comprobá derivando (x⁴ + C)' = 4x³!"},
                {"text": "`12x² + C`", "ok": False, "feedback": "Derivaste en vez de integrar: al integrar el exponente SUBE de 3 a 4."},
                {"text": "`4x⁴ + C`", "ok": False, "feedback": "Te faltó dividir por el nuevo exponente (4 ÷ 4 = 1)."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuánto vale `∫(de 0 a 4) 2x dx`?",
                "options": [
                    {"text": "`16` (`[x²]` de 0 a 4 = `16 − 0`)", "ok": True, "feedback": "Exacto: también es el área de un triángulo de base 4 y altura 8 → (4×8)/2 = 16!"},
                    {"text": "`8`", "ok": False, "feedback": "8 es la altura final f(4), no el área bajo la recta."},
                    {"text": "`32`", "ok": False, "feedback": "Te faltó dividir por 2 al antiderivar 2x → x²."},
                ],
            },
            {
                "question": "Si `h(x) = ∫(de 0 a x) cos(t²) dt`, ¿cuánto vale `h'(x)` por el TFC Parte 1?",
                "options": [
                    {"text": "`cos(x²)`", "ok": True, "feedback": "Exacto: ni siquiera existe antiderivada elemental para cos(t²), pero su derivada es directamente cos(x²)!"},
                    {"text": "`−2x · sen(x²)`", "ok": False, "feedback": "Derivaste dos veces (eso sería h''(x)); derivar la integral simplemente quita el símbolo ∫."},
                    {"text": "`sen(x²)`", "ok": False, "feedback": "No hay que integrar la función, solo evaluar la de adentro en x."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en una frase qué dice el Teorema Fundamental del Cálculo y por qué es tan potente para calcular áreas.",
    },
    "c1-ecuaciones-diferenciales": {
        "hook": "Las leyes de la naturaleza casi nunca dicen dónde están las cosas: dicen cómo CAMBIAN (`dy/dt = ...`). Las ecuaciones diferenciales reconstruyen toda la historia a partir de la regla de cambio.",
        "concept": {
            "points": [
                "Una **ecuación diferencial (EDO)** relaciona una función con su derivada (`dy/dx = ...`). Un **campo de pendientes** dibuja pequeñas flechas con pendiente `dy/dx` en cada `(x, y)` para ver las curvas solución sin resolver nada.",
                "**Separación de variables**: juntás todas las `y` con `dy` de un lado y las `x` con `dx` del otro (`g(y)dy = f(x)dx`), integrás ambos lados (agregando `+ C` de un lado) y usás la **condición inicial** `(x₀, y₀)` para fijar `C`.",
                "**Modelo estrella**: **`dy/dt = k·y`** se resuelve separando variables y produce **`y(t) = y₀ · e^(kt)`** (crecimiento si `k > 0`, decaimiento si `k < 0`).",
            ],
            "real_world": [
                {
                    "title": "Ley de enfriamiento de Newton (`dT/dt = −k(T − T_amb)`)",
                    "detail": "Un café se enfría más rápido cuanto más grande es la diferencia con el ambiente, tendiendo asintóticamente a `T_amb`.",
                },
                {
                    "title": "Circuitos RC (carga y descarga de capacitores)",
                    "detail": "El voltaje de un capacitor descargándose por una resistencia cumple `dV/dt = −V / (RC)` → decaimiento exponencial `V₀·e^(−t/RC)`.",
                },
                {
                    "title": "Epidemiología y crecimiento logístico",
                    "detail": "Los modelos poblacionales con recursos limitados usan `dP/dt = kP(1 − P/M)`: crece rápido al inicio y frena al acercarse a la capacidad `M`.",
                },
            ],
            "key_rule": "Separar variables: g(y)dy = f(x)dx → integrar ambos lados → usar (x₀, y₀) para hallar C.",
            "pitfall": "Intentar separar variables sumando/restando (en `dy/dx = x + y` NO se puede separar multiplicando!) o poner `+ C` recién al final después de aplicar `e^(...)` (en vez de transformarlo en factor multiplicativo `A·e^(kt)`).",
        },
        "example": {
            "title": "Resolver dy/dx = 2xy con condición inicial y(0) = 3",
            "steps": [
                "Separamos variables dividiendo por `y` y multiplicando por `dx`: `(1/y) dy = 2x dx`.",
                "Integramos ambos lados: `ln|y| = x² + C` → despejamos aplicando exponencial: `y = A · e^(x²)`.",
                "Aplicamos `y(0) = 3`: `3 = A · e⁰ = A` → solución particular exacta: `y(x) = 3 · e^(x²)`.",
            ],
            "lab_link": "math:integrals",
            "lab_cta": "Practicar integrales y EDOs en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál de estas ecuaciones diferenciales SÍ es separable (`g(y)dy = f(x)dx`)?",
            "options": [
                {"text": "`dy/dx = x² · y`", "ok": True, "feedback": "Exacto: dividiendo por y queda (1/y)dy = x² dx."},
                {"text": "`dy/dx = x + y`", "ok": False, "feedback": "Como x e y se suman, no se pueden separar como producto/cociente junto a dx y dy."},
                {"text": "`dy/dx = sen(x + y)`", "ok": False, "feedback": "x e y están atrapados sumándose dentro del seno."},
            ],
        },
        "checks": [
            {
                "question": "Si `dy/dx = −2x` y la curva pasa por `(1, 6)`, ¿cuál es la solución particular `y(x)`?",
                "options": [
                    {"text": "`y = −x² + 7`", "ok": True, "feedback": "Exacto: ∫(−2x)dx = −x² + C → 6 = −1 + C → C = 7."},
                    {"text": "`y = −x² + 6`", "ok": False, "feedback": "Si C = 6, entonces y(1) = −1 + 6 = 5, no 6."},
                    {"text": "`y = −2x² + 8`", "ok": False, "feedback": "La integral de −2x es −x², no −2x²."},
                ],
            },
            {
                "question": "En un campo de pendientes de `dy/dx = y`, ¿qué tienen en común todos los puntos de la recta horizontal `y = 2`?",
                "options": [
                    {"text": "Todas las rayitas tienen la misma pendiente `2` (no depende de `x`)", "ok": True, "feedback": "Exacto: como x no aparece en la fórmula, cada fila horizontal tiene pendientes idénticas."},
                    {"text": "Todas son horizontales (pendiente `0`)", "ok": False, "feedback": "Son horizontales solo en y = 0."},
                    {"text": "Cambian según el valor de `x`", "ok": False, "feedback": "Eso pasa cuando x aparece en la expresión de dy/dx."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en tus palabras los 3 pasos para resolver una ecuación diferencial separable con condición inicial.",
    },
    "c1-aplicaciones-integrales": {
        "hook": "Con la misma idea de 'rebanar y sumar' (`∫`), las integrales calculan promedios continuos, áreas entre curvas irregulares y volúmenes de piezas torneadas en 3D.",
        "concept": {
            "points": [
                "**Valor promedio**: **`f_prom = [1 / (b − a)] · ∫_a^b f(x)dx`** (es la altura del rectángulo que tiene exactamente la misma área que la curva). **Movimiento**: desplazamiento = `∫ v(t)dt`; distancia total = `∫ |v(t)|dt`.",
                "**Área entre dos curvas**: **`Área = ∫_a^b [f_arriba(x) − f_abajo(x)] dx`** (los límites `a, b` salen de igualar ambas curvas para ver dónde se cruzan).",
                "**Volúmenes 3D integrando rebanadas `∫ A(x)dx`**: al girar alrededor de un eje, **discos** → **`V = π ∫ R(x)² dx`**; con hueco interior, **arandelas** → **`V = π ∫ [R(x)² − r(x)²] dx`**.",
            ],
            "real_world": [
                {
                    "title": "Diseño CAD y piezas torneadas (CNC)",
                    "detail": "El volumen (y peso!) de una botella, copa o tobera de cohete se calcula exactamente girando su perfil 2D con el método de discos.",
                },
                {
                    "title": "Temperatura promedio del día y potencia media",
                    "detail": "El promedio de infinitas mediciones continuas a lo largo de 24 horas es `(1/24) ∫_0^24 T(t) dt`.",
                },
                {
                    "title": "Índice de Gini y excedentes en economía",
                    "detail": "La desigualdad de ingresos y el ahorro neto entre curvas de oferta y demanda se miden directamente como áreas entre dos curvas.",
                },
            ],
            "key_rule": "Promedio: (1/(b−a))∫f | Entre curvas: ∫(arriba − abajo) | Discos: π∫R² | Arandelas: π∫(R² − r²).",
            "pitfall": "Escribir `π(R − r)²` en el método de arandelas en lugar de `π(R² − r²)`: siempre elevás cada radio al cuadrado POR SEPARADO antes de restar.",
        },
        "example": {
            "title": "Área entre y = 6x y y = 3x², y volumen al girar y = √x en [0, 4]",
            "steps": [
                "Igualamos `6x = 3x²` → `3x(2 − x) = 0` → se cruzan en `x = 0` y `x = 2` (en el medio `6x` va arriba).",
                "Área = `∫(0 a 2) (6x − 3x²) dx = [3x² − x³]_0^2 = 12 − 8 = 4`.",
                "Volumen de `y = √x` girada en `[0, 4]`: radio `R(x) = √x` → `V = π ∫(0 a 4) (√x)² dx = π [x²/2]_0^4 = 8π`.",
            ],
            "lab_link": "math:integrals",
            "lab_cta": "Practicar áreas, promedios y volúmenes en el Laboratorio",
        },
        "check": {
            "question": "Si la integral `∫(de 2 a 7) f(x) dx` vale `30`, ¿cuál es el valor promedio de `f` en `[2, 7]`?",
            "options": [
                {"text": "`6` (`30 / (7 − 2)`)", "ok": True, "feedback": "Exacto: el ancho del intervalo es 7 − 2 = 5, y 30 ÷ 5 = 6."},
                {"text": "`30`", "ok": False, "feedback": "30 es la acumulación total; falta dividir por el ancho del intervalo (5)."},
                {"text": "`15`", "ok": False, "feedback": "Dividiste por 2 en vez de por (7 − 2 = 5)."},
            ],
        },
        "checks": [
            {
                "question": "Un objeto parte de `x = 0`, camina `10 m` hacia la derecha y vuelve `10 m` al origen. ¿Cuánto valen su desplazamiento (`∫ v dt`) y su distancia total (`∫ |v| dt`)?",
                "options": [
                    {"text": "Desplazamiento `0 m`, distancia total `20 m`", "ok": True, "feedback": "Exacto: la integral de v cancela ida y vuelta; la de |v| suma ambos trayectos."},
                    {"text": "Ambos valen `20 m`", "ok": False, "feedback": "Al volver al punto de partida el desplazamiento neto es 0 m."},
                    {"text": "Ambos valen `0 m`", "ok": False, "feedback": "La distancia total caminada fue 10 + 10 = 20 m."},
                ],
            },
            {
                "question": "Al girar un rectángulo de altura constante `R` y largo `h` alrededor del eje X con el método de discos (`π ∫_0^h R² dx`), ¿qué fórmula clásica de geometría redescubrís?",
                "options": [
                    {"text": "El volumen del cilindro (`V = πR²h`)", "ok": True, "feedback": "Exacto: π · R² · [x]_0^h = πR²h! Las integrales generalizan toda la geometría 3D."},
                    {"text": "El volumen del cono (`(1/3)πR²h`)", "ok": False, "feedback": "El cono sale al girar una recta inclinada y = (R/h)x, no una constante R."},
                    {"text": "El área del círculo (`πR²`)", "ok": False, "feedback": "Integrar desde 0 hasta h multiplica el área πR² por el largo h."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá cómo una sola idea (`∫ A(x) dx`, sumar rebanadas) unifica áreas entre curvas y volúmenes 3D por discos/arandelas.",
    },
}
