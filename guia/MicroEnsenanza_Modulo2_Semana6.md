# MicroEnseñanza — Módulo II · Semana 6
## Técnico en Programación (SEP 3061300006-23) · UTEC Celaya
### Asesor: MC. Román Fernando López González

| Campo | Detalle |
|---|---|
| Módulo / Semana | II / 6 de 13 |
| Hilo conector | "Ciclo cerrado" |
| Submódulos | S1 Frameworks (`get_object_or_404`, `instance=`, `editar_producto`, `eliminar_producto`) · S2 Ágiles (Sprint 2 Review, Retrospectiva, velocidad, Sprint 3 preview) |
| Stack | Django 4.2 · `get_object_or_404` · `instance=` · Python 3.11+ |
| Horario | 16:45–19:45 (180 min/día) |
| Plataforma institucional | Google Classroom |
| Tiempo fantasma (buffer) | 15 min/día máximo (último bloque) |
| Regla del docente | Expone ≤10 min por bloque; el resto circula y asesora |
| Prerrequisito | Semana 5 — `crear_producto` con `ModelForm` + Daily Scrum log en rama `sprint2/modelos-orm` |

**Leyenda de tipos:** 🟡 Arranque en frío · 📖 Mini-exposición (≤10 min) · ✏️ Copia en libreta / Punto de control · 🔍 Investigación rápida con IA · 💻 Práctica de laboratorio · ✅ Verificación/Coevaluación · 🎭 Taller colaborativo · 🗣️ Presentación oral · 📝 Reflexión/Retrospectiva · 📤 Subir a Classroom · 🔄 Anticipo del día siguiente · ⏸️ Pausa activa · 🆓 Buffer

---

## LUNES — Momento Tobón: APERTURA
**Propósito:** detonador "nombre mal escrito" + `get_object_or_404` + `instance=` concepto + Sprint 2 Review intro + rúbrica + URLs actualizadas.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "un producto dice 'Teclado usb' en vez de 'Teclado USB' — ¿cómo lo corriges sin abrir `/admin/`?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | `get_object_or_404` vs `try/except DoesNotExist`; `instance=` para pre-poblar un form con datos actuales | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC1** — copia `get_object_or_404` e `instance=` con sus diferencias clave | Nota PC1 | Libreta | — |
| 17:10 | 25 | 🎭 | Dibujar en libreta los 2 diagramas: flujo de editar (GET pre-poblado→POST→redirect) y flujo de eliminar (GET confirmación→POST→redirect) | Diagramas flujo | Libreta | — |
| 17:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:40 | 10 | 📖 | Sprint 2 Review: qué se demuestra, quién acepta el incremento, cómo verificar el Sprint Goal | — | Pizarrón | — |
| 17:50 | 10 | ✏️ | **PC2** — copia el formato del Sprint 2 Review y la fórmula de velocidad | Nota PC2 | Libreta | — |
| 18:00 | 25 | 🎭 | Sprint 2 Review simulado en parejas: uno hace de Product Owner (PO), el otro demuestra el CRUD | Review simulado | — | — |
| 18:25 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:30 | 25 | ✅ | Revisión de la **rúbrica** + `manage.py check` del proyecto de la Semana 5 | Check sin errores | Terminal | Classroom |
| 18:55 | 25 | 💻 | Actualizar `urls.py` con las rutas `editar/` y `eliminar/` + `manage.py check` | `urls.py` con CRUD completo | VS Code/Terminal | — |
| 19:20 | 10 | 📤🔄 | Subir diagramas de flujo + `urls.py` actualizado + anticipo del martes | Evidencia subida | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC1 — get_object_or_404 vs try/except + instance=
# Antes (semanas 4-5): 3 líneas
try:
    producto = Producto.objects.get(pk=producto_id)
except Producto.DoesNotExist:
    return HttpResponse("No encontrado", status=404)

# Ahora (semana 6): 1 línea
producto = get_object_or_404(Producto, pk=producto_id)
# → Si no existe: lanza Http404 → Django devuelve 404

# instance= en ModelForm:
form = ProductoForm(instance=producto)          # GET: pre-poblar
form = ProductoForm(request.POST, instance=producto)  # POST: actualizar
# Sin instance= → crea un Producto NUEVO cada POST
# Con instance= → actualiza el Producto EXISTENTE
```
```
PC2 — Sprint 2 Review + velocidad
Formato Review:
  Sprint Goal: ___________________________
  Incremento: lista de HUs entregadas + puntos
  Criterios de aceptación: Dado/Cuando/Entonces ✅
  PO acepta: SÍ / NO (con retroalimentación)

