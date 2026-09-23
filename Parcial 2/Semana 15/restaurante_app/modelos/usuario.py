from __future__ import annotations

from typing import Any


class Usuario:
    """Representa a un usuario del sistema."""

    def __init__(self, usuario: str, nombre: str, correo: str, password: str = "") -> None:
        self.usuario = self._validar_texto("usuario", usuario)
        self.nombre = self._validar_texto("nombre", nombre)
        self.correo = self._validar_texto("correo", correo)
        self.password = str(password).strip() if password is not None else ""

    @property
    def identificacion(self) -> str:
        return self.usuario

    @identificacion.setter
    def identificacion(self, valor: str) -> None:
        self.usuario = self._validar_texto("usuario", valor)

    @staticmethod
    def _validar_texto(nombre_campo: str, valor: Any) -> str:
        texto = str(valor).strip() if valor is not None else ""
        if not texto:
            raise ValueError(f"El campo '{nombre_campo}' no puede estar vacío.")
        return texto

    def mostrar_informacion(self) -> str:
        return f"Usuario: {self.usuario} | Nombre: {self.nombre} | Correo: {self.correo}"

    def to_dict(self) -> dict[str, Any]:
        return {
            "usuario": self.usuario,
            "nombre": self.nombre,
            "correo": self.correo,
            "password": self.password,
        }

    @classmethod
    def from_dict(cls, datos: dict[str, Any]) -> "Usuario":
        if not isinstance(datos, dict):
            raise KeyError("El registro de usuario no tiene el formato esperado.")
        usuario = datos.get("usuario") or datos.get("identificacion")
        if not usuario:
            raise KeyError("Falta el nombre de usuario o identificación.")
        return cls(
            usuario=usuario,
            nombre=datos.get("nombre") or datos.get("nombre_completo") or usuario,
            correo=datos.get("correo") or f"{usuario}@restaurante.local",
            password=datos.get("password", ""),
        )
