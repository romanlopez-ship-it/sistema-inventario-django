# Módulo II · Semana 5 — Guía Académica y de Laboratorio
## Técnico en Programación (SEP 3061300006-23) · UTEC Celaya
### Asesor: MC. Román Fernando López González

---

## 1. Identificación de la semana

| Campo | Detalle |
|---|---|
| Carrera | Técnico en Programación |
| Módulo | II — Desarrolla software con herramientas orientadas a la productividad (272 h) |
| Semana | 5 de 13 |
| Submódulos integrados | S1 Frameworks (144 h) · S2 Metodologías ágiles (128 h) |
| **Hilo conector de la semana** | **"El primer incremento funcional"** |
| Stack | Django 4.2 LTS · `ModelForm` · CSRF · Python 3.11+ |
| Carga horaria reportada | 17 h/semana (S1 = 9 h · S2 = 8 h) |
| Carga horaria real (planeación) | 14.16 h/semana |
| Tiempo fantasma máximo | 15 min/día |
| Plataforma institucional | Google Classroom |
| Prerrequisito | Semana 4 — modelo `Producto` + admin + vistas con ORM en rama `sprint2/modelos-orm` |

> **Hilo conector:** el `ModelForm` es el primer punto de contacto real entre el usuario y la base de datos —sin pasar por el admin—. El patrón GET/POST del formulario refleja el ciclo de inspección y adaptación del Daily Scrum: GET muestra el estado actual (formulario vacío = comienzo del día), POST válido avanza (producto guardado = tarea completada), POST inválido expone impedimentos (errores de validación = obstáculos del sprint). Esta semana el estudiante entrega el **primer incremento funcional** que un usuario real puede operar.

---

## 2. Competencias de la semana

**Resultado de aprendizaje (SEP):**
El estudiante implementa un formulario de creación de productos con `ModelForm`, gestiona el ciclo GET/POST y la protección CSRF; en paralelo, practica el Daily Scrum documentando un registro diario de avance e impedimentos del Sprint 2.

**Actividades clave de la competencia laboral:**

- **S1 — Frameworks:** Crea `forms.py` con `ProductoForm(ModelForm)`; implementa la vista `crear_producto` con manejo GET/POST; configura `{% csrf_token %}` y muestra errores de validación; actualiza URLs respetando el orden de patrones.
- **S2 — Metodologías ágiles:** Practica el Daily Scrum con las 3 preguntas; documenta un log de impedimentos; actualiza el Kanban moviendo HU-03 a "In Progress".

---

## 3. PARTE I — Estructura académica (modelo Corina Schmelkes)

### 3.1 Introducción

Hasta la Semana 4, la única forma de crear productos era el panel admin —una herramienta para administradores, no para usuarios finales—. La documentación oficial de Django (Django Software Foundation, s.f.) define el `ModelForm` como un mecanismo que genera automáticamente campos de formulario HTML a partir de la definición del modelo, heredando sus tipos y validaciones. Esto elimina la duplicación: el desarrollador define los tipos una sola vez en `models.py` y el formulario los reutiliza. Por el lado metodológico, Schwaber y Sutherland (2020) describen el Daily Scrum como un evento de 15 minutos en el que el equipo inspecciona el progreso hacia el Sprint Goal y adapta el plan del día. Esta semana, el patrón GET/POST del formulario y el Daily Scrum comparten la misma estructura lógica: inspeccionar el estado actual y actuar sobre él.

### 3.2 Planteamiento del problema

El administrador puede crear productos desde el panel admin, pero un usuario del sistema no tiene acceso a `/admin/`. ¿Cómo construir un formulario propio que valide los datos, los guarde en la base de datos y notifique al usuario si hay errores, sin repetir las reglas de validación que ya están en el modelo?

### 3.3 Justificación

El `ModelForm` resuelve exactamente ese problema: hereda los tipos y restricciones del modelo (`max_length`, `decimal_places`, `default`) y los traduce automáticamente en validación HTML y Python (Django Software Foundation, s.f.). El resultado es que el estudiante escribe menos código y comete menos errores de inconsistencia. En el plano ágil, Cohn (2005) señala que el Daily Scrum no es una reunión de reporte al Scrum Master, sino una herramienta del equipo para sincronizarse: el "impedimento" identificado en el standup es exactamente el equivalente al `form.errors` que la vista devuelve al usuario cuando algo no está bien.

