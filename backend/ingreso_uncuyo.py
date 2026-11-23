"""The 2027 entrance course (Curso de Ingreso) of the UNCuyo Engineering School, mapped onto the app.

Each subject lists its official units in the order of the syllabus, and each unit the app
topics (node slugs) that cover it. Topics that are not in the database yet are skipped, so
the map can name topics before their content exists. Anything in a subject's discipline that
is not listed here is outside the entrance syllabus (a prerequisite refresher or material for
later in the degree).
"""

from __future__ import annotations

from typing import Any

from backend import exercise_store
from backend.db import Database

COURSE = {
    "title": "Ingreso a Ingeniería · UNCuyo 2027",
    "pass_mark": 60,
    "summary": (
        "Tres módulos con examen presencial: Matemática, Física y Comprensión Lectora y Resolución de "
        "Problemas. Cada uno se aprueba con 60 sobre 100."
    ),
}

SUBJECTS: list[dict[str, Any]] = [
    {
        "key": "matematica",
        "name": "Matemática",
        "domain": "matematicas",
        "exam": "Dos parciales (o la Prueba General de Conocimientos) con 60 % para aprobar. Se valora el procedimiento, no solo el resultado.",
        "units": [
            {"title": "Unidad 0 · Teoría de conjuntos", "topics": ["al-teoria-conjuntos"]},
            {
                "title": "Unidad 1 · Números reales y radicales",
                "topics": [
                    "al-conjuntos-intervalos",
                    "al-reales-propiedades-combinados",
                    "al-irracionales",
                    "p-raices-notacion",
                    "al-exponentes-radicales",
                    "al-radicales-operaciones",
                    "p-ecuaciones-un-paso",
                    "al-ecuaciones-formulas",
                ],
            },
            {
                "title": "Unidad 2 · Geometría elemental y trigonometría básica",
                "topics": [
                    "g-angulos-rectas",
                    "g-poligonos-cuadrilateros",
                    "p-razones-tasas",
                    "p-porcentajes",
                    "g-semejanza",
                    "p-medicion-geometria",
                    "g-circulos-arcos",
                    "g-geometria-solida",
                    "g-pitagoras-especiales",
                    "g-trigonometria",
                ],
            },
            {
                "title": "Unidad 3 · Ecuaciones, inecuaciones, recta y sistemas",
                "topics": [
                    "al-parabolas-formula",
                    "p-desigualdades",
                    "a2-inecuaciones-avanzadas",
                    "al-valor-absoluto-partes",
                    "al-modulo-ecuaciones-inecuaciones",
                    "a2-ecuaciones-avanzadas",
                    "g-analitica-plano",
                    "p-plano-rectas",
                    "al-formas-lineales",
                    "p-sistemas-ecuaciones",
                    "al-sel-metodos-clasificacion",
                ],
            },
            {
                "title": "Unidad 4 · Polinomios y expresiones racionales",
                "topics": [
                    "al-polinomios-binomios",
                    "a2-polinomios-factorizacion",
                    "a2-division-polinomios",
                    "a2-casos-factoreo",
                    "al-factorizar-cuadraticas",
                    "a2-expresiones-racionales",
                ],
            },
            {
                "title": "Unidad 5 · Funciones",
                "topics": [
                    "p-funciones",
                    "al-dominio-rango",
                    "a2-estudio-funciones",
                    "al-cuadratica-formas",
                    "a2-transformaciones-funciones",
                    "a2-graficas-polinomios",
                ],
            },
            {
                "title": "Unidad 6 · Logaritmos y exponenciales",
                "topics": [
                    "al-exponenciales",
                    "a2-logaritmos",
                    "a2-ecuaciones-exponenciales-logaritmicas",
                    "a2-graficas-exp-log",
                ],
            },
            {
                "title": "Unidad 7 · Trigonometría",
                "topics": [
                    "t-sistemas-medicion",
                    "a2-circulo-unitario-ondas",
                    "t-reciprocas-referencia",
                    "t-relaciones-angulos",
                    "t-leyes-senos-cosenos",
                    "t-identidades-angulo-doble",
                    "t-ecuaciones-trigonometricas",
                ],
            },
        ],
    },
    {
        "key": "fisica",
        "name": "Física",
        "domain": "fisica",
        "exam": "Dos parciales y un examen global con 60 % para aprobar. Se usa g = 9,8 m/s², cifras significativas y unidades técnicas.",
        "units": [
            {
                "title": "Unidad 1 · Sistemas de unidades",
                "topics": ["f-intro-fisica", "f-sistemas-unidades", "f-cifras-significativas", "f-analisis-dimensional"],
            },
            {"title": "Unidad 2 · Magnitudes vectoriales", "topics": ["f-magnitudes-vectores", "f-vectores-operaciones"]},
            {
                "title": "Unidad 3 · Cinemática en una dirección",
                "topics": ["f-cinematica", "f-mru-encuentro", "f-mruv-graficas", "f-caida-libre-tiro-vertical"],
            },
            {
                "title": "Unidad 4 · Estática",
                "topics": ["f-estatica-concurrentes", "f-momento-cupla-vinculos", "f-estatica"],
            },
            {
                "title": "Unidad 5 · Dinámica",
                "topics": ["f-leyes-newton", "f-dcl-rozamiento-plano", "f-cuerpos-vinculados"],
            },
        ],
    },
    {
        "key": "clyrp",
        "name": "Comprensión Lectora y Resolución de Problemas",
        "domain": "comprension-problemas",
        "exam": "Un examen global presencial con 60 % para aprobar: textos científicos con preguntas, lógica, tablas y problemas.",
        "units": [
            {
                "title": "Unidad 1 · El lenguaje de las ciencias exactas",
                "topics": ["cl-consignas-lectura", "cl-texto-cientifico", "cl-organizadores", "cl-lenguaje-simbolico"],
            },
            {
                "title": "Unidad 2 · Lógica, cuadros, tablas y gráficos",
                "topics": ["cl-logica-enunciados", "cl-razonamiento-logico", "cl-tablas-graficos"],
            },
            {
                "title": "Unidad 3 · Estrategias de resolución de problemas",
                "topics": ["cl-estrategias-polya", "cl-porcentajes-fracciones", "cl-edades-sistemas", "cl-geometria-problemas"],
            },
        ],
    },
]


