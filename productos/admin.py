"""Registro del modelo Producto en el panel de administracion."""

from django.contrib import admin

from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """Configuracion del modelo Producto en el admin de Django.

    Attributes:
        list_display: columnas visibles en la lista.
        search_fields: campos en los que actua el buscador.
        list_filter: filtros laterales en el panel.
    """

    list_display = ["nombre", "precio", "stock", "creado"]
    search_fields = ["nombre"]
    list_filter = ["creado"]
