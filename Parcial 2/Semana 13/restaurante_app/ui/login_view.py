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

        self.frame = tk.Frame(self.root, bg="#f3f4f6", padx=40, pady=40)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

        card = tk.Frame(self.frame, bg="white", bd=1, relief="solid", padx=24, pady=24)
        card.grid(row=0, column=0, sticky="nsew")
        card.grid_columnconfigure(0, weight=1)

        title = tk.Label(card, text="Restaurante App", font=("Arial", 18, "bold"), bg="white", fg="#111827")
        title.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        subtitle = tk.Label(card, text="Iniciar sesión", font=("Arial", 12), bg="white", fg="#374151")
        subtitle.grid(row=1, column=0, sticky="ew", pady=(0, 15))

        tk.Label(card, text="Usuario", bg="white", fg="#374151").grid(row=2, column=0, sticky="w")
        self.usuario_var = tk.StringVar()
        entry_usuario = tk.Entry(card, textvariable=self.usuario_var, width=30, font=("Arial", 11))
        entry_usuario.grid(row=3, column=0, sticky="ew", pady=(4, 12))
        entry_usuario.focus_set()

        tk.Label(card, text="Contraseña", bg="white", fg="#374151").grid(row=4, column=0, sticky="w")
        self.password_var = tk.StringVar()
        entry_password = tk.Entry(card, textvariable=self.password_var, width=30, show="*", font=("Arial", 11))
        entry_password.grid(row=5, column=0, sticky="ew", pady=(4, 12))

        self.mensaje_var = tk.StringVar(value="")
        label_mensaje = tk.Label(card, textvariable=self.mensaje_var, bg="white", fg="#b91c1c")
        label_mensaje.grid(row=6, column=0, sticky="ew", pady=(0, 12))

        boton = tk.Button(
            card,
            text="Ingresar",
            command=self._autenticar,
            bg="#2563eb",
            fg="white",
            font=("Arial", 11, "bold"),
            width=18,
        )
        boton.grid(row=7, column=0, sticky="ew")

        footer = tk.Label(card, text="Credenciales de prueba: admin / admin123", bg="white", fg="#6b7280")
        footer.grid(row=8, column=0, sticky="ew", pady=(18, 0))

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
