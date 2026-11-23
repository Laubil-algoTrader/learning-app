"""Borrador: ejercicios de Comprensión Lectora del ingreso (CLyRP, UNCuyo).

Fuentes:
- «Comprensión Lectora 2023 - Práctica» (Trabajo Práctico Nº 1): textos con preguntas de opción múltiple,
  preguntas de idea principal y consignas abiertas (notación marginal, síntesis, cuadros).
- «Resolución de Problemas - Comprensión lectora 1» (Ingreso LCC): actividades C (opción múltiple) y D (V/F/NM).

El material no trae clave oficial. Las claves de los textos 1 y 2 de «Comprensión lectora» salen de la copia
corregida a mano del usuario; el resto se determinó releyendo cada pasaje y descartando cada distractor con
una razón textual (está en la resolución de cada problema). Cuando una pregunta tenía 5 opciones se dejaron la
correcta y 3 distractores (el formato admite 3 o 4).
"""

from __future__ import annotations

TC = "cl-texto-cientifico"
CO = "cl-consignas-lectura"
OR = "cl-organizadores"


def _q(prompt: str, options: list[str], correct: int) -> dict:
    return {
        "prompt": prompt,
        "check": {"type": "choice", "options": options, "correct": correct},
        "answer": options[correct],
    }


def _p(node, suffix, level, source, title, statement, parts, hints, solution) -> dict:
    return {
        "id": f"{node}-{suffix}",
        "node": node,
        "kind": "problem",
        "level": level,
        "source": source,
        "title": title,
        "statement": statement,
        "parts": parts,
        "hints": hints,
        "solution": solution,
    }


def _enc(n: int, rango: str, texto: str) -> str:
    return (
        f"Leé el texto y marcá la respuesta correcta de cada pregunta (en este problema van las preguntas {rango} "
        f"del texto {n}; las demás están en los otros problemas del mismo texto).\n\n**Texto {n}**\n\n{texto}"
    )


VOCAB = "En las preguntas de vocabulario, reemplazá la palabra por cada opción dentro de la oración del texto y quedate con la que conserva el sentido."
INCOMP = "En las preguntas de «incompatible» o «incongruente» buscás la única opción que el texto contradice: las otras están dichas o se deducen de él."
HIPO = "En las preguntas «Si…, probablemente…», aplicá la regla o la idea central del texto al caso nuevo; descartá las opciones que agregan datos que el texto no da o que exageran."

# ---------------------------------------------------------------------------------------------------------
# Textos de «Comprensión lectora» (práctica)
# ---------------------------------------------------------------------------------------------------------

T1 = "\n\n".join([
    "¿Revisas tu smartphone cada cinco minutos? ¿Has sentido vibraciones fantasmas? ¿Te llevas tu celular a la mesa e incluso hasta al baño? Si es así, seguramente perteneces a los millones de personas que padecen «nomofobia».",
    "El término surgió como abreviatura de no-mobile-phone-phobia durante un estudio realizado por la empresa inglesa de investigación demoscópica You Gov, para señalar la ansiedad y angustia que produce el estar sin celular.",
    "Si bien la denominación «fobia» podría ser incorrecta, un estudio conducido por el psicólogo Richard Balding de la Universidad de Worcester en Reino Unido, reveló que, efectivamente, el uso constante de estos aparatos aumenta los niveles de estrés, lo que a su vez incrementa los comportamientos compulsivos como el buscar incesantemente nuevas alertas, mensajes y actualizaciones.",
    "Durante el experimento, se les aplicó un cuestionario y una prueba psicosomática de estrés a 100 participantes, entre ellos estudiantes universitarios y empleados de diversas categorías y ocupaciones. Se confirmó la existencia de un círculo vicioso: si bien las personas adquirían el smartphone para manejar su carga de trabajo, una vez que el aparato extendía virtualmente su vida social, la angustia y el estrés se disparaban.",
    "La inhabilidad de apagar el celular, el tenerlo siempre a la mano, el asegurarse de que nunca se acabe la batería y el miedo a perder la señal son algunos síntomas de quienes sufren altos niveles de estrés.",
    "En México, existen más de 190 millones de smartphones: el 72% de los usuarios no salen de su casa sin su celular, según un informe realizado por Google, la consultora IPSOS y Mobile Marketing Association.",
])

T2 = "\n\n".join([
    "El respeto que siente el hombre por el conocimiento es una de sus características más peculiares. En latín conocimiento se dice scientia y ciencia llegó a ser el nombre de la clase de conocimiento más respetable. ¿Qué distingue al conocimiento de la superstición, la ideología o la pseudociencia? La Iglesia Católica excomulgó a los copernicanos, el Partido Comunista persiguió a los mendelianos por entender que sus doctrinas eran pseudocientíficas. La demarcación entre ciencia y pseudociencia no es un mero problema de filosofía de salón; tiene una importancia social y política vital.",
    "Muchos filósofos han intentado solucionar el problema de la demarcación en los términos siguientes: un enunciado constituye conocimiento si cree en él, con suficiente convicción, un número suficientemente elevado de personas. Pero la historia del pensamiento muestra que muchas personas han sido convencidos creyentes de nociones absurdas. Si el vigor de la creencia fuera un distintivo del conocimiento tendríamos que considerar como parte de ese conocimiento a muchas historias sobre demonios, ángeles, diablos, cielos e infiernos. Por otra parte, los científicos son muy escépticos incluso con respecto a sus mejores teorías. La de Newton es la teoría más poderosa que la ciencia ha producido nunca, pero el mismo Newton nunca creyó que los cuerpos se atrajeran entre sí a distancia. Por tanto, ningún grado de convencimiento con relación a ciertas creencias las convierte en conocimiento. Realmente lo que caracteriza a la conducta científica es un cierto escepticismo incluso con relación a nuestras teorías más estimadas. La profesión de fe ciega en una teoría no es una virtud intelectual sino un crimen intelectual. De este modo un enunciado puede ser pseudocientífico, aunque sea eminentemente plausible y aunque todo el mundo lo crea, o puede ser científicamente valioso, aunque sea increíble y nadie crea en él. Una teoría puede tener un valor científico incluso eminente, aunque nadie la comprenda y, aún menos, crea en ella.",
    "El valor cognoscitivo de una teoría nada tiene que ver con su influencia psicológica sobre las mentes humanas. Creencias, convicciones, comprensiones... son estados de la mente humana. Pero el valor científico y objetivo de una teoría es independiente de la mente humana que la crea o la comprende. Su valor científico depende solamente del apoyo objetivo que prestan los hechos a esa conjetura.",
])

T3 = "\n\n".join([
    "Se ha demostrado que el baile es uno de los mejores antídotos contra el estrés y el mal humor. No en vano es un gran estimulante en la producción de endorfinas, las hormonas del bienestar.",
    "Bailar es una especie de meditación activa que permite alejar de la mente las preocupaciones y tensiones, otorgándole al cuerpo una libertad que habitualmente le negamos. Todos podemos conectarnos con nuestra más íntima esencia si dejamos que sea el cuerpo quien asuma su capacidad sanadora, aunque esto nada tiene que ver con los diez minutos de gimnasia que podamos practicar a diario. Las investigaciones confirman que el baile aumenta la creatividad y la autoestima. La persona se siente más relajada, receptiva y llena de energía. Entonces, al regresar del trabajo o del estudio, baile en casa. No importa el tipo de música que prefiera, porque a veces no se necesita de una canción para dejar que su cuerpo se libere a través del baile. Hablamos de la música interior, del ritmo que su cuerpo es capaz de expresar tarareando o cantando a pleno pulmón para liberar lo que siente. Todos tenemos una melodía interna que la mente reconoce como una partitura con la cual liberar los sentimientos atrapados. Quizás sea una canción entera o unas notas sueltas. No importa, solo necesita dejar que suene en su interior y que su cuerpo siga el son.",
])

T4 = "\n\n".join([
    "Lo usual es atribuir la causa de las enfermedades mentales al entorno, con algunos raros casos de origen genético. La vanguardia de la patología molecular –la ciencia que busca las causas últimas de la enfermedad humana– está derribando ese paradigma al mostrar hasta qué punto el entorno actúa a través de los genes. Científicos de Tokio sugieren hoy que los transposones, o genes saltarines que cambian de posición en el genoma, presentes en las células precursoras de las neuronas, son una causa mayor de la esquizofrenia.",
    "Los transposones generan variedad neuronal durante el desarrollo normal. Su movilidad excesiva puede deberse a causas hereditarias, pero también provocarse por el entorno, lo que puede explicar las actuales paradojas sobre la genética de las enfermedades mentales.",
    "No es que el genoma de las neuronas se vuelva loco, todo empiece a ir mal y el azar acabe causando la esquizofrenia. Los meros errores pueden ser la causa de raras enfermedades hereditarias –las monogenéticas o debidas a la mutación de un solo gen–, pero las grandes enfermedades humanas, como el cáncer o el trastorno mental, tienen unos componentes genéticos mucho más sutiles.",
    "La razón de que los transposones generen la esquizofrenia es que se insertan cerca de genes esenciales para el desarrollo y el funcionamiento del cerebro. Así no solo alteran su actividad, sino también la forma en que responden al entorno.",
    "La regulación de los genes depende precisamente de las secuencias de ADN que tienen al lado, y el transposón protagonista de este estudio, llamado L1, contiene secuencias especializadas en responder al entorno y regular a los genes vecinos. En eso se basa su función durante el desarrollo normal, y también en la génesis de la esquizofrenia.",
    "Kato y Kazuya, los científicos de Tokio, presentan una investigación del cerebro de 48 pacientes de esquizofrenia y 47 personas de control, complementada con estudios genómicos, experimentos en células madre derivadas de pacientes y comprobaciones en modelos animales como ratones y macacos. Todos los resultados apuntan a la misma conclusión: un claro incremento de los sucesos de transposición en las neuronas en el córtex cerebral prefrontal de los pacientes de esquizofrenia.",
])

T5 = "\n\n".join([
    "**Lectura A**",
    "La muerte te borra del mapa. Muerto ya no estás por ahí —por aquí en todo caso— y, si no hay ningún otro lugar donde puedas estar (Cielo, Infierno, con la luz blanca), entonces todo lo que quedará de ti son tus efectos, lo que has dejado, tus rastros. La gente parece pensar que es importante seguir estando ahí de alguna manera. El concepto raíz parece ser este: no tendría que ser nunca como si no hubieras existido jamás. Una vida significante deja su impronta en el mundo. Una vida significante es, en algún sentido, permanente; marca una diferencia permanente en el mundo: deja rastros. Ser borrado completamente, incluso los rastros, es un largo camino hacia destruir el significado de la vida de uno. Sin embargo, durar, incluso si es una condición necesaria para una vida con sentido, ciertamente no es suficiente. Tenemos que preguntarnos qué tipo de rastro es importante y por qué ese tipo no lo es cuando es muy fugaz. Por ejemplo, a veces mucha gente habla de alcanzar la inmortalidad mediante sus hijos. Es desconcertante que la gente hable de alcanzar la inmortalidad dejando descendientes, puesto que no creen que su cadena de descendientes, si bien quizás sea muy larga, vaya a ser infinita. Por consiguiente, ¿cómo producen inmortalidad los descendientes en vez de una mortalidad prolongada de alguna manera? Quizá la situación sea la siguiente: mientras que la continuación infinita es lo mejor, cualquier continuación es mejor que ninguna.",
    "Nozick, R. (1981). Philosophical Explanations. Harvard University Press, pp. 582-583. (Adaptación).",
    "**Lectura B**",
    "Una visión extendida, hoy menos que antes, es que el significado de la vida o la existencia de la gente está conectado con la voluntad divina, con su deseo o plan para ellos. Dicho claramente, el significado de la vida de las personas se encuentra y realiza en el cumplimiento de la tarea que Dios les ha asignado. Si un ente superior diseñó y creó a las personas con un fin, de acuerdo con un plan para ellos, el propósito particular que tuvo para ellos sería para lo que están las personas. Esto es distinto de la visión que encuentra el significado de la vida en la meta de fusionarse con Dios, y también de la visión que sostiene que, si haces la voluntad divina, se te recompensará –te sentarás a su derecha y recibirás dicha eterna– y que el significado de la vida, y su propósito, es alcanzar esta recompensa intrínsecamente valiosa. Lo que nos concierne aquí no es la cuestión de si existe Dios; o si, de existir, tiene un propósito para nosotros; o si hay alguna manera de descubrir su propósito: si Dios revela su propósito a las personas. Más bien, nuestra pregunta es cómo todo esto, incluso de ser cierto, conseguiría dar significado a las vidas de las personas.",
    "Nozick, R. (1981). Philosophical Explanations. Harvard University Press, pp. 585-586. (Adaptación).",
])

T6 = "\n\n".join([
    "**Lectura A**",
    "En la actualidad, se considera que existen tantas modalidades de uso de telecomunicaciones en medicina, que es casi imposible hacer un inventario. Ante eso, el Centro de Política de Salud Conectada (CCHP, por sus siglas en inglés) ha organizado cuatro modalidades de telemedicina (ellos usan el término más amplio de telesalud): videollamadas en vivo entre profesionales de la salud para educación y consulta; salud móvil, que permite videollamadas entre un profesional de la salud y un paciente mediante aplicaciones en teléfonos inteligentes; monitoreo a distancia de signos y síntomas de pacientes; y recolección y envío de datos de pacientes a distancia (radiografías, análisis, imágenes de biopsias de pacientes).",
    "Como se puede ver, todos esos usos de la telemedicina —con excepción de la salud móvil— están encaminados a ayudar en la interpretación de exámenes de diagnóstico y en la educación a distancia, lo cual lleva a preguntarse: ¿podrán los teléfonos inteligentes reemplazar la visita al médico? Ese es un punto controversial. Es posible que estas puedan resolver problemas simples, cuyo diagnóstico depende más de una buena conversación que de un examen clínico completo, pero que reemplacen a una consulta médica cara a cara es discutible. Por ejemplo, muchos padecimientos comunes de la vida diaria (resfríos, alergias, dolores de cintura o diarreas) —y que representan 85% de los padecimientos— podrían ser adecuadamente manejados con una videollamada, guiando al paciente para buscar la ayuda correspondiente. En casos más complicados, incluyendo la receta de medicamentos especializados, una visita cara a cara será irreemplazable.",
    "Huerta, E. (2019). «Los médicos virtuales: beneficios y limitaciones de la telemedicina». El Comercio.",
    "**Lectura B**",
    "¿Te gustaría que tu médico te atendiera por internet? Cada vez más pacientes ven esta idea como una opción viable para consultar a un especialista cuando tienen alguna dolencia. Y los médicos también le han descubierto la utilidad a la atención remota, ante una población que aumenta y envejece a la vez. Por supuesto, una cosa es la calidad de vida. Pero la telemedicina también es producto de la economía. «Una importante porción de los pacientes que diariamente ven los médicos son seguimientos, análisis de resultados de laboratorio o renovaciones de recetas», le explicó a la BBC la doctora Oyuka Byambasuren, experta en temas de tecnología aplicada a la medicina. «Muchas de esas consultas se pueden hacer con el doctor en una videollamada», agregó. Y todo esto es producto de la acuciante falta de médicos suficientes para atender a toda la población alrededor del mundo. El número de consultas médicas virtuales en Estados Unidos alcanzará los 105 millones para 2022, en comparación con los 23 millones registrados en 2017, de acuerdo a datos de IHS Markit. Schocken es una consultora de 46 años que vive en Washington y disfruta no tener que perder el tiempo en salas de espera donde, según ella, corre el riesgo de contagiarse gripe u otros males de otros pacientes. «Es realmente limpio y eficiente y me encanta», señaló. La telemedicina ha despegado particularmente en los países nórdicos, y es atendible que, en poco tiempo, reemplace la atención médica directa.",
    "Belton, P. (2019). «¿Te gustaría que te atiendan por internet?». BBC Mundo.",
])

