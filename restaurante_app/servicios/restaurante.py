from __future__ import annotations

from typing import Optional, Set

from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    """Servicio encargado de administrar productos y usuarios."""

    def __init__(self, productos: Optional[list[Producto]] = None) -> None:
        self._productos: list[Producto] = productos.copy() if productos is not None else []
        self._usuarios: list[Usuario] = []

    def obtener_productos(self) -> list[Producto]:
        return self._productos.copy()

    def registrar_producto(self, producto: Producto) -> bool:
        if self._existe_codigo_producto(producto.codigo):
            return False
        self._productos.append(producto)
        return True

    def _existe_codigo_producto(self, codigo: str) -> bool:
        codigo = codigo.strip()
        return any(producto.codigo == codigo for producto in self._productos)

    def listar_productos(self) -> list[str]:
        return [producto.mostrar_informacion() for producto in self._productos]

    def obtener_producto(self, codigo: str) -> Optional[Producto]:
        codigo = codigo.strip()
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

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
        for indice, producto in enumerate(self._productos):
            if producto.codigo == codigo:
                del self._productos[indice]
                return True
        return False

    def obtener_categorias_unicas(self) -> Set[str]:
        return {producto.categoria for producto in self._productos}

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self._existe_identificacion_usuario(usuario.identificacion):
            return False
        self._usuarios.append(usuario)
        return True

    def _existe_identificacion_usuario(self, identificacion: str) -> bool:
        identificacion = identificacion.strip()
        return any(usuario.identificacion == identificacion for usuario in self._usuarios)

    def listar_usuarios(self) -> list[str]:
        return [usuario.mostrar_informacion() for usuario in self._usuarios]

    def eliminar_usuario(self, identificacion: str) -> bool:
        identificacion = identificacion.strip()
        for indice, usuario in enumerate(self._usuarios):
            if usuario.identificacion == identificacion:
                del self._usuarios[indice]
                return True
        return False
