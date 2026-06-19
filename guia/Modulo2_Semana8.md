# Módulo II · Semana 8 — Guía Académica y de Laboratorio
## Técnico en Programación (SEP 3061300006-23) · UTEC Celaya
### Asesor: MC. Román Fernando López González

---

## 1. Identificación de la semana

| Campo | Detalle |
|---|---|
| Carrera | Técnico en Programación |
| Módulo | II — Desarrolla software con herramientas orientadas a la productividad (272 h) |
| Semana | 8 de 13 |
| Submódulos integrados | S1 Frameworks (144 h) · S2 Metodologías ágiles (128 h) |
| **Hilo conector de la semana** | **"Usuarios reales"** |
| Stack | Django 4.2 · `django.contrib.auth` · `@login_required` · Python 3.11+ |
| Carga horaria reportada | 17 h/semana (S1 = 9 h · S2 = 8 h) |
| Carga horaria real (planeación) | 14.16 h/semana |
| Tiempo fantasma máximo | 15 min/día |
| Plataforma institucional | Google Classroom |
| Prerrequisito | Evaluación intermedia superada (Semana 7) · CRUD completo en `main` |

> **Hilo conector:** hasta la Semana 7, cualquier visitante podía crear, editar y eliminar productos. Esta semana el sistema adquiere **usuarios reales**: solo los autenticados modifican el inventario; los anónimos solo consultan. El Sprint 3 Planning hace lo equivalente en el equipo: convierte el backlog de ideas en un **compromiso real** para las semanas siguientes. En ambos planos, esta semana marca la transición de "demo" a "producción".

---

## 2. Competencias de la semana

**Resultado de aprendizaje (SEP):**
El estudiante integra el sistema de autenticación de Django para proteger las operaciones de escritura, configura el ciclo login/logout y adapta las plantillas para mostrar contenido condicional según el estado de autenticación; en paralelo, abre formalmente el Sprint 3 con un backlog refinado.

**Actividades clave de la competencia laboral:**

- **S1 — Frameworks:** Configura `LOGIN_URL`, `LOGIN_REDIRECT_URL` y `LOGOUT_REDIRECT_URL` en `settings.py`; registra `LoginView` y `LogoutView` en `urls.py`; crea `registration/login.html`; aplica `@login_required` en `crear_producto`, `editar_producto` y `eliminar_producto`; muestra contenido condicional con `{% if user.is_authenticated %}` en `base.html`.
- **S2 — Metodologías ágiles:** Abre el Sprint 3 con Sprint Goal definido; refina el backlog (historias con criterios de aceptación actualizados); mueve HU-05 y HU-06 a "In Progress" en el Kanban.

---

## 3. PARTE I — Estructura académica (modelo Corina Schmelkes)

### 3.1 Introducción

Un sistema de inventario sin autenticación expone sus datos a cualquier visitante. Django incluye un sistema de autenticación completo desde su instalación inicial —`django.contrib.auth` ya está en `INSTALLED_APPS` por defecto— que proporciona modelo de usuario, vistas de login/logout, y el decorador `@login_required` (Django Software Foundation, s.f.). Esta semana el estudiante activa esas baterías incluidas con configuración mínima. Desde el ángulo metodológico, Schwaber y Sutherland (2020) describen el refinamiento del backlog (*grooming*) como el proceso continuo de clarificar, estimar y priorizar historias antes de que entren en un sprint; es la actividad que garantiza que el equipo nunca arranque un sprint con trabajo ambiguo.

### 3.2 Planteamiento del problema

El CRUD del sistema es funcional, pero cualquier persona con la URL puede borrar un producto. ¿Cómo proteger las operaciones de escritura sin construir un sistema de autenticación desde cero, y cómo asegurarse de que el Sprint 3 arranque con historias claras y estimadas?

### 3.3 Justificación

`@login_required` es un decorador de una sola línea que encapsula toda la lógica de protección: si el usuario no está autenticado, lo redirige a `LOGIN_URL`; si lo está, ejecuta la vista normalmente. Django Software Foundation (s.f.) documenta este patrón como la forma canónica de proteger vistas funcionales. El refinamiento del backlog, en paralelo, aplica el mismo principio de "clarificar antes de ejecutar": una historia sin criterios de aceptación es tan peligrosa para el sprint como una vista sin `@login_required` para el sistema.

