from __future__ import annotations

try:
    from modelos.producto import Producto
    from modelos.usuario import Usuario
    from modelos.venta import Venta
    from servicios.archivo_servicio import ArchivoServicio
except ImportError:  # pragma: no cover
    from restaurante_app.modelos.producto import Producto
    from restaurante_app.modelos.usuario import Usuario
    from restaurante_app.modelos.venta import Venta
    from restaurante_app.servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Coordina validaciones, reglas del restaurante y persistencia."""

    def __init__(self, archivo_servicio: ArchivoServicio | None = None) -> None:
        self.archivo_servicio = archivo_servicio or ArchivoServicio()
        self.productos = self.archivo_servicio.cargar_productos()
        self.usuarios = self.archivo_servicio.cargar_usuarios()
        self.ventas = self.archivo_servicio.cargar_ventas()
        self._asignar_ids_usuarios()

    def listar_productos(self) -> list[Producto]:
        return self.productos.copy()

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios.copy()

    def listar_ventas(self) -> list[Venta]:
        return self.ventas.copy()

    def obtener_producto(self, codigo: str) -> Producto | None:
        codigo = codigo.strip()
        return next((p for p in self.productos if p.codigo.lower() == codigo.lower()), None)

    def obtener_usuario(self, usuario: str | int) -> Usuario | None:
        if isinstance(usuario, int):
            return self.obtener_usuario_por_id(usuario)
        usuario = usuario.strip()
        return next((u for u in self.usuarios if u.usuario.lower() == usuario.lower()), None)

    def obtener_usuario_por_id(self, identificador: int) -> Usuario | None:
        return next((u for u in self.usuarios if u.id == identificador), None)

    def validar_acceso(self, usuario: str, password: str) -> bool:
        usuario_normalizado = usuario.strip()
        password_normalizado = password.strip()
        if not usuario_normalizado or not password_normalizado:
            return False
        usuario_actual = self.obtener_usuario(usuario_normalizado)
        return usuario_actual is not None and usuario_actual.password == password_normalizado

    def registrar_venta(self, usuario_id: str, producto_codigo: str, cantidad: int) -> Venta:
        usuario_id = usuario_id.strip()
        producto_codigo = producto_codigo.strip()
        if not usuario_id or not producto_codigo:
            raise ValueError("Usuario y producto son requeridos para registrar una venta.")
        if self.obtener_usuario(usuario_id) is None:
            raise ValueError(f"No existe el usuario '{usuario_id}'.")
        producto = self.obtener_producto(producto_codigo)
        if producto is None:
            raise ValueError(f"No existe el producto '{producto_codigo}'.")

        producto.vender(cantidad)
        venta = Venta(
            usuario_id=usuario_id,
            producto_codigo=producto.codigo,
            cantidad=cantidad,
            precio_unitario=producto.precio,
        )
        self.archivo_servicio.guardar_productos(self.productos)
        self.ventas.append(venta)
        self.archivo_servicio.guardar_ventas(self.ventas)
        return venta

    def registrar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> Producto:
        if self.obtener_producto(codigo) is not None:
            raise ValueError(f"Ya existe un producto con el código '{codigo}'.")
        producto = Producto(codigo, nombre, categoria, precio, stock)
        self.productos.append(producto)
        self.archivo_servicio.guardar_productos(self.productos)
        return producto

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> Producto:
        if self.obtener_producto(codigo) is None:
            raise ValueError(f"No existe un producto con el código '{codigo}'.")
        producto = Producto(codigo, nombre, categoria, precio, stock)
        self.productos = [p if p.codigo.lower() != codigo.lower() else producto for p in self.productos]
        self.archivo_servicio.guardar_productos(self.productos)
        return producto

    def eliminar_producto(self, codigo: str) -> bool:
        if self.obtener_producto(codigo) is None:
            return False
        self.productos = [p for p in self.productos if p.codigo.lower() != codigo.lower()]
        self.archivo_servicio.guardar_productos(self.productos)
        return True

    def registrar_usuario(
        self,
        usuario: str,
        nombre: str,
        correo: str,
        password: str = "",
        rol: str = "Cliente",
    ) -> Usuario:
        rol_validado = self._validar_rol_gestionable(rol)
        if not password.strip():
            raise ValueError("La contraseña es obligatoria para registrar un usuario.")
        if self.obtener_usuario(usuario) is not None:
            raise ValueError(f"Ya existe un usuario con identificador '{usuario}'.")
        nuevo = Usuario(usuario, nombre, correo, password, rol_validado)
        nuevo.id = self._siguiente_id_usuario()
        self.usuarios.append(nuevo)
        self.archivo_servicio.guardar_usuarios(self.usuarios)
        return nuevo

    def actualizar_usuario(
        self,
        usuario: str,
        nombre: str,
        correo: str,
        password: str = "",
        rol: str = "Cliente",
    ) -> Usuario:
        usuario = usuario.strip()
        existente = self.obtener_usuario(usuario)
        if existente is None:
            raise ValueError(f"No existe un usuario con identificador '{usuario}'.")
        if existente.rol == "Administrador":
            raise ValueError("La cuenta Administrador no se gestiona desde esta sección.")
        rol_validado = self._validar_rol_gestionable(rol)
        actualizado = Usuario(
            usuario,
            nombre,
            correo,
            password.strip() or existente.password,
            rol_validado,
            id=existente.id,
        )
        self.usuarios = [u if u.usuario.lower() != usuario.lower() else actualizado for u in self.usuarios]
        self.archivo_servicio.guardar_usuarios(self.usuarios)
        return actualizado

    def eliminar_usuario(self, usuario: str, usuario_actual: str | None = None) -> bool:
        usuario = usuario.strip()
        existente = self.obtener_usuario(usuario)
        if existente is None:
            return False
        if usuario_actual and existente.usuario.casefold() == usuario_actual.strip().casefold():
            raise ValueError("No puedes eliminar la cuenta que está usando la sesión actual.")
        if existente.rol == "Administrador":
            raise ValueError("La cuenta Administrador no se gestiona desde esta sección.")
        self.usuarios = [u for u in self.usuarios if u.usuario.lower() != usuario.lower()]
        self.archivo_servicio.guardar_usuarios(self.usuarios)
        return True

    @staticmethod
    def _validar_rol_gestionable(rol: str) -> str:
        rol_normalizado = rol.strip().casefold()
        roles_gestionables = ("empleado", "cliente")
        for rol_valido in roles_gestionables:
            if rol_normalizado == rol_valido:
                return rol_valido.capitalize()
        raise ValueError("Solo se pueden asignar los roles Empleado o Cliente.")

    def _siguiente_id_usuario(self) -> int:
        return max((usuario.id or 0 for usuario in self.usuarios), default=0) + 1

    def _asignar_ids_usuarios(self) -> None:
        ids_utilizados: set[int] = set()
        necesita_guardar = False
        for usuario in self.usuarios:
            if usuario.id is None or usuario.id in ids_utilizados:
                usuario.id = self._siguiente_id_usuario()
                necesita_guardar = True
            ids_utilizados.add(usuario.id)
        if necesita_guardar:
            self.archivo_servicio.guardar_usuarios(self.usuarios)


Restaurante = RestauranteServicio
