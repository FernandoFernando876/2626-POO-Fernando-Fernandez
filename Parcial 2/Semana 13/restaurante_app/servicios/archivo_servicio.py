from __future__ import annotations

import json
from pathlib import Path

try:
    from restaurante_app.modelos.producto import Producto
    from restaurante_app.modelos.usuario import Usuario
except ImportError:  # pragma: no cover
    from modelos.producto import Producto
    from modelos.usuario import Usuario


class ArchivoServicio:
    """Gestiona la lectura de productos y usuarios desde archivos JSON."""

    def __init__(self, base_ruta: str | None = None) -> None:
        if base_ruta is not None:
            self.base_dir = Path(base_ruta)
        else:
            self.base_dir = Path(__file__).resolve().parent.parent / "datos"

        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.productos_path = self.base_dir / "productos.json"
        self.usuarios_path = self.base_dir / "usuarios.json"

    def cargar_productos(self) -> list[Producto]:
        productos: list[Producto] = []
        try:
            with self.productos_path.open("r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            return productos
        except (json.JSONDecodeError, OSError):
            return productos

        if not isinstance(datos, list):
            return productos

        for item in datos:
            try:
                productos.append(Producto.from_dict(item))
            except (KeyError, TypeError, ValueError):
                continue
        return productos

    def cargar_usuarios(self) -> list[Usuario]:
        usuarios: list[Usuario] = []
        try:
            with self.usuarios_path.open("r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            return usuarios
        except (json.JSONDecodeError, OSError):
            return usuarios

        if not isinstance(datos, list):
            return usuarios

        for item in datos:
            try:
                usuarios.append(Usuario.from_dict(item))
            except (KeyError, TypeError, ValueError):
                continue
        return usuarios
