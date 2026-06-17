"""Formularios de la aplicacion productos — Semana 5.

Define ProductoForm como ModelForm vinculado al modelo Producto.
Hilo conector: "El primer incremento funcional".
"""
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    """Formulario de creacion de productos.

    Genera automaticamente campos HTML a partir del modelo Producto.
    Valida tipos, longitudes y campos requeridos antes de guardar.

    Attributes:
        Meta.model: Modelo de origen de los campos.
        Meta.fields: Campos expuestos al usuario (excluye 'creado').
        Meta.labels: Etiquetas visibles en el formulario.
    """

    class Meta:
        model  = Producto
        fields = ["nombre", "precio", "stock"]
        labels = {
            "nombre": "Nombre del producto",
            "precio": "Precio unitario ($)",
            "stock":  "Unidades en stock",
        }