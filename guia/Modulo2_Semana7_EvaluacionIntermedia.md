# Módulo II · Semana 7 — Evaluación Intermedia
## Técnico en Programación (SEP 3061300006-23) · UTEC Celaya
### Asesor: MC. Román Fernando López González

---

## 1. Identificación de la semana

| Campo | Detalle |
|---|---|
| Carrera | Técnico en Programación |
| Módulo | II — Desarrolla software con herramientas orientadas a la productividad (272 h) |
| Semana | 7 de 13 · **EVALUACIÓN INTERMEDIA** |
| Submódulos evaluados | S1 Frameworks (144 h) · S2 Metodologías ágiles (128 h) |
| **Hilo conector de la semana** | **"Corte de avance"** |
| Periodo evaluado | Semanas 1–6 (Módulo II completo hasta CRUD) |
| Carga horaria reportada | 17 h/semana (S1 = 9 h · S2 = 8 h) |
| Carga horaria real (planeación) | 14.16 h/semana |
| Tiempo fantasma máximo | 15 min/día |

> **Hilo conector:** la **rúbrica de evaluación ES el Definition of Done** del CRUD. Los criterios técnicos que el evaluador verifica son exactamente los criterios de aceptación que el estudiante debería haber escrito en su Product Backlog. Evaluar el código y revisar el Sprint son la misma operación formal: demostrar que el incremento cumple lo prometido.

---

## 2. Competencias evaluadas

**Resultado de aprendizaje (SEP):**
El estudiante demuestra que domina el desarrollo de software con herramientas orientadas a la productividad mediante: un sistema CRUD funcional construido con Django 4.2, la documentación ágil del proceso (backlogs, retrospectivas, Kanban) y la capacidad de extender el sistema ante un requerimiento nuevo.

**Lo que se evalúa:**
- **S1:** arquitectura Django (MVT), ORM, migraciones, formularios (`ModelForm`), CRUD completo, plantillas con herencia, manejo de errores (`get_object_or_404`, CSRF).
- **S2:** Product Backlog con criterios de aceptación, Daily Scrum log, Sprint Reviews, Retrospectiva con velocidad, tablero Kanban.

---

## 3. INSTRUMENTO DE EVALUACIÓN

### 3.1 Puntaje global

| Componente | Puntos |
|---|---|
| A — Modelo y base de datos | 15 |
| B — Formularios (`ModelForm`) | 10 |
| C — Vistas CRUD completo | 25 |
| D — Plantillas y URLs | 10 |
| E — Tarea de extensión práctica | 10 |
| F — Sprint Review y artefactos Scrum | 20 |
| G — Conocimientos teóricos (10 preguntas) | 10 |
| **Total** | **100** |

> **Acreditación:** ≥ 60 / 100 · Equivalencia Schmelkes: 60=6.0 · 70=7.0 · 80=8.0 · 90=9.0 · 100=10.0

---

### A — Modelo y base de datos (15 pts)

| Criterio | Excelente (3) | Bien (2) | Suficiente (1) | Insuficiente (0) |
|---|---|---|---|---|
| A1 — Campos correctos | 4 campos con tipos exactos (CharField, DecimalField, IntegerField, DateTimeField auto_now_add) | 3 campos correctos | 2 campos correctos | 1 o ningún campo correcto |
| A2 — `class Meta` | `ordering`, `verbose_name` y `verbose_name_plural` presentes | 2 de 3 | 1 de 3 | Ausente |
| A3 — `__str__` | Devuelve `f"{nombre} (${precio:.2f})"` formateado | Devuelve nombre y precio sin formato | Solo devuelve el nombre | Ausente o error |
| A4 — Migraciones | `[X] 0001_initial` aplicada; `showmigrations` lo confirma | Migración creada pero no aplicada | Migración con errores | Sin migración |
| A5 — Datos en BD | Al menos 3 productos reales creados desde el admin | 1–2 productos | BD vacía | No accede al admin |

---

### B — Formularios (10 pts)

