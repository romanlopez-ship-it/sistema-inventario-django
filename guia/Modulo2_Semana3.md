# Módulo II · Semana 3 — Guía Académica y de Laboratorio
## Técnico en Programación (SEP 3061300006-23) · UTEC Celaya
### Asesor: MC. Román Fernando López González

---

## 1. Identificación de la semana

| Campo | Detalle |
|---|---|
| Carrera | Técnico en Programación |
| Módulo | II — Desarrolla software con herramientas orientadas a la productividad (272 h) |
| Semana | 3 de 13 |
| Submódulos integrados | S1 Frameworks (144 h) · S2 Metodologías ágiles (128 h) |
| **Hilo conector de la semana** | **"Historias → vistas"** |
| Stack | Django 4.2 LTS · Django Template Language (DTL) · Python 3.11+ |
| Carga horaria reportada | 17 h/semana (S1 = 9 h · S2 = 8 h) |
| Carga horaria real (planeación) | 14.16 h/semana |
| Tiempo fantasma máximo | 15 min/día |
| Plataforma institucional | Google Classroom |
| Prerrequisito | Semana 2 — vistas `lista_productos` y `detalle_producto` + Sprint 1 Planning en rama `sprint1/lista-detalle-productos` |

> **Hilo conector:** una historia de usuario describe en lenguaje natural lo que el usuario *verá* al usar el sistema. Una plantilla Django es exactamente eso: el HTML que el usuario verá. Esta semana el estudiante convierte sus historias en plantillas reales, y descubre que los **criterios de aceptación** de Scrum —*dado / cuando / entonces*— son la prueba de que la plantilla cumple lo que la historia prometió.

---

## 2. Competencias de la semana

**Resultado de aprendizaje (SEP):**
El estudiante aplica el Django Template Language para separar la lógica de presentación del código Python; implementa herencia de plantillas con `base.html`; y cierra el Sprint 1 con una revisión formal, escribiendo criterios de aceptación para el Product Backlog.

**Actividades clave de la competencia laboral:**

- **S1 — Frameworks:** Crea la jerarquía de plantillas (`base.html` + plantillas de *app*); usa `{% extends %}`, `{% block %}`, `{{ variables }}` y `{% for %}`/`{% empty %}`; reemplaza `HttpResponse` con `render()`.
- **S2 — Metodologías ágiles:** Realiza el Sprint 1 Review; añade criterios de aceptación en formato Gherkin (*Dado / Cuando / Entonces*) a cada historia del backlog; elabora el Sprint 2 Planning inicial.

---

## 3. PARTE I — Estructura académica (modelo Corina Schmelkes)

### 3.1 Introducción

Las semanas anteriores el estudiante devolvía HTML como texto plano dentro de `HttpResponse`. Eso viola un principio fundamental que Fowler (2003) denomina *separación de responsabilidades*: la vista Python debe decidir *qué* mostrar; la plantilla debe encargarse de *cómo* mostrarlo. Django Software Foundation (s.f.) implementa esta separación a través del Django Template Language (DTL): un lenguaje de plantillas que permite incrustar variables y lógica mínima en archivos HTML sin mezclarlos con código Python. En paralelo, Cohn (2004) señala que una historia de usuario solo está realmente terminada cuando cumple sus **criterios de aceptación** —condiciones verificables, escritas desde la perspectiva del usuario, que definen el comportamiento exacto esperado—. Esta semana ambos conceptos convergen: la plantilla implementa la historia; los criterios verifican que lo hace bien.

### 3.2 Planteamiento del problema

El sistema de inventario ya funciona: la lista y el detalle se muestran en el navegador. Pero todo el HTML vive dentro del código Python, mezclado con la lógica. Cambiar el color de un título o añadir un logo requeriría editar `views.py`. ¿Cómo organizar el proyecto para que el diseño visual sea independiente de la lógica, y cómo garantizar que cada cambio sigue cumpliendo lo que las historias prometieron?

### 3.3 Justificación

