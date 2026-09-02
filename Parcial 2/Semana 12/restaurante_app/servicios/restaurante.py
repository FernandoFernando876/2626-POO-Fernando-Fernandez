from __future__ import annotations

from typing import Optional, Set, List

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:
    """Servicio encargado de administrar productos, usuarios y ventas."""

    def __init__(
        self,
        productos: Optional[list[Producto]] = None,
        usuarios: Optional[list[Usuario]] = None,
        ventas: Optional[list[Venta]] = None,
    ) -> None:
        self._productos: List[Producto] = productos.copy() if productos is not None else []
        self._usuarios: List[Usuario] = usuarios.copy() if usuarios is not None else []
        self._ventas: List[Venta] = ventas.copy() if ventas is not None else []

        self._productos_por_codigo: dict[str, Producto] = {}
        self._usuarios_por_identificacion: dict[str, Usuario] = {}
        self._ventas_por_usuario: dict[str, list[Venta]] = {}
        self._reconstruir_indices()

    def _reconstruir_indices(self) -> None:
        self._productos_por_codigo = {producto.codigo: producto for producto in self._productos}
        self._usuarios_por_identificacion = {usuario.identificacion: usuario for usuario in self._usuarios}
        self._ventas_por_usuario = {}
        for venta in self._ventas:
            self._ventas_por_usuario.setdefault(venta.usuario_id, []).append(venta)

    # Productos
    def obtener_productos(self) -> list[Producto]:
        return self._productos.copy()

    def registrar_producto(self, producto: Producto) -> bool:
        if self._existe_codigo_producto(producto.codigo):
            return False
        self._productos.append(producto)
        self._productos_por_codigo[producto.codigo] = producto
        return True

    def _existe_codigo_producto(self, codigo: str) -> bool:
        codigo = codigo.strip()
        return codigo in self._productos_por_codigo

    def listar_productos(self) -> list[str]:
        return [producto.mostrar_informacion() for producto in self._productos]

    def obtener_producto(self, codigo: str) -> Optional[Producto]:
        codigo = codigo.strip()
        return self._productos_por_codigo.get(codigo)

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        return self.obtener_producto(codigo)

    def actualizar_producto(
        self,
        codigo: str,
        nombre: Optional[str] = None,
        categoria: Optional[str] = None,
        precio: Optional[float] = None,
    ) -> bool:
        producto = self.obtener_producto(codigo)
        if producto is None:
            return False

        if nombre is not None and nombre.strip():
            producto.nombre = nombre.strip()
        if categoria is not None and categoria.strip():
            producto.categoria = categoria.strip()
        if precio is not None:
            producto.precio = float(precio)
            if producto.precio <= 0:
                raise ValueError("El precio debe ser mayor que 0.")
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        codigo = codigo.strip()
        producto = self._productos_por_codigo.get(codigo)
        if producto is None:
            return False
        self._productos.remove(producto)
        self._productos_por_codigo.pop(codigo, None)
        return True

    def obtener_categorias_unicas(self) -> Set[str]:
        return {producto.categoria for producto in self._productos}

    # Usuarios
    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self._existe_identificacion_usuario(usuario.identificacion):
            return False
        self._usuarios.append(usuario)
        self._usuarios_por_identificacion[usuario.identificacion] = usuario
        return True

    def _existe_identificacion_usuario(self, identificacion: str) -> bool:
        identificacion = identificacion.strip()
        return identificacion in self._usuarios_por_identificacion

    def listar_usuarios(self) -> list[str]:
        return [usuario.mostrar_informacion() for usuario in self._usuarios]

    def obtener_usuarios(self) -> list[Usuario]:
        return self._usuarios.copy()

    def obtener_usuario(self, identificacion: str) -> Optional[Usuario]:
        identificacion = identificacion.strip()
        return self._usuarios_por_identificacion.get(identificacion)

    def eliminar_usuario(self, identificacion: str) -> bool:
        identificacion = identificacion.strip()
        usuario = self._usuarios_por_identificacion.get(identificacion)
        if usuario is None:
            return False
        self._usuarios.remove(usuario)
        self._usuarios_por_identificacion.pop(identificacion, None)
        return True

    # Ventas
    def obtener_ventas(self) -> list[Venta]:
        return self._ventas.copy()

    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        usuario = self.obtener_usuario(identificacion_usuario)
        producto = self.obtener_producto(codigo_producto)

        if usuario is None:
            return False
        if producto is None:
            return False

        try:
            producto.vender(cantidad)
        except ValueError:
            return False

        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)
        self._ventas_por_usuario.setdefault(venta.usuario_id, []).append(venta)
        return True

    def ventas_por_usuario(self, identificacion_usuario: str) -> list[Venta]:
        identificacion_usuario = identificacion_usuario.strip()
        return list(self._ventas_por_usuario.get(identificacion_usuario, []))
