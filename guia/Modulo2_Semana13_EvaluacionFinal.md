# Módulo II · Semana 13 — Evaluación Final
## Técnico en Programación (SEP 3061300006-23) · UTEC Celaya
### Asesor: MC. Román Fernando López González

---

## 1. Identificación de la semana

| Campo | Detalle |
|---|---|
| Carrera | Técnico en Programación |
| Módulo | II — Desarrolla software con herramientas orientadas a la productividad (272 h) |
| Semana | 13 de 13 · **EVALUACIÓN FINAL** |
| Submódulos evaluados | S1 Frameworks (144 h) · S2 Metodologías ágiles (128 h) |
| Periodo evaluado | Semanas 1–12 · 5 sprints · Módulo II completo |
| Carga horaria reportada | 17 h/semana (S1 = 9 h · S2 = 8 h) |

> **Propósito:** la evaluación final no examina memorización —examina que el estudiante construyó un sistema real y funcionando. El eje central del instrumento es la **URL pública** del sistema desplegado: si el sistema responde desde Internet, el trabajo de 13 semanas convergió. Los demás componentes verifican que ese sistema es correcto, probado, seguro, documentado y construido con metodología ágil.

---

## 2. Competencias evaluadas

**Resultado de aprendizaje (SEP):**
El estudiante demuestra dominio del Módulo II entregando un sistema de inventario completo y desplegado que integra: arquitectura Django MVT, CRUD con CBV, autenticación, API REST con DRF, pruebas automatizadas y despliegue en la nube con metodología ágil documentada.

---

## 3. INSTRUMENTO DE EVALUACIÓN

### 3.1 Puntaje global

| Componente | Puntos |
|---|---|
| A — Sistema desplegado y funcional | 25 |
| B — Código y arquitectura | 20 |
| C — Suite de pruebas automatizadas | 15 |
| D — Tarea de extensión práctica | 10 |
| E — Artefactos Scrum (5 sprints) | 20 |
| F — Conocimientos teóricos (10 preguntas) | 10 |
| **Total** | **100** |

> **Acreditación:** ≥ 60 / 100 · Equivalencia Schmelkes: 60=6.0 · 70=7.0 · 80=8.0 · 90=9.0 · 100=10.0
> **Condición mínima:** URL pública accesible + `manage.py test` sin errores.

---

### A — Sistema desplegado y funcional (25 pts)

| Criterio | Puntos | Indicador de verificación |
|---|---|---|
| A1 — URL pública accesible | 5 | `https://<app>.onrender.com` responde con status 200 |
| A2 — CRUD web funcional | 5 | Crear + editar + eliminar productos desde el navegador (autenticado) |
| A3 — Lista pública accesible sin login | 2 | `GET /productos/` → 200 sin autenticar |
| A4 — API REST funcional | 5 | `GET /api/productos/` → JSON 200; `POST` → 201; `DELETE` → 204 |
| A5 — Autenticación en producción | 3 | Login/logout funcionan en la URL pública |
| A6 — Archivos de despliegue correctos | 5 | `requirements.txt` + `Procfile` + `render.yaml` + `settings_prod.py` presentes y funcionales |

> **Verificación técnica directa (evaluador):**
> ```bash
> # En la terminal del alumno:
> DJANGO_SETTINGS_MODULE=inventario_proyecto.settings_prod \
>   python3 manage.py check
> # Esperado: "System check identified no issues (0 silenced)."
>
> # En el navegador:
> # https://<app>.onrender.com/api/productos/  → JSON con lista
> # https://<app>.onrender.com/admin/          → panel admin
> ```

---

### B — Código y arquitectura (20 pts)

