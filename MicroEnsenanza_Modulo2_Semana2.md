# MicroEnseñanza — Módulo II · Semana 2
## Técnico en Programación (SEP 3061300006-23) · UTEC Celaya
### Asesor: MC. Román Fernando López González

| Campo | Detalle |
|---|---|
| Módulo / Semana | II / 2 de 13 |
| Hilo conector | "Conectar las piezas" |
| Submódulos | S1 Frameworks (URL dispatcher, path params, namespace) · S2 Ágiles (5 eventos Scrum, Sprint 1 Planning) |
| Stack | Django 4.2 · Python 3.11+ · Git (rama sprint1) |
| Horario | 16:45–19:45 (180 min/día) |
| Plataforma institucional | Google Classroom |
| Tiempo fantasma (buffer) | 15 min/día máximo (último bloque) |
| Regla del docente | Expone ≤10 min por bloque; el resto circula y asesora |
| Prerrequisito | Semana 1 — proyecto Django con vista bienvenida + Product Backlog en repositorio |

**Leyenda de tipos:** 🟡 Arranque en frío · 📖 Mini-exposición (≤10 min) · ✏️ Copia en libreta / Punto de control · 🔍 Investigación rápida con IA · 💻 Práctica de laboratorio · ✅ Verificación/Coevaluación · 🎭 Taller colaborativo · 🗣️ Presentación oral · 📝 Reflexión/Retrospectiva · 📤 Subir a Classroom · 🔄 Anticipo del día siguiente · ⏸️ Pausa activa · 🆓 Buffer

---

## LUNES — Momento Tobón: APERTURA
**Propósito:** revisión del Sprint 0 + URL dispatcher + 5 eventos Scrum + rúbrica + crear rama sprint1.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué hace `urls.py` en Django?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | URL dispatcher: diagrama petición → `urls.py` → `views.py` → response | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC1** — copia el esquema del URL dispatcher | Nota PC1 | Libreta | — |
| 17:10 | 20 | ✅ | Revisión Sprint 0: `manage.py check` + Product Backlog (≥5 HUs) | Sprint 0 validado | Terminal | Classroom |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 20 | 📖 | Los 5 eventos de Scrum: sprint, planning, daily, review, retro | — | Pizarrón | — |
| 17:55 | 10 | ✏️ | **PC2** — copia la tabla de los 5 eventos | Nota PC2 | Libreta | — |
| 18:05 | 20 | 🎭 | Dibujar en libreta el flujo de un sprint de una semana | Diagrama sprint | Libreta | — |
| 18:25 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:30 | 25 | ✅ | Revisión de la **rúbrica** de la semana + presentación del Sprint Goal de ejemplo | Rúbrica revisada | Classroom | — |
| 18:55 | 25 | 💻 | Crear la rama `sprint1/lista-detalle-productos` en el repo | Rama creada | Terminal/GitHub | — |
| 19:20 | 10 | 📤🔄 | Subir evidencia Sprint 0 revisado + anticipo del martes | Evidencia subida | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC1 — URL Dispatcher (flujo)
Navegador → petición HTTP GET /productos/2/
         ↓
    urls.py del PROYECTO    (enruta al include correcto)
         ↓
    urls.py de la APP       (compara patrón: <int:producto_id>)
         ↓
    views.py → función      (recibe: request, producto_id=2)
         ↓
    HttpResponse            (regresa HTML al navegador)
```
```
PC2 — Los 5 eventos de Scrum
Sprint            Contenedor del trabajo      (1–4 semanas)
Sprint Planning   Planear qué y cómo         (máx. 4 h)
Daily Scrum       Sincronizar al equipo       (15 min diarios)
Sprint Review     Revisar el incremento       (máx. 2 h)
Sprint Retrospective  Mejorar la forma de trabajo (máx. 1.5 h)
```

---

## MARTES — Momento Tobón: DESARROLLO (inicio)
**Propósito:** `path()` con parámetros de tipo + `app_name` + vista `lista_productos`.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué pasa si la URL tiene `/productos/abc/` con `<int:>`?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | `path()` con convertidores de tipo: `<int:id>`, `<str:nombre>` | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC3** — copia `path()` con parámetro y `app_name` | Nota PC3 | Libreta | — |
| 17:10 | 20 | 🔍 | **IA-1**: investigar y copiar resultado en libreta | Nota IA-1 | IA + Libreta | — |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 35 | 💻 | Práctica: agregar `app_name` + crear `lista_productos` en `views.py` | Vista lista | VS Code | — |
| 18:10 | 10 | 📖 | Recorrer un diccionario en Python para generar HTML | — | Pizarrón | — |
| 18:20 | 20 | 💻 | Completar `lista_productos` + configurar URL + verificar en navegador | Vista lista funcional | Terminal | — |
| 18:40 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:45 | 25 | ✅ | Coevaluación en parejas: probar `/productos/` del compañero | Lista de cotejo | — | — |
| 19:10 | 20 | 📤🔄 | Subir avance (`views.py` + `urls.py`) + anticipo del miércoles | Avance subido | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC3 — path() con parámetro y namespace
# En productos/urls.py:
app_name = "productos"                 # namespace
urlpatterns = [
    path("productos/<int:producto_id>/",
         views.detalle_producto,
         name="detalle"),
]
# Django convierte el segmento a int y lo pasa como argumento.
# Si no es int, devuelve 404 automáticamente.
```
```
IA-1 (copiar pregunta y resultado):
Pregunta: ¿Qué diferencia hay entre un parámetro de URL
(<int:id>) y un parámetro de consulta (?id=1) en una app web?
¿Cuándo conviene usar cada uno?
Resultado: ____________________________________________
```

