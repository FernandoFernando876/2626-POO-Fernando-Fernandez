# Módulo: cliente.py
# Descripción: Define la clase Cliente que representa un cliente registrado en el restaurante

class Cliente:
    """
    Clase que representa un cliente registrado en el sistema del restaurante.
    
    Atributos:
        id_cliente (int): Identificador único del cliente
        nombre_completo (str): Nombre completo del cliente
        email (str): Correo electrónico del cliente
        telefono (str): Número de teléfono del cliente
        activo (bool): Estado activo o inactivo del cliente en el sistema
    """
    
    def __init__(self, id_cliente: int, nombre_completo: str, email: str, telefono: str, activo: bool = True):
        """
        Constructor de la clase Cliente.
        
        Args:
            id_cliente: Identificador único del cliente
            nombre_completo: Nombre completo del cliente
            email: Correo electrónico del cliente
            telefono: Número de teléfono del cliente
            activo: Estado del cliente (por defecto True)
        """
        self.id_cliente = id_cliente
        self.nombre_completo = nombre_completo
        self.email = email
        self.telefono = telefono
        self.activo = activo
    
    def obtener_estado(self) -> str:
        """Retorna el estado actual del cliente."""
        return "Activo" if self.activo else "Inactivo"
    
    def cambiar_estado(self, activo: bool) -> None:
        """Cambia el estado del cliente."""
        self.activo = activo
    
    def obtener_datos_contacto(self) -> str:
        """Retorna los datos de contacto del cliente."""
        return f"Email: {self.email} | Teléfono: {self.telefono}"
    
    def __str__(self) -> str:
        """Representación en texto de un Cliente."""
        return (
            f"[{self.id_cliente}] {self.nombre_completo}\n"
            f"  {self.obtener_datos_contacto()}\n"
            f"  Estado: {self.obtener_estado()}"
        )

