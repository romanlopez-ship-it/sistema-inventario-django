# Módulo II · Semana 6 — Guía Académica y de Laboratorio
## Técnico en Programación (SEP 3061300006-23) · UTEC Celaya
### Asesor: MC. Román Fernando López González

---

## 1. Identificación de la semana

| Campo | Detalle |
|---|---|
| Carrera | Técnico en Programación |
| Módulo | II — Desarrolla software con herramientas orientadas a la productividad (272 h) |
| Semana | 6 de 13 |
| Submódulos integrados | S1 Frameworks (144 h) · S2 Metodologías ágiles (128 h) |
| **Hilo conector de la semana** | **"Ciclo cerrado"** |
| Stack | Django 4.2 LTS · `get_object_or_404` · `instance=` · Python 3.11+ |
| Carga horaria reportada | 17 h/semana (S1 = 9 h · S2 = 8 h) |
| Carga horaria real (planeación) | 14.16 h/semana |
| Tiempo fantasma máximo | 15 min/día |
| Plataforma institucional | Google Classroom |
| Prerrequisito | Semana 5 — `crear_producto` con `ModelForm` + Daily Scrum log en rama `sprint2/modelos-orm` |

> **Hilo conector:** en el CRUD, *editar* corrige un dato existente y *eliminar* cierra el ciclo de vida de un producto. En el Sprint 2, la *Retrospectiva* corrige la forma de trabajar del equipo y el *Sprint Review* cierra formalmente la iteración. Esta semana ambos ciclos terminan con una confirmación explícita: la página "¿estás seguro de eliminar?" confirma antes de borrar; el Sprint Review confirma que el incremento cumple el Sprint Goal antes de cerrar. Completar el CRUD y cerrar el sprint son la misma operación en dos planos distintos.

---

## 2. Competencias de la semana

**Resultado de aprendizaje (SEP):**
El estudiante implementa las operaciones de actualización y eliminación con `ModelForm`, `get_object_or_404` y página de confirmación; cierra el Sprint 2 con Review, Retrospectiva y cálculo de velocidad, y describe el Sprint 3 que comienza la semana siguiente.

**Actividades clave de la competencia laboral:**

- **S1 — Frameworks:** Implementa `editar_producto` con `instance=` para pre-poblar el formulario; implementa `eliminar_producto` con página de confirmación GET y borrado en POST; sustituye `try/except DoesNotExist` por `get_object_or_404`; añade enlaces editar/eliminar en lista y detalle.
- **S2 — Metodologías ágiles:** Realiza el Sprint 2 Review (CRUD completo como incremento verificable); documenta la Sprint 2 Retrospectiva; calcula la velocidad del equipo; elabora el Sprint 3 Planning inicial.

---

## 3. PARTE I — Estructura académica (modelo Corina Schmelkes)

### 3.1 Introducción

La semana anterior el estudiante entregó la operación de *creación*: un usuario puede registrar productos. Esta semana cierra las dos operaciones restantes. La documentación oficial de Django (Django Software Foundation, s.f.) describe `get_object_or_404` como un atajo que combina `objects.get()` con el manejo del error 404 en una sola línea, siguiendo el principio DRY. El parámetro `instance=` en `ModelForm` —también documentado en Django Software Foundation (s.f.)— permite pre-poblar un formulario con los datos de un objeto existente, de modo que el POST siguiente actualiza ese objeto en lugar de crear uno nuevo. Desde el ángulo metodológico, la Sprint Retrospectiva es el momento en que el equipo examina sus propios procesos; Schwaber y Sutherland (2020) la describen como la oportunidad de identificar mejoras concretas para el siguiente sprint. Cohn (2005) añade que la velocidad —puntos de historia completados por sprint— es la métrica que hace predecible la planificación futura.

### 3.2 Planteamiento del problema

El sistema ya permite crear productos, pero no corregir un nombre mal escrito ni retirar un producto descontinuado. ¿Cómo implementar edición y eliminación de forma segura, evitando que una URL mal escrita borre datos por error, y cómo formalizar el cierre del Sprint 2 para que el equipo arranque el Sprint 3 con un plan claro?

### 3.3 Justificación

`get_object_or_404` simplifica el código y mejora la seguridad: cualquier intento de editar o eliminar un producto que no existe devuelve 404 en lugar de un error 500 (Django Software Foundation, s.f.). La página de confirmación del borrado aplica el principio de *diseño defensivo*: toda operación destructiva requiere una confirmación explícita del usuario. La Retrospectiva formaliza el mismo principio en el equipo: antes de avanzar, revisar qué mejorar (Schwaber y Sutherland, 2020).

