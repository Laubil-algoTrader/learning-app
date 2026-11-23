"""Ejercicios del material oficial del ingreso 2027 (UNCuyo), Matemática: TP0 a TP3.

Fuente: "Material ingreso 2027" — TP N°0 (Teoría de conjuntos), TP N°1 (Números reales),
TP N°2 (Geometría elemental) y TP N°3 (Ecuaciones e inecuaciones, recta y SEL).
Ningún TP trae respuestas: todas se resolvieron y verificaron con Python (math/fractions).
"""

from __future__ import annotations

EXERCISES: list[dict] = [
    # ============================ TP0 · TEORÍA DE CONJUNTOS ============================
    {
        "id": "al-teoria-conjuntos-tp0-6",
        "node": "al-teoria-conjuntos",
        "kind": "problem",
        "level": 1,
        "source": "Matemática · TP0, ej. 6 (a, e, i)",
        "title": "Operaciones entre conjuntos por extensión",
        "statement": "Dados los conjuntos `U = {x ∈ ℕ / x < 9}`, `A = {x ∈ ℕ / 2 ≤ x ≤ 8}`, `B = {1, 2, 3, 4}` y `C = {3, 4, 5, 6}`, representalos en un diagrama de Venn y escribí por extensión los conjuntos pedidos.",
        "parts": [
            {
                "prompt": "a) `A ∪ B`",
                "check": {"type": "choice", "options": ["{1, 2, 3, 4, 5, 6, 7, 8}", "{2, 3, 4}", "{1, 2, 3, 4, 5, 6, 7, 8, 9}", "{2, 3, 4, 5, 6, 7, 8}"], "correct": 0},
                "answer": "{1, 2, 3, 4, 5, 6, 7, 8} (es todo U)",
            },
            {
                "prompt": "b) `A − B`",
                "check": {"type": "choice", "options": ["{5, 6, 7, 8}", "{1}", "{1, 5, 6, 7, 8}", "{2, 3, 4}"], "correct": 0},
                "answer": "{5, 6, 7, 8}",
            },
            {
                "prompt": "c) `A − C`",
                "check": {"type": "choice", "options": ["{2, 7, 8}", "{7, 8}", "{3, 4, 5, 6}", "{1, 2, 7, 8}"], "correct": 0},
                "answer": "{2, 7, 8}",
            },
        ],
        "hints": [
            "Primero escribí U y A por extensión. En el material ℕ = {1, 2, 3, …} (el 0 aparece aparte como ℕ₀).",
            "`A − B` son los elementos de A que NO están en B: la resta saca solo lo que está en A.",
        ],
        "solution": [
            "Por extensión: `U = {1, 2, 3, 4, 5, 6, 7, 8}` y `A = {2, 3, 4, 5, 6, 7, 8}`.",
            "**a)** `A ∪ B` junta los elementos de los dos sin repetir: A aporta del 2 al 8 y B agrega el 1. `A ∪ B = {1, 2, 3, 4, 5, 6, 7, 8} = U`.",
            "**b)** `A − B`: de A sacamos los que también están en B (2, 3 y 4). Queda `A − B = {5, 6, 7, 8}`. El 1 no aparece porque no está en A.",
            "**c)** `A − C`: de A sacamos 3, 4, 5 y 6. Queda `A − C = {2, 7, 8}`.",
            "En el diagrama de Venn: el 1 va en B fuera de A; el 2 en A ∩ B fuera de C; 3 y 4 en la zona común de los tres; 5 y 6 en A ∩ C fuera de B; 7 y 8 solo en A.",
        ],
    },
    {
        "id": "al-teoria-conjuntos-tp0-7",
        "node": "al-teoria-conjuntos",
        "kind": "problem",
        "level": 1,
        "source": "Matemática · TP0, ej. 7",
        "title": "Unión e intersección de tres conjuntos",
        "statement": "Dados los conjuntos `A = {x ∈ ℕ / x < 6}`, `B = {x ∈ ℕ / x es impar ∧ 3 ≤ x ≤ 9}`, `C = {x ∈ ℕ / 3 < x ≤ 8}` y `U = {x ∈ ℕ / x es un dígito}`:",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la escritura de B por extensión?",
                "check": {"type": "choice", "options": ["{3, 5, 7, 9}", "{3, 5, 7}", "{1, 3, 5, 7, 9}", "{5, 7, 9}"], "correct": 0},
                "answer": "{3, 5, 7, 9}",
            },
            {
                "prompt": "b) `A ∪ B ∪ C`",
                "check": {"type": "choice", "options": ["{1, 2, 3, 4, 5, 6, 7, 8, 9}", "{1, 2, 3, 4, 5, 6, 7, 8}", "{3, 4, 5, 7}", "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}"], "correct": 0},
                "answer": "{1, 2, 3, 4, 5, 6, 7, 8, 9}",
            },
            {
                "prompt": "c) `A ∩ B ∩ C`",
                "check": {"type": "choice", "options": ["{5}", "∅", "{3, 5}", "{4, 5}"], "correct": 0},
                "answer": "{5}",
            },
        ],
        "hints": [
            "Mirá bien los extremos: `3 ≤ x ≤ 9` incluye al 3 y al 9; `3 < x ≤ 8` no incluye al 3.",
            "Para la intersección de tres conjuntos, buscá los elementos que aparecen en los TRES a la vez.",
        ],
        "solution": [
            "`A = {1, 2, 3, 4, 5}` (naturales menores que 6).",
            "`B = {3, 5, 7, 9}`: impares entre 3 y 9, con los dos extremos incluidos.",
            "`C = {4, 5, 6, 7, 8}`: el 3 queda afuera (desigualdad estricta) y el 8 entra.",
            "**b)** La unión junta todo: del 1 al 5 por A, 7 y 9 por B, 6 y 8 por C. `A ∪ B ∪ C = {1, 2, 3, 4, 5, 6, 7, 8, 9}` (coincide con U, porque con ℕ que arranca en 1 los dígitos son 1 a 9).",
            "**c)** `A ∩ B = {3, 5}`; de esos, solo el 5 está en C. `A ∩ B ∩ C = {5}`.",
        ],
    },
    {
        "id": "al-teoria-conjuntos-tp0-5",
        "node": "al-teoria-conjuntos",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP0, ej. 5 (d, e, i)",
        "title": "Leer un diagrama de Venn: ∈, ∉, ⊂, ⊄ y ⊃",
        "statement": "En el diagrama del ejercicio hay, dentro del universo U, cuatro conjuntos P, Q, S y R. P y Q son dos círculos que se cortan. S es un óvalo que corta a P y a Q, y su único elemento es **a**, que está en la zona común de P y Q. R es un círculo que corta a Q, pero en la zona común de Q y R no hay ningún elemento. Los elementos de cada región son:\n| Región | Elementos |\n|---|---|\n| solo en P | w, i (i queda fuera de S) |\n| en P y en Q, fuera de S | b |\n| en P, en Q y en S | a |\n| solo en Q | v, n (n queda fuera de R) |\n| solo en R | m |\nCompletá con el símbolo que corresponda.",
        "parts": [
            {
                "prompt": "a) `n ___ R`",
                "check": {"type": "choice", "options": ["∈", "∉", "⊂"], "correct": 1},
                "answer": "∉ (n está en Q pero fuera de R)",
            },
            {
                "prompt": "b) `P ___ S`",
                "check": {"type": "choice", "options": ["⊂", "⊃", "∈"], "correct": 1},
                "answer": "⊃ (P contiene a S = {a})",
            },
            {
                "prompt": "c) `{a, i} ___ S`",
                "check": {"type": "choice", "options": ["⊂", "⊄", "∈"], "correct": 1},
                "answer": "⊄ (i no pertenece a S)",
            },
        ],
        "hints": [
            "Antes de contestar, escribí cada conjunto por extensión a partir de la tabla.",
            "∈ y ∉ relacionan un ELEMENTO con un conjunto; ⊂, ⊄ y ⊃ relacionan dos CONJUNTOS.",
        ],
        "solution": [
            "Por extensión: `P = {w, i, b, a}`, `Q = {b, a, v, n}`, `S = {a}`, `R = {m}`.",
            "**a)** n es un elemento y no está en R (está en Q, del lado de afuera de R): `n ∉ R`.",
            "**b)** Todo elemento de S (solo a) está en P, así que S ⊂ P, que es lo mismo que `P ⊃ S`. No vale P ⊂ S porque w ∉ S, y ∈ no corresponde porque P es un conjunto, no un elemento de S.",
            "**c)** Para que `{a, i} ⊂ S` haría falta que a e i estén en S; a sí está pero i no. Entonces `{a, i} ⊄ S`.",
            "Ojo con la lectura del dibujo: i está dentro de P pero a la izquierda del óvalo S, y n está dentro de Q pero a la izquierda del círculo R.",
        ],
    },
    # ============================ TP1 · NÚMEROS REALES ============================
    {
        "id": "al-reales-propiedades-combinados-tp1-12a",
        "node": "al-reales-propiedades-combinados",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP1, ej. 12 (a, b, c)",
        "title": "Combinados con periódicos y raíces (1)",
        "statement": "Resolvé los siguientes ejercicios combinados (el símbolo ^ sobre una cifra indica que es el período: `0,5̂ = 0,555…`).\na) `[0,5̂ · √0,81 − (−1/2)²] : (1 − 1/2)²`\nb) `[√(0,64 : 4) − (1 − 3/2)⁻² · √(1 − 3/4) + 3/2]⁻¹`\nc) `√[(0,08̂ + 1,5̂ + 0,23̂) · 0,1]`",
        "parts": [
            {
                "prompt": "a) Resultado del inciso a). Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1",
            },
            {
                "prompt": "b) Resultado del inciso b). Respondé solo con el número.",
                "check": {"type": "numeric", "value": -10, "tolerance": 0, "unit": ""},
                "answer": "−10",
            },
            {
                "prompt": "c) Resultado del inciso c), como fracción irreducible o decimal con 3 cifras.",
                "check": {"type": "numeric", "value": 0.43333, "tolerance": 0.002, "unit": ""},
                "answer": "13/30 ≈ 0,433",
            },
        ],
        "hints": [
            "Pasá los periódicos a fracción: puro `0,5̂ = 5/9`; mixto `0,23̂ = (23 − 2)/90`.",
            "Un exponente negativo invierte la base: `(−1/2)⁻² = (−2)² = 4`.",
            "Resolvé primero lo de adentro de cada corchete y separá en términos antes de operar.",
        ],
        "solution": [
            "**a)** `0,5̂ = 5/9` y `√0,81 = 0,9 = 9/10`, así que `5/9 · 9/10 = 1/2`. Además `(−1/2)² = 1/4`. El corchete vale `1/2 − 1/4 = 1/4`.",
            "El divisor es `(1/2)² = 1/4`, entonces `1/4 : 1/4 = 1`.",
            "**b)** `0,64 : 4 = 0,16` y `√0,16 = 0,4`. `(1 − 3/2)⁻² = (−1/2)⁻² = 4` y `√(1 − 3/4) = √(1/4) = 1/2`, así que ese término vale `4 · 1/2 = 2`.",
            "El corchete queda `0,4 − 2 + 1,5 = −0,1` y `(−0,1)⁻¹ = 1/(−0,1) = −10`.",
            "**c)** `0,08̂ = 8/90 = 4/45`, `1,5̂ = 14/9`, `0,23̂ = 21/90 = 7/30`. Con denominador 90: `8/90 + 140/90 + 21/90 = 169/90`.",
            "Multiplicando por `0,1 = 1/10`: `169/900`, y `√(169/900) = 13/30 ≈ 0,433`.",
        ],
    },
    {
        "id": "al-reales-propiedades-combinados-tp1-12d",
        "node": "al-reales-propiedades-combinados",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP1, ej. 12 (d, e, f)",
        "title": "Combinados con periódicos y raíces (2)",
        "statement": "Resolvé los siguientes ejercicios combinados (^ indica el período).\nd) `(1/2 − 1)⁻² − (1,3̂)² − √(1 − 0,8̂)`\ne) `(∛0,027 − 0,3̂) : 0,05̂`\nf) `2⁻² · √1,44 + 2/3 − √(9/4) − √(1 : 36/25)`",
        "parts": [
            {
                "prompt": "a) Resultado de d), como fracción irreducible.",
                "check": {"type": "numeric", "value": 1.888889, "tolerance": 0.001, "unit": ""},
                "answer": "17/9",
            },
            {
                "prompt": "b) Resultado de e), como fracción irreducible.",
                "check": {"type": "numeric", "value": -0.6, "tolerance": 0.001, "unit": ""},
                "answer": "−3/5",
            },
            {
                "prompt": "c) Resultado de f), como fracción irreducible.",
                "check": {"type": "numeric", "value": -1.366667, "tolerance": 0.001, "unit": ""},
                "answer": "−41/30",
            },
        ],
        "hints": [
            "`1,3̂ = (13 − 1)/9 = 12/9 = 4/3`; `0,8̂ = 8/9`; `0,05̂ = 5/90 = 1/18`.",
            "`∛0,027 = 0,3` porque `0,3³ = 0,027`; no lo confundas con `0,3̂ = 1/3`.",
            "En f), `1 : 36/25 = 25/36`.",
        ],
        "solution": [
            "**d)** `(1/2 − 1)⁻² = (−1/2)⁻² = 4`; `(1,3̂)² = (4/3)² = 16/9`; `√(1 − 8/9) = √(1/9) = 1/3`.",
            "`4 − 16/9 − 1/3 = 36/9 − 16/9 − 3/9 = 17/9`.",
            "**e)** `∛0,027 − 0,3̂ = 3/10 − 1/3 = −1/30`. Dividido `0,05̂ = 1/18`: `−1/30 · 18 = −18/30 = −3/5`.",
            "**f)** `2⁻² · √1,44 = 1/4 · 1,2 = 0,3 = 3/10`; `√(9/4) = 3/2`; `√(1 : 36/25) = √(25/36) = 5/6`.",
            "`3/10 + 2/3 − 3/2 − 5/6`, con denominador 30: `(9 + 20 − 45 − 25)/30 = −41/30`.",
        ],
    },
    {
        "id": "p-ecuaciones-un-paso-tp1-15",
        "node": "p-ecuaciones-un-paso",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP1, ej. 15 (c, d, f)",
        "title": "Ecuaciones lineales con fracciones",
        "statement": "Resolvé las siguientes ecuaciones, si es posible.\nc) `x/3 + (x + 2)/5 + (x + 1)/4 = 3`\nd) `(x/4 + 3) · 2 = (5x/2 − 55) : 5`\nf) `x/5 − 2/3 + x = 0`",
        "parts": [
            {
                "prompt": "a) Solución de c). Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3",
            },
            {
                "prompt": "b) ¿Cuántas soluciones tiene d)?",
                "check": {"type": "choice", "options": ["Ninguna (S = ∅)", "Una sola: x = 0", "Infinitas (S = ℝ)", "Una sola: x = 17"], "correct": 0},
                "answer": "Ninguna (S = ∅)",
            },
            {
                "prompt": "c) Solución de f), como fracción irreducible.",
                "check": {"type": "numeric", "value": 0.555556, "tolerance": 0.001, "unit": ""},
                "answer": "5/9",
            },
        ],
        "hints": [
            "En c) multiplicá todo por el mcm de los denominadores (60) para sacar las fracciones.",
            "En d) distribuí: si al simplificar desaparece la x y queda una igualdad falsa, no hay solución.",
        ],
        "solution": [
            "**c)** Multiplicamos por 60: `20x + 12(x + 2) + 15(x + 1) = 180` → `20x + 12x + 24 + 15x + 15 = 180` → `47x = 141` → `x = 3`.",
            "Verificación: `3/3 + 5/5 + 4/4 = 1 + 1 + 1 = 3` ✓.",
            "**d)** Izquierda: `x/2 + 6`. Derecha: `(5x/2) : 5 − 55 : 5 = x/2 − 11`. Queda `x/2 + 6 = x/2 − 11`.",
            "Restando `x/2` a ambos lados: `6 = −11`, que es falso para todo x. La ecuación es incompatible: `S = ∅`.",
            "**f)** `x/5 + x = 2/3` → `6x/5 = 2/3` → `x = 2/3 · 5/6 = 10/18 = 5/9`.",
        ],
    },
    {
        "id": "p-ecuaciones-un-paso-tp1-16",
        "node": "p-ecuaciones-un-paso",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP1, ej. 16",
        "title": "Consecutivos y figuritas",
        "statement": "Planteá y resolvé:\na) La suma de tres números consecutivos es 24. ¿Cuáles son esos números?\nb) La suma de tres números pares consecutivos es igual a 300. ¿Cuáles son dichos números?\nc) Nicolás tiene el triple de figuritas que Rafael menos doscientas; Francisco tiene quinientas figuritas menos cuatro veces las figuritas de Rafael. Si dos de ellos tienen la misma cantidad de figuritas, ¿cuántas figuritas tiene cada uno?",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el menor de los tres consecutivos? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 7, "tolerance": 0, "unit": ""},
                "answer": "7 (los números son 7, 8 y 9)",
            },
            {
                "prompt": "b) ¿Cuál es el mayor de los tres pares consecutivos? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 102, "tolerance": 0, "unit": ""},
                "answer": "102 (los números son 98, 100 y 102)",
            },
            {
                "prompt": "c) ¿Cuántas figuritas tiene Rafael? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 100, "tolerance": 0, "unit": ""},
                "answer": "100 (y Nicolás y Francisco también tienen 100)",
            },
        ],
        "hints": [
            "Llamá n al primero: los consecutivos son n, n + 1, n + 2; los pares consecutivos, n, n + 2, n + 4.",
            "En c) llamá R a las figuritas de Rafael: N = 3R − 200 y F = 500 − 4R. Probá igualar de a dos.",
        ],
        "solution": [
            "**a)** `n + (n + 1) + (n + 2) = 24` → `3n + 3 = 24` → `n = 7`. Son 7, 8 y 9.",
            "**b)** `n + (n + 2) + (n + 4) = 300` → `3n + 6 = 300` → `n = 98`. Son 98, 100 y 102.",
            "**c)** Con R figuritas de Rafael: Nicolás `N = 3R − 200` y Francisco `F = 500 − 4R`.",
            "Si N = F: `3R − 200 = 500 − 4R` → `7R = 700` → `R = 100`; entonces `N = 100` y `F = 100`.",
            "Las otras parejas dan lo mismo: N = R → `2R = 200` → R = 100; F = R → `5R = 500` → R = 100. En todos los casos los tres tienen **100 figuritas**.",
        ],
    },
    {
        "id": "al-radicales-operaciones-tp1-17",
        "node": "al-radicales-operaciones",
        "kind": "problem",
        "level": 1,
        "source": "Matemática · TP1, ej. 17 (c, d, f)",
        "title": "Extraer factores fuera del radical",
        "statement": "Extraé todos los factores posibles fuera del radical (las letras representan números positivos).\nc) `∛56`\nd) `∛(m¹¹ n¹⁸)`\nf) `⁵√(128 · m¹²)`",
        "parts": [
            {
                "prompt": "a) `∛56` =",
                "check": {"type": "choice", "options": ["2∛7", "7∛2", "2∛14", "4∛7"], "correct": 0},
                "answer": "2∛7",
            },
            {
                "prompt": "b) `∛(m¹¹ n¹⁸)` =",
                "check": {"type": "choice", "options": ["m³ n⁶ ∛(m²)", "m³ n⁶ ∛m", "m⁸ n¹⁵ ∛(m³)", "m³ n⁵ ∛(m²)"], "correct": 0},
                "answer": "m³ n⁶ ∛(m²)",
            },
            {
                "prompt": "c) `⁵√(128 · m¹²)` =",
                "check": {"type": "choice", "options": ["2m² · ⁵√(4m²)", "2m² · ⁵√(2m²)", "4m² · ⁵√(4m²)", "2m³ · ⁵√4"], "correct": 0},
                "answer": "2m² · ⁵√(4m²)",
            },
        ],
        "hints": [
            "Factorizá en primos y dividí cada exponente por el índice: el cociente sale afuera y el resto queda adentro.",
            "Ejemplo: en `∛(m¹¹)`, 11 = 3 · 3 + 2, así que sale `m³` y queda `m²` adentro.",
        ],
        "solution": [
            "**c)** `56 = 2³ · 7`, así que `∛56 = ∛(2³) · ∛7 = 2∛7`.",
            "**d)** `11 : 3` da cociente 3 y resto 2 → sale `m³` y queda `m²`. `18 : 3` da 6 exacto → sale `n⁶`. Resultado: `m³ n⁶ ∛(m²)`.",
            "**f)** `128 = 2⁷` y `7 : 5` da cociente 1 y resto 2 → sale `2`, queda `2² = 4`. `12 : 5` da cociente 2 y resto 2 → sale `m²`, queda `m²`.",
            "Resultado: `⁵√(128 m¹²) = 2m² · ⁵√(4m²)`.",
        ],
    },
    {
        "id": "al-radicales-operaciones-tp1-18",
        "node": "al-radicales-operaciones",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP1, ej. 18 (b, d, e)",
        "title": "Sumas algebraicas de radicales",
        "statement": "Resolvé las siguientes sumas algebraicas.\nb) `⁴√9 − 3 · ⁶√27 − √3/3`\nd) `√18 + √75 − √200 + √128 − √507`\ne) `∛40 − ⁴√162 + ∛625 + 2 · ⁴√32 − ∛320`",
        "parts": [
            {
                "prompt": "a) Resultado de b)",
                "check": {"type": "choice", "options": ["−7√3/3", "−8√3/3", "−2√3", "2√3/3"], "correct": 0},
                "answer": "−7√3/3",
            },
            {
                "prompt": "b) Resultado de d)",
                "check": {"type": "choice", "options": ["√2 − 8√3", "−√2 − 8√3", "√2 + 8√3", "−7√2 − 8√3"], "correct": 0},
                "answer": "√2 − 8√3",
            },
            {
                "prompt": "c) Resultado de e)",
                "check": {"type": "choice", "options": ["3∛5 + ⁴√2", "3∛5 − ⁴√2", "∛5 + ⁴√2", "3∛5 + 5 · ⁴√2"], "correct": 0},
                "answer": "3∛5 + ⁴√2",
            },
        ],
        "hints": [
            "Solo se suman radicales SEMEJANTES (mismo índice y mismo radicando): primero extraé factores.",
            "Simplificá índices: `⁴√9 = ⁴√(3²) = √3` y `⁶√27 = ⁶√(3³) = √3`.",
        ],
        "solution": [
            "**b)** `⁴√9 = √3` y `⁶√27 = √3`. Queda `√3 − 3√3 − (1/3)√3 = (1 − 3 − 1/3)√3 = −(7/3)√3`.",
            "**d)** `√18 = 3√2`, `√75 = 5√3`, `√200 = 10√2`, `√128 = 8√2`, `√507 = √(169 · 3) = 13√3`.",
            "Agrupando: `(3 − 10 + 8)√2 + (5 − 13)√3 = √2 − 8√3`.",
            "**e)** `∛40 = 2∛5`, `⁴√162 = ⁴√(81 · 2) = 3 · ⁴√2`, `∛625 = ∛(125 · 5) = 5∛5`, `2 · ⁴√32 = 2 · ⁴√(16 · 2) = 4 · ⁴√2`, `∛320 = ∛(64 · 5) = 4∛5`.",
            "Agrupando: `(2 + 5 − 4)∛5 + (−3 + 4) · ⁴√2 = 3∛5 + ⁴√2`.",
        ],
    },
    {
        "id": "al-radicales-operaciones-tp1-20",
        "node": "al-radicales-operaciones",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP1, ej. 20 (c, d, f)",
        "title": "Multiplicar y dividir radicales de distinto índice",
        "statement": "Resolvé las siguientes multiplicaciones y divisiones (las letras representan números positivos).\nc) `⁴√8 : ∛2`\nd) `∛(2ax²) : √(3ax)`\nf) `∛(2m²) · √(2m) · ⁶√(4m⁵)`",
        "parts": [
            {
                "prompt": "a) Resultado de c)",
                "check": {"type": "choice", "options": ["¹²√32", "¹²√16", "⁴√2", "√2"], "correct": 0},
                "answer": "¹²√32",
            },
            {
                "prompt": "b) Resultado de d)",
                "check": {"type": "choice", "options": ["⁶√(4x/(27a))", "⁶√(2x/(3a))", "⁶√(4x³/(27a))", "∛(2x/3)"], "correct": 0},
                "answer": "⁶√(4x/(27a))",
            },
            {
                "prompt": "c) Resultado de f)",
                "check": {"type": "choice", "options": ["2m² · ⁶√2", "2m · ⁶√2", "4m² · ⁶√2", "2m² · ∛2"], "correct": 0},
                "answer": "2m² · ⁶√2",
            },
        ],
        "hints": [
            "Llevá todos los radicales a un índice común (el mcm de los índices): `ⁿ√a = ⁿᵏ√(aᵏ)`.",
            "Con el mismo índice, multiplicá o dividí los radicandos y después extraé lo que se pueda.",
        ],
        "solution": [
            "**c)** mcm(4, 3) = 12. `⁴√8 = ¹²√(8³) = ¹²√512` y `∛2 = ¹²√(2⁴) = ¹²√16`. Cociente: `¹²√(512/16) = ¹²√32`.",
            "**d)** mcm(3, 2) = 6. `∛(2ax²) = ⁶√(4a²x⁴)` y `√(3ax) = ⁶√(27a³x³)`.",
            "Cociente: `⁶√(4a²x⁴ / (27a³x³)) = ⁶√(4x/(27a))`.",
            "**f)** mcm(3, 2, 6) = 6. `∛(2m²) = ⁶√(4m⁴)`, `√(2m) = ⁶√(8m³)` y `⁶√(4m⁵)` queda igual.",
            "Producto: `⁶√(4 · 8 · 4 · m⁴⁺³⁺⁵) = ⁶√(128 m¹²)`. Como `128 = 2⁶ · 2` y `m¹² = (m²)⁶`, resulta `2m² · ⁶√2`.",
        ],
    },
    {
        "id": "al-radicales-operaciones-tp1-21",
        "node": "al-radicales-operaciones",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP1, ej. 21 (a, b, d)",
        "title": "Combinados con radicales",
        "statement": "Resolvé los siguientes ejercicios combinados.\na) `(3 · √20 − 2 · √5) · √5`\nb) `(3 · √12 + 12 · √75) : √3`\nd) `(2 + √3)³`",
        "parts": [
            {
                "prompt": "a) Resultado de a). Respondé solo con el número.",
                "check": {"type": "numeric", "value": 20, "tolerance": 0, "unit": ""},
                "answer": "20",
            },
            {
                "prompt": "b) Resultado de b). Respondé solo con el número.",
                "check": {"type": "numeric", "value": 66, "tolerance": 0, "unit": ""},
                "answer": "66",
            },
            {
                "prompt": "c) Resultado de d)",
                "check": {"type": "choice", "options": ["26 + 15√3", "8 + 3√3", "11 + 6√3", "26 + 12√3"], "correct": 0},
                "answer": "26 + 15√3",
            },
        ],
        "hints": [
            "Extraé factores antes de operar: `√20 = 2√5`, `√12 = 2√3`, `√75 = 5√3`.",
            "Para el cubo de un binomio: `(a + b)³ = a³ + 3a²b + 3ab² + b³`.",
        ],
        "solution": [
            "**a)** `3√20 = 6√5`, así que el paréntesis vale `6√5 − 2√5 = 4√5`. Por `√5`: `4 · 5 = 20`.",
            "**b)** `3√12 = 6√3` y `12√75 = 60√3`. Suma: `66√3`. Dividido `√3`: `66`.",
            "**d)** Con a = 2 y b = √3: `a³ = 8`, `3a²b = 12√3`, `3ab² = 3 · 2 · 3 = 18`, `b³ = 3√3`.",
            "Sumando: `(8 + 18) + (12 + 3)√3 = 26 + 15√3`.",
            "Error típico: hacer `(2 + √3)³ = 8 + 3√3`, como si la potencia se distribuyera en la suma.",
        ],
    },
    {
        "id": "al-radicales-operaciones-tp1-22",
        "node": "al-radicales-operaciones",
        "kind": "problem",
        "level": 3,
        "source": "Matemática · TP1, ej. 22 (c, e, h)",
        "title": "Racionalizar denominadores",
        "statement": "Racionalizá los denominadores (a ≠ 0).\nc) `(√3 + 1)/(√3 − 1)`\ne) `5/(2√3 + 3√2)`\nh) `4/∛(16 · a²)`",
        "parts": [
            {
                "prompt": "a) Resultado de c)",
                "check": {"type": "choice", "options": ["2 + √3", "1 + √3", "2 − √3", "(4 + 2√3)/4"], "correct": 0},
                "answer": "2 + √3",
            },
            {
                "prompt": "b) Resultado de e)",
                "check": {"type": "choice", "options": ["(15√2 − 10√3)/6", "(10√3 − 15√2)/6", "(10√3 + 15√2)/30", "(2√3 − 3√2)/6"], "correct": 0},
                "answer": "(15√2 − 10√3)/6",
            },
            {
                "prompt": "c) Resultado de h)",
                "check": {"type": "choice", "options": ["∛(4a)/a", "∛(4a)/(2a)", "2∛(4a)/a", "4∛a/a"], "correct": 0},
                "answer": "∛(4a)/a",
            },
        ],
        "hints": [
            "Si el denominador es un binomio con raíces cuadradas, multiplicá por su conjugado: `(p + q)(p − q) = p² − q²`.",
            "En h) primero simplificá `∛(16a²) = 2∛(2a²)` y después multiplicá por lo que falta para completar un cubo.",
        ],
        "solution": [
            "**c)** Por el conjugado `√3 + 1`: numerador `(√3 + 1)² = 3 + 2√3 + 1 = 4 + 2√3`; denominador `3 − 1 = 2`. Resultado: `2 + √3`.",
            "**e)** Por el conjugado `2√3 − 3√2`: denominador `(2√3)² − (3√2)² = 12 − 18 = −6`; numerador `5(2√3 − 3√2) = 10√3 − 15√2`.",
            "Entonces `(10√3 − 15√2)/(−6) = (15√2 − 10√3)/6`.",
            "**h)** `∛(16a²) = ∛(8 · 2a²) = 2∛(2a²)`, así que la expresión es `2/∛(2a²)`.",
            "Multiplicamos arriba y abajo por `∛(4a)`: abajo `∛(8a³) = 2a`, arriba `2∛(4a)`. Resultado: `2∛(4a)/(2a) = ∛(4a)/a`.",
        ],
    },
]

