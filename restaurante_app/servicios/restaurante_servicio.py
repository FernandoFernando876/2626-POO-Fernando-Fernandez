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
    def __init__(self, archivo_servicio: ArchivoServicio | None = None) -> None:
        self.archivo_servicio = archivo_servicio or ArchivoServicio()
        self.productos = self.archivo_servicio.cargar_productos()
        self.usuarios = self.archivo_servicio.cargar_usuarios()

    def listar_productos(self) -> list[Producto]:
        return self.productos.copy()

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios.copy()

    def obtener_producto(self, codigo: str) -> Producto | None:
        codigo = codigo.strip()
        for producto in self.productos:
            if producto.codigo.lower() == codigo.lower():
                return producto
        return None

    def validar_acceso(self, usuario: str, contraseña: str) -> bool:
        usuario_normalizado = usuario.strip()
        contraseña_normalizada = contraseña.strip()

        if not usuario_normalizado or not contraseña_normalizada:
            return False

        for usuario_actual in self.usuarios:
            if usuario_actual.usuario.lower() == usuario_normalizado.lower() and usuario_actual.password == contraseña_normalizada:
                return True

        return False


Restaurante = RestauranteServicio