### 3.4 Objetivos

**General:** Que el estudiante complete el CRUD con edición y eliminación, use `get_object_or_404` y cierre el Sprint 2 con Review, Retrospectiva y velocidad calculada.

**Específicos:**
1. Implementar `editar_producto` con `instance=` para pre-poblar el `ModelForm` (S1).
2. Implementar `eliminar_producto` con confirmación GET + borrado en POST (S1).
3. Sustituir `try/except DoesNotExist` por `get_object_or_404` en todas las vistas (S1).
4. Añadir enlaces editar/eliminar en las plantillas de lista y detalle (S1).
5. Realizar el Sprint 2 Review + Retrospectiva + calcular velocidad (S2).

### 3.5 Marco teórico (con código)

**`get_object_or_404`: el atajo limpio.** La documentación oficial de Django (Django Software Foundation, s.f.) define este atajo como equivalente a `objects.get()` + `raise Http404` si no existe. Convierte tres líneas en una:

```python
# Semana 4–5: try/except largo
try:
    producto = Producto.objects.get(pk=producto_id)
except Producto.DoesNotExist:
    return HttpResponse("No encontrado", status=404)

# Semana 6: get_object_or_404 → misma lógica, una sola línea
from django.shortcuts import get_object_or_404
producto = get_object_or_404(Producto, pk=producto_id)
# Si no existe → lanza Http404 → Django lo convierte en 404 automáticamente
```

**`instance=`: editar en lugar de crear.** El parámetro `instance` indica a `ModelForm` que trabaje sobre un objeto existente. Sin él, `form.save()` crea un registro nuevo; con él, actualiza el existente (Django Software Foundation, s.f.):

```python
# Sin instance → CREA un nuevo Producto en cada POST
form = ProductoForm(request.POST)

# Con instance → ACTUALIZA el Producto existente en cada POST
producto = get_object_or_404(Producto, pk=producto_id)
form = ProductoForm(request.POST, instance=producto)

# En el GET, instance pre-puebla el formulario con los datos actuales:
form = ProductoForm(instance=producto)
# Verificacion: el campo "nombre" en el form ya contiene "Teclado USB"
```

**Patrón de eliminación con confirmación.** Los navegadores no emiten peticiones HTTP DELETE; Django usa POST para operaciones destructivas. El patrón GET/POST de confirmación protege contra borrados accidentales:

```
GET  /productos/3/eliminar/  →  página "¿Eliminar Monitor 24in?" + botón POST
POST /productos/3/eliminar/  →  producto.delete() → redirect a lista
```

```python
def eliminar_producto(request, producto_id):
    """GET: confirmacion. POST: borrado."""
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == "POST":
        producto.delete()                          # borra de la BD
        return redirect("productos:lista")
    return render(request, "productos/eliminar.html", {"producto": producto})

# Verificaciones esperadas:
# GET  → status 200, contiene nombre del producto y "no se puede deshacer"
# POST → status 302, producto.objects.filter(pk=id).exists() == False
```

**Velocidad del equipo en Scrum.** Cohn (2005) define la velocidad como los puntos de historia completados en un sprint. Con ella, el equipo puede comprometerse realistamente en el siguiente sprint:

| Sprint | Semanas | Puntos completados |
|---|---|---|
| Sprint 0 (setup) | 1–2 | — |
| Sprint 1 (views + templates) | 3 | HU-01(2) + HU-01a(2) = **4 pts** |
| Sprint 2 (DB + CRUD) | 4–6 | HU-BD(3) + HU-02(2) + HU-03(5) + HU-04(5) = **15 pts** |
| Velocidad promedio | — | **≈10 pts/sprint** |

> Sprint 3 (autenticación + vistas basadas en clases): planear máximo ~10 pts.

### 3.6 Metodología

Trabajo guiado e individual. La sesión implementa `editar_producto` → `eliminar_producto` → `get_object_or_404` en todas las vistas → enlaces en plantillas → verificación de las 9 aserciones. En paralelo, se realiza el Sprint 2 Review formal y la Retrospectiva.

### 3.7 Desarrollo temático

**S1 — Frameworks (≈9 h reportadas)**
1. `get_object_or_404`: qué hace, por qué reemplaza `try/except DoesNotExist`.
2. `instance=` en `ModelForm`: diferencia entre crear y actualizar.
3. Vista `editar_producto`: GET pre-poblado + POST con `instance`.
4. Vista `eliminar_producto`: patrón GET (confirmación) + POST (borrado).
5. Actualizar plantillas: enlaces editar/eliminar en lista y detalle.

