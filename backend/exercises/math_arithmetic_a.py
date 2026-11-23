"""Ejercicios de Matemática: Aritmética (parte A).

Tres problemas por tema (niveles 1, 2 y 3) para valor posicional, las cuatro operaciones con
números naturales y fracciones (entender, sumar y restar). Son problemas de planteo con
situaciones cotidianas: hay que decidir qué operaciones hacer y encadenarlas. Todos los
resultados son exactos (tolerance 0).
"""

EXERCISES: list[dict] = [
    # ---------- a-valor-posicional ----------
    {
        "id": "a-valor-posicional-1",
        "node": "a-valor-posicional",
        "kind": "problem",
        "level": 1,
        "title": "Una transferencia con un dígito corrido",
        "statement": "Martina tiene que transferirle al dueño de su departamento **trescientos cuatro mil sesenta pesos** de alquiler. Apurada, tipea en el home banking el número `340 060` y confirma la operación.",
        "parts": [
            {
                "prompt": "a) ¿Qué número tendría que haber tipeado? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 304060, "tolerance": 0, "unit": "$"},
                "answer": "$304 060",
            },
            {
                "prompt": "b) ¿Cuántos pesos de más transfirió? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 36000, "tolerance": 0, "unit": "$"},
                "answer": "$36 000",
            },
        ],
        "hints": [
            "Separá el número dicho en palabras en clases: \"trescientos cuatro mil\" es la parte de los miles y \"sesenta\" la de las unidades. ¿Qué columnas quedan vacías?",
            "Para el inciso b), restá el número correcto al que tipeó. También podés comparar columna por columna qué dígitos cambiaron de lugar.",
        ],
        "solution": [
            "\"Trescientos cuatro mil\" = `304 000` (3 centenas de mil, 0 decenas de mil, 4 unidades de mil). \"Sesenta\" = `60`.",
            "Juntando: `304 000 + 60 = 304 060`. Los ceros guardan el lugar de las decenas de mil, las centenas y las unidades.",
            "Martina tipeó `340 060`: el 4 quedó en las decenas de mil (vale `40 000`) en lugar de las unidades de mil (`4000`), y el 0 pasó a los miles.",
            "Diferencia: `340 060 − 304 060 = 36 000`.",
            "Verificación por posiciones: en `340 060` hay `40 000` en esas dos columnas y en `304 060` hay `4000`; `40 000 − 4000 = 36 000`.",
            "Respuestas: debía tipear $304 060 y transfirió $36 000 de más. Error típico: escribir el número como `3 004 060` (\"300\" y \"4 mil\" por separado) o como `34 060` (sin los ceros guardalugar).",
        ],
    },
    {
        "id": "a-valor-posicional-2",
        "node": "a-valor-posicional",
        "kind": "problem",
        "level": 2,
        "title": "Estimar antes de llegar a la caja",
        "statement": "Una familia quiere renovar electrodomésticos y tiene ahorrado exactamente **$1 000 000**. Los precios son: heladera **$487 350**, lavarropas **$362 900** y microondas **$149 650**. Antes de sumar con cuidado, estiman el total redondeando cada precio a la **decena de mil** más cercana.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto da la estimación (suma de los tres precios redondeados)? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 1000000, "tolerance": 0, "unit": "$"},
                "answer": "$1 000 000",
            },
            {
                "prompt": "b) ¿Cuánto es el total exacto? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 999900, "tolerance": 0, "unit": "$"},
                "answer": "$999 900",
            },
            {
                "prompt": "c) Si compran los tres, ¿cuánto dinero les sobra de lo ahorrado? Respondé solo con el número en pesos.",
                "check": {"type": "numeric", "value": 100, "tolerance": 0, "unit": "$"},
                "answer": "$100",
            },
        ],
        "hints": [
            "Para redondear a la decena de mil, mirá el dígito de las unidades de mil: si es 5 o más, subís; si es 4 o menos, dejás.",
            "Para la suma exacta alineá las columnas y acordate de lo que llevás; después compará con lo ahorrado.",
        ],
        "solution": [
            "Heladera `487 350`: la cifra de los miles es 7 (≥ 5), se sube → `490 000`.",
            "Lavarropas `362 900`: la cifra de los miles es 2 (< 5), se deja → `360 000`. Microondas `149 650`: la cifra de los miles es 9 (≥ 5) → `150 000`.",
            "Estimación: `490 000 + 360 000 + 150 000 = 1 000 000`.",
            "Suma exacta: `487 350 + 362 900 = 850 250`; `850 250 + 149 650 = 999 900`.",
            "Lo que sobra: `1 000 000 − 999 900 = 100`.",
            "Respuestas: estimación $1 000 000, total exacto $999 900 y sobran $100. Moraleja: la estimación sirve para tener una idea rápida, pero cuando el resultado queda tan pegado al límite hay que hacer la cuenta exacta para saber si alcanza.",
        ],
    },
    {
        "id": "a-valor-posicional-3",
        "node": "a-valor-posicional",
        "kind": "problem",
        "level": 3,
        "title": "Seis tarjetas con dígitos",
        "statement": "En un juego de mesa tenés seis tarjetas con los dígitos **0, 2, 5, 7, 8 y 9**. Con las seis tarjetas, usando cada una exactamente una vez, se arman números de seis cifras (el 0 no puede ir adelante).",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el mayor número que se puede armar? Respondé solo con el número, sin puntos de miles.",
                "check": {"type": "numeric", "value": 987520, "tolerance": 0, "unit": ""},
                "answer": "987 520",
            },
            {
                "prompt": "b) ¿Cuál es el menor número de seis cifras que se puede armar? Respondé solo con el número, sin puntos de miles.",
                "check": {"type": "numeric", "value": 205789, "tolerance": 0, "unit": ""},
                "answer": "205 789",
            },
            {
                "prompt": "c) ¿Cuál es el número que se puede armar que queda más cerca de 500 000? Respondé solo con el número, sin puntos de miles.",
                "check": {"type": "numeric", "value": 502789, "tolerance": 0, "unit": ""},
                "answer": "502 789",
            },
        ],
        "hints": [
            "La columna de la izquierda (centenas de mil) es la que más pesa: decidí primero qué dígito va ahí y después seguí hacia la derecha.",
            "Para el menor, el 0 no puede ir primero, pero sí puede ir segundo.",
            "Para el c), probá los mejores candidatos por arriba y por abajo de 500 000: ¿qué dígitos pueden ir en las centenas de mil? Calculá la distancia de cada candidato a 500 000.",
        ],
        "solution": [
            "Mayor: en cada posición, de izquierda a derecha, ponés el dígito más grande disponible → `987 520`.",
            "Menor: en las centenas de mil va el menor dígito distinto de 0, que es 2; después el 0 y el resto en orden creciente → `205 789`.",
            "Para acercarse a `500 000` por arriba hay que empezar con 5 (no hay 4 ni 6 que compita). El menor número que empieza con 5 tiene después el 0 y los demás en orden creciente: `502 789`, que está a `502 789 − 500 000 = 2789`.",
            "Por abajo no hay 4: el mayor número menor que `500 000` empieza con 2 y es `298 750`, que está a `500 000 − 298 750 = 201 250`. Cualquier número que empiece con 7, 8 o 9 ya está a más de `200 000`.",
            "Como `2789 < 201 250`, el más cercano es `502 789`.",
            "Respuestas: 987 520; 205 789; 502 789. Error típico en b): poner el 0 adelante (`025 789` no es de seis cifras).",
        ],
    },
    # ---------- a-suma-resta ----------
    {
        "id": "a-suma-resta-1",
        "node": "a-suma-resta",
        "kind": "problem",
        "level": 1,
        "title": "Lo que queda del sueldo",
        "statement": "Lucía cobra **$485 000** por mes. Este mes pagó el alquiler (**$210 000**), las expensas (**$38 500**) y gastó **$97 650** en el supermercado. Lo que le queda lo quiere juntar para comprarse una bicicleta que cuesta **$180 000**.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto dinero le queda después de esos gastos? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 138850, "tolerance": 0, "unit": "$"},
                "answer": "$138 850",
            },
            {
                "prompt": "b) ¿Cuánto le falta para la bicicleta si usa todo lo que le quedó? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 41150, "tolerance": 0, "unit": "$"},
                "answer": "$41 150",
            },
        ],
        "hints": [
            "Podés sumar primero todos los gastos y restar una sola vez del sueldo.",
            "Para b), restá lo que le quedó del precio de la bici (o contá cuánto falta para llegar).",
        ],
        "solution": [
            "Gastos totales: `210 000 + 38 500 = 248 500`; `248 500 + 97 650 = 346 150`.",
            "Lo que queda: `485 000 − 346 150 = 138 850`.",
            "Verificación con suma: `138 850 + 346 150 = 485 000` ✓.",
            "Lo que falta para la bici: `180 000 − 138 850 = 41 150` (contando hacia arriba: `+1150` llega a `140 000` y `+40 000` llega a `180 000`).",
            "Respuestas: le quedan $138 850 y le faltan $41 150. Error típico: en la resta con ceros (`485 000 − 346 150`) olvidarse de pedir prestado a través de los ceros.",
        ],
    },
    {
        "id": "a-suma-resta-2",
        "node": "a-suma-resta",
        "kind": "problem",
        "level": 2,
        "title": "El odómetro en el viaje a Mendoza",
        "statement": "Una familia viaja en auto de Buenos Aires a Mendoza. Al salir, el odómetro marca **87 465 km**. Paran a almorzar en Río Cuarto y el odómetro marca **88 073 km**. Según el GPS, el viaje completo es de **1047 km**.",
        "parts": [
            {
                "prompt": "a) ¿Cuántos kilómetros recorrieron hasta Río Cuarto? Respondé solo con el número en km.",
                "check": {"type": "numeric", "value": 608, "tolerance": 0, "unit": "km"},
                "answer": "608 km",
            },
            {
                "prompt": "b) ¿Qué marcará el odómetro al llegar a Mendoza? Respondé solo con el número en km, sin puntos de miles.",
                "check": {"type": "numeric", "value": 88512, "tolerance": 0, "unit": "km"},
                "answer": "88 512 km",
            },
            {
                "prompt": "c) ¿Cuántos kilómetros les faltan desde Río Cuarto? Respondé solo con el número en km.",
                "check": {"type": "numeric", "value": 439, "tolerance": 0, "unit": "km"},
                "answer": "439 km",
            },
        ],
        "hints": [
            "Los kilómetros recorridos son la diferencia entre dos lecturas del odómetro.",
            "La lectura final es la inicial más todo el viaje. Lo que falta desde Río Cuarto se puede calcular de dos maneras: comparando lecturas o restando lo ya hecho del total.",
        ],
        "solution": [
            "Hasta Río Cuarto: `88 073 − 87 465`. Contando hacia arriba: de `87 465` a `87 500` hay 35, de `87 500` a `88 000` hay 500, y de `88 000` a `88 073` hay 73 → `35 + 500 + 73 = 608 km`.",
            "Lectura al llegar: `87 465 + 1047 = 88 512 km`.",
            "Lo que falta desde Río Cuarto: `88 512 − 88 073 = 439 km`.",
            "Verificación por otro camino: `1047 − 608 = 439 km` ✓.",
            "Respuestas: 608 km, el odómetro marcará 88 512 km y faltan 439 km. Error típico: restar columna por columna \"el mayor menos el menor\" (en las unidades, `5 − 3`) en lugar de pedir prestado.",
        ],
    },
    {
        "id": "a-suma-resta-3",
        "node": "a-suma-resta",
        "kind": "problem",
        "level": 3,
        "title": "La caja de la cooperadora",
        "statement": "La cooperadora de una escuela empezó el mes con **$253 480** en caja. Durante el mes cobró **$186 750** por una rifa y **$94 300** de cuotas de socios. Pagó **$312 900** de pintura y una compra de materiales cuyo comprobante se perdió. Al cerrar el mes quedaron **$79 630** en caja. El mes próximo esperan cobrar la misma cantidad de cuotas y no tener otros ingresos, y quieren comprar un toldo de **$250 000**.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto ingresó en total durante el mes? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 281050, "tolerance": 0, "unit": "$"},
                "answer": "$281 050",
            },
            {
                "prompt": "b) ¿Cuánto se pagó por los materiales? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 142000, "tolerance": 0, "unit": "$"},
                "answer": "$142 000",
            },
            {
                "prompt": "c) ¿Cuánto dinero les faltará para el toldo cuando cobren las cuotas del mes próximo? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 76070, "tolerance": 0, "unit": "$"},
                "answer": "$76 070",
            },
        ],
        "hints": [
            "Armá el balance: saldo inicial + ingresos − egresos = saldo final.",
            "Calculá cuánto tendría que haber quedado si solo se hubiera pagado la pintura; la diferencia con el saldo real es lo que costaron los materiales.",
            "Para c), el punto de partida del mes próximo es el saldo final de este mes.",
        ],
        "solution": [
            "Ingresos del mes: `186 750 + 94 300 = 281 050`.",
            "Dinero disponible: `253 480 + 281 050 = 534 530`.",
            "Después de pagar la pintura: `534 530 − 312 900 = 221 630`.",
            "Como al final quedaron `79 630`, los materiales costaron `221 630 − 79 630 = 142 000`.",
            "Verificación: `534 530 − 312 900 − 142 000 = 79 630` ✓.",
            "Mes próximo: `79 630 + 94 300 = 173 930`; falta `250 000 − 173 930 = 76 070`.",
            "Respuestas: ingresaron $281 050, los materiales costaron $142 000 y faltarán $76 070. Error típico: en c) olvidarse del saldo que ya había en caja y calcular `250 000 − 94 300`.",
        ],
    },
    # ---------- a-intro-multiplicacion ----------
    {
        "id": "a-intro-multiplicacion-1",
        "node": "a-intro-multiplicacion",
        "kind": "problem",
        "level": 1,
        "title": "Panes y salchichas para el cumpleaños",
        "statement": "Para un cumpleaños, Martín compra **6 paquetes de pan de pancho** que traen **8 panes** cada uno y **7 paquetes de salchichas** que traen **6 salchichas** cada uno. Cada pancho lleva un pan y una salchicha.",
        "parts": [
            {
                "prompt": "a) ¿Cuántos panchos completos puede armar? Respondé solo con el número en panchos.",
                "check": {"type": "numeric", "value": 42, "tolerance": 0, "unit": "panchos"},
                "answer": "42 panchos",
            },
            {
                "prompt": "b) Del producto que sobra, ¿cuántas unidades quedan sin usar? Respondé solo con el número en unidades.",
                "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": "unidades"},
                "answer": "6 unidades (sobran 6 panes)",
            },
            {
                "prompt": "c) ¿Cuántos paquetes de salchichas más tendría que comprar, como mínimo, para usar todos los panes? Respondé solo con el número en paquetes.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": "paquetes"},
                "answer": "1 paquete",
            },
        ],
        "hints": [
            "Calculá por separado cuántos panes y cuántas salchichas hay en total (grupos iguales).",
            "La cantidad de panchos la limita lo que haya en menor cantidad.",
        ],
        "solution": [
            "Panes: `6 × 8 = 48`. Salchichas: `7 × 6 = 42`.",
            "Cada pancho usa uno de cada cosa, así que se arman tantos panchos como el menor de los dos: `42` panchos.",
            "Sobran panes: `48 − 42 = 6`.",
            "Para usar esos 6 panes hacen falta 6 salchichas más, y un paquete trae exactamente 6: alcanza con `1` paquete (`8 × 6 = 48` salchichas para `48` panes).",
            "Respuestas: 42 panchos, sobran 6 panes, falta 1 paquete de salchichas. Error típico: confundir los factores y calcular `6 × 6` o `7 × 8`.",
        ],
    },
    {
        "id": "a-intro-multiplicacion-2",
        "node": "a-intro-multiplicacion",
        "kind": "problem",
        "level": 2,
        "title": "Las butacas del teatro del barrio",
        "statement": "En el teatro de un barrio, la platea tiene **9 filas de 8 butacas** y el pullman tiene **6 filas de 7 butacas**. Para una función escolar se reservan **2 filas completas de platea** para los docentes y todas las demás butacas son para alumnos.",
        "parts": [
            {
                "prompt": "a) ¿Cuántas butacas tiene el teatro en total? Respondé solo con el número en butacas.",
                "check": {"type": "numeric", "value": 114, "tolerance": 0, "unit": "butacas"},
                "answer": "114 butacas",
            },
            {
                "prompt": "b) ¿Cuántas butacas quedan para alumnos? Respondé solo con el número en butacas.",
                "check": {"type": "numeric", "value": 98, "tolerance": 0, "unit": "butacas"},
                "answer": "98 butacas",
            },
            {
                "prompt": "c) ¿Cuántas butacas más tiene la platea que el pullman? Respondé solo con el número en butacas.",
                "check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": "butacas"},
                "answer": "30 butacas",
            },
        ],
        "hints": [
            "Cada sector es un rectángulo de filas × butacas por fila.",
            "Las filas reservadas son de platea: ¿cuántas butacas son 2 filas de 8?",
        ],
        "solution": [
            "Platea: `9 × 8 = 72` (truco del 9: `10 × 8 − 8 = 72`).",
            "Pullman: `6 × 7 = 42` (`6 × 5 + 6 × 2 = 30 + 12`).",
            "Total: `72 + 42 = 114` butacas.",
            "Reservadas para docentes: `2 × 8 = 16`. Para alumnos: `114 − 16 = 98`.",
            "Diferencia entre sectores: `72 − 42 = 30`.",
            "Respuestas: 114, 98 y 30 butacas. Error típico en b): restar 2 butacas, o 2 filas de 7 (las filas reservadas son de platea, con 8 butacas cada una).",
        ],
    },
    {
        "id": "a-intro-multiplicacion-3",
        "node": "a-intro-multiplicacion",
        "kind": "problem",
        "level": 3,
        "title": "Paquetes de lápices mezclados",
        "statement": "En una librería venden lápices en paquetes de **6** y en paquetes de **8**. Joaquín compró **9 paquetes** en total (de los dos tipos) y, al abrirlos, contó **62 lápices**. El paquete de 6 cuesta **$900** y el de 8 cuesta **$1200**.",
        "parts": [
            {
                "prompt": "a) ¿Cuántos paquetes de 8 lápices compró? Respondé solo con el número en paquetes.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "paquetes"},
                "answer": "4 paquetes de 8",
            },
            {
                "prompt": "b) ¿Cuánto pagó en total? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 9300, "tolerance": 0, "unit": "$"},
                "answer": "$9300",
            },
        ],
        "hints": [
            "Imaginá que los 9 paquetes fueran de 6: ¿cuántos lápices habría? ¿Cuántos faltan para llegar a 62?",
            "Cada vez que cambiás un paquete de 6 por uno de 8, el total sube en 2 lápices.",
        ],
        "solution": [
            "Si los 9 paquetes fueran de 6: `9 × 6 = 54` lápices. Faltan `62 − 54 = 8` lápices.",
            "Cambiar un paquete de 6 por uno de 8 agrega `8 − 6 = 2` lápices. Para agregar 8 hacen falta 4 cambios (`4 × 2 = 8`).",
            "Entonces compró 4 paquetes de 8 y `9 − 4 = 5` paquetes de 6. Verificación: `5 × 6 + 4 × 8 = 30 + 32 = 62` ✓.",
            "Costo: `5 × 900 = 4500` y `4 × 1200 = 4800`; total `4500 + 4800 = 9300`.",
            "Control: en los dos paquetes cada lápiz sale $150 (`900 = 6 × 150` y `1200 = 8 × 150`), y `62 × 150 = 9300` ✓.",
            "Respuestas: 4 paquetes de 8 y $9300. Error típico: dividir 62 por 8 o por 6 sin tener en cuenta que hay 9 paquetes en total.",
        ],
    },
    # ---------- a-intro-division ----------
    {
        "id": "a-intro-division-1",
        "node": "a-intro-division",
        "kind": "problem",
        "level": 1,
        "title": "Cuentas claras del fin de semana",
        "statement": "Cuatro amigos se van un fin de semana y acuerdan dividir **todos** los gastos en partes iguales. Juan pagó la cabaña (**$48 000**) y la nafta (**$36 000**); Sol pagó el supermercado (**$28 000**); Tomi y Lu no pagaron nada durante el viaje.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto le corresponde pagar a cada uno? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 28000, "tolerance": 0, "unit": "$"},
                "answer": "$28 000",
            },
            {
                "prompt": "b) Al volver, ¿cuánto dinero tiene que recibir Juan en total de los demás? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 56000, "tolerance": 0, "unit": "$"},
                "answer": "$56 000",
            },
        ],
        "hints": [
            "Primero sumá todo lo que se gastó y repartilo entre las 4 personas.",
            "Juan puso más de lo que le toca: lo que debe recibir es lo que pagó menos su parte.",
        ],
        "solution": [
            "Gasto total: `48 000 + 36 000 + 28 000 = 112 000`.",
            "Parte de cada uno: `112 000 ÷ 4 = 28 000` (porque `4 × 28 000 = 112 000`).",
            "Juan pagó `48 000 + 36 000 = 84 000`; le correspondía `28 000`, así que tiene que recibir `84 000 − 28 000 = 56 000`.",
            "Sol pagó justo su parte (`28 000`), así que no da ni recibe. Tomi y Lu le pagan `28 000` cada uno a Juan: `2 × 28 000 = 56 000` ✓.",
            "Respuestas: $28 000 cada uno y Juan recibe $56 000. Error típico: dividir solo lo que pagó Juan entre 4 y olvidar el gasto de Sol.",
        ],
    },
    {
        "id": "a-intro-division-2",
        "node": "a-intro-division",
        "kind": "problem",
        "level": 2,
        "title": "Torneo de fútbol 5",
        "statement": "Un club organiza un torneo de fútbol 5 y se anotan **38 chicos**. Cada equipo tiene exactamente **5 jugadores** (no hay suplentes) y solo juegan equipos completos. Para el torneo se necesita **una pelota por equipo**, y las pelotas se venden en bolsas de **4**.",
        "parts": [
            {
                "prompt": "a) ¿Cuántos equipos completos se pueden formar? Respondé solo con el número en equipos.",
                "check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": "equipos"},
                "answer": "7 equipos",
            },
            {
                "prompt": "b) ¿Cuántos chicos más tendrían que anotarse para formar un equipo más? Respondé solo con el número en chicos.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "chicos"},
                "answer": "2 chicos",
            },
            {
                "prompt": "c) Con los equipos del inciso a), ¿cuántas bolsas de pelotas hay que comprar como mínimo? Respondé solo con el número en bolsas.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "bolsas"},
                "answer": "2 bolsas",
            },
        ],
        "hints": [
            "Hacé la división con resto `38 ÷ 5`: el cociente y el resto responden preguntas distintas.",
            "En c) el resto se interpreta al revés que en a): si las pelotas de una bolsa no alcanzan, hace falta otra bolsa entera.",
        ],
        "solution": [
            "`38 ÷ 5`: `5 × 7 = 35` y `38 − 35 = 3` → cociente 7, resto 3.",
            "a) Solo juegan equipos completos: se forman 7 equipos y quedan 3 chicos sin equipo (acá el resto se descarta).",
            "b) Para un octavo equipo hacen falta 5 chicos y hay 3: faltan `5 − 3 = 2`.",
            "c) Hacen falta 7 pelotas. `7 ÷ 4`: `4 × 1 = 4`, resto 3. Una bolsa no alcanza y sobran 3 equipos sin pelota, así que hay que comprar otra bolsa: `2` bolsas (8 pelotas).",
            "Respuestas: 7 equipos, faltan 2 chicos y 2 bolsas. Error típico: responder 1 bolsa en c) (redondear para abajo cuando el resto obliga a redondear para arriba).",
        ],
    },
    {
        "id": "a-intro-division-3",
        "node": "a-intro-division",
        "kind": "problem",
        "level": 3,
        "title": "¿Cuántas medialunas hizo la panadería?",
        "statement": "Una panadería hizo una tanda de **entre 50 y 60 medialunas**. Si las empaqueta en bolsas de **6**, le sobran **5**; si en cambio las empaqueta en bolsas de **9**, le sobran **8**.",
        "parts": [
            {
                "prompt": "a) ¿Cuántas medialunas hizo? Respondé solo con el número en medialunas.",
                "check": {"type": "numeric", "value": 53, "tolerance": 0, "unit": "medialunas"},
                "answer": "53 medialunas",
            },
            {
                "prompt": "b) ¿Cuántas bolsas de 6 completas llena? Respondé solo con el número en bolsas.",
                "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": "bolsas"},
                "answer": "8 bolsas",
            },
            {
                "prompt": "c) Si las empaquetara en bolsas de 7, ¿cuántas medialunas le sobrarían? Respondé solo con el número en medialunas.",
                "check": {"type": "numeric", "value": 4,"tolerance": 0, "unit": "medialunas"},
                "answer": "4 medialunas",
            },
        ],
        "hints": [
            "Recordá que número = divisor × cociente + resto. Listá los números entre 50 y 60 que dejan resto 5 al dividir por 6.",
            "Truco: sobran 5 de a 6 y 8 de a 9, es decir, siempre falta UNA para completar otra bolsa. ¿Qué pasa si agregás una medialuna?",
        ],
        "solution": [
            "Los números entre 50 y 60 que dan resto 5 al dividir por 6 son de la forma `6 × cociente + 5`: `6 × 8 + 5 = 53` y `6 × 9 + 5 = 59`.",
            "Probamos con 9: `53 = 9 × 5 + 8` → resto 8 ✓. `59 = 9 × 6 + 5` → resto 5 ✗. La cantidad es 53.",
            "Otra forma: con una medialuna más se completarían las bolsas en los dos casos, así que `N + 1` es múltiplo de 6 y de 9, es decir de 18. Entre 51 y 61 el único múltiplo de 18 es 54, y `N = 54 − 1 = 53`.",
            "Bolsas de 6 completas: `53 = 6 × 8 + 5` → 8 bolsas.",
            "Bolsas de 7: `7 × 7 = 49` y `53 − 49 = 4` → sobran 4.",
            "Respuestas: 53 medialunas, 8 bolsas y sobran 4. Error típico: dar 59 sin comprobar la segunda condición.",
        ],
    },
    # ---------- a-multiplicar-varios-digitos ----------
    {
        "id": "a-multiplicar-varios-digitos-1",
        "node": "a-multiplicar-varios-digitos",
        "kind": "problem",
        "level": 1,
        "title": "Uniformes para el equipo de vóley",
        "statement": "Un colegio encarga uniformes para **48 alumnos**. Cada uniforme lleva una remera de **$12 350** y un short de **$8 650**.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto cuestan en total las 48 remeras? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 592800, "tolerance": 0, "unit": "$"},
                "answer": "$592 800",
            },
            {
                "prompt": "b) ¿Cuánto cuesta el pedido completo (remeras y shorts)? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 1008000, "tolerance": 0, "unit": "$"},
                "answer": "$1 008 000",
            },
        ],
        "hints": [
            "Para a), descomponé uno de los factores: por ejemplo `48 = 50 − 2` o `40 + 8`.",
            "Para b), antes de multiplicar dos veces por 48, fijate cuánto cuesta un uniforme completo.",
        ],
        "solution": [
            "Remeras: `48 × 12 350 = 50 × 12 350 − 2 × 12 350`.",
            "`50 × 12 350 = 617 500` y `2 × 12 350 = 24 700`, así que `617 500 − 24 700 = 592 800`.",
            "Un uniforme completo: `12 350 + 8 650 = 21 000`.",
            "Pedido completo: `48 × 21 000 = 48 × 21 × 1000 = 1008 × 1000 = 1 008 000` (`48 × 21 = 48 × 20 + 48 = 960 + 48 = 1008`).",
            "Verificación: shorts `48 × 8 650 = 415 200` y `592 800 + 415 200 = 1 008 000` ✓.",
            "Respuestas: $592 800 y $1 008 000. Estimación de control: `50 × 20 000 = 1 000 000`, muy cerca.",
        ],
    },
    {
        "id": "a-multiplicar-varios-digitos-2",
        "node": "a-multiplicar-varios-digitos",
        "kind": "problem",
        "level": 2,
        "title": "¿Conviene el plan anual?",
        "statement": "Una familia paga **$23 900** por mes de internet y **$15 750** por mes de celular. La empresa le ofrece un plan anual que incluye los dos servicios por **$412 000** pagados una sola vez por los 12 meses.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto pagaría en un año por los dos servicios si sigue pagando mes a mes? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 475800, "tolerance": 0, "unit": "$"},
                "answer": "$475 800",
            },
            {
                "prompt": "b) ¿Cuánto ahorra en el año si elige el plan anual? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 63800, "tolerance": 0, "unit": "$"},
                "answer": "$63 800",
            },
        ],
        "hints": [
            "Sumá primero el gasto de un mes y después multiplicalo por la cantidad de meses.",
            "Para multiplicar por 12, podés hacer ×10 y sumarle el doble.",
        ],
        "solution": [
            "Gasto mensual: `23 900 + 15 750 = 39 650`.",
            "Gasto anual mes a mes: `12 × 39 650 = 10 × 39 650 + 2 × 39 650 = 396 500 + 79 300 = 475 800`.",
            "Ahorro con el plan anual: `475 800 − 412 000 = 63 800`.",
            "Estimación de control: `12 × 40 000 = 480 000`, coherente con `475 800`.",
            "Respuestas: $475 800 al año y un ahorro de $63 800. Error típico: comparar el plan anual con un solo mes, o multiplicar por 12 solo uno de los dos servicios.",
        ],
    },
    {
        "id": "a-multiplicar-varios-digitos-3",
        "node": "a-multiplicar-varios-digitos",
        "kind": "problem",
        "level": 3,
        "title": "Recaudación de un recital en el club",
        "statement": "Un club organiza un recital. La platea tiene **24 filas de 35 butacas** y la entrada cuesta **$12 500**; además se venden **1600 entradas de campo** a **$8 500**. Se vendieron todas las entradas de campo y todas las de platea **excepto 36**. El club paga **$3 750 000** de alquiler de sonido y le paga a la banda **$1200 por cada entrada vendida** (de cualquier tipo).",
        "parts": [
            {
                "prompt": "a) ¿Cuántas butacas tiene la platea? Respondé solo con el número en butacas.",
                "check": {"type": "numeric", "value": 840, "tolerance": 0, "unit": "butacas"},
                "answer": "840 butacas",
            },
            {
                "prompt": "b) ¿Cuánto se recaudó por la venta de entradas? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 23650000, "tolerance": 0, "unit": "$"},
                "answer": "$23 650 000",
            },
            {
                "prompt": "c) ¿Cuánto le queda al club después de pagar el sonido y a la banda? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 17015200, "tolerance": 0, "unit": "$"},
                "answer": "$17 015 200",
            },
        ],
        "hints": [
            "La platea es un rectángulo de filas × butacas; las vendidas son esas menos las 36 que quedaron libres.",
            "Calculá por separado lo recaudado en platea y en campo. Para el pago a la banda necesitás el total de entradas vendidas.",
            "Atajo: `12 500 = 100 000 ÷ 8`, así que multiplicar por 12 500 es multiplicar por 100 000 y dividir por 8.",
        ],
        "solution": [
            "Platea: `24 × 35 = 20 × 35 + 4 × 35 = 700 + 140 = 840` butacas. Vendidas: `840 − 36 = 804`.",
            "Recaudación platea: `804 × 12 500 = 804 × 100 000 ÷ 8 = 80 400 000 ÷ 8 = 10 050 000`.",
            "Recaudación campo: `1600 × 8 500 = 16 × 85 × 10 000 = 1360 × 10 000 = 13 600 000`.",
            "Total recaudado: `10 050 000 + 13 600 000 = 23 650 000`.",
            "Entradas vendidas: `804 + 1600 = 2404`. Pago a la banda: `2404 × 1200 = 2404 × 12 × 100 = 28 848 × 100 = 2 884 800`.",
            "Lo que queda: `23 650 000 − 3 750 000 − 2 884 800 = 19 900 000 − 2 884 800 = 17 015 200`.",
            "Respuestas: 840 butacas, $23 650 000 recaudados y $17 015 200 para el club. Error típico: calcular el pago a la banda con las 840 butacas de platea en vez de con todas las entradas vendidas.",
        ],
    },
    # ---------- a-dividir-varios-digitos ----------
    {
        "id": "a-dividir-varios-digitos-1",
        "node": "a-dividir-varios-digitos",
        "kind": "problem",
        "level": 1,
        "title": "Cuotas de un celular",
        "statement": "Un celular cuesta **$1 152 000** y se puede pagar en **18 cuotas sin interés**. Otra tienda ofrece el mismo celular en **24 cuotas de $52 000**.",
        "parts": [
            {
                "prompt": "a) ¿De cuánto es cada cuota en el plan de 18 cuotas? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 64000, "tolerance": 0, "unit": "$"},
                "answer": "$64 000",
            },
            {
                "prompt": "b) ¿Cuánto más se paga en total con el plan de 24 cuotas que con el de 18? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 96000, "tolerance": 0, "unit": "$"},
                "answer": "$96 000",
            },
        ],
        "hints": [
            "Para dividir por 18 podés sacar cocientes parciales cómodos (por ejemplo ×50 000 o ×10 000) o dividir dos veces: primero por 2 y después por 9.",
            "Para b) calculá el total que se paga en 24 cuotas y comparalo con el precio sin interés.",
        ],
        "solution": [
            "`1 152 000 ÷ 18`: tachando los tres ceros, alcanza con `1152 ÷ 18` y agregar `000` al final.",
            "Cocientes parciales: `18 × 50 = 900`, sobran `1152 − 900 = 252`; `18 × 10 = 180`, sobran `72`; `18 × 4 = 72`, sobran `0`. Cociente: `50 + 10 + 4 = 64`.",
            "Cuota: `64 000`. Verificación: `18 × 64 000 = 1 152 000` ✓.",
            "Plan de 24 cuotas: `24 × 52 000 = 1 248 000`.",
            "Diferencia: `1 248 000 − 1 152 000 = 96 000`.",
            "Respuestas: cuotas de $64 000 y se pagan $96 000 más en 24 cuotas. Error típico: comparar solo las cuotas (`64 000` vs. `52 000`) y concluir que el plan de 24 es más barato.",
        ],
    },
    {
        "id": "a-dividir-varios-digitos-2",
        "node": "a-dividir-varios-digitos",
        "kind": "problem",
        "level": 2,
        "title": "Nafta para un viaje entre amigos",
        "statement": "Cinco amigos viajan en auto de Córdoba a Bariloche, un trayecto de **1274 km**. El auto rinde **14 km por litro** y la nafta cuesta **$1150 por litro**. Acuerdan repartir el gasto de nafta en partes iguales.",
        "parts": [
            {
                "prompt": "a) ¿Cuántos litros de nafta consumen en el viaje? Respondé solo con el número en L.",
                "check": {"type": "numeric", "value": 91, "tolerance": 0, "unit": "L"},
                "answer": "91 L",
            },
            {
                "prompt": "b) ¿Cuánto gastan en nafta en total? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 104650, "tolerance": 0, "unit": "$"},
                "answer": "$104 650",
            },
            {
                "prompt": "c) ¿Cuánto pone cada amigo? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 20930, "tolerance": 0, "unit": "$"},
                "answer": "$20 930",
            },
        ],
        "hints": [
            "Si cada litro alcanza para 14 km, ¿cuántos litros hacen falta para 1274 km?",
            "Con los litros, el costo es una multiplicación; el reparto, una división por 5.",
        ],
        "solution": [
            "Litros: `1274 ÷ 14`. Cocientes parciales: `14 × 90 = 1260`, sobran `14`; `14 × 1 = 14`, sobran `0` → `91 L`.",
            "Verificación: `14 × 91 = 1274` ✓.",
            "Costo: `91 × 1150 = 91 × 1000 + 91 × 150 = 91 000 + 13 650 = 104 650`.",
            "Por persona: `104 650 ÷ 5 = 20 930` (`100 000 ÷ 5 = 20 000` y `4650 ÷ 5 = 930`).",
            "Respuestas: 91 L, $104 650 en total y $20 930 cada uno. Error típico: multiplicar `1274 × 14` en lugar de dividir (daría litros absurdos, más de 17 000).",
        ],
    },
    {
        "id": "a-dividir-varios-digitos-3",
        "node": "a-dividir-varios-digitos",
        "kind": "problem",
        "level": 3,
        "title": "Alfajores en cajas y cajones",
        "statement": "Una fábrica de alfajores produjo **8437 alfajores** en un día. Los empaca en **cajas de 24 alfajores**, y las cajas cerradas se despachan en **cajones de 15 cajas**. Solo se cierran cajas completas y solo se despachan cajones completos.",
        "parts": [
            {
                "prompt": "a) ¿Cuántas cajas completas se arman? Respondé solo con el número en cajas.",
                "check": {"type": "numeric", "value": 351, "tolerance": 0, "unit": "cajas"},
                "answer": "351 cajas (y sobran 13 alfajores sueltos)",
            },
            {
                "prompt": "b) ¿Cuántos cajones completos se despachan? Respondé solo con el número en cajones.",
                "check": {"type": "numeric", "value": 23, "tolerance": 0, "unit": "cajones"},
                "answer": "23 cajones (y quedan 6 cajas sin despachar)",
            },
            {
                "prompt": "c) ¿Cuántos alfajores más tendrían que producir ese día para despachar un cajón completo más? Respondé solo con el número en alfajores.",
                "check": {"type": "numeric", "value": 203, "tolerance": 0, "unit": "alfajores"},
                "answer": "203 alfajores",
            },
        ],
        "hints": [
            "Hacé una división con resto para las cajas y otra para los cajones; prestá atención a qué representa cada resto.",
            "Un cajón completo tiene `15 × 24` alfajores. ¿Cuántos alfajores quedaron fuera de los cajones despachados (cajas sueltas más alfajores sueltos)?",
        ],
        "solution": [
            "Cajas: `8437 ÷ 24`. Cocientes parciales: `24 × 300 = 7200`, sobran `1237`; `24 × 50 = 1200`, sobran `37`; `24 × 1 = 24`, sobran `13`. Cociente `351`, resto `13`.",
            "Verificación: `24 × 351 + 13 = 8424 + 13 = 8437` ✓.",
            "Cajones: `351 ÷ 15`: `15 × 20 = 300`, sobran `51`; `15 × 3 = 45`, sobran `6`. Cociente `23`, resto `6` (cajas sin despachar).",
            "Un cajón tiene `15 × 24 = 360` alfajores. Los 23 cajones llevan `23 × 360 = 8280`; quedan afuera `8437 − 8280 = 157` alfajores (6 cajas de 24 = 144, más 13 sueltos).",
            "Para otro cajón completo hacen falta 360: faltan `360 − 157 = 203` alfajores.",
            "Respuestas: 351 cajas, 23 cajones y faltan 203 alfajores. Error típico en c): calcular solo las cajas que faltan (`15 − 6 = 9` cajas = 216 alfajores) y olvidarse de los 13 alfajores sueltos que ya hay.",
        ],
    },
    # ---------- a-entender-fracciones ----------
    {
        "id": "a-entender-fracciones-1",
        "node": "a-entender-fracciones",
        "kind": "problem",
        "level": 1,
        "title": "¿Qué curso aprobó en mayor proporción?",
        "statement": "En el curso de ingreso, en la comisión A rindieron el parcial **36 alumnos** y aprobaron **24**. En la comisión B rindieron **28** y aprobaron **20**.",
        "parts": [
            {
                "prompt": "a) ¿Qué fracción de los alumnos de la comisión A aprobó? Escribila como fracción irreducible (ej. 4/9).",
                "check": {"type": "text", "accept": ["2/3"]},
                "answer": "2/3",
            },
            {
                "prompt": "b) ¿Qué fracción de los alumnos de la comisión B aprobó? Escribila como fracción irreducible (ej. 4/9).",
                "check": {"type": "text", "accept": ["5/7"]},
                "answer": "5/7",
            },
            {
                "prompt": "c) ¿Qué comisión aprobó en mayor proporción?",
                "check": {
                    "type": "choice",
                    "options": [
                        "La comisión B, porque 5/7 = 15/21 es mayor que 2/3 = 14/21",
                        "La comisión A, porque aprobaron más alumnos (24 contra 20)",
                        "Las dos por igual, porque en ambas desaprobaron 12 y 8, que son pocos",
                        "La comisión A, porque 2/3 tiene el denominador más chico",
                    ],
                    "correct": 0,
                },
                "answer": "La comisión B (5/7 > 2/3)",
            },
        ],
        "hints": [
            "La fracción es aprobados sobre los que rindieron; después simplificá dividiendo arriba y abajo por el mayor divisor común.",
            "Para comparar fracciones con distinto denominador, convertilas en equivalentes con el mismo denominador.",
        ],
        "solution": [
            "Comisión A: `24/36`. El mayor divisor común de 24 y 36 es 12: `24 ÷ 12 = 2`, `36 ÷ 12 = 3` → `2/3`.",
            "Comisión B: `20/28`. El mayor divisor común es 4: `20 ÷ 4 = 5`, `28 ÷ 4 = 7` → `5/7`.",
            "Para comparar, usamos denominador 21: `2/3 = 14/21` (×7 arriba y abajo) y `5/7 = 15/21` (×3 arriba y abajo).",
            "Como `15/21 > 14/21`, la comisión B aprobó en mayor proporción, aunque en número absoluto aprobaron menos alumnos.",
            "Respuestas: 2/3, 5/7 y la comisión B. Error típico: comparar cantidades (24 > 20) sin tener en cuenta cuántos rindieron en cada comisión.",
        ],
    },
    {
        "id": "a-entender-fracciones-2",
        "node": "a-entender-fracciones",
        "kind": "problem",
        "level": 2,
        "title": "Medir con una sola taza",
        "statement": "Una receta de budín lleva **2 y 1/3 tazas de harina** y **1 y 3/4 tazas de leche**. En tu casa solo encontrás una medidora de **1/3 de taza** y otra de **1/4 de taza**. Querés hacer **dos budines**, o sea, duplicar la receta.",
        "parts": [
            {
                "prompt": "a) Para UN budín, ¿cuántas veces tenés que llenar la medidora de 1/3 de taza con harina? Respondé solo con el número en medidas.",
                "check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": "medidas"},
                "answer": "7 medidas",
            },
            {
                "prompt": "b) Para los DOS budines, ¿cuántas tazas de harina necesitás? Escribila como fracción irreducible (ej. 9/4).",
                "check": {"type": "text", "accept": ["14/3"]},
                "answer": "14/3 (4 y 2/3 tazas)",
            },
            {
                "prompt": "c) Para los DOS budines, ¿cuántas veces llenás la medidora de 1/4 de taza con leche? Respondé solo con el número en medidas.",
                "check": {"type": "numeric", "value": 14, "tolerance": 0, "unit": "medidas"},
                "answer": "14 medidas",
            },
        ],
        "hints": [
            "Pasá cada número mixto a fracción impropia: los enteros también se pueden contar en tercios o en cuartos.",
            "El numerador de la fracción impropia te dice cuántas medidas de ese tamaño hacen falta.",
        ],
        "solution": [
            "Harina para un budín: `2 y 1/3 = 2 × 3/3 + 1/3 = 6/3 + 1/3 = 7/3` de taza → 7 medidas de 1/3.",
            "Para dos budines: `7/3 + 7/3 = 14/3` de taza (14 medidas). Como número mixto: `14 ÷ 3 = 4` con resto 2 → `4 y 2/3` tazas. 14 y 3 no tienen divisores comunes, así que `14/3` es irreducible.",
            "Leche para un budín: `1 y 3/4 = 4/4 + 3/4 = 7/4` de taza → 7 medidas de 1/4.",
            "Para dos budines: `7/4 + 7/4 = 14/4` de taza → 14 medidas de 1/4 (equivale a `7/2 = 3 y 1/2` tazas).",
            "Respuestas: 7 medidas, 14/3 de taza y 14 medidas. Error típico: pasar `2 y 1/3` a `3/3` o a `2/3` (hay que multiplicar el entero por el denominador y sumar el numerador: `2 × 3 + 1 = 7`).",
        ],
    },
    {
        "id": "a-entender-fracciones-3",
        "node": "a-entender-fracciones",
        "kind": "problem",
        "level": 3,
        "title": "El indicador de nafta en octavos",
        "statement": "El tanque de un auto tiene capacidad para **48 L** y su indicador de nafta está dividido en **8 partes iguales**. Al salir de viaje la aguja marca **6/8** del tanque. Durante el viaje el auto consume **26 L** y, en una estación de servicio, se cargan **20 L**.",
        "parts": [
            {
                "prompt": "a) ¿Cuántos litros había al salir? Respondé solo con el número en L.",
                "check": {"type": "numeric", "value": 36, "tolerance": 0, "unit": "L"},
                "answer": "36 L",
            },
            {
                "prompt": "b) ¿Cuántos litros quedan al terminar el viaje? Respondé solo con el número en L.",
                "check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": "L"},
                "answer": "30 L",
            },
            {
                "prompt": "c) ¿Qué fracción del tanque está llena al terminar el viaje? Escribila como fracción irreducible (ej. 3/7).",
                "check": {"type": "text", "accept": ["5/8"]},
                "answer": "5/8",
            },
        ],
        "hints": [
            "Cada octavo del indicador corresponde a `48 ÷ 8` litros.",
            "La fracción del tanque es litros que hay sobre capacidad total; después simplificá.",
        ],
        "solution": [
            "Cada octavo del tanque son `48 ÷ 8 = 6 L`. Al salir hay `6/8`, o sea 6 octavos: `6 × 6 = 36 L` (también `6/8 = 3/4` del tanque).",
            "Al final: `36 − 26 + 20 = 30 L`.",
            "Fracción del tanque: `30/48`. El mayor divisor común de 30 y 48 es 6: `30 ÷ 6 = 5`, `48 ÷ 6 = 8` → `5/8`.",
            "Control con el indicador: `30 L ÷ 6 L` por octavo = 5 octavos, o sea la aguja marca `5/8` ✓.",
            "Respuestas: 36 L, 30 L y 5/8 del tanque. Error típico: restar fracciones y litros mezclados (por ejemplo `6/8 − 26`) sin pasar todo a la misma unidad.",
        ],
    },
    # ---------- a-sumar-restar-fracciones-igual ----------
    {
        "id": "a-sumar-restar-fracciones-igual-1",
        "node": "a-sumar-restar-fracciones-igual",
        "kind": "problem",
        "level": 1,
        "title": "El sueldo dividido en décimos",
        "statement": "Sofía organiza su sueldo en décimos: destina **3/10** al alquiler, **2/10** a la comida, **1/10** al transporte y **1/10** a salidas. Todo lo que no gasta lo ahorra. Su sueldo es de **$650 000**.",
        "parts": [
            {
                "prompt": "a) ¿Qué fracción del sueldo gasta en total? Escribila como fracción irreducible (ej. 4/5).",
                "check": {"type": "text", "accept": ["7/10"]},
                "answer": "7/10",
            },
            {
                "prompt": "b) ¿Qué fracción del sueldo ahorra? Escribila como fracción irreducible (ej. 4/5).",
                "check": {"type": "text", "accept": ["3/10"]},
                "answer": "3/10",
            },
            {
                "prompt": "c) ¿Cuántos pesos ahorra por mes? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 195000, "tolerance": 0, "unit": "$"},
                "answer": "$195 000",
            },
        ],
        "hints": [
            "Las fracciones tienen el mismo denominador: sumás los numeradores y el denominador queda igual.",
            "El sueldo entero es `10/10`. Para pasar la fracción a pesos, calculá cuánto es un décimo del sueldo.",
        ],
        "solution": [
            "Gastos: `3/10 + 2/10 + 1/10 + 1/10 = (3 + 2 + 1 + 1)/10 = 7/10` (7 y 10 no tienen divisores comunes: es irreducible).",
            "Ahorro: el sueldo completo es `10/10`, así que `10/10 − 7/10 = 3/10`.",
            "Un décimo del sueldo: `650 000 ÷ 10 = 65 000`. Ahorro: `3 × 65 000 = 195 000`.",
            "Verificación: gastos `7 × 65 000 = 455 000` y `455 000 + 195 000 = 650 000` ✓.",
            "Respuestas: 7/10, 3/10 y $195 000. Error típico: sumar también los denominadores (`7/40`).",
        ],
    },
    {
        "id": "a-sumar-restar-fracciones-igual-2",
        "node": "a-sumar-restar-fracciones-igual",
        "kind": "problem",
        "level": 2,
        "title": "Cortes en un caño de 6 metros",
        "statement": "Un plomero tiene un caño de **6 m**. Corta un tramo de **1 y 5/8 m** y otro de **2 y 7/8 m**. Para terminar la instalación necesitaría un tercer tramo de **1 y 5/8 m**. (Despreciá el material que se pierde en cada corte.)",
        "parts": [
            {
                "prompt": "a) ¿Cuántos metros de caño cortó en total? Respondé solo con el número en m (podés usar decimal o fracción).",
                "check": {"type": "numeric", "value": 4.5, "tolerance": 0, "unit": "m"},
                "answer": "4.5 m (4 y 1/2 m)",
            },
            {
                "prompt": "b) ¿Cuántos metros de caño le sobran? Respondé solo con el número en m (podés usar decimal o fracción).",
                "check": {"type": "numeric", "value": 1.5, "tolerance": 0, "unit": "m"},
                "answer": "1.5 m (1 y 1/2 m)",
            },
            {
                "prompt": "c) ¿Cuánto le falta al sobrante para alcanzar el tercer tramo? Escribilo como fracción irreducible de metro (ej. 3/4).",
                "check": {"type": "text", "accept": ["1/8"]},
                "answer": "1/8 m",
            },
        ],
        "hints": [
            "Sumá enteros con enteros y octavos con octavos; si los octavos pasan de 8/8, se forma un entero más.",
            "Para restar de 6, pensá uno de los metros como 8/8.",
        ],
        "solution": [
            "Enteros: `1 + 2 = 3`. Octavos: `5/8 + 7/8 = 12/8 = 1 y 4/8 = 1 y 1/2`. Total cortado: `3 + 1 y 1/2 = 4 y 1/2 m = 4.5 m`.",
            "Sobrante: `6 − 4 y 1/2`. Escribimos `6 = 5 y 8/8` y `4 y 1/2 = 4 y 4/8`: `5 y 8/8 − 4 y 4/8 = 1 y 4/8 = 1 y 1/2 m = 1.5 m`.",
            "Comparación con el tercer tramo: `1 y 4/8` contra `1 y 5/8`. El sobrante es más corto: no alcanza.",
            "Lo que falta: `1 y 5/8 − 1 y 4/8 = 1/8 m` (12,5 cm).",
            "Respuestas: 4.5 m, 1.5 m y falta 1/8 m. Error típico: en a) escribir `3 y 12/8` y dejarlo así, sin convertir los 12/8 en `1 y 4/8`.",
        ],
    },
    {
        "id": "a-sumar-restar-fracciones-igual-3",
        "node": "a-sumar-restar-fracciones-igual",
        "kind": "problem",
        "level": 3,
        "title": "El tanque de agua del edificio",
        "statement": "El tanque de agua de un edificio tiene capacidad para **1200 L**. Un día amanece lleno hasta los **11/12** de su capacidad. Durante la mañana los vecinos consumen **7/12** del tanque; al mediodía la bomba sube agua equivalente a **5/12** del tanque, y a la noche se consumen otros **2/12** del tanque.",
        "parts": [
            {
                "prompt": "a) ¿Qué fracción del tanque queda llena al terminar la mañana (antes de que funcione la bomba)? Escribila como fracción irreducible (ej. 2/5).",
                "check": {"type": "text", "accept": ["1/3"]},
                "answer": "1/3",
            },
            {
                "prompt": "b) ¿Qué fracción del tanque queda llena al final del día? Escribila como fracción irreducible (ej. 2/5).",
                "check": {"type": "text", "accept": ["7/12"]},
                "answer": "7/12",
            },
            {
                "prompt": "c) ¿Cuántos litros habría que bombear al final del día para llenar el tanque? Respondé solo con el número en L.",
                "check": {"type": "numeric", "value": 500, "tolerance": 0, "unit": "L"},
                "answer": "500 L",
            },
        ],
        "hints": [
            "Todas las fracciones están en doceavos: seguí el nivel del tanque sumando lo que entra y restando lo que sale.",
            "Lo que falta para llenar es la diferencia con `12/12`. Para pasarlo a litros, calculá cuántos litros es un doceavo.",
        ],
        "solution": [
            "Después de la mañana: `11/12 − 7/12 = 4/12`; simplificando por 4 → `1/3`.",
            "Después de la bomba: `4/12 + 5/12 = 9/12` (= 3/4).",
            "Al final del día: `9/12 − 2/12 = 7/12`, que ya es irreducible.",
            "Falta para llenarlo: `12/12 − 7/12 = 5/12`. Un doceavo son `1200 ÷ 12 = 100 L`, así que faltan `5 × 100 = 500 L`.",
            "Verificación en litros: amanece con `1100 L`; `1100 − 700 = 400`; `400 + 500 = 900`; `900 − 200 = 700 L` (= 7/12); `1200 − 700 = 500 L` ✓.",
            "Respuestas: 1/3, 7/12 y 500 L. Error típico en a): dejar `4/12` sin simplificar o simplificar mal (`2/3`).",
        ],
    },
    # ---------- a-sumar-restar-fracciones-distinto ----------
    {
        "id": "a-sumar-restar-fracciones-distinto-1",
        "node": "a-sumar-restar-fracciones-distinto",
        "kind": "problem",
        "level": 1,
        "title": "Azúcar para la torta",
        "statement": "Para una torta usás **3/4 de taza** de azúcar en la masa y **2/3 de taza** en el almíbar. En el frasco había **2 tazas** de azúcar.",
        "parts": [
            {
                "prompt": "a) ¿Cuántas tazas de azúcar usaste en total? Escribila como fracción irreducible (ej. 5/8).",
                "check": {"type": "text", "accept": ["17/12"]},
                "answer": "17/12 (1 y 5/12 tazas)",
            },
            {
                "prompt": "b) ¿Cuántas tazas de azúcar quedaron en el frasco? Escribila como fracción irreducible (ej. 5/8).",
                "check": {"type": "text", "accept": ["7/12"]},
                "answer": "7/12",
            },
        ],
        "hints": [
            "Cuartos y tercios no se pueden sumar directamente: buscá un denominador común (el mcm de 4 y 3).",
            "Las 2 tazas también se pueden escribir en esa unidad.",
        ],
        "solution": [
            "Denominador común: `mcm(4, 3) = 12`. `3/4 = 9/12` (×3) y `2/3 = 8/12` (×4).",
            "Usado: `9/12 + 8/12 = 17/12` de taza (`1 y 5/12`). 17 es primo y no divide a 12: es irreducible.",
            "En el frasco había `2 = 24/12`.",
            "Queda: `24/12 − 17/12 = 7/12` de taza.",
            "Respuestas: 17/12 tazas usadas y 7/12 de taza en el frasco. Error típico: sumar numeradores y denominadores (`3/4 + 2/3 = 5/7`).",
        ],
    },
    {
        "id": "a-sumar-restar-fracciones-distinto-2",
        "node": "a-sumar-restar-fracciones-distinto",
        "kind": "problem",
        "level": 2,
        "title": "Un regalo entre tres hermanos",
        "statement": "Tres hermanos compran un regalo de **$96 000** para su mamá. Ana pone **1/3** del precio, Beto pone **1/4** del precio y Caro pone el resto.",
        "parts": [
            {
                "prompt": "a) ¿Qué fracción del precio pone Caro? Escribila como fracción irreducible (ej. 3/8).",
                "check": {"type": "text", "accept": ["5/12"]},
                "answer": "5/12",
            },
            {
                "prompt": "b) ¿Cuánto dinero pone Caro? Respondé solo con el número en pesos, sin puntos de miles.",
                "check": {"type": "numeric", "value": 40000, "tolerance": 0, "unit": "$"},
                "answer": "$40 000",
            },
        ],
        "hints": [
            "Sumá primero lo que ponen Ana y Beto, con un denominador común, y restalo del entero.",
            "Para pasar a pesos, calculá cuánto es 1/12 del precio.",
        ],
        "solution": [
            "Ana y Beto juntos: `1/3 + 1/4`. Con denominador 12: `4/12 + 3/12 = 7/12`.",
            "Caro: `12/12 − 7/12 = 5/12`.",
            "Un doceavo del precio: `96 000 ÷ 12 = 8000`. Caro pone `5 × 8000 = 40 000`.",
            "Verificación: Ana `96 000 ÷ 3 = 32 000`, Beto `96 000 ÷ 4 = 24 000`; `32 000 + 24 000 + 40 000 = 96 000` ✓.",
            "Respuestas: 5/12 del precio, $40 000. Error típico: calcular `1 − 1/3 − 1/4` como `1 − 2/7`.",
        ],
    },
    {
        "id": "a-sumar-restar-fracciones-distinto-3",
        "node": "a-sumar-restar-fracciones-distinto",
        "kind": "problem",
        "level": 3,
        "title": "Una travesía en bicicleta en tres días",
        "statement": "Una ciclista hace una travesía en tres días. El primer día recorre **2/5** del trayecto total, el segundo día **1/3** del trayecto total, y el tercer día completa los **24 km** que le faltaban.",
        "parts": [
            {
                "prompt": "a) ¿Qué fracción del trayecto recorre el tercer día? Escribila como fracción irreducible (ej. 2/9).",
                "check": {"type": "text", "accept": ["4/15"]},
                "answer": "4/15",
            },
            {
                "prompt": "b) ¿Cuál es la longitud total del trayecto? Respondé solo con el número en km.",
                "check": {"type": "numeric", "value": 90, "tolerance": 0, "unit": "km"},
                "answer": "90 km",
            },
            {
                "prompt": "c) ¿Cuántos kilómetros más recorrió el primer día que el segundo? Respondé solo con el número en km.",
                "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": "km"},
                "answer": "6 km",
            },
        ],
        "hints": [
            "Sumá las fracciones de los dos primeros días con denominador común y restá del entero.",
            "Si esa fracción equivale a 24 km, ¿cuántos km son 1/15 del trayecto?",
            "Para c) podés restar las fracciones de los dos días y pasar el resultado a km.",
        ],
        "solution": [
            "Dos primeros días: `2/5 + 1/3`. Denominador común 15: `6/15 + 5/15 = 11/15`.",
            "Tercer día: `15/15 − 11/15 = 4/15` del trayecto.",
            "Si `4/15` del trayecto son 24 km, entonces `1/15` son `24 ÷ 4 = 6 km` y el total es `15 × 6 = 90 km`.",
            "Primer día: `6 × 6 = 36 km`; segundo día: `5 × 6 = 30 km`. Diferencia: `36 − 30 = 6 km` (o bien `2/5 − 1/3 = 6/15 − 5/15 = 1/15` del trayecto, que son 6 km).",
            "Verificación: `36 + 30 + 24 = 90 km` ✓.",
            "Respuestas: 4/15, 90 km y 6 km. Error típico: pensar que los 24 km son lo que falta después de cada día por separado, o calcular `2/5 + 1/3 = 3/8`.",
        ],
    },
]