### 3.4 Objetivos

**General:** Que el estudiante implemente un formulario de creación con `ModelForm` respetando el ciclo GET/POST y la protección CSRF, y documente tres Daily Scrums del Sprint 2.

**Específicos:**
1. Crear `forms.py` con `ProductoForm(ModelForm)` vinculado al modelo (S1).
2. Implementar `crear_producto` con ciclo GET → form vacío / POST válido → guardar + redirect / POST inválido → form con errores (S1).
3. Agregar `{% csrf_token %}` y mostrar `form.errors` en la plantilla (S1).
4. Respetar el orden de URL patterns para evitar conflicto con `<int:producto_id>` (S1).
5. Documentar tres Daily Scrums y un log de impedimentos del Sprint 2 (S2).

### 3.5 Marco teórico (con código)

**`ModelForm`: herencia desde el modelo.** La documentación oficial de Django (Django Software Foundation, s.f.) explica que `ModelForm` lee la clase `Meta` del formulario para saber qué modelo usar y qué campos exponer. Los campos excluidos (como `creado`, que se asigna automáticamente) no aparecen en el formulario:

```python
# forms.py — ModelForm hereda tipos del modelo
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model  = Producto
        fields = ["nombre", "precio", "stock"]
        # "creado" no está en fields → no aparece en el formulario

# Verificacion esperada:
# ProductoForm().fields.keys() → ["nombre", "precio", "stock"]
# "creado" not in ProductoForm().fields  → True
```

**El ciclo GET/POST: el patrón fundamental del web.** Toda vista que maneja un formulario sigue la misma estructura:

```
Navegador          Django
   │─── GET ────►  vista: form = ProductoForm()         → 200 form vacío
   │◄── 200 ─────  render("crear.html", {"form": form})
   │
   │─── POST ───►  vista: form = ProductoForm(request.POST)
   │               if form.is_valid():
   │                   form.save()              ← guarda en BD
   │◄── 302 ─────      return redirect(lista)  ← Post-Redirect-Get
   │               else:
   │◄── 200 ─────      render("crear.html", {"form": form}) ← errores
```

```python
def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos:lista")
    else:
        form = ProductoForm()
    return render(request, "productos/crear.html", {"form": form})

# Verificacion esperada:
# GET  → status 200, contiene "Nuevo producto" y "csrf"
# POST válido   → status 302, producto guardado en BD
# POST inválido → status 200, errores en respuesta, nada guardado
```

**Protección CSRF.** La documentación oficial de Django (Django Software Foundation, s.f.) describe CSRF (*Cross-Site Request Forgery*) como un ataque en el que un sitio malicioso envía peticiones POST en nombre del usuario. `{% csrf_token %}` inserta un token secreto en el formulario que Django verifica antes de procesar el POST:

```html
<form method="post">
    {% csrf_token %}        ← OBLIGATORIO en todo formulario POST
    {{ form.as_p }}
    <button type="submit">Guardar</button>
</form>
```

**Orden de URL patterns — gotcha crítico.** Django evalúa los patrones de URL en orden. Si `<int:producto_id>` aparece antes que `nuevo/`, Django intentará convertir "nuevo" a entero y fallará:

```python
# ✗ INCORRECTO — Django intenta convertir "nuevo" a int → error
urlpatterns = [
    path("productos/<int:producto_id>/", ...),  # ← primero
    path("productos/nuevo/", ...),              # ← nunca llega aquí
]

# ✓ CORRECTO — la ruta específica va ANTES que el parámetro
urlpatterns = [
    path("productos/",                   ..., name="lista"),
    path("productos/nuevo/",             ..., name="crear"),    # ← primero
    path("productos/<int:producto_id>/", ..., name="detalle"),  # ← después
]
```