**S2 — Metodologías ágiles (≈8 h reportadas)**
1. Sprint 2 Review: demostrar CRUD completo al "Product Owner" (docente).
2. Sprint 2 Retrospectiva: ¿qué salió bien? ¿qué mejorar? ¿qué acción concreta?
3. Velocidad: calcular puntos completados por sprint.
4. Sprint 3 Planning inicial: autenticación + CBV, estimación a partir de la velocidad.

### 3.8 Práctica de laboratorio

**Objetivo:** completar el CRUD con edición y eliminación, refactorizar a `get_object_or_404` y documentar el cierre del Sprint 2.

---

#### PASO 1 — Actualizar `productos/views.py`

```python
"""Vistas de la aplicacion productos — Semana 6.

Agrega editar_producto y eliminar_producto.
Refactoriza todas las vistas a get_object_or_404.
Hilo conector: "Ciclo cerrado".
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductoForm
from .models import Producto


def bienvenida(request: HttpRequest) -> HttpResponse:
    """Devuelve la pagina principal del sistema."""
    return render(request, "base.html", {"titulo": "Bienvenido"})


def lista_productos(request: HttpRequest) -> HttpResponse:
    """Devuelve todos los productos desde la base de datos."""
    productos = Producto.objects.all()
    return render(request, "productos/lista.html", {"productos": productos})


def detalle_producto(request: HttpRequest, producto_id: int) -> HttpResponse:
    """Devuelve el detalle de un producto — refactorizado a get_object_or_404."""
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, "productos/detalle.html", {"producto": producto})


def crear_producto(request: HttpRequest) -> HttpResponse:
    """Muestra y procesa el formulario de creacion."""
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos:lista")
    else:
        form = ProductoForm()
    return render(request, "productos/crear.html", {"form": form})


def editar_producto(request: HttpRequest, producto_id: int) -> HttpResponse:
    """Muestra y procesa el formulario de edicion de un producto.

    GET  → formulario pre-poblado con los datos actuales del producto.
    POST → valida, guarda los cambios y redirige a la lista.

    Args:
        request: Objeto HttpRequest generado por Django.
        producto_id: Clave primaria del producto a editar.

    Returns:
        HttpResponse con formulario pre-poblado (200),
        HttpResponseRedirect tras guardar (302),
        o Http404 si el producto no existe.
    """
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)   # ← instance!
        if form.is_valid():
            form.save()
            return redirect("productos:lista")
    else:
        form = ProductoForm(instance=producto)                 # ← pre-poblar
    return render(
        request,
        "productos/editar.html",
        {"form": form, "producto": producto},
    )


def eliminar_producto(request: HttpRequest, producto_id: int) -> HttpResponse:
    """Muestra confirmacion de eliminacion y procesa el borrado.

    GET  → pagina de confirmacion con el nombre del producto.
    POST → elimina el producto de la BD y redirige a la lista.

    Args:
        request: Objeto HttpRequest generado por Django.
        producto_id: Clave primaria del producto a eliminar.

    Returns:
        HttpResponse con pagina de confirmacion (200),
        HttpResponseRedirect tras eliminar (302),
        o Http404 si el producto no existe.
    """
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == "POST":
        producto.delete()
        return redirect("productos:lista")
    return render(
        request,
        "productos/eliminar.html",
        {"producto": producto},
    )
```

---

#### PASO 2 — Actualizar `productos/urls.py`

```python
"""URLs de la aplicacion productos — Semana 6 (CRUD completo)."""

from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path("",                                      views.bienvenida,       name="bienvenida"),
    path("productos/",                            views.lista_productos,  name="lista"),
    path("productos/nuevo/",                      views.crear_producto,   name="crear"),
    path("productos/<int:producto_id>/",          views.detalle_producto, name="detalle"),
    path("productos/<int:producto_id>/editar/",   views.editar_producto,  name="editar"),
    path("productos/<int:producto_id>/eliminar/", views.eliminar_producto,name="eliminar"),
]
```

---

#### PASO 3 — Crear `productos/templates/productos/editar.html`

```html
{% extends "base.html" %}

{% block title %}Editar: {{ producto.nombre }}{% endblock %}

{% block content %}
<h2>Editar: {{ producto.nombre }}</h2>

{% if form.errors %}
<ul>
{% for campo, errores in form.errors.items %}
    <li><em>{{ campo }}</em>: {{ errores|join:", " }}</li>
{% endfor %}
</ul>
{% endif %}

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Guardar cambios</button>
</form>
<p><a href="/productos/">Cancelar</a></p>
{% endblock %}
```

