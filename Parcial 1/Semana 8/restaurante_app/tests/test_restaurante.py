import re
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente


def test_registrar_producto_bebida_y_listar():
    r = Restaurante()
    p = Producto("P01", "Pan", "Alimentos", 10.0)
    b = Bebida("B01", "Coca-Cola", "Bebidas", 3.5, "500ml", "lata")

    assert r.registrar_producto(p) is True
    assert r.registrar_producto(b) is True
    # duplicado
    assert r.registrar_producto(Producto("P01", "Pan2", "Alimentos", 12.0)) is False

    productos = r.listar_productos()
    assert len(productos) == 2
    # comprobar que la información incluye atributos de Bebida
    assert any("Tamaño" in s or "Tamaño" in s for s in productos)


def test_registrar_cliente_y_validar_duplicado():
    r = Restaurante()
    c = Cliente("C1", "Ana", "ana@example.com")
    assert r.registrar_cliente(c) is True
    # duplicado por identificación
    assert r.registrar_cliente(Cliente("C1", "Ana2", "ana2@example.com")) is False


def test_mostrar_informacion_polimorfismo():
    p = Producto("PX", "Queso", "Alimentos", 5.0)
    b = Bebida("BX", "Jugo", "Bebidas", 2.0, "250ml", "botella")
    # La salida debe contener los campos básicos
    info_p = p.mostrar_informacion()
    info_b = b.mostrar_informacion()
    assert "Código" in info_p
    assert "Nombre" in info_p
    # Bebida debe incluir campos de bebida
    assert re.search(r"Tama.n?o|Envase", info_b)

