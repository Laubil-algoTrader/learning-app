"""Ejercicios de Física (borrador): introducción, cinemática panorámica, termodinámica,
ondas y sonido, y electricidad y campos.

Tres problemas (niveles 1, 2 y 3) para f-intro-fisica y f-cinematica; cuatro problemas
(niveles 1, 2, 2 y 3) para f-termodinamica, f-ondas-sonido y f-electricidad-campos.

Convenciones: todas las constantes se dan en el enunciado (g = 10 m/s², calor específico
del agua 4200 J/(kg·°C), R = 8.31 J/(mol·K), sonido en el aire a 340 m/s,
k = 9 × 10⁹ N·m²/C², π ≈ 3.14 cuando aparece en un resultado). Se aclaran los supuestos
(recipiente aislado, gas ideal, cables y fuente ideales, sin rozamiento del aire).
"""

from __future__ import annotations

EXERCISES: list[dict] = [
    # ==================== INTRODUCCIÓN A LA FÍSICA ====================
    {
        "id": "f-intro-fisica-1",
        "node": "f-intro-fisica",
        "kind": "problem",
        "level": 1,
        "title": "Leer la fórmula de la distancia de frenado",
        "statement": (
            "Un modelo simple para la distancia que recorre un auto desde que las ruedas empiezan a frenar hasta "
            "que se detiene es `d = v² / (2 · μ · g)`, donde `v` es la velocidad al empezar a frenar (en m/s), "
            "`μ` es un número sin unidades que mide el agarre entre la goma y el asfalto y `g = 10 m/s²`. El modelo "
            "deja de lado el tiempo de reacción del conductor y supone que el auto frena siempre con la misma "
            "intensidad. En asfalto seco, `μ = 0.8`; en asfalto mojado, `μ = 0.4`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué distancia de frenado predice el modelo para un auto que va a 72 km/h en asfalto seco? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 25, "tolerance": 0, "unit": "m"},
                "answer": "25 m",
            },
            {
                "prompt": "b) Si en el mismo asfalto seco el auto va a 108 km/h, ¿por qué número queda multiplicada la distancia de frenado respecto de la del inciso a)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2.25, "tolerance": 0, "unit": "×"},
                "answer": "2.25 (la distancia pasa de 25 m a 56.25 m)",
            },
            {
                "prompt": "c) ¿Qué distancia de frenado predice el modelo a 72 km/h en asfalto mojado? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 50, "tolerance": 0, "unit": "m"},
                "answer": "50 m",
            },
        ],
        "hints": [
            "La fórmula pide la velocidad en m/s: antes de reemplazar, pasá los km/h dividiendo por 3.6.",
            "Leé la fórmula como receta: la velocidad está elevada al cuadrado y `μ` está en el denominador. ¿Qué le pasa a `d` si `v` se multiplica por 1.5? ¿Y si `μ` se divide por 2?",
        ],
        "solution": [
            "Paso de unidades: `72 km/h ÷ 3.6 = 20 m/s` y `108 km/h ÷ 3.6 = 30 m/s`.",
            "a) Asfalto seco a 20 m/s: `d = 20² / (2 · 0.8 · 10) = 400 / 16 = 25 m`.",
            "b) La velocidad pasa de 20 m/s a 30 m/s, es decir, se multiplica por `30 / 20 = 1.5`. Como `d` es proporcional a `v²`, la distancia se multiplica por `1.5² = 2.25`.",
            "Comprobación con la fórmula: `d = 30² / 16 = 900 / 16 = 56.25 m`, y `56.25 / 25 = 2.25`. Ir un 50% más rápido no alarga la frenada un 50%, sino un 125%.",
            "c) En mojado `μ` vale la mitad, y como `μ` está dividiendo, la distancia se duplica: `d = 400 / (2 · 0.4 · 10) = 400 / 8 = 50 m`.",
            "Respuestas: 25 m, factor 2.25 y 50 m. El error típico en b) es responder 1.5, como si la distancia fuera proporcional a la velocidad y no a su cuadrado; en c) es olvidar que dividir por algo más chico da un resultado más grande.",
        ],
    },
    {
        "id": "f-intro-fisica-2",
        "node": "f-intro-fisica",
        "kind": "problem",
        "level": 2,
        "title": "¿Cuánto pesa el aire del aula?",
        "statement": (
            "Querés estimar la masa del aire que hay dentro de tu aula. Para eso la modelás como un prisma "
            "rectangular (una caja) de 8 m de largo, 6 m de ancho y 3 m de alto, y despreciás el volumen que ocupan "
            "los bancos y las personas. La densidad del aire a temperatura ambiente es de aproximadamente 1.2 g/L "
            "(1 m³ = 1000 L y 1 kg = 1000 g)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué volumen de aire hay en el aula según el modelo? Respondé solo con el número en m³.",
                "check": {"type": "numeric", "value": 144, "tolerance": 0, "unit": "m³"},
                "answer": "144 m³",
            },
            {
                "prompt": "b) ¿Qué masa tiene ese aire? Respondé solo con el número en kg.",
                "check": {"type": "numeric", "value": 172.8, "tolerance": 0, "unit": "kg"},
                "answer": "172.8 kg",
            },
            {
                "prompt": "c) ¿Con cuál de estos objetos tiene el mismo orden de magnitud la masa del aire del aula?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Con una mochila con útiles (del orden de 10 kg)",
                        "Con dos o tres personas adultas juntas (del orden de 10² kg)",
                        "Con un auto mediano (del orden de 10³ kg)",
                        "Con una lapicera (del orden de 10⁻² kg)",
                    ],
                    "correct": 1,
                },
                "answer": "Con dos o tres personas adultas juntas (del orden de 10² kg)",
            },
        ],
        "hints": [
            "El volumen de una caja es largo × ancho × alto.",
            "Antes de multiplicar, pasá la densidad a kg/m³: 1 m³ tiene 1000 L, así que en 1 m³ entran 1000 veces 1.2 g.",
            "Para el orden de magnitud escribí la masa en notación científica y fijate a qué potencia de 10 está más cerca.",
        ],
        "solution": [
            "Modelo: el aula es una caja de `8 m × 6 m × 3 m`, sin descontar muebles ni personas (ocupan una fracción chica del volumen).",
            "a) Volumen: `V = 8 · 6 · 3 = 144 m³`.",
            "Paso de unidades de la densidad: `1.2 g/L = 1.2 g × 1000 / m³ = 1200 g/m³ = 1.2 kg/m³`. En el aire, cada metro cúbico tiene algo más de un kilo de masa.",
            "b) Masa: `m = densidad · V = 1.2 kg/m³ · 144 m³ = 172.8 kg`.",
            "c) En notación científica, `172.8 kg ≈ 1.7 × 10² kg`: su orden de magnitud es `10² kg`, el mismo que el de dos o tres personas adultas (unos 70 kg cada una).",
            "Respuestas: 144 m³, 172.8 kg y orden de 10² kg. Sorprende porque el aire 'no se siente', pero el chequeo de sentido común lo confirma: la densidad del aire es unas 800 veces menor que la del agua, y 144 000 L de agua pesarían 144 toneladas. El error típico es no convertir g/L a kg/m³ y obtener 172.8 'algo' con la unidad equivocada.",
        ],
    },
    {
        "id": "f-intro-fisica-3",
        "node": "f-intro-fisica",
        "kind": "problem",
        "level": 3,
        "title": "De la maqueta a la estatua de bronce",
        "statement": (
            "Un escultor hace una maqueta de bronce macizo de 40 cm de alto para una estatua que va a medir 2 m de "
            "alto. La estatua es una copia exacta de la maqueta, del mismo bronce macizo, con todas las medidas "
            "agrandadas en la misma proporción. La maqueta tiene una masa de 6 kg, apoya sobre una base cuadrada de "
            "10 cm × 10 cm y para cubrirla con una capa de barniz se usaron 0.06 L (la estatua va a llevar una capa "
            "del mismo espesor). La presión que un objeto ejerce sobre su base es `p = peso / área de la base`, en "
            "pascales (1 Pa = 1 N/m²). Usá `g = 10 m/s²`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué masa va a tener la estatua? Respondé solo con el número en kg.",
                "check": {"type": "numeric", "value": 750, "tolerance": 0, "unit": "kg"},
                "answer": "750 kg",
            },
            {
                "prompt": "b) ¿Cuántos litros de barniz va a necesitar la estatua? Respondé solo con el número en L.",
                "check": {"type": "numeric", "value": 1.5, "tolerance": 0, "unit": "L"},
                "answer": "1.5 L",
            },
            {
                "prompt": "c) ¿Qué presión va a ejercer la estatua sobre su base? Respondé solo con el número en Pa.",
                "check": {"type": "numeric", "value": 30000, "tolerance": 0, "unit": "Pa"},
                "answer": "30000 Pa (cinco veces la de la maqueta, que es 6000 Pa)",
            },
        ],
        "hints": [
            "Calculá primero el factor de escala de las longitudes (cuántas veces más alta es la estatua). Pasá las dos alturas a la misma unidad.",
            "Si todas las longitudes se multiplican por un factor, las superficies se multiplican por ese factor al cuadrado y los volúmenes por ese factor al cubo. ¿La masa depende del volumen o de la superficie? ¿Y el barniz?",
            "Para la presión necesitás el peso de la estatua y el área de su base: las dos cambian con la escala, pero no con el mismo exponente.",
        ],
        "solution": [
            "Factor de escala de las longitudes: `2 m / 0.4 m = 5`. Todo largo de la estatua es 5 veces el de la maqueta; toda superficie es `5² = 25` veces mayor y todo volumen `5³ = 125` veces mayor.",
            "a) Con el mismo bronce macizo, la masa es proporcional al volumen: `m = 6 kg · 125 = 750 kg`.",
            "b) Con una capa del mismo espesor, el barniz es proporcional a la superficie: `0.06 L · 25 = 1.5 L`. La estatua pesa 125 veces más pero se barniza con solo 25 veces más producto.",
            "Presión de la maqueta: peso `6 · 10 = 60 N`, base `0.1 m · 0.1 m = 0.01 m²`, así que `p = 60 / 0.01 = 6000 Pa`.",
            "c) Estatua: peso `750 · 10 = 7500 N`; la base mide `50 cm × 50 cm`, es decir `0.5 · 0.5 = 0.25 m²`. Entonces `p = 7500 / 0.25 = 30000 Pa`.",
            "Verificación con proporciones: el peso crece ×125 y el área ×25, así que la presión crece `125 / 25 = 5` veces: `6000 · 5 = 30000 Pa`. Por esta misma ley del cuadrado y el cubo los animales grandes necesitan patas proporcionalmente más gruesas.",
            "Respuestas: 750 kg, 1.5 L y 30000 Pa. El error típico es multiplicar todo por 5 (daría 30 kg y 0.3 L) o creer que la presión no cambia porque 'es la misma forma'.",
        ],
    },
    # ==================== CINEMÁTICA (PANORAMA) ====================
    {
        "id": "f-cinematica-1",
        "node": "f-cinematica",
        "kind": "problem",
        "level": 1,
        "title": "La bolita que se cae de la mesa",
        "statement": (
            "Filmás una bolita que rueda sobre una mesa horizontal hasta caerse por el borde. Con el video armás la "
            "gráfica posición-tiempo de la bolita sobre la mesa y obtenés una recta que pasa por los puntos "
            "(t = 0; x = 0) y (t = 0.5 s; x = 1 m). La bolita sale del borde con esa misma velocidad horizontal, y la "
            "mesa tiene 0.8 m de altura. Despreciá el rozamiento del aire y usá `g = 10 m/s²`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Con qué velocidad rueda la bolita sobre la mesa? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "m/s"},
                "answer": "2 m/s",
            },
            {
                "prompt": "b) ¿Cuánto tarda en llegar al piso desde que deja el borde de la mesa? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 0.4, "tolerance": 0, "unit": "s"},
                "answer": "0.4 s",
            },
            {
                "prompt": "c) ¿A qué distancia horizontal del borde de la mesa toca el piso? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 0.8, "tolerance": 0, "unit": "m"},
                "answer": "0.8 m",
            },
        ],
        "hints": [
            "En una gráfica x-t que es una recta, la velocidad es la pendiente: cuánto cambia x dividido cuánto cambia t.",
            "Al dejar la mesa, la velocidad vertical inicial es cero: la caída vertical es una caída libre desde 0.8 m, independiente del avance horizontal.",
        ],
        "solution": [
            "a) Pendiente de la recta x-t: `v = Δx / Δt = (1 m − 0) / (0.5 s − 0) = 2 m/s`. Como es una recta, la velocidad es constante (MRU sobre la mesa).",
            "Al dejar el borde, la bolita tiene `vx = 2 m/s` y `vy = 0`. Los dos ejes se tratan por separado: en x sigue con MRU y en y cae con aceleración `g`.",
            "b) Caída vertical desde el reposo: `0.8 = ½ · 10 · t²`, entonces `t² = 0.16` y `t = 0.4 s`.",
            "c) Durante esos 0.4 s avanza horizontalmente a velocidad constante: `x = vx · t = 2 · 0.4 = 0.8 m`.",
            "Respuestas: 2 m/s, 0.4 s y 0.8 m. El error típico es pensar que la bolita 'cae más lento' porque viene rodando: el tiempo de caída es el mismo que si la soltaras desde el borde, porque solo depende de la altura.",
        ],
    },
    {
        "id": "f-cinematica-2",
        "node": "f-cinematica",
        "kind": "problem",
        "level": 2,
        "title": "El dron que suelta un paquete",
        "statement": (
            "Un dron despega del suelo y sube en línea vertical. Su gráfica velocidad-tiempo es así: entre t = 0 y "
            "t = 4 s es una recta que va de 0 a 10 m/s; entre t = 4 s y t = 6 s se mantiene horizontal en 10 m/s. "
            "Justo en t = 6 s el dron suelta un paquete. Despreciá el rozamiento del aire sobre el paquete y usá "
            "`g = 10 m/s²`. Tomá el eje y hacia arriba con origen en el suelo."
        ),
        "parts": [
            {
                "prompt": "a) ¿A qué altura está el dron en t = 6 s? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 40, "tolerance": 0, "unit": "m"},
                "answer": "40 m",
            },
            {
                "prompt": "b) ¿Cuál es la altura máxima, medida desde el suelo, que alcanza el paquete? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 45, "tolerance": 0, "unit": "m"},
                "answer": "45 m",
            },
            {
                "prompt": "c) ¿Cuánto tiempo pasa desde que el dron suelta el paquete hasta que este llega al suelo? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "s"},
                "answer": "4 s",
            },
        ],
        "hints": [
            "En una gráfica v-t, el área entre la curva y el eje del tiempo es el desplazamiento. Dividila en un triángulo y un rectángulo.",
            "En el instante en que lo suelta, el paquete tiene la misma velocidad que el dron: no parte del reposo.",
            "Planteá la posición del paquete `y(t) = y₀ + v₀·t − ½·g·t²` e igualala a cero.",
        ],
        "solution": [
            "a) Área bajo la gráfica v-t entre 0 y 6 s: triángulo `½ · 4 s · 10 m/s = 20 m` más rectángulo `2 s · 10 m/s = 20 m`. Altura del dron: `y₀ = 40 m`.",
            "Al soltarlo, el paquete sale con `v₀ = +10 m/s` (hacia arriba, la velocidad del dron) desde `y₀ = 40 m`, y desde ahí solo actúa la gravedad: es un tiro vertical hacia arriba.",
            "b) Sube hasta que su velocidad se anula: `0 = 10 − 10 · t` da `t = 1 s`, y en ese tiempo sube `10² / (2 · 10) = 5 m`. Altura máxima: `40 + 5 = 45 m`.",
            "c) Posición: `y(t) = 40 + 10·t − 5·t²`. Igualando a cero: `5t² − 10t − 40 = 0`, o sea `t² − 2t − 8 = 0`, que factoriza como `(t − 4)(t + 2) = 0`. La raíz con sentido físico es `t = 4 s`.",
            "Verificación: `y(4) = 40 + 40 − 80 = 0` ✓, y llega con `v = 10 − 10 · 4 = −30 m/s` (30 m/s hacia abajo).",
            "Respuestas: 40 m, 45 m y 4 s. El error típico es suponer que el paquete parte del reposo: daría altura máxima 40 m y un tiempo de caída de √8 ≈ 2.83 s.",
        ],
    },
    {
        "id": "f-cinematica-3",
        "node": "f-cinematica",
        "kind": "problem",
        "level": 3,
        "title": "Reconstruir un tiro desde la terraza con dos gráficas",
        "statement": (
            "Desde el borde de una terraza se lanza una pelota y un programa de análisis de video entrega dos "
            "gráficas, desde el lanzamiento (t = 0) hasta que la pelota toca el suelo (t = 4 s). La gráfica de la "
            "posición horizontal en función del tiempo es una recta que pasa por (0; 0) y (4 s; 64 m). La gráfica de "
            "la velocidad vertical en función del tiempo es una recta que pasa por (0; 10 m/s) y (4 s; −30 m/s), con "
            "el eje y positivo hacia arriba. El suelo es horizontal y se desprecia el rozamiento del aire."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué altura tiene la terraza? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 40, "tolerance": 0, "unit": "m"},
                "answer": "40 m",
            },
            {
                "prompt": "b) ¿Cuál es la altura máxima de la pelota, medida desde el suelo? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 45, "tolerance": 0, "unit": "m"},
                "answer": "45 m",
            },
            {
                "prompt": "c) ¿Con qué rapidez (módulo de la velocidad) llega la pelota al suelo? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 34, "tolerance": 0, "unit": "m/s"},
                "answer": "34 m/s",
            },
        ],
        "hints": [
            "El área bajo la gráfica vy-t es el desplazamiento vertical, con signo: lo que queda por debajo del eje cuenta como negativo. Buscá primero en qué instante la recta corta el eje del tiempo.",
            "La altura máxima corresponde al instante en que vy = 0; el área del triángulo de arriba te dice cuánto sube por encima de la terraza.",
            "La velocidad horizontal sale de la pendiente de la otra gráfica y no cambia. Al llegar al suelo, combiná vx con la vy final usando Pitágoras.",
        ],
        "solution": [
            "Pendiente de la gráfica vy-t: `(−30 − 10) / 4 = −10 m/s²`, que es `−g`: el dato es coherente con un tiro sin rozamiento. La recta corta el eje en `vy = 10 − 10t = 0`, o sea `t = 1 s`.",
            "Área con signo: triángulo de arriba entre 0 y 1 s, `½ · 1 · 10 = +5 m`; triángulo de abajo entre 1 s y 4 s, `½ · 3 · (−30) = −45 m`. Desplazamiento vertical total: `5 − 45 = −40 m`.",
            "a) La pelota termina 40 m por debajo del punto de lanzamiento y ahí está el suelo: la terraza mide `40 m`.",
            "b) En t = 1 s la pelota está 5 m por encima de la terraza: altura máxima `40 + 5 = 45 m`.",
            "Pendiente de la gráfica x-t: `vx = 64 / 4 = 16 m/s`, constante durante todo el vuelo.",
            "c) Al tocar el suelo, `vx = 16 m/s` y `vy = −30 m/s`. Rapidez: `√(16² + 30²) = √(256 + 900) = √1156 = 34 m/s`.",
            "Respuestas: 40 m, 45 m y 34 m/s. Errores típicos: sumar las áreas sin signo (daría 50 m de terraza) o responder en c) solo 30 m/s, olvidando que la componente horizontal sigue presente al llegar al suelo.",
        ],
    },
    # ==================== TERMODINÁMICA ====================
    {
        "id": "f-termodinamica-1",
        "node": "f-termodinamica",
        "kind": "problem",
        "level": 1,
        "title": "Templar el agua del termo para el mate",
        "statement": (
            "En un termo ponés 600 g de agua recién calentada a 90 °C y le agregás 300 g de agua de la canilla a "
            "15 °C. Suponé que el termo es un recipiente aislado y que no absorbe calor (solo intercambian calor las "
            "dos porciones de agua). Calor específico del agua: `c = 4200 J/(kg·°C)`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la temperatura de equilibrio de la mezcla? Respondé solo con el número en °C.",
                "check": {"type": "numeric", "value": 65, "tolerance": 0, "unit": "°C"},
                "answer": "65 °C",
            },
            {
                "prompt": "b) ¿Cuánto calor cede el agua caliente hasta llegar al equilibrio? Respondé solo con el número en kJ.",
                "check": {"type": "numeric", "value": 63, "tolerance": 0, "unit": "kJ"},
                "answer": "63 kJ",
            },
        ],
        "hints": [
            "En un recipiente aislado, todo el calor que cede el agua caliente lo absorbe el agua fría: `Q_cedido = Q_absorbido`.",
            "Escribí cada calor como `m · c · ΔT`, con la temperatura final `T` como incógnita, y despejala.",
        ],
        "solution": [
            "Pasá las masas a kg: `0.6 kg` de agua caliente y `0.3 kg` de agua fría. Llamá `T` a la temperatura final común.",
            "Calor cedido por el agua caliente: `0.6 · 4200 · (90 − T)`. Calor absorbido por la fría: `0.3 · 4200 · (T − 15)`.",
            "a) Igualando (el 4200 se cancela): `0.6 · (90 − T) = 0.3 · (T − 15)`, o sea `54 − 0.6T = 0.3T − 4.5`. Entonces `58.5 = 0.9T` y `T = 65 °C`.",
            "b) Calor cedido: `Q = 0.6 · 4200 · (90 − 65) = 0.6 · 4200 · 25 = 63000 J = 63 kJ`.",
            "Verificación: el agua fría absorbe `0.3 · 4200 · (65 − 15) = 63000 J`, lo mismo. Además 65 °C está entre 15 °C y 90 °C y más cerca de 90 °C, porque hay el doble de agua caliente.",
            "Respuestas: 65 °C y 63 kJ. El error típico es promediar las temperaturas sin pesar las masas: `(90 + 15) / 2 = 52.5 °C` solo valdría con masas iguales.",
        ],
    },
    {
        "id": "f-termodinamica-2",
        "node": "f-termodinamica",
        "kind": "problem",
        "level": 2,
        "title": "Un gas que se calienta trabado y después se expande",
        "statement": (
            "Un cilindro con un émbolo contiene 4 mol de un gas ideal que ocupan 83.1 L a 27 °C. Primero el émbolo "
            "está trabado y se calienta el gas hasta 127 °C. Después se destraba el émbolo y el gas se expande "
            "lentamente manteniendo su temperatura en 127 °C hasta que la presión vuelve a valer lo mismo que al "
            "principio. No entra ni sale gas. Usá `R = 8.31 J/(mol·K)`, `T(K) = T(°C) + 273` y `1 L = 0.001 m³`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la presión inicial del gas? Respondé solo con el número en kPa.",
                "check": {"type": "numeric", "value": 120, "tolerance": 0, "unit": "kPa"},
                "answer": "120 kPa",
            },
            {
                "prompt": "b) ¿Cuál es la presión al terminar el calentamiento con el émbolo trabado? Respondé solo con el número en kPa.",
                "check": {"type": "numeric", "value": 160, "tolerance": 0, "unit": "kPa"},
                "answer": "160 kPa",
            },
            {
                "prompt": "c) ¿Qué volumen ocupa el gas al final de la expansión? Respondé solo con el número en L.",
                "check": {"type": "numeric", "value": 110.8, "tolerance": 0, "unit": "L"},
                "answer": "110.8 L",
            },
        ],
        "hints": [
            "En `P · V = n · R · T` la temperatura va en kelvin y el volumen en m³; así la presión sale en Pa.",
            "Con el émbolo trabado el volumen no cambia: `P` es proporcional a `T` (en kelvin).",
            "En la expansión a temperatura constante, `P · V` se mantiene constante.",
        ],
        "solution": [
            "Unidades: `T₁ = 27 + 273 = 300 K`, `T₂ = 127 + 273 = 400 K` y `V₁ = 83.1 L = 0.0831 m³`.",
            "a) `P₁ = n · R · T₁ / V₁ = 4 · 8.31 · 300 / 0.0831 = 9972 / 0.0831 = 120000 Pa = 120 kPa`.",
            "b) Calentamiento a volumen constante: `P₂ / T₂ = P₁ / T₁`, entonces `P₂ = 120 · 400 / 300 = 160 kPa`. (Con la ecuación de estado: `4 · 8.31 · 400 / 0.0831 = 160000 Pa` ✓.)",
            "c) Expansión a temperatura constante (400 K) hasta `P₃ = 120 kPa`: `P₂ · V₂ = P₃ · V₃`, así que `V₃ = 160 · 83.1 / 120 = 13296 / 120 = 110.8 L`.",
            "Verificación con la ecuación de estado: `n · R · T / P₃ = 4 · 8.31 · 400 / 120000 = 0.1108 m³ = 110.8 L` ✓. Otra forma de verlo: como la presión final es igual a la inicial, `V₃ / V₁ = T₂ / T₁ = 4/3`.",
            "Respuestas: 120 kPa, 160 kPa y 110.8 L. El error típico es usar grados Celsius en la proporción: `127 / 27 ≈ 4.7` haría creer que la presión casi se quintuplica, cuando en realidad solo crece un tercio.",
        ],
    },
    {
        "id": "f-termodinamica-3",
        "node": "f-termodinamica",
        "kind": "problem",
        "level": 2,
        "title": "Primera ley en una expansión a presión constante",
        "statement": (
            "Un gas ideal monoatómico está encerrado en un cilindro con un émbolo que se desliza sin rozamiento y "
            "mantiene la presión constante en 200 kPa. Inicialmente el gas ocupa 10 L a 27 °C. Se le entregan "
            "2500 J de calor y el gas se expande lentamente hasta ocupar 15 L. Usá la primera ley en la forma "
            "`ΔU = Q − W`, donde `W` es el trabajo que hace el gas, `T(K) = T(°C) + 273` y `1 L = 0.001 m³`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto trabajo hace el gas sobre el émbolo? Respondé solo con el número en J.",
                "check": {"type": "numeric", "value": 1000, "tolerance": 0, "unit": "J"},
                "answer": "1000 J",
            },
            {
                "prompt": "b) ¿Cuánto varía la energía interna del gas? Respondé solo con el número en J.",
                "check": {"type": "numeric", "value": 1500, "tolerance": 0, "unit": "J"},
                "answer": "1500 J (aumenta)",
            },
            {
                "prompt": "c) ¿Cuál es la temperatura final del gas? Respondé solo con el número en °C.",
                "check": {"type": "numeric", "value": 177, "tolerance": 0, "unit": "°C"},
                "answer": "177 °C (450 K)",
            },
        ],
        "hints": [
            "A presión constante, el trabajo del gas es `W = P · ΔV`. Pasá la presión a Pa y el volumen a m³.",
            "El calor que entra se reparte: una parte sale como trabajo y el resto queda como energía interna.",
            "A presión constante y con la misma cantidad de gas, `V / T` se mantiene constante (con T en kelvin).",
        ],
        "solution": [
            "Unidades: `P = 200 kPa = 200000 Pa`, `ΔV = 15 L − 10 L = 5 L = 0.005 m³` y `T₁ = 27 + 273 = 300 K`.",
            "a) `W = P · ΔV = 200000 · 0.005 = 1000 J`. Es positivo porque el gas se expande y empuja el émbolo.",
            "b) Primera ley: `ΔU = Q − W = 2500 − 1000 = 1500 J`. La energía interna aumenta, lo que es coherente con que el gas se calienta.",
            "c) A presión constante: `V₁ / T₁ = V₂ / T₂`, entonces `T₂ = 300 · 15 / 10 = 450 K`, y en Celsius `450 − 273 = 177 °C`.",
            "Verificación (para gas monoatómico): `ΔU = 3/2 · n·R·ΔT = 3/2 · P·ΔV = 1.5 · 1000 = 1500 J` ✓, y `Q = 5/2 · P·ΔV = 2500 J` ✓, el dato del enunciado.",
            "Respuestas: 1000 J, 1500 J y 177 °C. Errores típicos: olvidar pasar los litros a m³ (daría W = 1 000 000 J) y hacer la proporción `V/T` con grados Celsius (daría 40.5 °C).",
        ],
    },
    {
        "id": "f-termodinamica-4",
        "node": "f-termodinamica",
        "kind": "problem",
        "level": 3,
        "title": "Calorímetro con hielo que no termina de derretirse",
        "statement": (
            "En un calorímetro ideal (aislado y de capacidad calorífica despreciable) hay 400 g de agua a 20 °C. Se "
            "agregan 200 g de hielo a −10 °C y se espera a que se alcance el equilibrio térmico. Datos: calor "
            "específico del agua `4200 J/(kg·°C)`, calor específico del hielo `2100 J/(kg·°C)`, calor latente de "
            "fusión del hielo `L_f = 336000 J/kg`. El hielo se funde a 0 °C."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la temperatura final de equilibrio? Respondé solo con el número en °C.",
                "check": {"type": "numeric", "value": 0, "tolerance": 0, "unit": "°C"},
                "answer": "0 °C",
            },
            {
                "prompt": "b) ¿Qué masa de hielo queda sin derretir en el equilibrio? Respondé solo con el número en g.",
                "check": {"type": "numeric", "value": 112.5, "tolerance": 0, "unit": "g"},
                "answer": "112.5 g",
            },
            {
                "prompt": "c) ¿Qué masa mínima de agua a 20 °C debería haber habido en el calorímetro (en lugar de los 400 g) para que se derritiera todo el hielo? Respondé solo con el número en g.",
                "check": {"type": "numeric", "value": 850, "tolerance": 0, "unit": "g"},
                "answer": "850 g",
            },
        ],
        "hints": [
            "No plantees directamente `Q_cedido = Q_absorbido` con una temperatura final desconocida: primero hacé un balance de energía. ¿Cuánto calor puede ceder el agua si baja hasta 0 °C? ¿Cuánto hace falta para llevar el hielo a 0 °C y derretirlo entero?",
            "Si el calor disponible alcanza para calentar el hielo hasta 0 °C pero no para fundirlo todo, el sistema queda a 0 °C con hielo y agua juntos.",
            "Para c), la condición límite es que el agua ceda exactamente lo necesario para calentar y fundir todo el hielo, terminando todo a 0 °C.",
        ],
        "solution": [
            "Calor máximo que puede ceder el agua bajando de 20 °C a 0 °C: `0.4 · 4200 · 20 = 33600 J`.",
            "Calor para llevar el hielo de −10 °C a 0 °C: `0.2 · 2100 · 10 = 4200 J`. Calor para fundirlo entero: `0.2 · 336000 = 67200 J`. Total necesario para derretirlo todo: `71400 J`.",
            "a) Como `33600 J` alcanza para llevar el hielo a 0 °C (4200 J) pero no para fundirlo entero, el equilibrio queda a `0 °C` con hielo y agua. (Si el agua bajara de 0 °C se congelaría, y el hielo no puede pasar de 0 °C sin derretirse antes.)",
            "Calor que sobra para fundir: `33600 − 4200 = 29400 J`. Masa fundida: `29400 / 336000 = 0.0875 kg = 87.5 g`.",
            "b) Hielo que queda: `200 − 87.5 = 112.5 g`. En el calorímetro quedan `400 + 87.5 = 487.5 g` de agua y 112.5 g de hielo, todo a 0 °C.",
            "c) Condición límite: `m · 4200 · 20 = 71400`, entonces `m = 71400 / 84000 = 0.85 kg = 850 g`. Con más agua, todo el hielo se funde y la temperatura final queda por encima de 0 °C.",
            "Respuestas: 0 °C, 112.5 g y 850 g. El error típico es plantear la mezcla como si todo terminara líquido y despejar T: da una temperatura negativa, que es imposible con agua líquida en equilibrio, y es la señal de que el hielo no termina de fundirse.",
        ],
    },
    # ==================== ONDAS Y SONIDO ====================
    {
        "id": "f-ondas-sonido-1",
        "node": "f-ondas-sonido",
        "kind": "problem",
        "level": 1,
        "title": "La ecosonda de un pesquero",
        "statement": (
            "Un barco pesquero que sale de Mar del Plata usa una ecosonda: emite hacia abajo un pulso de sonido de "
            "50 kHz y registra el eco que rebota en el fondo 0.08 s después de emitirlo. En el agua de mar el sonido "
            "viaja a 1500 m/s; en el aire, a 340 m/s."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué profundidad tiene el mar en ese lugar? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": "m"},
                "answer": "60 m",
            },
            {
                "prompt": "b) ¿Cuál es la longitud de onda del pulso en el agua? Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": "cm"},
                "answer": "3 cm",
            },
            {
                "prompt": "c) Si la ecosonda emitiera la misma señal en el aire, ¿cuál sería su longitud de onda? Respondé solo con el número en mm.",
                "check": {"type": "numeric", "value": 6.8, "tolerance": 0, "unit": "mm"},
                "answer": "6.8 mm",
            },
        ],
        "hints": [
            "El tiempo del eco corresponde a un viaje de ida y vuelta.",
            "Usá `v = f · λ` con la frecuencia en Hz (1 kHz = 1000 Hz). Al cambiar de medio, la frecuencia la fija la fuente y no cambia: lo que cambia es la velocidad.",
        ],
        "solution": [
            "a) En 0.08 s el sonido recorre `1500 · 0.08 = 120 m`, que es ida y vuelta. La profundidad es la mitad: `120 / 2 = 60 m`.",
            "b) `λ = v / f = 1500 / 50000 = 0.03 m = 3 cm`.",
            "c) En el aire la frecuencia sigue siendo 50 kHz (la impone la fuente), pero la velocidad es 340 m/s: `λ = 340 / 50000 = 0.0068 m = 6.8 mm`.",
            "Respuestas: 60 m, 3 cm y 6.8 mm. Errores típicos: no dividir por 2 el recorrido del eco (daría 120 m de profundidad) y olvidar pasar los kHz a Hz (daría λ mil veces mayor). Además, 50 kHz es ultrasonido: los humanos oímos hasta unos 20 kHz.",
        ],
    },
    {
        "id": "f-ondas-sonido-2",
        "node": "f-ondas-sonido",
        "kind": "problem",
        "level": 2,
        "title": "La quinta cuerda de la guitarra: trastes y armónicos",
        "statement": (
            "En una guitarra criolla la parte vibrante de cada cuerda al aire mide 65 cm (de la cejuela al puente), y "
            "la quinta cuerda está afinada en La2 = 110 Hz como frecuencia fundamental. Una cuerda fija en sus dos "
            "extremos vibra con longitudes de onda `λₙ = 2L / n` (n = 1, 2, 3, …), y todas sus frecuencias "
            "comparten la misma velocidad de onda en la cuerda. Pisar un traste no cambia la tensión de la cuerda "
            "(por lo tanto tampoco la velocidad de la onda), solo acorta la parte que vibra."
        ),
        "parts": [
            {
                "prompt": "a) ¿A qué velocidad viajan las ondas por esa cuerda? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 143, "tolerance": 0, "unit": "m/s"},
                "answer": "143 m/s",
            },
            {
                "prompt": "b) Al pisar un traste, la parte vibrante de la quinta cuerda queda de 52 cm. ¿Qué frecuencia fundamental suena? Respondé solo con el número en Hz.",
                "check": {"type": "numeric", "value": 137.5, "tolerance": 0, "unit": "Hz"},
                "answer": "137.5 Hz",
            },
            {
                "prompt": "c) Con la cuerda al aire, apoyás el dedo suavemente (sin apretarla contra el diapasón) a 16.25 cm de la cejuela, casi sobre el traste 5, y la pulsás. Ese punto queda obligado a ser un nodo. ¿Cuál es la frecuencia más baja que puede sonar? Respondé solo con el número en Hz.",
                "check": {"type": "numeric", "value": 440, "tolerance": 0, "unit": "Hz"},
                "answer": "440 Hz",
            },
        ],
        "hints": [
            "Para la fundamental, `λ₁ = 2L`. Con `v = f · λ` sale la velocidad.",
            "Si la velocidad no cambia y la cuerda se acorta, la nueva fundamental sale de `f = v / (2L')`.",
            "16.25 cm es una fracción exacta de 65 cm. ¿Qué modos de vibración tienen un nodo justo ahí? Pensá en cuántos 'husos' entran en la cuerda.",
        ],
        "solution": [
            "a) Fundamental de la cuerda al aire: `λ₁ = 2 · 0.65 = 1.3 m`, entonces `v = f · λ = 110 · 1.3 = 143 m/s`.",
            "b) Con `L' = 0.52 m`: `f = v / (2L') = 143 / 1.04 = 137.5 Hz`. También por proporción: `110 · 65 / 52 = 137.5 Hz` (la frecuencia es inversamente proporcional al largo).",
            "c) `16.25 / 65 = 1/4`: el dedo impone un nodo a un cuarto de la cuerda. En el modo n, los nodos están en las posiciones `k · L / n` (k = 0, 1, …, n), así que hace falta que `1/4` sea de la forma `k/n`: n tiene que ser múltiplo de 4.",
            "El modo más bajo permitido es `n = 4`: `f₄ = 4 · 110 = 440 Hz`, el La4 que se usa como nota de afinación (dos octavas arriba de la cuerda al aire).",
            "Respuestas: 143 m/s, 137.5 Hz y 440 Hz. Errores típicos: usar `λ = L` en vez de `2L` (daría 71.5 m/s) y en c) creer que suena la fundamental de un pedazo de cuerda de 16.25 cm o de 48.75 cm, como si el dedo pisara un traste: al apoyarlo suavemente vibra la cuerda entera.",
        ],
    },
    {
        "id": "f-ondas-sonido-3",
        "node": "f-ondas-sonido",
        "kind": "problem",
        "level": 2,
        "title": "Un resorte y un péndulo que marcan el mismo ritmo",
        "statement": (
            "Sobre una mesa horizontal sin rozamiento, un bloque de 0.5 kg está unido a un resorte de constante "
            "`k = 200 N/m` cuyo otro extremo está fijo a la pared. Se aparta el bloque 5 cm de su posición de "
            "equilibrio y se lo suelta desde el reposo, de modo que oscila con movimiento armónico simple. Para un "
            "resorte el período es `T = 2π√(m/k)` y para un péndulo simple, `T = 2π√(L/g)`. Usá `π ≈ 3.14` y "
            "`g = 10 m/s²`."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el período de oscilación del bloque? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 0.314, "tolerance": 0.01, "unit": "s"},
                "answer": "0.314 s",
            },
            {
                "prompt": "b) ¿Cuál es la rapidez máxima del bloque? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": "m/s"},
                "answer": "1 m/s",
            },
            {
                "prompt": "c) ¿Qué largo debería tener un péndulo simple para oscilar con el mismo período que el bloque? Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 2.5, "tolerance": 0, "unit": "cm"},
                "answer": "2.5 cm",
            },
        ],
        "hints": [
            "Para el período, reemplazá en `T = 2π√(m/k)`: la raíz da un número exacto.",
            "La rapidez es máxima al pasar por el equilibrio. Ahí toda la energía elástica inicial `½·k·A²` se transformó en cinética.",
            "Igualá los dos períodos: el `2π` se cancela y queda `m/k = L/g`.",
        ],
        "solution": [
            "a) `√(m/k) = √(0.5 / 200) = √0.0025 = 0.05 s`, entonces `T = 2π · 0.05 = 0.1π ≈ 0.314 s` (un poco más de 3 oscilaciones por segundo).",
            "Energía elástica al soltarlo, con `A = 0.05 m`: `E = ½ · 200 · 0.05² = 0.25 J`. Sin rozamiento, se conserva durante toda la oscilación.",
            "b) En el equilibrio el resorte no está estirado y toda la energía es cinética: `½ · 0.5 · v² = 0.25`, entonces `v² = 1` y `v = 1 m/s`.",
            "c) Mismo período: `2π√(m/k) = 2π√(L/g)`, o sea `L = g · m / k = 10 · 0.5 / 200 = 0.025 m = 2.5 cm`. Comprobación: `2 · 3.14 · √(0.025 / 10) = 6.28 · 0.05 = 0.314 s` ✓.",
            "Respuestas: 0.314 s, 1 m/s y 2.5 cm. Dato curioso: 2.5 cm es justo lo que se estiraría ese resorte si colgaras el bloque verticalmente (`m·g/k`). El período no depende de la amplitud: si lo soltaras desde 10 cm, el período seguiría siendo 0.314 s y solo se duplicaría la rapidez máxima.",
        ],
    },
    {
        "id": "f-ondas-sonido-4",
        "node": "f-ondas-sonido",
        "kind": "problem",
        "level": 3,
        "title": "Efecto Doppler: deducir la velocidad de la ambulancia",
        "statement": (
            "Estás parado en la vereda de una avenida y pasa una ambulancia con la sirena encendida, a velocidad "
            "constante y en línea recta. Mientras se acerca escuchás un tono de 765 Hz y, después de que pasa, "
            "mientras se aleja, uno de 680 Hz. No conocés ni la frecuencia que emite la sirena ni la velocidad de la "
            "ambulancia. El sonido viaja a `v = 340 m/s` en el aire quieto. Para una fuente que se mueve a `v_f` y un "
            "oyente que se mueve a `v_o`, la frecuencia percibida es `f' = f · (v ± v_o) / (v ∓ v_f)`: en el "
            "numerador va `+` si el oyente se mueve hacia la fuente, y en el denominador va `−` si la fuente se "
            "mueve hacia el oyente (signos contrarios si se alejan)."
        ),
        "parts": [
            {
                "prompt": "a) ¿A qué velocidad va la ambulancia? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "m/s"},
                "answer": "20 m/s (72 km/h)",
            },
            {
                "prompt": "b) ¿Qué frecuencia emite realmente la sirena? Respondé solo con el número en Hz.",
                "check": {"type": "numeric", "value": 720, "tolerance": 0, "unit": "Hz"},
                "answer": "720 Hz",
            },
            {
                "prompt": "c) Si en lugar de estar parado fueras en un auto a 10 m/s hacia la ambulancia (que se acerca a 20 m/s), ¿qué frecuencia escucharías? Respondé solo con el número en Hz.",
                "check": {"type": "numeric", "value": 787.5, "tolerance": 0, "unit": "Hz"},
                "answer": "787.5 Hz",
            },
        ],
        "hints": [
            "Escribí dos ecuaciones con las dos incógnitas `f` y `v_f`: una para cuando se acerca (oyente quieto, denominador `340 − v_f`) y otra para cuando se aleja (denominador `340 + v_f`).",
            "Dividí una ecuación por la otra: `f` y el 340 del numerador se cancelan y queda una ecuación de primer grado en `v_f`.",
            "En c) se mueven los dos: el oyente se acerca (numerador `340 + 10`) y la fuente también (denominador `340 − 20`).",
        ],
        "solution": [
            "Oyente quieto: acercándose, `765 = f · 340 / (340 − v_f)`; alejándose, `680 = f · 340 / (340 + v_f)`.",
            "Dividiendo la primera por la segunda: `765 / 680 = (340 + v_f) / (340 − v_f)`. Como `765 / 680 = 9/8`: `8 · (340 + v_f) = 9 · (340 − v_f)`.",
            "a) `2720 + 8v_f = 3060 − 9v_f`, entonces `17v_f = 340` y `v_f = 20 m/s` (72 km/h).",
            "b) De la primera ecuación: `f = 765 · (340 − 20) / 340 = 765 · 320 / 340 = 720 Hz`. Verificación con la otra: `720 · 340 / 360 = 680 Hz` ✓.",
            "c) Oyente hacia la fuente a 10 m/s y fuente hacia el oyente a 20 m/s: `f' = 720 · (340 + 10) / (340 − 20) = 720 · 350 / 320 = 787.5 Hz`.",
            "Respuestas: 20 m/s, 720 Hz y 787.5 Hz. Errores típicos: suponer que la frecuencia real es el promedio de las dos que oís (`(765 + 680) / 2 = 722.5 Hz`, que no es 720 Hz porque el efecto no es simétrico) y equivocar los signos: acercarse siempre sube la frecuencia percibida y alejarse la baja.",
        ],
    },
    # ==================== ELECTRICIDAD Y CAMPOS ====================
    {
        "id": "f-electricidad-campos-1",
        "node": "f-electricidad-campos",
        "kind": "problem",
        "level": 1,
        "title": "Lo que cuesta la estufa eléctrica en un mes",
        "statement": (
            "Una estufa eléctrica de cuarzo tiene en la etiqueta '1100 W – 220 V' y está enchufada a la red de tu "
            "casa (220 V). En invierno la usás 4 horas por día durante 30 días. La distribuidora cobra el kWh "
            "a $ 125 (sin impuestos ni cargos fijos). Suponé que la estufa funciona siempre a su potencia nominal."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué corriente circula por la estufa mientras funciona? Respondé solo con el número en A.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "A"},
                "answer": "5 A",
            },
            {
                "prompt": "b) ¿Cuánta energía consume en el mes? Respondé solo con el número en kWh.",
                "check": {"type": "numeric", "value": 132, "tolerance": 0, "unit": "kWh"},
                "answer": "132 kWh",
            },
            {
                "prompt": "c) ¿Cuánto cuesta esa energía? Respondé solo con el número en pesos.",
                "check": {"type": "numeric", "value": 16500, "tolerance": 0, "unit": "$"},
                "answer": "16500 pesos",
            },
        ],
        "hints": [
            "De `P = V · I` despejá la corriente.",
            "El kWh es una unidad de energía: potencia en kW por tiempo en horas. Pasá los 1100 W a kW y calculá las horas totales del mes.",
        ],
        "solution": [
            "a) `I = P / V = 1100 W / 220 V = 5 A`. (La resistencia del filamento caliente es `R = V / I = 220 / 5 = 44 Ω`.)",
            "Tiempo de uso en el mes: `4 h/día · 30 días = 120 h`. Potencia en kW: `1100 W = 1.1 kW`.",
            "b) `E = P · t = 1.1 kW · 120 h = 132 kWh`.",
            "c) `Costo = 132 kWh · $ 125/kWh = $ 16500`.",
            "Respuestas: 5 A, 132 kWh y 16500 pesos. Chequeo de unidades: 1 kWh = 1000 W · 3600 s = 3 600 000 J, así que el mes equivale a unos 475 millones de joules. El error típico es multiplicar 1100 W por 120 h y obtener 132000 'kWh': sin pasar a kW, el resultado está en Wh.",
        ],
    },
    {
        "id": "f-electricidad-campos-2",
        "node": "f-electricidad-campos",
        "kind": "problem",
        "level": 2,
        "title": "Tres cargas en línea",
        "statement": (
            "Tres cargas puntuales están fijas sobre el eje x: `q₁ = +2 μC` en x = 0, `q₂ = +1 μC` en x = 10 cm y "
            "`q₃ = −4 μC` en x = 30 cm. Usá `k = 9 × 10⁹ N·m²/C²` y `1 μC = 10⁻⁶ C`. Tomá el sentido positivo del "
            "eje x hacia la derecha (de q₁ hacia q₃)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el módulo de la fuerza eléctrica neta sobre q₂? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 2.7, "tolerance": 0, "unit": "N"},
                "answer": "2.7 N (hacia +x, hacia q₃)",
            },
            {
                "prompt": "b) ¿Cuál es el módulo de la fuerza eléctrica neta sobre q₃? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 1.7, "tolerance": 0, "unit": "N"},
                "answer": "1.7 N (hacia −x)",
            },
            {
                "prompt": "c) ¿Cuál es el módulo de la fuerza eléctrica neta sobre q₁? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": "N"},
                "answer": "1 N (hacia −x)",
            },
        ],
        "hints": [
            "Calculá cada fuerza por separado con `F = k · |q₁| · |q₂| / r²` (distancias en metros) y decidí su sentido por separado: iguales se repelen, opuestas se atraen.",
            "Sumá las fuerzas con signo según el eje x: dos fuerzas en el mismo sentido se suman y en sentidos opuestos se restan.",
            "Para controlar: por acción y reacción, las tres fuerzas netas (con signo) tienen que sumar cero.",
        ],
        "solution": [
            "Distancias: q₁–q₂ = 0.1 m, q₂–q₃ = 0.2 m y q₁–q₃ = 0.3 m. Módulos de las fuerzas entre pares: `F₁₂ = 9×10⁹ · 2×10⁻⁶ · 1×10⁻⁶ / 0.01 = 1.8 N`; `F₂₃ = 9×10⁹ · 1×10⁻⁶ · 4×10⁻⁶ / 0.04 = 0.9 N`; `F₁₃ = 9×10⁹ · 2×10⁻⁶ · 4×10⁻⁶ / 0.09 = 0.8 N`.",
            "a) Sobre q₂: q₁ la repele (las dos positivas) hacia +x con 1.8 N; q₃ la atrae (signos opuestos) hacia q₃, también hacia +x, con 0.9 N. Neta: `1.8 + 0.9 = 2.7 N` hacia +x.",
            "b) Sobre q₃: q₁ la atrae hacia −x con 0.8 N y q₂ la atrae hacia −x con 0.9 N. Neta: `0.8 + 0.9 = 1.7 N` hacia −x.",
            "c) Sobre q₁: q₂ la repele hacia −x con 1.8 N y q₃ la atrae hacia +x con 0.8 N. Neta: `−1.8 + 0.8 = −1 N`, es decir, 1 N hacia −x.",
            "Verificación con acción y reacción: `(+2.7) + (−1.7) + (−1) = 0` ✓. Las fuerzas internas de un sistema siempre suman cero.",
            "Respuestas: 2.7 N, 1.7 N y 1 N. El error típico es olvidar pasar los cm a m (los resultados darían 10 000 veces más grandes) o restar en a) porque 'q₃ es negativa', cuando en realidad la atracción de q₃ y la repulsión de q₁ empujan a q₂ hacia el mismo lado.",
        ],
    },
    {
        "id": "f-electricidad-campos-3",
        "node": "f-electricidad-campos",
        "kind": "problem",
        "level": 2,
        "title": "Un circuito mixto con una batería de 12 V",
        "statement": (
            "Una batería ideal de 12 V alimenta un circuito con tres resistencias: `R₁ = 2 Ω` está en serie con un "
            "paralelo formado por `R₂ = 6 Ω` y `R₃ = 3 Ω`. Los cables son ideales (resistencia nula)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la resistencia equivalente de todo el circuito? Respondé solo con el número en Ω.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "Ω"},
                "answer": "4 Ω",
            },
            {
                "prompt": "b) ¿Qué corriente circula por R₂? Respondé solo con el número en A.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": "A"},
                "answer": "1 A",
            },
            {
                "prompt": "c) ¿Qué potencia disipa R₃? Respondé solo con el número en W.",
                "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": "W"},
                "answer": "12 W",
            },
        ],
        "hints": [
            "Primero reducí el paralelo a una sola resistencia (`1/R = 1/R₂ + 1/R₃`) y después sumala en serie con R₁.",
            "Con la corriente total, calculá cuánto voltaje cae en R₁; el resto queda aplicado a las dos ramas del paralelo por igual.",
            "La potencia en una resistencia es `P = I² · R` o `P = V² / R`.",
        ],
        "solution": [
            "Paralelo: `1/R_p = 1/6 + 1/3 = 1/6 + 2/6 = 3/6`, así que `R_p = 2 Ω`. a) En serie con R₁: `R_eq = 2 + 2 = 4 Ω`.",
            "Corriente total (la que pasa por la batería y por R₁): `I = V / R_eq = 12 / 4 = 3 A`.",
            "Caída en R₁: `V₁ = 3 · 2 = 6 V`. Queda para el paralelo: `12 − 6 = 6 V` (también `3 A · 2 Ω = 6 V`).",
            "b) `I₂ = 6 V / 6 Ω = 1 A`, y por R₃ pasa `I₃ = 6 / 3 = 2 A`. Verificación: `1 + 2 = 3 A` ✓, la corriente total se reparte entre las ramas.",
            "c) `P₃ = I₃² · R₃ = 2² · 3 = 12 W` (o `6² / 3 = 12 W`).",
            "Balance de potencias: `P₁ = 3² · 2 = 18 W`, `P₂ = 1² · 6 = 6 W`, `P₃ = 12 W`; total `36 W = 12 V · 3 A`, lo que entrega la batería ✓.",
            "Respuestas: 4 Ω, 1 A y 12 W. Errores típicos: sumar las resistencias en paralelo como si estuvieran en serie (daría 11 Ω) y aplicarle a R₂ los 12 V completos de la batería, olvidando la caída en R₁.",
        ],
    },
    {
        "id": "f-electricidad-campos-4",
        "node": "f-electricidad-campos",
        "kind": "problem",
        "level": 3,
        "title": "Dónde se anula el campo de dos cargas",
        "statement": (
            "Dos cargas puntuales están fijas sobre el eje x, separadas 30 cm: `q₁ = +4 nC` en x = 0 y "
            "`q₂ = +1 nC` en x = 30 cm. Usá `k = 9 × 10⁹ N·m²/C²` y `1 nC = 10⁻⁹ C`. Tomá el sentido positivo del "
            "eje x de q₁ hacia q₂."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el módulo del campo eléctrico total en el punto medio entre las cargas (x = 15 cm)? Respondé solo con el número en N/C.",
                "check": {"type": "numeric", "value": 1200, "tolerance": 0, "unit": "N/C"},
                "answer": "1200 N/C (hacia +x)",
            },
            {
                "prompt": "b) ¿En qué punto del eje x se anula el campo eléctrico total? Respondé solo con la coordenada x en cm.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "cm"},
                "answer": "20 cm",
            },
            {
                "prompt": "c) Si q₂ fuera −1 nC (en el mismo lugar), ¿en qué punto del eje x se anularía el campo? Respondé solo con la coordenada x en cm.",
                "check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": "cm"},
                "answer": "60 cm",
            },
        ],
        "hints": [
            "El campo de una carga puntual es `E = k · |q| / r²`; apunta alejándose de la carga si es positiva y hacia la carga si es negativa. Sumalos con signo.",
            "Para que el campo total sea cero, los dos campos tienen que tener sentidos opuestos e igual módulo. Mirá en qué región del eje (izquierda de q₁, entre las cargas o derecha de q₂) pasa eso, y si queda más cerca de la carga chica o de la grande.",
            "Al igualar módulos, sacá raíz cuadrada en los dos miembros: la ecuación queda de primer grado.",
        ],
        "solution": [
            "a) En x = 0.15 m: `E₁ = 9×10⁹ · 4×10⁻⁹ / 0.15² = 36 / 0.0225 = 1600 N/C` hacia +x (se aleja de q₁) y `E₂ = 9 / 0.0225 = 400 N/C` hacia −x (se aleja de q₂). Total: `1600 − 400 = 1200 N/C` hacia +x.",
            "b) Con las dos positivas, los campos son opuestos solo entre las cargas (afuera apuntan los dos hacia el mismo lado). El punto tiene que estar más cerca de la carga chica, q₂. Con x en metros: `k · 4×10⁻⁹ / x² = k · 1×10⁻⁹ / (0.3 − x)²`.",
            "Simplificando y sacando raíz: `2 / x = 1 / (0.3 − x)`, entonces `0.6 − 2x = x` y `x = 0.2 m = 20 cm`. Verificación: `E₁ = 36 / 0.04 = 900 N/C` y `E₂ = 9 / 0.01 = 900 N/C` ✓.",
            "c) Con cargas de signo opuesto, entre ellas los dos campos apuntan hacia +x y se suman: ahí no se anula. Afuera son opuestos, y el punto tiene que estar del lado de la carga de menor módulo (a la derecha de q₂), donde la carga grande, más lejana, puede compensar a la chica, más cercana.",
            "Para x > 0.3 m: `4 / x² = 1 / (x − 0.3)²`, entonces `2 / x = 1 / (x − 0.3)`, `2x − 0.6 = x` y `x = 0.6 m = 60 cm`. Verificación: `E₁ = 36 / 0.36 = 100 N/C` hacia +x y `E₂ = 9 / 0.09 = 100 N/C` hacia −x (hacia q₂) ✓.",
            "Respuestas: 1200 N/C, 20 cm y 60 cm. Errores típicos: buscar el punto nulo en el medio (15 cm) porque 'está a igual distancia', o, en c), buscarlo entre las cargas, donde los campos se refuerzan.",
        ],
    },
]
