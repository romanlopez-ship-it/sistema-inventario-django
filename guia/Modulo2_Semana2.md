# Módulo II · Semana 2 — Guía Académica y de Laboratorio
## Técnico en Programación (SEP 3061300006-23) · UTEC Celaya
### Asesor: MC. Román Fernando López González

---

## 1. Identificación de la semana

| Campo | Detalle |
|---|---|
| Carrera | Técnico en Programación |
| Módulo | II — Desarrolla software con herramientas orientadas a la productividad (272 h) |
| Semana | 2 de 13 |
| Submódulos integrados | S1 Frameworks (144 h) · S2 Metodologías ágiles (128 h) |
| **Hilo conector de la semana** | **"Conectar las piezas"** |
| Stack | Django 4.2 LTS · Python 3.11+ · Scrum Sprint 1 |
| Carga horaria reportada | 17 h/semana (S1 = 9 h · S2 = 8 h) |
| Carga horaria real (planeación) | 14.16 h/semana |
| Tiempo fantasma máximo | 15 min/día |
| Plataforma institucional | Google Classroom |
| Prerrequisito | Semana 1 — proyecto Django con vista `bienvenida` + Product Backlog en repositorio |

> **Hilo conector:** en Django, esta semana los **URLs conectan peticiones con vistas** —la pieza del enrutador que une lo que el navegador pide con el código que responde—. En Scrum, los **eventos** conectan el trabajo del equipo en un flujo continuo: planear → ejecutar → revisar → mejorar. Dos estructuras de conexión que esta semana el estudiante aprende a leer y a operar juntas, arrancando formalmente el **Sprint 1**.

---

## 2. Competencias de la semana

**Resultado de aprendizaje (SEP):**
El estudiante profundiza en la estructura de un proyecto Django, configura patrones de URL con parámetros y registra múltiples vistas; al mismo tiempo, pone en marcha el Sprint 1 aplicando los eventos de Scrum sobre el Product Backlog elaborado la semana anterior.

**Actividades clave de la competencia laboral:**

- **S1 — Frameworks:** Configura URL patterns con parámetros de ruta (`<int:id>`), aplica *namespace* de URLs y construye vistas de lista y detalle.
- **S2 — Metodologías ágiles:** Identifica y describe los cinco eventos de Scrum; elabora el Sprint 1 Planning (`sprint1_planning.md`) y arranca el primer sprint sobre una rama de Git.

---

## 3. PARTE I — Estructura académica (modelo Corina Schmelkes)

### 3.1 Introducción

La semana anterior el estudiante vio Django como una caja negra que devolvía texto. Esta semana abre esa caja: entiende cómo `urls.py` actúa como enrutador —recibe la petición del navegador y decide qué función Python la atiende—, y cómo esa función puede recibir datos directamente desde la URL. Django Software Foundation (s.f.) denomina a este mecanismo *URL dispatcher*: un sistema de expresiones de ruta que captura segmentos de la URL como argumentos de la vista. En el plano metodológico, Schwaber y Sutherland (2020) describen el Sprint Planning como el evento que da inicio a cada sprint: el equipo selecciona las historias del Product Backlog que entregará y define cómo lo hará. Conectar ambas piezas esta semana —el enrutador de Django y el Sprint 1 de Scrum— prepara al estudiante para construir, en las semanas siguientes, las operaciones CRUD completas.

### 3.2 Planteamiento del problema

El proyecto de la Semana 1 solo tiene una vista y una URL. ¿Cómo organizar un sistema que necesita decenas de rutas sin que `urls.py` se convierta en un archivo inmanejable? Y en paralelo, ¿cómo hace el equipo para transformar el Product Backlog —una lista de deseos— en trabajo concreto planificado semana a semana?

### 3.3 Justificación

El URL dispatcher de Django resuelve el primer problema mediante *namespacing* y parámetros de ruta: cada *app* gestiona sus propias URLs y los parámetros viajan directamente a la vista sin que el programador tenga que parsear la cadena. El Sprint Planning resuelve el segundo: Schwaber y Sutherland (2020) establecen que el Sprint Goal —el objetivo del sprint— convierte el backlog abstracto en un compromiso concreto y verificable al final del sprint. Ambas técnicas comparten la misma virtud: reducen el caos descomponiéndolo en piezas manejables.

