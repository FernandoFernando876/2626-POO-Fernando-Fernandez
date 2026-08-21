from typing import Dict, Any


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
        self.tipo: str = "Producto"

    def mostrar_informacion(self) -> str:
        """
        Devuelve una representación textual del producto.
        Diseñado para ser sobrescrito por clases hijas manteniendo compatibilidad.
        """
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Categoría: {self.categoria} | Precio: {self.precio:.2f}"

    def a_diccionario(self) -> Dict[str, Any]:
        """
        Convierte el objeto Producto a un diccionario para ser almacenado en JSON.
        Incluye un campo 'tipo' para identificar la clase al cargar desde JSON.
        """
        return {
            "tipo": self.tipo,
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }

