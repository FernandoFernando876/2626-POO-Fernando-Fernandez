from __future__ import annotations

from typing import Any


class Venta:
    """Representa una venta entre un usuario y un producto."""

    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int) -> None:
        self.usuario_id: str = str(usuario_id).strip()
        self.producto_codigo: str = str(producto_codigo).strip()
        try:
            cantidad_int = int(cantidad)
        except (TypeError, ValueError) as exc:
            raise ValueError("La cantidad de la venta debe ser un número entero.") from exc
        if cantidad_int <= 0:
            raise ValueError("La cantidad de la venta debe ser mayor que 0.")
        self.cantidad: int = cantidad_int

    def to_dict(self) -> dict[str, Any]:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
        }

    @classmethod
    def from_dict(cls, datos: dict[str, Any]) -> "Venta":
        if not isinstance(datos, dict):
            raise KeyError("El registro de venta no tiene el formato esperado.")

        claves = ["usuario_id", "producto_codigo", "cantidad"]
        faltantes = [c for c in claves if c not in datos]
        if faltantes:
            raise KeyError(f"Faltan campos en la venta: {', '.join(faltantes)}")

        return cls(
            usuario_id=datos["usuario_id"],
            producto_codigo=datos["producto_codigo"],
            cantidad=datos["cantidad"],
        )

    def mostrar_informacion(self) -> str:
        return f"Usuario: {self.usuario_id} | Producto: {self.producto_codigo} | Cantidad: {self.cantidad}"