# ============================ TP2 · GEOMETRÍA ELEMENTAL ============================
EXERCISES += [
    {
        "id": "p-razones-tasas-tp2-26a",
        "node": "p-razones-tasas",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP2, ej. 26 (a, b, c)",
        "title": "Proporciones con incógnita (1)",
        "statement": "Dadas las proporciones, calculá el valor de la incógnita.\na) `2(x + 2)/x = 0,5/1,2`\nb) `(8x − 10)/(13x − 2) = 2/3`\nc) `(5x + 2)/(3x + 25) = 1/2`",
        "parts": [
            {
                "prompt": "a) x en a), como fracción irreducible.",
                "check": {"type": "numeric", "value": -2.526316, "tolerance": 0.001, "unit": ""},
                "answer": "−48/19 ≈ −2,526",
            },
            {
                "prompt": "b) x en b). Respondé solo con el número.",
                "check": {"type": "numeric", "value": -13, "tolerance": 0, "unit": ""},
                "answer": "−13",
            },
            {
                "prompt": "c) x en c). Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3",
            },
        ],
        "hints": [
            "Propiedad fundamental: en una proporción, el producto de los extremos es igual al producto de los medios.",
            "Después de multiplicar en cruz queda una ecuación lineal; verificá que el denominador no se anule con el valor hallado.",
        ],
        "solution": [
            "**a)** `2(x + 2) · 1,2 = 0,5 · x` → `2,4x + 4,8 = 0,5x` → `1,9x = −4,8` → `x = −48/19 ≈ −2,53`.",
            "**b)** `3(8x − 10) = 2(13x − 2)` → `24x − 30 = 26x − 4` → `−2x = 26` → `x = −13`.",
            "Verificación b): `(−104 − 10)/(−169 − 2) = −114/−171 = 2/3` ✓.",
            "**c)** `2(5x + 2) = 1 · (3x + 25)` → `10x + 4 = 3x + 25` → `7x = 21` → `x = 3`.",
            "Verificación c): `17/34 = 1/2` ✓.",
        ],
    },
    {
        "id": "p-razones-tasas-tp2-26d",
        "node": "p-razones-tasas",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP2, ej. 26 (d, e, f)",
        "title": "Proporciones con incógnita (2)",
        "statement": "Dadas las proporciones, calculá el valor de la incógnita (^ indica el período).\nd) `(x + 4)/(0,3 − 2) = (x + 1)/(3 − 0,2)`\ne) `(x − 3)/(2x + 1) = −2/3`\nf) `1,3̂/(x − 0,3̂) = 2/(6x + 1)`",
        "parts": [
            {
                "prompt": "a) x en d), como fracción irreducible.",
                "check": {"type": "numeric", "value": -2.866667, "tolerance": 0.001, "unit": ""},
                "answer": "−43/15 ≈ −2,867",
            },
            {
                "prompt": "b) x en e). Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1",
            },
            {
                "prompt": "c) x en f), como fracción irreducible.",
                "check": {"type": "numeric", "value": -0.333333, "tolerance": 0.001, "unit": ""},
                "answer": "−1/3",
            },
        ],
        "hints": [
            "En d) hacé primero las cuentas de los denominadores: `0,3 − 2 = −1,7` y `3 − 0,2 = 2,8`.",
            "En f) pasá los periódicos a fracción: `1,3̂ = 4/3` y `0,3̂ = 1/3`.",
        ],
        "solution": [
            "**d)** `(x + 4)/(−1,7) = (x + 1)/2,8` → `2,8(x + 4) = −1,7(x + 1)` → `2,8x + 11,2 = −1,7x − 1,7`.",
            "`4,5x = −12,9` → `x = −12,9/4,5 = −43/15 ≈ −2,87`.",
            "**e)** `3(x − 3) = −2(2x + 1)` → `3x − 9 = −4x − 2` → `7x = 7` → `x = 1`. Verificación: `−2/3` ✓.",
            "**f)** `(4/3)/(x − 1/3) = 2/(6x + 1)` → `(4/3)(6x + 1) = 2(x − 1/3)` → `8x + 4/3 = 2x − 2/3` → `6x = −2` → `x = −1/3`.",
            "Verificación f): `(4/3)/(−2/3) = −2` y `2/(−2 + 1) = −2` ✓ (ningún denominador se anula).",
        ],
    },
    {
        "id": "p-razones-tasas-tp2-28-31",
        "node": "p-razones-tasas",
        "kind": "problem",
        "level": 1,
        "source": "Matemática · TP2, ej. 28 y 31",
        "title": "Repartir en una razón dada",
        "statement": "Ejercicio 28: el perímetro de una cancha de fútbol mide 432 metros. Si la razón entre el ancho y el largo es 5 : 7, ¿cuánto mide cada lado de la cancha?\nEjercicio 31: las medidas de los ángulos interiores de un triángulo están en la razón 3 : 4 : 5. ¿Cuánto mide cada uno de los ángulos?",
        "parts": [
            {
                "prompt": "a) Ancho de la cancha, en m.",
                "check": {"type": "numeric", "value": 90, "tolerance": 0, "unit": "m"},
                "answer": "90 m",
            },
            {
                "prompt": "b) Largo de la cancha, en m.",
                "check": {"type": "numeric", "value": 126, "tolerance": 0, "unit": "m"},
                "answer": "126 m",
            },
            {
                "prompt": "c) Ángulo mayor del triángulo, en grados.",
                "check": {"type": "numeric", "value": 75, "tolerance": 0, "unit": "°"},
                "answer": "75° (los ángulos son 45°, 60° y 75°)",
            },
        ],
        "hints": [
            "Con una razón 5 : 7 escribí ancho = 5k y largo = 7k.",
            "El perímetro es la suma de los CUATRO lados; los ángulos interiores de un triángulo suman 180°.",
        ],
        "solution": [
            "**Cancha**: ancho `5k` y largo `7k`. Perímetro: `2(5k + 7k) = 24k = 432` → `k = 18`.",
            "Ancho `5 · 18 = 90 m` y largo `7 · 18 = 126 m`. Control: `2(90 + 126) = 432` ✓.",
            "**Triángulo**: ángulos `3k`, `4k`, `5k` con `3k + 4k + 5k = 12k = 180°` → `k = 15°`.",
            "Los ángulos miden `45°`, `60°` y `75°`.",
        ],
    },
    {
        "id": "p-razones-tasas-tp2-29-32",
        "node": "p-razones-tasas",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP2, ej. 29, 30 y 32",
        "title": "Razones con edades y áreas",
        "statement": "Ejercicio 29: las edades de Jenny y Claudio son 25 y 35 años respectivamente. ¿Dentro de cuántos años estarán las edades en la razón 4 : 5?\nEjercicio 30: las áreas de dos triángulos están en una razón de 4 a 9. El triángulo más pequeño tiene un área de 50 cm². Encontrá el área del triángulo grande.\nEjercicio 32: las edades de Carla y Ricardo están en la relación de 7 a 5, respectivamente. Si dentro de 9 años estarán en la relación de 5 a 4, ¿cuál es la edad actual de Carla?",
        "parts": [
            {
                "prompt": "a) Ej. 29: ¿dentro de cuántos años? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": "años"},
                "answer": "15 años",
            },
            {
                "prompt": "b) Ej. 30: área del triángulo grande, en cm².",
                "check": {"type": "numeric", "value": 112.5, "tolerance": 0.001, "unit": "cm²"},
                "answer": "112,5 cm²",
            },
            {
                "prompt": "c) Ej. 32: edad actual de Carla, en años.",
                "check": {"type": "numeric", "value": 21, "tolerance": 0, "unit": "años"},
                "answer": "21 años (Ricardo tiene 15)",
            },
        ],
        "hints": [
            "En los problemas de edades, dentro de t años las DOS edades aumentan t.",
            "En el 32 escribí las edades actuales como 7k y 5k.",
        ],
        "solution": [
            "**29)** `(25 + t)/(35 + t) = 4/5` → `5(25 + t) = 4(35 + t)` → `125 + 5t = 140 + 4t` → `t = 15`. Control: 40/50 = 4/5 ✓.",
            "**30)** `50/A = 4/9` → `4A = 450` → `A = 112,5 cm²`.",
            "**32)** Hoy Carla tiene `7k` y Ricardo `5k`. Dentro de 9 años: `(7k + 9)/(5k + 9) = 5/4`.",
            "`4(7k + 9) = 5(5k + 9)` → `28k + 36 = 25k + 45` → `3k = 9` → `k = 3`.",
            "Carla tiene `7 · 3 = 21` años y Ricardo 15. Control: dentro de 9 años, 30/24 = 5/4 ✓.",
        ],
    },
    {
        "id": "p-porcentajes-tp2-33",
        "node": "p-porcentajes",
        "kind": "problem",
        "level": 1,
        "source": "Matemática · TP2, ej. 33 (a, c, e)",
        "title": "Aumentos y descuentos: ida y vuelta",
        "statement": "Completá con la respuesta correcta:\na) Al aumentar 4800 en un 20% se obtiene …\nc) La cantidad … aumentada en un 30% es 47 060.\ne) La cantidad … disminuida en un 19% es 55 485.",
        "parts": [
            {
                "prompt": "a) Respondé solo con el número.",
                "check": {"type": "numeric", "value": 5760, "tolerance": 0, "unit": ""},
                "answer": "5760",
            },
            {
                "prompt": "c) Respondé solo con el número.",
                "check": {"type": "numeric", "value": 36200, "tolerance": 0, "unit": ""},
                "answer": "36 200",
            },
            {
                "prompt": "e) Respondé solo con el número.",
                "check": {"type": "numeric", "value": 68500, "tolerance": 0, "unit": ""},
                "answer": "68 500",
            },
        ],
        "hints": [
            "Aumentar un 20% es multiplicar por 1,20; disminuir un 19% es multiplicar por 0,81.",
            "Si te dan el resultado y falta la cantidad original, dividí por el factor (no restes el porcentaje del resultado).",
        ],
        "solution": [
            "**a)** `4800 · 1,20 = 5760`.",
            "**c)** `C · 1,30 = 47 060` → `C = 47 060 / 1,30 = 36 200`.",
            "**e)** `C · 0,81 = 55 485` → `C = 55 485 / 0,81 = 68 500`.",
            "Error típico en c): calcular el 30% de 47 060 y restarlo (da 32 942), pero el 30% se aplicó sobre la cantidad original, no sobre el resultado.",
        ],
    },
    {
        "id": "p-porcentajes-tp2-35-36",
        "node": "p-porcentajes",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP2, ej. 35 y 36",
        "title": "Calcetines y guantes: volver al precio original",
        "statement": "Ejercicio 35: Juan se compró un par de calcetines el lunes; el martes su precio subió un 15% y el miércoles bajó un 10%. Si el miércoles el precio de venta es de $1035, ¿cuánto pagó Juan por el producto el lunes?\nEjercicio 36: Marta tiene $58 500 y gastó un 20% para comprar un par de guantes que estaban rebajados un 10%. ¿Cuánto costaba el par de guantes antes de ser rebajado?",
        "parts": [
            {
                "prompt": "a) Ej. 35: precio del lunes, en $.",
                "check": {"type": "numeric", "value": 1000, "tolerance": 0, "unit": "$"},
                "answer": "1000 $",
            },
            {
                "prompt": "b) Ej. 36: precio de los guantes antes de la rebaja, en $.",
                "check": {"type": "numeric", "value": 13000, "tolerance": 0, "unit": "$"},
                "answer": "13 000 $",
            },
        ],
        "hints": [
            "Porcentajes sucesivos se multiplican: subir 15% y bajar 10% es multiplicar por `1,15 · 0,90`.",
            "En el 36, lo que gastó Marta es el precio YA rebajado, es decir, el 90% del precio original.",
        ],
        "solution": [
            "**35)** Si p es el precio del lunes: `p · 1,15 · 0,90 = 1035` → `p · 1,035 = 1035` → `p = 1000`.",
            "Ojo: no da lo mismo que subir 5%, pero tampoco vuelve al valor original; el factor total es 1,035 (+3,5%).",
            "**36)** Marta gastó `20% de 58 500 = 0,20 · 58 500 = 11 700 $`.",
            "Ese es el precio rebajado: `P · 0,90 = 11 700` → `P = 13 000 $`.",
        ],
    },
    {
        "id": "p-porcentajes-tp2-37",
        "node": "p-porcentajes",
        "kind": "problem",
        "level": 1,
        "source": "Matemática · TP2, ej. 37",
        "title": "Composición de una aleación",
        "statement": "Una pieza cuya masa es de 36,5 kg debe ser hecha de una aleación de cobre, estaño y zinc. ¿Cuánto de cada metal se necesitará, si la aleación debe contener el 96% de cobre, el 3% de estaño y 1% de zinc?",
        "parts": [
            {
                "prompt": "a) Masa de cobre, en kg.",
                "check": {"type": "numeric", "value": 35.04, "tolerance": 0.001, "unit": "kg"},
                "answer": "35,04 kg",
            },
            {
                "prompt": "b) Masa de estaño, en kg.",
                "check": {"type": "numeric", "value": 1.095, "tolerance": 0.001, "unit": "kg"},
                "answer": "1,095 kg",
            },
            {
                "prompt": "c) Masa de zinc, en kg.",
                "check": {"type": "numeric", "value": 0.365, "tolerance": 0.001, "unit": "kg"},
                "answer": "0,365 kg",
            },
        ],
        "hints": [
            "El p% de una cantidad es `p/100` por la cantidad.",
            "Controlá al final que las tres masas sumen 36,5 kg.",
        ],
        "solution": [
            "Cobre: `0,96 · 36,5 = 35,04 kg`.",
            "Estaño: `0,03 · 36,5 = 1,095 kg`.",
            "Zinc: `0,01 · 36,5 = 0,365 kg`.",
            "Control: `35,04 + 1,095 + 0,365 = 36,5 kg` ✓ (los porcentajes suman 100%).",
        ],
    },
    {
        "id": "p-porcentajes-tp2-39",
        "node": "p-porcentajes",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP2, ej. 39",
        "title": "Porcentajes de porcentajes en un examen",
        "statement": "Hubo un 60% de alumnos que superaron el examen de matemáticas. De ellos, el 25% obtuvo una nota de 6 y el 50% del resto obtuvo una nota de 9. Si hay un total de 240 alumnos, ¿cuántos superaron la prueba? ¿Cuántos obtuvieron un 6 y cuántos un 9?",
        "parts": [
            {
                "prompt": "a) ¿Cuántos alumnos superaron la prueba?",
                "check": {"type": "numeric", "value": 144, "tolerance": 0, "unit": "alumnos"},
                "answer": "144 alumnos",
            },
            {
                "prompt": "b) ¿Cuántos obtuvieron un 6?",
                "check": {"type": "numeric", "value": 36, "tolerance": 0, "unit": "alumnos"},
                "answer": "36 alumnos",
            },
            {
                "prompt": "c) ¿Cuántos obtuvieron un 9?",
                "check": {"type": "numeric", "value": 54, "tolerance": 0, "unit": "alumnos"},
                "answer": "54 alumnos",
            },
        ],
        "hints": [
            "Cada porcentaje se calcula sobre un total distinto: fijate bien de qué cantidad es cada uno.",
            "\"El 50% del resto\" es la mitad de los aprobados que NO sacaron 6.",
        ],
        "solution": [
            "Aprobados: `0,60 · 240 = 144`.",
            "Con 6: `0,25 · 144 = 36`.",
            "El resto de los aprobados: `144 − 36 = 108`; con 9: `0,50 · 108 = 54`.",
            "Los otros 54 aprobados sacaron otras notas, y 96 alumnos no aprobaron.",
        ],
    },
    {
        "id": "p-porcentajes-tp2-40",
        "node": "p-porcentajes",
        "kind": "problem",
        "level": 3,
        "source": "Matemática · TP2, ej. 40",
        "title": "Se van hombres y llegan mujeres",
        "statement": "En una fiesta el número de hombres era el doble del número de mujeres; luego se retiran el 35% de los hombres y llegan 90 mujeres, quedando tantos hombres como mujeres. ¿Cuántas mujeres había inicialmente?",
        "parts": [
            {
                "prompt": "a) Cantidad inicial de mujeres. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 300, "tolerance": 0, "unit": "mujeres"},
                "answer": "300 mujeres",
            },
        ],
        "hints": [
            "Llamá M a las mujeres iniciales; los hombres son 2M.",
            "Si se va el 35% de los hombres, queda el 65%: `0,65 · 2M`.",
        ],
        "solution": [
            "Al principio: M mujeres y 2M hombres.",
            "Después: hombres `0,65 · 2M = 1,3M`; mujeres `M + 90`.",
            "Quedan iguales: `1,3M = M + 90` → `0,3M = 90` → `M = 300`.",
            "Control: 600 hombres, se van 210 y quedan 390; las mujeres pasan de 300 a 390 ✓.",
        ],
    },
    {
        "id": "g-semejanza-tp2-43",
        "node": "g-semejanza",
        "kind": "problem",
        "level": 1,
        "source": "Matemática · TP2, ej. 43",
        "title": "La altura del edificio por su sombra",
        "statement": "En un determinado momento del día un semáforo de 2 m de alto proyecta una sombra de 10 m y un edificio que se encuentra detrás del semáforo proyecta una sombra de 80 m. ¿Cuál es la altura del edificio?",
        "parts": [
            {
                "prompt": "a) Altura del edificio, en m.",
                "check": {"type": "numeric", "value": 16, "tolerance": 0, "unit": "m"},
                "answer": "16 m",
            },
        ],
        "hints": [
            "Los rayos de sol llegan paralelos: el semáforo con su sombra y el edificio con la suya forman triángulos rectángulos semejantes.",
        ],
        "solution": [
            "Cada objeto vertical, su sombra y el rayo de sol forman un triángulo rectángulo. Como los rayos son paralelos, los dos triángulos tienen los mismos ángulos: son semejantes (criterio AA).",
            "Lados homólogos proporcionales: `h/80 = 2/10`.",
            "`h = 80 · 2/10 = 16 m`.",
        ],
    },
    {
        "id": "g-pitagoras-especiales-tp2-52",
        "node": "g-pitagoras-especiales",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP2, ej. 52",
        "title": "¿De cuántas pulgadas es el televisor?",
        "statement": "La medida que se utiliza en los televisores es la longitud de la diagonal de la pantalla medida en pulgadas. Si David compró un televisor que entra justo en un hueco de 106 cm × 61 cm, ¿de cuántas pulgadas es el televisor? [1 pulgada = 1\" = 2,54 cm]",
        "parts": [
            {
                "prompt": "a) Diagonal en cm, redondeada a 0,1.",
                "check": {"type": "numeric", "value": 122.3, "tolerance": 0.002, "unit": "cm"},
                "answer": "122,3 cm",
            },
            {
                "prompt": "b) Diagonal en pulgadas, redondeada al entero.",
                "check": {"type": "numeric", "value": 48.15, "tolerance": 0.01, "unit": "\""},
                "answer": "48\" (48,15 pulgadas)",
            },
        ],
        "hints": [
            "La diagonal es la hipotenusa del triángulo rectángulo cuyos catetos son el ancho y el alto.",
            "Para pasar de cm a pulgadas, dividí por 2,54.",
        ],
        "solution": [
            "Por Pitágoras: `d² = 106² + 61² = 11 236 + 3721 = 14 957`.",
            "`d = √14 957 ≈ 122,3 cm`.",
            "En pulgadas: `122,3 / 2,54 ≈ 48,15`, o sea un televisor de **48 pulgadas**.",
        ],
    },
    {
        "id": "g-trigonometria-tp2-54",
        "node": "g-trigonometria",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP2, ej. 54",
        "title": "Calcular expresiones a partir de una razón",
        "statement": "Sabiendo que α es un ángulo agudo, calculá:\na) `(1 + sen α)/cos α`, sabiendo que `tg α = 3/4`\nb) `(cos α − sen α) · cosec α`, sabiendo que `sec α = 13/5`\nc) `(√3 · cosec α + cos α) · tg α`, sabiendo que `sen α = √3/√7`",
        "parts": [
            {
                "prompt": "a) Resultado de a). Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0.001, "unit": ""},
                "answer": "2",
            },
            {
                "prompt": "b) Resultado de b), como fracción irreducible.",
                "check": {"type": "numeric", "value": -0.583333, "tolerance": 0.001, "unit": ""},
                "answer": "−7/12",
            },
            {
                "prompt": "c) Resultado de c), redondeado a 0,01.",
                "check": {"type": "numeric", "value": 2.946, "tolerance": 0.005, "unit": ""},
                "answer": "2,95 (valor exacto 9√21/14)",
            },
        ],
        "hints": [
            "Dibujá un triángulo rectángulo con la razón dada y completá el lado que falta con Pitágoras.",
            "Recordá: `sec α = 1/cos α`, `cosec α = 1/sen α`, `tg α = sen α / cos α`.",
        ],
        "solution": [
            "**a)** `tg α = 3/4`: catetos 3 (opuesto) y 4 (adyacente), hipotenusa 5. `sen α = 3/5`, `cos α = 4/5`.",
            "`(1 + 3/5)/(4/5) = (8/5)/(4/5) = 2`.",
            "**b)** `sec α = 13/5` → `cos α = 5/13`; el cateto opuesto es `√(169 − 25) = 12`, así que `sen α = 12/13` y `cosec α = 13/12`.",
            "`(5/13 − 12/13) · 13/12 = −7/13 · 13/12 = −7/12`.",
            "**c)** `sen α = √3/√7` → `cos α = √(1 − 3/7) = 2/√7`; `cosec α = √7/√3`; `tg α = √3/2`.",
            "`√3 · cosec α = √7`, entonces el paréntesis vale `√7 + 2/√7 = 9/√7`. Por `tg α`: `9/√7 · √3/2 = 9√21/14 ≈ 2,95`.",
        ],
    },
    {
        "id": "g-trigonometria-tp2-58",
        "node": "g-trigonometria",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP2, ej. 58",
        "title": "Resolver un triángulo rectángulo con dos catetos",
        "statement": "Calculá los ángulos interiores, el perímetro y la superficie de un triángulo rectángulo de catetos a = 124,68 m y b = 86,13 m.",
        "parts": [
            {
                "prompt": "a) Ángulo agudo opuesto al cateto a, en grados (redondeá a 0,01°).",
                "check": {"type": "numeric", "value": 55.363, "tolerance": 0.001, "unit": "°"},
                "answer": "55,36° (el otro agudo mide 34,64°)",
            },
            {
                "prompt": "b) Perímetro, en m (redondeá a 0,01).",
                "check": {"type": "numeric", "value": 362.347, "tolerance": 0.001, "unit": "m"},
                "answer": "362,35 m",
            },
            {
                "prompt": "c) Superficie, en m² (redondeá a 0,01).",
                "check": {"type": "numeric", "value": 5369.344, "tolerance": 0.001, "unit": "m²"},
                "answer": "5369,34 m²",
            },
        ],
        "hints": [
            "Con los dos catetos, la tangente da el ángulo: `tg α = opuesto/adyacente`.",
            "La hipotenusa sale por Pitágoras y el área es cateto por cateto sobre 2.",
        ],
        "solution": [
            "Ángulo opuesto a a: `tg α = 124,68/86,13 ≈ 1,4476` → `α ≈ 55,36°`. El otro agudo: `β = 90° − 55,36° = 34,64°`; el tercero es el recto, 90°.",
            "Hipotenusa: `c = √(124,68² + 86,13²) = √(15 545,1 + 7418,4) ≈ 151,54 m`.",
            "Perímetro: `124,68 + 86,13 + 151,54 ≈ 362,35 m`.",
            "Superficie: `124,68 · 86,13 / 2 ≈ 5369,34 m²`.",
        ],
    },
    {
        "id": "g-trigonometria-tp2-61",
        "node": "g-trigonometria",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP2, ej. 61",
        "title": "Torre de agua vista desde una ventana",
        "statement": "Una torre de agua está situada a 25 m de un edificio. Desde una ventana del edificio, un observador ve que el ángulo de elevación a la parte superior de la torre es 39° y que el ángulo de depresión de la parte inferior de la torre es 25°. ¿Cuál es la altura de la torre? ¿Cuál es la altura de la ventana?",
        "parts": [
            {
                "prompt": "a) Altura de la torre, en m (redondeá a 0,01).",
                "check": {"type": "numeric", "value": 31.902, "tolerance": 0.002, "unit": "m"},
                "answer": "31,90 m",
            },
            {
                "prompt": "b) Altura de la ventana, en m (redondeá a 0,01).",
                "check": {"type": "numeric", "value": 11.658, "tolerance": 0.002, "unit": "m"},
                "answer": "11,66 m",
            },
        ],
        "hints": [
            "Trazá la horizontal desde la ventana hasta la torre (mide 25 m): divide la torre en una parte de arriba y una de abajo.",
            "En cada triángulo rectángulo, la parte de la torre es el cateto opuesto: `tg(ángulo) · 25`.",
        ],
        "solution": [
            "La horizontal que sale de la ventana mide 25 m y corta a la torre en dos tramos.",
            "Tramo de abajo (depresión 25°): `25 · tg 25° ≈ 25 · 0,4663 ≈ 11,66 m`. Es igual a la altura de la ventana.",
            "Tramo de arriba (elevación 39°): `25 · tg 39° ≈ 25 · 0,8098 ≈ 20,24 m`.",
            "Altura de la torre: `11,66 + 20,24 ≈ 31,90 m`; altura de la ventana: `11,66 m`.",
        ],
    },
    {
        "id": "g-trigonometria-tp2-62",
        "node": "g-trigonometria",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP2, ej. 62",
        "title": "El árbol quebrado",
        "statement": "Un árbol se quiebra debido a una tormenta y la parte que se ha quebrado se inclina de modo que su extremo superior toca el suelo formando un ángulo de 30° con este. La distancia entre el pie del árbol y el punto donde toca el suelo es de 8 m. Calculá la altura original del árbol.",
        "parts": [
            {
                "prompt": "a) Altura original del árbol, en m (redondeá a 0,01).",
                "check": {"type": "numeric", "value": 13.856, "tolerance": 0.002, "unit": "m"},
                "answer": "13,86 m (exacto: 8√3 m)",
            },
        ],
        "hints": [
            "El tronco que queda en pie, el suelo y la parte quebrada forman un triángulo rectángulo con el ángulo de 30° en el suelo.",
            "La altura original es el tronco en pie MÁS la parte quebrada (la hipotenusa).",
        ],
        "solution": [
            "Triángulo rectángulo: cateto horizontal 8 m (suelo), cateto vertical h₁ (tronco en pie) e hipotenusa h₂ (parte quebrada), con 30° en el punto del suelo.",
            "`h₁ = 8 · tg 30° = 8/√3 ≈ 4,62 m`.",
            "`h₂ = 8 / cos 30° = 16/√3 ≈ 9,24 m`.",
            "Altura original: `h₁ + h₂ = 24/√3 = 8√3 ≈ 13,86 m`.",
        ],
    },
    {
        "id": "g-trigonometria-tp2-63",
        "node": "g-trigonometria",
        "kind": "problem",
        "level": 3,
        "source": "Matemática · TP2, ej. 63",
        "title": "Acercarse al edificio: de 30° a 60°",
        "statement": "Un niño de 1,5 m de altura se encuentra a cierta distancia de un edificio de 30 m de altura. El ángulo de elevación desde sus ojos hasta la parte superior del edificio aumenta de 30° a 60° cuando camina hacia el edificio. ¿Qué distancia recorrió el niño? (Tomá la altura de los ojos igual a 1,5 m.)",
        "parts": [
            {
                "prompt": "a) Distancia recorrida, en m (redondeá a 0,01).",
                "check": {"type": "numeric", "value": 32.909, "tolerance": 0.002, "unit": "m"},
                "answer": "32,91 m (exacto: 19√3 m)",
            },
        ],
        "hints": [
            "Desde los ojos del niño, la parte del edificio que se ve hacia arriba mide 30 − 1,5 = 28,5 m.",
            "Calculá la distancia horizontal al edificio en cada posición con `distancia = 28,5 / tg(ángulo)` y restá.",
        ],
        "solution": [
            "Altura sobre los ojos: `30 − 1,5 = 28,5 m`.",
            "Primera posición (30°): `d₁ = 28,5 / tg 30° = 28,5√3 ≈ 49,36 m`.",
            "Segunda posición (60°): `d₂ = 28,5 / tg 60° = 28,5/√3 ≈ 16,45 m`.",
            "Recorrió `d₁ − d₂ ≈ 49,36 − 16,45 = 32,91 m` (exacto `19√3 m`).",
        ],
    },
    {
        "id": "g-trigonometria-tp2-64",
        "node": "g-trigonometria",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP2, ej. 64",
        "title": "Antena sobre un edificio",
        "statement": "Desde un punto del suelo se observan la parte inferior y la parte superior de una torre de transmisión ubicada sobre un edificio de 20 m de altura. Los ángulos de elevación son de 45° y 60°, respectivamente. Calculá la altura de la torre de transmisión.",
        "parts": [
            {
                "prompt": "a) Altura de la torre de transmisión, en m (redondeá a 0,01).",
                "check": {"type": "numeric", "value": 14.641, "tolerance": 0.002, "unit": "m"},
                "answer": "14,64 m (exacto: 20(√3 − 1) m)",
            },
        ],
        "hints": [
            "La base de la torre está a 20 m de altura (el techo del edificio): con 45°, eso te da la distancia horizontal.",
            "Con esa distancia y 60°, calculá la altura hasta la punta de la torre y restale los 20 m del edificio.",
        ],
        "solution": [
            "Base de la torre (45°): `tg 45° = 20/d` → `d = 20 m`.",
            "Punta de la torre (60°): altura total `= d · tg 60° = 20√3 ≈ 34,64 m`.",
            "Torre: `34,64 − 20 = 14,64 m` (exacto `20(√3 − 1)`).",
        ],
    },
    {
        "id": "g-trigonometria-tp2-65",
        "node": "g-trigonometria",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP2, ej. 65",
        "title": "Dos barcos vistos desde un faro de 75 m",
        "statement": "Desde el nivel del mar, observando desde la parte superior de un faro de 75 m de altura, los ángulos de depresión de dos barcos son de 30° y 45°. Si uno de los barcos se encuentra exactamente detrás del otro, del mismo lado del faro, calculá la distancia entre los dos barcos.",
        "parts": [
            {
                "prompt": "a) Distancia entre los barcos, en m (redondeá a 0,01).",
                "check": {"type": "numeric", "value": 54.904, "tolerance": 0.002, "unit": "m"},
                "answer": "54,90 m (exacto: 75(√3 − 1) m)",
            },
        ],
        "hints": [
            "El ángulo de depresión desde la punta del faro es igual al ángulo de elevación desde el barco (alternos internos).",
            "El barco con depresión mayor (45°) está más cerca del faro.",
        ],
        "solution": [
            "Barco cercano (45°): `d₁ = 75 / tg 45° = 75 m`.",
            "Barco lejano (30°): `d₂ = 75 / tg 30° = 75√3 ≈ 129,90 m`.",
            "Distancia entre ellos: `d₂ − d₁ = 75(√3 − 1) ≈ 54,90 m`.",
        ],
    },
    {
        "id": "g-trigonometria-tp2-66",
        "node": "g-trigonometria",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP2, ej. 66",
        "title": "Torre de cables desde un edificio de 7 m",
        "statement": "Desde la parte superior de un edificio de 7 m de altura, el ángulo de elevación de la parte superior de una torre de cables es de 60°, mientras que el ángulo de depresión de la base de la torre es de 45°. Determiná la altura de la torre.",
        "parts": [
            {
                "prompt": "a) Altura de la torre, en m (redondeá a 0,01).",
                "check": {"type": "numeric", "value": 19.124, "tolerance": 0.002, "unit": "m"},
                "answer": "19,12 m (exacto: 7 + 7√3 m)",
            },
        ],
        "hints": [
            "Con la depresión de 45° hacia la base y los 7 m del edificio, obtené la distancia horizontal entre edificio y torre.",
            "La torre es 7 m (hasta la horizontal del observador) más la parte que se ve con 60°.",
        ],
        "solution": [
            "Depresión 45° hacia la base: `tg 45° = 7/d` → `d = 7 m`.",
            "Por encima de la horizontal del observador: `7 · tg 60° = 7√3 ≈ 12,12 m`.",
            "Altura de la torre: `7 + 7√3 ≈ 19,12 m`.",
        ],
    },
    {
        "id": "g-poligonos-cuadrilateros-tp2-17",
        "node": "g-poligonos-cuadrilateros",
        "kind": "problem",
        "level": 1,
        "source": "Matemática · TP2, ej. 17 (b, d, f)",
        "title": "Verdadero o falso sobre cuadriláteros",
        "statement": "Indicá si los siguientes enunciados son verdaderos o falsos.\nb) Un trapecio es un cuadrilátero que tiene dos pares de lados opuestos paralelos.\nd) Las diagonales de un rectángulo son perpendiculares entre sí.\nf) Cada par de ángulos interiores correspondientes a vértices consecutivos de un paralelogramo son suplementarios.",
        "parts": [
            {
                "prompt": "a) Enunciado b)",
                "check": {"type": "choice", "options": ["Verdadero", "Falso: un trapecio tiene un solo par de lados opuestos paralelos", "Falso: un trapecio no tiene lados paralelos"], "correct": 1},
                "answer": "Falso: un trapecio tiene un solo par de lados opuestos paralelos",
            },
            {
                "prompt": "b) Enunciado d)",
                "check": {"type": "choice", "options": ["Verdadero", "Falso: solo son perpendiculares si el rectángulo es un cuadrado", "Falso: las diagonales de un rectángulo no se cortan"], "correct": 1},
                "answer": "Falso: solo son perpendiculares si el rectángulo es un cuadrado",
            },
            {
                "prompt": "c) Enunciado f)",
                "check": {"type": "choice", "options": ["Verdadero: suman 180°", "Falso: son congruentes", "Falso: suman 90°"], "correct": 0},
                "answer": "Verdadero: suman 180°",
            },
        ],
        "hints": [
            "Pensá en un contraejemplo concreto: un rectángulo de 4 × 2, por ejemplo.",
            "En un paralelogramo, dos lados opuestos son paralelos y el lado que los une es una transversal: los ángulos de sus extremos son conjugados internos.",
        ],
        "solution": [
            "**b) Falso.** El trapecio tiene UN solo par de lados opuestos paralelos (las bases). Con dos pares es un paralelogramo.",
            "**d) Falso.** Las diagonales de un rectángulo son iguales y se cortan en su punto medio, pero solo son perpendiculares si además es cuadrado. En un rectángulo de 4 × 2 se cortan formando ángulos de aprox. 53° y 127°.",
            "**f) Verdadero.** Dos lados opuestos son paralelos y el lado que los une es una transversal: los ángulos de dos vértices consecutivos son conjugados internos entre paralelas, y suman 180°.",
        ],
    },
    {
        "id": "g-poligonos-cuadrilateros-tp2-59",
        "node": "g-poligonos-cuadrilateros",
        "kind": "problem",
        "level": 3,
        "source": "Matemática · TP2, ej. 59",
        "title": "Área de un heptágono regular",
        "statement": "Un diseñador necesita elaborar una pieza decorativa con forma de heptágono regular ABCDEFG. Cada uno de sus lados mide 9,2 cm (en particular `AG = 9,2 cm`). Para determinar la cantidad de material necesario, se desea calcular el área de la pieza. En la figura, O es el centro, P es el punto medio del lado AG, OP es la apotema y **a** es el ángulo AOP.",
        "parts": [
            {
                "prompt": "a) Amplitud del ángulo a = AOP, en grados (redondeá a 0,01°).",
                "check": {"type": "numeric", "value": 25.714, "tolerance": 0.001, "unit": "°"},
                "answer": "25,71° (es 180°/7)",
            },
            {
                "prompt": "b) Apotema OP, en cm (redondeá a 0,01).",
                "check": {"type": "numeric", "value": 9.552, "tolerance": 0.002, "unit": "cm"},
                "answer": "9,55 cm",
            },
            {
                "prompt": "c) Área del heptágono, en cm² (redondeá a 0,1).",
                "check": {"type": "numeric", "value": 307.57, "tolerance": 0.002, "unit": "cm²"},
                "answer": "307,6 cm²",
            },
        ],
        "hints": [
            "Los 7 ángulos centrales del heptágono suman 360°; la apotema parte cada uno por la mitad.",
            "En el triángulo rectángulo OPA: `AP = 4,6 cm` es el cateto opuesto al ángulo a y la apotema es el adyacente.",
            "Área de un polígono regular: `perímetro · apotema / 2`.",
        ],
        "solution": [
            "Ángulo central: `360°/7 ≈ 51,43°`. La apotema lo divide en dos: `a = 180°/7 ≈ 25,71°`.",
            "En el triángulo OPA, rectángulo en P: `AP = 9,2/2 = 4,6 cm`.",
            "`tg a = AP/OP` → `OP = 4,6 / tg 25,71° ≈ 4,6 / 0,4816 ≈ 9,55 cm`.",
            "Perímetro: `7 · 9,2 = 64,4 cm`.",
            "Área: `64,4 · 9,552 / 2 ≈ 307,6 cm²`.",
        ],
    },
]

