"""Estática del ingreso a Ingeniería UNCuyo (Unidad 4 del programa).

En el curso de ingreso la estática se da ANTES que la dinámica, así que estos dos nodos abren una
sección "Estática" a continuación de la cinemática:
  - Resultante, equilibrante y equilibrio de fuerzas concurrentes
  - Momento de una fuerza, cupla, vínculos y equilibrio de cuerpos

Convenciones del material: g = 9,8 m/s²; ángulos de las fuerzas medidos desde el semieje x positivo
en sentido antihorario; momento positivo antihorario (N·m); fuerzas en N, kgf y dyn.
"""

from __future__ import annotations

_SECTION = "Estática"

INGRESO_PHYSICS_B_NODES: list[dict] = [
    # ==================== FUERZAS CONCURRENTES ====================
    {
        "slug": "f-estatica-concurrentes",
        "title": "Estática: resultante, equilibrante y equilibrio de fuerzas concurrentes",
        "summary": "Sumar fuerzas por componentes con ángulos desde el semieje x positivo, hallar resultante y equilibrante, y plantear ΣFx = 0 y ΣFy = 0 en nudos, planos inclinados y apoyos.",
        "prerequisites": ["f-vectores-operaciones"],
        "insert_after": "f-tiro-oblicuo",
        "metadata": {"section": _SECTION, "lab_tab": "forces", "est_minutes": 30},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Resultante de dos fuerzas dadas en kgf y en dyn",
                "prompt": "Sobre un cuerpo actúan dos fuerzas con la misma dirección y el mismo sentido: una de 15 kgf y otra de 3·10⁶ dyn. Usá 1 kgf = 9,8 N y 1 N = 10⁵ dyn. ¿Cuánto vale la resultante en newton? Respondé solo con el número en N.",
                "answer": "177 N: 15 kgf · 9,8 N/kgf = 147 N y 3·10⁶ dyn ÷ 10⁵ dyn/N = 30 N. Como son colineales y del mismo sentido, se suman: 147 N + 30 N = 177 N. Antes de sumar, todas las fuerzas tienen que estar en la misma unidad (en el SI, newton).",
                "hints": [
                    "Pasá cada fuerza a newton por separado: el kgf se multiplica por 9,8 y los dyn se dividen por 10⁵.",
                    "Fuerzas de igual dirección y sentido se suman como números.",
                ],
                "payload": {"check": {"type": "numeric", "value": 177, "tolerance": 0, "unit": "N"}},
            },
            {
                "item_type": "recall",
                "title": "Signo de la componente y de una fuerza a 210°",
                "prompt": "Una fuerza de 60 N forma 210° con el semieje x positivo (medidos en sentido antihorario). ¿Cuánto vale su componente Fy, con su signo? Respondé solo con el número en N.",
                "answer": "−30 N: Fy = 60 N · sen 210° = 60 N · (−0,5) = −30 N. Con el ángulo medido desde el semieje x positivo, la calculadora pone el signo sola: la fuerza apunta al III cuadrante (abajo y a la izquierda), así que Fy es negativa. La otra componente es Fx = 60 N · cos 210° ≈ −52,0 N.",
                "hints": ["Fy = F · sen α, con α medido desde el semieje x positivo; no hace falta poner el signo a mano."],
                "payload": {"check": {"type": "numeric", "value": -30, "tolerance": 0, "unit": "N"}},
            },
            {
                "item_type": "worked_example",
                "title": "Módulo de la resultante de tres fuerzas concurrentes",
                "prompt": "Tres fuerzas concurrentes actúan sobre un punto: F1 = 150 N a 30°, F2 = 100 N a 135° y F3 = 80 N a 270° (ángulos desde el semieje x positivo, en sentido antihorario). ¿Cuál es el módulo de la resultante? Respondé solo con el número en N, redondeado a un decimal.",
                "answer": "88,4 N: componentes x: 150·cos 30° = 129,9 N; 100·cos 135° = −70,7 N; 80·cos 270° = 0 → Rx = 59,2 N. Componentes y: 150·sen 30° = 75 N; 100·sen 135° = 70,7 N; 80·sen 270° = −80 N → Ry = 65,7 N. R = √(59,2² + 65,7²) = 88,4 N, a arctg(65,7/59,2) ≈ 48° (I cuadrante: las dos componentes son positivas). Sumar los módulos (330 N) no tiene sentido porque las fuerzas no son paralelas.",
                "hints": [
                    "Armá una tabla: Fx = F·cos α y Fy = F·sen α para cada fuerza, y sumá cada columna.",
                    "Con Rx y Ry, el módulo sale por Pitágoras.",
                ],
                "payload": {"check": {"type": "numeric", "value": 88.4, "tolerance": 0.005, "unit": "N"}},
            },
            {
                "item_type": "recall",
                "title": "Ángulo de una resultante del segundo cuadrante en grados y minutos",
                "prompt": "La resultante de un sistema tiene Rx = −40 N y Ry = 30 N. ¿Qué ángulo forma con el semieje x positivo?",
                "answer": "143°8': la calculadora da arctg(30/−40) = −36,87°, que es un ángulo del IV cuadrante. Pero Rx < 0 y Ry > 0 ubican a R en el II cuadrante, así que hay que sumar 180°: −36,87° + 180° = 143,13°. Para pasar a minutos: 0,13° · 60 = 7,8' ≈ 8'. Resultado: 143°8'.",
                "hints": [
                    "Primero mirá los signos de Rx y Ry para saber en qué cuadrante está R.",
                    "La arcotangente de la calculadora solo devuelve ángulos entre −90° y 90°; los minutos salen de multiplicar la parte decimal por 60.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["143°8'", "−36°52'", "36°52'", "216°52'"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Ángulo de la equilibrante de una resultante a 300°",
                "prompt": "La resultante de un sistema de fuerzas concurrentes mide 50 N y forma 300° con el semieje x positivo. ¿Qué ángulo forma la equilibrante con el semieje x positivo? Respondé solo con el número en grados, entre 0° y 360°.",
                "answer": "120°: la equilibrante tiene el mismo módulo (50 N) y la misma dirección que la resultante, pero sentido opuesto, así que su ángulo difiere en 180°. Como R está en el IV cuadrante, se resta: 300° − 180° = 120° (II cuadrante). Si R estuviera en el I o II cuadrante, se sumarían 180°.",
                "hints": ["Sentido opuesto = girar 180°. Elegí sumar o restar para que el resultado quede entre 0° y 360°."],
                "payload": {"check": {"type": "numeric", "value": 120, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "recall",
                "title": "Equilibrio de un cuerpo con movimiento rectilíneo uniforme",
                "prompt": "Un bloque se desliza sobre una mesa con movimiento rectilíneo uniforme. Desde el punto de vista de la Estática, ¿está en equilibrio?",
                "answer": "Sí: un cuerpo está en equilibrio cuando está en reposo o en movimiento rectilíneo uniforme. En los dos casos la resultante de las fuerzas es nula (ΣFx = 0 y ΣFy = 0). Que se mueva no implica que haya una fuerza neta en el sentido del movimiento.",
                "hints": ["Recordá la definición de equilibrio que da el material: hay dos situaciones posibles, no una."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Sí: la resultante es nula, y eso vale tanto en reposo como en MRU",
                            "No: solo está en equilibrio un cuerpo en reposo",
                            "No: si se mueve, la resultante apunta en el sentido del movimiento",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Tensión de la cadena horizontal que sostiene un anillo",
                "prompt": "Una lámpara de 200 N cuelga de una cadena vertical unida a un anillo. Del anillo salen otras dos cadenas: una horizontal hasta la pared y otra hasta el techo, que forma 40° con la horizontal. Los pesos de las cadenas y del anillo son despreciables. ¿Cuál es la tensión de la cadena horizontal? Respondé solo con el número en N, redondeado a un decimal.",
                "answer": "238,4 N: en el diagrama de cuerpo libre del anillo, la cadena del techo tira a 40°, la de la pared a 180° y la de la lámpara a 270° con 200 N. ΣFy = 0: T·sen 40° − 200 N = 0 → T = 311,1 N (la cadena inclinada). ΣFx = 0: T·cos 40° − Th = 0 → Th = 311,1 N · cos 40° = 238,4 N. Las dos cadenas tiran más que el peso de la lámpara.",
                "hints": [
                    "La cadena horizontal no tiene componente vertical: con ΣFy = 0 sale primero la tensión de la cadena inclinada.",
                    "Después usá ΣFx = 0 en el anillo.",
                ],
                "payload": {"check": {"type": "numeric", "value": 238.4, "tolerance": 0.005, "unit": "N"}},
            },
            {
                "item_type": "worked_example",
                "title": "Tensión de una soga en un nudo con ángulos de 45° y 30°",
                "prompt": "Un cartel de 150 N cuelga de un nudo del que salen dos sogas: la soga A va hacia la derecha formando 45° con la horizontal y la soga B va hacia la izquierda formando 30° con la horizontal. ¿Cuánto vale la tensión de la soga B? Respondé solo con el número en N, redondeado a un decimal.",
                "answer": "109,8 N: con los ángulos desde el semieje x positivo, TA va a 45°, TB a 150° y el peso a 270°. ΣFx = 0: TA·cos 45° + TB·cos 150° = 0 → TA = 1,2247·TB. ΣFy = 0: TA·sen 45° + TB·sen 150° − 150 N = 0 → 0,8660·TB + 0,5·TB = 150 N → TB = 109,8 N (y TA = 134,5 N). La soga más empinada carga más.",
                "hints": [
                    "La soga B apunta hacia arriba y a la izquierda: su ángulo desde el semieje x positivo es 180° − 30°.",
                    "De ΣFx = 0 despejá TA en función de TB y reemplazalo en ΣFy = 0.",
                ],
                "payload": {"check": {"type": "numeric", "value": 109.8, "tolerance": 0.005, "unit": "N"}},
            },
            {
                "item_type": "worked_example",
                "title": "Fuerza horizontal que mantiene un bloque en un plano liso",
                "prompt": "Un bloque de 120 N se mantiene en reposo sobre un plano inclinado 25° respecto de la horizontal, sin rozamiento, empujado por una fuerza F horizontal. ¿Cuánto vale F? Respondé solo con el número en N, redondeado a un decimal.",
                "answer": "56,0 N: tomando el eje x paralelo al plano y el y perpendicular, la componente del peso a lo largo del plano es P·sen 25° (cuesta abajo) y la de F es F·cos 25° (cuesta arriba). ΣFx = 0: F·cos 25° = P·sen 25° → F = P·tg 25° = 120 N · 0,4663 = 56,0 N. Con ΣFy = 0 sale la normal: N = P·cos 25° + F·sen 25° = 132,4 N, mayor que el peso porque F también aprieta el bloque contra el plano.",
                "hints": [
                    "Usá un eje paralelo al plano: así la normal no aparece en la ecuación de ese eje.",
                    "A lo largo del plano, la fuerza horizontal aporta F·cos 25° y el peso P·sen 25°.",
                ],
                "payload": {"check": {"type": "numeric", "value": 56.0, "tolerance": 0.005, "unit": "N"}},
            },
            {
                "item_type": "worked_example",
                "title": "Reacción de la pared sobre una esfera apoyada en un plano",
                "prompt": "Una esfera homogénea de 4 kg está quieta entre una pared vertical lisa y un plano liso inclinado 30° respecto de la horizontal, que baja hacia la pared. Usá g = 9,8 m/s². ¿Cuánto vale la reacción de la pared sobre la esfera? Respondé solo con el número en N, redondeado a un decimal.",
                "answer": "22,6 N: las tres fuerzas pasan por el centro de la esfera (sistema concurrente): el peso P = 4·9,8 = 39,2 N, la normal de la pared (horizontal, alejándose de la pared) y la normal del plano (perpendicular al plano, inclinada 30° respecto de la vertical). ΣFy = 0: Nplano·cos 30° = 39,2 N → Nplano = 45,3 N. ΣFx = 0: Npared = Nplano·sen 30° = 22,6 N (es decir, P·tg 30°).",
                "hints": [
                    "Cada superficie lisa empuja perpendicular a sí misma: la normal del plano forma 30° con la vertical.",
                    "Con ΣFy = 0 sacá la normal del plano y después usá ΣFx = 0.",
                ],
                "payload": {"check": {"type": "numeric", "value": 22.6, "tolerance": 0.005, "unit": "N"}},
            },
        ],
    },
    # ==================== MOMENTO, CUPLA Y VÍNCULOS ====================
    {
        "slug": "f-momento-cupla-vinculos",
        "title": "Momento de una fuerza, cupla, vínculos y equilibrio de cuerpos",
        "summary": "Calcular momentos con signo, usar el teorema de los momentos, reconocer cuplas y vínculos, y resolver vigas, barras articuladas y palancas con ΣFx = 0, ΣFy = 0 y ΣM = 0.",
        "prerequisites": ["f-estatica-concurrentes"],
        "insert_after": "f-estatica-concurrentes",
        "metadata": {"section": _SECTION, "lab_tab": "forces", "est_minutes": 35},
        "items": [
            {
                "item_type": "recall",
                "title": "Signo del momento de una fuerza que gira en sentido horario",
                "prompt": "Una llave de 0,30 m tiene la tuerca O en su extremo izquierdo. En el extremo derecho aplicás una fuerza de 40 N perpendicular a la llave, hacia abajo. ¿Cuánto vale el momento respecto de O, con su signo (antihorario positivo)? Respondé solo con el número en N·m.",
                "answer": "−12 N·m: en módulo, M = F·d = 40 N · 0,30 m = 12 N·m. Una fuerza hacia abajo aplicada a la derecha de O haría girar la llave en sentido horario, así que el momento es negativo: M = −12 N·m.",
                "hints": [
                    "Módulo: fuerza por distancia perpendicular desde O hasta la recta de acción.",
                    "Imaginá hacia dónde giraría la llave alrededor de O: horario es negativo.",
                ],
                "payload": {"check": {"type": "numeric", "value": -12, "tolerance": 0, "unit": "N·m"}},
            },
            {
                "item_type": "worked_example",
                "title": "Momento de una fuerza oblicua con M = F·r·sen θ",
                "prompt": "Una barra horizontal de 1,2 m puede girar alrededor de su extremo izquierdo O. En el extremo derecho se aplica una fuerza de 90 N dirigida hacia arriba y a la derecha, que forma 30° con la barra. ¿Cuánto vale el momento respecto de O, con su signo? Respondé solo con el número en N·m.",
                "answer": "54 N·m: M = F·r·sen θ = 90 N · 1,2 m · sen 30° = 54 N·m, positivo porque la fuerza tira hacia arriba desde la derecha de O (giro antihorario). Es lo mismo que multiplicar la componente perpendicular a la barra (90·sen 30° = 45 N) por 1,2 m: la componente a lo largo de la barra pasa por O y no hace momento.",
                "hints": [
                    "θ es el ángulo entre el vector posición (la barra) y la fuerza.",
                    "Solo la componente de la fuerza perpendicular a la barra la hace girar.",
                ],
                "payload": {"check": {"type": "numeric", "value": 54, "tolerance": 0, "unit": "N·m"}},
            },
            {
                "item_type": "worked_example",
                "title": "Momento de una fuerza con el teorema de los momentos",
                "prompt": "Una fuerza de componentes Fx = 40 N (hacia la derecha) y Fy = 60 N (hacia arriba) está aplicada en el punto (2; 1,5) m. Usando el teorema de los momentos, ¿cuánto vale su momento respecto del origen O, con su signo? Respondé solo con el número en N·m.",
                "answer": "60 N·m: por el teorema de los momentos (de Varignon), el momento de F es la suma algebraica de los momentos de sus componentes. Fy = 60 N tiene brazo 2 m y, al empujar hacia arriba a la derecha de O, gira antihorario: +120 N·m. Fx = 40 N tiene brazo 1,5 m y, al tirar hacia la derecha por encima de O, gira horario: −60 N·m. Total: 120 − 60 = 60 N·m.",
                "hints": [
                    "El brazo de la componente vertical es la distancia horizontal a O, y el de la horizontal es la altura del punto.",
                    "Decidí el signo de cada componente por separado según el giro que produciría alrededor de O.",
                ],
                "payload": {"check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": "N·m"}},
            },
            {
                "item_type": "worked_example",
                "title": "Momento de una cupla respecto de un punto fuera de la barra",
                "prompt": "Sobre una barra horizontal actúan dos fuerzas verticales de 25 N: en x = 0 una hacia abajo y en x = 0,8 m otra hacia arriba. ¿Cuánto vale el momento del sistema respecto de un punto P ubicado en x = −2 m (fuera de la barra), con su signo? Respondé solo con el número en N·m.",
                "answer": "20 N·m: respecto de P, la fuerza hacia abajo tiene brazo 2 m y gira en sentido horario: −25·2 = −50 N·m; la fuerza hacia arriba tiene brazo 2,8 m y gira antihorario: +25·2,8 = +70 N·m. Total: +20 N·m, que es exactamente F·d = 25 N · 0,8 m. Es una cupla: su resultante es nula y su momento es el mismo respecto de cualquier punto.",
                "hints": [
                    "Calculá el momento de cada fuerza respecto de P: el brazo es la distancia horizontal desde P hasta cada fuerza.",
                    "Fijate el sentido de giro de cada una alrededor de P antes de sumar.",
                ],
                "payload": {"check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "N·m"}},
            },
            {
                "item_type": "recall",
                "title": "Reacciones que introduce una articulación o apoyo fijo",
                "prompt": "En un diagrama de cuerpo libre reemplazás una articulación (apoyo fijo) por su reacción. ¿Cuántas incógnitas aporta y cuáles son?",
                "answer": "Dos: Rx y Ry. La articulación impide toda traslación pero deja girar, y no se sabe de antemano ni el módulo ni la dirección de su reacción, así que se dibujan sus dos proyecciones en el sentido que se suponga. En cambio, el apoyo móvil (simple) da una sola reacción, perpendicular a la superficie de apoyo, y el empotramiento, que además impide girar, da tres: Rx, Ry y un momento.",
                "hints": ["Pensá qué movimientos impide la articulación: puede trasladarse en x, en y, ¿y puede girar?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Dos: las proyecciones Rx y Ry, porque no se conoce ni el módulo ni la dirección de la reacción",
                            "Una sola reacción, perpendicular a la superficie de apoyo",
                            "Tres: Rx, Ry y un momento que impide el giro",
                            "Ninguna: como la articulación deja girar, no ejerce fuerza",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Recta de acción de la resultante de fuerzas paralelas",
                "prompt": "Una barra horizontal recibe tres fuerzas verticales: 200 N hacia abajo a 1 m del extremo O, 300 N hacia abajo a 3 m de O y 100 N hacia arriba a 4 m de O. ¿A qué distancia de O pasa la recta de acción de la resultante? Respondé solo con el número en m.",
                "answer": "1,75 m: la resultante es R = −200 − 300 + 100 = −400 N (400 N hacia abajo). El momento del sistema respecto de O es −200·1 − 300·3 + 100·4 = −700 N·m. Por el teorema de los momentos, la resultante sola debe producir ese mismo momento: −400 N · x = −700 N·m → x = 1,75 m a la derecha de O.",
                "hints": [
                    "Calculá por separado la resultante (suma con signo) y el momento total respecto de O.",
                    "La resultante ubicada a una distancia x de O tiene que dar el mismo momento que todo el sistema.",
                ],
                "payload": {"check": {"type": "numeric", "value": 1.75, "tolerance": 0, "unit": "m"}},
            },
            {
                "item_type": "worked_example",
                "title": "Reacción negativa en una viga con un extremo en voladizo",
                "prompt": "Una viga AC de 3 m pesa 300 N (aplicados en su punto medio) y está articulada en A (extremo izquierdo) y apoyada en B, a 2 m de A. Del extremo C cuelga una carga de 400 N. Suponiendo las dos reacciones hacia arriba, ¿cuánto vale la reacción en A? Respondé solo con el número en N, con su signo.",
                "answer": "−125 N: ΣMA = 0: RB·2 m − 300 N·1,5 m − 400 N·3 m = 0 → RB = 825 N. ΣFy = 0: RA + 825 N − 300 N − 400 N = 0 → RA = −125 N. El signo menos indica que el sentido supuesto era el contrario: en A el vínculo tira la viga hacia abajo con 125 N, como en un trampolín.",
                "hints": [
                    "Tomá momentos respecto de A: RA desaparece y queda RB sola.",
                    "Después usá ΣFy = 0 y no cambies el signo que te dé: interpretalo.",
                ],
                "payload": {"check": {"type": "numeric", "value": -125, "tolerance": 0, "unit": "N"}},
            },
            {
                "item_type": "worked_example",
                "title": "Reacción del apoyo móvil con una carga inclinada",
                "prompt": "Una viga de 5 m, de peso despreciable, tiene una articulación en A (extremo izquierdo) y un apoyo móvil en B (extremo derecho, reacción vertical). A 3 m de A recibe una fuerza de 4000 N dirigida hacia abajo y a la derecha, que forma 60° con la viga. ¿Cuánto vale la reacción del apoyo móvil B? Respondé solo con el número en N, redondeado a un decimal.",
                "answer": "2078,5 N: la fuerza se descompone en 4000·sen 60° = 3464,1 N hacia abajo y 4000·cos 60° = 2000 N hacia la derecha. La componente horizontal actúa a lo largo de la viga, pasa por A y no hace momento; la toma la articulación (RAx = 2000 N hacia la izquierda), porque el apoyo móvil no puede. ΣMA = 0: RB·5 m − 3464,1 N·3 m = 0 → RB = 2078,5 N. Con ΣFy = 0, RAy = 1385,6 N.",
                "hints": [
                    "Descomponé la fuerza inclinada en una componente perpendicular a la viga y otra a lo largo de ella.",
                    "Tomá momentos respecto de A: ¿cuál de las dos componentes tiene brazo?",
                ],
                "payload": {"check": {"type": "numeric", "value": 2078.5, "tolerance": 0.005, "unit": "N"}},
            },
            {
                "item_type": "worked_example",
                "title": "Módulo de la reacción en una barra articulada con cuerda horizontal",
                "prompt": "Una barra de 400 N (peso aplicado en su punto medio) está articulada en A, al pie de una pared vertical, y sube alejándose de la pared formando 60° con ella. De su extremo superior cuelga una carga de 200 N y una cuerda horizontal une ese extremo con la pared. ¿Cuál es el módulo de la reacción en la articulación A? Respondé solo con el número en N, redondeado a un decimal.",
                "answer": "916,5 N: con L el largo de la barra, los pesos tienen brazos horizontales (L/2)·sen 60° y L·sen 60°, y la tensión tiene brazo vertical L·cos 60°. ΣMA = 0: T·L·cos 60° = 400·(L/2)·sen 60° + 200·L·sen 60° → T = 400 N·tg 60° = 692,8 N (L se simplifica). ΣFx = 0: RAx = 692,8 N, alejándose de la pared. ΣFy = 0: RAy = 400 + 200 = 600 N. |RA| = √(692,8² + 600²) = 916,5 N, a arctg(600/692,8) = 40°54' de la horizontal.",
                "hints": [
                    "Tomá momentos respecto de A para sacar la tensión: la reacción de la articulación no aparece.",
                    "Después, ΣFx = 0 y ΣFy = 0 te dan RAx y RAy; el módulo sale por Pitágoras.",
                ],
                "payload": {"check": {"type": "numeric", "value": 916.5, "tolerance": 0.005, "unit": "N"}},
            },
            {
                "item_type": "recall",
                "title": "Género de la palanca de una carretilla",
                "prompt": "En una carretilla, la rueda es el punto de apoyo, la carga va en el medio y vos hacés fuerza en los mangos. ¿De qué género es esta palanca?",
                "answer": "Segundo género: la resistencia (la carga) está entre el apoyo (la rueda) y la potencia (tus manos). Como el brazo de potencia es más largo que el de resistencia, hacés menos fuerza que el peso de la carga. En la de primer género el apoyo está en el medio (balancín, tijera, alicate); en la de tercer género la potencia está en el medio (pinza de depilar, el antebrazo movido por el bíceps).",
                "hints": ["Fijate qué elemento queda en el medio: el apoyo, la resistencia o la potencia."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Primer género", "Segundo género", "Tercer género"],
                        "correct": 1,
                    },
                },
            },
        ],
    },
]


INGRESO_PHYSICS_B_LESSONS: dict[str, dict] = {
    "f-estatica-concurrentes": {
        "hook": {
            "question": "Un semáforo de 100 N cuelga de dos cables, uno a 30° y otro a 60° de la horizontal. ¿Cada cable sostiene la mitad del peso, 50 N?",
            "intuition": "No: el cable de 60° soporta unos 86,6 N y el de 30° unos 50 N, y entre los dos suman más que el peso. Cada cable tira **en su propia dirección**, y solo sus componentes verticales sostienen al semáforo. Para saber cuánto tira cada uno hay que descomponer las fuerzas y pedir que se anulen en cada eje: eso es la **Estática**.",
        },
        "concept": {
            "points": [
                "**Fuerza y sistemas de fuerzas**: la fuerza es un vector (módulo, dirección, sentido y punto de aplicación). Un **sistema de fuerzas** es el conjunto de fuerzas que actúan sobre un mismo cuerpo; es **concurrente** si todas sus rectas de acción pasan por un mismo punto. Antes de operar, todo a newton: `1 kgf = 9,8 N` y `1 N = 10⁵ dyn`.",
                "**Resultante por componentes**: con cada ángulo `α` medido desde el semieje x positivo en sentido antihorario, `Fx = F·cos α` y `Fy = F·sen α` salen con su signo solo. Después `Rx = ΣFx`, `Ry = ΣFy` y `R = √(Rx² + Ry²)`. La resultante es una única fuerza que produce el mismo efecto que todo el sistema.",
                "**Ángulo de la resultante**: `arctg(Ry/Rx)` de la calculadora solo da ángulos entre −90° y 90°. Ubicá el cuadrante con los signos de Rx y Ry: en el I queda igual; en el II y el III se suman 180°; en el IV se suman 360°. El material lo informa en grados y minutos: la parte decimal por 60 (`74,37° = 74°22'`).",
                "**Equilibrante**: fuerza de igual módulo, misma dirección, mismo punto de aplicación y **sentido opuesto** a la resultante. Su ángulo es `αR + 180°` si R está en el I o II cuadrante y `αR − 180°` si está en el III o IV.",
                "**Primera condición de equilibrio**: un cuerpo está en equilibrio si está en reposo o en MRU; con fuerzas concurrentes eso exige `ΣFx = 0` y `ΣFy = 0`. Son dos ecuaciones, así que se pueden despejar hasta dos incógnitas. El **diagrama de cuerpo libre** (DCL) dibuja solo las fuerzas sobre el nudo o el cuerpo: cada soga tira desde el nudo a lo largo de sí misma.",
                "**Superficies lisas**: la normal es perpendicular a la superficie. En un plano inclinado `θ` conviene un eje paralelo al plano: el peso aporta `P·sen θ` a lo largo del plano y `P·cos θ` contra él. Con una fuerza paralela al plano, `F = P·sen θ`; con una fuerza horizontal, `F = P·tg θ` y `N = P/cos θ`.",
            ],
            "real_world": [
                {
                    "title": "Semáforos y cables de tendido",
                    "detail": "Los cables que sostienen un semáforo o un cartel en una esquina se calculan con ΣFx = 0 y ΣFy = 0 en el punto de enganche: si los cables se acercan a la horizontal (menos flecha), la tensión de cada uno crece mucho aunque el peso sea el mismo.",
                },
                {
                    "title": "Remolcadores en el puerto",
                    "detail": "Dos remolcadores tiran de una barcaza con cabos en direcciones distintas: el práctico calcula la resultante por componentes para saber hacia dónde y con cuánta fuerza se moverá.",
                },
                {
                    "title": "Rampas y carga de camiones",
                    "detail": "Para sostener un tambor sobre una rampa alcanza con una fuerza P·sen θ a lo largo de ella; empujando horizontalmente hace falta más (P·tg θ) y además aumenta la fuerza contra la rampa.",
                },
            ],
            "key_rule": "Fx = F·cos α y Fy = F·sen α (α desde x+, antihorario) · R = √(Rx² + Ry²) y cuadrante por los signos · Equilibrante: mismo módulo, ángulo ± 180° · Equilibrio: ΣFx = 0 y ΣFy = 0.",
            "pitfall": "Copiar el ángulo que da la calculadora sin mirar los signos de Rx y Ry (por ejemplo, informar −36°52' para una resultante del II cuadrante), o mezclar en un mismo problema ángulos medidos desde el eje x con ángulos medidos desde el eje y: los signos de las componentes salen mal.",
        },
        "example": {
            "title": "Tensiones de los dos cables que sostienen un semáforo",
            "steps": [
                "Situación: un semáforo de 100 N cuelga de un nudo; el cable A va hacia la derecha a 30° de la horizontal y el cable B hacia la izquierda a 60° de la horizontal. **DCL del nudo**: `TA` a 30°, `TB` a 180° − 60° = 120° y el peso de 100 N a 270°.",
                "**ΣFx = 0**: `TA·cos 30° + TB·cos 120° = 0` → `0,866·TA − 0,5·TB = 0` → `TA = 0,577·TB`.",
                "**ΣFy = 0**: `TA·sen 30° + TB·sen 120° − 100 N = 0` → `0,5·TA + 0,866·TB = 100 N`.",
                "Reemplazando `TA`: `0,289·TB + 0,866·TB = 100 N` → `1,155·TB = 100 N` → **`TB = 86,6 N`**, y **`TA = 0,577 · 86,6 N = 50 N`**.",
                "Control: las componentes horizontales valen `50·cos 30° = 43,3 N` y `86,6·cos 60° = 43,3 N` (se anulan) y las verticales `25 N + 75 N = 100 N`. El cable más empinado carga más peso.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "La resultante de un sistema mide 73,1 N y forma 29° con el semieje x positivo. ¿Cuál es la equilibrante?",
            "options": [
                {"text": "73,1 N a 209°", "ok": True, "feedback": "Exacto: mismo módulo y misma dirección, sentido opuesto. R está en el I cuadrante, así que se suman 180°: 29° + 180° = 209° (III cuadrante)."},
                {"text": "73,1 N a 151°", "ok": False, "feedback": "151° = 180° − 29° es el reflejo de R respecto del eje y, no su opuesto: esa fuerza no anula a R, porque su componente y tiene el mismo signo."},
                {"text": "−73,1 N a 29°", "ok": False, "feedback": "El módulo de una fuerza nunca es negativo: el sentido opuesto se indica cambiando el ángulo en 180°, no poniéndole signo menos al módulo."},
            ],
        },
        "checks": [
            {
                "question": "Una caja de 400 N está en reposo sobre un plano inclinado 20°, sin rozamiento, sostenida por una fuerza F paralela al plano. ¿Cuánto vale F?",
                "options": [
                    {"text": "136,8 N", "ok": True, "feedback": "Exacto: a lo largo del plano, F equilibra la componente del peso P·sen 20° = 400 N · 0,342 = 136,8 N."},
                    {"text": "375,9 N", "ok": False, "feedback": "Eso es P·cos 20°, la componente del peso perpendicular al plano: la equilibra la normal, no F."},
                    {"text": "145,6 N", "ok": False, "feedback": "Eso es P·tg 20°, la fuerza necesaria si F fuera horizontal. Con F paralela al plano, alcanza con P·sen 20°."},
                ],
            },
            {
                "question": "La resultante de un sistema tiene Rx = 63,4 N y Ry = −35,8 N. ¿Qué ángulo forma con el semieje x positivo?",
                "options": [
                    {"text": "330°33'", "ok": True, "feedback": "Exacto: arctg(35,8/63,4) = 29°27' es el ángulo de referencia; con Rx > 0 y Ry < 0 la resultante está en el IV cuadrante: 360° − 29°27' = 330°33'."},
                    {"text": "209°27'", "ok": False, "feedback": "Sumar 180° la manda al III cuadrante, donde Rx sería negativa. Acá Rx es positiva."},
                    {"text": "150°33'", "ok": False, "feedback": "180° − 29°27' es un ángulo del II cuadrante, con Rx negativa y Ry positiva: los signos están al revés."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras cómo ubicás el ángulo de la resultante según los signos de Rx y Ry, y por qué la equilibrante tiene el ángulo de la resultante ± 180°.",
    },
    "f-momento-cupla-vinculos": {
        "hook": {
            "question": "¿Por qué una puerta se abre fácil si empujás cerca del picaporte y casi no se mueve si empujás con la misma fuerza al lado de las bisagras?",
            "intuition": "Porque lo que hace girar no es solo la fuerza, sino la fuerza **por la distancia** desde el eje hasta su recta de acción: el **momento**. Cerca de las bisagras esa distancia es casi cero. En un cuerpo extenso, para que haya equilibrio no alcanza con que las fuerzas se anulen: también tienen que anularse los momentos.",
        },
        "concept": {
            "points": [
                "**Momento de una fuerza** respecto de un centro O: `M = F·d`, con `d` la distancia perpendicular de O a la recta de acción, o `M = F·r·sen θ`, con `θ` el ángulo entre el vector posición y la fuerza. Unidad: `N·m` (el material escribe N.m; no es joule). **Signo**: positivo si la fuerza haría girar en sentido antihorario y negativo si es horario. Si la recta de acción pasa por O, `M = 0`. En otros temas de la app el momento aparece como **torque** o torca, `τ`.",
                "**Teorema de los momentos (de Varignon)**: el momento de un sistema es la suma algebraica de los momentos de sus fuerzas y, si el sistema tiene resultante, es igual al momento de la resultante. Sirve para calcular el momento de una fuerza sumando los de sus componentes y para ubicar la **recta de acción de la resultante** de fuerzas no concurrentes: si R corta al eje x en A, `M₀ = Ry·OA` → `OA = M₀/Ry`.",
                "**Cupla** (par de fuerzas): dos fuerzas paralelas, de igual intensidad y sentido contrario, con rectas de acción distintas. Su resultante es nula, pero produce rotación pura, y su momento (`F·d`, con `d` la distancia entre las rectas) es el mismo respecto de **cualquier** punto. No se equilibra con una sola fuerza: hace falta otra cupla de momento opuesto.",
                "**Vínculos y reacciones**: un vínculo reacciona en la dirección del movimiento que impide y en sentido opuesto. **Cuerda**: tensión a lo largo de ella, siempre tirando. **Superficie lisa**: normal perpendicular a la superficie. **Apoyo móvil** (simple): una reacción, perpendicular a la superficie de apoyo. **Articulación** o apoyo fijo: módulo y dirección desconocidos, se ponen `Rx` y `Ry`. **Empotramiento**: además impide girar, aporta `Rx`, `Ry` y un momento.",
                "**Equilibrio de un cuerpo extenso** (fuerzas no concurrentes): `ΣFx = 0`, `ΣFy = 0` y `ΣM = 0` (segunda condición). Son tres ecuaciones: hasta tres incógnitas. Conviene empezar por momentos respecto del punto donde concurren más incógnitas, porque ahí su brazo es cero. Si una reacción da negativa, su sentido real es el opuesto al supuesto.",
                "**Palanca**: barra rígida que gira sobre un apoyo; en equilibrio, `potencia × brazo de potencia = resistencia × brazo de resistencia`. **Primer género**: el apoyo está en el medio (balancín, tijera). **Segundo**: la resistencia está en el medio (carretilla, cascanueces). **Tercero**: la potencia está en el medio (pinza de depilar, antebrazo con el bíceps).",
            ],
            "real_world": [
                {
                    "title": "Llaves y volantes",
                    "detail": "Una llave cruz más larga afloja una tuerca con menos fuerza (más brazo, mismo momento); al girar un volante con las dos manos aplicás una cupla: el volante no se traslada, solo gira.",
                },
                {
                    "title": "Trampolines y balcones",
                    "detail": "En un trampolín o en una viga en voladizo, con una carga grande en la punta, el apoyo del extremo trasero puede tener que tirar hacia abajo: la ecuación de momentos lo muestra con una reacción negativa.",
                },
                {
                    "title": "Grúas y plumas articuladas",
                    "detail": "La pluma de una grúa está articulada abajo y sostenida por un cable: con ΣM = 0 respecto de la articulación se calcula la tensión del cable, y con ΣFx = 0 y ΣFy = 0 la reacción del perno.",
                },
            ],
            "key_rule": "M = F·d = F·r·sen θ (antihorario +, horario −) · Cupla: R = 0 y momento igual respecto de cualquier punto · Equilibrio: ΣFx = 0, ΣFy = 0 y ΣM = 0.",
            "pitfall": "Usar como brazo la distancia hasta el punto de aplicación en lugar de la distancia perpendicular a la recta de acción (o multiplicar por r sin el sen θ), y olvidarse del signo del momento: sumar todos los momentos como positivos da reacciones falsas.",
        },
        "example": {
            "title": "Reacciones en los apoyos de una barra con un niño encima",
            "steps": [
                "Situación (ejemplo del material): una barra AC de 2,00 m y 300 N está apoyada en A y en B, con AB = 1,75 m. Un niño de 25,00 kg está a 0,600 m de A y en el extremo C actúa una fuerza de 500 N hacia abajo. Peso del niño: `25,00 kg · 9,8 m/s² = 245 N`.",
                "**DCL**: `Ra` hacia arriba en A (x = 0), 245 N hacia abajo en x = 0,600 m, el peso de la barra de 300 N en su punto medio (x = 1,00 m), `Rb` hacia arriba en x = 1,75 m y 500 N hacia abajo en x = 2,00 m. Solo hay fuerzas verticales.",
                "**ΣMA = 0** (así `Ra` no aparece): `−245 N·0,600 m − 300 N·1,00 m + Rb·1,75 m − 500 N·2,00 m = 0` → `Rb = 1447 N·m / 1,75 m` → **`Rb ≈ 827 N`**.",
                "**ΣFy = 0**: `Ra − 245 N − 300 N + Rb − 500 N = 0` → **`Ra ≈ 218 N`**.",
                "Las dos reacciones dieron positivas: los sentidos supuestos (hacia arriba) eran correctos. Control con momentos respecto de B: `−218·1,75 + 245·1,15 + 300·0,75 − 500·0,25 ≈ 0`.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Una barra de 0,58 m está fija en su extremo O y en el otro extremo recibe una fuerza de 42 N dirigida a lo largo de la barra, alejándose de O. ¿Cuánto vale el momento respecto de O?",
            "options": [
                {"text": "0 N·m", "ok": True, "feedback": "Exacto: la recta de acción pasa por O, así que la distancia perpendicular es cero (θ = 0° y sen 0° = 0). Esa fuerza tira de la barra, pero no la hace girar."},
                {"text": "24,36 N·m", "ok": False, "feedback": "Multiplicaste 42 N · 0,58 m, pero el brazo es la distancia perpendicular de O a la recta de acción, que acá es cero."},
                {"text": "−24,36 N·m", "ok": False, "feedback": "No hay giro ni horario ni antihorario: la fuerza actúa sobre la misma recta que pasa por O, así que el momento es nulo, no negativo."},
            ],
        },
        "checks": [
            {
                "question": "Sobre un cuerpo libre, inicialmente en reposo, actúa solamente una cupla. ¿Qué le pasa?",
                "options": [
                    {"text": "Gira sin trasladarse", "ok": True, "feedback": "Exacto: la resultante es nula, así que no se traslada, pero el momento de la cupla no es nulo y produce rotación pura."},
                    {"text": "Queda en equilibrio, porque la resultante es nula", "ok": False, "feedback": "ΣF = 0 no alcanza en un cuerpo extenso: también hace falta ΣM = 0, y el momento de una cupla nunca es cero."},
                    {"text": "Se puede equilibrar agregando una única fuerza bien ubicada", "ok": False, "feedback": "Una única fuerza haría que ΣF ≠ 0. Una cupla solo se equilibra con otra cupla de momento opuesto."},
                ],
            },
            {
                "question": "Con una barra apoyada sobre un tronco querés levantar una piedra de 600 N que está a 0,4 m del apoyo, empujando a 1,2 m del apoyo del otro lado. ¿Qué fuerza tenés que hacer como mínimo?",
                "options": [
                    {"text": "200 N", "ok": True, "feedback": "Exacto: es una palanca de primer género; con momentos respecto del apoyo, F·1,2 m = 600 N·0,4 m → F = 200 N."},
                    {"text": "1800 N", "ok": False, "feedback": "Invertiste los brazos (600·1,2/0,4): el brazo más largo es el tuyo, así que tenés que hacer MENOS fuerza que el peso de la piedra."},
                    {"text": "150 N", "ok": False, "feedback": "Usaste el largo total de la barra (1,6 m) como brazo de potencia: el brazo se mide desde el apoyo, no desde la punta."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras por qué en el equilibrio de un cuerpo extenso no alcanza con ΣF = 0 y por qué conviene tomar momentos respecto de un vínculo.",
    },
}
