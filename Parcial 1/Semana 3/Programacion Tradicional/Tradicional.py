nombre_mascota = ""
tipo_mascota = ""
edad_mascota = 0
raza_mascota = ""
peso_mascota = 0.0
color_mascota = ""

def registrar_mascota():
    global nombre_mascota, tipo_mascota, edad_mascota, raza_mascota, peso_mascota, color_mascota
    print("\n" + "="*50)
    print("REGISTRO DE MASCOTA")
    print("="*50)
    nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()
    tipo_mascota = input("Ingrese el tipo de mascota (perro, gato, etc.): ").strip()
    try:
        edad_mascota = int(input("Ingrese la edad de la mascota (años): "))
    except ValueError:
        print("Error: La edad debe ser un número entero.")
        edad_mascota = 0
    raza_mascota = input("Ingrese la raza de la mascota: ").strip()
    try:
        peso_mascota = float(input("Ingrese el peso de la mascota (kg): "))
    except ValueError:
        print("Error: El peso debe ser un número.")
        peso_mascota = 0.0

    color_mascota = input("Ingrese el color de la mascota: ").strip()
    print("\n✓ Mascota registrada exitosamente.")

def mostrar_informacion():

    if not nombre_mascota:
        print("\n✗ Error: No hay datos de mascota registrados.")
        print("Por favor, registre una mascota primero.")
        return

    print("\n" + "="*50)
    print("INFORMACIÓN DE LA MASCOTA REGISTRADA")
    print("="*50)
    print(f"Nombre:               {nombre_mascota}")
    print(f"Tipo:                 {tipo_mascota}")
    print(f"Edad:                 {edad_mascota} años")
    print(f"Raza:                 {raza_mascota}")
    print(f"Peso:                 {peso_mascota} kg")
    print(f"Color:                {color_mascota}")
    print("="*50)

def obtener_descripcion():
    if not nombre_mascota:
        print("\n✗ Error: No hay datos de mascota registrados.")
        return

    descripcion = f"{nombre_mascota} es un {tipo_mascota} de raza {raza_mascota}, "
    descripcion += f"con un color {color_mascota}, pesa {peso_mascota} kg "
    descripcion += f"y tiene {edad_mascota} años de edad."

    print("\n" + "="*50)
    print("DESCRIPCIÓN DE LA MASCOTA")
    print("="*50)
    print(descripcion)
    print("="*50)

def menu_principal():

    while True:
        print("\n" + "="*50)
        print("SISTEMA DE GESTIÓN DE MASCOTAS")
        print("="*50)
        print("1. Registrar mascota")
        print("2. Mostrar información de la mascota")
        print("3. Ver descripción de la mascota")
        print("4. Salir")
        print("="*50)
        opcion = input("Seleccione una opción (1-4): ").strip()
        if opcion == "1":
            registrar_mascota()
        elif opcion == "2":
            mostrar_informacion()
        elif opcion == "3":
            obtener_descripcion()
        elif opcion == "4":
            print("\n¡Gracias por usar el sistema de gestión de mascotas!")
            print("Hasta luego.")
            break
        else:
            print("\n✗ Opción inválida. Por favor, seleccione una opción del 1 al 4.")

def main():
    print("\n╔════════════════════════════════════════════════════╗")
    print("  ║    BIENVENIDO AL SISTEMA DE GESTIÓN DE MASCOTAS    ║")
    print("  ║         Programación Tradicional en Python         ║")
    print("  ╚════════════════════════════════════════════════════╝")
    menu_principal()
if __name__ == "__main__":
    main()
