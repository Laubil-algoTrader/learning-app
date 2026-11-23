"""Ejercicios del material oficial del Curso de Ingreso 2027 (Ingeniería UNCuyo): Física, unidades 1 a 3.

Fuente: "PRÁCTICA DEL CURSO" (ejercicios en clase + solucionario) de las unidades 1, 2 y 3, y de las
guías del material complementario: TP1 parte B, TP2 parte B, TP3 parte B1 y B2 (con grilla de
corrección). Las gráficas se describen con tablas de puntos o tramos.

Convenciones del ingreso: coma decimal, intervalos con ";", g = 9,8 m/s² salvo que el enunciado diga
otra cosa, y en caída libre eje y hacia arriba (g = −9,8 m/s²). Las diferencias con el solucionario se
explican en la resolución de cada problema.
"""

from __future__ import annotations


def N(prompt: str, value: float, unit: str, answer: str, tol: float = 0.0) -> dict:
    return {"prompt": prompt, "check": {"type": "numeric", "value": value, "tolerance": tol, "unit": unit}, "answer": answer}


def C(prompt: str, options: list[str], answer: str, correct: int = 0) -> dict:
    return {"prompt": prompt, "check": {"type": "choice", "options": options, "correct": correct}, "answer": answer}


def P(suffix, node, level, source, title, statement, parts, hints, solution) -> dict:
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


SN = " Podés escribirlo en notación científica (por ejemplo 1,23.10^4)."
SNX = " Escribilo en notación científica (por ejemplo 1,23.10^4)."