---

#### PASO 4 — Crear `productos/templates/productos/eliminar.html`

```html
{% extends "base.html" %}

{% block title %}Eliminar: {{ producto.nombre }}{% endblock %}

{% block content %}
<h2>¿Eliminar "{{ producto.nombre }}"?</h2>
<p><strong>Esta acción no se puede deshacer.</strong></p>
<p>Precio: ${{ producto.precio }} | Stock: {{ producto.stock }}</p>

<form method="post">
    {% csrf_token %}
    <button type="submit">Sí, eliminar</button>
</form>
<p><a href="/productos/">Cancelar</a></p>
{% endblock %}
```

---

#### PASO 5 — Actualizar `lista.html` y `detalle.html` con enlaces

En `lista.html`, añadir dentro del `{% for p in productos %}`:
```html
| <a href="/productos/{{ p.pk }}/editar/">Editar</a>
| <a href="/productos/{{ p.pk }}/eliminar/">Eliminar</a>
```

En `detalle.html`, añadir debajo del stock:
```html
<a href="/productos/{{ producto.pk }}/editar/">Editar</a> |
<a href="/productos/{{ producto.pk }}/eliminar/">Eliminar</a> |
<a href="/productos/">← Lista</a>
```

---

#### PASO 6 — Verificar

```bash
python3 manage.py check
# Verificacion esperada: "System check identified no issues (0 silenced)."

python3 manage.py runserver
# Probar en el navegador:
#   GET  /productos/1/editar/    → form pre-poblado con datos actuales
#   POST /productos/1/editar/    → datos actualizados + redirect a lista
#   GET  /productos/2/eliminar/  → página de confirmación con nombre
#   POST /productos/2/eliminar/  → producto eliminado + redirect a lista
#   GET  /productos/999/editar/  → 404 Not Found
```

---

#### PASO 7 — Sprint 2 Retrospectiva + Sprint 3 Planning (S2)

Crea `sprint2_retrospective.md` en la raíz del proyecto:

```markdown
# Sprint 2 Retrospective — Sistema de Inventario
## Fecha: ___________

### Sprint Goal verificado
"El administrador puede gestionar productos (crear, editar, eliminar)
desde el panel admin y formularios propios, con datos en la base de datos."
✅ Sprint Goal cumplido.

### Incremento entregado
| Historia | Puntos | Estado |
|---|---|---|
| HU-BD  Modelo + ORM + migraciones | 3 | ✅ Done |
| HU-02  Panel admin CRUD           | 2 | ✅ Done |
| HU-03  Formulario crear           | 5 | ✅ Done |
| HU-04  Formulario editar/eliminar | 5 | ✅ Done |
| **Total Sprint 2**                | **15** | |

### Velocidad del equipo
Sprint 1: 4 pts | Sprint 2: 15 pts | Promedio: ~10 pts/sprint

### ¿Qué salió bien?
- ModelForm redujo el código: un archivo forms.py para crear y editar.
- El panel admin fue útil para poblar datos de prueba rápidamente.

### ¿Qué mejorar?
- Orden de URL patterns causó confusión (nuevo/ vs <int:>/).
- Las pruebas con RequestFactory no capturan Http404 directamente.

### Acción concreta para Sprint 3
Documentar el orden de URLs como estándar del proyecto desde el inicio.

### Sprint 3 — Preview (Semana 8)
Sprint Goal: "Los usuarios deben autenticarse para gestionar productos."
Historias candidatas:
  HU-05  Login/logout                     5 pts
  HU-06  Proteger vistas con @login_required  3 pts
  HU-07  Vistas basadas en clases (CBV)   5 pts
Capacidad estimada: ~10 pts
```

---

#### Entregables — Sprint 2 cerrado

```bash
git add productos/views.py productos/urls.py
git add productos/templates/productos/editar.html
git add productos/templates/productos/eliminar.html
git add sprint2_retrospective.md
git commit -m "Sprint 2 completo: CRUD editar/eliminar + get_object_or_404"
git push origin sprint2/modelos-orm

# Cerrar el Sprint 2: merge a main
git checkout main
git merge sprint2/modelos-orm
git push origin main
```

> **Fallback sin conexión:** omite los `push`. El merge local es válido.

---

### 3.9 Análisis (5 preguntas de reflexión)

