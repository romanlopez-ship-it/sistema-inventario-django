Aquí tienes un **único archivo en formato Markdown (`ERP_Django.md`)** que reúne toda la información de las últimas respuestas: la guía paso a paso del mini‑ERP en Django, el script Bash automatizado y además un archivo `.bat` para configurar tu USB en Windows.  

Puedes copiar este contenido directamente en Visual Studio Code y guardarlo como `ERP_Django.md`.  

---

```markdown
# 📘 Mini ERP con Django (Portable en USB)

Este proyecto crea un sistema educativo tipo ERP con las entidades:
**Cliente – Proveedor – Producto – Venta – DetalleVenta – Categoría**.  
Usa **Django + SQLite3**, con diseño en **Bootstrap/Tailwind**, **API REST**, pruebas con **TestCase**, y seguridad con **LoginRequiredMixin**.  

---

## 🚀 1. Preparación del entorno

### En tu USB (Linux/Mac/Windows con Git Bash)
```bash
# Crear carpeta del proyecto
mkdir ERP_Django && cd ERP_Django

# Crear entorno virtual portable
python -m venv venv

# Activar entorno
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instalar dependencias
pip install django djangorestframework whitenoise gunicorn
```

---

## 🏗️ 2. Crear proyecto y apps

```bash
django-admin startproject core .
python manage.py startapp clientes
python manage.py startapp proveedores
python manage.py startapp productos
python manage.py startapp ventas
```

En `core/settings.py` agrega:
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "clientes",
    "proveedores",
    "productos",
    "ventas",
]

MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware"]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

---

## 📊 3. Modelos principales (`models.py`)

Ejemplo en `productos/models.py`:
```python
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
```

En `clientes/models.py`:
```python
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
```

En `ventas/models.py`:
```python
from django.db import models
from clientes.models import Cliente
from productos.models import Producto

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta {self.id} - {self.cliente}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.producto} x {self.cantidad}"
```

---

## 🔐 4. Seguridad con `LoginRequiredMixin`

Ejemplo en `ventas/views.py`:
```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Venta

class VentaListView(LoginRequiredMixin, ListView):
    model = Venta
    template_name = "ventas/lista.html"
    login_url = "/login/"
```

---

## 🌐 5. API REST con DRF

En `productos/views.py`:
```python
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
```

En `productos/serializers.py`:
```python
from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"
```

En `core/urls.py`:
```python
from django.urls import path, include
from rest_framework import routers
from productos.views import ProductoViewSet

router = routers.DefaultRouter()
router.register(r"productos", ProductoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
```

---

## 🎨 6. Frontend con Bootstrap/Tailwind

En `templates/base.html`:
```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Mini ERP</title>
  <!-- Bootstrap -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- Tailwind -->
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="container mt-4">
  {% block content %}{% endblock %}
</body>
</html>
```

---

## 🧪 7. Pruebas automáticas (`tests.py`)

Ejemplo en `productos/tests.py`:
```python
from django.test import TestCase
from .models import Categoria, Producto

class ProductoTestCase(TestCase):
    def setUp(self):
        cat = Categoria.objects.create(nombre="Electrónica")
        Producto.objects.create(nombre="Laptop", precio=15000, categoria=cat)

    def test_producto_creado(self):
        laptop = Producto.objects.get(nombre="Laptop")
        self.assertEqual(laptop.precio, 15000)
```

---

## ⚡ 8. Migraciones y ejecución

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Accede a:
- **Admin**: `http://127.0.0.1:8000/admin/`
- **API REST**: `http://127.0.0.1:8000/api/productos/`

---

## 🌍 9. Portabilidad y despliegue

- El proyecto funciona con **sqlite3** (archivo `db.sqlite3` en tu USB).  
- Para producción:  
```bash
gunicorn core.wsgi
```

---

# ⚙️ Script Bash automatizado (`setup_erp.sh`)

```bash
#!/bin/bash
# ============================================================
# 🚀 Script de instalación automática Mini ERP con Django
# Autor: Roman Fernando Lopez Gonzalez
# Uso: ./setup_erp.sh
# ============================================================

mkdir -p ERP_Django && cd ERP_Django
python -m venv venv

if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

pip install --upgrade pip
pip install django djangorestframework whitenoise gunicorn

django-admin startproject core .
python manage.py startapp clientes
python manage.py startapp proveedores
python manage.py startapp productos
python manage.py startapp ventas

python manage.py makemigrations
python manage.py migrate

echo "from django.contrib.auth.models import User; \
User.objects.create_superuser('admin','admin@example.com','admin123')" \
| python manage.py shell

echo "✅ Mini ERP Django instalado correctamente."
echo "Ejecuta: source venv/bin/activate (Linux/Mac) o venv\\Scripts\\activate (Windows)"
echo "Luego: python manage.py runserver"
echo "Admin: http://127.0.0.1:8000/admin/ (usuario: admin / pass: admin123)"
```

---

# ⚙️ Script Windows Batch (`setup_erp.bat`)

```bat
@echo off
REM ============================================================
REM 🚀 Script de instalación automática Mini ERP con Django
REM Autor: Roman Fernando Lopez Gonzalez
REM Uso: setup_erp.bat
REM ============================================================

mkdir ERP_Django
cd ERP_Django

python -m venv venv
call venv\Scripts\activate

pip install --upgrade pip
pip install django djangorestframework whitenoise gunicorn

django-admin startproject core .
python manage.py startapp clientes
python manage.py startapp proveedores
python manage.py startapp productos
python manage.py startapp ventas

python manage.py makemigrations
python manage.py migrate

echo from django.contrib.auth.models import User; User.objects.create_superuser('admin','admin@example.com','admin123') | python manage.py shell

echo ✅ Mini ERP Django instalado correctamente.
echo Activa el entorno con: call venv\Scripts\activate
echo Luego ejecuta: python manage.py runserver
echo Admin: http://127.0.0.1:8000/admin/ (usuario: admin / pass: admin123)
```

---

# ✅ Conclusión
Este mini‑ERP en Django es **portable, modular y educativo**, ideal para aprender conceptos de **Cliente–Proveedor–Producto–Venta–DetalleVenta–Categoría**, con seguridad, API REST y pruebas incluidas.  
Incluye scripts para **Linux/Mac (Bash)** y **Windows (.bat)**, list