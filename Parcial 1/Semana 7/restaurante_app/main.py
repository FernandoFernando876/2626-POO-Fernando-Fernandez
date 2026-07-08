"""
main.py - Punto de entrada del Sistema de Restaurante
Descripción: Este archivo contiene el menú interactivo y la lógica principal
del sistema. Permite al usuario crear objetos Producto y Cliente desde la consola,
registrarlos en el servicio Restaurante, listarlos y buscarlos.

Flujo del programa:
    input() del usuario
        ↓
    constructor del modelo (Producto o Cliente)
        ↓
    creación del objeto
        ↓
    registro en la clase Restaurante
        ↓
    listado o búsqueda del registro
"""

from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente


# Variable global para el restaurante
restaurante = Restaurante("La Buena Mesa")


# ==================== FUNCIONES PARA PRODUCTOS ====================

def registrar_producto():
    """
    Función que permite al usuario registrar un nuevo producto.
    Utiliza input() para obtener datos del usuario y crea un objeto Producto.
    """
    print("\n" + "="*50)
    print("➕ REGISTRAR NUEVO PRODUCTO")
    print("="*50)

    try:
        nombre = input("Ingrese el nombre del producto: ").strip()
        categoria = input("Ingrese la categoría (Bebida, Platillo, Postre, etc.): ").strip()

        while True:
            try:
                precio_str = input("Ingrese el precio del producto ($): ")
                precio = float(precio_str)
                break
            except ValueError:
                print("❌ Error: Ingrese un número válido.")

        # Constructor tradicional __init__ - crea el objeto Producto
        nuevo_producto = Producto(
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            disponible=True
        )

        # Registra el producto en el servicio Restaurante
        restaurante.registrar_producto(nuevo_producto)
        print(nuevo_producto.mostrar_informacion())

    except ValueError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def listar_productos():
    """Función que lista todos los productos registrados."""
    restaurante.listar_productos()


def buscar_producto():
    """Función que permite buscar un producto."""
    print("\n" + "="*50)
    print("🔍 BUSCAR PRODUCTO")
    print("="*50)
    print("1. Buscar por nombre")
    print("2. Buscar por categoría")
    print("3. Volver")

    opcion = input("\nSeleccione una opción: ").strip()

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto a buscar: ").strip()
        restaurante.buscar_producto_por_nombre(nombre)
    elif opcion == "2":
        categoria = input("Ingrese la categoría a buscar: ").strip()
        restaurante.buscar_producto_por_categoria(categoria)
    elif opcion == "3":
        return
    else:
        print("❌ Opción no válida.")


# ==================== FUNCIONES PARA CLIENTES ====================

def registrar_cliente():
    """
    Función que permite al usuario registrar un nuevo cliente.
    Utiliza input() para obtener datos del usuario y crea un objeto Cliente con @dataclass.
    """
    print("\n" + "="*50)
    print("➕ REGISTRAR NUEVO CLIENTE")
    print("="*50)

    try:
        id_cliente = input("Ingrese el ID del cliente: ").strip()
        nombre = input("Ingrese el nombre del cliente: ").strip()
        correo = input("Ingrese el correo del cliente: ").strip()

        # Decorador @dataclass - crea automáticamente __init__, __repr__, etc.
        nuevo_cliente = Cliente(
            id_cliente=id_cliente,
            nombre=nombre,
            correo=correo
        )

        # Registra el cliente en el servicio Restaurante
        restaurante.registrar_cliente(nuevo_cliente)
        print(nuevo_cliente.mostrar_informacion())

    except Exception as e:
        print(f"❌ Error: {e}")


def listar_clientes():
    """Función que lista todos los clientes registrados."""
    restaurante.listar_clientes()


def buscar_cliente():
    """Función que permite buscar un cliente."""
    print("\n" + "="*50)
    print("🔍 BUSCAR CLIENTE")
    print("="*50)
    print("1. Buscar por nombre")
    print("2. Buscar por ID")
    print("3. Volver")

    opcion = input("\nSeleccione una opción: ").strip()

    if opcion == "1":
        nombre = input("Ingrese el nombre del cliente a buscar: ").strip()
        restaurante.buscar_cliente_por_nombre(nombre)
    elif opcion == "2":
        id_cliente = input("Ingrese el ID del cliente a buscar: ").strip()
        restaurante.buscar_cliente_por_id(id_cliente)
    elif opcion == "3":
        return
    else:
        print("❌ Opción no válida.")


