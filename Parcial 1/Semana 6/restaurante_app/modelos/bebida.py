# Módulo: bebida.py
# Descripción: Define la clase hija Bebida que hereda de Producto y añade el volumen en ml.

from .producto import Producto

class Bebida(Producto):
    """
    Clase que representa una bebida en el restaurante.
    Hereda de la clase Producto.

    Atributos adicionales:
        volumen_ml (int): Volumen de la bebida en mililitros (ml).
    """

    def __init__(self, nombre: str, precio: float, volumen_ml: int, disponible: bool = True):
        """
        Constructor de la clase Bebida.

        Args:
            nombre: Nombre de la bebida.
            precio: Precio de la bebida.
            volumen_ml: Volumen de la bebida en mililitros (debe ser mayor a cero).
            disponible: Estado de disponibilidad (por defecto True).
        """
        # Inicialización de la clase padre mediante super()
        super().__init__(nombre, precio, disponible)
        
        if volumen_ml <= 0:
            raise ValueError("El volumen en mililitros debe ser mayor a cero.")
        self.volumen_ml = volumen_ml

    def mostrar_informacion(self) -> str:
        """
        Sobrescribe el método de la clase padre para agregar detalles de la bebida.
        Demuestra polimorfismo.
        """
        info_padre = super().mostrar_informacion()
        return (
            f"{info_padre}\n"
            f"  Tipo: Bebida\n"
            f"  Volumen: {self.volumen_ml} ml"
        )