| Criterio | Pts | Indicador |
|---|---|---|
| B1 — Modelo con 5 campos, `Meta` y `__str__` | 3 | `ordering`, `verbose_name`, `__str__` devuelve `"Nombre ($X.XX)"` |
| B2 — `ProductoForm` y `ProductoSerializer` separados | 2 | `forms.py` + `serializers.py` como archivos independientes |
| B3 — 5 CBV con atributos correctos | 4 | `pk_url_kwarg`, `context_object_name`, `form_class`, `reverse_lazy` presentes |
| B4 — `LoginRequiredMixin` en las 3 CBV de escritura | 3 | `CreateView`, `UpdateView`, `DeleteView` con mixin en primera posición |
| B5 — `IsAuthenticatedOrReadOnly` en las 2 vistas de API | 2 | `permission_classes` en `ListCreateAPIView` y `RetrieveUpdateDestroyAPIView` |
| B6 — `settings_prod.py` separado de `settings.py` | 3 | Extiende con `from .settings import *`; `DEBUG=False`; `SECRET_KEY` en `os.getenv` |
| B7 — Docstrings en vistas, CBV y API | 3 | Al menos una línea de docstring en cada clase/función de `views.py`, `api_views.py` |

---

### C — Suite de pruebas automatizadas (15 pts)

| Criterio | Pts | Indicador |
|---|---|---|
| C1 — `ProductoModelTest` con ≥ 4 pruebas | 3 | `__str__`, `ordering`, `activo` default, `stock` default |
| C2 — `ProductoSerializerTest` con ≥ 5 pruebas | 4 | datos válidos/inválidos, `read_only`, nombre requerido, campos correctos |
| C3 — `ProductoAPITest` con ≥ 8 pruebas | 5 | GET/POST/PUT/PATCH/DELETE + 403 + 201 + 204 |
| C4 — `manage.py test` → `OK` (todos pasan) | 3 | `Ran N tests … OK` sin `FAIL` ni `ERROR` |

> **Verificación técnica directa:**
> ```bash
> python3 manage.py test productos --verbosity=0
> # Resultado mínimo: "Ran 17 tests … OK"
> ```

---

### D — Tarea de extensión práctica (10 pts)

**Instrucción:** en los primeros **60 minutos** de la sesión del martes, el estudiante agrega el siguiente campo al modelo `Producto` y actualiza todos los archivos necesarios:

```python
# Agregar en models.py, antes del campo 'activo':
descripcion = models.TextField(
    blank=True,
    default="",
    verbose_name="Descripcion",
)
```

**Secuencia completa esperada:**

```bash
# 1. Agregar el campo al modelo
# 2. Nueva migración
python3 manage.py makemigrations productos
# → "Add field descripcion to producto"
python3 manage.py migrate
# → 0002_producto_descripcion aplicada

# 3. Agregar "descripcion" a ProductoSerializer.Meta.fields
# fields = ["id","nombre","descripcion","precio","stock","activo","creado"]

# 4. Ejecutar tests → 1 test falla intencionalmente:
python3 manage.py test productos
# → FAILED (failures=1) — test_campos_correctos esperaba 6 campos, ahora hay 7

# 5. Corregir test_campos_correctos (7 campos) + agregar test nuevo:
def test_descripcion_default_vacio(self) -> None:
    """El campo descripcion tiene default vacío y acepta blank."""
    data = {"nombre":"X","precio":"1.00","stock":0,
            "activo":True,"descripcion":""}
    s = ProductoSerializer(data=data)
    self.assertTrue(s.is_valid(), s.errors)

# 6. Ejecutar tests → 18/18 OK
python3 manage.py test productos
# → Ran 18 tests … OK
```

> **El test que falla intencionalmente** (`test_campos_correctos`) es parte de la evaluación: demuestra que el alumno entiende que la suite refleja contratos —al cambiar el contrato, el test debe actualizarse.

| Sub-criterio | Pts |
|---|---|
| D1 — Campo `descripcion` en `models.py` con `blank=True` y `default=""` | 2 |
| D2 — Migración `0002` generada y aplicada sin errores | 2 |
| D3 — `"descripcion"` agregado a `ProductoSerializer.Meta.fields` | 2 |
| D4 — `test_campos_correctos` corregido (7 campos) + `test_descripcion_default_vacio` añadido | 2 |
| D5 — `manage.py test` → `Ran 18 tests … OK` | 2 |

---

### E — Artefactos Scrum (20 pts)