# ==================== DATOS DE EJEMPLO (DIDÁCTICOS) ====================

def cargar_datos_ejemplo():
    """
    Carga datos de ejemplo para hacer el sistema didáctico.

    Estos datos permiten al usuario ver inmediatamente cómo funciona
    el sistema sin necesidad de registrar productos y clientes manualmente.

    NOTA IMPORTANTE: En un sistema real, estos datos vendrían de una base de datos.
    En esta actividad educativa, se cargan al iniciar para demostrar funcionalidad.
    """
    print("\n" + "="*50)
    print("📚 CARGANDO DATOS DE EJEMPLO (DIDÁCTICOS)")
    print("="*50 + "\n")

    # Crear productos de ejemplo usando el constructor __init__
    productos_ejemplo = [
        Producto(nombre="Hamburguesa Clásica", categoria="Platillo", precio=8.50),
        Producto(nombre="Pizza Margherita", categoria="Platillo", precio=12.00),
        Producto(nombre="Ensalada César", categoria="Platillo", precio=9.99),
        Producto(nombre="Coca-Cola", categoria="Bebida", precio=2.50),
        Producto(nombre="Jugo Natural", categoria="Bebida", precio=3.50),
        Producto(nombre="Flan Casero", categoria="Postre", precio=4.00),
        Producto(nombre="Brownie Chocolatero", categoria="Postre", precio=5.50),
    ]

    # Registrar productos en el restaurante
    for producto in productos_ejemplo:
        restaurante.registrar_producto(producto)

    print()

    # Crear clientes de ejemplo usando @dataclass
    clientes_ejemplo = [
        Cliente(id_cliente="C001", nombre="Juan García", correo="juan.garcia@email.com"),
        Cliente(id_cliente="C002", nombre="María López", correo="maria.lopez@email.com"),
        Cliente(id_cliente="C003", nombre="Carlos Rodríguez", correo="carlos.rodriguez@email.com"),
        Cliente(id_cliente="C004", nombre="Ana Martínez", correo="ana.martinez@email.com"),
    ]

    # Registrar clientes en el restaurante
    for cliente in clientes_ejemplo:
        restaurante.registrar_cliente(cliente)

    print("\n✅ Datos de ejemplo cargados exitosamente.\n")


# ==================== MENÚ INTERACTIVO ====================

def mostrar_menu():
    """Muestra el menú principal del sistema."""
    print("\n" + "="*50)
    print("        🏪 SISTEMA DE RESTAURANTE")
    print("="*50)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("─" * 50)
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("─" * 50)
    print("0. Ver resumen del restaurante")
    print("7. Salir")
    print("="*50)


def ejecutar_menu():
    """
    Función principal que ejecuta el menú interactivo.
    El programa se mantiene en ejecución hasta que el usuario seleccione salir.
    """
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            registrar_cliente()
        elif opcion == "5":
            listar_clientes()
        elif opcion == "6":
            buscar_cliente()
        elif opcion == "0":
            restaurante.mostrar_resumen()
        elif opcion == "7":
            print("\n" + "="*50)
            print("👋 ¡Gracias por usar el Sistema de Restaurante!")
            print("="*50 + "\n")
            break
        else:
            print("\n❌ Opción no válida. Por favor, intente de nuevo.")


# ==================== PUNTO DE ENTRADA ====================

if __name__ == "__main__":
    """
    Punto de entrada del programa.
    
    Flujo:
    1. Mostrar bienvenida
    2. Cargar datos de ejemplo (didácticos)
    3. Ejecutar menú interactivo
    """
    print("\n" + "="*50)
    print("🎉 BIENVENIDO AL SISTEMA DE RESTAURANTE")
    print("="*50)
    print("\nEste sistema demuestra:")
    print("✓ Constructores tradicionales (__init__)")
    print("✓ Decoradores @property y @setter")
    print("✓ Decorador @dataclass")
    print("✓ Arquitectura modular por capas")
    print("✓ Entrada de datos desde consola (input)")
    print("✓ Creación de objetos a partir de datos")
    print("✓ Almacenamiento en listas de servicio")
    print("✓ Búsqueda y listado de registros")

    # Cargar datos de ejemplo para hacer el sistema didáctico
    cargar_datos_ejemplo()

    # Ejecutar el menú interactivo
    ejecutar_menu()

