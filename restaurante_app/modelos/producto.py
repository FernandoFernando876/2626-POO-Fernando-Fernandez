from __future__ import annotations

from typing import Any


class Producto:
    """Representa un producto del restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = self._validar_campo_texto("codigo", codigo)
        self.nombre: str = self._validar_campo_texto("nombre", nombre)
        self.categoria: str = self._validar_campo_texto("categoria", categoria)
        self.precio: float = self._validar_precio(precio)

    @staticmethod
    def _validar_campo_texto(nombre_campo: str, valor: Any) -> str:
        texto = str(valor).strip() if valor is not None else ""
        if not texto:
            raise ValueError(f"El campo '{nombre_campo}' no puede estar vacío.")
        return texto

    @staticmethod
    def _validar_precio(valor: Any) -> float:
        try:
            precio = float(valor)
        except (TypeError, ValueError) as exc:
            raise ValueError("El precio debe ser un número válido.") from exc
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        return precio

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: {self.precio:.2f}"
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
        }

    @classmethod
    def from_dict(cls, datos: dict[str, Any]) -> "Producto":
        if not isinstance(datos, dict):
            raise KeyError("El registro de producto no tiene el formato esperado.")

        claves_requeridas = ["codigo", "nombre", "categoria", "precio"]
        faltantes = [clave for clave in claves_requeridas if clave not in datos]
        if faltantes:
            raise KeyError(f"Faltan campos del producto: {', '.join(faltantes)}")

        return cls(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            categoria=datos["categoria"],
            precio=datos["precio"],
        )

