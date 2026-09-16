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

    def obtener_usuario(self, usuario: str) -> Usuario | None:
        usuario_normalizado = usuario.strip()
        for usuario_actual in self.usuarios:
            if usuario_actual.usuario.lower() == usuario_normalizado.lower():
                return usuario_actual
        return None

    def obtener_producto(self, codigo: str) -> Producto | None:
        codigo_normalizado = codigo.strip()
        for producto in self.productos:
            if producto.codigo.lower() == codigo_normalizado.lower():
                return producto
        return None

    def registrar_usuario(self, usuario: str, nombre: str, correo: str, clave: str) -> Usuario:
        usuario_normalizado = usuario.strip()
        nombre_normalizado = nombre.strip()
        correo_normalizado = correo.strip()
        clave_normalizada = clave.strip()

        if not usuario_normalizado:
            raise ValueError("El usuario es obligatorio.")
        if not nombre_normalizado:
            raise ValueError("El nombre es obligatorio.")
        if not correo_normalizado:
            raise ValueError("El correo es obligatorio.")
        if not clave_normalizada:
            raise ValueError("La contrasena es obligatoria.")
        if self.obtener_usuario(usuario_normalizado) is not None:
            raise ValueError("Ya existe un usuario con ese nombre de usuario.")

        nuevo_usuario = Usuario(
            usuario=usuario_normalizado,
            nombre=nombre_normalizado,
            correo=correo_normalizado,
            clave=clave_normalizada,
        )
        self.usuarios.append(nuevo_usuario)
        self.archivo_servicio.guardar_usuarios(self.usuarios)
        return nuevo_usuario

    def buscar_usuario(self, usuario: str) -> Usuario | None:
        return self.obtener_usuario(usuario)

    def actualizar_usuario(self, usuario: str, nombre: str, correo: str, clave: str) -> Usuario:
        usuario_normalizado = usuario.strip()
        nombre_normalizado = nombre.strip()
        correo_normalizado = correo.strip()
        clave_normalizada = clave.strip()

        if not usuario_normalizado:
            raise ValueError("Debes ingresar el usuario a actualizar.")
        if not nombre_normalizado:
            raise ValueError("El nombre es obligatorio.")
        if not correo_normalizado:
            raise ValueError("El correo es obligatorio.")
        if not clave_normalizada:
            raise ValueError("La contrasena es obligatoria.")

        usuario_actual = self.obtener_usuario(usuario_normalizado)
        if usuario_actual is None:
            raise ValueError("No existe un usuario con ese nombre de usuario.")

        usuario_actual.nombre = nombre_normalizado
        usuario_actual.correo = correo_normalizado
        usuario_actual.contrasena = clave_normalizada
        self.archivo_servicio.guardar_usuarios(self.usuarios)
        return usuario_actual

    def eliminar_usuario(self, usuario: str) -> None:
        usuario_normalizado = usuario.strip()
        if not usuario_normalizado:
            raise ValueError("Debes ingresar el usuario a eliminar.")

        usuario_actual = self.obtener_usuario(usuario_normalizado)
        if usuario_actual is None:
            raise ValueError("No existe un usuario con ese nombre de usuario.")

        self.usuarios = [item for item in self.usuarios if item.usuario.lower() != usuario_normalizado.lower()]
        self.archivo_servicio.guardar_usuarios(self.usuarios)

    def registrar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> Producto:
        codigo_normalizado = codigo.strip()
        nombre_normalizado = nombre.strip()
        categoria_normalizada = categoria.strip()

        if not codigo_normalizado:
            raise ValueError("El codigo del producto es obligatorio.")
        if not nombre_normalizado:
            raise ValueError("El nombre del producto es obligatorio.")
        if not categoria_normalizada:
            raise ValueError("La categoria del producto es obligatoria.")

        if self.obtener_producto(codigo_normalizado) is not None:
            raise ValueError("Ya existe un producto con ese codigo.")

        producto = Producto(
            codigo=codigo_normalizado,
            nombre=nombre_normalizado,
            categoria=categoria_normalizada,
            precio=precio,
            stock=stock,
        )
        self.productos.append(producto)
        self.archivo_servicio.guardar_productos(self.productos)
        return producto

    def buscar_producto(self, codigo: str) -> Producto | None:
        return self.obtener_producto(codigo)

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> Producto:
        codigo_normalizado = codigo.strip()
        nombre_normalizado = nombre.strip()
        categoria_normalizada = categoria.strip()

        if not codigo_normalizado:
            raise ValueError("Debes escribir el codigo del producto.")
        if not nombre_normalizado:
            raise ValueError("El nombre del producto es obligatorio.")
        if not categoria_normalizada:
            raise ValueError("La categoria del producto es obligatoria.")

        producto = self.obtener_producto(codigo_normalizado)
        if producto is None:
            raise ValueError("No existe un producto con ese codigo.")

        producto.nombre = nombre_normalizado
        producto.categoria = categoria_normalizada
        producto.precio = float(precio)
        producto.stock = int(stock)
        self.archivo_servicio.guardar_productos(self.productos)
        return producto

    def eliminar_producto(self, codigo: str) -> None:
        codigo_normalizado = codigo.strip()
        if not codigo_normalizado:
            raise ValueError("Debes ingresar el codigo del producto a eliminar.")

        producto = self.obtener_producto(codigo_normalizado)
        if producto is None:
            raise ValueError("No existe un producto con ese codigo.")

        self.productos = [item for item in self.productos if item.codigo.lower() != codigo_normalizado.lower()]
        self.archivo_servicio.guardar_productos(self.productos)

    def validar_acceso(self, usuario: str, contrasena: str) -> bool:
        usuario_normalizado = usuario.strip()
        contrasena_normalizada = contrasena.strip()

        if not usuario_normalizado or not contrasena_normalizada:
            return False

        for usuario_actual in self.usuarios:
            if usuario_actual.usuario.lower() == usuario_normalizado.lower() and usuario_actual.contrasena == contrasena_normalizada:
                return True

        return False


Restaurante = RestauranteServicio
