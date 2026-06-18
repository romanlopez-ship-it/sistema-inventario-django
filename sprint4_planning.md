# Sprint 4 Planning — Sistema de Inventario
## Fecha: ___________ | Duración: 2 semanas (Sem 10–11)

### Sprint Goal
"El sistema expone el inventario vía API REST autenticada,
consumible por cualquier cliente (móvil, web, Postman)."

### Definición de Terminado (DoD) — Sprint 4
Un endpoint está "terminado" cuando:
  [ ] manage.py check sin errores
  [ ] Aserciones de suite: GET/POST/PUT/PATCH/DELETE pasan
  [ ] read_only_fields correctos (id, creado no aceptan datos externos)
  [ ] IsAuthenticatedOrReadOnly: anónimos→200/403, auth→201/200/204
  [ ] Docstring en la vista con descripción y permisos
  [ ] Migración aplicada ([X] en showmigrations)

### Historias seleccionadas
| ID       | Historia                                        | Pts | Estado    |
|----------|-------------------------------------------------|-----|-----------|
| HU-API-01| GET /api/productos/ → lista JSON pública        | 3   | ✅ Sem 10 |
| HU-API-02| CRUD completo vía API (POST/PUT/PATCH/DELETE)   | 5   | ✅ Sem 10 |
| HU-API-03| IsAuthenticatedOrReadOnly verificado            | 2   | ✅ Sem 10 |
| HU-API-04| Pruebas automatizadas de la API (11 aserciones) | 3   | ✅ Sem 10 |
**Total: 13 pts comprometidos**

### Rama de Git
`sprint4/api-rest`