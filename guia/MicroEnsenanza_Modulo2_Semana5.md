# MicroEnseñanza — Módulo II · Semana 5
## Técnico en Programación (SEP 3061300006-23) · UTEC Celaya
### Asesor: MC. Román Fernando López González

| Campo | Detalle |
|---|---|
| Módulo / Semana | II / 5 de 13 |
| Hilo conector | "El primer incremento funcional" |
| Submódulos | S1 Frameworks (`forms.py`, `ModelForm`, GET/POST, CSRF, `form.errors`) · S2 Ágiles (Daily Scrum, impediment log, Kanban actualizado) |
| Stack | Django 4.2 · `ModelForm` · CSRF · Python 3.11+ · GitHub Projects |
| Horario | 16:45–19:45 (180 min/día) |
| Plataforma institucional | Google Classroom |
| Tiempo fantasma (buffer) | 15 min/día máximo (último bloque) |
| Regla del docente | Expone ≤10 min por bloque; el resto circula y asesora |
| Prerrequisito | Semana 4 — modelo `Producto` + admin + vistas con ORM en rama `sprint2/modelos-orm` |

**Leyenda de tipos:** 🟡 Arranque en frío · 📖 Mini-exposición (≤10 min) · ✏️ Copia en libreta / Punto de control · 🔍 Investigación rápida con IA · 💻 Práctica de laboratorio · ✅ Verificación/Coevaluación · 🎭 Taller colaborativo · 🗣️ Presentación oral · 📝 Reflexión/Retrospectiva · 📤 Subir a Classroom · 🔄 Anticipo del día siguiente · ⏸️ Pausa activa · 🆓 Buffer

---

## LUNES — Momento Tobón: APERTURA
**Propósito:** problema "usuario sin admin" + `ModelForm` (concepto) + diagrama GET/POST + Daily Scrum intro + rúbrica.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿puede un usuario sin contraseña de admin registrar un producto?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | `ModelForm`: hereda tipos del modelo; `class Meta`; `fields`; campos excluidos | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC1** — copia la estructura de `ModelForm` con `Meta` | Nota PC1 | Libreta | — |
| 17:10 | 25 | 🎭 | Dibujar en libreta el diagrama completo GET/POST (3 caminos: GET · POST válido · POST inválido) | Diagrama GET/POST | Libreta | — |
| 17:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:40 | 10 | 📖 | Daily Scrum: las 3 preguntas; 15 min máximo; no es un reporte | — | Pizarrón | — |
| 17:50 | 10 | ✏️ | **PC2** — copia las 3 preguntas del Daily Scrum y el formato del log | Nota PC2 | Libreta | — |
| 18:00 | 25 | 🎭 | Primer Daily Scrum simulado (equipos de 3): responder las 3 preguntas sobre el Sprint 2 | Daily Scrum oral | — | — |
| 18:25 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:30 | 25 | ✅ | Revisión de la **rúbrica** + `manage.py check` del proyecto de la Semana 4 | Check sin errores | Terminal | Classroom |
| 18:55 | 25 | 💻 | Crear `productos/forms.py` con estructura `ProductoForm` + `Meta` vacía (esqueleto) | `forms.py` inicial | VS Code | — |
| 19:20 | 10 | 📤🔄 | Subir diagrama GET/POST + `forms.py` inicial + anticipo del martes | Evidencia subida | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC1 — Estructura de ModelForm
# productos/forms.py
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model  = Producto
        fields = ["nombre", "precio", "stock"]
        # "creado" NO está en fields → Django lo excluye del form
        labels = {
            "nombre": "Nombre del producto",
            "precio": "Precio unitario ($)",
            "stock":  "Unidades en stock",
        }
# ModelForm hereda tipos del modelo:
# nombre → CharField → <input type="text">
# precio → DecimalField → <input type="number">
# stock  → IntegerField → <input type="number">
```
```
PC2 — Daily Scrum: 3 preguntas (máx. 15 min)
1. ¿Qué hice AYER para acercarme al Sprint Goal?
2. ¿Qué haré HOY para acercarme al Sprint Goal?
3. ¿Hay algún IMPEDIMENTO que me bloquee?
Regla: no es un reporte al Scrum Master.
        el equipo habla ENTRE SÍ.
Formato del log:
  Fecha | ¿Qué hice? | ¿Qué haré? | ¿Impedimentos?
