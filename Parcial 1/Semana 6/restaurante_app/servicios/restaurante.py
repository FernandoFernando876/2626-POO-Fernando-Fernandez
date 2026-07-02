# Módulo: restaurante.py
# Descripción: Clase de servicio que gestiona la lista de productos del restaurante y demuestra polimorfismo.

from typing import List
from modelos.producto import Producto

class Restaurante:
    """
    Clase de servicio encargada de administrar el menú de productos del restaurante.
    
    Atributos:
        nombre (str): Nombre del restaurante.
        lista_productos (List[Producto]): Lista de productos registrados en el restaurante.
    """

    def __init__(self, nombre: str):
        """
        Constructor de la clase Restaurante.

        Args:
            nombre: Nombre del restaurante.
        """
        self.nombre = nombre
        self.lista_productos: List[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        """
        Agrega un producto (Platillo o Bebida) a la lista del restaurante.

        Args:
            producto: Objeto que hereda de la clase base Producto.
        """
        self.lista_productos.append(producto)
        print(f"[OK] Producto '{producto.nombre}' agregado exitosamente al menu.")

    def mostrar_menu(self) -> None:
        """
        Muestra la información de todos los productos registrados en el restaurante.
        Demuestra polimorfismo al llamar a mostrar_informacion() en objetos
        que pueden ser tanto Platillos como Bebidas.
        """
        print("\n" + "=" * 60)
        print(f"MENU DEL RESTAURANTE: {self.nombre.upper()}")
        print("=" * 60)
        
        if not self.lista_productos:
            print("El menú está vacío. Registre productos primero.")
            print("=" * 60 + "\n")
            return

        for index, producto in enumerate(self.lista_productos, start=1):
            # Aquí ocurre el Polimorfismo: se ejecuta mostrar_informacion() de Platillo o Bebida 
            # de forma transparente según el tipo real del objeto.
            print(f"Item #{index}:")
            print(producto.mostrar_informacion())
            print("-" * 45)
            
        print("=" * 60 + "\n")
