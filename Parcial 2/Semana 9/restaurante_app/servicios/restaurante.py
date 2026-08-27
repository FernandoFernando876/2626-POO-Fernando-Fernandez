from typing import List, Optional, Set
from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    """
    Servicio que administra productos y clientes.
    Encapsula las colecciones internas y provee métodos para registrar y listar.
    """

    def __init__(self) -> None:
        self._productos: List[Producto] = []
        # Lista dinámica de usuarios (entidad general Usuario)
        self._usuarios: List[Usuario] = []

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

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        """Alias público para buscar un producto por su código."""
        return self.obtener_producto(codigo)

    def actualizar_producto(self, codigo: str, nombre: Optional[str] = None, categoria: Optional[str] = None, precio: Optional[float] = None) -> bool:
        """Actualiza los campos indicados de un producto existente. Devuelve True si se actualizó."""
        p = self.obtener_producto(codigo)
        if p is None:
            return False
        if nombre is not None and nombre.strip():
            p.nombre = nombre.strip()
        if categoria is not None and categoria.strip():
            p.categoria = categoria.strip()
        if precio is not None:
            try:
                precio_val = float(precio)
                if precio_val > 0:
                    p.precio = precio_val
            except (ValueError, TypeError):
                # invalid price — ignore update
                pass
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto por código. Devuelve True si se eliminó."""
        codigo = codigo.strip()
        for idx, p in enumerate(self._productos):
            if p.codigo == codigo:
                del self._productos[idx]
                return True
        return False

    def obtener_categorias_unicas(self) -> Set[str]:
        """Devuelve un conjunto con las categorías únicas de los productos registrados."""
        return set(p.categoria for p in self._productos)

    # Clientes
    def registrar_usuario(self, usuario: Usuario) -> bool:
        """
        Registra un Usuario. Devuelve True si se agregó, False si la identificación ya existía.
        """
        if self._existe_identificacion_usuario(usuario.identificacion):
            return False
        self._usuarios.append(usuario)
        return True

    def _existe_identificacion_usuario(self, identificacion: str) -> bool:
        identificacion = identificacion.strip()
        return any(u.identificacion == identificacion for u in self._usuarios)

    def listar_usuarios(self) -> List[str]:
        return [u.mostrar_informacion() for u in self._usuarios]

    def eliminar_usuario(self, identificacion: str) -> bool:
        """Elimina un usuario por identificación. Devuelve True si se eliminó."""
        identificacion = identificacion.strip()
        for idx, u in enumerate(self._usuarios):
            if u.identificacion == identificacion:
                del self._usuarios[idx]
                return True
        return False

    # Compatibilidad: métodos antiguos que delegan a los nuevos nombres
    def registrar_cliente(self, cliente: Usuario) -> bool:
        return self.registrar_usuario(cliente)

    def _existe_identificacion_cliente(self, identificacion: str) -> bool:
        return self._existe_identificacion_usuario(identificacion)

    def listar_clientes(self) -> List[str]:
        return self.listar_usuarios()

    def eliminar_cliente(self, identificacion: str) -> bool:
        """Compatibilidad: elimina un cliente por identificación delegando al nuevo método."""
        return self.eliminar_usuario(identificacion)