```

---

## MARTES — Momento Tobón: DESARROLLO (inicio)
**Propósito:** completar `forms.py` + vista `crear_producto` (parte GET).

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué campos expone `ProductoForm` al usuario?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | `ModelForm`: `fields`, `labels`, campos excluidos; por qué `creado` no aparece | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC3** — copia `ProductoForm` completo con `Meta` y `labels` | Nota PC3 | Libreta | — |
| 17:10 | 20 | 🔍 | **IA-1**: investigar y copiar resultado en libreta | Nota IA-1 | IA + Libreta | — |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 35 | 💻 | Completar `forms.py` (fields + labels) + importar en `views.py` + vista GET: `form = ProductoForm()` | `forms.py` + vista GET | VS Code | — |
| 18:10 | 25 | 💻 | Crear `productos/templates/productos/crear.html` (GET: `{{ form.as_p }}`, sin lógica POST aún) | `crear.html` parcial | VS Code | — |
| 18:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:40 | 20 | ✅ | Verificar GET `/productos/nuevo/` → 200 con 3 campos; `creado` ausente | GET verificado | Navegador | — |
| 19:00 | 15 | 📤🔄 | Subir `forms.py` + `views.py` (GET) + `crear.html` parcial + anticipo del miércoles | Avance subido | Classroom | Classroom |
| 19:15 | 15 | 🎭 | Revisión en parejas: ¿aparecen los 3 campos con los labels correctos? | Lista de cotejo | — | — |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC3 — ProductoForm completo
class ProductoForm(forms.ModelForm):
    class Meta:
        model  = Producto
        fields = ["nombre", "precio", "stock"]
        labels = {
            "nombre": "Nombre del producto",
            "precio": "Precio unitario ($)",
            "stock":  "Unidades en stock",
        }

# En views.py (parte GET):
from .forms import ProductoForm

def crear_producto(request):
    form = ProductoForm()           # formulario vacio
    return render(request, "productos/crear.html", {"form": form})

# Verificacion: GET /productos/nuevo/ → status 200
#               3 campos en la respuesta, "creado" ausente
```
```
IA-1 (copiar pregunta y resultado):
Pregunta: ¿Qué ventaja tiene ModelForm sobre crear un formulario
HTML manualmente? ¿Qué código te ahorra?
Resultado: ____________________________________________
```

---

## MIÉRCOLES — Momento Tobón: DESARROLLO (profundización)
**Propósito:** POST válido/inválido + `redirect()` + gotcha del orden de URLs.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué devuelve `crear_producto` si el POST tiene campos vacíos?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | Ciclo POST: `is_valid()` → `save()` → `redirect()`; gotcha crítico: orden de URL patterns | — | Pizarrón | — |
| 17:00 | 15 | 🔍 | **IA-2**: investigar y copiar resultado en libreta | Nota IA-2 | IA + Libreta | — |
| 17:15 | 10 | ✏️ | **PC4** — copia el ciclo GET/POST completo con `redirect` | Nota PC4 | Libreta | — |
| 17:25 | 10 | 💻 | Inicio del bloque POST en `views.py`: `if request.method == "POST": form = ProductoForm(request.POST)` | Avance POST | VS Code | — |
| 17:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:40 | 30 | 💻 | Completar POST: `is_valid()` → `save()` → `redirect("productos:lista")` + rama `else` con form vacío | Vista completa | VS Code | — |
| 18:10 | 25 | 💻 | Actualizar `urls.py`: colocar `nuevo/` **antes** de `<int:producto_id>/` + `manage.py check` | `urls.py` corregido | VS Code/Terminal | — |
| 18:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:40 | 20 | ✅ | Verificar POST válido (302 + producto en BD) y POST inválido (200 + errores en respuesta) | 2 caminos verificados | Navegador | — |
| 19:00 | 15 | 🎭 | Coevaluación: probar el POST del compañero con datos inválidos y verificar errores | Lista de cotejo | — | — |
| 19:15 | 15 | 📤🔄 | Subir `views.py` completo + `urls.py` corregido + anticipo del jueves | Entregables subidos | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC4 — Ciclo GET/POST completo + redirect
def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()                          # guarda en BD
            return redirect("productos:lista")   # POST-Redirect-Get
        # si no es válido: cae al return de abajo con errores
    else:
        form = ProductoForm()   # GET: form vacío
    return render(request, "productos/crear.html", {"form": form})

