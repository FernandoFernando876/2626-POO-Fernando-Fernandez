from __future__ import annotations

from datetime import datetime
from typing import Any


class Venta:
    """Representa una venta entre un usuario, un producto y su fecha."""

    def __init__(
        self,
        usuario_id: str,
        producto_codigo: str,
        cantidad: int,
        fecha: str | None = None,
    ) -> None:
        self.usuario_id = str(usuario_id).strip()
        self.producto_codigo = str(producto_codigo).strip()
        if not self.usuario_id or not self.producto_codigo:
            raise ValueError("Usuario y producto son requeridos para una venta.")
        try:
            self.cantidad = int(cantidad)
        except (TypeError, ValueError) as exc:
            raise ValueError("La cantidad de la venta debe ser un número entero.") from exc
        if self.cantidad <= 0:
            raise ValueError("La cantidad de la venta debe ser mayor que 0.")
        self.fecha = fecha or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> dict[str, Any]:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
            "fecha": self.fecha,
        }

    @classmethod
    def from_dict(cls, datos: dict[str, Any]) -> "Venta":
        if not isinstance(datos, dict):
            raise KeyError("El registro de venta no tiene el formato esperado.")
        requeridos = ("usuario_id", "producto_codigo", "cantidad")
        faltantes = [campo for campo in requeridos if campo not in datos]
        if faltantes:
            raise KeyError(f"Faltan campos en la venta: {', '.join(faltantes)}")
        return cls(
            usuario_id=datos["usuario_id"],
            producto_codigo=datos["producto_codigo"],
            cantidad=datos["cantidad"],
            fecha=datos.get("fecha"),
        )

    def mostrar_informacion(self) -> str:
        return (
            f"Fecha: {self.fecha} | Usuario: {self.usuario_id} | "
            f"Producto: {self.producto_codigo} | Cantidad: {self.cantidad}"
        )