Velocidad = puntos completados / sprint
  Sprint 1: 4 pts · Sprint 2: 15 pts
  Promedio: (4+15)/2 ≈ 10 pts/sprint
  → Sprint 3 compromiso máximo: ~10 pts
```

---

## MARTES — Momento Tobón: DESARROLLO (inicio)
**Propósito:** `editar_producto` parte GET con `instance=` pre-poblado + `editar.html`.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué hace `ProductoForm(instance=producto)` en el GET?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | `editar_producto` GET: `get_object_or_404` + `ProductoForm(instance=producto)` → form pre-poblado | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC3** — copia `editar_producto` parte GET completa | Nota PC3 | Libreta | — |
| 17:10 | 20 | 🔍 | **IA-1**: investigar y copiar resultado en libreta | Nota IA-1 | IA + Libreta | — |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 35 | 💻 | Implementar `editar_producto` (sólo bloque GET) en `views.py` + crear `editar.html` con `{% csrf_token %}` y `form.errors` | Vista GET + plantilla | VS Code | — |
| 18:10 | 25 | 💻 | Verificar GET `/productos/1/editar/` → form con datos actuales + probar con otro ID + `manage.py check` | GET verificado | Navegador | — |
| 18:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:40 | 20 | ✅ | Coevaluación: probar el GET del compañero con IDs distintos; verificar que el nombre ya aparece en el campo | Lista de cotejo | — | — |
| 19:00 | 15 | 📤🔄 | Subir `views.py` (GET editar) + `editar.html` + anticipo del miércoles | Avance subido | Classroom | Classroom |
| 19:15 | 15 | 🎭 | Revisión en parejas: ¿el `instance=` pre-pobla correctamente los 3 campos? | Lista de cotejo | — | — |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC3 — editar_producto parte GET
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    # --- GET: pre-poblar el formulario ---
    form = ProductoForm(instance=producto)   # campos con datos actuales
    return render(request, "productos/editar.html",
                  {"form": form, "producto": producto})

# Verificacion GET:
#   /productos/1/editar/ → status 200
#   form muestra "Teclado USB" en el campo nombre
#   form muestra "350.00" en el campo precio
#   /productos/999/editar/ → Http404 (no existe)
```
```
IA-1 (copiar pregunta y resultado):
Pregunta: ¿Cuál es la diferencia entre crear un ModelForm con
instance= y sin instance=? ¿Qué ocurre en la base de datos en
cada caso cuando se llama a form.save()?
Resultado: ____________________________________________
```

---

## MIÉRCOLES — Momento Tobón: DESARROLLO (profundización)
**Propósito:** POST de `editar_producto` + `eliminar_producto` completo + enlaces en plantillas.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿por qué eliminar necesita un formulario POST y no un simple enlace `<a href>`?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | POST de `editar` con `instance=`; patrón GET/POST de `eliminar` (confirmación + borrado); `Http404` | — | Pizarrón | — |
| 17:00 | 15 | 🔍 | **IA-2**: investigar y copiar resultado en libreta | Nota IA-2 | IA + Libreta | — |
| 17:15 | 10 | ✏️ | **PC4** — copia `eliminar_producto` GET/POST con confirmación | Nota PC4 | Libreta | — |
| 17:25 | 10 | 💻 | Inicio del bloque POST de `editar_producto`: `ProductoForm(request.POST, instance=producto)` + `is_valid()` | Avance POST editar | VS Code | — |
| 17:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:40 | 30 | 💻 | Completar POST `editar` + implementar `eliminar_producto` completo (GET confirmación + POST borrado + `eliminar.html`) | Vistas completas | VS Code | — |
| 18:10 | 25 | 💻 | Actualizar `lista.html` y `detalle.html` con enlaces editar/eliminar + verificar CRUD en navegador | Plantillas con enlaces | VS Code/Navegador | — |
| 18:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:40 | 20 | ✅ | Verificar ciclo: GET editar(200) · POST editar(302+BD) · GET eliminar(200+confirmación) · POST eliminar(302+borrado) | 4 caminos OK | Navegador | — |
| 19:00 | 15 | 🎭 | Coevaluación: probar eliminación del compañero — ¿aparece la confirmación? ¿se borra tras el POST? | Lista de cotejo | — | — |
| 19:15 | 15 | 📤🔄 | Subir `views.py` completo + `eliminar.html` + plantillas con enlaces + anticipo del jueves | Entregables subidos | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC4 — eliminar_producto GET/POST + confirmación
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == "POST":
        producto.delete()                    # ← borra de la BD
        return redirect("productos:lista")   # ← 302
    # GET: mostrar página de confirmación
    return render(request, "productos/eliminar.html",
                  {"producto": producto})

# En eliminar.html:
<form method="post">
    {% csrf_token %}
    <p>¿Eliminar "{{ producto.nombre }}"?</p>
    <p>Esta acción NO se puede deshacer.</p>
    <button type="submit">Sí, eliminar</button>