T7 = "\n\n".join([
    "La cumbre de la Revolución Científica de la modernidad fue el descubrimiento de Isaac Newton de la ley de gravitación universal: todos los objetos se atraen mutuamente con una fuerza directamente proporcional al producto de sus masas e inversamente proporcional al cuadrado de la distancia que los separa. Al subsumir bajo una única ley matemática los principales fenómenos físicos del universo observable, Newton demostró que la física terrestre y celeste eran una y la misma. De un golpe, el concepto de gravitación universal descubrió la significación física de las tres leyes de Johannes Kepler sobre el movimiento planetario, resolvió el espinoso problema del origen de las mareas y justificó a Galileo Galilei por su curiosa e inexplicada observación de que el descenso de un objeto en caída libre es independiente de su peso. Newton había realizado la meta de Kepler de desarrollar la física basada en las causas.",
    "El importante descubrimiento de la gravitación universal, que devino en el paradigma de la ciencia que obtiene éxitos, no fue el resultado de un aislado destello del genio; fue la culminación de una serie de ejercicios en la resolución del problema. No fue un producto de la inducción, sino de deducciones lógicas y transformaciones de las ideas existentes.",
    "El descubrimiento de la gravedad universal aportó lo que creo es una característica fundamental de todo gran avance en la ciencia, desde las innovaciones más simples hasta las revoluciones más dramáticas: la creación de algo nuevo mediante la transformación de las nociones existentes.",
])

T8 = "\n\n".join([
    "Dos exposiciones paralelas rescatan los extraordinarios dibujos procedentes de los cuadernos de bocetos de Leonardo da Vinci (1452-1519), el genio universal del Renacimiento italiano, quien en raras ocasiones se presentaba en las cortes como un pintor, sino más bien como un ingeniero, arquitecto, músico, diseñador de armas u organizador de fiestas. La muestra «Leonardo da Vinci: la mecánica del hombre» se puede visitar hasta el 10 de noviembre en The Queen's Gallery, en el Palacio de Holyroodhouse, en Edimburgo; y la muestra «Leonardo da Vinci: el hombre universal» se puede visitar hasta el 1 de diciembre en las Galerías de la Academia, en Venecia. Ambas retrospectivas representan una ocasión única para admirar los dibujos del célebre artista florentino, que son extremadamente frágiles, y en el caso de la muestra veneciana sólo se pueden exponer públicamente una vez durante una generación, ya que deben ser custodiados en la oscuridad más absoluta y bajo unas exigentes condiciones ambientales.",
    "«Leonardo da Vinci: la mecánica del hombre» examina los innovadores dibujos que realizó el artista sobre el cuerpo humano y demuestra que es uno de los más destacados anatomistas de la historia. La muestra reúne 30 obras que incluyen 18 hojas, entre las más preciosas de Leonardo, que forman el Manuscrito anatómico A, con más de 240 dibujos y 13000 palabras que rellenan estas páginas, que fueron realizadas durante el invierno de 1510 y 1511. Leonardo ilustró prácticamente cada hueso del cuerpo humano y los principales grupos musculares. Estos estudios anatómicos no fueron publicados a lo largo de su vida y permanecieron inéditos durante varios siglos. En sus anotaciones, presentes en la exposición, describe un examen post mortem de un hombre de 100 años de edad en el que ofrece la primera descripción exacta de una cirrosis hepática y del estrechamiento de las arterias. Los cuadernos de Leonardo se exhiben junto a imágenes médicas del siglo XXI que revelan el carácter precursor del genio florentino en técnicas como el escáner IRM o la modelización informática en 3D.",
    "«Leonardo da Vinci. El hombre universal» muestra los excepcionales folios del maestro florentino conservados desde el año 1822 en la colección gráfica del Gabinete de los Dibujos de las Galerías de la Academia, en Venecia. Un total de 25 obras gráficas que nunca han sido mostradas al público. La exposición cuenta también con otras 27 hojas procedentes de préstamos de museos italianos y extranjeros como la Biblioteca Real de Turín, la Galería Uffizi de Florencia, la Galería Nacional de Parma, la Royal Collection del Castillo de Windsor, el Museo Británico de Londres y el Museo Ashmolean de Oxford. La colección dedicada al estudio de las proporciones del cuerpo humano incluye el célebre Hombre de Vitruvio, una representación armónica que es un símbolo de la perfección clásica del cuerpo y la mente. También se pueden admirar sus dibujos de botánica, proyectos geométricos, retratos de hombres, figuras femeninas, batallas y proyectos de armas e ingenios militares.",
])

T9 = "\n\n".join([
    "Comienza a oscurecer, ya están encendidas las vitrinas de la Carrera Trece, en los andenes se agolpa la multitud; voy en un bus que lucha por abrirse paso en la congestión vehicular. Entre la ciudad y yo está el vidrio de la ventanilla que devuelve mi imagen, perdida en la masa de pasajeros que se mueven al ritmo espasmódico del tránsito. Ahora vamos por una cuadra sin comercio, la penumbra de las fachadas le permite al pequeño mundo del interior reflejarse en todo su cansado esplendor: ya no hay paisaje urbano superpuesto al reflejo. Sólo estamos nosotros, la indiferente comunidad que comparte el viaje.",
    "El bus acelera su marcha y la ciudad desaparece. Baudrillard dice que un simulacro es la suplantación de lo real por los signos de lo real. No hay lo real, tan sólo la ventanilla que nos refleja. Nosotros, los pasajeros, suplantamos la realidad, somos el paisaje. ¿Somos los signos de lo real?",
    "Un semáforo nos detiene en una esquina. Otro bus se acerca lentamente hasta quedar paralelo al nuestro; ante mí pasan otras ventanillas con otros pasajeros de otra comunidad igualmente apática. Pasan dos señoras en el primer puesto. Serán amigas -pienso-, quizás compañeras de trabajo. Pero no hablan entre ellas. Sigue pasando la gente detrás de las otras ventanas, mezclando su imagen real con nuestro reflejo. Creo verme sentado en la cuarta ventanilla del bus que espera la señal verde junto a nosotros. Es mi reflejo, intuyo; pero no es reflejo: soy yo mismo sentado en el otro bus. Con temor y asombro, él y yo cruzamos una mirada cómplice, creo que nos sonreímos más allá del cansancio del día de trabajo. Los dos vehículos arrancan en medio de una nube de humo negro.",
    "(En el original, la oración «Serán amigas -pienso-, quizás compañeras de trabajo» está en letra cursiva.)",
])

T10 = "\n\n".join([
    "**«No concibo un mundo de solo máquinas o solo humanos»** (Haldo Spontón)",
    "Según este experto en Inteligencia Artificial, en el futuro será más notorio el acompañamiento de las máquinas en las labores cotidianas del humano. Su desarrollo, asegura, debe estar acompañado de «mucha responsabilidad y ética».",
    "Actualmente la inteligencia artificial, aunque útil, es muy bruta si se la compara con la humana. Sus capacidades apenas le permiten hacer labores muy específicas, como reconocer lo que una persona le ordena con su voz, o diferenciar una persona de un animal. Para ser multitarea, asegura Spontón, le hacen falta años de desarrollo, pero sobre todo, datos.",
    "Desde su trabajo como director de tecnología de Inteligencia Artificial para Globant, Spontón reconoce que la IA (como se le puede decir de manera corta) ha demostrado ser muy útil para el desarrollo de diversas labores que hacen los humanos. Parte de sus hazañas, destaca, es la capacidad de predecir lo que una persona está próxima a comprar teniendo en cuenta sus registros de compra y demás datos como edad, domicilio, si tienes hijos… etc.",
    "La aplicación anterior puede ser bastante útil para una cadena de retail que, por ejemplo, sabe que el aceite que su cliente compró hace un mes está próximo a terminarse y que por esos días ese producto está en promoción. Con esos datos, la inteligencia artificial podrá sugerir que al correo de este comprador se envíe una publicidad contándole el descuento.",
    "En su entrevista con El Espectador, Spontón mencionó que no falta mucho para que la publicidad sea «uno a uno», es decir, que los mensajes promocionales que llegan a los diferentes canales de comunicación de una persona sean diferentes a los de otra. De hecho, este medio hace algunos días contó que Rappi y AdsMovil comenzaron a implementar un modelo publicitario que muestra en la pantalla de los celulares a sus clientes publicidad basada en los intereses que registran en su base de datos. Un ejemplo de que el panorama que vaticina Spontón ya está dando sus primeros pasos para masificarse.",
    "Sin embargo, pareciera que la inteligencia artificial cada día gana más terreno en las capacidades humanas: antes era fácil decir que las máquinas no podían crear, que solo obedecían órdenes y nada más. Pero esa limitación se está redefiniendo.",
    "En el Google I/O de este año, por ejemplo, los invitados a la conferencia de apertura fueron recibidos por un DJ bastante particular. Este músico, mientras ponía las canciones para animar la fiesta, era asesorado por un robot que, por medio de una cámara, analizaba los movimientos de baile que hacían los asistentes. Basado en esos datos, la inteligencia artificial de esta máquina le recomendaba qué canciones poner, para así estimular más a la audiencia.",
    "Este ejemplo grafica a la perfección una frase que Spontón arrojó en medio de su entrevista, «no concibo un mundo de solo máquinas o solo humanos»: para el profesional, el acompañamiento de las máquinas en la cotidianidad de las personas, por medio de su inteligencia artificial, será más protagónico con el pasar de los años.",
    "El solo hecho de que las máquinas puedan ayudar a crear, o incluso crear, genera una zona gris que dificulta explicar con sencillez en qué se diferencia una inteligencia humana de una artificial. Spontón incluso titubeó al intentar responder tal interrogante.",
    "«Si la inteligencia artificial les permite a las máquinas crear, ¿cómo podré explicarle a un niño de forma sencilla la diferencia entre esta y la humana?», fue la pregunta que se le hizo al profesional, quien, después de un momento de reflexión, concluyó que no habrá necesidad: la IA estará tan permeada en la humanidad que hará parte de las personas incluso desde sus primeros años de vida.",
    "«Hay dimensiones en las que siempre seremos mejores que las máquinas y las máquinas tienen cosas en las que siempre serán mejores que nosotros», es el análisis que hace Spontón. Todo esto lleva a pensar que la mezcla de las habilidades humanas y tecnológicas no es cosa del futuro: desde hace miles de años la tecnología ha estado acompañando las labores humanas.",
    "Tomado de: El Espectador.",
])

# ---------------------------------------------------------------------------------------------------------
# Textos de la sección «La jerarquía textual: el tema central y la idea principal»
# ---------------------------------------------------------------------------------------------------------

IDEA_INTRO = (
    "Una vez que hemos identificado el tema central de un texto, podemos determinar la idea principal. Esta se "
    "formula mediante una oración o un enunciado. Por ejemplo, si el tema central de un texto es «La importancia "
    "del sueño», la idea principal puede ser «El sueño es importante porque cumple con una función esencial de "
    "equilibrio de la vida mental». En consecuencia, la idea principal es el desarrollo esencial del tema central "
    "que se hace en el texto."
)

IP1 = "\n\n".join([
    "Con el grito O´zapft is!, se da por inaugurada la Oktoberfest, la Fiesta de la Cerveza en Múnich. Desde hace 180 años, la capital de Baviera celebra este festival que se ha proclamado como el evento popular más grande del mundo. Desde el día 21 de septiembre y hasta el 6 de octubre en la explanada de Theresienwiese, las casetas de las productoras históricas de cerveza de Múnich acogen a los siete millones de visitantes que año tras año acuden a la cita.",
    "El primer día de la Oktoberfest todos los habitantes de Múnich se dirigen en desfile hacia el recinto de la fiesta, custodiando los carros de las cervecerías que transportan el «oro líquido». Ésta no queda inaugurada hasta que el alcalde de la ciudad no introduce el grifo en una de las grandes cubas y la cerveza comienza a manar. Durante las dos semanas siguientes se servirán hasta seis millones de litros de cerveza en grandes jarras de un litro.",
    "Las principales cervecerías históricas tienen sus casetas en el interior del recinto que también acoge un gran parque de atracciones y multitud de puestos de comida. Las famosas y deliciosas cervezas Paulaner, Spaten, Hofbräu, Hacker-Pschorr, Augustiner y Löwenbräu se sirven en grandes mesas corridas en sus respectivos pabellones, donde además se pueden degustar los platos bávaros tradicionales como todo tipo de wurstel, brezel y pollo asado.",
])

IP2 = "\n\n".join([
    "Cuando empezaron a encontrarse vestigios de un mundo perdido en el fondo del mar del Norte, nadie podía creerlo. Aparecieron por primera vez hace un siglo y medio, cuando la pesca de arrastre se extendió por toda la costa neerlandesa. Los pescadores barrían el lecho marino con sus redes y las subían llenas de lenguados, platijas y otros peces que viven en el fondo del mar. Pero a veces caía también sobre la cubierta algún colmillo enorme, o los restos de un uro, de un rinoceronte lanudo o de alguna otra bestia extinguida. Estas pistas de que las cosas no siempre habían sido como eran ahora inquietaban a los pescadores, quienes devolvían al mar todo aquello para lo que no tenían explicación.",
    "Generaciones después, Dick Mol, un hábil aficionado a la paleontología, convenció a los pescadores para que le facilitasen esos huesos y tomasen nota de las coordenadas exactas del lugar donde los habían encontrado. En 1985 un capitán le entregó una mandíbula humana completa, perfectamente conservada, con los molares desgastados.",
    "Mol y su amigo Jan Glimmerveen, otro paleontólogo aficionado, hicieron datar el hueso mediante radiocarbono. Resultó que tenía 9500 años de antigüedad, lo cual quiere decir que el individuo a quien perteneció aquella mandíbula vivió durante el mesolítico, período que en el norte de Europa comenzó al final de la última glaciación, hace unos 12000 años, y se prolongó hasta la llegada de la agricultura, unos 6000 años más tarde.",
    "«Creemos que proviene de un enterramiento que ha permanecido intacto desde que aquel mundo desapareció bajo las olas, hace unos 8000 años», dice Glimmerveen.",
    "La historia de esta tierra desaparecida empieza con la retirada de los hielos. Hace unos 18000 años, el nivel del mar en el norte de Europa era unos 122 metros más bajo que el actual. Gran Bretaña no era una isla, sino la deshabitada esquina noroccidental de Europa, y entre ella y el resto del continente se extendía una tundra helada. A medida que el planeta calentaba y el hielo retrocedía, los ciervos, uros y jabalíes empezaron a dirigirse hacia el norte y hacia el oeste, seguidos de los hombres que los cazaban. Procedentes de las regiones montañosas de lo que hoy es la Europa continental, los cazadores se encontraron ante una vasta llanura de escasa altitud. Los arqueólogos denominan ese terreno desaparecido Doggerland, por el banco de arena del mar del Norte conocido como Dogger.",
])

IP3 = "\n\n".join([
    "En la primavera del año 1990, un grupo de obreros estaba realizando las obras de la carretera del nuevo aeropuerto internacional de la ciudad de Xian, al suroeste de Beijing, cuando, a unos seis metros de profundidad, el golpe de un pico produjo un extraño sonido. Los obreros observaron sorprendidos que habían dado con una especie de bóveda subterránea. Llamados a toda prisa, los arqueólogos no tardaron en darse cuenta de que estaban ante un descubrimiento excepcional. En efecto, los trabajos de excavación sacaron a la luz un complejo de bóvedas subterráneas que se extendían por un área de diez kilómetros cuadrados. En su interior aparecieron, cuidadosamente alineadas, miles de estatuillas de extraordinaria calidad, que representaban a personas con rostros exquisitamente moldeados, además de caballos y todo tipo de animales domésticos.",
    "No era éste el primer descubrimiento arqueológico importante en el área de Xian. En 1974, a pocos kilómetros de distancia, se había descubierto el impresionante ejército de terracota a tamaño natural de Qin Shi Huang Di, el primer emperador de China. Los lugareños se felicitaron ante la aparición de aquellos pequeños «hombres de barro», que, según creían, les traerían «hordas de turistas occidentales». Los arqueólogos identificaron fácilmente al propietario de aquellas fosas. Se trataba de Jing Di, cuarto emperador de la dinastía Han, que gobernó China entre 156 y 141 a.C., cuyo túmulo funerario, identificado desde hacía años pero que aún no ha sido excavado, se alza a un kilómetro de las fosas. Además, a unos 500 metros al este del túmulo de Jing Di se encuentra el enterramiento de su esposa, la emperatriz Wang.",
])

