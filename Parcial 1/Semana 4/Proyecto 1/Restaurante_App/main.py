# Punto de entrada del sistema de gestión de restaurante
# Autor: Fernando Fernández
# Importamos las clases necesarias desde los módulos correspondientes

from Modelos_.Productos import Producto
from Modelos_.Clientes import Cliente
from Servicios_.Restaurante import Restaurante


def main():
    """
    Función principal que demuestra el funcionamiento del sistema
    de gestión de restaurante.
    """

    # 1. Crear una instancia del restaurante
    print("\n" + "="*60)
    print("SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("="*60)

    restaurante = Restaurante("Mi Restaurante Favorito")
    print(f"\n✓ Restaurante creado: {restaurante.nombre}\n")

    # 2. Crear productos (platos y bebidas)
    print("Creando productos...")
    producto1 = Producto(1, "Pasta Carbonara", "Pasta con salsa cremosa de huevo y tocino", 12.99)
    producto2 = Producto(2, "Pizza Margherita", "Pizza clásica con tomate, mozzarella y albahaca", 11.50)
    producto3 = Producto(3, "Ensalada César", "Ensalada fresca con croutons y parmesano", 8.99)
    producto4 = Producto(4, "Filete de Salmón", "Salmón a la mantequilla con limón y vegetales", 18.99)
    producto5 = Producto(5, "Café Americano", "Café negro recién preparado", 2.50)

    # Agregar productos al restaurante
    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)
    restaurante.agregar_producto(producto3)
    restaurante.agregar_producto(producto4)
    restaurante.agregar_producto(producto5)

    print("✓ 5 productos agregados al restaurante\n")

    # 3. Crear clientes
    print("Creando clientes...")
    cliente1 = Cliente(1, "Juan García", "juan.garcia@email.com", "+34 612 345 678")
    cliente2 = Cliente(2, "María López", "maria.lopez@email.com", "+34 613 456 789")
    cliente3 = Cliente(3, "Carlos Rodríguez", "carlos.rodriguez@email.com", "+34 614 567 890")
    cliente4 = Cliente(4, "Ana Martínez", "ana.martinez@email.com", "+34 615 678 901")

    # Agregar clientes al restaurante
    restaurante.agregar_cliente(cliente1)
    restaurante.agregar_cliente(cliente2)
    restaurante.agregar_cliente(cliente3)
    restaurante.agregar_cliente(cliente4)

    print("✓ 4 clientes agregados al restaurante\n")

    # 4. Demostración de funcionalidades
    print("-" * 60)
    print("DEMOSTRACIONES DE FUNCIONALIDADES")
    print("-" * 60)

    # Registrar alguns pedidos
    cliente1.registrar_pedido()
    cliente1.registrar_pedido()
    cliente2.registrar_pedido()
    cliente3.registrar_pedido()
    cliente3.registrar_pedido()
    cliente3.registrar_pedido()

    print("\n✓ Se han registrado varios pedidos\n")

    # Cambiar disponibilidad de un producto
    print("Cambiando disponibilidad del producto 'Pasta Carbonara'...")
    producto = restaurante.obtener_producto(1)
    if producto:
        producto.cambiar_disponibilidad()
        print(f"✓ Producto actualizado: {producto.nombre} - Disponible: {producto.disponible}\n")

    # Desactivar un cliente
    print("Desactivando al cliente 'María López'...")
    cliente = restaurante.obtener_cliente(2)
    if cliente:
        cliente.desactivar_cliente()
        print(f"✓ Cliente actualizado: {cliente.nombre} - Activo: {cliente.activo}\n")

    # 5. Mostrar información completa del restaurante
    restaurante.mostrar_informacion()

    # 6. Mostrar detalles específicos
    print("\nDETALLES DE PRODUCTOS DISPONIBLES:")
    print("─" * 60)
    productos_disponibles = restaurante.listar_productos()
    for producto in productos_disponibles:
        print(f"\n  {producto}")

    print("\n\nDETALLES DE CLIENTES ACTIVOS:")
    print("─" * 60)
    clientes_activos = restaurante.listar_clientes()
    for cliente in clientes_activos:
        print(f"\n  {cliente}")

    # 7. Mostrar información de obtener_cliente usando diccionarios
    print("\n\nINFORMACIÓN DETALLADA DE UN CLIENTE:")
    print("─" * 60)
    cliente_detalle = restaurante.obtener_cliente(1)
    if cliente_detalle:
        info = cliente_detalle.obtener_informacion()
        print(f"\nDatos de {cliente_detalle.nombre}:")
        for clave, valor in info.items():
            print(f"  - {clave}: {valor}")

    print("\n" + "="*60)
    print("FIN DEL PROGRAMA")
    print("="*60 + "\n")


# Punto de entrada del programa
if __name__ == "__main__":
    main()

