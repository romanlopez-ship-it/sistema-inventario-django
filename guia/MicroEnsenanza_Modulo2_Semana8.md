# MicroEnseñanza — Módulo II · Semana 8
## Técnico en Programación (SEP 3061300006-23) · UTEC Celaya
### Asesor: MC. Román Fernando López González

| Campo | Detalle |
|---|---|
| Módulo / Semana | II / 8 de 13 |
| Hilo conector | "Usuarios reales" |
| Submódulos | S1 Frameworks (`settings.py` LOGIN*, `LoginView`/`LogoutView`, `registration/login.html`, `@login_required`, `{% if user.is_authenticated %}`) · S2 Ágiles (Sprint 3 Planning, backlog grooming, Kanban Sprint 3) |
| Stack | Django 4.2 · `django.contrib.auth` · `@login_required` · Python 3.11+ |
| Horario | 16:45–19:45 (180 min/día) |
| Plataforma institucional | Google Classroom |
| Tiempo fantasma (buffer) | 15 min/día máximo (último bloque) |
| Regla del docente | Expone ≤10 min por bloque; el resto circula y asesora |
| Prerrequisito | Evaluación intermedia superada (Semana 7) · CRUD completo en `main` |

**Leyenda de tipos:** 🟡 Arranque en frío · 📖 Mini-exposición (≤10 min) · ✏️ Copia en libreta / Punto de control · 🔍 Investigación rápida con IA · 💻 Práctica de laboratorio · ✅ Verificación/Coevaluación · 🎭 Taller colaborativo · 🗣️ Presentación oral · 📝 Reflexión/Retrospectiva · 📤 Subir a Classroom · 🔄 Anticipo del día siguiente · ⏸️ Pausa activa · 🆓 Buffer

---

## LUNES — Momento Tobón: APERTURA
**Propósito:** detonador "URL descubierta" + `django.contrib.auth` concepto + diagrama del flujo de autenticación + Sprint 3 Planning intro + rúbrica + rama sprint3.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué pasa si alguien que no es empleado descubre la URL `/productos/nuevo/`?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | `django.contrib.auth`: ya está en `INSTALLED_APPS`; `@login_required` en una línea; `LoginView`/`LogoutView` sin código propio | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC1** — copia las 3 constantes de autenticación + `ALLOWED_HOSTS` | Nota PC1 | Libreta | — |
| 17:10 | 25 | 🎭 | Dibujar en libreta el flujo completo: anónimo→`/accounts/login/?next=`→login→redirect→200 / autenticado→logout→login | Diagrama auth | Libreta | — |
| 17:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:40 | 10 | 📖 | Sprint 3 Planning: Sprint Goal; HU-05/06 esta semana (8 pts); HU-07 CBV Semana 9 (5 pts) | — | Pizarrón | — |
| 17:50 | 10 | ✏️ | **PC2** — copia el formato del Sprint 3 Planning + HUs seleccionadas | Nota PC2 | Libreta | — |
| 18:00 | 25 | 🎭 | Sprint 3 Planning simulado en equipos: definir el Sprint Goal con las propias palabras | Sprint Goal borrador | Libreta | — |
| 18:25 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:30 | 25 | ✅ | Revisión de la **rúbrica** + `manage.py check` del proyecto post-evaluación | Check sin errores | Terminal | Classroom |
| 18:55 | 25 | 💻 | Crear rama `sprint3/autenticacion-cbv` + actualizar `ALLOWED_HOSTS` en `settings.py` | Rama + settings | Terminal/VS Code | — |
| 19:20 | 10 | 📤🔄 | Subir diagrama de autenticación + `settings.py` actualizado + anticipo del martes | Evidencia subida | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC1 — Constantes de autenticación + ALLOWED_HOSTS
# inventario_proyecto/settings.py

# Hosts permitidos (incluir siempre en desarrollo)
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "testserver"]

# Autenticacion — Semana 8
LOGIN_URL           = "/accounts/login/"  # no autenticados van aqui
LOGIN_REDIRECT_URL  = "/productos/"        # tras login exitoso
LOGOUT_REDIRECT_URL = "/accounts/login/"  # tras logout

# Diagrama del flujo:
# Anónimo → /productos/nuevo/ → 302 → /accounts/login/?next=/productos/nuevo/
#                                        ↓ (login exitoso)
#                                      /productos/
```
```
PC2 — Sprint 3 Planning
Sprint Goal: "Los usuarios autenticados gestionan el inventario;
              los anónimos solo consultan."
Historias:
  HU-05  Login/logout (LoginView/LogoutView)       5 pts  Sem 8
  HU-06  @login_required en vistas de escritura    3 pts  Sem 8
  HU-07  Migrar CRUD a CBV                         5 pts  Sem 9
