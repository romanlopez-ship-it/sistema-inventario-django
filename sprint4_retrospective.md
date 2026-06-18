# Sprint 4 Retrospective — Sistema de Inventario
## Fecha: ___________ | Sprint: 4 (Sem 10–11)

### Sprint Goal verificado
"El sistema expone el inventario vía API REST autenticada."
✅ Sprint Goal cumplido.

### Incremento entregado
| HU       | Historia                        | Pts | Estado |
|----------|---------------------------------|-----|--------|
| HU-API-01| GET lista JSON pública          | 3   | ✅ Done|
| HU-API-02| CRUD completo vía API           | 5   | ✅ Done|
| HU-API-03| IsAuthenticatedOrReadOnly       | 2   | ✅ Done|
| HU-API-04| Suite 17 pruebas automatizadas  | 3   | ✅ Done|
**Total: 13 pts**

### Velocidad acumulada del módulo
| Sprint | Semanas | Puntos |
|--------|---------|--------|
| 1      | 1–3     | 4 pts  |
| 2      | 4–6     | 15 pts |
| 3      | 8–9     | 13 pts |
| 4      | 10–11   | 13 pts |
| **Total** | **8 sem** | **45 pts** |

### ¿Qué salió bien?
- DRF generics redujeron el código de las vistas de API al mínimo.
- APIClient + force_authenticate simplificó las pruebas de autenticación.

### ¿Qué mejorar?
- Las pruebas se escribieron al final del sprint, no junto al código.

### Kaizen — acción concreta para Sprint 5
**Acción:** en Sprint 5, cada nueva función va acompañada de al menos
2 tests ANTES de hacer git commit (test-alongside, no test-after).

### Sprint 5 Preview (Semanas 12–13)
Sprint Goal: "Entregar el proyecto integrador final: sistema de
inventario completo, probado y desplegado en el entorno de desarrollo."