### 3.4 Objetivos

**General:** Que el estudiante proteja las vistas de escritura con `@login_required`, configure el ciclo login/logout y abra el Sprint 3 con backlog refinado.

**Específicos:**
1. Registrar `LoginView` y `LogoutView` en `urls.py` del proyecto (S1).
2. Configurar `LOGIN_URL`, `LOGIN_REDIRECT_URL` y `LOGOUT_REDIRECT_URL` (S1).
3. Crear `registration/login.html` con `{% csrf_token %}` (S1).
4. Aplicar `@login_required` en las tres vistas de escritura (S1).
5. Mostrar `{% if user.is_authenticated %}` en `base.html` para contenido condicional (S1).
6. Documentar el Sprint 3 Planning con Sprint Goal + HUs refinadas (S2).

### 3.5 Marco teórico (con código)

**`django.contrib.auth`: baterías incluidas.** La documentación oficial de Django (Django Software Foundation, s.f.) indica que `django.contrib.auth` está activo por defecto y proporciona el modelo `User`, vistas de autenticación y el decorador `@login_required`. No se necesita instalar nada extra:

```python
# Verificacion: auth ya está en INSTALLED_APPS por defecto
# django.contrib.auth          ← modelo User
# django.contrib.contenttypes  ← requerido por auth
# Ambos ya están en INSTALLED_APPS al crear el proyecto
```

**Configurar `settings.py`.** Tres constantes controlan el flujo de redirección:

```python
# inventario_proyecto/settings.py
LOGIN_URL           = "/accounts/login/"   # a donde van los no autenticados
LOGIN_REDIRECT_URL  = "/productos/"         # a donde van tras login exitoso
LOGOUT_REDIRECT_URL = "/accounts/login/"   # a donde van tras logout
```

**Registrar las vistas en `urls.py`.** Django trae `LoginView` y `LogoutView` listas para usar:

```python
# inventario_proyecto/urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/",            admin.site.urls),
    path("accounts/login/",   auth_views.LoginView.as_view(),  name="login"),
    path("accounts/logout/",  auth_views.LogoutView.as_view(), name="logout"),
    path("",                  include("productos.urls", namespace="productos")),
]
```

**`registration/login.html`.** Django busca la plantilla en `registration/login.html` dentro de cualquier directorio de `TEMPLATES`. El formulario de login es un `AuthenticationForm` estándar:

```html
{% extends "base.html" %}
{% block title %}Iniciar sesión{% endblock %}
{% block content %}
<h2>Iniciar sesión</h2>
{% if form.errors %}
<p>Usuario o contraseña incorrectos. Intenta de nuevo.</p>
{% endif %}
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Entrar</button>
</form>
{% endblock %}
```

**`@login_required`: proteger una vista en una línea.** La documentación oficial (Django Software Foundation, s.f.) explica que el decorador verifica `request.user.is_authenticated`; si es `False`, redirige a `LOGIN_URL` con `?next=<url_solicitada>`:

```python
from django.contrib.auth.decorators import login_required

@login_required                    # ← UNA sola línea
def crear_producto(request):
    ...

# Verificaciones esperadas:
# GET /productos/nuevo/ sin autenticar → 302 a /accounts/login/?next=/productos/nuevo/
# GET /productos/nuevo/ autenticado   → 200 (form visible)
```

**Contenido condicional en `base.html`.** La variable `user` está disponible en todas las plantillas gracias al procesador de contexto `django.contrib.auth.context_processors.auth` (activo por defecto):

```html
{% if user.is_authenticated %}
    <a href="/accounts/logout/">Cerrar sesión ({{ user.username }})</a>
    | <a href="/productos/nuevo/">+ Nuevo</a>
{% else %}
    <a href="/accounts/login/">Iniciar sesión</a>
{% endif %}

<!-- Resultado:
     Usuario anónimo  → ve "Iniciar sesión"
     Usuario testuser → ve "Cerrar sesión (testuser)" | "+ Nuevo"  -->
```

