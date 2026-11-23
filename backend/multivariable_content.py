"""Multivariable Calculus curriculum (8 units, #92-#99) adapted from Khan Academy.

Covers all 5 units of Khan Academy Multivariable Calculus building on Cálculo 2 (#85-#91):
  - Multivariable functions, contour maps, 3D cross product & planes
  - Partial derivatives, gradient, directional derivatives, tangent planes & multivariable chain rule
  - 3D optimization (Hessian, saddle points) & Lagrange multipliers
  - Vector fields: divergence, curl & conservative fields
  - Double & triple integrals, Fubini & polar/cylindrical/spherical Jacobians
  - Line integrals (work), Fundamental Theorem for line integrals & surface flux
  - Green's Theorem (2D circulation-curl & flux-divergence)
  - Stokes' Theorem, Divergence Theorem (Gauss) & grand unification of Calculus
"""

from __future__ import annotations

MULTIVARIABLE_NODES: list[dict] = [
    # ==================== NIVEL 34: ESPACIO 3D, PARCIALES, GRADIENTE Y OPTIMIZACIÓN ====================
    {
        "slug": "mv-espacio-superficies",
        "title": "92. Funciones 3D, curvas de nivel y producto cruz",
        "level": 34,
        "order_index": 92,
        "summary": "Superficies z = f(x, y), mapas topográficos (curvas de nivel), producto cruz 3D (u × v) y ecuaciones de planos.",
        "prerequisites": ["pc-vectores", "c2-parametricas-vectores"],
        "metadata": {"section": "Cálculo multivariable", "lab_tab": "multivar_diff", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Evaluar una superficie z = f(x, y) en un punto",
                "prompt": "La altura de un terreno sigue f(x, y) = x² + 3xy − y (en metros). ¿Cuál es la altura z en las coordenadas (2, 3)? Respondé solo con el número.",
                "answer": "19 m: f(2, 3) = 2² + 3(2)(3) − 3 = 4 + 18 − 3 = 19 m.",
                "hints": ["Sustituí x = 2 e y = 3 en x² + 3xy − y."],
                "payload": {"check": {"type": "numeric", "value": 19, "tolerance": 0, "unit": "m"}},
            },
            {
                "item_type": "recall",
                "title": "Leer pendientes en un mapa de curvas de nivel",
                "prompt": "Mirás un mapa topográfico (curvas de nivel dibujadas cada 10 m de altura). En la zona A las líneas están MUY juntas y en la zona B están muy separadas. ¿Dónde es más empinada la montaña?",
                "answer": "En la zona A: líneas muy juntas significan que subís 10 m de altura avanzando muy pocos metros horizontales (pendiente alta).",
                "hints": ["Mismo salto vertical (10 m) dividido por una distancia horizontal muy chica."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "En la zona A (líneas juntas = pendiente empinada)",
                            "En la zona B (líneas separadas = pendiente empinada)",
                            "Tienen la misma pendiente",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Magnitud del producto cruz 3D (área del paralelogramo)",
                "prompt": "El producto cruz u × v entre u = ⟨2, 0, 0⟩ y v = ⟨0, 3, 0⟩ apunta perpendicular a ambos, en el eje +z. ¿Cuál es su magnitud |u × v| (igual al área del rectángulo que forman)? Respondé solo con el número.",
                "answer": "6: |u × v| = |u|·|v|·sen(90°) = 2 × 3 × 1 = 6 (y apunta hacia +z por regla de la mano derecha).",
                "hints": ["Multiplicá las magnitudes 2 × 3 (forman 90°)."],
                "payload": {"check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Producto cruz de dos vectores paralelos",
                "prompt": "¿Cuál es la magnitud del producto cruz |u × (2u)| de un vector consigo mismo duplicado (ángulo θ = 0°)? Respondé solo con el número.",
                "answer": "0: como sen(0°) = 0, el producto cruz de vectores paralelos es siempre el vector nulo ⟨0, 0, 0⟩ (área encerrada = 0).",
                "hints": ["Usá |u|·|v|·sen(0°)."],
                "payload": {"check": {"type": "numeric", "value": 0, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Anticonmutatividad del producto cruz (u × v vs. v × u)",
                "prompt": "A diferencia del producto punto (donde u · v = v · u), ¿qué pasa si invertís el orden en el producto cruz y calculás v × u?",
                "answer": "Da el vector opuesto: v × u = −(u × v) (misma magnitud, pero apunta exactamente para el lado contrario por la regla de la mano derecha).",
                "hints": ["Al girar los dedos de v hacia u tu pulgar apunta para el lado opuesto."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Invierte el sentido: v × u = −(u × v)",
                            "Da exactamente el mismo vector",
                            "Siempre da cero",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ecuación de un plano con vector normal n",
                "prompt": "Un plano con vector normal n = ⟨2, −1, 3⟩ pasa por el punto (1, 0, 2), cumpliendo 2x − y + 3z = d. Sustituyendo (1, 0, 2), ¿cuánto vale la constante d? Respondé solo con el número.",
                "answer": "8: 2(1) − 0 + 3(2) = 2 + 6 = 8 → ecuación del plano: 2x − y + 3z = 8.",
                "hints": ["Evaluá 2(1) − 1(0) + 3(2)."],
                "payload": {"check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    {
        "slug": "mv-parciales-gradiente",
        "title": "93. Derivadas parciales, gradiente (∇f) y derivada direccional",
        "level": 34,
        "order_index": 93,
        "summary": "Derivar congelando las otras variables (∂f/∂x, ∂f/∂y), el gradiente como dirección de ascenso máximo, D_u f = ∇f · u y cadena multivariable.",
        "prerequisites": ["mv-espacio-superficies", "c1-cadena-implicita"],
        "metadata": {"section": "Cálculo multivariable", "lab_tab": "multivar_diff", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Calcular una derivada parcial ∂f/∂x",
                "prompt": "Dada f(x, y) = x³y² + 5y, calculá ∂f/∂x (tratando a y como constante → 3x²y²) evaluada en el punto (2, 1). Respondé solo con el número.",
                "answer": "12: la derivada de 5y respecto de x es 0; queda 3(2²)(1²) = 12.",
                "hints": ["Evaluá 3x²y² en x = 2, y = 1."],
                "payload": {
                    "lab_link": "math:multivar_diff",
                    "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Calcular la otra derivada parcial ∂f/∂y",
                "prompt": "Para la misma función f(x, y) = x³y² + 5y, ahora congelá x como constante: ∂f/∂y = 2x³y + 5. ¿Cuánto vale en (2, 1)? Respondé solo con el número.",
                "answer": "21: 2(2³)(1) + 5 = 16 + 5 = 21 (así el vector gradiente en (2, 1) es ∇f(2, 1) = ⟨12, 21⟩!).",
                "hints": ["Evaluá 2(8)(1) + 5."],
                "payload": {
                    "lab_link": "math:multivar_diff",
                    "check": {"type": "numeric", "value": 21, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Pendiente máxima = magnitud del gradiente |∇f|",
                "prompt": "En un punto de una ladera el gradiente es ∇f = ⟨3, 4⟩. ¿Cuál es la tasa MÁXIMA de subida (la magnitud |∇f|)? Respondé solo con el número.",
                "answer": "5: el gradiente apunta hacia la subida más empinada y su longitud √(3² + 4²) = 5 es esa pendiente máxima.",
                "hints": ["Calculá √(3² + 4²)."],
                "payload": {
                    "lab_link": "math:multivar_diff",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Derivada direccional: D_u f = ∇f · u",
                "prompt": "En cierto punto ∇f = ⟨5, 10⟩ y caminás en la dirección del vector UNITARIO u = ⟨0.6, 0.8⟩. Calculá la pendiente en tu dirección D_u f = ∇f · u. Respondé solo con el número.",
                "answer": "11: (5)(0.6) + (10)(0.8) = 3 + 8 = 11 (si u no fuera unitario, primero tendrías que dividirlo por |u|!).",
                "hints": ["Hacé el producto punto: 5(0.6) + 10(0.8)."],
                "payload": {
                    "lab_link": "math:multivar_diff",
                    "check": {"type": "numeric", "value": 11, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Regla de la cadena multivariable (temperatura que siente un dron)",
                "prompt": "La temperatura en una sala es T(x, y) = 2x + 3y (°C) y un dron vuela con dx/dt = 4 m/s y dy/dt = −1 m/s. Usando dT/dt = T_x(dx/dt) + T_y(dy/dt), ¿cuántos °C/s cambia la temperatura que mide el dron? Respondé solo con el número.",
                "answer": "5 °C/s: 2(4) + 3(−1) = 8 − 3 = 5 °C/s (es simplemente ∇T · v!).",
                "hints": ["Calculá 2(4) + 3(−1)."],
                "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "°C/s"}},
            },
            {
                "item_type": "recall",
                "title": "Ángulo entre el gradiente ∇f y las curvas de nivel",
                "prompt": "En un mapa de curvas de nivel de f(x, y), ¿qué ángulo forma SIEMPRE el vector gradiente ∇f con la curva de nivel que pasa por ese punto?",
                "answer": "90° (perpendicular): a lo largo de una curva de nivel la altura no cambia (D_u f = ∇f · u = 0), lo que exige que ∇f sea ortogonal a la curva.",
                "hints": ["Caminar sobre una curva de nivel tiene pendiente 0, así que ∇f · u = 0."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "90° (siempre perpendicular a la curva de nivel)",
                            "0° (siempre tangente a la curva de nivel)",
                            "45°",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "mv-optimizacion-lagrange",
        "title": "94. Optimización 3D (Hessiano, puntos silla) y Lagrange",
        "level": 34,
        "order_index": 94,
        "summary": "Puntos críticos ∇f = 0, clasificar máximos/mínimos/sillas con el Hessiano H = f_xx·f_yy − f_xy² y multiplicadores de Lagrange (∇f = λ∇g).",
        "prerequisites": ["mv-parciales-gradiente", "c1-analisis-optimizacion"],
        "metadata": {"section": "Cálculo multivariable", "lab_tab": "multivar_diff", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Hallar un punto crítico igualando ∇f = ⟨0, 0⟩",
                "prompt": "Para f(x, y) = x² + y² − 6x + 4y + 1, sus parciales son f_x = 2x − 6 y f_y = 2y + 4. ¿Cuál es la coordenada x del punto crítico (donde f_x = 0 y f_y = 0)? Respondé solo con el número.",
                "answer": "3 (el punto crítico completo es (3, −2), que es el fondo de un paraboloide / mínimo global).",
                "hints": ["Igualá 2x − 6 = 0."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Calcular el determinante Hessiano de un punto silla",
                "prompt": "Para la silla de montar f(x, y) = x² − y², las segundas parciales son f_xx = 2, f_yy = −2 y f_xy = 0. Calculá H = f_xx · f_yy − (f_xy)². Respondé solo con el número.",
                "answer": "−4: como H < 0, en (0, 0) hay un PUNTO SILLA (sube a lo largo de X pero baja a lo largo de Y, como una papa frita Pringle!).",
                "hints": ["Calculá (2)(−2) − 0²."],
                "payload": {
                    "lab_link": "math:multivar_diff",
                    "check": {"type": "numeric", "value": -4, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Clasificar con el Hessiano H = f_xx·f_yy − (f_xy)²",
                "prompt": "En un punto crítico (∇f = 0) encontrás H > 0 y además f_xx > 0. ¿Qué tipo de extremo es?",
                "answer": "Un mínimo local: H > 0 asegura que las curvaturas en ambas direcciones tienen el mismo signo, y f_xx > 0 indica que abre hacia arriba (cuenco ∪).",
                "hints": ["H > 0 = mismo signo de concavidad (extremo); f_xx > 0 = cóncava hacia arriba."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Mínimo local (cuenco hacia arriba)",
                            "Máximo local (domo hacia abajo)",
                            "Punto silla",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Multiplicadores de Lagrange: optimizar f(x, y) = xy con x + y = 10",
                "prompt": "Querés maximizar f(x, y) = x·y sujeto a x + y = 10. Planteá la condición de Lagrange ∇f = λ∇g, hallá el punto y respondé: ¿cuál es el valor MÁXIMO de f(x, y)? Respondé solo con el número.",
                "answer": "25: ∇f = ⟨y, x⟩ y ∇g = ⟨1, 1⟩ dan y = λ y x = λ, o sea x = y; con x + y = 10 queda x = y = 5 y f(5, 5) = 25 (la curva de nivel xy = 25 roza tangencialmente a la recta x + y = 10).",
                "hints": ["∇f = ⟨y, x⟩ y ∇g = ⟨1, 1⟩: igualá componente a componente.", "Sale x = y; reemplazá en x + y = 10 y evaluá f en ese punto."],
                "payload": {"check": {"type": "numeric", "value": 25, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Significado geométrico de ∇f = λ∇g (Lagrange)",
                "prompt": "¿Por qué en un óptimo con restricción g(x, y) = c se cumple obligatoriamente ∇f = λ∇g?",
                "answer": "Porque en el punto óptimo las curvas de nivel de f y de g son TANGENTES, así que sus gradientes (perpendiculares a ambas) deben ser paralelos!",
                "hints": ["Si los gradientes no fueran paralelos, podrías moverte por g = c siguiendo una componente de ∇f y subir todavía más."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Las curvas de nivel de f y g son tangentes (sus gradientes son paralelos)",
                            "Ambos gradientes deben ser perpendiculares entre sí",
                            "Ambos gradientes valen cero",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Teorema de Clairaut (derivadas parciales mixtas)",
                "prompt": "Para cualquier función suave f(x, y), si calculás primero ∂/∂x y luego ∂/∂y (f_xy), ¿cómo se compara con derivar en el orden inverso (f_yx)?",
                "answer": "Son exactamente iguales (f_xy = f_yx): el orden de las derivadas parciales mixtas no cambia el resultado.",
                "hints": ["Es la razón por la que la matriz Hessiana siempre es simétrica."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Siempre son iguales (f_xy = f_yx)", "Tienen signos opuestos", "Depende de cuál sea mayor"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 35: DIVERGENCIA, ROTACIONAL E INTEGRALES MÚLTIPLES ====================
    {
        "slug": "mv-divergencia-rotacional",
        "title": "95. Divergencia (∇ · F), rotacional (∇ × F) y campos conservativos",
        "level": 35,
        "order_index": 95,
        "summary": "Medir fuentes/sumideros con divergencia, remolinos con rotacional 2D y reconocer campos conservativos (F = ∇f).",
        "prerequisites": ["mv-parciales-gradiente"],
        "metadata": {"section": "Cálculo multivariable", "lab_tab": "multivar_diff", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Calcular la divergencia de un campo expansivo",
                "prompt": "Para el campo F(x, y) = ⟨3x, 2y⟩, la divergencia es div(F) = ∂P/∂x + ∂Q/∂y. ¿Cuánto vale div(F)? Respondé solo con el número.",
                "answer": "5: ∂(3x)/∂x + ∂(2y)/∂y = 3 + 2 = 5 > 0 (en todo punto el campo actúa como una fuente que expande el fluido).",
                "hints": ["Sumá ∂(3x)/∂x más ∂(2y)/∂y."],
                "payload": {
                    "lab_link": "math:multivar_diff",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Divergencia variable evaluada en un punto",
                "prompt": "Dado F(x, y) = ⟨x², x·y⟩, calculá la divergencia div(F) = ∂P/∂x + ∂Q/∂y y evaluala en el punto (4, 2). Respondé solo con el número.",
                "answer": "12: ∂(x²)/∂x + ∂(xy)/∂y = 2x + x = 3x, y en (4, 2) da 3(4) = 12.",
                "hints": ["Derivá x² respecto de x, y x·y respecto de y.", "Queda 2x + x = 3x; evaluá en x = 4."],
                "payload": {
                    "lab_link": "math:multivar_diff",
                    "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Rotacional 2D de un remolino antihorario",
                "prompt": "Para el campo giratorio F(x, y) = ⟨−y, x⟩, el rotacional escalar 2D es rot(F) = ∂Q/∂x − ∂P/∂y. ¿Cuánto vale? Respondé solo con el número.",
                "answer": "2: ∂(x)/∂x − ∂(−y)/∂y = 1 − (−1) = +2 (positivo = una ruedita de paletas gira en sentido antihorario!).",
                "hints": ["Calculá 1 − (−1)."],
                "payload": {
                    "lab_link": "math:multivar_diff",
                    "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Test rápido de campo conservativo en 2D",
                "prompt": "Querés saber si un campo suave F = ⟨P, Q⟩ en todo el plano es conservativo (proviene de un potencial F = ∇f). ¿Qué condición debe cumplir su rotacional 2D?",
                "answer": "∂Q/∂x − ∂P/∂y = 0 en todas partes (rotacional nulo / irrotacional), consecuencia directa de f_yx = f_xy.",
                "hints": ["Los campos gradiente nunca tienen remolinos (rot(∇f) = 0)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "rot(F) = ∂Q/∂x − ∂P/∂y = 0 en todas partes",
                            "div(F) = ∂P/∂x + ∂Q/∂y = 0 en todas partes",
                            "P = Q siempre",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Significado físico de div(v) = 0 en fluidos",
                "prompt": "En hidrodinámica, el agua que circula por una cañería sin fuentes ni fugas cumple div(v) = 0. ¿Qué significa físicamente?",
                "answer": "Que el fluido es incompresible: en cada punto entra exactamente la misma cantidad de agua que la que sale.",
                "hints": ["Divergencia positiva = fuente/expansión; negativa = sumidero/compresión; cero = equilibrio exacto."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Es incompresible (lo que entra en cada región iguala lo que sale)",
                            "El agua está completamente quieta (v = 0)",
                            "El agua gira formando remolinos",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "¿Escalar o vector? Salidas de gradiente, divergencia y rotacional",
                "prompt": "¿Cuál de estos tres operadores recibe un campo VECTORIAL y devuelve un simple NÚMERO ESCALAR en cada punto?",
                "answer": "La divergencia (∇ · F): igual que el producto punto, produce un escalar (tasa de expansión en cada punto).",
                "hints": ["Mirando la notación ∇ · F, el punto recuerda al producto escalar."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "La divergencia (∇ · F)",
                            "El gradiente (∇f)",
                            "El rotacional 3D (∇ × F)",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "mv-integrales-dobles-triples",
        "title": "96. Integrales dobles, triples y cambio a polares (r dr dθ)",
        "level": 35,
        "order_index": 96,
        "summary": "Integración iterada (Fubini), volúmenes bajo superficies, Jacobiano polar r dr dθ e integrales triples en 3D.",
        "prerequisites": ["mv-espacio-superficies", "c2-polares-areas"],
        "metadata": {"section": "Cálculo multivariable", "lab_tab": "multivar_int", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Integral doble iterada sobre un rectángulo",
                "prompt": "Evaluá de adentro hacia afuera ∫(x=0 a 2) [ ∫(y=0 a 3) 2x dy ] dx. Adentro (y de 0 a 3) da 6x; afuera ∫(0 a 2) 6x dx = [3x²] de 0 a 2. ¿Cuál es el resultado? Respondé solo con el número.",
                "answer": "12: 3(2²) − 0 = 12 unidades cúbicas de volumen bajo la rampa z = 2x.",
                "hints": ["Evaluá 3x² en x = 2."],
                "payload": {
                    "lab_link": "math:multivar_int",
                    "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Integral doble de una constante (volumen de caja)",
                "prompt": "Calculá ∬_R 4 dA sobre el rectángulo R = [0, 2] × [0, 3] (base 2 × 3 y altura constante 4). Respondé solo con el número.",
                "answer": "24: 4 × Área(R) = 4 × 6 = 24.",
                "hints": ["Multiplicá la altura (4) por el área de la base (2 × 3)."],
                "payload": {
                    "lab_link": "math:multivar_int",
                    "check": {"type": "numeric", "value": 24, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Integral triple: masa de un bloque con densidad variable",
                "prompt": "Un bloque [0, 2] × [0, 1] × [0, 3] tiene densidad ρ(x, y, z) = 2z kg/m³. Su masa es ∫(x=0..2) ∫(y=0..1) ∫(z=0..3) 2z dz dy dx. ¿Cuántos kg pesa? Respondé solo con el número.",
                "answer": "18 kg: la integral de adentro da [z²]_0^3 = 9; como lo que queda no depende de y ni de x, se multiplica por el ancho en y (1) y el largo en x (2): 9 × 1 × 2 = 18 kg.",
                "hints": ["Empezá por la integral de adentro: ∫ 2z dz = z².", "De 0 a 3 da 9; después multiplicá por el ancho en y (1) y el largo en x (2)."],
                "payload": {"check": {"type": "numeric", "value": 18, "tolerance": 0, "unit": "kg"}},
            },
            {
                "item_type": "recall",
                "title": "El factor extra r en coordenadas polares (dA = r dr dθ)",
                "prompt": "Al pasar una integral doble a coordenadas polares, dA = dx dy se convierte en r dr dθ (y NO simplemente dr dθ). ¿Por qué aparece esa r extra?",
                "answer": "Porque una celda polar tiene largo dr pero su ancho de arco es r·dθ (las celdas se ensanchan al alejarse del origen!).",
                "hints": ["Longitud de arco de un ángulo dθ a distancia r del centro."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "El ancho del arco crece con la distancia al centro (r·dθ), así que el área es r dr dθ",
                            "Porque el radio siempre se eleva al cuadrado",
                            "Solo hace falta cuando el radio es mayor que 1",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Integral doble en polares sobre un círculo de radio 3",
                "prompt": "Calculá el volumen bajo el cono z = r sobre el disco de radio 3: ∫(θ=0..2π) ∫(r=0..3) r · (r dr dθ) = 2π · [r³/3]_0^3 = k · π. ¿Cuánto vale k? Respondé solo con el número.",
                "answer": "18 (volumen = 18π): [r³/3] de 0 a 3 vale 27/3 = 9, y 2π × 9 = 18π!",
                "hints": ["Integrá r² de 0 a 3 (da 9) y multiplicá por 2."],
                "payload": {"check": {"type": "numeric", "value": 18, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Teorema de Fubini (cambiar el orden de integración)",
                "prompt": "Sobre un rectángulo [a, b] × [c, d], si f(x, y) es continua, ¿cómo se relaciona ∫_a^b ∫_c^d f dy dx con ∫_c^d ∫_a^b f dx dy?",
                "answer": "Dan exactamente el mismo número (Fubini): podés elegir el orden de integración que haga las cuentas más fáciles.",
                "hints": ["Cortar un pan en rebanadas a lo largo o a lo ancho da el mismo volumen."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Son exactamente iguales (Teorema de Fubini)",
                            "Tienen signos opuestos",
                            "Solo coinciden si f es constante",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 36: LÍNEA, SUPERFICIE, GREEN, STOKES Y GAUSS ====================
    {
        "slug": "mv-linea-superficie",
        "title": "97. Integrales de línea (trabajo) y flujo por superficies",
        "level": 36,
        "order_index": 97,
        "summary": "Trabajo ∫_C F · dr, Teorema Fundamental de Integrales de Línea (campos conservativos) y flujo ∬_S F · dS.",
        "prerequisites": ["mv-divergencia-rotacional", "mv-integrales-dobles-triples"],
        "metadata": {"section": "Cálculo multivariable", "lab_tab": "multivar_int", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Teorema Fundamental de Integrales de Línea (campo conservativo)",
                "prompt": "El campo F = ⟨2x, 2y⟩ es conservativo con potencial f(x, y) = x² + y². Calculá el trabajo ∫_C F · dr para ir desde A(1, 2) hasta B(3, 4) usando f(B) − f(A). Respondé solo con el número.",
                "answer": "20: f(3, 4) − f(1, 2) = (9 + 16) − (1 + 4) = 25 − 5 = 20 (da 20 sin importar qué camino tomes!).",
                "hints": ["Calculá (3² + 4²) − (1² + 2²)."],
                "payload": {
                    "lab_link": "math:multivar_int",
                    "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Trabajo de un campo conservativo en una curva cerrada",
                "prompt": "Un excursionista sube una montaña por un sendero largo y vuelve exactamente al campamento base bajo el campo conservativo de gravedad. ¿Cuánto vale el trabajo neto ∮_C F · dr?",
                "answer": "0: en todo campo conservativo F = ∇f, si empezás y terminás en el mismo punto A, f(A) − f(A) = 0.",
                "hints": ["Aplicá f(fin) − f(inicio) cuando fin = inicio."],
                "payload": {"check": {"type": "numeric", "value": 0, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Trabajo de una fuerza constante en un segmento recto",
                "prompt": "Una fuerza constante F = ⟨4, 3⟩ N mueve una caja en línea recta desde (0, 0) hasta (5, 2) (Δr = ⟨5, 2⟩ m). Calculá el trabajo W = F · Δr (en Joules). Respondé solo con el número.",
                "answer": "26 J: (4)(5) + (3)(2) = 20 + 6 = 26 J.",
                "hints": ["Hacé el producto punto ⟨4, 3⟩ · ⟨5, 2⟩."],
                "payload": {"check": {"type": "numeric", "value": 26, "tolerance": 0, "unit": "J"}},
            },
            {
                "item_type": "worked_example",
                "title": "Flujo uniforme atravesando una sección de tubería",
                "prompt": "Agua fluye con velocidad v = ⟨0, 0, 5⟩ m/s perpendicular a una abertura plana de área 3 m² (normal n = ⟨0, 0, 1⟩). Calculá el flujo (caudal) Φ = (v · n) · Área (en m³/s). Respondé solo con el número.",
                "answer": "15 m³/s: (5)(3) = 15 m³/s atraviesan la sección cada segundo.",
                "hints": ["Multiplicá la componente perpendicular (5 m/s) por el área (3 m²)."],
                "payload": {"check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": "m³/s"}},
            },
            {
                "item_type": "worked_example",
                "title": "Flujo cuando el campo corre paralelo a la superficie",
                "prompt": "Un viento horizontal v = ⟨8, 0, 0⟩ m/s sopla paralelo al techo plano de una casa (normal hacia arriba n = ⟨0, 0, 1⟩). ¿Cuál es el flujo de aire que ATRAVIESA el techo? Respondé solo con el número.",
                "answer": "0: como v · n = 0 (el viento roza el techo sin cruzarlo), el flujo a través de la superficie es 0.",
                "hints": ["Calculá el producto punto ⟨8, 0, 0⟩ · ⟨0, 0, 1⟩."],
                "payload": {"check": {"type": "numeric", "value": 0, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Diferencia entre integral de línea escalar y vectorial",
                "prompt": "¿Qué mide una integral de línea vectorial ∫_C F · dr frente a una escalar ∫_C f ds?",
                "answer": "La vectorial suma solo la componente de F a favor del movimiento (trabajo/circulación, cambia de signo si invertís el recorrido); la escalar suma una densidad f por largo ds (ej. masa de un cable).",
                "hints": ["dr lleva dirección (producto punto con F); ds es siempre una longitud positiva."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "La vectorial mide trabajo/circulación (depende del sentido); la escalar suma densidad a lo largo del cable",
                            "Son exactamente la misma integral con distinta letra",
                            "La vectorial solo existe en 3D",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "mv-teorema-green",
        "title": "98. Teorema de Green (borde 2D = rotacional interior)",
        "level": 36,
        "order_index": 98,
        "summary": "Cambiar una integral de línea cerrada ∮ P dx + Q dy por la integral doble del rotacional ∬ (∂Q/∂x − ∂P/∂y) dA y forma de flujo 2D.",
        "prerequisites": ["mv-linea-superficie"],
        "metadata": {"section": "Cálculo multivariable", "lab_tab": "multivar_int", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Aplicar Green sobre un rectángulo sin parametrizar bordes",
                "prompt": "Usá el Teorema de Green ∮(−y dx + x dy) = ∬ (∂Q/∂x − ∂P/∂y) dA alrededor del borde antihorario de un rectángulo de 4 × 5 (área 20). Como rot = 1 − (−1) = 2, ¿cuánto da la circulación? Respondé solo con el número.",
                "answer": "40: ∬ 2 dA = 2 × 20 = 40 (en un segundo en vez de parametrizar 4 segmentos!).",
                "hints": ["Multiplicá el rotacional constante (2) por el área del rectángulo (20)."],
                "payload": {
                    "lab_link": "math:multivar_int",
                    "check": {"type": "numeric", "value": 40, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Teorema de Green con campo F = ⟨2y, 5x⟩",
                "prompt": "El campo F = ⟨2y, 5x⟩ tiene rotacional 2D constante ∂(5x)/∂x − ∂(2y)/∂y = 5 − 2 = 3. ¿Cuál es su circulación antihoraria alrededor de cualquier región de área 10? Respondé solo con el número.",
                "answer": "30: por Green, ∮ F · dr = ∬ 3 dA = 3 × 10 = 30 (no importa si la región es un círculo, un triángulo o un trébol!).",
                "hints": ["Multiplicá rot = 3 por Área = 10."],
                "payload": {
                    "lab_link": "math:multivar_int",
                    "check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Qué pasa si recorrés la curva en sentido HORARIO",
                "prompt": "En el problema anterior (F = ⟨2y, 5x⟩, región de área 10), si recorrés el borde en sentido HORARIO (opuesto a la convención positiva de Green), ¿cuánto da la integral de línea? Respondé solo con el número.",
                "answer": "−30: invertir la orientación de la curva siempre cambia el signo de la integral de línea.",
                "hints": ["La orientación estándar de Green es antihoraria (+30); horaria invierte el signo."],
                "payload": {"check": {"type": "numeric", "value": -30, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Forma de flujo 2D de Green (divergencia en el plano)",
                "prompt": "Por la versión de flujo de Green, el flujo neto saliente por un borde cerrado es ∮ F · n ds = ∬ div(F) dA. Para F = ⟨3x, 4y⟩ (div = 7) saliendo de una región de área 6, ¿cuánto flujo sale? Respondé solo con el número.",
                "answer": "42: ∬ 7 dA = 7 × 6 = 42.",
                "hints": ["Calculá div(F) = 3 + 4 = 7 y multiplicalo por el área (6)."],
                "payload": {
                    "lab_link": "math:multivar_int",
                    "check": {"type": "numeric", "value": 42, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Por qué se cancela el interior en el Teorema de Green",
                "prompt": "¿Por qué sumar todos los micro-remolinos (rotacionales) adentro de una región equivale a recorrer solamente su borde exterior?",
                "answer": "Porque cada arista interna es recorrida dos veces en sentidos opuestos por los dos cuadraditos vecinos y se cancela; solo sobrevive la frontera exterior!",
                "hints": ["Imaginá dos engranajes o cuadrados pegados girando ambos antihorario: en la pared compartida uno sube y el otro baja."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Las circulaciones en bordes internos compartidos van en sentidos opuestos y se cancelan",
                            "El rotacional vale siempre cero en el interior",
                            "El borde exterior siempre es un círculo",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Requisito crítico para aplicar Green sin errores",
                "prompt": "El campo F = ⟨−y/(x²+y²), x/(x²+y²)⟩ tiene rot = 0 en todos lados excepto en el origen (0, 0), donde divide por cero. ¿Podés aplicar Green directo en un círculo que encierra al origen?",
                "answer": "NO: el Teorema de Green exige que el campo y sus derivadas parciales sean continuos en TODO el interior de la región (sin agujeros ni singularidades adentro).",
                "hints": ["En (0, 0) hay una singularidad dentro del círculo, así que Green no aplica directamente allí."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "No, porque hay una singularidad (división por cero) dentro de la región",
                            "Sí, y la circulación da siempre 0",
                            "Sí, siempre que el radio sea 1",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "mv-stokes-divergencia",
        "title": "99. Teoremas de Stokes y de la Divergencia (Gauss) en 3D",
        "level": 36,
        "order_index": 99,
        "summary": "Elevar Green a superficies 3D (Stokes), cambiar flujo por volumen (Gauss) y unificar todo el Cálculo y las leyes de Maxwell.",
        "prerequisites": ["mv-teorema-green"],
        "metadata": {"section": "Cálculo multivariable", "lab_tab": "multivar_int", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Teorema de la Divergencia (Gauss) en un cubo",
                "prompt": "Para F(x, y, z) = ⟨2x, 3y, 4z⟩, la divergencia es constante: div(F) = 2 + 3 + 4 = 9. Por el Teorema de Gauss ∬_S F · dS = ∭_V div(F) dV, ¿cuál es el flujo saliente total a través de las 6 caras de un cubo de lado 2 (volumen 8)? Respondé solo con el número.",
                "answer": "72: 9 × 8 = 72 (una multiplicación en vez de 6 integrales de superficie!).",
                "hints": ["Multiplicá div(F) = 9 por el volumen del cubo (2³ = 8)."],
                "payload": {
                    "lab_link": "math:multivar_int",
                    "check": {"type": "numeric", "value": 72, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Gauss en una esfera de volumen 10 m³",
                "prompt": "El campo radial F = ⟨x, y, z⟩ tiene div(F) = 1 + 1 + 1 = 3. ¿Cuál es el flujo saliente total a través de cualquier superficie cerrada que encierra un volumen de 10 m³? Respondé solo con el número.",
                "answer": "30: ∭ 3 dV = 3 × 10 = 30.",
                "hints": ["Multiplicá div(F) = 3 por el volumen (10)."],
                "payload": {
                    "lab_link": "math:multivar_int",
                    "check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ley de Gauss eléctrica cuando no hay carga adentro",
                "prompt": "Una superficie cerrada está inmersa en un campo eléctrico uniforme, pero adentro NO encierra ninguna carga eléctrica (Q_enc = 0). ¿Cuánto vale el flujo eléctrico neto total ∬ E · dS?",
                "answer": "0: todo campo que entra por un lado vuelve a salir por el otro; solo las fuentes/cargas internas producen flujo neto distinto de cero.",
                "hints": ["Por la Ley de Gauss, flujo neto = Q_enc / ε₀."],
                "payload": {"check": {"type": "numeric", "value": 0, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Teorema de Stokes: cambiar una superficie difícil por un disco plano",
                "prompt": "Un domo semiesférico y un disco plano comparten exactamente el mismo borde circular C en el plano XY. Según el Teorema de Stokes ∬_S (∇ × F) · dS = ∮_C F · dr, ¿cómo se compara el flujo del rotacional por ambas superficies?",
                "answer": "Es exactamente IGUAL: solo depende de la curva frontera C, así que podés cambiar una superficie 3D complicada por el disco plano más fácil!",
                "hints": ["Ambos comparten el mismo lado derecho ∮_C F · dr."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Es exactamente igual (solo depende de la curva frontera C)",
                            "El domo tiene el doble de flujo porque tiene el doble de área",
                            "El disco plano siempre da 0",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Flujo del rotacional a través de una esfera cerrada (sin borde)",
                "prompt": "¿Cuánto vale ∬_S (∇ × F) · dS sobre una superficie CERRADA completa como una esfera (que no tiene ninguna curva borde C)? Respondé solo con el número.",
                "answer": "0: por Stokes la frontera es vacía (y por Gauss, div(rot F) = 0 siempre!).",
                "hints": ["Una esfera cerrada no tiene frontera C."],
                "payload": {"check": {"type": "numeric", "value": 0, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "La gran idea que unifica TFC, Green, Stokes y Gauss",
                "prompt": "¿Qué patrón universal comparten el Teorema Fundamental del Cálculo, Green, Stokes y el Teorema de la Divergencia?",
                "answer": "Todos transforman la integral de una 'derivada' (f', ∇f, rot F, div F) en el INTERIOR de una región en una medición hecha únicamente sobre su BORDE.",
                "hints": ["Compará ∫_a^b f' dx = f(b) − f(a) con ∭ div(F) dV = ∬ F · dS."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Integrar una derivada en el interior equivale a evaluar el campo en la frontera (borde)",
                            "Todos sirven únicamente en dos dimensiones",
                            "Todos requieren que el campo sea constante",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
]

MULTIVARIABLE_LESSONS: dict[str, dict] = {
    "mv-espacio-superficies": {
        "hook": "El mundo real no depende de una sola `x`: la temperatura de un mapa depende de `(x, y)` y un avión vuela en `(x, y, z)`. Aquí pasás de curvas planas a paisajes 3D.",
        "concept": {
            "points": [
                "Una función **`z = f(x, y)`** dibuja una **superficie 3D**. Para verla en papel se usan **curvas de nivel** (`f(x, y) = c`): donde las curvas se apilan muy juntas, la pendiente es empinada; donde se separan, el terreno es llano.",
                "**Producto cruz 3D (`u × v`)**: produce un **vector perpendicular** tanto a `u` como a `v` (dirección por regla de la mano derecha), cuya magnitud **`|u × v| = |u||v|sen(θ)`** es el área del paralelogramo que forman. ¡Ojo: `v × u = −(u × v)`!",
                "**Ecuación de un plano**: basta un punto `(x₀, y₀, z₀)` y un **vector normal `n = ⟨a, b, c⟩`** perpendicular al plano → **`a(x − x₀) + b(y − y₀) + c(z − z₀) = 0`** (`ax + by + cz = d`).",
            ],
            "real_world": [
                {
                    "title": "Mapas topográficos y mapas de presión (isobaras)",
                    "detail": "Cuando las isobaras de un pronóstico meteorológico están muy apretadas, el cambio de presión es brusco y soplan vientos fuertes.",
                },
                {
                    "title": "Torque y fuerza magnética en Física (`τ = r × F`)",
                    "detail": "Al apretar un tornillo con una llave inglesa, el torque es máximo a `90°` (`sen 90° = 1`) y apunta a lo largo del eje del tornillo.",
                },
                {
                    "title": "Normales de triángulos en gráficos 3D",
                    "detail": "Un motor gráfico calcula el producto cruz de dos bordes de cada triángulo de una malla 3D para saber hacia dónde apunta la cara y cómo reflejar la luz.",
                },
            ],
            "key_rule": "Curvas juntas = empinado | |u × v| = |u||v|sen(θ), perpendicular a ambos, v × u = −(u × v) | Plano: n · (r − r₀) = 0.",
            "pitfall": "Creer que `u × v = v × u` (eso solo vale para el producto punto `u · v`, no para el producto cruz!).",
        },
        "example": {
            "title": "Ecuación del plano normal a n = ⟨2, −1, 3⟩ pasando por (1, 0, 2)",
            "steps": [
                "Los coeficientes de `x, y, z` son directamente las componentes de `n`: `2x − 1y + 3z = d`.",
                "Sustituimos el punto conocido `(1, 0, 2)` para hallar `d`: `2(1) − 0 + 3(2) = 8`.",
                "Ecuación final: `2x − y + 3z = 8` (cualquier punto del plano cumple `n · (r − r₀) = 0`).",
            ],
            "lab_link": "math:multivar_diff",
            "lab_cta": "Practicar cálculo multivariable en el Laboratorio",
        },
        "check": {
            "question": "Si `u = ⟨1, 0, 0⟩` (eje `+x`) y `v = ⟨0, 1, 0⟩` (eje `+y`), ¿cuánto da `u × v`?",
            "options": [
                {"text": "`⟨0, 0, 1⟩` (eje `+z`)", "ok": True, "feedback": "Exacto: por regla de la mano derecha, girar de +x hacia +y levanta el pulgar hacia +z."},
                {"text": "`⟨0, 0, −1⟩` (eje `−z`)", "ok": False, "feedback": "Eso es v × u (orden invertido)."},
                {"text": "`0`", "ok": False, "feedback": "0 es el producto PUNTO u · v (son perpendiculares); el producto CRUZ tiene magnitud 1."},
            ],
        },
        "checks": [
            {
                "question": "En el plano `4x − 2y + 7z = 11`, ¿cuál es un vector normal perpendicular al plano?",
                "options": [
                    {"text": "`⟨4, −2, 7⟩`", "ok": True, "feedback": "Exacto: se lee directo de los coeficientes de x, y, z."},
                    {"text": "`⟨4, 2, 7⟩`", "ok": False, "feedback": "Cuidado con el signo negativo del término −2y."},
                    {"text": "`⟨4, −2, 11⟩`", "ok": False, "feedback": "El 11 de la derecha solo corre el plano en paralelo, no cambia su inclinación."},
                ],
            },
            {
                "question": "Las curvas de nivel de `f(x, y) = x² + y²` (un paraboloide) son:",
                "options": [
                    {"text": "Círculos concéntricos alrededor del origen (`x² + y² = c`)", "ok": True, "feedback": "Exacto: al fijar la altura z = c queda la ecuación de un círculo de radio √c."},
                    {"text": "Rectas paralelas", "ok": False, "feedback": "Rectas paralelas son las curvas de nivel de un plano ax + by."},
                    {"text": "Hipérbolas", "ok": False, "feedback": "Hipérbolas salen de x² − y² = c (silla de montar)."},
                ],
            },
        ],
        "takeaway_prompt": "Compará en dos líneas el producto punto (`u · v`) con el producto cruz (`u × v`): qué devuelve cada uno y cuándo vale cero.",
    },
    "mv-parciales-gradiente": {
        "hook": "Si estás parado en una montaña llena de niebla, el vector gradiente `∇f` es la brújula mágica que apunta SIEMPRE en la dirección exacta en la que la subida es más empinada.",
        "concept": {
            "points": [
                "**Derivadas parciales (`∂f/∂x`, `∂f/∂y`)**: derivás respecto de UNA variable mientras **congelás todas las demás como si fueran números fijos**.",
                "**El Gradiente `∇f = ⟨∂f/∂x, ∂f/∂y⟩`**: apunta en la dirección de **máximo ascenso**, su magnitud `|∇f|` es esa pendiente máxima, y es siempre **perpendicular (`90°`) a las curvas de nivel**.",
                "**Derivada direccional y Cadena**: la pendiente al caminar en cualquier dirección **unitaria `u`** es **`D_u f = ∇f · u`**. Y si te movés por `r(t) = ⟨x(t), y(t)⟩`, la tasa de cambio es **`df/dt = ∇f · r'(t) = f_x·x' + f_y·y'`**.",
            ],
            "real_world": [
                {
                    "title": "Descenso por gradiente en Inteligencia Artificial (`−∇L`)",
                    "detail": "Como `+∇L` apunta cuesta arriba, entrenar un modelo de IA da pasos en dirección **`−∇L`** (cuesta abajo más rápida) para minimizar el error con millones de parámetros.",
                },
                {
                    "title": "Flujo de calor y difusión",
                    "detail": "El calor siempre fluye desde lo más caliente a lo más frío en la dirección exacta de `−∇T`, perpendicular a las isotermas.",
                },
                {
                    "title": "Detección de bordes en visión por computadora",
                    "detail": "Los filtros de imágenes (como Sobel) calculan el gradiente del brillo `|∇I|` de cada píxel: donde el gradiente es enorme, hay un borde del objeto.",
                },
            ],
            "key_rule": "∇f = ⟨f_x, f_y⟩ (subida máxima, ⊥ curvas de nivel) | D_u f = ∇f · u (con |u| = 1) | df/dt = ∇f · v.",
            "pitfall": "Calcular `D_u f = ∇f · v` olvidando **normalizar `v`** a vector unitario (`u = v / |v|`) primero: sin normalizar el resultado queda inflado por `|v|`!",
        },
        "example": {
            "title": "Gradiente y derivada direccional de f(x, y) = x³y² + 5y en (2, 1)",
            "steps": [
                "Congelando `y`: `f_x = 3x²y²` → en `(2, 1)` vale `12`. Congelando `x`: `f_y = 2x³y + 5` → en `(2, 1)` vale `21`.",
                "Vector gradiente: `∇f(2, 1) = ⟨12, 21⟩` (la dirección más empinada, con pendiente `√(12² + 21²) ≈ 24.2`).",
                "Si caminamos hacia `u = ⟨0.6, 0.8⟩` (ya unitario): `D_u f = 12(0.6) + 21(0.8) = 7.2 + 16.8 = 24`.",
            ],
            "lab_link": "math:multivar_diff",
            "lab_cta": "Practicar derivadas parciales y gradiente en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es `∂f/∂x` de `f(x, y) = 4x²y³ + 7y² − 3x`?",
            "options": [
                {"text": "`8xy³ − 3`", "ok": True, "feedback": "Exacto: y³ es una constante multiplicando a 4x², y 7y² se deriva a 0 respecto de x."},
                {"text": "`8xy³ + 14y − 3`", "ok": False, "feedback": "Derivaste 7y² como si dependiera de x, pero y está congelada como constante."},
                {"text": "`24xy² − 3`", "ok": False, "feedback": "Derivaste x² e y³ a la vez; solo se deriva la x."},
            ],
        },
        "checks": [
            {
                "question": "Si querés bajar una montaña lo más rápido posible desde un punto donde `∇f = ⟨6, −8⟩`, ¿en qué dirección caminás?",
                "options": [
                    {"text": "En dirección `−∇f = ⟨−6, 8⟩` (y bajás a ritmo `−10`)", "ok": True, "feedback": "Exacto: el opuesto del gradiente es siempre el descenso más empinado (gradient descent!)."},
                    {"text": "En dirección `+∇f = ⟨6, −8⟩`", "ok": False, "feedback": "+∇f es el ascenso más empinado, no el descenso."},
                    {"text": "En dirección `⟨8, 6⟩`", "ok": False, "feedback": "⟨8, 6⟩ es perpendicular a ∇f: caminarías en plano sobre la curva de nivel (pendiente 0)."},
                ],
            },
            {
                "question": "Para calcular la derivada direccional en dirección del vector `v = ⟨3, 4⟩`, ¿qué hacés antes de hacer el producto punto con `∇f`?",
                "options": [
                    {"text": "Dividir `v` por su magnitud `5` para volverlo unitario (`u = ⟨0.6, 0.8⟩`)", "ok": True, "feedback": "Exacto: la fórmula D_u f = ∇f · u exige siempre |u| = 1."},
                    {"text": "Multiplicarlo por `5`", "ok": False, "feedback": "Hay que dividirlo por 5 para que mida 1."},
                    {"text": "Usarlo directo sin normalizar", "ok": False, "feedback": "Usarlo sin normalizar multiplicaría la pendiente real por 5."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué información te da el vector gradiente `∇f` y por qué el entrenamiento de redes neuronales avanza en dirección `−∇L`.",
    },
    "mv-optimizacion-lagrange": {
        "hook": "En 3D un punto plano (`∇f = 0`) no solo puede ser una cima o un pozo: también puede ser un **punto silla** (como un paso de montaña), y cuando hay un presupuesto limitado entran los multiplicadores de Lagrange.",
        "concept": {
            "points": [
                "**Puntos críticos 3D**: donde el plano tangente es horizontal → **`f_x = 0` y `f_y = 0`** a la vez.",
                "**Test del Hessiano**: calculás **`H = f_xx · f_yy − (f_xy)²`**: si **`H < 0`** → **punto silla**; si **`H > 0` y `f_xx > 0`** → **mínimo local**; si **`H > 0` y `f_xx < 0`** → **máximo local**; si `H = 0`, indeciso.",
                "**Multiplicadores de Lagrange** (optimizar `f` sujeto a una restricción `g(x, y) = c`): en el óptimo las curvas de nivel son tangentes, así que resolvés **`∇f = λ · ∇g`** junto con `g(x, y) = c`.",
            ],
            "real_world": [
                {
                    "title": "Puntos silla en paisajes de pérdida de IA",
                    "detail": "En espacios de millones de dimensiones, casi todos los puntos donde `∇L = 0` son puntos silla (suben en unas direcciones y bajan en otras), no mínimos locales.",
                },
                {
                    "title": "Economía: maximizar utilidad con presupuesto fijo",
                    "detail": "Lagrange demuestra que gastás óptimo cuando la utilidad marginal por peso gastado es igual en todos los bienes (`λ` = el valor extra de tener `$1` más de presupuesto!).",
                },
                {
                    "title": "Diseño estructural con peso límite",
                    "detail": "Maximizar la rigidez de una pieza de avión sujeto a una restricción de masa fija se formula directamente con `∇f = λ∇g`.",
                },
            ],
            "key_rule": "H = f_xx·f_yy − f_xy²: H < 0 ⇒ silla | H > 0, f_xx > 0 ⇒ mínimo | H > 0, f_xx < 0 ⇒ máximo | Restricción: ∇f = λ∇g.",
            "pitfall": "Olvidar restar `− (f_xy)²` en el Hessiano y mirar solo los signos de `f_xx` y `f_yy`: un término cruzado `f_xy` grande puede convertir un aparente mínimo en un punto silla!",
        },
        "example": {
            "title": "Clasificar (0, 0) en f(x, y) = x² − y² y optimizar xy sujeto a x + y = 10",
            "steps": [
                "En `f(x, y) = x² − y²`: `f_x = 2x = 0`, `f_y = −2y = 0` → punto crítico `(0, 0)`.",
                "Hessiano: `H = (2)(−2) − 0² = −4 < 0` → **punto silla** (mínimo en el eje X, máximo en el eje Y).",
                "Lagrange para `max(xy)` con `x + y = 10`: `⟨y, x⟩ = λ⟨1, 1⟩` → `x = y` → `2x = 10` → `(5, 5)` da máximo `25`.",
            ],
            "lab_link": "math:multivar_diff",
            "lab_cta": "Practicar parciales y operadores en el Laboratorio",
        },
        "check": {
            "question": "En un punto crítico sabés que `f_xx = −3`, `f_yy = −4` y `f_xy = 2`. Calculá `H` y clasificá el punto:",
            "options": [
                {"text": "`H = 8 > 0` y `f_xx < 0` → **máximo local**", "ok": True, "feedback": "Exacto: H = (−3)(−4) − 2² = 12 − 4 = 8 > 0 y f_xx = −3 < 0 (domo hacia abajo)."},
                {"text": "`H = 8 > 0` → mínimo local", "ok": False, "feedback": "Como f_xx = −3 es negativa, abre hacia abajo (máximo, no mínimo)."},
                {"text": "`H = −16 < 0` → punto silla", "ok": False, "feedback": "Menos por menos da más: (−3)(−4) = +12."},
            ],
        },
        "checks": [
            {
                "question": "Si `f_xx = 1`, `f_yy = 1` y `f_xy = 2`, ¿qué tipo de punto crítico es?",
                "options": [
                    {"text": "Punto silla (`H = 1·1 − 2² = −3 < 0`)", "ok": True, "feedback": "Exacto: aunque f_xx > 0 y f_yy > 0, la torsión f_xy = 2 hace caer la superficie por la diagonal y = −x!"},
                    {"text": "Mínimo local (porque `f_xx > 0` y `f_yy > 0`)", "ok": False, "feedback": "Justamente para detectar esa trampa existe el término −(f_xy)² del Hessiano!"},
                    {"text": "Máximo local", "ok": False, "feedback": "Al ser H < 0, sube en unas direcciones y baja en otras (silla)."},
                ],
            },
            {
                "question": "En el método de Lagrange, ¿qué representa económicamente el número `λ` en `∇f = λ∇g`?",
                "options": [
                    {"text": "Cuánto mejora el valor óptimo `f` por cada unidad extra que relajás la restricción `c`", "ok": True, "feedback": "Exacto: se llama 'precio sombra' (df*/dc = λ)."},
                    {"text": "Siempre vale `1`", "ok": False, "feedback": "λ cambia según las escalas de f y g."},
                    {"text": "Es siempre igual al valor máximo de `f`", "ok": False, "feedback": "Es la tasa de cambio del máximo respecto a la restricción, no el máximo mismo."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué un punto silla existe en 2D/3D aunque en 1D solo existían máximos, mínimos e inflexiones.",
    },
    "mv-divergencia-rotacional": {
        "hook": "Imaginá un fluido corriendo por el plano: la **divergencia** te dice dónde hay canillas o desagües (expansión), y el **rotacional** te dice dónde gira una ruedita de paletas (remolinos).",
        "concept": {
            "points": [
                "**Divergencia (`∇ · F`)**: para `F = ⟨P, Q⟩` (o `⟨P, Q, R⟩`), **`div(F) = ∂P/∂x + ∂Q/∂y (+ ∂R/∂z)`**. Es un **escalar**: `> 0` = fuente (se expande), `< 0` = sumidero (se comprime), `= 0` = incompresible.",
                "**Rotacional 2D (`∇ × F`)**: **`rot(F) = ∂Q/∂x − ∂P/∂y`**. Mide la tendencia a girar en torno a ese punto: `> 0` = giro antihorario, `< 0` = giro horario, `= 0` = irrotacional (sin remolino).",
                "**Campos conservativos (`F = ∇f`)**: si un campo proviene de un potencial `f`, SIEMPRE cumple **`rot(F) = 0`** (porque `f_yx − f_xy = 0`).",
            ],
            "real_world": [
                {
                    "title": "Las 4 Ecuaciones de Maxwell (electromagnetismo)",
                    "detail": "Toda la luz, el Wi-Fi y los motores eléctricos se escriben en 4 líneas usando divergencia y rotacional de `E` y `B` (`∇·B = 0` dice que no existen monopolos magnéticos!).",
                },
                {
                    "title": "Aerodinámica y meteorología (vorticidad)",
                    "detail": "Los meteorólogos ubican huracanes y tornados calculando el rotacional (`∇ × v`) del campo de vientos en la atmósfera.",
                },
                {
                    "title": "Simulación de agua y humo en cine (Navier-Stokes)",
                    "detail": "Para que el agua animada parezca real y no desaparezca ni explote, el simulador fuerza `∇ · v = 0` en cada fotograma.",
                },
            ],
            "key_rule": "div(F) = ∂P/∂x + ∂Q/∂y (fuente/sumidero, escalar) | rot₂D(F) = ∂Q/∂x − ∂P/∂y (giro) | Conservativo ⇒ rot = 0.",
            "pitfall": "Mezclar las derivadas: divergencia deriva `P` con `x` y `Q` con `y` (y SUMA); rotacional cruza `Q` con `x` menos `P` con `y` (y RESTA).",
        },
        "example": {
            "title": "Divergencia y rotacional del remolino F(x, y) = ⟨−y, x⟩",
            "steps": [
                "Divergencia: `∂(−y)/∂x + ∂(x)/∂y = 0 + 0 = 0` (el remolino gira en círculos sin expandirse ni comprimirse).",
                "Rotacional 2D: `∂(x)/∂x − ∂(−y)/∂y = 1 − (−1) = +2` (giro antihorario constante).",
                "Como `rot(F) = 2 ≠ 0`, este campo **NO es conservativo** (dar una vuelta a favor del remolino hace trabajo positivo distinto de cero!).",
            ],
            "lab_link": "math:multivar_diff",
            "lab_cta": "Practicar divergencia y rotacional en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto vale la divergencia de `F(x, y) = ⟨−4x, −y⟩` y qué representa físicamente?",
            "options": [
                {"text": "`−5` (sumidero: el campo se comprime hacia adentro)", "ok": True, "feedback": "Exacto: −4 + (−1) = −5 < 0."},
                {"text": "`+5` (fuente)", "ok": False, "feedback": "Ambos términos tienen signo negativo, así que fluye hacia adentro (sumidero)."},
                {"text": "`−3`", "ok": False, "feedback": "Sumaste mal: −4 + (−1) = −5 (no −4 − (−1))."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál es el rotacional 2D de `F(x, y) = ⟨2x, 3y⟩`?",
                "options": [
                    {"text": "`0` (`0 − 0 = 0`, irrotacional y conservativo con `f = x² + 1.5y²`)", "ok": True, "feedback": "Exacto: es el gradiente de `f = x² + 1.5y²`, así que se expande (su divergencia es `5`) pero no gira nada."},
                    {"text": "`5`", "ok": False, "feedback": "5 es la divergencia (∂P/∂x + ∂Q/∂y), no el rotacional."},
                    {"text": "`1`", "ok": False, "feedback": "En el rotacional las derivadas van cruzadas: ∂(3y)/∂x = 0 y ∂(2x)/∂y = 0."},
                ],
            },
            {
                "question": "Si un río corre solo horizontalmente pero más rápido arriba que abajo (`F = ⟨y, 0⟩`), ¿una ruedita de paletas gira (`rot ≠ 0`)?",
                "options": [
                    {"text": "Sí, gira en sentido horario (`rot = 0 − 1 = −1`)", "ok": True, "feedback": "Exacto: aunque todas las flechas son rectas paralelas, la corriente más rápida arriba empuja más las paletas superiores y hace girar la rueda!"},
                    {"text": "No, porque todas las flechas son líneas rectas", "ok": False, "feedback": "Esa es la intuición clave del rotacional: un flujo recto con distinta velocidad arriba y abajo (cizalladura) sí hace girar la rueda!"},
                    {"text": "Sí, en sentido antihorario (`+1`)", "ok": False, "feedback": "∂Q/∂x − ∂P/∂y = 0 − 1 = −1 (sentido horario)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con la imagen de un fluido (y una ruedita de paletas) qué miden la divergencia y el rotacional.",
    },
    "mv-integrales-dobles-triples": {
        "hook": "Para hallar el volumen bajo una carpa o la masa de un planeta cuya densidad cambia con la profundidad, integrás una dirección tras otra — y elegís el sistema de coordenadas que hace fácil la geometría.",
        "concept": {
            "points": [
                "**Integral doble `∬_R f(x, y) dA`**: suma los volúmenes de infinitas columnas de base `dA = dx dy` y altura `f(x, y)`. Se resuelve como **integral iterada** de adentro hacia afuera (congelando la variable exterior).",
                "**Teorema de Fubini**: en regiones bien comportadas podés intercambiar el orden `dy dx ↔ dx dy`. Y para regiones redondas pasás a **polares**, donde el elemento de área gana el factor Jacobiano **`dA = r dr dθ`**.",
                "**Integrales triples `∭_E f(x, y, z) dV`**: acumulan densidad en 3D (masa, carga total). Sus elementos de volumen son: rectangulares `dx dy dz`, **cilíndricas `r dz dr dθ`**, y **esféricas `ρ² sen(φ) dρ dφ dθ`**.",
            ],
            "real_world": [
                {
                    "title": "Centro de masa y momento de inercia",
                    "detail": "Para equilibrar un dron o satélite con piezas de distinta densidad, los ingenieros integran `∭ x·ρ(x,y,z) dV / M`.",
                },
                {
                    "title": "Probabilidad conjunta de dos variables aleatorias",
                    "detail": "La probabilidad de que altura y peso caigan en una región `R` es el volumen `∬_R p(x, y) dx dy` bajo la superficie de densidad conjunta.",
                },
                {
                    "title": "Lluvia total caída sobre una ciudad",
                    "detail": "Si el radar mide milímetros de lluvia `f(x, y)` en cada punto del mapa, `∬ f(x, y) dA` da el volumen total de agua caída.",
                },
            ],
            "key_rule": "Integrá de adentro hacia afuera | Polares: dA = r dr dθ | Cilíndricas: r dz dr dθ | Esféricas: ρ² sen φ dρ dφ dθ.",
            "pitfall": "Olvidar la `r` extra al convertir `dx dy → r dr dθ` en integrales dobles polares!",
        },
        "example": {
            "title": "Evaluar ∫(0..2) ∫(0..3) 2x dy dx y volumen bajo z = r en disco de radio 3",
            "steps": [
                "Integral interior (respecto de `y`, `2x` es constante): `[2xy]_{y=0}^{3} = 6x`.",
                "Integral exterior (respecto de `x`): `∫_0^2 6x dx = [3x²]_0^2 = 12`.",
                "En polares (`dA = r dr dθ`): `∫_0^(2π) ∫_0^3 r · (r dr) dθ = 2π · [r³/3]_0^3 = 2π(9) = 18π`.",
            ],
            "lab_link": "math:multivar_int",
            "lab_cta": "Practicar integrales dobles en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto vale `∫(x=0 a 1) ∫(y=0 a 2) 3y dy dx`?",
            "options": [
                {"text": "`6` (adentro `[1.5 y²]_0^2 = 6`, afuera `∫_0^1 6 dx = 6`)", "ok": True, "feedback": "Exacto: integrás 3y en y de 0 a 2 (da 6) y luego por el ancho en x (1)."},
                {"text": "`3`", "ok": False, "feedback": "Revisá: ∫_0^2 3y dy = 3(2²/2) = 6, no 3."},
                {"text": "`12`", "ok": False, "feedback": "Te olvidaste de dividir por 2 al antiderivar y → y²/2."},
            ],
        },
        "checks": [
            {
                "question": "Si integrás sobre el anillo `1 ≤ x² + y² ≤ 4`, ¿qué coordenadas simplifican drásticamente los límites?",
                "options": [
                    {"text": "Coordenadas polares (`1 ≤ r ≤ 2`, `0 ≤ θ ≤ 2π`, con `r dr dθ`)", "ok": True, "feedback": "Exacto: en polares el anillo se convierte en un simple rectángulo [1, 2] × [0, 2π]!"},
                    {"text": "Cartesianas `x, y`", "ok": False, "feedback": "En cartesianas tendrías que partir la región en varios trozos con raíces √(4 − x²) y √(1 − x²)."},
                    {"text": "Esféricas", "ok": False, "feedback": "El anillo vive en 2D, así que corresponden polares."},
                ],
            },
            {
                "question": "¿Qué representa físicamente `∭_E 1 dV` (integrar la función constante `1` sobre un sólido `E`)?",
                "options": [
                    {"text": "El volumen exacto del sólido `E`", "ok": True, "feedback": "Exacto: igual que ∬ 1 dA calcula el área de una región 2D."},
                    {"text": "El área superficial de `E`", "ok": False, "feedback": "dV suma bloquecitos de volumen 3D, no parches de superficie."},
                    {"text": "Siempre vale `1`", "ok": False, "feedback": "Vale 1 solo si el volumen del sólido es 1."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué el factor `r` aparece en `dA = r dr dθ` y cuándo te conviene cambiar a polares.",
    },
    "mv-linea-superficie": {
        "hook": "Cuánto trabajo hace el viento sobre un velero a lo largo de una ruta curva (`∫ F · dr`) y cuánta agua atraviesa una red sumergida (`∬ F · dS`) son las dos integrales centrales de la física.",
        "concept": {
            "points": [
                "**Integral de línea vectorial `∫_C F · dr`**: acumula el producto punto de un campo `F` con cada mini-paso `dr = r'(t)dt` a lo largo de la curva `C` (en física: **trabajo**; en curva cerrada: **circulación**).",
                "**Teorema Fundamental de Integrales de Línea**: si `F` es **conservativo (`F = ∇f`)**, el trabajo NO depende del camino: **`∫_C ∇f · dr = f(B) − f(A)`**, y en cualquier curva cerrada vale **`0`**!",
                "**Integral de superficie / Flujo `∬_S F · dS = ∬_S (F · n) dS`**: suma solo la componente de `F` **perpendicular** a la superficie `S` (mide caudal de fluido, flujo eléctrico o magnético que atraviesa la membrana).",
            ],
            "real_world": [
                {
                    "title": "Conservación de la energía (gravedad y campos eléctricos)",
                    "detail": "Como la gravedad es conservativa (`F = −∇U`), el trabajo al subir una valija al 5.° piso solo depende de la diferencia de altura `U(B) − U(A)`, no de si usaste escalera o rampa.",
                },
                {
                    "title": "Paneles solares y orientación (`Φ = I · n · A`)",
                    "detail": "El flujo de energía solar captado es máximo cuando los rayos golpean perpendiculares al panel (`cos 0° = 1`) y cero si llegan rasantes (`cos 90° = 0`).",
                },
                {
                    "title": "Inducción electromagnética (Ley de Faraday)",
                    "detail": "Los generadores eléctricos producen voltaje cambiando el flujo magnético `∬ B · dS` que atraviesa una bobina de cobre.",
                },
            ],
            "key_rule": "Trabajo: ∫_C F · dr | Conservativo (F = ∇f): f(B) − f(A) (cerrada = 0) | Flujo: ∬_S (F · n) dS.",
            "pitfall": "Parametrizar una curva complicada para calcular `∫_C F · dr` sin chequear primero si `F` es conservativo (`rot F = 0` en una región sin agujeros): si lo es, `f(B) − f(A)` te ahorra el 95% de las cuentas!",
        },
        "example": {
            "title": "Trabajo de F = ⟨2x, 2y⟩ de (1, 2) a (3, 4) por una espiral cualquiera",
            "steps": [
                "Chequeamos rotacional: `∂(2y)/∂x − ∂(2x)/∂y = 0 − 0 = 0` en todo el plano → `F` es conservativo!",
                "Hallamos el potencial integrando: `f(x, y) = x² + y²` (verificación: `∇f = ⟨2x, 2y⟩`).",
                "Aplicamos el Teorema Fundamental: `f(3, 4) − f(1, 2) = 25 − 5 = 20` (sin parametrizar la espiral!).",
            ],
            "lab_link": "math:multivar_int",
            "lab_cta": "Practicar integrales de línea conservativas en el Laboratorio",
        },
        "check": {
            "question": "Si `F = ∇f` con `f(x, y) = x·y`, ¿cuánto vale `∫_C F · dr` a lo largo de cualquier curva desde `(1, 2)` hasta `(4, 3)`?",
            "options": [
                {"text": "`10` (`f(4, 3) − f(1, 2) = 12 − 2`)", "ok": True, "feedback": "Exacto: el trabajo depende únicamente de los extremos."},
                {"text": "`14` (`12 + 2`)", "ok": False, "feedback": "Se RESTA f(fin) − f(inicio), no se suma."},
                {"text": "No se puede saber sin conocer la curva `C`", "ok": False, "feedback": "Como F = ∇f es conservativo, es completamente independiente del camino."},
            ],
        },
        "checks": [
            {
                "question": "Un panel de `2 m²` recibe un campo uniforme perpendicular de intensidad `10 W/m²`. Si inclinás el panel `60°` (`cos 60° = 0.5`), ¿cuánto flujo atraviesa el panel?",
                "options": [
                    {"text": "`10 W` (`10 × 2 × 0.5`)", "ok": True, "feedback": "Exacto: F · n · A = |F|·A·cos(60°) = 20 × 0.5 = 10 W."},
                    {"text": "`20 W`", "ok": False, "feedback": "20 W es cuando está completamente perpendicular (0°)."},
                    {"text": "`0 W`", "ok": False, "feedback": "Es 0 W solo a 90° (paralelo a los rayos)."},
                ],
            },
            {
                "question": "Si un campo NO es conservativo (como la fricción), ¿el trabajo alrededor de un circuito cerrado vale necesariamente `0`?",
                "options": [
                    {"text": "No: la fricción siempre se opone al movimiento y hace trabajo negativo neto en un lazo cerrado", "ok": True, "feedback": "Exacto: solo los campos conservativos garantizan circulación 0 en toda curva cerrada."},
                    {"text": "Sí, todo trabajo cerrado siempre es 0", "ok": False, "feedback": "Arrastrar una caja en círculo y volver al inicio gasta energía por rozamiento (W < 0)."},
                    {"text": "Siempre es positivo", "ok": False, "feedback": "La fricción apunta contra dr, así que F · dr < 0."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en tus palabras por qué un campo conservativo te permite olvidarte por completo de la forma del camino entre `A` y `B`.",
    },
    "mv-teorema-green": {
        "hook": "El Teorema de Green es un puente espectacular en 2D: te deja cambiar una caminata por el borde cerrado (`∮`) por sumar todos los mini-remolinos del interior (`∬`), ¡o al revés!",
        "concept": {
            "points": [
                "**Teorema de Green (circulación)**: para una curva cerrada simple `C` recorrida en sentido **antihorario** alrededor de `R` (sin agujeros ni singularidades adentro): **`∮_C (P dx + Q dy) = ∬_R (∂Q/∂x − ∂P/∂y) dA`**.",
                "**¿Por qué funciona?** Si partís `R` en miles de celdas, las circulaciones internas en aristas compartidas van en sentidos contrarios y se cancelan; la suma total es exactamente el borde exterior!",
                "**Dos bonos increíbles**: si elegís `P = −y/2, Q = x/2` (rot = `1`), obtenés el **área** midiendo solo el perímetro (`A = (1/2)∮(x dy − y dx)`). Y la versión **flujo 2D** relaciona el caudal saliente con la divergencia: **`∮_C F · n ds = ∬_R div(F) dA`**.",
            ],
            "real_world": [
                {
                    "title": "El planímetro mecánico (medir áreas rodeando un mapa)",
                    "detail": "Ese instrumento clásico de agrimensura calcula el área de cualquier lago irregular en un mapa solo trazando su borde, ejecutando físicamente `(1/2)∮(x dy − y dx)`!",
                },
                {
                    "title": "Fórmula del cordón (Shoelace) en programación y GIS",
                    "detail": "Calcular el área de cualquier polígono desde sus vértices `(x_i, y_i)` es la versión discreta del Teorema de Green.",
                },
                {
                    "title": "Circulación aerodinámica y sustentación de un ala",
                    "detail": "La fuerza de sustentación de un avión es proporcional a la circulación del aire alrededor del perfil del ala (`∮ v · dr`), conectada con la vorticidad por Green.",
                },
            ],
            "key_rule": "Green (antihorario): ∮_C P dx + Q dy = ∬_R (∂Q/∂x − ∂P/∂y) dA | Flujo 2D: ∮ F · n ds = ∬ div(F) dA.",
            "pitfall": "Olvidar chequear dos cosas: 1) la orientación (si es horaria, poné signo `−`), y 2) que el campo sea suave sin singularidades en TODO el interior de `R`.",
        },
        "example": {
            "title": "Evaluar ∮_C (2y dx + 5x dy) sobre cualquier borde antihorario de área 10",
            "steps": [
                "Identificamos `P = 2y` y `Q = 5x` (ambos suaves en todo el plano, sin singularidades!).",
                "Calculamos el rotacional 2D: `∂Q/∂x − ∂P/∂y = 5 − 2 = 3` (una constante!).",
                "Por Green: `∮_C F · dr = ∬_R 3 dA = 3 × Área(R) = 3 × 10 = 30`.",
            ],
            "lab_link": "math:multivar_int",
            "lab_cta": "Practicar Green y Gauss en el Laboratorio",
        },
        "check": {
            "question": "Aplicá el Teorema de Green para hallar `∮_C (y dx + 4x dy)` en sentido antihorario alrededor de un cuadrado de lado `3` (área `9`):",
            "options": [
                {"text": "`27` (`rot = 4 − 1 = 3`, multiplicado por área `9`)", "ok": True, "feedback": "Exacto: ∬ 3 dA = 3 × 9 = 27."},
                {"text": "`45`", "ok": False, "feedback": "Sumaste 4 + 1 en vez de restar ∂Q/∂x − ∂P/∂y = 4 − 1 = 3."},
                {"text": "`−27`", "ok": False, "feedback": "Como la orientación es antihoraria, el signo es positivo (+27)."},
            ],
        },
        "checks": [
            {
                "question": "Si el campo `F = ⟨3x², 4y³⟩` se integra por un borde cerrado suave cualquiera, ¿cuánto da por el Teorema de Green?",
                "options": [
                    {"text": "`0` (porque `∂(4y³)/∂x − ∂(3x²)/∂y = 0 − 0 = 0`)", "ok": True, "feedback": "Exacto: es un campo conservativo, así que su rotacional y su circulación cerrada son 0."},
                    {"text": "`6x + 12y²`", "ok": False, "feedback": "Eso es la divergencia, no el rotacional 2D."},
                    {"text": "Depende del tamaño de la región", "ok": False, "feedback": "Integrar 0 sobre cualquier región siempre da 0."},
                ],
            },
            {
                "question": "Usando la versión de flujo 2D de Green (`∮ F · n ds = ∬ div(F) dA`), si `div(F) = −2` en toda una región de área `8`, ¿qué ocurre en el borde?",
                "options": [
                    {"text": "Hay un flujo neto de `−16` (entra más fluido del que sale: sumidero)", "ok": True, "feedback": "Exacto: −2 × 8 = −16."},
                    {"text": "Salen `+16` unidades", "ok": False, "feedback": "Divergencia negativa indica flujo entrante (negativo)."},
                    {"text": "El flujo neto es `0`", "ok": False, "feedback": "Solo es 0 si div(F) = 0 o las fuentes y sumideros internos se cancelan."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá la diferencia entre la forma de circulación (rotacional) y la forma de flujo (divergencia) del Teorema de Green.",
    },
    "mv-stokes-divergencia": {
        "hook": "Estos dos teoremas coronan todo el Cálculo: **Stokes** eleva Green a superficies 3D, **Gauss** relaciona la piel de un sólido con su volumen interno, y juntos escriben las leyes del electromagnetismo.",
        "concept": {
            "points": [
                "**Teorema de Stokes (3D)**: **`∮_C F · dr = ∬_S (∇ × F) · dS`** (orientación por regla de la mano derecha). Dos superficies distintas con el **mismo borde `C`** tienen el mismo flujo del rotacional — ¡podés reemplazar un domo complicado por su tapa plana!",
                "**Teorema de la Divergencia / Gauss (3D)**: para una superficie **cerrada** `S` que envuelve un volumen `V` (normales hacia afuera): **`∬_S F · dS = ∭_V (∇ · F) dV`**. El flujo total que escapa por la cáscara es la suma de todas las fuentes menos sumideros internos.",
                "**La gran unificación del Cálculo**: TFC 1D, TFC de líneas, Green, Stokes y Gauss son todos casos de una sola verdad universal: **`∫_(interior) (derivada) = ∫_(borde) (campo)`**!",
            ],
            "real_world": [
                {
                    "title": "Ley de Gauss de la electrostática y la gravedad",
                    "detail": "Permite calcular el campo eléctrico de una esfera o cable infinito en 2 renglones sin hacer integrales vectoriales imposibles.",
                },
                {
                    "title": "Ley de Faraday y Ampère-Maxwell (Stokes en acción)",
                    "detail": "Un campo magnético cambiante a través de una superficie (`∬ ∂B/∂t · dS`) induce voltaje alrededor del cable que la bordea (`∮ E · dr`) — así funciona todo transformador y generador!",
                },
                {
                    "title": "Conservación de masa, carga y calor (ecuación de continuidad)",
                    "detail": "El Teorema de Gauss traduce 'la cantidad que sale por la frontera iguala la pérdida interna' en las ecuaciones diferenciales de toda la física continua.",
                },
            ],
            "key_rule": "Stokes: ∮_C F·dr = ∬_S (∇×F)·dS | Gauss (cerrada): ∬_S F·dS = ∭_V (∇·F) dV | Interior(derivada) = Borde(campo).",
            "pitfall": "Aplicar el Teorema de Gauss a una superficie ABIERTA (como un tazón sin tapa): Gauss exige SIEMPRE una superficie completamente **cerrada** (si falta la tapa, sumás la tapa y después la restás!).",
        },
        "example": {
            "title": "Flujo de F = ⟨2x, 3y, 4z⟩ saliendo de un cubo de lado 2 usando Gauss",
            "steps": [
                "En lugar de calcular 6 integrales de superficie (una por cada cara del cubo), verificamos que el cubo es una superficie **cerrada**.",
                "Calculamos la divergencia: `∇ · F = ∂(2x)/∂x + ∂(3y)/∂y + ∂(4z)/∂z = 2 + 3 + 4 = 9`.",
                "Aplicamos Gauss: `∬_S F · dS = ∭_V 9 dV = 9 × Volumen(cubo) = 9 × 2³ = 72`!",
            ],
            "lab_link": "math:multivar_int",
            "lab_cta": "Practicar integrales múltiples, Green y Gauss en el Laboratorio",
        },
        "check": {
            "question": "Si `F = ⟨x, 2y, −z⟩`, ¿cuál es su divergencia `∇ · F`, y cuál es el flujo saliente de una esfera de volumen `15`?",
            "options": [
                {"text": "`div(F) = 2` → flujo saliente = `30` (`2 × 15`)", "ok": True, "feedback": "Exacto: 1 + 2 + (−1) = 2, y por Gauss 2 × 15 = 30."},
                {"text": "`div(F) = 4` → flujo saliente = `60`", "ok": False, "feedback": "Cuidado con el signo negativo de −z: 1 + 2 − 1 = 2."},
                {"text": "`div(F) = 0` → flujo = `0`", "ok": False, "feedback": "1 + 2 − 1 = 2 ≠ 0."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál es la condición geométrica indispensable sobre la superficie `S` para aplicar el Teorema de la Divergencia (Gauss)?",
                "options": [
                    {"text": "Debe ser una superficie **cerrada** que encierre completamente un volumen `V`", "ok": True, "feedback": "Exacto: si la superficie tiene un agujero o le falta una tapa, Gauss no aplica directo."},
                    {"text": "Debe ser plana (como un disco)", "ok": False, "feedback": "Un disco es abierto; Gauss necesita un cascarón cerrado (esfera, cubo, cilindro con tapas)."},
                    {"text": "Debe tener una curva borde `C`", "ok": False, "feedback": "Tener curva borde C corresponde al Teorema de Stokes, no a Gauss."},
                ],
            },
            {
                "question": "Según el Teorema de Stokes, ¿para qué te sirve cambiar una superficie 3D ondulada `S₁` por una superficie plana `S₂` que comparte el mismo borde `C`?",
                "options": [
                    {"text": "Para calcular `∬ (∇ × F) · dS` mucho más fácil porque ambas dan exactamente el mismo resultado", "ok": True, "feedback": "Exacto: en la superficie plana la normal n es constante (por ej. ⟨0, 0, 1⟩) y la cuenta colapsa en 2 líneas!"},
                    {"text": "Solo sirve si `∇ × F = 0`", "ok": False, "feedback": "Sirve para cualquier campo vectorial suave F."},
                    {"text": "Cambia el valor pero da una buena aproximación", "ok": False, "feedback": "No es aproximación: Stokes garantiza igualdad exacta!"},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en tus palabras cómo se conectan TFC (1D), Green (2D), Stokes (3D borde) y Gauss (3D volumen) bajo una misma idea.",
    },
}
