# Clase que representa el servicio principal del restaurante
class Restaurante:
    """
    Servicio que gestiona los productos y clientes del restaurante.

    Atributos:
        nombre (str): Nombre del restaurante
        productos (list): Lista de productos disponibles
        clientes (list): Lista de clientes registrados
    """

    def __init__(self, nombre):
        """
        Inicializa un nuevo restaurante.

        Args:
            nombre: Nombre del restaurante
        """
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def __str__(self):
        """Representación en texto del restaurante."""
        return f"Restaurante: {self.nombre}\nProductos: {len(self.productos)} | Clientes: {len(self.clientes)}"

    # Métodos para gestionar productos
    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al restaurante.

        Args:
            producto: Objeto Producto a agregar
        """
        self.productos.append(producto)

    def obtener_producto(self, id_producto):
        """
        Obtiene un producto por su ID.

        Args:
            id_producto: ID del producto a buscar

        Returns:
            Producto encontrado o None
        """
        for producto in self.productos:
            if producto.id == id_producto:
                return producto
        return None

    def listar_productos(self):
        """Devuelve la lista de todos los productos disponibles."""
        return [p for p in self.productos if p.disponible]

    def listar_todos_productos(self):
        """Devuelve la lista de todos los productos (disponibles e indisponibles)."""
        return self.productos

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del restaurante.

        Args:
            id_producto: ID del producto a eliminar
        """
        self.productos = [p for p in self.productos if p.id != id_producto]

    # Métodos para gestionar clientes
    def agregar_cliente(self, cliente):
        """
        Agrega un nuevo cliente al restaurante.

        Args:
            cliente: Objeto Cliente a agregar
        """
        self.clientes.append(cliente)

    def obtener_cliente(self, id_cliente):
        """
        Obtiene un cliente por su ID.

        Args:
            id_cliente: ID del cliente a buscar

        Returns:
            Cliente encontrado o None
        """
        for cliente in self.clientes:
            if cliente.id == id_cliente:
                return cliente
        return None

    def listar_clientes(self):
        """Devuelve la lista de clientes activos."""
        return [c for c in self.clientes if c.activo]

    def listar_todos_clientes(self):
        """Devuelve la lista de todos los clientes."""
        return self.clientes

    def eliminar_cliente(self, id_cliente):
        """
        Elimina un cliente del restaurante.

        Args:
            id_cliente: ID del cliente a eliminar
        """
        self.clientes = [c for c in self.clientes if c.id != id_cliente]

    # Métodos informativos
    def obtener_estadisticas(self):
        """Devuelve estadísticas del restaurante."""
        productos_disponibles = len(self.listar_productos())
        clientes_activos = len(self.listar_clientes())

        return {
            'nombre_restaurante': self.nombre,
            'total_productos': len(self.productos),
            'productos_disponibles': productos_disponibles,
            'total_clientes': len(self.clientes),
            'clientes_activos': clientes_activos
        }

    def mostrar_informacion(self):
        """Muestra información completa del restaurante."""
        print(f"\n{'='*60}")
        print(f"INFORMACIÓN DEL RESTAURANTE: {self.nombre.upper()}")
        print(f"{'='*60}")

        # Estadísticas
        stats = self.obtener_estadisticas()
        print(f"\nEstadísticas:")
        print(f"  - Total de productos: {stats['total_productos']}")
        print(f"  - Productos disponibles: {stats['productos_disponibles']}")
        print(f"  - Total de clientes: {stats['total_clientes']}")
        print(f"  - Clientes activos: {stats['clientes_activos']}")

        # Productos
        print(f"\n{'─'*60}")
        print("PRODUCTOS:")
        print(f"{'─'*60}")
        if self.productos:
            for producto in self.productos:
                print(f"  {producto}")
        else:
            print("  No hay productos registrados.")

        # Clientes
        print(f"\n{'─'*60}")
        print("CLIENTES:")
        print(f"{'─'*60}")
        if self.clientes:
            for cliente in self.clientes:
                print(f"  {cliente}")
        else:
            print("  No hay clientes registrados.")

        print(f"\n{'='*60}\n")
