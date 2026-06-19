# Módulo II · Semana 4 — Guía Académica y de Laboratorio
## Técnico en Programación (SEP 3061300006-23) · UTEC Celaya
### Asesor: MC. Román Fernando López González

---

## 1. Identificación de la semana

| Campo | Detalle |
|---|---|
| Carrera | Técnico en Programación |
| Módulo | II — Desarrolla software con herramientas orientadas a la productividad (272 h) |
| Semana | 4 de 13 |
| Submódulos integrados | S1 Frameworks (144 h) · S2 Metodologías ágiles (128 h) |
| **Hilo conector de la semana** | **"Modelar el dominio"** |
| Stack | Django 4.2 LTS · ORM · SQLite · Python 3.11+ |
| Carga horaria reportada | 17 h/semana (S1 = 9 h · S2 = 8 h) |
| Carga horaria real (planeación) | 14.16 h/semana |
| Tiempo fantasma máximo | 15 min/día |
| Plataforma institucional | Google Classroom |
| Prerrequisito | Semana 3 — plantillas con herencia + Sprint 1 cerrado en `main` |

> **Hilo conector:** un **modelo** Django define los campos que describen un producto (nombre, precio, stock); un **Sprint Backlog** define los ítems que describen el trabajo del sprint. Ambos son planos que preceden a la construcción: el modelo antes de escribir datos, el backlog antes de escribir código. Esta semana el estudiante traza los dos planos y comprueba que el dominio, modelado correctamente, produce CRUD gratuito a través del panel admin.

---

## 2. Competencias de la semana

**Resultado de aprendizaje (SEP):**
El estudiante define modelos Django, ejecuta migraciones, registra el modelo en el panel admin y actualiza las vistas para usar el ORM; en paralelo, estima historias de usuario con puntos de historia y construye el Sprint 2 backlog con un tablero Kanban.

**Actividades clave de la competencia laboral:**

- **S1 — Frameworks:** Define `Producto` en `models.py`; ejecuta `makemigrations` y `migrate`; registra el modelo en `admin.py`; actualiza vistas para usar `Producto.objects.all()` y `Producto.objects.get(pk=id)`.
- **S2 — Metodologías ágiles:** Estima historias del backlog con puntos de historia (escala Fibonacci); construye el Sprint 2 backlog (`sprint2_planning.md`); configura el tablero Kanban en GitHub Projects con columnas To Do / In Progress / Done.

---

## 3. PARTE I — Estructura académica (modelo Corina Schmelkes)

### 3.1 Introducción

Hasta la Semana 3, el sistema de inventario operaba con un diccionario Python cargado en memoria: los datos desaparecían al detener el servidor. Django resuelve esto a través del ORM (*Object-Relational Mapper*): el desarrollador escribe clases Python y Django las traduce automáticamente a tablas SQL, sin necesidad de escribir una sola instrucción `CREATE TABLE`. Fowler (2003) describe el patrón ORM como un mapeador que elimina el *impedance mismatch* —la diferencia conceptual entre el mundo de objetos y el mundo relacional—. Por el lado metodológico, Cohn (2005) argumenta que estimar el esfuerzo relativo de cada historia —en lugar de horas absolutas— permite planear sprints sostenibles, porque los puntos de historia capturan la complejidad del trabajo sin depender de la velocidad individual del desarrollador. Esta semana ambos planos se trazan juntos.

### 3.2 Planteamiento del problema

El sistema tiene vistas y plantillas que funcionan, pero los datos son estáticos. Cualquier producto "creado" durante la clase desaparece al reiniciar. ¿Cómo persistir los datos sin abandonar Python ni aprender SQL desde cero? Y en el plano ágil: ¿cómo el equipo decide cuánto trabajo cabe en un sprint antes de comprometerse?

### 3.3 Justificación

El ORM de Django resuelve la persistencia con una abstracción que el estudiante ya conoce: las clases Python. Fowler (2003) demuestra que este patrón reduce la superficie de errores al centralizar el acceso a datos. Por su parte, Cohn (2005) muestra que los puntos de historia son más estables que las estimaciones en horas porque se calibran por comparación entre historias —si HU-01 (lista simple) vale 1 punto, HU-02 (formulario de creación) vale 3—. Cuando el equipo conoce su velocidad promedio, puede comprometerse con precisión.