# ============================ TP3 · ECUACIONES E INECUACIONES ============================
_M = "al-modulo-ecuaciones-inecuaciones"
EXERCISES += [
    {
        "id": "al-modulo-ecuaciones-inecuaciones-tp3-8a",
        "node": _M,
        "kind": "problem",
        "level": 1,
        "source": "Matemática · TP3, ej. 8 (a, b, c)",
        "title": "Inecuaciones con módulo (1)",
        "statement": "Resolvé las inecuaciones y escribí el conjunto solución como intervalo.\na) `|2x − 3| ≤ 7`\nb) `|6x − 1| ≥ 11`\nc) `2 · |x + 1| < 6`",
        "parts": [
            {
                "prompt": "a) S =",
                "check": {"type": "choice", "options": ["[−2; 5]", "(−2; 5)", "[−5; 2]", "(−∞; −2] ∪ [5; ∞)"], "correct": 0},
                "answer": "[−2; 5]",
            },
            {
                "prompt": "b) S =",
                "check": {"type": "choice", "options": ["(−∞; −5/3] ∪ [2; ∞)", "[−5/3; 2]", "(−∞; −2] ∪ [5/3; ∞)", "[2; ∞)"], "correct": 0},
                "answer": "(−∞; −5/3] ∪ [2; ∞)",
            },
            {
                "prompt": "c) S =",
                "check": {"type": "choice", "options": ["(−4; 2)", "(−2; 4)", "(−4; 2]", "(−∞; −4) ∪ (2; ∞)"], "correct": 0},
                "answer": "(−4; 2)",
            },
        ],
        "hints": [
            "`|u| ≤ k` (con k > 0) equivale a `−k ≤ u ≤ k`: un solo intervalo.",
            "`|u| ≥ k` equivale a `u ≤ −k` o `u ≥ k`: dos semirrectas unidas.",
            "Antes de aplicar la propiedad, dejá el módulo solo de un lado.",
        ],
        "solution": [
            "**a)** `−7 ≤ 2x − 3 ≤ 7` → sumando 3: `−4 ≤ 2x ≤ 10` → dividiendo por 2: `−2 ≤ x ≤ 5`. `S = [−2; 5]`.",
            "**b)** `6x − 1 ≥ 11` → `x ≥ 2`, o bien `6x − 1 ≤ −11` → `6x ≤ −10` → `x ≤ −5/3`.",
            "`S = (−∞; −5/3] ∪ [2; ∞)`.",
            "**c)** Dividimos por 2: `|x + 1| < 3` → `−3 < x + 1 < 3` → `−4 < x < 2`. `S = (−4; 2)`.",
            "El enunciado original dice \"Resuelva las ecuaciones\", pero son inecuaciones: el resultado es un intervalo, no un par de valores.",
        ],
    },
    {
        "id": "al-modulo-ecuaciones-inecuaciones-tp3-8d",
        "node": _M,
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP3, ej. 8 (d, e, f)",
        "title": "Inecuaciones con módulo (2)",
        "statement": "Resolvé las inecuaciones.\nd) `(5/3) · |x + 1| > 10`\ne) `−2 − |x + 4| > −5`\nf) `(4/5) · |x + 3/2| − 4 ≥ 2`",
        "parts": [
            {
                "prompt": "a) S de d) =",
                "check": {"type": "choice", "options": ["(−∞; −7) ∪ (5; ∞)", "(−7; 5)", "(−∞; −5) ∪ (7; ∞)", "(−∞; −7] ∪ [5; ∞)"], "correct": 0},
                "answer": "(−∞; −7) ∪ (5; ∞)",
            },
            {
                "prompt": "b) S de e) =",
                "check": {"type": "choice", "options": ["(−7; −1)", "(−∞; −7) ∪ (−1; ∞)", "(1; 7)", "(−7; 1)"], "correct": 0},
                "answer": "(−7; −1)",
            },
            {
                "prompt": "c) S de f) =",
                "check": {"type": "choice", "options": ["(−∞; −9] ∪ [6; ∞)", "[−9; 6]", "(−∞; −6] ∪ [9; ∞)", "(−∞; −9) ∪ (6; ∞)"], "correct": 0},
                "answer": "(−∞; −9] ∪ [6; ∞)",
            },
        ],
        "hints": [
            "Despejá el módulo como si fuera una incógnita común; cuidado al multiplicar o dividir por un negativo.",
            "En e), al pasar `−|x + 4| > −3` a `|x + 4| < 3` se invierte el sentido de la desigualdad.",
        ],
        "solution": [
            "**d)** `|x + 1| > 10 · 3/5 = 6` → `x + 1 > 6` o `x + 1 < −6` → `x > 5` o `x < −7`. `S = (−∞; −7) ∪ (5; ∞)`.",
            "**e)** `−|x + 4| > −5 + 2 = −3`. Multiplicando por −1 (se invierte): `|x + 4| < 3`.",
            "`−3 < x + 4 < 3` → `−7 < x < −1`. `S = (−7; −1)`.",
            "**f)** `(4/5)|x + 3/2| ≥ 6` → `|x + 3/2| ≥ 6 · 5/4 = 15/2`.",
            "`x + 3/2 ≥ 15/2` → `x ≥ 6`, o `x + 3/2 ≤ −15/2` → `x ≤ −9`. `S = (−∞; −9] ∪ [6; ∞)`.",
        ],
    },
    {
        "id": "al-modulo-ecuaciones-inecuaciones-tp3-8g",
        "node": _M,
        "kind": "problem",
        "level": 3,
        "source": "Matemática · TP3, ej. 8 (g, h, i)",
        "title": "Inecuaciones con módulo (3)",
        "statement": "Resolvé las inecuaciones.\ng) `4 + |2x − 3| ≥ 7`\nh) `(3/2 − |x + 5/4|)/(−2) − 3 ≤ 2`\ni) `(3/2 − |x + 1/4|)/(−3) − 1 ≤ 4`",
        "parts": [
            {
                "prompt": "a) S de g) =",
                "check": {"type": "choice", "options": ["(−∞; 0] ∪ [3; ∞)", "[0; 3]", "(−∞; 0) ∪ (3; ∞)", "[3; ∞)"], "correct": 0},
                "answer": "(−∞; 0] ∪ [3; ∞)",
            },
            {
                "prompt": "b) S de h) =",
                "check": {"type": "choice", "options": ["[−51/4; 41/4]", "(−∞; −51/4] ∪ [41/4; ∞)", "[−41/4; 51/4]", "[−29/4; 19/4]"], "correct": 0},
                "answer": "[−51/4; 41/4]",
            },
            {
                "prompt": "c) S de i) =",
                "check": {"type": "choice", "options": ["[−67/4; 65/4]", "(−∞; −67/4] ∪ [65/4; ∞)", "[−65/4; 67/4]", "[−13/4; 11/4]"], "correct": 0},
                "answer": "[−67/4; 65/4]",
            },
        ],
        "hints": [
            "En h) e i) pasá primero el número que resta, después multiplicá por el denominador negativo (¡se invierte!) y recién ahí despejá el módulo.",
            "Al final, restá el número que acompaña a x dentro del módulo en los dos extremos.",
        ],
        "solution": [
            "**g)** `|2x − 3| ≥ 3` → `2x − 3 ≥ 3` (x ≥ 3) o `2x − 3 ≤ −3` (x ≤ 0). `S = (−∞; 0] ∪ [3; ∞)`.",
            "**h)** `(3/2 − |x + 5/4|)/(−2) ≤ 5`. Multiplicando por −2 se invierte: `3/2 − |x + 5/4| ≥ −10`.",
            "`−|x + 5/4| ≥ −23/2` → `|x + 5/4| ≤ 23/2` → `−23/2 − 5/4 ≤ x ≤ 23/2 − 5/4` → `−51/4 ≤ x ≤ 41/4`.",
            "**i)** `(3/2 − |x + 1/4|)/(−3) ≤ 5` → por −3 (se invierte): `3/2 − |x + 1/4| ≥ −15` → `|x + 1/4| ≤ 33/2`.",
            "`−33/2 − 1/4 ≤ x ≤ 33/2 − 1/4` → `−67/4 ≤ x ≤ 65/4`. `S = [−67/4; 65/4]`.",
            "Si te olvidás de invertir la desigualdad al multiplicar por el negativo, obtenés justo el complemento (las dos semirrectas): por eso conviene verificar con un valor, por ejemplo x = 0 en h): `(3/2 − 5/4)/(−2) − 3 = −3,125 ≤ 2` ✓.",
        ],
    },
    {
        "id": "al-modulo-ecuaciones-inecuaciones-tp3-20a",
        "node": _M,
        "kind": "problem",
        "level": 1,
        "source": "Matemática · TP3, ej. 20 (a, d, e)",
        "title": "Ecuaciones modulares (1)",
        "statement": "Resolvé las ecuaciones modulares.\na) `|3x − 2| = 5`\nd) `|6 − 3x| = |2x + 1|`\ne) `|10x − 1| = |8x + 5|`",
        "parts": [
            {
                "prompt": "a) S =",
                "check": {"type": "choice", "options": ["S = {−1; 7/3}", "S = {1; −7/3}", "S = {7/3}", "S = {−1; 1}"], "correct": 0},
                "answer": "S = {−1; 7/3}",
            },
            {
                "prompt": "b) S de d) =",
                "check": {"type": "choice", "options": ["S = {1; 7}", "S = {1}", "S = {−1; 7}", "S = {1; −7}"], "correct": 0},
                "answer": "S = {1; 7}",
            },
            {
                "prompt": "c) S de e) =",
                "check": {"type": "choice", "options": ["S = {−2/9; 3}", "S = {3}", "S = {2/9; −3}", "S = {−3; 3}"], "correct": 0},
                "answer": "S = {−2/9; 3}",
            },
        ],
        "hints": [
            "`|u| = k` con k > 0 da dos ecuaciones: `u = k` o `u = −k`.",
            "`|u| = |w|` significa `u = w` o `u = −w`.",
        ],
        "solution": [
            "**a)** `3x − 2 = 5` → `x = 7/3`; `3x − 2 = −5` → `x = −1`. `S = {−1; 7/3}`.",
            "**d)** `6 − 3x = 2x + 1` → `5 = 5x` → `x = 1`; `6 − 3x = −(2x + 1)` → `6 − 3x = −2x − 1` → `x = 7`. `S = {1; 7}`.",
            "Verificación d): x = 7 → `|6 − 21| = 15` y `|15| = 15` ✓.",
            "**e)** `10x − 1 = 8x + 5` → `x = 3`; `10x − 1 = −8x − 5` → `18x = −4` → `x = −2/9`. `S = {−2/9; 3}`.",
        ],
    },
    {
        "id": "al-modulo-ecuaciones-inecuaciones-tp3-20b",
        "node": _M,
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP3, ej. 20 (b, g, i)",
        "title": "Ecuaciones modulares (2)",
        "statement": "Resolvé las ecuaciones modulares.\nb) `1/2 − |x + 1/6| = −3`\ng) `10 + |(5/4)x + 3| = 8`\ni) `−7 + |(1/3)x + 2| = 3`",
        "parts": [
            {
                "prompt": "a) S de b) =",
                "check": {"type": "choice", "options": ["S = {−11/3; 10/3}", "S = {−10/3; 11/3}", "S = {−8/3; 7/3}", "S = ∅"], "correct": 0},
                "answer": "S = {−11/3; 10/3}",
            },
            {
                "prompt": "b) S de g) =",
                "check": {"type": "choice", "options": ["S = ∅", "S = {−4; −4/5}", "S = {−4/5}", "S = ℝ"], "correct": 0},
                "answer": "S = ∅",
            },
            {
                "prompt": "c) S de i) =",
                "check": {"type": "choice", "options": ["S = {−36; 24}", "S = {24}", "S = {−24; 36}", "S = {−12; 8}"], "correct": 0},
                "answer": "S = {−36; 24}",
            },
        ],
        "hints": [
            "Primero aislá el módulo. Si queda igualado a un número NEGATIVO, no hay solución.",
        ],
        "solution": [
            "**b)** `−|x + 1/6| = −3 − 1/2 = −7/2` → `|x + 1/6| = 7/2`.",
            "`x + 1/6 = 7/2` → `x = 10/3`; `x + 1/6 = −7/2` → `x = −11/3`. `S = {−11/3; 10/3}`.",
            "**g)** `|(5/4)x + 3| = 8 − 10 = −2`. Un valor absoluto nunca es negativo: `S = ∅`.",
            "**i)** `|x/3 + 2| = 10` → `x/3 + 2 = 10` (x = 24) o `x/3 + 2 = −10` (x = −36). `S = {−36; 24}`.",
        ],
    },
    {
        "id": "al-modulo-ecuaciones-inecuaciones-tp3-21",
        "node": _M,
        "kind": "problem",
        "level": 3,
        "source": "Matemática · TP3, ej. 21 (a, c, d)",
        "title": "Módulo igualado a una expresión con x",
        "statement": "Resolvé las siguientes ecuaciones modulares.\na) `3 · |x − 1| + 2 = 5 − x`\nc) `5 · |3x − 1| = 6x − 5`\nd) `|x + 1| = 2x − 3`",
        "parts": [
            {
                "prompt": "a) S de a) =",
                "check": {"type": "choice", "options": ["S = {0; 3/2}", "S = {3/2}", "S = {0}", "S = {−3/2; 0}"], "correct": 0},
                "answer": "S = {0; 3/2}",
            },
            {
                "prompt": "b) S de c) =",
                "check": {"type": "choice", "options": ["S = ∅", "S = {0; 10/21}", "S = {10/21}", "S = {0}"], "correct": 0},
                "answer": "S = ∅",
            },
            {
                "prompt": "c) S de d) =",
                "check": {"type": "choice", "options": ["S = {4}", "S = {2/3; 4}", "S = {2/3}", "S = ∅"], "correct": 0},
                "answer": "S = {4}",
            },
        ],
        "hints": [
            "Como el módulo es ≥ 0, el otro miembro también tiene que serlo: eso da una condición sobre x.",
            "Separá en dos casos según el signo de lo que está dentro del módulo y quedate solo con los valores que cumplan la condición de cada caso.",
        ],
        "solution": [
            "**a)** `3|x − 1| = 3 − x` (exige `x ≤ 3`). Si `x ≥ 1`: `3x − 3 = 3 − x` → `x = 3/2` ✓. Si `x < 1`: `−3x + 3 = 3 − x` → `x = 0` ✓. `S = {0; 3/2}`.",
            "**c)** Exige `6x − 5 ≥ 0`, o sea `x ≥ 5/6`. Si `x ≥ 1/3`: `15x − 5 = 6x − 5` → `x = 0`, que no cumple `x ≥ 1/3`.",
            "Si `x < 1/3`: `−15x + 5 = 6x − 5` → `x = 10/21 ≈ 0,48`, que no cumple `x < 1/3`. Ninguno sirve: `S = ∅`.",
            "**d)** Exige `2x − 3 ≥ 0` (x ≥ 3/2). Si `x ≥ −1`: `x + 1 = 2x − 3` → `x = 4` ✓.",
            "Si `x < −1`: `−x − 1 = 2x − 3` → `x = 2/3`, que no es menor que −1 (y además da `|2/3 + 1| = 5/3` contra `2 · 2/3 − 3 = −5/3`). `S = {4}`.",
        ],
    },
    {
        "id": "al-exponentes-radicales-tp3-22a",
        "node": "al-exponentes-radicales",
        "kind": "problem",
        "level": 1,
        "source": "Matemática · TP3, ej. 22 (a, b, c)",
        "title": "Ecuaciones con potencias",
        "statement": "Resolvé las siguientes ecuaciones. Verificá.\na) `(x + 3)² = 169`\nb) `(x − 1)⁶ − 4 = 60`\nc) `(x + 5)³ − 23 = 102`",
        "parts": [
            {
                "prompt": "a) S =",
                "check": {"type": "choice", "options": ["S = {−16; 10}", "S = {10}", "S = {−10; 16}", "S = {−16; −10}"], "correct": 0},
                "answer": "S = {−16; 10}",
            },
            {
                "prompt": "b) S =",
                "check": {"type": "choice", "options": ["S = {−1; 3}", "S = {3}", "S = {−3; 1}", "S = {−1; 1}"], "correct": 0},
                "answer": "S = {−1; 3}",
            },
            {
                "prompt": "c) x = (respondé solo con el número)",
                "check": {"type": "numeric", "value": 0, "tolerance": 0, "unit": ""},
                "answer": "0",
            },
        ],
        "hints": [
            "Dejá la potencia sola y aplicá la raíz del mismo índice.",
            "Con índice PAR hay dos raíces opuestas (`√(u²) = |u|`); con índice impar hay una sola.",
        ],
        "solution": [
            "**a)** `|x + 3| = 13` → `x + 3 = 13` (x = 10) o `x + 3 = −13` (x = −16). `S = {−16; 10}`.",
            "**b)** `(x − 1)⁶ = 64` → `|x − 1| = ⁶√64 = 2` → `x = 3` o `x = −1`. `S = {−1; 3}`.",
            "Verificación b): `(3 − 1)⁶ = 64` y `(−1 − 1)⁶ = 64` ✓.",
            "**c)** `(x + 5)³ = 125` → `x + 5 = ∛125 = 5` → `x = 0` (índice impar: una sola solución).",
        ],
    },
    {
        "id": "al-exponentes-radicales-tp3-22e",
        "node": "al-exponentes-radicales",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP3, ej. 22 (e, f, k)",
        "title": "Ecuaciones con raíces",
        "statement": "Resolvé las siguientes ecuaciones. Verificá.\ne) `2 · √(x + 4) − 3 = 9`\nf) `(4 · √(20x) + 20)/4 = 15` (la raíz abarca solo a 20x)\nk) `(√45 − √(10x))/(−2) = (1/2)√5`",
        "parts": [
            {
                "prompt": "a) x en e) =",
                "check": {"type": "numeric", "value": 32, "tolerance": 0, "unit": ""},
                "answer": "32",
            },
            {
                "prompt": "b) x en f) =",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                "answer": "5",
            },
            {
                "prompt": "c) x en k) =",
                "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": ""},
                "answer": "8",
            },
        ],
        "hints": [
            "Despejá la raíz paso a paso (sumando, multiplicando…) y recién al final elevá al cuadrado.",
            "En k) usá `√45 = 3√5`.",
        ],
        "solution": [
            "**e)** `2√(x + 4) = 12` → `√(x + 4) = 6` → `x + 4 = 36` → `x = 32`. Verificación: `2 · 6 − 3 = 9` ✓.",
            "**f)** `4√(20x) + 20 = 60` → `4√(20x) = 40` → `√(20x) = 10` → `20x = 100` → `x = 5`.",
            "**k)** Multiplicamos por −2: `√45 − √(10x) = −√5` → `√(10x) = 3√5 + √5 = 4√5`.",
            "Elevando al cuadrado: `10x = 16 · 5 = 80` → `x = 8`. Verificación: `(3√5 − 4√5)/(−2) = √5/2` ✓.",
        ],
    },
    {
        "id": "al-exponentes-radicales-tp3-22h",
        "node": "al-exponentes-radicales",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP3, ej. 22 (h, i, l)",
        "title": "Raíces con fracciones y potencias de raíces",
        "statement": "Resolvé las siguientes ecuaciones. Verificá.\nh) `√(7x² − 1/3) = 2/3`\ni) `√((47/12)x² − 5/12) = 3/4`\nl) `(√(x + 5))³ − 7 = 20`",
        "parts": [
            {
                "prompt": "a) S de h) =",
                "check": {"type": "choice", "options": ["S = {−1/3; 1/3}", "S = {1/3}", "S = {−1/9; 1/9}", "S = ∅"], "correct": 0},
                "answer": "S = {−1/3; 1/3}",
            },
            {
                "prompt": "b) S de i) =",
                "check": {"type": "choice", "options": ["S = {−1/2; 1/2}", "S = {1/2}", "S = {−1/4; 1/4}", "S = ∅"], "correct": 0},
                "answer": "S = {−1/2; 1/2}",
            },
            {
                "prompt": "c) x en l) =",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4",
            },
        ],
        "hints": [
            "Elevá al cuadrado ambos miembros para sacar la raíz y despejá x².",
            "`x² = k` (k > 0) tiene dos soluciones: `x = ±√k`.",
        ],
        "solution": [
            "**h)** `7x² − 1/3 = 4/9` → `7x² = 4/9 + 3/9 = 7/9` → `x² = 1/9` → `x = ±1/3`.",
            "**i)** `(47/12)x² − 5/12 = 9/16` → `(47/12)x² = 27/48 + 20/48 = 47/48` → `x² = 47/48 · 12/47 = 1/4` → `x = ±1/2`.",
            "**l)** `(√(x + 5))³ = 27` → `√(x + 5) = ∛27 = 3` → `x + 5 = 9` → `x = 4`.",
            "Verificación l): `(√9)³ − 7 = 27 − 7 = 20` ✓.",
        ],
    },
    {
        "id": "al-cuadratica-formas-tp3-14-16",
        "node": "al-cuadratica-formas",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP3, ej. 14 y 16",
        "title": "Discriminante nulo: raíces repetidas",
        "statement": "Ejercicio 14: ¿para qué valores de m la ecuación tiene soluciones reales repetidas?\na) `2x² + mx − m = 0`\nb) `mx² − 3x + 9 = 0`\nEjercicio 16: dada la ecuación `x² − (m + 2)x + 10 = 0`, hallá el valor o los valores de m para los cuales la ecuación tiene dos raíces iguales.",
        "parts": [
            {
                "prompt": "a) Ej. 14 a):",
                "check": {"type": "choice", "options": ["m = 0 o m = −8", "m = −8", "m = 0 o m = 8", "m = 8"], "correct": 0},
                "answer": "m = 0 o m = −8",
            },
            {
                "prompt": "b) Ej. 14 b): m = (como fracción)",
                "check": {"type": "numeric", "value": 0.25, "tolerance": 0.001, "unit": ""},
                "answer": "1/4",
            },
            {
                "prompt": "c) Ej. 16:",
                "check": {"type": "choice", "options": ["m = −2 + 2√10 o m = −2 − 2√10", "m = 2 + 2√10 o m = 2 − 2√10", "m = −2 + √10 o m = −2 − √10", "m = 8 o m = −12"], "correct": 0},
                "answer": "m = −2 + 2√10 o m = −2 − 2√10",
            },
        ],
        "hints": [
            "En `ax² + bx + c = 0` las raíces son reales e iguales cuando `Δ = b² − 4ac = 0`.",
            "En 14 b) el coeficiente principal es m: tiene que ser distinto de 0 para que la ecuación sea cuadrática.",
        ],
        "solution": [
            "**14 a)** `Δ = m² − 4 · 2 · (−m) = m² + 8m = m(m + 8) = 0` → `m = 0` o `m = −8`.",
            "Con m = 0 queda `2x² = 0` (raíz doble x = 0) y con m = −8 queda `2x² − 8x + 8 = 2(x − 2)² = 0` (raíz doble x = 2).",
            "**14 b)** `Δ = 9 − 4 · m · 9 = 9 − 36m = 0` → `m = 1/4` (≠ 0, sirve). Queda `(1/4)x² − 3x + 9 = (1/4)(x − 6)² = 0`.",
            "**16)** `Δ = (m + 2)² − 40 = 0` → `(m + 2)² = 40` → `m + 2 = ±√40 = ±2√10`.",
            "`m = −2 + 2√10 ≈ 4,32` o `m = −2 − 2√10 ≈ −8,32`.",
        ],
    },
    {
        "id": "al-cuadratica-formas-tp3-15",
        "node": "al-cuadratica-formas",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP3, ej. 15",
        "title": "Discriminante positivo: raíces distintas",
        "statement": "¿Para qué valores de m la ecuación tiene soluciones reales distintas?\na) `x² + 6x − m = 0`\nb) `mx² + 5x − 5 = 0`",
        "parts": [
            {
                "prompt": "a) m ∈",
                "check": {"type": "choice", "options": ["(−9; ∞)", "(−∞; −9)", "(9; ∞)", "[−9; ∞)"], "correct": 0},
                "answer": "(−9; ∞)",
            },
            {
                "prompt": "b) m ∈",
                "check": {"type": "choice", "options": ["(−5/4; 0) ∪ (0; ∞)", "(−5/4; ∞)", "(−∞; −5/4)", "(5/4; ∞)"], "correct": 0},
                "answer": "(−5/4; 0) ∪ (0; ∞)",
            },
        ],
        "hints": [
            "Dos raíces reales distintas ⇔ `Δ > 0`.",
            "Si m multiplica a x², excluí m = 0: la ecuación dejaría de ser cuadrática y tendría una sola raíz.",
        ],
        "solution": [
            "**a)** `Δ = 36 − 4 · 1 · (−m) = 36 + 4m > 0` → `m > −9`. `m ∈ (−9; ∞)`.",
            "**b)** `Δ = 25 − 4 · m · (−5) = 25 + 20m > 0` → `m > −5/4`.",
            "Además `m ≠ 0`: con m = 0 queda `5x − 5 = 0`, lineal, con una sola solución.",
            "`m ∈ (−5/4; 0) ∪ (0; ∞)`.",
        ],
    },
    {
        "id": "al-cuadratica-formas-tp3-18-19",
        "node": "al-cuadratica-formas",
        "kind": "problem",
        "level": 3,
        "source": "Matemática · TP3, ej. 18 y 19 (b, c)",
        "title": "Triángulos que llevan a una cuadrática",
        "statement": "Ejercicio 19 b): las longitudes de los lados de un triángulo isósceles ABC, expresadas en cm, están dadas por `AB = 15 − 3x`, `BC = x² − 1` y `CA = 12 − 2x`, y su perímetro es 20 cm. Calculá la longitud de cada lado.\nEjercicio 19 c): la hipotenusa de un triángulo rectángulo mide 26 cm. Uno de los catetos es 14 cm más largo que el otro. Calculá las longitudes de los catetos.\nEjercicio 18: en un triángulo ABC rectángulo en B, los catetos miden `BC = x + 2` y `BA = 4x`, y la hipotenusa `CA = 4x + 1` (en cm). Calculá el perímetro y el área.",
        "parts": [
            {
                "prompt": "a) Ej. 19 b): longitud del lado BC, en cm.",
                "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": "cm"},
                "answer": "8 cm (AB = CA = 6 cm)",
            },
            {
                "prompt": "b) Ej. 19 c): cateto menor, en cm.",
                "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": "cm"},
                "answer": "10 cm (el otro mide 24 cm)",
            },
            {
                "prompt": "c) Ej. 18: ¿qué perímetro y área puede tener el triángulo?",
                "check": {"type": "choice", "options": ["12 cm y 6 cm², o bien 30 cm y 30 cm²", "Solo 12 cm y 6 cm²", "Solo 30 cm y 30 cm²", "Ningún valor de x da un triángulo"], "correct": 0},
                "answer": "12 cm y 6 cm², o bien 30 cm y 30 cm²",
            },
        ],
        "hints": [
            "En 19 b) planteá la suma de los tres lados igual a 20 y descartá la raíz que no da un triángulo isósceles.",
            "En 19 c) y en 18, aplicá Pitágoras y resolvé la cuadrática; descartá las longitudes negativas.",
        ],
        "solution": [
            "**19 b)** `(15 − 3x) + (x² − 1) + (12 − 2x) = 20` → `x² − 5x + 6 = 0` → `x = 2` o `x = 3`.",
            "Con x = 2 los lados son 9, 3 y 8 (no es isósceles: se descarta). Con x = 3: `AB = 6`, `BC = 8`, `CA = 6` ✓.",
            "**19 c)** Catetos a y a + 14: `a² + (a + 14)² = 26²` → `2a² + 28a − 480 = 0` → `a² + 14a − 240 = 0` → `a = 10` (la otra raíz, −24, no sirve). Catetos: 10 cm y 24 cm.",
            "**18)** `(x + 2)² + (4x)² = (4x + 1)²` → `x² + 4x + 4 + 16x² = 16x² + 8x + 1` → `x² − 4x + 3 = 0` → `x = 1` o `x = 3`.",
            "Las dos sirven: x = 1 da lados 3, 4, 5 (perímetro 12 cm, área `3 · 4/2 = 6 cm²`); x = 3 da 5, 12, 13 (perímetro 30 cm, área `5 · 12/2 = 30 cm²`).",
        ],
    },
    {
        "id": "al-formas-lineales-tp3-32a",
        "node": "al-formas-lineales",
        "kind": "problem",
        "level": 1,
        "source": "Matemática · TP3, ej. 32 (a, b, d)",
        "title": "Rectas paralelas y perpendiculares (1)",
        "statement": "Encontrá la ecuación de las siguientes rectas.\na) Paralela a `x + y + 2 = 0` y que pasa por el punto (0; 2).\nb) Perpendicular a `3x + 2y − 5 = 0` y que pasa por el punto (3; 3).\nd) Perpendicular a `3x − 6y + 2 = 0` y que pasa por (1; −1).",
        "parts": [
            {
                "prompt": "a) Recta a):",
                "check": {"type": "choice", "options": ["y = −x + 2", "y = x + 2", "y = −x − 2", "y = 2x"], "correct": 0},
                "answer": "y = −x + 2",
            },
            {
                "prompt": "b) Recta b):",
                "check": {"type": "choice", "options": ["y = (2/3)x + 1", "y = −(3/2)x + 15/2", "y = (2/3)x + 3", "y = −(2/3)x + 5"], "correct": 0},
                "answer": "y = (2/3)x + 1",
            },
            {
                "prompt": "c) Recta d):",
                "check": {"type": "choice", "options": ["y = −2x + 1", "y = (1/2)x − 3/2", "y = 2x − 3", "y = −2x − 1"], "correct": 0},
                "answer": "y = −2x + 1",
            },
        ],
        "hints": [
            "Despejá y en la recta dada para leer su pendiente.",
            "Paralelas: misma pendiente. Perpendiculares: `m₁ · m₂ = −1` (pendiente opuesta e inversa).",
            "Con la pendiente y un punto usá `y − y₀ = m(x − x₀)`.",
        ],
        "solution": [
            "**a)** `x + y + 2 = 0` → `y = −x − 2`, pendiente −1. Paralela por (0; 2): la ordenada al origen es 2 → `y = −x + 2`.",
            "**b)** `3x + 2y − 5 = 0` → `y = −(3/2)x + 5/2`, pendiente −3/2. Perpendicular: `m = 2/3`.",
            "Por (3; 3): `y − 3 = (2/3)(x − 3)` → `y = (2/3)x − 2 + 3` → `y = (2/3)x + 1`.",
            "**d)** `3x − 6y + 2 = 0` → `y = (1/2)x + 1/3`, pendiente 1/2. Perpendicular: `m = −2`.",
            "Por (1; −1): `y + 1 = −2(x − 1)` → `y = −2x + 1`.",
        ],
    },
    {
        "id": "al-formas-lineales-tp3-32i",
        "node": "al-formas-lineales",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP3, ej. 32 (i, j) y 33",
        "title": "Rectas paralelas y perpendiculares (2)",
        "statement": "Ejercicio 32:\ni) Perpendicular a la recta que pasa por los puntos A(0; 2) y B(3; 1), y que pasa por (−3; 3).\nj) Paralela a la recta que pasa por los puntos A(−1; 2) y B(1; −1), y que pasa por (1; 3).\nEjercicio 33: determiná el valor de t para que las rectas `r: 3x − 4y + 12 = 0` y `s: tx + 8y − 15 = 0` sean perpendiculares.",
        "parts": [
            {
                "prompt": "a) Recta i):",
                "check": {"type": "choice", "options": ["y = 3x + 12", "y = −(1/3)x + 2", "y = 3x − 6", "y = −3x − 6"], "correct": 0},
                "answer": "y = 3x + 12",
            },
            {
                "prompt": "b) Recta j):",
                "check": {"type": "choice", "options": ["y = −(3/2)x + 9/2", "y = (2/3)x + 7/3", "y = −(3/2)x + 3", "y = −(2/3)x + 11/3"], "correct": 0},
                "answer": "y = −(3/2)x + 9/2",
            },
            {
                "prompt": "c) Ej. 33: t = (como fracción)",
                "check": {"type": "numeric", "value": 10.666667, "tolerance": 0.001, "unit": ""},
                "answer": "32/3",
            },
        ],
        "hints": [
            "Pendiente por dos puntos: `m = (y₂ − y₁)/(x₂ − x₁)`.",
            "En el 33 despejá y en cada recta: la pendiente de s depende de t.",
        ],
        "solution": [
            "**i)** `m_AB = (1 − 2)/(3 − 0) = −1/3`; perpendicular: `m = 3`. Por (−3; 3): `y − 3 = 3(x + 3)` → `y = 3x + 12`.",
            "**j)** `m_AB = (−1 − 2)/(1 − (−1)) = −3/2`; paralela: misma pendiente. Por (1; 3): `y − 3 = −(3/2)(x − 1)` → `y = −(3/2)x + 9/2`.",
            "**33)** `r: y = (3/4)x + 3`, pendiente 3/4. `s: y = −(t/8)x + 15/8`, pendiente −t/8.",
            "Perpendiculares: `(3/4) · (−t/8) = −1` → `3t/32 = 1` → `t = 32/3`.",
        ],
    },
    {
        "id": "p-plano-rectas-tp3-32c",
        "node": "p-plano-rectas",
        "kind": "problem",
        "level": 1,
        "source": "Matemática · TP3, ej. 32 (c, e, g)",
        "title": "Rectas horizontales y verticales",
        "statement": "Encontrá la ecuación de las siguientes rectas.\nc) Paralela al eje de abscisas y que pasa por el punto (2; −2).\ne) Paralela a `x = 5` y que pasa por el punto (2; −2).\ng) Perpendicular a `y = −3` y que pasa por el punto (−2; 7).",
        "parts": [
            {
                "prompt": "a) Recta c):",
                "check": {"type": "choice", "options": ["y = −2", "x = 2", "y = x − 4", "x = −2"], "correct": 0},
                "answer": "y = −2",
            },
            {
                "prompt": "b) Recta e):",
                "check": {"type": "choice", "options": ["x = 2", "y = −2", "x = 5", "y = 5"], "correct": 0},
                "answer": "x = 2",
            },
            {
                "prompt": "c) Recta g):",
                "check": {"type": "choice", "options": ["x = −2", "y = 7", "y = −3", "x = 7"], "correct": 0},
                "answer": "x = −2",
            },
        ],
        "hints": [
            "Una recta horizontal tiene todos sus puntos con la misma ordenada: `y = constante`.",
            "Una recta vertical (como `x = 5`) tiene todos sus puntos con la misma abscisa: `x = constante`.",
        ],
        "solution": [
            "**c)** Paralela al eje x es horizontal: `y = k`. Como pasa por (2; −2), `y = −2`.",
            "**e)** `x = 5` es vertical; una paralela también lo es: `x = k`. Por (2; −2): `x = 2`.",
            "**g)** `y = −3` es horizontal; su perpendicular es vertical. Por (−2; 7): `x = −2`.",
            "Error típico: usar la ordenada del punto en una recta vertical (escribir `x = 7` en g).",
        ],
    },
    {
        "id": "al-sel-metodos-clasificacion-tp3-40",
        "node": "al-sel-metodos-clasificacion",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP3, ej. 40",
        "title": "Clasificar un sistema según el parámetro k",
        "statement": "Dado el sistema `{ kx + y = 2 ; 2x + 2y = 2k }`, determiná, si es que existe, el o los valores del parámetro k para que el sistema sea:\na) Compatible determinado\nb) Compatible indeterminado\nc) Incompatible",
        "parts": [
            {
                "prompt": "a) Compatible determinado:",
                "check": {"type": "choice", "options": ["k ≠ 1", "k = 1", "Para ningún valor de k", "Para todo k real"], "correct": 0},
                "answer": "k ≠ 1",
            },
            {
                "prompt": "b) Compatible indeterminado:",
                "check": {"type": "choice", "options": ["k ≠ 1", "k = 1", "Para ningún valor de k", "Para todo k real"], "correct": 2},
                "answer": "Para ningún valor de k",
            },
            {
                "prompt": "c) Incompatible:",
                "check": {"type": "choice", "options": ["k ≠ 1", "k = 1", "Para ningún valor de k", "Para todo k real"], "correct": 1},
                "answer": "k = 1",
            },
        ],
        "hints": [
            "Despejá y en las dos ecuaciones y compará pendientes: si son distintas, el sistema es compatible determinado.",
            "Si las pendientes son iguales, compará las ordenadas al origen: iguales → infinitas soluciones; distintas → ninguna.",
        ],
        "solution": [
            "Despejando: `y = −kx + 2` y `y = −x + k`.",
            "Las rectas se cortan en un punto si las pendientes son distintas: `−k ≠ −1`, es decir `k ≠ 1` → **compatible determinado**.",
            "Si `k = 1`: las rectas son `y = −x + 2` e `y = −x + 1`, paralelas con distinta ordenada → **incompatible**.",
            "Para que fueran la misma recta haría falta `k = 1` y a la vez `2 = k`, imposible: no hay valor de k que lo haga **compatible indeterminado**.",
        ],
    },
    {
        "id": "al-sel-metodos-clasificacion-tp3-41",
        "node": "al-sel-metodos-clasificacion",
        "kind": "problem",
        "level": 3,
        "source": "Matemática · TP3, ej. 41",
        "title": "Clasificar un sistema con dos parámetros",
        "statement": "Determiná qué valores deben tomar los parámetros a y b para que el sistema `{ ax + y = 2 ; 2x + 2y = b }` sea:\na) Compatible determinado\nb) Compatible indeterminado\nc) Incompatible",
        "parts": [
            {
                "prompt": "a) Compatible determinado:",
                "check": {"type": "choice", "options": ["a ≠ 1 (b cualquiera)", "a = 1 y b = 4", "a = 1 y b ≠ 4", "Para ningún valor de a y b"], "correct": 0},
                "answer": "a ≠ 1 (b cualquiera)",
            },
            {
                "prompt": "b) Compatible indeterminado:",
                "check": {"type": "choice", "options": ["a ≠ 1 (b cualquiera)", "a = 1 y b = 4", "a = 1 y b ≠ 4", "Para ningún valor de a y b"], "correct": 1},
                "answer": "a = 1 y b = 4",
            },
            {
                "prompt": "c) Incompatible:",
                "check": {"type": "choice", "options": ["a ≠ 1 (b cualquiera)", "a = 1 y b = 4", "a = 1 y b ≠ 4", "Para ningún valor de a y b"], "correct": 2},
                "answer": "a = 1 y b ≠ 4",
            },
        ],
        "hints": [
            "Escribí las dos rectas en forma explícita: la pendiente depende solo de a y la ordenada de la segunda, de b.",
        ],
        "solution": [
            "Despejando: `y = −ax + 2` y `y = −x + b/2`.",
            "Si `−a ≠ −1`, o sea `a ≠ 1`, las pendientes son distintas: **compatible determinado**, sin importar b.",
            "Si `a = 1`, las dos rectas tienen pendiente −1. Son la misma recta cuando además `2 = b/2`, o sea `b = 4`: **compatible indeterminado**.",
            "Si `a = 1` y `b ≠ 4`: rectas paralelas distintas, **incompatible**.",
        ],
    },
    {
        "id": "al-sel-metodos-clasificacion-tp3-43a",
        "node": "al-sel-metodos-clasificacion",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP3, ej. 43 (a, b, c)",
        "title": "Resolver sistemas 2×2 (1)",
        "statement": "Resolvé los siguientes sistemas por el método que prefieras. Verificá.\na) `{ (2/3)x − 5y = −3 ; 2x = 13/2 − (1/2)y }`\nb) `{ 4x − 2(y + 9) = 0 ; 3x + y − 1 = 0 }`\nc) `{ (5/2)x − y − 2 = 0 ; 2x + 8y − 6 = 0 }`",
        "parts": [
            {
                "prompt": "a) S =",
                "check": {"type": "choice", "options": ["S = {(3; 1)}", "S = {(1; 3)}", "S = {(−3; 1)}", "S = {(3; −1)}"], "correct": 0},
                "answer": "S = {(3; 1)}",
            },
            {
                "prompt": "b) S =",
                "check": {"type": "choice", "options": ["S = {(2; −5)}", "S = {(−5; 2)}", "S = {(2; 5)}", "S = {(1; −2)}"], "correct": 0},
                "answer": "S = {(2; −5)}",
            },
            {
                "prompt": "c) S =",
                "check": {"type": "choice", "options": ["S = {(1; 1/2)}", "S = {(1/2; 1)}", "S = {(1; −1/2)}", "S = {(2; 3)}"], "correct": 0},
                "answer": "S = {(1; 1/2)}",
            },
        ],
        "hints": [
            "Si una ecuación permite despejar fácil una incógnita (como y en b o en c), usá sustitución.",
            "Con fracciones, conviene multiplicar cada ecuación por el mcm de sus denominadores antes de empezar.",
        ],
        "solution": [
            "**a)** Multiplicando: la primera por 3 → `2x − 15y = −9`; la segunda por 2 → `4x + y = 13` → `y = 13 − 4x`.",
            "Sustituyendo: `2x − 15(13 − 4x) = −9` → `62x = 186` → `x = 3`, `y = 1`. Verificación: `2 − 5 = −3` ✓ y `6 = 6,5 − 0,5` ✓.",
            "**b)** De la segunda: `y = 1 − 3x`. En la primera: `4x − 2(10 − 3x) = 0` → `10x = 20` → `x = 2`, `y = −5`.",
            "**c)** De la primera: `y = (5/2)x − 2`. En la segunda: `2x + 20x − 16 − 6 = 0` → `22x = 22` → `x = 1`, `y = 1/2`.",
            "Verificación c): `2 + 4 − 6 = 0` ✓.",
        ],
    },
    {
        "id": "al-sel-metodos-clasificacion-tp3-43d",
        "node": "al-sel-metodos-clasificacion",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP3, ej. 43 (d, e, f)",
        "title": "Resolver sistemas 2×2 (2)",
        "statement": "Resolvé los siguientes sistemas. Verificá.\nd) `{ 4x − 5y = 7 ; −x + 10y = 0 }`\ne) `{ (6x − 8)/2 − y = 0 ; 2x − y = 0 }`\nf) `{ x/3 + (2x − y)/6 = x ; (5/2)x + (1/2)y = −7/2 }`",
        "parts": [
            {
                "prompt": "a) S de d) =",
                "check": {"type": "choice", "options": ["S = {(2; 1/5)}", "S = {(1/5; 2)}", "S = {(2; −1/5)}", "S = {(7/4; 0)}"], "correct": 0},
                "answer": "S = {(2; 1/5)}",
            },
            {
                "prompt": "b) S de e) =",
                "check": {"type": "choice", "options": ["S = {(4; 8)}", "S = {(8; 4)}", "S = {(−4; −8)}", "S = {(4/3; 8/3)}"], "correct": 0},
                "answer": "S = {(4; 8)}",
            },
            {
                "prompt": "c) S de f) =",
                "check": {"type": "choice", "options": ["S = {(−7/3; 14/3)}", "S = {(7/3; −14/3)}", "S = {(14/3; −7/3)}", "S = {(−1; 2)}"], "correct": 0},
                "answer": "S = {(−7/3; 14/3)}",
            },
        ],
        "hints": [
            "En d) despejá x de la segunda ecuación; en e) las dos ecuaciones tienen y despejada: igualá.",
            "En f) multiplicá la primera ecuación por 6 y simplificá antes de resolver.",
        ],
        "solution": [
            "**d)** De la segunda: `x = 10y`. En la primera: `40y − 5y = 7` → `y = 1/5`, `x = 2`.",
            "**e)** La primera queda `y = 3x − 4` y la segunda `y = 2x`. Igualando: `3x − 4 = 2x` → `x = 4`, `y = 8`.",
            "**f)** Primera por 6: `2x + 2x − y = 6x` → `y = −2x`. Segunda por 2: `5x + y = −7`.",
            "Sustituyendo: `5x − 2x = −7` → `x = −7/3`, `y = 14/3`.",
            "Verificación f): `(5/2)(−7/3) + (1/2)(14/3) = −35/6 + 14/6 = −21/6 = −7/2` ✓.",
        ],
    },
    {
        "id": "p-sistemas-ecuaciones-tp3-45a",
        "node": "p-sistemas-ecuaciones",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP3, ej. 45 (a, b, c)",
        "title": "Plantear sistemas: números y camiones",
        "statement": "En cada problema identificá las incógnitas, planteá el sistema y resolvelo.\na) La suma de dos números positivos es el doble de su diferencia. El número más grande es 6 más que el doble del más pequeño. ¿Cuáles son dichos números?\nb) Hallá un número de dos cifras sabiendo que la suma de las cifras es 12 y que la primera de ellas es el triple de la segunda.\nc) Con dos camiones cuyas capacidades de carga son respectivamente de 3 y 4 toneladas, se hicieron en total 23 viajes para transportar 80 toneladas de madera. ¿Cuántos viajes realizó cada camión?",
        "parts": [
            {
                "prompt": "a) El número más grande:",
                "check": {"type": "numeric", "value": 18, "tolerance": 0, "unit": ""},
                "answer": "18 (el otro es 6)",
            },
            {
                "prompt": "b) El número de dos cifras:",
                "check": {"type": "numeric", "value": 93, "tolerance": 0, "unit": ""},
                "answer": "93",
            },
            {
                "prompt": "c) Viajes del camión de 3 toneladas:",
                "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": "viajes"},
                "answer": "12 viajes (el de 4 t hizo 11)",
            },
        ],
        "hints": [
            "Escribí una ecuación por cada dato del enunciado: dos datos, dos ecuaciones.",
            "En c) una ecuación cuenta viajes y la otra cuenta toneladas (3 por viaje en un camión, 4 en el otro).",
        ],
        "solution": [
            "**a)** Mayor a, menor b: `a + b = 2(a − b)` → `a = 3b`; y `a = 2b + 6`. Igualando: `3b = 2b + 6` → `b = 6`, `a = 18`.",
            "Control: `18 + 6 = 24 = 2 · 12` ✓.",
            "**b)** Cifras p (decenas) y s (unidades): `p + s = 12` y `p = 3s` → `4s = 12` → `s = 3`, `p = 9`. El número es 93.",
            "**c)** x viajes del de 3 t e y del de 4 t: `x + y = 23` y `3x + 4y = 80`.",
            "De la primera `x = 23 − y`: `69 − 3y + 4y = 80` → `y = 11`, `x = 12`. Control: `36 + 44 = 80` ✓.",
        ],
    },
    {
        "id": "p-sistemas-ecuaciones-tp3-45d",
        "node": "p-sistemas-ecuaciones",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP3, ej. 45 (d, e)",
        "title": "Plantear sistemas: edades y mezcla de café",
        "statement": "d) La edad de Camila y la de su mamá suman 54 años y dentro de 9 años la edad de la mamá será el doble de la edad de Camila. ¿Cuántos años tiene cada una?\ne) Un cliente compra en una cafetería una mezcla de dos clases de café: café A, que cuesta 3,50 dólares el kilo, y café B, que cuesta 5,60 dólares el kilo. Si compra 3 kilos de la mezcla, que le cuestan 11,55 dólares, ¿cuántos gramos de cada clase de café entraron en la mezcla?",
        "parts": [
            {
                "prompt": "a) Edad actual de Camila, en años.",
                "check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": "años"},
                "answer": "15 años (la mamá tiene 39)",
            },
            {
                "prompt": "b) Gramos de café A en la mezcla.",
                "check": {"type": "numeric", "value": 2500, "tolerance": 0, "unit": "g"},
                "answer": "2500 g",
            },
            {
                "prompt": "c) Gramos de café B en la mezcla.",
                "check": {"type": "numeric", "value": 500, "tolerance": 0, "unit": "g"},
                "answer": "500 g",
            },
        ],
        "hints": [
            "Dentro de 9 años las dos edades aumentan 9.",
            "En la mezcla, una ecuación es de kilos (suman 3) y la otra de dinero (precio por kilo × kilos).",
        ],
        "solution": [
            "**d)** Camila c, mamá m: `c + m = 54` y `m + 9 = 2(c + 9)` → `m = 2c + 9`.",
            "Sustituyendo: `c + 2c + 9 = 54` → `c = 15`, `m = 39`. Control: dentro de 9 años, 48 = 2 · 24 ✓.",
            "**e)** a kilos de A y b de B: `a + b = 3` y `3,50a + 5,60b = 11,55`.",
            "Con `a = 3 − b`: `10,5 − 3,5b + 5,6b = 11,55` → `2,1b = 1,05` → `b = 0,5 kg`, `a = 2,5 kg`.",
            "En gramos: 2500 g de café A y 500 g de café B.",
        ],
    },
    {
        "id": "p-sistemas-ecuaciones-tp3-46a",
        "node": "p-sistemas-ecuaciones",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP3, ej. 46 (a, b)",
        "title": "Salmuera y edades en razón",
        "statement": "a) Una bióloga tiene dos soluciones de salmuera: una contiene 5% de sal y otra contiene 20% de sal. ¿Cuántos mililitros de cada solución debe mezclar para obtener 1 L = 1000 ml de una solución que contenga 14% de sal?\nb) ¿Cuáles son las edades de dos hermanos, sabiendo que la razón entre sus edades es 4 : 5 y dentro de 6 años la razón entre las mismas será 6 : 7?",
        "parts": [
            {
                "prompt": "a) Mililitros de la solución al 5%.",
                "check": {"type": "numeric", "value": 400, "tolerance": 0, "unit": "ml"},
                "answer": "400 ml (y 600 ml de la del 20%)",
            },
            {
                "prompt": "b) Edad del hermano menor, en años.",
                "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": "años"},
                "answer": "12 años",
            },
            {
                "prompt": "c) Edad del hermano mayor, en años.",
                "check": {"type": "numeric", "value": 15, "tolerance": 0, "unit": "años"},
                "answer": "15 años",
            },
        ],
        "hints": [
            "En la mezcla, la sal se conserva: `0,05x + 0,20y` tiene que ser el 14% de 1000 ml.",
            "Una razón `a : b = 4 : 5` se escribe como `5a = 4b`.",
        ],
        "solution": [
            "**a)** `x + y = 1000` y `0,05x + 0,20y = 0,14 · 1000 = 140`.",
            "Con `x = 1000 − y`: `50 − 0,05y + 0,20y = 140` → `0,15y = 90` → `y = 600`, `x = 400`.",
            "**b)** Menor a, mayor b: `a/b = 4/5` → `5a = 4b`; `(a + 6)/(b + 6) = 6/7` → `7a + 42 = 6b + 36` → `7a − 6b = −6`.",
            "Con `a = 4b/5`: `28b/5 − 6b = −6` → `−2b/5 = −6` → `b = 15`, `a = 12`.",
            "Control: 12/15 = 4/5 ✓ y 18/21 = 6/7 ✓.",
        ],
    },
    {
        "id": "p-sistemas-ecuaciones-tp3-46c",
        "node": "p-sistemas-ecuaciones",
        "kind": "problem",
        "level": 2,
        "source": "Matemática · TP3, ej. 46 (c, d)",
        "title": "Rectángulo agrandado y triángulo isósceles",
        "statement": "c) El perímetro de un rectángulo es de 40 metros. Si se duplica el largo del rectángulo y se aumenta en 6 metros el ancho, el perímetro queda en 76 metros. ¿Cuáles son las medidas originales del rectángulo y cuáles las del rectángulo agrandado?\nd) En un triángulo isósceles, los lados iguales miden 3 cm más que el otro lado. Si el perímetro del triángulo es de 48 cm, ¿cuánto mide cada lado del triángulo?",
        "parts": [
            {
                "prompt": "a) Largo original del rectángulo, en m.",
                "check": {"type": "numeric", "value": 12, "tolerance": 0, "unit": "m"},
                "answer": "12 m (ancho 8 m; agrandado: 24 m × 14 m)",
            },
            {
                "prompt": "b) Ancho del rectángulo agrandado, en m.",
                "check": {"type": "numeric", "value": 14, "tolerance": 0, "unit": "m"},
                "answer": "14 m",
            },
            {
                "prompt": "c) Medida de cada uno de los lados iguales del triángulo, en cm.",
                "check": {"type": "numeric", "value": 17, "tolerance": 0, "unit": "cm"},
                "answer": "17 cm (el lado distinto mide 14 cm)",
            },
        ],
        "hints": [
            "Perímetro de un rectángulo: `2 · (largo + ancho)`.",
            "En d) alcanza con una incógnita: el lado distinto b y los iguales b + 3.",
        ],
        "solution": [
            "**c)** Largo L y ancho A: `2(L + A) = 40` → `L + A = 20`; `2(2L + A + 6) = 76` → `2L + A = 32`.",
            "Restando: `L = 12`, entonces `A = 8`.",
            "Agrandado: largo `2 · 12 = 24 m` y ancho `8 + 6 = 14 m`. Control: `2(24 + 14) = 76` ✓.",
            "**d)** `b + 2(b + 3) = 48` → `3b + 6 = 48` → `b = 14`. Los lados iguales miden 17 cm y el distinto 14 cm.",
        ],
    },
    {
        "id": "g-trigonometria-tp3-48",
        "node": "g-trigonometria",
        "kind": "problem",
        "level": 3,
        "source": "Matemática · TP3, ej. 48",
        "title": "Torre de 18 m: ventana y distancia",
        "statement": "Una torre de 18 m de altura está situada a una distancia d de un edificio. Desde una ventana del edificio, ubicada a una altura h, un observador ve que el ángulo de elevación a la parte superior de la torre es 30° y que el ángulo de depresión de la parte inferior de la torre es 20°. ¿Cuál es la altura de la ventana? ¿Cuál es la distancia entre el edificio y la torre?",
        "parts": [
            {
                "prompt": "a) Distancia d entre el edificio y la torre, en m (redondeá a 0,01).",
                "check": {"type": "numeric", "value": 19.122, "tolerance": 0.002, "unit": "m"},
                "answer": "19,12 m",
            },
            {
                "prompt": "b) Altura h de la ventana, en m (redondeá a 0,01).",
                "check": {"type": "numeric", "value": 6.96, "tolerance": 0.002, "unit": "m"},
                "answer": "6,96 m",
            },
        ],
        "hints": [
            "La horizontal desde la ventana divide la torre en dos tramos: abajo mide h y arriba 18 − h.",
            "`h = d · tg 20°` y `18 − h = d · tg 30°`: sumalas para despejar d.",
        ],
        "solution": [
            "Tramo inferior (depresión 20°): `h = d · tg 20°`.",
            "Tramo superior (elevación 30°): `18 − h = d · tg 30°`.",
            "Sumando: `18 = d(tg 30° + tg 20°) = d(0,5774 + 0,3640) = 0,9413 d` → `d ≈ 19,12 m`.",
            "`h = 19,12 · tg 20° ≈ 19,12 · 0,3640 ≈ 6,96 m`.",
            "Control: `19,12 · tg 30° ≈ 11,04` y `6,96 + 11,04 = 18` ✓.",
        ],
    },
    {
        "id": "g-trigonometria-tp3-49",
        "node": "g-trigonometria",
        "kind": "problem",
        "level": 3,
        "source": "Matemática · TP3, ej. 49",
        "title": "Altura del faro con dos barcos alineados",
        "statement": "Desde el nivel del mar, observando desde la parte superior de un faro, los ángulos de depresión de dos barcos son de 30° y 45°. Si uno de los barcos se encuentra exactamente detrás del otro y la distancia entre ambos es de 20 m, ¿cuál es la altura del faro? ¿A qué distancia del faro se encuentra el primer barco (el más cercano)?",
        "parts": [
            {
                "prompt": "a) Altura del faro, en m (redondeá a 0,01).",
                "check": {"type": "numeric", "value": 27.32, "tolerance": 0.002, "unit": "m"},
                "answer": "27,32 m (exacto: 10(√3 + 1) m)",
            },
            {
                "prompt": "b) Distancia del faro al barco más cercano, en m (redondeá a 0,01).",
                "check": {"type": "numeric", "value": 27.32, "tolerance": 0.002, "unit": "m"},
                "answer": "27,32 m (el otro barco está a 47,32 m)",
            },
        ],
        "hints": [
            "El barco visto con 45° está más cerca; con 45° la distancia horizontal es igual a la altura h.",
            "El barco lejano está a `h / tg 30° = h√3`; la diferencia de las dos distancias es 20 m.",
        ],
        "solution": [
            "Llamamos h a la altura del faro. Barco cercano (45°): `d₁ = h / tg 45° = h`.",
            "Barco lejano (30°): `d₂ = h / tg 30° = h√3`.",
            "`d₂ − d₁ = 20` → `h(√3 − 1) = 20` → `h = 20/(√3 − 1) = 10(√3 + 1) ≈ 27,32 m`.",
            "El primer barco (el más cercano) está a `d₁ = h ≈ 27,32 m`; el segundo, a `27,32 + 20 = 47,32 m`. Si se entendiera «el primer barco» como el que se menciona primero (el de 30°), la respuesta sería 47,32 m.",
            "El enunciado no dice cuál es el \"primero\"; tomamos el más cercano al faro.",
        ],
    },
]
