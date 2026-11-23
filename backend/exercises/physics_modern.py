"""Ejercicios de Física: electromagnetismo, ondas electromagnéticas, óptica, relatividad y física cuántica/nuclear.

Problemas de varios pasos (tipo guía de trabajos prácticos / parcial de ingreso) para los temas
`f-electromagnetismo`, `f-ondas-em`, `f-optica-luz`, `f-relatividad` y `f-cuantica-nuclear`.
Tres por tema (niveles 1, 2 y 3), salvo óptica, que tiene cuatro (niveles 1, 2, 2 y 3).
"""

EXERCISES = [
    # ============================================================
    # f-electromagnetismo — transformador, carga en un campo, Faraday con barra móvil
    # ============================================================
    {
        "id": "f-electromagnetismo-1",
        "node": "f-electromagnetismo",
        "kind": "problem",
        "level": 1,
        "title": "La batidora que vino de Estados Unidos",
        "statement": (
            "Te traen de Estados Unidos una batidora que funciona con **110 V** de alterna y consume **550 W**. "
            "Para usarla en tu casa (red de **220 V**) comprás un transformador ideal (sin pérdidas) cuya bobina "
            "primaria, la que se enchufa a la pared, tiene **800 vueltas**. La batidora se conecta a la secundaria "
            "y funciona exactamente con su tensión y potencia nominales."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuántas vueltas tiene que tener la bobina secundaria? Respondé solo con el número en vueltas.",
                "check": {"type": "numeric", "value": 400, "tolerance": 0, "unit": "vueltas"},
                "answer": "400 vueltas",
            },
            {
                "prompt": "b) ¿Qué corriente circula por la batidora (bobina secundaria)? Respondé solo con el número en A.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "A"},
                "answer": "5 A",
            },
            {
                "prompt": "c) ¿Qué corriente toma el transformador de la red de 220 V (bobina primaria)? Respondé solo con el número en A.",
                "check": {"type": "numeric", "value": 2.5, "tolerance": 0, "unit": "A"},
                "answer": "2.5 A",
            },
        ],
        "hints": [
            "En un transformador ideal la tensión se reparte en la misma proporción que las vueltas: `V₂/V₁ = N₂/N₁`.",
            "Ideal significa que la potencia que entra por la primaria es la misma que sale por la secundaria: `V₁·I₁ = V₂·I₂`, con `P = V·I` en cada lado.",
        ],
        "solution": [
            "Datos: `V₁ = 220 V`, `N₁ = 800`, `V₂ = 110 V`, `P = 550 W`. Es un transformador reductor: la tensión baja a la mitad.",
            "a) `N₂ = N₁ · V₂/V₁ = 800 × 110/220 = 800 × 1/2 = 400 vueltas`.",
            "b) En la secundaria, `P = V₂ · I₂` → `I₂ = P/V₂ = 550 W / 110 V = 5 A`.",
            "c) Al ser ideal, la potencia que entra es la misma que sale: `V₁ · I₁ = 550 W` → `I₁ = 550 / 220 = 2.5 A`.",
            "Verificación: la tensión bajó a la mitad y la corriente subió al doble (`2.5 A → 5 A`), así que `220 × 2.5 = 110 × 5 = 550 W`. Error típico: creer que la corriente también se reduce a la mitad; un transformador no \"fabrica\" energía, lo que gana en corriente lo pierde en tensión.",
        ],
    },
    {
        "id": "f-electromagnetismo-2",
        "node": "f-electromagnetismo",
        "kind": "problem",
        "level": 2,
        "title": "Protones girando en un ciclotrón",
        "statement": (
            "En un ciclotrón que se usa para producir radioisótopos médicos, un protón entra con rapidez "
            "**v = 2 × 10⁶ m/s** en una zona de campo magnético uniforme **B = 0.5 T**, moviéndose perpendicular al "
            "campo. Datos: carga del protón **q = 1.6 × 10⁻¹⁹ C**, masa del protón **m ≈ 1.6 × 10⁻²⁷ kg**. "
            "Despreciá la gravedad y cualquier otra fuerza que no sea la magnética."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el radio de la circunferencia que describe el protón? Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "cm"},
                "answer": "4 cm",
            },
            {
                "prompt": (
                    "b) Ahora entra en el mismo campo, con la misma rapidez, una partícula alfa (carga **2q**, masa **4m**). "
                    "¿Cuál es el radio de su trayectoria? Respondé solo con el número en cm."
                ),
                "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": "cm"},
                "answer": "8 cm",
            },
            {
                "prompt": "c) Mientras el protón gira dentro del campo magnético, ¿qué pasa con su rapidez?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Se mantiene constante, porque la fuerza magnética es siempre perpendicular a la velocidad y no hace trabajo",
                        "Aumenta en cada vuelta, porque el campo magnético le entrega energía",
                        "Disminuye de a poco, porque la fuerza magnética apunta hacia el centro y lo frena",
                        "Se hace cero, porque el protón queda atrapado por el campo",
                    ],
                    "correct": 0,
                },
                "answer": "Se mantiene constante: la fuerza magnética es perpendicular a la velocidad, solo cambia la dirección y no realiza trabajo.",
            },
        ],
        "hints": [
            "La fuerza magnética sobre una carga que se mueve perpendicular al campo vale `F = q·v·B` y apunta siempre hacia el centro de la curva.",
            "Esa fuerza es la fuerza centrípeta: igualá `q·v·B = m·v²/r` y despejá `r`.",
        ],
        "solution": [
            "Fuerza magnética sobre el protón (velocidad perpendicular al campo): `F = q·v·B = 1.6 × 10⁻¹⁹ × 2 × 10⁶ × 0.5 = 1.6 × 10⁻¹³ N`.",
            "Como es perpendicular a la velocidad, actúa como fuerza centrípeta: `q·v·B = m·v²/r` → `r = m·v / (q·B)`.",
            "a) `r = (1.6 × 10⁻²⁷ × 2 × 10⁶) / (1.6 × 10⁻¹⁹ × 0.5) = (3.2 × 10⁻²¹) / (8 × 10⁻²⁰) = 0.04 m = 4 cm`. Verificación: `m·v²/r = 1.6 × 10⁻²⁷ × 4 × 10¹² / 0.04 = 1.6 × 10⁻¹³ N`, igual a la fuerza magnética.",
            "b) Para la alfa: `r_α = (4m)·v / ((2q)·B) = 2 · m·v/(q·B) = 2 × 4 cm = 8 cm`. La masa cuadruplica el radio y la carga doble lo reduce a la mitad.",
            "c) Una fuerza perpendicular a la velocidad no hace trabajo (`W = F·d·cos 90° = 0`), así que la energía cinética y la rapidez no cambian: el campo solo curva la trayectoria. (En un ciclotrón real, lo que acelera a la partícula es un campo eléctrico entre las \"D\", no el magnético.)",
            "Respuestas: 4 cm, 8 cm y rapidez constante. Error típico: usar `r = q·B/(m·v)` (invertido), que da 25 m⁻¹: un resultado que ni siquiera tiene unidades de longitud.",
        ],
    },
    {
        "id": "f-electromagnetismo-3",
        "node": "f-electromagnetismo",
        "kind": "problem",
        "level": 3,
        "title": "Barra que se desliza sobre rieles: generador y freno",
        "statement": (
            "Dos rieles conductores horizontales y paralelos, separados **0.5 m**, están unidos en un extremo por un "
            "resistor. Sobre ellos se desliza sin rozamiento una barra metálica perpendicular a los rieles, de modo "
            "que barra, rieles y resistor forman un circuito cerrado. Todo está dentro de un campo magnético uniforme "
            "**B = 0.4 T**, perpendicular al plano de los rieles. Un motor externo tira de la barra para que avance "
            "con velocidad constante **v = 5 m/s**, alejándose del resistor. La resistencia total del circuito es "
            "**R = 0.25 Ω**. Es un modelo simple de lo que pasa en el frenado regenerativo."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la fem inducida en el circuito? Respondé solo con el número en V.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": "V"},
                "answer": "1 V",
            },
            {
                "prompt": "b) ¿Qué corriente circula por el circuito? Respondé solo con el número en A.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "A"},
                "answer": "4 A",
            },
            {
                "prompt": "c) ¿Con qué fuerza tiene que tirar el motor de la barra para mantener la velocidad constante? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 0.8, "tolerance": 0, "unit": "N"},
                "answer": "0.8 N",
            },
        ],
        "hints": [
            "Al avanzar la barra, el área encerrada por el circuito crece; por lo tanto cambia el flujo `Φ = B·A`. Calculá cuánto área se agrega por segundo.",
            "Por Faraday, `fem = ΔΦ/Δt`. Con la corriente, la barra es un cable con corriente dentro de un campo: siente `F = B·I·L`. ¿Hacia dónde apunta según Lenz?",
            "A velocidad constante la fuerza neta es cero: el motor tiene que compensar exactamente la fuerza magnética.",
        ],
        "solution": [
            "En un intervalo `Δt` la barra avanza `v·Δt` y el área del circuito crece `ΔA = L·v·Δt = 0.5 × 5 × Δt = 2.5 m²` por cada segundo.",
            "a) Variación de flujo por segundo: `ΔΦ/Δt = B · ΔA/Δt = 0.4 T × 2.5 m²/s = 1 Wb/s`. Por la ley de Faraday, `fem = ΔΦ/Δt = 1 V` (es lo mismo que `B·L·v = 0.4 × 0.5 × 5 = 1 V`).",
            "b) Ley de Ohm para el circuito: `I = fem / R = 1 V / 0.25 Ω = 4 A`.",
            "Por la ley de Lenz, la corriente inducida circula en el sentido que se opone al aumento del flujo; el resultado es que la fuerza magnética sobre la barra apunta en contra de su movimiento (la frena).",
            "c) Fuerza magnética sobre la barra (cable con corriente perpendicular al campo): `F = B·I·L = 0.4 × 4 × 0.5 = 0.8 N`, hacia atrás. Para que la velocidad sea constante, el motor debe tirar con `0.8 N` hacia adelante.",
            "Verificación por energía: potencia mecánica del motor `P = F·v = 0.8 × 5 = 4 W`; potencia eléctrica en el resistor `P = I²·R = 4² × 0.25 = 4 W`. Todo el trabajo del motor se convierte en energía eléctrica. Error típico: pensar que la fuerza magnética empuja la barra hacia adelante; eso violaría la conservación de la energía.",
        ],
    },
    # ============================================================
    # f-ondas-em — c = f·λ, tiempo de viaje, energía por fotón, doble rendija
    # ============================================================
    {
        "id": "f-ondas-em-1",
        "node": "f-ondas-em",
        "kind": "problem",
        "level": 1,
        "title": "Del AM al láser: el mismo c para todas",
        "statement": (
            "Tres ondas electromagnéticas viajan por el aire (tomá la misma velocidad que en el vacío, "
            "**c = 3 × 10⁸ m/s**): la señal de la radio **AM 750** (frecuencia **750 kHz**), las microondas de un "
            "horno que trabaja a **2.5 GHz** y la luz verde de un puntero láser de longitud de onda **500 nm**. "
            "Recordá: 1 kHz = 10³ Hz, 1 GHz = 10⁹ Hz, 1 THz = 10¹² Hz, 1 nm = 10⁻⁹ m."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la longitud de onda de la radio AM 750? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 400, "tolerance": 0, "unit": "m"},
                "answer": "400 m",
            },
            {
                "prompt": "b) ¿Cuál es la longitud de onda de las microondas del horno? Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": "cm"},
                "answer": "12 cm",
            },
            {
                "prompt": "c) ¿Cuál es la frecuencia de la luz verde del láser? Respondé solo con el número en THz.",
                "check": {"type": "numeric", "value": 600, "tolerance": 0, "unit": "THz"},
                "answer": "600 THz",
            },
        ],
        "hints": [
            "Las tres cumplen `c = f · λ`; despejá lo que falte en cada caso.",
            "Pasá todo a unidades SI (Hz y m) antes de dividir, y recién al final convertí a la unidad pedida.",
        ],
        "solution": [
            "Las tres son ondas electromagnéticas: viajan a la misma velocidad `c` y solo difieren en `f` y `λ`, ligadas por `c = f · λ`.",
            "a) `f = 750 kHz = 7.5 × 10⁵ Hz` → `λ = c/f = 3 × 10⁸ / 7.5 × 10⁵ = 0.4 × 10³ m = 400 m`. Por eso las antenas de AM son torres enormes.",
            "b) `f = 2.5 GHz = 2.5 × 10⁹ Hz` → `λ = 3 × 10⁸ / 2.5 × 10⁹ = 1.2 × 10⁻¹ m = 0.12 m = 12 cm`.",
            "c) `λ = 500 nm = 5 × 10⁻⁷ m` → `f = c/λ = 3 × 10⁸ / 5 × 10⁻⁷ = 0.6 × 10¹⁵ Hz = 6 × 10¹⁴ Hz = 600 THz`.",
            "Verificación: a mayor frecuencia, menor longitud de onda (400 m → 12 cm → 0.0000005 m), como indica el orden del espectro radio < microondas < visible. Error típico: olvidar el prefijo (usar 750 Hz en lugar de 750 kHz da λ = 400 km).",
        ],
    },
    {
        "id": "f-ondas-em-2",
        "node": "f-ondas-em",
        "kind": "problem",
        "level": 2,
        "title": "Una llamada por el ARSAT",
        "statement": (
            "Un canal de TV de Buenos Aires envía una transmisión en vivo a Ushuaia a través de un satélite "
            "geoestacionario como el ARSAT-1. La señal sube de la estación terrena al satélite y baja a la otra "
            "estación; tomá **36 000 km** para cada tramo y **c = 300 000 km/s**. La señal usa la banda Ku, con "
            "longitud de onda **λ = 2.5 cm**. Para comparar, considerá un fotón de luz verde de **500 nm**. "
            "Usá **h·c = 1240 eV·nm**."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto tarda la señal en ir de Buenos Aires a Ushuaia pasando por el satélite? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 0.24, "tolerance": 0, "unit": "s"},
                "answer": "0.24 s",
            },
            {
                "prompt": "b) ¿Qué energía tiene un fotón de la luz verde de 500 nm? Respondé solo con el número en eV.",
                "check": {"type": "numeric", "value": 2.48, "tolerance": 0, "unit": "eV"},
                "answer": "2.48 eV",
            },
            {
                "prompt": "c) ¿Cuántas veces mayor es la energía de ese fotón verde que la de un fotón de la señal del satélite? Respondé solo con el número en veces.",
                "check": {"type": "numeric", "value": 50000, "tolerance": 0, "unit": "veces"},
                "answer": "50 000 veces",
            },
        ],
        "hints": [
            "La señal viaja a `c` en los dos tramos: sumá las distancias y usá `t = d / c`.",
            "La energía de un fotón es `E = h·f = h·c/λ`. Con `λ` en nm, `E = 1240/λ` da directamente eV.",
            "Como `E` es inversamente proporcional a `λ`, el cociente de energías es el cociente de longitudes de onda (invertido). Pasá las dos a la misma unidad.",
        ],
        "solution": [
            "a) Distancia total: `36 000 km + 36 000 km = 72 000 km`. Tiempo: `t = d/c = 72 000 / 300 000 = 0.24 s`. En una entrevista con ida y vuelta (pregunta y respuesta) el retardo se duplica a casi medio segundo: por eso se notan las pausas.",
            "b) `E_verde = h·c/λ = 1240 eV·nm / 500 nm = 2.48 eV`.",
            "c) Como `E = h·c/λ`, el cociente es `E_verde / E_satélite = λ_satélite / λ_verde`.",
            "Misma unidad: `λ_satélite = 2.5 cm = 0.025 m = 2.5 × 10⁷ nm`; `λ_verde = 500 nm`. Cociente: `2.5 × 10⁷ / 500 = 50 000`.",
            "Verificación: `E_satélite = 1240 / (2.5 × 10⁷) ≈ 5 × 10⁻⁵ eV`, y `2.48 / (4.96 × 10⁻⁵) = 50 000`. Cada fotón de la señal tiene una energía ínfima: por eso las microondas de comunicación no son ionizantes, aunque viajen a la misma velocidad que la luz. Error típico: comparar 2.5 cm con 500 nm sin pasar a la misma unidad.",
        ],
    },
    {
        "id": "f-ondas-em-3",
        "node": "f-ondas-em",
        "kind": "problem",
        "level": 3,
        "title": "Medir la longitud de onda de un láser con dos rendijas",
        "statement": (
            "En el laboratorio de la facultad iluminás una doble rendija con un láser rojo. La separación entre las "
            "rendijas es **d = 0.4 mm** y la pantalla está a **L = 2 m**. Medís que la **5ª franja brillante** "
            "(sin contar la central) está a **15.5 mm** del centro del patrón. Usá la aproximación de ángulos "
            "pequeños: las franjas brillantes están en `y = m·λ·L/d` (m = 0, 1, 2, …) y las oscuras a mitad de "
            "camino entre dos brillantes consecutivas. Usá **h·c = 1240 eV·nm**."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la longitud de onda del láser? Respondé solo con el número en nm.",
                "check": {"type": "numeric", "value": 620, "tolerance": 0, "unit": "nm"},
                "answer": "620 nm",
            },
            {
                "prompt": "b) ¿Qué energía tiene cada fotón de ese láser? Respondé solo con el número en eV.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "eV"},
                "answer": "2 eV",
            },
            {
                "prompt": "c) ¿A qué distancia del centro está la **segunda franja oscura**? Respondé solo con el número en mm.",
                "check": {"type": "numeric", "value": 4.65, "tolerance": 0, "unit": "mm"},
                "answer": "4.65 mm",
            },
        ],
        "hints": [
            "Despejá `λ` de `y = m·λ·L/d` con `m = 5`, cuidando que `y` y `d` estén en metros.",
            "La separación entre franjas brillantes consecutivas es `Δy = λ·L/d`. La primera oscura está a `0.5·Δy` del centro; ¿y la segunda?",
        ],
        "solution": [
            "a) De `y₅ = 5·λ·L/d` despejamos `λ = y₅·d / (5·L) = (15.5 × 10⁻³ m × 0.4 × 10⁻³ m) / (5 × 2 m) = 6.2 × 10⁻⁶ / 10 = 6.2 × 10⁻⁷ m = 620 nm` (rojo, como se esperaba).",
            "b) `E = h·c/λ = 1240 eV·nm / 620 nm = 2 eV`.",
            "c) Separación entre franjas brillantes: `Δy = λ·L/d = 6.2 × 10⁻⁷ × 2 / (0.4 × 10⁻³) = 3.1 × 10⁻³ m = 3.1 mm` (coincide con `15.5 mm / 5`).",
            "Las oscuras quedan a mitad de camino: la 1ª en `0.5·Δy = 1.55 mm` y la 2ª en `1.5·Δy = 1.5 × 3.1 = 4.65 mm`.",
            "Verificación de la aproximación: `y/L = 15.5 mm / 2000 mm ≈ 0.008`, un ángulo de menos de medio grado, así que `sen θ ≈ tan θ` es muy buena. Error típico: ubicar la 2ª oscura en `2·Δy = 6.2 mm`, que es la 2ª brillante.",
        ],
    },
    # ============================================================
    # f-optica-luz — reflexión y Snell, ángulo crítico, espejos, sistema de dos lentes
    # ============================================================
    {
        "id": "f-optica-luz-1",
        "node": "f-optica-luz",
        "kind": "problem",
        "level": 1,
        "title": "Un láser sobre la pileta",
        "statement": (
            "De noche apuntás un puntero láser a la superficie quieta de una pileta. El rayo llega desde el aire "
            "(**n = 1**) formando un ángulo **θ₁ ≈ 53°** con la normal, y parte de la luz se refleja mientras otra parte "
            "entra al agua (**n = 4/3 ≈ 1.33**). Datos: **sen 53° ≈ 0.8**, **sen 37° ≈ 0.6**, **c = 300 000 km/s**."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué ángulo forma con la normal el rayo que entra al agua? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 37, "tolerance": 0.01, "unit": "°"},
                "answer": "37°",
            },
            {
                "prompt": "b) ¿Qué ángulo forman entre sí el rayo reflejado y el rayo refractado? Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 90, "tolerance": 0.01, "unit": "°"},
                "answer": "90°",
            },
            {
                "prompt": "c) ¿A qué velocidad viaja la luz del láser dentro del agua? Respondé solo con el número en km/s.",
                "check": {"type": "numeric", "value": 225000, "tolerance": 0, "unit": "km/s"},
                "answer": "225 000 km/s",
            },
        ],
        "hints": [
            "Para el rayo que entra al agua usá Snell: `n₁·sen θ₁ = n₂·sen θ₂`. Para el reflejado: `θ_r = θ_i`.",
            "Hacé un dibujo: la normal es vertical; el reflejado queda arriba de la superficie y el refractado abajo, del otro lado de la normal. Sumá los ángulos alrededor del punto de incidencia.",
        ],
        "solution": [
            "a) Snell: `1 × sen 53° = (4/3) × sen θ₂` → `sen θ₂ = 0.8 × 3/4 = 0.6` → `θ₂ ≈ 37°`. El rayo se acerca a la normal porque entra a un medio de mayor índice.",
            "Reflexión: el rayo reflejado forma con la normal el mismo ángulo que el incidente, `θ_r = 53°`, y sale por arriba de la superficie.",
            "b) Medidos desde la superficie, el reflejado forma `90° − 53° = 37°` con el agua (por arriba) y el refractado `90° − 37° = 53°` (por abajo). Como el reflejado y el refractado quedan a un lado y otro de la superficie, el ángulo entre ellos es `37° + 53° = 90°` (equivalente: `180° − 53° − 37° = 90°`).",
            "c) `v = c/n = 300 000 / (4/3) = 300 000 × 3/4 = 225 000 km/s`.",
            "Respuestas: 37°, 90° y 225 000 km/s. Error típico: en a) multiplicar por 4/3 en lugar de dividir, lo que daría `sen θ₂ ≈ 1.07` (imposible). Que reflejado y refractado formen 90° es justamente la condición en la que el reflejo sale polarizado (ángulo de Brewster).",
        ],
    },
    {
        "id": "f-optica-luz-2",
        "node": "f-optica-luz",
        "kind": "problem",
        "level": 2,
        "title": "Cuándo la luz se queda adentro de la fibra",
        "statement": (
            "Una fibra óptica tiene un núcleo de vidrio con índice **n₁ = 1.5**, recubierto por un revestimiento de "
            "índice **n₂ = 1.2**. La luz entra por el extremo plano de la fibra desde el aire (**n = 1**) y viaja "
            "por el núcleo rebotando en la pared que lo separa del revestimiento. Datos: **sen 53° ≈ 0.8**, "
            "**sen 37° ≈ 0.6**."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale el seno del ángulo crítico en la pared núcleo–revestimiento? Respondé solo con el número (sin unidad).",
                "check": {"type": "numeric", "value": 0.8, "tolerance": 0, "unit": ""},
                "answer": "0.8 (ángulo crítico ≈ 53°)",
            },
            {
                "prompt": "b) Dentro del núcleo, un rayo llega a la pared formando **45°** con la normal y otro formando **60°**. ¿Qué les pasa?",
                "check": {
                    "type": "choice",
                    "options": [
                        "El de 60° se refleja totalmente; el de 45° pasa en parte al revestimiento",
                        "El de 45° se refleja totalmente; el de 60° pasa en parte al revestimiento",
                        "Los dos se reflejan totalmente, porque la luz va de un medio de mayor índice a uno de menor índice",
                        "Ninguno se refleja totalmente, porque los dos ángulos son menores que 90°",
                    ],
                    "correct": 0,
                },
                "answer": "El de 60° supera el ángulo crítico (≈ 53°) y se refleja totalmente; el de 45° no lo supera y una parte se escapa.",
            },
            {
                "prompt": (
                    "c) Un rayo entra por el extremo plano de la fibra (perpendicular al eje) desde el aire. ¿Cuál es el "
                    "máximo valor del seno del ángulo de entrada (medido desde el eje de la fibra) para que después haya "
                    "reflexión total en la pared? Respondé solo con el número (sin unidad)."
                ),
                "check": {"type": "numeric", "value": 0.9, "tolerance": 0, "unit": ""},
                "answer": "0.9",
            },
        ],
        "hints": [
            "El ángulo crítico cumple `n₁·sen θ_c = n₂·sen 90°`. Hay reflexión total cuando el rayo llega a la pared con un ángulo MAYOR que `θ_c`.",
            "Para c): el extremo es perpendicular a la pared lateral, así que si el rayo refractado forma un ángulo `θ_r` con el eje, llega a la pared con `90° − θ_r` respecto de su normal.",
            "Exigí `90° − θ_r ≥ θ_c`, o sea `θ_r ≤ 37°`, y volvé al aire con Snell en el extremo.",
        ],
        "solution": [
            "a) En el ángulo crítico el rayo refractado saldría rasante (90°): `1.5 · sen θ_c = 1.2 · 1` → `sen θ_c = 1.2/1.5 = 0.8` → `θ_c ≈ 53°`.",
            "b) Hay reflexión total solo si el ángulo de incidencia supera `θ_c ≈ 53°`. El rayo de 60° la supera y se refleja al 100%; el de 45° no, así que una parte se refracta hacia el revestimiento (`sen θ = 1.5 × sen 45°/1.2 ≈ 0.88 < 1`, tiene solución).",
            "c) En el extremo, el rayo entra con ángulo `θ_a` respecto del eje (que es la normal de esa cara) y se refracta con `θ_r`. Como el extremo y la pared son perpendiculares, el rayo llega a la pared con `90° − θ_r`.",
            "Condición de reflexión total: `90° − θ_r ≥ 53°` → `θ_r ≤ 37°` → `sen θ_r ≤ 0.6` (es decir, `sen θ_r ≤ cos θ_c`).",
            "Snell en la entrada: `1 · sen θ_a = 1.5 · sen θ_r ≤ 1.5 × 0.6 = 0.9`. El máximo es `sen θ_a = 0.9` (unos 64°). Este número se llama apertura numérica de la fibra.",
            "Error típico: pensar que basta con ir de mayor a menor índice para que haya reflexión total; además hace falta superar el ángulo crítico.",
        ],
    },
    {
        "id": "f-optica-luz-3",
        "node": "f-optica-luz",
        "kind": "problem",
        "level": 2,
        "title": "El espejo de maquillaje",
        "statement": (
            "Un espejo de maquillaje es un espejo **cóncavo** de distancia focal **f = 20 cm**. Acercás la cara a "
            "**15 cm** del espejo. Usá la ecuación `1/f = 1/d_o + 1/d_i` con esta convención: `f > 0` para espejo "
            "cóncavo, `d_i > 0` si la imagen es real (delante del espejo) y `d_i < 0` si es virtual (detrás del "
            "espejo); el aumento es `M = −d_i/d_o` (M > 0: imagen derecha; M < 0: invertida)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale `d_i`? Respondé solo con el número en cm, con su signo.",
                "check": {"type": "numeric", "value": -60, "tolerance": 0, "unit": "cm"},
                "answer": "−60 cm (imagen virtual, 60 cm detrás del espejo)",
            },
            {
                "prompt": "b) ¿Cuál es el aumento de la imagen? Respondé solo con el número (sin unidad).",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4 (imagen derecha y 4 veces más grande)",
            },
            {
                "prompt": "c) Si alejás la cara a **30 cm** del mismo espejo, ¿cómo es la imagen que forma?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Real, invertida y del doble de tamaño, a 60 cm delante del espejo",
                        "Virtual, derecha y del doble de tamaño, a 60 cm detrás del espejo",
                        "Real, invertida y de la mitad de tamaño, a 12 cm delante del espejo",
                        "Virtual, derecha y 4 veces más grande, igual que a 15 cm",
                    ],
                    "correct": 0,
                },
                "answer": "Real, invertida y del doble de tamaño: d_i = +60 cm y M = −2.",
            },
        ],
        "hints": [
            "Despejá `1/d_i = 1/f − 1/d_o` y operá con denominador común. El signo del resultado te dice si la imagen es real o virtual.",
            "Para c) repetí la cuenta con `d_o = 30 cm`. Fijate si el objeto quedó dentro o fuera de la distancia focal.",
        ],
        "solution": [
            "a) `1/d_i = 1/20 − 1/15 = 3/60 − 4/60 = −1/60` → `d_i = −60 cm`. El signo negativo indica imagen virtual, 60 cm detrás del espejo.",
            "b) `M = −d_i/d_o = −(−60)/15 = +4`: imagen derecha y 4 veces más grande. Por eso sirve para maquillarse: la cara está dentro de la distancia focal (15 cm < 20 cm) y el espejo funciona como lupa.",
            "c) Con `d_o = 30 cm`: `1/d_i = 1/20 − 1/30 = 3/60 − 2/60 = 1/60` → `d_i = +60 cm` (real, delante del espejo).",
            "Aumento: `M = −60/30 = −2`: invertida y del doble de tamaño. El objeto quedó entre `f` y `2f` (20 cm < 30 cm < 40 cm), que es justo el caso de imagen real, invertida y agrandada.",
            "Respuestas: −60 cm, 4 y \"real, invertida, doble\". Error típico: restar las distancias directamente (`20 − 15 = 5 cm`) en lugar de sus inversos, o perder el signo y creer que la imagen a 15 cm es real.",
        ],
    },
    {
        "id": "f-optica-luz-4",
        "node": "f-optica-luz",
        "kind": "problem",
        "level": 3,
        "title": "Dos lentes en fila",
        "statement": (
            "En un banco óptico hay dos lentes convergentes delgadas iguales, de distancia focal **f = 10 cm**, "
            "separadas **50 cm** sobre el mismo eje. Un objeto de **1.5 cm** de altura se coloca **15 cm** a la "
            "izquierda de la primera lente; la luz va de izquierda a derecha. Usá `1/f = 1/d_o + 1/d_i` "
            "(`d_i > 0`: imagen real del otro lado de la lente) y `M = −d_i/d_o`."
        ),
        "parts": [
            {
                "prompt": "a) ¿A qué distancia a la derecha de la primera lente se forma su imagen? Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": "cm"},
                "answer": "30 cm",
            },
            {
                "prompt": "b) ¿A qué distancia a la derecha de la segunda lente se forma la imagen final? Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": "cm"},
                "answer": "20 cm",
            },
            {
                "prompt": "c) ¿Cómo es la imagen final respecto del objeto original?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Real, derecha y de 3 cm de altura",
                        "Real, invertida y de 3 cm de altura",
                        "Virtual, derecha y de 3 cm de altura",
                        "Real, invertida y de 4.5 cm de altura",
                    ],
                    "correct": 0,
                },
                "answer": "Real, derecha y de 3 cm de altura (aumento total +2).",
            },
        ],
        "hints": [
            "Resolvé primero la lente 1 sola. Su imagen es el objeto de la lente 2.",
            "La distancia objeto para la lente 2 es la separación entre lentes menos la distancia de la primera imagen.",
            "El aumento total es el PRODUCTO de los aumentos de cada lente; el signo te dice si queda derecha o invertida.",
        ],
        "solution": [
            "a) Lente 1: `1/d_i1 = 1/10 − 1/15 = 3/30 − 2/30 = 1/30` → `d_i1 = 30 cm` (real, a la derecha). Aumento: `M₁ = −30/15 = −2` (invertida, doble).",
            "Esa imagen está a `50 − 30 = 20 cm` a la izquierda de la lente 2, así que funciona como objeto real para ella: `d_o2 = 20 cm`.",
            "b) Lente 2: `1/d_i2 = 1/10 − 1/20 = 2/20 − 1/20 = 1/20` → `d_i2 = 20 cm` a la derecha de la segunda lente (real). Aumento: `M₂ = −20/20 = −1`.",
            "c) Aumento total: `M = M₁ · M₂ = (−2) × (−1) = +2`. Altura final: `2 × 1.5 cm = 3 cm`. Como `M > 0`, la imagen final es derecha (la segunda lente vuelve a invertir la imagen invertida) y, al tener `d_i2 > 0`, es real: se puede proyectar en una pantalla.",
            "Verificación: el objeto de la lente 2 está en `2f` (20 cm), y una lente convergente con el objeto en `2f` da imagen en `2f`, invertida y de igual tamaño (`M₂ = −1`), como obtuvimos. Errores típicos: sumar los aumentos (`2 + 1 = 3` → 4.5 cm) o usar 50 cm como distancia objeto de la segunda lente.",
        ],
    },
    # ============================================================
    # f-relatividad — dilatación del tiempo, E = mc², partícula vista desde dos sistemas
    # ============================================================
    {
        "id": "f-relatividad-1",
        "node": "f-relatividad",
        "kind": "problem",
        "level": 1,
        "title": "Viaje a una estrella a 0.6 c",
        "statement": (
            "Una nave parte de la Tierra hacia una estrella que, medida desde la Tierra, está a **6 años luz** "
            "(la distancia que recorre la luz en 6 años). Viaja a velocidad constante **v = 0.6 c** "
            "(despreciá los tiempos de aceleración y frenado). Usá `γ = 1/√(1 − v²/c²)`."
        ),
        "parts": [
            {
                "prompt": "a) Según los relojes de la Tierra, ¿cuánto tarda la nave en llegar a la estrella? Respondé solo con el número en años.",
                "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "años"},
                "answer": "10 años",
            },
            {
                "prompt": "b) ¿Cuánto tiempo marca el reloj de la tripulación durante ese viaje de ida? Respondé solo con el número en años.",
                "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": "años"},
                "answer": "8 años",
            },
            {
                "prompt": (
                    "c) La nave vuelve a la Tierra a la misma velocidad. Una tripulante dejó a su hermano gemelo en la "
                    "Tierra. Al reencontrarse, ¿cuántos años más viejo es el que se quedó? Respondé solo con el número en años."
                ),
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "años"},
                "answer": "4 años",
            },
        ],
        "hints": [
            "Desde la Tierra el problema es de MRU: `t = d/v`. Un año luz dividido por c da un año.",
            "El reloj de la nave mide el tiempo propio `Δt₀`, que es el más corto: `Δt = γ · Δt₀`.",
        ],
        "solution": [
            "a) Desde la Tierra: `t = d/v = 6 años luz / 0.6 c = 10 años` (porque 1 año luz / c = 1 año).",
            "Factor de Lorentz: `v²/c² = 0.36` → `√(1 − 0.36) = √0.64 = 0.8` → `γ = 1/0.8 = 1.25`.",
            "b) El reloj de la nave está presente en la partida y en la llegada, así que mide el tiempo propio: `Δt₀ = Δt/γ = 10/1.25 = 8 años`.",
            "c) Ida y vuelta: en la Tierra pasan `2 × 10 = 20 años`; en la nave, `2 × 8 = 16 años`. Diferencia: `20 − 16 = 4 años`.",
            "Verificación: para la tripulación la distancia a la estrella está contraída a `6/1.25 = 4.8 años luz`, y `4.8 / 0.6 = 8 años`, igual que en b). Error típico: multiplicar por γ en vez de dividir y concluir que en la nave pasan 12.5 años; el viajero es quien envejece menos.",
        ],
    },
    {
        "id": "f-relatividad-2",
        "node": "f-relatividad",
        "kind": "problem",
        "level": 2,
        "title": "Cuánta energía hay en un miligramo",
        "statement": (
            "Imaginá (es una idealización) que pudieras convertir por completo en energía eléctrica una masa de "
            "**1 mg** de cualquier material. Una casa típica consume **250 kWh por mes**. Datos: "
            "**c = 3 × 10⁸ m/s**, **1 kWh = 3.6 × 10⁶ J**, **1 GJ = 10⁹ J**, **1 mg = 10⁻⁶ kg**."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la energía en reposo de 1 mg? Respondé solo con el número en GJ.",
                "check": {"type": "numeric", "value": 90, "tolerance": 0, "unit": "GJ"},
                "answer": "90 GJ",
            },
            {
                "prompt": "b) ¿Durante cuántos meses podría abastecer esa energía a una casa típica? Respondé solo con el número en meses.",
                "check": {"type": "numeric", "value": 100, "tolerance": 0, "unit": "meses"},
                "answer": "100 meses",
            },
            {
                "prompt": "c) ¿Qué masa habría que convertir en energía para abastecer un barrio de **1000 casas** durante **un año**? Respondé solo con el número en mg.",
                "check": {"type": "numeric", "value": 120, "tolerance": 0, "unit": "mg"},
                "answer": "120 mg",
            },
        ],
        "hints": [
            "`E = m·c²` con la masa en kg da joules. Ojo: `c² = 9 × 10¹⁶ m²/s²`.",
            "Para comparar con el consumo, pasá todo a la misma unidad (J o kWh).",
            "En c) calculá primero la energía total que consume el barrio en un año y después despejá `m = E/c²`.",
        ],
        "solution": [
            "a) `E = m·c² = 10⁻⁶ kg × (3 × 10⁸ m/s)² = 10⁻⁶ × 9 × 10¹⁶ = 9 × 10¹⁰ J = 90 × 10⁹ J = 90 GJ`.",
            "b) En kWh: `9 × 10¹⁰ / 3.6 × 10⁶ = 2.5 × 10⁴ kWh = 25 000 kWh`. Meses: `25 000 / 250 = 100 meses` (más de 8 años).",
            "c) Consumo del barrio en un año: `1000 casas × 12 meses × 250 kWh = 3 × 10⁶ kWh = 3 × 10⁶ × 3.6 × 10⁶ J = 1.08 × 10¹³ J`.",
            "Masa necesaria: `m = E/c² = 1.08 × 10¹³ / 9 × 10¹⁶ = 1.2 × 10⁻⁴ kg = 120 mg`.",
            "Verificación: por b), 1 mg cubre 100 casa-mes; el barrio necesita `1000 × 12 = 12 000` casa-mes, o sea `12 000/100 = 120 mg`. En una central nuclear real solo se convierte en energía una fracción ínfima de la masa del combustible (menos del 0.1%). Error típico: usar `c` en lugar de `c²`, o la masa en gramos.",
        ],
    },
    {
        "id": "f-relatividad-3",
        "node": "f-relatividad",
        "kind": "problem",
        "level": 3,
        "title": "¿Llega la partícula al detector?",
        "statement": (
            "En la alta atmósfera se crea una partícula inestable que baja en línea recta hacia un detector con "
            "velocidad constante **v = 0.8 c**. Medida desde la Tierra, la distancia entre el punto donde se crea y "
            "el detector es **540 m**. Suponé que, en su propio sistema de referencia, la partícula vive exactamente "
            "**1.5 μs** y luego se desintegra. Datos: **c = 3 × 10⁸ m/s**, `γ = 1/√(1 − v²/c²)`, **1 μs = 10⁻⁶ s**."
        ),
        "parts": [
            {
                "prompt": "a) Según los relojes de la Tierra, ¿cuánto tardaría la partícula en llegar al detector? Respondé solo con el número en μs.",
                "check": {"type": "numeric", "value": 2.25, "tolerance": 0, "unit": "μs"},
                "answer": "2.25 μs",
            },
            {
                "prompt": "b) En el sistema de la partícula, ¿cuánto mide la distancia que tiene que recorrer el detector hasta encontrarla? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 324, "tolerance": 0, "unit": "m"},
                "answer": "324 m",
            },
            {
                "prompt": "c) ¿Llega la partícula al detector antes de desintegrarse?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Sí: en su propio reloj el trayecto dura 1.35 μs, menos que los 1.5 μs que vive",
                        "No: sin relatividad recorrería solo 360 m en 1.5 μs, y el detector está a 540 m",
                        "No: el viaje dura 2.25 μs medidos en la Tierra, y eso es más que 1.5 μs",
                        "Sí para el observador en la Tierra, pero no en el sistema de la partícula",
                    ],
                    "correct": 0,
                },
                "answer": "Sí: en su sistema recorre 324 m en 1.35 μs < 1.5 μs; desde la Tierra vive 2.5 μs > 2.25 μs. Los dos sistemas coinciden.",
            },
        ],
        "hints": [
            "Con `v = 0.8 c` tenés `√(1 − 0.64) = 0.6` y `γ = 5/3`.",
            "Desde la Tierra, la vida de la partícula se dilata (`γ · 1.5 μs`); desde la partícula, la distancia se contrae (`540 m / γ`).",
            "Un hecho físico (que llegue o no) no puede depender del sistema: las dos cuentas tienen que dar la misma conclusión.",
        ],
        "solution": [
            "Velocidad: `v = 0.8 × 3 × 10⁸ = 2.4 × 10⁸ m/s`. Factor: `√(1 − 0.8²) = √0.36 = 0.6` → `γ = 1/0.6 = 5/3`.",
            "a) Sistema Tierra: `t = 540 m / 2.4 × 10⁸ m/s = 2.25 × 10⁻⁶ s = 2.25 μs`.",
            "En ese mismo sistema, la vida de la partícula está dilatada: `Δt = γ · Δt₀ = (5/3) × 1.5 = 2.5 μs`. Como `2.25 μs < 2.5 μs`, llega con vida.",
            "b) Sistema partícula: la distancia está contraída, `L = L₀/γ = 540 × 0.6 = 324 m`.",
            "c) En su propio reloj el trayecto dura `324 / 2.4 × 10⁸ = 1.35 × 10⁻⁶ s = 1.35 μs < 1.5 μs`: sí llega. Coherencia: `2.25 μs / γ = 2.25 × 0.6 = 1.35 μs`, el mismo tiempo propio calculado de las dos formas.",
            "Errores típicos: el cálculo clásico (`2.4 × 10⁸ × 1.5 × 10⁻⁶ = 360 m < 540 m`) predice que no llega, y es justamente lo que los experimentos con muones contradicen; también es un error comparar el tiempo de la Tierra (2.25 μs) con la vida propia (1.5 μs), porque son tiempos de sistemas distintos.",
        ],
    },
    # ============================================================
    # f-cuantica-nuclear — fotoeléctrico, vida media, defecto de masa y decaimiento
    # ============================================================
    {
        "id": "f-cuantica-nuclear-1",
        "node": "f-cuantica-nuclear",
        "kind": "problem",
        "level": 1,
        "title": "Luz ultravioleta sobre una placa metálica",
        "statement": (
            "Una placa metálica cuya función trabajo es **W = 2.5 eV** se ilumina con luz ultravioleta de "
            "longitud de onda **310 nm**. Los electrones arrancados se dirigen hacia un colector, y entre placa y "
            "colector se aplica una tensión que los frena. Usá **h·c = 1240 eV·nm**."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué energía tiene cada fotón incidente? Respondé solo con el número en eV.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "eV"},
                "answer": "4 eV",
            },
            {
                "prompt": "b) ¿Qué tensión de frenado mínima hace falta para que ningún electrón llegue al colector? Respondé solo con el número en V.",
                "check": {"type": "numeric", "value": 1.5, "tolerance": 0, "unit": "V"},
                "answer": "1.5 V",
            },
            {
                "prompt": "c) ¿Cuál es la longitud de onda umbral: la más larga que todavía arranca electrones de este metal? Respondé solo con el número en nm.",
                "check": {"type": "numeric", "value": 496, "tolerance": 0, "unit": "nm"},
                "answer": "496 nm",
            },
        ],
        "hints": [
            "`E = h·c/λ`; con `λ` en nm, `E = 1240/λ` da eV.",
            "Balance de energía: `E_fotón = W + K_máx`. Un electrón con energía `K` (en eV) se frena con una tensión de `K` voltios.",
            "En el umbral el fotón alcanza justo para arrancar el electrón, sin sobrante: `h·c/λ₀ = W`.",
        ],
        "solution": [
            "a) `E = 1240 eV·nm / 310 nm = 4 eV`.",
            "Energía cinética máxima de los electrones: `K_máx = E − W = 4 − 2.5 = 1.5 eV`.",
            "b) Para detener a los más rápidos, el campo tiene que quitarles `1.5 eV`: `e·V₀ = K_máx` → `V₀ = 1.5 V`. Con esa tensión la corriente se anula.",
            "c) Umbral: `1240/λ₀ = 2.5` → `λ₀ = 1240/2.5 = 496 nm` (luz verde-azulada). Longitudes de onda mayores (por ejemplo, luz roja) no arrancan electrones por más intensas que sean.",
            "Respuestas: 4 eV, 1.5 V y 496 nm. Error típico: creer que subir el brillo aumenta la tensión de frenado; la intensidad solo cambia cuántos electrones salen, no su energía máxima.",
        ],
    },
    {
        "id": "f-cuantica-nuclear-2",
        "node": "f-cuantica-nuclear",
        "kind": "problem",
        "level": 2,
        "title": "La dosis de tecnecio del centro de medicina nuclear",
        "statement": (
            "El tecnecio-99m es el radioisótopo más usado en centros de medicina nuclear para hacer centellogramas; "
            "su vida media es de **6 horas**. A las **8:00** la radiofarmacia prepara una dosis con una actividad de "
            "**800 MBq** (la actividad es proporcional a la cantidad de núcleos que quedan sin decaer)."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué actividad tiene la dosis a las 20:00 del mismo día? Respondé solo con el número en MBq.",
                "check": {"type": "numeric", "value": 200, "tolerance": 0, "unit": "MBq"},
                "answer": "200 MBq",
            },
            {
                "prompt": "b) ¿Cuántas horas después de preparada la actividad llega a 100 MBq? Respondé solo con el número en h.",
                "check": {"type": "numeric", "value": 18, "tolerance": 0, "unit": "h"},
                "answer": "18 h",
            },
            {
                "prompt": "c) A las 8:00 del día siguiente, ¿qué porcentaje de los núcleos de tecnecio iniciales ya decayó? Respondé solo con el número en %.",
                "check": {"type": "numeric", "value": 93.75, "tolerance": 0, "unit": "%"},
                "answer": "93.75 %",
            },
        ],
        "hints": [
            "Contá cuántas vidas medias entran en cada intervalo de tiempo; en cada una la cantidad se divide por 2.",
            "En c) la pregunta es por lo que DECAYÓ, no por lo que queda.",
        ],
        "solution": [
            "a) De 8:00 a 20:00 pasan 12 h = `12/6 = 2` vidas medias: `800 → 400 → 200 MBq` (queda `1/4`).",
            "b) `100/800 = 1/8 = (1/2)³`: hacen falta 3 vidas medias, o sea `3 × 6 = 18 h` (a las 2:00 de la madrugada).",
            "c) De 8:00 a 8:00 del día siguiente pasan 24 h = 4 vidas medias. Queda `(1/2)⁴ = 1/16` de los núcleos (50 MBq).",
            "Decayó `1 − 1/16 = 15/16 = 0.9375`, es decir, el `93.75 %`.",
            "Por eso el tecnecio se prepara el mismo día del estudio: se usa rápido y en un día decae más del 90 %, así que al día siguiente casi no queda actividad en el cuerpo del paciente. Error típico: suponer un decaimiento lineal (\"pierde 200 MBq cada 6 h\") y concluir que en 24 h se agota por completo.",
        ],
    },
    {
        "id": "f-cuantica-nuclear-3",
        "node": "f-cuantica-nuclear",
        "kind": "problem",
        "level": 3,
        "title": "La energía que libera una fuente de polonio",
        "statement": (
            "El polonio-210 decae emitiendo una partícula alfa: `²¹⁰Po → ²⁰⁶Pb + ⁴He`. Su vida media es de "
            "**138 días**. Masas atómicas: **Po-210 = 209.9829 u**, **Pb-206 = 205.9745 u**, **He-4 = 4.0026 u**. "
            "Equivalencias: **1 u ↔ 931.5 MeV**, **1 MeV = 1.6 × 10⁻¹³ J**. Una fuente contiene inicialmente "
            "**8 × 10¹⁸** núcleos de Po-210."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale el defecto de masa de cada desintegración? Respondé solo con el número en u.",
                "check": {"type": "numeric", "value": 0.0058, "tolerance": 0, "unit": "u"},
                "answer": "0.0058 u",
            },
            {
                "prompt": "b) ¿Qué energía libera cada desintegración? Redondeá a 1 decimal. Respondé solo con el número en MeV.",
                "check": {"type": "numeric", "value": 5.4, "tolerance": 0.01, "unit": "MeV"},
                "answer": "5.4 MeV (5.4027 MeV sin redondear)",
            },
            {
                "prompt": (
                    "c) Usando 5.4 MeV por desintegración, ¿cuánta energía liberó la fuente en total al cabo de "
                    "**414 días**? Respondé solo con el número en MJ (1 MJ = 10⁶ J)."
                ),
                "check": {"type": "numeric", "value": 6.048, "tolerance": 0.002, "unit": "MJ"},
                "answer": "6.048 MJ",
            },
        ],
        "hints": [
            "Defecto de masa: masa inicial menos la suma de las masas finales. Lo que \"falta\" se liberó como energía.",
            "Para c): ¿cuántas vidas medias son 414 días? Con eso sabés qué fracción de los núcleos ya decayó.",
            "Energía total = (cantidad de núcleos que decayeron) × (energía por desintegración), y después pasá de MeV a J.",
        ],
        "solution": [
            "a) `Δm = m(Po) − [m(Pb) + m(He)] = 209.9829 − (205.9745 + 4.0026) = 209.9829 − 209.9771 = 0.0058 u`. Al usar masas atómicas, los electrones se compensan (84 = 82 + 2).",
            "b) `Q = Δm · 931.5 MeV/u = 0.0058 × 931.5 = 5.4027 MeV ≈ 5.4 MeV`. Es positivo: la desintegración libera energía, que se lleva casi toda la partícula alfa como energía cinética.",
            "c) `414 / 138 = 3` vidas medias. Queda `(1/2)³ = 1/8` de los núcleos, así que decayó `7/8`: `N = (7/8) × 8 × 10¹⁸ = 7 × 10¹⁸` desintegraciones.",
            "Energía en MeV: `7 × 10¹⁸ × 5.4 MeV = 3.78 × 10¹⁹ MeV`.",
            "En joules: `3.78 × 10¹⁹ × 1.6 × 10⁻¹³ J = 6.048 × 10⁶ J = 6.048 MJ`.",
            "Verificación de orden de magnitud: unos 6 MJ equivalen a quemar unos 130 g de nafta, y salen de apenas unos 2.8 mg de polonio. Errores típicos: multiplicar por los 8 × 10¹⁸ núcleos iniciales (como si hubieran decaído todos) o por `1/8` (lo que queda) en lugar de `7/8`.",
        ],
    },
]