### 3.4 Objetivos

**General:** Que el estudiante configure URL routing con parámetros de ruta y *namespace*, construya vistas de lista y detalle, y arranque el Sprint 1 con su plan documentado.

**Específicos:**
1. Implementar `lista_productos` y `detalle_producto` con parámetro `<int:producto_id>` (S1).
2. Aplicar *namespace* de URLs con `app_name` para evitar colisiones entre *apps* (S1).
3. Identificar los cinco eventos de Scrum y su propósito (S2).
4. Elaborar el `sprint1_planning.md` con Sprint Goal, HUs seleccionadas y rama de Git (S2).

### 3.5 Marco teórico (con código)

**URL dispatcher y parámetros de ruta.**
La documentación oficial de Django (Django Software Foundation, s.f.) explica que `path()` acepta convertidores de tipo (`<int:id>`, `<str:nombre>`, `<slug:slug>`) que capturan segmentos de la URL y los pasan como argumentos a la vista. Esto elimina la necesidad de leer `request.GET` para datos de identificación:

```python
# productos/urls.py — patrón con parametro de tipo entero
from django.urls import path
from . import views

app_name = "productos"          # namespace: evita colisiones entre apps

urlpatterns = [
    path("",                             views.bienvenida,       name="bienvenida"),
    path("productos/",                   views.lista_productos,  name="lista"),
    path("productos/<int:producto_id>/", views.detalle_producto, name="detalle"),
]

# Con este patron:
#   /productos/       → llama a lista_productos(request)
#   /productos/3/     → llama a detalle_producto(request, producto_id=3)
#   /productos/abc/   → Django rechaza la URL (no coincide con <int:...>)
```

**Vista con parámetro de URL.**
La vista recibe el parámetro directamente como argumento Python:

```python
def detalle_producto(request: HttpRequest, producto_id: int) -> HttpResponse:
    """Devuelve el detalle de un producto segun su ID de URL.

    Args:
        request: Objeto HttpRequest generado por Django.
        producto_id: Entero capturado desde la URL por el dispatcher.

    Returns:
        HttpResponse 200 con el detalle, o 404 si no existe.
    """
    producto = PRODUCTOS_EJEMPLO.get(producto_id)
    if producto is None:
        return HttpResponse(
            f"<h1>Producto {producto_id} no encontrado</h1>",
            status=404,
        )
    return HttpResponse(f"<h1>{producto['nombre']}</h1>")

# Verificacion esperada:
#   producto_id=2  → status 200, contiene "Monitor 24 pulgadas"
#   producto_id=99 → status 404, contiene "no encontrado"
```

**Los cinco eventos de Scrum.**
Schwaber y Sutherland (2020) definen que el Sprint es el contenedor de los demás eventos:

| Evento | Propósito | Duración máx. (sprint 2 sem) |
|---|---|---|
| **Sprint** | Contenedor de todo el trabajo | 1–4 semanas |
| **Sprint Planning** | Definir qué y cómo se entregará | 4 h (sprint 2 sem) |
| **Daily Scrum** | Sincronizar el equipo cada día | 15 min |
| **Sprint Review** | Inspeccionar el incremento con el PO | 2 h |
| **Sprint Retrospective** | Mejorar la forma de trabajar | 1.5 h |

> La **cadencia** que impone Scrum hace que el equipo nunca trabaje más de un sprint sin recibir retroalimentación —el mismo principio que la espiral convergente aplica semana a semana en este módulo.

### 3.6 Metodología

Trabajo guiado e individual con computadora por alumno. La sesión extiende el proyecto de la Semana 1 añadiendo rutas y vistas, y lanza el Sprint 1 con un documento de planificación versionado en una rama de Git.

### 3.7 Desarrollo temático

**S1 — Frameworks (≈9 h reportadas)**
1. Revisión de la estructura del proyecto (manage.py, proyecto, *app*).
2. URL patterns: `path()`, convertidores de tipo, parámetros.
3. *Namespace* de URLs con `app_name`.
4. Vista `lista_productos`: recorrer una colección y generar HTML.
5. Vista `detalle_producto`: parámetro de ruta, respuesta 404.

