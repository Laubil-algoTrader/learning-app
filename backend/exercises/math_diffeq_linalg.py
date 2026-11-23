"""Ejercicios de Ecuaciones diferenciales (#100-#105) y Álgebra lineal (#106-#112).
Tres problemas por tema (niveles 1, 2 y 3). Borrador: la app ignora los archivos `_draft_`."""

EXERCISES: list[dict] = [
    # ==================== FACTOR INTEGRANTE ====================
    {
        "id": "de-factor-integrante-1",
        "node": "de-factor-integrante",
        "kind": "problem",
        "level": 1,
        "title": "Lineal con coeficiente variable delante de y'",
        "statement": "Resolvé el problema de valor inicial `x·y' − 2y = x⁴` con `y(1) = 3`, para `x > 0`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el factor integrante `μ(x)` que hay que usar?",
                "check": {"type": "choice", "options": ["μ(x) = x^(−2)", "μ(x) = x²", "μ(x) = e^(−2x)", "μ(x) = −2·ln(x)"], "correct": 0},
                "answer": "μ(x) = x^(−2) = 1/x²",
            },
            {
                "prompt": "b) ¿Cuánto vale `y(2)`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 18, "tolerance": 0, "unit": ""},
                "answer": "18",
            },
        ],
        "hints": [
            "Antes de leer `P(x)` dividí toda la ecuación por `x` para dejar `y'` con coeficiente 1.",
            "Con `P(x) = −2/x`, `∫P dx = −2·ln(x) = ln(x^(−2))`.",
        ],
        "solution": [
            "Forma estándar (dividimos por `x`): `y' − (2/x)·y = x³`, así que `P(x) = −2/x` y `Q(x) = x³`.",
            "Factor integrante: `μ(x) = e^(∫ −2/x dx) = e^(−2·ln x) = x^(−2)`.",
            "Multiplicando: `(x^(−2)·y)' = x^(−2)·x³ = x`. Integramos: `y/x² = x²/2 + C`.",
            "Despejamos (la `C` también se multiplica por `x²`): `y(x) = x⁴/2 + C·x²`.",
            "Condición inicial: `y(1) = 1/2 + C = 3` → `C = 5/2`. Entonces `y(x) = x⁴/2 + (5/2)·x²`.",
            "`y(2) = 16/2 + (5/2)·4 = 8 + 10 = 18`. Verificación: `x·y' − 2y = x(2x³ + 5x) − (x⁴ + 5x²) = x⁴` ✓. Error típico: tomar `P(x) = −2` sin dividir por `x`, que da `μ = e^(−2x)`.",
        ],
    },
    {
        "id": "de-factor-integrante-2",
        "node": "de-factor-integrante",
        "kind": "problem",
        "level": 2,
        "title": "Ecuación homogénea de primer orden",
        "statement": "Resolvé `dy/dx = y/x + x/y` con la condición `y(1) = 2`, para `x > 0` e `y > 0`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la solución general (con constante `C`)?",
                "check": {
                    "type": "choice",
                    "options": [
                        "y² = x²·(2·ln x + C)",
                        "y² = 2x²·ln x + C",
                        "y = x·(2·ln x + C)",
                        "y² = x²·(ln x + C)",
                    ],
                    "correct": 0,
                },
                "answer": "y² = x²·(2·ln x + C)",
            },
            {
                "prompt": "b) Con la condición `y(1) = 2`, ¿cuánto vale `(y/x)²` cuando `x = e³`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": ""},
                "answer": "10",
            },
        ],
        "hints": [
            "El lado derecho depende solo de `y/x`: probá la sustitución `v = y/x`, o sea `y = v·x` e `y' = v + x·v'`.",
            "Después de sustituir, los términos `v` se cancelan y queda una ecuación separable en `v` y `x`.",
        ],
        "solution": [
            "Con `v = y/x`: `y = v·x` → `y' = v + x·v'`. La ecuación queda `v + x·v' = v + 1/v`.",
            "Se cancela `v`: `x·v' = 1/v` → separamos: `v dv = dx/x`.",
            "Integramos: `v²/2 = ln x + K` → `v² = 2·ln x + C` (con `C = 2K`).",
            "Volviendo a `y`: `y²/x² = 2·ln x + C` → `y² = x²·(2·ln x + C)`.",
            "Condición: `x = 1`, `y = 2` → `4 = 1·(0 + C)` → `C = 4`. Así `(y/x)² = 2·ln x + 4`.",
            "En `x = e³`: `(y/x)² = 2·3 + 4 = 10`. Error típico: integrar mal y escribir `y² = 2x²·ln x + C` (la `C` también va multiplicada por `x²`).",
        ],
    },
    {
        "id": "de-factor-integrante-3",
        "node": "de-factor-integrante",
        "kind": "problem",
        "level": 3,
        "title": "Tanque de salmuera que se va llenando",
        "statement": "Un tanque de 200 L de capacidad contiene inicialmente 100 L de agua con 5 kg de sal disuelta. A partir de `t = 0` entra salmuera con 0,1 kg de sal por litro a razón de 4 L/min, y por un desagüe sale la mezcla (bien homogeneizada) a 2 L/min. Sea `S(t)` la cantidad de sal en kg y `t` el tiempo en minutos.",
        "parts": [
            {
                "prompt": "a) ¿En cuántos minutos se llena el tanque? Respondé solo con el número en min.",
                "check": {"type": "numeric", "value": 50, "tolerance": 0, "unit": "min"},
                "answer": "50 min",
            },
            {
                "prompt": "b) ¿Cuántos kg de sal hay en el tanque en el momento en que se llena? Respondé solo con el número en kg.",
                "check": {"type": "numeric", "value": 17.5, "tolerance": 0, "unit": "kg"},
                "answer": "17.5 kg",
            },
            {
                "prompt": "c) ¿Cuál es la concentración de sal en ese momento? Respondé solo con el número en g/L.",
                "check": {"type": "numeric", "value": 87.5, "tolerance": 0, "unit": "g/L"},
                "answer": "87.5 g/L",
            },
        ],
        "hints": [
            "El volumen no es constante: `V(t) = 100 + (4 − 2)·t`. La sal que sale por minuto es `2·S/V(t)`.",
            "Planteá `S' = (entra) − (sale)` y llevala a la forma `S' + P(t)·S = Q(t)`.",
            "`∫ 2/(100 + 2t) dt = ln(100 + 2t)`, así que el factor integrante es `100 + 2t`.",
        ],
        "solution": [
            "Volumen: `V(t) = 100 + 2t` L. Se llena cuando `100 + 2t = 200` → `t = 50` min.",
            "Balance de sal: entra `0,1 · 4 = 0,4` kg/min; sale `2 · S/(100 + 2t)` kg/min. Entonces `S' + (2/(100 + 2t))·S = 0,4`.",
            "Factor integrante: `μ = e^(∫ 2/(100 + 2t) dt) = e^(ln(100 + 2t)) = 100 + 2t`.",
            "`((100 + 2t)·S)' = 0,4·(100 + 2t)` → integrando: `(100 + 2t)·S = 40t + 0,4t² + C`.",
            "Condición `S(0) = 5`: `100 · 5 = C` → `C = 500`. Así `S(t) = (0,4t² + 40t + 500)/(100 + 2t)`.",
            "En `t = 50`: `S = (1000 + 2000 + 500)/200 = 3500/200 = 17,5` kg.",
            "Concentración: `17,5 kg / 200 L = 0,0875 kg/L = 87,5 g/L` (todavía por debajo de los 100 g/L de la salmuera que entra, como era de esperar). Error típico: usar `V = 100` constante en el término de salida.",
        ],
    },
    # ==================== ECUACIONES EXACTAS ====================
    {
        "id": "de-ecuaciones-exactas-1",
        "node": "de-ecuaciones-exactas",
        "kind": "problem",
        "level": 1,
        "title": "Potencial y valor de la solución en x = 0",
        "statement": "Considerá la ecuación `(3x²y + 2) dx + (x³ + 2y) dy = 0` y la curva solución que pasa por el punto `(1, 1)`.",
        "parts": [
            {
                "prompt": "a) Comprobá que es exacta. ¿Cuál es su solución general implícita?",
                "check": {
                    "type": "choice",
                    "options": [
                        "x³y + 2x + y² = C",
                        "2x³y + 2x + y² = C",
                        "x³y + y² = C",
                        "x³y + 2x + 2y² = C",
                    ],
                    "correct": 0,
                },
                "answer": "x³y + 2x + y² = C",
            },
            {
                "prompt": "b) Sobre la solución que pasa por `(1, 1)`, ¿cuánto vale `y` cuando `x = 0`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
        ],
        "hints": [
            "Test: `∂M/∂y` y `∂N/∂x` tienen que dar lo mismo.",
            "Integrá `M` respecto de `x` sumando `h(y)` y después usá `∂Ψ/∂y = N`.",
            "En `x = 0` queda una ecuación en `y`; elegí la raíz a la que se llega por continuidad desde `y(1) = 1`.",
        ],
        "solution": [
            "Test: `∂M/∂y = 3x²` y `∂N/∂x = 3x²` → es exacta.",
            "`Ψ = ∫(3x²y + 2) dx = x³y + 2x + h(y)`. Derivando en `y`: `x³ + h'(y) = x³ + 2y` → `h'(y) = 2y` → `h(y) = y²`.",
            "Solución general: `x³y + 2x + y² = C`. Por `(1, 1)`: `C = 1 + 2 + 1 = 4`.",
            "Como cuadrática en `y`: `y² + x³y + (2x − 4) = 0` → `y = (−x³ + √(x⁶ − 8x + 16))/2` (la rama con `+` es la que da `y(1) = (−1 + 3)/2 = 1`).",
            "El discriminante `x⁶ − 8x + 16` es positivo entre `x = 0` y `x = 1`, así que la rama sigue definida. En `x = 0`: `y = (0 + √16)/2 = 2`.",
            "Error típico: contar dos veces el término `x³y` (sumarlo al integrar `M` y otra vez al integrar `N`), que da `2x³y + 2x + y² = C`.",
        ],
    },
    {
        "id": "de-ecuaciones-exactas-2",
        "node": "de-ecuaciones-exactas",
        "kind": "problem",
        "level": 2,
        "title": "Volver exacta una ecuación con un factor integrante",
        "statement": "La ecuación `(2y² + 3x) dx + 2xy dy = 0` (con `x > 0`, `y > 0`) no es exacta, pero existe un factor integrante que depende solo de `x`. Resolvela con la condición `y(1) = 4`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál de estos factores la vuelve exacta?",
                "check": {"type": "choice", "options": ["μ = x", "μ = 1/x", "μ = y", "μ = x²"], "correct": 0},
                "answer": "μ = x",
            },
            {
                "prompt": "b) ¿Cuánto vale `y(2)`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1.5, "tolerance": 0, "unit": ""},
                "answer": "1.5 (= 3/2)",
            },
        ],
        "hints": [
            "Calculá `(∂M/∂y − ∂N/∂x)/N`: si depende solo de `x`, el factor es `μ = e^(∫ de eso dx)`.",
            "Multiplicada por `μ`, la ecuación es `(2xy² + 3x²) dx + 2x²y dy = 0`; buscá su potencial `Ψ`.",
        ],
        "solution": [
            "`∂M/∂y = 4y` y `∂N/∂x = 2y`: no es exacta. `(4y − 2y)/(2xy) = 1/x` depende solo de `x` → `μ = e^(∫ dx/x) = x`.",
            "Multiplicando: `(2xy² + 3x²) dx + 2x²y dy = 0`. Test: `∂/∂y(2xy² + 3x²) = 4xy` y `∂/∂x(2x²y) = 4xy` ✓.",
            "`Ψ = ∫(2xy² + 3x²) dx = x²y² + x³ + h(y)`; `∂Ψ/∂y = 2x²y + h'(y) = 2x²y` → `h' = 0`. Solución: `x²y² + x³ = C`.",
            "Con `y(1) = 4`: `16 + 1 = 17` → `x²y² + x³ = 17`.",
            "En `x = 2`: `4y² + 8 = 17` → `y² = 9/4` → `y = 3/2` (positiva, porque la solución arranca en `y = 4 > 0` y `y = √(17 − x³)/x` no se anula antes de `x = 2`).",
            "Los otros factores fallan: con `μ = x²` queda `∂M/∂y = 4x²y` pero `∂N/∂x = 6x²y`; con `1/x` o con `y` tampoco coinciden.",
        ],
    },
    {
        "id": "de-ecuaciones-exactas-3",
        "node": "de-ecuaciones-exactas",
        "kind": "problem",
        "level": 3,
        "title": "Exacta con exponenciales y trigonométricas",
        "statement": "Considerá el problema `(k·x·e^y + y·cos x) dx + (x²·e^y + sen x + 2y) dy = 0`, con `y(0) = 2`.",
        "parts": [
            {
                "prompt": "a) ¿Para qué valor de `k` la ecuación es exacta? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
            {
                "prompt": "b) Con ese `k`, ¿cuál es la solución implícita del problema?",
                "check": {
                    "type": "choice",
                    "options": [
                        "x²·e^y + y·sen x + y² = 4",
                        "x²·e^y + y·sen x + y² = 0",
                        "x²·e^y − y·sen x + y² = 4",
                        "2x·e^y + y·sen x + y² = 4",
                    ],
                    "correct": 0,
                },
                "answer": "x²·e^y + y·sen x + y² = 4",
            },
            {
                "prompt": "c) La solución `y(x)` decrece desde `y(0) = 2`. ¿En qué valor de `x > 0` se anula por primera vez? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
        ],
        "hints": [
            "Igualá `∂M/∂y = k·x·e^y + cos x` con `∂N/∂x`.",
            "Integrá `M` respecto de `x` (sumando `h(y)`) y comparalo con `N` para hallar `h(y)`.",
            "Para el inciso c) reemplazá `y = 0` en la solución implícita.",
        ],
        "solution": [
            "`∂M/∂y = k·x·e^y + cos x` y `∂N/∂x = 2x·e^y + cos x`. Son iguales si `k = 2`.",
            "`Ψ = ∫(2x·e^y + y·cos x) dx = x²·e^y + y·sen x + h(y)`.",
            "`∂Ψ/∂y = x²·e^y + sen x + h'(y) = x²·e^y + sen x + 2y` → `h'(y) = 2y` → `h(y) = y²`.",
            "Solución general `x²·e^y + y·sen x + y² = C`; con `(0, 2)`: `0 + 0 + 4 = C` → `C = 4`.",
            "Con `y = 0`: `x² = 4` → `x = 2` (la positiva).",
            "Es la primera vez: para `0 ≤ x < 2` y `y = 0` el potencial vale `x² < 4`, y como `∂Ψ/∂y = x²e^y + sen x + 2y > 0` para `0 < x ≤ 2`, `y > 0`, la solución queda positiva hasta `x = 2`. Error típico: no igualar a `C = 4` (la condición inicial fija la constante).",
        ],
    },
    # ==================== 2.° ORDEN HOMOGÉNEAS ====================
    {
        "id": "de-segundo-orden-homogeneas-1",
        "node": "de-segundo-orden-homogeneas",
        "kind": "problem",
        "level": 1,
        "title": "Raíces reales distintas con condiciones iniciales",
        "statement": "Resolvé `y'' + y' − 6y = 0` con `y(0) = 1` e `y'(0) = 7`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la solución del problema?",
                "check": {
                    "type": "choice",
                    "options": [
                        "y = 2e^(2t) − e^(−3t)",
                        "y = 2e^(−2t) − e^(3t)",
                        "y = −e^(2t) + 2e^(−3t)",
                        "y = (2 − t)·e^(2t)",
                    ],
                    "correct": 0,
                },
                "answer": "y = 2e^(2t) − e^(−3t)",
            },
            {
                "prompt": "b) ¿Cuánto vale `y(ln 2)`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 7.875, "tolerance": 0, "unit": ""},
                "answer": "7.875 (= 63/8)",
            },
        ],
        "hints": [
            "Ecuación característica: `r² + r − 6 = 0`; factorizala.",
            "Planteá `y(0) = c₁ + c₂` e `y'(0) = 2c₁ − 3c₂` y resolvé el sistema.",
        ],
        "solution": [
            "`r² + r − 6 = (r − 2)(r + 3) = 0` → `r = 2` y `r = −3`. Solución general: `y = c₁e^(2t) + c₂e^(−3t)`.",
            "`y(0) = c₁ + c₂ = 1` e `y'(0) = 2c₁ − 3c₂ = 7`.",
            "De la primera, `c₂ = 1 − c₁`: `2c₁ − 3 + 3c₁ = 7` → `c₁ = 2`, `c₂ = −1`. Entonces `y = 2e^(2t) − e^(−3t)`.",
            "`y(ln 2) = 2·e^(2 ln 2) − e^(−3 ln 2) = 2·4 − 1/8 = 63/8 = 7,875`.",
            "Verificación: `y'(0) = 4 + 3 = 7` ✓. Error típico: cambiar los signos de las raíces (`e^(−2t)`, `e^(3t)`), que da una función que no cumple la ecuación.",
        ],
    },
    {
        "id": "de-segundo-orden-homogeneas-2",
        "node": "de-segundo-orden-homogeneas",
        "kind": "problem",
        "level": 2,
        "title": "Cierrapuertas con amortiguamiento crítico",
        "statement": "El ángulo (en grados) que una puerta con cierrapuertas forma respecto de su posición cerrada cumple `y'' + 4y' + 4y = 0` (t en segundos). En `t = 0` está a `y(0) = 3°` y se mueve con velocidad `y'(0) = v₀`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la forma de la solución general?",
                "check": {
                    "type": "choice",
                    "options": [
                        "y = (c₁ + c₂·t)·e^(−2t)",
                        "y = c₁e^(−2t) + c₂e^(2t)",
                        "y = c₁cos(2t) + c₂sen(2t)",
                        "y = (c₁ + c₂)·e^(−2t)",
                    ],
                    "correct": 0,
                },
                "answer": "y = (c₁ + c₂·t)·e^(−2t)",
            },
            {
                "prompt": "b) Si `v₀ = −4 °/s`, ¿cuánto vale `y(1)`? Redondeá a 2 decimales. Respondé solo con el número en grados.",
                "check": {"type": "numeric", "value": 0.68, "tolerance": 0.01, "unit": "°"},
                "answer": "0.68°",
            },
            {
                "prompt": "c) ¿Qué velocidad inicial `v₀` hace que la puerta llegue a cerrarse (`y = 0`) justo en `t = 1 s`? Respondé solo con el número en °/s.",
                "check": {"type": "numeric", "value": -9, "tolerance": 0, "unit": "°/s"},
                "answer": "−9 °/s",
            },
        ],
        "hints": [
            "`r² + 4r + 4 = (r + 2)²`: raíz doble, así que el segundo término lleva una `t`.",
            "Con `y(0) = 3` sale `c₁ = 3`; derivá `(3 + c₂t)·e^(−2t)` para relacionar `c₂` con `v₀`.",
        ],
        "solution": [
            "`(r + 2)² = 0` → raíz doble `r = −2` → `y = (c₁ + c₂t)·e^(−2t)`.",
            "`y(0) = c₁ = 3`. Derivando: `y' = c₂e^(−2t) − 2(3 + c₂t)e^(−2t)` → `y'(0) = c₂ − 6 = v₀` → `c₂ = v₀ + 6`.",
            "b) Con `v₀ = −4`: `c₂ = 2` → `y = (3 + 2t)·e^(−2t)`, y `y(1) = 5·e^(−2) ≈ 0,677 ≈ 0,68°`.",
            "c) `y(1) = (3 + c₂)·e^(−2) = 0` → `c₂ = −3` → `v₀ = c₂ − 6 = −9 °/s`.",
            "Verificación: con `v₀ = −9`, `y = (3 − 3t)·e^(−2t)`, que vale 0 en `t = 1` ✓. Error típico: olvidar la `t` del caso de raíz doble; con `(c₁ + c₂)e^(−2t)` no se pueden cumplir dos condiciones iniciales a la vez.",
        ],
    },
    {
        "id": "de-segundo-orden-homogeneas-3",
        "node": "de-segundo-orden-homogeneas",
        "kind": "problem",
        "level": 3,
        "title": "Oscilador amortiguado: masa, resorte y amortiguador",
        "statement": "Una masa de 1 kg cuelga de un resorte de constante `k = 13 N/m` y está unida a un amortiguador de coeficiente `b = 4 N·s/m`. La posición `x(t)` (en cm, medida desde el equilibrio) cumple `x'' + 4x' + 13x = 0`. Se suelta desde `x(0) = 2 cm` con velocidad `x'(0) = 5 cm/s`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la frecuencia angular de oscilación (cuasi-frecuencia) del movimiento? Respondé solo con el número en rad/s.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": "rad/s"},
                "answer": "3 rad/s",
            },
            {
                "prompt": "b) ¿En qué instante `t > 0` la masa pasa por primera vez por la posición de equilibrio? Redondeá a 2 decimales. Respondé solo con el número en s.",
                "check": {"type": "numeric", "value": 0.85, "tolerance": 0.01, "unit": "s"},
                "answer": "0.85 s",
            },
            {
                "prompt": "c) Manteniendo la masa y el resorte, ¿qué coeficiente `b` produciría amortiguamiento crítico? Redondeá a 2 decimales. Respondé solo con el número en N·s/m.",
                "check": {"type": "numeric", "value": 7.21, "tolerance": 0.01, "unit": "N·s/m"},
                "answer": "7.21 N·s/m",
            },
        ],
        "hints": [
            "Las raíces de `r² + 4r + 13 = 0` son complejas `α ± βi`; `β` es la frecuencia.",
            "Con `x = e^(−2t)(c₁cos 3t + c₂sen 3t)`, usá las condiciones para hallar `c₁` y `c₂`; después igualá el paréntesis a 0.",
            "Amortiguamiento crítico: discriminante `b² − 4mk = 0`.",
        ],
        "solution": [
            "`r = (−4 ± √(16 − 52))/2 = −2 ± 3i` → `α = −2`, `β = 3`: oscila a `ω = 3 rad/s` con envolvente `e^(−2t)`.",
            "`x = e^(−2t)(c₁cos 3t + c₂sen 3t)`. `x(0) = c₁ = 2`. `x'(0) = −2c₁ + 3c₂ = 5` → `3c₂ = 9` → `c₂ = 3`.",
            "`x(t) = e^(−2t)(2cos 3t + 3sen 3t)`. Como `e^(−2t) > 0`, `x = 0` cuando `2cos 3t + 3sen 3t = 0` → `tg(3t) = −2/3`.",
            "En `t = 0` la masa está en `+2 cm` y sube; el primer cero ocurre con `3t` en el segundo cuadrante: `3t = π − arctg(2/3) ≈ 3,1416 − 0,5880 = 2,5536` → `t ≈ 0,851 s ≈ 0,85 s`.",
            "c) Crítico: `b² = 4·m·k = 4·1·13 = 52` → `b = √52 ≈ 7,21 N·s/m`.",
            "Error típico en b): tomar `3t = arctg(−2/3)`, que es negativo; hay que sumar `π` para obtener el primer instante positivo.",
        ],
    },
    # ==================== COEFICIENTES INDETERMINADOS ====================
    {
        "id": "de-coeficientes-indeterminados-1",
        "node": "de-coeficientes-indeterminados",
        "kind": "problem",
        "level": 1,
        "title": "Solución particular para un forzante lineal",
        "statement": "Hallá la solución general de `y'' − 3y' + 2y = 6t − 1` proponiendo una solución particular `y_p = At + B`.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale `A`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3",
            },
            {
                "prompt": "b) ¿Cuánto vale `B`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4",
            },
            {
                "prompt": "c) ¿Cuál es la solución general?",
                "check": {
                    "type": "choice",
                    "options": [
                        "y = c₁e^t + c₂e^(2t) + 3t + 4",
                        "y = c₁e^(−t) + c₂e^(−2t) + 3t + 4",
                        "y = 3t + 4",
                        "y = c₁e^t + c₂e^(2t) + 3t − 4",
                    ],
                    "correct": 0,
                },
                "answer": "y = c₁e^t + c₂e^(2t) + 3t + 4",
            },
        ],
        "hints": [
            "Con `y_p = At + B`: `y_p' = A` e `y_p'' = 0`. Sustituí e igualá coeficientes de `t` y términos independientes.",
            "Para `y_h` resolvé `r² − 3r + 2 = 0`.",
        ],
        "solution": [
            "Sustituimos `y_p = At + B`: `0 − 3A + 2(At + B) = 2A·t + (2B − 3A)`.",
            "Igualamos con `6t − 1`: `2A = 6` → `A = 3`; `2B − 3A = −1` → `2B = 8` → `B = 4`. Así `y_p = 3t + 4`.",
            "Homogénea: `r² − 3r + 2 = (r − 1)(r − 2) = 0` → `y_h = c₁e^t + c₂e^(2t)`.",
            "Solución general: `y = c₁e^t + c₂e^(2t) + 3t + 4`.",
            "Verificación: `−3·3 + 2(3t + 4) = 6t − 1` ✓. Error típico: dar solo `y_p` (le faltan las dos constantes) o cambiar el signo de las raíces.",
        ],
    },
    {
        "id": "de-coeficientes-indeterminados-2",
        "node": "de-coeficientes-indeterminados",
        "kind": "problem",
        "level": 2,
        "title": "Forzante senoidal con condiciones iniciales",
        "statement": "Resolvé `y'' + 3y' + 2y = 10·sen t` con `y(0) = 0` e `y'(0) = 0`.",
        "parts": [
            {
                "prompt": "a) Con `y_p = A·cos t + B·sen t`, ¿cuánto vale `A`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -3, "tolerance": 0, "unit": ""},
                "answer": "−3",
            },
            {
                "prompt": "b) ¿Cuál es la amplitud de la oscilación de estado estacionario? Redondeá a 2 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3.16, "tolerance": 0.01, "unit": ""},
                "answer": "3.16 (= √10)",
            },
            {
                "prompt": "c) En la solución completa `y = c₁e^(−t) + c₂e^(−2t) + y_p`, ¿cuánto vale `c₁`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                "answer": "5",
            },
        ],
        "hints": [
            "Sustituí `y_p` y separá los coeficientes de `cos t` y de `sen t`: quedan dos ecuaciones para `A` y `B`.",
            "La amplitud de `A·cos t + B·sen t` es `√(A² + B²)`.",
            "Las condiciones iniciales se aplican a la solución completa `y_h + y_p`, no a `y_h` sola.",
        ],
        "solution": [
            "`y_p' = −A·sen t + B·cos t`, `y_p'' = −A·cos t − B·sen t`. Sustituyendo: `(−A + 3B + 2A)·cos t + (−B − 3A + 2B)·sen t = (A + 3B)·cos t + (B − 3A)·sen t`.",
            "Igualamos con `10·sen t`: `A + 3B = 0` y `B − 3A = 10`. De la primera `A = −3B` → `B + 9B = 10` → `B = 1`, `A = −3`.",
            "`y_p = −3cos t + sen t`; su amplitud es `√(9 + 1) = √10 ≈ 3,16`.",
            "Homogénea: `r² + 3r + 2 = (r + 1)(r + 2)` → `y_h = c₁e^(−t) + c₂e^(−2t)`.",
            "`y(0) = c₁ + c₂ − 3 = 0` e `y'(0) = −c₁ − 2c₂ + 1 = 0` → `c₁ + c₂ = 3` y `c₁ + 2c₂ = 1` → `c₂ = −2`, `c₁ = 5`.",
            "Solución: `y = 5e^(−t) − 2e^(−2t) − 3cos t + sen t`. Los exponenciales se apagan (transitorio) y queda la oscilación de amplitud `√10`. Error típico: proponer solo `B·sen t`, que no alcanza porque `3y'` genera cosenos.",
        ],
    },
    {
        "id": "de-coeficientes-indeterminados-3",
        "node": "de-coeficientes-indeterminados",
        "kind": "problem",
        "level": 3,
        "title": "Resonancia en un sistema masa-resorte sin roce",
        "statement": "Un sistema masa-resorte sin rozamiento, forzado justo a su frecuencia natural, cumple `y'' + 9y = 12·cos(3t)` (y en cm, t en s), con `y(0) = 1` e `y'(0) = 0`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la solución del problema?",
                "check": {
                    "type": "choice",
                    "options": [
                        "y = cos(3t) + 2t·sen(3t)",
                        "y = cos(3t) + 4t·sen(3t)",
                        "y = cos(3t) + 2t·cos(3t)",
                        "y = 2t·sen(3t)",
                    ],
                    "correct": 0,
                },
                "answer": "y = cos(3t) + 2t·sen(3t)",
            },
            {
                "prompt": "b) ¿Cuánto vale `y(π/2)`? Redondeá a 2 decimales. Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": -3.14, "tolerance": 0.01, "unit": "cm"},
                "answer": "−3.14 cm (= −π)",
            },
        ],
        "hints": [
            "`cos(3t)` ya es solución de la homogénea: la propuesta `A·cos 3t + B·sen 3t` hay que multiplicarla por `t`.",
            "Con `y_p = t(A·cos 3t + B·sen 3t)`, al sustituir los términos con `t` se cancelan y queda `−6A·sen 3t + 6B·cos 3t`.",
        ],
        "solution": [
            "Homogénea: `r² + 9 = 0` → `r = ±3i` → `y_h = c₁cos 3t + c₂sen 3t`. El forzante tiene la misma frecuencia: resonancia.",
            "Proponemos `y_p = t(A·cos 3t + B·sen 3t)`. Derivando dos veces y sustituyendo: `y_p'' + 9y_p = −6A·sen 3t + 6B·cos 3t`.",
            "Igualamos con `12·cos 3t`: `A = 0` y `6B = 12` → `B = 2`. Entonces `y_p = 2t·sen 3t`.",
            "`y = c₁cos 3t + c₂sen 3t + 2t·sen 3t`. `y(0) = c₁ = 1`. `y' = −3c₁sen 3t + 3c₂cos 3t + 2sen 3t + 6t·cos 3t` → `y'(0) = 3c₂ = 0` → `c₂ = 0`.",
            "Solución: `y = cos 3t + 2t·sen 3t`; la amplitud crece linealmente con `t` (resonancia).",
            "`y(π/2) = cos(3π/2) + 2(π/2)·sen(3π/2) = 0 + π·(−1) = −π ≈ −3,14 cm`. Error típico: proponer `y_p` sin el factor `t`; al sustituir da `0 = 12·cos 3t`, imposible.",
        ],
    },
    # ==================== LAPLACE BÁSICA ====================
    {
        "id": "de-laplace-basica-1",
        "node": "de-laplace-basica",
        "kind": "problem",
        "level": 1,
        "title": "Transformada inversa por fracciones simples",
        "statement": "Al resolver un problema con Laplace llegaste a `Y(s) = (5s − 1)/(s² − s − 2)`. Hallá `y(t) = L⁻¹{Y(s)}`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es `y(t)`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "y(t) = 3e^(2t) + 2e^(−t)",
                        "y(t) = 3e^(−2t) + 2e^t",
                        "y(t) = 2e^(2t) + 3e^(−t)",
                        "y(t) = 3e^(2t) − 2e^(−t)",
                    ],
                    "correct": 0,
                },
                "answer": "y(t) = 3e^(2t) + 2e^(−t)",
            },
            {
                "prompt": "b) ¿Cuánto vale `y(ln 2)`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 13, "tolerance": 0, "unit": ""},
                "answer": "13",
            },
        ],
        "hints": [
            "Factorizá el denominador: `s² − s − 2 = (s − 2)(s + 1)`.",
            "Escribí `Y = A/(s − 2) + B/(s + 1)` y usá `L⁻¹{1/(s − a)} = e^(at)`.",
        ],
        "solution": [
            "`s² − s − 2 = (s − 2)(s + 1)`, así que `(5s − 1)/((s − 2)(s + 1)) = A/(s − 2) + B/(s + 1)`.",
            "`5s − 1 = A(s + 1) + B(s − 2)`. Con `s = 2`: `9 = 3A` → `A = 3`. Con `s = −1`: `−6 = −3B` → `B = 2`.",
            "`Y = 3/(s − 2) + 2/(s + 1)` → `y(t) = 3e^(2t) + 2e^(−t)`.",
            "`y(ln 2) = 3·e^(2 ln 2) + 2·e^(−ln 2) = 3·4 + 2·(1/2) = 13`.",
            "Error típico: leer `1/(s + 1)` como `e^(t)`; el signo se invierte: `s + 1 = s − (−1)` → `e^(−t)`.",
        ],
    },
    {
        "id": "de-laplace-basica-2",
        "node": "de-laplace-basica",
        "kind": "problem",
        "level": 2,
        "title": "PVI de segundo orden con forzante constante",
        "statement": "Usá la transformada de Laplace para resolver `y'' − 3y' + 2y = 4` con `y(0) = 1` e `y'(0) = 4`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es `Y(s) = L{y}`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "Y(s) = (s² + s + 4) / (s·(s² − 3s + 2))",
                        "Y(s) = (s² + 4s + 4) / (s·(s² − 3s + 2))",
                        "Y(s) = (s + 5) / (s² − 3s + 2)",
                        "Y(s) = (s² + s + 4) / (s·(s² + 3s + 2))",
                    ],
                    "correct": 0,
                },
                "answer": "Y(s) = (s² + s + 4) / (s·(s² − 3s + 2))",
            },
            {
                "prompt": "b) ¿Cuánto vale `y(ln 3)`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 29, "tolerance": 0, "unit": ""},
                "answer": "29",
            },
        ],
        "hints": [
            "`L{y''} = s²Y − s·y(0) − y'(0)`, `L{y'} = sY − y(0)` y `L{4} = 4/s`.",
            "El denominador es `s(s − 1)(s − 2)`: descomponé en tres fracciones simples.",
        ],
        "solution": [
            "Transformamos: `(s²Y − s − 4) − 3(sY − 1) + 2Y = 4/s` → `(s² − 3s + 2)·Y = s + 1 + 4/s = (s² + s + 4)/s`.",
            "`Y = (s² + s + 4)/(s(s − 1)(s − 2)) = A/s + B/(s − 1) + C/(s − 2)`.",
            "Por residuos: `A = 4/((−1)(−2)) = 2`; `B = (1 + 1 + 4)/(1·(−1)) = −6`; `C = (4 + 2 + 4)/(2·1) = 5`.",
            "`y(t) = 2 − 6e^t + 5e^(2t)`. Verificación: `y(0) = 2 − 6 + 5 = 1` ✓ e `y'(0) = −6 + 10 = 4` ✓.",
            "`y(ln 3) = 2 − 6·3 + 5·9 = 2 − 18 + 45 = 29`.",
            "Error típico: transformar `4` como `4` en vez de `4/s`, o escribir `−3(sY + 1)` (signo de `y(0)` mal), que cambian el numerador de `Y`.",
        ],
    },
    {
        "id": "de-laplace-basica-3",
        "node": "de-laplace-basica",
        "kind": "problem",
        "level": 3,
        "title": "Oscilador forzado por una exponencial",
        "statement": "Resolvé con Laplace el problema `y'' + 4y = 5e^t`, con `y(0) = 1` e `y'(0) = 0`.",
        "parts": [
            {
                "prompt": "a) Al descomponer `Y(s)` en fracciones simples, ¿cuál es el coeficiente del término `1/(s − 1)`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1",
            },
            {
                "prompt": "b) ¿Cuál es la solución `y(t)`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "y(t) = e^t − ½·sen(2t)",
                        "y(t) = e^t − cos(2t) − ½·sen(2t)",
                        "y(t) = e^t − sen(2t)",
                        "y(t) = e^t + ½·sen(2t)",
                    ],
                    "correct": 0,
                },
                "answer": "y(t) = e^t − ½·sen(2t)",
            },
            {
                "prompt": "c) ¿Cuánto vale `y(π/4)`? Redondeá a 2 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1.69, "tolerance": 0.01, "unit": ""},
                "answer": "1.69",
            },
        ],
        "hints": [
            "Transformá: `s²Y − s + 4Y = 5/(s − 1)` y despejá `Y`.",
            "Descomponé `5/((s − 1)(s² + 4)) = A/(s − 1) + (Bs + C)/(s² + 4)` y sumale el término que vino de `y(0)`.",
            "`L⁻¹{1/(s² + 4)} = ½·sen(2t)` (falta el `ω = 2` arriba).",
        ],
        "solution": [
            "`L{y''} = s²Y − s·1 − 0`. Entonces `(s² + 4)Y = s + 5/(s − 1)` → `Y = s/(s² + 4) + 5/((s − 1)(s² + 4))`.",
            "`5 = A(s² + 4) + (Bs + C)(s − 1)`. Con `s = 1`: `5 = 5A` → `A = 1`. Coeficiente de `s²`: `0 = A + B` → `B = −1`. Término independiente: `5 = 4A − C` → `C = −1`.",
            "`Y = s/(s² + 4) + 1/(s − 1) − s/(s² + 4) − 1/(s² + 4) = 1/(s − 1) − 1/(s² + 4)`: los cosenos se cancelan.",
            "`y(t) = e^t − ½·sen(2t)`. Verificación: `y'' + 4y = e^t + 2sen 2t + 4e^t − 2sen 2t = 5e^t` ✓, `y(0) = 1` ✓, `y'(0) = 1 − 1 = 0` ✓.",
            "`y(π/4) = e^(π/4) − ½·sen(π/2) ≈ 2,193 − 0,5 = 1,693 ≈ 1,69`.",
            "Error típico: olvidar el término `s/(s² + 4)` que aporta `y(0) = 1`; se obtiene `e^t − cos 2t − ½sen 2t`, que cumple la ecuación pero da `y(0) = 0`.",
        ],
    },
    # ==================== ESCALÓN E IMPULSO ====================
    {
        "id": "de-laplace-escalon-impulso-1",
        "node": "de-laplace-escalon-impulso",
        "kind": "problem",
        "level": 1,
        "title": "Dosis instantánea de un medicamento",
        "statement": "La concentración `y(t)` de un medicamento en sangre (mg/L, t en horas) se elimina según `y' + 2y = 0`. Al comienzo hay `y(0) = 1 mg/L` y en `t = 1 h` se inyecta una dosis instantánea que suma 3 mg/L, modelada como `y' + 2y = 3·δ(t − 1)`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es `y(t)`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "y = e^(−2t) + 3·u_1(t)·e^(−2(t − 1))",
                        "y = e^(−2t) + 3·u_1(t)·e^(−2t)",
                        "y = e^(−2t) + 3·e^(−2(t − 1))",
                        "y = e^(−2t) + 3·u_1(t)",
                    ],
                    "correct": 0,
                },
                "answer": "y = e^(−2t) + 3·u_1(t)·e^(−2(t − 1))",
            },
            {
                "prompt": "b) ¿Cuál es la concentración justo después de la inyección (`t = 1⁺`)? Redondeá a 2 decimales. Respondé solo con el número en mg/L.",
                "check": {"type": "numeric", "value": 3.14, "tolerance": 0.01, "unit": "mg/L"},
                "answer": "3.14 mg/L",
            },
            {
                "prompt": "c) ¿Cuál es la concentración en `t = 2 h`? Redondeá a 3 decimales. Respondé solo con el número en mg/L.",
                "check": {"type": "numeric", "value": 0.424, "tolerance": 0.01, "unit": "mg/L"},
                "answer": "0.424 mg/L",
            },
        ],
        "hints": [
            "`L{δ(t − 1)} = e^(−s)`. Transformá y despejá `Y(s)`.",
            "`e^(−s)·1/(s + 2)` es la transformada de `u_1(t)·e^(−2(t − 1))`: retardo de 1 h.",
        ],
        "solution": [
            "Transformamos: `sY − 1 + 2Y = 3e^(−s)` → `Y = 1/(s + 2) + 3e^(−s)/(s + 2)`.",
            "`L⁻¹{1/(s + 2)} = e^(−2t)`; por el segundo teorema de traslación, `L⁻¹{e^(−s)/(s + 2)} = u_1(t)·e^(−2(t − 1))`.",
            "`y(t) = e^(−2t) + 3·u_1(t)·e^(−2(t − 1))`: antes de `t = 1` solo decae; en `t = 1` salta 3 mg/L y desde ahí cada parte decae con la misma constante.",
            "Justo después: `y(1⁺) = e^(−2) + 3 ≈ 0,135 + 3 = 3,135 ≈ 3,14 mg/L`.",
            "En `t = 2`: `y = e^(−4) + 3e^(−2) ≈ 0,0183 + 0,4060 = 0,4243 ≈ 0,424 mg/L`.",
            "Error típico: escribir `3u_1(t)·e^(−2t)` sin correr también la exponencial; la dosis aportaría solo `3e^(−2) ≈ 0,41` justo al inyectarla en vez de 3.",
        ],
    },
    {
        "id": "de-laplace-escalon-impulso-2",
        "node": "de-laplace-escalon-impulso",
        "kind": "problem",
        "level": 2,
        "title": "Funciones definidas por tramos con escalones",
        "statement": "Sea `f(t) = 3` para `0 ≤ t < 2` y `f(t) = t + 1` para `t ≥ 2`. Además, sea `g(t) = L⁻¹{ e^(−πs)·4/(s² + 4) }`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es `F(s) = L{f(t)}`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "F(s) = 3/s + e^(−2s)/s²",
                        "F(s) = 3/s + e^(−2s)·(1/s² + 3/s)",
                        "F(s) = 3/s + e^(−2s)·(1/s² + 2/s)",
                        "F(s) = 3/s + e^(2s)/s²",
                    ],
                    "correct": 0,
                },
                "answer": "F(s) = 3/s + e^(−2s)/s²",
            },
            {
                "prompt": "b) ¿Cuánto vale `g(5π/4)`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
        ],
        "hints": [
            "Escribí `f(t) = 3 + u_2(t)·[(t + 1) − 3]` y expresá lo que multiplica a `u_2(t)` en función de `(t − 2)`.",
            "`L{u_c(t)·h(t − c)} = e^(−cs)·H(s)`. Para `g`: `4/(s² + 4) = 2·(2/(s² + 4))`.",
        ],
        "solution": [
            "El escalón `u_2(t)` «cambia de fórmula» en `t = 2`: `f(t) = 3 + u_2(t)·(t + 1 − 3) = 3 + u_2(t)·(t − 2)`.",
            "`L{3} = 3/s` y, por el segundo teorema de traslación, `L{u_2(t)·(t − 2)} = e^(−2s)·L{t} = e^(−2s)/s²`. Así `F(s) = 3/s + e^(−2s)/s²`.",
            "Para `g`: `L⁻¹{4/(s² + 4)} = 2·sen(2t)`, y el factor `e^(−πs)` lo retrasa `π`: `g(t) = 2·u_π(t)·sen(2(t − π)) = 2·u_π(t)·sen(2t)`.",
            "`5π/4 > π`, así que el escalón ya está encendido: `g(5π/4) = 2·sen(5π/2) = 2·1 = 2`.",
            "Errores típicos: en a), escribir `u_2(t)·(t + 1)` sin restar el 3 (da `e^(−2s)(1/s² + 3/s)`); en b), olvidar el escalón y evaluar en `t < π` como si la función ya estuviera encendida.",
        ],
    },
    {
        "id": "de-laplace-escalon-impulso-3",
        "node": "de-laplace-escalon-impulso",
        "kind": "problem",
        "level": 3,
        "title": "Circuito RLC con una fuente que se enciende en t = 1 s",
        "statement": "Un circuito RLC serie con `L = 1 H`, `R = 2 Ω` y `C = 0,2 F` está descargado y sin corriente (`q(0) = 0`, `q'(0) = 0`). En `t = 1 s` se conecta una fuente de 10 V, así que la carga cumple `q'' + 2q' + 5q = 10·u_1(t)` (q en coulombs, t en segundos).",
        "parts": [
            {
                "prompt": "a) ¿Cuál es `q(t)` para `t ≥ 1`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "q = 2 − e^(−(t − 1))·[2cos(2(t − 1)) + sen(2(t − 1))]",
                        "q = 2 − e^(−t)·[2cos(2t) + sen(2t)]",
                        "q = 2 − e^(−(t − 1))·[2cos(2(t − 1)) + 2sen(2(t − 1))]",
                        "q = 2 − 2e^(−(t − 1))·cos(2(t − 1))",
                    ],
                    "correct": 0,
                },
                "answer": "q = 2 − e^(−(t − 1))·[2cos(2(t − 1)) + sen(2(t − 1))]",
            },
            {
                "prompt": "b) ¿Cuánto vale la carga en `t = 1 + π/2`? Redondeá a 2 decimales. Respondé solo con el número en C.",
                "check": {"type": "numeric", "value": 2.42, "tolerance": 0.01, "unit": "C"},
                "answer": "2.42 C",
            },
            {
                "prompt": "c) ¿Cuánto vale la corriente `i = q'` en `t = 1 + π/4`? Redondeá a 2 decimales. Respondé solo con el número en A.",
                "check": {"type": "numeric", "value": 2.28, "tolerance": 0.01, "unit": "A"},
                "answer": "2.28 A",
            },
        ],
        "hints": [
            "Transformando: `(s² + 2s + 5)·Q = 10e^(−s)/s`. Primero invertí `10/(s(s² + 2s + 5))` y después aplicá el retardo.",
            "`10/(s(s² + 2s + 5)) = 2/s − (2s + 4)/(s² + 2s + 5)`; completá cuadrados: `s² + 2s + 5 = (s + 1)² + 4`.",
            "Primer teorema de traslación: `(s + 1)/((s + 1)² + 4)` ↔ `e^(−t)cos 2t` y `2/((s + 1)² + 4)` ↔ `e^(−t)sen 2t`.",
        ],
        "solution": [
            "Con condiciones nulas: `(s² + 2s + 5)Q = 10e^(−s)/s` → `Q = e^(−s)·H(s)` con `H = 10/(s(s² + 2s + 5))`.",
            "Fracciones: `10 = A(s² + 2s + 5) + (Bs + C)s` → `A = 2`; `s²`: `0 = 2 + B` → `B = −2`; `s`: `0 = 4 + C` → `C = −4`. `H = 2/s − (2s + 4)/((s + 1)² + 4)`.",
            "`(2s + 4) = 2(s + 1) + 2`, así que `h(t) = 2 − 2e^(−t)cos 2t − e^(−t)sen 2t = 2 − e^(−t)(2cos 2t + sen 2t)`.",
            "Retardo de 1 s: `q(t) = u_1(t)·h(t − 1)`. Para `t ≥ 1`: `q = 2 − e^(−(t − 1))[2cos(2(t − 1)) + sen(2(t − 1))]` (vale 0 y tiene derivada 0 en `t = 1` ✓).",
            "b) Con `τ = t − 1 = π/2`: `q = 2 − e^(−π/2)(2cos π + sen π) = 2 + 2e^(−π/2) ≈ 2 + 0,416 = 2,42 C`.",
            "c) Derivando `h`: `h'(τ) = e^(−τ)(2cos 2τ + sen 2τ) − e^(−τ)(−4sen 2τ + 2cos 2τ) = 5e^(−τ)sen 2τ`. Con `τ = π/4`: `i = 5e^(−π/4) ≈ 2,28 A`.",
            "A largo plazo `q → 2 C = C·E = 0,2 · 10` (capacitor cargado) ✓. Error típico: no correr `t` en la exponencial y los trigonométricos (opción con `e^(−t)`), que no cumple `q(1) = 0`.",
        ],
    },
    # ==================== ESPACIOS E INDEPENDENCIA ====================
    {
        "id": "la-espacios-independencia-1",
        "node": "la-espacios-independencia",
        "kind": "problem",
        "level": 1,
        "title": "Valor de k que vuelve dependientes a tres vectores",
        "statement": "Sean `v₁ = ⟨1, 2, 1⟩`, `v₂ = ⟨2, 1, 0⟩` y `v₃ = ⟨1, −1, k⟩` en `ℝ³`.",
        "parts": [
            {
                "prompt": "a) ¿Para qué valor de `k` los tres vectores son linealmente dependientes? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -1, "tolerance": 0, "unit": ""},
                "answer": "−1",
            },
            {
                "prompt": "b) Para ese `k`, escribí `v₃ = a·v₁ + b·v₂`. ¿Cuánto vale `a`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -1, "tolerance": 0, "unit": ""},
                "answer": "−1",
            },
        ],
        "hints": [
            "Tres vectores de `ℝ³` son dependientes si y solo si el determinante de la matriz que forman es 0.",
            "Para b), igualá componente a componente: las dos primeras ecuaciones no dependen de `k`.",
        ],
        "solution": [
            "Determinante con los vectores como columnas: `det [[1, 2, 1], [2, 1, −1], [1, 0, k]] = 1·(k − 0) − 2·(2k + 1) + 1·(0 − 1) = −3k − 3`.",
            "`−3k − 3 = 0` → `k = −1`. Para cualquier otro `k` el determinante no es 0 y los vectores son independientes.",
            "b) `a⟨1, 2, 1⟩ + b⟨2, 1, 0⟩ = ⟨1, −1, −1⟩`: `a + 2b = 1` y `2a + b = −1`.",
            "De `2a + b = −1`, `b = −1 − 2a`; sustituyendo, `a − 2 − 4a = 1` → `a = −1`, `b = 1`.",
            "Tercera componente: `a·1 + b·0 = −1 = k` ✓. Entonces `v₃ = −v₁ + v₂` (efectivamente `⟨−1 + 2, −2 + 1, −1 + 0⟩ = ⟨1, −1, −1⟩`).",
        ],
    },
    {
        "id": "la-espacios-independencia-2",
        "node": "la-espacios-independencia",
        "kind": "problem",
        "level": 2,
        "title": "Dimensión y coordenadas en un subespacio de ℝ⁴",
        "statement": "Sea `W = gen{v₁, v₂, v₃, v₄}` con `v₁ = ⟨1, 1, 0, 2⟩`, `v₂ = ⟨2, 1, 1, 3⟩`, `v₃ = ⟨0, 1, −1, 1⟩` y `v₄ = ⟨1, 0, 1, 1⟩`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la dimensión de `W`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
            {
                "prompt": "b) Sabiendo que `{v₁, v₂}` es base de `W`, ¿cuáles son las coordenadas de `w = ⟨3, 1, 2, 4⟩` en esa base?",
                "check": {"type": "choice", "options": ["(−1, 2)", "(2, −1)", "(1, 1)", "w no pertenece a W"], "correct": 0},
                "answer": "(−1, 2)",
            },
            {
                "prompt": "c) ¿Cuántas ecuaciones lineales homogéneas independientes hacen falta, como mínimo, para describir `W` dentro de `ℝ⁴`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
        ],
        "hints": [
            "Escalona la matriz cuyas filas son `v₁, …, v₄` y contá las filas no nulas, o buscá relaciones como `v₃ = 2v₁ − v₂`.",
            "Para b), planteá `a·v₁ + b·v₂ = w` y comprobá que las cuatro ecuaciones se cumplan.",
            "Cada ecuación independiente baja la dimensión en 1, partiendo de 4.",
        ],
        "solution": [
            "`2v₁ − v₂ = ⟨2 − 2, 2 − 1, 0 − 1, 4 − 3⟩ = ⟨0, 1, −1, 1⟩ = v₃` y `v₂ − v₁ = ⟨1, 0, 1, 1⟩ = v₄`: `v₃` y `v₄` sobran.",
            "`v₁` y `v₂` no son múltiplos (la 3.ª componente de `v₁` es 0 y la de `v₂` no), así que son independientes: `dim W = 2`.",
            "b) `a⟨1, 1, 0, 2⟩ + b⟨2, 1, 1, 3⟩ = ⟨3, 1, 2, 4⟩`: de la 3.ª componente `b = 2`; de la 2.ª `a + b = 1` → `a = −1`.",
            "Comprobamos las otras: 1.ª `−1 + 4 = 3` ✓; 4.ª `−2 + 6 = 4` ✓. Entonces `w ∈ W` con coordenadas `(−1, 2)`.",
            "c) `W` tiene dimensión 2 en `ℝ⁴`: hacen falta `4 − 2 = 2` ecuaciones homogéneas independientes (2 restricciones).",
            "Error típico: decir que `dim W = 4` porque hay 4 vectores; la dimensión es la cantidad de vectores de una base, no de un conjunto generador cualquiera.",
        ],
    },
    {
        "id": "la-espacios-independencia-3",
        "node": "la-espacios-independencia",
        "kind": "problem",
        "level": 3,
        "title": "Base de ℝ³ según un parámetro",
        "statement": "Para cada número real `k` considerá `B_k = {⟨1, k, 1⟩, ⟨k, 1, 1⟩, ⟨1, 1, k⟩}`.",
        "parts": [
            {
                "prompt": "a) ¿Para qué valores de `k` el conjunto `B_k` es una base de `ℝ³`?",
                "check": {
                    "type": "choice",
                    "options": ["k ≠ 1 y k ≠ −2", "k ≠ 1", "k ≠ −2", "k ≠ 1 y k ≠ 2"],
                    "correct": 0,
                },
                "answer": "k ≠ 1 y k ≠ −2",
            },
            {
                "prompt": "b) Para `k = 1`, ¿qué dimensión tiene el subespacio generado por `B_k`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1",
            },
            {
                "prompt": "c) Para `k = −2`, ¿qué dimensión tiene el subespacio generado por `B_k`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
        ],
        "hints": [
            "Tres vectores de `ℝ³` forman base si y solo si su determinante no es 0.",
            "El determinante da un polinomio de grado 3 en `k`; `k = 1` es una raíz, así que podés factorizar por `(k − 1)`.",
            "En los valores críticos, contá cuántos vectores independientes quedan.",
        ],
        "solution": [
            "`det [[1, k, 1], [k, 1, 1], [1, 1, k]] = 1·(k − 1) − k·(k² − 1) + 1·(k − 1) = 2(k − 1) − k(k − 1)(k + 1)`.",
            "Sacando factor común: `(k − 1)(2 − k² − k) = −(k − 1)(k² + k − 2) = −(k − 1)²(k + 2)`.",
            "Se anula en `k = 1` y `k = −2`: `B_k` es base de `ℝ³` exactamente cuando `k ≠ 1` y `k ≠ −2`.",
            "b) Con `k = 1` los tres vectores son `⟨1, 1, 1⟩`: generan una recta, dimensión 1.",
            "c) Con `k = −2`: `⟨1, −2, 1⟩, ⟨−2, 1, 1⟩, ⟨1, 1, −2⟩`. Suman `⟨0, 0, 0⟩`, así que son dependientes, pero los dos primeros no son múltiplos: dimensión 2 (un plano).",
            "Error típico: resolver `k² + k − 2 = 0` como `(k − 1)(k − 2)`; la factorización correcta es `(k − 1)(k + 2)`.",
        ],
    },
    # ==================== NÚCLEO, COLUMNA Y RANGO ====================
    {
        "id": "la-nucleo-columna-rango-1",
        "node": "la-nucleo-columna-rango",
        "kind": "problem",
        "level": 1,
        "title": "Rango y un vector del núcleo",
        "statement": "Sea `A = [[1, 2, 0, 1], [2, 4, 1, 4], [3, 6, 1, 5]]` (matriz de 3 × 4).",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el rango de `A`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
            {
                "prompt": "b) ¿Cuál de estos vectores pertenece a `Nul(A)`?",
                "check": {
                    "type": "choice",
                    "options": ["⟨−3, 1, −2, 1⟩", "⟨−2, 1, 0, 1⟩", "⟨1, 0, −2, 1⟩", "⟨−1, 0, 2, 1⟩"],
                    "correct": 0,
                },
                "answer": "⟨−3, 1, −2, 1⟩",
            },
        ],
        "hints": [
            "Escalona: restá múltiplos de la fila 1 a las otras y fijate si alguna fila queda nula.",
            "De la forma escalonada reducida despejá las variables pivote en función de las libres `x₂` y `x₄`.",
        ],
        "solution": [
            "`F₂ − 2F₁ = [0, 0, 1, 2]` y `F₃ − 3F₁ = [0, 0, 1, 2]`; luego `F₃ − F₂ = [0, 0, 0, 0]`. Quedan 2 filas no nulas: `rango(A) = 2`.",
            "Forma reducida: `[[1, 2, 0, 1], [0, 0, 1, 2], [0, 0, 0, 0]]`. Pivotes en las columnas 1 y 3; libres `x₂` y `x₄`.",
            "`x₁ = −2x₂ − x₄` y `x₃ = −2x₄`. Base de `Nul(A)`: `⟨−2, 1, 0, 0⟩` y `⟨−1, 0, −2, 1⟩` (nulidad `4 − 2 = 2`).",
            "`⟨−3, 1, −2, 1⟩` es la suma de esos dos (con `x₂ = 1`, `x₄ = 1`). Comprobación: `A·⟨−3, 1, −2, 1⟩ = ⟨−3 + 2 + 0 + 1, −6 + 4 − 2 + 4, −9 + 6 − 2 + 5⟩ = ⟨0, 0, 0⟩` ✓.",
            "Los otros fallan: por ejemplo `A·⟨−2, 1, 0, 1⟩ = ⟨1, 4, 5⟩ ≠ 0`. Error típico: copiar `x₃ = +2x₄` sin pasar de miembro con el signo cambiado.",
        ],
    },
    {
        "id": "la-nucleo-columna-rango-2",
        "node": "la-nucleo-columna-rango",
        "kind": "problem",
        "level": 2,
        "title": "Cuándo b está en el espacio columna",
        "statement": "Sea `A = [[1, 2, −1], [2, 5, 1], [1, 3, 2]]` y `b = ⟨1, 4, k⟩`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el rango de `A`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
            {
                "prompt": "b) ¿Para qué valor de `k` el sistema `Ax = b` tiene solución (es decir, `b ∈ Col(A)`)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3",
            },
            {
                "prompt": "c) Con ese `k`, ¿cuál es la solución general (`t ∈ ℝ`)?",
                "check": {
                    "type": "choice",
                    "options": [
                        "x = ⟨−3, 2, 0⟩ + t⟨7, −3, 1⟩",
                        "x = ⟨−3, 2, 0⟩ + t⟨−7, 3, 1⟩",
                        "x = ⟨1, 0, 0⟩ + t⟨7, −3, 1⟩",
                        "x = ⟨2, 2, 0⟩ + t⟨7, −3, 1⟩",
                    ],
                    "correct": 0,
                },
                "answer": "x = ⟨−3, 2, 0⟩ + t⟨7, −3, 1⟩",
            },
        ],
        "hints": [
            "Escalona la matriz ampliada `[A | b]` dejando `k` como incógnita.",
            "Si queda una fila `[0, 0, 0 | algo]`, ese «algo» tiene que ser 0 para que haya solución.",
            "La solución general es una solución particular más el núcleo: `x = x_p + t·n` con `A·n = 0`.",
        ],
        "solution": [
            "`[A | b]`: `F₂ − 2F₁ = [0, 1, 3 | 2]`, `F₃ − F₁ = [0, 1, 3 | k − 1]`, y `F₃ − F₂ = [0, 0, 0 | k − 3]`.",
            "Queda una fila nula en `A`: `rango(A) = 2`. Hay solución solo si `k − 3 = 0` → `k = 3` (`Col(A)` es el plano `b₃ = b₂ − b₁`).",
            "Con `k = 3`: `x₂ + 3x₃ = 2` y, de `F₁ − 2F₂`: `x₁ − 7x₃ = −3`. Variable libre `x₃ = t`.",
            "`x₁ = −3 + 7t`, `x₂ = 2 − 3t`, `x₃ = t` → `x = ⟨−3, 2, 0⟩ + t⟨7, −3, 1⟩`.",
            "Comprobación: `A⟨−3, 2, 0⟩ = ⟨1, 4, 3⟩` ✓ y `A⟨7, −3, 1⟩ = ⟨7 − 6 − 1, 14 − 15 + 1, 7 − 9 + 2⟩ = ⟨0, 0, 0⟩` ✓. Las otras opciones fallan: `A⟨−7, 3, 1⟩ ≠ 0` y `A⟨1, 0, 0⟩ = ⟨1, 2, 1⟩ ≠ b`.",
        ],
    },
    {
        "id": "la-nucleo-columna-rango-3",
        "node": "la-nucleo-columna-rango",
        "kind": "problem",
        "level": 3,
        "title": "Bases del núcleo y de la imagen con el teorema de la dimensión",
        "statement": "Sea `A = [[1, 2, 1, 0, 3], [2, 4, 3, 1, 7], [1, 2, 2, 1, 4]]`, que define `T: ℝ⁵ → ℝ³`, `T(x) = Ax`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la dimensión del núcleo de `A`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3",
            },
            {
                "prompt": "b) ¿Cuál es una base de `Col(A)` (la imagen de `T`)?",
                "check": {
                    "type": "choice",
                    "options": [
                        "{⟨1, 2, 1⟩, ⟨1, 3, 2⟩}",
                        "{⟨1, 0, 0⟩, ⟨0, 1, 0⟩}",
                        "{⟨1, 2, 1⟩, ⟨2, 4, 2⟩}",
                        "{⟨1, 2, 0, −1, 2⟩, ⟨0, 0, 1, 1, 1⟩}",
                    ],
                    "correct": 0,
                },
                "answer": "{⟨1, 2, 1⟩, ⟨1, 3, 2⟩}",
            },
            {
                "prompt": "c) ¿Cuál es una base de `Nul(A)`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "{⟨−2, 1, 0, 0, 0⟩, ⟨1, 0, −1, 1, 0⟩, ⟨−2, 0, −1, 0, 1⟩}",
                        "{⟨2, 1, 0, 0, 0⟩, ⟨1, 0, 1, 1, 0⟩, ⟨2, 0, 1, 0, 1⟩}",
                        "{⟨−2, 1, 0, 0, 0⟩, ⟨1, 0, −1, 1, 0⟩}",
                        "{⟨1, 2, 0, −1, 2⟩, ⟨0, 0, 1, 1, 1⟩, ⟨0, 0, 0, 0, 0⟩}",
                    ],
                    "correct": 0,
                },
                "answer": "{⟨−2, 1, 0, 0, 0⟩, ⟨1, 0, −1, 1, 0⟩, ⟨−2, 0, −1, 0, 1⟩}",
            },
        ],
        "hints": [
            "Llevá `A` a forma escalonada reducida e identificá las columnas pivote.",
            "La base de `Col(A)` se toma con las columnas pivote de la matriz ORIGINAL, no de la reducida.",
            "Para el núcleo, despejá las variables pivote en función de las libres y dale a cada libre el valor 1 (y 0 a las demás).",
        ],
        "solution": [
            "`F₂ − 2F₁ = [0, 0, 1, 1, 1]`, `F₃ − F₁ = [0, 0, 1, 1, 1]` → `F₃ − F₂ = 0`. Luego `F₁ − F₂ = [1, 2, 0, −1, 2]`.",
            "Forma reducida: `[[1, 2, 0, −1, 2], [0, 0, 1, 1, 1], [0, 0, 0, 0, 0]]`. Pivotes en columnas 1 y 3: `rango = 2`.",
            "Teorema de la dimensión: `dim Nul(A) = 5 − 2 = 3` (variables libres `x₂, x₄, x₅`).",
            "`Col(A)`: columnas 1 y 3 de `A`, `{⟨1, 2, 1⟩, ⟨1, 3, 2⟩}`. Las columnas de la reducida (`⟨1, 0, 0⟩, ⟨0, 1, 0⟩`) no sirven: por ejemplo `⟨1, 0, 0⟩` no está en `Col(A)` (no cumple `b₃ = b₂ − b₁`).",
            "Núcleo: `x₁ = −2x₂ + x₄ − 2x₅` y `x₃ = −x₄ − x₅`. Con `(x₂, x₄, x₅) = (1, 0, 0), (0, 1, 0), (0, 0, 1)` salen `⟨−2, 1, 0, 0, 0⟩`, `⟨1, 0, −1, 1, 0⟩`, `⟨−2, 0, −1, 0, 1⟩`.",
            "Verificación: `A` por cada uno da `⟨0, 0, 0⟩` ✓. La opción con dos vectores no alcanza (hacen falta 3) y la de signos cambiados no está en el núcleo (`A⟨2, 1, 0, 0, 0⟩ = ⟨4, 8, 4⟩`). Las filas de la reducida son base del espacio fila, no del núcleo.",
        ],
    },
    # ==================== TRANSFORMACIONES LINEALES ====================
    {
        "id": "la-transformaciones-lineales-1",
        "node": "la-transformaciones-lineales",
        "kind": "problem",
        "level": 1,
        "title": "Matriz a partir de las imágenes de dos vectores",
        "statement": "Una transformación lineal `T: ℝ² → ℝ²` cumple `T(⟨1, 1⟩) = ⟨3, 1⟩` y `T(⟨1, −1⟩) = ⟨1, 5⟩`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la matriz `A` de `T` en la base canónica?",
                "check": {
                    "type": "choice",
                    "options": ["[[2, 1], [3, −2]]", "[[2, 3], [1, −2]]", "[[3, 1], [1, 5]]", "[[1, 2], [−2, 3]]"],
                    "correct": 0,
                },
                "answer": "[[2, 1], [3, −2]]",
            },
            {
                "prompt": "b) ¿Cuál es la segunda componente de `T(⟨4, 2⟩)`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 8, "tolerance": 0, "unit": ""},
                "answer": "8",
            },
        ],
        "hints": [
            "Escribí `e₁` y `e₂` como combinación de `⟨1, 1⟩` y `⟨1, −1⟩`: `e₁ = ½(⟨1, 1⟩ + ⟨1, −1⟩)`.",
            "Por linealidad `T(e₁) = ½(T⟨1, 1⟩ + T⟨1, −1⟩)`. Las columnas de `A` son `T(e₁)` y `T(e₂)`.",
        ],
        "solution": [
            "`e₁ = ½(⟨1, 1⟩ + ⟨1, −1⟩)` → `T(e₁) = ½(⟨3, 1⟩ + ⟨1, 5⟩) = ⟨2, 3⟩`.",
            "`e₂ = ½(⟨1, 1⟩ − ⟨1, −1⟩)` → `T(e₂) = ½(⟨3, 1⟩ − ⟨1, 5⟩) = ⟨1, −2⟩`.",
            "Columnas: `A = [[2, 1], [3, −2]]`. Comprobación: `A⟨1, 1⟩ = ⟨3, 1⟩` ✓ y `A⟨1, −1⟩ = ⟨1, 5⟩` ✓.",
            "`T(⟨4, 2⟩) = ⟨2·4 + 1·2, 3·4 − 2·2⟩ = ⟨10, 8⟩`: la segunda componente es 8.",
            "Error típico: poner `T(e₁)` y `T(e₂)` como filas (`[[2, 3], [1, −2]]`), o usar directamente las imágenes dadas como columnas, aunque no son imágenes de `e₁` y `e₂`.",
        ],
    },
    {
        "id": "la-transformaciones-lineales-2",
        "node": "la-transformaciones-lineales",
        "kind": "problem",
        "level": 2,
        "title": "Composición de una rotación y una reflexión",
        "statement": "Sea `T: ℝ² → ℝ²` la transformación que primero rota cada vector 90° en sentido antihorario y después lo refleja respecto del eje `x`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la matriz de `T`?",
                "check": {
                    "type": "choice",
                    "options": ["[[0, −1], [−1, 0]]", "[[0, 1], [1, 0]]", "[[0, −1], [1, 0]]", "[[0, 1], [−1, 0]]"],
                    "correct": 0,
                },
                "answer": "[[0, −1], [−1, 0]]",
            },
            {
                "prompt": "b) ¿Cuál es la segunda componente de `T(⟨2, 5⟩)`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -2, "tolerance": 0, "unit": ""},
                "answer": "−2",
            },
            {
                "prompt": "c) ¿Qué transformación geométrica es `T`?",
                "check": {
                    "type": "choice",
                    "options": [
                        "La reflexión respecto de la recta y = −x",
                        "La reflexión respecto de la recta y = x",
                        "La rotación de 90° en sentido horario",
                        "La rotación de 180°",
                    ],
                    "correct": 0,
                },
                "answer": "La reflexión respecto de la recta y = −x",
            },
        ],
        "hints": [
            "Rotación 90° antihoraria: `R = [[0, −1], [1, 0]]`; reflexión respecto del eje `x`: `S = [[1, 0], [0, −1]]`.",
            "Lo que se aplica primero queda a la DERECHA en el producto: `T = S·R`.",
            "Para c), mirá qué vectores quedan fijos y cuáles cambian de signo.",
        ],
        "solution": [
            "`T(x) = S(R(x))`, así que su matriz es `S·R = [[1, 0], [0, −1]]·[[0, −1], [1, 0]] = [[0, −1], [−1, 0]]`.",
            "Comprobación con la base: `e₁` → (rota) `⟨0, 1⟩` → (refleja) `⟨0, −1⟩`, primera columna ✓; `e₂` → `⟨−1, 0⟩` → `⟨−1, 0⟩`, segunda columna ✓.",
            "`T(⟨2, 5⟩) = ⟨0·2 − 1·5, −1·2 + 0·5⟩ = ⟨−5, −2⟩`.",
            "`T(x, y) = (−y, −x)`: deja fijo `⟨1, −1⟩` (`T⟨1, −1⟩ = ⟨1, −1⟩`) y cambia de signo `⟨1, 1⟩`. Es la reflexión respecto de `y = −x`.",
            "Error típico: multiplicar en el orden de la lectura, `R·S = [[0, 1], [1, 0]]`, que es la reflexión respecto de `y = x` (otra transformación).",
        ],
    },
    {
        "id": "la-transformaciones-lineales-3",
        "node": "la-transformaciones-lineales",
        "kind": "problem",
        "level": 3,
        "title": "Matriz de una transformación en otra base",
        "statement": "Sea `T(x, y) = (x + 2y, 3x)` y la base `B = {b₁, b₂}` con `b₁ = ⟨1, 1⟩` y `b₂ = ⟨1, 2⟩`. Llamá `P = [[1, 1], [1, 2]]` a la matriz cuyas columnas son `b₁` y `b₂`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la matriz `[T]_B` de `T` en la base `B`?",
                "check": {
                    "type": "choice",
                    "options": ["[[3, 7], [0, −2]]", "[[6, −2], [12, −5]]", "[[3, 0], [7, −2]]", "[[1, 2], [3, 0]]"],
                    "correct": 0,
                },
                "answer": "[[3, 7], [0, −2]]",
            },
            {
                "prompt": "b) Para `v = ⟨2, 3⟩`, ¿cuál es la primera coordenada de `[T(v)]_B`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 10, "tolerance": 0, "unit": ""},
                "answer": "10",
            },
            {
                "prompt": "c) ¿Cuánto vale `det([T]_B)`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -6, "tolerance": 0, "unit": ""},
                "answer": "−6",
            },
        ],
        "hints": [
            "La matriz canónica es `A = [[1, 2], [3, 0]]` y `[T]_B = P⁻¹·A·P`.",
            "`P⁻¹ = [[2, −1], [−1, 1]]` (determinante de `P` igual a 1).",
            "Para b): `[T(v)]_B = [T]_B·[v]_B`, con `[v]_B = P⁻¹·v`.",
        ],
        "solution": [
            "Matriz canónica (columnas `T(e₁) = ⟨1, 3⟩`, `T(e₂) = ⟨2, 0⟩`): `A = [[1, 2], [3, 0]]`. `det P = 2 − 1 = 1` → `P⁻¹ = [[2, −1], [−1, 1]]`.",
            "`A·P = [[3, 5], [3, 3]]` y `P⁻¹·(A·P) = [[6 − 3, 10 − 3], [−3 + 3, −5 + 3]] = [[3, 7], [0, −2]]`.",
            "Interpretación: `T(b₁) = ⟨3, 3⟩ = 3b₁ + 0b₂` (primera columna) y `T(b₂) = ⟨5, 3⟩ = 7b₁ − 2b₂` (segunda columna) ✓.",
            "b) `[v]_B = P⁻¹⟨2, 3⟩ = ⟨4 − 3, −2 + 3⟩ = ⟨1, 1⟩` (en efecto `b₁ + b₂ = ⟨2, 3⟩`). `[T(v)]_B = [[3, 7], [0, −2]]·⟨1, 1⟩ = ⟨10, −2⟩`.",
            "Comprobación en canónica: `T(v) = (2 + 6, 6) = ⟨8, 6⟩ = 10⟨1, 1⟩ − 2⟨1, 2⟩` ✓.",
            "c) `det([T]_B) = 3·(−2) − 7·0 = −6 = det(A)`: matrices semejantes tienen el mismo determinante. Error típico: calcular `P·A·P⁻¹ = [[6, −2], [12, −5]]` (orden invertido).",
        ],
    },
    # ==================== PROYECCIONES ORTOGONALES ====================
    {
        "id": "la-proyecciones-ortogonales-1",
        "node": "la-proyecciones-ortogonales",
        "kind": "problem",
        "level": 1,
        "title": "Distancia de un punto a una recta por el origen",
        "statement": "Sea `L` la recta de `ℝ³` que pasa por el origen con dirección `u = ⟨1, 2, 2⟩`, y sea `P = (6, 6, 0)`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la tercera componente de la proyección ortogonal de `v = ⟨6, 6, 0⟩` sobre `u`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4",
            },
            {
                "prompt": "b) ¿Cuál es la distancia de `P` a la recta `L`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""},
                "answer": "6",
            },
        ],
        "hints": [
            "`proj_u(v) = [(v · u)/(u · u)]·u`. Ojo: `u` no es unitario.",
            "La distancia es la longitud del vector error `v − proj_u(v)`.",
        ],
        "solution": [
            "`v · u = 6 + 12 + 0 = 18` y `u · u = 1 + 4 + 4 = 9` → coeficiente `18/9 = 2`.",
            "`proj_u(v) = 2⟨1, 2, 2⟩ = ⟨2, 4, 4⟩`: tercera componente 4.",
            "Error: `e = v − proj = ⟨4, 2, −4⟩`. Comprobamos que es perpendicular a `u`: `4 + 4 − 8 = 0` ✓.",
            "Distancia: `|e| = √(16 + 4 + 16) = √36 = 6`.",
            "Error típico: dividir por `|u| = 3` en vez de por `|u|² = 9`, que da una proyección tres veces más larga.",
        ],
    },
    {
        "id": "la-proyecciones-ortogonales-2",
        "node": "la-proyecciones-ortogonales",
        "kind": "problem",
        "level": 2,
        "title": "Completar una base ortonormal y leer coordenadas",
        "statement": "Sean `q₁ = (1/3)⟨1, 2, 2⟩`, `q₂ = (1/3)⟨2, 1, −2⟩` y `q₃ = (1/3)⟨2, −2, k⟩`. Sea `v = ⟨3, 6, 9⟩`.",
        "parts": [
            {
                "prompt": "a) ¿Para qué valor de `k` el conjunto `{q₁, q₂, q₃}` es una base ortonormal de `ℝ³`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1",
            },
            {
                "prompt": "b) ¿Cuál es la coordenada de `v` sobre `q₁`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 11, "tolerance": 0, "unit": ""},
                "answer": "11",
            },
            {
                "prompt": "c) ¿Cuál es la coordenada de `v` sobre `q₂`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -2, "tolerance": 0, "unit": ""},
                "answer": "−2",
            },
        ],
        "hints": [
            "Pedí `q₁ · q₃ = 0` y `q₂ · q₃ = 0`; después controlá que `|q₃| = 1`.",
            "En una base ortonormal no hace falta resolver un sistema: la coordenada sobre `qᵢ` es `v · qᵢ`.",
        ],
        "solution": [
            "`q₁ · q₂ = (2 + 2 − 4)/9 = 0` ✓, y `|q₁| = |q₂| = √9/3 = 1` ✓.",
            "`q₁ · q₃ = (2 − 4 + 2k)/9 = 0` → `k = 1`; también `q₂ · q₃ = (4 − 2 − 2k)/9 = 0` con `k = 1` ✓, y `|q₃| = √(4 + 4 + 1)/3 = 1` ✓.",
            "`c₁ = v · q₁ = (3 + 12 + 18)/3 = 11`.",
            "`c₂ = v · q₂ = (6 + 6 − 18)/3 = −2` (y `c₃ = v · q₃ = (6 − 12 + 9)/3 = 1`).",
            "Verificación: `c₁² + c₂² + c₃² = 121 + 4 + 1 = 126 = |v|² = 9 + 36 + 81` ✓ (una matriz ortogonal conserva longitudes). Error típico: olvidar el factor `1/3` de `qᵢ` y obtener coordenadas 3 veces más grandes.",
        ],
    },
    {
        "id": "la-proyecciones-ortogonales-3",
        "node": "la-proyecciones-ortogonales",
        "kind": "problem",
        "level": 3,
        "title": "Proyección sobre un plano y matriz de proyección",
        "statement": "Sea `W = gen{u₁, u₂} ⊂ ℝ³` con `u₁ = ⟨1, 0, 1⟩` y `u₂ = ⟨1, 2, −1⟩`, y sea `b = ⟨2, 5, 0⟩`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es la proyección ortogonal de `b` sobre `W`?",
                "check": {
                    "type": "choice",
                    "options": ["⟨3, 4, −1⟩", "⟨−1, 1, 1⟩", "⟨2, 4, −2⟩", "⟨14, 24, −10⟩"],
                    "correct": 0,
                },
                "answer": "⟨3, 4, −1⟩",
            },
            {
                "prompt": "b) ¿Cuál es la distancia de `b` al plano `W`? Redondeá a 2 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1.73, "tolerance": 0.01, "unit": ""},
                "answer": "1.73 (= √3)",
            },
            {
                "prompt": "c) Sea `P` la matriz de 3 × 3 que proyecta ortogonalmente sobre `W`. ¿Cuánto vale su entrada `P₂₂` (fila 2, columna 2)? Podés escribirla como fracción o redondeada a 2 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2 / 3, "tolerance": 0.01, "unit": ""},
                "answer": "2/3 (≈ 0.67)",
            },
        ],
        "hints": [
            "Primero comprobá que `u₁ · u₂ = 0`: con una base ortogonal, la proyección es la suma de las proyecciones sobre cada vector.",
            "La distancia es la longitud de `b − proj_W(b)`, que debe ser perpendicular a `u₁` y a `u₂`.",
            "`P = u₁u₁ᵀ/(u₁ · u₁) + u₂u₂ᵀ/(u₂ · u₂)`.",
        ],
        "solution": [
            "`u₁ · u₂ = 1 + 0 − 1 = 0`: base ortogonal de `W`. `u₁ · u₁ = 2`, `u₂ · u₂ = 6`.",
            "`b · u₁ = 2` y `b · u₂ = 2 + 10 = 12`. `proj_W(b) = (2/2)u₁ + (12/6)u₂ = ⟨1, 0, 1⟩ + ⟨2, 4, −2⟩ = ⟨3, 4, −1⟩`.",
            "Error: `e = b − proj = ⟨−1, 1, 1⟩`. `e · u₁ = −1 + 1 = 0` ✓ y `e · u₂ = −1 + 2 − 1 = 0` ✓, así que `e ∈ W⊥`.",
            "Distancia: `|e| = √3 ≈ 1,73`.",
            "`P₂₂ = (0·0)/2 + (2·2)/6 = 4/6 = 2/3`. (La matriz completa es `(1/3)[[2, 1, 1], [1, 2, −1], [1, −1, 2]]`, y `P·b = ⟨3, 4, −1⟩` ✓.)",
            "Distractores: `⟨−1, 1, 1⟩` es la componente en `W⊥`; `⟨2, 4, −2⟩` es solo la proyección sobre `u₂`; `⟨14, 24, −10⟩` sale de no dividir por `uᵢ · uᵢ`.",
        ],
    },
    # ==================== GRAM-SCHMIDT Y MÍNIMOS CUADRADOS ====================
    {
        "id": "la-gram-schmidt-minimos-1",
        "node": "la-gram-schmidt-minimos",
        "kind": "problem",
        "level": 1,
        "title": "Gram-Schmidt con dos vectores de ℝ³",
        "statement": "Aplicá Gram-Schmidt a `v₁ = ⟨1, 2, 2⟩` y `v₂ = ⟨3, 0, 3⟩` (tomando `w₁ = v₁`).",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el vector `w₂ = v₂ − proj_{w₁}(v₂)`?",
                "check": {
                    "type": "choice",
                    "options": ["⟨2, −2, 1⟩", "⟨0, −6, −3⟩", "⟨−6, −18, −15⟩", "⟨4, 2, 5⟩"],
                    "correct": 0,
                },
                "answer": "⟨2, −2, 1⟩",
            },
            {
                "prompt": "b) ¿Cuánto vale `|w₂|`, la longitud por la que hay que dividir para obtener `q₂`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 3, "tolerance": 0, "unit": ""},
                "answer": "3",
            },
        ],
        "hints": [
            "`proj_{w₁}(v₂) = [(v₂ · w₁)/(w₁ · w₁)]·w₁`.",
            "Comprobá al final que `w₂ · w₁ = 0`.",
        ],
        "solution": [
            "`v₂ · w₁ = 3 + 0 + 6 = 9` y `w₁ · w₁ = 1 + 4 + 4 = 9` → coeficiente `9/9 = 1`.",
            "`proj_{w₁}(v₂) = ⟨1, 2, 2⟩` → `w₂ = ⟨3, 0, 3⟩ − ⟨1, 2, 2⟩ = ⟨2, −2, 1⟩`.",
            "Comprobación: `w₂ · w₁ = 2 − 4 + 2 = 0` ✓.",
            "`|w₂| = √(4 + 4 + 1) = 3` → `q₂ = (1/3)⟨2, −2, 1⟩` (y `q₁ = (1/3)⟨1, 2, 2⟩`).",
            "Errores típicos: dividir por `|w₁| = 3` en vez de `|w₁|² = 9` (da `⟨0, −6, −3⟩`), no dividir nada (`⟨−6, −18, −15⟩`) o sumar la proyección en lugar de restarla (`⟨4, 2, 5⟩`).",
        ],
    },
    {
        "id": "la-gram-schmidt-minimos-2",
        "node": "la-gram-schmidt-minimos",
        "kind": "problem",
        "level": 2,
        "title": "Factorización QR y mínimos cuadrados",
        "statement": "Sea `A` la matriz de 3 × 2 con columnas `a₁ = ⟨2, 2, 1⟩` y `a₂ = ⟨3, 6, 0⟩`, y sea `b = ⟨3, 3, 6⟩`. El sistema `Ax = b` no tiene solución exacta.",
        "parts": [
            {
                "prompt": "a) Al aplicar Gram-Schmidt a las columnas de `A`, ¿cuál es `q₂`?",
                "check": {
                    "type": "choice",
                    "options": ["(1/3)⟨−1, 2, −2⟩", "⟨−1, 2, −2⟩", "(1/√5)⟨1, 2, 0⟩", "(1/(3√2))⟨1, 4, −1⟩"],
                    "correct": 0,
                },
                "answer": "(1/3)⟨−1, 2, −2⟩",
            },
            {
                "prompt": "b) En `A = QR` con `R = [[r₁₁, r₁₂], [0, r₂₂]]`, ¿cuánto vale `r₁₂`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 6, "tolerance": 0, "unit": ""},
                "answer": "6",
            },
            {
                "prompt": "c) ¿Cuál es la segunda componente de la solución por mínimos cuadrados `x̂`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -1, "tolerance": 0, "unit": ""},
                "answer": "−1",
            },
        ],
        "hints": [
            "`q₁ = a₁/|a₁|`; después `w₂ = a₂ − (a₂ · q₁)q₁` y `q₂ = w₂/|w₂|`.",
            "Las entradas de `R` son `r₁₁ = |a₁|`, `r₁₂ = q₁ · a₂` y `r₂₂ = |w₂|`.",
            "Mínimos cuadrados con QR: `R·x̂ = Qᵀb` (o, si preferís, `AᵀA·x̂ = Aᵀb`).",
        ],
        "solution": [
            "`|a₁| = √(4 + 4 + 1) = 3` → `q₁ = (1/3)⟨2, 2, 1⟩`, `r₁₁ = 3`.",
            "`r₁₂ = q₁ · a₂ = (6 + 12 + 0)/3 = 6`. `w₂ = a₂ − 6q₁ = ⟨3, 6, 0⟩ − ⟨4, 4, 2⟩ = ⟨−1, 2, −2⟩`.",
            "`|w₂| = 3 = r₂₂` → `q₂ = (1/3)⟨−1, 2, −2⟩`. Comprobación: `q₁ · q₂ = (−2 + 4 − 2)/9 = 0` ✓.",
            "`Qᵀb = ⟨q₁ · b, q₂ · b⟩ = ⟨(6 + 6 + 6)/3, (−3 + 6 − 12)/3⟩ = ⟨6, −3⟩`.",
            "`R·x̂ = Qᵀb`: `3x̂₂ = −3` → `x̂₂ = −1`; `3x̂₁ + 6x̂₂ = 6` → `x̂₁ = 4`.",
            "Verificación con las ecuaciones normales: `AᵀA = [[9, 18], [18, 45]]`, `Aᵀb = ⟨18, 27⟩`; `9·4 + 18·(−1) = 18` ✓ y `18·4 + 45·(−1) = 27` ✓. Error típico: olvidar normalizar `w₂` (da `⟨−1, 2, −2⟩`, que no tiene longitud 1).",
        ],
    },
    {
        "id": "la-gram-schmidt-minimos-3",
        "node": "la-gram-schmidt-minimos",
        "kind": "problem",
        "level": 3,
        "title": "Recta de mínimos cuadrados para un resorte",
        "statement": "En el laboratorio de Física colgás masas de un resorte y medís su longitud: `(1 kg, 3 cm)`, `(2 kg, 5 cm)`, `(3 kg, 6 cm)` y `(4 kg, 9 cm)`. Buscás la recta `y = m·x + c` (x en kg, y en cm) que mejor ajusta los datos por mínimos cuadrados.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale la pendiente `m`? Respondé solo con el número en cm/kg.",
                "check": {"type": "numeric", "value": 1.9, "tolerance": 0, "unit": "cm/kg"},
                "answer": "1.9 cm/kg",
            },
            {
                "prompt": "b) ¿Cuánto vale la ordenada al origen `c`? Respondé solo con el número en cm.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": "cm"},
                "answer": "1 cm",
            },
            {
                "prompt": "c) ¿Cuánto vale la suma de los cuadrados de los residuos `|b − Ax̂|²`? Respondé solo con el número en cm².",
                "check": {"type": "numeric", "value": 0.7, "tolerance": 0, "unit": "cm²"},
                "answer": "0.7 cm²",
            },
        ],
        "hints": [
            "Armá `A` con filas `[xᵢ, 1]` y `b` con los `yᵢ`; las incógnitas son `(m, c)`.",
            "Ecuaciones normales: `AᵀA = [[Σx², Σx], [Σx, n]]` y `Aᵀb = ⟨Σxy, Σy⟩`.",
            "Para c), calculá cada predicción `m·xᵢ + c`, restala del dato y sumá los cuadrados.",
        ],
        "solution": [
            "`Σx = 10`, `Σx² = 1 + 4 + 9 + 16 = 30`, `n = 4`, `Σy = 23`, `Σxy = 3 + 10 + 18 + 36 = 67`.",
            "Ecuaciones normales: `30m + 10c = 67` y `10m + 4c = 23`.",
            "Multiplicando la segunda por 2,5: `25m + 10c = 57,5`. Restando de la primera: `5m = 9,5` → `m = 1,9 cm/kg`.",
            "`10·1,9 + 4c = 23` → `4c = 4` → `c = 1 cm`. Recta: `y = 1,9x + 1`.",
            "Predicciones: `2,9; 4,8; 6,7; 8,6`. Residuos: `0,1; 0,2; −0,7; 0,4` (suman 0, como debe pasar cuando el modelo tiene término constante).",
            "`|b − Ax̂|² = 0,01 + 0,04 + 0,49 + 0,16 = 0,70 cm²`. Ninguna otra recta da una suma menor.",
            "Error típico: usar `Σx = 10` en lugar de `n = 4` en la entrada inferior derecha de `AᵀA`, o intentar `A⁻¹b` con una matriz de 4 × 2, que no tiene inversa.",
        ],
    },
    # ==================== EIGENVALORES Y EIGENVECTORES ====================
    {
        "id": "la-eigenvalores-eigenvectores-1",
        "node": "la-eigenvalores-eigenvectores",
        "kind": "problem",
        "level": 1,
        "title": "Autovalores y autovector de una matriz 2 × 2",
        "statement": "Sea `A = [[1, 2], [3, 2]]`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el MAYOR autovalor de `A`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 4, "tolerance": 0, "unit": ""},
                "answer": "4",
            },
            {
                "prompt": "b) ¿Cuál de estos es un autovector asociado a ese autovalor?",
                "check": {"type": "choice", "options": ["⟨2, 3⟩", "⟨3, 2⟩", "⟨1, −1⟩", "⟨−2, 3⟩"], "correct": 0},
                "answer": "⟨2, 3⟩",
            },
        ],
        "hints": [
            "`det(A − λI) = (1 − λ)(2 − λ) − 6`; o usá traza y determinante: `λ² − 3λ + (−4) = 0`.",
            "Para el autovector resolvé `(A − 4I)v = 0`.",
        ],
        "solution": [
            "`det(A − λI) = (1 − λ)(2 − λ) − 6 = λ² − 3λ − 4 = (λ − 4)(λ + 1)` → `λ = 4` y `λ = −1`.",
            "Chequeo: `4 + (−1) = 3 = traza` ✓ y `4·(−1) = −4 = det(A) = 2 − 6` ✓.",
            "`A − 4I = [[−3, 2], [3, −2]]`: la ecuación `−3x + 2y = 0` da `y = (3/2)x` → `v = ⟨2, 3⟩`.",
            "Comprobación: `A⟨2, 3⟩ = ⟨2 + 6, 6 + 6⟩ = ⟨8, 12⟩ = 4⟨2, 3⟩` ✓.",
            "Los otros fallan: `A⟨3, 2⟩ = ⟨7, 13⟩` no es múltiplo; `⟨1, −1⟩` es autovector de `λ = −1`, no de 4. Error típico: invertir las componentes y responder `⟨3, 2⟩`.",
        ],
    },
    {
        "id": "la-eigenvalores-eigenvectores-2",
        "node": "la-eigenvalores-eigenvectores",
        "kind": "problem",
        "level": 2,
        "title": "Autovalor doble en una matriz 3 × 3",
        "statement": "Sea `A = [[4, 0, 1], [2, 3, 2], [1, 0, 4]]`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el MAYOR autovalor de `A`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 5, "tolerance": 0, "unit": ""},
                "answer": "5",
            },
            {
                "prompt": "b) ¿Cuál es la multiplicidad algebraica del autovalor `λ = 3`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
            {
                "prompt": "c) ¿Qué dimensión tiene el autoespacio de `λ = 3`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 2, "tolerance": 0, "unit": ""},
                "answer": "2",
            },
        ],
        "hints": [
            "Desarrollá `det(A − λI)` por la segunda columna: tiene dos ceros.",
            "La dimensión del autoespacio es `3 − rango(A − 3I)`.",
        ],
        "solution": [
            "Desarrollando por la columna 2: `det(A − λI) = (3 − λ)·det[[4 − λ, 1], [1, 4 − λ]] = (3 − λ)·((4 − λ)² − 1)`.",
            "`(4 − λ)² − 1 = (3 − λ)(5 − λ)`, así que `det(A − λI) = (3 − λ)²(5 − λ)`: autovalores `3` (doble) y `5`.",
            "Chequeo: `3 + 3 + 5 = 11 = traza` ✓ y `3·3·5 = 45 = det(A)` ✓.",
            "`A − 3I = [[1, 0, 1], [2, 0, 2], [1, 0, 1]]`: todas las filas son múltiplos de `[1, 0, 1]` → rango 1 → autoespacio de dimensión `3 − 1 = 2` (base: `⟨0, 1, 0⟩` y `⟨1, 0, −1⟩`).",
            "Como la multiplicidad geométrica (2) iguala a la algebraica (2), esta matriz sí es diagonalizable. Error típico: suponer que un autovalor doble siempre tiene un solo autovector.",
        ],
    },
    {
        "id": "la-eigenvalores-eigenvectores-3",
        "node": "la-eigenvalores-eigenvectores",
        "kind": "problem",
        "level": 3,
        "title": "Parámetro a partir de un autovector conocido",
        "statement": "Sea `A = [[k, 1], [4, 1]]`. Se sabe que `v = ⟨1, 2⟩` es autovector de `A`.",
        "parts": [
            {
                "prompt": "a) ¿Cuánto vale `k`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1",
            },
            {
                "prompt": "b) ¿Cuánto vale el OTRO autovalor de `A` (el que no corresponde a `v`)? Respondé solo con el número.",
                "check": {"type": "numeric", "value": -1, "tolerance": 0, "unit": ""},
                "answer": "−1",
            },
            {
                "prompt": "c) ¿Cuál es un autovector asociado a ese otro autovalor?",
                "check": {"type": "choice", "options": ["⟨1, −2⟩", "⟨1, 2⟩", "⟨2, −1⟩", "⟨−2, 1⟩"], "correct": 0},
                "answer": "⟨1, −2⟩",
            },
        ],
        "hints": [
            "Calculá `A·v` y exigí que sea `λ·v`: la segunda componente no depende de `k` y te da `λ`.",
            "Con `k` hallado, usá traza: `λ₁ + λ₂ = k + 1`.",
            "Resolvé `(A − λ₂I)w = 0`.",
        ],
        "solution": [
            "`A⟨1, 2⟩ = ⟨k + 2, 4 + 2⟩ = ⟨k + 2, 6⟩`. Debe ser `λ⟨1, 2⟩ = ⟨λ, 2λ⟩` → `2λ = 6` → `λ = 3` y `k + 2 = 3` → `k = 1`.",
            "`A = [[1, 1], [4, 1]]`: traza `2`, determinante `1 − 4 = −3`. `λ₂ = 2 − 3 = −1` (y `3·(−1) = −3` ✓).",
            "`A + I = [[2, 1], [4, 2]]`: `2x + y = 0` → `w = ⟨1, −2⟩`.",
            "Comprobación: `A⟨1, −2⟩ = ⟨1 − 2, 4 − 2⟩ = ⟨−1, 2⟩ = −1·⟨1, −2⟩` ✓.",
            "Los demás fallan: `⟨1, 2⟩` es el autovector de `λ = 3`; `A⟨2, −1⟩ = ⟨1, 7⟩` y `A⟨−2, 1⟩ = ⟨−1, −7⟩` no son múltiplos.",
        ],
    },
    # ==================== DIAGONALIZACIÓN Y APLICACIONES ====================
    {
        "id": "la-diagonalizacion-aplicaciones-1",
        "node": "la-diagonalizacion-aplicaciones",
        "kind": "problem",
        "level": 1,
        "title": "Diagonalizar y calcular A⁴",
        "statement": "Sea `A = [[4, −2], [1, 1]]`. Diagonalizala como `A = P·D·P⁻¹` con `D = [[2, 0], [0, 3]]`.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es una matriz `P` válida para ese `D`?",
                "check": {
                    "type": "choice",
                    "options": ["[[1, 2], [1, 1]]", "[[2, 1], [1, 1]]", "[[1, 1], [1, 2]]", "[[1, 2], [−1, 1]]"],
                    "correct": 0,
                },
                "answer": "[[1, 2], [1, 1]]",
            },
            {
                "prompt": "b) ¿Cuánto vale la entrada de la fila 2, columna 1 de `A⁴`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 65, "tolerance": 0, "unit": ""},
                "answer": "65",
            },
        ],
        "hints": [
            "Las columnas de `P` son autovectores en el MISMO orden que los autovalores de `D`: primero el de `λ = 2`, después el de `λ = 3`.",
            "`A⁴ = P·D⁴·P⁻¹` con `D⁴ = [[16, 0], [0, 81]]`.",
        ],
        "solution": [
            "`λ = 2`: `A − 2I = [[2, −2], [1, −1]]` → `x = y` → `⟨1, 1⟩`. `λ = 3`: `A − 3I = [[1, −2], [1, −2]]` → `x = 2y` → `⟨2, 1⟩`.",
            "`P = [[1, 2], [1, 1]]` (columna 1 para `λ = 2`, columna 2 para `λ = 3`). `det P = −1` → `P⁻¹ = [[−1, 2], [1, −1]]`.",
            "`P·D⁴ = [[16, 162], [16, 81]]`; `A⁴ = [[16, 162], [16, 81]]·[[−1, 2], [1, −1]] = [[146, −130], [65, −49]]`.",
            "Entrada (2, 1): `−16 + 81 = 65`. Chequeo: `traza(A⁴) = 146 − 49 = 97 = 2⁴ + 3⁴` ✓.",
            "Distractores: `[[2, 1], [1, 1]]` corresponde a `D = diag(3, 2)` (orden cambiado); `[[1, 1], [1, 2]]` tiene como segunda columna `⟨1, 2⟩`, que no es autovector (`A⟨1, 2⟩ = ⟨0, 3⟩`); `⟨1, −1⟩` no es autovector.",
        ],
    },
    {
        "id": "la-diagonalizacion-aplicaciones-2",
        "node": "la-diagonalizacion-aplicaciones",
        "kind": "problem",
        "level": 2,
        "title": "Matriz de covarianza y componentes principales",
        "statement": "La matriz de covarianza de dos variables de un conjunto de datos es `Σ = [[5, 2], [2, 2]]` (simétrica). Diagonalizala ortogonalmente como `Σ = Q·D·Qᵀ`, con los autovalores de `D` ordenados de mayor a menor.",
        "parts": [
            {
                "prompt": "a) ¿Cuál es el MENOR autovalor de `Σ`? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 1, "tolerance": 0, "unit": ""},
                "answer": "1",
            },
            {
                "prompt": "b) Con `D = [[6, 0], [0, 1]]`, ¿cuál es una matriz `Q` válida?",
                "check": {
                    "type": "choice",
                    "options": [
                        "(1/√5)·[[2, 1], [1, −2]]",
                        "[[2, 1], [1, −2]]",
                        "(1/√5)·[[1, 2], [−2, 1]]",
                        "(1/√5)·[[2, 1], [1, 2]]",
                    ],
                    "correct": 0,
                },
                "answer": "(1/√5)·[[2, 1], [1, −2]]",
            },
            {
                "prompt": "c) ¿Qué fracción de la varianza total explica la primera componente principal? Redondeá a 2 decimales. Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.86, "tolerance": 0.01, "unit": ""},
                "answer": "0.86 (= 6/7)",
            },
        ],
        "hints": [
            "Traza `7` y determinante `10 − 4 = 6`: los autovalores suman 7 y multiplican 6.",
            "Por ser simétrica, los autovectores son perpendiculares; `Q` necesita columnas de longitud 1.",
            "La varianza total es la traza (suma de autovalores).",
        ],
        "solution": [
            "`λ² − 7λ + 6 = 0` → `(λ − 6)(λ − 1) = 0` → `λ = 6` y `λ = 1`.",
            "`λ = 6`: `Σ − 6I = [[−1, 2], [2, −4]]` → `x = 2y` → `⟨2, 1⟩`. `λ = 1`: `Σ − I = [[4, 2], [2, 1]]` → `y = −2x` → `⟨1, −2⟩`. Son perpendiculares: `2 − 2 = 0` ✓.",
            "Normalizando (longitud `√5`): `Q = (1/√5)[[2, 1], [1, −2]]`, con `QᵀQ = I`, y `Q·D·Qᵀ = (1/5)[[24 + 1, 12 − 2], [12 − 2, 6 + 4]] = [[5, 2], [2, 2]]` ✓.",
            "Distractores: sin normalizar, `Q` no es ortogonal (`QDQᵀ = [[25, 10], [10, 10]]`); con las columnas en otro orden corresponde a `D = diag(1, 6)`; `(1/√5)[[2, 1], [1, 2]]` no tiene columnas perpendiculares.",
            "PCA: la primera componente es la dirección `⟨2, 1⟩/√5`, con varianza `6` sobre un total `6 + 1 = 7` → `6/7 ≈ 0,86` (86 % de la varianza).",
        ],
    },
    {
        "id": "la-diagonalizacion-aplicaciones-3",
        "node": "la-diagonalizacion-aplicaciones",
        "kind": "problem",
        "level": 3,
        "title": "Bicicletas públicas entre dos estaciones (cadena de Markov)",
        "statement": "Un sistema de bicicletas públicas tiene dos estaciones, A y B, y 1000 bicicletas. Cada día, de las bicicletas que están en A, el 80 % termina el día en A y el 20 % en B; de las que están en B, el 70 % queda en B y el 30 % pasa a A. El día 0 las 1000 bicicletas están en A. Suponé que el total no cambia.",
        "parts": [
            {
                "prompt": "a) La matriz de transición tiene autovalor 1. ¿Cuánto vale su otro autovalor? Respondé solo con el número.",
                "check": {"type": "numeric", "value": 0.5, "tolerance": 0, "unit": ""},
                "answer": "0.5",
            },
            {
                "prompt": "b) ¿Cuántas bicicletas hay en A al final del día 3? Respondé solo con el número en bicicletas.",
                "check": {"type": "numeric", "value": 650, "tolerance": 0, "unit": "bicicletas"},
                "answer": "650 bicicletas",
            },
            {
                "prompt": "c) A largo plazo, ¿cuántas bicicletas hay en B? Respondé solo con el número en bicicletas.",
                "check": {"type": "numeric", "value": 400, "tolerance": 0, "unit": "bicicletas"},
                "answer": "400 bicicletas",
            },
        ],
        "hints": [
            "Con el estado `x = ⟨A, B⟩`, la matriz es `M = [[0.8, 0.3], [0.2, 0.7]]` (cada columna suma 1). Traza y determinante te dan el otro autovalor.",
            "Escribí `x₀ = ⟨1000, 0⟩` como estado estacionario más un múltiplo del autovector del otro autovalor; así `xₙ` sale sin multiplicar matrices.",
            "El estado estacionario cumple `M·x = x` y `A + B = 1000`.",
        ],
        "solution": [
            "Con `x = ⟨A, B⟩`: `M = [[0.8, 0.3], [0.2, 0.7]]` (la columna 1 dice adónde van las bicicletas de A; cada columna suma 1). Traza `1,5`, determinante `0,56 − 0,06 = 0,5`. Como `λ₁ = 1`: `λ₂ = 1,5 − 1 = 0,5` (y `1·0,5 = 0,5` ✓).",
            "Estacionario (`λ = 1`): `(M − I)x = 0` → `−0,2A + 0,3B = 0` → `A = 1,5B`. Con `A + B = 1000`: `B = 400`, `A = 600`.",
            "Autovector de `λ = 0,5`: `M − 0,5I = [[0.3, 0.3], [0.2, 0.2]]` → `⟨1, −1⟩`.",
            "`x₀ = ⟨1000, 0⟩ = ⟨600, 400⟩ + 400·⟨1, −1⟩`. Como `M` multiplica el primer término por 1 y el segundo por `0,5`: `xₙ = ⟨600, 400⟩ + 400·(0,5)ⁿ·⟨1, −1⟩`.",
            "Día 3: `A = 600 + 400/8 = 650` (y `B = 350`). Comprobación paso a paso: `⟨1000, 0⟩ → ⟨800, 200⟩ → ⟨700, 300⟩ → ⟨650, 350⟩` ✓.",
            "Como `(0,5)ⁿ → 0`, a largo plazo `xₙ → ⟨600, 400⟩`: 400 bicicletas en B, sin importar cómo se arranque. Error típico: armar la matriz por filas (transpuesta), que no conserva el total de bicicletas al multiplicar por la derecha.",
        ],
    },
]
