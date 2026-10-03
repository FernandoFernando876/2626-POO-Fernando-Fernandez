from __future__ import annotations

from typing import Any


class Usuario:
    """Representa a una persona que usa el sistema del restaurante."""

    ROLES = ("Administrador", "Empleado", "Cliente")

    def __init__(
        self,
        usuario: str,
        nombre: str,
        correo: str,
        password: str = "",
        rol: str = "Cliente",
        id: int | None = None,
    ) -> None:
        self.usuario = self._validar_texto("usuario", usuario)
        self.nombre = self._validar_texto("nombre", nombre)
        self.correo = self._validar_texto("correo", correo)
        self.password = str(password).strip() if password is not None else ""
        self.rol = self._validar_rol(rol)
        if id is not None and (not isinstance(id, int) or id <= 0):
            raise ValueError("El identificador debe ser un entero positivo.")
        self.id = id

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

    @classmethod
    def _validar_rol(cls, rol: str) -> str:
        normalizado = str(rol).strip().casefold()
        for rol_valido in cls.ROLES:
            if normalizado == rol_valido.casefold():
                return rol_valido
        raise ValueError("El rol debe ser Administrador, Empleado o Cliente.")

    def mostrar_informacion(self) -> str:
        return f"Usuario: {self.usuario} | Nombre: {self.nombre} | Rol: {self.rol}"

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "usuario": self.usuario,
            "nombre": self.nombre,
            "correo": self.correo,
            "password": self.password,
            "rol": self.rol,
        }

    @classmethod
    def from_dict(cls, datos: dict[str, Any]) -> "Usuario":
        if not isinstance(datos, dict):
            raise KeyError("El registro de usuario no tiene el formato esperado.")
        usuario = datos.get("usuario") or datos.get("identificacion")
        if not usuario:
            raise KeyError("Falta el nombre de usuario o identificación.")
        rol = datos.get("rol")
        if not rol:
            rol = "Administrador" if str(usuario).casefold() == "admin" else "Cliente"
        identificador = datos.get("id")
        if identificador is not None:
            try:
                identificador = int(identificador)
            except (TypeError, ValueError) as exc:
                raise ValueError("El identificador del usuario debe ser numérico.") from exc
        return cls(
            usuario=usuario,
            nombre=datos.get("nombre") or datos.get("nombre_completo") or usuario,
            correo=datos.get("correo") or f"{usuario}@restaurante.local",
            password=datos.get("password", ""),
            rol=rol,
            id=identificador,
        )
