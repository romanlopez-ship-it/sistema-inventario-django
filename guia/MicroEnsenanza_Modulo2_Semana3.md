# MicroEnseñanza — Módulo II · Semana 3
## Técnico en Programación (SEP 3061300006-23) · UTEC Celaya
### Asesor: MC. Román Fernando López González

| Campo | Detalle |
|---|---|
| Módulo / Semana | II / 3 de 13 |
| Hilo conector | "Historias → vistas" |
| Submódulos | S1 Frameworks (DTL, herencia, `render()`) · S2 Ágiles (Gherkin, Sprint 1 Review, Sprint 2 Planning) |
| Stack | Django 4.2 · Django Template Language · Python 3.11+ · Git (merge `sprint1` → `main`) |
| Horario | 16:45–19:45 (180 min/día) |
| Plataforma institucional | Google Classroom |
| Tiempo fantasma (buffer) | 15 min/día máximo (último bloque) |
| Regla del docente | Expone ≤10 min por bloque; el resto circula y asesora |
| Prerrequisito | Semana 2 — vistas lista y detalle + `sprint1_planning.md` en rama `sprint1/lista-detalle-productos` |

**Leyenda de tipos:** 🟡 Arranque en frío · 📖 Mini-exposición (≤10 min) · ✏️ Copia en libreta / Punto de control · 🔍 Investigación rápida con IA · 💻 Práctica de laboratorio · ✅ Verificación/Coevaluación · 🎭 Taller colaborativo · 🗣️ Presentación oral · 📝 Reflexión/Retrospectiva · 📤 Subir a Classroom · 🔄 Anticipo del día siguiente · ⏸️ Pausa activa · 🆓 Buffer

---

## LUNES — Momento Tobón: APERTURA
**Propósito:** problema DRY + sintaxis DTL básica + configurar `settings.py` + estructura de directorios + rúbrica.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué harías si el cliente pide cambiar el título en todas las páginas?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | El problema DRY: HTML dentro de Python vs. plantillas separadas; ventaja de `render()` | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC1** — copia la sintaxis DTL: variables, etiquetas y filtros | Nota PC1 | Libreta | — |
| 17:10 | 25 | 💻 | Configurar `settings.py`: añadir `BASE_DIR / 'templates'` a `DIRS`; verificar `APP_DIRS: True` | `settings.py` actualizado | VS Code | — |
| 17:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:40 | 10 | 📖 | Estructura de directorios de plantillas: proyecto vs. *app* (dibujar en pizarrón) | — | Pizarrón | — |
| 17:50 | 10 | ✏️ | **PC2** — copia la configuración de `TEMPLATES` en `settings.py` | Nota PC2 | Libreta | — |
| 18:00 | 25 | 🎭 | Dibujar en libreta el árbol de herencia: `base.html` → `lista.html` / `detalle.html` | Diagrama de herencia | Libreta | — |
| 18:25 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:30 | 25 | ✅ | Revisión de la **rúbrica** de la semana + `manage.py check` del proyecto de la Semana 2 | Check sin errores | Terminal | Classroom |
| 18:55 | 25 | 💻 | Crear estructura de directorios vacíos con `mkdir` | Carpetas `templates/` creadas | Terminal | — |
| 19:20 | 10 | 📤🔄 | Subir `settings.py` actualizado + captura de estructura de carpetas + anticipo del martes | Evidencia subida | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC1 — Sintaxis DTL (Django Template Language)
{{ variable }}               imprime el valor de la variable
{{ precio|floatformat:2 }}   filtro: muestra 2 decimales
{% etiqueta %}               control: for, if, block, extends
{% for x in lista %}
    <li>{{ x }}</li>
{% empty %}
    <li>Sin elementos</li>   caso lista vacia
{% endfor %}
{# comentario #}             no se muestra en el HTML final
```
```
PC2 — Configurar TEMPLATES en settings.py
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],   # plantillas del proyecto
        'APP_DIRS': True,    # busca tambien en <app>/templates/<app>/
        ...
    },
]
# Estructura de directorios:
# templates/
#   base.html                 <- proyecto
# productos/templates/productos/
#   lista.html                <- app
#   detalle.html              <- app
```

---

## MARTES — Momento Tobón: DESARROLLO (inicio)
**Propósito:** crear `base.html` + `lista.html` con herencia, `{% for %}`/`{% empty %}`.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué hace `{% block content %}` en una plantilla?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | Herencia de plantillas: `{% extends %}`, `{% block %}`, `{% endblock %}`; regla: `{% extends %}` en línea 1 | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC3** — copia estructura de `base.html` con dos bloques | Nota PC3 | Libreta | — |
| 17:10 | 20 | 🔍 | **IA-1**: investigar y copiar resultado en libreta | Nota IA-1 | IA + Libreta | — |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 35 | 💻 | Crear `templates/base.html` completo: DOCTYPE, `<header>`, `<nav>`, `<main>`, `<footer>` con bloques | `base.html` | VS Code | — |
| 18:10 | 25 | 💻 | Crear `productos/templates/productos/lista.html` con `{% extends %}` + `{% for %}`/`{% empty %}` | `lista.html` | VS Code | — |
| 18:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:40 | 20 | ✅ | Verificar herencia: `runserver` → `/productos/` → comprobar `<header>` y `<footer>` presentes | Herencia verificada | Navegador | — |
| 19:00 | 15 | 📤🔄 | Subir `base.html` + `lista.html` + anticipo del miércoles | Avance subido | Classroom | Classroom |
| 19:15 | 15 | 🎭 | Revisión en parejas: ¿el `base.html` del compañero tiene los dos bloques `title` y `content`? | Lista de cotejo | — | — |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC3 — Estructura de base.html con bloques
<!DOCTYPE html>
<html lang="es">
<head>
    <title>{% block title %}Inventario{% endblock %}</title>
</head>
<body>
    <header><h1>Sistema de Inventario</h1></header>
    <main>
        {% block content %}{% endblock %}  <- hijas rellenan aqui
    </main>
    <footer><p>Modulo II</p></footer>
</body>
</html>

En lista.html ({% extends %} DEBE ser linea 1):
{% extends "base.html" %}
{% block title %}Lista de productos{% endblock %}
{% block content %}
    ...contenido especifico...
{% endblock %}
```
```
IA-1 (copiar pregunta y resultado):
Pregunta: ¿Qué significa el principio DRY (Don't Repeat Yourself)
en programación? Da un ejemplo de cómo base.html aplica este principio.
Resultado: ____________________________________________
```