### 3.4 Objetivos

**General:** Que el estudiante defina el modelo `Producto`, ejecute migraciones, opere el admin de Django y estime el Sprint 2 backlog con puntos de historia.

**Específicos:**
1. Definir los campos del modelo `Producto` con tipos Django apropiados (S1).
2. Ejecutar `makemigrations` y `migrate`; interpretar el archivo de migración generado (S1).
3. Registrar `Producto` en `admin.py` con `list_display` y `search_fields` (S1).
4. Actualizar las vistas para usar `Producto.objects.all()` y `Producto.objects.get()` (S1).
5. Estimar las historias del backlog con escala Fibonacci y construir el Sprint 2 Planning (S2).

### 3.5 Marco teórico (con código)

**El ORM de Django: clase → tabla.** Fowler (2003) describe el ORM como un traductor entre el modelo de objetos y el modelo relacional. En Django, cada clase que hereda de `models.Model` se convierte en una tabla; cada atributo de clase es una columna:

```python
# El ORM traduce esto...
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

# ...en SQL equivalente a:
# CREATE TABLE productos_producto (
#     id      INTEGER PRIMARY KEY AUTOINCREMENT,
#     nombre  VARCHAR(200) NOT NULL,
#     precio  DECIMAL(10,2) NOT NULL
# );
# Django genera el SQL; el desarrollador nunca lo escribe.
```

**Tipos de campo más usados:**

```python
models.CharField(max_length=N)        # texto corto (VARCHAR)
models.DecimalField(max_digits, decimal_places)  # decimal exacto
models.IntegerField(default=0)        # entero
models.DateTimeField(auto_now_add=True)  # fecha/hora automática al crear
models.BooleanField(default=True)     # verdadero/falso
models.TextField()                    # texto largo
```

**El ciclo de migraciones.** La documentación oficial de Django (Django Software Foundation, s.f.) describe las migraciones como "el sistema de control de versiones para el esquema de la base de datos":

```bash
# 1. Detectar cambios en models.py y generar el archivo de migración
python3 manage.py makemigrations productos
# Resultado: productos/migrations/0001_initial.py

# 2. Aplicar la migración a la base de datos
python3 manage.py migrate

# 3. Ver el estado de las migraciones
python3 manage.py showmigrations productos
# [X] 0001_initial   ← aplicada
```

**Consultas ORM más usadas en las vistas:**

```python
from .models import Producto

# Todos los productos (SELECT * FROM ...)
Producto.objects.all()

# Filtrar (SELECT ... WHERE precio <= 400)
Producto.objects.filter(precio__lte=400)

# Obtener uno por clave primaria (lanza DoesNotExist si no existe)
Producto.objects.get(pk=producto_id)

# Ordenar
Producto.objects.order_by("nombre")

# Contar
Producto.objects.count()

# Verificacion esperada:
# Producto.objects.filter(precio__lte=400).count() == 2
# (Teclado $350 y Mouse $280; Monitor $3200 excluido)
```

**Estimación con puntos de historia.** Cohn (2005) propone la escala de Fibonacci (1, 2, 3, 5, 8, 13) porque los saltos no lineales reflejan la incertidumbre creciente al estimar tareas grandes. La regla es: comparar cada historia con una historia de referencia conocida, no con horas de reloj.

| Historia | Complejidad relativa | Puntos |
|---|---|---|
| HU-00: Instalar Django + hola mundo | Referencia mínima | 1 |
| HU-01: Vista lista con plantilla | Un poco más complejo | 2 |
| HU-02: Modelo + admin + migración | Más piezas que HU-01 | 3 |
| HU-03: Formulario de creación | Más complejo que HU-02 | 5 |
| HU-08: Autenticación y sesiones | Significativamente más complejo | 8 |

### 3.6 Metodología

Trabajo guiado e individual con computadora por alumno. La sesión define el modelo → genera la migración → verifica en la BD → registra en admin → crea el superusuario → opera el CRUD desde el panel → actualiza las vistas. En paralelo, el equipo estima el backlog y lanza el Sprint 2.

### 3.7 Desarrollo temático

