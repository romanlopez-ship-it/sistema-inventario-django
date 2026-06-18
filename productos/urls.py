"""URLs de la aplicacion productos — Semana 9 (CBV completo)."""

from django.urls import path
from . import views # Importa las vistas desde la misma carpeta

# Definir el namespace (esto es una buena práctica del Módulo II)
app_name = "productos"          # namespace: evita colisiones entre apps

# Vistas de la aplicacion productos — Semana 9 (CBV completo).
urlpatterns = [
    path("",                                      views.bienvenida,       name="bienvenida"),
    path("productos/",                            views.ProductoListView.as_view(),  name="lista"),
    path("productos/nuevo/",                      views.ProductoCreateView.as_view(),   name="crear"),
    path("productos/<int:producto_id>/",          views.ProductoDetailView.as_view(), name="detalle"),
    path("productos/<int:producto_id>/editar/",   views.ProductoUpdateView.as_view(),  name="editar"),
    path("productos/<int:producto_id>/eliminar/", views.ProductoDeleteView.as_view(),name="eliminar"),
]

# Vistas de la aplicacion productos — Semana 3 y 4. (Comentadas para evitar conflictos con las nuevas CBV)
'''
urlpatterns = [
    path("",                                      views.bienvenida,       name="bienvenida"),
    path("productos/",                            views.lista_productos,  name="lista"),
    path("productos/nuevo/",                      views.crear_producto,   name="crear"),
    path("productos/<int:producto_id>/",          views.detalle_producto, name="detalle"),
    path("productos/<int:producto_id>/editar/",   views.editar_producto,  name="editar"),
    path("productos/<int:producto_id>/eliminar/", views.eliminar_producto,name="eliminar"),
]
'''