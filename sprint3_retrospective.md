# Sprint 3 Review + Retrospectiva — Sistema de Inventario
## Fecha: ___________ | Duración: 2 semanas (Sem 8–9)

### Sprint Goal verificado
"Los usuarios autenticados gestionan el inventario; los anónimos
 solo consultan. Las vistas de gestión migran a CBV."
✅ Sprint Goal cumplido.

### Burndown Chart — Sprint 3

| Punto del sprint | HUs completadas              | Pts restantes |
|------------------|------------------------------|---------------|
| Inicio (Sem 8)   | —                            | 13 pts        |
| Fin Sem 8        | HU-05 (5 pts) + HU-06 (3 pts)| 5 pts         |
| Fin Sem 9        | HU-07 (5 pts)                | 0 pts ✅      |

Velocidad Sprint 3: 13 pts / 2 semanas = **6.5 pts/semana**
Velocidad acumulada promedio: ~10 pts/sprint

### Incremento entregado
| HU    | Historia                        | Pts | Estado |
|-------|---------------------------------|-----|--------|
| HU-05 | Login/logout                    | 5   | ✅ Done|
| HU-06 | @login_required                 | 3   | ✅ Done|
| HU-07 | CRUD migrado a CBV              | 5   | ✅ Done|

### ¿Qué salió bien?
- LoginRequiredMixin más limpio que @login_required en CBV.
- reverse_lazy evita errores de orden de inicialización.

### ¿Qué mejorar?
- pk_url_kwarg no es obvio; documentarlo al inicio de cada proyecto.

### Sprint 4 Preview (Semana 10)
Sprint Goal: "El sistema expone datos vía API REST para su consumo."
HU candidatas: API con Django REST Framework (DRF)