</form>
<a href="/productos/">Cancelar</a>

# Verificaciones:
# GET  /productos/2/eliminar/ → status 200 + nombre en confirmación
# POST /productos/2/eliminar/ → status 302 + producto.exists() == False
# GET  /productos/999/eliminar/ → Http404
```
```
IA-2 (copiar pregunta y resultado):
Pregunta: ¿Por qué en Django la eliminación de un registro requiere
un formulario POST y no un simple enlace <a href>? ¿Qué riesgo evita?
Resultado: ____________________________________________
```

---

## JUEVES — Momento Tobón: CIERRE (inicio)
**Propósito:** refactorizar `detalle_producto` a `get_object_or_404` + 9 aserciones + `sprint2_retrospective.md` + merge + flashcards.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿cuántos puntos completó tu equipo en el Sprint 2?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | Velocidad del equipo: cálculo; Sprint 3 preview (autenticación + `@login_required` + CBV) | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC5** — copia la refactorización a `get_object_or_404` + estructura de la retrospectiva | Nota PC5 | Libreta | — |
| 17:10 | 20 | 🔍 | **IA-3**: investigar y copiar resultado en libreta | Nota IA-3 | IA + Libreta | — |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 25 | 💻 | Refactorizar `detalle_producto` a `get_object_or_404` + verificar las 9 aserciones del CRUD completo | CRUD 9/9 verificado | Terminal | — |
| 18:00 | 30 | 💻 | Redactar `sprint2_retrospective.md` (velocidad + qué bien + qué mejorar + Sprint 3) + `git commit` + `merge sprint2 → main` + `push` | Retrospectiva + merge | VS Code/GitHub | GitHub |
| 18:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:35 | 25 | 🎭 | Taller de **flashcards** de la semana | 8 flashcards | Libreta/Quizlet | — |
| 19:00 | 15 | ✏️ | **PC6** — copia conceptos clave para flashcards | Nota PC6 | Libreta | — |
| 19:15 | 15 | 📤🔄 | Subir `sprint2_retrospective.md` + URL de `main` con merge + anticipo del viernes | Enlace subido | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC5 — Refactor get_object_or_404 + estructura retrospectiva
# Refactorizar detalle_producto:
# ANTES:
try:
    producto = Producto.objects.get(pk=producto_id)
except Producto.DoesNotExist:
    return HttpResponse("...", status=404)
# DESPUÉS:
producto = get_object_or_404(Producto, pk=producto_id)

# Estructura sprint2_retrospective.md:
## Sprint Goal verificado: SÍ/NO
## Incremento: tabla HU | Puntos | Estado
## Velocidad: sprint1 pts + sprint2 pts → promedio
## ¿Qué salió BIEN?
## ¿Qué MEJORAR?
## Acción concreta para Sprint 3
## Sprint 3 Preview: Sprint Goal candidato + HUs estimadas
```
```
PC6 — Conceptos clave (flashcards)
get_object_or_404 · Http404 · instance= · pre-poblar form
editar_producto: GET(pre-pop) + POST(instance) + 302
eliminar_producto: GET(confirmación) + POST(delete) + 302
producto.delete() · página de confirmación · diseño defensivo
Sprint Review · Sprint Retrospectiva · velocidad del equipo
Fibonacci · promedio pts/sprint · Sprint 3 preview
CRUD: Create✓ Read✓ Update✓ Delete✓
```
```
IA-3 (copiar pregunta y resultado):
Pregunta: ¿Qué es la velocidad del equipo en Scrum y cómo se usa
para planear de manera realista el siguiente sprint?
Resultado: ____________________________________________
```

---

