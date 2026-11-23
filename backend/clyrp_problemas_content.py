"""Comprensión Lectora y Resolución de Problemas (Ingreso UNCuyo 2027): temas 6 a 11.

Seis nodos de la materia `comprension-problemas` que siguen a `cl-logica-enunciados`:
  - Razonamiento lógico: acertijos de orden, asignación y verdad
  - Lectura de tablas y gráficos
  - Estrategias de resolución de problemas (Pólya)
  - Problemas de porcentajes y fracciones
  - Problemas de edades y sistemas de ecuaciones
  - Problemas de geometría: ángulos, áreas y volúmenes

Siguen el programa del módulo (Unidades 2 y 3), el TP N.º 3 de Resolución de Problemas y el
libro "Resolución de Problemas" (EDIUNC, 2002), con sus etapas: Comprendiendo el problema,
Planificando y ejecutando, Revisando. La materia no tiene laboratorio.
"""

from __future__ import annotations

CLYRP_PROBLEMAS_NODES: list[dict] = [
    # ==================== RAZONAMIENTO LÓGICO ====================
    {
        "slug": "cl-razonamiento-logico",
        "title": "Razonamiento lógico: acertijos de orden, asignación y verdad",
        "summary": "Ordenar por comparaciones, asignar con tablas de doble entrada, ubicar en línea y en ronda, resolver verdades y mentiras y sumas con letras, sacando los datos implícitos y verificando.",
        "prerequisites": ["cl-logica-enunciados"],
        "insert_after": "cl-logica-enunciados",
        "metadata": {"section": "Lenguaje y lógica", "est_minutes": 30},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Encadenar comparaciones para hallar al más lento",
                "prompt": "Mateo corre más rápido que Leo. Iara corre más lento que Leo. Sol corre más rápido que Mateo. ¿Quién es el más lento de los cuatro?",
                "answer": "Iara: escribiendo cada frase como desigualdad de velocidades queda M > L, I < L y S > M. Encadenadas: I < L < M < S. Iara está en el extremo de los más lentos.",
                "hints": [
                    "Pasá cada frase a una desigualdad con iniciales (M > L, …).",
                    "Ubicá a los cuatro sobre una línea, del más lento al más rápido.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Iara", "Leo", "Mateo", "Sol"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Qué se puede asegurar con comparaciones incompletas",
                "prompt": "Bruno pesa más que Ciro y también pesa más que Dante. ¿Qué se puede asegurar con certeza?",
                "answer": "Que Bruno es el más pesado de los tres. Entre Ciro y Dante no hay ninguna comparación, así que cualquiera de los dos puede pesar más (o pueden pesar lo mismo): inventar ese orden es agregar un dato que el enunciado no da.",
                "hints": ["Dibujá las dos relaciones: ¿hay alguna flecha entre Ciro y Dante?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Bruno es el más pesado de los tres",
                            "Ciro pesa más que Dante",
                            "Dante pesa más que Ciro",
                            "Ciro y Dante pesan lo mismo",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Sacar un dato implícito de una pista",
                "prompt": "En un acertijo de asignar profesiones aparece esta pista: “El ingeniero juega al pádel todos los sábados con Rocío”. ¿Qué dato implícito aporta para la tabla?",
                "answer": "Rocío no es la ingeniera: nadie juega al pádel consigo mismo. Ese dato no está escrito, pero se deduce del contexto y se marca con una ✗ en la casilla Rocío–ingeniero.",
                "hints": ["Preguntate si una misma persona puede ocupar los dos lugares de la frase."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Rocío no es la ingeniera",
                            "Rocío es la ingeniera",
                            "Rocío juega mejor al pádel que el ingeniero",
                            "No aporta nada a la tabla",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Cruces que impone un acierto en una tabla de asignación",
                "prompt": "En una tabla de doble entrada asignás 4 personas a 4 oficios: cada persona tiene un solo oficio y cada oficio es de una sola persona. Marcás un ✓ en una casilla. ¿Cuántas casillas más quedan con ✗ automáticamente por ese ✓? Respondé solo con el número.",
                "answer": "6: las otras 3 casillas de su fila (esa persona ya tiene oficio) y las otras 3 de su columna (ese oficio ya tiene dueño).",
                "hints": ["Pensá por separado en la fila y en la columna del ✓."],
                "payload": {"check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Asignar instrumentos con una tabla de doble entrada",
                "prompt": "Fede, Gael y Hugo tocan guitarra, piano y batería, un instrumento distinto cada uno. Pistas: Hugo no toca la batería. El pianista y Fede son primos. Hugo no toca el piano. ¿Qué toca Fede?",
                "answer": "Batería. Dato implícito: Fede no es el pianista (no es primo de sí mismo). En la columna piano quedan ✗ en Fede y en Hugo, así que el piano es de Gael. Hugo no toca piano ni batería: toca la guitarra. A Fede le queda la batería. Verificación: las tres pistas se cumplen.",
                "hints": [
                    "La segunda pista esconde una negación: ¿puede Fede ser el pianista?",
                    "Mirá la columna del piano: ¿cuántas casillas quedan libres?",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Guitarra", "Piano", "Batería"],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ubicar vecinos en una hilera de casas",
                "prompt": "En una hilera de cinco casas numeradas del 1 al 5, de izquierda a derecha, viven P, Q, R, S y T (una familia por casa). R vive en la casa del medio. P vive en un extremo, a la izquierda de R, y S vive al lado de P. Q no vive al lado de R. ¿En qué casa vive T? Respondé solo con el número.",
                "answer": "4: R está en la 3. P está en un extremo y a la izquierda de R, así que P está en la 1 y S, que vive al lado, en la 2. Q no puede estar en la 2 ni en la 4 (son las vecinas de R), y la 1 está ocupada: Q va en la 5. A T le queda la 4.",
                "hints": [
                    "Empezá por los datos fijos: R en la 3 y P en un extremo.",
                    "Las casas vecinas de la 3 son la 2 y la 4.",
                ],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Ubicar personas en una mesa redonda de seis",
                "prompt": "Abril, Bruno, Cami, Dante, Ema y Fran se sientan en una mesa redonda de seis sillas igualmente espaciadas. Abril está frente a Dante. Bruno y Fran se sientan a los dos lados de Abril. Cami se sienta al lado de Bruno y también al lado de Dante. ¿Quién está frente a Bruno?",
                "answer": "Ema. Fijá a Abril en una silla: Dante queda en la opuesta. Bruno y Fran ocupan las dos sillas pegadas a Abril. Entre Bruno y Dante hay una sola silla, y es la de Cami. La silla que queda libre está entre Dante y Fran, y es la de Ema. En una mesa de seis, frente a Bruno está la silla ubicada entre Dante y Fran: la de Ema.",
                "hints": [
                    "En una ronda conviene fijar primero a una persona; así no contás dos veces la misma ubicación girada.",
                    "Dibujá un hexágono con seis sillas y completá con las pistas en orden.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["Ema", "Dante", "Cami", "Fran"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Encontrar el premio cuando un solo cartel dice la verdad",
                "prompt": "Hay tres cajas y una sola tiene premio. Caja 1: “El premio está acá”. Caja 2: “El premio no está acá”. Caja 3: “El premio no está en la caja 1”. Se sabe que exactamente uno de los tres carteles es verdadero. ¿Dónde está el premio?",
                "answer": "En la caja 2. Se prueba cada hipótesis: si el premio estuviera en la 1, serían verdaderos los carteles 1 y 2 (dos verdades); si estuviera en la 3, serían verdaderos el 2 y el 3 (dos verdades). Solo con el premio en la 2 hay exactamente un cartel verdadero: el 3.",
                "hints": [
                    "Suponé que el premio está en la caja 1 y contá cuántos carteles resultan verdaderos.",
                    "Repetí con la caja 2 y la caja 3: descartá las hipótesis que contradicen el dato.",
                ],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["En la caja 1", "En la caja 2", "En la caja 3"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Suma con letras de un dígito repetido tres veces",
                "prompt": "Cada letra representa una cifra y letras distintas son cifras distintas. En la cuenta A + A + A = BA, donde BA es un número de dos cifras (B decenas y A unidades), ¿cuánto vale A? Respondé solo con el número.",
                "answer": "5: la cuenta dice 3·A = 10·B + A, o sea 2·A = 10·B, A = 5·B. Como A es una cifra y B no puede ser 0 (BA tiene dos cifras), B = 1 y A = 5. Verificación: 5 + 5 + 5 = 15.",
                "hints": [
                    "BA no es B por A: vale 10·B + A.",
                    "Despejá A en función de B y probá qué valores de B dan una cifra.",
                ],
                "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Primera cifra cuando una suma gana una cifra",
                "prompt": "En una suma con letras, sumás dos números de tres cifras y el resultado tiene cuatro cifras. ¿Qué cifra tiene que ser la primera del resultado? Respondé solo con el número.",
                "answer": "1: la suma más grande posible es 999 + 999 = 1998, así que cualquier resultado de cuatro cifras está entre 1000 y 1998 y empieza con 1. Es la llave de muchos problemas de criptoaritmética.",
                "hints": ["Calculá la suma más grande posible de dos números de tres cifras."],
                "payload": {"check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    # ==================== TABLAS Y GRÁFICOS ====================
    {
        "slug": "cl-tablas-graficos",
        "title": "Lectura de tablas y gráficos",
        "summary": "Leer tablas de doble entrada y gráficos de barras, de torta y de líneas, calcular totales, porcentajes y variaciones, separar datos útiles de accesorios y detectar conclusiones inválidas y escalas engañosas.",
        "prerequisites": ["cl-lenguaje-simbolico"],
        "insert_after": "cl-razonamiento-logico",
        "metadata": {"section": "Lenguaje y lógica", "est_minutes": 30},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Porcentaje dentro de una columna de una tabla de doble entrada",
                "prompt": "Ingresantes de una facultad según carrera y turno:\n| Carrera | Mañana | Tarde | Total |\n|---|---|---|---|\n| Civil | 30 | 18 | 48 |\n| Industrial | 25 | 27 | 52 |\n| Mecánica | 15 | 15 | 30 |\n| Total | 70 | 60 | 130 |\n¿Qué porcentaje de los ingresantes del turno tarde estudia Civil? Respondé solo con el número (en %).",
                "answer": "30 %: la base es el total del turno tarde (60), no el total general. 18/60 · 100 = 30 %.",
                "hints": [
                    "“De los ingresantes del turno tarde” fija la base: buscá el total de esa columna.",
                    "Porcentaje = parte/total · 100.",
                ],
                "payload": {"check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": "%"}},
            },
            {
                "item_type": "worked_example",
                "title": "Elegir la base correcta en una tabla de doble entrada",
                "prompt": "Con la misma tabla de ingresantes:\n| Carrera | Mañana | Tarde | Total |\n|---|---|---|---|\n| Civil | 30 | 18 | 48 |\n| Industrial | 25 | 27 | 52 |\n| Mecánica | 15 | 15 | 30 |\n| Total | 70 | 60 | 130 |\n¿Qué porcentaje de los ingresantes de Civil cursa a la tarde?",
                "answer": "37,5 %: ahora la base es el total de Civil (48). 18/48 · 100 = 37,5 %. La celda es la misma (18), pero la pregunta cambia el total de referencia: 30 % es respecto del turno tarde y 13,8 % respecto del total general.",
                "hints": ["La frase “de los ingresantes de Civil” indica cuál es el 100 %."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["37,5 %", "30 %", "13,8 %", "18 %"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Variación porcentual entre dos años de un gráfico de líneas",
                "prompt": "Un gráfico de líneas muestra las ventas anuales de una empresa (en miles de unidades):\n| Año | 2021 | 2022 | 2023 |\n|---|---|---|---|\n| Ventas | 120 | 150 | 135 |\n¿Cuál fue la variación porcentual de 2022 a 2023? Respondé solo con el número (en %, con signo si es negativo).",
                "answer": "−10 %: variación = (final − inicial)/inicial · 100 = (135 − 150)/150 · 100 = −15/150 · 100 = −10 %. Se divide por el valor de partida (2022), no por el de llegada.",
                "hints": [
                    "El valor inicial es el de 2022.",
                    "Si las ventas bajaron, la variación es negativa.",
                ],
                "payload": {"check": {"type": "numeric", "value": -10, "tolerance": 0, "unit": "%"}},
            },
            {
                "item_type": "worked_example",
                "title": "Pasar del ángulo de un sector de torta a pesos",
                "prompt": "Un gráfico de torta muestra cómo se reparte un presupuesto mensual de $ 400 000. El sector “alquiler” tiene un ángulo central de 108°. ¿Cuántos pesos se destinan al alquiler? Respondé solo con el número (en $).",
                "answer": "120 000: la torta completa son 360° = 100 % del presupuesto. 108°/360° = 0,3 = 30 %, y 0,3 · 400 000 = 120 000 pesos.",
                "hints": ["¿Qué fracción de la vuelta completa (360°) es el sector?"],
                "payload": {"check": {"type": "numeric", "value": 120000, "tolerance": 0, "unit": "$"}},
            },
            {
                "item_type": "worked_example",
                "title": "Contar barras que superan el promedio",
                "prompt": "Un gráfico de barras muestra la lluvia caída en una ciudad:\n| Mes | Enero | Febrero | Marzo | Abril |\n|---|---|---|---|---|\n| Lluvia (mm) | 110 | 95 | 80 | 35 |\n¿En cuántos de esos meses la lluvia superó el promedio de los cuatro meses? Respondé solo con el número.",
                "answer": "2: el promedio es (110 + 95 + 80 + 35)/4 = 320/4 = 80 mm. Superan 80 mm enero y febrero; marzo lo iguala, pero igualar no es superar.",
                "hints": [
                    "Primero sumá las cuatro barras y dividí por 4.",
                    "“Superar” es estrictamente mayor.",
                ],
                "payload": {"check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Separar datos útiles de datos accesorios",
                "prompt": "Una tabla de horarios de colectivos informa, para cada servicio: hora de salida, hora de llegada, cantidad de paradas, tarifa y número de unidad. Te preguntan cuánto dura el viaje. ¿Qué datos son útiles?",
                "answer": "Solo la hora de salida y la de llegada: la duración es su diferencia. La cantidad de paradas, la tarifa y el número de unidad son datos accesorios para esta pregunta (servirían para otras).",
                "hints": ["Subrayá la pregunta y buscá qué dos columnas se restan para responderla."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Solo la hora de salida y la hora de llegada",
                            "La hora de salida y la cantidad de paradas",
                            "La tarifa y la cantidad de paradas",
                            "Todos: en un problema siempre se usan todos los datos",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Diferenciar puntos porcentuales de porcentaje de aumento",
                "prompt": "Según un informe, la desocupación pasó del 8 % al 10 %. ¿Cuál de estas descripciones es correcta?",
                "answer": "Subió 2 puntos porcentuales, que es un aumento del 25 % respecto del valor inicial: (10 − 8)/8 · 100 = 25 %. Decir “subió 2 %” confunde la resta de porcentajes con la variación porcentual.",
                "hints": ["La resta 10 − 8 da puntos porcentuales; la variación porcentual se divide por el valor inicial."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Subió 2 puntos porcentuales, un aumento del 25 %",
                            "Subió un 2 %",
                            "Subió un 20 %",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Comparar cantidades y no solo porcentajes",
                "prompt": "En la escuela A aprobó el 90 % de sus 40 alumnos. En la escuela B aprobó el 75 % de sus 80 alumnos. ¿Qué escuela tuvo más alumnos aprobados?",
                "answer": "La escuela B: A tuvo 0,9 · 40 = 36 aprobados y B tuvo 0,75 · 80 = 60. Un porcentaje mayor sobre un grupo más chico puede ser menos personas; la conclusión “A tuvo más aprobados” no se sigue de los porcentajes.",
                "hints": ["Pasá cada porcentaje a cantidad de alumnos."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["La escuela B", "La escuela A", "Tuvieron la misma cantidad"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Aumento real detrás de un eje que no empieza en cero",
                "prompt": "En un gráfico de barras el eje vertical empieza en 500 (no en 0). La barra de enero llega a 600 y la de febrero a 800, así que dibujada la de febrero se ve muchísimo más alta. ¿En qué porcentaje aumentó realmente el valor de enero a febrero? Redondeá a un decimal y respondé solo con el número (en %).",
                "answer": "33,3 %: (800 − 600)/600 · 100 ≈ 33,3 %. Las barras dibujadas desde 500 miden 100 y 300, y por eso parecen el triple; los valores reales se leen en la escala, no en el largo de la barra.",
                "hints": ["Usá los valores que marca el eje, no el largo de las barras.", "Variación % = (final − inicial)/inicial · 100."],
                "payload": {"check": {"type": "numeric", "value": 33.3, "tolerance": 0.01, "unit": "%"}},
            },
            {
                "item_type": "worked_example",
                "title": "Tramo de crecimiento más rápido con intervalos desparejos",
                "prompt": "Un gráfico de líneas muestra el nivel de un tanque durante una mañana:\n| Hora | 8 | 10 | 12 | 14 | 15 |\n|---|---|---|---|---|---|\n| Litros | 200 | 600 | 700 | 1000 | 1250 |\n¿En qué tramo el nivel subió más rápido (más litros por hora)?",
                "answer": "De 14 a 15 h: subió 250 L en 1 h (250 L/h). De 8 a 10 h subió más litros (400 L), pero en 2 h: 200 L/h. De 10 a 12 h fueron 50 L/h y de 12 a 14 h, 150 L/h. Con intervalos de distinto largo hay que dividir por el tiempo.",
                "hints": ["Ojo: los tramos no duran todos lo mismo.", "Ritmo = litros que subió ÷ horas del tramo."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["De 14 a 15 h", "De 8 a 10 h", "De 12 a 14 h", "De 10 a 12 h"],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    # ==================== ESTRATEGIAS (PÓLYA) ====================
    {
        "slug": "cl-estrategias-polya",
        "title": "Estrategias de resolución de problemas (Pólya)",
        "summary": "Recorrer las tres etapas (comprendiendo el problema, planificando y ejecutando, revisando) y elegir estrategias: tabla, dibujo, patrón, ensayo y error registrado, subproblemas, trabajar hacia atrás y ecuaciones con la variable bien definida.",
        "prerequisites": ["cl-lenguaje-simbolico"],
        "insert_after": "cl-tablas-graficos",
        "metadata": {"section": "Resolución de problemas", "est_minutes": 30},
        "items": [
            {
                "item_type": "recall",
                "title": "Las tres etapas del material en orden",
                "prompt": "Ordená las etapas de la resolución de un problema tal como las presenta el material del ingreso.",
                "answer": "1.ª Comprendiendo el problema → 2.ª Planificando y ejecutando → 3.ª Revisando. Si te perdés en el camino, se vuelve a empezar por la primera.",
                "hints": ["No se puede planificar algo que todavía no se entendió."],
                "payload": {
                    "check": {
                        "type": "order",
                        "lines": ["Comprendiendo el problema", "Planificando y ejecutando", "Revisando"],
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Identificar la incógnita y el dato que sobra",
                "prompt": "“Una pileta de 12 m de largo, 6 m de ancho y 1,5 m de profundidad se llena en 5 horas con una bomba. La entrada al club cuesta $ 3000. ¿Cuántos litros por hora entrega la bomba?” ¿Cuál es la incógnita y qué dato es accesorio?",
                "answer": "La incógnita es el caudal de la bomba (litros por hora) y sobra el precio de la entrada. El volumen de la pileta es un subproblema intermedio (hace falta para llegar), pero no es lo que se pregunta.",
                "hints": ["La incógnita está en la pregunta final, no en el primer cálculo que se te ocurra."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Incógnita: litros por hora de la bomba; sobra el precio de la entrada",
                            "Incógnita: volumen de la pileta; sobra el tiempo de llenado",
                            "Incógnita: litros por hora de la bomba; sobran el largo y el ancho",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Definir la variable con precisión",
                "prompt": "Vas a plantear una ecuación para un problema que dice “dentro de 5 años Juan tendrá el doble de la edad que tenía hace 4 años”. ¿Cuál es la mejor definición de la variable?",
                "answer": "x = edad de Juan hoy, en años. La definición dice de quién es, en qué momento y en qué unidad; “x = edad” deja abierto si es la de hoy, la de dentro de 5 años o la de hace 4, y ahí nacen los errores.",
                "hints": ["Una buena definición responde: ¿qué cosa?, ¿de quién?, ¿cuándo?, ¿en qué unidad?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "x = edad de Juan hoy, en años",
                            "x = edad",
                            "x = años",
                            "x = el doble de la edad",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Dibujar para contar árboles y espacios",
                "prompt": "A lo largo de una vereda de 40 m se planta un árbol cada 5 m, con un árbol en cada punta. ¿Cuántos árboles se plantan? Respondé solo con el número.",
                "answer": "9: hay 40 ÷ 5 = 8 espacios entre árboles y, como hay árbol en las dos puntas, los árboles son uno más que los espacios. Un dibujo de un caso chico (10 m: árboles en 0, 5 y 10 → 3 árboles, 2 espacios) evita el error de responder 8.",
                "hints": [
                    "Dibujá un caso chico, por ejemplo una vereda de 10 m.",
                    "Contá por separado los espacios y los árboles.",
                ],
                "payload": {"check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Patrón de fósforos para cuadrados en fila",
                "prompt": "Con fósforos se arman cuadrados en fila: cada cuadrado nuevo comparte un lado con el anterior. ¿Cuántos fósforos hacen falta para 25 cuadrados? Respondé solo con el número.",
                "answer": "76: con 1, 2 y 3 cuadrados se usan 4, 7 y 10 fósforos; cada cuadrado nuevo agrega 3. El patrón es 3n + 1 (verificá con un caso que no usaste: n = 4 da 13, y contando el dibujo también son 13). Para n = 25: 3 · 25 + 1 = 76.",
                "hints": [
                    "Simplificá: contá los fósforos para 1, 2 y 3 cuadrados y armá una tabla.",
                    "¿Cuántos fósforos agrega cada cuadrado nuevo?",
                ],
                "payload": {"check": {"type": "numeric", "value": 76, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Partidos de un torneo todos contra todos",
                "prompt": "En un torneo participan 12 equipos y cada equipo juega exactamente una vez contra cada uno de los demás. ¿Cuántos partidos se juegan en total? Respondé solo con el número.",
                "answer": "66: cada equipo juega contra los otros 11, lo que da 12 · 11 = 132, pero así cada partido se contó dos veces (una por cada equipo). Partidos = n(n − 1)/2 = 12 · 11/2 = 66.",
                "hints": [
                    "¿Contra cuántos rivales juega cada equipo?",
                    "El partido A–B y el partido B–A son el mismo.",
                ],
                "payload": {"check": {"type": "numeric", "value": 66, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Cantidad de personas a partir de los saludos",
                "prompt": "Al terminar una reunión, cada persona le dio la mano exactamente una vez a cada una de las demás, y hubo 45 apretones de manos. ¿Cuántas personas había? Respondé solo con el número.",
                "answer": "10: con n personas hay n(n − 1)/2 apretones. Ensayo y error registrado: n = 8 → 28; n = 9 → 36; n = 10 → 45. Verificación: 10 · 9/2 = 45.",
                "hints": [
                    "Usá la fórmula de los saludos n(n − 1)/2 al revés.",
                    "Armá una tabla probando valores de n.",
                ],
                "payload": {"check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Mínima cantidad de grupos de 3 o de 4",
                "prompt": "Hay que repartir 47 alumnos en grupos de 3 o de 4 integrantes, sin que nadie quede afuera, usando la menor cantidad posible de grupos. ¿Cuántos grupos se arman? Respondé solo con el número.",
                "answer": "12: para usar pocos grupos conviene que haya muchos de 4. Con 11 grupos de 4 (44 alumnos) quedan 3, que forman un grupo de 3: 11 + 1 = 12. Con 12 grupos de 4 se necesitarían 48 alumnos, y con menos grupos de 4 el total de grupos crece (8 de 4 y 5 de 3 son 13).",
                "hints": [
                    "Restricción: todos los grupos son de 3 o de 4 y nadie queda afuera.",
                    "Registrá intentos empezando con la mayor cantidad posible de grupos de 4.",
                ],
                "payload": {"check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Trabajar hacia atrás desde el resultado",
                "prompt": "Pensé un número, le resté 7, multipliqué el resultado por 3 y le sumé 6. Obtuve 51. ¿Qué número pensé? Respondé solo con el número.",
                "answer": "22: se deshacen las operaciones desde el final con la operación inversa: 51 − 6 = 45; 45 ÷ 3 = 15; 15 + 7 = 22. Verificación: (22 − 7) · 3 + 6 = 51.",
                "hints": [
                    "Empezá por el 51 y recorré el camino al revés.",
                    "Cada operación se deshace con su inversa: la suma con resta, el producto con división.",
                ],
                "payload": {"check": {"type": "numeric", "value": 22, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Número de dos cifras por ensayo y error registrado",
                "prompt": "Un número de dos cifras cumple que la suma de sus cifras es 11 y que, si se invierte el orden de sus cifras, el número aumenta en 27. ¿Cuál es el número? Respondé solo con el número.",
                "answer": "47: los candidatos cuyas cifras suman 11 son 29, 38, 47, 56, 65, 74, 83 y 92. Registrando el efecto de invertir: 29 → 92 (+63), 38 → 83 (+45), 47 → 74 (+27). Verificación: 4 + 7 = 11 y 74 − 47 = 27.",
                "hints": [
                    "Listá en una tabla los números de dos cifras cuyas cifras suman 11.",
                    "Para cada uno, anotá cuánto cambia al invertirlo.",
                ],
                "payload": {"check": {"type": "numeric", "value": 47, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    # ==================== PORCENTAJES Y FRACCIONES ====================
    {
        "slug": "cl-porcentajes-fracciones",
        "title": "Problemas de porcentajes y fracciones",
        "summary": "Porcentaje directo e inverso, descuentos y aumentos sucesivos, reintegros con tope, porcentajes de un subgrupo, regla de tres, fracción del resto con total desconocido y mezclas.",
        "prerequisites": ["cl-estrategias-polya"],
        "insert_after": "cl-estrategias-polya",
        "metadata": {"section": "Resolución de problemas", "est_minutes": 35},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Porcentaje de una cantidad con regla de tres",
                "prompt": "En un curso de ingreso hay 260 aspirantes y el 15 % cursa a distancia. ¿Cuántos aspirantes cursan a distancia? Respondé solo con el número.",
                "answer": "39: regla de tres: 100 % ↔ 260 aspirantes; 15 % ↔ x. x = 15 · 260/100 = 39.",
                "hints": ["El 100 % son los 260 aspirantes."],
                "payload": {"check": {"type": "numeric", "value": 39, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Qué porcentaje representa una parte",
                "prompt": "En un control de calidad se revisaron 450 piezas y 18 salieron defectuosas. ¿Qué porcentaje de las piezas salió defectuoso? Respondé solo con el número (en %).",
                "answer": "4 %: porcentaje = parte/total · 100 = 18/450 · 100 = 4 %.",
                "hints": ["El total de referencia son las piezas revisadas."],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "%"}},
            },
            {
                "item_type": "worked_example",
                "title": "Total a partir de una parte y su porcentaje",
                "prompt": "El 12 % de las butacas de un teatro están en la platea alta, y son 54 butacas. ¿Cuántas butacas tiene el teatro en total? Respondé solo con el número.",
                "answer": "450: regla de tres: 12 % ↔ 54 butacas; 100 % ↔ x. x = 54 · 100/12 = 450. Verificación: 12 % de 450 = 54.",
                "hints": ["Ahora el dato es la parte y la incógnita es el 100 %."],
                "payload": {"check": {"type": "numeric", "value": 450, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Precio de lista a partir de lo pagado con descuento",
                "prompt": "Con un 35 % de descuento pagaste $ 26 000 por una calculadora científica. ¿Cuál era el precio de lista? Respondé solo con el número (en $).",
                "answer": "40 000: lo pagado es el 65 % del precio de lista (100 % − 35 %). x · 0,65 = 26 000 → x = 26 000/0,65 = 40 000. Sumarle el 35 % a lo pagado daría 35 100, que es incorrecto porque el descuento se calculó sobre el precio de lista, no sobre lo pagado.",
                "hints": [
                    "¿Qué porcentaje del precio de lista pagaste?",
                    "El 35 % se aplicó sobre el precio original, que es la incógnita.",
                ],
                "payload": {"check": {"type": "numeric", "value": 40000, "tolerance": 0, "unit": "$"}},
            },
            {
                "item_type": "worked_example",
                "title": "Porcentaje de descuento que se aplicó",
                "prompt": "Unas zapatillas tenían un precio de lista de $ 48 000 y las pagaste $ 40 800. ¿Qué porcentaje de descuento te aplicaron? Respondé solo con el número (en %).",
                "answer": "15 %: el descuento fue 48 000 − 40 800 = 7200 pesos, y respecto del precio de lista es 7200/48 000 · 100 = 15 %.",
                "hints": ["Calculá cuántos pesos te descontaron y compará con el precio de lista (el 100 %)."],
                "payload": {"check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": "%"}},
            },
            {
                "item_type": "worked_example",
                "title": "Aumento acumulado de tres aumentos sucesivos",
                "prompt": "Un precio aumenta un 10 % por mes durante tres meses seguidos (cada aumento se aplica sobre el precio del mes anterior). ¿Cuál es el aumento total, en porcentaje, respecto del precio inicial? Respondé solo con el número (en %).",
                "answer": "33,1 %: cada aumento multiplica por 1,1, así que en tres meses el precio queda multiplicado por 1,1³ = 1,331, un aumento del 33,1 %. Sumar 10 + 10 + 10 = 30 % ignora que cada aumento se calcula sobre un precio ya aumentado.",
                "hints": [
                    "Un aumento del 10 % equivale a multiplicar por 1,1.",
                    "Los factores de porcentajes sucesivos se multiplican, no se suman.",
                ],
                "payload": {"check": {"type": "numeric", "value": 33.1, "tolerance": 0, "unit": "%"}},
            },
            {
                "item_type": "worked_example",
                "title": "Porcentaje real de un reintegro con tope",
                "prompt": "Un banco reintegra el 25 % de lo que gastes en una librería, con un tope de $ 5000 por compra. Gastás $ 32 000. ¿Qué porcentaje de tu gasto te reintegran realmente? Redondeá a un decimal y respondé solo con el número (en %).",
                "answer": "15,6 %: el 25 % de 32 000 sería 8000, pero el tope limita el reintegro a 5000. Porcentaje real = 5000/32 000 · 100 = 15,625 % ≈ 15,6 %. Para aprovechar todo el 25 % no conviene gastar más de 5000/0,25 = 20 000 pesos.",
                "hints": [
                    "Compará el 25 % del gasto con el tope y quedate con el menor.",
                    "Porcentaje real = reintegro/gasto · 100.",
                ],
                "payload": {"check": {"type": "numeric", "value": 15.6, "tolerance": 0.01, "unit": "%"}},
            },
            {
                "item_type": "worked_example",
                "title": "Porcentaje de un subgrupo",
                "prompt": "En una encuesta a 500 estudiantes, el 40 % va a la facultad en bicicleta. De los que van en bicicleta, el 30 % la usa todos los días. ¿Cuántos estudiantes usan la bicicleta todos los días? Respondé solo con el número.",
                "answer": "60: los que van en bicicleta son 0,4 · 500 = 200, y el 30 % de ese subgrupo es 0,3 · 200 = 60. El 30 % se calcula sobre los 200, no sobre los 500 (eso daría 150).",
                "hints": ["“De los que van en bicicleta” cambia la base: primero calculá ese subgrupo."],
                "payload": {"check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Fracción del resto con el total desconocido",
                "prompt": "Un ciclista recorre el primer día 2/5 de un trayecto y el segundo día la mitad de lo que le faltaba. Todavía le quedan 36 km. ¿Cuántos kilómetros tiene el trayecto completo? Respondé solo con el número (en km).",
                "answer": "120: sea x = longitud total (km). Después del primer día falta 3/5 · x; el segundo día recorre la mitad de eso, así que sigue faltando 1/2 · 3/5 · x = 3/10 · x. Entonces 3/10 · x = 36 → x = 120. Verificación: 48 km el primer día, 36 el segundo y quedan 36.",
                "hints": [
                    "Definí x = longitud total y escribí lo que falta después de cada día.",
                    "“La mitad de lo que le faltaba” se calcula sobre el resto, no sobre x.",
                ],
                "payload": {"check": {"type": "numeric", "value": 120, "tolerance": 0, "unit": "km"}},
            },
            {
                "item_type": "worked_example",
                "title": "Alcohol puro para subir la concentración de una mezcla",
                "prompt": "Tenés 6 L de una solución de alcohol al 20 %. ¿Cuántos litros de alcohol puro hay que agregarle para que la mezcla quede al 40 %? Respondé solo con el número (en L).",
                "answer": "2: sea y = litros de alcohol puro agregados. Alcohol al principio: 0,2 · 6 = 1,2 L. Después: 1,2 + y litros de alcohol en 6 + y litros de mezcla. 1,2 + y = 0,4 · (6 + y) → 1,2 + y = 2,4 + 0,4y → 0,6y = 1,2 → y = 2. Verificación: 3,2 L de alcohol en 8 L = 40 %.",
                "hints": [
                    "Escribí cuánto alcohol puro hay antes y después.",
                    "Al agregar alcohol también crece el volumen total de la mezcla.",
                ],
                "payload": {"check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "L"}},
            },
        ],
    },
    # ==================== EDADES Y SISTEMAS ====================
    {
        "slug": "cl-edades-sistemas",
        "title": "Problemas de edades y sistemas de ecuaciones",
        "summary": "Plantear problemas de edades con “hace”, “dentro de” y “cuando yo tenía”, resolverlos por ensayo y error con tabla y por ecuaciones, y resolver sistemas 2×2 y 3×3 sencillos y problemas de números consecutivos.",
        "prerequisites": ["cl-estrategias-polya"],
        "insert_after": "cl-porcentajes-fracciones",
        "metadata": {"section": "Resolución de problemas", "est_minutes": 35},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Edad actual a partir de un “dentro de” y un “hace”",
                "prompt": "Dentro de 9 años, Lara tendrá el doble de la edad que tenía hace 3 años. ¿Qué edad tiene Lara hoy? Respondé solo con el número (en años).",
                "answer": "15: sea x = edad de Lara hoy (años). Dentro de 9 años: x + 9; hace 3 años: x − 3. x + 9 = 2.(x − 3) → x + 9 = 2x − 6 → x = 15. Verificación: dentro de 9 años tendrá 24, y hace 3 años tenía 12; 24 es el doble de 12.",
                "hints": [
                    "Definí x como la edad de HOY y expresá las otras dos edades con x.",
                    "“El doble de la edad que tenía” va con paréntesis: 2.(x − 3).",
                ],
                "payload": {"check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": "años"}},
            },
            {
                "item_type": "worked_example",
                "title": "Cuando yo tenía la edad que vos tenés",
                "prompt": "Yo tengo 31 años y mi primo tiene 19. ¿Qué edad tenía mi primo cuando yo tenía la edad que él tiene ahora? Respondé solo con el número (en años).",
                "answer": "7: yo tuve 19 años hace 31 − 19 = 12 años. Hace 12 años mi primo tenía 19 − 12 = 7. La diferencia de edades (12 años) no cambia nunca: entonces nos llevábamos 19 − 7 = 12, igual que hoy.",
                "hints": [
                    "¿Hace cuántos años tuve yo 19?",
                    "Restale esa misma cantidad de años a la edad de mi primo.",
                ],
                "payload": {"check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": "años"}},
            },
            {
                "item_type": "worked_example",
                "title": "Dentro de cuántos años una edad será el triple",
                "prompt": "Una abuela tiene 66 años y su nieto 14. ¿Dentro de cuántos años la edad de la abuela será el triple de la edad del nieto? Respondé solo con el número (en años).",
                "answer": "12: sea t = años que tienen que pasar. 66 + t = 3.(14 + t) → 66 + t = 42 + 3t → 24 = 2t → t = 12. Verificación: dentro de 12 años tendrán 78 y 26, y 3 · 26 = 78.",
                "hints": [
                    "Los dos envejecen lo mismo: sumale t a cada edad.",
                    "También sirve una tabla: hoy, +5 años, +10 años… hasta que la abuela tenga el triple.",
                ],
                "payload": {"check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": "años"}},
            },
            {
                "item_type": "worked_example",
                "title": "Hace cuántos años una edad era el cuádruple",
                "prompt": "Una tía tiene 50 años y su sobrina 20. ¿Hace cuántos años la edad de la tía era el cuádruple de la edad de la sobrina? Respondé solo con el número (en años).",
                "answer": "10: sea t = años hacia atrás. 50 − t = 4.(20 − t) → 50 − t = 80 − 4t → 3t = 30 → t = 10. Verificación: hace 10 años tenían 40 y 10, y 4 · 10 = 40.",
                "hints": ["“Hace t años” se escribe restando t a CADA edad."],
                "payload": {"check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "años"}},
            },
            {
                "item_type": "worked_example",
                "title": "Entradas de dos precios con un sistema 2×2",
                "prompt": "Para una obra de teatro, la entrada de adulto cuesta $ 3000 y la de menor $ 1800. Se vendieron 70 entradas y se recaudaron $ 174 000. ¿Cuántas entradas de menor se vendieron? Respondé solo con el número.",
                "answer": "30: sean a = entradas de adulto y m = entradas de menor. a + m = 70 y 3000a + 1800m = 174 000. Por sustitución, a = 70 − m: 3000.(70 − m) + 1800m = 174 000 → 210 000 − 1200m = 174 000 → m = 30 (y a = 40). Verificación: 40 · 3000 + 30 · 1800 = 120 000 + 54 000 = 174 000.",
                "hints": [
                    "Una ecuación cuenta entradas y la otra cuenta dinero.",
                    "Despejá a en la primera y reemplazá en la segunda (sustitución).",
                ],
                "payload": {"check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Resolver un sistema 2×2 por reducción",
                "prompt": "Resolvé el sistema 2x + 3y = 24 ; 4x − 3y = 12. ¿Cuánto vale y? Respondé solo con el número.",
                "answer": "4: sumando las ecuaciones miembro a miembro se elimina y: 6x = 36 → x = 6. Reemplazando en la primera: 2 · 6 + 3y = 24 → 3y = 12 → y = 4. Verificación en la segunda: 4 · 6 − 3 · 4 = 12.",
                "hints": ["Fijate que los términos en y tienen coeficientes opuestos: +3y y −3y."],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Dos cantidades conociendo su suma y su diferencia",
                "prompt": "Dos tramos de caño miden 47 m entre los dos, y uno mide 9 m más que el otro. ¿Cuánto mide el tramo más corto? Respondé solo con el número (en m).",
                "answer": "19: sea c = tramo corto (m); el largo mide c + 9. c + (c + 9) = 47 → 2c = 38 → c = 19 (y el largo, 28). Otra forma: si al largo le sacás los 9 m de diferencia, quedan dos tramos iguales que suman 38.",
                "hints": ["Si los dos midieran lo mismo que el corto, ¿cuánto sumarían?"],
                "payload": {"check": {"type": "numeric", "value": 19, "tolerance": 0, "unit": "m"}},
            },
            {
                "item_type": "worked_example",
                "title": "Sistema 3×3 de sumas de a pares",
                "prompt": "Tres cajas A, B y C se pesan de a dos: A y B juntas pesan 21 kg, A y C pesan 25 kg, y B y C pesan 28 kg. ¿Cuánto pesa la caja C? Respondé solo con el número (en kg).",
                "answer": "16: sumando las tres ecuaciones, cada caja aparece dos veces: 2(A + B + C) = 21 + 25 + 28 = 74, así que A + B + C = 37. Entonces C = 37 − (A + B) = 37 − 21 = 16. Del mismo modo A = 9 y B = 12. Verificación: 9 + 12 = 21, 9 + 16 = 25, 12 + 16 = 28.",
                "hints": [
                    "Sumá las tres ecuaciones: ¿cuántas veces aparece cada caja?",
                    "Con el total de las tres, restá la pareja que no incluye a C.",
                ],
                "payload": {"check": {"type": "numeric", "value": 16, "tolerance": 0, "unit": "kg"}},
            },
            {
                "item_type": "worked_example",
                "title": "Sistema 3×3 encadenado por sustitución",
                "prompt": "En un estacionamiento hay el triple de autos que de motos, y la cantidad de bicicletas es el doble de la de autos y motos juntos. En total hay 180 vehículos. ¿Cuántas motos hay? Respondé solo con el número.",
                "answer": "15: sean m = motos, a = autos, b = bicicletas. a = 3m; b = 2.(a + m) = 2.(3m + m) = 8m. m + 3m + 8m = 180 → 12m = 180 → m = 15. Hay 45 autos y 120 bicicletas: 15 + 45 + 120 = 180.",
                "hints": [
                    "Expresá autos y bicicletas en función de las motos.",
                    "“El doble de autos y motos juntos” lleva paréntesis: 2.(a + m).",
                ],
                "payload": {"check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Tres números pares consecutivos",
                "prompt": "La suma de tres números pares consecutivos es 78. ¿Cuál es el mayor de los tres? Respondé solo con el número.",
                "answer": "28: dos pares consecutivos se diferencian en 2, así que se escriben n, n + 2 y n + 4. n + (n + 2) + (n + 4) = 78 → 3n + 6 = 78 → n = 24. Los números son 24, 26 y 28.",
                "hints": ["Entre un número par y el par siguiente hay 2 unidades, no 1."],
                "payload": {"check": {"type": "numeric", "value": 28, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    # ==================== GEOMETRÍA ====================
    {
        "slug": "cl-geometria-problemas",
        "title": "Problemas de geometría: ángulos, áreas y volúmenes",
        "summary": "Ángulos en triángulos, polígonos y entre paralelas, perímetros y áreas de figuras compuestas, volúmenes y capacidad en litros, conversión de unidades y problemas de planteo con figuras descriptas en palabras.",
        "prerequisites": ["cl-estrategias-polya"],
        "insert_after": "cl-edades-sistemas",
        "metadata": {"section": "Resolución de problemas", "est_minutes": 35},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Ángulo mayor de un triángulo con un ángulo doble de otro",
                "prompt": "En un triángulo, un ángulo mide 48° y otro mide el doble del tercero. ¿Cuánto mide el ángulo mayor? Respondé solo con el número (en grados).",
                "answer": "88°: sea x = medida del tercer ángulo. 48° + 2x + x = 180° → 3x = 132° → x = 44°. Los ángulos son 48°, 88° y 44°, y el mayor es 88°.",
                "hints": ["Los tres ángulos interiores de un triángulo suman 180°."],
                "payload": {"check": {"type": "numeric", "value": 88, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Problema: ángulo interior de un octógono regular",
                "prompt": "¿Cuánto mide cada ángulo interior de un octógono regular? Respondé solo con el número (en grados).",
                "answer": "135°: los ángulos interiores de un polígono de n lados suman (n − 2) · 180°. Para n = 8: 6 · 180° = 1080°, y como en el regular son todos iguales, cada uno mide 1080° ÷ 8 = 135°.",
                "hints": [
                    "Desde un vértice, el polígono se divide en n − 2 triángulos.",
                    "Regular = todos los ángulos iguales.",
                ],
                "payload": {"check": {"type": "numeric", "value": 135, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Conjugados internos entre paralelas con incógnita",
                "prompt": "Dos rectas paralelas son cortadas por una transversal. Dos ángulos conjugados internos miden 3x + 10° y 2x + 20°. ¿Cuánto mide el mayor de los dos? Respondé solo con el número (en grados).",
                "answer": "100°: los conjugados internos entre paralelas son suplementarios. (3x + 10°) + (2x + 20°) = 180° → 5x = 150° → x = 30°. Miden 100° y 80°.",
                "hints": ["Conjugados internos: del mismo lado de la transversal y entre las paralelas. ¿Son iguales o suman algo?"],
                "payload": {"check": {"type": "numeric", "value": 100, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Ángulo exterior en la base de un triángulo isósceles",
                "prompt": "En un triángulo isósceles, el ángulo desigual (entre los dos lados iguales) mide 40°. ¿Cuánto mide el ángulo exterior en cada vértice de la base? Respondé solo con el número (en grados).",
                "answer": "110°: los ángulos de la base son iguales y miden (180° − 40°)/2 = 70° cada uno. El exterior es suplementario del interior: 180° − 70° = 110°. También: el exterior es igual a la suma de los dos interiores no adyacentes, 40° + 70° = 110°.",
                "hints": [
                    "En un isósceles, los dos ángulos de la base son iguales.",
                    "Un ángulo interior y su exterior suman 180°.",
                ],
                "payload": {"check": {"type": "numeric", "value": 110, "tolerance": 0, "unit": "°"}},
            },
            {
                "item_type": "worked_example",
                "title": "Área de un ventanal con medio círculo",
                "prompt": "Un ventanal está formado por un rectángulo de 2 m de ancho y 1,5 m de alto, con un semicírculo encima cuyo diámetro es el lado superior del rectángulo. ¿Cuál es el área total del vidrio? Usá π y redondeá a dos decimales. Respondé solo con el número (en m²).",
                "answer": "4,57 m²: rectángulo 2 · 1,5 = 3 m²; semicírculo de radio 1 m: π · 1²/2 ≈ 1,57 m². Total ≈ 4,57 m².",
                "hints": [
                    "Dividí la figura en un rectángulo y un semicírculo.",
                    "El radio es la mitad del ancho.",
                ],
                "payload": {"check": {"type": "numeric", "value": 4.57, "tolerance": 0.01, "unit": "m²"}},
            },
            {
                "item_type": "worked_example",
                "title": "Perímetro de un ventanal con medio círculo",
                "prompt": "Para el mismo ventanal (rectángulo de 2 m de ancho y 1,5 m de alto con un semicírculo apoyado en el lado superior), hay que comprar el burlete del contorno exterior. ¿Cuántos metros mide ese contorno? Usá π y redondeá a dos decimales. Respondé solo con el número (en m).",
                "answer": "8,14 m: el contorno tiene la base (2 m), los dos lados (1,5 m cada uno) y el arco del semicírculo, π · r = π · 1 ≈ 3,14 m. 2 + 3 + 3,14 ≈ 8,14 m. El lado superior del rectángulo queda adentro de la figura y no se cuenta.",
                "hints": [
                    "Recorré el borde con el dedo: ¿el lado de arriba del rectángulo es parte del borde?",
                    "Medio círculo mide la mitad de 2 · π · r.",
                ],
                "payload": {"check": {"type": "numeric", "value": 8.14, "tolerance": 0.01, "unit": "m"}},
            },
            {
                "item_type": "worked_example",
                "title": "Capacidad en litros de un tanque cilíndrico",
                "prompt": "Un tanque cilíndrico tiene 1,2 m de diámetro y 1,5 m de altura. ¿Cuántos litros entran? Usá π y redondeá a la unidad. Respondé solo con el número (en litros).",
                "answer": "1696 L: radio = 0,6 m. V = π · r² · h = π · 0,36 · 1,5 ≈ 1,696 m³. Como 1 m³ = 1000 L, entran unos 1696 litros.",
                "hints": [
                    "Usá el radio, no el diámetro.",
                    "1 m³ = 1000 dm³ = 1000 L.",
                ],
                "payload": {"check": {"type": "numeric", "value": 1696, "tolerance": 0.01, "unit": "L"}},
            },
            {
                "item_type": "worked_example",
                "title": "Baldosas necesarias para una superficie",
                "prompt": "¿Cuántas baldosas cuadradas de 40 cm de lado hacen falta para cubrir exactamente 12 m² de piso (sin desperdicio)? Respondé solo con el número.",
                "answer": "75: cada baldosa cubre 0,4 m · 0,4 m = 0,16 m². 12 ÷ 0,16 = 75. (En cm²: 12 m² = 120 000 cm² y cada baldosa tiene 1600 cm²; 120 000 ÷ 1600 = 75.)",
                "hints": [
                    "Pasá todo a la misma unidad antes de dividir.",
                    "1 m² = 10 000 cm², no 100 cm².",
                ],
                "payload": {"check": {"type": "numeric", "value": 75, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Pasar decímetros cúbicos a centímetros cúbicos",
                "prompt": "¿A cuántos centímetros cúbicos equivalen 2,5 dm³?",
                "answer": "2500 cm³: en volumen cada escalón de unidad multiplica por 1000 (1 dm³ = 10 cm · 10 cm · 10 cm = 1000 cm³). Además 2,5 dm³ = 2,5 L = 2500 mL.",
                "hints": ["1 dm = 10 cm, y el cubo tiene tres dimensiones."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["2500 cm³", "250 cm³", "25 cm³", "25 000 cm³"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Área de un rectángulo descripto en palabras",
                "prompt": "Un terreno rectangular tiene un largo que supera al ancho en 5 m, y su perímetro es de 58 m. ¿Cuál es su área? Respondé solo con el número (en m²).",
                "answer": "204 m²: sea x = ancho (m); el largo es x + 5. Perímetro: 2.(x + x + 5) = 58 → 2x + 5 = 29 → x = 12. El terreno mide 12 m × 17 m, y su área es 204 m². Verificación: 2 · (12 + 17) = 58.",
                "hints": [
                    "Hacé un croquis y escribí los lados en función del ancho.",
                    "Primero usá el perímetro para hallar los lados; recién después calculá el área.",
                ],
                "payload": {"check": {"type": "numeric", "value": 204, "tolerance": 0, "unit": "m²"}},
            },
        ],
    },
]


CLYRP_PROBLEMAS_LESSONS: dict[str, dict] = {
    "cl-razonamiento-logico": {
        "hook": {
            "question": "Bruno es más alto que Ana y Ana es más alta que Caro. ¿Hace falta medir a Bruno y a Caro para saber quién de los dos es más alto?",
            "intuition": "No: “más alto que” se encadena, y queda **Caro < Ana < Bruno**. Pero si solo supieras que Bruno y Caro son más altos que Ana, no podrías ordenarlos entre sí. En los acertijos lógicos se deduce **todo lo que se sigue de las pistas y nada más**, y para eso conviene ordenar la información: una línea, una tabla o un dibujo de la mesa.",
        },
        "concept": {
            "points": [
                "**Método del material**: 1) identificá los **datos implícitos** (lo que no está escrito pero se deduce: si “el músico pesca con Juan”, Juan no es el músico); 2) armá una **tabla que muestre datos y restricciones**; 3) elegí una representación para la **negación** (✗ = “no es”); 4) **verificá** la solución confrontándola con cada pista del enunciado.",
                "**Ordenar por comparaciones**: pasá cada frase a una desigualdad (“A habla más bajo que R” → `A < R`) y encadenalas sobre una línea. Si entre dos elementos no hay ninguna cadena de comparaciones, su orden queda **indeterminado**: no lo inventes.",
                "**Tabla de doble entrada para asignar** (personas–oficios, personas–objetos): filas para unos, columnas para otros. Si la asignación es uno a uno, un ✓ llena de ✗ el resto de su fila y de su columna; y si en una fila (o columna) queda una sola casilla sin ✗, ahí va el ✓.",
                "**Ubicaciones en línea y en ronda**: en una línea los extremos tienen un solo vecino; en una ronda todos tienen dos, y “frente a” tiene sentido cuando la cantidad de sillas es par. Fijá primero a una persona: las rondas giradas son la misma ubicación. Izquierda y derecha se toman desde la persona sentada mirando al centro.",
                "**Verdades y mentiras**: suponé una hipótesis (“lo hizo X”), calculá qué frases resultan verdaderas y cuáles falsas, y descartá la hipótesis si contradice la condición del problema. Probá **todas** las hipótesis: puede haber una sola que cierre.",
                "**Sumas con letras (criptoaritmética)**: letras distintas = cifras distintas, y un número escrito con letras vale por posición (`AB = 10·A + B`). Mirá los acarreos: si dos números de n cifras suman uno de n + 1 cifras, la primera cifra del resultado es 1.",
            ],
            "real_world": [
                {
                    "title": "Armado de horarios y turnos",
                    "detail": "Asignar docentes a aulas y horarios (“el laboratorio no está libre los martes”, “nadie da dos clases a la vez”) es una tabla de doble entrada enorme con restricciones; los programas que arman horarios hacen las mismas deducciones con ✓ y ✗.",
                },
                {
                    "title": "Diagnóstico de fallas",
                    "detail": "Cuando dos sensores de una máquina dan lecturas contradictorias, el técnico supone que uno falla y verifica si el resto de las mediciones es coherente con esa hipótesis: es el razonamiento de verdades y mentiras.",
                },
                {
                    "title": "Algoritmos de búsqueda con restricciones",
                    "detail": "Los programas que resuelven un sudoku o asignan frecuencias de radio prueban una hipótesis, propagan las consecuencias (las ✗) y retroceden cuando aparece una contradicción.",
                },
            ],
            "key_rule": "Datos implícitos → tabla con ✓ y ✗ → deducir solo lo que se sigue → verificar la solución contra TODAS las pistas.",
            "pitfall": "Dar por cierto un orden o una asignación que las pistas no garantizan (si A > B y A > C, nada dice si B > C), o no verificar al final y quedarse con una solución que viola alguna pista.",
        },
        "example": {
            "title": "Luz, Mora y Nina: tres carreras y tres pistas",
            "steps": [
                "Enunciado: Luz, Mora y Nina estudian Civil, Química y Sistemas, una carrera distinta cada una. Pistas: (1) la que estudia Civil viaja en colectivo con Nina; (2) Mora es vecina de la que estudia Química; (3) Mora no estudia Civil.",
                "**Datos implícitos**: por (1), Nina no estudia Civil (no viaja consigo misma); por (2), Mora no estudia Química (no es vecina de sí misma). La asignación es uno a uno.",
                "**Tabla con las negaciones** (✗) de las pistas (1), (2) y (3):\n| | Civil | Química | Sistemas |\n|---|---|---|---|\n| Luz | | | |\n| Mora | ✗ | ✗ | |\n| Nina | ✗ | | |",
                "**Deducción**: en la columna Civil solo queda libre Luz → Luz estudia Civil (y ✗ en el resto de su fila). En la fila de Mora solo queda Sistemas. A Nina le queda Química.\n| | Civil | Química | Sistemas |\n|---|---|---|---|\n| Luz | ✓ | ✗ | ✗ |\n| Mora | ✗ | ✗ | ✓ |\n| Nina | ✗ | ✓ | ✗ |",
                "**Verificación**: (1) Luz, de Civil, viaja con Nina ✓; (2) Mora es vecina de Nina, la de Química ✓; (3) Mora estudia Sistemas, no Civil ✓.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Si P < Q, R > Q y S < P, ¿cuál es el mayor de los cuatro?",
            "options": [
                {"text": "R", "ok": True, "feedback": "Exacto: encadenando queda S < P < Q < R."},
                {"text": "Q", "ok": False, "feedback": "Q supera a P y a S, pero la pista R > Q dice que R es todavía mayor."},
                {"text": "S", "ok": False, "feedback": "Leíste los signos al revés: S < P significa que S es menor que P, y queda en el extremo de los menores."},
            ],
        },
        "checks": [
            {
                "question": "Ana, Beto o Caro rompió una ventana. Ana dice: “Fue Beto”. Beto dice: “Yo no fui”. Caro dice: “Yo no fui”. Solo uno dice la verdad. ¿Quién la rompió?",
                "options": [
                    {"text": "Caro", "ok": True, "feedback": "Exacto: si fue Caro, Ana miente, Beto dice la verdad y Caro miente: una sola verdad."},
                    {"text": "Beto", "ok": False, "feedback": "Si fue Beto, Ana dice la verdad y Caro también (ella no fue): serían dos verdades."},
                    {"text": "Ana", "ok": False, "feedback": "Si fue Ana, Beto y Caro dicen la verdad (ninguno de los dos fue): serían dos verdades."},
                ],
            },
            {
                "question": "En una tabla de asignación uno a uno de 3 × 3, una fila tiene ✗ en dos de sus tres casillas. ¿Qué se concluye?",
                "options": [
                    {"text": "La casilla restante de esa fila es ✓, y el resto de su columna se llena con ✗", "ok": True, "feedback": "Exacto: cada fila tiene que tener exactamente un ✓, y ese ✓ descarta a los demás de su columna."},
                    {"text": "No se puede concluir nada hasta tener otra pista", "ok": False, "feedback": "En una asignación uno a uno cada fila necesita un ✓; si solo queda una casilla posible, ya está decidida."},
                    {"text": "La casilla restante también es ✗", "ok": False, "feedback": "Entonces esa persona no tendría ninguna opción, lo que contradice que a cada una le corresponde exactamente una."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras qué es un dato implícito y dá un ejemplo de pista que esconda una negación.",
    },
    "cl-tablas-graficos": {
        "hook": {
            "question": "En un gráfico de barras, la barra de la marca A se ve el triple de alta que la de la marca B. ¿A vende el triple que B?",
            "intuition": "Solo si el eje vertical empieza en 0. Si el eje arranca en 900 y A vende 1200 y B 1000, las barras dibujadas miden 300 y 100 (el triple), pero A vende apenas un **20 %** más. Antes de sacar conclusiones de un gráfico hay que leer **qué mide, en qué unidades y desde dónde empieza la escala**.",
        },
        "concept": {
            "points": [
                "**Antes de los números**: leé el título, la fuente, las unidades (miles, %, $, mm), el período y qué representa cada fila, columna o eje. En una **tabla de doble entrada**, cada celda es el cruce de una categoría de fila con una de columna, y las filas y columnas “Total” son los totales marginales.",
                "**Tipos de gráfico**: de **barras** para comparar categorías; de **torta** (sectores) para las partes de un todo, que suman 100 % y 360° (cada 1 % ocupa 3,6°); de **líneas** para la evolución en el tiempo, donde una línea más empinada indica un cambio más rápido.",
                "**Cálculos típicos**: porcentaje de una parte = parte/total · 100; variación absoluta = final − inicial; **variación porcentual = (final − inicial)/inicial · 100**; promedio = suma/cantidad. En una tabla de doble entrada, la pregunta indica cuál total es el 100 % (el de la fila, el de la columna o el general).",
                "**Datos útiles y accesorios**: subrayá la pregunta y buscá solo la fila y la columna que hacen falta. Una tabla suele traer más datos de los necesarios, y usarlos todos no es una obligación.",
                "**Conclusiones válidas e inválidas**: una tabla describe esos datos; no prueba causas ni permite extrapolar fuera del período medido. Un porcentaje mayor de un grupo chico puede ser menos personas, y pasar del 8 % al 10 % es subir **2 puntos porcentuales** (un aumento del 25 %), no “un 2 %”.",
                "**Escalas engañosas**: un eje que no empieza en 0 exagera las diferencias; intervalos de tiempo desparejos cambian la pendiente aparente; las tortas en 3D agrandan los sectores del frente. Leé los valores en la escala, no el tamaño del dibujo.",
            ],
            "real_world": [
                {
                    "title": "Factura de luz o de gas",
                    "detail": "El gráfico de barras de consumo por bimestre sirve para comparar con el mismo bimestre del año anterior: comparar invierno con verano mezcla el efecto de la estación.",
                },
                {
                    "title": "Informes de ensayos de laboratorio",
                    "detail": "Una tabla de ensayo de tracción trae la carga en kN y el alargamiento en mm en el encabezado: leer mal la unidad de una columna arruina todos los cálculos que siguen.",
                },
                {
                    "title": "Gráficos en noticias y encuestas",
                    "detail": "Es común ver barras con el eje cortado o tortas que no suman 100 %: con los números de la escala se puede recalcular la variación real y detectar la exageración.",
                },
            ],
            "key_rule": "Primero qué se mide (unidades, período, cuál es el 100 %); después la cuenta: % = parte/total · 100 y variación % = (final − inicial)/inicial · 100, siempre sobre el valor inicial.",
            "pitfall": "Dividir la variación por el valor final en lugar del inicial, o comparar alturas de barras sin fijarse dónde empieza el eje.",
        },
        "example": {
            "title": "Producción trimestral de una fábrica de pastas",
            "steps": [
                "**Leer la tabla**: unidades en toneladas; filas = productos, columnas = meses; la última fila y la última columna son totales.\n| Producto | Enero | Febrero | Marzo | Total |\n|---|---|---|---|---|\n| Fideos | 40 | 45 | 50 | 135 |\n| Ravioles | 20 | 15 | 30 | 65 |\n| Total | 60 | 60 | 80 | 200 |",
                "**Porcentaje de una parte**: los ravioles fueron 65/200 · 100 = **32,5 %** de la producción del trimestre (la base es el total general, 200 t).",
                "**Variación porcentual**: los fideos pasaron de 40 t (enero) a 50 t (marzo): variación absoluta 10 t y variación porcentual 10/40 · 100 = **25 %** (sobre el valor inicial, enero).",
                "**Torta del trimestre**: el sector de ravioles ocuparía 32,5 · 3,6° = **117°**, y el de fideos, los 243° restantes.",
                "**Conclusiones**: “en febrero bajó la producción de pastas” es **inválida**: el total quedó en 60 t, porque los fideos subieron 5 t y los ravioles bajaron 5 t (un −25 %). “En marzo se produjo un tercio más que en febrero” es **válida**: (80 − 60)/60 ≈ 33,3 %.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Un precio pasa de $ 800 a $ 1000. ¿Cuál es la variación porcentual?",
            "options": [
                {"text": "25 %", "ok": True, "feedback": "Exacto: (1000 − 800)/800 · 100 = 25 %."},
                {"text": "20 %", "ok": False, "feedback": "Dividiste la diferencia por el valor final (200/1000). La variación se calcula sobre el valor inicial, 800."},
                {"text": "200 %", "ok": False, "feedback": "200 es la variación absoluta en pesos, no un porcentaje: falta dividirla por el valor inicial."},
            ],
        },
        "checks": [
            {
                "question": "En un gráfico de torta, un sector representa el 15 % del total. ¿Qué ángulo central tiene?",
                "options": [
                    {"text": "54°", "ok": True, "feedback": "Exacto: 15 % de 360° = 0,15 · 360° = 54°."},
                    {"text": "15°", "ok": False, "feedback": "Usaste el porcentaje como si fuera el ángulo; la vuelta completa son 360°, no 100°."},
                    {"text": "27°", "ok": False, "feedback": "Calculaste el 15 % de 180°, como si la torta fuera media vuelta."},
                ],
            },
            {
                "question": "Un gráfico de barras tiene el eje vertical de 90 a 100. La barra de A llega a 98 y la de B a 92. ¿Qué conclusión es correcta?",
                "options": [
                    {"text": "A supera a B en un 6,5 % aproximadamente, aunque su barra se vea 4 veces más alta", "ok": True, "feedback": "Exacto: (98 − 92)/92 · 100 ≈ 6,5 %. Las barras dibujadas desde 90 miden 8 y 2, y por eso parecen cuatro veces distintas."},
                    {"text": "A es 4 veces mayor que B", "ok": False, "feedback": "Comparaste el largo de las barras dibujadas (8 y 2), que empiezan en 90 y no en 0."},
                    {"text": "No se pueden comparar porque el eje no empieza en 0", "ok": False, "feedback": "Sí se pueden comparar: los valores se leen en la escala (98 y 92). Lo que engaña es el tamaño del dibujo, no los números."},
                ],
            },
        ],
        "takeaway_prompt": "Contá qué tres cosas mirás de una tabla o un gráfico antes de hacer cualquier cuenta, y por qué.",
    },
    "cl-estrategias-polya": {
        "hook": {
            "question": "Con fósforos armás cuadrados en fila, pegados uno al otro. ¿Cuántos fósforos necesitás para 50 cuadrados? ¿Los dibujás todos?",
            "intuition": "No hace falta. **Simplificás**: 1 cuadrado lleva 4 fósforos, 2 llevan 7 y 3 llevan 10. **Armás una tabla**, **buscás el patrón** (cada cuadrado agrega 3: `3n + 1`), lo **verificás** con un caso nuevo (4 cuadrados → 13 fósforos) y recién ahí lo usás: 3 · 50 + 1 = 151. Resolver problemas es elegir estrategias así, no adivinar la cuenta.",
        },
        "concept": {
            "points": [
                "Un **problema** es una situación que plantea una distancia entre lo que sabés y lo que querés saber. El material lo compara con un viaje en tres etapas: **1.ª Comprendiendo el problema**, **2.ª Planificando y ejecutando**, **3.ª Revisando**. (Pólya, en quien se basa, separa cuatro pasos: comprender, concebir un plan, ejecutarlo y examinar la solución.) Si te perdés, volvés a empezar.",
                "**Comprendiendo el problema**: leé hasta poder contarlo con tus palabras e identificá la **incógnita** (qué te piden), los **datos** (cuáles sobran y cuáles faltan) y las **restricciones** (condiciones que debe cumplir la respuesta: números enteros, cifras distintas, nadie queda afuera). Ayuda armar el cuadro “Lo que sé | Lo que quiero hacer”.",
                "**Planificando y ejecutando**, estrategias: **hacer una tabla**; **dibujar** o hacer un esquema; **simplificar** (resolver casos chicos) y **buscar un patrón**; **ensayo y error registrado** (anotar cada intento y usar el error para ajustar el siguiente); **dividir en subproblemas**; **trabajar hacia atrás** (desde el resultado, deshaciendo cada operación con su inversa); **plantear una ecuación**, definiendo siempre la variable (“x = edad de Juan hoy, en años”).",
                "**Patrones de conteo**: n cuadrados en fila con lados compartidos usan `3n + 1` palitos; si n personas se saludan todas con todas, cada una saluda a n − 1, pero cada saludo se cuenta dos veces: `n(n − 1)/2`. Una fórmula sacada de una tabla se comprueba con un caso que no usaste para armarla.",
                "**Revisando**: ¿la respuesta contesta lo que se preguntó? ¿cumple todos los datos y restricciones del enunciado **original** (no solo tu ecuación, que podría estar mal planteada)? ¿tiene unidades y sentido (no hay 2,5 personas)? ¿había otro camino más corto?",
            ],
            "real_world": [
                {
                    "title": "Depurar un programa",
                    "detail": "Ante un error, un programador lo reproduce con el caso más chico posible y busca el patrón de cuándo falla: es simplificar y generalizar.",
                },
                {
                    "title": "Planificar una obra",
                    "detail": "El presupuesto de una casa se divide en subproblemas (fundaciones, estructura, instalaciones, terminaciones) que se calculan por separado y después se suman.",
                },
                {
                    "title": "Llegar a horario",
                    "detail": "Si el examen es a las 8:00, el colectivo tarda 50 min y caminás 10 min hasta la parada, se trabaja hacia atrás: hay que salir a las 7:00 como muy tarde.",
                },
            ],
            "key_rule": "Comprender (incógnita, datos, restricciones) → planificar y ejecutar (elegir una estrategia) → revisar contra el enunciado. Toda letra que uses lleva escrito qué significa.",
            "pitfall": "Empezar a hacer cuentas con los números del enunciado sin saber qué se pide, o generalizar un patrón visto en dos casos sin comprobarlo con un tercero.",
        },
        "example": {
            "title": "Trabajar hacia atrás: ¿cuánto dinero tenía Sofía?",
            "steps": [
                "**Comprendiendo**: Sofía gastó la mitad de su dinero en un libro, después $ 2000 en un café y luego la mitad de lo que le quedaba en un regalo. Le quedaron $ 3000. Incógnita: el dinero inicial. Datos: las tres operaciones y el resultado final. Restricción: todas las cantidades son positivas.",
                "**Planificando**: conocemos el final y las operaciones, así que conviene **trabajar hacia atrás**, deshaciendo cada paso con su operación inversa.",
                "**Ejecutando**:\n| Paso (desde el final) | Operación inversa | Dinero |\n|---|---|---|\n| Después del regalo | — | 3000 |\n| Antes del regalo (gastó la mitad) | × 2 | 6000 |\n| Antes del café (gastó 2000) | + 2000 | 8000 |\n| Antes del libro (gastó la mitad) | × 2 | 16 000 |",
                "**Revisando** con el enunciado original: 16 000 → libro, queda 8000 → café, queda 6000 → regalo, queda 3000 ✓.",
                "**Otro camino**: con x = dinero inicial (en $), (x/2 − 2000)/2 = 3000 → x/2 − 2000 = 6000 → x = 16 000. Las dos estrategias coinciden: Sofía tenía $ 16 000.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "¿Qué es la incógnita de un problema?",
            "options": [
                {"text": "Lo que el problema pide averiguar", "ok": True, "feedback": "Exacto: se identifica en la pregunta, y nombrarla con precisión es parte de comprender el problema."},
                {"text": "Los datos numéricos del enunciado", "ok": False, "feedback": "Los datos son lo que ya sabés; la incógnita es lo que querés saber."},
                {"text": "Siempre la letra x", "ok": False, "feedback": "La x es solo un nombre que vos elegís para la incógnita; puede llamarse t, m o como quieras, siempre que digas qué representa."},
            ],
        },
        "checks": [
            {
                "question": "Con palitos se arman triángulos en fila, cada uno compartiendo un lado con el anterior: 1 triángulo usa 3 palitos, 2 usan 5 y 3 usan 7. ¿Cuántos palitos usan n triángulos?",
                "options": [
                    {"text": "2n + 1", "ok": True, "feedback": "Exacto: cada triángulo nuevo agrega 2 palitos. Comprobá la fórmula con un caso que no usaste para armarla: n = 4 da 9 palitos, igual que al contarlos."},
                    {"text": "3n", "ok": False, "feedback": "Eso valdría si los triángulos estuvieran separados; al compartir un lado, cada uno nuevo agrega solo 2 palitos (con n = 2 daría 6, no 5)."},
                    {"text": "n + 2", "ok": False, "feedback": "Coincide con n = 1, pero con n = 2 da 4 y no 5: un patrón se comprueba con más de un caso."},
                ],
            },
            {
                "question": "En la etapa “Revisando”, ¿qué conviene hacer con la respuesta obtenida?",
                "options": [
                    {"text": "Comprobar que cumple todas las condiciones del enunciado original", "ok": True, "feedback": "Exacto: así se detectan tanto errores de cuentas como ecuaciones mal planteadas."},
                    {"text": "Reemplazarla solo en la ecuación que planteaste", "ok": False, "feedback": "Si la ecuación estaba mal planteada, la respuesta la cumple igual y el error pasa de largo: hay que volver al enunciado."},
                    {"text": "Darla por buena si es un número entero", "ok": False, "feedback": "Que sea entera no garantiza nada: puede ser entera y no cumplir los datos."},
                ],
            },
        ],
        "takeaway_prompt": "Elegí un problema que hayas resuelto hace poco y contá qué hiciste en cada una de las tres etapas y qué estrategia usaste.",
    },
    "cl-porcentajes-fracciones": {
        "hook": {
            "question": "Un producto aumenta un 20 % y al mes siguiente baja un 20 %. ¿Vuelve a su precio original?",
            "intuition": "No: si costaba $ 100, sube a $ 120 y después baja el 20 % **de 120**, o sea 24: queda en $ 96. Cada porcentaje se calcula sobre una base distinta. Con factores se ve directo: `× 1,2` y después `× 0,8` es `× 0,96`, un 4 % menos. La pregunta clave de todo problema de porcentajes es **¿de qué cantidad es ese porcentaje?**",
        },
        "concept": {
            "points": [
                "**Porcentaje directo**: el p % de una cantidad es `p/100 · cantidad`. Con **regla de tres**: 100 % ↔ total; p % ↔ x. **Qué porcentaje es una parte**: `parte/total · 100`. **Total a partir de una parte**: si el p % son k unidades, el total es `k · 100/p`.",
                "**Factor multiplicador**: un aumento del p % es `× (1 + p/100)` y un descuento del p % es `× (1 − p/100)`. **Porcentaje inverso**: si pagaste P con un descuento del d %, el precio original es `P ÷ (1 − d/100)`. **Descuento aplicado** = (original − pagado)/original · 100.",
                "**Porcentajes sucesivos**: se multiplican los factores, no se suman los porcentajes (+10 % y +10 % es `× 1,1 · 1,1 = × 1,21`, o sea +21 %). **Tope de reintegro**: el reintegro es el menor entre el p % del gasto y el tope; el gasto que aprovecha todo el tope es `tope ÷ (p/100)`, y el porcentaje real es reintegro/gasto · 100.",
                "**Porcentaje de un subgrupo**: “el 30 % de los que…” se calcula sobre ese subgrupo, no sobre el total. **Fracción de una cantidad**: `a/b` de N es `a · N/b`, y una fracción de una fracción se multiplica: 2/3 de 3/4 es 1/2.",
                "**Fracción del resto con total desconocido** (repartos, herencias, gastos): definí x = total y escribí lo que queda después de cada paso (si se usa 1/3, queda 2/3 · x; si después se usa 1/4 **del resto**, queda 3/4 · 2/3 · x). Al final, la fracción que queda por x es igual al dato conocido.",
                "**Mezclas**: la cantidad de sustancia pura se conserva: `c₁ · V₁ + c₂ · V₂ = c · (V₁ + V₂)`, con las concentraciones como decimales (30 % = 0,3). El agua tiene concentración 0 y el producto puro, 1.",
            ],
            "real_world": [
                {
                    "title": "Promociones con tope",
                    "detail": "“25 % de reintegro con tope de $ 5000” solo rinde el 25 % hasta un gasto de $ 20 000; más allá, el porcentaje real baja.",
                },
                {
                    "title": "Inflación acumulada",
                    "detail": "Un 3 % mensual durante 12 meses no es un 36 % anual: el factor es 1,03¹² ≈ 1,426, un 42,6 % acumulado.",
                },
                {
                    "title": "Diluciones en el laboratorio",
                    "detail": "Para pasar alcohol al 96 % a alcohol al 70 % se agrega agua conservando la cantidad de alcohol puro: es la ecuación de mezclas.",
                },
            ],
            "key_rule": "Todo porcentaje es “de algo”: identificá la base. Descuento d % → × (1 − d/100); original = pagado ÷ (1 − d/100); porcentajes sucesivos → se multiplican los factores; “del resto” → sobre lo que queda.",
            "pitfall": "Calcular el precio original sumándole a lo pagado el mismo porcentaje: si pagaste $ 80 con un 20 % de descuento, el original es $ 100, no $ 96 (el 20 % se aplicó sobre 100, no sobre 80).",
        },
        "example": {
            "title": "Un tanque que se vacía por partes",
            "steps": [
                "**Enunciado**: el lunes se usa 1/3 del agua de un tanque y el martes 3/4 de lo que quedaba. Todavía quedan 150 L. ¿Cuántos litros tenía el tanque? **Variable**: x = litros iniciales.",
                "**Lunes**: se usa 1/3 · x, así que queda 2/3 · x.",
                "**Martes**: se usa 3/4 **del resto**, o sea 3/4 · 2/3 · x, y queda 1/4 · 2/3 · x = 1/6 · x.",
                "**Ecuación**: 1/6 · x = 150 → x = 900 L.",
                "**Revisando**: 900 → el lunes se usan 300, quedan 600 → el martes se usan 3/4 · 600 = 450, quedan 150 ✓. Error típico: escribir el martes 3/4 · x (sobre el total) en lugar de 3/4 del resto.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Pagaste $ 6000 por un artículo con un 25 % de descuento. ¿Cuál era el precio original?",
            "options": [
                {"text": "$ 8000", "ok": True, "feedback": "Exacto: pagaste el 75 % del original, así que original = 6000 ÷ 0,75 = 8000."},
                {"text": "$ 7500", "ok": False, "feedback": "Le sumaste a lo pagado el 25 % de 6000, pero el descuento se calculó sobre el precio original: con un original de 7500 habrías pagado 7500 · 0,75 = 5625, no 6000."},
                {"text": "$ 4500", "ok": False, "feedback": "Le aplicaste otro descuento del 25 % a lo pagado: eso va en la dirección contraria."},
            ],
        },
        "checks": [
            {
                "question": "Un precio aumenta un 10 % y después otro 20 %. ¿Cuál es el aumento total?",
                "options": [
                    {"text": "32 %", "ok": True, "feedback": "Exacto: 1,1 · 1,2 = 1,32, o sea +32 %."},
                    {"text": "30 %", "ok": False, "feedback": "Sumaste los porcentajes; el segundo aumento se aplica sobre el precio ya aumentado, así que los factores se multiplican."},
                    {"text": "2 %", "ok": False, "feedback": "Multiplicaste los porcentajes como decimales (0,1 · 0,2 = 0,02); lo que se multiplica son los factores 1,1 y 1,2."},
                ],
            },
            {
                "question": "Se mezclan 2 L de jugo con 50 % de fruta y 3 L de agua. ¿Qué porcentaje de fruta tiene la mezcla?",
                "options": [
                    {"text": "20 %", "ok": True, "feedback": "Exacto: hay 0,5 · 2 = 1 L de fruta en 5 L de mezcla: 1/5 = 20 %."},
                    {"text": "25 %", "ok": False, "feedback": "Promediaste 50 % y 0 % como si los volúmenes fueran iguales; con 2 L y 3 L hay que ponderar."},
                    {"text": "33,3 %", "ok": False, "feedback": "Dividiste el litro de fruta por los 3 L de agua, pero la base es el volumen total de la mezcla (5 L)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con un ejemplo tuyo por qué un descuento del 20 % no se deshace con un aumento del 20 %.",
    },
    "cl-edades-sistemas": {
        "hook": {
            "question": "Hoy tenés 18 años y tu hermana 6: tenés el triple de su edad. ¿Vas a tener siempre el triple?",
            "intuition": "No. Lo que nunca cambia es la **diferencia**: siempre le vas a llevar 12 años. Dentro de 6 años tendrán 24 y 12 (el doble), y dentro de 24 años, 42 y 30. Por eso en los problemas de edades se escribe todo en función de la edad de **hoy**, y a todas las personas se les suman (o restan) los mismos años.",
        },
        "concept": {
            "points": [
                "**Definí la variable con su momento**: “x = edad del hijo HOY, en años”. **Hace a años** → `x − a`; **dentro de a años** → `x + a`. Todos envejecen lo mismo, así que **la diferencia de edades es constante**.",
                "**“Cuando yo tenía tu edad”**: eso pasó hace (mi edad − tu edad) años, exactamente la diferencia. Una tabla con filas por persona y columnas “hace… / hoy / dentro de…” ordena los datos.",
                "**Dos caminos, como pide el material**: por **ensayo y error con tabla** (hoy, +1 año, +1 año… hasta que se cumpla la condición) y por **ecuación**. Conviene hacer los dos: la tabla da intuición y la ecuación da rapidez. Ojo con los paréntesis: “el triple de la edad que tendrá” es `3.(x + a)`, no `3x + a` (en el ingreso el producto se marca con punto, `3.(x + a)`; es lo mismo que `3·(x + a)` o `3(x + a)`).",
                "**Sistemas 2×2**: por **sustitución** (despejás una incógnita en una ecuación y la reemplazás en la otra) o por **reducción** (sumás o restás las ecuaciones, multiplicándolas antes si hace falta, para eliminar una incógnita). Verificá en **las dos** ecuaciones.",
                "**Sistemas 3×3 sencillos**: si te dan las **sumas de a pares** (a + b, a + c, b + c), sumá las tres ecuaciones: `2(a + b + c)` = suma de los datos; con ese total, cada incógnita es total − la pareja que no la incluye. Si vienen **encadenadas** (M = 2H, N = 3(H + M)), sustituí todo en función de una sola.",
                "**Números consecutivos**: `n, n + 1, n + 2`; pares (o impares) consecutivos: `n, n + 2, n + 4`. La suma de tres consecutivos es el triple del número del medio.",
            ],
            "real_world": [
                {
                    "title": "Recaudación con dos precios",
                    "detail": "Boleterías y peajes con dos categorías: con el total de unidades y el total de dinero se arma un sistema 2×2 para saber cuántas hubo de cada una.",
                },
                {
                    "title": "Balances de masa",
                    "detail": "Mezclar dos soluciones para lograr un volumen y una concentración pedidos es un sistema 2×2: una ecuación para el volumen y otra para la sustancia.",
                },
                {
                    "title": "Circuitos eléctricos",
                    "detail": "Las leyes de Kirchhoff dan una ecuación por nodo o por malla con las corrientes como incógnitas: en Física II los sistemas 3×3 son de todos los días.",
                },
            ],
            "key_rule": "Variable = edad de HOY. Hace a años → x − a; dentro de a años → x + a, para TODOS; la diferencia de edades no cambia. Sistemas: sustitución o reducción, y verificación en todas las ecuaciones.",
            "pitfall": "Sumarle los años a una sola persona (“dentro de 5 años el padre tendrá x + 5” y el hijo sigue igual) u olvidar el paréntesis: “el doble de la edad dentro de 5 años” es 2.(x + 5) = 2x + 10, no 2x + 5.",
        },
        "example": {
            "title": "Madre de 40 e hija de 12: ¿cuándo tendrá el doble?",
            "steps": [
                "**Comprendiendo**: la madre tiene 40 años y su hija 12. Incógnita: dentro de cuántos años la edad de la madre será el doble de la de la hija. Variable: t = años que tienen que pasar.",
                "**Ensayo y error con tabla**:\n| Años que pasan | Madre | Hija | Doble de la hija |\n|---|---|---|---|\n| 0 | 40 | 12 | 24 |\n| 5 | 45 | 17 | 34 |\n| 10 | 50 | 22 | 44 |\n| 15 | 55 | 27 | 54 |\n| 16 | 56 | 28 | 56 |\nCada 5 años la distancia entre “Madre” y “Doble de la hija” se achica 5; en t = 16 coinciden.",
                "**Por ecuación**: 40 + t = 2.(12 + t) → 40 + t = 24 + 2t → t = 16.",
                "**Con la diferencia constante**: la madre siempre le lleva 28 años a la hija. Si la madre tiene el doble, la hija tiene justo esa diferencia: 28 años, o sea dentro de 28 − 12 = 16 años.",
                "**Revisando**: dentro de 16 años tendrán 56 y 28, y 56 = 2 · 28 ✓.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Juan tiene x años hoy. ¿Cómo se escribe “hace 4 años Juan tenía la mitad de la edad que tendrá dentro de 6 años”?",
            "options": [
                {"text": "x − 4 = (x + 6)/2", "ok": True, "feedback": "Exacto: la edad de hace 4 años es igual a la mitad de toda la edad futura (x + 6). Da x = 14."},
                {"text": "x − 4 = x/2 + 6", "ok": False, "feedback": "Falta el paréntesis: la mitad es de toda la edad futura, (x + 6)/2, no solo de x."},
                {"text": "(x − 4)/2 = x + 6", "ok": False, "feedback": "Invertiste la relación: la que es la mitad es la edad de hace 4 años, no la de dentro de 6."},
            ],
        },
        "checks": [
            {
                "question": "Resolvé el sistema x + y = 20 ; x − y = 4.",
                "options": [
                    {"text": "x = 12 e y = 8", "ok": True, "feedback": "Exacto: sumando, 2x = 24 → x = 12, y entonces y = 20 − 12 = 8. Verificación: 12 − 8 = 4 ✓."},
                    {"text": "x = 8 e y = 12", "ok": False, "feedback": "Cumple la suma, pero 8 − 12 = −4, no 4: intercambiaste las incógnitas."},
                    {"text": "x = 10 e y = 10", "ok": False, "feedback": "Cumple la primera ecuación, pero no la segunda (10 − 10 = 0): hay que usar las dos."},
                ],
            },
            {
                "question": "Tres números consecutivos suman 51. ¿Cuál es el mayor?",
                "options": [
                    {"text": "18", "ok": True, "feedback": "Exacto: n + (n + 1) + (n + 2) = 51 → 3n + 3 = 51 → n = 16; los números son 16, 17 y 18."},
                    {"text": "17", "ok": False, "feedback": "Ese es el del medio (51 ÷ 3); la pregunta pide el mayor."},
                    {"text": "16", "ok": False, "feedback": "Ese es n, el menor de los tres; el mayor es n + 2."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué la diferencia de edades entre dos personas no cambia nunca y cómo usarías ese hecho para resolver un problema.",
    },
    "cl-geometria-problemas": {
        "hook": {
            "question": "Una pileta mide 8 m de largo, 4 m de ancho y 1,5 m de profundidad. ¿Cuántos litros de agua hacen falta para llenarla?",
            "intuition": "El volumen es 8 · 4 · 1,5 = 48 m³, y como **1 m³ = 1000 L**, son **48 000 litros**. El salto de m³ a litros es de 1000 y no de 10: en volumen cada escalón de unidad multiplica por 1000 porque se repite en las tres dimensiones. Medir, convertir y dibujar bien son las tres herramientas de los problemas geométricos.",
        },
        "concept": {
            "points": [
                "**Ángulos en figuras**: los ángulos interiores de un triángulo suman **180°**; los de un polígono de n lados, **(n − 2) · 180°** (si es regular, cada uno mide eso dividido n). Los exteriores de cualquier polígono convexo suman 360°. Complementarios suman 90°, suplementarios 180°, y los opuestos por el vértice son iguales.",
                "**Ángulos entre paralelas** cortadas por una transversal: los **alternos internos** y los **correspondientes** son iguales; los **conjugados internos** (del mismo lado, entre las paralelas) suman 180°. En un triángulo, cada **ángulo exterior** es igual a la suma de los dos interiores no adyacentes.",
                "**Perímetro** (contorno, en m) y **área** (superficie, en m²): rectángulo `b · h`; triángulo `b · h/2`; trapecio `(B + b) · h/2`; círculo `π · r²` y circunferencia `2 · π · r`. **Figuras compuestas**: el área se calcula sumando partes o restando un recorte; en el perímetro solo va el borde exterior, nunca los lados internos.",
                "**Volumen y capacidad**: prisma o cilindro = área de la base × altura (`π · r² · h` en el cilindro); pirámide y cono = 1/3 de base × altura; esfera `4/3 · π · r³`. **1 dm³ = 1 L**, 1 m³ = 1000 L y 1 cm³ = 1 mL.",
                "**Conversión de unidades**: en longitud cada escalón (km, hm, dam, m, dm, cm, mm) es × 10; en área, × 100 (1 m² = 10 000 cm²); en volumen, × 1000 (1 m³ = 1 000 000 cm³). Antes de operar, todo en la misma unidad. 1 ha = 10 000 m².",
                "**Figuras descriptas en palabras**: hacé un croquis (la estrategia “dibujar” del material), marcá los datos y poné la incógnita en la figura. “Un rectángulo cuyo largo es el triple del ancho y su perímetro es 48 m” → ancho x, largo 3x → 2.(3x + x) = 48 → x = 6: mide 6 m × 18 m.",
            ],
            "real_world": [
                {
                    "title": "Pintar un aula",
                    "detail": "Se calcula el área de las paredes, se restan puertas y ventanas y se divide por el rendimiento de la pintura (m² por litro) para saber cuántos litros comprar.",
                },
                {
                    "title": "Hormigón para una losa",
                    "detail": "El camión mixer se encarga en m³: largo × ancho × espesor, con el espesor pasado de cm a m (12 cm = 0,12 m).",
                },
                {
                    "title": "Tanques de agua",
                    "detail": "La capacidad en litros de un tanque cilíndrico sale de π · r² · h en m³, multiplicado por 1000.",
                },
            ],
            "key_rule": "Triángulo: 180°; polígono: (n − 2) · 180°. Perímetro en m, área en m², volumen en m³. Escalones: × 10 en longitud, × 100 en área, × 1000 en volumen; 1 dm³ = 1 L.",
            "pitfall": "Convertir 2 m² a cm² multiplicando por 100 (200 cm²) en lugar de por 10 000 (20 000 cm²), o sumar en el perímetro de una figura compuesta un lado que quedó adentro.",
        },
        "example": {
            "title": "Patio en forma de L con contrapiso",
            "steps": [
                "**Enunciado**: un patio es un rectángulo de 10 m × 6 m al que le falta, en una esquina, un rectángulo de 4 m × 3 m. Se le hará un contrapiso de 8 cm de espesor. Croquis: la L tiene lados de 10, 3, 4, 3, 6 y 6 m.",
                "**Área por resta**: 10 · 6 − 4 · 3 = 60 − 12 = **48 m²**.",
                "**Perímetro**: recorriendo el borde, 10 + 3 + 4 + 3 + 6 + 6 = **32 m**. Es el mismo perímetro que el rectángulo completo: el recorte de la esquina cambia dos lados de lugar pero no su largo total.",
                "**Volumen**: el espesor pasa a metros (8 cm = 0,08 m): 48 m² · 0,08 m = **3,84 m³**.",
                "**Capacidad**: 3,84 m³ = 3840 dm³ = **3840 L** de mezcla. Revisando: las unidades cierran (m² · m = m³) y el orden de magnitud es razonable para un patio.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "¿Cuánto suman los ángulos interiores de un hexágono?",
            "options": [
                {"text": "720°", "ok": True, "feedback": "Exacto: (6 − 2) · 180° = 720°."},
                {"text": "1080°", "ok": False, "feedback": "Multiplicaste 6 · 180°; un polígono de n lados se divide en n − 2 triángulos, no en n."},
                {"text": "360°", "ok": False, "feedback": "360° es la suma de los ángulos exteriores (o de los interiores de un cuadrilátero), no de los interiores del hexágono."},
            ],
        },
        "checks": [
            {
                "question": "¿A cuántos centímetros cuadrados equivalen 3 m²?",
                "options": [
                    {"text": "30 000 cm²", "ok": True, "feedback": "Exacto: 1 m² = 100 cm · 100 cm = 10 000 cm², así que 3 m² = 30 000 cm²."},
                    {"text": "300 cm²", "ok": False, "feedback": "Multiplicaste por 100 como en longitud; en área el factor se eleva al cuadrado: 100² = 10 000."},
                    {"text": "3 000 000 cm²", "ok": False, "feedback": "Multiplicaste por 1 000 000, que es el factor de m³ a cm³ (volumen), no de área."},
                ],
            },
            {
                "question": "Dos paralelas son cortadas por una transversal y un ángulo conjugado interno mide 65°. ¿Cuánto mide el otro conjugado interno?",
                "options": [
                    {"text": "115°", "ok": True, "feedback": "Exacto: los conjugados internos son suplementarios: 180° − 65° = 115°."},
                    {"text": "65°", "ok": False, "feedback": "Iguales son los alternos internos y los correspondientes; los conjugados internos suman 180°."},
                    {"text": "25°", "ok": False, "feedback": "Calculaste el complemento (90° − 65°); los conjugados internos son suplementarios, no complementarios."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con un dibujo mental por qué 1 m² son 10 000 cm² y 1 m³ son 1000 litros.",
    },
}
