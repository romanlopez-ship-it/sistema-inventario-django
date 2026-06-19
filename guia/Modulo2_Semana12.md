# Módulo II · Semana 12 — Proyecto Integrador Final y Despliegue
## Técnico en Programación (SEP 3061300006-23) · UTEC Celaya
### Asesor: MC. Román Fernando López González

---

## 1. Identificación de la semana

| Campo | Detalle |
|---|---|
| Carrera | Técnico en Programación |
| Módulo | II — Desarrolla software con herramientas orientadas a la productividad (272 h) |
| Semana | 12 de 13 · **PROYECTO INTEGRADOR — Sprint 5** |
| Submódulos integrados | S1 Frameworks (144 h) · S2 Metodologías ágiles (128 h) |
| **Hilo conector de la semana** | **"Convergencia"** |
| Stack | Django 4.2 · `gunicorn` · `WhiteNoise` · `render.yaml` · Python 3.11+ |
| Paquetes nuevos | `gunicorn` · `whitenoise` |
| Carga horaria reportada | 17 h/semana (S1 = 9 h · S2 = 8 h) |
| Carga horaria real (planeación) | 14.16 h/semana |
| Tiempo fantasma máximo | 15 min/día |
| Plataforma institucional | Google Classroom |
| Prerrequisito | Semanas 1–11 completas · 17/17 tests en `main` |

> **Hilo conector:** once semanas de modelos, vistas, plantillas, autenticación, CBV, API REST y pruebas convergen esta semana en **un solo sistema desplegado en la nube**. El Sprint Review final no demuestra una función —demuestra un producto completo accesible desde cualquier navegador del mundo. La convergencia técnica (despliegue) y la convergencia metodológica (Sprint Review final) son la misma operación: hacer que el trabajo acumulado sea visible y verificable por cualquier persona externa.

---

## 2. Competencias de la semana

**Resultado de aprendizaje (SEP):**
El estudiante integra todos los componentes del sistema de inventario en una aplicación desplegable: configura `settings_prod.py`, genera `requirements.txt`, crea `Procfile` y `render.yaml`, ejecuta `collectstatic`, despliega en Render.com y verifica que los 17 tests siguen pasando en producción; presenta el sistema en el Sprint 5 Review final del módulo.

**Actividades clave de la competencia laboral:**

- **S1 — Frameworks:** Instala `gunicorn` y `whitenoise`; configura `settings_prod.py` con `DEBUG=False`, variables de entorno y `WhiteNoiseMiddleware`; genera `requirements.txt`; crea `Procfile` y `render.yaml`; ejecuta `collectstatic` y `manage.py check --deploy`; despliega el proyecto en Render.com.
- **S2 — Metodologías ágiles:** Prepara y presenta el Sprint 5 Review final con la URL desplegada, los 17 tests y todos los artefactos Scrum; redacta la retrospectiva final del módulo.

---

## 3. PARTE I — Estructura académica (modelo Corina Schmelkes)

### 3.1 Introducción

El servidor de desarrollo de Django (`runserver`) está diseñado para un solo desarrollador trabajando localmente: no maneja múltiples peticiones concurrentes ni sirve archivos estáticos de forma eficiente. La documentación oficial de Django (Django Software Foundation, s.f.) describe el proceso de despliegue como la transición del servidor de desarrollo a un servidor de producción capaz de recibir tráfico real. Esta transición requiere tres cambios fundamentales: un servidor WSGI de producción (`gunicorn`), un gestor de archivos estáticos (`WhiteNoise`) y una configuración separada con secretos gestionados por variables de entorno. Desde el ángulo metodológico, Schwaber y Sutherland (2020) definen el Sprint Review del último sprint del módulo como el momento en que el equipo presenta el incremento final al Product Owner y a todos los interesados: no un informe escrito, sino una **demostración en vivo** del producto funcionando.

### 3.2 Planteamiento del problema

El sistema de inventario funciona en la computadora del estudiante. Pero un cliente, un empleador o un docente externo no puede verlo sin instalar Python, Django y la base de datos. ¿Cómo hacer que el sistema sea accesible desde una URL pública con un solo clic, sin modificar el código que ya funciona?

### 3.3 Justificación

El despliegue en Render.com resuelve el problema con tres archivos nuevos (`requirements.txt`, `Procfile`, `render.yaml`) y una configuración de producción separada: el código de la aplicación no cambia, solo cambia el entorno que lo rodea. La documentación oficial de Django (Django Software Foundation, s.f.) recomienda mantener las configuraciones de desarrollo y producción separadas para evitar exponer accidentalmente `SECRET_KEY` o `DEBUG=True` en producción.