---

## MIÉRCOLES — Momento Tobón: DESARROLLO (profundización)
**Propósito:** `detalle.html` + actualizar `views.py` con `render()` + verificar 5 aserciones.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué devuelve `render()` en Django?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | `render()` vs `HttpResponse`; el diccionario de contexto como "puente" entre vista y plantilla | — | Pizarrón | — |
| 17:00 | 15 | 🔍 | **IA-2**: investigar y copiar resultado en libreta | Nota IA-2 | IA + Libreta | — |
| 17:15 | 10 | ✏️ | **PC4** — copia `render()` con contexto y `{% extends %}` en vista hija | Nota PC4 | Libreta | — |
| 17:25 | 10 | 💻 | Inicio de `detalle.html`: declarar `{% extends %}` y completar bloque `title` con `{{ producto.nombre }}` | Avance detalle | VS Code | — |
| 17:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:40 | 30 | 💻 | Completar `detalle.html` (nombre, precio, enlace volver) + actualizar `detalle_producto` con `render()` | Vista detalle con plantilla | VS Code | — |
| 18:10 | 25 | 💻 | Actualizar `bienvenida` y `lista_productos` con `render()` + `manage.py check` | Todas las vistas con `render()` | Terminal | — |
| 18:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:40 | 20 | ✅ | Verificar las 5 aserciones: bienvenida(200) · lista(200, 3 prod.) · detalle/1/(200, $350) · detalle/99/(404) · herencia | 5 verificaciones OK | Navegador | — |
| 19:00 | 15 | 🎭 | Coevaluación: probar `render()` + herencia del compañero | Lista de cotejo | — | — |
| 19:15 | 15 | 📤🔄 | Subir `views.py` actualizado + `detalle.html` + anticipo del jueves | Entregables subidos | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC4 — render() con contexto y plantilla hija
# views.py
from django.shortcuts import render

