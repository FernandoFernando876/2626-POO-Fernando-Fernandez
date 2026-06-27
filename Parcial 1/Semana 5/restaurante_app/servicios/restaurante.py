# Módulo: restaurante.py
# Descripción: Define la clase Restaurante que gestiona productos y clientes

from typing import List
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase que administra el sistema del restaurante.
    
    Responsabilidades:
        - Gestionar una lista de productos disponibles
        - Gestionar una lista de clientes registrados
        - Proporcionar métodos para agregar, consultar y mostrar información
    
    Atributos:
        nombre_restaurante (str): Nombre del restaurante
        lista_productos (List[Producto]): Lista de productos disponibles
        lista_clientes (List[Cliente]): Lista de clientes registrados
    """
    
    def __init__(self, nombre_restaurante: str):
        """
        Constructor de la clase Restaurante.
        
        Args:
            nombre_restaurante: Nombre del restaurante
        """
        self.nombre_restaurante = nombre_restaurante
        self.lista_productos: List[Producto] = []
        self.lista_clientes: List[Cliente] = []
    
    # Métodos relacionados con Productos
    
    def agregar_producto(self, producto: Producto) -> None:
        """
        Agrega un producto a la lista de productos del restaurante.
        
        Args:
            producto: Objeto de tipo Producto a agregar
        """
        self.lista_productos.append(producto)
    
    def obtener_total_productos(self) -> int:
        """Retorna la cantidad total de productos registrados."""
        return len(self.lista_productos)
    
    def obtener_productos_disponibles(self) -> List[Producto]:
        """Retorna una lista de productos disponibles."""
        return [p for p in self.lista_productos if p.disponible]
    
    def mostrar_productos(self) -> str:
        """Retorna una representación en texto de todos los productos."""
        if not self.lista_productos:
            return "No hay productos registrados."
        
        informacion = "─" * 60 + "\n"
        informacion += "PRODUCTOS DEL RESTAURANTE\n"
        informacion += "─" * 60 + "\n"
        
        for producto in self.lista_productos:
            informacion += str(producto) + "\n"
        
        informacion += "─" * 60
        return informacion
    
    # Métodos relacionados con Clientes
    
    def agregar_cliente(self, cliente: Cliente) -> None:
        """
        Agrega un cliente a la lista de clientes del restaurante.
        
        Args:
            cliente: Objeto de tipo Cliente a agregar
        """
        self.lista_clientes.append(cliente)
    
    def obtener_total_clientes(self) -> int:
        """Retorna la cantidad total de clientes registrados."""
        return len(self.lista_clientes)
    
    def obtener_clientes_activos(self) -> List[Cliente]:
        """Retorna una lista de clientes activos."""
        return [c for c in self.lista_clientes if c.activo]
    
    def mostrar_clientes(self) -> str:
        """Retorna una representación en texto de todos los clientes."""
        if not self.lista_clientes:
            return "No hay clientes registrados."
        
        informacion = "─" * 60 + "\n"
        informacion += "CLIENTES DEL RESTAURANTE\n"
        informacion += "─" * 60 + "\n"
        
        for cliente in self.lista_clientes:
            informacion += str(cliente) + "\n"
        
        informacion += "─" * 60
        return informacion
    
    # Métodos de información general
    
    def mostrar_resumen_general(self) -> str:
        """Retorna un resumen general de la información del restaurante."""
        productos_disponibles = len(self.obtener_productos_disponibles())
        clientes_activos = len(self.obtener_clientes_activos())
        
        resumen = "\n" + "═" * 60 + "\n"
        resumen += f"RESUMEN GENERAL - {self.nombre_restaurante.upper()}\n"
        resumen += "═" * 60 + "\n"
        resumen += f"Total de productos: {self.obtener_total_productos()}\n"
        resumen += f"Productos disponibles: {productos_disponibles}\n"
        resumen += f"Total de clientes: {self.obtener_total_clientes()}\n"
        resumen += f"Clientes activos: {clientes_activos}\n"
        resumen += "═" * 60 + "\n"
        
        return resumen
    
    def mostrar_informacion_completa(self) -> None:
        """Muestra toda la información del restaurante en consola."""
        print(self.mostrar_resumen_general())
        print(self.mostrar_productos())
        print()
        print(self.mostrar_clientes())