**Daily Scrum: 3 preguntas, 15 minutos.** Schwaber y Sutherland (2020) establecen que cada miembro del equipo responde: ¿qué hice ayer para acercarme al Sprint Goal? ¿qué haré hoy? ¿hay algún impedimento? El resultado no es un reporte al Scrum Master, sino un plan compartido de 24 horas.

### 3.6 Metodología

Trabajo guiado e individual con computadora por alumno. La sesión crea `forms.py`, implementa la vista `crear_producto`, configura la plantilla y las URLs en el orden correcto, y verifica el ciclo completo. En paralelo, cada estudiante documenta tres Daily Scrums y un log de impedimentos.

### 3.7 Desarrollo temático

**S1 — Frameworks (≈9 h reportadas)**
1. `ModelForm`: herencia de tipos desde el modelo, clase `Meta`, `fields` y `labels`.
2. Vista `crear_producto`: ciclo GET/POST, `is_valid()`, `save()`, `redirect()`.
3. Protección CSRF: qué es, por qué es obligatoria, `{% csrf_token %}`.
4. Mostrar errores: `form.errors`, `{{ form.as_p }}`, errores por campo.
5. Orden de URL patterns: rutas específicas antes de rutas con parámetros.

**S2 — Metodologías ágiles (≈8 h reportadas)**
1. Daily Scrum: las 3 preguntas; duración máxima 15 min; quién habla y quién escucha.
2. Impediment log: qué es un impedimento, cómo se documenta, quién lo resuelve.
3. Kanban: mover HU-02 a "Done" y HU-03 a "In Progress".
4. Sprint velocity: puntos completados vs. puntos comprometidos.

### 3.8 Práctica de laboratorio

**Objetivo:** implementar el formulario de creación de productos, verificar el ciclo GET/POST y documentar tres Daily Scrums del Sprint 2.

---

#### PASO 1 — Crear `productos/forms.py` (archivo nuevo)

```python
"""Formularios de la aplicacion productos — Semana 5.

Define ProductoForm como ModelForm vinculado al modelo Producto.
Hilo conector: "El primer incremento funcional".
"""

from django import forms

from .models import Producto


class ProductoForm(forms.ModelForm):
    """Formulario de creacion de productos.

    Genera automaticamente campos HTML a partir del modelo Producto.
    Valida tipos, longitudes y campos requeridos antes de guardar.

    Attributes:
        Meta.model: Modelo de origen de los campos.
        Meta.fields: Campos expuestos al usuario (excluye 'creado').
        Meta.labels: Etiquetas visibles en el formulario.
    """

    class Meta:
        model  = Producto
        fields = ["nombre", "precio", "stock"]
        labels = {
            "nombre": "Nombre del producto",
            "precio": "Precio unitario ($)",
            "stock":  "Unidades en stock",
        }
```

---

#### PASO 2 — Actualizar `productos/views.py` (agregar `crear_producto`)

```python
"""Vistas de la aplicacion productos — Semana 5.

Agrega la vista crear_producto con ModelForm y ciclo GET/POST.
Hilo conector: "El primer incremento funcional".
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

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
    """Devuelve el detalle de un producto por su clave primaria."""
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        return HttpResponse(
            f"<h1>Producto {producto_id} no encontrado</h1>",
            status=404,
        )
    return render(request, "productos/detalle.html", {"producto": producto})


def crear_producto(request: HttpRequest) -> HttpResponse:
    """Muestra y procesa el formulario de creacion de productos.

    GET  → devuelve el formulario vacio.
    POST → valida y guarda el producto; redirige a la lista si es valido,
           o devuelve el formulario con errores si no lo es.

    Args:
        request: Objeto HttpRequest generado por Django.

    Returns:
        HttpResponse con el formulario (GET o POST invalido),
        o HttpResponseRedirect a la lista (POST valido, status 302).
    """
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos:lista")
    else:
        form = ProductoForm()

    return render(request, "productos/crear.html", {"form": form})
```

---

#### PASO 3 — Crear `productos/templates/productos/crear.html`

