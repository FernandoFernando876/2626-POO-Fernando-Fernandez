from __future__ import annotations

from typing import Any


class Producto:
    """Representa un producto del restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> None:
        self.codigo = self._validar_texto("codigo", codigo)
        self.nombre = self._validar_texto("nombre", nombre)
        self.categoria = self._validar_texto("categoria", categoria)
        self.precio = self._validar_precio(precio)
        self.stock = self._validar_stock(stock)

    @staticmethod
    def _validar_texto(nombre_campo: str, valor: Any) -> str:
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
            raise ValueError("El precio debe ser mayor que cero.")
        return precio

    @staticmethod
    def _validar_stock(valor: Any) -> int:
        try:
            stock = int(valor)
        except (TypeError, ValueError) as exc:
            raise ValueError("El stock debe ser un número entero.") from exc
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        return stock

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: ${self.precio:.2f} | Stock: {self.stock}"
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
        }

    @classmethod
    def from_dict(cls, datos: dict[str, Any]) -> "Producto":
        if not isinstance(datos, dict):
            raise KeyError("El producto no tiene un formato válido.")

        campos = ["codigo", "nombre", "categoria", "precio", "stock"]
        faltantes = [campo for campo in campos if campo not in datos]
        if faltantes:
            raise KeyError(f"Faltan campos del producto: {', '.join(faltantes)}")

        return cls(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            categoria=datos["categoria"],
            precio=datos["precio"],
            stock=datos["stock"],
        )
