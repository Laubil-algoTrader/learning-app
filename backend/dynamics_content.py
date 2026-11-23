"""Dinámica y estática para el ingreso a ingeniería (4 temas nuevos de Física).

Desarrolla con nivel de examen de ingreso lo que `f-leyes-newton` solo presenta:
  - Diagramas de cuerpo libre, normal, rozamiento estático/dinámico y plano inclinado
  - Cuerpos vinculados: sogas y poleas ideales, bloques en contacto, máquina de Atwood
  - Movimiento circular uniforme: T, f, ω, v = ω·r, aceleración centrípeta, transmisiones
  - Estática: equilibrio de la partícula (tensiones) y del cuerpo extenso (momentos)

Convención: en todos los problemas con peso se usa g = 10 m/s² (aclarado en cada consigna).
"""

from __future__ import annotations

DYNAMICS_NODES: list[dict] = [
    # ==================== DCL, ROZAMIENTO Y PLANO INCLINADO ====================
    {
        "slug": "f-dcl-rozamiento-plano",
        "title": "Diagramas de cuerpo libre, rozamiento y plano inclinado",
        "summary": "Qué fuerzas van en un diagrama de cuerpo libre, cuánto vale la normal en cada caso, rozamiento estático vs. dinámico y dinámica en el plano inclinado.",
        "prerequisites": ["f-leyes-newton"],
        "insert_after": "f-leyes-newton",
        "metadata": {"section": "Dinámica y energía", "lab_tab": "forces", "est_minutes": 25},
        "items": [
            {
                "item_type": "recall",
                "title": "Fuerzas en el diagrama de una caja que desliza sola",
                "prompt": "Le das un empujón a una caja y la soltás: sigue deslizando por el piso horizontal hasta frenarse. Mientras desliza, ya sin tu mano, ¿qué fuerzas van en su diagrama de cuerpo libre?",
                "answer": "Peso, normal y rozamiento dinámico. En el diagrama van solo las fuerzas que OTROS cuerpos le hacen a la caja en ese momento: la Tierra (peso) y el piso (normal y rozamiento, contrario al deslizamiento). Tu mano ya no la toca, así que no existe una 'fuerza del empujón': la caja sigue por inercia. La fuerza que la caja le hace al piso va en el diagrama del piso, no en el de la caja.",
                "hints": ["Para cada fuerza preguntate: ¿qué cuerpo se la está haciendo a la caja en este momento?"],
                "payload": {
                    "lab_link": "physics:forces",
                    "check": {
                        "type": "choice",
                        "options": [
                            "Peso, normal, rozamiento y la fuerza del empujón, que la caja sigue llevando",
                            "Peso, normal y rozamiento dinámico (contrario al deslizamiento)",
                            "Peso, normal, rozamiento y la fuerza que la caja le hace al piso",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Cuándo la normal vale exactamente m·g",
                "prompt": "¿En cuál de estas situaciones la fuerza normal sobre una caja de masa m vale exactamente m·g?",
                "answer": "Solo cuando está en reposo sobre un piso horizontal sin otras fuerzas verticales: ahí ΣFy = 0 da N = m·g. En la rampa N = m·g·cos θ (menor); en el ascensor que acelera hacia arriba N = m·(g + a) (mayor); y si la empujás con una fuerza inclinada hacia abajo N = m·g + F·sen θ (mayor). La normal no tiene fórmula fija: sale de la ecuación en la dirección perpendicular a la superficie.",
                "hints": ["La normal se calcula con ΣF en la dirección perpendicular a la superficie, mirando si hay aceleración en esa dirección."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Apoyada en reposo sobre una rampa inclinada",
                            "En el piso de un ascensor que arranca acelerando hacia arriba",
                            "Apoyada en reposo sobre un piso horizontal, sin otras fuerzas verticales",
                            "En un piso horizontal mientras la empujás con una fuerza inclinada hacia abajo",
                        ],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Normal cuando tirás de una soga en ángulo",
                "prompt": "Arrastrás una caja de 20 kg por un piso horizontal tirando de una soga con 50 N, inclinada 37° hacia arriba respecto de la horizontal (sen 37° = 0.6 y cos 37° = 0.8; g = 10 m/s²). La caja no se despega del piso. ¿Cuánto vale la fuerza normal? Respondé solo con el número en N.",
                "answer": "170 N: en el eje vertical no hay aceleración, así que N + F·sen 37° − m·g = 0. Entonces N = m·g − F·sen 37° = 20·10 − 50·0.6 = 200 − 30 = 170 N. La soga sostiene parte del peso, por eso la normal es menor que m·g.",
                "hints": [
                    "Planteá ΣFy = 0 con tres fuerzas verticales: el peso, la normal y la componente vertical de la soga.",
                    "La componente vertical de la soga es F·sen 37° y apunta hacia arriba.",
                ],
                "payload": {"check": {"type": "numeric", "value": 170, "tolerance": 0, "unit": "N"}},
            },
            {
                "item_type": "worked_example",
                "title": "Rozamiento estático cuando el empuje no alcanza",
                "prompt": "Un ropero de 40 kg está apoyado en un piso horizontal (μₑ = 0.5 y μ_d = 0.4; g = 10 m/s²). Lo empujás horizontalmente con 120 N. ¿Cuánto vale la fuerza de rozamiento que le hace el piso? Respondé solo con el número en N.",
                "answer": "120 N: la normal es N = m·g = 400 N y el rozamiento estático máximo es μₑ·N = 0.5·400 = 200 N. Como tu empuje (120 N) no lo supera, el ropero no se mueve y el rozamiento estático se ajusta para empatar al empuje: 120 N. Los 200 N son solo el tope, y μ_d·N = 160 N valdría recién si el ropero deslizara.",
                "hints": [
                    "Primero averiguá si el ropero llega a moverse: compará el empuje con μₑ·N.",
                    "Si no se mueve, ΣFx = 0: el rozamiento estático vale lo mismo que el empuje.",
                ],
                "payload": {
                    "lab_link": "physics:forces",
                    "check": {"type": "numeric", "value": 120, "tolerance": 0, "unit": "N"},
                },
            },
            {
                "item_type": "recall",
                "title": "Dos chicos de distinta masa en un tobogán sin rozamiento",
                "prompt": "Un chico de 30 kg y otro de 60 kg se tiran por el mismo tobogán, que suponemos sin rozamiento. ¿Cómo son sus aceleraciones?",
                "answer": "Iguales. La fuerza que los hace bajar es m·g·sen θ y, al dividir por la masa, queda a = g·sen θ: el chico más pesado recibe el doble de fuerza, pero también tiene el doble de masa para acelerar. (Con rozamiento dinámico de igual μ_d pasa lo mismo: a = g·(sen θ − μ_d·cos θ).)",
                "hints": ["Escribí la 2ª ley en el eje paralelo al plano y fijate qué pasa con m."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "El de 60 kg acelera el doble, porque su peso tira el doble",
                            "El de 30 kg acelera el doble, porque tiene la mitad de inercia",
                            "Iguales: a = g·sen θ no depende de la masa",
                        ],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Aceleración bajando por un plano con rozamiento",
                "prompt": "Una caja de 5 kg baja deslizando por una rampa inclinada 37° (sen 37° = 0.6 y cos 37° = 0.8) con coeficiente de rozamiento dinámico μ_d = 0.25. Usá g = 10 m/s². ¿Con qué aceleración baja? Respondé solo con el número en m/s².",
                "answer": "4 m/s²: componente del peso paralela al plano: m·g·sen 37° = 50·0.6 = 30 N. Normal: N = m·g·cos 37° = 50·0.8 = 40 N. Rozamiento: μ_d·N = 0.25·40 = 10 N, hacia arriba del plano. Entonces a = (30 − 10)/5 = 4 m/s². En general a = g·(sen θ − μ_d·cos θ), sin depender de la masa.",
                "hints": [
                    "Usá un eje paralelo al plano y otro perpendicular: la normal sale del perpendicular (N = m·g·cos θ).",
                    "En el eje paralelo: m·g·sen θ − μ_d·N = m·a.",
                ],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "m/s²"}},
            },
            {
                "item_type": "worked_example",
                "title": "Coeficiente estático a partir del ángulo crítico",
                "prompt": "Apoyás un libro sobre una tabla y la vas inclinando de a poco. El libro empieza a deslizar justo cuando la tabla forma 37° con la horizontal (sen 37° = 0.6 y cos 37° = 0.8). ¿Cuánto vale el coeficiente de rozamiento estático μₑ entre el libro y la tabla? Respondé solo con el número.",
                "answer": "0.75: justo antes de deslizar, el rozamiento estático está en su máximo: m·g·sen θ = μₑ·m·g·cos θ. La masa y g se simplifican y queda μₑ = tan θ = sen 37°/cos 37° = 0.6/0.8 = 0.75.",
                "hints": [
                    "En el ángulo crítico, la componente del peso paralela al plano iguala al rozamiento estático máximo μₑ·N.",
                    "Con N = m·g·cos θ queda μₑ = sen θ / cos θ.",
                ],
                "payload": {"check": {"type": "numeric", "value": 0.75, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Pasos para hallar la aceleración en un plano con rozamiento",
                "prompt": "Ordená los pasos para calcular la aceleración de un bloque que baja deslizando por un plano inclinado con rozamiento.",
                "answer": "Primero el diagrama de cuerpo libre; después los ejes inclinados y la descomposición del peso; del eje perpendicular sale la normal, con ella el rozamiento (μ_d·N), y recién entonces el eje paralelo da la aceleración.",
                "hints": ["El rozamiento necesita la normal, y la normal sale del eje perpendicular al plano."],
                "payload": {
                    "check": {
                        "type": "order",
                        "lines": [
                            "Dibujar el diagrama de cuerpo libre del bloque: peso, normal y rozamiento",
                            "Elegir un eje paralelo al plano y otro perpendicular, y descomponer el peso en esos ejes",
                            "Con el eje perpendicular, obtener la normal: N = m·g·cos θ",
                            "Calcular el rozamiento dinámico: f = μ_d·N",
                            "Con el eje paralelo, plantear m·g·sen θ − f = m·a y despejar a",
                        ],
                    },
                },
            },
        ],
    },
    # ==================== CUERPOS VINCULADOS ====================
    {
        "slug": "f-cuerpos-vinculados",
        "title": "Cuerpos vinculados: sogas, poleas y máquina de Atwood",
        "summary": "Soga y polea ideales, bloques en contacto o unidos por sogas, bloque en la mesa con otro colgante y máquina de Atwood: una ecuación por cuerpo y sumar.",
        "prerequisites": ["f-dcl-rozamiento-plano"],
        "insert_after": "f-dcl-rozamiento-plano",
        "metadata": {"section": "Dinámica y energía", "lab_tab": "forces", "est_minutes": 25},
        "items": [
            {
                "item_type": "recall",
                "title": "Qué garantiza una soga ideal",
                "prompt": "En los problemas de cuerpos vinculados se usa una soga ideal: inextensible y de masa despreciable. ¿Qué consecuencia tiene cada propiedad?",
                "answer": "Inextensible: como la soga no se estira, lo que avanza un cuerpo lo avanza el otro, así que tienen velocidad y aceleración de igual módulo. Sin masa: la fuerza neta sobre la soga es m_soga·a = 0, así que tira igual de sus dos extremos y hay una sola tensión T. Si además la polea es ideal (sin masa y sin rozamiento en el eje), solo cambia la dirección de la soga, no el valor de T.",
                "hints": ["Pensá qué pasaría con las distancias si la soga se estirara, y qué fuerza neta necesita un objeto de masa cero."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Inextensible: la tensión iguala al peso de lo que cuelga. Sin masa: la soga no ejerce fuerza",
                            "Inextensible: los dos cuerpos tienen aceleración de igual módulo. Sin masa: la tensión vale lo mismo en los dos extremos",
                            "Inextensible: la tensión vale lo mismo en los dos extremos. Sin masa: los cuerpos caen con aceleración g",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Fuerza de contacto entre dos cajas empujadas",
                "prompt": "Sobre un piso sin rozamiento hay dos cajas en contacto: A de 4 kg y, delante de ella, B de 2 kg. Empujás horizontalmente a la caja A con 30 N. ¿Con qué fuerza empuja A a B? Respondé solo con el número en N.",
                "answer": "10 N: las dos cajas se mueven juntas, así que a = F/(m_A + m_B) = 30/6 = 5 m/s². La única fuerza horizontal sobre B es la de contacto: F_AB = m_B·a = 2·5 = 10 N. No se transmiten los 30 N enteros: los otros 20 N son la fuerza neta que acelera a la propia caja A.",
                "hints": [
                    "Primero tratá las dos cajas como un solo cuerpo para hallar la aceleración.",
                    "Después hacé el diagrama de cuerpo libre de B sola: en horizontal solo actúa la fuerza de contacto.",
                ],
                "payload": {"check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "N"}},
            },
            {
                "item_type": "worked_example",
                "title": "Tensión de la soga entre dos changuitos",
                "prompt": "Dos changuitos están unidos por una soga ideal sobre un piso sin rozamiento: el de adelante tiene 3 kg y el de atrás, 5 kg. Tirás del de adelante con una fuerza horizontal de 24 N. ¿Cuánto vale la tensión de la soga que los une? Respondé solo con el número en N.",
                "answer": "15 N: el conjunto acelera con a = 24/(3 + 5) = 3 m/s². Sobre el changuito de atrás la única fuerza horizontal es la tensión: T = 5·3 = 15 N. Verificación con el de adelante: 24 − T = 3·3 → T = 15 N.",
                "hints": [
                    "La aceleración es la misma para los dos: fuerza externa sobre masa total.",
                    "La soga intermedia solo tiene que acelerar al changuito de atrás.",
                ],
                "payload": {"check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": "N"}},
            },
            {
                "item_type": "worked_example",
                "title": "Aceleración de un bloque en la mesa unido a otro que cuelga",
                "prompt": "Un bloque de 3 kg apoyado en una mesa horizontal sin rozamiento está unido, por una soga ideal que pasa por una polea ideal en el borde, a un bloque de 2 kg que cuelga. Usá g = 10 m/s². ¿Con qué aceleración se mueven? Respondé solo con el número en m/s².",
                "answer": "4 m/s²: bloque que cuelga: m₂·g − T = m₂·a → 20 − T = 2·a. Bloque en la mesa: T = m₁·a = 3·a. Sumando las dos ecuaciones se cancela T: 20 = 5·a → a = 4 m/s². El peso del bloque colgante tiene que acelerar a los DOS bloques, por eso a < g.",
                "hints": [
                    "Escribí una ecuación por cuerpo, con la misma a y la misma T.",
                    "Sumá las ecuaciones: la única fuerza externa a favor del movimiento es el peso del bloque que cuelga, y mueve la masa total.",
                ],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "m/s²"}},
            },
            {
                "item_type": "recall",
                "title": "Tensión y peso de un cuerpo que baja acelerando",
                "prompt": "Un balde cuelga de una soga y baja ACELERANDO (por ejemplo, porque del otro lado arrastra un carrito por una mesa). ¿Cómo es la tensión de la soga comparada con el peso del balde?",
                "answer": "Menor. Para el balde: m·g − T = m·a, así que T = m·(g − a) < m·g. Si la tensión igualara al peso, la fuerza neta sería cero y el balde no aceleraría (bajaría a velocidad constante o quedaría quieto). T = m·g vale solo en equilibrio; si el balde acelerara hacia arriba sería T = m·(g + a) > m·g.",
                "hints": ["Planteá la 2ª ley solo para el balde, con sentido positivo hacia abajo."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Igual al peso: la soga sostiene al balde",
                            "Mayor que el peso: además de sostenerlo, arrastra al carrito",
                            "Menor que el peso: hace falta fuerza neta hacia abajo para que acelere",
                        ],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Aceleración en una máquina de Atwood",
                "prompt": "De los extremos de una soga ideal que pasa por una polea ideal cuelgan una pesa de 6 kg y otra de 4 kg. Usá g = 10 m/s². ¿Con qué aceleración se mueven al soltarlas? Respondé solo con el número en m/s².",
                "answer": "2 m/s²: tomando como positivo el sentido del movimiento (la de 6 kg baja, la de 4 kg sube): 60 − T = 6·a y T − 40 = 4·a. Sumando: 20 = 10·a → a = 2 m/s². En general a = (m₁ − m₂)·g/(m₁ + m₂): la diferencia de pesos mueve la masa total.",
                "hints": [
                    "Una ecuación por pesa: la más pesada baja y la más liviana sube con la misma aceleración.",
                    "Al sumar las ecuaciones la tensión se cancela.",
                ],
                "payload": {"check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "m/s²"}},
            },
            {
                "item_type": "worked_example",
                "title": "Tensión de la soga en una máquina de Atwood",
                "prompt": "En una máquina de Atwood (soga y polea ideales) cuelgan una pesa de 3 kg y otra de 1 kg. Usá g = 10 m/s². ¿Cuánto vale la tensión de la soga mientras se mueven? Respondé solo con el número en N.",
                "answer": "15 N: 30 − T = 3·a y T − 10 = 1·a. Sumando: 20 = 4·a → a = 5 m/s². Reemplazando en la segunda: T = 10 + 1·5 = 15 N. La tensión queda entre los dos pesos (10 N < 15 N < 30 N): le gana al peso de la pesa que sube y pierde con el de la que baja.",
                "hints": [
                    "Primero hallá la aceleración sumando las dos ecuaciones.",
                    "Después reemplazá a en la ecuación de cualquiera de las dos pesas para despejar T.",
                ],
                "payload": {"check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": "N"}},
            },
            {
                "item_type": "recall",
                "title": "Pasos para resolver dos cuerpos unidos por una soga",
                "prompt": "Ordená los pasos para hallar la aceleración y la tensión en un sistema de dos cuerpos unidos por una soga ideal.",
                "answer": "Primero un diagrama de cuerpo libre por cuerpo (con un sentido positivo que siga a la soga); después ΣF = m·a para cada uno con la misma a y la misma T; al sumar las ecuaciones se cancela T y sale a; por último se reemplaza a en cualquiera de las ecuaciones para obtener T.",
                "hints": ["La tensión es una fuerza interna del sistema: aparece con signos opuestos en las dos ecuaciones."],
                "payload": {
                    "check": {
                        "type": "order",
                        "lines": [
                            "Dibujar un diagrama de cuerpo libre para cada cuerpo y elegir el sentido positivo siguiendo la soga",
                            "Escribir ΣF = m·a para cada cuerpo, con la misma a y la misma T",
                            "Sumar las ecuaciones para que se cancele T y despejar a",
                            "Reemplazar a en una de las ecuaciones para obtener T",
                        ],
                    },
                },
            },
        ],
    },
    # ==================== MOVIMIENTO CIRCULAR UNIFORME ====================
    {
        "slug": "f-mcu",
        "title": "Movimiento circular uniforme: período, frecuencia y velocidad angular",
        "summary": "Período y frecuencia, rpm a Hz y rad/s, velocidad angular y tangencial (v = ω·r), aceleración centrípeta y transmisión por correas o engranajes.",
        "prerequisites": ["f-leyes-newton"],
        "insert_after": "f-cuerpos-vinculados",
        "metadata": {"section": "Dinámica y energía", "lab_tab": "forces", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Período de un centrifugado a partir de las rpm",
                "prompt": "El tambor de un lavarropas centrifuga a 1200 rpm (vueltas por minuto). ¿Cuánto tarda en dar una vuelta, es decir, cuál es su período? Respondé solo con el número en s.",
                "answer": "0.05 s: primero la frecuencia en Hz: f = 1200 vueltas / 60 s = 20 Hz. El período es el inverso: T = 1/f = 1/20 = 0.05 s.",
                "hints": [
                    "Pasá las rpm a vueltas por segundo (Hz) dividiendo por 60.",
                    "El período es el inverso de la frecuencia: T = 1/f.",
                ],
                "payload": {"check": {"type": "numeric", "value": 0.05, "tolerance": 0, "unit": "s"}},
            },
            {
                "item_type": "worked_example",
                "title": "Velocidad angular de un ventilador en función de π",
                "prompt": "Un ventilador de techo gira a 90 rpm. ¿Cuál es su velocidad angular?",
                "answer": "3π rad/s: f = 90/60 = 1.5 Hz y ω = 2π·f = 2π·1.5 = 3π rad/s (≈ 9.42 rad/s). 180π sale de no pasar las rpm a Hz, y 1.5π de olvidar el 2 de 2π·f.",
                "hints": [
                    "Primero pasá las rpm a Hz.",
                    "Cada vuelta son 2π radianes: ω = 2π·f.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["180π rad/s", "1.5π rad/s", "3π rad/s", "90π rad/s"],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Velocidad tangencial del borde de una rueda",
                "prompt": "La rueda de una bicicleta fija gira con velocidad angular ω = 12 rad/s y tiene 0.35 m de radio. ¿Qué velocidad tangencial tiene un punto de la cubierta? Respondé solo con el número en m/s.",
                "answer": "4.2 m/s: v = ω·r = 12·0.35 = 4.2 m/s (unos 15 km/h).",
                "hints": ["La velocidad tangencial es la velocidad angular por el radio."],
                "payload": {"check": {"type": "numeric", "value": 4.2, "tolerance": 0, "unit": "m/s"}},
            },
            {
                "item_type": "worked_example",
                "title": "Aceleración centrípeta a partir de la velocidad angular",
                "prompt": "Revoleás una piedra atada a un hilo en un círculo de 0.8 m de radio, con velocidad angular constante ω = 5 rad/s. ¿Cuánto vale su aceleración centrípeta? Respondé solo con el número en m/s².",
                "answer": "20 m/s²: a_c = ω²·r = 5²·0.8 = 25·0.8 = 20 m/s², apuntando hacia el centro. Da lo mismo con v = ω·r = 4 m/s: a_c = v²/r = 16/0.8 = 20 m/s².",
                "hints": [
                    "Con ω y r: a_c = ω²·r.",
                    "Solo ω va al cuadrado, no el radio.",
                ],
                "payload": {"check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "m/s²"}},
            },
            {
                "item_type": "worked_example",
                "title": "Velocidad de la punta del segundero",
                "prompt": "El segundero de un reloj de pared mide 15 cm desde el eje hasta la punta. ¿Con qué velocidad tangencial se mueve la punta? Usá π ≈ 3.14 y redondeá a 2 decimales. Respondé solo con el número en cm/s.",
                "answer": "1.57 cm/s: el segundero da una vuelta en T = 60 s, y en ese tiempo la punta recorre una circunferencia de 2π·r. Entonces v = 2π·r/T = 2·3.14·15/60 = 94.2/60 = 1.57 cm/s.",
                "hints": [
                    "¿Cuánto tarda el segundero en dar una vuelta completa? Ese es el período T.",
                    "v = 2π·r/T (una circunferencia por período).",
                ],
                "payload": {"check": {"type": "numeric", "value": 1.57, "tolerance": 0.005, "unit": "cm/s"}},
            },
            {
                "item_type": "recall",
                "title": "Dos chicos a distinto radio en la misma calesita",
                "prompt": "En una calesita que gira, Juan va sentado en el borde, a 3 m del eje, y Sofi a 1.5 m del eje. ¿Cómo se comparan sus movimientos?",
                "answer": "Misma velocidad angular y mismo período, y Juan con el doble de velocidad tangencial. La calesita es un cuerpo rígido: todos sus puntos barren el mismo ángulo en el mismo tiempo, así que comparten ω y T. Como v = ω·r, a doble radio corresponde doble velocidad tangencial (y también doble aceleración centrípeta, ω²·r).",
                "hints": ["¿Quién tarda más en dar una vuelta completa? Después compará el largo de la circunferencia que recorre cada uno."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Tienen la misma velocidad tangencial; Sofi tiene el doble de velocidad angular",
                            "Tienen la misma velocidad angular y el mismo período; Juan tiene el doble de velocidad tangencial",
                            "Juan tiene el doble de velocidad angular y el doble de velocidad tangencial",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Plato y piñón unidos por la cadena",
                "prompt": "En una bicicleta, el plato (radio 10 cm) está unido por la cadena al piñón (radio 4 cm). Si pedaleás haciendo girar el plato a 6 rad/s, ¿con qué velocidad angular gira el piñón? Respondé solo con el número en rad/s.",
                "answer": "15 rad/s: la cadena no desliza, así que el borde del plato y el del piñón tienen la misma velocidad tangencial: ω₁·r₁ = ω₂·r₂ → 6·10 = ω₂·4 → ω₂ = 60/4 = 15 rad/s. La rueda dentada más chica gira más rápido.",
                "hints": [
                    "La cadena avanza a una sola velocidad: los bordes de las dos ruedas dentadas comparten la misma v.",
                    "Igualá ω₁·r₁ = ω₂·r₂ (podés dejar los dos radios en cm).",
                ],
                "payload": {"check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": "rad/s"}},
            },
            {
                "item_type": "recall",
                "title": "Qué se mantiene constante en un movimiento circular uniforme",
                "prompt": "Una cabina de la vuelta al mundo gira con movimiento circular uniforme. ¿Cuál de estas afirmaciones es correcta?",
                "answer": "La rapidez y la velocidad angular son constantes, pero la velocidad es un vector tangente a la trayectoria y su dirección cambia en cada instante. Cambiar la dirección de la velocidad es acelerar: la aceleración centrípeta tiene módulo constante v²/r, pero su dirección también va cambiando, porque apunta siempre hacia el centro.",
                "hints": ["Velocidad y aceleración son vectores: fijate qué pasa con su dirección, no solo con su módulo."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "El vector velocidad es constante, por eso la aceleración es cero",
                            "La rapidez y la velocidad angular son constantes, pero el vector velocidad cambia de dirección: hay aceleración centrípeta",
                            "La rapidez es constante y el vector aceleración también, porque siempre mide v²/r",
                        ],
                        "correct": 1,
                    },
                },
            },
        ],
    },
    # ==================== ESTÁTICA ====================
    {
        "slug": "f-estatica",
        "title": "Estática: equilibrio con tensiones y momentos",
        "summary": "Equilibrio de la partícula (ΣFx = 0 y ΣFy = 0) con sogas en ángulo, y del cuerpo extenso (ΣF = 0 y ΣM = 0): vigas con dos apoyos y palancas.",
        "prerequisites": ["f-torque-rotacion", "f-dcl-rozamiento-plano"],
        "insert_after": "f-torque-rotacion",
        "metadata": {"section": "Dinámica y energía", "lab_tab": "forces", "est_minutes": 25},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Tercera fuerza para equilibrar una argolla",
                "prompt": "En una cinchada de tres sogas atadas a una misma argolla, un equipo tira con 300 N hacia el este y otro con 400 N hacia el norte. ¿Qué módulo debe tener la fuerza del tercer equipo para que la argolla quede en equilibrio? Respondé solo con el número en N.",
                "answer": "500 N: para el equilibrio ΣFx = 0 y ΣFy = 0, así que la tercera fuerza debe tener una componente de 300 N hacia el oeste y otra de 400 N hacia el sur. Su módulo es √(300² + 400²) = 500 N. No son 700 N: dos fuerzas perpendiculares no se suman como números.",
                "hints": [
                    "La tercera fuerza tiene que cancelar por separado la componente este-oeste y la componente norte-sur.",
                    "Con las dos componentes, el módulo sale por Pitágoras.",
                ],
                "payload": {"check": {"type": "numeric", "value": 500, "tolerance": 0, "unit": "N"}},
            },
            {
                "item_type": "worked_example",
                "title": "Tensión en dos sogas simétricas",
                "prompt": "Un cartel de 12 kg cuelga quieto de dos sogas iguales; cada una forma 37° con la horizontal (sen 37° = 0.6 y cos 37° = 0.8). Usá g = 10 m/s². ¿Cuánto vale la tensión de cada soga? Respondé solo con el número en N.",
                "answer": "100 N: por simetría las dos tensiones son iguales y sus componentes horizontales se cancelan. En vertical: 2·T·sen 37° = m·g → 2·T·0.6 = 120 → T = 120/1.2 = 100 N. Cada soga tira con más que la mitad del peso (60 N) porque solo su componente vertical sostiene al cartel.",
                "hints": [
                    "Solo la componente vertical de cada tensión (T·sen 37°) sostiene el peso.",
                    "ΣFy = 0: 2·T·sen 37° − m·g = 0.",
                ],
                "payload": {"check": {"type": "numeric", "value": 100, "tolerance": 0, "unit": "N"}},
            },
            {
                "item_type": "worked_example",
                "title": "Tensión de una soga inclinada con otra horizontal",
                "prompt": "Una maceta de 6 kg cuelga de un nudo sostenido por dos sogas: una va al techo formando 53° con la horizontal (sen 53° = 0.8 y cos 53° = 0.6) y la otra va horizontal hasta la pared. Usá g = 10 m/s². ¿Cuánto vale la tensión de la soga inclinada? Respondé solo con el número en N.",
                "answer": "75 N: la soga horizontal no tiene componente vertical, así que la inclinada sostiene sola todo el peso: T·sen 53° = m·g → T·0.8 = 60 → T = 75 N. Después, con ΣFx = 0, la soga horizontal vale T·cos 53° = 75·0.6 = 45 N.",
                "hints": [
                    "Planteá ΣFy = 0 en el nudo: ¿qué soga tiene componente vertical?",
                    "T·sen 53° = m·g.",
                ],
                "payload": {"check": {"type": "numeric", "value": 75, "tolerance": 0, "unit": "N"}},
            },
            {
                "item_type": "recall",
                "title": "Por qué una soga casi horizontal soporta tanta tensión",
                "prompt": "Colgás una campera mojada en el medio de la soga de la ropa. Si tensás más la soga para que quede casi horizontal, ¿qué pasa con la tensión que soporta?",
                "answer": "Aumenta mucho. El equilibrio vertical pide 2·T·sen θ = P (con θ medido desde la horizontal), o sea T = P/(2·sen θ). Cuando θ se acerca a 0, sen θ se acerca a 0 y T crece sin límite: por eso ninguna soga cargada queda perfectamente horizontal. T = P/2 vale solo si las dos sogas cuelgan verticales.",
                "hints": ["Solo la componente vertical T·sen θ sostiene el peso. ¿Qué le pasa a sen θ cuando θ es muy chico?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "No cambia: cada mitad de la soga soporta la mitad del peso, cualquiera sea el ángulo",
                            "Disminuye: al estar más horizontal, la soga deja de cargar el peso",
                            "Aumenta mucho: con un ángulo chico cada mitad aporta poca componente vertical y hace falta más tensión para sostener el mismo peso",
                        ],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Dos fuerzas iguales y opuestas sobre una barra",
                "prompt": "Una barra orientada de este a oeste está apoyada sobre una mesa de hielo (sin rozamiento). Empujás su extremo este con 10 N hacia el norte y su extremo oeste con 10 N hacia el sur. ¿Queda en equilibrio?",
                "answer": "No. La suma de fuerzas es cero, así que el centro de la barra no se acelera, pero las dos fuerzas la hacen girar en el mismo sentido (forman una cupla): ΣM ≠ 0. Un cuerpo extenso está en equilibrio solo si se cumplen las dos condiciones: ΣF = 0 y ΣM = 0.",
                "hints": ["Calculá el momento de cada fuerza respecto del centro de la barra: ¿hacen girar en el mismo sentido o en sentidos opuestos?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Sí: las fuerzas son iguales y opuestas, así que ΣF = 0 y eso alcanza",
                            "No: ΣF = 0, pero los momentos de las dos fuerzas se suman y la barra gira",
                            "No: la fuerza neta no es cero y la barra se traslada hacia el norte",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Elegir el punto para tomar momentos",
                "prompt": "Una viga en equilibrio está apoyada en A y en B, y no conocés ninguna de las dos reacciones. ¿Por qué conviene tomar momentos respecto del punto A para calcular la reacción en B?",
                "answer": "Porque una fuerza cuya recta de acción pasa por el punto elegido tiene brazo cero y momento cero: la reacción en A desaparece y queda una ecuación con una sola incógnita (R_B). En equilibrio, ΣM = 0 se cumple respecto de CUALQUIER punto; elegir A es solo lo más cómodo.",
                "hints": ["El momento es fuerza por distancia perpendicular al punto: ¿qué distancia tiene la reacción en A respecto de A?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Porque la reacción en A tiene brazo cero respecto de A y desaparece de la ecuación, que queda con una sola incógnita",
                            "Porque ΣM = 0 solo se cumple respecto de los puntos de apoyo",
                            "Porque respecto de A el peso de la carga no hace momento",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Reacción de un apoyo en un tablón con una persona",
                "prompt": "Un tablón de 4 m, de peso despreciable, está apoyado en sus extremos A y B. Una persona de 80 kg se para a 1 m del extremo A. Usá g = 10 m/s². ¿Cuánto vale la reacción del apoyo B? Respondé solo con el número en N.",
                "answer": "200 N: tomando momentos respecto de A (así la reacción en A no aparece): R_B·4 − 800·1 = 0 → R_B = 200 N. Con ΣFy = 0, R_A = 800 − 200 = 600 N: el apoyo más cercano a la persona carga más.",
                "hints": [
                    "Tomá momentos respecto del apoyo A: la reacción en A tiene brazo cero.",
                    "Respecto de A, el peso de la persona tiene brazo 1 m y R_B tiene brazo 4 m.",
                ],
                "payload": {"check": {"type": "numeric", "value": 200, "tolerance": 0, "unit": "N"}},
            },
            {
                "item_type": "worked_example",
                "title": "Fuerza para levantar una piedra con una barreta",
                "prompt": "Querés levantar una piedra de 120 kg con una barreta de 1.5 m de largo y peso despreciable. Metés una punta debajo de la piedra y apoyás la barreta sobre un tronco ubicado a 0.3 m de esa punta. Considerá la barreta horizontal y usá g = 10 m/s². ¿Qué fuerza mínima, perpendicular a la barreta, tenés que hacer hacia abajo en el otro extremo? Respondé solo con el número en N.",
                "answer": "300 N: se toman momentos respecto del punto de apoyo (el tronco). La piedra pesa 1200 N y tiene brazo 0.3 m; tu fuerza tiene brazo 1.5 − 0.3 = 1.2 m. Entonces F·1.2 = 1200·0.3 = 360 → F = 300 N: con un brazo 4 veces más largo hacés la cuarta parte de la fuerza.",
                "hints": [
                    "Tomá momentos respecto del tronco, que es el punto de apoyo.",
                    "Tu brazo no es el largo total de la barreta: es la distancia desde el tronco hasta tu mano.",
                ],
                "payload": {"check": {"type": "numeric", "value": 300, "tolerance": 0, "unit": "N"}},
            },
        ],
    },
]


DYNAMICS_LESSONS: dict[str, dict] = {
    "f-dcl-rozamiento-plano": {
        "hook": {
            "question": "Apoyás el celular sobre un cuaderno y lo vas inclinando de a poco. ¿Por qué al principio no se mueve y, al llegar a cierto ángulo, sale deslizando de golpe?",
            "intuition": "Porque el rozamiento estático no vale una cantidad fija: **se ajusta** para empatar a la fuerza que quiere mover al celular, pero solo hasta un máximo (`μₑ·N`). Al inclinar, la parte del peso que tira cuesta abajo (`m·g·sen θ`) crece y la normal (`m·g·cos θ`) se achica; cuando lo pedido supera el máximo, desliza.",
        },
        "concept": {
            "points": [
                "**Diagrama de cuerpo libre (DCL)**: aislá UN cuerpo y dibujá solo las fuerzas que **otros cuerpos le hacen a él**: peso (la Tierra), normal y rozamiento (la superficie), tensión (una soga), empuje (una mano). No van las fuerzas que él les hace a otros, ni una 'fuerza del movimiento', ni `m·a` (que es el resultado de sumar las fuerzas, no una fuerza más).",
                "**La normal no tiene fórmula fija**: sale de `ΣF` en la dirección perpendicular a la superficie. En piso horizontal sin otras fuerzas verticales, `N = m·g`. En un plano inclinado, `N = m·g·cos θ`. Si tirás con una fuerza `F` inclinada hacia arriba, `N = m·g − F·sen θ`. En un ascensor que acelera hacia arriba, `N = m·(g + a)`.",
                "**Rozamiento estático**: mientras no hay deslizamiento vale lo necesario para que no lo haya, con un tope: `0 ≤ fₑ ≤ μₑ·N`. **Rozamiento dinámico**: cuando desliza vale `f_d = μ_d·N`, opuesto al deslizamiento. Para un mismo par de superficies, lo habitual es `μ_d < μₑ`.",
                "**Plano inclinado**: usá un eje paralelo al plano y otro perpendicular. El peso se descompone en `m·g·sen θ` (paralela, cuesta abajo) y `m·g·cos θ` (perpendicular, contra el plano). Sin rozamiento, `a = g·sen θ`; bajando con rozamiento dinámico, `a = g·(sen θ − μ_d·cos θ)`.",
                "**Ángulo crítico**: un cuerpo en reposo sobre el plano empieza a deslizar cuando `m·g·sen θ` iguala al rozamiento estático máximo `μₑ·m·g·cos θ`, es decir, cuando `tan θ = μₑ` (no depende de la masa).",
            ],
            "real_world": [
                {
                    "title": "Rampas de garage los días de lluvia",
                    "detail": "Con el piso mojado baja `μₑ` y entonces baja el ángulo crítico (`tan θ = μₑ`): con `μₑ = 0.3` ya se desliza a partir de unos 17°. Por eso las rampas llevan ranuras o cintas antideslizantes.",
                },
                {
                    "title": "Tirar de la valija en vez de empujarla",
                    "detail": "Si tirás con la manija inclinada hacia arriba, parte de tu fuerza sostiene el peso: baja la normal y con ella el rozamiento (`μ_d·N`). Si empujás inclinado hacia abajo, pasa lo contrario: apretás la carga contra el piso y roza más.",
                },
                {
                    "title": "Frenos ABS",
                    "detail": "Una rueda que gira sin patinar se agarra al asfalto con rozamiento estático, cuyo máximo es mayor que el rozamiento dinámico de una rueda bloqueada. El ABS evita el bloqueo para frenar con el rozamiento más grande disponible.",
                },
            ],
            "key_rule": "`0 ≤ fₑ ≤ μₑ·N` · `f_d = μ_d·N` · En el plano: `N = m·g·cos θ` y cuesta abajo tira `m·g·sen θ` · Empieza a deslizar cuando `tan θ = μₑ`.",
            "pitfall": "Escribir `N = m·g` y `fₑ = μₑ·N` por costumbre: la normal sale de la ecuación perpendicular a la superficie (no siempre es el peso), y `μₑ·N` es solo el **máximo** del rozamiento estático, no su valor en cualquier situación.",
        },
        "example": {
            "title": "Buscá el empuje justo que despega al bloque",
            "steps": [
                "Abrí el Laboratorio de Física → Fuerzas, elegí superficie **Goma** (`μ = 0.70`) y masa `5 kg`. El cuadro **FRICCIÓN MÁX** marca `0.70 · 5 · 9.81 ≈ 34.3 N` (el simulador usa `g = 9.81 m/s²` y un solo `μ` para el caso estático y el dinámico).",
                "Subí el empuje de a poco hasta `34 N`: el bloque sigue quieto, la flecha roja `fr` crece igual que tu empuje y la fuerza neta marca `0 N`. Eso es rozamiento estático ajustándose.",
                "Pasá a `35 N`: superaste el máximo, el rozamiento queda clavado en `34.3 N` y el bloque arranca con `a = (35 − 34.34) / 5 ≈ 0.13 m/s²`.",
                "Subí la masa a `10 kg`: la normal se duplica y la fricción máxima también (`≈ 68.7 N`), así que ni el empuje máximo del simulador (`60 N`) lo mueve.",
            ],
            "lab_link": "physics:forces",
            "lab_cta": "Abrir Simulador de Fuerzas",
        },
        "check": {
            "question": "Empujás horizontalmente con 30 N una caja de 10 kg apoyada en un piso horizontal (`μₑ = 0.4`, `g = 10 m/s²`) y la caja no se mueve. ¿Cuánto vale el rozamiento?",
            "options": [
                {"text": "40 N", "ok": False, "feedback": "40 N es el máximo posible (μₑ·N = 0.4 · 100). El rozamiento estático solo llega a ese valor cuando la caja está a punto de deslizar; si valiera 40 N contra un empuje de 30 N, la caja aceleraría hacia vos."},
                {"text": "30 N", "ok": True, "feedback": "Exacto: como no se mueve, ΣFx = 0 y el rozamiento estático empata al empuje. Los 40 N (μₑ·N) son solo el tope."},
                {"text": "100 N", "ok": False, "feedback": "100 N es el peso (y la normal): m·g = 10 · 10. El rozamiento es horizontal y se obtiene de ΣFx = 0, no es igual a la normal."},
            ],
        },
        "checks": [
            {
                "question": "Un bloque de 2 kg está en reposo sobre un plano inclinado 30° (`sen 30° = 0.5`, `cos 30° ≈ 0.87`, `g = 10 m/s²`). ¿Cuánto vale la fuerza normal?",
                "options": [
                    {"text": "17.4 N", "ok": True, "feedback": "Exacto: en el eje perpendicular al plano, N = m·g·cos 30° = 20 · 0.87 = 17.4 N."},
                    {"text": "20 N", "ok": False, "feedback": "Usaste N = m·g = 2 · 10, que vale solo en un piso horizontal. En el plano la normal equilibra únicamente a la componente perpendicular del peso."},
                    {"text": "10 N", "ok": False, "feedback": "Calculaste m·g·sen 30° = 20 · 0.5, que es la componente paralela al plano (la que tira cuesta abajo). La normal equilibra a la otra: m·g·cos 30°."},
                ],
            },
            {
                "question": "Arrastrás una caja por el piso tirando de una soga inclinada hacia arriba. Comparado con tirar en horizontal con la misma fuerza, el rozamiento dinámico con el piso…",
                "options": [
                    {"text": "Es igual, porque solo depende del peso de la caja y de `μ_d`", "ok": False, "feedback": "Eso supone N = m·g en cualquier caso. El rozamiento es μ_d·N, y acá la normal es N = m·g − F·sen θ, menor que el peso."},
                    {"text": "Es mayor, porque la soga agrega una fuerza vertical", "ok": False, "feedback": "La componente vertical de la soga apunta hacia arriba, así que se resta del peso en vez de sumarse. La normal aumentaría si empujaras inclinado hacia abajo."},
                    {"text": "Es menor, porque la componente vertical de la soga reduce la normal", "ok": True, "feedback": "Exacto: N = m·g − F·sen θ, y como f_d = μ_d·N, al bajar la normal baja el rozamiento."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué la normal no siempre vale m·g y cuál es la diferencia entre el rozamiento estático y el dinámico, usando el ejemplo de un objeto sobre un plano que se va inclinando.",
    },
    "f-cuerpos-vinculados": {
        "hook": {
            "question": "Colgás un balde de 2 kg de una soga que pasa por una polea y, del otro lado, arrastra un carrito por la mesa. Mientras el balde baja acelerando, ¿la soga tira con 20 N, el peso del balde?",
            "intuition": "No. Si la soga tirara hacia arriba con los mismos 20 N con que la Tierra tira hacia abajo, la fuerza neta sobre el balde sería cero y no podría acelerar. Para que baje cada vez más rápido, el peso tiene que **ganarle** a la tensión: `T < m·g`.",
        },
        "concept": {
            "points": [
                "**Soga ideal**: es *inextensible* (lo que avanza un cuerpo lo avanza el otro, así que tienen aceleración de **igual módulo**) y *sin masa* (tira con la **misma tensión** `T` en sus dos extremos). **Polea ideal** (sin masa y sin rozamiento en el eje): solo cambia la dirección de la soga, no el valor de `T`.",
                "**Método**: un diagrama de cuerpo libre y una ecuación `ΣF = m·a` **por cuerpo**, tomando como positivo el sentido del movimiento siguiendo la soga. Al sumar las ecuaciones, las fuerzas internas (tensión, contacto) se cancelan y queda `a = (fuerzas externas a favor − en contra) / masa total`.",
                "**Bloques empujados o tirados sobre una mesa sin rozamiento**: `a = F / (m₁ + m₂)`. La fuerza de contacto, o la tensión de la soga intermedia, solo acelera a lo que viene atrás: vale `m_atrás·a`, siempre menos que `F`.",
                "**Bloque en la mesa (`m₁`, sin rozamiento) unido a otro que cuelga (`m₂`)**: `m₂·g − T = m₂·a` y `T = m₁·a`. Sumando, `a = m₂·g / (m₁ + m₂)`, menor que `g`.",
                "**Máquina de Atwood** (dos masas colgando de una polea, `m₁ > m₂`): `a = (m₁ − m₂)·g / (m₁ + m₂)` y `T = 2·m₁·m₂·g / (m₁ + m₂)`. La tensión queda entre los dos pesos.",
            ],
            "real_world": [
                {
                    "title": "Ascensor con contrapeso",
                    "detail": "Es una máquina de Atwood con motor: la cabina y el contrapeso cuelgan del mismo cable. Como los pesos casi se compensan, el motor solo tiene que aportar la diferencia en vez de levantar toda la cabina.",
                },
                {
                    "title": "Locomotora y vagones",
                    "detail": "Todos aceleran igual, pero el enganche del primer vagón tiene que arrastrar a todos los que vienen atrás y el del último solo a uno: la tensión va bajando hacia la cola del tren.",
                },
                {
                    "title": "Subir un balde con la roldana de una obra",
                    "detail": "Mientras el balde sube a velocidad constante, la soga tira con su peso. En el arranque (acelera hacia arriba) hay que tirar con más: `T = m·(g + a)`.",
                },
            ],
            "key_rule": "Un DCL y una ecuación por cuerpo · misma `a` y misma `T` · sumá las ecuaciones: `a = fuerza externa neta / masa total` · después reemplazá para hallar `T`.",
            "pitfall": "Poner `T = m·g` para el cuerpo que cuelga: eso vale solo si está en equilibrio (quieto o a velocidad constante). Si acelera hacia abajo, `T = m·(g − a)`; si acelera hacia arriba, `T = m·(g + a)`.",
        },
        "example": {
            "title": "Resolvé una máquina de Atwood paso a paso",
            "steps": [
                "De una polea ideal cuelgan `5 kg` y `3 kg` (con `g = 10 m/s²`: pesos de `50 N` y `30 N`). Sobre cada pesa actúan solo su peso y la tensión `T`. Sentido positivo: la de 5 kg baja y la de 3 kg sube.",
                "Una ecuación por cuerpo: `50 − T = 5·a` (la que baja) y `T − 30 = 3·a` (la que sube).",
                "Sumá las dos: `T` se cancela y queda `20 = 8·a`, o sea `a = 2.5 m/s²`.",
                "Reemplazá en la segunda: `T = 30 + 3 · 2.5 = 37.5 N`. Control: está entre `30 N` y `50 N`, como tiene que ser.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Un bloque de 4 kg sobre una mesa sin rozamiento está unido por una soga y una polea ideales a otro de 1 kg que cuelga (`g = 10 m/s²`). ¿Con qué aceleración se mueven?",
            "options": [
                {"text": "10 m/s²", "ok": False, "feedback": "Eso sería caída libre. El bloque colgante no cae libremente: la soga lo frena porque su peso también tiene que acelerar al bloque de la mesa."},
                {"text": "2.5 m/s²", "ok": False, "feedback": "Dividiste el peso colgante (10 N) solo por la masa de la mesa (4 kg). Ese peso acelera a los dos bloques: hay que dividir por la masa total, 5 kg."},
                {"text": "2 m/s²", "ok": True, "feedback": "Exacto: 10 − T = 1·a y T = 4·a; sumando, 10 = 5·a → a = 2 m/s²."},
            ],
        },
        "checks": [
            {
                "question": "Empujás con 12 N una caja de 1 kg que tiene pegada adelante otra de 3 kg, sobre un piso sin rozamiento. ¿Qué fuerza le hace la primera caja a la segunda?",
                "options": [
                    {"text": "9 N", "ok": True, "feedback": "Exacto: a = 12 / (1 + 3) = 3 m/s², y la caja de adelante solo recibe la fuerza de contacto: 3 kg · 3 m/s² = 9 N."},
                    {"text": "12 N", "ok": False, "feedback": "El empuje no se transmite entero: parte se usa en acelerar a la caja de 1 kg. Si pasaran los 12 N, la fuerza neta sobre la primera caja sería cero."},
                    {"text": "3 N", "ok": False, "feedback": "3 N = 1 kg · 3 m/s² es la fuerza NETA sobre la caja que empujás. La de contacto es lo que hace falta para acelerar a la de 3 kg: 3 · 3 = 9 N."},
                ],
            },
            {
                "question": "En una máquina de Atwood con masas distintas que se está moviendo, la tensión de la soga…",
                "options": [
                    {"text": "Es igual al peso del cuerpo más pesado", "ok": False, "feedback": "Si la tensión igualara al peso del cuerpo pesado, la fuerza neta sobre él sería cero y no aceleraría hacia abajo."},
                    {"text": "Es mayor que el peso del cuerpo liviano y menor que el del pesado", "ok": True, "feedback": "Exacto: el liviano sube acelerando (T > m₂·g) y el pesado baja acelerando (T < m₁·g)."},
                    {"text": "Es igual a la diferencia entre los dos pesos", "ok": False, "feedback": "La diferencia de pesos es la fuerza neta que acelera al sistema completo, no la tensión. La tensión sale de reemplazar a en la ecuación de uno de los cuerpos."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué en un sistema con soga ideal se plantea una ecuación por cuerpo con la misma aceleración y la misma tensión, y por qué la tensión no es igual al peso del cuerpo que cuelga cuando hay aceleración.",
    },
    "f-mcu": {
        "hook": {
            "question": "En una calesita que gira, ¿va más rápido el caballito del borde o el que está cerca del centro?",
            "intuition": "Depende de qué 'rápido' mires. Los dos dan la vuelta en el mismo tiempo: tienen la **misma velocidad angular**. Pero el del borde recorre una circunferencia más larga en ese mismo tiempo: tiene **mayor velocidad tangencial**. En un movimiento circular conviven esas dos velocidades.",
        },
        "concept": {
            "points": [
                "**Período (`T`)**: tiempo que tarda una vuelta, en segundos. **Frecuencia (`f`)**: vueltas por segundo, en hertz (Hz). Son inversos: `T = 1/f`. Para pasar de rpm (vueltas por minuto) a Hz, dividí por 60.",
                "**Velocidad angular (`ω`)**: ángulo barrido por unidad de tiempo, en rad/s. Como una vuelta son `2π` radianes, `ω = 2π/T = 2π·f`.",
                "**Velocidad tangencial (`v`)**: distancia recorrida por unidad de tiempo, tangente a la circunferencia. En una vuelta se recorre `2π·r`, así que `v = 2π·r/T = ω·r`.",
                "**Aceleración centrípeta**: aunque la rapidez sea constante, el vector velocidad cambia de dirección todo el tiempo, y eso es acelerar. Apunta hacia el centro y vale `a_c = v²/r = ω²·r`.",
                "**Quién comparte qué**: todos los puntos de un mismo cuerpo rígido (un disco, una calesita) tienen la **misma `ω`** y su `v` crece con el radio. Dos ruedas unidas por una correa o cadena que no desliza, o dos engranajes en contacto, tienen la **misma `v` en el borde**: `ω₁·r₁ = ω₂·r₂`, la rueda chica gira más rápido.",
            ],
            "real_world": [
                {
                    "title": "Los cambios de la bici",
                    "detail": "La cadena obliga al plato y al piñón a tener la misma velocidad en el borde. Con plato grande y piñón chico, cada pedaleada hace girar varias veces la rueda trasera: avanzás más por vuelta, pero cuesta más fuerza.",
                },
                {
                    "title": "Centrifugado del lavarropas",
                    "detail": "A 1200 rpm (20 Hz) el tambor gira con `ω = 40π ≈ 126 rad/s`. Con un radio de 0.25 m, la ropa tiene una aceleración centrípeta `ω²·r` de casi `4000 m/s²`, unas 400 veces `g`.",
                },
                {
                    "title": "La rotación de la Tierra",
                    "detail": "Todos damos una vuelta cada 24 h (misma `ω`), pero en el Ecuador el radio de giro es el mayor y la velocidad tangencial ronda los 1670 km/h; a la latitud de Buenos Aires el círculo es más chico y es de unos 1370 km/h.",
                },
            ],
            "key_rule": "`T = 1/f` · `ω = 2π/T = 2π·f` · `v = ω·r` · `a_c = v²/r = ω²·r` · mismo cuerpo rígido: misma `ω` · misma correa o cadena: misma `v`.",
            "pitfall": "Meter la frecuencia en rpm dentro de `ω = 2π·f`: primero pasala a Hz dividiendo por 60. Y no confundir `ω` (rad/s, igual para todo el disco) con `v` (m/s, mayor cuanto más lejos del eje).",
        },
        "example": {
            "title": "De las rpm de una calesita a su aceleración",
            "steps": [
                "Una calesita gira a `6 rpm` y un caballito está a `4 m` del eje. Frecuencia: `f = 6/60 = 0.1 Hz`. Período: `T = 1/f = 10 s` por vuelta.",
                "Velocidad angular: `ω = 2π·f = 0.2π rad/s ≈ 0.63 rad/s`.",
                "Velocidad tangencial del caballito: `v = ω·r = 0.2π · 4 = 0.8π ≈ 2.51 m/s` (unos 9 km/h).",
                "Aceleración centrípeta: `a_c = ω²·r = (0.2π)² · 4 ≈ 1.58 m/s²`, hacia el eje. Un caballito a `2 m` del eje tendría la misma `ω`, pero la mitad de `v` y la mitad de `a_c`.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Una rueda da 5 vueltas por segundo. ¿Cuál es su período?",
            "options": [
                {"text": "5 s", "ok": False, "feedback": "5 es la frecuencia (vueltas por segundo), no el tiempo de una vuelta. El período es su inverso: T = 1/f."},
                {"text": "0.2 s", "ok": True, "feedback": "Exacto: T = 1/f = 1/5 = 0.2 s por vuelta."},
                {"text": "12 s", "ok": False, "feedback": "Hiciste 60/5, como si fueran 5 vueltas por MINUTO. Acá la frecuencia ya está en vueltas por segundo: T = 1/5 s."},
            ],
        },
        "checks": [
            {
                "question": "Dos poleas están unidas por una correa que no desliza: la chica tiene 5 cm de radio y la grande, 20 cm. Si la chica gira a 8 vueltas por segundo, la grande gira a…",
                "options": [
                    {"text": "8 vueltas por segundo", "ok": False, "feedback": "Compartir la frecuencia (y ω) vale para puntos de un mismo cuerpo rígido. Dos poleas unidas por correa comparten la velocidad del borde, no la frecuencia."},
                    {"text": "32 vueltas por segundo", "ok": False, "feedback": "Invertiste la proporción (8 · 20/5). Como v = ω·r es igual en los dos bordes, la polea de mayor radio gira MÁS lento."},
                    {"text": "2 vueltas por segundo", "ok": True, "feedback": "Exacto: misma v en el borde → f₁·r₁ = f₂·r₂ → f₂ = 8 · 5/20 = 2 vueltas por segundo."},
                ],
            },
            {
                "question": "Un objeto gira con velocidad angular `ω` constante. Si se lo pasa a un círculo del DOBLE de radio manteniendo la misma `ω`, su aceleración centrípeta…",
                "options": [
                    {"text": "Se duplica", "ok": True, "feedback": "Exacto: a_c = ω²·r; con ω fija es proporcional al radio."},
                    {"text": "Se reduce a la mitad", "ok": False, "feedback": "Usaste a_c = v²/r dejando v fija. Pero con la misma ω, v = ω·r también se duplica: (2v)²/(2r) = 2·v²/r."},
                    {"text": "Se cuadruplica", "ok": False, "feedback": "Elevaste al cuadrado el radio. En a_c = ω²·r lo que va al cuadrado es ω, que acá no cambia."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá la diferencia entre velocidad angular y velocidad tangencial con el ejemplo de una calesita, y por qué hay aceleración aunque la rapidez sea constante.",
    },
    "f-estatica": {
        "hook": {
            "question": "¿Podés tensar la soga de la ropa hasta que quede perfectamente horizontal con una toalla mojada colgada en el medio?",
            "intuition": "No, por más fuerza que hagas. Para sostener el peso, la soga necesita tirar un poco **hacia arriba**, y solo la componente vertical de la tensión (`T·sen θ`) hace eso. Cuanto más horizontal queda la soga, más chica es esa componente y más grande tiene que ser `T`; perfectamente horizontal haría falta una tensión infinita.",
        },
        "concept": {
            "points": [
                "**Equilibrio de una partícula** (todas las fuerzas pasan por un mismo punto, como un nudo): `ΣFx = 0` y `ΣFy = 0`. Descomponé cada tensión en sus componentes y planteá una ecuación por eje.",
                "**Cuerpo colgado de dos sogas simétricas** que forman un ángulo `θ` con la horizontal: `2·T·sen θ = P`, o sea `T = P / (2·sen θ)`. Verticales (`θ = 90°`) da `T = P/2`; cuanto más horizontales, mayor es la tensión.",
                "**Equilibrio de un cuerpo extenso** (una viga, una barra): hacen falta dos condiciones, `ΣF = 0` (no se acelera) y `ΣM = 0` (no empieza a girar). El **momento** de una fuerza respecto de un punto es `M = F·d`, con `d` la distancia perpendicular del punto a la recta de acción de la fuerza, y lleva signo según el sentido en que haría girar.",
                "**Elección del punto**: en equilibrio, `ΣM = 0` vale respecto de cualquier punto. Conviene elegir uno por donde pase una fuerza desconocida: su brazo es cero, no aparece en la ecuación y queda una sola incógnita.",
                "**Viga apoyada en dos apoyos A y B**: los momentos respecto de A dan `R_B`, y `ΣFy = 0` da `R_A`. El peso de una viga homogénea se aplica en su centro. El apoyo más cercano a la carga soporta la mayor parte.",
            ],
            "real_world": [
                {
                    "title": "La carretilla",
                    "detail": "Es una palanca con el apoyo en la rueda: si la carga de `600 N` está a `0.4 m` del eje y tus manos a `1.2 m`, levantás con `600 · 0.4 / 1.2 = 200 N`, un tercio del peso.",
                },
                {
                    "title": "Andamios y puentes",
                    "detail": "Cuando una persona camina por un tablón apoyado en dos caballetes, la reacción de cada apoyo va cambiando: el más cercano a la persona carga más. Los ingenieros calculan cada apoyo para la peor posición de la carga.",
                },
                {
                    "title": "Cables con 'panza'",
                    "detail": "Los cables de alta tensión, las tirolesas y las cintas de slackline se dejan con algo de flecha: si quedaran casi horizontales, sostener el mismo peso exigiría una tensión enorme y podrían cortarse o arrancar los anclajes.",
                },
            ],
            "key_rule": "Partícula: `ΣFx = 0` y `ΣFy = 0` · Cuerpo extenso: además `ΣM = 0` · `M = F·d` (distancia perpendicular) · tomá momentos en el punto por donde pasa la fuerza que no conocés.",
            "pitfall": "Repartir el peso 'mitad y mitad' sin mirar ángulos ni distancias: dos sogas inclinadas tiran cada una con MÁS que la mitad del peso, y en una viga el apoyo más cercano a la carga se lleva la mayor parte.",
        },
        "example": {
            "title": "Reacciones en un tablón con un pintor",
            "steps": [
                "Un tablón liviano de `5 m` está apoyado en sus extremos A y B. Un pintor de `70 kg` (peso `700 N` con `g = 10 m/s²`) se para a `2 m` de A. Fuerzas sobre el tablón: `R_A` y `R_B` hacia arriba y `700 N` hacia abajo.",
                "Momentos respecto de A (así `R_A` no aparece): `R_B · 5 − 700 · 2 = 0`, entonces `R_B = 280 N`.",
                "Suma de fuerzas verticales: `R_A + R_B = 700`, entonces `R_A = 420 N`. El apoyo A, más cercano al pintor, carga más.",
                "Control tomando momentos respecto de B: `R_A · 5 = 700 · 3`, que da `R_A = 420 N`. Coincide.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Una lámpara de 4 kg cuelga de dos cables simétricos que forman 30° con la horizontal (`sen 30° = 0.5`, `g = 10 m/s²`). ¿Cuánto vale la tensión de cada cable?",
            "options": [
                {"text": "20 N", "ok": False, "feedback": "Repartiste el peso (40 N) en dos mitades, como si los cables colgaran verticales. Inclinados, solo la componente vertical T·sen 30° de cada uno sostiene a la lámpara."},
                {"text": "40 N", "ok": True, "feedback": "Exacto: 2·T·sen 30° = 40 N → 2·T·0.5 = 40 → T = 40 N. Cada cable tira con todo el peso de la lámpara."},
                {"text": "80 N", "ok": False, "feedback": "Planteaste T·sen 30° = 40 N con un solo cable. Son dos cables sosteniendo: 2·T·sen 30° = 40 N."},
            ],
        },
        "checks": [
            {
                "question": "Un tablón de 3 m y peso despreciable está apoyado en sus extremos A y B. Se apoya una caja de 600 N a 1 m de A. ¿Cuánto vale la reacción en A?",
                "options": [
                    {"text": "200 N", "ok": False, "feedback": "Esa es la reacción en B (R_B·3 = 600·1). El apoyo más cercano a la carga, A, soporta la parte mayor."},
                    {"text": "300 N", "ok": False, "feedback": "Repartiste mitad y mitad, y eso vale solo si la carga está en el centro del tablón. Acá está más cerca de A."},
                    {"text": "400 N", "ok": True, "feedback": "Exacto: momentos respecto de B: R_A·3 = 600·2 → R_A = 400 N (y R_B = 200 N)."},
                ],
            },
            {
                "question": "¿Qué tiene que cumplirse para que un cuerpo extenso, como una viga, esté en equilibrio?",
                "options": [
                    {"text": "Alcanza con que la suma de fuerzas sea cero", "ok": False, "feedback": "Dos fuerzas iguales y opuestas aplicadas en puntos distintos suman cero y sin embargo hacen girar al cuerpo (una cupla). Falta pedir ΣM = 0."},
                    {"text": "La suma de fuerzas y la suma de momentos tienen que ser cero", "ok": True, "feedback": "Exacto: ΣF = 0 evita que se acelere y ΣM = 0 evita que empiece a girar."},
                    {"text": "Alcanza con que la suma de momentos respecto de su centro sea cero", "ok": False, "feedback": "Una única fuerza aplicada en el centro tiene momento cero respecto del centro, pero acelera al cuerpo. También hace falta ΣF = 0."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué dos condiciones aseguran el equilibrio de una viga, por qué conviene tomar momentos respecto de un apoyo y por qué una soga casi horizontal soporta una tensión enorme.",
    },
}