1. ¿Por qué `get_object_or_404(Producto, pk=99)` es más limpio que `try: Producto.objects.get(pk=99) except DoesNotExist`? ¿Cuándo NO usarías `get_object_or_404`?
2. ¿Qué pasaría si en `editar_producto` omitieras el parámetro `instance=producto` en el POST? ¿Cuántos productos habría en la BD después de guardar?
3. ¿Por qué la eliminación requiere una página de confirmación (GET) antes del POST? ¿Qué ataque o accidente previene?
4. La velocidad del equipo en el Sprint 2 fue de 15 puntos. ¿Cuántas historias de 5 puntos podrías comprometer en el Sprint 3 si la velocidad promedio es ~10 pts?
5. Compara la Retrospectiva del sprint (qué mejorar para el siguiente) con la sección `{% if form.errors %}` de la plantilla (qué corregir antes de guardar). ¿Qué función comparten?

### 3.10 Conclusiones

Esta semana el sistema de inventario alcanzó su primera versión completa: cualquier usuario puede **crear, leer, editar y eliminar** productos desde una interfaz web propia, sin tocar el panel admin. `get_object_or_404` simplificó el código de todas las vistas; `instance=` demostró que `ModelForm` sirve tanto para crear como para actualizar. El Sprint 2 cerrado con Review y Retrospectiva documenta la velocidad del equipo —15 puntos en 3 semanas— y establece el punto de partida realista para el Sprint 3: autenticación y vistas basadas en clases.

---

## 4. PARTE II — Momentos didácticos (Sergio Tobón)

### 4.1 Momento 1 — Apertura
Planteamiento: "el inventario tiene un producto con nombre incorrecto — ¿cómo lo corregimos sin usar el admin?". Demo del docente: mostrar `instance=` con un objeto existente en el shell de Django. Introducir la Sprint Retrospectiva con la pregunta "¿qué hicimos bien y qué haríamos diferente?".

### 4.2 Momento 2 — Desarrollo
Codificación guiada de `editar_producto` (GET pre-poblado + POST con `instance=`) → `eliminar_producto` (confirmación + borrado) → refactorizar todas las vistas a `get_object_or_404` → actualizar plantillas con enlaces → verificar las 9 aserciones. En paralelo, redactar la Retrospectiva y calcular velocidad.

### 4.3 Momento 3 — Cierre
Sprint 2 Review formal con el docente como Product Owner. Merge a `main`, commit final, subida a Classroom y respuestas de análisis.

---

## 5. Estrategia de evaluación de la semana

| Evidencia | Submódulo | Instrumento | Ponderación |
|---|---|---|---|
| `editar_producto`: GET pre-poblado (200) + POST válido (302, BD actualizada) + inválido (200, sin cambios) | S1 | Rúbrica de vista (instance= correcto) | 25 % |
| `eliminar_producto`: GET confirmación (200) + POST borrado (302, BD limpia) + 404 correcto | S1 | Lista de cotejo | 20 % |
| `get_object_or_404` en todas las vistas; enlaces en lista y detalle | S1 | Verificación directa | 10 % |
| `sprint2_retrospective.md`: velocidad + qué mejorar + Sprint 3 preview | S2 | Lista de cotejo | 30 % |
| Respuestas de análisis (5 preguntas) | Transversal | Lista de cotejo | 15 % |

---

## 6. Recursos didácticos

- Proyecto Django de la Semana 5 en rama `sprint2/modelos-orm`.
- Computadora con Python 3.11+, Django 4.2 y VS Code.
- Navegador web para verificar editar/eliminar.
- GitHub Projects para cerrar HU-04 y actualizar el Kanban.
- Google Classroom para entrega de evidencias.

---

## 7. Referencias (APA 7)

Cohn, M. (2005). *Agile estimating and planning*. Prentice Hall.

Django Software Foundation. (s.f.). *Shortcut functions: get_object_or_404*. https://docs.djangoproject.com/en/4.2/topics/http/shortcuts/#get-object-or-404

Django Software Foundation. (s.f.). *Deleting objects*. https://docs.djangoproject.com/en/4.2/topics/db/queries/#deleting-objects

Django Software Foundation. (s.f.). *Creating forms from models: instance*. https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/#the-save-method

Schwaber, K., & Sutherland, J. (2020). *La guía de Scrum*. https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf

---

*Guía generada bajo ROL 2 — Asesor Académico Experto · Prompt Maestro v1.0 · Una semana a la vez.*
*Parámetros respetados: 13 semanas · submódulos y horas SEP sin modificar · cita narrativa.*
*Código verificado: 9 aserciones (GET editar pre-poblado · POST editar válido 302+BD · POST editar inválido · editar 404 · GET eliminar confirmación · POST eliminar 302+borrado · eliminar 404 · lista con enlaces · CRUD completo Create/Read/Update/Delete).*