**S1 — Frameworks (≈9 h reportadas)**
1. Concepto ORM: clase → tabla; atributos → columnas; `id` automático.
2. Tipos de campo Django más usados.
3. `class Meta`: `verbose_name`, `ordering`.
4. `__str__`: representación legible del modelo.
5. Ciclo de migraciones: `makemigrations` → `migrate` → `showmigrations`.
6. `admin.py`: `@admin.register`, `list_display`, `search_fields`, `list_filter`.
7. `createsuperuser` y acceso al panel.
8. Actualizar vistas con `objects.all()` y `objects.get(pk=)`.

**S2 — Metodologías ágiles (≈8 h reportadas)**
1. Puntos de historia: escala Fibonacci, referencia relativa.
2. Planning Poker: estimación en equipo.
3. Velocidad del equipo: cómo calibrar el sprint.
4. Sprint 2 backlog: selección y estimación de HU-02 y HU-03.
5. Tablero Kanban: columnas To Do / In Progress / Done en GitHub Projects.

### 3.8 Práctica de laboratorio

**Objetivo:** definir el modelo `Producto`, migrarlo, operar el admin con datos reales y actualizar las vistas para que usen el ORM.

---

#### PASO 1 — Definir el modelo (`productos/models.py`)

```python
"""Modelos del dominio — Semana 4.

Define la entidad Producto como clase Python que Django
traduce automaticamente a una tabla en la base de datos.
Hilo conector: "Modelar el dominio".
"""

from decimal import Decimal

from django.db import models


class Producto(models.Model):
    """Representa un producto en el sistema de inventario.

    Attributes:
        nombre: Nombre descriptivo del producto.
        precio: Precio unitario con hasta 2 decimales.
        stock: Cantidad disponible en inventario.
        creado: Fecha y hora de alta, asignada automaticamente.
    """

    nombre = models.CharField(
        max_length=200,
        verbose_name="Nombre",
    )
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Precio",
    )
    stock = models.IntegerField(
        default=0,
        verbose_name="Stock",
    )
    creado = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de alta",
    )

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre"]

    def __str__(self) -> str:
        """Devuelve representacion legible del producto.

        Returns:
            Cadena con nombre y precio formateado a 2 decimales.
        """
        precio_dec = Decimal(str(self.precio))
        return f"{self.nombre} (${precio_dec:.2f})"
```

---

#### PASO 2 — Migraciones

```bash
python3 manage.py makemigrations productos
# Resultado esperado:
# Migrations for 'productos':
#   productos/migrations/0001_initial.py
#     - Create model Producto

python3 manage.py migrate
# Resultado esperado: OK en cada migración aplicada

python3 manage.py showmigrations productos
# Resultado esperado:
# productos
#  [X] 0001_initial
```

---

#### PASO 3 — Registrar en el admin (`productos/admin.py`)

```python
"""Registro del modelo Producto en el panel de administracion."""

from django.contrib import admin

from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """Configuracion del modelo Producto en el admin de Django.

    Attributes:
        list_display: columnas visibles en la lista.
        search_fields: campos en los que actua el buscador.
        list_filter: filtros laterales en el panel.
    """

    list_display = ["nombre", "precio", "stock", "creado"]
    search_fields = ["nombre"]
    list_filter = ["creado"]
```

---

#### PASO 4 — Crear superusuario y probar el admin

```bash
python3 manage.py createsuperuser
# Ingresar: nombre de usuario, correo (opcional), contraseña

python3 manage.py runserver
# Abrir: http://127.0.0.1:8000/admin/
# Verificacion esperada:
#   - Aparece la sección "PRODUCTOS" con el modelo "Productos"
#   - Se pueden crear, editar y eliminar productos desde el panel
#   - La lista muestra columnas: nombre | precio | stock | fecha de alta
#   - El buscador filtra por nombre
```

---

#### PASO 5 — Actualizar las vistas para usar el ORM (`productos/views.py`)

