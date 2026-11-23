"""Hands-on exercise pack: electronics mini projects and guitar practice routines.

Two items per topic (one short level-1 item and a more ambitious level-2/3 one). Every
electronics project runs in the free Wokwi simulator and on a real ESP32 DevKit at
3.3 V / 5 V only (the ones that fit its bench also run in AprendeLab's Arduino virtual); every guitar routine is measurable (bpm, repetitions, minutes) and
uses chord progressions instead of copyrighted songs.
"""

from __future__ import annotations

from typing import Any

_WOKWI_O_PLACA = "Simulador Wokwi (proyecto nuevo de ESP32) o ESP32 DevKit con cable USB de datos"
_VIRTUAL_WOKWI_O_PLACA = (
    "Arduino virtual de AprendeLab (Laboratorios → Electrónica → Arduino virtual), "
    "simulador Wokwi (proyecto nuevo de ESP32) o ESP32 DevKit con cable USB de datos"
)

ELECTRONICS: list[dict[str, Any]] = [
    # ------------------------------------------------------------------ e-ley-de-ohm
    {
        "id": "e-ley-de-ohm-1",
        "node": "e-ley-de-ohm",
        "kind": "project",
        "level": 1,
        "title": "LED rojo a 3.3 V con la resistencia justa",
        "statement": (
            "Vas a calcular la resistencia limitadora para un LED rojo alimentado con los `3.3 V` del ESP32 "
            "y a armar el circuito para verlo encendido. Sirve para fijar la fórmula "
            "`R = (V_fuente − V_led) / I` y la costumbre de elegir el valor comercial inmediato superior. "
            "Todavía no hace falta programar: la placa se usa solo como fuente."
        ),
        "materials": [
            _WOKWI_O_PLACA,
            "LED rojo (`Vf ≈ 2.0 V`)",
            "Resistencia del valor que calcules (serie E12)",
            "Protoboard y 2 cables (solo con hardware real)",
            "Papel y calculadora",
        ],
        "steps": [
            "En papel: calculá la resistencia para `I = 10 mA` con fuente de `3.3 V` y `Vf = 2.0 V`, usando `R = (3.3 − 2.0) / 0.010`.",
            "Elegí el valor comercial E12 igual o inmediato superior al resultado y recalculá la corriente real con `I = (3.3 − 2.0) / R_comercial`.",
            "Abrí el Laboratorio de Electrónica → Ley de Ohm, elegí `3.3V · ESP32`, LED rojo y `10 mA`, y compará la resistencia comercial y la corriente real con tus cuentas.",
            "Armá el circuito con la simulación detenida o el USB desconectado: pin `3V3` → resistencia → pata larga del LED (ánodo); pata corta (cátodo) → `GND`.",
            "Iniciá la simulación (no hace falta tocar el código de ejemplo) o conectá el USB: el LED tiene que quedar encendido fijo.",
            "Invertí el LED, comprobá que no enciende y volvé a dejarlo bien.",
        ],
        "done_when": [
            "Tu cuenta da `130 Ω` exactos y elegiste `150 Ω` como valor comercial.",
            "La corriente real que calculaste (≈ `8.7 mA`) coincide con la que muestra la calculadora del laboratorio.",
            "El LED enciende con la resistencia en serie y queda apagado al invertirlo.",
        ],
        "hints": [
            "Pasá los mA a A antes de dividir: `10 mA = 0.010 A`.",
            "Wokwi no simula la corriente de forma analógica: el LED se ve igual con cualquier resistencia. Por eso la cuenta se verifica con la calculadora del laboratorio y no mirando el brillo.",
            "Si tu kit no trae `150 Ω`, usá el siguiente valor que tengas hacia arriba (por ejemplo `220 Ω`, que da ≈ `5.9 mA`); nunca uno más chico que el calculado.",
        ],
        "lab_link": "electronics:ohm",
        "minutes": 15,
    },
    {
        "id": "e-ley-de-ohm-2",
        "node": "e-ley-de-ohm",
        "kind": "project",
        "level": 2,
        "title": "Tablero de tres LEDs: una resistencia para cada color",
        "statement": (
            "Cada color de LED tiene un voltaje directo distinto, así que cada uno pide su propia resistencia. "
            "Vas a diseñar y armar un tablero con un LED rojo, uno amarillo y uno verde siempre encendidos desde `3.3 V`, "
            "con una tabla de diseño que incluya resistencia exacta, valor comercial, corriente real y potencia. "
            "Es el mismo procedimiento que vas a repetir en cada proyecto que tenga un LED."
        ),
        "materials": [
            _WOKWI_O_PLACA,
            "LED rojo (`Vf ≈ 2.0 V`), LED amarillo (`Vf ≈ 2.1 V`) y LED verde (`Vf ≈ 2.2 V`)",
            "3 resistencias de los valores que calcules (serie E12)",
            "Protoboard y cables",
            "Papel y calculadora",
        ],
        "steps": [
            "Armá una tabla con una fila por LED y estas columnas: `Vf`, R exacta, R comercial (E12), corriente real y potencia en la resistencia.",
            "Calculá la R exacta de cada uno para `10 mA` desde `3.3 V` con `R = (3.3 − Vf) / 0.010`.",
            "Elegí para cada uno el valor E12 igual o inmediato superior y calculá la corriente real con `I = (3.3 − Vf) / R`.",
            "Calculá la potencia que disipa cada resistencia con `P = (3.3 − Vf) × I` y comparala con los `250 mW` que aguanta una resistencia común de 1/4 W.",
            "Sumá las tres corrientes reales: eso es lo que le pedís en total al pin `3V3`.",
            "Verificá cada fila en el Laboratorio de Electrónica → Ley de Ohm (fuente `3.3 V`, `10 mA`, cambiando el color del LED) y mirá las bandas de color de cada resistencia.",
            "Armá las tres ramas en paralelo entre `3V3` y `GND`, cada LED con SU resistencia en serie. Energizá y comprobá que prenden los tres.",
        ],
        "done_when": [
            "La tabla coincide con el laboratorio: rojo `130 Ω → 150 Ω`, amarillo `120 Ω → 120 Ω` y verde `110 Ω → 120 Ω`.",
            "Las corrientes reales te dan ≈ `8.7 mA`, `10.0 mA` y `9.2 mA`, y la suma queda cerca de `27.8 mA`.",
            "Las tres potencias quedan entre `10` y `12 mW`, muy lejos de los `250 mW`.",
            "Los tres LEDs encienden, cada uno con su propia resistencia (ninguna compartida).",
        ],
        "hints": [
            "No compartas una sola resistencia entre varios LEDs en paralelo: como cada color tiene distinto `Vf`, el de menor `Vf` se lleva casi toda la corriente.",
            "Bandas de color: `150 Ω` = marrón, verde, marrón; `120 Ω` = marrón, rojo, marrón.",
            "Si tu kit no tiene `120 Ω` ni `150 Ω`, usá `220 Ω` en los tres y rehacé la columna de corriente real: brillan un poco menos, pero es seguro.",
        ],
        "lab_link": "electronics:ohm",
        "minutes": 35,
    },
    # ------------------------------------------------------- e-protoboard-seguridad
    {
        "id": "e-protoboard-seguridad-1",
        "node": "e-protoboard-seguridad",
        "kind": "project",
        "level": 1,
        "title": "Cuatro experimentos seguros para entender la protoboard",
        "statement": (
            "Vas a armar un LED con su resistencia usando los rieles y las filas de la protoboard, y a modificar el "
            "circuito de cuatro maneras que no pueden dañar nada. Primero predecís y después comprobás: así te queda "
            "grabado cómo están unidos los huecos por dentro, para qué sirve la zanja y por qué importa la polaridad."
        ),
        "materials": [
            "Simulador Wokwi (ESP32 + protoboard) o ESP32 DevKit con protoboard y cable USB",
            "LED rojo",
            "Resistencia de `220 Ω`",
            "5 cables",
        ],
        "steps": [
            "Con el USB desconectado (o la simulación detenida), llevá `3V3` al riel rojo (+) y `GND` al riel azul (−) con un cable cada uno.",
            "Circuito base: riel + → resistencia de `220 Ω` → fila A; ánodo del LED (pata larga) en la fila A y cátodo en la fila B; un cable de la fila B al riel −. Energizá y comprobá que enciende.",
            "Antes de cada cambio anotá tu predicción (¿enciende o no?) y desconectá el USB o detené la simulación. Experimento 1: invertí el LED.",
            "Experimento 2: con el LED otra vez al derecho, mové el ánodo a otro hueco de la MISMA fila A.",
            "Experimento 3: mové el ánodo a la fila que queda enfrente, del otro lado de la zanja central.",
            "Experimento 4: sin mover el LED, agregá un cable que cruce la zanja y una esa fila con la fila A.",
            "Escribí al lado de cada experimento la causa en una frase y volvé a dejar el circuito base.",
        ],
        "done_when": [
            "El circuito base enciende usando los dos rieles (ningún cable va directo de la placa al LED).",
            "Comprobaste los cuatro resultados: invertido = apagado; otro hueco de la misma fila = encendido; del otro lado de la zanja = apagado; con el puente sobre la zanja = encendido.",
            "Hiciste cada cambio con el USB desconectado o la simulación detenida.",
            "Anotaste la causa de cada resultado (polaridad, 5 huecos unidos, zanja que aísla, cable que une).",
        ],
        "hints": [
            "Si el circuito base no enciende, revisá que las dos patas de la resistencia estén en filas distintas: en la misma fila queda puenteada.",
            "En todos los experimentos la resistencia sigue en serie, por eso ninguno es peligroso: con `220 Ω` el LED rojo recibe ≈ `5.9 mA`.",
            "En muchas protoboards largas los rieles están cortados al medio: si media placa queda sin alimentación, uní las dos mitades con un cable.",
        ],
        "lab_link": "electronics:pinout",
        "minutes": 15,
    },
    {
        "id": "e-protoboard-seguridad-2",
        "node": "e-protoboard-seguridad",
        "kind": "project",
        "level": 2,
        "title": "Dos rieles, dos tensiones: testigos de 3.3 V y de 5 V",
        "statement": (
            "Vas a preparar una protoboard con un riel de `3.3 V` y otro de `5 V`, cada uno con un LED testigo calculado "
            "para su tensión, y a diseñar el divisor que haría falta para que una señal de `5 V` pueda entrar a un GPIO. "
            "Es la base ordenada sobre la que se montan los proyectos que siguen, y te entrena en la regla que salva "
            "placas: **ningún GPIO del ESP32 recibe 5 V**."
        ),
        "materials": [
            "Simulador Wokwi (ESP32 + protoboard) o ESP32 DevKit con protoboard y cable USB",
            "2 LEDs rojos (`Vf ≈ 2.0 V`)",
            "2 resistencias de los valores que calcules (serie E12)",
            "Cables de dos colores para distinguir `3.3 V` de `5 V`, y negros para GND",
            "Multímetro (opcional, solo con hardware real)",
            "Papel y calculadora",
        ],
        "steps": [
            "Con el USB desconectado, cableá: pin `3V3` → riel rojo de arriba; pin `VIN` (o `5V`, según la placa) → riel rojo de abajo; `GND` → un riel azul, y uní los dos rieles azules con un cable (tierra común).",
            "Calculá la resistencia de cada testigo para `10 mA` con `R = (V_fuente − 2.0) / 0.010`: una vez con `3.3 V` y otra con `5 V`. Elegí los valores E12 inmediatos superiores y calculá la corriente real de cada uno.",
            "Armá los dos testigos, cada uno entre su riel + y el riel −, con su resistencia en serie y la pata larga del LED hacia el +.",
            "Diseñá en papel un divisor para una señal de `5 V` con `R1 = 1 kΩ` (hacia la señal) y `R2 = 2 kΩ` (hacia GND): `V_out = 5 × R2 / (R1 + R2)`. Comprobalo en el Laboratorio de Electrónica → Ley de Ohm, sección Divisor Resistivo.",
            "En el mismo simulador subí R2 a `2.5 kΩ` dejando R1 en `1 kΩ` y anotá por qué ese divisor ya no sirve para un ESP32.",
            "Checklist antes de energizar: polaridad de los dos LEDs, GND común, cada resistencia con sus patas en filas distintas y ningún cable del riel de `5 V` tocando un pin GPIO.",
            "Conectá el USB o iniciá la simulación: tienen que encender los dos testigos.",
            "Solo con hardware real y multímetro: medí tensión continua entre cada riel + y GND. Lo esperable es ≈ `3.3 V` en uno y entre `4.5` y `5.1 V` en el otro.",
        ],
        "done_when": [
            "Los dos testigos encienden: el de `3.3 V` con `150 Ω` y el de `5 V` con `330 Ω` (o los valores superiores que tengas).",
            "Calculaste la corriente real de cada uno (≈ `8.7 mA` y ≈ `9.1 mA`): por eso brillan parecido aunque las tensiones sean distintas.",
            "Tu divisor da `V_out ≈ 3.33 V` y el laboratorio lo marca como seguro; con `R2 = 2.5 kΩ` da ≈ `3.57 V` y lo marca en peligro.",
            "Ningún cable une el riel de `5 V` con un GPIO, y los dos rieles − están unidos entre sí.",
        ],
        "hints": [
            "El DevKit es ancho: en una protoboard común tapa casi todos los huecos y deja libre una sola hilera de un lado. Podés montarlo a caballo de dos protoboards o usar cables macho-hembra.",
            "Etiquetá el riel de `5 V` con cinta o con un color de cable propio: el error que quema placas es confundirlo con el de `3.3 V`.",
            "Un divisor resistivo sirve para señales (corrientes muy chicas), no para alimentar módulos: no lo uses como fuente de `3.3 V`.",
        ],
        "lab_link": "electronics:ohm",
        "minutes": 40,
    },
    # ----------------------------------------------------------------- e-blink-wokwi
    {
        "id": "e-blink-wokwi-1",
        "node": "e-blink-wokwi",
        "kind": "project",
        "level": 1,
        "title": "Latido de corazón con el LED de GPIO 2",
        "statement": (
            "Vas a programar el LED de `GPIO 2` para que haga un latido: dos destellos cortos y una pausa, una vez por "
            "segundo, y a contar los latidos por el Monitor Serial. Practicás lo esencial del tema: qué va en `setup()`, "
            "qué va en `loop()` y cómo se arma un ritmo con `digitalWrite()` y `delay()`."
        ),
        "materials": [
            _VIRTUAL_WOKWI_O_PLACA,
            "LED rojo y resistencia de `220 Ω` (en la placa real podés usar el LED integrado, que ya está en `GPIO 2`)",
            "Cronómetro o celular",
        ],
        "steps": [
            "Si usás LED externo: `GPIO 2` → resistencia de `220 Ω` → ánodo del LED; cátodo → `GND`.",
            "Definí el pin como constante arriba de todo. En `setup()` iniciá el puerto serie con `Serial.begin(115200)` y configurá el pin con `pinMode(LED_PIN, OUTPUT)`.",
            "En `loop()` armá el latido con cuatro tiempos que sumen `1000 ms`: encendido `100`, apagado `150`, encendido `100`, apagado `650`.",
            "Declará una variable global que cuente latidos; al final de cada latido sumale 1 e imprimila con `Serial.println()`.",
            "Ejecutá y cronometrá 10 segundos mientras mirás el contador.",
            "Variación: cambiá solo la última pausa para que el corazón lata 120 veces por minuto (un latido cada `500 ms`) y volvé a cronometrar.",
        ],
        "done_when": [
            "Se ven claramente dos destellos seguidos y después una pausa más larga.",
            "En 10 segundos de cronómetro el contador avanza 10 latidos (±1).",
            "El Monitor Serial a `115200` muestra el contador legible, sin símbolos raros.",
            "En la variación, con la última pausa en `150 ms`, el contador avanza 20 latidos (±1) en 10 segundos.",
        ],
        "hints": [
            "En el Arduino virtual el LED está en `D13`: usá `LED_PIN = 13`. Con el osciloscopio en `100 ms/div` ves los dos destellos y podés medir cada tiempo con el cursor.",
            "Si el LED no enciende o apenas brilla, revisá que no falte `pinMode(LED_PIN, OUTPUT)` en `setup()`.",
            "Símbolos raros en el Monitor Serial = el monitor está en una velocidad distinta de `115200`.",
            "Los cuatro `delay()` tienen que sumar el período del latido: `100 + 150 + 100 + 650 = 1000 ms`.",
        ],
        "lab_link": "electronics:arduino:serial-blink",
        "minutes": 15,
    },
    {
        "id": "e-blink-wokwi-2",
        "node": "e-blink-wokwi",
        "kind": "project",
        "level": 2,
        "title": "Semáforo de tres luces con secuencia cronometrada",
        "statement": (
            "Vas a construir un semáforo con tres LEDs que recorre cuatro fases con tiempos exactos y anuncia cada una "
            "por el Monitor Serial. Aprendés a manejar varias salidas a la vez, a ordenar el código con constantes y una "
            "función auxiliar, y a verificar un programa midiendo con cronómetro en vez de 'a ojo'."
        ),
        "materials": [
            _WOKWI_O_PLACA,
            "LED rojo, LED amarillo y LED verde",
            "3 resistencias de `220 Ω`",
            "Protoboard y 4 cables",
            "Cronómetro o celular",
        ],
        "steps": [
            "Cableá cada LED con su resistencia de `220 Ω` en serie: rojo en `GPIO 18`, amarillo en `GPIO 19` y verde en `GPIO 23`; los tres cátodos a `GND`.",
            "Declará tres constantes de pin y cuatro constantes de tiempo en ms: verde `4000`, amarillo `1000`, rojo `4000` y rojo + amarillo `1000`.",
            "En `setup()`: `Serial.begin(115200)` y un `pinMode(..., OUTPUT)` por cada LED.",
            "Escribí una función auxiliar que reciba tres valores (rojo, amarillo, verde) y haga los tres `digitalWrite()`: así cada fase se enciende con una sola línea.",
            "En `loop()` encadená las cuatro fases en orden: verde → amarillo → rojo → rojo + amarillo. En cada una imprimí su nombre con `Serial.println()` y esperá con `delay()`.",
            "Cronometrá 3 ciclos completos, de verde a verde.",
            "Experimento de diagnóstico: comentá el `pinMode()` del LED verde, ejecutá, anotá qué cambia y volvé a dejarlo como estaba.",
        ],
        "done_when": [
            "La secuencia es verde → amarillo → rojo → rojo + amarillo y se repite sola.",
            "Nunca quedan encendidos el verde y el rojo al mismo tiempo.",
            "Tres ciclos completos duran 30 segundos (±1 s).",
            "El Monitor Serial muestra el nombre de cada fase en el momento en que cambian las luces.",
            "Sin su `pinMode()` el LED verde no enciende (o apenas brilla), y lo dejaste anotado.",
        ],
        "hints": [
            "El error típico es prender la luz nueva sin apagar la anterior: la función que escribe los tres pines a la vez lo evita.",
            "`GPIO 18`, `19` y `23` no tienen restricciones de arranque. No uses `GPIO 34` a `39` para LEDs: son solo entrada.",
            "Con `220 Ω` cada LED recibe entre 5 y 6 mA: se ve bien y queda muy lejos del límite del pin.",
        ],
        "lab_link": "electronics:pinout",
        "minutes": 40,
    },
    # ------------------------------------------------------------- e-entradas-pullup
    {
        "id": "e-entradas-pullup-1",
        "node": "e-entradas-pullup",
        "kind": "project",
        "level": 1,
        "title": "Pulsador que avisa solo cuando cambia",
        "statement": (
            "Vas a leer un pulsador con `INPUT_PULLUP` y a imprimir un mensaje únicamente en el instante en que se "
            "presiona o se suelta, en vez de inundar el Monitor Serial. Practicás el cableado a GND, la lógica invertida "
            "(presionado = `LOW`) y la detección de cambios, que es la base de cualquier botón bien leído."
        ),
        "materials": [
            _VIRTUAL_WOKWI_O_PLACA,
            "Pulsador",
            "2 cables y protoboard",
            "LED integrado de `GPIO 2` (o LED rojo con resistencia de `220 Ω`)",
        ],
        "steps": [
            "Conectá el pulsador entre `GPIO 4` y `GND`, sin ninguna resistencia externa. En un pulsador de 4 patas usá dos patas en diagonal para no errarle.",
            "En `setup()`: `Serial.begin(115200)`, `pinMode(4, INPUT_PULLUP)` y el LED de `GPIO 2` como `OUTPUT`.",
            "Primero mirá el dato crudo: en `loop()` imprimí `digitalRead(4)` con un `delay(200)` y anotá qué número aparece con el botón suelto y cuál presionado.",
            "Ahora guardá la lectura anterior en una variable global. En cada vuelta leé el pin y compará: solo si cambió, imprimí `PRESIONADO` (si pasó a `LOW`) o `SUELTO` (si pasó a `HIGH`) y actualizá la variable.",
            "Hacé que el LED acompañe: encendido mientras el botón está presionado y apagado cuando está suelto.",
            "Si una sola pulsación imprime varias líneas, agregá un `delay(30)` justo después de detectar el cambio (antirrebote simple) y volvé a probar.",
        ],
        "done_when": [
            "Con el botón suelto se lee `1` y presionado `0`, y no hay ninguna resistencia externa en el circuito.",
            "Sin tocar el botón, el Monitor Serial queda quieto: no aparece ninguna línea nueva durante 10 segundos.",
            "10 pulsaciones producen exactamente 10 líneas `PRESIONADO` y 10 líneas `SUELTO`.",
            "El LED está encendido solo mientras mantenés apretado el botón.",
        ],
        "hints": [
            "Con `INPUT_PULLUP` la lógica va al revés de la intuición: presionado es `LOW`. Si tu LED prende al soltar, la condición está invertida.",
            "No uses `GPIO 34` a `39` para el botón: son solo entrada y no tienen pull-up interno.",
            "En Wokwi y en el Arduino virtual el pulsador imita el rebote mecánico de uno real, así que las líneas repetidas también aparecen en el simulador.",
            "En el Arduino virtual el pulsador está en `D2` y el LED en `D13`: usá esos números en lugar de `GPIO 4` y `GPIO 2`. Para ver el rebote, activá el «Disparo único» del osciloscopio con `0,5 ms/div`.",
        ],
        "lab_link": "electronics:arduino:pullup",
        "minutes": 20,
    },
    {
        "id": "e-entradas-pullup-2",
        "node": "e-entradas-pullup",
        "kind": "project",
        "level": 2,
        "title": "Lámpara de toque con contador y botón de reinicio",
        "statement": (
            "Vas a construir una lámpara que cambia de estado con cada toque (uno prende, el siguiente apaga), cuenta las "
            "pulsaciones y tiene un segundo botón que la reinicia. Es el paso de 'el LED copia al botón' a 'el botón "
            "dispara un evento', y te obliga a resolver bien el flanco y el rebote con dos entradas `INPUT_PULLUP` a la vez."
        ),
        "materials": [
            _WOKWI_O_PLACA,
            "2 pulsadores",
            "LED (rojo, amarillo o verde) y resistencia de `220 Ω`",
            "Protoboard y cables",
        ],
        "steps": [
            "Cableá: pulsador A entre `GPIO 4` y `GND`, pulsador B entre `GPIO 19` y `GND`, y el LED con su resistencia de `220 Ω` en `GPIO 18`.",
            "Configurá los dos botones con `INPUT_PULLUP` y el LED como `OUTPUT`. Declará variables globales para el estado de la lámpara, el contador de toques y la lectura anterior de cada botón.",
            "Detectá el flanco de bajada del botón A: la lectura anterior era `HIGH` y la actual es `LOW`. Solo en ese instante invertí el estado de la lámpara, sumá 1 al contador y escribí el LED.",
            "Agregá el antirrebote: después de un flanco válido esperá unos `30 ms` antes de volver a leer.",
            "Imprimí por Serial una línea por toque con el contador y el estado (`ON` u `OFF`).",
            "Con el mismo método, hacé que un flanco de bajada en el botón B apague la lámpara, ponga el contador en 0 e imprima `REINICIO`.",
            "Pruebas: reiniciá y hacé 20 toques seguidos; después un toque mantenido 3 segundos; y por último reiniciá con la lámpara encendida.",
        ],
        "done_when": [
            "Cada toque del botón A cambia la lámpara una sola vez, aunque lo mantengas apretado 3 segundos.",
            "Partiendo de un reinicio, después de 20 toques el contador marca exactamente 20 y la lámpara queda apagada.",
            "El botón B apaga la lámpara y vuelve el contador a 0 en cualquier momento.",
            "No hay resistencias externas en los botones, y los dos se detectan por flanco (comparando con la lectura anterior).",
        ],
        "hints": [
            "Si un toque cuenta 2 o 3 veces, es rebote: subí la espera a `50 ms`.",
            "Si la lámpara parpadea rapidísimo mientras mantenés apretado, estás actuando por nivel (`== LOW`) y no por flanco.",
            "Actualizá la variable de lectura anterior en TODAS las vueltas de `loop()`, no solo cuando hay flanco.",
        ],
        "lab_link": "electronics:debug",
        "minutes": 45,
    },
    # ------------------------------------------------------------------ e-analog-pwm
    {
        "id": "e-analog-pwm-1",
        "node": "e-analog-pwm",
        "kind": "project",
        "level": 1,
        "title": "Voltímetro de potenciómetro por Serial",
        "statement": (
            "Vas a leer un potenciómetro con el ADC del ESP32 y a mostrar por el Monitor Serial el valor crudo, el "
            "voltaje y el porcentaje de giro. Sirve para entender qué significa el rango `0..4095` antes de usarlo para "
            "controlar algo, y para acostumbrarte a elegir un pin de ADC1."
        ),
        "materials": [
            _VIRTUAL_WOKWI_O_PLACA,
            "Potenciómetro de `10 kΩ`",
            "3 cables y protoboard",
        ],
        "steps": [
            "Cableá el potenciómetro: un extremo a `3V3`, el otro extremo a `GND` y la pata del medio (cursor) a `GPIO 34`. Nunca lo alimentes desde `VIN` (5 V).",
            "En `loop()` leé `analogRead(34)` y guardalo en una variable entera.",
            "Convertilo a voltaje con decimales: `float voltios = crudo * 3.3 / 4095.0;`",
            "Calculá el porcentaje de giro con `map(crudo, 0, 4095, 0, 100)`.",
            "Imprimí los tres datos en una sola línea cada `250 ms` (acá alcanza con un `delay(250)`).",
            "Girá de punta a punta y después dejalo al medio: anotá los tres valores en cada posición.",
        ],
        "done_when": [
            "En un extremo se lee cerca de `0` y en el otro cerca de `4095` (≈ `3.3 V`).",
            "Con el cursor al medio el crudo queda entre `1800` y `2300`, y el voltaje y el porcentaje impresos son coherentes con ese crudo (por ejemplo `2048` → `1.65 V` → `50`).",
            "El valor sube o baja de forma continua al girar, sin saltos al azar.",
            "El cursor está en un pin de ADC1 (`GPIO 32` a `39`) y no en `GPIO 4`.",
        ],
        "hints": [
            "En el Arduino virtual el potenciómetro está en `A0` y el Nano mide `0..1023` con `5 V`: usá `analogRead(A0)`, `crudo * 5.0 / 1023.0` y `map(crudo, 0, 1023, 0, 100)`. Al medio se lee ≈ `512` → `2.50 V` → `50`.",
            "Si dividís por `4095` (entero) con una variable entera perdés los decimales: usá `4095.0` y guardá el resultado en un `float`.",
            "Lecturas que saltan al azar = cursor desconectado (pin flotante) o algún extremo del potenciómetro sin cablear.",
            "En la placa real el ADC del ESP32 no es perfectamente lineal: satura un poco antes de los extremos y el punto medio puede leerse algo corrido. En Wokwi es ideal.",
        ],
        "lab_link": "electronics:arduino:pote",
        "minutes": 20,
    },
    {
        "id": "e-analog-pwm-2",
        "node": "e-analog-pwm",
        "kind": "project",
        "level": 2,
        "title": "Luz nocturna automática con sensor de luz",
        "statement": (
            "Vas a construir una luz que se enciende sola cuando oscurece: un sensor de luz (LDR) entra por el ADC y un "
            "LED responde con PWM, más brillante cuanto menos luz hay. Combina las dos mitades del tema —leer el mundo "
            "analógico y dosificar potencia— y te hace calibrar con tus propias mediciones en vez de usar números de memoria."
        ),
        "materials": [
            _WOKWI_O_PLACA,
            "Sensor de luz: módulo fotorresistor de Wokwi, o una LDR con una resistencia de `10 kΩ`",
            "LED rojo o amarillo y resistencia de `220 Ω`",
            "Protoboard y cables",
        ],
        "steps": [
            "Sensor con hardware real: LDR entre `3V3` y el punto medio, resistencia de `10 kΩ` entre el punto medio y `GND`, y el punto medio a `GPIO 34`. En Wokwi: módulo fotorresistor con `VCC` a `3V3`, `GND` a `GND` y `AO` a `GPIO 34`.",
            "Conectá el LED con su resistencia de `220 Ω` en `GPIO 18`.",
            "Calibración: imprimí `analogRead(34)` cada `200 ms` y anotá dos números: la lectura con luz plena (`LUZ`) y la lectura con el sensor tapado (`OSCURO`). En Wokwi se cambia con el control de lux del sensor.",
            "Convertí la lectura en brillo con `map(crudo, OSCURO, LUZ, 255, 0)` y limitá el resultado con `constrain(brillo, 0, 255)`.",
            "Aplicá el brillo con `analogWrite(18, brillo)`.",
            "Imprimí en cada vuelta el crudo, el brillo y el duty cycle en % (`brillo * 100 / 255`).",
            "Probá cinco niveles de luz, de plena a tapado, y anotá el duty de cada uno.",
            "Ajuste fino: hacé que por debajo de un duty de 10 % (brillo menor a `26`) el LED quede totalmente apagado.",
        ],
        "done_when": [
            "Con luz plena el LED está apagado y con el sensor tapado queda al máximo (duty de 95 % o más).",
            "Al oscurecer de a poco el brillo sube de forma gradual: distinguís al menos 4 niveles intermedios.",
            "El Monitor Serial muestra crudo, brillo (siempre entre `0` y `255`) y duty en %, y los tres se mueven de forma coherente.",
            "Las constantes `LUZ` y `OSCURO` salen de tus propias mediciones y las tenés anotadas.",
            "El sensor está en ADC1 (`GPIO 34`), así que seguiría funcionando si mañana sumás Wi-Fi.",
        ],
        "hints": [
            "No importa si tu sensor entrega más voltaje con luz o con oscuridad (depende de cómo quede armado el divisor): al usar tus dos lecturas medidas en `map()`, la cuenta sale bien en los dos casos.",
            "Sin `constrain()`, una lectura fuera del rango calibrado da brillos negativos o mayores a 255 y el LED hace cosas raras.",
            "`GPIO 34` es solo entrada: perfecto para el sensor, inservible para el LED.",
        ],
        "lab_link": "electronics:pinout",
        "minutes": 50,
    },
    # ----------------------------------------------------------- e-millis-multitarea
    {
        "id": "e-millis-multitarea-1",
        "node": "e-millis-multitarea",
        "kind": "project",
        "level": 1,
        "title": "Dos LEDs, dos relojes",
        "statement": (
            "Vas a hacer parpadear dos LEDs a ritmos distintos (uno cambia cada `300 ms` y el otro cada `1000 ms`) sin "
            "usar `delay()`. Es el ejercicio mínimo para comprobar que entendiste el patrón de `millis()`: una marca de "
            "tiempo por tarea y un `loop()` que nunca se queda esperando."
        ),
        "materials": [
            _WOKWI_O_PLACA,
            "2 LEDs (rojo, amarillo o verde)",
            "2 resistencias de `220 Ω`",
            "Protoboard y cables",
        ],
        "steps": [
            "Cableá un LED con su resistencia de `220 Ω` en `GPIO 18` y el otro en `GPIO 19`.",
            "Declará, para cada LED, una marca de tiempo `unsigned long` y una variable de estado. Los intervalos van como constantes: `300` y `1000`.",
            "Al empezar `loop()` guardá una sola vez el tiempo actual: `unsigned long ahora = millis();`",
            "Escribí el bloque del LED rápido: si `ahora - ultimoA >= 300`, actualizá la marca, invertí el estado y escribí el pin.",
            "Copiá el bloque para el LED lento, con SUS variables y el intervalo de `1000`.",
            "Dentro de cada bloque imprimí qué LED cambió y el valor de `ahora`, para medir los intervalos reales en el Monitor Serial.",
            "Buscá la palabra `delay` en el sketch: no tiene que aparecer en ningún lado.",
        ],
        "done_when": [
            "El LED lento cambia de estado 10 veces en 10 segundos (±1), y el rápido cambia más de 3 veces por cada cambio del lento.",
            "En el Monitor Serial, la diferencia entre dos marcas seguidas del mismo LED es `300` o `1000 ms` (±5 ms).",
            "El sketch no contiene ningún `delay()`.",
            "Las marcas de tiempo están declaradas como `unsigned long`.",
        ],
        "hints": [
            "Si un LED queda parpadeando rapidísimo, te olvidaste de actualizar su marca de tiempo dentro del `if`.",
            "Si los dos LEDs cambian siempre juntos, están compartiendo la misma variable de tiempo: cada tarea necesita la suya.",
            "Compará siempre con resta (`ahora - ultimo >= intervalo`), nunca con `ahora >= ultimo + intervalo`.",
        ],
        "lab_link": "electronics:debug",
        "minutes": 20,
    },
    {
        "id": "e-millis-multitarea-2",
        "node": "e-millis-multitarea",
        "kind": "project",
        "level": 3,
        "title": "Semáforo con botón peatonal que nunca se cuelga",
        "statement": (
            "Vas a programar un semáforo como una máquina de estados con `millis()`: los autos tienen verde hasta que un "
            "peatón aprieta el botón, y el pedido se registra al instante en cualquier momento del ciclo. Mientras tanto, "
            "el LED de `GPIO 2` late cada medio segundo como prueba de que `loop()` nunca se bloquea. Es el salto de "
            "'una secuencia con `delay()`' a 'varias tareas a la vez', que es como se programan los proyectos reales."
        ),
        "materials": [
            _WOKWI_O_PLACA,
            "LED rojo, LED amarillo y LED verde",
            "3 resistencias de `220 Ω`",
            "Pulsador",
            "LED integrado de `GPIO 2` (o un LED extra con resistencia de `220 Ω`)",
            "Protoboard y cables",
            "Cronómetro o celular",
        ],
        "steps": [
            "Cableá: rojo en `GPIO 18`, amarillo en `GPIO 19` y verde en `GPIO 23` (cada uno con `220 Ω`); pulsador entre `GPIO 4` y `GND` con `INPUT_PULLUP`; y el LED de `GPIO 2` como latido.",
            "Tarea 1, latido: con su propia marca de tiempo, invertí `GPIO 2` cada `500 ms`. Probala sola antes de seguir.",
            "Tarea 2, botón: en cada vuelta leé el pulsador; ante un flanco de bajada poné en verdadero una variable `pedido` e imprimí `PEDIDO` junto con el valor de `millis()`.",
            "Tarea 3, semáforo: definí tres estados (`VERDE`, `AMARILLO`, `ROJO`), una variable con el estado actual y otra `unsigned long` con el momento en que empezó.",
            "Escribí las transiciones: de `VERDE` se sale solo si hay `pedido` Y ya pasaron al menos `5000 ms` de verde; `AMARILLO` dura `2000 ms`; `ROJO` dura `5000 ms` y al terminar vuelve a `VERDE` y borra el `pedido`.",
            "Al entrar a cada estado: guardá el momento de entrada, escribí los tres LEDs e imprimí el nombre del estado.",
            "Pruebas: (a) sin tocar nada durante 30 segundos; (b) botón a los 2 segundos de empezado el verde; (c) botón durante el amarillo y durante el rojo; (d) botón mantenido apretado.",
            "Revisión final: el sketch no tiene ningún `delay()`. Si necesitás antirrebote, también se hace comparando tiempos.",
        ],
        "done_when": [
            "Sin apretar el botón, el semáforo se queda en verde y el LED de latido sigue cambiando cada `500 ms`.",
            "Si apretás con más de 5 s de verde, el amarillo aparece de inmediato; si apretás a los 2 s, aparece recién al cumplirse los 5 s.",
            "El amarillo dura 2 s y el rojo 5 s (±0.5 s, medidos con cronómetro).",
            "`PEDIDO` aparece en el Monitor Serial en el instante de cada pulsación, también durante el amarillo y el rojo.",
            "El latido de `GPIO 2` no se frena en ningún momento del ciclo y el sketch no contiene `delay()`.",
        ],
        "hints": [
            "Usá un `enum` (o tres constantes) para los estados y un `switch`: una rama por estado, y en cada rama solo la pregunta '¿ya pasó el tiempo?'.",
            "Si `PEDIDO` sale repetido por el rebote, ignorá los flancos que lleguen a menos de `50 ms` del anterior, usando otra marca de tiempo.",
            "Sumá las tareas de a una: si el latido se frena al agregar algo, ese algo está bloqueando.",
        ],
        "lab_link": "electronics:debug",
        "minutes": 75,
    },
    # ---------------------------------------------------------------- e-i2c-sensores
    {
        "id": "e-i2c-sensores-1",
        "node": "e-i2c-sensores",
        "kind": "project",
        "level": 1,
        "title": "Mapa del bus: dos módulos, dos direcciones",
        "statement": (
            "Vas a colgar dos módulos I2C de los mismos dos cables y a usar el I2C Scanner para armar el mapa de "
            "direcciones de tu bus. Comprobás con tus ojos la idea central del tema —un bus compartido donde cada módulo "
            "responde por su dirección— y te queda el procedimiento de diagnóstico que vas a repetir con cada módulo nuevo."
        ),
        "materials": [
            _WOKWI_O_PLACA,
            "Pantalla OLED SSD1306 I2C",
            "Un segundo módulo I2C distinto (en Wokwi: MPU6050; con hardware real, el que tengas)",
            "Protoboard y cables",
            "Código del I2C Scanner (Laboratorio de Electrónica → Proyectos → Iteración 03)",
        ],
        "steps": [
            "Con la alimentación desconectada, cableá la OLED: `VCC` → `3V3`, `GND` → `GND`, `SDA` → `GPIO 21` y `SCL` → `GPIO 22`.",
            "Cargá el I2C Scanner del laboratorio, ejecutalo y anotá la dirección que aparece.",
            "Sumá el segundo módulo en paralelo sobre las mismas líneas: su `SDA` también a `GPIO 21` y su `SCL` también a `GPIO 22`, más `3V3` y `GND`.",
            "Reiniciá la placa (el scanner corre una sola vez, en `setup()`) y anotá las direcciones que aparecen ahora.",
            "Experimento: intercambiá los cables de `SDA` y `SCL` de UN solo módulo, reiniciá y mirá cuál deja de aparecer. Después dejalo bien.",
            "Armá tu tabla del bus: dirección en hexadecimal → módulo.",
        ],
        "done_when": [
            "Con los dos módulos conectados el scanner lista 2 direcciones distintas (en Wokwi: `0x3C` para la OLED y `0x68` para el MPU6050).",
            "Los dos módulos comparten `GPIO 21` y `GPIO 22`: no usaste ningún otro pin de datos.",
            "Con `SDA` y `SCL` cruzados, ese módulo deja de aparecer en el scanner; al corregirlo vuelve a aparecer.",
            "Tenés anotada la tabla dirección → módulo.",
        ],
        "hints": [
            "Si el scanner no encuentra nada, revisá primero alimentación y GND común, y después que `SDA` y `SCL` no estén cruzados.",
            "Dos módulos iguales tienen la misma dirección y chocan en el bus: por eso se combinan módulos distintos, o se cambia la dirección con el puente que traen algunos.",
            "Alimentá los módulos desde `3V3`: con 5 V, sus líneas de datos pueden llegar con 5 V a los GPIO del ESP32.",
        ],
        "lab_link": "electronics:projects",
        "minutes": 20,
    },
    {
        "id": "e-i2c-sensores-2",
        "node": "e-i2c-sensores",
        "kind": "project",
        "level": 3,
        "title": "Nivel de burbuja digital (MPU6050 + OLED)",
        "statement": (
            "Vas a construir un nivel de burbuja electrónico: un acelerómetro MPU6050 mide la inclinación y una pantalla "
            "OLED muestra el ángulo en grados y una burbuja que se mueve. Los dos módulos comparten el bus I2C, así que "
            "practicás direcciones, librerías y refresco sin `delay()` en un instrumento que podés usar de verdad para "
            "nivelar un estante."
        ),
        "materials": [
            _WOKWI_O_PLACA,
            "Pantalla OLED SSD1306 de 128×64 I2C",
            "Módulo acelerómetro MPU6050 (GY-521)",
            "Protoboard y cables",
            "Librerías Adafruit SSD1306, Adafruit GFX y Adafruit MPU6050",
        ],
        "steps": [
            "Cableá los dos módulos al mismo bus: `VCC` → `3V3`, `GND` → `GND`, `SDA` → `GPIO 21` y `SCL` → `GPIO 22`.",
            "Corré el I2C Scanner y confirmá las dos direcciones antes de escribir una sola línea más (lo esperable: `0x3C` y `0x68`).",
            "Inicializá la pantalla con la dirección detectada y mostrá un texto fijo de prueba. Si la inicialización falla, avisá por Serial y no sigas.",
            "Inicializá el MPU6050 e imprimí por Serial la aceleración en X y en Z cada `100 ms`, temporizando con `millis()`.",
            "Calculá la inclinación en grados: `float angulo = atan2(ax, az) * 180.0 / PI;`",
            "Mostrá el ángulo en la OLED con un decimal y texto grande, refrescando cada `100 ms`.",
            "Dibujá la burbuja: un círculo cuya posición horizontal salga de un `map()` de `−45..45` grados a `0..127` píxeles (limitado con `constrain`), más una marca fija en el centro de la pantalla.",
            "Agregá el aviso de nivelado: cuando el ángulo esté entre `−1°` y `+1°`, mostrá el cartel `NIVELADO`.",
            "Probá: en Wokwi hacé click en el MPU6050 y cambiá la aceleración en X y en Z; con hardware real, apoyalo en la mesa e inclinalo de a poco.",
        ],
        "done_when": [
            "El scanner detecta los dos módulos y el código usa exactamente esas direcciones.",
            "Apoyado plano (X = `0`, Z = `1 g`) la pantalla marca entre `−2°` y `+2°` y la burbuja queda sobre la marca central.",
            "Con X igual a Z (por ejemplo `0.7 g` y `0.7 g`) marca cerca de `45°`, y con el signo de X invertido, cerca de `−45°`.",
            "La pantalla se actualiza unas 10 veces por segundo y `loop()` no usa `delay()`.",
            "El cartel `NIVELADO` aparece solo dentro de ±1°.",
        ],
        "hints": [
            "Pantalla en negro con el scanner funcionando = dirección equivocada en el código (`0x3C` vs `0x3D`), no un problema de cables.",
            "Las funciones de dibujo solo escriben en memoria: sin la llamada final a `display()` no se ve nada en la pantalla.",
            "Borrá la pantalla con `clearDisplay()` al empezar cada refresco, o la burbuja va a dejar rastro.",
        ],
        "lab_link": "electronics:projects",
        "minutes": 90,
    },
    # -------------------------------------------------------------- e-esp32-wifi-iot
    {
        "id": "e-esp32-wifi-iot-1",
        "node": "e-esp32-wifi-iot",
        "kind": "project",
        "level": 1,
        "title": "Testigo de conexión Wi-Fi con timeout",
        "statement": (
            "Vas a conectar el ESP32 a una red en modo estación y a usar el LED de `GPIO 2` como testigo: parpadea "
            "mientras intenta, queda fijo si conectó y se apaga si venció el tiempo de espera. Practicás el flujo completo "
            "del tema (`WiFi.mode`, `WiFi.begin`, espera con timeout, `WiFi.localIP`) y, sobre todo, el camino de error "
            "que casi nadie prueba."
        ),
        "materials": [
            "Simulador Wokwi (red `Wokwi-GUEST`, sin contraseña) o ESP32 DevKit con una red Wi-Fi de 2.4 GHz",
            "LED integrado de `GPIO 2` (o LED rojo con resistencia de `220 Ω`)",
            "Cronómetro o celular",
        ],
        "steps": [
            "Definí arriba de todo el nombre de la red y la contraseña como constantes. En Wokwi: `Wokwi-GUEST` y contraseña vacía.",
            "En `setup()`: Serial a `115200`, `GPIO 2` como salida, `WiFi.mode(WIFI_STA)` y `WiFi.begin(ssid, password)`.",
            "Guardá el momento de inicio con `millis()` y esperá en un bucle mientras `WiFi.status() != WL_CONNECTED` y no hayan pasado `15000 ms`. Dentro del bucle invertí el LED y esperá `150 ms`: ese es el parpadeo de 'conectando'.",
            "Al salir del bucle preguntá por qué saliste. Si conectó: LED fijo encendido, e imprimí `WiFi.localIP()` y la señal `WiFi.RSSI()` en dBm. Si no: LED apagado e imprimí `SIN CONEXION`.",
            "Probá el camino feliz y anotá la IP y el RSSI.",
            "Probá el camino de error: cambiale una letra al nombre de la red, ejecutá y cronometrá cuánto tarda en rendirse. Después restaurá el nombre.",
        ],
        "done_when": [
            "Con la red correcta, el LED parpadea unos instantes y queda fijo, y el Monitor Serial muestra una IP y un RSSI.",
            "Con el nombre de red mal escrito, el LED parpadea 15 segundos (±1 s), se apaga y aparece `SIN CONEXION`.",
            "En los dos casos el programa llega al final de `setup()`: nunca queda colgado esperando.",
        ],
        "hints": [
            "En la placa real, el ESP32 clásico solo ve redes de 2.4 GHz: si tu router emite también en 5 GHz con el mismo nombre, puede no conectar.",
            "No dejes tu contraseña real en un proyecto público de Wokwi ni en capturas de pantalla: en el simulador usá siempre `Wokwi-GUEST`.",
            "El RSSI es negativo: cuanto más cerca de 0, mejor señal (`−50 dBm` es muy buena; `−85 dBm` es floja).",
        ],
        "lab_link": "electronics:projects",
        "minutes": 20,
    },
    {
        "id": "e-esp32-wifi-iot-2",
        "node": "e-esp32-wifi-iot",
        "kind": "project",
        "level": 3,
        "title": "Registrador de datos con hora de internet (NTP)",
        "statement": (
            "Vas a armar un registrador conectado: el ESP32 toma la hora real de internet por NTP, lee un sensor "
            "analógico cada 5 segundos e imprime una línea con hora, valor y señal Wi-Fi, lista para pegar en una "
            "planilla. Si el Wi-Fi se cae, sigue midiendo y reintenta solo. Reúne todo el recorrido: ADC1, `millis()`, "
            "conexión robusta y un servicio real de internet."
        ),
        "materials": [
            "Simulador Wokwi (red `Wokwi-GUEST`) o ESP32 DevKit con una red Wi-Fi de 2.4 GHz con internet",
            "Potenciómetro de `10 kΩ` (o tu sensor de luz del tema 5)",
            "LED rojo y resistencia de `220 Ω` (alarma)",
            "LED integrado de `GPIO 2` (testigo de Wi-Fi)",
            "Protoboard y cables",
            "Planilla de cálculo",
        ],
        "steps": [
            "Cableá el potenciómetro (extremos a `3V3` y `GND`, cursor a `GPIO 34`) y el LED de alarma con su resistencia de `220 Ω` en `GPIO 18`.",
            "Conectá a la red con timeout de 15 segundos y usá `GPIO 2` como testigo de conexión.",
            "Después de conectar, pedí la hora de Argentina (UTC−3) con una línea: `configTime(-3 * 3600, 0, \"pool.ntp.org\");`",
            "Escribí una función que llame a `getLocalTime()` y devuelva la hora como texto `HH:MM:SS`; si todavía no hay hora, que devuelva `--:--:--`.",
            "Tarea 1, cada `5000 ms` con `millis()`: leé `analogRead(34)` e imprimí una línea con el formato `hora;valor;rssi`.",
            "Tarea 2, en cada vuelta: si el valor supera `3000`, encendé el LED de alarma; si no, apagalo.",
            "Tarea 3, cada `10000 ms`: si `WiFi.status()` no es `WL_CONNECTED`, apagá el testigo y llamá a `WiFi.reconnect()` sin quedarte esperando; cuando vuelva la conexión, encendé el testigo.",
            "Dejalo correr 2 minutos moviendo el potenciómetro, copiá las líneas del Monitor Serial y pegalas en una planilla separando por punto y coma.",
            "Solo con hardware real: apagá un minuto el router o el punto de acceso del celular y comprobá que sigue registrando y que reconecta solo.",
        ],
        "done_when": [
            "La hora impresa coincide con la de tu celular (±2 s).",
            "En 2 minutos hay entre 23 y 25 líneas, separadas 5 segundos entre sí.",
            "El LED de alarma responde al instante al pasar de `3000`, sin esperar a la próxima línea.",
            "`loop()` no contiene ningún `delay()` y el sensor está en un pin de ADC1.",
            "Las líneas se abren como tres columnas (hora, valor, señal) en la planilla.",
        ],
        "hints": [
            "Con el Wi-Fi encendido, `analogRead()` solo es confiable en ADC1 (`GPIO 32` a `39`): en `GPIO 4` (ADC2) este proyecto dejaría de leer.",
            "La primera sincronización NTP puede tardar unos segundos: por eso la función tiene que tolerar que `getLocalTime()` devuelva falso.",
            "`getLocalTime()` espera hasta 5 segundos si todavía no hay hora: pasale un tiempo máximo corto como segundo parámetro (en ms) para no bloquear `loop()`.",
        ],
        "lab_link": "electronics:projects",
        "minutes": 90,
    },
]

