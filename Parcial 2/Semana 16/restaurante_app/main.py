from __future__ import annotations

import tkinter as tk

try:
    from servicios.archivo_servicio import ArchivoServicio
    from servicios.restaurante_servicio import RestauranteServicio
    from ui.login_view import LoginView
    from ui.main_view import MainView
except ImportError:  # pragma: no cover
    from restaurante_app.servicios.archivo_servicio import ArchivoServicio
    from restaurante_app.servicios.restaurante_servicio import RestauranteServicio
    from restaurante_app.ui.login_view import LoginView
    from restaurante_app.ui.main_view import MainView


class Aplicacion:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Restaurante App - Semana 16")
        self.root.geometry("1000x720")
        self.root.minsize(850, 650)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.restaurante_servicio = RestauranteServicio(ArchivoServicio())
        self.login_view = LoginView(self.root, self.restaurante_servicio, on_login=self.mostrar_main_view)
        self.main_view = MainView(self.root, self.restaurante_servicio, on_logout=self.mostrar_login_view)

        self.mostrar_login_view()

    def mostrar_login_view(self) -> None:
        self.login_view.limpiar()
        self.login_view.frame.tkraise()

    def mostrar_main_view(self, usuario: str) -> None:
        self.main_view.establecer_usuario_actual(self.restaurante_servicio.obtener_usuario(usuario))
        self.main_view.mostrar_productos()
        self.main_view.frame.tkraise()

    def iniciar(self) -> None:
        self.root.mainloop()


def main() -> None:
    ventana = tk.Tk()
    app = Aplicacion(ventana)
    app.iniciar()


if __name__ == "__main__":
    main()
