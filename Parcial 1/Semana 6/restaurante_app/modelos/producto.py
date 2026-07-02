# Módulo: producto.py
# Descripción: Define la clase padre Producto con encapsulación del precio.

class Producto:
    """
    Clase base que representa un producto genérico en el restaurante.

    Atributos:
        nombre (str): Nombre descriptivo del producto.
        __precio (float): Precio del producto (atributo encapsulado de forma privada).
        disponible (bool): Estado que indica si el producto está disponible.
    """

    def __init__(self, nombre: str, precio: float, disponible: bool = True):
        """
        Constructor de la clase Producto.

        Args:
            nombre: Nombre del producto.
            precio: Precio del producto (debe ser mayor a cero).
            disponible: Estado de disponibilidad (por defecto True).
        """
        self.nombre = nombre
        self.disponible = disponible
        
        # Uso de encapsulación para proteger el precio
        self.__precio = 0.0
        self.cambiar_precio(precio)  # Reutilizamos el setter para aplicar la validación inicial

    def obtener_precio(self) -> float:
        """
        Método de acceso (Getter) para obtener el precio encapsulado.
        
        Returns:
            float: El precio del producto.
        """
        return self.__precio

    def cambiar_precio(self, nuevo_precio: float) -> None:
        """
        Método de modificación (Setter) para cambiar el precio con validación.
        El precio debe ser estrictamente mayor que cero.

        Args:
            nuevo_precio: El nuevo precio que se le quiere asignar al producto.
        """
        if nuevo_precio <= 0:
            raise ValueError(f"Error: El precio (${nuevo_precio}) debe ser un numero positivo mayor que cero.")
        self.__precio = nuevo_precio

    def obtener_estado_disponibilidad(self) -> str:
        """Retorna el estado de disponibilidad en formato de texto."""
        return "Disponible" if self.disponible else "Agotado"

    def mostrar_informacion(self) -> str:
        """
        Retorna la información básica del producto.
        Este método será sobrescrito en las clases hijas para demostrar polimorfismo.
        """
        return (
            f"Producto: {self.nombre}\n"
            f"  Precio: ${self.obtener_precio():.2f}\n"
            f"  Estado: {self.obtener_estado_disponibilidad()}"
        )