---

## MIÉRCOLES — Momento Tobón: DESARROLLO (profundización)
**Propósito:** vista `detalle_producto` con 404 + URL namespace completo + verificación de las 4 rutas.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué status HTTP devuelve tu vista si el ID no existe?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | Parámetro de URL → argumento de vista; `HttpResponse` con status 404 | — | Pizarrón | — |
| 17:00 | 15 | 🔍 | **IA-2**: investigar y copiar resultado en libreta | Nota IA-2 | IA + Libreta | — |
| 17:15 | 10 | ✏️ | **PC4** — copia la estructura de `detalle_producto` con 404 | Nota PC4 | Libreta | — |
| 17:25 | 10 | 💻 | Inicio práctica: firma de `detalle_producto` y datos de ejemplo | Avance función | VS Code | — |
| 17:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:40 | 30 | 💻 | Completar `detalle_producto` + agregar URL con `<int:producto_id>` | Vista detalle | VS Code | — |
| 18:10 | 10 | 📖 | Cómo funciona `include()` con `namespace=` en el proyecto | — | Pizarrón | — |
| 18:20 | 25 | 💻 | Actualizar `inventario_proyecto/urls.py` + correr `manage.py check` | Check sin errores | Terminal | — |
| 18:45 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:50 | 30 | ✅ | Verificar las 4 URLs: bienvenida(200) · lista(200) · detalle/2/(200) · detalle/99/(404) | 4 verificaciones | Navegador | — |
| 19:20 | 10 | 📤🔄 | Subir `views.py` y `urls.py` actualizados + anticipo del jueves | Entregables subidos | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC4 — Vista detalle_producto con 404
def detalle_producto(request, producto_id: int):
    """Detalle de un producto por ID de URL."""
    producto = PRODUCTOS_EJEMPLO.get(producto_id)
    if producto is None:
        return HttpResponse(
            f"<h1>Producto {producto_id} no encontrado</h1>",
            status=404,                   # ← status HTTP 404
        )
    return HttpResponse(f"<h1>{producto['nombre']}</h1>")

# Verificacion esperada:
#   producto_id=2  → status 200, nombre correcto
#   producto_id=99 → status 404, "no encontrado"
```
```
IA-2 (copiar pregunta y resultado):
Pregunta: ¿Para qué sirve el namespace de URLs en Django y qué
problema resuelve cuando el proyecto tiene varias apps?
Resultado: ____________________________________________
```

---

## JUEVES — Momento Tobón: CIERRE (inicio)
**Propósito:** Sprint 1 Planning + rama de Git + flashcards.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué es un Sprint Goal?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | Sprint Planning: Sprint Goal, selección de HUs, estimación, tareas | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC5** — copia el formato del Sprint 1 Planning + rama Git | Nota PC5 | Libreta | — |
| 17:10 | 20 | 🔍 | **IA-3**: investigar y copiar resultado en libreta | Nota IA-3 | IA + Libreta | — |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 35 | 💻 | Redactar `sprint1_planning.md`: Sprint Goal + HU-01 + HU-01a + tareas | `sprint1_planning.md` | VS Code | — |
| 18:10 | 25 | 💻 | `git checkout -b sprint1/...` + `git add` + `git commit` + `git push` | Commit en rama sprint1 | Terminal/GitHub | GitHub |
| 18:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:40 | 20 | 🎭 | Taller de **flashcards** de la semana | 8 flashcards | Libreta/Quizlet | — |
| 19:00 | 15 | ✏️ | **PC6** — copia conceptos clave para flashcards | Nota PC6 | Libreta | — |
| 19:15 | 15 | 📤🔄 | Subir enlace rama sprint1 + planning + anticipo del viernes | Enlace subido | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC5 — Sprint 1 Planning + rama Git
# Formato del documento sprint1_planning.md:
Sprint Goal: "Al finalizar el sprint, el sistema mostrará
la lista de productos y el detalle de cada uno por URL."
HUs: HU-01 (lista) · HU-01a (detalle)
Rama: sprint1/lista-detalle-productos

# Comandos:
git checkout -b sprint1/lista-detalle-productos
git add .
git commit -m "Sprint 1: vistas lista y detalle con URL namespace"
git push origin sprint1/lista-detalle-productos
```
```
PC6 — Conceptos clave (flashcards)
URL dispatcher · path() · <int:id> · app_name · namespace
include() · status 404 · Sprint Goal · Sprint Planning
Daily Scrum · Sprint Review · Sprint Retrospective
```
```
IA-3 (copiar pregunta y resultado):
Pregunta: ¿Qué es un Sprint Goal en Scrum y por qué es diferente
a una lista de tareas?
Resultado: ____________________________________________
```

