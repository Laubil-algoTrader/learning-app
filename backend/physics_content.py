"""Expanded Physics curriculum adapted from Khan Academy Physics (17 units here, plus the
detailed mechanics units spliced in at the end of this module: 26 in total).

Starts from absolute zero with an intuitive "Introducción a la física" lesson,
followed by 16 progressive units with everyday real-world examples, 3 diagnostic
comprehension checks per lesson, and 116 auto-graded practice cards.
"""

from __future__ import annotations

PHYSICS_DOMAIN = {
    "slug": "fisica",
    "name": "Física",
    "icon": "physics",
    "color": "#7c3f58",
    "domain_type": "conceptual",
    "lab_type": "physics",
    "description": (
        "Física completa desde cero absoluto en 26 temas cotidianos, con la mecánica del "
        "ingreso a ingeniería desarrollada en detalle: introducción, vectores, MRU, MRUV, "
        "tiro oblicuo, Newton, rozamiento, cuerpos vinculados, estática, energía, choques, fluidos, "
        "calor, ondas, electricidad, magnetismo, óptica, relatividad y cuántica."
    ),
    "config": {
        "tools": [
            "kinematics_sim",
            "forces_dcl",
            "waves_audio",
            "energy_ramp",
            "fluids_archimedes",
            "optics_snell",
        ],
        "method_tips": [
            "Construí primero la intuición física ('¿qué ocurre en la vida real y por qué?') antes de reemplazar números en una fórmula.",
            "Dibujá siempre vectores o un Diagrama de Cuerpo Libre y pasá todo al Sistema Internacional (m, kg, s) antes de calcular.",
            "Usá los 6 simuladores de Física para predecir qué va a pasar antes de apretar el botón y comprobar tu hipótesis.",
        ],
    },
    "nodes": [
        # ==================== NIVEL 1 ====================
        {
            "slug": "f-intro-fisica",
            "title": "1. Introducción a la física (empezando de cero)",
            "level": 1,
            "order_index": 1,
            "summary": "Qué estudia la física, cómo usar modelos simples, prefijos cotidianos (kilo/centi/mili) y leer fórmulas sin memorizar.",
            "prerequisites": [],
            "metadata": {"section": "Cinemática y base", "lab_tab": "kinematics", "est_minutes": 15},
            "items": [
                {
                    "item_type": "recall",
                    "title": "¿Por qué la física empieza simplificando (modelos)?",
                    "prompt": "Al estudiar una pelota que cae, los libros de física suelen empezar diciendo 'ignoremos la resistencia del aire'. ¿Por qué hacen eso si en la vida real sí hay aire?",
                    "answer": "Porque aislar primero la causa principal (la gravedad) permite entender la regla base con claridad; una vez dominada, se agregan el aire, el viento o la forma del objeto como capas extra.",
                    "hints": ["Es como aprender a andar en bici en un piso plano antes de bajar una montaña con barro."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Para aislar primero la regla principal y después sumar complejidad paso a paso",
                                "Porque en la Tierra el aire casi nunca afecta a ningún objeto",
                                "Porque las leyes de la física solo funcionan en el espacio",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Prefijo kilo: distancia de una corrida en metros",
                    "prompt": "Saliste a correr 2.5 km por el parque. ¿Cuántos metros son en unidades del Sistema Internacional (kilo = ×1000)? Respondé solo con el número en m.",
                    "answer": "2.5 km × 1000 = 2500 m. El prefijo 'kilo' siempre multiplica por 1000 (1 kg = 1000 g, 1 kW = 1000 W).",
                    "hints": ["Multiplicá los kilómetros por 1000."],
                    "payload": {"check": {"type": "numeric", "value": 2500, "tolerance": 0.01, "unit": "m"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Prefijo centi: medir una puerta en metros",
                    "prompt": "Medís el alto de una puerta con la cinta métrica y da 210 cm. ¿Cuánto es en metros (1 m = 100 cm)? Respondé solo con el número en m.",
                    "answer": "210 ÷ 100 = 2.1 m. Pasar siempre a metros antes de aplicar una fórmula evita errores de factor 100.",
                    "hints": ["Dividí los centímetros por 100."],
                    "payload": {"check": {"type": "numeric", "value": 2.1, "tolerance": 0.01, "unit": "m"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Prefijo mili: tiempo de reacción en segundos",
                    "prompt": "Un ser humano promedio tarda unos 250 ms (milisegundos) en reaccionar ante una luz roja. ¿Cuántos segundos son (1 s = 1000 ms)? Respondé solo con el número en s.",
                    "answer": "250 ÷ 1000 = 0.25 s (un cuarto de segundo). El prefijo 'mili' siempre divide por 1000 (igual que mA en electrónica).",
                    "hints": ["Dividí los milisegundos por 1000."],
                    "payload": {"check": {"type": "numeric", "value": 0.25, "tolerance": 0.01, "unit": "s"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Leer una fórmula como receta (caminar al almacén)",
                    "prompt": "Caminás a paso normal (1.5 m/s) durante exactamente 2 minutos (120 s) hasta la esquina. Usando distancia = velocidad × tiempo, ¿cuántos metros caminaste? Respondé solo con el número en m.",
                    "answer": "Primero pasás el tiempo a segundos (2 min = 120 s) para que coincida con m/s; después d = 1.5 × 120 = 180 m (casi dos cuadras: tiene total sentido).",
                    "hints": ["Nunca mezcles m/s con minutos: usá 120 s."],
                    "payload": {"check": {"type": "numeric", "value": 180, "tolerance": 0.02, "unit": "m"}},
                },
                {
                    "item_type": "recall",
                    "title": "Chequeo de sentido común en un resultado",
                    "prompt": "Hacés una cuenta para calcular a qué velocidad anda una bicicleta en la ciudad y te da 350 m/s (unos 1260 km/h). ¿Qué te indica el chequeo de sentido común?",
                    "answer": "Que cometiste un error de cálculo o de unidades (por ejemplo olvidar dividir o mezclar km con m): 350 m/s supera la velocidad del sonido. Revisar si un número es realista es la mejor red de seguridad en física.",
                    "hints": ["El sonido viaja a 340 m/s: ¿puede una bici romper la barrera del sonido?"],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Que seguro hubo un error de unidades o despeje, porque 350 m/s es más rápido que el sonido",
                                "Que el resultado es correcto si la bici tiene cambios livianos",
                                "Que en física los números nunca tienen relación con la realidad",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Orden de pasos para pensar cualquier problema de física",
                    "prompt": "Ordená los 4 pasos que conviene seguir frente a cualquier situación física para no trabarte.",
                    "answer": "1) Entender qué ocurre e identificar datos → 2) Pasar las unidades al Sistema Internacional → 3) Usar la relación física adecuada → 4) Chequear si el número final tiene sentido en la vida real.",
                    "hints": ["Primero se entiende el problema; al final siempre se verifica si el resultado es realista."],
                    "payload": {
                        "check": {
                            "type": "order",
                            "lines": [
                                "Entender qué pasa en la situación e identificar los datos",
                                "Pasar todas las medidas a unidades estándar (m, kg, s)",
                                "Aplicar la relación o fórmula que conecta las magnitudes",
                                "Chequear si el resultado final tiene sentido en la vida real",
                            ],
                        },
                    },
                },
            ],
        },
        {
            "slug": "f-magnitudes-vectores",
            "title": "2. Escalares, vectores y conversión de unidades",
            "level": 1,
            "order_index": 2,
            "summary": "Distinguir escalares de vectores, pasar km/h a m/s y descomponer direcciones en ejes X/Y.",
            "prerequisites": ["f-intro-fisica"],
            "metadata": {"section": "Cinemática y base", "lab_tab": "kinematics", "est_minutes": 15},
            "items": [
                {
                    "item_type": "recall",
                    "title": "Escalar vs. Vector",
                    "prompt": "Un pronóstico dice '22°C' y 'viento de 30 km/h hacia el sur'. ¿Cuál es escalar y cuál es vector?",
                    "answer": "La temperatura (22°C) es escalar: queda definida solo con valor y unidad. La velocidad del viento (30 km/h hacia el sur) es vectorial porque además importa hacia dónde apunta.",
                    "hints": ["Preguntate en cuál de los dos tiene sentido preguntar '¿hacia dónde?'."],
                    "payload": {
                        "lab_link": "physics:kinematics",
                        "check": {
                            "type": "choice",
                            "options": [
                                "Temperatura = escalar; viento con dirección = vector",
                                "Temperatura = vector; viento = escalar",
                                "Las dos son escalares porque tienen números",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Descomposición vectorial con cos y sen",
                    "prompt": "Pateás una pelota de fútbol a v = 20 m/s con ángulo θ = 60° respecto al pasto (sen 60° ≈ 0.866). ¿Cuánto vale su componente vertical inicial Vy? Respondé solo con el número en m/s.",
                    "answer": "Vy = v · sen(60°) ≈ 20 · 0.866 = 17.3 m/s (mientras que la horizontal es Vx = 20 · cos 60° = 10 m/s).",
                    "hints": ["Vertical (opuesto al ángulo con el suelo) usa seno."],
                    "payload": {
                        "lab_link": "physics:kinematics",
                        "check": {"type": "numeric", "value": 17.3, "tolerance": 0.03, "unit": "m/s"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Componente horizontal de una velocidad",
                    "prompt": "Una manguera lanza agua a v = 40 m/s inclinada a θ = 60° (cos 60° = 0.5). ¿Cuánto vale su componente horizontal Vx? Respondé solo con el número en m/s.",
                    "answer": "Vx = v · cos(θ) = 40 · 0.5 = 20 m/s.",
                    "hints": ["La componente horizontal (adyacente al ángulo) usa coseno."],
                    "payload": {
                        "lab_link": "physics:kinematics",
                        "check": {"type": "numeric", "value": 20, "tolerance": 0.02, "unit": "m/s"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Distancia real con dos tramos perpendiculares",
                    "prompt": "Un repartidor en bici pedalea 5 cuadras (500 m) al este y luego 12 cuadras (1200 m) al norte. ¿A qué distancia en línea recta quedó del local? Respondé solo con el número en m.",
                    "answer": "Los tramos forman un ángulo recto, así que el desplazamiento es la diagonal: √(500² + 1200²) = √1 690 000 = 1300 m (aunque pedaleó 1700 m).",
                    "hints": ["No se suman directo: aplicá Pitágoras."],
                    "payload": {"check": {"type": "numeric", "value": 1300, "tolerance": 0.02, "unit": "m"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Conversión a unidades SI: km/h a m/s",
                    "prompt": "En una avenida un auto va a 72 km/h. ¿Cuántos metros avanza cada segundo (m/s)? Respondé solo con el número en m/s.",
                    "answer": "72 km/h ÷ 3.6 = 20 m/s. En un solo segundo de distracción mirando el celular, el auto recorre 20 metros.",
                    "hints": ["Atajo para pasar km/h a m/s: dividí por 3.6."],
                    "payload": {"check": {"type": "numeric", "value": 20, "tolerance": 0.02, "unit": "m/s"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Dron volando con viento lateral",
                    "prompt": "Un dron vuela hacia el norte a 12 m/s mientras un viento lateral lo empuja hacia el este a 5 m/s. ¿Cuál es su rapidez total respecto al suelo? Respondé solo con el número en m/s.",
                    "answer": "Como los vectores son perpendiculares, v = √(12² + 5²) = √(144 + 25) = √169 = 13 m/s (en diagonal hacia el noreste).",
                    "hints": ["Sumá las componentes perpendiculares con Pitágoras."],
                    "payload": {"check": {"type": "numeric", "value": 13, "tolerance": 0.02, "unit": "m/s"}},
                },
                {
                    "item_type": "recall",
                    "title": "Identificar una magnitud vectorial",
                    "prompt": "¿Cuál de estas magnitudes es vectorial?",
                    "answer": "La aceleración: además de un valor tiene dirección y sentido. Temperatura, masa y tiempo son escalares.",
                    "hints": ["¿Para cuál importa hacia dónde apunta?"],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": ["Temperatura", "Masa", "Aceleración", "Tiempo"],
                            "correct": 2,
                        },
                    },
                },
            ],
        },
        {
            "slug": "f-cinematica",
            "title": "3. Cinemática 1D y 2D: gráficas, caída libre y proyectiles",
            "level": 1,
            "order_index": 3,
            "summary": "MRU, MRUV, lectura de gráficas x-t y v-t, frenado realista, caída libre y tiro parabólico.",
            "prerequisites": ["f-magnitudes-vectores"],
            "metadata": {"section": "Cinemática y base", "lab_tab": "kinematics", "est_minutes": 20},
            "items": [
                {
                    "item_type": "recall",
                    "title": "Caída libre en el vacío (martillo vs. pluma)",
                    "prompt": "Si soltás un martillo y una pluma a la vez en la Luna (sin aire), ¿cuál llega antes al suelo y por qué?",
                    "answer": "Llegan exactamente al mismo tiempo: la aceleración gravitatoria g es independiente de la masa del objeto. En la Tierra solo difieren por la resistencia del aire.",
                    "hints": ["Sin aire no hay frenado aerodinámico."],
                    "payload": {
                        "lab_link": "physics:kinematics",
                        "check": {
                            "type": "choice",
                            "options": [
                                "El martillo, porque pesa más",
                                "Llegan a la vez: la aceleración g no depende de la masa",
                                "La pluma, porque es más liviana",
                            ],
                            "correct": 1,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Punto más alto de un tiro vertical/parabólico",
                    "prompt": "En el punto más alto de un tiro libre de básquet, ¿qué vale la velocidad vertical Vy y qué vale la aceleración?",
                    "answer": "Vy = 0 m/s justo en la cima, pero la aceleración sigue siendo g = 9.81 m/s² hacia abajo (y Vx sigue constante).",
                    "hints": ["La gravedad nunca se apaga arriba."],
                    "payload": {
                        "lab_link": "physics:kinematics",
                        "check": {
                            "type": "choice",
                            "options": [
                                "Vy = 0 y la aceleración también es 0",
                                "Vy es máxima y la aceleración es 0",
                                "Vy = 0 y la aceleración sigue siendo g hacia abajo",
                            ],
                            "correct": 2,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "MRU: posición con velocidad constante",
                    "prompt": "Un ciclista pasa por la marca de 10 m y mantiene 4 m/s constantes por la bicisenda. ¿En qué marca está a los 5 s? Respondé solo con el número en m.",
                    "answer": "x = x₀ + v · t = 10 + 4 · 5 = 30 m.",
                    "hints": ["Sumá la posición inicial a lo que avanzó."],
                    "payload": {
                        "lab_link": "physics:kinematics",
                        "check": {"type": "numeric", "value": 30, "tolerance": 0.02, "unit": "m"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "MRUV: velocidad final",
                    "prompt": "Al entrar a una autopista, una moto va a 5 m/s y acelera a 3 m/s² durante 4 s. ¿Qué velocidad alcanza? Respondé solo con el número en m/s.",
                    "answer": "v = v₀ + a · t = 5 + 3 · 4 = 17 m/s (unos 61 km/h).",
                    "hints": ["Cada segundo gana 3 m/s."],
                    "payload": {
                        "lab_link": "physics:kinematics",
                        "check": {"type": "numeric", "value": 17, "tolerance": 0.02, "unit": "m/s"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Caída libre: distancia recorrida",
                    "prompt": "Se te cae una llave desde un balcón (parte del reposo, g = 9.81 m/s²) y tarda exactamente 2 s en tocar la vereda. ¿Desde qué altura cayó? Respondé solo con el número en m.",
                    "answer": "h = ½ · g · t² = 0.5 · 9.81 · 2² ≈ 19.6 m (unos 6 pisos de altura).",
                    "hints": ["Con v₀ = 0 solo queda ½ · g · t²."],
                    "payload": {
                        "lab_link": "physics:kinematics",
                        "check": {"type": "numeric", "value": 19.62, "tolerance": 0.03, "unit": "m"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Distancia de frenado de un auto (gráfica v-t)",
                    "prompt": "Un auto va a 20 m/s (72 km/h) y frena parejo hasta detenerse en 4 s. Usando el área del triángulo en la gráfica v-t (½ · base · altura), ¿cuántos metros recorre mientras frena? Respondé solo con el número en m.",
                    "answer": "El área bajo una gráfica velocidad-tiempo siempre es el desplazamiento: d = ½ · 4 s · 20 m/s = 40 m (casi media cuadra solo frenando, sin contar tu tiempo de reacción).",
                    "hints": ["En una gráfica v-t, frenar linealmente de 20 a 0 en 4 s dibuja un triángulo."],
                    "payload": {
                        "lab_link": "physics:kinematics",
                        "check": {"type": "numeric", "value": 40, "tolerance": 0.02, "unit": "m"},
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Ángulos con el mismo alcance",
                    "prompt": "Regando el jardín (sin rozamiento del aire), si a 30° el chorro cae en un cantero, ¿qué otro ángulo de disparo logra el mismo alcance? Respondé solo con el número en grados.",
                    "answer": "60°. Dos ángulos complementarios (suman 90°) logran exactamente el mismo alcance; el máximo se obtiene a 45°.",
                    "hints": ["Los dos ángulos suman 90°."],
                    "payload": {
                        "lab_link": "physics:kinematics",
                        "check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": "°"},
                    },
                },
            ],
        },
        # ==================== NIVEL 2 ====================
        {
            "slug": "f-leyes-newton",
            "title": "4. Leyes de Newton, fricción y planos inclinados",
            "level": 2,
            "order_index": 4,
            "summary": "Inercia, F = m·a, acción-reacción, fricción estática vs. cinética, ascensores y rampas.",
            "prerequisites": ["f-cinematica"],
            "metadata": {"section": "Dinámica y energía", "lab_tab": "forces", "est_minutes": 25},
            "items": [
                {
                    "item_type": "recall",
                    "title": "Fuerza neta cuando la velocidad es constante",
                    "prompt": "Un auto viaja en ruta recta con control crucero clavado en 100 km/h constantes. ¿Cuánto vale la fuerza NETA sobre el auto? Respondé solo con el número en N.",
                    "answer": "0 N. El motor sigue haciendo fuerza, pero exactamente igual a la resistencia del aire y el rozamiento: como la aceleración es 0, F_neta = m · 0 = 0 N.",
                    "hints": ["Fuerza neta produce cambio de velocidad, no velocidad constante."],
                    "payload": {
                        "lab_link": "physics:forces",
                        "check": {"type": "numeric", "value": 0, "tolerance": 0, "unit": "N"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "2ª Ley con fricción",
                    "prompt": "Empujás una caja de mudanza de 5 kg con 30 N mientras el piso roza con 10 N en contra. ¿Cuál es su aceleración? Respondé solo con el número en m/s².",
                    "answer": "F_neta = 30 N − 10 N = 20 N. Entonces a = F_neta / m = 20 / 5 = 4 m/s².",
                    "hints": ["Restá la fricción al empuje antes de dividir por la masa."],
                    "payload": {
                        "lab_link": "physics:forces",
                        "check": {"type": "numeric", "value": 4, "tolerance": 0.01, "unit": "m/s²"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "2ª Ley: calcular la fuerza neta",
                    "prompt": "Un carrito de supermercado cargado de 20 kg acelera a 1.5 m/s² cuando arrancás. ¿Qué fuerza neta actúa sobre él? Respondé solo con el número en N.",
                    "answer": "F_neta = m · a = 20 · 1.5 = 30 N.",
                    "hints": ["Masa por aceleración."],
                    "payload": {
                        "lab_link": "physics:forces",
                        "check": {"type": "numeric", "value": 30, "tolerance": 0.02, "unit": "N"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "2ª Ley con fricción: otra caja",
                    "prompt": "Empujás un mueble de 10 kg con 45 N y la fricción cinética se opone con 15 N. ¿Cuál es su aceleración? Respondé solo con el número en m/s².",
                    "answer": "F_neta = 45 − 15 = 30 N. Entonces a = F_neta / m = 30 / 10 = 3 m/s².",
                    "hints": ["Primero la fuerza neta; después dividí por la masa."],
                    "payload": {
                        "lab_link": "physics:forces",
                        "check": {"type": "numeric", "value": 3, "tolerance": 0.02, "unit": "m/s²"},
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Fricción estática vs. cinética al mover una heladera",
                    "prompt": "¿Por qué cuesta más poner en movimiento una heladera pesada desde el reposo que mantenerla deslizando una vez que arrancó?",
                    "answer": "Porque la fricción estática máxima (μ_e · N) es mayor que la fricción cinética (μ_c · N): romper las micro-trabazones entre superficies en reposo exige más fuerza que deslizarlas.",
                    "hints": ["Compará μ estático con μ cinético."],
                    "payload": {
                        "lab_link": "physics:forces",
                        "check": {
                            "type": "choice",
                            "options": [
                                "Porque al moverse la heladera pesa menos",
                                "Porque la fricción estática máxima es mayor que la fricción cinética",
                                "Porque una vez en movimiento desaparece toda fricción",
                            ],
                            "correct": 1,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Peso aparente en un ascensor que arranca hacia arriba",
                    "prompt": "Pesás 70 kg y te parás sobre una balanza dentro de un ascensor que acelera hacia arriba a 2 m/s² (usá g = 10 m/s²). ¿Qué fuerza normal (en N) marca la balanza?",
                    "answer": "N − mg = m·a → N = m·(g + a) = 70 · (10 + 2) = 840 N (sentís un 20% más de peso durante el arranque).",
                    "hints": ["El piso del ascensor tiene que vencer tu peso mg Y además acelerarte hacia arriba (m·a)."],
                    "payload": {
                        "lab_link": "physics:forces",
                        "check": {"type": "numeric", "value": 840, "tolerance": 0.02, "unit": "N"},
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Por qué acción y reacción no se cancelan",
                    "prompt": "Al caminar empujás el piso hacia atrás y el piso te empuja hacia adelante con igual fuerza. ¿Por qué no se cancelan?",
                    "answer": "Porque actúan sobre cuerpos distintos: una fuerza actúa sobre el piso y la otra sobre tu pie. Solo pueden cancelarse fuerzas que actúan sobre el MISMO objeto.",
                    "hints": ["En un Diagrama de Cuerpo Libre solo dibujás fuerzas sobre UN cuerpo."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Porque actúan sobre cuerpos distintos",
                                "Porque la reacción siempre es un poco más débil",
                                "Porque aparecen en momentos distintos",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Pasos para resolver un problema de dinámica",
                    "prompt": "Ordená los pasos para calcular la aceleración de un objeto empujado con fricción.",
                    "answer": "Primero el Diagrama de Cuerpo Libre, después la fuerza neta y por último a = F_neta / m.",
                    "hints": ["Antes de cualquier ecuación va el dibujo."],
                    "payload": {
                        "lab_link": "physics:forces",
                        "check": {
                            "type": "order",
                            "lines": [
                                "Dibujar el Diagrama de Cuerpo Libre con todas las fuerzas sobre el objeto",
                                "Sumar las fuerzas (con su sentido) para obtener la fuerza neta",
                                "Calcular a = F_neta / m",
                            ],
                        },
                    },
                },
            ],
        },
        {
            "slug": "f-circular-gravitacion",
            "title": "5. Movimiento circular, fuerza centrípeta y gravitación",
            "level": 2,
            "order_index": 5,
            "summary": "Aceleración centrípeta (v²/r), curvas en la ruta, Ley de Gravitación Universal y por qué orbitan los satélites.",
            "prerequisites": ["f-leyes-newton"],
            "metadata": {"section": "Dinámica y energía", "lab_tab": "forces", "est_minutes": 20},
            "items": [
                {
                    "item_type": "recall",
                    "title": "Hacia dónde apunta la aceleración en una rotonda",
                    "prompt": "Un auto gira en una rotonda a 40 km/h constantes (misma rapidez todo el tiempo). ¿Está acelerando y hacia dónde apunta la fuerza neta?",
                    "answer": "Sí está acelerando: aunque la rapidez no cambie, cambia constantemente la DIRECCIÓN del vector velocidad. La fuerza neta (fuerza centrípeta, provista por el agarre de las cubiertas) apunta hacia el CENTRO de la curva.",
                    "hints": ["Velocidad es un vector: doblar es cambiar de velocidad."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "No acelera porque el velocímetro marca siempre 40 km/h",
                                "Sí acelera: la fuerza centrípeta apunta hacia el centro de la rotonda",
                                "Sí acelera: una fuerza real lo empuja hacia afuera de la curva",
                            ],
                            "correct": 1,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Tomar una curva al doble de velocidad",
                    "prompt": "La fuerza de agarre necesaria para no derrapar en una curva es F_c = m·v²/r. Si entrás a la misma curva al DOBLE de velocidad, ¿por qué factor se multiplica la fricción que necesitan tus cubiertas? Respondé solo con el número.",
                    "answer": "Por 4: como v está al cuadrado en m·v²/r, duplicar la velocidad cuadruplica la fuerza centrípeta necesaria. Por eso los carteles de velocidad máxima en curvas son tan críticos bajo lluvia.",
                    "hints": ["Reemplazá v por 2v dentro de v²."],
                    "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "×"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Aceleración centrípeta en una curva de autopista",
                    "prompt": "Un auto toma una curva de radio r = 50 m a v = 10 m/s (36 km/h). ¿Cuál es su aceleración centrípeta a_c = v² / r? Respondé solo con el número en m/s².",
                    "answer": "a_c = v² / r = 10² / 50 = 100 / 50 = 2 m/s² (unos 0.2 g, cómodo para los pasajeros).",
                    "hints": ["Elevá v al cuadrado y dividí por el radio r."],
                    "payload": {"check": {"type": "numeric", "value": 2, "tolerance": 0.02, "unit": "m/s²"}},
                },
                {
                    "item_type": "recall",
                    "title": "¿Por qué flotan los astronautas en la Estación Espacial (EEI)?",
                    "prompt": "A 400 km de altura, la gravedad terrestre todavía vale casi un 90% de la que sentimos en el piso. Entonces, ¿por qué flotan los astronautas en la Estación Espacial?",
                    "answer": "Porque la estación y los astronautas están en caída libre continua alrededor de la Tierra: avanzan tan rápido de costado (~27 600 km/h) que el planeta 'se curva debajo' al mismo ritmo que caen.",
                    "hints": ["Pensá en estar dentro de un ascensor al que se le corta el cable."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Porque en el espacio a 400 km la gravedad es cero",
                                "Porque caen libremente alrededor de la Tierra junto con la estación",
                                "Porque la rotación de la estación cancela la gravedad",
                            ],
                            "correct": 1,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Ley de Gravitación Universal: duplicar la distancia",
                    "prompt": "Según F = G · m₁·m₂ / r², si un satélite se aleja al DOBLE de distancia del centro de la Tierra, ¿qué porcentaje de la fuerza gravitatoria original siente? Respondé solo con el número en %.",
                    "answer": "25% (un cuarto): la gravedad cae con el cuadrado de la distancia (1 / 2² = 1/4 = 25%).",
                    "hints": ["Dividí 100% por 2²."],
                    "payload": {"check": {"type": "numeric", "value": 25, "tolerance": 0.01, "unit": "%"}},
                },
                {
                    "item_type": "recall",
                    "title": "Centrifugado del lavarropas",
                    "prompt": "Cuando el tambor del lavarropas gira rápido, el agua sale por los agujeros mientras la ropa queda adentro. ¿Qué explicación física es la correcta?",
                    "answer": "Por inercia (1ª ley), tanto la ropa como el agua tienden a seguir en línea recta (tangente). La pared del tambor le aplica fuerza centrípeta a la ropa para obligarla a girar, pero en los agujeros no hay pared que empuje al agua, así que el agua escapa por la tangente.",
                    "hints": ["No existe una fuerza misteriosa 'hacia afuera': es inercia + falta de pared en los agujeros."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "La pared empuja la ropa hacia adentro, pero en los agujeros el agua sigue en línea recta por inercia",
                                "El tambor genera un campo que repele específicamente al agua",
                                "La gravedad aumenta dentro del tambor y empuja el agua",
                            ],
                            "correct": 0,
                        },
                    },
                },
            ],
        },
        {
            "slug": "f-trabajo-energia",
            "title": "6. Trabajo, energía, resortes y potencia",
            "level": 2,
            "order_index": 6,
            "summary": "Energía cinética (½mv²), potencial gravitatoria (mgh) y elástica (½kx²), conservación y potencia (W y kWh).",
            "prerequisites": ["f-leyes-newton"],
            "metadata": {"section": "Dinámica y energía", "lab_tab": "energy", "est_minutes": 20},
            "items": [
                {
                    "item_type": "recall",
                    "title": "Efecto de duplicar la velocidad sobre la energía cinética",
                    "prompt": "Si un auto pasa de 50 a 100 km/h (duplica su velocidad), ¿por qué factor se multiplica su energía cinética Ek = ½mv² (y su distancia mínima de frenado)? Respondé solo con el número.",
                    "answer": "Por 4 (se cuadruplica), porque la velocidad está elevada al cuadrado.",
                    "hints": ["Reemplazá v por 2v dentro de v²."],
                    "payload": {
                        "lab_link": "physics:energy",
                        "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "×"},
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Conservación de energía con fricción",
                    "prompt": "Cuando un ciclista frena bajando una cuesta y se detiene, ¿se 'destruyó' su energía mecánica?",
                    "answer": "No: la energía total siempre se conserva; la energía mecánica pasó a ser energía térmica (por eso los discos de freno salen hirviendo).",
                    "hints": ["Probalo en el Laboratorio de Física → Energía."],
                    "payload": {
                        "lab_link": "physics:energy",
                        "check": {
                            "type": "choice",
                            "options": [
                                "Sí: los frenos destruyen la energía",
                                "No: se transformó en calor en las pastillas y discos; la energía total se conserva",
                                "No: quedó guardada como energía potencial en el piso",
                            ],
                            "correct": 1,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Energía cinética de una pelota",
                    "prompt": "Una pelota de 2 kg se mueve a 3 m/s. ¿Cuánta energía cinética tiene? Respondé solo con el número en J.",
                    "answer": "Ek = ½ · m · v² = 0.5 · 2 · 3² = 9 J.",
                    "hints": ["Elevá la velocidad al cuadrado antes de multiplicar."],
                    "payload": {
                        "lab_link": "physics:energy",
                        "check": {"type": "numeric", "value": 9, "tolerance": 0.02, "unit": "J"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Energía potencial gravitatoria",
                    "prompt": "Subís una caja de 3 kg a un estante a 4 m de altura (g = 9.81 m/s²). ¿Cuánta energía potencial ganó? Respondé solo con el número en J.",
                    "answer": "Ep = m · g · h = 3 · 9.81 · 4 ≈ 117.7 J.",
                    "hints": ["Masa × gravedad × altura."],
                    "payload": {
                        "lab_link": "physics:energy",
                        "check": {"type": "numeric", "value": 117.72, "tolerance": 0.03, "unit": "J"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Energía elástica de un resorte (amortiguador)",
                    "prompt": "Al pasar por un lomo de burro, el resorte de una bici (constante k = 2000 N/m) se comprime x = 0.1 m (10 cm). ¿Cuánta energía elástica almacena (Ee = ½ · k · x²)? Respondé solo con el número en J.",
                    "answer": "Ee = ½ · 2000 · (0.1)² = 1000 · 0.01 = 10 J.",
                    "hints": ["Recordá elevar x = 0.1 al cuadrado primero: 0.1² = 0.01."],
                    "payload": {"check": {"type": "numeric", "value": 10, "tolerance": 0.02, "unit": "J"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Potencia: energía por unidad de tiempo",
                    "prompt": "Subís una escalera de 6 m (pesás 60 kg, g = 10 m/s², así que Ep = 3600 J) en 12 segundos. ¿Qué potencia promedio desarrollaron tus piernas? Respondé solo con el número en W.",
                    "answer": "P = Energía / tiempo = 3600 J / 12 s = 300 W (como 30 lámparas LED de 10 W encendidas a la vez).",
                    "hints": ["1 W = 1 J/s."],
                    "payload": {"check": {"type": "numeric", "value": 300, "tolerance": 0.02, "unit": "W"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Conservación: velocidad al pie de una rampa",
                    "prompt": "Un skater parte del reposo y baja sin fricción una rampa de 5 m de altura (usá g = 10 m/s²). ¿Con qué velocidad llega abajo? Respondé solo con el número en m/s.",
                    "answer": "m·g·h = ½·m·v² → v² = 2·g·h = 100 → v = 10 m/s (36 km/h). La masa se cancela: da igual cuánto pese el skater.",
                    "hints": ["Igualá Ep arriba con Ek abajo."],
                    "payload": {
                        "lab_link": "physics:energy",
                        "check": {"type": "numeric", "value": 10, "tolerance": 0.03, "unit": "m/s"},
                    },
                },
            ],
        },
        # ==================== NIVEL 3 ====================
        {
            "slug": "f-momento-choques",
            "title": "7. Momento lineal, impulso y choques",
            "level": 3,
            "order_index": 7,
            "summary": "Cantidad de movimiento (p = mv), impulso (F·Δt) en airbags y cascos, conservación y choques elásticos/inelásticos.",
            "prerequisites": ["f-trabajo-energia"],
            "metadata": {"section": "Dinámica y energía", "lab_tab": "forces", "est_minutes": 20},
            "items": [
                {
                    "item_type": "recall",
                    "title": "¿Cómo te salva la vida un airbag?",
                    "prompt": "En un choque, tu cabeza pasa de moverse rápido a velocidad 0 (mismo cambio de momento Δp con o sin airbag). ¿Qué cambia el airbag para reducir drásticamente la fuerza sobre tu cráneo?",
                    "answer": "Aumenta el tiempo de frenado Δt. Como F · Δt = Δp, al estirar el choque de ~0.01 s (volante rígido) a ~0.10 s (bolsa blanda), la fuerza media se reduce unas 10 veces.",
                    "hints": ["Fijate en F = Δp / Δt: el cambio de momento es fijo."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Reduce el cambio total de momento Δp a la mitad",
                                "Aumenta el tiempo de impacto Δt, reduciendo la fuerza media F = Δp / Δt",
                                "Elimina tu masa durante el choque",
                            ],
                            "correct": 1,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Impulso: fuerza media al atajar una pelota",
                    "prompt": "Atajás una pelota de 0.5 kg que venía a 12 m/s (Δp = 6 kg·m/s) acompañando el movimiento con las manos durante Δt = 0.2 s. ¿Qué fuerza media sentís en las palmas? Respondé solo con el número en N.",
                    "answer": "F = Δp / Δt = 6 / 0.2 = 30 N. Si pusieras las manos rígidas (Δt = 0.02 s), sentirías 300 N y te dolería.",
                    "hints": ["Dividí el cambio de momento (m · v) por el tiempo Δt."],
                    "payload": {"check": {"type": "numeric", "value": 30, "tolerance": 0.02, "unit": "N"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Choque inelástico en un semáforo",
                    "prompt": "Un auto de 1000 kg a 12 m/s choca por detrás a otro auto idéntico de 1000 kg detenido y quedan enganchados juntos. ¿A qué velocidad salen moviéndose justo después del impacto? Respondé solo con el número en m/s.",
                    "answer": "Momento inicial = 1000 · 12 + 1000 · 0 = 12 000 kg·m/s. Masa conjunta = 2000 kg → v_f = 12 000 / 2000 = 6 m/s.",
                    "hints": ["El momento total antes y después es igual: m₁v₁ = (m₁ + m₂)·v_f."],
                    "payload": {"check": {"type": "numeric", "value": 6, "tolerance": 0.02, "unit": "m/s"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Retroceso sobre una patineta",
                    "prompt": "Estás quieto sobre una patineta (masa total 60 kg) y lanzás hacia adelante una mochila de 6 kg a 5 m/s. ¿Con qué rapidez salís rodando hacia atrás? Respondé solo con el número en m/s.",
                    "answer": "El momento inicial era 0, así que 60 · v = 6 · 5 = 30 → v = 30 / 60 = 0.5 m/s hacia atrás. Exactamente así funciona un cohete en el vacío expulsando gases.",
                    "hints": ["El momento de la mochila hacia adelante iguala al tuyo hacia atrás."],
                    "payload": {"check": {"type": "numeric", "value": 0.5, "tolerance": 0.02, "unit": "m/s"}},
                },
                {
                    "item_type": "recall",
                    "title": "Choque elástico vs. inelástico",
                    "prompt": "En un choque inelástico (como dos autos que se abollan y quedan pegados), ¿qué magnitud se conserva y cuál NO se conserva?",
                    "answer": "El momento lineal total SIEMPRE se conserva (si no hay fuerzas externas); la energía cinética NO se conserva porque gran parte se gasta en deformar la chapa, sonido y calor.",
                    "hints": ["Diferenciá p = mv de Ek = ½mv²."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Se conserva el momento lineal, pero se pierde energía cinética en deformación y calor",
                                "Se conserva la energía cinética, pero se pierde el momento lineal",
                                "No se conserva ninguno de los dos",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Cómo propulsarse en el vacío del espacio",
                    "prompt": "Un cohete en el vacío no tiene aire contra el cual empujar. ¿Cómo logra acelerar?",
                    "answer": "Por conservación del momento (y 3ª ley de Newton): expulsa gases a altísima velocidad hacia atrás, ganando exactamente el mismo momento hacia adelante.",
                    "hints": ["Igual que lanzar la mochila desde una patineta."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Empuja contra la gravedad de los planetas cercanos",
                                "Expulsa masa (gases) hacia atrás y conserva el momento acelerando hacia adelante",
                                "Usa la presión de la luz solar para frenar el vacío",
                            ],
                            "correct": 1,
                        },
                    },
                },
            ],
        },
        {
            "slug": "f-torque-rotacion",
            "title": "8. Torca (torque), equilibrio y momento angular",
            "level": 3,
            "order_index": 8,
            "summary": "Palancas y torque (τ = r·F·sen θ), equilibrio en subibajas, momento de inercia y conservación del momento angular.",
            "prerequisites": ["f-leyes-newton"],
            "metadata": {"section": "Dinámica y energía", "lab_tab": "forces", "est_minutes": 20},
            "items": [
                {
                    "item_type": "worked_example",
                    "title": "Aflojar la tuerca de una rueda con un caño extensor",
                    "prompt": "Hacés 100 N de fuerza perpendicular sobre una llave de 0.3 m (30 cm) para sacar una rueda pinchada. ¿Qué torque (τ = r · F) aplicás? Respondé solo con el número en N·m.",
                    "answer": "τ = 0.3 m · 100 N = 30 N·m. Si le ponés un caño extensor de 0.6 m, con la misma fuerza duplicás el torque a 60 N·m.",
                    "hints": ["Multiplicá el brazo de palanca (en metros) por la fuerza perpendicular."],
                    "payload": {"check": {"type": "numeric", "value": 30, "tolerance": 0.02, "unit": "N·m"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Equilibrio en un subibaja de plaza",
                    "prompt": "En un subibaja, un chico de 30 kg se sienta a 2 m del eje central. ¿A qué distancia del otro lado debe sentarse un adulto de 60 kg para quedar en equilibrio? Respondé solo con el número en m.",
                    "answer": "Para que los torques se igualen: 30 · 2 = 60 · d → d = 60 / 60 = 1 m (al doble de peso, la mitad de brazo).",
                    "hints": ["Igualá masa₁ · distancia₁ = masa₂ · distancia₂."],
                    "payload": {"check": {"type": "numeric", "value": 1, "tolerance": 0.02, "unit": "m"}},
                },
                {
                    "item_type": "recall",
                    "title": "Por qué el picaporte está lejos de las bisagras",
                    "prompt": "¿Por qué las manijas de todas las puertas están en el borde opuesto a las bisagras y no en el medio?",
                    "answer": "Para maximizar el brazo de palanca r: como τ = r · F, cuanto más lejos del eje (bisagra) empujás, menos fuerza F necesitás para generar el mismo giro.",
                    "hints": ["Despejá F = τ / r."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Para maximizar el brazo r y abrir la puerta con la mínima fuerza posible",
                                "Porque la madera pesa menos en ese borde",
                                "Para que la puerta gire más lento y no golpee",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "La patinadora que junta los brazos para girar rápido",
                    "prompt": "Cuando una patinadora sobre hielo (o vos en una silla giratoria) acerca los brazos al pecho mientras gira, su velocidad de giro se dispara. ¿Por qué?",
                    "answer": "Por conservación del momento angular (L = I · ω): al acercar la masa al eje baja su momento de inercia I, y para que L se mantenga constante debe subir la velocidad angular ω.",
                    "hints": ["L = I · ω se conserva si no hay torque externo."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Porque al juntar los brazos aplica más fuerza contra el aire",
                                "Porque baja su momento de inercia I y, para conservar L = I·ω, sube su velocidad angular ω",
                                "Porque su masa total disminuye al encogerse",
                            ],
                            "correct": 1,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Empujar una llave en diagonal (efecto del ángulo)",
                    "prompt": "Tirás de una llave de 0.4 m con 50 N, pero en diagonal a 30° respecto al mango (sen 30° = 0.5). ¿Qué torque efectivo generás (τ = r · F · sen θ)? Respondé solo con el número en N·m.",
                    "answer": "τ = 0.4 · 50 · 0.5 = 10 N·m (la mitad que si empujaras a 90° perpendicular al mango).",
                    "hints": ["Solo cuenta la componente perpendicular: F · sen(30°)."],
                    "payload": {"check": {"type": "numeric", "value": 10, "tolerance": 0.02, "unit": "N·m"}},
                },
                {
                    "item_type": "recall",
                    "title": "Para qué lleva una barra larga un equilibrista",
                    "prompt": "¿Por qué un equilibrista en la cuerda floja carga una vara muy larga y pesada en las puntas?",
                    "answer": "Aumenta mucho su momento de inercia I: al repartir masa lejos del eje de caída, cualquier pequeño desequilibrio lo hace girar mucho más despacio, dándole tiempo para corregir.",
                    "hints": ["Más masa lejos del eje = mayor inercia rotacional (resistencia a empezar a girar)."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Para aumentar su momento de inercia I y caer más lento, ganando tiempo para corregirse",
                                "Para pesar menos sobre la cuerda",
                                "Para generar sustentación con el viento",
                            ],
                            "correct": 0,
                        },
                    },
                },
            ],
        },
        {
            "slug": "f-fluidos",
            "title": "9. Fluidos: presión, flotación y principio de Bernoulli",
            "level": 3,
            "order_index": 9,
            "summary": "Presión hidrostática al bucear, frenos hidráulicos (Pascal), barcos que flotan (Arquímedes) y mangueras/aviones (Bernoulli).",
            "prerequisites": ["f-trabajo-energia"],
            "metadata": {"section": "Fluidos, calor y ondas", "lab_tab": "fluids", "est_minutes": 25},
            "items": [
                {
                    "item_type": "worked_example",
                    "title": "Presión bajo el agua al bucear",
                    "prompt": "En la superficie hay 1 atm (~100 kPa) y cada 10 m bajo el agua la presión suma ~1 atm (ρ·g·h ≈ 1000 · 10 · 10 = 100 kPa). ¿Cuántas atmósferas de presión total siente un buzo a 20 m de profundidad? Respondé solo con el número en atm.",
                    "answer": "3 atm: 1 atm de la atmósfera + 2 atm por los 20 metros de agua encima. Por eso hay que compensar los oídos al bajar.",
                    "hints": ["No te olvides de sumar la 1 atm del aire en la superficie."],
                    "payload": {
                        "lab_link": "physics:fluids",
                        "check": {"type": "numeric", "value": 3, "tolerance": 0.05, "unit": "atm"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Gato hidráulico (Principio de Pascal)",
                    "prompt": "En un elevador hidráulico, el pistón chico tiene área A₁ = 10 cm² y el grande A₂ = 500 cm² (50 veces mayor). Si empujás el chico con F₁ = 200 N, ¿qué peso F₂ podés levantar? Respondé solo con el número en N.",
                    "answer": "Por Pascal la presión es igual en ambos lados (F₁/A₁ = F₂/A₂), así que F₂ = 200 · (500/10) = 10 000 N (~1 tonelada, un auto chico). A cambio, tenés que bombear 50 veces más recorrido.",
                    "hints": ["La fuerza se multiplica por la relación de áreas A₂ / A₁."],
                    "payload": {
                        "lab_link": "physics:fluids",
                        "check": {"type": "numeric", "value": 10000, "tolerance": 0.02, "unit": "N"},
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Por qué un barco de acero flota y un clavo se hunde",
                    "prompt": "El acero es casi 8 veces más denso que el agua. ¿Por qué un barco enorme de acero flota y un pequeño clavo de acero se hunde?",
                    "answer": "El casco del barco encierra mucho aire, haciendo que su densidad PROMEDIO (masa total / volumen total) sea menor que la del agua: desplaza un volumen de agua cuyo peso iguala al del barco (Arquímedes).",
                    "hints": ["Pensá en la densidad promedio de todo el volumen que desaloja el casco."],
                    "payload": {
                        "lab_link": "physics:fluids",
                        "check": {
                            "type": "choice",
                            "options": [
                                "Porque el barco tiene motores que lo sostienen arriba",
                                "Porque el casco encierra aire y su densidad promedio es menor que la del agua",
                                "Porque el agua de mar empuja más a los objetos grandes que a los chicos por su forma",
                            ],
                            "correct": 1,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Qué porcentaje de un iceberg queda bajo el agua",
                    "prompt": "El hielo tiene una densidad de unos 900 kg/m³ y el agua unos 1000 kg/m³ (valores redondeados). Según Arquímedes, ¿qué porcentaje del volumen de un iceberg queda sumergido bajo el agua? Respondé solo con el número en %.",
                    "answer": "90% (ρ_hielo / ρ_agua = 900 / 1000 = 0.90). Solo asoma un 10% por encima de la superficie. Comprobalo en el Laboratorio de Física → Fluidos.",
                    "hints": ["Dividí la densidad del objeto por la densidad del líquido."],
                    "payload": {
                        "lab_link": "physics:fluids",
                        "check": {"type": "numeric", "value": 90, "tolerance": 0.03, "unit": "%"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Tapar la boca de una manguera (continuidad)",
                    "prompt": "Por una manguera sale agua a 2 m/s. Ponés el pulgar y reducís el área de salida a un cuarto (A₂ = A₁ / 4). Con el mismo caudal (A₁·v₁ = A₂·v₂), ¿a qué velocidad sale el chorro? Respondé solo con el número en m/s.",
                    "answer": "v₂ = 4 · 2 = 8 m/s. Al achicar el paso por 4, el fluido debe ir 4 veces más rápido para que siga pasando la misma cantidad de litros por segundo.",
                    "hints": ["Si el área baja 4 veces, la velocidad sube 4 veces."],
                    "payload": {"check": {"type": "numeric", "value": 8, "tolerance": 0.02, "unit": "m/s"}},
                },
                {
                    "item_type": "recall",
                    "title": "Principio de Bernoulli: velocidad vs. presión",
                    "prompt": "En un caño que se angosta, el agua corre más rápido por la parte estrecha; algo parecido pasa con el aire que acelera sobre el ala de un avión. ¿Qué pasa con la presión del fluido en la zona donde se mueve más rápido?",
                    "answer": "La presión BAJA (Bernoulli): donde el fluido acelera gana energía cinética a costa de presión. Por eso en la parte estrecha de un caño (tubo Venturi) la presión es menor: así aspiran el líquido los pulverizadores y los carburadores.",
                    "hints": ["En Bernoulli, mayor velocidad del fluido implica menor presión."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "La presión baja donde el fluido se mueve más rápido",
                                "La presión sube donde el fluido se mueve más rápido",
                                "La presión no depende de la velocidad del fluido",
                            ],
                            "correct": 0,
                        },
                    },
                },
            ],
        },
        {
            "slug": "f-termodinamica",
            "title": "10. Calor, temperatura, gases y termodinámica",
            "level": 3,
            "order_index": 10,
            "summary": "Calor vs. temperatura, Q = m·c·ΔT, cambios de fase, gases ideales (PV = nRT), 1ª y 2ª ley y disipación térmica.",
            "prerequisites": ["f-trabajo-energia"],
            "metadata": {"section": "Fluidos, calor y ondas", "lab_tab": "energy", "est_minutes": 25},
            "items": [
                {
                    "item_type": "recall",
                    "title": "Diferencia física entre temperatura y calor",
                    "prompt": "¿En qué se diferencian físicamente la temperatura y el calor?",
                    "answer": "La temperatura mide la energía cinética promedio de las partículas. El calor (Q) es energía térmica en tránsito desde un cuerpo más caliente hacia uno más frío.",
                    "hints": ["Un objeto 'tiene' temperatura; el calor 'fluye'."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Son lo mismo, medido en unidades distintas",
                                "Temperatura = energía cinética promedio de las partículas; calor = energía en tránsito de lo caliente a lo frío",
                                "Temperatura = energía térmica total del cuerpo; calor = qué tan caliente se siente al tacto",
                            ],
                            "correct": 1,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Calentar agua para el mate (Q = m · c · ΔT)",
                    "prompt": "Querés calentar 1 kg (1 litro) de agua de 20°C a 80°C (ΔT = 60°C). El calor específico del agua es c = 4.2 kJ/(kg·°C). ¿Cuántos kJ de energía necesitás? Respondé solo con el número en kJ.",
                    "answer": "Q = m · c · ΔT = 1 · 4.2 · 60 = 252 kJ. Con una pava eléctrica de 2000 W (2 kJ/s) tarda unos 252 / 2 = 126 s (~2 minutos).",
                    "hints": ["Multiplicá masa × calor específico × salto de temperatura."],
                    "payload": {"check": {"type": "numeric", "value": 252, "tolerance": 0.03, "unit": "kJ"}},
                },
                {
                    "item_type": "recall",
                    "title": "Por qué transpirar te refresca (calor latente)",
                    "prompt": "¿Por qué mojarte la cara o transpirar te enfría incluso cuando el aire está caluroso?",
                    "answer": "Para evaporarse (pasar de líquido a gas), el agua absorbe una enorme cantidad de energía térmica (calor latente de vaporización) directamente de tu piel.",
                    "hints": ["Cambiar de líquido a vapor cuesta mucha energía térmica."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Porque el sudor sale del cuerpo más frío que la sangre",
                                "Porque al evaporarse el agua absorbe energía térmica (calor latente) de tu piel",
                                "Porque el agua bloquea la radiación del aire",
                            ],
                            "correct": 1,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Presión de las cubiertas del auto en invierno (PV = nRT)",
                    "prompt": "En una mañana helada de invierno, el tablero del auto avisa 'baja presión en neumáticos' aunque no estén pinchados. ¿Por qué?",
                    "answer": "Por la ley de gases ideales (P·V = n·R·T): a volumen V casi fijo, cuando baja la temperatura T del aire adentro de la cubierta, las moléculas golpean menos fuerte y la presión P cae.",
                    "hints": ["Con V y n constantes, P es proporcional a T (en Kelvin)."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Al bajar la temperatura T con volumen casi constante, baja la presión P del aire interior",
                                "El frío encoge las moléculas de aire hasta hacerlas escapar por el caucho",
                                "La goma se expande con el frío y agranda el volumen",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Los 3 mecanismos de transferencia de calor",
                    "prompt": "Nombrá los 3 mecanismos por los que se transfiere el calor y un ejemplo de cada uno.",
                    "answer": "Conducción (contacto directo, ej. chip → disipador), Convección (movimiento de fluido/aire, ej. ventilador o estufa) y Radiación (ondas infrarrojas, ej. el Sol o brasas).",
                    "hints": ["Sólidos, fluidos y vacío."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Conducción, inducción y evaporación",
                                "Fusión, convección y reflexión",
                                "Conducción, convección y radiación",
                            ],
                            "correct": 2,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Efecto Joule: potencia disipada en una resistencia",
                    "prompt": "Por una resistencia de 220 Ω circulan 20 mA (0.02 A). ¿Cuánta potencia disipa como calor (P = I² · R)? Respondé solo con el número en mW.",
                    "answer": "P = 0.02² · 220 = 0.088 W = 88 mW (muy por debajo de los 250 mW de una resistencia de 1/4 W).",
                    "hints": ["Elevá la corriente en amperios al cuadrado y pasá el resultado de W a mW."],
                    "payload": {
                        "lab_link": "electronics:ohm",
                        "check": {"type": "numeric", "value": 88, "tolerance": 0.02, "unit": "mW"},
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Mecanismo de transferencia: ventilador sobre un disipador",
                    "prompt": "Un ventilador sopla aire sobre las aletas de un disipador de PC. ¿Qué mecanismo de transferencia de calor está reforzando?",
                    "answer": "Convección: el aire en movimiento se lleva el calor de las aletas.",
                    "hints": ["El calor viaja arrastrado por el fluido en movimiento."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": ["Conducción", "Convección", "Radiación"],
                            "correct": 1,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Mecanismo de transferencia: el calor del Sol",
                    "prompt": "¿Por qué mecanismo llega el calor del Sol a la Tierra a través del vacío del espacio?",
                    "answer": "Radiación: ondas electromagnéticas que no necesitan materia para viajar.",
                    "hints": ["En el vacío no hay ni contacto ni aire."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": ["Conducción", "Convección", "Radiación"],
                            "correct": 2,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Sentido espontáneo del flujo de calor",
                    "prompt": "Apoyás un cubito de hielo en la palma de la mano. ¿Qué pasa con el calor?",
                    "answer": "El calor fluye de tu mano (más caliente) al hielo (más frío). El 'frío' no viaja: sentís que tu mano pierde energía térmica.",
                    "hints": ["2ª Ley: el calor va espontáneamente de lo caliente a lo frío."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "El frío pasa del hielo a tu mano",
                                "El calor pasa de tu mano al hielo",
                                "No hay flujo de calor: solo cambia la temperatura",
                            ],
                            "correct": 1,
                        },
                    },
                },
            ],
        },
        # ==================== NIVEL 4 ====================
        {
            "slug": "f-ondas-sonido",
            "title": "11. Oscilaciones, ondas, sonido y efecto Doppler",
            "level": 4,
            "order_index": 11,
            "summary": "Péndulos y resortes (MAS), v = f·λ, acústica en guitarra, distancia a una tormenta y efecto Doppler.",
            "prerequisites": ["f-trabajo-energia"],
            "metadata": {"section": "Fluidos, calor y ondas", "lab_tab": "waves", "est_minutes": 25},
            "items": [
                {
                    "item_type": "recall",
                    "title": "Frecuencia vs. Amplitud en sonido",
                    "prompt": "En una cuerda de guitarra, ¿qué percibe tu oído cuando cambia la frecuencia vs. cuando cambia la amplitud?",
                    "answer": "La frecuencia (Hz) define la altura musical (grave o agudo); la amplitud define el volumen.",
                    "hints": ["Tocar más fuerte no cambia la nota."],
                    "payload": {
                        "lab_link": "physics:waves",
                        "check": {
                            "type": "choice",
                            "options": [
                                "Frecuencia → altura (grave o agudo); amplitud → volumen",
                                "Frecuencia → volumen; amplitud → altura (grave o agudo)",
                                "Las dos cambian la altura de la nota",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "El péndulo de una hamaca: ¿importa el peso?",
                    "prompt": "Un niño de 25 kg y un adulto de 80 kg se hamacan en dos hamacas con cadenas del MISMO largo. ¿Quién va y vuelve más rápido (menor período T = 2π√(L/g))?",
                    "answer": "Oscilan exactamente al mismo ritmo: el período de un péndulo depende del largo L y de la gravedad g, NO de la masa colgada.",
                    "hints": ["Fijate si la masa m aparece en T = 2π√(L/g)."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "El adulto, porque pesa más y baja más rápido",
                                "El niño, porque es más liviano",
                                "Oscilan al mismo ritmo: el período solo depende del largo L y de g",
                            ],
                            "correct": 2,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Efecto Doppler: la sirena de la ambulancia",
                    "prompt": "Una ambulancia pasa a toda velocidad frente a vos. ¿Por qué escuchás la sirena más aguda cuando se acerca y de golpe más grave cuando se aleja?",
                    "answer": "Al acercarse comprime las crestas de sonido (menor λ, mayor frecuencia → más agudo); al alejarse las estira (mayor λ, menor frecuencia → más grave). El conductor escucha siempre la misma nota.",
                    "hints": ["Pensá en cómo se juntan o se separan las ondas delante y detrás de un objeto en movimiento."],
                    "payload": {
                        "lab_link": "physics:waves",
                        "check": {
                            "type": "choice",
                            "options": [
                                "Al acercarse comprime las ondas (mayor frecuencia = agudo) y al alejarse las estira (menor frecuencia = grave)",
                                "Porque el sonido viaja más rápido cuando la ambulancia viene hacia vos",
                                "Porque el volumen más alto hace que el oído perciba notas más agudas",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Calcular a qué distancia cayó un rayo",
                    "prompt": "Ves el relámpago (la luz llega casi al instante) y 6 segundos después escuchás el trueno (v_sonido ≈ 340 m/s). ¿A cuántos metros cayó el rayo? Respondé solo con el número en m.",
                    "answer": "d = v · t = 340 · 6 = 2040 m (~2 km). Regla práctica de tormenta: dividí los segundos por 3 y te da los kilómetros aproximados.",
                    "hints": ["Distancia = velocidad del sonido × tiempo."],
                    "payload": {"check": {"type": "numeric", "value": 2040, "tolerance": 0.03, "unit": "m"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Relación de octava y longitud de cuerda",
                    "prompt": "La 5ª cuerda de guitarra vibra a 110 Hz (La2). Al pisar el traste 12 (mitad exacta de la cuerda), ¿qué frecuencia emite? Respondé solo con el número en Hz.",
                    "answer": "220 Hz (La3, una octava exacta arriba).",
                    "hints": ["Mitad de longitud de onda → doble de frecuencia."],
                    "payload": {
                        "lab_link": "physics:waves",
                        "check": {"type": "numeric", "value": 220, "tolerance": 0, "unit": "Hz"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Período a partir de la frecuencia",
                    "prompt": "La corriente eléctrica domiciliaria oscila a f = 50 Hz. ¿Cuánto dura cada ciclo completo (período T)? Respondé solo con el número en s.",
                    "answer": "T = 1 / f = 1 / 50 = 0.02 s (20 milisegundos).",
                    "hints": ["T = 1 / f."],
                    "payload": {
                        "lab_link": "physics:waves",
                        "check": {"type": "numeric", "value": 0.02, "tolerance": 0.02, "unit": "s"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Longitud de onda con v = f · λ",
                    "prompt": "El sonido viaja a 340 m/s en el aire. ¿Qué longitud de onda tiene una nota de 680 Hz? Respondé solo con el número en m.",
                    "answer": "λ = v / f = 340 / 680 = 0.5 m.",
                    "hints": ["Despejá λ de v = f · λ."],
                    "payload": {
                        "lab_link": "physics:waves",
                        "check": {"type": "numeric", "value": 0.5, "tolerance": 0.02, "unit": "m"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Frecuencia de un armónico",
                    "prompt": "La fundamental de una cuerda es 110 Hz. ¿Qué frecuencia tiene su armónico n = 3? Respondé solo con el número en Hz.",
                    "answer": "f₃ = 3 · 110 = 330 Hz.",
                    "hints": ["Multiplicá la fundamental por n."],
                    "payload": {
                        "lab_link": "physics:waves",
                        "check": {"type": "numeric", "value": 330, "tolerance": 0, "unit": "Hz"},
                    },
                },
            ],
        },
        {
            "slug": "f-electricidad-campos",
            "title": "12. Carga eléctrica, campo eléctrico y circuitos",
            "level": 4,
            "order_index": 12,
            "summary": "Ley de Coulomb (1/r²), significado físico de Voltio/Amperio/Watt, circuitos serie/paralelo en casa y baterías.",
            "prerequisites": ["f-trabajo-energia"],
            "metadata": {"section": "Electricidad y óptica", "lab_tab": "ohm", "est_minutes": 25},
            "items": [
                {
                    "item_type": "recall",
                    "title": "Significado físico de Voltio, Amperio y Watt",
                    "prompt": "Definí físicamente 1 Amperio, 1 Voltio y 1 Watt en términos de Coulombs, Joules y segundos.",
                    "answer": "1 A = 1 C/s (caudal de carga); 1 V = 1 J/C (energía por carga); 1 W = 1 J/s = V · I (potencia).",
                    "hints": ["(J/C) × (C/s) = J/s = Watts."],
                    "payload": {
                        "lab_link": "electronics:ohm",
                        "check": {
                            "type": "choice",
                            "options": [
                                "1 A = 1 C/s; 1 V = 1 J/C; 1 W = 1 J/s",
                                "1 A = 1 J/C; 1 V = 1 C/s; 1 W = 1 J/s",
                                "1 A = 1 C/s; 1 V = 1 J/s; 1 W = 1 J/C",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Ley de Coulomb: alejar dos cargas el triple",
                    "prompt": "La fuerza eléctrica entre dos cargas sigue F = k · q₁·q₂ / r². Si triplicás la distancia entre ellas (3r), ¿por qué factor se divide la fuerza? Respondé solo con el número.",
                    "answer": "Se divide por 9 (3² = 9): igual que la gravedad, el campo eléctrico de una carga puntual cae con el cuadrado de la distancia.",
                    "hints": ["Elevá el factor de distancia al cuadrado."],
                    "payload": {"check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": "×"}},
                },
                {
                    "item_type": "recall",
                    "title": "Por qué los enchufes de tu casa van en paralelo (y saltan las térmicas)",
                    "prompt": "Enchufás un caloventor y una pava eléctrica a la misma zapatilla (conexión en paralelo a 220 V) y salta la llave térmica. ¿Qué pasó con la corriente total del cable?",
                    "answer": "En paralelo cada aparato recibe 220 V completos, y sus corrientes se SUMAN en el cable principal (I_total = I₁ + I₂). Al superar el límite del cable, la térmica corta para evitar un incendio.",
                    "hints": ["En paralelo cada rama agrega un nuevo camino para la corriente."],
                    "payload": {
                        "lab_link": "electronics:ohm",
                        "check": {
                            "type": "choice",
                            "options": [
                                "Las corrientes de ambos aparatos se suman en el cable principal y superan el límite seguro",
                                "El voltaje sube de 220 V a 440 V al conectar dos cosas",
                                "La resistencia total del circuito se vuelve infinita",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Qué viaja rápido en un cable eléctrico",
                    "prompt": "Cuando prendés la luz de tu cuarto, ¿son los electrones individuales los que viajan a la velocidad de la luz hasta la lámpara?",
                    "answer": "No: los electrones avanzan a milímetros por segundo; lo que viaja casi a la velocidad de la luz es el campo eléctrico que empuja a todos los electrones del cable casi a la vez.",
                    "hints": ["Pensá en una manguera ya llena de agua."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Sí: cada electrón recorre el cable casi a la velocidad de la luz",
                                "No: los electrones avanzan a mm/s; lo que se propaga casi a la velocidad de la luz es el campo eléctrico",
                                "No: nada se mueve hasta que la lámpara se calienta",
                            ],
                            "correct": 1,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Potencia eléctrica P = V · I",
                    "prompt": "Un cargador rápido entrega 9 V y 2 A a tu celular. ¿Qué potencia suministra? Respondé solo con el número en W.",
                    "answer": "P = V · I = 9 · 2 = 18 W (18 joules cada segundo).",
                    "hints": ["Multiplicá voltaje por corriente."],
                    "payload": {
                        "lab_link": "electronics:ohm",
                        "check": {"type": "numeric", "value": 18, "tolerance": 0.02, "unit": "W"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Corriente como carga por unidad de tiempo",
                    "prompt": "Por un cable pasan 12 C de carga en 4 s. ¿Qué corriente circula? Respondé solo con el número en A.",
                    "answer": "I = q / t = 12 / 4 = 3 A.",
                    "hints": ["1 A = 1 C/s."],
                    "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0.02, "unit": "A"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Voltaje como energía por unidad de carga",
                    "prompt": "Una batería entrega 18 J de energía a 2 C de carga. ¿Cuál es su voltaje? Respondé solo con el número en V.",
                    "answer": "V = E / q = 18 / 2 = 9 V.",
                    "hints": ["1 V = 1 J/C."],
                    "payload": {"check": {"type": "numeric", "value": 9, "tolerance": 0.02, "unit": "V"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Autonomía de una batería",
                    "prompt": "Un ESP32 consume 150 mA constantes de una batería de 3000 mAh. ¿Cuántas horas dura, en teoría? Respondé solo con el número en h.",
                    "answer": "Autonomía = 3000 mAh / 150 mA = 20 h (en la práctica algo menos por eficiencia).",
                    "hints": ["mAh dividido mA da horas."],
                    "payload": {"check": {"type": "numeric", "value": 20, "tolerance": 0.02, "unit": "h"}},
                },
            ],
        },
        {
            "slug": "f-electromagnetismo",
            "title": "13. Magnetismo, motores e inducción de Faraday",
            "level": 4,
            "order_index": 13,
            "summary": "Electroimanes, fuerza de Lorentz, Ley de Faraday y Lenz, cargadores inalámbricos, transformadores y pastillas de guitarra.",
            "prerequisites": ["f-electricidad-campos"],
            "metadata": {"section": "Electricidad y óptica", "lab_tab": "waves", "est_minutes": 25},
            "items": [
                {
                    "item_type": "recall",
                    "title": "Ley de Faraday y pastillas de guitarra eléctrica",
                    "prompt": "¿Por qué una cuerda metálica vibrando sobre la pastilla de una guitarra eléctrica genera señal, y qué pasa si deja de vibrar?",
                    "answer": "Solo un campo magnético CAMBIANTE induce voltaje en la bobina (Ley de Faraday). Si la cuerda se detiene, el flujo deja de cambiar y el voltaje cae a 0.",
                    "hints": ["La inducción exige variación en el tiempo."],
                    "payload": {
                        "lab_link": "physics:waves",
                        "check": {
                            "type": "choice",
                            "options": [
                                "Porque solo un campo magnético que CAMBIA induce voltaje; si la cuerda se detiene, la señal cae a 0",
                                "Porque la cuerda conduce corriente de la batería; si se detiene, la señal sigue constante",
                                "Porque el imán empuja electrones todo el tiempo; quieta o vibrando, la señal es la misma",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "El vínculo entre corriente y magnetismo",
                    "prompt": "¿Cómo se relacionan un motor eléctrico/parlante con un generador/frenado regenerativo de auto eléctrico?",
                    "answer": "Son procesos inversos: en un motor/parlante la corriente en un campo magnético crea fuerza (Lorentz); en un generador/freno regenerativo el movimiento cambia el flujo magnético e induce electricidad (Faraday) devolviendo carga a la batería.",
                    "hints": ["Electricidad ↔ Movimiento a través del magnetismo."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Son el mismo proceso: en los dos la electricidad produce movimiento",
                                "No tienen relación: uno es eléctrico y el otro magnético",
                                "Son procesos inversos: el motor convierte electricidad en fuerza; el generador convierte movimiento en electricidad",
                            ],
                            "correct": 2,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Transformador de cargador (relación de vueltas)",
                    "prompt": "Un transformador ideal recibe 220 V en su bobina primaria de 1100 vueltas. Si la bobina secundaria tiene 55 vueltas (20 veces menos), ¿qué voltaje alterno entrega? Respondé solo con el número en V.",
                    "answer": "V₂ / V₁ = N₂ / N₁ → V₂ = 220 · (55 / 1100) = 220 / 20 = 11 V (y solo funciona con corriente alterna, porque Faraday necesita un campo cambiante).",
                    "hints": ["El voltaje baja en la misma proporción que el número de vueltas."],
                    "payload": {"check": {"type": "numeric", "value": 11, "tolerance": 0.02, "unit": "V"}},
                },
                {
                    "item_type": "recall",
                    "title": "¿Por qué un cargador inalámbrico (Qi) necesita corriente alterna?",
                    "prompt": "Al apoyar tu celular en una base de carga inalámbrica no hay contacto metálico. ¿Por qué la bobina de la base usa corriente alterna de alta frecuencia en lugar de corriente continua fija?",
                    "answer": "Porque una corriente continua fija crea un campo magnético estático y no induce nada en la bobina del celular; la corriente alterna genera un campo cambiante que induce corriente por la Ley de Faraday.",
                    "hints": ["Recordá qué necesita la Ley de Faraday para inducir voltaje."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Porque solo una corriente cambiante genera un campo magnético variable que induce voltaje en el celular",
                                "Porque la corriente continua no atraviesa el plástico de la funda",
                                "Porque las baterías de litio solo cargan con corriente alterna",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "¿Electricidad → movimiento o movimiento → electricidad?",
                    "prompt": "¿Cuál de estos dispositivos convierte electricidad en movimiento?",
                    "answer": "El parlante: la corriente variable en la bobina dentro del imán produce fuerza (Lorentz) que hace vibrar el cono y empuja el aire.",
                    "hints": ["Pensá cuál recibe señal eléctrica y mueve algo físico."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": ["La pastilla de una guitarra eléctrica", "Un generador", "Un parlante"],
                            "correct": 2,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Frecuencia de la señal de una pastilla",
                    "prompt": "La 6ª cuerda de una guitarra eléctrica vibra a 82 Hz sobre la pastilla. ¿De qué frecuencia es la señal eléctrica inducida? Respondé solo con el número en Hz.",
                    "answer": "82 Hz: la corriente inducida copia el ritmo exacto con que la cuerda perturba el campo magnético.",
                    "hints": ["El campo magnético varía al mismo ritmo que la cuerda."],
                    "payload": {
                        "lab_link": "physics:waves",
                        "check": {"type": "numeric", "value": 82, "tolerance": 0.01, "unit": "Hz"},
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Cuándo hay inducción en una bobina",
                    "prompt": "¿En cuál de estos casos se induce voltaje en una bobina?",
                    "answer": "Solo cuando el imán entra y sale: el flujo magnético debe cambiar en el tiempo.",
                    "hints": ["Importa el cambio, no la potencia estática del imán."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Un imán muy potente apoyado quieto sobre la bobina",
                                "Un imán entrando y saliendo de la bobina",
                                "Un imán quieto adentro de la bobina",
                            ],
                            "correct": 1,
                        },
                    },
                },
            ],
        },
        # ==================== NIVEL 5 ====================
        {
            "slug": "f-ondas-em",
            "title": "14. Ondas electromagnéticas, luz e interferencia",
            "level": 5,
            "order_index": 14,
            "summary": "El espectro EM (radio, Wi-Fi, microondas, luz, UV, rayos X), c = f·λ, polarización e interferencia.",
            "prerequisites": ["f-ondas-sonido", "f-electromagnetismo"],
            "metadata": {"section": "Electricidad y óptica", "lab_tab": "waves", "est_minutes": 20},
            "items": [
                {
                    "item_type": "recall",
                    "title": "Ordenar el espectro electromagnético por frecuencia",
                    "prompt": "Ordená estas ondas electromagnéticas de MENOR frecuencia (ondas más largas, menos energía) a MAYOR frecuencia (más energía).",
                    "answer": "Radio/Wi-Fi → Infrarrojo (control remoto/calor) → Luz visible → Ultravioleta (UV) → Rayos X. Todas son la misma física viajando a c = 300 000 km/s; solo cambia su frecuencia.",
                    "hints": ["Radio/Wi-Fi son las más largas y suaves; los rayos X son los más energéticos."],
                    "payload": {
                        "check": {
                            "type": "order",
                            "lines": [
                                "Ondas de radio y Wi-Fi",
                                "Infrarrojo (calor y control remoto)",
                                "Luz visible",
                                "Ultravioleta (UV) y Rayos X",
                            ],
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Longitud de onda del Wi-Fi de 2.4 GHz",
                    "prompt": "Las ondas del Wi-Fi viajan a c = 3 × 10⁸ m/s con f = 2.4 × 10⁹ Hz. ¿Cuánto mide su longitud de onda λ = c / f? Respondé solo con el número en cm.",
                    "answer": "λ = (3 × 10⁸) / (2.4 × 10⁹) = 0.125 m = 12.5 cm (por eso las antenas de router suelen medir unos 6 cm = media onda o ~3 cm = cuarto de onda).",
                    "hints": ["Dividí 3 por 2.4 (da 1.25) y restá exponentes (10⁸ / 10⁹ = 0.1): 1.25 × 0.1 m. Después pasalo a cm."],
                    "payload": {
                        "lab_link": "physics:waves",
                        "check": {"type": "numeric", "value": 12.5, "tolerance": 0.03, "unit": "cm"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Longitud de onda de una radio FM",
                    "prompt": "Sintonizás una radio FM en 100 MHz (1 × 10⁸ Hz). Con c = 3 × 10⁸ m/s, ¿cuánto mide su longitud de onda λ? Respondé solo con el número en m.",
                    "answer": "λ = (3 × 10⁸) / (1 × 10⁸) = 3 m. Las ondas tan largas rodean edificios mucho mejor que las de 5 GHz.",
                    "hints": ["Los 10⁸ arriba y abajo se cancelan."],
                    "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0.02, "unit": "m"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Retardo de la señal entre la Tierra y la Luna",
                    "prompt": "La Luna está a unos 384 000 km de la Tierra y las señales de radio viajan a c = 300 000 km/s. ¿Cuántos segundos tarda un mensaje de voz en llegar (solo ida)? Respondé solo con el número en s.",
                    "answer": "t = d / c = 384 000 / 300 000 = 1.28 s (casi 2.6 s ida y vuelta; con Marte puede tardar entre 4 y 22 minutos).",
                    "hints": ["Dividí distancia por velocidad de la luz."],
                    "payload": {"check": {"type": "numeric", "value": 1.28, "tolerance": 0.05, "unit": "s"}},
                },
                {
                    "item_type": "recall",
                    "title": "Cómo eliminan el reflejo los anteojos de sol polarizados",
                    "prompt": "¿Por qué los anteojos polarizados reducen muchísimo el encandilamiento del sol reflejado en el asfalto mojado o el agua?",
                    "answer": "La luz reflejada en superficies horizontales queda polarizada horizontalmente; el filtro polarizado vertical de los anteojos bloquea justo esa dirección de oscilación del campo eléctrico.",
                    "hints": ["Es como una reja vertical frente a una cuerda que vibra en horizontal."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Bloquean la luz que oscila en horizontal (la del reflejo) dejando pasar el resto",
                                "Frenan la velocidad de la luz a la mitad",
                                "Reflejan únicamente el color azul del cielo",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Colores arcoíris en una burbuja de jabón",
                    "prompt": "El agua jabonosa es transparente, pero una burbuja muestra bandas de colores brillantes que cambian al moverse. ¿Qué fenómeno ondulatorio lo produce?",
                    "answer": "Interferencia en películas delgadas: la luz reflejada en la cara externa e interna de la película se suma (refuerza) para ciertos colores y se cancela para otros según el espesor.",
                    "hints": ["Dos reflejos de la misma onda se superponen constructiva o destructivamente."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Interferencia entre la luz reflejada en la cara exterior e interior de la burbuja",
                                "El jabón contiene pigmentos microscópicos de todos los colores",
                                "Efecto Doppler producido por el aire adentro de la burbuja",
                            ],
                            "correct": 0,
                        },
                    },
                },
            ],
        },
        {
            "slug": "f-optica-luz",
            "title": "15. Óptica geométrica: espejos, refracción y lentes",
            "level": 5,
            "order_index": 15,
            "summary": "Reflexión, Ley de Snell, fibra óptica (reflexión interna total), lentes (1/f = 1/do + 1/di), ojo humano y cámaras.",
            "prerequisites": ["f-ondas-em"],
            "metadata": {"section": "Electricidad y óptica", "lab_tab": "optics", "est_minutes": 25},
            "items": [
                {
                    "item_type": "worked_example",
                    "title": "Velocidad de la luz dentro de una fibra óptica de vidrio",
                    "prompt": "El vidrio tiene índice de refracción n = 1.5 (v = c / n). Si c = 300 000 km/s en el vacío, ¿a cuántos km/s viaja tu conexión de internet dentro de la fibra óptica? Respondé solo con el número en km/s.",
                    "answer": "v = 300 000 / 1.5 = 200 000 km/s. Al cambiar de velocidad al pasar de un medio a otro es que el rayo de luz se quiebra (refracción).",
                    "hints": ["Dividí c por el índice de refracción n."],
                    "payload": {
                        "lab_link": "physics:optics",
                        "check": {"type": "numeric", "value": 200000, "tolerance": 0.02, "unit": "km/s"},
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Cómo viaja internet doblando esquinas por fibra óptica",
                    "prompt": "La luz viaja en línea recta, pero un cable de fibra óptica dobla esquinas sin que se escape la señal. ¿Qué fenómeno óptico mantiene la luz atrapada adentro?",
                    "answer": "Reflexión interna total: cuando la luz intenta pasar de un medio más denso ópticamente (vidrio, n=1.5) a uno menos denso (revestimiento/aire) con un ángulo mayor al ángulo crítico, rebota al 100% hacia adentro como en un espejo perfecto.",
                    "hints": ["Probalo en el Laboratorio de Física → Óptica poniendo Vidrio → Aire y subiendo el ángulo."],
                    "payload": {
                        "lab_link": "physics:optics",
                        "check": {
                            "type": "choice",
                            "options": [
                                "Reflexión interna total al superar el ángulo crítico dentro del vidrio",
                                "La fibra tiene imanes que doblan el haz de luz",
                                "Difracción producida por el plástico negro exterior",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Por qué una pileta parece menos profunda de lo que es",
                    "prompt": "Mirás el fondo de una pileta desde afuera y parece mucho menos profunda de lo real (o una bombilla en un vaso parece quebrada). ¿Por qué?",
                    "answer": "Por refracción (Ley de Snell): al salir del agua (n=1.33) al aire (n=1.00), la luz acelera y se aleja de la normal; tu cerebro proyecta el rayo en línea recta hacia atrás y ve el fondo más arriba.",
                    "hints": ["El rayo se dobla al cambiar de velocidad entre agua y aire."],
                    "payload": {
                        "lab_link": "physics:optics",
                        "check": {
                            "type": "choice",
                            "options": [
                                "Porque el agua absorbe la luz que viene de mayor profundidad",
                                "Por refracción: los rayos se desvían al pasar del agua al aire y tu cerebro los proyecta rectos",
                                "Por reflexión interna total en la superficie",
                            ],
                            "correct": 1,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Ecuación de lentes delgadas (proyector / cámara)",
                    "prompt": "Colocás un objeto a d_o = 30 cm frente a una lente convergente de distancia focal f = 10 cm. Usando 1/f = 1/d_o + 1/d_i, ¿a qué distancia d_i se forma la imagen nítida? Respondé solo con el número en cm.",
                    "answer": "1/d_i = 1/10 − 1/30 = 3/30 − 1/30 = 2/30 = 1/15 → d_i = 15 cm.",
                    "hints": ["Restá 1/10 − 1/30 y después invertí la fracción."],
                    "payload": {
                        "lab_link": "physics:optics",
                        "check": {"type": "numeric", "value": 15, "tolerance": 0.02, "unit": "cm"},
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Anteojos para miopía: ¿convergente o divergente?",
                    "prompt": "En un ojo con miopía, la imagen de los objetos lejanos se enfoca ANTES de llegar a la retina. ¿Qué tipo de lente corrige la miopía?",
                    "answer": "Una lente DIVERGENTE (cóncava): abre ligeramente los rayos antes de entrar al ojo para empujar el punto de enfoque hacia atrás, justo sobre la retina.",
                    "hints": ["El ojo ya enfoca 'demasiado rápido': hay que abrir un poco los rayos."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Lente divergente (abre un poco los rayos para que enfoquen más atrás, en la retina)",
                                "Lente convergente (junta aún más rápido los rayos)",
                                "Un espejo plano",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "El espejo retrovisor derecho del auto",
                    "prompt": "Los espejos laterales convexos de los autos advierten 'los objetos están más cerca de lo que parecen'. ¿Por qué se usan igual?",
                    "answer": "Porque un espejo convexo forma imágenes más pequeñas pero amplía muchísimo el campo de visión, reduciendo el punto ciego al cambiar de carril.",
                    "hints": ["Pensá qué ventaja de seguridad da ver un ángulo más ancho."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Agranda el campo de visión reduciendo el punto ciego, a costa de mostrar imágenes más chicas",
                                "Hace que los autos de atrás se vean más grandes y fáciles de distinguir",
                                "Elimina los reflejos nocturnos por polarización",
                            ],
                            "correct": 0,
                        },
                    },
                },
            ],
        },
        {
            "slug": "f-relatividad",
            "title": "16. Relatividad especial: tiempo, espacio y E = mc²",
            "level": 5,
            "order_index": 16,
            "summary": "Constancia de la velocidad de la luz, dilatación del tiempo en satélites GPS, contracción espacial y E = mc².",
            "prerequisites": ["f-cinematica", "f-ondas-em"],
            "metadata": {"section": "Física moderna", "lab_tab": "kinematics", "est_minutes": 20},
            "items": [
                {
                    "item_type": "recall",
                    "title": "Las luces de una nave a mitad de la velocidad de la luz",
                    "prompt": "Una nave espacial viaja hacia vos a 0.5 c (la mitad de la velocidad de la luz) y prende sus faros delanteros. ¿A qué velocidad medís vos llegar esa luz?",
                    "answer": "Exactamente a c (1.0 c). El segundo postulado de Einstein dice que la luz en el vacío SIEMPRE viaja a c para cualquier observador, sin sumarse con la velocidad de la fuente.",
                    "hints": ["Las velocidades de la luz NO se suman como pelotas tiradas desde un tren."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "A 1.5 c (se suma la velocidad de la nave y la de la luz)",
                                "A exactamente c (siempre igual para cualquier observador)",
                                "A 0.5 c",
                            ],
                            "correct": 1,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Por qué tu GPS del celular depende de Einstein",
                    "prompt": "Los satélites GPS orbitan a ~14 000 km/h (y además están más lejos de la gravedad terrestre). ¿Qué pasaría con Google Maps si los relojes atómicos del GPS no corrigieran la relatividad?",
                    "answer": "Los relojes se desfasarían unos 38 microsegundos por día; multiplicado por la velocidad de la luz, tu ubicación en el mapa acumularía más de 11 kilómetros de error CADA DÍA.",
                    "hints": ["Un error de 1 microsegundo en una señal a velocidad c equivale a 300 metros."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Nada notable: los efectos relativistas solo importan cerca de agujeros negros",
                                "La posición acumularía kilómetros de error cada día por desfase de los relojes",
                                "Los satélites caerían a la Tierra por perder gravedad",
                            ],
                            "correct": 1,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Dilatación del tiempo a 0.6 c (factor de Lorentz)",
                    "prompt": "El factor de dilatación es γ = 1 / √(1 − v²/c²). Para una nave a v = 0.6 c (0.6² = 0.36 → √0.64 = 0.8), si adentro pasan 4 años para la tripulación, ¿cuántos años pasan en la Tierra (Δt = γ · Δt₀)? Respondé solo con el número en años.",
                    "answer": "γ = 1 / 0.8 = 1.25. Entonces Δt = 1.25 · 4 = 5 años en la Tierra mientras los astronautas envejecieron solo 4 años.",
                    "hints": ["Dividí 4 por 0.8 (o multiplicalo por 1.25)."],
                    "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0.02, "unit": "años"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Contracción de la longitud a 0.8 c",
                    "prompt": "Una nave mide L₀ = 100 m en reposo y pasa frente a una estación a v = 0.8 c (√(1 − 0.8²) = √0.36 = 0.6). ¿Qué largo le miden desde la estación al verla pasar (L = L₀ · 0.6)? Respondé solo con el número en m.",
                    "answer": "L = 100 · 0.6 = 60 m en la dirección del movimiento. Para los viajeros adentro, la nave sigue midiendo 100 m y lo que se acorta es la distancia hasta su destino.",
                    "hints": ["Multiplicá el largo propio por √(1 − v²/c²) = 0.6."],
                    "payload": {"check": {"type": "numeric", "value": 60, "tolerance": 0.02, "unit": "m"}},
                },
                {
                    "item_type": "recall",
                    "title": "Qué significa realmente E = m · c²",
                    "prompt": "¿Qué expresa la famosa ecuación E = m · c² y cómo explica por qué brilla el Sol?",
                    "answer": "Que la masa es una forma ultra concentrada de energía (multiplicada por c² = 9 × 10¹⁶). En el Sol, la fusión nuclear convierte una pequeñísima fracción de masa en una cantidad colosal de luz y calor.",
                    "hints": ["La masa y la energía son equivalentes; c² es un factor gigantesco."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Que la masa es energía concentrada: convertir una mínima masa libera una energía gigantesca",
                                "Que un objeto solo tiene energía si viaja a la velocidad de la luz",
                                "Que la luz tiene mucha masa cuando se frena",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Por qué un objeto con masa no puede alcanzar la velocidad c",
                    "prompt": "En aceleradores como el LHC del CERN llevan protones al 99.999999% de c, pero jamás llegan a 100% de c. ¿Por qué?",
                    "answer": "Porque a medida que v se acerca a c, el factor γ tiende a infinito y la energía necesaria para seguir acelerando también tiende a infinito. Solo partículas sin masa (como los fotones) viajan a c.",
                    "hints": ["Mirá el denominador √(1 − v²/c²) cuando v → c."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Por la fricción del aire residual dentro del acelerador",
                                "Porque al acercarse a c la energía requerida para acelerar crece hacia infinito",
                                "Porque los protones se evaporan al llegar a 0.99 c",
                            ],
                            "correct": 1,
                        },
                    },
                },
            ],
        },
        {
            "slug": "f-cuantica-nuclear",
            "title": "17. Física cuántica y nuclear: fotones, LEDs y átomos",
            "level": 5,
            "order_index": 17,
            "summary": "Fotones (E = hf), efecto fotoeléctrico (paneles solares), niveles cuánticos (LEDs), vida media (C-14) y fisión/fusión.",
            "prerequisites": ["f-optica-luz"],
            "metadata": {"section": "Física moderna", "lab_tab": "optics", "est_minutes": 25},
            "items": [
                {
                    "item_type": "recall",
                    "title": "Efecto fotoeléctrico: luz roja intensa vs. violeta débil",
                    "prompt": "Iluminás una placa metálica con un reflector rojo potentísimo y no salta ni un electrón; en cambio con una linternita violeta muy débil sí saltan electrones. ¿Por qué?",
                    "answer": "La luz llega en paquetes (fotones) con energía E = h·f. Un fotón rojo tiene poca frecuencia y no alcanza la energía mínima para arrancar un electrón, por más que mandes millones; cada fotón violeta sí supera ese umbral.",
                    "hints": ["La energía de CADA fotón depende de la frecuencia (color), no del brillo."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Cada fotón violeta tiene más frecuencia y energía (E = h·f) y supera el umbral; el brillo solo suma más fotones sin energía suficiente",
                                "La luz roja viaja más lento que la violeta",
                                "El metal solo absorbe colores fríos",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Por qué un LED azul necesita más voltaje que un LED rojo",
                    "prompt": "En electrónica, un LED rojo enciende cerca de ~1.8 V, mientras que un LED azul o blanco necesita ~3.0 V. ¿Cuál es la razón cuántica?",
                    "answer": "La luz azul tiene mayor frecuencia que la roja, así que cada fotón azul lleva más energía (E = h·f). El salto cuántico en el semiconductor debe ser más grande y requiere más energía por electrón (más Voltios).",
                    "hints": ["Un Voltio es energía por carga; luz más azul = fotones más energéticos."],
                    "payload": {
                        "lab_link": "electronics:ohm",
                        "check": {
                            "type": "choice",
                            "options": [
                                "Los fotones azules tienen mayor frecuencia y energía (E = h·f), exigiendo un salto cuántico más alto",
                                "El plástico azul del LED deja pasar menos corriente",
                                "Los LEDs azules tienen más resistencia en las patitas",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Energía de un fotón al duplicar la frecuencia",
                    "prompt": "Un fotón infrarrojo tiene energía de 1.5 eV. ¿Qué energía (en eV) tiene un fotón con el DOBLE de frecuencia (E = h · f)? Respondé solo con el número en eV.",
                    "answer": "3 eV: la energía de un fotón es directamente proporcional a su frecuencia.",
                    "hints": ["E = h · f es lineal con f."],
                    "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0.02, "unit": "eV"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Vida media y datación por Carbono-14",
                    "prompt": "Un material radiactivo tiene una vida media de 5730 años (cada 5730 años queda la mitad). Si pasan 3 vidas medias (17 190 años), ¿qué porcentaje del Carbono-14 original queda? Respondé solo con el número en %.",
                    "answer": "100% → 50% (1ª) → 25% (2ª) → 12.5% (3ª vida media). Así los arqueólogos fechan fósiles y madera antigua.",
                    "hints": ["Dividí 100 por 2 tres veces seguidas."],
                    "payload": {"check": {"type": "numeric", "value": 12.5, "tolerance": 0.02, "unit": "%"}},
                },
                {
                    "item_type": "recall",
                    "title": "Espectros atómicos: por qué cada gas brilla de un color propio",
                    "prompt": "¿Por qué un tubo de neón brilla naranja-rojo y los astrónomos pueden saber de qué elementos está hecha una estrella a millones de años luz?",
                    "answer": "Porque los electrones de cada átomo solo pueden ocupar niveles de energía discretos (cuantizados). Al bajar de nivel emiten fotones con frecuencias únicas: una 'huella digital' luminosa de cada elemento.",
                    "hints": ["Los niveles de energía son escalones fijos, no una rampa continua."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Cada elemento tiene escalones cuánticos únicos y emite solo frecuencias específicas de luz",
                                "Porque cada gas vibra con una temperatura distinta",
                                "Por la reflexión de la luz solar sobre los gases",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Fisión nuclear (centrales) vs. Fusión nuclear (Sol)",
                    "prompt": "¿Cuál es la diferencia entre fisión nuclear y fusión nuclear?",
                    "answer": "Fisión es PARTIR núcleos pesados (como uranio) en núcleos más livianos (usada en centrales nucleares actuales). Fusión es UNIR núcleos livianos (hidrógeno → helio), la fuente de energía del Sol y las estrellas.",
                    "hints": ["Fisión = fisura/partir; Fusión = fundir/unir."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Fisión parte núcleos pesados; fusión une núcleos livianos como en el Sol",
                                "Fisión une átomos; fusión los parte",
                                "Son dos nombres para la misma reacción química",
                            ],
                            "correct": 0,
                        },
                    },
                },
            ],
        },
    ],
}


PHYSICS_LESSONS: dict[str, dict] = {
    # ==================== NIVEL 1 ====================
    "f-intro-fisica": {
        "hook": {
            "question": "¿Hace falta ser un genio en matemáticas para entender física, o ya la venís usando sin darte cuenta cada día?",
            "intuition": "Cada vez que atajás unas llaves en el aire, doblás en bici inclinándote hacia adentro o dejás enfriar un café, tu cerebro ya está aplicando física por instinto. Estudiar física desde cero no es memorizar fórmulas raras: es descubrir las reglas simples que explican todo eso y aprender a predecirlo con precisión.",
        },
        "concept": {
            "points": [
                "**¿Qué estudia la física?** Busca las reglas más fundamentales del universo: cómo se mueven las cosas, por qué funcionan la electricidad, el calor, el sonido y la luz. Sobre esas reglas se apoyan la química, la biología y toda la ingeniería.",
                "**Pensar con modelos (simplificar primero)**: el mundo real tiene mil detalles a la vez (viento, rozamiento, formas raras). Por eso en física primero aislamos lo esencial —por ejemplo, estudiar una caída sin aire— y después vamos sumando los detalles reales.",
                "**Medir con unidades estándar (SI) y prefijos**: un número suelto no dice nada (`10` ¿qué? ¿metros, segundos o kilos?). Usamos **metros (`m`)**, **kilogramos (`kg`)** y **segundos (`s`)**, y tres prefijos diarios: **kilo (`k`) = ×1000**, **centi (`c`) = ÷100**, **mili (`m`) = ÷1000**.",
                "**Leer fórmulas como recetas y usar el sentido común**: una fórmula como `distancia = velocidad × tiempo` no se aprende de memoria; se lee como causa y efecto (doble tiempo → doble distancia). Y al terminar cualquier cuenta, preguntate siempre: *¿tiene sentido este número en la vida real?*",
            ],
            "real_world": [
                {
                    "title": "Prefijos que ya usás todos los días",
                    "detail": "`2.5 km` son `2500 m`, tu altura de `175 cm` es `1.75 m`, y un LED que toma `20 mA` consume `0.02 A`.",
                },
                {
                    "title": "El detector automático de errores",
                    "detail": "Si calculás la velocidad de una persona caminando y te da `350 m/s` (más rápido que un avión comercial), sabés al instante que mezclaste unidades.",
                },
                {
                    "title": "¿Qué matemática necesito para empezar?",
                    "detail": "Para arrancar solo necesitás multiplicar, dividir y despejar una incógnita simple. Pitágoras y trigonometría aparecen de a poco recién cuando se necesitan.",
                },
            ],
            "key_rule": "Entender qué pasa → Pasar a `m`, `kg`, `s` (`k` ×1000, `c` ÷100, `m` ÷1000) → Aplicar la relación → Chequear sentido común.",
            "pitfall": "Mezclar unidades distintas en la misma cuenta (como multiplicar `m/s` por `minutos` en vez de `segundos`) o copiar un resultado absurdo sin cuestionarlo.",
        },
        "example": {
            "title": "Pensá un trayecto cotidiano paso a paso como un físico",
            "steps": [
                "Situación: caminás a paso normal (`1.5 m/s`) durante `2 minutos` hasta el almacén. ¿A cuántos metros está?",
                "Paso clave de unidades: la velocidad está en `m/s`, así que pasamos los minutos a segundos: `2 min × 60 = 120 s`.",
                "Aplicamos la relación `distancia = velocidad × tiempo = 1.5 × 120 = 180 m`. Chequeo realista: casi 2 cuadras en 2 minutos. Tiene total sentido.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Cuando los físicos dicen 'imaginemos esta caída sin resistencia del aire', ¿por qué lo hacen?",
            "options": [
                {"text": "Para simplificar primero, entender la regla principal (gravedad) y sumar el efecto del aire después", "ok": True, "feedback": "Exacto: así funcionan los modelos científicos, de lo esencial a lo complejo."},
                {"text": "Porque en la Tierra el aire nunca frena a ningún objeto", "ok": False, "feedback": "El aire sí frena (pensá en una hoja de papel o un paracaídas); solo lo dejamos de lado en el primer modelo."},
                {"text": "Porque sin aire no existe la gravedad", "ok": False, "feedback": "La gravedad sigue existiendo igual en el vacío."},
            ],
        },
        "checks": [
            {
                "question": "Medís el ancho de tu escritorio y mide `140 cm`. ¿Cómo se escribe en la unidad estándar del Sistema Internacional (metros)?",
                "options": [
                    {"text": "14 m", "ok": False, "feedback": "Dividiste por 10; 1 metro tiene 100 centímetros (un escritorio de 14 m sería más largo que un colectivo)."},
                    {"text": "1.4 m", "ok": True, "feedback": "Exacto: 140 ÷ 100 = 1.4 m, y además pasa el chequeo de sentido común."},
                    {"text": "14 000 m", "ok": False, "feedback": "Multiplicaste en vez de dividir: eso serían 14 kilómetros."},
                ],
            },
            {
                "question": "Según la relación `distancia = velocidad × tiempo`, si mantenés la misma velocidad pero caminás el TRIPLE de tiempo, ¿qué pasa con la distancia?",
                "options": [
                    {"text": "Se triplica también", "ok": True, "feedback": "Exacto: leíste la fórmula como relación causa-efecto sin hacer ninguna cuenta rara."},
                    {"text": "Se divide por tres", "ok": False, "feedback": "Si caminás más tiempo a igual ritmo, avanzás más distancia, no menos."},
                    {"text": "Queda exactamente igual", "ok": False, "feedback": "La distancia crece proporcionalmente al tiempo."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras qué estudia la física y cuál es la ventaja de usar modelos simples y unidades estándar.",
    },
    "f-magnitudes-vectores": {
        "hook": {
            "question": "Si caminás 3 cuadras al este y 4 cuadras al norte, caminaste 7 cuadras… pero ¿a cuántas cuadras reales estás de tu casa?",
            "intuition": "A solo 5 cuadras en diagonal. En física, decir 'cuánto' sin decir 'hacia dónde' suele dejar la historia a medias: por eso separamos escalares (solo número) de vectores (número + dirección).",
        },
        "concept": {
            "points": [
                "**Escalar**: queda completo con número y unidad (`22°C`, `5 kg`, `10 s`). No tiene dirección.",
                "**Vector**: necesita tamaño (módulo), dirección y sentido (velocidad, fuerza, aceleración, desplazamiento).",
                "**Sistema Internacional (SI)**: pasá todo a `m`, `kg`, `s`, `A` antes de hacer cuentas. Atajo diario: para pasar de `km/h` a `m/s`, **dividí por 3.6**.",
                "**Descomponer en ejes X/Y**: cualquier vector inclinado `V` con ángulo `θ` respecto al suelo se parte en dos tramos perpendiculares: `Vx = V · cos(θ)` y `Vy = V · sen(θ)`.",
            ],
            "real_world": [
                {
                    "title": "Celular al volante (72 km/h)",
                    "detail": "`72 ÷ 3.6 = 20 m/s`. Mirar una notificación 2 segundos significa avanzar 40 metros a ciegas.",
                },
                {
                    "title": "Un dron con viento cruzado",
                    "detail": "Aunque apuntes el dron derecho al norte, el viento suma un vector lateral y el resultado real es una diagonal (Pitágoras).",
                },
                {
                    "title": "El error de USD 125 millones de la NASA",
                    "detail": "En 1999 la sonda Mars Climate Orbiter se estrelló porque un equipo calculó empuje en libras y otro lo leyó en Newtons (SI).",
                },
            ],
            "key_rule": "Escalar = número + unidad · Vector = magnitud + dirección · `km/h ÷ 3.6 = m/s` · `Vx = V·cos θ`, `Vy = V·sen θ`.",
            "pitfall": "Sumar vectores en distintas direcciones como números comunes (`3 + 4 = 7`), cuando perpendiculares se combinan por Pitágoras (`√(3² + 4²) = 5`).",
        },
        "example": {
            "title": "Descomponé un pase de fútbol en el aire",
            "steps": [
                "Pateás una pelota a `v = 20 m/s` con un ángulo de `60°` respecto al pasto.",
                "¿Qué tan rápido avanza hacia el arco? `Vx = 20 · cos(60°) = 20 · 0.5 = 10 m/s`.",
                "¿Qué tan rápido sube al despegar? `Vy = 20 · sen(60°) ≈ 20 · 0.866 = 17.3 m/s`. Probalo en vivo en el simulador.",
            ],
            "lab_link": "physics:kinematics",
            "lab_cta": "Ver vectores Vx y Vy",
        },
        "check": {
            "question": "¿Cuál de las siguientes parejas contiene únicamente magnitudes VECTORIALES?",
            "options": [
                {"text": "Fuerza y velocidad", "ok": True, "feedback": "Correcto: en ambas importa tanto el tamaño como hacia dónde apuntan."},
                {"text": "Masa y temperatura", "ok": False, "feedback": "Ambas son escalares: no tienen dirección espacial."},
                {"text": "Tiempo y fuerza", "ok": False, "feedback": "El tiempo es escalar."},
            ],
        },
        "checks": [
            {
                "question": "Un repartidor pedalea 600 m al este y después 800 m al norte. ¿A qué distancia en línea recta quedó del punto de partida?",
                "options": [
                    {"text": "1400 m", "ok": False, "feedback": "1400 m es la distancia total pedaleada, no la línea recta entre inicio y fin."},
                    {"text": "1000 m", "ok": True, "feedback": "Exacto: forman ángulo recto, así que √(600² + 800²) = 1000 m."},
                    {"text": "200 m", "ok": False, "feedback": "Solo se restan si van en sentidos opuestos sobre la misma calle."},
                ],
            },
            {
                "question": "Un auto circula a 108 km/h por autopista. ¿Cuántos metros avanza por segundo?",
                "options": [
                    {"text": "30 m/s", "ok": True, "feedback": "Exacto: 108 ÷ 3.6 = 30 m/s."},
                    {"text": "388 m/s", "ok": False, "feedback": "Multiplicaste en vez de dividir por 3.6 (eso sería más rápido que el sonido)."},
                    {"text": "10.8 m/s", "ok": False, "feedback": "1 hora tiene 3600 s y 1 km son 1000 m, así que el factor es 3.6, no 10."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con un ejemplo de la calle por qué no alcanza con decir solo el número en un vector.",
    },
    "f-cinematica": {
        "hook": {
            "question": "Si soltás un martillo y una pluma al mismo tiempo en la Luna (sin aire), ¿cuál llega primero al suelo?",
            "intuition": "Tocan el suelo en el mismo instante. En la Tierra la pluma tarda más solo porque el aire la frena. Sin aire, la gravedad acelera igual a cualquier objeto (`g ≈ 9.81 m/s²` aquí), pese 1 gramo o 1 tonelada.",
        },
        "concept": {
            "points": [
                "**Velocidad (`v`)** mide qué tan rápido cambia tu posición (`m/s`). **Aceleración (`a`)** mide qué tan rápido cambia tu velocidad (`m/s²`).",
                "**Velocidad constante (MRU)**: `x = x₀ + v · t`. **Aceleración constante (MRUV)**: `v = v₀ + a · t` y `x = x₀ + v₀·t + ½·a·t²`.",
                "**Leer gráficas sin memorizar**: en una gráfica `velocidad vs. tiempo`, la **pendiente** es la aceleración y el **área debajo de la curva** es la distancia recorrida.",
                "**Tiro parabólico (2D)**: los dos ejes viven vidas independientes. Horizontalmente `Vx` no cambia nunca; verticalmente la gravedad frena la subida y acelera la bajada.",
            ],
            "real_world": [
                {
                    "title": "Frenada en una avenida",
                    "detail": "A 72 km/h (20 m/s), si tardás 1 s en reaccionar (20 m) y 4 s en frenar (área del triángulo = 40 m), necesitás 60 metros completos para detenerte.",
                },
                {
                    "title": "Deportes con pelota",
                    "detail": "Un tiro libre de fútbol o básquet es una parábola donde `Vx` sigue firme mientras `Vy` baja 9.81 m/s cada segundo hasta llegar a 0 en la cima y caer.",
                },
                {
                    "title": "Medir un pozo con una piedra",
                    "detail": "Soltás una piedra y contás los segundos hasta oír el golpe: `h = ½ · g · t²` (en 2 s cae casi 20 m; en 3 s ya son 44 m).",
                },
            ],
            "key_rule": "Gráfica `v-t`: pendiente = aceleración, área = distancia · Proyectiles: `Vx` constante y `Vy` con gravedad `g`.",
            "pitfall": "Creer que en la cima de un lanzamiento la aceleración es cero: ahí `Vy = 0` un instante, pero la gravedad sigue tirando hacia abajo a `9.81 m/s²`.",
        },
        "example": {
            "title": "Experimentá proyectiles y gravedad en el simulador",
            "steps": [
                "Abrí el Laboratorio de Física → Proyectiles y dispará a `30°` y luego a `60°` con la misma velocidad sin limpiar la pantalla.",
                "Comprobá que ambos caen en el mismo punto (ángulos que suman 90° empatan; `45°` es el máximo) y mirá el vector verde `Vx` congelado.",
                "Cambiá de Tierra (`9.81`) a Luna (`1.62`) y observá cuánto más lejos y más alto vuela el mismo tiro.",
            ],
            "lab_link": "physics:kinematics",
            "lab_cta": "Probar Simulador de Proyectiles",
        },
        "check": {
            "question": "Lanzás una pelota verticalmente hacia arriba. Justo en el punto más alto de su vuelo…",
            "options": [
                {"text": "Su velocidad es 0, pero su aceleración sigue siendo `g = 9.81 m/s²` hacia abajo", "ok": True, "feedback": "Exacto: si la aceleración también fuera 0, se quedaría flotando arriba para siempre."},
                {"text": "Tanto su velocidad como su aceleración son 0", "ok": False, "feedback": "La gravedad nunca se apaga en el punto más alto."},
                {"text": "Su aceleración apunta hacia arriba", "ok": False, "feedback": "La gravedad siempre tira hacia abajo."},
            ],
        },
        "checks": [
            {
                "question": "Un subte acelera parejo de 0 a 20 m/s en 10 s. ¿Qué distancia recorrió en esos 10 s (área del triángulo en la gráfica v-t)?",
                "options": [
                    {"text": "200 m", "ok": False, "feedback": "200 m sería si hubiera ido a 20 m/s desde el inicio; arrancó en 0, así que es la mitad."},
                    {"text": "100 m", "ok": True, "feedback": "Exacto: área del triángulo = ½ · 10 s · 20 m/s = 100 m."},
                    {"text": "2 m", "ok": False, "feedback": "2 m/s² es la aceleración (la pendiente), no la distancia."},
                ],
            },
            {
                "question": "Desde la misma mesa y sin aire, empujás una moneda en horizontal y a la vez soltás otra recta hacia abajo. ¿Cuál toca el piso primero?",
                "options": [
                    {"text": "La que soltaste recta", "ok": False, "feedback": "El movimiento horizontal no frena ni acelera la caída vertical."},
                    {"text": "La empujada, porque sale más rápido", "ok": False, "feedback": "Su velocidad extra es solo horizontal."},
                    {"text": "Llegan al mismo tiempo", "ok": True, "feedback": "Exacto: la caída vertical es independiente del avance horizontal."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué significan la pendiente y el área en una gráfica velocidad-tiempo, y qué pasa arriba de un lanzamiento.",
    },
    # ==================== NIVEL 2 ====================
    "f-leyes-newton": {
        "hook": {
            "question": "Si una nave espacial en el vacío apaga sus motores viajando a 10 000 km/h, ¿se frena sola o sigue para siempre?",
            "intuition": "Sigue eternamente a 10 000 km/h en línea recta. En la Tierra tenemos la falsa intuición de que 'moverse requiere fuerza continua' solo porque el aire y el piso frenan todo por fricción.",
        },
        "concept": {
            "points": [
                "**1ª Ley (Inercia)**: si `F_neta = 0`, lo quieto sigue quieto y lo que se mueve sigue a **velocidad constante** en línea recta.",
                "**2ª Ley (`F_neta = m · a`)**: la fuerza neta no produce velocidad, produce **aceleración**. A mayor masa, más cuesta cambiar su movimiento.",
                "**3ª Ley (Acción y Reacción)**: las fuerzas siempre nacen de a pares iguales y opuestos, pero actúan sobre **dos objetos distintos**, por eso nunca se cancelan.",
                "**Fricción y planos inclinados**: la fricción estática (arrancar un mueble) es mayor que la cinética (deslizarlo). En una rampa inclinada, el peso se divide: una parte aprieta el piso (`mg·cos θ`) y otra desliza cuesta abajo (`mg·sen θ`).",
            ],
            "real_world": [
                {
                    "title": "Frenada brusca en colectivo",
                    "detail": "Tus pies frenan con el piso, pero tu torso sigue hacia adelante por inercia (1ª ley). Por eso existen los cinturones de seguridad.",
                },
                {
                    "title": "Arranque del ascensor",
                    "detail": "Cuando acelera hacia arriba el piso te empuja con más fuerza que tu peso (`N = m(g + a)`) y te sentís más pesado; al bajar, más liviano.",
                },
                {
                    "title": "Rampas de accesibilidad",
                    "detail": "Subir una silla de ruedas por una rampa requiere mucha menos fuerza que levantarla vertical porque solo vencés `mg·sen θ`, no todo el peso `mg`.",
                },
            ],
            "key_rule": "Dibujá primero el Diagrama de Cuerpo Libre · `F_neta = m · a` · Velocidad constante significa `F_neta = 0`.",
            "pitfall": "Pensar que si un auto va a 100 km/h constantes la fuerza del motor supera a la fricción: en realidad están empatadas (`F_neta = 0`).",
        },
        "example": {
            "title": "Probá fricción e inercia en tiempo real",
            "steps": [
                "Abrí el Laboratorio de Física → Fuerzas y elegí superficie **Madera**.",
                "Empujá suavemente por debajo de la fricción máxima: ves que la fricción estática se ajusta sola y `F_neta = 0`.",
                "Cambiá a **Hielo**, dale velocidad al bloque y bajá el empuje a `0 N`: observá la 1ª Ley en acción.",
            ],
            "lab_link": "physics:forces",
            "lab_cta": "Abrir Simulador de Fuerzas y DCL",
        },
        "check": {
            "question": "Empujás una caja por el piso a velocidad CONSTANTE de 2 m/s. ¿Cuánto vale la fuerza NETA sobre la caja?",
            "options": [
                {"text": "Cero: tu empuje empata exactamente a la fricción", "ok": True, "feedback": "Exacto: velocidad constante = aceleración 0 → F_neta = 0."},
                {"text": "Mayor que la fricción", "ok": False, "feedback": "Si tu empuje superara a la fricción, la caja aceleraría cada vez más rápido."},
                {"text": "Igual a 2 N", "ok": False, "feedback": "2 m/s es velocidad, no fuerza."},
            ],
        },
        "checks": [
            {
                "question": "Un ascensor arranca acelerando hacia arriba. ¿Cómo se compara la fuerza del piso sobre tus pies (Normal) con tu peso real `mg`?",
                "options": [
                    {"text": "Es mayor que tu peso: por eso te sentís más pesado", "ok": True, "feedback": "Exacto: N = m·(g + a) > mg para poder acelerarte hacia arriba."},
                    {"text": "Es igual a tu peso todo el tiempo", "ok": False, "feedback": "Si N = mg, la fuerza neta sería 0 y el ascensor no podría arrancar."},
                    {"text": "Es menor que tu peso", "ok": False, "feedback": "Eso pasa cuando acelera hacia abajo."},
                ],
            },
            {
                "question": "Un camión choca contra un mosquito. ¿Cómo son las fuerzas que se hacen entre sí?",
                "options": [
                    {"text": "El camión le hace mucha más fuerza al mosquito", "ok": False, "feedback": "La 3ª ley dice que ambas fuerzas son exactamente iguales."},
                    {"text": "Solo el camión ejerce fuerza", "ok": False, "feedback": "Las fuerzas siempre aparecen de a pares."},
                    {"text": "Iguales y opuestas; al mosquito le va peor por su masa diminuta", "ok": True, "feedback": "Exacto: misma F, pero con a = F/m la aceleración del mosquito es brutal."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con un ejemplo cotidiano la diferencia entre velocidad constante y aceleración usando las Leyes de Newton.",
    },
    "f-circular-gravitacion": {
        "hook": {
            "question": "A la altura de la Estación Espacial Internacional todavía existe casi el 90% de la gravedad de la Tierra. Entonces, ¿por qué flotan los astronautas?",
            "intuition": "No flotan porque 'no haya gravedad': flotan porque están cayendo sin parar hacia la Tierra, pero viajan tan rápido de costado (`27 600 km/h`) que el suelo curvo del planeta se les escapa al mismo ritmo. Orbitar es caer y errarle al suelo todo el tiempo.",
        },
        "concept": {
            "points": [
                "**Girar siempre es acelerar**: aunque tu velocímetro no se mueva en una rotonda, la dirección cambia sin parar. Esa aceleración apunta al **centro** y vale `a_c = v² / r`.",
                "**Fuerza centrípeta (`F_c = m · v² / r`)**: no es una fuerza nueva, es el *rol* que cumple quien te obliga a doblar (el agarre de las cubiertas, la cuerda de una boleadora o la gravedad en una órbita).",
                "**Cuidado con la velocidad al cuadrado**: doblar al doble de velocidad exige **4 veces** más agarre. Si el piso mojado no llega, seguís derecho por inercia (derrape).",
                "**Gravitación Universal (`F = G · m₁·m₂ / r²`)**: toda masa atrae a toda masa. Si duplicás la distancia entre dos cuerpos, la atracción cae a la cuarta parte (`1/2² = 1/4`).",
            ],
            "real_world": [
                {
                    "title": "Curvas con peralte en rutas y velódromos",
                    "detail": "Las curvas se inclinan hacia adentro para que parte de la fuerza normal del piso ayude a aportar fuerza centrípeta sin depender solo del caucho.",
                },
                {
                    "title": "El centrifugado del lavarropas",
                    "detail": "La pared empuja la ropa hacia adentro para hacerla girar; donde hay agujeros, nada empuja al agua y escapa en línea recta por inercia.",
                },
                {
                    "title": "Satélites GPS y mareas",
                    "detail": "Los satélites caen eternamente en órbita gracias a la gravedad terrestre, y la atracción gravitatoria de la Luna sobre los océanos genera las mareas.",
                },
            ],
            "key_rule": "`a_c = v² / r` hacia el centro · Duplicar `v` cuadruplica la fuerza necesaria · Gravedad cae como `1 / r²`.",
            "pitfall": "Creer que existe una 'fuerza centrífuga' empujándote hacia afuera del auto: lo que sentís es tu propio cuerpo queriendo seguir en línea recta mientras la puerta te empuja hacia el centro.",
        },
        "example": {
            "title": "Calculá el límite de una curva bajo lluvia",
            "steps": [
                "Un auto de `1000 kg` entra a una curva de radio `r = 50 m` a `10 m/s` (36 km/h).",
                "Fuerza de agarre necesaria: `F_c = 1000 · 10² / 50 = 2000 N` (muy manejable).",
                "Si entra al doble (`20 m/s` = 72 km/h), necesita `1000 · 20² / 50 = 8000 N` (4× más): en asfalto mojado las ruedas pierden agarre y el auto sigue recto.",
            ],
            "lab_link": "physics:forces",
            "lab_cta": "Explorar fricción",
        },
        "check": {
            "question": "Un auto gira en una rotonda a rapidez constante de 30 km/h. ¿Hacia dónde apunta la fuerza neta sobre el auto?",
            "options": [
                {"text": "Hacia el centro de la rotonda (fuerza centrípeta)", "ok": True, "feedback": "Exacto: es la fricción lateral de las cubiertas doblando continuamente la dirección del auto."},
                {"text": "Hacia afuera de la rotonda", "ok": False, "feedback": "No hay ninguna fuerza física tirando hacia afuera; si se pierde agarre el auto sale tangente (recto)."},
                {"text": "La fuerza neta es cero porque no cambia el velocímetro", "ok": False, "feedback": "Cambiar de dirección es acelerar, y eso exige fuerza neta."},
            ],
        },
        "checks": [
            {
                "question": "Si la Luna estuviera al DOBLE de distancia de la Tierra, ¿cómo cambiaría la fuerza gravitatoria entre ellas?",
                "options": [
                    {"text": "Sería la mitad", "ok": False, "feedback": "La distancia está al cuadrado en el denominador: 1 / r²."},
                    {"text": "Sería una cuarta parte (4 veces menor)", "ok": True, "feedback": "Exacto: 1 / 2² = 1/4."},
                    {"text": "Sería exactamente igual", "ok": False, "feedback": "La gravedad disminuye rápidamente con la distancia."},
                ],
            },
            {
                "question": "Girás una piedra atada a un hilo en círculos sobre tu cabeza y el hilo se corta de golpe. ¿Qué trayectoria sigue la piedra (vista desde arriba)?",
                "options": [
                    {"text": "Sale disparada derecho hacia afuera desde el centro", "ok": False, "feedback": "Al cortarse la fuerza centrípeta, conserva la velocidad que tenía en ese instante, que era tangente."},
                    {"text": "Sigue en línea recta por la tangente al círculo", "ok": True, "feedback": "Exacto: por la 1ª Ley de Newton, sin fuerza centrípeta sigue en línea recta en la dirección que llevaba."},
                    {"text": "Sigue dando un par de vueltas curvas antes de caer", "ok": False, "feedback": "Sin fuerza lateral no puede curvar su trayectoria."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en 2 frases por qué los astronautas flotan en órbita y por qué es tan peligroso duplicar la velocidad en una curva.",
    },
    "f-trabajo-energia": {
        "hook": {
            "question": "¿Por qué una montaña rusa no lleva motor después de la primera gran subida?",
            "intuition": "La energía no se crea ni se destruye: solo cambia de forma. La cadena inicial te compra energía potencial (altura) y todo el resto del paseo la va canjeando ida y vuelta por energía cinética (velocidad).",
        },
        "concept": {
            "points": [
                "**Trabajo (`W = F · d · cos θ`)**: solo hacés trabajo físico (en Joules, `J`) cuando tu fuerza produce desplazamiento en su dirección. Sostener algo quieto cansa tus músculos pero hace `W = 0`.",
                "**Energía Cinética (`Ek = ½ · m · v²`)**: energía de movimiento. Duplicar la velocidad **cuadruplica** la energía (y la distancia de frenado).",
                "**Energías Potenciales**: gravitatoria `Ep = m · g · h` (altura) y **elástica de resortes** `Ee = ½ · k · x²` (deformación, con fuerza de Hooke `F = k · x`).",
                "**Conservación y Potencia**: sin fricción, `Ek + Ep + Ee = constante`. Con fricción, la diferencia pasa a calor. La **Potencia** (`P = E / t`, en Watts) dice qué tan rápido transferís energía (`1 kWh` de tu factura = `3.6 millones de Joules`).",
            ],
            "real_world": [
                {
                    "title": "Frenado a 100 km/h vs. 50 km/h",
                    "detail": "Como `Ek ∝ v²`, ir a 100 km/h no lleva el doble de energía que a 50 km/h: lleva **4 veces** más energía que los frenos deben convertir en calor.",
                },
                {
                    "title": "Amortiguadores y arcos",
                    "detail": "Al caer en un pozo, el resorte de la suspensión absorbe el golpe guardando `½kx²` para no transmitírselo al chasis.",
                },
                {
                    "title": "Factura de luz (kWh) y tu cuerpo",
                    "detail": "Un microondas de 1000 W encendido 1 hora gasta 1 kWh. Un ciclista entrenado sostiene unos 250–300 W subiendo una cuesta.",
                },
            ],
            "key_rule": "`Ek = ½mv²` · `Ep = mgh` · `Ee = ½kx²` · `P = E / t` · La energía total siempre se conserva.",
            "pitfall": "Creer que un carrito más pesado baja más rápido una rampa sin fricción: en `mgh = ½mv²` la masa se cancela y llegan a la misma velocidad.",
        },
        "example": {
            "title": "Observá el canje Ep ↔ Ek ↔ Calor en la rampa",
            "steps": [
                "Abrí el Laboratorio de Física → Energía y dejá la opción **Sin fricción**.",
                "Mirá cómo suben y bajan `Ep` y `Ek` mientras la barra **Total** no se mueve ni un milímetro.",
                "Activá **Con fricción**: la bola se frena al fondo, pero toda la energía mecánica perdida apareció íntegra en la barra **Térmica**.",
            ],
            "lab_link": "physics:energy",
            "lab_cta": "Abrir Simulador de Energía en Rampa",
        },
        "check": {
            "question": "Si un auto duplica su velocidad (de 50 a 100 km/h), ¿cómo cambia su energía cinética?",
            "options": [
                {"text": "Se cuadruplica (×4), porque `v` va al cuadrado en `½mv²`", "ok": True, "feedback": "Exacto: (2v)² = 4v², por eso la distancia de frenado crece tanto."},
                {"text": "Se duplica (×2)", "ok": False, "feedback": "Sería lineal si no estuviera elevada al cuadrado."},
                {"text": "Se mantiene igual", "ok": False, "feedback": "La energía cinética depende directamente de la velocidad."},
            ],
        },
        "checks": [
            {
                "question": "Comprimís un resorte el DOBLE de distancia (`2x`). ¿Cuánta energía elástica guarda comparado con `x`?",
                "options": [
                    {"text": "El doble", "ok": False, "feedback": "La fuerza F = kx se duplica, pero la energía ½kx² crece con el cuadrado."},
                    {"text": "4 veces más", "ok": True, "feedback": "Exacto: en Ee = ½ · k · x², duplicar x cuadruplica la energía guardada."},
                    {"text": "La mitad", "ok": False, "feedback": "Comprimir más siempre almacena más energía."},
                ],
            },
            {
                "question": "Sostenés una mochila pesada completamente quieta durante un minuto. ¿Cuánto trabajo mecánico hacés sobre la mochila?",
                "options": [
                    {"text": "Cero, porque no hay desplazamiento", "ok": True, "feedback": "Exacto: W = F · d · cos θ y con d = 0 el trabajo físico es 0, aunque tus músculos gasten energía química."},
                    {"text": "Mucho, porque te cansás", "ok": False, "feedback": "El cansancio es gasto interno de tus fibras musculares, no trabajo sobre la mochila."},
                    {"text": "Depende solo del peso", "ok": False, "feedback": "Sin desplazamiento d no hay trabajo mecánico."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué relación hay entre `Ek = ½mv²` y la distancia de frenado de un auto.",
    },
    # ==================== NIVEL 3 ====================
    "f-momento-choques": {
        "hook": {
            "question": "¿Por qué un auto moderno se abolla entero adelante al chocar, en vez de ser duro como un tanque indestructible?",
            "intuition": "Un auto rígido te frena en una centésima de segundo con una fuerza letal sobre tus órganos. Las zonas deformables y el airbag alargan el tiempo de frenado (`Δt`), bajando drásticamente la fuerza del golpe (`F = Δp / Δt`).",
        },
        "concept": {
            "points": [
                "**Momento lineal (`p = m · v`)**: mide 'qué tan difícil es frenar algo'. Un camión lento y una bala veloz pueden tener el mismo momento.",
                "**Impulso (`J = F · Δt = Δp`)**: cambiar el momento de un objeto requiere fuerza aplicada durante un tiempo. Mismo cambio de velocidad en **más tiempo** = **mucha menos fuerza pico**.",
                "**Conservación del momento**: en cualquier choque o explosión sin fuerzas externas, el momento total **antes** iguala exactamente al momento total **después** (es vectorial: importa el signo).",
                "**Elástico vs. inelástico**: en ambos se conserva el momento `p`. Solo en choques **elásticos** (bolas de billar) se conserva además la energía cinética; en los **inelásticos** (autos pegados) parte de `Ek` se va en deformación y calor.",
            ],
            "real_world": [
                {
                    "title": "Airbags, cascos de bici y flexionar las rodillas",
                    "detail": "Todos hacen el mismo truco físico: estiran el tiempo de frenado `Δt` para que la fuerza pico sobre tu cuerpo sea muchísimo menor.",
                },
                {
                    "title": "Retroceso de un cohete o una manguera",
                    "detail": "Al lanzar agua o gases hacia atrás con gran momento, la manguera o el cohete reciben exactamente el mismo momento hacia adelante.",
                },
                {
                    "title": "Bolas de billar",
                    "detail": "Cuando una bola golpea de lleno a otra igual quieta (choque casi elástico), la primera se frena en seco y le entrega todo su momento y energía a la segunda.",
                },
            ],
            "key_rule": "`p = m · v` · `F · Δt = Δp` (más tiempo = menos fuerza) · En todo choque aislado, `p_antes = p_después`.",
            "pitfall": "Pensar que en un choque entre un camión y un auto chico el camión sufre menos cambio de momento: el cambio de momento `|Δp|` es exactamente igual para los dos, pero en el auto chico (menos masa) implica un cambio brutal de velocidad.",
        },
        "example": {
            "title": "Con airbag vs. sin airbag en números reales",
            "steps": [
                "Un pasajero de `70 kg` frena de `20 m/s` (72 km/h) a `0`: su cambio de momento es `Δp = 70 · 20 = 1400 kg·m/s`.",
                "Contra un tablero rígido (`Δt = 0.01 s`): `F = 1400 / 0.01 = 140 000 N` (equivale a 14 toneladas golpeándote).",
                "Con cinturón + airbag + zona deformable (`Δt = 0.14 s`): `F = 1400 / 0.14 = 10 000 N` (14 veces menos fuerza, la diferencia entre sobrevivir y no hacerlo).",
            ],
            "lab_link": "physics:forces",
            "lab_cta": "Repasar fuerza y aceleración",
        },
        "check": {
            "question": "Cuando saltás desde una pared bajita, flexionás las rodillas al tocar el piso en lugar de caer con las piernas trabadas. ¿Por qué?",
            "options": [
                {"text": "Alargás el tiempo de frenado `Δt`, reduciendo la fuerza pico sobre tus rodillas", "ok": True, "feedback": "Exacto: el cambio de momento Δp es el mismo, pero dividir por un Δt mayor reduce mucho F."},
                {"text": "Reducís tu momento lineal antes de tocar el piso", "ok": False, "feedback": "Justo antes de tocar el suelo llegás con la misma velocidad y el mismo momento."},
                {"text": "Eliminás la gravedad durante la caída", "ok": False, "feedback": "La gravedad sigue actuando igual."},
            ],
        },
        "checks": [
            {
                "question": "Un carrito de 2 kg a 6 m/s choca y queda pegado a otro carrito de 4 kg que estaba quieto. ¿A qué velocidad se mueven juntos después?",
                "options": [
                    {"text": "3 m/s", "ok": False, "feedback": "La masa total es 2 + 4 = 6 kg, no 4 kg."},
                    {"text": "2 m/s", "ok": True, "feedback": "Exacto: p_antes = 2·6 = 12 kg·m/s; dividido la masa total (6 kg) da 2 m/s."},
                    {"text": "6 m/s", "ok": False, "feedback": "Al sumar la masa del segundo carrito, la velocidad tiene que bajar."},
                ],
            },
            {
                "question": "En un choque donde dos autos se abollan y quedan pegados, ¿qué magnitud física se conserva igual?",
                "options": [
                    {"text": "El momento lineal total", "ok": True, "feedback": "Exacto: el momento siempre se conserva en colisiones aisladas, aunque se pierda energía cinética en chapa abollada y calor."},
                    {"text": "La energía cinética total", "ok": False, "feedback": "Parte de la energía cinética se transformó en deformación, sonido y calor."},
                    {"text": "Ninguna magnitud se conserva", "ok": False, "feedback": "El momento lineal total (y la energía total sumando calor/deformación) siempre se conserva."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en 2 frases cómo la fórmula `F · Δt = Δp` explica por qué funcionan los airbags y los cascos.",
    },
    "f-torque-rotacion": {
        "hook": {
            "question": "¿Por qué una tuerca oxidada que no podés mover con una llave corta se afloja sin esfuerzo si le encajás un caño largo?",
            "intuition": "Para hacer girar algo no importa solo cuánta fuerza hacés, sino **qué tan lejos del eje** la aplicás. Esa capacidad de giro se llama **torca o torque** (`τ = r · F · sen θ`).",
        },
        "concept": {
            "points": [
                "**Torca o torque (`τ = r · F · sen θ`)**: mide la capacidad de una fuerza para hacer girar un cuerpo. Crece con la distancia al eje (`r`), con la fuerza (`F`) y es máxima cuando empujás **perpendicular** (`90°`).",
                "**Equilibrio rotacional**: para que algo no vuelque ni gire (un puente, una grúa, un subibaja), los torques a favor y en contra del reloj deben empatar (`Στ = 0`).",
                "**Centro de masa y momento de inercia (`I`)**: el centro de masa es el punto de equilibrio de un cuerpo. El momento de inercia (`I`) es la resistencia a girar: depende mucho más de **qué tan lejos del eje está la masa** (`m·r²`).",
                "**Conservación del momento angular (`L = I · ω`)**: si nada frena el giro desde afuera, reducir `I` (acercar los brazos) dispara la velocidad de giro `ω`.",
            ],
            "real_world": [
                {
                    "title": "Cambiar una rueda pinchada o abrir una puerta",
                    "detail": "El picaporte está en el borde opuesto a las bisagras, y la llave cruz te da más brazo `r` para generar el torque necesario con menos fuerza.",
                },
                {
                    "title": "Patinadores, clavadistas y sillas giratorias",
                    "detail": "Un clavadista se hace bolita en el aire (achica `I`) para dar 3 vueltas rápidas y abre el cuerpo antes de entrar al agua (agranda `I`) para frenar el giro.",
                },
                {
                    "title": "Por qué una bici andando casi no se cae",
                    "detail": "Las ruedas girando tienen momento angular `L`, y las bicicletas además se auto-corrigen girando el manubrio hacia el lado que se inclinan.",
                },
            ],
            "key_rule": "`τ = r · F · sen θ` · Más brazo = menos fuerza · `L = I · ω` se conserva al cambiar de postura girando.",
            "pitfall": "Empujar en dirección hacia las bisagras (`θ = 0°`): por más fuerza que hagas, `sen(0°) = 0`, el torque es cero y la puerta no gira.",
        },
        "example": {
            "title": "Equilibrá un subibaja desigual",
            "steps": [
                "Un chico de `25 kg` se sienta en la punta a `2 m` del pivote: genera un torque proporcional a `25 × 2 = 50`.",
                "Su papá de `75 kg` (el triple de peso) se sienta del otro lado.",
                "Para empatar (`75 × d = 50`), el papá debe sentarse a `d = 50 / 75 ≈ 0.67 m` del centro (un tercio de la distancia).",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Intentás abrir una puerta muy pesada. ¿Dónde y en qué dirección conviene empujar para hacer la menor fuerza posible?",
            "options": [
                {"text": "En el borde más alejado de las bisagras y perpendicular (90°) a la puerta", "ok": True, "feedback": "Exacto: maximizás el brazo r y sen(90°) = 1."},
                {"text": "Cerca de las bisagras porque el recorrido es más corto", "ok": False, "feedback": "Con brazo r muy chico tendrías que hacer una fuerza enorme."},
                {"text": "En diagonal a 30° en el medio de la puerta", "ok": False, "feedback": "Perdés tanto brazo de palanca como componente perpendicular."},
            ],
        },
        "checks": [
            {
                "question": "Un clavadista salta y en el aire se hace bolita abrazando sus rodillas. ¿Qué pasa con su velocidad de giro?",
                "options": [
                    {"text": "Aumenta, porque baja su momento de inercia `I` y se conserva `L = I · ω`", "ok": True, "feedback": "Exacto: acercar la masa al eje reduce I y dispara ω."},
                    {"text": "Disminuye, porque ofrece menos superficie al aire", "ok": False, "feedback": "La razón principal es la conservación del momento angular, y gira mucho más rápido."},
                    {"text": "No cambia una vez que dejó el trampolín", "ok": False, "feedback": "Lo que no cambia es L = I · ω; si cambia I, cambia ω."},
                ],
            },
            {
                "question": "Aflojás un tornillo haciendo 40 N perpendiculares sobre una llave de 0.25 m. ¿Qué torque aplicás?",
                "options": [
                    {"text": "160 N·m", "ok": False, "feedback": "Dividiste en vez de multiplicar r · F."},
                    {"text": "10 N·m", "ok": True, "feedback": "Exacto: τ = 0.25 m · 40 N = 10 N·m."},
                    {"text": "40.25 N·m", "ok": False, "feedback": "El torque es un producto, no una suma."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué es el torque usando una llave inglesa y por qué un patinador gira más rápido al cerrar los brazos.",
    },
    "f-fluidos": {
        "hook": {
            "question": "¿Cómo logra un barco de 100 000 toneladas de acero flotar en el mar mientras una simple llave de metal se va directo al fondo?",
            "intuition": "El agua empuja hacia arriba todo lo que sumergís con una fuerza igual al peso del agua que desalojás (Arquímedes). Un barco hueco desplaza una pileta entera de agua: su densidad promedio (acero + aire adentro) es mucho menor que la del mar.",
        },
        "concept": {
            "points": [
                "**Presión (`P = F / A`) y profundidad (`P = P₀ + ρ·g·h`)**: a igual fuerza, menos área = más presión (por eso corta un cuchillo afilado). Bajo el agua, cada **10 metros** de profundidad la presión suma **+1 atmósfera**.",
                "**Principio de Pascal (multiplicador hidráulico)**: la presión aplicada a un fluido encerrado se transmite igual a todos lados (`F₁/A₁ = F₂/A₂`). Empujás suave en un pistón chico y levantás un auto en el pistón grande.",
                "**Principio de Arquímedes (flotación)**: el empuje hacia arriba vale `E = ρ_líquido · V_sumergido · g`. Si un objeto es menos denso que el líquido, flota (y se sumerge la fracción `ρ_obj / ρ_liq`).",
                "**Fluidos en movimiento**: al achicar un caño el fluido acelera (**Continuidad**: `A₁·v₁ = A₂·v₂`), y donde el fluido va más rápido su presión baja (**Bernoulli**).",
            ],
            "real_world": [
                {
                    "title": "Frenos hidráulicos y gato de taller",
                    "detail": "Apretás el pedal con un pie y el líquido de frenos multiplica esa fuerza sobre las cuatro ruedas gracias a Pascal.",
                },
                {
                    "title": "Flotar mejor en el mar que en la pileta",
                    "detail": "El agua salada es más densa (`1025 kg/m³`) que el agua dulce (`1000 kg/m³`), así que te empuja con más fuerza hacia arriba.",
                },
                {
                    "title": "Pulgar en la manguera y pulverizadores",
                    "detail": "Tapar la boca reduce el área y dispara la velocidad del chorro (Continuidad); en un pulverizador, el aire que pasa rápido sobre el tubito baja la presión ahí y hace subir el líquido (Bernoulli).",
                },
            ],
            "key_rule": "`P = P₀ + ρgh` · Pascal: `F₁/A₁ = F₂/A₂` · Arquímedes: flota si `ρ_obj < ρ_liq` · Bernoulli: más velocidad → menos presión.",
            "pitfall": "Creer que un objeto flota o se hunde por su peso total: lo que decide es su **densidad promedio** comparada con el líquido (un tronco enorme flota; una piedrita se hunde).",
        },
        "example": {
            "title": "Probá flotación y presión en el tanque de Fluidos",
            "steps": [
                "Abrí el Laboratorio de Física → **Fluidos** y probá soltar **Hielo** (`900 kg/m³`) en **Agua dulce**: ves cómo queda sumergido el 90%, igual que un iceberg.",
                "Cambiá el objeto a **Acero** en agua (se hunde porque `7800 > 1000`) y después cambiá el líquido a **Mercurio** (`13 600 kg/m³`): ¡el acero flota!",
                "Bajá el control de profundidad hasta 20 m y mirá cómo la presión hidrostática salta a ~3 atm.",
            ],
            "lab_link": "physics:fluids",
            "lab_cta": "Abrir Simulador de Fluidos y Arquímedes",
        },
        "check": {
            "question": "Un bloque de madera (`ρ = 600 kg/m³`) se coloca en agua (`ρ = 1000 kg/m³`). ¿Qué ocurre?",
            "options": [
                {"text": "Flota con el 60% de su volumen sumergido", "ok": True, "feedback": "Exacto: como ρ_obj < ρ_agua, flota y se sumerge la fracción 600 / 1000 = 60%."},
                {"text": "Se hunde hasta el fondo", "ok": False, "feedback": "Solo se hunde si su densidad supera a la del agua."},
                {"text": "Flota apoyado arriba sin sumergir nada", "ok": False, "feedback": "Necesita sumergir suficiente volumen para desplazar un peso de agua igual al suyo."},
            ],
        },
        "checks": [
            {
                "question": "En un gato hidráulico, el pistón grande tiene 20 veces el área del pistón chico. Si aplicás 100 N en el chico, ¿cuánta fuerza sale en el grande?",
                "options": [
                    {"text": "5 N", "ok": False, "feedback": "Dividiste en lugar de multiplicar: el área mayor multiplica la fuerza."},
                    {"text": "2000 N", "ok": True, "feedback": "Exacto: F₂ = 100 N × 20 = 2000 N por el Principio de Pascal."},
                    {"text": "120 N", "ok": False, "feedback": "La relación es multiplicativa (A₂ / A₁), no aditiva."},
                ],
            },
            {
                "question": "Tapás media boca de una manguera con el dedo para regar más lejos. ¿Por qué sale más rápido el agua?",
                "options": [
                    {"text": "Ecuación de continuidad (`A₁v₁ = A₂v₂`): al achicar el área a la mitad, la velocidad se duplica", "ok": True, "feedback": "Exacto: para pasar el mismo caudal por la mitad de espacio, el agua debe duplicar su velocidad."},
                    {"text": "Porque el dedo agrega energía cinética al agua", "ok": False, "feedback": "Tu dedo no empuja el agua hacia adelante; solo restringe el área de salida."},
                    {"text": "Por el Principio de Arquímedes", "ok": False, "feedback": "Arquímedes describe flotación, no flujo en cañerías."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con ejemplos cotidianos la diferencia entre Pascal (frenos), Arquímedes (barcos) y Bernoulli (pulverizadores/aviones).",
    },
    "f-termodinamica": {
        "hook": {
            "question": "¿Por qué una porción de pizza recién salida del horno te quema el paladar con el queso y la salsa, pero casi no te quema al tocar la masa que está a la misma temperatura?",
            "intuition": "Temperatura no es calor guardado. La salsa tiene mucha agua (altísimo calor específico `c`), así que almacena y transfiere muchísima más energía térmica a tu boca que la masa seca a idénticos 90°C.",
        },
        "concept": {
            "points": [
                "**Temperatura vs. Calor**: la temperatura mide qué tan rápido vibran las partículas; el calor (`Q`) es energía térmica viajando de lo caliente a lo frío.",
                "**Calentar y cambiar de estado**: subir temperatura cuesta `Q = m · c · ΔT` (calentar agua cuesta entre 5 y 10 veces más energía por grado que calentar la misma masa de aluminio o hierro). Derretir o evaporar consume **calor latente** sin subir la temperatura.",
                "**Gases ideales (`P · V = n · R · T`) y dilatación**: al calentar un gas encerrado sube su presión; los sólidos también se expanden (por eso los puentes tienen juntas metálicas dentadas).",
                "**Leyes y 3 transferencias**: 1ª Ley (`ΔU = Q − W`, conservación); 2ª Ley (el calor fluye solo de caliente a frío; ninguna máquina térmica es 100% eficiente). Se mueve por **Conducción**, **Convección** y **Radiación**.",
            ],
            "real_world": [
                {
                    "title": "El agua del mate y las ciudades costeras",
                    "detail": "Por su enorme calor específico, el agua tarda en calentarse en la pava y el océano suaviza el clima de las costas respecto al desierto.",
                },
                {
                    "title": "Transpirar para enfriarte y heladeras",
                    "detail": "Evaporar sudor absorbe calor latente de tu piel. Una heladera hace lo mismo con un gas refrigerante y gasta electricidad para bombear calor hacia afuera.",
                },
                {
                    "title": "Disipadores de aluminio en chips",
                    "detail": "El metal extrae el calor de un regulador o CPU por conducción y el ventilador lo arrastra al aire por convección.",
                },
            ],
            "key_rule": "`Q = m·c·ΔT` · `P·V = n·R·T` · Calor fluye de caliente a frío por Conducción, Convección o Radiación.",
            "pitfall": "Creer que un metal a 20°C está 'más frío' que la madera a 20°C: están a la misma temperatura, pero el metal conduce mucho más rápido y te roba calor de la mano al instante.",
        },
        "example": {
            "title": "Puente con Electrónica: calor por Efecto Joule",
            "steps": [
                "Toda corriente atravesando una resistencia convierte energía eléctrica en calor: `P = V · I = I² · R`.",
                "Una resistencia estándar de `1/4 W` (250 mW) se recalienta y se quema si le hacés disipar 500 mW.",
                "Comprobá la disipación en mW en el Laboratorio de Electrónica → Ley de Ohm cuando subís la fuente a 12 V.",
            ],
            "lab_link": "electronics:ohm",
            "lab_cta": "Ver disipación en mW",
        },
        "check": {
            "question": "¿Por qué un procesador caliente lleva un bloque de aluminio con aletas y un ventilador encima?",
            "options": [
                {"text": "El aluminio extrae calor por conducción y las aletas + ventilador lo evacúan por convección", "ok": True, "feedback": "Exacto: conducción del silicio al aluminio y convección forzada hacia el aire."},
                {"text": "Porque el aluminio bloquea el paso de electricidad", "ok": False, "feedback": "Su función es térmica, no de aislamiento eléctrico (de hecho el aluminio es conductor)."},
                {"text": "Para bajar el voltaje de la fuente", "ok": False, "feedback": "El voltaje lo regulan circuitos electrónicos; el disipador solo evacúa calor."},
            ],
        },
        "checks": [
            {
                "question": "Una botella de plástico cerrada queda en el auto al sol y se pone durísima (inflada). ¿Qué ley lo explica?",
                "options": [
                    {"text": "Ley de gases ideales (`PV = nRT`): al subir T con volumen fijo, aumenta la presión interna P", "ok": True, "feedback": "Exacto: las moléculas golpean las paredes más rápido y fuerte."},
                    {"text": "Se crearon moléculas nuevas de aire por el calor", "ok": False, "feedback": "La cantidad de gas n en la botella cerrada no cambió."},
                    {"text": "La presión atmosférica bajó a cero afuera", "ok": False, "feedback": "Afuera la presión atmosférica casi no varió; subió la presión adentro."},
                ],
            },
            {
                "question": "Por una resistencia de 100 Ω y 1/4 W circulan 0.1 A. ¿Cuánta potencia disipa?",
                "options": [
                    {"text": "0.01 W: aguanta sin problema", "ok": False, "feedback": "Te quedaste en I² = 0.01; faltó multiplicar por R = 100 Ω."},
                    {"text": "10 W", "ok": False, "feedback": "I · R = 10 es el voltaje en voltios; potencia es I² · R."},
                    {"text": "1 W: se sobrecalienta", "ok": True, "feedback": "Exacto: P = 0.01 · 100 = 1 W, cuatro veces su límite."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá la diferencia entre temperatura y calor y por qué transpirar enfría el cuerpo.",
    },
    # ==================== NIVEL 4 ====================
    "f-ondas-sonido": {
        "hook": {
            "question": "¿Por qué una ambulancia suena aguda al acercarse y cambia de golpe a grave justo cuando pasa frente a vos?",
            "intuition": "El sonido viaja como compresiones en el aire. Al acercarse, la ambulancia 'aplasta' sus propias ondas (más ciclos por segundo = más agudo); al alejarse las estira (menos ciclos por segundo = más grave). Es el **efecto Doppler**.",
        },
        "concept": {
            "points": [
                "**Oscilaciones (MAS)**: un péndulo o resorte oscila con un período fijo. En un péndulo (`T = 2π√(L/g)`), el ritmo depende del **largo**, NO de cuánto pesás.",
                "**Onda (`v = f · λ`)**: transporta energía sin arrastrar materia de punta a punta. El período es `T = 1 / f`.",
                "**Sonido**: la **frecuencia (`Hz`)** define la nota (grave/agudo) y la **amplitud** define el volumen. En el aire viaja a `~340 m/s` (unos 3 segundos por kilómetro).",
                "**Armónicos y Doppler**: una cuerda de guitarra vibra en múltiplos enteros (`f₁, 2f₁, 3f₁…`) dando el timbre; si fuente u oyente se mueven, cambia la frecuencia percibida (Doppler).",
            ],
            "real_world": [
                {
                    "title": "Calcular la distancia a una tormenta",
                    "detail": "La luz llega al instante y el sonido tarda ~3 s por km: si contás 6 s entre relámpago y trueno, el rayo cayó a ~2 km.",
                },
                {
                    "title": "Traste 12 de tu guitarra",
                    "detail": "Pisar justo la mitad de la cuerda recorta `λ` a la mitad y duplica `f` (110 Hz → 220 Hz): una octava exacta arriba.",
                },
                {
                    "title": "Radares de tránsito y ecografías Doppler",
                    "detail": "Miden cuánto cambió la frecuencia del eco reflejado para calcular la velocidad de un auto o del flujo sanguíneo en una arteria.",
                },
            ],
            "key_rule": "`v = f · λ` · `T = 1 / f` · Frecuencia = nota, Amplitud = volumen · Péndulo depende de `L`, no de la masa.",
            "pitfall": "Confundir volumen con tono: tocar una cuerda más fuerte aumenta la amplitud (más fuerte), pero la frecuencia (la nota) sigue siendo la misma.",
        },
        "example": {
            "title": "Escuchá armónicos y nodos en vivo",
            "steps": [
                "Abrí el Laboratorio de Física → **Ondas** y activá el sonido en `110 Hz` (5ª cuerda de guitarra, La2).",
                "Cambiá a armónico `n = 2` (`220 Hz`): mirá el nodo quieto en el centro exacto (traste 12) y escuchá la octava.",
                "Subí a `n = 3` y `n = 4` para ver cómo se multiplican los nodos y las frecuencias.",
            ],
            "lab_link": "physics:waves",
            "lab_cta": "Abrir Simulador de Ondas con Audio",
        },
        "check": {
            "question": "Si la 5ª cuerda de una guitarra vibra a 110 Hz (La2) y la pisás en el traste 12 (mitad de la cuerda), ¿qué frecuencia produce?",
            "options": [
                {"text": "220 Hz (una octava arriba)", "ok": True, "feedback": "Exacto: media longitud de onda a igual velocidad implica el doble de frecuencia."},
                {"text": "55 Hz", "ok": False, "feedback": "Acortar la cuerda da una nota más aguda (más Hz), no más grave."},
                {"text": "122 Hz", "ok": False, "feedback": "La octava duplica la frecuencia (×2), no suma 12."},
            ],
        },
        "checks": [
            {
                "question": "Un niño y un adulto se hamacan en dos hamacas del mismo largo. ¿Cuál tarda menos en hacer una ida y vuelta?",
                "options": [
                    {"text": "El adulto, porque pesa más", "ok": False, "feedback": "La masa se cancela en el péndulo, igual que en caída libre."},
                    {"text": "Tardan exactamente lo mismo", "ok": True, "feedback": "Exacto: T = 2π√(L/g) depende solo del largo L y la gravedad g."},
                    {"text": "El niño, porque es más liviano", "ok": False, "feedback": "La masa no entra en el período del péndulo."},
                ],
            },
            {
                "question": "Ves un relámpago y 9 segundos después escuchás el trueno (v ≈ 340 m/s). ¿A qué distancia aproximada cayó?",
                "options": [
                    {"text": "A unos 3 kilómetros (~3060 m)", "ok": True, "feedback": "Exacto: 340 × 9 = 3060 m ≈ 3 km."},
                    {"text": "A unos 38 metros", "ok": False, "feedback": "Dividiste en lugar de multiplicar velocidad por tiempo."},
                    {"text": "A 9 kilómetros", "ok": False, "feedback": "El sonido recorre ~1 km cada 3 segundos, no 1 km por segundo."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué produce el efecto Doppler y qué relación hay entre frecuencia, amplitud y longitud de onda.",
    },
    "f-electricidad-campos": {
        "hook": {
            "question": "¿Los electrones corren a la velocidad de la luz por el cable cuando tocás el interruptor de la luz?",
            "intuition": "No: los electrones avanzan a paso de caracol (milímetros por segundo). Lo que viaja casi a la velocidad de la luz es el **campo eléctrico** que empuja a la fila entera de electrones ya presentes dentro del cobre, como el agua en una manguera ya llena.",
        },
        "concept": {
            "points": [
                "**Carga (`q`) y Ley de Coulomb (`F = k·q₁·q₂ / r²`)**: cargas iguales se repelen, opuestas se atraen, y la fuerza cae con el cuadrado de la distancia (como la gravedad, pero muchísimo más intensa).",
                "**Corriente (`I = q/t`) y Voltaje (`V = E/q`)**: `1 Amperio` es `1 Coulomb por segundo` (caudal); `1 Voltio` es `1 Joule por Coulomb` (energía por carga). **Potencia**: `P = V · I`.",
                "**Serie vs. Paralelo**: en **serie** la corriente es la misma y los voltajes se reparten (si se corta una lámpara se apaga todo). En **paralelo** todos reciben el mismo voltaje (`220 V` en tu casa) y sus corrientes se **suman**.",
                "**Capacitores**: almacenan energía en un campo eléctrico entre dos placas y la sueltan en milisegundos (flashes de cámara, pantallas táctiles y filtros de fuentes).",
            ],
            "real_world": [
                {
                    "title": "Zapatilla sobrecargada en casa",
                    "detail": "Como los enchufes están en paralelo, sumar pava eléctrica + estufa suma sus corrientes en un solo cable y hace saltar la llave térmica para evitar un incendio.",
                },
                {
                    "title": "Chispazo al bajar del auto en días secos",
                    "detail": "El roce acumula carga estática (miles de voltios) que crea un campo eléctrico capaz de ionizar el aire en una micro-chispa al tocar la chapa.",
                },
                {
                    "title": "Consumo de un ESP32 con batería",
                    "detail": "A 3.3 V y 200 mA consume `0.66 W`. Una batería de 2000 mAh rinde ~10 h continuas (por eso los sensores IoT duermen casi todo el tiempo).",
                },
            ],
            "key_rule": "`F = k·q₁q₂/r²` · `I = q/t` · `V = E/q` · `P = V·I` · En paralelo mismo voltaje, se suman las corrientes.",
            "pitfall": "Creer que la pila 'trae los electrones adentro' y cuando se agota se quedó sin electrones: la pila solo aporta energía química (voltaje) para bombear electrones que ya estaban en los cables.",
        },
        "example": {
            "title": "Calculá potencia y corriente de una pava eléctrica",
            "steps": [
                "Una pava eléctrica de `2200 W` enchufada a `220 V` toma `I = P / V = 2200 / 220 = 10 A`.",
                "Si en la misma zapatilla (límite `10 A`) enchufás además una tostadora de `1100 W` (`5 A`), la corriente total en paralelo trepa a `15 A`.",
                "El cable se calienta por `I²·R` y la térmica corta el circuito antes de que se derrita el aislante.",
            ],
            "lab_link": "electronics:ohm",
            "lab_cta": "Explorar V, I, R y Potencia",
        },
        "check": {
            "question": "Físicamente, ¿qué significa decir que una batería entrega 9 Voltios?",
            "options": [
                {"text": "Que entrega 9 Joules de energía por cada Coulomb de carga que impulsa", "ok": True, "feedback": "Exacto: 1 V = 1 J/C."},
                {"text": "Que impulsa exactamente 9 Amperios siempre", "ok": False, "feedback": "La corriente depende de la resistencia conectada (I = V / R)."},
                {"text": "Que los electrones viajan a 9 m/s", "ok": False, "feedback": "Voltaje es energía por unidad de carga, no velocidad."},
            ],
        },
        "checks": [
            {
                "question": "En tu casa las luces están conectadas en paralelo. Si se quema la lamparita de la cocina, ¿qué pasa con la del living?",
                "options": [
                    {"text": "Se apaga también", "ok": False, "feedback": "Eso solo pasaría si estuvieran en serie."},
                    {"text": "Sigue prendida igual, porque tiene su propio camino a 220 V", "ok": True, "feedback": "Exacto: en paralelo cada rama es independiente y recibe los mismos 220 V."},
                    {"text": "Brilla el doble porque recibe el doble de voltaje", "ok": False, "feedback": "La red sigue entregando 220 V fijos."},
                ],
            },
            {
                "question": "Una pila se 'agota'. ¿Qué es lo que realmente se le terminó?",
                "options": [
                    {"text": "Los electrones que tenía guardados", "ok": False, "feedback": "Los electrones ya están en los cables de cobre."},
                    {"text": "La corriente almacenada de fábrica", "ok": False, "feedback": "La corriente solo existe mientras el circuito está cerrado."},
                    {"text": "La energía química con la que bombeaba las cargas", "ok": True, "feedback": "Exacto: se agotó la reacción química que sostenía la diferencia de potencial (voltaje)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué enchufar dos electrodomésticos potentes a la misma zapatilla hace saltar la térmica.",
    },
    "f-electromagnetismo": {
        "hook": {
            "question": "¿Qué tienen en común una pastilla de guitarra eléctrica, un cargador inalámbrico, un parlante y el freno regenerativo de un auto eléctrico?",
            "intuition": "Todos explotan las dos caras de la misma moneda: **electricidad en movimiento crea magnetismo**, y **magnetismo cambiante induce electricidad**.",
        },
        "concept": {
            "points": [
                "**Corriente → Magnetismo**: toda corriente crea un campo magnético alrededor del cable. Enrollándolo en bobina con hierro adentro hacés un **electroimán**.",
                "**Fuerza de Lorentz (motores y parlantes)**: una corriente dentro de un campo magnético siente una fuerza lateral que hace girar un motor o vibrar el cono de un parlante.",
                "**Ley de Faraday (generadores y pastillas)**: un campo magnético **cambiante** atravesando una bobina induce voltaje eléctrico. Si el campo queda quieto, el voltaje es **cero**.",
                "**Ley de Lenz y Transformadores**: la corriente inducida siempre se opone al cambio (así frena un auto eléctrico recargando su batería). Dos bobinas con distinto número de vueltas suben o bajan voltaje alterno (`V₂/V₁ = N₂/N₁`).",
            ],
            "real_world": [
                {
                    "title": "Pastilla de guitarra eléctrica",
                    "detail": "La cuerda metálica vibrando a 110 Hz perturba el campo de los imanes e induce una señal alterna de 110 Hz en la bobina.",
                },
                {
                    "title": "Cargador inalámbrico (Qi) y cocina de inducción",
                    "detail": "Una bobina con corriente alterna genera un campo cambiante que induce corriente en la bobina del celular (o directamente en la base metálica de la olla).",
                },
                {
                    "title": "Frenado regenerativo en autos y trenes eléctricos",
                    "detail": "Al soltar el acelerador, el motor funciona al revés como generador: la resistencia magnética frena las ruedas y devuelve energía a la batería.",
                },
            ],
            "key_rule": "Corriente → Fuerza magnética (motor/parlante) · Flujo magnético CAMBIANTE → Voltaje (Faraday) · `V₂/V₁ = N₂/N₁`.",
            "pitfall": "Pensar que un imán potente quieto al lado de una bobina produce electricidad: sin cambio en el tiempo, Faraday da exactamente cero.",
        },
        "example": {
            "title": "Cómo baja 220 V de la pared a tu celular",
            "steps": [
                "La electricidad llega a tu casa como corriente alterna (completa 50 ciclos por segundo) justamente para poder transformarla con bobinas.",
                "La bobina primaria crea un campo magnético oscilante que atraviesa una bobina secundaria con muchas menos vueltas (`V₂/V₁ = N₂/N₁`).",
                "Así baja el voltaje sin partes móviles, y luego un rectificador lo convierte en los 5 V continuos del USB.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Apoyás un imán de neodimio potentísimo completamente QUIETO sobre una bobina de cobre. ¿Cuánto voltaje se induce?",
            "options": [
                {"text": "Cero: la Ley de Faraday solo induce voltaje cuando el flujo magnético CAMBIA", "ok": True, "feedback": "Exacto: hace falta movimiento o variación de corriente."},
                {"text": "Un voltaje constante muy alto", "ok": False, "feedback": "Un campo estático no induce voltaje."},
                {"text": "Depende del grosor del alambre", "ok": False, "feedback": "Sin variación temporal no se induce nada."},
            ],
        },
        "checks": [
            {
                "question": "Un transformador ideal recibe 220 V en 1000 vueltas y tiene 100 vueltas en la salida. ¿Qué voltaje sale?",
                "options": [
                    {"text": "2200 V", "ok": False, "feedback": "Tiene 10 veces MENOS vueltas en la salida, así que el voltaje baja 10 veces."},
                    {"text": "22 V", "ok": True, "feedback": "Exacto: V₂ = 220 × (100 / 1000) = 22 V."},
                    {"text": "220 V", "ok": False, "feedback": "Solo saldría 220 V si ambas bobinas tuvieran la misma cantidad de vueltas."},
                ],
            },
            {
                "question": "¿Cuál de estos dispositivos convierte movimiento en electricidad?",
                "options": [
                    {"text": "La pastilla de una guitarra eléctrica", "ok": True, "feedback": "Exacto: la vibración de la cuerda cambia el campo magnético e induce señal."},
                    {"text": "Un parlante", "ok": False, "feedback": "El parlante hace lo inverso: corriente → movimiento del cono."},
                    {"text": "Un ventilador", "ok": False, "feedback": "Un motor recibe electricidad y produce movimiento."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué las cocinas de inducción, los transformadores y los cargadores inalámbricos necesitan corriente alterna.",
    },
    # ==================== NIVEL 5 ====================
    "f-ondas-em": {
        "hook": {
            "question": "¿Qué tienen en común la señal de Wi-Fi, el calor de unas brasas, la luz del sol y una radiografía?",
            "intuition": "Son exactamente el mismo fenómeno físico: **ondas electromagnéticas** viajando a `300 000 km/s` (`c`). Lo único que cambia de una a otra es su frecuencia (cuántas veces oscilan por segundo) y su longitud de onda.",
        },
        "concept": {
            "points": [
                "**Una sola familia (`c = f · λ`)**: todas viajan a `c = 3 × 10⁸ m/s` en el vacío. A mayor frecuencia `f`, menor longitud de onda `λ` y mayor energía.",
                "**El espectro completo (de menor a mayor frecuencia)**: Radio → Microondas / Wi-Fi → Infrarrojo → **Luz visible** (rojo a violeta) → Ultravioleta (UV) → Rayos X → Rayos Gamma.",
                "**Polarización**: la luz es una onda transversal. Un filtro polarizado deja pasar solo una dirección de oscilación, eliminando los reflejos horizontales molestos.",
                "**Interferencia y difracción**: cuando dos ondas de luz se superponen pueden reforzarse (brillo/color) o cancelarse (oscuridad). Por eso una película finísima transparente produce arcoíris.",
            ],
            "real_world": [
                {
                    "title": "Wi-Fi 2.4 GHz vs. 5 GHz en tu casa",
                    "detail": "2.4 GHz tiene onda más larga (`12.5 cm`) y atraviesa paredes mejor; 5 GHz (`6 cm`) lleva más datos pero pierde señal antes tras el cemento.",
                },
                {
                    "title": "Anteojos de sol polarizados al manejar",
                    "detail": "El reflejo del sol en el asfalto o el agua está polarizado en horizontal; el cristal polarizado en vertical lo bloquea casi por completo.",
                },
                {
                    "title": "Burbujas de jabón y charcos con nafta",
                    "detail": "Los dos reflejos (cara de arriba y cara de abajo de la película fina) interfieren entre sí y refuerzan distintos colores según el espesor.",
                },
            ],
            "key_rule": "`c = f · λ = 3 × 10⁸ m/s` · Radio < Microondas < IR < Visible < UV < Rayos X < Gamma.",
            "pitfall": "Creer que el Wi-Fi o la radio viajan más lento que la luz (o que el Wi-Fi es 'radiación ionizante' como los rayos X): todas viajan a `c`, pero cada fotón de radio/Wi-Fi tiene cientos de miles de veces menos energía que uno de UV (y muchísimo menos que uno de rayos X).",
        },
        "example": {
            "title": "Calculá el tamaño físico de la onda de tu Wi-Fi",
            "steps": [
                "Tu router emite a `f = 2.4 GHz = 2.4 × 10⁹ Hz` y la onda viaja a `c = 3 × 10⁸ m/s`.",
                "Despejamos longitud de onda: `λ = c / f = (3 × 10⁸) / (2.4 × 10⁹) = 0.125 m = 12.5 cm`.",
                "Las antenas funcionan mejor cuando miden `λ/2` o `λ/4`: por eso muchas antenas de Wi-Fi miden unos 6 cm o 3 cm.",
            ],
            "lab_link": "physics:waves",
            "lab_cta": "Visualizar ondas y λ",
        },
        "check": {
            "question": "¿Cuál es la diferencia fundamental entre una onda de radio FM y la luz visible?",
            "options": [
                {"text": "Su frecuencia y longitud de onda (la luz vibra mucho más rápido)", "ok": True, "feedback": "Exacto: ambas son ondas electromagnéticas viajando a la misma velocidad c."},
                {"text": "La luz viaja mucho más rápido que las ondas de radio", "ok": False, "feedback": "En el vacío todas viajan exactamente a c = 300 000 km/s."},
                {"text": "La radio es sonido y la luz es electricidad", "ok": False, "feedback": "La radio viaja como onda electromagnética hasta tu antena; recién el parlante la vuelve sonido."},
            ],
        },
        "checks": [
            {
                "question": "¿Por qué el sol (UV) puede quemarte la piel y dañar ADN, mientras estar rodeado de señales de radio y Wi-Fi no te quema?",
                "options": [
                    {"text": "Porque la radiación UV tiene frecuencias muchísimo más altas y energía suficiente para romper enlaces químicos", "ok": True, "feedback": "Exacto: radio y Wi-Fi son radiación no ionizante de muy baja frecuencia."},
                    {"text": "Porque el Wi-Fi no atraviesa el aire", "ok": False, "feedback": "El Wi-Fi viaja por el aire sin problema; su energía por fotón es diminuta."},
                    {"text": "Porque el UV viaja más rápido que c", "ok": False, "feedback": "Nada viaja más rápido que c."},
                ],
            },
            {
                "question": "Mirás un monitor LCD a través de unos anteojos polarizados y los vas girando: en cierta posición la pantalla se oscurece casi por completo. ¿Por qué?",
                "options": [
                    {"text": "La pantalla emite luz polarizada y, cuando el filtro de los anteojos queda cruzado a 90° con ella, bloquea esa dirección de oscilación", "ok": True, "feedback": "Exacto: es la prueba casera perfecta de que la luz es una onda transversal polarizable."},
                    {"text": "Los anteojos absorben la electricidad de la pantalla", "ok": False, "feedback": "Es un efecto puramente óptico sobre la luz ya emitida."},
                    {"text": "El monitor se apaga por infrarrojos", "ok": False, "feedback": "La pantalla sigue encendida igual."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en 2 frases cómo se ordena el espectro electromagnético y por qué funcionan los anteojos polarizados.",
    },
    "f-optica-luz": {
        "hook": {
            "question": "¿Cómo logra internet viajar por cables de vidrio doblando esquinas por toda la ciudad sin que se escape la luz?",
            "intuition": "Cuando la luz intenta salir del vidrio hacia un medio con menor índice de refracción en un ángulo suficientemente rasante, no puede salir: rebota al 100% hacia adentro (**reflexión interna total**). La fibra óptica es un túnel de espejos perfectos.",
        },
        "concept": {
            "points": [
                "**Reflexión y espejos**: el ángulo con que entra el rayo iguala al que sale (`θ_i = θ_r`). Espejos planos dan tamaño real; convexos (retrovisor del auto) achican la imagen para darte más campo visual.",
                "**Refracción y Ley de Snell (`n₁·sen θ₁ = n₂·sen θ₂`)**: la luz frena al entrar a agua (`n=1.33`) o vidrio (`n=1.50`), con `v = c / n`. Al frenar se dobla hacia la normal; al acelerar se aleja.",
                "**Reflexión interna total**: al pasar de un medio denso (`n₁`) a uno menos denso (`n₂`), si superás el **ángulo crítico** (`sen θ_c = n₂/n₁`), toda la luz se refleja adentro (fibra óptica y brillo de diamantes).",
                "**Lentes delgadas (`1/f = 1/d_o + 1/d_i`)**: lentes **convergentes** juntan rayos (lupas, cámaras, hipermetropía); **divergentes** los abren (miopía).",
            ],
            "real_world": [
                {
                    "title": "Tu conexión de internet por fibra óptica",
                    "detail": "Pulsos láser rebotan miles de veces por reflexión interna total a `200 000 km/s` recorriendo océanos enteros casi sin pérdida.",
                },
                {
                    "title": "El ojo humano y los anteojos",
                    "detail": "El cristalino es una lente convergente flexible. Si sos miope enfoca antes de la retina y usás lente divergente; si tenés hipermetropía enfoca detrás y usás convergente.",
                },
                {
                    "title": "Una pileta parece más playita",
                    "detail": "Al salir del agua al aire los rayos se abren; tu cerebro los extiende en línea recta y calcula mal la profundidad real.",
                },
            ],
            "key_rule": "`v = c / n` · Snell: `n₁·sen θ₁ = n₂·sen θ₂` · Lentes: `1/f = 1/d_o + 1/d_i`.",
            "pitfall": "Pensar que la reflexión interna total puede ocurrir yendo de aire hacia agua: SOLO ocurre cuando la luz va de un medio de MAYOR índice `n₁` hacia uno de MENOR índice `n₂` (ej. vidrio → aire).",
        },
        "example": {
            "title": "Simulá refracción y fibra óptica en vivo",
            "steps": [
                "Abrí el Laboratorio de Física → **Óptica** y probá **Aire → Agua**: ves que el rayo siempre se quiebra acercándose a la vertical.",
                "Ahora invertí los medios a **Vidrio → Aire** y arrastrá el ángulo hasta pasar los `41.8°` (ángulo crítico).",
                "Observá cómo desaparece el rayo refractado y aparece la **Reflexión Interna Total** al 100%, exactamente como adentro de una fibra óptica.",
            ],
            "lab_link": "physics:optics",
            "lab_cta": "Abrir Simulador de Óptica y Ley de Snell",
        },
        "check": {
            "question": "¿En qué dirección debe viajar la luz para que pueda ocurrir reflexión interna total (como en la fibra óptica)?",
            "options": [
                {"text": "Desde un medio con mayor índice `n` (vidrio/agua) hacia uno con menor `n` (aire/revestimiento)", "ok": True, "feedback": "Exacto: solo al acelerar en el segundo medio el rayo puede llegar a 90° y rebotar por completo."},
                {"text": "Desde el aire hacia el agua o vidrio", "ok": False, "feedback": "Al entrar desde el aire el rayo se acerca a la normal y siempre logra pasar."},
                {"text": "Entre dos medios idénticos", "ok": False, "feedback": "Si n₁ = n₂ el rayo sigue derecho sin desviarse."},
            ],
        },
        "checks": [
            {
                "question": "Si el agua tiene índice `n = 1.33` y el diamante `n = 2.42`, ¿en cuál viaja más lento la luz?",
                "options": [
                    {"text": "En el diamante (`v = c / 2.42`), y por eso tiene un ángulo crítico tan chico y brilla tanto", "ok": True, "feedback": "Exacto: mayor n significa luz más lenta y mayor desvío."},
                    {"text": "En el agua", "ok": False, "feedback": "Cuanto mayor es n, más se divide c (más lenta va)."},
                    {"text": "Viaja igual a `c` en ambos", "ok": False, "feedback": "Solo en el vacío viaja a c."},
                ],
            },
            {
                "question": "Usás una lente convergente de distancia focal `f = 20 cm` con un objeto a `d_o = 60 cm`. ¿Dónde se forma la imagen (`1/f = 1/d_o + 1/d_i`)?",
                "options": [
                    {"text": "A 30 cm", "ok": True, "feedback": "Exacto: 1/d_i = 1/20 − 1/60 = 2/60 = 1/30 → d_i = 30 cm."},
                    {"text": "A 40 cm", "ok": False, "feedback": "No se restan las distancias directo: se restan sus inversos (1/20 − 1/60)."},
                    {"text": "A 80 cm", "ok": False, "feedback": "Recordá usar la fórmula de los inversos 1/f = 1/do + 1/di."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué es la refracción y cómo aprovecha la fibra óptica la reflexión interna total.",
    },
    "f-relatividad": {
        "hook": {
            "question": "Si la relatividad de Einstein suena a ciencia ficción, ¿por qué tu celular te ubicaría 11 kilómetros fuera de lugar todos los días sin ella?",
            "intuition": "El tiempo no corre al mismo ritmo en todo el universo. Los satélites GPS se mueven rapidísimo y están en menor gravedad, así que sus relojes atómicos corren a distinto ritmo que los de la Tierra. Si los ingenieros no corrigieran con las ecuaciones de Einstein, el GPS sería inútil en pocas horas.",
        },
        "concept": {
            "points": [
                "**Los 2 postulados de Einstein**: (1) las leyes de la física son iguales para cualquiera que se mueva a velocidad constante; (2) la luz en el vacío **siempre** viaja a `c = 300 000 km/s` sin importar qué tan rápido se mueva quien la emite o quien la mide.",
                "**Dilatación del tiempo (`Δt = γ · Δt₀`)**: para mantener `c` constante, el tiempo pasa más **despacio** en un reloj que se mueve rápido respecto a vos (`γ = 1 / √(1 − v²/c²)`).",
                "**Contracción de la longitud (`L = L₀ / γ`)**: un objeto veloz se mide más corto a lo largo de la dirección en que viaja (y el universo se acorta para el viajero).",
                "**`E = m · c²`**: la masa es energía ultra concentrada. Como `c² = 9 × 10¹⁶`, convertir apenas **1 gramo** de masa en energía equivale a ~25 millones de kWh.",
            ],
            "real_world": [
                {
                    "title": "Satélites GPS de tu teléfono",
                    "detail": "Corrigen ~38 microsegundos diarios combinando relatividad especial (velocidad) y general (altura/gravedad); sin eso errarían ~11 km por día.",
                },
                {
                    "title": "Muones cósmicos que llegan al suelo",
                    "detail": "Partículas creadas en la atmósfera alta deberían desintegrarse mucho antes de tocar tierra, pero como viajan a `0.995 c` su reloj interno va tan lento que llegan vivas a los detectores.",
                },
                {
                    "title": "La energía del Sol",
                    "detail": "El Sol convierte 4 millones de toneladas de masa en luz cada segundo mediante `E = mc²`, y aún le queda combustible para 5000 millones de años.",
                },
            ],
            "key_rule": "`c` es constante para todos · Relojes en movimiento corren más lento (`γ = 1/√(1−v²/c²)`) · `E = m·c²`.",
            "pitfall": "Creer que los viajeros dentro de una nave veloz se sienten 'en cámara lenta': para ellos su pulso y su reloj se sienten 100% normales; la diferencia aparece recién al comparar relojes con quien quedó en la Tierra.",
        },
        "example": {
            "title": "Viaje espacial a 0.6 c con cuentas exactas",
            "steps": [
                "Una nave viaja a `v = 0.6 c`. Calculamos `v²/c² = 0.36`, así que `√(1 − 0.36) = √0.64 = 0.8`.",
                "El factor de Lorentz es `γ = 1 / 0.8 = 1.25`.",
                "Por cada `4 años` que vive la tripulación adentro, en la Tierra transcurren `4 × 1.25 = 5 años`.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Una nave avanza a `0.8 c` y enciende un láser hacia adelante. ¿Con qué velocidad mide ese rayo alguien quieto en una estación espacial?",
            "options": [
                {"text": "Exactamente `c`", "ok": True, "feedback": "Exacto: la velocidad de la luz en el vacío es invariante para todo observador."},
                {"text": "`1.8 c`", "ok": False, "feedback": "La luz nunca supera c ni se suma a la velocidad de la fuente."},
                {"text": "`0.2 c`", "ok": False, "feedback": "No se restan; siempre vale exactamente c."},
            ],
        },
        "checks": [
            {
                "question": "Para un astronauta que viaja a `0.9 c`, ¿cómo percibe el paso del tiempo dentro de su propia nave?",
                "options": [
                    {"text": "Completamente normal (1 segundo dura 1 segundo para él); la diferencia se nota al comparar con la Tierra", "ok": True, "feedback": "Exacto: en tu propio sistema en reposo todo se siente normal (1º postulado)."},
                    {"text": "Siente que piensa y respira en cámara lenta", "ok": False, "feedback": "El reloj biológico y el de pulsera van juntos, así que no percibe cámara lenta."},
                    {"text": "El tiempo se detiene totalmente", "ok": False, "feedback": "Ningún cuerpo con masa llega a c ni detiene su propio tiempo."},
                ],
            },
            {
                "question": "¿Por qué los muones cósmicos creados a 15 km de altura logran llegar a la superficie terrestre pese a vivir solo 2.2 microsegundos?",
                "options": [
                    {"text": "Porque viajan casi a `c`: desde la Tierra su reloj se dilata (y desde el muón, la atmósfera se contrae)", "ok": True, "feedback": "Exacto: es una de las pruebas experimentales más directas de la relatividad especial."},
                    {"text": "Porque el aire los frena y los mantiene jóvenes", "ok": False, "feedback": "Al contrario: cuanto más rápido van, mayor es γ."},
                    {"text": "Porque viajan más rápido que la luz", "ok": False, "feedback": "Tienen masa y siempre viajan por debajo de c."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en 2 frases cómo se conectan la constancia de `c`, la dilatación del tiempo y el GPS.",
    },
    "f-cuantica-nuclear": {
        "hook": {
            "question": "¿Por qué un LED azul necesita bastante más voltaje que un LED rojo (unos 3 V contra 1.8 V), y por qué un panel solar genera electricidad cuando le pega la luz?",
            "intuition": "A escala atómica la energía no viene en chorro continuo sino en paquetes mínimos llamados **fotones** (`E = h · f`). La luz azul trae paquetes más energéticos que la roja, y cuando esos paquetes golpean el silicio de un panel solar, liberan electrones directamente.",
        },
        "concept": {
            "points": [
                "**Fotones (`E = h · f`)**: la luz también se comporta como paquetes de energía. Más frecuencia = fotones más potentes; más brillo = *más cantidad* de fotones, pero cada uno con la misma energía.",
                "**Efecto fotoeléctrico**: un electrón solo salta de un material si un fotón individual supera la energía umbral. El mismo principio (un fotón con energía suficiente libera un electrón) hace funcionar los paneles solares, los sensores de las cámaras digitales (CMOS) y las fotocélulas de los portones.",
                "**Átomos cuantizados y dualidad**: los electrones solo ocupan escalones fijos de energía (por eso cada LED o gas neón emite colores exactos). Además, electrones y partículas también tienen comportamiento de onda (microscopios electrónicos).",
                "**Física nuclear**: los isótopos inestables decaen reduciéndose a la mitad cada **vida media** (datación por Carbono-14). La **fisión** parte núcleos pesados (centrales); la **fusión** une núcleos livianos (el Sol).",
            ],
            "real_world": [
                {
                    "title": "LEDs y pantallas OLED",
                    "detail": "El color de cada LED sale del tamaño del 'escalón cuántico' (bandgap) del semiconductor: rojo ~1.8 V, verde ~2.2 V, azul ~3.0 V.",
                },
                {
                    "title": "Paneles solares y sensores de cámara",
                    "detail": "Cada píxel de tu celular cuenta cuántos fotones golpearon el silicio y liberaron electrones por efecto fotoeléctrico.",
                },
                {
                    "title": "Datación por Carbono-14 y medicina nuclear",
                    "detail": "Midiendo qué fracción de C-14 quedó tras varias vidas medias (5730 años) se calcula la edad de restos antiguos; radioisótopos de vida media corta permiten tomografías PET.",
                },
            ],
            "key_rule": "`E = h · f` (color = energía por fotón; brillo = cantidad) · Cada vida media queda `½` · Fisión = partir, Fusión = unir.",
            "pitfall": "Pensar que aumentando el brillo de una luz roja se logra arrancar electrones que requerían luz ultravioleta: si cada fotón no alcanza el umbral, mandar millones de fotones débiles tampoco alcanza.",
        },
        "example": {
            "title": "Datá un fósil usando vidas medias de Carbono-14",
            "steps": [
                "La vida media del Carbono-14 es `5730 años`: cada vez que pasa ese lapso, la cantidad que queda se divide por 2.",
                "Un trozo de madera antigua conserva exactamente el `25%` (`1/4`) del C-14 que tenía un árbol vivo.",
                "Como `100% → 50%` (1 vida media) `→ 25%` (2 vidas medias), la madera tiene aproximadamente `2 × 5730 = 11 460 años`.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "En el efecto fotoeléctrico, aumentás al triple el brillo (intensidad) de una luz que YA logra arrancar electrones. ¿Qué cambia?",
            "options": [
                {"text": "Salen el triple de electrones por segundo (más corriente), con la misma energía máxima por electrón", "ok": True, "feedback": "Exacto: más brillo = más fotones por segundo, pero cada fotón sigue teniendo la misma energía E = h·f."},
                {"text": "Cada electrón sale con el triple de energía", "ok": False, "feedback": "Para darles más energía a cada electrón hay que subir la frecuencia (cambiar de color), no el brillo."},
                {"text": "Dejan de salir electrones por saturación", "ok": False, "feedback": "Al contrario, aumenta proporcionalmente la fotocorriente."},
            ],
        },
        "checks": [
            {
                "question": "¿Por qué un LED azul necesita mayor voltaje que un LED rojo para encender?",
                "options": [
                    {"text": "Porque los fotones azules tienen mayor frecuencia y energía (`E = h·f`), exigiendo un salto cuántico más grande", "ok": True, "feedback": "Exacto: más energía por fotón se traduce directo en más Voltios (J/C)."},
                    {"text": "Porque el vidrio azul absorbe la mitad de la corriente", "ok": False, "feedback": "El color nace del salto de energía en el cristal semiconductor, no de un plástico pintado."},
                    {"text": "Porque el azul tiene menor frecuencia que el rojo", "ok": False, "feedback": "Es al revés: el azul tiene mayor frecuencia que el rojo (alrededor de un 35% más)."},
                ],
            },
            {
                "question": "Un isótopo médico tiene una vida media de 2 horas. Si empezás con 80 mg, ¿cuántos mg quedan después de 6 horas?",
                "options": [
                    {"text": "20 mg", "ok": False, "feedback": "6 horas son 3 vidas medias (6 ÷ 2 = 3), no 2."},
                    {"text": "10 mg", "ok": True, "feedback": "Exacto: 80 → 40 (2 h) → 20 (4 h) → 10 mg (6 h)."},
                    {"text": "0 mg", "ok": False, "feedback": "El decaimiento radiactivo reduce a la mitad en cada ciclo, no se agota linealmente."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué diferencia hay entre subir el brillo vs. subir la frecuencia de la luz en términos de fotones.",
    },
}

# Detailed mechanics for the engineering entrance exam lives in its own modules. Each of
# those nodes names the existing node it follows; positions and "N." prefixes are derived.
from backend.content_merge import insert_nodes, renumber  # noqa: E402
from backend.dynamics_content import DYNAMICS_LESSONS, DYNAMICS_NODES  # noqa: E402
from backend.ingreso_physics_a_content import INGRESO_PHYSICS_A_LESSONS, INGRESO_PHYSICS_A_NODES  # noqa: E402
from backend.ingreso_physics_b_content import INGRESO_PHYSICS_B_LESSONS, INGRESO_PHYSICS_B_NODES  # noqa: E402
from backend.kinematics_content import KINEMATICS_LESSONS, KINEMATICS_NODES  # noqa: E402

# Units, significant figures, dimensional analysis and statics follow the UNCuyo 2027 entrance syllabus.
insert_nodes(PHYSICS_DOMAIN["nodes"], KINEMATICS_NODES + DYNAMICS_NODES + INGRESO_PHYSICS_A_NODES + INGRESO_PHYSICS_B_NODES)
renumber(PHYSICS_DOMAIN["nodes"])
PHYSICS_LESSONS.update(KINEMATICS_LESSONS)
PHYSICS_LESSONS.update(DYNAMICS_LESSONS)
PHYSICS_LESSONS.update(INGRESO_PHYSICS_A_LESSONS)
PHYSICS_LESSONS.update(INGRESO_PHYSICS_B_LESSONS)