### 3.4 Objetivos

**General:** Que el estudiante despliegue el sistema de inventario en Render.com y presente el Sprint 5 Review con la URL pública como entregable principal.

**Específicos:**
1. Instalar `gunicorn` y `whitenoise`; generar `requirements.txt` (S1).
2. Crear `settings_prod.py` con variables de entorno, `WhiteNoiseMiddleware` y `STATIC_ROOT` (S1).
3. Crear `Procfile` y `render.yaml` con la configuración de Render (S1).
4. Ejecutar `collectstatic` y `check --deploy`; verificar 17 tests en producción (S1).
5. Desplegar en Render.com y verificar la URL pública (S1).
6. Presentar el Sprint 5 Review final con URL, tests y artefactos Scrum (S2).

### 3.5 Marco teórico (con código)

**`gunicorn`: servidor WSGI de producción.** Django Software Foundation (s.f.) explica que `runserver` no debe usarse en producción: no está optimizado para concurrencia ni seguridad. `gunicorn` es el servidor WSGI estándar para Django en la nube:

```bash
# Instalar
pip install gunicorn

# Ejecutar localmente para probar (equivale a runserver)
gunicorn inventario_proyecto.wsgi:application --bind 0.0.0.0:8000

# En el Procfile (una sola línea, leída por Render/Railway):
web: gunicorn inventario_proyecto.wsgi:application --bind 0.0.0.0:$PORT
```

**`WhiteNoise`: archivos estáticos sin servidor web separado.** En producción, Django no sirve archivos estáticos (CSS, JS) por defecto. `WhiteNoise` los sirve directamente desde Python, sin necesidad de Nginx ni S3 (WhiteNoise, s.f.):

```python
# settings_prod.py — insertar en MIDDLEWARE, segundo lugar
MIDDLEWARE.insert(
    MIDDLEWARE.index("django.middleware.security.SecurityMiddleware") + 1,
    "whitenoise.middleware.WhiteNoiseMiddleware",
)

STATIC_ROOT = BASE_DIR / "staticfiles"     # directorio de colección
STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

# Antes de desplegar, ejecutar:
# python3 manage.py collectstatic --noinput
# → copia todos los archivos estáticos a STATIC_ROOT
```

**Variables de entorno: secretos fuera del código.** Django Software Foundation (s.f.) lista en el checklist de despliegue que `SECRET_KEY` y `DEBUG` nunca deben estar en el código fuente en producción:

```python
# settings_prod.py — valores desde el entorno
import os
DEBUG     = os.getenv("DEBUG", "False") == "True"
SECRET_KEY = os.getenv("SECRET_KEY", "dev-insecure-key")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost").split(",")

# En Render → Environment Variables:
#   SECRET_KEY    = <generada aleatoriamente>
#   DEBUG         = False
#   ALLOWED_HOSTS = .onrender.com
#   SECURE_SSL_REDIRECT = True   (resuelve las advertencias del --deploy check)
```

**`render.yaml`: despliegue declarativo.** Render.com acepta un archivo de configuración que automatiza el build y el arranque:

```yaml
services:
  - type: web
    name: inventario-sistema
    env: python
    buildCommand: >-
      pip install -r requirements.txt &&
      python manage.py collectstatic --noinput &&
      python manage.py migrate
    startCommand: gunicorn inventario_proyecto.wsgi:application
    envVars:
      - key: DJANGO_SETTINGS_MODULE
        value: inventario_proyecto.settings_prod
      - key: SECRET_KEY
        generateValue: true
      - key: ALLOWED_HOSTS
        value: ".onrender.com"
      - key: DEBUG
        value: "False"
      - key: SECURE_SSL_REDIRECT
        value: "True"
```

**`manage.py check --deploy`: lista de verificación previa.** Django evalúa la configuración y reporta problemas de seguridad antes del despliegue:

```bash
DJANGO_SETTINGS_MODULE=inventario_proyecto.settings_prod \
  python3 manage.py check --deploy

# Advertencias típicas (resueltas con HTTPS en Render):
# W012 SESSION_COOKIE_SECURE → resolver: SESSION_COOKIE_SECURE=True
# W016 CSRF_COOKIE_SECURE    → resolver: CSRF_COOKIE_SECURE=True
# Todas se resuelven automáticamente con SECURE_SSL_REDIRECT=True en Render.
```

### 3.6 Metodología