Total comprometido: 13 pts (velocidad promedio ~10)
Justificación: HU-05/06 son estratégicas (seguridad).
```

---

## MARTES — Momento Tobón: DESARROLLO (inicio)
**Propósito:** `LoginView`/`LogoutView` en `urls.py` + `registration/login.html` + verificar login en navegador.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué hace `LoginView.as_view()` sin escribir ningún código de autenticación propio?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | `LoginView`/`LogoutView` en `urls.py`; dónde busca Django `registration/login.html`; `AuthenticationForm` automático | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC3** — copia `LoginView`/`LogoutView` en `urls.py` + estructura de `login.html` | Nota PC3 | Libreta | — |
| 17:10 | 20 | 🔍 | **IA-1**: investigar y copiar resultado en libreta | Nota IA-1 | IA + Libreta | — |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 35 | 💻 | Actualizar `inventario_proyecto/urls.py` (agregar `LoginView`/`LogoutView`) + crear `templates/registration/` + `login.html` | `urls.py` + `login.html` | VS Code | — |
| 18:10 | 25 | 💻 | Agregar `LOGIN_REDIRECT_URL` y `LOGOUT_REDIRECT_URL` a `settings.py` + `manage.py check` + probar `/accounts/login/` | Login visible en navegador | Terminal/Navegador | — |
| 18:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:40 | 20 | ✅ | `createsuperuser` + probar ciclo login → `/productos/` → logout → `/accounts/login/` | Ciclo verificado | Navegador | — |
| 19:00 | 15 | 📤🔄 | Subir `urls.py` + `login.html` + `settings.py` actualizado + anticipo del miércoles | Avance subido | Classroom | Classroom |
| 19:15 | 15 | 🎭 | Revisión en parejas: ¿el login muestra el formulario? ¿el logout redirige? | Lista de cotejo | — | — |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC3 — LoginView/LogoutView en urls.py + login.html
# inventario_proyecto/urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/",            admin.site.urls),
    path("accounts/login/",   auth_views.LoginView.as_view(),  name="login"),
    path("accounts/logout/",  auth_views.LogoutView.as_view(), name="logout"),
    path("",                  include("productos.urls", namespace="productos")),
]

# templates/registration/login.html:
{% extends "base.html" %}
{% block title %}Iniciar sesión{% endblock %}
{% block content %}
<h2>Iniciar sesión</h2>
{% if form.errors %}<p>Credenciales incorrectas.</p>{% endif %}
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Entrar</button>
</form>
{% endblock %}
# Django busca esta plantilla en CUALQUIER directorio de TEMPLATES.
```
```
IA-1 (copiar pregunta y resultado):
Pregunta: ¿Qué hace Django con el parámetro ?next= que añade a la
URL de login cuando un usuario no autenticado accede a una vista
protegida? ¿Cómo lo usa tras el login exitoso?
Resultado: ____________________________________________
```

---

## MIÉRCOLES — Momento Tobón: DESARROLLO (profundización)
**Propósito:** `@login_required` en 3 vistas + nav condicional + verificar 11 aserciones.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué ve un usuario anónimo que intenta acceder a `/productos/nuevo/` ahora?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | `@login_required`: qué hace exactamente; `?next=` en la URL; qué vistas proteger y cuáles dejar públicas | — | Pizarrón | — |
| 17:00 | 15 | 🔍 | **IA-2**: investigar y copiar resultado en libreta | Nota IA-2 | IA + Libreta | — |
| 17:15 | 10 | ✏️ | **PC4** — copia `@login_required` + `{% if user.is_authenticated %}` | Nota PC4 | Libreta | — |
| 17:25 | 10 | 💻 | Inicio: agregar `@login_required` a `crear_producto` en `views.py` | Inicio views.py | VS Code | — |
| 17:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:40 | 30 | 💻 | Agregar `@login_required` a `editar_producto` y `eliminar_producto` + actualizar `base.html` con nav condicional (`{% if user.is_authenticated %}`) | Vistas + nav | VS Code | — |
| 18:10 | 25 | 💻 | Verificar las 11 aserciones: crear/editar/eliminar anónimo→302 / autenticado→200 / lista pública / nav condicional | 11/11 verificaciones | Navegador | — |
| 18:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:40 | 20 | ✅ | Coevaluación: probar acceso anónimo a las 3 vistas del compañero; verificar redirect a login | Lista de cotejo | — | — |
| 19:00 | 15 | 📤🔄 | Subir `views.py` + `base.html` + anticipo del jueves | Entregables subidos | Classroom | Classroom |
| 19:15 | 15 | 🎭 | Coevaluación: ¿el nav muestra el `username` cuando está autenticado? | Lista de cotejo | — | — |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC4 — @login_required + {% if user.is_authenticated %}
# views.py — decorador ANTES de cada vista protegida:
from django.contrib.auth.decorators import login_required

