# ========================================
# CLASE MASCOTA - PROGRAMACIÓN ORIENTADA A OBJETOS
# ========================================

class Mascota:

    def __init__(self, nombre, especie, edad):
        """
        Constructor de la clase Mascota.

        Args:
            nombre (str): El nombre de la mascota
            especie (str): La especie de la mascota
            edad (int): La edad de la mascota
        """
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        """
        Método que muestra la información de la mascota.
        """
        print("\n" + "="*50)
        print("INFORMACIÓN DE LA MASCOTA")
        print("="*50)
        print(f"Nombre:        {self.nombre}")
        print(f"Especie:       {self.especie}")
        print(f"Edad:          {self.edad} años")
        print("="*50)

    def hacer_sonido(self):
        """
        Método que simula el sonido de la mascota según su especie.
        """
        sonidos = {
            "perro": "¡Guau guau!",
            "gato": "¡Miau miau!",
            "pajaro": "¡Pío pío!",
            "hamster": "¡Chis chis!",
            "conejo": "¡Croc croc!",
            "reptil": "¡Sssss!"
        }

        especie_lower = self.especie.lower()
        sonido = sonidos.get(especie_lower, "¡Hace un sonido misterioso!")

        print(f"\n{self.nombre} hace: {sonido}")

