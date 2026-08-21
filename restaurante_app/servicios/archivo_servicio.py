from __future__ import annotations

import json
from pathlib import Path

from modelos.producto import Producto


class ArchivoServicio:
    """Encapsula la carga y escritura de productos en formato JSON."""

    def __init__(self, ruta_archivo: str | None = None) -> None:
        if ruta_archivo is not None:
            self.ruta_archivo = Path(ruta_archivo)
        else:
            base_dir = Path(__file__).resolve().parent.parent
            self.ruta_archivo = base_dir / "datos" / "productos.json"

    def guardar_productos(self, productos: list[Producto]) -> None:
        try:
            self.ruta_archivo.parent.mkdir(parents=True, exist_ok=True)
            with self.ruta_archivo.open("w", encoding="utf-8") as archivo:
                json.dump([producto.to_dict() for producto in productos], archivo, ensure_ascii=False, indent=2)
        except PermissionError as exc:
            print(f"No tienes permisos para escribir en {self.ruta_archivo}: {exc}")
        except OSError as exc:
            print(f"No se pudo guardar la información en {self.ruta_archivo}: {exc}")

    def cargar_productos(self) -> list[Producto]:
        productos: list[Producto] = []

        try:
            with self.ruta_archivo.open("r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            return productos
        except json.JSONDecodeError as exc:
            print(f"El archivo {self.ruta_archivo} no tiene un JSON válido: {exc}")
            return productos
        except PermissionError as exc:
            print(f"No tienes permisos para leer {self.ruta_archivo}: {exc}")
            return productos
        except OSError as exc:
            print(f"No se pudo abrir {self.ruta_archivo}: {exc}")
            return productos

        if not isinstance(datos, list):
            print(f"El contenido de {self.ruta_archivo} no es una lista de productos.")
            return productos

        for item in datos:
            try:
                productos.append(Producto.from_dict(item))
            except (KeyError, TypeError, ValueError) as exc:
                print(f"Se omite un registro inválido: {exc}")

        return productos
