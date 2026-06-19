# MicroEnseñanza — Módulo II · Semana 12
## Técnico en Programación (SEP 3061300006-23) · UTEC Celaya
### Asesor: MC. Román Fernando López González

| Campo | Detalle |
|---|---|
| Módulo / Semana | II / 12 de 13 · **Proyecto Integrador Final — Sprint 5** |
| Hilo conector | "Convergencia" |
| Submódulos | S1 Frameworks (`gunicorn`, `WhiteNoise`, `requirements.txt`, `settings_prod.py`, `Procfile`, `render.yaml`, `README.md`, Render.com) · S2 Ágiles (Sprint 5 Planning, kaizen final, `sprint5_retrospective.md`, velocidad del módulo) |
| Stack | Django 4.2 · `gunicorn` · `whitenoise` · Render.com · Python 3.11+ |
| Horario | 16:45–19:45 (180 min/día) |
| Plataforma institucional | Google Classroom |
| Tiempo fantasma (buffer) | 15 min/día máximo (último bloque) |
| Regla del docente | Expone ≤10 min por bloque; el resto circula y asesora |
| Prerrequisito | Semanas 1–11 completas · 17/17 tests en `main` |

**Leyenda de tipos:** 🟡 Arranque en frío · 📖 Mini-exposición (≤10 min) · ✏️ Copia en libreta / Punto de control · 🔍 Investigación rápida con IA · 💻 Práctica de laboratorio · ✅ Verificación/Coevaluación · 🎭 Taller colaborativo · 🗣️ Presentación oral · 📝 Reflexión/Retrospectiva · 📤 Subir a Classroom · 🔄 Anticipo del día siguiente · ⏸️ Pausa activa · 🆓 Buffer

---

## LUNES — Momento Tobón: APERTURA
**Propósito:** demo URL pública + `runserver` vs. `gunicorn` + Sprint 5 Planning + `requirements.txt`.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: **demo en vivo** — el docente abre desde su teléfono una URL pública de Django ya desplegada en Render | Demo URL pública | Teléfono/Proyector | — |
| 16:50 | 10 | 📖 | `runserver` vs. `gunicorn`: concurrencia, seguridad, archivos estáticos; `DEBUG=False` en producción | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC1** — copia la diferencia `runserver`/`gunicorn` + variables de entorno esenciales | Nota PC1 | Libreta | — |
| 17:10 | 25 | 🎭 | Diagrama en libreta: arquitectura de producción completa (GitHub → Render → `gunicorn` → Django → BD) | Diagrama arquitectura | Libreta | — |
| 17:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:40 | 10 | 📖 | Sprint 5 Planning: Sprint Goal de cierre + velocidad acumulada del módulo (~60 pts en 13 semanas) | — | Pizarrón | — |
| 17:50 | 10 | ✏️ | **PC2** — copia el Sprint 5 Planning + tabla de velocidad del módulo | Nota PC2 | Libreta | — |
| 18:00 | 25 | 🎭 | Sprint 5 Planning simulado en equipos: cada equipo redacta el Sprint Goal final con sus propias palabras | Sprint Goal borrador | Libreta | — |
| 18:25 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:30 | 25 | ✅ | Revisión de la **rúbrica** + `pip install gunicorn whitenoise` + `pip freeze > requirements.txt` | `requirements.txt` generado | Terminal | Classroom |
| 18:55 | 25 | 💻 | Verificar que `requirements.txt` contiene los 6 paquetes esenciales + `manage.py check` | Check sin errores | Terminal | — |
| 19:20 | 10 | 📤🔄 | Subir `requirements.txt` + diagrama de arquitectura + anticipo del martes | Evidencia subida | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC1 — runserver vs. gunicorn + variables de entorno
runserver:   un hilo, sin concurrencia, solo desarrollo local
gunicorn:    múltiples workers, producción, maneja carga real

Variables de entorno esenciales para producción:
  DEBUG         = False          (nunca True en prod)
  SECRET_KEY    = <generada>     (nunca en el código)
  ALLOWED_HOSTS = .onrender.com  (dominio de producción)
  SECURE_SSL_REDIRECT = True     (Render da HTTPS automático)