La separación en plantillas es una práctica estándar en todos los frameworks web: Django, Flask, Laravel, React (JSX) y Angular la implementan de formas distintas, pero con el mismo propósito (Fowler, 2003). Aprender la de Django consolida un patrón mental transferible. Por otro lado, Cohn (2004) demuestra que los equipos ágiles que escriben criterios de aceptación antes de implementar reducen significativamente los errores de interpretación entre el Product Owner y el equipo de desarrollo. Esta semana el estudiante cierra el Sprint 1 con criterios que ya puede verificar ejecutando su propio servidor.

### 3.4 Objetivos

**General:** Que el estudiante implemente herencia de plantillas Django con `base.html` y criterios de aceptación Gherkin para las historias del Sprint 1.

**Específicos:**
1. Crear `base.html` con bloques `title` y `content` reutilizables (S1).
2. Implementar `lista.html` y `detalle.html` que extiendan `base.html` (S1).
3. Actualizar las vistas para usar `render()` en lugar de `HttpResponse` (S1).
4. Escribir criterios de aceptación Gherkin para HU-01 y HU-01a (S2).
5. Cerrar el Sprint 1 con un Sprint Review y abrir el Sprint 2 Planning (S2).

### 3.5 Marco teórico (con código)

**El Django Template Language (DTL).** Django Software Foundation (s.f.) define tres tipos de construcciones en las plantillas: *variables* (`{{ }}`), *etiquetas* (`{% %}`) y *filtros* (`|`). Las variables se reemplazan con sus valores en tiempo de render; las etiquetas controlan la lógica (bucles, condiciones, bloques); los filtros transforman el valor antes de mostrarlo.

```html
<!-- Ejemplos de sintaxis DTL -->
{{ producto.nombre }}            <!-- variable: imprime el nombre -->
{{ precio|floatformat:2 }}       <!-- filtro: dos decimales -->
{% for item in lista %}          <!-- etiqueta: bucle -->
    <li>{{ item }}</li>
{% empty %}                      <!-- caso lista vacía -->
    <li>Sin elementos</li>
{% endfor %}
```