| Criterio | Excelente (2) | Bien (1.5) | Suficiente (1) | Insuficiente (0) |
|---|---|---|---|---|
| B1 — `ProductoForm` definido | `ModelForm` con `fields` = [`nombre`,`precio`,`stock`]; `creado` excluido | `fields` correcto, `creado` incluido por error | Solo 2 campos en `fields` | Ausente o sin herencia de `ModelForm` |
| B2 — `labels` personalizados | Los 3 campos tienen etiquetas descriptivas | 2 de 3 | 1 de 3 | Sin `labels` |
| B3 — Validación funciona | `is_valid()` True con datos correctos; False con precio inválido o nombre vacío | Solo un caso funciona | Valida pero no muestra errores | No valida |
| B4 — Errores en plantilla | `{% if form.errors %}` muestra los errores al usuario | Muestra errores sin formato | Errores en consola únicamente | Sin manejo de errores |
| B5 — `form.as_p` | Formulario renderizado con `{{ form.as_p }}` en la plantilla | Campos renderizados manualmente | Formulario HTML sin DTL | Sin formulario HTML |

---

### C — Vistas CRUD (25 pts)

| Vista | Criterio | Pts max | Indicadores de verificación |
|---|---|---|---|
| **C1 Lista** | `lista_productos` con ORM | 3 | `Producto.objects.all()` · status 200 · plantilla renderizada · herencia `base.html` |
| **C2 Detalle** | `detalle_producto` con `get_object_or_404` | 3 | `get_object_or_404(Producto, pk=id)` · status 200 con datos · Http404 en ID inexistente |
| **C3 Crear** | `crear_producto` ciclo GET/POST | 5 | GET 200 form vacío · POST válido 302 + BD · POST inválido 200 sin guardar · `{% csrf_token %}` |
| **C4 Editar** | `editar_producto` con `instance=` | 7 | GET 200 form pre-poblado · POST válido 302 + BD actualizada · POST inválido sin cambios · Http404 ID inexistente |
| **C5 Eliminar** | `eliminar_producto` confirmación | 7 | GET 200 con confirmación · POST 302 + borrado en BD · Http404 ID inexistente · `{% csrf_token %}` |

> **Verificación técnica directa** (el evaluador ejecuta estos comandos):
> ```bash
> python3 manage.py check
> # Esperado: "System check identified no issues (0 silenced)."
>
> python3 -c "
> import django, os, sys
> os.environ['DJANGO_SETTINGS_MODULE']='inventario_proyecto.settings'
> sys.path.insert(0,'.')
> django.setup()
> from productos.models import Producto
> print(Producto.objects.count(), 'productos en BD')
> print([str(p) for p in Producto.objects.all()[:3]])
> "
> ```

---

### D — Plantillas y URLs (10 pts)

| Criterio | Puntos | Indicador |
|---|---|---|
| D1 — `base.html` con bloques `title` y `content` | 2 | `{% block title %}` y `{% block content %}` presentes |
| D2 — Herencia en todas las plantillas | 2 | `{% extends "base.html" %}` en lista, detalle, crear, editar, eliminar |
| D3 — `{% csrf_token %}` en todos los forms POST | 2 | Presente en crear, editar y eliminar |
| D4 — URL order correcto | 2 | `nuevo/` declarado antes de `<int:producto_id>/` en `urls.py` |
| D5 — `app_name` y namespace | 1 | `app_name = "productos"` en `urls.py` |
| D6 — URLs de editar y eliminar | 1 | Rutas `<int:id>/editar/` y `<int:id>/eliminar/` registradas |

---

### E — Tarea de extensión práctica (10 pts)

**Instrucción:** En los primeros 60 minutos de la sesión de evaluación (martes), el estudiante agrega el siguiente campo al modelo `Producto` y demuestra que el sistema sigue funcionando:

```python
# Agregar en models.py, antes del campo 'creado':
activo = models.BooleanField(
    default=True,
    verbose_name="Activo",
)
```

**Lo que debe producir:**

```bash
# 1. Nueva migración
python3 manage.py makemigrations productos
# → Resultado esperado: "Add field activo to producto"

python3 manage.py migrate
# → OK

python3 manage.py showmigrations productos
# → [X] 0001_initial
# → [X] 0002_producto_activo
```

```python
# 2. Actualizar admin.py — añadir "activo" a list_display:
list_display = ["nombre", "precio", "stock", "activo", "creado"]
```

```html
<!-- 3. Actualizar lista.html — mostrar estado activo: -->
{% if p.activo %}✓{% else %}✗{% endif %}
```

