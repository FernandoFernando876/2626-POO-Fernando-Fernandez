# Módulo: main.py
# Descripción: Punto de arranque del programa. Demuestra herencia, encapsulación y polimorfismo.

from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

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
    print("\n--- Demostracion de Polimorfismo ---")
    print("Recorriendo la lista de productos y llamando a mostrar_informacion()...")
    mi_restaurante.mostrar_menu()

    # 6. Demostración de Encapsulación y Validación de Precios
    print("--- Demostracion de Encapsulacion y Validacion ---")
    print(f"Producto seleccionado: {platillo1.nombre}")
    
    # Intento de acceso directo al atributo privado __precio (debe fallar o no ser accesible directamente)
    print("\nIntentando acceder directamente a platillo1.__precio...")
    try:
        # Esto lanzará AttributeError porque __precio está encapsulado de forma privada (mangled)
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

    print("\n" + "=" * 60)
    print("FIN DE LA DEMONSTRACION")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