GUITAR: list[dict[str, Any]] = [
    # ----------------------------------------------------------- g-postura-afinacion
    {
        "id": "g-postura-afinacion-1",
        "node": "g-postura-afinacion",
        "kind": "project",
        "level": 1,
        "title": "Afinación completa y chequeo de postura",
        "statement": (
            "Vas a afinar las seis cuerdas con el afinador del laboratorio y a repasar la postura con una lista corta. "
            "Es la rutina de arranque de cualquier sesión: si la guitarra está desafinada o el cuerpo tenso, todo lo "
            "demás suena mal aunque lo toques bien."
        ),
        "materials": [
            "Guitarra",
            "Afinador del Laboratorio de Guitarra (con micrófono o con los tonos de referencia)",
            "Silla sin apoyabrazos",
            "Un lugar silencioso",
        ],
        "steps": [
            "Calentamiento (1 minuto): sacudí las manos, abrí y cerrá los dedos 10 veces y aflojá los hombros.",
            "Sentate en el borde de la silla con la espalda derecha y la guitarra apoyada en la pierna, con el mástil apenas inclinado hacia arriba. El pulgar izquierdo va detrás del mástil, sin apretar.",
            "Decí en voz alta las cuerdas de 6ª a 1ª: Mi – La – Re – Sol – Si – Mi (E – A – D – G – B – E).",
            "Abrí el Afinador, tocá la 6ª cuerda al aire y dejala sonar. Mirá si está baja o alta ANTES de tocar la clavija.",
            "Girá la clavija de a poco, siempre haciendo sonar la cuerda. Si te pasaste, aflojá un poco y volvé a llegar a la nota subiendo la tensión.",
            "Repetí con la 5ª, la 4ª, la 3ª, la 2ª y la 1ª.",
            "Segunda pasada: volvé a revisar las seis en orden, porque al tensar unas cuerdas las otras se mueven.",
            "Prueba de limpieza: pisá el traste 2 de la 4ª cuerda con el dedo 1, justo detrás de la varilla, y tocala 5 veces.",
        ],
        "done_when": [
            "En la segunda pasada las 6 cuerdas quedan centradas en el afinador sin tocar ninguna clavija.",
            "Dijiste las 6 cuerdas en orden, de memoria, de 6ª a 1ª.",
            "La nota del traste 2 de la 4ª cuerda sonó limpia, sin zumbido, 5 veces seguidas.",
            "Terminaste con los hombros y la muñeca sueltos, sin dolor.",
        ],
        "hints": [
            "Si el micrófono no funciona (necesita el permiso del navegador y `localhost` o HTTPS), usá los tonos de referencia y compará de oído.",
            "Girá la clavija de a cuartos de vuelta: tensar de más sin escuchar es la forma clásica de cortar una cuerda.",
            "Que moleste la yema del dedo al principio es normal; si duele la muñeca o el antebrazo, pará y descansá.",
        ],
        "lab_link": "guitar:tuner",
        "minutes": 15,
    },
    {
        "id": "g-postura-afinacion-2",
        "node": "g-postura-afinacion",
        "kind": "project",
        "level": 2,
        "title": "Notas limpias: un dedo por traste con metrónomo",
        "statement": (
            "Vas a tocar notas sueltas con los cuatro dedos, un dedo por traste, al ritmo del metrónomo. No es música "
            "todavía: es el entrenamiento que le enseña a cada dedo a caer justo detrás de la varilla con la mínima "
            "fuerza, que es lo que después hace sonar limpios los acordes."
        ),
        "materials": [
            "Guitarra afinada",
            "Metrónomo del Laboratorio de Guitarra",
            "Púa (opcional: también podés tocar con el pulgar)",
        ],
        "steps": [
            "Calentamiento (1 minuto): sacudí las manos y abrí y cerrá los dedos 10 veces.",
            "Ubicá la mano en los trastes 5 a 8, donde los trastes están más juntos que cerca de la cejuela: dedo 1 en el traste 5, dedo 2 en el 6, dedo 3 en el 7 y dedo 4 en el 8.",
            "Sin metrónomo, en la 3ª cuerda: tocá los trastes 5, 6, 7 y 8 dejando sonar cada nota 2 segundos. Si zumba, acercá la yema a la varilla en vez de apretar más.",
            "Metrónomo a 50 BPM, una nota por pulso: 5–6–7–8 en la 6ª cuerda, después en la 5ª, y así hasta la 1ª (24 notas, medio minuto).",
            "Descansá 30 segundos con la mano colgando y repetí la pasada.",
            "Hacé pasadas hasta lograr 3 limpias seguidas. Si una nota sale sucia, esa pasada no cuenta.",
            "Bajada: 3 pasadas de la 1ª a la 6ª cuerda tocando 8–7–6–5 en cada una.",
            "Cierre: una última pasada lenta, sin metrónomo, revisando que el pulgar siga suelto detrás del mástil.",
        ],
        "done_when": [
            "Completaste 3 pasadas seguidas de 24 notas a 50 BPM sin zumbidos ni notas apagadas.",
            "Cada nota cayó junto con el clic, sin frenar al pasar de una cuerda a la otra.",
            "Hiciste las 3 pasadas de bajada (8–7–6–5).",
            "No hubo dolor en la muñeca ni en el antebrazo en toda la rutina.",
        ],
        "hints": [
            "Dejá apoyados los dedos que ya tocaste mientras cae el siguiente: la mano aprende la apertura sin esfuerzo extra.",
            "Si el meñique no llega cómodo al traste 8, corré un poco el pulgar hacia el centro del mástil; no fuerces el estiramiento.",
            "Parar a tiempo también es practicar: ante dolor (no la molestia normal de la yema), cortá la sesión.",
        ],
        "lab_link": "guitar:metronome",
        "minutes": 25,
    },
    # --------------------------------------------------------------- g-acordes-em-am
    {
        "id": "g-acordes-em-am-1",
        "node": "g-acordes-em-am",
        "kind": "project",
        "level": 1,
        "title": "Em y Am limpios, cuerda por cuerda",
        "statement": (
            "Vas a armar Mi menor y La menor y a revisarlos cuerda por cuerda hasta que todas suenen. Antes de pensar en "
            "velocidad necesitás que el acorde suene bien cada vez que lo armás: esta rutina entrena eso y el movimiento "
            "en bloque de los dedos 2 y 3."
        ),
        "materials": [
            "Guitarra afinada",
            "Diagramas y audio de Em y Am (Laboratorio de Guitarra → Cambios de acordes)",
        ],
        "steps": [
            "Calentamiento (1 minuto): abrí y cerrá las manos 10 veces y sacudilas.",
            "Armá Em: dedo 2 en la 5ª cuerda traste 2 y dedo 3 en la 4ª cuerda traste 2. Tocá las 6 cuerdas de a una, de 6ª a 1ª, escuchando cada una.",
            "Si alguna suena apagada o zumba, corregí (yema más cerca de la varilla, dedo más arqueado) y repetí el arpegio hasta lograr 3 limpios seguidos.",
            "Armá Am: dedos 2 y 3 en el traste 2 de la 4ª y la 3ª cuerda, y dedo 1 en la 2ª cuerda traste 1. Tocá de a una desde la 5ª hasta la 1ª; la 6ª no se toca.",
            "Prestá atención a la 1ª cuerda en Am: si suena apagada, arqueá más el dedo 1. Repetí hasta lograr 3 arpegios limpios seguidos.",
            "Armar y soltar: armá Em, levantá los dedos 1 cm sin perder la forma y volvé a apoyarlos, 10 veces. Hacé lo mismo con Am.",
            "Cambio en cámara lenta, sin tempo: de Em a Am bajando juntos los dedos 2 y 3 una cuerda y sumando el dedo 1; después volvé a Em. 10 cambios, rasgueando una vez cada acorde.",
            "Compará tu sonido con el botón Escuchar de cada acorde en el laboratorio.",
        ],
        "done_when": [
            "Em suena con sus 6 cuerdas limpias en 3 arpegios seguidos.",
            "Am suena con sus 5 cuerdas limpias (incluida la 1ª) en 3 arpegios seguidos, sin tocar la 6ª.",
            "Hiciste 10 cambios lentos moviendo los dedos 2 y 3 como un bloque, no de a uno.",
            "Terminaste sin dolor en la mano ni en la muñeca.",
        ],
        "hints": [
            "Uñas de la mano izquierda cortas: con uñas largas el dedo no puede caer de punta.",
            "Que arda un poco la yema los primeros días es normal; dolor en la muñeca o en la base del pulgar, no: pará y aflojá.",
        ],
        "lab_link": "guitar:chords",
        "minutes": 15,
    },
    {
        "id": "g-acordes-em-am-2",
        "node": "g-acordes-em-am",
        "kind": "project",
        "level": 2,
        "title": "Em ↔ Am a tempo: de 15 a 30 cambios por minuto",
        "statement": (
            "Vas a llevar el cambio Em ↔ Am al metrónomo: primero un cambio cada 4 pulsos y después uno cada 2, siempre a "
            "60 BPM. Cerrás midiendo tus cambios limpios en un minuto para tener una marca propia que superar. Es el paso "
            "de 'me sale el acorde' a 'me sale a tiempo'."
        ),
        "materials": [
            "Guitarra afinada",
            "Metrónomo del Laboratorio de Guitarra",
            "Contador de cambios (Laboratorio de Guitarra → Cambios de acordes)",
        ],
        "steps": [
            "Calentamiento (2 minutos): manos sueltas y 5 cambios Em ↔ Am en cámara lenta, revisando que suenen limpios.",
            "Metrónomo a 60 BPM en 4/4. Etapa 1: un rasgueo ↓ en el pulso 1 y lo dejás sonar; usás los pulsos 3 y 4 para mover la mano. Cambiás de acorde en cada compás (15 cambios por minuto). Hacelo 2 minutos seguidos.",
            "Descansá 30 segundos con la mano colgando.",
            "Etapa 2: rasgueo ↓ en los pulsos 1 y 3, cambiando de acorde cada 2 pulsos (Em en el 1, Am en el 3): son 30 cambios por minuto. Hacelo 1 minuto.",
            "Si en la etapa 2 más de 3 cambios salieron sucios o tarde, volvé 1 minuto a la etapa 1 y reintentá.",
            "Medición: en Laboratorio de Guitarra → Cambios de acordes elegí Em y Am, iniciá los 60 segundos y contá solo los cambios limpios, sin metrónomo, a tu máxima velocidad prolija.",
            "Guardá la marca y anotala con la fecha.",
            "Cierre: 3 cambios lentos perfectos, sin tempo.",
        ],
        "done_when": [
            "Completaste 2 minutos seguidos cambiando cada 4 pulsos a 60 BPM (30 cambios) sin perder ningún pulso 1.",
            "Completaste 1 minuto cambiando cada 2 pulsos a 60 BPM (30 cambios) con 3 errores o menos.",
            "Tu marca guardada en el laboratorio es de 20 cambios limpios por minuto o más.",
            "Cerraste con 3 cambios lentos perfectos y sin dolor.",
        ],
        "hints": [
            "Si llegás tarde, no frenes: el pulso manda. Bajá a 50 BPM antes que tocar desparejo a 60.",
            "Mirá el destino antes de despegar: los dedos 2 y 3 viajan juntos y el dedo 1 cae al mismo tiempo.",
            "Si hoy no llegás a 20 por minuto, guardá igual la marca: la meta es superarla en la próxima sesión.",
        ],
        "lab_link": "guitar:chords",
        "minutes": 25,
    },
    # --------------------------------------------------------------- g-acordes-d-a-e
    {
        "id": "g-acordes-d-a-e-1",
        "node": "g-acordes-d-a-e",
        "kind": "project",
        "level": 1,
        "title": "Dedo ancla: D → A → E sin soltar la 3ª cuerda",
        "statement": (
            "Vas a armar D, A y E y a encadenarlos en cámara lenta usando el dedo 1 como ancla sobre la 3ª cuerda. El "
            "objetivo no es la velocidad sino grabar el recorrido mínimo: cuando el índice no se despega, los otros dos "
            "dedos encuentran su lugar solos."
        ),
        "materials": [
            "Guitarra afinada",
            "Diagramas y audio de D, A y E (Laboratorio de Guitarra → Cambios de acordes)",
        ],
        "steps": [
            "Calentamiento (1 minuto): abrí y cerrá las manos y hacé 5 cambios Em ↔ Am lentos.",
            "Armá D (dedo 1 en la 3ª cuerda traste 2, dedo 2 en la 1ª cuerda traste 2 y dedo 3 en la 2ª cuerda traste 3) y arpegiá desde la 4ª cuerda. Corregí hasta que suenen las 4.",
            "Armá A con la digitación 2-1-3 (dedo 2 en la 4ª, dedo 1 en la 3ª y dedo 3 en la 2ª cuerda, los tres en el traste 2) y arpegiá desde la 5ª cuerda.",
            "Armá E (dedo 1 en la 3ª cuerda traste 1, dedos 2 y 3 en el traste 2 de la 5ª y la 4ª cuerda) y arpegiá las 6 cuerdas.",
            "D → A en cámara lenta: el dedo 1 NO se levanta de la 3ª cuerda traste 2; solo se reacomodan los dedos 2 y 3. 5 veces ida y vuelta.",
            "A → E: deslizá el dedo 1 por la 3ª cuerda del traste 2 al 1 sin despegarlo, mientras los dedos 2 y 3 van a la 5ª y la 4ª cuerda. 5 veces ida y vuelta.",
            "Rueda completa D → A → E → A, sin tempo, con un rasgueo por acorde desde la cuerda que corresponde. Repetila hasta lograr 5 ruedas seguidas con el ancla siempre apoyada.",
        ],
        "done_when": [
            "D suena limpio desde la 4ª cuerda, A desde la 5ª y E con las 6.",
            "Hiciste 5 ruedas D → A → E → A seguidas sin que el dedo 1 se despegue de la 3ª cuerda.",
            "En ningún rasgueo de D sonaron la 6ª ni la 5ª cuerda.",
            "Terminaste sin dolor en la mano.",
        ],
        "hints": [
            "En D, si la 1ª cuerda suena apagada, el dedo 3 está inclinado y la roza: arquealo más.",
            "El ancla no aprieta todo el tiempo: durante el cambio afloja la presión, pero sigue tocando la cuerda, como sobre un riel.",
        ],
        "lab_link": "guitar:chords",
        "minutes": 15,
    },
    {
        "id": "g-acordes-d-a-e-2",
        "node": "g-acordes-d-a-e",
        "kind": "project",
        "level": 2,
        "title": "Blues de 12 compases en La con A, D y E",
        "statement": (
            "Vas a tocar una vuelta de blues de 12 compases en La usando solo A, D y E (los grados I, IV y V). Es la "
            "primera forma musical completa que podés tocar con los tres acordes del tema, y te obliga a hacer los "
            "cambios A ↔ D, A ↔ E y E → D a tiempo y de memoria."
        ),
        "materials": [
            "Guitarra afinada",
            "Metrónomo del Laboratorio de Guitarra",
            "Papel y lápiz para anotar la estructura",
        ],
        "steps": [
            "Calentamiento (2 minutos): manos sueltas y 5 ruedas lentas D → A → E → A con el dedo ancla.",
            "Copiá en un papel la estructura, con un acorde por compás: `A A A A | D D A A | E D A E`.",
            "Sin metrónomo: recorré los 12 compases con un solo rasgueo por compás, diciendo en voz alta el número de compás.",
            "Aislá el cambio que más te cueste (suele ser E → D, en los compases 9 y 10): 10 repeticiones lentas solo de ese cambio.",
            "Metrónomo a 60 BPM en 4/4: tocá la vuelta con un rasgueo ↓ en el pulso 1 de cada compás. Una vuelta son 48 pulsos, es decir, 48 segundos.",
            "Cuando salga sin perder ningún compás, pasá a 4 rasgueos ↓ por compás (uno por pulso), cambiando de acorde justo en el pulso 1.",
            "Tocá 2 vueltas seguidas (96 segundos) sin frenar la mano derecha, aunque algún acorde salga sucio.",
            "Cierre: una vuelta lenta sin metrónomo, buscando que cada acorde suene limpio.",
        ],
        "done_when": [
            "Tocaste la estructura de 12 compases de memoria, sin mirar el papel.",
            "Completaste una vuelta a 60 BPM con un rasgueo por compás sin perder ningún pulso 1.",
            "Completaste 2 vueltas seguidas a 60 BPM con 4 rasgueos por compás sin detener la mano derecha.",
            "D sonó siempre desde la 4ª cuerda y A desde la 5ª.",
        ],
        "hints": [
            "En E → D el ancla también sirve: el dedo 1 se desliza por la 3ª cuerda del traste 1 al 2.",
            "Si te perdés en la forma, pensala en tres renglones de 4 compases: el primero es todo A, el segundo es D–D–A–A y el tercero es E–D–A–E.",
            "Bajá a 50 BPM si no llegás a los cambios: tempo estable antes que tempo alto. Ante dolor en la mano, pará.",
        ],
        "lab_link": "guitar:metronome",
        "minutes": 30,
    },
    # ------------------------------------------------------------------- g-ritmo-4-4
    {
        "id": "g-ritmo-4-4-1",
        "node": "g-ritmo-4-4",
        "kind": "project",
        "level": 1,
        "title": "Péndulo de corcheas con las cuerdas apagadas",
        "statement": (
            "Vas a entrenar solo la mano derecha: un péndulo constante de corcheas sobre las cuerdas apagadas, contando "
            "en voz alta. Sin acordes que distraigan, el brazo aprende a no frenarse nunca, que es la regla de oro del ritmo."
        ),
        "materials": [
            "Guitarra",
            "Metrónomo del Laboratorio de Guitarra",
            "Púa (opcional)",
        ],
        "steps": [
            "Calentamiento (1 minuto): sacudí el brazo derecho y aflojá la muñeca. El movimiento sale del antebrazo, no del hombro.",
            "Apoyá la mano izquierda sobre las 6 cuerdas sin apretar, para que suenen percusivas.",
            "Metrónomo a 60 BPM en 4/4. Contá en voz alta `1 y 2 y 3 y 4 y`.",
            "Corcheas completas: ↓ en cada número y ↑ en cada 'y' (↓↑ ↓↑ ↓↑ ↓↑). 2 minutos seguidos sin parar.",
            "Negras con péndulo: la mano sigue subiendo en cada 'y', pero pasa por el aire sin tocar; solo suenan los ↓ de los números. 1 minuto.",
            "Alternancia: un compás de corcheas y un compás de negras, 8 compases seguidos, sin que el brazo cambie de velocidad.",
            "Acentos: volvé a las corcheas y tocá más fuerte los pulsos 2 y 4 durante 8 compases.",
        ],
        "done_when": [
            "Tocaste 2 minutos seguidos de corcheas a 60 BPM (30 compases) sin detener la mano.",
            "En el minuto de negras la mano subió por el aire en todos los 'y', sin quedarse quieta.",
            "Hiciste los 8 compases alternados sin frenar ni acelerar al cambiar de figura.",
            "Contaste en voz alta todo el tiempo y los ↓ cayeron junto con el clic.",
        ],
        "hints": [
            "Sostené la púa floja (o rasgueá con el pulgar y el índice): si la apretás, se traba en las cuerdas al subir.",
            "Al subir no hace falta tocar las 6 cuerdas: con rozar las 3 o 4 más finas alcanza.",
            "Si el hombro o el antebrazo se cansan o duelen, hay tensión de más: pará, sacudí el brazo y achicá el movimiento.",
        ],
        "lab_link": "guitar:metronome",
        "minutes": 15,
    },
    {
        "id": "g-ritmo-4-4-2",
        "node": "g-ritmo-4-4",
        "kind": "project",
        "level": 2,
        "title": "Tres patrones con el mismo péndulo",
        "statement": (
            "Vas a encadenar tres patrones de rasgueo —negras, `1 2y 3 4y` y el patrón universal— sin que la mano derecha "
            "cambie nunca su péndulo, primero con las cuerdas apagadas y después sobre Em y Am. Terminás subiendo el "
            "patrón universal por la Escalera de BPM hasta 70."
        ),
        "materials": [
            "Guitarra afinada",
            "Metrónomo del Laboratorio de Guitarra (con la Escalera de BPM)",
            "Púa (opcional)",
        ],
        "steps": [
            "Calentamiento (2 minutos): péndulo de corcheas con las cuerdas apagadas a 60 BPM.",
            "Patrón 1, negras: ↓ ↓ ↓ ↓ (se cuenta `1 2 3 4`, subiendo por el aire). 4 compases con cuerdas apagadas.",
            "Patrón 2: ↓ ↓↑ ↓ ↓↑ (se cuenta `1 2y 3 4y`). 4 compases con cuerdas apagadas.",
            "Patrón 3, universal: ↓ ↓↑ ↑↓↑ (se cuenta `1 2y y4y`; en el 3 la mano baja por el aire). 4 compases con cuerdas apagadas.",
            "Cadena: 4 compases de cada patrón, uno detrás del otro (12 compases), a 60 BPM y sin parar entre patrones.",
            "Repetí la cadena con el acorde Em, y después alternando 2 compases de Em y 2 de Am.",
            "Escalera de BPM (Laboratorio de Guitarra → Metrónomo): patrón universal en Em desde 55 BPM. Cada repetición son 4 compases; con 3 limpias seguidas sube 5 BPM, y si hay error bajás 5.",
            "Cierre: 4 compases del patrón universal a 55 BPM, lo más relajado que puedas.",
        ],
        "done_when": [
            "Tocaste la cadena de 12 compases a 60 BPM con cuerdas apagadas sin detener la mano.",
            "Tocaste la cadena de 12 compases con Em y Am sin perder el pulso 1 en los cambios.",
            "En el patrón universal suenan 6 rasgueos por compás y la mano pasa por el aire en el 'y' del 1 y en el 3.",
            "Guardaste en la Escalera una marca limpia del patrón universal a 70 BPM.",
        ],
        "hints": [
            "Aprendé cada patrón diciéndolo primero en voz alta (`1, 2 y, y 4 y`) mientras movés la mano en el aire.",
            "El error típico del patrón universal es frenar la mano en el 3: tiene que bajar igual, sin tocar las cuerdas.",
            "Si hoy no llegás a 70 BPM, guardá tu marca y retomá la escalera desde ahí en la próxima sesión. Ante dolor en el brazo, pará.",
        ],
        "lab_link": "guitar:metronome",
        "minutes": 30,
    },
    # ----------------------------------------------------------------- g-acordes-g-c
    {
        "id": "g-acordes-g-c-1",
        "node": "g-acordes-g-c",
        "kind": "project",
        "level": 1,
        "title": "G y C limpios y aterrizaje en cámara lenta",
        "statement": (
            "Vas a armar Sol mayor y Do mayor hasta que suenen todas sus cuerdas y a practicar el cambio entre los dos en "
            "cámara lenta, con la digitación 3-2-4 de G. Es la preparación para el cambio más difícil de esta etapa: "
            "primero la trayectoria correcta, después la velocidad."
        ),
        "materials": [
            "Guitarra afinada",
            "Diagramas y audio de G y C (Laboratorio de Guitarra → Cambios de acordes)",
        ],
        "steps": [
            "Calentamiento (2 minutos): abrí y cerrá las manos y separá suavemente los dedos de a pares, sin forzar.",
            "Armá C: dedo 3 en la 5ª cuerda traste 3, dedo 2 en la 4ª cuerda traste 2 y dedo 1 en la 2ª cuerda traste 1. Arpegiá de la 5ª a la 1ª.",
            "Revisá la 1ª cuerda: si suena apagada, bajá un poco el pulgar detrás del mástil y arqueá más el dedo 1. Repetí hasta lograr 3 arpegios limpios seguidos.",
            "Armá G con la digitación 3-2-4: dedo 3 en la 6ª cuerda traste 3, dedo 2 en la 5ª cuerda traste 2 y dedo 4 en la 1ª cuerda traste 3. Arpegiá las 6 cuerdas hasta lograr 3 limpios seguidos.",
            "Vuelo en el aire: armá G, levantá los dedos 1 cm y, sin apoyar, llevá los dedos 3 y 2 una cuerda hacia las finas. Mirá que el recorrido es mínimo.",
            "Cambio G → C en cámara lenta: bajan juntos los dedos 3 y 2, se suma el dedo 1 y se levanta el meñique. Contá hasta 4 mientras se mueven. 10 cambios ida y vuelta, rasgueando cada acorde una vez.",
            "Cierre: 3 cambios más buscando que todos los dedos apoyen a la vez, no de a uno.",
        ],
        "done_when": [
            "C suena con sus 5 cuerdas limpias, incluida la 1ª al aire, en 3 arpegios seguidos.",
            "G (digitación 3-2-4) suena con las 6 cuerdas limpias en 3 arpegios seguidos.",
            "Hiciste 10 cambios lentos G ↔ C sin que ningún dedo quedara acomodándose después del rasgueo.",
            "En C no sonó la 6ª cuerda y no hubo dolor al abrir la mano.",
        ],
        "hints": [
            "G y C piden abrir la mano más que los acordes anteriores: acercá el codo al cuerpo y adelantá un poco la muñeca.",
            "Si el meñique todavía no llega cómodo a la 1ª cuerda en G, practicá unos días con la digitación 2-1-3 y volvé a probar; no fuerces.",
            "Estirar no es doler: ante dolor en la muñeca o en la base de los dedos, pará.",
        ],
        "lab_link": "guitar:chords",
        "minutes": 15,
    },
    {
        "id": "g-acordes-g-c-2",
        "node": "g-acordes-g-c",
        "kind": "project",
        "level": 2,
        "title": "Pirámide de cambios G ↔ C a 60 BPM",
        "statement": (
            "Vas a llevar el cambio G ↔ C al metrónomo con una pirámide: cambiar cada 8 pulsos, después cada 4 y después "
            "cada 2, siempre a 60 BPM. Terminás midiendo tus cambios limpios por minuto y tocando la pareja con el patrón "
            "universal. El objetivo es que el 'muro' del principiante deje de frenarte el ritmo."
        ),
        "materials": [
            "Guitarra afinada",
            "Metrónomo del Laboratorio de Guitarra",
            "Contador de cambios (Laboratorio de Guitarra → Cambios de acordes)",
        ],
        "steps": [
            "Calentamiento (2 minutos): manos sueltas y 5 cambios G ↔ C en cámara lenta.",
            "Metrónomo a 60 BPM en 4/4. Escalón 1: 2 compases por acorde (un cambio cada 8 pulsos), con 4 rasgueos ↓ por compás. 2 minutos.",
            "Escalón 2: 1 compás por acorde (un cambio cada 4 pulsos). 2 minutos, que son 30 cambios.",
            "Descansá 30 segundos con la mano colgando.",
            "Escalón 3: medio compás por acorde (un cambio cada 2 pulsos), con un rasgueo ↓ por pulso. 1 minuto, que son 30 cambios.",
            "Si en un escalón se te escapan más de 3 cambios, volvé un minuto al escalón anterior antes de reintentar.",
            "Medición: en Laboratorio de Guitarra → Cambios de acordes elegí G y C, iniciá los 60 segundos y contá solo los cambios limpios. Guardá la marca.",
            "Aplicación: 8 compases alternando G y C (uno por compás) con el patrón universal ↓ ↓↑ ↑↓↑ a 60 BPM, soltando la mano izquierda en el último 'y' para llegar a tiempo.",
            "Cierre: 3 cambios lentos perfectos.",
        ],
        "done_when": [
            "Completaste el escalón 2 (2 minutos, 30 cambios) sin perder ningún pulso 1.",
            "Completaste el escalón 3 (1 minuto, 30 cambios) con 3 errores o menos.",
            "Tu marca guardada en el laboratorio es de 25 cambios limpios por minuto o más.",
            "Tocaste los 8 compases con el patrón universal sin frenar la mano derecha.",
        ],
        "hints": [
            "Apoyá primero los dedos graves (3 y 2): si esos llegan a tiempo, el acorde ya suena aunque el resto caiga un instante después.",
            "Mirá el traste de destino antes de soltar el acorde actual.",
            "Este cambio suele tardar varios días en soltarse: si hoy quedás en 15 o 20 por minuto, guardá la marca y repetí la rutina mañana. Ante dolor, pará.",
        ],
        "lab_link": "guitar:chords",
        "minutes": 30,
    },
    # ------------------------------------------------------------- g-primera-cancion
    {
        "id": "g-primera-cancion-1",
        "node": "g-primera-cancion",
        "kind": "project",
        "level": 1,
        "title": "Diagnóstico de enlaces en G – D – Em – C",
        "statement": (
            "Vas a tocar la progresión I–V–vi–IV en Sol (G – D – Em – C) con un rasgueo por compás y a medir cuál de sus "
            "cuatro enlaces es tu punto débil, para trabajarlo aislado. Es la técnica de fragmentos aplicada: en vez de "
            "repetir toda la vuelta, arreglás solo el cambio que falla y después lo reconectás."
        ),
        "materials": [
            "Guitarra afinada",
            "Metrónomo del Laboratorio de Guitarra, con la progresión `I–V–vi–IV (G - D - Em - C)`",
            "Papel y lápiz",
        ],
        "steps": [
            "Calentamiento (2 minutos): manos sueltas y un arpegio lento de cada acorde (G, D, Em y C) para revisar que suenen limpios.",
            "En Laboratorio de Guitarra → Metrónomo elegí la progresión `I–V–vi–IV (G - D - Em - C)` a 60 BPM. Tocá 2 vueltas con un rasgueo largo en el pulso 1 de cada compás.",
            "Diagnóstico sin metrónomo: hacé 10 veces cada enlace por separado (G → D, D → Em, Em → C y C → G) y anotá cuántas de las 10 salieron limpias y sin dudar.",
            "Elegí el enlace con peor puntaje y repetilo en cámara lenta hasta lograr 5 repeticiones limpias seguidas.",
            "Reconexión: tocá solo los dos compases que rodean a ese enlace, con metrónomo a 60 BPM, 4 veces.",
            "Volvé a la vuelta completa a 60 BPM: 4 vueltas seguidas (16 compases, 64 segundos) con un rasgueo por compás.",
            "Cierre: una vuelta lenta sin metrónomo, escuchando cada acorde.",
        ],
        "done_when": [
            "Tenés anotado el puntaje (de 0 a 10) de los 4 enlaces e identificaste el más flojo.",
            "Lograste 5 repeticiones limpias seguidas del enlace más flojo.",
            "Tocaste 4 vueltas seguidas a 60 BPM, con un rasgueo por compás, sin perder ningún pulso 1.",
            "Cuando te equivocaste, trabajaste solo ese enlace: no volviste al principio para agarrar envión.",
        ],
        "hints": [
            "No te olvides de C → G: es el enlace que cierra la vuelta y el que más se descuida.",
            "En G → D y C → G no hay dedo ancla: mirá el destino antes de soltar.",
            "Si un acorde no llega a tiempo, tocá igual en el pulso 1 lo que haya: el ritmo no se frena. Ante dolor, pará.",
        ],
        "lab_link": "guitar:metronome",
        "minutes": 20,
    },
    {
        "id": "g-primera-cancion-2",
        "node": "g-primera-cancion",
        "kind": "project",
        "level": 3,
        "title": "Tu primera canción con forma: intro, estrofa y estribillo",
        "statement": (
            "Vas a armar una canción completa de algo más de dos minutos sobre G – D – Em – C, con intro, estrofas, "
            "estribillos y final, cambiando el rasgueo y la intensidad en cada sección. Después te grabás y te escuchás. "
            "Es la prueba integradora: acordes, ritmo, anticipación y resistencia para llegar al final sin frenar."
        ),
        "materials": [
            "Guitarra afinada",
            "Metrónomo del Laboratorio de Guitarra, con la progresión `I–V–vi–IV (G - D - Em - C)`",
            "Celular para grabarte",
            "Papel con el mapa de la canción",
        ],
        "steps": [
            "Calentamiento (3 minutos): 2 vueltas de G – D – Em – C a 60 BPM con un rasgueo por compás.",
            "Copiá el mapa (una vuelta son 4 compases): Intro, 1 vuelta · Estrofa, 2 vueltas · Estribillo, 2 vueltas · Estrofa, 2 vueltas · Estribillo, 2 vueltas · Final, un rasgueo de G que queda sonando.",
            "Definí el rasgueo de cada sección: Intro = un rasgueo ↓ por compás; Estrofa = ↓ ↓ ↓ ↓ suave; Estribillo = patrón universal ↓ ↓↑ ↑↓↑ fuerte.",
            "Practicá por fragmentos a 65 BPM: solo la intro y la primera estrofa (12 compases) hasta que salgan 2 veces seguidas.",
            "Practicá las dos costuras difíciles: de estrofa a estribillo (cambia el rasgueo) y de estribillo a estrofa (baja la intensidad). 4 compases antes y 4 después, 3 veces cada una.",
            "Canción completa con metrónomo a 65 BPM: son 37 compases, unos 2 minutos 17 segundos. Si te equivocás, seguí: no se vuelve atrás.",
            "Grabate con el celular tocando la canción completa.",
            "Escuchá la grabación con el mapa en la mano y marcá dónde se frenó el pulso o llegó tarde un cambio.",
            "Trabajá aislado el punto más flojo que encontraste y grabá una segunda toma.",
        ],
        "done_when": [
            "Tocaste la canción completa a 65 BPM, de la intro al G final, sin detener la mano derecha.",
            "En la grabación el estribillo se distingue con claridad de la estrofa (más fuerte y con otro rasgueo).",
            "En la segunda toma, como máximo 3 cambios de acorde llegaron tarde.",
            "Respetaste el mapa: 1 + 2 + 2 + 2 + 2 vueltas y el G final.",
            "Terminaste sin dolor ni tensión acumulada en los hombros y las manos.",
        ],
        "hints": [
            "La diferencia entre estrofa y estribillo se logra con el volumen y el rasgueo, no con la velocidad: el tempo es el mismo en toda la canción.",
            "Soltá la mano izquierda en el último 'y' de cada compás: las cuerdas al aire un instante te regalan el tiempo del cambio.",
            "Si 65 BPM te queda grande, grabá a 55: una toma pareja y lenta vale más que una rápida que se frena. Descansá entre tomas.",
        ],
        "lab_link": "guitar:metronome",
        "minutes": 45,
    },
    # ---------------------------------------------------------------- g-oido-musical
    {
        "id": "g-oido-musical-1",
        "node": "g-oido-musical",
        "kind": "project",
        "level": 1,
        "title": "Mayor o menor: del dedo al oído",
        "statement": (
            "Vas a escuchar en tu propia guitarra qué cambia entre un acorde mayor y su menor (E/Em y A/Am), a cantar la "
            "nota que se mueve y a poner a prueba el oído con 10 preguntas del laboratorio. Unir el gesto, la voz y la "
            "escucha es lo que hace que el color mayor o menor quede grabado."
        ),
        "materials": [
            "Guitarra afinada",
            "Laboratorio de Guitarra → Oído (modo Mayor vs Menor)",
            "Auriculares o parlante",
        ],
        "steps": [
            "Calentamiento (1 minuto): tocá E y Em una vez cada uno, lento, y tarareá cualquier nota que te quede cómoda.",
            "Tocá E, dejalo sonar y levantá solo el dedo 1 (3ª cuerda, traste 1) para pasar a Em. Repetí la ida y vuelta 5 veces escuchando el cambio de color.",
            "Ahora tocá solo la 3ª cuerda: en el traste 1 (la tercera mayor) y al aire (la tercera menor). Cantá las dos notas.",
            "Hacé lo mismo con A y Am: la nota que cambia está en la 2ª cuerda (traste 2 en A, traste 1 en Am). Tocala sola y cantala.",
            "Abrí Laboratorio de Guitarra → Oído en modo Mayor vs Menor. Antes de responder cada prueba, repetí el sonido y tarareá la nota del medio.",
            "Hacé una tanda de 10 pruebas y anotá tus aciertos. Si sacaste menos de 8, volvé al paso 2 y hacé otra tanda de 10.",
        ],
        "done_when": [
            "Encontraste y cantaste la nota que cambia en E/Em (3ª cuerda) y en A/Am (2ª cuerda).",
            "Comprobaste en el mástil que esa nota se mueve exactamente 1 traste (un semitono).",
            "Acertaste al menos 8 de 10 pruebas de Mayor vs Menor en una misma tanda.",
        ],
        "hints": [
            "No hace falta cantar afinado ni fuerte: tararear bajito ya activa el oído.",
            "En el laboratorio las tres notas del acorde suenan una detrás de la otra: la que decide es la segunda.",
            "Usá Repetir todas las veces que quieras: apurarse no entrena nada.",
        ],
        "lab_link": "guitar:ear",
        "minutes": 15,
    },
    {
        "id": "g-oido-musical-2",
        "node": "g-oido-musical",
        "kind": "project",
        "level": 2,
        "title": "Intervalos en una cuerda: tercera, quinta y octava",
        "statement": (
            "Vas a medir intervalos con tus propios dedos sobre la 5ª cuerda: tercera menor (3 trastes), tercera mayor "
            "(4), quinta justa (7) y octava (12). Primero los tocás y los cantás, después los buscás de oído y al final "
            "te medís con 20 pruebas del laboratorio. Es el primer paso para sacar melodías sin tablatura."
        ),
        "materials": [
            "Guitarra afinada",
            "Laboratorio de Guitarra → Oído (modo Intervalos)",
            "Papel y lápiz",
        ],
        "steps": [
            "Calentamiento (1 minuto): tocá la 5ª cuerda al aire (La) y tarareá esa nota hasta que tu voz coincida.",
            "Tocá la cuerda al aire y después el traste 4 (tercera mayor). Cantá las dos notas. Repetí 5 veces.",
            "Hacé lo mismo con el traste 3 (tercera menor), el traste 7 (quinta justa) y el traste 12 (octava), 5 veces cada uno.",
            "Asociá cada intervalo a un comienzo de melodía que conozcas bien y anotalo como referencia.",
            "Juego de búsqueda: tocá la cuerda al aire, cantá primero la quinta y recién después buscala deslizando un dedo por la cuerda. Mirá en qué traste frenaste. 5 intentos con la quinta y 5 con la tercera mayor.",
            "Repetí el juego en la 6ª cuerda (Mi): los trastes son los mismos, cambia la nota de partida.",
            "En Laboratorio de Guitarra → Oído, modo Intervalos (3ª, 5ª, 8ª), hacé 20 pruebas cantando la segunda nota antes de responder.",
            "Anotá tus aciertos. Si confundís siempre el mismo par, volvé a tocarlo 5 veces en la guitarra.",
        ],
        "done_when": [
            "Tocaste y cantaste los 4 intervalos (trastes 3, 4, 7 y 12) sobre la 5ª cuerda.",
            "En el juego de búsqueda frenaste en el traste 7, o a un traste de distancia, en al menos 3 de 5 intentos de quinta.",
            "Acertaste al menos 16 de 20 pruebas de intervalos en el laboratorio.",
            "Tenés anotada una melodía de referencia para cada intervalo.",
        ],
        "hints": [
            "La octava suena a 'la misma nota, más aguda'; la quinta, abierta y estable; la tercera mayor, dulce y cercana.",
            "Si tu voz no llega a la nota aguda, cantala una octava más abajo: sirve igual.",
            "El error más común es confundir la quinta con la octava: tocalas una detrás de la otra varias veces.",
        ],
        "lab_link": "guitar:ear",
        "minutes": 25,
    },
    # ------------------------------------------------------------- g-pua-pentatonica
    {
        "id": "g-pua-pentatonica-1",
        "node": "g-pua-pentatonica",
        "kind": "project",
        "level": 1,
        "title": "Púa alternada y Caja 1 en negras",
        "statement": (
            "Vas a entrenar la púa alternada estricta (↓ ↑), primero en una sola cuerda y después recorriendo la Caja 1 "
            "de la pentatónica de La menor a 60 BPM, una nota por pulso. Es la base de coordinación entre las dos manos "
            "para tocar melodías y solos."
        ),
        "materials": [
            "Guitarra afinada",
            "Púa",
            "Metrónomo del Laboratorio de Guitarra",
            "Laboratorio de Guitarra → Diapasón (patrón Pentatónica Am, Caja 1)",
        ],
        "steps": [
            "Calentamiento (2 minutos): manos sueltas y, sin metrónomo, una nota lenta con cada dedo en la 3ª cuerda (trastes 5, 6, 7 y 8).",
            "Abrí Laboratorio de Guitarra → Diapasón con la Caja 1 de Am y repasá el mapa de 6ª a 1ª cuerda: 5–8, 5–7, 5–7, 5–7, 5–8, 5–8. Ubicá las tres tónicas (La).",
            "Púa sola: metrónomo a 60 BPM, 3ª cuerda al aire, una nota por pulso alternando ↓ ↑ ↓ ↑ durante 1 minuto. Después dos notas por pulso (↓ en el clic, ↑ en el medio) otro minuto.",
            "Caja 1 subiendo, una nota por pulso a 60 BPM, de la 6ª cuerda a la 1ª (12 notas), con un dedo por traste: índice en el 5, anular en el 7 y meñique en el 8.",
            "Caja 1 bajando, de la 1ª cuerda a la 6ª (otras 12 notas). La púa sigue alternando aunque cambies de cuerda.",
            "Subida y bajada completas sin parar (24 notas, 24 segundos). Repetí hasta lograr 3 pasadas limpias seguidas.",
            "Cierre: tocá las tres tónicas (6ª cuerda traste 5, 4ª cuerda traste 7 y 1ª cuerda traste 5) y terminá en la más grave.",
        ],
        "done_when": [
            "Mantuviste 1 minuto de ↓ ↑ estricto en una cuerda a 60 BPM, dos notas por pulso, sin dos golpes seguidos en la misma dirección.",
            "Tocaste la Caja 1 subiendo y bajando (24 notas) a 60 BPM en 3 pasadas limpias seguidas.",
            "Usaste un dedo por traste: el meñique pisó todos los trastes 8.",
            "Ubicaste las tres tónicas de memoria, sin mirar el diapasón del laboratorio.",
        ],
        "hints": [
            "Tomá la púa entre el pulgar y el costado del índice, asomando apenas 2 o 3 mm: menos punta, más control.",
            "Decí en voz alta 'abajo, arriba' mientras tocás: al cambiar de cuerda es donde la mano quiere hacer trampa.",
            "Si el meñique se cansa o duele, descansá un minuto con la mano colgando; no lo reemplaces por el anular.",
        ],
        "lab_link": "guitar:fretboard",
        "minutes": 20,
    },
    {
        "id": "g-pua-pentatonica-2",
        "node": "g-pua-pentatonica",
        "kind": "project",
        "level": 3,
        "title": "Tu primer solo: frases sobre una base grabada",
        "statement": (
            "Vas a subir la Caja 1 a corcheas con la Escalera de BPM y después a improvisar tus primeras frases sobre una "
            "base de acordes que grabás vos (Am – C – G – Am). Las reglas son pocas: púa alternada, frases cortas, "
            "silencios y terminar en La. Así la escala deja de ser un ejercicio y empieza a sonar a música."
        ),
        "materials": [
            "Guitarra afinada",
            "Púa",
            "Metrónomo del Laboratorio de Guitarra (con la Escalera de BPM)",
            "Celular para grabar y reproducir la base",
            "Papel y lápiz",
        ],
        "steps": [
            "Calentamiento (3 minutos): Caja 1 subiendo y bajando en negras a 60 BPM, 2 pasadas.",
            "Corcheas: la misma caja con dos notas por pulso (↓ en el clic, ↑ entre clics) a 60 BPM. En la Escalera de BPM marcá 3 pasadas limpias para subir 5 BPM, hasta guardar la marca de 70.",
            "Grabá la base con el celular: metrónomo a 70 BPM, 4 rasgueos ↓ por compás y un compás por acorde en la rueda `Am – C – G – Am`. Grabá 8 ruedas seguidas (32 compases, cerca de 1 minuto 50).",
            "Primera pasada sobre la base: tocá solo las tónicas (La), con notas largas, para sentir dónde descansa la música.",
            "Frases: improvisá grupos de 3 a 5 notas vecinas de la caja. Cada frase termina en un La y después dejás al menos 2 pulsos de silencio.",
            "Pregunta y respuesta: una frase que termina en cualquier nota que no sea La (pregunta) y otra que termina en La (respuesta). Hacé al menos 4 parejas.",
            "Grabá tu mejor intento completo sobre la base y escuchalo.",
            "Anotá las dos frases que más te gustaron (cuerda y traste de cada nota) para reusarlas mañana.",
        ],
        "done_when": [
            "Guardaste en la Escalera una marca limpia de la Caja 1 en corcheas a 70 BPM, con púa alternada estricta.",
            "Grabaste la base de 8 ruedas sin frenar el pulso.",
            "Improvisaste durante toda la base con al menos 6 frases terminadas en La y silencios entre ellas.",
            "Todas las notas que tocaste pertenecen a la Caja 1 (trastes 5, 7 y 8).",
            "Tenés 2 frases propias anotadas y no hubo dolor en ninguna de las dos manos.",
        ],
        "hints": [
            "Menos notas y más ritmo: una frase de 3 notas bien puesta suena mejor que 12 corridas.",
            "Si una nota 'choca', movete a la nota vecina de la caja y seguí: en la pentatónica nunca estás lejos de una que suena bien.",
            "Si no tenés cómo reproducir la base, improvisá solo con el metrónomo pensando los acordes: lo importante son las frases y los silencios.",
        ],
        "lab_link": "guitar:metronome",
        "minutes": 45,
    },
]

EXERCISES: list[dict[str, Any]] = ELECTRONICS + GUITAR