```html
{% extends "base.html" %}

{% block title %}Nuevo producto{% endblock %}

{% block content %}
<h2>Nuevo producto</h2>

{% if form.errors %}
<div>
    <strong>Corrige los siguientes errores:</strong>
    <ul>
    {% for campo, errores in form.errors.items %}
        <li><em>{{ campo }}</em>: {{ errores|join:", " }}</li>
    {% endfor %}
    </ul>
</div>
{% endif %}

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Guardar producto</button>
</form>
<p><a href="/productos/">Cancelar</a></p>
{% endblock %}
```

---

#### PASO 4 — Actualizar `productos/urls.py` (orden correcto)

```python
"""URLs de la aplicacion productos — Semana 5.

IMPORTANTE: 'nuevo/' debe declararse ANTES de '<int:producto_id>/'
para evitar que Django intente convertir "nuevo" a entero.
"""

from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path("",                             views.bienvenida,      name="bienvenida"),
    path("productos/",                   views.lista_productos, name="lista"),
    path("productos/nuevo/",             views.crear_producto,  name="crear"),   # ← antes
    path("productos/<int:producto_id>/", views.detalle_producto,name="detalle"), # ← después
]
```

---

#### PASO 5 — Actualizar `base.html` (agregar enlace "+ Nuevo")

```html
<nav>
    <a href="/">Inicio</a> |
    <a href="/productos/">Productos</a> |
    <a href="/productos/nuevo/">+ Nuevo producto</a>
</nav>
```

---

#### PASO 6 — Verificar el ciclo completo

```bash
python3 manage.py check
# Verificacion esperada: "System check identified no issues (0 silenced)."

python3 manage.py runserver
# Probar en el navegador:
#   GET  /productos/nuevo/           → formulario vacío con 3 campos
#   POST con datos válidos           → status 302, producto en /productos/
#   POST con nombre vacío            → status 200, error en campo "nombre"
#   POST con precio "abc"            → status 200, error en campo "precio"
```

---

#### PASO 7 — Daily Scrum log (S2)

Crea `daily_scrum_log.md` en la raíz del proyecto:

```markdown
# Daily Scrum Log — Sprint 2
## Sistema de Inventario

### Martes (Semana 5)
| Pregunta | Respuesta |
|---|---|
| ¿Qué hice ayer? | Creé models.py, ejecuté migraciones y registré el admin |
| ¿Qué haré hoy? | Implementar forms.py y la vista crear_producto |
| ¿Impedimentos? | Sí: error al configurar el orden de URL patterns |
**Resolución del impedimento:** colocar `nuevo/` antes de `<int:producto_id>/`

### Miércoles (Semana 5)
| Pregunta | Respuesta |
|---|---|
| ¿Qué hice ayer? | Implementé forms.py y la vista con ciclo GET/POST |
| ¿Qué haré hoy? | Agregar {% csrf_token %} y mostrar errores en la plantilla |
| ¿Impedimentos? | No |

### Jueves (Semana 5)
| Pregunta | Respuesta |
|---|---|
| ¿Qué hice ayer? | Completé crear.html con errores y csrf |
| ¿Qué haré hoy? | Verificar las 8 aserciones y actualizar el Kanban |
| ¿Impedimentos? | No |

## Actualización del Kanban
- HU-02 (panel admin): ✅ Done
- HU-03 (formulario crear): 🔄 In Progress → completado esta semana
```

---

#### Entregables — Sprint 2 avanza

```bash
git add productos/forms.py productos/views.py
git add productos/urls.py productos/templates/productos/crear.html
git add templates/base.html daily_scrum_log.md
git commit -m "Sprint 2: ModelForm crear_producto + Daily Scrum log"
git push origin sprint2/modelos-orm
```

> **Fallback sin conexión:** omite `git push`. El commit local es válido.

---

### 3.9 Análisis (5 preguntas de reflexión)

1. ¿Por qué `crear_producto` devuelve status 302 en el POST válido y 200 en el inválido? ¿Qué problema evita el patrón Post-Redirect-Get?
2. Si añades un campo `activo = models.BooleanField(default=True)` al modelo, ¿qué cambios necesitarías hacer en `forms.py` para que aparezca en el formulario?
3. ¿Qué pasaría si omites `{% csrf_token %}` en el formulario y envías el POST?
4. Compara el ciclo GET/POST del formulario con el ciclo Daily Scrum: ¿en qué se parecen la validación de errores y la gestión de impedimentos?
5. En el `daily_scrum_log.md`, ¿el impedimento que documentaste fue técnico o de proceso? ¿Quién lo resolvió y cómo?

