from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType


def _cargar_aplicacion_semana_16() -> ModuleType:
    carpeta_app = Path(__file__).resolve().parent.parent / "Parcial 2" / "Semana 16" / "restaurante_app"
    sys.path.insert(0, str(carpeta_app))
    especificacion = importlib.util.spec_from_file_location(
        "restaurante_semana_16_main",
        carpeta_app / "main.py",
    )
    if especificacion is None or especificacion.loader is None:
        raise ImportError(f"No se pudo cargar la aplicación de Semana 16 desde {carpeta_app}.")
    aplicacion = importlib.util.module_from_spec(especificacion)
    sys.modules[especificacion.name] = aplicacion
    especificacion.loader.exec_module(aplicacion)
    return aplicacion


def main() -> None:
    _cargar_aplicacion_semana_16().main()


if __name__ == "__main__":
    main()
