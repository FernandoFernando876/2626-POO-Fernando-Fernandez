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
            if (
                usuario_actual.usuario.lower() == usuario_normalizado.lower()
                and usuario_actual.password == contraseña_normalizada
            ):
                return True

        return False

    # Operaciones de productos: registrar, actualizar, eliminar
    def registrar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> Producto:
        if self.obtener_producto(codigo) is not None:
            raise ValueError(f"Ya existe un producto con el código '{codigo}'.")
        producto = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio, stock=stock)
        self.productos.append(producto)
        self.archivo_servicio.guardar_productos(self.productos)
        return producto

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> Producto:
        producto_actual = self.obtener_producto(codigo)
        if producto_actual is None:
            raise ValueError(f"No existe un producto con el código '{codigo}'.")
        # Crear un nuevo objeto para validar los datos
        producto_nuevo = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio, stock=stock)
        # Reemplazar en la lista
        for idx, p in enumerate(self.productos):
            if p.codigo.lower() == codigo.lower():
                self.productos[idx] = producto_nuevo
                break
        self.archivo_servicio.guardar_productos(self.productos)
        return producto_nuevo

    def eliminar_producto(self, codigo: str) -> bool:
        producto_actual = self.obtener_producto(codigo)
        if producto_actual is None:
            return False
        self.productos = [p for p in self.productos if p.codigo.lower() != codigo.lower()]
        self.archivo_servicio.guardar_productos(self.productos)
        return True

    # Operaciones de usuarios: obtener, registrar, actualizar, eliminar
    def obtener_usuario(self, usuario: str) -> Usuario | None:
        usuario = usuario.strip()
        for u in self.usuarios:
            if u.usuario.lower() == usuario.lower():
                return u
        return None

    def registrar_usuario(self, usuario: str, nombre: str, correo: str, password: str = "") -> Usuario:
        if self.obtener_usuario(usuario) is not None:
            raise ValueError(f"Ya existe un usuario con identificador '{usuario}'.")
        nuevo = Usuario(usuario=usuario, nombre=nombre, correo=correo, password=password)
        self.usuarios.append(nuevo)
        self.archivo_servicio.guardar_usuarios(self.usuarios)
        return nuevo

    def actualizar_usuario(self, usuario: str, nombre: str, correo: str, password: str = "") -> Usuario:
        actual = self.obtener_usuario(usuario)
        if actual is None:
            raise ValueError(f"No existe un usuario con identificador '{usuario}'.")
        actualizado = Usuario(usuario=usuario, nombre=nombre, correo=correo, password=password)
        for idx, u in enumerate(self.usuarios):
            if u.usuario.lower() == usuario.lower():
                self.usuarios[idx] = actualizado
                break
        self.archivo_servicio.guardar_usuarios(self.usuarios)
        return actualizado

    def eliminar_usuario(self, usuario: str) -> bool:
        actual = self.obtener_usuario(usuario)
        if actual is None:
            return False
        self.usuarios = [u for u in self.usuarios if u.usuario.lower() != usuario.lower()]
        self.archivo_servicio.guardar_usuarios(self.usuarios)
        return True


Restaurante = RestauranteServicio