**S2 — Metodologías ágiles (≈8 h reportadas)**
1. Los cinco eventos de Scrum: propósito y duración.
2. Daily Scrum: formato (¿qué hice ayer? ¿qué haré hoy? ¿hay impedimentos?).
3. Sprint Goal: qué debe quedar funcionando al terminar el sprint.
4. Sprint Planning: seleccionar HUs del backlog para el Sprint 1.
5. Rama de Git como espejo del sprint: una rama por sprint.

### 3.8 Práctica de laboratorio

**Objetivo:** extender el proyecto Django con vistas de lista y detalle, aplicar *namespace* de URLs y arrancar el Sprint 1 con su plan documentado en una rama.

---

#### PASO 1 — Abrir el proyecto de la Semana 1

```bash
cd inventario_proyecto      # carpeta del proyecto de la semana 1
git checkout main
git checkout -b sprint1/lista-detalle-productos
```

---
#### APENDICE 1 — Antes de continuar, un poquito de HTML: Etiquetas más usadas

#### Un poquito de HTML: Tabla de etiquetas más usadas

**Explicación:**  
En Django es común combinar **Python** con **HTML** dentro de las vistas.  
- En Python utilizamos **f-Strings** para insertar valores dinámicos en cadenas de texto.  
- Dentro de esas cadenas podemos incluir **etiquetas HTML**, que son las que finalmente se renderizan en el navegador.  
- En el Módulo 1, trabajando con **Reflex**, ya vimos cómo los f-Strings eran frecuentes para generar contenido dinámico.  
- En Django ocurre algo similar: usamos etiquetas HTML para construir listas (`<ul>`, `<li>`) y enlaces (`<a>`), mezclando la lógica de Python con el marcado HTML que define la estructura visual.

De esta manera, Django nos permite **unir la lógica del servidor con la presentación en el navegador**, generando páginas dinámicas que muestran datos en tiempo real.

La siguiente tabla resume las etiquetas más utilizadas y su propósito:

#### Tabla de etiquetas HTML más usadas

| Etiqueta | Uso principal | Ejemplo compacto |
|----------|---------------|------------------|
| `<h1>`   | Título principal | `<h1>Bienvenido</h1>` |
| `<p>`    | Párrafo de texto | `<p>Este es un párrafo.</p>` |
| `<a>`    | Hipervínculo | `<a href="/contacto">Contacto</a>` |
| `<ul>`   | Lista desordenada | `<ul><li>Item</li></ul>` |
| `<ol>`   | Lista ordenada | `<ol><li>Primero</li></ol>` |
| `<li>`   | Elemento de lista | `<li>Producto</li>` |
| `<div>`  | Contenedor genérico | `<div>Contenido</div>` |
| `<span>` | Texto en línea | `<span>Etiqueta</span>` |
| `<img>`  | Imagen | `<img src="foto.jpg" alt="Foto">` |
| `<form>` | Formulario | `<form><input type="text"></form>` |

---

### Ejemplo compacto en HTML
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Ejemplo compacto</title>
  </head>
  <body>
    <h1>Lista de productos</h1>
    <p>Selecciona un producto para ver detalles:</p>
    <ul>
      <li><a href="/productos/1/">Laptop</a></li>
      <li><a href="/productos/2/">Impresora</a></li>
      <li><a href="/productos/3/">Monitor</a></li>
    </ul>
    <img src="logo.png" alt="Logo de la tienda">
  </body>
</html>
```

---

#### PASO 2 — Actualizar `productos/views.py`

```python
"""Vistas de la aplicacion productos — Semana 2.

Agrega lista de productos y detalle con parametro de URL.
Hilo conector: "Conectar las piezas".
"""

from django.http import HttpRequest, HttpResponse

# Datos de ejemplo (sin base de datos — se incorpora en Semana 4)
PRODUCTOS_EJEMPLO: dict[int, dict] = {
    1: {"nombre": "Teclado USB",         "precio": 350.00},
    2: {"nombre": "Monitor 24 pulgadas", "precio": 3200.00},
    3: {"nombre": "Mouse inalambrico",   "precio": 280.00},
}