**Herencia de plantillas.** Django Software Foundation (s.f.) describe la herencia como el mecanismo DRY (*Don't Repeat Yourself*) de las plantillas. `base.html` define la estructura común; cada plantilla hija declara `{% extends "base.html" %}` y sobreescribe solo los bloques que necesita:

```
base.html          ← estructura HTML completa + bloques vacíos
    │
    ├── lista.html     {% extends "base.html" %} + rellena {% block content %}
    └── detalle.html   {% extends "base.html" %} + rellena {% block content %}
```

```python
# views.py: render() en lugar de HttpResponse
from django.shortcuts import render

def lista_productos(request):
    context = {"productos": PRODUCTOS_EJEMPLO}
    return render(request, "productos/lista.html", context)
    # render() busca la plantilla, inyecta el contexto y devuelve HttpResponse

# Verificacion esperada: la respuesta contiene <header> de base.html
#   Y contiene los nombres de los productos inyectados desde context.
```

**Criterios de aceptación en formato Gherkin.** Cohn (2004) propone escribir los criterios de aceptación con la estructura *Dado / Cuando / Entonces* (*Given / When / Then*), que describe el estado inicial, la acción y el resultado esperado:

```
HU-01: Ver lista de productos
  Dado que hay 3 productos registrados
  Cuando el usuario accede a /productos/
  Entonces ve una lista con el nombre de cada producto
  Y cada nombre es un enlace a su página de detalle

HU-01a: Ver detalle de un producto
  Dado que existe el producto con ID 1
  Cuando el usuario accede a /productos/1/
  Entonces ve el nombre "Teclado USB" y el precio "$350.00"

  Dado que NO existe el producto con ID 99
  Cuando el usuario accede a /productos/99/
  Entonces recibe una respuesta con status HTTP 404
```

> Nota: estas tres condiciones corresponden exactamente a las verificaciones que `manage.py test` (o el cliente de pruebas) ejecutará automáticamente. Los criterios de aceptación *son* las pruebas.

### 3.6 Metodología

Trabajo guiado e individual. La sesión migra el proyecto existente de `HttpResponse` a plantillas en tres pasos: crear `base.html` → crear plantillas de app que extienden base → actualizar vistas con `render()`. En paralelo, el equipo cierra el Sprint 1 y escribe criterios de aceptación para el backlog.

### 3.7 Desarrollo temático

**S1 — Frameworks (≈9 h reportadas)**
1. El problema: HTML mezclado con Python y el principio DRY.
2. Configuración de `TEMPLATES` en `settings.py`: `DIRS` y `APP_DIRS`.
3. Estructura de directorios de plantillas.
4. Sintaxis DTL: `{{ }}`, `{% %}`, filtros, `{% for %}` / `{% empty %}`.
5. Herencia: `{% extends %}`, `{% block %}` / `{% endblock %}`.
6. `render()`: diferencias con `HttpResponse`; el diccionario de contexto.

**S2 — Metodologías ágiles (≈8 h reportadas)**
1. Sprint Review: ¿el incremento cumple el Sprint Goal?
2. Criterios de aceptación: propósito y formato Gherkin.
3. Refinamiento del backlog: añadir criterios a las historias existentes.
4. Sprint 2 Planning: selección de HU-02 (registrar producto) para la siguiente iteración.

### 3.8 Práctica de laboratorio

**Objetivo:** migrar el proyecto de la Semana 2 a plantillas Django con herencia de `base.html`, y cerrar el Sprint 1 con criterios de aceptación documentados.

---

#### PASO 1 — Estructura de directorios de plantillas

```
inventario_proyecto/          ← raíz del proyecto
├── templates/
│   └── base.html             ← plantilla base del proyecto
├── productos/
│   └── templates/
│       └── productos/
│           ├── lista.html
│           └── detalle.html
```

```bash
mkdir -p templates
mkdir -p productos/templates/productos
```

---

#### PASO 2 — Configurar `settings.py`

Añadir la carpeta `templates/` del proyecto a `TEMPLATES[0]['DIRS']`:

```python
# inventario_proyecto/settings.py
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],   # ← agregar esta línea
        'APP_DIRS': True,                   # busca también en <app>/templates/
        ...
    },
]
```

---

#### PASO 3 — Crear `templates/base.html`

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Sistema de Inventario{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Sistema de Inventario</h1>
        <nav>
            <a href="/">Inicio</a> |
            <a href="/productos/">Productos</a>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <p>Tecnico en Programacion — Modulo II</p>
    </footer>
</body>
</html>
```

---

#### PASO 4 — Crear `productos/templates/productos/lista.html`

```html
{% extends "base.html" %}

{% block title %}Lista de productos{% endblock %}

{% block content %}
<h2>Productos ({{ productos|length }})</h2>
<ul>
{% for pid, datos in productos.items %}
    <li>
        <a href="/productos/{{ pid }}/">{{ datos.nombre }}</a>
        — ${{ datos.precio }}
    </li>
{% empty %}
    <li>No hay productos registrados.</li>
{% endfor %}
</ul>
{% endblock %}
```

---

#### PASO 5 — Crear `productos/templates/productos/detalle.html`

```html
{% extends "base.html" %}

{% block title %}{{ producto.nombre }}{% endblock %}

{% block content %}
<h2>{{ producto.nombre }}</h2>
<p><strong>Precio:</strong> ${{ producto.precio }}</p>
<p><a href="/productos/">← Volver a la lista</a></p>
{% endblock %}
```

---

#### PASO 6 — Actualizar `productos/views.py`

```python
"""Vistas de la aplicacion productos — Semana 3.

Reemplaza HttpResponse con render() y plantillas Django.
Hilo conector: "Historias -> vistas".
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Datos de ejemplo (sin base de datos — se incorpora en Semana 4)
PRODUCTOS_EJEMPLO: dict[int, dict] = {
    1: {"nombre": "Teclado USB",         "precio": 350.00},
    2: {"nombre": "Monitor 24 pulgadas", "precio": 3200.00},
    3: {"nombre": "Mouse inalambrico",   "precio": 280.00},
}


def bienvenida(request: HttpRequest) -> HttpResponse:
    """Devuelve la pagina principal usando la plantilla base.

    Args:
        request: Objeto HttpRequest generado por Django.

    Returns:
        HttpResponse renderizado con base.html.
    """
    return render(request, "base.html", {"titulo": "Bienvenido"})


def lista_productos(request: HttpRequest) -> HttpResponse:
    """Devuelve la lista de productos usando una plantilla Django.

    Args:
        request: Objeto HttpRequest generado por Django.

    Returns:
        HttpResponse renderizado con productos/lista.html.
    """
    context = {"productos": PRODUCTOS_EJEMPLO}
    return render(request, "productos/lista.html", context)


def detalle_producto(request: HttpRequest, producto_id: int) -> HttpResponse:
    """Devuelve el detalle de un producto usando una plantilla Django.

    Args:
        request: Objeto HttpRequest generado por Django.
        producto_id: Identificador entero capturado desde la URL.

    Returns:
        HttpResponse renderizado con productos/detalle.html (200),
        o HttpResponse de error (404) si el producto no existe.
    """
    producto = PRODUCTOS_EJEMPLO.get(producto_id)
    if producto is None:
        return HttpResponse(
            f"<h1>Producto {producto_id} no encontrado</h1>",
            status=404,
        )
    context = {"producto_id": producto_id, "producto": producto}
    return render(request, "productos/detalle.html", context)
```

---

#### PASO 7 — Verificar

```bash
python3 manage.py check
# Verificacion esperada: "System check identified no issues (0 silenced)."

python3 manage.py runserver
# Abrir en el navegador y verificar:
#   /             → bienvenida con <header> y <footer> de base.html
#   /productos/   → lista de 3 productos, cada uno con enlace
#   /productos/1/ → "Teclado USB" con precio $350.0
#   /productos/99/→ status 404
```

---

#### PASO 8 — Sprint 1 Review + Backlog refinado (S2)

Crea `sprint1_review.md` en la raíz del proyecto:

```markdown
# Sprint 1 Review — Sistema de Inventario
## Fecha: ___________

### Sprint Goal verificado
"El sistema muestra la lista de productos y el detalle de cada uno
 accesible por URL, con plantillas HTML separadas del código Python."

### Incremento entregado
- [x] Vista `lista_productos` con plantilla `lista.html`
- [x] Vista `detalle_producto` con plantilla `detalle.html`
- [x] Herencia de `base.html` (header/footer compartidos)
- [x] Status 404 para productos inexistentes

### Criterios de aceptación verificados (Gherkin)
HU-01: Ver lista de productos
  ✅ Dado 3 productos / Cuando GET /productos/ / Entonces lista con nombres y enlaces

HU-01a: Ver detalle de producto
  ✅ Dado ID=1 / Cuando GET /productos/1/ / Entonces nombre y precio correctos
  ✅ Dado ID=99 / Cuando GET /productos/99/ / Entonces status 404

### Deuda técnica identificada
- Los datos son estáticos (diccionario). Sprint 2 introducirá la base de datos.

### Sprint 2 — Historia seleccionada
HU-02: Registrar un producto nuevo (requiere modelo + formulario — Semana 4)
```

---

#### Entregables — cierre del Sprint 1

```bash
# Añadir plantillas y sprint review al commit
git add templates/ productos/templates/ productos/views.py sprint1_review.md
git commit -m "Sprint 1 completo: plantillas con herencia y Sprint Review"
git push origin sprint1/lista-detalle-productos

# Merge a main: Sprint 1 cerrado
git checkout main
git merge sprint1/lista-detalle-productos
git push origin main
```

> **Fallback sin conexión:** omite los `push`. Los commits locales y el merge son válidos; publica después con `git push origin main`.

---

### 3.9 Análisis (5 preguntas de reflexión)

1. ¿Por qué `APP_DIRS = True` en `settings.py` permite a Django encontrar `productos/templates/productos/lista.html` sin declarar la ruta explícitamente?
2. ¿Qué pasaría si en `lista.html` escribieras `{% extends "base.html" %}` en la línea 3 en lugar de la línea 1?
3. Escribe el criterio de aceptación Gherkin para HU-02 (registrar un producto nuevo).
4. ¿En qué se parece el bloque `{% block content %}` de `base.html` a una función con `return` en Python?
5. El filtro `{{ precio|floatformat:2 }}` muestra dos decimales. ¿Cómo mostrarías el precio con un símbolo de moneda, usando solo DTL?

### 3.10 Conclusiones

La separación entre lógica (Python) y presentación (plantillas HTML) es uno de los avances más visibles de la semana: el archivo `views.py` se volvió más corto y más legible, y las plantillas pueden editarse sin tocar Python. El Sprint 1 Review cierra formalmente la primera iteración del proyecto e introduce los criterios de aceptación como el puente entre la historia de usuario y la verificación técnica —un puente que el estudiante ya sabe cruzar en ambas direcciones.

---

## 4. PARTE II — Momentos didácticos (Sergio Tobón)

### 4.1 Momento 1 — Apertura
Planteamiento del problema: "¿qué pasa si el cliente quiere cambiar el color del título?". Demo del docente: editar `views.py` para cambiar HTML vs. editar `base.html`. Introducción a la sintaxis DTL y al principio DRY.

### 4.2 Momento 2 — Desarrollo
Creación guiada de `base.html` → `lista.html` → `detalle.html`; actualización de `views.py` con `render()`; verificación en navegador de las cuatro URLs. En paralelo, redacción de criterios de aceptación Gherkin para HU-01 y HU-01a.

### 4.3 Momento 3 — Cierre
Sprint 1 Review formal (`sprint1_review.md`), commit de cierre del sprint, merge a `main` y subida a Classroom. Respuesta a las 5 preguntas de análisis.

---

## 5. Estrategia de evaluación de la semana

| Evidencia | Submódulo | Instrumento | Ponderación |
|---|---|---|---|
| `base.html` con bloques `title` y `content`; `lista.html` y `detalle.html` con `{% extends %}` | S1 | Rúbrica de plantillas (herencia + DTL correcto) | 35 % |
| Vistas actualizadas con `render()`, 5 verificaciones pasan | S1 | Lista de cotejo técnica | 15 % |
| `sprint1_review.md` con criterios Gherkin verificados y Sprint 2 HU seleccionada | S2 | Lista de cotejo | 35 % |
| Respuestas de análisis (5 preguntas) | Transversal | Lista de cotejo | 15 % |

---

## 6. Recursos didácticos

- Proyecto Django de la Semana 2 en rama `sprint1/lista-detalle-productos`.
- Computadora con Python 3.11+, Django 4.2 y VS Code.
- Navegador web para verificar plantillas renderizadas.
- Google Classroom para entrega de evidencias.

---

## 7. Referencias (APA 7)

Cohn, M. (2004). *User stories applied: For agile software development*. Addison-Wesley Professional.

Django Software Foundation. (s.f.). *The Django template language*. https://docs.djangoproject.com/en/4.2/ref/templates/language/

Django Software Foundation. (s.f.). *Template inheritance*. https://docs.djangoproject.com/en/4.2/ref/templates/language/#template-inheritance

Fowler, M. (2003). *Patterns of enterprise application architecture*. Addison-Wesley.

Schwaber, K., & Sutherland, J. (2020). *La guía de Scrum*. https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf

---

*Guía generada bajo ROL 2 — Asesor Académico Experto · Prompt Maestro v1.0 · Una semana a la vez.*
*Parámetros respetados: 13 semanas · submódulos y horas SEP sin modificar · cita narrativa · código verificado (5 aserciones: 200 bienvenida, 200 lista 3 productos, 200 detalle Teclado USB $350, 404 detalle ID=99, herencia base.html con header+footer).*
