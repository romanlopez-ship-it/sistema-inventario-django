"""Vistas de la API REST — Semana 10.

Expone el modelo Producto como API JSON usando DRF generics.
Hilo conector: "Exponer los datos".
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Producto
from .serializers import ProductoSerializer


class ProductoListCreateAPIView(generics.ListCreateAPIView):
    """Lista todos los productos (GET) y crea uno nuevo (POST).

    Permisos:
        - GET  → publico (anónimos pueden leer)
        - POST → requiere autenticacion (403 si no autenticado)

    Attributes:
        queryset: Conjunto de datos que sirve la vista.
        serializer_class: Convierte Producto ↔ JSON.
        permission_classes: IsAuthenticatedOrReadOnly.
    """

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Detalle, edicion completa/parcial y eliminacion de un producto.

    Permisos:
        - GET          → publico
        - PUT/PATCH    → requiere autenticacion
        - DELETE       → requiere autenticacion

    Attributes:
        lookup_field: Campo usado para buscar el objeto ('pk' por defecto).
    """

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "pk"