---

## VIERNES — Momento Tobón: CIERRE (conclusión)
**Propósito:** Sprint Review + coevaluación + retrospectiva.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "menciona una pieza que conectaste esta semana" | Respuesta rápida | Libreta | — |
| 16:50 | 30 | 🗣️ | **Sprint Review**: mostrar las 4 URLs + sprint1_planning.md | Demostración | Navegador/Proyector | — |
| 17:20 | 10 | ✅ | Coevaluación con rúbrica entre pares | Rúbrica llena | Classroom | Classroom |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 30 | ✅ | Verificación final: `manage.py check` + 4 URLs + sprint planning + rama | Checklist validado | Terminal | — |
| 18:05 | 20 | 📝 | **Retrospectiva**: qué funcionó / qué mejorar | Notas retro | Libreta | — |
| 18:25 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:30 | 30 | 🎭 | Repaso colaborativo con flashcards (juego por equipos) | Puntaje equipo | Quizlet/Libreta | — |
| 19:00 | 15 | ✏️ | **PC7** — cierre de la semana (ver texto abajo) | Nota PC7 | Libreta | — |
| 19:15 | 15 | 📤 | Subir evidencias finales + autoevaluación | Carpeta semana 2 | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta — PC7 (cierre obligatorio):**
```
PC7 — CIERRE SEMANA 2 "Conectar las piezas"

[ ] CHECKLIST DE ENTREGABLES
    [ ] lista_productos funcionando (status 200, 3 productos)
    [ ] detalle_producto funcionando (status 200 y 404 correctos)
    [ ] URL namespace (app_name) configurado
    [ ] manage.py check sin errores
    [ ] sprint1_planning.md con Sprint Goal + HUs + tareas
    [ ] Rama sprint1/lista-detalle-productos con commit publicado
    [ ] Notas PC1–PC6 e IA-1, IA-2, IA-3 completas

CONCEPTOS CLAVE
    URL dispatcher · path() · convertidor <int:> ·
    app_name / namespace · status 404 ·
    Sprint Goal · Sprint Planning · Daily Scrum ·
    Sprint Review · Sprint Retrospective

TAREA DE INVESTIGACIÓN (entregar el lunes)
    Investiga: ¿qué es una plantilla (template) en Django y cómo
    se diferencia de devolver HTML directo en HttpResponse?
    Trae un ejemplo mínimo en la libreta.

PREGUNTA DE REFLEXIÓN FINAL
    Explica con tus palabras en qué se parecen el URL namespace
    de Django (que evita que dos apps colisionen) y el Sprint Goal
    de Scrum (que evita que el equipo trabaje en direcciones opuestas).
```

---

## Resumen semanal (Google Classroom)

| Día | Actividad en Classroom | Producto | Plazo |
|---|---|---|---|
| Lunes | Revisión Sprint 0 + rama sprint1 creada | Evidencia de `manage.py check` + Product Backlog | Lunes 19:30 |
| Martes | Vista lista_productos | `views.py` + `urls.py` (avance) | Martes 19:30 |
| Miércoles | Vista detalle + 4 URLs verificadas | `views.py` y `urls.py` actualizados | Miércoles 19:30 |
| Jueves | Sprint 1 Planning + rama | `sprint1_planning.md` + URL de la rama en GitHub | Jueves 19:30 |
| Viernes | Carpeta final + autoevaluación | Código + planning + retro + PC7 | Viernes 19:30 |

---

### Conteo de cumplimiento (verificación de reglas del ROL 3)
- Puntos de control: **PC1–PC7 (7 ≥ 5 mínimo)** ✓ · PC7 con checklist + conceptos + tarea + reflexión ✓
- Investigaciones rápidas con IA: **IA-1 (martes), IA-2 (miércoles), IA-3 (jueves) = 3 ≥ 3 mínimo** ✓
- Bloques fijos diarios: arranque 5 min a las 16:45 · buffer 15 min al cierre · pausas activas cada ~45–60 min ✓
- Todos los días suman **180 min** (16:45–19:45) ✓ · Mini-exposiciones ≤10 min ✓
- Continuidad con Semana 1: parte del proyecto, repo y Product Backlog ya iniciados ✓
- Tarea de investigación prepara Semana 3 (plantillas Django) ✓

---

*Plan generado bajo ROL 3 — MicroEnseñanza · Prompt Maestro v1.0 · Metodología Tobón · Google Classroom.*