Procfile (1 línea):
  web: gunicorn inventario_proyecto.wsgi:application --bind 0.0.0.0:$PORT
```
```
PC2 — Sprint 5 Planning + velocidad del módulo
Sprint Goal: "Entregar el sistema completo, probado y desplegado."
Duración: 2 semanas (Sem 12–13)

Velocidad acumulada del Módulo II:
  Sprint 1 (Sem 1–3)   →  4 pts
  Sprint 2 (Sem 4–6)   → 15 pts
  Sprint 3 (Sem 8–9)   → 13 pts
  Sprint 4 (Sem 10–11) → 13 pts
  Sprint 5 (Sem 12–13) → ~15 pts
  TOTAL               → ~60 pts en 13 semanas
```

---

## MARTES — Momento Tobón: DESARROLLO (inicio)
**Propósito:** `settings_prod.py` + `collectstatic` + `check --deploy` + 17 tests con settings de producción.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿por qué `DEBUG=True` en producción expone información peligrosa?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | `settings_prod.py`: `os.getenv()`, `WhiteNoiseMiddleware`, `STATIC_ROOT`, `HTTPS settings` | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC3** — copia `settings_prod.py` con `WhiteNoiseMiddleware` y `STATIC_ROOT` | Nota PC3 | Libreta | — |
| 17:10 | 20 | 🔍 | **IA-1**: investigar y copiar resultado en libreta | Nota IA-1 | IA + Libreta | — |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 35 | 💻 | Crear `inventario_proyecto/settings_prod.py` completo + `DJANGO_SETTINGS_MODULE=settings_prod manage.py collectstatic` + leer output | `settings_prod.py` + static files | VS Code/Terminal | — |
| 18:10 | 25 | 💻 | `check --deploy` + interpretar advertencias W012/W016 + 17 tests con settings_prod → `OK` | 17/17 OK en prod | Terminal | — |
| 18:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:40 | 20 | ✅ | Coevaluación: revisar `settings_prod.py` del compañero — `DEBUG=False`? `WhiteNoise` en `MIDDLEWARE`? `SECRET_KEY` en `os.getenv`? | Lista de cotejo | — | — |
| 19:00 | 15 | 📤🔄 | Subir `settings_prod.py` + captura de `collectstatic` + captura `17/17 OK` con `settings_prod` + anticipo miércoles | Avance subido | Classroom | Classroom |
| 19:15 | 15 | 🎭 | Revisión en parejas: ¿la `SECRET_KEY` está en el código fuente o en `os.getenv`? | Lista de cotejo | — | — |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC3 — settings_prod.py + WhiteNoiseMiddleware + STATIC_ROOT
# inventario_proyecto/settings_prod.py
import os
from .settings import *   # importar base — nunca reemplazar

DEBUG      = os.getenv("DEBUG", "False") == "True"
SECRET_KEY = os.getenv("SECRET_KEY", SECRET_KEY)  # from base
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS","localhost").split(",")

# HTTPS (Render provee HTTPS → activar con SECURE_SSL_REDIRECT=True)
_ssl = os.getenv("SECURE_SSL_REDIRECT","False") == "True"
SECURE_SSL_REDIRECT   = _ssl
SESSION_COOKIE_SECURE = _ssl
CSRF_COOKIE_SECURE    = _ssl

# WhiteNoise: insertar DESPUÉS de SecurityMiddleware
MIDDLEWARE.insert(
    MIDDLEWARE.index("django.middleware.security.SecurityMiddleware")+1,
    "whitenoise.middleware.WhiteNoiseMiddleware")
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage")
```
```
IA-1 (copiar pregunta y resultado):
Pregunta: ¿Por qué Django no sirve archivos estáticos en producción
por defecto? ¿Cómo resuelve WhiteNoise ese problema?
Resultado: ____________________________________________
```

---