IP4 = "\n\n".join([
    "Según un nuevo estudio del Journal of Agricultural Food and Chemistry, el consumo de zumo de sandía antes de un entrenamiento duro ayuda a reducir la frecuencia cardíaca de los atletas y el dolor muscular al día siguiente.",
    "El motivo es que la sandía es rica en un aminoácido llamado L-Citrulina, que el cuerpo convierte en L-Arginina, un aminoácido esencial que ayuda a relajar los vasos sanguíneos y mejorar la circulación. Según un estudio publicado por el fisiólogo de la universidad de Florida Arturo Figueroa, las mujeres posmenopáusicas experimentan una mejor salud cardiovascular después de tomar suplementos de extracto de sandía durante 6 semanas. Además, en otro estudio de 2012, publicado por Figueroa también, confirmaba que tales suplementos ayudaban a aliviar la presión arterial en adultos obesos de mediana edad. Además de los beneficios para el corazón parece ser que puede servir como viagra natural también. También es cierto que para conseguir los efectos deseados es necesario ingerir unas grandes cantidades lo que puede causar otros efectos no deseados ya que la sandía es considerada como un buen diurético. Se suele pensar que la sandía tiene poco valor nutricional ya que el 80% de su composición es agua. Sin embargo 300 ml (una cuña) de sandía es alrededor de un tercio de la cantidad diaria de vitaminas A y C recomendadas. Además también contiene un poco de potasio.",
    "La sandía es una de las mejores fuentes dietéticas de licopeno, un antioxidante ligado tanto a la prevención como al tratamiento del cáncer de próstata, aunque los científicos todavía están investigando los detalles de esa conexión.",
])

TECNO = "\n\n".join([
    "**La Tecnología**",
    "La palabra «tecnología» se utiliza hoy a diestra y siniestra, sin que se perciba exactamente su significado. Para algunos, designa las aplicaciones de la ciencia; para otros, se confunde con la actividad de los ingenieros, es decir, el desarrollo. Por mi parte doy a la palabra un significado concreto que tiene, al menos, la ventaja de clarificar las cosas. Considero que, por una parte, están las ciencias de la naturaleza -entre las que está la física, cuya raíz es la palabra griega physis «naturaleza»- destinadas a descubrir y explicar las leyes de la naturaleza. Y por otra parte, la tecnología que consiste en fabricar objetos, artefactos y después estudiar sus propiedades. Porque está claro que cuando se fabrica un objeto (un péndulo, un ordenador, una nueva molécula química) no se conocen necesariamente sus propiedades (suena raro, pero eso existe).",
    "Cuando se inventó el láser, recuerdo que Pierre Aigrain, por entonces un joven y brillante director de las investigaciones para las aplicaciones militares, hizo un llamamiento para que surgieran ideas en vistas a su aplicación práctica. Cuando se descubrió el efecto Joule -desprendimiento de calor vinculado con el paso de la corriente eléctrica- y se construyeron los primeros aparatos, Edison no había inventado aún la bombilla. Claro está que a menudo las invenciones tecnológicas se hacen en vistas a una aplicación, pero para mí eso no es consustancial a ellas.",
    "Así, se puede hacer investigación pura, fundamental, en tecnología. El que trabaja en la construcción de un nuevo lenguaje para tal tipo de ordenador hace una investigación que puede considerarse pura y, por ejemplo, transferible a la biología para descodificar el ADN. El que crea nuevos lubricantes para mejorar los engranajes quizás esté desarrollando investigaciones fundamentales sobre la propiedad mecánica de los polímeros, etc. Tecnología no es sinónimo de ciencia aplicada, ni de ciencia para el ingeniero.",
])

PREHIST = "\n\n".join([
    "**La Prehistoria**",
    "El ser humano comenzó a surgir al principio de un extenso periodo conocido como prehistoria… La prehistoria es un periodo de la historia de la humanidad. El primero y el que más tiempo duró: desde que comenzó el proceso de evolución humana hasta la aparición de la escritura (un pueblo vive en la prehistoria hasta que escribe).",
    "La arqueología se ocupa del estudio de la prehistoria. Los arqueólogos buscan y analizan los restos de materiales que dejaron los primeros seres humanos. Gracias a la arqueología sabemos algo de la vida de nuestros antepasados: quiénes eran, dónde vivían, cuáles fueron los primeros instrumentos que fabricaron y sus primeras obras de arte. Como fue un periodo muy largo, la prehistoria suele dividirse en dos grandes etapas o edades: la edad de piedra y la edad de los metales.",
    "**La edad de piedra.** Se llama así porque en aquel remoto tiempo los antepasados del ser humano comenzaron a fabricar, sobre todo con piedra, sus primeros instrumentos o utensilios. También usaron otros materiales como la madera, y los huesos, cuernos y tendones de los animales que cazaban. Durante la edad de piedra se produjo el largo proceso de la evolución humana. Cuando la edad de piedra finalizó, ya existía el ser humano actual: ¡los científicos lo llaman Homo sapiens! Por el camino quedaron muchas especies parecidas al hombre, que se extinguieron o evolucionaron. La edad de piedra se divide en tres periodos:",
    "El paleolítico. Este período comenzó hace 2,5 millones de años, cuando el hombre aprendió a tallar la piedra. Los seres humanos del paleolítico eran cazadores-recolectores. ¿Qué quiere decir esto? Sencillamente, que vivían de la caza y la pesca, y de lo que recogían de las plantas (raíces, frutos).",
    "El mesolítico. Se prolongó desde el final del paleolítico hasta inicios del neolítico. En este período el ser humano seguía cazando y recolectando para sobrevivir.",
    "El neolítico. El hombre pulimentaba ya la piedra (es decir, la trabajaba con mayor precisión y podía construir utensilios más sofisticados). Pero el gran cambio que se produjo durante el neolítico (puede que escuches la expresión «revolución neolítica») es que nació la agricultura (aproximadamente hace 11.000 años, en el 9000 antes de Cristo). Debido a ello, el ser humano dejó de ser nómada (hasta ese momento, no tenía un hogar fijo) y se hizo sedentario, apareciendo así los primeros poblados. También comenzó a ser habitual la fabricación de piezas de cerámica.",
    "**La edad de los metales.** Llegó un momento de la prehistoria en que los pueblos dejaron de hacer sus instrumentos de piedra y pasaron a fabricarlos con metales (porque aprendieron las técnicas necesarias para ello). La edad de los metales se divide en tres periodos.",
    "La edad de cobre. El cobre fue el primer metal utilizado por los seres humanos.",
    "La edad de bronce. Se llama así porque el hombre empezó a utilizar el bronce, después de aprender a alear (mezclar) el cobre con otro metal: el estaño. Las antiguas culturas de Mesopotamia nacieron y se desarrollaron durante la edad de bronce. Al final de ese periodo surgieron también las principales civilizaciones de Grecia.",
    "La edad de hierro. Comenzó en Oriente, hace aproximadamente 3.200 años, aunque en la mayor parte de Europa no se inició hasta hace unos 2.800 años, y en América no se trabajó el hierro hasta la llegada de los europeos a finales del siglo XV de nuestra era. En este periodo los utensilios pasaron a ser fabricados con hierro.",
])

LENGUA = "\n\n".join([
    "**Lenguaje, lengua, dialecto y habla**",
    "Aunque muchas veces se utilizan como sinónimos, los conceptos de lenguaje, lengua, habla y dialecto tienen sus particularidades, cada uno se refiere a un aspecto diferente del acto comunicativo, por lo que es importante conocer sus características:",
    "- El lenguaje es la capacidad de poder establecer comunicación mediante signos, ya sean orales o escritos. De esta manera el lenguaje presenta muchísimas manifestaciones distintas en las diversas comunidades que existen en nuestro planeta. Una de esas manifestaciones son las lenguas o idiomas como el español, inglés, francés.",
    "- Una lengua es un sistema lingüístico utilizado por una comunidad de hablantes. Las palabras lengua e idioma se pueden considerar sinónimas. Una lengua se caracteriza principalmente por las siguientes características: se diferencia de otras por su escritura; tiene gramática y ortografía propias; tiene una tradición literaria importante, es decir, escritores conocidos.",
    "- Un dialecto es una variante lingüística de una lengua común, pero sin una fuerte diferenciación, que normalmente tiene una delimitación geográfica muy concreta.",
    "- El habla es la utilización que cada individuo hace de la lengua, de tal manera que si no hubiera hablantes, no habría lengua y al revés. La lengua es siempre la misma porque evoluciona muy lentamente, el habla cambia con frecuencia por el uso.",
])

MEMORIA = (
    "**¿Cuál es la capacidad de memoria del cerebro en gigabytes?**\n\n"
    "Desde un planteamiento estrictamente científico no se puede comparar la capacidad memorística del cerebro "
    "humano con la de un PC. Esto es así, porque desde el punto de vista técnico el software y el hardware de "
    "ambas máquinas están organizados de formas muy distintas. Mientras que en un ordenador, la información se "
    "guarda físicamente en un disco duro en secuencias de ceros y unos, en el cerebro la capacidad memorística es "
    "guardada en diferentes sitios, siguiendo un patrón de redes neuronales. No obstante, los neurólogos aseguran "
    "que nuestra cabeza guarda más gigabytes que los que puede albergar el ordenador más potente. Basta con pensar "
    "que poseemos unos 100.000 millones de neuronas, cada una de las cuales establece hasta 50.000 contactos con "
    "sus células vecinas."
)

LITIO = (
    "**¿Por qué las pilas de litio pueden recargarse cientos de veces?**\n\n"
    "La clave se encuentra en la propia química de la pila. Una batería de litio posee dos electrodos –uno positivo "
    "y otro negativo– y un electrolito que proporciona el medio conductor necesario para que los iones de litio se "
    "muevan entre los electrodos. Estos permiten a los iones colarse dentro de ellos y también salir: durante la "
    "inserción el litio penetra en el electrodo; en el proceso inverso, la extracción, salen del mismo. Cuando la "
    "batería se está descargando, el ion de litio se dirige del electrodo negativo –normalmente hecho de grafito– "
    "al positivo y entra en él. En el proceso de carga se produce el camino inverso. Ahora bien, no soportan más de "
    "trescientas a mil recargas, dependiendo de la pila."
)

VFNM = ["Verdadero", "Falso", "No mencionado"]

