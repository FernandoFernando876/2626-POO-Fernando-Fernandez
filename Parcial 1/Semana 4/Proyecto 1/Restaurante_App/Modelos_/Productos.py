# Clase que representa un producto (plato o bebida) del restaurante
class Producto:
    """
    Representa un producto disponible en el restaurante.

    Atributos:
        id (int): Identificador único del producto
        nombre (str): Nombre del producto
        descripcion (str): Descripción breve del producto
        precio (float): Precio del producto
        disponible (bool): Indica si el producto está disponible
    """

    def __init__(self, id, nombre, descripcion, precio):
        """
        Inicializa un nuevo producto.

        Args:
            id: Identificador único del producto
            nombre: Nombre del producto
            descripcion: Descripción del producto
            precio: Precio del producto
        """
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.disponible = True

    def __str__(self):
        """Representación en texto del producto."""
        estado = "Disponible" if self.disponible else "No disponible"
        return f"[{self.id}] {self.nombre} - ${self.precio:.2f} ({estado})\n    {self.descripcion}"

    def cambiar_disponibilidad(self):
        """Cambia el estado de disponibilidad del producto."""
        self.disponible = not self.disponible

    def obtener_informacion(self):
        """Retorna la información del producto de forma detallada."""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'disponible': self.disponible
        }

