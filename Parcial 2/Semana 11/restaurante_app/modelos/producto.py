from __future__ import annotations

from typing import Any


class Producto:
    """Representa un producto del restaurante con control de stock."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0) -> None:
        self.codigo: str = self._validar_campo_texto("codigo", codigo)
        self.nombre: str = self._validar_campo_texto("nombre", nombre)
        self.categoria: str = self._validar_campo_texto("categoria", categoria)
        self.precio: float = self._validar_precio(precio)
        self.stock: int = self._validar_stock(stock)

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
            f"Categoría: {self.categoria} | Precio: {self.precio:.2f} | Stock: {self.stock}"
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
            raise KeyError("El registro de producto no tiene el formato esperado.")

        claves_requeridas = ["codigo", "nombre", "categoria", "precio", "stock"]
        faltantes = [clave for clave in claves_requeridas if clave not in datos]
        if faltantes:
            raise KeyError(f"Faltan campos del producto: {', '.join(faltantes)}")

        return cls(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            categoria=datos["categoria"],
            precio=datos["precio"],
            stock=datos["stock"],
        )

    def vender(self, cantidad: int) -> None:
        """Disminuye el stock cuando se realiza una venta. Lanza ValueError si no hay stock suficiente."""
        try:
            cantidad_int = int(cantidad)
        except (TypeError, ValueError) as exc:
            raise ValueError("La cantidad a vender debe ser un número entero.") from exc
        if cantidad_int <= 0:
            raise ValueError("La cantidad a vender debe ser mayor que 0.")
        if cantidad_int > self.stock:
            raise ValueError("Stock insuficiente para realizar la venta.")
        self.stock -= cantidad_int