EXERCISES: list[dict] = [
    # ======================================================================================================
    # cl-consignas-lectura: notación marginal, idea principal, resumen y síntesis
    # ======================================================================================================
    _p(
        CO, "notacion-marginal-informatica", 1, "CLyRP · Práctica de lectura, notación marginal",
        "Notación marginal: la Informática",
        "Complete la notación marginal para cada uno de los siguientes párrafos (en la app: elegí, para cada párrafo, "
        "el título breve que va en el margen).\n\n"
        "**Párrafo 1.** La Informática es la ciencia aplicada que abarca el estudio y aplicación del tratamiento "
        "automático de la información, utilizando sistemas computacionales, generalmente implementados como "
        "dispositivos electrónicos. También está definida como el procesamiento automático de la información.\n\n"
        "**Párrafo 2.** En la informática convergen los fundamentos de las ciencias de la computación, la "
        "programación y metodologías para el desarrollo de software, la arquitectura de computadores, las redes de "
        "computadores, la inteligencia artificial y ciertas cuestiones relacionadas con la electrónica.\n\n"
        "**Párrafo 3.** Esta disciplina se aplica a numerosas y variadas áreas del conocimiento o las actividades "
        "humanas, como por ejemplo: gestión de negocios, almacenamiento y consulta de información, monitorización y "
        "control de proceso, industria, robótica, comunicaciones, control de transportes, investigación, desarrollo de "
        "juegos, diseño computarizado, aplicaciones/herramientas multimedia, etc. Una de las aplicaciones más "
        "importantes de la informática es proveer información en forma oportuna y veraz, lo cual, por ejemplo, puede "
        "tanto facilitar la toma de decisiones a nivel gerencial (en una empresa) como permitir el control de procesos "
        "críticos.",
        [
            _q("a) Notación marginal del párrafo 1.",
               ["Definición de informática", "Disciplinas que convergen en la informática", "Aplicaciones de la informática", "Origen histórico de la informática"], 0),
            _q("b) Notación marginal del párrafo 2.",
               ["Definición de informática", "Disciplinas que convergen en la informática", "Aplicaciones de la informática", "Origen histórico de la informática"], 1),
            _q("c) Notación marginal del párrafo 3.",
               ["Definición de informática", "Disciplinas que convergen en la informática", "Aplicaciones de la informática", "Origen histórico de la informática"], 2),
        ],
        [
            "La notación marginal es un título de una o dos palabras clave que resume la idea principal de cada párrafo.",
            "Fijate en el verbo central de cada párrafo: «es» (qué es), «convergen» (qué la forma), «se aplica» (para qué sirve).",
        ],
        [
            "La notación marginal pone en el margen de cada párrafo una o dos palabras clave con su idea principal, para ver de un golpe la estructura del texto. Se busca la oración núcleo de cada párrafo.",
            "Párrafo 1: «La Informática es la ciencia aplicada que abarca el estudio y aplicación del tratamiento automático de la información» y «También está definida como…». Es una definición → **Definición de informática**.",
            "Párrafo 2: «En la informática convergen los fundamentos de…» y sigue una lista de campos (computación, programación, redes, IA, electrónica) → **Disciplinas que convergen en la informática**.",
            "Párrafo 3: «Esta disciplina se aplica a numerosas y variadas áreas…» y siguen ejemplos (negocios, robótica, transportes) más la aplicación más importante → **Aplicaciones de la informática**.",
            "«Origen histórico» no corresponde a ningún párrafo: el texto no da fechas ni la historia de la disciplina. Un título general posible para todo el texto: «La Informática: definición, componentes y aplicaciones».",
        ],
    ),
    _p(
        CO, "idea-principal-oktoberfest", 2, "CLyRP · Práctica de lectura, idea principal, texto 1",
        "Idea principal: la Oktoberfest",
        IDEA_INTRO + "\n\nFormule la idea principal del siguiente texto (en la app: elegí la mejor formulación).\n\n**Texto 1**\n\n" + IP1,
        [
            _q("¿Cuál de estas oraciones formula mejor la idea principal del texto?", [
                "La Oktoberfest de Múnich, considerada el evento popular más grande del mundo, reúne cada año a millones de visitantes en torno a la cerveza de las cervecerías históricas de la ciudad.",
                "Durante las dos semanas de la Oktoberfest se sirven hasta seis millones de litros de cerveza en grandes jarras de un litro.",
                "La Oktoberfest no queda inaugurada hasta que el alcalde de Múnich introduce el grifo en una de las grandes cubas.",
                "Las cervecerías Paulaner, Spaten y Hofbräu son las más famosas de Baviera por sus platos tradicionales.",
            ], 0),
        ],
        [
            "Primero nombrá el tema (¿de qué habla todo el texto?) y después preguntate qué dice el texto de ese tema en conjunto.",
            "Una idea principal no puede ser un dato de un solo párrafo.",
        ],
        [
            "Tema central: la Oktoberfest de Múnich. Los tres párrafos la desarrollan: qué es y cuán grande es (párrafo 1), cómo se inaugura y cuánta cerveza se sirve (párrafo 2) y qué hay en el recinto (párrafo 3).",
            "La idea principal tiene que abarcar ese desarrollo: el evento popular más grande del mundo («se ha proclamado como el evento popular más grande del mundo»), con millones de visitantes («siete millones de visitantes») alrededor de la cerveza de las cervecerías históricas. Eso dice la opción «La Oktoberfest de Múnich, considerada el evento popular más grande del mundo…».",
            "«Se sirven hasta seis millones de litros…» y «no queda inaugurada hasta que el alcalde…» son datos ciertos pero de un solo párrafo (el segundo): son ideas secundarias.",
            "«Las cervecerías… son las más famosas de Baviera por sus platos tradicionales» además de ser un detalle es falsa: el texto dice que en los pabellones «además se pueden degustar los platos bávaros», no que las cervecerías sean famosas por la comida.",
        ],
    ),
    _p(
        CO, "idea-principal-doggerland", 2, "CLyRP · Práctica de lectura, idea principal, texto 2",
        "Idea principal: Doggerland",
        "Lea el siguiente texto y conteste la pregunta de opción múltiple.\n\n**Texto 2**\n\n" + IP2,
        [
            _q("¿Cuál es la idea principal del texto?", [
                "El repliegue de los hielos origina catástrofes que permiten la obtención de evidencia respecto de la existencia de vida en lugares ahora ocupados por el mar.",
                "Un grupo de pescadores encontró restos de un ser humano que vivió durante el mesolítico, etapa que se desarrolló al final de la última glaciación al norte de Europa.",
                "La existencia de relictos que pertenecen a poblaciones desaparecidas de su lugar de origen hace miles de años ha dejado sorprendidos a los investigadores europeos.",
                "La existencia de Doggerland inquieta a los arqueólogos que buscan respuestas acerca de la desaparición de una población cuando su tierra es tragada por el mar.",
            ], 0),
        ],
        [
            "Seguí el hilo del texto completo: hallazgos en el fondo del mar → datación de la mandíbula → qué era ese lugar y por qué desapareció.",
            "Desconfiá de las opciones que atribuyen a una persona algo que el texto atribuye a otra (¿quién se inquietaba?).",
        ],
        [
            "El texto cuenta cómo aparecieron en el fondo del mar del Norte restos de animales y de un ser humano, y explica que pertenecen a una tierra habitada (Doggerland) que el mar cubrió cuando se retiraron los hielos: «La historia de esta tierra desaparecida empieza con la retirada de los hielos» y «aquel mundo desapareció bajo las olas».",
            "Este texto no trae clave oficial: la respuesta se justifica con el texto así. «El repliegue de los hielos origina catástrofes…» es la única opción que junta las dos partes: el retiro de los hielos (que hizo subir el mar y tragó esa tierra) y la evidencia de vida en un lugar que hoy es mar. Es la idea principal.",
            "«Un grupo de pescadores encontró restos de un ser humano…» es un detalle parcial: resume el hallazgo y la datación de la mandíbula (párrafos 2 y 3), pero deja afuera lo que el texto termina explicando, el mundo perdido de Doggerland y por qué quedó bajo el mar. La idea principal tiene que abarcar eso, no un hueso.",
            "«…ha dejado sorprendidos a los investigadores europeos»: el texto no nombra a ningún grupo de «investigadores europeos» (habla de pescadores, de dos paleontólogos aficionados y de los arqueólogos que le pusieron nombre a la región) ni de «poblaciones desaparecidas de su lugar de origen»: lo que desapareció fue la tierra, bajo el mar. Además, el asombro inicial («nadie podía creerlo») es solo la frase de arranque, un detalle.",
            "«La existencia de Doggerland inquieta a los arqueólogos»: también traslada la inquietud, que en el texto es de los pescadores («inquietaban a los pescadores»); los arqueólogos solo aparecen poniéndole nombre a la región. (La quinta opción del original, sobre cazadores que iban hacia las montañas, invierte el texto: venían «procedentes de las regiones montañosas».)",
        ],
    ),
    _p(
        CO, "idea-principal-xian", 2, "CLyRP · Práctica de lectura, idea principal, texto 3",
        "Idea principal: las fosas de Xian",
        "Lea el siguiente texto y conteste la pregunta de opción múltiple.\n\n**Texto 3**\n\n" + IP3,
        [
            _q("¿Cuál es la idea principal del texto?", [
                "El cuarto emperador de la dinastía Han, Jing Di, que gobernó China entre 156 y 141 a.C., fue propietario de una fosa llena de estatuillas de un ejército chino.",
                "El emperador chino Jing Di hizo que enterraran a su esposa, la emperatriz Wang, a unos 500 metros al este del lugar donde este fue cuidadosamente enterrado.",
                "En 1990 los arqueólogos hallaron en Xian miles de figuras humanas y de animales, y un ejército en 1974, cerca de la tumba del emperador chino Jing Di.",
                "En el área de Xian se detectó el impresionante y numeroso ejército de Qin Shi Huang, primer emperador de China, a tamaño natural hecho con terracota.",
            ], 2),
        ],
        [
            "El texto tiene dos párrafos: el hallazgo de 1990 y su contexto (hallazgo de 1974 y a quién pertenecían las fosas). La idea principal tiene que cubrir ambos.",
        ],
        [
            "Párrafo 1: en 1990 aparecen en Xian bóvedas con «miles de estatuillas… que representaban a personas… además de caballos y todo tipo de animales domésticos». Párrafo 2: no era el primer hallazgo (el ejército de terracota de 1974, «a pocos kilómetros») y las fosas eran de Jing Di, cuyo túmulo «se alza a un kilómetro de las fosas».",
            "Este texto no trae clave oficial: la respuesta se justifica con el texto así. «En 1990 los arqueólogos hallaron en Xian miles de figuras…» es la única opción que reúne los dos hallazgos y su ubicación cerca de la tumba de Jing Di: es la idea principal.",
            "La opción de Jing Di como «propietario de una fosa llena de estatuillas de un ejército chino» falla en el contenido: las estatuillas de 1990 eran personas y animales domésticos, no «un ejército»; el ejército era de Qin Shi Huang Di.",
            "La de la tumba de la emperatriz Wang y la del ejército de terracota de Qin Shi Huang son detalles del segundo párrafo. Tampoco sirve la quinta del original (lo que esperaban los lugareños): otro detalle.",
        ],
    ),
    _p(
        CO, "idea-principal-sandia", 2, "CLyRP · Práctica de lectura, idea principal, texto 4",
        "Idea principal: la sandía",
        "Lea el siguiente texto y conteste la pregunta de opción múltiple.\n\n**Texto 4**\n\n" + IP4,
        [
            _q("¿Cuál es la idea principal del texto?", [
                "La reducción de la frecuencia cardíaca y el dolor muscular, la mejora de la circulación, entre otras razones, hacen favorable el consumo de sandía.",
                "La sandía puede servir para contrarrestar los efectos nocivos del cáncer a la próstata, aunque las pesquisas sobre esta conexión todavía continúan.",
                "Una cuña de sandía contiene alrededor de un tercio de la cantidad diaria de vitaminas A y C que un individuo requiere, además de contener Potasio.",
                "La sandía es rica en un aminoácido llamado L-Citrulina, que el cuerpo convierte en L-Arginina, un aminoácido esencial que ayuda a relajar los vasos.",
            ], 0),
        ],
        [
            "Todo el texto enumera efectos de la sandía. ¿Qué opción los agrupa en vez de elegir uno?",
        ],
        [
            "El texto recorre los beneficios de la sandía: baja la frecuencia cardíaca y el dolor muscular (párrafo 1), mejora la circulación y la salud cardiovascular, aporta vitaminas y potasio (párrafo 2) y licopeno (párrafo 3).",
            "Este texto no trae clave oficial: la respuesta se justifica con el texto así. La opción que generaliza esos beneficios («entre otras razones, hacen favorable el consumo de sandía») es la idea principal.",
            "La del cáncer de próstata sale del último párrafo y además exagera: el texto solo dice que el licopeno está «ligado» a la prevención y el tratamiento, y que los científicos «todavía están investigando».",
            "La de las vitaminas A y C y la de la L-Citrulina son datos de un solo pasaje del segundo párrafo (ideas secundarias que explican o ejemplifican). La quinta opción del original, sobre las mujeres posmenopáusicas, es otro detalle y además lo deforma («diariamente», «mejoran sensiblemente»).",
        ],
    ),
    _p(
        CO, "sintesis-tecnologia", 2, "CLyRP · Práctica de lectura, resumen y síntesis («La Tecnología»)",
        "Resumen y síntesis: «La Tecnología»",
        "Lea el texto. Las consignas originales piden subrayar las ideas principales, hacer un resumen y una "
        "síntesis; en la app se convierten en dos preguntas de opción múltiple.\n\n"
        "Recordá: el **resumen** transcribe las ideas principales con el mismo vocabulario y en el mismo orden del "
        "texto; la **síntesis** también condensa, pero con vocabulario y estilo propios (es una reelaboración personal).\n\n"
        + TECNO,
        [
            _q("a) ¿Cuál es la idea principal (la tesis) que sostiene el autor?", [
                "La tecnología consiste en fabricar objetos y estudiar después sus propiedades; no es sinónimo de ciencia aplicada y en ella también se hace investigación pura.",
                "La tecnología es la aplicación práctica de las ciencias de la naturaleza, como la física.",
                "Las invenciones tecnológicas se hacen siempre en vistas a una aplicación, como muestra el caso del láser.",
                "La tecnología es la actividad de los ingenieros, es decir, el desarrollo.",
            ], 0),
            _q("b) ¿Cuál de estos textos es una **síntesis** adecuada (no un resumen) de la lectura?", [
                "Para el autor, lo que define a la tecnología no es su utilidad sino su objeto: crear artefactos cuyas propiedades hay que investigar después. Por eso en ella cabe la investigación básica, y reducirla a ciencia aplicada o a ingeniería es un error.",
                "La palabra tecnología se utiliza sin que se perciba su significado. Por una parte están las ciencias de la naturaleza, destinadas a descubrir y explicar sus leyes; por otra, la tecnología, que consiste en fabricar objetos y después estudiar sus propiedades. Se puede hacer investigación pura en tecnología. Tecnología no es sinónimo de ciencia aplicada.",
                "Para el autor, la tecnología vale por sus aplicaciones: el láser y el efecto Joule muestran que primero se piensa en la aplicación y después se fabrica el objeto.",
                "El texto cuenta la historia del láser y de la bombilla de Edison para mostrar que los inventos tardan muchos años en llegar al público.",
            ], 0),
        ],
        [
            "El autor discute dos definiciones ajenas («Para algunos… para otros…») y después da la suya («Por mi parte…»). La tesis es la suya.",
            "Para b): primero descartá las que dicen algo que el autor rechaza; entre las que quedan, la síntesis es la que no copia las frases del texto.",
        ],
        [
            "Ideas principales: párrafo 1, la tecnología «consiste en fabricar objetos, artefactos y después estudiar sus propiedades»; párrafo 2, la aplicación no es «consustancial» a las invenciones; párrafo 3, «se puede hacer investigación pura, fundamental, en tecnología» y «Tecnología no es sinónimo de ciencia aplicada, ni de ciencia para el ingeniero».",
            "a) La tesis es «La tecnología consiste en fabricar objetos y estudiar después sus propiedades; no es sinónimo de ciencia aplicada…», que junta esas tres ideas. «La aplicación práctica de las ciencias de la naturaleza» y «la actividad de los ingenieros» son justamente las dos definiciones que el autor descarta al principio («Para algunos…; para otros…») y al final. «Se hacen siempre en vistas a una aplicación» contradice «a menudo… pero para mí eso no es consustancial a ellas»; el láser es el ejemplo de una invención para la que se buscaron aplicaciones después.",
            "b) La opción que empieza «La palabra tecnología se utiliza sin que se perciba su significado…» dice lo correcto pero copia frases del texto en el mismo orden: es un **resumen**, no una síntesis.",
            "La de «la tecnología vale por sus aplicaciones» invierte la tesis (el autor dice que la aplicación no es lo esencial) y la de «la historia del láser y de la bombilla de Edison» toma los ejemplos como si fueran el tema; además, el texto no habla de cuánto tardan los inventos en llegar al público.",
            "La que empieza «Para el autor, lo que define a la tecnología no es su utilidad sino su objeto…» reformula la tesis con palabras propias («lo que define… no es su utilidad sino su objeto») y relaciona las ideas: es la **síntesis** adecuada.",
        ],
    ),
    # ======================================================================================================
    # cl-texto-cientifico: «Comprensión lectora», textos 1 a 10
    # ======================================================================================================
    # ---- Texto 1: nomofobia (clave de la copia corregida del usuario: b, e, c, d, e, a, d) ----
    _p(
        TC, "cl1-nomofobia-a", 2, "CLyRP · Práctica de lectura, texto 1",
        "Texto 1: nomofobia (preguntas 1 a 3)",
        _enc(1, "1 a 3", T1),
        [
            _q("Pregunta 1. ¿Cuál es el tema central del texto?", [
                "La nomofobia o estrés ocasionado por el uso de celular.",
                "El estrés asociado al uso compulsivo de tecnología digital.",
                "La sensación de vibraciones fantasmas en el smartphone.",
                "El uso necesario de teléfonos inteligentes en la actualidad.",
            ], 0),
            _q("Pregunta 2. Determine la idea principal del texto.", [
                "Quienes usan smartphones buscan que este registre nuevos mensajes.",
                "El nombre nomofobia surgió abreviando la frase no-mobile-phone-phobia.",
                "Los jóvenes son incapaces de dejar inactivos sus teléfonos celulares.",
                "La nomofobia es el estrés ocasionado por el uso compulsivo del celular.",
            ], 3),
            _q("Pregunta 3. En el texto, la palabra DISPARAR implica el desarrollo de un proceso", [
                "Gradual.", "Armónico.", "Acelerado.", "Complejo.",
            ], 2),
        ],
        [
            "El tema central se dice en pocas palabras (un sustantivo con su complemento); la idea principal es una oración que dice qué afirma el texto sobre ese tema.",
            "Descartá las opciones demasiado amplias (hablan de algo más que el texto) y las demasiado estrechas (un solo dato).",
            VOCAB,
        ],
        [
            "Respuestas de la clave oficial del curso: 1 «La nomofobia o estrés ocasionado por el uso de celular», 2 «La nomofobia es el estrés ocasionado por el uso compulsivo del celular», 3 «Acelerado». El texto presenta la nomofobia, explica el origen del nombre, el estudio de Balding (el uso constante sube el estrés y los comportamientos compulsivos), los síntomas y datos de México.",
            "Pregunta 1: «La nomofobia o estrés ocasionado por el uso de celular». «El estrés asociado al uso compulsivo de tecnología digital» es demasiado amplio: el texto habla solo del celular («la ansiedad y angustia que produce el estar sin celular»). «Las vibraciones fantasmas» es una de las preguntas del arranque, un detalle. «El uso necesario de teléfonos inteligentes» no aparece: el texto no defiende que sean necesarios.",
            "Pregunta 2: «La nomofobia es el estrés ocasionado por el uso compulsivo del celular» une el tema con lo que el texto afirma: el uso constante «aumenta los niveles de estrés» y «los comportamientos compulsivos». «Buscan que registre nuevos mensajes» es uno de esos comportamientos (detalle); el origen del nombre es solo el segundo párrafo; «los jóvenes» generaliza algo que el texto no dice (los participantes eran estudiantes y empleados, sin hablar de edad). La opción del 72% de México (quinta del original) también es un dato aislado.",
            "Pregunta 3: «la angustia y el estrés se disparaban» = subían de golpe, rápido → **acelerado**. No es gradual (subida paulatina, lo contrario), ni armónico (equilibrado), ni complejo: el verbo habla de la velocidad del aumento, no de su complejidad.",
        ],
    ),
    _p(
        TC, "cl1-nomofobia-b", 2, "CLyRP · Práctica de lectura, texto 1",
        "Texto 1: nomofobia (preguntas 4 y 5)",
        _enc(1, "4 y 5", T1),
        [
            _q("Pregunta 4. La palabra INHABILIDAD connota", [
                "Defecto.", "Desmesura.", "Impericia.", "Torpeza.",
            ], 2),
            _q("Pregunta 5. Resulta incompatible con la información textual afirmar que los individuos nomofóbicos", [
                "Incrementan sus niveles de estrés debido al uso compulsivo de sus celulares.",
                "Acusan cierto temor ante una posible descarga del celular y la pérdida de señal.",
                "Pueden sentir subjetivamente que el teléfono celular se encuentra vibrando.",
                "Son completamente independientes y desinteresados de la aceptación social.",
            ], 3),
        ],
        [VOCAB, INCOMP],
        [
            "Respuestas de la clave oficial del curso: 4 «Impericia», 5 «Son completamente independientes y desinteresados de la aceptación social».",
            "Pregunta 4: «La inhabilidad de apagar el celular» = no ser capaz de hacerlo, falta de habilidad. «Impericia» es exactamente falta de pericia o habilidad (in- + pericia, como in- + habilidad). «Defecto» es una imperfección cualquiera, demasiado general; «desmesura» es exceso, describiría el uso, no la incapacidad; «torpeza» alude más a la falta de agilidad o de tino al moverse o actuar, no a no poder hacer algo.",
            "Pregunta 5: la incompatible es «Son completamente independientes y desinteresados de la aceptación social». El texto dice lo contrario: el estrés se dispara «una vez que el aparato extendía virtualmente su vida social» y buscan «incesantemente nuevas alertas, mensajes y actualizaciones».",
            "Las otras están en el texto: el uso constante «aumenta los niveles de estrés» (primera); «el asegurarse de que nunca se acabe la batería y el miedo a perder la señal» (segunda); «¿Has sentido vibraciones fantasmas?» (tercera).",
        ],
    ),
    _p(
        TC, "cl1-nomofobia-c", 2, "CLyRP · Práctica de lectura, texto 1",
        "Texto 1: nomofobia (preguntas 6 y 7)",
        _enc(1, "6 y 7", T1),
        [
            _q("Pregunta 6. Es incongruente con lo señalado en el texto sostener que el público usado como objeto del experimento", [
                "Constituía una población que realizaba las mismas actividades.",
                "Pasó por una prueba psicosomática y la resolución de un test.",
                "Estaba conformado parcialmente por estudiantes universitarios.",
                "Contaba, en parte, con la participación de empleados diversos.",
            ], 0),
            _q("Pregunta 7. Respecto de las personas que padecen nomofobia, se puede colegir que", [
                "Ascienden a la alarmante e inopinada cifra de 190 millones solamente en México.",
                "Toman medidas muy seguras de prevención para evitar el elevado estrés y miedo.",
                "Podrían evitar el incremento del estrés si usaran el celular solo para organizarse.",
                "La vida social los lleva inexorablemente a comprar smartphones más sofisticados.",
            ], 2),
        ],
        [
            INCOMP,
            "Para «colegir» (inferir), releé el «círculo vicioso» del cuarto párrafo: ¿en qué momento se dispara el estrés?",
        ],
        [
            "Respuestas de la clave oficial del curso: 6 «Constituía una población que realizaba las mismas actividades», 7 «Podrían evitar el incremento del estrés si usaran el celular solo para organizarse». En la pregunta 7 corregimos la errata «usarán» → «usaran».",
            "Pregunta 6: la incongruente es «realizaba las mismas actividades»: eran «estudiantes universitarios y empleados de diversas categorías y ocupaciones». Las demás están dichas: «se les aplicó un cuestionario y una prueba psicosomática de estrés»; «entre ellos estudiantes universitarios»; «empleados de diversas categorías».",
            "Pregunta 7: el círculo vicioso es que «las personas adquirían el smartphone para manejar su carga de trabajo» y el estrés se disparaba «una vez que el aparato extendía virtualmente su vida social». Se colige que, usándolo solo para organizarse, podrían evitar ese aumento.",
            "Distractores: los 190 millones son smartphones, no personas nomofóbicas; «toman medidas muy seguras de prevención» es lo contrario de lo que dice el texto (cuidar la batería y la señal son síntomas del estrés, no prevención); y el texto nunca habla de comprar smartphones más sofisticados.",
        ],
    ),
    # ---- Texto 2: demarcación ciencia/pseudociencia (clave de la copia corregida: c, e, b, d, a, e, c) ----
    _p(
        TC, "cl2-demarcacion-a", 2, "CLyRP · Práctica de lectura, texto 2",
        "Texto 2: ciencia y pseudociencia (preguntas 1 a 3)",
        _enc(2, "1 a 3", T2),
        [
            _q("Pregunta 1. El tema central que el autor expone es", [
                "El valor cognoscitivo que una teoría ostenta al margen de su creador.",
                "La distinción entre el conocimiento científico y el pseudocientífico.",
                "La comprensión cabal que hace de una teoría un saber aceptado.",
                "Los motivos que determinaron la persecución de los mendelianos.",
            ], 1),
            _q("Pregunta 2. En el texto, la expresión FILOSOFÍA DE SALÓN alude a una actividad", [
                "Relevante para la sociedad en la cual se desarrolla.",
                "De tipo pseudocientífico y arbitrariamente dependiente.",
                "Intelectual que cuenta con un estatus social elevado.",
                "Puramente reflexiva, sin ninguna aplicación práctica.",
            ], 3),
            _q("Pregunta 3. Determine la idea principal del texto.", [
                "Muchos filósofos sostienen que un enunciado constituye un conocimiento científico si un número elevado de individuos lo aceptan y lo comparten con suficiente convicción.",
                "La diferencia entre ciencia y pseudociencia reside en que la primera depende del apoyo objetivo de los hechos mientras que la segunda está relacionada con estados de la mente.",
                "La aceptación y la defensa viscerales de los asertos más innovadores y sólidos de una teoría científica constituyen un crimen intelectual más que una capacidad intelectual virtuosa.",
                "Los científicos actúan con mucha cautela respecto de sus teorías mejor elaboradas, como lo demuestra la incredulidad de Newton respecto de la atracción de cuerpos a distancia.",
            ], 1),
        ],
        [
            "La pregunta que organiza todo el texto está en el primer párrafo: «¿Qué distingue al conocimiento de la superstición, la ideología o la pseudociencia?».",
            "Para FILOSOFÍA DE SALÓN, mirá con qué se contrapone en la misma oración («no es un mero problema de… ; tiene una importancia…»).",
        ],
        [
            "Respuestas de la clave oficial del curso: 1 «La distinción entre el conocimiento científico y el pseudocientífico», 2 «Puramente reflexiva, sin ninguna aplicación práctica», 3 «La diferencia entre ciencia y pseudociencia reside en que la primera depende del apoyo objetivo de los hechos…». En la opción de la pregunta 2 corregimos la errata «Puramente y reflexiva» → «Puramente reflexiva».",
            "Pregunta 1: el texto gira en torno al problema de la «demarcación entre ciencia y pseudociencia» → «La distinción entre el conocimiento científico y el pseudocientífico». «El valor cognoscitivo… al margen de su creador» es un aspecto del último párrafo; «la comprensión cabal» es justo lo que el autor dice que no importa («aunque nadie la comprenda»); la persecución de los mendelianos es un ejemplo.",
            "Pregunta 2: «no es un mero problema de filosofía de salón; tiene una importancia social y política vital». Por contraste, filosofía de salón es una discusión puramente teórica, sin consecuencias prácticas. «Relevante para la sociedad» es lo opuesto (eso es lo que sí tiene la demarcación); «estatus social elevado» se queda con la palabra «salón» pero ignora el contraste; nada la vincula con lo pseudocientífico.",
            "Pregunta 3: la idea principal es «La diferencia entre ciencia y pseudociencia reside en que la primera depende del apoyo objetivo de los hechos…»: el valor científico «depende solamente del apoyo objetivo que prestan los hechos», mientras que «creencias, convicciones, comprensiones… son estados de la mente humana». La de «muchos filósofos sostienen…» es la postura que el autor refuta; la del «crimen intelectual» deforma la frase (habla de la «fe ciega», no de defender los asertos más sólidos) y es secundaria; la de Newton es un ejemplo que apoya la tesis.",
        ],
    ),
    _p(
        TC, "cl2-demarcacion-b", 2, "CLyRP · Práctica de lectura, texto 2",
        "Texto 2: ciencia y pseudociencia (preguntas 4 y 5)",
        _enc(2, "4 y 5", T2),
        [
            _q("Pregunta 4. Es incompatible con lo sostenido por el autor del texto aseverar que la aceptación mayoritaria de un tipo particular de conocimiento", [
                "Es posible que evidencie un influjo de tipo psicológico.",
                "Abre la posibilidad de que este sea pseudocientífico.",
                "Se relaciona muchas veces con creencias absurdas.",
                "Determina de forma irrecusable su estatus científico.",
            ], 3),
            _q("Pregunta 5. En el texto, la palabra PODEROSA adquiere el sentido de", [
                "Sólida.", "Grande.", "Ingente.", "Mirífica.",
            ], 0),
        ],
        [INCOMP, VOCAB],
        [
            "Respuestas de la clave oficial del curso: 4 «Determina de forma irrecusable su estatus científico», 5 «Sólida».",
            "Pregunta 4: el autor sostiene que «ningún grado de convencimiento con relación a ciertas creencias las convierte en conocimiento» y que un enunciado puede ser pseudocientífico «aunque todo el mundo lo crea». Decir que la aceptación mayoritaria «determina de forma irrecusable su estatus científico» es incompatible.",
            "Las otras son compatibles: la aceptación es un efecto sobre las mentes («su influencia psicológica sobre las mentes humanas»); puede ser pseudocientífico aunque todos lo crean; y «muchas personas han sido convencidos creyentes de nociones absurdas».",
            "Pregunta 5: «La de Newton es la teoría más poderosa que la ciencia ha producido nunca»: se habla de su fuerza explicativa, de su solidez → **sólida**. «Grande» e «ingente» hablan de tamaño o cantidad; «mirífica» (maravillosa) es una valoración de asombro, no de fortaleza. Además, la frase contrasta con que Newton dudaba de ella: aun la teoría más sólida merece escepticismo.",
        ],
    ),
    _p(
        TC, "cl2-demarcacion-c", 3, "CLyRP · Práctica de lectura, texto 2",
        "Texto 2: ciencia y pseudociencia (preguntas 6 y 7)",
        _enc(2, "6 y 7", T2),
        [
            _q("Pregunta 6. Si tanto la ciencia como la pseudociencia fueran aceptadas masivamente y determinaran un influjo en la mente de quienes la aceptan, probablemente", [
                "Newton habría tenido más razones para dudar de su teoría.",
                "El apoyo objetivo en la evidencia fáctica sería inevitable.",
                "Se superaría la confirmación a partir de los hechos reales.",
                "El deslinde entre una y otra sería sumamente impreciso.",
            ], 3),
            _q("Pregunta 7. Si la creencia en los ángeles fuera aceptada por un conjunto minúsculo de personas,", [
                "Tendría que ser considerada como un conocimiento cimentado de forma sólida.",
                "Al carecer de un apoyo objetivo en los hechos, seguiría siendo pseudocientífica.",
                "Sería menester considerarla científica pues dejaría de ser una creencia absurda.",
                "El autor del texto la soslayaría como ejemplo de consideraciones inverosímiles.",
            ], 1),
        ],
        [
            HIPO,
            "El único criterio que el autor acepta para el valor científico está en la última oración del texto.",
        ],
        [
            "Respuestas de la clave oficial del curso: 6 «El deslinde entre una y otra sería sumamente impreciso», 7 «Al carecer de un apoyo objetivo en los hechos, seguiría siendo pseudocientífica». Para el autor, la aceptación y la influencia psicológica no sirven para distinguir ciencia de pseudociencia; lo único que cuenta es «el apoyo objetivo que prestan los hechos».",
            "Pregunta 6: si las dos fueran aceptadas masivamente e influyeran en las mentes, esos rasgos no permitirían distinguirlas: el deslinde por ese camino sería sumamente impreciso. «Newton habría tenido más razones para dudar» no tiene relación con la aceptación; «el apoyo objetivo sería inevitable» y «se superaría la confirmación por los hechos» atribuyen a la aceptación un efecto sobre la evidencia que el autor niega («nada tiene que ver con su influencia psicológica»).",
            "Pregunta 7: que la crean pocos o muchos no cambia nada: los ángeles aparecen en el texto entre las «nociones absurdas» sin apoyo en los hechos, así que seguiría siendo pseudocientífica. Ser aceptada por pocos no la vuelve «conocimiento cimentado» ni «científica» ni deja de ser absurda; y el autor no la dejaría de lado como ejemplo, porque su argumento es justamente que el número de creyentes no importa.",
        ],
    ),
    # ---- Texto 3: el baile ----
    _p(
        TC, "cl3-baile-a", 2, "CLyRP · Práctica de lectura, texto 3",
        "Texto 3: el baile (preguntas 1 a 3)",
        _enc(3, "1 a 3", T3),
        [
            _q("Pregunta 1. ¿Qué título expresa mejor la idea central del texto?", [
                "Que el cuerpo siga el ritmo musical.",
                "El baile es mejor que el ejercicio.",
                "Baile en casa al regresar del trabajo.",
                "Más salud con el baile.",
            ], 3),
            _q("Pregunta 2. El texto no evidencia que el baile garantice la:", [
                "Felicidad.", "Relajación.", "Autoexpresión.", "Creatividad.",
            ], 0),
            _q("Pregunta 3. El autor destaca del baile su:", [
                "Condición de antídoto contra el estrés y el mal humor.",
                "Eficacia para bajar de peso.",
                "Capacidad sanadora de cuerpo y mente.",
                "Utilidad para aprender música.",
            ], 0),
        ],
        [
            "La primera oración del texto dice qué «se ha demostrado»; el resto la explica y al final da un consejo práctico.",
            "Para la pregunta 2, buscá cada palabra (o un sinónimo claro) en el texto: la que no aparezca es la respuesta.",
        ],
        [
            "Este texto no trae clave oficial; estas son las respuestas, que se justifican con el texto en los pasos siguientes: 1 «Más salud con el baile», 2 «felicidad», 3 «antídoto contra el estrés y el mal humor».",
            "Pregunta 1: el texto enumera beneficios del baile para la mente y el cuerpo (antídoto contra el estrés, endorfinas, creatividad, autoestima, energía) → «Más salud con el baile». «Que el cuerpo siga el ritmo» y «Baile en casa al regresar del trabajo» son el consejo final, una parte; «El baile es mejor que el ejercicio» exagera: solo dice que la capacidad sanadora «nada tiene que ver con los diez minutos de gimnasia», no que el baile supere a todo ejercicio.",
            "Pregunta 2: el texto sí nombra la relajación («se siente más relajada»), la autoexpresión («liberar lo que siente», «liberar los sentimientos atrapados») y la creatividad («aumenta la creatividad y la autoestima»). La felicidad no aparece: habla de bienestar y de combatir el mal humor, pero no dice que el baile la garantice.",
            "Pregunta 3: lo que el autor pone primero y presenta como demostrado es que el baile es «uno de los mejores antídotos contra el estrés y el mal humor»; el resto del texto (las endorfinas, alejar «las preocupaciones y tensiones») desarrolla esa misma idea. El texto nunca habla de bajar de peso, y la música aparece como algo que cada uno lleva adentro («la música interior»), no como algo que el baile ayude a aprender. «Capacidad sanadora de cuerpo y mente» no está así en el texto: la capacidad sanadora es del cuerpo («que sea el cuerpo quien asuma su capacidad sanadora»). (La quinta opción del original, la superioridad sobre todo ejercicio, ya se descartó en la pregunta 1.)",
        ],
    ),
    _p(
        TC, "cl3-baile-b", 2, "CLyRP · Práctica de lectura, texto 3",
        "Texto 3: el baile (preguntas 4 y 5)",
        _enc(3, "4 y 5", T3),
        [
            _q("Pregunta 4. ¿Cuál de los siguientes términos tiene una mayor aproximación al sentido en el que se emplea la palabra baile?", [
                "Ejercicio.", "Bienestar.", "Creatividad.", "Reflexión.",
            ], 3),
            _q("Pregunta 5. El autor recomienda sobre todo que", [
                "Se cante o se tararee para reforzar los sentimientos.",
                "Cada quien siga el ritmo de su música.",
                "La música domine nuestra esencia más íntima.",
                "Se elija siempre música alegre.",
            ], 1),
        ],
        [
            "Buscá la oración en la que el texto dice qué ES bailar (no qué produce).",
            "La recomendación aparece después de «Entonces,…»; leé hasta el final del párrafo.",
        ],
        [
            "Este texto no trae clave oficial; estas son las respuestas, que se justifican con el texto en los pasos siguientes: 4 «reflexión», 5 «cada quien siga el ritmo de su música».",
            "Pregunta 4: la única definición del baile en el texto es «Bailar es una especie de meditación activa». Ninguna opción es sinónimo exacto de «meditación», pero **reflexión** (volver el pensamiento sobre uno mismo) es la más cercana; las otras no dicen qué es el baile. «Ejercicio» queda descartado por el propio texto («nada tiene que ver con los diez minutos de gimnasia»); «bienestar» y «creatividad» son efectos del baile («hormonas del bienestar», «aumenta la creatividad»), no lo que el baile es. (La opción «endorfinas» del original también es un efecto.)",
            "Pregunta 5: después de «Entonces… baile en casa», el autor insiste en que «no importa el tipo de música», que se trata de «la música interior», y cierra con «dejar que suene en su interior y que su cuerpo siga el son» → que cada uno siga el ritmo de su propia música.",
            "Cantar o tararear es un medio «para liberar lo que siente», no para «reforzar los sentimientos»; el texto no quiere que la música «domine» la esencia, sino «conectarnos con nuestra más íntima esencia»; y elegir «siempre música alegre» contradice «No importa el tipo de música que prefiera». (La opción «más ejercicios físicos con música» del original contradice la distinción con la gimnasia.)",
        ],
    ),
    # ---- Texto 4: transposones y esquizofrenia ----
    _p(
        TC, "cl4-esquizofrenia-a", 2, "CLyRP · Práctica de lectura, texto 4",
        "Texto 4: genes saltarines y esquizofrenia (preguntas 1 a 3)",
        _enc(4, "1 a 3", T4),
        [
            _q("Pregunta 1. El texto gira en torno a", [
                "Una investigación sobre la raíz de las grandes enfermedades.",
                "La razón verdadera de la esquizofrenia en el mundo actual.",
                "Una nueva explicación de la causa de la esquizofrenia.",
                "La relevancia del entorno en las enfermedades mentales.",
            ], 2),
            _q("Pregunta 2. El vocablo REGULAR se emplea en el sentido de", [
                "Utilizar.", "Examinar.", "Controlar.", "Observar.",
            ], 2),
            _q("Pregunta 3. Una idea contraria a las conclusiones de Kato y Kazuya es que", [
                "La esquizofrenia está determinada por el medio ambiente.",
                "La esquizofrenia se genera en el córtex cerebral frontal.",
                "Los genes saltarines tienen un rol central en la esquizofrenia.",
                "El entorno resulta cuestionado como eje de la esquizofrenia.",
            ], 0),
        ],
        [
            "El primer párrafo opone «lo usual» (causa: el entorno) a lo que muestra la investigación nueva.",
            VOCAB,
        ],
        [
            "Este texto no trae clave oficial; estas son las respuestas, que se justifican con el texto en los pasos siguientes: 1 «una nueva explicación de la causa de la esquizofrenia», 2 «controlar», 3 «la esquizofrenia está determinada por el medio ambiente».",
            "Pregunta 1: el texto presenta la propuesta de los científicos de Tokio («los transposones… son una causa mayor de la esquizofrenia»), que derriba el paradigma usual → una nueva explicación. «La raíz de las grandes enfermedades» es demasiado amplio (el cáncer solo se menciona de paso); «la razón verdadera… en el mundo actual» exagera lo que el texto presenta como algo que los científicos «sugieren»; «la relevancia del entorno» es un aspecto: el punto es que el entorno actúa a través de los genes.",
            "Pregunta 2: «secuencias especializadas en responder al entorno y regular a los genes vecinos»; antes dice que los transposones «alteran su actividad» y que «la regulación de los genes depende… de las secuencias de ADN que tienen al lado». Regular = controlar su actividad. Utilizar, examinar y observar no describen una acción de una secuencia de ADN sobre un gen. (Se omitió la opción «aprobar» del original.)",
            "Pregunta 3: las conclusiones ponen la causa en los transposones; el entorno solo actúa «a través de los genes», y la idea de atribuir la causa «al entorno» es el paradigma que se está derribando. Decir que la esquizofrenia está determinada por el medio ambiente es contrario. El incremento se halló «en el córtex cerebral prefrontal», que es parte del lóbulo frontal, así que esa opción no contradice; el rol central de los genes saltarines y el cuestionamiento del entorno coinciden con las conclusiones. (Se omitió la opción «los experimentos realizados refuerzan las conclusiones», también compatible.)",
        ],
    ),
    _p(
        TC, "cl4-esquizofrenia-b", 3, "CLyRP · Práctica de lectura, texto 4",
        "Texto 4: genes saltarines y esquizofrenia (preguntas 4 y 5)",
        _enc(4, "4 y 5", T4),
        [
            _q("Pregunta 4. A partir de los resultados de la investigación nipona, se puede inferir que", [
                "Los transposones generan variedad neuronal durante el desarrollo normal.",
                "Las enfermedades mentales y el cáncer preocupan a la humanidad.",
                "La patología molecular está alcanzando un desarrollo inusitado.",
                "Las ideas respecto al origen de las enfermedades pueden cambiar.",
            ], 3),
            _q("Pregunta 5. Si la contrastación en modelos animales hubiese resultado contraria a lo esperado por Kato y Kazuya, probablemente", [
                "Los transposones no cumplirían las funciones que ellos les atribuyen.",
                "La cura contra enfermedades mentales se atrasaría notoriamente.",
                "El papel de la herencia en el origen de la enfermedad sería relevante.",
                "La patología molecular sería una ciencia con pocos logros que exhibir.",
            ], 0),
        ],
        [
            "Inferir no es repetir: descartá lo que el texto ya dice literalmente como dato de fondo.",
            HIPO,
        ],
        [
            "Este texto no trae clave oficial; estas son las respuestas, que se justifican con el texto en los pasos siguientes: 4 «las ideas respecto al origen de las enfermedades pueden cambiar», 5 «los transposones no cumplirían las funciones que ellos les atribuyen».",
            "Pregunta 4: los resultados apoyan que los transposones son una causa mayor de la esquizofrenia, y el texto dice que la patología molecular «está derribando ese paradigma» (el entorno como causa). Se infiere que las ideas sobre el origen de las enfermedades pueden cambiar. Que los transposones generan variedad neuronal no se infiere de los resultados: es un dato de fondo dicho literalmente. La preocupación de la humanidad no sale de los resultados, y «desarrollo inusitado» exagera (el texto la llama «vanguardia», nada más).",
            "Nota: omitimos la opción del original «la movilidad excesiva de los transposones es perjudicial en el desarrollo», porque también se puede defender a partir del texto («su movilidad excesiva…», insertos «cerca de genes esenciales para el desarrollo») y la pregunta quedaba con dos respuestas posibles.",
            "Pregunta 5: los modelos animales son una de las líneas de evidencia, y «todos los resultados apuntan a la misma conclusión». Si esa contrastación hubiera salido en contra, lo que quedaría en duda es el papel que le atribuyen a los transposones. El texto no habla de curas; un resultado contrario en animales no mostraría que la herencia es lo relevante (es otra hipótesis que nadie planteó); y un experimento fallido no dice nada sobre los logros de toda la patología molecular. (Omitimos «la idea de un gen saltarín no resultaría totalmente equivocada»: la existencia de los genes saltarines no está en discusión, así que esa opción también podía defenderse.)",
        ],
    ),
    # ---- Texto 5: Nozick ----
    _p(
        TC, "cl5-nozick-a", 3, "CLyRP · Práctica de lectura, texto 5",
        "Texto 5: el sentido de la vida, Nozick (preguntas 1 y 2)",
        _enc(5, "1 y 2", T5),
        [
            _q("Pregunta 1. Tanto la lectura A como la lectura B abordan el tema de", [
                "El deseo del ser humano de calzar en el plan de Dios.",
                "Los hijos como mecanismo para alcanzar inmortalidad.",
                "La voluntad de Dios como fuente de la vida significante.",
                "Cómo el hombre busca acceder a una vida significante.",
            ], 3),
            _q("Pregunta 2. En la lectura A, la expresión DEJAR SU IMPRONTA EN EL MUNDO connota", [
                "Materialismo.", "Divinidad.", "Trascendencia.", "Inmanencia.",
            ], 2),
        ],
        [
            "En una pregunta sobre «tanto A como B», descartá las opciones que solo valen para una de las dos lecturas.",
            "Impronta = marca, huella. ¿Qué significa que una vida deje una huella que dura más allá de la muerte?",
        ],
        [
            "Este texto no trae clave oficial; estas son las respuestas, que se justifican con el texto en los pasos siguientes: 1 «cómo el hombre busca acceder a una vida significante», 2 «trascendencia».",
            "Pregunta 1: A trata de los rastros que deja una vida («Una vida significante deja su impronta en el mundo»); B, de la voluntad divina como fuente del significado («el significado de la vida… está conectado con la voluntad divina»). Lo común es la búsqueda de una vida con sentido. El plan de Dios y la voluntad de Dios solo aparecen en B; los hijos como camino a la inmortalidad solo en A.",
            "Pregunta 2: dejar la impronta es dejar una marca que permanece («marca una diferencia permanente en el mundo: deja rastros») aun después de morir → **trascendencia** (ir más allá de uno mismo y de su tiempo).",
            "No es «inmanencia», que es lo contrario (permanecer dentro de sí); ni «divinidad», porque A deja a un lado el más allá («si no hay ningún otro lugar donde puedas estar»); ni «materialismo»: los rastros son los efectos de una vida, no bienes materiales.",
        ],
    ),
    _p(
        TC, "cl5-nozick-b", 2, "CLyRP · Práctica de lectura, texto 5",
        "Texto 5: el sentido de la vida, Nozick (preguntas 3 y 4)",
        _enc(5, "3 y 4", T5),
        [
            _q("Pregunta 3. Respecto de la argumentación presentada en la lectura B, resulta incompatible sostener que la existencia de Dios", [
                "Implica una cuestión de índole metafísica.",
                "Garantiza alcanzar una vida significativa.",
                "Es una cuestión que el autor deja abierta.",
                "Dista de ser plenamente demostrada.",
            ], 1),
            _q("Pregunta 4. A partir de la lectura A se infiere que, si una persona dejara una prole numerosa,", [
                "Habría garantizado el logro de una trascendencia infinita.",
                "Podría haber llegado a la cúspide de la plena inmortalidad.",
                "No habría dejado ningún rastro verdaderamente significante.",
                "Solamente habría extendido su mortalidad por un tiempo largo.",
            ], 3),
        ],
        [
            "En B, leé con atención la última oración: ¿qué es lo que el autor pone en duda «incluso de ser cierto» todo lo anterior?",
            "En A, buscá la pregunta del autor sobre los descendientes: ¿inmortalidad o…?",
        ],
        [
            "Este texto no trae clave oficial; estas son las respuestas, que se justifican con el texto en los pasos siguientes: 3 «garantiza alcanzar una vida significativa», 4 «solamente habría extendido su mortalidad por un tiempo largo».",
            "Pregunta 3: el autor deja expresamente de lado si Dios existe, si tiene un propósito o si lo revela («Lo que nos concierne aquí no es la cuestión de…»), y plantea: «nuestra pregunta es cómo todo esto, incluso de ser cierto, conseguiría dar significado a las vidas». Es decir, aun existiendo Dios no queda garantizado el significado: afirmar que lo garantiza es incompatible con su argumentación.",
            "Las otras no chocan con el texto: si Dios existe es una cuestión metafísica que el autor aparta; el propio autor la deja abierta («Lo que nos concierne aquí no es la cuestión de si existe Dios»); y que la existencia de Dios no está demostrada es compatible con que la deje abierta.",
            "Pregunta 4: «¿cómo producen inmortalidad los descendientes en vez de una mortalidad prolongada de alguna manera?», porque nadie cree que su cadena de descendientes «vaya a ser infinita». Con muchos hijos, solo se prolonga la mortalidad. La trascendencia infinita y la plena inmortalidad son justo lo que el autor niega; y decir que no deja ningún rastro contradice «cualquier continuación es mejor que ninguna»: los hijos sí son un rastro.",
        ],
    ),
    # ---- Texto 6: telemedicina ----
    _p(
        TC, "cl6-telemedicina-a", 3, "CLyRP · Práctica de lectura, texto 6",
        "Texto 6: telemedicina (preguntas 1 a 3)",
        _enc(6, "1 a 3", T6),
        [
            _q("Pregunta 1. Tanto la lectura A como la lectura B abordan el tema:", [
                "De los costos de instalar equipos de telemedicina en los hospitales.",
                "Del potencial reemplazo de las visitas médicas por las videollamadas médicas.",
                "Del efecto de los tratamientos médicos virtuales en la vida de pacientes graves.",
                "De la protección de los datos personales de los pacientes en internet.",
            ], 1),
            _q("Pregunta 2. En la lectura B, la palabra ACUCIANTE significa:", [
                "Intermitente.", "Estimulante.", "Enervante.", "Inquietante.",
            ], 3),
            _q("Pregunta 3. Respecto al desarrollo temático de la lectura B, el autor de la lectura A sostendría de forma medular:", [
                "El rechazo hacia el uso de cualquier forma que impida al médico realizar una atención efectiva.",
                "Una postura que impugne la consideración de que las tecnologías reemplazarían las visitas médicas.",
                "La correlación entre uso de tecnologías y depreciación de la práctica médica en situaciones de riesgo.",
                "Que la práctica médica debe ajustarse a los lineamientos eclécticos de aquel para mejoras en la salud.",
            ], 1),
        ],
        [
            "Buscá la pregunta que se hace A y la conclusión con la que termina B: hablan de lo mismo, pero no opinan igual.",
            VOCAB,
        ],
        [
            "Este texto no trae clave oficial; estas son las respuestas, que se justifican con el texto en los pasos siguientes: 1 «del potencial reemplazo de las visitas médicas por las videollamadas», 2 «inquietante», 3 «una postura que impugne…».",
            "Pregunta 1: A se pregunta «¿podrán los teléfonos inteligentes reemplazar la visita al médico?» y B termina diciendo que «es atendible que, en poco tiempo, reemplace la atención médica directa». Ese es el tema común. Ninguna lectura habla de lo que cuesta equipar los hospitales (B dice que la telemedicina es «producto de la economía», pero por la falta de médicos y las consultas de rutina) ni de la protección de los datos de los pacientes; y los «pacientes graves» no son el tema (A los usa para marcar el límite).",
            "Pregunta 2: «la acuciante falta de médicos suficientes»: una falta urgente, que preocupa → **inquietante**. No es intermitente (la falta no va y viene); «estimulante» es un sentido de acuciar (dar prisa), pero aplicado a un problema o una necesidad significa inquietar o preocupar; «enervante» (que debilita o pone nervioso) no describe la falta de médicos.",
            "Pregunta 3: B cree que la telemedicina reemplazará la atención directa; A sostiene que eso «es discutible» y que en casos complicados «una visita cara a cara será irreemplazable» → A impugnaría esa idea. A no rechaza «cualquier forma» de tecnología (acepta las videollamadas para el 85% de los padecimientos comunes); no habla de «depreciación de la práctica médica»; y los «lineamientos eclécticos» no aparecen en ninguna lectura.",
        ],
    ),
    _p(
        TC, "cl6-telemedicina-b", 3, "CLyRP · Práctica de lectura, texto 6",
        "Texto 6: telemedicina (preguntas 4 y 5)",
        _enc(6, "4 y 5", T6),
        [
            _q("Pregunta 4. Se infiere de la lectura B que las atenciones médicas mediante aplicativos:", [
                "Resultarían necesarias en países en los cuales las citas médicas son lentas, además de que tendrían consecuencias en la higiene.",
                "Determinarían la disminución de hospitales públicos y de la demanda médica en países con problemas de asistencia social.",
                "Posibilitarían el acceso a clínicas costosas y médicos reputados en tiempo real a aquellas personas en pobreza extrema.",
                "Aumentarían el cierre de las facultades de medicina y la deserción universitaria en lugares en los que los médicos no son útiles.",
            ], 0),
            _q("Pregunta 5. Si las videollamadas permitieran realizar un diagnóstico complejo que posibilite la atención de pacientes en casos de aislamiento obligatorio por pandemias,", [
                "La práctica médica sería ejecutada por autómatas en centros especializados de diagnóstico.",
                "Los médicos serían reemplazados por smartphones de alta gama en países en vías de desarrollo.",
                "Aun así el autor de A consideraría que es el médico el agente más importante en una acción integral.",
                "Las enfermedades mortales se tratarían de manera más efectiva sin la necesidad de un médico.",
            ], 2),
        ],
        [
            "Para la 4, juntá dos datos de B: por qué hacen falta las consultas virtuales y qué le gusta a Schocken.",
            HIPO,
        ],
        [
            "Este texto no trae clave oficial; estas son las respuestas, que se justifican con el texto en los pasos siguientes: 4 «resultarían necesarias en países en los cuales las citas médicas son lentas…», 5 «aun así el autor de A consideraría que es el médico el agente más importante».",
            "Pregunta 4: B dice que la telemedicina responde a «la acuciante falta de médicos suficientes» (de ahí, citas lentas) y Schocken valora no esperar en salas «donde… corre el riesgo de contagiarse gripe u otros males» y que «es realmente limpio» (higiene). Las demás agregan cosas que B no dice: cierre de hospitales públicos, acceso de personas en pobreza extrema a clínicas costosas, cierre de facultades de medicina.",
            "Pregunta 5: aunque el diagnóstico complejo fuera posible a distancia, la videollamada sigue siendo un medio entre el paciente y el médico; A insiste en que la visita cara a cara es irreemplazable en casos complicados y en que la tecnología guía «al paciente para buscar la ayuda correspondiente». El médico seguiría siendo el agente central.",
            "Las otras eliminan al médico (autómatas, smartphones que reemplazan médicos, tratamiento sin médico), algo que ninguna de las dos lecturas plantea: hasta B habla de consultas «con el doctor en una videollamada».",
        ],
    ),
    # ---- Texto 7: Newton ----
    _p(
        TC, "cl7-newton-a", 2, "CLyRP · Práctica de lectura, texto 7",
        "Texto 7: la gravitación de Newton (preguntas 1 a 3)",
        _enc(7, "1 a 3", T7),
        [
            _q("Pregunta 1. ¿Cuál es la idea principal del texto?", [
                "Tanto Newton como Kepler sostuvieron un modelo científico según el cual la física debe sustentarse en las causas.",
                "La gran revolución newtoniana se logró por una serie de ejercicios lógicos sobre un problema que preocupó a Galileo.",
                "Newton logró descubrir la ley de gravitación universal al emplear armónicamente principios deductivos e inductivos.",
                "El gran descubrimiento newtoniano implicó postular algo nuevo sobre la base de transformar ideas preexistentes.",
            ], 3),
            _q("Pregunta 2. El sentido contextual de la palabra SUBSUMIR es", [
                "Abarcar.", "Mediar.", "Describir.", "Demostrar.",
            ], 0),
            _q("Pregunta 3. Resulta incompatible con el texto aseverar que", [
                "En la indagación newtoniana es crucial referirse a las causas.",
                "Galileo determinó que un cuerpo cae con independencia de su peso.",
                "Para Newton la ley de la gravitación sólo se aplica a los cielos.",
                "Gracias a Newton se pudo comprender el problema de las mareas.",
            ], 2),
        ],
        [
            "La idea principal está en el último párrafo, que generaliza lo que mostró el caso de Newton.",
            VOCAB,
            INCOMP,
        ],
        [
            "Este texto no trae clave oficial; estas son las respuestas, que se justifican con el texto en los pasos siguientes: 1 «el gran descubrimiento newtoniano implicó postular algo nuevo sobre la base de transformar ideas preexistentes», 2 «abarcar», 3 «para Newton la ley de la gravitación sólo se aplica a los cielos».",
            "Pregunta 1: el texto cierra con la tesis: el descubrimiento aportó «la creación de algo nuevo mediante la transformación de las nociones existentes», y antes: «No fue un producto de la inducción, sino de deducciones lógicas y transformaciones de las ideas existentes». Lo de Kepler y las causas es un detalle; Galileo solo fue «justificado» por la ley, el problema no era suyo; y lo de principios «inductivos» contradice el texto. (La opción del original que hablaba del «cuadrado de sus masas» es falsa: es el producto de las masas y el cuadrado de la distancia.)",
            "Pregunta 2: «Al subsumir bajo una única ley matemática los principales fenómenos físicos» = incluir, abarcar varios fenómenos dentro de una sola ley. «Demostrar» tienta porque la oración sigue con «Newton demostró», pero es otro verbo con otro objeto; «mediar» y «describir» no encajan con «bajo una única ley».",
            "Pregunta 3: incompatible: el texto dice que «Newton demostró que la física terrestre y celeste eran una y la misma» (y la ley explica también las mareas y la caída libre, que son fenómenos terrestres). Las otras están en el texto: «la meta de Kepler de desarrollar la física basada en las causas», la «observación de que el descenso de un objeto en caída libre es independiente de su peso» y que la ley «resolvió el espinoso problema del origen de las mareas».",
        ],
    ),
    _p(
        TC, "cl7-newton-b", 3, "CLyRP · Práctica de lectura, texto 7",
        "Texto 7: la gravitación de Newton (preguntas 4 y 5)",
        _enc(7, "4 y 5", T7),
        [
            _q("Pregunta 4. Si un historiador sostuviera que la ley de Newton se obtiene inductivamente a partir de las leyes de Kepler,", [
                "Estaría esencialmente en lo correcto.",
                "El autor diría que está equivocado.",
                "Haría un aporte a la historia de la ciencia.",
                "Comprendería la obra de Newton.",
            ], 1),
            _q("Pregunta 5. Se infiere del texto que un avance significativo en ciencia implica", [
                "La utilización de razonamientos inductivos.",
                "Destellos geniales de un científico metódico.",
                "Partir de algunas ideas aceptadas previamente.",
                "Partir de las innovaciones lógicas más simples.",
            ], 2),
        ],
        [HIPO, "Las dos preguntas se resuelven con el segundo y el tercer párrafo."],
        [
            "Este texto no trae clave oficial; estas son las respuestas, que se justifican con el texto en los pasos siguientes: 4 «el autor diría que está equivocado», 5 «partir de algunas ideas aceptadas previamente».",
            "Pregunta 4: el autor afirma que el descubrimiento «no fue un producto de la inducción, sino de deducciones lógicas y transformaciones de las ideas existentes». Un historiador que hable de inducción contradice al autor, que diría que está equivocado. Las otras opciones dan por bueno al historiador (está en lo correcto, hace un aporte, comprende la obra). (Omitimos la quinta del original, «debería mencionar también a Galileo», que no responde a la cuestión.)",
            "Pregunta 5: el rasgo de «todo gran avance en la ciencia» es «la creación de algo nuevo mediante la transformación de las nociones existentes»: hay que partir de ideas ya aceptadas.",
            "Descartes: la inducción queda excluida («No fue un producto de la inducción»); los destellos geniales también («no fue el resultado de un aislado destello del genio»); y «desde las innovaciones más simples hasta las revoluciones más dramáticas» describe el alcance de los avances, no su punto de partida. (Omitimos «alejarse de los problemas considerados cruciales», que no tiene apoyo en el texto.)",
        ],
    ),
    # ---- Texto 8: Leonardo ----
    _p(
        TC, "cl8-leonardo-a", 2, "CLyRP · Práctica de lectura, texto 8",
        "Texto 8: los dibujos de Leonardo (preguntas 1 a 3)",
        _enc(8, "1 a 3", T8),
        [
            _q("Pregunta 1. Fundamentalmente, el tema central gira en torno a", [
                "Dos muestras en Edimburgo y Venecia que rescatan dibujos de Da Vinci.",
                "La forma meticulosa en que Leonardo da Vinci dibujó la anatomía humana.",
                "Un conjunto de dibujos inéditos que fueron hechos por Leonardo da Vinci.",
                "La armonía alcanzada por Da Vinci en la representación del cuerpo humano.",
            ], 0),
            _q("Pregunta 2. En el texto, la palabra INGENIO adquiere el sentido de", [
                "Prodigio.", "Talento.", "Facultad.", "Artefacto.",
            ], 3),
            _q("Pregunta 3. Se puede colegir del texto que la notable fama de Da Vinci como creador pictórico", [
                "Empieza cuando todos sus dibujos se exhibieron en Italia.",
                "Es equiparable a su habilidad como organizador de fiestas.",
                "Fue escasamente promovida por el propio artista.",
                "Se inicia con la exposición de sus dibujos en Edimburgo.",
            ], 2),
        ],
        [
            "El primer párrafo anuncia de qué va todo el texto; el segundo y el tercero describen una muestra cada uno.",
            "INGENIO aparece al final: «proyectos de armas e ingenios militares». ¿Se puede dibujar un talento?",
        ],
        [
            "Este texto no trae clave oficial; estas son las respuestas, que se justifican con el texto en los pasos siguientes: 1 «dos muestras en Edimburgo y Venecia…», 2 «artefacto», 3 «fue escasamente promovida por el propio artista».",
            "Pregunta 1: «Dos exposiciones paralelas rescatan los extraordinarios dibujos… de Leonardo da Vinci», y luego un párrafo para cada una. La anatomía es el tema de una sola muestra (Edimburgo); no todos los dibujos son inéditos (en Venecia hay 27 hojas prestadas por museos); la armonía del cuerpo (Hombre de Vitruvio) es un detalle de la muestra de Venecia.",
            "Pregunta 2: «proyectos de armas e ingenios militares»: un ingenio es una máquina o artificio → **artefacto**. Prodigio, talento y facultad son el otro sentido de ingenio (la capacidad mental), que no sirve aquí: se habla de cosas que se proyectan y se dibujan, en plural y junto a «armas». (Omitimos «ilusión».)",
            "Pregunta 3: Leonardo «en raras ocasiones se presentaba en las cortes como un pintor, sino más bien como un ingeniero, arquitecto, músico…»: él casi no promovía su faceta de pintor, o sea, la promovió escasamente. Las otras son falsas: el texto no dice que «todos» sus dibujos se exhibieran en Italia ni que su fama empezara ahí o en Edimburgo (son muestras actuales; además los estudios anatómicos estuvieron inéditos siglos) y no compara su pintura con la organización de fiestas. (Omitimos «solo fue eclipsada por su fama como diseñador de armas», tampoco dicho.)",
        ],
    ),
    _p(
        TC, "cl8-leonardo-b", 3, "CLyRP · Práctica de lectura, texto 8",
        "Texto 8: los dibujos de Leonardo (preguntas 4 a 6)",
        _enc(8, "4 a 6", T8),
        [
            _q("Pregunta 4. ¿Cuál es la idea principal del texto?", [
                "Los dibujos exhibidos en las dos muestras artísticas están en lugares que cuentan con condiciones ambientales rigurosas, dada la notoria fragilidad de la muestra.",
                "Dos muestras, una en el Palacio de Holyroodhouse (Edimburgo) y otra en las Galerías de la Academia (Venecia), rescatan dibujos de Leonardo da Vinci.",
                "Leonardo da Vinci. El hombre universal presenta al público un total de 25 obras que nunca antes han sido mostradas y que se conservan desde 1822.",
                "Leonardo da Vinci: la mecánica del hombre examina los innovadores dibujos del pintor y demuestra que es uno de los más destacados anatomistas de la historia.",
            ], 1),
            _q("Pregunta 5. Resulta incompatible con el desarrollo textual afirmar que la muestra que se realiza en Venecia", [
                "Se llevará a cabo de forma sostenida y perpetua.",
                "Se realizará solamente hasta el 1 de diciembre.",
                "Presenta esbozos de armas e ingenios militares.",
                "Permite admirar dibujos de botánica y retratos.",
            ], 0),
            _q("Pregunta 6. Si Leonardo da Vinci hubiese carecido de interés respecto de la anatomía humana, posiblemente", [
                "El valor ecuménico de su legado artístico como pintor renacentista se vería notoriamente mellado en la actualidad.",
                "Sus dibujos inéditos relacionados con sus proyectos geométricos, batallas y material de guerra permanecerían ocultos por mucho tiempo.",
                "Jamás se hubiera presentado ante las cortes como arquitecto y diseñador de artefactos de guerra, entre otros productos creativos.",
                "La caracterización fidedigna de la cirrosis hepática y el estrechamiento arterial padecidos por un anciano no habría sido realizada por Leonardo.",
            ], 3),
        ],
        [
            "La idea principal tiene que valer para las dos muestras, no para una sola.",
            INCOMP,
            HIPO,
        ],
        [
            "Este texto no trae clave oficial; estas son las respuestas, que se justifican con el texto en los pasos siguientes: 4 «Dos muestras… rescatan dibujos de Leonardo», 5 «se llevará a cabo de forma sostenida y perpetua», 6 «la caracterización de la cirrosis hepática… no habría sido realizada por Leonardo».",
            "Pregunta 4: el texto desarrolla las dos exposiciones; la opción que las nombra a ambas es la idea principal. La de las condiciones ambientales es un detalle (y en el texto se refiere sobre todo a la muestra veneciana); la de las 25 obras inéditas habla solo de Venecia; la de los dibujos anatómicos, solo de Edimburgo. (Omitimos la del Hombre de Vitruvio, otro detalle.)",
            "Pregunta 5: incompatible: la muestra veneciana «se puede visitar hasta el 1 de diciembre» y esos dibujos «sólo se pueden exponer públicamente una vez durante una generación»: no es perpetua. Las demás están en el texto: la fecha de cierre, «proyectos de armas e ingenios militares», «dibujos de botánica… retratos de hombres». (Omitimos «incluye dibujos prestados de museos italianos», también dicho.)",
            "Pregunta 6: la descripción de la cirrosis y del estrechamiento de las arterias sale de su examen post mortem de «un hombre de 100 años», o sea, de sus estudios anatómicos: sin interés por la anatomía, Leonardo no la habría hecho (la opción no afirma que nadie más la habría hecho nunca, cosa que el texto no permite saber). Su fama como pintor no dependió de esos estudios, que «permanecieron inéditos durante varios siglos»; los dibujos de geometría, batallas y armas, y su presentación ante las cortes como ingeniero o arquitecto, no tienen relación con la anatomía. (Omitimos la de los museos italianos sin muestras, que tampoco se sigue.)",
        ],
    ),
    # ---- Texto 9: el bus ----
    _p(
        TC, "cl9-bus-a", 3, "CLyRP · Práctica de lectura, texto 9",
        "Texto 9: viaje en bus (preguntas 1 a 3)",
        _enc(9, "1 a 3", T9),
        [
            _q("Pregunta 1. En el texto anterior predomina:", [
                "La descripción del entorno material de una ciudad a partir de un viaje en bus por el centro de ella.",
                "La narración del viaje que alguien realiza en un bus por el centro de una ciudad y la presentación de sus reflexiones.",
                "La caracterización de una ciudad a partir de la relación existente entre el transporte público y el individuo.",
                "La presentación de una teoría sobre la forma de descubrir la falsedad dentro de una ciudad.",
            ], 1),
            _q("Pregunta 2. Otro posible título para el texto anterior sería:", [
                "La ciudad y el transporte terrestre.",
                "Caos y transporte.",
                "La ciudad se puede leer.",
                "El transporte público.",
            ], 2),
            _q("Pregunta 3. El enunciado «un simulacro es la suplantación de lo real por los signos de lo real» se introduce en el texto con la intención de:", [
                "Argumentar la idea de que leer la ciudad es leernos a nosotros mismos.",
                "Definir el significado de simulacro partiendo de un viaje en bus por la ciudad.",
                "Proponer un método para leer la ciudad a partir de los planteamientos de Baudrillard.",
                "Discutir la concepción de Baudrillard en torno a la posibilidad de hallar la ciudad.",
            ], 0),
        ],
        [
            "Fijate quién habla (primera persona), qué hechos se suceden y qué piensa el narrador mientras tanto.",
            "Para la 3, leé lo que viene justo después de la cita de Baudrillard.",
        ],
        [
            "Este texto no trae clave oficial; estas son las respuestas, que se justifican con el texto en los pasos siguientes: 1 la narración con reflexiones, 2 «La ciudad se puede leer», 3 «argumentar la idea de que leer la ciudad es leernos a nosotros mismos».",
            "Pregunta 1: hay un narrador en primera persona («voy en un bus»), una sucesión de hechos (oscurece, el bus acelera, el semáforo, arrancan) y reflexiones («¿Somos los signos de lo real?»). La descripción de la ciudad es mínima (incluso «la ciudad desaparece»); no se caracteriza la ciudad por el transporte; Baudrillard se cita, no se presenta una teoría para descubrir falsedades.",
            "Pregunta 2: el texto no trata del transporte (es solo el escenario), sino de interpretar lo que se ve desde la ventanilla: signos, reflejos, el propio narrador en el otro bus. «La ciudad se puede leer» apunta a esa lectura. «La ciudad y el transporte terrestre», «Caos y transporte» y «El transporte público» se quedan con el escenario; la congestión es un detalle del arranque.",
            "Pregunta 3: tras la cita, el narrador concluye: «No hay lo real, tan sólo la ventanilla que nos refleja. Nosotros, los pasajeros, suplantamos la realidad, somos el paisaje». La usa para sostener que, al mirar la ciudad, nos vemos a nosotros mismos. No la define a partir del viaje (es una cita de Baudrillard), no propone un método y no la discute: la aplica.",
        ],
    ),
    _p(
        TC, "cl9-bus-b", 2, "CLyRP · Práctica de lectura, texto 9",
        "Texto 9: viaje en bus (preguntas 4 a 6)",
        _enc(9, "4 a 6", T9),
        [
            _q("Pregunta 4. Del enunciado «Nosotros, los pasajeros, suplantamos la realidad, somos el paisaje» se puede concluir que:", [
                "Los individuos que componen la masa son sólo objetos para ser observados.",
                "Siempre que se hace parte de algo colectivo, es inevitable suplantar la realidad.",
                "El concepto de paisaje se fundamenta en la inexistencia de la individualidad.",
                "El objeto que constituye la realidad es el mismo sujeto que la observa.",
            ], 3),
            _q("Pregunta 5. Las expresiones «Serán amigas -pienso-, quizás compañeras de trabajo», ubicadas en el tercer párrafo, se han impreso en letra cursiva con la intención de:", [
                "Introducir comentarios que el autor del texto hace para sí mismo.",
                "Formular interrogantes del autor del texto hacia sus lectores.",
                "Señalar diálogos entre el autor y el narrador del texto.",
                "Evidenciar la participación de uno de los personajes en el texto.",
            ], 0),
            _q("Pregunta 6. Cuando el texto habla de comunidades apáticas e indiferentes, se refiere a:", [
                "Las personas que transitan por el centro de la ciudad.",
                "Todos los individuos que observan críticamente la ciudad.",
                "Todos los seres que pertenecemos a la ciudad.",
                "Otros usuarios del transporte público en la ciudad.",
            ], 3),
        ],
        [
            "En la 4: los pasajeros miran por la ventanilla… y lo que ven es su propio reflejo. ¿Quién mira y qué es lo mirado?",
            "En la 5, la palabra clave entre guiones es «pienso».",
        ],
        [
            "Este texto no trae clave oficial; estas son las respuestas, que se justifican con el texto en los pasos siguientes: 4 «el objeto que constituye la realidad es el mismo sujeto que la observa», 5 «comentarios que el autor hace para sí mismo», 6 «otros usuarios del transporte público».",
            "Pregunta 4: los pasajeros, que miran el paisaje, pasan a ser el paisaje (lo que se ve en la ventanilla es su reflejo); al final el narrador incluso se ve a sí mismo en el otro bus. Observador y observado coinciden. No son «sólo objetos» (también observan); «siempre… es inevitable» generaliza más allá del texto; y nada dice que el paisaje se funde en la «inexistencia de la individualidad».",
            "Pregunta 5: el «-pienso-» marca que es un pensamiento del narrador, una conjetura para sí mismo sobre las dos señoras. No es una pregunta a los lectores, no hay diálogo («no hablan entre ellas»), y las señoras no participan: solo son miradas.",
            "Pregunta 6: el texto habla de «la indiferente comunidad que comparte el viaje» y de «otros pasajeros de otra comunidad igualmente apática»: son los usuarios de los buses. La multitud de los andenes no recibe esos adjetivos; «observan críticamente» es lo contrario de apáticos; y «todos los seres que pertenecemos a la ciudad» generaliza más allá de lo que dice el texto.",
        ],
    ),
    # ---- Texto 10: inteligencia artificial (consignas abiertas convertidas) ----
    _p(
        TC, "cl10-ia-sintesis", 2, "CLyRP · Práctica de lectura, texto 10 (consignas 3 y 4b)",
        "Texto 10: inteligencia artificial",
        "Las consignas originales piden: realizar las 3 fases de lectura comprensiva, subrayar las ideas principales, "
        "elaborar una síntesis y responder «¿Qué es y cómo se desarrolla el Google I/O?». En la app, la síntesis y "
        "la pregunta del Google I/O se convierten en opción múltiple.\n\n**Texto 10**\n\n" + T10,
        [
            _q("a) ¿Cuál es la mejor síntesis del texto?", [
                "Para Spontón, la IA actual todavía es limitada, pero ya resulta útil (por ejemplo, para personalizar la publicidad) y empieza a participar en tareas creativas; su presencia junto a las personas crecerá, en una convivencia de humanos y máquinas que debe desarrollarse con responsabilidad y ética.",
                "Spontón sostiene que en el futuro las máquinas reemplazarán a los humanos en las tareas creativas, como muestra el robot que hizo de DJ en el Google I/O.",
                "El texto explica cómo Rappi y AdsMovil usan sus bases de datos para enviar publicidad «uno a uno» a los celulares de sus clientes.",
                "Según Spontón, la IA ya es multitarea y supera a la inteligencia humana en casi todas las dimensiones.",
            ], 0),
            _q("b) Según el texto, ¿cómo se desarrolló la apertura del Google I/O?", [
                "Un DJ humano pasaba música asesorado por un robot que, con una cámara, analizaba los movimientos de baile del público y le recomendaba qué canciones poner.",
                "Un robot reemplazó al DJ y eligió la música a partir de una base de datos con los gustos de los invitados.",
                "Los invitados votaban desde sus celulares las canciones que el DJ debía poner.",
                "Spontón presentó un robot que componía canciones originales para el público.",
            ], 0),
        ],
        [
            "Una síntesis tiene que cubrir todo el texto (qué puede la IA hoy, para qué sirve, hacia dónde va) sin contradecirlo.",
            "Para b), releé el párrafo que empieza «En el Google I/O de este año…»: ¿quién elegía las canciones y quién lo ayudaba?",
        ],
        [
            "Ideas principales: la IA de hoy es «muy bruta» y hace labores «muy específicas»; ya es útil (predecir compras, publicidad «uno a uno»); empieza a ayudar a crear; su acompañamiento será «más protagónico con el pasar de los años», en un mundo que no es «de solo máquinas o solo humanos», y su desarrollo pide «mucha responsabilidad y ética».",
            "a) La opción «Para Spontón, la IA actual todavía es limitada, pero ya resulta útil…» reúne esas ideas con palabras propias: es la síntesis.",
            "La de que «las máquinas reemplazarán a los humanos en las tareas creativas» contradice al texto: Spontón dice que no concibe «un mundo de solo máquinas o solo humanos», y en el Google I/O el DJ era un músico asesorado por un robot, no un robot. La de Rappi y AdsMovil es un ejemplo de un solo párrafo. La de que la IA «ya es multitarea y supera a la inteligencia humana» invierte el texto: para ser multitarea a la IA «le hacen falta años de desarrollo» y Spontón dice que en algunas dimensiones «siempre seremos mejores».",
            "b) «Este músico, mientras ponía las canciones…, era asesorado por un robot que, por medio de una cámara, analizaba los movimientos de baile… [y] le recomendaba qué canciones poner». El robot no reemplazó al DJ, no hubo votación por celular y nadie compuso canciones.",
            "La parte de «¿qué es el Google I/O?» no se pudo convertir: el texto solo dice que tiene una «conferencia de apertura» con invitados (es la conferencia anual de Google para desarrolladores, pero eso no está en el texto).",
        ],
    ),
    # ---- Resolución de Problemas: Comprensión lectora 1 ----
    _p(
        TC, "rp-memoria-cerebro", 2, "CLyRP · Resolución de Problemas, Comprensión lectora 1, act. C",
        "Memoria del cerebro y de la PC",
        "Comprensión de textos mediante preguntas de elección múltiple. Realiza la lectura del texto y elegí la mejor respuesta.\n\n" + MEMORIA,
        [
            _q("1. Un ordenador y nuestro cerebro, ¿se asemejan en la capacidad de memoria?", [
                "Ambas máquinas son iguales.",
                "La información se guarda en un disco duro.",
                "Nuestro cerebro guarda más gigabytes que cualquier PC.",
                "La capacidad memorística es guardada en diferentes sitios.",
            ], 2),
        ],
        [
            "La pregunta es sobre la capacidad (cuánto guardan), no sobre cómo se guarda la información.",
            "Una opción puede ser cierta según el texto y aun así no responder la pregunta.",
        ],
        [
            "Hay que elegir la opción que responda a la pregunta (¿se parecen en capacidad?) y que el texto respalde.",
            "«Nuestro cerebro guarda más gigabytes que cualquier PC»: el texto dice que «los neurólogos aseguran que nuestra cabeza guarda más gigabytes que los que puede albergar el ordenador más potente». Es la respuesta: no se asemejan, el cerebro guarda más.",
            "«Ambas máquinas son iguales» es falsa: el texto dice que están «organizados de formas muy distintas».",
            "«La información se guarda en un disco duro» y «La capacidad memorística es guardada en diferentes sitios» son ciertas, pero cada una describe solo cómo guarda uno de los dos (la PC o el cerebro): no comparan su capacidad.",
        ],
    ),
    _p(
        TC, "rp-pilas-litio-a", 1, "CLyRP · Resolución de Problemas, Comprensión lectora 1, act. D",
        "Pilas de litio: V, F o no mencionado (1 a 3)",
        "Comprensión de textos mediante preguntas «Verdadero/Falso». Para cada afirmación, indicá si es V (verdadero "
        "según el texto), F (falso según el texto) o NM (no ha sido mencionado).\n\n" + LITIO,
        [
            _q("1. Una batería de litio posee dos electrodos.", VFNM, 0),
            _q("2. El litio es un elemento químico.", VFNM, 2),
            _q("3. Los electrodos del litio: uno es positivo y el otro negativo.", VFNM, 0),
        ],
        [
            "Juzgá solo con lo que dice el texto, no con lo que sabés de química: si el texto no lo dice, es NM aunque sea cierto.",
        ],
        [
            "Criterio: V si el texto lo afirma; F si el texto dice lo contrario; NM si el texto no dice nada sobre eso (aunque en la realidad sea verdadero).",
            "1. Verdadero: «Una batería de litio posee dos electrodos».",
            "2. No mencionado: el texto habla de «la propia química de la pila» y de «iones de litio», pero nunca dice que el litio sea un elemento químico (aunque lo sea).",
            "3. Verdadero: «dos electrodos –uno positivo y otro negativo–».",
        ],
    ),
    _p(
        TC, "rp-pilas-litio-b", 1, "CLyRP · Resolución de Problemas, Comprensión lectora 1, act. D",
        "Pilas de litio: V, F o no mencionado (4 y 5)",
        "Comprensión de textos mediante preguntas «Verdadero/Falso». Para cada afirmación, indicá si es V (verdadero "
        "según el texto), F (falso según el texto) o NM (no ha sido mencionado).\n\n" + LITIO,
        [
            _q("4. Cuando la batería se está descargando, el ion de litio se dirige del electrodo positivo al negativo.", VFNM, 1),
            _q("5. El ion es una partícula cargada eléctricamente.", VFNM, 2),
        ],
        [
            "En la 4, compará el sentido del movimiento con el de la oración del texto sobre la descarga.",
            "Juzgá solo con lo que dice el texto: si no lo dice, es NM aunque sea cierto.",
        ],
        [
            "Criterio: V si el texto lo afirma; F si el texto dice lo contrario; NM si el texto no lo trata.",
            "4. Falso: el texto dice que, al descargarse, «el ion de litio se dirige del electrodo negativo… al positivo»; la afirmación invierte el sentido (de positivo a negativo es lo que pasa en la carga: «se produce el camino inverso»).",
            "5. No mencionado: el texto usa la palabra «ion» pero nunca define qué es; que sea una partícula con carga eléctrica es cierto en química, pero no está en el texto.",
        ],
    ),
    # ======================================================================================================
    # cl-organizadores: cuadro sinóptico y cuadro comparativo
    # ======================================================================================================
    _p(
        OR, "sinoptico-prehistoria", 2, "CLyRP · Práctica de lectura, cuadro sinóptico",
        "Cuadro sinóptico: la Prehistoria",
        "Realiza una lectura comprensiva y posteriormente elabora un cuadro sinóptico (en papel). Después usá tu "
        "cuadro para responder.\n\n" + PREHIST,
        [
            _q("a) En el cuadro sinóptico de «La Prehistoria», ¿cuál es la primera división (la primera llave)?", [
                "Edad de piedra y edad de los metales.",
                "Paleolítico, mesolítico y neolítico.",
                "Edad de cobre, edad de bronce y edad de hierro.",
                "Pueblos nómadas y pueblos sedentarios.",
            ], 0),
            _q("b) ¿En qué casillero del cuadro van el nacimiento de la agricultura y el paso al sedentarismo?", [
                "Paleolítico.", "Mesolítico.", "Neolítico.", "Edad de bronce.",
            ], 2),
            _q("c) ¿Qué rasgo corresponde a la edad de bronce?", [
                "Aleación de cobre y estaño; nacen las culturas de Mesopotamia.",
                "El cobre es el primer metal utilizado por los seres humanos.",
                "Comenzó en Oriente hace unos 3.200 años.",
                "El hombre pulimenta la piedra y fabrica cerámica.",
            ], 0),
        ],
        [
            "Un cuadro sinóptico va de lo general a lo particular: Prehistoria → edades → periodos → características.",
            "Buscá la oración que dice en cuántas «grandes etapas o edades» se divide la prehistoria.",
        ],
        [
            "Estructura del cuadro: **Prehistoria** (desde el inicio de la evolución humana hasta la escritura; la estudia la arqueología) → { **Edad de piedra** → { paleolítico, mesolítico, neolítico } ; **Edad de los metales** → { cobre, bronce, hierro } }.",
            "a) «La prehistoria suele dividirse en dos grandes etapas o edades: la edad de piedra y la edad de los metales». Esa es la primera llave. Paleolítico/mesolítico/neolítico y cobre/bronce/hierro son subdivisiones de cada edad (segundo nivel); nómadas y sedentarios son características, no una división del texto.",
            "b) En el neolítico «nació la agricultura… el ser humano dejó de ser nómada… y se hizo sedentario, apareciendo así los primeros poblados». En el paleolítico y el mesolítico seguían cazando y recolectando; la edad de bronce ya es de los metales.",
            "c) Edad de bronce: «después de aprender a alear (mezclar) el cobre con otro metal: el estaño. Las antiguas culturas de Mesopotamia nacieron y se desarrollaron durante la edad de bronce». El primer metal es el rasgo de la edad de cobre; «comenzó en Oriente hace unos 3.200 años» es de la edad de hierro; pulir la piedra y la cerámica son del neolítico.",
            "Nota: en el texto del material hay erratas evidentes que corregimos («un pruebo vive en la prehistoria hasta que escribe» → «un pueblo…», «el gen 4 cambio» → «el gran cambio», «la edad de los materiales» → «la edad de los metales»).",
        ],
    ),
    _p(
        OR, "comparativo-lenguaje", 1, "CLyRP · Práctica de lectura, cuadro comparativo",
        "Cuadro comparativo: lenguaje, lengua, dialecto y habla",
        "Realiza una lectura comprensiva y posteriormente elabora un cuadro comparativo, completando:\n\n"
        "| | Lenguaje | Lengua | Dialecto | Habla |\n|---|---|---|---|---|\n"
        "| Definición | … | … | … | … |\n| Características | … | … | … | … |\n\n" + LENGUA,
        [
            _q("a) ¿Qué va en el casillero «Definición» de la columna **Lenguaje**?", [
                "Capacidad de comunicarse mediante signos, orales o escritos.",
                "Sistema lingüístico utilizado por una comunidad de hablantes.",
                "Variante de una lengua común, sin fuerte diferenciación y con delimitación geográfica.",
                "Utilización que cada individuo hace de la lengua.",
            ], 0),
            _q("b) ¿Qué va en el casillero «Definición» de la columna **Dialecto**?", [
                "Capacidad de comunicarse mediante signos, orales o escritos.",
                "Sistema lingüístico utilizado por una comunidad de hablantes.",
                "Variante de una lengua común, sin fuerte diferenciación y con delimitación geográfica.",
                "Utilización que cada individuo hace de la lengua.",
            ], 2),
            _q("c) ¿Qué va en el casillero «Características» de la columna **Habla**?", [
                "Cambia con frecuencia por el uso; sin hablantes no habría lengua.",
                "Evoluciona muy lentamente; tiene gramática, ortografía y tradición literaria propias.",
                "Normalmente tiene una delimitación geográfica muy concreta.",
                "Presenta muchísimas manifestaciones distintas, como las lenguas o idiomas.",
            ], 0),
        ],
        [
            "Cada concepto tiene su párrafo con guion: la primera oración es la definición y lo que sigue, las características.",
            "Para c), fijate en la última oración del texto, que compara lengua y habla.",
        ],
        [
            "Cuadro completo. Lenguaje: capacidad de comunicarse mediante signos orales o escritos; tiene muchísimas manifestaciones (las lenguas). Lengua: sistema lingüístico de una comunidad de hablantes (= idioma); se distingue por su escritura, tiene gramática y ortografía propias y tradición literaria, y evoluciona muy lentamente.",
            "Dialecto: variante de una lengua común, sin fuerte diferenciación; normalmente con delimitación geográfica muy concreta. Habla: uso que cada individuo hace de la lengua; cambia con frecuencia por el uso, y sin hablantes no habría lengua (y al revés).",
            "a) «El lenguaje es la capacidad de poder establecer comunicación mediante signos, ya sean orales o escritos» → «Capacidad de comunicarse mediante signos, orales o escritos». Las otras tres son las definiciones de lengua, dialecto y habla.",
            "b) «Un dialecto es una variante lingüística de una lengua común, pero sin una fuerte diferenciación, que normalmente tiene una delimitación geográfica muy concreta» → «Variante de una lengua común, sin fuerte diferenciación y con delimitación geográfica».",
            "c) «El habla cambia con frecuencia por el uso» y «si no hubiera hablantes, no habría lengua» → «Cambia con frecuencia por el uso; sin hablantes no habría lengua». «Evoluciona muy lentamente…» es de la lengua; la delimitación geográfica es del dialecto; las muchas manifestaciones, del lenguaje.",
        ],
    ),
]