**Nota sobre `ALLOWED_HOSTS`.** Para que el cliente de pruebas y el servidor de desarrollo funcionen, `ALLOWED_HOSTS` debe incluir los hosts usados:

```python
# settings.py — desarrollo local
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "testserver"]
# Verificacion: manage.py check no debe reportar DisallowedHost
```

### 3.6 Metodología

Trabajo guiado e individual. La sesión sigue el orden: configurar `settings.py` → registrar URLs de auth → crear plantilla de login → aplicar `@login_required` → actualizar `base.html` con nav condicional → verificar el ciclo completo con las 11 aserciones.

### 3.7 Desarrollo temático

**S1 — Frameworks (≈9 h reportadas)**
1. `django.contrib.auth`: qué incluye, por qué ya está en `INSTALLED_APPS`.
2. `LoginView` y `LogoutView`: vistas basadas en clases incluidas; no se necesita código propio.
3. `settings.py`: `LOGIN_URL`, `LOGIN_REDIRECT_URL`, `LOGOUT_REDIRECT_URL`.
4. `registration/login.html`: dónde la busca Django; `AuthenticationForm` automático.
5. `@login_required`: qué hace, la redirección con `?next=`, vistas que proteger.
6. `user.is_authenticated` y `user.username` en plantillas.
7. `ALLOWED_HOSTS`: por qué importa para el servidor de desarrollo y las pruebas.

**S2 — Metodologías ágiles (≈8 h reportadas)**
1. Refinamiento del backlog (*grooming*): clarificar, re-estimar y priorizar HUs.
2. Sprint 3 Planning: Sprint Goal + HUs seleccionadas + estimación + Kanban.
3. HU-05 (login/logout, 5 pts) y HU-06 (`@login_required`, 3 pts) — completadas esta semana.
4. HU-07 (CBV, 5 pts) — queda para la Semana 9.

### 3.8 Práctica de laboratorio

**Objetivo:** activar el sistema de autenticación de Django, proteger las vistas de escritura y verificar el ciclo completo login → acceso → logout.

---

#### PASO 1 — Actualizar `settings.py`

```python
# inventario_proyecto/settings.py

# Hosts permitidos (desarrollo)
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "testserver"]

# Al final del archivo — autenticacion
LOGIN_URL           = "/accounts/login/"
LOGIN_REDIRECT_URL  = "/productos/"
LOGOUT_REDIRECT_URL = "/accounts/login/"
```

---

#### PASO 2 — Actualizar `inventario_proyecto/urls.py`

```python
"""URLs del proyecto — Semana 8: autenticacion integrada."""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path("admin/",            admin.site.urls),
    path("accounts/login/",   auth_views.LoginView.as_view(),  name="login"),
    path("accounts/logout/",  auth_views.LogoutView.as_view(), name="logout"),
    path("",                  include("productos.urls", namespace="productos")),
]
```

---

#### PASO 3 — Crear `templates/registration/login.html`

```bash
mkdir -p templates/registration
```

```html
{% extends "base.html" %}

{% block title %}Iniciar sesión{% endblock %}

{% block content %}
<h2>Iniciar sesión</h2>

{% if form.errors %}
<p><strong>Usuario o contraseña incorrectos.</strong> Intenta de nuevo.</p>
{% endif %}

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Entrar</button>
</form>
{% endblock %}
```

---

#### PASO 4 — Actualizar `productos/views.py` (agregar `@login_required`)

