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
        elif opcion == "6":
            print("Saliendo... ¡hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
        print("\n")  # separación entre iteraciones

if __name__ == "__main__":
    main()

