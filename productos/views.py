"""
### Vistas de la aplicacion productos — Semana 3.

Reemplaza HttpResponse con render() y plantillas Django.
Hilo conector: "Historias -> vistas".

### Vistas de la aplicacion productos — Semana 4.

Reemplaza el diccionario de ejemplo por consultas ORM reales.
Hilo conector: "Modelar el dominio".

### Vistas de la aplicacion productos — Semana 5.

Agrega la vista crear_producto con ModelForm y ciclo GET/POST.
Hilo conector: "El primer incremento funcional".
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import ProductoForm
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
    """Devuelve la pagina principal del sistema."""
    return render(request, "base.html", {"titulo": "Bienvenido"})


def lista_productos(request: HttpRequest) -> HttpResponse:
    """Devuelve todos los productos desde la base de datos."""
    productos = Producto.objects.all()
    return render(request, "productos/lista.html", {"productos": productos})


def detalle_producto(request: HttpRequest, producto_id: int) -> HttpResponse:
    """Devuelve el detalle de un producto por su clave primaria."""
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:    
        return HttpResponse(
            f"<h1>Producto {producto_id} no encontrado</h1>",
            status=404,
        )     
    
    return render(request, "productos/detalle.html", {"producto": producto},)

## Vista de creacion de productos (Semana 5)
def crear_producto(request: HttpRequest) -> HttpResponse:
    """Maneja la creacion de un nuevo producto con un formulario."""
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo producto en la base de datos
            return redirect("productos:lista")  # Redirige a la lista de productos
    else:
        form = ProductoForm()  # Formulario vacio para GET

    return render(request, "productos/crear.html", {"form": form})

