"""Algebra 1 curriculum (12 units, #30-#41) adapted from Khan Academy Algebra 1.

Covers all new Algebra 1 concepts building on Aritmética (#1-#17) and Preálgebra (#18-#29):
  - Multi-step & literal equations + compound unit analysis
  - Linear equation forms (standard, point-slope, perpendicular lines)
  - 2D inequalities & systems of inequalities
  - Function domain, range, features & average rate of change
  - Arithmetic & geometric sequences (explicit & recursive)
  - Absolute value & piecewise functions
  - Rational exponents & simplifying radicals
  - Exponential growth & decay
  - Multiplying binomials & special products
  - Factoring quadratics & zero-product property
  - Parabolas, vertex, quadratic formula & discriminant
  - Rational vs. irrational numbers
"""

from __future__ import annotations

ALGEBRA1_NODES: list[dict] = [
    # ==================== NIVEL 11: ECUACIONES AVANZADAS, UNIDADES Y RECTAS ====================
    {
        "slug": "al-ecuaciones-formulas",
        "title": "30. Ecuaciones complejas, despeje de fórmulas y unidades",
        "level": 11,
        "order_index": 30,
        "summary": "Ecuaciones sin solución o con infinitas soluciones, despejar variables en fórmulas reales y convertir tasas compuestas.",
        "prerequisites": ["p-ecuaciones-un-paso", "p-razones-tasas"],
        "metadata": {"section": "Álgebra 1", "lab_tab": "linear_eq", "est_minutes": 20},
        "items": [
            {
                "item_type": "recall",
                "title": "Detectar 0 soluciones vs. infinitas soluciones",
                "prompt": "Al resolver una ecuación llegás a 4x + 5 = 4x + 9 (y al restar 4x queda 5 = 9). ¿Cuántas soluciones tiene?",
                "answer": "Ninguna solución (0): ningún número x puede hacer que 5 sea igual a 9. En cambio, si llegaras a 5 = 5 (identidad), tendría infinitas soluciones.",
                "hints": ["¿Para qué valor de x es cierto que 5 = 9?"],
                "payload": {
                    "lab_link": "math:linear_eq",
                    "check": {
                        "type": "choice",
                        "options": [
                            "Ninguna solución (es una contradicción)",
                            "Infinitas soluciones (sirve cualquier x)",
                            "Una única solución: x = 4",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Despejar una fórmula literal (Física y Geometría)",
                "prompt": "El área de un triángulo es A = (b · h) / 2. Si necesitás despejar la altura h en función de A y b, ¿cómo queda?",
                "answer": "h = 2A / b: primero multiplicás ambos lados por 2 (2A = b · h) y luego dividís ambos lados por b.",
                "hints": ["Deshacé primero la división por 2 y después la multiplicación por b."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["h = 2A / b", "h = A / (2b)", "h = 2A − b"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Convertir temperatura de Fahrenheit a Celsius",
                "prompt": "Un día de verano en Estados Unidos el termómetro marca F = 86°F. Usando C = 5/9 · (F − 32), ¿cuántos °C son? Respondé solo con el número en °C.",
                "answer": "30°C: 86 − 32 = 54 → 54 ÷ 9 = 6 → 6 × 5 = 30°C.",
                "hints": ["Restá 32 primero, dividí por 9 y multiplicá por 5."],
                "payload": {"check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": "°C"}},
            },
            {
                "item_type": "worked_example",
                "title": "Análisis dimensional: convertir caudal de L/min a L/h",
                "prompt": "Una canilla que gotea pierde 0.25 litros por minuto. ¿Cuántos litros pierde en una hora completa (× 60 min/h)? Respondé solo con el número en L.",
                "answer": "15 litros por hora (0.25 × 60 = 15 L/h). Multiplicar por factores unitarios cancela los minutos y deja horas.",
                "hints": ["Multiplicá por 60 (un cuarto de 60)."],
                "payload": {"check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": "L"}},
            },
            {
                "item_type": "worked_example",
                "title": "Ecuación multi-paso con paréntesis en ambos lados",
                "prompt": "Resolvé 3(x + 2) = 2(x + 7). ¿Cuánto vale x? Respondé solo con el número.",
                "answer": "8: distribuís ambos lados → 3x + 6 = 2x + 14 → restás 2x (x + 6 = 14) → restás 6 → x = 8.",
                "hints": ["Distribuí el 3 y el 2 primero, después juntá las x."],
                "payload": {
                    "lab_link": "math:linear_eq",
                    "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Identidad: infinitas soluciones",
                "prompt": "Al simplificar 2(x + 3) = 2x + 6 ambos lados quedan idénticos. ¿Qué significa?",
                "answer": "Tiene infinitas soluciones: cualquier número real que pongas en x cumple la igualdad porque son dos maneras distintas de escribir la misma expresión.",
                "hints": ["Probá x = 0, x = 5 y x = −10: todos funcionan."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Infinitas soluciones: vale para cualquier valor de x",
                            "Ninguna solución",
                            "Solo vale para x = 0",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "al-formas-lineales",
        "title": "31. Formas de rectas (estándar y punto-pendiente) y perpendiculares",
        "level": 11,
        "order_index": 31,
        "summary": "Forma estándar Ax + By = C (interceptos rápidos), forma punto-pendiente y rectas perpendiculares (m₂ = −1/m₁).",
        "prerequisites": ["p-plano-rectas"],
        "metadata": {"section": "Álgebra 1", "lab_tab": "linear_fn", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Intercepto X desde la forma estándar (presupuesto)",
                "prompt": "Tenés $60 para comprar cuadernos de $6 (x) y lapiceras de $3 (y): 6x + 3y = 60. Si comprás 0 lapiceras (y = 0), ¿cuántos cuadernos comprás (intercepto en X)? Respondé solo con el número.",
                "answer": "10 cuadernos (6x = 60 → x = 10; intercepto en X = (10, 0)). Tapar la y te da el cruce con el eje X en 1 segundo.",
                "hints": ["Reemplazá y = 0 y despejá x."],
                "payload": {
                    "lab_link": "math:linear_fn",
                    "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Reconocer la forma punto-pendiente y − y₁ = m(x − x₁)",
                "prompt": "La recta y − 4 = 3(x − 2) está escrita en forma punto-pendiente. ¿Qué pendiente tiene y por qué punto pasa?",
                "answer": "Pendiente m = 3 y pasa por (2, 4). Atención a los signos: la fórmula lleva 'menos', así que x − 2 significa x₁ = +2.",
                "hints": ["Compara término a término con y − y₁ = m(x − x₁)."],
                "payload": {
                    "lab_link": "math:linear_fn",
                    "check": {
                        "type": "choice",
                        "options": [
                            "Pendiente 3, pasa por (2, 4)",
                            "Pendiente 3, pasa por (−2, −4)",
                            "Pendiente 4, pasa por (3, 2)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Pasar de forma estándar a pendiente-ordenada (y = mx + b)",
                "prompt": "Dada 2x + y = 9, despejá y para leer su pendiente m. ¿Cuánto vale la pendiente m? Incluí el signo.",
                "answer": "−2: al restar 2x en ambos lados queda y = −2x + 9, así que m = −2 y b = 9.",
                "hints": ["Despejá y restando 2x a ambos lados."],
                "payload": {
                    "lab_link": "math:linear_fn",
                    "check": {"type": "numeric", "value": -2, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Pendiente de una recta perpendicular (esquina a 90°)",
                "prompt": "Una calle en un plano tiene pendiente m₁ = 2 (o 2/1). ¿Cuál es la pendiente m₂ de una calle perpendicular (a 90°)? Respondé en decimal o fracción (ej. 0.25 o 1/4), con su signo.",
                "answer": "−0.5 (−1/2): para ser perpendiculares, las pendientes se invierten y cambian de signo (2 × (−1/2) = −1).",
                "hints": ["Las pendientes perpendiculares son opuestas e inversas: m₂ = −1/m₁.", "Da vuelta 2/1 a 1/2 y cambiale el signo."],
                "payload": {
                    "lab_link": "math:linear_fn",
                    "check": {"type": "numeric", "value": -0.5, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Recta horizontal vs. recta vertical",
                "prompt": "¿Cuál ecuación representa una recta HORIZONTAL que pasa por altura 5 (pendiente 0)?",
                "answer": "y = 5: sin importar qué valor tome x, la altura y es siempre 5. En cambio x = 5 es una recta VERTICAL (pendiente indefinida).",
                "hints": ["Si la altura es siempre 5, ¿qué letra vale siempre 5?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["y = 5", "x = 5", "y = 5x"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Hallar la ordenada b a partir de un punto y pendiente",
                "prompt": "Una recta tiene pendiente m = 4 y pasa por (2, 11). Usando y = 4x + b, ¿cuánto vale b? Respondé solo con el número.",
                "answer": "3: reemplazás (2, 11) → 11 = 4(2) + b → 11 = 8 + b → b = 3.",
                "hints": ["Sustituí x = 2 e y = 11 en y = 4x + b."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    {
        "slug": "al-sistemas-desigualdades",
        "title": "32. Gráficas y sistemas de desigualdades en 2D",
        "level": 11,
        "order_index": 32,
        "summary": "Frontera sólida vs. punteada, sombrear semiplanos y zonas factibles con dos restricciones simultáneas.",
        "prerequisites": ["p-desigualdades", "p-sistemas-ecuaciones"],
        "metadata": {"section": "Álgebra 1", "lab_tab": "systems", "est_minutes": 18},
        "items": [
            {
                "item_type": "recall",
                "title": "Línea sólida vs. línea punteada en una gráfica 2D",
                "prompt": "Al graficar la desigualdad y > 2x + 1 en el plano cartesiano, ¿la recta frontera se dibuja sólida o punteada, y qué lado se sombrea?",
                "answer": "Punteada (porque '>' NO incluye los puntos sobre la recta) y sombreada hacia ARRIBA (valores de y mayores).",
                "hints": ["'>' es estricto (no incluye el borde); '≥' sí lo incluye."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Punteada y sombreada por encima de la recta",
                            "Sólida y sombreada por encima de la recta",
                            "Punteada y sombreada por debajo de la recta",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Probar un punto testigo (0, 0) para saber qué lado sombrear",
                "prompt": "Querés saber si el punto (0, 0) está dentro de la zona solución de 2x + 3y ≤ 12. ¿Qué da al probarlo?",
                "answer": "Sí está incluido: 2(0) + 3(0) = 0 ≤ 12 (verdadero), así que se sombrea el lado que contiene al origen (0, 0).",
                "hints": ["Reemplazá x = 0 e y = 0 y chequeá si la desigualdad es verdadera."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Verdadero (0 ≤ 12): se sombrea el lado que contiene a (0, 0)",
                            "Falso: se sombrea el lado opuesto a (0, 0)",
                            "No se puede usar (0, 0) porque da cero",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Qué es la zona factible de un sistema de desigualdades",
                "prompt": "Organizás un evento con dos límites a la vez: presupuesto (5x + 10y ≤ 100) y capacidad del salón (x + y ≤ 15). En el gráfico, ¿qué combinaciones (x, y) son válidas?",
                "answer": "Solo los puntos donde se SUPERPONEN las dos regiones sombreadas (cumplen presupuesto Y capacidad a la vez).",
                "hints": ["Un sistema exige cumplir TODAS las restricciones simultáneamente."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Solo la región donde se cruzan/superponen ambos sombreados",
                            "Cualquier punto sombreado por al menos una de las dos rectas",
                            "Únicamente el único punto donde se cortan las dos rectas",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Verificar si una combinación cumple un sistema de desigualdades",
                "prompt": "Tenés el sistema: x + y ≤ 10 (horas disponibles)  y  20x + 15y ≥ 170 (meta mínima de dinero). ¿Cuál par (x, y) cumple AMBAS?",
                "answer": "(6, 4): suma 6 + 4 = 10 ≤ 10 (cumple horas) y gana 20(6) + 15(4) = 120 + 60 = 180 ≥ 170 (cumple meta).",
                "hints": ["Chequeá suma ≤ 10 y 20x + 15y ≥ 170 en cada opción."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(5, 3)", "(6, 4)", "(8, 4)"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Restricción de tiempo y presupuesto",
                "prompt": "En un taller hacés piezas chicas (x, 2 h c/u) y grandes (y, 5 h c/u) con tope de 30 horas: 2x + 5y ≤ 30. Si ya decidiste hacer y = 4 grandes, ¿cuántas chicas (x) podés hacer como MÁXIMO? Respondé solo con el número.",
                "answer": "5 piezas chicas: 2x + 5(4) ≤ 30 → 2x + 20 ≤ 30 → 2x ≤ 10 → x ≤ 5.",
                "hints": ["Reemplazá y = 4 y despejá x."],
                "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Un punto sobre una recta punteada",
                "prompt": "El punto (2, 5) cae EXACTAMENTE sobre la recta frontera punteada de y > 2x + 1. ¿Es solución de la desigualdad?",
                "answer": "No: 5 > 2(2) + 1 da 5 > 5, que es falso. Una línea punteada excluye a todos los puntos sobre ella.",
                "hints": ["Evaluá 5 > 5: ¿es verdadero o falso?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "No, porque '>' es estricto y 5 > 5 es falso",
                            "Sí, todos los puntos de la frontera son solución",
                            "Depende de qué lado esté sombreado",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 12: FUNCIONES PROFUNDAS, SUCESIONES Y TRAMOS ====================
    {
        "slug": "al-dominio-rango",
        "title": "33. Dominio, rango, tasa de cambio e interpretación de gráficas",
        "level": 12,
        "order_index": 33,
        "summary": "Entradas válidas (dominio), salidas posibles (rango), máximos/mínimos y tasa promedio de cambio en curvas reales.",
        "prerequisites": ["p-funciones"],
        "metadata": {"section": "Álgebra 1", "lab_tab": "linear_fn", "est_minutes": 18},
        "items": [
            {
                "item_type": "recall",
                "title": "Dominio vs. Rango en una situación real",
                "prompt": "Vendés entre 0 y 50 entradas de un show a $10 cada una (ingresos de $0 a $500). ¿Cuál es el DOMINIO y cuál es el RANGO?",
                "answer": "Dominio = entradas válidas (enteros de 0 a 50). Rango = salidas posibles (ingresos de $0 a $500, múltiplos de 10).",
                "hints": ["Dominio = eje X (entradas); Rango = eje Y (salidas)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Dominio: 0 a 50 entradas; Rango: $0 a $500",
                            "Dominio: $0 a $500; Rango: 0 a 50 entradas",
                            "Dominio y rango son todos los números reales incluidos negativos",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Restricciones algebraicas de dominio (dividir por cero y raíz negativa)",
                "prompt": "¿Qué valor de x está PROHIBIDO en el dominio de f(x) = 10 / (x − 4)?",
                "answer": "x = 4, porque hace cero el denominador (10 ÷ 0 es indefinido). El dominio son todos los reales excepto 4.",
                "hints": ["¿Qué valor de x convierte (x − 4) en 0?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["x = 0", "x = 4", "x = −4", "Ninguno"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Tasa promedio de cambio en una curva (crecimiento de usuarios)",
                "prompt": "Una app tiene f(1) = 20 usuarios en el mes 1 y f(5) = 100 usuarios en el mes 5. ¿Cuál fue su tasa promedio de cambio entre el mes 1 y el 5 ([f(5)−f(1)] / [5−1])? Respondé solo con el número.",
                "answer": "20 usuarios/mes: (100 − 20) / (5 − 1) = 80 / 4 = 20. Es la pendiente de la recta que une esos dos puntos.",
                "hints": ["(Salida final − Salida inicial) dividido (Entrada final − Entrada inicial)."],
                "payload": {"check": {"type": "numeric", "value": 20, "tolerance": 0.01, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Leer intervalos crecientes, decrecientes y máximo en una curva",
                "prompt": "La altura de una pelota lanzada hacia arriba sube de t = 0 s hasta t = 2 s (llega a 20 m) y luego baja hasta t = 4 s. ¿En qué intervalo es CRECIENTE la función?",
                "answer": "Entre t = 0 y t = 2 s (mientras la curva sube de izquierda a derecha); en t = 2 s alcanza su máximo de 20 m y de 2 a 4 s es decreciente.",
                "hints": ["Los intervalos crecientes/decrecientes se expresan siempre usando valores del eje X (tiempo)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "De t = 0 s a t = 2 s",
                            "De t = 2 s a t = 4 s",
                            "De 0 m a 20 m",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Tasa promedio de cambio en un viaje con paradas",
                "prompt": "A las 2 h de viaje llevabas 110 km y a las 5 h llevabas 320 km. ¿Cuál fue tu velocidad promedio en ese tramo? Respondé solo con el número en km/h.",
                "answer": "70 km/h: (320 − 110) / (5 − 2) = 210 / 3 = 70 km/h.",
                "hints": ["Dividí los km avanzados (210) por las horas transcurridas (3)."],
                "payload": {"check": {"type": "numeric", "value": 70, "tolerance": 0.01, "unit": "km/h"}},
            },
            {
                "item_type": "recall",
                "title": "Dominio de una raíz cuadrada real √(x − 3)",
                "prompt": "Si trabajás con números reales, ¿cuál es el dominio de g(x) = √(x − 3)?",
                "answer": "x ≥ 3: lo de adentro de la raíz cuadrada no puede ser negativo (x − 3 ≥ 0 → x ≥ 3).",
                "hints": ["¿Qué valores de x hacen que (x − 3) sea mayor o igual a 0?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["x ≥ 3", "x > 0", "Todos los reales"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "al-sucesiones",
        "title": "34. Sucesiones aritméticas y geométricas",
        "level": 12,
        "order_index": 34,
        "summary": "Patrones que suman (aritméticas) vs. que multiplican (geométricas), fórmulas explícitas para saltar al término 100 y recursivas.",
        "prerequisites": ["p-funciones"],
        "metadata": {"section": "Álgebra 1", "lab_tab": "exponentials", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Fórmula explícita de una sucesión aritmética (saltar al mes 10)",
                "prompt": "Ahorrás $100 el mes 1 y cada mes sumás $25 más que el anterior: 100, 125, 150… Usando a_n = 100 + (n − 1)·25, ¿cuánto ahorrás en el mes n = 10? Respondé solo con el número.",
                "answer": "$325: 100 + 9 × 25 = 100 + 225 = 325. (Atención: del mes 1 al 10 hay 9 saltos, no 10!).",
                "hints": ["Reemplazá n = 10: son 9 saltos de +25 desde 100."],
                "payload": {"check": {"type": "numeric", "value": 325, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Fórmula explícita de una sucesión geométrica (triplicación)",
                "prompt": "Un video empieza con 5 vistas el día 1 y cada día se triplica: 5, 15, 45… Usando a_n = 5 · 3^(n − 1), ¿cuántas vistas tiene el día n = 4? Respondé solo con el número.",
                "answer": "135 vistas: 5 × 3³ = 5 × 27 = 135 (5 → 15 → 45 → 135).",
                "hints": ["Son 3 multiplicaciones por 3: 5 × 27."],
                "payload": {
                    "lab_link": "math:exponentials",
                    "check": {"type": "numeric", "value": 135, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Distinguir sucesión aritmética vs. geométrica",
                "prompt": "Sucesión A: 4, 10, 16, 22…  Sucesión B: 4, 12, 36, 108… ¿Cuál es cuál?",
                "answer": "A es aritmética (suma constante d = +6, equivale a una función lineal). B es geométrica (multiplica por razón constante r = 3, equivale a una función exponencial).",
                "hints": ["Aritmética = suma/resta fija; Geométrica = multiplica/divide fijo."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "A es aritmética (+6) y B es geométrica (×3)",
                            "A es geométrica y B es aritmética",
                            "Las dos son aritméticas",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Fórmula recursiva vs. fórmula explícita",
                "prompt": "¿Qué ventaja tiene una fórmula EXPLÍCITA (como a_n = 5 + 3(n−1)) frente a una RECURSIVA (a_n = a_(n−1) + 3)?",
                "answer": "La explícita permite calcular directamente el término 100 en una sola cuenta; la recursiva te obliga a calcular los 99 anteriores paso a paso.",
                "hints": ["Imaginá querer hallar a_100 con cada una."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "La explícita calcula cualquier término n directo sin pasar por todos los anteriores",
                            "La recursiva sirve solo para números negativos",
                            "Son dos nombres para la misma fórmula",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Sucesión geométrica decreciente (rebote de una pelota)",
                "prompt": "Una pelota cae desde 80 cm y en cada rebote llega a la mitad de la altura anterior (r = 0.5): 80, 40, 20… ¿Qué altura alcanza en el 4º valor (3er rebote)? Respondé solo con el número en cm.",
                "answer": "10 cm: 80 → 40 → 20 → 10 cm (80 × 0.5³ = 10).",
                "hints": ["Dividí por 2 tres veces desde 80."],
                "payload": {"check": {"type": "numeric", "value": 10, "tolerance": 0.01, "unit": "cm"}},
            },
            {
                "item_type": "worked_example",
                "title": "Usar una fórmula recursiva",
                "prompt": "Dada la regla recursiva a₁ = 7 y a_n = a_(n−1) − 2, ¿cuánto vale a₄? Respondé solo con el número.",
                "answer": "1: a₁ = 7 → a₂ = 5 → a₃ = 3 → a₄ = 1.",
                "hints": ["Restá 2 tres veces empezando en 7."],
                "payload": {"check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    {
        "slug": "al-valor-absoluto-partes",
        "title": "35. Valor absoluto y funciones definidas por partes",
        "level": 12,
        "order_index": 35,
        "summary": "Ecuaciones |x − a| = d (tolerancias reales), gráfica en 'V' y funciones por tramos (envíos por peso, impuestos).",
        "prerequisites": ["p-funciones", "al-dominio-rango"],
        "metadata": {"section": "Álgebra 1", "lab_tab": "linear_fn", "est_minutes": 18},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Ecuación con valor absoluto (tolerancia de una pieza)",
                "prompt": "Un tornillo de 10 mm admite un error máximo de ±0.5 mm: las medidas aceptadas cumplen |x − 10| ≤ 0.5 y los extremos salen de |x − 10| = 0.5. ¿Cuál es la medida MÁXIMA aceptada (la solución mayor)? Respondé solo con el número en mm.",
                "answer": "10.5 mm (y la mínima es 9.5 mm): la distancia al 10 es 0.5 hacia arriba o hacia abajo.",
                "hints": ["x − 10 puede ser +0.5 o −0.5."],
                "payload": {"check": {"type": "numeric", "value": 10.5, "tolerance": 0.01, "unit": "mm"}},
            },
            {
                "item_type": "recall",
                "title": "Por qué |x − 3| = −4 no tiene solución",
                "prompt": "¿Cuántas soluciones reales tiene la ecuación |x − 3| = −4?",
                "answer": "Ninguna (0): el valor absoluto mide distancia y JAMÁS puede ser negativo.",
                "hints": ["¿Puede una distancia ser igual a −4?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Ninguna, porque un valor absoluto nunca puede ser negativo",
                            "Dos soluciones: x = −1 y x = 7",
                            "Una solución: x = −1",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Vértice de una gráfica en 'V' f(x) = |x − h| + k",
                "prompt": "¿Dónde está el vértice (punta inferior) de f(x) = |x − 3| + 2?",
                "answer": "En (3, 2): la expresión adentro del valor absoluto se hace 0 cuando x = 3 (ese es el punto más bajo), dando y = 0 + 2 = 2.",
                "hints": ["¿Qué valor de x hace que |x − 3| sea 0?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(3, 2)", "(−3, 2)", "(2, 3)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Evaluar una función por tramos (tarifa de correo)",
                "prompt": "Un correo cobra según el peso x: si x ≤ 2 kg cobra $500; si x > 2 kg cobra 500 + 200(x − 2). ¿Cuánto cuesta enviar un paquete de x = 5 kg? Respondé solo con el número.",
                "answer": "$1100: como 5 > 2 usás la segunda regla → 500 + 200(5 − 2) = 500 + 600 = 1100.",
                "hints": ["Primero fijate en qué tramo cae x = 5, después reemplazá."],
                "payload": {"check": {"type": "numeric", "value": 1100, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Las dos soluciones de |2x − 4| = 6",
                "prompt": "Resolvé |2x − 4| = 6 (separando en 2x − 4 = 6 y 2x − 4 = −6). ¿Cuánto vale la solución NEGATIVA? Incluí el signo.",
                "answer": "−1 (la positiva es 5): 2x − 4 = −6 → 2x = −2 → x = −1.",
                "hints": ["Resolvé el caso 2x − 4 = −6."],
                "payload": {"check": {"type": "numeric", "value": -1, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Ejemplos reales de funciones definidas por partes",
                "prompt": "¿Cuál de estas situaciones cotidianas se modela con una función por partes (distintas reglas según el tramo)?",
                "answer": "Un estacionamiento que cobra $1000 la primera hora y $600 por cada hora adicional (o tramos de impuestos / horas extras laborales).",
                "hints": ["Buscá una regla que cambie de fórmula a partir de cierto umbral."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Estacionamiento con tarifa fija la 1ª hora y otra tarifa por hora extra",
                            "Un kilo de pan siempre al mismo precio por kilo",
                            "La circunferencia de un círculo 2πr",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 13: RADICALES Y EXPONENCIALES ====================
    {
        "slug": "al-exponentes-radicales",
        "title": "36. Exponentes fraccionarios y simplificación de radicales",
        "level": 13,
        "order_index": 36,
        "summary": "Conectar raíces con potencias fraccionarias (x^(1/2) = √x) y simplificar raíces sacando cuadrados perfectos (√72 = 6√2).",
        "prerequisites": ["p-raices-notacion"],
        "metadata": {"section": "Álgebra 1", "lab_tab": "powers", "est_minutes": 18},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Exponente 1/2 equivale a raíz cuadrada",
                "prompt": "¿Cuánto vale 49^(1/2)? Respondé solo con el número.",
                "answer": "7: porque 49^(1/2) = √49 = 7 (al elevarlo al cuadrado: (49^(1/2))² = 49¹ = 49).",
                "hints": ["El denominador del exponente es el índice de la raíz."],
                "payload": {
                    "lab_link": "math:powers",
                    "check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Exponente fraccionario compuesto a^(m/n)",
                "prompt": "Calculá 8^(2/3) (tip: sacá primero la raíz cúbica ∛8 y después elevalo al cuadrado). Respondé solo con el número.",
                "answer": "4: ∛8 = 2, y 2² = 4. Sacar la raíz primero mantiene los números chiquitos.",
                "hints": ["Denominador 3 = raíz cúbica (∛8 = 2); numerador 2 = elevar al cuadrado."],
                "payload": {
                    "lab_link": "math:powers",
                    "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Simplificar una raíz sacando el mayor cuadrado perfecto",
                "prompt": "¿Cómo queda simplificada √72 al máximo (pista: 72 = 36 × 2)?",
                "answer": "6√2: √(36 · 2) = √36 · √2 = 6√2 (3√8 vale lo mismo, pero no está simplificada al máximo porque 8 = 4 · 2).",
                "hints": ["Buscá el cuadrado perfecto más grande que divide a 72 (36)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["6√2", "36√2", "3√8"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Trampa clásica con raíces de una suma",
                "prompt": "¿Es cierto que √(9 + 16) es igual a √9 + √16 (= 3 + 4 = 7)?",
                "answer": "NO: √(9 + 16) = √25 = 5 (≠ 7). Las raíces se reparten en MULTIPLICACIÓN y DIVISIÓN, ¡nunca en suma o resta!",
                "hints": ["Calculá primero 9 + 16 = 25 y sacale la raíz."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Falso: √(9 + 16) = √25 = 5 (la raíz NO se reparte en sumas)",
                            "Verdadero: da 7",
                            "Solo es verdadero cuando los dos números son positivos",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Multiplicar dos raíces √2 · √8",
                "prompt": "Usando √a · √b = √(a·b), ¿cuánto vale √2 · √8? Respondé solo con el número.",
                "answer": "4: √(2 × 8) = √16 = 4.",
                "hints": ["Juntá ambos adentro de la misma raíz: √16."],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Raíz cúbica con exponente fraccionario",
                "prompt": "¿Cuánto vale 64^(1/3) (raíz cúbica de 64)? Respondé solo con el número.",
                "answer": "4 (porque 4 × 4 × 4 = 64).",
                "hints": ["¿Qué número al cubo da 64?"],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    {
        "slug": "al-exponenciales",
        "title": "37. Crecimiento y decaimiento exponencial (y = a · bˣ)",
        "level": 13,
        "order_index": 37,
        "summary": "Interés compuesto, depreciación de un auto, vida media de medicamentos y por qué lo exponencial supera a lo lineal.",
        "prerequisites": ["al-sucesiones", "al-exponentes-radicales"],
        "metadata": {"section": "Álgebra 1", "lab_tab": "exponentials", "est_minutes": 20},
        "items": [
            {
                "item_type": "recall",
                "title": "Crecimiento vs. Decaimiento en y = a · bˣ",
                "prompt": "El valor de un auto tras t años se modela como V(t) = 20 000 · (0.85)^t. ¿Qué significan 20 000 y 0.85?",
                "answer": "$20 000 es el valor inicial (t = 0); 0.85 significa que conserva el 85% cada año, es decir PIERDE (depreciación) un 15% anual.",
                "hints": ["b > 1 crece; 0 < b < 1 decrece (1 − 0.85 = 0.15 = 15%)."],
                "payload": {
                    "lab_link": "math:exponentials",
                    "check": {
                        "type": "choice",
                        "options": [
                            "Arranca en $20 000 y pierde un 15% de su valor cada año",
                            "Arranca en $20 000 y pierde un 85% cada año",
                            "Arranca en $20 000 y baja $850 fijos por año",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Interés compuesto en una inversión",
                "prompt": "Invertís $1000 al 10% anual compuesto: A(t) = 1000 · (1.10)^t. ¿Cuánto tenés después de t = 2 años? Respondé solo con el número.",
                "answer": "$1210: 1000 × 1.10 × 1.10 = 1000 × 1.21 = $1210 ($10 más que con interés simple, porque el 2º año ganás interés sobre el interés del 1º).",
                "hints": ["1.10² = 1.21."],
                "payload": {
                    "lab_link": "math:exponentials",
                    "check": {"type": "numeric", "value": 1210, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Decaimiento exponencial: cafeína en sangre (vida media)",
                "prompt": "Un café tiene 160 mg de cafeína y tu cuerpo elimina la mitad cada 5 horas: C(n) = 160 · (0.5)^n. ¿Cuántos mg quedan después de 15 horas (n = 3 períodos)? Respondé solo con el número en mg.",
                "answer": "20 mg: 160 → 80 (5 h) → 40 (10 h) → 20 mg (15 h).",
                "hints": ["15 h son 3 períodos de 5 h: dividí 160 por 2 tres veces."],
                "payload": {
                    "lab_link": "math:exponentials",
                    "check": {"type": "numeric", "value": 20, "tolerance": 0.01, "unit": "mg"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Duplicación exponencial (cultivo o viralidad)",
                "prompt": "Una población empieza con 50 y se duplica cada día: P(t) = 50 · 2^t. ¿Cuánto vale a los t = 5 días? Respondé solo con el número.",
                "answer": "1600 (50 × 2⁵ = 50 × 32 = 1600).",
                "hints": ["2⁵ = 32; multiplicá 50 × 32."],
                "payload": {
                    "lab_link": "math:exponentials",
                    "check": {"type": "numeric", "value": 1600, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Lineal vs. Exponencial a largo plazo",
                "prompt": "Opción A: recibir $1000 fijos por día. Opción B: empezar con $1 el día 1 y duplicar cada día ($1, $2, $4, $8…). Al cabo de 30 días, ¿cuál rinde más?",
                "answer": "La Opción B por paliza: en 30 días la A da $30 000, mientras la B supera los $500 millones. Todo crecimiento exponencial termina superando a cualquier crecimiento lineal.",
                "hints": ["2²⁹ es más de 500 millones."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Opción B (duplicar): supera por millones a la opción lineal",
                            "Opción A ($1000/día): porque $1 es demasiado poco para alcanzarla",
                            "Terminan casi empatadas el día 30",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Factor de crecimiento para un aumento del 8%",
                "prompt": "Si una población crece un 8% cada año, ¿cuál es la base b en la fórmula y = a · b^t? Respondé en decimal.",
                "answer": "1.08 (1 + 0.08 = 1.08).",
                "hints": ["100% + 8% pasado a decimal."],
                "payload": {"check": {"type": "numeric", "value": 1.08, "tolerance": 0.002, "unit": ""}},
            },
        ],
    },
    # ==================== NIVEL 14: CUADRÁTICAS E IRRACIONALES ====================
    {
        "slug": "al-polinomios-binomios",
        "title": "38. Multiplicar binomios y productos notables",
        "level": 14,
        "order_index": 38,
        "summary": "Expandir (x+a)(x+b) con modelo de área, evitar la trampa de (x+a)² y aprovechar la diferencia de cuadrados (a+b)(a−b).",
        "prerequisites": ["p-variables-expresiones"],
        "metadata": {"section": "Álgebra 1", "lab_tab": "factoring", "est_minutes": 20},
        "items": [
            {
                "item_type": "recall",
                "title": "Expandir dos binomios (modelo de área / todos con todos)",
                "prompt": "¿Cuál es la forma expandida de (x + 3)(x + 5)?",
                "answer": "x² + 8x + 15: x·x = x², los términos cruzados suman 3x + 5x = 8x, y 3·5 = 15.",
                "hints": ["Multiplicá cada término del primero por cada término del segundo y sumá los del medio."],
                "payload": {
                    "lab_link": "math:factoring",
                    "check": {
                        "type": "choice",
                        "options": ["x² + 8x + 15", "x² + 15", "x² + 15x + 8"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "La trampa #1 de Álgebra: (x + 4)² NO es x² + 16",
                "prompt": "¿Cuál es el resultado correcto de (x + 4)²?",
                "answer": "x² + 8x + 16: (x + 4)² significa (x + 4)(x + 4) = x² + 4x + 4x + 16. Nunca te olvides el término doble del medio (2ab)!",
                "hints": ["Escribilo como (x + 4)(x + 4) y probá con x = 1: (1+4)² = 25, no 1²+16 = 17."],
                "payload": {
                    "lab_link": "math:factoring",
                    "check": {
                        "type": "choice",
                        "options": ["x² + 16", "x² + 8x + 16", "x² + 4x + 16"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Diferencia de cuadrados: (x + 6)(x − 6)",
                "prompt": "¿Qué queda al multiplicar (x + 6)(x − 6)?",
                "answer": "x² − 36: los términos del medio (+6x y −6x) se cancelan exactamente, dejando a² − b².",
                "hints": ["+6x − 6x = 0."],
                "payload": {
                    "lab_link": "math:factoring",
                    "check": {
                        "type": "choice",
                        "options": ["x² − 36", "x² + 36", "x² − 12x − 36"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Cálculo mental relámpago con diferencia de cuadrados",
                "prompt": "Usando (a − b)(a + b) = a² − b², calculá 49 × 51 pensándolo como (50 − 1)(50 + 1) = 50² − 1². Respondé solo con el número.",
                "answer": "2499 (2500 − 1 = 2499). La diferencia de cuadrados convierte multiplicaciones feas en una resta de 1 segundo.",
                "hints": ["50² = 2500, menos 1²."],
                "payload": {"check": {"type": "numeric", "value": 2499, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Binomio con signos distintos: (x + 7)(x − 2)",
                "prompt": "Expandí (x + 7)(x − 2).",
                "answer": "x² + 5x − 14: los del medio dan 7x − 2x = +5x, y 7 · (−2) = −14.",
                "hints": ["Sumá +7 y −2 para el coeficiente de x; multiplicalos para el término independiente."],
                "payload": {
                    "lab_link": "math:factoring",
                    "check": {
                        "type": "choice",
                        "options": ["x² + 5x − 14", "x² − 5x − 14", "x² + 9x − 14"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Agrandar un jardín rectangular (área algebraica)",
                "prompt": "Un terreno cuadrado de lado x se agranda 2 m de largo y 3 m de ancho: área = (x + 2)(x + 3) = x² + 5x + 6. Si x = 4 m, ¿cuántos m² tiene el terreno agrandado? Respondé solo con el número.",
                "answer": "42 m² (6 × 7 = 42, o 4² + 5·4 + 6 = 16 + 20 + 6 = 42).",
                "hints": ["(4 + 2) × (4 + 3)."],
                "payload": {"check": {"type": "numeric", "value": 42, "tolerance": 0, "unit": "m²"}},
            },
        ],
    },
    {
        "slug": "al-factorizar-cuadraticas",
        "title": "39. Factorizar cuadráticas y propiedad del producto cero",
        "level": 14,
        "order_index": 39,
        "summary": "El camino inverso: reescribir x² + bx + c como (x + p)(x + q) para resolver ecuaciones cuadráticas en segundos.",
        "prerequisites": ["al-polinomios-binomios"],
        "metadata": {"section": "Álgebra 1", "lab_tab": "factoring", "est_minutes": 20},
        "items": [
            {
                "item_type": "recall",
                "title": "Factorizar x² + 7x + 12 (suma 7, producto 12)",
                "prompt": "¿Cuál es la factorización correcta de x² + 7x + 12?",
                "answer": "(x + 3)(x + 4): porque 3 + 4 = 7 y 3 × 4 = 12.",
                "hints": ["Buscá dos números que multiplicados den 12 y sumados den 7."],
                "payload": {
                    "lab_link": "math:factoring",
                    "check": {
                        "type": "choice",
                        "options": ["(x + 3)(x + 4)", "(x + 2)(x + 6)", "(x + 1)(x + 12)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Propiedad del producto cero: (x − 3)(x + 5) = 0",
                "prompt": "Si (x − 3)(x + 5) = 0, ¿cuáles son las dos soluciones de x?",
                "answer": "x = 3  y  x = −5: para que un producto dé 0, al menos uno de los dos paréntesis debe valer 0 (x − 3 = 0 → x = 3; x + 5 = 0 → x = −5).",
                "hints": ["Igualá cada paréntesis a cero por separado."],
                "payload": {
                    "lab_link": "math:factoring",
                    "check": {
                        "type": "choice",
                        "options": ["x = 3 y x = −5", "x = −3 y x = 5", "x = 0 y x = −15"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Resolver x² − 5x + 6 = 0 factorizando",
                "prompt": "Factorizá x² − 5x + 6 = 0 (dos números que multipliquen +6 y sumen −5) y encontrá la solución MAYOR. Respondé solo con el número.",
                "answer": "3 (las dos soluciones son x = 2 y x = 3, porque (x − 2)(x − 3) = 0).",
                "hints": ["(−2) × (−3) = +6 y (−2) + (−3) = −5."],
                "payload": {
                    "lab_link": "math:factoring",
                    "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Factorizar una diferencia de cuadrados: x² − 49",
                "prompt": "¿Cómo se factoriza x² − 49?",
                "answer": "(x + 7)(x − 7): siempre que veas un cuadrado menos otro cuadrado (a² − b²), se parte directo en suma por diferencia.",
                "hints": ["49 = 7²."],
                "payload": {
                    "lab_link": "math:factoring",
                    "check": {
                        "type": "choice",
                        "options": ["(x + 7)(x − 7)", "(x − 7)²", "(x − 49)(x + 1)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Factor común antes de resolver: 2x² − 10x = 0",
                "prompt": "Sacando factor común 2x en 2x² − 10x = 0 queda 2x(x − 5) = 0. Además de x = 0, ¿cuál es la otra solución? Respondé solo con el número.",
                "answer": "5: si x − 5 = 0, entonces x = 5. (¡Nunca dividas por x al despejar porque perderías la solución x = 0!).",
                "hints": ["Igualá (x − 5) = 0."],
                "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Orden para resolver una ecuación cuadrática factorizando",
                "prompt": "Ordená los pasos correctos para resolver x² + 2x = 15 por factorización.",
                "answer": "1) Pasar todo a un lado para igualar a 0 (x² + 2x − 15 = 0) → 2) Factorizar ((x+5)(x−3) = 0) → 3) Igualar cada factor a 0 → 4) Verificar las dos soluciones.",
                "hints": ["La propiedad del producto cero SOLO funciona cuando el otro lado es 0."],
                "payload": {
                    "lab_link": "math:factoring",
                    "check": {
                        "type": "order",
                        "lines": [
                            "Pasar todos los términos a un lado para igualar a cero",
                            "Factorizar el trinomio en dos paréntesis (x + p)(x + q) = 0",
                            "Igualar cada paréntesis a cero para despejar las dos soluciones",
                            "Comprobar ambas soluciones en la ecuación original",
                        ],
                    },
                },
            },
        ],
    },
    {
        "slug": "al-parabolas-formula",
        "title": "40. Parábolas, vértice y fórmula cuadrática",
        "level": 14,
        "order_index": 40,
        "summary": "Hallar máximos y mínimos con el vértice x = −b/(2a), la fórmula general que resuelve cualquier cuadrática y el discriminante.",
        "prerequisites": ["al-factorizar-cuadraticas"],
        "metadata": {"section": "Álgebra 1", "lab_tab": "quadratics", "est_minutes": 22},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Altura máxima de una pelota (vértice de la parábola)",
                "prompt": "La altura de una pelota lanzada hacia arriba es h(t) = −5t² + 20t + 2. Usando el vértice t = −b / (2a), ¿en qué segundo t alcanza su altura MÁXIMA? Respondé solo con el número en s.",
                "answer": "2 s: t = −20 / (2 · (−5)) = −20 / (−10) = 2 s (y la altura máxima es h(2) = −20 + 40 + 2 = 22 m).",
                "hints": ["Aquí a = −5 y b = 20; calculá −b / (2a)."],
                "payload": {
                    "lab_link": "math:quadratics",
                    "check": {"type": "numeric", "value": 2, "tolerance": 0.01, "unit": "s"},
                },
            },
            {
                "item_type": "recall",
                "title": "Forma canónica (vértice visible): y = a(x − h)² + k",
                "prompt": "La parábola y = −2(x − 3)² + 10 abre hacia abajo (porque a = −2 < 0). ¿Cuál es su punto máximo (vértice)?",
                "answer": "(3, 10): el cuadrado nunca es negativo, así que −2(x−3)² es como máximo 0 cuando x = 3, dejando y = 10.",
                "hints": ["Leé (h, k) directamente de a(x − h)² + k."],
                "payload": {
                    "lab_link": "math:quadratics",
                    "check": {
                        "type": "choice",
                        "options": ["(3, 10)", "(−3, 10)", "(−2, 10)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Calcular el discriminante Δ = b² − 4ac",
                "prompt": "En la ecuación x² − 6x + 9 = 0 (a = 1, b = −6, c = 9), ¿cuánto vale el discriminante Δ = b² − 4ac? Respondé solo con el número.",
                "answer": "0: (−6)² − 4(1)(9) = 36 − 36 = 0. Cuando Δ = 0 la parábola apenas toca el eje X en una única solución doble (x = 3).",
                "hints": ["(−6)² = +36; restale 4 × 1 × 9."],
                "payload": {
                    "lab_link": "math:quadratics",
                    "check": {"type": "numeric", "value": 0, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Qué predice el signo del discriminante b² − 4ac",
                "prompt": "Calculás el discriminante Δ = b² − 4ac de una cuadrática y te da un número NEGATIVO (ej. −12). ¿Cuántas soluciones REALES tiene la ecuación?",
                "answer": "Ninguna solución real (0): dentro de la fórmula general aparece √Δ, y no existe raíz cuadrada real de un número negativo (la parábola nunca cruza el eje X).",
                "hints": ["Recordá que el discriminante va adentro de la raíz √(b² − 4ac)."],
                "payload": {
                    "lab_link": "math:quadratics",
                    "check": {
                        "type": "choice",
                        "options": [
                            "Ninguna solución real (la parábola no cruza el eje X)",
                            "Exactamente una solución real",
                            "Dos soluciones negativas",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Resolver con la fórmula cuadrática",
                "prompt": "Usá x = (−b ± √(b² − 4ac)) / (2a) para 2x² − 5x − 3 = 0 (a=2, b=−5, c=−3; √49 = 7). ¿Cuánto vale la solución POSITIVA? Respondé solo con el número.",
                "answer": "3 (la otra es −0.5): x = (5 + 7) / 4 = 12 / 4 = 3.",
                "hints": ["(5 + 7) dividido (2 × 2)."],
                "payload": {
                    "lab_link": "math:quadratics",
                    "check": {"type": "numeric", "value": 3, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Hacia dónde abre una parábola y = ax² + bx + c",
                "prompt": "¿Cómo sabés en 1 segundo si y = ax² + bx + c tiene forma de 'U' (tiene mínimo) o de '∩' (tiene máximo)?",
                "answer": "Por el signo de a: si a > 0 abre hacia arriba (∪, tiene mínimo); si a < 0 abre hacia abajo (∩, tiene máximo, como una pelota en el aire).",
                "hints": ["Mirá el signo del coeficiente que acompaña a x²."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Si a > 0 abre hacia arriba (mínimo); si a < 0 abre hacia abajo (máximo)",
                            "Depende del signo del término independiente c",
                            "Siempre abre hacia arriba porque x² es positivo",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "al-irracionales",
        "title": "41. Números racionales vs. irracionales",
        "level": 14,
        "order_index": 41,
        "summary": "Qué hace irracional a √2 y π, decimales periódicos vs. infinitos sin patrón y reglas al combinarlos.",
        "prerequisites": ["al-exponentes-radicales"],
        "metadata": {"section": "Álgebra 1", "lab_tab": "powers", "est_minutes": 15},
        "items": [
            {
                "item_type": "recall",
                "title": "Identificar un número irracional",
                "prompt": "¿Cuál de estos números es IRRACIONAL (imposible de escribir como fracción exacta de dos enteros)?",
                "answer": "√5 es irracional (decimal infinito sin patrón). −7 = −7/1, 0.333… = 1/3 y √16 = 4 son todos RACIONALES.",
                "hints": ["Cuidado con √16: tiene raíz exacta (= 4), así que SÍ es racional."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["−7", "0.3333… (= 1/3)", "√16", "√5"],
                        "correct": 3,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Decimales periódicos: ¿racionales o irracionales?",
                "prompt": "El número 0.66666… tiene infinitos decimales. ¿Es racional o irracional?",
                "answer": "Es RACIONAL: porque los decimales repiten un patrón periódico y se escribe exactamente como la fracción 2/3. Solo los decimales infinitos SIN patrón (como π o √2) son irracionales.",
                "hints": ["¿Se puede escribir como fracción de dos enteros?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Racional, porque es periódico y equivale exactamente a 2/3",
                            "Irracional, porque sus decimales nunca terminan",
                            "No es un número real",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Sumar un racional con un irracional",
                "prompt": "Si sumás 3 (racional) + √2 (irracional), ¿el resultado 3 + √2 es racional o irracional?",
                "answer": "Siempre IRRACIONAL: sumarle un número exacto jamás puede 'arreglar' los decimales infinitos sin patrón de √2.",
                "hints": ["3 + 1.4142135… = 4.4142135… sigue sin patrón."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Siempre irracional",
                            "Siempre racional",
                            "Racional solo si el número entero es par",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Multiplicar dos irracionales: ¿puede dar racional?",
                "prompt": "¿El producto de dos números irracionales da SIEMPRE irracional?",
                "answer": "NO siempre: por ejemplo √2 × √2 = 2 (racional!), o √2 × √8 = √16 = 4 (racional). En cambio racional (≠ 0) × irracional SÍ da siempre irracional.",
                "hints": ["Probá multiplicar √2 por sí mismo."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "No: a veces da racional (ej. √2 × √2 = 2)",
                            "Sí: irracional por irracional siempre da irracional",
                            "Siempre da racional",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Por qué π ≈ 3.14 es solo una aproximación",
                "prompt": "¿Por qué en los cálculos usamos π ≈ 3.14 o 22/7 en vez de escribir el valor exacto decimal de π?",
                "answer": "Porque π es irracional: sus decimales son infinitos y jamás se repiten en bloque, así que cualquier decimal finito o fracción es solo una aproximación práctica.",
                "hints": ["Ninguna fracción puede ser igual exactamente a un número irracional."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Porque π es irracional (decimales infinitos sin patrón) y no existe fracción exacta",
                            "Porque todavía no se descubrió si π termina en algún dígito",
                            "Porque 22/7 es exactamente igual a π",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Dónde aparece √2 en la vida real (hojas A4 y diagonales)",
                "prompt": "Un cuadrado de 1 m × 1 m tiene diagonal √2 ≈ 1.414 m. ¿Qué objeto cotidiano usa la proporción √2 para que al doblarlo por la mitad mantenga exactamente la misma forma?",
                "answer": "El papel estándar A4 (210 × 297 mm, 297 ÷ 210 ≈ 1.414 = √2): al cortar un A3 a la mitad sale un A4 con idénticas proporciones.",
                "hints": ["Pensá en las hojas de impresora."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Las hojas de papel A4 / A3 / A5 (relación largo/ancho = √2)",
                            "Las monedas redondas",
                            "Los relojes analógicos",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
]


ALGEBRA1_LESSONS: dict[str, dict] = {
    "al-ecuaciones-formulas": {
        "hook": {
            "question": "Si sabés que `d = v · t` o `A = b·h / 2`, ¿por qué memorizar tres fórmulas distintas cuando el álgebra te permite despejar cualquier letra en 2 pasos?",
            "intuition": "Despejar una **ecuación literal** usa las mismas reglas de la balanza que con números, solo que dejás las otras letras quietas. Además, aprenderás a reconocer ecuaciones tramposas (con `0` o `infinitas` soluciones) y a convertir tasas compuestas sin confundirte.",
        },
        "concept": {
            "points": [
                "**Los 3 resultados de una ecuación lineal**: (1) **1 solución** (`x = 8`); (2) **0 soluciones** si llegás a algo absurdo como `5 = 9`; (3) **infinitas soluciones** si ambos lados quedan idénticos como `5 = 5`.",
                "**Despejar fórmulas (ecuaciones literales)**: tratá todas las demás letras como si fueran números comunes y aplicá operaciones inversas hasta dejar sola la variable que buscás (`A = b·h/2` → `2A = b·h` → `h = 2A/b`).",
                "**Análisis dimensional (unidades que se cancelan)**: para convertir tasas compuestas (como `L/min` a `L/h` o `km/h` a `m/s`), multiplicá por fracciones equivalentes a `1` (`60 min / 1 h`) de modo que la unidad vieja se tache arriba y abajo.",
                "**Verificación por unidades**: si buscás un tiempo en segundos y las unidades de tu despeje te dan `m²/s`, sabés antes de meter números que despejaste mal.",
            ],
            "real_world": [
                {
                    "title": "Fórmulas de Física y Electrónica",
                    "detail": "De una sola Ley de Ohm (`V = I·R`) sacás al instante `I = V/R` y `R = V/I` sin memorizar triángulos.",
                },
                {
                    "title": "Recetas en °F → °C",
                    "detail": "Con `C = (5/9)(F − 32)` pasás cualquier temperatura de horno estadounidense (`350°F ≈ 177°C`) en segundos.",
                },
                {
                    "title": "Detectar pérdidas de agua o consumo eléctrico",
                    "detail": "Una canilla que pierde `0.25 L/min` pierde `0.25 × 60 = 15 L/h` (`360 L/día`).",
                },
            ],
            "key_rule": "`5 = 9` → 0 soluciones · `5 = 5` → infinitas · En fórmulas literales despejás igual que con números · Tachá unidades para convertir tasas.",
            "pitfall": "Creer que llegar a `0 = 0` significa 'la solución es `x = 0`': en realidad significa que sirve **cualquier número real** (infinitas soluciones).",
        },
        "example": {
            "title": "Despejá `F` en `C = (5/9)(F − 32)`",
            "steps": [
                "Multiplicamos ambos lados por `9/5` para cancelar el `5/9`: `(9/5)C = F − 32`.",
                "Sumamos `32` en ambos lados: **`F = (9/5)C + 32`**.",
                "Comprobamos con agua hirviendo (`C = 100°C`): `(9/5)(100) + 32 = 180 + 32 = 212°F`. ¡Exacto!",
            ],
            "lab_link": "math:linear_eq",
            "lab_cta": "Practicar despejes en el Laboratorio",
        },
        "check": {
            "question": "Al despejar `3(x + 2) = 3x + 10` llegás a `6 = 10`. ¿Qué significa?",
            "options": [
                {"text": "No tiene ninguna solución", "ok": True, "feedback": "Exacto: ningún valor de x puede convertir 6 en 10."},
                {"text": "Tiene infinitas soluciones", "ok": False, "feedback": "Infinitas soluciones sería si quedara 6 = 6."},
                {"text": "La solución es `x = 4`", "ok": False, "feedback": "Con x = 4 da 18 = 22 (falso)."},
            ],
        },
        "checks": [
            {
                "question": "Despejá el tiempo `t` en la fórmula de movimiento `d = v · t`.",
                "options": [
                    {"text": "`t = d / v`", "ok": True, "feedback": "Exacto: dividís ambos lados por v (y las unidades m ÷ (m/s) dan s!)."},
                    {"text": "`t = v / d`", "ok": False, "feedback": "Dividiste al revés; eso daría 1/s."},
                    {"text": "`t = d − v`", "ok": False, "feedback": "v estaba multiplicando a t, no sumando."},
                ],
            },
            {
                "question": "Una impresora 3D extruye `2 cm` de filamento por segundo. ¿Cuántos centímetros extruye en `1 minuto` (`× 60 s/min`)?",
                "options": [
                    {"text": "120 cm/min", "ok": True, "feedback": "Exacto: (2 cm/s) × (60 s/min) = 120 cm/min."},
                    {"text": "30 cm/min", "ok": False, "feedback": "Dividiste por 2 en vez de multiplicar por 60."},
                    {"text": "62 cm/min", "ok": False, "feedback": "Sumaste 60 + 2 en vez de multiplicar."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá la diferencia entre llegar a `4 = 4` y llegar a `4 = 9` al resolver una ecuación.",
    },
    "al-formas-lineales": {
        "hook": {
            "question": "Ya conocés `y = mx + b`, pero ¿para qué existen otras dos formas de escribir una recta (`Ax + By = C` y `y − y₁ = m(x − x₁)`)?",
            "intuition": "Cada forma es una herramienta hecha a medida: la **estándar** modela presupuestos con dos productos y da los cruces con los ejes en 2 segundos; la **punto-pendiente** te deja escribir la recta al instante cuando solo tenés un punto cualquiera y la inclinación.",
        },
        "concept": {
            "points": [
                "**Forma pendiente-ordenada (`y = mx + b`)**: ideal para graficar y leer tasa de cambio (`m`) e inicio (`b`).",
                "**Forma punto-pendiente (`y − y₁ = m(x − x₁)`)**: ideal si conocés la pendiente `m` y un punto `(x₁, y₁)` cualquiera sin tener que buscar `b` primero.",
                "**Forma estándar (`Ax + By = C`)**: ideal para presupuestos (`6x + 3y = 60`). Ponés `y = 0` para sacar el cruce con X (`10, 0`) y `x = 0` para el cruce con Y (`0, 20`).",
                "**Paralelas vs. Perpendiculares**: paralelas tienen **misma pendiente** (`m₂ = m₁`); perpendiculares (a 90°) tienen pendiente **opuesta e inversa** (`m₂ = −1/m₁`, así que `m₁ · m₂ = −1`).",
            ],
            "real_world": [
                {
                    "title": "Presupuesto con dos productos (`Ax + By = C`)",
                    "detail": "Con `$60`, cuadernos de `$6` y lapiceras de `$3` → `6x + 3y = 60`: o 10 cuadernos o 20 lapiceras o cualquier punto de la recta.",
                },
                {
                    "title": "Planos de calles o carpintería a 90°",
                    "detail": "Si una pared sigue pendiente `2/3`, una pared perpendicular exacta tiene pendiente `−3/2`.",
                },
                {
                    "title": "Proyectar ventas desde un dato del mes",
                    "detail": "Si el día 5 vendiste 40 y subís a ritmo de +6/día, `y − 40 = 6(x − 5)` te da el modelo en 1 segundo.",
                },
            ],
            "key_rule": "Estándar `Ax+By=C` → poné 0 para interceptos · Punto-pendiente `y−y₁=m(x−x₁)` · Perpendiculares: `m₂ = −1/m₁`.",
            "pitfall": "Olvidar cambiar el signo en perpendiculares (usar `+1/2` en vez de `−1/2` para perpendicular a `m = 2`).",
        },
        "example": {
            "title": "Armá una recta perpendicular a `y = 2x + 1` que pase por `(4, 5)`",
            "steps": [
                "La pendiente dada es `m₁ = 2`, así que la perpendicular es el opuesto inverso: `m₂ = −1/2`.",
                "Usamos forma punto-pendiente con `(4, 5)`: `y − 5 = −1/2 · (x − 4)`.",
                "Si la queremos en `y = mx + b`: distribuimos `y − 5 = −0.5x + 2` → **`y = −0.5x + 7`**.",
            ],
            "lab_link": "math:linear_fn",
            "lab_cta": "Comprobar pendientes en el Graficador",
        },
        "check": {
            "question": "En la recta en forma estándar `4x + 5y = 20`, ¿en qué punto corta al eje vertical `Y` (`x = 0`)?",
            "options": [
                {"text": "`(0, 4)`", "ok": True, "feedback": "Exacto: con x = 0 queda 5y = 20 → y = 4."},
                {"text": "`(0, 5)`", "ok": False, "feedback": "5 es el coeficiente de y; hay que dividir 20 ÷ 5 = 4."},
                {"text": "`(5, 0)`", "ok": False, "feedback": "(5, 0) es el cruce con el eje X (cuando y = 0)."},
            ],
        },
        "checks": [
            {
                "question": "¿Qué pendiente tiene una recta PERPENDICULAR a `y = −3x + 4`?",
                "options": [
                    {"text": "`1/3`", "ok": True, "feedback": "Exacto: invertís −3/1 a −1/3 y cambiás el signo a +1/3."},
                    {"text": "`−1/3`", "ok": False, "feedback": "Invertiste bien, pero faltó cambiar el signo de negativo a positivo."},
                    {"text": "`3`", "ok": False, "feedback": "Cambiaste el signo, pero faltó invertirlo (3 × (−3) = −9 ≠ −1)."},
                ],
            },
            {
                "question": "¿Cuál recta pasa por `(1, 5)` con pendiente `m = 2`?",
                "options": [
                    {"text": "`y − 5 = 2(x − 1)`", "ok": True, "feedback": "Exacto: forma punto-pendiente directa (equivale a y = 2x + 3)."},
                    {"text": "`y − 1 = 2(x − 5)`", "ok": False, "feedback": "Pusiste x₁ y y₁ al revés."},
                    {"text": "`y + 5 = 2(x + 1)`", "ok": False, "feedback": "Esa pasaría por (−1, −5)."},
                ],
            },
        ],
        "takeaway_prompt": "Resumí cuándo conviene usar cada una de las 3 formas de la recta y cómo sacás una pendiente perpendicular.",
    },
    "al-sistemas-desigualdades": {
        "hook": {
            "question": "Al planificar un viaje o un emprendimiento casi nunca tenés una sola condición: tenés **tope de plata** Y **tope de tiempo** a la vez. ¿Cómo se ven en un gráfico todas las combinaciones posibles?",
            "intuition": "Cada desigualdad pinta medio plano entero. Cuando ponés dos restricciones juntas, la **zona donde se cruzan los dos sombreados** muestra de un vistazo todas las opciones viables (la base de la optimización real).",
        },
        "concept": {
            "points": [
                "**Graficar una desigualdad 2D**: dibujás la recta frontera como si tuviera `=`. Si es `≤` o `≥`, va **sólida** (incluye el borde); si es `<` o `>`, va **punteada** (no incluye el borde).",
                "**Saber qué lado sombrear**: probá un **punto testigo** fácil (casi siempre `(0, 0)` si no está sobre la recta). Si cumple la desigualdad, pintás el lado de `(0, 0)`; si falla, pintás el otro lado.",
                "**Sistema de desigualdades**: graficás cada restricción en el mismo plano. Solo los puntos que caen en la **superposición de ambos sombreados** cumplen el sistema completo.",
                "**Esquinas óptimas**: en problemas reales de ganancias o costos con límites lineales, la mejor combinación suele estar en los vértices de esa región factible.",
            ],
            "real_world": [
                {
                    "title": "Organizar un presupuesto con dos límites",
                    "detail": "Tope de dinero (`5x + 10y ≤ 100`) y tope de espacio (`x + y ≤ 15`) definen la región de compras posibles.",
                },
                {
                    "title": "Planificar horas de estudio y descanso",
                    "detail": "Al menos 2 h de práctica (`x ≥ 2`) y no más de 10 h totales (`x + y ≤ 10`).",
                },
                {
                    "title": "Logística y programación lineal",
                    "detail": "Aerolíneas y fábricas usan sistemas de miles de desigualdades para decidir rutas y producción óptimas.",
                },
            ],
            "key_rule": "`≤, ≥` = línea sólida · `<, >` = punteada · Probá `(0, 0)` para sombrear · Solución del sistema = intersección de sombreados.",
            "pitfall": "Pensar que un punto sobre una recta **punteada** cuenta como solución, o sombrear hacia arriba solo por ver `>` sin haber despejado `y` primero (si `y` tiene signo menos adelante, al despejar se invierte!).",
        },
        "example": {
            "title": "Chequeá si un plan cumple dos restricciones",
            "steps": [
                "Restricción 1 (horas): `x + y ≤ 10`. Restricción 2 (ingresos): `20x + 15y ≥ 170`.",
                "Probamos `(6, 4)`: horas `6 + 4 = 10 ≤ 10` (cumple) e ingresos `120 + 60 = 180 ≥ 170` (cumple).",
                "Probamos `(5, 3)`: horas `8 ≤ 10` (cumple), pero ingresos `100 + 45 = 145` (NO llega a 170 → queda afuera).",
            ],
            "lab_link": "math:systems",
            "lab_cta": "Ver dos rectas en el Graficador dual",
        },
        "check": {
            "question": "¿Cuál de estos puntos es solución de `y ≤ 3x − 1`?",
            "options": [
                {"text": "`(2, 4)`", "ok": True, "feedback": "Exacto: 4 ≤ 3(2) − 1 → 4 ≤ 5 (verdadero)."},
                {"text": "`(0, 0)`", "ok": False, "feedback": "0 ≤ −1 es falso."},
                {"text": "`(1, 5)`", "ok": False, "feedback": "5 ≤ 2 es falso."},
            ],
        },
        "checks": [
            {
                "question": "Al graficar `x + y ≥ 6`, ¿cómo es la línea frontera y de qué lado está `(0, 0)`?",
                "options": [
                    {"text": "Línea sólida, y `(0, 0)` NO cumple (`0 ≥ 6` falso), así que se sombrea el lado opuesto", "ok": True, "feedback": "Exacto: incluye el borde y sombrea hacia arriba/derecha."},
                    {"text": "Línea punteada, sombreada hacia `(0, 0)`", "ok": False, "feedback": "≥ incluye el borde (sólida) y 0 + 0 no es ≥ 6."},
                    {"text": "Línea sólida, sombreada hacia `(0, 0)`", "ok": False, "feedback": "0 ≥ 6 es falso, así que el origen queda afuera."},
                ],
            },
            {
                "question": "Despejás `−y < 2x − 4` multiplicando por `−1` para graficar. ¿Qué desigualdad queda?",
                "options": [
                    {"text": "`y > −2x + 4` (se invierte el signo y se sombrea hacia arriba)", "ok": True, "feedback": "Exacto: nunca te olvides de invertir al multiplicar por −1."},
                    {"text": "`y < −2x + 4`", "ok": False, "feedback": "Al cambiar todos los signos multiplicando por −1, '<' debe cambiar a '>'."},
                    {"text": "`y > 2x − 4`", "ok": False, "feedback": "Faltó cambiar también los signos del lado derecho."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en 2 frases cómo decidís si la frontera es sólida o punteada y cómo elegís qué lado sombrear.",
    },
    # ==================== NIVEL 12: FUNCIONES, SUCESIONES Y TRAMOS ====================
    "al-dominio-rango": {
        "hook": {
            "question": "Si una fórmula calcula el precio de vender `x` entradas de un recital (`f(x) = 10x`), ¿tiene sentido meter `x = −5` o `x = 2.7` entradas?",
            "intuition": "No: en el papel podés meter cualquier número, pero en el mundo real toda función tiene un **dominio** (entradas con sentido) y un **rango** (salidas posibles). Leer eso en una gráfica te deja interpretar cualquier dato real.",
        },
        "concept": {
            "points": [
                "**Dominio (entradas `x`) y Rango (salidas `y`)**: el dominio es qué valores entran (de izquierda a derecha en la gráfica); el rango es qué valores salen (de abajo hacia arriba).",
                "**Restricciones matemáticas automáticas**: en números reales, **nunca podés dividir por `0`** (`x − 4 ≠ 0`) ni **sacar raíz cuadrada de un negativo** (`x − 3 ≥ 0`).",
                "**Rasgos de una curva**: **creciente** (sube de izquierda a derecha), **decreciente** (baja), **máximo/mínimo** (picos y valles) y **ceros/raíces** (donde cruza el eje `X`, `f(x) = 0`).",
                "**Tasa promedio de cambio**: entre `a` y `b` vale `(f(b) − f(a)) / (b − a)`. Incluso en una curva complicada, te da el ritmo promedio de subida o bajada en ese tramo.",
            ],
            "real_world": [
                {
                    "title": "Velocidad promedio en un viaje con paradas",
                    "detail": "Salir del km 110 a las 2 h y llegar al km 320 a las 5 h da una tasa promedio de `(320 − 110)/(5 − 2) = 70 km/h`.",
                },
                {
                    "title": "Curva de batería o altura de un dron",
                    "detail": "El dominio va desde el despegue (`t = 0`) hasta aterrizar; el rango va de `0 m` hasta la altura máxima.",
                },
                {
                    "title": "Métricas de crecimiento mensual",
                    "detail": "Pasar de 20 a 100 clientes en 4 meses es una tasa promedio de `+20` clientes/mes aunque no todos los meses hayan sido iguales.",
                },
            ],
            "key_rule": "Dominio = eje X (entradas válidas) · Rango = eje Y (salidas) · Tasa promedio = `[f(b) − f(a)] / (b − a)`.",
            "pitfall": "Confundir intervalos crecientes (siempre se leen en el eje `X`, ej. 'de `t = 0` a `t = 2`') con los valores alcanzados en `Y`.",
        },
        "example": {
            "title": "Calculá la tasa promedio de cambio en una curva `f(x) = x²`",
            "steps": [
                "Queremos saber qué tan rápido crece `f(x) = x²` entre `x = 1` y `x = 4`.",
                "Calculamos las dos salidas: `f(1) = 1² = 1` y `f(4) = 4² = 16`.",
                "Tasa promedio: `(16 − 1) / (4 − 1) = 15 / 3 = 5` unidades de `y` por cada unidad de `x`.",
            ],
            "lab_link": "math:linear_fn",
            "lab_cta": "Explorar pendientes en el Laboratorio",
        },
        "check": {
            "question": "¿Qué valor de `x` queda FUERA del dominio de `f(x) = 5 / (x + 2)`?",
            "options": [
                {"text": "`x = −2` (porque anula el denominador)", "ok": True, "feedback": "Exacto: −2 + 2 = 0 y no se puede dividir por cero."},
                {"text": "`x = 2`", "ok": False, "feedback": "Con x = 2 queda 5/4 = 1.25, totalmente válido."},
                {"text": "`x = 0`", "ok": False, "feedback": "Con x = 0 queda 5/2 = 2.5, totalmente válido."},
            ],
        },
        "checks": [
            {
                "question": "Una planta mide `10 cm` el día 2 y `34 cm` el día 8. ¿Cuál fue su tasa promedio de crecimiento?",
                "options": [
                    {"text": "`4 cm/día`", "ok": True, "feedback": "Exacto: (34 − 10) / (8 − 2) = 24 / 6 = 4 cm por día."},
                    {"text": "`24 cm/día`", "ok": False, "feedback": "24 cm es el crecimiento total en 6 días; faltó dividir por 6."},
                    {"text": "`3 cm/día`", "ok": False, "feedback": "Dividiste por 8 en vez de por (8 − 2) = 6 días transcurridos."},
                ],
            },
            {
                "question": "Un tanque lleno tiene `500 L` y se vacía hasta `0 L` en `25 min`. ¿Cuál es el RANGO de litros en el tanque?",
                "options": [
                    {"text": "De `0` a `500` litros", "ok": True, "feedback": "Exacto: el rango son las salidas posibles (litros); de 0 a 25 min es el dominio."},
                    {"text": "De `0` a `25` minutos", "ok": False, "feedback": "Los minutos son el dominio (entrada), no el rango (salida)."},
                    {"text": "Todos los números reales", "ok": False, "feedback": "Un tanque no puede tener litros negativos ni más de 500 L."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá la diferencia entre dominio y rango y cómo se calcula la tasa promedio de cambio entre dos instantes.",
    },
    "al-sucesiones": {
        "hook": {
            "question": "Si una lista empieza `10, 14, 18, 22…` y te piden el término número `100`, ¿vas a sumar `+4` noventa y nueve veces a mano?",
            "intuition": "Con una **fórmula explícita** saltás directo al lugar 100 en una cuenta (`10 + 99×4 = 406`). Existen dos familias estrella: las **aritméticas** (suman siempre lo mismo) y las **geométricas** (multiplican siempre por lo mismo).",
        },
        "concept": {
            "points": [
                "**Sucesión aritmética (suma constante `d`)**: `a_n = a₁ + (n − 1) · d`. Ojo con `(n − 1)`: para llegar al 10º término solo diste **9 saltos** desde el 1º.",
                "**Sucesión geométrica (multiplicación constante `r`)**: `a_n = a₁ · r^(n − 1)`. Si `r > 1` crece explosivamente; si `0 < r < 1` se achica hacia 0 (como una pelota rebotando).",
                "**Explícita vs. Recursiva**: la **explícita** calcula `a_n` directo desde `n`. La **recursiva** te dice cómo arrancar (`a₁ = 10`) y cómo sacar el siguiente desde el anterior (`a_n = a_(n−1) + 4`).",
                "**Puente con funciones**: toda sucesión aritmética es una **función lineal** evaluada en `n = 1, 2, 3…`, y toda sucesión geométrica es una **función exponencial**.",
            ],
            "real_world": [
                {
                    "title": "Plan de ahorro escalonado (aritmética)",
                    "detail": "Ahorrar `$100` el mes 1 y sumar `$25` cada mes → el mes 10 ponés `100 + 9×25 = $325`.",
                },
                {
                    "title": "Rebotes de una pelota o cuotas con interés (geométrica)",
                    "detail": "Si rebota a la mitad cada vez (`r = 0.5`): `80 → 40 → 20 → 10 cm`.",
                },
                {
                    "title": "Bucles `for` en programación",
                    "detail": "Una regla recursiva (`actual = anterior * 2`) es literalmente cómo funciona un bucle en código.",
                },
            ],
            "key_rule": "Aritmética: `a_n = a₁ + (n−1)d` · Geométrica: `a_n = a₁ · r^(n−1)` · Del 1º al término `n` hay `n − 1` saltos.",
            "pitfall": "Usar `n` en lugar de `n − 1` en las fórmulas explícitas (correr toda la secuencia un paso hacia adelante).",
        },
        "example": {
            "title": "Saltá directo al término 10 en una aritmética y al 5 en una geométrica",
            "steps": [
                "Aritmética `5, 8, 11, 14…` (`a₁ = 5`, `d = +3`): el 10º término es `5 + (10−1)·3 = 5 + 27 = 32`.",
                "Geométrica `2, 6, 18…` (`a₁ = 2`, `r = 3`): el 5º término es `2 · 3^(5−1) = 2 · 3⁴ = 2 · 81 = 162`.",
                "Con `n = 1` ambas fórmulas devuelven exacto `a₁` (`5 + 0 = 5` y `2 · 3⁰ = 2`).",
            ],
            "lab_link": "math:exponentials",
            "lab_cta": "Explorar crecimiento geométrico en el Laboratorio",
        },
        "check": {
            "question": "En la sucesión aritmética `20, 26, 32, 38…`, ¿cuál es su fórmula explícita?",
            "options": [
                {"text": "`a_n = 20 + 6(n − 1)`", "ok": True, "feedback": "Exacto: probando n=1 da 20, n=2 da 26, n=3 da 32."},
                {"text": "`a_n = 20 + 6n`", "ok": False, "feedback": "Con n = 1 eso daría 26 en vez de 20."},
                {"text": "`a_n = 20 · 6^(n − 1)`", "ok": False, "feedback": "Eso sería geométrica (multiplicando por 6), no sumando 6."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál es la razón `r` de la sucesión geométrica `80, 40, 20, 10…`?",
                "options": [
                    {"text": "`0.5` (`1/2`)", "ok": True, "feedback": "Exacto: cada término se divide por 2, es decir se multiplica por 1/2."},
                    {"text": "`−40`", "ok": False, "feedback": "−40 solo sirve del 1º al 2º; del 2º al 3º bajó 20, no 40."},
                    {"text": "`2`", "ok": False, "feedback": "Con r = 2 la sucesión crecería (80, 160, 320…)."},
                ],
            },
            {
                "question": "Dada la regla recursiva `a₁ = 3` y `a_n = 2 · a_(n−1)`, ¿cuánto vale `a₄`?",
                "options": [
                    {"text": "`24`", "ok": True, "feedback": "Exacto: 3 → 6 → 12 → 24."},
                    {"text": "`12`", "ok": False, "feedback": "12 es a₃; falta multiplicar una vez más por 2."},
                    {"text": "`9`", "ok": False, "feedback": "Sumaste 2 en vez de multiplicar por 2."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá cómo distinguís una sucesión aritmética de una geométrica y por qué aparece `(n − 1)` en sus fórmulas.",
    },
    "al-valor-absoluto-partes": {
        "hook": {
            "question": "¿Por qué una fábrica que produce tornillos de `10 mm` dice 'error admisible ±0.5 mm' y un correo te cobra distinto a partir de los `2 kg`?",
            "intuition": "La primera es una desigualdad de **valor absoluto** (`|x − 10| ≤ 0.5`, distancia al valor objetivo) y la segunda es una **función por partes** (cambia de fórmula según el tramo). Ambas modelan reglas del mundo real donde la recta simple no alcanza.",
        },
        "concept": {
            "points": [
                "**Valor absoluto como distancia**: `|x − c| = d` significa *'números que están a distancia `d` del centro `c`'* → siempre tiene **dos ramas**: `x − c = +d` y `x − c = −d` (si `d = 0` las dos ramas coinciden en una sola solución, `x = c`; si `d < 0` hay `0` soluciones!).",
                "**Gráfica en forma de 'V'**: `f(x) = a|x − h| + k` tiene su vértice (punta) en **`(h, k)`**. Abre hacia arriba si `a > 0` y hacia abajo si `a < 0`.",
                "**Funciones definidas por partes**: tienen 2 o más fórmulas, cada una válida en un intervalo de `x` (como `x ≤ 2` y `x > 2`).",
                "**Cómo evaluar una función por partes**: paso 1, mirá **en qué condición cae tu `x`**; paso 2, usá **únicamente** la fórmula de ese renglón.",
            ],
            "real_world": [
                {
                    "title": "Tolerancias industriales y de resistencias",
                    "detail": "Una resistencia de `100 Ω ± 5%` cumple `|R − 100| ≤ 5` (entre `95 Ω` y `105 Ω`).",
                },
                {
                    "title": "Envíos por peso y estacionamientos",
                    "detail": "Tarifa plana hasta `2 kg` (`$500`), y por encima `500 + 200(x − 2)`: función por tramos pura.",
                },
                {
                    "title": "Escalas impositivas y horas extras",
                    "detail": "Tus primeras 40 h se pagan a tarifa normal y a partir de la hora 41 se paga ×1.5.",
                },
            ],
            "key_rule": "`|expresión| = d` → separá en `+d` y `−d` (si `d < 0`, sin solución) · En funciones por partes elegí primero el tramo correcto.",
            "pitfall": "Al resolver `|x − 5| = 3`, encontrar solo `x = 8` y olvidar la segunda rama `x − 5 = −3` (`x = 2`).",
        },
        "example": {
            "title": "Resolvé `|x − 10| = 2` y una tarifa por tramos",
            "steps": [
                "Para `|x − 10| = 2`: rama 1 → `x − 10 = 2` (`x = 12`); rama 2 → `x − 10 = −2` (`x = 8`). Ambos están a distancia 2 del 10.",
                "Para una tarifa `f(x) = 500` si `x ≤ 2` y `500 + 200(x − 2)` si `x > 2`: con `x = 1.5` cae en el 1er tramo (`$500`).",
                "Con `x = 5` cae en el 2º tramo: `500 + 200(5 − 2) = $1100`.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "¿Cuáles son las DOS soluciones de `|x − 6| = 4`?",
            "options": [
                {"text": "`x = 10` y `x = 2`", "ok": True, "feedback": "Exacto: 6 + 4 = 10 y 6 − 4 = 2 (los dos números a distancia 4 del 6)."},
                {"text": "`x = 10` y `x = −10`", "ok": False, "feedback": "Probá x = −10: |−10 − 6| = 16 ≠ 4."},
                {"text": "Solo `x = 10`", "ok": False, "feedback": "Faltó la rama negativa (x − 6 = −4 → x = 2)."},
            ],
        },
        "checks": [
            {
                "question": "Un gimnasio cobra `$100` si vas `≤ 4` veces al mes, y `100 + 20(x − 4)` si vas más de 4 veces. ¿Cuánto pagás si vas `7` veces?",
                "options": [
                    {"text": "`$160`", "ok": True, "feedback": "Exacto: 7 > 4 → 100 + 20(7 − 4) = 100 + 60 = $160."},
                    {"text": "`$240`", "ok": False, "feedback": "Multiplicaste 20 × 7 en vez de 20 × (7 − 4), cobrando doble las primeras 4 visitas."},
                    {"text": "`$100`", "ok": False, "feedback": "7 supera el tope de 4 visitas."},
                ],
            },
            {
                "question": "¿Dónde está el vértice (punta) de `g(x) = |x + 4| − 1`?",
                "options": [
                    {"text": "`(−4, −1)`", "ok": True, "feedback": "Exacto: x + 4 se hace cero en x = −4, dejando y = −1."},
                    {"text": "`(4, −1)`", "ok": False, "feedback": "Si x = 4, |4 + 4| = 8 (no es el mínimo)."},
                    {"text": "`(−4, 1)`", "ok": False, "feedback": "El −1 afuera baja el vértice a y = −1."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué `|x − 10| = 2` tiene dos soluciones y cómo evaluás una función por tramos.",
    },
    # ==================== NIVEL 13: RADICALES Y EXPONENCIALES ====================
    "al-exponentes-radicales": {
        "hook": {
            "question": "¿Qué significa elevar un número a una fracción, como `9^(1/2)` o `8^(2/3)`? ¿Cómo multiplicás algo 'media vez'?",
            "intuition": "No es un truco raro: si `(9^(1/2))² = 9^(1/2 + 1/2) = 9¹ = 9`, entonces `9^(1/2)` TIENE que ser el número que al cuadrado da `9`, o sea **`√9 = 3`**! Las raíces y los exponentes son en realidad el mismo idioma.",
        },
        "concept": {
            "points": [
                "**Raíces como exponentes fraccionarios**: `a^(1/2) = √a`, `a^(1/3) = ∛a`, y en general **`a^(m/n) = (ⁿ√a)ᵐ`** (el de abajo es la raíz, el de arriba la potencia).",
                "**Truco de cálculo**: en `8^(2/3)` sacá **primero la raíz** (`∛8 = 2`) y después elevá (`2² = 4`). Mantener números chicos evita errores.",
                "**Simplificar radicales**: buscá el mayor cuadrado perfecto (`4, 9, 16, 25, 36, 49…`) dentro de la raíz y sacalo afuera (`√72 = √(36·2) = 6√2`; `√50 = √(25·2) = 5√2`).",
                "**Propiedad clave**: `√(a · b) = √a · √b` funciona en **multiplicación y división**, pero **NUNCA en suma o resta** (`√(9 + 16) = 5 ≠ 3 + 4`).",
            ],
            "real_world": [
                {
                    "title": "Escalas musicales en tu guitarra",
                    "detail": "Cada traste multiplica la frecuencia por **`2^(1/12)`** (la raíz doceava de 2): 12 trastes dan `(2^(1/12))¹² = 2` (una octava exacta!).",
                },
                {
                    "title": "Fórmulas en Excel y programación",
                    "detail": "En Python escribís `x ** 0.5` o `x ** (1/3)`, y en una planilla `=A1^0.5` o `=A1^(1/3)`, para calcular raíces cuadradas y cúbicas directo.",
                },
                {
                    "title": "Diagonales exactas en geometría",
                    "detail": "Un cuadrado de lado `5` tiene diagonal `√50 = 5√2`.",
                },
            ],
            "key_rule": "`a^(m/n) = (ⁿ√a)ᵐ` · Sacá cuadrados perfectos fuera de `√` · `√(a·b) = √a·√b`, pero `√(a+b) ≠ √a + √b`.",
            "pitfall": "Repartir una raíz sobre una suma (`√(x² + 9) = x + 3` es FALSO; probá `x = 4`: `√25 = 5 ≠ 7`).",
        },
        "example": {
            "title": "Simplificá `√72` y calculá `27^(2/3)`",
            "steps": [
                "Para `√72`: el cuadrado perfecto más grande que divide a `72` es `36` (`72 = 36 × 2`).",
                "Separamos: `√72 = √36 · √2 = 6√2`.",
                "Para `27^(2/3)`: primero raíz cúbica `∛27 = 3`, luego al cuadrado `3² = 9`.",
            ],
            "lab_link": "math:powers",
            "lab_cta": "Practicar exponentes en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto vale `16^(3/4)` (raíz cuarta de 16, y luego al cubo)?",
            "options": [
                {"text": "`8`", "ok": True, "feedback": "Exacto: ⁴√16 = 2 (porque 2⁴ = 16), y 2³ = 8."},
                {"text": "`12`", "ok": False, "feedback": "Multiplicaste 16 × 3/4 en vez de usarlo como exponente."},
                {"text": "`4`", "ok": False, "feedback": "Sacaste √16 = 4 pero el exponente es 3/4, no 1/2."},
            ],
        },
        "checks": [
            {
                "question": "Simplificá `√50` al máximo.",
                "options": [
                    {"text": "`5√2`", "ok": True, "feedback": "Exacto: √(25 · 2) = √25 · √2 = 5√2."},
                    {"text": "`25√2`", "ok": False, "feedback": "Cuando 25 sale de la raíz se transforma en √25 = 5."},
                    {"text": "`2√5`", "ok": False, "feedback": "2√5 = √(4·5) = √20, no √50."},
                ],
            },
            {
                "question": "¿Cuánto da `√(36 + 64)`?",
                "options": [
                    {"text": "`10`", "ok": True, "feedback": "Exacto: primero sumás adentro (36 + 64 = 100) y después √100 = 10."},
                    {"text": "`14`", "ok": False, "feedback": "Hiciste √36 + √64 = 6 + 8 = 14: la raíz NO se reparte sobre sumas."},
                    {"text": "`50`", "ok": False, "feedback": "Dividiste 100 por 2 en vez de sacar la raíz cuadrada."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué significa `a^(m/n)` y por qué la raíz de una suma no es igual a la suma de las raíces.",
    },
    "al-exponenciales": {
        "hook": {
            "question": "¿Preferís cobrar `$1000` fijos por día durante 30 días, o empezar con `$1` el día 1 y duplicarlo cada día?",
            "intuition": "A los 10 días el dólar duplicado parece un chiste (llevás `$1023` contra `$10 000`)… pero el día 30 supera los **500 millones de dólares** (frente a `$30 000`). Eso es el poder del **crecimiento exponencial**: crecer multiplicando, no sumando.",
        },
        "concept": {
            "points": [
                "**La fórmula universal `y = a · bˣ`**: **`a`** es el valor inicial (cuando `x = 0`) y **`b`** es el **factor multiplicativo** en cada paso.",
                "**Crecimiento (`b > 1`) vs. Decaimiento (`0 < b < 1`)**: crecer `r%` da `b = 1 + r` (ej. `+10%` → `1.10`); perder `r%` da `b = 1 − r` (ej. `−15%` → `0.85`).",
                "**Interés compuesto y vida media**: en interés compuesto el porcentaje nuevo se aplica sobre el total acumulado; en vida media (`b = 0.5`) la cantidad cae a la mitad cada período (cafeína, fármacos, Carbono-14).",
                "**Lineal vs. Exponencial**: lo lineal suma siempre la misma cantidad (`+100`); lo exponencial multiplica siempre por el mismo factor (`×1.10`). A la larga, lo exponencial siempre gana.",
            ],
            "real_world": [
                {
                    "title": "Ahorros e interés compuesto",
                    "detail": "`$1000` al `10%` anual por 2 años da `1000 × 1.10² = $1210`; en 20 años llega a `~$6727` sin poner un peso extra.",
                },
                {
                    "title": "Depreciación de autos y electrónica",
                    "detail": "Un auto de `$20 000` que pierde `15%` anual vale `20 000 × 0.85^t` (al año 2 vale `$14 450`).",
                },
                {
                    "title": "Eliminación de cafeína o medicamentos",
                    "detail": "Con vida media de 5 h, un café de `160 mg` a las 15 h (3 períodos) todavía deja `160 × 0.5³ = 20 mg` en sangre.",
                },
            ],
            "key_rule": "`y = a · bˣ` · `a` = inicio · Crece `r%` → `b = 1 + r` · Cae `r%` → `b = 1 − r`.",
            "pitfall": "Poner el porcentaje de pérdida directo como base (usar `0.15^t` en vez de `0.85^t` cuando algo pierde 15%: `0.15^t` perdería el 85% por año!).",
        },
        "example": {
            "title": "Seguí un depósito de `$1000` al `10%` compuesto",
            "steps": [
                "Identificamos `a = 1000` y `b = 1 + 0.10 = 1.10` → `A(t) = 1000 · (1.10)^t`.",
                "Año 1: `1000 × 1.10 = $1100` (ganaste `$100`).",
                "Año 2: `1100 × 1.10 = $1210` (ahora ganaste `$110`, porque los `$100` del año 1 también generaron interés).",
            ],
            "lab_link": "math:exponentials",
            "lab_cta": "Practicar exponenciales en el Laboratorio",
        },
        "check": {
            "question": "Un teléfono de `$800` pierde el `25%` de su valor cada año. ¿Qué fórmula modela su valor tras `t` años?",
            "options": [
                {"text": "`V(t) = 800 · (0.75)^t`", "ok": True, "feedback": "Exacto: perder 25% significa conservar el 75% (1 − 0.25 = 0.75) cada año."},
                {"text": "`V(t) = 800 · (0.25)^t`", "ok": False, "feedback": "Eso conservaría solo el 25% (perdería el 75% cada año)."},
                {"text": "`V(t) = 800 − 25t`", "ok": False, "feedback": "Eso restaría $25 fijos por año (lineal), no un 25% exponencial."},
            ],
        },
        "checks": [
            {
                "question": "En `P(t) = 300 · (1.06)^t`, ¿qué porcentaje crece `P` cada período?",
                "options": [
                    {"text": "`6%`", "ok": True, "feedback": "Exacto: 1.06 = 1 + 0.06 → +6% por período."},
                    {"text": "`106%`", "ok": False, "feedback": "106% es el total resultante; el aumento sobre 100% es 6%."},
                    {"text": "`60%`", "ok": False, "feedback": "60% sería 1.60, no 1.06."},
                ],
            },
            {
                "question": "Una dosis de `200 mg` baja a la mitad cada 4 horas (`200 · 0.5^n`). ¿Cuánto queda a las `8 horas` (`n = 2`)?",
                "options": [
                    {"text": "`50 mg`", "ok": True, "feedback": "Exacto: 200 → 100 (4 h) → 50 mg (8 h)."},
                    {"text": "`100 mg`", "ok": False, "feedback": "100 mg es a las 4 horas (n = 1); a las 8 h pasó una segunda vida media."},
                    {"text": "`0 mg`", "ok": False, "feedback": "El decaimiento exponencial se reduce a la mitad cada vez, nunca llega a 0 de golpe."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué representa cada letra en `y = a · bˣ` y por qué un descuento del 15% usa `b = 0.85`.",
    },
    # ==================== NIVEL 14: CUADRÁTICAS E IRRACIONALES ====================
    "al-polinomios-binomios": {
        "hook": {
            "question": "¿Por qué `(x + 3)²` NO es `x² + 9`? Y ¿cómo podés calcular `49 × 51` en tu cabeza en menos de dos segundos?",
            "intuition": "Imaginate un cuadrado de lado `x + 3`: al partirlo en un área de `x` y `3` salen **cuatro piezas** (`x²`, dos rectángulos `3x`, y `9`), no dos. Y para `49 × 51`, la **diferencia de cuadrados** `(50−1)(50+1) = 2500 − 1 = 2499` es magia pura.",
        },
        "concept": {
            "points": [
                "**Multiplicar binomios (todos con todos / modelo de área)**: en `(x + a)(x + b)`, cada término del primero multiplica a cada término del segundo → **`x² + (a + b)x + a·b`**.",
                "**Cuadrado de un binomio**: `(a + b)² = a² + 2ab + b²` y `(a − b)² = a² − 2ab + b²`. ¡Jamás te comas el término cruzado **`2ab`** del medio!",
                "**Diferencia de cuadrados**: `(a + b)(a − b) = a² − b²`. Los dos términos cruzados (`+ab` y `−ab`) se cancelan exactamente.",
                "**Prueba numérica rápida**: si dudás de una expansión algebraica, reemplazá `x = 1` o `x = 2` en los dos lados; si no dan igual, faltó un término.",
            ],
            "real_world": [
                {
                    "title": "Cálculo mental relámpago (`49 × 51` o `98 × 102`)",
                    "detail": "`98 × 102 = (100 − 2)(100 + 2) = 10 000 − 4 = 9996` en un segundo.",
                },
                {
                    "title": "Ampliar habitaciones o terrenos",
                    "detail": "Si un cuadrado de lado `x` se agranda `+2 m` y `+3 m`, su nueva área es `(x+2)(x+3) = x² + 5x + 6`.",
                },
                {
                    "title": "Puente directo a factorizar",
                    "detail": "Ver cómo `(x + a)(x + b)` produce `suma` en el medio y `producto` al final te prepara para desarmarlo al revés en la próxima lección.",
                },
            ],
            "key_rule": "`(x+a)(x+b) = x² + (a+b)x + ab` · `(a±b)² = a² ± 2ab + b²` · `(a+b)(a−b) = a² − b²`.",
            "pitfall": "Escribir `(x + 3)² = x² + 9` (el error más común de toda el álgebra: probalo con `x = 2`: `5² = 25`, mientras `2² + 9 = 13`!).",
        },
        "example": {
            "title": "Expandí `(x + 3)²` y `(x + 5)(x − 5)`",
            "steps": [
                "Reescribimos `(x + 3)²` como `(x + 3)(x + 3)` para no olvidar ningún producto.",
                "Multiplicamos todos con todos: `x² + 3x + 3x + 9 = x² + 6x + 9`.",
                "Para `(x + 5)(x − 5)`: `x² − 5x + 5x − 25 = x² − 25` (los del medio se cancelan).",
            ],
            "lab_link": "math:factoring",
            "lab_cta": "Practicar binomios en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es la expansión correcta de `(x − 5)²`?",
            "options": [
                {"text": "`x² − 10x + 25`", "ok": True, "feedback": "Exacto: x² − 5x − 5x + (−5)² = x² − 10x + 25."},
                {"text": "`x² − 25`", "ok": False, "feedback": "x² − 25 es (x + 5)(x − 5), no (x − 5)²."},
                {"text": "`x² + 25`", "ok": False, "feedback": "Faltó el doble producto del medio (−10x)."},
            ],
        },
        "checks": [
            {
                "question": "Usando `(a − b)(a + b) = a² − b²`, ¿cuánto da `29 × 31` (`(30 − 1)(30 + 1)`)?",
                "options": [
                    {"text": "`899`", "ok": True, "feedback": "Exacto: 30² − 1² = 900 − 1 = 899."},
                    {"text": "`901`", "ok": False, "feedback": "Es resta (a² − b²), no suma."},
                    {"text": "`890`", "ok": False, "feedback": "1² es 1, no 10."},
                ],
            },
            {
                "question": "Expandí `(x + 4)(x − 3)`.",
                "options": [
                    {"text": "`x² + x − 12`", "ok": True, "feedback": "Exacto: +4 − 3 = +1 (es decir +x) y 4 × (−3) = −12."},
                    {"text": "`x² − x − 12`", "ok": False, "feedback": "4 − 3 es +1, no −1."},
                    {"text": "`x² + 7x − 12`", "ok": False, "feedback": "Sumaste 4 + 3 ignorando el signo menos del 3."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué `(x + 3)²` lleva el término `6x` en el medio usando un cuadrado partido en 4 áreas.",
    },
    "al-factorizar-cuadraticas": {
        "hook": {
            "question": "Si dos números multiplicados dan cero (`A · B = 0`), ¿qué sabés con total certeza sobre `A` o `B`?",
            "intuition": "Que **al menos uno de los dos vale `0`**. Ese hecho tan simple (propiedad del producto cero) hace que factorizar `x² + 7x + 12 = 0` en `(x + 3)(x + 4) = 0` resuelva la ecuación en dos segundos: `x = −3` o `x = −4`.",
        },
        "concept": {
            "points": [
                "**Siempre empezá por el factor común**: en `2x² − 10x = 0`, sacá `2x` afuera → `2x(x − 5) = 0` → `x = 0` y `x = 5`.",
                "**Factorizar `x² + bx + c`**: buscá dos números `p` y `q` tales que **`p + q = b`** (sumen el del medio) y **`p · q = c`** (multipliquen el último) → `(x + p)(x + q)`.",
                "**Diferencia de cuadrados al revés**: `x² − 49 = (x + 7)(x − 7)`.",
                "**Propiedad del producto cero**: primero dejá **`= 0`** de un lado; después factorizá e igualá cada paréntesis a `0` por separado.",
            ],
            "real_world": [
                {
                    "title": "Cuándo toca el piso una pelota (`h(t) = 0`)",
                    "detail": "En `−5t² + 20t = 0` → `−5t(t − 4) = 0`: despega en `t = 0 s` y cae al suelo en `t = 4 s`.",
                },
                {
                    "title": "Hallar dimensiones desde un área",
                    "detail": "Un jardín 2 m más largo que ancho con área `35 m²`: `x(x + 2) = 35` → `x² + 2x − 35 = 0` → `(x+7)(x−5)=0` → ancho `5 m`.",
                },
                {
                    "title": "Simplificar fórmulas de ingeniería",
                    "detail": "Factorizar numerador y denominador permite cancelar factores repetidos y limpiar modelos complejos.",
                },
            ],
            "key_rule": "Igualá a `0` → Factor común primero → Buscá `p + q = b` y `p · q = c` → Cada factor igual a `0`.",
            "pitfall": "Intentar usar la propiedad del producto cero cuando el otro lado NO es `0` (ej. de `(x+1)(x+2) = 6` decir `x+1 = 6` es FALSO; primero hay que pasar el `6` restando para igualar a `0`).",
        },
        "example": {
            "title": "Resolvé `x² + 2x = 15` factorizando",
            "steps": [
                "Pasamos `15` restando para igualar a cero: `x² + 2x − 15 = 0`.",
                "Buscamos dos números que multipliquen `−15` y sumen `+2`: son **`+5` y `−3`** → `(x + 5)(x − 3) = 0`.",
                "Igualamos cada paréntesis a cero: **`x = −5`** y **`x = 3`**. Comprobá ambos en `x² + 2x = 15`!",
            ],
            "lab_link": "math:factoring",
            "lab_cta": "Practicar factorización en el Laboratorio",
        },
        "check": {
            "question": "Factorizá `x² − 9x + 20`.",
            "options": [
                {"text": "`(x − 4)(x − 5)`", "ok": True, "feedback": "Exacto: (−4) + (−5) = −9 y (−4) × (−5) = +20."},
                {"text": "`(x + 4)(x + 5)`", "ok": False, "feedback": "Eso daría +9x en el medio, no −9x."},
                {"text": "`(x − 2)(x − 10)`", "ok": False, "feedback": "−2 + (−10) = −12, no −9."},
            ],
        },
        "checks": [
            {
                "question": "Si `(x + 6)(x − 2) = 0`, ¿cuáles son las soluciones?",
                "options": [
                    {"text": "`x = −6` y `x = 2`", "ok": True, "feedback": "Exacto: los valores que vuelven cero a cada paréntesis."},
                    {"text": "`x = 6` y `x = −2`", "ok": False, "feedback": "Cuidado con el signo: con x = 6 el primer paréntesis da 12, no 0."},
                    {"text": "`x = −12`", "ok": False, "feedback": "Probá cada paréntesis igualado a cero."},
                ],
            },
            {
                "question": "La altura de un chorro es `h(t) = −5t² + 15t`. Factorizando `−5t(t − 3) = 0`, ¿en qué dos instantes está en el suelo (`h = 0`)?",
                "options": [
                    {"text": "En `t = 0 s` (al salir) y `t = 3 s` (al caer)", "ok": True, "feedback": "Exacto: −5t = 0 da t = 0 y t − 3 = 0 da t = 3 s."},
                    {"text": "Solo en `t = 3 s`", "ok": False, "feedback": "También está en el suelo al despegar (t = 0 s)."},
                    {"text": "En `t = −5 s` y `t = 15 s`", "ok": False, "feedback": "Buscamos cuándo cada factor vale 0, no los coeficientes."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué condición debe cumplir una ecuación antes de aplicar la propiedad del producto cero y cómo elegís `p` y `q`.",
    },
    "al-parabolas-formula": {
        "hook": {
            "question": "¿Cómo sabés en qué segundo exacto llega a su altura máxima una pelota lanzada al aire — y cómo resolvés cualquier cuadrática incluso cuando NO se puede factorizar a ojo?",
            "intuition": "Toda función cuadrática dibuja una **parábola** simétrica con un único pico o valle (el **vértice**, en `x = −b/(2a)`). Y cuando factorizar no sale fácil, la **fórmula cuadrática** resuelve 100% de los casos.",
        },
        "concept": {
            "points": [
                "**La parábola (`y = ax² + bx + c`)**: si `a > 0` abre hacia arriba (`∪`, tiene mínimo); si `a < 0` abre hacia abajo (`∩`, tiene máximo). El eje de simetría pasa justo por el **vértice en `x = −b / (2a)`**.",
                "**Forma canónica (`y = a(x − h)² + k`)**: te muestra el vértice **`(h, k)`** a simple vista sin hacer cuentas.",
                "**La fórmula cuadrática universal**: para `ax² + bx + c = 0`, **`x = (−b ± √(b² − 4ac)) / (2a)`** (sale de completar el cuadrado y funciona SIEMPRE).",
                "**El discriminante (`Δ = b² − 4ac`)**: mirá lo de adentro de la raíz antes de hacer todo el cálculo: `Δ > 0` → **2 soluciones**; `Δ = 0` → **1 solución** (toca justo el eje); `Δ < 0` → **0 soluciones reales**.",
            ],
            "real_world": [
                {
                    "title": "Tiro parabólico en Física",
                    "detail": "La altura `h(t) = −5t² + 20t + 2` alcanza su techo justo en el vértice `t = −20/(−10) = 2 s` (`h = 22 m`).",
                },
                {
                    "title": "Precio que maximiza ganancias",
                    "detail": "Si subís mucho el precio vendés menos unidades: la ganancia forma una parábola invertida cuyo vértice es el precio óptimo.",
                },
                {
                    "title": "Antenas parabólicas y faros de auto",
                    "detail": "La forma parabólica concentra todas las señales entrantes en un solo punto focal (el receptor).",
                },
            ],
            "key_rule": "Vértice: `x = −b/(2a)` · Fórmula: `x = (−b ± √Δ)/(2a)` con `Δ = b² − 4ac` (`+`→2, `0`→1, `−`→0 soluciones).",
            "pitfall": "Olvidar que `b` puede ser negativo al poner `−b` (si `b = −5`, entonces `−b = +5`), o olvidar dividir también al `−b` por `2a`.",
        },
        "example": {
            "title": "Hallá el pico y los cruces de `h(t) = −5t² + 20t`",
            "steps": [
                "Identificamos `a = −5`, `b = 20`, `c = 0`. Como `a < 0`, abre hacia abajo (tiene altura máxima).",
                "Instante del vértice: `t = −20 / (2 · (−5)) = 2 s`.",
                "Altura máxima: reemplazamos `t = 2` → `h(2) = −5(4) + 20(2) = −20 + 40 = 20 m`.",
            ],
            "lab_link": "math:quadratics",
            "lab_cta": "Practicar vértice y discriminante en el Laboratorio",
        },
        "check": {
            "question": "Una parábola tiene `y = x² − 8x + 12` (`a = 1`, `b = −8`). ¿En qué valor de `x` está su vértice?",
            "options": [
                {"text": "`x = 4`", "ok": True, "feedback": "Exacto: x = −(−8) / (2 · 1) = 8 / 2 = 4 (y el mínimo es y = 16 − 32 + 12 = −4)."},
                {"text": "`x = −4`", "ok": False, "feedback": "Cuidado con el doble signo menos: −(−8) = +8."},
                {"text": "`x = 8`", "ok": False, "feedback": "Faltó dividir por 2a (= 2)."},
            ],
        },
        "checks": [
            {
                "question": "Calculás el discriminante `Δ = b² − 4ac` de `x² + 2x + 5 = 0` (`2² − 4·1·5 = −16`). ¿Cuántas veces cruza el eje `X`?",
                "options": [
                    {"text": "Ninguna (0 soluciones reales)", "ok": True, "feedback": "Exacto: con discriminante negativo la parábola no toca el eje X (acá, como `a > 0`, queda entera por encima)."},
                    {"text": "Dos veces", "ok": False, "feedback": "Eso ocurre solo cuando Δ > 0."},
                    {"text": "Una sola vez", "ok": False, "feedback": "Eso ocurre cuando Δ = 0."},
                ],
            },
            {
                "question": "Usando `x = (−b ± √Δ) / (2a)` en `x² − 3x − 4 = 0` (`a=1, b=−3, c=−4`, `Δ = 9 + 16 = 25`), ¿cuáles son las dos soluciones?",
                "options": [
                    {"text": "`x = 4` y `x = −1`", "ok": True, "feedback": "Exacto: (3 + 5)/2 = 4 y (3 − 5)/2 = −1."},
                    {"text": "`x = −4` y `x = 1`", "ok": False, "feedback": "Olvidaste el signo de −b: −(−3) = +3."},
                    {"text": "`x = 8` y `x = −2`", "ok": False, "feedback": "Faltó dividir por 2a = 2."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá para qué sirve el vértice `x = −b/(2a)` y qué te cuenta el discriminante `b² − 4ac` antes de terminar la fórmula.",
    },
    "al-irracionales": {
        "hook": {
            "question": "Si dibujás un cuadrado perfecto de `1 m × 1 m`, su diagonal mide `√2 ≈ 1.41421356…` ¿Por qué es matemáticamente IMPOSIBLE escribir esa longitud como una fracción exacta?",
            "intuition": "Hay números perfectamente reales que existen en la geometría y la naturaleza (`√2`, `π`), pero cuyas cifras decimales siguen para siempre sin repetir ningún patrón: son los **números irracionales**.",
        },
        "concept": {
            "points": [
                "**Números racionales**: cualquier número que se pueda escribir como fracción `a/b` de dos enteros (`b ≠ 0`). Incluye enteros (`−5 = −5/1`), decimales finitos (`0.75 = 3/4`) y **decimales periódicos** (`0.333… = 1/3`).",
                "**Números irracionales**: decimales infinitos que **nunca repiten un bloque** (`π = 3.14159…`, `√2 = 1.41421…`, `√3`, `√5`, y cualquier raíz cuadrada de un entero que no sea cuadrado perfecto).",
                "**Reglas al mezclarlos**:\n  • Racional + Irracional = **siempre irracional** (`3 + √2`).\n  • Racional (≠ 0) × Irracional = **siempre irracional** (`2π`).\n  • Irracional + o × Irracional = **puede dar racional o irracional** (ej. `√2 × √2 = 2` es racional!).",
                "**Todos juntos forman los Números Reales (`ℝ`)**: cubren sin dejar ni un hueco la recta numérica entera.",
            ],
            "real_world": [
                {
                    "title": "Hojas A4 (`√2`)",
                    "detail": "Las hojas A4 miden `210 × 297 mm` (`297/210 ≈ √2`): al cortarlas por la mitad conservan la misma proporción (A5).",
                },
                {
                    "title": "Ruedas, cables y círculos (`π`)",
                    "detail": "La relación entre el contorno y el diámetro de cualquier círculo del universo es exactamente el irracional `π`.",
                },
                {
                    "title": "Diagonales y distancias",
                    "detail": "Cruzar en diagonal un cuadrado de 1 cuadra × 1 cuadra mide `√2 ≈ 1.41` cuadras (te ahorrás casi 0.6 cuadras).",
                },
            ],
            "key_rule": "Racional = fracción exacta (incluye periódicos) · Irracional = infinito sin patrón (`π`, `√2`) · Racional + Irracional = Irracional.",
            "pitfall": "Clasificar `√9` como irracional solo por ver el símbolo `√` (`√9 = 3` es entero y racional), o creer que `0.333…` es irracional por ser infinito (es `1/3`, racional).",
        },
        "example": {
            "title": "Clasificá 4 números sospechosos en 10 segundos",
            "steps": [
                "`√25`: es `5` exacto → **racional**.",
                "`0.181818…`: repite el bloque `18` (`2/11`) → **racional**.",
                "`√7` y `4 + π`: raíz no exacta y suma con `π` → ambos **irracionales**.",
            ],
            "lab_link": "math:powers",
            "lab_cta": "Repasar potencias y raíces en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál de estos números es RACIONAL?",
            "options": [
                {"text": "`√36`", "ok": True, "feedback": "Exacto: √36 = 6 = 6/1, un número entero y racional."},
                {"text": "`√35`", "ok": False, "feedback": "35 no es un cuadrado perfecto, así que √35 es irracional."},
                {"text": "`2π`", "ok": False, "feedback": "Racional distinto de 0 por irracional siempre da irracional."},
            ],
        },
        "checks": [
            {
                "question": "Si multiplicás `√3 × √12` (= `√36 = 6`), ¿qué te demuestra sobre el producto de dos irracionales?",
                "options": [
                    {"text": "Que dos irracionales multiplicados SÍ pueden dar un resultado racional", "ok": True, "feedback": "Exacto: √3 y √12 son irracionales, pero su producto es el entero 6."},
                    {"text": "Que `√3` en realidad era racional", "ok": False, "feedback": "√3 sigue siendo irracional; al multiplicarse con √12 se formó el cuadrado perfecto 36."},
                    {"text": "Que siempre da racional", "ok": False, "feedback": "√2 × √3 = √6 sigue siendo irracional: depende de los factores."},
                ],
            },
            {
                "question": "¿Por qué `0.272727…` es un número racional aunque tenga infinitas cifras?",
                "options": [
                    {"text": "Porque es un decimal periódico (repite un patrón y equivale a `27/99 = 3/11`)", "ok": True, "feedback": "Exacto: todo decimal periódico se puede escribir como fracción exacta."},
                    {"text": "Porque termina en un número impar", "ok": False, "feedback": "No termina nunca; es racional porque repite el patrón 27."},
                    {"text": "No es racional, es irracional", "ok": False, "feedback": "Los irracionales son únicamente los infinitos SIN patrón periódico."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con ejemplos cómo distinguís un número racional de uno irracional, incluyendo el caso de decimales infinitos periódicos.",
    },
}
