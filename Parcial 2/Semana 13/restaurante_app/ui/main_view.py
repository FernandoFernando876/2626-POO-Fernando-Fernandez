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
        self.frame.grid_rowconfigure(2, weight=1)

        header = tk.Frame(self.frame, bg="#1f2937", padx=18, pady=16)
        header.grid(row=0, column=0, sticky="ew")
        header.grid_columnconfigure(0, weight=1)

        tk.Label(header, text="Panel principal", fg="white", bg="#1f2937", font=("Arial", 16, "bold")).grid(row=0, column=0, sticky="w")

        toolbar = tk.Frame(self.frame, bg="#e5e7eb")
        toolbar.grid(row=1, column=0, sticky="ew", pady=(16, 12))

        tk.Button(toolbar, text="Productos", command=self.mostrar_productos, width=18).grid(row=0, column=0, padx=(0, 10), sticky="w")
        tk.Button(toolbar, text="Usuarios", command=self.mostrar_usuarios, width=18).grid(row=0, column=1, padx=(0, 10), sticky="w")
        tk.Button(toolbar, text="Ventas (pendiente)", command=self.mostrar_pendiente, width=18).grid(row=0, column=2, padx=(0, 10), sticky="w")
        tk.Button(toolbar, text="Cerrar sesión", command=self._logout, width=18, bg="#dc2626", fg="white").grid(row=0, column=3, sticky="e")

        content = tk.Frame(self.frame, bg="white", bd=1, relief="solid")
        content.grid(row=2, column=0, sticky="nsew")
        content.grid_columnconfigure(0, weight=1)
        content.grid_rowconfigure(0, weight=1)

        self.info_text = tk.Text(content, height=18, width=100, wrap="word")
        self.info_text.grid(row=0, column=0, sticky="nsew", padx=12, pady=12)
        self.info_text.config(state="disabled")

    def mostrar_productos(self) -> None:
        productos = self.restaurante_servicio.listar_productos()
        lines = [producto.mostrar_informacion() for producto in productos]
        self._mostrar_lista("Productos registrados", lines)

    def mostrar_usuarios(self) -> None:
        usuarios = self.restaurante_servicio.listar_usuarios()
        lines = [f"Usuario: {usuario.usuario} | Nombre: {usuario.nombre} | Correo: {usuario.correo}" for usuario in usuarios]
        self._mostrar_lista("Usuarios registrados", lines)

    def mostrar_pendiente(self) -> None:
        self._mostrar_lista("Ventas", ["Funcionalidad pendiente para la siguiente etapa."])

    def _mostrar_lista(self, titulo: str, elementos: list[str]) -> None:
        self.info_text.config(state="normal")
        self.info_text.delete("1.0", tk.END)
        self.info_text.insert(tk.END, f"{titulo}\n\n")

        if not elementos:
            self.info_text.insert(tk.END, "No hay registros disponibles.")
        else:
            for elemento in elementos:
                self.info_text.insert(tk.END, f"- {elemento}\n")

        self.info_text.config(state="disabled")

    def _logout(self) -> None:
        if self.on_logout is not None:
            self.on_logout()
