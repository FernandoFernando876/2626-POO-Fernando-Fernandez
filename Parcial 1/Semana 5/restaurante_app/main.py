# Módulo: main.py
# Descripción: Punto de arranque del sistema de gestión de restaurante
# Aquí se crean instancias de productos y clientes, se agregan al restaurante y se muestra la información

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():
    """Función principal que ejecuta el sistema de gestión del restaurante."""

    print("\n" + "=" * 60)
    print("SISTEMA DE GESTIÓN DE RESTAURANTE - POO")
    print("=" * 60 + "\n")

    # ─────────────────────────────────────────────────────────
    # PASO 1: Crear instancia del restaurante
    # ─────────────────────────────────────────────────────────

    restaurante = Restaurante("La Cocina de Don Fernando")
    print(f"✓ Restaurante creado: {restaurante.nombre_restaurante}\n")

    # ─────────────────────────────────────────────────────────
    # PASO 2: Crear objetos de tipo Producto
    # ─────────────────────────────────────────────────────────

    print("Creando productos...\n")

    # Producto 1
    producto1 = Producto(
        id_producto=1,
        nombre="Pasta Carbonara",
        descripcion="Pasta fresca con salsa cremosa de huevo y tocino",
        precio=12.99,
        disponible=True
    )

    # Producto 2
    producto2 = Producto(
        id_producto=2,
        nombre="Pizza Margherita",
        descripcion="Pizza clásica con tomate, mozzarella fresca y albahaca",
        precio=11.50,
        disponible=True
    )

    # Producto 3
    producto3 = Producto(
        id_producto=3,
        nombre="Ensalada César",
        descripcion="Ensalada fresca con croutons caseros y queso parmesano",
        precio=8.99,
        disponible=False
    )

    # Producto 4
    producto4 = Producto(
        id_producto=4,
        nombre="Salmón a la Mantequilla",
        descripcion="Filete de salmón fresco con salsa de mantequilla y limón",
        precio=18.99,
        disponible=True
    )

    print(f"✓ {4} productos creados exitosamente\n")

    # ─────────────────────────────────────────────────────────
    # PASO 3: Agregar productos al restaurante
    # ─────────────────────────────────────────────────────────

    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)
    restaurante.agregar_producto(producto3)
    restaurante.agregar_producto(producto4)

    # ─────────────────────────────────────────────────────────
    # PASO 4: Crear objetos de tipo Cliente
    # ─────────────────────────────────────────────────────────

    print("Creando clientes...\n")

    # Cliente 1
    cliente1 = Cliente(
        id_cliente=1,
        nombre_completo="Juan García López",
        email="juan.garcia@email.com",
        telefono="+34 612 345 678",
        activo=True
    )

    # Cliente 2
    cliente2 = Cliente(
        id_cliente=2,
        nombre_completo="María Rodríguez Martínez",
        email="maria.rodriguez@email.com",
        telefono="+34 613 456 789",
        activo=True
    )

    # Cliente 3
    cliente3 = Cliente(
        id_cliente=3,
        nombre_completo="Carlos Fernández Ruiz",
        email="carlos.fernandez@email.com",
        telefono="+34 614 567 890",
        activo=False
    )

    # Cliente 4
    cliente4 = Cliente(
        id_cliente=4,
        nombre_completo="Ana Martínez Sánchez",
        email="ana.martinez@email.com",
        telefono="+34 615 678 901",
        activo=True
    )

    print(f"✓ {4} clientes creados exitosamente\n")

    # ─────────────────────────────────────────────────────────
    # PASO 5: Agregar clientes al restaurante
    # ─────────────────────────────────────────────────────────

    restaurante.agregar_cliente(cliente1)
    restaurante.agregar_cliente(cliente2)
    restaurante.agregar_cliente(cliente3)
    restaurante.agregar_cliente(cliente4)

    # ─────────────────────────────────────────────────────────
    # PASO 6: Mostrar información completa del restaurante
    # ─────────────────────────────────────────────────────────

    restaurante.mostrar_informacion_completa()

    # ─────────────────────────────────────────────────────────
    # PASO 7: Realizar algunas operaciones adicionales
    # ─────────────────────────────────────────────────────────

    print("\n" + "─" * 60)
    print("DEMOSTRACIONES DE FUNCIONALIDADES")
    print("─" * 60 + "\n")

    # Cambiar disponibilidad de un producto
    print("✓ Cambiando disponibilidad de 'Ensalada César'...")
    producto3.cambiar_disponibilidad(True)
    print(f"  Nuevo estado: {producto3.obtener_disponibilidad()}\n")

    # Cambiar estado de un cliente
    print("✓ Desactivando al cliente 'Carlos Fernández Ruiz'...")
    cliente3.cambiar_estado(False)
    print(f"  Nuevo estado: {cliente3.obtener_estado()}\n")

    # Mostrar productos disponibles
    print("─" * 60)
    print("PRODUCTOS DISPONIBLES DESPUÉS DE LOS CAMBIOS:")
    print("─" * 60 + "\n")
    productos_disponibles = restaurante.obtener_productos_disponibles()
    for producto in productos_disponibles:
        print(f"  • {producto.nombre} - {producto.obtener_informacion_precio()}")

    print("\n" + "─" * 60)
    print("CLIENTES ACTIVOS DESPUÉS DE LOS CAMBIOS:")
    print("─" * 60 + "\n")
    clientes_activos = restaurante.obtener_clientes_activos()
    for cliente in clientes_activos:
        print(f"  • {cliente.nombre_completo} ({cliente.obtener_estado()})")

    print("\n" + "=" * 60)
    print("FIN DEL PROGRAMA")
    print("=" * 60 + "\n")


# Verificar que este sea el módulo principal y ejecutar la función main
if __name__ == "__main__":
    main()

