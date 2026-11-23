"""Pre-Algebra curriculum (12 units, #18-#29) adapted from Khan Academy Pre-Algebra.

Builds seamlessly on top of the 17 Arithmetic units without repeating basic
fraction/decimal/negative drills: factors & primes (GCD/LCM), data & averages,
measurement/area/volume, ratios/rates, percentages, roots & scientific notation,
variables & expressions, 1- & 2-step equations, inequalities, coordinate plane &
lines, functions, and 2x2 systems of equations.
"""

from __future__ import annotations

PREALGEBRA_NODES: list[dict] = [
    # ==================== NIVEL 6: DIVISIBILIDAD, DATOS Y MEDICIÓN ====================
    {
        "slug": "p-factores-multiplos",
        "title": "18. Factores, múltiplos, primos, MCD y mcm",
        "level": 6,
        "order_index": 18,
        "summary": "Divisibilidad rápida, números primos y factorización, MCD para repartir sin sobras y mcm para ciclos que coinciden.",
        "prerequisites": ["a-dividir-varios-digitos"],
        "metadata": {"section": "Preálgebra", "lab_tab": "mult_div", "est_minutes": 20},
        "items": [
            {
                "item_type": "recall",
                "title": "Identificar un número primo sin caer en trampas",
                "prompt": "¿Cuál de estos números es PRIMO (mayor que 1 y con exactamente dos divisores: 1 y él mismo)?",
                "answer": "29 es primo. 1 no se considera primo por definición, 21 = 3×7 y 27 = 3×9 son compuestos.",
                "hints": ["Probá dividir por 2, 3 y 5; recordá que el 1 no es primo."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["1", "21", "29", "27"],
                        "correct": 2,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "mcm en la vida real: colectivos que coinciden",
                "prompt": "El colectivo A pasa cada 12 minutos y el B cada 18 minutos. Si acaban de pasar juntos a las 8:00, ¿en cuántos minutos vuelven a coincidir (mcm de 12 y 18)? Respondé solo con el número en min.",
                "answer": "36 minutos: múltiplos de 18 → 18, 36 (y 36 = 12 × 3). Volverán a pasar juntos a las 8:36.",
                "hints": ["Buscá el primer múltiplo de 18 que también esté en la tabla del 12."],
                "payload": {"check": {"type": "numeric", "value": 36, "tolerance": 0, "unit": "min"}},
            },
            {
                "item_type": "worked_example",
                "title": "MCD en la vida real: cortar cables iguales sin desperdicio",
                "prompt": "Tenés un cable de 24 m y otro de 36 m y querés cortarlos en tramos del MISMO largo lo más largos posibles sin que sobre nada (MCD de 24 y 36). ¿Cuánto mide cada tramo? Respondé solo con el número en m.",
                "answer": "12 m: 12 divide tanto a 24 (2 tramos) como a 36 (3 tramos), y es el divisor común más grande.",
                "hints": ["¿Cuál es el número más grande que divide exactamente a 24 y a 36?"],
                "payload": {"check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": "m"}},
            },
            {
                "item_type": "recall",
                "title": "Regla rápida de divisibilidad por 3",
                "prompt": "Sin hacer la división larga, ¿cuál de estos números es divisible exactamente por 3?",
                "answer": "471 (4 + 7 + 1 = 12, que es múltiplo de 3). Sumar los dígitos revela al instante si un número se puede dividir por 3.",
                "hints": ["Sumá las cifras de cada número y fijate cuál da múltiplo de 3."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["412", "471", "523", "704"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Factorización prima de un número",
                "prompt": "Descomponiendo 60 en factores primos queda 2 × 2 × 3 × p. ¿Qué número primo es p? Respondé solo con el número.",
                "answer": "5: 2 × 2 = 4, 4 × 3 = 12, y 60 ÷ 12 = 5 (60 = 2² × 3 × 5).",
                "hints": ["Multiplicá 2 × 2 × 3 = 12 y fijate cuánto falta para llegar a 60."],
                "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Armar bolsitas idénticas con dos productos (MCD)",
                "prompt": "Tenés 18 alfajores y 30 caramelos y querés armar la MÁXIMA cantidad de bolsitas idénticas sin que sobre nada (MCD de 18 y 30). ¿Cuántas bolsitas podés armar? Respondé solo con el número.",
                "answer": "6 bolsitas (cada una con 3 alfajores y 5 caramelos).",
                "hints": ["Buscá el mayor divisor común de 18 y 30."],
                "payload": {"check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""}},
            },
        ],
    },
    {
        "slug": "p-patrones-datos",
        "title": "19. Patrones numéricos, promedios y lectura de datos",
        "level": 6,
        "order_index": 19,
        "summary": "Detectar reglas en sucesiones, calcular media, mediana y moda, y leer gráficos sin caer en engaños visuales.",
        "prerequisites": ["a-dividir-varios-digitos"],
        "metadata": {"section": "Preálgebra", "lab_tab": "place_value", "est_minutes": 18},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Promedio (media) de notas o gastos",
                "prompt": "Tus 4 facturas de luz fueron $20, $24, $28 y $32. ¿Cuál es el gasto promedio mensual (media)? Respondé solo con el número.",
                "answer": "26: sumás todos (20+24+28+32 = 104) y dividís por 4 → 104 ÷ 4 = 26.",
                "hints": ["Sumá los 4 valores y dividí por 4."],
                "payload": {"check": {"type": "numeric", "value": 26, "tolerance": 0.01, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Mediana con un valor extremo (sueldos)",
                "prompt": "En un taller chico los 5 sueldos ordenados son: $10, $12, $14, $14 y $100 (el dueño). ¿Cuál es la MEDIANA (el valor justo del medio)? Respondé solo con el número.",
                "answer": "14: con los datos ordenados, el del medio es $14 (mientras la media daría $30, un número engañoso que casi nadie cobra).",
                "hints": ["Ordená los 5 números y tomá el tercero (el del centro)."],
                "payload": {"check": {"type": "numeric", "value": 14, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Cuándo la mediana informa mejor que el promedio",
                "prompt": "Al analizar precios de casas o salarios en una ciudad donde unos pocos multimillonarios disparan los números, ¿qué medida describe mejor a la persona típica?",
                "answer": "La mediana: no se distorsiona cuando aparecen valores extremos altísimos (outliers), mientras que la media sí se dispara hacia arriba.",
                "hints": ["Pensá qué le pasa al promedio de ingresos de un bar si entra un multimillonario."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "La mediana, porque no se dispara por unos pocos valores extremos",
                            "La media (promedio), porque siempre representa a la mayoría",
                            "El rango (máximo menos mínimo)",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Detectar la regla de un patrón numérico",
                "prompt": "Un plan de entrenamiento suma minutos así cada semana: 15, 22, 29, 36… ¿Cuántos minutos tocan en la 5ª semana? Respondé solo con el número.",
                "answer": "43 minutos: el patrón suma +7 cada semana (36 + 7 = 43).",
                "hints": ["Restá dos términos vecinos para ver cuánto sube cada paso."],
                "payload": {"check": {"type": "numeric", "value": 43, "tolerance": 0, "unit": "min"}},
            },
            {
                "item_type": "worked_example",
                "title": "Hallar un dato faltante conociendo el promedio",
                "prompt": "En tus primeros 3 exámenes sacaste 7, 8 y 9 (suma = 24). ¿Cuánto necesitás sacar en el 4º examen para que tu promedio final sea exactamente 8? Respondé solo con el número.",
                "answer": "8: para promediar 8 en 4 exámenes necesitás sumar 8 × 4 = 32 puntos; como llevás 24, te faltan 32 − 24 = 8.",
                "hints": ["Promedio 8 en 4 notas exige una suma total de 32."],
                "payload": {"check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Trampa visual en gráficos de barras",
                "prompt": "Un gráfico en redes muestra dos barras: la barra B parece el TRIPLE de alta que la A, pero al mirar el eje vertical notás que arranca en 95 (A=96, B=98). ¿Qué está pasando?",
                "answer": "El eje vertical está truncado (no empieza en 0), exagerando visualmente una diferencia real de apenas ~2%.",
                "hints": ["Revisá siempre en qué número arranca el eje vertical de un gráfico."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "El eje vertical está cortado y no empieza en 0, exagerando una diferencia chica",
                            "B realmente es tres veces más grande que A",
                            "Los gráficos de barras siempre empiezan en el mínimo de los datos",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "p-medicion-geometria",
        "title": "20. Perímetro, área, volumen y conversión de unidades",
        "level": 6,
        "order_index": 20,
        "summary": "Perímetro para cercar, áreas de rectángulos/triángulos/círculos (πr²), volumen en litros y conversiones prácticas.",
        "prerequisites": ["a-multiplicar-dividir-decimales"],
        "metadata": {"section": "Preálgebra", "lab_tab": "mult_div", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Perímetro vs. Área en una habitación",
                "prompt": "Una habitación mide 5 m de largo por 4 m de ancho. ¿Cuántos metros de zócalo (perímetro) necesitás rodeando las 4 paredes? Respondé solo con el número en m.",
                "answer": "18 m: el perímetro es el contorno (5 + 4 + 5 + 4 = 18 m). El área del piso (para poner cerámica) sería 5 × 4 = 20 m².",
                "hints": ["Perímetro suma los 4 lados; área multiplica largo × ancho."],
                "payload": {"check": {"type": "numeric", "value": 18, "tolerance": 0, "unit": "m"}},
            },
            {
                "item_type": "worked_example",
                "title": "Área de un triángulo (vela o pared inclinada)",
                "prompt": "Un frente triangular tiene base b = 8 m y altura h = 5 m. ¿Cuál es su área (b × h ÷ 2)? Respondé solo con el número en m².",
                "answer": "20 m²: un triángulo siempre es la mitad de un rectángulo de igual base y altura → (8 × 5) / 2 = 20 m².",
                "hints": ["Base por altura dividido 2."],
                "payload": {"check": {"type": "numeric", "value": 20, "tolerance": 0.01, "unit": "m²"}},
            },
            {
                "item_type": "worked_example",
                "title": "Área de una pizza redonda (π · r²)",
                "prompt": "Una pizza redonda tiene radio r = 10 cm (diámetro 20 cm). Usando π ≈ 3.14, ¿cuántos cm² de pizza tiene (π · r²)? Respondé solo con el número en cm².",
                "answer": "314 cm² (3.14 × 10² = 3.14 × 100 = 314 cm²). Dato clave: una pizza de doble radio tiene 4 veces más comida (no el doble!).",
                "hints": ["Elevá el radio al cuadrado (10² = 100) y multiplicá por 3.14."],
                "payload": {"check": {"type": "numeric", "value": 314, "tolerance": 0.001, "unit": "cm²"}},
            },
            {
                "item_type": "worked_example",
                "title": "Volumen de una pecera en litros",
                "prompt": "Una pecera mide 50 cm de largo, 20 cm de ancho y 30 cm de alto (1 litro = 1000 cm³). ¿Cuántos litros de agua entran? Respondé solo con el número en L.",
                "answer": "30 litros: volumen = 50 × 20 × 30 = 30 000 cm³, y dividido 1000 cm³/L = 30 L.",
                "hints": ["Multiplicá las 3 dimensiones en cm y dividí por 1000."],
                "payload": {"check": {"type": "numeric", "value": 30, "tolerance": 0.01, "unit": "L"}},
            },
            {
                "item_type": "recall",
                "title": "Trampa de las pizzas: duplicar el diámetro",
                "prompt": "En una pizzería la pizza chica mide 20 cm de diámetro y la grande 40 cm (el doble de diámetro). ¿Cuánta más superficie de comida trae la grande?",
                "answer": "4 veces más superficie (no el doble): al duplicar el radio, r² se cuadruplica (2² = 4). Casi siempre conviene comprar una grande antes que dos chicas.",
                "hints": ["El área del círculo depende de r², no de r."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "El doble (×2)",
                            "4 veces más (×4), porque el radio está al cuadrado en πr²",
                            "3 veces más (×3)",
                        ],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Conversión de área: m² a cm²",
                "prompt": "Un cuadrado mide 1 m × 1 m (1 m²). Como 1 m = 100 cm, ¿cuántos cm² entran en 1 m²? Respondé solo con el número.",
                "answer": "10 000 cm² (100 cm × 100 cm = 10 000 cm²): en áreas el factor se eleva al cuadrado (NO es 100!).",
                "hints": ["Multiplicá 100 cm de ancho por 100 cm de alto."],
                "payload": {"check": {"type": "numeric", "value": 10000, "tolerance": 0, "unit": "cm²"}},
            },
        ],
    },
    # ==================== NIVEL 7: RAZONES, PROPORCIONES Y PORCENTAJES ====================
    {
        "slug": "p-razones-tasas",
        "title": "21. Razones, tasas unitarias y proporcionalidad",
        "level": 7,
        "order_index": 21,
        "summary": "Comparar precio por kilo/litro (tasa unitaria), escalas, recetas proporcionales y regla de tres directa vs. inversa.",
        "prerequisites": ["a-dividir-fracciones", "a-multiplicar-dividir-decimales"],
        "metadata": {"section": "Preálgebra", "lab_tab": "percentages", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Tasa unitaria en el supermercado (qué envase conviene)",
                "prompt": "El café A trae 250 g a $5000 y el café B trae 400 g a $7200. ¿Cuánto cuesta cada 100 g del café B? Respondé solo con el número.",
                "answer": "$1800 cada 100 g (7200 ÷ 4 = 1800), frente a $2000 cada 100 g del café A (5000 ÷ 2.5 = 2000). Conviene el café B.",
                "hints": ["400 g son 4 paquetes de 100 g: dividí 7200 por 4."],
                "payload": {
                    "lab_link": "math:percentages",
                    "check": {"type": "numeric", "value": 1800, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Regla de tres directa (receta para más invitados)",
                "prompt": "Una receta para 4 personas lleva 300 g de fideos. ¿Cuántos gramos necesitás para 6 personas? Respondé solo con el número en g.",
                "answer": "450 g: primero sacás por persona (300 ÷ 4 = 75 g/persona) y multiplicás por 6 → 75 × 6 = 450 g.",
                "hints": ["Calculá cuántos gramos son para 1 persona (o para 2) y escalá a 6."],
                "payload": {
                    "lab_link": "math:percentages",
                    "check": {"type": "numeric", "value": 450, "tolerance": 0, "unit": "g"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Proporcionalidad inversa (no todo es regla de tres directa)",
                "prompt": "3 pintores tardan 8 horas en pintar un departamento. Si se suman más y trabajan 6 pintores al mismo ritmo, ¿cuántas horas tardan? Respondé solo con el número en h.",
                "answer": "4 horas: al DOBLE de pintores les lleva la MITAD del tiempo (el trabajo total es constante: 3×8 = 24 horas-hombre → 24 ÷ 6 = 4 h).",
                "hints": ["Más pintores = MENOS tiempo (proporción inversa)."],
                "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0.01, "unit": "h"}},
            },
            {
                "item_type": "worked_example",
                "title": "Escala de un mapa o plano",
                "prompt": "En un mapa con escala 1 cm = 25 km, dos ciudades están separadas por 3.2 cm. ¿Cuál es la distancia real entre ellas? Respondé solo con el número en km.",
                "answer": "80 km (3.2 × 25 = 80 km).",
                "hints": ["Multiplicá 3.2 × 25."],
                "payload": {"check": {"type": "numeric", "value": 80, "tolerance": 0.01, "unit": "km"}},
            },
            {
                "item_type": "worked_example",
                "title": "Resolver una proporción a/b = c/d",
                "prompt": "Si un auto consume 7 litros cada 100 km, ¿cuántos litros necesita para un viaje de 350 km? Respondé solo con el número en L.",
                "answer": "24.5 L: 350 km son 3.5 veces 100 km → 7 × 3.5 = 24.5 L.",
                "hints": ["7 × 3.5."],
                "payload": {"check": {"type": "numeric", "value": 24.5, "tolerance": 0, "unit": "L"}},
            },
            {
                "item_type": "recall",
                "title": "Detectar si una situación es proporcionalidad directa o inversa",
                "prompt": "Viajás a una ciudad a 300 km: si duplicás tu velocidad promedio (de 50 km/h a 100 km/h), ¿qué pasa con el tiempo de viaje?",
                "answer": "Se reduce a la mitad (proporcionalidad inversa: de 6 h pasa a 3 h). En la directa ambas crecen juntas; en la inversa cuando una se multiplica por k, la otra se divide por k.",
                "hints": ["¿Ir más rápido te hace tardar más tiempo o menos tiempo?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Se reduce a la mitad (proporcionalidad inversa)",
                            "Se duplica también (proporcionalidad directa)",
                            "Queda igual",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "p-porcentajes",
        "title": "22. Porcentajes en la vida real: descuentos, IVA y aumentos",
        "level": 7,
        "order_index": 22,
        "summary": "Descomponer porcentajes mentalmente (10%, 5%, 25%), factores multiplicativos (×0.80, ×1.21) y la trampa de porcentajes sucesivos.",
        "prerequisites": ["p-razones-tasas"],
        "metadata": {"section": "Preálgebra", "lab_tab": "percentages", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Calcular 15% mentalmente (propina o descuento)",
                "prompt": "Una cena salió $240 (o $24 000 ÷ 100) y querés dejar el 15% de propina (10% + 5%). ¿Cuánto es el 15% de 240? Respondé solo con el número.",
                "answer": "36: 10% de 240 = 24; 5% es la mitad = 12 → 24 + 12 = 36.",
                "hints": ["10% es correr la coma un lugar (24), y 5% es la mitad (12)."],
                "payload": {
                    "lab_link": "math:percentages",
                    "check": {"type": "numeric", "value": 36, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Precio final con descuento en un solo paso",
                "prompt": "Una campera de $8000 tiene 20% de descuento en efectivo (pagás el 80%, o sea × 0.80). ¿Cuánto pagás? Respondé solo con el número.",
                "answer": "$6400 (8000 × 0.80 = 6400; o 8000 − 1600 = 6400).",
                "hints": ["Descontar 20% es multiplicar por 0.80."],
                "payload": {
                    "lab_link": "math:percentages",
                    "check": {"type": "numeric", "value": 6400, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Sumar IVA o recargo con factor multiplicativo",
                "prompt": "Un repuesto cuesta $500 más 21% de IVA (multiplicar por 1.21). ¿Cuál es el precio final? Respondé solo con el número.",
                "answer": "$605 (500 × 1.21 = 605; 21% de 500 = 5 × 21 = 105 → 500 + 105 = 605).",
                "hints": ["Sumar 21% equivale a multiplicar por 1.21."],
                "payload": {
                    "lab_link": "math:percentages",
                    "check": {"type": "numeric", "value": 605, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "La trampa del +20% seguido de −20%",
                "prompt": "Un producto vale $100. Primero sube 20% (llega a $120) y después le hacen 20% de descuento sobre el nuevo precio. ¿Cuánto termina valiendo? Respondé solo con el número.",
                "answer": "$96 (NO $100!): el segundo 20% se calcula sobre $120 (20% de 120 = $24 → 120 − 24 = $96). Los porcentajes siempre dependen de su base.",
                "hints": ["Calculá el 20% de 120 y restáselo a 120."],
                "payload": {
                    "lab_link": "math:percentages",
                    "check": {"type": "numeric", "value": 96, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Hallar el precio ORIGINAL antes de un descuento",
                "prompt": "Pagaste $60 por un libro que ya tenía 25% de descuento (es decir, $60 es el 75% = 3/4 del precio original). ¿Cuánto salía originalmente? Respondé solo con el número.",
                "answer": "$80: $60 ÷ 0.75 = $80 (si 3/4 vale 60, 1/4 vale 20 y 4/4 vale 80). Ojo: sumar 25% a 60 da $75, que es incorrecto!",
                "hints": ["Dividí el precio final por 0.75 (no le sumes 25% a 60)."],
                "payload": {"check": {"type": "numeric", "value": 80, "tolerance": 0.01, "unit": ""}},
            },
            {
                "item_type": "worked_example",
                "title": "Calcular el porcentaje de aumento",
                "prompt": "Un café pasó de $400 a $500 (subió $100 respecto a los $400 iniciales). ¿Qué porcentaje aumentó? Respondé solo con el número en %.",
                "answer": "25%: aumento ÷ valor inicial = 100 / 400 = 0.25 = 25%.",
                "hints": ["Dividí la diferencia (100) por el precio INICIAL (400)."],
                "payload": {"check": {"type": "numeric", "value": 25, "tolerance": 0.01, "unit": "%"}},
            },
        ],
    },
    # ==================== NIVEL 8: EXPONENTES, RAÍCES Y NOTACIÓN CIENTÍFICA ====================
    {
        "slug": "p-raices-notacion",
        "title": "23. Leyes de exponentes, raíces y notación científica",
        "level": 8,
        "order_index": 23,
        "summary": "Exponentes negativos (10⁻³), multiplicar/dividir potencias, raíces cuadradas y cúbicas, y notación científica.",
        "prerequisites": ["a-exponentes-potencias-10", "a-multiplicar-dividir-negativos"],
        "metadata": {"section": "Preálgebra", "lab_tab": "powers", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Multiplicar y dividir potencias de igual base",
                "prompt": "Simplificá 10⁵ × 10² ÷ 10⁴ = 10^k. ¿Cuánto vale el exponente k? Respondé solo con el número.",
                "answer": "3 (5 + 2 − 4 = 3 → 10³ = 1000). Al multiplicar sumás exponentes; al dividir los restás.",
                "hints": ["Sumá 5 + 2 y restale 4."],
                "payload": {
                    "lab_link": "math:powers",
                    "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Exponente negativo (miliamperios y decimales chicos)",
                "prompt": "Un sensor consume 5 × 10⁻³ A (5 mA). Escribí 5 × 10⁻³ como número decimal normal.",
                "answer": "0.005: el exponente −3 significa dividir por 10³ (1000), corriendo la coma 3 lugares a la izquierda. ¡Nunca hace negativo al número!",
                "hints": ["Corré la coma de 5.0 tres lugares hacia la izquierda."],
                "payload": {
                    "lab_link": "math:powers",
                    "check": {"type": "numeric", "value": 0.005, "tolerance": 0.0005, "unit": "A"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Raíz cuadrada como inversa de elevar al cuadrado",
                "prompt": "Una habitación cuadrada tiene 81 m² de superficie. ¿Cuántos metros mide cada pared (√81)? Respondé solo con el número en m.",
                "answer": "9 m (porque 9 × 9 = 81).",
                "hints": ["¿Qué número multiplicado por sí mismo da 81?"],
                "payload": {"check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": "m"}},
            },
            {
                "item_type": "worked_example",
                "title": "Raíz cúbica en un cubo 3D",
                "prompt": "Un tanque cúbico tiene 27 m³ de volumen (lado × lado × lado = 27). ¿Cuánto mide su arista (∛27)? Respondé solo con el número en m.",
                "answer": "3 m (3 × 3 × 3 = 27).",
                "hints": ["¿Qué número multiplicado 3 veces por sí mismo da 27?"],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": "m"}},
            },
            {
                "item_type": "recall",
                "title": "Escribir un número en notación científica válida",
                "prompt": "La distancia a la Luna es ~384 000 km. ¿Cómo se escribe correctamente en notación científica (un solo dígito 1–9 antes de la coma)?",
                "answer": "3.84 × 10⁵ km: corrés la coma 5 lugares a la izquierda para dejar el 3 adelante.",
                "hints": ["La mantisa debe quedar entre 1 y 10 (3.84), y contá los lugares corridos."],
                "payload": {
                    "lab_link": "math:powers",
                    "check": {
                        "type": "choice",
                        "options": ["38.4 × 10⁴", "3.84 × 10⁵", "0.384 × 10⁶"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Qué significa un exponente negativo (no es un número negativo)",
                "prompt": "¿Cuánto vale 2⁻³?",
                "answer": "1/8 (positivo!): un exponente negativo da vuelta el número a fracción (1 / 2³ = 1/8 = 0.125), jamás cambia el signo a −8.",
                "hints": ["a⁻ⁿ = 1 / aⁿ."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["−6", "−8", "1/8 (= 0.125)"],
                        "correct": 2,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 9: VARIABLES, ECUACIONES Y DESIGUALDADES ====================
    {
        "slug": "p-variables-expresiones",
        "title": "24. Variables, expresiones algebraicas y términos semejantes",
        "level": 9,
        "order_index": 24,
        "summary": "Pasar de números fijos a letras (variables), traducir frases reales a álgebra, agrupar términos y distribuir.",
        "prerequisites": ["a-multiplicar-dividir-negativos"],
        "metadata": {"section": "Preálgebra", "lab_tab": "linear_eq", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Evaluar una expresión (costo de un taxi)",
                "prompt": "Un viaje cuesta 500 + 80x (donde x son los kilómetros recorridos). ¿Cuánto pagás por un viaje de x = 6 km? Respondé solo con el número.",
                "answer": "$980: reemplazás x por 6 → 500 + 80×6 = 500 + 480 = 980.",
                "hints": ["Multiplicá 80 × 6 primero y después sumá 500."],
                "payload": {
                    "lab_link": "math:linear_eq",
                    "check": {"type": "numeric", "value": 980, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Traducir una frase cotidiana a expresión algebraica",
                "prompt": "Compro x empanadas a $1200 cada una y pago $1500 fijos de envío. ¿Qué expresión representa el total a pagar?",
                "answer": "1200x + 1500: el precio por empanada multiplica a x y el envío se suma una sola vez.",
                "hints": ["¿Cuál de los dos costos depende de cuántas empanadas comprás?"],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["1200x + 1500", "1500x + 1200", "2700x"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Combinar términos semejantes",
                "prompt": "¿A qué equivale simplificar 5x + 3 − 2x + 7?",
                "answer": "3x + 10: juntás las x con las x (5x − 2x = 3x) y los números sueltos con los números sueltos (3 + 7 = 10). No podés mezclar 3x con 10.",
                "hints": ["Sumá manzanas con manzanas (x) y números sueltos aparte."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["3x + 10", "13x", "7x + 10"],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Propiedad distributiva con variables",
                "prompt": "¿Cuál es la forma expandida correcta de 4(2x − 5)?",
                "answer": "8x − 20: el 4 de afuera multiplica a TODOS los términos de adentro (4·2x = 8x y 4·(−5) = −20).",
                "hints": ["Acordate de multiplicar el 4 también por el −5."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["8x − 5", "8x − 20", "6x − 9"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Evaluar con número negativo",
                "prompt": "Evaluá 2x − 9 cuando x = −3. Incluí el signo.",
                "answer": "−15: 2 · (−3) − 9 = −6 − 9 = −15.",
                "hints": ["Primero 2 × (−3) = −6, después restale 9."],
                "payload": {"check": {"type": "numeric", "value": -15, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "Por qué 3x + 4 NO es 7x",
                "prompt": "¿Por qué no se puede simplificar 3x + 4 escribiendo 7x?",
                "answer": "Porque 3x significa 'tres veces x' y 4 son 4 unidades sueltas: si x = 10, 3(10)+4 = 34, mientras que 7(10) = 70. Solo se suman términos con la misma variable y exponente.",
                "hints": ["Probá poner x = 10 en las dos expresiones y compará."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Porque no son términos semejantes (con x=10, 3x+4=34 pero 7x=70)",
                            "Sí se puede si x es un número entero",
                            "Porque primero hay que multiplicar 3 por 4",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "p-ecuaciones-un-paso",
        "title": "25. Ecuaciones de uno y dos pasos (la balanza)",
        "level": 9,
        "order_index": 25,
        "summary": "Mantener la igualdad equilibrada aplicando operaciones inversas a ambos lados, ecuaciones con paréntesis y verificación.",
        "prerequisites": ["p-variables-expresiones"],
        "metadata": {"section": "Preálgebra", "lab_tab": "linear_eq", "est_minutes": 20},
        "items": [
            {
                "item_type": "worked_example",
                "title": "Ecuación de 1 paso: cuánto te falta ahorrar",
                "prompt": "Tenés $350 y querés juntar $920: 350 + x = 920. ¿Cuánto vale x? Respondé solo con el número.",
                "answer": "570: restás 350 en ambos lados → x = 920 − 350 = 570.",
                "hints": ["Deshacé el +350 restando 350 a ambos lados."],
                "payload": {
                    "lab_link": "math:linear_eq",
                    "check": {"type": "numeric", "value": 570, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ecuación de 2 pasos (modelo clásico de balanza)",
                "prompt": "Resolvé 3x − 7 = 14. ¿Cuánto vale x? Respondé solo con el número.",
                "answer": "7: sumás 7 a ambos lados → 3x = 21; dividís por 3 → x = 7. Comprobación: 3(7) − 7 = 14.",
                "hints": ["Primero deshacé el −7 sumando 7; al final dividí por 3."],
                "payload": {
                    "lab_link": "math:linear_eq",
                    "check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Problema real: calcular horas de un técnico",
                "prompt": "Un técnico cobra $40 de visita fija más $25 por hora, y la factura total fue $140 (40 + 25h = 140). ¿Cuántas horas trabajó? Respondé solo con el número.",
                "answer": "4 horas: 25h = 140 − 40 = 100 → h = 100 ÷ 25 = 4 h.",
                "hints": ["Restá la visita fija de $40 y dividí el resto por $25."],
                "payload": {
                    "lab_link": "math:linear_eq",
                    "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "h"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ecuación con paréntesis (distribuir o dividir primero)",
                "prompt": "Resolvé 2(x + 5) = 24. ¿Cuánto vale x? Respondé solo con el número.",
                "answer": "7: podés dividir ambos lados por 2 (x + 5 = 12 → x = 7) o distribuir (2x + 10 = 24 → 2x = 14 → x = 7).",
                "hints": ["Dividí los dos lados por 2 para sacar el paréntesis de un golpe."],
                "payload": {
                    "lab_link": "math:linear_eq",
                    "check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Ecuación con x en ambos lados",
                "prompt": "Resolvé 5x − 4 = 2x + 11. ¿Cuánto vale x? Respondé solo con el número.",
                "answer": "5: restá 2x en ambos lados (3x − 4 = 11), sumá 4 (3x = 15), dividí por 3 → x = 5.",
                "hints": ["Juntá las x de un lado y los números del otro."],
                "payload": {
                    "lab_link": "math:linear_eq",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Orden para despejar 4x + 5 = 29",
                "prompt": "Ordená los pasos para despejar x y comprobar la solución.",
                "answer": "1) Restar 5 a ambos lados (4x = 24) → 2) Dividir ambos lados por 4 (x = 6) → 3) Verificar sustituyendo 4(6) + 5 = 29.",
                "hints": ["Deshacés las operaciones en orden inverso a PEMDAS."],
                "payload": {
                    "lab_link": "math:linear_eq",
                    "check": {
                        "type": "order",
                        "lines": [
                            "Restar 5 en ambos lados para obtener 4x = 24",
                            "Dividir ambos lados por 4 para hallar x = 6",
                            "Comprobar reemplazando en la original: 4(6) + 5 = 29",
                        ],
                    },
                },
            },
        ],
    },
    {
        "slug": "p-desigualdades",
        "title": "26. Desigualdades (<, >, ≤, ≥) y topes reales",
        "level": 9,
        "order_index": 26,
        "summary": "Modelar presupuestos, límites de peso y metas ('al menos', 'como máximo') y la regla de invertir el signo al dividir por negativo.",
        "prerequisites": ["p-ecuaciones-un-paso"],
        "metadata": {"section": "Preálgebra", "lab_tab": "linear_eq", "est_minutes": 18},
        "items": [
            {
                "item_type": "recall",
                "title": "Traducir 'como máximo' y 'al menos'",
                "prompt": "Un ascensor soporta 'como máximo 400 kg' y un juego pide 'al menos 18 años'. ¿Qué símbolos corresponden?",
                "answer": "Como máximo 400 kg → peso ≤ 400 (incluye 400). Al menos 18 años → edad ≥ 18 (incluye 18).",
                "hints": ["Cuando el límite SÍ está permitido, lleva la rayita de igual abajo (≤ o ≥)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "peso ≤ 400  y  edad ≥ 18",
                            "peso < 400  y  edad > 18",
                            "peso ≥ 400  y  edad ≤ 18",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Tope de presupuesto mensual",
                "prompt": "Tenés como máximo $50 en total para pagar $14 de envío más libros de $12 cada uno (12x + 14 ≤ 50). ¿Cuántos libros como MÁXIMO podés comprar? Respondé solo con el número.",
                "answer": "3 libros: 12x ≤ 36 → x ≤ 3.",
                "hints": ["Restá 14 a 50 y dividí por 12."],
                "payload": {"check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""}},
            },
            {
                "item_type": "recall",
                "title": "La regla de oro al multiplicar o dividir por un negativo",
                "prompt": "Tenés la desigualdad −2x > 10 y dividís ambos lados por −2. ¿Cómo queda?",
                "answer": "x < −5: al multiplicar o dividir por un número NEGATIVO, el signo de desigualdad SIEMPRE se da vuelta. Probalo con x = −6: −2(−6) = +12 > 10 (verdadero!).",
                "hints": ["Probá con un ejemplo simple: 2 < 5, pero si multiplicás por −1 queda −2 > −5."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["x > −5", "x < −5", "x > 5"],
                        "correct": 1,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Círculo abierto vs. cerrado en la recta numérica",
                "prompt": "Al graficar x ≥ 4 en una recta numérica, ¿cómo se dibuja el punto sobre el 4?",
                "answer": "Círculo relleno (cerrado) en el 4 con flecha hacia la derecha: el relleno indica que el 4 SÍ está incluido en la solución.",
                "hints": ["Relleno = incluye el borde (≤, ≥); hueco = no lo incluye (<, >)."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Círculo relleno en 4 y flecha hacia la derecha",
                            "Círculo hueco en 4 y flecha hacia la derecha",
                            "Círculo relleno en 4 y flecha hacia la izquierda",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Meta mínima de ahorro semanal",
                "prompt": "Querés juntar al menos $200. Ya tenés $60 y ahorrás $20 por semana (60 + 20s ≥ 200). ¿Cuál es el MÍNIMO de semanas necesarias? Respondé solo con el número.",
                "answer": "7 semanas: 20s ≥ 140 → s ≥ 7.",
                "hints": ["Restá 60 a 200 y dividí por 20."],
                "payload": {"check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": "semanas"}},
            },
            {
                "item_type": "recall",
                "title": "Comprobar si un número cumple una desigualdad",
                "prompt": "¿Cuál de estos valores NO cumple 3x − 1 < 11?",
                "answer": "x = 4 (porque 3(4) − 1 = 11, y 11 NO es estrictamente menor que 11). Para x = 3 da 8 < 11, que sí cumple.",
                "hints": ["Reemplazá cada opción y recordá que '<' exige ser estrictamente menor."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": ["x = 0", "x = 3", "x = 4", "x = −2"],
                        "correct": 2,
                    },
                },
            },
        ],
    },
    # ==================== NIVEL 10: PLANO, RECTAS, FUNCIONES Y SISTEMAS ====================
    {
        "slug": "p-plano-rectas",
        "title": "27. Plano cartesiano, pendiente y rectas (y = mx + b)",
        "level": 10,
        "order_index": 27,
        "summary": "Coordenadas (x, y), pendiente m = Δy/Δx como tasa de cambio real, ordenada al origen b y graficar rectas.",
        "prerequisites": ["p-ecuaciones-un-paso"],
        "metadata": {"section": "Preálgebra", "lab_tab": "linear_fn", "est_minutes": 20},
        "items": [
            {
                "item_type": "recall",
                "title": "Orden de las coordenadas (x, y)",
                "prompt": "Para ubicar el punto (−3, 4) en el plano cartesiano partiendo del origen (0, 0), ¿cómo te movés?",
                "answer": "3 unidades a la IZQUIERDA (eje x negativo) y 4 unidades hacia ARRIBA (eje y positivo): siempre horizontal primero, vertical después.",
                "hints": ["Primera cifra = eje X (izquierda/derecha); segunda = eje Y (arriba/abajo)."],
                "payload": {
                    "lab_link": "math:linear_fn",
                    "check": {
                        "type": "choice",
                        "options": [
                            "3 a la izquierda y 4 hacia arriba",
                            "3 hacia abajo y 4 a la derecha",
                            "4 a la izquierda y 3 hacia arriba",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Calcular la pendiente m entre dos puntos",
                "prompt": "Una recta pasa por (1, 3) y (5, 11). ¿Cuál es su pendiente m = (y₂ − y₁) / (x₂ − x₁)? Respondé solo con el número.",
                "answer": "2: sube Δy = 11 − 3 = 8 mientras avanza Δx = 5 − 1 = 4 → m = 8 / 4 = 2.",
                "hints": ["Cambio vertical dividido cambio horizontal."],
                "payload": {
                    "lab_link": "math:linear_fn",
                    "check": {"type": "numeric", "value": 2, "tolerance": 0.01, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Significado real de m y b en y = mx + b",
                "prompt": "Un remis cobra y = 150x + 800 (donde x son kilómetros e y es el precio). ¿Qué representan 150 y 800?",
                "answer": "150 (la pendiente m) es el precio por cada kilómetro adicional; 800 (la ordenada b) es la bajada de bandera fija cuando x = 0 km.",
                "hints": ["Poné x = 0 para ver qué es b, y mirá cuánto sube el precio al sumar 1 km."],
                "payload": {
                    "lab_link": "math:linear_fn",
                    "check": {
                        "type": "choice",
                        "options": [
                            "150 = costo por km (pendiente); 800 = tarifa fija inicial (ordenada al origen)",
                            "800 = costo por km; 150 = tarifa fija inicial",
                            "150 = máximo de kilómetros; 800 = total del viaje",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Pendiente negativa: batería descargándose",
                "prompt": "Un celular arranca al 100% (x = 0 h) y a las 4 horas está al 40% (x = 4 h). ¿Cuántos puntos porcentuales cambia por hora (pendiente m)? Incluí el signo negativo.",
                "answer": "−15 (% por hora): Δy / Δx = (40 − 100) / (4 − 0) = −60 / 4 = −15. Pendiente negativa = la recta baja de izquierda a derecha.",
                "hints": ["(40 − 100) ÷ 4."],
                "payload": {
                    "lab_link": "math:linear_fn",
                    "check": {"type": "numeric", "value": -15, "tolerance": 0.01, "unit": "%/h"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Evaluar una recta en un punto",
                "prompt": "Dada la recta y = 3x − 2, ¿cuánto vale y cuando x = 4? Respondé solo con el número.",
                "answer": "10 (3 · 4 − 2 = 12 − 2 = 10).",
                "hints": ["Reemplazá x por 4."],
                "payload": {
                    "lab_link": "math:linear_fn",
                    "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Rectas paralelas",
                "prompt": "¿Cuándo son paralelas dos rectas (nunca se cruzan) en el plano cartesiano?",
                "answer": "Cuando tienen exactamente la MISMA pendiente m pero distinta ordenada al origen b (ej. y = 2x + 1 e y = 2x + 5).",
                "hints": ["Misma inclinación, distinto punto de partida."],
                "payload": {
                    "lab_link": "math:linear_fn",
                    "check": {
                        "type": "choice",
                        "options": [
                            "Cuando tienen la misma pendiente m y distinta ordenada b",
                            "Cuando tienen la misma ordenada b y distinta pendiente m",
                            "Cuando sus pendientes suman 0",
                        ],
                        "correct": 0,
                    },
                },
            },
        ],
    },
    {
        "slug": "p-funciones",
        "title": "28. Introducción a funciones: entradas, salidas y modelos",
        "level": 10,
        "order_index": 28,
        "summary": "Qué es una función f(x), prueba de la línea vertical, tablas de entrada/salida y distinguir modelos lineales de no lineales.",
        "prerequisites": ["p-plano-rectas"],
        "metadata": {"section": "Preálgebra", "lab_tab": "linear_fn", "est_minutes": 18},
        "items": [
            {
                "item_type": "recall",
                "title": "Qué define a una función (regla de entrada → salida)",
                "prompt": "¿Qué condición debe cumplir una relación para ser una FUNCIÓN matemática?",
                "answer": "A cada entrada x le corresponde UNA ÚNICA salida f(x). (Dos entradas distintas sí pueden dar la misma salida, como una máquina expendedora donde dos botones dan agua, pero un mismo botón no puede dar dos cosas distintas a la vez).",
                "hints": ["Pensá en una máquina: misma entrada → siempre una sola salida predecible."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Cada entrada x produce exactamente una única salida f(x)",
                            "Cada salida debe venir de una entrada diferente",
                            "Su gráfica siempre tiene que ser una línea recta",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Notación de función f(x)",
                "prompt": "Si el costo de imprimir x fotos es f(x) = 4x + 10, ¿cuánto vale f(7)? Respondé solo con el número.",
                "answer": "38: f(7) significa 'evaluá la regla f cuando la entrada es 7' → 4(7) + 10 = 38. (¡f(7) NO significa f multiplicado por 7!).",
                "hints": ["Sustituí x = 7 dentro de 4x + 10."],
                "payload": {
                    "lab_link": "math:linear_fn",
                    "check": {"type": "numeric", "value": 38, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Hallar la entrada x dada la salida f(x)",
                "prompt": "Para f(x) = 5x − 3, ¿qué entrada x produce la salida f(x) = 22? Respondé solo con el número.",
                "answer": "5: planteás 5x − 3 = 22 → 5x = 25 → x = 5.",
                "hints": ["Igualá 5x − 3 = 22 y despejá x."],
                "payload": {
                    "lab_link": "math:linear_fn",
                    "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Distinguir función lineal vs. no lineal en una tabla",
                "prompt": "Tabla A: (0,2), (1,5), (2,8), (3,11). Tabla B: (0,1), (1,2), (2,4), (3,8). ¿Cuál es LINEAL y por qué?",
                "answer": "La Tabla A es lineal porque suma siempre una tasa constante (+3 por cada +1 en x). La Tabla B se duplica cada paso (exponencial, curva).",
                "hints": ["En una función lineal el salto en y es siempre igual cuando x avanza de a 1."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Tabla A: suma siempre +3 por cada paso (tasa constante)",
                            "Tabla B: porque multiplica por 2 en cada paso",
                            "Las dos son lineales porque siguen un patrón regular",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "recall",
                "title": "Prueba de la línea vertical en un gráfico",
                "prompt": "Si trazás una línea vertical sobre un gráfico y corta la curva en DOS puntos distintos, ¿qué te indica?",
                "answer": "Que NO es una función: para un mismo valor de entrada x habría dos salidas y distintas a la vez.",
                "hints": ["Un mismo x tendría dos valores de y distintos."],
                "payload": {
                    "check": {
                        "type": "choice",
                        "options": [
                            "Que NO es una función (una misma entrada x da dos salidas)",
                            "Que es una función cuadrática",
                            "Que la función tiene pendiente cero",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Comparar tasas de cambio de dos servicios",
                "prompt": "Plan A: f(x) = 12x + 50. Plan B: pasa por (0, 20) y (5, 95). ¿Cuánto cuesta cada unidad extra en el Plan B (su pendiente)? Respondé solo con el número.",
                "answer": "15 por unidad: (95 − 20) / (5 − 0) = 75 / 5 = 15 (crece más rápido que los 12 del Plan A).",
                "hints": ["Calculá (95 − 20) ÷ 5."],
                "payload": {"check": {"type": "numeric", "value": 15, "tolerance": 0.01, "unit": ""}},
            },
        ],
    },
    {
        "slug": "p-sistemas-ecuaciones",
        "title": "29. Sistemas de ecuaciones 2×2 (dos condiciones a la vez)",
        "level": 10,
        "order_index": 29,
        "summary": "Cuándo empatan dos tarifas o planes, punto de cruce gráfico, método de sustitución y método de eliminación.",
        "prerequisites": ["p-funciones"],
        "metadata": {"section": "Preálgebra", "lab_tab": "systems", "est_minutes": 22},
        "items": [
            {
                "item_type": "recall",
                "title": "Qué significa gráficamente resolver un sistema 2×2",
                "prompt": "Graficás el costo del Plan A y el del Plan B en el mismo plano cartesiano. ¿Qué representa el punto (x, y) donde se cruzan las dos rectas?",
                "answer": "El único par (x, y) que cumple AMBAS ecuaciones a la vez: la cantidad x en la que los dos planes salen exactamente lo mismo.",
                "hints": ["Probalo en el Graficador dual del Laboratorio de Matemáticas."],
                "payload": {
                    "lab_link": "math:systems",
                    "check": {
                        "type": "choice",
                        "options": [
                            "El punto exacto (x, y) que satisface las dos ecuaciones al mismo tiempo",
                            "El promedio de las dos pendientes",
                            "El punto donde x vale siempre cero",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "worked_example",
                "title": "Elegir entre dos planes de gimnasio (sustitución)",
                "prompt": "Gimnasio A cobra $30 fijo + $5 por clase (y = 5x + 30). Gimnasio B cobra $10 por clase sin matrícula (y = 10x). ¿A partir de cuántas clases empatan en precio (5x + 30 = 10x)? Respondé solo con el número.",
                "answer": "6 clases: 30 = 5x → x = 6 (ambos salen $60). Menos de 6 clases conviene el B; más de 6 conviene el A.",
                "hints": ["Igualá 5x + 30 = 10x y despejá x."],
                "payload": {
                    "lab_link": "math:systems",
                    "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": "clases"},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Método de eliminación (sumar ecuaciones)",
                "prompt": "Dos números suman 14 (x + y = 14) y su diferencia es 4 (x − y = 4). Sumando ambas ecuaciones, ¿cuánto vale el número mayor x? Respondé solo con el número.",
                "answer": "9: al sumar (+y y −y se cancelan) queda 2x = 18 → x = 9 (y el otro número es y = 5).",
                "hints": ["Sumá lado izquierdo con izquierdo y derecho con derecho: 2x = 18."],
                "payload": {
                    "lab_link": "math:systems",
                    "check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "worked_example",
                "title": "Problema real de entradas (adultos y niños)",
                "prompt": "Compraste 10 entradas en total (a + n = 10). Las de adulto salen $10 y las de niño $6, gastando $84 (10a + 6n = 84). ¿Cuántas entradas de adulto (a) compraste? Respondé solo con el número.",
                "answer": "6 de adulto (y 4 de niño): reemplazás n = 10 − a → 10a + 6(10 − a) = 84 → 4a + 60 = 84 → 4a = 24 → a = 6.",
                "hints": ["Sustituí n = 10 − a en la ecuación del precio."],
                "payload": {
                    "lab_link": "math:systems",
                    "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""},
                },
            },
            {
                "item_type": "recall",
                "title": "Cuándo un sistema 2×2 NO tiene solución",
                "prompt": "Intentás resolver el sistema y = 2x + 3  e  y = 2x + 8. ¿Cuántas soluciones tiene?",
                "answer": "Ninguna (0 soluciones): son dos rectas paralelas (misma pendiente 2, distinta ordenada), así que jamás se cruzan.",
                "hints": ["¿Puede 2x + 3 ser igual a 2x + 8 para algún x?"],
                "payload": {
                    "lab_link": "math:systems",
                    "check": {
                        "type": "choice",
                        "options": [
                            "Ninguna: son rectas paralelas que nunca se cruzan",
                            "Una sola solución en x = 0",
                            "Infinitas soluciones",
                        ],
                        "correct": 0,
                    },
                },
            },
            {
                "item_type": "drill",
                "title": "Práctica en el Laboratorio de Matemáticas: Sistemas 2×2",
                "prompt": "Abrí el Laboratorio de Matemáticas en 'Sistemas 2×2', probá mover dos rectas en el Graficador dual y resolvé 5 ejercicios.",
                "answer": "Tu precisión del Laboratorio queda registrada para sugerir la calificación de esta tarjeta.",
                "hints": ["Al sumar x + y y x − y, las y se cancelan de inmediato."],
                "payload": {
                    "lab_link": "math:systems",
                    "lab_metric": {"type": "math_accuracy", "good": 80, "easy": 95, "unit": "%"},
                },
            },
        ],
    },
]


PREALGEBRA_LESSONS: dict[str, dict] = {
    "p-factores-multiplos": {
        "hook": {
            "question": "Si el colectivo A pasa cada `12` minutos y el B cada `18` minutos, y acaban de salir juntos, ¿en cuántos minutos exactos vuelven a coincidir?",
            "intuition": "En `36` minutos (el **mínimo común múltiplo**). Entender factores, números primos, MCD y mcm te da las herramientas para simplificar fracciones, sincronizar ciclos y repartir materiales sin desperdiciar nada.",
        },
        "concept": {
            "points": [
                "**Factores vs. Múltiplos**: los **factores** (divisores) de 12 son los números chicos que lo dividen justo (`1, 2, 3, 4, 6, 12`). Los **múltiplos** son su tabla (`12, 24, 36, 48…`).",
                "**Números primos**: mayores que `1` que solo se dividen por `1` y por sí mismos (`2, 3, 5, 7, 11, 13…`). Todo número compuesto se desarma de forma única en primos (como ladrillos LEGO: `60 = 2 × 2 × 3 × 5`).",
                "**Atajos de divisibilidad**: por `2` (termina en par), por `3` (la suma de dígitos es múltiplo de 3), por `5` (termina en 0 o 5), por `10` (termina en 0).",
                "**MCD vs. mcm**: el **MCD** (máximo común divisor) sirve para **repartir o cortar** en trozos máximos sin sobras y simplificar fracciones. El **mcm** (mínimo común múltiplo) sirve para **coincidencias de ciclos** y denominadores comunes.",
            ],
            "real_world": [
                {
                    "title": "Colectivos o alarmas que coinciden (mcm)",
                    "detail": "Ciclos de 12 min y 18 min vuelven a alinearse exactamente cada `mcm(12, 18) = 36` min.",
                },
                {
                    "title": "Cortar cables o maderas sin sobras (MCD)",
                    "detail": "Un rollo de 24 m y otro de 36 m se cortan en piezas iguales máximas de `MCD(24, 36) = 12 m`.",
                },
                {
                    "title": "Criptografía de internet (números primos)",
                    "detail": "Multiplicar dos primos gigantes es fácil, pero factorizar el resultado al revés es tan difícil que protege tus claves bancarias (RSA).",
                },
            ],
            "key_rule": "Primos = bloques base (el `1` no es primo) · **MCD** corta/reparte sin sobras · **mcm** sincroniza ciclos.",
            "pitfall": "Confundir MCD con mcm: recordá que el MCD siempre es **menor o igual** a tus números, y el mcm siempre es **mayor o igual**.",
        },
        "example": {
            "title": "Sacá MCD y mcm de `12` y `18` con sus bloques primos",
            "steps": [
                "Factorizamos en primos: `12 = 2 × 2 × 3` y `18 = 2 × 3 × 3`.",
                "**MCD** (lo que comparten ambos): comparten un `2` y un `3` → `2 × 3 = 6`.",
                "**mcm** (juntando lo máximo de cada primo para contener a ambos): dos `2` y dos `3` → `2 × 2 × 3 × 3 = 36`.",
            ],
            "lab_link": "math:mult_div",
            "lab_cta": "Practicar multiplicación y división en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál de estos números es un número PRIMO?",
            "options": [
                {"text": "1", "ok": False, "feedback": "Por definición los primos tienen exactamente dos divisores distintos (1 y sí mismo); el 1 solo tiene uno."},
                {"text": "15", "ok": False, "feedback": "15 = 3 × 5, es compuesto."},
                {"text": "17", "ok": True, "feedback": "Exacto: solo se divide exactamente por 1 y por 17."},
            ],
        },
        "checks": [
            {
                "question": "Una luz parpadea cada 4 s y otra cada 6 s. Si parpadean juntas ahora, ¿cada cuántos segundos vuelven a coincidir?",
                "options": [
                    {"text": "Cada 2 s", "ok": False, "feedback": "2 es el MCD (divisor), no el múltiplo común en el que coinciden."},
                    {"text": "Cada 12 s", "ok": True, "feedback": "Exacto: mcm(4, 6) = 12 s."},
                    {"text": "Cada 24 s", "ok": False, "feedback": "A los 24 s coinciden por segunda vez; la primera vez es a los 12 s."},
                ],
            },
            {
                "question": "¿Qué número grande es divisible por 3 usando la regla de sumar sus cifras?",
                "options": [
                    {"text": "234", "ok": True, "feedback": "Exacto: 2 + 3 + 4 = 9, que es múltiplo de 3 (234 ÷ 3 = 78)."},
                    {"text": "235", "ok": False, "feedback": "2 + 3 + 5 = 10, no está en la tabla del 3."},
                    {"text": "104", "ok": False, "feedback": "1 + 0 + 4 = 5, no es múltiplo de 3."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con un ejemplo propio la diferencia entre usar el MCD y usar el mcm.",
    },
    "p-patrones-datos": {
        "hook": {
            "question": "Si en una habitación hay 4 personas que ganan `$10` y entra una persona que gana `$1000`, el promedio salta a `$208`. ¿Ese promedio describe bien a la gente de la sala?",
            "intuition": "Para nada: nadie gana cerca de `$208`. Por eso en lectura de datos no alcanza con el promedio (**media**); también miramos la **mediana** (el valor del medio) y revisamos si los ejes de un gráfico están trucados.",
        },
        "concept": {
            "points": [
                "**Media (promedio)**: sumás todos los valores y dividís por cuántos son. Funciona genial cuando los datos son parejos, pero un solo extremo la distorsiona.",
                "**Mediana**: ordenás los datos de menor a mayor y tomás el **del centro** (si hay cantidad par, promediás los dos del centro). Resiste valores extremos.",
                "**Moda y rango**: la **moda** es el valor que más se repite; el **rango** (`máximo − mínimo`) dice qué tan dispersos están los datos.",
                "**Leer gráficos con ojo crítico**: mirá siempre las etiquetas y **dónde arranca el eje vertical**. Un eje cortado que no empieza en `0` hace parecer gigantes diferencias minúsculas.",
            ],
            "real_world": [
                {
                    "title": "Salarios y precios de viviendas",
                    "detail": "Los informes económicos serios usan la **mediana** salarial porque unos pocos ingresos altísimos inflan el promedio.",
                },
                {
                    "title": "Notas para aprobar una materia",
                    "detail": "Si necesitás promedio 7 en 4 exámenes, tu meta real es sumar `7 × 4 = 28` puntos en total.",
                },
                {
                    "title": "Gráficos engañosos en noticias o publicidad",
                    "detail": "Un eje que arranca en `98%` hace que `99%` parezca el doble de alto que `98.5%`.",
                },
            ],
            "key_rule": "Media = suma ÷ cantidad · Mediana = el centro ordenado (a prueba de extremos) · En gráficos, chequeá siempre el 0 del eje.",
            "pitfall": "Sacar la mediana sin ordenar los números primero (agarrar el que vino en el medio de la lista desordenada).",
        },
        "example": {
            "title": "Compará media y mediana en tus tiempos de corrida",
            "steps": [
                "Cinco corridas de 5 km: `28`, `29`, `30`, `30` y `58` minutos (un día que paraste a charlar).",
                "La **media** da `(28+29+30+30+58) ÷ 5 = 35 min` (inflada por ese día raro).",
                "La **mediana** (el 3º valor ordenado) es `30 min`, que refleja tu ritmo real de todos los días.",
            ],
            "lab_link": None,
            "lab_cta": None,
        },
        "check": {
            "question": "Tus últimos 5 puntajes fueron `10, 4, 8, 6, 12`. ¿Cuál es la MEDIANA?",
            "options": [
                {"text": "8", "ok": True, "feedback": "Exacto: ordenados quedan 4, 6, 8, 10, 12 y el del medio es 8."},
                {"text": "6", "ok": False, "feedback": "6 es el segundo valor una vez ordenados, no el del centro."},
                {"text": "40", "ok": False, "feedback": "40 es la suma total, no la mediana."},
            ],
        },
        "checks": [
            {
                "question": "Tenés los datos `2, 5, 5, 7, 11`. ¿Cuál es la MODA?",
                "options": [
                    {"text": "5 (el valor que más veces aparece)", "ok": True, "feedback": "Exacto: el 5 se repite dos veces y todos los demás una sola vez."},
                    {"text": "6", "ok": False, "feedback": "6 es la media (promedio), no la moda."},
                    {"text": "9", "ok": False, "feedback": "9 es el rango (11 − 2), no la moda."},
                ],
            },
            {
                "question": "En la secuencia `4, 9, 14, 19…`, ¿qué número sigue?",
                "options": [
                    {"text": "24", "ok": True, "feedback": "Exacto: suma +5 en cada paso (19 + 5 = 24)."},
                    {"text": "23", "ok": False, "feedback": "Sumaste +4 en vez de +5."},
                    {"text": "29", "ok": False, "feedback": "Sumaste +10 (saltaste dos pasos)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá cuándo conviene mirar la mediana en vez del promedio y qué revisar primero en un gráfico de barras.",
    },
    "p-medicion-geometria": {
        "hook": {
            "question": "En la pizzería, la pizza grande mide el DOBLE de ancho que la chica (`40 cm` vs. `20 cm`). ¿Trae el doble de comida… o cuatro veces más?",
            "intuition": "**Cuatro veces más**. Al duplicar el largo y el ancho a la vez, la superficie (área) se multiplica por `2 × 2 = 4`. Distinguir perímetro (1D), área (2D) y volumen (3D) ahorra dinero real.",
        },
        "concept": {
            "points": [
                "**Perímetro (1D, metros `m`)**: la suma del borde exterior (cercas, zócalos, marcos).",
                "**Área (2D, `m²`)**: la superficie cubierta por dentro. Rectángulo = `base × altura`; Triángulo = `(base × altura) ÷ 2`; Círculo = `π · r²` (`π ≈ 3.14`, con radio `r = diámetro ÷ 2`).",
                "**Volumen (3D, `m³` o litros)**: el espacio que cabe adentro. Caja = `largo × ancho × alto`; Cilindro = `π · r² · altura`.",
                "**Unidades al cuadrado y al cubo**: `1 m = 100 cm`, pero **`1 m² = 10 000 cm²`** (`100 × 100`), y **`1 litro = 1000 cm³`** (un cubo de `10 × 10 × 10 cm`).",
            ],
            "real_world": [
                {
                    "title": "Comprar pintura vs. comprar zócalos",
                    "detail": "Los zócalos van por **perímetro** (`m`), la pintura y la cerámica van por **área** (`m²`).",
                },
                {
                    "title": "Elegir el tamaño de pizza",
                    "detail": "Una pizza de `r = 20 cm` (`π·400 ≈ 1256 cm²`) tiene **4 veces** el área de una de `r = 10 cm` (`314 cm²`).",
                },
                {
                    "title": "Capacidad de una pecera o tanque",
                    "detail": "Multiplicás las 3 medidas en `cm` y dividís por `1000` para saber los **litros** exactos.",
                },
            ],
            "key_rule": "Perímetro = contorno (`m`) · Área = `b·h`, `b·h/2`, `πr²` (`m²`) · Volumen = `l·a·h` (`1 L = 1000 cm³`).",
            "pitfall": "Usar el diámetro en lugar del radio en `π · r²`, o creer que `1 m²` son `100 cm²` (en realidad son `10 000 cm²`).",
        },
        "example": {
            "title": "Calculá cuántos litros caben en una caja de agua",
            "steps": [
                "Una pecera mide `50 cm` de largo, `20 cm` de ancho y `30 cm` de alto.",
                "Multiplicamos las 3 medidas: `50 × 20 × 30 = 30 000 cm³`.",
                "Como cada litro ocupa `1000 cm³`, dividimos por `1000`: caben exactamente **`30 litros`**.",
            ],
            "lab_link": "math:mult_div",
            "lab_cta": "Practicar multiplicaciones en el Laboratorio",
        },
        "check": {
            "question": "Querés poner alambrado alrededor de un jardín de `6 m × 4 m`. ¿Qué necesitás calcular?",
            "options": [
                {"text": "El perímetro: `6 + 4 + 6 + 4 = 20 m`", "ok": True, "feedback": "Exacto: el alambrado rodea el contorno."},
                {"text": "El área: `6 × 4 = 24 m²`", "ok": False, "feedback": "El área te serviría para comprar pasto/césped, no alambrado."},
                {"text": "El volumen", "ok": False, "feedback": "El volumen es para espacio en 3D (como tierra o agua)."},
            ],
        },
        "checks": [
            {
                "question": "Un triángulo tiene base `10 cm` y altura `6 cm`. ¿Cuál es su área?",
                "options": [
                    {"text": "60 cm²", "ok": False, "feedback": "60 es el rectángulo entero; el triángulo es la mitad."},
                    {"text": "30 cm²", "ok": True, "feedback": "Exacto: (10 × 6) ÷ 2 = 30 cm²."},
                    {"text": "16 cm²", "ok": False, "feedback": "Sumaste base + altura en vez de multiplicar y dividir por 2."},
                ],
            },
            {
                "question": "Un círculo tiene **diámetro** `10 cm`. ¿Cuánto vale el radio `r` que ponés en `π · r²`?",
                "options": [
                    {"text": "5 cm", "ok": True, "feedback": "Exacto: el radio es siempre la mitad del diámetro (área ≈ 3.14 × 25 = 78.5 cm²)."},
                    {"text": "10 cm", "ok": False, "feedback": "10 cm es el diámetro completo de lado a lado."},
                    {"text": "20 cm", "ok": False, "feedback": "El radio es la mitad del diámetro, no el doble."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá la diferencia entre perímetro, área y volumen y por qué una pizza de doble diámetro trae 4 veces más comida.",
    },
    # ==================== NIVEL 7: RAZONES Y PORCENTAJES ====================
    "p-razones-tasas": {
        "hook": {
            "question": "En la góndola hay un café de `250 g` a `$5000` y otro de `400 g` a `$7200`. ¿Cuál te sale realmente más barato sin adivinar?",
            "intuition": "Pasando ambos a **tasa unitaria** (precio por cada `100 g`): el chico sale `$2000` y el grande `$1800`. Las razones y tasas unitarias te permiten comparar cualquier oferta en segundos.",
        },
        "concept": {
            "points": [
                "**Razón (`a : b`)**: compara dos cantidades (`2 tazas de agua por cada 1 de arroz`). Multiplicar o dividir ambos lados por lo mismo mantiene la receta intacta (`4 : 2`, `6 : 3`).",
                "**Tasa unitaria**: lleva la segunda cantidad a **1 unidad** (`$/kg`, `km/L`, `km/h`). Es la forma más limpia de comparar productos o velocidades.",
                "**Proporcionalidad directa (regla de tres)**: si una sube al doble, la otra también (`4 personas → 300 g`; `1 persona → 75 g`; `6 personas → 450 g`).",
                "**Proporcionalidad inversa (¡cuidado!)**: cuando subir una **achica** la otra (más velocidad → menos tiempo; doble de pintores → mitad de horas). El producto `A × B` queda constante.",
            ],
            "real_world": [
                {
                    "title": "Comparar precios en el supermercado",
                    "detail": "Mirar el precio por kilo o por litro (tasa unitaria) desenmascara envases 'económicos' que en realidad son más caros.",
                },
                {
                    "title": "Escalar recetas de cocina",
                    "detail": "Si una receta es para 4 y vienen 6, dividís por 4 (por persona) y multiplicás por 6.",
                },
                {
                    "title": "Tiempos de viaje o trabajo en equipo",
                    "detail": "3 personas pintan en 8 h (`24 h-persona`); 6 personas lo terminan en `24 ÷ 6 = 4 h` (inversa).",
                },
            ],
            "key_rule": "Tasa unitaria = llevar a 1 unidad · Directa: suben juntas · Inversa: cuando una sube `×k`, la otra baja `÷k`.",
            "pitfall": "Aplicar regla de tres directa cuando la situación es inversa (decir que el doble de obreros tardará el doble de días).",
        },
        "example": {
            "title": "Resolvé proporciones pasando por la unidad",
            "steps": [
                "Problema: una receta para `4` personas lleva `300 g` de fideos. ¿Cuánto para `6` personas?",
                "Paso 1 (tasa unitaria): para `1` persona son `300 ÷ 4 = 75 g`.",
                "Paso 2 (escalar): para `6` personas multiplicamos `75 × 6 = 450 g`.",
            ],
            "lab_link": "math:percentages",
            "lab_cta": "Practicar proporciones en el Laboratorio",
        },
        "check": {
            "question": "Un paquete de `500 g` de yerba cuesta `$3000` y otro de `1 kg` (`1000 g`) cuesta `$5400`. ¿Cuál tiene menor precio por kilo?",
            "options": [
                {"text": "El de 1 kg (`$5400/kg` frente a `$6000/kg` del chico)", "ok": True, "feedback": "Exacto: dos paquetes chicos de 500 g saldrían $6000."},
                {"text": "El de 500 g, porque $3000 es menor que $5400", "ok": False, "feedback": "Estás comparando cantidades distintas; llevado al mismo kilo sale $6000."},
                {"text": "Salen exactamente lo mismo por kilo", "ok": False, "feedback": "$5400 vs. $6000 no es igual."},
            ],
        },
        "checks": [
            {
                "question": "4 personas arman un pedido en 6 horas. Si se suman más y son 8 personas trabajando igual, ¿cuánto tardan?",
                "options": [
                    {"text": "12 horas", "ok": False, "feedback": "Aplicaste directa: el doble de gente no tarda el doble, tarda la mitad."},
                    {"text": "3 horas", "ok": True, "feedback": "Exacto: proporcionalidad inversa (4×6 = 24 horas-persona → 24 ÷ 8 = 3 h)."},
                    {"text": "6 horas", "ok": False, "feedback": "Con el doble de manos se termina en la mitad del tiempo."},
                ],
            },
            {
                "question": "Un auto gasta `8 litros` cada `100 km`. ¿Cuántos litros necesita para `250 km`?",
                "options": [
                    {"text": "20 litros", "ok": True, "feedback": "Exacto: 250 km = 2.5 × 100 km → 8 × 2.5 = 20 L."},
                    {"text": "16 litros", "ok": False, "feedback": "16 L alcanzan solo para 200 km; faltan los 50 km extra (4 L más)."},
                    {"text": "24 litros", "ok": False, "feedback": "24 L serían para 300 km."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá la diferencia entre proporcionalidad directa e inversa con un ejemplo cotidiano de cada una.",
    },
    "p-porcentajes": {
        "hook": {
            "question": "Si un producto de `$100` sube `20%` y al mes siguiente le hacen `20%` de descuento, ¿vuelve a costar `$100`?",
            "intuition": "No: termina en **`$96`**. Porque el primer `20%` fue sobre `$100` (`+$20` → `$120`), pero el segundo `20%` se descontó sobre `$120` (`−$24` → `$96`). Entender la base del porcentaje te evita caer en casi todas las trampas comerciales.",
        },
        "concept": {
            "points": [
                "**Qué es un porcentaje**: simplemente una fracción sobre `100` (`25% = 25/100 = 0.25 = 1/4`).",
                "**Cálculo mental instantáneo**: `10%` = dividir por `10`; `5%` = mitad del 10%; `1%` = dividir por `100`; `25%` = dividir por `4`; `50%` = mitad.",
                "**Factor multiplicativo (1 solo paso)**: descontar `20%` es pagar el `80%` → multiplicás por **`0.80`**. Sumar `21%` de IVA es pagar `121%` → multiplicás por **`1.21`**.",
                "**Volver al precio original**: si pagaste `$60` con `25%` off (`0.75`), para recuperar el original **dividís** por `0.75` (`60 ÷ 0.75 = $80`), ¡NO le sumás `25%` a `$60`!",
            ],
            "real_world": [
                {
                    "title": "Propinas y descuentos en 2 segundos",
                    "detail": "`15%` de `$240`: `10%` = `24`, `5%` = `12` → `24 + 12 = $36`.",
                },
                {
                    "title": "Inflación o intereses compuestos",
                    "detail": "Dos aumentos seguidos de `10%` NO son `20%`: son `1.10 × 1.10 = 1.21` (`+21%`), porque el segundo sube sobre el primero.",
                },
                {
                    "title": "Calcular impuestos (IVA 21%)",
                    "detail": "Precio neto × `1.21` = precio con IVA; precio con IVA ÷ `1.21` = precio neto.",
                },
            ],
            "key_rule": "Descuento `p%` → `× (1 − p/100)` · Recargo `p%` → `× (1 + p/100)` · Porcentajes sucesivos se **multiplican**, no se suman.",
            "pitfall": "Sumar `25%` al precio descontado para buscar el precio original (o pensar que `+20%` y `−20%` se cancelan).",
        },
        "example": {
            "title": "Descuento + recargo en una sola línea",
            "steps": [
                "Una bicicleta cuesta `$10 000`, tiene `20%` de descuento y además paga `10%` de envío sobre lo que pagás.",
                "Aplicamos descuento: `10 000 × 0.80 = $8000`.",
                "Aplicamos `+10%`: `8000 × 1.10 = $8800` (factor combinado `0.80 × 1.10 = 0.88`, o sea `−12%` neto).",
            ],
            "lab_link": "math:percentages",
            "lab_cta": "Practicar porcentajes en el Laboratorio",
        },
        "check": {
            "question": "Una campera de `$200` tiene `30%` de descuento. ¿Por qué número podés multiplicar `$200` para obtener el precio FINAL en un solo paso?",
            "options": [
                {"text": "`0.70` (porque pagás el 70% → `$140`)", "ok": True, "feedback": "Exacto: 100% − 30% = 70% = 0.70."},
                {"text": "`0.30`", "ok": False, "feedback": "× 0.30 te da el descuento ($60), no lo que terminás pagando."},
                {"text": "`1.30`", "ok": False, "feedback": "× 1.30 sumaría un 30% de recargo."},
            ],
        },
        "checks": [
            {
                "question": "Un precio de `$100` baja `50%` y luego sube `50%`. ¿En cuánto queda?",
                "options": [
                    {"text": "`$100`", "ok": False, "feedback": "Baja a $50, y el 50% de $50 es solo $25, no $50."},
                    {"text": "`$75`", "ok": True, "feedback": "Exacto: 100 × 0.50 = 50, y 50 × 1.50 = 75."},
                    {"text": "`$125`", "ok": False, "feedback": "Primero bajó a la mitad ($50) antes de subir."},
                ],
            },
            {
                "question": "Dos subas consecutivas de `10%` equivalen a un aumento total de:",
                "options": [
                    {"text": "`20%`", "ok": False, "feedback": "La segunda suba también se aplica sobre el primer 10%."},
                    {"text": "`21%` (`1.10 × 1.10 = 1.21`)", "ok": True, "feedback": "Exacto: 100 → 110 → 121 (+21%)."},
                    {"text": "`11%`", "ok": False, "feedback": "Cada suba es del 10%, así que supera el 20%."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué subir 20% y bajar 20% no vuelve al número original y cómo usar factores como `0.80` o `1.21`.",
    },
    # ==================== NIVEL 8: RAÍCES Y NOTACIÓN CIENTÍFICA ====================
    "p-raices-notacion": {
        "hook": {
            "question": "¿Cómo escriben los científicos la distancia al Sol (`150 000 000 000 m`) o el tamaño de un transistor (`0.000000003 m`) sin volverse locos contando ceros?",
            "intuition": "Con **notación científica**: `1.5 × 10¹¹ m` y `3 × 10⁻⁹ m`. Combinando leyes de exponentes y raíces, cualquier número gigante o microscópico se maneja con cuentas cortísimas.",
        },
        "concept": {
            "points": [
                "**Leyes de exponentes (misma base)**: multiplicar **suma** exponentes (`10³ · 10⁴ = 10⁷`); dividir **resta** exponentes (`10⁵ ÷ 10² = 10³`); potencia de potencia **multiplica** (`(2³)² = 2⁶`).",
                "**Exponente 0 y negativos**: `a⁰ = 1` (para `a ≠ 0`) y **`a⁻ⁿ = 1 / aⁿ`**. Un exponente negativo da el **recíproco** y NO cambia el signo: con base mayor que 1 el resultado queda chico (`10⁻³ = 0.001`).",
                "**Raíces (inversas de potencias)**: `√49 = 7` (porque `7² = 49`) y `∛27 = 3` (porque `3³ = 27`). Si no es exacta (ej. `√50`), sabés al instante que está apenas arriba de `7`.",
                "**Notación científica (`a × 10ⁿ`)**: siempre deja **un solo dígito (1 a 9)** antes de la coma. Exponente positivo = número grande; negativo = número chico (`< 1`).",
            ],
            "real_world": [
                {
                    "title": "Física y Astronomía",
                    "detail": "La velocidad de la luz es `3 × 10⁸ m/s` y el Wi-Fi vibra a `2.4 × 10⁹ Hz`: dividirlos es solo `3 ÷ 2.4` y `10⁸ ÷ 10⁹ = 10⁻¹`.",
                },
                {
                    "title": "Electrónica (mA, kΩ, μF)",
                    "detail": "`mili` es `10⁻³`, `micro` es `10⁻⁶`, `kilo` es `10³`, `mega` es `10⁶`.",
                },
                {
                    "title": "Medir el lado de un terreno cuadrado",
                    "detail": "Un lote cuadrado de `144 m²` tiene lados de `√144 = 12 m`.",
                },
            ],
            "key_rule": "`aᵐ·aⁿ = aᵐ⁺ⁿ` · `a⁻ⁿ = 1/aⁿ` (recíproco, no cambia el signo!) · Notación científica: `1 ≤ a < 10` × `10ⁿ`.",
            "pitfall": "Pensar que `10⁻²` es `−100` (en realidad es `1/100 = 0.01`) o que `√25` es `12.5` (no es dividir por 2, es buscar qué número al cuadrado da 25).",
        },
        "example": {
            "title": "Calculá corriente con potencias de 10",
            "steps": [
                "Una fuente de `6 V` alimenta una resistencia de `3 kΩ = 3 × 10³ Ω`.",
                "Dividimos números y potencias aparte: `I = 6 / (3 × 10³) = (6 ÷ 3) × 10⁻³ = 2 × 10⁻³ A`.",
                "Como `10⁻³ A` es `1 mA`, el resultado es `2 mA` (`0.002 A`) sin escribir un solo cero extra.",
            ],
            "lab_link": "math:powers",
            "lab_cta": "Practicar potencias y exponentes en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es el valor de `10⁻²`?",
            "options": [
                {"text": "`0.01` (`1/100`)", "ok": True, "feedback": "Exacto: exponente negativo invierte a fracción 1 / 10² = 0.01."},
                {"text": "`−100`", "ok": False, "feedback": "Un exponente negativo jamás cambia el signo del número a negativo."},
                {"text": "`−20`", "ok": False, "feedback": "No se multiplica la base por el exponente."},
            ],
        },
        "checks": [
            {
                "question": "¿Entre qué dos enteros está `√50`?",
                "options": [
                    {"text": "Entre `7` y `8` (cerca de `7.1`, porque `7² = 49` y `8² = 64`)", "ok": True, "feedback": "Exacto: estimar raíces comparando cuadrados cercanos es súper útil."},
                    {"text": "Entre `24` y `26`", "ok": False, "feedback": "Dividiste por 2; 25² es 625, no 50."},
                    {"text": "Entre `5` y `6`", "ok": False, "feedback": "6² es 36, todavía lejos de 50."},
                ],
            },
            {
                "question": "Simplificá `2⁵ ÷ 2²`.",
                "options": [
                    {"text": "`2³` (= `8`)", "ok": True, "feedback": "Exacto: al dividir potencias de igual base se restan los exponentes (5 − 2 = 3)."},
                    {"text": "`2⁷`", "ok": False, "feedback": "Sumaste exponentes; eso es para multiplicación."},
                    {"text": "`1³`", "ok": False, "feedback": "La base 2 se conserva, no se divide 2 ÷ 2."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué hace realmente un exponente negativo (`10⁻³`) y cómo facilita trabajar con números gigantes o microscópicos.",
    },
    # ==================== NIVEL 9: VARIABLES, ECUACIONES Y DESIGUALDADES ====================
    "p-variables-expresiones": {
        "hook": {
            "question": "¿Por qué de golpe las matemáticas empiezan a usar letras como `x`? ¿Se inventaron para complicarte la vida?",
            "intuition": "Al contrario: una letra es solo una **caja vacía con etiqueta** para guardar un número que cambia (como los kilómetros de un viaje o las horas trabajadas). En vez de hacer la misma cuenta 50 veces, escribís la receta UNA sola vez: `500 + 80x`.",
        },
        "concept": {
            "points": [
                "**Variable**: una letra (`x`, `t`, `n`) que representa un número desconocido o que puede variar. Nota: `4x` significa `4 × x` (se omite el signo `×` para no confundirlo con la letra `x`).",
                "**Evaluar**: reemplazar la letra por un número concreto y calcular respetando PEMDAS (`500 + 80x` para `x = 6` da `980`).",
                "**Términos semejantes**: solo podés sumar/restar términos que tengan la **misma letra y mismo exponente** (`5x − 2x = 3x`, y los números sueltos aparte: `3 + 7 = 10` → `3x + 10`).",
                "**Propiedad distributiva**: el número pegado a un paréntesis multiplica a **todo lo que está adentro** (`4(2x − 5) = 8x − 20`).",
            ],
            "real_world": [
                {
                    "title": "Fórmulas de hojas de cálculo (Excel/Sheets)",
                    "detail": "Cuando ponés `=500 + 80*A2`, la celda `A2` es literalmente la variable `x`.",
                },
                {
                    "title": "Programar en Arduino o Python",
                    "detail": "Cada variable del código (`velocidad`, `precio`, `tiempo`) funciona exactamente igual que una variable algebraica.",
                },
                {
                    "title": "Presupuestos con costo fijo + variable",
                    "detail": "Envío fijo (`$1500`) + `x` unidades a `$1200` → `1200x + 1500` sirve para cualquier pedido.",
                },
            ],
            "key_rule": "`4x` = `4 · x` · Sumá solo términos semejantes (`x` con `x`, números con números) · Distribuí a TODOS los términos del paréntesis.",
            "pitfall": "Sumar `3x + 4` como `7x`, o al distribuir `3(x + 5)` multiplicar solo el primero y olvidar el segundo (`3x + 5` en vez de `3x + 15`).",
        },
        "example": {
            "title": "Simplificá `3(x + 4) − x + 2`",
            "steps": [
                "Primero distribuimos el `3` en el paréntesis: `3·x + 3·4 = 3x + 12` → queda `3x + 12 − x + 2`.",
                "Agrupamos términos con `x`: `3x − 1x = 2x`.",
                "Agrupamos números sueltos: `12 + 2 = 14`. Resultado limpio: **`2x + 14`**.",
            ],
            "lab_link": "math:linear_eq",
            "lab_cta": "Explorar ecuaciones en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál es la simplificación correcta de `6x + 4 − 2x + 5`?",
            "options": [
                {"text": "`4x + 9`", "ok": True, "feedback": "Exacto: (6x − 2x) = 4x y (4 + 5) = 9."},
                {"text": "`13x`", "ok": False, "feedback": "No podés sumar números sueltos con términos que llevan x."},
                {"text": "`8x + 9`", "ok": False, "feedback": "El 2x tenía un signo menos adelante (6x − 2x = 4x)."},
            ],
        },
        "checks": [
            {
                "question": "Expandí `5(x − 3)` usando la propiedad distributiva.",
                "options": [
                    {"text": "`5x − 3`", "ok": False, "feedback": "Te faltó multiplicar el 5 también por el −3."},
                    {"text": "`5x − 15`", "ok": True, "feedback": "Exacto: 5·x = 5x y 5·(−3) = −15."},
                    {"text": "`5x + 15`", "ok": False, "feedback": "Cuidado con el signo: +5 × (−3) = −15."},
                ],
            },
            {
                "question": "Si una entrada cuesta `$10` y el estacionamiento fijo `$15`, ¿cuánto pagás en total si comprás `x = 4` entradas (`10x + 15`)?",
                "options": [
                    {"text": "`$55`", "ok": True, "feedback": "Exacto: 10(4) + 15 = 40 + 15 = $55."},
                    {"text": "`$100`", "ok": False, "feedback": "El estacionamiento se paga una sola vez, no 4 veces."},
                    {"text": "`$29`", "ok": False, "feedback": "10x significa 10 × 4 = 40, no 10 + 4."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué es una variable usando un ejemplo cotidiano y por qué `3x + 4` no se puede juntar en `7x`.",
    },
    "p-ecuaciones-un-paso": {
        "hook": {
            "question": "Un técnico te cobró `$140` en total (`$40` de visita fija + `$25` por hora). ¿Cómo descubrís cuántas horas trabajó usando la regla de la balanza?",
            "intuition": "Una ecuación (`40 + 25h = 140`) es una **balanza en equilibrio**. Mientras hagas exactamente la misma operación en ambos platillos (sacar `40` de cada lado → `25h = 100`; dividir por `25` → `h = 4`), el equilibrio jamás se rompe.",
        },
        "concept": {
            "points": [
                "**Principio de la balanza**: el signo `=` garantiza que ambos lados pesan igual. Todo lo que sumás, restás, multiplicás o dividís de un lado, **lo hacés también del otro**.",
                "**Operaciones inversas**: suma ↔ resta; multiplicación ↔ división.",
                "**Orden al despejar (PEMDAS al revés)**: para `3x − 7 = 14`, primero deshacés lo más flojo (sumas/restas: `+7` → `3x = 21`) y al final lo pegado a la `x` (`÷3` → `x = 7`).",
                "**Verificación instantánea**: meté tu respuesta en la ecuación original (`3(7) − 7 = 14`). Si ambos lados dan lo mismo, sabés con 100% de certeza que está bien.",
            ],
            "real_world": [
                {
                    "title": "Despejar cualquier fórmula de Física o Electrónica",
                    "detail": "De `V = I · R` a `I = V / R`, o de `F = m · a` a `a = F / m`: es exactamente una ecuación de 1 paso.",
                },
                {
                    "title": "Revisar facturas con cargo fijo + variable",
                    "detail": "Restás el cargo fijo y dividís por el precio por unidad/hora para verificar cuántas unidades te cobraron.",
                },
                {
                    "title": "Planificar metas de ahorro",
                    "detail": "`ahorro_actual + mensual · meses = meta` te dice los meses exactos.",
                },
            ],
            "key_rule": "Misma operación en ambos lados · Deshacé primero las sumas/restas que están fuera de paréntesis, luego multiplicaciones/divisiones · Verificá siempre sustituyendo.",
            "pitfall": "Olvidar cambiar la operación al despejar (en `3x − 7 = 14`, restar 7 en vez de sumar 7) o dividir solo un término en vez de todo el lado.",
        },
        "example": {
            "title": "Despejá `3x − 7 = 14` y comprobalo",
            "steps": [
                "Sumamos `7` en ambos platillos para anular el `−7`: `3x = 21`.",
                "Dividimos ambos lados por `3`: `x = 7`.",
                "Verificamos reemplazando en la original: `3(7) − 7 = 21 − 7 = 14`. ¡Exacto!",
            ],
            "lab_link": "math:linear_eq",
            "lab_cta": "Practicar despejes en el Laboratorio",
        },
        "check": {
            "question": "Resolvé `4x + 5 = 29`. ¿Cuánto vale `x`?",
            "options": [
                {"text": "`6`", "ok": True, "feedback": "Exacto: restás 5 → 4x = 24 → dividís por 4 → x = 6 (4·6 + 5 = 29)."},
                {"text": "`8.5`", "ok": False, "feedback": "Sumaste 5 en lugar de restarlo (29 + 5 = 34)."},
                {"text": "`24`", "ok": False, "feedback": "24 es 4x; faltó el último paso de dividir por 4."},
            ],
        },
        "checks": [
            {
                "question": "Resolvé `3(x − 2) = 15`.",
                "options": [
                    {"text": "`7`", "ok": True, "feedback": "Exacto: dividís por 3 → x − 2 = 5 → sumás 2 → x = 7."},
                    {"text": "`3`", "ok": False, "feedback": "Restaste 2 en vez de sumarlo (3 − 2 = 1, y 3×1 = 3 ≠ 15)."},
                    {"text": "`5`", "ok": False, "feedback": "5 es (x − 2), todavía falta sumar 2 para despejar x."},
                ],
            },
            {
                "question": "Resolvé `6x − 2 = 4x + 10`.",
                "options": [
                    {"text": "`6`", "ok": True, "feedback": "Exacto: restás 4x (2x − 2 = 10) → sumás 2 (2x = 12) → x = 6."},
                    {"text": "`4`", "ok": False, "feedback": "Restaste 2 en vez de sumar 2 al 10."},
                    {"text": "`1.2`", "ok": False, "feedback": "Sumaste 6x + 4x en vez de restar 4x en ambos lados."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con la analogía de la balanza cómo se resuelve una ecuación de dos pasos y cómo sabés si te dio bien.",
    },
    "p-desigualdades": {
        "hook": {
            "question": "En la vida real casi nunca tenés que gastar *exactamente* `$50` — tenés que gastar **`$50` o menos**. ¿En qué se parece y en qué única regla cambia una desigualdad respecto a una ecuación?",
            "intuition": "Se despeja casi 100% igual que una ecuación, con **una sola regla extra** que hay que grabar a fuego: si multiplicás o dividís ambos lados por un **número negativo**, el pico de la desigualdad **se da vuelta**.",
        },
        "concept": {
            "points": [
                "**Los 4 símbolos**: `<` (menor estricto), `>` (mayor estricto), `≤` (menor o igual = *como máximo*), `≥` (mayor o igual = *al menos / como mínimo*).",
                "**Muchas soluciones, no solo una**: `x ≤ 3` significa que vale `3` y cualquier número menor (`2.5`, `2`, `0`, `−1.7`…). En la recta numérica: punto **relleno** si incluye el borde (`≤, ≥`), punto **hueco** si no (`<, >`).",
                "**Sumar o restar no cambia el signo**: `x + 5 ≤ 12` → restás `5` → `x ≤ 7`.",
                "**La regla de oro del negativo**: probalo con `2 < 5`. Si multiplicás ambos lados por `−1`, `−2` es MAYOR que `−5` (`−2 > −5`)! Por eso, al multiplicar o dividir por un negativo **siempre se invierte el símbolo**.",
            ],
            "real_world": [
                {
                    "title": "Presupuestos con tope",
                    "detail": "Envío `$14` + `x` libros de `$12` con tope `$50` → `12x + 14 ≤ 50` → `x ≤ 3` libros.",
                },
                {
                    "title": "Límites de seguridad",
                    "detail": "Peso máximo en un ascensor (`p ≤ 400 kg`), velocidad máxima (`v ≤ 60 km/h`), edad mínima (`e ≥ 18`).",
                },
                {
                    "title": "Márgenes en electrónica",
                    "detail": "Una resistencia de 1/4 W exige `P ≤ 250 mW` para no quemarse.",
                },
            ],
            "key_rule": "Despejá igual que una ecuación, PERO **al multiplicar o dividir por un negativo, invertí el signo** (`<` ↔ `>`).",
            "pitfall": "Olvidar dar vuelta el signo al dividir por un negativo (escribir `−3x ≤ 12` → `x ≤ −4` en vez de `x ≥ −4`).",
        },
        "example": {
            "title": "Resolvé `−2x + 4 < 10` paso a paso",
            "steps": [
                "Restamos `4` en ambos lados (restar NO cambia el signo): `−2x < 6`.",
                "Dividimos por `−2` (es negativo → **damos vuelta** `<` a `>`): `x > −3`.",
                "Chequeo con un valor fácil que cumpla `x > −3`, por ejemplo `x = 0`: `−2(0) + 4 = 4 < 10` ¡Verdadero!",
            ],
            "lab_link": "math:linear_eq",
            "lab_cta": "Reforzar despejes en el Laboratorio",
        },
        "check": {
            "question": "Resolvé `−3x ≥ 15`.",
            "options": [
                {"text": "`x ≤ −5`", "ok": True, "feedback": "Exacto: dividiste por −3 (negativo) y diste vuelta ≥ a ≤."},
                {"text": "`x ≥ −5`", "ok": False, "feedback": "Probá x = 0 (cumple ≥ −5): −3(0) = 0, y 0 NO es ≥ 15. Faltó invertir el signo."},
                {"text": "`x ≤ 5`", "ok": False, "feedback": "15 ÷ (−3) = −5, no +5."},
            ],
        },
        "checks": [
            {
                "question": "Un paquete no puede superar `20 kg` (`peso ≤ 20`). Si la caja vacía pesa `2 kg` y cada libro `3 kg`, ¿cuántos libros como máximo caben (`2 + 3x ≤ 20`)?",
                "options": [
                    {"text": "6 libros", "ok": True, "feedback": "Exacto: 3x ≤ 18 → x ≤ 6."},
                    {"text": "7 libros", "ok": False, "feedback": "2 + 3(7) = 23 kg, se pasa del límite."},
                    {"text": "5 libros", "ok": False, "feedback": "Con 6 libros da justo 20 kg, y ≤ incluye el 20."},
                ],
            },
            {
                "question": "Al despejar `x − 7 > −2`, ¿hay que dar vuelta el signo `>`?",
                "options": [
                    {"text": "No: solo sumás `7` a ambos lados → `x > 5`", "ok": True, "feedback": "Exacto: el signo SOLO se invierte al multiplicar o dividir por un negativo, nunca al sumar o restar."},
                    {"text": "Sí, porque aparece un número negativo (`−2`)", "ok": False, "feedback": "Que haya un negativo en la cuenta no invierte el signo; solo multiplicar o dividir ambos lados por un negativo."},
                    {"text": "Sí, siempre que se mueve algo al otro lado", "ok": False, "feedback": "Sumar o restar lo mismo a ambos lados mantiene intacto el orden."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con un ejemplo numérico sencillo por qué hay que invertir la desigualdad al multiplicar o dividir por un negativo.",
    },
    # ==================== NIVEL 10: PLANO, RECTAS, FUNCIONES Y SISTEMAS ====================
    "p-plano-rectas": {
        "hook": {
            "question": "Si un remis cobra `$800` de bajada de bandera más `$150` por kilómetro, ¿cómo podés dibujar TODAS las tarifas posibles de un solo trazo?",
            "intuition": "Con una línea recta en el plano cartesiano: `y = 150x + 800`. El `800` (`b`) te dice dónde arranca la recta en el eje vertical, y el `150` (`m`) te dice qué tan empinada sube cada kilómetro.",
        },
        "concept": {
            "points": [
                "**Coordenadas `(x, y)`**: dos rectas numéricas cruzadas en `(0, 0)`. Primero te movés en horizontal (`x`), después en vertical (`y`).",
                "**Pendiente (`m = Δy / Δx`)**: cuánto sube (o baja) `y` cada vez que `x` avanza `1`. Se calcula entre dos puntos cualesquiera: `m = (y₂ − y₁) / (x₂ − x₁)`.",
                "**Signo de la pendiente**: `m > 0` sube de izquierda a derecha; `m < 0` baja (ej. batería descargándose); `m = 0` es horizontal (constante).",
                "**Forma `y = m·x + b`**: `m` es la **tasa de cambio** (pendiente) y `b` es el **valor inicial** donde la recta corta el eje `Y` (`x = 0`). Dos rectas con igual `m` son paralelas.",
            ],
            "real_world": [
                {
                    "title": "Tarifas de transporte y servicios",
                    "detail": "Cargo fijo (`b`) + precio por km/minuto/kWh (`m`) = línea recta `y = mx + b`.",
                },
                {
                    "title": "Carga o descarga de batería",
                    "detail": "Arranca en `100%` (`b = 100`) y baja `15%` por hora (`m = −15`): `y = −15x + 100`.",
                },
                {
                    "title": "Gráficas de Física (MRU)",
                    "detail": "En `x = x₀ + v·t`, la velocidad `v` es literalmente la pendiente de la recta posición-tiempo.",
                },
            ],
            "key_rule": "`y = mx + b` · `m = (y₂ − y₁)/(x₂ − x₁)` (tasa de cambio) · `b` = inicio en `x = 0`.",
            "pitfall": "Invertir las coordenadas `(x, y)` al graficar o calcular la pendiente al revés (`Δx / Δy` en lugar de `Δy / Δx`).",
        },
        "example": {
            "title": "Explorá `m` y `b` en vivo en el Graficador",
            "steps": [
                "Abrí el Laboratorio de Matemáticas → **Graficador y pizarra**.",
                "Mové el control de `b₁`: ves cómo la recta entera sube o baja sin cambiar su inclinación.",
                "Mové `m₁` de positivo a `0` y luego a negativo: observá cómo rota de subida, a horizontal y a bajada.",
            ],
            "lab_link": "math:linear_fn",
            "lab_cta": "Abrir Graficador de rectas en el Laboratorio",
        },
        "check": {
            "question": "Una recta pasa por `(0, 4)` y `(2, 10)`. ¿Cuál es su ecuación `y = mx + b`?",
            "options": [
                {"text": "`y = 3x + 4`", "ok": True, "feedback": "Exacto: b = 4 (en x=0) y m = (10 − 4) / (2 − 0) = 6 / 2 = 3."},
                {"text": "`y = 4x + 3`", "ok": False, "feedback": "Intercambiaste pendiente m y ordenada b."},
                {"text": "`y = 6x + 4`", "ok": False, "feedback": "Subió 6 en 2 pasos en x, así que por cada 1 paso sube 6 ÷ 2 = 3."},
            ],
        },
        "checks": [
            {
                "question": "Si una recta tiene ecuación `y = −2x + 7`, ¿qué pasa cuando `x` aumenta en `1`?",
                "options": [
                    {"text": "`y` baja `2` unidades", "ok": True, "feedback": "Exacto: pendiente m = −2 indica descenso de 2 por cada +1 en x."},
                    {"text": "`y` sube `7` unidades", "ok": False, "feedback": "7 es solo el valor inicial cuando x = 0."},
                    {"text": "`y` sube `2` unidades", "ok": False, "feedback": "El signo menos adelante del 2 indica bajada."},
                ],
            },
            {
                "question": "¿En qué punto corta al eje vertical `Y` la recta `y = 5x − 3`?",
                "options": [
                    {"text": "`(0, −3)`", "ok": True, "feedback": "Exacto: en el eje Y siempre x = 0, así que y = 5(0) − 3 = −3."},
                    {"text": "`(0, 5)`", "ok": False, "feedback": "5 es la pendiente, no la ordenada al origen."},
                    {"text": "`(−3, 0)`", "ok": False, "feedback": "En el eje Y la primera coordenada (x) es 0."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué representan la pendiente `m` y la ordenada `b` usando un ejemplo cotidiano como un taxi o una batería.",
    },
    "p-funciones": {
        "hook": {
            "question": "¿Qué tienen en común una máquina expendedora, el costo de tu plan de celular y una función en programación (`def calcular(x)`)?",
            "intuition": "Las tres son **funciones**: le das una entrada `x`, aplica una regla clara y te devuelve **una única salida** `f(x)`. Pensar en funciones es el puente directo entre la aritmética y el álgebra real.",
        },
        "concept": {
            "points": [
                "**Regla fundamental**: a cada entrada `x` le toca **una sola salida** `f(x)`. (Dos entradas distintas pueden repetir salida, pero la misma entrada nunca puede dar dos respuestas distintas).",
                "**Notación `f(x)`**: se lee *'f de x'* (la salida de la regla `f` para la entrada `x`). ¡No significa `f` multiplicado por `x`!",
                "**Prueba de la línea vertical**: en un gráfico, si alguna vertical corta la curva en 2 o más puntos, **no es una función**.",
                "**Lineal vs. No lineal**: una función es **lineal** cuando cambia siempre a ritmo constante (`+3` cada paso). Si se duplica cada paso (`2, 4, 8, 16`) o crece con `x²`, es **no lineal** (curva).",
            ],
            "real_world": [
                {
                    "title": "Funciones en código (Python / Arduino)",
                    "detail": "`f(x) = 2x + 5` es idéntico a `def f(x): return 2*x + 5`.",
                },
                {
                    "title": "Termostatos y sensores",
                    "detail": "Un sensor transforma temperatura (`x`) en un voltaje único (`f(x)`) que lee el ESP32.",
                },
                {
                    "title": "Crecimiento lineal vs. exponencial",
                    "detail": "Ahorrar `$100` por mes es lineal (recta); un interés que suma `10%` sobre el acumulado es exponencial (curva que se dispara).",
                },
            ],
            "key_rule": "Función = 1 entrada → 1 salida única · `f(3)` = evaluar en `x = 3` · Tasa constante = lineal; tasa variable = no lineal.",
            "pitfall": "Leer `f(4)` como 'f por 4' en vez de 'el valor de la función cuando x = 4'.",
        },
        "example": {
            "title": "Evaluar hacia adelante y hacia atrás en `f(x) = 3x + 2`",
            "steps": [
                "Hacia adelante — nos dan la entrada `x = 4`: `f(4) = 3(4) + 2 = 14`.",
                "Hacia atrás — nos dan la salida `f(x) = 20`: planteamos `3x + 2 = 20`.",
                "Despejamos: `3x = 18` → la entrada era `x = 6`.",
            ],
            "lab_link": "math:linear_fn",
            "lab_cta": "Practicar funciones lineales en el Laboratorio",
        },
        "check": {
            "question": "Dada `f(x) = 4x − 5`, ¿cuánto vale `f(3)`?",
            "options": [
                {"text": "`7`", "ok": True, "feedback": "Exacto: 4(3) − 5 = 12 − 5 = 7."},
                {"text": "`−1`", "ok": False, "feedback": "Hiciste 4 − 5 sin multiplicar el 4 por la entrada 3."},
                {"text": "`17`", "ok": False, "feedback": "Sumaste 5 en lugar de restarlo."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál de estos conjuntos de pares `(entrada, salida)` NO puede ser una función?",
                "options": [
                    {"text": "`(1, 5), (2, 5), (3, 5)`", "ok": False, "feedback": "Sí es una función (función constante): cada entrada tiene una única salida."},
                    {"text": "`(1, 4), (2, 7), (1, 9)`", "ok": True, "feedback": "Exacto: la entrada 1 produce dos salidas distintas (4 y 9) a la vez."},
                    {"text": "`(0, 0), (1, 1), (2, 4)`", "ok": False, "feedback": "Es f(x) = x², una función válida (no lineal)."},
                ],
            },
            {
                "question": "Si una tabla muestra `(1, 4), (2, 7), (3, 10), (4, 13)`, ¿es una función lineal?",
                "options": [
                    {"text": "Sí, porque sube siempre `+3` por cada paso en `x` (`f(x) = 3x + 1`)", "ok": True, "feedback": "Exacto: tasa de cambio constante = función lineal."},
                    {"text": "No, porque no pasa por `(0, 0)`", "ok": False, "feedback": "Una función lineal puede tener cualquier ordenada al origen b (acá b = 1)."},
                    {"text": "No, porque los números son impares y pares", "ok": False, "feedback": "Lo único que define linealidad es que el cambio Δy/Δx sea constante."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué es una función `f(x)` y cómo distinguís si una tabla corresponde a una función lineal o no.",
    },
    "p-sistemas-ecuaciones": {
        "hook": {
            "question": "Un gimnasio cobra `$30` de matrícula + `$5` por clase, y otro cobra `$10` por clase sin matrícula. ¿Cómo sabés exactamente a partir de cuántas clases te conviene cambiar al primero?",
            "intuition": "Cuando dos reglas compiten a la vez tenés un **sistema de ecuaciones 2×2**. Resolverlo es hallar el **punto de cruce exacto** donde los dos empatan (`6` clases = `$60`). Antes conviene uno; después conviene el otro.",
        },
        "concept": {
            "points": [
                "**Qué es un sistema 2×2**: dos ecuaciones con dos incógnitas (`x` e `y`) que deben cumplirse **al mismo tiempo**. Gráficamente es el punto `(x, y)` donde se cortan dos rectas.",
                "**Método 1 — Sustitución**: cuando una letra ya está despejada (`y = 10x`), la metés dentro de la otra ecuación (`10x = 5x + 30` → `x = 6`).",
                "**Método 2 — Eliminación (sumar/restar ecuaciones)**: si una variable tiene signos opuestos (`x + y = 14` y `x − y = 4`), sumás ambas ecuaciones y desaparece de golpe (`2x = 18` → `x = 9`).",
                "**Los 3 casos posibles**: se cruzan en **1 punto** (solución única), son **paralelas** (0 soluciones) o son la **misma recta** (infinitas soluciones).",
            ],
            "real_world": [
                {
                    "title": "Comparar planes de celular, luz o gimnasio",
                    "detail": "El punto de intersección te dice exactamente a partir de qué consumo te conviene pagar una cuota fija más alta.",
                },
                {
                    "title": "Punto de equilibrio en un emprendimiento",
                    "detail": "Donde la recta de ingresos (`precio · x`) cruza la de costos (`fijo + costo · x`) empezás a ganar dinero.",
                },
                {
                    "title": "Mezclas y conteo de entradas",
                    "detail": "Conociendo cantidad total (`a + n = 10`) y plata total (`10a + 6n = 84`) sacás cuántos de cada uno.",
                },
            ],
            "key_rule": "Solución 2×2 = punto de cruce `(x, y)` · Sustituí si una letra está sola · Sumá/restá si dos términos se cancelan.",
            "pitfall": "Encontrar solo `x` y olvidarse de reemplazarlo en una de las ecuaciones para hallar `y` (la solución completa siempre es el par `(x, y)`).",
        },
        "example": {
            "title": "Resolvé `x + y = 10` y `x − y = 4` y miralo en el Graficador",
            "steps": [
                "Sumamos las dos ecuaciones columna por columna: `(x + x) + (y − y) = 10 + 4` → `2x = 14`.",
                "Despejamos `x = 7` y reemplazamos en `x + y = 10` para hallar `y = 3`.",
                "Comprobalo en el **Graficador dual** del Laboratorio: las dos rectas se cortan justo en `(7, 3)`.",
            ],
            "lab_link": "math:systems",
            "lab_cta": "Probar Sistemas 2×2 y Graficador dual",
        },
        "check": {
            "question": "Si `x + y = 12` y `x − y = 2`, ¿cuál es la solución `(x, y)`?",
            "options": [
                {"text": "`x = 7, y = 5`", "ok": True, "feedback": "Exacto: sumando queda 2x = 14 → x = 7, y 7 + 5 = 12, 7 − 5 = 2."},
                {"text": "`x = 14, y = 2`", "ok": False, "feedback": "14 es 2x; faltó dividir por 2."},
                {"text": "`x = 6, y = 6`", "ok": False, "feedback": "6 + 6 = 12, pero 6 − 6 = 0 (no 2)."},
            ],
        },
        "checks": [
            {
                "question": "Plan A: `y = 4x + 20`. Plan B: `y = 8x`. ¿Para qué valor de `x` cuestan exactamente lo mismo?",
                "options": [
                    {"text": "`x = 5` (ambos salen `$40`)", "ok": True, "feedback": "Exacto: 4x + 20 = 8x → 20 = 4x → x = 5."},
                    {"text": "`x = 4`", "ok": False, "feedback": "En x = 4, A vale 36 y B vale 32 (todavía no empataron)."},
                    {"text": "`x = 20`", "ok": False, "feedback": "Faltó dividir 20 por la diferencia de pendientes (8 − 4 = 4)."},
                ],
            },
            {
                "question": "Dos rectas en un sistema tienen la misma pendiente (`m = 3`) pero distinta ordenada al origen (`b = 1` y `b = 5`). ¿Cuántas soluciones tiene el sistema?",
                "options": [
                    {"text": "Ninguna (son paralelas y nunca se cortan)", "ok": True, "feedback": "Exacto: si dos planes suben al mismo ritmo pero uno arranca más caro, jamás se alcanzan."},
                    {"text": "Una solución única", "ok": False, "feedback": "Para cruzarse necesitan tener pendientes distintas."},
                    {"text": "Dos soluciones", "ok": False, "feedback": "Dos rectas distintas pueden cortarse como máximo en un punto."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué significa el punto de cruce de un sistema 2×2 usando el ejemplo de comparar dos planes o tarifas.",
    },
}