```python
"""Vistas de la aplicacion productos — Semana 8.

Protege las operaciones de escritura con @login_required.
Hilo conector: "Usuarios reales".
"""

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductoForm
from .models import Producto


def bienvenida(request: HttpRequest) -> HttpResponse:
    """Pagina principal — publica."""
    return render(request, "base.html", {"titulo": "Bienvenido"})


def lista_productos(request: HttpRequest) -> HttpResponse:
    """Lista publica de productos — sin autenticacion."""
    productos = Producto.objects.all()
    return render(request, "productos/lista.html", {"productos": productos})


def detalle_producto(request: HttpRequest, producto_id: int) -> HttpResponse:
    """Detalle publico de un producto."""
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, "productos/detalle.html", {"producto": producto})


@login_required
def crear_producto(request: HttpRequest) -> HttpResponse:
    """Crear un producto — requiere autenticacion.

    Usuarios no autenticados son redirigidos a LOGIN_URL.
    """
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos:lista")
    else:
        form = ProductoForm()
    return render(request, "productos/crear.html", {"form": form})


@login_required
def editar_producto(request: HttpRequest, producto_id: int) -> HttpResponse:
    """Editar un producto — requiere autenticacion."""
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("productos:lista")
    else:
        form = ProductoForm(instance=producto)
    return render(
        request, "productos/editar.html",
        {"form": form, "producto": producto},
    )


@login_required
def eliminar_producto(request: HttpRequest, producto_id: int) -> HttpResponse:
    """Eliminar un producto — requiere autenticacion."""
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == "POST":
        producto.delete()
        return redirect("productos:lista")
    return render(
        request, "productos/eliminar.html",
        {"producto": producto},
    )
```

---

#### PASO 5 — Actualizar `templates/base.html` (nav condicional)

```html
<nav>
    <a href="/">Inicio</a> |
    <a href="/productos/">Productos</a>
    {% if user.is_authenticated %}
        | <a href="/productos/nuevo/">+ Nuevo producto</a>
        | <a href="/accounts/logout/">Cerrar sesión ({{ user.username }})</a>
    {% else %}
        | <a href="/accounts/login/">Iniciar sesión</a>
    {% endif %}
</nav>
```

---

#### PASO 6 — Crear usuario y verificar

```bash
python3 manage.py createsuperuser   # o usar el admin existente
# Ingresar: username, email (opcional), contraseña

python3 manage.py check
# Verificacion esperada: "System check identified no issues (0 silenced)."

python3 manage.py runserver
# Pruebas manuales:
#   GET /productos/nuevo/            → redirect 302 a /accounts/login/?next=...
#   GET /accounts/login/             → formulario de login (200)
#   POST /accounts/login/ (válido)   → redirect 302 a /productos/
#   GET /productos/nuevo/            → 200 (autenticado)
#   GET /accounts/logout/            → logout + redirect a /accounts/login/
#   GET /productos/nuevo/            → redirect 302 (bloqueado de nuevo)
```

---

#### PASO 7 — Sprint 3 Planning (S2)

Crea `sprint3_planning.md` en la raíz del proyecto:

```markdown
# Sprint 3 Planning — Sistema de Inventario
## Fecha: ___________ | Duración: 2 semanas (Sem 8–9)

### Sprint Goal
"Los usuarios autenticados gestionan el inventario; los anónimos
 solo consultan. Las vistas de gestión migran a Vistas Basadas
 en Clases (CBV) para mejorar la mantenibilidad del código."

### Velocidad del equipo: ~10 pts/sprint

### Historias seleccionadas
| ID    | Historia                                         | Pts | Estado       |
|-------|--------------------------------------------------|-----|--------------|
| HU-05 | Login/logout con LoginView/LogoutView            | 5   | ✅ Esta semana |
| HU-06 | @login_required en vistas de escritura           | 3   | ✅ Esta semana |
| HU-07 | Migrar CRUD a Vistas Basadas en Clases (CBV)     | 5   | To Do (Sem 9)|

### Total comprometido: 13 pts (ligeramente sobre velocidad; HU-05/06 son estratégicas)

### Kanban
- HU-05 → In Progress (iniciada Semana 8)
- HU-06 → In Progress (iniciada Semana 8)
- HU-07 → To Do (Semana 9)
```

---

#### Entregables — Sprint 3 arranca

```bash
git checkout main
git checkout -b sprint3/autenticacion-cbv
git add productos/views.py inventario_proyecto/urls.py
git add inventario_proyecto/settings.py
git add templates/registration/ sprint3_planning.md
git commit -m "Sprint 3: @login_required + LoginView + nav condicional"
git push origin sprint3/autenticacion-cbv
```

---

### 3.9 Análisis (5 preguntas de reflexión)