## MIÉRCOLES — Momento Tobón: DESARROLLO (profundización)
**Propósito:** `Procfile` + `render.yaml` + `README.md` + push a GitHub con todos los archivos de despliegue.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué hace el `Procfile` y quién lo lee?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | `Procfile` (1 línea); `render.yaml` (build/start/envVars/generateValue); `README.md` como documentación mínima | — | Pizarrón | — |
| 17:00 | 15 | 🔍 | **IA-2**: investigar y copiar resultado en libreta | Nota IA-2 | IA + Libreta | — |
| 17:15 | 10 | ✏️ | **PC4** — copia `Procfile` + estructura de `render.yaml` | Nota PC4 | Libreta | — |
| 17:25 | 10 | 💻 | Crear `Procfile` (1 línea exacta) + `render.yaml` completo | `Procfile` + `render.yaml` | VS Code | — |
| 17:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:40 | 30 | 💻 | Crear `README.md` completo (stack, instalación local, endpoints API, instrucciones Render) | `README.md` | VS Code | — |
| 18:10 | 25 | 💻 | `git add` todos los archivos nuevos + `git commit -m "Sprint 5: archivos de despliegue"` + `git push origin main` | Push a GitHub | Terminal/GitHub | GitHub |
| 18:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:40 | 20 | ✅ | Verificar en GitHub que `requirements.txt` + `Procfile` + `render.yaml` + `README.md` aparecen en el repositorio | Repositorio verificado | GitHub | — |
| 19:00 | 15 | 📤🔄 | Subir URL del commit en GitHub + anticipo del jueves (despliegue real en Render) | Enlace subido | Classroom | Classroom |
| 19:15 | 15 | 🎭 | Coevaluación: probar `pip install -r requirements.txt` del repositorio del compañero | Lista de cotejo | — | — |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC4 — Procfile + render.yaml estructura
# Procfile (raíz del proyecto, SIN extensión, 1 línea):
web: gunicorn inventario_proyecto.wsgi:application --bind 0.0.0.0:$PORT

# render.yaml (raíz del proyecto):
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
        generateValue: true   # ← Render genera una clave segura
      - key: ALLOWED_HOSTS
        value: ".onrender.com"
      - key: DEBUG
        value: "False"
      - key: SECURE_SSL_REDIRECT
        value: "True"
```
```
IA-2 (copiar pregunta y resultado):
Pregunta: ¿Qué es un Procfile y para qué lo usan plataformas como
Render o Railway? ¿Qué hace gunicorn que runserver no hace?
Resultado: ____________________________________________
```

---

## JUEVES — Momento Tobón: CIERRE (inicio)
**Propósito:** despliegue real en Render.com + verificar URL + `sprint5_retrospective.md` + kaizen final + flashcards.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué esperas ver en `/api/productos/` cuando el deploy de Render termine?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | Proceso de despliegue en Render: connect repo → build → migrate → start → URL; fallback local con `gunicorn` | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC5** — copia el checklist de despliegue + estructura de `sprint5_retrospective.md` | Nota PC5 | Libreta | — |
| 17:10 | 20 | 🔍 | **IA-3**: investigar y copiar resultado en libreta | Nota IA-3 | IA + Libreta | — |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 25 | 💻 | Conectar GitHub con Render → iniciar deploy → esperar build (~3 min) → verificar URL pública | URL pública obtenida | Render.com/Navegador | — |
| 18:00 | 30 | 💻 | Redactar `sprint5_retrospective.md` (URL + velocidad módulo + kaizen final) + `git commit` + `git push` | Retrospectiva en main | VS Code/GitHub | GitHub |
| 18:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:35 | 25 | 🎭 | Taller de **flashcards** de la semana y del módulo completo | 8 flashcards | Libreta/Quizlet | — |
| 19:00 | 15 | ✏️ | **PC6** — copia conceptos clave del módulo completo para flashcards | Nota PC6 | Libreta | — |
| 19:15 | 15 | 📤🔄 | Subir URL de producción + `sprint5_retrospective.md` + anticipo del viernes | Enlace subido | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC5 — Checklist de despliegue + sprint5_retrospective.md
Checklist ANTES de conectar Render:
  [X] requirements.txt con gunicorn y whitenoise
  [X] Procfile con gunicorn --bind 0.0.0.0:$PORT
  [X] render.yaml con buildCommand/startCommand/envVars
  [X] settings_prod.py con DEBUG=False y WhiteNoise
  [X] collectstatic sin errores
  [X] check --deploy sin errores (advertencias OK)
  [X] 17/17 tests con settings_prod
  [X] git push origin main

Estructura sprint5_retrospective.md:
  ## Sprint Goal verificado → URL pública
  ## Incremento: requirements + Procfile + render + README + URL
  ## Velocidad del módulo: tabla 5 sprints + total ~60 pts
  ## Kaizen final: escribir tests desde Sprint 1 en módulos futuros
  ## ¿Qué aprendí? (3 habilidades concretas)
```
```
PC6 — Conceptos clave Módulo II completo (flashcards)
Framework · MVT · ORM · migraciones · ModelForm · ModelSerializer
CRUD: Create/Read/Update/Delete · CBV · LoginRequiredMixin ·
@login_required · LoginView · LogoutView · IsAuthenticatedOrReadOnly ·
TestCase · setUp() · APIClient · force_authenticate ·
gunicorn · WhiteNoise · requirements.txt · Procfile · render.yaml ·
DEBUG=False · os.getenv · collectstatic · STATIC_ROOT ·
Sprint · backlog · DoD · kaizen · velocidad · burndown · 5 sprints
```
```
IA-3 (copiar pregunta y resultado):
Pregunta: ¿Qué es el Sprint Review final en Scrum y en qué se
diferencia de los Sprint Reviews intermedios?
Resultado: ____________________________________________
```

