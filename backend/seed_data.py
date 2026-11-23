"""Curated evidence-based beginner curricula for Guitar, Electronics, and Math.

Designed for learners starting from zero in Spanish (preserving standard
technical terms like BPM, GPIO, PWM, I2C, FSRS).
"""

from __future__ import annotations

from typing import Any

from backend.math_content import MATH_DOMAIN, RETIRED_MATH_NODE_SLUGS
from backend.clyrp_content import CLYRP_DOMAIN
from backend.physics_content import PHYSICS_DOMAIN

SEED_DOMAINS: list[dict[str, Any]] = [
    {
        "slug": "guitarra",
        "name": "Guitarra",
        "icon": "guitar",
        "color": "#296a6c",
        "domain_type": "motor",
        "lab_type": "guitar",
        "description": (
            "Aprendizaje motor deliberado desde cero: postura, acordes abiertos, "
            "cambios limpios con metrónomo, ritmo, oído y repertorio."
        ),
        "config": {
            "tools": ["metronome", "chord_trainer", "tuner", "overlearning"],
            "method_tips": [
                "Toca tan lento como necesites para lograr 0 errores: la memoria muscular graba lo que repetís.",
                "Antes de cerrar un ejercicio difícil, hacé 3 repeticiones limpias seguidas (overlearning).",
                "Alterná bloques cortos de 3–5 min entre cambios de acordes, ritmo y oído (interleaving).",
            ],
        },
        "nodes": [
            {
                "slug": "g-postura-afinacion",
                "title": "1. Postura, partes y afinación estándar",
                "level": 1,
                "order_index": 1,
                "summary": "Sostener la guitarra sin tensión, numeración de dedos/cuerdas y afinación E-A-D-G-B-E.",
                "prerequisites": [],
                "metadata": {"section": "Fundamentos", "lab_tab": "tuner", "est_minutes": 15},
                "items": [
                    {
                        "item_type": "recall",
                        "title": "Afinación estándar de 6ª a 1ª cuerda",
                        "prompt": "¿Cuál es la nota de cada cuerda de la guitarra desde la más grave (6ª) hasta la más aguda (1ª)? Escribí las 6 notas en orden, separadas por espacios (con sus nombres o en cifrado americano).",
                        "answer": "6ª Mi (E) — 5ª La (A) — 4ª Re (D) — 3ª Sol (G) — 2ª Si (B) — 1ª Mi (E). Regla rápida: E-A-D-G-B-E.",
                        "hints": ["Empieza y termina en la misma nota (Mi / E).", "En cifrado americano: E A D G B E."],
                        "payload": {
                            "lab_link": "guitar:tuner",
                            "check": {
                                "type": "text",
                                "accept": ["e a d g b e", "mi la re sol si mi", "e2 a2 d3 g3 b3 e4"],
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Posición óptima del dedo sobre el traste",
                        "prompt": "¿En qué parte del espacio del traste debe pisar la yema del dedo para evitar trasteos con la mínima fuerza?",
                        "answer": "Justo detrás de la varilla metálica (lo más cerca posible del traste hacia el cuerpo, sin pisar encima de la varilla) y usando la punta del dedo arqueado.",
                        "hints": ["No pises en el medio ni pegado al traste anterior."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": [
                                    "En el medio del espacio entre las dos varillas",
                                    "Exactamente encima de la varilla metálica",
                                    "Justo detrás de la varilla metálica, sin pisarla",
                                    "Pegado a la varilla anterior, la más cercana a la cejuela",
                                ],
                                "correct": 2,
                            },
                        },
                    },
                    {
                        "item_type": "drill",
                        "title": "Drill: Afinación de oído guiada (6 cuerdas)",
                        "prompt": "Abrí el Afinador de Referencia en el Laboratorio de Guitarra, escuchá cada cuerda (6ª a 1ª) y cantá o compará el tono con tu guitarra.",
                        "answer": "Objetivo: identificar si tu cuerda suena más grave (baja) o más aguda (alta) que la referencia antes de ajustar la clavija.",
                        "hints": ["Ajustá siempre subiendo la tensión al final para mantener afinación estable."],
                        "payload": {"lab_link": "guitar:tuner", "overlearning_reps": 3},
                    },
                    {
                        "item_type": "recall",
                        "title": "Nota de la 5ª cuerda al aire",
                        "prompt": "En afinación estándar, ¿qué nota suena al tocar la 5ª cuerda al aire? Respondé con el nombre de la nota (o su letra en cifrado americano).",
                        "answer": "La (A). De 6ª a 1ª: E–A–D–G–B–E, así que la 5ª es la segunda de la lista.",
                        "hints": ["Es la cuerda que sigue a la más gruesa."],
                        "payload": {
                            "lab_link": "guitar:tuner",
                            "check": {"type": "text", "accept": ["la", "a", "la (a)", "a (la)", "a2", "la2"]},
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Numeración de los dedos de la mano izquierda",
                        "prompt": "En las digitaciones de guitarra, ¿qué dedo de la mano izquierda es el número 3?",
                        "answer": "El anular. La cuenta arranca en el índice: 1=índice, 2=medio, 3=anular, 4=meñique. El pulgar no se numera: va apoyado atrás del mástil.",
                        "hints": ["El pulgar no cuenta: el 1 es el índice."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": ["Índice", "Medio", "Anular", "Meñique"],
                                "correct": 2,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Orden para afinar una cuerda con el afinador",
                        "prompt": "Ordená los pasos para afinar una cuerda usando el Afinador de Referencia.",
                        "answer": "Elegís la cuerda, la tocás al aire comparándola con la referencia, decidís si está más grave o más aguda y recién ahí girás la clavija, terminando el ajuste subiendo la tensión. Al final volvés a tocarla para confirmar.",
                        "hints": ["Antes de tocar la clavija tenés que saber hacia dónde corregir."],
                        "payload": {
                            "lab_link": "guitar:tuner",
                            "check": {
                                "type": "order",
                                "lines": [
                                    "Abrí el afinador y elegí la cuerda que vas a afinar",
                                    "Tocá esa cuerda al aire y comparala con la nota de referencia",
                                    "Decidí si tu cuerda suena más grave o más aguda que la referencia",
                                    "Girá la clavija de a poco, terminando el ajuste subiendo la tensión",
                                    "Volvé a tocar la cuerda para confirmar que quedó en la nota",
                                ],
                            },
                        },
                    },
                ],
            },
            {
                "slug": "g-acordes-em-am",
                "title": "2. Primeros acordes: Em y Am",
                "level": 1,
                "order_index": 2,
                "summary": "Dos acordes cómodos y musicales para construir callos, postura limpia y el primer cambio fluido.",
                "prerequisites": ["g-postura-afinacion"],
                "metadata": {"section": "Fundamentos", "lab_tab": "chords", "chords": ["Em", "Am"], "est_minutes": 20},
                "items": [
                    {
                        "item_type": "recall",
                        "title": "Digitación de Mi menor (Em)",
                        "prompt": "¿Qué dedos y trastes forman el acorde de Mi menor (Em) y qué cuerdas se rasguean?",
                        "answer": "Dedo 2 en 5ª cuerda traste 2; Dedo 3 en 4ª cuerda traste 2. Se rasguean las 6 cuerdas al aire.",
                        "hints": ["Es uno de los acordes más simples: solo usa 2 dedos en el traste 2."],
                        "payload": {
                            "chord": "Em",
                            "lab_link": "guitar:chords",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Dedos 2 y 3 en el traste 2 de la 4ª y la 3ª cuerda; se rasguea desde la 5ª",
                                    "Dedos 2 y 3 en el traste 2 de la 5ª y la 4ª cuerda; se rasguean las 6 cuerdas",
                                    "Dedos 1 y 2 en el traste 1 de la 5ª y la 4ª cuerda; se rasguean las 6 cuerdas",
                                ],
                                "correct": 1,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Digitación de La menor (Am)",
                        "prompt": "¿Cómo se arma La menor (Am) y cuál cuerda NO se debe rasguear?",
                        "answer": "Dedo 1 en 2ª cuerda traste 1; Dedo 2 en 4ª cuerda traste 2; Dedo 3 en 3ª cuerda traste 2. No se rasguea la 6ª cuerda (empezá desde la 5ª).",
                        "hints": ["La nota raíz es La (5ª cuerda al aire)."],
                        "payload": {
                            "chord": "Am",
                            "lab_link": "guitar:chords",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Dedo 1 en 2ª cuerda traste 1, dedo 2 en 4ª traste 2 y dedo 3 en 3ª traste 2; no se rasguea la 6ª",
                                    "Dedo 2 en 5ª cuerda traste 2 y dedo 3 en 4ª traste 2; se rasguean las 6 cuerdas",
                                    "Dedo 1 en 2ª cuerda traste 1, dedo 2 en 4ª traste 2 y dedo 3 en 3ª traste 2; no se rasguea la 1ª",
                                ],
                                "correct": 0,
                            },
                        },
                    },
                    {
                        "item_type": "drill",
                        "title": "Micro-Drill: Cambios Em ↔ Am (1 minuto)",
                        "prompt": "En el Laboratorio de Guitarra → Cambios de acordes, hacé 1 minuto de cambios Em ↔ Am. Comprobá antes que cada cuerda suene limpia una por una (arpegio lento).",
                        "answer": "Meta inicial: 20 cambios limpios/min. Meta sólida: 35–40 cambios/min. Terminá con 3 cambios lentos perfectos (overlearning).",
                        "hints": ["Mové los dedos 2 y 3 juntos como un bloque al bajar una cuerda."],
                        "payload": {
                            "lab_link": "guitar:chords",
                            "pair": ["Em", "Am"],
                            "overlearning_reps": 3,
                            "lab_metric": {"type": "chord_changes_min", "good": 20, "easy": 35, "unit": "cambios/min"},
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "El movimiento mínimo de Em a Am",
                        "prompt": "Partiendo de Em, ¿qué movimiento arma La menor (Am)?",
                        "answer": "Los dedos 2 y 3 bajan juntos, como un bloque, una cuerda cada uno (de 5ª/4ª a 4ª/3ª) sin cambiar de traste, y se suma el dedo 1 en la 2ª cuerda, traste 1.",
                        "hints": ["Em y Am comparten la forma de los dedos 2 y 3."],
                        "payload": {
                            "lab_link": "guitar:chords",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Subir los dedos 2 y 3 al traste 3 y sumar el dedo 1 en la 1ª cuerda",
                                    "Bajar los dedos 2 y 3 una cuerda cada uno (mismo traste 2) y sumar el dedo 1 en 2ª cuerda traste 1",
                                    "Dejar quietos los dedos 2 y 3 y sumar el dedo 1 en 2ª cuerda traste 1",
                                ],
                                "correct": 1,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Cantidad de cuerdas que se rasguean en Am",
                        "prompt": "¿Cuántas cuerdas se rasguean en La menor (Am)? Respondé solo con el número de cuerdas.",
                        "answer": "5 cuerdas: de la 5ª (La al aire, la raíz) a la 1ª. La 6ª no se toca.",
                        "hints": ["Em usa las 6; en Am se evita la más grave."],
                        "payload": {"check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": "cuerdas"}},
                    },
                    {
                        "item_type": "recall",
                        "title": "Rutina para entrenar Em ↔ Am sin grabar errores",
                        "prompt": "Ordená los pasos de una sesión de práctica del cambio Em ↔ Am.",
                        "answer": "Primero verificás que Em suene limpio cuerda por cuerda, después hacés el cambio en bloque, medís 1 minuto de cambios limpios y cerrás con 3 cambios lentos perfectos (overlearning).",
                        "hints": ["La limpieza se verifica antes de medir velocidad."],
                        "payload": {
                            "lab_link": "guitar:chords",
                            "check": {
                                "type": "order",
                                "lines": [
                                    "Armá Em y tocá cuerda por cuerda para verificar que suene limpio",
                                    "Bajá el bloque de dedos 2–3 una cuerda y caé junto con el dedo 1 en Am",
                                    "Hacé 1 minuto medido contando solo los cambios limpios",
                                    "Cerrá con 3 cambios lentos perfectos (overlearning)",
                                ],
                            },
                        },
                    },
                ],
            },
            {
                "slug": "g-acordes-d-a-e",
                "title": "3. Tríada fundamental: D, A y E",
                "level": 2,
                "order_index": 3,
                "summary": "Los tres acordes mayores más usados al inicio y el concepto de 'dedo ancla' para cambiar más rápido.",
                "prerequisites": ["g-acordes-em-am"],
                "metadata": {"section": "Acordes y ritmo", "lab_tab": "chords", "chords": ["D", "A", "E"], "est_minutes": 20},
                "items": [
                    {
                        "item_type": "recall",
                        "title": "El truco del 'dedo ancla' entre D, A y E",
                        "prompt": "¿Qué dedo puede quedar apoyado en la 3ª cuerda como 'dedo ancla' al cambiar entre D, A y E (digitación moderna)?",
                        "answer": "El dedo índice (1) permanece en la 3ª cuerda: traste 2 en D y A (en la digitación 2-1-3 de A), y desliza al traste 1 en E.",
                        "hints": ["Mantener un punto de referencia reduce drásticamente el error motor."],
                        "payload": {
                            "lab_link": "guitar:chords",
                            "check": {
                                "type": "choice",
                                "options": ["Índice (1)", "Medio (2)", "Anular (3)", "Meñique (4)"],
                                "correct": 0,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Cuerdas activas en Re mayor (D)",
                        "prompt": "¿Desde qué cuerda se rasguea el acorde de Re mayor (D) y por qué?",
                        "answer": "Desde la 4ª cuerda (Re al aire) hacia abajo. La 6ª y 5ª se evitan para no ensuciar el bajo del acorde.",
                        "hints": ["El nombre del acorde te dice cuál es su cuerda grave al aire."],
                        "payload": {
                            "chord": "D",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Desde la 6ª cuerda",
                                    "Desde la 5ª cuerda",
                                    "Desde la 4ª cuerda",
                                    "Desde la 3ª cuerda",
                                ],
                                "correct": 2,
                            },
                        },
                    },
                    {
                        "item_type": "drill",
                        "title": "Micro-Drill intercalado: D ↔ A y A ↔ E",
                        "prompt": "Alterná 2 minutos de D ↔ A y 2 minutos de A ↔ E a 50 BPM (un rasgueo cada 4 pulsos, luego cada 2). Registrá tus cambios limpios en el Laboratorio de Guitarra.",
                        "answer": "Subí a 60 BPM solo cuando puedas completar 4 compases seguidos sin trasteo ni pausas.",
                        "hints": ["Si dudás antes de caer en el tiempo 1, bajá 10 BPM."],
                        "payload": {
                            "lab_link": "guitar:metronome",
                            "target_bpm": 60,
                            "overlearning_reps": 3,
                            "lab_metric": {"type": "bpm_clean", "good": 50, "easy": 60, "unit": "BPM"},
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Digitación de Re mayor (D)",
                        "prompt": "¿Qué dedos y trastes forman Re mayor (D)?",
                        "answer": "Dedo 1 en 3ª cuerda traste 2, dedo 2 en 1ª cuerda traste 2 y dedo 3 en 2ª cuerda traste 3. Se rasguea desde la 4ª cuerda. (Las otras dos digitaciones son E y A.)",
                        "hints": ["Es el único de los tres acordes que usa el traste 3."],
                        "payload": {
                            "chord": "D",
                            "lab_link": "guitar:chords",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Dedo 1 en 3ª cuerda traste 1, dedo 2 en 5ª traste 2 y dedo 3 en 4ª traste 2",
                                    "Dedo 2 en 4ª cuerda traste 2, dedo 1 en 3ª traste 2 y dedo 3 en 2ª traste 2",
                                    "Dedo 1 en 3ª cuerda traste 2, dedo 2 en 1ª traste 2 y dedo 3 en 2ª traste 3",
                                ],
                                "correct": 2,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Traste del dedo 1 en Mi mayor (E)",
                        "prompt": "En Mi mayor (E), ¿en qué traste de la 3ª cuerda queda el dedo 1? Respondé solo con el número de traste.",
                        "answer": "En el traste 1. Viniendo de D o A, el dedo 1 se desliza por la 3ª cuerda del traste 2 al traste 1, y los dedos 2 y 3 van al traste 2 de la 5ª y la 4ª cuerda (como en Em).",
                        "hints": ["En D y A el dedo ancla está en el traste 2; en E se desliza hacia la cejuela."],
                        "payload": {
                            "chord": "E",
                            "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": "traste"},
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Reconocer un acorde por su digitación",
                        "prompt": "Dedo 2 en 4ª cuerda traste 2, dedo 1 en 3ª cuerda traste 2 y dedo 3 en 2ª cuerda traste 2. ¿Qué acorde es? Respondé con el nombre o la letra del acorde.",
                        "answer": "La mayor (A), con la digitación moderna 2-1-3: los tres dedos en el traste 2 y el índice en la 3ª cuerda, igual que en D.",
                        "hints": ["Los tres dedos están en el mismo traste."],
                        "payload": {
                            "chord": "A",
                            "lab_link": "guitar:chords",
                            "check": {
                                "type": "text",
                                "accept": ["a", "la", "la mayor", "a mayor", "la mayor (a)", "a (la mayor)"],
                            },
                        },
                    },
                ],
            },
            {
                "slug": "g-ritmo-4-4",
                "title": "4. Ritmo base en 4/4 y metrónomo",
                "level": 2,
                "order_index": 4,
                "summary": "El motor rítmico constante: la mano derecha nunca se detiene (péndulo de corcheas) y patrones universales.",
                "prerequisites": ["g-acordes-em-am"],
                "metadata": {"section": "Acordes y ritmo", "lab_tab": "metronome", "est_minutes": 15},
                "items": [
                    {
                        "item_type": "recall",
                        "title": "Regla de oro de la mano derecha (péndulo)",
                        "prompt": "Al rasguear en corcheas ('1 y 2 y 3 y 4 y'), ¿cuál es el principio más importante de la mano derecha?",
                        "answer": "Mantener un movimiento pendular constante: bajar en los números (1, 2, 3, 4) y subir en los 'y', aunque en algunos tiempos pases por el aire sin tocar las cuerdas.",
                        "hints": ["Tu brazo derecho actúa como un metrónomo mecánico."],
                        "payload": {
                            "lab_link": "guitar:metronome",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Frenar la mano en los silencios para no hacer ruido",
                                    "Mantener el péndulo constante: bajar en los números y subir en los 'y', aunque a veces pase por el aire",
                                    "Rasguear siempre hacia abajo para marcar fuerte cada pulso",
                                ],
                                "correct": 1,
                            },
                        },
                    },
                    {
                        "item_type": "drill",
                        "title": "Escalera de BPM: Patrón universal (D - D U - U D U)",
                        "prompt": "Con las cuerdas silenciadas (mano izquierda apoyada suave) o en Em, practicá el patrón ↓  ↓↑  ↑↓↑ ('1  2y  y4y') en Escalera de BPM empezando en 55 BPM.",
                        "answer": "Hacé 3 vueltas limpias sin perder el tiempo 1 para subir +5 BPM. Variación: acentuá el tiempo 2 y 4.",
                        "hints": ["En el tiempo 3 tu mano baja en el aire sin golpear cuerdas."],
                        "payload": {
                            "lab_link": "guitar:metronome",
                            "start_bpm": 55,
                            "overlearning_reps": 3,
                            "lab_metric": {"type": "bpm_clean", "good": 70, "easy": 90, "unit": "BPM"},
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Rasgueos que suenan en el patrón universal",
                        "prompt": "En el patrón universal ↓  ↓↑  ↑↓↑ (contado '1  2 y  y 4 y'), ¿cuántos rasgueos suenan en un compás? Respondé solo con el número.",
                        "answer": "6 rasgueos: 1 (↓), 2 (↓), 'y' del 2 (↑), 'y' del 3 (↑), 4 (↓) y 'y' del 4 (↑). La mano hace 8 movimientos, pero 2 pasan por el aire.",
                        "hints": ["Contá las flechas del patrón, no los movimientos de la mano."],
                        "payload": {
                            "lab_link": "guitar:metronome",
                            "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": "rasgueos"},
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Golpes al aire del patrón universal",
                        "prompt": "En el patrón universal, ¿en qué dos momentos del compás la mano pasa por el aire sin tocar las cuerdas?",
                        "answer": "En el 'y' del 1 (la mano sube sin tocar) y en el 3 (la mano baja sin tocar). El péndulo sigue igual; solo se saltean esos dos golpes.",
                        "hints": ["Mirá los huecos de '1  2 y  y 4 y'."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": [
                                    "En el 2 y en el 4",
                                    "En el 'y' del 1 y en el 3",
                                    "En el 1 y en el 'y' del 4",
                                ],
                                "correct": 1,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Cómo empezar a practicar un patrón de rasgueo",
                        "prompt": "Ordená los pasos para aprender el patrón universal desde cero.",
                        "answer": "Primero apagás las cuerdas con la mano izquierda, después tocás el patrón a 55 BPM con el péndulo constante, lo repetís hasta que salga automático 4 vueltas seguidas y recién ahí agregás el acorde Em.",
                        "hints": ["El acorde se agrega al final, cuando la mano derecha ya va sola."],
                        "payload": {
                            "lab_link": "guitar:metronome",
                            "check": {
                                "type": "order",
                                "lines": [
                                    "Apagá las cuerdas apoyando la mano izquierda sin apretar",
                                    "Tocá el patrón a 55 BPM con el péndulo constante",
                                    "Repetilo hasta que salga automático 4 vueltas seguidas",
                                    "Recién ahí agregá el acorde Em",
                                ],
                            },
                        },
                    },
                ],
            },
            {
                "slug": "g-acordes-g-c",
                "title": "5. Acordes G y C (apertura de mano)",
                "level": 3,
                "order_index": 5,
                "summary": "Dominar Sol mayor y Do mayor, los pilares de miles de canciones, aislando la transición G ↔ C.",
                "prerequisites": ["g-acordes-d-a-e", "g-ritmo-4-4"],
                "metadata": {"section": "Primeras canciones", "lab_tab": "chords", "chords": ["G", "C"], "est_minutes": 20},
                "items": [
                    {
                        "item_type": "recall",
                        "title": "Evitar apagar la 1ª cuerda en Do mayor (C)",
                        "prompt": "¿Por qué suele sonar apagada la 1ª cuerda (Mi agudo) al aprender Do mayor (C) y cómo se corrige?",
                        "answer": "Porque el dedo 1 (en 2ª cuerda traste 1) se aplasta y roza la 1ª cuerda. Se corrige bajando ligeramente el pulgar detrás del mástil y arqueando más los nudillos.",
                        "hints": ["Revisá la altura de la muñeca y el ángulo de ataque de la yema."],
                        "payload": {
                            "chord": "C",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Falta pisar la 1ª cuerda en el traste 1; se corrige agregando el meñique",
                                    "La 1ª cuerda está desafinada; se corrige con el afinador",
                                    "El dedo 1 se aplasta y roza la 1ª cuerda; se corrige bajando el pulgar y arqueando más el dedo",
                                ],
                                "correct": 2,
                            },
                        },
                    },
                    {
                        "item_type": "drill",
                        "title": "Micro-Drill: G ↔ C en cámara lenta + 1 minuto",
                        "prompt": "Aislá solo el salto de dedos entre G y C. Primero 5 repeticiones lentísimas cayendo todos los dedos a la vez, luego 1 minuto medido en el Laboratorio de Guitarra.",
                        "answer": "Meta: >25 cambios limpios/min. Variación (Johns Hopkins): probá el mismo cambio con rasgueo hacia arriba en el tiempo 4.",
                        "hints": ["Mirá el destino antes de despegar los dedos."],
                        "payload": {
                            "lab_link": "guitar:chords",
                            "pair": ["G", "C"],
                            "overlearning_reps": 3,
                            "lab_metric": {"type": "chord_changes_min", "good": 25, "easy": 40, "unit": "cambios/min"},
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Digitación de Do mayor (C)",
                        "prompt": "¿Qué dedos y trastes forman Do mayor (C)?",
                        "answer": "Dedo 3 en 5ª cuerda traste 3, dedo 2 en 4ª cuerda traste 2 y dedo 1 en 2ª cuerda traste 1. La 3ª y la 1ª van al aire y se rasguea desde la 5ª.",
                        "hints": ["Forma una diagonal: trastes 3, 2 y 1."],
                        "payload": {
                            "chord": "C",
                            "lab_link": "guitar:chords",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Dedo 3 en 5ª cuerda traste 3, dedo 2 en 4ª traste 2 y dedo 1 en 2ª traste 1",
                                    "Dedo 3 en 6ª cuerda traste 3, dedo 2 en 5ª traste 2 y dedo 4 en 1ª traste 3",
                                    "Dedo 3 en 5ª cuerda traste 3, dedo 2 en 4ª traste 2 y dedo 1 en 1ª traste 1",
                                ],
                                "correct": 0,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Por qué armar G con los dedos 3–2–4",
                        "prompt": "¿Qué ventaja tiene la digitación 3–2–4 de Sol mayor (G) cuando el acorde siguiente es C?",
                        "answer": "Con anular en 6ª, medio en 5ª y meñique en 1ª, los dedos 3 y 2 solo bajan una cuerda cada uno (a la 5ª y la 4ª) para convertirse en C: el recorrido es mínimo.",
                        "hints": ["Compará dónde están los dedos 3 y 2 en G y en C."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Deja el meñique libre para descansar",
                                    "Los dedos 3 y 2 solo bajan una cuerda cada uno para formar C",
                                    "Permite rasguear C con las 6 cuerdas",
                                ],
                                "correct": 1,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Cuerdas que se rasguean en G y en C",
                        "prompt": "¿Desde qué cuerda se rasguea Sol mayor (G) y desde cuál Do mayor (C)?",
                        "answer": "G se rasguea con las 6 cuerdas (desde la 6ª) y C desde la 5ª: la 6ª cuerda no se toca en Do mayor.",
                        "hints": ["En C la raíz (Do) está en la 5ª cuerda, traste 3."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": [
                                    "G desde la 5ª; C desde la 6ª",
                                    "Los dos desde la 6ª",
                                    "G desde la 6ª; C desde la 5ª",
                                ],
                                "correct": 2,
                            },
                        },
                    },
                ],
            },
            {
                "slug": "g-primera-cancion",
                "title": "6. Primera canción completa (I–V–vi–IV)",
                "level": 3,
                "order_index": 6,
                "summary": "Integrar G – D – Em – C con ritmo continuo aplicando práctica por fragmentos (chunking).",
                "prerequisites": ["g-acordes-g-c"],
                "metadata": {"section": "Primeras canciones", "lab_tab": "metronome", "est_minutes": 25},
                "items": [
                    {
                        "item_type": "recall",
                        "title": "Método correcto para estudiar una canción",
                        "prompt": "Si te trabás siempre al pasar del compás 2 al 3 en una canción, ¿por qué NO conviene volver a tocarla desde el principio?",
                        "answer": "Porque perdés tiempo repitiendo lo que ya sabés y llegás con tensión al error. La práctica deliberada aísla solo la transición difícil (ej. D → Em) hasta que salga 5 veces limpias y luego la reconecta.",
                        "hints": ["Aislar el micro-fallo acelera la mielinización del circuito correcto."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Porque el principio de la canción siempre es la parte más difícil",
                                    "Porque repetís lo que ya sabés y llegás tenso al error; conviene aislar solo esa transición y después reconectarla",
                                    "Porque primero hay que subir el tempo y recién después corregir el error",
                                ],
                                "correct": 1,
                            },
                        },
                    },
                    {
                        "item_type": "drill",
                        "title": "Progresión completa: G → D → Em → C a tempo estable",
                        "prompt": "Tocá 1 compás por acorde (G - D - Em - C) con el metrónomo a 65 BPM sin frenar la mano derecha aunque un acorde tarde un instante.",
                        "answer": "Regla de oro musical: el ritmo nunca se detiene. Completá 4 vueltas limpias y guardá tu BPM limpio.",
                        "hints": ["Anticipá el movimiento de la mano izquierda en el último 'y' del compás."],
                        "payload": {
                            "lab_link": "guitar:metronome",
                            "target_bpm": 65,
                            "overlearning_reps": 3,
                            "lab_metric": {"type": "bpm_clean", "good": 65, "easy": 80, "unit": "BPM"},
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Orden de la progresión I–V–vi–IV en Sol mayor",
                        "prompt": "Ordená los acordes de la progresión I–V–vi–IV en Sol mayor.",
                        "answer": "G → D → Em → C: un compás de cada uno, y la vuelta vuelve a empezar en G.",
                        "hints": ["Arranca en el acorde que le da nombre a la tonalidad."],
                        "payload": {
                            "lab_link": "guitar:metronome",
                            "check": {"type": "order", "lines": ["G", "D", "Em", "C"]},
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Pulsos de una vuelta completa",
                        "prompt": "Con un compás de 4/4 por acorde, ¿cuántos pulsos dura una vuelta completa de G – D – Em – C? Respondé solo con el número de pulsos.",
                        "answer": "16 pulsos: 4 acordes × 4 pulsos cada uno.",
                        "hints": ["Cada compás de 4/4 tiene 4 pulsos."],
                        "payload": {"check": {"type": "numeric", "value": 16, "tolerance": 0, "unit": "pulsos"}},
                    },
                    {
                        "item_type": "recall",
                        "title": "Anticipación del cambio de acorde",
                        "prompt": "Para llegar en tiempo al acorde siguiente, ¿en qué momento conviene despegar la mano izquierda?",
                        "answer": "En el último 'y' del pulso 4: suenan las cuerdas al aire un instante y la mano izquierda gana tiempo para caer justo en el pulso 1 del acorde siguiente.",
                        "hints": ["Hay que salir antes para llegar a tiempo."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": [
                                    "En el último 'y' del pulso 4",
                                    "Justo en el pulso 1 del compás nuevo",
                                    "En el pulso 2, a mitad del compás",
                                ],
                                "correct": 0,
                            },
                        },
                    },
                ],
            },
            {
                "slug": "g-oido-musical",
                "title": "7. Entrenamiento auditivo inicial",
                "level": 4,
                "order_index": 7,
                "summary": "Reconocer sonoridad mayor vs. menor e intervalos fundamentales (3ª, 5ª, 8ª) para tocar de oído.",
                "prerequisites": ["g-acordes-d-a-e"],
                "metadata": {"section": "Oído y técnica", "lab_tab": "ear", "est_minutes": 15},
                "items": [
                    {
                        "item_type": "recall",
                        "title": "Diferencia interválica entre acorde Mayor y Menor",
                        "prompt": "¿Qué nota cambia exactamente entre un acorde mayor (ej. E) y su homónimo menor (ej. Em)?",
                        "answer": "La tercera del acorde baja medio tono (1 traste hacia la cejuela). En E → Em levantás el dedo 1 de la 3ª cuerda traste 1 (Sol# → Sol).",
                        "hints": ["Es solo 1 semitono de diferencia, pero cambia totalmente el color emocional."],
                        "payload": {
                            "lab_link": "guitar:ear",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "La raíz, que baja un semitono",
                                    "La tercera, que baja un semitono",
                                    "La quinta, que baja un semitono",
                                ],
                                "correct": 1,
                            },
                        },
                    },
                    {
                        "item_type": "drill",
                        "title": "Drill Auditivo: Mayor vs. Menor e Intervalos",
                        "prompt": "Abrí el Laboratorio de Guitarra → Oído y acertá al menos 8 de 10 pruebas seguidas distinguiendo acordes mayores/menores e intervalos.",
                        "answer": "Cantá la segunda nota antes de elegir tu respuesta: involucrar la voz duplica la retención auditiva.",
                        "hints": ["Asociá cada intervalo a una melodía conocida."],
                        "payload": {"lab_link": "guitar:ear", "overlearning_reps": 3},
                    },
                    {
                        "item_type": "recall",
                        "title": "Semitonos de una tercera menor",
                        "prompt": "¿Cuántos semitonos (trastes) hay entre la raíz y la tercera en un acorde MENOR? Respondé solo con el número de semitonos.",
                        "answer": "3 semitonos. La tercera mayor está a 4; esa diferencia de 1 semitono es la que cambia el color del acorde.",
                        "hints": ["Es uno menos que en el acorde mayor."],
                        "payload": {
                            "lab_link": "guitar:ear",
                            "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": "semitonos"},
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Trastes de una quinta justa",
                        "prompt": "¿A cuántos trastes de la raíz está la quinta justa? Respondé solo con el número de trastes.",
                        "answer": "A 7 trastes (7 semitonos). Es el salto del inicio de Star Wars.",
                        "hints": ["La octava está a 12 trastes; la quinta queda un poco más allá de la mitad."],
                        "payload": {
                            "lab_link": "guitar:ear",
                            "check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": "trastes"},
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Las tres notas de una tríada",
                        "prompt": "¿Qué tres notas forman un acorde básico (tríada)?",
                        "answer": "Raíz (1ª), tercera (3ª) y quinta (5ª). La tercera es la que define si el acorde es mayor o menor.",
                        "hints": ["Una de las tres decide si suena alegre o melancólico."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Raíz, segunda y octava",
                                    "Tercera, quinta y séptima",
                                    "Raíz, tercera y quinta",
                                ],
                                "correct": 2,
                            },
                        },
                    },
                ],
            },
            {
                "slug": "g-pua-pentatonica",
                "title": "8. Púa alternada y escala pentatónica menor",
                "level": 4,
                "order_index": 8,
                "summary": "Coordinación mano izquierda/derecha con púa abajo-arriba y la caja 1 de la pentatónica de Em/Am.",
                "prerequisites": ["g-primera-cancion", "g-oido-musical"],
                "metadata": {"section": "Oído y técnica", "lab_tab": "metronome", "est_minutes": 20},
                "items": [
                    {
                        "item_type": "recall",
                        "title": "Principio de la púa alternada (Alternate Picking)",
                        "prompt": "¿Por qué conviene alternar estrictamente ↓ ↑ ↓ ↑ incluso cuando tocás lento en notas sueltas?",
                        "answer": "Porque economiza el movimiento a la mitad y sincroniza la mano derecha con el pulso (↓ en tiempos fuertes, ↑ en contratiempos), eliminando un techo de velocidad futuro.",
                        "hints": ["Pensá en eficiencia de trayectoria y ritmo."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Porque reduce el recorrido de la mano a la mitad y la sincroniza con el pulso",
                                    "Porque suena más fuerte que tocar todo hacia abajo",
                                    "Porque así la mano izquierda no necesita apretar tanto",
                                ],
                                "correct": 0,
                            },
                        },
                    },
                    {
                        "item_type": "drill",
                        "title": "Caja 1 Pentatónica de La menor (traste 5) en Escalera BPM",
                        "prompt": "Tocá la forma 1 de Am pentatónica (6ª: 5-8, 5ª: 5-7, 4ª: 5-7, 3ª: 5-7, 2ª: 5-8, 1ª: 5-8) con púa alternada estricta a 60 BPM en negras, luego corcheas.",
                        "answer": "Variación motora: tocá subiendo con acento en la 1ª nota de cada cuerda, o en grupos de 3 notas.",
                        "hints": ["Un dedo por traste: índice en traste 5, anular en 7, meñique en 8."],
                        "payload": {
                            "lab_link": "guitar:metronome",
                            "start_bpm": 60,
                            "overlearning_reps": 3,
                            "lab_metric": {"type": "bpm_clean", "good": 70, "easy": 90, "unit": "BPM"},
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Trastes de la 4ª cuerda en la Caja 1 de Am",
                        "prompt": "En la Caja 1 de la pentatónica de La menor, ¿qué trastes se tocan en la 4ª cuerda?",
                        "answer": "5 y 7 (índice y anular). El patrón de 6ª a 1ª es 5–8, 5–7, 5–7, 5–7, 5–8, 5–8.",
                        "hints": ["Las tres cuerdas del medio (5ª, 4ª y 3ª) comparten la misma pareja de trastes."],
                        "payload": {
                            "lab_link": "guitar:fretboard",
                            "check": {"type": "choice", "options": ["5 y 7", "5 y 8", "5 y 6"], "correct": 0},
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Tónicas (La) dentro de la Caja 1",
                        "prompt": "¿Dónde están las tres notas La (A) de la Caja 1 de Am pentatónica?",
                        "answer": "6ª cuerda traste 5, 4ª cuerda traste 7 y 1ª cuerda traste 5. Empezar o terminar una frase ahí suena resuelto.",
                        "hints": ["Dos de las tres están en el traste 5, en las dos cuerdas Mi."],
                        "payload": {
                            "lab_link": "guitar:fretboard",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "6ª cuerda traste 8, 3ª traste 5 y 1ª traste 8",
                                    "6ª cuerda traste 5, 4ª traste 7 y 1ª traste 5",
                                    "5ª cuerda traste 5, 4ª traste 5 y 2ª traste 5",
                                ],
                                "correct": 1,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Dedo del traste 8 en la Caja 1",
                        "prompt": "Con la regla de 'un dedo por traste' en la Caja 1 (traste 5), ¿qué dedo pisa el traste 8?",
                        "answer": "El meñique: índice=traste 5, medio=6, anular=7 y meñique=8.",
                        "hints": ["El índice se queda en el traste 5."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": ["Índice", "Medio", "Anular", "Meñique"],
                                "correct": 3,
                            },
                        },
                    },
                ],
            },
        ],
    },
    {
        "slug": "electronica",
        "name": "Electrónica (Arduino / ESP32)",
        "icon": "electronics",
        "color": "#387478",
        "domain_type": "project",
        "lab_type": "electronics",
        "description": (
            "Aprendizaje basado en proyectos (PBL) en espiral: electricidad intuitiva, "
            "simulación en el Arduino virtual y en Wokwi, protoboard, debugging de hardware/firmware y proyectos IoT con ESP32."
        ),
        "config": {
            "tools": ["ohm_lab", "pinout", "debug_puzzles", "spiral_pbl"],
            "method_tips": [
                "Simulá primero en el Arduino virtual (o en Wokwi si usás Wi-Fi o I²C del ESP32) para aislar errores de lógica antes de cablear en la protoboard física.",
                "Ante un fallo, separá siempre la hipótesis: ¿es hardware (alimentación/cableado) o software (pin/lógica)?",
                "Usá Serial.println() como 'rayos X' de tu firmware para ver qué está leyendo realmente el microcontrolador.",
            ],
        },
        "nodes": [
            {
                "slug": "e-ley-de-ohm",
                "title": "1. Intuición eléctrica y Ley de Ohm",
                "level": 1,
                "order_index": 1,
                "summary": "Voltaje (presión), Corriente (flujo) y Resistencia (estrechamiento) + cálculo de resistencia para LED.",
                "prerequisites": [],
                "metadata": {"section": "Electricidad y taller", "lab_tab": "ohm", "est_minutes": 20},
                "items": [
                    {
                        "item_type": "recall",
                        "title": "Analogía física de V, I y R",
                        "prompt": "Usando la analogía del agua en una tubería, explicá qué son Voltaje (V), Corriente (I) y Resistencia (R) y escribí la Ley de Ohm.",
                        "answer": "Voltaje (V) = presión que empuja el agua; Corriente (I, Amperios) = caudal que fluye; Resistencia (R, Ohmios Ω) = estrechamiento del tubo. Ley de Ohm: V = I · R (y I = V/R, R = V/I).",
                        "hints": ["A mayor voltaje con misma resistencia, mayor corriente."],
                        "payload": {"lab_link": "electronics:ohm"},
                    },
                    {
                        "item_type": "recall",
                        "title": "Fórmula de resistencia limitadora para un LED",
                        "prompt": "¿Por qué se quema un LED si lo conectás directo a 5V sin resistencia, y cómo calculás la resistencia necesaria?",
                        "answer": "Un LED tiene muy baja resistencia interna una vez superado su voltaje directo (Vf ≈ 2V en rojo), por lo que absorbe corriente excesiva y se quema. Fórmula: R = (V_fuente - V_led) / I_deseada. Ej: (5V - 2V) / 0.015A = 200 Ω → usar 220 Ω.",
                        "hints": ["Restá la caída del LED al voltaje de la fuente antes de dividir por la corriente en amperios."],
                        "payload": {
                            "lab_link": "electronics:ohm",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Porque pasado su Vf casi no limita la corriente; R = (V_fuente − V_led) / I",
                                    "Porque 5 V supera el voltaje máximo de cualquier LED; R = V_fuente / I",
                                    "Porque el LED tiene una resistencia interna muy alta; R = (V_fuente + V_led) · I",
                                ],
                                "correct": 0,
                            },
                        },
                    },
                    {
                        "item_type": "drill",
                        "title": "Simulación práctica: LED en 3.3V (ESP32) vs 5V (Arduino)",
                        "prompt": "Abrí el Laboratorio de Electrónica → Ley de Ohm y calculá la resistencia comercial para un LED azul (Vf=3.0V, 10mA) en Arduino (5V) y en ESP32 (3.3V).",
                        "answer": "En 5V: (5 - 3)/0.01 = 200 Ω (comercial 220 Ω). En 3.3V: (3.3 - 3)/0.01 = 30 Ω (comercial 33 Ω o 47 Ω).",
                        "hints": ["Cambiá el selector de voltaje en el simulador para ver las bandas de color."],
                        "payload": {"lab_link": "electronics:ohm"},
                    },
                    {
                        "item_type": "worked_example",
                        "title": "Resistencia para un LED rojo a 9 V",
                        "prompt": "Calculá la resistencia teórica para un LED rojo (Vf = 2 V) alimentado con 9 V y una corriente de 10 mA. Respondé solo con el número en Ω (antes de elegir el valor comercial).",
                        "answer": "R = (9 − 2) / 0.010 = 7 / 0.010 = 700 Ω. El valor comercial inmediato superior de la serie E12 es 820 Ω.",
                        "hints": ["Restá la caída del LED y convertí 10 mA a 0.010 A."],
                        "payload": {
                            "lab_link": "electronics:ohm",
                            "check": {"type": "numeric", "value": 700, "tolerance": 0.02, "unit": "Ω"},
                        },
                    },
                    {
                        "item_type": "worked_example",
                        "title": "Corriente por una resistencia (I = V / R)",
                        "prompt": "Una resistencia de 330 Ω queda conectada directamente a 3.3 V. ¿Qué corriente circula? Respondé solo con el número en mA.",
                        "answer": "I = V / R = 3.3 / 330 = 0.010 A = 10 mA.",
                        "hints": ["Calculá en amperios y multiplicá por 1000 para pasar a mA."],
                        "payload": {
                            "lab_link": "electronics:ohm",
                            "check": {"type": "numeric", "value": 10, "tolerance": 0.02, "unit": "mA"},
                        },
                    },
                    {
                        "item_type": "worked_example",
                        "title": "Caída de voltaje en una resistencia (V = I · R)",
                        "prompt": "Por una resistencia de 150 Ω circulan 20 mA. ¿Cuántos voltios caen sobre ella? Respondé solo con el número en V.",
                        "answer": "V = I · R = 0.020 A × 150 Ω = 3 V.",
                        "hints": ["Pasá 20 mA a 0.020 A antes de multiplicar."],
                        "payload": {
                            "lab_link": "electronics:ohm",
                            "check": {"type": "numeric", "value": 3, "tolerance": 0.02, "unit": "V"},
                        },
                    },
                ],
            },
            {
                "slug": "e-protoboard-seguridad",
                "title": "2. Protoboard, multímetro y 3.3V vs 5V",
                "level": 1,
                "order_index": 2,
                "summary": "Cómo están conectadas las pistas internas de la protoboard, polaridad y reglas para no quemar un ESP32.",
                "prerequisites": ["e-ley-de-ohm"],
                "metadata": {"section": "Electricidad y taller", "lab_tab": "pinout", "est_minutes": 15},
                "items": [
                    {
                        "item_type": "recall",
                        "title": "Regla crítica de voltaje: Arduino Uno vs ESP32",
                        "prompt": "¿Qué pasa si conectás una señal de salida de 5V de un sensor/Arduino directo a un pin GPIO de un ESP32?",
                        "answer": "Podés dañar permanentemente el ESP32: sus pines GPIO trabajan a 3.3V y NO son tolerantes a 5V. Necesitás un divisor resistivo o un conversor de nivel lógico (level shifter).",
                        "hints": ["Revisá el voltaje lógico en el Laboratorio de Electrónica → Pines."],
                        "payload": {
                            "lab_link": "electronics:pinout",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "No pasa nada: los GPIO del ESP32 toleran 5 V",
                                    "Podés dañar el ESP32: sus GPIO trabajan a 3.3 V; hace falta un divisor resistivo o un level shifter",
                                    "El ESP32 se apaga solo para protegerse y después sigue funcionando normal",
                                ],
                                "correct": 1,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Conexiones internas de una protoboard",
                        "prompt": "¿Cómo están conectados internamente los rieles laterales (+/-) versus las filas centrales separadas por el canal del medio?",
                        "answer": "Los rieles laterales (+/-) corren conectados a lo largo (verticalmente) para alimentación; las filas centrales conectan grupos de 5 huecos en horizontal, aislados por la zanja central.",
                        "hints": ["La zanja central está pensada para montar circuitos integrados o el ESP32 sin cortocircuitar sus patas."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Todos los huecos de la protoboard están conectados entre sí",
                                    "Rieles laterales en grupos de 5 huecos; filas centrales unidas a lo largo de toda la placa",
                                    "Rieles laterales unidos a lo largo; filas centrales en grupos de 5 huecos, separadas por la zanja",
                                ],
                                "correct": 2,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Polaridad del LED: ánodo y cátodo",
                        "prompt": "En un LED nuevo, ¿qué pata es el ánodo (+)?",
                        "answer": "La pata larga es el ánodo (+). La pata corta, del lado del borde plano, es el cátodo (−) y va hacia GND.",
                        "hints": ["Larga = positivo."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": ["La pata larga", "La pata corta", "La que está del lado del borde plano"],
                                "correct": 0,
                            },
                        },
                    },
                    {
                        "item_type": "worked_example",
                        "title": "Divisor resistivo para bajar 5 V",
                        "prompt": "Un divisor con R1 = 2.2 kΩ (hacia la señal de 5 V) y R2 = 3.3 kΩ (hacia GND) entrega V_out = V_in · R2 / (R1 + R2). ¿Cuánto vale V_out? Respondé solo con el número en V.",
                        "answer": "V_out = 5 · 3.3 / (2.2 + 3.3) = 5 · 0.6 = 3.0 V: un nivel seguro para un GPIO del ESP32 (máximo 3.3 V).",
                        "hints": ["Sumá primero las dos resistencias; los kΩ se cancelan en la división."],
                        "payload": {
                            "lab_link": "electronics:ohm",
                            "check": {"type": "numeric", "value": 3, "tolerance": 0.02, "unit": "V"},
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Rutina segura antes de energizar el circuito",
                        "prompt": "Ordená los pasos para armar un circuito en la protoboard sin riesgo para la placa.",
                        "answer": "Siempre se cablea con el USB desconectado, se revisa (polaridades, GND común y que ningún GPIO del ESP32 reciba 5 V) y recién al final se conecta la alimentación.",
                        "hints": ["La alimentación es lo último que se conecta."],
                        "payload": {
                            "check": {
                                "type": "order",
                                "lines": [
                                    "Desconectá el cable USB",
                                    "Cableá el circuito en la protoboard",
                                    "Revisá polaridades, GND común y que ningún GPIO del ESP32 reciba 5 V",
                                    "Conectá el USB y probá",
                                ],
                            },
                        },
                    },
                ],
            },
            {
                "slug": "e-blink-wokwi",
                "title": "3. Primer firmware: Blink y ciclo setup/loop",
                "level": 2,
                "order_index": 3,
                "summary": "Nivel 1 (Guiado): escribir, simular en el Arduino virtual y cargar tu primer programa en Arduino/ESP32.",
                "prerequisites": ["e-protoboard-seguridad"],
                "metadata": {"section": "Microcontrolador", "lab_tab": "projects", "wokwi_url": "https://wokwi.com/projects/new/esp32", "est_minutes": 20},
                "items": [
                    {
                        "item_type": "recall",
                        "title": "Diferencia entre setup() y loop()",
                        "prompt": "En un sketch de Arduino/ESP32, ¿cuántas veces corre setup() y cuántas veces corre loop()? ¿Qué suele ir en cada uno?",
                        "answer": "setup() corre una sola vez al encender o reiniciar la placa (configurar pinMode, Serial.begin, Wi-Fi). loop() corre infinitamente en ciclo continuo (leer sensores, decidir, activar salidas).",
                        "hints": ["Uno inicializa, el otro ejecuta el comportamiento continuo."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": [
                                    "setup() corre una sola vez al encender o reiniciar; loop() se repite sin fin",
                                    "setup() se repite sin fin; loop() corre una sola vez",
                                    "Las dos corren una sola vez: primero setup() y después loop()",
                                ],
                                "correct": 0,
                            },
                        },
                    },
                    {
                        "item_type": "project_step",
                        "title": "Proyecto v1: LED parpadeante SOS en el simulador → Protoboard",
                        "prompt": "En el Arduino virtual del Laboratorio de Electrónica (LED en D13) o en Wokwi (GPIO 2 del ESP32), hacé parpadear el LED en Morse SOS y verificá qué pasa si olvidás pinMode(PIN, OUTPUT).",
                        "answer": "Sin pinMode(PIN, OUTPUT), el pin queda en modo entrada (alta impedancia) y el LED apenas brilla o no enciende.",
                        "hints": ["Probá primero en el Arduino virtual: con el osciloscopio ves la tensión de D13 en cada parte del SOS. Después pasalo a hardware real."],
                        "payload": {"lab_link": "electronics:arduino:serial-blink", "wokwi_url": "https://wokwi.com/projects/new/esp32"},
                    },
                    {
                        "item_type": "recall",
                        "title": "Estructura de un sketch Blink",
                        "prompt": "Ordená las líneas para formar un sketch Blink válido.",
                        "answer": "Primero la constante del pin, después setup() con pinMode(LED_PIN, OUTPUT) (corre una sola vez) y por último loop() con el encendido y apagado que se repite para siempre.",
                        "hints": ["La constante se declara antes de usarla; setup() va antes que loop()."],
                        "payload": {
                            "lab_link": "electronics:projects",
                            "check": {
                                "type": "order",
                                "lines": [
                                    "const int LED_PIN = 2;",
                                    "void setup() {",
                                    "  pinMode(LED_PIN, OUTPUT); }",
                                    "void loop() {",
                                    "  digitalWrite(LED_PIN, HIGH); delay(500); digitalWrite(LED_PIN, LOW); delay(500); }",
                                ],
                            },
                        },
                    },
                    {
                        "item_type": "debug",
                        "title": "Bug: el LED apenas brilla",
                        "prompt": "Este sketch compila, pero el LED en GPIO 2 apenas brilla: void setup() { Serial.begin(115200); }  void loop() { digitalWrite(2, HIGH); }  ¿Qué línea falta?",
                        "answer": "Falta pinMode(2, OUTPUT); en setup(). Sin esa línea el pin queda como entrada (alta impedancia) y casi no entrega corriente al LED.",
                        "hints": ["Antes de escribir en un pin hay que configurarlo."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Serial.println(\"LED\"); dentro de loop()",
                                    "pinMode(2, OUTPUT); dentro de setup()",
                                    "digitalWrite(2, LOW); dentro de setup()",
                                ],
                                "correct": 1,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Voltaje de un pin en HIGH (ESP32)",
                        "prompt": "¿Qué voltaje pone digitalWrite(PIN, HIGH) en un pin de un ESP32? Respondé solo con el número en V.",
                        "answer": "3.3 V. En un Arduino Uno serían 5 V; LOW es 0 V (GND) en las dos placas.",
                        "hints": ["El ESP32 trabaja con una lógica más baja que el Arduino Uno."],
                        "payload": {"check": {"type": "numeric", "value": 3.3, "tolerance": 0.01, "unit": "V"}},
                    },
                ],
            },
            {
                "slug": "e-entradas-pullup",
                "title": "4. Entradas digitales y debugging de pin flotante",
                "level": 2,
                "order_index": 4,
                "summary": "Leer pulsadores de forma confiable usando INPUT_PULLUP y diagnosticar lecturas aleatorias.",
                "prerequisites": ["e-blink-wokwi"],
                "metadata": {"section": "Microcontrolador", "lab_tab": "debug", "est_minutes": 20},
                "items": [
                    {
                        "item_type": "debug",
                        "title": "Bug clásico: El botón se activa solo sin tocarlo",
                        "prompt": "Conectaste un pulsador entre GPIO 4 y 3.3V usando pinMode(4, INPUT). Cuando NO lo presionás, Serial.println(digitalRead(4)) imprime 0 y 1 al azar. ¿Cuál es la causa y la solución más limpia?",
                        "answer": "El pin está 'flotante' (actúa como antena captando ruido electromagnético). Solución más limpia: conectar el botón entre GPIO 4 y GND, configurar pinMode(4, INPUT_PULLUP) y recordar que presionado = LOW.",
                        "hints": ["Sin resistencia pull-up o pull-down, un pin abierto no tiene voltaje definido."],
                        "payload": {
                            "lab_link": "electronics:debug",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "El pulsador está fallado; hay que cambiarlo por uno nuevo",
                                    "El pin queda flotante y capta ruido; botón a GND con INPUT_PULLUP (presionado = LOW)",
                                    "Falta un delay(1000) en loop() para estabilizar la lectura",
                                ],
                                "correct": 1,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Lógica invertida con INPUT_PULLUP",
                        "prompt": "Cuando usás pinMode(PIN, INPUT_PULLUP) con un pulsador a GND, ¿qué devuelve digitalRead(PIN) cuando el botón está suelto vs. presionado?",
                        "answer": "Suelto devuelve HIGH (1) gracias a la resistencia interna hacia VCC; presionado conecta a tierra y devuelve LOW (0).",
                        "hints": ["Pull-UP tira el voltaje hacia ARRIBA cuando nadie presiona."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Suelto = LOW (0); presionado = HIGH (1)",
                                    "Suelto = HIGH (1); presionado = LOW (0)",
                                    "Suelto = valor al azar; presionado = HIGH (1)",
                                ],
                                "correct": 1,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Código mínimo para leer un pulsador con INPUT_PULLUP",
                        "prompt": "Ordená las líneas para leer un pulsador conectado entre GPIO 4 y GND.",
                        "answer": "Se declara el pin, en setup() se inicia Serial y se configura el pin con INPUT_PULLUP, y en loop() se pregunta por LOW, porque con pull-up presionado = LOW.",
                        "hints": ["La configuración va en setup(); la lectura, en loop()."],
                        "payload": {
                            "lab_link": "electronics:debug",
                            "check": {
                                "type": "order",
                                "lines": [
                                    "const int BTN_PIN = 4;",
                                    "void setup() {",
                                    "  Serial.begin(115200); pinMode(BTN_PIN, INPUT_PULLUP); }",
                                    "void loop() {",
                                    "  if (digitalRead(BTN_PIN) == LOW) {",
                                    "    Serial.println(\"Presionado\"); } }",
                                ],
                            },
                        },
                    },
                    {
                        "item_type": "debug",
                        "title": "Bug: la acción se dispara cuando NO tocás el botón",
                        "prompt": "Pulsador entre GPIO 4 y GND con pinMode(4, INPUT_PULLUP). El código hace if (digitalRead(4) == HIGH) { digitalWrite(LED, HIGH); } y el LED queda prendido sin tocar nada. ¿Cuál es el arreglo?",
                        "answer": "Cambiar la condición a digitalRead(4) == LOW. Con INPUT_PULLUP la lógica es invertida: suelto = HIGH y presionado = LOW, así que preguntar por HIGH dispara la acción en reposo.",
                        "hints": ["¿Qué lee el pin cuando nadie lo presiona?"],
                        "payload": {
                            "lab_link": "electronics:debug",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Cambiar INPUT_PULLUP por INPUT",
                                    "Agregar una resistencia de 220 Ω en serie con el botón",
                                    "Cambiar la condición a == LOW",
                                ],
                                "correct": 2,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Cableado del pulsador con INPUT_PULLUP",
                        "prompt": "Con pinMode(PIN, INPUT_PULLUP), ¿entre qué dos puntos se conecta el pulsador?",
                        "answer": "Entre el pin y GND, sin resistencias externas: la pull-up interna mantiene el pin en HIGH y al presionar queda conectado a tierra (LOW).",
                        "hints": ["La resistencia interna ya tira hacia arriba; el botón tiene que tirar hacia el otro lado."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": ["Entre el pin y GND", "Entre el pin y 3.3 V", "Entre 3.3 V y GND"],
                                "correct": 0,
                            },
                        },
                    },
                ],
            },
            {
                "slug": "e-analog-pwm",
                "title": "5. Entradas analógicas (ADC) y PWM (Dimmer)",
                "level": 3,
                "order_index": 5,
                "summary": "Leer un potenciómetro (0–4095 en ESP32 / 0–1023 en Arduino) y modular brillo/velocidad con PWM.",
                "prerequisites": ["e-entradas-pullup"],
                "metadata": {"section": "Señales y multitarea", "lab_tab": "pinout", "est_minutes": 25},
                "items": [
                    {
                        "item_type": "recall",
                        "title": "¿Qué es PWM y cómo atenúa un LED?",
                        "prompt": "Si un pin digital solo puede sacar 0V o 3.3V/5V, ¿cómo logra PWM que un LED brille al 25% o 50%?",
                        "answer": "Enciende y apaga el pin cientos/miles de veces por segundo variando el 'duty cycle' (porcentaje de tiempo en HIGH). El ojo humano promedia la luz percibiendo menor brillo.",
                        "hints": ["Pulse Width Modulation = modulación por ancho de pulso."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Baja el voltaje del pin a un valor intermedio fijo (por ejemplo 1.65 V)",
                                    "Prende y apaga el pin muy rápido variando el porcentaje de tiempo en HIGH (duty cycle); el ojo promedia",
                                    "Limita la corriente con una resistencia interna variable",
                                ],
                                "correct": 1,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Resolución ADC y trampa ADC2 en ESP32",
                        "prompt": "¿Qué rango numérico entrega analogRead() en ESP32 (12 bits) vs Arduino Uno (10 bits), y qué pines ADC conviene evitar si usás Wi-Fi en ESP32?",
                        "answer": "ESP32 (12 bits): 0 a 4095; Arduino Uno (10 bits): 0 a 1023. En ESP32 evitá ADC2 cuando el Wi-Fi está activo; usá pines de ADC1 (GPIO 32–39).",
                        "hints": ["2^10 = 1024; 2^12 = 4096. Consultá la pestaña Pines del laboratorio."],
                        "payload": {
                            "lab_link": "electronics:pinout",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "ESP32: 0 a 1023; Uno: 0 a 4095; evitar ADC1 con Wi-Fi",
                                    "ESP32: 0 a 255; Uno: 0 a 1023; evitar GPIO 34 con Wi-Fi",
                                    "ESP32: 0 a 4095; Uno: 0 a 1023; evitar ADC2 con Wi-Fi (usar ADC1, GPIO 32–39)",
                                ],
                                "correct": 2,
                            },
                        },
                    },
                    {
                        "item_type": "worked_example",
                        "title": "Duty cycle de un valor de analogWrite",
                        "prompt": "Escribís analogWrite(LED_PIN, 51) (rango 0..255). ¿Qué duty cycle aproximado tiene la salida? Respondé solo con el número en %.",
                        "answer": "51 / 255 = 0.20 → 20%: el pin pasa en HIGH una quinta parte del tiempo y el LED se ve a un 20% de brillo.",
                        "hints": ["Dividí el valor por el máximo del rango (255)."],
                        "payload": {"check": {"type": "numeric", "value": 20, "tolerance": 0.03, "unit": "%"}},
                    },
                    {
                        "item_type": "worked_example",
                        "title": "Escalar una lectura ADC a PWM con map()",
                        "prompt": "En un ESP32, analogRead(34) devuelve 2048. ¿Qué valor entero aproximado da map(2048, 0, 4095, 0, 255)? Respondé solo con el número.",
                        "answer": "≈ 127: 2048 es la mitad del rango 0..4095, así que cae en la mitad del rango 0..255 (2048 × 255 / 4095 ≈ 127.5, y map() descarta los decimales).",
                        "hints": ["Regla de tres: 2048 es a 4095 como x es a 255."],
                        "payload": {"check": {"type": "numeric", "value": 127, "tolerance": 0.02, "unit": ""}},
                    },
                    {
                        "item_type": "recall",
                        "title": "Dimmer con potenciómetro: orden de las líneas",
                        "prompt": "Ordená las tres líneas de loop() para que un potenciómetro controle el brillo de un LED.",
                        "answer": "Primero leés el potenciómetro con analogRead (0..4095), después escalás a 0..255 con map() y por último aplicás el brillo con analogWrite.",
                        "hints": ["Leer → convertir → escribir."],
                        "payload": {
                            "lab_link": "electronics:pinout",
                            "check": {
                                "type": "order",
                                "lines": [
                                    "int crudo = analogRead(34);",
                                    "int brillo = map(crudo, 0, 4095, 0, 255);",
                                    "analogWrite(LED_PIN, brillo);",
                                ],
                            },
                        },
                    },
                ],
            },
            {
                "slug": "e-millis-multitarea",
                "title": "6. Código no bloqueante: delay() vs millis()",
                "level": 3,
                "order_index": 6,
                "summary": "Superar el cuello de botella #1 de principiantes mediante Parson's Problems con millis().",
                "prerequisites": ["e-analog-pwm"],
                "metadata": {"section": "Señales y multitarea", "lab_tab": "debug", "est_minutes": 25},
                "items": [
                    {
                        "item_type": "debug",
                        "title": "Por qué delay(2000) arruina los botones y sensores",
                        "prompt": "Tenés un LED que parpadea con delay(2000) y un botón de emergencia en el mismo loop(). ¿Por qué el botón casi nunca responde y cómo se resuelve?",
                        "answer": "delay(2000) congela completamente el procesador durante 2 segundos ignorando digitalRead(). Se resuelve guardando marcas de tiempo con unsigned long anterior = millis() y comprobando si (millis() - anterior >= intervalo).",
                        "hints": ["Usá resta (millis() - anterior) para evitar problemas incluso ante overflow."],
                        "payload": {
                            "lab_link": "electronics:debug",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "delay() congela el programa 2 s y en ese lapso no se lee el botón; se resuelve con el patrón millis()",
                                    "El botón necesita su propio delay(), más largo que el del LED",
                                    "El LED consume la corriente que necesita el botón; se resuelve con otra resistencia",
                                ],
                                "correct": 0,
                            },
                        },
                    },
                    {
                        "item_type": "drill",
                        "title": "Parson's Problem: Reordenar Blink sin delay()",
                        "prompt": "Abrí el Laboratorio de Electrónica → Encontrar el error y resolvé el rompecabezas de código para construir un parpadeo no bloqueante con millis().",
                        "answer": "Secuencia clave: leer ahora = millis() → comparar if (ahora - ultimo >= intervalo) → actualizar ultimo = ahora → invertir estado y escribir digitalWrite.",
                        "hints": ["Primero capturás el tiempo actual y verificás si pasó el intervalo."],
                        "payload": {
                            "lab_link": "electronics:debug",
                            "lab_metric": {"type": "debug_solved", "good": 1, "easy": 1, "unit": "puzzle"},
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Patrón millis(): orden de las líneas",
                        "prompt": "Ordená las líneas del patrón no bloqueante dentro de loop().",
                        "answer": "Primero capturás el tiempo actual, después comparás con resta contra el intervalo y, si se cumplió, actualizás la marca de tiempo y ejecutás la acción.",
                        "hints": ["La marca de tiempo se actualiza dentro del if, no afuera."],
                        "payload": {
                            "lab_link": "electronics:debug",
                            "check": {
                                "type": "order",
                                "lines": [
                                    "unsigned long ahora = millis();",
                                    "if (ahora - ultimo >= intervalo) {",
                                    "  ultimo = ahora; estado = !estado; digitalWrite(LED_PIN, estado);",
                                    "}",
                                ],
                            },
                        },
                    },
                    {
                        "item_type": "worked_example",
                        "title": "¿Cuándo se cumple la condición de millis()?",
                        "prompt": "Con ultimo = 2000 e intervalo = 500, ¿desde qué valor de millis() se cumple (millis() - ultimo >= intervalo)? Respondé solo con el número en ms.",
                        "answer": "Desde 2500 ms: 2500 − 2000 = 500, que ya cumple >= 500. Con 2499 la resta da 499 y todavía no.",
                        "hints": ["Sumá el intervalo a la última marca de tiempo."],
                        "payload": {"check": {"type": "numeric", "value": 2500, "tolerance": 0, "unit": "ms"}},
                    },
                    {
                        "item_type": "debug",
                        "title": "Bug: el LED parpadea rapidísimo con millis()",
                        "prompt": "Este código debería invertir el LED cada 1 s, pero pasado el primer segundo el LED queda parpadeando rapidísimo: if (millis() - ultimo >= 1000) { estado = !estado; digitalWrite(LED_PIN, estado); }  ¿Qué falta?",
                        "answer": "Falta actualizar la marca de tiempo: ultimo = millis(); dentro del if. Sin eso, la condición queda siempre verdadera y el LED se invierte en cada vuelta de loop().",
                        "hints": ["¿Qué variable debería avanzar cada vez que se cumple el intervalo?"],
                        "payload": {
                            "lab_link": "electronics:debug",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "ultimo = millis(); dentro del if",
                                    "delay(1000); dentro del if",
                                    "pinMode(LED_PIN, INPUT_PULLUP); en setup()",
                                ],
                                "correct": 0,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Tipo de dato para guardar tiempos de millis()",
                        "prompt": "¿Con qué tipo de dato se declaran las variables que guardan valores de millis()? Respondé con el nombre del tipo.",
                        "answer": "unsigned long. Un int se queda corto enseguida (en un Arduino Uno se desborda a los ~32 segundos) y rompe la temporización.",
                        "hints": ["Es un entero sin signo y más grande que int."],
                        "payload": {
                            "check": {"type": "text", "accept": ["unsigned long", "uint32_t", "unsigned long int"]},
                        },
                    },
                ],
            },
            {
                "slug": "e-i2c-sensores",
                "title": "7. Bus I2C: Sensor + OLED (Estación v1)",
                "level": 4,
                "order_index": 7,
                "summary": "Conectar múltiples dispositivos con solo 2 cables (SDA/SCL) en tu Estación Meteorológica v1.",
                "prerequisites": ["e-millis-multitarea"],
                "metadata": {"section": "Sensores e IoT", "lab_tab": "projects", "est_minutes": 30},
                "items": [
                    {
                        "item_type": "recall",
                        "title": "Cómo comparten cables varios dispositivos I2C",
                        "prompt": "¿Cuántos cables de datos usa I2C, cómo se llaman y cómo distingue el ESP32 entre un sensor BME280 y una pantalla OLED en los mismos pines?",
                        "answer": "Usa 2 líneas: SDA (datos) y SCL (reloj) — en ESP32 por defecto GPIO 21 y 22; en Arduino Uno A4 y A5. Cada dispositivo tiene una dirección hexadecimal única (ej. OLED 0x3C, sensor 0x76).",
                        "hints": ["Si no responde un módulo, corré primero un 'I2C Scanner' para ver su dirección."],
                        "payload": {
                            "lab_link": "electronics:pinout",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "2 líneas por cada dispositivo (TX y RX); se distinguen por el pin al que van",
                                    "2 líneas compartidas (SDA y SCL); cada dispositivo tiene una dirección única",
                                    "1 sola línea (DATA); se distinguen por el orden en que se conectan",
                                ],
                                "correct": 1,
                            },
                        },
                    },
                    {
                        "item_type": "project_step",
                        "title": "Estación Meteorológica v1: Leer DHT22/BME280 y mostrar en OLED",
                        "prompt": "En el Laboratorio de Electrónica → Proyectos, completá la Iteración 2: leé temperatura/humedad cada 2s (usando millis()) y mostrálos en Serial Monitor y OLED I2C.",
                        "answer": "Validá primero en Wokwi que el I2C Scanner detecte la dirección antes de debuggear la librería de pantalla.",
                        "hints": ["Recordá unir todas las tierras (GND) en común."],
                        "payload": {"lab_link": "electronics:projects"},
                    },
                    {
                        "item_type": "recall",
                        "title": "Pines I2C por defecto en el ESP32",
                        "prompt": "¿Qué GPIO usa el ESP32 por defecto para SDA y SCL?",
                        "answer": "SDA = GPIO 21 y SCL = GPIO 22. (En un Arduino Uno son A4 y A5.)",
                        "hints": ["Son dos GPIO consecutivos; SDA va en el más bajo."],
                        "payload": {
                            "lab_link": "electronics:pinout",
                            "check": {
                                "type": "choice",
                                "options": [
                                    "SDA = GPIO 22 y SCL = GPIO 21",
                                    "SDA = GPIO 21 y SCL = GPIO 22",
                                    "SDA = GPIO 34 y SCL = GPIO 35",
                                ],
                                "correct": 1,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Puesta en marcha de un módulo I2C",
                        "prompt": "Ordená los pasos para poner en marcha una pantalla OLED I2C nueva.",
                        "answer": "Primero el cableado (VCC, GND, SDA, SCL), después el I2C Scanner para confirmar que la placa ve el módulo y en qué dirección, y recién al final el código de la pantalla con esa dirección.",
                        "hints": ["El scanner va antes que cualquier librería."],
                        "payload": {
                            "lab_link": "electronics:projects",
                            "check": {
                                "type": "order",
                                "lines": [
                                    "Cableá VCC→3.3V, GND→GND, SDA→GPIO 21 y SCL→GPIO 22",
                                    "Cargá y ejecutá el I2C Scanner",
                                    "Leé en el Monitor Serial la dirección detectada (ej. 0x3C)",
                                    "Cargá el código de la pantalla usando esa dirección",
                                ],
                            },
                        },
                    },
                    {
                        "item_type": "debug",
                        "title": "Bug: OLED en negro con el scanner funcionando",
                        "prompt": "El I2C Scanner informa un dispositivo en 0x3C, pero tu sketch inicializa la pantalla en 0x3D y queda en negro. ¿Qué corregís?",
                        "answer": "La dirección en el código: tiene que ser 0x3C, la que detectó el scanner. Si el scanner ve el módulo, el cableado y la alimentación ya están bien.",
                        "hints": ["El scanner ya descartó los problemas de hardware."],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": [
                                    "El cableado: intercambiar SDA y SCL",
                                    "La alimentación: pasar de 3.3 V a 5 V",
                                    "La dirección en el código: usar 0x3C",
                                ],
                                "correct": 2,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Dirección I2C típica de una OLED SSD1306",
                        "prompt": "¿Cuál es la dirección I2C más habitual de una pantalla OLED SSD1306? Respondé en hexadecimal (formato 0x..).",
                        "answer": "0x3C. Algunos módulos vienen en 0x3D; por eso conviene confirmarlo con el I2C Scanner.",
                        "hints": ["Empieza con 0x3."],
                        "payload": {"check": {"type": "text", "accept": ["0x3C", "3C"]}},
                    },
                ],
            },
            {
                "slug": "e-esp32-wifi-iot",
                "title": "8. ESP32 Wi-Fi e IoT (Estación v2)",
                "level": 4,
                "order_index": 8,
                "summary": "Conectar el ESP32 a tu Wi-Fi local para publicar lecturas en una página web o alerta automática.",
                "prerequisites": ["e-i2c-sensores"],
                "metadata": {"section": "Sensores e IoT", "lab_tab": "projects", "est_minutes": 30},
                "items": [
                    {
                        "item_type": "recall",
                        "title": "Flujo básico para conectar un ESP32 a Wi-Fi",
                        "prompt": "Ordená los pasos básicos en código para conectar un ESP32 en modo estación (WIFI_STA) y saber su IP.",
                        "answer": "1) WiFi.mode(WIFI_STA); WiFi.begin(ssid, password); 2) Esperar en bucle mientras WiFi.status() != WL_CONNECTED (con timeout); 3) Imprimir WiFi.localIP() por Serial.",
                        "hints": ["Un timeout evita que tu placa quede colgada si se cae el router."],
                        "payload": {
                            "check": {
                                "type": "order",
                                "lines": [
                                    "WiFi.mode(WIFI_STA);",
                                    "WiFi.begin(ssid, password);",
                                    "Esperar mientras WiFi.status() != WL_CONNECTED (con timeout)",
                                    "Serial.println(WiFi.localIP());",
                                ],
                            },
                        },
                    },
                    {
                        "item_type": "project_step",
                        "title": "Reto Abierto (Nivel 3): Monitor Ambiental Wi-Fi con Alerta",
                        "prompt": "Extendé tu Estación Meteorológica v1 para que el ESP32 sirva una página web local con temperatura/humedad y encienda un LED o buzzer cuando la temperatura supere un umbral elegido por vos.",
                        "answer": "Checklist de ingeniería: alimentación estable, código sin delay() bloqueante, manejo de reconexión Wi-Fi y prueba real con datos en vivo.",
                        "hints": ["Podés simular Wi-Fi en Wokwi con la red 'Wokwi-GUEST' antes de subirlo a tu ESP32 físico."],
                        "payload": {"lab_link": "electronics:projects"},
                    },
                    {
                        "item_type": "recall",
                        "title": "Banda Wi-Fi que soporta el ESP32 clásico",
                        "prompt": "¿En qué banda de frecuencia Wi-Fi puede conectarse un ESP32 clásico? Respondé solo con el número en GHz.",
                        "answer": "2.4 GHz. No ve las redes de 5 GHz: es una causa muy común de que 'no conecte' aunque la contraseña esté bien.",
                        "hints": ["Es la banda más vieja y de mayor alcance."],
                        "payload": {"check": {"type": "numeric", "value": 2.4, "tolerance": 0.01, "unit": "GHz"}},
                    },
                    {
                        "item_type": "debug",
                        "title": "Bug: la placa queda colgada cuando no hay Wi-Fi",
                        "prompt": "Tu setup() espera así: while (WiFi.status() != WL_CONNECTED) { delay(500); }  Un día el router está apagado. ¿Qué pasa y cómo se arregla?",
                        "answer": "Queda atrapada para siempre en el while y nunca llega a loop(). Se arregla agregando un timeout (por ejemplo, salir del bucle a los 15 segundos) para poder reintentar o seguir sin red.",
                        "hints": ["¿Cuándo termina ese while si la condición nunca cambia?"],
                        "payload": {
                            "check": {
                                "type": "choice",
                                "options": [
                                    "Se conecta sola a otra red abierta; no hay que cambiar nada",
                                    "Queda atrapada para siempre en el while; hay que agregar un timeout (ej. 15 s)",
                                    "Se reinicia sola a los 2 s; hay que sacar el delay(500)",
                                ],
                                "correct": 1,
                            },
                        },
                    },
                    {
                        "item_type": "recall",
                        "title": "Función para conocer la IP del ESP32",
                        "prompt": "Una vez conectado en modo WIFI_STA, ¿qué función devuelve la IP local del ESP32? Respondé con el nombre de la función.",
                        "answer": "WiFi.localIP(). Se imprime por Serial para saber a qué dirección entrar desde el navegador.",
                        "hints": ["Pertenece al objeto WiFi."],
                        "payload": {"check": {"type": "text", "accept": ["WiFi.localIP()", "localIP()"]}},
                    },
                ],
            },
        ],
    },
    MATH_DOMAIN,
    PHYSICS_DOMAIN,
    CLYRP_DOMAIN,
]