1. ¿Qué hace Django con el parámetro `?next=/productos/nuevo/` que añade a la URL de login? ¿Cómo lo usa después del login exitoso?
2. ¿Por qué `lista_productos` y `detalle_producto` no llevan `@login_required`? ¿Cuándo sería razonable protegerlas también?
3. `LoginView` es una **Vista Basada en Clases** (CBV). ¿Qué ventaja tiene sobre una función de vista equivalente?
4. Si un atacante intenta acceder a `/productos/nuevo/` sin autenticar, ¿qué ve exactamente y por qué no puede forzar la acción?
5. HU-05 y HU-06 suman 8 pts y la velocidad promedio es ~10. ¿Por qué comprometiste 13 pts en el Sprint 3? Justifica la decisión.

### 3.10 Conclusiones

Con `@login_required` activo, el sistema de inventario tiene su primera capa de seguridad real. Un visitante anónimo puede ver los productos pero no modificarlos; la navegación se adapta visualmente según el estado de autenticación. `LoginView` y `LogoutView` demostraron una idea central del módulo: los frameworks de alta productividad incluyen soluciones probadas para problemas comunes —no hay que reinventar el login—. El Sprint 3 arranca con dos historias entregadas esta misma semana y una pendiente (CBV) que veremos en la Semana 9.

---

## 4. PARTE II — Momentos didácticos (Sergio Tobón)

### 4.1 Momento 1 — Apertura
Planteamiento: "¿qué pasa si alguien descubre la URL `/productos/nuevo/`?". Demo del docente: acceder sin autenticar → redirect a login → ingresar credenciales → acceso. Introducir el Sprint 3 Planning con el Sprint Goal.

### 4.2 Momento 2 — Desarrollo
Configuración guiada de `settings.py` → `urls.py` con `LoginView`/`LogoutView` → `registration/login.html` → `@login_required` en vistas → nav condicional en `base.html` → verificar las 11 aserciones. En paralelo, redactar `sprint3_planning.md`.

### 4.3 Momento 3 — Cierre
Verificación del ciclo completo (anónimo → login → acceso → logout → bloqueado), commit del Sprint 3, subida a Classroom y respuestas de análisis.

---

## 5. Estrategia de evaluación de la semana

| Evidencia | Submódulo | Instrumento | Ponderación |
|---|---|---|---|
| `@login_required` en crear, editar y eliminar; redirect 302 a login sin autenticar | S1 | Lista de cotejo (11 aserciones) | 35 % |
| `LoginView`/`LogoutView` en `urls.py`; plantilla `registration/login.html` funcional | S1 | Verificación directa | 20 % |
| Nav condicional: anónimo ve "login" / autenticado ve username + "Cerrar sesión" | S1 | Captura de pantalla | 10 % |
| `sprint3_planning.md`: Sprint Goal + HU-05/06 In Progress + HU-07 To Do + Kanban | S2 | Lista de cotejo | 25 % |
| Respuestas de análisis (5 preguntas) | Transversal | Lista de cotejo | 10 % |

---

## 6. Recursos didácticos

- Proyecto Django de la Semana 7 (evaluación superada) en `main`.
- Computadora con Python 3.11+, Django 4.2 y VS Code.
- Navegador web para probar el ciclo login/logout.
- GitHub Projects para actualizar el Kanban del Sprint 3.
- Google Classroom para entrega de evidencias.

---

## 7. Referencias (APA 7)

Django Software Foundation. (s.f.). *User authentication in Django*. https://docs.djangoproject.com/en/4.2/topics/auth/

Django Software Foundation. (s.f.). *Using the Django authentication system*. https://docs.djangoproject.com/en/4.2/topics/auth/default/

Django Software Foundation. (s.f.). *The login_required decorator*. https://docs.djangoproject.com/en/4.2/topics/auth/default/#the-login-required-decorator

Schwaber, K., & Sutherland, J. (2020). *La guía de Scrum*. https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf

---

*Guía generada bajo ROL 2 — Asesor Académico Experto · Prompt Maestro v1.0 · Una semana a la vez.*
*Parámetros respetados: 13 semanas · submódulos y horas SEP sin modificar · cita narrativa.*
*Código verificado: 11 aserciones (crear/editar/eliminar anónimo→302·login / crear autenticado→200+302+BD / lista pública→200 / settings correctos / LoginView→200 / ciclo bloq→login→200→logout→bloq / credenciales incorrectas / nav condicional).*
