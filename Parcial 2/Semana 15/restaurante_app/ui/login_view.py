from __future__ import annotations

import tkinter as tk
from typing import Callable


class LoginView:
    def __init__(
        self,
        root: tk.Misc,
        restaurante_servicio,
        on_login: Callable[[], None] | None = None,
    ) -> None:
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.on_login = on_login

        self.frame = tk.Frame(self.root, bg="#f4f4f4", padx=40, pady=40)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

        card = tk.Frame(self.frame, bg="white", padx=24, pady=24, bd=1, relief="solid")
        card.grid(row=0, column=0, sticky="nsew")
        card.grid_columnconfigure(0, weight=1)

        title = tk.Label(
            card,
            text="Restaurante App",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#1f2937",
        )
        title.grid(row=0, column=0, sticky="ew", pady=(0, 18))

        subtitle = tk.Label(
            card,
            text="Iniciar sesión",
            font=("Arial", 12),
            bg="white",
            fg="#374151",
        )
        subtitle.grid(row=1, column=0, sticky="ew", pady=(0, 18))

        tk.Label(card, text="Usuario", bg="white", fg="#374151").grid(row=2, column=0, sticky="w")
        self.usuario_var = tk.StringVar()
        usuario_entry = tk.Entry(card, textvariable=self.usuario_var, width=30, font=("Arial", 11))
        usuario_entry.grid(row=3, column=0, sticky="ew", pady=(4, 10))
        usuario_entry.focus_set()

        tk.Label(card, text="Contraseña", bg="white", fg="#374151").grid(row=4, column=0, sticky="w")
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(card, textvariable=self.password_var, width=30, show="*", font=("Arial", 11))
        password_entry.grid(row=5, column=0, sticky="ew", pady=(4, 12))

        self.mensaje_var = tk.StringVar(value="")
        self.error_label = tk.Label(card, textvariable=self.mensaje_var, fg="#b91c1c", bg="white")
        self.error_label.grid(row=6, column=0, sticky="ew", pady=(0, 10))

        login_button = tk.Button(
            card,
            text="Ingresar",
            command=self._autenticar,
            bg="#2563eb",
            fg="white",
            font=("Arial", 11, "bold"),
            width=18,
            height=1,
        )
        login_button.grid(row=7, column=0, sticky="ew")

        admin_label = tk.Label(
            card,
            text="Credenciales de administrador: Admin / Admin123",
            bg="white",
            fg="#1d4ed8",
            font=("Arial", 9, "bold"),
        )
        admin_label.grid(row=8, column=0, sticky="ew", pady=(14, 0))

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

    def _autenticar(self) -> None:
        usuario = self.usuario_var.get().strip()
        password = self.password_var.get().strip()

        if not usuario or not password:
            self.mostrar_mensaje("Debes completar usuario y contraseña.")
            return

        if self.restaurante_servicio.validar_acceso(usuario, password):
            self.mostrar_mensaje("")
            if self.on_login is not None:
                self.on_login()
            return

        self.mostrar_mensaje("Credenciales incorrectas. Intenta nuevamente.")

    def mostrar_mensaje(self, mensaje: str) -> None:
        self.mensaje_var.set(mensaje)

    def limpiar(self) -> None:
        self.usuario_var.set("")
        self.password_var.set("")
        self.mostrar_mensaje("")
