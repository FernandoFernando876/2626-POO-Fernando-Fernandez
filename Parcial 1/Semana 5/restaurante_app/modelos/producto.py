# Módulo: producto.py
# Descripción: Define la clase Producto que representa un plato, bebida o servicio del restaurante

class Producto:
    """
    Clase que representa un producto disponible en el restaurante.
    
    Atributos:
        id_producto (int): Identificador único del producto
        nombre (str): Nombre descriptivo del producto
        descripcion (str): Descripción detallada del producto
        precio (float): Precio del producto en unidades monetarias
        disponible (bool): Estado de disponibilidad del producto
    """
    
    def __init__(self, id_producto: int, nombre: str, descripcion: str, precio: float, disponible: bool = True):
        """
        Constructor de la clase Producto.
        
        Args:
            id_producto: Identificador único del producto
            nombre: Nombre del producto
            descripcion: Descripción del producto
            precio: Precio del producto
            disponible: Estado de disponibilidad (por defecto True)
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.disponible = disponible
    
    def obtener_disponibilidad(self) -> str:
        """Retorna el estado de disponibilidad del producto."""
        return "Disponible" if self.disponible else "No disponible"
    
    def cambiar_disponibilidad(self, disponible: bool) -> None:
        """Cambia el estado de disponibilidad del producto."""
        self.disponible = disponible
    
    def obtener_informacion_precio(self) -> str:
        """Retorna información formateada del precio del producto."""
        return f"${self.precio:.2f}"
    
    def __str__(self) -> str:
        """Representación en texto de un Producto."""
        return (
            f"[{self.id_producto}] {self.nombre}\n"
            f"  Descripción: {self.descripcion}\n"
            f"  Precio: {self.obtener_informacion_precio()}\n"
            f"  Estado: {self.obtener_disponibilidad()}"
        )

