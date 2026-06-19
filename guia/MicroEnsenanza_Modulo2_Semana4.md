# MicroEnseñanza — Módulo II · Semana 4
## Técnico en Programación (SEP 3061300006-23) · UTEC Celaya
### Asesor: MC. Román Fernando López González

| Campo | Detalle |
|---|---|
| Módulo / Semana | II / 4 de 13 |
| Hilo conector | "Modelar el dominio" |
| Submódulos | S1 Frameworks (`models.py`, migraciones, admin, ORM) · S2 Ágiles (Fibonacci, Planning Poker, Sprint 2 backlog, Kanban) |
| Stack | Django 4.2 · ORM · SQLite · Python 3.11+ · GitHub Projects |
| Horario | 16:45–19:45 (180 min/día) |
| Plataforma institucional | Google Classroom |
| Tiempo fantasma (buffer) | 15 min/día máximo (último bloque) |
| Regla del docente | Expone ≤10 min por bloque; el resto circula y asesora |
| Prerrequisito | Semana 3 — plantillas con herencia + Sprint 1 cerrado en `main` |

**Leyenda de tipos:** 🟡 Arranque en frío · 📖 Mini-exposición (≤10 min) · ✏️ Copia en libreta / Punto de control · 🔍 Investigación rápida con IA · 💻 Práctica de laboratorio · ✅ Verificación/Coevaluación · 🎭 Taller colaborativo · 🗣️ Presentación oral · 📝 Reflexión/Retrospectiva · 📤 Subir a Classroom · 🔄 Anticipo del día siguiente · ⏸️ Pausa activa · 🆓 Buffer

---

## LUNES — Momento Tobón: APERTURA
**Propósito:** problema de persistencia + ORM (clase→tabla) + escala Fibonacci + rúbrica + crear rama Sprint 2.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "reinicia el servidor — ¿dónde están los productos que creaste la semana pasada?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | El problema de persistencia: RAM vs. BD; el ORM como traductor clase→tabla | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC1** — copia los tipos de campo Django y la estructura mínima de un modelo | Nota PC1 | Libreta | — |
| 17:10 | 25 | 🎭 | Dibujar en libreta: clase `Producto` (Python) → tabla `productos_producto` (SQL), columnas y tipos | Diagrama ORM | Libreta | — |
| 17:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:40 | 10 | 📖 | Escala Fibonacci: estimación relativa vs. horas absolutas; por qué los saltos no son lineales | — | Pizarrón | — |
| 17:50 | 10 | ✏️ | **PC2** — copia la escala Fibonacci y la tabla de referencia de historias | Nota PC2 | Libreta | — |
| 18:00 | 25 | 🎭 | Planning Poker básico: estimar HU-01, HU-02 y HU-03 en equipos de 3 | Estimaciones | Libreta | — |
| 18:25 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:30 | 25 | ✅ | Revisión de la **rúbrica** + `manage.py check` del proyecto de la Semana 3 | Check sin errores | Terminal | Classroom |
| 18:55 | 25 | 💻 | Crear rama `sprint2/modelos-orm` desde `main` | Rama creada | Terminal/GitHub | — |
| 19:20 | 10 | 📤🔄 | Subir diagrama ORM + estimaciones del Planning Poker + anticipo del martes | Evidencia subida | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC1 — Tipos de campo Django y estructura del modelo
models.CharField(max_length=N)           texto corto (VARCHAR)
models.DecimalField(max_digits, decimal_places)  decimal exacto
models.IntegerField(default=0)           entero
models.DateTimeField(auto_now_add=True)  fecha/hora automática al crear
models.BooleanField(default=True)        verdadero/falso

Estructura mínima:
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        ordering = ["nombre"]       # orden por defecto en consultas
    def __str__(self):
        return self.nombre          # etiqueta legible en el admin
```
```
PC2 — Escala Fibonacci para estimación
1 · 2 · 3 · 5 · 8 · 13 · 21  (puntos de historia)
Referencia:
  1 pt  → mínimo esfuerzo (hola mundo)
  2 pt  → un poco más (vista simple)
  3 pt  → moderado (modelo + admin)
  5 pt  → complejo (formulario propio)
  8 pt  → muy complejo (autenticación)