### 3.10 Conclusiones

Con el formulario de creación funcionando, el sistema de inventario ya tiene su primer incremento funcional real: un usuario puede registrar productos sin tocar el panel admin. El `ModelForm` demostró una de las ideas centrales del módulo —la **productividad**—: una sola clase en `forms.py` genera campos, validaciones y mensajes de error automáticamente, reutilizando lo que el modelo ya define. El Daily Scrum log documenta cómo el equipo navega los obstáculos técnicos semana a semana, convirtiendo cada impedimento en una lección aprendida.

---

## 4. PARTE II — Momentos didácticos (Sergio Tobón)

### 4.1 Momento 1 — Apertura
Planteamiento del problema: "¿puede un usuario que no es admin registrar un producto?". Demo del docente: mostrar que `/admin/` requiere contraseña y que el sistema necesita una ruta propia. Introducir `ModelForm` y el ciclo GET/POST con el diagrama del pizarrón.

### 4.2 Momento 2 — Desarrollo
Creación guiada de `forms.py` → vista `crear_producto` → plantilla `crear.html` → actualización de URLs en orden correcto → verificación del ciclo completo en el navegador. En paralelo, cada estudiante completa su primer Daily Scrum del sprint.

### 4.3 Momento 3 — Cierre
Verificación de las 8 aserciones, documentación del `daily_scrum_log.md`, commit, subida a Classroom y respuesta a las preguntas de análisis.

---

## 5. Estrategia de evaluación de la semana

| Evidencia | Submódulo | Instrumento | Ponderación |
|---|---|---|---|
| `forms.py` con `ProductoForm`: 3 campos, sin `creado`, labels correctos | S1 | Rúbrica de formulario | 25 % |
| Vista `crear_producto`: GET(200) + POST válido(302+BD) + POST inválido(200+errores) | S1 | Lista de cotejo técnica | 25 % |
| `crear.html` con `{% csrf_token %}` y `form.errors` | S1 | Verificación directa | 10 % |
| URLs en orden correcto (`nuevo/` antes de `<int:>`) | S1 | Verificación en `urls.py` | 10 % |
| `daily_scrum_log.md`: 3 días + ≥1 impedimento documentado + Kanban actualizado | S2 | Lista de cotejo | 20 % |
| Respuestas de análisis (5 preguntas) | Transversal | Lista de cotejo | 10 % |

---

## 6. Recursos didácticos

- Proyecto Django de la Semana 4 en rama `sprint2/modelos-orm`.
- Computadora con Python 3.11+, Django 4.2 y VS Code.
- Navegador web para probar el ciclo GET/POST.
- GitHub Projects para actualizar el Kanban.
- Google Classroom para entrega de evidencias.

---

## 7. Referencias (APA 7)

Cohn, M. (2005). *Agile estimating and planning*. Prentice Hall.

Django Software Foundation. (s.f.). *Working with forms*. https://docs.djangoproject.com/en/4.2/topics/forms/

Django Software Foundation. (s.f.). *Creating forms from models (ModelForm)*. https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/

Django Software Foundation. (s.f.). *Cross Site Request Forgery protection*. https://docs.djangoproject.com/en/4.2/ref/csrf/

Schwaber, K., & Sutherland, J. (2020). *La guía de Scrum*. https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf

---

*Guía generada bajo ROL 2 — Asesor Académico Experto · Prompt Maestro v1.0 · Una semana a la vez.*
*Parámetros respetados: 13 semanas · submódulos y horas SEP sin modificar · cita narrativa.*
*Código verificado: 8 aserciones (form vacío 3 campos / form válido / form inválido con errores / GET 200 con csrf / POST válido 302 + BD / POST inválido 200 sin guardar / lista refleja nuevo / labels correctos).*
