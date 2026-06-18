"""Serializadores de la aplicacion productos — Semana 10.

Convierte instancias de Producto a JSON y viceversa.
Hilo conector: "Exponer los datos".
"""

from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    """Serializa/deserializa el modelo Producto a formato JSON.

    Attributes:
        Meta.model: Modelo de origen.
        Meta.fields: Campos incluidos en la representacion JSON.
        Meta.read_only_fields: Campos que el servidor asigna automaticamente.
    """
    class Meta:
        model = Producto
        fields = ["id", "nombre", "precio", "stock", "activo", "creado"]
        read_only_fields = ["id", "creado"]