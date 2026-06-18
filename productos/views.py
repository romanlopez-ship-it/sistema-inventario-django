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

### Vistas de la aplicacion productos — Semana 6.

Agrega editar_producto y eliminar_producto.
Refactoriza todas las vistas a get_object_or_404.
Hilo conector: "Ciclo cerrado".

### Vistas de la aplicacion productos — Semana 8.

Protege las operaciones de escritura con @login_required.
Hilo conector: "Usuarios reales".
"""

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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
    """Devuelve el detalle de un producto — refactorizado a get_object_or_404."""
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, "productos/detalle.html", {"producto": producto})

## Vista de creacion de productos (Semana 5)
@login_required
def crear_producto(request: HttpRequest) -> HttpResponse:
    """Maneja la creacion de un nuevo producto con un formulario."""
    """Crear un producto — requiere autenticacion."""
    """Usuarios no autenticados son redirigidos a LOGIN_URL."""
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo producto en la base de datos
            return redirect("productos:lista")  # Redirige a la lista de productos
    else:
        form = ProductoForm()  # Formulario vacio para GET
    return render(request, "productos/crear.html", {"form": form})


## Vistas de edicion y eliminacion de productos (Semana 6)
@login_required
def editar_producto(request: HttpRequest, producto_id: int) -> HttpResponse:
    """Maneja la edicion de un producto existente. — requiere autenticacion."""
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()  # Guarda los cambios en la base de datos
            return redirect("productos:lista")
    else:
        form = ProductoForm(instance=producto)  # Formulario con datos actuales
    return render(request, "productos/editar.html", {"form": form, "producto": producto})

@login_required
def eliminar_producto(request: HttpRequest, producto_id: int) -> HttpResponse:
    """Maneja la eliminacion de un producto. — requiere autenticacion."""
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == "POST":
        producto.delete()  # Elimina el producto de la base de datos
        return redirect("productos:lista")
    return render(request, "productos/eliminar.html", {"producto": producto})
