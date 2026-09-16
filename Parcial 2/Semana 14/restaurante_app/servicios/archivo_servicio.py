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
    """Encapsula la lectura y escritura de datos del restaurante en JSON."""

    def __init__(self, base_ruta: str | None = None) -> None:
        base_dir = Path(__file__).resolve().parent.parent
        self.base_dir = Path(base_ruta) if base_ruta is not None else base_dir / "datos"
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.productos_path = self.base_dir / "productos.json"
        self.usuarios_path = self.base_dir / "usuarios.json"

        if not self.productos_path.exists():
            self.guardar_productos([])
        if not self.usuarios_path.exists():
            self.guardar_usuarios([])

    def guardar_productos(self, productos: list[Producto]) -> None:
        try:
            with self.productos_path.open("w", encoding="utf-8") as archivo:
                json.dump([producto.to_dict() for producto in productos], archivo, ensure_ascii=False, indent=2)
        except PermissionError as exc:
            print(f"No tienes permisos para escribir en {self.productos_path}: {exc}")
        except OSError as exc:
            print(f"No se pudo guardar la información en {self.productos_path}: {exc}")

    def cargar_productos(self) -> list[Producto]:
        productos: list[Producto] = []
        try:
            with self.productos_path.open("r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            return productos
        except json.JSONDecodeError as exc:
            print(f"El archivo {self.productos_path} no tiene un JSON válido: {exc}")
            return productos
        except PermissionError as exc:
            print(f"No tienes permisos para leer {self.productos_path}: {exc}")
            return productos
        except OSError as exc:
            print(f"No se pudo abrir {self.productos_path}: {exc}")
            return productos

        if not isinstance(datos, list):
            print(f"El contenido de {self.productos_path} no es una lista de productos.")
            return productos

        for item in datos:
            try:
                productos.append(Producto.from_dict(item))
            except (KeyError, TypeError, ValueError) as exc:
                print(f"Se omite un registro inválido de producto: {exc}")
        return productos

    def guardar_usuarios(self, usuarios: list[Usuario]) -> None:
        try:
            with self.usuarios_path.open("w", encoding="utf-8") as archivo:
                json.dump([usuario.to_dict() for usuario in usuarios], archivo, ensure_ascii=False, indent=2)
        except PermissionError as exc:
            print(f"No tienes permisos para escribir en {self.usuarios_path}: {exc}")
        except OSError as exc:
            print(f"No se pudo guardar la información en {self.usuarios_path}: {exc}")

    def cargar_usuarios(self) -> list[Usuario]:
        usuarios: list[Usuario] = []
        try:
            with self.usuarios_path.open("r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            return usuarios
        except json.JSONDecodeError as exc:
            print(f"El archivo {self.usuarios_path} no tiene un JSON válido: {exc}")
            return usuarios
        except PermissionError as exc:
            print(f"No tienes permisos para leer {self.usuarios_path}: {exc}")
            return usuarios
        except OSError as exc:
            print(f"No se pudo abrir {self.usuarios_path}: {exc}")
            return usuarios

        if not isinstance(datos, list):
            print(f"El contenido de {self.usuarios_path} no es una lista de usuarios.")
            return usuarios

        for item in datos:
            try:
                usuarios.append(Usuario.from_dict(item))
            except (KeyError, TypeError, ValueError) as exc:
                print(f"Se omite un registro inválido de usuario: {exc}")
        return usuarios