# Built-in nodes retired when a built-in curriculum is replaced from scratch.
RETIRED_SEED_NODE_SLUGS: dict[str, tuple[str, ...]] = {
    "matematicas": RETIRED_MATH_NODE_SLUGS,
}

# Built-in cards whose title changed. Titles are the key used to sync content into
# existing databases, so renames are applied first to keep each card's progress.
SEED_TITLE_RENAMES: dict[str, str] = {
    "Proyecto v1: LED parpadeante SOS en Wokwi → Protoboard": "Proyecto v1: LED parpadeante SOS en el simulador → Protoboard",
    "Práctica en Math Lab: Fracciones": "Práctica en el Laboratorio de Matemáticas: Fracciones",
    "Práctica en Math Lab: Enteros y orden de operaciones": "Práctica en el Laboratorio de Matemáticas: Enteros y orden de operaciones",
    "Práctica en Math Lab: Potencias y notación científica": "Práctica en el Laboratorio de Matemáticas: Exponentes y potencias de 10",
    "Convertir una tasa bianual (+21% cada 2 años) a tasa anual": "Convertir una tasa bienal (+21% cada 2 años) a tasa anual",
    "Fórmula explícita de una sucesión geométrica (duplicación)": "Fórmula explícita de una sucesión geométrica (triplicación)",
    "Hallar la distancia focal c de una elipse": "Hallar la distancia c del centro a cada foco de una elipse",
    "División de 2 dígitos por 2 dígitos con resto": "División de 3 dígitos por 2 dígitos con resto",
}
