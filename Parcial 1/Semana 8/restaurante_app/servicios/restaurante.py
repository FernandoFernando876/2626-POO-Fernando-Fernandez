from typing import List, Optional
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """
    Servicio que administra productos y clientes.
    Encapsula las colecciones internas y provee métodos para registrar y listar.
    """

    def __init__(self) -> None:
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []

    # Productos
    def registrar_producto(self, producto: Producto) -> bool:
        """
        Registra un Producto o una Bebida. Devuelve True si se agregó, False si el código ya existía.
        """
        if self._existe_codigo_producto(producto.codigo):
            return False
        self._productos.append(producto)
        return True

    def _existe_codigo_producto(self, codigo: str) -> bool:
        codigo = codigo.strip()
        return any(p.codigo == codigo for p in self._productos)

    def listar_productos(self) -> List[str]:
        """
        Devuelve una lista de cadenas con la información de cada producto.
        Usa polimorfismo: llama a mostrar_informacion() sin preguntar el tipo concreto.
        """
        return [p.mostrar_informacion() for p in self._productos]

    def obtener_producto(self, codigo: str) -> Optional[Producto]:
        codigo = codigo.strip()
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    # Clientes
    def registrar_cliente(self, cliente: Cliente) -> bool:
        """
        Registra un cliente. Devuelve True si se agregó, False si la identificación ya existía.
        """
        if self._existe_identificacion_cliente(cliente.identificacion):
            return False
        self._clientes.append(cliente)
        return True

    def _existe_identificacion_cliente(self, identificacion: str) -> bool:
        identificacion = identificacion.strip()
        return any(c.identificacion == identificacion for c in self._clientes)

    def listar_clientes(self) -> List[str]:
        return [c.mostrar_informacion() for c in self._clientes]

