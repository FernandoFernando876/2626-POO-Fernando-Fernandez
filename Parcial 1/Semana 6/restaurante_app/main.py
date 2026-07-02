# Módulo: main.py
# Descripción: Punto de arranque del programa. Demuestra herencia, encapsulación y polimorfismo.

from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def menu_interactivo(restaurante: Restaurante):
    """Ofrece un menú interactivo en consola para gestionar el restaurante de forma dinámica."""
    while True:
        print("\n" + "=" * 60)
        print(f"        MENU INTERACTIVO - {restaurante.nombre.upper()}")
        print("=" * 60)
        print("1. Ver el menú completo")
        print("2. Ver estadísticas resumidas")
        print("3. Buscar un producto por nombre")
        print("4. Modificar el precio de un producto (Encapsulamiento)")
        print("5. Realizar un nuevo pedido (Simulación de boleta)")
        print("6. Cambiar disponibilidad de un producto")
        print("7. Salir")
        print("=" * 60)
        
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        if opcion == "1":
            restaurante.mostrar_menu()
            
        elif opcion == "2":
            stats = restaurante.obtener_estadisticas()
            print("\n" + "-" * 40)
            print("ESTADÍSTICAS DEL MENÚ")
            print("-" * 40)
            print(f"Total de productos:       {stats['total']}")
            print(f"  - Platillos (Comida):   {stats['platillos']}")
            print(f"  - Bebidas:              {stats['bebidas']}")
            print(f"Productos disponibles:    {stats['disponibles']}")
            print(f"Productos agotados:       {stats['agotados']}")
            print(f"Precio promedio:          ${stats['promedio_precio']:.2f}")
            if stats['mas_caro']:
                print(f"Producto más caro:        {stats['mas_caro'].nombre} (${stats['mas_caro'].obtener_precio():.2f})")
            if stats['mas_barato']:
                print(f"Producto más barato:      {stats['mas_barato'].nombre} (${stats['mas_barato'].obtener_precio():.2f})")
            print("-" * 40)
            
        elif opcion == "3":
            nombre = input("\nIngrese el nombre del producto a buscar: ")
            prod = restaurante.buscar_producto(nombre)
            if prod:
                print("\n[PRODUCTO ENCONTRADO]")
                print(prod.mostrar_informacion())
            else:
                print(f"\n[ERROR] No se encontró ningún producto con el nombre '{nombre}'.")
                
        elif opcion == "4":
            nombre = input("\nIngrese el nombre del producto a modificar: ")
            prod = restaurante.buscar_producto(nombre)
            if prod:
                print(f"Precio actual de '{prod.nombre}': ${prod.obtener_precio():.2f}")
                try:
                    nuevo_precio_str = input("Ingrese el nuevo precio: ").strip()
                    nuevo_precio = float(nuevo_precio_str)
                    prod.cambiar_precio(nuevo_precio)
                    print(f"[OK] Precio actualizado con éxito. Nuevo precio: ${prod.obtener_precio():.2f}")
                except ValueError as e:
                    print(f"[ERROR] No se pudo cambiar el precio: {e}")
            else:
                print(f"\n[ERROR] No se encontró ningún producto con el nombre '{nombre}'.")
                
        elif opcion == "5":
            print("\n--- Realizar Pedido Nuevo ---")
            items_a_pedir = []
            while True:
                nombre = input("Ingrese el nombre del producto (o Enter para finalizar): ").strip()
                if not nombre:
                    break
                
                prod = restaurante.buscar_producto(nombre)
                if not prod:
                    print(f"[ADVERTENCIA] '{nombre}' no está registrado en el menú. Se agregará de todas formas para verificar validación.")
                
                try:
                    cant_str = input(f"Cantidad para '{nombre}': ").strip()
                    cantidad = int(cant_str)
                    if cantidad <= 0:
                        print("[ERROR] La cantidad debe ser un número entero positivo mayor a cero.")
                        continue
                    items_a_pedir.append((nombre, cantidad))
                except ValueError:
                    print("[ERROR] Ingrese un número entero válido para la cantidad.")
            
            if items_a_pedir:
                print("\nProcesando pedido...")
                pedido = restaurante.realizar_pedido(items_a_pedir)
                restaurante.imprimir_recibo(pedido)
            else:
                print("[INFO] Pedido cancelado (no se ingresaron productos).")
                
        elif opcion == "6":
            nombre = input("\nIngrese el nombre del producto a modificar disponibilidad: ")
            prod = restaurante.buscar_producto(nombre)
            if prod:
                estado_actual = prod.obtener_estado_disponibilidad()
                print(f"Estado actual de '{prod.nombre}': {estado_actual}")
                nuevo_estado_str = input("¿Está disponible? (S/N): ").strip().upper()
                if nuevo_estado_str == "S":
                    prod.disponible = True
                    print(f"[OK] '{prod.nombre}' ahora está Disponible.")
                elif nuevo_estado_str == "N":
                    prod.disponible = False
                    print(f"[OK] '{prod.nombre}' ahora está Agotado.")
                else:
                    print("[ERROR] Opción no válida (debe ser S o N). No se realizaron cambios.")
            else:
                print(f"\n[ERROR] No se encontró ningún producto con el nombre '{nombre}'.")
                
        elif opcion == "7":
            print("\n¡Gracias por utilizar el sistema de gestión del restaurante! Saliendo...")
            break
        else:
            print("\n[ERROR] Opción no válida. Por favor, ingrese un número del 1 al 7.")


