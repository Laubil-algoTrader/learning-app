"""Comprensión lectora y resolución de problemas (ingreso a Ingeniería UNCuyo 2027).

Materia nueva (slug `comprension-problemas`, sin laboratorio). Cinco nodos encadenados:
  - Cómo leer una consigna y un texto de estudio
  - Comprensión de textos científicos: los tipos de pregunta del examen
  - Resumen, síntesis, cuadros y mapas conceptuales
  - Del lenguaje coloquial al simbólico
  - Lógica y lectura de teoremas: proposiciones, conectivos, hipótesis y tesis

Sigue el cuadernillo «Comprensión de textos y estrategias de estudio» del ingreso, su práctica
(TP Nº1), los apuntes «Comprensión lectora 1 y 2» de Resolución de Problemas y la parte de
formulación de expresiones algebraicas del TP Nº3. Los párrafos de las tarjetas son originales.
"""

from __future__ import annotations

CLYRP_LECTURA_NODES: list[dict] = [
    # ==================== CONSIGNAS Y LECTURA COMPRENSIVA ====================
    {
        "slug": "cl-consignas-lectura",
        "title": "Cómo leer una consigna y un texto de estudio",
        "summary": "Reconocer el verbo y el contenido de una consigna, recorrer las tres fases de la lectura comprensiva y distinguir tema, idea central, ideas principales y secundarias para subrayar y anotar al margen.",
        "prerequisites": [],
        "insert_after": "__start__",
        "metadata": {"section": "Comprensión lectora", "est_minutes": 15},
        "items": [
            {
                "item_type": "recall",
                "title": "Qué pide el verbo describir",
                "prompt": "Una consigna de Biología dice: «Describa una célula vegetal». ¿Qué se espera que hagas?",
                "answer": "Enunciar sus características: forma, partes (pared celular, cloroplastos, vacuola…), cómo es. Describir no es definir (dar el significado del concepto) ni explicar (desarrollar causas, relaciones y consecuencias).",
                "hints": ["Pensá en qué responderías a «¿cómo es?».", "Definir responde «¿qué es?»; explicar responde «¿por qué?» o «¿cómo funciona?»."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Enunciar sus características: forma, partes y cómo es",
                            "Dar en una oración el significado del concepto «célula vegetal»",
                            "Desarrollar las causas y consecuencias de su funcionamiento",
                            "Dar ejemplos de plantas que tienen esas células",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Verbo que pide causas, relaciones y consecuencias",
                "prompt": "Una consigna pide desarrollar por qué ocurre un fenómeno, con sus causas, sus relaciones con otros hechos y sus consecuencias. ¿Qué verbo de consigna corresponde a ese pedido?",
                "answer": "Explicar: es desarrollar una idea, teoría o suceso con sus causas, relaciones y consecuencias. Describir se queda en las características; enunciar es formular algo de manera breve; definir es dar el significado.",
                "hints": ["Es el verbo que responde a la pregunta «¿por qué?»."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Describir", "Enunciar", "Explicar", "Definir"],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Qué pide el verbo argumentar",
                "prompt": "Una consigna dice: «Argumente a favor o en contra del uso de la telemedicina». ¿Qué tenés que hacer?",
                "answer": "Tomar una posición y exponer las ideas en que se basa. Argumentar implica discutir un tema defendiendo una postura; si solo definís telemedicina o enumerás sus características, no argumentaste.",
                "hints": ["La consigna dice «a favor o en contra»: hay que elegir un lado.", "Una postura sin razones no es un argumento."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Dar el significado de «telemedicina»",
                            "Enumerar sus características sin opinar",
                            "Tomar una posición y exponer las ideas en que se basa",
                            "Formular en una frase breve un principio sobre la telemedicina",
                        ],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Qué pide el verbo enunciar",
                "prompt": "En un examen de Matemática dice: «Enuncie el teorema de Pitágoras». ¿Qué corresponde hacer?",
                "answer": "Formularlo de manera breve y clara: «En todo triángulo rectángulo, el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos». Enunciar no pide demostrarlo ni dar ejemplos numéricos: eso serían otras consignas (demostrar, ejemplificar).",
                "hints": ["Enunciar es «decir» el principio, no probarlo."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Demostrarlo paso a paso",
                            "Formularlo de manera breve y clara",
                            "Resolver un triángulo rectángulo con números",
                            "Contar quién lo descubrió y en qué época",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Qué pide el verbo comparar",
                "prompt": "Te piden: «Compare los metales y los no metales». ¿Qué respuesta cumple la consigna?",
                "answer": "Una que señale semejanzas y diferencias usando los mismos criterios para ambos (brillo, conductividad, estado a temperatura ambiente…). Describir primero uno y después el otro con criterios distintos no es comparar: es como decir «esta hoja es verde, mientras que aquella es pequeña».",
                "hints": ["Comparar exige semejanzas y diferencias.", "Los criterios tienen que ser los mismos para los dos grupos."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Semejanzas y diferencias según los mismos criterios para ambos grupos",
                            "Una descripción de los metales y, aparte, otra de los no metales con otros criterios",
                            "Solo las diferencias entre ambos grupos",
                            "Una opinión sobre cuál de los dos grupos es más útil",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Reponer el verbo omitido de una consigna",
                "prompt": "Algunas consignas no traen el verbo y hay que reponerlo mentalmente. En la consigna «¿Qué elementos del triángulo son conocidos?», ¿cuál es el verbo omitido?",
                "answer": "Identificar (o indicar): la consigna pide reconocer y señalar cuáles son los datos del triángulo, no calcular los que faltan. Reponer el verbo evita hacer de más o de menos.",
                "hints": ["La pregunta es sobre lo que ya se sabe, no sobre lo que falta.", "Reformulala empezando con un verbo en infinitivo."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Calcular (los elementos que faltan)",
                            "Identificar o indicar (los datos)",
                            "Demostrar (que el triángulo existe)",
                            "Definir (qué es un triángulo)",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Orden de las fases de la lectura comprensiva",
                "prompt": "Ordená las tres fases de la lectura comprensiva tal como se hacen al estudiar un texto.",
                "answer": "Prelectura (lectura rápida para la idea general y para marcar palabras desconocidas) → lectura crítica o comprensiva (párrafo por párrafo, con subrayado y notas marginales) → poslectura (reorganizar en cuadros, mapas, resúmenes o fichas con preguntas).",
                "hints": ["Primero se mira el texto «por arriba».", "Los organizadores gráficos se arman cuando el texto ya está comprendido."],
                "payload": {
                    "check": {
                        "type": "order",
                        "lines": [
                            "Prelectura: lectura rápida para captar la idea general y marcar las palabras desconocidas",
                            "Lectura crítica o comprensiva: análisis párrafo por párrafo con subrayado y notas marginales",
                            "Poslectura: reorganizar la información en cuadros, mapas, resúmenes o fichas con preguntas",
                        ],
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Distinguir el tema de la idea principal",
                "prompt": "Mirá estas dos formulaciones sobre un mismo texto:\n(1) «La importancia del sueño»\n(2) «El sueño es importante porque cumple una función esencial de equilibrio de la vida mental»\n¿Qué es cada una?",
                "answer": "(1) es el tema: dice de qué trata el texto con una frase sin verbo conjugado. (2) es la idea principal: una oración que afirma algo sobre ese tema, el desarrollo esencial del tema central.",
                "hints": ["¿Cuál de las dos afirma algo que podría ser verdadero o falso?", "El tema se nombra; la idea se enuncia con una oración."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "(1) es la idea principal y (2) es el tema",
                            "(1) es el tema y (2) es la idea principal",
                            "Las dos son ideas secundarias",
                            "Las dos son el tema, dicho de dos formas",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Función de una idea secundaria",
                "prompt": "En un párrafo sobre la conductividad eléctrica aparece la oración: «Por ejemplo, el cobre conduce mucho mejor que el hierro». ¿Qué tipo de idea es?",
                "answer": "Una idea secundaria: explica y amplía la idea principal con un ejemplo. Si la sacás, el párrafo conserva su sentido; en cambio, sin la idea principal el párrafo lo pierde.",
                "hints": ["Probá tacharla: ¿el párrafo sigue diciendo lo esencial?", "Los ejemplos, datos y reformulaciones suelen acompañar a otra idea."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Idea principal", "Idea secundaria", "Idea central del texto", "Tema del párrafo"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Elegir una notación marginal adecuada",
                "prompt": "Este párrafo está en un texto sobre informática:\n«Esta disciplina se aplica a numerosas áreas: gestión de negocios, almacenamiento de información, control de procesos, industria, robótica, comunicaciones, investigación… Una de sus aplicaciones más importantes es proveer información oportuna y veraz para tomar decisiones.»\n¿Cuál es la mejor notación marginal para escribir al costado?",
                "answer": "«Aplicaciones de la informática»: la notación marginal es un título de una o dos palabras clave con la idea principal del párrafo. «Robótica» es solo uno de los ejemplos; copiar una oración entera no sintetiza; «Definición» corresponde a otro párrafo.",
                "hints": ["La notación marginal tiene que caber al costado del párrafo: una o dos palabras clave.", "Tiene que abarcar todo el párrafo, no un ejemplo."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Aplicaciones de la informática",
                            "Robótica",
                            "Definición de informática",
                            "Una de sus aplicaciones más importantes es proveer información oportuna y veraz",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== TIPOS DE PREGUNTA SOBRE TEXTOS CIENTÍFICOS ====================
    {
        "slug": "cl-texto-cientifico",
        "title": "Comprensión de textos científicos: los tipos de pregunta del examen",
        "summary": "Reconocer los tipos de pregunta de opción múltiple del ingreso (tema central, idea principal, sentido contextual, incompatibilidad, inferencia, extrapolación, comparación de textos, intención de un recurso) y aplicar una estrategia para cada uno.",
        "prerequisites": ["cl-consignas-lectura"],
        "insert_after": "cl-consignas-lectura",
        "metadata": {"section": "Comprensión lectora", "est_minutes": 25},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Tema central de un texto sobre el hormigón romano",
                "prompt": "«El hormigón que usaban los romanos sigue en pie después de dos mil años, mientras que muchas estructuras modernas se agrietan en pocas décadas. Durante mucho tiempo se atribuyó esa durabilidad a la ceniza volcánica de la mezcla. Estudios recientes encontraron, además, pequeños grumos de cal que funcionan como una reserva: cuando aparece una fisura y entra agua, la cal se disuelve, reacciona y vuelve a sellar la grieta. Hoy se ensayan mezclas que imitan ese mecanismo.»\n\n¿Cuál es el tema central del texto?",
                "answer": "La autorreparación del hormigón romano y su posible imitación: abarca todo el texto sin pasarse. La ceniza volcánica es la explicación anterior, que el texto completa; las grietas modernas aparecen solo como contraste; «la arquitectura romana» es demasiado amplio.",
                "hints": ["El tema central tiene que abarcar todo el texto, no solo la primera oración.", "Descartá lo que es un dato parcial y lo que es más amplio que el texto."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "La autorreparación del hormigón romano y su posible imitación",
                            "La ceniza volcánica como causa de la durabilidad del hormigón",
                            "Las grietas de las estructuras modernas",
                            "La historia de la arquitectura romana",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Idea principal de un texto sobre el color del cielo",
                "prompt": "«La luz del Sol parece blanca, pero es una mezcla de todos los colores. Al atravesar la atmósfera, choca con las moléculas de nitrógeno y oxígeno, que desvían mucho más la luz de longitud de onda corta —violeta y azul— que la de onda larga, como el rojo. Ese azul desviado nos llega desde todas las direcciones del cielo. Que no lo veamos violeta se debe a que el Sol emite menos violeta y nuestros ojos son menos sensibles a él. Al atardecer, la luz recorre mucho más aire: casi todo el azul se dispersa antes de llegar y predominan los tonos rojizos.»\n\n¿Cuál es la idea principal?",
                "answer": "«El cielo se ve azul porque la atmósfera desvía mucho más la luz azul del Sol que la roja»: es lo esencial que el texto afirma. Que la luz solar sea una mezcla es el punto de partida; la sensibilidad del ojo al violeta y el atardecer rojizo son ideas secundarias que completan la explicación.",
                "hints": ["Las cuatro opciones son verdaderas según el texto: buscá la que explica lo que todo el párrafo desarrolla.", "Las aclaraciones y las consecuencias suelen ser ideas secundarias."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "La luz del Sol es una mezcla de todos los colores",
                            "El cielo se ve azul porque la atmósfera desvía mucho más la luz azul que la roja",
                            "Nuestros ojos son poco sensibles a la luz violeta",
                            "Los atardeceres son rojizos porque la luz recorre más aire",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Sentido contextual de la palabra poderosa",
                "prompt": "«En los años cincuenta, calcular cómo se deformaba el ala de un avión exigía semanas de cuentas a mano. El método de los elementos finitos cambió eso: divide la pieza en miles de trozos simples, resuelve ecuaciones sencillas en cada uno y después los ensambla. Hoy es una herramienta tan poderosa que permite predecir, antes de fabricar nada, dónde se va a fisurar un puente o cómo se calienta un chip.»\n\nEn el texto, la palabra PODEROSA adquiere el sentido de:",
                "answer": "Eficaz: el texto destaca lo que la herramienta logra hacer (predecir fallas). Ingente significa enorme en tamaño o cantidad; adinerada es otra acepción real de poderoso (muy rico), pero no encaja con una herramienta: es la trampa del significado más común; inusitada, poco habitual. Probá cada sinónimo en la oración: solo «tan eficaz que permite predecir» mantiene el sentido.",
                "hints": ["Reemplazá la palabra por cada opción y releé la oración completa.", "Fijate qué destaca el texto de la herramienta: ¿su tamaño, su rareza o lo que logra?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Eficaz", "Ingente", "Adinerada", "Inusitada"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Afirmación incompatible sobre los tardígrados",
                "prompt": "«Los tardígrados son animales que rara vez superan el milímetro que viven, por ejemplo, en el musgo húmedo. Cuando el ambiente se seca, pierden casi toda el agua de su cuerpo, se encogen y detienen su metabolismo. En ese estado, llamado criptobiosis, toleran temperaturas cercanas al cero absoluto, radiaciones intensas e incluso el vacío del espacio, como se comprobó en un experimento orbital en 2007. Al volver a mojarse, muchos se reactivan en pocas horas. Activos e hidratados, en cambio, son bastante frágiles.»\n\nResulta INCOMPATIBLE con el texto afirmar que los tardígrados:",
                "answer": "Son igual de resistentes activos que en criptobiosis: el texto dice lo contrario («activos e hidratados son bastante frágiles»). Las otras tres afirmaciones están en el texto. Incompatible significa que contradice al texto, no que «no se menciona».",
                "hints": ["Buscá la opción que choca con una oración concreta del texto.", "Releé la última oración."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "detienen su metabolismo al deshidratarse",
                            "fueron expuestos al vacío del espacio",
                            "son igual de resistentes activos que en criptobiosis",
                            "pueden habitar en el musgo",
                        ],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Qué se puede colegir sobre la resistencia a los antibióticos",
                "prompt": "«Cada vez que se usa un antibiótico mueren las bacterias sensibles, pero pueden sobrevivir unas pocas que, por mutaciones al azar, ya resistían al fármaco. Esas sobrevivientes se multiplican sin competencia y, con el tiempo, la población entera pasa a ser resistente. Por eso los médicos insisten en no tomar antibióticos contra los resfríos —causados por virus, sobre los que esos fármacos no actúan— y en completar los tratamientos indicados.»\n\nDel texto se puede colegir que:",
                "answer": "Tomar antibióticos sin necesidad favorece que se multipliquen las bacterias resistentes: no está escrito literalmente, pero se deduce del mecanismo (cada uso selecciona a las resistentes) y de la recomendación médica. Colegir es inferir, deducir. El texto dice que las mutaciones son al azar y previas (el fármaco selecciona, no las provoca), que los antibióticos no actúan sobre virus, y no compara la peligrosidad de bacterias y virus.",
                "hints": ["Una inferencia se apoya en el texto pero no lo copia.", "Descartá lo que contradice al texto y lo que va más allá de lo que dice."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "tomar antibióticos sin necesidad favorece que se multipliquen las bacterias resistentes",
                            "los antibióticos provocan las mutaciones que vuelven resistentes a las bacterias",
                            "los resfríos se curan más rápido con antibióticos",
                            "las bacterias resistentes son más peligrosas que los virus",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Extrapolación sobre el agua de deshielo",
                "prompt": "«En Mendoza, la mayor parte del agua de riego proviene del deshielo de la nieve acumulada en la cordillera durante el invierno. Los ríos alcanzan su caudal máximo a fines de la primavera y en el verano, cuando el calor derrite esa reserva, y lo pierden hacia el otoño. Los diques permiten guardar parte de ese caudal para usarlo en los meses de menor escurrimiento.»\n\nSi durante varios inviernos seguidos nevara mucho menos de lo normal en la cordillera, probablemente:",
                "answer": "Disminuiría el agua disponible para riego en los veranos siguientes: es aplicar la lógica del texto (riego ← deshielo ← nieve) a la nueva condición. Con menos nieve los ríos no crecerían más; los diques serían más importantes, no menos; y el texto no da ninguna base para hablar de lluvias de verano.",
                "hints": ["Seguí la cadena causa → efecto que plantea el texto.", "En una extrapolación, descartá las consecuencias que el texto no permite sostener."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "aumentaría el caudal de los ríos en el verano",
                            "disminuiría el agua disponible para riego en los veranos siguientes",
                            "los diques dejarían de ser útiles",
                            "el agua de riego pasaría a provenir de las lluvias de verano",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Tema común de dos lecturas sobre autos eléctricos",
                "prompt": "Lectura A: «Los autos eléctricos no emiten gases por el caño de escape, lo que mejora el aire de las ciudades. Además, un motor eléctrico aprovecha cerca del 90 % de la energía que recibe, mientras que un motor naftero, en el uso real, aprovecha alrededor de la cuarta parte.»\nLectura B: «Que un auto eléctrico no tenga caño de escape no significa que no contamine: si la electricidad con la que se carga proviene de centrales a carbón, las emisiones solo se mudan de la calle a la usina. Fabricar sus baterías exige, además, extraer litio y otros minerales.»\n\nTanto la lectura A como la B abordan el tema de:",
                "answer": "El impacto ambiental de los autos eléctricos: A lo presenta como positivo y B lo relativiza, pero las dos hablan de eso. Las ventajas son el enfoque de A solamente; las centrales a carbón y el litio son argumentos de B, no el tema común.",
                "hints": ["El tema común tiene que estar en las dos lecturas, aunque opinen distinto.", "Descartá lo que aparece en una sola."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "las ventajas de los autos eléctricos",
                            "la contaminación de las centrales a carbón",
                            "el impacto ambiental de los autos eléctricos",
                            "la extracción de litio para baterías",
                        ],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Significado de acuciante",
                "prompt": "«La acuciante falta de agua obligó a racionar el riego en toda la provincia.» En esta oración, ACUCIANTE significa:",
                "answer": "Apremiante o urgente: acuciar es apremiar, dar prisa, inquietar. Intermitente es lo que se interrumpe y vuelve; acuciante no dice nada sobre la intensidad leve ni sobre que algo sea imaginario.",
                "hints": ["Si obligó a racionar, ¿era un problema que podía esperar?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Apremiante, urgente", "Intermitente", "Leve, pasajera", "Imaginaria"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Significado de irrecusable",
                "prompt": "«Las mediciones de los dos laboratorios coincidieron: era una prueba irrecusable de que el material fallaba por fatiga.» IRRECUSABLE significa:",
                "answer": "Que no se puede rechazar ni poner en duda: recusar es rechazar, y el prefijo «ir-» lo niega. Por eso en las preguntas del ingreso «determina de forma irrecusable» equivale a «determina sin lugar a dudas».",
                "hints": ["Separá el prefijo: ir- + recusable.", "Recusar es rechazar."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Dudosa, discutible",
                            "Que no se puede rechazar ni poner en duda",
                            "Que se puede repetir muchas veces",
                            "Que todavía no fue publicada",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Significado de inmanente",
                "prompt": "«Para el autor, la curiosidad es inmanente a la ciencia.» INMANENTE significa:",
                "answer": "Inherente: que forma parte de la esencia de algo y no le viene de afuera. No confundir con inminente (que está por ocurrir) ni con trascendente (que va más allá de algo, lo contrario de inmanente).",
                "hints": ["Es una palabra parecida a otra que significa «que está por suceder»: no es esa.", "Su opuesto filosófico es «trascendente»."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Que está por ocurrir muy pronto",
                            "Que va más allá de la ciencia",
                            "Inherente, que forma parte de su esencia",
                            "Que permanece sin cambios para siempre",
                        ],
                        "correct": 2,
                    },
                },
            },
        ],
    },
    # ==================== ORGANIZADORES DE LA INFORMACIÓN ====================
    {
        "slug": "cl-organizadores",
        "title": "Resumen, síntesis, cuadros y mapas conceptuales",
        "summary": "Diferenciar resumen y síntesis, y elegir entre esquema, cuadro sinóptico, cuadro comparativo y mapa conceptual según cómo está organizado el contenido.",
        "prerequisites": ["cl-consignas-lectura"],
        "insert_after": "cl-texto-cientifico",
        "metadata": {"section": "Comprensión lectora", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Extensión de un resumen sin consigna de tamaño",
                "prompt": "Tenés que resumir un artículo de 1200 palabras y el profesor no fijó la extensión. ¿Cuántas palabras debería tener, aproximadamente, tu resumen? Respondé solo con el número.",
                "answer": "300: cuando no se propone otra extensión, un resumen ocupa aproximadamente el 25 % del texto de partida, y 25 % de 1200 = 1200 / 4 = 300.",
                "hints": ["El cuadernillo da un porcentaje orientativo para el resumen: es la cuarta parte.", "Calculá ese porcentaje de 1200."],
                "payload": {"check": {"type": "numeric", "value": 300, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Técnica redactada con vocabulario propio",
                "prompt": "Un compañero reduce un texto reescribiéndolo con sus propias palabras y su propio estilo, reorganiza las ideas y las relaciona con lo que ya sabía. ¿Qué técnica usó?",
                "answer": "Una síntesis: condensa la información como el resumen, pero con vocabulario y estilo propios; es una reelaboración personal que forma un mensaje nuevo. El resumen, en cambio, conserva el vocabulario del autor y el orden de aparición de las ideas.",
                "hints": ["Las dos técnicas redactadas reducen el texto; la diferencia está en de quién son las palabras."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Resumen", "Síntesis", "Notación marginal", "Cuadro sinóptico"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Qué se omite al resumir",
                "prompt": "Al hacer un resumen, ¿qué información se omite?",
                "answer": "La información secundaria: ejemplos, reformulaciones, situaciones repetidas, diálogos. En cambio se conservan las ideas principales, el orden en que el autor las desarrolla y el vocabulario técnico de la asignatura.",
                "hints": ["El resumen conserva la estructura del pensamiento del autor.", "Lo que se saca es lo que amplía o repite."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "El vocabulario técnico, reemplazándolo por palabras comunes",
                            "Los ejemplos, las reformulaciones y lo repetido",
                            "El orden en que el autor presenta las ideas",
                            "Las ideas principales, para que quede corto",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Filas y columnas de un cuadro comparativo",
                "prompt": "Querés comparar lenguaje, lengua, dialecto y habla según su definición y sus características. En un cuadro comparativo, ¿cómo se ubican los elementos y los criterios?",
                "answer": "Los elementos a comparar (lenguaje, lengua, dialecto, habla) van en la primera fila, uno por columna, y los criterios o variables de análisis (definición, características) en la primera columna, uno por fila. Así cada criterio se aplica a todos los elementos.",
                "hints": ["Hay una columna por cada cosa que comparás.", "Cada fila es una misma pregunta que le hacés a todos."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Elementos en la primera fila (columnas) y criterios en la primera columna (filas)",
                            "Un cuadro distinto para cada elemento",
                            "Todo en una sola columna, alternando elementos y criterios",
                            "Criterios distintos para cada elemento, según lo que diga el texto de cada uno",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Comparar con un mismo criterio",
                "prompt": "¿Cuál de estas oraciones es una comparación correcta?",
                "answer": "«El cobre funde a unos 1085 °C y el aluminio a unos 660 °C»: usa el mismo criterio (temperatura de fusión) para los dos. Las demás mezclan criterios distintos, como el ejemplo del cuadernillo «esta hoja es verde, mientras que aquella es pequeña».",
                "hints": ["Fijate si las dos partes de la oración responden a la misma pregunta."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "El cobre es rojizo, mientras que el aluminio es liviano",
                            "El cobre funde a unos 1085 °C y el aluminio a unos 660 °C",
                            "El cobre conduce bien la electricidad y el aluminio es barato",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Cuándo conviene un cuadro sinóptico",
                "prompt": "¿Para qué tipo de contenido está especialmente indicado el cuadro sinóptico?",
                "answer": "Para temas con muchas clasificaciones y subdivisiones: con llaves, de izquierda a derecha, muestra de un vistazo cómo se divide el tema. Para comparar entidades con los mismos criterios conviene el cuadro comparativo; para relaciones entre conceptos, el mapa conceptual.",
                "hints": ["Pensá en su herramienta gráfica: las llaves que agrupan."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Temas con muchas clasificaciones y subdivisiones",
                            "Comparar varias entidades según los mismos criterios",
                            "Mostrar relaciones entre conceptos con palabras de enlace",
                            "Reescribir el texto con palabras propias",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Qué va sobre las líneas de un mapa conceptual",
                "prompt": "En un mapa conceptual, ¿qué se escribe sobre o junto a las líneas que unen los conceptos?",
                "answer": "Las palabras de enlace (conectores): verbos, adverbios, preposiciones o conjunciones que dicen qué relación hay entre los conceptos, como «se clasifica en», «produce», «por ejemplo». Los conceptos van dentro de las figuras.",
                "hints": ["Leídos en orden, concepto + línea + concepto tienen que formar una frase con sentido."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Los conceptos más importantes",
                            "Palabras de enlace que indican la relación",
                            "Números de orden de lectura",
                            "Oraciones completas copiadas del texto",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Proposición bien formada en un mapa conceptual",
                "prompt": "¿Cuál de estos fragmentos de mapa conceptual forma una proposición correcta? (Los corchetes representan las figuras con conceptos.)",
                "answer": "[Energía] —puede ser→ [cinética]: dos conceptos unidos por una palabra de enlace forman una unidad con sentido, y el más general está arriba. Una línea sin enlace no dice la relación; una oración entera dentro de la figura no es un concepto; e invertir el orden dice algo falso.",
                "hints": ["Una proposición es concepto + palabra de enlace + concepto.", "Leela en voz alta: ¿es verdadera y tiene sentido?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "[Energía] —puede ser→ [cinética]",
                            "[Energía] ——— [cinética]",
                            "[La energía puede ser cinética o potencial]",
                            "[Cinética] —puede ser→ [energía]",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Jerarquía de los conceptos en un mapa conceptual",
                "prompt": "Ordená estos conceptos como irían en un mapa conceptual, de arriba (el más general) hacia abajo (el más específico).",
                "answer": "Materia → sustancias puras → elementos químicos → hierro. En un mapa conceptual los conceptos más generales e inclusivos van arriba y, al descender, aparecen los más específicos y los ejemplos.",
                "hints": ["Cada concepto tiene que incluir al que va debajo.", "El ejemplo concreto va al final."],
                "payload": {
                    "check": {
                        "type": "order",
                        "lines": ["Materia", "Sustancias puras", "Elementos químicos", "Hierro"],
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Ideas de igual jerarquía en un esquema",
                "prompt": "Al armar un esquema de contenidos, ¿cómo se escriben dos ideas secundarias que tienen la misma jerarquía?",
                "answer": "Al mismo nivel (misma sangría), con la misma forma gramatical y el mismo tipo de numeración (por ejemplo, I y II, o a y b). Así la disposición gráfica muestra la estructura del texto de un vistazo.",
                "hints": ["En un esquema, la posición en la hoja indica la importancia."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Una debajo de la otra, con sangría cada vez mayor",
                            "Al mismo nivel, con la misma forma y el mismo tipo de numeración",
                            "Dentro de la idea principal, como una oración larga",
                        ],
                        "correct": 1,
                    },
                },
            },
        ],
    },
    # ==================== LENGUAJE COLOQUIAL Y SIMBÓLICO ====================
    {
        "slug": "cl-lenguaje-simbolico",
        "title": "Del lenguaje coloquial al simbólico",
        "summary": "Traducir enunciados coloquiales a expresiones simbólicas y viceversa (doble, mitad, consecutivos, «excede en», cuadrado de la suma), y leer la notación de conjuntos y los cuantificadores.",
        "prerequisites": ["cl-consignas-lectura"],
        "insert_after": "cl-organizadores",
        "metadata": {"section": "Lenguaje y lógica", "est_minutes": 20},
        "items": [
            {
                "item_type": "recall",
                "title": "Traducir el doble de la suma",
                "prompt": "Elegí la traducción simbólica de: «el doble de la suma de un número y cinco».",
                "answer": "2.(x + 5): la frase empieza con «el doble de…», así que duplicar es la última operación y se aplica a toda la suma; por eso va entre paréntesis. 2x + 5 sería «la suma del doble de un número y cinco».",
                "hints": ["La primera palabra («doble») indica la operación que se hace al final.", "Todo lo que viene después de «de» es lo que se duplica."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["2x + 5", "2.(x + 5)", "(x + 5)²", "2 + (x + 5)"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Traducir la suma de los cuadrados",
                "prompt": "Elegí la traducción simbólica de: «la suma de los cuadrados de dos números».",
                "answer": "a² + b²: primero se eleva cada número al cuadrado y la última operación es la suma. (a + b)² es «el cuadrado de la suma», y no es lo mismo: (a + b)² = a² + 2ab + b².",
                "hints": ["La frase empieza con «la suma de…»: ¿qué es lo que se suma?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["(a + b)²", "a² + b²", "2a + 2b", "a².b²"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Expresar tres números pares consecutivos",
                "prompt": "Con n ∈ Z, ¿cuál de estas ternas representa SIEMPRE a tres números pares consecutivos?",
                "answer": "2n, 2n + 2 y 2n + 4: 2n es par para cualquier entero n, y entre dos pares consecutivos hay 2 de diferencia. 2n, 2n + 1, 2n + 2 son consecutivos cualesquiera (el del medio es impar); n, n + 2, n + 4 son impares si n es impar; y 2n, 4n, 6n no sirve en general (con n = 3 da 6, 12, 18).",
                "hints": ["Un par se escribe 2n.", "¿Cuánto hay que sumarle a un par para llegar al par siguiente?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["2n, 2n + 1 y 2n + 2", "n, n + 2 y n + 4", "2n, 2n + 2 y 2n + 4", "2n, 4n y 6n"],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Plantear y resolver: el doble menos la mitad",
                "prompt": "Si al doble de un número se le resta su mitad, resulta 54. ¿Cuál es el número? Respondé solo con el número.",
                "answer": "36: la ecuación es 2x − x/2 = 54. Como 2x − x/2 = 3x/2, queda 3x/2 = 54, entonces x = 54 . 2/3 = 36. Verificación: 2 . 36 − 36/2 = 72 − 18 = 54.",
                "hints": ["Traducí por partes: «el doble de un número», «su mitad», «resulta».", "Multiplicá toda la ecuación por 2 para sacar el denominador."],
                "payload": {"check": {"type": "numeric", "value": 36, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Traducir excede en",
                "prompt": "Sea a la edad de Ana y l la de Luis. Elegí la traducción de: «la edad de Ana excede en 7 años a la de Luis».",
                "answer": "a − l = 7: «a excede a b en c» significa que a es mayor que b y que la diferencia a − b es c. a = 7l diría «siete veces»; l − a = 7 y a + 7 = l dirían que Luis es el mayor.",
                "hints": ["¿Quién es mayor, Ana o Luis?", "«Exceder en» habla de una diferencia, no de un producto."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["l − a = 7", "a = 7l", "a − l = 7", "a + 7 = l"],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Traducir la diferencia entre el triplo y cuatro",
                "prompt": "Elegí la traducción simbólica de: «la diferencia entre el triplo de un número y cuatro».",
                "answer": "3x − 4: la última operación es la diferencia (se nombra primero), su primer término es el triplo del número y el segundo es 4, en ese orden. 3.(x − 4) sería «el triplo de la diferencia»; triplo es multiplicar por 3, no elevar al cubo.",
                "hints": ["«La diferencia entre A y B» es A − B, en ese orden.", "Triplo (o triple) significa «tres veces»."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["3.(x − 4)", "4 − 3x", "x³ − 4", "3x − 4"],
                        "correct": 3,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Traducir el cociente entre un número y su consecutivo",
                "prompt": "Elegí la traducción simbólica de: «el cociente entre un número y su consecutivo».",
                "answer": "x/(x + 1): el consecutivo de x es x + 1 y va entero en el denominador, por eso lleva paréntesis. Sin ellos, x/x + 1 significa (x/x) + 1, que vale 2 para todo x ≠ 0.",
                "hints": ["¿Cómo se escribe el consecutivo de x?", "Pensá qué se divide primero si no ponés paréntesis."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["x/(x + 1)", "(x + 1)/x", "x/x + 1", "x.(x + 1)"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Definir por extensión un conjunto de naturales",
                "prompt": "Definí por extensión el conjunto A = { x ∈ IN / x < 6 }.",
                "answer": "A = {1, 2, 3, 4, 5}: la barra «/» se lee «tal que», así que A reúne a los naturales menores que 6. En el ingreso IN no incluye el 0 (el conjunto con el 0 es IN₀), y el 6 queda afuera porque la desigualdad es estricta.",
                "hints": ["«Por extensión» significa listar todos los elementos.", "Revisá si el 0 es natural en la convención del ingreso y si el 6 cumple x < 6."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["{0, 1, 2, 3, 4, 5}", "{1, 2, 3, 4, 5}", "{1, 2, 3, 4, 5, 6}", "{6}"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Leer en palabras un cuantificador universal",
                "prompt": "¿Cuál es la lectura correcta de ∀ x ∈ IR: x² ≥ 0?",
                "answer": "«Para todo número real x, su cuadrado es mayor o igual que cero». ∀ se lee «para todo». Decir «positivo» es un error: 0² = 0 no es positivo; x² ≥ 0 significa «no negativo».",
                "hints": ["∀ es «para todo»; ∃ es «existe».", "≥ 0 incluye al cero."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Para todo número real x, su cuadrado es mayor o igual que cero",
                            "Existe un número real cuyo cuadrado es mayor o igual que cero",
                            "Todo número real elevado al cuadrado da un resultado positivo",
                            "Para todo número real x, x es mayor o igual que su cuadrado",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Simbolizar un enunciado existencial",
                "prompt": "Elegí la traducción simbólica de: «hay al menos un número entero cuyo cuadrado es 4».",
                "answer": "∃ x ∈ Z / x² = 4: «hay al menos uno» es el cuantificador existencial ∃, y «cuyo» funciona como «tal que». Con ∀ diría que todos los enteros cumplen x² = 4 (falso: 3² = 9); x = 4² dice que x es 16; 2x = 4 habla del doble, no del cuadrado.",
                "hints": ["«Hay al menos un» se simboliza con ∃.", "El cuadrado de x es x², no 2x."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["∀ x ∈ Z: x² = 4", "∃ x ∈ Z / x = 4²", "∃ x ∈ Z / 2x = 4", "∃ x ∈ Z / x² = 4"],
                        "correct": 3,
                    },
                },
            },
        ],
    },
    # ==================== LÓGICA Y LECTURA DE TEOREMAS ====================
    {
        "slug": "cl-logica-enunciados",
        "title": "Lógica y lectura de teoremas: proposiciones, conectivos, hipótesis y tesis",
        "summary": "Reconocer proposiciones, negarlas (incluidos «todos» y «algunos»), usar las tablas de verdad de los conectivos y leer un teorema: hipótesis, tesis, recíproco, contrario, contrarrecíproco, condiciones necesarias y suficientes y contraejemplos.",
        "prerequisites": ["cl-lenguaje-simbolico"],
        "insert_after": "cl-lenguaje-simbolico",
        "metadata": {"section": "Lenguaje y lógica", "est_minutes": 30},
        "items": [
            {
                "item_type": "recall",
                "title": "Reconocer una proposición",
                "prompt": "¿Cuál de estas expresiones es una proposición?",
                "answer": "«7 es un número primo»: es un enunciado declarativo al que se le puede asignar un único valor de verdad (en este caso, V). Una pregunta o una orden no son ni verdaderas ni falsas, y x + 3 = 5 depende del valor de x: es una forma abierta (función proposicional), no una proposición.",
                "hints": ["Una proposición es verdadera o falsa, sin depender de nada más.", "Probá preguntarte «¿es verdad?» ante cada opción."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["¿Cuánto mide el lado?", "7 es un número primo", "x + 3 = 5", "Resolvé la ecuación"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Negar una afirmación con todos",
                "prompt": "¿Cuál es la negación de «Todos los números primos son impares»?",
                "answer": "«Existe al menos un número primo que no es impar»: negar un «para todo» es afirmar que hay al menos un caso que no cumple. «Ninguno es impar» o «todos son pares» son afirmaciones contrarias, no la negación; «algunos son impares» no contradice a la original. Acá la original es falsa (2 es primo y par) y su negación, verdadera.",
                "hints": ["Para que «todos cumplen» sea falso, alcanza con un caso que no cumpla.", "Una proposición y su negación siempre tienen valores de verdad opuestos."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Ningún número primo es impar",
                            "Todos los números primos son pares",
                            "Existe al menos un número primo que no es impar",
                            "Algunos números primos son impares",
                        ],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Negar una afirmación con algún",
                "prompt": "¿Cuál es la negación de «Algún número real es mayor que su cuadrado»?",
                "answer": "«Todo número real es menor o igual que su cuadrado»: negar un «existe» es afirmar que ninguno cumple, o sea que todos cumplen lo contrario; y lo contrario de «mayor» es «menor o igual». «Algún real no es mayor…» puede ser verdadera a la vez que la original (1/2 > 1/4 pero 2 < 4), y «menor» a secas olvida el caso de igualdad (1 = 1²).",
                "hints": ["La negación de ∃ x / P(x) es ∀ x: no P(x).", "La negación de x > y es x ≤ y."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Algún número real no es mayor que su cuadrado",
                            "Todo número real es menor que su cuadrado",
                            "Todo número real es mayor que su cuadrado",
                            "Todo número real es menor o igual que su cuadrado",
                        ],
                        "correct": 3,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Valores de verdad con conectivos",
                "prompt": "Sean p: «3 es impar» y q: «3 > 5». ¿Cuál de estas proposiciones compuestas es verdadera?",
                "answer": "p ∨ q: p es V y q es F, y una disyunción es verdadera si al menos una de sus partes lo es. En cambio p ∧ q es F (hace falta que las dos sean V), ~p es F (p es V) y p ⇔ q es F (p y q tienen distinto valor).",
                "hints": ["Primero decidí el valor de p y el de q.", "Después usá la tabla de cada conectivo."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["p ∧ q", "p ∨ q", "~p", "p ⇔ q"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Único caso falso de un condicional",
                "prompt": "¿En qué caso el condicional p ⇒ q es FALSO?",
                "answer": "Solo cuando el antecedente p es verdadero y el consecuente q es falso. Si p es falso, p ⇒ q es verdadero sea cual sea q: el condicional solo promete algo para los casos en que p se cumple.",
                "hints": ["Pensá en una promesa: «si aprobás, te regalo una bici». ¿Cuándo se rompe la promesa?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Cuando p es verdadera y q es falsa",
                            "Cuando p es falsa y q es verdadera",
                            "Cuando p y q son falsas",
                            "Siempre que p es falsa",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Identificar la tesis de un teorema",
                "prompt": "Teorema: «Si un triángulo es rectángulo, entonces el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos». ¿Cuál es la tesis?",
                "answer": "«El cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos»: la tesis es el consecuente, lo que el teorema garantiza. La hipótesis es lo que se supone (el triángulo es rectángulo). Invertir el «si…, entonces…» da el recíproco, que es otro enunciado.",
                "hints": ["En «si H, entonces T», la tesis es lo que va después de «entonces»."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "El triángulo es rectángulo",
                            "El cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos",
                            "Si el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos, el triángulo es rectángulo",
                            "La hipotenusa es el lado más largo del triángulo",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Escribir el contrarrecíproco",
                "prompt": "¿Cuál es el contrarrecíproco de «Si n es divisible por 6, entonces n es par»?",
                "answer": "«Si n no es par, entonces n no es divisible por 6»: el contrarrecíproco de p ⇒ q es ~q ⇒ ~p (se intercambian y se niegan ambas). «Si n es par, es divisible por 6» es el recíproco (falso: n = 4); «si n no es divisible por 6, no es par» es el contrario (falso: n = 4); la cuarta opción es la negación del condicional.",
                "hints": ["Contrarrecíproco: intercambiá hipótesis y tesis Y negá las dos.", "Debería ser verdadero si el original lo es."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Si n es par, entonces n es divisible por 6",
                            "Si n no es divisible por 6, entonces n no es par",
                            "Si n no es par, entonces n no es divisible por 6",
                            "n es divisible por 6 y n no es par",
                        ],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Qué enunciado asociado sigue siendo verdadero",
                "prompt": "Sabés que es verdadero el teorema «Si un cuadrilátero es un cuadrado, entonces sus diagonales son iguales». ¿Cuál de estos enunciados es seguro verdadero, sin más análisis?",
                "answer": "«Si las diagonales de un cuadrilátero no son iguales, entonces no es un cuadrado»: es el contrarrecíproco, equivalente al teorema. El recíproco («si las diagonales son iguales, es un cuadrado») y el contrario («si no es un cuadrado, sus diagonales no son iguales») son falsos: un rectángulo no cuadrado tiene diagonales iguales.",
                "hints": ["Solo una de las formas asociadas tiene siempre el mismo valor de verdad que el condicional original.", "Buscá un cuadrilátero que no sea cuadrado pero tenga diagonales iguales."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Si las diagonales de un cuadrilátero son iguales, entonces es un cuadrado",
                            "Si un cuadrilátero no es un cuadrado, entonces sus diagonales no son iguales",
                            "Si las diagonales de un cuadrilátero no son iguales, entonces no es un cuadrado",
                        ],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Condición necesaria en un condicional",
                "prompt": "Es verdadero que «si n es divisible por 6, entonces n es par». Para que n sea divisible por 6, ser par es una condición…",
                "answer": "Necesaria, pero no suficiente: en p ⇒ q, la tesis q es condición necesaria para p (sin ser par, no hay forma de ser divisible por 6) y la hipótesis p es condición suficiente para q. Ser par no alcanza: 4 es par y no es divisible por 6.",
                "hints": ["¿Puede un número impar ser divisible por 6?", "¿Alcanza con ser par para ser divisible por 6? Probá con 4."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Suficiente, pero no necesaria",
                            "Necesaria, pero no suficiente",
                            "Necesaria y suficiente",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Encontrar un contraejemplo",
                "prompt": "¿Cuál de estos valores es un contraejemplo de «Para todo x ∈ IR, x² > x»?",
                "answer": "x = 1/2: (1/2)² = 1/4, y 1/4 > 1/2 es falso. Un contraejemplo es un caso que cumple la hipótesis (es real) pero no la tesis, y alcanza uno solo para refutar un «para todo». Con 2, −3 y −1/2 la desigualdad se cumple (4 > 2, 9 > −3, 1/4 > −1/2).",
                "hints": ["Probá cada valor en x² > x.", "Los números entre 0 y 1 se achican al elevarlos al cuadrado."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["x = 2", "x = −1/2", "x = 1/2", "x = −3"],
                        "correct": 2,
                    },
                },
            },
        ],
    },
]


CLYRP_LECTURA_LESSONS: dict[str, dict] = {
    "cl-consignas-lectura": {
        "hook": {
            "question": "En un parcial te piden «Explique por qué un cuerpo en caída libre acelera». Escribís una definición de aceleración prolija y correcta. ¿Te dan el punto?",
            "intuition": "Probablemente no: **definiste**, pero te pidieron **explicar** (causas y relaciones). El cuadernillo del ingreso lo advierte: muchos fracasos en los exámenes se deben más a no interpretar la consigna que a no saber el tema. Leer bien empieza por el verbo.",
        },
        "concept": {
            "points": [
                "**Una consigna = verbo + contenido.** El verbo (en infinitivo, «definir», o en imperativo, «defina») dice qué hacer; el contenido, sobre qué. En «Definir por extensión el conjunto A = { x ∈ IN / x < 6 }» el verbo es definir y el contenido, el conjunto A. Para comprenderla: identificá el objetivo (el o los verbos), los conceptos que involucra, el **orden y la jerarquía** de las acciones y la mejor estrategia. Si el verbo no está («¿Qué elementos son conocidos?»), reponelo vos: identificar.",
                "**Verbos de consigna**:\n| Verbo | Qué pide |\n|---|---|\n| Definir | Dar el significado de un concepto |\n| Describir | Enunciar las características de un objeto, hecho o situación |\n| Explicar | Desarrollar una idea o suceso con sus causas, relaciones y consecuencias |\n| Ejemplificar | Dar situaciones concretas que reflejen una idea general |\n| Enunciar | Formular una idea, principio o teorema de manera breve y clara |\n| Argumentar | Tomar posición y exponer las ideas en que se basa |\n| Fundamentar | Construir un sistema de razones o pruebas que sustente una afirmación |\n| Comparar | Señalar semejanzas y diferencias con los mismos criterios |",
                "**Lector activo** y las **tres fases de la lectura comprensiva**: (1) **prelectura** o lectura rápida: idea general, títulos, imágenes, palabras desconocidas; (2) **lectura crítica o comprensiva**: párrafo por párrafo, separando hechos de opiniones, con subrayado y notas marginales; (3) **poslectura**: reorganizar en cuadros, mapas, resúmenes o fichas con preguntas. Antes de leer, preguntate para qué leés y qué sabés del tema.",
                "**Jerarquía textual.** El **tema** dice de qué trata el texto con una frase sin verbo conjugado («La importancia del sueño»). La **idea central** es la idea vertebral de todo el texto, formulada como oración. La **idea principal** es la más importante de cada párrafo: si la sacás, el párrafo pierde sentido. Las **ideas secundarias** la explican y amplían (ejemplos, datos, reformulaciones). En las preguntas de examen, «idea principal del texto» se usa como sinónimo de idea central.",
                "**Subrayado**: no en la primera lectura; solo lo esencial, con la menor cantidad de palabras y sin marcar dos veces la misma idea. **Notación marginal**: al costado de cada párrafo, un título de una o dos palabras clave (o un símbolo) con su idea principal, para ver de un golpe de vista la estructura del texto.",
            ],
            "real_world": [
                {
                    "title": "Parciales de Matemática y Física",
                    "detail": "«Determine…, grafique… y justifique…» son tres acciones distintas en un orden. Si resolvés bien pero no justificás, la respuesta queda incompleta aunque el número esté bien.",
                },
                {
                    "title": "Hojas de datos y normas técnicas",
                    "detail": "Un ingeniero hace una prelectura de títulos, tablas y gráficos de una hoja de datos antes de leer el detalle: así sabe dónde está la información que necesita.",
                },
                {
                    "title": "Repasar un apunte de cátedra",
                    "detail": "Con notas marginales bien puestas, encontrar «dónde explicaba la ley de Ohm» lleva segundos en lugar de releer veinte páginas la noche anterior al examen.",
                },
            ],
            "key_rule": "Primero el verbo, después el contenido | Prelectura → lectura crítica → poslectura | Subrayá en la segunda lectura, poco y lo esencial | Tema = frase; idea principal = oración que dice algo del tema.",
            "pitfall": "Contestar lo que uno sabe del tema en lugar de lo que pide el verbo (definir cuando piden explicar, describir cada cosa por separado cuando piden comparar), o subrayar casi todo el párrafo en la primera lectura.",
        },
        "example": {
            "title": "Analizar una consigna con varios verbos",
            "steps": [
                "Consigna: «Determine el dominio de f(x) = √(x − 2), represéntelo en la recta numérica y justifique por qué el 1 no pertenece a él».",
                "**Verbos**: determine, represéntelo, justifique. Son tres acciones y la respuesta tiene que tener tres partes.",
                "**Contenidos**: dominio de una función, raíz cuadrada, intervalos en la recta numérica.",
                "**Orden y jerarquía**: representar y justificar dependen del dominio, así que primero se determina: x − 2 ≥ 0, o sea Dom f = [2; +∞).",
                "Se representa [2; +∞) con punto lleno en 2, y se **justifica** con una razón, no repitiendo el resultado: f(1) = √(−1), que no es un número real.",
                "Control final: ¿respondí a cada verbo? Tres verbos, tres respuestas.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Empezás a leer un apunte nuevo. En esa primera lectura, ¿qué conviene hacer?",
            "options": [
                {"text": "Leer rápido para captar la idea general y marcar las palabras desconocidas", "ok": True, "feedback": "Exacto: es la prelectura. Subrayar y organizar vienen después, cuando ya sabés qué es lo esencial."},
                {"text": "Subrayar las ideas principales de cada párrafo", "ok": False, "feedback": "Todavía no tenés una idea general del tema, así que no sabés qué es esencial: el cuadernillo recomienda no subrayar en la primera lectura."},
                {"text": "Armar el mapa conceptual del tema", "ok": False, "feedback": "El mapa conceptual es una tarea de poslectura: se arma cuando el texto ya está comprendido."},
            ],
        },
        "checks": [
            {
                "question": "La consigna dice «Ejemplifique el principio de acción y reacción». ¿Qué se pide?",
                "options": [
                    {"text": "Enunciar el principio de forma breve y clara", "ok": False, "feedback": "Eso pide el verbo enunciar. Ejemplificar es otra acción."},
                    {"text": "Explicar por qué se cumple el principio", "ok": False, "feedback": "Eso sería explicar (causas y relaciones). La consigna no pide el porqué."},
                    {"text": "Dar situaciones concretas en las que se vea el principio", "ok": True, "feedback": "Exacto: ejemplificar es encontrar casos concretos (un remo empujando el agua, un rifle que retrocede) que reflejen la idea general."},
                ],
            },
            {
                "question": "¿Cuál de estas formulaciones es el **tema** de un texto (y no una idea)?",
                "options": [
                    {"text": "La contaminación del agua subterránea", "ok": True, "feedback": "Exacto: es una frase que nombra de qué trata el texto, sin afirmar nada."},
                    {"text": "El agua subterránea se contamina por el uso de fertilizantes", "ok": False, "feedback": "Es una oración que afirma algo sobre el tema: sería una idea (principal o central), no el tema."},
                    {"text": "Por ejemplo, en algunos pozos se midieron nitratos", "ok": False, "feedback": "Es un ejemplo que amplía otra idea: una idea secundaria."},
                ],
            },
        ],
        "takeaway_prompt": "Elegí una consigna de un práctico de Matemática o Física, marcá sus verbos y escribí con tus palabras qué pide cada uno y en qué orden los harías.",
    },
    "cl-texto-cientifico": {
        "hook": {
            "question": "En el examen te dan un texto sobre genética y preguntan qué «se puede colegir». Las cinco opciones parecen salidas del texto. ¿Cómo elegís?",
            "intuition": "Cada tipo de pregunta tiene su trampa típica: en «idea principal», un dato verdadero pero secundario; en «se infiere», una frase copiada o una exageración; en «incompatible», algo que el texto simplemente no menciona. Si reconocés el **tipo** de pregunta, sabés qué buscar y qué descartar.",
        },
        "concept": {
            "points": [
                "**Método general**: leé el texto completo antes de las opciones (prelectura), ubicá el tema y, para cada opción, buscá la **línea del texto** que la sostiene o la contradice. Las preguntas se responden según lo que dice el texto, no según lo que vos sabés del tema.",
                "**Tipos de pregunta y estrategia**:\n| Tipo | Qué buscar | Trampa típica |\n|---|---|---|\n| Tema central / mejor título | Lo que abarca TODO el texto | Un detalle, o algo más amplio que el texto |\n| Idea principal | La oración con lo esencial sobre el tema | Un dato, cifra o ejemplo (idea secundaria) |\n| Sentido contextual | El sinónimo que encaja en ESA oración | El significado más común de la palabra |\n| Incompatible / incongruente | La opción que contradice al texto | Algo que el texto no menciona |\n| Se infiere / se puede colegir | Lo que se deduce sin estar escrito | Una copia literal o una exageración |\n| Si…, probablemente… | La consecuencia que sigue la lógica del texto | Consecuencias ajenas o extremas |\n| Dos textos | El tema que tratan ambos | El enfoque de uno solo |\n| Intención de un recurso | Para qué sirve la cita, la cursiva o el ejemplo | Describir el recurso en vez de su función |",
                "**Inferir no es copiar ni inventar.** Colegir = inferir = deducir: la respuesta no está escrita tal cual, pero se sigue de lo que el texto dice. Y «no se infiere» no es lo mismo que «incompatible»: algo puede no deducirse del texto sin contradecirlo.",
                "**Sentido contextual**: reemplazá la palabra por cada opción y releé la oración. Una palabra cambia de sentido según el contexto: «ingenio» puede ser talento o un artefacto («ingenios militares»); «regular» puede ser controlar o mediocre.",
                "**Vocabulario culto frecuente** en estos textos:\n| Palabra | Significado |\n|---|---|\n| Colegir | Inferir, deducir |\n| Ingente | Enorme, muy grande |\n| Acuciante | Apremiante, urgente |\n| Inmanente | Inherente, propio de la esencia de algo (≠ inminente, ≠ trascendente) |\n| Irrecusable | Que no se puede rechazar ni poner en duda |\n| Mirífico | Admirable, maravilloso |\n| Soslayar / insoslayable | Eludir / inevitable |\n| Inusitado | Insólito, poco habitual |\n| Aseverar | Afirmar |\n| Impugnar | Combatir, refutar |\n| Subsumir | Incluir algo en un conjunto más amplio |\n| Menester | Necesario («es menester») |\n| Connotar | Sugerir un sentido además del literal |",
            ],
            "real_world": [
                {
                    "title": "Leer un artículo científico o técnico",
                    "detail": "Separar lo que el autor demostró de lo que vos inferís es la base para citar bien un trabajo en un informe de laboratorio.",
                },
                {
                    "title": "Noticias de ciencia",
                    "detail": "«Un estudio en ratones» convertido en «la cura definitiva» es una extrapolación indebida: la misma trampa que la opción exagerada de una pregunta «si…, probablemente…».",
                },
                {
                    "title": "Pliegos de licitación y contratos de obra",
                    "detail": "Una oferta incompatible con una cláusula del pliego se rechaza: lo que cuenta es la letra exacta del texto, no lo que «se entiende» que quiso decir.",
                },
            ],
            "key_rule": "Identificá el tipo de pregunta | Cada opción correcta tiene una línea del texto que la sostiene | Inferir ≠ copiar | Incompatible = contradice, no «no se menciona» | Sentido contextual: probá el sinónimo en la oración.",
            "pitfall": "Elegir una opción porque es verdadera o porque aparece literal en el texto, aunque no responda a lo que pregunta: en «idea principal» casi siempre hay una opción con un dato textual que es solo una idea secundaria.",
        },
        "example": {
            "title": "Cuatro tipos de pregunta sobre un mismo párrafo",
            "steps": [
                "Texto: «Las ondas gravitacionales fueron predichas por Einstein en 1916, pero él mismo dudaba de que algún día pudieran medirse: la energía que transportan es ingente, pero la deformación que producen al llegar a la Tierra cambia la longitud de los brazos de un detector unas mil veces menos que el diámetro de un protón. Recién en 2015 los detectores LIGO, con brazos de cuatro kilómetros, registraron la señal de dos agujeros negros que se fusionaron a más de mil millones de años luz. El hallazgo abrió una forma nueva de observar el universo: ya no solo con luz, sino también \"escuchando\" cómo vibra el espacio-tiempo.»",
                "**Tema central**: la detección de las ondas gravitacionales. «Einstein» o «los detectores LIGO» son partes del texto, no su tema.",
                "**Idea principal**: «Las ondas gravitacionales, predichas en 1916 y muy difíciles de medir, se detectaron en 2015 y abrieron una nueva forma de observar el universo». «Los brazos miden cuatro kilómetros» es un dato secundario.",
                "**Sentido contextual de INGENTE**: enorme. Probalo en la oración: «la energía que transportan es enorme, pero la deformación es minúscula»; el «pero» marca el contraste y lo confirma.",
                "**Incompatible**: «Einstein estaba seguro de que se medirían pronto» (el texto dice que dudaba). **Se infiere**: «medir deformaciones tan pequeñas exigió instrumentos de enorme precisión»: no está escrito, pero se deduce.",
                "**Intención del recurso**: las comillas en \"escuchando\" marcan un uso figurado; las ondas gravitacionales no son sonido.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Un autor escribe: «Galileo afirmó que el libro de la naturaleza está escrito en lenguaje matemático» y a continuación explica cómo se modela una caída libre. ¿Con qué intención incluye la cita?",
            "options": [
                {"text": "Respaldar con una voz autorizada la idea de que la naturaleza se describe con matemática", "ok": True, "feedback": "Exacto: la cita es un argumento de autoridad que prepara lo que sigue, el modelo matemático de la caída."},
                {"text": "Narrar la biografía de Galileo", "ok": False, "feedback": "El texto no sigue hablando de Galileo: la cita sirve a la explicación, no la reemplaza."},
                {"text": "Refutar la opinión de Galileo", "ok": False, "feedback": "El autor usa la cita a favor de lo que va a explicar, no en contra."},
            ],
        },
        "checks": [
            {
                "question": "En una pregunta de «incompatibilidad», una opción afirma algo que el texto no menciona ni contradice. ¿Es la respuesta?",
                "options": [
                    {"text": "Sí: lo que el texto no menciona es incompatible con él", "ok": False, "feedback": "Incompatible significa que no pueden ser verdaderas a la vez: algo no mencionado no choca con el texto."},
                    {"text": "No: incompatible es lo que contradice lo que el texto afirma", "ok": True, "feedback": "Exacto: buscá la opción que choca con una oración concreta del texto."},
                    {"text": "Sí, si la opción es falsa en la realidad", "ok": False, "feedback": "Las preguntas se juzgan contra el texto, no contra lo que vos sabés del tema."},
                ],
            },
            {
                "question": "Un texto explica cómo los murciélagos emiten ultrasonidos, cómo calculan la distancia por el eco y cómo los ingenieros copiaron ese principio en el sonar. ¿Qué título expresa mejor la idea central?",
                "options": [
                    {"text": "Los murciélagos", "ok": False, "feedback": "Es demasiado amplio: no dice qué aspecto de los murciélagos trata, y deja afuera el sonar."},
                    {"text": "El sonar de los submarinos", "ok": False, "feedback": "Toma solo la última parte del texto."},
                    {"text": "Ecos que guían: del murciélago al sonar", "ok": True, "feedback": "Exacto: abarca las dos partes del texto, la ecolocalización y su imitación técnica."},
                ],
            },
        ],
        "takeaway_prompt": "Elegí una nota corta de divulgación científica y escribí para ella una pregunta de cada tipo (tema central, sentido contextual, incompatibilidad e inferencia), con la respuesta correcta y un distractor que caiga en la trampa típica.",
    },
    "cl-organizadores": {
        "hook": {
            "question": "Tenés que estudiar 30 páginas de un apunte para el lunes. ¿Las releés tres veces o las transformás en otra cosa?",
            "intuition": "Releer da sensación de dominio, pero se olvida rápido. **Transformar** el texto —reducirlo a un resumen, reescribirlo en una síntesis o dibujarlo como cuadro o mapa— obliga a decidir qué es importante y cómo se relaciona: eso es comprender. El cuadernillo divide estas técnicas en **redactadas** y **no redactadas**.",
        },
        "concept": {
            "points": [
                "**Técnicas redactadas**:\n| | Resumen | Síntesis |\n|---|---|---|\n| Vocabulario | El del autor (y el técnico de la materia) | Propio |\n| Orden de las ideas | El del texto original | Reelaborado |\n| Qué es | Lo esencial del texto, breve y objetivo | Un mensaje nuevo, con relaciones con lo que ya sabías |",
                "**Cómo resumir**: primera lectura para la unidad temática; segunda para la organización interna; diccionario si hace falta; subrayar las ideas principales (puede haber párrafos de transición sin ninguna); redactar un texto nuevo uniendo las ideas con conectores (por lo tanto, entonces, porque, pero). Si no te fijan extensión, apuntá a **un 25 %** del original. Se omiten ejemplos, reformulaciones y repeticiones; el resultado tiene que ser **autónomo** (entendible sin el original).",
                "**Esquema de contenidos**: las ideas principales son los encabezados; las de igual jerarquía van al mismo nivel, con la misma forma gramatical y numeración del mismo tipo (I, II…; 1.1, 1.2…; a, b…). **Cuadro sinóptico**: un esquema con **llaves**, con el título a la izquierda y las subdivisiones hacia la derecha; ideal para temas con muchas clasificaciones (su desventaja: la letra se aprieta a la derecha).",
                "**Cuadro comparativo**: una tabla con los **elementos** a comparar en la primera fila (columnas) y los **criterios** o variables de análisis en la primera columna (filas). Todos los elementos se comparan con los mismos criterios: nada de «esta hoja es verde, mientras que aquella es pequeña».",
                "**Mapa conceptual** (basado en las ideas de Ausubel): **conceptos** dentro de figuras (palabras clave, no oraciones, sin repetirlos), unidos por líneas con **palabras de enlace**; concepto + enlace + concepto forma una **proposición** con sentido. Los conceptos más generales van arriba y los específicos y ejemplos, abajo; las **conexiones cruzadas** unen ramas distintas.",
                "**Cuándo conviene cada uno**:\n| Si el contenido… | Conviene… |\n|---|---|\n| hay que reducirlo respetando al autor | Resumen |\n| hay que reelaborarlo y relacionarlo | Síntesis |\n| tiene clasificaciones y subdivisiones | Esquema o cuadro sinóptico |\n| compara entidades según criterios | Cuadro comparativo |\n| relaciona muchos conceptos entre sí | Mapa conceptual |",
            ],
            "real_world": [
                {
                    "title": "Elegir un material en un proyecto",
                    "detail": "Acero, aluminio y PVC comparados según densidad, costo y resistencia a la corrosión: un cuadro comparativo es la forma estándar de justificar la elección en un informe.",
                },
                {
                    "title": "El resumen de un informe técnico",
                    "detail": "El «resumen ejecutivo» o abstract de un informe cumple las reglas del resumen: breve, autónomo, con las ideas principales en el orden del trabajo. Con él, quien decide sabe si leer el resto.",
                },
                {
                    "title": "Estudiar Química del ingreso",
                    "detail": "La clasificación de la materia (sustancias puras y mezclas, elementos y compuestos, mezclas homogéneas y heterogéneas) entra en un cuadro sinóptico de una sola hoja.",
                },
            ],
            "key_rule": "Resumen ≈ 25 %, con palabras y orden del autor | Síntesis = palabras propias | Clasificaciones → cuadro sinóptico | Elementos × criterios → cuadro comparativo | Relaciones entre conceptos → mapa conceptual con palabras de enlace.",
            "pitfall": "Llamar resumen a copiar lo subrayado tal cual, o armar un «mapa conceptual» con oraciones largas en los recuadros y líneas sin palabras de enlace: así no se lee ninguna relación.",
        },
        "example": {
            "title": "Pasar un párrafo sobre los estados de la materia a tres organizadores",
            "steps": [
                "Texto: «La materia se presenta habitualmente en tres estados: sólido, líquido y gaseoso. Los sólidos tienen forma y volumen propios; los líquidos tienen volumen propio, pero adoptan la forma del recipiente; los gases no tienen forma ni volumen propios y ocupan todo el recipiente que los contiene».",
                "**Subrayado**: tres estados (sólido, líquido, gaseoso) y dos criterios que se repiten: forma propia y volumen propio.",
                "**Resumen** (palabras del autor): «La materia se presenta en estado sólido, con forma y volumen propios; líquido, con volumen propio y la forma del recipiente; y gaseoso, sin forma ni volumen propios».",
                "**Cuadro comparativo** (estados en columnas, criterios en filas):\n| Criterio | Sólido | Líquido | Gaseoso |\n|---|---|---|---|\n| Forma propia | Sí | No | No |\n| Volumen propio | Sí | Sí | No |",
                "**Mapa conceptual**: [Materia] —se presenta en→ [estados] —que son→ [sólido], [líquido] y [gaseoso]; [sólido] —tiene→ [forma y volumen propios]; [líquido] —tiene→ [volumen propio]…",
                "**Elección**: el texto compara tres entidades con los mismos dos criterios, así que el cuadro comparativo es el más claro y el más rápido de repasar.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Un texto clasifica los triángulos según sus lados (equiláteros, isósceles, escalenos) y según sus ángulos (acutángulos, rectángulos, obtusángulos). ¿Qué organizador conviene?",
            "options": [
                {"text": "Un cuadro sinóptico", "ok": True, "feedback": "Exacto: es un tema de clasificaciones con subdivisiones, justo lo que muestran las llaves de un cuadro sinóptico."},
                {"text": "Una síntesis", "ok": False, "feedback": "Es una técnica redactada: no muestra de un vistazo cómo se divide el tema."},
                {"text": "Un cuadro comparativo", "ok": False, "feedback": "Sirve para comparar entidades con los mismos criterios, no para mostrar clasificaciones y subclasificaciones."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál de estas características corresponde a un buen resumen?",
                "options": [
                    {"text": "Incluye los ejemplos del autor para que se entienda mejor", "ok": False, "feedback": "Los ejemplos son información secundaria: en el resumen se omiten."},
                    {"text": "Reemplaza el vocabulario técnico por palabras más simples", "ok": False, "feedback": "El vocabulario técnico o específico de la asignatura se respeta. Usar palabras propias es lo que hace la síntesis."},
                    {"text": "Se entiende sin haber leído el texto original", "ok": True, "feedback": "Exacto: un resumen es un texto autónomo que reproduce la organización del original y puede sustituirlo."},
                ],
            },
            {
                "question": "En un mapa conceptual sobre la energía, ¿dónde va el concepto «Energía»?",
                "options": [
                    {"text": "Arriba, porque es el más general", "ok": True, "feedback": "Exacto: los conceptos más generales e inclusivos ocupan la parte superior; abajo van los específicos (cinética, potencial) y los ejemplos."},
                    {"text": "Abajo, como conclusión del mapa", "ok": False, "feedback": "El mapa se jerarquiza de lo general (arriba) a lo específico (abajo), no termina en una conclusión."},
                    {"text": "Sobre una de las líneas, como palabra de enlace", "ok": False, "feedback": "Las líneas llevan palabras de enlace (verbos, preposiciones); «Energía» es un concepto y va dentro de una figura."},
                ],
            },
        ],
        "takeaway_prompt": "Tomá un tema de Física o Química que estés estudiando, decidí si te conviene un cuadro sinóptico, un cuadro comparativo o un mapa conceptual, justificá la elección y armalo.",
    },
    "cl-lenguaje-simbolico": {
        "hook": {
            "question": "«El doble de un número más tres»: ¿es `2x + 3` o `2.(x + 3)`? Con x = 5 da 13 o 16.",
            "intuition": "El lenguaje coloquial puede ser ambiguo; el simbólico no. Leída de corrido, la frase significa `2x + 3`; para decir lo otro se dice «el doble de **la suma** de un número y tres». Traducir bien es decidir **qué operación se hace al final**: en palabras lo marca el orden de la frase y en símbolos, los paréntesis.",
        },
        "concept": {
            "points": [
                "**Vocabulario básico** (x es un número cualquiera y n ∈ Z):\n| Coloquial | Simbólico |\n|---|---|\n| doble o duplo / triple o triplo / cuádruplo | 2x / 3x / 4x |\n| mitad / tercera parte / cuarta parte | x/2 / x/3 / x/4 |\n| cuadrado / cubo | x² / x³ |\n| consecutivo (siguiente) / anterior | x + 1 / x − 1 |\n| número par / impar | 2n / 2n + 1 |\n| pares consecutivos | 2n, 2n + 2, 2n + 4 |\n| impares consecutivos | 2n + 1, 2n + 3, 2n + 5 |",
                "**Operaciones y relaciones**: «x aumentado en 3» es x + 3; «disminuido en 3», x − 3; «la diferencia entre a y b», a − b (en ese orden); «a excede a b en c», a − b = c; «el producto de a y b», a.b; «el cociente entre a y b», a/b; «la razón entre a y b», a/b (por ejemplo, «la razón entre a y b es 3/4» es a/b = 3/4).",
                "**La primera operación que se nombra es la última que se hace.** «El doble de la suma de x e y» → 2.(x + y); «la suma del doble de x e y» → 2x + y; «el cuadrado de la suma» → (a + b)²; «la suma de los cuadrados» → a² + b². No son iguales: (a + b)² = a² + 2ab + b².",
                "**Notación de conjuntos**: ∈ «pertenece a», ∉ «no pertenece a»; IN (naturales, sin el 0), IN₀ (con el 0), Z, Q, IR (en otras partes de la app aparecen como ℕ, ℤ, ℚ, ℝ). La barra «/» se lee «tal que»: A = { x ∈ IN / x < 6 } es la definición **por comprensión** (por una propiedad) y A = {1, 2, 3, 4, 5}, **por extensión** (listando los elementos).",
                "**Cuantificadores**: ∀ «para todo» y ∃ «existe (al menos un)». ∀ x ∈ IR: x + 0 = x se lee «para todo real x, x más cero es igual a x»; ∃ x ∈ Z / x² = 4 se lee «existe un entero x tal que su cuadrado es 4».",
                "**Leer una expresión en palabras**: empezá por la operación principal (la última que se hace). (a + b)/2 es «la mitad de la suma de a y b»; a + b/2 es «a más la mitad de b»; 3.(x − 1)² es «el triple del cuadrado del anterior de x».",
            ],
            "real_world": [
                {
                    "title": "Planilla de cálculo",
                    "detail": "=2*(A1+B1) y =2*A1+B1 dan resultados distintos: la planilla hace exactamente lo que dicen los paréntesis, no lo que quisiste decir.",
                },
                {
                    "title": "Programación",
                    "detail": "Recorrer una lista para verificar que todos sus elementos cumplen una condición es un ∀; buscar si alguno la cumple es un ∃. Muchos lenguajes tienen funciones con esos nombres (all, any).",
                },
                {
                    "title": "Enunciados de Física",
                    "detail": "«La velocidad final excede en 5 m/s a la inicial» se traduce v_f − v_i = 5 m/s; «la masa de A es el triple de la de B», m_A = 3.m_B. Una traducción mal hecha arruina un planteo bien pensado.",
                },
            ],
            "key_rule": "La primera palabra es la operación principal | «el doble de la suma…» → paréntesis | a excede a b en c → a − b = c | consecutivo: x + 1 | pares consecutivos: 2n, 2n + 2 | «/» = tal que | ∀ = para todo, ∃ = existe.",
            "pitfall": "Olvidar los paréntesis: escribir 2x + 5 por «el doble de la suma de x y 5», o x/x + 1 por «el cociente entre x y su consecutivo». Y creer que (a + b)² = a² + b².",
        },
        "example": {
            "title": "Traducir y resolver: el doble más la tercera parte",
            "steps": [
                "Enunciado: «Si al doble de un número le sumo su tercera parte, obtengo el número aumentado en 20. ¿Cuál es el número?». Incógnita: x = el número.",
                "Traducción por partes: «el doble de un número» → 2x; «le sumo su tercera parte» → + x/3; «obtengo» → =; «el número aumentado en 20» → x + 20.",
                "Ecuación: 2x + x/3 = x + 20.",
                "Multiplicamos todo por 3: 6x + x = 3x + 60, o sea 7x − 3x = 60, de donde 4x = 60 y x = 15.",
                "Verificación en el enunciado original: 2 . 15 + 15/3 = 30 + 5 = 35 y 15 + 20 = 35. S = {15}.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "¿Cómo se lee `(a + b)/2`?",
            "options": [
                {"text": "La suma de a y la mitad de b", "ok": False, "feedback": "Eso es a + b/2: sin paréntesis, solo b se divide por 2."},
                {"text": "La mitad de la suma de a y b", "ok": True, "feedback": "Exacto: la operación principal es dividir por 2, y se aplica a toda la suma."},
                {"text": "El doble de la suma de a y b", "ok": False, "feedback": "El doble sería 2.(a + b): multiplicar, no dividir."},
            ],
        },
        "checks": [
            {
                "question": "Con n ∈ Z, dos números impares consecutivos se escriben:",
                "options": [
                    {"text": "2n + 1 y 2n + 3", "ok": True, "feedback": "Exacto: 2n + 1 es impar para cualquier entero n, y el impar siguiente está 2 unidades más adelante."},
                    {"text": "2n + 1 y 2n + 2", "ok": False, "feedback": "2n + 2 = 2.(n + 1) es par: esos son dos números consecutivos cualesquiera."},
                    {"text": "n y n + 2", "ok": False, "feedback": "Si n es par, los dos son pares: la expresión no garantiza que sean impares."},
                ],
            },
            {
                "question": "Con la convención del ingreso (IN sin el 0), la proposición `∃ x ∈ IN / x < 1` es:",
                "options": [
                    {"text": "Verdadera, porque 0 < 1", "ok": False, "feedback": "En el ingreso 0 ∉ IN (el conjunto que lo incluye es IN₀). En IN₀ sí sería verdadera."},
                    {"text": "Falsa, porque el menor natural es 1", "ok": True, "feedback": "Exacto: no hay ningún natural menor que 1, así que no existe el x que pide el enunciado."},
                    {"text": "No tiene valor de verdad, porque tiene una variable", "ok": False, "feedback": "La variable está cuantificada por ∃: el enunciado completo es verdadero o falso."},
                ],
            },
        ],
        "takeaway_prompt": "Inventá una frase coloquial que se traduzca como `2.(x + 3)` y otra que se traduzca como `2x + 3`, y explicá qué palabras marcan la diferencia.",
    },
    "cl-logica-enunciados": {
        "hook": {
            "question": "Teorema: «Si un número es divisible por 4, entonces es par». ¿Eso dice también que todo número par es divisible por 4?",
            "intuition": "No: 6 es par y no es divisible por 4. Un teorema afirma una implicación **en un solo sentido**. Leer un teorema es separar la **hipótesis** (lo que se supone) de la **tesis** (lo que se garantiza) y saber qué otras frases dicen lo mismo y cuáles no.",
        },
        "concept": {
            "points": [
                "**Proposición**: enunciado declarativo que es verdadero (V) o falso (F), y no ambas cosas. No son proposiciones las preguntas, las órdenes ni las formas abiertas como x + 3 = 5, que dependen de x: se vuelven proposiciones al darle un valor a x o al cuantificarla (∀, ∃).",
                "**Negación** ~p (también se escribe ¬p): tiene el valor opuesto a p. Con cuantificadores: la negación de «∀ x: P(x)» es «∃ x / no P(x)» (no todos = al menos uno no) y la de «∃ x / P(x)» es «∀ x: no P(x)» (no existe ninguno = todos no). La negación de «todos son impares» no es «todos son pares» ni «ninguno es impar». Y la negación de «>» es «≤».",
                "**Conectivos y tablas de verdad**: ∧ «y» (V solo si las dos son V); ∨ «o» inclusivo (F solo si las dos son F); ⇒ «si…, entonces…» (F solo si p es V y q es F); ⇔ «si y solo si» (V cuando tienen el mismo valor).\n| p | q | p ∧ q | p ∨ q | p ⇒ q | p ⇔ q |\n|---|---|---|---|---|---|\n| V | V | V | V | V | V |\n| V | F | F | V | F | F |\n| F | V | F | V | V | F |\n| F | F | F | F | V | V |",
                "**Teorema** «si H, entonces T» (H ⇒ T): la **hipótesis** H es el antecedente, lo que se supone; la **tesis** T es el consecuente, lo que se demuestra. A veces no aparece el «si…, entonces…»: «Los ángulos opuestos por el vértice son iguales» tiene H: dos ángulos son opuestos por el vértice; T: son iguales.",
                "**Formas asociadas** a p ⇒ q: **recíproco** q ⇒ p; **contrario** ~p ⇒ ~q; **contrarrecíproco** ~q ⇒ ~p. Solo el contrarrecíproco es **equivalente** al original (siempre tiene su mismo valor de verdad); el recíproco y el contrario son equivalentes entre sí, pero no al original. Si el teorema y su recíproco son ambos verdaderos, vale p ⇔ q.",
                "**Condiciones y contraejemplos**: en p ⇒ q verdadero, p es condición **suficiente** para q y q es condición **necesaria** para p; con ⇔, cada una es necesaria y suficiente para la otra. Para refutar un «para todo» alcanza un **contraejemplo**: un caso que cumple la hipótesis y no la tesis. Muchos ejemplos a favor no demuestran un «para todo».",
            ],
            "real_world": [
                {
                    "title": "Programación",
                    "detail": "Las condiciones de un if usan and, or y not con estas mismas tablas. Negar «a and b» da «(not a) or (not b)»: el mismo cuidado que al negar un «todos».",
                },
                {
                    "title": "Diagnóstico de fallas",
                    "detail": "«Si el fusible está quemado, la lámpara no enciende.» Que la lámpara no encienda no prueba que el fusible esté quemado (eso es el recíproco); que encienda sí prueba que no lo está (contrarrecíproco).",
                },
                {
                    "title": "Normas técnicas",
                    "detail": "«Si una viga supera la flecha admisible, se rechaza» no dice que toda viga que no la supere se acepte (ese es el contrario): puede rechazarse por otras causas.",
                },
            ],
            "key_rule": "p ⇒ q es F solo si p es V y q es F | Equivalente: contrarrecíproco ~q ⇒ ~p | Negación de «todos» = «existe uno que no» | Hipótesis = suficiente; tesis = necesaria | Un contraejemplo refuta un «para todo».",
            "pitfall": "Usar el recíproco como si fuera el mismo teorema («si es par, es divisible por 4»), negar «todos son X» con «ninguno es X» y creer que muchos ejemplos a favor demuestran una afirmación general.",
        },
        "example": {
            "title": "Analizar el teorema «si n es divisible por 4, entonces n es par» (n ∈ IN)",
            "steps": [
                "**Hipótesis**: n es divisible por 4 (p). **Tesis**: n es par (q). Forma: p ⇒ q.",
                "**Valor**: verdadero. Si n = 4k con k ∈ IN, entonces n = 2.(2k), que es par.",
                "**Recíproco** (q ⇒ p): «si n es par, es divisible por 4». Falso: contraejemplo n = 6. **Contrario** (~p ⇒ ~q): «si n no es divisible por 4, no es par». Falso con el mismo n = 6.",
                "**Contrarrecíproco** (~q ⇒ ~p): «si n no es par, no es divisible por 4». Verdadero, como el teorema: son equivalentes.",
                "**Condiciones**: ser divisible por 4 es suficiente para ser par; ser par es necesario para ser divisible por 4, pero no suficiente.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Si `p ⇔ q` es verdadera, ¿qué podés asegurar?",
            "options": [
                {"text": "Que p y q son ambas verdaderas", "ok": False, "feedback": "No necesariamente: si p y q son ambas falsas, p ⇔ q también es verdadera."},
                {"text": "Que p y q tienen el mismo valor de verdad", "ok": True, "feedback": "Exacto: el bicondicional es V cuando las dos son V o las dos son F."},
                {"text": "Que p es verdadera y q puede ser cualquier cosa", "ok": False, "feedback": "Si p es V y q es F, el bicondicional es F: q tiene que acompañar a p."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál es el valor de verdad de «Si 2 + 2 = 5, entonces la Luna es cuadrada»?",
                "options": [
                    {"text": "Verdadero", "ok": True, "feedback": "Exacto: el antecedente es falso, y un condicional con antecedente falso es verdadero, sea cual sea el consecuente."},
                    {"text": "Falso, porque la conclusión es absurda", "ok": False, "feedback": "El condicional solo es falso con antecedente V y consecuente F. Acá el antecedente es F."},
                    {"text": "No es una proposición", "ok": False, "feedback": "Es una proposición compuesta: sus dos partes tienen valor de verdad, así que ella también."},
                ],
            },
            {
                "question": "Comprobaste que n² + n + 41 es primo para n = 1, 2, 3, …, 39. ¿Demostraste que es primo para todo n ∈ IN?",
                "options": [
                    {"text": "Sí: 39 casos seguidos son suficientes", "ok": False, "feedback": "Ninguna cantidad de ejemplos demuestra un «para todo». De hecho, con n = 40 da 1681 = 41², que no es primo."},
                    {"text": "Sí, porque los casos probados incluyen números grandes", "ok": False, "feedback": "El tamaño de los ejemplos no cambia nada: n = 40 es un contraejemplo (40² + 40 + 41 = 1681 = 41.41)."},
                    {"text": "No: hace falta una demostración general, y un solo contraejemplo alcanza para refutarlo", "ok": True, "feedback": "Exacto: y existe uno, n = 40, donde da 1681 = 41²."},
                ],
            },
        ],
        "takeaway_prompt": "Escribí un teorema de Geometría que conozcas con la forma «si…, entonces…», marcá la hipótesis y la tesis, y escribí su recíproco y su contrarrecíproco indicando cuál es verdadero.",
    },
}