# Resultados esperados:
# GET              → status 200 (form vacío)
# POST válido      → status 302 (redirect a lista)
# POST inválido    → status 200 (form con errores)

# ⚠️ GOTCHA — orden de URLs (CRITICO):
# ✓ CORRECTO:
#   path("productos/nuevo/", ...)           # primero
#   path("productos/<int:producto_id>/",...)# segundo
# ✗ INCORRECTO: Django trata "nuevo" como int → error 404
```
```
IA-2 (copiar pregunta y resultado):
Pregunta: ¿Qué es el patrón Post-Redirect-Get (PRG) y qué problema
resuelve en las aplicaciones web?
Resultado: ____________________________________________
```

---

## JUEVES — Momento Tobón: CIERRE (inicio)
**Propósito:** `crear.html` con `{% csrf_token %}` y `form.errors` + `daily_scrum_log.md` + Kanban + flashcards.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué error devuelve Django si olvidas `{% csrf_token %}`?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | CSRF: qué es el ataque, por qué `{% csrf_token %}` es obligatorio, error 403 | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC5** — copia `{% csrf_token %}` + `form.errors` + gotcha orden URLs | Nota PC5 | Libreta | — |
| 17:10 | 20 | 🔍 | **IA-3**: investigar y copiar resultado en libreta | Nota IA-3 | IA + Libreta | — |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 25 | 💻 | Completar `crear.html`: añadir `{% csrf_token %}` + bloque `{% if form.errors %}` + enlace cancelar | `crear.html` completa | VS Code | — |
| 18:00 | 30 | 💻 | Redactar `daily_scrum_log.md` (3 días: mar/mié/jue) + actualizar Kanban: HU-02→Done, HU-03→In Progress | `daily_scrum_log.md` + Kanban | VS Code/GitHub | GitHub |
| 18:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:35 | 25 | 🎭 | Taller de **flashcards** de la semana | 8 flashcards | Libreta/Quizlet | — |
| 19:00 | 15 | ✏️ | **PC6** — copia conceptos clave para flashcards | Nota PC6 | Libreta | — |
| 19:15 | 15 | 📤🔄 | Subir `crear.html` + `daily_scrum_log.md` + URL del Kanban + anticipo del viernes | Enlace subido | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC5 — {% csrf_token %} + form.errors + URL order
<!-- En crear.html: -->
<form method="post">
    {% csrf_token %}     ← OBLIGATORIO en todo form POST
    {{ form.as_p }}      ← genera campos con labels
    <button type="submit">Guardar</button>
</form>

<!-- Mostrar errores de validacion: -->
{% if form.errors %}
<ul>
{% for campo, errores in form.errors.items %}
    <li>{{ campo }}: {{ errores|join:", " }}</li>
{% endfor %}
</ul>
{% endif %}

# Sin {% csrf_token %} → Django devuelve HTTP 403 Forbidden
# Orden urls.py: "productos/nuevo/" ANTES de "productos/<int:>/"
```
```
PC6 — Conceptos clave (flashcards)
ModelForm · class Meta · fields · labels · exclude
GET / POST · request.method · is_valid() · save() · redirect()
form.as_p · form.errors · {% csrf_token %} · HTTP 302 · HTTP 403
Post-Redirect-Get (PRG) · gotcha URL order
Daily Scrum · impedimento · Kanban: Done / In Progress
```
```
IA-3 (copiar pregunta y resultado):
Pregunta: ¿Qué es CSRF (Cross-Site Request Forgery) y por qué
Django requiere {% csrf_token %} en todos los formularios POST?
Resultado: ____________________________________________
```

---