| Criterio | Pts | Indicador |
|---|---|---|
| E1 — Product Backlog con ≥ 10 HUs y criterios Gherkin en ≥ 3 | 3 | `product_backlog.md` presente; HUs con ID, descripción, puntos, criterios |
| E2 — 5 Sprint Plannings con Sprint Goal | 4 | Un archivo por sprint; Sprint Goal, HUs seleccionadas, estimación |
| E3 — 5 Sprint Retrospectivas con velocidad y kaizen | 5 | Velocidad calculada; ≥ 1 acción kaizen concreta por sprint |
| E4 — DoD definida con ≥ 6 criterios verificables | 3 | `sprint4_planning.md` o archivo equivalente; DoD no es lista de deseos |
| E5 — Burndown chart del Sprint 3 documentado | 2 | Gráfica o tabla con 13→5→0 puntos por semana |
| E6 — Velocidad total del módulo calculada y documentada | 3 | ~60 pts en 13 semanas, promedio por sprint |

---

### F — Conocimientos teóricos (10 pts, 1 pt c/u)

El estudiante responde por escrito en la libreta. El evaluador verifica contra la respuesta mínima.

| # | Pregunta | Respuesta mínima esperada |
|---|---|---|
| F1 | ¿Cuál es la diferencia entre una vista de función y una CBV? ¿Cuándo usarías cada una? | Función = procedimental, explícito; CBV = declarativo, reutilizable; CBV para CRUD estándar, función para lógica ad-hoc |
| F2 | ¿Por qué `LoginRequiredMixin` debe ser el **primer** elemento en la herencia de una CBV? | El MRO de Python ejecuta mixins de izquierda a derecha; si no es primero, la vista puede ejecutarse antes de verificar autenticación |
| F3 | ¿Qué diferencia hay entre `PUT` y `PATCH` en una API REST? | `PUT` reemplaza el objeto completo (todos los campos requeridos); `PATCH` actualiza solo los campos enviados |
| F4 | ¿Qué hace `setUp()` en `TestCase` y por qué se ejecuta antes de cada test? | Crea el estado inicial limpio; se repite para aislar los tests entre sí (cada test parte de cero) |
| F5 | ¿Por qué `DEBUG=False` en producción y qué información expone `DEBUG=True` si ocurre un error? | `DEBUG=True` muestra el traceback completo, variables locales y settings al usuario; expone secretos e información del sistema |
| F6 | ¿Qué es el kaizen y cómo se aplica en la Retrospectiva Scrum? | Mejora continua en pasos pequeños; en la Retrospectiva se identifica UNA acción concreta para el siguiente sprint |
| F7 | ¿Por qué `reverse_lazy` y no `reverse()` en `success_url` de una CBV? | `reverse()` se evalúa cuando se define la clase (antes de que las URLs estén cargadas); `reverse_lazy` se evalúa solo cuando se necesita |
| F8 | ¿Qué hace `WhiteNoise` y por qué Django no sirve estáticos en producción por defecto? | WhiteNoise sirve archivos estáticos desde Python sin servidor externo; Django no los sirve en producción porque es ineficiente sin un servidor dedicado |
| F9 | ¿Cuál es la diferencia entre la DoD y los criterios de aceptación de una historia? | DoD = umbral mínimo universal para cualquier incremento; criterios de aceptación = condiciones específicas de cada historia individual |
| F10 | ¿Qué son los puntos de historia y por qué se usa la escala Fibonacci? | Miden complejidad relativa; Fibonacci porque la incertidumbre crece no linealmente y los números grandes señalan historias que deben partirse |

---

## 4. Autoevaluación del estudiante

Antes del martes, el estudiante completa este checklist como autodiagnóstico:

