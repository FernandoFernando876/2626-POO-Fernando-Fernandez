from __future__ import annotations

import re
from typing import Callable, Dict

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante

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


def registrar_producto(rest: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\nRegistro de producto:")
    codigo = solicitar_input("Código: ")
    nombre = solicitar_input("Nombre: ")
    categoria = solicitar_input("Categoría: ")

    try:
        precio = float(solicitar_input("Precio: "))
    except ValueError:
        print("Precio inválido. Registro cancelado.")
        return

    try:
        producto = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)
    except ValueError as exc:
        print(f"Datos del producto inválidos: {exc}")
        return

    if rest.registrar_producto(producto):
        archivo_servicio.guardar_productos(rest.obtener_productos())
        print("Producto registrado correctamente.")
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
    for indice, info in enumerate(productos, start=1):
        print(f"{indice}. {info}")


def buscar_producto(rest: Restaurante) -> None:
    codigo = solicitar_input("Código del producto a buscar: ")
    if not codigo:
        print("Código vacío.")
        return
    producto = rest.buscar_producto(codigo)
    if producto is None:
        print("Producto no encontrado.")
    else:
        print("Producto encontrado:")
        print(producto.mostrar_informacion())


def actualizar_producto(rest: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    codigo = solicitar_input("Código del producto a actualizar: ")
    if not codigo:
        print("Código vacío.")
        return

    producto = rest.obtener_producto(codigo)
    if producto is None:
        print("Producto no encontrado.")
        return

    print("Dejar en blanco para mantener el valor actual.")
    nombre = solicitar_input(f"Nuevo nombre [{producto.nombre}]: ")
    categoria = solicitar_input(f"Nueva categoría [{producto.categoria}]: ")
    precio_input = solicitar_input(f"Nuevo precio [{producto.precio}]: ")

    precio = None
    if precio_input:
        try:
            precio = float(precio_input)
        except ValueError:
            print("Precio inválido. Actualización cancelada.")
            return

    try:
        actualizado = rest.actualizar_producto(
            codigo,
            nombre=nombre or None,
            categoria=categoria or None,
            precio=precio,
        )
    except ValueError as exc:
        print(f"No se pudo actualizar el producto: {exc}")
        return

    if actualizado:
        archivo_servicio.guardar_productos(rest.obtener_productos())
        print("Producto actualizado correctamente.")
    else:
        print("No se pudo actualizar el producto.")


def eliminar_producto(rest: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    codigo = solicitar_input("Código del producto a eliminar: ")
    if not codigo:
        print("Código vacío.")
        return

    confirmado = solicitar_input("Confirma eliminación? (s/n): ")
    if confirmado.lower() != "s":
        print("Eliminación cancelada.")
        return

    if rest.eliminar_producto(codigo):
        archivo_servicio.guardar_productos(rest.obtener_productos())
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado. No se eliminó.")


def eliminar_usuario(rest: Restaurante) -> None:
    identificacion = solicitar_input("Identificación del usuario a eliminar: ")
    if not identificacion:
        print("Identificación vacía.")
        return

    confirmado = solicitar_input("Confirma eliminación del usuario? (s/n): ")
    if confirmado.lower() != "s":
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
    for indice, info in enumerate(usuarios, start=1):
        print(f"{indice}. {info}")


def mostrar_categorias(rest: Restaurante) -> None:
    categorias = rest.obtener_categorias_unicas()
    if not categorias:
        print("No hay categorías registradas.")
        return
    print("Categorías disponibles (sin duplicados):")
    for categoria in sorted(categorias):
        print(f"- {categoria}")


def main() -> None:
    archivo_servicio = ArchivoServicio()
    productos_iniciales = archivo_servicio.cargar_productos()
    rest = Restaurante(productos=productos_iniciales)

    menu_actions: Dict[str, Callable[[Restaurante, ArchivoServicio], None]] = {
        "1": lambda r, a: registrar_producto(r, a),
        "2": lambda r, a: buscar_producto(r),
        "3": lambda r, a: actualizar_producto(r, a),
        "4": lambda r, a: eliminar_producto(r, a),
        "5": lambda r, a: listar_productos(r),
        "6": lambda r, a: registrar_usuario(r),
        "7": lambda r, a: eliminar_usuario(r),
        "8": lambda r, a: listar_usuarios(r),
        "9": lambda r, a: mostrar_categorias(r),
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
                accion(rest, archivo_servicio)
            except Exception as exc:
                print(f"Ocurrió un error al procesar la opción: {exc}")
        else:
            print("Opción inválida. Intente de nuevo.")
        print("\n")


if __name__ == "__main__":
    main()

