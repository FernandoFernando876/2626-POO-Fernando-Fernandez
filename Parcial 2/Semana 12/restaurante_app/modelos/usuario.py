from __future__ import annotations

from typing import Any


class Usuario:
    """
    Representa un usuario general del sistema.

    Atributos:
        identificacion: id única del usuario (str)
        nombre: nombre completo (str)
        correo: correo electrónico (str)
    """

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = self._validar_texto("identificacion", identificacion)
        self.nombre: str = self._validar_texto("nombre", nombre)
        self.correo: str = self._validar_texto("correo", correo)

    @staticmethod
    def _validar_texto(nombre_campo: str, valor: Any) -> str:
        texto = str(valor).strip() if valor is not None else ""
        if not texto:
            raise ValueError(f"El campo '{nombre_campo}' no puede estar vacío.")
        return texto

    def mostrar_informacion(self) -> str:
        return f"ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"

    def to_dict(self) -> dict[str, Any]:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
        }

    @classmethod
    def from_dict(cls, datos: dict[str, Any]) -> "Usuario":
        if not isinstance(datos, dict):
            raise KeyError("El registro de usuario no tiene el formato esperado.")

        claves = ["identificacion", "nombre", "correo"]
        faltantes = [c for c in claves if c not in datos]
        if faltantes:
            raise KeyError(f"Faltan campos del usuario: {', '.join(faltantes)}")

        return cls(
            identificacion=datos["identificacion"],
            nombre=datos["nombre"],
            correo=datos["correo"],
        )

