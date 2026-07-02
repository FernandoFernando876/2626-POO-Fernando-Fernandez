# Módulo: platillo.py
# Descripción: Define la clase hija Platillo que hereda de Producto y añade tiempo de preparación.

from .producto import Producto

class Platillo(Producto):
    """
    Clase que representa un platillo de comida en el restaurante.
    Hereda de la clase Producto.

    Atributos adicionales:
        tiempo_preparacion (int): Tiempo de preparación estimado en minutos.
    """

    def __init__(self, nombre: str, precio: float, tiempo_preparacion: int, disponible: bool = True):
        """
        Constructor de la clase Platillo.

        Args:
            nombre: Nombre del platillo.
            precio: Precio del platillo.
            tiempo_preparacion: Tiempo estimado en minutos (debe ser mayor a cero).
            disponible: Estado de disponibilidad (por defecto True).
        """
        # Inicialización de la clase padre mediante super()
        super().__init__(nombre, precio, disponible)
        
        if tiempo_preparacion <= 0:
            raise ValueError("El tiempo de preparacion debe ser mayor a cero minutos.")
        self.tiempo_preparacion = tiempo_preparacion

    def mostrar_informacion(self) -> str:
        """
        Sobrescribe el método de la clase padre para agregar detalles del platillo.
        Demuestra polimorfismo.
        """
        info_padre = super().mostrar_informacion()
        return (
            f"{info_padre}\n"
            f"  Tipo: Platillo de Comida\n"
            f"  Tiempo de Preparacion: {self.tiempo_preparacion} min"
        )