def lista_productos(request):
    context = {"productos": PRODUCTOS_EJEMPLO}   # dict de datos
    return render(request, "productos/lista.html", context)
    #  render() = busca plantilla + inyecta context + devuelve HttpResponse

# HttpResponse → HTML directo en Python (sem 1-2, sin plantilla)
# render()     → delega la presentacion a la plantilla (sem 3+)

# En detalle.html la variable llega como:
{{ producto.nombre }}      <- viene del context["producto"]["nombre"]
{{ producto.precio }}      <- viene del context["producto"]["precio"]
```
```
IA-2 (copiar pregunta y resultado):
Pregunta: ¿Qué diferencia hay entre render() y HttpResponse() en
Django? ¿Cuándo conviene usar cada uno?
Resultado: ____________________________________________
```

---

## JUEVES — Momento Tobón: CIERRE (inicio)
**Propósito:** criterios de aceptación Gherkin + Sprint 1 Review + merge a `main` + flashcards.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué es un criterio de aceptación?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | Formato Gherkin: *Dado / Cuando / Entonces*; propósito en el Sprint Review | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC5** — copia el formato Gherkin con los 3 criterios del Sprint 1 | Nota PC5 | Libreta | — |
| 17:10 | 20 | 🔍 | **IA-3**: investigar y copiar resultado en libreta | Nota IA-3 | IA + Libreta | — |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 30 | 💻 | Redactar `sprint1_review.md`: Sprint Goal verificado + criterios Gherkin + Sprint 2 HU-02 | `sprint1_review.md` | VS Code | — |
| 18:05 | 25 | 💻 | `git add` plantillas + review → `commit` → `merge sprint1 → main` → `push` | Sprint 1 cerrado en `main` | Terminal/GitHub | GitHub |
| 18:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:35 | 25 | 🎭 | Taller de **flashcards** de la semana | 8 flashcards | Libreta/Quizlet | — |
| 19:00 | 15 | ✏️ | **PC6** — copia conceptos clave para flashcards | Nota PC6 | Libreta | — |
| 19:15 | 15 | 📤🔄 | Subir `sprint1_review.md` + enlace a `main` con merge + anticipo del viernes | Enlace subido | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC5 — Formato Gherkin (criterios de aceptación)
HU-01: Ver lista de productos
  Dado que hay 3 productos registrados
  Cuando el usuario accede a /productos/
  Entonces ve una lista con nombre y enlace de cada producto

HU-01a: Ver detalle de producto
  Dado que existe el producto con ID 1
  Cuando accede a /productos/1/
  Entonces ve "Teclado USB" con precio $350.0

  Dado que NO existe el producto con ID 99
  Cuando accede a /productos/99/
  Entonces recibe status HTTP 404
```
```
PC6 — Conceptos clave (flashcards)
DTL (Django Template Language) · {{ variable }} · {% etiqueta %}
filtro (|floatformat:2) · {% extends %} · {% block %}/{% endblock %}
{% for %}/{% empty %}/{% endfor %} · render() · contexto (dict)
DRY · criterio de aceptacion · Gherkin: Dado/Cuando/Entonces
Sprint Review · merge branch
```
```
IA-3 (copiar pregunta y resultado):
Pregunta: ¿Qué son los criterios de aceptación en metodologías ágiles
y por qué se escriben ANTES de implementar la funcionalidad?
Resultado: ____________________________________________
```

---