```
CHECKLIST DE AUTOEVALUACIÓN — Evaluación Final M2

SISTEMA DESPLEGADO
[ ] URL pública en Render accesible desde cualquier dispositivo
[ ] CRUD web: crear + editar + eliminar (autenticado)
[ ] API: GET/POST/PUT/PATCH/DELETE funcionan en producción
[ ] Login/logout funcional en la URL pública

CÓDIGO
[ ] Modelo: 5 campos + Meta + __str__ correcto
[ ] 5 CBV con pk_url_kwarg + context_object_name + reverse_lazy
[ ] LoginRequiredMixin PRIMERO en Create/Update/Delete
[ ] IsAuthenticatedOrReadOnly en ambas vistas de API
[ ] settings_prod.py separado, DEBUG=False, SECRET_KEY en os.getenv

PRUEBAS
[ ] ProductoModelTest ≥ 4 pruebas
[ ] ProductoSerializerTest ≥ 5 pruebas
[ ] ProductoAPITest ≥ 8 pruebas
[ ] manage.py test → OK

DESPLIEGUE
[ ] requirements.txt con gunicorn + whitenoise
[ ] Procfile con gunicorn --bind 0.0.0.0:$PORT
[ ] render.yaml con build/start/envVars
[ ] collectstatic OK

SCRUM
[ ] 5 sprint plannings con Sprint Goal
[ ] 5 retrospectivas con velocidad y kaizen
[ ] DoD con ≥ 6 criterios
[ ] Velocidad total del módulo calculada
```

---

## 5. Criterios de acreditación

| Puntuación | Equiv. Schmelkes | Nivel |
|---|---|---|
| 90–100 | 9.0–10.0 | Sobresaliente |
| 80–89 | 8.0–8.9 | Notable |
| 70–79 | 7.0–7.9 | Bien |
| 60–69 | 6.0–6.9 | Suficiente |
| < 60 | < 6.0 | No acredita |

> **Condición mínima de acreditación:**
> - URL pública accesible (A1 ≥ 5 pts) O evidencia de `gunicorn` corriendo localmente.
> - `manage.py test` sin errores (C4 = 3 pts).
> - Al menos 2 sprint retrospectivas con velocidad (E3 parcial).

---

## 6. Procedimiento de la semana

### Lunes — Presentación del instrumento + autodiagnóstico
El docente presenta el instrumento completo. Los estudiantes realizan el autodiagnóstico y corrigen pendientes. Todos deben tener la URL pública funcionando antes del martes.

### Martes — Tarea de extensión (60 min) + demo técnica (90 min)
**Primeros 60 min:** tarea de extensión (`descripcion` → migración 0002 → serializer → fix test → 18/18 OK).
**Siguientes 90 min:** demo técnica ante el evaluador: URL pública + CRUD web + API REST + `manage.py test`.

### Miércoles — Conocimientos teóricos + revisión de artefactos Scrum
**Primeros 40 min:** preguntas F1–F10 escritas en la libreta.
**Siguientes 80 min:** revisión de artefactos Scrum (5 plannings + 5 retrospectivas + DoD + velocidad).

### Jueves — Retroalimentación individual
El docente entrega las rúbricas completadas. Correcciones para los ítems con puntaje < 1.

### Viernes — Cierre del Módulo II
Autoevaluación, firma de conformidad con la calificación, celebración del sistema desplegado y apertura del Módulo III.

---

## 7. Recursos

- Repositorio GitHub del proyecto con todos los archivos de despliegue.
- URL pública en Render.com.
- Computadora con Python 3.11+, Django 4.2 y VS Code.
- Google Classroom para entrega de evidencias de la evaluación.

---

## 8. Referencias (APA 7)

Django REST Framework. (s.f.). *Django REST framework documentation*. https://www.django-rest-framework.org/

Django Software Foundation. (s.f.). *Deployment checklist*. https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

Django Software Foundation. (s.f.). *Testing in Django*. https://docs.djangoproject.com/en/4.2/topics/testing/

Imai, M. (1986). *Kaizen: The key to Japan's competitive success*. McGraw-Hill.

Schmelkes, C., & Schmelkes, N. (2010). *Manual para la presentación de anteproyectos e informes de investigación* (3.ª ed.). Oxford University Press.

Schwaber, K., & Sutherland, J. (2020). *La guía de Scrum*. https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf

WhiteNoise. (s.f.). *WhiteNoise documentation*. http://whitenoise.evans.io/

---

*Guía de Evaluación Final generada bajo ROL 1/ROL 2 · Prompt Maestro v1.0 · Celaya, junio 2026.*
*Base empírica: tarea de extensión verificada — campo `descripcion` + migración `0002` + test intencionalmente fallido + corrección → 18/18 pasan.*
*Módulo II: 13 semanas · 5 sprints · ~60 pts · 1 sistema desplegado en la nube.*
