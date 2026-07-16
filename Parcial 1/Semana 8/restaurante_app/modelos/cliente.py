class Cliente:
    """
    Representa la entidad Cliente.
    Atributos:
        identificacion: id única (str)
        nombre: nombre del cliente (str)
        correo: email (str)
    """

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion.strip()
        self.nombre: str = nombre.strip()
        self.correo: str = correo.strip()

    def mostrar_informacion(self) -> str:
        return f"ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"