def program_slugs(subject_key: str | None = None) -> set[str]:
    """Every topic slug in the syllabus (of one subject, or of all of them)."""
    return {
        slug
        for subject in SUBJECTS
        if subject_key in (None, subject["key"])
        for unit in subject["units"]
        for slug in unit["topics"]
    }


def overview(db: Database) -> dict[str, Any]:
    """The syllabus with the learner's progress on every topic it maps to."""
    subjects = []
    for subject in SUBJECTS:
        try:
            roadmap = db.get_roadmap(subject["domain"])
            exercises = exercise_store.domain_exercises(db, subject["domain"])
        except KeyError:
            continue  # discipline not installed in this database
        nodes = {n["slug"]: n for n in roadmap["nodes"]}
        exercise_topics = {t["slug"]: t for t in exercises["topics"]}
        units = []
        for unit in subject["units"]:
            topics = []
            for slug in unit["topics"]:
                node = nodes.get(slug)
                if node is None:
                    continue
                ex_topic = exercise_topics.get(slug)
                ex_items = ex_topic["exercises"] if ex_topic else []
                topics.append(
                    {
                        "node_id": node["id"],
                        "slug": slug,
                        "title": node["title"],
                        "status": node["status"],
                        "lesson_completed": node["lesson_completed"],
                        "practiced_pct": node["practiced_pct"],
                        "mastery_pct": node["mastery_pct"],
                        "due_count": node["due_count"],
                        "cards": node["items"] if isinstance(node["items"], int) else len(node["items"]),
                        "exercises_total": len(ex_items),
                        "exercises_solved": sum(1 for e in ex_items if e["status"]["solved"]),
                        "exercises_official": sum(1 for e in ex_items if e.get("source")),
                    }
                )
            if topics:
                done = sum(1 for t in topics if t["lesson_completed"])
                units.append(
                    {
                        "title": unit["title"],
                        "topics": topics,
                        "lessons_done": done,
                        "progress_pct": round(sum(_topic_progress(t) for t in topics) / len(topics)),
                    }
                )
        listed = {t["slug"] for u in units for t in u["topics"]}
        all_topics = [t for u in units for t in u["topics"]]
        next_topic = next((t for t in all_topics if not t["lesson_completed"]), None) or next(
            (t for t in all_topics if t["exercises_solved"] < t["exercises_total"]), None
        )
        subjects.append(
            {
                "key": subject["key"],
                "name": subject["name"],
                "domain": roadmap["domain"]["slug"],
                "lab_type": roadmap["domain"].get("lab_type"),
                "exam": subject["exam"],
                "units": units,
                "topics_total": len(all_topics),
                "lessons_done": sum(1 for t in all_topics if t["lesson_completed"]),
                "exercises_total": sum(t["exercises_total"] for t in all_topics),
                "exercises_solved": sum(t["exercises_solved"] for t in all_topics),
                "exercises_official": sum(t["exercises_official"] for t in all_topics),
                "progress_pct": round(sum(_topic_progress(t) for t in all_topics) / len(all_topics)) if all_topics else 0,
                "outside_count": sum(1 for slug in nodes if slug not in listed),
                "next_topic": next_topic,
            }
        )
    return {**COURSE, "subjects": subjects}


def _topic_progress(topic: dict[str, Any]) -> float:
    """0–100 for one topic: a third each for the lesson, the review cards and the exercises."""
    lesson = 100 if topic["lesson_completed"] else 0
    cards = topic["practiced_pct"]
    exercises = 100 * topic["exercises_solved"] / topic["exercises_total"] if topic["exercises_total"] else cards
    return (lesson + cards + exercises) / 3
