from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import Callable


class MainView:
    def __init__(
        self,
        root: tk.Misc,
        restaurante_servicio,
        on_logout: Callable[[], None] | None = None,
    ) -> None:
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.on_logout = on_logout

        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)

        self.header = tk.Frame(self.frame, bg="#111827", padx=18, pady=14)
        self.header.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.header.grid_columnconfigure(0, weight=1)

        title = tk.Label(
            self.header,
            text="Panel principal",
            fg="white",
            bg="#111827",
            font=("Arial", 16, "bold"),
        )
        title.grid(row=0, column=0, sticky="w")

        self.nav_frame = tk.Frame(self.frame, bg="#e5e7eb", padx=12, pady=12)
        self.nav_frame.grid(row=1, column=0, sticky="ns", padx=(0, 14))
        self.nav_frame.grid_rowconfigure(5, weight=1)

        self.btn_productos = tk.Button(self.nav_frame, text="Productos", width=18, command=self.mostrar_productos)
        self.btn_productos.grid(row=0, column=0, pady=(0, 8), sticky="ew")

        self.btn_usuarios = tk.Button(self.nav_frame, text="Usuarios", width=18, command=self.mostrar_usuarios)
        self.btn_usuarios.grid(row=1, column=0, pady=(0, 8), sticky="ew")

        self.btn_cerrar = tk.Button(
            self.nav_frame,
            text="Cerrar sesion",
            width=18,
            bg="#dc2626",
            fg="white",
            command=self._logout,
        )
        self.btn_cerrar.grid(row=2, column=0, sticky="ew")

        self.content_frame = tk.Frame(self.frame, bg="#f8fafc")
        self.content_frame.grid(row=1, column=1, sticky="nsew")
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

        self.product_section = ttk.LabelFrame(self.content_frame, text="Gestion de productos", padding=12)
        self.product_section.grid(row=0, column=0, sticky="nsew")
        self.product_section.grid_columnconfigure(0, weight=1)

        self.product_form = ttk.Frame(self.product_section)
        self.product_form.grid(row=0, column=0, sticky="nsew")
        self.product_form.grid_columnconfigure(1, weight=1)

        self.product_vars = {}
        for index, (label_text, key) in enumerate([
            ("Codigo", "codigo"),
            ("Nombre", "nombre"),
            ("Categoria", "categoria"),
            ("Precio", "precio"),
            ("Stock", "stock"),
        ]):
            ttk.Label(self.product_form, text=f"{label_text}:").grid(row=index, column=0, sticky="w", padx=(0, 10), pady=5)
            var = tk.StringVar()
            self.product_vars[key] = var
            ttk.Entry(self.product_form, textvariable=var, width=30).grid(row=index, column=1, sticky="ew", pady=5)

        product_buttons = ttk.Frame(self.product_section)
        product_buttons.grid(row=1, column=0, sticky="ew", pady=(12, 10))
        for col in range(5):
            product_buttons.grid_columnconfigure(col, weight=1)

        ttk.Button(product_buttons, text="Registrar", command=self.registrar_producto).grid(row=0, column=0, padx=(0, 6), sticky="ew")
        ttk.Button(product_buttons, text="Buscar", command=self.buscar_producto).grid(row=0, column=1, padx=6, sticky="ew")
        ttk.Button(product_buttons, text="Actualizar", command=self.actualizar_producto).grid(row=0, column=2, padx=6, sticky="ew")
        ttk.Button(product_buttons, text="Eliminar", command=self.eliminar_producto).grid(row=0, column=3, padx=6, sticky="ew")
        ttk.Button(product_buttons, text="Limpiar", command=self.limpiar_formulario_producto).grid(row=0, column=4, padx=(6, 0), sticky="ew")

        self.product_status_var = tk.StringVar(value="Sistema listo para productos.")
        self.product_status_label = tk.Label(self.product_section, textvariable=self.product_status_var, fg="#1f2937", bg="#f8fafc", anchor="w")
        self.product_status_label.grid(row=2, column=0, sticky="ew", pady=(0, 8))

        self.product_table_frame = ttk.LabelFrame(self.product_section, text="Productos registrados", padding=8)
        self.product_table_frame.grid(row=3, column=0, sticky="nsew")
        self.product_table_frame.grid_columnconfigure(0, weight=1)
        self.product_table_frame.grid_rowconfigure(0, weight=1)

        self.product_table = ttk.Treeview(
            self.product_table_frame,
            columns=("codigo", "nombre", "categoria", "precio", "stock"),
            show="headings",
            height=8,
        )
        self.product_table.heading("codigo", text="Codigo")
        self.product_table.heading("nombre", text="Nombre")
        self.product_table.heading("categoria", text="Categoria")
        self.product_table.heading("precio", text="Precio")
        self.product_table.heading("stock", text="Stock")
        self.product_table.column("codigo", width=90, anchor="center")
        self.product_table.column("nombre", width=180)
        self.product_table.column("categoria", width=120)
        self.product_table.column("precio", width=100, anchor="center")
        self.product_table.column("stock", width=80, anchor="center")
        self.product_table.grid(row=0, column=0, sticky="nsew")

        product_scroll = ttk.Scrollbar(self.product_table_frame, orient="vertical", command=self.product_table.yview)
        product_scroll.grid(row=0, column=1, sticky="ns")
        self.product_table.configure(yscrollcommand=product_scroll.set)

        self.user_section = ttk.LabelFrame(self.content_frame, text="Gestion de usuarios", padding=12)
        self.user_section.grid(row=0, column=0, sticky="nsew")
        self.user_section.grid_columnconfigure(0, weight=1)

        self.user_form = ttk.Frame(self.user_section)
        self.user_form.grid(row=0, column=0, sticky="nsew")
        self.user_form.grid_columnconfigure(1, weight=1)

        self.user_vars = {}
        for index, (label_text, key) in enumerate([
            ("Usuario", "usuario"),
            ("Nombre", "nombre"),
            ("Correo", "correo"),
            ("Contrasena", "clave"),
        ]):
            ttk.Label(self.user_form, text=f"{label_text}:").grid(row=index, column=0, sticky="w", padx=(0, 10), pady=5)
            var = tk.StringVar()
            self.user_vars[key] = var
            if key == "clave":
                tk.Entry(self.user_form, textvariable=var, width=30, show="*").grid(row=index, column=1, sticky="ew", pady=5)
            else:
                ttk.Entry(self.user_form, textvariable=var, width=30).grid(row=index, column=1, sticky="ew", pady=5)

        user_buttons = ttk.Frame(self.user_section)
        user_buttons.grid(row=1, column=0, sticky="ew", pady=(12, 10))
        for col in range(5):
            user_buttons.grid_columnconfigure(col, weight=1)

        ttk.Button(user_buttons, text="Registrar", command=self.registrar_usuario).grid(row=0, column=0, padx=(0, 6), sticky="ew")
        ttk.Button(user_buttons, text="Buscar", command=self.buscar_usuario).grid(row=0, column=1, padx=6, sticky="ew")
        ttk.Button(user_buttons, text="Actualizar", command=self.actualizar_usuario).grid(row=0, column=2, padx=6, sticky="ew")
        ttk.Button(user_buttons, text="Eliminar", command=self.eliminar_usuario).grid(row=0, column=3, padx=6, sticky="ew")
        ttk.Button(user_buttons, text="Limpiar", command=self.limpiar_formulario_usuario).grid(row=0, column=4, padx=(6, 0), sticky="ew")

        self.user_status_var = tk.StringVar(value="Sistema listo para usuarios.")
        self.user_status_label = tk.Label(self.user_section, textvariable=self.user_status_var, fg="#1f2937", bg="#f8fafc", anchor="w")
        self.user_status_label.grid(row=2, column=0, sticky="ew", pady=(0, 8))

        self.user_table_frame = ttk.LabelFrame(self.user_section, text="Usuarios registrados", padding=8)
        self.user_table_frame.grid(row=3, column=0, sticky="nsew")
        self.user_table_frame.grid_columnconfigure(0, weight=1)
        self.user_table_frame.grid_rowconfigure(0, weight=1)

        self.user_table = ttk.Treeview(
            self.user_table_frame,
            columns=("usuario", "nombre", "correo"),
            show="headings",
            height=8,
        )
        self.user_table.heading("usuario", text="Usuario")
        self.user_table.heading("nombre", text="Nombre")
        self.user_table.heading("correo", text="Correo")
        self.user_table.column("usuario", width=120, anchor="center")
        self.user_table.column("nombre", width=220)
        self.user_table.column("correo", width=260)
        self.user_table.grid(row=0, column=0, sticky="nsew")

        user_scroll = ttk.Scrollbar(self.user_table_frame, orient="vertical", command=self.user_table.yview)
        user_scroll.grid(row=0, column=1, sticky="ns")
        self.user_table.configure(yscrollcommand=user_scroll.set)

        self.user_section.grid_remove()
        self.mostrar_productos()

    def limpiar_formulario_producto(self) -> None:
        for key in self.product_vars:
            self.product_vars[key].set("")
        self.product_status_var.set("Formulario de productos limpio.")
        self.product_status_label.config(fg="#1f2937")

    def registrar_producto(self) -> None:
        try:
            producto = self.restaurante_servicio.registrar_producto(
                codigo=self.product_vars["codigo"].get(),
                nombre=self.product_vars["nombre"].get(),
                categoria=self.product_vars["categoria"].get(),
                precio=self.product_vars["precio"].get(),
                stock=self.product_vars["stock"].get(),
            )
            self.limpiar_formulario_producto()
            self._refrescar_productos()
            self.product_status_var.set(f"Producto '{producto.nombre}' registrado correctamente.")
            self.product_status_label.config(fg="#15803d")
        except ValueError as exc:
            self.product_status_var.set(str(exc))
            self.product_status_label.config(fg="#b91c1c")

    def buscar_producto(self) -> None:
        codigo = self.product_vars["codigo"].get().strip()
        if not codigo:
            self.product_status_var.set("Debes ingresar un codigo para buscar el producto.")
            self.product_status_label.config(fg="#b91c1c")
            return

        producto = self.restaurante_servicio.buscar_producto(codigo)
        if producto is None:
            self.product_status_var.set("No existe un producto con ese codigo.")
            self.product_status_label.config(fg="#b91c1c")
            return

        self.product_vars["codigo"].set(producto.codigo)
        self.product_vars["nombre"].set(producto.nombre)
        self.product_vars["categoria"].set(producto.categoria)
        self.product_vars["precio"].set(str(producto.precio))
        self.product_vars["stock"].set(str(producto.stock))
        self.product_status_var.set(f"Producto '{producto.nombre}' cargado correctamente.")
        self.product_status_label.config(fg="#1d4ed8")

    def actualizar_producto(self) -> None:
        try:
            producto = self.restaurante_servicio.actualizar_producto(
                codigo=self.product_vars["codigo"].get(),
                nombre=self.product_vars["nombre"].get(),
                categoria=self.product_vars["categoria"].get(),
                precio=self.product_vars["precio"].get(),
                stock=self.product_vars["stock"].get(),
            )
            self._refrescar_productos()
            self.product_status_var.set(f"Producto '{producto.nombre}' actualizado correctamente.")
            self.product_status_label.config(fg="#15803d")
        except ValueError as exc:
            self.product_status_var.set(str(exc))
            self.product_status_label.config(fg="#b91c1c")

    def eliminar_producto(self) -> None:
        codigo = self.product_vars["codigo"].get().strip()
        if not codigo:
            self.product_status_var.set("Debes escribir el codigo del producto a eliminar.")
            self.product_status_label.config(fg="#b91c1c")
            return

        try:
            self.restaurante_servicio.eliminar_producto(codigo)
            self.limpiar_formulario_producto()
            self._refrescar_productos()
            self.product_status_var.set("Producto eliminado correctamente.")
            self.product_status_label.config(fg="#15803d")
        except ValueError as exc:
            self.product_status_var.set(str(exc))
            self.product_status_label.config(fg="#b91c1c")

    def _refrescar_productos(self) -> None:
        for fila in self.product_table.get_children():
            self.product_table.delete(fila)
        for producto in self.restaurante_servicio.listar_productos():
            self.product_table.insert(
                "",
                tk.END,
                values=(producto.codigo, producto.nombre, producto.categoria, f"{producto.precio:.2f}", producto.stock),
            )

    def mostrar_productos(self) -> None:
        self.product_section.grid()
        self.user_section.grid_remove()
        self._refrescar_productos()
        self.product_status_var.set("Listado de productos actualizado.")
        self.product_status_label.config(fg="#1f2937")

    def limpiar_formulario_usuario(self) -> None:
        for key in self.user_vars:
            self.user_vars[key].set("")
        self.user_status_var.set("Formulario de usuarios limpio.")
        self.user_status_label.config(fg="#1f2937")

    def registrar_usuario(self) -> None:
        try:
            usuario = self.restaurante_servicio.registrar_usuario(
                usuario=self.user_vars["usuario"].get(),
                nombre=self.user_vars["nombre"].get(),
                correo=self.user_vars["correo"].get(),
                clave=self.user_vars["clave"].get(),
            )
            self.limpiar_formulario_usuario()
            self._refrescar_usuarios()
            self.user_status_var.set(f"Usuario '{usuario.usuario}' registrado correctamente.")
            self.user_status_label.config(fg="#15803d")
        except ValueError as exc:
            self.user_status_var.set(str(exc))
            self.user_status_label.config(fg="#b91c1c")

    def buscar_usuario(self) -> None:
        usuario_id = self.user_vars["usuario"].get().strip()
        if not usuario_id:
            self.user_status_var.set("Debes ingresar el usuario para buscarlo.")
            self.user_status_label.config(fg="#b91c1c")
            return

        usuario = self.restaurante_servicio.buscar_usuario(usuario_id)
        if usuario is None:
            self.user_status_var.set("No existe un usuario con ese nombre de usuario.")
            self.user_status_label.config(fg="#b91c1c")
            return

        self.user_vars["usuario"].set(usuario.usuario)
        self.user_vars["nombre"].set(usuario.nombre)
        self.user_vars["correo"].set(usuario.correo)
        self.user_vars["clave"].set(usuario.contrasena)
        self.user_status_var.set(f"Usuario '{usuario.usuario}' cargado correctamente.")
        self.user_status_label.config(fg="#1d4ed8")

    def actualizar_usuario(self) -> None:
        try:
            usuario = self.restaurante_servicio.actualizar_usuario(
                usuario=self.user_vars["usuario"].get(),
                nombre=self.user_vars["nombre"].get(),
                correo=self.user_vars["correo"].get(),
                clave=self.user_vars["clave"].get(),
            )
            self._refrescar_usuarios()
            self.user_status_var.set(f"Usuario '{usuario.usuario}' actualizado correctamente.")
            self.user_status_label.config(fg="#15803d")
        except ValueError as exc:
            self.user_status_var.set(str(exc))
            self.user_status_label.config(fg="#b91c1c")

    def eliminar_usuario(self) -> None:
        usuario_id = self.user_vars["usuario"].get().strip()
        if not usuario_id:
            self.user_status_var.set("Debes escribir el usuario a eliminar.")
            self.user_status_label.config(fg="#b91c1c")
            return

        try:
            self.restaurante_servicio.eliminar_usuario(usuario_id)
            self.limpiar_formulario_usuario()
            self._refrescar_usuarios()
            self.user_status_var.set("Usuario eliminado correctamente.")
            self.user_status_label.config(fg="#15803d")
        except ValueError as exc:
            self.user_status_var.set(str(exc))
            self.user_status_label.config(fg="#b91c1c")

    def _refrescar_usuarios(self) -> None:
        for fila in self.user_table.get_children():
            self.user_table.delete(fila)
        for usuario in self.restaurante_servicio.listar_usuarios():
            self.user_table.insert("", tk.END, values=(usuario.usuario, usuario.nombre, usuario.correo))

    def mostrar_usuarios(self) -> None:
        self.user_section.grid()
        self.product_section.grid_remove()
        self._refrescar_usuarios()
        self.user_status_var.set("Consulta de usuarios actualizada.")
        self.user_status_label.config(fg="#1f2937")

    def _logout(self) -> None:
        if self.on_logout is not None:
            self.on_logout()