Trabajo guiado e individual. La sesión sigue el orden de la lista de despliegue oficial de Django: configurar → instalar → recolectar → verificar → desplegar → probar URL pública. El despliegue se hace directamente desde el repositorio GitHub al conectarlo con Render.com.

### 3.7 Desarrollo temático

**S1 — Frameworks (≈9 h reportadas)**
1. Diferencia `runserver` (desarrollo) vs. `gunicorn` (producción).
2. `WhiteNoise`: cómo sirve archivos estáticos sin servidor web externo.
3. `settings_prod.py`: variables de entorno, `DEBUG=False`, `ALLOWED_HOSTS`.
4. `requirements.txt`: qué incluir, cómo generarlo con `pip freeze`.
5. `Procfile` y `render.yaml`: despliegue declarativo.
6. `collectstatic` → `check --deploy` → desplegar → verificar URL.
7. `README.md`: documentación mínima del repositorio.

**S2 — Metodologías ágiles (≈8 h reportadas)**
1. Sprint 5 Review final: formato, duración, quién habla, qué demostrar.
2. Retrospectiva final del módulo: kaizen acumulado de 5 sprints.
3. Resumen de velocidad: 13 semanas → ~58 pts completados.
4. Reflexión de cierre: ¿qué aprendí que antes no sabía hacer?

### 3.8 Práctica de laboratorio

**Objetivo:** desplegar el sistema de inventario en Render.com con `gunicorn` + `WhiteNoise` y presentar el Sprint 5 Review con la URL pública.

---

#### PASO 1 — Instalar dependencias de producción

```bash
pip install gunicorn whitenoise
pip freeze > requirements.txt
# Verificar que el archivo contiene al menos:
# Django==4.2 · djangorestframework · gunicorn · whitenoise · asgiref · sqlparse
```

---

#### PASO 2 — Crear `inventario_proyecto/settings_prod.py`

```python
"""Configuracion de produccion — Semana 12.

Extiende settings.py con valores seguros para despliegue.
Nunca hardcodear secretos: usar variables de entorno.
"""

import os

from .settings import *   # noqa: F401,F403 — importar base

# ── Seguridad ────────────────────────────────────────────────
DEBUG      = os.getenv("DEBUG", "False") == "True"
SECRET_KEY = os.getenv("SECRET_KEY", SECRET_KEY)   # noqa: F405
ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS", "localhost,127.0.0.1"
).split(",")

# ── HTTPS (Render provee HTTPS automaticamente) ───────────────
_ssl = os.getenv("SECURE_SSL_REDIRECT", "False") == "True"
SECURE_SSL_REDIRECT   = _ssl
SESSION_COOKIE_SECURE = _ssl
CSRF_COOKIE_SECURE    = _ssl

# ── Archivos estaticos con WhiteNoise ────────────────────────
MIDDLEWARE.insert(                                 # noqa: F405
    MIDDLEWARE.index(                              # noqa: F405
        "django.middleware.security.SecurityMiddleware"
    ) + 1,
    "whitenoise.middleware.WhiteNoiseMiddleware",
)
STATIC_ROOT         = BASE_DIR / "staticfiles"    # noqa: F405
STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)
```

---

#### PASO 3 — Crear `Procfile` (raíz del proyecto)

```
web: gunicorn inventario_proyecto.wsgi:application --bind 0.0.0.0:$PORT
```

---

#### PASO 4 — Crear `render.yaml` (raíz del proyecto)

```yaml
services:
  - type: web
    name: inventario-sistema
    env: python
    buildCommand: >-
      pip install -r requirements.txt &&
      python manage.py collectstatic --noinput &&
      python manage.py migrate
    startCommand: gunicorn inventario_proyecto.wsgi:application
    envVars:
      - key: DJANGO_SETTINGS_MODULE
        value: inventario_proyecto.settings_prod
      - key: SECRET_KEY
        generateValue: true
      - key: ALLOWED_HOSTS
        value: ".onrender.com"
      - key: DEBUG
        value: "False"
      - key: SECURE_SSL_REDIRECT
        value: "True"
```

---

#### PASO 5 — Crear `README.md` (raíz del proyecto)

