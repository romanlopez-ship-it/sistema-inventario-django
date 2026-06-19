"""Modelos del dominio — Semana 4.

Define la entidad Producto como clase Python que Django
traduce automaticamente a una tabla en la base de datos.
Hilo conector: "Modelar el dominio".
"""

from decimal import Decimal

from django.db import models


class Producto(models.Model):
    """Representa un producto en el sistema de inventario.

    Attributes:
        nombre: Nombre descriptivo del producto.
        precio: Precio unitario con hasta 2 decimales.
        stock: Cantidad disponible en inventario.
        creado: Fecha y hora de alta, asignada automaticamente.
    """

    nombre = models.CharField(
        max_length=200,
        verbose_name="Nombre",
    )
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Precio",
    )
    stock = models.IntegerField(
        default=0,
        verbose_name="Stock",
    )
    creado = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de alta",
    )

    # Agregar en models.py, antes del campo 'creado':
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo",
    )

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre"]

    def __str__(self) -> str:
        """Devuelve representacion legible del producto.

        Returns:
            Cadena con nombre y precio formateado a 2 decimales.
        """
        precio_dec = Decimal(str(self.precio))
        return f"{self.nombre} (${precio_dec:.2f})"