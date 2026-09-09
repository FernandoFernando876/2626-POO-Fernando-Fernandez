from __future__ import annotations

try:
    from restaurante_app.modelos.producto import Producto
    from restaurante_app.modelos.usuario import Usuario
    from restaurante_app.servicios.archivo_servicio import ArchivoServicio
except ImportError:  # pragma: no cover
    from modelos.producto import Producto
    from modelos.usuario import Usuario
    from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Centraliza la lógica de acceso y consulta del restaurante."""

    def __init__(self, archivo_servicio: ArchivoServicio | None = None) -> None:
        self.archivo_servicio = archivo_servicio or ArchivoServicio()
        self.productos: list[Producto] = self.archivo_servicio.cargar_productos()
        self.usuarios: list[Usuario] = self.archivo_servicio.cargar_usuarios()

    def validar_acceso(self, usuario: str, password: str) -> bool:
        usuario_normalizado = usuario.strip()
        password_normalizado = password.strip()

        if not usuario_normalizado or not password_normalizado:
            return False

        for usuario_actual in self.usuarios:
            if usuario_actual.usuario.lower() == usuario_normalizado.lower() and usuario_actual.password == password_normalizado:
                return True
        return False

    def listar_productos(self) -> list[Producto]:
        return self.productos.copy()

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios.copy()

    def obtener_producto(self, codigo: str) -> Producto | None:
        codigo_normalizado = codigo.strip().lower()
        for producto in self.productos:
            if producto.codigo.lower() == codigo_normalizado:
                return producto
        return None

    def obtener_usuario(self, nombre_usuario: str) -> Usuario | None:
        nombre_normalizado = nombre_usuario.strip().lower()
        for usuario in self.usuarios:
            if usuario.usuario.lower() == nombre_normalizado:
                return usuario
        return None