## VIERNES — Momento Tobón: CIERRE (conclusión)
**Propósito:** Sprint Review + coevaluación + retrospectiva.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "menciona una conexión entre plantillas Django y metodologías ágiles" | Respuesta rápida | Libreta | — |
| 16:50 | 30 | 🗣️ | **Sprint Review**: mostrar plantillas en navegador (5 URLs) + `sprint1_review.md` + `git log --graph` | Demostración | Navegador/Proyector | — |
| 17:20 | 10 | ✅ | Coevaluación con rúbrica entre pares | Rúbrica llena | Classroom | Classroom |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 30 | ✅ | Verificación final: 5 aserciones + herencia + merge a `main` + criterios Gherkin en review | Checklist validado | Terminal/GitHub | — |
| 18:05 | 20 | 📝 | **Retrospectiva**: qué funcionó / qué mejorar | Notas retro | Libreta | — |
| 18:25 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:30 | 30 | 🎭 | Repaso colaborativo con flashcards (juego por equipos) | Puntaje equipo | Quizlet/Libreta | — |
| 19:00 | 15 | ✏️ | **PC7** — cierre de la semana (ver texto abajo) | Nota PC7 | Libreta | — |
| 19:15 | 15 | 📤 | Subir evidencias finales + autoevaluación | Carpeta semana 3 | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta — PC7 (cierre obligatorio):**
```
PC7 — CIERRE SEMANA 3 "Historias → vistas"

[ ] CHECKLIST DE ENTREGABLES
    [ ] templates/base.html con bloques title y content
    [ ] productos/templates/productos/lista.html con {% extends %}
    [ ] productos/templates/productos/detalle.html con {% extends %}
    [ ] views.py: las 3 vistas usan render()
    [ ] 5 aserciones verificadas (200/200/200/404/herencia)
    [ ] sprint1_review.md con criterios Gherkin completos
    [ ] Merge sprint1 → main publicado en GitHub
    [ ] Notas PC1–PC6 e IA-1, IA-2, IA-3 completas

CONCEPTOS CLAVE
    DTL · {{ }} / {% %} / filtros · {% extends %} ·
    {% block %}/{% endblock %} · {% for %}/{% empty %} ·
    render() · diccionario de contexto · DRY ·
    Gherkin (Dado/Cuando/Entonces) · Sprint Review ·
    criterios de aceptacion · merge de rama

TAREA DE INVESTIGACIÓN (entregar el lunes)
    Investiga: ¿qué son los modelos (models.py) en Django y cómo
    se relacionan con una base de datos?
    Trae escrito el modelo mínimo para un producto con campos
    nombre (texto) y precio (decimal).

PREGUNTA DE REFLEXIÓN FINAL
    El bloque {% block content %} en base.html define un espacio
    vacío que cada plantilla hija rellena. Un Sprint Goal define
    un resultado vacío que el equipo rellena cada sprint.
    ¿En qué se parecen estos dos conceptos?
```

---

## Resumen semanal (Google Classroom)

| Día | Actividad en Classroom | Producto | Plazo |
|---|---|---|---|
| Lunes | Configuración de plantillas | `settings.py` + captura de estructura de carpetas | Lunes 19:30 |
| Martes | Plantillas base y lista | `base.html` + `lista.html` con herencia verificada | Martes 19:30 |
| Miércoles | Plantilla detalle + `render()` | `detalle.html` + `views.py` con 5 aserciones OK | Miércoles 19:30 |
| Jueves | Sprint 1 Review + merge | `sprint1_review.md` + URL de `main` con merge | Jueves 19:30 |
| Viernes | Carpeta final + autoevaluación | Código + review + retro + PC7 | Viernes 19:30 |

---

### Conteo de cumplimiento (verificación de reglas del ROL 3)
- Puntos de control: **PC1–PC7 (7 ≥ 5 mínimo)** ✓ · PC7 con checklist (8 ítems) + conceptos + tarea + reflexión ✓
- Investigaciones rápidas con IA: **IA-1 (martes), IA-2 (miércoles), IA-3 (jueves) = 3 ≥ 3 mínimo** ✓
- Bloques fijos diarios: arranque 5 min a las 16:45 · buffer 15 min al cierre · pausas activas cada ~45–60 min ✓
- Todos los días suman **180 min** verificados aritméticamente (16:45–19:45) ✓
- Mini-exposiciones ≤10 min ✓
- Continuidad con Semana 2: parte del proyecto y rama `sprint1` ya iniciados ✓
- Tarea de investigación prepara Semana 4 (modelos Django + ORM) ✓
- Sprint 1 cerrado formalmente con merge a `main` ✓

---

*Plan generado bajo ROL 3 — MicroEnseñanza · Prompt Maestro v1.0 · Metodología Tobón · Google Classroom.*
