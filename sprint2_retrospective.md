# Sprint 2 Retrospective — Sistema de Inventario
## Fecha: ___________

### Sprint Goal verificado
"El administrador puede gestionar productos (crear, editar, eliminar)
desde el panel admin y formularios propios, con datos en la base de datos."
✅ Sprint Goal cumplido.

### Incremento entregado
| Historia | Puntos | Estado |
|---|---|---|
| HU-BD  Modelo + ORM + migraciones | 3 | ✅ Done |
| HU-02  Panel admin CRUD           | 2 | ✅ Done |
| HU-03  Formulario crear           | 5 | ✅ Done |
| HU-04  Formulario editar/eliminar | 5 | ✅ Done |
| **Total Sprint 2**                | **15** | |

### Velocidad del equipo
Sprint 1: 4 pts | Sprint 2: 15 pts | Promedio: ~10 pts/sprint

### ¿Qué salió bien?
- ModelForm redujo el código: un archivo forms.py para crear y editar.
- El panel admin fue útil para poblar datos de prueba rápidamente.

### ¿Qué mejorar?
- Orden de URL patterns causó confusión (nuevo/ vs <int:>/).
- Las pruebas con RequestFactory no capturan Http404 directamente.

### Acción concreta para Sprint 3
Documentar el orden de URLs como estándar del proyecto desde el inicio.

### Sprint 3 — Preview (Semana 8)
Sprint Goal: "Los usuarios deben autenticarse para gestionar productos."
Historias candidatas:
  HU-05  Login/logout                     5 pts
  HU-06  Proteger vistas con @login_required  3 pts
  HU-07  Vistas basadas en clases (CBV)   5 pts
Capacidad estimada: ~10 pts