Los puntos miden COMPLEJIDAD RELATIVA, no horas de reloj.
```

---

## MARTES — Momento Tobón: DESARROLLO (inicio)
**Propósito:** escribir `models.py` + ciclo completo de migraciones.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué hace `makemigrations`?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | Ciclo de migraciones: `makemigrations` → `migrate` → `showmigrations`; el archivo `.py` como control de versiones del esquema | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC3** — copia los 3 comandos del ciclo de migraciones | Nota PC3 | Libreta | — |
| 17:10 | 20 | 🔍 | **IA-1**: investigar y copiar resultado en libreta | Nota IA-1 | IA + Libreta | — |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 35 | 💻 | Escribir `models.py` completo: 4 campos + `Meta` + `__str__` | `models.py` | VS Code | — |
| 18:10 | 25 | 💻 | `makemigrations productos` → `migrate` → `showmigrations` → leer `0001_initial.py` | Migración aplicada | Terminal | — |
| 18:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:40 | 20 | ✅ | Verificar: `manage.py check` sin errores + `[X] 0001_initial` en `showmigrations` | Check OK + migración OK | Terminal | — |
| 19:00 | 15 | 📤🔄 | Subir `models.py` + captura de `showmigrations` + anticipo del miércoles | Avance subido | Classroom | Classroom |
| 19:15 | 15 | 🎭 | Revisión en parejas: comparar `models.py` — ¿coinciden los 4 campos y el `ordering`? | Lista de cotejo | — | — |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC3 — Ciclo de migraciones
# 1. Detectar cambios en models.py y generar archivo
python3 manage.py makemigrations productos
# → productos/migrations/0001_initial.py

# 2. Aplicar la migración a la base de datos
python3 manage.py migrate
# → OK en cada migración aplicada

# 3. Verificar estado
python3 manage.py showmigrations productos
# → [X] 0001_initial   (X = aplicada)

# Regla: siempre makemigrations ANTES de migrate.
# Nunca editar el archivo .py de migración a mano.
```
```
IA-1 (copiar pregunta y resultado):
Pregunta: ¿Qué es una migración en Django y por qué se genera un
archivo .py en lugar de ejecutar el SQL directamente?
Resultado: ____________________________________________
```

---

## MIÉRCOLES — Momento Tobón: DESARROLLO (profundización)
**Propósito:** `admin.py` + `createsuperuser` + operar el panel + actualizar vistas con ORM.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué devuelve `Producto.objects.all()`?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | ORM: `objects.all()`, `filter()`, `get()`; `@admin.register` y `list_display` | — | Pizarrón | — |
| 17:00 | 15 | 🔍 | **IA-2**: investigar y copiar resultado en libreta | Nota IA-2 | IA + Libreta | — |
| 17:15 | 10 | ✏️ | **PC4** — copia `@admin.register` y las 3 consultas ORM clave | Nota PC4 | Libreta | — |
| 17:25 | 10 | 💻 | Inicio `admin.py`: decorador `@admin.register` + clase `ProductoAdmin` | Avance admin | VS Code | — |
| 17:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:40 | 25 | 💻 | Completar `admin.py` + `createsuperuser` + `runserver` → abrir `/admin/` | Admin operando | Navegador | — |
| 18:05 | 30 | 💻 | Operar el admin: crear 3 productos reales, editar uno, probar el buscador | 3 productos en BD | Admin panel | — |
| 18:35 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:40 | 20 | 💻 | Actualizar `views.py`: reemplazar diccionario por `objects.all()` y `objects.get(pk=)` | Vistas con ORM | VS Code | — |
| 19:00 | 15 | ✅ | Verificar `/productos/` y `/productos/1/` con datos reales del admin | Datos reales en vistas | Navegador | — |
| 19:15 | 15 | 📤🔄 | Subir `admin.py` + `views.py` + captura del panel admin + anticipo del jueves | Entregables subidos | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC4 — @admin.register y consultas ORM
# admin.py
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display  = ["nombre", "precio", "stock", "creado"]
    search_fields = ["nombre"]      # buscador en el panel
    list_filter   = ["creado"]      # filtro lateral

