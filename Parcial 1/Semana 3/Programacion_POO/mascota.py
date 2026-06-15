class Mascota:

    def __init__(self, nombre, especie, edad):

        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        print("\n" + "="*50)
        print("INFORMACIÓN DE LA MASCOTA")
        print("="*50)
        print(f"Nombre:        {self.nombre}")
        print(f"Especie:       {self.especie}")
        print(f"Edad:          {self.edad} años")
        print("="*50)

    def hacer_sonido(self):
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