```python
"""Vistas de la aplicacion productos — Semana 4.

Reemplaza el diccionario de ejemplo por consultas ORM reales.
Hilo conector: "Modelar el dominio".
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Producto


def bienvenida(request: HttpRequest) -> HttpResponse:
    """Devuelve la pagina principal del sistema.

    Args:
        request: Objeto HttpRequest generado por Django.

    Returns:
        HttpResponse renderizado con base.html.
    """
    return render(request, "base.html", {"titulo": "Bienvenido"})


def lista_productos(request: HttpRequest) -> HttpResponse:
    """Devuelve todos los productos desde la base de datos.

    Args:
        request: Objeto HttpRequest generado por Django.

    Returns:
        HttpResponse renderizado con productos/lista.html.
    """
    productos = Producto.objects.all()
    return render(request, "productos/lista.html", {"productos": productos})


def detalle_producto(request: HttpRequest, producto_id: int) -> HttpResponse:
    """Devuelve el detalle de un producto usando el ORM.

    Args:
        request: Objeto HttpRequest generado por Django.
        producto_id: Clave primaria del producto (capturada desde la URL).

    Returns:
        HttpResponse renderizado con productos/detalle.html (200),
        o HttpResponse de error (404) si el producto no existe.
    """
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        return HttpResponse(
            f"<h1>Producto {producto_id} no encontrado</h1>",
            status=404,
        )
    return render(
        request,
        "productos/detalle.html",
        {"producto": producto},
    )
```

---

#### PASO 6 — Actualizar las plantillas para usar atributos del modelo

En `lista.html`, cambiar la iteración del diccionario a objetos del modelo:

```html
{% block content %}
<h2>Productos ({{ productos|length }})</h2>
<ul>
{% for p in productos %}
    <li>
        <a href="/productos/{{ p.pk }}/">{{ p.nombre }}</a>
        — ${{ p.precio }} | Stock: {{ p.stock }}
    </li>
{% empty %}
    <li>No hay productos. <a href="/admin/productos/producto/add/">Agregar uno</a>.</li>
{% endfor %}
</ul>
{% endblock %}
```

En `detalle.html`, añadir el campo `stock`:

```html
{% block content %}
<h2>{{ producto.nombre }}</h2>
<p><strong>Precio:</strong> ${{ producto.precio }}</p>
<p><strong>Stock:</strong> {{ producto.stock }} unidades</p>
<p><a href="/productos/">← Volver a la lista</a></p>
{% endblock %}
```

---

#### PASO 7 — Sprint 2 Planning (S2)

Crea `sprint2_planning.md` en la raíz del proyecto:

```markdown
# Sprint 2 Planning — Sistema de Inventario
## Fecha: ___________ | Duración: 3 semanas (Sem 4–6)

### Sprint Goal
"Al finalizar el sprint, el administrador puede gestionar productos
 completos (crear, editar, eliminar) desde el panel admin y a través
 de formularios propios, con datos persistidos en la base de datos."

### Velocidad estimada del equipo: ___ puntos

### Historias seleccionadas del backlog
| ID     | Historia                                     | Puntos | Estado    |
|--------|----------------------------------------------|--------|-----------|
| HU-BD  | Modelo Producto + migraciones + ORM          | 3      | ✅ Hecho  |
| HU-02  | Panel admin: registrar y editar productos    | 2      | En curso  |
| HU-03  | Formulario propio: crear producto (sem 5)    | 5      | To Do     |
| HU-04  | Formulario propio: editar producto (sem 6)   | 5      | To Do     |

### Tablero Kanban (GitHub Projects)
Columnas: Backlog | To Do | In Progress | Done
Mover HU-02 a "In Progress" al arrancar la sesión.

### Rama de Git
`sprint2/modelos-orm`
```

---

#### Entregables — Sprint 2 arranca

```bash
git checkout main
git checkout -b sprint2/modelos-orm
git add productos/models.py productos/admin.py productos/views.py
git add productos/migrations/ productos/templates/ sprint2_planning.md
git commit -m "Sprint 2: modelo Producto + ORM + admin + Sprint 2 Planning"
git push origin sprint2/modelos-orm
```

> **Fallback sin conexión:** omite `git push`. El commit local es válido.

---

### 3.9 Análisis (5 preguntas de reflexión)

