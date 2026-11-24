"""Ejercicios de Lógica y lectura de teoremas para Comprensión Lectora y Resolución de Problemas.

Tema: cl-logica-enunciados (proposiciones, negación con cuantificadores, conectivos y tablas de
verdad, hipótesis y tesis, formas asociadas de un condicional, condiciones necesarias y suficientes,
y contraejemplos).
"""

from __future__ import annotations


def _ch(options: list[str], correct: int) -> dict:
    return {"type": "choice", "options": options, "correct": correct}


NODE = "cl-logica-enunciados"

EXERCISES: list[dict] = [
    {
        "id": "cl-logica-enunciados-1",
        "node": NODE,
        "kind": "problem",
        "level": 1,
        "title": "Proposiciones y negación con cuantificadores",
        "statement": (
            "Analizá los siguientes enunciados usando las definiciones de proposición y negación:\n\n"
            "• A: «¿Es 17 un número primo?»\n"
            "• B: «Resolvé la ecuación x² = 9.»\n"
            "• C: «2x − 1 = 7»\n"
            "• D: «Todo número impar es divisible por 3.»\n\n"
            "Luego negá dos afirmaciones cuantificadas."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál de los enunciados A, B, C o D es una proposición?",
                "check": _ch(
                    [
                        "D («Todo número impar es divisible por 3»)",
                        "C («2x − 1 = 7»)",
                        "A («¿Es 17 un número primo?»)",
                        "B («Resolvé la ecuación x² = 9»)",
                    ],
                    0,
                ),
                "answer": "D: es un enunciado declarativo con un valor de verdad definido (falso).",
            },
            {
                "prompt": "b) ¿Cuál es la negación de «Todos los múltiplos de 5 terminan en 5»?",
                "check": _ch(
                    [
                        "Existe al menos un múltiplo de 5 que no termina en 5.",
                        "Ningún múltiplo de 5 termina en 5.",
                        "Todos los múltiplos de 5 terminan en 0.",
                        "Algunos múltiplos de 5 terminan en 5.",
                    ],
                    0,
                ),
                "answer": "Existe al menos un múltiplo de 5 que no termina en 5.",
            },
            {
                "prompt": "c) ¿Cuál es la negación de «Existe al menos un número real x tal que x² < 0»?",
                "check": _ch(
                    [
                        "Para todo número real x, x² ≥ 0.",
                        "Para todo número real x, x² > 0.",
                        "Existe al menos un número real x tal que x² ≥ 0.",
                        "Para todo número real x, x² ≤ 0.",
                    ],
                    0,
                ),
                "answer": "Para todo número real x, x² ≥ 0.",
            },
        ],
        "hints": [
            "Una proposición puede ser falsa: lo que importa es que tenga un valor de verdad definido sin depender de una variable libre.",
            "Al negar un «para todo» aparece un «existe al menos uno que no…», y al negar un «existe» aparece un «para todo… no…».",
            "Lo contrario de `<` es `≥` (incluye la igualdad), no `>`.",
        ],
        "solution": [
            "a) A es una pregunta y B es una orden: no son verdaderas ni falsas. C (`2x − 1 = 7`) es una forma abierta porque depende del valor de `x` (es V para `x = 4` y F para `x = 1`).",
            "D es un enunciado declarativo cuantificado con valor de verdad único: es **falso** (por ejemplo, 5 es impar y no es divisible por 3), así que **sí es una proposición**.",
            "b) Negar `∀ x: P(x)` da `∃ x / ~P(x)`. Por eso la negación de «Todos los múltiplos de 5 terminan en 5» es «Existe al menos un múltiplo de 5 que no termina en 5» (verdadera: 10 es múltiplo de 5 y termina en 0).",
            "«Ninguno termina en 5» es demasiado fuerte (es falsa, igual que la original: 15 sí termina en 5) y «Algunos terminan en 5» no contradice a «Todos».",
            "c) Negar `∃ x ∈ IR / x² < 0` cambia `∃` por `∀` y niega `<` como `≥`: «Para todo número real x, x² ≥ 0». Poner `x² > 0` olvida el caso `x = 0`, donde `0² = 0`.",
        ],
    },
    {
        "id": "cl-logica-enunciados-2",
        "node": NODE,
        "kind": "problem",
        "level": 2,
        "title": "Conectivos lógicos y tablas de verdad",
        "statement": (
            "Considerá las siguientes proposiciones simples:\n\n"
            "• `p`: «12 es múltiplo de 4»\n"
            "• `q`: «√9 = −3»\n"
            "• `r`: «5 > 8»\n\n"
            "Determiná el valor de verdad de las proposiciones compuestas y una equivalencia de negación."
        ),
        "parts": [
            {
                "prompt": "a) ¿Cuál es el valor de verdad de `(p ∧ ~q) ⇒ r`?",
                "check": _ch(
                    [
                        "Falso, porque el antecedente `(p ∧ ~q)` es verdadero y el consecuente `r` es falso.",
                        "Verdadero, porque `q` y `r` son ambas falsas.",
                        "Verdadero, porque `p` es verdadera.",
                        "Falso, porque `p ∧ ~q` es falso.",
                    ],
                    0,
                ),
                "answer": "Falso: `p ∧ ~q` es V y `r` es F, el único caso falso de `⇒`.",
            },
            {
                "prompt": "b) ¿Cuál es el valor de verdad de `r ⇒ (p ∧ q)` y de `q ⇔ r`?",
                "check": _ch(
                    [
                        "Ambas son verdaderas.",
                        "`r ⇒ (p ∧ q)` es falsa y `q ⇔ r` es verdadera.",
                        "`r ⇒ (p ∧ q)` es verdadera y `q ⇔ r` es falsa.",
                        "Ambas son falsas.",
                    ],
                    0,
                ),
                "answer": "Ambas son verdaderas (`F ⇒ F` es V y `F ⇔ F` es V).",
            },
            {
                "prompt": "c) ¿Qué proposición es lógicamente equivalente a la negación `~(p ∧ ~q)`?",
                "check": _ch(
                    ["~p ∨ q", "~p ∧ q", "~p ∨ ~q", "p ∨ q"],
                    0,
                ),
                "answer": "~p ∨ q (por ley de De Morgan).",
            },
        ],
        "hints": [
            "Primero hallá los valores de verdad de `p`, `q` y `r` por separado. Recordá que el símbolo `√9` indica la raíz cuadrada principal (positiva).",
            "Un condicional `A ⇒ B` es falso únicamente cuando `A` es V y `B` es F; un bicondicional `A ⇔ B` es verdadero cuando ambos tienen el mismo valor.",
            "Para negar una conjunción `A ∧ B`, se niegan ambas partes y `∧` cambia a `∨`.",
        ],
        "solution": [
            "Valores simples: `p` es **V** (`12 = 4 · 3`); `q` es **F** (la raíz cuadrada principal `√9` vale `3`, no `−3`); `r` es **F** (`5` es menor que `8`).",
            "a) Como `q` es F, `~q` es V. Entonces `p ∧ ~q` es `V ∧ V = V`. Luego `(p ∧ ~q) ⇒ r` es `V ⇒ F = F`.",
            "b) En `r ⇒ (p ∧ q)`, el antecedente `r` es F y el consecuente `p ∧ q` es `V ∧ F = F`. Un condicional con antecedente falso es siempre **V** (`F ⇒ F = V`).",
            "En `q ⇔ r`, tanto `q` como `r` son F; como tienen el mismo valor de verdad, `F ⇔ F = V`. Por lo tanto, ambas son verdaderas.",
            "c) Por la ley de De Morgan, `~(A ∧ B) ≡ ~A ∨ ~B`. Aplicándolo a `~(p ∧ ~q)` obtenemos `~p ∨ ~(~q) ≡ ~p ∨ q`.",
        ],
    },
    {
        "id": "cl-logica-enunciados-3",
        "node": NODE,
        "kind": "problem",
        "level": 2,
        "title": "Teoremas: hipótesis, tesis y formas asociadas",
        "statement": (
            "Leé el siguiente teorema de Geometría (verdadero):\n\n"
            "«Todo rombo tiene sus diagonales perpendiculares.»\n\n"
            "Reescribilo con la forma «si…, entonces…» para analizar su hipótesis, su tesis y sus formas asociadas."
        ),
        "parts": [
            {
                "prompt": "a) Al escribir el teorema como `H ⇒ T`, ¿cuáles son la hipótesis `H` y la tesis `T`?",
                "check": _ch(
                    [
                        "H: un cuadrilátero es un rombo · T: sus diagonales son perpendiculares.",
                        "H: las diagonales de un cuadrilátero son perpendiculares · T: es un rombo.",
                        "H: un cuadrilátero no es un rombo · T: sus diagonales no son perpendiculares.",
                        "H: un polígono tiene cuatro lados · T: es un rombo.",
                    ],
                    0,
                ),
                "answer": "H: un cuadrilátero es un rombo · T: sus diagonales son perpendiculares.",
            },
            {
                "prompt": "b) ¿Cuál es el recíproco del teorema y cuál es su valor de verdad?",
                "check": _ch(
                    [
                        "«Si un cuadrilátero tiene sus diagonales perpendiculares, entonces es un rombo» — Falso.",
                        "«Si un cuadrilátero tiene sus diagonales perpendiculares, entonces es un rombo» — Verdadero.",
                        "«Si un cuadrilátero no es un rombo, entonces sus diagonales no son perpendiculares» — Falso.",
                        "«Si un cuadrilátero no tiene sus diagonales perpendiculares, entonces no es un rombo» — Verdadero.",
                    ],
                    0,
                ),
                "answer": "«Si un cuadrilátero tiene sus diagonales perpendiculares, entonces es un rombo» — Falso.",
            },
            {
                "prompt": "c) ¿Cuál de estas afirmaciones es el contrarrecíproco (equivalente al teorema original)?",
                "check": _ch(
                    [
                        "Si un cuadrilátero no tiene sus diagonales perpendiculares, entonces no es un rombo.",
                        "Si un cuadrilátero no es un rombo, entonces sus diagonales no son perpendiculares.",
                        "Si un cuadrilátero tiene sus diagonales perpendiculares, entonces es un rombo.",
                        "Existe un rombo cuyas diagonales no son perpendiculares.",
                    ],
                    0,
                ),
                "answer": "Si un cuadrilátero no tiene sus diagonales perpendiculares, entonces no es un rombo.",
            },
        ],
        "hints": [
            "«Todo A cumple B» equivale a «Si un objeto es A, entonces cumple B»: A es la hipótesis y B es la tesis.",
            "Para `H ⇒ T`: recíproco es `T ⇒ H`, contrario es `~H ⇒ ~T`, y contrarrecíproco es `~T ⇒ ~H`.",
            "Pensá en un barrilete (romboide) o en un cuadrilátero dibujado sobre dos segmentos perpendiculares de distinto largo: ¿tiene los cuatro lados iguales?",
        ],
        "solution": [
            "a) El teorema dice «Si un cuadrilátero es un rombo (`H`), entonces sus diagonales son perpendiculares (`T`)». La hipótesis es lo que se supone; la tesis, lo que se asegura.",
            "b) El recíproco intercambia hipótesis y tesis (`T ⇒ H`): «Si un cuadrilátero tiene sus diagonales perpendiculares, entonces es un rombo».",
            "Ese recíproco es **falso**: un romboide (barrilete) tiene diagonales perpendiculares, pero no tiene los cuatro lados iguales, así que no es un rombo.",
            "c) El contrarrecíproco intercambia y niega ambas (`~T ⇒ ~H`): «Si un cuadrilátero no tiene sus diagonales perpendiculares, entonces no es un rombo».",
            "Como el contrarrecíproco es lógicamente equivalente al teorema original, es **verdadero** sin necesidad de otra demostración. (En cambio, «si no es rombo, no tiene diagonales perpendiculares» es el *contrario*, que también es falso por el romboide.)",
        ],
    },
    {
        "id": "cl-logica-enunciados-4",
        "node": NODE,
        "kind": "problem",
        "level": 3,
        "title": "Condiciones necesarias, suficientes y contraejemplos",
        "statement": (
            "Aplicá la relación entre implicación, condiciones necesarias/suficientes, contrarrecíproco y contraejemplos en tres situaciones:\n\n"
            "1. Teorema verdadero: «Si un número entero `n` es divisible por 9, entonces `n` es múltiplo de 3.»\n"
            "2. Afirmación a evaluar: «Para todo número real `x`, si `x² > 4`, entonces `x > 2`.»\n"
            "3. Regla de seguridad industrial: «Si el sensor supera los 90 °C, la válvula de alivio se abre.»"
        ),
        "parts": [
            {
                "prompt": "a) Según el teorema 1, para que `n` sea divisible por 9, ser múltiplo de 3 es una condición…",
                "check": _ch(
                    [
                        "Necesaria, pero no suficiente.",
                        "Suficiente, pero no necesaria.",
                        "Necesaria y suficiente.",
                        "Ni necesaria ni suficiente.",
                    ],
                    0,
                ),
                "answer": "Necesaria, pero no suficiente (sin ser múltiplo de 3 no puede ser divisible por 9, pero 6 es múltiplo de 3 y no es divisible por 9).",
            },
            {
                "prompt": "b) ¿Cuál de estos valores es un contraejemplo válido que refuta la afirmación 2?",
                "check": _ch(
                    ["x = −3", "x = 1", "x = 3", "x = −2"],
                    0,
                ),
                "answer": "x = −3: cumple (−3)² = 9 > 4 (hipótesis V) y no cumple −3 > 2 (tesis F).",
            },
            {
                "prompt": "c) En la situación 3, mirás el tablero y ves que la válvula de alivio está CERRADA. ¿Qué podés asegurar con certeza?",
                "check": _ch(
                    [
                        "Que el sensor no superó los 90 °C.",
                        "Que el sensor superó los 90 °C.",
                        "Nada: la regla solo habla de cuando la válvula se abre.",
                        "Que si la válvula estuviera abierta, el sensor seguro habría superado los 90 °C.",
                    ],
                    0,
                ),
                "answer": "Que el sensor no superó los 90 °C (por el contrarrecíproco de la regla).",
            },
        ],
        "hints": [
            "En `p ⇒ q` verdadero: `p` es condición suficiente para `q`, y `q` es condición necesaria para `p`.",
            "Un contraejemplo de `H ⇒ T` tiene que hacer **verdadera** la hipótesis `H` y **falsa** la tesis `T`. Si `H` es falsa, ese caso no refuta nada.",
            "En la situación 3, «válvula cerrada» es `~T`. ¿Qué dice el contrarrecíproco `~T ⇒ ~H`?",
        ],
        "solution": [
            "a) En `p ⇒ q` («divisible por 9 ⇒ múltiplo de 3»), la tesis `q` (ser múltiplo de 3) es **condición necesaria** para `p`: si no es múltiplo de 3, imposible que sea divisible por 9.",
            "No es suficiente porque el recíproco falla: `n = 6` es múltiplo de 3 y no es divisible por 9.",
            "b) Buscamos un `x ∈ IR` que cumpla `x² > 4` y NO cumpla `x > 2`. Con `x = −3`: `(−3)² = 9 > 4` (V) y `−3 > 2` (F). Es contraejemplo válido.",
            "Descartamos los demás: `x = 1` (`1 > 4` es F) y `x = −2` (`4 > 4` es F, la desigualdad es estricta) no cumplen la hipótesis; `x = 3` cumple hipótesis y tesis.",
            "c) La regla es `S > 90 °C ⇒ válvula abierta`. Su contrarrecíproco, lógicamente equivalente, es `válvula cerrada ⇒ S ≤ 90 °C`. Por eso, ver la válvula cerrada asegura que el sensor **no** superó los 90 °C.",
            "En cambio, ver la válvula abierta no probaría que superó los 90 °C (eso sería el recíproco: podría haberse abierto manualmente o por otro disparo).",
        ],
    },
]