## VIERNES — Momento Tobón: CIERRE (conclusión)
**Propósito:** Sprint 2 Review formal ante el docente + coevaluación + retrospectiva.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "demuestra el CRUD completo en menos de 2 minutos" | Demo rápida | Navegador | — |
| 16:50 | 30 | 🗣️ | **Sprint 2 Review formal**: CRUD completo en vivo (crear → leer → editar → eliminar) + `sprint2_retrospective.md` + `git log --graph` | Demostración ante docente (PO) | Navegador/Proyector | — |
| 17:20 | 10 | ✅ | Coevaluación con rúbrica entre pares | Rúbrica llena | Classroom | Classroom |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 30 | ✅ | Verificación final: 9 aserciones + merge a `main` + retrospectiva con velocidad + Sprint 3 preview | Checklist validado | Terminal/GitHub | — |
| 18:05 | 20 | 📝 | **Retrospectiva de equipo**: ¿qué salió bien esta semana? ¿qué acción concreta para el Sprint 3? | Notas retro | Libreta | — |
| 18:25 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:30 | 30 | 🎭 | Repaso colaborativo con flashcards: CRUD + Scrum Sprint 2 completo (juego por equipos) | Puntaje equipo | Quizlet/Libreta | — |
| 19:00 | 15 | ✏️ | **PC7** — cierre de la semana (ver texto abajo) | Nota PC7 | Libreta | — |
| 19:15 | 15 | 📤 | Subir evidencias finales + autoevaluación | Carpeta semana 6 | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta — PC7 (cierre obligatorio):**
```
PC7 — CIERRE SEMANA 6 "Ciclo cerrado"

[ ] CHECKLIST DE ENTREGABLES
    [ ] editar_producto: GET(200 pre-poblado) + POST válido(302+BD) +
        POST inválido(200 sin cambios) + Http404 ID inexistente
    [ ] eliminar_producto: GET(200 confirmación) + POST(302+borrado) +
        Http404 ID inexistente
    [ ] get_object_or_404 en TODAS las vistas (detalle, editar, eliminar)
    [ ] lista.html y detalle.html con enlaces editar y eliminar
    [ ] CRUD completo verificado: Create✓ Read✓ Update✓ Delete✓
    [ ] sprint2_retrospective.md con velocidad + qué mejorar + Sprint 3 preview
    [ ] Merge sprint2/modelos-orm → main publicado en GitHub
    [ ] Notas PC1–PC6 e IA-1, IA-2, IA-3 completas

CONCEPTOS CLAVE
    get_object_or_404 · Http404 · instance= (pre-poblar vs actualizar) ·
    editar: GET(pre-pop) + POST(instance=) + 302 ·
    eliminar: GET(confirmación) + POST(delete()) + 302 ·
    diseño defensivo · enlace vs formulario POST ·
    Sprint Review · Sprint Retrospectiva · velocidad ·
    Fibonacci · promedio pts/sprint · Sprint 3 autenticación/CBV ·
    CRUD completo (Create / Read / Update / Delete)

TAREA DE INVESTIGACIÓN (entregar el lunes de Semana 8)
    Investiga: ¿qué es @login_required en Django y cómo protege
    una vista? ¿Qué pasa si un usuario no autenticado intenta
    acceder a /productos/nuevo/?

PREGUNTA DE REFLEXIÓN FINAL
    La página de eliminación dice "¿estás seguro?" antes de borrar.
    La Retrospectiva dice "¿qué mejorar?" antes del siguiente sprint.
    ¿Qué principio de diseño comparten? ¿Por qué las acciones
    destructivas o de cambio mayor requieren confirmación explícita?
```

---

## Resumen semanal (Google Classroom)

| Día | Actividad en Classroom | Producto | Plazo |
|---|---|---|---|
| Lunes | Diagramas de flujo + `urls.py` | Diagramas editar/eliminar + `urls.py` con CRUD completo | Lunes 19:30 |
| Martes | `editar_producto` GET + `editar.html` | `views.py` (GET editar) + `editar.html` pre-poblado | Martes 19:30 |
| Miércoles | CRUD editar/eliminar + plantillas | `views.py` completo + `eliminar.html` + plantillas con enlaces | Miércoles 19:30 |
| Jueves | Retrospectiva + merge + retrospectiva | `sprint2_retrospective.md` + URL de `main` con merge | Jueves 19:30 |
| Viernes | Carpeta final Sprint 2 + autoevaluación | Código + retrospectiva + retro equipo + PC7 | Viernes 19:30 |

---

### Conteo de cumplimiento (verificación de reglas del ROL 3)
- Puntos de control: **PC1–PC7 (7 ≥ 5 mínimo)** ✓ · PC7 con checklist (8 ítems) + conceptos + tarea + reflexión ✓
- Investigaciones rápidas con IA: **IA-1 (martes), IA-2 (miércoles), IA-3 (jueves) = 3 ≥ 3 mínimo** ✓
- Bloques fijos diarios: arranque 5 min a las 16:45 · buffer 15 min al cierre · pausas activas cada ~45–60 min ✓
- Todos los días suman **180 min** verificados aritméticamente ✓ · Mini-exposiciones ≤10 min ✓
- Sprint 2 Review **formal ante el docente como Product Owner** el viernes ✓
- Review simulado en parejas el lunes (práctica antes del formal) ✓
- Tarea de investigación prepara la Semana 8 (`@login_required`, autenticación) ✓
- Pregunta de reflexión cierra el hilo conector (diseño defensivo: confirmación antes de acción destructiva) ✓

---

*Plan generado bajo ROL 3 — MicroEnseñanza · Prompt Maestro v1.0 · Metodología Tobón · Google Classroom.*
