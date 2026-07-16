from .producto import Producto

class Bebida(Producto):
    """
    Bebida hereda de Producto e incorpora atributos específicos.
    Atributos adicionales:
        tamano: e.g., '500ml', '1L'
        envase: e.g., 'lata', 'botella', 'vaso'
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamano: str, envase: str) -> None:
        super().__init__(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)
        self.tamano: str = tamano.strip()
        self.envase: str = envase.strip()

    def mostrar_informacion(self) -> str:
        """
        Mantiene la firma de Producto.mostrar_informacion() para garantizar Liskov.
        """
        base = super().mostrar_informacion()
        return f"{base} | Tamaño: {self.tamano} | Envase: {self.envase}"

