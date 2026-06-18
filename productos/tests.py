"""Suite de pruebas automatizadas — Semana 11.

Cubre modelo, serializer y endpoints de la API REST.
Hilo conector: "Calidad ágil".
"""

from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Producto
from .serializers import ProductoSerializer


# ─────────────────────────────────────────────────────────────
# BLOQUE 1 — Pruebas del modelo
# ─────────────────────────────────────────────────────────────
class ProductoModelTest(TestCase):
    """Pruebas unitarias del modelo Producto."""

    def setUp(self) -> None:
        """Crea un producto de prueba reutilizable en cada test."""
        self.producto = Producto.objects.create(
            nombre="Teclado USB",
            precio=Decimal("350.00"),
            stock=10,
        )

    def test_str_formato_correcto(self) -> None:
        """__str__ devuelve 'Nombre ($precio.2f)'."""
        self.assertEqual(str(self.producto), "Teclado USB ($350.00)")

    def test_ordering_alfabetico(self) -> None:
        """Los productos se ordenan alfabeticamente por nombre."""
        Producto.objects.create(nombre="Monitor", precio=Decimal("3200.00"), stock=5)
        nombres = list(Producto.objects.values_list("nombre", flat=True))
        self.assertEqual(nombres, sorted(nombres))

    def test_activo_default_true(self) -> None:
        """El campo activo tiene default=True."""
        self.assertTrue(self.producto.activo)

    def test_stock_default_cero(self) -> None:
        """El campo stock tiene default=0 cuando no se especifica."""
        p = Producto.objects.create(nombre="Raton", precio=Decimal("200.00"))
        self.assertEqual(p.stock, 0)


# ─────────────────────────────────────────────────────────────
# BLOQUE 2 — Pruebas del serializer
# ─────────────────────────────────────────────────────────────
class ProductoSerializerTest(TestCase):
    """Pruebas unitarias de ProductoSerializer."""

    def test_datos_validos(self) -> None:
        """El serializer acepta datos correctos y es valido."""
        data = {"nombre": "Monitor", "precio": "3200.00",
                "stock": 5, "activo": True}
        s = ProductoSerializer(data=data)
        self.assertTrue(s.is_valid(), s.errors)

    def test_precio_invalido(self) -> None:
        """Precio no numerico produce error en el campo precio."""
        data = {"nombre": "X", "precio": "abc", "stock": 0, "activo": True}
        s = ProductoSerializer(data=data)
        self.assertFalse(s.is_valid())
        self.assertIn("precio", s.errors)

    def test_nombre_requerido(self) -> None:
        """Nombre vacio produce error en el campo nombre."""
        data = {"nombre": "", "precio": "100.00", "stock": 0, "activo": True}
        s = ProductoSerializer(data=data)
        self.assertFalse(s.is_valid())
        self.assertIn("nombre", s.errors)

    def test_read_only_id_ignorado(self) -> None:
        """El campo id es read_only y no aparece en validated_data."""
        data = {"id": 999, "nombre": "X", "precio": "1.00",
                "stock": 0, "activo": True}
        s = ProductoSerializer(data=data)
        s.is_valid()
        self.assertNotIn("id", s.validated_data)

    def test_campos_correctos(self) -> None:
        """El serializer expone exactamente 6 campos definidos."""
        campos = set(ProductoSerializer().fields.keys())
        self.assertEqual(
            campos, {"id", "nombre", "precio", "stock", "activo", "creado"}
        )


# ─────────────────────────────────────────────────────────────
# BLOQUE 3 — Pruebas de la API REST
# ─────────────────────────────────────────────────────────────
class ProductoAPITest(TestCase):
    """Pruebas de integracion de los endpoints de la API."""

    def setUp(self) -> None:
        """Crea usuario, producto y cliente API para cada test."""
        self.client_api = APIClient()
        self.user = User.objects.create_user(
            "testuser", "t@t.com", "test1234"
        )
        self.p1 = Producto.objects.create(
            nombre="Teclado USB", precio=Decimal("350.00"), stock=10
        )

    def test_get_lista_anonimo_200(self) -> None:
        """GET /api/productos/ devuelve 200 y la lista de productos."""
        r = self.client_api.get("/api/productos/")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.data), 1)

    def test_get_detalle_200(self) -> None:
        """GET /api/productos/<pk>/ devuelve 200 con datos correctos."""
        r = self.client_api.get(f"/api/productos/{self.p1.pk}/")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data["nombre"], "Teclado USB")
        self.assertEqual(r.data["precio"], "350.00")

    def test_get_detalle_404(self) -> None:
        """GET /api/productos/9999/ devuelve 404."""
        r = self.client_api.get("/api/productos/9999/")
        self.assertEqual(r.status_code, 404)

    def test_post_anonimo_403(self) -> None:
        """POST sin autenticar devuelve 403 Forbidden."""
        r = self.client_api.post(
            "/api/productos/",
            {"nombre": "X", "precio": "1.00", "stock": 0, "activo": True},
            format="json",
        )
        self.assertEqual(r.status_code, 403)

    def test_post_autenticado_201(self) -> None:
        """POST autenticado crea el producto y devuelve 201 Created."""
        self.client_api.force_authenticate(user=self.user)
        r = self.client_api.post(
            "/api/productos/",
            {"nombre": "Monitor HD", "precio": "2800.00",
             "stock": 3, "activo": True},
            format="json",
        )
        self.assertEqual(r.status_code, 201)
        self.assertTrue(Producto.objects.filter(nombre="Monitor HD").exists())
        self.assertIn("id", r.data)

    def test_put_autenticado_200(self) -> None:
        """PUT autenticado actualiza el producto y devuelve 200."""
        self.client_api.force_authenticate(user=self.user)
        r = self.client_api.put(
            f"/api/productos/{self.p1.pk}/",
            {"nombre": "Teclado Mec", "precio": "750.00",
             "stock": 8, "activo": True},
            format="json",
        )
        self.assertEqual(r.status_code, 200)
        self.p1.refresh_from_db()
        self.assertEqual(self.p1.nombre, "Teclado Mec")

    def test_patch_autenticado_200(self) -> None:
        """PATCH autenticado actualiza solo el stock."""
        self.client_api.force_authenticate(user=self.user)
        r = self.client_api.patch(
            f"/api/productos/{self.p1.pk}/",
            {"stock": 25},
            format="json",
        )
        self.assertEqual(r.status_code, 200)
        self.p1.refresh_from_db()
        self.assertEqual(self.p1.stock, 25)

    def test_delete_autenticado_204(self) -> None:
        """DELETE autenticado elimina el producto y devuelve 204."""
        self.client_api.force_authenticate(user=self.user)
        r = self.client_api.delete(f"/api/productos/{self.p1.pk}/")
        self.assertEqual(r.status_code, 204)
        self.assertFalse(Producto.objects.filter(pk=self.p1.pk).exists())