def bienvenida(request: HttpRequest) -> HttpResponse:
    """Devuelve la pagina principal del sistema.

    Args:
        request: Objeto HttpRequest generado por Django.

    Returns:
        HttpResponse con enlaces a las vistas disponibles.
    """
    html = (
        "<h1>Sistema de Inventario</h1>"
        "<ul>"
        "<li><a href='/productos/'>Ver lista de productos</a></li>"
        "<li><a href='/productos/1/'>Ejemplo: detalle producto 1</a></li>"
        "</ul>"
    )
    return HttpResponse(html)


def lista_productos(request: HttpRequest) -> HttpResponse:
    """Devuelve la lista completa de productos de ejemplo.

    Args:
        request: Objeto HttpRequest generado por Django.

    Returns:
        HttpResponse con un listado HTML de todos los productos.
    """
    items = "".join(
        f"<li><a href='/productos/{pid}/'>{datos['nombre']}</a></li>"
        for pid, datos in PRODUCTOS_EJEMPLO.items()
    )
    html = f"<h1>Lista de productos ({len(PRODUCTOS_EJEMPLO)})</h1><ul>{items}</ul>"
    return HttpResponse(html)


def detalle_producto(request: HttpRequest, producto_id: int) -> HttpResponse:
    """Devuelve el detalle de un producto segun su ID de URL.

    Args:
        request: Objeto HttpRequest generado por Django.
        producto_id: Identificador entero capturado desde la URL.

    Returns:
        HttpResponse 200 con el detalle del producto, o 404 si no existe.
    """
    producto = PRODUCTOS_EJEMPLO.get(producto_id)
    if producto is None:
        return HttpResponse(
            f"<h1>Producto {producto_id} no encontrado</h1>",
            status=404,
        )
    html = (
        f"<h1>{producto['nombre']}</h1>"
        f"<p>Precio: ${producto['precio']:.2f}</p>"
        f"<p><a href='/productos/'>Volver a la lista</a></p>"
    )
    return HttpResponse(html)
```
---

#### PASO 3 — Actualizar `productos/urls.py`

```python
"""URLs de la aplicacion productos — Semana 2."""

from django.urls import path
from . import views

app_name = "productos"          # namespace: evita colisiones entre apps

