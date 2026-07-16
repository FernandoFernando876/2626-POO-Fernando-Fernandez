class Producto:
    """
    Representa un producto genérico del restaurante.
    Atributos:
        codigo: identificador único del producto (str)
        nombre: nombre del producto (str)
        categoria: categoría o tipo (str)
        precio: precio en unidades monetarias (float)
    """

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = codigo.strip()
        self.nombre: str = nombre.strip()
        self.categoria: str = categoria.strip()
        self.precio: float = float(precio)

    def mostrar_informacion(self) -> str:
        """
        Devuelve una representación textual del producto.
        Diseñado para ser sobrescrito por clases hijas manteniendo compatibilidad.
        """
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Categoría: {self.categoria} | Precio: {self.precio:.2f}"