---

## VIERNES — Momento Tobón: CIERRE (conclusión) · SPRINT 5 REVIEW FINAL
**Propósito:** presentación final del módulo — URL pública proyectada en pantalla.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "abre tu URL de Render en el teléfono del compañero" | URL en teléfono ajeno | Teléfono | — |
| 16:50 | 30 | 🗣️ | **Sprint 5 Review FINAL del Módulo II**: URL pública proyectada → demo web (CRUD + auth) → demo API (`/api/productos/`) → `manage.py test` 17/17 → todos los artefactos Scrum (5 plannings + 5 reviews + retrospectivas) | Demo completa | URL/Terminal/Proyector | — |
| 17:20 | 10 | ✅ | Coevaluación con rúbrica entre pares | Rúbrica llena | Classroom | Classroom |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 30 | ✅ | Verificación final del módulo: URL pública + 17/17 + `requirements.txt` + `Procfile` + `render.yaml` + `README.md` + `sprint5_retrospective.md` | Checklist completo | Terminal/GitHub/Render | — |
| 18:05 | 20 | 📝 | **Retrospectiva final del módulo**: ¿qué aprendiste que antes no sabías hacer? | Notas retro final | Libreta | — |
| 18:25 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:30 | 30 | 🎭 | Repaso colaborativo con flashcards del **módulo completo** (juego por equipos) | Puntaje equipo | Quizlet/Libreta | — |
| 19:00 | 15 | ✏️ | **PC7** — cierre del módulo (ver texto abajo) | Nota PC7 | Libreta | — |
| 19:15 | 15 | 📤 | Subir evidencias finales + autoevaluación del módulo | Carpeta semana 12 | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta — PC7 (cierre obligatorio de la Semana 12 y del Módulo II):**
```
PC7 — CIERRE SEMANA 12 "Convergencia" + CIERRE MÓDULO II

[ ] CHECKLIST DE ENTREGABLES SEMANA 12
    [ ] requirements.txt con gunicorn + whitenoise + 4 deps más
    [ ] settings_prod.py: DEBUG=False + WhiteNoise + os.getenv + HTTPS
    [ ] Procfile: 1 línea con gunicorn --bind 0.0.0.0:$PORT
    [ ] render.yaml: build + start + 5 envVars (SECRET_KEY generateValue)
    [ ] README.md: stack + instalación + endpoints API
    [ ] collectstatic: N archivos copiados a staticfiles/
    [ ] 17/17 tests con DJANGO_SETTINGS_MODULE=settings_prod
    [ ] URL pública de Render funcionando
    [ ] sprint5_retrospective.md: URL + velocidad + kaizen final
    [ ] git push origin main con todos los archivos

VELOCIDAD FINAL DEL MÓDULO II
  5 sprints · ~60 pts · 13 semanas · 1 sistema desplegado en la nube

HABILIDADES ADQUIRIDAS EN EL MÓDULO II
  (completar con 3 propias):
  1. _______________________________________________
  2. _______________________________________________
  3. _______________________________________________

TAREA DE PREPARACIÓN PARA LA SEMANA 13 (Evaluación Final)
    Prepara una presentación de 5 minutos que incluya:
    1. URL pública de tu sistema en Render
    2. Demo del CRUD web (crear + editar + eliminar)
    3. Demo de la API REST (/api/productos/ + POST + DELETE)
    4. manage.py test → 17/17 OK en pantalla
    5. 1 artefacto Scrum de cada sprint (planning o retrospectiva)

PREGUNTA DE REFLEXIÓN FINAL DEL MÓDULO
    El despliegue hace el trabajo visible a cualquier persona del mundo.
    El Sprint Review hace el trabajo visible a los stakeholders.
    ¿En qué se parece esa "apertura al exterior" al principio de
    transparencia de Scrum? ¿Qué valor pierde el trabajo si
    nunca se despliega ni se revisa?
```

