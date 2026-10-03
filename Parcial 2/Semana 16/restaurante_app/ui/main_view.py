from __future__ import annotations

import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk
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
        self.usuario_actual = None
        self._usuario_seleccionado: int | None = None

        self.frame = tk.Frame(self.root, bg="#e5e7eb", padx=20, pady=20)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=0)
        self.frame.grid_rowconfigure(2, weight=1)

        header = tk.Frame(self.frame, bg="#1f2937", padx=20, pady=16)
        header.grid(row=0, column=0, sticky="ew")
        header.grid_columnconfigure(0, weight=1)

        assets_dir = Path(__file__).resolve().parent.parent / "assets"
        self.logo_image = self._cargar_icono_ppm(assets_dir / "logo.ppm", escala=8)
        logo = tk.Label(header, image=self.logo_image, bg="#1f2937")
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

        self.ventas_image = self._cargar_icono_ppm(assets_dir / "ventas.ppm", escala=5)
        self.btn_ventas = tk.Button(
            actions,
            text="Ventas",
            image=self.ventas_image,
            compound="left",
            command=self.mostrar_ventas,
            width=110,
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
        self.notebook.bind("<<NotebookTabChanged>>", self._al_cambiar_pestana)

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
        usuarios_container.grid_rowconfigure(10, weight=1)

        self.user_panel = tk.Frame(usuarios_container, bg="white", padx=12, pady=12)
        self.user_panel.grid(row=0, column=0, sticky="ew")
        for column in (0, 1):
            self.user_panel.grid_columnconfigure(column, weight=1)

        tk.Label(self.user_panel, text="Gestión de usuarios", bg="white", font=("Arial", 12, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 4)
        )
        self.u_id_var = tk.StringVar(value="Sin selección")
        id_frame = tk.Frame(self.user_panel, bg="white")
        id_frame.grid(row=0, column=1, sticky="e")
        tk.Label(id_frame, text="ID:", bg="white").pack(side="left", padx=(0, 4))
        tk.Label(id_frame, textvariable=self.u_id_var, bg="white", fg="#6b7280").pack(side="left")

        tk.Label(self.user_panel, text="Usuario", bg="white").grid(row=1, column=0, columnspan=2, sticky="w")
        self.u_usuario_var = tk.StringVar()
        self.u_usuario_entry = tk.Entry(self.user_panel, textvariable=self.u_usuario_var, width=22)
        self.u_usuario_entry.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(2, 4))

        tk.Label(self.user_panel, text="Contraseña", bg="white").grid(row=3, column=0, columnspan=2, sticky="w")
        self.u_password_var = tk.StringVar()
        self.u_password_entry = tk.Entry(self.user_panel, textvariable=self.u_password_var, show="*", width=22)
        self.u_password_entry.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(2, 4))

        tk.Label(self.user_panel, text="Nombre", bg="white").grid(row=5, column=0, columnspan=2, sticky="w")
        self.u_nombre_var = tk.StringVar()
        self.u_nombre_entry = tk.Entry(self.user_panel, textvariable=self.u_nombre_var, width=22)
        self.u_nombre_entry.grid(row=6, column=0, columnspan=2, sticky="ew", pady=(2, 4))

        tk.Label(self.user_panel, text="Rol", bg="white").grid(row=7, column=0, columnspan=2, sticky="w")
        self.u_rol_var = tk.StringVar(value="Cliente")
        self.u_rol_cb = ttk.Combobox(
            self.user_panel,
            textvariable=self.u_rol_var,
            values=("Administrador", "Empleado", "Cliente"),
            state="readonly",
        )
        self.u_rol_cb.grid(row=8, column=0, columnspan=2, sticky="ew", pady=(2, 4))
        self.u_rol_cb.bind("<<ComboboxSelected>>", self._al_cambiar_rol)

        tk.Label(self.user_panel, text="Correo", bg="white").grid(row=9, column=0, columnspan=2, sticky="w")
        self.u_correo_var = tk.StringVar()
        self.u_correo_entry = tk.Entry(self.user_panel, textvariable=self.u_correo_var, width=22)
        self.u_correo_entry.grid(row=10, column=0, columnspan=2, sticky="ew", pady=(2, 4))

        self.user_message_var = tk.StringVar(value="")
        tk.Label(
            self.user_panel,
            textvariable=self.user_message_var,
            fg="#1f4f46",
            bg="white",
            wraplength=370,
            justify="left",
        ).grid(row=11, column=0, columnspan=2, sticky="w", pady=(2, 4))

        user_buttons = tk.Frame(self.user_panel, bg="white")
        user_buttons.grid(row=12, column=0, columnspan=2, sticky="w", pady=(4, 0))

        tk.Button(user_buttons, text="Registrar", command=self._registrar_usuario, bg="#10b981", fg="white", width=10).grid(row=0, column=0, padx=(0, 4))
        tk.Button(user_buttons, text="Consultar", command=self._consultar_usuario, width=10).grid(row=0, column=1, padx=(0, 4))
        self.btn_actualizar_usuario = tk.Button(user_buttons, text="Actualizar", command=self._actualizar_usuario, width=10)
        self.btn_actualizar_usuario.grid(row=0, column=2, padx=(0, 4))
        self.btn_eliminar_usuario = tk.Button(user_buttons, text="Eliminar", command=self._eliminar_usuario, bg="#ef4444", fg="white", width=10)
        self.btn_eliminar_usuario.grid(row=0, column=3, padx=(0, 4))
        tk.Button(user_buttons, text="Limpiar", command=self._limpiar_user_form, width=10).grid(row=0, column=4)

        # Tabla a todo el ancho debajo del formulario.
        self.user_list_frame = tk.Frame(usuarios_container, bg="white", padx=12, pady=12)
        self.user_list_frame.grid(row=1, column=0, sticky="nsew")
        self.user_list_frame.grid_rowconfigure(1, weight=1)
        self.user_list_frame.grid_columnconfigure(0, weight=1)

        tk.Label(self.user_list_frame, text="Usuarios registrados", bg="white", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w")
        ucols = ("id", "usuario", "nombre", "rol")
        self.user_tree = ttk.Treeview(self.user_list_frame, columns=ucols, show="headings", height=12)
        for col, title in (("id", "ID"), ("usuario", "Usuario"), ("nombre", "Nombre"), ("rol", "Rol")):
            self.user_tree.heading(
                col,
                text=title,
                command=lambda c=col: self._sort_tree(self.user_tree, c, c == "id"),
            )
            self.user_tree.column(col, width=95 if col == "id" else 140, anchor="w", stretch=True)
        self.user_tree.grid(row=1, column=0, sticky="nsew", pady=(6,0))
        user_scroll = ttk.Scrollbar(self.user_list_frame, orient="vertical", command=self.user_tree.yview)
        user_scroll.grid(row=1, column=1, sticky="ns", pady=(6,0))
        self.user_tree.configure(yscrollcommand=user_scroll.set)
        self.user_tree.bind("<<TreeviewSelect>>", self._al_seleccionar_usuario)
        self.user_tree.bind("<Escape>", self._atajo_limpiar_usuario)
        for entrada in (self.u_usuario_entry, self.u_nombre_entry, self.u_correo_entry, self.u_password_entry, self.u_rol_cb):
            entrada.bind("<Return>", self._atajo_registrar_usuario)
            entrada.bind("<Escape>", self._atajo_limpiar_usuario)

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

    @staticmethod
    def _cargar_icono_ppm(ruta: Path, escala: int) -> tk.PhotoImage:
        tokens = ruta.read_text(encoding="ascii").split()
        if len(tokens) < 4 or tokens[0] != "P3":
            raise ValueError(f"El recurso visual {ruta.name} no es un PPM P3 válido.")
        ancho, alto, maximo = map(int, tokens[1:4])
        componentes = list(map(int, tokens[4:]))
        if ancho <= 0 or alto <= 0 or maximo <= 0 or len(componentes) != ancho * alto * 3:
            raise ValueError(f"El recurso visual {ruta.name} tiene dimensiones o píxeles inválidos.")

        imagen = tk.PhotoImage(width=ancho, height=alto)
        for y in range(alto):
            colores = []
            for x in range(ancho):
                inicio = (y * ancho + x) * 3
                rgb = componentes[inicio:inicio + 3]
                colores.append("#" + "".join(f"{round(c * 255 / maximo):02x}" for c in rgb))
            imagen.put("{" + " ".join(colores) + "}", to=(0, y))
        return imagen.zoom(escala, escala)

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

    def establecer_usuario_actual(self, usuario) -> None:
        self.usuario_actual = usuario
        if self._es_administrador():
            self.btn_usuarios.grid()
            self.notebook.tab(self.usuarios_tab, state="normal")
        else:
            self.btn_usuarios.grid_remove()
            self.notebook.tab(self.usuarios_tab, state="hidden")
            self.notebook.select(self.productos_tab)
        self._limpiar_user_form()

    def _es_administrador(self) -> bool:
        return self.usuario_actual is not None and self.usuario_actual.rol == "Administrador"

    def mostrar_usuarios(self) -> None:
        if not self._es_administrador():
            self._mostrar_info("Acceso restringido", ["Solo un Administrador puede gestionar usuarios."])
            return

        self.notebook.select(self.usuarios_tab)
        self._actualizar_tabla_usuarios()

    def _actualizar_tabla_usuarios(self) -> None:
        usuarios = self.restaurante_servicio.listar_usuarios()
        for item in self.user_tree.get_children():
            self.user_tree.delete(item)
        for usuario in usuarios:
            self.user_tree.insert(
                "",
                tk.END,
                iid=str(usuario.id),
                values=(usuario.id, usuario.identificacion, usuario.nombre, usuario.rol),
            )

    def _al_cambiar_pestana(self, _evento) -> None:
        pestaña_actual = self.notebook.select()
        if pestaña_actual == str(self.usuarios_tab):
            if not self._es_administrador():
                self.notebook.select(self.productos_tab)
                return
            self.info_text.grid_remove()
            self._actualizar_tabla_usuarios()
        elif self.info_text.winfo_manager() != "grid":
            self.info_text.grid()

    def _al_seleccionar_usuario(self, _evento) -> None:
        seleccion = self.user_tree.selection()
        if not seleccion:
            return
        self.u_id_var.set(seleccion[0])
        self._consultar_usuario()

    def _consultar_usuario(self) -> None:
        seleccion = self.user_tree.selection()
        valor_id = seleccion[0] if seleccion else self.u_id_var.get().strip()
        if not valor_id or valor_id == "Sin selección":
            self.user_message_var.set("Selecciona un usuario de la tabla para consultarlo.")
            return
        try:
            identificador = int(valor_id)
        except ValueError:
            self.user_message_var.set("El ID del usuario seleccionado no es válido.")
            return
        usuario = self.restaurante_servicio.obtener_usuario_por_id(identificador)
        if usuario is None:
            self.user_message_var.set("El usuario seleccionado ya no está disponible.")
            return
        self._usuario_seleccionado = identificador
        self.u_id_var.set(str(usuario.id))
        self.u_usuario_var.set(usuario.identificacion)
        self.u_usuario_entry.configure(state="readonly")
        self.u_nombre_var.set(usuario.nombre)
        self.u_correo_var.set(usuario.correo)
        self.u_password_var.set("")
        self.u_rol_var.set(usuario.rol)
        es_admin = usuario.rol == "Administrador"
        self.u_rol_cb.configure(state="disabled" if es_admin else "readonly")
        self.btn_actualizar_usuario.configure(state="disabled" if es_admin else "normal")
        self.btn_eliminar_usuario.configure(state="disabled" if es_admin else "normal")
        self.user_message_var.set(
            f"Usuario {usuario.usuario} cargado."
            if es_admin
            else f"Usuario {usuario.usuario} cargado. La contraseña se conserva si queda vacía."
        )

    def _al_cambiar_rol(self, _evento) -> None:
        self.user_message_var.set(f"El nuevo usuario se guardará con el rol {self.u_rol_var.get()}.")

    def _atajo_registrar_usuario(self, _evento) -> str:
        self._registrar_usuario()
        return "break"

    def _atajo_limpiar_usuario(self, _evento) -> str:
        self._limpiar_user_form()
        return "break"

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
        if not self._es_administrador():
            self.user_message_var.set("Solo un Administrador puede registrar usuarios.")
            return
        usuario = self.u_usuario_var.get().strip()
        nombre = self.u_nombre_var.get().strip()
        correo = self.u_correo_var.get().strip()
        password = self.u_password_var.get().strip()
        rol = self.u_rol_var.get().strip()
        try:
            self.restaurante_servicio.registrar_usuario(usuario, nombre, correo, password, rol)
        except ValueError as exc:
            self.user_message_var.set(str(exc))
            return
        self._limpiar_user_form()
        self.mostrar_usuarios()
        self.user_message_var.set(f"Usuario {usuario} registrado correctamente.")

    def _actualizar_usuario(self) -> None:
        if not self._es_administrador():
            self.user_message_var.set("Solo un Administrador puede actualizar usuarios.")
            return
        if self._usuario_seleccionado is None:
            self.user_message_var.set("Selecciona un usuario en la tabla para actualizarlo.")
            return
        seleccionado = self.restaurante_servicio.obtener_usuario_por_id(self._usuario_seleccionado)
        if seleccionado is None:
            self.user_message_var.set("El usuario seleccionado ya no está disponible.")
            return
        usuario = seleccionado.usuario
        nombre = self.u_nombre_var.get().strip()
        correo = self.u_correo_var.get().strip()
        password = self.u_password_var.get().strip()
        rol = self.u_rol_var.get().strip()
        try:
            self.restaurante_servicio.actualizar_usuario(usuario, nombre, correo, password, rol)
        except ValueError as exc:
            self.user_message_var.set(str(exc))
            return
        self._limpiar_user_form()
        self.mostrar_usuarios()
        self.user_message_var.set(f"Usuario {usuario} actualizado correctamente.")

    def _eliminar_usuario(self) -> None:
        if not self._es_administrador():
            self.user_message_var.set("Solo un Administrador puede eliminar usuarios.")
            return
        if self._usuario_seleccionado is None:
            self.user_message_var.set("Selecciona un usuario en la tabla para eliminarlo.")
            return
        seleccionado = self.restaurante_servicio.obtener_usuario_por_id(self._usuario_seleccionado)
        if seleccionado is None:
            self.user_message_var.set("El usuario seleccionado ya no está disponible.")
            return
        usuario = seleccionado.usuario
        if not messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Deseas eliminar el usuario {usuario}?",
            parent=self.root,
        ):
            return
        try:
            ok = self.restaurante_servicio.eliminar_usuario(
                usuario,
                usuario_actual=self.usuario_actual.identificacion,
            )
        except ValueError as exc:
            self.user_message_var.set(str(exc))
            return
        if not ok:
            self.user_message_var.set(f"No existe el usuario {usuario}.")
            return
        self._limpiar_user_form()
        self.mostrar_usuarios()
        self.user_message_var.set(f"Usuario {usuario} eliminado correctamente.")

    def _limpiar_user_form(self) -> None:
        self._usuario_seleccionado = None
        self.u_id_var.set("Sin selección")
        if hasattr(self, "user_tree"):
            seleccion = self.user_tree.selection()
            if seleccion:
                self.user_tree.selection_remove(*seleccion)
            self.u_usuario_entry.configure(state="normal")
            self.u_usuario_var.set("")
        self.u_rol_cb.configure(state="readonly")
        self.btn_actualizar_usuario.configure(state="normal")
        self.btn_eliminar_usuario.configure(state="normal")
        self.u_nombre_var.set("")
        self.u_correo_var.set("")
        self.u_password_var.set("")
        self.u_rol_var.set("Cliente")
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
        self.establecer_usuario_actual(None)
        if self.on_logout is not None:
            self.on_logout()
