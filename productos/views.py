"""
Vistas de la aplicacion productos — Semana 3.

Reemplaza HttpResponse con render() y plantillas Django.
Hilo conector: "Historias -> vistas".

Vistas de la aplicacion productos — Semana 4.

Reemplaza el diccionario de ejemplo por consultas ORM reales.
Hilo conector: "Modelar el dominio".
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Producto

'''
# Datos de ejemplo (sin base de datos — se incorpora en Semana 4)
PRODUCTOS_EJEMPLO: dict[int, dict] = {
    1: {"nombre": "Teclado USB",         "precio": 350.00},
    2: {"nombre": "Monitor 24 pulgadas", "precio": 3200.00},
    3: {"nombre": "Mouse inalambrico",   "precio": 280.00},
}
'''

def bienvenida(request: HttpRequest) -> HttpResponse:
    """Devuelve la pagina principal usando la plantilla base.

    Args:
        request: Objeto HttpRequest generado por Django.

    Returns:
        HttpResponse renderizado con base.html.
    """
    return render(request, "base.html", {"titulo": "Bienvenido"})


def lista_productos(request: HttpRequest) -> HttpResponse:
    """Devuelve todos los productos desde la base de datos.

    Args:
        request: Objeto HttpRequest generado por Django.

    Returns:
        HttpResponse renderizado con productos/lista.html.
    """
    productos = Producto.objects.all()
    return render(request, "productos/lista.html", {"productos": productos})


def detalle_producto(request: HttpRequest, producto_id: int) -> HttpResponse:
    """Devuelve el detalle de un producto segun su ID de URL.

    Args:
        request: Objeto HttpRequest generado por Django.
        producto_id: Identificador entero capturado desde la URL.

    Returns:
        HttpResponse 200 con el detalle del producto, o 404 si no existe.
    """
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:    
        return HttpResponse(
            f"<h1>Producto {producto_id} no encontrado</h1>",
            status=404,
        )     
    
    return render(request, "productos/detalle.html", {"producto": producto},)