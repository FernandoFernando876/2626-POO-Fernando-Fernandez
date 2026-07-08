"""
Módulo restaurante.py - Contiene la clase Restaurante (servicio)
Descripción: Define la clase Restaurante que administra las listas de
productos y clientes, proporcionando métodos para registrar, listar y buscar.
"""

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase de servicio que administra productos y clientes del restaurante.

    Responsabilidades:
    - Mantener listas de productos y clientes
    - Registrar nuevos productos y clientes
    - Listar todos los productos y clientes
    - Buscar productos y clientes por diferentes criterios

    Atributos:
    - _productos (list): Lista de objetos Producto
    - _clientes (list): Lista de objetos Cliente
    - _nombre (str): Nombre del restaurante
    """

    def __init__(self, nombre="Mi Restaurante"):
        """
        Constructor del Restaurante.

        Args:
            nombre (str): Nombre del restaurante (por defecto "Mi Restaurante")
        """
        self._nombre = nombre
        self._productos = []
        self._clientes = []

    # ==================== MÉTODOS PARA PRODUCTOS ====================

    def registrar_producto(self, producto):
        """
        Registra un nuevo producto en el restaurante.

        Args:
            producto (Producto): Objeto de tipo Producto a registrar

        Returns:
            bool: True si el registro fue exitoso, False en caso contrario
        """
        if not isinstance(producto, Producto):
            print("❌ Error: El objeto debe ser de tipo Producto.")
            return False

        # Verificar que el producto no esté duplicado
        for prod in self._productos:
            if prod.nombre.lower() == producto.nombre.lower():
                print(f"⚠️ Advertencia: El producto '{producto.nombre}' ya está registrado.")
                return False

        self._productos.append(producto)
        print(f"✅ Producto '{producto.nombre}' registrado exitosamente.")
        return True

    def listar_productos(self):
        """
        Lista todos los productos registrados en el restaurante.

        Returns:
            list: Lista de objetos Producto
        """
        if not self._productos:
            print("\n⚠️ No hay productos registrados.")
            return []

        print(f"\n{'='*50}")
        print(f"📦 LISTADO DE PRODUCTOS ({len(self._productos)} registrados)")
        print(f"{'='*50}")
        for i, producto in enumerate(self._productos, 1):
            print(f"{i}. {producto}")
        print(f"{'='*50}\n")

        return self._productos

    def buscar_producto_por_nombre(self, nombre):
        """
        Busca un producto por su nombre.

        Args:
            nombre (str): Nombre del producto a buscar

        Returns:
            list: Lista de productos encontrados
        """
        productos_encontrados = [
            prod for prod in self._productos
            if nombre.lower() in prod.nombre.lower()
        ]

        if not productos_encontrados:
            print(f"\n❌ No se encontraron productos con el nombre '{nombre}'.")
            return []

        print(f"\n{'='*50}")
        print(f"🔍 BÚSQUEDA DE PRODUCTOS - '{nombre}'")
        print(f"{'='*50}")
        for i, producto in enumerate(productos_encontrados, 1):
            print(f"{i}. {producto}")
        print(f"{'='*50}\n")

        return productos_encontrados

    def buscar_producto_por_categoria(self, categoria):
        """
        Busca productos por categoría.

        Args:
            categoria (str): Categoría a buscar

        Returns:
            list: Lista de productos encontrados
        """
        productos_encontrados = [
            prod for prod in self._productos
            if categoria.lower() in prod.categoria.lower()
        ]

        if not productos_encontrados:
            print(f"\n❌ No se encontraron productos en la categoría '{categoria}'.")
            return []

        print(f"\n{'='*50}")
        print(f"🔍 BÚSQUEDA POR CATEGORÍA - '{categoria}'")
        print(f"{'='*50}")
        for i, producto in enumerate(productos_encontrados, 1):
            print(f"{i}. {producto}")
        print(f"{'='*50}\n")

        return productos_encontrados

    def obtener_cantidad_productos(self):
        """Obtiene la cantidad total de productos registrados."""
        return len(self._productos)

    # ==================== MÉTODOS PARA CLIENTES ====================

    def registrar_cliente(self, cliente):
        """
        Registra un nuevo cliente en el restaurante.

        Args:
            cliente (Cliente): Objeto de tipo Cliente a registrar

        Returns:
            bool: True si el registro fue exitoso, False en caso contrario
        """
        if not isinstance(cliente, Cliente):
            print("❌ Error: El objeto debe ser de tipo Cliente.")
            return False

        # Verificar que el cliente no esté duplicado por ID
        for cli in self._clientes:
            if cli.id_cliente == cliente.id_cliente:
                print(f"⚠️ Advertencia: El cliente con ID '{cliente.id_cliente}' ya está registrado.")
                return False

        self._clientes.append(cliente)
        print(f"✅ Cliente '{cliente.nombre}' registrado exitosamente.")
        return True

    def listar_clientes(self):
        """
        Lista todos los clientes registrados en el restaurante.

        Returns:
            list: Lista de objetos Cliente
        """
        if not self._clientes:
            print("\n⚠️ No hay clientes registrados.")
            return []

        print(f"\n{'='*50}")
        print(f"👥 LISTADO DE CLIENTES ({len(self._clientes)} registrados)")
        print(f"{'='*50}")
        for i, cliente in enumerate(self._clientes, 1):
            print(f"{i}. {cliente}")
        print(f"{'='*50}\n")

        return self._clientes

    def buscar_cliente_por_nombre(self, nombre):
        """
        Busca un cliente por su nombre.

        Args:
            nombre (str): Nombre del cliente a buscar

        Returns:
            list: Lista de clientes encontrados
        """
        clientes_encontrados = [
            cli for cli in self._clientes
            if nombre.lower() in cli.nombre.lower()
        ]

        if not clientes_encontrados:
            print(f"\n❌ No se encontraron clientes con el nombre '{nombre}'.")
            return []

        print(f"\n{'='*50}")
        print(f"🔍 BÚSQUEDA DE CLIENTES - '{nombre}'")
        print(f"{'='*50}")
        for i, cliente in enumerate(clientes_encontrados, 1):
            print(f"{i}. {cliente}")
        print(f"{'='*50}\n")

        return clientes_encontrados

    def buscar_cliente_por_id(self, id_cliente):
        """
        Busca un cliente por su ID.

        Args:
            id_cliente (str): ID del cliente a buscar

        Returns:
            Cliente: Objeto Cliente encontrado, None en caso contrario
        """
        for cliente in self._clientes:
            if cliente.id_cliente == id_cliente:
                print(f"\n{'='*50}")
                print(f"🔍 BÚSQUEDA POR ID - '{id_cliente}'")
                print(f"{'='*50}")
                print(cliente)
                print(f"{'='*50}\n")
                return cliente

        print(f"\n❌ No se encontró cliente con ID '{id_cliente}'.")
        return None

    def obtener_cantidad_clientes(self):
        """Obtiene la cantidad total de clientes registrados."""
        return len(self._clientes)

    # ==================== MÉTODOS GENERALES ====================

    def mostrar_resumen(self):
        """Muestra un resumen del estado del restaurante."""
        print(f"\n{'='*50}")
        print(f"🏪 RESUMEN DEL RESTAURANTE - {self._nombre}")
        print(f"{'='*50}")
        print(f"📦 Productos registrados: {self.obtener_cantidad_productos()}")
        print(f"👥 Clientes registrados:  {self.obtener_cantidad_clientes()}")
        print(f"{'='*50}\n")

