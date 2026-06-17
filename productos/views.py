#from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest, HttpResponse

# Datos de ejemplo (sin base de datos — se incorpora en Semana 4)
PRODUCTOS_EJEMPLO: dict[int, dict] = {
    1: {"nombre": "Teclado USB",         "precio": 350.00},
    2: {"nombre": "Monitor 24 pulgadas", "precio": 3200.00},
    3: {"nombre": "Mouse inalambrico",   "precio": 280.00},
}

def bienvenida(request: HttpRequest) -> HttpResponse:
    """Devuelve la pagina principal del sistema.

    Args:
        request: Objeto HttpRequest generado por Django.

    Returns:
        HttpResponse con enlaces a las vistas disponibles.
    """
    html = (
        "<h1>Sistema de Inventario</h1>"
        "<ul>"
        "<li><a href='/productos/'>Ver lista de productos</a></li>"
        "<li><a href='/productos/1/'>Ejemplo: detalle producto 1</a></li>"
        "</ul>"
    )
    return HttpResponse(html)


def lista_productos(request: HttpRequest) -> HttpResponse:
    """Devuelve la lista completa de productos de ejemplo.

    Args:
        request: Objeto HttpRequest generado por Django.

    Returns:
        HttpResponse con un listado HTML de todos los productos.
    """
    items = "".join(
        f"<li><a href='/productos/{pid}/'>{datos['nombre']}</a></li>"
        for pid, datos in PRODUCTOS_EJEMPLO.items()
    )
    html = f"<h1>Lista de productos ({len(PRODUCTOS_EJEMPLO)})</h1><ul>{items}</ul>"
    return HttpResponse(html)


def detalle_producto(request: HttpRequest, producto_id: int) -> HttpResponse:
    """Devuelve el detalle de un producto segun su ID de URL.

    Args:
        request: Objeto HttpRequest generado por Django.
        producto_id: Identificador entero capturado desde la URL.

    Returns:
        HttpResponse 200 con el detalle del producto, o 404 si no existe.
    """
    producto = PRODUCTOS_EJEMPLO.get(producto_id)
    if producto is None:
        return HttpResponse(
            f"<h1>Producto {producto_id} no encontrado</h1>",
            status=404,
        )
    html = (
        f"<h1>{producto['nombre']}</h1>"
        f"<p>Precio: ${producto['precio']:.2f}</p>"
        f"<p><a href='/productos/'>Volver a la lista</a></p>"
    )
    return HttpResponse(html)