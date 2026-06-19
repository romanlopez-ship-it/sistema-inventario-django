# Guía de Observación — Semana 1, Módulo II: Técnico en Programación
**Alumno:** ___________________________  
**Fecha:** ___________________________  
**Módulo:** Técnico en Programación (clave 3061300006-23) — Módulo II  
**Sprint:** Sprint 0 — "Del lenguaje al framework"

---

## 1. Infraestructura Portable (USB → PC → USB)

### Objetivo
Trabajar en cualquier computadora sin instalar nada en el sistema anfitrión y proteger la vida útil de la USB.

### Estructura creada en la USB

```
USB_Drive/
├── Python_Portable/        → Intérprete Python 3.11 embeddable (motor autónomo)
├── Git_Portable/           → Git for Windows Portable
└── WorkSpace/              → Respaldo del proyecto (código + db.sqlite3 + .git)
```

### Scripts de sesión

| Archivo | Función | Ubicación |
|---|---|---|
| `iniciar_sesion.bat` | Copia proyecto USB → `C:\Temp_Workspace_M2` y configura PATH | Raíz de la USB |
| `finalizar_sesion.bat` | Copia proyecto `C:\Temp_Workspace_M2` → USB | Raíz de la USB |

> **Regla de oro:** Nunca se trabaja directo en la USB. El "taller" es `C:\Temp_Workspace_M2`; la USB es la "caja fuerte".

### Verificaciones realizadas

- [x] `Python_Portable/` contiene el intérprete Python 3.11 con `import site` habilitado en `python311._pth`
- [x] `WorkSpace/` existe como carpeta (no como archivo)
- [x] `iniciar_sesion.bat` copia correctamente a la PC
- [x] `finalizar_sesion.bat` regresa los archivos a la USB
- [x] Prueba de fuego: archivo `HelloWorld.py` creado en PC y sincronizado a USB

---

## 2. Stack Tecnológico Instalado

```bash
python -m pip install "django==4.2" djangorestframework whitenoise gunicorn
```

| Herramienta | Versión | Propósito |
|---|---|---|
| Django | 4.2 LTS | Framework web principal |
| Django REST Framework | Última estable | APIs REST (Semanas 10-11) |
| WhiteNoise | Última estable | Archivos estáticos en producción |
| Gunicorn | Última estable | Servidor WSGI para despliegue |

### Verificación

```bash
python -m django --version   # Debe mostrar: 4.2.x
python manage.py check       # Debe mostrar: System check identified no issues (0 silenced).
```

---

## 3. Estructura del Proyecto Django (Sprint 0)

```
C:\Temp_Workspace_M2\
├── manage.py
├── db.sqlite3                   ← Base de datos SQLite (portable)
├── product_backlog.md           ← Artefacto Scrum
├── sprint0_planning.md          ← Artefacto Scrum
├── inventario_proyecto\
│   ├── settings.py              ← 'productos' registrado en INSTALLED_APPS
│   ├── urls.py                  ← include('productos.urls')
│   ├── wsgi.py
│   └── asgi.py
├── productos\
│   ├── views.py                 ← Función bienvenida() con HttpResponse
│   ├── urls.py                  ← path('', views.bienvenida, name='bienvenida')
│   ├── models.py
│   ├── admin.py
│   └── apps.py
└── env_inventario\              ← Entorno virtual (NO se respalda en USB)
    └── Scripts\
        └── activate
```

### Comandos de creación ejecutados

```bash
django-admin startproject inventario_proyecto .
python manage.py startapp productos
python manage.py migrate
python manage.py runserver
```

---

## 4. Patrón MVT — Flujo de una Petición

```
Navegador → URL Dispatcher → Vista → Modelo → Plantilla → Navegador
             urls.py          views.py  models.py  *.html
```

| Capa | Archivo | Responsabilidad |
|---|---|---|
| **Modelo (M)** | `productos/models.py` | Define estructura de datos y ORM |
| **Vista (V)** | `productos/views.py` | Lógica de negocio y respuesta |
| **Plantilla (T)** | `templates/*.html` | Presentación (HTML dinámico) |
| **Enrutador** | `*/urls.py` | Conecta URL con Vista correcta |

### Vista de bienvenida implementada

```python
# productos/views.py
from django.http import HttpResponse

def bienvenida(request):
    """Vista inicial del sistema de inventario."""
    return HttpResponse("<h1>Sistema de Inventario - Sprint 0</h1>")
```

### Errores encontrados y solución