# Consultas ORM en views.py
Producto.objects.all()              # todos los productos
Producto.objects.filter(precio__lte=400)  # precio <= 400
Producto.objects.get(pk=producto_id)      # uno por pk
# → lanza Producto.DoesNotExist si no existe → usar try/except
```
```
IA-2 (copiar pregunta y resultado):
Pregunta: ¿Qué ventaja tiene el panel admin de Django para un equipo
de desarrollo en las primeras etapas de un proyecto?
Resultado: ____________________________________________
```

---

## JUEVES — Momento Tobón: CIERRE (inicio)
**Propósito:** actualizar plantillas + Sprint 2 Planning + Kanban + flashcards.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué columna del Kanban corresponde a tu modelo hoy?" | Respuesta rápida | Libreta | — |
| 16:50 | 10 | 📖 | Sprint 2 Planning: Sprint Goal, selección de HUs estimadas, tablero Kanban | — | Pizarrón | — |
| 17:00 | 10 | ✏️ | **PC5** — copia el formato del Sprint 2 Planning y las columnas del Kanban | Nota PC5 | Libreta | — |
| 17:10 | 20 | 🔍 | **IA-3**: investigar y copiar resultado en libreta | Nota IA-3 | IA + Libreta | — |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 25 | 💻 | Actualizar `lista.html` (`p.pk`, `p.stock`) y `detalle.html` (`p.stock`) + verificar en navegador | Plantillas con campos del modelo | VS Code | — |
| 18:00 | 30 | 💻 | Redactar `sprint2_planning.md` + crear tablero Kanban en GitHub Projects + mover HU-02 a "In Progress" | `sprint2_planning.md` + Kanban | GitHub | GitHub |
| 18:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:35 | 25 | 🎭 | Taller de **flashcards** de la semana | 8 flashcards | Libreta/Quizlet | — |
| 19:00 | 15 | ✏️ | **PC6** — copia conceptos clave para flashcards | Nota PC6 | Libreta | — |
| 19:15 | 15 | 📤🔄 | Subir `sprint2_planning.md` + URL del tablero Kanban + anticipo del viernes | Enlace subido | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta:**
```
PC5 — Sprint 2 Planning y tablero Kanban
Sprint Goal: "El administrador puede gestionar productos (crear,
editar, eliminar) desde el panel admin y a través de formularios
propios, con datos persistidos en la base de datos."

Historias estimadas (puntos Fibonacci):
  HU-BD   Modelo + migraciones + ORM        3 pts  ✅ Hecho
  HU-02   Panel admin: crear y editar        2 pts  In Progress
  HU-03   Formulario propio: crear           5 pts  To Do
  HU-04   Formulario propio: editar          5 pts  To Do

Columnas del Kanban:
  Backlog | To Do | In Progress | Done
```
```
PC6 — Conceptos clave (flashcards)
ORM · models.Model · CharField · DecimalField · IntegerField
DateTimeField(auto_now_add) · Meta · __str__ · makemigrations
migrate · showmigrations · @admin.register · list_display
objects.all() · objects.get(pk=) · DoesNotExist · puntos de historia
Fibonacci · Planning Poker · Sprint Goal · Kanban · In Progress
```
```
IA-3 (copiar pregunta y resultado):
Pregunta: ¿Por qué se usa la escala Fibonacci para estimar puntos de
historia en lugar de números lineales (1,2,3,4...)? ¿Qué ventaja tiene?
Resultado: ____________________________________________
```

---

## VIERNES — Momento Tobón: CIERRE (conclusión)
**Propósito:** Sprint Review + coevaluación + retrospectiva.

| Hora | Duración | Tipo | Descripción | Producto | Herramienta | Reportar en |
|---|---|---|---|---|---|---|
| 16:45 | 5 | 🟡 | Arranque en frío: "¿qué cambia cuando las vistas usan el ORM en vez del diccionario?" | Respuesta rápida | Libreta | — |
| 16:50 | 30 | 🗣️ | **Sprint Review**: demostrar el modelo en el admin (CRUD real) + vistas con datos reales + Sprint 2 Planning | Demostración | Admin/Navegador/Proyector | — |
| 17:20 | 10 | ✅ | Coevaluación con rúbrica entre pares | Rúbrica llena | Classroom | Classroom |
| 17:30 | 5 | ⏸️ | Pausa activa | — | — | — |
| 17:35 | 30 | ✅ | Verificación final: 8 aserciones (modelo · `__str__` · ordering · filter · lista ORM · detalle · 404 · admin) | Checklist validado | Terminal/Admin | — |
| 18:05 | 20 | 📝 | **Retrospectiva**: qué funcionó / qué mejorar | Notas retro | Libreta | — |
| 18:25 | 5 | ⏸️ | Pausa activa | — | — | — |
| 18:30 | 30 | 🎭 | Repaso colaborativo con flashcards (juego por equipos) | Puntaje equipo | Quizlet/Libreta | — |
| 19:00 | 15 | ✏️ | **PC7** — cierre de la semana (ver texto abajo) | Nota PC7 | Libreta | — |
| 19:15 | 15 | 📤 | Subir evidencias finales + autoevaluación | Carpeta semana 4 | Classroom | Classroom |
| 19:30 | 15 | 🆓 | Buffer | — | — | — |

**Texto exacto para libreta — PC7 (cierre obligatorio):**
```
PC7 — CIERRE SEMANA 4 "Modelar el dominio"

