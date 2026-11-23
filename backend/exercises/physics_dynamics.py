"""Ejercicios de Física: dinámica y estática (ingreso a ingeniería).

Problemas de varios pasos para los temas:
  - f-leyes-newton
  - f-dcl-rozamiento-plano
  - f-cuerpos-vinculados
  - f-circular-gravitacion
  - f-estatica

Convención: en todo problema con peso se usa g = 10 m/s² (aclarado en cada enunciado).
"""

from __future__ import annotations

EXERCISES: list[dict] = [
    # ==================== LEYES DE NEWTON ====================
    {
        "id": "f-leyes-newton-1",
        "node": "f-leyes-newton",
        "kind": "problem",
        "level": 1,
        "title": "Frenada en la avenida",
        "statement": (
            "Un auto de 1200 kg circula a 20 m/s (72 km/h) por una avenida recta y horizontal. "
            "El conductor ve que el semáforo se pone en rojo, frena con aceleración constante y "
            "se detiene después de recorrer 40 m."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el módulo de la aceleración durante la frenada? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "m/s²"},
                "answer": "5 m/s² (en sentido contrario a la velocidad)",
            },
            {
                "prompt": "b) ¿Cuánto vale el módulo de la fuerza neta sobre el auto mientras frena? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 6000, "tolerance": 0, "unit": "N"},
                "answer": "6000 N, hacia atrás",
            },
            {
                "prompt": "c) ¿Cuánto dura la frenada? Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "s"},
                "answer": "4 s",
            },
        ],
        "hints": [
            "No conocés el tiempo, pero sí las dos velocidades y la distancia: usá `v² = v₀² + 2·a·Δx`.",
            "Con la aceleración, la 2ª ley te da la fuerza neta: `F_neta = m·a`. No hace falta saber qué fuerzas la componen.",
            "Para el tiempo: `v = v₀ + a·t` con `v = 0`.",
        ],
        "solution": [
            "Datos: `m = 1200 kg`, `v₀ = 20 m/s`, `v = 0` y `Δx = 40 m`. Tomamos como positivo el sentido en que avanza el auto.",
            "Aceleración: de `v² = v₀² + 2·a·Δx` sale `0 = 20² + 2·a·40`, o sea `0 = 400 + 80·a` → `a = −5 m/s²`. El signo menos indica que se opone a la velocidad; su módulo es `5 m/s²`.",
            "Fuerza neta (2ª ley): `F_neta = m·a = 1200·(−5) = −6000 N`. Módulo: `6000 N`, hacia atrás. Es la fuerza que el asfalto les hace a las cubiertas; el peso y la normal se cancelan entre sí porque no hay aceleración vertical.",
            "Tiempo: `v = v₀ + a·t` → `0 = 20 − 5·t` → `t = 4 s`.",
            "Verificación: con velocidad media `(20 + 0)/2 = 10 m/s` durante `4 s` se recorren `40 m`, como dice el enunciado. Error típico: creer que hace falta una fuerza hacia adelante porque el auto 'sigue avanzando'; mientras frena, la fuerza neta apunta hacia atrás.",
        ],
    },
    {
        "id": "f-leyes-newton-2",
        "node": "f-leyes-newton",
        "kind": "problem",
        "level": 2,
        "title": "Dos patinadores que se empujan",
        "statement": (
            "En una pista de hielo (rozamiento despreciable), Lucía, de 50 kg, y Martín, de 75 kg, "
            "están quietos, frente a frente. Lucía empuja a Martín con una fuerza horizontal "
            "constante de 150 N durante 0.5 s, hasta que sus manos se separan."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué aceleración tiene Martín mientras dura el empujón? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "m/s²"},
                "answer": "2 m/s²",
            },
            {
                "prompt": "b) ¿Cuál es el módulo de la aceleración de Lucía durante el empujón? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": "m/s²"},
                "answer": "3 m/s² (en sentido contrario a la de Martín)",
            },
            {
                "prompt": "c) Cuando se sueltan, ¿con qué rapidez se aleja uno del otro (velocidad relativa)? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 2.5, "tolerance": 0, "unit": "m/s"},
                "answer": "2.5 m/s",
            },
        ],
        "hints": [
            "Hacé un diagrama de cuerpo libre para cada patinador por separado. En horizontal, ¿qué fuerza actúa sobre Lucía?",
            "Por la 3ª ley, Martín le hace a Lucía una fuerza de igual módulo (150 N) y sentido opuesto. Misma fuerza, distinta masa: distinta aceleración.",
            "Cada uno parte del reposo y acelera durante 0.5 s: `v = a·t`. Como se mueven en sentidos opuestos, las rapideces se suman.",
        ],
        "solution": [
            "Sobre Martín, la única fuerza horizontal es el empuje de Lucía (no hay rozamiento): `a_M = F/m_M = 150/75 = 2 m/s²`.",
            "Por la 3ª ley, Martín ejerce sobre Lucía una fuerza de `150 N` en sentido contrario. Es la única fuerza horizontal sobre ella: `a_L = 150/50 = 3 m/s²`, hacia el otro lado.",
            "Velocidades al terminar el empujón (parten del reposo, `t = 0.5 s`): `v_M = 2·0.5 = 1 m/s` y `v_L = 3·0.5 = 1.5 m/s`, en sentidos opuestos.",
            "Como se alejan en sentidos opuestos, la rapidez con que crece la distancia entre ellos es la suma: `1 + 1.5 = 2.5 m/s`.",
            "Respuestas: `2 m/s²`, `3 m/s²` y `2.5 m/s`. Las fuerzas del par acción-reacción son iguales, pero NO se cancelan porque actúan sobre personas distintas; la más liviana se lleva la mayor aceleración. Error típico: pensar que Lucía no se mueve porque 'es la que empuja'.",
        ],
    },
    {
        "id": "f-leyes-newton-3",
        "node": "f-leyes-newton",
        "kind": "problem",
        "level": 2,
        "title": "La heladera por la rampa del camión",
        "statement": (
            "Para cargar un camión de mudanzas subís una heladera montada sobre un carro con ruedas "
            "(80 kg en total) por una rampa de 4.5 m de largo inclinada 30° respecto del piso "
            "(sen 30° = 0.5). Empujás con una fuerza constante de 480 N paralela a la rampa y el "
            "carro parte del reposo desde el pie de la rampa. Despreciá el rozamiento y usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿Con qué aceleración sube el carro? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": "m/s²"},
                "answer": "1 m/s²",
            },
            {
                "prompt": "b) ¿Con qué velocidad llega al extremo superior de la rampa? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": "m/s"},
                "answer": "3 m/s",
            },
            {
                "prompt": "c) ¿Con qué fuerza paralela a la rampa habría que empujar para subirlo a velocidad constante? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 400, "tolerance": 0, "unit": "N"},
                "answer": "400 N",
            },
        ],
        "hints": [
            "Usá un eje paralelo a la rampa. De todo el peso, solo la componente `m·g·sen 30°` tira cuesta abajo.",
            "2ª ley en ese eje: `F − m·g·sen 30° = m·a`. Para la velocidad final no tenés el tiempo: `v² = v₀² + 2·a·Δx`.",
            "Velocidad constante significa aceleración cero, o sea fuerza neta cero.",
        ],
        "solution": [
            "Fuerzas sobre el carro: tu empuje (`480 N`, paralelo a la rampa y hacia arriba), el peso (`m·g = 80·10 = 800 N`, vertical) y la normal (perpendicular a la rampa). Elegimos un eje paralelo a la rampa, positivo hacia arriba.",
            "Componente del peso paralela a la rampa: `m·g·sen 30° = 800·0.5 = 400 N`, cuesta abajo. La normal no tiene componente en este eje.",
            "2ª ley en el eje paralelo: `480 − 400 = 80·a` → `a = 80/80 = 1 m/s²`.",
            "Velocidad arriba (parte del reposo y recorre `4.5 m`): `v² = 0² + 2·1·4.5 = 9` → `v = 3 m/s`.",
            "Velocidad constante: `a = 0`, entonces `F − 400 = 0` → `F = 400 N`. Alcanza con empatar la componente del peso paralela a la rampa.",
            "Respuestas: `1 m/s²`, `3 m/s` y `400 N`. Fijate que 400 N es la mitad de los 800 N que harían falta para levantar la carga en vertical: esa es la ventaja de la rampa. Error típico: restar el peso completo (800 N) en lugar de su componente `m·g·sen θ`.",
        ],
    },
    {
        "id": "f-leyes-newton-4",
        "node": "f-leyes-newton",
        "kind": "problem",
        "level": 3,
        "title": "La balanza en el ascensor",
        "statement": (
            "Mica, de 60 kg, se para sobre una balanza de baño dentro de un ascensor detenido en la "
            "planta baja. La balanza indica, en newtons, la fuerza normal que le hace a Mica. "
            "El ascensor arranca hacia arriba: durante los primeros 2 s la balanza marca 720 N; "
            "durante los 5 s siguientes marca 600 N; y después marca 480 N hasta que el ascensor se "
            "detiene. Suponé que en cada tramo la aceleración es constante y usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es la aceleración del ascensor en el primer tramo? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "m/s²"},
                "answer": "2 m/s², hacia arriba",
            },
            {
                "prompt": "b) ¿Con qué velocidad sube el ascensor durante el segundo tramo? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "m/s"},
                "answer": "4 m/s",
            },
            {
                "prompt": "c) ¿Qué altura total subió el ascensor desde que arrancó hasta que se detuvo? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 28, "tolerance": 0, "unit": "m"},
                "answer": "28 m",
            },
        ],
        "hints": [
            "Diagrama de cuerpo libre de Mica: solo actúan su peso (hacia abajo) y la normal de la balanza (hacia arriba). La balanza marca la normal, no el peso.",
            "En cada tramo planteá `N − m·g = m·a` con positivo hacia arriba. Si la balanza marca justo `m·g`, la aceleración es cero.",
            "En el tercer tramo la aceleración sale negativa: el ascensor sigue subiendo, pero frenando. Calculá cuánto tarda en detenerse y sumá las tres distancias.",
        ],
        "solution": [
            "Sobre Mica actúan el peso `m·g = 60·10 = 600 N` (hacia abajo) y la normal `N` de la balanza (hacia arriba). Con positivo hacia arriba, la 2ª ley es `N − m·g = m·a`. Mica tiene la misma aceleración que el ascensor.",
            "Tramo 1: `720 − 600 = 60·a₁` → `a₁ = 120/60 = 2 m/s²`, hacia arriba.",
            "Al final del tramo 1 (parte del reposo, `t = 2 s`): `v = a₁·t = 2·2 = 4 m/s`. Altura subida: `Δy₁ = ½·a₁·t² = ½·2·2² = 4 m`.",
            "Tramo 2: `600 − 600 = 60·a₂` → `a₂ = 0`. Sube a velocidad constante de `4 m/s` durante `5 s`: `Δy₂ = 4·5 = 20 m`.",
            "Tramo 3: `480 − 600 = 60·a₃` → `a₃ = −2 m/s²` (apunta hacia abajo: el ascensor frena). Tiempo hasta detenerse: `0 = 4 − 2·t` → `t = 2 s`. Altura: `Δy₃ = 4·2 − ½·2·2² = 8 − 4 = 4 m`.",
            "Altura total: `4 + 20 + 4 = 28 m`.",
            "Respuestas: `2 m/s²`, `4 m/s` y `28 m`. Error típico: creer que cuando la balanza marca menos que el peso (480 N) el ascensor está bajando. La balanza informa la ACELERACIÓN, no el sentido del movimiento: acá el ascensor sigue subiendo mientras frena.",
        ],
    },
    # ==================== DCL, ROZAMIENTO Y PLANO INCLINADO ====================
    {
        "id": "f-dcl-rozamiento-plano-1",
        "node": "f-dcl-rozamiento-plano",
        "kind": "problem",
        "level": 1,
        "title": "El cajón de herramientas que arranca",
        "statement": (
            "Un cajón de herramientas de 20 kg está en reposo sobre el piso horizontal de un taller. "
            "Entre el cajón y el piso, μₑ = 0.4 y μ_d = 0.3. Lo empujás con una fuerza horizontal "
            "de 100 N. Usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale el rozamiento estático máximo entre el cajón y el piso? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 80, "tolerance": 0, "unit": "N"},
                "answer": "80 N",
            },
            {
                "prompt": "b) ¿Con qué aceleración se mueve el cajón mientras lo empujás con 100 N? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "m/s²"},
                "answer": "2 m/s²",
            },
            {
                "prompt": "c) Una vez en movimiento, ¿con qué fuerza horizontal hay que empujarlo para que siga a velocidad constante? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 60, "tolerance": 0, "unit": "N"},
                "answer": "60 N",
            },
        ],
        "hints": [
            "En un piso horizontal y con empuje horizontal, el eje vertical da `N = m·g`. El tope del rozamiento estático es `μₑ·N`.",
            "Compará tu empuje con ese tope para saber si el cajón arranca. Si desliza, el rozamiento pasa a ser el dinámico, `μ_d·N`.",
            "Velocidad constante quiere decir `ΣFx = 0`.",
        ],
        "solution": [
            "Eje vertical: no hay aceleración ni otras fuerzas verticales, así que `N = m·g = 20·10 = 200 N`.",
            "Rozamiento estático máximo: `μₑ·N = 0.4·200 = 80 N`.",
            "Tu empuje (`100 N`) supera ese máximo, así que el cajón arranca. Mientras desliza actúa el rozamiento dinámico: `f_d = μ_d·N = 0.3·200 = 60 N`, contrario al movimiento.",
            "Eje horizontal: `100 − 60 = 20·a` → `a = 40/20 = 2 m/s²`.",
            "Velocidad constante: `F − f_d = 0` → `F = 60 N`.",
            "Respuestas: `80 N`, `2 m/s²` y `60 N`. Cuesta más arrancarlo (hay que superar 80 N) que mantenerlo en movimiento (60 N). Error típico: restar los 80 N del rozamiento estático máximo para calcular la aceleración; una vez que desliza se usa `μ_d`.",
        ],
    },
    {
        "id": "f-dcl-rozamiento-plano-2",
        "node": "f-dcl-rozamiento-plano",
        "kind": "problem",
        "level": 2,
        "title": "Empujar hacia abajo o tirar hacia arriba",
        "statement": (
            "Un baúl de 10 kg desliza sobre un piso horizontal con coeficiente de rozamiento dinámico "
            "μ_d = 0.25. Lo empujás con una fuerza de 100 N inclinada 37° hacia abajo respecto de la "
            "horizontal (sen 37° = 0.6 y cos 37° = 0.8). Usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la fuerza normal que el piso le hace al baúl? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 160, "tolerance": 0, "unit": "N"},
                "answer": "160 N",
            },
            {
                "prompt": "b) ¿Con qué aceleración avanza el baúl? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "m/s²"},
                "answer": "4 m/s²",
            },
            {
                "prompt": "c) Si en lugar de empujarlo tiraras de una soga con los mismos 100 N, inclinada 37° hacia ARRIBA de la horizontal (el baúl no se despega del piso), ¿con qué aceleración avanzaría? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": "m/s²"},
                "answer": "7 m/s²",
            },
        ],
        "hints": [
            "Descomponé la fuerza de 100 N: una componente horizontal `F·cos 37°` y una vertical `F·sen 37°`. Al empujar hacia abajo, la vertical aprieta el baúl contra el piso.",
            "La normal sale de `ΣFy = 0`; NO es `m·g`. Recién con la normal podés calcular el rozamiento `μ_d·N`.",
            "Al tirar hacia arriba, la componente vertical cambia de sentido: ahora ayuda a sostener el peso.",
        ],
        "solution": [
            "Componentes de la fuerza: horizontal `F·cos 37° = 100·0.8 = 80 N` y vertical `F·sen 37° = 100·0.6 = 60 N`. El peso es `m·g = 10·10 = 100 N`.",
            "Empujando hacia abajo, eje vertical (sin aceleración): `N − m·g − F·sen 37° = 0` → `N = 100 + 60 = 160 N`.",
            "Rozamiento dinámico: `f_d = μ_d·N = 0.25·160 = 40 N`, contrario al movimiento.",
            "Eje horizontal: `80 − 40 = 10·a` → `a = 4 m/s²`.",
            "Tirando hacia arriba: `N + F·sen 37° − m·g = 0` → `N = 100 − 60 = 40 N` (positiva: el baúl sigue apoyado). Rozamiento: `f_d = 0.25·40 = 10 N`.",
            "Eje horizontal: `80 − 10 = 10·a` → `a = 7 m/s²`.",
            "Respuestas: `160 N`, `4 m/s²` y `7 m/s²`. Con la misma fuerza y la misma componente horizontal, tirar hacia arriba rinde casi el doble porque baja la normal y, con ella, el rozamiento. Error típico: usar `N = m·g = 100 N` en los dos casos.",
        ],
    },
    {
        "id": "f-dcl-rozamiento-plano-3",
        "node": "f-dcl-rozamiento-plano",
        "kind": "problem",
        "level": 2,
        "title": "Sube por la rampa... ¿y después?",
        "statement": (
            "Lanzás un bloque de 2 kg hacia arriba por una rampa larga inclinada 37° (sen 37° = 0.6 y "
            "cos 37° = 0.8), con una velocidad inicial de 10 m/s paralela a la rampa. Entre el bloque "
            "y la rampa, μₑ = 0.6 y μ_d = 0.5. Usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el módulo de la aceleración del bloque mientras sube? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "m/s²"},
                "answer": "10 m/s² (apunta cuesta abajo: el bloque frena)",
            },
            {
                "prompt": "b) ¿Qué distancia recorre sobre la rampa hasta detenerse? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "m"},
                "answer": "5 m",
            },
            {
                "prompt": "c) ¿Qué pasa con el bloque después de detenerse en el punto más alto?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Queda en reposo: el rozamiento estático alcanza para sostenerlo",
                        "Vuelve a bajar con una aceleración de 2 m/s²",
                        "Vuelve a bajar con una aceleración de 10 m/s², la misma que al subir",
                        "Vuelve a bajar con una aceleración de 6 m/s²",
                    ],
                    "correct": 1,
                },
                "answer": "Vuelve a bajar con una aceleración de 2 m/s²: la componente del peso paralela a la rampa (12 N) supera al rozamiento estático máximo (9.6 N), y al deslizar actúa el dinámico (8 N).",
            },
        ],
        "hints": [
            "El rozamiento dinámico se opone al deslizamiento. Mientras el bloque SUBE, ¿hacia dónde apunta? ¿Y la componente del peso paralela a la rampa?",
            "Subiendo, las dos fuerzas paralelas a la rampa apuntan cuesta abajo y se suman. Con esa aceleración, usá `v² = v₀² + 2·a·Δx`.",
            "Cuando se detiene, compará `m·g·sen θ` con el rozamiento estático máximo `μₑ·N`. Si baja, el rozamiento cambia de sentido.",
        ],
        "solution": [
            "Peso: `m·g = 2·10 = 20 N`. Componente paralela a la rampa: `20·0.6 = 12 N` (cuesta abajo). Eje perpendicular: `N = m·g·cos 37° = 20·0.8 = 16 N`.",
            "Mientras sube, el rozamiento dinámico `f_d = μ_d·N = 0.5·16 = 8 N` también apunta cuesta abajo (se opone al deslizamiento). Fuerza neta: `12 + 8 = 20 N` cuesta abajo → `a = 20/2 = 10 m/s²`, frenando al bloque.",
            "Distancia hasta detenerse: `0 = 10² − 2·10·Δx` → `Δx = 100/20 = 5 m`.",
            "Arriba, en reposo: el rozamiento estático máximo es `μₑ·N = 0.6·16 = 9.6 N`, menor que los `12 N` que tiran cuesta abajo. No alcanza: el bloque vuelve a bajar. (Equivale a comprobar que `tan 37° = 0.75 > μₑ = 0.6`.)",
            "Bajando, el rozamiento dinámico (`8 N`) apunta ahora cuesta arriba: `12 − 8 = 2·a` → `a = 2 m/s²`.",
            "Respuestas: `10 m/s²`, `5 m` y vuelve a bajar con `2 m/s²`. La aceleración no es la misma de ida que de vuelta porque el rozamiento cambia de sentido: subiendo se suma a la componente del peso (`g·(sen θ + μ_d·cos θ)`) y bajando se resta (`g·(sen θ − μ_d·cos θ)`). Los 6 m/s² saldrían de olvidar el rozamiento.",
        ],
    },
    {
        "id": "f-dcl-rozamiento-plano-4",
        "node": "f-dcl-rozamiento-plano",
        "kind": "problem",
        "level": 3,
        "title": "Sostener y subir un cajón por la rampa de carga",
        "statement": (
            "Un cajón de 50 kg está apoyado sobre una rampa de carga inclinada 37° (sen 37° = 0.6 y "
            "cos 37° = 0.8). Entre el cajón y la rampa, μₑ = 0.5 y μ_d = 0.25. Un operario le aplica "
            "una fuerza F paralela a la rampa y dirigida hacia arriba. Usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el valor MÍNIMO de F para que el cajón, inicialmente quieto, no deslice hacia abajo? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 100, "tolerance": 0, "unit": "N"},
                "answer": "100 N",
            },
            {
                "prompt": "b) ¿Cuál es el valor MÁXIMO de F que se puede aplicar sin que el cajón, inicialmente quieto, empiece a subir? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 500, "tolerance": 0, "unit": "N"},
                "answer": "500 N",
            },
            {
                "prompt": "c) Una vez que el cajón ya está deslizando hacia arriba, ¿qué valor de F lo hace subir a velocidad constante? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 400, "tolerance": 0, "unit": "N"},
                "answer": "400 N",
            },
        ],
        "hints": [
            "Calculá primero las tres cantidades fijas: la componente del peso paralela a la rampa, la normal y el rozamiento estático máximo `μₑ·N`.",
            "El rozamiento estático se opone a la tendencia a deslizar. Con F mínima el cajón está por caerse cuesta abajo: ¿hacia dónde apunta el rozamiento? ¿Y con F máxima?",
            "Cuando ya desliza hacia arriba, el rozamiento es dinámico (`μ_d·N`) y apunta cuesta abajo. Velocidad constante: `ΣF = 0` en el eje paralelo.",
        ],
        "solution": [
            "Peso: `m·g = 50·10 = 500 N`. Componente paralela a la rampa: `500·0.6 = 300 N` (cuesta abajo). Eje perpendicular (F es paralela a la rampa, así que no cambia la normal): `N = 500·0.8 = 400 N`.",
            "Rozamiento estático máximo: `μₑ·N = 0.5·400 = 200 N`. Sin ayuda el cajón deslizaría, porque `300 N > 200 N`.",
            "F mínima: el cajón está a punto de deslizar hacia ABAJO, así que el rozamiento estático apunta hacia arriba y vale su máximo. Equilibrio en el eje paralelo: `F + 200 − 300 = 0` → `F = 100 N`.",
            "F máxima: el cajón está a punto de deslizar hacia ARRIBA, así que el rozamiento estático apunta hacia abajo con su valor máximo: `F − 300 − 200 = 0` → `F = 500 N`.",
            "Es decir, el cajón quieto se queda en reposo para cualquier F entre 100 N y 500 N: el rozamiento estático se ajusta en módulo y en sentido (con `F = 300 N` vale cero).",
            "Subiendo a velocidad constante: rozamiento dinámico `f_d = μ_d·N = 0.25·400 = 100 N`, cuesta abajo. `F − 300 − 100 = 0` → `F = 400 N`.",
            "Respuestas: `100 N`, `500 N` y `400 N`. Mantenerlo subiendo (400 N) cuesta menos que arrancarlo (más de 500 N), porque `μ_d < μₑ`. Error típico: poner siempre el rozamiento 'en contra de F'; el rozamiento se opone al deslizamiento (o a la tendencia a deslizar), no a la fuerza aplicada.",
        ],
    },
    # ==================== CUERPOS VINCULADOS ====================
    {
        "id": "f-cuerpos-vinculados-1",
        "node": "f-cuerpos-vinculados",
        "kind": "problem",
        "level": 1,
        "title": "Tres trineos en fila",
        "statement": (
            "En una pista de nieve dura y horizontal de Bariloche, un instructor arrastra tres trineos "
            "cargados, unidos entre sí por sogas ideales horizontales: el de adelante tiene 20 kg, el "
            "del medio 30 kg y el de atrás 50 kg. Tira del primero con una fuerza horizontal de 200 N. "
            "Despreciá el rozamiento con la nieve."
        ),
        "parts": [
            {
                "prompt": "a) ¿Con qué aceleración se mueven los trineos? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "m/s²"},
                "answer": "2 m/s²",
            },
            {
                "prompt": "b) ¿Cuánto vale la tensión de la soga que une el primer trineo con el del medio? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 160, "tolerance": 0, "unit": "N"},
                "answer": "160 N",
            },
            {
                "prompt": "c) ¿Cuánto vale la tensión de la soga que une el trineo del medio con el de atrás? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 100, "tolerance": 0, "unit": "N"},
                "answer": "100 N",
            },
        ],
        "hints": [
            "Los tres trineos tienen la misma aceleración. Tratalos como un solo cuerpo: la única fuerza externa horizontal son los 200 N.",
            "Cada soga tiene que acelerar a todo lo que viene DETRÁS de ella. Aislá esa parte del sistema y aplicá `ΣF = m·a`.",
        ],
        "solution": [
            "Las sogas son inextensibles, así que los tres trineos comparten la aceleración. Para el conjunto, las tensiones son fuerzas internas y la única fuerza externa horizontal es la del instructor: `a = F/(m₁ + m₂ + m₃) = 200/(20 + 30 + 50) = 200/100 = 2 m/s²`.",
            "Soga entre el primero y el del medio (`T₁`): aislamos los dos trineos de atrás (30 kg + 50 kg). La única fuerza horizontal sobre ese conjunto es `T₁`: `T₁ = (30 + 50)·2 = 160 N`.",
            "Soga entre el del medio y el de atrás (`T₂`): aislamos el último trineo. `T₂ = 50·2 = 100 N`.",
            "Verificación con el trineo de adelante: `200 − T₁ = 20·a` → `200 − 160 = 40 = 20·2`. Y con el del medio: `T₁ − T₂ = 160 − 100 = 60 = 30·2`. Las dos se cumplen.",
            "Respuestas: `2 m/s²`, `160 N` y `100 N`. La tensión va bajando hacia la cola porque cada soga arrastra menos masa. Error típico: suponer que los 200 N se transmiten enteros por todas las sogas.",
        ],
    },
    {
        "id": "f-cuerpos-vinculados-2",
        "node": "f-cuerpos-vinculados",
        "kind": "problem",
        "level": 2,
        "title": "Bloque en una mesa con rozamiento y balde que cuelga",
        "statement": (
            "Un bloque de 6 kg apoyado sobre una mesa horizontal está unido, mediante una soga ideal "
            "que pasa por una polea ideal ubicada en el borde, a un balde de 4 kg que cuelga a 0.5 m "
            "del piso. El coeficiente de rozamiento dinámico entre el bloque y la mesa es μ_d = 0.5. "
            "Se sueltan desde el reposo y el sistema se pone en movimiento. Usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿Con qué aceleración se mueven el bloque y el balde? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": "m/s²"},
                "answer": "1 m/s²",
            },
            {
                "prompt": "b) ¿Cuánto vale la tensión de la soga mientras se mueven? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 36, "tolerance": 0, "unit": "N"},
                "answer": "36 N",
            },
            {
                "prompt": "c) ¿Con qué velocidad llega el balde al piso? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": "m/s"},
                "answer": "1 m/s",
            },
        ],
        "hints": [
            "Un diagrama de cuerpo libre por cuerpo. Para el bloque, el eje vertical te da la normal y con ella el rozamiento `μ_d·N`.",
            "Ecuaciones con el sentido del movimiento como positivo: balde `m₂·g − T = m₂·a`; bloque `T − f_d = m₁·a`. Sumalas para eliminar T.",
            "El balde baja 0.5 m con aceleración constante partiendo del reposo: `v² = 2·a·Δy`.",
        ],
        "solution": [
            "Bloque (`m₁ = 6 kg`), eje vertical: `N = m₁·g = 60 N`. Rozamiento dinámico: `f_d = μ_d·N = 0.5·60 = 30 N`, contrario al movimiento.",
            "Ecuación del bloque (positivo hacia la polea): `T − 30 = 6·a`.",
            "Ecuación del balde (`m₂ = 4 kg`, positivo hacia abajo): `m₂·g − T = m₂·a` → `40 − T = 4·a`.",
            "Sumando las dos se cancela T: `40 − 30 = (6 + 4)·a` → `a = 10/10 = 1 m/s²`.",
            "Tensión, reemplazando en la ecuación del balde: `T = 40 − 4·1 = 36 N`. Control con el bloque: `36 − 30 = 6 = 6·1`.",
            "Velocidad del balde al llegar al piso: `v² = 2·a·Δy = 2·1·0.5 = 1` → `v = 1 m/s`.",
            "Respuestas: `1 m/s²`, `36 N` y `1 m/s`. La tensión (36 N) es menor que el peso del balde (40 N), como debe ser si baja acelerando. Errores típicos: poner `T = m₂·g = 40 N`, o dividir la fuerza neta solo por la masa del balde en lugar de la masa total.",
        ],
    },
    {
        "id": "f-cuerpos-vinculados-3",
        "node": "f-cuerpos-vinculados",
        "kind": "problem",
        "level": 2,
        "title": "Máquina de Atwood y el gancho del techo",
        "statement": (
            "Una polea ideal cuelga de un gancho fijo al techo. Por la polea pasa una soga ideal de "
            "cuyos extremos cuelgan dos pesas, una de 7 kg y otra de 3 kg. Se sueltan desde el reposo. "
            "Usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿Con qué aceleración se mueven las pesas? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "m/s²"},
                "answer": "4 m/s²",
            },
            {
                "prompt": "b) ¿Cuánto vale la tensión de la soga mientras se mueven? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 42, "tolerance": 0, "unit": "N"},
                "answer": "42 N",
            },
            {
                "prompt": "c) ¿Qué fuerza hace el gancho para sostener la polea mientras las pesas se mueven? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 84, "tolerance": 0, "unit": "N"},
                "answer": "84 N",
            },
        ],
        "hints": [
            "Una ecuación por pesa, tomando como positivo el sentido del movimiento: la de 7 kg baja y la de 3 kg sube, con la misma aceleración y la misma tensión.",
            "Sumá las ecuaciones para hallar `a` y reemplazá en cualquiera de las dos para hallar `T`.",
            "Hacé el diagrama de cuerpo libre de la POLEA: la soga tira de ella hacia abajo de los dos lados. La polea no tiene masa y su centro no se mueve.",
        ],
        "solution": [
            "Pesos: `70 N` y `30 N`. La pesa de 7 kg baja y la de 3 kg sube.",
            "Pesa de 7 kg (positivo hacia abajo): `70 − T = 7·a`. Pesa de 3 kg (positivo hacia arriba): `T − 30 = 3·a`.",
            "Sumando: `70 − 30 = 10·a` → `a = 4 m/s²`.",
            "Tensión: `T = 30 + 3·4 = 42 N`. Control con la otra pesa: `70 − 42 = 28 = 7·4`. Además `30 N < 42 N < 70 N`, como corresponde.",
            "Polea: sobre ella actúan el gancho (hacia arriba) y los dos tramos de soga, cada uno tirando hacia abajo con `T`. Como es ideal (sin masa) y su centro está quieto: `F_gancho − 2·T = 0` → `F_gancho = 2·42 = 84 N`.",
            "Respuestas: `4 m/s²`, `42 N` y `84 N`. El gancho soporta MENOS que el peso total de las pesas (100 N): soportaría los 100 N solo si estuvieran en equilibrio. Como el conjunto de las dos pesas tiene aceleración neta hacia abajo (baja la más pesada), la fuerza que lo sostiene es menor que su peso.",
        ],
    },
    {
        "id": "f-cuerpos-vinculados-4",
        "node": "f-cuerpos-vinculados",
        "kind": "problem",
        "level": 3,
        "title": "Bloque en un plano inclinado con rozamiento y contrapeso",
        "statement": (
            "Un bloque de 4 kg está apoyado sobre un plano inclinado 37° (sen 37° = 0.6 y cos 37° = 0.8). "
            "Una soga ideal, paralela al plano, lo une a través de una polea ideal ubicada en la cima "
            "con un contrapeso de 6 kg que cuelga verticalmente. Entre el bloque y el plano, μₑ = 0.6 "
            "y μ_d = 0.5. El sistema se suelta desde el reposo. Usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué hace el sistema al soltarlo?",
                "check": {
                    "type": "choice",
                    "options": [
                        "El bloque sube por el plano y el contrapeso baja",
                        "El bloque baja por el plano y el contrapeso sube",
                        "Queda en reposo: el rozamiento estático alcanza para sostenerlo",
                    ],
                    "correct": 0,
                },
                "answer": "El bloque sube por el plano y el contrapeso baja: el peso del contrapeso (60 N) supera a la componente del peso del bloque paralela al plano (24 N) en 36 N, más que el rozamiento estático máximo (19.2 N).",
            },
            {
                "prompt": "b) ¿Cuál es el módulo de la aceleración del sistema? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": "m/s²"},
                "answer": "2 m/s²",
            },
            {
                "prompt": "c) ¿Cuánto vale la tensión de la soga mientras se mueven? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 48, "tolerance": 0, "unit": "N"},
                "answer": "48 N",
            },
        ],
        "hints": [
            "Primero decidí hacia dónde TIENDE a moverse el sistema ignorando el rozamiento: compará el peso del contrapeso con la componente del peso del bloque paralela al plano.",
            "Después compará esa diferencia con el rozamiento estático máximo `μₑ·N`, con `N = m·g·cos 37°`. Si la supera, hay movimiento y el rozamiento pasa a ser dinámico, opuesto al deslizamiento.",
            "Una ecuación por cuerpo con positivo en el sentido del movimiento: contrapeso `m₂·g − T = m₂·a`; bloque `T − m₁·g·sen 37° − f_d = m₁·a`.",
        ],
        "solution": [
            "Bloque (`m₁ = 4 kg`, peso `40 N`): componente paralela al plano `40·0.6 = 24 N` (cuesta abajo) y normal `N = 40·0.8 = 32 N`. Contrapeso (`m₂ = 6 kg`): peso `60 N`.",
            "Tendencia: el contrapeso tira de la soga con hasta `60 N` y cuesta abajo tiran solo `24 N`, así que el bloque tiende a SUBIR. Para que quedara en reposo, el rozamiento estático tendría que valer `60 − 24 = 36 N`.",
            "Rozamiento estático máximo: `μₑ·N = 0.6·32 = 19.2 N`, menor que `36 N`. No alcanza: el bloque sube por el plano y el contrapeso baja.",
            "En movimiento, el rozamiento es dinámico y apunta cuesta abajo (se opone al deslizamiento): `f_d = μ_d·N = 0.5·32 = 16 N`.",
            "Ecuaciones (positivo en el sentido del movimiento). Contrapeso: `60 − T = 6·a`. Bloque: `T − 24 − 16 = 4·a`.",
            "Sumando: `60 − 24 − 16 = 10·a` → `20 = 10·a` → `a = 2 m/s²`.",
            "Tensión: `T = 60 − 6·2 = 48 N`. Control con el bloque: `48 − 24 − 16 = 8 = 4·2`.",
            "Respuestas: el bloque sube, `a = 2 m/s²` y `T = 48 N`. Errores típicos: dibujar el rozamiento antes de saber el sentido del movimiento, usar `N = m₁·g` en lugar de `m₁·g·cos θ`, o poner `T = 60 N` (el contrapeso baja acelerando, así que `T < m₂·g`).",
        ],
    },
    # ==================== MOVIMIENTO CIRCULAR Y GRAVITACIÓN ====================
    {
        "id": "f-circular-gravitacion-1",
        "node": "f-circular-gravitacion",
        "kind": "problem",
        "level": 1,
        "title": "Un disco atado a un hilo sobre una mesa de aire",
        "statement": (
            "En el laboratorio, un disco de 0.2 kg se desliza sobre una mesa de aire horizontal (sin "
            "rozamiento), atado a un hilo ideal de 0.5 m cuyo otro extremo está fijo a un clavo en el "
            "centro de la mesa. El disco describe una circunferencia con rapidez constante de 3 m/s."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la aceleración centrípeta del disco? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 18, "tolerance": 0, "unit": "m/s²"},
                "answer": "18 m/s², hacia el clavo",
            },
            {
                "prompt": "b) ¿Cuánto vale la tensión del hilo? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 3.6, "tolerance": 0, "unit": "N"},
                "answer": "3.6 N",
            },
            {
                "prompt": "c) Si el hilo se corta cuando la tensión supera los 10 N, ¿cuál es la máxima rapidez con la que puede girar el disco? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "m/s"},
                "answer": "5 m/s",
            },
        ],
        "hints": [
            "El radio de la circunferencia es el largo del hilo. `a_c = v²/r`.",
            "Hacé el diagrama de cuerpo libre: el peso y la normal se cancelan en vertical. ¿Cuál es la única fuerza horizontal? Esa es la que cumple el rol de fuerza centrípeta.",
            "Para el inciso c) despejá `v` de `T = m·v²/r` con `T = 10 N`.",
        ],
        "solution": [
            "Aceleración centrípeta: `a_c = v²/r = 3²/0.5 = 9/0.5 = 18 m/s²`, dirigida hacia el clavo (el centro).",
            "Fuerzas sobre el disco: peso y normal (verticales, se cancelan) y la tensión del hilo (horizontal, hacia el centro). La tensión es la resultante y hace de fuerza centrípeta: `T = m·a_c = 0.2·18 = 3.6 N`.",
            "Rapidez máxima: `T_máx = m·v²/r` → `10 = 0.2·v²/0.5` → `v² = 10·0.5/0.2 = 25` → `v = 5 m/s`.",
            "Respuestas: `18 m/s²`, `3.6 N` y `5 m/s`. Como la fuerza crece con `v²`, pasar de 3 m/s a 5 m/s lleva la tensión de 3.6 N a 10 N. Error típico: agregar en el diagrama una 'fuerza centrífuga' hacia afuera; la única fuerza horizontal real es la tensión, y si el hilo se corta el disco sigue derecho por la tangente.",
        ],
    },
    {
        "id": "f-circular-gravitacion-2",
        "node": "f-circular-gravitacion",
        "kind": "problem",
        "level": 2,
        "title": "Montaña rusa: la hondonada y el rulo",
        "statement": (
            "Sofía, de 50 kg, viaja sentada en el carrito de una montaña rusa. Primero pasa por el "
            "punto más bajo de una hondonada circular de 20 m de radio a 20 m/s. Más adelante pasa, "
            "cabeza abajo, por el punto más alto de un rulo vertical circular de 10 m de radio a 12 m/s. "
            "Usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿Qué fuerza le hace el asiento a Sofía en el punto más bajo de la hondonada? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 1500, "tolerance": 0, "unit": "N"},
                "answer": "1500 N, hacia arriba (el triple de su peso)",
            },
            {
                "prompt": "b) ¿Cuál es el módulo de la fuerza que le hace el asiento a Sofía en el punto más alto del rulo? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 220, "tolerance": 0, "unit": "N"},
                "answer": "220 N, hacia abajo (hacia el centro del rulo)",
            },
            {
                "prompt": "c) ¿Cuál es la velocidad mínima con la que debe pasar por el punto más alto del rulo para no despegarse del asiento? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "m/s"},
                "answer": "10 m/s",
            },
        ],
        "hints": [
            "En cada punto dibujá las dos fuerzas sobre Sofía (peso y normal del asiento) y ubicá el centro de la circunferencia: la resultante debe apuntar hacia el centro y valer `m·v²/r`.",
            "En el punto más bajo el centro está ARRIBA: `N − m·g = m·v²/r`. En el punto más alto del rulo el centro está ABAJO y, como va cabeza abajo, el asiento la empuja hacia abajo: `N + m·g = m·v²/r`.",
            "La velocidad mínima arriba corresponde al caso límite en que el asiento deja de empujar: `N = 0`.",
        ],
        "solution": [
            "Peso de Sofía: `m·g = 50·10 = 500 N`. En los dos puntos, la suma de las fuerzas en la dirección radial debe dar `m·v²/r` hacia el centro.",
            "Punto más bajo de la hondonada (centro arriba; normal hacia arriba, peso hacia abajo): `N − m·g = m·v²/r` → `N = 500 + 50·20²/20 = 500 + 1000 = 1500 N`.",
            "Punto más alto del rulo (centro abajo; el asiento está por encima de Sofía y la empuja hacia abajo, igual que el peso): `N + m·g = m·v²/r` → `N = 50·12²/10 − 500 = 720 − 500 = 220 N`.",
            "Velocidad mínima arriba: si va más despacio, hace falta menos fuerza centrípeta y la normal disminuye; el límite es `N = 0`, donde el peso solo hace de fuerza centrípeta: `m·g = m·v²/r` → `v² = g·r = 10·10 = 100` → `v = 10 m/s`. No depende de la masa.",
            "Respuestas: `1500 N`, `220 N` y `10 m/s`. En el fondo de la hondonada Sofía se siente tres veces más pesada, y arriba del rulo el asiento la sigue apretando porque `12 m/s > 10 m/s`. Error típico: escribir `N = m·g` en esos puntos o sumar una 'fuerza centrífuga'; `m·v²/r` no es una fuerza más, es lo que tiene que dar la suma de las fuerzas reales.",
        ],
    },
    {
        "id": "f-circular-gravitacion-3",
        "node": "f-circular-gravitacion",
        "kind": "problem",
        "level": 2,
        "title": "El peso de una sonda lejos de la Tierra",
        "statement": (
            "Una sonda espacial de 180 kg pesa 1800 N en la superficie de la Tierra (g = 10 m/s²). "
            "Llamamos M a la masa de la Tierra y R a su radio. La fuerza gravitatoria es "
            "`F = G·m₁·m₂/r²`, con r medida desde el CENTRO del planeta. La sonda viaja a un planeta "
            "cuya masa es M/10 y cuyo radio es R/2 (valores parecidos a los de Marte)."
        ),
        "parts": [
            {
                "prompt": "a) En el camino, ¿cuánto pesa la sonda (fuerza con que la atrae la Tierra) cuando está a una altura de 2R sobre la superficie terrestre? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 200, "tolerance": 0, "unit": "N"},
                "answer": "200 N",
            },
            {
                "prompt": "b) ¿Cuánto vale la aceleración de la gravedad en la superficie del otro planeta? Respondé solo con el número en m/s².",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": "m/s²"},
                "answer": "4 m/s²",
            },
            {
                "prompt": "c) ¿Cuánto pesa la sonda apoyada en la superficie de ese planeta? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 720, "tolerance": 0, "unit": "N"},
                "answer": "720 N",
            },
        ],
        "hints": [
            "No hace falta el valor de G: trabajá con proporciones respecto de la superficie terrestre, donde `r = R` y el peso es 1800 N.",
            "Ojo con el inciso a): la altura se mide desde la superficie, pero en la fórmula va la distancia al centro, `r = R + h`.",
            "En la superficie de un planeta, `g = G·M_planeta/R_planeta²`. Fijate por cuánto se multiplica al cambiar la masa por M/10 y el radio por R/2.",
        ],
        "solution": [
            "En la superficie terrestre: `P = G·M·m/R² = 1800 N`, y `g = G·M/R² = 10 m/s²`.",
            "A una altura `h = 2R`, la distancia al centro es `r = R + 2R = 3R`. La fuerza va como `1/r²`: al triplicar la distancia se divide por `3² = 9`. `P' = 1800/9 = 200 N`.",
            "Gravedad en el otro planeta: `g_p = G·(M/10)/(R/2)² = G·(M/10)/(R²/4) = (4/10)·G·M/R² = 0.4·10 = 4 m/s²`.",
            "Peso de la sonda allí (la masa no cambia, sigue siendo 180 kg): `P_p = m·g_p = 180·4 = 720 N`.",
            "Respuestas: `200 N`, `4 m/s²` y `720 N`. Errores típicos: en a) usar `r = 2R` (confundir altura con distancia al centro), lo que daría 450 N; en b) olvidar que el radio va al cuadrado: un radio dos veces menor multiplica la gravedad por 4, que junto con la masa 10 veces menor da el factor `4/10`.",
        ],
    },
    {
        "id": "f-circular-gravitacion-4",
        "node": "f-circular-gravitacion",
        "kind": "problem",
        "level": 3,
        "title": "Curva peraltada en una pista de pruebas",
        "statement": (
            "En una pista de pruebas hay una curva circular de 120 m de radio, peraltada 37° respecto "
            "de la horizontal (sen 37° = 0.6, cos 37° = 0.8 y tan 37° = 0.75). Una mañana de helada el "
            "pavimento está tan resbaladizo que el rozamiento lateral es despreciable. Un auto de "
            "1200 kg toma la curva con rapidez constante, sin deslizar hacia arriba ni hacia abajo del "
            "peralte. Usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿A qué velocidad está tomando la curva? Respondé solo con el número en m/s.",
                "check": {"type": "numeric", "value": 30, "tolerance": 0, "unit": "m/s"},
                "answer": "30 m/s (108 km/h)",
            },
            {
                "prompt": "b) ¿Cuánto vale la fuerza normal que la pista le hace al auto? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 15000, "tolerance": 0, "unit": "N"},
                "answer": "15000 N",
            },
            {
                "prompt": "c) Si la curva tuviera el mismo radio pero fuera plana (sin peralte), ¿qué coeficiente de rozamiento estático mínimo haría falta para tomarla a esa misma velocidad? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.75, "tolerance": 0, "unit": ""},
                "answer": "0.75",
            },
        ],
        "hints": [
            "Sin rozamiento, sobre el auto solo actúan el peso y la normal (perpendicular a la pista inclinada). La trayectoria es una circunferencia HORIZONTAL, así que la aceleración centrípeta es horizontal: conviene usar ejes horizontal y vertical, no inclinados.",
            "La normal forma 37° con la vertical. Eje vertical: `N·cos 37° = m·g`. Eje horizontal (hacia el centro): `N·sen 37° = m·v²/r`.",
            "En la curva plana, la normal es vertical (`N = m·g`) y la única fuerza hacia el centro es el rozamiento estático: `m·v²/r ≤ μₑ·m·g`.",
        ],
        "solution": [
            "Fuerzas sobre el auto (sin rozamiento): peso `m·g = 1200·10 = 12000 N`, vertical, y normal `N`, perpendicular a la pista, o sea inclinada 37° respecto de la vertical y volcada hacia el centro de la curva.",
            "El auto no sube ni baja: en el eje vertical no hay aceleración. `N·cos 37° − m·g = 0` → `N = 12000/0.8 = 15000 N`.",
            "Eje horizontal: la componente horizontal de la normal es la única fuerza hacia el centro y hace de fuerza centrípeta. `N·sen 37° = m·v²/r` → `15000·0.6 = 1200·v²/120` → `9000 = 10·v²` → `v² = 900` → `v = 30 m/s` (108 km/h).",
            "Atajo: dividiendo las dos ecuaciones, `tan 37° = v²/(r·g)` → `v² = 0.75·120·10 = 900`. La masa se simplifica: esa velocidad sirve para cualquier vehículo.",
            "Curva plana: en vertical `N = m·g = 12000 N`. Fuerza centrípeta necesaria: `m·v²/r = 1200·900/120 = 9000 N`, que solo puede aportar el rozamiento estático: `9000 ≤ μₑ·12000` → `μₑ ≥ 0.75`.",
            "Respuestas: `30 m/s`, `15000 N` y `0.75`. No es casualidad que el coeficiente coincida con `tan 37°`: en los dos casos hace falta `v²/(r·g) = 0.75`. Error típico: copiar del plano inclinado `N = m·g·cos θ` (daría 9600 N); acá la aceleración es horizontal, no paralela a la pista, y resulta `N = m·g/cos θ`, MAYOR que el peso.",
        ],
    },
    # ==================== ESTÁTICA ====================
    {
        "id": "f-estatica-1",
        "node": "f-estatica",
        "kind": "problem",
        "level": 1,
        "title": "Equilibrar el subibaja",
        "statement": (
            "El subibaja de una plaza es una tabla homogénea de 4 m de largo y 20 kg, apoyada sobre un "
            "eje ubicado justo en su centro. Benja, de 30 kg, se sienta en un extremo, a 2 m del eje. "
            "Su papá, de 75 kg, se sienta del otro lado, y el subibaja queda en equilibrio en posición "
            "horizontal, sin tocar el piso. Usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿A qué distancia del eje se sentó el papá? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 0.8, "tolerance": 0, "unit": "m"},
                "answer": "0.8 m",
            },
            {
                "prompt": "b) ¿Qué fuerza hace el eje sobre la tabla? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 1250, "tolerance": 0, "unit": "N"},
                "answer": "1250 N, hacia arriba",
            },
        ],
        "hints": [
            "Tomá momentos respecto del eje: la fuerza del eje tiene brazo cero y, como la tabla es homogénea y está apoyada en su centro, su peso también.",
            "Los momentos de los dos pesos deben compensarse: `P_Benja·d_Benja = P_papá·d_papá`.",
            "Para la fuerza del eje usá `ΣFy = 0`, sin olvidarte de ninguna de las fuerzas hacia abajo.",
        ],
        "solution": [
            "Fuerzas sobre la tabla: peso de Benja (`30·10 = 300 N`), peso del papá (`75·10 = 750 N`), peso propio de la tabla (`20·10 = 200 N`, aplicado en su centro) y la fuerza del eje, hacia arriba.",
            "Momentos respecto del eje: la fuerza del eje y el peso de la tabla pasan por ese punto, así que no hacen momento. Quedan los dos pesos, que harían girar en sentidos opuestos: `300·2 = 750·d`.",
            "Despejando: `d = 600/750 = 0.8 m`.",
            "Suma de fuerzas verticales: `R − 300 − 750 − 200 = 0` → `R = 1250 N`.",
            "Respuestas: `0.8 m` y `1250 N`. El papá pesa 2.5 veces más que Benja, así que se sienta 2.5 veces más cerca del eje. Error típico: olvidar el peso de la tabla en la suma de fuerzas porque 'no hace momento'; no hace girar, pero el eje lo tiene que sostener igual.",
        ],
    },
    {
        "id": "f-estatica-2",
        "node": "f-estatica",
        "kind": "problem",
        "level": 2,
        "title": "Semáforo colgado de dos cables distintos",
        "statement": (
            "Un semáforo de 25 kg cuelga quieto sobre una esquina, sostenido por dos cables ideales "
            "que salen del mismo punto de enganche: el de la izquierda forma 37° con la horizontal y "
            "el de la derecha forma 53° con la horizontal (sen 37° = cos 53° = 0.6 y "
            "cos 37° = sen 53° = 0.8). Usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la tensión del cable que forma 37° con la horizontal? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 150, "tolerance": 0, "unit": "N"},
                "answer": "150 N",
            },
            {
                "prompt": "b) ¿Cuánto vale la tensión del cable que forma 53° con la horizontal? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 200, "tolerance": 0, "unit": "N"},
                "answer": "200 N",
            },
        ],
        "hints": [
            "Es el equilibrio de una partícula (el punto de enganche): descomponé cada tensión en horizontal y vertical y planteá `ΣFx = 0` y `ΣFy = 0`.",
            "`ΣFx = 0` relaciona las dos tensiones: `T₁·cos 37° = T₂·cos 53°`. Los cables no son simétricos, así que las tensiones NO son iguales.",
            "Reemplazá esa relación en `ΣFy = 0`: `T₁·sen 37° + T₂·sen 53° = m·g`.",
        ],
        "solution": [
            "Peso: `m·g = 25·10 = 250 N`. Llamamos `T₁` a la tensión del cable de 37° y `T₂` a la del cable de 53°. Sobre el punto de enganche actúan `T₁` (hacia arriba y a la izquierda), `T₂` (hacia arriba y a la derecha) y el peso.",
            "Eje horizontal: `T₂·cos 53° − T₁·cos 37° = 0` → `0.6·T₂ = 0.8·T₁` → `T₂ = (4/3)·T₁`.",
            "Eje vertical: `T₁·sen 37° + T₂·sen 53° − 250 = 0` → `0.6·T₁ + 0.8·T₂ = 250`.",
            "Reemplazando `T₂ = (4/3)·T₁`: `0.6·T₁ + 0.8·(4/3)·T₁ = 250`. Multiplicando todo por 3: `1.8·T₁ + 3.2·T₁ = 750` → `5·T₁ = 750` → `T₁ = 150 N`.",
            "Entonces `T₂ = (4/3)·150 = 200 N`.",
            "Verificación: horizontal `150·0.8 = 120 N` y `200·0.6 = 120 N` (se cancelan); vertical `150·0.6 + 200·0.8 = 90 + 160 = 250 N` (igual al peso). Respuestas: `150 N` y `200 N`. El cable más vertical carga más. Error típico: repartir 125 N a cada cable, o creer que las tensiones deben sumar 250 N: suman 350 N, porque solo sus componentes verticales sostienen el peso.",
        ],
    },
    {
        "id": "f-estatica-3",
        "node": "f-estatica",
        "kind": "problem",
        "level": 2,
        "title": "Un tablón con voladizo",
        "statement": (
            "En una obra, un tablón homogéneo de 6 m de largo y 30 kg descansa horizontal sobre dos "
            "caballetes: el caballete A está en el extremo izquierdo y el caballete B a 4 m de A, de "
            "modo que 2 m del tablón quedan en voladizo. El tablón está simplemente apoyado (no está "
            "clavado ni atado). Un albañil de 60 kg se para sobre el tablón a 1 m de A. "
            "Usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) Con el albañil a 1 m de A, ¿cuánto vale la reacción del caballete B? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 375, "tolerance": 0, "unit": "N"},
                "answer": "375 N",
            },
            {
                "prompt": "b) En esa misma posición, ¿cuánto vale la reacción del caballete A? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 525, "tolerance": 0, "unit": "N"},
                "answer": "525 N",
            },
            {
                "prompt": "c) Después el albañil camina hacia el voladizo. ¿Hasta qué distancia más allá de B puede llegar sin que el tablón vuelque? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 0.5, "tolerance": 0, "unit": "m"},
                "answer": "0.5 m",
            },
        ],
        "hints": [
            "El peso del tablón homogéneo se aplica en su centro, a 3 m de A. Tomá momentos respecto de A para que `R_A` no aparezca.",
            "Con `R_B` calculada, `ΣFy = 0` te da `R_A`.",
            "El tablón está por volcar cuando se despega del caballete A, es decir, cuando `R_A = 0`. En ese instante tomá momentos respecto de B.",
        ],
        "solution": [
            "Fuerzas sobre el tablón: su peso `30·10 = 300 N` aplicado en el centro (a 3 m de A), el peso del albañil `60·10 = 600 N` (a 1 m de A) y las reacciones `R_A` (en A) y `R_B` (a 4 m de A), hacia arriba.",
            "Momentos respecto de A (`R_A` tiene brazo cero): `R_B·4 − 600·1 − 300·3 = 0` → `R_B·4 = 600 + 900 = 1500` → `R_B = 375 N`.",
            "Suma de fuerzas verticales: `R_A + R_B = 600 + 300 = 900` → `R_A = 900 − 375 = 525 N`.",
            "Control con momentos respecto de B: `R_A·4 = 600·3 + 300·1 = 2100` → `R_A = 525 N`. Coincide.",
            "Vuelco: cuando el albañil pasa al voladizo, su peso tiende a hacer girar el tablón alrededor de B y la reacción en A disminuye. El límite es `R_A = 0` (un apoyo simple no puede tirar hacia abajo).",
            "En ese límite, momentos respecto de B: el peso del tablón actúa 1 m a la izquierda de B (su centro está a 3 m de A y B a 4 m) y el albañil a una distancia `x` a la derecha: `300·1 = 600·x` → `x = 0.5 m`.",
            "Respuestas: `375 N`, `525 N` y `0.5 m`. Aunque hay 2 m de voladizo, solo puede usar el primer medio metro. Error típico: aplicar el peso del tablón en el punto medio entre los caballetes (a 2 m de A) en lugar de en el centro del tablón (a 3 m de A).",
        ],
    },
    {
        "id": "f-estatica-4",
        "node": "f-estatica",
        "kind": "problem",
        "level": 3,
        "title": "La escalera del pintor",
        "statement": (
            "Una escalera homogénea de 5 m de largo y 12 kg está apoyada contra una pared vertical "
            "lisa (sin rozamiento): su pie está sobre el piso horizontal, a 3 m de la pared, y su "
            "extremo superior toca la pared a 4 m de altura. Entre el pie de la escalera y el piso "
            "el coeficiente de rozamiento estático es μₑ = 0.5. Un pintor de 60 kg va a subir por "
            "ella. Usá g = 10 m/s²."
        ),
        "parts": [
            {
                "prompt": "a) Antes de que suba el pintor, ¿qué fuerza le hace la pared a la escalera? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 45, "tolerance": 0, "unit": "N"},
                "answer": "45 N, horizontal",
            },
            {
                "prompt": "b) Cuando el pintor está parado a 2 m del pie, medidos a lo largo de la escalera, ¿cuánto vale el rozamiento que el piso le hace a la escalera? Respondé solo con el número en N.",
                "check": {"type": "numeric", "value": 225, "tolerance": 0, "unit": "N"},
                "answer": "225 N",
            },
            {
                "prompt": "c) ¿Hasta qué distancia del pie, medida a lo largo de la escalera, puede subir el pintor antes de que la escalera empiece a resbalar? Respondé solo con el número en m.",
                "check": {"type": "numeric", "value": 3.5, "tolerance": 0, "unit": "m"},
                "answer": "3.5 m",
            },
        ],
        "hints": [
            "Fuerzas sobre la escalera: los pesos (verticales), la normal del piso (vertical), el rozamiento del piso (horizontal, hacia la pared) y la normal de la pared (horizontal, porque la pared es lisa). Tomá momentos respecto del PIE: ahí se anulan dos incógnitas.",
            "Respecto del pie, el brazo de un peso es la distancia HORIZONTAL hasta su recta de acción: un punto a una distancia `d` sobre la escalera está a `d·3/5` del pie en horizontal. El brazo de la normal de la pared es la altura, 4 m.",
            "`ΣFx = 0` dice que el rozamiento iguala a la fuerza de la pared, y `ΣFy = 0` da la normal del piso. La escalera resbala cuando el rozamiento necesario llega a `μₑ·N_piso`.",
        ],
        "solution": [
            "Geometría: la escalera, el piso y la pared forman un triángulo 3-4-5, así que un punto ubicado a una distancia `d` del pie medida sobre la escalera está a `0.6·d` del pie en horizontal. Fuerzas: peso de la escalera `120 N` en su centro (`d = 2.5 m`), peso del pintor `600 N`, normal del piso `N` y rozamiento `f` en el pie, y normal de la pared `N_p`, horizontal, a 4 m de altura.",
            "Escalera sola, momentos respecto del pie (`N` y `f` tienen brazo cero): `N_p·4 − 120·(0.6·2.5) = 0` → `N_p·4 = 120·1.5 = 180` → `N_p = 45 N`.",
            "Con el pintor a `d = 2 m` del pie (brazo horizontal `0.6·2 = 1.2 m`): `N_p·4 = 120·1.5 + 600·1.2 = 180 + 720 = 900` → `N_p = 225 N`.",
            "Eje horizontal: las únicas fuerzas horizontales son `N_p` y el rozamiento del piso, así que `f = N_p = 225 N`, apuntando hacia la pared.",
            "¿Aguanta? Eje vertical: `N = 120 + 600 = 720 N`, entonces el rozamiento estático máximo es `μₑ·N = 0.5·720 = 360 N`. Como `225 N < 360 N`, la escalera no resbala.",
            "Posición límite: con el pintor a una distancia `d`, `N_p·4 = 180 + 600·0.6·d` → `N_p = 45 + 90·d`, que crece a medida que sube. La escalera empieza a resbalar cuando `f = N_p` alcanza el máximo: `45 + 90·d = 360` → `d = 315/90 = 3.5 m`.",
            "Respuestas: `45 N`, `225 N` y `3.5 m` (de los 5 m de escalera). Cuanto más alto está el pintor, más empuja la pared y más rozamiento hace falta, aunque la normal del piso no cambie. Errores típicos: usar como brazo de los pesos la distancia medida sobre la escalera en lugar de la horizontal, o suponer que el rozamiento vale siempre `μₑ·N`.",
        ],
    },
]
