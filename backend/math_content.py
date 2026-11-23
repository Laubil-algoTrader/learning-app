"""Complete Math curriculum adapted from Khan Academy:
Arithmetic (17) + Pre-Algebra (12) + Algebra 1 (12) + Geometry (10) + Algebra 2 (11)
+ Trigonometry (6) + Precalculus (8) + Calculus 1 / AP AB (8) + Calculus 2 / AP BC (7)
+ Multivariable Calculus (8) + Differential Equations (6) + Linear Algebra (7) = 112 progressive units,
plus 5 entrance-exam algebra units spliced in at the end of this module (117 in total).
"""

from __future__ import annotations

from backend.algebra1_content import ALGEBRA1_LESSONS, ALGEBRA1_NODES
from backend.algebra2_content import ALGEBRA2_LESSONS, ALGEBRA2_NODES
from backend.calculus1_content import CALCULUS1_LESSONS, CALCULUS1_NODES
from backend.calculus2_content import CALCULUS2_LESSONS, CALCULUS2_NODES
from backend.diffeq_content import DIFFEQ_LESSONS, DIFFEQ_NODES
from backend.geometry_content import GEOMETRY_LESSONS, GEOMETRY_NODES
from backend.linalg_content import LINALG_LESSONS, LINALG_NODES
from backend.multivariable_content import MULTIVARIABLE_LESSONS, MULTIVARIABLE_NODES
from backend.prealgebra_content import PREALGEBRA_LESSONS, PREALGEBRA_NODES
from backend.precalculus_content import PRECALCULUS_LESSONS, PRECALCULUS_NODES
from backend.trigonometry_content import TRIGONOMETRY_LESSONS, TRIGONOMETRY_NODES

RETIRED_MATH_NODE_SLUGS: tuple[str, ...] = (
    "m-enteros-pemdas",
    "m-fracciones",
    "m-porcentajes-proporciones",
    "m-potencias-cientifica",
    "m-ecuaciones-lineales",
    "m-sistemas-2x2",
    "m-funciones-lineales",
    "m-geometria-trigonometria",
)