---

## Resumen semanal (Google Classroom)

| Día | Actividad en Classroom | Producto | Plazo |
|---|---|---|---|
| Lunes | `requirements.txt` + diagrama arquitectura | `requirements.txt` con 6 paquetes + diagrama | Lunes 19:30 |
| Martes | `settings_prod.py` + collectstatic + 17/17 | `settings_prod.py` + captura collectstatic + captura 17/17 prod | Martes 19:30 |
| Miércoles | `Procfile` + `render.yaml` + `README.md` | Push GitHub con los 4 archivos nuevos | Miércoles 19:30 |
| Jueves | URL pública + retrospectiva | URL de Render + `sprint5_retrospective.md` | Jueves 19:30 |
| Viernes | Carpeta final módulo II + autoevaluación | Todo + retro final + PC7 | Viernes 19:30 |

---

### Conteo de cumplimiento (verificación de reglas del ROL 3)
- Puntos de control: **PC1–PC7 (7 ≥ 5 mínimo)** ✓ · PC7 como **cierre del módulo completo** + checklist (10 ítems) + habilidades adquiridas + tarea evaluación final + reflexión ✓
- Investigaciones rápidas con IA: **IA-1 (martes), IA-2 (miércoles), IA-3 (jueves) = 3 ≥ 3 mínimo** ✓
- Bloques fijos diarios: arranque 5 min a las 16:45 · buffer 15 min al cierre · pausas activas cada ~45–60 min ✓
- Todos los días suman **180 min** verificados aritméticamente ✓ · Mini-exposiciones ≤10 min ✓
- **Demo en vivo del lunes**: el docente abre la URL desde el teléfono — el argumento más poderoso para el despliegue ✓
- **"Abre la URL en el teléfono del compañero"** el viernes — verifica que el sistema es accesible desde cualquier dispositivo ✓
- Sprint 5 Review Final cierra el Módulo II completo con todos los artefactos Scrum ✓
- PC7 incluye el espacio para que el alumno escriba sus **3 habilidades adquiridas** — reflexión metacognitiva de cierre ✓
- Tarea de la Semana 13 es una presentación de 5 minutos con 5 elementos específicos ✓

---

*Plan generado bajo ROL 3 — MicroEnseñanza · Prompt Maestro v1.0 · Metodología Tobón · Google Classroom.*
*Semana 12 de 13 — Módulo II completado en contenido. Semana 13: Evaluación Final.*
