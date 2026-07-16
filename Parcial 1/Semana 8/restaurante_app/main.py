from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente

def mostrar_menu() -> None:
    print("========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")
    print("7. Explicación didáctica (SOLID)\n")

def solicitar_input(prompt: str) -> str:
    return input(prompt).strip()

def registrar_producto(rest: Restaurante) -> None:
    print("\nRegistro de producto:")
    codigo = solicitar_input("Código: ")
    nombre = solicitar_input("Nombre: ")
    categoria = solicitar_input("Categoría: ")
    try:
        precio = float(solicitar_input("Precio: "))
    except ValueError:
        print("Precio inválido. Registro cancelado.")
        return

    producto = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)
    if rest.registrar_producto(producto):
        print("Producto registrado correctamente.")
    else:
        print(f"Ya existe un producto con el código '{codigo}'. No se registró.")

def registrar_bebida(rest: Restaurante) -> None:
    print("\nRegistro de bebida:")
    codigo = solicitar_input("Código: ")
    nombre = solicitar_input("Nombre: ")
    categoria = solicitar_input("Categoría: ")
    try:
        precio = float(solicitar_input("Precio: "))
    except ValueError:
        print("Precio inválido. Registro cancelado.")
        return
    tamano = solicitar_input("Tamaño (ej. 500ml): ")
    envase = solicitar_input("Envase (ej. botella, lata): ")

    bebida = Bebida(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio, tamano=tamano, envase=envase)
    if rest.registrar_producto(bebida):
        print("Bebida registrada correctamente.")
    else:
        print(f"Ya existe un producto con el código '{codigo}'. No se registró.")

def registrar_cliente(rest: Restaurante) -> None:
    print("\nRegistro de cliente:")
    identificacion = solicitar_input("Identificación: ")
    nombre = solicitar_input("Nombre: ")
    correo = solicitar_input("Correo: ")

    cliente = Cliente(identificacion=identificacion, nombre=nombre, correo=correo)
    if rest.registrar_cliente(cliente):
        print("Cliente registrado correctamente.")
    else:
        print(f"Ya existe un cliente con la identificación '{identificacion}'. No se registró.")

def listar_productos(rest: Restaurante) -> None:
    print("\nListado de productos:")
    productos = rest.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for idx, info in enumerate(productos, start=1):
        print(f"{idx}. {info}")

def listar_clientes(rest: Restaurante) -> None:
    print("\nListado de clientes:")
    clientes = rest.listar_clientes()
    if not clientes:
        print("No hay clientes registrados.")
        return
    for idx, info in enumerate(clientes, start=1):
        print(f"{idx}. {info}")

def mostrar_explicacion(rest: Restaurante) -> None:
    """
    Muestra una explicación didáctica sobre la organización del proyecto y cómo se aplican
    los principios SOLID. Además muestra ejemplos en tiempo real usando los objetos actuales.
    """
    print("\n--- Explicación didáctica y aplicación de SOLID ---")
    print("Este sistema sigue una separación clara de responsabilidades:")
    print("- Producto/Bebida: representan datos y cómo mostrarlos (método mostrar_informacion()).")
    print("- Cliente: representa datos de cliente y su presentación.")
    print("- Restaurante: servicio que administra registro y listado, sin conocer detalles internos.")
    print("- main.py: responsable únicamente de la interacción con el usuario.")

    print("\nAplicación de principios SOLID (resumen interactivo):")
    print("S - Single Responsibility: Cada clase tiene una sola responsabilidad clara.")
    print("O - Open/Closed: Restaurante opera sobre la interfaz de Producto, por tanto se puede")
    print("    extender con nuevas subclases (p.ej. Platillo) sin modificar Restaurante.")
    print("L - Liskov Substitution: Una Bebida puede usarse donde se espera un Producto.")
    print("I/D no se aplican explícitamente en este ejercicio simple, pero la estructura permite")
    print("    inyectar dependencias o separar interfaces en extensiones futuras.")

    # Ejemplos en tiempo real
    productos = rest.listar_productos()
    clientes = rest.listar_clientes()
    print(f"\nEjemplos en el estado actual: {len(productos)} productos registrados, {len(clientes)} clientes registrados.")
    if productos:
        print("Ejemplo de polimorfismo — se llama a mostrar_informacion() en cada producto sin preguntar su tipo:")
        for i, info in enumerate(productos[:3], start=1):
            print(f" {i}. {info}")
    else:
        print("No hay productos para mostrar un ejemplo de polimorfismo. Registra uno y vuelve aquí.")

    input("\nPresiona Enter para volver al menú...")

def main() -> None:
    rest = Restaurante()
    while True:
        mostrar_menu()
        opcion = solicitar_input("Seleccione una opción: ")
        if opcion == "1":
            registrar_producto(rest)
        elif opcion == "2":
            registrar_bebida(rest)
        elif opcion == "3":
            registrar_cliente(rest)
        elif opcion == "4":
            listar_productos(rest)
        elif opcion == "5":
            listar_clientes(rest)
        elif opcion == "7":
            mostrar_explicacion(rest)
        elif opcion == "6":
            print("Saliendo... ¡hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
        print("\n")  # separación entre iteraciones

if __name__ == "__main__":
    main()