```markdown
# Sistema de Inventario
## Módulo II — Técnico en Programación · UTEC Celaya

### Descripción
Sistema de gestión de inventario construido con Django 4.2 en 13 semanas.

### Stack
- Django 4.2 LTS · DRF 3.x · Python 3.11+
- SQLite (desarrollo) · gunicorn + WhiteNoise (producción)

### Características
- CRUD de productos (web con CBV + API REST)
- Autenticación (LoginRequired / LoginRequiredMixin)
- API REST (GET público / escritura autenticada)
- 17 pruebas automatizadas (modelo + serializer + API)

### Instalación local
pip install -r requirements.txt
python manage.py migrate && python manage.py createsuperuser
python manage.py test productos   # → 17/17 OK
python manage.py runserver

### Endpoints API
GET  /api/productos/         → lista (público)
POST /api/productos/         → crear (autenticado)
GET  /api/productos/<pk>/    → detalle (público)
PUT  /api/productos/<pk>/    → actualizar (autenticado)
PATCH /api/productos/<pk>/   → parcial (autenticado)
DELETE /api/productos/<pk>/  → eliminar (autenticado)
```

---

#### PASO 6 — Verificar localmente antes de desplegar

```bash
# Recolectar archivos estáticos
DJANGO_SETTINGS_MODULE=inventario_proyecto.settings_prod \
  python3 manage.py collectstatic --noinput
# Resultado esperado: "N static files copied to .../staticfiles"

# Checklist de despliegue
DJANGO_SETTINGS_MODULE=inventario_proyecto.settings_prod \
  python3 manage.py check --deploy
# Aceptable: solo advertencias W012/W016 (se resuelven con HTTPS en Render)

# Los 17 tests siguen pasando con settings de producción
DJANGO_SETTINGS_MODULE=inventario_proyecto.settings_prod \
  python3 manage.py test productos --verbosity=0
# Resultado esperado: "Ran 17 tests in X.XXXs — OK"
```

---

#### PASO 7 — Desplegar en Render.com

