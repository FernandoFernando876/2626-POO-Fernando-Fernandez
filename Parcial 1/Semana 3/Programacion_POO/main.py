# ========================================
# PROGRAMA PRINCIPAL - PROGRAMACIÓN ORIENTADA A OBJETOS
# ========================================

from mascota import Mascota


def main():
    """
    Función principal del programa.
    Crea objetos de la clase Mascota y ejecuta sus métodos.
    """

    print("\n" + "="*50)
    print("SISTEMA DE MASCOTAS - POO")
    print("="*50)

    # Crear primer objeto de la clase Mascota
    print("\n[Creando Objeto 1]")
    mascota1 = Mascota("Max", "perro", 5)
    print(f"✓ Objeto creado: mascota1 = Mascota('Max', 'perro', 5)")

    # Crear segundo objeto de la clase Mascota
    print("\n[Creando Objeto 2]")
    mascota2 = Mascota("Whiskers", "gato", 3)
    print(f"✓ Objeto creado: mascota2 = Mascota('Whiskers', 'gato', 3)")

    # Ejecutar métodos del primer objeto
    print("\n" + "="*50)
    print("EJECUCIÓN DE MÉTODOS - OBJETO 1")
    print("="*50)
    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()

    # Ejecutar métodos del segundo objeto
    print("\n" + "="*50)
    print("EJECUCIÓN DE MÉTODOS - OBJETO 2")
    print("="*50)
    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()

    # Resumen de conceptos POO
    print("\n" + "="*50)
    print("CONCEPTOS DE POO DEMOSTRADOS")
    print("="*50)
    print("✓ Clase: Mascota")
    print("✓ Objetos: mascota1, mascota2")
    print("✓ Atributos: nombre, especie, edad")
    print("✓ Métodos: mostrar_informacion(), hacer_sonido()")
    print("✓ Abstracción: Comportamiento encapsulado en la clase")
    print("="*50 + "\n")


if __name__ == "__main__":
    main()