@login_required                    # ← UNA línea
def crear_producto(request):
    ...

@login_required
def editar_producto(request, producto_id):
    ...

@login_required
def eliminar_producto(request, producto_id):
    ...

# lista_productos y detalle_producto → SIN decorador (públicas)

# base.html — nav condicional:
{% if user.is_authenticated %}
    <a href="/productos/nuevo/">+ Nuevo</a>
    | <a href="/accounts/logout/">Cerrar sesión ({{ user.username }})</a>
{% else %}
    <a href="/accounts/login/">Iniciar sesión</a>
{% endif %}
```
```
IA-2 (copiar pregunta y resultado):
Pregunta: ¿Por qué @login_required es considerado un "decorador"
en Python? ¿Qué diferencia hay entre un decorador y llamar a
una función normal?
Resultado: ____________________________________________
```

---

## JUEVES — Momento Tobón: CIERRE (inicio)
**Propósito:** `sprint3_planning.md` completo + Kanban Sprint 3 + flashcards.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué diferencia hay entre HU-05 (login/logout) y HU-06 (`@login_required`)?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | Refinamiento del backlog: clarificar HUs, actualizar criterios Gherkin, re-estimar si cambió la complejidad | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC5** — copia el Sprint 3 Planning completo con HUs y estado | Nota PC5 | Libreta | — |
| 17:10 | 20 | 🔍 | **IA-3**: investigar y copiar resultado en libreta | Nota IA-3 | IA + Libreta | — |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 25 | 💻 | Redactar `sprint3_planning.md` completo + `git commit` + `git push sprint3/autenticacion-cbv` | `sprint3_planning.md` en rama | VS Code/GitHub | GitHub |
| 18:00 | 30 | 💻 | Actualizar Kanban en GitHub Projects: mover HU-05→Done + HU-06→Done + HU-07→To Do | Kanban actualizado | GitHub | GitHub |
| 18:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:35 | 25 | 🎭 | Taller de **flashcards** de la semana | 8 flashcards | Libreta/Quizlet | — |
| 19:00 | 15 | ✏️ | **PC6** — copia conceptos clave para flashcards | Nota PC6 | Libreta | — |
| 19:15 | 15 | 📤🔄 | Subir `sprint3_planning.md` + URL del Kanban + anticipo del viernes | Enlace subido | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC5 — Sprint 3 Planning completo
Sprint Goal: "Los usuarios autenticados gestionan el inventario;
los anónimos solo consultan."
Duración: 2 semanas (Sem 8–9)

| HU    | Historia                            | Pts | Estado   |
|-------|-------------------------------------|-----|----------|
| HU-05 | Login/logout LoginView/LogoutView   | 5   | ✅ Done  |
| HU-06 | @login_required en 3 vistas         | 3   | ✅ Done  |
| HU-07 | CRUD a Vistas Basadas en Clases CBV | 5   | To Do    |
Total: 13 pts comprometidos

Rama Git: sprint3/autenticacion-cbv
```
```
PC6 — Conceptos clave (flashcards)
django.contrib.auth · INSTALLED_APPS por defecto ·
LOGIN_URL · LOGIN_REDIRECT_URL · LOGOUT_REDIRECT_URL ·
ALLOWED_HOSTS · LoginView · LogoutView · AuthenticationForm ·
registration/login.html · @login_required · ?next= ·
user.is_authenticated · user.username · nav condicional ·
Sprint 3 · backlog grooming · CBV (Vista Basada en Clases)
```
```
IA-3 (copiar pregunta y resultado):
Pregunta: ¿Qué es el refinamiento del backlog (backlog grooming)
en Scrum y por qué se recomienda hacerlo regularmente durante
el sprint activo?
Resultado: ____________________________________________
```

---