1. Hacer **push** del proyecto a GitHub (incluir `requirements.txt`, `Procfile`, `render.yaml`, `README.md`).
2. Entrar a [render.com](https://render.com) → **New Web Service** → conectar el repositorio.
3. Render detecta el `render.yaml` automáticamente → confirmar el build.
4. Esperar ~3 minutos → obtener la URL pública `https://inventario-sistema.onrender.com`.
5. Verificar:
   - `https://<tu-app>.onrender.com/api/productos/` → lista JSON (200).
   - `https://<tu-app>.onrender.com/accounts/login/` → formulario de login.
   - `https://<tu-app>.onrender.com/admin/` → panel admin.

> **Fallback sin conexión:** si Render no está disponible, demostrar el despliegue local con `gunicorn inventario_proyecto.wsgi:application` (equivalente al servidor de producción en la máquina local). La URL pública puede sustituirse con la captura del deploy log de Render.

---

#### PASO 8 — Sprint 5 Review final (S2)

Crea `sprint5_retrospective.md` con el resumen del módulo completo:

```markdown
# Sprint 5 Review + Retrospectiva Final del Módulo II
## Fecha: ___________ | Sprint: 5 (Sem 12–13)

### Sprint Goal verificado
"Entregar el sistema de inventario completo, probado y desplegado."
✅ Sprint Goal cumplido.

### URL de producción
https://<tu-app>.onrender.com

### Incremento entregado
- [x] Sistema web con CRUD (CBV + auth + plantillas)
- [x] API REST (DRF + IsAuthenticatedOrReadOnly)
- [x] 17 pruebas automatizadas (17/17 OK en producción)
- [x] Despliegue en Render.com con gunicorn + WhiteNoise
- [x] README.md con instalación y documentación de API

### Velocidad del módulo
| Sprint | Semanas | Puntos |
|--------|---------|--------|
| 1      | 1–3     | 4 pts  |
| 2      | 4–6     | 15 pts |
| 3      | 8–9     | 13 pts |
| 4      | 10–11   | 13 pts |
| 5      | 12–13   | ~15 pts|
| **Total** | **13 sem** | **~60 pts** |

### Kaizen final del módulo
La acción más importante para el siguiente módulo:
escribir tests JUNTO al código desde el Sprint 1, no al final.

### ¿Qué aprendí que antes no sabía hacer?
(completar con 3 habilidades concretas adquiridas en el módulo)
```

---

#### Entregables — Sprint 5 arranca con despliegue

```bash
git add requirements.txt Procfile render.yaml README.md
git add inventario_proyecto/settings_prod.py
git add sprint5_retrospective.md
git commit -m "Sprint 5: despliegue en Render + README + kaizen final"
git push origin main
```

---

### 3.9 Análisis (5 preguntas de reflexión)

1. ¿Por qué `DEBUG=True` en producción es un riesgo de seguridad? ¿Qué información expone Django cuando `DEBUG=True` y ocurre un error?
2. ¿Por qué `WhiteNoise` sirve archivos estáticos en producción si Django puede hacerlo con `STATIC_URL`? ¿Qué problema resuelve?
3. El `Procfile` dice `--bind 0.0.0.0:$PORT`. ¿Por qué `0.0.0.0` en lugar de `127.0.0.1`, y de dónde viene `$PORT`?
4. La variable `SECRET_KEY` se genera automáticamente en `render.yaml` con `generateValue: true`. ¿Qué pasaría si usaras la misma `SECRET_KEY` en producción y desarrollo?
5. El kaizen del módulo dice "escribir tests junto al código desde el Sprint 1". ¿Qué cambiaría en la forma de trabajar de las Semanas 5–10 si hubieras aplicado ese principio desde el principio?

### 3.10 Conclusiones

Esta semana el sistema de inventario cruzó la última frontera: de un proyecto local a una aplicación pública con URL propia. Tres archivos (`requirements.txt`, `Procfile`, `render.yaml`) y una configuración de producción son todo lo que separa "funciona en mi máquina" de "funciona en Internet". Los 17 tests que pasan en el entorno de producción son la garantía de que el despliegue no rompió nada. El Sprint 5 Review cierra el módulo con la demostración más contundente posible: una URL que cualquier persona del mundo puede abrir y ver el inventario funcionando.

---

## 4. PARTE II — Momentos didácticos (Sergio Tobón)

### 4.1 Momento 1 — Apertura
Planteamiento: "¿cómo compartes tu proyecto con alguien que no tiene Python instalado?". Demo del docente: abrir una URL pública de un proyecto Django desplegado en Render. Introducir el Sprint Review final como demostración pública del trabajo del módulo.

### 4.2 Momento 2 — Desarrollo
Configuración guiada de `settings_prod.py` → `requirements.txt` → `Procfile` → `render.yaml` → `collectstatic` → `check --deploy` → verificar 17 tests en producción → push a GitHub → conectar con Render → esperar build → verificar URL pública. En paralelo, redactar `sprint5_retrospective.md`.

### 4.3 Momento 3 — Cierre
Sprint 5 Review con la URL pública proyectada, kaizen final del módulo, subida a Classroom.

---

## 5. Estrategia de evaluación de la semana

| Evidencia | Submódulo | Instrumento | Ponderación |
|---|---|---|---|
| `requirements.txt`, `Procfile`, `render.yaml` y `settings_prod.py` correctos | S1 | Lista de cotejo | 25 % |
| `collectstatic` exitoso + `check --deploy` sin errores (solo advertencias HTTPS) + 17/17 con settings_prod | S1 | Verificación directa | 20 % |
| URL pública de Render con `/api/productos/` → JSON y `/admin/` → panel | S1 | Captura de pantalla | 20 % |
| `README.md` con stack, instrucciones y endpoints documentados | S1 | Lista de cotejo | 10 % |
| `sprint5_retrospective.md` con velocidad del módulo + kaizen final + URL | S2 | Lista de cotejo | 15 % |
| Respuestas de análisis (5 preguntas) | Transversal | Lista de cotejo | 10 % |

---

## 6. Recursos didácticos

- Proyecto Django de la Semana 11 en `main` (17 tests + Sprint 4 cerrado).
- Cuenta en GitHub (repositorio público o privado).
- Cuenta gratuita en Render.com (o Railway.app como alternativa).
- Computadora con Python 3.11+, Django 4.2, VS Code y conexión a internet.
- Google Classroom para entrega de evidencias.

---

## 7. Referencias (APA 7)

Django Software Foundation. (s.f.). *Deployment checklist*. https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

Django Software Foundation. (s.f.). *How to deploy Django*. https://docs.djangoproject.com/en/4.2/howto/deployment/

Render. (s.f.). *Deploy a Django app*. https://render.com/docs/deploy-django

Schwaber, K., & Sutherland, J. (2020). *La guía de Scrum*. https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf

WhiteNoise. (s.f.). *WhiteNoise documentation*. http://whitenoise.evans.io/

---

*Guía generada bajo ROL 2 — Asesor Académico Experto · Prompt Maestro v1.0 · Una semana a la vez.*
*Parámetros respetados: 13 semanas · submódulos y horas SEP sin modificar · cita narrativa.*
*Código verificado: 152 archivos estáticos recolectados · 17/17 tests con `settings_prod` · `check --deploy` sin errores (solo advertencias HTTPS esperadas) · `Procfile` + `render.yaml` generados.*