EXERCISES: list[dict] = [
    # ======================================================================
    # UNIDAD 1 · PRÁCTICA DEL CURSO
    # ======================================================================
    P(
        "u1-1", "f-analisis-dimensional", 1, "Física · Práctica U1, ej. 1",
        "Ecuaciones de dimensión de magnitudes conocidas",
        "Realizá el análisis dimensional para las siguientes magnitudes: volumen, velocidad, fuerza y presión "
        "(usá L para longitud, M para masa y T para tiempo).",
        [
            C("a) ¿Cuál es la ecuación de dimensión de la velocidad?",
              ["[v] = L·T⁻¹", "[v] = L·T⁻²", "[v] = M·L·T⁻¹", "[v] = L⁻¹·T"], "[v] = L·M⁰·T⁻¹"),
            C("b) ¿Cuál es la ecuación de dimensión de la fuerza?",
              ["[F] = M·L·T⁻²", "[F] = M·L·T⁻¹", "[F] = M·L²·T⁻²", "[F] = L·T⁻²"], "[F] = M·L·T⁻²"),
            C("c) ¿Cuál es la ecuación de dimensión de la presión?",
              ["[P] = M·L⁻¹·T⁻²", "[P] = M·L·T⁻²", "[P] = M·L⁻²·T⁻²", "[P] = M·L²·T⁻²"], "[P] = L⁻¹·M·T⁻²"),
        ],
        [
            "Partí de la definición de cada magnitud: velocidad = distancia / tiempo, fuerza = masa · aceleración, presión = fuerza / superficie.",
            "Reemplazá cada magnitud por su dimensión y operá con los exponentes: dividir resta exponentes.",
        ],
        [
            "Volumen = largo · ancho · alto: `[V] = L·L·L = L³·M⁰·T⁰`.",
            "Velocidad = distancia / tiempo: `[v] = L / T = L·M⁰·T⁻¹`.",
            "Aceleración = velocidad / tiempo: `[a] = L·T⁻¹ / T = L·T⁻²`.",
            "Fuerza = masa · aceleración: `[F] = M·L·T⁻²`.",
            "Presión = fuerza / superficie: `[P] = M·L·T⁻² / L² = L⁻¹·M·T⁻²`.",
            "Respuestas: `[v] = L·T⁻¹`, `[F] = M·L·T⁻²`, `[P] = L⁻¹·M·T⁻²`. Error típico en la presión: olvidarse de que la superficie es L² y dejar `M·L·T⁻²` (eso es fuerza).",
        ],
    ),
    P(
        "u1-2", "f-analisis-dimensional", 2, "Física · Práctica U1, ej. 2 y 3",
        "Dimensión de S, de K y de α/β",
        "Ejercicio 2: hallá la dimensión de S en la fórmula física `S = F·d / (m·v²)`, siendo m: masa; F: fuerza; "
        "v: velocidad; d: distancia. Hallá además qué magnitud es K si `K = F·v⁻¹ + Q`, siendo F: fuerza y v: velocidad.\n\n"
        "Ejercicio 3: determiná la dimensión de `[α/β]` sabiendo que `W = v²/α + F/β`, donde W es la magnitud trabajo, "
        "v es velocidad y F es fuerza.",
        [
            C("a) ¿Cuál es la dimensión de S?",
              ["S es adimensional ([S] = 1)", "[S] = L", "[S] = M·L²·T⁻²", "[S] = T"], "S es adimensional: [S] = L⁰·M⁰·T⁰ = 1"),
            C("b) ¿Qué magnitud es K?",
              ["Caudal másico (M·T⁻¹)", "Cantidad de movimiento (M·L·T⁻¹)", "Potencia (M·L²·T⁻³)", "Energía (M·L²·T⁻²)"],
              "Caudal másico: [K] = M·T⁻¹"),
            C("c) ¿Cuál es la dimensión de [α/β]?",
              ["L·M⁻¹", "M·L⁻¹", "M⁻¹", "L⁻¹·M⁻¹"], "[α/β] = L·M⁻¹·T⁰"),
        ],
        [
            "Para S: el trabajo `F·d` y la energía `m·v²` tienen la misma dimensión. ¿Qué queda al dividirlas?",
            "Por homogeneidad, en una suma todos los términos tienen la misma dimensión: `[K] = [F·v⁻¹] = [Q]`, y en el ejercicio 3 `[v²/α] = [W]` y `[F/β] = [W]`.",
            "Despejá `[α] = [v²]/[W]` y `[β] = [F]/[W]` por separado y recién después dividilas.",
        ],
        [
            "S: `[F·d] = M·L·T⁻²·L = M·L²·T⁻²` y `[m·v²] = M·(L·T⁻¹)² = M·L²·T⁻²`. El cociente da `L⁰·M⁰·T⁰`: **S es adimensional**.",
            "K: `[F·v⁻¹] = M·L·T⁻² / (L·T⁻¹) = M·T⁻¹`. Masa por unidad de tiempo: **caudal másico** (por ejemplo en kg/s). Por homogeneidad Q tiene la misma dimensión.",
            "Ejercicio 3, trabajo: `[W] = [F·d] = M·L²·T⁻²`.",
            "`[v²/α] = [W]` → `[α] = L²·T⁻² / (M·L²·T⁻²) = M⁻¹`.",
            "`[F/β] = [W]` → `[β] = M·L·T⁻² / (M·L²·T⁻²) = L⁻¹`.",
            "`[α/β] = M⁻¹ / L⁻¹ = L·M⁻¹·T⁰`. Error típico: invertir el cociente y responder `M·L⁻¹`.",
        ],
    ),
    P(
        "u1-4", "f-cifras-significativas", 1, "Física · Práctica U1, ej. 4",
        "Redondear a las cifras pedidas",
        "Escribí los siguientes números con la cantidad de cifras significativas que se piden: 0,357898 con 5 cifras "
        "significativas; 0,0156 con 1 cifra significativa; 2,356 con 1 cifra significativa; 1,356×10⁵ con 3 cifras "
        "significativas; 168,56 con 2 cifras significativas.",
        [
            C("a) 0,357898 con 5 cifras significativas:", ["0,35790", "0,3579", "0,35789", "0,357898"], "0,35790 (o 3,5790×10⁻¹)"),
            C("b) 0,0156 con 1 cifra significativa:", ["0,02", "0,01", "0,016", "0,0"], "0,02 (o 2×10⁻²)"),
            C("c) 168,56 con 2 cifras significativas:", ["1,7×10²", "1,6×10²", "17", "168"], "1,7×10²"),
        ],
        [
            "Los ceros a la izquierda del primer dígito distinto de cero NO son significativos; los ceros a la derecha de un dígito distinto de cero SÍ lo son.",
            "Cortá en la cifra pedida y mirá el dígito siguiente: si es mayor que 4, la última cifra sube una unidad.",
            "Si para respetar las cifras tenés que 'tapar' enteros (como en 168,56 con 2 cifras), usá notación científica.",
        ],
        [
            "a) 0,357898: las cifras significativas son 3, 5, 7, 8, 9, 8. Con 5 cifras cortás en 0,35789|8; el siguiente es 8 > 4, así que el 9 sube y arrastra: **0,35790**. El cero final se escribe porque es significativo.",
            "b) 0,0156: los ceros iniciales no cuentan; la primera cifra significativa es el 1. Cortás en 0,01|56; el siguiente es 5 > 4: **0,02 = 2×10⁻²**.",
            "c) 168,56 con 2 cifras: cortás después del 6 (16|8,56); el siguiente es 8 > 4, así que el 6 sube a 7 y quedan 17 decenas: **1,7×10²**. Escribir 170 no sirve porque, por la regla del curso, ese cero final contaría como tercera cifra significativa.",
            "Los otros dos ítems: 2,356 con 1 cifra → **2**; 1,356×10⁵ con 3 cifras → **1,36×10⁵**.",
            "Error típico: en a) contar los ceros iniciales y quedarse con 0,3579 (4 cifras); en c) truncar y escribir 1,6×10².",
        ],
    ),
    P(
        "u1-5a", "f-cifras-significativas", 1, "Física · Práctica U1, ej. 5 (a, c, d)",
        "Sumas y productos con cifras significativas",
        "Escribí el resultado final de las siguientes operaciones con las cifras significativas correctas:\n"
        "a) 0,2568 + 4,32 + 2,1 =\n"
        "b) 2,56 + 4,267 + 3,112 =\n"
        "c) 0,0231 + 0,87 − 12,145 =\n"
        "d) 120 × 0,21 =",
        [
            N("a) 0,2568 + 4,32 + 2,1 = ? Respondé solo con el número, redondeado según la regla de la suma.", 6.7, "", "6,7"),
            N("c) 0,0231 + 0,87 − 12,145 = ? Respondé solo con el número.", -11.25, "", "−11,25"),
            N("d) 120 × 0,21 = ? Respondé solo con el número, con las cifras significativas correctas.", 25, "", "25"),
        ],
        [
            "Suma y resta: el resultado lleva la misma cantidad de DECIMALES que el sumando que tenga menos decimales.",
            "Multiplicación y división: el resultado lleva la misma cantidad de CIFRAS SIGNIFICATIVAS que el factor que tenga menos.",
            "Hacé la cuenta completa con la calculadora y redondeá solo al final.",
        ],
        [
            "a) `0,2568 + 4,32 + 2,1 = 6,6768`. El sumando con menos decimales es 2,1 (un decimal), así que el resultado se redondea a la décima: **6,7**. (El solucionario acepta también 6,6, que es lo que sale si se trunca en lugar de redondear; con la regla de redondeo del curso es 6,7).",
            "b) (no se pide acá) `2,56 + 4,267 + 3,112 = 9,939` → a la centésima: 9,94.",
            "c) `0,0231 + 0,87 − 12,145 = −11,2519`. El que tiene menos decimales es 0,87 (dos decimales): **−11,25**.",
            "d) `120 × 0,21 = 25,2`. 120 tiene 3 cifras significativas (por la regla del curso, el cero a la derecha cuenta) y 0,21 tiene 2: el resultado lleva 2 → **25**.",
            "Error típico: aplicar la regla de los decimales a la multiplicación (y dejar 25,2) o la de las cifras a la suma.",
        ],
    ),
    P(
        "u1-5b", "f-cifras-significativas", 2, "Física · Práctica U1, ej. 5 (e, g, h)",
        "Operaciones combinadas con cifras significativas",
        "Escribí el resultado final de las siguientes operaciones con las cifras significativas correctas:\n"
        "e) 1023 × 0,3 =\n"
        "f) 245,10 × 0,111 =\n"
        "g) (2,4 × 35,1) + 300,1 =\n"
        "h) (21,1 × 3) + 1,2000 =",
        [
            N("e) 1023 × 0,3 = ? Respondé solo con el número." + SNX, 300, "", "3×10²"),
            N("g) (2,4 × 35,1) + 300,1 = ? Respondé solo con el número.", 384, "", "384"),
            N("h) (21,1 × 3) + 1,2000 = ? Respondé solo con el número." + SNX, 60, "", "6×10¹"),
        ],
        [
            "En las operaciones combinadas resolvé primero el producto aplicando su regla (cifras significativas) y después la suma con la suya (decimales).",
            "Cuando el resultado tiene que quedar con 1 cifra significativa y es mayor que 10, escribilo en notación científica.",
        ],
        [
            "e) `1023 × 0,3 = 306,9`. 0,3 tiene 1 cifra significativa → el resultado lleva 1: **3×10²**.",
            "f) (no se pide acá) `245,10 × 0,111 = 27,2061` → 3 cifras (por 0,111): 27,2.",
            "g) Producto: `2,4 × 35,1 = 84,24` → 2 cifras (por 2,4): 84. Suma: `84 + 300,1 = 384,1`; 84 no tiene decimales, así que el resultado va a las unidades: **384**.",
            "h) Producto: `21,1 × 3 = 63,3` → 1 cifra (por el 3): 6×10¹, es decir, conocido a la decena. Suma: `6×10¹ + 1,2000 = 61,2`, que redondeado a la decena da **6×10¹**.",
            "Fijate en h): aunque 1,2000 tiene 5 cifras significativas, no mejora la precisión del resultado, porque el término menos preciso solo se conoce a la decena.",
        ],
    ),
    P(
        "u1-6a", "f-sistemas-unidades", 1, "Física · Práctica U1, ej. 6 (a, b, c)",
        "Pasajes de unidades con fracciones unitarias (1)",
        "Realizá el pasaje de las siguientes unidades, respetando las cifras significativas, e indicá la magnitud a la "
        "cual están asociadas las unidades:\n"
        "a) 1,35 dg a dag\n"
        "b) 35,95 dam² a cm²\n"
        "c) 0,25 m/s a km/h",
        [
            N("a) 1,35 dg = ? dag. Respondé solo con el número.", 0.0135, "dag", "0,0135 dag (magnitud: masa)"),
            N("b) 35,95 dam² = ? cm². Respondé solo con el número." + SN, 3.595e7, "cm²", "35950000 cm² = 3,595×10⁷ cm² (magnitud: superficie)", 0.001),
            N("c) 0,25 m/s = ? km/h. Respondé solo con el número.", 0.9, "km/h", "0,90 km/h (magnitud: velocidad)"),
        ],
        [
            "Multiplicá por fracciones unitarias (valen 1) armadas para que la unidad vieja se simplifique: por ejemplo `1 g / 10 dg`.",
            "Si la unidad está al cuadrado, la fracción unitaria también va al cuadrado: `(1000 cm / 1 dam)²`.",
            "Para m/s → km/h convertí por separado numerador (m → km) y denominador (s → h).",
        ],
        [
            "a) `1,35 dg · (1 g / 10 dg) · (1 dag / 10 g) = 0,0135 dag`. Magnitud: **masa**. Mantiene 3 cifras significativas (los ceros iniciales no cuentan).",
            "b) 1 dam = 10 m = 1000 cm, así que `1 dam² = (1000 cm)² = 10⁶ cm²`.",
            "`35,95 dam² · (10⁶ cm² / 1 dam²) = 3,595×10⁷ cm²`. Magnitud: **superficie**. Se escribe en notación científica para conservar 4 cifras significativas.",
            "c) `0,25 m/s · (1 km / 1000 m) · (3600 s / 1 h) = 0,90 km/h`. Magnitud: **velocidad**. Con 2 cifras significativas se escribe 0,90.",
            "Error típico en b): usar 10³ en lugar de (10³)² = 10⁶ por olvidarse de elevar la fracción unitaria al cuadrado.",
        ],
    ),
    P(
        "u1-6b", "f-sistemas-unidades", 2, "Física · Práctica U1, ej. 6 (d, e, f)",
        "Pasajes de unidades con fracciones unitarias (2)",
        "Realizá el pasaje de las siguientes unidades, respetando las cifras significativas, e indicá la magnitud a la "
        "cual están asociadas las unidades:\n"
        "d) 1,2×10² m³/h a cm³/s\n"
        "e) 100 kg·m/s² a g·mm/min²\n"
        "f) 4,200 N/m² a kgf/cm² (1 kgf = 9,8 N)",
        [
            N("d) 1,2×10² m³/h = ? cm³/s, con 2 cifras significativas. Respondé solo con el número." + SNX, 33000, "cm³/s",
              "3,3×10⁴ cm³/s (magnitud: caudal volumétrico)", 0.005),
            N("e) 100 kg·m/s² = ? g·mm/min². Respondé solo con el número." + SNX, 3.6e11, "g·mm/min²",
              "3,60×10¹¹ g·mm/min² (magnitud: fuerza)", 0.001),
            N("f) 4,200 N/m² = ? kgf/cm². Respondé solo con el número." + SN, 4.286e-5, "kgf/cm²",
              "0,00004286 kgf/cm² = 4,286×10⁻⁵ kgf/cm² (magnitud: presión)", 0.01),
        ],
        [
            "Escribí una fracción unitaria por cada unidad que tengas que cambiar, incluidas las del denominador; las que están al cuadrado o al cubo, elevalas.",
            "En e) el tiempo está al cuadrado: `(60 s / 1 min)² = 3600 s²/min²`.",
            "En f) necesitás dos pasajes: N → kgf (1 kgf = 9,8 N) y m² → cm² (1 m² = 10⁴ cm²).",
        ],
        [
            "d) `1,2×10² m³/h · (10⁶ cm³ / 1 m³) · (1 h / 3600 s) = 33 333 cm³/s` → con 2 cifras significativas: **3,3×10⁴ cm³/s**. Magnitud: caudal (volumen por unidad de tiempo).",
            "e) `100 kg·m/s² · (1000 g / 1 kg) · (1000 mm / 1 m) · (3600 s² / 1 min²) = 3,60×10¹¹ g·mm/min²`. Magnitud: **fuerza** (kg·m/s² es el newton).",
            "f) `4,200 N/m² · (1 kgf / 9,8 N) · (1 m² / 10⁴ cm²) = 4,286×10⁻⁵ kgf/cm²`, con 4 cifras como el dato. Magnitud: **presión**.",
            "Con g = 9,806 65 m/s² sale 4,283×10⁻⁵ kgf/cm²: la diferencia está en la cuarta cifra y el corrector acepta las dos.",
            "Error típico en f): multiplicar por 10⁴ en vez de dividir. Pensalo así: 1 cm² es mucho más chico que 1 m², así que sobre 1 cm² cae mucho menos fuerza.",
        ],
    ),
    P(
        "u1-7", "f-sistemas-unidades", 2, "Física · Práctica U1, ej. 7",
        "Una cuadra, una pileta y el agua",
        "Resolvé los siguientes problemas, teniendo en cuenta el pasaje de unidades y las cifras significativas "
        "(recordá las reglas para suma y multiplicación).\n"
        "a) Cada casa de un barrio tiene 10,00 m de frente (sin medianera) y 25,0 cm la medianera de cada lado. Si en una "
        "cuadra hay 13 casas, ¿cuántos metros tiene una cuadra?\n"
        "b) Una persona desea llenar una pileta con agua; la pileta tiene 6,0 m de largo, 150 cm de profundidad y 30 dm "
        "de ancho. ¿Cuántos m³ de agua necesitará?\n"
        "c) La densidad del agua es de 1000 kg/m³. Se requieren 2 500 000 cm³. ¿Cuál es la masa de agua que utilizará?",
        [
            N("a) ¿Cuántos metros tiene la cuadra? Respondé solo con el número en m.", 136.5, "m", "136,5 m"),
            N("b) ¿Cuántos m³ de agua necesita? Respondé solo con el número en m³.", 27, "m³", "27 m³"),
            N("c) ¿Qué masa de agua se usa? Respondé solo con el número en kg.", 2500, "kg", "2500 kg"),
        ],
        [
            "Antes de operar pasá todo a la misma unidad (m o m³).",
            "En a) cada casa ocupa su frente más las dos medianeras; el 13 es un número de casas (exacto), no una medición.",
            "En c) `m = densidad · volumen`, con el volumen en m³.",
        ],
        [
            "a) Medianera: `25,0 cm · (1 m / 100 cm) = 0,250 m`. Cada casa ocupa `10,00 m + 2 · 0,250 m = 10,50 m` (suma: dos decimales).",
            "La cuadra: `13 · 10,50 m = 136,5 m`. El 13 es un conteo exacto, así que no limita las cifras: quedan las 4 de 10,50 → **136,5 m**.",
            "b) `150 cm = 1,50 m` y `30 dm = 3,0 m`. Volumen: `6,0 m · 1,50 m · 3,0 m = 27 m³` (2 cifras significativas, por 6,0 y 3,0) → **27 m³**.",
            "c) `2 500 000 cm³ · (1 m³ / 10⁶ cm³) = 2,5 m³`.",
            "`m = 1000 kg/m³ · 2,5 m³ = 2500 kg` → **2500 kg**.",
        ],
    ),
    P(
        "u1-8", "f-cifras-significativas", 2, "Física · Práctica U1, ej. 8 (b, d, e)",
        "Elegir el prefijo adecuado",
        "Indicá un prefijo adecuado y respetá las cifras significativas para las siguientes cantidades medidas: "
        "a) 128 563 m; b) 0,00056 g; c) 12333 s; d) 20000 kg; e) 0,0000080 mm; f) 0,0000000052976 C; g) 98400 A.",
        [
            C("b) 0,00056 g se escribe:", ["0,56 mg", "560 μg", "5,6 mg", "0,56 μg"], "0,56 mg"),
            C("d) 20000 kg se escribe:", ["20,000 Mg", "20 000 Mg", "2,0000 Mg", "20,000 Gg"], "20,000 Mg (= 20 Mg, con 5 cifras significativas)"),
            C("e) 0,0000080 mm se escribe:", ["8,0 nm", "8 nm", "80 nm", "8,0 μm"], "8,0 nm"),
        ],
        [
            "Pasá primero a la unidad base (g, m, s…) y después elegí el prefijo que deje un número cómodo: m = 10⁻³, μ = 10⁻⁶, n = 10⁻⁹, k = 10³, M = 10⁶.",
            "Un cambio de prefijo no puede agregar ni quitar cifras significativas: contá las del dato y conservalas.",
            "Ojo con kg: el prefijo se aplica sobre el gramo, así que 1 Mg = 10⁶ g = 10³ kg.",
        ],
        [
            "b) 0,00056 g tiene 2 cifras significativas (5 y 6). `0,00056 g = 0,56×10⁻³ g = 0,56 mg`. Escribir 560 μg agrega un cero que, por la regla del curso (los ceros a la derecha de una cifra distinta de cero son significativos), contaría como tercera cifra; el solucionario lo acepta solo 'sin cs'.",
            "d) 20000 kg = 2,0000×10⁷ g = 20,000×10⁶ g = **20,000 Mg**. Por la regla del curso los ceros a la derecha del 2 son significativos (5 cifras), y el pasaje los conserva.",
            "Atención con la escritura de d): con coma decimal, 20,000 Mg es **veinte** megagramos (20 Mg = 20 t), no veinte mil. La opción '20 000 Mg' (veinte mil megagramos) es 1000 veces más grande.",
            "e) `0,0000080 mm = 8,0×10⁻⁶ mm = 8,0×10⁻⁹ m = 8,0 nm`. El cero final es significativo (2 cifras), por eso no alcanza con '8 nm'.",
            "Los demás ítems, según el solucionario: a) 128,563 km; c) 12,333 ks; f) 5,2976 nC; g) 98,400 kA.",
        ],
    ),
    P(
        "u1-9", "f-sistemas-unidades", 2, "Física · Práctica U1, ej. 9",
        "Energía de una partícula y masa de la Luna",
        "Resolvé los siguientes problemas, utilizando los conceptos aprendidos sobre fracciones unitarias, cifras "
        "significativas y prefijos. (Datos ficticios del ejercicio original: sirven para practicar conversiones, no son "
        "valores reales; por ejemplo, 2,0 Gm/s supera la velocidad de la luz.)\n"
        "a) Se sabe que la masa de una partícula es de 9 pg. Si en un tubo de aceleración alcanza la velocidad de "
        "2,0 Gm/s, ¿qué energía cinética (`E = ½·m·v²`) alcanza en el tubo, en unidades del SI? Tené en cuenta las "
        "cifras significativas.\n"
        "b) Tomá para la Luna una densidad de 3,34 g/cm³ y un volumen de 13,6 Gm³ (el volumen real de la Luna es mucho "
        "menor, ≈ 2,2×10¹⁹ m³). Calculá la masa que resulta con esos datos, sin tener en cuenta las cifras significativas.",
        [
            N("a) ¿Cuánto vale la energía cinética en J, con las cifras significativas correctas? Respondé solo con el número." + SNX,
              20000, "J", "2×10⁴ J"),
            C("b) ¿Cuál es la masa de la Luna según estos datos?",
              ["4,54×10³⁴ g", "4,54×10¹⁶ g", "4,54×10²⁸ g", "4,54×10⁴⁰ g"], "4,54×10³⁴ g"),
        ],
        [
            "Pasá todo al SI antes de reemplazar: p = 10⁻¹², G = 10⁹, y la masa en kg (1 kg = 10³ g).",
            "El prefijo se eleva junto con la unidad: `1 Gm³ = (10⁹ m)³ = 10²⁷ m³`, y `1 m³ = 10⁶ cm³`.",
        ],
        [
            "a) Masa: `9 pg = 9×10⁻¹² g = 9×10⁻¹⁵ kg`. Velocidad: `2,0 Gm/s = 2,0×10⁹ m/s`.",
            "`E = ½ · 9×10⁻¹⁵ kg · (2,0×10⁹ m/s)² = ½ · 9×10⁻¹⁵ · 4,0×10¹⁸ = 1,8×10⁴ kg·m²/s²`.",
            "El dato 9 pg tiene 1 cifra significativa, así que el resultado lleva 1: **E = 2×10⁴ J** (kg·m²/s² = J).",
            "b) Volumen: `13,6 Gm³ = 13,6 · (10⁹ m)³ = 1,36×10²⁸ m³ = 1,36×10²⁸ · 10⁶ cm³ = 1,36×10³⁴ cm³`.",
            "`m = 3,34 g/cm³ · 1,36×10³⁴ cm³ = 4,54×10³⁴ g`.",
            "Los distractores salen de errores reales: 4,54×10¹⁶ g es tomar 1 Gm³ como 10⁹ m³ (sin elevar el prefijo) y 4,54×10²⁸ g es olvidarse de pasar m³ a cm³.",
        ],
    ),
    # ======================================================================
    # UNIDAD 2 · PRÁCTICA DEL CURSO
    # ======================================================================
    P(
        "u2-1", "f-magnitudes-vectores", 1, "Física · Práctica U2, ej. 1 y 2",
        "Componentes desde dos puntos y módulos",
        "Ejercicio 1: encontrá las componentes del vector AB dados el punto de origen A y el punto extremo B: "
        "a) A(−3; 1) y B(0; 2); b) A(−1; −1) y B(2; −1); c) A(5; −1) y B(5; 2); d) A(−1/2; 0) y B(−1; −1).\n\n"
        "Ejercicio 2: encontrá el módulo de los vectores u = (3,0; −1,0), v = (1,0; −5,0), w = (−2,0; 7,0) y t = (−4,0; −6,0).",
        [
            N("a) En el inciso d) del ejercicio 1, ¿cuánto vale la componente x de AB? Respondé solo con el número.", -0.5, "", "−1/2"),
            N("b) En el inciso d) del ejercicio 1, ¿cuánto vale la componente y de AB? Respondé solo con el número.", -1, "", "−1"),
            N("c) Ejercicio 2: ¿cuánto vale el módulo de w? Respondé solo con el número, con dos decimales.", 7.2801, "", "7,28 (= √53)", 0.01),
        ],
        [
            "Las componentes de AB son 'extremo menos origen': `AB = (xB − xA; yB − yA)`.",
            "El módulo sale por Pitágoras: `|w| = √(wx² + wy²)`.",
        ],
        [
            "Ejercicio 1, extremo menos origen: a) `(0 − (−3); 2 − 1) = (3; 1)`; b) `(2 − (−1); −1 − (−1)) = (3; 0)`; c) `(5 − 5; 2 − (−1)) = (0; 3)`.",
            "d) `AB = (−1 − (−1/2); −1 − 0) = (−1/2; −1)`: componente x **−1/2** y componente y **−1**.",
            "Ejercicio 2: `|u| = √(9 + 1) = √10 ≈ 3,16`; `|v| = √(1 + 25) = √26 ≈ 5,10`.",
            "`|w| = √((−2)² + 7²) = √(4 + 49) = √53 ≈ 7,28`; `|t| = √(16 + 36) = √52 ≈ 7,21`.",
            "Error típico: restar al revés (origen menos extremo), que da el vector opuesto BA.",
        ],
    ),
    P(
        "u2-3", "f-magnitudes-vectores", 1, "Física · Práctica U2, ej. 3",
        "Componente y a partir del módulo",
        "Encontrá las componentes 'y' de los vectores, conocidos los siguientes datos:\n"
        "|u| = 5,0 y u = (3,0; y) (vector del IV cuadrante)\n"
        "|v| = 10 y v = (−1,0; y) (vector del II cuadrante)",
        [
            N("a) ¿Cuánto vale la componente y de u? Respondé solo con el número.", -4, "", "−4,0"),
            N("b) ¿Cuánto vale la componente y de v? Respondé solo con el número.", 9.95, "", "9,9 (√99 ≈ 9,95)", 0.01),
        ],
        [
            "Planteá Pitágoras con la incógnita: `|u|² = ux² + uy²` y despejá `uy²`.",
            "La raíz da dos signos posibles: el cuadrante te dice cuál corresponde.",
        ],
        [
            "u: `5,0² = 3,0² + uy²` → `uy² = 25 − 9 = 16` → `uy = ±4,0`.",
            "En el IV cuadrante la componente y es negativa: **uy = −4,0**.",
            "v: `10² = (−1,0)² + vy²` → `vy² = 100 − 1 = 99` → `vy = ±√99 ≈ ±9,95`.",
            "En el II cuadrante la componente y es positiva: **vy ≈ 9,9** (con 2 cifras significativas, como el dato 10).",
            "En el solucionario la segunda respuesta aparece rotulada 'uy', pero corresponde al vector v.",
        ],
    ),
    P(
        "u2-4", "f-vectores-operaciones", 2, "Física · Práctica U2, ej. 4",
        "Componentes de cuatro vectores del gráfico",
        "Encontrá las componentes de los vectores del gráfico, conocidos los siguientes datos: α = 40°, φ = 75°, "
        "θ = 35°; |A| = 10 m, |B| = 20 m, |C| = 5,0 m, |D| = 22 m.\n\n"
        "Descripción del gráfico (todos los vectores salen del origen):\n"
        "|Vector|Cuadrante|Ángulo dado|\n"
        "|---|---|---|\n"
        "|A|I|α = 40° con el semieje x positivo|\n"
        "|B|sobre el semieje x negativo|—|\n"
        "|C|III|φ = 75° con el semieje x negativo (por debajo)|\n"
        "|D|IV|θ = 35° con el semieje x positivo (por debajo)|",
        [
            N("a) ¿Cuánto vale Cx? Respondé solo con el número en m, con su signo.", -1.294, "m", "−1,3 m", 0.01),
            N("b) ¿Cuánto vale Cy? Respondé solo con el número en m, con su signo.", -4.830, "m", "−4,8 m", 0.01),
            N("c) ¿Cuánto vale Dy? Respondé solo con el número en m, con su signo y un decimal.", -12.62, "m", "−12,6 m (≈ −13 m)", 0.01),
        ],
        [
            "El cateto adyacente al ángulo dado va con el coseno y el opuesto con el seno; después ponés el signo según el cuadrante.",
            "Para C el ángulo se mide desde el semieje x negativo: la componente x es `|C|·cos φ` y la y es `|C|·sen φ`, ambas negativas en el III cuadrante.",
        ],
        [
            "A (I cuadrante): `Ax = 10·cos 40° = 7,7 m`, `Ay = 10·sen 40° = 6,4 m`.",
            "B (semieje x negativo): `Bx = −20 m`, `By = 0 m`.",
            "C (III cuadrante, 75° desde x negativo): `Cx = −5,0·cos 75° = −1,29 m ≈ −1,3 m`; `Cy = −5,0·sen 75° = −4,83 m ≈ −4,8 m`.",
            "D (IV cuadrante, 35° debajo de x positivo): `Dx = 22·cos 35° = 18,0 m`; `Dy = −22·sen 35° = −12,6 m` (el solucionario lo da con 2 cifras: −13 m).",
            "Verificación de C: `√(1,29² + 4,83²) ≈ 5,0 m`. Error típico: usar el seno para la componente x de C, como si φ estuviera medido desde el eje y; eso intercambia las componentes (Cx = −4,83 m y Cy = −1,29 m).",
        ],
    ),
    P(
        "u2-5", "f-magnitudes-vectores", 2, "Física · Práctica U2, ej. 5",
        "Módulo y ángulo respecto del eje más cercano",
        "Graficá y encontrá módulo y ángulo de los siguientes vectores. El ángulo calculado tiene que estar referido a "
        "alguno de los dos ejes que limitan el cuadrante del vector: a) u = 2,0i + 3,0j; b) v = (1,0; −2,0); "
        "c) t = −3,0i − 4,0j; d) s = (−2,0; 3,5).",
        [
            N("a) ¿Cuánto vale |s|? Respondé solo con el número, con dos cifras significativas.", 4.031, "", "4,0 (√16,25 ≈ 4,03)", 0.01),
            N("b) ¿Qué ángulo forma v con el semieje x positivo, medido en sentido horario? Respondé solo con el número en grados decimales, con dos decimales.",
              63.43, "°", "63,43° (= 63°26´)", 0.01),
            N("c) ¿Qué ángulo forma t con el semieje y negativo? Respondé solo con el número en grados decimales, con dos decimales.",
              36.87, "°", "36,87° (= 36°52´)", 0.01),
        ],
        [
            "Módulo por Pitágoras. Para el ángulo, armá el triángulo rectángulo con las dos componentes en valor absoluto.",
            "Si el ángulo se mide desde el eje x, `tg α = |componente y| / |componente x|`; si se mide desde el eje y, la tangente se invierte.",
            "Los ángulos de t medidos desde x negativo y desde y negativo suman 90°.",
        ],
        [
            "a) u = (2,0; 3,0): `|u| = √13 ≈ 3,6`, `α = arctg(3/2) = 56,31° = 56°19´` respecto de x positivo.",
            "b) v = (1,0; −2,0) en el IV cuadrante: `|v| = √5 ≈ 2,2`; `α = arctg(2/1) = 63,43° = 63°26´` por debajo de x positivo (sentido horario).",
            "c) t = (−3,0; −4,0) en el III cuadrante: `|t| = 5,0`. Desde x negativo: `arctg(4/3) = 53,13° = 53°8´`. Desde y negativo: `arctg(3/4) = 36,87° = 36°52´`.",
            "El solucionario dice '36,3° respecto a y−', pero eso es un error: el complemento de 53°8´ es 90° − 53°8´ = **36°52´ = 36,87°**.",
            "d) s = (−2,0; 3,5) en el II cuadrante: `|s| = √(4 + 12,25) = √16,25 ≈ 4,0`; respecto de y positivo, `arctg(2,0/3,5) = 29,74° = 29°45´`.",
        ],
    ),
    P(
        "u2-5-1", "f-vectores-operaciones", 2, "Física · Práctica U2, ej. 5.1",
        "Ángulos medidos desde el eje x positivo",
        "Indicá el ángulo respecto del eje positivo de las x (medido en sentido antihorario) de los vectores "
        "u = 2,0i + 3,0j, v = (1,0; −2,0), t = −3,0i − 4,0j y s = (−2,0; 3,5).",
        [
            N("a) Ángulo de u. Respondé solo con el número en grados decimales, con dos decimales.", 56.31, "°", "56,31° (= 56°19´)", 0.01),
            N("b) Ángulo de v. Respondé solo con el número en grados decimales, con dos decimales.", 296.57, "°", "296,57° (= 296°34´)", 0.01),
            N("c) Ángulo de s. Respondé solo con el número en grados decimales, con dos decimales.", 119.74, "°", "119,74° (= 119°45´)", 0.01),
        ],
        [
            "Calculá primero el ángulo agudo con el eje x (`arctg(|y|/|x|)`) y después ubicá el cuadrante con los signos de las componentes.",
            "II cuadrante: 180° − agudo. III cuadrante: 180° + agudo. IV cuadrante: 360° − agudo.",
        ],
        [
            "u = (2,0; 3,0), I cuadrante: `arctg(3/2) = 56,31°` → **56,31° = 56°19´**. El solucionario pone 35°46´ en este inciso, pero es un error: el valor correcto es el que da el propio solucionario en el ejercicio 5 (56°18´; el solucionario trunca los minutos y da uno menos, porque 0,31° · 60 ≈ 18,6´).",
            "v = (1,0; −2,0), IV cuadrante: agudo `arctg(2/1) = 63,43°` → `360° − 63,43° = 296,57° = 296°34´` (el solucionario da 296°33´, por redondeo de minutos).",
            "t = (−3,0; −4,0), III cuadrante: agudo `arctg(4/3) = 53,13°` → `180° + 53,13° = 233,13° = 233°8´`.",
            "s = (−2,0; 3,5), II cuadrante: agudo `arctg(3,5/2,0) = 60,26°` → `180° − 60,26° = 119,74° = 119°45´`.",
            "Pasaje a grados y minutos: la parte decimal por 60. Por ejemplo `0,31° · 60 ≈ 18,6´ ≈ 19´` (se redondea al minuto más cercano).",
        ],
    ),
    P(
        "u2-6a", "f-vectores-operaciones", 2, "Física · Práctica U2, ej. 6 (gráfico 1)",
        "Suma de tres vectores (gráfico 1)",
        "Realizá la suma de vectores en forma analítica y encontrá módulo y ángulo de la resultante. Datos: A = 100 u, "
        "B = 75 u, C = 165 u, α = 60°, θ = 70°.\n\n"
        "Descripción del gráfico:\n"
        "|Vector|Cuadrante|Ángulo dado|\n"
        "|---|---|---|\n"
        "|A|I|α = 60° con el semieje x positivo|\n"
        "|B|sobre el semieje x positivo|—|\n"
        "|C|III|θ = 70° con el semieje x negativo (por debajo)|",
        [
            N("a) ¿Cuánto vale la componente y de la resultante? Respondé solo con el número, con su signo.", -68.45, "u", "−68 u", 0.01),
            N("b) ¿Cuánto vale el módulo de la resultante? Respondé solo con el número.", 96.88, "u", "97 u", 0.01),
            N("c) ¿Qué ángulo forma la resultante con el eje x positivo (sentido antihorario)? Respondé solo con el número en grados decimales.",
              315.05, "°", "315° (≈ 315°03´)", 0.01),
        ],
        [
            "Descomponé cada vector en x e y con su signo, sumá todas las x por un lado y todas las y por otro.",
            "Con Rx y Ry sacás el módulo (Pitágoras) y el ángulo agudo con el eje x; los signos te dicen el cuadrante.",
        ],
        [
            "A: `(100·cos 60°; 100·sen 60°) = (50,0; 86,6)`. B: `(75; 0)`. C: `(−165·cos 70°; −165·sen 70°) = (−56,4; −155,0)`.",
            "`Rx = 50,0 + 75 − 56,4 = 68,6 ≈ 69` y `Ry = 86,6 + 0 − 155,0 = −68,4 ≈ −68`: IV cuadrante.",
            "`|R| = √(68,6² + 68,4²) ≈ 96,9 ≈ 97 u`.",
            "Agudo: `arctg(68,4/68,6) ≈ 44,95°`; en el IV cuadrante: `360° − 44,95° ≈ 315,05° = 315°03´`.",
            "El solucionario da 315°25´ porque calcula el ángulo con Rx y Ry ya redondeados (69 y −68). La diferencia es de décimas de grado y el corrector acepta ambos valores.",
        ],
    ),
    P(
        "u2-6b", "f-vectores-operaciones", 2, "Física · Práctica U2, ej. 6 (gráfico 2)",
        "Suma de tres vectores (gráfico 2)",
        "Realizá la suma de vectores en forma analítica y encontrá módulo y ángulo de la resultante. Datos: A = 22 m, "
        "B = 35 m, C = 15 m, β = 80°, θ = 70°.\n\n"
        "Descripción del gráfico:\n"
        "|Vector|Cuadrante|Ángulo dado|\n"
        "|---|---|---|\n"
        "|A|sobre el semieje x positivo|—|\n"
        "|B|I|β = 80° con el semieje x positivo|\n"
        "|C|III|θ = 70° con el semieje y negativo|",
        [
            N("a) ¿Cuánto vale la componente x de la resultante? Respondé solo con el número en m.", 13.98, "m", "13,98 m (el solucionario da 13,9 m)", 0.01),
            N("b) ¿Cuánto vale el módulo de la resultante? Respondé solo con el número en m.", 32.50, "m", "32,5 m", 0.01),
            N("c) ¿Qué ángulo forma la resultante con el eje x positivo? Respondé solo con el número en grados decimales.", 64.52, "°", "64,5°", 0.01),
        ],
        [
            "C está medido desde el eje y: su componente x va con el seno de θ y su componente y con el coseno, las dos negativas.",
            "Sumá componente a componente y después aplicá Pitágoras y la tangente.",
        ],
        [
            "A: `(22; 0)`. B: `(35·cos 80°; 35·sen 80°) = (6,08; 34,47)`.",
            "C (III cuadrante, 70° desde y negativo): `(−15·sen 70°; −15·cos 70°) = (−14,10; −5,13)`.",
            "`Rx = 22 + 6,08 − 14,10 = 13,98 m` y `Ry = 0 + 34,47 − 5,13 = 29,34 m`: I cuadrante.",
            "`|R| = √(13,98² + 29,34²) ≈ 32,5 m`; `β = arctg(29,34/13,98) ≈ 64,5°`.",
            "El solucionario da Rx = 13,9; |R| = 32,4 y 64,4°: diferencias de redondeo en la última cifra, que el corrector acepta.",
        ],
    ),
    P(
        "u2-6c", "f-vectores-operaciones", 3, "Física · Práctica U2, ej. 6 (gráfico 3)",
        "Suma de cuatro vectores (gráfico 3)",
        "Realizá la suma de vectores en forma analítica y encontrá módulo y ángulo de la resultante. Datos: A = 50 u, "
        "B = 75 u, C = 90 u, D = 80 u, α = 40°, β = 60°, θ = 50°, φ = 48°.\n\n"
        "Descripción del gráfico:\n"
        "|Vector|Cuadrante|Ángulo dado|\n"
        "|---|---|---|\n"
        "|A|II|α = 40° con el semieje y positivo|\n"
        "|D|I|β = 60° con el semieje x positivo|\n"
        "|C|III|θ = 50° con el semieje x negativo|\n"
        "|B|IV|φ = 48° con el semieje y negativo|",
        [
            N("a) ¿Cuánto vale la componente x de la resultante? Respondé solo con el número.", 5.75, "u", "5,7 u", 0.01),
            N("b) ¿Cuánto vale el módulo de la resultante? Respondé solo con el número.", 12.90, "u", "12,9 u (el solucionario da 12,8 u)", 0.01),
            N("c) ¿Qué ángulo forma la resultante con el eje x positivo (sentido antihorario)? Respondé solo con el número en grados decimales.",
              296.46, "°", "296,5° (≈ 296°28´)", 0.01),
        ],
        [
            "Para los vectores medidos desde el eje y (A y B), la componente x va con el seno y la y con el coseno.",
            "Fijate los signos de cada componente según el cuadrante antes de sumar.",
            "Con Rx > 0 y Ry < 0 la resultante está en el IV cuadrante: el ángulo es 360° menos el agudo.",
        ],
        [
            "A (II, 40° desde y+): `(−50·sen 40°; 50·cos 40°) = (−32,14; 38,30)`. D (I, 60° desde x+): `(80·cos 60°; 80·sen 60°) = (40,00; 69,28)`.",
            "C (III, 50° desde x−): `(−90·cos 50°; −90·sen 50°) = (−57,85; −68,94)`. B (IV, 48° desde y−): `(75·sen 48°; −75·cos 48°) = (55,74; −50,18)`.",
            "`Rx = −32,14 + 40,00 − 57,85 + 55,74 = 5,75` y `Ry = 38,30 + 69,28 − 68,94 − 50,18 = −11,54`.",
            "`|R| = √(5,75² + 11,54²) ≈ 12,9 u`. Agudo: `arctg(11,54/5,75) ≈ 63,5°` → `360° − 63,5° = 296,5°`.",
            "El solucionario da Rx = 5,7; Ry = −11,5; |R| = 12,8 y 296°21´: trabaja con valores redondeados; la diferencia es menor al 1 % y el corrector la acepta.",
        ],
    ),
    P(
        "u2-7", "f-vectores-operaciones", 3, "Física · Práctica U2, ej. 7",
        "El vector que falta en la suma",
        "Dada la resultante R de la suma vectorial entre los vectores A, B y C, encontrá el módulo y la dirección del vector B.\n"
        "|A| = 40, α = 35° respecto del eje x positivo en sentido antihorario.\n"
        "|C| = 20, β = 20° respecto del eje x negativo en sentido antihorario.\n"
        "|R| = 80, γ = 30° respecto del eje x positivo en sentido horario.",
        [
            N("a) ¿Cuánto vale Bx? Respondé solo con el número.", 55.31, "", "55,3", 0.01),
            N("b) ¿Cuánto vale |B|? Respondé solo con el número.", 78.78, "", "78,8", 0.01),
            N("c) ¿Qué ángulo forma B con el eje x positivo, en sentido antihorario? Respondé solo con el número en grados decimales.",
              314.59, "°", "314,59° (= 314°36´)", 0.01),
        ],
        [
            "Como `A + B + C = R`, despejá `B = R − A − C` y hacelo componente a componente.",
            "Pasá cada ángulo a 'desde x positivo, antihorario': C está a 180° + 20° = 200° y R a −30° (o 330°).",
        ],
        [
            "A: `(40·cos 35°; 40·sen 35°) = (32,77; 22,94)`.",
            "C a 200°: `(20·cos 200°; 20·sen 200°) = (−18,79; −6,84)`.",
            "R a −30°: `(80·cos 30°; −80·sen 30°) = (69,28; −40,00)`.",
            "`Bx = 69,28 − 32,77 − (−18,79) = 55,3` y `By = −40,00 − 22,94 − (−6,84) = −56,1`.",
            "`|B| = √(55,3² + 56,1²) ≈ 78,8`. IV cuadrante: agudo `arctg(56,1/55,3) ≈ 45,41°` → `360° − 45,41° = 314,59°`. Con más decimales es 314,592°, y `0,592 · 60 ≈ 35,5´`, que redondeado da **314°36´**.",
            "Error típico: restar los módulos (80 − 40 − 20) en lugar de restar vectores.",
        ],
    ),
    P(
        "u2-8", "f-vectores-operaciones", 1, "Física · Práctica U2, ej. 8 y 10",
        "Operaciones combinadas con u, v y s",
        "Dados tres vectores u = (−2; 3), v = (−1; −1) y s = (0; 4):\n"
        "Ejercicio 8: realizá en forma analítica a) u + v; b) v − s; c) u − s + v; d) v − s − u.\n"
        "Ejercicio 10: realizá en forma analítica a) 3·u; b) −2·v; c) 2·u − s; d) −2·v + u + 3·s.",
        [
            N("a) Ejercicio 8 d): ¿cuánto vale la componente x de v − s − u? Respondé solo con el número.", 1, "", "1"),
            N("b) Ejercicio 8 d): ¿cuánto vale la componente y de v − s − u? Respondé solo con el número.", -8, "", "−8"),
            N("c) Ejercicio 10 d): ¿cuánto vale la componente y de −2·v + u + 3·s? Respondé solo con el número.", 17, "", "17"),
        ],
        [
            "Sumar o restar vectores es sumar o restar componente a componente; un escalar multiplica a las dos componentes.",
            "Cuidado con los signos al restar un vector con componentes negativas: `−(−2) = +2`.",
        ],
        [
            "Ejercicio 8: a) `u + v = (−3; 2)`; b) `v − s = (−1; −5)`; c) `u − s + v = (−2 − 0 − 1; 3 − 4 − 1) = (−3; −2)`.",
            "d) `v − s − u = (−1 − 0 − (−2); −1 − 4 − 3) = (1; −8)`.",
            "Ejercicio 10: a) `3·u = (−6; 9)`; b) `−2·v = (2; 2)`; c) `2·u − s = (−4; 6 − 4) = (−4; 2)`.",
            "d) `−2·v + u + 3·s = (2; 2) + (−2; 3) + (0; 12) = (0; 17)`.",
            "Error típico en 8 d): restar u sin cambiarle el signo a su componente x negativa (−2), lo que da −3 en lugar de 1.",
        ],
    ),
    P(
        "u2-9", "f-magnitudes-vectores", 1, "Física · Práctica U2, ej. 9",
        "Multiplicar un vector por un escalar λ",
        "Indicá qué intervalos de λ (un escalar real) hacen que el vector u disminuya su módulo sin cambiar el sentido. "
        "¿Qué intervalo de valores de λ hará que u cambie el sentido? ¿Hay algún valor de λ que genere el cambio de "
        "dirección de u? (En el gráfico del material, u sale del origen hacia el II cuadrante y λ·u es una flecha más "
        "larga sobre la misma recta.)",
        [
            C("a) ¿Para qué valores de λ el vector λ·u tiene menor módulo que u y el mismo sentido?",
              ["0 < λ < 1", "λ > 1", "λ < 0", "−1 < λ < 0"], "0 < λ < 1"),
            C("b) ¿Para qué valores de λ el vector λ·u tiene sentido opuesto al de u?",
              ["λ < 0", "0 < λ < 1", "Solo λ < −1", "λ > 1"], "λ < 0"),
            C("c) ¿Hay algún valor de λ que cambie la dirección de u?",
              ["No: λ·u siempre queda sobre la misma recta que u", "Sí, cualquier λ negativo", "Sí, cuando |λ| > 1", "Sí, cuando 0 < λ < 1"],
              "No: ningún valor de λ cambia la dirección"),
        ],
        [
            "`|λ·u| = |λ|·|u|`: el módulo crece si |λ| > 1 y se achica si |λ| < 1.",
            "El signo de λ decide el sentido; la dirección (la recta que contiene al vector) no la cambia ningún escalar.",
        ],
        [
            "`|λ·u| = |λ|·|u|`, así que el módulo se achica cuando `|λ| < 1`.",
            "Si λ > 0 el sentido se conserva; si λ < 0 se invierte.",
            "a) Achica el módulo y conserva el sentido: **0 < λ < 1**. (Con λ > 1 conserva el sentido y aumenta el módulo.)",
            "b) Cambia el sentido: **λ < 0**. Además, si |λ| > 1 el módulo aumenta y si 0 < |λ| < 1 disminuye.",
            "c) **Ningún** valor de λ cambia la dirección: λ·u siempre es paralelo a u. Sentido y dirección no son lo mismo: un vector y su opuesto tienen la misma dirección y sentidos contrarios. (λ = 0 da el vector nulo.)",
        ],
    ),
    P(
        "u2-11", "f-vectores-operaciones", 2, "Física · Práctica U2, ej. 11",
        "Despejar un vector de una ecuación vectorial",
        "Dados tres vectores u = (1; 3), v = (x; y) y s = (−1; 2), encontrá el valor de las componentes de v, sabiendo que:\n"
        "a) 2u − v + 3s = (1; 2)\n"
        "b) −½u + v + 2u − s = (5; −1)",
        [
            N("a) En a), ¿cuánto vale la componente x de v? Respondé solo con el número.", -2, "", "−2"),
            N("b) En a), ¿cuánto vale la componente y de v? Respondé solo con el número.", 10, "", "10"),
            N("c) En b), ¿cuánto vale la componente y de v? Respondé solo con el número.", -3.5, "", "−7/2"),
        ],
        [
            "Despejá v como en una ecuación común, pasando los demás vectores al otro miembro, y recién después reemplazá componentes.",
            "En b) agrupá primero los términos en u: `−½u + 2u = (3/2)u`.",
        ],
        [
            "a) `2u − v + 3s = (1; 2)` → `v = 2u + 3s − (1; 2)`.",
            "`v = (2; 6) + (−3; 6) − (1; 2) = (2 − 3 − 1; 6 + 6 − 2) = (−2; 10)`.",
            "b) `(3/2)u + v − s = (5; −1)` → `v = (5; −1) − (3/2)u + s`.",
            "`v = (5; −1) − (3/2; 9/2) + (−1; 2) = (5 − 3/2 − 1; −1 − 9/2 + 2) = (5/2; −7/2)`.",
            "Respuestas: a) v = (−2; 10); b) v = (5/2; −7/2).",
        ],
    ),
    P(
        "u2-12", "f-vectores-operaciones", 2, "Física · Práctica U2, ej. 12",
        "Hallar s a partir del gráfico de u y v",
        "Dados los vectores u y v del gráfico, encontrá el vector s.\n"
        "a) −u + v − 2s = (2; −2)\n"
        "b) 2u − 3v + s = (0; −1)\n\n"
        "Descripción del gráfico (cuadrícula de 1 unidad): u va desde el punto (2; 2) hasta el punto (4; 4); v va desde "
        "el punto (−1; −1) hasta el punto (−3; 2).",
        [
            N("a) En a), ¿cuánto vale la componente x de s? Respondé solo con el número.", -3, "", "−3"),
            N("b) En a), ¿cuánto vale la componente y de s? Respondé solo con el número.", 1.5, "", "3/2"),
            N("c) En b), ¿cuánto vale la componente x de s? Respondé solo con el número.", -10, "", "−10"),
        ],
        [
            "Primero sacá las componentes de u y v del gráfico: extremo menos origen.",
            "Después despejá s de cada ecuación y operá componente a componente.",
        ],
        [
            "Del gráfico: `u = (4 − 2; 4 − 2) = (2; 2)` y `v = (−3 − (−1); 2 − (−1)) = (−2; 3)`.",
            "a) `−2s = (2; −2) + u − v = (2 + 2 + 2; −2 + 2 − 3) = (6; −3)` → `s = (−3; 3/2)`.",
            "b) `s = (0; −1) − 2u + 3v = (0 − 4 − 6; −1 − 4 + 9) = (−10; 4)`.",
            "Respuestas: a) s = (−3; 3/2); b) s = (−10; 4).",
            "Error típico: leer las coordenadas del extremo como si fueran las componentes (u = (4; 4)), olvidando que el vector no sale del origen.",
        ],
    ),
    # ======================================================================
    # UNIDAD 3 · PRÁCTICA DEL CURSO
    # ======================================================================
    P(
        "u3-1", "f-cinematica", 1, "Física · Práctica U3, ej. 1",
        "Desplazamiento y distancia en una gráfica x-t",
        "Dada la gráfica x-t, calculá el desplazamiento total del cuerpo y la distancia total recorrida. Calculá el "
        "desplazamiento por tramo (0; 3) s, (3; 5) s, (5; 7) s, (7; 10) s, (10; 12) s y (12; 16) s. Interpretá los resultados.\n\n"
        "La gráfica está formada por segmentos rectos que unen estos puntos:\n"
        "|t (s)|0|3|5|7|10|12|16|\n"
        "|---|---|---|---|---|---|---|---|\n"
        "|x (m)|30|−10|−10|−30|25|40|10|",
        [
            N("a) ¿Cuánto vale el desplazamiento total entre 0 y 16 s? Respondé solo con el número en m, con su signo.", -20, "m", "−20 m"),
            N("b) ¿Cuánto vale la distancia total recorrida? Respondé solo con el número en m.", 160, "m", "160 m"),
            N("c) ¿Cuánto vale el desplazamiento en el tramo (7; 10) s? Respondé solo con el número en m, con su signo.", 55, "m", "55 m"),
        ],
        [
            "El desplazamiento de un tramo es `x_final − x_inicial`; el total solo depende de la primera y la última posición.",
            "La distancia recorrida suma los desplazamientos de cada tramo en valor absoluto (cada tramo recto va siempre en el mismo sentido).",
        ],
        [
            "Desplazamientos por tramo: (0; 3) s: `−10 − 30 = −40 m`; (3; 5) s: `0 m` (no se mueve); (5; 7) s: `−20 m`.",
            "(7; 10) s: `25 − (−30) = 55 m`; (10; 12) s: `15 m`; (12; 16) s: `10 − 40 = −30 m`.",
            "Desplazamiento total: `Δx = 10 − 30 = −20 m`. El cuerpo termina 20 m a la izquierda de donde partió (también sale sumando los tramos con signo).",
            "Distancia total: `40 + 0 + 20 + 55 + 15 + 30 = 160 m`.",
            "Interpretación: la distancia es mucho mayor que el módulo del desplazamiento porque el cuerpo va y vuelve. Error típico: sumar los tramos con signo y dar −20 m como distancia.",
        ],
    ),
    P(
        "u3-2a", "f-cinematica", 1, "Física · Práctica U3, ej. 2.1",
        "Distancia y desplazamiento con la gráfica en km",
        "Un móvil se mueve en trayectoria recta, como muestra la gráfica posición-tiempo (x en km, t en s), formada por "
        "segmentos rectos que unen estos puntos:\n"
        "|t (s)|0|2|3|4|5|6|7|\n"
        "|---|---|---|---|---|---|---|---|\n"
        "|x (km)|20|60|60|40|40|−40|−40|\n\n"
        "2.1) Encontrá la distancia recorrida y el desplazamiento entre 0 y 5,0 s y entre 0 y 7,0 s.",
        [
            N("a) Distancia recorrida entre 0 y 5,0 s. Respondé solo con el número en km.", 60, "km", "60 km"),
            N("b) Desplazamiento entre 0 y 5,0 s. Respondé solo con el número en km, con su signo.", 20, "km", "20 km"),
            N("c) Desplazamiento entre 0 y 7,0 s. Respondé solo con el número en km, con su signo.", -60, "km", "−60 km"),
        ],
        [
            "Desplazamiento: posición final menos posición inicial. Distancia: suma de lo recorrido en cada tramo, sin signo.",
            "Los tramos horizontales (2; 3) s, (4; 5) s y (6; 7) s no suman distancia: el móvil está quieto.",
        ],
        [
            "Entre 0 y 5,0 s: recorre 40 km (de 20 a 60), queda quieto, recorre 20 km (de 60 a 40) y vuelve a quedar quieto. Distancia: `40 + 20 = 60 km`.",
            "Desplazamiento (0; 5,0) s: `40 − 20 = 20 km`.",
            "Entre 0 y 7,0 s se agrega el tramo (5; 6) s, de 40 a −40 km: 80 km más. Distancia: `60 + 80 = 140 km`; desplazamiento: `−40 − 20 = −60 km`.",
            "Diferencia con el solucionario: la consigna pide 0 a 5,0 s, pero el solucionario resuelve 0 a 5,5 s (x(5,5) = 0 km), y por eso da d = 100 km y Δx = −20 km. Acá se respeta la consigna.",
            "Los resultados entre 0 y 7,0 s (140 km y −60 km) coinciden con el solucionario.",
        ],
    ),
    P(
        "u3-2b", "f-cinematica", 2, "Física · Práctica U3, ej. 2.2 y 2.3",
        "Velocidad media y rapidez media",
        "Un móvil se mueve en trayectoria recta, como muestra la gráfica posición-tiempo (x en km, t en s), formada por "
        "segmentos rectos que unen estos puntos:\n"
        "|t (s)|0|2|3|4|5|6|7|\n"
        "|---|---|---|---|---|---|---|---|\n"
        "|x (km)|20|60|60|40|40|−40|−40|\n\n"
        "2.2) Encontrá la velocidad media y la rapidez media entre 0 y 5,0 s y entre 0 y 7,0 s.\n"
        "2.3) Encontrá la velocidad media entre 5,0 y 5,5 s, entre 5,5 y 6,0 s y entre 5,0 y 6,0 s.",
        [
            N("a) Velocidad media entre 0 y 7,0 s. Respondé solo con el número en km/s, con su signo y dos cifras significativas.", -8.571, "km/s", "−8,6 km/s", 0.01),
            N("b) Rapidez media entre 0 y 7,0 s. Respondé solo con el número en km/s.", 20, "km/s", "20 km/s"),
            N("c) Velocidad media entre 5,0 y 6,0 s. Respondé solo con el número en km/s, con su signo.", -80, "km/s", "−80 km/s"),
        ],
        [
            "Velocidad media = desplazamiento / tiempo (con signo). Rapidez media = distancia recorrida / tiempo (siempre positiva).",
            "Entre 5 y 6 s la gráfica es un solo segmento recto: la velocidad es constante en todo ese intervalo.",
        ],
        [
            "De la gráfica: entre 0 y 5,0 s, Δx = 20 km y d = 60 km; entre 0 y 7,0 s, Δx = −60 km y d = 140 km.",
            "(0; 5,0) s: `vm = 20/5,0 = 4,0 km/s` y `rm = 60/5,0 = 12 km/s`.",
            "(0; 7,0) s: `vm = −60/7,0 ≈ −8,6 km/s` y `rm = 140/7,0 = 20 km/s`.",
            "2.3: x(5,0) = 40 km, x(5,5) = 0 km, x(6,0) = −40 km. `v(5; 5,5) = (0 − 40)/0,5 = −80 km/s`; `v(5,5; 6) = (−40 − 0)/0,5 = −80 km/s`; `v(5; 6) = −80/1,0 = −80 km/s`. Iguales, porque el tramo es recto (MRU).",
            "El solucionario calcula el primer intervalo como 0 a 5,5 s (vm = −3,6 km/s y rm = 18,2 km/s); con la consigna (0 a 5,0 s) salen 4,0 km/s y 12 km/s.",
        ],
    ),
    P(
        "u3-3", "f-mru-encuentro", 2, "Física · Práctica U3, ej. 3",
        "Ida y vuelta con la misma rapidez",
        "Un cuerpo se mueve con velocidad constante en una trayectoria rectilínea, partiendo del origen en t = 0. A los "
        "10,0 s se encuentra a 10,0 m del origen, a la izquierda. ¿Dónde se encontrará 30,0 s después de que partió, si "
        "empieza a moverse hacia la derecha desde los 10,0 s, manteniendo la misma rapidez del primer tramo? Analizá la "
        "distancia, el desplazamiento y la velocidad del primer tramo y luego la posición a los 30,0 s (tomá la derecha "
        "como sentido positivo).",
        [
            N("a) ¿Cuál es la velocidad en el primer tramo? Respondé solo con el número en m/s, con su signo.", -1, "m/s", "−1,00 m/s"),
            N("b) ¿Cuál es la posición a los 30,0 s? Respondé solo con el número en m, con su signo.", 10, "m", "10,0 m"),
            N("c) ¿Qué distancia recorrió en total entre 0 y 30,0 s? Respondé solo con el número en m.", 30, "m", "30,0 m"),
        ],
        [
            "Primer tramo: Δx = −10,0 m en 10,0 s. Con eso sacás la velocidad (con signo) y la rapidez.",
            "Segundo tramo: arranca en x = −10,0 m en t = 10,0 s con velocidad +rapidez y dura 20,0 s.",
        ],
        [
            "Primer tramo (0; 10,0) s: `Δx = −10,0 − 0 = −10,0 m`, distancia 10,0 m, `v₁ = −10,0 m / 10,0 s = −1,00 m/s`.",
            "Segundo tramo: misma rapidez, hacia la derecha: `v₂ = +1,00 m/s`, desde t = 10,0 s hasta t = 30,0 s (20,0 s).",
            "Ecuación horaria del segundo tramo: `x(t) = −10,0 + 1,00·(t − 10,0)`.",
            "`x(30,0) = −10,0 + 1,00·20,0 = 10,0 m`: termina 10,0 m a la derecha del origen.",
            "Distancia total: `10,0 + 20,0 = 30,0 m`; desplazamiento total: `10,0 − 0 = 10,0 m`. La gráfica x-t son dos rectas: una que baja hasta (10,0 s; −10,0 m) y otra que sube hasta (30,0 s; 10,0 m).",
        ],
    ),
    P(
        "u3-4", "f-mru-encuentro", 1, "Física · Práctica U3, ej. 4",
        "Un viaje con velocidad negativa",
        "Un auto viaja a una velocidad de −120 km/h de forma rectilínea durante 2,50 h. Calculá el desplazamiento del "
        "auto e interpretá el resultado obtenido.",
        [
            N("a) ¿Cuánto vale el desplazamiento? Respondé solo con el número en km, con su signo.", -300, "km", "−300 km"),
            N("b) ¿Qué distancia recorrió? Respondé solo con el número en km.", 300, "km", "300 km"),
        ],
        [
            "En MRU, `Δx = v·Δt`; el signo de la velocidad pasa al desplazamiento.",
        ],
        [
            "`Δx = v·Δt = −120 km/h · 2,50 h = −300 km`.",
            "El signo negativo indica que el auto se desplazó en el sentido negativo del eje elegido (hacia la izquierda): termina 300 km a la izquierda de donde partió.",
            "Como no cambia de sentido, la distancia recorrida es el módulo del desplazamiento: 300 km.",
        ],
    ),
    P(
        "u3-5", "f-cinematica", 2, "Física · Práctica U3, ej. 5 y 10",
        "Deducir gráficas a partir de otras",
        "Ejercicio 5: a partir de la gráfica 2 (x-t), deducí las gráficas de velocidad-tiempo y aceleración-tiempo. "
        "La gráfica 2 es una recta descendente: en t = 0 la posición es positiva, la recta corta el eje t y sigue hacia "
        "posiciones negativas.\n\n"
        "Ejercicio 10: determiná las gráficas faltantes en los casos c) y d) (son MRUV).\n"
        "c) Se da la gráfica v-t: una recta que sale del origen (v = 0 en t = 0) y baja, con velocidades cada vez más "
        "negativas. Suponé que el móvil parte del origen.\n"
        "d) Se da la gráfica x-t: una curva que empieza en una posición positiva, baja cortando el eje t y se va "
        "aplanando hasta quedar con tangente horizontal al final del intervalo.",
        [
            C("a) Ejercicio 5: ¿cómo son las gráficas v-t y a-t de la gráfica 2?",
              ["v-t: recta horizontal por debajo del eje t; a-t: sobre el eje t (a = 0)",
               "v-t: recta descendente que cruza el eje t; a-t: horizontal por debajo del eje",
               "v-t: recta horizontal por encima del eje t; a-t: sobre el eje t (a = 0)",
               "v-t: recta horizontal por debajo del eje t; a-t: horizontal por debajo del eje"],
              "v-t: horizontal y negativa; a-t: a = 0"),
            C("b) Ejercicio 10 c): ¿cómo son las gráficas x-t y a-t?",
              ["x-t: rama de parábola que sale del origen hacia x negativos, cada vez más empinada; a-t: horizontal por debajo del eje",
               "x-t: recta descendente desde el origen; a-t: sobre el eje t (a = 0)",
               "x-t: rama de parábola que sale del origen hacia x positivos; a-t: horizontal por encima del eje",
               "x-t: rama de parábola que sale del origen hacia x negativos; a-t: horizontal por encima del eje"],
              "x-t: parábola hacia x negativos con concavidad hacia abajo; a-t: a constante y negativa"),
            C("c) Ejercicio 10 d): ¿cómo son las gráficas v-t y a-t?",
              ["v-t: recta que empieza en un valor negativo y sube hasta v = 0; a-t: horizontal por encima del eje",
               "v-t: recta que empieza en un valor positivo y baja hasta v = 0; a-t: horizontal por debajo del eje",
               "v-t: recta horizontal negativa; a-t: sobre el eje t (a = 0)",
               "v-t: recta que empieza en un valor negativo y se hace más negativa; a-t: horizontal por debajo del eje"],
              "v-t: de negativa a cero; a-t: a constante y positiva"),
        ],
        [
            "La velocidad es la pendiente de la gráfica x-t; la aceleración es la pendiente de la gráfica v-t.",
            "En x-t, una curva que se aplana indica que |v| disminuye; si además baja, v es negativa.",
            "Si v y a tienen el mismo signo el movimiento es acelerado; si tienen signos opuestos, desacelerado.",
        ],
        [
            "Ejercicio 5: la x-t es una recta de pendiente negativa → velocidad constante y negativa (recta horizontal debajo del eje t) y aceleración nula. Es un MRU con velocidad negativa: el móvil pasa por el origen sin cambiar de sentido.",
            "Ejercicio 10 c): v-t recta descendente desde 0 → pendiente negativa constante: a < 0 (horizontal debajo del eje).",
            "La posición: parte de x = 0 y, como v < 0 y crece en valor absoluto, baja cada vez más rápido: rama de parábola con concavidad hacia abajo. v y a tienen el mismo signo: MRUV acelerado.",
            "Ejercicio 10 d): la x-t baja (v < 0) y se aplana hasta tangente horizontal (v = 0 al final): v-t es una recta que sube desde un valor negativo hasta 0.",
            "Esa recta tiene pendiente positiva: a > 0 constante. v < 0 y a > 0: MRUV desacelerado.",
        ],
    ),
    P(
        "u3-6", "f-mru-encuentro", 2, "Física · Práctica U3, ej. 6",
        "Dos vehículos que salen al encuentro",
        "Dos vehículos que se mueven en forma rectilínea salen al encuentro desde ciudades separadas, de norte a sur, por "
        "300 km, con rapideces de 100 km/h (vehículo A) y 72 km/h (vehículo B), respectivamente. Medí las posiciones "
        "desde la ciudad de A.\n"
        "a) Si ambos salen al mismo tiempo, determiná cuánto tardan en encontrarse y en qué posición se cruzan.\n"
        "b) Si el vehículo A sale dos horas más tarde que B (es el caso que resuelve el solucionario), planteá nuevamente "
        "el problema y verificá la posición y el tiempo de encuentro.",
        [
            N("a) ¿Cuánto tardan en encontrarse en a)? Respondé solo con el número en h, con dos decimales.", 1.744, "h", "1,74 h (≈ 1 h 45 min)", 0.01),
            N("b) ¿A qué distancia de la ciudad de A se cruzan en a)? Respondé solo con el número en km.", 174.4, "km", "174 km", 0.01),
            N("c) ¿A qué distancia de la ciudad de A se cruzan en b)? Respondé solo con el número en km.", 90.7, "km", "90,7 km", 0.01),
        ],
        [
            "Escribí las dos ecuaciones horarias con el origen en la ciudad de A: `xA = 100·t` y `xB = 300 − 72·t`. En el encuentro `xA = xB`.",
            "En b), si medís t desde que sale B, A recién arranca en t = 2 h: `xA = 100·(t − 2)`.",
        ],
        [
            "a) `100·t = 300 − 72·t` → `172·t = 300` → `t = 1,744 h ≈ 1 h 45 min` (`0,744 · 60 ≈ 44,7 min`).",
            "Posición: `xA = 100 · 1,744 ≈ 174 km` desde la ciudad de A (y 126 km desde la de B).",
            "b) Con t medido desde la salida de B: `xB = 300 − 72·t` y `xA = 100·(t − 2)` para t ≥ 2 h.",
            "`100·t − 200 = 300 − 72·t` → `172·t = 500` → `t = 2,907 h ≈ 2 h 54 min` desde que salió B (0,907 h después de que salió A).",
            "Posición: `xA = 100 · 0,907 ≈ 90,7 km` desde la ciudad de A. Coincide con el solucionario (2 h 54 min y 90 km).",
            "Verificación: en 2 h, B ya recorrió 144 km; quedan 156 km que se cierran a `100 + 72 = 172 km/h` → 0,907 h.",
        ],
    ),
    P(
        "u3-7", "f-mruv-graficas", 1, "Física · Práctica U3, ej. 7 y 11",
        "Velocidad final en un MRUV",
        "Ejercicio 7: un velocista parte del reposo y acelera durante 4,0 segundos con una aceleración constante de "
        "3,5 m/s² hasta alcanzar su velocidad máxima. Hallá esa velocidad.\n\n"
        "Ejercicio 11: ¿cuál es la velocidad final de un cuerpo cuya velocidad inicial es de 57 m/s y sufre una "
        "aceleración de 1,2 m/s² durante 2 s?",
        [
            N("a) Ejercicio 7: velocidad máxima del velocista. Respondé solo con el número en m/s.", 14, "m/s", "14 m/s"),
            N("b) Ejercicio 11: velocidad final del cuerpo. Respondé solo con el número en m/s.", 59.4, "m/s", "59,4 m/s", 0.01),
        ],
        [
            "En MRUV la velocidad cambia linealmente con el tiempo: `v = v₀ + a·t`.",
        ],
        [
            "Ejercicio 7: `v = v₀ + a·t = 0 + 3,5 m/s² · 4,0 s = 14 m/s`.",
            "Ejercicio 11: `v = 57 m/s + 1,2 m/s² · 2 s = 57 + 2,4 = 59,4 m/s`.",
            "En los dos casos a y v tienen el mismo signo: el movimiento es acelerado y la velocidad aumenta.",
        ],
    ),
    P(
        "u3-8", "f-mruv-graficas", 2, "Física · Práctica U3, ej. 8",
        "Leer una gráfica v-t con tres tramos",
        "Observá la gráfica v-t y contestá. La gráfica está formada por segmentos rectos:\n"
        "|Tramo|t (s)|v (m/s)|\n"
        "|---|---|---|\n"
        "|A|de 0 a 10|constante, 5|\n"
        "|B|de 10 a 20|baja de 5 a 0|\n"
        "|C|de 20 a 30|baja de 0 a −5|\n\n"
        "a) ¿En qué intervalos de tiempo el cuerpo se mueve hacia la derecha y en cuáles hacia la izquierda? b) ¿En cuáles "
        "presenta MRU? c) Calculá la aceleración en los intervalos (10; 20) s, (20; 30) s y (10; 30) s. d) Indicá en qué "
        "intervalos el movimiento es acelerado y en cuáles desacelerado.",
        [
            C("a) ¿Hacia dónde se mueve el cuerpo?",
              ["Hacia la derecha en (0; 20) s y hacia la izquierda en (20; 30) s",
               "Hacia la derecha en (0; 10) s y hacia la izquierda en (10; 30) s",
               "Hacia la derecha en (0; 10) s, quieto en (10; 20) s y hacia la izquierda en (20; 30) s",
               "Siempre hacia la derecha"],
              "Derecha en (0; 20) s; izquierda en (20; 30) s"),
            N("b) ¿Cuánto vale la aceleración en el intervalo (10; 30) s? Respondé solo con el número en m/s², con su signo.", -0.5, "m/s²", "−0,5 m/s²"),
            C("c) ¿Cómo es el movimiento en (10; 20) s y en (20; 30) s?",
              ["Desacelerado en (10; 20) s y acelerado en (20; 30) s",
               "Desacelerado en los dos intervalos, porque a < 0",
               "Acelerado en (10; 20) s y desacelerado en (20; 30) s",
               "Acelerado en los dos intervalos"],
              "Desacelerado en (10; 20) s y acelerado en (20; 30) s"),
        ],
        [
            "El sentido del movimiento lo da el signo de v, no el de a. La aceleración es la pendiente de la recta v-t.",
            "Acelerado = |v| aumenta (v y a del mismo signo); desacelerado = |v| disminuye (signos opuestos).",
        ],
        [
            "a) v > 0 en (0; 20) s → hacia la derecha; v < 0 en (20; 30) s → hacia la izquierda. En t = 20 s se detiene un instante y cambia de sentido.",
            "b) MRU (v constante, a = 0) solo en (0; 10) s.",
            "c) `a(10; 20) = (0 − 5)/10 = −0,5 m/s²`; `a(20; 30) = (−5 − 0)/10 = −0,5 m/s²`; `a(10; 30) = (−5 − 5)/20 = −0,5 m/s²`. Es la misma recta, por eso la pendiente no cambia.",
            "d) En (10; 20) s, v > 0 y a < 0: desacelerado (frena). En (20; 30) s, v < 0 y a < 0: acelerado (|v| crece hacia la izquierda).",
            "Error típico: decir que 'a negativa' siempre significa frenar.",
        ],
    ),
    P(
        "u3-9", "f-cinematica", 2, "Física · Práctica U3, ej. 9",
        "Analizar una parábola en la gráfica x-t",
        "Analizá el movimiento de la siguiente gráfica x-t: es una parábola con concavidad hacia abajo que pasa por "
        "x = 20 m en t = 0, alcanza su vértice (x ≈ 32 m) en t = 5 s y corta el eje t (x = 0) en t ≈ 13 s.",
        [
            C("a) ¿Cómo es el movimiento entre 0 y 5 s?",
              ["Hacia la derecha (v > 0) y desacelerado", "Hacia la derecha (v > 0) y acelerado", "Hacia la izquierda (v < 0) y desacelerado", "MRU hacia la derecha"],
              "Hacia la derecha y desacelerado"),
            C("b) ¿Qué pasa en t = 5 s?",
              ["La velocidad es cero por un instante y el móvil cambia de sentido", "La aceleración es cero", "El móvil pasa por el origen", "La velocidad es máxima"],
              "v = 0 por un instante: el móvil pega la vuelta"),
            C("c) ¿Cómo es el movimiento entre 5 y 13 s?",
              ["Hacia la izquierda (v < 0) y acelerado", "Hacia la izquierda (v < 0) y desacelerado", "Hacia la derecha (v > 0) y acelerado", "Hacia la izquierda con velocidad constante"],
              "Hacia la izquierda y acelerado"),
        ],
        [
            "La pendiente de la recta tangente a la curva x-t es la velocidad; la concavidad indica el signo de la aceleración (hacia abajo: a < 0).",
            "Compará el signo de v con el de a en cada intervalo.",
        ],
        [
            "Concavidad hacia abajo en toda la gráfica: a < 0 constante (MRUV).",
            "Entre 0 y 5 s la tangente tiene pendiente positiva (v > 0) y va perdiendo inclinación: el móvil va hacia la derecha y desacelera (v y a de signos opuestos).",
            "En t = 5 s la tangente es horizontal: v = 0 por un instante; ahí el móvil pega la vuelta (posición máxima ≈ 32 m).",
            "Entre 5 y 13 s la pendiente es negativa y cada vez más empinada: v < 0 y a < 0, movimiento acelerado hacia la izquierda; vuelve a pasar por 20 m y llega a x = 0 a los 13 s.",
            "Error típico: confundir el vértice de la parábola (v = 0) con un punto de aceleración nula; la aceleración es la misma en todo el recorrido.",
        ],
    ),
    P(
        "u3-12", "f-mruv-graficas", 2, "Física · Práctica U3, ej. 12",
        "El ciclista que acelera",
        "Un ciclista que pedalea a 5,00 m/s (18,0 km/h) acelera a razón de 0,20 m/s². ¿Cuánto tarda en recorrer 200 m? "
        "¿Cuál será su velocidad en ese momento?",
        [
            N("a) ¿Cuánto tarda en recorrer 200 m? Respondé solo con el número en s, con un decimal.", 26.23, "s", "26,2 s", 0.01),
            N("b) ¿Qué velocidad tiene en ese momento? Respondé solo con el número en m/s, con un decimal.", 10.25, "m/s", "10,2 m/s", 0.01),
        ],
        [
            "Planteá `Δx = v₀·t + ½·a·t²` con Δx = 200 m: queda una ecuación cuadrática en t.",
            "De las dos soluciones de la cuadrática, quedate con la positiva.",
        ],
        [
            "`200 = 5,00·t + ½·0,20·t²` → `0,10·t² + 5,00·t − 200 = 0`.",
            "`t = (−5,00 + √(5,00² + 4·0,10·200)) / (2·0,10) = (−5,00 + √105) / 0,20 ≈ (−5,00 + 10,25)/0,20 ≈ 26,2 s`.",
            "La otra raíz es negativa y no tiene sentido físico.",
            "`v = v₀ + a·t = 5,00 + 0,20·26,2 ≈ 10,2 m/s` (o `v² = v₀² + 2·a·Δx = 25 + 80 = 105` → `v ≈ 10,2 m/s`).",
        ],
    ),
    P(
        "u3-13", "f-mruv-graficas", 1, "Física · Práctica U3, ej. 13",
        "Cuatro metros en el primer segundo",
        "Un automóvil que parte del reposo, con aceleración constante, recorre en el primer segundo 4 metros. ¿Qué "
        "aceleración posee? ¿Qué velocidad tendrá a los 10 segundos?",
        [
            N("a) ¿Qué aceleración tiene? Respondé solo con el número en m/s².", 8, "m/s²", "8 m/s²"),
            N("b) ¿Qué velocidad tiene a los 10 s? Respondé solo con el número en m/s.", 80, "m/s", "80 m/s"),
        ],
        [
            "Desde el reposo, `Δx = ½·a·t²`: reemplazá Δx = 4 m y t = 1 s y despejá a.",
        ],
        [
            "`4 m = ½·a·(1 s)²` → `a = 2·4/1 = 8 m/s²`.",
            "`v(10 s) = 0 + 8 m/s² · 10 s = 80 m/s`.",
            "Error típico: hacer `a = Δx/t² = 4 m/s²`, olvidando el factor ½ de la ecuación horaria.",
        ],
    ),
    P(
        "u3-14", "f-mruv-graficas", 3, "Física · Práctica U3, ej. 14",
        "De la gráfica a-t a la distancia recorrida",
        "Un vehículo parte del reposo y se mueve en forma rectilínea durante todo el recorrido, hacia la derecha al menos "
        "durante el primer y el segundo tramo. Su gráfica aceleración-tiempo es:\n"
        "|Tramo|t (s)|a (m/s²)|\n"
        "|---|---|---|\n"
        "|1|de 0 a 2|1,5|\n"
        "|2|de 2 a 2,5|0|\n"
        "|3|de 2,5 a 4|−4|\n\n"
        "A partir de esta gráfica, indicá la distancia que recorrió, la velocidad final e interpretá qué sucede durante el recorrido.",
        [
            N("a) ¿Cuál es la velocidad final (en t = 4 s)? Respondé solo con el número en m/s, con su signo.", -3, "m/s", "−3 m/s"),
            N("b) ¿Qué distancia total recorrió entre 0 y 4 s? Respondé solo con el número en m.", 6.75, "m", "6,75 m", 0.01),
            N("c) ¿Cuánto vale el desplazamiento total entre 0 y 4 s? Respondé solo con el número en m.", 4.5, "m", "4,5 m", 0.01),
        ],
        [
            "Encadená los tramos: la velocidad final de uno es la inicial del siguiente (`v = v₀ + a·t`).",
            "En el tercer tramo la velocidad pasa de positiva a negativa: buscá el instante en que se anula y separá el tramo en dos (ida y vuelta).",
            "La distancia suma lo recorrido en cada parte en valor absoluto; el desplazamiento los suma con signo.",
        ],
        [
            "Tramo 1 (MRUV acelerado, v > 0 y a > 0): `v(2) = 1,5·2 = 3 m/s`; `Δx₁ = ½·1,5·2² = 3 m`.",
            "Tramo 2 (MRU): `Δx₂ = 3 m/s · 0,5 s = 1,5 m`.",
            "Tramo 3: `v(4) = 3 + (−4)·1,5 = −3 m/s`. Se detiene cuando `3 − 4·t' = 0` → `t' = 0,75 s` (en t = 3,25 s).",
            "Ida: `Δx₃' = 3²/(2·4) = 1,125 m` hacia la derecha. Vuelta (0,75 s desde el reposo con a = −4): `Δx₄' = −½·4·0,75² = −1,125 m`. El desplazamiento del tramo 3 es 0.",
            "Distancia total: `3 + 1,5 + 1,125 + 1,125 = 6,75 m` (el solucionario da 6,76 m porque redondea a 1,13 m cada parte). Desplazamiento total: `3 + 1,5 + 0 = 4,5 m`.",
            "Interpretación: acelera hacia la derecha, sigue con velocidad constante, frena hasta detenerse a los 3,25 s y después acelera hacia la izquierda; termina con v = −3 m/s.",
        ],
    ),
    P(
        "u3-15", "f-mruv-graficas", 2, "Física · Práctica U3, ej. 15",
        "Velocidad a partir del área de la gráfica v-t",
        "Para la siguiente gráfica v-t, hallá la velocidad en t = 5 s si el recorrido es de 120 m en 7 s. La gráfica es: "
        "una recta que sube desde v = 0 en t = 0 hasta un valor v_máx en t = 2 s, y luego una recta horizontal "
        "(v = v_máx) desde t = 2 s hasta t = 7 s.",
        [
            N("a) ¿Cuánto vale la velocidad en t = 5 s? Respondé solo con el número en m/s.", 20, "m/s", "20 m/s"),
            N("b) ¿Cuánto vale la aceleración entre 0 y 2 s? Respondé solo con el número en m/s².", 10, "m/s²", "10 m/s²"),
        ],
        [
            "El desplazamiento es el área bajo la gráfica v-t: un triángulo (0 a 2 s) más un rectángulo (2 a 7 s), los dos con altura v_máx.",
            "En t = 5 s el móvil está en el tramo horizontal.",
        ],
        [
            "Área del triángulo: `½·2 s·v_máx = 1 s·v_máx`. Área del rectángulo: `5 s·v_máx`.",
            "`120 m = 1·v_máx + 5·v_máx = 6 s·v_máx` → `v_máx = 20 m/s`.",
            "En t = 5 s está en el tramo de velocidad constante: **v = 20 m/s**.",
            "Aceleración del primer tramo: `a = 20 m/s / 2 s = 10 m/s²`.",
        ],
    ),
    P(
        "u3-16", "f-mru-encuentro", 3, "Física · Práctica U3, ej. 16",
        "El auto y el metrotranvía",
        "Un automóvil se desplaza por una carretera paralela a la vía de un metrotranvía. El automóvil se detiene ante un "
        "semáforo en rojo en el mismo instante en que pasa un metrotranvía con una rapidez constante de 12,0 m/s. El "
        "automóvil permanece detenido durante 6,0 s y luego parte con una aceleración constante de 2,0 m/s². Determiná:\n"
        "a) el tiempo que emplea el automóvil en alcanzar al metrotranvía, medido desde el instante en que se detuvo ante el semáforo;\n"
        "b) la distancia que recorrió el automóvil desde el semáforo hasta que alcanzó al metrotranvía;\n"
        "c) la rapidez del automóvil en el instante en que alcanza al metrotranvía.",
        [
            N("a) Tiempo desde que el auto se detuvo. Respondé solo con el número en s, con un decimal.", 22.39, "s", "22,4 s", 0.01),
            N("b) Distancia recorrida por el auto. Respondé solo con el número en m.", 268.7, "m", "268,7 m", 0.01),
            N("c) Rapidez del auto al alcanzarlo. Respondé solo con el número en m/s.", 32.78, "m/s", "32,8 m/s", 0.01),
        ],
        [
            "Tomá el origen en el semáforo y t = 0 cuando el auto se detiene. Metrotranvía (MRU): `xM = 12,0·t`.",
            "El auto arranca recién en t = 6,0 s: `xA = ½·2,0·(t − 6,0)²` para t ≥ 6,0 s.",
            "Igualá las posiciones y resolvé la cuadrática; quedate con la raíz mayor que 6,0 s.",
        ],
        [
            "Ecuaciones: `xM = 12,0·t` y `xA = (t − 6,0)²` (porque ½·2,0 = 1,0).",
            "`12,0·t = t² − 12,0·t + 36` → `t² − 24,0·t + 36 = 0` → `t = 12 ± √108`. La raíz 1,6 s es anterior a la partida del auto; queda `t = 12 + 10,39 = 22,4 s`.",
            "b) `x = 12,0 · 22,39 ≈ 268,7 m` (igual que `(22,39 − 6,0)² ≈ 268,7 m`).",
            "c) `v = 2,0 · (22,39 − 6,0) ≈ 32,8 m/s`.",
            "Diferencia con el solucionario: da t = 16,4 s, que es el tiempo medido desde que el auto ARRANCA (22,4 − 6,0); la consigna pide medirlo desde que se detuvo. También da 269,9 m y 32,9 m/s: con t = 22,39 s salen 268,7 m y 32,8 m/s.",
        ],
    ),
    P(
        "u3-17", "f-caida-libre-tiro-vertical", 2, "Física · Práctica U3, ej. 17",
        "Disparo hacia arriba desde un edificio",
        "Se dispara desde lo alto de un edificio un pequeño cuerpo hacia arriba, de manera que vuelve a pasar por el "
        "sitio de disparo, ahora hacia abajo, 3 segundos después. Finalmente, a los 10 segundos de haber sido lanzado, "
        "llega al piso (g = 9,8 m/s², eje y hacia arriba).\n"
        "a) ¿Con qué velocidad fue disparado? b) ¿Cuál fue su altura máxima? c) ¿Cuánto mide el edificio?",
        [
            N("a) Velocidad de disparo. Respondé solo con el número en m/s.", 14.7, "m/s", "14,7 m/s", 0.01),
            N("b) Altura máxima, medida desde el punto de disparo. Respondé solo con el número en m.", 11.025, "m", "11,0 m (11,025 m)", 0.01),
            N("c) Altura del edificio. Respondé solo con el número en m.", 343, "m", "343 m", 0.01),
        ],
        [
            "Por simetría del tiro vertical, sube durante la mitad de los 3 s que tarda en volver al punto de disparo.",
            "En la altura máxima v = 0: `v₀ = g·t_subida` y `h = v₀²/(2g)`.",
            "Para el edificio, usá `y(10 s) = v₀·t − ½·g·t²` con origen en el punto de disparo: el resultado negativo es la altura del edificio.",
        ],
        [
            "Tiempo de subida: `3 s / 2 = 1,5 s`. En la altura máxima `v = 0 = v₀ − 9,8·1,5` → `v₀ = 14,7 m/s`.",
            "`h_máx = v₀²/(2g) = 14,7²/19,6 = 11,025 m ≈ 11,0 m` por encima del punto de disparo.",
            "Con origen en el punto de disparo: `y(10) = 14,7·10 − ½·9,8·10² = 147 − 490 = −343 m`.",
            "El piso está 343 m por debajo del punto de disparo: el edificio mide **343 m** (y la altura máxima respecto del piso es 343 + 11,0 ≈ 354 m).",
        ],
    ),
    P(
        "u3-18", "f-caida-libre-tiro-vertical", 1, "Física · Práctica U3, ej. 18 y 19",
        "La bomba y los dos objetos que caen",
        "Ejercicio 18: una bomba que se deja caer libremente desde un avión tarda 10 segundos en dar en el blanco. ¿A qué "
        "altura volaba el avión?\n\n"
        "Ejercicio 19: se deja caer un objeto al mismo tiempo que otro que es lanzado hacia abajo con una rapidez de "
        "2,0 m/s. ¿Cuánto tiempo pasará para que la distancia entre ellos sea de 18 metros?\n\n"
        "Usá g = 9,8 m/s².",
        [
            N("a) Ejercicio 18: altura del avión. Respondé solo con el número en m.", 490, "m", "490 m"),
            N("b) Ejercicio 19: tiempo hasta que están separados 18 m. Respondé solo con el número en s.", 9, "s", "9 s"),
        ],
        [
            "Caída libre desde el reposo: `h = ½·g·t²`.",
            "En el ejercicio 19 los dos tienen la misma aceleración: restá sus posiciones y fijate qué término sobrevive.",
        ],
        [
            "Ejercicio 18: `h = ½ · 9,8 · 10² = 490 m`.",
            "Ejercicio 19 (eje hacia abajo, origen en el punto de partida): `y₁ = ½·g·t²` y `y₂ = 2,0·t + ½·g·t²`.",
            "Distancia entre ellos: `y₂ − y₁ = 2,0·t`: los términos de g se cancelan, porque los dos aceleran igual.",
            "`2,0·t = 18` → `t = 9 s`.",
        ],
    ),
    P(
        "u3-20", "f-caida-libre-tiro-vertical", 3, "Física · Práctica U3, ej. 20",
        "Correr para atrapar la pelota",
        "Un niño que se encuentra en la calle ve caer una pelota verticalmente desde una ventana. Si el niño está parado "
        "a 4 m de distancia en horizontal del punto de caída y la altura de la ventana es de 15 m, calculá a qué velocidad "
        "terminará corriendo para atraparla antes de que llegue al suelo. Suponé, como en el desarrollo del curso, que el "
        "niño arranca desde el reposo en el mismo instante en que la pelota empieza a caer, corre en línea recta con "
        "aceleración constante y la atrapa justo al llegar al suelo (g = 9,8 m/s²).",
        [
            N("a) ¿Cuánto tarda la pelota en llegar al suelo? Respondé solo con el número en s, con dos decimales.", 1.7496, "s", "1,75 s", 0.01),
            N("b) ¿Con qué velocidad termina corriendo el niño? Respondé solo con el número en m/s, con dos cifras significativas.", 4.572, "m/s", "4,6 m/s", 0.03),
        ],
        [
            "La pelota cae desde el reposo: `15 = ½·9,8·t²`.",
            "El niño recorre 4 m desde el reposo en ese mismo tiempo: `4 = ½·a·t²`. Despejá a y después `v = a·t`.",
            "Atajo: desde el reposo con aceleración constante, la velocidad media es la mitad de la final, así que `v_final = 2·d/t`.",
        ],
        [
            "Tiempo de caída: `t = √(2·15/9,8) = √3,06 ≈ 1,75 s`.",
            "El niño: `4 = ½·a·t²` → `a = 8/t² = 8/3,06 ≈ 2,61 m/s²`.",
            "`v = a·t = 8/t = 8/1,75 ≈ 4,57 m/s ≈ 4,6 m/s`.",
            "El solucionario da 4,7 m/s porque redondea antes el tiempo a 1,7 s (8/1,7 ≈ 4,7). Sin redondear en el medio sale 4,57 m/s; el corrector acepta también 4,7 m/s (el valor con t redondeado a 1,7 s).",
            "Si el niño corriera con velocidad constante, alcanzaría con `4/1,75 ≈ 2,3 m/s`; el enunciado habla de la velocidad con la que 'termina corriendo', por eso se interpreta que acelera desde el reposo.",
        ],
    ),
    # ======================================================================
    # GUÍAS · MATERIAL COMPLEMENTARIO (parte B, con grilla)
    # ======================================================================
    P(
        "tp1b-5", "f-analisis-dimensional", 2, "Física · Guía TP1 parte B, ej. 5 c y d",
        "Constantes dimensionales en fórmulas",
        "c) Hallá la dimensión de α y β en la fórmula `V = α·A + β·D`, siendo V: volumen; A: área; D: densidad.\n"
        "d) La velocidad de cierto móvil puede determinarse con la fórmula empírica `v = a·T³ + b/(T² − c)`, donde T: "
        "tiempo; v: velocidad; y a, b, c son constantes dimensionales para que la fórmula sea homogénea. Hallá sus dimensiones.",
        [
            C("a) ¿Cuál es la dimensión de β?", ["M⁻¹·L⁶", "M·L⁻⁶", "L", "M⁻¹·L³"], "[β] = M⁻¹·L⁶"),
            C("b) ¿Cuál es la dimensión de a?", ["L·T⁻⁴", "L·T⁻²", "L·T²", "L·T⁻³"], "[a] = L·T⁻⁴"),
            C("c) ¿Cuál es la dimensión de b?", ["L·T", "L·T⁻¹", "L·T⁻³", "T²"], "[b] = L·T"),
        ],
        [
            "Homogeneidad: cada término de una suma tiene la misma dimensión que el miembro izquierdo.",
            "Solo se pueden restar magnitudes de la misma dimensión: en `T² − c`, c tiene que tener dimensión T².",
        ],
        [
            "c) `[α·A] = [V]` → `[α] = L³/L² = L`. `[β·D] = [V]` con `[D] = M·L⁻³` → `[β] = L³/(M·L⁻³) = M⁻¹·L⁶`.",
            "d) `[a·T³] = [v] = L·T⁻¹` → `[a] = L·T⁻¹/T³ = L·T⁻⁴`.",
            "En `T² − c` se restan magnitudes de la misma dimensión: `[c] = T²`, y entonces `[T² − c] = T²`.",
            "`[b/T²] = L·T⁻¹` → `[b] = L·T⁻¹·T² = L·T`.",
            "Coincide con la grilla: [α] = L; [β] = M⁻¹·L⁶; [a] = L·T⁻⁴; [b] = L·T; [c] = T².",
        ],
    ),
    P(
        "tp1b-6a", "f-sistemas-unidades", 2, "Física · Guía TP1 parte B, ej. 6 b, d y j",
        "Gotas, milímetros de mercurio y pies",
        "b) Un surtidor pierde agua a razón de 27 litros por mes (30 días). Expresá dicha pérdida en gotas por minuto, si "
        "el volumen estimado de una gota es de 2,5 mm³.\n"
        "d) Expresá 200 mm Hg en kgf/m² (760 mm Hg = 1,013×10⁵ N/m²; 1 kgf = 9,8 N).\n"
        "j) ¿A cuántos km/h² equivale 4,62 (pie/s)/min? (1 pie = 30,48 cm)",
        [
            N("b) ¿Cuántas gotas por minuto pierde? Respondé solo con el número.", 250, "gotas/min", "250 gotas/min"),
            N("d) ¿Cuántos kgf/m² son 200 mm Hg? Respondé solo con el número, con 3 cifras significativas." + SNX, 2720, "kgf/m²", "2,72×10³ kgf/m²", 0.01),
            N("j) ¿A cuántos km/h² equivale? Respondé solo con el número, con 3 cifras significativas." + SN, 304.2, "km/h²", "304 km/h² = 3,04×10² km/h²", 0.01),
        ],
        [
            "Armá una cadena de fracciones unitarias: en b) L → dm³ → mm³ → gotas, y mes → días → h → min.",
            "En d) primero pasá mm Hg a N/m² con la equivalencia dada y después N a kgf.",
            "En j) (pie/s)/min es una aceleración: pasá pie → km, s → h y min → h.",
        ],
        [
            "b) `27 L/mes · (10⁶ mm³ / 1 L) · (1 gota / 2,5 mm³) · (1 mes / 30 días) · (1 día / 1440 min) = 1,08×10⁷ / 43 200 = 250 gotas/min`.",
            "d) `200 mm Hg · (1,013×10⁵ N/m² / 760 mm Hg) = 2,666×10⁴ N/m²`.",
            "`2,666×10⁴ N/m² · (1 kgf / 9,8 N) = 2,72×10³ kgf/m²` (con 9,806 65 da 2,718×10³: el corrector acepta los dos).",
            "j) `4,62 pie/(s·min) · (0,3048 m / 1 pie) · (1 km / 1000 m) · (3600 s / 1 h) · (60 min / 1 h) = 4,62 · 0,3048 · 216 ≈ 304 km/h²`.",
            "Respuestas, como en la grilla: 250 gotas/min; 2,72×10³ kgf/m²; 3,04×10² km/h².",
        ],
    ),
    P(
        "tp1b-6b", "f-cifras-significativas", 3, "Física · Guía TP1 parte B, ej. 6 f, g e i",
        "Densidades y energía con prefijos y cifras",
        "f) La masa de la Tierra está estimada en 5,98×10¹⁸ Gg y su volumen es de 1,083×10³⁰ mm³. Su densidad (δ = m/V), "
        "expresada en unidades del SI y con el número de cifras significativas correcto, es:\n"
        "g) La energía en reposo E de un objeto con masa en reposo m está dada por la ecuación de Einstein `E = m·c²`. Si "
        "la masa del electrón es 9,11×10⁻³⁴ Mg y la velocidad de la luz es c = 299 792 458 000 mm/s, E expresada en "
        "unidades del SI y con el número de cifras significativas correcto es:\n"
        "i) Un cuerpo de masa 1 500 Mg ocupa un volumen de 4,5×10¹² m³. Su densidad, expresada en μg/m³, es:",
        [
            N("f) Densidad de la Tierra en kg/m³, con 3 cifras significativas. Respondé solo con el número." + SNX, 5520, "kg/m³", "5,52×10³ kg/m³", 0.003),
            C("g) ¿Cuánto vale E?", ["8,19×10⁻¹⁴ J", "8,19×10⁻¹⁷ J", "8,19×10⁻⁸ J", "8,187 66×10⁻¹⁴ J"], "8,19×10⁻¹⁴ J"),
            N("i) Densidad en μg/m³, con 2 cifras significativas. Respondé solo con el número." + SNX, 330, "μg/m³", "3,3×10² μg/m³", 0.005),
        ],
        [
            "Pasá todo a unidades SI antes de operar: Gg = 10⁶ kg, Mg = 10³ kg, y `1 mm³ = (10⁻³ m)³ = 10⁻⁹ m³`.",
            "El resultado lleva tantas cifras significativas como el dato que menos tenga (c tiene muchas; no limita).",
            "En i) pasá la masa a μg: `1 Mg = 10⁶ g = 10¹² μg`.",
        ],
        [
            "f) `m = 5,98×10¹⁸ Gg = 5,98×10¹⁸ · 10⁶ kg = 5,98×10²⁴ kg`; `V = 1,083×10³⁰ mm³ · 10⁻⁹ m³/mm³ = 1,083×10²¹ m³`.",
            "`δ = 5,98×10²⁴ / 1,083×10²¹ = 5,52×10³ kg/m³` (3 cifras, por 5,98).",
            "g) `m = 9,11×10⁻³⁴ Mg = 9,11×10⁻³¹ kg`; `c = 2,997 924 58×10⁸ m/s`. `E = 9,11×10⁻³¹ · (2,998×10⁸)² = 8,19×10⁻¹⁴ J` (3 cifras, por 9,11).",
            "Distractores de g): 10⁻¹⁷ J sale de tomar la masa como si estuviera en kg; 10⁻⁸ J, de dejar c en mm/s; 8,187 66 tiene demasiadas cifras.",
            "i) `m = 1 500 Mg = 1,5×10¹⁵ μg`; `δ = 1,5×10¹⁵ / 4,5×10¹² = 333 μg/m³` → con 2 cifras (por 4,5): **3,3×10² μg/m³**.",
        ],
    ),
    P(
        "tp2b-10", "f-vectores-operaciones", 2, "Física · Guía TP2 parte B, ej. 10 C y D",
        "Desplazamientos hacia el sur, el oeste y el norte",
        "C) Inicialmente una partícula se desplaza 8 km hacia el sur y 5 segundos después se desplaza 6 km hacia el "
        "oeste. ¿Cuál es el desplazamiento total de la partícula? (Indicá la dirección respecto del este.)\n"
        "D) Un avión vuela 450 km al este y luego se desplaza una distancia hacia el norte. Finalmente regresa a su punto "
        "de partida recorriendo 525 km en línea recta. ¿Cuánto recorrió el avión en dirección norte? ¿Qué dirección tomó "
        "en su regreso al punto de partida, tomando como referencia la dirección este?",
        [
            N("a) C) Ángulo del desplazamiento total medido desde el este en sentido antihorario. Respondé solo con el número en grados decimales.", 233.13, "°", "233,13° (= 233°08´)", 0.01),
            N("b) D) ¿Cuánto recorrió hacia el norte? Respondé solo con el número en km.", 270.4, "km", "270 km", 0.01),
            N("c) D) Ángulo del tramo de regreso medido desde el este en sentido antihorario. Respondé solo con el número en grados.", 211.0, "°", "211°", 0.01),
        ],
        [
            "Tomá x hacia el este e y hacia el norte y escribí cada desplazamiento como un par de componentes.",
            "En D) los tres tramos forman un triángulo rectángulo cerrado: el regreso es la hipotenusa.",
            "Calculá el ángulo agudo con la tangente y ubicá el cuadrante con los signos de las componentes.",
        ],
        [
            "C) `Δr = (0; −8) + (−6; 0) = (−6; −8) km`. Módulo: `√(36 + 64) = 10 km`.",
            "III cuadrante: agudo con el oeste `arctg(8/6) = 53,13°` → desde el este antihorario: `180° + 53,13° = 233,13°` (suroeste). La grilla lo da como 233°.",
            "D) `525² = 450² + N²` → `N = √(275 625 − 202 500) = √73 125 ≈ 270 km`.",
            "El regreso es el vector `(−450; −270) km`, en el III cuadrante: agudo `arctg(270/450) ≈ 31°` → `180° + 31° = 211°`.",
            "Coincide con la grilla: 10 km a 233°; N ≈ 270 km; regreso a 211°.",
        ],
    ),
    P(
        "tp3b1-3", "f-mruv-graficas", 2, "Física · Guía TP3 parte B1, ej. 3",
        "Desplazamiento y distancia con el área de v-t",
        "La gráfica muestra la velocidad de un móvil que se desplaza con movimiento rectilíneo, en función del tiempo. Está "
        "formada por segmentos rectos que unen estos puntos:\n"
        "|t (s)|0|10|20|30|40|50|\n"
        "|---|---|---|---|---|---|---|\n"
        "|v (m/s)|0|20|10|10|0|−10|\n\n"
        "Calculá: c) ¿en qué instante el móvil está detenido?; d) el desplazamiento realizado al cabo de los 50 s; g) la "
        "distancia recorrida durante los 50 primeros segundos.",
        [
            N("a) ¿En qué instante, además de t = 0, el móvil está detenido? Respondé solo con el número en s.", 40, "s", "40 s"),
            N("b) ¿Cuánto vale el desplazamiento entre 0 y 50 s? Respondé solo con el número en m.", 350, "m", "350 m"),
            N("c) ¿Qué distancia recorrió entre 0 y 50 s? Respondé solo con el número en m.", 450, "m", "450 m"),
        ],
        [
            "Detenido significa v = 0: buscá dónde la gráfica toca el eje t.",
            "El desplazamiento es el área bajo la curva v-t, con signo (las áreas por debajo del eje restan).",
            "La distancia suma todas las áreas en valor absoluto.",
        ],
        [
            "c) v = 0 en t = 0 s y en t = 40 s.",
            "Áreas por tramo: (0; 10) s triángulo `½·10·20 = 100 m`; (10; 20) s trapecio `(20 + 10)/2·10 = 150 m`; (20; 30) s rectángulo `10·10 = 100 m`.",
            "(30; 40) s triángulo `½·10·10 = 50 m`; (40; 50) s triángulo por debajo del eje: `−½·10·10 = −50 m`.",
            "d) Desplazamiento: `100 + 150 + 100 + 50 − 50 = 350 m`.",
            "g) Distancia: `100 + 150 + 100 + 50 + 50 = 450 m`. Coincide con la grilla. Además: desacelera en (10; 20) s y (30; 40) s, y en (40; 50) s acelera hacia la izquierda.",
        ],
    ),
    P(
        "tp3b1-7h", "f-mru-encuentro", 3, "Física · Guía TP3 parte B1, ej. 7 H",
        "Persecución con arranque demorado",
        "Un móvil que pasa por un punto a 32 m/s comienza a ser perseguido por otro móvil que estaba detenido en ese "
        "punto y que desarrolla una aceleración de 1 m/s². Si el móvil perseguidor tarda 9 segundos en comenzar a acelerar:\n"
        "a) ¿Cuánto tiempo tarda en alcanzarlo? b) ¿Cuántos metros recorre hasta alcanzarlo? c) ¿Qué velocidad alcanza al "
        "encontrar al otro móvil? (Medí el tiempo desde que el primero pasa por el punto.)",
        [
            N("a) Tiempo hasta el encuentro. Respondé solo con el número en s.", 81, "s", "81 s"),
            N("b) Distancia recorrida hasta alcanzarlo. Respondé solo con el número en m.", 2592, "m", "2592 m"),
            N("c) Velocidad del perseguidor al alcanzarlo. Respondé solo con el número en m/s.", 72, "m/s", "72 m/s"),
        ],
        [
            "Origen en el punto y t = 0 cuando pasa el primero: `x₁ = 32·t` y, para t ≥ 9 s, `x₂ = ½·1·(t − 9)²`.",
            "Igualá y resolvé la cuadrática; una de las raíces es anterior a que el perseguidor arranque.",
        ],
        [
            "`32·t = ½·(t − 9)²` → `64·t = t² − 18·t + 81` → `t² − 82·t + 81 = 0`.",
            "Raíces: `t = 1 s` y `t = 81 s`. La de 1 s no sirve: en ese instante el perseguidor todavía no arrancó (empieza a los 9 s). Queda **t = 81 s**.",
            "Distancia: `x = 32 · 81 = 2592 m` (verificación: `½·(81 − 9)² = ½·72² = 2592 m`).",
            "Velocidad del perseguidor: `v = 1 · (81 − 9) = 72 m/s`.",
            "Coincide con la grilla (81 s; 2592 m; 72 m/s).",
        ],
    ),
    P(
        "tp3b2-2a", "f-caida-libre-tiro-vertical", 3, "Física · Guía TP3 parte B2, ej. 2 A",
        "Dos piedras lanzadas con dos segundos de diferencia",
        "Una persona lanza una piedra verticalmente hacia arriba con una velocidad de 86,4 km/h (24 m/s) y a los dos "
        "segundos lanza otra piedra, con la misma velocidad y en el mismo sentido (g = 9,8 m/s², eje y hacia arriba con "
        "origen en el punto de lanzamiento).\n"
        "a) ¿En qué tiempo se encuentran las piedras? b) ¿A qué altura se produce el encuentro? c) ¿Qué velocidad tiene "
        "cada piedra en el momento del cruce?",
        [
            N("a) Tiempo de encuentro, medido desde el primer lanzamiento. Respondé solo con el número en s.", 3.449, "s", "3,45 s", 0.01),
            N("b) Altura del encuentro. Respondé solo con el número en m.", 24.49, "m", "24,5 m", 0.01),
            N("c) Velocidad de la primera piedra en el cruce, con signo (eje y hacia arriba). Respondé solo con el número en m/s.", -9.8, "m/s", "−9,8 m/s", 0.01),
        ],
        [
            "Escribí las dos ecuaciones horarias con el mismo reloj: `y₁ = 24·t − 4,9·t²` e `y₂ = 24·(t − 2) − 4,9·(t − 2)²`.",
            "Al igualarlas, los términos en t² se cancelan y queda una ecuación lineal.",
        ],
        [
            "`24·t − 4,9·t² = 24·t − 48 − 4,9·(t² − 4·t + 4)`.",
            "Simplificando: `0 = −48 + 19,6·t − 19,6` → `t = 67,6/19,6 ≈ 3,45 s`.",
            "Altura: `y = 24·3,449 − 4,9·3,449² ≈ 82,8 − 58,3 ≈ 24,5 m`.",
            "Velocidades: `v₁ = 24 − 9,8·3,449 ≈ −9,8 m/s` (ya baja) y `v₂ = 24 − 9,8·1,449 ≈ +9,8 m/s` (todavía sube).",
            "Son opuestas porque se cruzan a la misma altura en tramos simétricos del mismo tiro. La grilla da ±9,81 m/s (redondeo).",
        ],
    ),
    P(
        "tp3b2-2g", "f-caida-libre-tiro-vertical", 3, "Física · Guía TP3 parte B2, ej. 2 G",
        "La cañita voladora que se queda sin combustible",
        "Una cañita voladora, que parte del reposo a nivel del piso, es impulsada verticalmente hacia arriba con una "
        "aceleración que se supone constante mientras dura el combustible. Este se agota a los 5 segundos de partir, "
        "cuando está a 100 m de altura. Desde ese instante se mueve libremente hasta que regresa al punto de partida "
        "(considerá g = 10 m/s²).\n"
        "a) Determiná la máxima velocidad que alcanzará al ascender. b) ¿A qué altura máxima del piso llegará la cañita?",
        [
            N("a) Velocidad máxima al ascender. Respondé solo con el número en m/s.", 40, "m/s", "40 m/s"),
            N("b) Altura máxima respecto del piso. Respondé solo con el número en m.", 180, "m", "180 m"),
        ],
        [
            "Primera etapa (con combustible), desde el reposo: `100 = ½·a·5²` te da la aceleración del motor.",
            "La velocidad máxima es la que tiene cuando se apaga el motor; después solo actúa g y empieza a frenar.",
            "Segunda etapa: sube `v²/(2g)` más por encima de los 100 m.",
        ],
        [
            "Etapa con motor: `100 = ½·a·25` → `a = 8 m/s²`.",
            "Velocidad al agotarse el combustible: `v = 8·5 = 40 m/s`. Es la máxima: a partir de ahí la gravedad la reduce.",
            "Subida libre: `Δh = v²/(2g) = 40²/20 = 80 m`.",
            "Altura máxima: `100 + 80 = 180 m`.",
            "La grilla tiene las respuestas invertidas (dice a) hmáx = 180 m y b) vmáx = 40 m/s): lo que pide a) es la velocidad, 40 m/s, y lo que pide b) es la altura, 180 m.",
        ],
    ),
]
