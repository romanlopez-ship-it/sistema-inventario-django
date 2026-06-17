from django.urls import path
from . import views # Importa las vistas desde la misma carpeta

# Definir el namespace (esto es una buena práctica del Módulo II)
app_name = "productos"          # namespace: evita colisiones entre apps

urlpatterns = [
    path("",                             views.bienvenida,       name="bienvenida"),
    path("productos/",                   views.lista_productos,  name="lista"),
    path("productos/nuevo/",             views.crear_producto,   name="crear"),
    path("productos/<int:producto_id>/", views.detalle_producto, name="detalle"),
]