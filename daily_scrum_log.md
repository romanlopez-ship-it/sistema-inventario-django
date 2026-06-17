# Daily Scrum Log — Sprint 2
## Sistema de Inventario

### Martes (Semana 5)
| Pregunta | Respuesta |
|---|---|
| ¿Qué hice ayer? | Creé models.py, ejecuté migraciones y registré el admin |
| ¿Qué haré hoy? | Implementar forms.py y la vista crear_producto |
| ¿Impedimentos? | Sí: error al configurar el orden de URL patterns |
**Resolución del impedimento:** colocar `nuevo/` antes de `<int:producto_id>/`

### Miércoles (Semana 5)
| Pregunta | Respuesta |
|---|---|
| ¿Qué hice ayer? | Implementé forms.py y la vista con ciclo GET/POST |
| ¿Qué haré hoy? | Agregar {% csrf_token %} y mostrar errores en la plantilla |
| ¿Impedimentos? | No |

### Jueves (Semana 5)
| Pregunta | Respuesta |
|---|---|
| ¿Qué hice ayer? | Completé crear.html con errores y csrf |
| ¿Qué haré hoy? | Verificar las 8 aserciones y actualizar el Kanban |
| ¿Impedimentos? | No |

## Actualización del Kanban
- HU-02 (panel admin): ✅ Done
- HU-03 (formulario crear): 🔄 In Progress → completado esta semana