urlpatterns = [
    path("",                             views.bienvenida,       name="bienvenida"),
    path("productos/",                   views.lista_productos,  name="lista"),
    path("productos/<int:producto_id>/", views.detalle_producto, name="detalle"),
]
```

---

#### PASO 4 — Actualizar `inventario_proyecto/urls.py`

```python
"""URLs del proyecto inventario_proyecto — Semana 2."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",       include("productos.urls", namespace="productos")),
]
```

---

#### PASO 5 — Verificar y ejecutar

```bash
python3 manage.py check
# Verificacion esperada: "System check identified no issues (0 silenced)."

python3 manage.py runserver
# Abrir en el navegador:
#   http://127.0.0.1:8000/           → bienvenida con enlaces
#   http://127.0.0.1:8000/productos/ → lista de 3 productos
#   http://127.0.0.1:8000/productos/2/ → Monitor 24 pulgadas, $3200.00
#   http://127.0.0.1:8000/productos/99/ → status 404, "no encontrado"
```

---

#### PASO 6 — Sprint 1 Planning (S2)

Crea el archivo `sprint1_planning.md` en la raíz del proyecto:

```markdown
# Sprint 1 Planning — Sistema de Inventario
## Fecha: ___________  |  Duración: 1 semana

### Sprint Goal
"Al finalizar el sprint, el sistema mostrará la lista de productos
 y el detalle de cada uno accesible por URL."

### Historias de usuario seleccionadas del backlog
| ID     | Historia                                         | Estimación |
|--------|--------------------------------------------------|------------|
| HU-01  | Ver lista de productos                           | ___ pts    |
| HU-01a | Ver detalle de un producto por su ID             | ___ pts    |

### Plan de trabajo
| Tarea                            | Responsable | Estado   |
|----------------------------------|-------------|----------|
| Implementar vista lista_productos | ___         | En curso |
| Implementar vista detalle_producto | ___        | En curso |
| Configurar URL namespace          | ___         | En curso |
| Commit + push a la rama sprint1   | ___         | Pendiente |

### Rama de Git
`sprint1/lista-detalle-productos`
```

---

#### Entregables (versionado — Sprint 1)

```bash
git add productos/views.py productos/urls.py inventario_proyecto/urls.py
git add sprint1_planning.md
git commit -m "Sprint 1: vistas lista y detalle con URL namespace"
git push origin sprint1/lista-detalle-productos
```

> **Fallback sin conexión:** omite `git push`. El commit local es válido; publica después con `git push origin sprint1/lista-detalle-productos`.

---

### 3.9 Análisis (5 preguntas de reflexión)

1. ¿Qué pasaría si Django recibiera la URL `/productos/abc/` con el patrón `<int:producto_id>/`? ¿Por qué?
2. ¿Para qué sirve el `app_name` en `urls.py` y qué problema resuelve cuando el proyecto crece?
3. ¿En qué se parecen el Sprint Goal de Scrum y el hilo conector de la semana en esta guía?
4. ¿Por qué se trabaja en una rama `sprint1/...` en lugar de hacer commits directamente en `main`?
5. La vista `detalle_producto` devuelve status 404 cuando el producto no existe. ¿Qué tipo de prueba unitaria escribirías para verificarlo automáticamente?

### 3.10 Conclusiones

Esta semana el estudiante comprendió que Django no es solo "una caja que devuelve texto", sino un enrutador que conecta URLs con funciones y parámetros con argumentos. Esa misma lógica de conexión la ejerció en Scrum: el Sprint Planning conecta el backlog con el trabajo concreto del sprint. Las semanas siguientes añadirán plantillas (Semana 3) y modelos de base de datos (Semana 4) —las dos piezas que faltan para que el sistema de inventario deje de usar datos de ejemplo y trabaje con datos reales.

---

## 4. PARTE II — Momentos didácticos (Sergio Tobón)

### 4.1 Momento 1 — Apertura
Revisión del Sprint 0: ¿el proyecto de la Semana 1 pasa `manage.py check`? ¿El Product Backlog tiene al menos cinco historias? El docente introduce el concepto de URL dispatcher con un diagrama en el pizarrón (petición → urls.py → view → response) y presenta los cinco eventos de Scrum.

### 4.2 Momento 2 — Desarrollo
Codificación guiada de `lista_productos` y `detalle_producto`; configuración del *namespace*; prueba de las cuatro URLs en el navegador o con `check`. En paralelo, redacción del `sprint1_planning.md` con Sprint Goal y selección de HUs.

### 4.3 Momento 3 — Cierre
Commit del Sprint 1 en su rama, subida a Classroom (código + planning) y respuesta a las 5 preguntas de análisis. Coevaluación breve en parejas: verificar que la URL `/productos/99/` devuelva 404.

---

## 5. Estrategia de evaluación de la semana

| Evidencia | Submódulo | Instrumento | Ponderación |
|---|---|---|---|
| `lista_productos` y `detalle_producto` funcionando (200 y 404 correctos) | S1 | Rúbrica de código (PEP 8, docstrings, verifica) | 35 % |
| URL namespace (`app_name`) configurado | S1 | Verificación directa en `urls.py` | 10 % |
| `sprint1_planning.md` con Sprint Goal + HUs + tareas | S2 | Lista de cotejo | 35 % |
| Respuestas de análisis (5 preguntas) | Transversal | Lista de cotejo | 20 % |

---

## 6. Recursos didácticos

- Proyecto Django de la Semana 1 en repositorio Git.
- Computadora con Python 3.11+, Django 4.2 y VS Code.
- Navegador web para verificar rutas.
- GitHub Projects o Trello para el tablero Kanban (opcional esta semana).
- Google Classroom para entrega de evidencias.

---

## 7. Referencias (APA 7)

Django Software Foundation. (s.f.). *URL dispatcher*. https://docs.djangoproject.com/en/4.2/topics/http/urls/

Django Software Foundation. (s.f.). *Writing views*. https://docs.djangoproject.com/en/4.2/topics/http/views/

Fowler, M. (2003). *Patterns of enterprise application architecture*. Addison-Wesley.

Schwaber, K., & Sutherland, J. (2020). *La guía de Scrum*. https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf

---

*Guía generada bajo ROL 2 — Asesor Académico Experto · Prompt Maestro v1.0 · Una semana a la vez.*
*Parámetros respetados: 13 semanas · submódulos y horas SEP sin modificar · cita narrativa · código verificado (4 aserciones: 200 bienvenida, 200 lista, 200 detalle ID=2, 404 detalle ID=99).*
