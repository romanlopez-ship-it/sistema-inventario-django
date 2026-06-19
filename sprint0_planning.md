# Sprint 0 Planning - Sistema de Inventario

**Sprint Goal:** Establecer la infraestructura técnica del framework Django y definir el marco de trabajo ágil (Scrum) para el desarrollo del sistema [3, 9].

## 1. Roles de Scrum
*   **Product Owner:** Docente (MC. Román Fernando López González) [10].
*   **Scrum Master:** [Tu Nombre] [10].
*   **Equipo de Desarrollo:** [Tu Nombre] [10].

## 2. Historias de Usuario Seleccionadas
Para el Sprint 0, el enfoque es la preparación del entorno, aunque se sientan las bases para la primera funcionalidad [3]:
*   **HU-Pre:** Configuración del entorno de desarrollo y repositorio.
*   **HU-01 (Borrador):** Como encargado de bodega quiero ver una bienvenida para confirmar que el sistema está en línea [9].

## 3. Sprint Backlog (Tareas Técnicas)
| Tarea | Prioridad | Estado |
| :--- | :--- | :--- |
| Instalar Django 4.2 y verificar versión [11]. | Alta | Completada |
| Crear proyecto `inventario_proyecto` y app `productos` [11]. | Alta | Completada |
| Configurar `settings.py` (INSTALLED_APPS) [7]. | Alta | Completada |
| Crear vista de bienvenida y configurar `urls.py` [11]. | Alta | Completada |
| Ejecutar `python manage.py migrate` para base de datos inicial [5]. | Media | Completada |

## 4. Sprint Backlog (Tareas de Gestión)
| Tarea | Prioridad | Estado |
| :--- | :--- | :--- |
| Crear `product_backlog.md` con ≥5 historias de usuario [7]. | Alta | Completada |
| Definir criterios de aceptación iniciales [12]. | Media | Pendiente |
| Inicializar repositorio Git y realizar primer commit [5]. | Alta | Completada |
| Configurar rama `main` como línea base estable [3]. | Alta | Completada |

## 5. Definición de Terminado (DoD) para el Sprint 0
*   El comando `python manage.py check` no arroja errores [13].
*   La vista de bienvenida responde con un status HTTP 200 en el navegador [13].
*   El código sigue las normas de estilo PEP 8 [13].
*   Los artefactos de gestión están publicados en GitHub [3].