[ ] CHECKLIST DE ENTREGABLES
    [ ] models.py con 4 campos (nombre/precio/stock/creado), Meta y __str__
    [ ] makemigrations: 0001_initial.py generado
    [ ] migrate: [X] 0001_initial en showmigrations
    [ ] admin.py con @admin.register, list_display y search_fields
    [ ] createsuperuser creado y /admin/ operando con CRUD real
    [ ] views.py con objects.all() y objects.get(pk=) / DoesNotExist
    [ ] lista.html y detalle.html usando atributos del modelo (p.pk, p.stock)
    [ ] sprint2_planning.md con Sprint Goal + 4 HUs estimadas
    [ ] Tablero Kanban con HU-02 en "In Progress"
    [ ] Rama sprint2/modelos-orm con commit publicado
    [ ] Notas PC1–PC6 e IA-1, IA-2, IA-3 completas

CONCEPTOS CLAVE
    ORM · models.Model · CharField/DecimalField/IntegerField/DateTimeField ·
    class Meta · __str__ · makemigrations · migrate · showmigrations ·
    @admin.register · list_display · objects.all/get/filter ·
    DoesNotExist · puntos de historia · Fibonacci · Planning Poker ·
    Sprint Goal · Kanban (Backlog/To Do/In Progress/Done)

TAREA DE INVESTIGACIÓN (entregar el lunes)
    Investiga: ¿qué es un ModelForm en Django y para qué sirve?
    ¿Cómo genera automáticamente un formulario HTML a partir de
    un modelo? Trae un ejemplo mínimo en la libreta.

PREGUNTA DE REFLEXIÓN FINAL
    El modelo Producto define campos con tipos (CharField, Decimal...).
    Un ModelForm hereda esos tipos para validar entradas del usuario.
    ¿En qué se parece esto a {% extends "base.html" %} en las plantillas?
```

---

## Resumen semanal (Google Classroom)

| Día | Actividad en Classroom | Producto | Plazo |
|---|---|---|---|
| Lunes | Diagrama ORM + estimaciones Planning Poker + rama sprint2 | Diagrama clase→tabla + tabla Fibonacci con HUs estimadas | Lunes 19:30 |
| Martes | `models.py` + migración | `models.py` + captura de `showmigrations [X] 0001_initial` | Martes 19:30 |
| Miércoles | Admin operando + vistas ORM | `admin.py` + `views.py` + captura del panel admin con 3 productos | Miércoles 19:30 |
| Jueves | Sprint 2 Planning + Kanban | `sprint2_planning.md` + URL del tablero Kanban | Jueves 19:30 |
| Viernes | Carpeta final + autoevaluación | Código + planning + retro + PC7 | Viernes 19:30 |

---

### Conteo de cumplimiento (verificación de reglas del ROL 3)
- Puntos de control: **PC1–PC7 (7 ≥ 5 mínimo)** ✓ · PC7 con checklist (11 ítems) + conceptos + tarea + reflexión ✓
- Investigaciones rápidas con IA: **IA-1 (martes), IA-2 (miércoles), IA-3 (jueves) = 3 ≥ 3 mínimo** ✓
- Bloques fijos diarios: arranque 5 min a las 16:45 · buffer 15 min al cierre · pausas activas cada ~45–60 min ✓
- Todos los días suman **180 min** verificados aritméticamente ✓ · Mini-exposiciones ≤10 min ✓
- Continuidad con Semana 3: parte del proyecto con plantillas de herencia y Sprint 1 cerrado ✓
- Tarea de investigación prepara Semana 5 (ModelForm y formularios propios) ✓
- Sprint 2 arrancado formalmente con Kanban y estimaciones ✓

---

*Plan generado bajo ROL 3 — MicroEnseñanza · Prompt Maestro v1.0 · Metodología Tobón · Google Classroom.*
