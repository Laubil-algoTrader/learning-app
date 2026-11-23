# AprendeLab

App local para aprender desde cero **guitarra**, **electrónica (Arduino / ESP32)**, **matemáticas**, **física**, **comprensión lectora y resolución de problemas** y cualquier materia que quieras sumar. Lecciones cortas, laboratorios para practicar y repasos espaciados que aparecen justo antes de que te olvides.

Corre en tu computadora con Python 3 estándar y SQLite: no hay nada que instalar ni cuentas que crear. Lo único que viene de internet son las tipografías (Google Fonts); sin conexión la app funciona igual con las fuentes del sistema.

## Arranque

```bash
python3 app.py
```

Abrí `http://localhost:8000`. Por defecto la app **solo es accesible desde esta computadora**.

### Usarla en el celular

```bash
python3 app.py --lan
```

La consola muestra la dirección de tu Wi-Fi (por ejemplo `http://192.168.1.20:8000`) y un **PIN de 6 dígitos**. Cada dispositivo lo ingresa una sola vez. El PIN se guarda en la base y no cambia entre reinicios (podés fijar uno con `--pin 123456`).

### Micrófono e instalación como app en el celular (HTTPS)

Los navegadores solo permiten el micrófono (afinador) y la instalación como app en `localhost` o por HTTPS.

```bash
python3 app.py --lan --https
```

Esto genera un certificado autofirmado (necesita `openssl`) y sirve por `https://`. El celular va a mostrar una advertencia la primera vez; al aceptarla, el micrófono funciona.

Para que además se pueda **instalar como app y funcione el caché offline**, el certificado tiene que ser de confianza para el celular. La forma más simple es [mkcert](https://github.com/FiloSottile/mkcert): generás un certificado para la IP de tu PC, instalás su autoridad raíz en el celular y arrancás con:

```bash
python3 app.py --lan --cert ruta/cert.pem --key ruta/key.pem
```

### Otras opciones

`--port 8080` · `--db data/otra.db` · `--host 0.0.0.0`

## Cómo se usa

1. **Hoy** te dice qué hacer ahora: repasar lo que toca o aprender la próxima lección.
2. **Ingreso**: el programa del Curso de Ingreso 2027 de Ingeniería de la UNCuyo (Matemática, Física y Comprensión Lectora y Resolución de Problemas), unidad por unidad, con lo que te falta de cada tema (lección, repaso y ejercicios) y un simulacro solo con temas del programa. El resto de la ruta de cada materia es base previa o material para después del ingreso. El mapa del programa está en `backend/ingreso_uncuyo.py`.
3. **Aprender**: cada materia es una ruta de lecciones de cinco pasos (la idea, cómo funciona, un ejemplo, tres preguntas de comprobación y un cierre con tus palabras). Para terminar la lección hay que responder bien las preguntas; las que te costaron se convierten en tarjetas.
4. **Repaso**: solo aparecen tarjetas de lecciones que ya completaste, con un tope de tarjetas nuevas por día (8 por defecto, se cambia en Ajustes). Antes de ver cada respuesta decís qué tan seguro estás. Muchas tarjetas se corrigen solas (número, texto corto, opción múltiple u ordenar pasos). Lo que fallás vuelve en la misma sesión.
5. **Ejercicios**: problemas de varios pasos para resolver en papel (matemática y física) y mini proyectos o rutinas (electrónica y guitarra), ordenados por tema y por dificultad. Los que vienen de las guías oficiales del ingreso llevan la fuente (por ejemplo «Física · Práctica U3, ej. 16»); cuando el solucionario oficial tiene un error, la resolución lo aclara. Cada problema se corrige solo, tiene pistas y una resolución paso a paso. El **simulacro** mezcla temas y corrige una sola vez, como un parcial. A diferencia del repaso, no se agendan: los elegís vos y queda registrado cuáles resolviste.
6. **Laboratorios**: metrónomo, afinador con micrófono, acordes y diapasón; ley de Ohm, pines del ESP32 y depuración; ejemplos guiados y graficador; simuladores de física.
7. **Sesión guiada**: arma el orden por vos (repasos, lo que más te cuesta, mezcla de temas y cierre). Si recargás la página, la sesión continúa donde estaba.

### Cómo se mide el progreso

- Una lección **desbloquea la siguiente** cuando la completaste y practicaste al menos el 60 % de sus tarjetas una vez.
- Un tema está **dominado** cuando sus tarjetas tienen al menos 3 repasos y el modelo estima que las recordás por 3 semanas o más. Un solo acierto no alcanza.
- El calendario de repasos usa el algoritmo FSRS-5 (`backend/fsrs.py`).

### Agregar ejercicios

Los ejercicios viven en `backend/exercises/`: cada archivo define una lista `EXERCISES` y se publica solo, sin tocar nada más. Un ejercicio se asocia a un tema por su `slug` (campo `node`). Hay dos tipos: `problem` (enunciado, incisos autocorregidos, pistas y resolución) y `project` (materiales, pasos y criterios de "está hecho cuando"). Los archivos cuyo nombre empieza con `_` (por ejemplo `_draft_algo.py`) se ignoran: sirven para dejar un paquete en borrador hasta revisarlo.

Para revisar un paquete antes de publicarlo:

```bash
python3 tools/exercise_tools.py validate backend.exercises._draft_algo
python3 tools/exercise_tools.py dump backend.exercises._draft_algo > paquete.txt
```

`tools/topic_tools.py` hace lo mismo con paquetes de temas (lecciones y tarjetas) que se intercalan en una ruta con `insert_after`.

## Editor de materias

Desde el menú «⋯» → *Editor de materias* podés crear materias, lecciones y tarjetas (con corrección automática opcional), y exportar o importar un respaldo en JSON.

## Datos

Todo vive en `data/aprendelab.db`. Al actualizar la app, las tarjetas nuevas del contenido incluido se agregan una sola vez sin tocar tu progreso.

## Pruebas

```bash
python3 -m unittest discover -s tests -v
```
