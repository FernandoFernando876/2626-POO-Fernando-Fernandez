from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.usuario import Usuario
import re
from typing import Callable, Dict

# Opciones estables del sistema (tupla) — información que no cambia en tiempo de ejecución
MENU_OPTIONS = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Eliminar usuario",
    "8. Listar usuarios",
    "9. Mostrar categorías",
    "10. Salir",
)

def mostrar_menu() -> None:
    print("========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    for opcion in MENU_OPTIONS:
        print(opcion)

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

    if not codigo:
        print("Código vacío. Registro cancelado.")
        return
    if not nombre:
        print("Nombre vacío. Registro cancelado.")
        return
    if precio <= 0:
        print("El precio debe ser un número mayor que 0. Registro cancelado.")
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

    if not codigo:
        print("Código vacío. Registro cancelado.")
        return
    if not nombre:
        print("Nombre vacío. Registro cancelado.")
        return
    if precio <= 0:
        print("El precio debe ser un número mayor que 0. Registro cancelado.")
        return

    bebida = Bebida(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio, tamano=tamano, envase=envase)
    if rest.registrar_producto(bebida):
        print("Bebida registrada correctamente.")
    else:
        print(f"Ya existe un producto con el código '{codigo}'. No se registró.")

def registrar_usuario(rest: Restaurante) -> None:
    print("\nRegistro de usuario:")
    identificacion = solicitar_input("Identificación: ")
    nombre = solicitar_input("Nombre: ")
    correo = solicitar_input("Correo: ")
    if not identificacion:
        print("Identificación vacía. Registro cancelado.")
        return
    if not nombre:
        print("Nombre vacío. Registro cancelado.")
        return

    # Validación simple de correo
    correo_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(correo_pattern, correo):
        print("Correo inválido. Registro cancelado.")
        return

    usuario = Usuario(identificacion=identificacion, nombre=nombre, correo=correo)
    if rest.registrar_usuario(usuario):
        print("Usuario registrado correctamente.")
    else:
        print(f"Ya existe un usuario con la identificación '{identificacion}'. No se registró.")

def listar_productos(rest: Restaurante) -> None:
    print("\nListado de productos:")
    productos = rest.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for idx, info in enumerate(productos, start=1):
        print(f"{idx}. {info}")

def buscar_producto(rest: Restaurante) -> None:
    codigo = solicitar_input("Código del producto a buscar: ")
    if not codigo:
        print("Código vacío.")
        return
    p = rest.buscar_producto(codigo)
    if p is None:
        print("Producto no encontrado.")
    else:
        print("Producto encontrado:")
        print(p.mostrar_informacion())

def actualizar_producto(rest: Restaurante) -> None:
    codigo = solicitar_input("Código del producto a actualizar: ")
    if not codigo:
        print("Código vacío.")
        return
    p = rest.obtener_producto(codigo)
    if p is None:
        print("Producto no encontrado.")
        return
    print("Dejar en blanco para mantener el valor actual.")
    nombre = solicitar_input(f"Nuevo nombre [{p.nombre}]: ")
    categoria = solicitar_input(f"Nueva categoría [{p.categoria}]: ")
    precio_input = solicitar_input(f"Nuevo precio [{p.precio}]: ")
    precio = None
    if precio_input:
        try:
            precio = float(precio_input)
            if precio <= 0:
                print("Precio debe ser mayor que 0. Actualización cancelada.")
                return
        except ValueError:
            print("Precio inválido. Actualización cancelada.")
            return
    if rest.actualizar_producto(codigo, nombre=nombre or None, categoria=categoria or None, precio=precio):
        print("Producto actualizado correctamente.")
    else:
        print("No se pudo actualizar el producto.")

def eliminar_producto(rest: Restaurante) -> None:
    codigo = solicitar_input("Código del producto a eliminar: ")
    if not codigo:
        print("Código vacío.")
        return
    confirmado = solicitar_input("Confirma eliminación? (s/n): ")
    if confirmado.lower() != 's':
        print("Eliminación cancelada.")
        return
    if rest.eliminar_producto(codigo):
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado. No se eliminó.")

def eliminar_usuario(rest: Restaurante) -> None:
    identificacion = solicitar_input("Identificación del usuario a eliminar: ")
    if not identificacion:
        print("Identificación vacía.")
        return
    confirmado = solicitar_input("Confirma eliminación del usuario? (s/n): ")
    if confirmado.lower() != 's':
        print("Eliminación cancelada.")
        return
    if rest.eliminar_usuario(identificacion):
        print("Usuario eliminado correctamente.")
    else:
        print("Usuario no encontrado. No se eliminó.")

def listar_usuarios(rest: Restaurante) -> None:
    print("\nListado de usuarios:")
    usuarios = rest.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for idx, info in enumerate(usuarios, start=1):
        print(f"{idx}. {info}")

def mostrar_categorias(rest: Restaurante) -> None:
    categorias = rest.obtener_categorias_unicas()
    if not categorias:
        print("No hay categorías registradas.")
        return
    print("Categorías disponibles (sin duplicados):")
    for c in sorted(categorias):
        print(f"- {c}")

def main() -> None:
    rest = Restaurante()

    # Diccionario que asocia la opción (clave) con la función a ejecutar (valor)
    menu_actions: Dict[str, Callable[[Restaurante], None]] = {
        "1": lambda r: registrar_producto(r),
        "2": lambda r: buscar_producto(r),
        "3": lambda r: actualizar_producto(r),
        "4": lambda r: eliminar_producto(r),
        "5": lambda r: listar_productos(r),
        "6": lambda r: registrar_usuario(r),
        "7": lambda r: eliminar_usuario(r),
        "8": lambda r: listar_usuarios(r),
        "9": lambda r: mostrar_categorias(r),
    }

    while True:
        mostrar_menu()
        opcion = solicitar_input("Seleccione una opción: ")
        if opcion == "10":
            print("Saliendo... ¡hasta luego!")
            break
        accion = menu_actions.get(opcion)
        if accion:
            try:
                accion(rest)
            except Exception as e:
                print(f"Ocurrió un error al procesar la opción: {e}")
        else:
            print("Opción inválida. Intente de nuevo.")
        print("\n")  # separación entre iteraciones

if __name__ == "__main__":
    main()


