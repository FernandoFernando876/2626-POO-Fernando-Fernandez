from __future__ import annotations

import json
from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:
    """Encapsula la carga y escritura de productos, usuarios y ventas en JSON."""

    def __init__(self, base_ruta: str | None = None) -> None:
        base_dir = Path(__file__).resolve().parent.parent
        if base_ruta is not None:
            self.base_dir = Path(base_ruta)
        else:
            self.base_dir = base_dir / "datos"
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.productos_path = self.base_dir / "productos.json"
        self.usuarios_path = self.base_dir / "usuarios.json"
        self.ventas_path = self.base_dir / "ventas.json"

    # Productos
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

    # Usuarios
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

    # Ventas
    def guardar_ventas(self, ventas: list[Venta]) -> None:
        try:
            with self.ventas_path.open("w", encoding="utf-8") as archivo:
                json.dump([venta.to_dict() for venta in ventas], archivo, ensure_ascii=False, indent=2)
        except PermissionError as exc:
            print(f"No tienes permisos para escribir en {self.ventas_path}: {exc}")
        except OSError as exc:
            print(f"No se pudo guardar la información en {self.ventas_path}: {exc}")

    def cargar_ventas(self) -> list[Venta]:
        ventas: list[Venta] = []
        try:
            with self.ventas_path.open("r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            return ventas
        except json.JSONDecodeError as exc:
            print(f"El archivo {self.ventas_path} no tiene un JSON válido: {exc}")
            return ventas
        except PermissionError as exc:
            print(f"No tienes permisos para leer {self.ventas_path}: {exc}")
            return ventas
        except OSError as exc:
            print(f"No se pudo abrir {self.ventas_path}: {exc}")
            return ventas

        if not isinstance(datos, list):
            print(f"El contenido de {self.ventas_path} no es una lista de ventas.")
            return ventas

        for item in datos:
            try:
                ventas.append(Venta.from_dict(item))
            except (KeyError, TypeError, ValueError) as exc:
                print(f"Se omite un registro inválido de venta: {exc}")
        return ventas
