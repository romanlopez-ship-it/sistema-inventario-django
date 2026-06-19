# Sistema de Inventario
## Módulo II — Técnico en Programación · UTEC Celaya

### Descripción
Sistema de gestión de inventario construido con Django 4.2 en 13 semanas.

### Stack
- Django 4.2 LTS · DRF 3.x · Python 3.11+
- SQLite (desarrollo) · gunicorn + WhiteNoise (producción)

### Características
- CRUD de productos (web con CBV + API REST)
- Autenticación (LoginRequired / LoginRequiredMixin)
- API REST (GET público / escritura autenticada)
- 17 pruebas automatizadas (modelo + serializer + API)

### Instalación local
pip install -r requirements.txt
python manage.py migrate && python manage.py createsuperuser
python manage.py test productos   # → 17/17 OK
python manage.py runserver

### Endpoints API
GET  /api/productos/         → lista (público)
POST /api/productos/         → crear (autenticado)
GET  /api/productos/<pk>/    → detalle (público)
PUT  /api/productos/<pk>/    → actualizar (autenticado)
PATCH /api/productos/<pk>/   → parcial (autenticado)
DELETE /api/productos/<pk>/  → eliminar (autenticado)