1. ¿Qué ventaja tiene usar `Producto.objects.get(pk=id)` con `try/except DoesNotExist` en lugar de `filter(pk=id).first()`?
2. ¿Por qué Django genera un archivo de migración (`.py`) en lugar de ejecutar el SQL directamente? ¿Qué ventaja da ese archivo?
3. El panel admin provee CRUD completo sin escribir una sola vista. ¿En qué se parece esto al concepto de "velocidad" en Scrum: obtener valor sin invertir más esfuerzo?
4. Asigna puntos de historia a HU-05 (búsqueda de productos). Justifica tu estimación comparándola con HU-02 y HU-03.
5. ¿Qué columna de tu tablero Kanban corresponde al `{% empty %}` de la plantilla de lista? Explica la analogía.

### 3.10 Conclusiones

Con el modelo `Producto` en la base de datos, el sistema de inventario dejó de ser un prototipo: ahora los datos persisten entre sesiones y el panel admin provee CRUD completo sin código adicional. El Sprint 2 backlog documenta cuánto trabajo queda —formularios propios— y la estimación en puntos permite al equipo comprometerse con la semana siguiente sin sobreestimar. Las Semanas 5 y 6 construirán esos formularios, cerrando el ciclo de lectura y escritura con código Python propio.

---

## 4. PARTE II — Momentos didácticos (Sergio Tobón)

### 4.1 Momento 1 — Apertura
Planteamiento del problema: "reinicia el servidor — ¿dónde están los productos que creaste la semana pasada?". El docente introduce el ORM con el diagrama clase → tabla en el pizarrón. Introduce la escala Fibonacci con un ejemplo de estimación relativa.

### 4.2 Momento 2 — Desarrollo
Codificación guiada de `models.py` → `makemigrations` → `migrate` → `admin.py` → `createsuperuser` → operar el admin con datos reales → actualizar vistas con ORM. En paralelo, estimar las historias del backlog y redactar `sprint2_planning.md`.

### 4.3 Momento 3 — Cierre
Verificar las 8 aserciones (modelo, `__str__`, ordering, filter, lista ORM, detalle, 404, admin), commit del Sprint 2, subida a Classroom y respuesta a las preguntas de análisis.

---

## 5. Estrategia de evaluación de la semana

| Evidencia | Submódulo | Instrumento | Ponderación |
|---|---|---|---|
| `models.py` con 4 campos, `Meta`, `__str__` correctos | S1 | Rúbrica de modelo | 25 % |
| `makemigrations` + `migrate` exitosos; `[X] 0001_initial` | S1 | Verificación `showmigrations` | 15 % |
| Admin operando: lista + búsqueda + CRUD desde panel | S1 | Captura de pantalla | 20 % |
| Vistas actualizadas con `objects.all()` y `objects.get()` | S1 | Lista de cotejo | 10 % |
| `sprint2_planning.md` con Sprint Goal + historias estimadas | S2 | Lista de cotejo | 20 % |
| Respuestas de análisis (5 preguntas) | Transversal | Lista de cotejo | 10 % |

---

## 6. Recursos didácticos

- Proyecto Django de la Semana 3 en `main` (Sprint 1 cerrado).
- Computadora con Python 3.11+, Django 4.2 y VS Code.
- Navegador web para el panel admin (`/admin/`).
- GitHub Projects (o Trello) para el tablero Kanban.
- Google Classroom para entrega de evidencias.

---

## 7. Referencias (APA 7)

Cohn, M. (2005). *Agile estimating and planning*. Prentice Hall.

Django Software Foundation. (s.f.). *Models*. https://docs.djangoproject.com/en/4.2/topics/db/models/

Django Software Foundation. (s.f.). *The Django admin site*. https://docs.djangoproject.com/en/4.2/ref/contrib/admin/

Django Software Foundation. (s.f.). *Migrations*. https://docs.djangoproject.com/en/4.2/topics/migrations/

Fowler, M. (2003). *Patterns of enterprise application architecture*. Addison-Wesley.

Schwaber, K., & Sutherland, J. (2020). *La guía de Scrum*. https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf

---

*Guía generada bajo ROL 2 — Asesor Académico Experto · Prompt Maestro v1.0 · Una semana a la vez.*
*Parámetros respetados: 13 semanas · submódulos y horas SEP sin modificar · cita narrativa.*
*Código verificado: 8 aserciones (modelo, __str__, ordering, filter ORM, lista 3 prod., detalle, 404, admin list_display).*
