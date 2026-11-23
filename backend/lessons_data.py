"""Rich 5-step interactive beginner lessons for all 32 curriculum nodes.

Each lesson follows evidence-based cognitive-science scaffolding:
  1. hook       — Everyday intuition & misconception breaker ("¿Por qué importa?")
  2. concept    — Clear step-by-step explanation, key rule, and common pitfall
  3. example    — Concrete worked walkthrough (plus optional Lab deep-link)
  4. check      — Interactive ConcepTest (multiple-choice with feedback per option)
  5. takeaway   — Summary prompt to write in your own words (Feynman) before FSRS practice
"""

from __future__ import annotations

from typing import Any

from backend.clyrp_content import CLYRP_LESSONS
from backend.math_content import MATH_LESSONS
from backend.physics_content import PHYSICS_LESSONS

LESSONS_BY_SLUG: dict[str, dict[str, Any]] = {
    # ==================== GUITARRA (8) ====================
    "g-postura-afinacion": {
        "hook": {
            "question": "¿Por qué a casi todo principiante le trastean o suenan apagadas las cuerdas el primer día?",
            "intuition": "No es por falta de fuerza en los dedos: suele ser por pisar en el medio del traste y con la muñeca tensa. Una postura relajada hace que la guitarra suene limpia con la mitad de esfuerzo.",
        },
        "concept": {
            "points": [
                "Las cuerdas se cuentan de abajo hacia arriba: 1ª es la más fina (aguda) y 6ª es la más gruesa (grave).",
                "Afinación estándar de 6ª a 1ª: Mi – La – Re – Sol – Si – Mi (en cifrado americano: E – A – D – G – B – E).",
                "Mano izquierda: dedo 1=índice, 2=medio, 3=anular, 4=meñique. El pulgar va apoyado atrás del mástil, sin apretar como pinza.",
                "Regla del traste: pisá justo detrás de la varilla metálica (hacia el cuerpo de la guitarra), usando la punta del dedo arqueado.",
            ],
            "key_rule": "E – A – D – G – B – E · Yema arqueada justo detrás de la varilla metálica.",
            "pitfall": "Apretar con demasiada fuerza o apoyar la palma contra el borde del mástil apaga las cuerdas vecinas y cansa la mano.",
        },
        "example": {
            "title": "Prueba de limpieza en 30 segundos",
            "steps": [
                "Abrí el Afinador en el Laboratorio de Guitarra y tocá la 6ª cuerda (E2) comparando el tono con tu guitarra.",
                "Apoyá el dedo 1 en el traste 2 de la 4ª cuerda, justo antes de la varilla metálica.",
                "Pulsá la cuerda suavemente: si suena zumbido, acercá el dedo un milímetro más a la varilla sin apretar más fuerte.",
            ],
            "lab_link": "guitar:tuner",
            "lab_cta": "Probar en el Afinador de Referencia",
        },
        "check": {
            "question": "Si al pisar el traste 2 escuchás un zumbido metálico (trasteo), ¿cuál es el primer ajuste más efectivo?",
            "options": [
                {"text": "Apretar mucho más fuerte con el pulgar", "ok": False, "feedback": "Más fuerza genera tensión y fatiga; primero corregí la ubicación del dedo."},
                {"text": "Acercar la punta del dedo justo detrás de la varilla del traste 2", "ok": True, "feedback": "Exacto: en ese punto necesitás la mínima presión para que la cuerda vibre limpia."},
                {"text": "Pisar exactamente encima de la varilla metálica", "ok": False, "feedback": "Pisar encima de la varilla apaga la vibración de la cuerda."},
            ],
        },
        "checks": [
            {
                "question": "El afinador te pide ajustar la nota Re (D). ¿Qué cuerda al aire tenés que tocar?",
                "options": [
                    {"text": "La 3ª cuerda", "ok": False, "feedback": "La 3ª es Sol (G); llegás a ese error si contás desde la más gruesa, pero la numeración arranca en la más fina."},
                    {"text": "La 4ª cuerda", "ok": True, "feedback": "Exacto: de 6ª a 1ª es E–A–D–G–B–E, así que Re (D) cae en la 4ª."},
                    {"text": "La 5ª cuerda", "ok": False, "feedback": "La 5ª es La (A); Re (D) es la siguiente hacia las finas, la 4ª."},
                ],
            },
            {
                "question": "Un diagrama indica 'dedo 3 en la 2ª cuerda'. ¿Qué dedo usás y sobre qué cuerda?",
                "options": [
                    {"text": "El medio, sobre la cuerda La (A)", "ok": False, "feedback": "El pulgar no se numera: el 3 es el anular, y la 2ª cuerda es Si (B), no La."},
                    {"text": "El anular, sobre la cuerda La (A), la segunda más gruesa", "ok": False, "feedback": "El dedo está bien, pero las cuerdas se cuentan desde la más fina: la 2ª es Si (B)."},
                    {"text": "El anular, sobre la cuerda Si (B), la segunda más fina", "ok": True, "feedback": "Exacto: 1=índice, 2=medio, 3=anular, y la 2ª cuerda es Si (B)."},
                ],
            },
        ],
        "takeaway_prompt": "Escribí en una frase el orden de las 6 cuerdas y dónde debe caer la yema del dedo.",
    },
    "g-acordes-em-am": {
        "hook": {
            "question": "¿Sabías que con solo dos acordes (Em y Am) ya podés entrenar el movimiento de bloque que usan los guitarristas expertos?",
            "intuition": "El secreto de cambiar rápido de acorde no es mover los dedos velozmente uno por uno, sino moverlos juntos en bloque mientras viajan en el aire.",
        },
        "concept": {
            "points": [
                "Mi menor (Em): dedo 2 en 5ª cuerda traste 2, dedo 3 en 4ª cuerda traste 2. Rasgueás las 6 cuerdas.",
                "La menor (Am): bajás exactamente esos dos dedos una cuerda cada uno (4ª y 3ª traste 2) y sumás el dedo 1 en 2ª cuerda traste 1.",
                "En Am evitás la 6ª cuerda (empezás a rasguear desde la 5ª, que es La al aire).",
                "Antes de medir velocidad, tocá cada cuerda de una en una (arpegio lento) para verificar que ninguna suene muda.",
            ],
            "key_rule": "Em y Am comparten el bloque de dedos 2–3: bajalos juntos una cuerda.",
            "pitfall": "Aplastar el dedo 1 en Am hace que la 1ª cuerda (Mi agudo) quede apagada.",
        },
        "example": {
            "title": "Cómo entrenar Em ↔ Am sin grabar errores",
            "steps": [
                "Armá Em, escuchá el acorde limpio en el Laboratorio de Guitarra y tocá cuerda por cuerda (6ª a 1ª).",
                "Despegá suavemente el bloque 2–3, bajalo una cuerda y caé junto con el dedo 1 en Am.",
                "Hacé 1 minuto medido en el Laboratorio de Guitarra contando solo cambios limpios y cerrá con 3 cambios lentos perfectos (overlearning).",
            ],
            "lab_link": "guitar:chords",
            "lab_cta": "Practicar Em ↔ Am con audio",
        },
        "check": {
            "question": "¿Por qué en La menor (Am) se empieza a rasguear desde la 5ª cuerda y no desde la 6ª?",
            "options": [
                {"text": "Porque la 5ª cuerda al aire es La (la nota raíz del acorde)", "ok": True, "feedback": "Correcto: empezar en la nota raíz hace que el acorde suene claro y definido."},
                {"text": "Porque la 6ª cuerda está desafinada", "ok": False, "feedback": "La 6ª es Mi, que pertenece al acorde pero enturbia el bajo si suena más grave que La."},
                {"text": "Porque los acordes menores solo usan 4 cuerdas", "ok": False, "feedback": "Em usa las 6 cuerdas y Am usa 5; depende de dónde está la raíz."},
            ],
        },
        "checks": [
            {
                "question": "Estás en Em y querés pasar a Am. ¿Qué hacen los dedos 2 y 3?",
                "options": [
                    {"text": "Bajan juntos una cuerda cada uno (a la 4ª y la 3ª), sin cambiar de traste", "ok": True, "feedback": "Exacto: el bloque 2–3 se mueve entero y solo falta sumar el dedo 1 en la 2ª cuerda, traste 1."},
                    {"text": "Se quedan donde están y solo agregás el dedo 1", "ok": False, "feedback": "Si no bajás el bloque seguís teniendo la forma de Em con una nota de más, no Am."},
                    {"text": "Suben los dos al traste 3", "ok": False, "feedback": "El traste no cambia (siguen en el 2); lo que cambia es la cuerda que pisa cada dedo."},
                ],
            },
            {
                "question": "Tocás Am cuerda por cuerda y la 1ª suena apagada. ¿Qué revisás primero?",
                "options": [
                    {"text": "Si estás apretando la 1ª cuerda en el traste 1", "ok": False, "feedback": "En Am la 1ª cuerda va al aire; no hay que pisarla."},
                    {"text": "Si rasgueaste también la 6ª cuerda", "ok": False, "feedback": "Tocar la 6ª ensucia el bajo, pero no apaga la 1ª cuerda."},
                    {"text": "Si el dedo 1 está aplastado y roza la 1ª cuerda", "ok": True, "feedback": "Exacto: arqueando el dedo 1 y pisando con la punta, la 1ª cuerda queda libre para sonar."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué movimiento mínimo transforma Em en Am.",
    },
    "g-acordes-d-a-e": {
        "hook": {
            "question": "¿Cómo hacen los guitarristas para cambiar entre D, A y E sin mirar el mástil?",
            "intuition": "Usan un 'dedo ancla': un dedo que casi no se despega de su cuerda y guía a los demás como un riel.",
        },
        "concept": {
            "points": [
                "Re mayor (D): dedo 1 en 3ª traste 2, dedo 2 en 1ª traste 2, dedo 3 en 2ª traste 3. Rasguear desde la 4ª cuerda.",
                "La mayor (A) con digitación moderna 2-1-3: dedo 1 queda en 3ª traste 2 (¡exactamente igual que en D!), dedo 2 en 4ª traste 2 y dedo 3 en 2ª traste 2.",
                "Mi mayor (E): deslizás el mismo dedo 1 por la 3ª cuerda del traste 2 al traste 1, y colocás dedos 2 y 3 como en Em.",
            ],
            "key_rule": "El dedo índice (1) permanece sobre la 3ª cuerda al viajar entre D, A y E.",
            "pitfall": "En D, dejar que la yema del dedo 3 se incline hacia abajo suele silenciar la 1ª cuerda.",
        },
        "example": {
            "title": "Transición D → A → E con dedo ancla",
            "steps": [
                "Armá D y verificá con arpegio desde la 4ª cuerda.",
                "Mantené el dedo 1 pegado a la 3ª cuerda traste 2 y acercá los dedos 2 y 3 para formar A.",
                "Deslizá el dedo 1 al traste 1 de la 3ª cuerda mientras 2 y 3 suben al traste 2 (5ª y 4ª) para formar E.",
            ],
            "lab_link": "guitar:chords",
            "lab_cta": "Probar cambios D ↔ A ↔ E",
        },
        "check": {
            "question": "Al usar la digitación moderna (2-1-3) de La mayor (A), ¿qué ventaja clave ganás?",
            "options": [
                {"text": "El dedo índice (1) funciona como ancla fija en la 3ª cuerda para cambiar a D y E", "ok": True, "feedback": "Exacto: menos movimiento aéreo significa cambios más rápidos y precisos."},
                {"text": "Permite rasguear la 6ª cuerda en D", "ok": False, "feedback": "Re mayor sigue rasgueándose desde la 4ª cuerda."},
                {"text": "Solo usa dos dedos", "ok": False, "feedback": "A mayor utiliza 3 dedos en el traste 2."},
            ],
        },
        "checks": [
            {
                "question": "Rasgueás Re mayor (D) y el acorde suena turbio en los graves. ¿Cuál es la causa más probable?",
                "options": [
                    {"text": "Estás tocando también la 6ª y la 5ª cuerda", "ok": True, "feedback": "Exacto: D se rasguea desde la 4ª cuerda (Re al aire); las dos más graves embarran el bajo."},
                    {"text": "Te falta pisar la 6ª cuerda en el traste 2", "ok": False, "feedback": "En D la 6ª cuerda no se pisa ni se toca."},
                    {"text": "D se toca solo con las tres cuerdas más finas", "ok": False, "feedback": "La 4ª al aire es Re, la raíz del acorde, y sí se toca."},
                ],
            },
            {
                "question": "Para pasar de A (digitación 2-1-3) a E, ¿qué hace el dedo 1?",
                "options": [
                    {"text": "Se levanta y salta a la 5ª cuerda", "ok": False, "feedback": "Así perdés el ancla: los que van a la 5ª y la 4ª cuerda son los dedos 2 y 3."},
                    {"text": "Se desliza por la 3ª cuerda del traste 2 al traste 1 sin despegarse", "ok": True, "feedback": "Exacto: el dedo 1 funciona como riel y guía a los dedos 2 y 3 hacia la 5ª y la 4ª cuerda."},
                    {"text": "Se queda quieto en el traste 2 de la 3ª cuerda", "ok": False, "feedback": "En E el dedo 1 pisa el traste 1 de la 3ª cuerda; si queda en el 2, el acorde ya no es Mi mayor."},
                ],
            },
        ],
        "takeaway_prompt": "Anotá desde qué cuerda se rasguea cada uno (D, A, E) y cuál es tu dedo ancla.",
    },
    "g-ritmo-4-4": {
        "hook": {
            "question": "¿Por qué alguien que sabe 10 acordes puede sonar menos musical que alguien que solo sabe 2 pero mantiene el ritmo?",
            "intuition": "En música, el pulso manda. Si tu mano derecha funciona como un péndulo constante que nunca se frena, hasta un acorde imperfecto suena como una canción real.",
        },
        "concept": {
            "points": [
                "Contá en voz alta '1 y 2 y 3 y 4 y' (corcheas): en los números tu mano BAJA (↓), en los 'y' tu mano SUBE (↑).",
                "El secreto del péndulo: tu brazo sigue subiendo y bajando siempre; para crear silencios o patrones simplemente pasás por el aire sin tocar las cuerdas.",
                "Patrón universal de guitarra: ↓  (aire↑)  ↓ ↑  (aire↓) ↑ ↓ ↑ → se cuenta '1  2 y  y 4 y'.",
            ],
            "key_rule": "La mano derecha es el metrónomo: baja en los números, sube en los 'y', nunca se detiene.",
            "pitfall": "Frenar la mano derecha mientras buscás el acorde con la izquierda rompe el pulso de la canción.",
        },
        "example": {
            "title": "Dominar el patrón universal a 55 BPM",
            "steps": [
                "Apoyá suavemente la mano izquierda sobre las cuerdas (sin apretar) para hacer sonido percusivo.",
                "Poné el metrónomo del Laboratorio de Guitarra en 55 BPM (4/4) y mové el antebrazo en péndulo constante.",
                "Recién cuando el patrón salga automático 4 vueltas seguidas, agregá el acorde Em.",
            ],
            "lab_link": "guitar:metronome",
            "lab_cta": "Practicar ritmo con el metrónomo",
        },
        "check": {
            "question": "En el patrón universal (↓  ↓↑  ↑↓↑), ¿qué hace tu mano derecha exactamente en el pulso 3?",
            "options": [
                {"text": "Se detiene quieta esperando el pulso 4", "ok": False, "feedback": "Si la frenás perdés la referencia del péndulo."},
                {"text": "Baja pasando por el aire sin golpear las cuerdas, para quedar lista y subir en el 'y' del 3", "ok": True, "feedback": "Exacto: el golpe fantasma en el aire es el truco que mantiene el groove impecable."},
                {"text": "Rasguea hacia arriba", "ok": False, "feedback": "Los números (1, 2, 3, 4) siempre corresponden a movimiento descendente."},
            ],
        },
        "checks": [
            {
                "question": "Contando '1 y 2 y 3 y 4 y', ¿hacia dónde se mueve tu mano en el 'y' del 2?",
                "options": [
                    {"text": "Hacia abajo (↓)", "ok": False, "feedback": "Hacia abajo van los números; los 'y' siempre son el movimiento de subida."},
                    {"text": "Queda quieta esperando el 3", "ok": False, "feedback": "El péndulo nunca se frena: si no toca, pasa por el aire, pero se mueve igual."},
                    {"text": "Hacia arriba (↑)", "ok": True, "feedback": "Exacto: la mano baja en los números y sube en cada 'y'."},
                ],
            },
            {
                "question": "En medio de una canción, el acorde nuevo no te llega a tiempo. ¿Qué hace la mano derecha?",
                "options": [
                    {"text": "Sigue el péndulo sin frenar, aunque el acorde suene incompleto", "ok": True, "feedback": "Exacto: el pulso manda; un acorde a medio armar en tiempo suena mejor que uno perfecto pero tarde."},
                    {"text": "Frena hasta que la mano izquierda termine de armar el acorde", "ok": False, "feedback": "Frenar la derecha rompe el pulso, que es lo que más se nota al escuchar."},
                    {"text": "Acelera después para recuperar el tiempo perdido", "ok": False, "feedback": "Acelerar también rompe el pulso; la mano derecha es el metrónomo y va siempre pareja."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras por qué la mano derecha nunca debe detener el movimiento pendular.",
    },
    "g-acordes-g-c": {
        "hook": {
            "question": "¿Por qué el cambio entre G y C es el primer gran muro de todo guitarrista principiante?",
            "intuition": "Porque requiere abrir los dedos en diagonal y cambiar la altura de la muñeca. Si aislás solo ese movimiento en cámara lenta, el cerebro aprende la trayectoria en pocos días.",
        },
        "concept": {
            "points": [
                "Sol mayor (G): 6ª traste 3, 5ª traste 2, 1ª traste 3. Rasgueás las 6 cuerdas.",
                "Do mayor (C): 5ª traste 3 (dedo 3), 4ª traste 2 (dedo 2), 2ª traste 1 (dedo 1). Rasgueás desde la 5ª cuerda.",
                "Tip clave para G ↔ C: probá la digitación de G con dedos 3–2–4 (anular en 6ª, medio en 5ª, meñique en 1ª) porque los dedos 3 y 2 solo tienen que bajar una cuerda para convertirse en C.",
                "Bajá el pulgar hacia el centro trasero del mástil al armar C para arquear bien el dedo 1 y liberar la 1ª cuerda.",
            ],
            "key_rule": "Visualizá el destino antes de despegar los dedos; aterrizá los dedos graves primero.",
            "pitfall": "Tocar G ↔ C demasiado rápido y desprolijo graba el tropiezo en la memoria muscular.",
        },
        "example": {
            "title": "Aislamiento de transición G ↔ C",
            "steps": [
                "Armá C y verificá que la 1ª cuerda suene cristalina al aire.",
                "Hacé 5 cambios en cámara súper lenta buscando que todos los dedos caigan casi juntos.",
                "Registrá tu marca de 1 minuto en el Laboratorio de Guitarra (meta inicial: 20 cambios limpios).",
            ],
            "lab_link": "guitar:chords",
            "lab_cta": "Entrenar G ↔ C",
        },
        "check": {
            "question": "Al tocar Do mayor (C), la 1ª cuerda suena apagada ('tuc'). ¿Cuál es la causa más común?",
            "options": [
                {"text": "La parte inferior del dedo 1 (en 2ª cuerda traste 1) está rozando la 1ª cuerda", "ok": True, "feedback": "Exacto: bajar un poco el pulgar detrás del mástil arquea el dedo 1 y libera la 1ª cuerda."},
                {"text": "Hay que apretar la 1ª cuerda en el traste 1", "ok": False, "feedback": "En C mayor, la 1ª cuerda va al aire (traste 0)."},
                {"text": "Falta rasguear la 6ª cuerda", "ok": False, "feedback": "La 6ª cuerda no se toca en C mayor."},
            ],
        },
        "checks": [
            {
                "question": "¿Qué ganás al armar G con los dedos 3–2–4 si el acorde siguiente es C?",
                "options": [
                    {"text": "El meñique queda libre para descansar", "ok": False, "feedback": "En esa digitación el meñique sí trabaja: pisa la 1ª cuerda en el traste 3."},
                    {"text": "Los dedos 3 y 2 solo tienen que bajar una cuerda cada uno para formar C", "ok": True, "feedback": "Exacto: el 3 pasa de la 6ª a la 5ª y el 2 de la 5ª a la 4ª, casi sin recorrido."},
                    {"text": "Podés rasguear C desde la 6ª cuerda", "ok": False, "feedback": "C se rasguea desde la 5ª cuerda con cualquier digitación de G."},
                ],
            },
            {
                "question": "¿Qué cuerdas se rasguean en cada acorde?",
                "options": [
                    {"text": "G: las 6 cuerdas; C: desde la 5ª", "ok": True, "feedback": "Exacto: G usa las 6, y en C arrancás en la 5ª, donde está su raíz (Do, traste 3)."},
                    {"text": "Los dos con las 6 cuerdas", "ok": False, "feedback": "En C la 6ª cuerda no se toca: se rasguea desde la 5ª."},
                    {"text": "G: desde la 5ª; C: las 6 cuerdas", "ok": False, "feedback": "Es al revés: G lleva las 6 cuerdas y C arranca en la 5ª."},
                ],
            },
        ],
        "takeaway_prompt": "Anotá qué ajuste postural te ayuda a que la 1ª cuerda suene limpia en Do mayor (C).",
    },
    "g-primera-cancion": {
        "hook": {
            "question": "¿Cómo una misma secuencia de 4 acordes (G – D – Em – C) sirve para tocar cientos de canciones famosas?",
            "intuition": "Esa progresión (I–V–vi–IV) crea un viaje perfecto de reposo, tensión, emoción y regreso. Practicarla por fragmentos une todo lo que aprendiste hasta hoy.",
        },
        "concept": {
            "points": [
                "Progresión I–V–vi–IV en Sol mayor: 1 compás de G → 1 de D → 1 de Em → 1 de C.",
                "Técnica de Chunking (fragmentos): si te trabás entre D y Em, NO vuelvas al principio de la canción; aislá solo D ↔ Em 5 veces limpias y recién ahí reconectá toda la vuelta.",
                "Anticipación: en el último 'y' del pulso 4, despegar suavemente la mano izquierda (tocando cuerdas al aire un instante) te regala tiempo para caer exacto en el pulso 1 del siguiente acorde.",
            ],
            "key_rule": "Aislá el enlace que falla, nunca practiques desde el principio por inercia.",
            "pitfall": "Frenar el compás para acomodar los dedos: preferí un acorde a medio armar en tiempo que un acorde perfecto fuera de ritmo.",
        },
        "example": {
            "title": "Progresión guiada en tiempo real",
            "steps": [
                "Abrí el Laboratorio de Guitarra → Metrónomo y elegí 'I–V–vi–IV (G - D - Em - C)' a 60 BPM.",
                "Tocá solo un rasgueo largo en el pulso 1 de cada compás para automatizar los cambios.",
                "Cuando logres 4 vueltas limpias, pasá al patrón ↓  ↓↑  ↑↓↑ y registrá tu BPM en la Escalera.",
            ],
            "lab_link": "guitar:metronome",
            "lab_cta": "Tocar G – D – Em – C con metrónomo guiado",
        },
        "check": {
            "question": "Si siempre tropezás al pasar de Em a C dentro de la canción, ¿qué indica la práctica deliberada?",
            "options": [
                {"text": "Volver siempre al primer acorde (G) para agarrar envión", "ok": False, "feedback": "Repetir lo que ya sabés desperdicia energía y refuerza la tensión antes del fallo."},
                {"text": "Aislar únicamente la transición Em ↔ C lentamente hasta hacer 5 repeticiones limpias y luego reconectar", "ok": True, "feedback": "Exacto: aislar el micro-fallo acelera drásticamente el aprendizaje motor."},
                {"text": "Subir 20 BPM para forzar la velocidad", "ok": False, "feedback": "Subir tempo con errores graba los errores en tu memoria muscular."},
            ],
        },
        "checks": [
            {
                "question": "¿Para qué sirve despegar la mano izquierda en el último 'y' del pulso 4?",
                "options": [
                    {"text": "Para dejar un silencio entre acorde y acorde", "ok": False, "feedback": "No hay silencio: la mano derecha sigue rasgueando y suenan las cuerdas al aire un instante."},
                    {"text": "Para que la mano derecha pueda descansar", "ok": False, "feedback": "La derecha nunca frena; la anticipación es un recurso de la mano izquierda."},
                    {"text": "Para ganar tiempo y caer justo en el pulso 1 del acorde siguiente", "ok": True, "feedback": "Exacto: salís un instante antes para llegar en tiempo al acorde nuevo."},
                ],
            },
            {
                "question": "Tocás I–V–vi–IV en Sol mayor con un compás por acorde. ¿Qué acorde suena en el tercer compás?",
                "options": [
                    {"text": "D", "ok": False, "feedback": "D es el V y ocupa el segundo compás."},
                    {"text": "Em", "ok": True, "feedback": "Exacto: el orden es G → D → Em → C, y el vi (Em) cae en el tercer compás."},
                    {"text": "C", "ok": False, "feedback": "C es el IV y cierra la vuelta en el cuarto compás."},
                ],
            },
        ],
        "takeaway_prompt": "Escribí tu estrategia de 3 pasos cuando una transición dentro de una canción se traba.",
    },
    "g-oido-musical": {
        "hook": {
            "question": "¿Por qué un solo semitono (un único traste de diferencia) convierte un acorde alegre en uno melancólico?",
            "intuition": "La diferencia física entre un acorde mayor y uno menor es apenas 1 traste en una sola nota (la tercera). Entrenar el oído desde el principio te permitirá sacar canciones sin depender siempre de tablaturas.",
        },
        "concept": {
            "points": [
                "Un acorde básico (tríada) se forma por 3 notas: Raíz (1ª), Tercera (3ª) y Quinta (5ª).",
                "Tercera Mayor (4 semitonos desde la raíz) → sonido brillante/alegre (ej. E, A, D, G, C).",
                "Tercera Menor (3 semitonos desde la raíz) → sonido introspectivo/melancólico (ej. Em, Am, Dm).",
                "Intervalos clave de referencia: 5ª Justa (7 trastes — inicio de Star Wars), Octava (12 trastes — misma nota al doble de frecuencia).",
            ],
            "key_rule": "Mayor vs. Menor = solo 1 semitono de diferencia en la tercera del acorde.",
            "pitfall": "Intentar adivinar de oído en silencio sin cantar: tararear la nota activa el circuito auditivo-motor y duplica el aprendizaje.",
        },
        "example": {
            "title": "Compará E vs Em y entrená tu oído",
            "steps": [
                "Tocá E mayor en tu guitarra, levantá únicamente el dedo 1 (3ª cuerda) para tocar Em y escuchá el cambio emocional.",
                "Abrí el Laboratorio de Guitarra → Oído y resolvé 8 pruebas de Mayor vs Menor cantando la nota media.",
                "Pasá a Intervalos (3ª, 5ª, 8ª) y asociá cada uno a una melodía que conozcas.",
            ],
            "lab_link": "guitar:ear",
            "lab_cta": "Entrenar oído",
        },
        "check": {
            "question": "Si tocás E mayor y levantás el dedo 1 de la 3ª cuerda traste 1 (bajando esa nota 1 semitono), ¿qué acorde suena?",
            "options": [
                {"text": "Mi menor (Em)", "ok": True, "feedback": "Correcto: bajaste la tercera mayor a tercera menor."},
                {"text": "La menor (Am)", "ok": False, "feedback": "La raíz sigue siendo Mi (E)."},
                {"text": "Sol mayor (G)", "ok": False, "feedback": "Solo cambió 1 semitono en la tercera, convirtiendo E en Em."},
            ],
        },
        "checks": [
            {
                "question": "Tocás una nota y después otra 4 trastes más arriba en la misma cuerda. ¿Qué intervalo formaste?",
                "options": [
                    {"text": "Una tercera menor", "ok": False, "feedback": "La tercera menor mide 3 semitonos (3 trastes), uno menos."},
                    {"text": "Una tercera mayor", "ok": True, "feedback": "Exacto: 4 semitonos desde la raíz es la tercera mayor, la del sonido brillante."},
                    {"text": "Una quinta justa", "ok": False, "feedback": "La quinta justa está a 7 trastes de la raíz."},
                ],
            },
            {
                "question": "Comparás una cuerda al aire con esa misma cuerda pisada en el traste 12. ¿Qué intervalo escuchás?",
                "options": [
                    {"text": "Una octava", "ok": True, "feedback": "Exacto: 12 trastes arriba suena la misma nota al doble de frecuencia."},
                    {"text": "Una quinta justa", "ok": False, "feedback": "La quinta justa está en el traste 7, no en el 12."},
                    {"text": "Una tercera mayor", "ok": False, "feedback": "La tercera mayor está apenas a 4 trastes."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en una línea qué cambia físicamente entre un acorde mayor y su homónimo menor.",
    },
    "g-pua-pentatonica": {
        "hook": {
            "question": "¿Por qué la escala pentatónica menor de 5 notas es la llave para improvisar tus primeros solos sin sonar mal?",
            "intuition": "Al quitar las dos notas más tensas de la escala menor, las 5 notas restantes encajan casi mágicamente sobre progresiones de rock, blues y pop.",
        },
        "concept": {
            "points": [
                "Púa alternada estricta (↓ ↑ ↓ ↑): economiza el recorrido a la mitad y sincroniza la mano derecha con el pulso.",
                "Regla de 'un dedo por traste': en la Caja 1 de La menor (traste 5), índice=traste 5, medio=6, anular=7, meñique=8.",
                "Mapa Caja 1 de Am pentatónica (de 6ª a 1ª cuerda): 5–8, 5–7, 5–7, 5–7, 5–8, 5–8.",
                "Las notas raíz (La / A) están en 6ª traste 5, 4ª traste 7 y 1ª traste 5: empezar o terminar frases ahí suena resuelto.",
            ],
            "key_rule": "Púa alternada ↓ ↑ estricta + un dedo por traste + resolver en la nota raíz.",
            "pitfall": "Tocar siempre con púa hacia abajo (↓ ↓ ↓) crea un techo de velocidad y tensión al pasar a corcheas.",
        },
        "example": {
            "title": "Explorá la Caja 1 escuchando cada nota",
            "steps": [
                "Abrí el Laboratorio de Guitarra → Diapasón con el patrón 'Pentatónica Am (Caja 1)' activo.",
                "Hacé click en las tónicas (resaltadas en verde petróleo) para memorizar dónde viven las notas La (A).",
                "Practicá subir y bajar la caja en tu guitarra a 60 BPM con púa alternada ↓ ↑ estricta.",
            ],
            "lab_link": "guitar:fretboard",
            "lab_cta": "Explorar Caja 1 en el diapasón",
        },
        "check": {
            "question": "¿Qué combinación de trastes corresponde a la 6ª cuerda (grave) en la Caja 1 de la pentatónica de La menor?",
            "options": [
                {"text": "Traste 5 (índice) y traste 8 (meñique)", "ok": True, "feedback": "Exacto: traste 5 es La (tónica) y traste 8 es Do (tercera menor)."},
                {"text": "Traste 5 y traste 7", "ok": False, "feedback": "5–7 se usa en la 5ª, 4ª y 3ª cuerda; en 6ª, 2ª y 1ª es 5–8."},
                {"text": "Traste 1 y traste 3", "ok": False, "feedback": "La Caja 1 de La menor se ancla en el traste 5."},
            ],
        },
        "checks": [
            {
                "question": "En la Caja 1 de Am, con la regla de 'un dedo por traste', ¿qué dedo pisa el traste 7?",
                "options": [
                    {"text": "El medio", "ok": False, "feedback": "Al medio le toca el traste 6, que en esta caja no se usa."},
                    {"text": "El meñique", "ok": False, "feedback": "El meñique se ocupa del traste 8."},
                    {"text": "El anular", "ok": True, "feedback": "Exacto: índice=5, medio=6, anular=7, meñique=8."},
                ],
            },
            {
                "question": "Querés que tu frase suene 'resuelta'. ¿En cuál de estas notas de la Caja 1 conviene terminar?",
                "options": [
                    {"text": "4ª cuerda, traste 5", "ok": False, "feedback": "Esa nota es Sol; pertenece a la escala pero no es la raíz."},
                    {"text": "4ª cuerda, traste 7", "ok": True, "feedback": "Exacto: ahí hay un La (A), una de las tres raíces de la caja."},
                    {"text": "2ª cuerda, traste 8", "ok": False, "feedback": "Esa nota es Sol; las raíces están en 6ª traste 5, 4ª traste 7 y 1ª traste 5."},
                ],
            },
        ],
        "takeaway_prompt": "Anotá las 3 posiciones de la nota raíz (A) dentro de la Caja 1 de Am.",
    },

    # ==================== ELECTRÓNICA (8) ====================
    "e-ley-de-ohm": {
        "hook": {
            "question": "¿Por qué un LED de $0.10 se quema en menos de un segundo si lo conectás directo a 5V, pero dura 50.000 horas con una pequeña resistencia?",
            "intuition": "Imaginá una manguera con agua: el Voltaje (V) es la presión, la Corriente (I) es el caudal y la Resistencia (R) es una llave que estrecha el paso. Sin resistencia, la presión manda demasiado caudal y destruye el LED.",
        },
        "concept": {
            "points": [
                "Ley de Ohm: V = I · R (Voltios = Amperios × Ohmios). De ahí despejás I = V / R y R = V / I.",
                "Un LED necesita su voltaje directo Vf (≈2.0V rojo, ≈3.0V azul) y una corriente segura (10–15 mA = 0.010–0.015 A).",
                "La resistencia absorbe el voltaje sobrante: R = (V_fuente − V_led) / I_deseada.",
                "Siempre elegís el valor comercial estándar (serie E12: 220 Ω, 330 Ω, 470 Ω, 1 kΩ...) igual o inmediatamente superior.",
            ],
            "key_rule": "V = I · R  |  Para un LED: R = (V_fuente − V_led) / I",
            "pitfall": "Olvidar convertir miliamperios (mA) a amperios (A): 15 mA es 0.015 A (dividir por 1000).",
        },
        "example": {
            "title": "Cálculo real: LED rojo en Arduino (5V) vs ESP32 (3.3V)",
            "steps": [
                "En Arduino (5V) con LED rojo (2V) a 15 mA (0.015 A): R = (5 − 2) / 0.015 = 200 Ω → usamos 220 Ω.",
                "En ESP32 (3.3V) con el mismo LED: R = (3.3 − 2) / 0.015 = 86.7 Ω → usamos 100 Ω.",
                "Verificá las bandas de color de 220 Ω (Rojo-Rojo-Marrón) en el Laboratorio de Electrónica.",
            ],
            "lab_link": "electronics:ohm",
            "lab_cta": "Simular LED y bandas",
        },
        "check": {
            "question": "Si conectás un LED rojo (Vf = 2V) a una fuente de 5V buscando 10 mA (0.01 A), ¿qué resistencia necesitás?",
            "options": [
                {"text": "300 Ω (comercial: 330 Ω)", "ok": True, "feedback": "Correcto: (5 − 2) / 0.01 = 3 / 0.01 = 300 Ω → comercial inmediata superior 330 Ω."},
                {"text": "500 Ω", "ok": False, "feedback": "Faltó restar la caída del LED (2V) antes de dividir."},
                {"text": "30 Ω", "ok": False, "feedback": "Recordá convertir 10 mA a 0.01 A (no 0.1 A)."},
            ],
        },
        "checks": [
            {
                "question": "Conectás una resistencia de 1 kΩ directamente a 5 V. ¿Qué corriente circula?",
                "options": [
                    {"text": "5 A", "ok": False, "feedback": "Faltó convertir 1 kΩ a 1000 Ω antes de dividir."},
                    {"text": "200 mA", "ok": False, "feedback": "Dividiste R por V; la ley es I = V / R = 5 / 1000."},
                    {"text": "5 mA", "ok": True, "feedback": "Exacto: I = V / R = 5 / 1000 = 0.005 A = 5 mA."},
                ],
            },
            {
                "question": "El cálculo de la resistencia para tu LED da 86.7 Ω. ¿Qué valor comercial elegís?",
                "options": [
                    {"text": "82 Ω, porque es el más cercano", "ok": False, "feedback": "Un valor menor al calculado deja pasar más corriente que la que querías."},
                    {"text": "100 Ω, el inmediato superior", "ok": True, "feedback": "Exacto: redondeás hacia arriba para que la corriente quede apenas por debajo de la deseada."},
                    {"text": "1 kΩ, para ir bien seguro", "ok": False, "feedback": "Con unas diez veces más resistencia la corriente cae a cerca de la décima parte y el LED casi no brilla."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá en tus palabras qué representa V, I y R y por qué siempre ponemos una resistencia en serie con un LED.",
    },
    "e-protoboard-seguridad": {
        "hook": {
            "question": "¿Cuál es el error #1 que quema placas ESP32 en los primeros días de laboratorio?",
            "intuition": "Asumir que todos los pines soportan 5V como Arduino Uno. El ESP32 funciona con lógica de 3.3V: meterle 5V en un pin GPIO puede arruinar el chip internamente.",
        },
        "concept": {
            "points": [
                "Protoboard: los rieles laterales (+ rojo / − azul) corren conectados a lo largo; las filas centrales conectan grupos de 5 huecos en horizontal.",
                "La zanja central separa ambos lados para montar el ESP32 o circuitos integrados sin cortocircuitar sus patas.",
                "Polaridad del LED: pata larga = Ánodo (+), pata corta / borde plano = Cátodo (− a GND).",
                "Lógica 3.3V (ESP32) vs 5V (Arduino Uno): si un sensor entrega 5V hacia un ESP32, bajalo con un divisor resistivo (1kΩ / 2kΩ).",
            ],
            "key_rule": "Desconectá el USB antes de cablear · Compartí GND en común · Nunca metas 5V a un GPIO del ESP32.",
            "pitfall": "Conectar dos cables en la misma fila horizontal pensando que están separados, o cruzar VCC directo a GND.",
        },
        "example": {
            "title": "Inspeccioná el pinout y probá un divisor 5V → 3.3V",
            "steps": [
                "Abrí el Laboratorio de Electrónica → Pines y compará los voltajes de ESP32 DevKit vs Arduino Uno.",
                "Hacé click en GPIO 34 (solo entrada) y en VIN (5V) para ver las alertas reales.",
                "En Ohm & Divisor probá R1=1kΩ y R2=2kΩ sobre 5V para confirmar V_out = 3.33V.",
            ],
            "lab_link": "electronics:pinout",
            "lab_cta": "Explorar los pines del ESP32",
        },
        "check": {
            "question": "Querés conectar la salida de datos de un sensor que envía 5V a una entrada digital de tu ESP32. ¿Qué debés hacer?",
            "options": [
                {"text": "Conectarlo directo a GPIO 4", "ok": False, "feedback": "Los GPIO del ESP32 NO son tolerantes a 5V y pueden dañarse."},
                {"text": "Usar un divisor resistivo (ej. 1kΩ y 2kΩ) o un level shifter para bajarlo a ~3.3V", "ok": True, "feedback": "Exacto: así protegés la entrada del ESP32 manteniendo una señal HIGH limpia."},
                {"text": "Conectar la salida del sensor a GND", "ok": False, "feedback": "Eso provocaría un cortocircuito en la salida del sensor."},
            ],
        },
        "checks": [
            {
                "question": "Enchufás las dos patas de una resistencia en la misma fila central de 5 huecos. ¿Qué pasa?",
                "options": [
                    {"text": "Funciona normal: cada hueco es independiente", "ok": False, "feedback": "Los 5 huecos de una fila están unidos por dentro."},
                    {"text": "Queda conectada sola al riel positivo", "ok": False, "feedback": "Las filas centrales no se conectan con los rieles salvo que pongas un cable."},
                    {"text": "Las dos patas quedan unidas entre sí y la resistencia queda anulada", "ok": True, "feedback": "Exacto: la fila puentea la resistencia; cada pata tiene que ir en una fila distinta."},
                ],
            },
            {
                "question": "Tenés un LED nuevo. ¿Qué pata va hacia GND?",
                "options": [
                    {"text": "La pata corta, del lado del borde plano (cátodo)", "ok": True, "feedback": "Exacto: el cátodo (−) va hacia GND y la pata larga (ánodo) hacia el positivo."},
                    {"text": "La pata larga (ánodo)", "ok": False, "feedback": "La pata larga es el ánodo (+) y va hacia el lado positivo."},
                    {"text": "Cualquiera: el LED no tiene polaridad", "ok": False, "feedback": "El LED es un diodo: conduce en un solo sentido y al revés no enciende."},
                ],
            },
        ],
        "takeaway_prompt": "Resumí las 3 reglas de seguridad antes de enchufar el cable USB a tu protoboard.",
    },
    "e-blink-wokwi": {
        "hook": {
            "question": "¿Por qué conviene probar tu primer circuito en un simulador virtual antes de tocar cables reales?",
            "intuition": "En el Arduino virtual del laboratorio los cables nunca están flojos y no podés quemar componentes, pero el circuito se comporta como el real: ves la corriente del LED, el osciloscopio y el monitor serie. Así separás el aprendizaje del código de los problemas físicos de la protoboard.",
        },
        "concept": {
            "points": [
                "Todo programa Arduino/ESP32 tiene dos funciones obligatorias: setup() y loop().",
                "setup() corre UNA sola vez al encender o reiniciar la placa: ahí configurás pinMode(PIN, OUTPUT) y Serial.begin(115200).",
                "loop() se repite infinitamente miles de veces por segundo: ahí lee entradas, toma decisiones y enciende/apaga salidas.",
                "digitalWrite(PIN, HIGH) pone 3.3V (ESP32) o 5V (Uno) en el pin; LOW lo pone a 0V (GND).",
            ],
            "key_rule": "setup() configura una vez · loop() ejecuta para siempre · Serial.println() son tus rayos X.",
            "pitfall": "Olvidar pinMode(LED_PIN, OUTPUT): el pin queda en entrada (alta impedancia) y el LED apenas brilla.",
        },
        "example": {
            "title": "Tu primer Blink en el Arduino virtual en 3 minutos",
            "steps": [
                "Abrí el Arduino virtual con el botón de abajo: ya tiene cargado el Blink de la Iteración 01 (LED en D13).",
                "Apretá 'Cargar y ejecutar': mirá el LED, la tensión de D13 en el osciloscopio y los mensajes del monitor serie.",
                "Borrá la línea de pinMode y volvé a ejecutar: el LED apenas brilla. Después cambiá el ritmo a Morse SOS.",
            ],
            "lab_link": "electronics:arduino:serial-blink",
            "lab_cta": "Abrir el Arduino virtual con el Blink",
        },
        "check": {
            "question": "¿Dónde debés colocar Serial.begin(115200) y pinMode(LED_PIN, OUTPUT)?",
            "options": [
                {"text": "Dentro de setup(), porque solo se ejecutan una vez al arrancar", "ok": True, "feedback": "Correcto: setup() inicializa pines y periféricos al inicio."},
                {"text": "Dentro de loop(), para repetirlo constantemente", "ok": False, "feedback": "Reinicializar el puerto Serial en cada vuelta de loop() es innecesario y genera errores."},
                {"text": "Fuera de cualquier función", "ok": False, "feedback": "Las llamadas ejecutables en C++ deben vivir dentro de una función."},
            ],
        },
        "checks": [
            {
                "question": "Con Serial.begin(115200) en setup(), ponés Serial.println(\"Hola\") dentro de loop(). ¿Qué ves en el Monitor Serial?",
                "options": [
                    {"text": "'Hola' una sola vez", "ok": False, "feedback": "Una sola vez saldría si estuviera en setup(); loop() se repite sin parar."},
                    {"text": "'Hola' repetido sin parar", "ok": True, "feedback": "Exacto: loop() vuelve a empezar apenas termina, miles de veces por segundo."},
                    {"text": "Nada: println solo funciona dentro de setup()", "ok": False, "feedback": "Serial.println() funciona en cualquier función una vez hecho Serial.begin()."},
                ],
            },
            {
                "question": "Tu sketch hace digitalWrite(LED_PIN, HIGH) pero el LED apenas brilla. ¿Qué es lo primero que revisás?",
                "options": [
                    {"text": "Que haya un Serial.begin(115200) en setup()", "ok": False, "feedback": "El puerto Serial sirve para depurar; no influye en el brillo del LED."},
                    {"text": "Que digitalWrite esté en setup() y no en loop()", "ok": False, "feedback": "digitalWrite funciona en cualquiera de las dos; el problema es el modo del pin."},
                    {"text": "Que exista pinMode(LED_PIN, OUTPUT) en setup()", "ok": True, "feedback": "Exacto: sin eso el pin queda como entrada (alta impedancia) y casi no entrega corriente."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá la diferencia entre setup() y loop() con una analogía cotidiana.",
    },
    "e-entradas-pullup": {
        "hook": {
            "question": "¿Por qué un pulsador mal cableado hace que tu Arduino o ESP32 'imagine' clics fantasma aunque nadie lo toque?",
            "intuition": "Un pin configurado como entrada abierta no está en 0V: queda 'flotando' en el aire como una antena de radio, captando ruido eléctrico de tus manos y del ambiente.",
        },
        "concept": {
            "points": [
                "Nunca dejes una entrada digital desconectada (flotante): siempre necesita una referencia eléctrica clara.",
                "La forma más limpia y sin resistencias externas es pinMode(BTN_PIN, INPUT_PULLUP) con el pulsador entre el pin y GND.",
                "La resistencia pull-up interna tira suavemente el pin hacia 3.3V/5V (HIGH) cuando nadie presiona.",
                "Atención a la lógica invertida: con INPUT_PULLUP, suelto = HIGH (1) y presionado = LOW (0).",
            ],
            "key_rule": "Botón a GND + pinMode(PIN, INPUT_PULLUP) → presionado significa digitalRead(PIN) == LOW.",
            "pitfall": "Escribir if (digitalRead(BTN) == HIGH) con INPUT_PULLUP hará que la acción se dispare cuando NO tocás el botón.",
        },
        "example": {
            "title": "Practicá reconstruyendo el código INPUT_PULLUP",
            "steps": [
                "Abrí el Laboratorio de Electrónica → Encontrar el error.",
                "Seleccioná 'Reto 02 · INPUT_PULLUP' en el Parson's Problem y ordená las líneas.",
                "Resolvé el Diagnóstico 01 ('Botón fantasma') para fijar el concepto.",
            ],
            "lab_link": "electronics:debug",
            "lab_cta": "Resolver reto INPUT_PULLUP",
        },
        "check": {
            "question": "Conectás un pulsador entre GPIO 4 y GND usando pinMode(4, INPUT_PULLUP). ¿Qué devuelve digitalRead(4) mientras lo mantenés presionado?",
            "options": [
                {"text": "LOW (0)", "ok": True, "feedback": "Exacto: presionar el botón conecta el pin directamente a tierra (0V = LOW)."},
                {"text": "HIGH (1)", "ok": False, "feedback": "HIGH es el estado de reposo (suelto) gracias a la resistencia pull-up interna."},
                {"text": "Un número aleatorio entre 0 y 4095", "ok": False, "feedback": "digitalRead solo devuelve 0 (LOW) o 1 (HIGH), y con pull-up es estable."},
            ],
        },
        "checks": [
            {
                "question": "Hacés pinMode(4, INPUT) y dejás el GPIO 4 sin conectar a nada. ¿Qué devuelve digitalRead(4)?",
                "options": [
                    {"text": "Siempre LOW, porque no le llega voltaje", "ok": False, "feedback": "Un pin sin conectar no está en 0 V: queda flotando sin referencia."},
                    {"text": "Valores que saltan al azar entre HIGH y LOW", "ok": True, "feedback": "Exacto: el pin flotante funciona como antena y capta ruido eléctrico."},
                    {"text": "Siempre HIGH, porque el pin está libre", "ok": False, "feedback": "Solo quedaría estable en HIGH si activaras la resistencia pull-up."},
                ],
            },
            {
                "question": "Para usar INPUT_PULLUP, ¿cómo cableás el pulsador?",
                "options": [
                    {"text": "Entre el pin y GND, sin resistencia externa", "ok": True, "feedback": "Exacto: la pull-up interna mantiene HIGH en reposo y el botón lleva el pin a LOW."},
                    {"text": "Entre el pin y 3.3 V", "ok": False, "feedback": "Así el pin leería HIGH tanto suelto como presionado y nunca verías el cambio."},
                    {"text": "Entre 3.3 V y GND", "ok": False, "feedback": "Eso pone la alimentación en cortocircuito al presionar, y el pin ni se entera."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá qué es un 'pin flotante' y cómo INPUT_PULLUP lo soluciona sin agregar componentes.",
    },
    "e-analog-pwm": {
        "hook": {
            "question": "¿Cómo logra un microcontrolador digital (que solo sabe decir 0 o 1) atenuar suavemente el brillo de un LED?",
            "intuition": "Con un truco visual llamado PWM: enciende y apaga el LED cientos de veces por segundo. Si está encendido el 25% del tiempo, tu ojo promedia la luz y lo ve al 25% de brillo.",
        },
        "concept": {
            "points": [
                "ADC (Conversor Analógico-Digital): traduce un voltaje continuo (ej. un potenciómetro) a un número entero.",
                "Resolución: Arduino Uno usa 10 bits (0 a 1023); ESP32 usa 12 bits (0 a 4095 — 4 veces más preciso).",
                "PWM (Modulación por Ancho de Pulso): analogWrite(PIN, 0..255) ajusta el ciclo de trabajo (duty cycle) para controlar brillo de LEDs o velocidad de motores.",
                "Trampa vital de ESP32: usá pines de ADC1 (GPIO 32–39) para analogRead(), porque ADC2 se desactiva cuando prendés el Wi-Fi.",
            ],
            "key_rule": "ADC lee el mundo continuo (0..4095 en ESP32) · map() escala rangos · PWM controla potencia promedio.",
            "pitfall": "Conectar un potenciómetro a GPIO 4 (ADC2) en ESP32 funciona hoy, pero se rompe mágicamente en cuanto agregás Wi-Fi.",
        },
        "example": {
            "title": "Dimmer con potenciómetro",
            "steps": [
                "Leé el potenciómetro: int crudo = analogRead(34); (entrega 0..4095 en ESP32).",
                "Convertilo al rango PWM (0..255): int brillo = map(crudo, 0, 4095, 0, 255);",
                "Aplicá la salida: analogWrite(LED_PIN, brillo); y mirá la Iteración 02 en el Laboratorio de Electrónica.",
            ],
            "lab_link": "electronics:pinout",
            "lab_cta": "Ver los pines ADC1 seguros",
        },
        "check": {
            "question": "En un ESP32 con Wi-Fi encendido, ¿cuál de estos pines es SEGURO para leer un sensor analógico con analogRead()?",
            "options": [
                {"text": "GPIO 34 (pertenece a ADC1)", "ok": True, "feedback": "Correcto: los pines ADC1 (GPIO 32–39) nunca entran en conflicto con el radio Wi-Fi."},
                {"text": "GPIO 4 (pertenece a ADC2)", "ok": False, "feedback": "ADC2 comparte hardware interno con Wi-Fi y falla al leer."},
                {"text": "VIN (5V)", "ok": False, "feedback": "VIN es alimentación, no una entrada ADC."},
            ],
        },
        "checks": [
            {
                "question": "En un ESP32, el potenciómetro está justo a la mitad de su recorrido. ¿Qué valor aproximado devuelve analogRead()?",
                "options": [
                    {"text": "Cerca de 512", "ok": False, "feedback": "Ese sería el punto medio en un Arduino Uno (10 bits, 0 a 1023)."},
                    {"text": "Cerca de 2048", "ok": True, "feedback": "Exacto: el ADC de 12 bits va de 0 a 4095 y la mitad queda alrededor de 2048."},
                    {"text": "Cerca de 128", "ok": False, "feedback": "128 es la mitad del rango de PWM (0 a 255), no del ADC."},
                ],
            },
            {
                "question": "Escribís analogWrite(LED_PIN, 64). ¿Con qué brillo aproximado ves el LED?",
                "options": [
                    {"text": "Cerca del 64%", "ok": False, "feedback": "El valor no es un porcentaje: la escala va de 0 a 255."},
                    {"text": "Cerca del 6%", "ok": False, "feedback": "Eso saldría con una escala de 0 a 1023, pero analogWrite usa 0 a 255."},
                    {"text": "Cerca del 25%", "ok": True, "feedback": "Exacto: 64 / 255 ≈ 0.25, el pin pasa en HIGH un cuarto del tiempo."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá la diferencia entre una entrada ADC y una salida PWM.",
    },
    "e-millis-multitarea": {
        "hook": {
            "question": "¿Por qué cuando agregás un segundo LED o un botón a un código con delay(1000) todo deja de responder?",
            "intuition": "delay(1000) es como quedarte mirando el reloj con los ojos cerrados durante un segundo entero: si alguien toca el timbre en ese lapso, ni te enterás. millis() te permite mirar la hora de reojo mientras seguís atento a todo.",
        },
        "concept": {
            "points": [
                "millis() devuelve los milisegundos transcurridos desde que encendió la placa (tipo unsigned long).",
                "Patrón no bloqueante: guardás ultimoTiempo y en cada vuelta de loop() preguntás si (millis() - ultimoTiempo >= intervalo).",
                "Cuando se cumple el tiempo, actualizás ultimoTiempo = ahora y ejecutás la acción (ej. invertir el LED).",
                "El resto de loop() corre libremente miles de veces por segundo leyendo botones, sensores y Wi-Fi sin congelarse.",
            ],
            "key_rule": "if (millis() - ultimo >= intervalo) { ultimo = millis(); /* acción */ }",
            "pitfall": "Usar int en vez de unsigned long (se desborda a los 32 segundos) u olvidar actualizar ultimo = ahora.",
        },
        "example": {
            "title": "Reconstruí el patrón millis() paso a paso",
            "steps": [
                "Abrí el Laboratorio de Electrónica → Encontrar el error.",
                "Completá el 'Reto 01 · millis()' ordenando las 6 líneas del Parson's Problem.",
                "Observá cómo podés repetir ese mismo patrón con 2 variables independientes para controlar dos tareas a ritmos distintos.",
            ],
            "lab_link": "electronics:debug",
            "lab_cta": "Resolver Parson's Problem de millis()",
        },
        "check": {
            "question": "¿Por qué se escribe siempre (millis() - ultimo >= 500) con RESTA y tipo unsigned long?",
            "options": [
                {"text": "Porque no congela el loop() y maneja correctamente incluso el reinicio del contador a los ~49 días", "ok": True, "feedback": "Exacto: la aritmética modular sin signo con resta evita bugs de desbordamiento."},
                {"text": "Porque millis() solo funciona con 500 ms", "ok": False, "feedback": "Funciona con cualquier intervalo en milisegundos."},
                {"text": "Porque reemplaza a pinMode()", "ok": False, "feedback": "millis() solo mide tiempo transcurrido."},
            ],
        },
        "checks": [
            {
                "question": "En el patrón con millis() te olvidás la línea ultimo = ahora;. ¿Qué pasa una vez cumplido el primer intervalo?",
                "options": [
                    {"text": "El LED no cambia nunca más", "ok": False, "feedback": "Al contrario: la condición se sigue cumpliendo y la acción se repite sin parar."},
                    {"text": "La condición queda siempre verdadera y la acción se ejecuta en cada vuelta de loop()", "ok": True, "feedback": "Exacto: como ultimo nunca avanza, la resta millis() - ultimo siempre supera el intervalo."},
                    {"text": "La placa se reinicia sola", "ok": False, "feedback": "No hay ningún reinicio; solo se perdió la temporización."},
                ],
            },
            {
                "question": "Querés un LED que parpadee cada 300 ms y otro cada 1000 ms, sin bloquear. ¿Qué necesitás?",
                "options": [
                    {"text": "Un delay(300) seguido de un delay(1000)", "ok": False, "feedback": "Los delay() se suman y bloquean: ninguno de los dos LEDs tendría su ritmo propio."},
                    {"text": "Dos funciones loop(), una por LED", "ok": False, "feedback": "Un sketch tiene un solo loop(); las tareas se reparten adentro con marcas de tiempo."},
                    {"text": "Dos variables de tiempo independientes, cada una con su intervalo", "ok": True, "feedback": "Exacto: repetís el mismo patrón con dos marcas de tiempo y cada tarea lleva su propio reloj."},
                ],
            },
        ],
        "takeaway_prompt": "Explicá con tus palabras por qué millis() supera a delay() en proyectos reales.",
    },
    "e-i2c-sensores": {
        "hook": {
            "question": "¿Cómo podés conectar una pantalla OLED, un sensor de temperatura y un acelerómetro al ESP32 usando solo DOS cables de datos?",
            "intuition": "El bus I2C funciona como una sala de chat compartida: todos escuchan los mismos dos cables (SDA y SCL), pero cada módulo tiene un nombre único en hexadecimal (su dirección, ej. 0x3C) y solo contesta cuando lo llaman.",
        },
        "concept": {
            "points": [
                "I2C usa 2 líneas compartidas: SDA (datos) y SCL (reloj), más alimentación (3.3V) y tierra común (GND).",
                "Pines por defecto: ESP32 usa GPIO 21 (SDA) y GPIO 22 (SCL); Arduino Uno usa A4 (SDA) y A5 (SCL).",
                "Cada dispositivo tiene una dirección única (ej. OLED SSD1306 suele ser 0x3C; BME280 suele ser 0x76 o 0x77).",
                "Regla de oro de debugging I2C: ante la duda, corré un 'I2C Scanner' (disponible en el Laboratorio de Electrónica → Proyectos → Iteración 03) para confirmar que la placa ve el dispositivo.",
            ],
            "key_rule": "I2C = 2 cables compartidos (SDA/SCL) + dirección hexadecimal única por módulo.",
            "pitfall": "Cruzar SDA con SCL o usar la dirección 0x3D cuando tu pantalla física es 0x3C.",
        },
        "example": {
            "title": "Estación Meteorológica v1 con I2C Scanner",
            "steps": [
                "Conectá VCC→3.3V, GND→GND, SDA→GPIO 21 y SCL→GPIO 22.",
                "Copiá el I2C Scanner de la Iteración 03 en el Laboratorio de Electrónica y confirmá la dirección impresa en Serial.",
                "Recién cuando el scanner detecte tu sensor/OLED, cargá las librerías de pantalla.",
            ],
            "lab_link": "electronics:projects",
            "lab_cta": "Ver I2C Scanner y Estación v1",
        },
        "check": {
            "question": "Conectaste una pantalla OLED I2C al ESP32 pero queda totalmente negra. ¿Cuál es el paso de diagnóstico más inteligente?",
            "options": [
                {"text": "Correr un I2C Scanner para comprobar si el ESP32 detecta el cableado y qué dirección hexadecimal responde", "ok": True, "feedback": "Exacto: en 10 segundos sabés si el fallo es de cables/alimentación o de código/dirección."},
                {"text": "Subir la alimentación de 3.3V a 9V", "ok": False, "feedback": "9V quemaría instantáneamente el OLED y el ESP32."},
                {"text": "Cambiar cada cable de I2C a un pin analógico distinto", "ok": False, "feedback": "I2C usa el par SDA/SCL (21 y 22 por defecto en ESP32)."},
            ],
        },
        "checks": [
            {
                "question": "Tu ESP32 ya tiene una OLED I2C y sumás un sensor BME280. ¿A qué pines van SDA y SCL del sensor?",
                "options": [
                    {"text": "A dos GPIO nuevos: cada módulo necesita su propio par", "ok": False, "feedback": "I2C es un bus compartido: todos los módulos cuelgan de las mismas dos líneas."},
                    {"text": "A los mismos GPIO 21 (SDA) y 22 (SCL) que usa la OLED", "ok": True, "feedback": "Exacto: comparten los cables y el ESP32 los distingue por su dirección."},
                    {"text": "SDA del sensor al SCL de la pantalla, para encadenarlos", "ok": False, "feedback": "No se cruzan: SDA va con SDA y SCL con SCL."},
                ],
            },
            {
                "question": "El I2C Scanner encuentra tu OLED en 0x3C, pero el código usa 0x3D. ¿Qué pasa?",
                "options": [
                    {"text": "Funciona igual: la dirección es solo una etiqueta", "ok": False, "feedback": "La dirección es el 'nombre' al que responde el módulo; si llamás a otro, nadie contesta."},
                    {"text": "La pantalla se quema", "ok": False, "feedback": "Una dirección equivocada no daña nada; simplemente no hay respuesta."},
                    {"text": "La pantalla queda en negro porque nadie responde en 0x3D", "ok": True, "feedback": "Exacto: corregís la dirección en el código por la que mostró el scanner."},
                ],
            },
        ],
        "takeaway_prompt": "Anotá qué pines usa I2C en ESP32 y para qué sirve correr un I2C Scanner.",
    },
    "e-esp32-wifi-iot": {
        "hook": {
            "question": "¿Qué convierte al ESP32 en una placa tan poderosa frente al Arduino Uno clásico?",
            "intuition": "Trae Wi-Fi y Bluetooth integrados en el mismo chip de pocos dólares. En 15 líneas de código tu sensor físico se convierte en un dispositivo IoT accesible desde tu celular.",
        },
        "concept": {
            "points": [
                "Modo estación (WIFI_STA): el ESP32 se conecta a tu router Wi-Fi igual que un celular y recibe una IP local.",
                "Siempre agregá un timeout al bucle de conexión (ej. 15 segundos) para que la placa no quede colgada si el router se reinicia.",
                "Servidor web local: el ESP32 responde peticiones HTTP devolviendo HTML liviano o JSON con las lecturas de tus sensores.",
                "Podés probar todo el flujo Wi-Fi gratis en Wokwi usando la red simulada 'Wokwi-GUEST' (sin contraseña).",
            ],
            "key_rule": "WiFi.mode(WIFI_STA) → WiFi.begin() con timeout → WiFi.localIP() → servir datos sin delay().",
            "pitfall": "Olvidar que el ESP32 clásico solo soporta redes Wi-Fi de 2.4 GHz (no 5 GHz).",
        },
        "example": {
            "title": "Conectar tu ESP32 a Wi-Fi en Wokwi",
            "steps": [
                "Abrí el Laboratorio de Electrónica → Proyectos → Iteración 04 y copiá el bloque de conexión Wi-Fi con timeout.",
                "Ejecutalo en Wokwi con SSID 'Wokwi-GUEST' y verificá la IP impresa en Serial Monitor.",
                "Reto abierto: integrá tus lecturas de temperatura con un aviso cuando supere tu umbral.",
            ],
            "lab_link": "electronics:projects",
            "lab_cta": "Abrir Iteración 04 (ESP32 Wi-Fi)",
        },
        "check": {
            "question": "Intentás conectar tu ESP32 físico a tu Wi-Fi doméstico pero nunca conecta, aunque la contraseña está bien. ¿Qué causa técnica frecuente debés revisar?",
            "options": [
                {"text": "Que la red sea de 5 GHz: el ESP32 estándar solo se conecta a redes de 2.4 GHz", "ok": True, "feedback": "Exacto: es una de las causas más comunes al configurar un ESP32 por primera vez."},
                {"text": "Que falta conectar una resistencia al router", "ok": False, "feedback": "La comunicación es inalámbrica."},
                {"text": "Que Wi-Fi no funciona si usás Serial.begin()", "ok": False, "feedback": "Serial y Wi-Fi conviven perfectamente; el conflicto es con ADC2."},
            ],
        },
        "checks": [
            {
                "question": "¿Para qué sirve el timeout en el bucle que espera la conexión Wi-Fi?",
                "options": [
                    {"text": "Para que la conexión se establezca más rápido", "ok": False, "feedback": "El timeout no acelera nada: solo limita cuánto tiempo se espera."},
                    {"text": "Porque el Wi-Fi se corta solo cada 15 segundos", "ok": False, "feedback": "La conexión no tiene ese límite; los 15 s son el tiempo máximo de espera que elegís vos."},
                    {"text": "Para que la placa no quede colgada para siempre si el router no responde", "ok": True, "feedback": "Exacto: pasado ese tiempo el programa sigue y puede reintentar o avisar del error."},
                ],
            },
            {
                "question": "Tu ESP32 se conectó en modo WIFI_STA. ¿Cómo sabés qué dirección abrir en el navegador del celular?",
                "options": [
                    {"text": "Imprimiendo WiFi.localIP() por Serial", "ok": True, "feedback": "Exacto: es la IP local que el router le asignó a la placa."},
                    {"text": "Siempre es 192.168.4.1", "ok": False, "feedback": "Esa es la IP típica cuando el ESP32 crea su propia red; en modo estación la asigna tu router."},
                    {"text": "Usando la dirección 0x3C", "ok": False, "feedback": "0x3C es la dirección I2C de un módulo, no una IP de red."},
                ],
            },
        ],
        "takeaway_prompt": "Resumí los 3 pasos para conectar un ESP32 a Wi-Fi de forma robusta.",
    },

}

LESSONS_BY_SLUG.update(MATH_LESSONS)
LESSONS_BY_SLUG.update(PHYSICS_LESSONS)
LESSONS_BY_SLUG.update(CLYRP_LESSONS)