def main():
    """Función principal para inicializar y demostrar el funcionamiento del sistema."""

    print("\n" + "=" * 60)
    print("SISTEMA DE GESTION DE RESTAURANTE - SEMANA 6 POO")
    print("=" * 60 + "\n")

    # 1. Crear la instancia del servicio Restaurante
    mi_restaurante = Restaurante("El Rincon del Sabor Latino")
    print(f"[OK] Restaurante creado: {mi_restaurante.nombre}\n")

    # 2. Crear al menos dos objetos de tipo Platillo
    print("Registrando Platillos...")
    platillo1 = Platillo(
        nombre="Lomo Saltado", 
        precio=14.50, 
        tiempo_preparacion=20, 
        disponible=True
    )
    platillo2 = Platillo(
        nombre="Ceviche Mixto Especial", 
        precio=18.90, 
        tiempo_preparacion=15, 
        disponible=True
    )

    # 3. Crear al menos dos objetos de tipo Bebida
    print("\nRegistrando Bebidas...")
    bebida1 = Bebida(
        nombre="Pisco Sour Clasico", 
        precio=8.00, 
        volumen_ml=250, 
        disponible=True
    )
    bebida2 = Bebida(
        nombre="Chicha Morada Familiar", 
        precio=6.50, 
        volumen_ml=1000, 
        disponible=False
    )

    # 4. Agregar los objetos creados a la lista de Restaurante
    print("\nAgregando productos al menu del restaurante...")
    mi_restaurante.agregar_producto(platillo1)
    mi_restaurante.agregar_producto(platillo2)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_producto(bebida2)

    # 5. Mostrar la información del menú (Demostración de Polimorfismo)
    print("\n--- Demostracion de Polimorfismo (Mostrar Menú) ---")
    print("Recorriendo la lista de productos y llamando a mostrar_informacion()...")
    mi_restaurante.mostrar_menu()

    # 6. Mostrar estadísticas del menú (Nueva funcionalidad de información completa)
    print("--- Demostracion de Calculo de Estadisticas de Menu ---")
    stats = mi_restaurante.obtener_estadisticas()
    print(f"Total de ítems registrados: {stats['total']}")
    print(f"  - Platillos de Comida:    {stats['platillos']}")
    print(f"  - Bebidas del Menú:       {stats['bebidas']}")
    print(f"  - Disponibles al público: {stats['disponibles']}")
    print(f"  - Agotados temporalmente: {stats['agotados']}")
    print(f"Precio promedio del menú:   ${stats['promedio_precio']:.2f}")
    if stats['mas_caro']:
        print(f"Producto de mayor precio:  {stats['mas_caro'].nombre} (${stats['mas_caro'].obtener_precio():.2f})")
    if stats['mas_barato']:
        print(f"Producto de menor precio:  {stats['mas_barato'].nombre} (${stats['mas_barato'].obtener_precio():.2f})")
    print("-" * 60 + "\n")

    # 7. Simular Pedidos y Emisión de Comprobantes (Nueva funcionalidad de flujo de negocio)
    print("--- Demostracion de Procesamiento de Pedido y Emision de Boleta ---")
    print("Caso 1: Realizando un pedido exitoso (2x Lomo Saltado + 1x Pisco Sour)...")
    pedido_exitoso = mi_restaurante.realizar_pedido([
        ("Lomo Saltado", 2),
        ("Pisco Sour Clasico", 1)
    ])
    mi_restaurante.imprimir_recibo(pedido_exitoso)

    print("Caso 2: Realizando pedido con productos agotados o no existentes...")
    pedido_con_errores = mi_restaurante.realizar_pedido([
        ("Ceviche Mixto Especial", 1),
        ("Chicha Morada Familiar", 1),  # Agotado
        ("Tallarines Verdes", 2)        # No existe
    ])
    mi_restaurante.imprimir_recibo(pedido_con_errores)

    # 8. Demostración de Encapsulación y Validación de Precios
    print("--- Demostracion de Encapsulacion y Validacion ---")
    print(f"Producto seleccionado para pruebas de encapsulacion: {platillo1.nombre}")
    
    # Intento de acceso directo al atributo privado __precio (debe fallar)
    print("\nIntentando acceder directamente a platillo1.__precio...")
    try:
        valor_privado = platillo1.__precio
        print(f"Acceso directo: {valor_privado}")
    except AttributeError as e:
        print(f"[ERROR] Acceso directo denegado (comportamiento esperado por encapsulacion): {e}")

    # Uso correcto del método de acceso (Getter)
    print(f"[OK] Precio actual obtenido mediante getter: ${platillo1.obtener_precio():.2f}")

    # Modificación exitosa del precio usando el método de modificación (Setter)
    nuevo_precio_valido = 16.00
    print(f"\nModificando precio a un valor valido: ${nuevo_precio_valido:.2f}...")
    try:
        platillo1.cambiar_precio(nuevo_precio_valido)
        print(f"[OK] Cambio exitoso. Nuevo precio: ${platillo1.obtener_precio():.2f}")
    except ValueError as e:
        print(f"[ERROR] Error inesperado: {e}")

    # Intento de modificación inválida (precio negativo o cero) para probar la validación
    nuevo_precio_invalido = -5.50
    print(f"\nModificando precio a un valor invalido (negativo): ${nuevo_precio_invalido:.2f}...")
    try:
        platillo1.cambiar_precio(nuevo_precio_invalido)
    except ValueError as e:
        print(f"[OK] Validacion exitosa. Mensaje de error capturado:\n   {e}")

    nuevo_precio_cero = 0.0
    print(f"\nModificando precio a un valor invalido (cero): ${nuevo_precio_cero:.2f}...")
    try:
        platillo1.cambiar_precio(nuevo_precio_cero)
    except ValueError as e:
        print(f"[OK] Validacion exitosa. Mensaje de error capturado:\n   {e}")

    # Mostrar menú actualizado con el nuevo precio
    print("\n--- Comprobacion final del precio del Lomo Saltado en el Menú ---")
    info_lomo = platillo1.mostrar_informacion()
    print(info_lomo)
    print("-" * 60 + "\n")

    print("=" * 60)
    print("FIN DE LA DEMONSTRACION ESTATICA DE POO")
    print("=" * 60 + "\n")

    # Preguntar si desea ingresar al modo interactivo para probar todas las funciones
    respuesta = input("¿Desea ingresar al menú interactivo de gestión? (S/N): ").strip().upper()
    if respuesta == "S":
        menu_interactivo(mi_restaurante)
    else:
        print("\nEjecución finalizada. Que tenga un buen día.")

if __name__ == "__main__":
    main()