## VIERNES — Momento Tobón: CIERRE (conclusión)
**Propósito:** Sprint Review (demo auth) + coevaluación + retrospectiva.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "demuestra en 30 segundos que un anónimo no puede crear un producto" | Demo rápida | Navegador | — |
| 16:50 | 30 | 🗣️ | **Sprint Review** (Sprint 3 parcial): demo auth completa — anónimo→login→crear→logout→bloqueado + nav condicional + `sprint3_planning.md` | Demostración ante docente | Navegador/Proyector | — |
| 17:20 | 10 | ✅ | Coevaluación con rúbrica entre pares | Rúbrica llena | Classroom | Classroom |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 30 | ✅ | Verificación final: 11 aserciones + `manage.py check` + Kanban HU-05/06→Done + `sprint3_planning.md` | Checklist validado | Terminal/GitHub | — |
| 18:05 | 20 | 📝 | **Retrospectiva**: ¿qué cambió al agregar `@login_required`? ¿qué mejorar para la Semana 9 (CBV)? | Notas retro | Libreta | — |
| 18:25 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:30 | 30 | 🎭 | Repaso colaborativo con flashcards (juego por equipos) | Puntaje equipo | Quizlet/Libreta | — |
| 19:00 | 15 | ✏️ | **PC7** — cierre de la semana (ver texto abajo) | Nota PC7 | Libreta | — |
| 19:15 | 15 | 📤 | Subir evidencias finales + autoevaluación | Carpeta semana 8 | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta — PC7 (cierre obligatorio):**
```
PC7 — CIERRE SEMANA 8 "Usuarios reales"

[ ] CHECKLIST DE ENTREGABLES
    [ ] settings.py: LOGIN_URL + LOGIN_REDIRECT_URL + LOGOUT_REDIRECT_URL
    [ ] settings.py: ALLOWED_HOSTS = ["localhost","127.0.0.1","testserver"]
    [ ] urls.py: LoginView + LogoutView registrados en /accounts/
    [ ] templates/registration/login.html con {% csrf_token %}
    [ ] @login_required en crear, editar y eliminar (3 vistas)
    [ ] base.html: nav condicional {% if user.is_authenticated %}
    [ ] 11 aserciones verificadas (anónimo→302 / autenticado→200 / ciclo)
    [ ] sprint3_planning.md con Sprint Goal + HU-05/06 Done + HU-07 To Do
    [ ] Kanban: HU-05→Done, HU-06→Done, HU-07→To Do
    [ ] Commit en sprint3/autenticacion-cbv publicado
    [ ] Notas PC1–PC6 e IA-1, IA-2, IA-3 completas

CONCEPTOS CLAVE
    django.contrib.auth (baterías incluidas) · ALLOWED_HOSTS ·
    LOGIN_URL / LOGIN_REDIRECT_URL / LOGOUT_REDIRECT_URL ·
    LoginView · LogoutView · registration/login.html ·
    @login_required · ?next= · Http 302 a login ·
    user.is_authenticated · user.username · nav condicional ·
    Sprint 3 · backlog grooming · HU-07 CBV pendiente

TAREA DE INVESTIGACIÓN (entregar el lunes)
    Investiga: ¿qué es una Vista Basada en Clases (CBV) en Django?
    ¿Cuál es la diferencia entre una vista de función y una vista
    de clase? Trae el ejemplo mínimo de ListView en la libreta.

PREGUNTA DE REFLEXIÓN FINAL
    @login_required es un decorador que añade seguridad a una función
    sin modificar su código interno. Un Sprint Goal añade dirección
    a un sprint sin modificar las historias individuales.
    ¿Qué principio de diseño comparten los dos mecanismos?
```

---

## Resumen semanal (Google Classroom)

| Día | Actividad en Classroom | Producto | Plazo |
|---|---|---|---|
| Lunes | Diagrama auth + rama sprint3 | Diagrama flujo auth + `settings.py` con `ALLOWED_HOSTS` | Lunes 19:30 |
| Martes | `LoginView`/`LogoutView` + `login.html` | `urls.py` + `templates/registration/login.html` | Martes 19:30 |
| Miércoles | `@login_required` + nav condicional | `views.py` + `base.html` + 11 aserciones OK | Miércoles 19:30 |
| Jueves | Sprint 3 Planning + Kanban | `sprint3_planning.md` + URL Kanban actualizado | Jueves 19:30 |
| Viernes | Carpeta final + autoevaluación | Código + planning + retro + PC7 | Viernes 19:30 |

---

### Conteo de cumplimiento (verificación de reglas del ROL 3)
- Puntos de control: **PC1–PC7 (7 ≥ 5 mínimo)** ✓ · PC7 con checklist (11 ítems) + conceptos + tarea + reflexión ✓
- Investigaciones rápidas con IA: **IA-1 (martes), IA-2 (miércoles), IA-3 (jueves) = 3 ≥ 3 mínimo** ✓
- Bloques fijos diarios: arranque 5 min a las 16:45 · buffer 15 min al cierre · pausas activas cada ~45–60 min ✓
- Todos los días suman **180 min** verificados aritméticamente ✓ · Mini-exposiciones ≤10 min ✓
- Sprint 3 Planning simulado el lunes (definir Sprint Goal en equipo antes de la práctica) ✓
- Demo auth en Sprint Review del viernes: anónimo→login→crear→logout→bloqueado en vivo ✓
- Tarea de investigación prepara Semana 9 (`ListView`, CBV) ✓
- Reflexión PC7 conecta `@login_required` (decorador = añadir sin modificar) con Sprint Goal (dirección = añadir sin modificar HUs) ✓

---

*Plan generado bajo ROL 3 — MicroEnseñanza · Prompt Maestro v1.0 · Metodología Tobón · Google Classroom.*
