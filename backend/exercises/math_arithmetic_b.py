"""Ejercicios de Matemática: Aritmética (fracciones, decimales, potencias, negativos) y Preálgebra
(factores y múltiplos, datos, medición, expresiones).

Tres problemas de planteo por tema (niveles 1, 2 y 3). Situaciones cotidianas que obligan a decidir
qué operaciones hacer y encadenarlas; el nivel 3 combina varias ideas. Decimales con punto, como en
las lecciones; π ≈ 3.14 cuando aparece.
"""

EXERCISES: list[dict] = [
    # ============================ ARITMÉTICA ============================
    # ---------- a-multiplicar-fracciones ----------
    {
        "id": "a-multiplicar-fracciones-1",
        "node": "a-multiplicar-fracciones",
        "kind": "problem",
        "level": 1,
        "title": "Pan casero para menos gente",
        "statement": "Una receta de pan casero rinde **8 porciones** y lleva **3/4 kg** de harina y **1 1/2 tazas** de leche. Querés hacer solo **6 porciones**, manteniendo las proporciones de la receta.",
        "parts": [
            {
                "prompt": "a) ¿Cuántos kg de harina usás? Escribila como fracción irreducible (ej. 2/7).",
                "check": {"type": "text", "accept": ["9/16"]},
                "answer": "9/16 kg",
            },
            {
                "prompt": "b) Tu balanza marca en gramos (1 kg = 1000 g). ¿Cuántos gramos de harina pesás? Respondé solo con el número en g.",
                "check": {"type": "numeric", "value": 562.5, "tolerance": 0, "unit": "g"},
                "answer": "562.5 g",
            },
            {
                "prompt": "c) ¿Cuántas tazas de leche usás? Escribila como fracción irreducible (ej. 2/7).",
                "check": {"type": "text", "accept": ["9/8"]},
                "answer": "9/8 de taza (1 1/8 tazas)",
            },
        ],
        "hints": [
            "6 porciones de las 8 que rinde la receta es una fracción de la receta: escribila y simplificala.",
            "Cada ingrediente se multiplica por esa fracción. Pasá `1 1/2` a fracción impropia antes de multiplicar.",
        ],
        "solution": [
            "Fracción de la receta que hacés: `6/8 = 3/4`.",
            "Harina: `3/4 × 3/4 = (3 × 3)/(4 × 4) = 9/16 kg`.",
            "En gramos: `9/16 × 1000 = 9000/16 = 562.5 g` (o bien `1000 ÷ 16 = 62.5` y `62.5 × 9 = 562.5`).",
            "Leche: `1 1/2 = 3/2`, entonces `3/4 × 3/2 = 9/8 = 1 1/8` tazas.",
            "Control: multiplicar por `3/4` (menor que 1) tiene que achicar cada cantidad: `9/16 < 3/4` y `9/8 < 3/2`. Respuestas: `9/16 kg`, `562.5 g` y `9/8` de taza. Error típico: restar 2 porciones a cada ingrediente en vez de multiplicar por `3/4`.",
        ],
    },
    {
        "id": "a-multiplicar-fracciones-2",
        "node": "a-multiplicar-fracciones",
        "kind": "problem",
        "level": 2,
        "title": "Fracciones del sueldo",
        "statement": "Lucía cobra **$480 000** por mes. Destina **3/8** del sueldo al alquiler; de lo que le queda, **2/5** va al supermercado; y de lo que le queda después de eso, ahorra **1/3**. El resto queda libre para otros gastos.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto gasta en el supermercado? Respondé solo con el número en pesos (sin puntos de miles).",
                "check": {"type": "numeric", "value": 120000, "tolerance": 0, "unit": "$"},
                "answer": "120000 ($120 000)",
            },
            {
                "prompt": "b) ¿Cuánto ahorra por mes? Respondé solo con el número en pesos (sin puntos de miles).",
                "check": {"type": "numeric", "value": 60000, "tolerance": 0, "unit": "$"},
                "answer": "60000 ($60 000)",
            },
            {
                "prompt": "c) ¿Qué fracción del sueldo total queda libre para otros gastos? Escribila como fracción irreducible (ej. 2/7).",
                "check": {"type": "text", "accept": ["1/4"]},
                "answer": "1/4 del sueldo",
            },
        ],
        "hints": [
            "Cada fracción se aplica sobre lo que QUEDA en ese momento, no sobre el sueldo completo.",
            "Si gasta `3/8`, le quedan `5/8`. El supermercado es `2/5` de esos `5/8`: `2/5 × 5/8` del sueldo.",
            "Para el inciso c) podés trabajar solo con fracciones: lo que queda en cada paso es `1 −` la fracción que se usa.",
        ],
        "solution": [
            "Alquiler: `3/8 × 480 000 = 180 000`. Le quedan `480 000 − 180 000 = 300 000` (son los `5/8` del sueldo).",
            "Supermercado: `2/5 × 300 000 = 120 000`. Le quedan `300 000 − 120 000 = 180 000`.",
            "Ahorro: `1/3 × 180 000 = 60 000`. Queda libre `180 000 − 60 000 = 120 000`.",
            "Como fracción del sueldo: después del alquiler queda `5/8`; después del súper, `3/5 × 5/8 = 3/8`; después de ahorrar, `2/3 × 3/8 = 6/24 = 1/4`.",
            "Control: `1/4 × 480 000 = 120 000`, igual que en pesos. Respuestas: $120 000, $60 000 y `1/4`. Error típico: calcular el súper como `2/5` del sueldo entero (`192 000`).",
        ],
    },
    {
        "id": "a-multiplicar-fracciones-3",
        "node": "a-multiplicar-fracciones",
        "kind": "problem",
        "level": 3,
        "title": "¿Cómo llegan a la escuela?",
        "statement": "En una escuela técnica, **3/5** de los alumnos viaja en colectivo y, de ellos, **5/6** tiene boleto estudiantil. De los alumnos que NO viajan en colectivo, **5/8** va caminando y el resto va en bicicleta. Se sabe que **48 alumnos** viajan en colectivo sin boleto estudiantil.",
        "parts": [
            {
                "prompt": "a) ¿Cuántos alumnos tiene la escuela? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 480, "tolerance": 0, "unit": "alumnos"},
                "answer": "480 alumnos",
            },
            {
                "prompt": "b) ¿Cuántos alumnos viajan con boleto estudiantil? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 240, "tolerance": 0, "unit": "alumnos"},
                "answer": "240 alumnos",
            },
            {
                "prompt": "c) ¿Qué fracción del total de alumnos va en bicicleta? Escribila como fracción irreducible (ej. 2/7).",
                "check": {"type": "text", "accept": ["3/20"]},
                "answer": "3/20 del total",
            },
        ],
        "hints": [
            "Los que van en colectivo sin boleto son una fracción de una fracción: `1/6` de los `3/5` del total.",
            "Si sabés qué fracción del total son esos 48 alumnos, el total sale de ahí.",
            "Para la bici: primero la fracción que NO va en colectivo, después la parte de ella que no camina.",
        ],
        "solution": [
            "Sin boleto: `1 − 5/6 = 1/6` de los que van en colectivo. Del total: `1/6 × 3/5 = 3/30 = 1/10`.",
            "Esos 48 alumnos son `1/10` del total, así que el total es `48 × 10 = 480` alumnos.",
            "Con boleto: `5/6 × 3/5 = 15/30 = 1/2` del total → `1/2 × 480 = 240` alumnos (control: en colectivo van `3/5 × 480 = 288`, y `288 − 48 = 240`).",
            "No van en colectivo: `1 − 3/5 = 2/5`. En bici va el resto de los que no caminan: `1 − 5/8 = 3/8` de ellos.",
            "Fracción del total en bici: `3/8 × 2/5 = 6/40 = 3/20` (son `3/20 × 480 = 72` alumnos).",
            "Respuestas: 480 alumnos, 240 con boleto y `3/20` en bici. Error típico: tomar los 48 como `1/6` del total y obtener 288 (eso son solo los que viajan en colectivo).",
        ],
    },
    # ---------- a-dividir-fracciones ----------
    {
        "id": "a-dividir-fracciones-1",
        "node": "a-dividir-fracciones",
        "kind": "problem",
        "level": 1,
        "title": "Fraccionar un bidón de agua",
        "statement": "Tenés un bidón con **7 1/2 L** de agua. Primero pensás servirla en botellas de **3/4 L**; después evaluás usar, en cambio, vasos de **2/5 L**.",
        "parts": [
            {
                "prompt": "a) ¿Cuántas botellas de 3/4 L llenás con el bidón? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "botellas"},
                "answer": "10 botellas",
            },
            {
                "prompt": "b) Si usás vasos de 2/5 L, ¿cuántos vasos llenás COMPLETOS? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 18, "tolerance": 0, "unit": "vasos"},
                "answer": "18 vasos",
            },
            {
                "prompt": "c) ¿Cuántos litros de agua sobran después de llenar esos vasos? Escribila como fracción irreducible (ej. 2/7).",
                "check": {"type": "text", "accept": ["3/10"]},
                "answer": "3/10 L",
            },
        ],
        "hints": [
            "¿Cuántas veces cabe `3/4` en `7 1/2`? Pasá el número mixto a fracción impropia y dividí (multiplicá por el recíproco).",
            "Con los vasos la división no da exacta: la parte entera son los vasos llenos y la parte fraccionaria es un vaso incompleto. Esa parte está medida en VASOS, no en litros.",
        ],
        "solution": [
            "`7 1/2 = 15/2`. Botellas: `15/2 ÷ 3/4 = 15/2 × 4/3 = 60/6 = 10` botellas.",
            "Vasos: `15/2 ÷ 2/5 = 15/2 × 5/2 = 75/4 = 18 3/4`. Se llenan **18** vasos completos.",
            "El `3/4` que sobra es tres cuartos de un vaso: `3/4 × 2/5 = 6/20 = 3/10 L`.",
            "Control: `18 × 2/5 = 36/5 = 7.2 L` en vasos, y `7.5 − 7.2 = 0.3 L = 3/10 L`. Respuestas: 10 botellas, 18 vasos y sobran `3/10 L`. Error típico: decir que sobran `3/4 L` (confundir \"3/4 de vaso\" con litros).",
        ],
    },
    {
        "id": "a-dividir-fracciones-2",
        "node": "a-dividir-fracciones",
        "kind": "problem",
        "level": 2,
        "title": "La canilla que gotea",
        "statement": "Una canilla que gotea llenó **9/10 L** de un recipiente en **3/4 de hora**. Suponé que gotea siempre al mismo ritmo.",
        "parts": [
            {
                "prompt": "a) ¿Cuántos litros pierde por hora? Respondé solo con el número en L/h.",
                "check": {"type": "numeric", "value": 1.2, "tolerance": 0, "unit": "L/h"},
                "answer": "1.2 L/h (6/5 L por hora)",
            },
            {
                "prompt": "b) ¿Cuántas horas tarda en llenar un balde de 6 L? Respondé solo con el número en h.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "h"},
                "answer": "5 h",
            },
            {
                "prompt": "c) ¿Cuántos minutos tarda en juntar 1/2 L? Respondé solo con el número en min.",
                "check": {"type": "numeric", "value": 25, "tolerance": 0, "unit": "min"},
                "answer": "25 min",
            },
        ],
        "hints": [
            "\"Litros por hora\" es litros ÷ horas, aunque las dos cantidades sean fracciones.",
            "Para el tiempo, preguntate cuántas veces cabe el ritmo por hora en la cantidad pedida: litros ÷ (litros por hora).",
            "En c) te va a dar una fracción de hora: multiplicala por 60.",
        ],
        "solution": [
            "Ritmo: `9/10 ÷ 3/4 = 9/10 × 4/3 = 36/30 = 6/5 L/h = 1.2 L/h`.",
            "Balde de 6 L: `6 ÷ 6/5 = 6 × 5/6 = 5 h`.",
            "Medio litro: `1/2 ÷ 6/5 = 1/2 × 5/6 = 5/12 h`.",
            "En minutos: `5/12 × 60 = 300/12 = 25 min`.",
            "Control: en 25 min (`5/12 h`) pierde `6/5 × 5/12 = 30/60 = 1/2 L`. Respuestas: 1.2 L/h, 5 h y 25 min. Error típico: multiplicar `9/10 × 3/4 = 27/40` en vez de dividir.",
        ],
    },
    {
        "id": "a-dividir-fracciones-3",
        "node": "a-dividir-fracciones",
        "kind": "problem",
        "level": 3,
        "title": "El tanque de la casa",
        "statement": "El tanque de agua de una casa está lleno hasta **5/8** de su capacidad. Se sacan **90 L** y el nivel baja a **1/4** de la capacidad. Con el agua que quedó se podrían llenar bidones de **2 1/2 L**. A partir de ese nivel de `1/4` (sin sacar más agua), se enciende una bomba que carga **3/20** de la capacidad del tanque cada **media hora**.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la capacidad del tanque? Respondé solo con el número en L.",
                "check": {"type": "numeric", "value": 240, "tolerance": 0, "unit": "L"},
                "answer": "240 L",
            },
            {
                "prompt": "b) ¿Cuántos bidones de 2 1/2 L se llenarían con el agua que quedó en el tanque? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 24, "tolerance": 0, "unit": "bidones"},
                "answer": "24 bidones",
            },
            {
                "prompt": "c) ¿Cuántas horas tarda la bomba en llenar el tanque? Respondé solo con el número en h.",
                "check": {"type": "numeric", "value": 2.5, "tolerance": 0, "unit": "h"},
                "answer": "2.5 h (2 h 30 min)",
            },
        ],
        "hints": [
            "Los 90 L corresponden a la diferencia entre los dos niveles: `5/8 − 1/4` de la capacidad.",
            "Si una fracción conocida de la capacidad son 90 L, la capacidad es 90 dividido esa fracción.",
            "Pasá el ritmo de la bomba a \"fracción de tanque por hora\" y fijate cuánto le falta al tanque para estar lleno.",
        ],
        "solution": [
            "Fracción que se sacó: `5/8 − 1/4 = 5/8 − 2/8 = 3/8` de la capacidad, y eso son 90 L.",
            "Capacidad: `90 ÷ 3/8 = 90 × 8/3 = 240 L`.",
            "Quedaron `1/4 × 240 = 60 L`. Bidones: `60 ÷ 2 1/2 = 60 ÷ 5/2 = 60 × 2/5 = 24` bidones.",
            "Ritmo de la bomba: `3/20 ÷ 1/2 = 3/20 × 2 = 3/10` de la capacidad por hora. Falta llenar `1 − 1/4 = 3/4` del tanque.",
            "Tiempo: `3/4 ÷ 3/10 = 3/4 × 10/3 = 10/4 = 5/2 = 2.5 h`.",
            "Control: en 2.5 h hay 5 medias horas, y `5 × 3/20 = 15/20 = 3/4` ✓. Respuestas: 240 L, 24 bidones y 2.5 h. Error típico: hacer `90 × 3/8` en vez de `90 ÷ 3/8`.",
        ],
    },
    # ---------- a-decimales-valor-posicional ----------
    {
        "id": "a-decimales-valor-posicional-1",
        "node": "a-decimales-valor-posicional",
        "kind": "problem",
        "level": 1,
        "title": "Torneo de salto en largo",
        "statement": "En un torneo intercolegial de salto en largo, las mejores marcas fueron: Ana **4.07 m**, Belén **4.7 m**, Carla **4.075 m** y Dana **4.69 m**.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el orden de las cuatro, de la marca MAYOR a la menor?",
                "check": {"type": "choice", "options": [
                    "Belén, Dana, Carla, Ana",
                    "Carla, Dana, Ana, Belén",
                    "Belén, Dana, Ana, Carla",
                    "Carla, Ana, Dana, Belén",
                ], "correct": 0},
                "answer": "Belén (4.7), Dana (4.69), Carla (4.075), Ana (4.07)",
            },
            {
                "prompt": "b) La planilla oficial registra las marcas redondeadas a décimas (1 decimal). ¿Qué marca le anotan a Dana? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 4.7, "tolerance": 0, "unit": "m"},
                "answer": "4.7 m",
            },
            {
                "prompt": "c) ¿Qué fracción de metro es la parte decimal de la marca de Carla (0.075 m)? Escribila como fracción irreducible (ej. 2/7).",
                "check": {"type": "text", "accept": ["3/40"]},
                "answer": "3/40 m",
            },
        ],
        "hints": [
            "Completá con ceros a la derecha para que todas tengan 3 decimales y compará cifra por cifra, de izquierda a derecha.",
            "Para redondear a décimas mirá la cifra de los centésimos: si es 5 o más, la de las décimas sube.",
            "`0.075` son 75 milésimos: escribilo sobre 1000 y simplificá.",
        ],
        "solution": [
            "Con 3 decimales: Ana `4.070`, Belén `4.700`, Carla `4.075`, Dana `4.690`.",
            "Todas tienen 4 unidades. Décimos: Belén 7, Dana 6, Carla 0, Ana 0. Entre Carla y Ana (empate en décimos y centésimos) deciden los milésimos: `5 > 0`, gana Carla. Orden: Belén, Dana, Carla, Ana.",
            "Dana: `4.69` → la cifra de los centésimos es 9 (≥ 5), así que la décima sube de 6 a 7: `4.7 m`. En la planilla queda empatada con Belén, aunque Belén saltó 1 cm más.",
            "Carla: `0.075 = 75/1000`. Dividiendo por 25: `3/40`.",
            "Respuestas: Belén, Dana, Carla, Ana; `4.7 m`; `3/40 m`. Error típico: creer que `4.075` es mayor que `4.7` porque \"tiene más cifras\".",
        ],
    },
    {
        "id": "a-decimales-valor-posicional-2",
        "node": "a-decimales-valor-posicional",
        "kind": "problem",
        "level": 2,
        "title": "Tornillos en pulgadas",
        "statement": "En la ferretería las medidas de tornillos vienen en pulgadas con fracciones. Necesitás un tornillo que entre en un agujero de **0.25 pulgadas** (tiene que ser MÁS FINO que el agujero), y en la caja hay tornillos de **3/16**, **7/32**, **9/32** y **5/16** pulgadas.",
        "parts": [
            {
                "prompt": "a) Escribí 7/32 en forma decimal (exacta). Respondé solo con el número en pulgadas.",
                "check": {"type": "numeric", "value": 0.21875, "tolerance": 0, "unit": "in"},
                "answer": "0.21875 pulgadas",
            },
            {
                "prompt": "b) ¿Cuál es el tornillo MÁS GRUESO que todavía es más fino que el agujero?",
                "check": {"type": "choice", "options": ["3/16", "7/32", "9/32", "5/16"], "correct": 1},
                "answer": "7/32 de pulgada (0.21875)",
            },
            {
                "prompt": "c) El catálogo informa las medidas redondeadas a centésimos. ¿Qué valor figura para el tornillo de 9/32? Respondé solo con el número en pulgadas.",
                "check": {"type": "numeric", "value": 0.28, "tolerance": 0, "unit": "in"},
                "answer": "0.28 pulgadas",
            },
        ],
        "hints": [
            "Pasá cada fracción a decimal dividiendo numerador por denominador. Ayuda saber que `1/16 = 0.0625` y `1/32 = 0.03125`.",
            "Con todo en decimal, descartá los que superan `0.25` y quedate con el mayor de los restantes.",
        ],
        "solution": [
            "`1/32 = 0.03125`, así que `7/32 = 7 × 0.03125 = 0.21875` (o `7 ÷ 32 = 0.21875`).",
            "Las otras: `3/16 = 0.1875`, `9/32 = 0.28125`, `5/16 = 0.3125`.",
            "Más finos que `0.25` (= `0.25000`): `0.1875` y `0.21875`. El más grueso de esos dos es `0.21875`, es decir, `7/32`.",
            "`9/32 = 0.28125`: la cifra de los centésimos es 8 y la siguiente es 1 (< 5), así que queda `0.28`.",
            "Respuestas: `0.21875`, el de `7/32` y `0.28`. Error típico: comparar solo los numeradores (`9 > 7 > 5 > 3`) sin llevar las fracciones al mismo denominador o a decimal.",
        ],
    },
    {
        "id": "a-decimales-valor-posicional-3",
        "node": "a-decimales-valor-posicional",
        "kind": "problem",
        "level": 3,
        "title": "Control de calidad de un eje",
        "statement": "Un tornero mide el diámetro de un eje con un micrómetro digital que muestra **4 decimales**: **12.4846 mm**. La planilla de control pide registrar el valor redondeado a **centésimos** (2 decimales), y la pieza se acepta si el valor registrado está entre **12.45 mm** y **12.48 mm**, inclusive.",
        "parts": [
            {
                "prompt": "a) ¿Qué valor debe registrar? Respondé solo con el número en mm.",
                "check": {"type": "numeric", "value": 12.48, "tolerance": 0, "unit": "mm"},
                "answer": "12.48 mm (la pieza se acepta)",
            },
            {
                "prompt": "b) Otro operario redondea primero a milésimos y después redondea ESE resultado a centésimos. ¿Qué anota y qué pasa con la pieza?",
                "check": {"type": "choice", "options": [
                    "Anota 12.49 y rechaza una pieza que en realidad cumple: el doble redondeo arrastra el error",
                    "Anota 12.48 y la acepta: redondear en dos pasos da siempre lo mismo",
                    "Anota 12.49 y la acepta, porque 12.49 está dentro del rango",
                    "Anota 12.5 y la rechaza, porque el último 5 hace subir todas las cifras",
                ], "correct": 0},
                "answer": "Anota 12.49 y la rechaza por error de doble redondeo",
            },
            {
                "prompt": "c) ¿Cuál es la MAYOR lectura posible del micrómetro (con sus 4 decimales) que, redondeada correctamente a centésimos, da 12.48? Respondé solo con el número en mm.",
                "check": {"type": "numeric", "value": 12.4849, "tolerance": 0, "unit": "mm"},
                "answer": "12.4849 mm",
            },
        ],
        "hints": [
            "Para redondear a centésimos se mira SOLO la cifra de los milésimos, la que está justo a la derecha del corte.",
            "Hacé el redondeo en dos pasos como el operario y fijate qué cambia en el primero.",
            "Para c): ¿a partir de qué valor una lectura ya se redondea a 12.49?",
        ],
        "solution": [
            "`12.4846`: el corte va después de los centésimos (`12.48|46`). La cifra siguiente es 4 (< 5), así que queda `12.48`, dentro del rango: se acepta.",
            "Doble redondeo: a milésimos, `12.484|6` → como 6 ≥ 5, sube a `12.485`. Después, a centésimos, `12.48|5` → como 5 ≥ 5, sube a `12.49`.",
            "`12.49` supera el máximo `12.48`: el operario rechaza una pieza que cumple. El error viene de redondear un valor ya redondeado.",
            "Una lectura se redondea a `12.48` si la cifra de los milésimos (después de `12.48`) es menor que 5, o sea, si va de `12.4750` a `12.4849`. Desde `12.4850` ya da `12.49`.",
            "Con 4 decimales, la mayor es `12.4849 mm`. Respuestas: `12.48 mm`; anota 12.49 y la rechaza; `12.4849 mm`.",
        ],
    },
    # ---------- a-sumar-restar-decimales ----------
    {
        "id": "a-sumar-restar-decimales-1",
        "node": "a-sumar-restar-decimales",
        "kind": "problem",
        "level": 1,
        "title": "Parciales de natación",
        "statement": "En una prueba de 150 m, una nadadora hizo los tres parciales de 50 m en **31.45 s**, **33.8 s** y **34.07 s**. Su mejor marca anterior en esa misma prueba era **1 min 40.1 s**.",
        "parts": [
            {
                "prompt": "a) ¿Cuál fue su tiempo total? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 99.32, "tolerance": 0, "unit": "s"},
                "answer": "99.32 s (1 min 39.32 s)",
            },
            {
                "prompt": "b) ¿Por cuántos segundos mejoró su marca anterior? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 0.78, "tolerance": 0, "unit": "s"},
                "answer": "0.78 s",
            },
        ],
        "hints": [
            "Encolumná las comas y completá con ceros: `33.8 = 33.80`.",
            "Antes de restar, pasá la marca anterior a segundos (1 min = 60 s).",
        ],
        "solution": [
            "Encolumnando: `31.45 + 33.80 + 34.07 = 99.32 s`.",
            "Marca anterior en segundos: `60 + 40.1 = 100.1 s`.",
            "Mejora: `100.10 − 99.32 = 0.78 s`.",
            "Control con estimación: `31 + 34 + 34 ≈ 99` y `100 − 99 ≈ 1`, coherente. Respuestas: 99.32 s y 0.78 s. Error típico: alinear `33.8` por la derecha y sumarlo como si fuera `3.38`.",
        ],
    },
    {
        "id": "a-sumar-restar-decimales-2",
        "node": "a-sumar-restar-decimales",
        "kind": "problem",
        "level": 2,
        "title": "Cortes en una tabla",
        "statement": "De una tabla de **2.4 m** tenés que cortar tres piezas de **0.85 m**, **0.675 m** y **0.5 m**. Para separar cada pieza hacés un corte con la sierra (3 cortes en total), y cada corte se come **3 mm** (0.003 m) de madera.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto miden las tres piezas juntas? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 2.025, "tolerance": 0, "unit": "m"},
                "answer": "2.025 m",
            },
            {
                "prompt": "b) ¿Cuánto mide el pedazo de tabla que sobra? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 0.366, "tolerance": 0, "unit": "m"},
                "answer": "0.366 m",
            },
            {
                "prompt": "c) ¿Alcanza ese sobrante para sacar una cuarta pieza de 0.37 m?",
                "check": {"type": "choice", "options": [
                    "No: le faltan 4 mm (0.004 m)",
                    "Sí: sobran 4 mm (0.004 m)",
                    "Sí: 0.366 es mayor que 0.37 porque tiene más cifras",
                    "No: le faltan 4 cm (0.04 m)",
                ], "correct": 0},
                "answer": "No: le faltan 4 mm",
            },
        ],
        "hints": [
            "Completá con ceros para que todas tengan 3 decimales: `0.850`, `0.675`, `0.500`.",
            "Lo que se pierde en los cortes también sale de la tabla: sumalo a lo usado antes de restar.",
        ],
        "solution": [
            "Piezas: `0.850 + 0.675 + 0.500 = 2.025 m`.",
            "Cortes: `0.003 + 0.003 + 0.003 = 0.009 m`. Total que sale de la tabla: `2.025 + 0.009 = 2.034 m`.",
            "Sobrante: `2.400 − 2.034 = 0.366 m`.",
            "Comparando con 3 decimales: `0.366 < 0.370`. Falta `0.370 − 0.366 = 0.004 m = 4 mm`.",
            "Respuestas: 2.025 m, 0.366 m y no alcanza (faltan 4 mm). Error típico: olvidarse de la madera de los cortes y creer que sobran `0.375 m`, que sí alcanzaría.",
        ],
    },
    {
        "id": "a-sumar-restar-decimales-3",
        "node": "a-sumar-restar-decimales",
        "kind": "problem",
        "level": 3,
        "title": "El pluviómetro de Posadas",
        "statement": "Un pluviómetro en Posadas registró en una semana (en mm): lunes **12.75**, martes **0**, miércoles **8.4**, jueves **?** (el dato se borró), viernes **3.05**, sábado **0.6** y domingo **15**. El total de la semana fue **52.3 mm**. Antes de esa semana, en el mes ya se habían acumulado **98.65 mm**, y la lluvia media histórica de ese mes es **175 mm**.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto llovió el jueves? Respondé solo con el número en mm.",
                "check": {"type": "numeric", "value": 12.5, "tolerance": 0, "unit": "mm"},
                "answer": "12.5 mm",
            },
            {
                "prompt": "b) Al terminar esa semana, ¿cuántos mm faltan para llegar a la media histórica del mes? Respondé solo con el número en mm.",
                "check": {"type": "numeric", "value": 24.05, "tolerance": 0, "unit": "mm"},
                "answer": "24.05 mm",
            },
            {
                "prompt": "c) En lo que resta del mes solo llueve 7.8 mm un día y 9.65 mm otro. ¿Se alcanza la media histórica?",
                "check": {"type": "choice", "options": [
                    "No: el mes queda 6.6 mm por debajo de la media",
                    "Sí: la supera por 6.6 mm",
                    "No: el mes queda 13.62 mm por debajo de la media",
                    "Sí: la iguala exactamente",
                ], "correct": 0},
                "answer": "No: queda 6.6 mm por debajo",
            },
        ],
        "hints": [
            "El dato faltante es el total de la semana menos la suma de los días conocidos.",
            "Para b), sumá lo acumulado antes de la semana con lo de la semana y comparalo con 175.",
            "En c), encolumná las comas: `7.80 + 9.65`.",
        ],
        "solution": [
            "Días conocidos: `12.75 + 0 + 8.40 + 3.05 + 0.60 + 15.00 = 39.80 mm`.",
            "Jueves: `52.30 − 39.80 = 12.50 mm`.",
            "Acumulado del mes: `98.65 + 52.30 = 150.95 mm`. Faltan `175.00 − 150.95 = 24.05 mm`.",
            "Lluvia posterior: `7.80 + 9.65 = 17.45 mm`. Sigue faltando `24.05 − 17.45 = 6.60 mm`.",
            "Respuestas: 12.5 mm, 24.05 mm y no se alcanza (quedan 6.6 mm por debajo). Error típico: encolumnar `7.8` por la derecha como si fuera `0.78`, que da `10.43` y deja 13.62 mm por debajo.",
        ],
    },
    # ---------- a-multiplicar-dividir-decimales ----------
    {
        "id": "a-multiplicar-dividir-decimales-1",
        "node": "a-multiplicar-dividir-decimales",
        "kind": "problem",
        "level": 1,
        "title": "En la fiambrería",
        "statement": "En la fiambrería, el jamón cocido cuesta **$18 400 el kg** y el queso de máquina **$12 600 el kg**. Pedís **0.35 kg** de jamón y **0.45 kg** de queso.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto pagás por el jamón? Respondé solo con el número en pesos (sin puntos de miles).",
                "check": {"type": "numeric", "value": 6440, "tolerance": 0, "unit": "$"},
                "answer": "6440 ($6440)",
            },
            {
                "prompt": "b) ¿Cuánto pagás en total? Respondé solo con el número en pesos (sin puntos de miles).",
                "check": {"type": "numeric", "value": 12110, "tolerance": 0, "unit": "$"},
                "answer": "12110 ($12 110)",
            },
        ],
        "hints": [
            "Lo que pagás es precio por kg × kg que llevás.",
            "Multiplicá sin comas y después contá los decimales: `0.35` tiene 2.",
        ],
        "solution": [
            "Jamón: `18 400 × 0.35`. Sin comas: `18 400 × 35 = 644 000`; con 2 decimales: `6440.00`, o sea $6440.",
            "Queso: `12 600 × 0.45`. Sin comas: `12 600 × 45 = 567 000`; con 2 decimales: $5670.",
            "Total: `6440 + 5670 = $12 110`.",
            "Control: `0.35 kg` es un poco más de un tercio de kilo y `18 400 ÷ 3 ≈ 6133`, coherente con 6440. Error típico: correr mal la coma y pagar $644 o $64 400.",
        ],
    },
    {
        "id": "a-multiplicar-dividir-decimales-2",
        "node": "a-multiplicar-dividir-decimales",
        "kind": "problem",
        "level": 2,
        "title": "Rendimiento del auto",
        "statement": "En un viaje, un auto recorrió **387.5 km** y gastó **31 L** de nafta. Ahora vas a hacer un viaje de **562.5 km** con el mismo rendimiento, y la nafta cuesta **$1240.80 el litro**.",
        "parts": [
            {
                "prompt": "a) ¿Cuántos km recorre el auto por litro? Respondé solo con el número en km/L.",
                "check": {"type": "numeric", "value": 12.5, "tolerance": 0, "unit": "km/L"},
                "answer": "12.5 km/L",
            },
            {
                "prompt": "b) ¿Cuántos litros vas a necesitar para el viaje nuevo? Respondé solo con el número en L.",
                "check": {"type": "numeric", "value": 45, "tolerance": 0, "unit": "L"},
                "answer": "45 L",
            },
            {
                "prompt": "c) ¿Cuánto vas a gastar en nafta? Respondé solo con el número en pesos (sin puntos de miles).",
                "check": {"type": "numeric", "value": 55836, "tolerance": 0, "unit": "$"},
                "answer": "55836 ($55 836)",
            },
        ],
        "hints": [
            "Rendimiento = km recorridos ÷ litros gastados.",
            "Litros necesarios = km del viaje ÷ rendimiento. Para dividir por un decimal, corré la coma en los dos números hasta que el divisor sea entero.",
        ],
        "solution": [
            "Rendimiento: `387.5 ÷ 31 = 12.5 km/L` (control: `31 × 12.5 = 387.5`).",
            "Litros: `562.5 ÷ 12.5`. Corriendo la coma un lugar en ambos: `5625 ÷ 125 = 45 L`.",
            "Costo: `45 × 1240.80`. Sin comas: `45 × 124 080 = 5 583 600`; con 2 decimales: `55 836.00`.",
            "Respuestas: 12.5 km/L, 45 L y $55 836. Control con estimación: `45 × 1200 = 54 000`, cerca. Error típico: dividir al revés (`31 ÷ 387.5 = 0.08`, que son litros por km).",
        ],
    },
    {
        "id": "a-multiplicar-dividir-decimales-3",
        "node": "a-multiplicar-dividir-decimales",
        "kind": "problem",
        "level": 3,
        "title": "¿Qué detergente conviene?",
        "statement": "En el súper hay tres presentaciones del mismo detergente: botella de **0.75 L** a **$1890**, botella de **1.25 L** a **$3000** y pack de **3 botellas de 0.5 L** a **$3480**. Necesitás exactamente **6 L** y solo podés comprar envases enteros.",
        "parts": [
            {
                "prompt": "a) ¿Qué presentación tiene el menor precio por litro?",
                "check": {"type": "choice", "options": [
                    "La botella de 0.75 L",
                    "La botella de 1.25 L",
                    "El pack de 3 botellas de 0.5 L",
                ], "correct": 2},
                "answer": "El pack de 3 × 0.5 L ($2320 por litro)",
            },
            {
                "prompt": "b) ¿Cuánto cuesta el litro en esa presentación? Respondé solo con el número en pesos (sin puntos de miles).",
                "check": {"type": "numeric", "value": 2320, "tolerance": 0, "unit": "$/L"},
                "answer": "2320 ($2320 por litro)",
            },
            {
                "prompt": "c) ¿Cuánto ahorrás si comprás los 6 L en la presentación más barata por litro en vez de en la más cara por litro? Respondé solo con el número en pesos (sin puntos de miles).",
                "check": {"type": "numeric", "value": 1200, "tolerance": 0, "unit": "$"},
                "answer": "1200 ($1200)",
            },
        ],
        "hints": [
            "Compará precio por litro: precio ÷ litros de la presentación. El pack trae `3 × 0.5` litros.",
            "Para dividir por un decimal, multiplicá dividendo y divisor por 100 (o por 10) hasta que el divisor sea entero.",
            "Para c), calculá cuántos envases de cada presentación hacen 6 L justos y cuánto pagás en cada caso.",
        ],
        "solution": [
            "Botella de 0.75 L: `1890 ÷ 0.75 = 189 000 ÷ 75 = $2520` por litro.",
            "Botella de 1.25 L: `3000 ÷ 1.25 = 300 000 ÷ 125 = $2400` por litro.",
            "Pack: trae `3 × 0.5 = 1.5 L`, así que `3480 ÷ 1.5 = 34 800 ÷ 15 = $2320` por litro. Es el más barato; el más caro es la botella de 0.75 L.",
            "6 L en packs: `6 ÷ 1.5 = 4` packs → `4 × 3480 = $13 920`. 6 L en botellas de 0.75: `6 ÷ 0.75 = 8` botellas → `8 × 1890 = $15 120`.",
            "Ahorro: `15 120 − 13 920 = $1200` (control: `6 × (2520 − 2320) = 6 × 200 = 1200`).",
            "Respuestas: el pack, $2320 por litro y $1200 de ahorro. Error típico: comparar los precios de cada envase sin llevarlos a precio por litro (la botella de 0.75 L parece la más barata y es la más cara).",
        ],
    },
    # ---------- a-exponentes-potencias-10 ----------
    {
        "id": "a-exponentes-potencias-10-1",
        "node": "a-exponentes-potencias-10",
        "kind": "problem",
        "level": 1,
        "title": "Miligramos y gramos de un antibiótico",
        "statement": "Un antibiótico viene en comprimidos de **2.5 × 10² mg**. Cada caja trae **3 blísteres de 10 comprimidos**. El tratamiento indicado es **1 comprimido cada 8 horas durante 7 días**. Recordá que `1 g = 10³ mg`.",
        "parts": [
            {
                "prompt": "a) ¿Cuántos mg tiene cada comprimido? Respondé solo con el número en mg.",
                "check": {"type": "numeric", "value": 250, "tolerance": 0, "unit": "mg"},
                "answer": "250 mg",
            },
            {
                "prompt": "b) ¿Cuántos gramos de antibiótico hay en una caja completa? Respondé solo con el número en g.",
                "check": {"type": "numeric", "value": 7.5, "tolerance": 0, "unit": "g"},
                "answer": "7.5 g",
            },
            {
                "prompt": "c) ¿Cuántos gramos de antibiótico toma en todo el tratamiento? Respondé solo con el número en g.",
                "check": {"type": "numeric", "value": 5.25, "tolerance": 0, "unit": "g"},
                "answer": "5.25 g",
            },
        ],
        "hints": [
            "Multiplicar por `10²` corre la coma 2 lugares a la derecha; dividir por `10³` la corre 3 lugares a la izquierda.",
            "Para el tratamiento: ¿cuántas tomas hay por día si toma cada 8 horas?",
        ],
        "solution": [
            "`2.5 × 10² = 2.5 × 100 = 250 mg` (la coma se corre 2 lugares a la derecha).",
            "Una caja: `3 × 10 = 30` comprimidos → `30 × 250 = 7500 mg`. En gramos: `7500 ÷ 10³ = 7.5 g`.",
            "Tratamiento: `24 ÷ 8 = 3` tomas por día, durante 7 días → `3 × 7 = 21` comprimidos.",
            "`21 × 250 = 5250 mg = 5250 ÷ 10³ = 5.25 g`.",
            "Respuestas: 250 mg, 7.5 g y 5.25 g (alcanza con una caja y sobran 9 comprimidos). Error típico: leer `10²` como `10 × 2 = 20` y obtener 50 mg por comprimido.",
        ],
    },
    {
        "id": "a-exponentes-potencias-10-2",
        "node": "a-exponentes-potencias-10",
        "kind": "problem",
        "level": 2,
        "title": "Una cadena de mensajes",
        "statement": "Una cadena de mensajes arranca así: en la ronda 1 la reciben 3 personas. En cada ronda siguiente, cada persona que la recibió en la ronda anterior la reenvía a 3 personas nuevas (nadie la recibe dos veces).",
        "parts": [
            {
                "prompt": "a) ¿Cuántas personas la reciben en la ronda 5? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 243, "tolerance": 0, "unit": "personas"},
                "answer": "243 personas",
            },
            {
                "prompt": "b) ¿Cuántas personas la recibieron en total entre las rondas 1 y 5? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 363, "tolerance": 0, "unit": "personas"},
                "answer": "363 personas",
            },
            {
                "prompt": "c) ¿En qué ronda la reciben, en esa sola ronda, más de 10⁴ personas por primera vez? Respondé solo con el número de ronda.",
                "check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": "ronda"},
                "answer": "9 (en la ronda 9 la reciben 19 683 personas)",
            },
        ],
        "hints": [
            "Armá una tablita: ronda 1 → 3, ronda 2 → 3 × 3, ronda 3 → 3 × 3 × 3… ¿Qué potencia de 3 corresponde a la ronda n?",
            "`10⁴ = 10 000`. Seguí calculando potencias de 3 (cada una es la anterior × 3) hasta pasarte.",
        ],
        "solution": [
            "Cada ronda multiplica por 3 la anterior, así que en la ronda n la reciben `3ⁿ` personas.",
            "Ronda 5: `3⁵ = 3 × 3 × 3 × 3 × 3 = 243`.",
            "Total: `3 + 9 + 27 + 81 + 243 = 363` personas.",
            "Potencias de 3: `3⁶ = 729`, `3⁷ = 2187`, `3⁸ = 6561`, `3⁹ = 19 683`. Como `10⁴ = 10 000`, la primera que lo supera es `3⁹`.",
            "Respuestas: 243, 363 y la ronda 9. Error típico: calcular `3⁵` como `3 × 5 = 15`.",
        ],
    },
    {
        "id": "a-exponentes-potencias-10-3",
        "node": "a-exponentes-potencias-10",
        "kind": "problem",
        "level": 3,
        "title": "Operación combinada y centro de datos",
        "statement": "Primera parte: calculá `E = 2 + 3 × (4² − 2³)² ÷ 6 − 10⁰` respetando el orden de operaciones.\n\nSegunda parte: un centro de datos procesa **3 × 10⁴** consultas por segundo durante **2 × 10³** segundos, y las reparte en partes iguales entre **1.5 × 10²** servidores.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale E? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 33, "tolerance": 0, "unit": ""},
                "answer": "33",
            },
            {
                "prompt": "b) Un compañero obtuvo E = 97. ¿Qué error cometió?",
                "check": {"type": "choice", "options": [
                    "Distribuyó el cuadrado sobre la resta: (4² − 2³)² = 4⁴ − 2⁶",
                    "Tomó 10⁰ = 0",
                    "Sumó 2 + 3 antes de multiplicar",
                    "Calculó 8² como 8 × 2",
                ], "correct": 0},
                "answer": "Distribuyó el cuadrado sobre la resta",
            },
            {
                "prompt": "c) ¿Cuántas consultas procesa cada servidor? Respondé solo con el número (sin puntos de miles).",
                "check": {"type": "numeric", "value": 400000, "tolerance": 0, "unit": "consultas"},
                "answer": "400000 (4 × 10⁵ consultas)",
            },
        ],
        "hints": [
            "Orden: paréntesis → potencias → multiplicaciones y divisiones de izquierda a derecha → sumas y restas.",
            "Para b), rehacé la cuenta con cada error propuesto y fijate cuál da 97.",
            "Para c), multiplicá los números entre sí y las potencias de 10 entre sí (sumando exponentes); al dividir, restás exponentes.",
        ],
        "solution": [
            "Paréntesis: `4² − 2³ = 16 − 8 = 8`. Potencias: `8² = 64` y `10⁰ = 1`.",
            "Multiplicación y división de izquierda a derecha: `3 × 64 = 192`, `192 ÷ 6 = 32`. Entonces `E = 2 + 32 − 1 = 33`.",
            "Con el error del cuadrado distribuido: `4⁴ − 2⁶ = 256 − 64 = 192`, y `2 + 3 × 192 ÷ 6 − 1 = 2 + 96 − 1 = 97`. Los otros errores dan 34 (`10⁰ = 0`), `5 × 64 ÷ 6 − 1 ≈ 52.3` (sumar primero) y 9 (`8 × 2 = 16`).",
            "Consultas totales: `(3 × 10⁴) × (2 × 10³) = 6 × 10⁷`.",
            "Por servidor: `6 × 10⁷ ÷ (1.5 × 10²) = (6 ÷ 1.5) × 10⁷⁻² = 4 × 10⁵ = 400 000`.",
            "Respuestas: E = 33; el error fue distribuir el cuadrado; 400 000 consultas. Recordá que `(a − b)² ≠ a² − b²`.",
        ],
    },
    # ---------- a-sumar-restar-negativos ----------
    {
        "id": "a-sumar-restar-negativos-1",
        "node": "a-sumar-restar-negativos",
        "kind": "problem",
        "level": 1,
        "title": "Un día de invierno en La Quiaca",
        "statement": "A las 6 h, en La Quiaca el termómetro marcaba **−7°C**. Desde ahí la temperatura subió sin parar **18°C** hasta las 14 h, y después bajó sin parar **21°C** hasta las 23 h.",
        "parts": [
            {
                "prompt": "a) ¿Qué temperatura hacía a las 14 h? Respondé solo con el número en °C.",
                "check": {"type": "numeric", "value": 11, "tolerance": 0, "unit": "°C"},
                "answer": "11 °C",
            },
            {
                "prompt": "b) ¿Qué temperatura hacía a las 23 h? Respondé solo con el número en °C, con el signo incluido.",
                "check": {"type": "numeric", "value": -10, "tolerance": 0, "unit": "°C"},
                "answer": "−10 °C",
            },
            {
                "prompt": "c) ¿Cuál fue la amplitud térmica entre las 6 h y las 23 h (máxima − mínima)? Respondé solo con el número en °C.",
                "check": {"type": "numeric", "value": 21, "tolerance": 0, "unit": "°C"},
                "answer": "21 °C",
            },
        ],
        "hints": [
            "Subir es sumar (moverte a la derecha en la recta); bajar es restar (moverte a la izquierda).",
            "La máxima y la mínima no tienen por qué ser las de las 6 h y las 14 h: mirá los tres valores.",
        ],
        "solution": [
            "14 h: `−7 + 18 = 11 °C`.",
            "23 h: `11 − 21 = −10 °C`.",
            "Como subió sin parar hasta las 14 h y bajó sin parar después, la máxima es `11 °C` y la mínima es la menor entre `−7` y `−10`: `−10 °C` (más a la izquierda en la recta).",
            "Amplitud: `11 − (−10) = 11 + 10 = 21 °C`.",
            "Respuestas: 11 °C, −10 °C y 21 °C. Error típico: tomar `−7` como mínima (porque 7 < 10) y obtener 18 °C.",
        ],
    },
    {
        "id": "a-sumar-restar-negativos-2",
        "node": "a-sumar-restar-negativos",
        "kind": "problem",
        "level": 2,
        "title": "La cuenta corriente del taller",
        "statement": "La cuenta corriente de un taller arranca el mes con saldo **−$12 500** (en descubierto). Los movimientos, en este orden, fueron: depósito de **$38 000**; débito de la luz por **$9200**; débito de la tarjeta por **$31 700**; devolución de una compra por **$4600** (acreditada); y el banco **anula** un débito erróneo de **$2300** que ya estaba descontado del saldo.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el saldo al final del mes? Respondé solo con el número en pesos, con el signo incluido (sin puntos de miles).",
                "check": {"type": "numeric", "value": -8500, "tolerance": 0, "unit": "$"},
                "answer": "−8500 (−$8500)",
            },
            {
                "prompt": "b) ¿Cuál fue el saldo MÁS BAJO durante el mes (después de algún movimiento)? Respondé solo con el número en pesos, con el signo incluido (sin puntos de miles).",
                "check": {"type": "numeric", "value": -15400, "tolerance": 0, "unit": "$"},
                "answer": "−15400 (−$15 400, después del débito de la tarjeta)",
            },
            {
                "prompt": "c) ¿Cuánto tiene que depositar al final del mes para que el saldo quede en +$5000? Respondé solo con el número en pesos (sin puntos de miles).",
                "check": {"type": "numeric", "value": 13500, "tolerance": 0, "unit": "$"},
                "answer": "13500 ($13 500)",
            },
        ],
        "hints": [
            "Depósitos y acreditaciones suman; débitos restan. Anular un débito es restar un negativo: `− (−2300) = + 2300`.",
            "Para b), anotá el saldo después de CADA movimiento.",
            "Para c), la distancia en la recta entre el saldo final y +5000 es `5000 − (saldo final)`.",
        ],
        "solution": [
            "Partida: `−12 500`. Depósito: `−12 500 + 38 000 = 25 500`.",
            "Luz: `25 500 − 9200 = 16 300`. Tarjeta: `16 300 − 31 700 = −15 400`.",
            "Devolución: `−15 400 + 4600 = −10 800`. Anulación del débito: `−10 800 − (−2300) = −10 800 + 2300 = −8500`.",
            "El saldo más bajo de la lista `25 500, 16 300, −15 400, −10 800, −8500` es `−15 400` (el más a la izquierda en la recta).",
            "Para llegar a +5000: `5000 − (−8500) = 5000 + 8500 = 13 500`.",
            "Respuestas: −$8500, −$15 400 y $13 500. Error típico: restar la anulación (`−10 800 − 2300 = −13 100`).",
        ],
    },
    {
        "id": "a-sumar-restar-negativos-3",
        "node": "a-sumar-restar-negativos",
        "kind": "problem",
        "level": 3,
        "title": "Resultados de un semestre",
        "statement": "Una pyme registró sus resultados mensuales (ganancia positiva, pérdida negativa), en miles de pesos: enero **+320**, febrero **−145**, marzo **−210**, abril **+95**, mayo **−60** y junio **+180**. Llamamos **variación** de un mes al resultado de ese mes menos el resultado del mes anterior.",
        "parts": [
            {
                "prompt": "a) ¿Cuál fue el resultado acumulado del semestre? Respondé solo con el número en miles de pesos, con el signo si corresponde.",
                "check": {"type": "numeric", "value": 180, "tolerance": 0, "unit": "miles de $"},
                "answer": "180 miles de pesos (+$180 000)",
            },
            {
                "prompt": "b) ¿Cuál fue la variación MÁS NEGATIVA (la peor caída de un mes al siguiente)? Respondé solo con el número en miles de pesos, con el signo incluido.",
                "check": {"type": "numeric", "value": -465, "tolerance": 0, "unit": "miles de $"},
                "answer": "−465 miles de pesos (de enero a febrero)",
            },
            {
                "prompt": "c) Si vas sumando mes a mes, ¿cuál fue el MENOR valor que tomó el acumulado? Respondé solo con el número en miles de pesos, con el signo incluido.",
                "check": {"type": "numeric", "value": -35, "tolerance": 0, "unit": "miles de $"},
                "answer": "−35 miles de pesos (al cierre de marzo)",
            },
        ],
        "hints": [
            "Para el acumulado, agrupá positivos por un lado y negativos por el otro, y después restá.",
            "Variación = mes − mes anterior. Cuando el mes anterior es negativo, restás un negativo: `−210 − (−145) = −210 + 145`.",
            "Para c), escribí el acumulado al final de cada mes: enero, enero + febrero, y así.",
        ],
        "solution": [
            "Positivos: `320 + 95 + 180 = 595`. Negativos: `−145 − 210 − 60 = −415`. Acumulado: `595 − 415 = 180`.",
            "Variaciones: feb `−145 − 320 = −465`; mar `−210 − (−145) = −65`; abr `95 − (−210) = 305`; may `−60 − 95 = −155`; jun `180 − (−60) = 240`.",
            "La más negativa es `−465` (de enero a febrero). Ojo: marzo tuvo el peor resultado, pero su variación (`−65`) fue chica.",
            "Acumulados: ene `320`; feb `175`; mar `−35`; abr `60`; may `0`; jun `180`.",
            "El menor es `−35` (al cierre de marzo). Respuestas: 180, −465 y −35 (en miles de pesos). Error típico: en las variaciones, hacer `95 − 210 = −115` en vez de `95 − (−210) = 305`.",
        ],
    },
    # ---------- a-multiplicar-dividir-negativos ----------
    {
        "id": "a-multiplicar-dividir-negativos-1",
        "node": "a-multiplicar-dividir-negativos",
        "kind": "problem",
        "level": 1,
        "title": "El freezer recién enchufado",
        "statement": "Un freezer está a **4°C** cuando lo enchufás y, a partir de ahí, la temperatura cambia **−3°C por hora** de forma pareja hasta llegar a **−20°C**, su temperatura de trabajo.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto cambió la temperatura en las primeras 7 horas? Respondé solo con el número en °C, con el signo incluido.",
                "check": {"type": "numeric", "value": -21, "tolerance": 0, "unit": "°C"},
                "answer": "−21 °C",
            },
            {
                "prompt": "b) ¿Qué temperatura marca a las 7 horas de enchufarlo? Respondé solo con el número en °C, con el signo incluido.",
                "check": {"type": "numeric", "value": -17, "tolerance": 0, "unit": "°C"},
                "answer": "−17 °C",
            },
            {
                "prompt": "c) ¿Cuántas horas tarda en llegar a −20°C desde que lo enchufás? Respondé solo con el número en h.",
                "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": "h"},
                "answer": "8 h",
            },
        ],
        "hints": [
            "Cambio total = (cambio por hora) × (horas). Signos distintos → resultado negativo.",
            "Para c), calculá el cambio total que necesita (final − inicial) y dividilo por el cambio por hora.",
        ],
        "solution": [
            "Cambio en 7 h: `7 × (−3) = −21 °C`.",
            "Temperatura a las 7 h: `4 + (−21) = −17 °C`.",
            "Cambio total necesario: `−20 − 4 = −24 °C`.",
            "Horas: `(−24) ÷ (−3) = 8 h` (signos iguales → positivo, como tiene que ser un tiempo).",
            "Control: `4 + 8 × (−3) = 4 − 24 = −20` ✓. Respuestas: −21 °C, −17 °C y 8 h. Error típico: hacer `20 ÷ 3` olvidando que arranca en +4 °C.",
        ],
    },
    {
        "id": "a-multiplicar-dividir-negativos-2",
        "node": "a-multiplicar-dividir-negativos",
        "kind": "problem",
        "level": 2,
        "title": "Torneo de preguntas",
        "statement": "En un torneo de preguntas de 25 preguntas, cada respuesta correcta suma **4 puntos**, cada incorrecta resta **3** y cada pregunta sin responder resta **1**. Ana tuvo 12 correctas, 9 incorrectas y 4 sin responder. Bruno tuvo 8 correctas, 14 incorrectas y 3 sin responder.",
        "parts": [
            {
                "prompt": "a) ¿Cuántos puntos sacó Ana? Respondé solo con el número, con el signo si corresponde.",
                "check": {"type": "numeric", "value": 17, "tolerance": 0, "unit": "puntos"},
                "answer": "17 puntos",
            },
            {
                "prompt": "b) ¿Cuántos puntos sacó Bruno? Respondé solo con el número, con el signo incluido.",
                "check": {"type": "numeric", "value": -13, "tolerance": 0, "unit": "puntos"},
                "answer": "−13 puntos",
            },
            {
                "prompt": "c) Carla también participa. ¿Cuántos puntos tiene que sacar para que el promedio de los tres sea exactamente −2? Respondé solo con el número, con el signo incluido.",
                "check": {"type": "numeric", "value": -10, "tolerance": 0, "unit": "puntos"},
                "answer": "−10 puntos",
            },
        ],
        "hints": [
            "Escribí cada puntaje como `correctas × 4 + incorrectas × (−3) + sin responder × (−1)`.",
            "Si el promedio de 3 puntajes es −2, la suma de los 3 es `3 × (−2)`.",
        ],
        "solution": [
            "Ana: `12 × 4 + 9 × (−3) + 4 × (−1) = 48 − 27 − 4 = 17`.",
            "Bruno: `8 × 4 + 14 × (−3) + 3 × (−1) = 32 − 42 − 3 = −13`.",
            "Promedio −2 entre 3 personas → la suma tiene que ser `3 × (−2) = −6`.",
            "Ana + Bruno = `17 + (−13) = 4`. Carla: `−6 − 4 = −10`.",
            "Control: `(17 − 13 − 10) ÷ 3 = −6 ÷ 3 = −2` ✓ (Carla puede lograrlo, por ejemplo con 5 correctas, 5 incorrectas y 15 sin responder). Respuestas: 17, −13 y −10. Error típico: hacer `14 × (−3) = +42`.",
        ],
    },
    {
        "id": "a-multiplicar-dividir-negativos-3",
        "node": "a-multiplicar-dividir-negativos",
        "kind": "problem",
        "level": 3,
        "title": "Signos, potencias y orden de operaciones",
        "statement": "Resolvé respetando el orden de operaciones:\n\n`E = (−2)³ − 3 × (−4)² ÷ (−6) + (−1)⁵ × (−3²)`\n\n`F = −48 ÷ (−2)³ × (−3) − (−5)²`",
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale E? Respondé solo con el número, con el signo si corresponde.",
                "check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": ""},
                "answer": "9",
            },
            {
                "prompt": "b) Un compañero obtuvo E = −9. ¿Qué error cometió?",
                "check": {"type": "choice", "options": [
                    "Calculó −3² como +9 (le aplicó el cuadrado también al signo menos)",
                    "Calculó (−2)³ como +8",
                    "Calculó (−4)² como −16",
                    "Calculó 3 × (−4)² como (3 × (−4))² = 144",
                ], "correct": 0},
                "answer": "Tomó −3² como +9",
            },
            {
                "prompt": "c) ¿Cuánto vale F? Respondé solo con el número, con el signo incluido.",
                "check": {"type": "numeric", "value": -43, "tolerance": 0, "unit": ""},
                "answer": "−43",
            },
        ],
        "hints": [
            "Primero las potencias. Ojo: `(−3)²` y `−3²` NO son lo mismo; sin paréntesis el cuadrado afecta solo al 3.",
            "Multiplicaciones y divisiones van de izquierda a derecha, con la regla de signos en cada paso.",
            "En F, la división `−48 ÷ (−2)³` se hace ANTES que la multiplicación por `(−3)`, porque está más a la izquierda.",
        ],
        "solution": [
            "Potencias de E: `(−2)³ = −8`, `(−4)² = 16`, `(−1)⁵ = −1` (exponente impar) y `−3² = −(3 × 3) = −9`.",
            "Término del medio, de izquierda a derecha: `3 × 16 = 48` y `48 ÷ (−6) = −8`. Último término: `(−1) × (−9) = 9`.",
            "`E = −8 − (−8) + 9 = −8 + 8 + 9 = 9`.",
            "Con `−3² = +9` el último término sería `(−1) × 9 = −9` y E daría `−8 + 8 − 9 = −9`: ese fue el error. Los otros dan 25, −7 y 25.",
            "F: `(−2)³ = −8` y `(−5)² = 25`. De izquierda a derecha: `−48 ÷ (−8) = 6`; `6 × (−3) = −18`.",
            "`F = −18 − 25 = −43`. Respuestas: E = 9, el error fue `−3² = 9`, F = −43. Error típico en F: hacer primero `(−8) × (−3) = 24` y obtener `−48 ÷ 24 − 25 = −27`.",
        ],
    },
    # ============================ PREÁLGEBRA ============================
    # ---------- p-factores-multiplos ----------
    {
        "id": "p-factores-multiplos-1",
        "node": "p-factores-multiplos",
        "kind": "problem",
        "level": 1,
        "title": "Baldosas sin cortes",
        "statement": "Querés cubrir el piso de un patio rectangular de **3.15 m × 4.05 m** con baldosas cuadradas, todas iguales y lo más grandes posible, sin cortar ninguna. El lado de cada baldosa tiene que ser un número entero de centímetros. Las baldosas se venden en cajas de **8 unidades**.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto mide el lado de cada baldosa? Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 45, "tolerance": 0, "unit": "cm"},
                "answer": "45 cm",
            },
            {
                "prompt": "b) ¿Cuántas baldosas necesitás? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 63, "tolerance": 0, "unit": "baldosas"},
                "answer": "63 baldosas",
            },
            {
                "prompt": "c) ¿Cuántas cajas tenés que comprar? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": "cajas"},
                "answer": "8 cajas (sobra 1 baldosa)",
            },
        ],
        "hints": [
            "Pasá las medidas a cm. El lado tiene que dividir exactamente a los dos lados del patio y ser el mayor posible: es el MCD.",
            "Descomponé 315 y 405 en factores primos y quedate con los primos comunes, con el menor exponente.",
        ],
        "solution": [
            "En cm: el patio mide `315 cm × 405 cm`.",
            "`315 = 3² × 5 × 7` y `405 = 3⁴ × 5`. Comunes con el menor exponente: `3² × 5 = 45`. MCD = 45 cm.",
            "Baldosas por lado: `315 ÷ 45 = 7` y `405 ÷ 45 = 9`. Total: `7 × 9 = 63` baldosas.",
            "Cajas: `63 ÷ 8 = 7.875`; con 7 cajas (56) no alcanza, así que hacen falta **8 cajas** (64 baldosas, sobra 1).",
            "Respuestas: 45 cm, 63 baldosas y 8 cajas. Error típico: usar el mcm, que da una baldosa más grande que el propio patio.",
        ],
    },
    {
        "id": "p-factores-multiplos-2",
        "node": "p-factores-multiplos",
        "kind": "problem",
        "level": 2,
        "title": "Tres remedios con distintos horarios",
        "statement": "Por indicación médica, Martín toma el remedio A cada **4 h**, el B cada **6 h** y el C cada **10 h**. El lunes a las **8:00** tomó los tres juntos.",
        "parts": [
            {
                "prompt": "a) ¿Cada cuántas horas le toca tomar los tres juntos? Respondé solo con el número en h.",
                "check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": "h"},
                "answer": "60 h",
            },
            {
                "prompt": "b) ¿Qué día y a qué hora vuelve a tomar los tres juntos por primera vez?",
                "check": {"type": "choice", "options": [
                    "Miércoles a las 20:00",
                    "Martes a las 20:00",
                    "Miércoles a las 8:00",
                    "Jueves a las 8:00",
                ], "correct": 0},
                "answer": "Miércoles a las 20:00",
            },
            {
                "prompt": "c) Entre esas dos tomas triples (sin contarlas), ¿cuántas veces toma A y B juntos SIN el C? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "veces"},
                "answer": "4 veces (a las 12, 24, 36 y 48 h)",
            },
        ],
        "hints": [
            "Coincidencias de ciclos → mínimo común múltiplo.",
            "Sumá las horas al lunes 8:00 de a 24 h (un día) por vez.",
            "A y B coinciden cada `mcm(4, 6)` horas. De esas coincidencias, descartá las que también son múltiplo de 10.",
        ],
        "solution": [
            "`4 = 2²`, `6 = 2 × 3`, `10 = 2 × 5`. mcm: `2² × 3 × 5 = 60` h.",
            "Lunes 8:00 + 48 h = miércoles 8:00; + 12 h más = **miércoles 20:00**.",
            "A y B coinciden cada `mcm(4, 6) = 12` h: a las 12, 24, 36, 48 y 60 h de la toma inicial.",
            "C se toma a las 10, 20, 30, 40, 50 y 60 h. De las coincidencias A-B, solo la de 60 h incluye a C (y esa no se cuenta).",
            "Quedan 4 coincidencias de A y B sin C (12, 24, 36 y 48 h). Respuestas: 60 h, miércoles 20:00 y 4 veces. Error típico: multiplicar `4 × 6 × 10 = 240` en vez de usar el mcm.",
        ],
    },
    {
        "id": "p-factores-multiplos-3",
        "node": "p-factores-multiplos",
        "kind": "problem",
        "level": 3,
        "title": "Bolsones de la cooperativa",
        "statement": "Una cooperativa recibe **84 kg de yerba**, **126 kg de azúcar** y **210 kg de harina**, y arma la MAYOR cantidad posible de bolsones iguales (cada bolsón con la misma cantidad entera de kg de cada producto, sin que sobre nada). Los reparte con dos camionetas: la A sale del depósito cada **40 minutos** y la B cada **60 minutos**; las dos salieron juntas a las **8:00**. En cada salida, cada camioneta lleva exactamente **3 bolsones** (si salen juntas, son 6), y siguen saliendo hasta repartir todos.",
        "parts": [
            {
                "prompt": "a) ¿Cuántos bolsones arman? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 42, "tolerance": 0, "unit": "bolsones"},
                "answer": "42 bolsones (de 2 kg de yerba, 3 de azúcar y 5 de harina)",
            },
            {
                "prompt": "b) ¿Cada cuántos minutos salen juntas las dos camionetas? Respondé solo con el número en min.",
                "check": {"type": "numeric", "value": 120, "tolerance": 0, "unit": "min"},
                "answer": "120 min (cada 2 horas)",
            },
            {
                "prompt": "c) ¿A qué hora sale la última camioneta cargada?",
                "check": {"type": "choice", "options": ["12:40", "13:00", "13:20", "14:40"], "correct": 1},
                "answer": "13:00",
            },
        ],
        "hints": [
            "Repartir en la mayor cantidad de grupos iguales sin sobras → MCD de las tres cantidades.",
            "Las salidas juntas se repiten cada `mcm(40, 60)` minutos.",
            "Calculá cuántas salidas hacen falta (cada una lleva 3 bolsones) y listá los horarios de salida en orden, contando dos salidas cuando coinciden.",
        ],
        "solution": [
            "`84 = 2² × 3 × 7`, `126 = 2 × 3² × 7`, `210 = 2 × 3 × 5 × 7`. MCD = `2 × 3 × 7 = 42` bolsones, cada uno con `2` kg de yerba, `3` de azúcar y `5` de harina.",
            "`40 = 2³ × 5` y `60 = 2² × 3 × 5`. mcm = `2³ × 3 × 5 = 120` min: salen juntas cada 2 horas (8:00, 10:00, 12:00…).",
            "Hacen falta `42 ÷ 3 = 14` salidas. En cada ciclo de 2 h hay: la salida doble del comienzo (2 salidas) más A a los 40 y 80 min y B a los 60 min → 5 salidas por ciclo.",
            "Ciclo 8:00–9:59: 8:00 (×2), 8:40, 9:00, 9:20 → 5 salidas. Ciclo 10:00–11:59: otras 5 → 10 en total.",
            "Desde las 12:00: 12:00 (×2) → 12 salidas; 12:40 (A) → 13; 13:00 (B) → 14. Con esa se completan los 42 bolsones.",
            "Respuestas: 42 bolsones, 120 min y la última sale a las 13:00. Error típico: contar la salida conjunta como una sola salida (3 bolsones en vez de 6).",
        ],
    },
    # ---------- p-patrones-datos ----------
    {
        "id": "p-patrones-datos-1",
        "node": "p-patrones-datos",
        "kind": "problem",
        "level": 1,
        "title": "Esperando el colectivo",
        "statement": "Durante 8 días anotaste cuántos minutos esperaste el colectivo a la mañana: **7, 12, 5, 9, 31, 8, 6 y 10**. (El de 31 fue un día de paro parcial.)",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la espera media (promedio)? Respondé solo con el número en min.",
                "check": {"type": "numeric", "value": 11, "tolerance": 0, "unit": "min"},
                "answer": "11 min",
            },
            {
                "prompt": "b) ¿Cuál es la mediana? Respondé solo con el número en min.",
                "check": {"type": "numeric", "value": 8.5, "tolerance": 0, "unit": "min"},
                "answer": "8.5 min",
            },
            {
                "prompt": "c) ¿Qué medida describe mejor la espera de un día típico?",
                "check": {"type": "choice", "options": [
                    "La mediana, porque el 31 es un valor atípico que infla la media",
                    "La media, porque usa todos los datos y por eso siempre es la más representativa",
                    "El rango, porque indica cuánto esperás un día común",
                ], "correct": 0},
                "answer": "La mediana",
            },
        ],
        "hints": [
            "Media: sumá todo y dividí por la cantidad de datos.",
            "Mediana: ordená de menor a mayor. Con una cantidad PAR de datos, promediá los dos del centro.",
        ],
        "solution": [
            "Suma: `7 + 12 + 5 + 9 + 31 + 8 + 6 + 10 = 88`. Media: `88 ÷ 8 = 11` min.",
            "Ordenados: `5, 6, 7, 8, 9, 10, 12, 31`. Hay 8 datos: los del centro son el 4º y el 5º, `8` y `9`.",
            "Mediana: `(8 + 9) ÷ 2 = 8.5` min.",
            "Solo 2 de los 8 días superan la media de 11 min: el 31 la arrastra hacia arriba. La mediana no se mueve con ese extremo (sin el 31, la media sería `57 ÷ 7 ≈ 8.1`).",
            "Respuestas: 11 min, 8.5 min y la mediana. Error típico: tomar como mediana el dato del medio sin ordenar.",
        ],
    },
    {
        "id": "p-patrones-datos-2",
        "node": "p-patrones-datos",
        "kind": "problem",
        "level": 2,
        "title": "Plan de ahorro creciente",
        "statement": "Sofía arma un plan de ahorro: la semana 1 guarda **$1500**, y cada semana guarda **$250 más** que la semana anterior.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto guarda en la semana 20? Respondé solo con el número en pesos (sin puntos de miles).",
                "check": {"type": "numeric", "value": 6250, "tolerance": 0, "unit": "$"},
                "answer": "6250 ($6250)",
            },
            {
                "prompt": "b) ¿Cuánto juntó en total al terminar la semana 20? Respondé solo con el número en pesos (sin puntos de miles).",
                "check": {"type": "numeric", "value": 77500, "tolerance": 0, "unit": "$"},
                "answer": "77500 ($77 500)",
            },
            {
                "prompt": "c) ¿En qué semana el depósito SUPERA por primera vez los $10 000? Respondé solo con el número de semana.",
                "check": {"type": "numeric", "value": 36, "tolerance": 0, "unit": "semana"},
                "answer": "36 (deposita $10 250)",
            },
        ],
        "hints": [
            "Hasta la semana n hubo `n − 1` aumentos de $250: el depósito es `1500 + 250 × (n − 1)`.",
            "Para sumar 20 depósitos que crecen parejo, emparejá el primero con el último, el segundo con el anteúltimo… todas las parejas suman lo mismo.",
            "Ojo en c): \"supera\" significa estrictamente mayor.",
        ],
        "solution": [
            "Depósito de la semana n: `1500 + 250 × (n − 1)`. Semana 20: `1500 + 250 × 19 = 1500 + 4750 = 6250`.",
            "Parejas: semana 1 + semana 20 = `1500 + 6250 = 7750`, y lo mismo para 2 + 19, 3 + 18… Hay `20 ÷ 2 = 10` parejas.",
            "Total: `10 × 7750 = 77 500`.",
            "Para superar 10 000: `1500 + 250 × (n − 1) > 10 000` → `250 × (n − 1) > 8500` → `n − 1 > 34`. En la semana 35 deposita exactamente `1500 + 250 × 34 = 10 000` (no lo supera).",
            "En la semana 36 deposita `1500 + 250 × 35 = 10 250`. Respuestas: $6250, $77 500 y la semana 36. Error típico: hacer `1500 + 250 × 20` (contar 20 aumentos en vez de 19).",
        ],
    },
    {
        "id": "p-patrones-datos-3",
        "node": "p-patrones-datos",
        "kind": "problem",
        "level": 3,
        "title": "Promedios ponderados en el ingreso",
        "statement": "En un curso de ingreso, la nota final es un promedio ponderado: el primer parcial vale **35%**, el segundo parcial **40%** y los trabajos prácticos **25%**. Sacaste **6** en el primer parcial y **8** en los prácticos. Además, el curso tiene dos comisiones: la A, de **24 alumnos**, terminó con promedio **6.5**, y la B, de **16 alumnos**, con promedio **7.75**.",
        "parts": [
            {
                "prompt": "a) ¿Qué nota necesitás en el segundo parcial para terminar con exactamente 7? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 7.25, "tolerance": 0, "unit": ""},
                "answer": "7.25",
            },
            {
                "prompt": "b) ¿Cuál es la nota final más alta que podés alcanzar (con 10 en el segundo parcial)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 8.1, "tolerance": 0, "unit": ""},
                "answer": "8.1",
            },
            {
                "prompt": "c) ¿Cuál es el promedio de todos los alumnos del curso (las dos comisiones juntas)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": ""},
                "answer": "7",
            },
        ],
        "hints": [
            "Nota final = `0.35 × P1 + 0.40 × P2 + 0.25 × TP`. Calculá lo que ya tenés asegurado y fijate cuánto falta para llegar a 7.",
            "Para c), el promedio general NO es el promedio de los dos promedios: reconstruí la suma de notas de cada comisión (alumnos × promedio).",
        ],
        "solution": [
            "Lo asegurado: `0.35 × 6 + 0.25 × 8 = 2.1 + 2 = 4.1`.",
            "Falta `7 − 4.1 = 2.9`, que tiene que aportar el segundo parcial: `0.40 × P2 = 2.9` → `P2 = 2.9 ÷ 0.4 = 7.25`.",
            "Con 10 en el segundo: `4.1 + 0.40 × 10 = 4.1 + 4 = 8.1`.",
            "Suma de notas: comisión A `24 × 6.5 = 156`; comisión B `16 × 7.75 = 124`. Total: `156 + 124 = 280` entre `24 + 16 = 40` alumnos.",
            "Promedio general: `280 ÷ 40 = 7`.",
            "Respuestas: 7.25, 8.1 y 7. Error típico en c): promediar `(6.5 + 7.75) ÷ 2 = 7.125`, ignorando que la comisión A tiene más alumnos.",
        ],
    },
    # ---------- p-medicion-geometria ----------
    {
        "id": "p-medicion-geometria-1",
        "node": "p-medicion-geometria",
        "kind": "problem",
        "level": 1,
        "title": "Piso nuevo para el dormitorio",
        "statement": "Un dormitorio rectangular mide **4.5 m × 3.2 m**. Vas a poner piso flotante, que cuesta **$18 000 por m²**, y zócalo en todo el borde salvo en la puerta, que tiene **0.8 m** de ancho.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la superficie del piso? Respondé solo con el número en m².",
                "check": {"type": "numeric", "value": 14.4, "tolerance": 0, "unit": "m²"},
                "answer": "14.4 m²",
            },
            {
                "prompt": "b) ¿Cuánto cuesta el piso flotante? Respondé solo con el número en pesos (sin puntos de miles).",
                "check": {"type": "numeric", "value": 259200, "tolerance": 0, "unit": "$"},
                "answer": "259200 ($259 200)",
            },
            {
                "prompt": "c) ¿Cuántos metros de zócalo necesitás? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 14.6, "tolerance": 0, "unit": "m"},
                "answer": "14.6 m",
            },
        ],
        "hints": [
            "El piso cubre una SUPERFICIE (área, m²); el zócalo recorre el BORDE (perímetro, m).",
            "Al perímetro restale el ancho de la puerta.",
        ],
        "solution": [
            "Área: `4.5 × 3.2 = 14.4 m²`.",
            "Costo del piso: `14.4 × 18 000 = $259 200`.",
            "Perímetro: `2 × 4.5 + 2 × 3.2 = 9 + 6.4 = 15.4 m`.",
            "Zócalo: `15.4 − 0.8 = 14.6 m`.",
            "Respuestas: 14.4 m², $259 200 y 14.6 m. Error típico: confundir área y perímetro (comprar 14.4 m de zócalo o calcular el piso con 15.4).",
        ],
    },
    {
        "id": "p-medicion-geometria-2",
        "node": "p-medicion-geometria",
        "kind": "problem",
        "level": 2,
        "title": "Una mesa con puntas redondeadas",
        "statement": "La tapa de una mesa está formada por un rectángulo de **1.2 m × 0.8 m** con un semicírculo pegado en cada uno de los dos lados de 0.8 m (cada semicírculo tiene diámetro 0.8 m). Usá **π ≈ 3.14**.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la superficie de la tapa? Respondé solo con el número en m².",
                "check": {"type": "numeric", "value": 1.4624, "tolerance": 0, "unit": "m²"},
                "answer": "1.4624 m²",
            },
            {
                "prompt": "b) ¿Cuántos metros de cinta de canto hacen falta para cubrir todo el borde de la tapa? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 4.912, "tolerance": 0, "unit": "m"},
                "answer": "4.912 m",
            },
            {
                "prompt": "c) Querés un mantel con la misma forma que cuelgue 10 cm más allá del borde en todo el contorno. ¿Cuántos m² de tela tiene el mantel? Respondé solo con el número en m².",
                "check": {"type": "numeric", "value": 1.985, "tolerance": 0, "unit": "m²"},
                "answer": "1.985 m²",
            },
        ],
        "hints": [
            "Los dos semicírculos juntos forman un círculo entero de diámetro 0.8 m. Usá el radio, no el diámetro.",
            "El borde tiene dos tramos rectos de 1.2 m (los lados de 0.8 m quedan tapados por los semicírculos) más la circunferencia de ese círculo.",
            "En el mantel, los tramos rectos siguen midiendo 1.2 m, pero el ancho pasa a ser `0.8 + 2 × 0.1` y el radio de las puntas crece 10 cm.",
        ],
        "solution": [
            "Rectángulo: `1.2 × 0.8 = 0.96 m²`. Dos semicírculos = un círculo de radio `0.8 ÷ 2 = 0.4 m`: `3.14 × 0.4² = 3.14 × 0.16 = 0.5024 m²`.",
            "Área de la tapa: `0.96 + 0.5024 = 1.4624 m²`.",
            "Borde: dos tramos rectos `2 × 1.2 = 2.4 m` más la circunferencia `π × d = 3.14 × 0.8 = 2.512 m`. Total `2.4 + 2.512 = 4.912 m`.",
            "Mantel: rectángulo central `1.2 × 1.0 = 1.2 m²` (el ancho pasa a `0.8 + 0.2 = 1.0 m`) y un círculo de radio `0.4 + 0.1 = 0.5 m`: `3.14 × 0.25 = 0.785 m²`.",
            "Tela: `1.2 + 0.785 = 1.985 m²`. Respuestas: 1.4624 m², 4.912 m y 1.985 m². Error típico: usar el diámetro como radio (`3.14 × 0.8²`) o sumar al borde los lados de 0.8 m que no quedan expuestos.",
        ],
    },
    {
        "id": "p-medicion-geometria-3",
        "node": "p-medicion-geometria",
        "kind": "problem",
        "level": 3,
        "title": "Llenar y pintar la pileta",
        "statement": "Una pileta tiene forma de caja: **8 m** de largo, **4 m** de ancho y **1.6 m** de profundidad. Se llena hasta **10 cm** por debajo del borde con una manguera que entrega **40 L por minuto**. Antes de llenarla se pinta todo el interior (fondo y las 4 paredes completas) con **2 manos** de una pintura que rinde **8 m² por litro y por mano**, y que se vende en latas de **4 L**. Recordá: `1 m³ = 1000 L`.",
        "parts": [
            {
                "prompt": "a) ¿Cuántos litros de agua lleva la pileta? Respondé solo con el número en L (sin puntos de miles).",
                "check": {"type": "numeric", "value": 48000, "tolerance": 0, "unit": "L"},
                "answer": "48000 L (48 m³)",
            },
            {
                "prompt": "b) ¿Cuántas horas tarda en llenarse? Respondé solo con el número en h.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "h"},
                "answer": "20 h",
            },
            {
                "prompt": "c) ¿Cuántas latas de pintura hay que comprar? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "latas"},
                "answer": "5 latas",
            },
        ],
        "hints": [
            "La altura del agua no es 1.6 m: pasá los 10 cm a metros y restalos.",
            "Volumen en m³ → litros (× 1000) → minutos (÷ 40) → horas (÷ 60).",
            "La superficie a pintar es el fondo más las 4 paredes, que tienen la profundidad TOTAL de la pileta. Con 2 manos se pinta dos veces esa superficie.",
        ],
        "solution": [
            "Altura del agua: `1.6 − 0.1 = 1.5 m`. Volumen: `8 × 4 × 1.5 = 48 m³ = 48 × 1000 = 48 000 L`.",
            "Tiempo: `48 000 ÷ 40 = 1200 min = 1200 ÷ 60 = 20 h`.",
            "Fondo: `8 × 4 = 32 m²`. Paredes: `2 × (8 × 1.6) + 2 × (4 × 1.6) = 25.6 + 12.8 = 38.4 m²`. Total: `32 + 38.4 = 70.4 m²`.",
            "Con 2 manos: `2 × 70.4 = 140.8 m²` a cubrir. Litros: `140.8 ÷ 8 = 17.6 L`.",
            "Latas: `17.6 ÷ 4 = 4.4` → con 4 latas (16 L) no alcanza: hay que comprar **5 latas**.",
            "Respuestas: 48 000 L, 20 h y 5 latas. Error típico: usar 1.5 m también para las paredes, o redondear 4.4 latas hacia abajo.",
        ],
    },
    # ---------- p-variables-expresiones ----------
    {
        "id": "p-variables-expresiones-1",
        "node": "p-variables-expresiones",
        "kind": "problem",
        "level": 1,
        "title": "La tarifa del remís",
        "statement": "Una agencia de remises cobra **$1800** de bajada de bandera, **$950** por cada kilómetro recorrido y **$200** por cada minuto de espera. Llamá `k` a los kilómetros y `m` a los minutos de espera.",
        "parts": [
            {
                "prompt": "a) ¿Qué expresión da el precio total del viaje?",
                "check": {"type": "choice", "options": [
                    "1800 + 950k + 200m",
                    "1800k + 950 + 200m",
                    "(1800 + 950 + 200)(k + m)",
                    "1800 + 950 + 200 + k + m",
                ], "correct": 0},
                "answer": "1800 + 950k + 200m",
            },
            {
                "prompt": "b) ¿Cuánto cuesta un viaje de 8 km con 5 minutos de espera? Respondé solo con el número en pesos (sin puntos de miles).",
                "check": {"type": "numeric", "value": 10400, "tolerance": 0, "unit": "$"},
                "answer": "10400 ($10 400)",
            },
            {
                "prompt": "c) Si otro viaje tiene 3 km más y la misma espera, ¿cuánto más cuesta? Respondé solo con el número en pesos (sin puntos de miles).",
                "check": {"type": "numeric", "value": 2850, "tolerance": 0, "unit": "$"},
                "answer": "2850 ($2850)",
            },
        ],
        "hints": [
            "Lo fijo se suma una sola vez; lo que se cobra \"por cada\" unidad va multiplicado por la variable.",
            "Para b), reemplazá `k = 8` y `m = 5` y respetá el orden de operaciones (primero los productos).",
            "Para c), fijate qué término de la expresión cambia cuando `k` aumenta 3.",
        ],
        "solution": [
            "Fijo: `1800`. Kilómetros: `950 × k = 950k`. Espera: `200 × m = 200m`. Precio: `1800 + 950k + 200m`.",
            "Con `k = 8`, `m = 5`: `1800 + 950 × 8 + 200 × 5 = 1800 + 7600 + 1000 = 10 400`.",
            "Si `k` pasa a `k + 3`, solo cambia el término `950k`: aumenta `950 × 3 = 2850` (lo fijo y la espera no cambian).",
            "Control: con `k = 11`, `m = 5`: `1800 + 10 450 + 1000 = 13 250`, y `13 250 − 10 400 = 2850` ✓.",
            "Respuestas: `1800 + 950k + 200m`, $10 400 y $2850. Error típico: multiplicar la bajada de bandera por los km.",
        ],
    },
    {
        "id": "p-variables-expresiones-2",
        "node": "p-variables-expresiones",
        "kind": "problem",
        "level": 2,
        "title": "El alambrado del terreno",
        "statement": "Un terreno rectangular mide `(3x + 2)` metros de largo y `(x − 1)` metros de ancho, con `x > 1`. Se lo quiere rodear con alambrado.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la expresión simplificada del perímetro, en metros?",
                "check": {"type": "choice", "options": ["8x + 2", "4x + 1", "8x + 3", "8x + 6"], "correct": 0},
                "answer": "8x + 2",
            },
            {
                "prompt": "b) ¿Cuántos metros de alambrado hacen falta si x = 4.5? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 38, "tolerance": 0, "unit": "m"},
                "answer": "38 m",
            },
            {
                "prompt": "c) Si x aumenta 1, ¿cuántos metros más de alambrado hacen falta? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": "m"},
                "answer": "8 m",
            },
        ],
        "hints": [
            "Perímetro de un rectángulo: `2 × largo + 2 × ancho`. El 2 multiplica a TODO lo que está en cada paréntesis.",
            "Después de distribuir, juntá términos semejantes: las `x` con las `x` y los números con los números.",
            "Para c), compará la expresión con `x` y con `x + 1`: ¿qué término cambia?",
        ],
        "solution": [
            "`P = 2(3x + 2) + 2(x − 1) = 6x + 4 + 2x − 2`.",
            "Términos semejantes: `6x + 2x = 8x` y `4 − 2 = 2`. `P = 8x + 2`.",
            "Con `x = 4.5`: `P = 8 × 4.5 + 2 = 36 + 2 = 38 m`. Control con las medidas: largo `3 × 4.5 + 2 = 15.5`, ancho `4.5 − 1 = 3.5`, y `2 × 15.5 + 2 × 3.5 = 31 + 7 = 38` ✓.",
            "Si `x` pasa a `x + 1`: `8(x + 1) + 2 = 8x + 10`, que es 8 más que `8x + 2`. El coeficiente de `x` es lo que crece el perímetro por cada unidad de `x`.",
            "Respuestas: `8x + 2`, 38 m y 8 m. Errores típicos: `2(x − 1) = 2x − 1` (distribuir solo al primer término, da `8x + 3`) o `2(x − 1) = 2x + 2` (error de signo, da `8x + 6`).",
        ],
    },
    {
        "id": "p-variables-expresiones-3",
        "node": "p-variables-expresiones",
        "kind": "problem",
        "level": 3,
        "title": "Las cuentas de la fiesta del club",
        "statement": "Un club organiza una fiesta y llama `x` a la cantidad de pizzas que compra. Cada pizza cuesta **$8500**; compran el **doble** de botellas de bebida que de pizzas, a **$2200** cada botella; y pagan un alquiler fijo del salón de **$45 000**. Calculan **4 personas por pizza**, y cada persona paga una entrada de **$6000**. La ganancia `G` es lo recaudado menos lo gastado.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la expresión simplificada de G (en pesos)?",
                "check": {"type": "choice", "options": [
                    "G = 11 100x − 45 000",
                    "G = 11 100x + 45 000",
                    "G = 13 300x − 45 000",
                    "G = −6900x − 45 000",
                ], "correct": 0},
                "answer": "G = 11 100x − 45 000",
            },
            {
                "prompt": "b) ¿Cuál es la ganancia si compran 4 pizzas? Respondé solo con el número en pesos, con el signo incluido (sin puntos de miles).",
                "check": {"type": "numeric", "value": -600, "tolerance": 0, "unit": "$"},
                "answer": "−600 (pierden $600)",
            },
            {
                "prompt": "c) ¿Cuál es la menor cantidad de pizzas con la que el club NO pierde plata (G ≥ 0)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "pizzas"},
                "answer": "5 pizzas (ganancia de $10 500)",
            },
        ],
        "hints": [
            "Escribí por separado lo recaudado (personas × entrada, con personas = 4x) y lo gastado (pizzas + bebidas + alquiler).",
            "Al restar lo gastado, el signo menos afecta a TODO el paréntesis, incluido el alquiler.",
            "Para c), evaluá G en valores enteros de x alrededor de donde cambia de signo.",
        ],
        "solution": [
            "Recaudado: `4x` personas × `6000 = 24 000x`. Gastado: pizzas `8500x`, bebidas `2 × x × 2200 = 4400x`, alquiler `45 000`.",
            "`G = 24 000x − (8500x + 4400x + 45 000) = 24 000x − 8500x − 4400x − 45 000`.",
            "Términos semejantes: `24 000 − 8500 − 4400 = 11 100`. `G = 11 100x − 45 000`.",
            "Con `x = 4`: `G = 11 100 × 4 − 45 000 = 44 400 − 45 000 = −600`: pierden $600.",
            "Con `x = 5`: `G = 55 500 − 45 000 = 10 500 ≥ 0`. Como con 4 pizzas todavía hay pérdida (y con menos pizzas G es aún menor), el mínimo es 5.",
            "Respuestas: `G = 11 100x − 45 000`, −$600 y 5 pizzas. Errores típicos: no distribuir el menos al alquiler (`+45 000`) u olvidar el doble de botellas (`13 300x`).",
        ],
    },
]