| Error | Causa | Solución aplicada |
|---|---|---|
| `ImportError: cannot import 'views' from 'inventario_proyecto'` | `from . import views` puesto en el urls.py del proyecto, no en el de la app | Mover al `productos/urls.py` |
| `ModuleNotFoundError: No module named 'productos.urls'` | El archivo `urls.py` no existía dentro de `productos/` | Crear `productos/urls.py` manualmente |

---

## 5. Artefactos Scrum Generados

### 5.1 Product Backlog (`product_backlog.md`)

| ID | Historia de Usuario | Prioridad | Puntos |
|---|---|---|---|
| HU-01 | Ver lista de productos | Alta | 2 |
| HU-01a | Ver detalle de un producto | Alta | 2 |
| HU-02 | Registrar un nuevo producto | Media | 3 |
| HU-03 | Editar datos de un producto | Media | 3 |
| HU-04 | Eliminar productos obsoletos | Baja | 5 |
| HU-05 | Sistema de autenticación (login/logout) | Alta | 8 |

**Roles del equipo:**
- **Product Owner:** Docente
- **Scrum Master:** Alumno
- **Equipo de Desarrollo:** Alumno

### 5.2 Criterios de Aceptación (formato Gherkin)

**HU-01 — Ver lista de productos:**
```gherkin
Dado que existen 3 productos en la base de datos
Cuando el usuario navega a /productos/
Entonces el sistema responde HTTP 200 y muestra los 3 artículos
```

**HU-02 — Registrar un producto:**
```gherkin
Dado que el formulario está vacío
Cuando el usuario llena nombre, precio y stock y envía el formulario
Entonces el producto aparece en la lista y la base de datos tiene un registro más
```

### 5.3 Sprint 0 Planning (`sprint0_planning.md`)

**Sprint Goal:** Establecer la infraestructura técnica de Django y el marco ágil (Scrum) para el sistema de inventario.

**Definición de Terminado (DoD):**
- `python manage.py check` sin errores
- Vista de bienvenida responde HTTP 200
- Código sigue PEP 8
- Artefactos publicados en GitHub

---

## 6. Control de Versiones Git

### Flujo de trabajo

```bash
git init
git add .
git commit -m "Sprint 0: Infraestructura MVT corregida y funcional"
git remote add origin https://github.com/usuario/sistema-inventario-django.git
git branch -M main
git push -u origin main
```

### Convención de ramas

| Rama | Propósito |
|---|---|
| `main` | Línea base estable (entregable final) |
| `sprint1/crud-basico` | Trabajo del Sprint 1 |
| `sprint2/...` | Trabajo del Sprint 2 |

### Estado al cierre de Semana 1

- [x] Repositorio local inicializado
- [x] Primer commit realizado
- [x] Push a GitHub exitoso
- [x] Respaldo en USB ejecutado con `finalizar_sesion.bat`

---

## 7. Ciclo de Trabajo Diario

```
1. Conectar USB
2. Ejecutar iniciar_sesion.bat  → Copia USB a C:\Temp_Workspace_M2
3. Activar entorno virtual:
       env_inventario\Scripts\activate
4. Trabajar (Django corre desde la PC, no desde la USB)
5. Al terminar:
       git add .
       git commit -m "Descripción del avance"
       (opcional) git push origin main
6. Ejecutar finalizar_sesion.bat → Copia C:\Temp_Workspace_M2 a USB
7. Retirar USB
```

---

## 8. Avance vs. Cronograma de la Semana 1

| Día | Objetivo según plan | Estado |
|---|---|---|
| Lunes | Instalar Django, crear proyecto y app | ✅ Completado |
| Martes | Vista de bienvenida + urls.py funcional | ✅ Completado |
| Miércoles | `migrate` + Product Backlog + primer commit | ✅ Completado |
| Jueves | Push a GitHub + Sprint 0 Planning | ✅ Completado |
| Viernes | Sprint 0 Review (demo al docente) | ⏳ Pendiente |

> **Nota:** Se completaron 4 días de trabajo al ritmo acelerado solicitado.

---

## 9. Qué Sigue (Semana 2)

- Crear el **Modelo `Producto`** en `productos/models.py` con campos: `nombre`, `precio`, `stock`, `creado`
- Ejecutar `makemigrations` y `migrate`
- Crear **plantillas HTML** para la lista y el detalle (DTL — Django Template Language)
- Iniciar **Sprint 1** con las HU-01 y HU-01a
- Crear `sprint1_planning.md`

---

*Documento generado como cierre del Sprint 0 — Semana 1, Módulo II.*