## VIERNES — Momento Tobón: CIERRE (conclusión)
**Propósito:** Sprint Review + coevaluación + retrospectiva.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "demuestra el primer incremento funcional del sprint" | Respuesta rápida | Libreta | — |
| 16:50 | 30 | 🗣️ | **Sprint Review**: demostrar ciclo completo GET/POST + errores + redirect + producto en lista | Demostración en vivo | Navegador/Proyector | — |
| 17:20 | 10 | ✅ | Coevaluación con rúbrica entre pares | Rúbrica llena | Classroom | Classroom |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 30 | ✅ | Verificación final: 8 aserciones (form vacío · form válido · form inválido · GET 200 + csrf · POST 302 + BD · POST inválido 200 · lista · labels) | Checklist validado | Terminal | — |
| 18:05 | 20 | 📝 | **Retrospectiva**: qué funcionó / qué mejorar (especialmente el gotcha del orden de URLs) | Notas retro | Libreta | — |
| 18:25 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:30 | 30 | 🎭 | Repaso colaborativo con flashcards (juego por equipos) | Puntaje equipo | Quizlet/Libreta | — |
| 19:00 | 15 | ✏️ | **PC7** — cierre de la semana (ver texto abajo) | Nota PC7 | Libreta | — |
| 19:15 | 15 | 📤 | Subir evidencias finales + autoevaluación | Carpeta semana 5 | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta — PC7 (cierre obligatorio):**
```
PC7 — CIERRE SEMANA 5 "El primer incremento funcional"

[ ] CHECKLIST DE ENTREGABLES
    [ ] forms.py con ProductoForm: 3 campos, "creado" excluido, labels
    [ ] views.py: GET(200) + POST válido(302+BD) + POST inválido(200+errores)
    [ ] crear.html con {% csrf_token %} y form.errors visible
    [ ] urls.py: "nuevo/" ANTES de "<int:producto_id>/"
    [ ] daily_scrum_log.md: 3 días (mar/mié/jue) + ≥1 impedimento
    [ ] Kanban: HU-02 → Done | HU-03 → In Progress
    [ ] Commit en rama sprint2/modelos-orm publicado
    [ ] Notas PC1–PC6 e IA-1, IA-2, IA-3 completas

CONCEPTOS CLAVE
    ModelForm · class Meta · fields · labels · forms.py ·
    GET/POST · request.method · is_valid() · save() · redirect() ·
    form.as_p · form.errors · {% csrf_token %} · HTTP 302 · HTTP 403 ·
    Post-Redirect-Get · gotcha URL order ·
    Daily Scrum · impedimento · Kanban Done/In Progress

TAREA DE INVESTIGACIÓN (entregar el lunes)
    Investiga: ¿cómo se edita un objeto existente con ModelForm en
    Django? ¿Cómo se instancia el formulario con datos previos
    usando instance=? Trae un ejemplo mínimo en la libreta.

PREGUNTA DE REFLEXIÓN FINAL
    El formulario tiene 3 caminos: GET (mostrar), POST válido
    (guardar y redirigir), POST inválido (mostrar errores).
    El Daily Scrum también tiene 3 respuestas: avancé, avanzaré,
    tengo un impedimento. ¿Qué estructura comparten los dos?
```

---

## Resumen semanal (Google Classroom)

| Día | Actividad en Classroom | Producto | Plazo |
|---|---|---|---|
| Lunes | Diagrama GET/POST + `forms.py` inicial | Diagrama + `forms.py` con esqueleto `Meta` | Lunes 19:30 |
| Martes | `forms.py` completo + vista GET | `forms.py` + `views.py` (GET) + `crear.html` parcial | Martes 19:30 |
| Miércoles | Vista POST completa + URLs | `views.py` completo + `urls.py` corregido | Miércoles 19:30 |
| Jueves | `crear.html` + Daily Scrum + Kanban | `crear.html` con csrf/errors + `daily_scrum_log.md` + URL del Kanban | Jueves 19:30 |
| Viernes | Carpeta final + autoevaluación | Código + log + retro + PC7 | Viernes 19:30 |

---

### Conteo de cumplimiento (verificación de reglas del ROL 3)
- Puntos de control: **PC1–PC7 (7 ≥ 5 mínimo)** ✓ · PC7 con checklist (8 ítems) + conceptos + tarea + reflexión ✓
- Investigaciones rápidas con IA: **IA-1 (martes), IA-2 (miércoles), IA-3 (jueves) = 3 ≥ 3 mínimo** ✓
- Bloques fijos diarios: arranque 5 min a las 16:45 · buffer 15 min al cierre · pausas activas cada ~45–60 min ✓
- Todos los días suman **180 min** verificados aritméticamente ✓ · Mini-exposiciones ≤10 min ✓
- Continuidad: parte del proyecto de Semana 4 (modelo + admin + ORM) ✓
- Daily Scrum simulado el lunes en equipos de 3 (actividad oral) ✓
- Gotcha del orden de URLs documentado como lección aprendida en retrospectiva ✓
- Tarea de investigación prepara Semana 6 (`instance=` para edición) ✓

---

*Plan generado bajo ROL 3 — MicroEnseñanza · Prompt Maestro v1.0 · Metodología Tobón · Google Classroom.*