MATH_DOMAIN = {
    "slug": "matematicas",
    "name": "Matemáticas",
    "icon": "math",
    "color": "#4b5563",
    "domain_type": "conceptual",
    "lab_type": "math",
    "description": (
        "Ruta completa desde cero hasta universidad (117 temas): Aritmética, Preálgebra, "
        "Álgebra 1, Geometría, Álgebra 2, Trigonometría, Precálculo, Cálculo 1, Cálculo 2, "
        "Cálculo multivariable, Ecuaciones diferenciales y Álgebra lineal."
    ),
    "config": {
        "tools": ["worked_examples", "interleaved_practice", "scratchpad"],
        "method_tips": [
            "Estimá primero el orden de magnitud ('¿tendría que dar cerca de 20 o de 200?') antes de hacer la cuenta exacta.",
            "Entendé el 'por qué' con dinero, recetas o medidas reales: las reglas mecánicas se olvidan, la intuición queda.",
            "Usá la práctica mezclada del Laboratorio de Matemáticas para detectar tus errores típicos y reforzarlos en el acto.",
        ],
    },
    "nodes": [
        # ==================== NIVEL 1: BASES DE ARITMÉTICA ====================
        {
            "slug": "a-valor-posicional",
            "title": "1. Valor posicional, comparación y redondeo (hasta 1 000 000)",
            "level": 1,
            "order_index": 1,
            "summary": "Cuánto vale cada dígito según su lugar, descomponer números grandes y redondear para estimar gastos.",
            "prerequisites": [],
            "metadata": {"lab_tab": "place_value", "est_minutes": 15},
            "items": [
                {
                    "item_type": "worked_example",
                    "title": "Cuánto vale un dígito según su posición",
                    "prompt": "En el precio de un celular usado de $247 850, ¿cuánto representa realmente el dígito 4? Respondé solo con el número.",
                    "answer": "40 000 (cuatro decenas de mil): está en el quinto lugar desde la derecha (4 × 10 000).",
                    "hints": ["Contá los lugares desde la derecha: unidades, decenas, centenas, miles, decenas de mil."],
                    "payload": {
                        "lab_link": "math:place_value",
                        "check": {"type": "numeric", "value": 40000, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Efecto de mover un dígito un lugar a la izquierda",
                    "prompt": "Compará el 6 en $600 con el 6 en $6000. ¿Por cuánto se multiplica su valor al correrlo un lugar a la izquierda? Respondé solo con el número.",
                    "answer": "Por 10: nuestro sistema es decimal (base 10), así que cada posición hacia la izquierda vale 10 veces más.",
                    "hints": ["6000 ÷ 600."],
                    "payload": {"check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "×"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Redondear un precio a la centena más cercana",
                    "prompt": "Una compra en el súper salió $3680. Para llevar la cuenta mentalmente, redondeá 3680 a la centena más cercana (múltiplo de 100). Respondé solo con el número.",
                    "answer": "3700: como la cifra siguiente (8) es 5 o mayor, se redondea hacia arriba (3680 está a solo 20 de 3700).",
                    "hints": ["Mirá la decena (8): si es 5 o más, subís la centena."],
                    "payload": {
                        "lab_link": "math:place_value",
                        "check": {"type": "numeric", "value": 3700, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Redondear a la unidad de mil (presupuesto)",
                    "prompt": "Un pasaje cuesta $84 320. Redondeado al millar más cercano (múltiplo de 1000), ¿cuánto es? Respondé solo con el número.",
                    "answer": "84 000: la centena es 3 (menor que 5), así que queda en 84 000.",
                    "hints": ["Mirá el 3 después del 4: como es menor que 5, redondea hacia abajo."],
                    "payload": {"check": {"type": "numeric", "value": 84000, "tolerance": 0, "unit": ""}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Armar un número desde su forma expandida",
                    "prompt": "Un cuentakilómetros tiene 300 000 + 50 000 + 400 + 20 + 7 kilómetros. ¿Qué número es? Respondé solo con el número (sin espacios).",
                    "answer": "350427 (ojo con el 0 en los miles: no hay unidades de mil, y ese cero guarda el lugar).",
                    "hints": ["Atención: no hay miles sueltos, así que ahí va un 0."],
                    "payload": {"check": {"type": "numeric", "value": 350427, "tolerance": 0, "unit": ""}},
                },
                {
                    "item_type": "recall",
                    "title": "Comparar números grandes sin confundirse",
                    "prompt": "¿Cuál es la manera más rápida y segura de comparar dos números grandes como 409 850 y 410 120?",
                    "answer": "Primero contar cuántos dígitos tienen; si tienen los mismos, comparar dígito por dígito de izquierda a derecha hasta el primero distinto (en las decenas de mil: 1 > 0, así que 410 120 es mayor).",
                    "hints": ["Las posiciones de la izquierda valen muchísimo más que las de la derecha."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Comparar primero cantidad de dígitos y luego de izquierda a derecha",
                                "Comparar primero el último dígito de la derecha",
                                "Sumar todos los dígitos de cada número",
                            ],
                            "correct": 0,
                        },
                    },
                },
            ],
        },
        {
            "slug": "a-suma-resta",
            "title": "2. Sumar y restar números grandes (reagrupar y cálculo mental)",
            "level": 1,
            "order_index": 2,
            "summary": "Sumar llevando, restar pidiendo prestado incluso con ceros y usar trucos mentales para vueltos y presupuestos.",
            "prerequisites": ["a-valor-posicional"],
            "metadata": {"lab_tab": "place_value", "est_minutes": 18},
            "items": [
                {
                    "item_type": "worked_example",
                    "title": "Truco mental de compensación en el supermercado",
                    "prompt": "Comprás un café a $1980 y unas medialunas a $650. Sumalo rápido (pista: pensá 1980 como 2000 − 20). Respondé solo con el número.",
                    "answer": "2630 (2000 + 650 = 2650, y restás los 20 que agregaste → 2630).",
                    "hints": ["Redondeá 1980 a 2000, sumá 650 y devolvé los 20."],
                    "payload": {
                        "lab_link": "math:place_value",
                        "check": {"type": "numeric", "value": 2630, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Vuelto con billete redondo (restar sobre ceros)",
                    "prompt": "Pagás una compra de $1375 con un billete de $5000. ¿Cuánto es tu vuelto? Respondé solo con el número.",
                    "answer": "3625. Truco sin sufrir con los ceros: restá 1 a ambos (4999 − 1374 = 3625) o subí desde 1375: +25 llega a 1400, +600 a 2000, +3000 a 5000 → 3625.",
                    "hints": ["Atajo: 5000 − 1375 da exactamente lo mismo que 4999 − 1374 (sin pedir prestado)."],
                    "payload": {
                        "lab_link": "math:place_value",
                        "check": {"type": "numeric", "value": 3625, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Suma con reagrupación (presupuesto mensual)",
                    "prompt": "Tus dos gastos fijos del mes son $14 850 de internet y $27 680 de luz. ¿Cuánto suman en total? Respondé solo con el número.",
                    "answer": "42 530 (unidades 0, decenas 5+8=13 llevo 1, centenas 1+8+6=15 llevo 1, miles 1+4+7=12 llevo 1, d.mil 1+1+2=4).",
                    "hints": ["Alineá las unidades a la derecha y acordate de sumar lo que llevás."],
                    "payload": {"check": {"type": "numeric", "value": 42530, "tolerance": 0, "unit": ""}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Diferencia de kilómetros en un viaje",
                    "prompt": "Al salir de viaje el odómetro marcaba 48 650 km y al llegar 51 200 km. ¿Cuántos kilómetros recorriste? Respondé solo con el número.",
                    "answer": "2550 km (de 48 650 a 49 000 hay 350; de 49 000 a 51 200 hay 2200 → 2550).",
                    "hints": ["Restá 51 200 − 48 650 (o contá cuánto falta para llegar)."],
                    "payload": {"check": {"type": "numeric", "value": 2550, "tolerance": 0, "unit": "km"}},
                },
                {
                    "item_type": "recall",
                    "title": "Qué significa realmente 'pedir prestado' en una resta",
                    "prompt": "En la resta 52 − 17, tachamos el 5 para dejar 4 y convertimos el 2 en 12. ¿Qué estamos haciendo matemáticamente?",
                    "answer": "Reagrupando el 52 sin cambiar su valor: en vez de 5 decenas + 2 unidades lo escribimos como 4 decenas + 12 unidades (40 + 12 sigue siendo 52).",
                    "hints": ["Una decena se desarma en 10 unidades."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Reescribiendo 50 + 2 como 40 + 12 sin cambiar el valor del número",
                                "Sumándole 10 extra al resultado final",
                                "Cambiando el número 52 por 42 para hacerlo más fácil",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Verificar una resta usando suma",
                    "prompt": "Calculaste 4000 − 1640 y te dio 2460. ¿Cómo comprobás al instante si está bien o mal?",
                    "answer": "Sumando 2460 + 1640 = 4100 ≠ 4000: te sobraron 100, así que la resta correcta es 2360. La suma siempre chequea a la resta.",
                    "hints": ["Si A − B = C, entonces C + B tiene que volver a dar A."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Sumando 2460 + 1640: da 4100, así que está mal (el resultado correcto es 2360)",
                                "Sumando 2460 + 1640: da 4000, así que está bien",
                                "Restando 2460 − 1640 para ver si da 0",
                            ],
                            "correct": 0,
                        },
                    },
                },
            ],
        },
        {
            "slug": "a-intro-multiplicacion",
            "title": "3. Introducción a la multiplicación y tablas (1 dígito)",
            "level": 1,
            "order_index": 3,
            "summary": "Multiplicar como grupos iguales y áreas, reconstruir tablas difíciles con la propiedad distributiva y reglas del 0, 1 y 10.",
            "prerequisites": ["a-suma-resta"],
            "metadata": {"lab_tab": "mult_div", "est_minutes": 18},
            "items": [
                {
                    "item_type": "worked_example",
                    "title": "Reconstruir 7 × 8 sin memorizar a ciegas",
                    "prompt": "Tenés 7 paquetes con 8 tornillos cada uno. Si separás el 8 en 5 + 3 (7×5 + 7×3), ¿cuántos tornillos tenés en total? Respondé solo con el número.",
                    "answer": "56 (7×5 = 35 y 7×3 = 21 → 35 + 21 = 56). Partir un número en partes amigables (propiedad distributiva) salva cualquier tabla trabada.",
                    "hints": ["35 + 21."],
                    "payload": {
                        "lab_link": "math:mult_div",
                        "check": {"type": "numeric", "value": 56, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Truco del 9: pensar en 10 menos 1",
                    "prompt": "Comprás 9 entradas de cine (o 9 metros de cable) a $6 cada unidad (pensá 10×6 − 1×6). ¿Cuánto da 9 × 6? Respondé solo con el número.",
                    "answer": "54 (10 × 6 = 60, menos 6 = 54).",
                    "hints": ["Multiplicá por 10 y restale una vez el 6."],
                    "payload": {"check": {"type": "numeric", "value": 54, "tolerance": 0, "unit": ""}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Área de un piso en baldosas",
                    "prompt": "Un patio tiene 8 filas de 9 baldosas cada una. ¿Cuántas baldosas necesitás comprar? Respondé solo con el número.",
                    "answer": "72 baldosas (8 × 9 = 80 − 8 = 72).",
                    "hints": ["8 × 10 = 80, menos un grupo de 8."],
                    "payload": {"check": {"type": "numeric", "value": 72, "tolerance": 0, "unit": ""}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Horas semanales de práctica",
                    "prompt": "Si practicás guitarra 6 días por semana durante 7 semanas seguidas, ¿cuántos días de práctica acumulaste? Respondé solo con el número.",
                    "answer": "42 días (6 × 7 = 6×5 + 6×2 = 30 + 12 = 42).",
                    "hints": ["6 × 7 = 30 + 12."],
                    "payload": {"check": {"type": "numeric", "value": 42, "tolerance": 0, "unit": "días"}},
                },
                {
                    "item_type": "recall",
                    "title": "Propiedad conmutativa: el orden no cambia el total",
                    "prompt": "¿Por qué 4 cajas de 8 lápices tienen exactamente la misma cantidad que 8 cajas de 4 lápices?",
                    "answer": "Por la propiedad conmutativa (4 × 8 = 8 × 4 = 32): rotar un rectángulo de 4×8 a 8×4 no agrega ni quita cuadraditos. Eso reduce a la mitad las tablas que necesitás recordar.",
                    "hints": ["Imaginá girar un tablero de 4 filas × 8 columnas."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Porque en la multiplicación el orden de los factores no altera el producto (a × b = b × a)",
                                "Solo pasa porque ambos números son pares",
                                "No tienen la misma cantidad: 8 cajas siempre dan más",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Multiplicar por 0 y por 1",
                    "prompt": "¿Cuánto da (8 × 0) + (7 × 1)? Respondé solo con el número.",
                    "answer": "7: cualquier número por 0 da 0 (0 grupos de 8 es nada), y cualquier número por 1 queda igual.",
                    "hints": ["8 × 0 = 0 y 7 × 1 = 7."],
                    "payload": {"check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": ""}},
                },
            ],
        },
        {
            "slug": "a-intro-division",
            "title": "4. Introducción a la división y división con resto",
            "level": 1,
            "order_index": 4,
            "summary": "Repartir en grupos iguales, la división como inversa de multiplicar, el cero prohibido y cómo interpretar el resto en la vida real.",
            "prerequisites": ["a-intro-multiplicacion"],
            "metadata": {"lab_tab": "mult_div", "est_minutes": 18},
            "items": [
                {
                    "item_type": "worked_example",
                    "title": "División exacta repartiendo una cuenta",
                    "prompt": "Entre 6 amigos pagan una pizza grande de $54 (o 54 mil pesos) en partes iguales. ¿Cuánto pone cada uno? Respondé solo con el número.",
                    "answer": "9 (porque 6 × 9 = 54).",
                    "hints": ["¿Qué número multiplicado por 6 da 54?"],
                    "payload": {
                        "lab_link": "math:mult_div",
                        "check": {"type": "numeric", "value": 9, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "División con resto: calcular el sobrante",
                    "prompt": "Tenés 29 empanadas y armás cajas de a 6. ¿Cuántas cajas COMPLETAS armás y cuántas sobran? Respondé solo con cuántas empanadas SOBRAN (el resto).",
                    "answer": "Sobran 5 empanadas: 6 × 4 = 24 (armás 4 cajas completas) y 29 − 24 = 5 de resto.",
                    "hints": ["El múltiplo de 6 más cercano por debajo de 29 es 24."],
                    "payload": {
                        "lab_link": "math:mult_div",
                        "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Interpretar el resto en la vida real (autos para un viaje)",
                    "prompt": "Van 19 personas a un recital y en cada auto entran máximo 4 pasajeros. ¿Cuántos autos necesitan como MÍNIMO para que nadie quede afuera? Respondé solo con el número.",
                    "answer": "5 autos: 19 ÷ 4 = 4 con resto 3. No podés dejar a 3 personas en la vereda, así que necesitás un quinto auto.",
                    "hints": ["4 autos solo llevan 16 personas; ¿qué hacés con las 3 que sobran?"],
                    "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "autos"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Interpretar el resto cuando NO alcanza (cuántos completos podés comprar)",
                    "prompt": "Tenés $35 y cada alfajor cuesta $8. ¿Cuántos alfajores enteros te alcanza para comprar? Respondé solo con el número.",
                    "answer": "4 alfajores (4 × 8 = $32 y te sobran $3, que no alcanzan para un quinto).",
                    "hints": ["Aquí el resto no permite redondear hacia arriba: te falta plata para el 5º."],
                    "payload": {"check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""}},
                },
                {
                    "item_type": "recall",
                    "title": "Por qué NO existe dividir por cero (8 ÷ 0 vs. 0 ÷ 8)",
                    "prompt": "¿Cuál es la diferencia entre 0 ÷ 8 y 8 ÷ 0?",
                    "answer": "0 ÷ 8 = 0 (repartir $0 entre 8 personas da $0 a cada una). En cambio 8 ÷ 0 NO está definido porque ningún número multiplicado por 0 puede dar 8.",
                    "hints": ["Probá invertir con multiplicación: ? × 0 = 8."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "0 ÷ 8 = 0, pero 8 ÷ 0 es indefinido (ningún número por 0 da 8)",
                                "Los dos dan 0",
                                "0 ÷ 8 es indefinido y 8 ÷ 0 = 8",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Comprobar una división con resto",
                    "prompt": "Dividiste un número por 7, dio cociente 8 y resto 3. ¿Cuál era el número original (divisor × cociente + resto)? Respondé solo con el número.",
                    "answer": "59 (7 × 8 + 3 = 56 + 3 = 59).",
                    "hints": ["Multiplicá 7 × 8 y sumale el resto 3."],
                    "payload": {"check": {"type": "numeric", "value": 59, "tolerance": 0, "unit": ""}},
                },
            ],
        },
        # ==================== NIVEL 2: VARIOS DÍGITOS ====================
        {
            "slug": "a-multiplicar-varios-digitos",
            "title": "5. Multiplicar números de varios dígitos (modelo de área)",
            "level": 2,
            "order_index": 5,
            "summary": "Atajos con ceros (×10, ×100), multiplicar descomponiendo en partes (modelo de área) y algoritmo estándar.",
            "prerequisites": ["a-intro-multiplicacion"],
            "metadata": {"lab_tab": "mult_div", "est_minutes": 20},
            "items": [
                {
                    "item_type": "worked_example",
                    "title": "Multiplicar múltiplos de 10 y 100",
                    "prompt": "Un taller compra 40 cajas con 300 resistencias cada una. ¿Cuántas resistencias son en total (40 × 300)? Respondé solo con el número.",
                    "answer": "12 000: multiplicás 4 × 3 = 12 y agregás los 3 ceros (uno del 40 y dos del 300).",
                    "hints": ["4 × 3 y contá todos los ceros al final."],
                    "payload": {
                        "lab_link": "math:mult_div",
                        "check": {"type": "numeric", "value": 12000, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Multiplicar 1 dígito por 2 dígitos descomponiendo",
                    "prompt": "Trabajás 6 horas por día a $47 la hora (o 6 paquetes de 47 g). Calculá 6 × 47 partiendo 47 en 40 + 7. Respondé solo con el número.",
                    "answer": "282 (6 × 40 = 240 y 6 × 7 = 42 → 240 + 42 = 282).",
                    "hints": ["6 × 40 + 6 × 7."],
                    "payload": {
                        "lab_link": "math:mult_div",
                        "check": {"type": "numeric", "value": 282, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Multiplicar 2 dígitos × 2 dígitos (modelo de área)",
                    "prompt": "Una habitación mide 14 baldosas de ancho por 23 de largo. Calculá 14 × 23 (10×23 + 4×23). Respondé solo con el número.",
                    "answer": "322 (10 × 23 = 230 y 4 × 23 = 92 → 230 + 92 = 322).",
                    "hints": ["Separá 14 en 10 + 4 y sumá los dos productos."],
                    "payload": {
                        "lab_link": "math:mult_div",
                        "check": {"type": "numeric", "value": 322, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Gasto anual de una suscripción mensual",
                    "prompt": "Un servicio de streaming cuesta $125 por mes (o $1250 ÷ 10). ¿Cuánto pagás en 12 meses (125 × 12)? Respondé solo con el número.",
                    "answer": "1500 (125 × 10 = 1250, más 125 × 2 = 250 → 1500).",
                    "hints": ["Multiplicá por 10 y sumale el doble."],
                    "payload": {"check": {"type": "numeric", "value": 1500, "tolerance": 0, "unit": ""}},
                },
                {
                    "item_type": "recall",
                    "title": "Por qué se deja un cero en la segunda fila de la multiplicación",
                    "prompt": "Al multiplicar 34 × 25 en papel, primero hacemos 34 × 5 = 170 y abajo ponemos un 0 antes de escribir 34 × 2 = 68 (quedando 680). ¿Por qué va ese cero?",
                    "answer": "Porque el 2 de 25 no vale 2, vale 20 (dos decenas): 34 × 20 = 680. Sin ese cero estarías calculando 34 × 7 en vez de 34 × 25.",
                    "hints": ["Mirá el valor posicional del 2 en el número 25."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Porque ese 2 vale en realidad 20 (dos decenas), así que 34 × 20 = 680",
                                "Por una convención estética para alinear los números",
                                "Para compensar el redondeo del 5",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Estimar antes de multiplicar (detectar errores de ceros)",
                    "prompt": "Hacés 48 × 31 y alguien te dice que da 148. Estimando con 50 × 30, ¿cerca de qué número debería dar en realidad? Respondé solo con 50 × 30.",
                    "answer": "1500 (exacto es 1488). Estimar primero te avisa al instante si te faltó un cero.",
                    "hints": ["5 × 3 = 15, y agregás dos ceros."],
                    "payload": {"check": {"type": "numeric", "value": 1500, "tolerance": 0, "unit": ""}},
                },
            ],
        },
        {
            "slug": "a-dividir-varios-digitos",
            "title": "6. Dividir números de varios dígitos y estimar cocientes",
            "level": 2,
            "order_index": 6,
            "summary": "División larga paso a paso (cocientes parciales), cuotas sin interés, rendimiento por litro y verificación.",
            "prerequisites": ["a-intro-division", "a-multiplicar-varios-digitos"],
            "metadata": {"lab_tab": "mult_div", "est_minutes": 20},
            "items": [
                {
                    "item_type": "worked_example",
                    "title": "Dividir por múltiplos de 10 tachando ceros",
                    "prompt": "Ahorraste $36 000 para pagar cuotas de $400. ¿Cuántas cuotas cubrís (36 000 ÷ 400)? Respondé solo con el número.",
                    "answer": "90 cuotas: tachás dos ceros de ambos números (dividís arriba y abajo por 100) y queda 360 ÷ 4 = 90.",
                    "hints": ["Sacá la misma cantidad de ceros (dos) a los dos números."],
                    "payload": {
                        "lab_link": "math:mult_div",
                        "check": {"type": "numeric", "value": 90, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Calcular cuotas mensuales (división exacta)",
                    "prompt": "Comprás una guitarra de $756 en 6 cuotas sin interés. ¿De cuánto es cada cuota (756 ÷ 6)? Respondé solo con el número.",
                    "answer": "126 (600 ÷ 6 = 100; sobran 156 → 120 ÷ 6 = 20; sobran 36 → 36 ÷ 6 = 6 → 100 + 20 + 6 = 126).",
                    "hints": ["Partí 756 en 600 + 120 + 36 y dividí cada parte por 6."],
                    "payload": {
                        "lab_link": "math:mult_div",
                        "check": {"type": "numeric", "value": 126, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Consumo de nafta (kilómetros por litro)",
                    "prompt": "Recorriste 420 km y cargaste 35 litros para volver a llenar el tanque. ¿Cuántos km rinde tu auto por litro (420 ÷ 35)? Respondé solo con el número.",
                    "answer": "12 km/L (35 × 10 = 350; faltan 70 → 35 × 2 = 70 → 10 + 2 = 12).",
                    "hints": ["10 litros dan 350 km; ¿cuántos litros más cubren los 70 km restantes?"],
                    "payload": {
                        "lab_link": "math:mult_div",
                        "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": "km/L"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "División larga con cero en el medio",
                    "prompt": "Dividís un premio de $824 entre 4 personas. ¿Cuánto recibe cada una (824 ÷ 4)? Respondé solo con el número.",
                    "answer": "206 (800 ÷ 4 = 200 y 24 ÷ 4 = 6; ojo con no olvidarte el 0 de las decenas y escribir 26!).",
                    "hints": ["800 ÷ 4 es 200, así que el resultado tiene que ser mayor a 200 (no 26)."],
                    "payload": {"check": {"type": "numeric", "value": 206, "tolerance": 0, "unit": ""}},
                },
                {
                    "item_type": "worked_example",
                    "title": "División de 3 dígitos por 2 dígitos con resto",
                    "prompt": "Tenés 250 fotos y querés imprimir álbumes de 24 fotos cada uno. ¿Cuántos álbumes COMPLETOS llenás (250 ÷ 24)? Respondé solo con el número de álbumes completos.",
                    "answer": "10 álbumes completos (24 × 10 = 240 fotos, y sobran 10 fotos de resto).",
                    "hints": ["24 × 10 = 240; ¿te alcanza lo que sobra para otro álbum de 24?"],
                    "payload": {"check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": ""}},
                },
                {
                    "item_type": "recall",
                    "title": "Orden del método de cocientes parciales",
                    "prompt": "Ordená los pasos para dividir un número grande (como 468 ÷ 12) por cocientes parciales sin perderte.",
                    "answer": "1) Estimar un múltiplo fácil del divisor → 2) Restarlo del total → 3) Repetir hasta que el sobrante sea menor al divisor → 4) Sumar todos los cocientes parciales.",
                    "hints": ["Vas sacando 'paquetes grandes' del divisor hasta que no entre ninguno más."],
                    "payload": {
                        "check": {
                            "type": "order",
                            "lines": [
                                "Elegir un múltiplo cómodo del divisor (ej. ×10, ×20) que no se pase",
                                "Restar ese bloque del dividendo",
                                "Repetir con lo que sobra hasta que el resto sea menor al divisor",
                                "Sumar todos los cocientes parciales obtenidos",
                            ],
                        },
                    },
                },
            ],
        },
        # ==================== NIVEL 3: FRACCIONES COMPLETAS ====================
        {
            "slug": "a-entender-fracciones",
            "title": "7. Entender las fracciones, equivalencias y números mixtos",
            "level": 3,
            "order_index": 7,
            "summary": "Qué significa numerador y denominador, recta numérica, fracciones equivalentes, simplificar y números mixtos.",
            "prerequisites": ["a-intro-division"],
            "metadata": {"lab_tab": "fractions", "est_minutes": 20},
            "items": [
                {
                    "item_type": "recall",
                    "title": "Qué indica el denominador vs. el numerador",
                    "prompt": "Una receta pide 3/4 de taza de harina. ¿Qué indica el 4 (denominador) y qué indica el 3 (numerador)?",
                    "answer": "El denominador (4) dice en cuántas partes IGUALES se divide el entero; el numerador (3) dice cuántas de esas partes tomás.",
                    "hints": ["Abajo = tamaño/cantidad de partes del entero; arriba = cuántas elegís."],
                    "payload": {
                        "lab_link": "math:fractions",
                        "check": {
                            "type": "choice",
                            "options": [
                                "4 = en cuántas partes iguales se parte la taza; 3 = cuántas partes tomás",
                                "4 = cuántas tazas enteras usás; 3 = cuántas sobran",
                                "3 = tamaño de la parte; 4 = cantidad de partes tomadas",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Simplificar una fracción a su forma más simple",
                    "prompt": "Cortaste una pizza en 12 porciones y comiste 8 (8/12). Escribí esa fracción simplificada al máximo (ej. 1/2).",
                    "answer": "2/3: dividís numerador y denominador por su mayor divisor común (4): 8÷4 = 2 y 12÷4 = 3.",
                    "hints": ["Tanto 8 como 12 se pueden dividir por 4."],
                    "payload": {
                        "lab_link": "math:fractions",
                        "check": {"type": "text", "accept": ["2/3"]},
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Comparar fracciones con el mismo numerador",
                    "prompt": "¿Qué porción de torta es más grande: 1/3 o 1/8?",
                    "answer": "1/3 es mucho más grande: cuanto más grande es el denominador, entre más personas repartís la misma torta y más chica sale cada porción.",
                    "hints": ["¿Preferís repartir una pizza entre 3 amigos o entre 8?"],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "1/3 (repartir entre menos da porciones más grandes)",
                                "1/8 (porque 8 es mayor que 3)",
                                "Valen exactamente lo mismo",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Fracciones equivalentes (ajustar a otro denominador)",
                    "prompt": "Si 3/4 = ?/20, ¿qué número va en el lugar de '?' para que valgan exactamente lo mismo? Respondé solo con el número.",
                    "answer": "15: para pasar de 4 a 20 multiplicaste por 5, así que multiplicás arriba también por 5 (3 × 5 = 15).",
                    "hints": ["Lo que multiplicás abajo, multiplicalo arriba."],
                    "payload": {
                        "lab_link": "math:fractions",
                        "check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Fracción impropia a número mixto",
                    "prompt": "Compraste 7 cuartos de kilo de helado (7/4 kg). ¿Cuántos kilos enteros tenés y cuántos cuartos sobran? Escribí solo los kilos ENTEROS.",
                    "answer": "1 kilo entero (y sobran 3/4 kg): 7 ÷ 4 = 1 con resto 3 → 7/4 = 1 y 3/4.",
                    "hints": ["4 cuartos hacen 1 kilo entero."],
                    "payload": {"check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": "kg"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Número mixto a fracción impropia",
                    "prompt": "Una película dura 2 horas y media (2 y 1/2 h). ¿Cuántas medias horas son en total (fracción ?/2)? Escribí la fracción completa (ej. 3/2).",
                    "answer": "5/2: las 2 horas enteras son 4/2, más 1/2 = 5/2.",
                    "hints": ["2 × 2 + 1 sobre 2."],
                    "payload": {"check": {"type": "text", "accept": ["5/2"]}},
                },
            ],
        },
        {
            "slug": "a-sumar-restar-fracciones-igual",
            "title": "8. Sumar y restar fracciones con igual denominador",
            "level": 3,
            "order_index": 8,
            "summary": "Sumar y restar porciones del mismo tamaño, restar a un entero y operar números mixtos en recetas y tiempos.",
            "prerequisites": ["a-entender-fracciones"],
            "metadata": {"lab_tab": "fractions", "est_minutes": 18},
            "items": [
                {
                    "item_type": "worked_example",
                    "title": "Sumar fracciones con igual denominador",
                    "prompt": "En una receta usás 2/8 de taza de aceite para la masa y 4/8 para el relleno. ¿Qué fracción total de taza usaste? Escribila simplificada (ej. 1/2).",
                    "answer": "3/4: primero sumás numeradores dejando el denominador igual (2/8 + 4/8 = 6/8) y luego simplificás por 2 → 3/4.",
                    "hints": ["2/8 + 4/8 = 6/8; recordá simplificar."],
                    "payload": {
                        "lab_link": "math:fractions",
                        "check": {"type": "text", "accept": ["3/4"]},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Restar una fracción a un entero",
                    "prompt": "Tenías 1 tanque lleno de nafta y gastaste 3/8 en el viaje de ida. ¿Qué fracción del tanque te queda? Escribila como fracción (ej. 1/2).",
                    "answer": "5/8: convertís 1 entero en 8/8 y restás 8/8 − 3/8 = 5/8.",
                    "hints": ["Pensá el 1 entero como 8/8."],
                    "payload": {"check": {"type": "text", "accept": ["5/8"]}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Sumar números mixtos (horas de estudio)",
                    "prompt": "Estudiaste 1 y 3/4 horas a la mañana y 2 y 3/4 horas a la tarde. ¿Cuántas horas estudiaste en total? Respondé como decimal o fracción (ej. 2.5 o 5/2).",
                    "answer": "4.5 horas (4 y 1/2): enteros 1+2 = 3; fracciones 3/4 + 3/4 = 6/4 = 1 y 2/4 = 1.5 → 3 + 1.5 = 4.5.",
                    "hints": ["Sumá enteros por un lado y cuartos por otro: 6/4 es 1 entero y medio."],
                    "payload": {"check": {"type": "numeric", "value": 4.5, "tolerance": 0.01, "unit": "h"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Restar con reagrupación en madera (carpintería)",
                    "prompt": "Tenés un listón de 3 metros y cortás un tramo de 1 y 1/4 m (5/4 m). ¿Cuántos metros te sobran? Respondé como decimal o fracción (ej. 2.5 o 5/2).",
                    "answer": "1.75 m (1 y 3/4 m): 3 − 1 = 2 m, y 2 − 1/4 = 1 y 3/4 m = 1.75 m.",
                    "hints": ["Restá primero el metro entero y después 1/4 al metro que queda."],
                    "payload": {"check": {"type": "numeric", "value": 1.75, "tolerance": 0.01, "unit": "m"}},
                },
                {
                    "item_type": "recall",
                    "title": "Error clásico: por qué NO se suman los denominadores",
                    "prompt": "Alguien dice que 1/2 pizza + 1/2 pizza = 2/4 pizza. ¿Por qué es imposible?",
                    "answer": "Porque 2/4 es otra vez media pizza: el denominador indica el tamaño de cada porción (medios), no se suma. Media pizza + media pizza = 2/2 = 1 pizza entera.",
                    "hints": ["1 manzana + 1 manzana = 2 manzanas, no 2 'doble-manzanas'."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Porque el denominador indica el tamaño de la porción y se conserva: 1/2 + 1/2 = 2/2 = 1",
                                "Porque en fracciones solo se puede sumar si los denominadores son impares",
                                "Sí se suman los denominadores, pero falta multiplicar por 2",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Resta de fracciones con simplificación",
                    "prompt": "Una jarra tenía 9/10 de litro de jugo y serviste 4/10 de litro. ¿Qué fracción de litro quedó, simplificada al máximo?",
                    "answer": "1/2 litro: 9/10 − 4/10 = 5/10, y dividiendo arriba y abajo por 5 queda 1/2.",
                    "hints": ["9 − 4 = 5 décimos; simplificá 5/10."],
                    "payload": {"check": {"type": "text", "accept": ["1/2"]}},
                },
            ],
        },
        {
            "slug": "a-sumar-restar-fracciones-distinto",
            "title": "9. Sumar y restar fracciones con distinto denominador",
            "level": 3,
            "order_index": 9,
            "summary": "Buscar un denominador común (MCM), convertir a equivalentes, operar y simplificar sin trampas.",
            "prerequisites": ["a-sumar-restar-fracciones-igual"],
            "metadata": {"lab_tab": "fractions", "est_minutes": 20},
            "items": [
                {
                    "item_type": "worked_example",
                    "title": "Sumar medios y tercios",
                    "prompt": "Caminaste 1/2 km hasta la parada y después 1/3 km hasta el trabajo. ¿Qué fracción de km caminaste en total? Escribila como fracción (ej. 3/4).",
                    "answer": "5/6 km: denominador común 6 → 1/2 = 3/6 y 1/3 = 2/6 → 3/6 + 2/6 = 5/6.",
                    "hints": ["Pasá ambos a sextos (denominador 6)."],
                    "payload": {
                        "lab_link": "math:fractions",
                        "check": {"type": "text", "accept": ["5/6"]},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Sumar tercios y cuartos (visual en Laboratorio)",
                    "prompt": "Mezclás 2/3 de litro de pintura blanca con 1/4 de litro de entonador. ¿Qué fracción de litro tenés en total?",
                    "answer": "11/12 L: común denominador 12 → 8/12 + 3/12 = 11/12.",
                    "hints": ["2/3 = 8/12 y 1/4 = 3/12."],
                    "payload": {
                        "lab_link": "math:fractions",
                        "check": {"type": "text", "accept": ["11/12"]},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Restar fracciones con distinto denominador",
                    "prompt": "Una botella tenía 3/4 de litro de agua y tomaste 1/3 de litro. ¿Qué fracción de litro queda?",
                    "answer": "5/12 L: común denominador 12 → 9/12 − 4/12 = 5/12.",
                    "hints": ["Convertí 3/4 y 1/3 a doceavos."],
                    "payload": {
                        "lab_link": "math:fractions",
                        "check": {"type": "text", "accept": ["5/12"]},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Cuando un denominador ya es múltiplo del otro",
                    "prompt": "Sumá 1/2 + 3/8 (pista: solo necesitás convertir una de las dos fracciones). Escribí la fracción resultado.",
                    "answer": "7/8: como 8 es múltiplo de 2, pasás 1/2 = 4/8 y sumás 4/8 + 3/8 = 7/8.",
                    "hints": ["Usá 8 como común denominador: 1/2 = 4/8."],
                    "payload": {"check": {"type": "text", "accept": ["7/8"]}},
                },
                {
                    "item_type": "recall",
                    "title": "Orden para sumar fracciones con distinto denominador",
                    "prompt": "Ordená los pasos correctos para resolver 2/3 + 1/4.",
                    "answer": "1) Encontrar un denominador común → 2) Convertir cada fracción a equivalente → 3) Sumar solo los numeradores → 4) Simplificar si se puede.",
                    "hints": ["No se puede sumar hasta que los pedazos tengan el mismo tamaño."],
                    "payload": {
                        "lab_link": "math:fractions",
                        "check": {
                            "type": "order",
                            "lines": [
                                "Buscar un denominador común (mcm)",
                                "Reescribir cada fracción como equivalente con ese denominador",
                                "Sumar solo los numeradores manteniendo el denominador común",
                                "Simplificar el resultado si numerador y denominador comparten divisor",
                            ],
                        },
                    },
                },
                {
                    "item_type": "drill",
                    "title": "Práctica en el Laboratorio de Matemáticas: Fracciones",
                    "prompt": "Abrí el Laboratorio de Matemáticas en 'Fracciones', hacé el ejemplo desvanecido y resolvé al menos 5 ejercicios con 80%+ de precisión.",
                    "answer": "Al registrar 5 ejercicios en el Laboratorio, la app guarda tu precisión y te sugiere calificación automáticamente.",
                    "hints": ["Acordate de simplificar cada fracción antes de enviar."],
                    "payload": {
                        "lab_link": "math:fractions",
                        "lab_metric": {"type": "math_accuracy", "good": 80, "easy": 95, "unit": "%"},
                    },
                },
            ],
        },
        {
            "slug": "a-multiplicar-fracciones",
            "title": "10. Multiplicar fracciones ('una parte de otra')",
            "level": 3,
            "order_index": 10,
            "summary": "Entender multiplicar por una fracción como 'tomar una parte de', simplificar cruzado y ajustar recetas o descuentos.",
            "prerequisites": ["a-entender-fracciones"],
            "metadata": {"lab_tab": "fractions", "est_minutes": 18},
            "items": [
                {
                    "item_type": "worked_example",
                    "title": "Fracción de una cantidad entera",
                    "prompt": "Un pantalón de $400 tiene un descuento de 1/4 del precio (o pagás 3/4). ¿Cuánto es 3/4 de 400? Respondé solo con el número.",
                    "answer": "300: 1/4 de 400 es 100 (400 ÷ 4), así que 3/4 son 3 × 100 = 300.",
                    "hints": ["Dividí 400 por 4 y multiplicá por 3."],
                    "payload": {
                        "lab_link": "math:fractions",
                        "check": {"type": "numeric", "value": 300, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Reducir una receta a la mitad",
                    "prompt": "Una receta lleva 3/4 de taza de azúcar, pero querés hacer solo la MITAD (1/2 × 3/4). ¿Qué fracción de taza necesitás?",
                    "answer": "3/8 de taza: multiplicás arriba con arriba (1×3=3) y abajo con abajo (2×4=8). ¡Para multiplicar NO hace falta común denominador!",
                    "hints": ["Numerador × numerador sobre denominador × denominador."],
                    "payload": {
                        "lab_link": "math:fractions",
                        "check": {"type": "text", "accept": ["3/8"]},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Simplificar cruzado antes de multiplicar",
                    "prompt": "Calculá 2/3 × 3/5 y escribilo simplificado al máximo.",
                    "answer": "2/5: podés cancelar el 3 de arriba con el 3 de abajo antes de multiplicar (o hacer 6/15 y dividir por 3 → 2/5).",
                    "hints": ["2×3 / 3×5 = 6/15 → simplificá por 3."],
                    "payload": {"check": {"type": "text", "accept": ["2/5"]}},
                },
                {
                    "item_type": "recall",
                    "title": "¿Multiplicar siempre agranda el resultado?",
                    "prompt": "Multiplicás un número positivo (por ejemplo 20) por una fracción menor que 1 (como 3/4). ¿El resultado es mayor o menor que 20?",
                    "answer": "MENOR que 20 (da 15): multiplicar por algo menor que 1 significa tomar solo una parte del número original.",
                    "hints": ["Pensá en 20 × 1/2 = 10."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Menor que 20, porque estás tomando una parte de 20",
                                "Siempre mayor que 20, porque multiplicar agranda",
                                "Igual a 20",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Tiempo efectivo de un entrenamiento",
                    "prompt": "Entrenás 2/3 de hora (40 min) y dedicás 3/4 de ese tiempo a técnica. ¿Qué fracción de hora dedicaste a técnica (2/3 × 3/4), simplificada?",
                    "answer": "1/2 hora (30 min): (2×3)/(3×4) = 6/12 = 1/2.",
                    "hints": ["Cancelá el 3 con el 3 y te queda 2/4 = 1/2."],
                    "payload": {"check": {"type": "text", "accept": ["1/2"]}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Multiplicar un número mixto por un entero",
                    "prompt": "Cada tabla mide 1 y 1/2 metros (3/2 m). Si ponés 4 tablas una atrás de otra, ¿cuántos metros cubrís? Respondé solo con el número en m.",
                    "answer": "6 m (4 × 1 = 4 más 4 × 1/2 = 2 → 6 m; o 3/2 × 4 = 12/2 = 6).",
                    "hints": ["4 enteros + 4 mitades."],
                    "payload": {"check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": "m"}},
                },
            ],
        },
        {
            "slug": "a-dividir-fracciones",
            "title": "11. Dividir fracciones (cuántas veces cabe y recíproco)",
            "level": 3,
            "order_index": 11,
            "summary": "Entender qué significa dividir por una fracción ('¿cuántas porciones entran?') y por qué se multiplica por el recíproco.",
            "prerequisites": ["a-multiplicar-fracciones"],
            "metadata": {"lab_tab": "fractions", "est_minutes": 18},
            "items": [
                {
                    "item_type": "worked_example",
                    "title": "Intuición: ¿cuántos cuartos de kilo salen de 3 kilos?",
                    "prompt": "Compraste 3 kg de café y lo fraccionás en bolsitas de 1/4 kg (3 ÷ 1/4). ¿Cuántas bolsitas llenás? Respondé solo con el número.",
                    "answer": "12 bolsitas: en cada kilo entran 4 cuartos, así que en 3 kilos entran 3 × 4 = 12. Dividir por una fracción menor que 1 AGRANDA el resultado.",
                    "hints": ["En 1 kg caben 4 bolsitas de 1/4 kg."],
                    "payload": {
                        "lab_link": "math:fractions",
                        "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Dividir una fracción por un entero (repartir sobras)",
                    "prompt": "Quedó 1/2 torta y la repartís en partes iguales entre 3 amigos (1/2 ÷ 3). ¿Qué fracción de la torta entera recibe cada uno?",
                    "answer": "1/6: repartir la mitad entre 3 es lo mismo que tomar 1/3 de 1/2 → 1/2 × 1/3 = 1/6.",
                    "hints": ["Cada mitad se parte en 3 pedazos → 6 pedazos en toda la torta."],
                    "payload": {"check": {"type": "text", "accept": ["1/6"]}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Dividir fracción por fracción (recíproco)",
                    "prompt": "Tenés 3/4 de litro de pintura y cada maceta necesita 1/8 de litro (3/4 ÷ 1/8). ¿Cuántas macetas podés pintar? Respondé solo con el número.",
                    "answer": "6 macetas: 3/4 × 8/1 = 24/4 = 6 (también ves que 3/4 = 6/8, así que caben exactamente seis octavos).",
                    "hints": ["Multiplicá la primera fracción por la segunda dada vuelta (8/1)."],
                    "payload": {
                        "lab_link": "math:fractions",
                        "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "División general de dos fracciones",
                    "prompt": "Calculá 2/3 ÷ 4/5 y escribilo como fracción simplificada.",
                    "answer": "5/6: das vuelta la segunda → 2/3 × 5/4 = 10/12, y simplificando por 2 queda 5/6.",
                    "hints": ["Dejá 2/3 quieto, cambiá ÷ por ×, invertí 4/5 a 5/4 y simplificá."],
                    "payload": {"check": {"type": "text", "accept": ["5/6"]}},
                },
                {
                    "item_type": "recall",
                    "title": "Por qué dividir por 1/2 es multiplicar por 2",
                    "prompt": "¿Por qué dividir cualquier número por 1/2 da el DOBLE del número?",
                    "answer": "Porque preguntar '¿cuántas mitades caben en N?' siempre tiene como respuesta 2×N: en cada entero caben 2 mitades (multiplicar por el recíproco de 1/2, que es 2/1).",
                    "hints": ["¿Cuántas monedas de $0.50 forman $10?"],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Porque en cada unidad caben 2 mitades, así que preguntar cuántas mitades entran da el doble",
                                "Es un error: dividir por 1/2 da la mitad",
                                "Solo funciona con números pares",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Cortar un cable en tramos fraccionarios",
                    "prompt": "Tenés un rollo de 6 metros de cable y cortás tramos de 3/4 m (6 ÷ 3/4). ¿Cuántos tramos obtenés? Respondé solo con el número.",
                    "answer": "8 tramos: 6 × 4/3 = 24/3 = 8.",
                    "hints": ["6 × 4 ÷ 3."],
                    "payload": {"check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": ""}},
                },
            ],
        },
        # ==================== NIVEL 4: DECIMALES Y POTENCIAS DE 10 ====================
        {
            "slug": "a-decimales-valor-posicional",
            "title": "12. Decimales, valor posicional y relación con fracciones",
            "level": 4,
            "order_index": 12,
            "summary": "Décimos, centésimos y milésimos, comparar decimales sin caer en trampas, redondear y equivalencias con fracciones.",
            "prerequisites": ["a-entender-fracciones"],
            "metadata": {"lab_tab": "decimals", "est_minutes": 18},
            "items": [
                {
                    "item_type": "recall",
                    "title": "Trampa clásica al comparar decimales: 0.4 vs. 0.35",
                    "prompt": "Un atleta corre un tramo en 0.4 segundos y otro en 0.35 segundos. ¿Cuál número es MAYOR?",
                    "answer": "0.4 es mayor que 0.35: pensalo como dinero ($0.40 vs. $0.35). Tener más dígitos después de la coma NO hace más grande al número.",
                    "hints": ["Agregá un cero al final de 0.4 → 0.40."],
                    "payload": {
                        "lab_link": "math:decimals",
                        "check": {
                            "type": "choice",
                            "options": [
                                "0.4 (equivale a 0.40, mayor que 0.35)",
                                "0.35 (porque 35 es mayor que 4)",
                                "Son iguales",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Fracciones cotidianas pasadas a decimal",
                    "prompt": "Comprás 3/4 kg de pan en una balanza digital. ¿Qué número muestra la pantalla en kg? Respondé en decimal (ej. 0.5).",
                    "answer": "0.75 kg (3 ÷ 4 = 0.75; los tres básicos para saber de memoria: 1/4 = 0.25, 1/2 = 0.5, 3/4 = 0.75).",
                    "hints": ["Un cuarto es 0.25; tres cuartos es 3 × 0.25."],
                    "payload": {
                        "lab_link": "math:decimals",
                        "check": {"type": "text", "accept": ["0.75", "0.750", "0.75 kg", "0.750 kg"]},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Decimal a fracción simplificada",
                    "prompt": "Un tornillo mide 0.4 cm (4 décimos = 4/10). Escribí esa medida como fracción simplificada al máximo.",
                    "answer": "2/5: 0.4 = 4/10, y dividiendo por 2 queda 2/5.",
                    "hints": ["4/10 simplificado por 2."],
                    "payload": {"check": {"type": "text", "accept": ["2/5"]}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Redondear a la décima (1 decimal)",
                    "prompt": "Un termómetro digital marca 37.68°C. Redondeado a 1 decimal (décimas), ¿cuánto es? Respondé solo con el número.",
                    "answer": "37.7°C: el segundo decimal es 8 (≥ 5), así que el 6 sube a 7.",
                    "hints": ["Mirá el dígito de los centésimos (8)."],
                    "payload": {"check": {"type": "numeric", "value": 37.7, "tolerance": 0, "unit": "°C"}},
                },
                {
                    "item_type": "recall",
                    "title": "Valor de la posición de los milésimos",
                    "prompt": "En una resistencia medida con tester de precisión como 4.725 kΩ, ¿qué lugar ocupa el dígito 5?",
                    "answer": "Milésimos (5/1000 = 0.005): primer lugar décimos, segundo centésimos, tercero milésimos.",
                    "hints": ["Después de la coma: décimos (1º), centésimos (2º), milésimos (3º)."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": ["Décimos (1/10)", "Centésimos (1/100)", "Milésimos (1/1000)"],
                            "correct": 2,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Convertir 1/8 a decimal",
                    "prompt": "La mitad de 1/4 (0.25) es 1/8. ¿Cuánto vale 1/8 escrito en decimal (ej. 0.5)?",
                    "answer": "0.125 (0.25 ÷ 2 = 0.125).",
                    "hints": ["Sacale la mitad a 0.250."],
                    "payload": {"check": {"type": "text", "accept": ["0.125", "0.1250"]}},
                },
            ],
        },
        {
            "slug": "a-sumar-restar-decimales",
            "title": "13. Sumar y restar decimales (dinero y medidas)",
            "level": 4,
            "order_index": 13,
            "summary": "Alinear siempre el punto decimal, rellenar con ceros al final y resolver tickets, vueltos y mediciones.",
            "prerequisites": ["a-decimales-valor-posicional"],
            "metadata": {"lab_tab": "decimals", "est_minutes": 18},
            "items": [
                {
                    "item_type": "worked_example",
                    "title": "Sumar decimales con distinta cantidad de cifras",
                    "prompt": "Cargás dos archivos de 1.8 GB y 0.45 GB en un pendrive. ¿Cuántos GB ocupan juntos (1.8 + 0.45)? Respondé solo con el número.",
                    "answer": "2.25 GB: alineás la coma (1.80 + 0.45 = 2.25). Si no alineás, caés en la trampa de sumar 8 + 5.",
                    "hints": ["Escribí 1.8 como 1.80 antes de sumar."],
                    "payload": {
                        "lab_link": "math:decimals",
                        "check": {"type": "numeric", "value": 2.25, "tolerance": 0.005, "unit": "GB"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Restar un decimal a un número entero (vuelto)",
                    "prompt": "Pagás un café de $3.65 con un billete de $10. ¿Cuánto te devuelven (10 − 3.65)? Respondé solo con el número.",
                    "answer": "6.35: pensá 10 como 10.00 → de 3.65 a 4.00 faltan 0.35, y de 4 a 10 faltan 6 → 6.35.",
                    "hints": ["Poné 10.00 − 3.65 alineando la coma."],
                    "payload": {
                        "lab_link": "math:decimals",
                        "check": {"type": "numeric", "value": 6.35, "tolerance": 0.005, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Diferencia de voltaje en una batería",
                    "prompt": "Una batería de litio cargada mide 4.20 V y descargada 3.35 V. ¿Cuántos voltios cayó (4.20 − 3.35)? Respondé solo con el número.",
                    "answer": "0.85 V (de 3.35 a 4.00 hay 0.65, más 0.20 = 0.85 V).",
                    "hints": ["Restá 4.20 − 3.35 como si fueran centavos (420 − 335 = 85 centavos)."],
                    "payload": {
                        "lab_link": "math:decimals",
                        "check": {"type": "numeric", "value": 0.85, "tolerance": 0.005, "unit": "V"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Sumar tres precios de ticket",
                    "prompt": "Comprás pan ($2.40), leche ($1.85) y fruta ($3.75). ¿Cuánto da el total del ticket? Respondé solo con el número.",
                    "answer": "8 (o 8.00): 1.85 + 3.75 = 5.60, y 5.60 + 2.40 = 8.00.",
                    "hints": ["Agrupá primero 1.85 + 3.75 = 5.60."],
                    "payload": {"check": {"type": "numeric", "value": 8, "tolerance": 0.005, "unit": ""}},
                },
                {
                    "item_type": "recall",
                    "title": "Regla de oro al sumar o restar decimales",
                    "prompt": "¿Por qué hay que alinear las comas decimales (y NO el borde derecho de los números) al sumar 4.5 + 0.28?",
                    "answer": "Para sumar décimos con décimos y centésimos con centésimos (mismo valor posicional). Si alineás a la derecha sumarías 5 décimos con 8 centésimos como si valieran lo mismo.",
                    "hints": ["No podés sumar monedas de 10 centavos con monedas de 1 centavo como si fueran iguales."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "Para sumar cada posición con su igual (unidades con unidades, décimos con décimos)",
                                "Porque siempre hay que tener la misma cantidad de dígitos antes de la coma",
                                "En realidad da lo mismo alinear a la derecha que por la coma",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Medida con calibre (milímetros)",
                    "prompt": "Una pieza debe medir 12.5 mm pero mide 12.82 mm. ¿Cuántos milímetros sobran (12.82 − 12.5)? Respondé solo con el número.",
                    "answer": "0.32 mm (12.82 − 12.50 = 0.32).",
                    "hints": ["Completá 12.5 como 12.50."],
                    "payload": {"check": {"type": "numeric", "value": 0.32, "tolerance": 0.005, "unit": "mm"}},
                },
            ],
        },
        {
            "slug": "a-multiplicar-dividir-decimales",
            "title": "14. Multiplicar y dividir decimales en la vida real",
            "level": 4,
            "order_index": 14,
            "summary": "Ubicar la coma contando decimales, dividir corriendo la coma para tener divisor entero y calcular precios por kilo o litro.",
            "prerequisites": ["a-sumar-restar-decimales", "a-multiplicar-varios-digitos"],
            "metadata": {"lab_tab": "decimals", "est_minutes": 20},
            "items": [
                {
                    "item_type": "worked_example",
                    "title": "Precio por peso en la verdulería",
                    "prompt": "Las manzanas cuestan $3.20 el kilo y llevás 2.5 kg. ¿Cuánto pagás (3.2 × 2.5)? Respondé solo con el número.",
                    "answer": "8 ($8.00): hacés 32 × 25 = 800 y corrés la coma 2 lugares (1 decimal + 1 decimal) → 8.00. Chequeo rápido: 3 × 2.5 = 7.5, así que 8 tiene total sentido.",
                    "hints": ["Multiplicá 32 × 25 = 800 y colocá la coma usando estimación (cerca de 3 × 2.5)."],
                    "payload": {
                        "lab_link": "math:decimals",
                        "check": {"type": "numeric", "value": 8, "tolerance": 0.01, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Multiplicar dos decimales chicos",
                    "prompt": "Calculá 0.3 × 0.4 (pensá: tres décimos de cuatro décimos). Respondé solo con el número.",
                    "answer": "0.12 (3 × 4 = 12, con 1 + 1 = 2 lugares decimales → 0.12; ojo con escribir 1.2!).",
                    "hints": ["Contá el total de cifras decimales entre los dos factores: 1 + 1 = 2."],
                    "payload": {
                        "lab_link": "math:decimals",
                        "check": {"type": "numeric", "value": 0.12, "tolerance": 0.002, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Dividir un gasto con decimales entre amigos",
                    "prompt": "Un pedido de comida salió $18.60 entre 3 personas. ¿Cuánto pone cada una (18.60 ÷ 3)? Respondé solo con el número.",
                    "answer": "6.2 (o $6.20): 18 ÷ 3 = 6 y 0.60 ÷ 3 = 0.20.",
                    "hints": ["Dividí los pesos por un lado y los centavos por otro."],
                    "payload": {
                        "lab_link": "math:decimals",
                        "check": {"type": "numeric", "value": 6.2, "tolerance": 0.01, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Dividir por un decimal corriendo la coma",
                    "prompt": "Tenés 6 litros de detergente y cargás botellitas de 0.5 L (6 ÷ 0.5). ¿Cuántas botellitas llenás? Respondé solo con el número.",
                    "answer": "12 botellitas: corrés la coma 1 lugar en ambos números (×10) para volver entero el divisor → 60 ÷ 5 = 12.",
                    "hints": ["Multiplicá ambos por 10: 6 ÷ 0.5 = 60 ÷ 5."],
                    "payload": {
                        "lab_link": "math:decimals",
                        "check": {"type": "numeric", "value": 12, "tolerance": 0.01, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Precio por litro de nafta",
                    "prompt": "Cargaste 2.4 litros en un bidón y pagaste $3.60. ¿Cuánto cuesta cada litro (3.60 ÷ 2.4)? Respondé solo con el número.",
                    "answer": "1.5 ($1.50/L): corrés la coma un lugar en ambos → 36 ÷ 24 = 3/2 = 1.5.",
                    "hints": ["Pasalo a 36 ÷ 24 simplificando por 12 → 3 ÷ 2."],
                    "payload": {
                        "lab_link": "math:decimals",
                        "check": {"type": "numeric", "value": 1.5, "tolerance": 0.01, "unit": ""},
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Cómo saber dónde va la coma al dividir 4.8 ÷ 0.12",
                    "prompt": "Para hacer 4.8 ÷ 0.12 sin equivocarte, ¿en qué división equivalente con divisor entero conviene transformarla?",
                    "answer": "480 ÷ 12 (= 40): multiplicás ambos números por 100 (corrés la coma 2 lugares a la derecha en ambos) para que 0.12 se vuelva el entero 12.",
                    "hints": ["Mové la coma la MISMA cantidad de lugares en los dos números hasta que el divisor no tenga coma."],
                    "payload": {
                        "check": {
                            "type": "choice",
                            "options": [
                                "480 ÷ 12 (multiplicando ambos por 100)",
                                "48 ÷ 12 (sacándole la coma a cada uno por separado)",
                                "4.8 ÷ 12 (solo cambiando el divisor)",
                            ],
                            "correct": 0,
                        },
                    },
                },
            ],
        },
        {
            "slug": "a-exponentes-potencias-10",
            "title": "15. Exponentes, potencias de 10 y orden de operaciones",
            "level": 4,
            "order_index": 15,
            "summary": "Qué significa un exponente, correr la coma con potencias de 10 (kilo/mili/GB) y resolver operaciones combinadas (PEMDAS).",
            "prerequisites": ["a-multiplicar-dividir-decimales"],
            "metadata": {"lab_tab": "powers", "est_minutes": 20},
            "items": [
                {
                    "item_type": "worked_example",
                    "title": "Significado de un exponente (evitar el error 2³ = 6)",
                    "prompt": "Una bacteria se duplica cada hora durante 4 horas (2⁴ = 2 × 2 × 2 × 2). ¿Cuántas bacterias hay al final? Respondé solo con el número.",
                    "answer": "16 (2×2=4, ×2=8, ×2=16). Ojo: 2⁴ NO es 2 × 4 = 8.",
                    "hints": ["Multiplicá el 2 por sí mismo 4 veces."],
                    "payload": {
                        "lab_link": "math:powers",
                        "check": {"type": "numeric", "value": 16, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Multiplicar un decimal por una potencia de 10",
                    "prompt": "Un sensor lee 3.45 × 10³ (equivale a 3.45 kΩ en ohmios). ¿Qué número entero es? Respondé solo con el número.",
                    "answer": "3450: multiplicar por 10³ (1000) corre la coma 3 lugares hacia la derecha.",
                    "hints": ["Corré la coma 3 lugares a la derecha, completando con un 0."],
                    "payload": {
                        "lab_link": "math:powers",
                        "check": {"type": "numeric", "value": 3450, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Dividir por una potencia de 10",
                    "prompt": "Tenés 470 ÷ 10² (como pasar 470 cm a metros). ¿Cuánto da? Respondé solo con el número.",
                    "answer": "4.7: dividir por 10² (100) corre la coma 2 lugares hacia la izquierda.",
                    "hints": ["Dividí 470 por 100."],
                    "payload": {
                        "lab_link": "math:powers",
                        "check": {"type": "numeric", "value": 4.7, "tolerance": 0.005, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Orden de operaciones (PEMDAS): multiplicación antes que suma",
                    "prompt": "Comprás 1 café ($5) y 3 medialunas ($2 cada una): 5 + 3 × 2. ¿Cuánto da? Respondé solo con el número.",
                    "answer": "11: primero 3 × 2 = 6, después 5 + 6 = 11 (NO (5+3)×2 = 16).",
                    "hints": ["Multiplicá antes de sumar."],
                    "payload": {
                        "lab_link": "math:integers",
                        "check": {"type": "numeric", "value": 11, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Paréntesis y exponentes juntos",
                    "prompt": "Calculá 2 + 3 × (4 − 1)². Respondé solo con el número.",
                    "answer": "29: paréntesis (4−1)=3 → exponente 3²=9 → multiplicación 3×9=27 → suma 2+27=29.",
                    "hints": ["Orden: Paréntesis → Exponentes → Multiplicación → Suma."],
                    "payload": {
                        "lab_link": "math:powers",
                        "check": {"type": "numeric", "value": 29, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "recall",
                    "title": "Orden correcto de las operaciones combinadas",
                    "prompt": "Ordená de mayor a menor prioridad cómo se resuelve una operación combinada.",
                    "answer": "1) Paréntesis → 2) Exponentes → 3) Multiplicaciones y divisiones (de izquierda a derecha) → 4) Sumas y restas (de izquierda a derecha).",
                    "hints": ["Recordá PEMDAS."],
                    "payload": {
                        "check": {
                            "type": "order",
                            "lines": [
                                "Paréntesis (desde adentro hacia afuera)",
                                "Exponentes y potencias",
                                "Multiplicaciones y divisiones (de izquierda a derecha)",
                                "Sumas y restas (de izquierda a derecha)",
                            ],
                        },
                    },
                },
                {
                    "item_type": "drill",
                    "title": "Práctica en el Laboratorio de Matemáticas: Exponentes y potencias de 10",
                    "prompt": "Abrí el Laboratorio de Matemáticas en 'Exponentes y potencias de 10', completá el ejemplo desvanecido y resolvé 5 ejercicios.",
                    "answer": "La precisión del Laboratorio queda registrada y te sugiere calificación en este repaso.",
                    "hints": ["Multiplicar por 10^n corre la coma a la derecha; al multiplicar potencias de igual base sumás exponentes."],
                    "payload": {
                        "lab_link": "math:powers",
                        "lab_metric": {"type": "math_accuracy", "good": 80, "easy": 95, "unit": "%"},
                    },
                },
            ],
        },
        # ==================== NIVEL 5: NÚMEROS NEGATIVOS ====================
        {
            "slug": "a-sumar-restar-negativos",
            "title": "16. Números negativos: recta numérica, sumar y restar",
            "level": 5,
            "order_index": 16,
            "summary": "Temperaturas bajo cero, deudas y saldos, valor absoluto y por qué restar un negativo equivale a sumar.",
            "prerequisites": ["a-suma-resta"],
            "metadata": {"lab_tab": "integers", "est_minutes": 20},
            "items": [
                {
                    "item_type": "recall",
                    "title": "Comparar números negativos (temperaturas bajo cero)",
                    "prompt": "En Bariloche hace −8°C y en Ushuaia hace −3°C. ¿Qué número es MAYOR?",
                    "answer": "−3 es mayor que −8: en la recta numérica −3 está más a la derecha (más cerca del 0, menos frío). Cuanto más grande es el número detrás del signo menos, MÁS chico es.",
                    "hints": ["¿Qué día hace menos frío: −3°C o −8°C?"],
                    "payload": {
                        "lab_link": "math:integers",
                        "check": {
                            "type": "choice",
                            "options": [
                                "−3 (está más a la derecha en la recta numérica)",
                                "−8 (porque 8 es mayor que 3)",
                                "Valen lo mismo",
                            ],
                            "correct": 0,
                        },
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Sumar un positivo a un negativo (sube la temperatura)",
                    "prompt": "A la madrugada hacía −5°C y al mediodía la temperatura subió 12°C (−5 + 12). ¿Qué temperatura hace al mediodía? Respondé solo con el número en °C.",
                    "answer": "7°C: subir 5 te lleva a 0°C, y los otros 7 te dejan en +7°C.",
                    "hints": ["De −5 a 0 hay 5; todavía quedan 7 grados más hacia arriba."],
                    "payload": {
                        "lab_link": "math:integers",
                        "check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": "°C"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Sumar dos negativos (acumular gastos en rojo)",
                    "prompt": "Tu cuenta bancaria está en −$400 y te debitan un gasto de $250 (−400 − 250). ¿Cuál es tu nuevo saldo? Respondé con el signo incluido.",
                    "answer": "−650: dos movimientos hacia abajo se suman en negativo (debías 400 y ahora debés 650).",
                    "hints": ["Si ya estabas abajo del cero y bajás 250 más, te alejás más del 0."],
                    "payload": {
                        "lab_link": "math:integers",
                        "check": {"type": "numeric", "value": -650, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Restar un número negativo (anular una deuda)",
                    "prompt": "Tenías saldo $50 y el banco te ANULA (resta) una multa de −$30: 50 − (−30). ¿Cuánto te queda? Respondé solo con el número.",
                    "answer": "80: quitar un negativo (una deuda) te suma dinero → 50 − (−30) = 50 + 30 = 80.",
                    "hints": ["Restar un negativo equivale a sumar el positivo."],
                    "payload": {
                        "lab_link": "math:integers",
                        "check": {"type": "numeric", "value": 80, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Valor absoluto: distancia al cero",
                    "prompt": "Un submarino está a −120 m respecto al nivel del mar. ¿Cuál es su valor absoluto |−120| (distancia al nivel 0)? Respondé solo con el número.",
                    "answer": "120: el valor absoluto siempre es la distancia al cero, por lo tanto nunca es negativo.",
                    "hints": ["Las distancias siempre son positivas (o cero)."],
                    "payload": {"check": {"type": "numeric", "value": 120, "tolerance": 0, "unit": "m"}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Diferencia de temperatura entre la noche y el día",
                    "prompt": "La mínima fue −4°C y la máxima fue 11°C. ¿Cuántos grados de diferencia hubo (11 − (−4))? Respondé solo con el número.",
                    "answer": "15°C: 4 grados para subir de −4 a 0, más 11 grados hasta 11 = 15°C.",
                    "hints": ["Contá el salto en la recta numérica desde −4 hasta +11."],
                    "payload": {"check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": "°C"}},
                },
            ],
        },
        {
            "slug": "a-multiplicar-dividir-negativos",
            "title": "17. Multiplicar y dividir números negativos (regla de signos)",
            "level": 5,
            "order_index": 17,
            "summary": "Regla de signos con intuición real, varios factores negativos y operaciones combinadas con enteros.",
            "prerequisites": ["a-sumar-restar-negativos", "a-exponentes-potencias-10"],
            "metadata": {"lab_tab": "integers", "est_minutes": 20},
            "items": [
                {
                    "item_type": "worked_example",
                    "title": "Positivo por negativo (gastos repetidos)",
                    "prompt": "Una suscripción te descuenta $6 (−6) por mes durante 4 meses: 4 × (−6). ¿Cuál es el cambio acumulado en tu saldo? Incluí el signo.",
                    "answer": "−24: repetir 4 veces una pérdida de 6 da una pérdida total de 24 (+ × − = −).",
                    "hints": ["Signos distintos al multiplicar dan negativo."],
                    "payload": {
                        "lab_link": "math:integers",
                        "check": {"type": "numeric", "value": -24, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Negativo por negativo (anular cargos repetidos)",
                    "prompt": "Te cancelan (−3) tres cobros erróneos de −$5 cada uno: (−3) × (−5). ¿Cuánto mejora tu saldo? Respondé solo con el número.",
                    "answer": "15 (+15): quitar 3 deudas de $5 te deja $15 a favor (− × − = +).",
                    "hints": ["Signos iguales al multiplicar o dividir dan positivo."],
                    "payload": {
                        "lab_link": "math:integers",
                        "check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Dividir negativos (descenso por hora)",
                    "prompt": "La temperatura bajó 18°C (−18) en 6 horas de forma pareja. ¿Cuánto cambió por hora (−18 ÷ 6)? Incluí el signo.",
                    "answer": "−3°C por hora: negativo dividido positivo da negativo.",
                    "hints": ["18 ÷ 6 = 3, y signos distintos → negativo."],
                    "payload": {
                        "lab_link": "math:integers",
                        "check": {"type": "numeric", "value": -3, "tolerance": 0, "unit": "°C/h"},
                    },
                },
                {
                    "item_type": "worked_example",
                    "title": "Dividir negativo por negativo",
                    "prompt": "Calculá (−48) ÷ (−8). Respondé solo con el número.",
                    "answer": "6 (+6): signos iguales en la división siempre dan positivo.",
                    "hints": ["¿Cuántas veces cabe −8 dentro de −48?"],
                    "payload": {"check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Multiplicar tres números negativos",
                    "prompt": "Calculá (−2) × (−3) × (−4). Incluí el signo.",
                    "answer": "−24: (−2)×(−3) = +6, y (+6)×(−4) = −24. Regla rápida: cantidad PAR de signos menos → positivo; cantidad IMPAR → negativo.",
                    "hints": ["Hay 3 signos negativos (número impar)."],
                    "payload": {"check": {"type": "numeric", "value": -24, "tolerance": 0, "unit": ""}},
                },
                {
                    "item_type": "worked_example",
                    "title": "Combinada final: PEMDAS + signos negativos",
                    "prompt": "Resolvé 12 − 3 × (2 − 6). Respondé solo con el número.",
                    "answer": "24: paréntesis (2 − 6) = −4 → multiplicación (−3) × (−4) = +12 → 12 + 12 = 24.",
                    "hints": ["Resolvé el paréntesis primero y aplicá menos por menos = más."],
                    "payload": {
                        "lab_link": "math:integers",
                        "check": {"type": "numeric", "value": 24, "tolerance": 0, "unit": ""},
                    },
                },
                {
                    "item_type": "drill",
                    "title": "Práctica en el Laboratorio de Matemáticas: Enteros y orden de operaciones",
                    "prompt": "Abrí el Laboratorio de Matemáticas en 'Negativos y orden de operaciones', resolvé el ejemplo desvanecido y completá 5 ejercicios sin caer en trampas de signos.",
                    "answer": "Tu precisión del Laboratorio queda guardada para sugerir la calificación de esta tarjeta.",
                    "hints": ["Cuidado con hacer la resta antes de multiplicar el paréntesis."],
                    "payload": {
                        "lab_link": "math:integers",
                        "lab_metric": {"type": "math_accuracy", "good": 80, "easy": 95, "unit": "%"},
                    },
                },
            ],
        },
    ],
}


MATH_LESSONS: dict[str, dict] = {
    # ==================== NIVEL 1 ====================
    "a-valor-posicional": {
        "hook": {
            "question": "¿Por qué los mismos tres dígitos (`1`, `5`, `0`) pueden significar `$150` o `$510`, o hacerte pagar 10 veces de más si se corre un cero?",
            "intuition": "En nuestro sistema numérico, **el lugar donde está parado un dígito decide cuánto vale**. Cada paso hacia la izquierda multiplica su valor por `10`. Entender esto hace que los números grandes dejen de intimidar.",
        },
        "concept": {
            "points": [
                "**Cada columna vale ×10 que la de su derecha**: unidades (`1`), decenas (`10`), centenas (`100`), miles (`1000`), decenas de mil (`10 000`), centenas de mil (`100 000`).",
                "**El cero es un guardalugar**: en `3050`, los ceros dicen que no hay centenas ni unidades sueltas; sin ellos el número colapsaría a `35`.",
                "**Comparar sin dudar**: primero mirá quién tiene más dígitos; si empatan, compará **de izquierda a derecha** porque la columna más a la izquierda pesa mucho más.",
                "**Redondear para estimar**: elegí la columna a redondear y mirá el dígito de su derecha. Si es `0–4`, dejala igual; si es `5–9`, subila en 1 y completá con ceros.",
            ],
            "real_world": [
                {
                    "title": "Transferencias bancarias sin errores",
                    "detail": "Agrupar de a 3 cifras (`$150 000` vs. `$15 000`) evita mandar 10 veces más dinero por un cero de más.",
                },
                {
                    "title": "Calcular el carrito del súper al paso",
                    "detail": "Redondear `$3680` a `$3700` y `$2290` a `$2300` te dice al instante que vas por `~$6000` antes de llegar a la caja.",
                },
                {
                    "title": "Comparar precios de autos o alquileres",
                    "detail": "Entre `$409 900` y `$410 100`, la cifra de las decenas de mil (`0` vs. `1`) define todo de un vistazo.",
                },
            ],
            "key_rule": "Un lugar a la izquierda = `×10` · Compará de izquierda a derecha · Redondeo: `5` o más sube, menos de `5` baja.",
            "pitfall": "Olvidar escribir el `0` cuando armás un número desde su forma expandida (ej. escribir `300 000 + 400 + 5` como `345` en vez de `300 405`).",
        },
        "example": {
            "title": "Desarmá y redondeá un presupuesto real",
            "steps": [
                "Un presupuesto para arreglar una bici sale `$48 670`.",
                "Desarmado por valor posicional: `40 000 + 8000 + 600 + 70` (el `8` vale `8000`, no `8`).",
                "Para redondear al millar más cercano miramos el `6` de las centenas: como `6 ≥ 5`, sube a `$49 000`.",
            ],
            "lab_link": "math:place_value",
            "lab_cta": "Practicar valor posicional en el Laboratorio",
        },
        "check": {
            "question": "En el número `382 410`, ¿cuánto vale realmente el dígito `8`?",
            "options": [
                {"text": "80 000 (ocho decenas de mil)", "ok": True, "feedback": "Exacto: está en la 5ª posición desde la derecha (8 × 10 000)."},
                {"text": "8000", "ok": False, "feedback": "8000 sería la 4ª posición (donde está el 2)."},
                {"text": "800", "ok": False, "feedback": "800 son centenas (donde está el 4)."},
            ],
        },
        "checks": [
            {
                "question": "Redondeá `$7480` a la centena más cercana (múltiplo de 100).",
                "options": [
                    {"text": "$7400", "ok": False, "feedback": "La decena es 8 (mayor que 5), así que 7480 está mucho más cerca de 7500."},
                    {"text": "$7500", "ok": True, "feedback": "Exacto: solo faltan 20 para llegar a 7500."},
                    {"text": "$7000", "ok": False, "feedback": "Eso sería redondear al millar, no a la centena."},
                ],
            },
            {
                "question": "¿Cuál de estos dos números es MAYOR: `98 765` o `101 002`?",
                "options": [
                    {"text": "98 765, porque sus dígitos son más grandes", "ok": False, "feedback": "El tamaño de los dígitos sueltos no gana a tener una columna entera más a la izquierda."},
                    {"text": "101 002, porque tiene 6 dígitos (centena de mil) frente a 5", "ok": True, "feedback": "Exacto: 100 000 siempre le gana a cualquier número de 5 cifras."},
                    {"text": "Son casi iguales, depende del último dígito", "ok": False, "feedback": "Siempre manda primero la cantidad de cifras y las posiciones de la izquierda."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en 2 frases cómo funciona el valor posicional y cómo usás el redondeo para estimar gastos.",
    },
    "a-suma-resta": {
        "hook": {
            "question": "Si pagás `$1375` con un billete de `$5000`, ¿por qué restar sobre tres ceros (`5000 − 1375`) suele confundir… y cuál es el truco para sacarlo mentalmente en 3 segundos?",
            "intuition": "Restar `5000 − 1375` da exactamente lo mismo que restar `4999 − 1374` (le bajás `1` a ambos números y desaparecen todos los 'pedir prestado'). Entender qué es reagrupar te libera de sufrir con los ceros.",
        },
        "concept": {
            "points": [
                "**Sumar 'llevando' (reagrupar)**: cuando una columna pasa de `9` (ej. `7 + 8 = 15`), dejás el `5` y pasás `1` paquete de `10` a la columna de la izquierda.",
                "**Restar 'pidiendo prestado'**: no estás cambiando el número, solo lo desarmás distinto (ej. `52` es `50 + 2`, pero también es `40 + 12`).",
                "**Compensación mental para sumar**: para `1980 + 650`, sumá `20` al primero (`2000 + 650 = 2650`) y devolvelos al final (`2630`).",
                "**Atajo para vueltos (subir contando)**: de `$1375` a `$5000`, sumás `+25` (`1400`), `+600` (`2000`) y `+3000` (`5000`) → `$3625`. Y siempre podés chequear una resta sumando al revés.",
            ],
            "real_world": [
                {
                    "title": "Revisar el vuelto en la caja",
                    "detail": "Contar hacia arriba desde el precio hasta tu billete te permite controlar el vuelto sin calculadora en segundos.",
                },
                {
                    "title": "Sumar gastos del mes",
                    "detail": "Redondear mentalmente antes de sumar te da un techo aproximado para detectar si tecleaste mal un número.",
                },
                {
                    "title": "Kilómetros recorridos en un viaje",
                    "detail": "El odómetro final menos el inicial te dice exactamente cuánto avanzaste.",
                },
            ],
            "key_rule": "Alineá unidades a la derecha · Reagrupar conserva el valor · Toda resta `A − B = C` se comprueba con `C + B = A`.",
            "pitfall": "Restar siempre 'el más grande menos el más chico' dentro de una columna (ej. hacer `42 − 18` poniendo `8 − 2 = 6` y llegar a `36` en vez de `24`).",
        },
        "example": {
            "title": "Vuelto sin pedir prestado con el truco del −1",
            "steps": [
                "Queremos calcular `$5000 − $1375` sin enredarnos con los tres ceros.",
                "Restamos `1` a ambos números (la distancia entre ellos no cambia): `4999 − 1374`.",
                "Ahora cada columna se resta directo sin pedir prestado: `9−4=5`, `9−7=2`, `9−3=6`, `4−1=3` → `$3625`.",
            ],
            "lab_link": "math:place_value",
            "lab_cta": "Practicar sumas y restas en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál de estas formas calcula `298 + 47` más rápido y sin error?",
            "options": [
                {"text": "Hacer `300 + 47 = 347` y restar los `2` que sumaste → `345`", "ok": True, "feedback": "Exacto: compensación limpia, cero riesgo de equivocarte llevando."},
                {"text": "Hacer `300 + 47 = 347` y sumar `2` más → `349`", "ok": False, "feedback": "Como ya agregaste 2 de más al 298, al final hay que restarlos, no volver a sumarlos."},
                {"text": "Sumar `2 + 4 = 6` y `98 + 7 = 105` → `6105`", "ok": False, "feedback": "El 2 de 298 vale 200 y el 4 de 47 vale 40: están en posiciones distintas."},
            ],
        },
        "checks": [
            {
                "question": "Al hacer `4000 − 1265`, el truco de restar 1 a ambos convierte la cuenta en:",
                "options": [
                    {"text": "`3999 − 1264` (= `2735`)", "ok": True, "feedback": "Exacto: ninguna columna necesita pedir prestado y el resultado es idéntico."},
                    {"text": "`3999 − 1266`", "ok": False, "feedback": "Para mantener la misma diferencia tenés que restar 1 a AMBOS, no restar a uno y sumar al otro."},
                    {"text": "`4001 − 1264`", "ok": False, "feedback": "Eso aumentaría la diferencia en 2."},
                ],
            },
            {
                "question": "Hiciste `630 − 285` y te dio `455`. ¿Qué te dice la prueba de la suma (`455 + 285`)?",
                "options": [
                    {"text": "Da `740` (se pasó por 110), así que está mal; el resultado real es `345`", "ok": True, "feedback": "Exacto: comprobar con la suma atrapa al instante los errores al pedir prestado."},
                    {"text": "Da `630`, está perfecta", "ok": False, "feedback": "400 + 200 ya es 600, y 55 + 85 suma 140 más → 740."},
                    {"text": "No se puede probar una resta con suma", "ok": False, "feedback": "La suma es la operación inversa exacta de la resta."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá el truco mental que más te sirvió para sumar o dar vueltos sin equivocarte.",
    },
    "a-intro-multiplicacion": {
        "hook": {
            "question": "Si te olvidás cuánto es `7 × 8`, ¿estás trabado para siempre o podés reconstruirlo en 2 segundos usando tablas fáciles?",
            "intuition": "Multiplicar es solo sumar grupos iguales. Así que `7 × 8` es simplemente `7 × 5` (`35`) + `7 × 3` (`21`) = `56`. Cuando entendés cómo se parte una multiplicación, nunca más quedás en blanco.",
        },
        "concept": {
            "points": [
                "**Qué significa multiplicar**: `4 × 6` son 4 grupos de 6 (o un rectángulo de 4 filas por 6 columnas = 24 cuadraditos).",
                "**Propiedad conmutativa (`a × b = b × a`)**: si sabés `3 × 8 = 24`, ya sabés `8 × 3 = 24`. Eso recorta a la mitad lo que hay que recordar.",
                "**Propiedad distributiva (el superpoder)**: partí el número difícil en dos fáciles. Ejemplos: `×9` es `×10 − ×1`; `×8` es `×5 + ×3` (o duplicar tres veces: `×2 → ×2 → ×2`).",
                "**Reglas instantáneas**: cualquier número `× 0 = 0`; cualquier número `× 1` queda igual; cualquier número `× 10` corre sus cifras y agrega un `0`.",
            ],
            "real_world": [
                {
                    "title": "Comprar en packs",
                    "detail": "6 packs de 8 latas son `6 × 8 = 48` latas sin tener que contar de una en una.",
                },
                {
                    "title": "Calcular baldosas o asientos",
                    "detail": "Un salón con 7 filas de 9 sillas tiene `7 × 9 = 70 − 7 = 63` asientos.",
                },
                {
                    "title": "Acumular minutos de estudio",
                    "detail": "Practicar 25 min por día durante 4 días equivale a `4 × 25 = 100` minutos.",
                },
            ],
            "key_rule": "El orden no cambia el producto · Partí tablas difíciles en partes fáciles (`×9 = ×10 − ×1`, `×7 = ×5 + ×2`).",
            "pitfall": "Confundir `6 × 0` con `6` (0 grupos de 6 siempre es `0`) o intentar recordar las 100 multiplicaciones de memoria sin usar descomposiciones.",
        },
        "example": {
            "title": "Dos caminos rápidos para calcular `8 × 9`",
            "steps": [
                "Camino 1 (truco del 9): pensá `9` como `10 − 1` → `8 × 10 = 80`, menos `8` = `72`.",
                "Camino 2 (duplicar): `9 × 2 = 18`, `18 × 2 = 36`, `36 × 2 = 72` (multiplicar por 8 es duplicar 3 veces).",
                "Elegí el atajo que te resulte más natural: los dos dan `72`.",
            ],
            "lab_link": "math:mult_div",
            "lab_cta": "Practicar multiplicación en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál descomposición calcula correctamente `7 × 6`?",
            "options": [
                {"text": "`(7 × 5) + (7 × 1) = 35 + 7 = 42`", "ok": True, "feedback": "Exacto: partiste el 6 en 5 + 1 usando la propiedad distributiva."},
                {"text": "`(7 × 5) + 1 = 36`", "ok": False, "feedback": "Faltó multiplicar también ese 1 por 7."},
                {"text": "`(7 + 5) × 1 = 12`", "ok": False, "feedback": "No se cambia la multiplicación por suma entre 7 y 5."},
            ],
        },
        "checks": [
            {
                "question": "Usando el truco del 9 (`×10 − ×1`), ¿cuánto da `9 × 7`?",
                "options": [
                    {"text": "63", "ok": True, "feedback": "Exacto: 70 − 7 = 63."},
                    {"text": "61", "ok": False, "feedback": "Restaste 9 en vez de restar 7 (es 10×7 − 1×7)."},
                    {"text": "77", "ok": False, "feedback": "Sumaste 7 en vez de restarlo (eso sería 11 × 7)."},
                ],
            },
            {
                "question": "Tenés 0 cajas y en cada caja caben 9 libros. ¿Cuántos libros tenés (`0 × 9`)?",
                "options": [
                    {"text": "0", "ok": True, "feedback": "Exacto: cero cajas = cero libros."},
                    {"text": "9", "ok": False, "feedback": "9 sería si tuvieras 1 caja (1 × 9)."},
                    {"text": "1", "ok": False, "feedback": "Multiplicar por 0 siempre da 0."},
                ],
            },
        ],
        "takeaway_prompt": "Mostrá con tus palabras cómo reconstruirías `8 × 7` si no te acordaras la tabla.",
    },
    "a-intro-division": {
        "hook": {
            "question": "Si van `19` personas a un recital y en cada auto entran `4`, ¿por qué la respuesta real NO es `4` autos ni `4.75` autos?",
            "intuition": "`19 ÷ 4` da `4` con **resto 3**. En la hoja el resto es un numerito aparte, pero en la vida real ese resto decide si necesitás **un auto extra** (5 autos) o si te sobra vuelto sin alcanzar para un alfajor más.",
        },
        "concept": {
            "points": [
                "**Dividir es lo opuesto a multiplicar**: `42 ÷ 6 = ?` pregunta lo mismo que `6 × ? = 42` (`7`). Sirve tanto para *repartir* entre 6 personas como para ver *cuántos grupos de 6 entran*.",
                "**División con resto**: cuando no entra justo, queda un sobrante (resto) siempre **menor que el divisor**. Se chequea con: `divisor × cociente + resto = dividendo`.",
                "**El resto en la vida real tiene 3 destinos**: a veces te obliga a **subir 1** (autos, cajas para embalar), a veces **se descarta** (cuántos artículos enteros te alcanza para comprar), y a veces **se parte** en fracciones o decimales (repartir plata o comida).",
                "**El cero en la división**: `0 ÷ 5 = 0`, pero **`5 ÷ 0` no existe** (ningún número multiplicado por 0 puede dar 5).",
            ],
            "real_world": [
                {
                    "title": "Dividir la cuenta de una cena",
                    "detail": "`$54 000 ÷ 6 = $9000` por persona: repartir en partes iguales.",
                },
                {
                    "title": "Armar equipos o mesas",
                    "detail": "Con 25 personas y mesas de 4, `25 ÷ 4 = 6` resto `1`: necesitás **7 mesas** para sentar a todos.",
                },
                {
                    "title": "Comprar con presupuesto fijo",
                    "detail": "Con `$50` y pasajes de `$8`, `50 ÷ 8 = 6` resto `2`: comprás solo **6** pasajes y te quedan `$2`.",
                },
            ],
            "key_rule": "`dividendo = divisor × cociente + resto` (con `resto < divisor`) · Nunca se puede dividir por `0`.",
            "pitfall": "Responder mecánicamente solo el cociente sin leer qué pide el problema real con el resto (dejar gente afuera o comprar cosas sin que alcance la plata).",
        },
        "example": {
            "title": "Misma división, dos respuestas reales distintas",
            "steps": [
                "Calculamos `26 ÷ 4`: el múltiplo más cercano por debajo es `4 × 6 = 24`, así que da **6 con resto 2**.",
                "Caso A (botellas en cajas de 4 para llevar las 26): necesitás **7 cajas** (la séptima lleva las 2 restantes).",
                "Caso B (tenés `$26` y cada lápiz sale `$4`): solo te alcanza para **6 lápices** y te sobran `$2`.",
            ],
            "lab_link": "math:mult_div",
            "lab_cta": "Practicar divisiones en el Laboratorio",
        },
        "check": {
            "question": "Van `22` chicos de campamento y en cada carpa entran máximo `4`. ¿Cuántas carpas hay que llevar como mínimo?",
            "options": [
                {"text": "5 carpas", "ok": False, "feedback": "5 carpas solo alojan a 20 chicos; 2 quedarían durmiendo afuera."},
                {"text": "6 carpas", "ok": True, "feedback": "Exacto: 22 ÷ 4 = 5 con resto 2, así que hace falta una 6ª carpa."},
                {"text": "2 carpas", "ok": False, "feedback": "2 es el resto (los chicos sobrantes), no la cantidad de carpas."},
            ],
        },
        "checks": [
            {
                "question": "Al dividir un número por `5`, ¿puede quedar un resto igual a `6`?",
                "options": [
                    {"text": "No: si sobran 6, todavía entra un grupo más de 5 y el resto real es 1", "ok": True, "feedback": "Exacto: el resto siempre tiene que ser menor que el divisor."},
                    {"text": "Sí, si el dividendo era muy grande", "ok": False, "feedback": "No importa qué tan grande sea el dividendo, siempre podés armar otro grupo de 5."},
                    {"text": "Sí, solo en divisiones impares", "ok": False, "feedback": "Nunca: el resto siempre está entre 0 y (divisor − 1)."},
                ],
            },
            {
                "question": "¿Cuánto da `0 ÷ 12` vs. `12 ÷ 0`?",
                "options": [
                    {"text": "`0 ÷ 12 = 0` y `12 ÷ 0` no está definido", "ok": True, "feedback": "Exacto: 0×12=0 funciona, pero ?×0=12 no tiene solución."},
                    {"text": "Los dos valen `0`", "ok": False, "feedback": "Dividir por cero nunca da cero; no tiene sentido matemático."},
                    {"text": "Los dos dan `12`", "ok": False, "feedback": "Repartir nada entre 12 da 0, y dividir por 0 es imposible."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con un ejemplo real cuándo el resto te hace sumar 1 al resultado y cuándo se descarta.",
    },
    # ==================== NIVEL 2 ====================
    "a-multiplicar-varios-digitos": {
        "hook": {
            "question": "¿Por qué al multiplicar `24 × 15` en el papel te enseñaron a poner misteriosamente un cero (o dejar un hueco) en la segunda fila?",
            "intuition": "No es ningún truco mágico: el `1` de `15` vale **`10`**, así que estás haciendo `24 × 5` (`120`) por un lado y `24 × 10` (`240`) por el otro. Al verlo como un rectángulo partido en piezas (**modelo de área**), todo cobra sentido inmediato.",
        },
        "concept": {
            "points": [
                "**Atajo de ceros**: para `40 × 300`, hacés `4 × 3 = 12` y sumás los `3` ceros al final → `12 000`.",
                "**Modelo de área (descomponer)**: partí ambos números en decenas y unidades. Para `24 × 15 = (20 + 4) × (10 + 5)` → `200 + 100 + 40 + 20 = 360`.",
                "**El algoritmo tradicional es lo mismo resumido**: la primera fila es `× unidades` (`24 × 5 = 120`) y la segunda es `× decenas` (`24 × 10 = 240`, por eso lleva ese `0` al final).",
                "**Estimá antes de empezar**: redondeá para saber la zona (`24 × 15 ≈ 25 × 15 = 375`). Si te da `36` o `3600`, el error salta a la vista.",
            ],
            "real_world": [
                {
                    "title": "Presupuesto por hora o mensual",
                    "detail": "12 meses a `$125` es `10×125 + 2×125 = 1250 + 250 = $1500` sin calculadora.",
                },
                {
                    "title": "Comprar cerámica o pintura (m²)",
                    "detail": "Un patio de `14 × 23` baldosas lleva `10×23 + 4×23 = 230 + 92 = 322` baldosas.",
                },
                {
                    "title": "Compras al por mayor",
                    "detail": "30 cajas de 400 tornillos = `3 × 4` con tres ceros = `12 000` tornillos.",
                },
            ],
            "key_rule": "Estimá primero · Descomponé en decenas y unidades (`24 × 15 = 24×10 + 24×5`) · Cada fila respeta su valor posicional.",
            "pitfall": "Olvidarse el `0` en la fila de las decenas al multiplicar por 2 cifras (sumar `120 + 24 = 144` en vez de `120 + 240 = 360`).",
        },
        "example": {
            "title": "Resolvé `24 × 15` por modelo de área",
            "steps": [
                "Estimación rápida: `24 × 15` tiene que andar cerca de `20 × 15 = 300` (un poco más).",
                "Partimos `15` en `10 + 5`: primero `24 × 10 = 240`, y `24 × 5` es la mitad de 240 = `120`.",
                "Sumamos ambos bloques: `240 + 120 = 360`. Coincide perfecto con nuestra estimación.",
            ],
            "lab_link": "math:mult_div",
            "lab_cta": "Probar el modelo de área en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto da `30 × 500` usando el atajo de los ceros?",
            "options": [
                {"text": "1500", "ok": False, "feedback": "30 tiene 1 cero y 500 tiene 2 ceros: son 3 ceros en total, no 2."},
                {"text": "15 000", "ok": True, "feedback": "Exacto: 3 × 5 = 15 más 3 ceros = 15 000."},
                {"text": "150 000", "ok": False, "feedback": "Agregaste un cero de más."},
            ],
        },
        "checks": [
            {
                "question": "Si partís `16 × 25` como `(10 × 25) + (6 × 25)`, ¿cuánto da?",
                "options": [
                    {"text": "400", "ok": True, "feedback": "Exacto: 250 + 150 = 400."},
                    {"text": "350", "ok": False, "feedback": "6 × 25 es 150, y 250 + 150 = 400."},
                    {"text": "256", "ok": False, "feedback": "Hay que multiplicar el 6 por 25, no sumarlo."},
                ],
            },
            {
                "question": "Multiplicás `42 × 19` y te da `420`. Usando una estimación (`40 × 20`), ¿ese resultado es creíble?",
                "options": [
                    {"text": "No: `40 × 20 = 800`, así que `420` es casi la mitad de lo esperado (probablemente faltó el 0 de las decenas)", "ok": True, "feedback": "Exacto: 42 × 19 = 798, pegado a 800."},
                    {"text": "Sí, porque 420 empieza con 42", "ok": False, "feedback": "420 sería 42 × 10, casi la mitad de 42 × 19."},
                    {"text": "No, debería dar cerca de 8000", "ok": False, "feedback": "40 × 20 tiene solo dos ceros (800)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué se pone un cero en la segunda fila de la multiplicación tradicional usando el valor posicional.",
    },
    "a-dividir-varios-digitos": {
        "hook": {
            "question": "¿Te traba la división larga de 2 cifras en el divisor (como `420 ÷ 35`)? ¿Sabías que podés resolverla sin adivinar la cifra exacta a la primera?",
            "intuition": "Con el método de **cocientes parciales** vas restando bloques fáciles que SÍ conocés (por ejemplo `35 × 10 = 350`, y te quedan solo `70`, que es `35 × 2` → `10 + 2 = 12`). Cero adivinanza, mismo resultado exacto.",
        },
        "concept": {
            "points": [
                "**Simplificar ceros**: si ambos terminan en cero, tachá la **misma cantidad** en los dos (`36 000 ÷ 400 = 360 ÷ 4 = 90`).",
                "**Cocientes parciales**: en vez de buscar la cifra perfecta de golpe, sacá múltiplos cómodos (`×10`, `×20`, `×100`), restalos y repetí hasta que sobre menos que el divisor. Después sumás los bloques.",
                "**Cuidado con los ceros en el medio**: en `824 ÷ 4`, el `2` no alcanza para 4, así que ponés **`0`** en las decenas y recién bajás el `4` → `206` (estimar `800 ÷ 4 = 200` evita escribir `26`).",
                "**Verificación infalible**: multiplicá `cociente × divisor + resto`; si vuelve al dividendo, tenés 100% de certeza.",
            ],
            "real_world": [
                {
                    "title": "Cuotas sin interés",
                    "detail": "Una compra de `$756` en 6 cuotas: `600÷6 = 100`, `120÷6 = 20`, `36÷6 = 6` → `$126` por mes.",
                },
                {
                    "title": "Rendimiento de combustible (km/L)",
                    "detail": "`420 km ÷ 35 L`: con 10 L hacés 350 km, quedan 70 km = 2 L → `12 km/L`.",
                },
                {
                    "title": "Tiempo para ahorrar una meta",
                    "detail": "Juntar `$36 000` ahorrando `$400` por día = `360 ÷ 4 = 90` días.",
                },
            ],
            "key_rule": "Tachá mismos ceros · Sacá bloques fáciles (`×10`, `×100`) y sumalos · Estimá para no perder ceros en el medio.",
            "pitfall": "Bajar dos cifras seguidas en la división larga sin escribir el `0` en el cociente (convertir `206` en `26`).",
        },
        "example": {
            "title": "Calculá `420 ÷ 35` por cocientes parciales",
            "steps": [
                "¿Cuántos `35` entran fácil en `420`? Probamos `10`: `35 × 10 = 350`.",
                "Restamos ese bloque: `420 − 350 = 70`.",
                "¿Cuántos `35` entran en `70`? Exactamente `2` (`35 × 2 = 70`, resto `0`). Sumamos: `10 + 2 = 12`.",
            ],
            "lab_link": "math:mult_div",
            "lab_cta": "Practicar divisiones en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto da `48 000 ÷ 600` simplificando ceros?",
            "options": [
                {"text": "80", "ok": True, "feedback": "Exacto: tachás dos ceros de ambos → 480 ÷ 6 = 80."},
                {"text": "8", "ok": False, "feedback": "Tachaste tres ceros al 48 000 y solo dos al 600; hay que tachar la misma cantidad."},
                {"text": "800", "ok": False, "feedback": "Chequeá: 800 × 600 = 480 000, diez veces más grande."},
            ],
        },
        "checks": [
            {
                "question": "Calculás `918 ÷ 9` y te da `12`. ¿Qué te avisa tu estimación (`900 ÷ 9`)?",
                "options": [
                    {"text": "Que faltó el cero en el medio: `900 ÷ 9 = 100`, así que el resultado real es `102`", "ok": True, "feedback": "Exacto: 900÷9 = 100 y 18÷9 = 2 → 102."},
                    {"text": "Que `12` está perfecto porque 9÷9=1 y 18÷9=2", "ok": False, "feedback": "El primer 9 vale 900 (centenas), así que el 1 vale 100, no 10."},
                    {"text": "Que debería dar cerca de 1000", "ok": False, "feedback": "900 dividido 9 es 100."},
                ],
            },
            {
                "question": "Dividís `315 ÷ 15` por cocientes parciales: primero sacás `15 × 20 = 300`. ¿Cuánto queda y cuál es el cociente final?",
                "options": [
                    {"text": "Quedan `15` (1 más) → cociente `21`", "ok": True, "feedback": "Exacto: 20 + 1 = 21 (y 21 × 15 = 315)."},
                    {"text": "Quedan `15` → cociente `20` con resto `15`", "ok": False, "feedback": "El resto nunca puede ser igual al divisor: en 15 entra un 15 más."},
                    {"text": "Quedan `30` → cociente `22`", "ok": False, "feedback": "315 − 300 = 15, no 30."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá cómo funciona el método de cocientes parciales para dividir sin adivinar.",
    },
    # ==================== NIVEL 3: FRACCIONES ====================
    "a-entender-fracciones": {
        "hook": {
            "question": "¿Por qué `1/3` de pizza es MÁS grande que `1/8`, aunque `8` sea un número mucho más grande que `3`?",
            "intuition": "El número de abajo (denominador) dice **entre cuántas partes iguales cortaste el entero**. Cortar la misma pizza en 8 porciones hace porciones mucho más flacas que cortarla en 3.",
        },
        "concept": {
            "points": [
                "**Numerador y Denominador**: en `3/4`, el `4` (abajo) es en cuántas partes iguales se divide 1 entero; el `3` (arriba) es cuántas partes tomás.",
                "**Fracciones equivalentes**: cortar cada mitad en dos convierte `1/2` en `2/4` — cambió el corte, NO la cantidad de comida. Multiplicar o dividir arriba y abajo por el **mismo número** conserva el valor.",
                "**Simplificar**: dividir arriba y abajo por un divisor común hasta dejar la fracción en su versión más limpia (`8/12 = 2/3`).",
                "**Fracciones mayores que 1**: cuando el numerador supera al denominador (`7/4`) tenés más de un entero. Se escribe también como número mixto: `1 y 3/4` (`7 ÷ 4 = 1`, resto `3`).",
            ],
            "real_world": [
                {
                    "title": "Medir en la cocina o carpintería",
                    "detail": "Dos medidas de `1/4` de taza son exactamente `2/4 = 1/2` taza.",
                },
                {
                    "title": "El reloj en fracciones de hora",
                    "detail": "15 minutos son `15/60 = 1/4` de hora; 45 minutos son `3/4` de hora.",
                },
                {
                    "title": "Helado o compras por peso",
                    "detail": "Pedir 5 cuartos de kilo (`5/4 kg`) es exactamente `1 kg y 1/4`.",
                },
            ],
            "key_rule": "Abajo = tamaño del corte · Arriba = cuántas partes · Equivalentes: multiplicar o dividir arriba y abajo por el mismo número.",
            "pitfall": "Creer que `2/6` es más grande que `1/3` porque tiene números más grandes (en realidad son exactamente iguales: `2/6 = 1/3`).",
        },
        "example": {
            "title": "Simplificá y ubicá fracciones de una hora",
            "steps": [
                "Una clase dura `40` minutos de una hora (`60` minutos): es la fracción `40/60`.",
                "Dividimos arriba y abajo por `10` → `4/6`, y luego por `2` → `2/3` de hora.",
                "Comprobación: una hora partida en 3 tercios da bloques de 20 min; 2 de esos bloques son `40 min`.",
            ],
            "lab_link": "math:fractions",
            "lab_cta": "Ver barras de fracciones en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál fracción es equivalente a `3/5`?",
            "options": [
                {"text": "`9/15`", "ok": True, "feedback": "Exacto: multiplicaste arriba y abajo por 3 (3×3=9 y 5×3=15)."},
                {"text": "`5/7`", "ok": False, "feedback": "Sumar 2 arriba y abajo NO mantiene la equivalencia; hay que multiplicar o dividir."},
                {"text": "`6/15`", "ok": False, "feedback": "Multiplicaste por 2 arriba y por 3 abajo: tiene que ser el mismo número."},
            ],
        },
        "checks": [
            {
                "question": "Simplificada al máximo, ¿a qué equivale `12/16`?",
                "options": [
                    {"text": "`6/8`", "ok": False, "feedback": "Es equivalente, pero todavía se puede dividir por 2 una vez más."},
                    {"text": "`3/4`", "ok": True, "feedback": "Exacto: dividiendo arriba y abajo por 4 queda 3/4."},
                    {"text": "`2/3`", "ok": False, "feedback": "12÷4 = 3 (no 2) y 16÷4 = 4 (no 3)."},
                ],
            },
            {
                "question": "Compraste `9/4` litros de leche. ¿Cómo se expresa como número mixto?",
                "options": [
                    {"text": "`2` litros y `1/4`", "ok": True, "feedback": "Exacto: 8/4 son 2 enteros y sobra 1/4."},
                    {"text": "`1` litro y `5/4`", "ok": False, "feedback": "En 5/4 todavía entra un entero más."},
                    {"text": "`4` litros y `1/2`", "ok": False, "feedback": "9 ÷ 4 da 2, no 4."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con un ejemplo de comida o tiempo por qué `1/2`, `2/4` y `3/6` representan exactamente lo mismo.",
    },
    "a-sumar-restar-fracciones-igual": {
        "hook": {
            "question": "Si tenés `3/8` de torta y te dan `2/8` más, ¿por qué da `5/8` y NO `5/16`?",
            "intuition": "Pensá en la palabra 'octavos' como si fuera una moneda o fruta: `3 octavos + 2 octavos = 5 octavos`. Cuando las porciones ya tienen el mismo tamaño, solo contás cuántas tenés.",
        },
        "concept": {
            "points": [
                "**Mismo denominador = cuenta directa**: sumás o restás solo los numeradores y dejás intacto el denominador (`3/8 + 2/8 = 5/8`).",
                "**Restar a un entero**: convertí `1` en el denominador que necesitás (`1 = 8/8 = 4/4 = 5/5`). Así `1 − 3/8 = 8/8 − 3/8 = 5/8`.",
                "**Números mixtos**: sumá enteros con enteros y fracciones con fracciones. Si la fracción se pasa de un entero (ej. `6/4 = 1 y 2/4`), pasá ese entero a la parte entera.",
                "**Simplificá siempre al final**: si el resultado es `6/8` o `4/6`, dejalo limpio como `3/4` o `2/3`.",
            ],
            "real_world": [
                {
                    "title": "Medidor de combustible",
                    "detail": "El tanque tiene 8 rayitas (octavos): si salís con `7/8` y gastás `4/8`, te quedan `3/8`.",
                },
                {
                    "title": "Recetas con la misma taza medidora",
                    "detail": "`3/4` taza + `3/4` taza = `6/4` = `1` taza y media.",
                },
                {
                    "title": "Cortar un listón de madera",
                    "detail": "A 2 metros le cortás `1/4` m: desarmás 1 metro en `4/4` y te queda `1 y 3/4` m.",
                },
            ],
            "key_rule": "Con igual denominador: operás solo arriba y mantenés abajo · `1 entero = n/n` · Simplificá al final.",
            "pitfall": "Sumar los denominadores (`1/4 + 1/4 = 2/8`), que en realidad mantiene el valor en vez de duplicarlo.",
        },
        "example": {
            "title": "Sumá horas de práctica con números mixtos",
            "steps": [
                "Practicaste `1 y 3/4` horas el sábado y `2 y 3/4` horas el domingo.",
                "Sumamos enteros (`1 + 2 = 3`) y cuartos (`3/4 + 3/4 = 6/4`).",
                "Como `6/4` es `1 entero y 2/4` (`1 y 1/2`), sumamos `3 + 1 y 1/2 = 4 y 1/2` horas.",
            ],
            "lab_link": "math:fractions",
            "lab_cta": "Practicar fracciones en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto da `5/12 + 3/12`, simplificado al máximo?",
            "options": [
                {"text": "`8/24`", "ok": False, "feedback": "Sumaste los denominadores; el 12 se mantiene igual."},
                {"text": "`2/3`", "ok": True, "feedback": "Exacto: 5/12 + 3/12 = 8/12, y dividiendo por 4 queda 2/3."},
                {"text": "`8/12` (no se puede simplificar)", "ok": False, "feedback": "8 y 12 se pueden dividir por 4."},
            ],
        },
        "checks": [
            {
                "question": "Tenías 1 barra de chocolate entera y comiste `2/5`. ¿Cuánto queda?",
                "options": [
                    {"text": "`3/5`", "ok": True, "feedback": "Exacto: 5/5 − 2/5 = 3/5."},
                    {"text": "`1/5`", "ok": False, "feedback": "El entero tiene 5 quintos, no 3."},
                    {"text": "`3/10`", "ok": False, "feedback": "El denominador sigue siendo 5."},
                ],
            },
            {
                "question": "Calculá `2 − 1/3` (desarmando 1 entero en `3/3`).",
                "options": [
                    {"text": "`1 y 2/3`", "ok": True, "feedback": "Exacto: 2 = 1 y 3/3; al restar 1/3 queda 1 y 2/3."},
                    {"text": "`2 y 2/3`", "ok": False, "feedback": "Si restás a 2, el resultado tiene que ser menor que 2."},
                    {"text": "`1 y 1/3`", "ok": False, "feedback": "3/3 − 1/3 deja 2/3, no 1/3."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué el denominador no cambia al sumar y cómo hacés `1 − 3/8` mentalmente.",
    },
    "a-sumar-restar-fracciones-distinto": {
        "hook": {
            "question": "No podés sumar `2 dólares + 3 pesos` y decir que tenés `5` sin pasarlos primero a la misma moneda. ¿Por qué con `2/3 + 1/4` pasa exactamente lo mismo?",
            "intuition": "Tercios y cuartos son porciones de distinto tamaño. Antes de sumar o restar hay que **traducir ambas fracciones al mismo corte** (un denominador común, como doceavos: `8/12 + 3/12 = 11/12`).",
        },
        "concept": {
            "points": [
                "**Buscá un denominador común**: el número más chico que esté en las tablas de ambos denominadores (mcm). Si uno ya es múltiplo del otro (ej. `2` y `8`), ¡usá el mayor (`8`)!",
                "**Convertí a fracciones equivalentes**: multiplicá arriba y abajo de cada fracción para llegar al denominador común sin cambiar su valor.",
                "**Recién ahí sumá o restá arriba**: mantené el denominador común intacto.",
                "**Simplificá al final**: revisá si numerador y denominador comparten algún divisor.",
            ],
            "real_world": [
                {
                    "title": "Combinar tiempos distintos",
                    "detail": "Media hora (`1/2`) + un tercio de hora (`1/3`, 20 min) = `3/6 + 2/6 = 5/6` de hora (50 min).",
                },
                {
                    "title": "Mezclar ingredientes en cocina o pintura",
                    "detail": "`2/3` L + `1/4` L = `8/12 + 3/12 = 11/12` L (casi 1 litro entero).",
                },
                {
                    "title": "Medir espesores con pulgadas",
                    "detail": "Una arandela de `1/2\"` más una de `3/8\"` da `4/8 + 3/8 = 7/8\"`.",
                },
            ],
            "key_rule": "Mismo denominador primero (equivalentes) → Sumá/restá solo arriba → Simplificá.",
            "pitfall": "Cambiar el denominador para llegar al común olvidando multiplicar también el numerador (escribir `1/3` como `1/12` en vez de `4/12`).",
        },
        "example": {
            "title": "Visualizá `2/3 + 1/4` paso a paso",
            "steps": [
                "El múltiplo común más chico de `3` y `4` es `12`.",
                "Pasamos a doceavos: `2/3 × 4/4 = 8/12` y `1/4 × 3/3 = 3/12`.",
                "Ahora que todas las piezas son doceavos: `8/12 + 3/12 = 11/12`. Miralo dibujado en barras en el Laboratorio.",
            ],
            "lab_link": "math:fractions",
            "lab_cta": "Ver barras de 2/3 + 1/4 en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto da `1/2 + 1/4`?",
            "options": [
                {"text": "`2/6`", "ok": False, "feedback": "Nunca se suman numeradores y denominadores por separado."},
                {"text": "`3/4`", "ok": True, "feedback": "Exacto: 1/2 = 2/4, y 2/4 + 1/4 = 3/4."},
                {"text": "`2/4`", "ok": False, "feedback": "2/4 es solo 1/2; faltó sumarle el 1/4."},
            ],
        },
        "checks": [
            {
                "question": "Tenías `5/6` de litro de agua y tomaste `1/2` litro. ¿Cuánto queda (simplificado)?",
                "options": [
                    {"text": "`1/3` de litro", "ok": True, "feedback": "Exacto: 1/2 = 3/6 → 5/6 − 3/6 = 2/6 = 1/3."},
                    {"text": "`4/4` de litro", "ok": False, "feedback": "No se restan los denominadores entre sí."},
                    {"text": "`1/2` litro", "ok": False, "feedback": "5/6 − 3/6 deja 2/6 (= 1/3), no 3/6."},
                ],
            },
            {
                "question": "Para calcular `3/4 + 1/6`, ¿cuál es el denominador común más cómodo (mcm)?",
                "options": [
                    {"text": "12 (porque 12 está en la tabla del 4 y del 6)", "ok": True, "feedback": "Exacto: 9/12 + 2/12 = 11/12 (más chico y limpio que usar 24)."},
                    {"text": "10 (4 + 6)", "ok": False, "feedback": "10 no es múltiplo de 4 ni de 6."},
                    {"text": "6", "ok": False, "feedback": "6 no es múltiplo de 4."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en 2 frases por qué hace falta denominador común para sumar fracciones y cómo se convierte cada una.",
    },
    "a-multiplicar-fracciones": {
        "hook": {
            "question": "Desde chicos nos dicen que 'multiplicar agranda'. Entonces, ¿por qué `1/2 × 3/4` da `3/8`, que es MÁS CHICO que los dos?",
            "intuition": "Con fracciones, el signo `×` se lee como **'de'**. Calcular `1/2 × 3/4` es pedir **la mitad de tres cuartos** — y obviamente la mitad de algo tiene que ser más chica que ese algo.",
        },
        "concept": {
            "points": [
                "**La buena noticia**: para multiplicar fracciones **NO necesitás denominador común**. Multiplicás directo: `numerador × numerador` arriba y `denominador × denominador` abajo.",
                "**Fracción × entero**: escribí el entero sobre `1` (`3/4 × 20 = 3/4 × 20/1 = 60/4 = 15`), o más rápido: dividí primero por el de abajo (`20 ÷ 4 = 5`) y multiplicá por el de arriba (`5 × 3 = 15`).",
                "**Simplificar cruzado ahorra trabajo**: en `2/3 × 3/5`, el `3` arriba y el `3` abajo se cancelan antes de multiplicar → `2/5` directo.",
                "**Tamaño del resultado**: multiplicar por algo menor que `1` **achica** el número; multiplicar por algo mayor que `1` lo **agranda**.",
            ],
            "real_world": [
                {
                    "title": "Ajustar una receta a la mitad",
                    "detail": "Si la torta lleva `3/4` taza de leche, media receta lleva `1/2 × 3/4 = 3/8` taza.",
                },
                {
                    "title": "Descuentos rápidos en fracciones",
                    "detail": "Un producto de `$400` con `1/4` off te ahorra `$100` y pagás `3/4 × 400 = $300`.",
                },
                {
                    "title": "Fracción de tu tiempo",
                    "detail": "`3/4` de una clase de `2/3` de hora (40 min) = `6/12 = 1/2` hora (30 min).",
                },
            ],
            "key_rule": "`(a/b) × (c/d) = (a·c)/(b·d)` · No hace falta común denominador · Simplificá antes para números chicos.",
            "pitfall": "Multiplicar en cruz (como en división) o buscar denominador común sin necesidad y complicar las cuentas.",
        },
        "example": {
            "title": "Calculá `3/5` de `$250` en 2 segundos",
            "steps": [
                "En vez de hacer `3 × 250 = 750` y después dividir por `5`, dividí primero.",
                "Calculamos un quinto: `250 ÷ 5 = 50`.",
                "Tomamos 3 de esos quintos: `50 × 3 = $150`.",
            ],
            "lab_link": "math:fractions",
            "lab_cta": "Practicar fracciones en el Laboratorio",
        },
        "check": {
            "question": "Una receta lleva `2/3` de taza de avena y querés preparar la mitad (`1/2 × 2/3`). ¿Cuánto usás?",
            "options": [
                {"text": "`1/3` de taza", "ok": True, "feedback": "Exacto: (1×2)/(2×3) = 2/6 = 1/3 (la mitad de dos tercios es un tercio)."},
                {"text": "`3/5` de taza", "ok": False, "feedback": "Sumaste en vez de multiplicar."},
                {"text": "`4/3` de taza", "ok": False, "feedback": "Eso sería el doble, no la mitad."},
            ],
        },
        "checks": [
            {
                "question": "Sin hacer la cuenta exacta, ¿cómo será el resultado de `15 × 4/5` comparado con `15`?",
                "options": [
                    {"text": "Menor que 15 (porque `4/5 < 1`)", "ok": True, "feedback": "Exacto: da 12, estás tomando cuatro quintas partes de 15."},
                    {"text": "Mayor que 15", "ok": False, "feedback": "Solo daría mayor si la fracción fuera mayor que 1 (como 6/5)."},
                    {"text": "Igual a 15", "ok": False, "feedback": "Solo queda igual al multiplicar por 1 (5/5)."},
                ],
            },
            {
                "question": "Calculá `3/4 × 8/9` simplificando cruzado.",
                "options": [
                    {"text": "`2/3`", "ok": True, "feedback": "Exacto: 3/9 = 1/3 y 8/4 = 2 → 1/1 × 2/3 = 2/3 (o 24/36 = 2/3)."},
                    {"text": "`11/13`", "ok": False, "feedback": "Sumaste en lugar de multiplicar."},
                    {"text": "`27/32`", "ok": False, "feedback": "Multiplicaste en cruz en lugar de multiplicar en línea recta."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá por qué multiplicar por una fracción menor a 1 achica el resultado y cuál es la diferencia clave con sumar fracciones.",
    },
    "a-dividir-fracciones": {
        "hook": {
            "question": "Si tenés `3` kilos de café y armás bolsitas de `1/4` kg, te salen `12` bolsitas (`3 ÷ 1/4 = 12`). ¿Por qué dividir te dio un número 4 veces MÁS GRANDE?",
            "intuition": "Porque dividir pregunta **'¿cuántas veces cabe?'**. Como cada bolsita es chiquita (`1/4` kg), caben 4 por kilo, o sea `3 × 4 = 12`. ¡Esa es la razón real detrás de la regla de invertir y multiplicar!",
        },
        "concept": {
            "points": [
                "**Dividir = preguntar cuántas veces cabe**: `3 ÷ 1/4` pregunta cuántos cuartos caben en 3 → `12`. Por eso dividir por un número menor a `1` **agranda**.",
                "**El recíproco (dar vuelta)**: el recíproco de `c/d` es `d/c` (multiplicados siempre dan `1`).",
                "**La regla ('dejar, cambiar, invertir')**: `(a/b) ÷ (c/d) = (a/b) × (d/c)`. Solo se invierte la **segunda** fracción (el divisor), nunca la primera.",
                "**Truco de verificación**: podés pensar el mismo denominador (`3/4 ÷ 1/8 = 6/8 ÷ 1/8 = 6`): ¿cuántos octavos entran en 6 octavos? Exactamente `6`.",
            ],
            "real_world": [
                {
                    "title": "Fraccionar compras a granel",
                    "detail": "Con `3/4` kg de yerba en porciones de `1/8` kg salen `3/4 ÷ 1/8 = 6` termos.",
                },
                {
                    "title": "Cortar madera o cable en tramos iguales",
                    "detail": "Un cable de `6 m` cortado en piezas de `3/4 m` da `6 × 4/3 = 8` cables iguales.",
                },
                {
                    "title": "Repartir sobras entre amigos",
                    "detail": "`1/2` torta dividida entre `3` (`1/2 ÷ 3/1 = 1/2 × 1/3`) da `1/6` de torta para cada uno.",
                },
            ],
            "key_rule": "`(a/b) ÷ (c/d) = (a/b) × (d/c)` · Solo invertís el divisor (la segunda fracción) · Dividir por `< 1` agranda.",
            "pitfall": "Dar vuelta la PRIMERA fracción en vez de la segunda (o dar vuelta las dos), lo cual invierte por completo el resultado.",
        },
        "example": {
            "title": "Resolvé `3/4 ÷ 1/8` de dos maneras",
            "steps": [
                "Manera intuitiva: pasamos `3/4` a octavos → `6/8`. ¿Cuántas veces cabe `1/8` en `6/8`? Exactamente `6` veces.",
                "Manera rápida (recíproco): dejamos `3/4`, cambiamos `÷` por `×`, invertimos `1/8` a `8/1`.",
                "Calculamos: `3/4 × 8/1 = 24/4 = 6`. Exactamente igual.",
            ],
            "lab_link": "math:fractions",
            "lab_cta": "Repasar fracciones en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál operación es equivalente a `2/5 ÷ 3/4`?",
            "options": [
                {"text": "`2/5 × 4/3` (= `8/15`)", "ok": True, "feedback": "Exacto: dejás la primera igual e invertís la segunda."},
                {"text": "`5/2 × 3/4`", "ok": False, "feedback": "Invertiste la primera fracción en vez de la segunda."},
                {"text": "`2/5 × 3/4`", "ok": False, "feedback": "Eso es multiplicar, no dividir; faltó invertir el divisor."},
            ],
        },
        "checks": [
            {
                "question": "Tenés `4` litros de jugo y vasos de `1/2` litro. ¿Cuántos vasos llenás (`4 ÷ 1/2`)?",
                "options": [
                    {"text": "2 vasos", "ok": False, "feedback": "2 es 4 × 1/2 (la mitad de 4); en cada litro caben 2 vasos de medio litro."},
                    {"text": "8 vasos", "ok": True, "feedback": "Exacto: 4 × 2 = 8 vasos."},
                    {"text": "6 vasos", "ok": False, "feedback": "4 litros × 2 medios litros por litro = 8."},
                ],
            },
            {
                "question": "Quedó `3/4` de pizza y la repartís entre `3` personas (`3/4 ÷ 3`). ¿Qué fracción de pizza come cada uno?",
                "options": [
                    {"text": "`1/4`", "ok": True, "feedback": "Exacto: tres cuartos repartidos entre tres da un cuarto para cada uno (3/4 × 1/3 = 1/4)."},
                    {"text": "`9/4`", "ok": False, "feedback": "Multiplicaste por 3 en vez de dividir por 3."},
                    {"text": "`1/12`", "ok": False, "feedback": "Faltó el 3 del numerador: 3/12 simplifica a 1/4."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con un ejemplo real por qué `3 ÷ 1/4 = 12` y qué fracción se invierte al dividir.",
    },
    # ==================== NIVEL 4: DECIMALES Y POTENCIAS ====================
    "a-decimales-valor-posicional": {
        "hook": {
            "question": "En una carrera, un corredor saca `0.4` s de ventaja y otro `0.35` s. ¿Por qué tanta gente piensa equivocadamente que `0.35` es mayor que `0.4`?",
            "intuition": "Porque el cerebro compara `35` contra `4` como si fueran enteros. Pero después de la coma, los ceros al final no cambian el valor: `0.4` es lo mismo que **`0.40`** (40 centavos > 35 centavos).",
        },
        "concept": {
            "points": [
                "**Los decimales son fracciones disfrazadas de potencias de 10**: 1er lugar = **décimos** (`/10`), 2º = **centésimos** (`/100`), 3º = **milésimos** (`/1000`).",
                "**Comparar sin trampas**: completá con ceros a la derecha hasta que tengan el mismo largo (`0.4` → `0.40` vs. `0.35`) y compará de izquierda a derecha.",
                "**Equivalencias clave para la vida diaria**: `1/2 = 0.5`, `1/4 = 0.25`, `3/4 = 0.75`, `1/5 = 0.2`, `1/10 = 0.1`, `1/8 = 0.125`.",
                "**Redondear decimales**: misma regla que en enteros — mirás la cifra justo a la derecha del corte (`≥ 5` sube, `< 5` queda igual).",
            ],
            "real_world": [
                {
                    "title": "Dinero y balanzas digitales",
                    "detail": "Cuando pedís `3/4 kg` en la fiambrería, la balanza marca `0.750 kg`; medio kilo es `0.500 kg`.",
                },
                {
                    "title": "Cronómetros y electrónica",
                    "detail": "Un LED de `3.3 V` o una pausa de `0.025 s` (25 milisegundos) usan décimos y milésimos todo el tiempo.",
                },
                {
                    "title": "Redondeo de precios y promedios",
                    "detail": "Un promedio de `7.68` redondeado a 1 decimal sube a `7.7` porque el centésimo (`8`) es `≥ 5`.",
                },
            ],
            "key_rule": "Posiciones tras la coma: décimos (`0.1`), centésimos (`0.01`), milésimos (`0.001`) · Agregá ceros al final para comparar.",
            "pitfall": "Creer que más cifras después de la coma significa un número más grande (`0.125` es MENOR que `0.2`, porque `0.200 > 0.125`).",
        },
        "example": {
            "title": "Ordená tres medidas de menor a mayor sin equivocarte",
            "steps": [
                "Tenemos tres espesores: `0.5 mm`, `0.18 mm` y `0.45 mm`.",
                "Igualamos a 2 decimales agregando ceros al final: `0.50`, `0.18` y `0.45`.",
                "Ahora el orden es evidente: `0.18 < 0.45 < 0.50`.",
            ],
            "lab_link": "math:decimals",
            "lab_cta": "Practicar decimales en el Laboratorio",
        },
        "check": {
            "question": "¿Cuál de estos números es el MÁS GRANDE?",
            "options": [
                {"text": "`0.6`", "ok": True, "feedback": "Exacto: equivale a 0.600, mayor que 0.590 y 0.099."},
                {"text": "`0.59`", "ok": False, "feedback": "0.59 tiene 5 décimos; 0.6 tiene 6 décimos (0.60)."},
                {"text": "`0.099`", "ok": False, "feedback": "Tiene un 0 en los décimos: es menor que 0.1."},
            ],
        },
        "checks": [
            {
                "question": "Una balanza digital marca `0.25 kg`. ¿A qué fracción de kilo equivale?",
                "options": [
                    {"text": "`1/4` kg", "ok": True, "feedback": "Exacto: 25/100 simplificado por 25 es 1/4."},
                    {"text": "`1/25` kg", "ok": False, "feedback": "0.25 es 25/100 (un cuarto), mucho más grande que 1/25 (0.04)."},
                    {"text": "`1/2` kg", "ok": False, "feedback": "1/2 kg es 0.50 kg."},
                ],
            },
            {
                "question": "Redondeá `4.836` a 2 decimales (centésimos).",
                "options": [
                    {"text": "`4.84`", "ok": True, "feedback": "Exacto: el tercer decimal es 6 (≥ 5), así que el 3 sube a 4."},
                    {"text": "`4.83`", "ok": False, "feedback": "Como sigue un 6, hay que redondear hacia arriba."},
                    {"text": "`4.8`", "ok": False, "feedback": "Eso tiene solo 1 decimal (décimos)."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá el truco de agregar ceros al final para comparar decimales sin caer en la trampa de la cantidad de dígitos.",
    },
    "a-sumar-restar-decimales": {
        "hook": {
            "question": "Si pagás `$3.65` con un billete de `$10`, ¿por qué sumar o restar decimales es exactamente igual a manejar pesos y centavos?",
            "intuition": "Todo el secreto se resume en una regla: **alineá la coma decimal**. Cuando alineás la coma y rellenás con ceros invisibles (`10.00 − 3.65`), sumás unidades con unidades y centavos con centavos, igual que una suma común.",
        },
        "concept": {
            "points": [
                "**Alineá la coma verticalmente**: nunca alinees al borde derecho si tienen distinta cantidad de decimales (`1.8 + 0.45` va con las comas una debajo de la otra).",
                "**Ceros de relleno**: todo entero tiene una coma invisible al final (`10 = 10.00`), y `1.8 = 1.80`. Rellenar los huecos elimina casi todos los errores.",
                "**Bajá la coma al resultado** en la misma columna vertical.",
                "**Chequeo con enteros**: antes de confirmar `1.8 + 0.45`, estimá `~2 + 0.5 = 2.5`. Si te dio `0.63` o `22.5`, la coma quedó mal.",
            ],
            "real_world": [
                {
                    "title": "Tickets y vueltos",
                    "detail": "`$10.00 − $3.65`: +0.35 llega a `$4`, +6 llega a `$10` → `$6.35`.",
                },
                {
                    "title": "Almacenamiento en tu celular (GB)",
                    "detail": "Una app de `1.8 GB` + un video de `0.45 GB` = `1.80 + 0.45 = 2.25 GB`.",
                },
                {
                    "title": "Medir voltajes con multímetro",
                    "detail": "Una batería baja de `4.20 V` a `3.35 V`: perdió `0.85 V`.",
                },
            ],
            "key_rule": "Alineá la coma · Rellená huecos con ceros (`5 = 5.00`) · Operá como enteros y bajá la coma.",
            "pitfall": "Alinear `1.8` y `0.45` a la derecha y sumar `8 + 5` (mezclando décimos con centésimos).",
        },
        "example": {
            "title": "Calculá `5 − 1.38` sin enredos",
            "steps": [
                "Escribimos `5` con dos ceros decimales: `5.00 − 1.38`.",
                "Truco rápido de vuelto: de `1.38` a `2.00` faltan `0.62`; de `2.00` a `5.00` faltan `3.00`.",
                "Total: `3.62`. Verificación: `3.62 + 1.38 = 5.00`.",
            ],
            "lab_link": "math:decimals",
            "lab_cta": "Practicar suma y resta de decimales en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto da `2.5 + 0.35`?",
            "options": [
                {"text": "`2.85`", "ok": True, "feedback": "Exacto: 2.50 + 0.35 = 2.85."},
                {"text": "`0.60`", "ok": False, "feedback": "Alineaste a la derecha; 2.5 ya es mayor que 2."},
                {"text": "`2.40`", "ok": False, "feedback": "Sumaste el 5 con el 5 en los centésimos en vez de en los décimos."},
            ],
        },
        "checks": [
            {
                "question": "Tenés `$20` y gastás `$4.75`. ¿Cuánto te queda?",
                "options": [
                    {"text": "`$16.25`", "ok": False, "feedback": "Chequeá con suma: 16.25 + 4.75 = 21.00 (te pasaste por 1)."},
                    {"text": "`$15.25`", "ok": True, "feedback": "Exacto: 15.25 + 4.75 = 20.00."},
                    {"text": "`$15.75`", "ok": False, "feedback": "0.75 + 0.75 da 1.50, no 1.00."},
                ],
            },
            {
                "question": "Un cable mide `3.2 m` y cortás `0.85 m`. ¿Cuánto cable queda?",
                "options": [
                    {"text": "`2.35 m`", "ok": True, "feedback": "Exacto: 3.20 − 0.85 = 2.35 m."},
                    {"text": "`2.65 m`", "ok": False, "feedback": "2.65 + 0.85 = 3.50, no 3.20."},
                    {"text": "`3.65 m`", "ok": False, "feedback": "Restaste 5 − 2 al revés en vez de usar 3.20."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué hacés cuando tenés que restar un decimal a un número entero como `10 − 3.65`.",
    },
    "a-multiplicar-dividir-decimales": {
        "hook": {
            "question": "¿Por qué `0.3 × 0.4` da `0.12` (y NO `1.2`), mientras `6 ÷ 0.5` da `12` (el DOBLE de 6)?",
            "intuition": "En multiplicación y división con decimales NO alineás comas: hacés la cuenta como si fueran enteros y después ubicás la coma con dos reglas ultra simples (y un chequeo rápido de estimación).",
        },
        "concept": {
            "points": [
                "**Multiplicar decimales**: (1) ignorá las comas y multiplicá normal (`3 × 4 = 12`); (2) sumá cuántas cifras decimales había entre los dos factores (`1 + 1 = 2`); (3) poné la coma dejando esa cantidad de decimales (`0.12`).",
                "**Dividir por un entero**: dividís normal y subís la coma al cociente justo cuando cruzás la coma del dividendo (`18.6 ÷ 3 = 6.2`).",
                "**Dividir por un decimal**: ¡nunca dividas por un decimal directo! Corré la coma hacia la derecha la **misma cantidad de lugares** en ambos números (×10 o ×100) hasta que el divisor sea entero (`3.6 ÷ 2.4 = 36 ÷ 24 = 1.5`).",
                "**Red de seguridad**: estimá siempre con enteros (`3.2 × 2.5 ≈ 3 × 2.5 = 7.5`, así sabés que es `8.0`, nunca `80` ni `0.8`).",
            ],
            "real_world": [
                {
                    "title": "Comprar por peso en la verdulería",
                    "detail": "`2.5 kg` a `$3.20/kg`: `32 × 25 = 800`, 2 decimales → `$8.00`.",
                },
                {
                    "title": "Fraccionar en botellas de medio litro",
                    "detail": "`6 L ÷ 0.5 L` = `60 ÷ 5` = `12` botellas.",
                },
                {
                    "title": "Calcular el precio por litro o por unidad",
                    "detail": "Si `2.4 L` costaron `$3.60`, cada litro sale `36 ÷ 24 = $1.50`.",
                },
            ],
            "key_rule": "Multiplicar: contá el total de decimales · Dividir por decimal: corré la coma igual en ambos hasta tener divisor entero.",
            "pitfall": "Correr la coma solo en el divisor y olvidarte de correrla también en el dividendo (transformar `6 ÷ 0.5` en `6 ÷ 5 = 1.2` en vez de `60 ÷ 5 = 12`).",
        },
        "example": {
            "title": "Calculá `3.2 × 2.5` y `3.6 ÷ 2.4`",
            "steps": [
                "Para `3.2 × 2.5`: multiplicamos `32 × 25 = 800`. Entre `3.2` (1 decimal) y `2.5` (1 decimal) suman 2 decimales → `8.00`.",
                "Para `3.6 ÷ 2.4`: multiplicamos ambos por 10 para sacar la coma → `36 ÷ 24`.",
                "Simplificamos por 12: `3 ÷ 2 = 1.5`. Chequeo: `1.5 × 2.4 = 3.6`.",
            ],
            "lab_link": "math:decimals",
            "lab_cta": "Practicar decimales en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto da `0.2 × 0.5`?",
            "options": [
                {"text": "`0.10` (= `0.1`)", "ok": True, "feedback": "Exacto: 2 × 5 = 10, con 2 lugares decimales queda 0.10 = 0.1 (la mitad de 0.2)."},
                {"text": "`1.0`", "ok": False, "feedback": "Faltó contar un decimal: 0.2 (1) + 0.5 (1) = 2 lugares decimales."},
                {"text": "`0.01`", "ok": False, "feedback": "Corriste 3 lugares en vez de 2."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuál división tiene el mismo resultado que `4.5 ÷ 0.15`?",
                "options": [
                    {"text": "`450 ÷ 15` (= `30`)", "ok": True, "feedback": "Exacto: multiplicaste ambos por 100 (2 lugares a la derecha)."},
                    {"text": "`45 ÷ 15` (= `3`)", "ok": False, "feedback": "Moviste 1 lugar en 4.5 y 2 lugares en 0.15: tiene que ser la misma cantidad en los dos."},
                    {"text": "`4.5 ÷ 15`", "ok": False, "feedback": "Si multiplicás el divisor por 100, también tenés que multiplicar el dividendo por 100."},
                ],
            },
            {
                "question": "Si `4.1 × 3.9` lo resolviste como `41 × 39 = 1599`, ¿dónde va la coma?",
                "options": [
                    {"text": "`15.99`", "ok": True, "feedback": "Exacto: 2 decimales en total, y además 4 × 4 = 16 lo confirma."},
                    {"text": "`159.9`", "ok": False, "feedback": "4 × 4 ronda 16, nunca 160."},
                    {"text": "`1.599`", "ok": False, "feedback": "4 × 4 ronda 16, no 1.6."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en 2 frases cómo ubicás la coma al multiplicar decimales y qué hacés al dividir por un decimal.",
    },
    "a-exponentes-potencias-10": {
        "hook": {
            "question": "¿Por qué `2 + 3 × 4` da `14` y NO `20`, y por qué `10³` hace tan fácil pasar de kilómetros a metros o de kΩ a Ω?",
            "intuition": "Los exponentes abrevian multiplicaciones repetidas (`2⁴ = 2×2×2×2`). Y en matemáticas todos acordamos el mismo orden (**PEMDAS**) para que una cuenta escrita tenga una sola respuesta correcta en cualquier lugar del mundo.",
        },
        "concept": {
            "points": [
                "**Qué es un exponente (`bⁿ`)**: multiplicar la base `b` por sí misma `n` veces (`3² = 3×3 = 9`, `2³ = 2×2×2 = 8`). ¡Nunca es `base × exponente`!",
                "**Potencias de 10**: `10¹ = 10`, `10² = 100`, `10³ = 1000` (el exponente cuenta los ceros). Multiplicar por `10ⁿ` corre la coma `n` lugares a la **derecha**; dividir por `10ⁿ` la corre `n` lugares a la **izquierda**.",
                "**Producto de igual base**: `10² × 10³ = 10⁵` (sumás los exponentes). Y cualquier número distinto de cero elevado a `0` da `1` (`10⁰ = 1`).",
                "**Orden de operaciones (PEMDAS)**: **P**aréntesis → **E**xponentes → **M**ultiplicación/**D**ivisión (de izquierda a derecha) → **A**dición/**S**ustracción, o sea sumas y restas (de izquierda a derecha).",
            ],
            "real_world": [
                {
                    "title": "Prefijos en tecnología y física",
                    "detail": "`kilo = 10³` (1000), `mega = 10⁶` (millón), `giga = 10⁹`. Un archivo de `2.5 × 10³` MB son `2500 MB`.",
                },
                {
                    "title": "Tickets combinados",
                    "detail": "1 entrada (`$5`) + 3 bebidas (`$2` c/u) = `5 + 3 × 2 = 11` (multiplicás primero las bebidas).",
                },
                {
                    "title": "Crecimiento rápido (duplicación)",
                    "detail": "Doblar un papel 10 veces multiplica su grosor por `2¹⁰ = 1024` veces.",
                },
            ],
            "key_rule": "`bⁿ` = multiplicar `b` por sí misma `n` veces · `×10ⁿ` corre la coma a la derecha · Orden: Paréntesis → Exponentes → ×/÷ → +/−.",
            "pitfall": "Calcular `3⁴` como `3 × 4 = 12` (en realidad es `3×3×3×3 = 81`) o resolver `5 + 3 × 2` de izquierda a derecha como `8 × 2 = 16`.",
        },
        "example": {
            "title": "Resolvé `2 + 3 × (4 − 1)²` en orden",
            "steps": [
                "Paréntesis primero: `4 − 1 = 3` → queda `2 + 3 × 3²`.",
                "Exponentes antes que multiplicar: `3² = 9` → queda `2 + 3 × 9`.",
                "Multiplicación antes que suma: `3 × 9 = 27`, y recién al final `2 + 27 = 29`.",
            ],
            "lab_link": "math:powers",
            "lab_cta": "Practicar potencias y exponentes en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto vale `3³`?",
            "options": [
                {"text": "9", "ok": False, "feedback": "Hiciste 3 × 3 (eso es 3²); falta multiplicar por 3 una vez más."},
                {"text": "27", "ok": True, "feedback": "Exacto: 3 × 3 × 3 = 27."},
                {"text": "6", "ok": False, "feedback": "Sumaste 3 + 3; un exponente multiplica repetidamente."},
            ],
        },
        "checks": [
            {
                "question": "¿Cuánto da `4.2 × 10³`?",
                "options": [
                    {"text": "4200", "ok": True, "feedback": "Exacto: corrés la coma 3 lugares hacia la derecha."},
                    {"text": "420", "ok": False, "feedback": "Eso sería × 10² (2 lugares); 10³ son 3 lugares."},
                    {"text": "126", "ok": False, "feedback": "10³ es 1000, no 30."},
                ],
            },
            {
                "question": "Resolvé `20 − 4 × 3` respetando PEMDAS.",
                "options": [
                    {"text": "48", "ok": False, "feedback": "Restaste antes de multiplicar (16 × 3). Siempre se multiplica primero."},
                    {"text": "8", "ok": True, "feedback": "Exacto: primero 4 × 3 = 12, después 20 − 12 = 8."},
                    {"text": "13", "ok": False, "feedback": "4 × 3 = 12 y 20 − 12 = 8."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué hace `×10ⁿ` y `÷10ⁿ` con la coma decimal y en qué orden se resuelve una cuenta combinada.",
    },
    # ==================== NIVEL 5: NÚMEROS NEGATIVOS ====================
    "a-sumar-restar-negativos": {
        "hook": {
            "question": "Si debés `$30` (tenés una multa de `−$30`) y el banco decide **anularte** (restarte) esa multa, ¿terminás con más o con menos plata?",
            "intuition": "Terminás con `$30` MÁS. Por eso en matemáticas **restar un número negativo equivale a sumar**: `50 − (−30) = 50 + 30 = 80`. Quitar una deuda siempre suma.",
        },
        "concept": {
            "points": [
                "**La recta numérica**: hacia la derecha los números siempre **crecen**, hacia la izquierda **decrecen**. Por eso `−3` es MAYOR que `−8` (`−3°C` es más cálido que `−8°C`).",
                "**Valor absoluto (`|x|`)**: es la distancia al `0` sin importar el lado (`|−7| = 7` y `|7| = 7`). Siempre es positivo o cero.",
                "**Sumar en la recta**: sumar un positivo mueve a la **derecha** (`−5 + 12 = +7`); sumar un negativo (o restar un positivo) mueve a la **izquierda** (`−4 − 3 = −7`).",
                "**Restar un negativo = sumar**: `a − (−b) = a + b`. Dos signos menos pegados se convierten en un más.",
            ],
            "real_world": [
                {
                    "title": "Termómetro bajo cero",
                    "detail": "Si amanece en `−5°C` y sube `12°C`, pasás por `0°C` (+5) y llegás a `+7°C`.",
                },
                {
                    "title": "Saldos bancarios y tarjetas",
                    "detail": "Estar en `−$400` y gastar `$250` más te deja en `−$650`; que te devuelvan un cargo de `−$100` te sube a `−$550`.",
                },
                {
                    "title": "Subsuelos de un edificio o nivel del mar",
                    "detail": "Subir del subsuelo `−2` al piso `+5` son `5 − (−2) = 7` pisos de recorrido.",
                },
            ],
            "key_rule": "Más a la derecha = mayor (`−3 > −8`) · `|−7| = |7| = 7` · Restar un negativo es sumar: `a − (−b) = a + b`.",
            "pitfall": "Pensar que `−10` es mayor que `−2` porque `10 > 2`, o confundir `−4 − 3` con `+7` (al sumar/restar NO se aplica 'menos por menos = más'!).",
        },
        "example": {
            "title": "Seguí un saldo bancario con negativos",
            "steps": [
                "Arrancás con `−$200` (descubierto).",
                "Depositás `$500`: `−200 + 500 = +$300`.",
                "Te anulan una comisión de `−$45`: `300 − (−45) = 300 + 45 = +$345`.",
            ],
            "lab_link": "math:integers",
            "lab_cta": "Practicar enteros y signos en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto da `−6 − 4`?",
            "options": [
                {"text": "`−10`", "ok": True, "feedback": "Exacto: estás en −6 y bajás 4 lugares más hacia la izquierda → −10."},
                {"text": "`+10`", "ok": False, "feedback": "'Menos por menos = más' es SOLO para multiplicar/dividir, no para restar."},
                {"text": "`−2`", "ok": False, "feedback": "−2 sería −6 + 4 (subir 4)."},
            ],
        },
        "checks": [
            {
                "question": "Resolvé `7 − (−5)`.",
                "options": [
                    {"text": "`12`", "ok": True, "feedback": "Exacto: restar un negativo equivale a sumar → 7 + 5 = 12."},
                    {"text": "`2`", "ok": False, "feedback": "2 es 7 − 5; acá estás restando −5 (quitando una deuda)."},
                    {"text": "`−12`", "ok": False, "feedback": "Arrancás en +7 y subís 5, así que queda positivo."},
                ],
            },
            {
                "question": "Subís en ascensor desde el subsuelo `−3` hasta el piso `4`. ¿Cuántos pisos subiste (`4 − (−3)`)?",
                "options": [
                    {"text": "7 pisos", "ok": True, "feedback": "Exacto: 3 pisos hasta planta baja (0) + 4 pisos arriba = 7."},
                    {"text": "1 piso", "ok": False, "feedback": "Restaste 4 − 3 olvidando el signo negativo del subsuelo."},
                    {"text": "−7 pisos", "ok": False, "feedback": "La cantidad de pisos subidos es positiva."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con un ejemplo de dinero o temperatura por qué `−6 − 4 = −10` mientras `6 − (−4) = 10`.",
    },
    "a-multiplicar-dividir-negativos": {
        "hook": {
            "question": "Si una deuda de `$5` (`−5`) se te cobra `3` veces (`3 × −5 = −15`), ¿por qué **cancelar** (`−3`) esas 3 deudas de `−$5` te da **`+$15`**?",
            "intuition": "Ese es el verdadero porqué de `menos × menos = más`: deshacer una pérdida repetida produce una ganancia. Lo mismo vale exactamente para dividir.",
        },
        "concept": {
            "points": [
                "**Regla de signos (SOLO para multiplicar y dividir)**:\n  • **Signos iguales → Positivo (`+`)**: `+ × + = +` y `− × − = +`\n  • **Signos distintos → Negativo (`−`)**: `+ × − = −` y `− × + = −`",
                "**En la división vale exactamente la misma regla**: `(−20) ÷ 4 = −5`, y `(−20) ÷ (−4) = +5`.",
                "**Varios factores negativos**: contá cuántos signos `−` multiplican. Cantidad **par** (2, 4…) → positivo; cantidad **impar** (1, 3…) → negativo.",
                "**Cuidado con los exponentes y paréntesis**: `(−3)² = (−3)×(−3) = +9`, pero `−3² = −(3×3) = −9` (sin paréntesis el cuadrado afecta solo al `3`).",
            ],
            "real_world": [
                {
                    "title": "Descenso constante de temperatura",
                    "detail": "Si la temperatura cambia `−2°C` por hora (baja 2 grados) durante `5` horas, el cambio total es `5 × (−2) = −10°C`.",
                },
                {
                    "title": "Reembolso de cargos duplicados",
                    "detail": "Que te anulen (`−4`) cuatro débitos de `−$10` suma `(−4) × (−10) = +$40` a tu favor.",
                },
                {
                    "title": "Puente directo a Física y Álgebra",
                    "detail": "En física la aceleración negativa (frenado) y el trabajo negativo usan exactamente estas reglas de signos.",
                },
            ],
            "key_rule": "Multiplicar/Dividir: signos iguales → `+`, signos distintos → `−` · Par de `−` = `+`, impar de `−` = `−`.",
            "pitfall": "Aplicar 'menos por menos = más' cuando en realidad estás SUMANDO dos negativos (`−5 − 3` es `−8`, nunca `+8`).",
        },
        "example": {
            "title": "Combiná PEMDAS y signos en `12 − 3 × (2 − 6)`",
            "steps": [
                "Resolvemos el paréntesis: `2 − 6 = −4` → queda `12 − 3 × (−4)`.",
                "Multiplicamos respetando los signos: `(−3) × (−4) = +12` (signos iguales → positivo).",
                "Sumamos al final: `12 + 12 = 24`. Probalo con variaciones aleatorias en el Laboratorio.",
            ],
            "lab_link": "math:integers",
            "lab_cta": "Practicar signos y PEMDAS en el Laboratorio",
        },
        "check": {
            "question": "¿Cuánto da `(−6) × (−7)`?",
            "options": [
                {"text": "`42`", "ok": True, "feedback": "Exacto: signos iguales al multiplicar dan positivo."},
                {"text": "`−42`", "ok": False, "feedback": "Sería negativo solo si uno fuera positivo y el otro negativo."},
                {"text": "`−13`", "ok": False, "feedback": "Eso es −6 − 7 (suma/resta), no multiplicación."},
            ],
        },
        "checks": [
            {
                "question": "Un buzo desciende `36 m` (`−36`) a ritmo constante en `9` segundos. ¿Cuántos metros cambia por segundo (`−36 ÷ 9`)?",
                "options": [
                    {"text": "`−4 m/s`", "ok": True, "feedback": "Exacto: signos distintos en división dan negativo (−4 m cada segundo)."},
                    {"text": "`+4 m/s`", "ok": False, "feedback": "El signo positivo indicaría que está subiendo."},
                    {"text": "`−27 m/s`", "ok": False, "feedback": "Restaste 36 − 9 en vez de dividir."},
                ],
            },
            {
                "question": "¿Cuál es el signo de `(−1) × (−2) × (−3) × (−4)`?",
                "options": [
                    {"text": "Positivo (`+24`), porque hay 4 factores negativos (cantidad par)", "ok": True, "feedback": "Exacto: cada pareja de negativos se vuelve positiva."},
                    {"text": "Negativo (`−24`), porque todos son negativos", "ok": False, "feedback": "Cada par de signos menos se cancela y da positivo; 4 es par."},
                    {"text": "Cero", "ok": False, "feedback": "Solo da cero si alguno de los factores es 0."},
                ],
            },
        ],
        "takeaway_prompt": "Resumí la regla de signos para multiplicar/dividir y en qué se diferencia de sumar dos negativos.",
    },
}

# Tag all 17 Arithmetic nodes with section="Aritmética", then append Preálgebra (#18-#29), Álgebra 1 (#30-#41), Geometría (#42-#51), Álgebra 2 (#52-#62), Trigonometría (#63-#68), Precálculo (#69-#76), Cálculo 1 (#77-#84), Cálculo 2 (#85-#91), Cálculo multivariable (#92-#99), Ecuaciones diferenciales (#100-#105) and Álgebra lineal (#106-#112)
for _node in MATH_DOMAIN["nodes"]:
    _node.setdefault("metadata", {})["section"] = "Aritmética"

MATH_DOMAIN["nodes"].extend(PREALGEBRA_NODES)
MATH_DOMAIN["nodes"].extend(ALGEBRA1_NODES)
MATH_DOMAIN["nodes"].extend(GEOMETRY_NODES)
MATH_DOMAIN["nodes"].extend(ALGEBRA2_NODES)
MATH_DOMAIN["nodes"].extend(TRIGONOMETRY_NODES)
MATH_DOMAIN["nodes"].extend(PRECALCULUS_NODES)
MATH_DOMAIN["nodes"].extend(CALCULUS1_NODES)
MATH_DOMAIN["nodes"].extend(CALCULUS2_NODES)
MATH_DOMAIN["nodes"].extend(MULTIVARIABLE_NODES)
MATH_DOMAIN["nodes"].extend(DIFFEQ_NODES)
MATH_DOMAIN["nodes"].extend(LINALG_NODES)
MATH_LESSONS.update(PREALGEBRA_LESSONS)
MATH_LESSONS.update(ALGEBRA1_LESSONS)
MATH_LESSONS.update(GEOMETRY_LESSONS)
MATH_LESSONS.update(ALGEBRA2_LESSONS)
MATH_LESSONS.update(TRIGONOMETRY_LESSONS)
MATH_LESSONS.update(PRECALCULUS_LESSONS)
MATH_LESSONS.update(CALCULUS1_LESSONS)
MATH_LESSONS.update(CALCULUS2_LESSONS)
MATH_LESSONS.update(MULTIVARIABLE_LESSONS)
MATH_LESSONS.update(DIFFEQ_LESSONS)
MATH_LESSONS.update(LINALG_LESSONS)

# Entrance-exam algebra topics added later live in their own module. Each of those nodes
# names the existing node it follows; positions and "N." prefixes are derived here.
from backend.algebra_ingreso_content import ALGEBRA_INGRESO_LESSONS, ALGEBRA_INGRESO_NODES  # noqa: E402
from backend.content_merge import insert_nodes, renumber  # noqa: E402
from backend.ingreso_math_a_content import INGRESO_MATH_A_LESSONS, INGRESO_MATH_A_NODES  # noqa: E402
from backend.ingreso_math_b_content import INGRESO_MATH_B_LESSONS, INGRESO_MATH_B_NODES  # noqa: E402
from backend.ingreso_math_c_content import INGRESO_MATH_C_LESSONS, INGRESO_MATH_C_NODES  # noqa: E402

# Topics added to follow the UNCuyo 2027 entrance syllabus (sets, radicals, absolute value,
# study of functions, linear systems, quadratic forms, polygons, factoring cases, exponential/log graphs, angle measure and reduction formulas).
insert_nodes(MATH_DOMAIN["nodes"], ALGEBRA_INGRESO_NODES + INGRESO_MATH_A_NODES + INGRESO_MATH_B_NODES + INGRESO_MATH_C_NODES)
renumber(MATH_DOMAIN["nodes"])
MATH_LESSONS.update(ALGEBRA_INGRESO_LESSONS)
MATH_LESSONS.update(INGRESO_MATH_A_LESSONS)
MATH_LESSONS.update(INGRESO_MATH_B_LESSONS)
MATH_LESSONS.update(INGRESO_MATH_C_LESSONS)
