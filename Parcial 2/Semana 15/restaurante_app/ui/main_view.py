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
        self.frame.grid_rowconfigure(2, weight=1)

        header = tk.Frame(self.frame, bg="#1f2937", padx=20, pady=16)
        header.grid(row=0, column=0, sticky="ew")
        header.grid_columnconfigure(0, weight=1)

        logo = tk.Label(
            header,
            text="  RESTAURANTE  ",
            bg="#f59e0b",
            fg="#1f2937",
            font=("Arial", 11, "bold"),
            padx=8,
            pady=6,
        )
        logo.grid(row=0, column=0, sticky="w", padx=(0, 14))

        title = tk.Label(
            header,
            text="Panel principal · Restaurante App",
            fg="white",
            bg="#1f2937",
            font=("Arial", 16, "bold"),
        )
        title.grid(row=0, column=1, sticky="w")

        actions = tk.Frame(self.frame, bg="#e5e7eb")
        actions.grid(row=1, column=0, sticky="ew", pady=(16, 10))

        self.btn_productos = tk.Button(actions, text="Productos", command=self.mostrar_productos, width=18)
        self.btn_productos.grid(row=0, column=0, padx=(0, 10), sticky="w")

        self.btn_usuarios = tk.Button(actions, text="Usuarios", command=self.mostrar_usuarios, width=18)
        self.btn_usuarios.grid(row=0, column=1, padx=(0, 10), sticky="w")

        self.btn_ventas = tk.Button(
            actions,
            text="Ventas",
            command=self.mostrar_ventas,
            width=18,
        )
        self.btn_ventas.grid(row=0, column=2, sticky="w")

        logout_btn = tk.Button(actions, text="Cerrar sesión", command=self._logout, width=18, bg="#dc2626", fg="white")
        logout_btn.grid(row=0, column=3, padx=(10, 0), sticky="e")

        # Contenedor principal: usar pestañas para Productos/Usuarios
        self.notebook = ttk.Notebook(self.frame)
        self.notebook.grid(row=2, column=0, sticky="nsew")

        # pestañas
        self.productos_tab = tk.Frame(self.notebook, bg="white")
        self.usuarios_tab = tk.Frame(self.notebook, bg="white")
        self.ventas_tab = tk.Frame(self.notebook, bg="white")
        self.notebook.add(self.productos_tab, text="Productos")
        self.notebook.add(self.usuarios_tab, text="Usuarios")
        self.notebook.add(self.ventas_tab, text="Ventas")

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

        # Ventas: formulario y lista
        ventas_container = tk.Frame(self.ventas_tab, bg="white", bd=1, relief="solid")
        ventas_container.pack(fill="both", expand=True, padx=4, pady=6)
        ventas_container.grid_columnconfigure(0, weight=1)
        ventas_container.grid_columnconfigure(1, weight=1)
        ventas_container.grid_rowconfigure(0, weight=1)

        # Formulario de ventas (izquierda)
        venta_form = tk.Frame(ventas_container, bg="white", padx=12, pady=12)
        venta_form.grid(row=0, column=0, sticky="nsew")
        tk.Label(venta_form, text="Usuario (ID)", bg="white").grid(row=0, column=0, sticky="w")
        self.venta_usuario_cb = ttk.Combobox(venta_form, values=[], width=30)
        self.venta_usuario_cb.grid(row=1, column=0, sticky="w", pady=(2,8))
        self.venta_usuario_var = tk.StringVar()
        self.venta_usuario_cb.configure(textvariable=self.venta_usuario_var)
        self.venta_usuario_var.trace_add("write", self._actualizar_detalles_venta)

        self.venta_cliente_info_var = tk.StringVar(value="Selecciona un usuario para ver sus datos.")
        tk.Label(
            venta_form,
            textvariable=self.venta_cliente_info_var,
            bg="#eff6ff",
            fg="#1e3a8a",
            justify="left",
            anchor="w",
            width=42,
            padx=6,
            pady=5,
        ).grid(row=2, column=0, sticky="ew", pady=(0, 8))

        tk.Label(venta_form, text="Producto (Código)", bg="white").grid(row=3, column=0, sticky="w")
        self.venta_producto_cb = ttk.Combobox(venta_form, values=[], width=30)
        self.venta_producto_cb.grid(row=4, column=0, sticky="w", pady=(2,8))
        self.venta_producto_var = tk.StringVar()
        self.venta_producto_cb.configure(textvariable=self.venta_producto_var)
        self.venta_producto_var.trace_add("write", self._actualizar_detalles_venta)

        self.venta_producto_info_var = tk.StringVar(value="Selecciona un producto para ver sus datos.")
        tk.Label(
            venta_form,
            textvariable=self.venta_producto_info_var,
            bg="#f0fdf4",
            fg="#166534",
            justify="left",
            anchor="w",
            width=42,
            padx=6,
            pady=5,
        ).grid(row=5, column=0, sticky="ew", pady=(0, 8))

        tk.Label(venta_form, text="Cantidad", bg="white").grid(row=6, column=0, sticky="w")
        self.venta_cantidad_var = tk.StringVar()
        tk.Entry(venta_form, textvariable=self.venta_cantidad_var, width=10).grid(row=7, column=0, sticky="w", pady=(2,8))
        self.venta_cantidad_var.trace_add("write", self._actualizar_total_venta)
        self.venta_total_var = tk.StringVar(value="Total: $0.00")
        tk.Label(
            venta_form,
            textvariable=self.venta_total_var,
            bg="white",
            fg="#111827",
            font=("Arial", 11, "bold"),
        ).grid(row=8, column=0, sticky="w", pady=(0, 8))
        venta_btns = tk.Frame(venta_form, bg="white")
        venta_btns.grid(row=9, column=0, sticky="w", pady=(8,0))
        tk.Button(venta_btns, text="Registrar Venta", command=self._registrar_venta, bg="#10b981", fg="white", width=14).grid(row=0, column=0, padx=(0,6))
        tk.Button(venta_btns, text="Limpiar", command=self._limpiar_venta_form, width=12).grid(row=0, column=1)

        # Lista de ventas (derecha)
        ventas_list_frame = tk.Frame(ventas_container, bg="white", padx=12, pady=12)
        ventas_list_frame.grid(row=0, column=1, sticky="nsew")
        ventas_list_frame.grid_rowconfigure(0, weight=1)
        ventas_list_frame.grid_columnconfigure(0, weight=1)
        tk.Label(ventas_list_frame, text="Ventas", bg="white", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w")
        vcols = ("fecha", "usuario_id", "producto_codigo", "cantidad", "precio_unitario", "total")
        self.ventas_tree = ttk.Treeview(ventas_list_frame, columns=vcols, show="headings", height=12)
        for col, title in (
            ("fecha", "Fecha"), ("usuario_id","Usuario"), ("producto_codigo","Producto"),
            ("cantidad","Cantidad"), ("precio_unitario", "Precio unitario"), ("total", "Total"),
        ):
            is_num = col in ("cantidad", "precio_unitario", "total")
            self.ventas_tree.heading(col, text=title, command=lambda c=col, n=is_num: self._sort_tree(self.ventas_tree, c, n))
            self.ventas_tree.column(col, width=120, anchor="w", stretch=True)
        self.ventas_tree.grid(row=1, column=0, sticky="nsew", pady=(6,0))
        vscroll = ttk.Scrollbar(ventas_list_frame, orient="vertical", command=self.ventas_tree.yview)
        vscroll.grid(row=1, column=1, sticky="ns", pady=(6,0))
        self.ventas_tree.configure(yscrollcommand=vscroll.set)

        # Texto de información debajo
        self.info_text = tk.Text(self.frame, height=6, wrap="word")
        self.info_text.grid(row=3, column=0, sticky="ew", padx=20, pady=(12, 0))
        self.info_text.config(state="disabled")

        # Inicializar vistas de ventas
        try:
            self._refresh_ventas_inputs()
            self._refresh_ventas_tree()
        except Exception:
            pass

        # Inicializar listas y bindings
        self.product_codes: list[str] = []
        self.user_ids: list[str] = []
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

    def mostrar_ventas(self) -> None:
        # seleccionar pestaña Ventas y refrescar
        try:
            self.notebook.select(self.ventas_tab)
        except Exception:
            pass
        self._refresh_ventas_inputs()
        self._refresh_ventas_tree()

    def _refresh_ventas_inputs(self) -> None:
        # actualizar valores para comboboxes de ventas (usuarios y productos)
        productos = self.restaurante_servicio.listar_productos()
        self.product_codes = [p.codigo for p in productos]
        try:
            self.venta_producto_cb['values'] = self.product_codes
        except Exception:
            pass
        usuarios = self.restaurante_servicio.listar_usuarios()
        self.user_ids = [u.usuario for u in usuarios]
        try:
            self.venta_usuario_cb['values'] = self.user_ids
        except Exception:
            pass

    def _refresh_ventas_tree(self) -> None:
        ventas = self.restaurante_servicio.listar_ventas()
        # limpiar
        try:
            children = list(self.ventas_tree.get_children())
        except Exception:
            children = []
        for item in children:
            try:
                self.ventas_tree.delete(item)
            except Exception:
                pass
        for idx, v in enumerate(ventas):
            iid = f"venta_{idx}"
            try:
                self.ventas_tree.insert(
                    "", tk.END, iid=iid,
                    values=(
                        v.fecha,
                        v.usuario_id,
                        v.producto_codigo,
                        str(v.cantidad),
                        f"${v.precio_unitario:.2f}",
                        f"${v.total:.2f}",
                    ),
                )
            except Exception:
                pass
        lines = [v.mostrar_informacion() for v in ventas]
        self._mostrar_info("Ventas registradas", lines)

    def _registrar_venta(self) -> None:
        usuario = self.venta_usuario_var.get().strip()
        producto = self.venta_producto_var.get().strip()
        cantidad = self.venta_cantidad_var.get().strip()
        if not usuario or not producto or not cantidad:
            self._mostrar_info("Error", ["Usuario, producto y cantidad son requeridos."])
            return
        try:
            cantidad_val = int(cantidad)
            self.restaurante_servicio.registrar_venta(usuario, producto, cantidad_val)
        except (TypeError, ValueError) as exc:
            self._mostrar_info("Error al registrar venta", [str(exc)])
            return
        # éxito
        self._limpiar_venta_form()
        self._refresh_ventas_tree()
        # actualizar vista de productos porque el stock cambió
        self.mostrar_productos()
        self._mostrar_info("Venta registrada", ["La venta se registró correctamente."])

    def _limpiar_venta_form(self) -> None:
        self.venta_usuario_var.set("")
        self.venta_producto_var.set("")
        self.venta_cantidad_var.set("")
        self.venta_cliente_info_var.set("Selecciona un usuario para ver sus datos.")
        self.venta_producto_info_var.set("Selecciona un producto para ver sus datos.")
        self.venta_total_var.set("Total: $0.00")

    def _actualizar_detalles_venta(self, *_args) -> None:
        usuario = self.restaurante_servicio.obtener_usuario(self.venta_usuario_var.get())
        if usuario is None:
            self.venta_cliente_info_var.set("Selecciona un usuario para ver sus datos.")
        else:
            self.venta_cliente_info_var.set(
                f"Cliente: {usuario.nombre}\nUsuario: {usuario.usuario} | Correo: {usuario.correo}"
            )

        producto = self.restaurante_servicio.obtener_producto(self.venta_producto_var.get())
        if producto is None:
            self.venta_producto_info_var.set("Selecciona un producto para ver sus datos.")
        else:
            self.venta_producto_info_var.set(
                f"Producto: {producto.nombre} ({producto.codigo})\n"
                f"Categoría: {producto.categoria} | Precio: ${producto.precio:.2f} | Stock: {producto.stock}"
            )
        self._actualizar_total_venta()

    def _actualizar_total_venta(self, *_args) -> None:
        producto = self.restaurante_servicio.obtener_producto(self.venta_producto_var.get())
        try:
            cantidad = int(self.venta_cantidad_var.get())
        except (TypeError, ValueError):
            cantidad = 0
        total = producto.precio * cantidad if producto is not None and cantidad > 0 else 0
        self.venta_total_var.set(f"Total: ${total:.2f}")

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
