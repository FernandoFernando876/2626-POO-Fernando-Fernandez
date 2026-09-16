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

        self.frame = tk.Frame(self.root, bg="#e5e7eb", padx=20, pady=20)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)

        header = tk.Frame(self.frame, bg="#1f2937", padx=20, pady=16)
        header.grid(row=0, column=0, sticky="ew")
        header.grid_columnconfigure(0, weight=1)

        title = tk.Label(
            header,
            text="Panel principal",
            fg="white",
            bg="#1f2937",
            font=("Arial", 16, "bold"),
        )
        title.grid(row=0, column=0, sticky="w")

        actions = tk.Frame(self.frame, bg="#e5e7eb")
        actions.grid(row=1, column=0, sticky="ew", pady=(16, 10))

        self.btn_productos = tk.Button(actions, text="Productos", command=self.mostrar_productos, width=18)
        self.btn_productos.grid(row=0, column=0, padx=(0, 10), sticky="w")

        self.btn_usuarios = tk.Button(actions, text="Usuarios", command=self.mostrar_usuarios, width=18)
        self.btn_usuarios.grid(row=0, column=1, padx=(0, 10), sticky="w")

        self.btn_ventas = tk.Button(actions, text="Ventas (pendiente)", command=self.mostrar_pendiente, width=18)
        self.btn_ventas.grid(row=0, column=2, sticky="w")

        logout_btn = tk.Button(actions, text="Cerrar sesión", command=self._logout, width=18, bg="#dc2626", fg="white")
        logout_btn.grid(row=0, column=3, padx=(10, 0), sticky="e")

        # Contenedor principal: usar pestañas para Productos/Usuarios
        self.notebook = ttk.Notebook(self.frame)
        self.notebook.grid(row=2, column=0, sticky="nsew")

        # pestañas
        self.productos_tab = tk.Frame(self.notebook, bg="white")
        self.usuarios_tab = tk.Frame(self.notebook, bg="white")
        self.notebook.add(self.productos_tab, text="Productos")
        self.notebook.add(self.usuarios_tab, text="Usuarios")

        # --- Panel de productos dentro de la pestaña ---
        # contenedor interior
        productos_container = tk.Frame(self.productos_tab, bg="white", bd=1, relief="solid")
        productos_container.pack(fill="both", expand=True, padx=4, pady=6)
        productos_container.grid_columnconfigure(0, weight=1)
        productos_container.grid_columnconfigure(1, weight=1)
        productos_container.grid_rowconfigure(0, weight=1)

        # formulario productos (lado izquierdo)
        self.form_frame = tk.Frame(productos_container, bg="white", padx=12, pady=12)
        self.form_frame.grid(row=0, column=0, sticky="nsew")

        tk.Label(self.form_frame, text="Código", bg="white").grid(row=0, column=0, sticky="w")
        self.codigo_var = tk.StringVar()
        tk.Entry(self.form_frame, textvariable=self.codigo_var, width=25).grid(row=1, column=0, sticky="w", pady=(2, 8))

        tk.Label(self.form_frame, text="Nombre", bg="white").grid(row=2, column=0, sticky="w")
        self.nombre_var = tk.StringVar()
        tk.Entry(self.form_frame, textvariable=self.nombre_var, width=40).grid(row=3, column=0, sticky="w", pady=(2, 8))

        tk.Label(self.form_frame, text="Categoría", bg="white").grid(row=4, column=0, sticky="w")
        self.categoria_var = tk.StringVar()
        tk.Entry(self.form_frame, textvariable=self.categoria_var, width=30).grid(row=5, column=0, sticky="w", pady=(2, 8))

        tk.Label(self.form_frame, text="Precio", bg="white").grid(row=6, column=0, sticky="w")
        self.precio_var = tk.StringVar()
        tk.Entry(self.form_frame, textvariable=self.precio_var, width=20).grid(row=7, column=0, sticky="w", pady=(2, 8))

        tk.Label(self.form_frame, text="Stock", bg="white").grid(row=8, column=0, sticky="w")
        self.stock_var = tk.StringVar()
        tk.Entry(self.form_frame, textvariable=self.stock_var, width=10).grid(row=9, column=0, sticky="w", pady=(2, 8))

        self.form_message_var = tk.StringVar(value="")
        tk.Label(self.form_frame, textvariable=self.form_message_var, fg="#b91c1c", bg="white").grid(row=10, column=0, sticky="w", pady=(4, 8))

        buttons_frame = tk.Frame(self.form_frame, bg="white")
        buttons_frame.grid(row=11, column=0, sticky="w", pady=(8, 0))

        tk.Button(buttons_frame, text="Registrar", command=self._registrar_producto, bg="#10b981", fg="white", width=12).grid(row=0, column=0, padx=(0, 6))
        tk.Button(buttons_frame, text="Cargar", command=self._cargar_producto, width=12).grid(row=0, column=1, padx=(0, 6))
        tk.Button(buttons_frame, text="Actualizar", command=self._actualizar_producto, width=12).grid(row=0, column=2, padx=(0, 6))
        tk.Button(buttons_frame, text="Eliminar", command=self._eliminar_producto, bg="#ef4444", fg="white", width=12).grid(row=0, column=3)
        tk.Button(self.form_frame, text="Limpiar", command=self._limpiar_form, width=12).grid(row=12, column=0, pady=(8, 0), sticky="w")

        # lista productos (lado derecho)
        self.list_frame = tk.Frame(productos_container, bg="white", padx=12, pady=12)
        self.list_frame.grid(row=0, column=1, sticky="nsew")
        self.list_frame.grid_rowconfigure(0, weight=1)
        self.list_frame.grid_columnconfigure(0, weight=1)

        tk.Label(self.list_frame, text="Productos", bg="white", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w")
        columns = ("codigo","nombre","categoria","precio","stock")
        self.tree = ttk.Treeview(self.list_frame, columns=columns, show="headings", height=12)
        for col, title in (("codigo","Código"),("nombre","Nombre"),("categoria","Categoría"),("precio","Precio"),("stock","Stock")):
            is_numeric = col in ("precio","stock")
            self.tree.heading(col, text=title, command=lambda c=col, n=is_numeric: self._sort_tree(self.tree, c, n))
            self.tree.column(col, width=100, anchor="w", stretch=True)
        self.tree.grid(row=1, column=0, sticky="nsew", pady=(6,0))
        scrollbar = ttk.Scrollbar(self.list_frame, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=1, column=1, sticky="ns", pady=(6,0))
        self.tree.configure(yscrollcommand=scrollbar.set)
        self._sort_dirs = {}

        # --- Panel de usuarios en su propia pestaña ---
        usuarios_container = tk.Frame(self.usuarios_tab, bg="white", bd=1, relief="solid")
        usuarios_container.pack(fill="both", expand=True, padx=4, pady=6)
        usuarios_container.grid_columnconfigure(0, weight=1)
        usuarios_container.grid_columnconfigure(1, weight=1)
        usuarios_container.grid_rowconfigure(0, weight=1)

        self.user_panel = tk.Frame(usuarios_container, bg="white", padx=12, pady=12)
        self.user_panel.grid(row=0, column=0, sticky="nsew")

        tk.Label(self.user_panel, text="Usuario", bg="white").grid(row=0, column=0, sticky="w")
        self.u_usuario_var = tk.StringVar()
        tk.Entry(self.user_panel, textvariable=self.u_usuario_var, width=25).grid(row=1, column=0, sticky="w", pady=(2, 8))

        tk.Label(self.user_panel, text="Nombre", bg="white").grid(row=2, column=0, sticky="w")
        self.u_nombre_var = tk.StringVar()
        tk.Entry(self.user_panel, textvariable=self.u_nombre_var, width=40).grid(row=3, column=0, sticky="w", pady=(2, 8))

        tk.Label(self.user_panel, text="Correo", bg="white").grid(row=4, column=0, sticky="w")
        self.u_correo_var = tk.StringVar()
        tk.Entry(self.user_panel, textvariable=self.u_correo_var, width=40).grid(row=5, column=0, sticky="w", pady=(2, 8))

        tk.Label(self.user_panel, text="Contraseña", bg="white").grid(row=6, column=0, sticky="w")
        self.u_password_var = tk.StringVar()
        tk.Entry(self.user_panel, textvariable=self.u_password_var, show="*", width=30).grid(row=7, column=0, sticky="w", pady=(2, 8))

        self.user_message_var = tk.StringVar(value="")
        tk.Label(self.user_panel, textvariable=self.user_message_var, fg="#b91c1c", bg="white").grid(row=8, column=0, sticky="w", pady=(4, 8))

        user_buttons = tk.Frame(self.user_panel, bg="white")
        user_buttons.grid(row=9, column=0, sticky="w", pady=(8, 0))

        tk.Button(user_buttons, text="Registrar", command=self._registrar_usuario, bg="#10b981", fg="white", width=12).grid(row=0, column=0, padx=(0, 6))
        tk.Button(user_buttons, text="Cargar", command=self._cargar_usuario, width=12).grid(row=0, column=1, padx=(0, 6))
        tk.Button(user_buttons, text="Actualizar", command=self._actualizar_usuario, width=12).grid(row=0, column=2, padx=(0, 6))
        tk.Button(user_buttons, text="Eliminar", command=self._eliminar_usuario, bg="#ef4444", fg="white", width=12).grid(row=0, column=3)
        tk.Button(self.user_panel, text="Limpiar", command=self._limpiar_user_form, width=12).grid(row=10, column=0, pady=(8, 0), sticky="w")

        # lista usuarios (lado derecho)
        self.user_list_frame = tk.Frame(usuarios_container, bg="white", padx=12, pady=12)
        self.user_list_frame.grid(row=0, column=1, rowspan=11, sticky="nsew")
        self.user_list_frame.grid_rowconfigure(0, weight=1)
        self.user_list_frame.grid_columnconfigure(0, weight=1)

        tk.Label(self.user_list_frame, text="Usuarios", bg="white", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w")
        ucols = ("usuario","nombre","correo")
        self.user_tree = ttk.Treeview(self.user_list_frame, columns=ucols, show="headings", height=12)
        for col, title in (("usuario","Usuario"),("nombre","Nombre"),("correo","Correo")):
            self.user_tree.heading(col, text=title, command=lambda c=col: self._sort_tree(self.user_tree, c, False))
            self.user_tree.column(col, width=140, anchor="w", stretch=True)
        self.user_tree.grid(row=1, column=0, sticky="nsew", pady=(6,0))
        user_scroll = ttk.Scrollbar(self.user_list_frame, orient="vertical", command=self.user_tree.yview)
        user_scroll.grid(row=1, column=1, sticky="ns", pady=(6,0))
        self.user_tree.configure(yscrollcommand=user_scroll.set)


        # Texto de información debajo
        self.info_text = tk.Text(self.frame, height=6, wrap="word")
        self.info_text.grid(row=3, column=0, sticky="ew", padx=20, pady=(12, 0))
        self.info_text.config(state="disabled")

        # Inicializar listas y bindings
        self.product_codes: list[str] = []
        self.user_ids: list[str] = []
        self.tree.bind('<<TreeviewSelect>>', self._on_product_select)
        self.user_tree.bind('<<TreeviewSelect>>', self._on_user_select)

        # Mostrar inicialmente productos
        self.mostrar_productos()

    def _mostrar_info(self, titulo: str, elementos: list[str]) -> None:
        self.info_text.config(state="normal")
        self.info_text.delete("1.0", tk.END)
        self.info_text.insert(tk.END, f"{titulo}\n\n")
        if not elementos:
            self.info_text.insert(tk.END, "No hay registros disponibles.")
        else:
            for elemento in elementos:
                self.info_text.insert(tk.END, f"- {elemento}\n")
        self.info_text.config(state="disabled")

    def mostrar_productos(self) -> None:
        # Seleccionar pestaña Productos
        try:
            self.notebook.select(self.productos_tab)
        except Exception:
            pass

        productos = self.restaurante_servicio.listar_productos()
        lines = [p.mostrar_informacion() for p in productos]
        # Actualizar treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        for p in productos:
            self.tree.insert("", tk.END, iid=p.codigo, values=(p.codigo, p.nombre, p.categoria, f"{p.precio:.2f}", str(p.stock)))
        self._mostrar_info("Productos registrados", lines)

    def mostrar_usuarios(self) -> None:
        # Seleccionar pestaña Usuarios
        try:
            self.notebook.select(self.usuarios_tab)
        except Exception:
            pass

        usuarios = self.restaurante_servicio.listar_usuarios()
        lines = [f"{usuario.usuario} - {usuario.nombre} - {usuario.correo}" for usuario in usuarios]
        # Actualizar user_tree
        for item in self.user_tree.get_children():
            self.user_tree.delete(item)
        for u in usuarios:
            self.user_tree.insert("", tk.END, iid=u.usuario, values=(u.usuario, u.nombre, u.correo))
        self._mostrar_info("Usuarios registrados", lines)

    def mostrar_pendiente(self) -> None:
        self._mostrar_info("Ventas", ["Funcionalidad pendiente para la siguiente etapa."])

    # Selección desde las listas
    # Selección desde las treeviews
    def _on_product_select(self, event) -> None:
        sel = self.tree.selection()
        if not sel:
            return
        codigo = sel[0]
        producto = self.restaurante_servicio.obtener_producto(codigo)
        if producto:
            self.codigo_var.set(producto.codigo)
            self.nombre_var.set(producto.nombre)
            self.categoria_var.set(producto.categoria)
            self.precio_var.set(str(producto.precio))
            self.stock_var.set(str(producto.stock))
            self.form_message_var.set("")

    def _on_user_select(self, event) -> None:
        sel = self.user_tree.selection()
        if not sel:
            return
        usuario_id = sel[0]
        u = self.restaurante_servicio.obtener_usuario(usuario_id)
        if u:
            self.u_usuario_var.set(u.usuario)
            self.u_nombre_var.set(u.nombre)
            self.u_correo_var.set(u.correo)
            self.u_password_var.set(u.password)
            self.user_message_var.set("")

    def _sort_tree(self, tree: ttk.Treeview, col: str, numeric: bool = False) -> None:
        """Ordena los elementos del treeview por la columna indicada.
        Alterna entre ascendente y descendente en cada click.
        """
        # clave para diccionario de direcciones
        key = (id(tree), col)
        reverse = self._sort_dirs.get(key, False)
        items = list(tree.get_children(''))
        def _get_val(item):
            v = tree.set(item, col)
            if numeric:
                try:
                    return float(v)
                except Exception:
                    return float('-inf')
            return v.lower()
        try:
            items.sort(key=lambda it: _get_val(it), reverse=reverse)
        except Exception:
            items.sort(key=lambda it: tree.set(it, col), reverse=reverse)
        # reinsertar en nuevo orden
        for index, item in enumerate(items):
            tree.move(item, '', index)
        # alternar para la próxima vez
        self._sort_dirs[key] = not reverse

    # Operaciones para usuarios
    def _registrar_usuario(self) -> None:
        usuario = self.u_usuario_var.get().strip()
        nombre = self.u_nombre_var.get().strip()
        correo = self.u_correo_var.get().strip()
        password = self.u_password_var.get().strip()
        try:
            self.restaurante_servicio.registrar_usuario(usuario, nombre, correo, password)
        except Exception as exc:
            self.user_message_var.set(str(exc))
            return
        self.user_message_var.set("")
        self._limpiar_user_form()
        self.mostrar_usuarios()

    def _cargar_usuario(self) -> None:
        usuario = self.u_usuario_var.get().strip()
        if not usuario:
            self.user_message_var.set("Ingresa el identificador de usuario a cargar.")
            return
        u = self.restaurante_servicio.obtener_usuario(usuario)
        if u is None:
            self.user_message_var.set(f"No existe usuario con id {usuario}.")
            return
        self.u_nombre_var.set(u.nombre)
        self.u_correo_var.set(u.correo)
        self.u_password_var.set(u.password)
        self.user_message_var.set("")

    def _actualizar_usuario(self) -> None:
        usuario = self.u_usuario_var.get().strip()
        nombre = self.u_nombre_var.get().strip()
        correo = self.u_correo_var.get().strip()
        password = self.u_password_var.get().strip()
        try:
            self.restaurante_servicio.actualizar_usuario(usuario, nombre, correo, password)
        except Exception as exc:
            self.user_message_var.set(str(exc))
            return
        self.user_message_var.set("")
        self._limpiar_user_form()
        self.mostrar_usuarios()

    def _eliminar_usuario(self) -> None:
        usuario = self.u_usuario_var.get().strip()
        if not usuario:
            self.user_message_var.set("Ingresa el identificador del usuario a eliminar.")
            return
        ok = self.restaurante_servicio.eliminar_usuario(usuario)
        if not ok:
            self.user_message_var.set(f"No existe usuario con id {usuario}.")
            return
        self.user_message_var.set("")
        self._limpiar_user_form()
        self.mostrar_usuarios()

    def _limpiar_user_form(self) -> None:
        self.u_usuario_var.set("")
        self.u_nombre_var.set("")
        self.u_correo_var.set("")
        self.u_password_var.set("")
        self.user_message_var.set("")

    def _registrar_producto(self) -> None:
        codigo = self.codigo_var.get().strip()
        nombre = self.nombre_var.get().strip()
        categoria = self.categoria_var.get().strip()
        precio = self.precio_var.get().strip()
        stock = self.stock_var.get().strip()
        try:
            precio_val = float(precio)
            stock_val = int(stock)
            self.restaurante_servicio.registrar_producto(codigo, nombre, categoria, precio_val, stock_val)
        except Exception as exc:
            self.form_message_var.set(str(exc))
            return
        self.form_message_var.set("")
        self._limpiar_form()
        self.mostrar_productos()

    def _cargar_producto(self) -> None:
        codigo = self.codigo_var.get().strip()
        if not codigo:
            self.form_message_var.set("Ingresa el código del producto a cargar.")
            return
        producto = self.restaurante_servicio.obtener_producto(codigo)
        if producto is None:
            self.form_message_var.set(f"No existe producto con código {codigo}.")
            return
        # Rellenar formulario
        self.nombre_var.set(producto.nombre)
        self.categoria_var.set(producto.categoria)
        self.precio_var.set(str(producto.precio))
        self.stock_var.set(str(producto.stock))
        self.form_message_var.set("")

    def _actualizar_producto(self) -> None:
        codigo = self.codigo_var.get().strip()
        nombre = self.nombre_var.get().strip()
        categoria = self.categoria_var.get().strip()
        precio = self.precio_var.get().strip()
        stock = self.stock_var.get().strip()
        try:
            precio_val = float(precio)
            stock_val = int(stock)
            self.restaurante_servicio.actualizar_producto(codigo, nombre, categoria, precio_val, stock_val)
        except Exception as exc:
            self.form_message_var.set(str(exc))
            return
        self.form_message_var.set("")
        self._limpiar_form()
        self.mostrar_productos()

    def _eliminar_producto(self) -> None:
        codigo = self.codigo_var.get().strip()
        if not codigo:
            self.form_message_var.set("Ingresa el código del producto a eliminar.")
            return
        ok = self.restaurante_servicio.eliminar_producto(codigo)
        if not ok:
            self.form_message_var.set(f"No existe producto con código {codigo}.")
            return
        self.form_message_var.set("")
        self._limpiar_form()
        self.mostrar_productos()

    def _limpiar_form(self) -> None:
        self.codigo_var.set("")
        self.nombre_var.set("")
        self.categoria_var.set("")
        self.precio_var.set("")
        self.stock_var.set("")
        self.form_message_var.set("")

    def _logout(self) -> None:
        if self.on_logout is not None:
            self.on_logout()
