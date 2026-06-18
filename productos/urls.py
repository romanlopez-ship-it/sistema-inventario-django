"""URLs de la aplicacion productos — Semana 10 (web + API REST)."""

from django.contrib.auth import views as auth_views
from django.urls import path
from . import api_views
from . import views

app_name = "productos"

urlpatterns = [
    # Vistas de la aplicacion productos — Semana 9 (CBV completo).
    path("",                                      views.bienvenida,                    name="bienvenida"),
    path("productos/",                            views.ProductoListView.as_view(),    name="lista"),
    path("productos/nuevo/",                      views.ProductoCreateView.as_view(),  name="crear"),
    path("productos/<int:producto_id>/",          views.ProductoDetailView.as_view(),  name="detalle"),
    path("productos/<int:producto_id>/editar/",   views.ProductoUpdateView.as_view(),  name="editar"),
    path("productos/<int:producto_id>/eliminar/", views.ProductoDeleteView.as_view(),  name="eliminar"),
    # Vistas de API REST — Semana 10 (CBV con DRF).
    # ── Autenticacion ──────────────────────────────────────────
    path("accounts/login/",  auth_views.LoginView.as_view(),  name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),

    # ── API REST — prefijo "api/" para separar de las vistas web ──
    path("api/productos/",
         api_views.ProductoListCreateAPIView.as_view(),
         name="api-lista"),
    path("api/productos/<int:pk>/",
         api_views.ProductoRetrieveUpdateDestroyAPIView.as_view(),
         name="api-detalle"),
]

'''
### Vistas de la aplicacion productos — Semana 3 y 4. (Comentadas para evitar conflictos con las nuevas CBV)
urlpatterns = [
    path("",                                      views.bienvenida,       name="bienvenida"),
    path("productos/",                            views.lista_productos,  name="lista"),
    path("productos/nuevo/",                      views.crear_producto,   name="crear"),
    path("productos/<int:producto_id>/",          views.detalle_producto, name="detalle"),
    path("productos/<int:producto_id>/editar/",   views.editar_producto,  name="editar"),
    path("productos/<int:producto_id>/eliminar/", views.eliminar_producto,name="eliminar"),
]
'''