| Sub-criterio | Pts |
|---|---|
| E1 — Campo `activo` definido correctamente en `models.py` | 2 |
| E2 — Migración `0002` generada y aplicada sin errores | 3 |
| E3 — Admin muestra columna `activo` | 2 |
| E4 — Plantilla `lista.html` muestra ✓/✗ según `p.activo` | 2 |
| E5 — `manage.py check` sin errores tras la extensión | 1 |

---

### F — Sprint Review y artefactos Scrum (20 pts)

| Criterio | Puntos | Indicador |
|---|---|---|
| F1 — `product_backlog.md` con ≥5 HUs | 2 | Archivo presente; HUs con ID, descripción y prioridad |
| F2 — Criterios de aceptación Gherkin en ≥2 HUs | 3 | Formato Dado/Cuando/Entonces en HU-01 y HU-01a mínimo |
| F3 — `sprint1_review.md` o equivalente | 2 | Sprint Goal verificado; incremento descrito |
| F4 — `sprint2_retrospective.md` | 4 | Sprint Goal · velocidad calculada (pts/sprint) · qué bien/qué mejorar · acción concreta |
| F5 — Daily Scrum log ≥3 entradas | 3 | 3 preguntas respondidas cada día; ≥1 impedimento documentado |
| F6 — Kanban con columnas y estado final | 3 | Columnas To Do/In Progress/Done; HU-04 en Done |
| F7 — Sprint 3 preview | 3 | Sprint Goal candidato + ≥2 HUs estimadas con Fibonacci |

---

### G — Conocimientos teóricos (10 pts, 1 pt c/u)

El estudiante responde por escrito en la libreta. El evaluador verifica la respuesta mínima esperada.

| # | Pregunta | Respuesta mínima esperada |
|---|---|---|
| G1 | ¿Qué diferencia hay entre un *framework* y una *librería*? | Framework llama al código del programador; librería es llamada por el programador |
| G2 | Describe el patrón MVT de Django | Model (datos), View (lógica), Template (presentación); urls.py como enrutador |
| G3 | ¿Qué hace `makemigrations`? ¿Y `migrate`? | `makemigrations` genera el archivo `.py`; `migrate` lo aplica a la BD |
| G4 | ¿Cuándo usarías `instance=producto` en `ProductoForm`? | Para editar un objeto existente; sin `instance=` se crea uno nuevo |
| G5 | ¿Por qué `get_object_or_404` es preferible a `try/except DoesNotExist`? | Es más conciso (1 línea vs 3); mismo resultado: Http404 si no existe |
| G6 | ¿Por qué eliminar requiere POST y no un enlace `<a href>`? | Un enlace GET puede ser ejecutado por bots/prefetch; POST requiere intención explícita del usuario |
| G7 | ¿Qué hace `{% extends "base.html" %}`? | La plantilla hija hereda la estructura; solo sobreescribe los `{% block %}` |
| G8 | ¿Qué son los puntos de historia y por qué se usa Fibonacci? | Miden complejidad relativa; Fibonacci porque la incertidumbre crece no linealmente |
| G9 | ¿Qué problema resuelve el patrón Post-Redirect-Get (PRG)? | Evita que recargar la página envíe el formulario dos veces |
| G10 | ¿Qué diferencia hay entre `Sprint Review` y `Sprint Retrospectiva`? | Review inspecciona el *incremento*; Retrospectiva inspecciona el *proceso* del equipo |

---

## 4. PARTE II — Momentos didácticos: procedimiento de la semana

### Lunes — Preparación y autodiagnóstico
El docente explica el instrumento de evaluación completo (rúbricas, tarea de extensión, preguntas). Los estudiantes realizan un autodiagnóstico usando el checklist de la §3.8 y corrigen pendientes antes del martes.

### Martes — Evaluación técnica práctica (S1)
- **Primeros 60 min:** tarea de extensión práctica (campo `activo` → migración → admin → template).
- **Siguientes 90 min:** verificación técnica de las 27 pruebas del CRUD con el evaluador.
- **30 min:** preguntas teóricas (G1–G10) en la libreta.

### Miércoles — Sprint Review formal (S2)
El estudiante presenta el sistema ante el docente (rol de Product Owner):
1. Demostración CRUD en vivo (≤5 minutos).
2. Presentación de `sprint2_retrospective.md` y Kanban.
3. Velocidad calculada y Sprint 3 preview.
4. El PO acepta o devuelve con retroalimentación.

