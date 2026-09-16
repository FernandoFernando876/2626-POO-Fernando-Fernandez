from __future__ import annotations

import tkinter as tk
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

        # Contenedor principal para interfaz de productos y visualización
        display_frame = tk.Frame(self.frame, bg="white", bd=1, relief="solid")
        display_frame.grid(row=2, column=0, sticky="nsew")
        display_frame.grid_columnconfigure(0, weight=1)
        display_frame.grid_columnconfigure(1, weight=1)
        display_frame.grid_rowconfigure(0, weight=1)

        # Formulario de productos (lado izquierdo)
        form_frame = tk.Frame(display_frame, bg="white", padx=12, pady=12)
        form_frame.grid(row=0, column=0, sticky="nsew")

        tk.Label(form_frame, text="Código", bg="white").grid(row=0, column=0, sticky="w")
        self.codigo_var = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.codigo_var, width=25).grid(row=1, column=0, sticky="w", pady=(2, 8))

        tk.Label(form_frame, text="Nombre", bg="white").grid(row=2, column=0, sticky="w")
        self.nombre_var = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.nombre_var, width=40).grid(row=3, column=0, sticky="w", pady=(2, 8))

        tk.Label(form_frame, text="Categoría", bg="white").grid(row=4, column=0, sticky="w")
        self.categoria_var = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.categoria_var, width=30).grid(row=5, column=0, sticky="w", pady=(2, 8))

        tk.Label(form_frame, text="Precio", bg="white").grid(row=6, column=0, sticky="w")
        self.precio_var = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.precio_var, width=20).grid(row=7, column=0, sticky="w", pady=(2, 8))

        tk.Label(form_frame, text="Stock", bg="white").grid(row=8, column=0, sticky="w")
        self.stock_var = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.stock_var, width=10).grid(row=9, column=0, sticky="w", pady=(2, 8))

        self.form_message_var = tk.StringVar(value="")
        tk.Label(form_frame, textvariable=self.form_message_var, fg="#b91c1c", bg="white").grid(row=10, column=0, sticky="w", pady=(4, 8))

        buttons_frame = tk.Frame(form_frame, bg="white")
        buttons_frame.grid(row=11, column=0, sticky="w", pady=(8, 0))

        tk.Button(buttons_frame, text="Registrar", command=self._registrar_producto, bg="#10b981", fg="white", width=12).grid(row=0, column=0, padx=(0, 6))
        tk.Button(buttons_frame, text="Cargar", command=self._cargar_producto, width=12).grid(row=0, column=1, padx=(0, 6))
        tk.Button(buttons_frame, text="Actualizar", command=self._actualizar_producto, width=12).grid(row=0, column=2, padx=(0, 6))
        tk.Button(buttons_frame, text="Eliminar", command=self._eliminar_producto, bg="#ef4444", fg="white", width=12).grid(row=0, column=3)
        tk.Button(form_frame, text="Limpiar", command=self._limpiar_form, width=12).grid(row=12, column=0, pady=(8, 0), sticky="w")

        # Lista de productos (lado derecho)
        list_frame = tk.Frame(display_frame, bg="white", padx=12, pady=12)
        list_frame.grid(row=0, column=1, sticky="nsew")
        list_frame.grid_rowconfigure(0, weight=1)
        list_frame.grid_columnconfigure(0, weight=1)

        tk.Label(list_frame, text="Productos", bg="white", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w")
        self.listbox = tk.Listbox(list_frame, height=18)
        self.listbox.grid(row=1, column=0, sticky="nsew", pady=(6, 0))
        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.grid(row=1, column=1, sticky="ns", pady=(6, 0))
        self.listbox.configure(yscrollcommand=scrollbar.set)

        # Texto de información debajo
        self.info_text = tk.Text(self.frame, height=6, wrap="word")
        self.info_text.grid(row=3, column=0, sticky="ew", padx=20, pady=(12, 0))
        self.info_text.config(state="disabled")

        # Inicializar lista
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
        productos = self.restaurante_servicio.listar_productos()
        lines = [p.mostrar_informacion() for p in productos]
        # Actualizar lista visual
        self.listbox.delete(0, tk.END)
        for p in productos:
            self.listbox.insert(tk.END, p.mostrar_informacion())
        self._mostrar_info("Productos registrados", lines)

    def mostrar_usuarios(self) -> None:
        usuarios = self.restaurante_servicio.listar_usuarios()
        lines = [f"{usuario.usuario} - {usuario.nombre} - {usuario.correo}" for usuario in usuarios]
        self._mostrar_info("Usuarios registrados", lines)

    def mostrar_pendiente(self) -> None:
        self._mostrar_info("Ventas", ["Funcionalidad pendiente para la siguiente etapa."])

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
