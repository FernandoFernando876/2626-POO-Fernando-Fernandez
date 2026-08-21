import os
import re
from typing import Callable, Dict
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.usuario import Usuario


# Configuración de rutas
RUTA_PRODUCTOS = os.path.join(os.path.dirname(__file__), "datos", "productos.json")

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
    """Muestra el menú principal del sistema."""
    print("========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    for opcion in MENU_OPTIONS:
        print(opcion)


def solicitar_input(prompt: str) -> str:
    """Solicita entrada del usuario y elimina espacios en blanco."""
    return input(prompt).strip()


def registrar_producto(rest: Restaurante, archivo: ArchivoServicio) -> None:
    """Registra un nuevo producto y lo persiste en JSON."""
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
        # Guardar en JSON después del registro exitoso
        if archivo.guardar_productos(rest.obtener_productos_copia()):
            print("Cambios guardados en la base de datos.")
        else:
            print("Advertencia: No se pudieron guardar los cambios.")
    else:
        print(f"Ya existe un producto con el código '{codigo}'. No se registró.")


def registrar_bebida(rest: Restaurante, archivo: ArchivoServicio) -> None:
    """Registra una nueva bebida y la persiste en JSON."""
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
    if not tamano or not envase:
        print("Tamaño o envase vacío. Registro cancelado.")
        return

    bebida = Bebida(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio, tamano=tamano, envase=envase)
    if rest.registrar_producto(bebida):
        print("Bebida registrada correctamente.")
        # Guardar en JSON después del registro exitoso
        if archivo.guardar_productos(rest.obtener_productos_copia()):
            print("Cambios guardados en la base de datos.")
        else:
            print("Advertencia: No se pudieron guardar los cambios.")
    else:
        print(f"Ya existe un producto con el código '{codigo}'. No se registró.")


def registrar_usuario(rest: Restaurante) -> None:
    """Registra un nuevo usuario. Los usuarios no se persisten en esta semana."""
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
    """Lista todos los productos registrados."""
    print("\nListado de productos:")
    productos = rest.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for idx, info in enumerate(productos, start=1):
        print(f"{idx}. {info}")


def buscar_producto(rest: Restaurante) -> None:
    """Busca un producto por código."""
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


def actualizar_producto(rest: Restaurante, archivo: ArchivoServicio) -> None:
    """Actualiza un producto existente y persiste los cambios en JSON."""
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
        # Guardar en JSON después de la actualización exitosa
        if archivo.guardar_productos(rest.obtener_productos_copia()):
            print("Cambios guardados en la base de datos.")
        else:
            print("Advertencia: No se pudieron guardar los cambios.")
    else:
        print("No se pudo actualizar el producto.")


def eliminar_producto(rest: Restaurante, archivo: ArchivoServicio) -> None:
    """Elimina un producto y persiste el cambio en JSON."""
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
        # Guardar en JSON después de la eliminación exitosa
        if archivo.guardar_productos(rest.obtener_productos_copia()):
            print("Cambios guardados en la base de datos.")
        else:
            print("Advertencia: No se pudieron guardar los cambios.")
    else:
        print("Producto no encontrado. No se eliminó.")


def eliminar_usuario(rest: Restaurante) -> None:
    """Elimina un usuario. Los cambios no se persisten en esta semana."""
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
    """Lista todos los usuarios registrados."""
    print("\nListado de usuarios:")
    usuarios = rest.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for idx, info in enumerate(usuarios, start=1):
        print(f"{idx}. {info}")


def mostrar_categorias(rest: Restaurante) -> None:
    """Muestra todas las categorías únicas de productos."""
    categorias = rest.obtener_categorias_unicas()
    if not categorias:
        print("No hay categorías registradas.")
        return
    print("Categorías disponibles (sin duplicados):")
    for c in sorted(categorias):
        print(f"- {c}")


def main() -> None:
    """Función principal que coordina toda la lógica del sistema."""
    # Inicializar servicios
    archivo = ArchivoServicio(RUTA_PRODUCTOS)
    rest = Restaurante()

    # Cargar productos desde JSON al iniciar
    print("Inicializando sistema...")
    productos_cargados = archivo.cargar_productos()
    rest.cargar_productos_iniciales(productos_cargados)
    print("Sistema listo.\n")

    # Diccionario que asocia la opción con la función a ejecutar
    menu_actions: Dict[str, Callable] = {
        "1": lambda: registrar_producto(rest, archivo),
        "2": lambda: buscar_producto(rest),
        "3": lambda: actualizar_producto(rest, archivo),
        "4": lambda: eliminar_producto(rest, archivo),
        "5": lambda: listar_productos(rest),
        "6": lambda: registrar_usuario(rest),
        "7": lambda: eliminar_usuario(rest),
        "8": lambda: listar_usuarios(rest),
        "9": lambda: mostrar_categorias(rest),
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
                accion()
            except Exception as e:
                print(f"Ocurrió un error al procesar la opción: {e}")
        else:
            print("Opción inválida. Intente de nuevo.")
        print("\n")  # separación entre iteraciones


if __name__ == "__main__":
    main()