### Jueves — Retroalimentación y correcciones
El docente entrega las rúbricas completadas. Los estudiantes corrigen los ítems con puntaje < 1 en una sesión de trabajo autónomo.

### Viernes — Cierre y apertura del Sprint 3
Autoevaluación, firma de conformidad con la calificación, presentación de correcciones y arranque del Sprint 3 (autenticación — Semana 8).

---

## 5. Autoevaluación del estudiante

Antes del martes, el estudiante completa este checklist. Cada ✅ es un punto de confianza; cada ✗ es una corrección prioritaria.

```
CHECKLIST DE AUTOEVALUACIÓN — Evaluación Intermedia M2

MODELO
[ ] models.py: 4 campos con tipos correctos
[ ] Meta: ordering + verbose_name + verbose_name_plural
[ ] __str__: devuelve nombre y precio formateado ($X.XX)
[ ] [X] 0001_initial en showmigrations

FORMS
[ ] ProductoForm: fields = [nombre, precio, stock]
[ ] "creado" NO aparece en el formulario
[ ] Formulario válido con datos correctos
[ ] Formulario inválido con precio = "abc"

VISTAS CRUD
[ ] lista_productos: objects.all() + status 200
[ ] detalle_producto: get_object_or_404 + Http404 si ID no existe
[ ] crear_producto: GET(200) + POST válido(302+BD) + POST inválido(200)
[ ] editar_producto: GET pre-poblado(200) + POST instance=(302+BD)
[ ] eliminar_producto: GET confirmación(200) + POST(302+borrado)

PLANTILLAS
[ ] base.html: bloques title y content
[ ] Todas las plantillas: {% extends "base.html" %}
[ ] {% csrf_token %} en crear, editar y eliminar
[ ] urls.py: nuevo/ antes de <int:id>/

SCRUM
[ ] product_backlog.md con ≥5 HUs
[ ] Criterios de aceptación Gherkin en ≥2 HUs
[ ] sprint2_retrospective.md con velocidad calculada
[ ] Daily Scrum log ≥3 entradas con impedimento
[ ] Kanban con HU-04 en Done
[ ] Sprint 3 preview con Sprint Goal y HUs estimadas
```

---

## 6. Criterios de acreditación

| Puntuación | Equivalencia Schmelkes | Nivel |
|---|---|---|
| 90–100 | 9.0–10.0 | Sobresaliente |
| 80–89 | 8.0–8.9 | Notable |
| 70–79 | 7.0–7.9 | Bien |
| 60–69 | 6.0–6.9 | Suficiente |
| < 60 | < 6.0 | No acredita — presentar correcciones el jueves |

> **Condición mínima para acreditar la evaluación práctica:** `manage.py check` sin errores y al menos Create + Read funcionando (C1 + C2 + C3 ≥ 8 pts).

---

## 7. Recursos

- Proyecto Django de la Semana 6 en `main` (Sprint 2 cerrado).
- Computadora con Python 3.11+, Django 4.2 y VS Code.
- Navegador web para demostración en vivo.
- GitHub Projects con Kanban actualizado.
- `sprint2_retrospective.md` y todos los artefactos Scrum de las Semanas 1–6.
- Google Classroom para entrega de evidencias de evaluación.

---

## 8. Referencias (APA 7)

Cohn, M. (2005). *Agile estimating and planning*. Prentice Hall.

Django Software Foundation. (s.f.). *Django documentation*. https://docs.djangoproject.com/en/4.2/

Fowler, M. (2003). *Patterns of enterprise application architecture*. Addison-Wesley.

Schmelkes, C., & Schmelkes, N. (2010). *Manual para la presentación de anteproyectos e informes de investigación (tesis)* (3.ª ed.). Oxford University Press.

Schwaber, K., & Sutherland, J. (2020). *La guía de Scrum*. https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf

---

*Guía de Evaluación Intermedia generada bajo ROL 1/ROL 2 · Prompt Maestro v1.0 · Celaya, junio 2026.*
*Base empírica: suite de 27 verificaciones automatizadas (27/27 pasan en el proyecto de referencia).*
*Tarea de extensión verificada: campo `activo` BooleanField(default=True) + migración `0002` aplicada sin errores.*
